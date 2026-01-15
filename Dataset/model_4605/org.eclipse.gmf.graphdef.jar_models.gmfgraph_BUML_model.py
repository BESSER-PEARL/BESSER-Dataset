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
ColorConstants: Enumeration = Enumeration(
    name="ColorConstants",
    literals={
            EnumerationLiteral(name="white"),
			EnumerationLiteral(name="black"),
			EnumerationLiteral(name="lightGray"),
			EnumerationLiteral(name="gray"),
			EnumerationLiteral(name="darkGray"),
			EnumerationLiteral(name="red"),
			EnumerationLiteral(name="orange"),
			EnumerationLiteral(name="yellow"),
			EnumerationLiteral(name="green"),
			EnumerationLiteral(name="lightGreen"),
			EnumerationLiteral(name="darkGreen"),
			EnumerationLiteral(name="cyan"),
			EnumerationLiteral(name="lightBlue"),
			EnumerationLiteral(name="blue"),
			EnumerationLiteral(name="darkBlue")
    }
)

FontStyle: Enumeration = Enumeration(
    name="FontStyle",
    literals={
            EnumerationLiteral(name="NORMAL"),
			EnumerationLiteral(name="BOLD"),
			EnumerationLiteral(name="ITALIC")
    }
)

Direction: Enumeration = Enumeration(
    name="Direction",
    literals={
            EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="NORTH"),
			EnumerationLiteral(name="SOUTH"),
			EnumerationLiteral(name="WEST"),
			EnumerationLiteral(name="EAST"),
			EnumerationLiteral(name="NORTH_EAST"),
			EnumerationLiteral(name="NORTH_WEST"),
			EnumerationLiteral(name="SOUTH_EAST"),
			EnumerationLiteral(name="SOUTH_WEST"),
			EnumerationLiteral(name="NORTH_SOUTH"),
			EnumerationLiteral(name="EAST_WEST"),
			EnumerationLiteral(name="NSEW")
    }
)

LineKind: Enumeration = Enumeration(
    name="LineKind",
    literals={
            EnumerationLiteral(name="LINE_SOLID"),
			EnumerationLiteral(name="LINE_DASH"),
			EnumerationLiteral(name="LINE_DOT"),
			EnumerationLiteral(name="LINE_DASHDOT"),
			EnumerationLiteral(name="LINE_DASHDOTDOT"),
			EnumerationLiteral(name="LINE_CUSTOM")
    }
)

Alignment: Enumeration = Enumeration(
    name="Alignment",
    literals={
            EnumerationLiteral(name="BEGINNING"),
			EnumerationLiteral(name="CENTER"),
			EnumerationLiteral(name="END"),
			EnumerationLiteral(name="FILL")
    }
)

SVGPropertyType: Enumeration = Enumeration(
    name="SVGPropertyType",
    literals={
            EnumerationLiteral(name="STRING"),
			EnumerationLiteral(name="COLOR"),
			EnumerationLiteral(name="FLOAT")
    }
)

# Classes
gmfgraph_Border = Class(name="gmfgraph::Border", is_abstract=True)
gmfgraph_Layout = Class(name="gmfgraph::Layout", is_abstract=True)
gmfgraph_Canvas = Class(name="gmfgraph::Canvas")
Identity = Class(name="Identity")
gmfgraph_FigureGallery = Class(name="gmfgraph::FigureGallery")
gmfgraph_Node = Class(name="gmfgraph::Node")
gmfgraph_Connection = Class(name="gmfgraph::Connection")
gmfgraph_Compartment = Class(name="gmfgraph::Compartment")
gmfgraph_DiagramLabel = Class(name="gmfgraph::DiagramLabel")
gmfgraph_RealFigure = Class(name="gmfgraph::RealFigure", is_abstract=True)
gmfgraph_FigureDescriptor = Class(name="gmfgraph::FigureDescriptor")
Node = Class(name="Node")
gmfgraph_GeneralFacet = Class(name="gmfgraph::GeneralFacet")
VisualFacet = Class(name="VisualFacet")
gmfgraph_Identity = Class(name="gmfgraph::Identity", is_abstract=True)
gmfgraph_DiagramElement = Class(name="gmfgraph::DiagramElement", is_abstract=True)
gmfgraph_VisualFacet = Class(name="gmfgraph::VisualFacet", is_abstract=True)
gmfgraph_AbstractNode = Class(name="gmfgraph::AbstractNode", is_abstract=True)
DiagramElement = Class(name="DiagramElement")
AbstractNode = Class(name="AbstractNode")
gmfgraph_ChildAccess = Class(name="gmfgraph::ChildAccess")
gmfgraph_Font = Class(name="gmfgraph::Font", is_abstract=True)
gmfgraph_Insets = Class(name="gmfgraph::Insets")
gmfgraph_AlignmentFacet = Class(name="gmfgraph::AlignmentFacet")
gmfgraph_GradientFacet = Class(name="gmfgraph::GradientFacet")
gmfgraph_LabelOffsetFacet = Class(name="gmfgraph::LabelOffsetFacet")
gmfgraph_DefaultSizeFacet = Class(name="gmfgraph::DefaultSizeFacet")
gmfgraph_Dimension = Class(name="gmfgraph::Dimension")
gmfgraph_Figure = Class(name="gmfgraph::Figure", is_abstract=True)
Layoutable = Class(name="Layoutable")
gmfgraph_Color = Class(name="gmfgraph::Color", is_abstract=True)
gmfgraph_ConnectionFigure = Class(name="gmfgraph::ConnectionFigure", is_abstract=True)
RealFigure = Class(name="RealFigure")
gmfgraph_DecorationFigure = Class(name="gmfgraph::DecorationFigure", is_abstract=True)
gmfgraph_Shape = Class(name="gmfgraph::Shape", is_abstract=True)
gmfgraph_Point = Class(name="gmfgraph::Point")
gmfgraph_AbstractFigure = Class(name="gmfgraph::AbstractFigure", is_abstract=True)
Figure = Class(name="Figure")
AbstractFigure = Class(name="AbstractFigure")
gmfgraph_FigureRef = Class(name="gmfgraph::FigureRef")
gmfgraph_ScalablePolygon = Class(name="gmfgraph::ScalablePolygon")
Polygon = Class(name="Polygon")
gmfgraph_PolylineConnection = Class(name="gmfgraph::PolylineConnection")
ConnectionFigure = Class(name="ConnectionFigure")
gmfgraph_Label = Class(name="gmfgraph::Label")
gmfgraph_LabeledContainer = Class(name="gmfgraph::LabeledContainer")
gmfgraph_Rectangle = Class(name="gmfgraph::Rectangle")
Shape = Class(name="Shape")
gmfgraph_RoundedRectangle = Class(name="gmfgraph::RoundedRectangle")
gmfgraph_Ellipse = Class(name="gmfgraph::Ellipse")
gmfgraph_Polyline = Class(name="gmfgraph::Polyline")
gmfgraph_Polygon = Class(name="gmfgraph::Polygon")
Polyline = Class(name="Polyline")
gmfgraph_RGBColor = Class(name="gmfgraph::RGBColor")
Color = Class(name="Color")
gmfgraph_ConstantColor = Class(name="gmfgraph::ConstantColor")
gmfgraph_PolylineDecoration = Class(name="gmfgraph::PolylineDecoration")
DecorationFigure = Class(name="DecorationFigure")
gmfgraph_PolygonDecoration = Class(name="gmfgraph::PolygonDecoration")
gmfgraph_CustomClass = Class(name="gmfgraph::CustomClass", is_abstract=True)
gmfgraph_CustomAttribute = Class(name="gmfgraph::CustomAttribute")
gmfgraph_FigureAccessor = Class(name="gmfgraph::FigureAccessor")
gmfgraph_CustomFigure = Class(name="gmfgraph::CustomFigure")
CustomClass = Class(name="CustomClass")
gmfgraph_CustomDecoration = Class(name="gmfgraph::CustomDecoration")
CustomFigure = Class(name="CustomFigure")
gmfgraph_CustomConnection = Class(name="gmfgraph::CustomConnection")
gmfgraph_LineBorder = Class(name="gmfgraph::LineBorder")
gmfgraph_MarginBorder = Class(name="gmfgraph::MarginBorder")
gmfgraph_BasicFont = Class(name="gmfgraph::BasicFont")
Font = Class(name="Font")
gmfgraph_BorderRef = Class(name="gmfgraph::BorderRef")
Border = Class(name="Border")
gmfgraph_BorderLayoutData = Class(name="gmfgraph::BorderLayoutData")
gmfgraph_CompoundBorder = Class(name="gmfgraph::CompoundBorder")
gmfgraph_CustomBorder = Class(name="gmfgraph::CustomBorder")
gmfgraph_LayoutData = Class(name="gmfgraph::LayoutData", is_abstract=True)
gmfgraph_Layoutable = Class(name="gmfgraph::Layoutable", is_abstract=True)
gmfgraph_CustomLayoutData = Class(name="gmfgraph::CustomLayoutData")
LayoutData = Class(name="LayoutData")
gmfgraph_GridLayoutData = Class(name="gmfgraph::GridLayoutData")
gmfgraph_FlowLayout = Class(name="gmfgraph::FlowLayout")
gmfgraph_LayoutRef = Class(name="gmfgraph::LayoutRef")
Layout = Class(name="Layout")
gmfgraph_CustomLayout = Class(name="gmfgraph::CustomLayout")
gmfgraph_GridLayout = Class(name="gmfgraph::GridLayout")
gmfgraph_BorderLayout = Class(name="gmfgraph::BorderLayout")
gmfgraph_XYLayout = Class(name="gmfgraph::XYLayout")
gmfgraph_XYLayoutData = Class(name="gmfgraph::XYLayoutData")
gmfgraph_StackLayout = Class(name="gmfgraph::StackLayout")
gmfgraph_SVGFigure = Class(name="gmfgraph::SVGFigure")
gmfgraph_SVGProperty = Class(name="gmfgraph::SVGProperty")
gmfgraph_Rectangle2D = Class(name="gmfgraph::Rectangle2D")

# gmfgraph_Border class attributes and methods

# gmfgraph_Layout class attributes and methods

# gmfgraph_Canvas class attributes and methods

# Identity class attributes and methods

# gmfgraph_FigureGallery class attributes and methods
gmfgraph_FigureGallery_implementationBundle: Property = Property(name="implementationBundle", type=StringType)
gmfgraph_FigureGallery.attributes={gmfgraph_FigureGallery_implementationBundle}

# gmfgraph_Node class attributes and methods
gmfgraph_Node_resizeConstraint: Property = Property(name="resizeConstraint", type=StringType)
gmfgraph_Node_affixedParentSide: Property = Property(name="affixedParentSide", type=StringType)
gmfgraph_Node.attributes={gmfgraph_Node_resizeConstraint, gmfgraph_Node_affixedParentSide}

# gmfgraph_Connection class attributes and methods

# gmfgraph_Compartment class attributes and methods
gmfgraph_Compartment_collapsible: Property = Property(name="collapsible", type=BooleanType)
gmfgraph_Compartment_needsTitle: Property = Property(name="needsTitle", type=BooleanType)
gmfgraph_Compartment.attributes={gmfgraph_Compartment_needsTitle, gmfgraph_Compartment_collapsible}

# gmfgraph_DiagramLabel class attributes and methods
gmfgraph_DiagramLabel_elementIcon: Property = Property(name="elementIcon", type=BooleanType)
gmfgraph_DiagramLabel_external: Property = Property(name="external", type=BooleanType)
gmfgraph_DiagramLabel.attributes={gmfgraph_DiagramLabel_elementIcon, gmfgraph_DiagramLabel_external}

# gmfgraph_RealFigure class attributes and methods
gmfgraph_RealFigure_name: Property = Property(name="name", type=StringType)
gmfgraph_RealFigure.attributes={gmfgraph_RealFigure_name}

# gmfgraph_FigureDescriptor class attributes and methods

# Node class attributes and methods

# gmfgraph_GeneralFacet class attributes and methods
gmfgraph_GeneralFacet_identifier: Property = Property(name="identifier", type=StringType)
gmfgraph_GeneralFacet_data: Property = Property(name="data", type=StringType)
gmfgraph_GeneralFacet.attributes={gmfgraph_GeneralFacet_identifier, gmfgraph_GeneralFacet_data}

# VisualFacet class attributes and methods

# gmfgraph_Identity class attributes and methods
gmfgraph_Identity_name: Property = Property(name="name", type=StringType)
gmfgraph_Identity.attributes={gmfgraph_Identity_name}

# gmfgraph_DiagramElement class attributes and methods

# gmfgraph_VisualFacet class attributes and methods

# gmfgraph_AbstractNode class attributes and methods

# DiagramElement class attributes and methods

# AbstractNode class attributes and methods

# gmfgraph_ChildAccess class attributes and methods
gmfgraph_ChildAccess_accessor: Property = Property(name="accessor", type=StringType)
gmfgraph_ChildAccess.attributes={gmfgraph_ChildAccess_accessor}

# gmfgraph_Font class attributes and methods

# gmfgraph_Insets class attributes and methods
gmfgraph_Insets_top: Property = Property(name="top", type=IntegerType)
gmfgraph_Insets_left: Property = Property(name="left", type=IntegerType)
gmfgraph_Insets_bottom: Property = Property(name="bottom", type=IntegerType)
gmfgraph_Insets_right: Property = Property(name="right", type=IntegerType)
gmfgraph_Insets.attributes={gmfgraph_Insets_left, gmfgraph_Insets_right, gmfgraph_Insets_top, gmfgraph_Insets_bottom}

# gmfgraph_AlignmentFacet class attributes and methods
gmfgraph_AlignmentFacet_alignment: Property = Property(name="alignment", type=StringType)
gmfgraph_AlignmentFacet.attributes={gmfgraph_AlignmentFacet_alignment}

# gmfgraph_GradientFacet class attributes and methods
gmfgraph_GradientFacet_direction: Property = Property(name="direction", type=StringType)
gmfgraph_GradientFacet.attributes={gmfgraph_GradientFacet_direction}

# gmfgraph_LabelOffsetFacet class attributes and methods
gmfgraph_LabelOffsetFacet_x: Property = Property(name="x", type=IntegerType)
gmfgraph_LabelOffsetFacet_y: Property = Property(name="y", type=IntegerType)
gmfgraph_LabelOffsetFacet.attributes={gmfgraph_LabelOffsetFacet_y, gmfgraph_LabelOffsetFacet_x}

# gmfgraph_DefaultSizeFacet class attributes and methods

# gmfgraph_Dimension class attributes and methods
gmfgraph_Dimension_dx: Property = Property(name="dx", type=IntegerType)
gmfgraph_Dimension_dy: Property = Property(name="dy", type=IntegerType)
gmfgraph_Dimension.attributes={gmfgraph_Dimension_dy, gmfgraph_Dimension_dx}

# gmfgraph_Figure class attributes and methods

# Layoutable class attributes and methods

# gmfgraph_Color class attributes and methods

# gmfgraph_ConnectionFigure class attributes and methods

# RealFigure class attributes and methods

# gmfgraph_DecorationFigure class attributes and methods

# gmfgraph_Shape class attributes and methods
gmfgraph_Shape_outline: Property = Property(name="outline", type=BooleanType)
gmfgraph_Shape_fill: Property = Property(name="fill", type=BooleanType)
gmfgraph_Shape_lineWidth: Property = Property(name="lineWidth", type=IntegerType)
gmfgraph_Shape_lineKind: Property = Property(name="lineKind", type=StringType)
gmfgraph_Shape_xorFill: Property = Property(name="xorFill", type=BooleanType)
gmfgraph_Shape_xorOutline: Property = Property(name="xorOutline", type=BooleanType)
gmfgraph_Shape.attributes={gmfgraph_Shape_outline, gmfgraph_Shape_lineWidth, gmfgraph_Shape_xorFill, gmfgraph_Shape_lineKind, gmfgraph_Shape_fill, gmfgraph_Shape_xorOutline}

# gmfgraph_Point class attributes and methods
gmfgraph_Point_x: Property = Property(name="x", type=IntegerType)
gmfgraph_Point_y: Property = Property(name="y", type=IntegerType)
gmfgraph_Point.attributes={gmfgraph_Point_x, gmfgraph_Point_y}

# gmfgraph_AbstractFigure class attributes and methods

# Figure class attributes and methods

# AbstractFigure class attributes and methods

# gmfgraph_FigureRef class attributes and methods

# gmfgraph_ScalablePolygon class attributes and methods

# Polygon class attributes and methods

# gmfgraph_PolylineConnection class attributes and methods

# ConnectionFigure class attributes and methods

# gmfgraph_Label class attributes and methods
gmfgraph_Label_text: Property = Property(name="text", type=StringType)
gmfgraph_Label.attributes={gmfgraph_Label_text}

# gmfgraph_LabeledContainer class attributes and methods

# gmfgraph_Rectangle class attributes and methods

# Shape class attributes and methods

# gmfgraph_RoundedRectangle class attributes and methods
gmfgraph_RoundedRectangle_cornerWidth: Property = Property(name="cornerWidth", type=IntegerType)
gmfgraph_RoundedRectangle_cornerHeight: Property = Property(name="cornerHeight", type=IntegerType)
gmfgraph_RoundedRectangle.attributes={gmfgraph_RoundedRectangle_cornerHeight, gmfgraph_RoundedRectangle_cornerWidth}

# gmfgraph_Ellipse class attributes and methods

# gmfgraph_Polyline class attributes and methods

# gmfgraph_Polygon class attributes and methods

# Polyline class attributes and methods

# gmfgraph_RGBColor class attributes and methods
gmfgraph_RGBColor_red: Property = Property(name="red", type=IntegerType)
gmfgraph_RGBColor_green: Property = Property(name="green", type=IntegerType)
gmfgraph_RGBColor_blue: Property = Property(name="blue", type=IntegerType)
gmfgraph_RGBColor.attributes={gmfgraph_RGBColor_blue, gmfgraph_RGBColor_green, gmfgraph_RGBColor_red}

# Color class attributes and methods

# gmfgraph_ConstantColor class attributes and methods
gmfgraph_ConstantColor_value: Property = Property(name="value", type=StringType)
gmfgraph_ConstantColor.attributes={gmfgraph_ConstantColor_value}

# gmfgraph_PolylineDecoration class attributes and methods

# DecorationFigure class attributes and methods

# gmfgraph_PolygonDecoration class attributes and methods

# gmfgraph_CustomClass class attributes and methods
gmfgraph_CustomClass_qualifiedClassName: Property = Property(name="qualifiedClassName", type=StringType)
gmfgraph_CustomClass.attributes={gmfgraph_CustomClass_qualifiedClassName}

# gmfgraph_CustomAttribute class attributes and methods
gmfgraph_CustomAttribute_name: Property = Property(name="name", type=StringType)
gmfgraph_CustomAttribute_value: Property = Property(name="value", type=StringType)
gmfgraph_CustomAttribute_directAccess: Property = Property(name="directAccess", type=BooleanType)
gmfgraph_CustomAttribute_multiStatementValue: Property = Property(name="multiStatementValue", type=BooleanType)
gmfgraph_CustomAttribute.attributes={gmfgraph_CustomAttribute_value, gmfgraph_CustomAttribute_multiStatementValue, gmfgraph_CustomAttribute_name, gmfgraph_CustomAttribute_directAccess}

# gmfgraph_FigureAccessor class attributes and methods
gmfgraph_FigureAccessor_accessor: Property = Property(name="accessor", type=StringType)
gmfgraph_FigureAccessor.attributes={gmfgraph_FigureAccessor_accessor}

# gmfgraph_CustomFigure class attributes and methods

# CustomClass class attributes and methods

# gmfgraph_CustomDecoration class attributes and methods

# CustomFigure class attributes and methods

# gmfgraph_CustomConnection class attributes and methods

# gmfgraph_LineBorder class attributes and methods
gmfgraph_LineBorder_width: Property = Property(name="width", type=IntegerType)
gmfgraph_LineBorder.attributes={gmfgraph_LineBorder_width}

# gmfgraph_MarginBorder class attributes and methods

# gmfgraph_BasicFont class attributes and methods
gmfgraph_BasicFont_faceName: Property = Property(name="faceName", type=StringType)
gmfgraph_BasicFont_height: Property = Property(name="height", type=IntegerType)
gmfgraph_BasicFont_style: Property = Property(name="style", type=StringType)
gmfgraph_BasicFont.attributes={gmfgraph_BasicFont_faceName, gmfgraph_BasicFont_height, gmfgraph_BasicFont_style}

# Font class attributes and methods

# gmfgraph_BorderRef class attributes and methods

# Border class attributes and methods

# gmfgraph_BorderLayoutData class attributes and methods
gmfgraph_BorderLayoutData_alignment: Property = Property(name="alignment", type=StringType)
gmfgraph_BorderLayoutData_vertical: Property = Property(name="vertical", type=BooleanType)
gmfgraph_BorderLayoutData.attributes={gmfgraph_BorderLayoutData_vertical, gmfgraph_BorderLayoutData_alignment}

# gmfgraph_CompoundBorder class attributes and methods

# gmfgraph_CustomBorder class attributes and methods

# gmfgraph_LayoutData class attributes and methods

# gmfgraph_Layoutable class attributes and methods

# gmfgraph_CustomLayoutData class attributes and methods

# LayoutData class attributes and methods

# gmfgraph_GridLayoutData class attributes and methods
gmfgraph_GridLayoutData_grabExcessVerticalSpace: Property = Property(name="grabExcessVerticalSpace", type=BooleanType)
gmfgraph_GridLayoutData_verticalAlignment: Property = Property(name="verticalAlignment", type=StringType)
gmfgraph_GridLayoutData_horizontalAlignment: Property = Property(name="horizontalAlignment", type=StringType)
gmfgraph_GridLayoutData_verticalSpan: Property = Property(name="verticalSpan", type=IntegerType)
gmfgraph_GridLayoutData_horizontalSpan: Property = Property(name="horizontalSpan", type=IntegerType)
gmfgraph_GridLayoutData_horizontalIndent: Property = Property(name="horizontalIndent", type=IntegerType)
gmfgraph_GridLayoutData_grabExcessHorizontalSpace: Property = Property(name="grabExcessHorizontalSpace", type=BooleanType)
gmfgraph_GridLayoutData.attributes={gmfgraph_GridLayoutData_horizontalAlignment, gmfgraph_GridLayoutData_grabExcessHorizontalSpace, gmfgraph_GridLayoutData_horizontalSpan, gmfgraph_GridLayoutData_horizontalIndent, gmfgraph_GridLayoutData_verticalSpan, gmfgraph_GridLayoutData_verticalAlignment, gmfgraph_GridLayoutData_grabExcessVerticalSpace}

# gmfgraph_FlowLayout class attributes and methods
gmfgraph_FlowLayout_vertical: Property = Property(name="vertical", type=BooleanType)
gmfgraph_FlowLayout_matchMinorSize: Property = Property(name="matchMinorSize", type=BooleanType)
gmfgraph_FlowLayout_forceSingleLine: Property = Property(name="forceSingleLine", type=BooleanType)
gmfgraph_FlowLayout_majorAlignment: Property = Property(name="majorAlignment", type=StringType)
gmfgraph_FlowLayout_minorAlignment: Property = Property(name="minorAlignment", type=StringType)
gmfgraph_FlowLayout_majorSpacing: Property = Property(name="majorSpacing", type=IntegerType)
gmfgraph_FlowLayout_minorSpacing: Property = Property(name="minorSpacing", type=IntegerType)
gmfgraph_FlowLayout.attributes={gmfgraph_FlowLayout_minorAlignment, gmfgraph_FlowLayout_majorAlignment, gmfgraph_FlowLayout_majorSpacing, gmfgraph_FlowLayout_forceSingleLine, gmfgraph_FlowLayout_vertical, gmfgraph_FlowLayout_minorSpacing, gmfgraph_FlowLayout_matchMinorSize}

# gmfgraph_LayoutRef class attributes and methods

# Layout class attributes and methods

# gmfgraph_CustomLayout class attributes and methods

# gmfgraph_GridLayout class attributes and methods
gmfgraph_GridLayout_numColumns: Property = Property(name="numColumns", type=IntegerType)
gmfgraph_GridLayout_equalWidth: Property = Property(name="equalWidth", type=BooleanType)
gmfgraph_GridLayout.attributes={gmfgraph_GridLayout_numColumns, gmfgraph_GridLayout_equalWidth}

# gmfgraph_BorderLayout class attributes and methods

# gmfgraph_XYLayout class attributes and methods

# gmfgraph_XYLayoutData class attributes and methods

# gmfgraph_StackLayout class attributes and methods

# gmfgraph_SVGFigure class attributes and methods
gmfgraph_SVGFigure_documentURI: Property = Property(name="documentURI", type=StringType)
gmfgraph_SVGFigure_noCanvasWidth: Property = Property(name="noCanvasWidth", type=BooleanType)
gmfgraph_SVGFigure_noCanvasHeight: Property = Property(name="noCanvasHeight", type=BooleanType)
gmfgraph_SVGFigure.attributes={gmfgraph_SVGFigure_noCanvasHeight, gmfgraph_SVGFigure_documentURI, gmfgraph_SVGFigure_noCanvasWidth}

# gmfgraph_SVGProperty class attributes and methods
gmfgraph_SVGProperty_query: Property = Property(name="query", type=StringType)
gmfgraph_SVGProperty_attribute: Property = Property(name="attribute", type=StringType)
gmfgraph_SVGProperty_type: Property = Property(name="type", type=StringType)
gmfgraph_SVGProperty_getter: Property = Property(name="getter", type=StringType)
gmfgraph_SVGProperty_setter: Property = Property(name="setter", type=StringType)
gmfgraph_SVGProperty_callSuper: Property = Property(name="callSuper", type=BooleanType)
gmfgraph_SVGProperty.attributes={gmfgraph_SVGProperty_query, gmfgraph_SVGProperty_setter, gmfgraph_SVGProperty_getter, gmfgraph_SVGProperty_type, gmfgraph_SVGProperty_callSuper, gmfgraph_SVGProperty_attribute}

# gmfgraph_Rectangle2D class attributes and methods
gmfgraph_Rectangle2D_height: Property = Property(name="height", type=FloatType)
gmfgraph_Rectangle2D_x: Property = Property(name="x", type=FloatType)
gmfgraph_Rectangle2D_y: Property = Property(name="y", type=FloatType)
gmfgraph_Rectangle2D_width: Property = Property(name="width", type=FloatType)
gmfgraph_Rectangle2D.attributes={gmfgraph_Rectangle2D_height, gmfgraph_Rectangle2D_y, gmfgraph_Rectangle2D_x, gmfgraph_Rectangle2D_width}

# Relationships
descriptors11: BinaryAssociation = BinaryAssociation(
    name="descriptors11",
    ends={
        Property(name="gmfgraph_FigureGallery12", type=gmfgraph_FigureDescriptor, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="gmfgraph_FigureDescriptor", type=gmfgraph_FigureGallery, multiplicity=Multiplicity(1, 1))
    }
)
borders13: BinaryAssociation = BinaryAssociation(
    name="borders13",
    ends={
        Property(name="gmfgraph_Border", type=gmfgraph_FigureGallery, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_FigureGallery14", type=gmfgraph_Border, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
layouts15: BinaryAssociation = BinaryAssociation(
    name="layouts15",
    ends={
        Property(name="gmfgraph_Layout", type=gmfgraph_FigureGallery, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_FigureGallery16", type=gmfgraph_Layout, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
figures0: BinaryAssociation = BinaryAssociation(
    name="figures0",
    ends={
        Property(name="gmfgraph_FigureGallery", type=gmfgraph_Canvas, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_Canvas", type=gmfgraph_FigureGallery, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodes1: BinaryAssociation = BinaryAssociation(
    name="nodes1",
    ends={
        Property(name="gmfgraph_Node", type=gmfgraph_Canvas, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_Canvas2", type=gmfgraph_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connections3: BinaryAssociation = BinaryAssociation(
    name="connections3",
    ends={
        Property(name="gmfgraph_Connection", type=gmfgraph_Canvas, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_Canvas4", type=gmfgraph_Connection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
compartments5: BinaryAssociation = BinaryAssociation(
    name="compartments5",
    ends={
        Property(name="gmfgraph_Compartment", type=gmfgraph_Canvas, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_Canvas6", type=gmfgraph_Compartment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
labels7: BinaryAssociation = BinaryAssociation(
    name="labels7",
    ends={
        Property(name="gmfgraph_DiagramLabel", type=gmfgraph_Canvas, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_Canvas8", type=gmfgraph_DiagramLabel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
figures9: BinaryAssociation = BinaryAssociation(
    name="figures9",
    ends={
        Property(name="gmfgraph_RealFigure", type=gmfgraph_FigureGallery, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_FigureGallery10", type=gmfgraph_RealFigure, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
accessor26: BinaryAssociation = BinaryAssociation(
    name="accessor26",
    ends={
        Property(name="gmfgraph_ChildAccess28", type=gmfgraph_DiagramLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_DiagramLabel27", type=gmfgraph_ChildAccess, multiplicity=Multiplicity(0, 1))
    }
)
container29: BinaryAssociation = BinaryAssociation(
    name="container29",
    ends={
        Property(name="gmfgraph_ChildAccess31", type=gmfgraph_DiagramLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_DiagramLabel30", type=gmfgraph_ChildAccess, multiplicity=Multiplicity(0, 1))
    }
)
figure17: BinaryAssociation = BinaryAssociation(
    name="figure17",
    ends={
        Property(name="gmfgraph_FigureDescriptor18", type=gmfgraph_DiagramElement, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_DiagramElement", type=gmfgraph_FigureDescriptor, multiplicity=Multiplicity(1, 1))
    }
)
facets19: BinaryAssociation = BinaryAssociation(
    name="facets19",
    ends={
        Property(name="gmfgraph_VisualFacet", type=gmfgraph_DiagramElement, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_DiagramElement20", type=gmfgraph_VisualFacet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contentPane21: BinaryAssociation = BinaryAssociation(
    name="contentPane21",
    ends={
        Property(name="gmfgraph_ChildAccess", type=gmfgraph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_Node22", type=gmfgraph_ChildAccess, multiplicity=Multiplicity(0, 1))
    }
)
accessor23: BinaryAssociation = BinaryAssociation(
    name="accessor23",
    ends={
        Property(name="gmfgraph_ChildAccess25", type=gmfgraph_Compartment, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_Compartment24", type=gmfgraph_ChildAccess, multiplicity=Multiplicity(0, 1))
    }
)
minimumSize43: BinaryAssociation = BinaryAssociation(
    name="minimumSize43",
    ends={
        Property(name="gmfgraph_Dimension45", type=gmfgraph_Figure, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_Figure44", type=gmfgraph_Dimension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
preferredSize46: BinaryAssociation = BinaryAssociation(
    name="preferredSize46",
    ends={
        Property(name="gmfgraph_Dimension48", type=gmfgraph_Figure, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_Figure47", type=gmfgraph_Dimension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
font49: BinaryAssociation = BinaryAssociation(
    name="font49",
    ends={
        Property(name="gmfgraph_Font", type=gmfgraph_Figure, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_Figure50", type=gmfgraph_Font, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
insets51: BinaryAssociation = BinaryAssociation(
    name="insets51",
    ends={
        Property(name="gmfgraph_Insets", type=gmfgraph_Figure, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_Figure52", type=gmfgraph_Insets, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultSize32: BinaryAssociation = BinaryAssociation(
    name="defaultSize32",
    ends={
        Property(name="gmfgraph_Dimension", type=gmfgraph_DefaultSizeFacet, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_DefaultSizeFacet", type=gmfgraph_Dimension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
descriptor33: BinaryAssociation = BinaryAssociation(
    name="descriptor33",
    ends={
        Property(name="gmfgraph_FigureDescriptor34", type=gmfgraph_Figure, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_Figure", type=gmfgraph_FigureDescriptor, multiplicity=Multiplicity(0, 1))
    }
)
foregroundColor35: BinaryAssociation = BinaryAssociation(
    name="foregroundColor35",
    ends={
        Property(name="gmfgraph_Color", type=gmfgraph_Figure, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_Figure36", type=gmfgraph_Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
backgroundColor37: BinaryAssociation = BinaryAssociation(
    name="backgroundColor37",
    ends={
        Property(name="gmfgraph_Color39", type=gmfgraph_Figure, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_Figure38", type=gmfgraph_Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
maximumSize40: BinaryAssociation = BinaryAssociation(
    name="maximumSize40",
    ends={
        Property(name="gmfgraph_Dimension42", type=gmfgraph_Figure, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_Figure41", type=gmfgraph_Dimension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
figure72: BinaryAssociation = BinaryAssociation(
    name="figure72",
    ends={
        Property(name="gmfgraph_RealFigure73", type=gmfgraph_FigureRef, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_FigureRef", type=gmfgraph_RealFigure, multiplicity=Multiplicity(1, 1))
    }
)
border53: BinaryAssociation = BinaryAssociation(
    name="border53",
    ends={
        Property(name="gmfgraph_Border55", type=gmfgraph_Figure, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_Figure54", type=gmfgraph_Border, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
location56: BinaryAssociation = BinaryAssociation(
    name="location56",
    ends={
        Property(name="gmfgraph_Point", type=gmfgraph_Figure, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_Figure57", type=gmfgraph_Point, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
size58: BinaryAssociation = BinaryAssociation(
    name="size58",
    ends={
        Property(name="gmfgraph_Point60", type=gmfgraph_Figure, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_Figure59", type=gmfgraph_Point, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actualFigure61: BinaryAssociation = BinaryAssociation(
    name="actualFigure61",
    ends={
        Property(name="gmfgraph_Figure63", type=gmfgraph_FigureDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_FigureDescriptor62", type=gmfgraph_Figure, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
accessors64: BinaryAssociation = BinaryAssociation(
    name="accessors64",
    ends={
        Property(name="ChildAccess", type=gmfgraph_FigureDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=gmfgraph_ChildAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner65: BinaryAssociation = BinaryAssociation(
    name="owner65",
    ends={
        Property(name="FigureDescriptor", type=gmfgraph_ChildAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="accessors", type=gmfgraph_FigureDescriptor, multiplicity=Multiplicity(1, 1))
    }
)
figure66: BinaryAssociation = BinaryAssociation(
    name="figure66",
    ends={
        Property(name="gmfgraph_Figure68", type=gmfgraph_ChildAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_ChildAccess67", type=gmfgraph_Figure, multiplicity=Multiplicity(1, 1))
    }
)
children69: BinaryAssociation = BinaryAssociation(
    name="children69",
    ends={
        Property(name="gmfgraph_Figure71", type=gmfgraph_RealFigure, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_RealFigure70", type=gmfgraph_Figure, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sourceDecoration78: BinaryAssociation = BinaryAssociation(
    name="sourceDecoration78",
    ends={
        Property(name="gmfgraph_DecorationFigure", type=gmfgraph_PolylineConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_PolylineConnection", type=gmfgraph_DecorationFigure, multiplicity=Multiplicity(0, 1))
    }
)
targetDecoration79: BinaryAssociation = BinaryAssociation(
    name="targetDecoration79",
    ends={
        Property(name="gmfgraph_DecorationFigure81", type=gmfgraph_PolylineConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_PolylineConnection80", type=gmfgraph_DecorationFigure, multiplicity=Multiplicity(0, 1))
    }
)
resolvedChildren74: BinaryAssociation = BinaryAssociation(
    name="resolvedChildren74",
    ends={
        Property(name="gmfgraph_Figure75", type=gmfgraph_Shape, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_Shape", type=gmfgraph_Figure, multiplicity=Multiplicity(0, 9999))
    }
)
template76: BinaryAssociation = BinaryAssociation(
    name="template76",
    ends={
        Property(name="gmfgraph_Point77", type=gmfgraph_Polyline, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_Polyline", type=gmfgraph_Point, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes82: BinaryAssociation = BinaryAssociation(
    name="attributes82",
    ends={
        Property(name="gmfgraph_CustomAttribute", type=gmfgraph_CustomClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_CustomClass", type=gmfgraph_CustomAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typedFigure83: BinaryAssociation = BinaryAssociation(
    name="typedFigure83",
    ends={
        Property(name="gmfgraph_RealFigure84", type=gmfgraph_FigureAccessor, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_FigureAccessor", type=gmfgraph_RealFigure, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
customChildren85: BinaryAssociation = BinaryAssociation(
    name="customChildren85",
    ends={
        Property(name="gmfgraph_FigureAccessor86", type=gmfgraph_CustomFigure, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_CustomFigure", type=gmfgraph_FigureAccessor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actual87: BinaryAssociation = BinaryAssociation(
    name="actual87",
    ends={
        Property(name="gmfgraph_Border88", type=gmfgraph_BorderRef, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_BorderRef", type=gmfgraph_Border, multiplicity=Multiplicity(1, 1))
    }
)
color89: BinaryAssociation = BinaryAssociation(
    name="color89",
    ends={
        Property(name="gmfgraph_Color90", type=gmfgraph_LineBorder, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_LineBorder", type=gmfgraph_Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sizeHint99: BinaryAssociation = BinaryAssociation(
    name="sizeHint99",
    ends={
        Property(name="gmfgraph_Dimension100", type=gmfgraph_GridLayoutData, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_GridLayoutData", type=gmfgraph_Dimension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
insets91: BinaryAssociation = BinaryAssociation(
    name="insets91",
    ends={
        Property(name="gmfgraph_Insets92", type=gmfgraph_MarginBorder, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_MarginBorder", type=gmfgraph_Insets, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
outer93: BinaryAssociation = BinaryAssociation(
    name="outer93",
    ends={
        Property(name="gmfgraph_Border94", type=gmfgraph_CompoundBorder, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_CompoundBorder", type=gmfgraph_Border, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inner95: BinaryAssociation = BinaryAssociation(
    name="inner95",
    ends={
        Property(name="gmfgraph_Border97", type=gmfgraph_CompoundBorder, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_CompoundBorder96", type=gmfgraph_Border, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owner98: BinaryAssociation = BinaryAssociation(
    name="owner98",
    ends={
        Property(name="Layoutable", type=gmfgraph_LayoutData, multiplicity=Multiplicity(1, 1)),
        Property(name="layoutData", type=gmfgraph_Layoutable, multiplicity=Multiplicity(1, 1))
    }
)
spacing112: BinaryAssociation = BinaryAssociation(
    name="spacing112",
    ends={
        Property(name="gmfgraph_Dimension113", type=gmfgraph_BorderLayout, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_BorderLayout", type=gmfgraph_Dimension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
layoutData101: BinaryAssociation = BinaryAssociation(
    name="layoutData101",
    ends={
        Property(name="LayoutData", type=gmfgraph_Layoutable, multiplicity=Multiplicity(1, 1)),
        Property(name="owner102", type=gmfgraph_LayoutData, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
layout103: BinaryAssociation = BinaryAssociation(
    name="layout103",
    ends={
        Property(name="gmfgraph_Layout104", type=gmfgraph_Layoutable, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_Layoutable", type=gmfgraph_Layout, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actual105: BinaryAssociation = BinaryAssociation(
    name="actual105",
    ends={
        Property(name="gmfgraph_Layout106", type=gmfgraph_LayoutRef, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_LayoutRef", type=gmfgraph_Layout, multiplicity=Multiplicity(1, 1))
    }
)
margins107: BinaryAssociation = BinaryAssociation(
    name="margins107",
    ends={
        Property(name="gmfgraph_Dimension108", type=gmfgraph_GridLayout, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_GridLayout", type=gmfgraph_Dimension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
spacing109: BinaryAssociation = BinaryAssociation(
    name="spacing109",
    ends={
        Property(name="gmfgraph_Dimension111", type=gmfgraph_GridLayout, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_GridLayout110", type=gmfgraph_Dimension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
topLeft114: BinaryAssociation = BinaryAssociation(
    name="topLeft114",
    ends={
        Property(name="gmfgraph_Point115", type=gmfgraph_XYLayoutData, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_XYLayoutData", type=gmfgraph_Point, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
size116: BinaryAssociation = BinaryAssociation(
    name="size116",
    ends={
        Property(name="gmfgraph_Dimension118", type=gmfgraph_XYLayoutData, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_XYLayoutData117", type=gmfgraph_Dimension, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
properties119: BinaryAssociation = BinaryAssociation(
    name="properties119",
    ends={
        Property(name="gmfgraph_SVGProperty", type=gmfgraph_SVGFigure, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_SVGFigure", type=gmfgraph_SVGProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
areaOfInterest120: BinaryAssociation = BinaryAssociation(
    name="areaOfInterest120",
    ends={
        Property(name="gmfgraph_Rectangle2D", type=gmfgraph_SVGFigure, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_SVGFigure121", type=gmfgraph_Rectangle2D, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_gmfgraph_Canvas_Identity = Generalization(general=Identity, specific=gmfgraph_Canvas)
gen_gmfgraph_FigureGallery_Identity = Generalization(general=Identity, specific=gmfgraph_FigureGallery)
gen_gmfgraph_DiagramLabel_Node = Generalization(general=Node, specific=gmfgraph_DiagramLabel)
gen_gmfgraph_GeneralFacet_VisualFacet = Generalization(general=VisualFacet, specific=gmfgraph_GeneralFacet)
gen_gmfgraph_DiagramElement_Identity = Generalization(general=Identity, specific=gmfgraph_DiagramElement)
gen_gmfgraph_AbstractNode_DiagramElement = Generalization(general=DiagramElement, specific=gmfgraph_AbstractNode)
gen_gmfgraph_Node_AbstractNode = Generalization(general=AbstractNode, specific=gmfgraph_Node)
gen_gmfgraph_Connection_DiagramElement = Generalization(general=DiagramElement, specific=gmfgraph_Connection)
gen_gmfgraph_Compartment_DiagramElement = Generalization(general=DiagramElement, specific=gmfgraph_Compartment)
gen_gmfgraph_AlignmentFacet_VisualFacet = Generalization(general=VisualFacet, specific=gmfgraph_AlignmentFacet)
gen_gmfgraph_GradientFacet_VisualFacet = Generalization(general=VisualFacet, specific=gmfgraph_GradientFacet)
gen_gmfgraph_LabelOffsetFacet_VisualFacet = Generalization(general=VisualFacet, specific=gmfgraph_LabelOffsetFacet)
gen_gmfgraph_DefaultSizeFacet_VisualFacet = Generalization(general=VisualFacet, specific=gmfgraph_DefaultSizeFacet)
gen_gmfgraph_Figure_Layoutable = Generalization(general=Layoutable, specific=gmfgraph_Figure)
gen_gmfgraph_ConnectionFigure_RealFigure = Generalization(general=RealFigure, specific=gmfgraph_ConnectionFigure)
gen_gmfgraph_DecorationFigure_RealFigure = Generalization(general=RealFigure, specific=gmfgraph_DecorationFigure)
gen_gmfgraph_Shape_RealFigure = Generalization(general=RealFigure, specific=gmfgraph_Shape)
gen_gmfgraph_AbstractFigure_Figure = Generalization(general=Figure, specific=gmfgraph_AbstractFigure)
gen_gmfgraph_FigureDescriptor_Identity = Generalization(general=Identity, specific=gmfgraph_FigureDescriptor)
gen_gmfgraph_RealFigure_AbstractFigure = Generalization(general=AbstractFigure, specific=gmfgraph_RealFigure)
gen_gmfgraph_FigureRef_AbstractFigure = Generalization(general=AbstractFigure, specific=gmfgraph_FigureRef)
gen_gmfgraph_ScalablePolygon_Polygon = Generalization(general=Polygon, specific=gmfgraph_ScalablePolygon)
gen_gmfgraph_PolylineConnection_Polyline = Generalization(general=Polyline, specific=gmfgraph_PolylineConnection)
gen_gmfgraph_PolylineConnection_ConnectionFigure = Generalization(general=ConnectionFigure, specific=gmfgraph_PolylineConnection)
gen_gmfgraph_Label_RealFigure = Generalization(general=RealFigure, specific=gmfgraph_Label)
gen_gmfgraph_LabeledContainer_RealFigure = Generalization(general=RealFigure, specific=gmfgraph_LabeledContainer)
gen_gmfgraph_Rectangle_Shape = Generalization(general=Shape, specific=gmfgraph_Rectangle)
gen_gmfgraph_RoundedRectangle_Shape = Generalization(general=Shape, specific=gmfgraph_RoundedRectangle)
gen_gmfgraph_Ellipse_Shape = Generalization(general=Shape, specific=gmfgraph_Ellipse)
gen_gmfgraph_Polyline_Shape = Generalization(general=Shape, specific=gmfgraph_Polyline)
gen_gmfgraph_Polygon_Polyline = Generalization(general=Polyline, specific=gmfgraph_Polygon)
gen_gmfgraph_RGBColor_Color = Generalization(general=Color, specific=gmfgraph_RGBColor)
gen_gmfgraph_ConstantColor_Color = Generalization(general=Color, specific=gmfgraph_ConstantColor)
gen_gmfgraph_PolylineDecoration_Polyline = Generalization(general=Polyline, specific=gmfgraph_PolylineDecoration)
gen_gmfgraph_PolylineDecoration_DecorationFigure = Generalization(general=DecorationFigure, specific=gmfgraph_PolylineDecoration)
gen_gmfgraph_PolygonDecoration_Polygon = Generalization(general=Polygon, specific=gmfgraph_PolygonDecoration)
gen_gmfgraph_PolygonDecoration_DecorationFigure = Generalization(general=DecorationFigure, specific=gmfgraph_PolygonDecoration)
gen_gmfgraph_CustomFigure_RealFigure = Generalization(general=RealFigure, specific=gmfgraph_CustomFigure)
gen_gmfgraph_CustomFigure_CustomClass = Generalization(general=CustomClass, specific=gmfgraph_CustomFigure)
gen_gmfgraph_CustomDecoration_CustomFigure = Generalization(general=CustomFigure, specific=gmfgraph_CustomDecoration)
gen_gmfgraph_CustomDecoration_DecorationFigure = Generalization(general=DecorationFigure, specific=gmfgraph_CustomDecoration)
gen_gmfgraph_CustomConnection_CustomFigure = Generalization(general=CustomFigure, specific=gmfgraph_CustomConnection)
gen_gmfgraph_CustomConnection_ConnectionFigure = Generalization(general=ConnectionFigure, specific=gmfgraph_CustomConnection)
gen_gmfgraph_LineBorder_Border = Generalization(general=Border, specific=gmfgraph_LineBorder)
gen_gmfgraph_MarginBorder_Border = Generalization(general=Border, specific=gmfgraph_MarginBorder)
gen_gmfgraph_BasicFont_Font = Generalization(general=Font, specific=gmfgraph_BasicFont)
gen_gmfgraph_BorderRef_Border = Generalization(general=Border, specific=gmfgraph_BorderRef)
gen_gmfgraph_BorderLayoutData_LayoutData = Generalization(general=LayoutData, specific=gmfgraph_BorderLayoutData)
gen_gmfgraph_CompoundBorder_Border = Generalization(general=Border, specific=gmfgraph_CompoundBorder)
gen_gmfgraph_CustomBorder_Border = Generalization(general=Border, specific=gmfgraph_CustomBorder)
gen_gmfgraph_CustomBorder_CustomClass = Generalization(general=CustomClass, specific=gmfgraph_CustomBorder)
gen_gmfgraph_CustomLayoutData_LayoutData = Generalization(general=LayoutData, specific=gmfgraph_CustomLayoutData)
gen_gmfgraph_CustomLayoutData_CustomClass = Generalization(general=CustomClass, specific=gmfgraph_CustomLayoutData)
gen_gmfgraph_GridLayoutData_LayoutData = Generalization(general=LayoutData, specific=gmfgraph_GridLayoutData)
gen_gmfgraph_FlowLayout_Layout = Generalization(general=Layout, specific=gmfgraph_FlowLayout)
gen_gmfgraph_LayoutRef_Layout = Generalization(general=Layout, specific=gmfgraph_LayoutRef)
gen_gmfgraph_CustomLayout_Layout = Generalization(general=Layout, specific=gmfgraph_CustomLayout)
gen_gmfgraph_CustomLayout_CustomClass = Generalization(general=CustomClass, specific=gmfgraph_CustomLayout)
gen_gmfgraph_GridLayout_Layout = Generalization(general=Layout, specific=gmfgraph_GridLayout)
gen_gmfgraph_BorderLayout_Layout = Generalization(general=Layout, specific=gmfgraph_BorderLayout)
gen_gmfgraph_XYLayout_Layout = Generalization(general=Layout, specific=gmfgraph_XYLayout)
gen_gmfgraph_XYLayoutData_LayoutData = Generalization(general=LayoutData, specific=gmfgraph_XYLayoutData)
gen_gmfgraph_StackLayout_Layout = Generalization(general=Layout, specific=gmfgraph_StackLayout)
gen_gmfgraph_SVGFigure_RealFigure = Generalization(general=RealFigure, specific=gmfgraph_SVGFigure)

# Domain Model
domain_model = DomainModel(
    name="gmfgraph",
    types={gmfgraph_Border, gmfgraph_Layout, gmfgraph_Canvas, Identity, gmfgraph_FigureGallery, gmfgraph_Node, gmfgraph_Connection, gmfgraph_Compartment, gmfgraph_DiagramLabel, gmfgraph_RealFigure, gmfgraph_FigureDescriptor, Node, gmfgraph_GeneralFacet, VisualFacet, gmfgraph_Identity, gmfgraph_DiagramElement, gmfgraph_VisualFacet, gmfgraph_AbstractNode, DiagramElement, AbstractNode, gmfgraph_ChildAccess, gmfgraph_Font, gmfgraph_Insets, gmfgraph_AlignmentFacet, gmfgraph_GradientFacet, gmfgraph_LabelOffsetFacet, gmfgraph_DefaultSizeFacet, gmfgraph_Dimension, gmfgraph_Figure, Layoutable, gmfgraph_Color, gmfgraph_ConnectionFigure, RealFigure, gmfgraph_DecorationFigure, gmfgraph_Shape, gmfgraph_Point, gmfgraph_AbstractFigure, Figure, AbstractFigure, gmfgraph_FigureRef, gmfgraph_ScalablePolygon, Polygon, gmfgraph_PolylineConnection, ConnectionFigure, gmfgraph_Label, gmfgraph_LabeledContainer, gmfgraph_Rectangle, Shape, gmfgraph_RoundedRectangle, gmfgraph_Ellipse, gmfgraph_Polyline, gmfgraph_Polygon, Polyline, gmfgraph_RGBColor, Color, gmfgraph_ConstantColor, gmfgraph_PolylineDecoration, DecorationFigure, gmfgraph_PolygonDecoration, gmfgraph_CustomClass, gmfgraph_CustomAttribute, gmfgraph_FigureAccessor, gmfgraph_CustomFigure, CustomClass, gmfgraph_CustomDecoration, CustomFigure, gmfgraph_CustomConnection, gmfgraph_LineBorder, gmfgraph_MarginBorder, gmfgraph_BasicFont, Font, gmfgraph_BorderRef, Border, gmfgraph_BorderLayoutData, gmfgraph_CompoundBorder, gmfgraph_CustomBorder, gmfgraph_LayoutData, gmfgraph_Layoutable, gmfgraph_CustomLayoutData, LayoutData, gmfgraph_GridLayoutData, gmfgraph_FlowLayout, gmfgraph_LayoutRef, Layout, gmfgraph_CustomLayout, gmfgraph_GridLayout, gmfgraph_BorderLayout, gmfgraph_XYLayout, gmfgraph_XYLayoutData, gmfgraph_StackLayout, gmfgraph_SVGFigure, gmfgraph_SVGProperty, gmfgraph_Rectangle2D, ColorConstants, FontStyle, Direction, LineKind, Alignment, SVGPropertyType},
    associations={descriptors11, borders13, layouts15, figures0, nodes1, connections3, compartments5, labels7, figures9, accessor26, container29, figure17, facets19, contentPane21, accessor23, minimumSize43, preferredSize46, font49, insets51, defaultSize32, descriptor33, foregroundColor35, backgroundColor37, maximumSize40, figure72, border53, location56, size58, actualFigure61, accessors64, owner65, figure66, children69, sourceDecoration78, targetDecoration79, resolvedChildren74, template76, attributes82, typedFigure83, customChildren85, actual87, color89, sizeHint99, insets91, outer93, inner95, owner98, spacing112, layoutData101, layout103, actual105, margins107, spacing109, topLeft114, size116, properties119, areaOfInterest120},
    generalizations={gen_gmfgraph_Canvas_Identity, gen_gmfgraph_FigureGallery_Identity, gen_gmfgraph_DiagramLabel_Node, gen_gmfgraph_GeneralFacet_VisualFacet, gen_gmfgraph_DiagramElement_Identity, gen_gmfgraph_AbstractNode_DiagramElement, gen_gmfgraph_Node_AbstractNode, gen_gmfgraph_Connection_DiagramElement, gen_gmfgraph_Compartment_DiagramElement, gen_gmfgraph_AlignmentFacet_VisualFacet, gen_gmfgraph_GradientFacet_VisualFacet, gen_gmfgraph_LabelOffsetFacet_VisualFacet, gen_gmfgraph_DefaultSizeFacet_VisualFacet, gen_gmfgraph_Figure_Layoutable, gen_gmfgraph_ConnectionFigure_RealFigure, gen_gmfgraph_DecorationFigure_RealFigure, gen_gmfgraph_Shape_RealFigure, gen_gmfgraph_AbstractFigure_Figure, gen_gmfgraph_FigureDescriptor_Identity, gen_gmfgraph_RealFigure_AbstractFigure, gen_gmfgraph_FigureRef_AbstractFigure, gen_gmfgraph_ScalablePolygon_Polygon, gen_gmfgraph_PolylineConnection_Polyline, gen_gmfgraph_PolylineConnection_ConnectionFigure, gen_gmfgraph_Label_RealFigure, gen_gmfgraph_LabeledContainer_RealFigure, gen_gmfgraph_Rectangle_Shape, gen_gmfgraph_RoundedRectangle_Shape, gen_gmfgraph_Ellipse_Shape, gen_gmfgraph_Polyline_Shape, gen_gmfgraph_Polygon_Polyline, gen_gmfgraph_RGBColor_Color, gen_gmfgraph_ConstantColor_Color, gen_gmfgraph_PolylineDecoration_Polyline, gen_gmfgraph_PolylineDecoration_DecorationFigure, gen_gmfgraph_PolygonDecoration_Polygon, gen_gmfgraph_PolygonDecoration_DecorationFigure, gen_gmfgraph_CustomFigure_RealFigure, gen_gmfgraph_CustomFigure_CustomClass, gen_gmfgraph_CustomDecoration_CustomFigure, gen_gmfgraph_CustomDecoration_DecorationFigure, gen_gmfgraph_CustomConnection_CustomFigure, gen_gmfgraph_CustomConnection_ConnectionFigure, gen_gmfgraph_LineBorder_Border, gen_gmfgraph_MarginBorder_Border, gen_gmfgraph_BasicFont_Font, gen_gmfgraph_BorderRef_Border, gen_gmfgraph_BorderLayoutData_LayoutData, gen_gmfgraph_CompoundBorder_Border, gen_gmfgraph_CustomBorder_Border, gen_gmfgraph_CustomBorder_CustomClass, gen_gmfgraph_CustomLayoutData_LayoutData, gen_gmfgraph_CustomLayoutData_CustomClass, gen_gmfgraph_GridLayoutData_LayoutData, gen_gmfgraph_FlowLayout_Layout, gen_gmfgraph_LayoutRef_Layout, gen_gmfgraph_CustomLayout_Layout, gen_gmfgraph_CustomLayout_CustomClass, gen_gmfgraph_GridLayout_Layout, gen_gmfgraph_BorderLayout_Layout, gen_gmfgraph_XYLayout_Layout, gen_gmfgraph_XYLayoutData_LayoutData, gen_gmfgraph_StackLayout_Layout, gen_gmfgraph_SVGFigure_RealFigure},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)