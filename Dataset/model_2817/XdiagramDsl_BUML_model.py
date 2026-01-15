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
AnchorDirection: Enumeration = Enumeration(
    name="AnchorDirection",
    literals={
            EnumerationLiteral(name="INCOMING"),
			EnumerationLiteral(name="OUTGOING")
    }
)

DefaultColor: Enumeration = Enumeration(
    name="DefaultColor",
    literals={
            EnumerationLiteral(name="MAROON"),
			EnumerationLiteral(name="YELLOW"),
			EnumerationLiteral(name="OLIVE"),
			EnumerationLiteral(name="LIME"),
			EnumerationLiteral(name="GREEN"),
			EnumerationLiteral(name="AQUA"),
			EnumerationLiteral(name="WHITE"),
			EnumerationLiteral(name="TEAL"),
			EnumerationLiteral(name="SILVER"),
			EnumerationLiteral(name="BLUE"),
			EnumerationLiteral(name="GRAY"),
			EnumerationLiteral(name="NAVY"),
			EnumerationLiteral(name="BLACK"),
			EnumerationLiteral(name="FUCHSIA"),
			EnumerationLiteral(name="RED"),
			EnumerationLiteral(name="PURPLE")
    }
)

Operator: Enumeration = Enumeration(
    name="Operator",
    literals={
            EnumerationLiteral(name="EQUAL"),
			EnumerationLiteral(name="DIFFERENT")
    }
)

BooleanLiteral: Enumeration = Enumeration(
    name="BooleanLiteral",
    literals={
            EnumerationLiteral(name="TRUE"),
			EnumerationLiteral(name="FALSE")
    }
)

TextAlignValue: Enumeration = Enumeration(
    name="TextAlignValue",
    literals={
            EnumerationLiteral(name="CENTER"),
			EnumerationLiteral(name="RIGHT"),
			EnumerationLiteral(name="LEFT")
    }
)

LineType: Enumeration = Enumeration(
    name="LineType",
    literals={
            EnumerationLiteral(name="SOLID"),
			EnumerationLiteral(name="DASH"),
			EnumerationLiteral(name="DOT")
    }
)

# Classes
model_ImportStatement = Class(name="model::ImportStatement")
model_EClass = Class(name="model::EClass")
model_XDiagram = Class(name="model::XDiagram")
model_MetaModel = Class(name="model::MetaModel")
model_Diagram = Class(name="model::Diagram")
model_Colors = Class(name="model::Colors")
model_DiagramElement = Class(name="model::DiagramElement")
model_CustomFigure = Class(name="model::CustomFigure")
model_Value = Class(name="model::Value")
model_Node = Class(name="model::Node")
DiagramElement = Class(name="DiagramElement")
model_ConnectableElement = Class(name="model::ConnectableElement")
model_Contains = Class(name="model::Contains")
model_Feature = Class(name="model::Feature")
model_FeatureConditional = Class(name="model::FeatureConditional")
model_FeatureContainer = Class(name="model::FeatureContainer")
model_EAttribute = Class(name="model::EAttribute")
model_Link = Class(name="model::Link")
FeatureContainer = Class(name="FeatureContainer")
model_CustomColor = Class(name="model::CustomColor")
model_EReference = Class(name="model::EReference")
model_Decorator = Class(name="model::Decorator")
model_Anchor = Class(name="model::Anchor")
Feature = Class(name="Feature")
model_Color = Class(name="model::Color")
model_Rhombus = Class(name="model::Rhombus")
model_Custom = Class(name="model::Custom")
ConnectableElement = Class(name="ConnectableElement")
model_Rectangle = Class(name="model::Rectangle")
model_DoubleValue = Class(name="model::DoubleValue")
model_Ellipse = Class(name="model::Ellipse")
model_Polyline = Class(name="model::Polyline")
model_Triangle = Class(name="model::Triangle")
model_Line = Class(name="model::Line")
model_Arrow = Class(name="model::Arrow")
model_IntValue = Class(name="model::IntValue")
Value = Class(name="Value")
model_StringValue = Class(name="model::StringValue")
model_BooleanValue = Class(name="model::BooleanValue")
model_EnumValue = Class(name="model::EnumValue")
model_Label = Class(name="model::Label")
model_Image = Class(name="model::Image")
model_Invisible = Class(name="model::Invisible")
model_ColorFeature = Class(name="model::ColorFeature")
model_Transparency = Class(name="model::Transparency")
model_Visible = Class(name="model::Visible")
model_Size = Class(name="model::Size")
model_Point = Class(name="model::Point")
model_Position = Class(name="model::Position")
model_Corner = Class(name="model::Corner")
model_Layout = Class(name="model::Layout")
model_TextValue = Class(name="model::TextValue")
model_TextPart = Class(name="model::TextPart")
model_FontProperties = Class(name="model::FontProperties")
model_TextAlign = Class(name="model::TextAlign")
model_LineStyle = Class(name="model::LineStyle")
model_LineWidth = Class(name="model::LineWidth")

# model_ImportStatement class attributes and methods
model_ImportStatement_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
model_ImportStatement.attributes={model_ImportStatement_importedNamespace}

# model_EClass class attributes and methods

# model_XDiagram class attributes and methods

# model_MetaModel class attributes and methods
model_MetaModel_plugin: Property = Property(name="plugin", type=StringType)
model_MetaModel_ecorePath: Property = Property(name="ecorePath", type=StringType)
model_MetaModel.attributes={model_MetaModel_ecorePath, model_MetaModel_plugin}

# model_Diagram class attributes and methods

# model_Colors class attributes and methods

# model_DiagramElement class attributes and methods

# model_CustomFigure class attributes and methods
model_CustomFigure_name: Property = Property(name="name", type=StringType)
model_CustomFigure.attributes={model_CustomFigure_name}

# model_Value class attributes and methods

# model_Node class attributes and methods

# DiagramElement class attributes and methods

# model_ConnectableElement class attributes and methods

# model_Contains class attributes and methods

# model_Feature class attributes and methods

# model_FeatureConditional class attributes and methods
model_FeatureConditional_operator: Property = Property(name="operator", type=StringType)
model_FeatureConditional.attributes={model_FeatureConditional_operator}

# model_FeatureContainer class attributes and methods

# model_EAttribute class attributes and methods

# model_Link class attributes and methods
model_Link_reference: Property = Property(name="reference", type=BooleanType)
model_Link_complex: Property = Property(name="complex", type=BooleanType)
model_Link.attributes={model_Link_reference, model_Link_complex}

# FeatureContainer class attributes and methods

# model_CustomColor class attributes and methods
model_CustomColor_name: Property = Property(name="name", type=StringType)
model_CustomColor_R: Property = Property(name="R", type=IntegerType)
model_CustomColor_G: Property = Property(name="G", type=IntegerType)
model_CustomColor_B: Property = Property(name="B", type=IntegerType)
model_CustomColor.attributes={model_CustomColor_B, model_CustomColor_G, model_CustomColor_name, model_CustomColor_R}

# model_EReference class attributes and methods

# model_Decorator class attributes and methods

# model_Anchor class attributes and methods
model_Anchor_direction: Property = Property(name="direction", type=StringType)
model_Anchor_max: Property = Property(name="max", type=IntegerType)
model_Anchor.attributes={model_Anchor_direction, model_Anchor_max}

# Feature class attributes and methods

# model_Color class attributes and methods
model_Color_default: Property = Property(name="default", type=StringType)
model_Color.attributes={model_Color_default}

# model_Rhombus class attributes and methods

# model_Custom class attributes and methods

# ConnectableElement class attributes and methods

# model_Rectangle class attributes and methods
model_Rectangle_square: Property = Property(name="square", type=BooleanType)
model_Rectangle_rectangle: Property = Property(name="rectangle", type=BooleanType)
model_Rectangle.attributes={model_Rectangle_square, model_Rectangle_rectangle}

# model_DoubleValue class attributes and methods
model_DoubleValue_valueInt: Property = Property(name="valueInt", type=IntegerType)
model_DoubleValue_valueDecimal: Property = Property(name="valueDecimal", type=IntegerType)
model_DoubleValue.attributes={model_DoubleValue_valueInt, model_DoubleValue_valueDecimal}

# model_Ellipse class attributes and methods
model_Ellipse_ellipse: Property = Property(name="ellipse", type=BooleanType)
model_Ellipse_circle: Property = Property(name="circle", type=BooleanType)
model_Ellipse.attributes={model_Ellipse_circle, model_Ellipse_ellipse}

# model_Polyline class attributes and methods
model_Polyline_polygon: Property = Property(name="polygon", type=BooleanType)
model_Polyline_polyline: Property = Property(name="polyline", type=BooleanType)
model_Polyline.attributes={model_Polyline_polyline, model_Polyline_polygon}

# model_Triangle class attributes and methods

# model_Line class attributes and methods
model_Line_horizontal: Property = Property(name="horizontal", type=BooleanType)
model_Line_vertical: Property = Property(name="vertical", type=BooleanType)
model_Line.attributes={model_Line_horizontal, model_Line_vertical}

# model_Arrow class attributes and methods

# model_IntValue class attributes and methods
model_IntValue_value: Property = Property(name="value", type=IntegerType)
model_IntValue.attributes={model_IntValue_value}

# Value class attributes and methods

# model_StringValue class attributes and methods
model_StringValue_null: Property = Property(name="null", type=BooleanType)
model_StringValue_value: Property = Property(name="value", type=StringType)
model_StringValue.attributes={model_StringValue_value, model_StringValue_null}

# model_BooleanValue class attributes and methods
model_BooleanValue_value: Property = Property(name="value", type=StringType)
model_BooleanValue.attributes={model_BooleanValue_value}

# model_EnumValue class attributes and methods
model_EnumValue_name: Property = Property(name="name", type=StringType)
model_EnumValue.attributes={model_EnumValue_name}

# model_Label class attributes and methods

# model_Image class attributes and methods
model_Image_imageId: Property = Property(name="imageId", type=StringType)
model_Image.attributes={model_Image_imageId}

# model_Invisible class attributes and methods

# model_ColorFeature class attributes and methods
model_ColorFeature_type: Property = Property(name="type", type=StringType)
model_ColorFeature.attributes={model_ColorFeature_type}

# model_Transparency class attributes and methods
model_Transparency_percent: Property = Property(name="percent", type=IntegerType)
model_Transparency.attributes={model_Transparency_percent}

# model_Visible class attributes and methods

# model_Size class attributes and methods
model_Size_width: Property = Property(name="width", type=IntegerType)
model_Size_widthRelative: Property = Property(name="widthRelative", type=BooleanType)
model_Size_height: Property = Property(name="height", type=IntegerType)
model_Size_heightRelative: Property = Property(name="heightRelative", type=BooleanType)
model_Size_resizable: Property = Property(name="resizable", type=BooleanType)
model_Size.attributes={model_Size_widthRelative, model_Size_height, model_Size_resizable, model_Size_width, model_Size_heightRelative}

# model_Point class attributes and methods
model_Point_x: Property = Property(name="x", type=IntegerType)
model_Point_y: Property = Property(name="y", type=IntegerType)
model_Point.attributes={model_Point_y, model_Point_x}

# model_Position class attributes and methods
model_Position_x: Property = Property(name="x", type=IntegerType)
model_Position_xRelative: Property = Property(name="xRelative", type=BooleanType)
model_Position_y: Property = Property(name="y", type=IntegerType)
model_Position_yRelative: Property = Property(name="yRelative", type=BooleanType)
model_Position.attributes={model_Position_xRelative, model_Position_x, model_Position_yRelative, model_Position_y}

# model_Corner class attributes and methods
model_Corner_angle: Property = Property(name="angle", type=IntegerType)
model_Corner.attributes={model_Corner_angle}

# model_Layout class attributes and methods
model_Layout_vertical: Property = Property(name="vertical", type=BooleanType)
model_Layout_horizontal: Property = Property(name="horizontal", type=BooleanType)
model_Layout_margin: Property = Property(name="margin", type=IntegerType)
model_Layout.attributes={model_Layout_vertical, model_Layout_horizontal, model_Layout_margin}

# model_TextValue class attributes and methods

# model_TextPart class attributes and methods
model_TextPart_text: Property = Property(name="text", type=StringType)
model_TextPart_editable: Property = Property(name="editable", type=BooleanType)
model_TextPart.attributes={model_TextPart_editable, model_TextPart_text}

# model_FontProperties class attributes and methods
model_FontProperties_face: Property = Property(name="face", type=StringType)
model_FontProperties_size: Property = Property(name="size", type=IntegerType)
model_FontProperties_bold: Property = Property(name="bold", type=BooleanType)
model_FontProperties_italics: Property = Property(name="italics", type=BooleanType)
model_FontProperties.attributes={model_FontProperties_italics, model_FontProperties_size, model_FontProperties_bold, model_FontProperties_face}

# model_TextAlign class attributes and methods
model_TextAlign_value: Property = Property(name="value", type=StringType)
model_TextAlign.attributes={model_TextAlign_value}

# model_LineStyle class attributes and methods
model_LineStyle_style: Property = Property(name="style", type=StringType)
model_LineStyle_manhattan: Property = Property(name="manhattan", type=BooleanType)
model_LineStyle.attributes={model_LineStyle_style, model_LineStyle_manhattan}

# model_LineWidth class attributes and methods
model_LineWidth_width: Property = Property(name="width", type=IntegerType)
model_LineWidth.attributes={model_LineWidth_width}

# Relationships
metamodel0: BinaryAssociation = BinaryAssociation(
    name="metamodel0",
    ends={
        Property(name="model_MetaModel", type=model_XDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="model_XDiagram", type=model_MetaModel, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
diagram1: BinaryAssociation = BinaryAssociation(
    name="diagram1",
    ends={
        Property(name="model_Diagram", type=model_XDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="model_XDiagram2", type=model_Diagram, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
customColors3: BinaryAssociation = BinaryAssociation(
    name="customColors3",
    ends={
        Property(name="model_Colors", type=model_XDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="model_XDiagram4", type=model_Colors, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elements5: BinaryAssociation = BinaryAssociation(
    name="elements5",
    ends={
        Property(name="model_DiagramElement", type=model_XDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="model_XDiagram6", type=model_DiagramElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
figures7: BinaryAssociation = BinaryAssociation(
    name="figures7",
    ends={
        Property(name="model_CustomFigure", type=model_XDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="model_XDiagram8", type=model_CustomFigure, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value21: BinaryAssociation = BinaryAssociation(
    name="value21",
    ends={
        Property(name="model_Value", type=model_FeatureConditional, multiplicity=Multiplicity(1, 1)),
        Property(name="model_FeatureConditional22", type=model_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rootFigure23: BinaryAssociation = BinaryAssociation(
    name="rootFigure23",
    ends={
        Property(name="model_ConnectableElement", type=model_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Node", type=model_ConnectableElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modelClass9: BinaryAssociation = BinaryAssociation(
    name="modelClass9",
    ends={
        Property(name="model_EClass", type=model_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Diagram10", type=model_EClass, multiplicity=Multiplicity(0, 1))
    }
)
contains11: BinaryAssociation = BinaryAssociation(
    name="contains11",
    ends={
        Property(name="model_Contains", type=model_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Diagram12", type=model_Contains, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modelClass13: BinaryAssociation = BinaryAssociation(
    name="modelClass13",
    ends={
        Property(name="model_EClass15", type=model_DiagramElement, multiplicity=Multiplicity(1, 1)),
        Property(name="model_DiagramElement14", type=model_EClass, multiplicity=Multiplicity(0, 1))
    }
)
conditional16: BinaryAssociation = BinaryAssociation(
    name="conditional16",
    ends={
        Property(name="model_FeatureConditional", type=model_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Feature", type=model_FeatureConditional, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
features17: BinaryAssociation = BinaryAssociation(
    name="features17",
    ends={
        Property(name="model_Feature18", type=model_FeatureContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="model_FeatureContainer", type=model_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modelAttribute19: BinaryAssociation = BinaryAssociation(
    name="modelAttribute19",
    ends={
        Property(name="model_EAttribute", type=model_FeatureConditional, multiplicity=Multiplicity(1, 1)),
        Property(name="model_FeatureConditional20", type=model_EAttribute, multiplicity=Multiplicity(0, 1))
    }
)
modelReference36: BinaryAssociation = BinaryAssociation(
    name="modelReference36",
    ends={
        Property(name="model_EReference37", type=model_Anchor, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Anchor", type=model_EReference, multiplicity=Multiplicity(0, 1))
    }
)
colors38: BinaryAssociation = BinaryAssociation(
    name="colors38",
    ends={
        Property(name="model_CustomColor", type=model_Colors, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Colors39", type=model_CustomColor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modelReference24: BinaryAssociation = BinaryAssociation(
    name="modelReference24",
    ends={
        Property(name="model_EReference", type=model_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Link", type=model_EReference, multiplicity=Multiplicity(0, 1))
    }
)
sourceReference25: BinaryAssociation = BinaryAssociation(
    name="sourceReference25",
    ends={
        Property(name="model_EReference27", type=model_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Link26", type=model_EReference, multiplicity=Multiplicity(0, 1))
    }
)
targetReference28: BinaryAssociation = BinaryAssociation(
    name="targetReference28",
    ends={
        Property(name="model_EReference30", type=model_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Link29", type=model_EReference, multiplicity=Multiplicity(0, 1))
    }
)
decorators31: BinaryAssociation = BinaryAssociation(
    name="decorators31",
    ends={
        Property(name="model_Decorator", type=model_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Link32", type=model_Decorator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
element33: BinaryAssociation = BinaryAssociation(
    name="element33",
    ends={
        Property(name="model_FeatureContainer35", type=model_Decorator, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Decorator34", type=model_FeatureContainer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
custom40: BinaryAssociation = BinaryAssociation(
    name="custom40",
    ends={
        Property(name="model_CustomColor41", type=model_Color, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Color", type=model_CustomColor, multiplicity=Multiplicity(0, 1))
    }
)
children42: BinaryAssociation = BinaryAssociation(
    name="children42",
    ends={
        Property(name="model_FeatureContainer44", type=model_ConnectableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ConnectableElement43", type=model_FeatureContainer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
element45: BinaryAssociation = BinaryAssociation(
    name="element45",
    ends={
        Property(name="model_ConnectableElement47", type=model_CustomFigure, multiplicity=Multiplicity(1, 1)),
        Property(name="model_CustomFigure46", type=model_ConnectableElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
figure48: BinaryAssociation = BinaryAssociation(
    name="figure48",
    ends={
        Property(name="model_CustomFigure49", type=model_Custom, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Custom", type=model_CustomFigure, multiplicity=Multiplicity(0, 1))
    }
)
modelReference50: BinaryAssociation = BinaryAssociation(
    name="modelReference50",
    ends={
        Property(name="model_EReference52", type=model_Contains, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Contains51", type=model_EReference, multiplicity=Multiplicity(0, 1))
    }
)
color53: BinaryAssociation = BinaryAssociation(
    name="color53",
    ends={
        Property(name="model_Color54", type=model_ColorFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ColorFeature", type=model_Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parts55: BinaryAssociation = BinaryAssociation(
    name="parts55",
    ends={
        Property(name="model_TextPart", type=model_TextValue, multiplicity=Multiplicity(1, 1)),
        Property(name="model_TextValue", type=model_TextPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modelAttribute56: BinaryAssociation = BinaryAssociation(
    name="modelAttribute56",
    ends={
        Property(name="model_EAttribute58", type=model_TextPart, multiplicity=Multiplicity(1, 1)),
        Property(name="model_TextPart57", type=model_EAttribute, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_model_Node_DiagramElement = Generalization(general=DiagramElement, specific=model_Node)
gen_model_Link_DiagramElement = Generalization(general=DiagramElement, specific=model_Link)
gen_model_Link_FeatureContainer = Generalization(general=FeatureContainer, specific=model_Link)
gen_model_Anchor_Feature = Generalization(general=Feature, specific=model_Anchor)
gen_model_Rhombus_ConnectableElement = Generalization(general=ConnectableElement, specific=model_Rhombus)
gen_model_ConnectableElement_FeatureContainer = Generalization(general=FeatureContainer, specific=model_ConnectableElement)
gen_model_Custom_ConnectableElement = Generalization(general=ConnectableElement, specific=model_Custom)
gen_model_Rectangle_ConnectableElement = Generalization(general=ConnectableElement, specific=model_Rectangle)
gen_model_DoubleValue_Value = Generalization(general=Value, specific=model_DoubleValue)
gen_model_Ellipse_ConnectableElement = Generalization(general=ConnectableElement, specific=model_Ellipse)
gen_model_Polyline_ConnectableElement = Generalization(general=ConnectableElement, specific=model_Polyline)
gen_model_Triangle_ConnectableElement = Generalization(general=ConnectableElement, specific=model_Triangle)
gen_model_Line_FeatureContainer = Generalization(general=FeatureContainer, specific=model_Line)
gen_model_Arrow_FeatureContainer = Generalization(general=FeatureContainer, specific=model_Arrow)
gen_model_Contains_Feature = Generalization(general=Feature, specific=model_Contains)
gen_model_IntValue_Value = Generalization(general=Value, specific=model_IntValue)
gen_model_StringValue_Value = Generalization(general=Value, specific=model_StringValue)
gen_model_BooleanValue_Value = Generalization(general=Value, specific=model_BooleanValue)
gen_model_EnumValue_Value = Generalization(general=Value, specific=model_EnumValue)
gen_model_Label_ConnectableElement = Generalization(general=ConnectableElement, specific=model_Label)
gen_model_Image_ConnectableElement = Generalization(general=ConnectableElement, specific=model_Image)
gen_model_Invisible_ConnectableElement = Generalization(general=ConnectableElement, specific=model_Invisible)
gen_model_ColorFeature_Feature = Generalization(general=Feature, specific=model_ColorFeature)
gen_model_Transparency_Feature = Generalization(general=Feature, specific=model_Transparency)
gen_model_Size_Feature = Generalization(general=Feature, specific=model_Size)
gen_model_Point_Feature = Generalization(general=Feature, specific=model_Point)
gen_model_Position_Feature = Generalization(general=Feature, specific=model_Position)
gen_model_Corner_Feature = Generalization(general=Feature, specific=model_Corner)
gen_model_Layout_Feature = Generalization(general=Feature, specific=model_Layout)
gen_model_Visible_Feature = Generalization(general=Feature, specific=model_Visible)
gen_model_TextValue_Feature = Generalization(general=Feature, specific=model_TextValue)
gen_model_FontProperties_Feature = Generalization(general=Feature, specific=model_FontProperties)
gen_model_TextAlign_Feature = Generalization(general=Feature, specific=model_TextAlign)
gen_model_LineStyle_Feature = Generalization(general=Feature, specific=model_LineStyle)
gen_model_LineWidth_Feature = Generalization(general=Feature, specific=model_LineWidth)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_ImportStatement, model_EClass, model_XDiagram, model_MetaModel, model_Diagram, model_Colors, model_DiagramElement, model_CustomFigure, model_Value, model_Node, DiagramElement, model_ConnectableElement, model_Contains, model_Feature, model_FeatureConditional, model_FeatureContainer, model_EAttribute, model_Link, FeatureContainer, model_CustomColor, model_EReference, model_Decorator, model_Anchor, Feature, model_Color, model_Rhombus, model_Custom, ConnectableElement, model_Rectangle, model_DoubleValue, model_Ellipse, model_Polyline, model_Triangle, model_Line, model_Arrow, model_IntValue, Value, model_StringValue, model_BooleanValue, model_EnumValue, model_Label, model_Image, model_Invisible, model_ColorFeature, model_Transparency, model_Visible, model_Size, model_Point, model_Position, model_Corner, model_Layout, model_TextValue, model_TextPart, model_FontProperties, model_TextAlign, model_LineStyle, model_LineWidth, AnchorDirection, DefaultColor, Operator, BooleanLiteral, TextAlignValue, LineType},
    associations={metamodel0, diagram1, customColors3, elements5, figures7, value21, rootFigure23, modelClass9, contains11, modelClass13, conditional16, features17, modelAttribute19, modelReference36, colors38, modelReference24, sourceReference25, targetReference28, decorators31, element33, custom40, children42, element45, figure48, modelReference50, color53, parts55, modelAttribute56},
    generalizations={gen_model_Node_DiagramElement, gen_model_Link_DiagramElement, gen_model_Link_FeatureContainer, gen_model_Anchor_Feature, gen_model_Rhombus_ConnectableElement, gen_model_ConnectableElement_FeatureContainer, gen_model_Custom_ConnectableElement, gen_model_Rectangle_ConnectableElement, gen_model_DoubleValue_Value, gen_model_Ellipse_ConnectableElement, gen_model_Polyline_ConnectableElement, gen_model_Triangle_ConnectableElement, gen_model_Line_FeatureContainer, gen_model_Arrow_FeatureContainer, gen_model_Contains_Feature, gen_model_IntValue_Value, gen_model_StringValue_Value, gen_model_BooleanValue_Value, gen_model_EnumValue_Value, gen_model_Label_ConnectableElement, gen_model_Image_ConnectableElement, gen_model_Invisible_ConnectableElement, gen_model_ColorFeature_Feature, gen_model_Transparency_Feature, gen_model_Size_Feature, gen_model_Point_Feature, gen_model_Position_Feature, gen_model_Corner_Feature, gen_model_Layout_Feature, gen_model_Visible_Feature, gen_model_TextValue_Feature, gen_model_FontProperties_Feature, gen_model_TextAlign_Feature, gen_model_LineStyle_Feature, gen_model_LineWidth_Feature},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)