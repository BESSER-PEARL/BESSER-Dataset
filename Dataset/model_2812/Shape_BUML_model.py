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
CompartmentLayout: Enumeration = Enumeration(
    name="CompartmentLayout",
    literals={
            EnumerationLiteral(name="FIXED"),
			EnumerationLiteral(name="VERTICAL"),
			EnumerationLiteral(name="HORIZONTAL"),
			EnumerationLiteral(name="FIT")
    }
)

HAlign: Enumeration = Enumeration(
    name="HAlign",
    literals={
            EnumerationLiteral(name="LEFT"),
			EnumerationLiteral(name="CENTER"),
			EnumerationLiteral(name="RIGHT")
    }
)

VAlign: Enumeration = Enumeration(
    name="VAlign",
    literals={
            EnumerationLiteral(name="TOP"),
			EnumerationLiteral(name="MIDDLE"),
			EnumerationLiteral(name="BOTTOM")
    }
)

ConnectionStyle: Enumeration = Enumeration(
    name="ConnectionStyle",
    literals={
            EnumerationLiteral(name="freeform"),
			EnumerationLiteral(name="manhatten")
    }
)

AnchorPredefiniedEnum: Enumeration = Enumeration(
    name="AnchorPredefiniedEnum",
    literals={
            EnumerationLiteral(name="center"),
			EnumerationLiteral(name="corners")
    }
)

TextType: Enumeration = Enumeration(
    name="TextType",
    literals={
            EnumerationLiteral(name="default"),
			EnumerationLiteral(name="multiline")
    }
)

# Classes
shape_Description = Class(name="shape::Description")
shape_Anchor = Class(name="shape::Anchor")
shape_ShapeConnection = Class(name="shape::ShapeConnection")
shape_ShapeContainer = Class(name="shape::ShapeContainer")
shape_ShapeContainerElement = Class(name="shape::ShapeContainerElement")
shape_ConnectionDefinition = Class(name="shape::ConnectionDefinition")
ShapeContainerElement = Class(name="ShapeContainerElement")
shape_ShapestyleLayout = Class(name="shape::ShapestyleLayout")
shape_PlacingDefinition = Class(name="shape::PlacingDefinition")
shape_ShapeDefinition = Class(name="shape::ShapeDefinition")
shape_ShapeLayout = Class(name="shape::ShapeLayout")
shape_Shape = Class(name="shape::Shape")
shape_LineLayout = Class(name="shape::LineLayout")
shape_CDPolyline = Class(name="shape::CDPolyline")
shape_PolyLineLayout = Class(name="shape::PolyLineLayout")
shape_CDRectangle = Class(name="shape::CDRectangle")
shape_RectangleEllipseLayout = Class(name="shape::RectangleEllipseLayout")
shape_CDRoundedRectangle = Class(name="shape::CDRoundedRectangle")
shape_AnchorType = Class(name="shape::AnchorType")
shape_AnchorPredefinied = Class(name="shape::AnchorPredefinied")
AnchorType = Class(name="AnchorType")
shape_AnchorManual = Class(name="shape::AnchorManual")
shape_AnchorPosition = Class(name="shape::AnchorPosition")
shape_AnchorPositionPos = Class(name="shape::AnchorPositionPos")
shape_AnchorRelativePosition = Class(name="shape::AnchorRelativePosition")
AnchorPositionPos = Class(name="AnchorPositionPos")
shape_AnchorFixPointPosition = Class(name="shape::AnchorFixPointPosition")
shape_CDLine = Class(name="shape::CDLine")
ShapeConnection = Class(name="ShapeConnection")
shape_CompartmentInfo = Class(name="shape::CompartmentInfo")
shape_RoundedRectangle = Class(name="shape::RoundedRectangle")
shape_RoundedRectangleLayout = Class(name="shape::RoundedRectangleLayout")
shape_CDPolygon = Class(name="shape::CDPolygon")
shape_CDEllipse = Class(name="shape::CDEllipse")
shape_CDText = Class(name="shape::CDText")
shape_TextLayout = Class(name="shape::TextLayout")
shape_TextBody = Class(name="shape::TextBody")
shape_Line = Class(name="shape::Line")
Shape = Class(name="Shape")
shape_Polyline = Class(name="shape::Polyline")
shape_Rectangle = Class(name="shape::Rectangle")
shape_Compartment = Class(name="shape::Compartment")
shape_Polygon = Class(name="shape::Polygon")
shape_Ellipse = Class(name="shape::Ellipse")
shape_Text = Class(name="shape::Text")
shape_CompartmentShape = Class(name="shape::CompartmentShape")
shape_CompartmentRectangle = Class(name="shape::CompartmentRectangle")
CompartmentShape = Class(name="CompartmentShape")
shape_CompartmentRoundedRectangle = Class(name="shape::CompartmentRoundedRectangle")
shape_CompartmentPolygon = Class(name="shape::CompartmentPolygon")
shape_CompartmentEllipse = Class(name="shape::CompartmentEllipse")
shape_CommonLayout = Class(name="shape::CommonLayout")
shape_Point = Class(name="shape::Point")

# shape_Description class attributes and methods
shape_Description_style: Property = Property(name="style", type=StringType)
shape_Description_hAlign: Property = Property(name="hAlign", type=StringType)
shape_Description_vAlign: Property = Property(name="vAlign", type=StringType)
shape_Description.attributes={shape_Description_vAlign, shape_Description_style, shape_Description_hAlign}

# shape_Anchor class attributes and methods

# shape_ShapeConnection class attributes and methods
shape_ShapeConnection_style: Property = Property(name="style", type=StringType)
shape_ShapeConnection.attributes={shape_ShapeConnection_style}

# shape_ShapeContainer class attributes and methods

# shape_ShapeContainerElement class attributes and methods
shape_ShapeContainerElement_name: Property = Property(name="name", type=StringType)
shape_ShapeContainerElement_style: Property = Property(name="style", type=StringType)
shape_ShapeContainerElement.attributes={shape_ShapeContainerElement_style, shape_ShapeContainerElement_name}

# shape_ConnectionDefinition class attributes and methods
shape_ConnectionDefinition_connectionStyle: Property = Property(name="connectionStyle", type=StringType)
shape_ConnectionDefinition.attributes={shape_ConnectionDefinition_connectionStyle}

# ShapeContainerElement class attributes and methods

# shape_ShapestyleLayout class attributes and methods

# shape_PlacingDefinition class attributes and methods
shape_PlacingDefinition_offset: Property = Property(name="offset", type=StringType)
shape_PlacingDefinition_distance: Property = Property(name="distance", type=IntegerType)
shape_PlacingDefinition_angle: Property = Property(name="angle", type=IntegerType)
shape_PlacingDefinition.attributes={shape_PlacingDefinition_offset, shape_PlacingDefinition_angle, shape_PlacingDefinition_distance}

# shape_ShapeDefinition class attributes and methods

# shape_ShapeLayout class attributes and methods
shape_ShapeLayout_minwidth: Property = Property(name="minwidth", type=IntegerType)
shape_ShapeLayout_minheight: Property = Property(name="minheight", type=IntegerType)
shape_ShapeLayout_maxwidth: Property = Property(name="maxwidth", type=IntegerType)
shape_ShapeLayout_maxheight: Property = Property(name="maxheight", type=IntegerType)
shape_ShapeLayout_stretchH: Property = Property(name="stretchH", type=StringType)
shape_ShapeLayout_stretchV: Property = Property(name="stretchV", type=StringType)
shape_ShapeLayout_proportional: Property = Property(name="proportional", type=StringType)
shape_ShapeLayout.attributes={shape_ShapeLayout_stretchH, shape_ShapeLayout_stretchV, shape_ShapeLayout_maxheight, shape_ShapeLayout_maxwidth, shape_ShapeLayout_minwidth, shape_ShapeLayout_proportional, shape_ShapeLayout_minheight}

# shape_Shape class attributes and methods
shape_Shape_style: Property = Property(name="style", type=StringType)
shape_Shape.attributes={shape_Shape_style}

# shape_LineLayout class attributes and methods

# shape_CDPolyline class attributes and methods

# shape_PolyLineLayout class attributes and methods

# shape_CDRectangle class attributes and methods

# shape_RectangleEllipseLayout class attributes and methods

# shape_CDRoundedRectangle class attributes and methods

# shape_AnchorType class attributes and methods

# shape_AnchorPredefinied class attributes and methods
shape_AnchorPredefinied_value: Property = Property(name="value", type=StringType)
shape_AnchorPredefinied.attributes={shape_AnchorPredefinied_value}

# AnchorType class attributes and methods

# shape_AnchorManual class attributes and methods

# shape_AnchorPosition class attributes and methods

# shape_AnchorPositionPos class attributes and methods

# shape_AnchorRelativePosition class attributes and methods
shape_AnchorRelativePosition_xoffset: Property = Property(name="xoffset", type=StringType)
shape_AnchorRelativePosition_yoffset: Property = Property(name="yoffset", type=StringType)
shape_AnchorRelativePosition.attributes={shape_AnchorRelativePosition_yoffset, shape_AnchorRelativePosition_xoffset}

# AnchorPositionPos class attributes and methods

# shape_AnchorFixPointPosition class attributes and methods
shape_AnchorFixPointPosition_xcor: Property = Property(name="xcor", type=IntegerType)
shape_AnchorFixPointPosition_ycor: Property = Property(name="ycor", type=IntegerType)
shape_AnchorFixPointPosition.attributes={shape_AnchorFixPointPosition_xcor, shape_AnchorFixPointPosition_ycor}

# shape_CDLine class attributes and methods

# ShapeConnection class attributes and methods

# shape_CompartmentInfo class attributes and methods
shape_CompartmentInfo_spacing: Property = Property(name="spacing", type=IntegerType)
shape_CompartmentInfo_margin: Property = Property(name="margin", type=IntegerType)
shape_CompartmentInfo_invisible: Property = Property(name="invisible", type=BooleanType)
shape_CompartmentInfo_compartmentLayout: Property = Property(name="compartmentLayout", type=StringType)
shape_CompartmentInfo_stretchH: Property = Property(name="stretchH", type=StringType)
shape_CompartmentInfo_stretchV: Property = Property(name="stretchV", type=StringType)
shape_CompartmentInfo.attributes={shape_CompartmentInfo_stretchH, shape_CompartmentInfo_stretchV, shape_CompartmentInfo_invisible, shape_CompartmentInfo_margin, shape_CompartmentInfo_spacing, shape_CompartmentInfo_compartmentLayout}

# shape_RoundedRectangle class attributes and methods

# shape_RoundedRectangleLayout class attributes and methods
shape_RoundedRectangleLayout_curveWidth: Property = Property(name="curveWidth", type=IntegerType)
shape_RoundedRectangleLayout_curveHeight: Property = Property(name="curveHeight", type=IntegerType)
shape_RoundedRectangleLayout.attributes={shape_RoundedRectangleLayout_curveHeight, shape_RoundedRectangleLayout_curveWidth}

# shape_CDPolygon class attributes and methods

# shape_CDEllipse class attributes and methods

# shape_CDText class attributes and methods
shape_CDText_texttype: Property = Property(name="texttype", type=StringType)
shape_CDText.attributes={shape_CDText_texttype}

# shape_TextLayout class attributes and methods
shape_TextLayout_hAlign: Property = Property(name="hAlign", type=StringType)
shape_TextLayout_vAlign: Property = Property(name="vAlign", type=StringType)
shape_TextLayout.attributes={shape_TextLayout_hAlign, shape_TextLayout_vAlign}

# shape_TextBody class attributes and methods
shape_TextBody_value: Property = Property(name="value", type=StringType)
shape_TextBody.attributes={shape_TextBody_value}

# shape_Line class attributes and methods

# Shape class attributes and methods

# shape_Polyline class attributes and methods

# shape_Rectangle class attributes and methods

# shape_Compartment class attributes and methods
shape_Compartment_compartmentLayout: Property = Property(name="compartmentLayout", type=StringType)
shape_Compartment.attributes={shape_Compartment_compartmentLayout}

# shape_Polygon class attributes and methods

# shape_Ellipse class attributes and methods

# shape_Text class attributes and methods
shape_Text_texttype: Property = Property(name="texttype", type=StringType)
shape_Text.attributes={shape_Text_texttype}

# shape_CompartmentShape class attributes and methods

# shape_CompartmentRectangle class attributes and methods

# CompartmentShape class attributes and methods

# shape_CompartmentRoundedRectangle class attributes and methods

# shape_CompartmentPolygon class attributes and methods

# shape_CompartmentEllipse class attributes and methods

# shape_CommonLayout class attributes and methods
shape_CommonLayout_xcor: Property = Property(name="xcor", type=IntegerType)
shape_CommonLayout_ycor: Property = Property(name="ycor", type=IntegerType)
shape_CommonLayout_width: Property = Property(name="width", type=IntegerType)
shape_CommonLayout_heigth: Property = Property(name="heigth", type=IntegerType)
shape_CommonLayout.attributes={shape_CommonLayout_heigth, shape_CommonLayout_xcor, shape_CommonLayout_width, shape_CommonLayout_ycor}

# shape_Point class attributes and methods
shape_Point_xcor: Property = Property(name="xcor", type=StringType)
shape_Point_ycor: Property = Property(name="ycor", type=StringType)
shape_Point_curveBefore: Property = Property(name="curveBefore", type=IntegerType)
shape_Point_curveAfter: Property = Property(name="curveAfter", type=IntegerType)
shape_Point.attributes={shape_Point_xcor, shape_Point_curveBefore, shape_Point_curveAfter, shape_Point_ycor}

# Relationships
description7: BinaryAssociation = BinaryAssociation(
    name="description7",
    ends={
        Property(name="shape_Description", type=shape_ShapeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_ShapeDefinition8", type=shape_Description, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
anchor9: BinaryAssociation = BinaryAssociation(
    name="anchor9",
    ends={
        Property(name="shape_Anchor", type=shape_ShapeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_ShapeDefinition10", type=shape_Anchor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
shapeCon11: BinaryAssociation = BinaryAssociation(
    name="shapeCon11",
    ends={
        Property(name="shape_ShapeConnection", type=shape_PlacingDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_PlacingDefinition12", type=shape_ShapeConnection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
shapeContainerElement0: BinaryAssociation = BinaryAssociation(
    name="shapeContainerElement0",
    ends={
        Property(name="shape_ShapeContainerElement", type=shape_ShapeContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_ShapeContainer", type=shape_ShapeContainerElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
layout1: BinaryAssociation = BinaryAssociation(
    name="layout1",
    ends={
        Property(name="shape_ShapestyleLayout", type=shape_ConnectionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_ConnectionDefinition", type=shape_ShapestyleLayout, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
placing2: BinaryAssociation = BinaryAssociation(
    name="placing2",
    ends={
        Property(name="shape_PlacingDefinition", type=shape_ConnectionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_ConnectionDefinition3", type=shape_PlacingDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
shapeLayout4: BinaryAssociation = BinaryAssociation(
    name="shapeLayout4",
    ends={
        Property(name="shape_ShapeLayout", type=shape_ShapeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_ShapeDefinition", type=shape_ShapeLayout, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
shape5: BinaryAssociation = BinaryAssociation(
    name="shape5",
    ends={
        Property(name="shape_Shape", type=shape_ShapeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_ShapeDefinition6", type=shape_Shape, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
layout18: BinaryAssociation = BinaryAssociation(
    name="layout18",
    ends={
        Property(name="shape_LineLayout", type=shape_CDLine, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_CDLine", type=shape_LineLayout, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
layout19: BinaryAssociation = BinaryAssociation(
    name="layout19",
    ends={
        Property(name="shape_PolyLineLayout", type=shape_CDPolyline, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_CDPolyline", type=shape_PolyLineLayout, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
layout20: BinaryAssociation = BinaryAssociation(
    name="layout20",
    ends={
        Property(name="shape_RectangleEllipseLayout", type=shape_CDRectangle, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_CDRectangle", type=shape_RectangleEllipseLayout, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type13: BinaryAssociation = BinaryAssociation(
    name="type13",
    ends={
        Property(name="shape_AnchorType", type=shape_Anchor, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_Anchor14", type=shape_AnchorType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
position15: BinaryAssociation = BinaryAssociation(
    name="position15",
    ends={
        Property(name="shape_AnchorPosition", type=shape_AnchorManual, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_AnchorManual", type=shape_AnchorPosition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pos16: BinaryAssociation = BinaryAssociation(
    name="pos16",
    ends={
        Property(name="shape_AnchorPositionPos", type=shape_AnchorPosition, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_AnchorPosition17", type=shape_AnchorPositionPos, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
compartmentInfo33: BinaryAssociation = BinaryAssociation(
    name="compartmentInfo33",
    ends={
        Property(name="shape_CompartmentInfo", type=shape_Rectangle, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_Rectangle", type=shape_CompartmentInfo, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
layout34: BinaryAssociation = BinaryAssociation(
    name="layout34",
    ends={
        Property(name="shape_RectangleEllipseLayout36", type=shape_Rectangle, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_Rectangle35", type=shape_RectangleEllipseLayout, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
shape37: BinaryAssociation = BinaryAssociation(
    name="shape37",
    ends={
        Property(name="shape_Shape39", type=shape_Rectangle, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_Rectangle38", type=shape_Shape, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
layout40: BinaryAssociation = BinaryAssociation(
    name="layout40",
    ends={
        Property(name="shape_RoundedRectangleLayout41", type=shape_RoundedRectangle, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_RoundedRectangle", type=shape_RoundedRectangleLayout, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
layout21: BinaryAssociation = BinaryAssociation(
    name="layout21",
    ends={
        Property(name="shape_RoundedRectangleLayout", type=shape_CDRoundedRectangle, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_CDRoundedRectangle", type=shape_RoundedRectangleLayout, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
layout22: BinaryAssociation = BinaryAssociation(
    name="layout22",
    ends={
        Property(name="shape_PolyLineLayout23", type=shape_CDPolygon, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_CDPolygon", type=shape_PolyLineLayout, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
layout24: BinaryAssociation = BinaryAssociation(
    name="layout24",
    ends={
        Property(name="shape_RectangleEllipseLayout25", type=shape_CDEllipse, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_CDEllipse", type=shape_RectangleEllipseLayout, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
layout26: BinaryAssociation = BinaryAssociation(
    name="layout26",
    ends={
        Property(name="shape_TextLayout", type=shape_CDText, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_CDText", type=shape_TextLayout, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body27: BinaryAssociation = BinaryAssociation(
    name="body27",
    ends={
        Property(name="shape_TextBody", type=shape_CDText, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_CDText28", type=shape_TextBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
layout29: BinaryAssociation = BinaryAssociation(
    name="layout29",
    ends={
        Property(name="shape_LineLayout30", type=shape_Line, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_Line", type=shape_LineLayout, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
layout31: BinaryAssociation = BinaryAssociation(
    name="layout31",
    ends={
        Property(name="shape_PolyLineLayout32", type=shape_Polyline, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_Polyline", type=shape_PolyLineLayout, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
id63: BinaryAssociation = BinaryAssociation(
    name="id63",
    ends={
        Property(name="shape_TextBody65", type=shape_CompartmentInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_CompartmentInfo64", type=shape_TextBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
shape42: BinaryAssociation = BinaryAssociation(
    name="shape42",
    ends={
        Property(name="shape_Shape44", type=shape_RoundedRectangle, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_RoundedRectangle43", type=shape_Shape, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
layout45: BinaryAssociation = BinaryAssociation(
    name="layout45",
    ends={
        Property(name="shape_PolyLineLayout46", type=shape_Polygon, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_Polygon", type=shape_PolyLineLayout, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
shape47: BinaryAssociation = BinaryAssociation(
    name="shape47",
    ends={
        Property(name="shape_Shape49", type=shape_Polygon, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_Polygon48", type=shape_Shape, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
compartmentInfo50: BinaryAssociation = BinaryAssociation(
    name="compartmentInfo50",
    ends={
        Property(name="shape_CompartmentInfo51", type=shape_Ellipse, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_Ellipse", type=shape_CompartmentInfo, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
layout52: BinaryAssociation = BinaryAssociation(
    name="layout52",
    ends={
        Property(name="shape_RectangleEllipseLayout54", type=shape_Ellipse, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_Ellipse53", type=shape_RectangleEllipseLayout, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
shape55: BinaryAssociation = BinaryAssociation(
    name="shape55",
    ends={
        Property(name="shape_Shape57", type=shape_Ellipse, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_Ellipse56", type=shape_Shape, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
layout58: BinaryAssociation = BinaryAssociation(
    name="layout58",
    ends={
        Property(name="shape_TextLayout59", type=shape_Text, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_Text", type=shape_TextLayout, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body60: BinaryAssociation = BinaryAssociation(
    name="body60",
    ends={
        Property(name="shape_TextBody62", type=shape_Text, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_Text61", type=shape_TextBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body83: BinaryAssociation = BinaryAssociation(
    name="body83",
    ends={
        Property(name="shape_TextBody85", type=shape_Description, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_Description84", type=shape_TextBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
shape66: BinaryAssociation = BinaryAssociation(
    name="shape66",
    ends={
        Property(name="shape_CompartmentShape", type=shape_Compartment, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_Compartment", type=shape_CompartmentShape, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
layout67: BinaryAssociation = BinaryAssociation(
    name="layout67",
    ends={
        Property(name="shape_RectangleEllipseLayout69", type=shape_CompartmentShape, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_CompartmentShape68", type=shape_RectangleEllipseLayout, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
id70: BinaryAssociation = BinaryAssociation(
    name="id70",
    ends={
        Property(name="shape_TextBody72", type=shape_CompartmentShape, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_CompartmentShape71", type=shape_TextBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
layout73: BinaryAssociation = BinaryAssociation(
    name="layout73",
    ends={
        Property(name="shape_RoundedRectangleLayout74", type=shape_CompartmentRoundedRectangle, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_CompartmentRoundedRectangle", type=shape_RoundedRectangleLayout, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
id75: BinaryAssociation = BinaryAssociation(
    name="id75",
    ends={
        Property(name="shape_TextBody77", type=shape_CompartmentRoundedRectangle, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_CompartmentRoundedRectangle76", type=shape_TextBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
layout78: BinaryAssociation = BinaryAssociation(
    name="layout78",
    ends={
        Property(name="shape_PolyLineLayout79", type=shape_CompartmentPolygon, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_CompartmentPolygon", type=shape_PolyLineLayout, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
id80: BinaryAssociation = BinaryAssociation(
    name="id80",
    ends={
        Property(name="shape_TextBody82", type=shape_CompartmentPolygon, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_CompartmentPolygon81", type=shape_TextBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
common86: BinaryAssociation = BinaryAssociation(
    name="common86",
    ends={
        Property(name="shape_CommonLayout", type=shape_RectangleEllipseLayout, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_RectangleEllipseLayout87", type=shape_CommonLayout, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
layout88: BinaryAssociation = BinaryAssociation(
    name="layout88",
    ends={
        Property(name="shape_ShapestyleLayout90", type=shape_RectangleEllipseLayout, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_RectangleEllipseLayout89", type=shape_ShapestyleLayout, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
point91: BinaryAssociation = BinaryAssociation(
    name="point91",
    ends={
        Property(name="shape_Point", type=shape_LineLayout, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_LineLayout92", type=shape_Point, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
layout93: BinaryAssociation = BinaryAssociation(
    name="layout93",
    ends={
        Property(name="shape_ShapestyleLayout95", type=shape_LineLayout, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_LineLayout94", type=shape_ShapestyleLayout, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
point96: BinaryAssociation = BinaryAssociation(
    name="point96",
    ends={
        Property(name="shape_Point98", type=shape_PolyLineLayout, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_PolyLineLayout97", type=shape_Point, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
layout99: BinaryAssociation = BinaryAssociation(
    name="layout99",
    ends={
        Property(name="shape_ShapestyleLayout101", type=shape_PolyLineLayout, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_PolyLineLayout100", type=shape_ShapestyleLayout, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
common102: BinaryAssociation = BinaryAssociation(
    name="common102",
    ends={
        Property(name="shape_CommonLayout104", type=shape_RoundedRectangleLayout, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_RoundedRectangleLayout103", type=shape_CommonLayout, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
layout105: BinaryAssociation = BinaryAssociation(
    name="layout105",
    ends={
        Property(name="shape_ShapestyleLayout107", type=shape_RoundedRectangleLayout, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_RoundedRectangleLayout106", type=shape_ShapestyleLayout, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
common108: BinaryAssociation = BinaryAssociation(
    name="common108",
    ends={
        Property(name="shape_CommonLayout110", type=shape_TextLayout, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_TextLayout109", type=shape_CommonLayout, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
layout111: BinaryAssociation = BinaryAssociation(
    name="layout111",
    ends={
        Property(name="shape_ShapestyleLayout113", type=shape_TextLayout, multiplicity=Multiplicity(1, 1)),
        Property(name="shape_TextLayout112", type=shape_ShapestyleLayout, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_shape_ConnectionDefinition_ShapeContainerElement = Generalization(general=ShapeContainerElement, specific=shape_ConnectionDefinition)
gen_shape_ShapeDefinition_ShapeContainerElement = Generalization(general=ShapeContainerElement, specific=shape_ShapeDefinition)
gen_shape_CDPolyline_ShapeConnection = Generalization(general=ShapeConnection, specific=shape_CDPolyline)
gen_shape_CDRectangle_ShapeConnection = Generalization(general=ShapeConnection, specific=shape_CDRectangle)
gen_shape_AnchorPredefinied_AnchorType = Generalization(general=AnchorType, specific=shape_AnchorPredefinied)
gen_shape_AnchorManual_AnchorType = Generalization(general=AnchorType, specific=shape_AnchorManual)
gen_shape_AnchorRelativePosition_AnchorPositionPos = Generalization(general=AnchorPositionPos, specific=shape_AnchorRelativePosition)
gen_shape_AnchorFixPointPosition_AnchorPositionPos = Generalization(general=AnchorPositionPos, specific=shape_AnchorFixPointPosition)
gen_shape_CDLine_ShapeConnection = Generalization(general=ShapeConnection, specific=shape_CDLine)
gen_shape_RoundedRectangle_Shape = Generalization(general=Shape, specific=shape_RoundedRectangle)
gen_shape_CDRoundedRectangle_ShapeConnection = Generalization(general=ShapeConnection, specific=shape_CDRoundedRectangle)
gen_shape_CDPolygon_ShapeConnection = Generalization(general=ShapeConnection, specific=shape_CDPolygon)
gen_shape_CDEllipse_ShapeConnection = Generalization(general=ShapeConnection, specific=shape_CDEllipse)
gen_shape_CDText_ShapeConnection = Generalization(general=ShapeConnection, specific=shape_CDText)
gen_shape_Line_Shape = Generalization(general=Shape, specific=shape_Line)
gen_shape_Polyline_Shape = Generalization(general=Shape, specific=shape_Polyline)
gen_shape_Rectangle_Shape = Generalization(general=Shape, specific=shape_Rectangle)
gen_shape_Polygon_Shape = Generalization(general=Shape, specific=shape_Polygon)
gen_shape_Ellipse_Shape = Generalization(general=Shape, specific=shape_Ellipse)
gen_shape_Text_Shape = Generalization(general=Shape, specific=shape_Text)
gen_shape_CompartmentRectangle_CompartmentShape = Generalization(general=CompartmentShape, specific=shape_CompartmentRectangle)
gen_shape_CompartmentEllipse_CompartmentShape = Generalization(general=CompartmentShape, specific=shape_CompartmentEllipse)

# Domain Model
domain_model = DomainModel(
    name="shape",
    types={shape_Description, shape_Anchor, shape_ShapeConnection, shape_ShapeContainer, shape_ShapeContainerElement, shape_ConnectionDefinition, ShapeContainerElement, shape_ShapestyleLayout, shape_PlacingDefinition, shape_ShapeDefinition, shape_ShapeLayout, shape_Shape, shape_LineLayout, shape_CDPolyline, shape_PolyLineLayout, shape_CDRectangle, shape_RectangleEllipseLayout, shape_CDRoundedRectangle, shape_AnchorType, shape_AnchorPredefinied, AnchorType, shape_AnchorManual, shape_AnchorPosition, shape_AnchorPositionPos, shape_AnchorRelativePosition, AnchorPositionPos, shape_AnchorFixPointPosition, shape_CDLine, ShapeConnection, shape_CompartmentInfo, shape_RoundedRectangle, shape_RoundedRectangleLayout, shape_CDPolygon, shape_CDEllipse, shape_CDText, shape_TextLayout, shape_TextBody, shape_Line, Shape, shape_Polyline, shape_Rectangle, shape_Compartment, shape_Polygon, shape_Ellipse, shape_Text, shape_CompartmentShape, shape_CompartmentRectangle, CompartmentShape, shape_CompartmentRoundedRectangle, shape_CompartmentPolygon, shape_CompartmentEllipse, shape_CommonLayout, shape_Point, CompartmentLayout, HAlign, VAlign, ConnectionStyle, AnchorPredefiniedEnum, TextType},
    associations={description7, anchor9, shapeCon11, shapeContainerElement0, layout1, placing2, shapeLayout4, shape5, layout18, layout19, layout20, type13, position15, pos16, compartmentInfo33, layout34, shape37, layout40, layout21, layout22, layout24, layout26, body27, layout29, layout31, id63, shape42, layout45, shape47, compartmentInfo50, layout52, shape55, layout58, body60, body83, shape66, layout67, id70, layout73, id75, layout78, id80, common86, layout88, point91, layout93, point96, layout99, common102, layout105, common108, layout111},
    generalizations={gen_shape_ConnectionDefinition_ShapeContainerElement, gen_shape_ShapeDefinition_ShapeContainerElement, gen_shape_CDPolyline_ShapeConnection, gen_shape_CDRectangle_ShapeConnection, gen_shape_AnchorPredefinied_AnchorType, gen_shape_AnchorManual_AnchorType, gen_shape_AnchorRelativePosition_AnchorPositionPos, gen_shape_AnchorFixPointPosition_AnchorPositionPos, gen_shape_CDLine_ShapeConnection, gen_shape_RoundedRectangle_Shape, gen_shape_CDRoundedRectangle_ShapeConnection, gen_shape_CDPolygon_ShapeConnection, gen_shape_CDEllipse_ShapeConnection, gen_shape_CDText_ShapeConnection, gen_shape_Line_Shape, gen_shape_Polyline_Shape, gen_shape_Rectangle_Shape, gen_shape_Polygon_Shape, gen_shape_Ellipse_Shape, gen_shape_Text_Shape, gen_shape_CompartmentRectangle_CompartmentShape, gen_shape_CompartmentEllipse_CompartmentShape},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)