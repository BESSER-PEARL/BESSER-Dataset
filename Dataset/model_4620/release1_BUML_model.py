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

FontStyle: Enumeration = Enumeration(
    name="FontStyle",
    literals={
            EnumerationLiteral(name="NORMAL"),
			EnumerationLiteral(name="BOLD"),
			EnumerationLiteral(name="ITALIC")
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

# Classes
gmfgraph_Identity = Class(name="gmfgraph::Identity", is_abstract=True)
gmfgraph_Canvas = Class(name="gmfgraph::Canvas")
Identity = Class(name="Identity")
gmfgraph_FigureGallery = Class(name="gmfgraph::FigureGallery")
gmfgraph_Node = Class(name="gmfgraph::Node")
gmfgraph_Compartment = Class(name="gmfgraph::Compartment")
gmfgraph_DiagramLabel = Class(name="gmfgraph::DiagramLabel")
gmfgraph_RealFigure = Class(name="gmfgraph::RealFigure", is_abstract=True)
gmfgraph_FigureDescriptor = Class(name="gmfgraph::FigureDescriptor")
gmfgraph_DiagramElement = Class(name="gmfgraph::DiagramElement", is_abstract=True)
gmfgraph_VisualFacet = Class(name="gmfgraph::VisualFacet", is_abstract=True)
AbstractNode = Class(name="AbstractNode")
gmfgraph_ChildAccess = Class(name="gmfgraph::ChildAccess")
DiagramElement = Class(name="DiagramElement")
Node = Class(name="Node")
gmfgraph_GeneralFacet = Class(name="gmfgraph::GeneralFacet")
VisualFacet = Class(name="VisualFacet")
gmfgraph_AlignmentFacet = Class(name="gmfgraph::AlignmentFacet")
gmfgraph_Connection = Class(name="gmfgraph::Connection")
gmfgraph_LabelOffsetFacet = Class(name="gmfgraph::LabelOffsetFacet")
gmfgraph_CustomClass = Class(name="gmfgraph::CustomClass", is_abstract=True)
gmfgraph_CustomAttribute = Class(name="gmfgraph::CustomAttribute")
gmfgraph_FigureAccessor = Class(name="gmfgraph::FigureAccessor")
gmfgraph_Color = Class(name="gmfgraph::Color", is_abstract=True)
gmfgraph_RGBColor = Class(name="gmfgraph::RGBColor")
Color = Class(name="Color")
gmfgraph_ConstantColor = Class(name="gmfgraph::ConstantColor")
gmfgraph_Font = Class(name="gmfgraph::Font", is_abstract=True)
gmfgraph_BasicFont = Class(name="gmfgraph::BasicFont")
gmfgraph_GradientFacet = Class(name="gmfgraph::GradientFacet")
gmfgraph_Point = Class(name="gmfgraph::Point")
gmfgraph_Dimension = Class(name="gmfgraph::Dimension")
gmfgraph_Insets = Class(name="gmfgraph::Insets")
gmfgraph_Border = Class(name="gmfgraph::Border", is_abstract=True)
gmfgraph_LineBorder = Class(name="gmfgraph::LineBorder")
Border = Class(name="Border")
gmfgraph_MarginBorder = Class(name="gmfgraph::MarginBorder")
gmfgraph_CompoundBorder = Class(name="gmfgraph::CompoundBorder")
gmfgraph_CustomBorder = Class(name="gmfgraph::CustomBorder")
CustomClass = Class(name="CustomClass")
Font = Class(name="Font")
gmfgraph_GridLayoutData = Class(name="gmfgraph::GridLayoutData")
gmfgraph_BorderLayoutData = Class(name="gmfgraph::BorderLayoutData")
gmfgraph_Layout = Class(name="gmfgraph::Layout", is_abstract=True)
gmfgraph_Figure = Class(name="gmfgraph::Figure", is_abstract=True)
Layoutable = Class(name="Layoutable")
gmfgraph_LayoutData = Class(name="gmfgraph::LayoutData", is_abstract=True)
gmfgraph_Layoutable = Class(name="gmfgraph::Layoutable", is_abstract=True)
gmfgraph_CustomLayoutData = Class(name="gmfgraph::CustomLayoutData")
LayoutData = Class(name="LayoutData")
AbstractFigure = Class(name="AbstractFigure")
gmfgraph_ConnectionFigure = Class(name="gmfgraph::ConnectionFigure", is_abstract=True)
RealFigure = Class(name="RealFigure")
gmfgraph_DecorationFigure = Class(name="gmfgraph::DecorationFigure", is_abstract=True)
gmfgraph_Shape = Class(name="gmfgraph::Shape", is_abstract=True)
gmfgraph_Label = Class(name="gmfgraph::Label")
gmfgraph_LabeledContainer = Class(name="gmfgraph::LabeledContainer")
gmfgraph_Rectangle = Class(name="gmfgraph::Rectangle")
Shape = Class(name="Shape")
gmfgraph_RoundedRectangle = Class(name="gmfgraph::RoundedRectangle")
gmfgraph_Ellipse = Class(name="gmfgraph::Ellipse")
gmfgraph_Polyline = Class(name="gmfgraph::Polyline")
gmfgraph_Polygon = Class(name="gmfgraph::Polygon")
Polyline = Class(name="Polyline")
gmfgraph_FigureRef = Class(name="gmfgraph::FigureRef")
gmfgraph_PolylineDecoration = Class(name="gmfgraph::PolylineDecoration")
DecorationFigure = Class(name="DecorationFigure")
gmfgraph_PolygonDecoration = Class(name="gmfgraph::PolygonDecoration")
Polygon = Class(name="Polygon")
gmfgraph_CustomFigure = Class(name="gmfgraph::CustomFigure")
gmfgraph_CustomDecoration = Class(name="gmfgraph::CustomDecoration")
CustomFigure = Class(name="CustomFigure")
gmfgraph_CustomConnection = Class(name="gmfgraph::CustomConnection")
gmfgraph_CustomLayout = Class(name="gmfgraph::CustomLayout")
Layout = Class(name="Layout")
gmfgraph_GridLayout = Class(name="gmfgraph::GridLayout")
gmfgraph_BorderLayout = Class(name="gmfgraph::BorderLayout")
gmfgraph_FlowLayout = Class(name="gmfgraph::FlowLayout")
gmfgraph_XYLayout = Class(name="gmfgraph::XYLayout")
gmfgraph_PolylineConnection = Class(name="gmfgraph::PolylineConnection")
ConnectionFigure = Class(name="ConnectionFigure")
gmfgraph_StackLayout = Class(name="gmfgraph::StackLayout")
gmfgraph_ScalablePolygon = Class(name="gmfgraph::ScalablePolygon")
gmfgraph_DefaultSizeFacet = Class(name="gmfgraph::DefaultSizeFacet")
gmfgraph_AbstractNode = Class(name="gmfgraph::AbstractNode", is_abstract=True)
gmfgraph_AbstractFigure = Class(name="gmfgraph::AbstractFigure", is_abstract=True)
Figure = Class(name="Figure")
gmfgraph_XYLayoutData = Class(name="gmfgraph::XYLayoutData")

# gmfgraph_Identity class attributes and methods
gmfgraph_Identity_name: Property = Property(name="name", type=StringType)
gmfgraph_Identity.attributes={gmfgraph_Identity_name}

# gmfgraph_Canvas class attributes and methods

# Identity class attributes and methods

# gmfgraph_FigureGallery class attributes and methods
gmfgraph_FigureGallery_implementationBundle: Property = Property(name="implementationBundle", type=StringType)
gmfgraph_FigureGallery.attributes={gmfgraph_FigureGallery_implementationBundle}

# gmfgraph_Node class attributes and methods
gmfgraph_Node_resizeConstraint: Property = Property(name="resizeConstraint", type=StringType)
gmfgraph_Node_affixedParentSide: Property = Property(name="affixedParentSide", type=StringType)
gmfgraph_Node.attributes={gmfgraph_Node_resizeConstraint, gmfgraph_Node_affixedParentSide}

# gmfgraph_Compartment class attributes and methods
gmfgraph_Compartment_collapsible: Property = Property(name="collapsible", type=BooleanType)
gmfgraph_Compartment_needsTitle: Property = Property(name="needsTitle", type=BooleanType)
gmfgraph_Compartment.attributes={gmfgraph_Compartment_collapsible, gmfgraph_Compartment_needsTitle}

# gmfgraph_DiagramLabel class attributes and methods
gmfgraph_DiagramLabel_elementIcon: Property = Property(name="elementIcon", type=BooleanType)
gmfgraph_DiagramLabel_external: Property = Property(name="external", type=BooleanType)
gmfgraph_DiagramLabel.attributes={gmfgraph_DiagramLabel_external, gmfgraph_DiagramLabel_elementIcon}

# gmfgraph_RealFigure class attributes and methods
gmfgraph_RealFigure_name: Property = Property(name="name", type=StringType)
gmfgraph_RealFigure.attributes={gmfgraph_RealFigure_name}

# gmfgraph_FigureDescriptor class attributes and methods

# gmfgraph_DiagramElement class attributes and methods

# gmfgraph_VisualFacet class attributes and methods

# AbstractNode class attributes and methods

# gmfgraph_ChildAccess class attributes and methods
gmfgraph_ChildAccess_accessor: Property = Property(name="accessor", type=StringType)
gmfgraph_ChildAccess.attributes={gmfgraph_ChildAccess_accessor}

# DiagramElement class attributes and methods

# Node class attributes and methods

# gmfgraph_GeneralFacet class attributes and methods
gmfgraph_GeneralFacet_identifier: Property = Property(name="identifier", type=StringType)
gmfgraph_GeneralFacet_data: Property = Property(name="data", type=StringType)
gmfgraph_GeneralFacet.attributes={gmfgraph_GeneralFacet_identifier, gmfgraph_GeneralFacet_data}

# VisualFacet class attributes and methods

# gmfgraph_AlignmentFacet class attributes and methods
gmfgraph_AlignmentFacet_alignment: Property = Property(name="alignment", type=StringType)
gmfgraph_AlignmentFacet.attributes={gmfgraph_AlignmentFacet_alignment}

# gmfgraph_Connection class attributes and methods

# gmfgraph_LabelOffsetFacet class attributes and methods
gmfgraph_LabelOffsetFacet_x: Property = Property(name="x", type=IntegerType)
gmfgraph_LabelOffsetFacet_y: Property = Property(name="y", type=IntegerType)
gmfgraph_LabelOffsetFacet.attributes={gmfgraph_LabelOffsetFacet_y, gmfgraph_LabelOffsetFacet_x}

# gmfgraph_CustomClass class attributes and methods
gmfgraph_CustomClass_qualifiedClassName: Property = Property(name="qualifiedClassName", type=StringType)
gmfgraph_CustomClass.attributes={gmfgraph_CustomClass_qualifiedClassName}

# gmfgraph_CustomAttribute class attributes and methods
gmfgraph_CustomAttribute_name: Property = Property(name="name", type=StringType)
gmfgraph_CustomAttribute_value: Property = Property(name="value", type=StringType)
gmfgraph_CustomAttribute_directAccess: Property = Property(name="directAccess", type=BooleanType)
gmfgraph_CustomAttribute_multiStatementValue: Property = Property(name="multiStatementValue", type=BooleanType)
gmfgraph_CustomAttribute.attributes={gmfgraph_CustomAttribute_name, gmfgraph_CustomAttribute_value, gmfgraph_CustomAttribute_directAccess, gmfgraph_CustomAttribute_multiStatementValue}

# gmfgraph_FigureAccessor class attributes and methods
gmfgraph_FigureAccessor_accessor: Property = Property(name="accessor", type=StringType)
gmfgraph_FigureAccessor.attributes={gmfgraph_FigureAccessor_accessor}

# gmfgraph_Color class attributes and methods

# gmfgraph_RGBColor class attributes and methods
gmfgraph_RGBColor_red: Property = Property(name="red", type=IntegerType)
gmfgraph_RGBColor_green: Property = Property(name="green", type=IntegerType)
gmfgraph_RGBColor_blue: Property = Property(name="blue", type=IntegerType)
gmfgraph_RGBColor.attributes={gmfgraph_RGBColor_red, gmfgraph_RGBColor_green, gmfgraph_RGBColor_blue}

# Color class attributes and methods

# gmfgraph_ConstantColor class attributes and methods
gmfgraph_ConstantColor_value: Property = Property(name="value", type=StringType)
gmfgraph_ConstantColor.attributes={gmfgraph_ConstantColor_value}

# gmfgraph_Font class attributes and methods

# gmfgraph_BasicFont class attributes and methods
gmfgraph_BasicFont_faceName: Property = Property(name="faceName", type=StringType)
gmfgraph_BasicFont_height: Property = Property(name="height", type=IntegerType)
gmfgraph_BasicFont_style: Property = Property(name="style", type=StringType)
gmfgraph_BasicFont.attributes={gmfgraph_BasicFont_height, gmfgraph_BasicFont_faceName, gmfgraph_BasicFont_style}

# gmfgraph_GradientFacet class attributes and methods
gmfgraph_GradientFacet_direction: Property = Property(name="direction", type=StringType)
gmfgraph_GradientFacet.attributes={gmfgraph_GradientFacet_direction}

# gmfgraph_Point class attributes and methods
gmfgraph_Point_x: Property = Property(name="x", type=IntegerType)
gmfgraph_Point_y: Property = Property(name="y", type=IntegerType)
gmfgraph_Point.attributes={gmfgraph_Point_y, gmfgraph_Point_x}

# gmfgraph_Dimension class attributes and methods
gmfgraph_Dimension_dx: Property = Property(name="dx", type=IntegerType)
gmfgraph_Dimension_dy: Property = Property(name="dy", type=IntegerType)
gmfgraph_Dimension.attributes={gmfgraph_Dimension_dy, gmfgraph_Dimension_dx}

# gmfgraph_Insets class attributes and methods
gmfgraph_Insets_top: Property = Property(name="top", type=IntegerType)
gmfgraph_Insets_left: Property = Property(name="left", type=IntegerType)
gmfgraph_Insets_bottom: Property = Property(name="bottom", type=IntegerType)
gmfgraph_Insets_right: Property = Property(name="right", type=IntegerType)
gmfgraph_Insets.attributes={gmfgraph_Insets_left, gmfgraph_Insets_top, gmfgraph_Insets_bottom, gmfgraph_Insets_right}

# gmfgraph_Border class attributes and methods

# gmfgraph_LineBorder class attributes and methods
gmfgraph_LineBorder_width: Property = Property(name="width", type=IntegerType)
gmfgraph_LineBorder.attributes={gmfgraph_LineBorder_width}

# Border class attributes and methods

# gmfgraph_MarginBorder class attributes and methods

# gmfgraph_CompoundBorder class attributes and methods

# gmfgraph_CustomBorder class attributes and methods

# CustomClass class attributes and methods

# Font class attributes and methods

# gmfgraph_GridLayoutData class attributes and methods
gmfgraph_GridLayoutData_grabExcessHorizontalSpace: Property = Property(name="grabExcessHorizontalSpace", type=BooleanType)
gmfgraph_GridLayoutData_grabExcessVerticalSpace: Property = Property(name="grabExcessVerticalSpace", type=BooleanType)
gmfgraph_GridLayoutData_verticalSpan: Property = Property(name="verticalSpan", type=IntegerType)
gmfgraph_GridLayoutData_horizontalSpan: Property = Property(name="horizontalSpan", type=IntegerType)
gmfgraph_GridLayoutData_horizontalIndent: Property = Property(name="horizontalIndent", type=IntegerType)
gmfgraph_GridLayoutData_verticalAlignment: Property = Property(name="verticalAlignment", type=StringType)
gmfgraph_GridLayoutData_horizontalAlignment: Property = Property(name="horizontalAlignment", type=StringType)
gmfgraph_GridLayoutData.attributes={gmfgraph_GridLayoutData_horizontalSpan, gmfgraph_GridLayoutData_verticalAlignment, gmfgraph_GridLayoutData_grabExcessVerticalSpace, gmfgraph_GridLayoutData_horizontalAlignment, gmfgraph_GridLayoutData_grabExcessHorizontalSpace, gmfgraph_GridLayoutData_verticalSpan, gmfgraph_GridLayoutData_horizontalIndent}

# gmfgraph_BorderLayoutData class attributes and methods
gmfgraph_BorderLayoutData_vertical: Property = Property(name="vertical", type=BooleanType)
gmfgraph_BorderLayoutData_alignment: Property = Property(name="alignment", type=StringType)
gmfgraph_BorderLayoutData.attributes={gmfgraph_BorderLayoutData_alignment, gmfgraph_BorderLayoutData_vertical}

# gmfgraph_Layout class attributes and methods

# gmfgraph_Figure class attributes and methods

# Layoutable class attributes and methods

# gmfgraph_LayoutData class attributes and methods

# gmfgraph_Layoutable class attributes and methods

# gmfgraph_CustomLayoutData class attributes and methods

# LayoutData class attributes and methods

# AbstractFigure class attributes and methods

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
gmfgraph_Shape.attributes={gmfgraph_Shape_fill, gmfgraph_Shape_xorFill, gmfgraph_Shape_lineKind, gmfgraph_Shape_outline, gmfgraph_Shape_lineWidth, gmfgraph_Shape_xorOutline}

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

# gmfgraph_FigureRef class attributes and methods

# gmfgraph_PolylineDecoration class attributes and methods

# DecorationFigure class attributes and methods

# gmfgraph_PolygonDecoration class attributes and methods

# Polygon class attributes and methods

# gmfgraph_CustomFigure class attributes and methods

# gmfgraph_CustomDecoration class attributes and methods

# CustomFigure class attributes and methods

# gmfgraph_CustomConnection class attributes and methods

# gmfgraph_CustomLayout class attributes and methods

# Layout class attributes and methods

# gmfgraph_GridLayout class attributes and methods
gmfgraph_GridLayout_numColumns: Property = Property(name="numColumns", type=IntegerType)
gmfgraph_GridLayout_equalWidth: Property = Property(name="equalWidth", type=BooleanType)
gmfgraph_GridLayout.attributes={gmfgraph_GridLayout_equalWidth, gmfgraph_GridLayout_numColumns}

# gmfgraph_BorderLayout class attributes and methods

# gmfgraph_FlowLayout class attributes and methods
gmfgraph_FlowLayout_vertical: Property = Property(name="vertical", type=BooleanType)
gmfgraph_FlowLayout_matchMinorSize: Property = Property(name="matchMinorSize", type=BooleanType)
gmfgraph_FlowLayout_forceSingleLine: Property = Property(name="forceSingleLine", type=BooleanType)
gmfgraph_FlowLayout_majorAlignment: Property = Property(name="majorAlignment", type=StringType)
gmfgraph_FlowLayout_minorAlignment: Property = Property(name="minorAlignment", type=StringType)
gmfgraph_FlowLayout_majorSpacing: Property = Property(name="majorSpacing", type=IntegerType)
gmfgraph_FlowLayout_minorSpacing: Property = Property(name="minorSpacing", type=IntegerType)
gmfgraph_FlowLayout.attributes={gmfgraph_FlowLayout_minorSpacing, gmfgraph_FlowLayout_vertical, gmfgraph_FlowLayout_majorSpacing, gmfgraph_FlowLayout_minorAlignment, gmfgraph_FlowLayout_majorAlignment, gmfgraph_FlowLayout_matchMinorSize, gmfgraph_FlowLayout_forceSingleLine}

# gmfgraph_XYLayout class attributes and methods

# gmfgraph_PolylineConnection class attributes and methods

# ConnectionFigure class attributes and methods

# gmfgraph_StackLayout class attributes and methods

# gmfgraph_ScalablePolygon class attributes and methods

# gmfgraph_DefaultSizeFacet class attributes and methods

# gmfgraph_AbstractNode class attributes and methods

# gmfgraph_AbstractFigure class attributes and methods

# Figure class attributes and methods

# gmfgraph_XYLayoutData class attributes and methods

# Relationships
figures0: BinaryAssociation = BinaryAssociation(
    name="figures0",
    ends={
        Property(name="gmfgraph_FigureGallery", type=gmfgraph_Canvas, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_Canvas", type=gmfgraph_FigureGallery, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
descriptors11: BinaryAssociation = BinaryAssociation(
    name="descriptors11",
    ends={
        Property(name="gmfgraph_FigureDescriptor", type=gmfgraph_FigureGallery, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_FigureGallery12", type=gmfgraph_FigureDescriptor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
facets13: BinaryAssociation = BinaryAssociation(
    name="facets13",
    ends={
        Property(name="gmfgraph_VisualFacet", type=gmfgraph_DiagramElement, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_DiagramElement", type=gmfgraph_VisualFacet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
figure14: BinaryAssociation = BinaryAssociation(
    name="figure14",
    ends={
        Property(name="gmfgraph_FigureDescriptor16", type=gmfgraph_DiagramElement, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_DiagramElement15", type=gmfgraph_FigureDescriptor, multiplicity=Multiplicity(1, 1))
    }
)
contentPane17: BinaryAssociation = BinaryAssociation(
    name="contentPane17",
    ends={
        Property(name="gmfgraph_ChildAccess", type=gmfgraph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_Node18", type=gmfgraph_ChildAccess, multiplicity=Multiplicity(0, 1))
    }
)
accessor19: BinaryAssociation = BinaryAssociation(
    name="accessor19",
    ends={
        Property(name="gmfgraph_ChildAccess21", type=gmfgraph_Compartment, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_Compartment20", type=gmfgraph_ChildAccess, multiplicity=Multiplicity(0, 1))
    }
)
accessor22: BinaryAssociation = BinaryAssociation(
    name="accessor22",
    ends={
        Property(name="gmfgraph_ChildAccess24", type=gmfgraph_DiagramLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_DiagramLabel23", type=gmfgraph_ChildAccess, multiplicity=Multiplicity(0, 1))
    }
)
container25: BinaryAssociation = BinaryAssociation(
    name="container25",
    ends={
        Property(name="gmfgraph_ChildAccess27", type=gmfgraph_DiagramLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_DiagramLabel26", type=gmfgraph_ChildAccess, multiplicity=Multiplicity(0, 1))
    }
)
nodes1: BinaryAssociation = BinaryAssociation(
    name="nodes1",
    ends={
        Property(name="gmfgraph_Node", type=gmfgraph_Canvas, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_Canvas2", type=gmfgraph_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes28: BinaryAssociation = BinaryAssociation(
    name="attributes28",
    ends={
        Property(name="gmfgraph_CustomAttribute", type=gmfgraph_CustomClass, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_CustomClass", type=gmfgraph_CustomAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typedFigure29: BinaryAssociation = BinaryAssociation(
    name="typedFigure29",
    ends={
        Property(name="gmfgraph_RealFigure30", type=gmfgraph_FigureAccessor, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_FigureAccessor", type=gmfgraph_RealFigure, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
color31: BinaryAssociation = BinaryAssociation(
    name="color31",
    ends={
        Property(name="gmfgraph_Color", type=gmfgraph_LineBorder, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_LineBorder", type=gmfgraph_Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
insets32: BinaryAssociation = BinaryAssociation(
    name="insets32",
    ends={
        Property(name="gmfgraph_Insets", type=gmfgraph_MarginBorder, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_MarginBorder", type=gmfgraph_Insets, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
outer33: BinaryAssociation = BinaryAssociation(
    name="outer33",
    ends={
        Property(name="gmfgraph_Border", type=gmfgraph_CompoundBorder, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_CompoundBorder", type=gmfgraph_Border, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inner34: BinaryAssociation = BinaryAssociation(
    name="inner34",
    ends={
        Property(name="gmfgraph_Border36", type=gmfgraph_CompoundBorder, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_CompoundBorder35", type=gmfgraph_Border, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sizeHint38: BinaryAssociation = BinaryAssociation(
    name="sizeHint38",
    ends={
        Property(name="gmfgraph_Dimension", type=gmfgraph_GridLayoutData, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_GridLayoutData", type=gmfgraph_Dimension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
layoutData39: BinaryAssociation = BinaryAssociation(
    name="layoutData39",
    ends={
        Property(name="LayoutData", type=gmfgraph_Layoutable, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=gmfgraph_LayoutData, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
layout40: BinaryAssociation = BinaryAssociation(
    name="layout40",
    ends={
        Property(name="gmfgraph_Layout", type=gmfgraph_Layoutable, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_Layoutable", type=gmfgraph_Layout, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
foregroundColor41: BinaryAssociation = BinaryAssociation(
    name="foregroundColor41",
    ends={
        Property(name="gmfgraph_Color42", type=gmfgraph_Figure, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_Figure", type=gmfgraph_Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
backgroundColor43: BinaryAssociation = BinaryAssociation(
    name="backgroundColor43",
    ends={
        Property(name="gmfgraph_Color45", type=gmfgraph_Figure, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_Figure44", type=gmfgraph_Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
maximumSize46: BinaryAssociation = BinaryAssociation(
    name="maximumSize46",
    ends={
        Property(name="gmfgraph_Dimension48", type=gmfgraph_Figure, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_Figure47", type=gmfgraph_Dimension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
minimumSize49: BinaryAssociation = BinaryAssociation(
    name="minimumSize49",
    ends={
        Property(name="gmfgraph_Dimension51", type=gmfgraph_Figure, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_Figure50", type=gmfgraph_Dimension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
preferredSize52: BinaryAssociation = BinaryAssociation(
    name="preferredSize52",
    ends={
        Property(name="gmfgraph_Dimension54", type=gmfgraph_Figure, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_Figure53", type=gmfgraph_Dimension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
font55: BinaryAssociation = BinaryAssociation(
    name="font55",
    ends={
        Property(name="gmfgraph_Font", type=gmfgraph_Figure, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_Figure56", type=gmfgraph_Font, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
insets57: BinaryAssociation = BinaryAssociation(
    name="insets57",
    ends={
        Property(name="gmfgraph_Insets59", type=gmfgraph_Figure, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_Figure58", type=gmfgraph_Insets, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
border60: BinaryAssociation = BinaryAssociation(
    name="border60",
    ends={
        Property(name="gmfgraph_Border62", type=gmfgraph_Figure, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_Figure61", type=gmfgraph_Border, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
location63: BinaryAssociation = BinaryAssociation(
    name="location63",
    ends={
        Property(name="gmfgraph_Point", type=gmfgraph_Figure, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_Figure64", type=gmfgraph_Point, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
size65: BinaryAssociation = BinaryAssociation(
    name="size65",
    ends={
        Property(name="gmfgraph_Point67", type=gmfgraph_Figure, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_Figure66", type=gmfgraph_Point, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owner37: BinaryAssociation = BinaryAssociation(
    name="owner37",
    ends={
        Property(name="Layoutable", type=gmfgraph_LayoutData, multiplicity=Multiplicity(1, 1)),
        Property(name="layoutData", type=gmfgraph_Layoutable, multiplicity=Multiplicity(1, 1))
    }
)
figure71: BinaryAssociation = BinaryAssociation(
    name="figure71",
    ends={
        Property(name="gmfgraph_RealFigure72", type=gmfgraph_FigureRef, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_FigureRef", type=gmfgraph_RealFigure, multiplicity=Multiplicity(1, 1))
    }
)
resolvedChildren73: BinaryAssociation = BinaryAssociation(
    name="resolvedChildren73",
    ends={
        Property(name="gmfgraph_Figure74", type=gmfgraph_Shape, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_Shape", type=gmfgraph_Figure, multiplicity=Multiplicity(0, 9999))
    }
)
template75: BinaryAssociation = BinaryAssociation(
    name="template75",
    ends={
        Property(name="gmfgraph_Point76", type=gmfgraph_Polyline, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_Polyline", type=gmfgraph_Point, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
descriptor68: BinaryAssociation = BinaryAssociation(
    name="descriptor68",
    ends={
        Property(name="gmfgraph_FigureDescriptor70", type=gmfgraph_Figure, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_Figure69", type=gmfgraph_FigureDescriptor, multiplicity=Multiplicity(0, 1))
    }
)
targetDecoration78: BinaryAssociation = BinaryAssociation(
    name="targetDecoration78",
    ends={
        Property(name="gmfgraph_DecorationFigure80", type=gmfgraph_PolylineConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_PolylineConnection79", type=gmfgraph_DecorationFigure, multiplicity=Multiplicity(0, 1))
    }
)
customChildren81: BinaryAssociation = BinaryAssociation(
    name="customChildren81",
    ends={
        Property(name="gmfgraph_FigureAccessor82", type=gmfgraph_CustomFigure, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_CustomFigure", type=gmfgraph_FigureAccessor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
margins83: BinaryAssociation = BinaryAssociation(
    name="margins83",
    ends={
        Property(name="gmfgraph_Dimension84", type=gmfgraph_GridLayout, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_GridLayout", type=gmfgraph_Dimension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
spacing85: BinaryAssociation = BinaryAssociation(
    name="spacing85",
    ends={
        Property(name="gmfgraph_Dimension87", type=gmfgraph_GridLayout, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_GridLayout86", type=gmfgraph_Dimension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
spacing88: BinaryAssociation = BinaryAssociation(
    name="spacing88",
    ends={
        Property(name="gmfgraph_Dimension89", type=gmfgraph_BorderLayout, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_BorderLayout", type=gmfgraph_Dimension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sourceDecoration77: BinaryAssociation = BinaryAssociation(
    name="sourceDecoration77",
    ends={
        Property(name="gmfgraph_DecorationFigure", type=gmfgraph_PolylineConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_PolylineConnection", type=gmfgraph_DecorationFigure, multiplicity=Multiplicity(0, 1))
    }
)
defaultSize95: BinaryAssociation = BinaryAssociation(
    name="defaultSize95",
    ends={
        Property(name="gmfgraph_Dimension96", type=gmfgraph_DefaultSizeFacet, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_DefaultSizeFacet", type=gmfgraph_Dimension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
children97: BinaryAssociation = BinaryAssociation(
    name="children97",
    ends={
        Property(name="gmfgraph_Figure99", type=gmfgraph_RealFigure, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_RealFigure98", type=gmfgraph_Figure, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
figure100: BinaryAssociation = BinaryAssociation(
    name="figure100",
    ends={
        Property(name="gmfgraph_Figure102", type=gmfgraph_ChildAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_ChildAccess101", type=gmfgraph_Figure, multiplicity=Multiplicity(1, 1))
    }
)
owner103: BinaryAssociation = BinaryAssociation(
    name="owner103",
    ends={
        Property(name="FigureDescriptor", type=gmfgraph_ChildAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="accessors", type=gmfgraph_FigureDescriptor, multiplicity=Multiplicity(1, 1))
    }
)
actualFigure104: BinaryAssociation = BinaryAssociation(
    name="actualFigure104",
    ends={
        Property(name="gmfgraph_Figure106", type=gmfgraph_FigureDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_FigureDescriptor105", type=gmfgraph_Figure, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
accessors107: BinaryAssociation = BinaryAssociation(
    name="accessors107",
    ends={
        Property(name="ChildAccess", type=gmfgraph_FigureDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="owner108", type=gmfgraph_ChildAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
topLeft90: BinaryAssociation = BinaryAssociation(
    name="topLeft90",
    ends={
        Property(name="gmfgraph_Point91", type=gmfgraph_XYLayoutData, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_XYLayoutData", type=gmfgraph_Point, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
size92: BinaryAssociation = BinaryAssociation(
    name="size92",
    ends={
        Property(name="gmfgraph_Dimension94", type=gmfgraph_XYLayoutData, multiplicity=Multiplicity(1, 1)),
        Property(name="gmfgraph_XYLayoutData93", type=gmfgraph_Dimension, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_gmfgraph_Canvas_Identity = Generalization(general=Identity, specific=gmfgraph_Canvas)
gen_gmfgraph_FigureGallery_Identity = Generalization(general=Identity, specific=gmfgraph_FigureGallery)
gen_gmfgraph_DiagramElement_Identity = Generalization(general=Identity, specific=gmfgraph_DiagramElement)
gen_gmfgraph_Node_AbstractNode = Generalization(general=AbstractNode, specific=gmfgraph_Node)
gen_gmfgraph_Connection_DiagramElement = Generalization(general=DiagramElement, specific=gmfgraph_Connection)
gen_gmfgraph_Compartment_DiagramElement = Generalization(general=DiagramElement, specific=gmfgraph_Compartment)
gen_gmfgraph_DiagramLabel_Node = Generalization(general=Node, specific=gmfgraph_DiagramLabel)
gen_gmfgraph_GeneralFacet_VisualFacet = Generalization(general=VisualFacet, specific=gmfgraph_GeneralFacet)
gen_gmfgraph_AlignmentFacet_VisualFacet = Generalization(general=VisualFacet, specific=gmfgraph_AlignmentFacet)
gen_gmfgraph_LabelOffsetFacet_VisualFacet = Generalization(general=VisualFacet, specific=gmfgraph_LabelOffsetFacet)
gen_gmfgraph_RGBColor_Color = Generalization(general=Color, specific=gmfgraph_RGBColor)
gen_gmfgraph_ConstantColor_Color = Generalization(general=Color, specific=gmfgraph_ConstantColor)
gen_gmfgraph_GradientFacet_VisualFacet = Generalization(general=VisualFacet, specific=gmfgraph_GradientFacet)
gen_gmfgraph_LineBorder_Border = Generalization(general=Border, specific=gmfgraph_LineBorder)
gen_gmfgraph_MarginBorder_Border = Generalization(general=Border, specific=gmfgraph_MarginBorder)
gen_gmfgraph_CompoundBorder_Border = Generalization(general=Border, specific=gmfgraph_CompoundBorder)
gen_gmfgraph_CustomBorder_Border = Generalization(general=Border, specific=gmfgraph_CustomBorder)
gen_gmfgraph_CustomBorder_CustomClass = Generalization(general=CustomClass, specific=gmfgraph_CustomBorder)
gen_gmfgraph_BasicFont_Font = Generalization(general=Font, specific=gmfgraph_BasicFont)
gen_gmfgraph_CustomLayoutData_CustomClass = Generalization(general=CustomClass, specific=gmfgraph_CustomLayoutData)
gen_gmfgraph_GridLayoutData_LayoutData = Generalization(general=LayoutData, specific=gmfgraph_GridLayoutData)
gen_gmfgraph_BorderLayoutData_LayoutData = Generalization(general=LayoutData, specific=gmfgraph_BorderLayoutData)
gen_gmfgraph_Figure_Layoutable = Generalization(general=Layoutable, specific=gmfgraph_Figure)
gen_gmfgraph_CustomLayoutData_LayoutData = Generalization(general=LayoutData, specific=gmfgraph_CustomLayoutData)
gen_gmfgraph_FigureRef_AbstractFigure = Generalization(general=AbstractFigure, specific=gmfgraph_FigureRef)
gen_gmfgraph_ConnectionFigure_RealFigure = Generalization(general=RealFigure, specific=gmfgraph_ConnectionFigure)
gen_gmfgraph_DecorationFigure_RealFigure = Generalization(general=RealFigure, specific=gmfgraph_DecorationFigure)
gen_gmfgraph_Shape_RealFigure = Generalization(general=RealFigure, specific=gmfgraph_Shape)
gen_gmfgraph_Label_RealFigure = Generalization(general=RealFigure, specific=gmfgraph_Label)
gen_gmfgraph_LabeledContainer_RealFigure = Generalization(general=RealFigure, specific=gmfgraph_LabeledContainer)
gen_gmfgraph_Rectangle_Shape = Generalization(general=Shape, specific=gmfgraph_Rectangle)
gen_gmfgraph_RoundedRectangle_Shape = Generalization(general=Shape, specific=gmfgraph_RoundedRectangle)
gen_gmfgraph_Ellipse_Shape = Generalization(general=Shape, specific=gmfgraph_Ellipse)
gen_gmfgraph_Polyline_Shape = Generalization(general=Shape, specific=gmfgraph_Polyline)
gen_gmfgraph_Polygon_Polyline = Generalization(general=Polyline, specific=gmfgraph_Polygon)
gen_gmfgraph_PolylineDecoration_Polyline = Generalization(general=Polyline, specific=gmfgraph_PolylineDecoration)
gen_gmfgraph_PolylineDecoration_DecorationFigure = Generalization(general=DecorationFigure, specific=gmfgraph_PolylineDecoration)
gen_gmfgraph_PolygonDecoration_Polygon = Generalization(general=Polygon, specific=gmfgraph_PolygonDecoration)
gen_gmfgraph_PolygonDecoration_DecorationFigure = Generalization(general=DecorationFigure, specific=gmfgraph_PolygonDecoration)
gen_gmfgraph_CustomFigure_CustomClass = Generalization(general=CustomClass, specific=gmfgraph_CustomFigure)
gen_gmfgraph_CustomFigure_RealFigure = Generalization(general=RealFigure, specific=gmfgraph_CustomFigure)
gen_gmfgraph_CustomDecoration_CustomFigure = Generalization(general=CustomFigure, specific=gmfgraph_CustomDecoration)
gen_gmfgraph_CustomDecoration_DecorationFigure = Generalization(general=DecorationFigure, specific=gmfgraph_CustomDecoration)
gen_gmfgraph_CustomConnection_CustomFigure = Generalization(general=CustomFigure, specific=gmfgraph_CustomConnection)
gen_gmfgraph_CustomConnection_ConnectionFigure = Generalization(general=ConnectionFigure, specific=gmfgraph_CustomConnection)
gen_gmfgraph_CustomLayout_Layout = Generalization(general=Layout, specific=gmfgraph_CustomLayout)
gen_gmfgraph_CustomLayout_CustomClass = Generalization(general=CustomClass, specific=gmfgraph_CustomLayout)
gen_gmfgraph_GridLayout_Layout = Generalization(general=Layout, specific=gmfgraph_GridLayout)
gen_gmfgraph_BorderLayout_Layout = Generalization(general=Layout, specific=gmfgraph_BorderLayout)
gen_gmfgraph_FlowLayout_Layout = Generalization(general=Layout, specific=gmfgraph_FlowLayout)
gen_gmfgraph_XYLayout_Layout = Generalization(general=Layout, specific=gmfgraph_XYLayout)
gen_gmfgraph_PolylineConnection_Polyline = Generalization(general=Polyline, specific=gmfgraph_PolylineConnection)
gen_gmfgraph_PolylineConnection_ConnectionFigure = Generalization(general=ConnectionFigure, specific=gmfgraph_PolylineConnection)
gen_gmfgraph_StackLayout_Layout = Generalization(general=Layout, specific=gmfgraph_StackLayout)
gen_gmfgraph_ScalablePolygon_Polygon = Generalization(general=Polygon, specific=gmfgraph_ScalablePolygon)
gen_gmfgraph_DefaultSizeFacet_VisualFacet = Generalization(general=VisualFacet, specific=gmfgraph_DefaultSizeFacet)
gen_gmfgraph_AbstractNode_DiagramElement = Generalization(general=DiagramElement, specific=gmfgraph_AbstractNode)
gen_gmfgraph_RealFigure_AbstractFigure = Generalization(general=AbstractFigure, specific=gmfgraph_RealFigure)
gen_gmfgraph_AbstractFigure_Figure = Generalization(general=Figure, specific=gmfgraph_AbstractFigure)
gen_gmfgraph_FigureDescriptor_Identity = Generalization(general=Identity, specific=gmfgraph_FigureDescriptor)
gen_gmfgraph_XYLayoutData_LayoutData = Generalization(general=LayoutData, specific=gmfgraph_XYLayoutData)

# Domain Model
domain_model = DomainModel(
    name="gmfgraph",
    types={gmfgraph_Identity, gmfgraph_Canvas, Identity, gmfgraph_FigureGallery, gmfgraph_Node, gmfgraph_Compartment, gmfgraph_DiagramLabel, gmfgraph_RealFigure, gmfgraph_FigureDescriptor, gmfgraph_DiagramElement, gmfgraph_VisualFacet, AbstractNode, gmfgraph_ChildAccess, DiagramElement, Node, gmfgraph_GeneralFacet, VisualFacet, gmfgraph_AlignmentFacet, gmfgraph_Connection, gmfgraph_LabelOffsetFacet, gmfgraph_CustomClass, gmfgraph_CustomAttribute, gmfgraph_FigureAccessor, gmfgraph_Color, gmfgraph_RGBColor, Color, gmfgraph_ConstantColor, gmfgraph_Font, gmfgraph_BasicFont, gmfgraph_GradientFacet, gmfgraph_Point, gmfgraph_Dimension, gmfgraph_Insets, gmfgraph_Border, gmfgraph_LineBorder, Border, gmfgraph_MarginBorder, gmfgraph_CompoundBorder, gmfgraph_CustomBorder, CustomClass, Font, gmfgraph_GridLayoutData, gmfgraph_BorderLayoutData, gmfgraph_Layout, gmfgraph_Figure, Layoutable, gmfgraph_LayoutData, gmfgraph_Layoutable, gmfgraph_CustomLayoutData, LayoutData, AbstractFigure, gmfgraph_ConnectionFigure, RealFigure, gmfgraph_DecorationFigure, gmfgraph_Shape, gmfgraph_Label, gmfgraph_LabeledContainer, gmfgraph_Rectangle, Shape, gmfgraph_RoundedRectangle, gmfgraph_Ellipse, gmfgraph_Polyline, gmfgraph_Polygon, Polyline, gmfgraph_FigureRef, gmfgraph_PolylineDecoration, DecorationFigure, gmfgraph_PolygonDecoration, Polygon, gmfgraph_CustomFigure, gmfgraph_CustomDecoration, CustomFigure, gmfgraph_CustomConnection, gmfgraph_CustomLayout, Layout, gmfgraph_GridLayout, gmfgraph_BorderLayout, gmfgraph_FlowLayout, gmfgraph_XYLayout, gmfgraph_PolylineConnection, ConnectionFigure, gmfgraph_StackLayout, gmfgraph_ScalablePolygon, gmfgraph_DefaultSizeFacet, gmfgraph_AbstractNode, gmfgraph_AbstractFigure, Figure, gmfgraph_XYLayoutData, ColorConstants, Direction, LineKind, FontStyle, Alignment},
    associations={figures0, connections3, compartments5, labels7, figures9, descriptors11, facets13, figure14, contentPane17, accessor19, accessor22, container25, nodes1, attributes28, typedFigure29, color31, insets32, outer33, inner34, sizeHint38, layoutData39, layout40, foregroundColor41, backgroundColor43, maximumSize46, minimumSize49, preferredSize52, font55, insets57, border60, location63, size65, owner37, figure71, resolvedChildren73, template75, descriptor68, targetDecoration78, customChildren81, margins83, spacing85, spacing88, sourceDecoration77, defaultSize95, children97, figure100, owner103, actualFigure104, accessors107, topLeft90, size92},
    generalizations={gen_gmfgraph_Canvas_Identity, gen_gmfgraph_FigureGallery_Identity, gen_gmfgraph_DiagramElement_Identity, gen_gmfgraph_Node_AbstractNode, gen_gmfgraph_Connection_DiagramElement, gen_gmfgraph_Compartment_DiagramElement, gen_gmfgraph_DiagramLabel_Node, gen_gmfgraph_GeneralFacet_VisualFacet, gen_gmfgraph_AlignmentFacet_VisualFacet, gen_gmfgraph_LabelOffsetFacet_VisualFacet, gen_gmfgraph_RGBColor_Color, gen_gmfgraph_ConstantColor_Color, gen_gmfgraph_GradientFacet_VisualFacet, gen_gmfgraph_LineBorder_Border, gen_gmfgraph_MarginBorder_Border, gen_gmfgraph_CompoundBorder_Border, gen_gmfgraph_CustomBorder_Border, gen_gmfgraph_CustomBorder_CustomClass, gen_gmfgraph_BasicFont_Font, gen_gmfgraph_CustomLayoutData_CustomClass, gen_gmfgraph_GridLayoutData_LayoutData, gen_gmfgraph_BorderLayoutData_LayoutData, gen_gmfgraph_Figure_Layoutable, gen_gmfgraph_CustomLayoutData_LayoutData, gen_gmfgraph_FigureRef_AbstractFigure, gen_gmfgraph_ConnectionFigure_RealFigure, gen_gmfgraph_DecorationFigure_RealFigure, gen_gmfgraph_Shape_RealFigure, gen_gmfgraph_Label_RealFigure, gen_gmfgraph_LabeledContainer_RealFigure, gen_gmfgraph_Rectangle_Shape, gen_gmfgraph_RoundedRectangle_Shape, gen_gmfgraph_Ellipse_Shape, gen_gmfgraph_Polyline_Shape, gen_gmfgraph_Polygon_Polyline, gen_gmfgraph_PolylineDecoration_Polyline, gen_gmfgraph_PolylineDecoration_DecorationFigure, gen_gmfgraph_PolygonDecoration_Polygon, gen_gmfgraph_PolygonDecoration_DecorationFigure, gen_gmfgraph_CustomFigure_CustomClass, gen_gmfgraph_CustomFigure_RealFigure, gen_gmfgraph_CustomDecoration_CustomFigure, gen_gmfgraph_CustomDecoration_DecorationFigure, gen_gmfgraph_CustomConnection_CustomFigure, gen_gmfgraph_CustomConnection_ConnectionFigure, gen_gmfgraph_CustomLayout_Layout, gen_gmfgraph_CustomLayout_CustomClass, gen_gmfgraph_GridLayout_Layout, gen_gmfgraph_BorderLayout_Layout, gen_gmfgraph_FlowLayout_Layout, gen_gmfgraph_XYLayout_Layout, gen_gmfgraph_PolylineConnection_Polyline, gen_gmfgraph_PolylineConnection_ConnectionFigure, gen_gmfgraph_StackLayout_Layout, gen_gmfgraph_ScalablePolygon_Polygon, gen_gmfgraph_DefaultSizeFacet_VisualFacet, gen_gmfgraph_AbstractNode_DiagramElement, gen_gmfgraph_RealFigure_AbstractFigure, gen_gmfgraph_AbstractFigure_Figure, gen_gmfgraph_FigureDescriptor_Identity, gen_gmfgraph_XYLayoutData_LayoutData},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)