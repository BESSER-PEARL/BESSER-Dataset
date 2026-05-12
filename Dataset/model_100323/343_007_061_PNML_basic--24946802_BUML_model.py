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
PNML_IdedElement = Class(name="PNML_IdedElement", is_abstract=True)
PNML_NetElement = Class(name="PNML_NetElement")
IdedElement = Class(name="IdedElement")
PNMLDocument = Class(name="PNMLDocument")
NetContent = Class(name="NetContent")
ToolSpecific = Class(name="ToolSpecific")
NetGraphics = Class(name="NetGraphics")
Name = Class(name="Name")
PNML_NetContent = Class(name="PNML_NetContent", is_abstract=True)
PNML_PNMLDocument = Class(name="PNML_PNMLDocument")
URI = Class(name="URI")
NetElement = Class(name="NetElement")
Arc = Class(name="Arc")
Node = Class(name="Node")
PNML_LabeledElement = Class(name="PNML_LabeledElement", is_abstract=True)
Label = Class(name="Label")
AnnotationGraphics = Class(name="AnnotationGraphics")
PNML_Label = Class(name="PNML_Label")
LabeledElement = Class(name="LabeledElement")
PNML_Name = Class(name="PNML_Name")
PNML_ToolSpecific = Class(name="PNML_ToolSpecific")
AnyElement = Class(name="AnyElement")
PNML_Arc = Class(name="PNML_Arc")
NetContentElement = Class(name="NetContentElement")
EdgeGraphics = Class(name="EdgeGraphics")
Inscription = Class(name="Inscription")
PNML_Node = Class(name="PNML_Node")
PNML_Inscription = Class(name="PNML_Inscription")
PNML_InitialMarking = Class(name="PNML_InitialMarking")
Place = Class(name="Place")
PNML_NetContentElement = Class(name="PNML_NetContentElement", is_abstract=True)
PNML_NodeGraphics = Class(name="PNML_NodeGraphics")
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
Offset = Class(name="Offset")
Font = Class(name="Font")
PNML_Coordinate = Class(name="PNML_Coordinate", is_abstract=True)
PNML_Position = Class(name="PNML_Position")
Coordinate = Class(name="Coordinate")
PNML_AnnotationGraphics = Class(name="PNML_AnnotationGraphics")
PNML_Fill = Class(name="PNML_Fill")
Color = Class(name="Color")
PNML_Line = Class(name="PNML_Line")
PNML_Offset = Class(name="PNML_Offset")
PNML_Dimension = Class(name="PNML_Dimension")
PNML_Font = Class(name="PNML_Font")

# PNML_URI class attributes and methods
PNML_URI_value: Property = Property(name="value", type=StringType)
PNML_URI.attributes={PNML_URI_value}

# PNML_Color class attributes and methods

# PNML_AnyElement class attributes and methods
PNML_AnyElement_name: Property = Property(name="name", type=StringType)
PNML_AnyElement_text: Property = Property(name="text", type=StringType)
PNML_AnyElement.attributes={PNML_AnyElement_name, PNML_AnyElement_text}

# PNML_IdedElement class attributes and methods
PNML_IdedElement_id: Property = Property(name="id", type=StringType)
PNML_IdedElement.attributes={PNML_IdedElement_id}

# PNML_NetElement class attributes and methods

# IdedElement class attributes and methods

# PNMLDocument class attributes and methods

# NetContent class attributes and methods

# ToolSpecific class attributes and methods

# NetGraphics class attributes and methods

# Name class attributes and methods

# PNML_NetContent class attributes and methods

# PNML_PNMLDocument class attributes and methods

# URI class attributes and methods

# NetElement class attributes and methods

# Arc class attributes and methods

# Node class attributes and methods

# PNML_LabeledElement class attributes and methods

# Label class attributes and methods

# AnnotationGraphics class attributes and methods

# PNML_Label class attributes and methods
PNML_Label_text: Property = Property(name="text", type=StringType)
PNML_Label.attributes={PNML_Label_text}

# LabeledElement class attributes and methods

# PNML_Name class attributes and methods

# PNML_ToolSpecific class attributes and methods
PNML_ToolSpecific_tool: Property = Property(name="tool", type=StringType)
PNML_ToolSpecific_version: Property = Property(name="version", type=StringType)
PNML_ToolSpecific.attributes={PNML_ToolSpecific_tool, PNML_ToolSpecific_version}

# AnyElement class attributes and methods

# PNML_Arc class attributes and methods

# NetContentElement class attributes and methods

# EdgeGraphics class attributes and methods

# Inscription class attributes and methods

# PNML_Node class attributes and methods

# PNML_Inscription class attributes and methods

# PNML_InitialMarking class attributes and methods

# Place class attributes and methods

# PNML_NetContentElement class attributes and methods

# PNML_NodeGraphics class attributes and methods

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

# Offset class attributes and methods

# Font class attributes and methods

# PNML_Coordinate class attributes and methods
PNML_Coordinate_x: Property = Property(name="x", type=StringType)
PNML_Coordinate_y: Property = Property(name="y", type=StringType)
PNML_Coordinate.attributes={PNML_Coordinate_x, PNML_Coordinate_y}

# PNML_Position class attributes and methods

# Coordinate class attributes and methods

# PNML_AnnotationGraphics class attributes and methods

# PNML_Fill class attributes and methods
PNML_Fill_gradientrotation: Property = Property(name="gradientrotation", type=StringType)
PNML_Fill.attributes={PNML_Fill_gradientrotation}

# Color class attributes and methods

# PNML_Line class attributes and methods
PNML_Line_width: Property = Property(name="width", type=StringType)
PNML_Line_shape: Property = Property(name="shape", type=StringType)
PNML_Line_style: Property = Property(name="style", type=StringType)
PNML_Line.attributes={PNML_Line_width, PNML_Line_style, PNML_Line_shape}

# PNML_Offset class attributes and methods

# PNML_Dimension class attributes and methods
PNML_Dimension_width: Property = Property(name="width", type=StringType)
PNML_Dimension_height: Property = Property(name="height", type=StringType)
PNML_Dimension.attributes={PNML_Dimension_height, PNML_Dimension_width}

# PNML_Font class attributes and methods
PNML_Font_weight: Property = Property(name="weight", type=StringType)
PNML_Font_size: Property = Property(name="size", type=StringType)
PNML_Font_decoration: Property = Property(name="decoration", type=StringType)
PNML_Font_align: Property = Property(name="align", type=StringType)
PNML_Font_rotation: Property = Property(name="rotation", type=StringType)
PNML_Font_family: Property = Property(name="family", type=StringType)
PNML_Font_style: Property = Property(name="style", type=StringType)
PNML_Font.attributes={PNML_Font_align, PNML_Font_size, PNML_Font_decoration, PNML_Font_style, PNML_Font_rotation, PNML_Font_family, PNML_Font_weight}

# Relationships
type2: BinaryAssociation = BinaryAssociation(
    name="type2",
    ends={
        Property(name="URI3", type=PNML_NetElement, multiplicity=Multiplicity(1, 1)),
        Property(name="PNML_NetElement", type=URI, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
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
arc19: BinaryAssociation = BinaryAssociation(
    name="arc19",
    ends={
        Property(name="Arc", type=PNML_ToolSpecific, multiplicity=Multiplicity(1, 1)),
        Property(name="tools20", type=Arc, multiplicity=Multiplicity(0, 1))
    }
)
node21: BinaryAssociation = BinaryAssociation(
    name="node21",
    ends={
        Property(name="Node", type=PNML_ToolSpecific, multiplicity=Multiplicity(1, 1)),
        Property(name="tools22", type=Node, multiplicity=Multiplicity(0, 1))
    }
)
labels23: BinaryAssociation = BinaryAssociation(
    name="labels23",
    ends={
        Property(name="Label", type=PNML_LabeledElement, multiplicity=Multiplicity(1, 1)),
        Property(name="namedelement", type=Label, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotationgraphics24: BinaryAssociation = BinaryAssociation(
    name="annotationgraphics24",
    ends={
        Property(name="AnnotationGraphics", type=PNML_LabeledElement, multiplicity=Multiplicity(1, 1)),
        Property(name="namedelement25", type=AnnotationGraphics, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
namedelement26: BinaryAssociation = BinaryAssociation(
    name="namedelement26",
    ends={
        Property(name="LabeledElement", type=PNML_Label, multiplicity=Multiplicity(1, 1)),
        Property(name="labels", type=LabeledElement, multiplicity=Multiplicity(1, 1))
    }
)
net27: BinaryAssociation = BinaryAssociation(
    name="net27",
    ends={
        Property(name="NetElement28", type=PNML_Name, multiplicity=Multiplicity(1, 1)),
        Property(name="name", type=NetElement, multiplicity=Multiplicity(0, 1))
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
anyelement16: BinaryAssociation = BinaryAssociation(
    name="anyelement16",
    ends={
        Property(name="AnyElement", type=PNML_ToolSpecific, multiplicity=Multiplicity(1, 1)),
        Property(name="PNML_ToolSpecific", type=AnyElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
net17: BinaryAssociation = BinaryAssociation(
    name="net17",
    ends={
        Property(name="NetElement18", type=PNML_ToolSpecific, multiplicity=Multiplicity(1, 1)),
        Property(name="tools", type=NetElement, multiplicity=Multiplicity(0, 1))
    }
)
node35: BinaryAssociation = BinaryAssociation(
    name="node35",
    ends={
        Property(name="netcontentelement", type=Node, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Node36", type=PNML_NetContentElement, multiplicity=Multiplicity(1, 1))
    }
)
source37: BinaryAssociation = BinaryAssociation(
    name="source37",
    ends={
        Property(name="NetContentElement", type=PNML_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="PNML_Arc", type=NetContentElement, multiplicity=Multiplicity(1, 1))
    }
)
target38: BinaryAssociation = BinaryAssociation(
    name="target38",
    ends={
        Property(name="NetContentElement40", type=PNML_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="PNML_Arc39", type=NetContentElement, multiplicity=Multiplicity(1, 1))
    }
)
tools41: BinaryAssociation = BinaryAssociation(
    name="tools41",
    ends={
        Property(name="ToolSpecific42", type=PNML_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="arc", type=ToolSpecific, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edgegraphics43: BinaryAssociation = BinaryAssociation(
    name="edgegraphics43",
    ends={
        Property(name="EdgeGraphics", type=PNML_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="arc44", type=EdgeGraphics, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inscription45: BinaryAssociation = BinaryAssociation(
    name="inscription45",
    ends={
        Property(name="Inscription", type=PNML_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="arc46", type=Inscription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
netcontentelement47: BinaryAssociation = BinaryAssociation(
    name="netcontentelement47",
    ends={
        Property(name="NetContentElement48", type=PNML_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="node", type=NetContentElement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
netcontent29: BinaryAssociation = BinaryAssociation(
    name="netcontent29",
    ends={
        Property(name="NetContent31", type=PNML_Name, multiplicity=Multiplicity(1, 1)),
        Property(name="name30", type=NetContent, multiplicity=Multiplicity(0, 1))
    }
)
arc32: BinaryAssociation = BinaryAssociation(
    name="arc32",
    ends={
        Property(name="Arc33", type=PNML_Inscription, multiplicity=Multiplicity(1, 1)),
        Property(name="inscription", type=Arc, multiplicity=Multiplicity(1, 1))
    }
)
place34: BinaryAssociation = BinaryAssociation(
    name="place34",
    ends={
        Property(name="Place", type=PNML_InitialMarking, multiplicity=Multiplicity(1, 1)),
        Property(name="initialmarking", type=Place, multiplicity=Multiplicity(1, 1))
    }
)
net55: BinaryAssociation = BinaryAssociation(
    name="net55",
    ends={
        Property(name="NetElement56", type=PNML_NetGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="netgraphics", type=NetElement, multiplicity=Multiplicity(1, 1))
    }
)
node57: BinaryAssociation = BinaryAssociation(
    name="node57",
    ends={
        Property(name="Node58", type=PNML_NodeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="nodegraphics", type=Node, multiplicity=Multiplicity(1, 1))
    }
)
position59: BinaryAssociation = BinaryAssociation(
    name="position59",
    ends={
        Property(name="Position", type=PNML_NodeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="nodegraphics60", type=Position, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dimension61: BinaryAssociation = BinaryAssociation(
    name="dimension61",
    ends={
        Property(name="Dimension", type=PNML_NodeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="nodegraphics62", type=Dimension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fill63: BinaryAssociation = BinaryAssociation(
    name="fill63",
    ends={
        Property(name="Fill", type=PNML_NodeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="nodegraphics64", type=Fill, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
line65: BinaryAssociation = BinaryAssociation(
    name="line65",
    ends={
        Property(name="Line", type=PNML_NodeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="nodegraphics66", type=Line, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tools49: BinaryAssociation = BinaryAssociation(
    name="tools49",
    ends={
        Property(name="ToolSpecific51", type=PNML_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="node50", type=ToolSpecific, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodegraphics52: BinaryAssociation = BinaryAssociation(
    name="nodegraphics52",
    ends={
        Property(name="NodeGraphics", type=PNML_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="node53", type=NodeGraphics, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initialmarking54: BinaryAssociation = BinaryAssociation(
    name="initialmarking54",
    ends={
        Property(name="InitialMarking", type=PNML_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="place", type=InitialMarking, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
offset80: BinaryAssociation = BinaryAssociation(
    name="offset80",
    ends={
        Property(name="Offset", type=PNML_AnnotationGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="annotationgraphics81", type=Offset, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
font82: BinaryAssociation = BinaryAssociation(
    name="font82",
    ends={
        Property(name="Font", type=PNML_AnnotationGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="annotationgraphics83", type=Font, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fill84: BinaryAssociation = BinaryAssociation(
    name="fill84",
    ends={
        Property(name="Fill86", type=PNML_AnnotationGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="annotationgraphics85", type=Fill, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
line87: BinaryAssociation = BinaryAssociation(
    name="line87",
    ends={
        Property(name="Line89", type=PNML_AnnotationGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="annotationgraphics88", type=Line, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nodegraphics90: BinaryAssociation = BinaryAssociation(
    name="nodegraphics90",
    ends={
        Property(name="NodeGraphics91", type=PNML_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="position", type=NodeGraphics, multiplicity=Multiplicity(0, 1))
    }
)
edgegraphics92: BinaryAssociation = BinaryAssociation(
    name="edgegraphics92",
    ends={
        Property(name="EdgeGraphics94", type=PNML_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="position93", type=EdgeGraphics, multiplicity=Multiplicity(0, 1))
    }
)
arc67: BinaryAssociation = BinaryAssociation(
    name="arc67",
    ends={
        Property(name="Arc68", type=PNML_EdgeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="edgegraphics", type=Arc, multiplicity=Multiplicity(1, 1))
    }
)
position69: BinaryAssociation = BinaryAssociation(
    name="position69",
    ends={
        Property(name="Position71", type=PNML_EdgeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="edgegraphics70", type=Position, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fill72: BinaryAssociation = BinaryAssociation(
    name="fill72",
    ends={
        Property(name="Fill74", type=PNML_EdgeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="edgegraphics73", type=Fill, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
line75: BinaryAssociation = BinaryAssociation(
    name="line75",
    ends={
        Property(name="Line77", type=PNML_EdgeGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="edgegraphics76", type=Line, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
namedelement78: BinaryAssociation = BinaryAssociation(
    name="namedelement78",
    ends={
        Property(name="LabeledElement79", type=PNML_AnnotationGraphics, multiplicity=Multiplicity(1, 1)),
        Property(name="annotationgraphics", type=LabeledElement, multiplicity=Multiplicity(1, 1))
    }
)
interiorcolor99: BinaryAssociation = BinaryAssociation(
    name="interiorcolor99",
    ends={
        Property(name="Color", type=PNML_Fill, multiplicity=Multiplicity(1, 1)),
        Property(name="PNML_Fill", type=Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
gradientcolor100: BinaryAssociation = BinaryAssociation(
    name="gradientcolor100",
    ends={
        Property(name="Color102", type=PNML_Fill, multiplicity=Multiplicity(1, 1)),
        Property(name="PNML_Fill101", type=Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
image103: BinaryAssociation = BinaryAssociation(
    name="image103",
    ends={
        Property(name="URI105", type=PNML_Fill, multiplicity=Multiplicity(1, 1)),
        Property(name="PNML_Fill104", type=URI, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nodegraphics106: BinaryAssociation = BinaryAssociation(
    name="nodegraphics106",
    ends={
        Property(name="NodeGraphics107", type=PNML_Fill, multiplicity=Multiplicity(1, 1)),
        Property(name="fill", type=NodeGraphics, multiplicity=Multiplicity(0, 1))
    }
)
edgegraphics108: BinaryAssociation = BinaryAssociation(
    name="edgegraphics108",
    ends={
        Property(name="EdgeGraphics110", type=PNML_Fill, multiplicity=Multiplicity(1, 1)),
        Property(name="fill109", type=EdgeGraphics, multiplicity=Multiplicity(0, 1))
    }
)
annotationgraphics111: BinaryAssociation = BinaryAssociation(
    name="annotationgraphics111",
    ends={
        Property(name="AnnotationGraphics113", type=PNML_Fill, multiplicity=Multiplicity(1, 1)),
        Property(name="fill112", type=AnnotationGraphics, multiplicity=Multiplicity(0, 1))
    }
)
color114: BinaryAssociation = BinaryAssociation(
    name="color114",
    ends={
        Property(name="Color115", type=PNML_Line, multiplicity=Multiplicity(1, 1)),
        Property(name="PNML_Line", type=Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotationgraphics95: BinaryAssociation = BinaryAssociation(
    name="annotationgraphics95",
    ends={
        Property(name="AnnotationGraphics96", type=PNML_Offset, multiplicity=Multiplicity(1, 1)),
        Property(name="offset", type=AnnotationGraphics, multiplicity=Multiplicity(1, 1))
    }
)
nodegraphics97: BinaryAssociation = BinaryAssociation(
    name="nodegraphics97",
    ends={
        Property(name="NodeGraphics98", type=PNML_Dimension, multiplicity=Multiplicity(1, 1)),
        Property(name="dimension", type=NodeGraphics, multiplicity=Multiplicity(1, 1))
    }
)
annotationgraphics124: BinaryAssociation = BinaryAssociation(
    name="annotationgraphics124",
    ends={
        Property(name="AnnotationGraphics125", type=PNML_Font, multiplicity=Multiplicity(1, 1)),
        Property(name="font", type=AnnotationGraphics, multiplicity=Multiplicity(1, 1))
    }
)
nodegraphics116: BinaryAssociation = BinaryAssociation(
    name="nodegraphics116",
    ends={
        Property(name="NodeGraphics117", type=PNML_Line, multiplicity=Multiplicity(1, 1)),
        Property(name="line", type=NodeGraphics, multiplicity=Multiplicity(0, 1))
    }
)
edgegraphics118: BinaryAssociation = BinaryAssociation(
    name="edgegraphics118",
    ends={
        Property(name="EdgeGraphics120", type=PNML_Line, multiplicity=Multiplicity(1, 1)),
        Property(name="line119", type=EdgeGraphics, multiplicity=Multiplicity(0, 1))
    }
)
annotationgraphics121: BinaryAssociation = BinaryAssociation(
    name="annotationgraphics121",
    ends={
        Property(name="AnnotationGraphics123", type=PNML_Line, multiplicity=Multiplicity(1, 1)),
        Property(name="line122", type=AnnotationGraphics, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_PNML_NetElement_IdedElement = Generalization(general=IdedElement, specific=PNML_NetElement)
gen_PNML_Name_LabeledElement = Generalization(general=LabeledElement, specific=PNML_Name)
gen_PNML_Arc_NetContent = Generalization(general=NetContent, specific=PNML_Arc)
gen_PNML_Arc_IdedElement = Generalization(general=IdedElement, specific=PNML_Arc)
gen_PNML_Node_IdedElement = Generalization(general=IdedElement, specific=PNML_Node)
gen_PNML_Inscription_LabeledElement = Generalization(general=LabeledElement, specific=PNML_Inscription)
gen_PNML_InitialMarking_LabeledElement = Generalization(general=LabeledElement, specific=PNML_InitialMarking)
gen_PNML_NetContentElement_NetContent = Generalization(general=NetContent, specific=PNML_NetContentElement)
gen_PNML_NetGraphics_Graphics = Generalization(general=Graphics, specific=PNML_NetGraphics)
gen_PNML_NodeGraphics_Graphics = Generalization(general=Graphics, specific=PNML_NodeGraphics)
gen_PNML_EdgeGraphics_Graphics = Generalization(general=Graphics, specific=PNML_EdgeGraphics)
gen_PNML_Place_NetContentElement = Generalization(general=NetContentElement, specific=PNML_Place)
gen_PNML_Transition_NetContentElement = Generalization(general=NetContentElement, specific=PNML_Transition)
gen_PNML_Position_Coordinate = Generalization(general=Coordinate, specific=PNML_Position)
gen_PNML_AnnotationGraphics_Graphics = Generalization(general=Graphics, specific=PNML_AnnotationGraphics)
gen_PNML_Offset_Coordinate = Generalization(general=Coordinate, specific=PNML_Offset)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={PNML_URI, PNML_Color, PNML_AnyElement, PNML_IdedElement, PNML_NetElement, IdedElement, PNMLDocument, NetContent, ToolSpecific, NetGraphics, Name, PNML_NetContent, PNML_PNMLDocument, URI, NetElement, Arc, Node, PNML_LabeledElement, Label, AnnotationGraphics, PNML_Label, LabeledElement, PNML_Name, PNML_ToolSpecific, AnyElement, PNML_Arc, NetContentElement, EdgeGraphics, Inscription, PNML_Node, PNML_Inscription, PNML_InitialMarking, Place, PNML_NetContentElement, PNML_NodeGraphics, Position, Dimension, Fill, Line, PNML_EdgeGraphics, NodeGraphics, PNML_Place, InitialMarking, PNML_Transition, PNML_Graphics, PNML_NetGraphics, Graphics, Offset, Font, PNML_Coordinate, PNML_Position, Coordinate, PNML_AnnotationGraphics, PNML_Fill, Color, PNML_Line, PNML_Offset, PNML_Dimension, PNML_Font, RotationType, ShapeType, StyleType, DecorationType, AlignType},
    associations={type2, document4, contents5, tools6, netgraphics8, name10, xmlns0, nets1, arc19, node21, labels23, annotationgraphics24, namedelement26, net27, net12, name14, anyelement16, net17, node35, source37, target38, tools41, edgegraphics43, inscription45, netcontentelement47, netcontent29, arc32, place34, net55, node57, position59, dimension61, fill63, line65, tools49, nodegraphics52, initialmarking54, offset80, font82, fill84, line87, nodegraphics90, edgegraphics92, arc67, position69, fill72, line75, namedelement78, interiorcolor99, gradientcolor100, image103, nodegraphics106, edgegraphics108, annotationgraphics111, color114, annotationgraphics95, nodegraphics97, annotationgraphics124, nodegraphics116, edgegraphics118, annotationgraphics121},
    generalizations={gen_PNML_NetElement_IdedElement, gen_PNML_Name_LabeledElement, gen_PNML_Arc_NetContent, gen_PNML_Arc_IdedElement, gen_PNML_Node_IdedElement, gen_PNML_Inscription_LabeledElement, gen_PNML_InitialMarking_LabeledElement, gen_PNML_NetContentElement_NetContent, gen_PNML_NetGraphics_Graphics, gen_PNML_NodeGraphics_Graphics, gen_PNML_EdgeGraphics_Graphics, gen_PNML_Place_NetContentElement, gen_PNML_Transition_NetContentElement, gen_PNML_Position_Coordinate, gen_PNML_AnnotationGraphics_Graphics, gen_PNML_Offset_Coordinate},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)