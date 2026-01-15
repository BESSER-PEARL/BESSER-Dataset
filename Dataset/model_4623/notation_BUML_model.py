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
Orientation: Enumeration = Enumeration(
    name="Orientation",
    literals={
            EnumerationLiteral(name="HORIZONTAL"),
			EnumerationLiteral(name="VERTICAL"),
			EnumerationLiteral(name="LEFT_DIAGONAL"),
			EnumerationLiteral(name="RIGHT_DIAGONAL")
    }
)

LineTextureType: Enumeration = Enumeration(
    name="LineTextureType",
    literals={
            EnumerationLiteral(name="INVISIBLE"),
			EnumerationLiteral(name="SOLID"),
			EnumerationLiteral(name="DASH"),
			EnumerationLiteral(name="DOT"),
			EnumerationLiteral(name="DASHDOT"),
			EnumerationLiteral(name="DASHDOTDOT"),
			EnumerationLiteral(name="DOUBLE")
    }
)

Color: Enumeration = Enumeration(
    name="Color",
    literals={
            EnumerationLiteral(name="RED"),
			EnumerationLiteral(name="ORANGE"),
			EnumerationLiteral(name="YELLOW"),
			EnumerationLiteral(name="GREEN"),
			EnumerationLiteral(name="LIGHT_GREEN"),
			EnumerationLiteral(name="DARK_GREEN"),
			EnumerationLiteral(name="CYAN"),
			EnumerationLiteral(name="LIGHT_BLUE"),
			EnumerationLiteral(name="BLUE"),
			EnumerationLiteral(name="DARK_BLUE"),
			EnumerationLiteral(name="WHITE"),
			EnumerationLiteral(name="BLACK"),
			EnumerationLiteral(name="LIGHT_GRAY"),
			EnumerationLiteral(name="GRAY"),
			EnumerationLiteral(name="DARK_GRAY")
    }
)

FillTextureType: Enumeration = Enumeration(
    name="FillTextureType",
    literals={
            EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="STRIP"),
			EnumerationLiteral(name="DASH"),
			EnumerationLiteral(name="DOT"),
			EnumerationLiteral(name="DASHDOT"),
			EnumerationLiteral(name="DASHDOTDOT")
    }
)

DefinitionType: Enumeration = Enumeration(
    name="DefinitionType",
    literals={
            EnumerationLiteral(name="GRAPHICAL"),
			EnumerationLiteral(name="TEXTUAL"),
			EnumerationLiteral(name="HYBRID")
    }
)

Layout: Enumeration = Enumeration(
    name="Layout",
    literals={
            EnumerationLiteral(name="HORIZONTAL"),
			EnumerationLiteral(name="VERTICAL"),
			EnumerationLiteral(name="UNKNOWN")
    }
)

IconType: Enumeration = Enumeration(
    name="IconType",
    literals={
            EnumerationLiteral(name="CROSS"),
			EnumerationLiteral(name="ARROW"),
			EnumerationLiteral(name="LETTER")
    }
)

AudienceType: Enumeration = Enumeration(
    name="AudienceType",
    literals={
            EnumerationLiteral(name="EXPERT"),
			EnumerationLiteral(name="BEGINNER"),
			EnumerationLiteral(name="BOTH")
    }
)

# Classes
notation_Node = Class(name="notation::Node")
DiagramElement = Class(name="DiagramElement")
notation_GraphicalElement = Class(name="notation::GraphicalElement", is_abstract=True)
notation_Relation = Class(name="notation::Relation", is_abstract=True)
notation_Compartment = Class(name="notation::Compartment")
Relation = Class(name="Relation")
notation_Link = Class(name="notation::Link")
notation_NotationDefinition = Class(name="notation::NotationDefinition")
notation_DiagramDefinition = Class(name="notation::DiagramDefinition")
notation_DiagramElement = Class(name="notation::DiagramElement", is_abstract=True)
notation_IDElement = Class(name="notation::IDElement")
IDElement = Class(name="IDElement")
notation_Figure = Class(name="notation::Figure", is_abstract=True)
notation_FigureStyle = Class(name="notation::FigureStyle")
notation_BorderStyle = Class(name="notation::BorderStyle")
notation_FigureContainment = Class(name="notation::FigureContainment")
notation_SyntaxOf = Class(name="notation::SyntaxOf")
GraphicalElement = Class(name="GraphicalElement")
notation_Icon = Class(name="notation::Icon")
notation_IconStyle = Class(name="notation::IconStyle")
notation_Image = Class(name="notation::Image")
notation_Composite = Class(name="notation::Composite")
notation_Label = Class(name="notation::Label")
notation_TextStyle = Class(name="notation::TextStyle")
notation_TextualContainment = Class(name="notation::TextualContainment")
notation_Line = Class(name="notation::Line")
notation_LineStyle = Class(name="notation::LineStyle")
notation_Rectangle = Class(name="notation::Rectangle")
Figure = Class(name="Figure")
notation_Roundtangle = Class(name="notation::Roundtangle")
notation_Square = Class(name="notation::Square")
notation_Diamond = Class(name="notation::Diamond")
notation_Triangle = Class(name="notation::Triangle")
notation_Circle = Class(name="notation::Circle")
notation_Cylinder = Class(name="notation::Cylinder")
notation_Cube = Class(name="notation::Cube")
notation_Polyline = Class(name="notation::Polyline")
notation_Point = Class(name="notation::Point")
notation_TextualElement = Class(name="notation::TextualElement", is_abstract=True)
notation_Token = Class(name="notation::Token")
TextualElement = Class(name="TextualElement")
notation_Keyword = Class(name="notation::Keyword")
notation_Value = Class(name="notation::Value", is_abstract=True)
notation_AttributeValue = Class(name="notation::AttributeValue")
Value = Class(name="Value")
notation_ReferenceValue = Class(name="notation::ReferenceValue")
notation_Style = Class(name="notation::Style", is_abstract=True)
Style = Class(name="Style")

# notation_Node class attributes and methods

# DiagramElement class attributes and methods

# notation_GraphicalElement class attributes and methods

# notation_Relation class attributes and methods

# notation_Compartment class attributes and methods
notation_Compartment_layout: Property = Property(name="layout", type=StringType)
notation_Compartment.attributes={notation_Compartment_layout}

# Relation class attributes and methods

# notation_Link class attributes and methods

# notation_NotationDefinition class attributes and methods
notation_NotationDefinition_Type: Property = Property(name="Type", type=StringType)
notation_NotationDefinition.attributes={notation_NotationDefinition_Type}

# notation_DiagramDefinition class attributes and methods
notation_DiagramDefinition_Legend: Property = Property(name="Legend", type=StringType)
notation_DiagramDefinition_Level: Property = Property(name="Level", type=IntegerType)
notation_DiagramDefinition_allowChunks: Property = Property(name="allowChunks", type=BooleanType)
notation_DiagramDefinition_targetedAudience: Property = Property(name="targetedAudience", type=StringType)
notation_DiagramDefinition.attributes={notation_DiagramDefinition_Level, notation_DiagramDefinition_targetedAudience, notation_DiagramDefinition_allowChunks, notation_DiagramDefinition_Legend}

# notation_DiagramElement class attributes and methods

# notation_IDElement class attributes and methods
notation_IDElement_ID: Property = Property(name="ID", type=StringType)
notation_IDElement.attributes={notation_IDElement_ID}

# IDElement class attributes and methods

# notation_Figure class attributes and methods

# notation_FigureStyle class attributes and methods
notation_FigureStyle_fillTexture: Property = Property(name="fillTexture", type=StringType)
notation_FigureStyle_fillOrientation: Property = Property(name="fillOrientation", type=StringType)
notation_FigureStyle_fillTextureColor: Property = Property(name="fillTextureColor", type=StringType)
notation_FigureStyle_width: Property = Property(name="width", type=FloatType)
notation_FigureStyle_height: Property = Property(name="height", type=FloatType)
notation_FigureStyle_orientation: Property = Property(name="orientation", type=StringType)
notation_FigureStyle_brightness: Property = Property(name="brightness", type=IntegerType)
notation_FigureStyle_fillColor: Property = Property(name="fillColor", type=StringType)
notation_FigureStyle.attributes={notation_FigureStyle_height, notation_FigureStyle_fillTextureColor, notation_FigureStyle_fillOrientation, notation_FigureStyle_brightness, notation_FigureStyle_orientation, notation_FigureStyle_fillColor, notation_FigureStyle_width, notation_FigureStyle_fillTexture}

# notation_BorderStyle class attributes and methods
notation_BorderStyle_thickness: Property = Property(name="thickness", type=FloatType)
notation_BorderStyle_color: Property = Property(name="color", type=StringType)
notation_BorderStyle_texture: Property = Property(name="texture", type=StringType)
notation_BorderStyle.attributes={notation_BorderStyle_color, notation_BorderStyle_thickness, notation_BorderStyle_texture}

# notation_FigureContainment class attributes and methods
notation_FigureContainment_layout: Property = Property(name="layout", type=StringType)
notation_FigureContainment.attributes={notation_FigureContainment_layout}

# notation_SyntaxOf class attributes and methods

# GraphicalElement class attributes and methods

# notation_Icon class attributes and methods
notation_Icon_iconType: Property = Property(name="iconType", type=StringType)
notation_Icon.attributes={notation_Icon_iconType}

# notation_IconStyle class attributes and methods
notation_IconStyle_width: Property = Property(name="width", type=FloatType)
notation_IconStyle_height: Property = Property(name="height", type=FloatType)
notation_IconStyle_orientation: Property = Property(name="orientation", type=StringType)
notation_IconStyle_brightness: Property = Property(name="brightness", type=IntegerType)
notation_IconStyle_color: Property = Property(name="color", type=StringType)
notation_IconStyle.attributes={notation_IconStyle_width, notation_IconStyle_brightness, notation_IconStyle_height, notation_IconStyle_color, notation_IconStyle_orientation}

# notation_Image class attributes and methods
notation_Image_path: Property = Property(name="path", type=StringType)
notation_Image.attributes={notation_Image_path}

# notation_Composite class attributes and methods
notation_Composite_layout: Property = Property(name="layout", type=StringType)
notation_Composite.attributes={notation_Composite_layout}

# notation_Label class attributes and methods

# notation_TextStyle class attributes and methods
notation_TextStyle_fontSize: Property = Property(name="fontSize", type=IntegerType)
notation_TextStyle_fontName: Property = Property(name="fontName", type=StringType)
notation_TextStyle_bold: Property = Property(name="bold", type=BooleanType)
notation_TextStyle_italic: Property = Property(name="italic", type=BooleanType)
notation_TextStyle_underlined: Property = Property(name="underlined", type=BooleanType)
notation_TextStyle_fontColor: Property = Property(name="fontColor", type=StringType)
notation_TextStyle.attributes={notation_TextStyle_fontName, notation_TextStyle_italic, notation_TextStyle_fontSize, notation_TextStyle_underlined, notation_TextStyle_bold, notation_TextStyle_fontColor}

# notation_TextualContainment class attributes and methods
notation_TextualContainment_layout: Property = Property(name="layout", type=StringType)
notation_TextualContainment.attributes={notation_TextualContainment_layout}

# notation_Line class attributes and methods

# notation_LineStyle class attributes and methods
notation_LineStyle_thickness: Property = Property(name="thickness", type=FloatType)
notation_LineStyle_color: Property = Property(name="color", type=StringType)
notation_LineStyle_orientation: Property = Property(name="orientation", type=StringType)
notation_LineStyle_length: Property = Property(name="length", type=FloatType)
notation_LineStyle_brightness: Property = Property(name="brightness", type=IntegerType)
notation_LineStyle_texture: Property = Property(name="texture", type=StringType)
notation_LineStyle.attributes={notation_LineStyle_length, notation_LineStyle_color, notation_LineStyle_thickness, notation_LineStyle_texture, notation_LineStyle_brightness, notation_LineStyle_orientation}

# notation_Rectangle class attributes and methods

# Figure class attributes and methods

# notation_Roundtangle class attributes and methods

# notation_Square class attributes and methods

# notation_Diamond class attributes and methods

# notation_Triangle class attributes and methods

# notation_Circle class attributes and methods

# notation_Cylinder class attributes and methods

# notation_Cube class attributes and methods

# notation_Polyline class attributes and methods

# notation_Point class attributes and methods
notation_Point_x: Property = Property(name="x", type=IntegerType)
notation_Point_y: Property = Property(name="y", type=IntegerType)
notation_Point.attributes={notation_Point_y, notation_Point_x}

# notation_TextualElement class attributes and methods

# notation_Token class attributes and methods

# TextualElement class attributes and methods

# notation_Keyword class attributes and methods

# notation_Value class attributes and methods

# notation_AttributeValue class attributes and methods

# Value class attributes and methods

# notation_ReferenceValue class attributes and methods

# notation_Style class attributes and methods

# Style class attributes and methods

# Relationships
graphicalElement3: BinaryAssociation = BinaryAssociation(
    name="graphicalElement3",
    ends={
        Property(name="notation_GraphicalElement", type=notation_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_Node", type=notation_GraphicalElement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
nodeType4: BinaryAssociation = BinaryAssociation(
    name="nodeType4",
    ends={
        Property(name="notation_Node5", type=notation_Compartment, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_Compartment", type=notation_Node, multiplicity=Multiplicity(0, 1))
    }
)
diagrams0: BinaryAssociation = BinaryAssociation(
    name="diagrams0",
    ends={
        Property(name="notation_DiagramDefinition", type=notation_NotationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_NotationDefinition", type=notation_DiagramDefinition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
elements1: BinaryAssociation = BinaryAssociation(
    name="elements1",
    ends={
        Property(name="notation_DiagramElement", type=notation_DiagramDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_DiagramDefinition2", type=notation_DiagramElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
figureStyle22: BinaryAssociation = BinaryAssociation(
    name="figureStyle22",
    ends={
        Property(name="notation_FigureStyle", type=notation_Figure, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_Figure", type=notation_FigureStyle, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
borderStyle23: BinaryAssociation = BinaryAssociation(
    name="borderStyle23",
    ends={
        Property(name="notation_BorderStyle", type=notation_Figure, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_Figure24", type=notation_BorderStyle, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
figureContainment25: BinaryAssociation = BinaryAssociation(
    name="figureContainment25",
    ends={
        Property(name="notation_FigureContainment", type=notation_Figure, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_Figure26", type=notation_FigureContainment, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elements27: BinaryAssociation = BinaryAssociation(
    name="elements27",
    ends={
        Property(name="notation_GraphicalElement29", type=notation_FigureContainment, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_FigureContainment28", type=notation_GraphicalElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
graphicalElement6: BinaryAssociation = BinaryAssociation(
    name="graphicalElement6",
    ends={
        Property(name="notation_GraphicalElement7", type=notation_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_Link", type=notation_GraphicalElement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referredElement8: BinaryAssociation = BinaryAssociation(
    name="referredElement8",
    ends={
        Property(name="notation_DiagramElement9", type=notation_SyntaxOf, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_SyntaxOf", type=notation_DiagramElement, multiplicity=Multiplicity(1, 1))
    }
)
style10: BinaryAssociation = BinaryAssociation(
    name="style10",
    ends={
        Property(name="notation_IconStyle", type=notation_Icon, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_Icon", type=notation_IconStyle, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
approximateRepresentation11: BinaryAssociation = BinaryAssociation(
    name="approximateRepresentation11",
    ends={
        Property(name="notation_GraphicalElement12", type=notation_Image, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_Image", type=notation_GraphicalElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subElements13: BinaryAssociation = BinaryAssociation(
    name="subElements13",
    ends={
        Property(name="notation_GraphicalElement14", type=notation_Composite, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_Composite", type=notation_GraphicalElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
primaryShape15: BinaryAssociation = BinaryAssociation(
    name="primaryShape15",
    ends={
        Property(name="notation_GraphicalElement17", type=notation_Composite, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_Composite16", type=notation_GraphicalElement, multiplicity=Multiplicity(1, 1))
    }
)
textStyle18: BinaryAssociation = BinaryAssociation(
    name="textStyle18",
    ends={
        Property(name="notation_TextStyle", type=notation_Label, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_Label", type=notation_TextStyle, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
text19: BinaryAssociation = BinaryAssociation(
    name="text19",
    ends={
        Property(name="notation_TextualContainment", type=notation_Label, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_Label20", type=notation_TextualContainment, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lineStyle21: BinaryAssociation = BinaryAssociation(
    name="lineStyle21",
    ends={
        Property(name="notation_LineStyle", type=notation_Line, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_Line", type=notation_LineStyle, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
points30: BinaryAssociation = BinaryAssociation(
    name="points30",
    ends={
        Property(name="notation_Point", type=notation_Polyline, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_Polyline", type=notation_Point, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements31: BinaryAssociation = BinaryAssociation(
    name="elements31",
    ends={
        Property(name="notation_TextualElement", type=notation_TextualContainment, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_TextualContainment32", type=notation_TextualElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_notation_Node_DiagramElement = Generalization(general=DiagramElement, specific=notation_Node)
gen_notation_Relation_DiagramElement = Generalization(general=DiagramElement, specific=notation_Relation)
gen_notation_Compartment_Relation = Generalization(general=Relation, specific=notation_Compartment)
gen_notation_Link_Relation = Generalization(general=Relation, specific=notation_Link)
gen_notation_DiagramElement_IDElement = Generalization(general=IDElement, specific=notation_DiagramElement)
gen_notation_Figure_GraphicalElement = Generalization(general=GraphicalElement, specific=notation_Figure)
gen_notation_GraphicalElement_IDElement = Generalization(general=IDElement, specific=notation_GraphicalElement)
gen_notation_SyntaxOf_GraphicalElement = Generalization(general=GraphicalElement, specific=notation_SyntaxOf)
gen_notation_Icon_GraphicalElement = Generalization(general=GraphicalElement, specific=notation_Icon)
gen_notation_Image_GraphicalElement = Generalization(general=GraphicalElement, specific=notation_Image)
gen_notation_Composite_GraphicalElement = Generalization(general=GraphicalElement, specific=notation_Composite)
gen_notation_Label_GraphicalElement = Generalization(general=GraphicalElement, specific=notation_Label)
gen_notation_Line_GraphicalElement = Generalization(general=GraphicalElement, specific=notation_Line)
gen_notation_IconStyle_Style = Generalization(general=Style, specific=notation_IconStyle)
gen_notation_BorderStyle_Style = Generalization(general=Style, specific=notation_BorderStyle)
gen_notation_Rectangle_Figure = Generalization(general=Figure, specific=notation_Rectangle)
gen_notation_Roundtangle_Figure = Generalization(general=Figure, specific=notation_Roundtangle)
gen_notation_Square_Figure = Generalization(general=Figure, specific=notation_Square)
gen_notation_Diamond_Figure = Generalization(general=Figure, specific=notation_Diamond)
gen_notation_Triangle_Figure = Generalization(general=Figure, specific=notation_Triangle)
gen_notation_Circle_Figure = Generalization(general=Figure, specific=notation_Circle)
gen_notation_Cylinder_Figure = Generalization(general=Figure, specific=notation_Cylinder)
gen_notation_Cube_Figure = Generalization(general=Figure, specific=notation_Cube)
gen_notation_Polyline_Figure = Generalization(general=Figure, specific=notation_Polyline)
gen_notation_TextualElement_IDElement = Generalization(general=IDElement, specific=notation_TextualElement)
gen_notation_Token_TextualElement = Generalization(general=TextualElement, specific=notation_Token)
gen_notation_Keyword_TextualElement = Generalization(general=TextualElement, specific=notation_Keyword)
gen_notation_Value_TextualElement = Generalization(general=TextualElement, specific=notation_Value)
gen_notation_AttributeValue_Value = Generalization(general=Value, specific=notation_AttributeValue)
gen_notation_ReferenceValue_Value = Generalization(general=Value, specific=notation_ReferenceValue)
gen_notation_LineStyle_Style = Generalization(general=Style, specific=notation_LineStyle)
gen_notation_FigureStyle_Style = Generalization(general=Style, specific=notation_FigureStyle)
gen_notation_TextStyle_Style = Generalization(general=Style, specific=notation_TextStyle)

# Domain Model
domain_model = DomainModel(
    name="notation",
    types={notation_Node, DiagramElement, notation_GraphicalElement, notation_Relation, notation_Compartment, Relation, notation_Link, notation_NotationDefinition, notation_DiagramDefinition, notation_DiagramElement, notation_IDElement, IDElement, notation_Figure, notation_FigureStyle, notation_BorderStyle, notation_FigureContainment, notation_SyntaxOf, GraphicalElement, notation_Icon, notation_IconStyle, notation_Image, notation_Composite, notation_Label, notation_TextStyle, notation_TextualContainment, notation_Line, notation_LineStyle, notation_Rectangle, Figure, notation_Roundtangle, notation_Square, notation_Diamond, notation_Triangle, notation_Circle, notation_Cylinder, notation_Cube, notation_Polyline, notation_Point, notation_TextualElement, notation_Token, TextualElement, notation_Keyword, notation_Value, notation_AttributeValue, Value, notation_ReferenceValue, notation_Style, Style, Orientation, LineTextureType, Color, FillTextureType, DefinitionType, Layout, IconType, AudienceType},
    associations={graphicalElement3, nodeType4, diagrams0, elements1, figureStyle22, borderStyle23, figureContainment25, elements27, graphicalElement6, referredElement8, style10, approximateRepresentation11, subElements13, primaryShape15, textStyle18, text19, lineStyle21, points30, elements31},
    generalizations={gen_notation_Node_DiagramElement, gen_notation_Relation_DiagramElement, gen_notation_Compartment_Relation, gen_notation_Link_Relation, gen_notation_DiagramElement_IDElement, gen_notation_Figure_GraphicalElement, gen_notation_GraphicalElement_IDElement, gen_notation_SyntaxOf_GraphicalElement, gen_notation_Icon_GraphicalElement, gen_notation_Image_GraphicalElement, gen_notation_Composite_GraphicalElement, gen_notation_Label_GraphicalElement, gen_notation_Line_GraphicalElement, gen_notation_IconStyle_Style, gen_notation_BorderStyle_Style, gen_notation_Rectangle_Figure, gen_notation_Roundtangle_Figure, gen_notation_Square_Figure, gen_notation_Diamond_Figure, gen_notation_Triangle_Figure, gen_notation_Circle_Figure, gen_notation_Cylinder_Figure, gen_notation_Cube_Figure, gen_notation_Polyline_Figure, gen_notation_TextualElement_IDElement, gen_notation_Token_TextualElement, gen_notation_Keyword_TextualElement, gen_notation_Value_TextualElement, gen_notation_AttributeValue_Value, gen_notation_ReferenceValue_Value, gen_notation_LineStyle_Style, gen_notation_FigureStyle_Style, gen_notation_TextStyle_Style},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)