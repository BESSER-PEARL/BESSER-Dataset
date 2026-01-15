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
FontDecoration: Enumeration = Enumeration(
    name="FontDecoration",
    literals={
            EnumerationLiteral(name="underline"),
			EnumerationLiteral(name="overline"),
			EnumerationLiteral(name="lineThrough")
    }
)

ElementKind: Enumeration = Enumeration(
    name="ElementKind",
    literals={
            EnumerationLiteral(name="canvas"),
			EnumerationLiteral(name="circle"),
			EnumerationLiteral(name="clipPath"),
			EnumerationLiteral(name="ellipse"),
			EnumerationLiteral(name="group"),
			EnumerationLiteral(name="image"),
			EnumerationLiteral(name="line"),
			EnumerationLiteral(name="marker"),
			EnumerationLiteral(name="path"),
			EnumerationLiteral(name="polygon"),
			EnumerationLiteral(name="polyline"),
			EnumerationLiteral(name="rectangle"),
			EnumerationLiteral(name="text"),
			EnumerationLiteral(name="use")
    }
)

TextAnchor: Enumeration = Enumeration(
    name="TextAnchor",
    literals={
            EnumerationLiteral(name="start"),
			EnumerationLiteral(name="middle"),
			EnumerationLiteral(name="end")
    }
)

# Classes
dg_Canvas = Class(name="dg::Canvas")
Group = Class(name="Group")
dg_ClipPath = Class(name="dg::ClipPath")
dg_Bounds = Class(name="dg::Bounds")
dg_Group = Class(name="dg::Group")
GraphicalElement = Class(name="GraphicalElement")
dg_GraphicalElement = Class(name="dg::GraphicalElement", is_abstract=True)
Definition = Class(name="Definition")
dg_MoveTo = Class(name="dg::MoveTo")
PathCommand = Class(name="PathCommand")
dg_Style = Class(name="dg::Style")
dg_Transform = Class(name="dg::Transform", is_abstract=True)
dg_Definition = Class(name="dg::Definition", is_abstract=True)
dg_Point = Class(name="dg::Point")
dg_PathCommand = Class(name="dg::PathCommand", is_abstract=True)
dg_Paint = Class(name="dg::Paint")
dg_PaintServer = Class(name="dg::PaintServer", is_abstract=True)
dg_Circle = Class(name="dg::Circle")
dg_Definitions = Class(name="dg::Definitions")
dg_ClosePath = Class(name="dg::ClosePath")
dg_CubicCurveTo = Class(name="dg::CubicCurveTo")
dg_StyleSheet = Class(name="dg::StyleSheet")
dg_StyleRule = Class(name="dg::StyleRule")
dg_StyleSelector = Class(name="dg::StyleSelector")
dg_Ellipse = Class(name="dg::Ellipse")
dg_Dimension = Class(name="dg::Dimension")
dg_EllipticalArcTo = Class(name="dg::EllipticalArcTo")
dg_GradientStop = Class(name="dg::GradientStop")
dg_QuadraticCurveTo = Class(name="dg::QuadraticCurveTo")
dg_Gradient = Class(name="dg::Gradient", is_abstract=True)
PaintServer = Class(name="PaintServer")
dg_Image = Class(name="dg::Image")
dg_Line = Class(name="dg::Line")
MarkedElement = Class(name="MarkedElement")
dg_MarkedElement = Class(name="dg::MarkedElement", is_abstract=True)
dg_LinearGradient = Class(name="dg::LinearGradient")
Gradient = Class(name="Gradient")
dg_Marker = Class(name="dg::Marker")
dg_Path = Class(name="dg::Path")
dg_LineTo = Class(name="dg::LineTo")
dg_Matrix = Class(name="dg::Matrix")
Transform = Class(name="Transform")
dg_Pattern = Class(name="dg::Pattern")
dg_Polygon = Class(name="dg::Polygon")
dg_Polyline = Class(name="dg::Polyline")
dg_RadialGradient = Class(name="dg::RadialGradient")
dg_Rectangle = Class(name="dg::Rectangle")
dg_Rotate = Class(name="dg::Rotate")
dg_RootCanvas = Class(name="dg::RootCanvas")
Canvas = Class(name="Canvas")
dg_Skew = Class(name="dg::Skew")
dg_Scale = Class(name="dg::Scale")
dg_Text = Class(name="dg::Text")
dg_Translate = Class(name="dg::Translate")
dg_Use = Class(name="dg::Use")

# dg_Canvas class attributes and methods
dg_Canvas_m_canvasCannotHaveTransforms: Method = Method(name="canvasCannotHaveTransforms", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
dg_Canvas.methods={dg_Canvas_m_canvasCannotHaveTransforms}

# Group class attributes and methods

# dg_ClipPath class attributes and methods

# dg_Bounds class attributes and methods

# dg_Group class attributes and methods
dg_Group_layout: Property = Property(name="layout", type=StringType)
dg_Group.attributes={dg_Group_layout}

# GraphicalElement class attributes and methods

# dg_GraphicalElement class attributes and methods
dg_GraphicalElement_class: Property = Property(name="class", type=StringType)
dg_GraphicalElement_layoutData: Property = Property(name="layoutData", type=StringType)
dg_GraphicalElement_m_referencedClippathHasId: Method = Method(name="referencedClippathHasId", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
dg_GraphicalElement.attributes={dg_GraphicalElement_layoutData, dg_GraphicalElement_class}
dg_GraphicalElement.methods={dg_GraphicalElement_m_referencedClippathHasId}

# Definition class attributes and methods

# dg_MoveTo class attributes and methods

# PathCommand class attributes and methods

# dg_Style class attributes and methods
dg_Style_fontName: Property = Property(name="fontName", type=StringType)
dg_Style_fontItalic: Property = Property(name="fontItalic", type=StringType)
dg_Style_fontBold: Property = Property(name="fontBold", type=StringType)
dg_Style_fillOpacity: Property = Property(name="fillOpacity", type=StringType)
dg_Style_strokeWidth: Property = Property(name="strokeWidth", type=StringType)
dg_Style_strokeOpacity: Property = Property(name="strokeOpacity", type=StringType)
dg_Style_strokeDashLength: Property = Property(name="strokeDashLength", type=StringType)
dg_Style_fontSize: Property = Property(name="fontSize", type=StringType)
dg_Style_fontDecoration: Property = Property(name="fontDecoration", type=StringType)
dg_Style_m_validFillOpacity: Method = Method(name="validFillOpacity", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
dg_Style_m_validStrokeWidth: Method = Method(name="validStrokeWidth", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
dg_Style_m_validFontSize: Method = Method(name="validFontSize", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
dg_Style_m_validDashLengthSize: Method = Method(name="validDashLengthSize", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
dg_Style_m_validStrokeOpacity: Method = Method(name="validStrokeOpacity", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
dg_Style.attributes={dg_Style_fontName, dg_Style_strokeDashLength, dg_Style_fontSize, dg_Style_fontBold, dg_Style_fontDecoration, dg_Style_strokeWidth, dg_Style_strokeOpacity, dg_Style_fontItalic, dg_Style_fillOpacity}
dg_Style.methods={dg_Style_m_validFontSize, dg_Style_m_validFillOpacity, dg_Style_m_validStrokeWidth, dg_Style_m_validDashLengthSize, dg_Style_m_validStrokeOpacity}

# dg_Transform class attributes and methods

# dg_Definition class attributes and methods
dg_Definition_id: Property = Property(name="id", type=StringType)
dg_Definition_m_idCannotBeEmpty: Method = Method(name="idCannotBeEmpty", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
dg_Definition.attributes={dg_Definition_id}
dg_Definition.methods={dg_Definition_m_idCannotBeEmpty}

# dg_Point class attributes and methods

# dg_PathCommand class attributes and methods
dg_PathCommand_isRelative: Property = Property(name="isRelative", type=StringType)
dg_PathCommand.attributes={dg_PathCommand_isRelative}

# dg_Paint class attributes and methods
dg_Paint_color: Property = Property(name="color", type=StringType)
dg_Paint_m_referencedPaintServerHasId: Method = Method(name="referencedPaintServerHasId", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
dg_Paint.attributes={dg_Paint_color}
dg_Paint.methods={dg_Paint_m_referencedPaintServerHasId}

# dg_PaintServer class attributes and methods

# dg_Circle class attributes and methods
dg_Circle_radius: Property = Property(name="radius", type=StringType)
dg_Circle_m_nonNegativeRadius: Method = Method(name="nonNegativeRadius", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
dg_Circle.attributes={dg_Circle_radius}
dg_Circle.methods={dg_Circle_m_nonNegativeRadius}

# dg_Definitions class attributes and methods

# dg_ClosePath class attributes and methods

# dg_CubicCurveTo class attributes and methods

# dg_StyleSheet class attributes and methods

# dg_StyleRule class attributes and methods

# dg_StyleSelector class attributes and methods
dg_StyleSelector_kind: Property = Property(name="kind", type=StringType)
dg_StyleSelector_class: Property = Property(name="class", type=StringType)
dg_StyleSelector.attributes={dg_StyleSelector_class, dg_StyleSelector_kind}

# dg_Ellipse class attributes and methods

# dg_Dimension class attributes and methods

# dg_EllipticalArcTo class attributes and methods
dg_EllipticalArcTo_rotation: Property = Property(name="rotation", type=StringType)
dg_EllipticalArcTo_isLargeArc: Property = Property(name="isLargeArc", type=StringType)
dg_EllipticalArcTo_isSweep: Property = Property(name="isSweep", type=StringType)
dg_EllipticalArcTo.attributes={dg_EllipticalArcTo_rotation, dg_EllipticalArcTo_isSweep, dg_EllipticalArcTo_isLargeArc}

# dg_GradientStop class attributes and methods
dg_GradientStop_offset: Property = Property(name="offset", type=StringType)
dg_GradientStop_opacity: Property = Property(name="opacity", type=StringType)
dg_GradientStop_color: Property = Property(name="color", type=StringType)
dg_GradientStop_m_validOffset: Method = Method(name="validOffset", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
dg_GradientStop_m_validOpacity: Method = Method(name="validOpacity", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
dg_GradientStop.attributes={dg_GradientStop_opacity, dg_GradientStop_offset, dg_GradientStop_color}
dg_GradientStop.methods={dg_GradientStop_m_validOpacity, dg_GradientStop_m_validOffset}

# dg_QuadraticCurveTo class attributes and methods

# dg_Gradient class attributes and methods

# PaintServer class attributes and methods

# dg_Image class attributes and methods
dg_Image_source: Property = Property(name="source", type=StringType)
dg_Image_isAspectRatioPreserved: Property = Property(name="isAspectRatioPreserved", type=StringType)
dg_Image_m_sourceCannotBeEmpty: Method = Method(name="sourceCannotBeEmpty", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
dg_Image.attributes={dg_Image_source, dg_Image_isAspectRatioPreserved}
dg_Image.methods={dg_Image_m_sourceCannotBeEmpty}

# dg_Line class attributes and methods

# MarkedElement class attributes and methods

# dg_MarkedElement class attributes and methods
dg_MarkedElement_m_referencedMidMarkerHasId: Method = Method(name="referencedMidMarkerHasId", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
dg_MarkedElement_m_referencedEndMarkerHasId: Method = Method(name="referencedEndMarkerHasId", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
dg_MarkedElement_m_referencedStartMarkerHasId: Method = Method(name="referencedStartMarkerHasId", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
dg_MarkedElement.methods={dg_MarkedElement_m_referencedMidMarkerHasId, dg_MarkedElement_m_referencedEndMarkerHasId, dg_MarkedElement_m_referencedStartMarkerHasId}

# dg_LinearGradient class attributes and methods
dg_LinearGradient_m_validGradientVector: Method = Method(name="validGradientVector", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
dg_LinearGradient.methods={dg_LinearGradient_m_validGradientVector}

# Gradient class attributes and methods

# dg_Marker class attributes and methods

# dg_Path class attributes and methods
dg_Path_m_firstCommandMustBeMove: Method = Method(name="firstCommandMustBeMove", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
dg_Path.methods={dg_Path_m_firstCommandMustBeMove}

# dg_LineTo class attributes and methods

# dg_Matrix class attributes and methods
dg_Matrix_c: Property = Property(name="c", type=StringType)
dg_Matrix_d: Property = Property(name="d", type=StringType)
dg_Matrix_e: Property = Property(name="e", type=StringType)
dg_Matrix_f: Property = Property(name="f", type=StringType)
dg_Matrix_a: Property = Property(name="a", type=StringType)
dg_Matrix_b: Property = Property(name="b", type=StringType)
dg_Matrix.attributes={dg_Matrix_c, dg_Matrix_f, dg_Matrix_e, dg_Matrix_a, dg_Matrix_b, dg_Matrix_d}

# Transform class attributes and methods

# dg_Pattern class attributes and methods

# dg_Polygon class attributes and methods

# dg_Polyline class attributes and methods

# dg_RadialGradient class attributes and methods
dg_RadialGradient_radius: Property = Property(name="radius", type=StringType)
dg_RadialGradient_m_validFocusPoint: Method = Method(name="validFocusPoint", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
dg_RadialGradient_m_validCenterPoint: Method = Method(name="validCenterPoint", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
dg_RadialGradient_m_validRadius: Method = Method(name="validRadius", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
dg_RadialGradient.attributes={dg_RadialGradient_radius}
dg_RadialGradient.methods={dg_RadialGradient_m_validCenterPoint, dg_RadialGradient_m_validRadius, dg_RadialGradient_m_validFocusPoint}

# dg_Rectangle class attributes and methods
dg_Rectangle_cornerRadius: Property = Property(name="cornerRadius", type=StringType)
dg_Rectangle_m_nonNegativeCornerRadius: Method = Method(name="nonNegativeCornerRadius", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
dg_Rectangle.attributes={dg_Rectangle_cornerRadius}
dg_Rectangle.methods={dg_Rectangle_m_nonNegativeCornerRadius}

# dg_Rotate class attributes and methods
dg_Rotate_angle: Property = Property(name="angle", type=StringType)
dg_Rotate.attributes={dg_Rotate_angle}

# dg_RootCanvas class attributes and methods
dg_RootCanvas_script: Property = Property(name="script", type=StringType)
dg_RootCanvas_backgroundColor: Property = Property(name="backgroundColor", type=StringType)
dg_RootCanvas.attributes={dg_RootCanvas_backgroundColor, dg_RootCanvas_script}

# Canvas class attributes and methods

# dg_Skew class attributes and methods
dg_Skew_angleX: Property = Property(name="angleX", type=StringType)
dg_Skew_angleY: Property = Property(name="angleY", type=StringType)
dg_Skew.attributes={dg_Skew_angleX, dg_Skew_angleY}

# dg_Scale class attributes and methods
dg_Scale_factorY: Property = Property(name="factorY", type=StringType)
dg_Scale_factorX: Property = Property(name="factorX", type=StringType)
dg_Scale_m_nonnegativescale: Method = Method(name="nonnegativescale", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
dg_Scale.attributes={dg_Scale_factorY, dg_Scale_factorX}
dg_Scale.methods={dg_Scale_m_nonnegativescale}

# dg_Text class attributes and methods
dg_Text_anchor: Property = Property(name="anchor", type=StringType)
dg_Text_data: Property = Property(name="data", type=StringType)
dg_Text_m_dataCannotBeEmpty: Method = Method(name="dataCannotBeEmpty", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
dg_Text.attributes={dg_Text_data, dg_Text_anchor}
dg_Text.methods={dg_Text_m_dataCannotBeEmpty}

# dg_Translate class attributes and methods
dg_Translate_deltaX: Property = Property(name="deltaX", type=StringType)
dg_Translate_deltaY: Property = Property(name="deltaY", type=StringType)
dg_Translate.attributes={dg_Translate_deltaY, dg_Translate_deltaX}

# dg_Use class attributes and methods
dg_Use_m_referencedElementHasId: Method = Method(name="referencedElementHasId", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
dg_Use.methods={dg_Use_m_referencedElementHasId}

# Relationships
clipPath2: BinaryAssociation = BinaryAssociation(
    name="clipPath2",
    ends={
        Property(name="dg_ClipPath", type=dg_GraphicalElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dg_GraphicalElement", type=dg_ClipPath, multiplicity=Multiplicity(0, 1))
    }
)
group3: BinaryAssociation = BinaryAssociation(
    name="group3",
    ends={
        Property(name="Group", type=dg_GraphicalElement, multiplicity=Multiplicity(1, 1)),
        Property(name="member", type=dg_Group, multiplicity=Multiplicity(0, 1))
    }
)
bounds0: BinaryAssociation = BinaryAssociation(
    name="bounds0",
    ends={
        Property(name="dg_Bounds", type=dg_Canvas, multiplicity=Multiplicity(1, 1)),
        Property(name="dg_Canvas", type=dg_Bounds, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
member1: BinaryAssociation = BinaryAssociation(
    name="member1",
    ends={
        Property(name="GraphicalElement", type=dg_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="group", type=dg_GraphicalElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
style4: BinaryAssociation = BinaryAssociation(
    name="style4",
    ends={
        Property(name="dg_Style", type=dg_GraphicalElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dg_GraphicalElement5", type=dg_Style, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transform6: BinaryAssociation = BinaryAssociation(
    name="transform6",
    ends={
        Property(name="dg_Transform", type=dg_GraphicalElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dg_GraphicalElement7", type=dg_Transform, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
point8: BinaryAssociation = BinaryAssociation(
    name="point8",
    ends={
        Property(name="dg_Point", type=dg_MoveTo, multiplicity=Multiplicity(1, 1)),
        Property(name="dg_MoveTo", type=dg_Point, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fill9: BinaryAssociation = BinaryAssociation(
    name="fill9",
    ends={
        Property(name="dg_Paint", type=dg_Style, multiplicity=Multiplicity(1, 1)),
        Property(name="dg_Style10", type=dg_Paint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stroke11: BinaryAssociation = BinaryAssociation(
    name="stroke11",
    ends={
        Property(name="dg_Paint13", type=dg_Style, multiplicity=Multiplicity(1, 1)),
        Property(name="dg_Style12", type=dg_Paint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
paintServer14: BinaryAssociation = BinaryAssociation(
    name="paintServer14",
    ends={
        Property(name="dg_PaintServer", type=dg_Paint, multiplicity=Multiplicity(1, 1)),
        Property(name="dg_Paint15", type=dg_PaintServer, multiplicity=Multiplicity(0, 1))
    }
)
center19: BinaryAssociation = BinaryAssociation(
    name="center19",
    ends={
        Property(name="dg_Point20", type=dg_Circle, multiplicity=Multiplicity(1, 1)),
        Property(name="dg_Circle", type=dg_Point, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
transform16: BinaryAssociation = BinaryAssociation(
    name="transform16",
    ends={
        Property(name="dg_Transform18", type=dg_PaintServer, multiplicity=Multiplicity(1, 1)),
        Property(name="dg_PaintServer17", type=dg_Transform, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
startControl21: BinaryAssociation = BinaryAssociation(
    name="startControl21",
    ends={
        Property(name="dg_Point22", type=dg_CubicCurveTo, multiplicity=Multiplicity(1, 1)),
        Property(name="dg_CubicCurveTo", type=dg_Point, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
endControl23: BinaryAssociation = BinaryAssociation(
    name="endControl23",
    ends={
        Property(name="dg_Point25", type=dg_CubicCurveTo, multiplicity=Multiplicity(1, 1)),
        Property(name="dg_CubicCurveTo24", type=dg_Point, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
point26: BinaryAssociation = BinaryAssociation(
    name="point26",
    ends={
        Property(name="dg_Point28", type=dg_CubicCurveTo, multiplicity=Multiplicity(1, 1)),
        Property(name="dg_CubicCurveTo27", type=dg_Point, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definition29: BinaryAssociation = BinaryAssociation(
    name="definition29",
    ends={
        Property(name="dg_Definition", type=dg_Definitions, multiplicity=Multiplicity(1, 1)),
        Property(name="dg_Definitions", type=dg_Definition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
styleSheet30: BinaryAssociation = BinaryAssociation(
    name="styleSheet30",
    ends={
        Property(name="dg_StyleSheet", type=dg_Definitions, multiplicity=Multiplicity(1, 1)),
        Property(name="dg_Definitions31", type=dg_StyleSheet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rule32: BinaryAssociation = BinaryAssociation(
    name="rule32",
    ends={
        Property(name="dg_StyleRule", type=dg_StyleSheet, multiplicity=Multiplicity(1, 1)),
        Property(name="dg_StyleSheet33", type=dg_StyleRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
selector34: BinaryAssociation = BinaryAssociation(
    name="selector34",
    ends={
        Property(name="dg_StyleSelector", type=dg_StyleRule, multiplicity=Multiplicity(1, 1)),
        Property(name="dg_StyleRule35", type=dg_StyleSelector, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
style36: BinaryAssociation = BinaryAssociation(
    name="style36",
    ends={
        Property(name="dg_Style38", type=dg_StyleRule, multiplicity=Multiplicity(1, 1)),
        Property(name="dg_StyleRule37", type=dg_Style, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
radii43: BinaryAssociation = BinaryAssociation(
    name="radii43",
    ends={
        Property(name="dg_Dimension44", type=dg_EllipticalArcTo, multiplicity=Multiplicity(1, 1)),
        Property(name="dg_EllipticalArcTo", type=dg_Dimension, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
center39: BinaryAssociation = BinaryAssociation(
    name="center39",
    ends={
        Property(name="dg_Point40", type=dg_Ellipse, multiplicity=Multiplicity(1, 1)),
        Property(name="dg_Ellipse", type=dg_Point, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
radii41: BinaryAssociation = BinaryAssociation(
    name="radii41",
    ends={
        Property(name="dg_Dimension", type=dg_Ellipse, multiplicity=Multiplicity(1, 1)),
        Property(name="dg_Ellipse42", type=dg_Dimension, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
stop53: BinaryAssociation = BinaryAssociation(
    name="stop53",
    ends={
        Property(name="dg_GradientStop", type=dg_Gradient, multiplicity=Multiplicity(1, 1)),
        Property(name="dg_Gradient", type=dg_GradientStop, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
point45: BinaryAssociation = BinaryAssociation(
    name="point45",
    ends={
        Property(name="dg_Point47", type=dg_EllipticalArcTo, multiplicity=Multiplicity(1, 1)),
        Property(name="dg_EllipticalArcTo46", type=dg_Point, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
control48: BinaryAssociation = BinaryAssociation(
    name="control48",
    ends={
        Property(name="dg_Point49", type=dg_QuadraticCurveTo, multiplicity=Multiplicity(1, 1)),
        Property(name="dg_QuadraticCurveTo", type=dg_Point, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
point50: BinaryAssociation = BinaryAssociation(
    name="point50",
    ends={
        Property(name="dg_Point52", type=dg_QuadraticCurveTo, multiplicity=Multiplicity(1, 1)),
        Property(name="dg_QuadraticCurveTo51", type=dg_Point, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bounds54: BinaryAssociation = BinaryAssociation(
    name="bounds54",
    ends={
        Property(name="dg_Bounds55", type=dg_Image, multiplicity=Multiplicity(1, 1)),
        Property(name="dg_Image", type=dg_Bounds, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
start56: BinaryAssociation = BinaryAssociation(
    name="start56",
    ends={
        Property(name="dg_Point57", type=dg_Line, multiplicity=Multiplicity(1, 1)),
        Property(name="dg_Line", type=dg_Point, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
end58: BinaryAssociation = BinaryAssociation(
    name="end58",
    ends={
        Property(name="dg_Point60", type=dg_Line, multiplicity=Multiplicity(1, 1)),
        Property(name="dg_Line59", type=dg_Point, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
endMarker61: BinaryAssociation = BinaryAssociation(
    name="endMarker61",
    ends={
        Property(name="dg_Marker", type=dg_MarkedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dg_MarkedElement", type=dg_Marker, multiplicity=Multiplicity(0, 1))
    }
)
midMarker62: BinaryAssociation = BinaryAssociation(
    name="midMarker62",
    ends={
        Property(name="dg_Marker64", type=dg_MarkedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dg_MarkedElement63", type=dg_Marker, multiplicity=Multiplicity(0, 1))
    }
)
startMarker65: BinaryAssociation = BinaryAssociation(
    name="startMarker65",
    ends={
        Property(name="dg_Marker67", type=dg_MarkedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dg_MarkedElement66", type=dg_Marker, multiplicity=Multiplicity(0, 1))
    }
)
size68: BinaryAssociation = BinaryAssociation(
    name="size68",
    ends={
        Property(name="dg_Dimension70", type=dg_Marker, multiplicity=Multiplicity(1, 1)),
        Property(name="dg_Marker69", type=dg_Dimension, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
reference71: BinaryAssociation = BinaryAssociation(
    name="reference71",
    ends={
        Property(name="dg_Point73", type=dg_Marker, multiplicity=Multiplicity(1, 1)),
        Property(name="dg_Marker72", type=dg_Point, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
start74: BinaryAssociation = BinaryAssociation(
    name="start74",
    ends={
        Property(name="dg_Point75", type=dg_LinearGradient, multiplicity=Multiplicity(1, 1)),
        Property(name="dg_LinearGradient", type=dg_Point, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
end76: BinaryAssociation = BinaryAssociation(
    name="end76",
    ends={
        Property(name="dg_Point78", type=dg_LinearGradient, multiplicity=Multiplicity(1, 1)),
        Property(name="dg_LinearGradient77", type=dg_Point, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
point79: BinaryAssociation = BinaryAssociation(
    name="point79",
    ends={
        Property(name="dg_Point80", type=dg_LineTo, multiplicity=Multiplicity(1, 1)),
        Property(name="dg_LineTo", type=dg_Point, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bounds82: BinaryAssociation = BinaryAssociation(
    name="bounds82",
    ends={
        Property(name="dg_Bounds83", type=dg_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="dg_Pattern", type=dg_Bounds, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tile84: BinaryAssociation = BinaryAssociation(
    name="tile84",
    ends={
        Property(name="dg_GraphicalElement86", type=dg_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="dg_Pattern85", type=dg_GraphicalElement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
command81: BinaryAssociation = BinaryAssociation(
    name="command81",
    ends={
        Property(name="dg_PathCommand", type=dg_Path, multiplicity=Multiplicity(1, 1)),
        Property(name="dg_Path", type=dg_PathCommand, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
point87: BinaryAssociation = BinaryAssociation(
    name="point87",
    ends={
        Property(name="dg_Point88", type=dg_Polygon, multiplicity=Multiplicity(1, 1)),
        Property(name="dg_Polygon", type=dg_Point, multiplicity=Multiplicity(3, 9999), is_composite=True)
    }
)
point89: BinaryAssociation = BinaryAssociation(
    name="point89",
    ends={
        Property(name="dg_Point90", type=dg_Polyline, multiplicity=Multiplicity(1, 1)),
        Property(name="dg_Polyline", type=dg_Point, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
center91: BinaryAssociation = BinaryAssociation(
    name="center91",
    ends={
        Property(name="dg_Point92", type=dg_RadialGradient, multiplicity=Multiplicity(1, 1)),
        Property(name="dg_RadialGradient", type=dg_Point, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
focus93: BinaryAssociation = BinaryAssociation(
    name="focus93",
    ends={
        Property(name="dg_Point95", type=dg_RadialGradient, multiplicity=Multiplicity(1, 1)),
        Property(name="dg_RadialGradient94", type=dg_Point, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
externalStyleSheet100: BinaryAssociation = BinaryAssociation(
    name="externalStyleSheet100",
    ends={
        Property(name="dg_StyleSheet102", type=dg_RootCanvas, multiplicity=Multiplicity(1, 1)),
        Property(name="dg_RootCanvas101", type=dg_StyleSheet, multiplicity=Multiplicity(0, 9999))
    }
)
bounds96: BinaryAssociation = BinaryAssociation(
    name="bounds96",
    ends={
        Property(name="dg_Bounds97", type=dg_Rectangle, multiplicity=Multiplicity(1, 1)),
        Property(name="dg_Rectangle", type=dg_Bounds, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definitions98: BinaryAssociation = BinaryAssociation(
    name="definitions98",
    ends={
        Property(name="dg_Definitions99", type=dg_RootCanvas, multiplicity=Multiplicity(1, 1)),
        Property(name="dg_RootCanvas", type=dg_Definitions, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
center103: BinaryAssociation = BinaryAssociation(
    name="center103",
    ends={
        Property(name="dg_Point104", type=dg_Rotate, multiplicity=Multiplicity(1, 1)),
        Property(name="dg_Rotate", type=dg_Point, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bounds105: BinaryAssociation = BinaryAssociation(
    name="bounds105",
    ends={
        Property(name="dg_Bounds106", type=dg_Text, multiplicity=Multiplicity(1, 1)),
        Property(name="dg_Text", type=dg_Bounds, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referencedElement109: BinaryAssociation = BinaryAssociation(
    name="referencedElement109",
    ends={
        Property(name="dg_GraphicalElement111", type=dg_Use, multiplicity=Multiplicity(1, 1)),
        Property(name="dg_Use110", type=dg_GraphicalElement, multiplicity=Multiplicity(1, 1))
    }
)
bounds107: BinaryAssociation = BinaryAssociation(
    name="bounds107",
    ends={
        Property(name="dg_Bounds108", type=dg_Use, multiplicity=Multiplicity(1, 1)),
        Property(name="dg_Use", type=dg_Bounds, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_dg_Canvas_Group = Generalization(general=Group, specific=dg_Canvas)
gen_dg_Group_GraphicalElement = Generalization(general=GraphicalElement, specific=dg_Group)
gen_dg_GraphicalElement_Definition = Generalization(general=Definition, specific=dg_GraphicalElement)
gen_dg_MoveTo_PathCommand = Generalization(general=PathCommand, specific=dg_MoveTo)
gen_dg_ClipPath_Group = Generalization(general=Group, specific=dg_ClipPath)
gen_dg_PaintServer_Definition = Generalization(general=Definition, specific=dg_PaintServer)
gen_dg_Circle_GraphicalElement = Generalization(general=GraphicalElement, specific=dg_Circle)
gen_dg_ClosePath_PathCommand = Generalization(general=PathCommand, specific=dg_ClosePath)
gen_dg_CubicCurveTo_PathCommand = Generalization(general=PathCommand, specific=dg_CubicCurveTo)
gen_dg_Ellipse_GraphicalElement = Generalization(general=GraphicalElement, specific=dg_Ellipse)
gen_dg_EllipticalArcTo_PathCommand = Generalization(general=PathCommand, specific=dg_EllipticalArcTo)
gen_dg_QuadraticCurveTo_PathCommand = Generalization(general=PathCommand, specific=dg_QuadraticCurveTo)
gen_dg_Gradient_PaintServer = Generalization(general=PaintServer, specific=dg_Gradient)
gen_dg_Image_GraphicalElement = Generalization(general=GraphicalElement, specific=dg_Image)
gen_dg_Line_MarkedElement = Generalization(general=MarkedElement, specific=dg_Line)
gen_dg_MarkedElement_GraphicalElement = Generalization(general=GraphicalElement, specific=dg_MarkedElement)
gen_dg_LinearGradient_Gradient = Generalization(general=Gradient, specific=dg_LinearGradient)
gen_dg_Marker_Group = Generalization(general=Group, specific=dg_Marker)
gen_dg_LineTo_PathCommand = Generalization(general=PathCommand, specific=dg_LineTo)
gen_dg_Matrix_Transform = Generalization(general=Transform, specific=dg_Matrix)
gen_dg_Path_MarkedElement = Generalization(general=MarkedElement, specific=dg_Path)
gen_dg_Pattern_PaintServer = Generalization(general=PaintServer, specific=dg_Pattern)
gen_dg_Polygon_MarkedElement = Generalization(general=MarkedElement, specific=dg_Polygon)
gen_dg_Polyline_MarkedElement = Generalization(general=MarkedElement, specific=dg_Polyline)
gen_dg_RadialGradient_Gradient = Generalization(general=Gradient, specific=dg_RadialGradient)
gen_dg_Rectangle_GraphicalElement = Generalization(general=GraphicalElement, specific=dg_Rectangle)
gen_dg_Rotate_Transform = Generalization(general=Transform, specific=dg_Rotate)
gen_dg_RootCanvas_Canvas = Generalization(general=Canvas, specific=dg_RootCanvas)
gen_dg_Skew_Transform = Generalization(general=Transform, specific=dg_Skew)
gen_dg_Scale_Transform = Generalization(general=Transform, specific=dg_Scale)
gen_dg_Text_GraphicalElement = Generalization(general=GraphicalElement, specific=dg_Text)
gen_dg_Translate_Transform = Generalization(general=Transform, specific=dg_Translate)
gen_dg_Use_GraphicalElement = Generalization(general=GraphicalElement, specific=dg_Use)

# Domain Model
domain_model = DomainModel(
    name="dg",
    types={dg_Canvas, Group, dg_ClipPath, dg_Bounds, dg_Group, GraphicalElement, dg_GraphicalElement, Definition, dg_MoveTo, PathCommand, dg_Style, dg_Transform, dg_Definition, dg_Point, dg_PathCommand, dg_Paint, dg_PaintServer, dg_Circle, dg_Definitions, dg_ClosePath, dg_CubicCurveTo, dg_StyleSheet, dg_StyleRule, dg_StyleSelector, dg_Ellipse, dg_Dimension, dg_EllipticalArcTo, dg_GradientStop, dg_QuadraticCurveTo, dg_Gradient, PaintServer, dg_Image, dg_Line, MarkedElement, dg_MarkedElement, dg_LinearGradient, Gradient, dg_Marker, dg_Path, dg_LineTo, dg_Matrix, Transform, dg_Pattern, dg_Polygon, dg_Polyline, dg_RadialGradient, dg_Rectangle, dg_Rotate, dg_RootCanvas, Canvas, dg_Skew, dg_Scale, dg_Text, dg_Translate, dg_Use, FontDecoration, ElementKind, TextAnchor},
    associations={clipPath2, group3, bounds0, member1, style4, transform6, point8, fill9, stroke11, paintServer14, center19, transform16, startControl21, endControl23, point26, definition29, styleSheet30, rule32, selector34, style36, radii43, center39, radii41, stop53, point45, control48, point50, bounds54, start56, end58, endMarker61, midMarker62, startMarker65, size68, reference71, start74, end76, point79, bounds82, tile84, command81, point87, point89, center91, focus93, externalStyleSheet100, bounds96, definitions98, center103, bounds105, referencedElement109, bounds107},
    generalizations={gen_dg_Canvas_Group, gen_dg_Group_GraphicalElement, gen_dg_GraphicalElement_Definition, gen_dg_MoveTo_PathCommand, gen_dg_ClipPath_Group, gen_dg_PaintServer_Definition, gen_dg_Circle_GraphicalElement, gen_dg_ClosePath_PathCommand, gen_dg_CubicCurveTo_PathCommand, gen_dg_Ellipse_GraphicalElement, gen_dg_EllipticalArcTo_PathCommand, gen_dg_QuadraticCurveTo_PathCommand, gen_dg_Gradient_PaintServer, gen_dg_Image_GraphicalElement, gen_dg_Line_MarkedElement, gen_dg_MarkedElement_GraphicalElement, gen_dg_LinearGradient_Gradient, gen_dg_Marker_Group, gen_dg_LineTo_PathCommand, gen_dg_Matrix_Transform, gen_dg_Path_MarkedElement, gen_dg_Pattern_PaintServer, gen_dg_Polygon_MarkedElement, gen_dg_Polyline_MarkedElement, gen_dg_RadialGradient_Gradient, gen_dg_Rectangle_GraphicalElement, gen_dg_Rotate_Transform, gen_dg_RootCanvas_Canvas, gen_dg_Skew_Transform, gen_dg_Scale_Transform, gen_dg_Text_GraphicalElement, gen_dg_Translate_Transform, gen_dg_Use_GraphicalElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)