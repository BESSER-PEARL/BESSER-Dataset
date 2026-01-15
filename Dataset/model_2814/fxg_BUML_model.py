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
Winding: Enumeration = Enumeration(
    name="Winding",
    literals={
            EnumerationLiteral(name="NOT_SET"),
			EnumerationLiteral(name="evenOdd"),
			EnumerationLiteral(name="nonZero")
    }
)

MaskType: Enumeration = Enumeration(
    name="MaskType",
    literals={
            EnumerationLiteral(name="CLIP"),
			EnumerationLiteral(name="ALPHA")
    }
)

BlendMode: Enumeration = Enumeration(
    name="BlendMode",
    literals={
            EnumerationLiteral(name="subtract"),
			EnumerationLiteral(name="NOT_SET"),
			EnumerationLiteral(name="add"),
			EnumerationLiteral(name="alpha"),
			EnumerationLiteral(name="darken"),
			EnumerationLiteral(name="difference"),
			EnumerationLiteral(name="erase"),
			EnumerationLiteral(name="hardlight"),
			EnumerationLiteral(name="invert"),
			EnumerationLiteral(name="layer"),
			EnumerationLiteral(name="lighten"),
			EnumerationLiteral(name="multiply"),
			EnumerationLiteral(name="normal"),
			EnumerationLiteral(name="overlay"),
			EnumerationLiteral(name="screen"),
			EnumerationLiteral(name="shader")
    }
)

Cap: Enumeration = Enumeration(
    name="Cap",
    literals={
            EnumerationLiteral(name="ROUND"),
			EnumerationLiteral(name="SQUARE"),
			EnumerationLiteral(name="NONE")
    }
)

Joint: Enumeration = Enumeration(
    name="Joint",
    literals={
            EnumerationLiteral(name="ROUND"),
			EnumerationLiteral(name="MITER"),
			EnumerationLiteral(name="BEVEL")
    }
)

FontStyle: Enumeration = Enumeration(
    name="FontStyle",
    literals={
            EnumerationLiteral(name="NORMAL"),
			EnumerationLiteral(name="ITALIC")
    }
)

FontWeight: Enumeration = Enumeration(
    name="FontWeight",
    literals={
            EnumerationLiteral(name="NORMAL"),
			EnumerationLiteral(name="BOLD")
    }
)

TextDecoration: Enumeration = Enumeration(
    name="TextDecoration",
    literals={
            EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="UNDERLINE")
    }
)

WhitespaceCollapse: Enumeration = Enumeration(
    name="WhitespaceCollapse",
    literals={
            EnumerationLiteral(name="PRESERVE"),
			EnumerationLiteral(name="COLLAPSE")
    }
)

Kerning: Enumeration = Enumeration(
    name="Kerning",
    literals={
            EnumerationLiteral(name="ON"),
			EnumerationLiteral(name="OFF"),
			EnumerationLiteral(name="AUTO")
    }
)

SpreadMethod: Enumeration = Enumeration(
    name="SpreadMethod",
    literals={
            EnumerationLiteral(name="NOT_SET"),
			EnumerationLiteral(name="pad"),
			EnumerationLiteral(name="reflect"),
			EnumerationLiteral(name="repeat")
    }
)

InterpolationMethod: Enumeration = Enumeration(
    name="InterpolationMethod",
    literals={
            EnumerationLiteral(name="NOT_SET"),
			EnumerationLiteral(name="rgb"),
			EnumerationLiteral(name="linearRGB")
    }
)

JustificationRule: Enumeration = Enumeration(
    name="JustificationRule",
    literals={
            EnumerationLiteral(name="auto"),
			EnumerationLiteral(name="space"),
			EnumerationLiteral(name="eastAsian")
    }
)

JustificationStyle: Enumeration = Enumeration(
    name="JustificationStyle",
    literals={
            EnumerationLiteral(name="auto"),
			EnumerationLiteral(name="prioritizeLeastAdjustment"),
			EnumerationLiteral(name="pushInKinsoku"),
			EnumerationLiteral(name="pushOutOnly")
    }
)

ScaleMode: Enumeration = Enumeration(
    name="ScaleMode",
    literals={
            EnumerationLiteral(name="NORMAL"),
			EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="HORIZONTAL"),
			EnumerationLiteral(name="VERTICAL")
    }
)

BevelFilterType: Enumeration = Enumeration(
    name="BevelFilterType",
    literals={
            EnumerationLiteral(name="INNER"),
			EnumerationLiteral(name="OUTER"),
			EnumerationLiteral(name="FULL")
    }
)

FillMode: Enumeration = Enumeration(
    name="FillMode",
    literals={
            EnumerationLiteral(name="SCALE"),
			EnumerationLiteral(name="CLIP"),
			EnumerationLiteral(name="REPEAT")
    }
)

TextAlign: Enumeration = Enumeration(
    name="TextAlign",
    literals={
            EnumerationLiteral(name="justify"),
			EnumerationLiteral(name="start"),
			EnumerationLiteral(name="end"),
			EnumerationLiteral(name="left"),
			EnumerationLiteral(name="center"),
			EnumerationLiteral(name="right")
    }
)

LineBreak: Enumeration = Enumeration(
    name="LineBreak",
    literals={
            EnumerationLiteral(name="toFit"),
			EnumerationLiteral(name="explicit")
    }
)

BreakOpportunity: Enumeration = Enumeration(
    name="BreakOpportunity",
    literals={
            EnumerationLiteral(name="auto"),
			EnumerationLiteral(name="any"),
			EnumerationLiteral(name="none"),
			EnumerationLiteral(name="all")
    }
)

TextJustify: Enumeration = Enumeration(
    name="TextJustify",
    literals={
            EnumerationLiteral(name="interWord"),
			EnumerationLiteral(name="distribute")
    }
)

LeadingModel: Enumeration = Enumeration(
    name="LeadingModel",
    literals={
            EnumerationLiteral(name="auto"),
			EnumerationLiteral(name="romanUp"),
			EnumerationLiteral(name="ideographicTopUp"),
			EnumerationLiteral(name="ideographicCenterUp"),
			EnumerationLiteral(name="ascentDescentUp"),
			EnumerationLiteral(name="ideographicTopDown"),
			EnumerationLiteral(name="ideographicCenterDown")
    }
)

BlockProgression: Enumeration = Enumeration(
    name="BlockProgression",
    literals={
            EnumerationLiteral(name="tb"),
			EnumerationLiteral(name="rl")
    }
)

VerticalAlign: Enumeration = Enumeration(
    name="VerticalAlign",
    literals={
            EnumerationLiteral(name="inherit"),
			EnumerationLiteral(name="top"),
			EnumerationLiteral(name="middle"),
			EnumerationLiteral(name="bottom"),
			EnumerationLiteral(name="justify")
    }
)

LigatureLevel: Enumeration = Enumeration(
    name="LigatureLevel",
    literals={
            EnumerationLiteral(name="minimum"),
			EnumerationLiteral(name="common"),
			EnumerationLiteral(name="uncommon"),
			EnumerationLiteral(name="exotic")
    }
)

DigitCase: Enumeration = Enumeration(
    name="DigitCase",
    literals={
            EnumerationLiteral(name="default"),
			EnumerationLiteral(name="lining"),
			EnumerationLiteral(name="oldStyle")
    }
)

DigitWidth: Enumeration = Enumeration(
    name="DigitWidth",
    literals={
            EnumerationLiteral(name="default"),
			EnumerationLiteral(name="proportional"),
			EnumerationLiteral(name="tabular")
    }
)

DominantBaseline: Enumeration = Enumeration(
    name="DominantBaseline",
    literals={
            EnumerationLiteral(name="auto"),
			EnumerationLiteral(name="roman"),
			EnumerationLiteral(name="ascent"),
			EnumerationLiteral(name="descent"),
			EnumerationLiteral(name="ideographicTop"),
			EnumerationLiteral(name="ideographicCenter"),
			EnumerationLiteral(name="ideographicBottom")
    }
)

AlignmentBaseline: Enumeration = Enumeration(
    name="AlignmentBaseline",
    literals={
            EnumerationLiteral(name="ascent"),
			EnumerationLiteral(name="descent"),
			EnumerationLiteral(name="ideographicTop"),
			EnumerationLiteral(name="ideographicCenter"),
			EnumerationLiteral(name="ideographicBottom"),
			EnumerationLiteral(name="useDominantBaseline"),
			EnumerationLiteral(name="auto"),
			EnumerationLiteral(name="roman")
    }
)

TypographicCase: Enumeration = Enumeration(
    name="TypographicCase",
    literals={
            EnumerationLiteral(name="default"),
			EnumerationLiteral(name="capsToSmallCaps"),
			EnumerationLiteral(name="uppercase"),
			EnumerationLiteral(name="lowercase"),
			EnumerationLiteral(name="lowercaseToSmallCaps")
    }
)

TextRotation: Enumeration = Enumeration(
    name="TextRotation",
    literals={
            EnumerationLiteral(name="auto"),
			EnumerationLiteral(name="rotate0"),
			EnumerationLiteral(name="rotate90"),
			EnumerationLiteral(name="rotate180"),
			EnumerationLiteral(name="rotate270")
    }
)

# Classes
fxg_Group = Class(name="fxg::Group")
fxg_Library = Class(name="fxg::Library")
fxg_Private = Class(name="fxg::Private")
FXGElement = Class(name="FXGElement")
fxg_Definition = Class(name="fxg::Definition")
fxg_Graphic = Class(name="fxg::Graphic")
fxg_Matrix = Class(name="fxg::Matrix")
fxg_ColorTransform = Class(name="fxg::ColorTransform")
fxg_PlaceObject = Class(name="fxg::PlaceObject")
fxg_Transform = Class(name="fxg::Transform")
fxg_Filter = Class(name="fxg::Filter", is_abstract=True)
fxg_Fill = Class(name="fxg::Fill", is_abstract=True)
fxg_Stroke = Class(name="fxg::Stroke", is_abstract=True)
fxg_Path = Class(name="fxg::Path")
fxg_Ellipse = Class(name="fxg::Ellipse")
fxg_Shape = Class(name="fxg::Shape", is_abstract=True)
fxg_Rect = Class(name="fxg::Rect")
Shape = Class(name="Shape")
fxg_RichText = Class(name="fxg::RichText")
ParagraphAttributes = Class(name="ParagraphAttributes")
ContainerAttributes = Class(name="ContainerAttributes")
CharacterAttributes = Class(name="CharacterAttributes")
fxg_Line = Class(name="fxg::Line")
fxg_CharacterAttributes = Class(name="fxg::CharacterAttributes", is_abstract=True)
fxg_RichTextContent = Class(name="fxg::RichTextContent", is_abstract=True)
fxg_RichTextContentContainer = Class(name="fxg::RichTextContentContainer")
RichTextContent = Class(name="RichTextContent")
fxg_ParagraphAttributes = Class(name="fxg::ParagraphAttributes", is_abstract=True)
fxg_ContainerAttributes = Class(name="fxg::ContainerAttributes", is_abstract=True)
fxg_div = Class(name="fxg::div")
RichTextContentContainer = Class(name="RichTextContentContainer")
fxg_p = Class(name="fxg::p")
fxg_tcy = Class(name="fxg::tcy")
fxg_a = Class(name="fxg::a")
fxg_img = Class(name="fxg::img")
fxg_rawtext = Class(name="fxg::rawtext")
fxg_LinearGradient = Class(name="fxg::LinearGradient")
fxg_span = Class(name="fxg::span")
fxg_br = Class(name="fxg::br")
fxg_tab = Class(name="fxg::tab")
fxg_linkNormalFormat = Class(name="fxg::linkNormalFormat")
fxg_linkHoverFormat = Class(name="fxg::linkHoverFormat")
fxg_linkActiveFormat = Class(name="fxg::linkActiveFormat")
fxg_BitmapImage = Class(name="fxg::BitmapImage")
fxg_SolidColor = Class(name="fxg::SolidColor")
Fill = Class(name="Fill")
fxg_SolidColorStroke = Class(name="fxg::SolidColorStroke")
Stroke = Class(name="Stroke")
fxg_RadialGradient = Class(name="fxg::RadialGradient")
fxg_BitmapFill = Class(name="fxg::BitmapFill")
fxg_GradientEntry = Class(name="fxg::GradientEntry")
fxg_LinearGradientStroke = Class(name="fxg::LinearGradientStroke")
fxg_RadialGradientStroke = Class(name="fxg::RadialGradientStroke")
fxg_BlurFilter = Class(name="fxg::BlurFilter")
Filter = Class(name="Filter")
fxg_DropShadowFilter = Class(name="fxg::DropShadowFilter")
fxg_BevelFilter = Class(name="fxg::BevelFilter")
fxg_GradientGlowFilter = Class(name="fxg::GradientGlowFilter")
fxg_GradientBevelFilter = Class(name="fxg::GradientBevelFilter")
fxg_ColorMatrixFilter = Class(name="fxg::ColorMatrixFilter")
fxg_FXGElement = Class(name="fxg::FXGElement", is_abstract=True)
fxg_ContainerElement = Class(name="fxg::ContainerElement")

# fxg_Group class attributes and methods
fxg_Group_rotation: Property = Property(name="rotation", type=StringType)
fxg_Group_scaleX: Property = Property(name="scaleX", type=StringType)
fxg_Group_scaleY: Property = Property(name="scaleY", type=StringType)
fxg_Group_x: Property = Property(name="x", type=StringType)
fxg_Group_y: Property = Property(name="y", type=StringType)
fxg_Group_blendMode: Property = Property(name="blendMode", type=StringType)
fxg_Group_alpha: Property = Property(name="alpha", type=StringType)
fxg_Group_id: Property = Property(name="id", type=StringType)
fxg_Group_transformX: Property = Property(name="transformX", type=StringType)
fxg_Group_transformY: Property = Property(name="transformY", type=StringType)
fxg_Group_maskType: Property = Property(name="maskType", type=StringType)
fxg_Group_visible: Property = Property(name="visible", type=StringType)
fxg_Group_scaleGridLeft: Property = Property(name="scaleGridLeft", type=StringType)
fxg_Group_scaleGridRight: Property = Property(name="scaleGridRight", type=StringType)
fxg_Group_scaleGridTop: Property = Property(name="scaleGridTop", type=StringType)
fxg_Group_scaleGridBottom: Property = Property(name="scaleGridBottom", type=StringType)
fxg_Group.attributes={fxg_Group_y, fxg_Group_scaleX, fxg_Group_alpha, fxg_Group_scaleY, fxg_Group_rotation, fxg_Group_scaleGridLeft, fxg_Group_transformX, fxg_Group_blendMode, fxg_Group_id, fxg_Group_scaleGridRight, fxg_Group_scaleGridTop, fxg_Group_visible, fxg_Group_transformY, fxg_Group_scaleGridBottom, fxg_Group_maskType, fxg_Group_x}

# fxg_Library class attributes and methods

# fxg_Private class attributes and methods

# FXGElement class attributes and methods

# fxg_Definition class attributes and methods
fxg_Definition_name: Property = Property(name="name", type=StringType)
fxg_Definition.attributes={fxg_Definition_name}

# fxg_Graphic class attributes and methods
fxg_Graphic_viewHeight: Property = Property(name="viewHeight", type=IntegerType)
fxg_Graphic_version: Property = Property(name="version", type=StringType)
fxg_Graphic_scaleGridLeft: Property = Property(name="scaleGridLeft", type=StringType)
fxg_Graphic_scaleGridRight: Property = Property(name="scaleGridRight", type=StringType)
fxg_Graphic_scaleGridTop: Property = Property(name="scaleGridTop", type=StringType)
fxg_Graphic_scaleGridBottom: Property = Property(name="scaleGridBottom", type=StringType)
fxg_Graphic_viewWidth: Property = Property(name="viewWidth", type=IntegerType)
fxg_Graphic.attributes={fxg_Graphic_version, fxg_Graphic_scaleGridTop, fxg_Graphic_scaleGridRight, fxg_Graphic_scaleGridLeft, fxg_Graphic_scaleGridBottom, fxg_Graphic_viewHeight, fxg_Graphic_viewWidth}

# fxg_Matrix class attributes and methods
fxg_Matrix_a: Property = Property(name="a", type=StringType)
fxg_Matrix_b: Property = Property(name="b", type=StringType)
fxg_Matrix_c: Property = Property(name="c", type=StringType)
fxg_Matrix_d: Property = Property(name="d", type=StringType)
fxg_Matrix_tx: Property = Property(name="tx", type=StringType)
fxg_Matrix_ty: Property = Property(name="ty", type=StringType)
fxg_Matrix.attributes={fxg_Matrix_b, fxg_Matrix_ty, fxg_Matrix_d, fxg_Matrix_c, fxg_Matrix_tx, fxg_Matrix_a}

# fxg_ColorTransform class attributes and methods
fxg_ColorTransform_alphaMultiplier: Property = Property(name="alphaMultiplier", type=StringType)
fxg_ColorTransform_alphaOffset: Property = Property(name="alphaOffset", type=StringType)
fxg_ColorTransform_blueMultiplier: Property = Property(name="blueMultiplier", type=StringType)
fxg_ColorTransform_blueOffset: Property = Property(name="blueOffset", type=StringType)
fxg_ColorTransform_greenMultiplier: Property = Property(name="greenMultiplier", type=StringType)
fxg_ColorTransform_greenOffset: Property = Property(name="greenOffset", type=StringType)
fxg_ColorTransform_redMultiplier: Property = Property(name="redMultiplier", type=StringType)
fxg_ColorTransform_redOffset: Property = Property(name="redOffset", type=StringType)
fxg_ColorTransform.attributes={fxg_ColorTransform_blueMultiplier, fxg_ColorTransform_redMultiplier, fxg_ColorTransform_alphaMultiplier, fxg_ColorTransform_redOffset, fxg_ColorTransform_greenOffset, fxg_ColorTransform_greenMultiplier, fxg_ColorTransform_blueOffset, fxg_ColorTransform_alphaOffset}

# fxg_PlaceObject class attributes and methods
fxg_PlaceObject_id: Property = Property(name="id", type=StringType)
fxg_PlaceObject.attributes={fxg_PlaceObject_id}

# fxg_Transform class attributes and methods

# fxg_Filter class attributes and methods

# fxg_Fill class attributes and methods

# fxg_Stroke class attributes and methods

# fxg_Path class attributes and methods
fxg_Path_rotation: Property = Property(name="rotation", type=StringType)
fxg_Path_scaleX: Property = Property(name="scaleX", type=StringType)
fxg_Path_scaleY: Property = Property(name="scaleY", type=StringType)
fxg_Path_blendMode: Property = Property(name="blendMode", type=StringType)
fxg_Path_visible: Property = Property(name="visible", type=StringType)
fxg_Path_alpha: Property = Property(name="alpha", type=StringType)
fxg_Path_winding: Property = Property(name="winding", type=StringType)
fxg_Path_data: Property = Property(name="data", type=StringType)
fxg_Path_x: Property = Property(name="x", type=StringType)
fxg_Path_y: Property = Property(name="y", type=StringType)
fxg_Path.attributes={fxg_Path_x, fxg_Path_rotation, fxg_Path_scaleX, fxg_Path_y, fxg_Path_visible, fxg_Path_blendMode, fxg_Path_winding, fxg_Path_data, fxg_Path_scaleY, fxg_Path_alpha}

# fxg_Ellipse class attributes and methods
fxg_Ellipse_alpha: Property = Property(name="alpha", type=StringType)
fxg_Ellipse_width: Property = Property(name="width", type=StringType)
fxg_Ellipse_height: Property = Property(name="height", type=StringType)
fxg_Ellipse_x: Property = Property(name="x", type=StringType)
fxg_Ellipse_y: Property = Property(name="y", type=StringType)
fxg_Ellipse_rotation: Property = Property(name="rotation", type=StringType)
fxg_Ellipse_scaleX: Property = Property(name="scaleX", type=StringType)
fxg_Ellipse_scaleY: Property = Property(name="scaleY", type=StringType)
fxg_Ellipse_blendMode: Property = Property(name="blendMode", type=StringType)
fxg_Ellipse_visible: Property = Property(name="visible", type=StringType)
fxg_Ellipse.attributes={fxg_Ellipse_width, fxg_Ellipse_scaleX, fxg_Ellipse_y, fxg_Ellipse_height, fxg_Ellipse_x, fxg_Ellipse_rotation, fxg_Ellipse_blendMode, fxg_Ellipse_visible, fxg_Ellipse_scaleY, fxg_Ellipse_alpha}

# fxg_Shape class attributes and methods

# fxg_Rect class attributes and methods
fxg_Rect_width: Property = Property(name="width", type=StringType)
fxg_Rect_height: Property = Property(name="height", type=StringType)
fxg_Rect_radiusX: Property = Property(name="radiusX", type=StringType)
fxg_Rect_radiusY: Property = Property(name="radiusY", type=StringType)
fxg_Rect_topLeftRadiusX: Property = Property(name="topLeftRadiusX", type=StringType)
fxg_Rect_topLeftRadiusY: Property = Property(name="topLeftRadiusY", type=StringType)
fxg_Rect_topRightRadiusX: Property = Property(name="topRightRadiusX", type=StringType)
fxg_Rect_topRightRadiusY: Property = Property(name="topRightRadiusY", type=StringType)
fxg_Rect_bottomLeftRadiusX: Property = Property(name="bottomLeftRadiusX", type=StringType)
fxg_Rect_bottomLeftRadiusY: Property = Property(name="bottomLeftRadiusY", type=StringType)
fxg_Rect_bottomRightRadiusX: Property = Property(name="bottomRightRadiusX", type=StringType)
fxg_Rect_bottomRightRadiusY: Property = Property(name="bottomRightRadiusY", type=StringType)
fxg_Rect_x: Property = Property(name="x", type=StringType)
fxg_Rect_y: Property = Property(name="y", type=StringType)
fxg_Rect_rotation: Property = Property(name="rotation", type=StringType)
fxg_Rect_scaleX: Property = Property(name="scaleX", type=StringType)
fxg_Rect_scaleY: Property = Property(name="scaleY", type=StringType)
fxg_Rect_blendMode: Property = Property(name="blendMode", type=StringType)
fxg_Rect_visible: Property = Property(name="visible", type=StringType)
fxg_Rect_alpha: Property = Property(name="alpha", type=StringType)
fxg_Rect.attributes={fxg_Rect_bottomLeftRadiusY, fxg_Rect_bottomLeftRadiusX, fxg_Rect_bottomRightRadiusY, fxg_Rect_scaleY, fxg_Rect_radiusY, fxg_Rect_visible, fxg_Rect_topLeftRadiusY, fxg_Rect_blendMode, fxg_Rect_topRightRadiusX, fxg_Rect_height, fxg_Rect_radiusX, fxg_Rect_rotation, fxg_Rect_width, fxg_Rect_topLeftRadiusX, fxg_Rect_bottomRightRadiusX, fxg_Rect_scaleX, fxg_Rect_x, fxg_Rect_topRightRadiusY, fxg_Rect_y, fxg_Rect_alpha}

# Shape class attributes and methods

# fxg_RichText class attributes and methods
fxg_RichText_rotation: Property = Property(name="rotation", type=StringType)
fxg_RichText_scaleX: Property = Property(name="scaleX", type=StringType)
fxg_RichText_scaleY: Property = Property(name="scaleY", type=StringType)
fxg_RichText_x: Property = Property(name="x", type=StringType)
fxg_RichText_y: Property = Property(name="y", type=StringType)
fxg_RichText_blendMode: Property = Property(name="blendMode", type=StringType)
fxg_RichText_alpha: Property = Property(name="alpha", type=StringType)
fxg_RichText_id: Property = Property(name="id", type=StringType)
fxg_RichText_maskType: Property = Property(name="maskType", type=StringType)
fxg_RichText_visible: Property = Property(name="visible", type=StringType)
fxg_RichText_width: Property = Property(name="width", type=StringType)
fxg_RichText_height: Property = Property(name="height", type=StringType)
fxg_RichText__tempcontent: Property = Property(name="_tempcontent", type=StringType)
fxg_RichText.attributes={fxg_RichText_y, fxg_RichText_width, fxg_RichText_rotation, fxg_RichText__tempcontent, fxg_RichText_height, fxg_RichText_alpha, fxg_RichText_maskType, fxg_RichText_scaleY, fxg_RichText_blendMode, fxg_RichText_visible, fxg_RichText_scaleX, fxg_RichText_x, fxg_RichText_id}

# ParagraphAttributes class attributes and methods

# ContainerAttributes class attributes and methods

# CharacterAttributes class attributes and methods

# fxg_Line class attributes and methods
fxg_Line_xFrom: Property = Property(name="xFrom", type=StringType)
fxg_Line_yFrom: Property = Property(name="yFrom", type=StringType)
fxg_Line_xTo: Property = Property(name="xTo", type=StringType)
fxg_Line_yTo: Property = Property(name="yTo", type=StringType)
fxg_Line_x: Property = Property(name="x", type=StringType)
fxg_Line_y: Property = Property(name="y", type=StringType)
fxg_Line_rotation: Property = Property(name="rotation", type=StringType)
fxg_Line_scaleX: Property = Property(name="scaleX", type=StringType)
fxg_Line_scaleY: Property = Property(name="scaleY", type=StringType)
fxg_Line_blendMode: Property = Property(name="blendMode", type=StringType)
fxg_Line_alpha: Property = Property(name="alpha", type=StringType)
fxg_Line_id: Property = Property(name="id", type=StringType)
fxg_Line_maskType: Property = Property(name="maskType", type=StringType)
fxg_Line_visible: Property = Property(name="visible", type=StringType)
fxg_Line.attributes={fxg_Line_id, fxg_Line_alpha, fxg_Line_yFrom, fxg_Line_scaleY, fxg_Line_xTo, fxg_Line_maskType, fxg_Line_visible, fxg_Line_xFrom, fxg_Line_yTo, fxg_Line_x, fxg_Line_y, fxg_Line_rotation, fxg_Line_blendMode, fxg_Line_scaleX}

# fxg_CharacterAttributes class attributes and methods
fxg_CharacterAttributes_fontFamily: Property = Property(name="fontFamily", type=StringType)
fxg_CharacterAttributes_fontSize: Property = Property(name="fontSize", type=StringType)
fxg_CharacterAttributes_fontStyle: Property = Property(name="fontStyle", type=StringType)
fxg_CharacterAttributes_fontWeight: Property = Property(name="fontWeight", type=StringType)
fxg_CharacterAttributes_lineHeight: Property = Property(name="lineHeight", type=StringType)
fxg_CharacterAttributes_textDecoration: Property = Property(name="textDecoration", type=StringType)
fxg_CharacterAttributes_lineThrough: Property = Property(name="lineThrough", type=StringType)
fxg_CharacterAttributes_color: Property = Property(name="color", type=StringType)
fxg_CharacterAttributes_textAlpha: Property = Property(name="textAlpha", type=StringType)
fxg_CharacterAttributes_whiteSpaceCollapse: Property = Property(name="whiteSpaceCollapse", type=StringType)
fxg_CharacterAttributes_kerning: Property = Property(name="kerning", type=StringType)
fxg_CharacterAttributes_backgroundAlpha: Property = Property(name="backgroundAlpha", type=StringType)
fxg_CharacterAttributes_backgroundColor: Property = Property(name="backgroundColor", type=StringType)
fxg_CharacterAttributes_baselineShift: Property = Property(name="baselineShift", type=StringType)
fxg_CharacterAttributes_breakOpportunity: Property = Property(name="breakOpportunity", type=StringType)
fxg_CharacterAttributes_digitCase: Property = Property(name="digitCase", type=StringType)
fxg_CharacterAttributes_digitWidth: Property = Property(name="digitWidth", type=StringType)
fxg_CharacterAttributes_dominantBaseline: Property = Property(name="dominantBaseline", type=StringType)
fxg_CharacterAttributes_alignmentBaseline: Property = Property(name="alignmentBaseline", type=StringType)
fxg_CharacterAttributes_ligatureLevel: Property = Property(name="ligatureLevel", type=StringType)
fxg_CharacterAttributes_locale: Property = Property(name="locale", type=StringType)
fxg_CharacterAttributes_typographicCase: Property = Property(name="typographicCase", type=StringType)
fxg_CharacterAttributes_textRotation: Property = Property(name="textRotation", type=StringType)
fxg_CharacterAttributes_trackingLeft: Property = Property(name="trackingLeft", type=StringType)
fxg_CharacterAttributes_trackingRight: Property = Property(name="trackingRight", type=StringType)
fxg_CharacterAttributes.attributes={fxg_CharacterAttributes_backgroundColor, fxg_CharacterAttributes_fontSize, fxg_CharacterAttributes_lineThrough, fxg_CharacterAttributes_alignmentBaseline, fxg_CharacterAttributes_trackingRight, fxg_CharacterAttributes_color, fxg_CharacterAttributes_textAlpha, fxg_CharacterAttributes_dominantBaseline, fxg_CharacterAttributes_backgroundAlpha, fxg_CharacterAttributes_baselineShift, fxg_CharacterAttributes_fontStyle, fxg_CharacterAttributes_fontWeight, fxg_CharacterAttributes_locale, fxg_CharacterAttributes_whiteSpaceCollapse, fxg_CharacterAttributes_typographicCase, fxg_CharacterAttributes_textDecoration, fxg_CharacterAttributes_breakOpportunity, fxg_CharacterAttributes_trackingLeft, fxg_CharacterAttributes_ligatureLevel, fxg_CharacterAttributes_textRotation, fxg_CharacterAttributes_kerning, fxg_CharacterAttributes_digitCase, fxg_CharacterAttributes_digitWidth, fxg_CharacterAttributes_fontFamily, fxg_CharacterAttributes_lineHeight}

# fxg_RichTextContent class attributes and methods

# fxg_RichTextContentContainer class attributes and methods

# RichTextContent class attributes and methods

# fxg_ParagraphAttributes class attributes and methods
fxg_ParagraphAttributes_textAlign: Property = Property(name="textAlign", type=StringType)
fxg_ParagraphAttributes_textAlignLast: Property = Property(name="textAlignLast", type=StringType)
fxg_ParagraphAttributes_textIndent: Property = Property(name="textIndent", type=StringType)
fxg_ParagraphAttributes_paragraphStartIndent: Property = Property(name="paragraphStartIndent", type=StringType)
fxg_ParagraphAttributes_paragraphEndIndent: Property = Property(name="paragraphEndIndent", type=StringType)
fxg_ParagraphAttributes_paragraphSpaceBefore: Property = Property(name="paragraphSpaceBefore", type=StringType)
fxg_ParagraphAttributes_paragraphSpaceAfter: Property = Property(name="paragraphSpaceAfter", type=StringType)
fxg_ParagraphAttributes_justificationRule: Property = Property(name="justificationRule", type=StringType)
fxg_ParagraphAttributes_justificationStyle: Property = Property(name="justificationStyle", type=StringType)
fxg_ParagraphAttributes_textJustify: Property = Property(name="textJustify", type=StringType)
fxg_ParagraphAttributes_leadingModel: Property = Property(name="leadingModel", type=StringType)
fxg_ParagraphAttributes_tabStops: Property = Property(name="tabStops", type=StringType)
fxg_ParagraphAttributes.attributes={fxg_ParagraphAttributes_paragraphEndIndent, fxg_ParagraphAttributes_paragraphSpaceAfter, fxg_ParagraphAttributes_tabStops, fxg_ParagraphAttributes_textAlignLast, fxg_ParagraphAttributes_leadingModel, fxg_ParagraphAttributes_paragraphSpaceBefore, fxg_ParagraphAttributes_textJustify, fxg_ParagraphAttributes_justificationStyle, fxg_ParagraphAttributes_justificationRule, fxg_ParagraphAttributes_paragraphStartIndent, fxg_ParagraphAttributes_textIndent, fxg_ParagraphAttributes_textAlign}

# fxg_ContainerAttributes class attributes and methods
fxg_ContainerAttributes_blockProgression: Property = Property(name="blockProgression", type=StringType)
fxg_ContainerAttributes_paddingLeft: Property = Property(name="paddingLeft", type=StringType)
fxg_ContainerAttributes_paddingRight: Property = Property(name="paddingRight", type=StringType)
fxg_ContainerAttributes_paddingTop: Property = Property(name="paddingTop", type=StringType)
fxg_ContainerAttributes_paddingBottom: Property = Property(name="paddingBottom", type=StringType)
fxg_ContainerAttributes_columnGap: Property = Property(name="columnGap", type=StringType)
fxg_ContainerAttributes_columnCount: Property = Property(name="columnCount", type=StringType)
fxg_ContainerAttributes_columnWidth: Property = Property(name="columnWidth", type=StringType)
fxg_ContainerAttributes_firstBaselineOffset: Property = Property(name="firstBaselineOffset", type=StringType)
fxg_ContainerAttributes_verticalAlign: Property = Property(name="verticalAlign", type=StringType)
fxg_ContainerAttributes_lineBreak: Property = Property(name="lineBreak", type=StringType)
fxg_ContainerAttributes.attributes={fxg_ContainerAttributes_verticalAlign, fxg_ContainerAttributes_paddingTop, fxg_ContainerAttributes_paddingRight, fxg_ContainerAttributes_firstBaselineOffset, fxg_ContainerAttributes_paddingLeft, fxg_ContainerAttributes_columnGap, fxg_ContainerAttributes_columnWidth, fxg_ContainerAttributes_blockProgression, fxg_ContainerAttributes_lineBreak, fxg_ContainerAttributes_columnCount, fxg_ContainerAttributes_paddingBottom}

# fxg_div class attributes and methods

# RichTextContentContainer class attributes and methods

# fxg_p class attributes and methods

# fxg_tcy class attributes and methods

# fxg_a class attributes and methods

# fxg_img class attributes and methods

# fxg_rawtext class attributes and methods
fxg_rawtext__text: Property = Property(name="_text", type=StringType)
fxg_rawtext.attributes={fxg_rawtext__text}

# fxg_LinearGradient class attributes and methods
fxg_LinearGradient_x: Property = Property(name="x", type=StringType)
fxg_LinearGradient_y: Property = Property(name="y", type=StringType)
fxg_LinearGradient_scaleX: Property = Property(name="scaleX", type=StringType)
fxg_LinearGradient_rotation: Property = Property(name="rotation", type=StringType)
fxg_LinearGradient_spreadMethod: Property = Property(name="spreadMethod", type=StringType)
fxg_LinearGradient_interpolationMethod: Property = Property(name="interpolationMethod", type=StringType)
fxg_LinearGradient.attributes={fxg_LinearGradient_rotation, fxg_LinearGradient_interpolationMethod, fxg_LinearGradient_scaleX, fxg_LinearGradient_spreadMethod, fxg_LinearGradient_x, fxg_LinearGradient_y}

# fxg_span class attributes and methods

# fxg_br class attributes and methods

# fxg_tab class attributes and methods

# fxg_linkNormalFormat class attributes and methods

# fxg_linkHoverFormat class attributes and methods

# fxg_linkActiveFormat class attributes and methods

# fxg_BitmapImage class attributes and methods
fxg_BitmapImage_x: Property = Property(name="x", type=StringType)
fxg_BitmapImage_y: Property = Property(name="y", type=StringType)
fxg_BitmapImage_width: Property = Property(name="width", type=StringType)
fxg_BitmapImage_height: Property = Property(name="height", type=StringType)
fxg_BitmapImage_rotation: Property = Property(name="rotation", type=StringType)
fxg_BitmapImage_scaleX: Property = Property(name="scaleX", type=StringType)
fxg_BitmapImage_scaleY: Property = Property(name="scaleY", type=StringType)
fxg_BitmapImage_fillMode: Property = Property(name="fillMode", type=StringType)
fxg_BitmapImage_source: Property = Property(name="source", type=StringType)
fxg_BitmapImage_visible: Property = Property(name="visible", type=StringType)
fxg_BitmapImage_alpha: Property = Property(name="alpha", type=StringType)
fxg_BitmapImage_blendMode: Property = Property(name="blendMode", type=StringType)
fxg_BitmapImage.attributes={fxg_BitmapImage_source, fxg_BitmapImage_scaleX, fxg_BitmapImage_height, fxg_BitmapImage_alpha, fxg_BitmapImage_scaleY, fxg_BitmapImage_y, fxg_BitmapImage_x, fxg_BitmapImage_rotation, fxg_BitmapImage_fillMode, fxg_BitmapImage_blendMode, fxg_BitmapImage_width, fxg_BitmapImage_visible}

# fxg_SolidColor class attributes and methods
fxg_SolidColor_alpha: Property = Property(name="alpha", type=StringType)
fxg_SolidColor_color: Property = Property(name="color", type=StringType)
fxg_SolidColor.attributes={fxg_SolidColor_alpha, fxg_SolidColor_color}

# Fill class attributes and methods

# fxg_SolidColorStroke class attributes and methods
fxg_SolidColorStroke_alpha: Property = Property(name="alpha", type=StringType)
fxg_SolidColorStroke_caps: Property = Property(name="caps", type=StringType)
fxg_SolidColorStroke_color: Property = Property(name="color", type=StringType)
fxg_SolidColorStroke_joints: Property = Property(name="joints", type=StringType)
fxg_SolidColorStroke_miterLimit: Property = Property(name="miterLimit", type=StringType)
fxg_SolidColorStroke_pixelHinting: Property = Property(name="pixelHinting", type=StringType)
fxg_SolidColorStroke_scaleMode: Property = Property(name="scaleMode", type=StringType)
fxg_SolidColorStroke_weight: Property = Property(name="weight", type=StringType)
fxg_SolidColorStroke.attributes={fxg_SolidColorStroke_alpha, fxg_SolidColorStroke_color, fxg_SolidColorStroke_miterLimit, fxg_SolidColorStroke_caps, fxg_SolidColorStroke_joints, fxg_SolidColorStroke_scaleMode, fxg_SolidColorStroke_weight, fxg_SolidColorStroke_pixelHinting}

# Stroke class attributes and methods

# fxg_RadialGradient class attributes and methods
fxg_RadialGradient_x: Property = Property(name="x", type=StringType)
fxg_RadialGradient_y: Property = Property(name="y", type=StringType)
fxg_RadialGradient_scaleX: Property = Property(name="scaleX", type=StringType)
fxg_RadialGradient_scaleY: Property = Property(name="scaleY", type=StringType)
fxg_RadialGradient_rotation: Property = Property(name="rotation", type=StringType)
fxg_RadialGradient_spreadMethod: Property = Property(name="spreadMethod", type=StringType)
fxg_RadialGradient_interpolationMethod: Property = Property(name="interpolationMethod", type=StringType)
fxg_RadialGradient_focalPointRatio: Property = Property(name="focalPointRatio", type=StringType)
fxg_RadialGradient.attributes={fxg_RadialGradient_focalPointRatio, fxg_RadialGradient_x, fxg_RadialGradient_spreadMethod, fxg_RadialGradient_scaleX, fxg_RadialGradient_interpolationMethod, fxg_RadialGradient_y, fxg_RadialGradient_rotation, fxg_RadialGradient_scaleY}

# fxg_BitmapFill class attributes and methods
fxg_BitmapFill_x: Property = Property(name="x", type=StringType)
fxg_BitmapFill_y: Property = Property(name="y", type=StringType)
fxg_BitmapFill_scaleX: Property = Property(name="scaleX", type=StringType)
fxg_BitmapFill_scaleY: Property = Property(name="scaleY", type=StringType)
fxg_BitmapFill_rotation: Property = Property(name="rotation", type=StringType)
fxg_BitmapFill_source: Property = Property(name="source", type=StringType)
fxg_BitmapFill_fillMode: Property = Property(name="fillMode", type=StringType)
fxg_BitmapFill.attributes={fxg_BitmapFill_scaleX, fxg_BitmapFill_y, fxg_BitmapFill_x, fxg_BitmapFill_scaleY, fxg_BitmapFill_source, fxg_BitmapFill_fillMode, fxg_BitmapFill_rotation}

# fxg_GradientEntry class attributes and methods
fxg_GradientEntry_color: Property = Property(name="color", type=StringType)
fxg_GradientEntry_alpha: Property = Property(name="alpha", type=StringType)
fxg_GradientEntry_ratio: Property = Property(name="ratio", type=StringType)
fxg_GradientEntry.attributes={fxg_GradientEntry_alpha, fxg_GradientEntry_ratio, fxg_GradientEntry_color}

# fxg_LinearGradientStroke class attributes and methods
fxg_LinearGradientStroke_x: Property = Property(name="x", type=StringType)
fxg_LinearGradientStroke_y: Property = Property(name="y", type=StringType)
fxg_LinearGradientStroke_scaleX: Property = Property(name="scaleX", type=StringType)
fxg_LinearGradientStroke_rotation: Property = Property(name="rotation", type=StringType)
fxg_LinearGradientStroke_spreadMethod: Property = Property(name="spreadMethod", type=StringType)
fxg_LinearGradientStroke_interpolationMethod: Property = Property(name="interpolationMethod", type=StringType)
fxg_LinearGradientStroke_scaleMode: Property = Property(name="scaleMode", type=StringType)
fxg_LinearGradientStroke_caps: Property = Property(name="caps", type=StringType)
fxg_LinearGradientStroke_joints: Property = Property(name="joints", type=StringType)
fxg_LinearGradientStroke_miterLimit: Property = Property(name="miterLimit", type=StringType)
fxg_LinearGradientStroke_weight: Property = Property(name="weight", type=StringType)
fxg_LinearGradientStroke_pixelHinting: Property = Property(name="pixelHinting", type=StringType)
fxg_LinearGradientStroke.attributes={fxg_LinearGradientStroke_rotation, fxg_LinearGradientStroke_pixelHinting, fxg_LinearGradientStroke_caps, fxg_LinearGradientStroke_joints, fxg_LinearGradientStroke_spreadMethod, fxg_LinearGradientStroke_y, fxg_LinearGradientStroke_scaleX, fxg_LinearGradientStroke_scaleMode, fxg_LinearGradientStroke_miterLimit, fxg_LinearGradientStroke_weight, fxg_LinearGradientStroke_interpolationMethod, fxg_LinearGradientStroke_x}

# fxg_RadialGradientStroke class attributes and methods
fxg_RadialGradientStroke_x: Property = Property(name="x", type=StringType)
fxg_RadialGradientStroke_y: Property = Property(name="y", type=StringType)
fxg_RadialGradientStroke_scaleX: Property = Property(name="scaleX", type=StringType)
fxg_RadialGradientStroke_scaleY: Property = Property(name="scaleY", type=StringType)
fxg_RadialGradientStroke_rotation: Property = Property(name="rotation", type=StringType)
fxg_RadialGradientStroke_spreadMethod: Property = Property(name="spreadMethod", type=StringType)
fxg_RadialGradientStroke_interpolationMethod: Property = Property(name="interpolationMethod", type=StringType)
fxg_RadialGradientStroke_focalPointRatio: Property = Property(name="focalPointRatio", type=StringType)
fxg_RadialGradientStroke_scaleMode: Property = Property(name="scaleMode", type=StringType)
fxg_RadialGradientStroke_caps: Property = Property(name="caps", type=StringType)
fxg_RadialGradientStroke_joints: Property = Property(name="joints", type=StringType)
fxg_RadialGradientStroke_miterLimit: Property = Property(name="miterLimit", type=StringType)
fxg_RadialGradientStroke_weight: Property = Property(name="weight", type=StringType)
fxg_RadialGradientStroke_pixelHinting: Property = Property(name="pixelHinting", type=StringType)
fxg_RadialGradientStroke.attributes={fxg_RadialGradientStroke_scaleMode, fxg_RadialGradientStroke_scaleX, fxg_RadialGradientStroke_y, fxg_RadialGradientStroke_weight, fxg_RadialGradientStroke_caps, fxg_RadialGradientStroke_miterLimit, fxg_RadialGradientStroke_x, fxg_RadialGradientStroke_spreadMethod, fxg_RadialGradientStroke_scaleY, fxg_RadialGradientStroke_interpolationMethod, fxg_RadialGradientStroke_rotation, fxg_RadialGradientStroke_joints, fxg_RadialGradientStroke_pixelHinting, fxg_RadialGradientStroke_focalPointRatio}

# fxg_BlurFilter class attributes and methods
fxg_BlurFilter_blurX: Property = Property(name="blurX", type=StringType)
fxg_BlurFilter_blurY: Property = Property(name="blurY", type=StringType)
fxg_BlurFilter_quality: Property = Property(name="quality", type=StringType)
fxg_BlurFilter.attributes={fxg_BlurFilter_blurY, fxg_BlurFilter_blurX, fxg_BlurFilter_quality}

# Filter class attributes and methods

# fxg_DropShadowFilter class attributes and methods
fxg_DropShadowFilter_alpha: Property = Property(name="alpha", type=StringType)
fxg_DropShadowFilter_angle: Property = Property(name="angle", type=StringType)
fxg_DropShadowFilter_blurX: Property = Property(name="blurX", type=StringType)
fxg_DropShadowFilter_blurY: Property = Property(name="blurY", type=StringType)
fxg_DropShadowFilter_color: Property = Property(name="color", type=StringType)
fxg_DropShadowFilter_distance: Property = Property(name="distance", type=StringType)
fxg_DropShadowFilter_inner: Property = Property(name="inner", type=StringType)
fxg_DropShadowFilter_hideObject: Property = Property(name="hideObject", type=StringType)
fxg_DropShadowFilter_knockout: Property = Property(name="knockout", type=StringType)
fxg_DropShadowFilter_quality: Property = Property(name="quality", type=StringType)
fxg_DropShadowFilter_strength: Property = Property(name="strength", type=StringType)
fxg_DropShadowFilter.attributes={fxg_DropShadowFilter_hideObject, fxg_DropShadowFilter_knockout, fxg_DropShadowFilter_quality, fxg_DropShadowFilter_inner, fxg_DropShadowFilter_distance, fxg_DropShadowFilter_angle, fxg_DropShadowFilter_strength, fxg_DropShadowFilter_color, fxg_DropShadowFilter_blurX, fxg_DropShadowFilter_blurY, fxg_DropShadowFilter_alpha}

# fxg_BevelFilter class attributes and methods
fxg_BevelFilter_highlightAlpha: Property = Property(name="highlightAlpha", type=StringType)
fxg_BevelFilter_highlightColor: Property = Property(name="highlightColor", type=StringType)
fxg_BevelFilter_angle: Property = Property(name="angle", type=StringType)
fxg_BevelFilter_blurX: Property = Property(name="blurX", type=StringType)
fxg_BevelFilter_blurY: Property = Property(name="blurY", type=StringType)
fxg_BevelFilter_distance: Property = Property(name="distance", type=StringType)
fxg_BevelFilter_knockout: Property = Property(name="knockout", type=StringType)
fxg_BevelFilter_quality: Property = Property(name="quality", type=StringType)
fxg_BevelFilter_shadowAlpha: Property = Property(name="shadowAlpha", type=StringType)
fxg_BevelFilter_shadowColor: Property = Property(name="shadowColor", type=StringType)
fxg_BevelFilter_strength: Property = Property(name="strength", type=StringType)
fxg_BevelFilter_type: Property = Property(name="type", type=StringType)
fxg_BevelFilter.attributes={fxg_BevelFilter_highlightColor, fxg_BevelFilter_distance, fxg_BevelFilter_blurY, fxg_BevelFilter_knockout, fxg_BevelFilter_angle, fxg_BevelFilter_shadowAlpha, fxg_BevelFilter_type, fxg_BevelFilter_quality, fxg_BevelFilter_shadowColor, fxg_BevelFilter_strength, fxg_BevelFilter_highlightAlpha, fxg_BevelFilter_blurX}

# fxg_GradientGlowFilter class attributes and methods
fxg_GradientGlowFilter_blurX: Property = Property(name="blurX", type=StringType)
fxg_GradientGlowFilter_blurY: Property = Property(name="blurY", type=StringType)
fxg_GradientGlowFilter_distance: Property = Property(name="distance", type=StringType)
fxg_GradientGlowFilter_angle: Property = Property(name="angle", type=StringType)
fxg_GradientGlowFilter_inner: Property = Property(name="inner", type=StringType)
fxg_GradientGlowFilter_knockout: Property = Property(name="knockout", type=StringType)
fxg_GradientGlowFilter_quality: Property = Property(name="quality", type=StringType)
fxg_GradientGlowFilter_strength: Property = Property(name="strength", type=StringType)
fxg_GradientGlowFilter.attributes={fxg_GradientGlowFilter_strength, fxg_GradientGlowFilter_distance, fxg_GradientGlowFilter_knockout, fxg_GradientGlowFilter_blurY, fxg_GradientGlowFilter_quality, fxg_GradientGlowFilter_inner, fxg_GradientGlowFilter_angle, fxg_GradientGlowFilter_blurX}

# fxg_GradientBevelFilter class attributes and methods
fxg_GradientBevelFilter_angle: Property = Property(name="angle", type=StringType)
fxg_GradientBevelFilter_blurX: Property = Property(name="blurX", type=StringType)
fxg_GradientBevelFilter_blurY: Property = Property(name="blurY", type=StringType)
fxg_GradientBevelFilter_distance: Property = Property(name="distance", type=StringType)
fxg_GradientBevelFilter_knockout: Property = Property(name="knockout", type=StringType)
fxg_GradientBevelFilter_quality: Property = Property(name="quality", type=StringType)
fxg_GradientBevelFilter_strength: Property = Property(name="strength", type=StringType)
fxg_GradientBevelFilter_type: Property = Property(name="type", type=StringType)
fxg_GradientBevelFilter.attributes={fxg_GradientBevelFilter_knockout, fxg_GradientBevelFilter_strength, fxg_GradientBevelFilter_quality, fxg_GradientBevelFilter_blurX, fxg_GradientBevelFilter_type, fxg_GradientBevelFilter_distance, fxg_GradientBevelFilter_angle, fxg_GradientBevelFilter_blurY}

# fxg_ColorMatrixFilter class attributes and methods
fxg_ColorMatrixFilter_matrix: Property = Property(name="matrix", type=StringType)
fxg_ColorMatrixFilter.attributes={fxg_ColorMatrixFilter_matrix}

# fxg_FXGElement class attributes and methods

# fxg_ContainerElement class attributes and methods

# Relationships
mask0: BinaryAssociation = BinaryAssociation(
    name="mask0",
    ends={
        Property(name="fxg_Group", type=fxg_Graphic, multiplicity=Multiplicity(1, 1)),
        Property(name="fxg_Graphic", type=fxg_Group, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mask6: BinaryAssociation = BinaryAssociation(
    name="mask6",
    ends={
        Property(name="fxg_Group7", type=fxg_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="fxg_Group5", type=fxg_Group, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
matrix8: BinaryAssociation = BinaryAssociation(
    name="matrix8",
    ends={
        Property(name="fxg_Matrix", type=fxg_Transform, multiplicity=Multiplicity(1, 1)),
        Property(name="fxg_Transform9", type=fxg_Matrix, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
colorTransform10: BinaryAssociation = BinaryAssociation(
    name="colorTransform10",
    ends={
        Property(name="fxg_ColorTransform", type=fxg_Transform, multiplicity=Multiplicity(1, 1)),
        Property(name="fxg_Transform11", type=fxg_ColorTransform, multiplicity=Multiplicity(0, 1))
    }
)
transform1: BinaryAssociation = BinaryAssociation(
    name="transform1",
    ends={
        Property(name="fxg_Transform", type=fxg_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="fxg_Group2", type=fxg_Transform, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
filters3: BinaryAssociation = BinaryAssociation(
    name="filters3",
    ends={
        Property(name="fxg_Filter", type=fxg_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="fxg_Group4", type=fxg_Filter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fill20: BinaryAssociation = BinaryAssociation(
    name="fill20",
    ends={
        Property(name="fxg_Fill", type=fxg_Path, multiplicity=Multiplicity(1, 1)),
        Property(name="fxg_Path", type=fxg_Fill, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stroke21: BinaryAssociation = BinaryAssociation(
    name="stroke21",
    ends={
        Property(name="fxg_Stroke", type=fxg_Path, multiplicity=Multiplicity(1, 1)),
        Property(name="fxg_Path22", type=fxg_Stroke, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transform12: BinaryAssociation = BinaryAssociation(
    name="transform12",
    ends={
        Property(name="fxg_Transform13", type=fxg_PlaceObject, multiplicity=Multiplicity(1, 1)),
        Property(name="fxg_PlaceObject", type=fxg_Transform, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
filters14: BinaryAssociation = BinaryAssociation(
    name="filters14",
    ends={
        Property(name="fxg_Filter16", type=fxg_PlaceObject, multiplicity=Multiplicity(1, 1)),
        Property(name="fxg_PlaceObject15", type=fxg_Filter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mask17: BinaryAssociation = BinaryAssociation(
    name="mask17",
    ends={
        Property(name="fxg_Group19", type=fxg_PlaceObject, multiplicity=Multiplicity(1, 1)),
        Property(name="fxg_PlaceObject18", type=fxg_Group, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
filters34: BinaryAssociation = BinaryAssociation(
    name="filters34",
    ends={
        Property(name="fxg_Filter36", type=fxg_Rect, multiplicity=Multiplicity(1, 1)),
        Property(name="fxg_Rect35", type=fxg_Filter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fill37: BinaryAssociation = BinaryAssociation(
    name="fill37",
    ends={
        Property(name="fxg_Fill39", type=fxg_Rect, multiplicity=Multiplicity(1, 1)),
        Property(name="fxg_Rect38", type=fxg_Fill, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stroke40: BinaryAssociation = BinaryAssociation(
    name="stroke40",
    ends={
        Property(name="fxg_Stroke42", type=fxg_Rect, multiplicity=Multiplicity(1, 1)),
        Property(name="fxg_Rect41", type=fxg_Stroke, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mask43: BinaryAssociation = BinaryAssociation(
    name="mask43",
    ends={
        Property(name="fxg_Group45", type=fxg_Rect, multiplicity=Multiplicity(1, 1)),
        Property(name="fxg_Rect44", type=fxg_Group, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
filters23: BinaryAssociation = BinaryAssociation(
    name="filters23",
    ends={
        Property(name="fxg_Filter25", type=fxg_Path, multiplicity=Multiplicity(1, 1)),
        Property(name="fxg_Path24", type=fxg_Filter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transform26: BinaryAssociation = BinaryAssociation(
    name="transform26",
    ends={
        Property(name="fxg_Transform28", type=fxg_Path, multiplicity=Multiplicity(1, 1)),
        Property(name="fxg_Path27", type=fxg_Transform, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mask29: BinaryAssociation = BinaryAssociation(
    name="mask29",
    ends={
        Property(name="fxg_Group31", type=fxg_Path, multiplicity=Multiplicity(1, 1)),
        Property(name="fxg_Path30", type=fxg_Group, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transform32: BinaryAssociation = BinaryAssociation(
    name="transform32",
    ends={
        Property(name="fxg_Transform33", type=fxg_Rect, multiplicity=Multiplicity(1, 1)),
        Property(name="fxg_Rect", type=fxg_Transform, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
filters62: BinaryAssociation = BinaryAssociation(
    name="filters62",
    ends={
        Property(name="fxg_Filter64", type=fxg_Line, multiplicity=Multiplicity(1, 1)),
        Property(name="fxg_Line63", type=fxg_Filter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fill65: BinaryAssociation = BinaryAssociation(
    name="fill65",
    ends={
        Property(name="fxg_Fill67", type=fxg_Line, multiplicity=Multiplicity(1, 1)),
        Property(name="fxg_Line66", type=fxg_Fill, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stroke68: BinaryAssociation = BinaryAssociation(
    name="stroke68",
    ends={
        Property(name="fxg_Stroke70", type=fxg_Line, multiplicity=Multiplicity(1, 1)),
        Property(name="fxg_Line69", type=fxg_Stroke, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mask71: BinaryAssociation = BinaryAssociation(
    name="mask71",
    ends={
        Property(name="fxg_Group73", type=fxg_Line, multiplicity=Multiplicity(1, 1)),
        Property(name="fxg_Line72", type=fxg_Group, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transform46: BinaryAssociation = BinaryAssociation(
    name="transform46",
    ends={
        Property(name="fxg_Transform47", type=fxg_Ellipse, multiplicity=Multiplicity(1, 1)),
        Property(name="fxg_Ellipse", type=fxg_Transform, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
filters48: BinaryAssociation = BinaryAssociation(
    name="filters48",
    ends={
        Property(name="fxg_Filter50", type=fxg_Ellipse, multiplicity=Multiplicity(1, 1)),
        Property(name="fxg_Ellipse49", type=fxg_Filter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fill51: BinaryAssociation = BinaryAssociation(
    name="fill51",
    ends={
        Property(name="fxg_Fill53", type=fxg_Ellipse, multiplicity=Multiplicity(1, 1)),
        Property(name="fxg_Ellipse52", type=fxg_Fill, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stroke54: BinaryAssociation = BinaryAssociation(
    name="stroke54",
    ends={
        Property(name="fxg_Stroke56", type=fxg_Ellipse, multiplicity=Multiplicity(1, 1)),
        Property(name="fxg_Ellipse55", type=fxg_Stroke, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mask57: BinaryAssociation = BinaryAssociation(
    name="mask57",
    ends={
        Property(name="fxg_Group59", type=fxg_Ellipse, multiplicity=Multiplicity(1, 1)),
        Property(name="fxg_Ellipse58", type=fxg_Group, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transform60: BinaryAssociation = BinaryAssociation(
    name="transform60",
    ends={
        Property(name="fxg_Transform61", type=fxg_Line, multiplicity=Multiplicity(1, 1)),
        Property(name="fxg_Line", type=fxg_Transform, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
content74: BinaryAssociation = BinaryAssociation(
    name="content74",
    ends={
        Property(name="fxg_RichTextContent", type=fxg_RichText, multiplicity=Multiplicity(1, 1)),
        Property(name="fxg_RichText", type=fxg_RichTextContent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
_children75: BinaryAssociation = BinaryAssociation(
    name="_children75",
    ends={
        Property(name="fxg_RichTextContent76", type=fxg_RichTextContentContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="fxg_RichTextContentContainer", type=fxg_RichTextContent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
matrix77: BinaryAssociation = BinaryAssociation(
    name="matrix77",
    ends={
        Property(name="fxg_Matrix78", type=fxg_LinearGradient, multiplicity=Multiplicity(1, 1)),
        Property(name="fxg_LinearGradient", type=fxg_Matrix, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
matrix79: BinaryAssociation = BinaryAssociation(
    name="matrix79",
    ends={
        Property(name="fxg_Matrix80", type=fxg_RadialGradient, multiplicity=Multiplicity(1, 1)),
        Property(name="fxg_RadialGradient", type=fxg_Matrix, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
matrix81: BinaryAssociation = BinaryAssociation(
    name="matrix81",
    ends={
        Property(name="fxg_Matrix82", type=fxg_BitmapFill, multiplicity=Multiplicity(1, 1)),
        Property(name="fxg_BitmapFill", type=fxg_Matrix, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
matrix83: BinaryAssociation = BinaryAssociation(
    name="matrix83",
    ends={
        Property(name="fxg_Matrix84", type=fxg_LinearGradientStroke, multiplicity=Multiplicity(1, 1)),
        Property(name="fxg_LinearGradientStroke", type=fxg_Matrix, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
matrix85: BinaryAssociation = BinaryAssociation(
    name="matrix85",
    ends={
        Property(name="fxg_Matrix86", type=fxg_RadialGradientStroke, multiplicity=Multiplicity(1, 1)),
        Property(name="fxg_RadialGradientStroke", type=fxg_Matrix, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_fxg_Private_FXGElement = Generalization(general=FXGElement, specific=fxg_Private)
gen_fxg_Transform_FXGElement = Generalization(general=FXGElement, specific=fxg_Transform)
gen_fxg_PlaceObject_FXGElement = Generalization(general=FXGElement, specific=fxg_PlaceObject)
gen_fxg_Matrix_FXGElement = Generalization(general=FXGElement, specific=fxg_Matrix)
gen_fxg_Path_FXGElement = Generalization(general=FXGElement, specific=fxg_Path)
gen_fxg_Ellipse_Shape = Generalization(general=Shape, specific=fxg_Ellipse)
gen_fxg_Shape_FXGElement = Generalization(general=FXGElement, specific=fxg_Shape)
gen_fxg_Rect_Shape = Generalization(general=Shape, specific=fxg_Rect)
gen_fxg_RichText_FXGElement = Generalization(general=FXGElement, specific=fxg_RichText)
gen_fxg_RichText_ParagraphAttributes = Generalization(general=ParagraphAttributes, specific=fxg_RichText)
gen_fxg_RichText_ContainerAttributes = Generalization(general=ContainerAttributes, specific=fxg_RichText)
gen_fxg_RichText_CharacterAttributes = Generalization(general=CharacterAttributes, specific=fxg_RichText)
gen_fxg_Line_Shape = Generalization(general=Shape, specific=fxg_Line)
gen_fxg_RichTextContentContainer_RichTextContent = Generalization(general=RichTextContent, specific=fxg_RichTextContentContainer)
gen_fxg_div_RichTextContent = Generalization(general=RichTextContent, specific=fxg_div)
gen_fxg_div_RichTextContentContainer = Generalization(general=RichTextContentContainer, specific=fxg_div)
gen_fxg_p_RichTextContent = Generalization(general=RichTextContent, specific=fxg_p)
gen_fxg_p_RichTextContentContainer = Generalization(general=RichTextContentContainer, specific=fxg_p)
gen_fxg_p_ParagraphAttributes = Generalization(general=ParagraphAttributes, specific=fxg_p)
gen_fxg_tcy_RichTextContent = Generalization(general=RichTextContent, specific=fxg_tcy)
gen_fxg_tcy_RichTextContentContainer = Generalization(general=RichTextContentContainer, specific=fxg_tcy)
gen_fxg_a_RichTextContent = Generalization(general=RichTextContent, specific=fxg_a)
gen_fxg_a_RichTextContentContainer = Generalization(general=RichTextContentContainer, specific=fxg_a)
gen_fxg_img_RichTextContent = Generalization(general=RichTextContent, specific=fxg_img)
gen_fxg_rawtext_RichTextContent = Generalization(general=RichTextContent, specific=fxg_rawtext)
gen_fxg_span_RichTextContent = Generalization(general=RichTextContent, specific=fxg_span)
gen_fxg_span_RichTextContentContainer = Generalization(general=RichTextContentContainer, specific=fxg_span)
gen_fxg_br_RichTextContent = Generalization(general=RichTextContent, specific=fxg_br)
gen_fxg_tab_RichTextContent = Generalization(general=RichTextContent, specific=fxg_tab)
gen_fxg_linkNormalFormat_RichTextContent = Generalization(general=RichTextContent, specific=fxg_linkNormalFormat)
gen_fxg_linkHoverFormat_RichTextContent = Generalization(general=RichTextContent, specific=fxg_linkHoverFormat)
gen_fxg_BitmapImage_FXGElement = Generalization(general=FXGElement, specific=fxg_BitmapImage)
gen_fxg_Fill_FXGElement = Generalization(general=FXGElement, specific=fxg_Fill)
gen_fxg_SolidColor_Fill = Generalization(general=Fill, specific=fxg_SolidColor)
gen_fxg_SolidColorStroke_Stroke = Generalization(general=Stroke, specific=fxg_SolidColorStroke)
gen_fxg_BitmapFill_Fill = Generalization(general=Fill, specific=fxg_BitmapFill)
gen_fxg_Stroke_FXGElement = Generalization(general=FXGElement, specific=fxg_Stroke)
gen_fxg_GradientEntry_FXGElement = Generalization(general=FXGElement, specific=fxg_GradientEntry)
gen_fxg_ColorTransform_FXGElement = Generalization(general=FXGElement, specific=fxg_ColorTransform)
gen_fxg_Filter_FXGElement = Generalization(general=FXGElement, specific=fxg_Filter)
gen_fxg_BlurFilter_Filter = Generalization(general=Filter, specific=fxg_BlurFilter)
gen_fxg_DropShadowFilter_Filter = Generalization(general=Filter, specific=fxg_DropShadowFilter)
gen_fxg_BevelFilter_Filter = Generalization(general=Filter, specific=fxg_BevelFilter)
gen_fxg_ColorMatrixFilter_Filter = Generalization(general=Filter, specific=fxg_ColorMatrixFilter)
gen_fxg_ContainerElement_FXGElement = Generalization(general=FXGElement, specific=fxg_ContainerElement)

# Domain Model
domain_model = DomainModel(
    name="fxg",
    types={fxg_Group, fxg_Library, fxg_Private, FXGElement, fxg_Definition, fxg_Graphic, fxg_Matrix, fxg_ColorTransform, fxg_PlaceObject, fxg_Transform, fxg_Filter, fxg_Fill, fxg_Stroke, fxg_Path, fxg_Ellipse, fxg_Shape, fxg_Rect, Shape, fxg_RichText, ParagraphAttributes, ContainerAttributes, CharacterAttributes, fxg_Line, fxg_CharacterAttributes, fxg_RichTextContent, fxg_RichTextContentContainer, RichTextContent, fxg_ParagraphAttributes, fxg_ContainerAttributes, fxg_div, RichTextContentContainer, fxg_p, fxg_tcy, fxg_a, fxg_img, fxg_rawtext, fxg_LinearGradient, fxg_span, fxg_br, fxg_tab, fxg_linkNormalFormat, fxg_linkHoverFormat, fxg_linkActiveFormat, fxg_BitmapImage, fxg_SolidColor, Fill, fxg_SolidColorStroke, Stroke, fxg_RadialGradient, fxg_BitmapFill, fxg_GradientEntry, fxg_LinearGradientStroke, fxg_RadialGradientStroke, fxg_BlurFilter, Filter, fxg_DropShadowFilter, fxg_BevelFilter, fxg_GradientGlowFilter, fxg_GradientBevelFilter, fxg_ColorMatrixFilter, fxg_FXGElement, fxg_ContainerElement, Winding, MaskType, BlendMode, Cap, Joint, FontStyle, FontWeight, TextDecoration, WhitespaceCollapse, Kerning, SpreadMethod, InterpolationMethod, JustificationRule, JustificationStyle, ScaleMode, BevelFilterType, FillMode, TextAlign, LineBreak, BreakOpportunity, TextJustify, LeadingModel, BlockProgression, VerticalAlign, LigatureLevel, DigitCase, DigitWidth, DominantBaseline, AlignmentBaseline, TypographicCase, TextRotation},
    associations={mask0, mask6, matrix8, colorTransform10, transform1, filters3, fill20, stroke21, transform12, filters14, mask17, filters34, fill37, stroke40, mask43, filters23, transform26, mask29, transform32, filters62, fill65, stroke68, mask71, transform46, filters48, fill51, stroke54, mask57, transform60, content74, _children75, matrix77, matrix79, matrix81, matrix83, matrix85},
    generalizations={gen_fxg_Private_FXGElement, gen_fxg_Transform_FXGElement, gen_fxg_PlaceObject_FXGElement, gen_fxg_Matrix_FXGElement, gen_fxg_Path_FXGElement, gen_fxg_Ellipse_Shape, gen_fxg_Shape_FXGElement, gen_fxg_Rect_Shape, gen_fxg_RichText_FXGElement, gen_fxg_RichText_ParagraphAttributes, gen_fxg_RichText_ContainerAttributes, gen_fxg_RichText_CharacterAttributes, gen_fxg_Line_Shape, gen_fxg_RichTextContentContainer_RichTextContent, gen_fxg_div_RichTextContent, gen_fxg_div_RichTextContentContainer, gen_fxg_p_RichTextContent, gen_fxg_p_RichTextContentContainer, gen_fxg_p_ParagraphAttributes, gen_fxg_tcy_RichTextContent, gen_fxg_tcy_RichTextContentContainer, gen_fxg_a_RichTextContent, gen_fxg_a_RichTextContentContainer, gen_fxg_img_RichTextContent, gen_fxg_rawtext_RichTextContent, gen_fxg_span_RichTextContent, gen_fxg_span_RichTextContentContainer, gen_fxg_br_RichTextContent, gen_fxg_tab_RichTextContent, gen_fxg_linkNormalFormat_RichTextContent, gen_fxg_linkHoverFormat_RichTextContent, gen_fxg_BitmapImage_FXGElement, gen_fxg_Fill_FXGElement, gen_fxg_SolidColor_Fill, gen_fxg_SolidColorStroke_Stroke, gen_fxg_BitmapFill_Fill, gen_fxg_Stroke_FXGElement, gen_fxg_GradientEntry_FXGElement, gen_fxg_ColorTransform_FXGElement, gen_fxg_Filter_FXGElement, gen_fxg_BlurFilter_Filter, gen_fxg_DropShadowFilter_Filter, gen_fxg_BevelFilter_Filter, gen_fxg_ColorMatrixFilter_Filter, gen_fxg_ContainerElement_FXGElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)