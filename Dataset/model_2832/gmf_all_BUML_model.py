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
LabelTextAccessMethod: Enumeration = Enumeration(
    name="LabelTextAccessMethod",
    literals={
            EnumerationLiteral(name="MESSAGE_FORMAT"),
			EnumerationLiteral(name="NATIVE"),
			EnumerationLiteral(name="REGEXP"),
			EnumerationLiteral(name="PRINTF")
    }
)

Severity: Enumeration = Enumeration(
    name="Severity",
    literals={
            EnumerationLiteral(name="INFO"),
			EnumerationLiteral(name="WARNING"),
			EnumerationLiteral(name="ERROR")
    }
)

Language: Enumeration = Enumeration(
    name="Language",
    literals={
            EnumerationLiteral(name="ocl"),
			EnumerationLiteral(name="java"),
			EnumerationLiteral(name="regexp"),
			EnumerationLiteral(name="nregexp"),
			EnumerationLiteral(name="literal")
    }
)

StandardToolKind: Enumeration = Enumeration(
    name="StandardToolKind",
    literals={
            EnumerationLiteral(name="SELECT"),
			EnumerationLiteral(name="SELECT_PAN"),
			EnumerationLiteral(name="MARQUEE"),
			EnumerationLiteral(name="ZOOM_PAN"),
			EnumerationLiteral(name="ZOOM_IN"),
			EnumerationLiteral(name="ZOOM_OUT")
    }
)

ActionKind: Enumeration = Enumeration(
    name="ActionKind",
    literals={
            EnumerationLiteral(name="CREATE"),
			EnumerationLiteral(name="PROPCHANGE"),
			EnumerationLiteral(name="MODIFY"),
			EnumerationLiteral(name="PROCESS"),
			EnumerationLiteral(name="CUSTOM")
    }
)

AppearanceStyle: Enumeration = Enumeration(
    name="AppearanceStyle",
    literals={
            EnumerationLiteral(name="Font"),
			EnumerationLiteral(name="Fill"),
			EnumerationLiteral(name="Line")
    }
)

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

LineKind: Enumeration = Enumeration(
    name="LineKind",
    literals={
            EnumerationLiteral(name="LINE_SOLID"),
			EnumerationLiteral(name="LINE_CUSTOM"),
			EnumerationLiteral(name="LINE_DASH"),
			EnumerationLiteral(name="LINE_DOT"),
			EnumerationLiteral(name="LINE_DASHDOT"),
			EnumerationLiteral(name="LINE_DASHDOTDOT")
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
gmf_all_mappings_Mapping = Class(name="gmf::all::mappings::Mapping")
TopNodeReference = Class(name="TopNodeReference")
LinkMapping = Class(name="LinkMapping")
CanvasMapping = Class(name="CanvasMapping")
StyleSelector = Class(name="StyleSelector")
AuditContainer = Class(name="AuditContainer")
MetricContainer = Class(name="MetricContainer")
gmf_all_mappings_MappingEntry = Class(name="gmf::all::mappings::MappingEntry", is_abstract=True)
mappings_gmf_all_EClass = Class(name="mappings::gmf::all::EClass")
Constraint = Class(name="Constraint")
ElementInitializer = Class(name="ElementInitializer")
LabelMapping = Class(name="LabelMapping")
VisualEffectMapping = Class(name="VisualEffectMapping")
gmf_all_mappings_NodeReference = Class(name="gmf::all::mappings::NodeReference", is_abstract=True)
NeedsContainment = Class(name="NeedsContainment")
NodeMapping = Class(name="NodeMapping")
gmf_all_mappings_ChildReference = Class(name="gmf::all::mappings::ChildReference")
NodeReference = Class(name="NodeReference")
CompartmentMapping = Class(name="CompartmentMapping")
gmf_all_mappings_TopNodeReference = Class(name="gmf::all::mappings::TopNodeReference")
gmf_all_mappings_NodeMapping = Class(name="gmf::all::mappings::NodeMapping")
mappings_MappingEntry = Class(name="mappings::MappingEntry")
mappings_MenuOwner = Class(name="mappings::MenuOwner")
mappings_ToolOwner = Class(name="mappings::ToolOwner")
gmf_all_mappings_NeedsContainment = Class(name="gmf::all::mappings::NeedsContainment", is_abstract=True)
mappings_gmf_all_EReference = Class(name="mappings::gmf::all::EReference")
ChildReference = Class(name="ChildReference")
gmf_all_mappings_CompartmentMapping = Class(name="gmf::all::mappings::CompartmentMapping")
Compartment = Class(name="Compartment")
gmf_all_mappings_LinkMapping = Class(name="gmf::all::mappings::LinkMapping")
mappings_NeedsContainment = Class(name="mappings::NeedsContainment")
Connection = Class(name="Connection")
mappings_gmf_all_EStructuralFeature = Class(name="mappings::gmf::all::EStructuralFeature")
LinkConstraints = Class(name="LinkConstraints")
mappings_AppearanceSteward = Class(name="mappings::AppearanceSteward")
Node = Class(name="Node")
mappings_gmf_all_EPackage = Class(name="mappings::gmf::all::EPackage")
Palette = Class(name="Palette")
MainMenu = Class(name="MainMenu")
Toolbar = Class(name="Toolbar")
gmf_all_mappings_LabelMapping = Class(name="gmf::all::mappings::LabelMapping")
DiagramLabel = Class(name="DiagramLabel")
MappingEntry = Class(name="MappingEntry")
gmf_all_mappings_FeatureLabelMapping = Class(name="gmf::all::mappings::FeatureLabelMapping")
mappings_gmf_all_EAttribute = Class(name="mappings::gmf::all::EAttribute")
gmf_all_mappings_OclChoiceLabelMapping = Class(name="gmf::all::mappings::OclChoiceLabelMapping")
gmf_all_mappings_CanvasMapping = Class(name="gmf::all::mappings::CanvasMapping")
Canvas = Class(name="Canvas")
ValueExpression = Class(name="ValueExpression")
gmf_all_mappings_DesignLabelMapping = Class(name="gmf::all::mappings::DesignLabelMapping")
gmf_all_mappings_ExpressionLabelMapping = Class(name="gmf::all::mappings::ExpressionLabelMapping")
gmf_all_mappings_Constraint = Class(name="gmf::all::mappings::Constraint")
gmf_all_mappings_LinkConstraints = Class(name="gmf::all::mappings::LinkConstraints")
gmf_all_mappings_ValueExpression = Class(name="gmf::all::mappings::ValueExpression")
gmf_all_mappings_ElementInitializer = Class(name="gmf::all::mappings::ElementInitializer", is_abstract=True)
gmf_all_mappings_FeatureSeqInitializer = Class(name="gmf::all::mappings::FeatureSeqInitializer")
FeatureInitializer = Class(name="FeatureInitializer")
ReferenceNewElementSpec = Class(name="ReferenceNewElementSpec")
gmf_all_mappings_FeatureInitializer = Class(name="gmf::all::mappings::FeatureInitializer", is_abstract=True)
FeatureSeqInitializer = Class(name="FeatureSeqInitializer")
gmf_all_mappings_FeatureValueSpec = Class(name="gmf::all::mappings::FeatureValueSpec")
gmf_all_mappings_ReferenceNewElementSpec = Class(name="gmf::all::mappings::ReferenceNewElementSpec")
gmf_all_mappings_MenuOwner = Class(name="gmf::all::mappings::MenuOwner", is_abstract=True)
ContextMenu = Class(name="ContextMenu")
gmf_all_mappings_ToolOwner = Class(name="gmf::all::mappings::ToolOwner", is_abstract=True)
AbstractTool = Class(name="AbstractTool")
gmf_all_mappings_AppearanceSteward = Class(name="gmf::all::mappings::AppearanceSteward", is_abstract=True)
gmf_all_mappings_AuditContainer = Class(name="gmf::all::mappings::AuditContainer")
AuditRule = Class(name="AuditRule")
gmf_all_mappings_RuleBase = Class(name="gmf::all::mappings::RuleBase", is_abstract=True)
gmf_all_mappings_AuditRule = Class(name="gmf::all::mappings::AuditRule")
RuleBase = Class(name="RuleBase")
Auditable = Class(name="Auditable")
gmf_all_mappings_DomainElementTarget = Class(name="gmf::all::mappings::DomainElementTarget")
mappings_Auditable = Class(name="mappings::Auditable")
mappings_Measurable = Class(name="mappings::Measurable")
gmf_all_mappings_DomainAttributeTarget = Class(name="gmf::all::mappings::DomainAttributeTarget")
gmf_all_mappings_NotationElementTarget = Class(name="gmf::all::mappings::NotationElementTarget")
gmf_all_mappings_MetricContainer = Class(name="gmf::all::mappings::MetricContainer")
MetricRule = Class(name="MetricRule")
gmf_all_mappings_MetricRule = Class(name="gmf::all::mappings::MetricRule")
Measurable = Class(name="Measurable")
gmf_all_mappings_AuditedMetricTarget = Class(name="gmf::all::mappings::AuditedMetricTarget")
gmf_all_mappings_DiagramElementTarget = Class(name="gmf::all::mappings::DiagramElementTarget")
gmf_all_mappings_Auditable = Class(name="gmf::all::mappings::Auditable", is_abstract=True)
gmf_all_mappings_Measurable = Class(name="gmf::all::mappings::Measurable", is_abstract=True)
gmf_all_mappings_VisualEffectMapping = Class(name="gmf::all::mappings::VisualEffectMapping")
Pin = Class(name="Pin")
gmf_all_tooldef_ToolRegistry = Class(name="gmf::all::tooldef::ToolRegistry")
MenuAction = Class(name="MenuAction")
Menu = Class(name="Menu")
gmf_all_tooldef_AbstractTool = Class(name="gmf::all::tooldef::AbstractTool", is_abstract=True)
Image = Class(name="Image")
gmf_all_tooldef_ToolContainer = Class(name="gmf::all::tooldef::ToolContainer", is_abstract=True)
gmf_all_tooldef_Palette = Class(name="gmf::all::tooldef::Palette")
gmf_all_tooldef_StandardTool = Class(name="gmf::all::tooldef::StandardTool")
gmf_all_tooldef_CreationTool = Class(name="gmf::all::tooldef::CreationTool")
gmf_all_tooldef_GenericTool = Class(name="gmf::all::tooldef::GenericTool")
gmf_all_tooldef_ItemBase = Class(name="gmf::all::tooldef::ItemBase", is_abstract=True)
gmf_all_tooldef_Menu = Class(name="gmf::all::tooldef::Menu", is_abstract=True)
ItemBase = Class(name="ItemBase")
gmf_all_tooldef_Separator = Class(name="gmf::all::tooldef::Separator")
gmf_all_tooldef_PredefinedItem = Class(name="gmf::all::tooldef::PredefinedItem")
gmf_all_tooldef_PredefinedMenu = Class(name="gmf::all::tooldef::PredefinedMenu")
tooldef_Menu = Class(name="tooldef::Menu")
tooldef_PredefinedItem = Class(name="tooldef::PredefinedItem")
gmf_all_tooldef_ContributionItem = Class(name="gmf::all::tooldef::ContributionItem", is_abstract=True)
gmf_all_tooldef_MenuAction = Class(name="gmf::all::tooldef::MenuAction")
ContributionItem = Class(name="ContributionItem")
gmf_all_tooldef_ItemRef = Class(name="gmf::all::tooldef::ItemRef")
gmf_all_tooldef_ContextMenu = Class(name="gmf::all::tooldef::ContextMenu")
gmf_all_tooldef_PaletteSeparator = Class(name="gmf::all::tooldef::PaletteSeparator")
gmf_all_tooldef_ToolGroup = Class(name="gmf::all::tooldef::ToolGroup")
ToolContainer = Class(name="ToolContainer")
gmf_all_tooldef_MainMenu = Class(name="gmf::all::tooldef::MainMenu")
gmf_all_tooldef_Toolbar = Class(name="gmf::all::tooldef::Toolbar")
gmf_all_tooldef_Image = Class(name="gmf::all::tooldef::Image", is_abstract=True)
gmf_all_tooldef_DefaultImage = Class(name="gmf::all::tooldef::DefaultImage")
gmf_all_tooldef_BundleImage = Class(name="gmf::all::tooldef::BundleImage")
gmf_all_tooldef_StyleSelector = Class(name="gmf::all::tooldef::StyleSelector", is_abstract=True)
gmf_all_tooldef_GenericStyleSelector = Class(name="gmf::all::tooldef::GenericStyleSelector")
gmf_all_gmfgraph_Canvas = Class(name="gmf::all::gmfgraph::Canvas")
Identity = Class(name="Identity")
FigureGallery = Class(name="FigureGallery")
gmf_all_gmfgraph_FigureGallery = Class(name="gmf::all::gmfgraph::FigureGallery")
gmf_all_tooldef_PopupMenu = Class(name="gmf::all::tooldef::PopupMenu")
tooldef_ContributionItem = Class(name="tooldef::ContributionItem")
FigureDescriptor = Class(name="FigureDescriptor")
Border = Class(name="Border")
Layout = Class(name="Layout")
gmf_all_gmfgraph_Identity = Class(name="gmf::all::gmfgraph::Identity", is_abstract=True)
gmf_all_gmfgraph_DiagramElement = Class(name="gmf::all::gmfgraph::DiagramElement", is_abstract=True)
VisualFacet = Class(name="VisualFacet")
gmf_all_gmfgraph_AbstractNode = Class(name="gmf::all::gmfgraph::AbstractNode", is_abstract=True)
DiagramElement = Class(name="DiagramElement")
gmf_all_gmfgraph_Node = Class(name="gmf::all::gmfgraph::Node")
AbstractNode = Class(name="AbstractNode")
ChildAccess = Class(name="ChildAccess")
gmf_all_gmfgraph_Connection = Class(name="gmf::all::gmfgraph::Connection")
gmf_all_gmfgraph_Compartment = Class(name="gmf::all::gmfgraph::Compartment")
gmf_all_gmfgraph_DiagramLabel = Class(name="gmf::all::gmfgraph::DiagramLabel")
gmf_all_gmfgraph_VisualFacet = Class(name="gmf::all::gmfgraph::VisualFacet", is_abstract=True)
RealFigure = Class(name="RealFigure")
gmf_all_gmfgraph_AlignmentFacet = Class(name="gmf::all::gmfgraph::AlignmentFacet")
gmf_all_gmfgraph_GradientFacet = Class(name="gmf::all::gmfgraph::GradientFacet")
gmf_all_gmfgraph_LabelOffsetFacet = Class(name="gmf::all::gmfgraph::LabelOffsetFacet")
gmf_all_gmfgraph_DefaultSizeFacet = Class(name="gmf::all::gmfgraph::DefaultSizeFacet")
Dimension = Class(name="Dimension")
gmf_all_gmfgraph_Figure = Class(name="gmf::all::gmfgraph::Figure", is_abstract=True)
Layoutable = Class(name="Layoutable")
Color = Class(name="Color")
Font = Class(name="Font")
Insets = Class(name="Insets")
Point = Class(name="Point")
gmf_all_gmfgraph_GeneralFacet = Class(name="gmf::all::gmfgraph::GeneralFacet")
gmf_all_gmfgraph_ChildAccess = Class(name="gmf::all::gmfgraph::ChildAccess")
gmf_all_gmfgraph_RealFigure = Class(name="gmf::all::gmfgraph::RealFigure", is_abstract=True)
gmfgraph_AbstractFigure = Class(name="gmfgraph::AbstractFigure")
gmfgraph_PinOwner = Class(name="gmfgraph::PinOwner")
gmfgraph_CustomAttributeOwner = Class(name="gmfgraph::CustomAttributeOwner")
gmf_all_gmfgraph_FigureRef = Class(name="gmf::all::gmfgraph::FigureRef")
AbstractFigure = Class(name="AbstractFigure")
gmf_all_gmfgraph_ConnectionFigure = Class(name="gmf::all::gmfgraph::ConnectionFigure", is_abstract=True)
gmf_all_gmfgraph_DecorationFigure = Class(name="gmf::all::gmfgraph::DecorationFigure", is_abstract=True)
gmf_all_gmfgraph_Shape = Class(name="gmf::all::gmfgraph::Shape", is_abstract=True)
gmf_all_gmfgraph_AbstractFigure = Class(name="gmf::all::gmfgraph::AbstractFigure", is_abstract=True)
Figure = Class(name="Figure")
gmf_all_gmfgraph_FigureDescriptor = Class(name="gmf::all::gmfgraph::FigureDescriptor")
gmf_all_gmfgraph_LabeledContainer = Class(name="gmf::all::gmfgraph::LabeledContainer")
gmf_all_gmfgraph_VerticalLabel = Class(name="gmf::all::gmfgraph::VerticalLabel")
gmf_all_gmfgraph_Rectangle = Class(name="gmf::all::gmfgraph::Rectangle")
Shape = Class(name="Shape")
gmf_all_gmfgraph_InvisibleRectangle = Class(name="gmf::all::gmfgraph::InvisibleRectangle")
gmf_all_gmfgraph_RoundedRectangle = Class(name="gmf::all::gmfgraph::RoundedRectangle")
gmf_all_gmfgraph_Ellipse = Class(name="gmf::all::gmfgraph::Ellipse")
gmf_all_gmfgraph_Polyline = Class(name="gmf::all::gmfgraph::Polyline")
gmf_all_gmfgraph_Polygon = Class(name="gmf::all::gmfgraph::Polygon")
Polyline = Class(name="Polyline")
gmf_all_gmfgraph_ScalablePolygon = Class(name="gmf::all::gmfgraph::ScalablePolygon")
Polygon = Class(name="Polygon")
gmf_all_gmfgraph_PolylineConnection = Class(name="gmf::all::gmfgraph::PolylineConnection")
gmfgraph_Polyline = Class(name="gmfgraph::Polyline")
gmfgraph_ConnectionFigure = Class(name="gmfgraph::ConnectionFigure")
DecorationFigure = Class(name="DecorationFigure")
gmf_all_gmfgraph_PolylineDecoration = Class(name="gmf::all::gmfgraph::PolylineDecoration")
gmfgraph_DecorationFigure = Class(name="gmfgraph::DecorationFigure")
gmf_all_gmfgraph_PolygonDecoration = Class(name="gmf::all::gmfgraph::PolygonDecoration")
gmfgraph_Polygon = Class(name="gmfgraph::Polygon")
gmf_all_gmfgraph_Label = Class(name="gmf::all::gmfgraph::Label")
gmf_all_gmfgraph_CustomAttributeOwner = Class(name="gmf::all::gmfgraph::CustomAttributeOwner", is_abstract=True)
CustomAttribute = Class(name="CustomAttribute")
gmf_all_gmfgraph_CustomClass = Class(name="gmf::all::gmfgraph::CustomClass", is_abstract=True)
CustomAttributeOwner = Class(name="CustomAttributeOwner")
gmf_all_gmfgraph_CustomAttribute = Class(name="gmf::all::gmfgraph::CustomAttribute")
gmf_all_gmfgraph_FigureAccessor = Class(name="gmf::all::gmfgraph::FigureAccessor")
gmf_all_gmfgraph_CustomFigure = Class(name="gmf::all::gmfgraph::CustomFigure")
gmfgraph_RealFigure = Class(name="gmfgraph::RealFigure")
gmfgraph_CustomClass = Class(name="gmfgraph::CustomClass")
FigureAccessor = Class(name="FigureAccessor")
gmf_all_gmfgraph_Color = Class(name="gmf::all::gmfgraph::Color", is_abstract=True)
gmf_all_gmfgraph_RGBColor = Class(name="gmf::all::gmfgraph::RGBColor")
gmf_all_gmfgraph_ConstantColor = Class(name="gmf::all::gmfgraph::ConstantColor")
gmf_all_gmfgraph_Font = Class(name="gmf::all::gmfgraph::Font", is_abstract=True)
gmf_all_gmfgraph_BasicFont = Class(name="gmf::all::gmfgraph::BasicFont")
gmf_all_gmfgraph_Point = Class(name="gmf::all::gmfgraph::Point")
gmf_all_gmfgraph_Dimension = Class(name="gmf::all::gmfgraph::Dimension")
gmf_all_gmfgraph_Insets = Class(name="gmf::all::gmfgraph::Insets")
gmf_all_gmfgraph_CustomDecoration = Class(name="gmf::all::gmfgraph::CustomDecoration")
gmfgraph_CustomFigure = Class(name="gmfgraph::CustomFigure")
gmf_all_gmfgraph_CustomConnection = Class(name="gmf::all::gmfgraph::CustomConnection")
gmf_all_gmfgraph_LineBorder = Class(name="gmf::all::gmfgraph::LineBorder")
gmf_all_gmfgraph_Border = Class(name="gmf::all::gmfgraph::Border", is_abstract=True)
gmf_all_gmfgraph_BorderRef = Class(name="gmf::all::gmfgraph::BorderRef")
gmf_all_gmfgraph_CompoundBorder = Class(name="gmf::all::gmfgraph::CompoundBorder")
gmf_all_gmfgraph_CustomBorder = Class(name="gmf::all::gmfgraph::CustomBorder")
gmfgraph_Border = Class(name="gmfgraph::Border")
gmf_all_gmfgraph_MarginBorder = Class(name="gmf::all::gmfgraph::MarginBorder")
gmf_all_gmfgraph_LayoutData = Class(name="gmf::all::gmfgraph::LayoutData", is_abstract=True)
gmf_all_gmfgraph_CustomLayoutData = Class(name="gmf::all::gmfgraph::CustomLayoutData")
gmfgraph_LayoutData = Class(name="gmfgraph::LayoutData")
gmf_all_gmfgraph_GridLayoutData = Class(name="gmf::all::gmfgraph::GridLayoutData")
LayoutData = Class(name="LayoutData")
gmf_all_gmfgraph_BorderLayoutData = Class(name="gmf::all::gmfgraph::BorderLayoutData")
gmf_all_gmfgraph_Layoutable = Class(name="gmf::all::gmfgraph::Layoutable", is_abstract=True)
gmf_all_gmfgraph_Layout = Class(name="gmf::all::gmfgraph::Layout", is_abstract=True)
gmf_all_gmfgraph_LayoutRef = Class(name="gmf::all::gmfgraph::LayoutRef")
gmf_all_gmfgraph_GridLayout = Class(name="gmf::all::gmfgraph::GridLayout")
gmf_all_gmfgraph_BorderLayout = Class(name="gmf::all::gmfgraph::BorderLayout")
gmf_all_gmfgraph_CustomLayout = Class(name="gmf::all::gmfgraph::CustomLayout")
gmfgraph_Layout = Class(name="gmfgraph::Layout")
gmf_all_gmfgraph_XYLayout = Class(name="gmf::all::gmfgraph::XYLayout")
gmf_all_gmfgraph_XYLayoutData = Class(name="gmf::all::gmfgraph::XYLayoutData")
gmf_all_gmfgraph_StackLayout = Class(name="gmf::all::gmfgraph::StackLayout")
gmf_all_gmfgraph_CenterLayout = Class(name="gmf::all::gmfgraph::CenterLayout")
gmf_all_gmfgraph_SVGFigure = Class(name="gmf::all::gmfgraph::SVGFigure")
SVGProperty = Class(name="SVGProperty")
gmf_all_gmfgraph_FlowLayout = Class(name="gmf::all::gmfgraph::FlowLayout")
gmf_all_gmfgraph_SVGProperty = Class(name="gmf::all::gmfgraph::SVGProperty")
gmf_all_gmfgraph_Rectangle2D = Class(name="gmf::all::gmfgraph::Rectangle2D")
gmf_all_gmfgraph_Pin = Class(name="gmf::all::gmfgraph::Pin", is_abstract=True)
Rectangle2D = Class(name="Rectangle2D")
gmf_all_gmfgraph_ColorPin = Class(name="gmf::all::gmfgraph::ColorPin")
gmf_all_gmfgraph_VisiblePin = Class(name="gmf::all::gmfgraph::VisiblePin")
gmf_all_gmfgraph_PinOwner = Class(name="gmf::all::gmfgraph::PinOwner", is_abstract=True)
gmf_all_gmfgraph_CustomPin = Class(name="gmf::all::gmfgraph::CustomPin")

# gmf_all_mappings_Mapping class attributes and methods

# TopNodeReference class attributes and methods

# LinkMapping class attributes and methods

# CanvasMapping class attributes and methods

# StyleSelector class attributes and methods

# AuditContainer class attributes and methods

# MetricContainer class attributes and methods

# gmf_all_mappings_MappingEntry class attributes and methods
gmf_all_mappings_MappingEntry_m_getDomainContext: Method = Method(name="getDomainContext", parameters={}, type=StringType)
gmf_all_mappings_MappingEntry.methods={gmf_all_mappings_MappingEntry_m_getDomainContext}

# mappings_gmf_all_EClass class attributes and methods

# Constraint class attributes and methods

# ElementInitializer class attributes and methods

# LabelMapping class attributes and methods

# VisualEffectMapping class attributes and methods

# gmf_all_mappings_NodeReference class attributes and methods

# NeedsContainment class attributes and methods

# NodeMapping class attributes and methods

# gmf_all_mappings_ChildReference class attributes and methods

# NodeReference class attributes and methods

# CompartmentMapping class attributes and methods

# gmf_all_mappings_TopNodeReference class attributes and methods

# gmf_all_mappings_NodeMapping class attributes and methods

# mappings_MappingEntry class attributes and methods

# mappings_MenuOwner class attributes and methods

# mappings_ToolOwner class attributes and methods

# gmf_all_mappings_NeedsContainment class attributes and methods

# mappings_gmf_all_EReference class attributes and methods

# ChildReference class attributes and methods

# gmf_all_mappings_CompartmentMapping class attributes and methods

# Compartment class attributes and methods

# gmf_all_mappings_LinkMapping class attributes and methods

# mappings_NeedsContainment class attributes and methods

# Connection class attributes and methods

# mappings_gmf_all_EStructuralFeature class attributes and methods

# LinkConstraints class attributes and methods

# mappings_AppearanceSteward class attributes and methods

# Node class attributes and methods

# mappings_gmf_all_EPackage class attributes and methods

# Palette class attributes and methods

# MainMenu class attributes and methods

# Toolbar class attributes and methods

# gmf_all_mappings_LabelMapping class attributes and methods
gmf_all_mappings_LabelMapping_readOnly: Property = Property(name="readOnly", type=BooleanType)
gmf_all_mappings_LabelMapping.attributes={gmf_all_mappings_LabelMapping_readOnly}

# DiagramLabel class attributes and methods

# MappingEntry class attributes and methods

# gmf_all_mappings_FeatureLabelMapping class attributes and methods
gmf_all_mappings_FeatureLabelMapping_viewPattern: Property = Property(name="viewPattern", type=StringType)
gmf_all_mappings_FeatureLabelMapping_editorPattern: Property = Property(name="editorPattern", type=StringType)
gmf_all_mappings_FeatureLabelMapping_editPattern: Property = Property(name="editPattern", type=StringType)
gmf_all_mappings_FeatureLabelMapping_viewMethod: Property = Property(name="viewMethod", type=StringType)
gmf_all_mappings_FeatureLabelMapping_editMethod: Property = Property(name="editMethod", type=StringType)
gmf_all_mappings_FeatureLabelMapping.attributes={gmf_all_mappings_FeatureLabelMapping_editMethod, gmf_all_mappings_FeatureLabelMapping_editPattern, gmf_all_mappings_FeatureLabelMapping_viewPattern, gmf_all_mappings_FeatureLabelMapping_editorPattern, gmf_all_mappings_FeatureLabelMapping_viewMethod}

# mappings_gmf_all_EAttribute class attributes and methods

# gmf_all_mappings_OclChoiceLabelMapping class attributes and methods

# gmf_all_mappings_CanvasMapping class attributes and methods

# Canvas class attributes and methods

# ValueExpression class attributes and methods

# gmf_all_mappings_DesignLabelMapping class attributes and methods

# gmf_all_mappings_ExpressionLabelMapping class attributes and methods

# gmf_all_mappings_Constraint class attributes and methods

# gmf_all_mappings_LinkConstraints class attributes and methods

# gmf_all_mappings_ValueExpression class attributes and methods
gmf_all_mappings_ValueExpression_body: Property = Property(name="body", type=StringType)
gmf_all_mappings_ValueExpression_language: Property = Property(name="language", type=StringType)
gmf_all_mappings_ValueExpression_langName: Property = Property(name="langName", type=StringType)
gmf_all_mappings_ValueExpression.attributes={gmf_all_mappings_ValueExpression_body, gmf_all_mappings_ValueExpression_language, gmf_all_mappings_ValueExpression_langName}

# gmf_all_mappings_ElementInitializer class attributes and methods

# gmf_all_mappings_FeatureSeqInitializer class attributes and methods

# FeatureInitializer class attributes and methods

# ReferenceNewElementSpec class attributes and methods

# gmf_all_mappings_FeatureInitializer class attributes and methods

# FeatureSeqInitializer class attributes and methods

# gmf_all_mappings_FeatureValueSpec class attributes and methods

# gmf_all_mappings_ReferenceNewElementSpec class attributes and methods

# gmf_all_mappings_MenuOwner class attributes and methods

# ContextMenu class attributes and methods

# gmf_all_mappings_ToolOwner class attributes and methods

# AbstractTool class attributes and methods

# gmf_all_mappings_AppearanceSteward class attributes and methods

# gmf_all_mappings_AuditContainer class attributes and methods
gmf_all_mappings_AuditContainer_id: Property = Property(name="id", type=StringType)
gmf_all_mappings_AuditContainer_name: Property = Property(name="name", type=StringType)
gmf_all_mappings_AuditContainer_description: Property = Property(name="description", type=StringType)
gmf_all_mappings_AuditContainer.attributes={gmf_all_mappings_AuditContainer_name, gmf_all_mappings_AuditContainer_description, gmf_all_mappings_AuditContainer_id}

# AuditRule class attributes and methods

# gmf_all_mappings_RuleBase class attributes and methods
gmf_all_mappings_RuleBase_name: Property = Property(name="name", type=StringType)
gmf_all_mappings_RuleBase_description: Property = Property(name="description", type=StringType)
gmf_all_mappings_RuleBase.attributes={gmf_all_mappings_RuleBase_name, gmf_all_mappings_RuleBase_description}

# gmf_all_mappings_AuditRule class attributes and methods
gmf_all_mappings_AuditRule_id: Property = Property(name="id", type=StringType)
gmf_all_mappings_AuditRule_severity: Property = Property(name="severity", type=StringType)
gmf_all_mappings_AuditRule_useInLiveMode: Property = Property(name="useInLiveMode", type=BooleanType)
gmf_all_mappings_AuditRule_message: Property = Property(name="message", type=StringType)
gmf_all_mappings_AuditRule.attributes={gmf_all_mappings_AuditRule_id, gmf_all_mappings_AuditRule_useInLiveMode, gmf_all_mappings_AuditRule_message, gmf_all_mappings_AuditRule_severity}

# RuleBase class attributes and methods

# Auditable class attributes and methods

# gmf_all_mappings_DomainElementTarget class attributes and methods

# mappings_Auditable class attributes and methods

# mappings_Measurable class attributes and methods

# gmf_all_mappings_DomainAttributeTarget class attributes and methods
gmf_all_mappings_DomainAttributeTarget_nullAsError: Property = Property(name="nullAsError", type=BooleanType)
gmf_all_mappings_DomainAttributeTarget.attributes={gmf_all_mappings_DomainAttributeTarget_nullAsError}

# gmf_all_mappings_NotationElementTarget class attributes and methods

# gmf_all_mappings_MetricContainer class attributes and methods

# MetricRule class attributes and methods

# gmf_all_mappings_MetricRule class attributes and methods
gmf_all_mappings_MetricRule_key: Property = Property(name="key", type=StringType)
gmf_all_mappings_MetricRule_lowLimit: Property = Property(name="lowLimit", type=StringType)
gmf_all_mappings_MetricRule_highLimit: Property = Property(name="highLimit", type=StringType)
gmf_all_mappings_MetricRule.attributes={gmf_all_mappings_MetricRule_key, gmf_all_mappings_MetricRule_lowLimit, gmf_all_mappings_MetricRule_highLimit}

# Measurable class attributes and methods

# gmf_all_mappings_AuditedMetricTarget class attributes and methods

# gmf_all_mappings_DiagramElementTarget class attributes and methods

# gmf_all_mappings_Auditable class attributes and methods

# gmf_all_mappings_Measurable class attributes and methods

# gmf_all_mappings_VisualEffectMapping class attributes and methods
gmf_all_mappings_VisualEffectMapping_oclExpression: Property = Property(name="oclExpression", type=StringType)
gmf_all_mappings_VisualEffectMapping.attributes={gmf_all_mappings_VisualEffectMapping_oclExpression}

# Pin class attributes and methods

# gmf_all_tooldef_ToolRegistry class attributes and methods

# MenuAction class attributes and methods

# Menu class attributes and methods

# gmf_all_tooldef_AbstractTool class attributes and methods
gmf_all_tooldef_AbstractTool_title: Property = Property(name="title", type=StringType)
gmf_all_tooldef_AbstractTool_description: Property = Property(name="description", type=StringType)
gmf_all_tooldef_AbstractTool.attributes={gmf_all_tooldef_AbstractTool_title, gmf_all_tooldef_AbstractTool_description}

# Image class attributes and methods

# gmf_all_tooldef_ToolContainer class attributes and methods

# gmf_all_tooldef_Palette class attributes and methods

# gmf_all_tooldef_StandardTool class attributes and methods
gmf_all_tooldef_StandardTool_toolKind: Property = Property(name="toolKind", type=StringType)
gmf_all_tooldef_StandardTool.attributes={gmf_all_tooldef_StandardTool_toolKind}

# gmf_all_tooldef_CreationTool class attributes and methods

# gmf_all_tooldef_GenericTool class attributes and methods
gmf_all_tooldef_GenericTool_toolClass: Property = Property(name="toolClass", type=StringType)
gmf_all_tooldef_GenericTool.attributes={gmf_all_tooldef_GenericTool_toolClass}

# gmf_all_tooldef_ItemBase class attributes and methods

# gmf_all_tooldef_Menu class attributes and methods

# ItemBase class attributes and methods

# gmf_all_tooldef_Separator class attributes and methods
gmf_all_tooldef_Separator_name: Property = Property(name="name", type=StringType)
gmf_all_tooldef_Separator.attributes={gmf_all_tooldef_Separator_name}

# gmf_all_tooldef_PredefinedItem class attributes and methods
gmf_all_tooldef_PredefinedItem_identifier: Property = Property(name="identifier", type=StringType)
gmf_all_tooldef_PredefinedItem.attributes={gmf_all_tooldef_PredefinedItem_identifier}

# gmf_all_tooldef_PredefinedMenu class attributes and methods

# tooldef_Menu class attributes and methods

# tooldef_PredefinedItem class attributes and methods

# gmf_all_tooldef_ContributionItem class attributes and methods
gmf_all_tooldef_ContributionItem_title: Property = Property(name="title", type=StringType)
gmf_all_tooldef_ContributionItem.attributes={gmf_all_tooldef_ContributionItem_title}

# gmf_all_tooldef_MenuAction class attributes and methods
gmf_all_tooldef_MenuAction_kind: Property = Property(name="kind", type=StringType)
gmf_all_tooldef_MenuAction_hotKey: Property = Property(name="hotKey", type=StringType)
gmf_all_tooldef_MenuAction.attributes={gmf_all_tooldef_MenuAction_hotKey, gmf_all_tooldef_MenuAction_kind}

# ContributionItem class attributes and methods

# gmf_all_tooldef_ItemRef class attributes and methods

# gmf_all_tooldef_ContextMenu class attributes and methods

# gmf_all_tooldef_PaletteSeparator class attributes and methods

# gmf_all_tooldef_ToolGroup class attributes and methods
gmf_all_tooldef_ToolGroup_collapsible: Property = Property(name="collapsible", type=BooleanType)
gmf_all_tooldef_ToolGroup_stack: Property = Property(name="stack", type=BooleanType)
gmf_all_tooldef_ToolGroup.attributes={gmf_all_tooldef_ToolGroup_collapsible, gmf_all_tooldef_ToolGroup_stack}

# ToolContainer class attributes and methods

# gmf_all_tooldef_MainMenu class attributes and methods
gmf_all_tooldef_MainMenu_title: Property = Property(name="title", type=StringType)
gmf_all_tooldef_MainMenu.attributes={gmf_all_tooldef_MainMenu_title}

# gmf_all_tooldef_Toolbar class attributes and methods

# gmf_all_tooldef_Image class attributes and methods

# gmf_all_tooldef_DefaultImage class attributes and methods

# gmf_all_tooldef_BundleImage class attributes and methods
gmf_all_tooldef_BundleImage_path: Property = Property(name="path", type=StringType)
gmf_all_tooldef_BundleImage_bundle: Property = Property(name="bundle", type=StringType)
gmf_all_tooldef_BundleImage.attributes={gmf_all_tooldef_BundleImage_bundle, gmf_all_tooldef_BundleImage_path}

# gmf_all_tooldef_StyleSelector class attributes and methods
gmf_all_tooldef_StyleSelector_m_isOk: Method = Method(name="isOk", parameters={Parameter(name='style')}, type=BooleanType)
gmf_all_tooldef_StyleSelector.methods={gmf_all_tooldef_StyleSelector_m_isOk}

# gmf_all_tooldef_GenericStyleSelector class attributes and methods
gmf_all_tooldef_GenericStyleSelector_values: Property = Property(name="values", type=StringType)
gmf_all_tooldef_GenericStyleSelector.attributes={gmf_all_tooldef_GenericStyleSelector_values}

# gmf_all_gmfgraph_Canvas class attributes and methods

# Identity class attributes and methods

# FigureGallery class attributes and methods

# gmf_all_gmfgraph_FigureGallery class attributes and methods
gmf_all_gmfgraph_FigureGallery_implementationBundle: Property = Property(name="implementationBundle", type=StringType)
gmf_all_gmfgraph_FigureGallery.attributes={gmf_all_gmfgraph_FigureGallery_implementationBundle}

# gmf_all_tooldef_PopupMenu class attributes and methods
gmf_all_tooldef_PopupMenu_iD: Property = Property(name="iD", type=StringType)
gmf_all_tooldef_PopupMenu.attributes={gmf_all_tooldef_PopupMenu_iD}

# tooldef_ContributionItem class attributes and methods

# FigureDescriptor class attributes and methods

# Border class attributes and methods

# Layout class attributes and methods

# gmf_all_gmfgraph_Identity class attributes and methods
gmf_all_gmfgraph_Identity_name: Property = Property(name="name", type=StringType)
gmf_all_gmfgraph_Identity.attributes={gmf_all_gmfgraph_Identity_name}

# gmf_all_gmfgraph_DiagramElement class attributes and methods

# VisualFacet class attributes and methods

# gmf_all_gmfgraph_AbstractNode class attributes and methods

# DiagramElement class attributes and methods

# gmf_all_gmfgraph_Node class attributes and methods
gmf_all_gmfgraph_Node_resizeConstraint: Property = Property(name="resizeConstraint", type=StringType)
gmf_all_gmfgraph_Node_affixedParentSide: Property = Property(name="affixedParentSide", type=StringType)
gmf_all_gmfgraph_Node.attributes={gmf_all_gmfgraph_Node_affixedParentSide, gmf_all_gmfgraph_Node_resizeConstraint}

# AbstractNode class attributes and methods

# ChildAccess class attributes and methods

# gmf_all_gmfgraph_Connection class attributes and methods

# gmf_all_gmfgraph_Compartment class attributes and methods
gmf_all_gmfgraph_Compartment_collapsible: Property = Property(name="collapsible", type=BooleanType)
gmf_all_gmfgraph_Compartment_needsTitle: Property = Property(name="needsTitle", type=BooleanType)
gmf_all_gmfgraph_Compartment.attributes={gmf_all_gmfgraph_Compartment_collapsible, gmf_all_gmfgraph_Compartment_needsTitle}

# gmf_all_gmfgraph_DiagramLabel class attributes and methods
gmf_all_gmfgraph_DiagramLabel_elementIcon: Property = Property(name="elementIcon", type=BooleanType)
gmf_all_gmfgraph_DiagramLabel_external: Property = Property(name="external", type=BooleanType)
gmf_all_gmfgraph_DiagramLabel.attributes={gmf_all_gmfgraph_DiagramLabel_external, gmf_all_gmfgraph_DiagramLabel_elementIcon}

# gmf_all_gmfgraph_VisualFacet class attributes and methods

# RealFigure class attributes and methods

# gmf_all_gmfgraph_AlignmentFacet class attributes and methods
gmf_all_gmfgraph_AlignmentFacet_alignment: Property = Property(name="alignment", type=StringType)
gmf_all_gmfgraph_AlignmentFacet.attributes={gmf_all_gmfgraph_AlignmentFacet_alignment}

# gmf_all_gmfgraph_GradientFacet class attributes and methods
gmf_all_gmfgraph_GradientFacet_direction: Property = Property(name="direction", type=StringType)
gmf_all_gmfgraph_GradientFacet.attributes={gmf_all_gmfgraph_GradientFacet_direction}

# gmf_all_gmfgraph_LabelOffsetFacet class attributes and methods
gmf_all_gmfgraph_LabelOffsetFacet_x: Property = Property(name="x", type=IntegerType)
gmf_all_gmfgraph_LabelOffsetFacet_y: Property = Property(name="y", type=IntegerType)
gmf_all_gmfgraph_LabelOffsetFacet.attributes={gmf_all_gmfgraph_LabelOffsetFacet_y, gmf_all_gmfgraph_LabelOffsetFacet_x}

# gmf_all_gmfgraph_DefaultSizeFacet class attributes and methods

# Dimension class attributes and methods

# gmf_all_gmfgraph_Figure class attributes and methods

# Layoutable class attributes and methods

# Color class attributes and methods

# Font class attributes and methods

# Insets class attributes and methods

# Point class attributes and methods

# gmf_all_gmfgraph_GeneralFacet class attributes and methods
gmf_all_gmfgraph_GeneralFacet_data: Property = Property(name="data", type=StringType)
gmf_all_gmfgraph_GeneralFacet_identifier: Property = Property(name="identifier", type=StringType)
gmf_all_gmfgraph_GeneralFacet.attributes={gmf_all_gmfgraph_GeneralFacet_identifier, gmf_all_gmfgraph_GeneralFacet_data}

# gmf_all_gmfgraph_ChildAccess class attributes and methods
gmf_all_gmfgraph_ChildAccess_accessor: Property = Property(name="accessor", type=StringType)
gmf_all_gmfgraph_ChildAccess.attributes={gmf_all_gmfgraph_ChildAccess_accessor}

# gmf_all_gmfgraph_RealFigure class attributes and methods
gmf_all_gmfgraph_RealFigure_name: Property = Property(name="name", type=StringType)
gmf_all_gmfgraph_RealFigure.attributes={gmf_all_gmfgraph_RealFigure_name}

# gmfgraph_AbstractFigure class attributes and methods

# gmfgraph_PinOwner class attributes and methods

# gmfgraph_CustomAttributeOwner class attributes and methods

# gmf_all_gmfgraph_FigureRef class attributes and methods

# AbstractFigure class attributes and methods

# gmf_all_gmfgraph_ConnectionFigure class attributes and methods

# gmf_all_gmfgraph_DecorationFigure class attributes and methods

# gmf_all_gmfgraph_Shape class attributes and methods
gmf_all_gmfgraph_Shape_outline: Property = Property(name="outline", type=BooleanType)
gmf_all_gmfgraph_Shape_fill: Property = Property(name="fill", type=BooleanType)
gmf_all_gmfgraph_Shape_lineWidth: Property = Property(name="lineWidth", type=IntegerType)
gmf_all_gmfgraph_Shape_lineKind: Property = Property(name="lineKind", type=StringType)
gmf_all_gmfgraph_Shape_xorFill: Property = Property(name="xorFill", type=BooleanType)
gmf_all_gmfgraph_Shape_xorOutline: Property = Property(name="xorOutline", type=BooleanType)
gmf_all_gmfgraph_Shape.attributes={gmf_all_gmfgraph_Shape_lineKind, gmf_all_gmfgraph_Shape_lineWidth, gmf_all_gmfgraph_Shape_outline, gmf_all_gmfgraph_Shape_xorOutline, gmf_all_gmfgraph_Shape_xorFill, gmf_all_gmfgraph_Shape_fill}

# gmf_all_gmfgraph_AbstractFigure class attributes and methods

# Figure class attributes and methods

# gmf_all_gmfgraph_FigureDescriptor class attributes and methods

# gmf_all_gmfgraph_LabeledContainer class attributes and methods

# gmf_all_gmfgraph_VerticalLabel class attributes and methods
gmf_all_gmfgraph_VerticalLabel_text: Property = Property(name="text", type=StringType)
gmf_all_gmfgraph_VerticalLabel.attributes={gmf_all_gmfgraph_VerticalLabel_text}

# gmf_all_gmfgraph_Rectangle class attributes and methods

# Shape class attributes and methods

# gmf_all_gmfgraph_InvisibleRectangle class attributes and methods

# gmf_all_gmfgraph_RoundedRectangle class attributes and methods
gmf_all_gmfgraph_RoundedRectangle_cornerWidth: Property = Property(name="cornerWidth", type=IntegerType)
gmf_all_gmfgraph_RoundedRectangle_cornerHeight: Property = Property(name="cornerHeight", type=IntegerType)
gmf_all_gmfgraph_RoundedRectangle.attributes={gmf_all_gmfgraph_RoundedRectangle_cornerHeight, gmf_all_gmfgraph_RoundedRectangle_cornerWidth}

# gmf_all_gmfgraph_Ellipse class attributes and methods

# gmf_all_gmfgraph_Polyline class attributes and methods

# gmf_all_gmfgraph_Polygon class attributes and methods

# Polyline class attributes and methods

# gmf_all_gmfgraph_ScalablePolygon class attributes and methods

# Polygon class attributes and methods

# gmf_all_gmfgraph_PolylineConnection class attributes and methods

# gmfgraph_Polyline class attributes and methods

# gmfgraph_ConnectionFigure class attributes and methods

# DecorationFigure class attributes and methods

# gmf_all_gmfgraph_PolylineDecoration class attributes and methods

# gmfgraph_DecorationFigure class attributes and methods

# gmf_all_gmfgraph_PolygonDecoration class attributes and methods

# gmfgraph_Polygon class attributes and methods

# gmf_all_gmfgraph_Label class attributes and methods
gmf_all_gmfgraph_Label_text: Property = Property(name="text", type=StringType)
gmf_all_gmfgraph_Label.attributes={gmf_all_gmfgraph_Label_text}

# gmf_all_gmfgraph_CustomAttributeOwner class attributes and methods

# CustomAttribute class attributes and methods

# gmf_all_gmfgraph_CustomClass class attributes and methods
gmf_all_gmfgraph_CustomClass_qualifiedClassName: Property = Property(name="qualifiedClassName", type=StringType)
gmf_all_gmfgraph_CustomClass.attributes={gmf_all_gmfgraph_CustomClass_qualifiedClassName}

# CustomAttributeOwner class attributes and methods

# gmf_all_gmfgraph_CustomAttribute class attributes and methods
gmf_all_gmfgraph_CustomAttribute_name: Property = Property(name="name", type=StringType)
gmf_all_gmfgraph_CustomAttribute_value: Property = Property(name="value", type=StringType)
gmf_all_gmfgraph_CustomAttribute_directAccess: Property = Property(name="directAccess", type=BooleanType)
gmf_all_gmfgraph_CustomAttribute_multiStatementValue: Property = Property(name="multiStatementValue", type=BooleanType)
gmf_all_gmfgraph_CustomAttribute.attributes={gmf_all_gmfgraph_CustomAttribute_directAccess, gmf_all_gmfgraph_CustomAttribute_multiStatementValue, gmf_all_gmfgraph_CustomAttribute_value, gmf_all_gmfgraph_CustomAttribute_name}

# gmf_all_gmfgraph_FigureAccessor class attributes and methods
gmf_all_gmfgraph_FigureAccessor_accessor: Property = Property(name="accessor", type=StringType)
gmf_all_gmfgraph_FigureAccessor.attributes={gmf_all_gmfgraph_FigureAccessor_accessor}

# gmf_all_gmfgraph_CustomFigure class attributes and methods

# gmfgraph_RealFigure class attributes and methods

# gmfgraph_CustomClass class attributes and methods

# FigureAccessor class attributes and methods

# gmf_all_gmfgraph_Color class attributes and methods

# gmf_all_gmfgraph_RGBColor class attributes and methods
gmf_all_gmfgraph_RGBColor_red: Property = Property(name="red", type=IntegerType)
gmf_all_gmfgraph_RGBColor_green: Property = Property(name="green", type=IntegerType)
gmf_all_gmfgraph_RGBColor_blue: Property = Property(name="blue", type=IntegerType)
gmf_all_gmfgraph_RGBColor.attributes={gmf_all_gmfgraph_RGBColor_green, gmf_all_gmfgraph_RGBColor_red, gmf_all_gmfgraph_RGBColor_blue}

# gmf_all_gmfgraph_ConstantColor class attributes and methods
gmf_all_gmfgraph_ConstantColor_value: Property = Property(name="value", type=StringType)
gmf_all_gmfgraph_ConstantColor.attributes={gmf_all_gmfgraph_ConstantColor_value}

# gmf_all_gmfgraph_Font class attributes and methods

# gmf_all_gmfgraph_BasicFont class attributes and methods
gmf_all_gmfgraph_BasicFont_faceName: Property = Property(name="faceName", type=StringType)
gmf_all_gmfgraph_BasicFont_height: Property = Property(name="height", type=IntegerType)
gmf_all_gmfgraph_BasicFont_style: Property = Property(name="style", type=StringType)
gmf_all_gmfgraph_BasicFont.attributes={gmf_all_gmfgraph_BasicFont_style, gmf_all_gmfgraph_BasicFont_height, gmf_all_gmfgraph_BasicFont_faceName}

# gmf_all_gmfgraph_Point class attributes and methods
gmf_all_gmfgraph_Point_x: Property = Property(name="x", type=IntegerType)
gmf_all_gmfgraph_Point_y: Property = Property(name="y", type=IntegerType)
gmf_all_gmfgraph_Point.attributes={gmf_all_gmfgraph_Point_x, gmf_all_gmfgraph_Point_y}

# gmf_all_gmfgraph_Dimension class attributes and methods
gmf_all_gmfgraph_Dimension_dx: Property = Property(name="dx", type=IntegerType)
gmf_all_gmfgraph_Dimension_dy: Property = Property(name="dy", type=IntegerType)
gmf_all_gmfgraph_Dimension.attributes={gmf_all_gmfgraph_Dimension_dx, gmf_all_gmfgraph_Dimension_dy}

# gmf_all_gmfgraph_Insets class attributes and methods
gmf_all_gmfgraph_Insets_top: Property = Property(name="top", type=IntegerType)
gmf_all_gmfgraph_Insets_left: Property = Property(name="left", type=IntegerType)
gmf_all_gmfgraph_Insets_bottom: Property = Property(name="bottom", type=IntegerType)
gmf_all_gmfgraph_Insets_right: Property = Property(name="right", type=IntegerType)
gmf_all_gmfgraph_Insets.attributes={gmf_all_gmfgraph_Insets_left, gmf_all_gmfgraph_Insets_bottom, gmf_all_gmfgraph_Insets_right, gmf_all_gmfgraph_Insets_top}

# gmf_all_gmfgraph_CustomDecoration class attributes and methods

# gmfgraph_CustomFigure class attributes and methods

# gmf_all_gmfgraph_CustomConnection class attributes and methods

# gmf_all_gmfgraph_LineBorder class attributes and methods
gmf_all_gmfgraph_LineBorder_width: Property = Property(name="width", type=IntegerType)
gmf_all_gmfgraph_LineBorder.attributes={gmf_all_gmfgraph_LineBorder_width}

# gmf_all_gmfgraph_Border class attributes and methods

# gmf_all_gmfgraph_BorderRef class attributes and methods

# gmf_all_gmfgraph_CompoundBorder class attributes and methods

# gmf_all_gmfgraph_CustomBorder class attributes and methods

# gmfgraph_Border class attributes and methods

# gmf_all_gmfgraph_MarginBorder class attributes and methods

# gmf_all_gmfgraph_LayoutData class attributes and methods

# gmf_all_gmfgraph_CustomLayoutData class attributes and methods

# gmfgraph_LayoutData class attributes and methods

# gmf_all_gmfgraph_GridLayoutData class attributes and methods
gmf_all_gmfgraph_GridLayoutData_grabExcessHorizontalSpace: Property = Property(name="grabExcessHorizontalSpace", type=BooleanType)
gmf_all_gmfgraph_GridLayoutData_grabExcessVerticalSpace: Property = Property(name="grabExcessVerticalSpace", type=BooleanType)
gmf_all_gmfgraph_GridLayoutData_verticalSpan: Property = Property(name="verticalSpan", type=IntegerType)
gmf_all_gmfgraph_GridLayoutData_horizontalSpan: Property = Property(name="horizontalSpan", type=IntegerType)
gmf_all_gmfgraph_GridLayoutData_horizontalIndent: Property = Property(name="horizontalIndent", type=IntegerType)
gmf_all_gmfgraph_GridLayoutData_verticalAlignment: Property = Property(name="verticalAlignment", type=StringType)
gmf_all_gmfgraph_GridLayoutData_horizontalAlignment: Property = Property(name="horizontalAlignment", type=StringType)
gmf_all_gmfgraph_GridLayoutData.attributes={gmf_all_gmfgraph_GridLayoutData_grabExcessHorizontalSpace, gmf_all_gmfgraph_GridLayoutData_grabExcessVerticalSpace, gmf_all_gmfgraph_GridLayoutData_verticalAlignment, gmf_all_gmfgraph_GridLayoutData_horizontalAlignment, gmf_all_gmfgraph_GridLayoutData_verticalSpan, gmf_all_gmfgraph_GridLayoutData_horizontalIndent, gmf_all_gmfgraph_GridLayoutData_horizontalSpan}

# LayoutData class attributes and methods

# gmf_all_gmfgraph_BorderLayoutData class attributes and methods
gmf_all_gmfgraph_BorderLayoutData_alignment: Property = Property(name="alignment", type=StringType)
gmf_all_gmfgraph_BorderLayoutData_vertical: Property = Property(name="vertical", type=BooleanType)
gmf_all_gmfgraph_BorderLayoutData.attributes={gmf_all_gmfgraph_BorderLayoutData_vertical, gmf_all_gmfgraph_BorderLayoutData_alignment}

# gmf_all_gmfgraph_Layoutable class attributes and methods

# gmf_all_gmfgraph_Layout class attributes and methods

# gmf_all_gmfgraph_LayoutRef class attributes and methods

# gmf_all_gmfgraph_GridLayout class attributes and methods
gmf_all_gmfgraph_GridLayout_numColumns: Property = Property(name="numColumns", type=IntegerType)
gmf_all_gmfgraph_GridLayout_equalWidth: Property = Property(name="equalWidth", type=BooleanType)
gmf_all_gmfgraph_GridLayout.attributes={gmf_all_gmfgraph_GridLayout_numColumns, gmf_all_gmfgraph_GridLayout_equalWidth}

# gmf_all_gmfgraph_BorderLayout class attributes and methods

# gmf_all_gmfgraph_CustomLayout class attributes and methods

# gmfgraph_Layout class attributes and methods

# gmf_all_gmfgraph_XYLayout class attributes and methods

# gmf_all_gmfgraph_XYLayoutData class attributes and methods

# gmf_all_gmfgraph_StackLayout class attributes and methods

# gmf_all_gmfgraph_CenterLayout class attributes and methods

# gmf_all_gmfgraph_SVGFigure class attributes and methods
gmf_all_gmfgraph_SVGFigure_documentURI: Property = Property(name="documentURI", type=StringType)
gmf_all_gmfgraph_SVGFigure_noCanvasWidth: Property = Property(name="noCanvasWidth", type=BooleanType)
gmf_all_gmfgraph_SVGFigure_noCanvasHeight: Property = Property(name="noCanvasHeight", type=BooleanType)
gmf_all_gmfgraph_SVGFigure.attributes={gmf_all_gmfgraph_SVGFigure_noCanvasHeight, gmf_all_gmfgraph_SVGFigure_noCanvasWidth, gmf_all_gmfgraph_SVGFigure_documentURI}

# SVGProperty class attributes and methods

# gmf_all_gmfgraph_FlowLayout class attributes and methods
gmf_all_gmfgraph_FlowLayout_forceSingleLine: Property = Property(name="forceSingleLine", type=BooleanType)
gmf_all_gmfgraph_FlowLayout_majorAlignment: Property = Property(name="majorAlignment", type=StringType)
gmf_all_gmfgraph_FlowLayout_minorAlignment: Property = Property(name="minorAlignment", type=StringType)
gmf_all_gmfgraph_FlowLayout_majorSpacing: Property = Property(name="majorSpacing", type=IntegerType)
gmf_all_gmfgraph_FlowLayout_minorSpacing: Property = Property(name="minorSpacing", type=IntegerType)
gmf_all_gmfgraph_FlowLayout_vertical: Property = Property(name="vertical", type=BooleanType)
gmf_all_gmfgraph_FlowLayout_matchMinorSize: Property = Property(name="matchMinorSize", type=BooleanType)
gmf_all_gmfgraph_FlowLayout.attributes={gmf_all_gmfgraph_FlowLayout_minorAlignment, gmf_all_gmfgraph_FlowLayout_majorSpacing, gmf_all_gmfgraph_FlowLayout_forceSingleLine, gmf_all_gmfgraph_FlowLayout_majorAlignment, gmf_all_gmfgraph_FlowLayout_minorSpacing, gmf_all_gmfgraph_FlowLayout_matchMinorSize, gmf_all_gmfgraph_FlowLayout_vertical}

# gmf_all_gmfgraph_SVGProperty class attributes and methods
gmf_all_gmfgraph_SVGProperty_query: Property = Property(name="query", type=StringType)
gmf_all_gmfgraph_SVGProperty_attribute: Property = Property(name="attribute", type=StringType)
gmf_all_gmfgraph_SVGProperty_type: Property = Property(name="type", type=StringType)
gmf_all_gmfgraph_SVGProperty_getter: Property = Property(name="getter", type=StringType)
gmf_all_gmfgraph_SVGProperty_setter: Property = Property(name="setter", type=StringType)
gmf_all_gmfgraph_SVGProperty_callSuper: Property = Property(name="callSuper", type=BooleanType)
gmf_all_gmfgraph_SVGProperty.attributes={gmf_all_gmfgraph_SVGProperty_type, gmf_all_gmfgraph_SVGProperty_callSuper, gmf_all_gmfgraph_SVGProperty_attribute, gmf_all_gmfgraph_SVGProperty_query, gmf_all_gmfgraph_SVGProperty_getter, gmf_all_gmfgraph_SVGProperty_setter}

# gmf_all_gmfgraph_Rectangle2D class attributes and methods
gmf_all_gmfgraph_Rectangle2D_x: Property = Property(name="x", type=FloatType)
gmf_all_gmfgraph_Rectangle2D_y: Property = Property(name="y", type=FloatType)
gmf_all_gmfgraph_Rectangle2D_width: Property = Property(name="width", type=FloatType)
gmf_all_gmfgraph_Rectangle2D_height: Property = Property(name="height", type=FloatType)
gmf_all_gmfgraph_Rectangle2D.attributes={gmf_all_gmfgraph_Rectangle2D_width, gmf_all_gmfgraph_Rectangle2D_x, gmf_all_gmfgraph_Rectangle2D_y, gmf_all_gmfgraph_Rectangle2D_height}

# gmf_all_gmfgraph_Pin class attributes and methods
gmf_all_gmfgraph_Pin_m_getOperationName: Method = Method(name="getOperationName", parameters={}, type=StringType)
gmf_all_gmfgraph_Pin_m_getOperationType: Method = Method(name="getOperationType", parameters={}, type=StringType)
gmf_all_gmfgraph_Pin.methods={gmf_all_gmfgraph_Pin_m_getOperationType, gmf_all_gmfgraph_Pin_m_getOperationName}

# Rectangle2D class attributes and methods

# gmf_all_gmfgraph_ColorPin class attributes and methods
gmf_all_gmfgraph_ColorPin_backgroundNotForeground: Property = Property(name="backgroundNotForeground", type=BooleanType)
gmf_all_gmfgraph_ColorPin.attributes={gmf_all_gmfgraph_ColorPin_backgroundNotForeground}

# gmf_all_gmfgraph_VisiblePin class attributes and methods

# gmf_all_gmfgraph_PinOwner class attributes and methods

# gmf_all_gmfgraph_CustomPin class attributes and methods
gmf_all_gmfgraph_CustomPin_customOperationName: Property = Property(name="customOperationName", type=StringType)
gmf_all_gmfgraph_CustomPin_customOperationType: Property = Property(name="customOperationType", type=StringType)
gmf_all_gmfgraph_CustomPin.attributes={gmf_all_gmfgraph_CustomPin_customOperationName, gmf_all_gmfgraph_CustomPin_customOperationType}

# Relationships
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="TopNodeReference", type=gmf_all_mappings_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_Mapping", type=TopNodeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
links1: BinaryAssociation = BinaryAssociation(
    name="links1",
    ends={
        Property(name="LinkMapping", type=gmf_all_mappings_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_Mapping2", type=LinkMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
diagram3: BinaryAssociation = BinaryAssociation(
    name="diagram3",
    ends={
        Property(name="CanvasMapping", type=gmf_all_mappings_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_Mapping4", type=CanvasMapping, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
appearanceStyles5: BinaryAssociation = BinaryAssociation(
    name="appearanceStyles5",
    ends={
        Property(name="StyleSelector", type=gmf_all_mappings_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_Mapping6", type=StyleSelector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
audits7: BinaryAssociation = BinaryAssociation(
    name="audits7",
    ends={
        Property(name="AuditContainer", type=gmf_all_mappings_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_Mapping8", type=AuditContainer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
metrics9: BinaryAssociation = BinaryAssociation(
    name="metrics9",
    ends={
        Property(name="MetricContainer", type=gmf_all_mappings_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_Mapping10", type=MetricContainer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
domainMetaElement11: BinaryAssociation = BinaryAssociation(
    name="domainMetaElement11",
    ends={
        Property(name="mappings_gmf_all_EClass", type=gmf_all_mappings_MappingEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_MappingEntry", type=mappings_gmf_all_EClass, multiplicity=Multiplicity(0, 1))
    }
)
domainSpecialization12: BinaryAssociation = BinaryAssociation(
    name="domainSpecialization12",
    ends={
        Property(name="Constraint", type=gmf_all_mappings_MappingEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_MappingEntry13", type=Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
domainInitializer14: BinaryAssociation = BinaryAssociation(
    name="domainInitializer14",
    ends={
        Property(name="ElementInitializer", type=gmf_all_mappings_MappingEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_MappingEntry15", type=ElementInitializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
labelMappings16: BinaryAssociation = BinaryAssociation(
    name="labelMappings16",
    ends={
        Property(name="mappings", type=gmf_all_mappings_MappingEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="LabelMapping", type=LabelMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relatedDiagrams17: BinaryAssociation = BinaryAssociation(
    name="relatedDiagrams17",
    ends={
        Property(name="CanvasMapping19", type=gmf_all_mappings_MappingEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_MappingEntry18", type=CanvasMapping, multiplicity=Multiplicity(0, 9999))
    }
)
containmentFeature22: BinaryAssociation = BinaryAssociation(
    name="containmentFeature22",
    ends={
        Property(name="mappings_gmf_all_EReference", type=gmf_all_mappings_NeedsContainment, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_NeedsContainment", type=mappings_gmf_all_EReference, multiplicity=Multiplicity(0, 1))
    }
)
childrenFeature23: BinaryAssociation = BinaryAssociation(
    name="childrenFeature23",
    ends={
        Property(name="mappings_gmf_all_EReference24", type=gmf_all_mappings_NodeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_NodeReference", type=mappings_gmf_all_EReference, multiplicity=Multiplicity(0, 1))
    }
)
child25: BinaryAssociation = BinaryAssociation(
    name="child25",
    ends={
        Property(name="NodeMapping", type=gmf_all_mappings_NodeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_NodeReference26", type=NodeMapping, multiplicity=Multiplicity(0, 1))
    }
)
parentNode27: BinaryAssociation = BinaryAssociation(
    name="parentNode27",
    ends={
        Property(name="mappings29", type=gmf_all_mappings_ChildReference, multiplicity=Multiplicity(1, 1)),
        Property(name="NodeMapping28", type=NodeMapping, multiplicity=Multiplicity(1, 1))
    }
)
compartment30: BinaryAssociation = BinaryAssociation(
    name="compartment30",
    ends={
        Property(name="mappings31", type=gmf_all_mappings_ChildReference, multiplicity=Multiplicity(1, 1)),
        Property(name="CompartmentMapping", type=CompartmentMapping, multiplicity=Multiplicity(0, 1))
    }
)
ownedChild32: BinaryAssociation = BinaryAssociation(
    name="ownedChild32",
    ends={
        Property(name="NodeMapping33", type=gmf_all_mappings_ChildReference, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_ChildReference", type=NodeMapping, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referencedChild34: BinaryAssociation = BinaryAssociation(
    name="referencedChild34",
    ends={
        Property(name="NodeMapping36", type=gmf_all_mappings_ChildReference, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_ChildReference35", type=NodeMapping, multiplicity=Multiplicity(0, 1))
    }
)
ownedChild37: BinaryAssociation = BinaryAssociation(
    name="ownedChild37",
    ends={
        Property(name="NodeMapping38", type=gmf_all_mappings_TopNodeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_TopNodeReference", type=NodeMapping, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
visualEffects20: BinaryAssociation = BinaryAssociation(
    name="visualEffects20",
    ends={
        Property(name="mappings21", type=gmf_all_mappings_MappingEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="VisualEffectMapping", type=VisualEffectMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
diagramNode39: BinaryAssociation = BinaryAssociation(
    name="diagramNode39",
    ends={
        Property(name="gmf_all_mappings_NodeMapping", type=Node, multiplicity=Multiplicity(1, 1)),
        Property(name="Node", type=gmf_all_mappings_NodeMapping, multiplicity=Multiplicity(1, 1))
    }
)
children40: BinaryAssociation = BinaryAssociation(
    name="children40",
    ends={
        Property(name="mappings41", type=gmf_all_mappings_NodeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="ChildReference", type=ChildReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
compartments42: BinaryAssociation = BinaryAssociation(
    name="compartments42",
    ends={
        Property(name="mappings44", type=gmf_all_mappings_NodeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="CompartmentMapping43", type=CompartmentMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
compartment45: BinaryAssociation = BinaryAssociation(
    name="compartment45",
    ends={
        Property(name="Compartment", type=gmf_all_mappings_CompartmentMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_CompartmentMapping", type=Compartment, multiplicity=Multiplicity(1, 1))
    }
)
parentNode46: BinaryAssociation = BinaryAssociation(
    name="parentNode46",
    ends={
        Property(name="mappings48", type=gmf_all_mappings_CompartmentMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="NodeMapping47", type=NodeMapping, multiplicity=Multiplicity(1, 1))
    }
)
children49: BinaryAssociation = BinaryAssociation(
    name="children49",
    ends={
        Property(name="mappings51", type=gmf_all_mappings_CompartmentMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="ChildReference50", type=ChildReference, multiplicity=Multiplicity(0, 9999))
    }
)
diagramLink52: BinaryAssociation = BinaryAssociation(
    name="diagramLink52",
    ends={
        Property(name="Connection", type=gmf_all_mappings_LinkMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_LinkMapping", type=Connection, multiplicity=Multiplicity(1, 1))
    }
)
sourceMetaFeature53: BinaryAssociation = BinaryAssociation(
    name="sourceMetaFeature53",
    ends={
        Property(name="mappings_gmf_all_EStructuralFeature", type=gmf_all_mappings_LinkMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_LinkMapping54", type=mappings_gmf_all_EStructuralFeature, multiplicity=Multiplicity(0, 1))
    }
)
linkMetaFeature55: BinaryAssociation = BinaryAssociation(
    name="linkMetaFeature55",
    ends={
        Property(name="mappings_gmf_all_EStructuralFeature57", type=gmf_all_mappings_LinkMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_LinkMapping56", type=mappings_gmf_all_EStructuralFeature, multiplicity=Multiplicity(0, 1))
    }
)
creationConstraints58: BinaryAssociation = BinaryAssociation(
    name="creationConstraints58",
    ends={
        Property(name="mappings59", type=gmf_all_mappings_LinkMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="LinkConstraints", type=LinkConstraints, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
diagramCanvas60: BinaryAssociation = BinaryAssociation(
    name="diagramCanvas60",
    ends={
        Property(name="Canvas", type=gmf_all_mappings_CanvasMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_CanvasMapping", type=Canvas, multiplicity=Multiplicity(1, 1))
    }
)
domainModel61: BinaryAssociation = BinaryAssociation(
    name="domainModel61",
    ends={
        Property(name="mappings_gmf_all_EPackage", type=gmf_all_mappings_CanvasMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_CanvasMapping62", type=mappings_gmf_all_EPackage, multiplicity=Multiplicity(0, 1))
    }
)
domainMetaElement63: BinaryAssociation = BinaryAssociation(
    name="domainMetaElement63",
    ends={
        Property(name="mappings_gmf_all_EClass65", type=gmf_all_mappings_CanvasMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_CanvasMapping64", type=mappings_gmf_all_EClass, multiplicity=Multiplicity(0, 1))
    }
)
palette66: BinaryAssociation = BinaryAssociation(
    name="palette66",
    ends={
        Property(name="Palette", type=gmf_all_mappings_CanvasMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_CanvasMapping67", type=Palette, multiplicity=Multiplicity(0, 1))
    }
)
menuContributions68: BinaryAssociation = BinaryAssociation(
    name="menuContributions68",
    ends={
        Property(name="MainMenu", type=gmf_all_mappings_CanvasMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_CanvasMapping69", type=MainMenu, multiplicity=Multiplicity(0, 9999))
    }
)
toolbarContributions70: BinaryAssociation = BinaryAssociation(
    name="toolbarContributions70",
    ends={
        Property(name="Toolbar", type=gmf_all_mappings_CanvasMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_CanvasMapping71", type=Toolbar, multiplicity=Multiplicity(0, 9999))
    }
)
diagramLabel72: BinaryAssociation = BinaryAssociation(
    name="diagramLabel72",
    ends={
        Property(name="DiagramLabel", type=gmf_all_mappings_LabelMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_LabelMapping", type=DiagramLabel, multiplicity=Multiplicity(1, 1))
    }
)
mapEntry73: BinaryAssociation = BinaryAssociation(
    name="mapEntry73",
    ends={
        Property(name="mappings74", type=gmf_all_mappings_LabelMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="MappingEntry", type=MappingEntry, multiplicity=Multiplicity(1, 1))
    }
)
features75: BinaryAssociation = BinaryAssociation(
    name="features75",
    ends={
        Property(name="mappings_gmf_all_EAttribute", type=gmf_all_mappings_FeatureLabelMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_FeatureLabelMapping", type=mappings_gmf_all_EAttribute, multiplicity=Multiplicity(1, 9999))
    }
)
editableFeatures76: BinaryAssociation = BinaryAssociation(
    name="editableFeatures76",
    ends={
        Property(name="mappings_gmf_all_EAttribute78", type=gmf_all_mappings_FeatureLabelMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_FeatureLabelMapping77", type=mappings_gmf_all_EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
itemsExpression81: BinaryAssociation = BinaryAssociation(
    name="itemsExpression81",
    ends={
        Property(name="ValueExpression", type=gmf_all_mappings_OclChoiceLabelMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_OclChoiceLabelMapping82", type=ValueExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
showExpression83: BinaryAssociation = BinaryAssociation(
    name="showExpression83",
    ends={
        Property(name="ValueExpression85", type=gmf_all_mappings_OclChoiceLabelMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_OclChoiceLabelMapping84", type=ValueExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
viewExpression86: BinaryAssociation = BinaryAssociation(
    name="viewExpression86",
    ends={
        Property(name="ValueExpression87", type=gmf_all_mappings_ExpressionLabelMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_ExpressionLabelMapping", type=ValueExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
editExpression88: BinaryAssociation = BinaryAssociation(
    name="editExpression88",
    ends={
        Property(name="ValueExpression90", type=gmf_all_mappings_ExpressionLabelMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_ExpressionLabelMapping89", type=ValueExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
validateExpression91: BinaryAssociation = BinaryAssociation(
    name="validateExpression91",
    ends={
        Property(name="Constraint93", type=gmf_all_mappings_ExpressionLabelMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_ExpressionLabelMapping92", type=Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
linkMapping94: BinaryAssociation = BinaryAssociation(
    name="linkMapping94",
    ends={
        Property(name="mappings96", type=gmf_all_mappings_LinkConstraints, multiplicity=Multiplicity(1, 1)),
        Property(name="LinkMapping95", type=LinkMapping, multiplicity=Multiplicity(1, 1))
    }
)
sourceEnd97: BinaryAssociation = BinaryAssociation(
    name="sourceEnd97",
    ends={
        Property(name="Constraint98", type=gmf_all_mappings_LinkConstraints, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_LinkConstraints", type=Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
feature79: BinaryAssociation = BinaryAssociation(
    name="feature79",
    ends={
        Property(name="mappings_gmf_all_EStructuralFeature80", type=gmf_all_mappings_OclChoiceLabelMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_OclChoiceLabelMapping", type=mappings_gmf_all_EStructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
targetEnd99: BinaryAssociation = BinaryAssociation(
    name="targetEnd99",
    ends={
        Property(name="Constraint101", type=gmf_all_mappings_LinkConstraints, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_LinkConstraints100", type=Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mappingEntry102: BinaryAssociation = BinaryAssociation(
    name="mappingEntry102",
    ends={
        Property(name="MappingEntry103", type=gmf_all_mappings_ElementInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_ElementInitializer", type=MappingEntry, multiplicity=Multiplicity(1, 1))
    }
)
initializers104: BinaryAssociation = BinaryAssociation(
    name="initializers104",
    ends={
        Property(name="mappings105", type=gmf_all_mappings_FeatureSeqInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="FeatureInitializer", type=FeatureInitializer, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
elementClass106: BinaryAssociation = BinaryAssociation(
    name="elementClass106",
    ends={
        Property(name="mappings_gmf_all_EClass107", type=gmf_all_mappings_FeatureSeqInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_FeatureSeqInitializer", type=mappings_gmf_all_EClass, multiplicity=Multiplicity(0, 1))
    }
)
creatingInitializer108: BinaryAssociation = BinaryAssociation(
    name="creatingInitializer108",
    ends={
        Property(name="mappings109", type=gmf_all_mappings_FeatureSeqInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="ReferenceNewElementSpec", type=ReferenceNewElementSpec, multiplicity=Multiplicity(0, 1))
    }
)
feature110: BinaryAssociation = BinaryAssociation(
    name="feature110",
    ends={
        Property(name="mappings_gmf_all_EStructuralFeature111", type=gmf_all_mappings_FeatureInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_FeatureInitializer", type=mappings_gmf_all_EStructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
featureSeqInitializer112: BinaryAssociation = BinaryAssociation(
    name="featureSeqInitializer112",
    ends={
        Property(name="mappings113", type=gmf_all_mappings_FeatureInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="FeatureSeqInitializer", type=FeatureSeqInitializer, multiplicity=Multiplicity(1, 1))
    }
)
value114: BinaryAssociation = BinaryAssociation(
    name="value114",
    ends={
        Property(name="ValueExpression115", type=gmf_all_mappings_FeatureValueSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_FeatureValueSpec", type=ValueExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
newElementInitializers116: BinaryAssociation = BinaryAssociation(
    name="newElementInitializers116",
    ends={
        Property(name="mappings118", type=gmf_all_mappings_ReferenceNewElementSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="FeatureSeqInitializer117", type=FeatureSeqInitializer, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
contextMenu119: BinaryAssociation = BinaryAssociation(
    name="contextMenu119",
    ends={
        Property(name="ContextMenu", type=gmf_all_mappings_MenuOwner, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_MenuOwner", type=ContextMenu, multiplicity=Multiplicity(0, 1))
    }
)
tool120: BinaryAssociation = BinaryAssociation(
    name="tool120",
    ends={
        Property(name="AbstractTool", type=gmf_all_mappings_ToolOwner, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_ToolOwner", type=AbstractTool, multiplicity=Multiplicity(0, 1))
    }
)
appearanceStyle121: BinaryAssociation = BinaryAssociation(
    name="appearanceStyle121",
    ends={
        Property(name="StyleSelector122", type=gmf_all_mappings_AppearanceSteward, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_AppearanceSteward", type=StyleSelector, multiplicity=Multiplicity(0, 1))
    }
)
parentContainer123: BinaryAssociation = BinaryAssociation(
    name="parentContainer123",
    ends={
        Property(name="mappings125", type=gmf_all_mappings_AuditContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="AuditContainer124", type=AuditContainer, multiplicity=Multiplicity(0, 1))
    }
)
rule131: BinaryAssociation = BinaryAssociation(
    name="rule131",
    ends={
        Property(name="Constraint132", type=gmf_all_mappings_AuditRule, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_AuditRule", type=Constraint, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target133: BinaryAssociation = BinaryAssociation(
    name="target133",
    ends={
        Property(name="Auditable", type=gmf_all_mappings_AuditRule, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_AuditRule134", type=Auditable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
container135: BinaryAssociation = BinaryAssociation(
    name="container135",
    ends={
        Property(name="mappings137", type=gmf_all_mappings_AuditRule, multiplicity=Multiplicity(1, 1)),
        Property(name="AuditContainer136", type=AuditContainer, multiplicity=Multiplicity(1, 1))
    }
)
element138: BinaryAssociation = BinaryAssociation(
    name="element138",
    ends={
        Property(name="mappings_gmf_all_EClass139", type=gmf_all_mappings_DomainElementTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_DomainElementTarget", type=mappings_gmf_all_EClass, multiplicity=Multiplicity(1, 1))
    }
)
attribute140: BinaryAssociation = BinaryAssociation(
    name="attribute140",
    ends={
        Property(name="mappings_gmf_all_EAttribute141", type=gmf_all_mappings_DomainAttributeTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_DomainAttributeTarget", type=mappings_gmf_all_EAttribute, multiplicity=Multiplicity(1, 1))
    }
)
audits126: BinaryAssociation = BinaryAssociation(
    name="audits126",
    ends={
        Property(name="mappings127", type=gmf_all_mappings_AuditContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="AuditRule", type=AuditRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
childContainers128: BinaryAssociation = BinaryAssociation(
    name="childContainers128",
    ends={
        Property(name="mappings130", type=gmf_all_mappings_AuditContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="AuditContainer129", type=AuditContainer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
element142: BinaryAssociation = BinaryAssociation(
    name="element142",
    ends={
        Property(name="MappingEntry143", type=gmf_all_mappings_DiagramElementTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_DiagramElementTarget", type=MappingEntry, multiplicity=Multiplicity(1, 1))
    }
)
element144: BinaryAssociation = BinaryAssociation(
    name="element144",
    ends={
        Property(name="mappings_gmf_all_EClass145", type=gmf_all_mappings_NotationElementTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_NotationElementTarget", type=mappings_gmf_all_EClass, multiplicity=Multiplicity(1, 1))
    }
)
metrics146: BinaryAssociation = BinaryAssociation(
    name="metrics146",
    ends={
        Property(name="mappings147", type=gmf_all_mappings_MetricContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="MetricRule", type=MetricRule, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
rule148: BinaryAssociation = BinaryAssociation(
    name="rule148",
    ends={
        Property(name="ValueExpression149", type=gmf_all_mappings_MetricRule, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_MetricRule", type=ValueExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target150: BinaryAssociation = BinaryAssociation(
    name="target150",
    ends={
        Property(name="Measurable", type=gmf_all_mappings_MetricRule, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_MetricRule151", type=Measurable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
container152: BinaryAssociation = BinaryAssociation(
    name="container152",
    ends={
        Property(name="mappings154", type=gmf_all_mappings_MetricRule, multiplicity=Multiplicity(1, 1)),
        Property(name="MetricContainer153", type=MetricContainer, multiplicity=Multiplicity(1, 1))
    }
)
diagramPin157: BinaryAssociation = BinaryAssociation(
    name="diagramPin157",
    ends={
        Property(name="Pin", type=gmf_all_mappings_VisualEffectMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_VisualEffectMapping", type=Pin, multiplicity=Multiplicity(1, 1))
    }
)
parentMapEntry158: BinaryAssociation = BinaryAssociation(
    name="parentMapEntry158",
    ends={
        Property(name="mappings160", type=gmf_all_mappings_VisualEffectMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="MappingEntry159", type=MappingEntry, multiplicity=Multiplicity(1, 1))
    }
)
sharedActions161: BinaryAssociation = BinaryAssociation(
    name="sharedActions161",
    ends={
        Property(name="MenuAction", type=gmf_all_tooldef_ToolRegistry, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_tooldef_ToolRegistry", type=MenuAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allMenus162: BinaryAssociation = BinaryAssociation(
    name="allMenus162",
    ends={
        Property(name="Menu", type=gmf_all_tooldef_ToolRegistry, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_tooldef_ToolRegistry163", type=Menu, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
palette164: BinaryAssociation = BinaryAssociation(
    name="palette164",
    ends={
        Property(name="Palette166", type=gmf_all_tooldef_ToolRegistry, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_tooldef_ToolRegistry165", type=Palette, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
smallIcon167: BinaryAssociation = BinaryAssociation(
    name="smallIcon167",
    ends={
        Property(name="Image", type=gmf_all_tooldef_AbstractTool, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_tooldef_AbstractTool", type=Image, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
largeIcon168: BinaryAssociation = BinaryAssociation(
    name="largeIcon168",
    ends={
        Property(name="Image170", type=gmf_all_tooldef_AbstractTool, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_tooldef_AbstractTool169", type=Image, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tools171: BinaryAssociation = BinaryAssociation(
    name="tools171",
    ends={
        Property(name="AbstractTool172", type=gmf_all_tooldef_ToolContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_tooldef_ToolContainer", type=AbstractTool, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metric155: BinaryAssociation = BinaryAssociation(
    name="metric155",
    ends={
        Property(name="MetricRule156", type=gmf_all_mappings_AuditedMetricTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_mappings_AuditedMetricTarget", type=MetricRule, multiplicity=Multiplicity(1, 1))
    }
)
active173: BinaryAssociation = BinaryAssociation(
    name="active173",
    ends={
        Property(name="AbstractTool174", type=gmf_all_tooldef_ToolGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_tooldef_ToolGroup", type=AbstractTool, multiplicity=Multiplicity(0, 1))
    }
)
default175: BinaryAssociation = BinaryAssociation(
    name="default175",
    ends={
        Property(name="AbstractTool176", type=gmf_all_tooldef_Palette, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_tooldef_Palette", type=AbstractTool, multiplicity=Multiplicity(0, 1))
    }
)
items177: BinaryAssociation = BinaryAssociation(
    name="items177",
    ends={
        Property(name="ItemBase", type=gmf_all_tooldef_Menu, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_tooldef_Menu", type=ItemBase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
icon178: BinaryAssociation = BinaryAssociation(
    name="icon178",
    ends={
        Property(name="Image179", type=gmf_all_tooldef_ContributionItem, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_tooldef_ContributionItem", type=Image, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
item180: BinaryAssociation = BinaryAssociation(
    name="item180",
    ends={
        Property(name="ItemBase181", type=gmf_all_tooldef_ItemRef, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_tooldef_ItemRef", type=ItemBase, multiplicity=Multiplicity(1, 1))
    }
)
figures184: BinaryAssociation = BinaryAssociation(
    name="figures184",
    ends={
        Property(name="FigureGallery", type=gmf_all_gmfgraph_Canvas, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_Canvas", type=FigureGallery, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodes185: BinaryAssociation = BinaryAssociation(
    name="nodes185",
    ends={
        Property(name="Node187", type=gmf_all_gmfgraph_Canvas, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_Canvas186", type=Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connections188: BinaryAssociation = BinaryAssociation(
    name="connections188",
    ends={
        Property(name="Connection190", type=gmf_all_gmfgraph_Canvas, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_Canvas189", type=Connection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
compartments191: BinaryAssociation = BinaryAssociation(
    name="compartments191",
    ends={
        Property(name="Compartment193", type=gmf_all_gmfgraph_Canvas, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_Canvas192", type=Compartment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
labels194: BinaryAssociation = BinaryAssociation(
    name="labels194",
    ends={
        Property(name="DiagramLabel196", type=gmf_all_gmfgraph_Canvas, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_Canvas195", type=DiagramLabel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
default182: BinaryAssociation = BinaryAssociation(
    name="default182",
    ends={
        Property(name="MenuAction183", type=gmf_all_tooldef_ContextMenu, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_tooldef_ContextMenu", type=MenuAction, multiplicity=Multiplicity(0, 1))
    }
)
descriptors198: BinaryAssociation = BinaryAssociation(
    name="descriptors198",
    ends={
        Property(name="FigureDescriptor", type=gmf_all_gmfgraph_FigureGallery, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_FigureGallery199", type=FigureDescriptor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
borders200: BinaryAssociation = BinaryAssociation(
    name="borders200",
    ends={
        Property(name="Border", type=gmf_all_gmfgraph_FigureGallery, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_FigureGallery201", type=Border, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
layouts202: BinaryAssociation = BinaryAssociation(
    name="layouts202",
    ends={
        Property(name="Layout", type=gmf_all_gmfgraph_FigureGallery, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_FigureGallery203", type=Layout, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
figure204: BinaryAssociation = BinaryAssociation(
    name="figure204",
    ends={
        Property(name="FigureDescriptor205", type=gmf_all_gmfgraph_DiagramElement, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_DiagramElement", type=FigureDescriptor, multiplicity=Multiplicity(1, 1))
    }
)
facets206: BinaryAssociation = BinaryAssociation(
    name="facets206",
    ends={
        Property(name="VisualFacet", type=gmf_all_gmfgraph_DiagramElement, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_DiagramElement207", type=VisualFacet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contentPane208: BinaryAssociation = BinaryAssociation(
    name="contentPane208",
    ends={
        Property(name="ChildAccess", type=gmf_all_gmfgraph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_Node", type=ChildAccess, multiplicity=Multiplicity(0, 1))
    }
)
accessor209: BinaryAssociation = BinaryAssociation(
    name="accessor209",
    ends={
        Property(name="ChildAccess210", type=gmf_all_gmfgraph_Compartment, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_Compartment", type=ChildAccess, multiplicity=Multiplicity(0, 1))
    }
)
accessor211: BinaryAssociation = BinaryAssociation(
    name="accessor211",
    ends={
        Property(name="ChildAccess212", type=gmf_all_gmfgraph_DiagramLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_DiagramLabel", type=ChildAccess, multiplicity=Multiplicity(0, 1))
    }
)
container213: BinaryAssociation = BinaryAssociation(
    name="container213",
    ends={
        Property(name="ChildAccess215", type=gmf_all_gmfgraph_DiagramLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_DiagramLabel214", type=ChildAccess, multiplicity=Multiplicity(0, 1))
    }
)
figures197: BinaryAssociation = BinaryAssociation(
    name="figures197",
    ends={
        Property(name="RealFigure", type=gmf_all_gmfgraph_FigureGallery, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_FigureGallery", type=RealFigure, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultSize216: BinaryAssociation = BinaryAssociation(
    name="defaultSize216",
    ends={
        Property(name="Dimension", type=gmf_all_gmfgraph_DefaultSizeFacet, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_DefaultSizeFacet", type=Dimension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
descriptor217: BinaryAssociation = BinaryAssociation(
    name="descriptor217",
    ends={
        Property(name="FigureDescriptor218", type=gmf_all_gmfgraph_Figure, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_Figure", type=FigureDescriptor, multiplicity=Multiplicity(0, 1))
    }
)
foregroundColor219: BinaryAssociation = BinaryAssociation(
    name="foregroundColor219",
    ends={
        Property(name="Color", type=gmf_all_gmfgraph_Figure, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_Figure220", type=Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
backgroundColor221: BinaryAssociation = BinaryAssociation(
    name="backgroundColor221",
    ends={
        Property(name="Color223", type=gmf_all_gmfgraph_Figure, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_Figure222", type=Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
maximumSize224: BinaryAssociation = BinaryAssociation(
    name="maximumSize224",
    ends={
        Property(name="Dimension226", type=gmf_all_gmfgraph_Figure, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_Figure225", type=Dimension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
minimumSize227: BinaryAssociation = BinaryAssociation(
    name="minimumSize227",
    ends={
        Property(name="Dimension229", type=gmf_all_gmfgraph_Figure, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_Figure228", type=Dimension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
preferredSize230: BinaryAssociation = BinaryAssociation(
    name="preferredSize230",
    ends={
        Property(name="Dimension232", type=gmf_all_gmfgraph_Figure, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_Figure231", type=Dimension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
font233: BinaryAssociation = BinaryAssociation(
    name="font233",
    ends={
        Property(name="Font", type=gmf_all_gmfgraph_Figure, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_Figure234", type=Font, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
insets235: BinaryAssociation = BinaryAssociation(
    name="insets235",
    ends={
        Property(name="Insets", type=gmf_all_gmfgraph_Figure, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_Figure236", type=Insets, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
border237: BinaryAssociation = BinaryAssociation(
    name="border237",
    ends={
        Property(name="Border239", type=gmf_all_gmfgraph_Figure, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_Figure238", type=Border, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
location240: BinaryAssociation = BinaryAssociation(
    name="location240",
    ends={
        Property(name="Point", type=gmf_all_gmfgraph_Figure, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_Figure241", type=Point, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
size242: BinaryAssociation = BinaryAssociation(
    name="size242",
    ends={
        Property(name="Point244", type=gmf_all_gmfgraph_Figure, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_Figure243", type=Point, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actualFigure245: BinaryAssociation = BinaryAssociation(
    name="actualFigure245",
    ends={
        Property(name="Figure", type=gmf_all_gmfgraph_FigureDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_FigureDescriptor", type=Figure, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
accessors246: BinaryAssociation = BinaryAssociation(
    name="accessors246",
    ends={
        Property(name="gmfgraph", type=gmf_all_gmfgraph_FigureDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="ChildAccess247", type=ChildAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner248: BinaryAssociation = BinaryAssociation(
    name="owner248",
    ends={
        Property(name="gmfgraph250", type=gmf_all_gmfgraph_ChildAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="FigureDescriptor249", type=FigureDescriptor, multiplicity=Multiplicity(1, 1))
    }
)
figure251: BinaryAssociation = BinaryAssociation(
    name="figure251",
    ends={
        Property(name="Figure252", type=gmf_all_gmfgraph_ChildAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_ChildAccess", type=Figure, multiplicity=Multiplicity(1, 1))
    }
)
children253: BinaryAssociation = BinaryAssociation(
    name="children253",
    ends={
        Property(name="Figure254", type=gmf_all_gmfgraph_RealFigure, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_RealFigure", type=Figure, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
figure255: BinaryAssociation = BinaryAssociation(
    name="figure255",
    ends={
        Property(name="RealFigure256", type=gmf_all_gmfgraph_FigureRef, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_FigureRef", type=RealFigure, multiplicity=Multiplicity(1, 1))
    }
)
template259: BinaryAssociation = BinaryAssociation(
    name="template259",
    ends={
        Property(name="Point260", type=gmf_all_gmfgraph_Polyline, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_Polyline", type=Point, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sourceDecoration261: BinaryAssociation = BinaryAssociation(
    name="sourceDecoration261",
    ends={
        Property(name="DecorationFigure", type=gmf_all_gmfgraph_PolylineConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_PolylineConnection", type=DecorationFigure, multiplicity=Multiplicity(0, 1))
    }
)
targetDecoration262: BinaryAssociation = BinaryAssociation(
    name="targetDecoration262",
    ends={
        Property(name="DecorationFigure264", type=gmf_all_gmfgraph_PolylineConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_PolylineConnection263", type=DecorationFigure, multiplicity=Multiplicity(0, 1))
    }
)
resolvedChildren257: BinaryAssociation = BinaryAssociation(
    name="resolvedChildren257",
    ends={
        Property(name="Figure258", type=gmf_all_gmfgraph_Shape, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_Shape", type=Figure, multiplicity=Multiplicity(0, 9999))
    }
)
attributes265: BinaryAssociation = BinaryAssociation(
    name="attributes265",
    ends={
        Property(name="CustomAttribute", type=gmf_all_gmfgraph_CustomAttributeOwner, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_CustomAttributeOwner", type=CustomAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typedFigure266: BinaryAssociation = BinaryAssociation(
    name="typedFigure266",
    ends={
        Property(name="RealFigure267", type=gmf_all_gmfgraph_FigureAccessor, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_FigureAccessor", type=RealFigure, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
customChildren268: BinaryAssociation = BinaryAssociation(
    name="customChildren268",
    ends={
        Property(name="FigureAccessor", type=gmf_all_gmfgraph_CustomFigure, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_CustomFigure", type=FigureAccessor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actual269: BinaryAssociation = BinaryAssociation(
    name="actual269",
    ends={
        Property(name="Border270", type=gmf_all_gmfgraph_BorderRef, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_BorderRef", type=Border, multiplicity=Multiplicity(1, 1))
    }
)
color271: BinaryAssociation = BinaryAssociation(
    name="color271",
    ends={
        Property(name="Color272", type=gmf_all_gmfgraph_LineBorder, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_LineBorder", type=Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
insets273: BinaryAssociation = BinaryAssociation(
    name="insets273",
    ends={
        Property(name="Insets274", type=gmf_all_gmfgraph_MarginBorder, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_MarginBorder", type=Insets, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
outer275: BinaryAssociation = BinaryAssociation(
    name="outer275",
    ends={
        Property(name="Border276", type=gmf_all_gmfgraph_CompoundBorder, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_CompoundBorder", type=Border, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inner277: BinaryAssociation = BinaryAssociation(
    name="inner277",
    ends={
        Property(name="Border279", type=gmf_all_gmfgraph_CompoundBorder, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_CompoundBorder278", type=Border, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owner280: BinaryAssociation = BinaryAssociation(
    name="owner280",
    ends={
        Property(name="gmfgraph281", type=gmf_all_gmfgraph_LayoutData, multiplicity=Multiplicity(1, 1)),
        Property(name="Layoutable", type=Layoutable, multiplicity=Multiplicity(1, 1))
    }
)
sizeHint282: BinaryAssociation = BinaryAssociation(
    name="sizeHint282",
    ends={
        Property(name="Dimension283", type=gmf_all_gmfgraph_GridLayoutData, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_GridLayoutData", type=Dimension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
layoutData284: BinaryAssociation = BinaryAssociation(
    name="layoutData284",
    ends={
        Property(name="gmfgraph285", type=gmf_all_gmfgraph_Layoutable, multiplicity=Multiplicity(1, 1)),
        Property(name="LayoutData", type=LayoutData, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
layout286: BinaryAssociation = BinaryAssociation(
    name="layout286",
    ends={
        Property(name="Layout287", type=gmf_all_gmfgraph_Layoutable, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_Layoutable", type=Layout, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actual288: BinaryAssociation = BinaryAssociation(
    name="actual288",
    ends={
        Property(name="Layout289", type=gmf_all_gmfgraph_LayoutRef, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_LayoutRef", type=Layout, multiplicity=Multiplicity(1, 1))
    }
)
margins290: BinaryAssociation = BinaryAssociation(
    name="margins290",
    ends={
        Property(name="Dimension291", type=gmf_all_gmfgraph_GridLayout, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_GridLayout", type=Dimension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
spacing292: BinaryAssociation = BinaryAssociation(
    name="spacing292",
    ends={
        Property(name="Dimension294", type=gmf_all_gmfgraph_GridLayout, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_GridLayout293", type=Dimension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
spacing295: BinaryAssociation = BinaryAssociation(
    name="spacing295",
    ends={
        Property(name="Dimension296", type=gmf_all_gmfgraph_BorderLayout, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_BorderLayout", type=Dimension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
topLeft297: BinaryAssociation = BinaryAssociation(
    name="topLeft297",
    ends={
        Property(name="Point298", type=gmf_all_gmfgraph_XYLayoutData, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_XYLayoutData", type=Point, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
size299: BinaryAssociation = BinaryAssociation(
    name="size299",
    ends={
        Property(name="Dimension301", type=gmf_all_gmfgraph_XYLayoutData, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_XYLayoutData300", type=Dimension, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
properties302: BinaryAssociation = BinaryAssociation(
    name="properties302",
    ends={
        Property(name="SVGProperty", type=gmf_all_gmfgraph_SVGFigure, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_SVGFigure", type=SVGProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
areaOfInterest303: BinaryAssociation = BinaryAssociation(
    name="areaOfInterest303",
    ends={
        Property(name="Rectangle2D", type=gmf_all_gmfgraph_SVGFigure, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_SVGFigure304", type=Rectangle2D, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pins305: BinaryAssociation = BinaryAssociation(
    name="pins305",
    ends={
        Property(name="Pin306", type=gmf_all_gmfgraph_PinOwner, multiplicity=Multiplicity(1, 1)),
        Property(name="gmf_all_gmfgraph_PinOwner", type=Pin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_gmf_all_mappings_NodeReference_NeedsContainment = Generalization(general=NeedsContainment, specific=gmf_all_mappings_NodeReference)
gen_gmf_all_mappings_ChildReference_NodeReference = Generalization(general=NodeReference, specific=gmf_all_mappings_ChildReference)
gen_gmf_all_mappings_TopNodeReference_NodeReference = Generalization(general=NodeReference, specific=gmf_all_mappings_TopNodeReference)
gen_gmf_all_mappings_NodeMapping_mappings_MappingEntry = Generalization(general=mappings_MappingEntry, specific=gmf_all_mappings_NodeMapping)
gen_gmf_all_mappings_NodeMapping_mappings_MenuOwner = Generalization(general=mappings_MenuOwner, specific=gmf_all_mappings_NodeMapping)
gen_gmf_all_mappings_NodeMapping_mappings_ToolOwner = Generalization(general=mappings_ToolOwner, specific=gmf_all_mappings_NodeMapping)
gen_gmf_all_mappings_LinkMapping_mappings_MappingEntry = Generalization(general=mappings_MappingEntry, specific=gmf_all_mappings_LinkMapping)
gen_gmf_all_mappings_LinkMapping_mappings_NeedsContainment = Generalization(general=mappings_NeedsContainment, specific=gmf_all_mappings_LinkMapping)
gen_gmf_all_mappings_LinkMapping_mappings_MenuOwner = Generalization(general=mappings_MenuOwner, specific=gmf_all_mappings_LinkMapping)
gen_gmf_all_mappings_LinkMapping_mappings_ToolOwner = Generalization(general=mappings_ToolOwner, specific=gmf_all_mappings_LinkMapping)
gen_gmf_all_mappings_LinkMapping_mappings_AppearanceSteward = Generalization(general=mappings_AppearanceSteward, specific=gmf_all_mappings_LinkMapping)
gen_gmf_all_mappings_NodeMapping_mappings_AppearanceSteward = Generalization(general=mappings_AppearanceSteward, specific=gmf_all_mappings_NodeMapping)
gen_gmf_all_mappings_FeatureLabelMapping_LabelMapping = Generalization(general=LabelMapping, specific=gmf_all_mappings_FeatureLabelMapping)
gen_gmf_all_mappings_OclChoiceLabelMapping_LabelMapping = Generalization(general=LabelMapping, specific=gmf_all_mappings_OclChoiceLabelMapping)
gen_gmf_all_mappings_DesignLabelMapping_LabelMapping = Generalization(general=LabelMapping, specific=gmf_all_mappings_DesignLabelMapping)
gen_gmf_all_mappings_ExpressionLabelMapping_LabelMapping = Generalization(general=LabelMapping, specific=gmf_all_mappings_ExpressionLabelMapping)
gen_gmf_all_mappings_Constraint_ValueExpression = Generalization(general=ValueExpression, specific=gmf_all_mappings_Constraint)
gen_gmf_all_mappings_FeatureSeqInitializer_ElementInitializer = Generalization(general=ElementInitializer, specific=gmf_all_mappings_FeatureSeqInitializer)
gen_gmf_all_mappings_FeatureValueSpec_FeatureInitializer = Generalization(general=FeatureInitializer, specific=gmf_all_mappings_FeatureValueSpec)
gen_gmf_all_mappings_ReferenceNewElementSpec_FeatureInitializer = Generalization(general=FeatureInitializer, specific=gmf_all_mappings_ReferenceNewElementSpec)
gen_gmf_all_mappings_AuditRule_RuleBase = Generalization(general=RuleBase, specific=gmf_all_mappings_AuditRule)
gen_gmf_all_mappings_DomainElementTarget_mappings_Auditable = Generalization(general=mappings_Auditable, specific=gmf_all_mappings_DomainElementTarget)
gen_gmf_all_mappings_DomainElementTarget_mappings_Measurable = Generalization(general=mappings_Measurable, specific=gmf_all_mappings_DomainElementTarget)
gen_gmf_all_mappings_DomainAttributeTarget_Auditable = Generalization(general=Auditable, specific=gmf_all_mappings_DomainAttributeTarget)
gen_gmf_all_mappings_NotationElementTarget_mappings_Auditable = Generalization(general=mappings_Auditable, specific=gmf_all_mappings_NotationElementTarget)
gen_gmf_all_mappings_NotationElementTarget_mappings_Measurable = Generalization(general=mappings_Measurable, specific=gmf_all_mappings_NotationElementTarget)
gen_gmf_all_mappings_MetricRule_RuleBase = Generalization(general=RuleBase, specific=gmf_all_mappings_MetricRule)
gen_gmf_all_mappings_AuditedMetricTarget_Auditable = Generalization(general=Auditable, specific=gmf_all_mappings_AuditedMetricTarget)
gen_gmf_all_mappings_DiagramElementTarget_mappings_Auditable = Generalization(general=mappings_Auditable, specific=gmf_all_mappings_DiagramElementTarget)
gen_gmf_all_mappings_DiagramElementTarget_mappings_Measurable = Generalization(general=mappings_Measurable, specific=gmf_all_mappings_DiagramElementTarget)
gen_gmf_all_tooldef_ToolContainer_AbstractTool = Generalization(general=AbstractTool, specific=gmf_all_tooldef_ToolContainer)
gen_gmf_all_tooldef_Palette_ToolContainer = Generalization(general=ToolContainer, specific=gmf_all_tooldef_Palette)
gen_gmf_all_tooldef_StandardTool_AbstractTool = Generalization(general=AbstractTool, specific=gmf_all_tooldef_StandardTool)
gen_gmf_all_tooldef_CreationTool_AbstractTool = Generalization(general=AbstractTool, specific=gmf_all_tooldef_CreationTool)
gen_gmf_all_tooldef_GenericTool_AbstractTool = Generalization(general=AbstractTool, specific=gmf_all_tooldef_GenericTool)
gen_gmf_all_tooldef_Separator_ItemBase = Generalization(general=ItemBase, specific=gmf_all_tooldef_Separator)
gen_gmf_all_tooldef_PredefinedItem_ItemBase = Generalization(general=ItemBase, specific=gmf_all_tooldef_PredefinedItem)
gen_gmf_all_tooldef_PredefinedMenu_tooldef_Menu = Generalization(general=tooldef_Menu, specific=gmf_all_tooldef_PredefinedMenu)
gen_gmf_all_tooldef_PredefinedMenu_tooldef_PredefinedItem = Generalization(general=tooldef_PredefinedItem, specific=gmf_all_tooldef_PredefinedMenu)
gen_gmf_all_tooldef_ContributionItem_ItemBase = Generalization(general=ItemBase, specific=gmf_all_tooldef_ContributionItem)
gen_gmf_all_tooldef_MenuAction_ContributionItem = Generalization(general=ContributionItem, specific=gmf_all_tooldef_MenuAction)
gen_gmf_all_tooldef_ItemRef_ItemBase = Generalization(general=ItemBase, specific=gmf_all_tooldef_ItemRef)
gen_gmf_all_tooldef_ContextMenu_Menu = Generalization(general=Menu, specific=gmf_all_tooldef_ContextMenu)
gen_gmf_all_tooldef_PaletteSeparator_AbstractTool = Generalization(general=AbstractTool, specific=gmf_all_tooldef_PaletteSeparator)
gen_gmf_all_tooldef_ToolGroup_ToolContainer = Generalization(general=ToolContainer, specific=gmf_all_tooldef_ToolGroup)
gen_gmf_all_tooldef_MainMenu_Menu = Generalization(general=Menu, specific=gmf_all_tooldef_MainMenu)
gen_gmf_all_tooldef_Toolbar_Menu = Generalization(general=Menu, specific=gmf_all_tooldef_Toolbar)
gen_gmf_all_tooldef_DefaultImage_Image = Generalization(general=Image, specific=gmf_all_tooldef_DefaultImage)
gen_gmf_all_tooldef_BundleImage_Image = Generalization(general=Image, specific=gmf_all_tooldef_BundleImage)
gen_gmf_all_tooldef_GenericStyleSelector_StyleSelector = Generalization(general=StyleSelector, specific=gmf_all_tooldef_GenericStyleSelector)
gen_gmf_all_gmfgraph_Canvas_Identity = Generalization(general=Identity, specific=gmf_all_gmfgraph_Canvas)
gen_gmf_all_gmfgraph_FigureGallery_Identity = Generalization(general=Identity, specific=gmf_all_gmfgraph_FigureGallery)
gen_gmf_all_tooldef_PopupMenu_tooldef_Menu = Generalization(general=tooldef_Menu, specific=gmf_all_tooldef_PopupMenu)
gen_gmf_all_tooldef_PopupMenu_tooldef_ContributionItem = Generalization(general=tooldef_ContributionItem, specific=gmf_all_tooldef_PopupMenu)
gen_gmf_all_gmfgraph_DiagramElement_Identity = Generalization(general=Identity, specific=gmf_all_gmfgraph_DiagramElement)
gen_gmf_all_gmfgraph_AbstractNode_DiagramElement = Generalization(general=DiagramElement, specific=gmf_all_gmfgraph_AbstractNode)
gen_gmf_all_gmfgraph_Node_AbstractNode = Generalization(general=AbstractNode, specific=gmf_all_gmfgraph_Node)
gen_gmf_all_gmfgraph_Connection_DiagramElement = Generalization(general=DiagramElement, specific=gmf_all_gmfgraph_Connection)
gen_gmf_all_gmfgraph_Compartment_DiagramElement = Generalization(general=DiagramElement, specific=gmf_all_gmfgraph_Compartment)
gen_gmf_all_gmfgraph_DiagramLabel_Node = Generalization(general=Node, specific=gmf_all_gmfgraph_DiagramLabel)
gen_gmf_all_gmfgraph_AlignmentFacet_VisualFacet = Generalization(general=VisualFacet, specific=gmf_all_gmfgraph_AlignmentFacet)
gen_gmf_all_gmfgraph_GradientFacet_VisualFacet = Generalization(general=VisualFacet, specific=gmf_all_gmfgraph_GradientFacet)
gen_gmf_all_gmfgraph_LabelOffsetFacet_VisualFacet = Generalization(general=VisualFacet, specific=gmf_all_gmfgraph_LabelOffsetFacet)
gen_gmf_all_gmfgraph_DefaultSizeFacet_VisualFacet = Generalization(general=VisualFacet, specific=gmf_all_gmfgraph_DefaultSizeFacet)
gen_gmf_all_gmfgraph_Figure_Layoutable = Generalization(general=Layoutable, specific=gmf_all_gmfgraph_Figure)
gen_gmf_all_gmfgraph_GeneralFacet_VisualFacet = Generalization(general=VisualFacet, specific=gmf_all_gmfgraph_GeneralFacet)
gen_gmf_all_gmfgraph_RealFigure_gmfgraph_AbstractFigure = Generalization(general=gmfgraph_AbstractFigure, specific=gmf_all_gmfgraph_RealFigure)
gen_gmf_all_gmfgraph_RealFigure_gmfgraph_PinOwner = Generalization(general=gmfgraph_PinOwner, specific=gmf_all_gmfgraph_RealFigure)
gen_gmf_all_gmfgraph_RealFigure_gmfgraph_CustomAttributeOwner = Generalization(general=gmfgraph_CustomAttributeOwner, specific=gmf_all_gmfgraph_RealFigure)
gen_gmf_all_gmfgraph_FigureRef_AbstractFigure = Generalization(general=AbstractFigure, specific=gmf_all_gmfgraph_FigureRef)
gen_gmf_all_gmfgraph_ConnectionFigure_RealFigure = Generalization(general=RealFigure, specific=gmf_all_gmfgraph_ConnectionFigure)
gen_gmf_all_gmfgraph_DecorationFigure_RealFigure = Generalization(general=RealFigure, specific=gmf_all_gmfgraph_DecorationFigure)
gen_gmf_all_gmfgraph_Shape_RealFigure = Generalization(general=RealFigure, specific=gmf_all_gmfgraph_Shape)
gen_gmf_all_gmfgraph_AbstractFigure_Figure = Generalization(general=Figure, specific=gmf_all_gmfgraph_AbstractFigure)
gen_gmf_all_gmfgraph_FigureDescriptor_Identity = Generalization(general=Identity, specific=gmf_all_gmfgraph_FigureDescriptor)
gen_gmf_all_gmfgraph_LabeledContainer_RealFigure = Generalization(general=RealFigure, specific=gmf_all_gmfgraph_LabeledContainer)
gen_gmf_all_gmfgraph_VerticalLabel_RealFigure = Generalization(general=RealFigure, specific=gmf_all_gmfgraph_VerticalLabel)
gen_gmf_all_gmfgraph_Rectangle_Shape = Generalization(general=Shape, specific=gmf_all_gmfgraph_Rectangle)
gen_gmf_all_gmfgraph_InvisibleRectangle_RealFigure = Generalization(general=RealFigure, specific=gmf_all_gmfgraph_InvisibleRectangle)
gen_gmf_all_gmfgraph_RoundedRectangle_Shape = Generalization(general=Shape, specific=gmf_all_gmfgraph_RoundedRectangle)
gen_gmf_all_gmfgraph_Ellipse_Shape = Generalization(general=Shape, specific=gmf_all_gmfgraph_Ellipse)
gen_gmf_all_gmfgraph_Polyline_Shape = Generalization(general=Shape, specific=gmf_all_gmfgraph_Polyline)
gen_gmf_all_gmfgraph_Polygon_Polyline = Generalization(general=Polyline, specific=gmf_all_gmfgraph_Polygon)
gen_gmf_all_gmfgraph_ScalablePolygon_Polygon = Generalization(general=Polygon, specific=gmf_all_gmfgraph_ScalablePolygon)
gen_gmf_all_gmfgraph_PolylineConnection_gmfgraph_Polyline = Generalization(general=gmfgraph_Polyline, specific=gmf_all_gmfgraph_PolylineConnection)
gen_gmf_all_gmfgraph_PolylineConnection_gmfgraph_ConnectionFigure = Generalization(general=gmfgraph_ConnectionFigure, specific=gmf_all_gmfgraph_PolylineConnection)
gen_gmf_all_gmfgraph_PolylineDecoration_gmfgraph_Polyline = Generalization(general=gmfgraph_Polyline, specific=gmf_all_gmfgraph_PolylineDecoration)
gen_gmf_all_gmfgraph_PolylineDecoration_gmfgraph_DecorationFigure = Generalization(general=gmfgraph_DecorationFigure, specific=gmf_all_gmfgraph_PolylineDecoration)
gen_gmf_all_gmfgraph_PolygonDecoration_gmfgraph_Polygon = Generalization(general=gmfgraph_Polygon, specific=gmf_all_gmfgraph_PolygonDecoration)
gen_gmf_all_gmfgraph_Label_RealFigure = Generalization(general=RealFigure, specific=gmf_all_gmfgraph_Label)
gen_gmf_all_gmfgraph_PolygonDecoration_gmfgraph_DecorationFigure = Generalization(general=gmfgraph_DecorationFigure, specific=gmf_all_gmfgraph_PolygonDecoration)
gen_gmf_all_gmfgraph_CustomClass_CustomAttributeOwner = Generalization(general=CustomAttributeOwner, specific=gmf_all_gmfgraph_CustomClass)
gen_gmf_all_gmfgraph_CustomFigure_gmfgraph_RealFigure = Generalization(general=gmfgraph_RealFigure, specific=gmf_all_gmfgraph_CustomFigure)
gen_gmf_all_gmfgraph_CustomFigure_gmfgraph_CustomClass = Generalization(general=gmfgraph_CustomClass, specific=gmf_all_gmfgraph_CustomFigure)
gen_gmf_all_gmfgraph_RGBColor_Color = Generalization(general=Color, specific=gmf_all_gmfgraph_RGBColor)
gen_gmf_all_gmfgraph_ConstantColor_Color = Generalization(general=Color, specific=gmf_all_gmfgraph_ConstantColor)
gen_gmf_all_gmfgraph_BasicFont_Font = Generalization(general=Font, specific=gmf_all_gmfgraph_BasicFont)
gen_gmf_all_gmfgraph_CustomDecoration_gmfgraph_CustomFigure = Generalization(general=gmfgraph_CustomFigure, specific=gmf_all_gmfgraph_CustomDecoration)
gen_gmf_all_gmfgraph_CustomDecoration_gmfgraph_DecorationFigure = Generalization(general=gmfgraph_DecorationFigure, specific=gmf_all_gmfgraph_CustomDecoration)
gen_gmf_all_gmfgraph_CustomConnection_gmfgraph_CustomFigure = Generalization(general=gmfgraph_CustomFigure, specific=gmf_all_gmfgraph_CustomConnection)
gen_gmf_all_gmfgraph_CustomConnection_gmfgraph_ConnectionFigure = Generalization(general=gmfgraph_ConnectionFigure, specific=gmf_all_gmfgraph_CustomConnection)
gen_gmf_all_gmfgraph_LineBorder_Border = Generalization(general=Border, specific=gmf_all_gmfgraph_LineBorder)
gen_gmf_all_gmfgraph_BorderRef_Border = Generalization(general=Border, specific=gmf_all_gmfgraph_BorderRef)
gen_gmf_all_gmfgraph_CompoundBorder_Border = Generalization(general=Border, specific=gmf_all_gmfgraph_CompoundBorder)
gen_gmf_all_gmfgraph_CustomBorder_gmfgraph_Border = Generalization(general=gmfgraph_Border, specific=gmf_all_gmfgraph_CustomBorder)
gen_gmf_all_gmfgraph_CustomBorder_gmfgraph_CustomClass = Generalization(general=gmfgraph_CustomClass, specific=gmf_all_gmfgraph_CustomBorder)
gen_gmf_all_gmfgraph_MarginBorder_Border = Generalization(general=Border, specific=gmf_all_gmfgraph_MarginBorder)
gen_gmf_all_gmfgraph_CustomLayoutData_gmfgraph_LayoutData = Generalization(general=gmfgraph_LayoutData, specific=gmf_all_gmfgraph_CustomLayoutData)
gen_gmf_all_gmfgraph_CustomLayoutData_gmfgraph_CustomClass = Generalization(general=gmfgraph_CustomClass, specific=gmf_all_gmfgraph_CustomLayoutData)
gen_gmf_all_gmfgraph_GridLayoutData_LayoutData = Generalization(general=LayoutData, specific=gmf_all_gmfgraph_GridLayoutData)
gen_gmf_all_gmfgraph_BorderLayoutData_LayoutData = Generalization(general=LayoutData, specific=gmf_all_gmfgraph_BorderLayoutData)
gen_gmf_all_gmfgraph_LayoutRef_Layout = Generalization(general=Layout, specific=gmf_all_gmfgraph_LayoutRef)
gen_gmf_all_gmfgraph_CustomLayout_gmfgraph_CustomClass = Generalization(general=gmfgraph_CustomClass, specific=gmf_all_gmfgraph_CustomLayout)
gen_gmf_all_gmfgraph_GridLayout_Layout = Generalization(general=Layout, specific=gmf_all_gmfgraph_GridLayout)
gen_gmf_all_gmfgraph_BorderLayout_Layout = Generalization(general=Layout, specific=gmf_all_gmfgraph_BorderLayout)
gen_gmf_all_gmfgraph_CustomLayout_gmfgraph_Layout = Generalization(general=gmfgraph_Layout, specific=gmf_all_gmfgraph_CustomLayout)
gen_gmf_all_gmfgraph_XYLayout_Layout = Generalization(general=Layout, specific=gmf_all_gmfgraph_XYLayout)
gen_gmf_all_gmfgraph_XYLayoutData_LayoutData = Generalization(general=LayoutData, specific=gmf_all_gmfgraph_XYLayoutData)
gen_gmf_all_gmfgraph_StackLayout_Layout = Generalization(general=Layout, specific=gmf_all_gmfgraph_StackLayout)
gen_gmf_all_gmfgraph_CenterLayout_Layout = Generalization(general=Layout, specific=gmf_all_gmfgraph_CenterLayout)
gen_gmf_all_gmfgraph_SVGFigure_RealFigure = Generalization(general=RealFigure, specific=gmf_all_gmfgraph_SVGFigure)
gen_gmf_all_gmfgraph_FlowLayout_Layout = Generalization(general=Layout, specific=gmf_all_gmfgraph_FlowLayout)
gen_gmf_all_gmfgraph_Pin_Identity = Generalization(general=Identity, specific=gmf_all_gmfgraph_Pin)
gen_gmf_all_gmfgraph_ColorPin_Pin = Generalization(general=Pin, specific=gmf_all_gmfgraph_ColorPin)
gen_gmf_all_gmfgraph_VisiblePin_Pin = Generalization(general=Pin, specific=gmf_all_gmfgraph_VisiblePin)
gen_gmf_all_gmfgraph_CustomPin_Pin = Generalization(general=Pin, specific=gmf_all_gmfgraph_CustomPin)

# Domain Model
domain_model = DomainModel(
    name="gmf_all",
    types={gmf_all_mappings_Mapping, TopNodeReference, LinkMapping, CanvasMapping, StyleSelector, AuditContainer, MetricContainer, gmf_all_mappings_MappingEntry, mappings_gmf_all_EClass, Constraint, ElementInitializer, LabelMapping, VisualEffectMapping, gmf_all_mappings_NodeReference, NeedsContainment, NodeMapping, gmf_all_mappings_ChildReference, NodeReference, CompartmentMapping, gmf_all_mappings_TopNodeReference, gmf_all_mappings_NodeMapping, mappings_MappingEntry, mappings_MenuOwner, mappings_ToolOwner, gmf_all_mappings_NeedsContainment, mappings_gmf_all_EReference, ChildReference, gmf_all_mappings_CompartmentMapping, Compartment, gmf_all_mappings_LinkMapping, mappings_NeedsContainment, Connection, mappings_gmf_all_EStructuralFeature, LinkConstraints, mappings_AppearanceSteward, Node, mappings_gmf_all_EPackage, Palette, MainMenu, Toolbar, gmf_all_mappings_LabelMapping, DiagramLabel, MappingEntry, gmf_all_mappings_FeatureLabelMapping, mappings_gmf_all_EAttribute, gmf_all_mappings_OclChoiceLabelMapping, gmf_all_mappings_CanvasMapping, Canvas, ValueExpression, gmf_all_mappings_DesignLabelMapping, gmf_all_mappings_ExpressionLabelMapping, gmf_all_mappings_Constraint, gmf_all_mappings_LinkConstraints, gmf_all_mappings_ValueExpression, gmf_all_mappings_ElementInitializer, gmf_all_mappings_FeatureSeqInitializer, FeatureInitializer, ReferenceNewElementSpec, gmf_all_mappings_FeatureInitializer, FeatureSeqInitializer, gmf_all_mappings_FeatureValueSpec, gmf_all_mappings_ReferenceNewElementSpec, gmf_all_mappings_MenuOwner, ContextMenu, gmf_all_mappings_ToolOwner, AbstractTool, gmf_all_mappings_AppearanceSteward, gmf_all_mappings_AuditContainer, AuditRule, gmf_all_mappings_RuleBase, gmf_all_mappings_AuditRule, RuleBase, Auditable, gmf_all_mappings_DomainElementTarget, mappings_Auditable, mappings_Measurable, gmf_all_mappings_DomainAttributeTarget, gmf_all_mappings_NotationElementTarget, gmf_all_mappings_MetricContainer, MetricRule, gmf_all_mappings_MetricRule, Measurable, gmf_all_mappings_AuditedMetricTarget, gmf_all_mappings_DiagramElementTarget, gmf_all_mappings_Auditable, gmf_all_mappings_Measurable, gmf_all_mappings_VisualEffectMapping, Pin, gmf_all_tooldef_ToolRegistry, MenuAction, Menu, gmf_all_tooldef_AbstractTool, Image, gmf_all_tooldef_ToolContainer, gmf_all_tooldef_Palette, gmf_all_tooldef_StandardTool, gmf_all_tooldef_CreationTool, gmf_all_tooldef_GenericTool, gmf_all_tooldef_ItemBase, gmf_all_tooldef_Menu, ItemBase, gmf_all_tooldef_Separator, gmf_all_tooldef_PredefinedItem, gmf_all_tooldef_PredefinedMenu, tooldef_Menu, tooldef_PredefinedItem, gmf_all_tooldef_ContributionItem, gmf_all_tooldef_MenuAction, ContributionItem, gmf_all_tooldef_ItemRef, gmf_all_tooldef_ContextMenu, gmf_all_tooldef_PaletteSeparator, gmf_all_tooldef_ToolGroup, ToolContainer, gmf_all_tooldef_MainMenu, gmf_all_tooldef_Toolbar, gmf_all_tooldef_Image, gmf_all_tooldef_DefaultImage, gmf_all_tooldef_BundleImage, gmf_all_tooldef_StyleSelector, gmf_all_tooldef_GenericStyleSelector, gmf_all_gmfgraph_Canvas, Identity, FigureGallery, gmf_all_gmfgraph_FigureGallery, gmf_all_tooldef_PopupMenu, tooldef_ContributionItem, FigureDescriptor, Border, Layout, gmf_all_gmfgraph_Identity, gmf_all_gmfgraph_DiagramElement, VisualFacet, gmf_all_gmfgraph_AbstractNode, DiagramElement, gmf_all_gmfgraph_Node, AbstractNode, ChildAccess, gmf_all_gmfgraph_Connection, gmf_all_gmfgraph_Compartment, gmf_all_gmfgraph_DiagramLabel, gmf_all_gmfgraph_VisualFacet, RealFigure, gmf_all_gmfgraph_AlignmentFacet, gmf_all_gmfgraph_GradientFacet, gmf_all_gmfgraph_LabelOffsetFacet, gmf_all_gmfgraph_DefaultSizeFacet, Dimension, gmf_all_gmfgraph_Figure, Layoutable, Color, Font, Insets, Point, gmf_all_gmfgraph_GeneralFacet, gmf_all_gmfgraph_ChildAccess, gmf_all_gmfgraph_RealFigure, gmfgraph_AbstractFigure, gmfgraph_PinOwner, gmfgraph_CustomAttributeOwner, gmf_all_gmfgraph_FigureRef, AbstractFigure, gmf_all_gmfgraph_ConnectionFigure, gmf_all_gmfgraph_DecorationFigure, gmf_all_gmfgraph_Shape, gmf_all_gmfgraph_AbstractFigure, Figure, gmf_all_gmfgraph_FigureDescriptor, gmf_all_gmfgraph_LabeledContainer, gmf_all_gmfgraph_VerticalLabel, gmf_all_gmfgraph_Rectangle, Shape, gmf_all_gmfgraph_InvisibleRectangle, gmf_all_gmfgraph_RoundedRectangle, gmf_all_gmfgraph_Ellipse, gmf_all_gmfgraph_Polyline, gmf_all_gmfgraph_Polygon, Polyline, gmf_all_gmfgraph_ScalablePolygon, Polygon, gmf_all_gmfgraph_PolylineConnection, gmfgraph_Polyline, gmfgraph_ConnectionFigure, DecorationFigure, gmf_all_gmfgraph_PolylineDecoration, gmfgraph_DecorationFigure, gmf_all_gmfgraph_PolygonDecoration, gmfgraph_Polygon, gmf_all_gmfgraph_Label, gmf_all_gmfgraph_CustomAttributeOwner, CustomAttribute, gmf_all_gmfgraph_CustomClass, CustomAttributeOwner, gmf_all_gmfgraph_CustomAttribute, gmf_all_gmfgraph_FigureAccessor, gmf_all_gmfgraph_CustomFigure, gmfgraph_RealFigure, gmfgraph_CustomClass, FigureAccessor, gmf_all_gmfgraph_Color, gmf_all_gmfgraph_RGBColor, gmf_all_gmfgraph_ConstantColor, gmf_all_gmfgraph_Font, gmf_all_gmfgraph_BasicFont, gmf_all_gmfgraph_Point, gmf_all_gmfgraph_Dimension, gmf_all_gmfgraph_Insets, gmf_all_gmfgraph_CustomDecoration, gmfgraph_CustomFigure, gmf_all_gmfgraph_CustomConnection, gmf_all_gmfgraph_LineBorder, gmf_all_gmfgraph_Border, gmf_all_gmfgraph_BorderRef, gmf_all_gmfgraph_CompoundBorder, gmf_all_gmfgraph_CustomBorder, gmfgraph_Border, gmf_all_gmfgraph_MarginBorder, gmf_all_gmfgraph_LayoutData, gmf_all_gmfgraph_CustomLayoutData, gmfgraph_LayoutData, gmf_all_gmfgraph_GridLayoutData, LayoutData, gmf_all_gmfgraph_BorderLayoutData, gmf_all_gmfgraph_Layoutable, gmf_all_gmfgraph_Layout, gmf_all_gmfgraph_LayoutRef, gmf_all_gmfgraph_GridLayout, gmf_all_gmfgraph_BorderLayout, gmf_all_gmfgraph_CustomLayout, gmfgraph_Layout, gmf_all_gmfgraph_XYLayout, gmf_all_gmfgraph_XYLayoutData, gmf_all_gmfgraph_StackLayout, gmf_all_gmfgraph_CenterLayout, gmf_all_gmfgraph_SVGFigure, SVGProperty, gmf_all_gmfgraph_FlowLayout, gmf_all_gmfgraph_SVGProperty, gmf_all_gmfgraph_Rectangle2D, gmf_all_gmfgraph_Pin, Rectangle2D, gmf_all_gmfgraph_ColorPin, gmf_all_gmfgraph_VisiblePin, gmf_all_gmfgraph_PinOwner, gmf_all_gmfgraph_CustomPin, LabelTextAccessMethod, Severity, Language, StandardToolKind, ActionKind, AppearanceStyle, ColorConstants, FontStyle, LineKind, Direction, Alignment, SVGPropertyType},
    associations={nodes0, links1, diagram3, appearanceStyles5, audits7, metrics9, domainMetaElement11, domainSpecialization12, domainInitializer14, labelMappings16, relatedDiagrams17, containmentFeature22, childrenFeature23, child25, parentNode27, compartment30, ownedChild32, referencedChild34, ownedChild37, visualEffects20, diagramNode39, children40, compartments42, compartment45, parentNode46, children49, diagramLink52, sourceMetaFeature53, linkMetaFeature55, creationConstraints58, diagramCanvas60, domainModel61, domainMetaElement63, palette66, menuContributions68, toolbarContributions70, diagramLabel72, mapEntry73, features75, editableFeatures76, itemsExpression81, showExpression83, viewExpression86, editExpression88, validateExpression91, linkMapping94, sourceEnd97, feature79, targetEnd99, mappingEntry102, initializers104, elementClass106, creatingInitializer108, feature110, featureSeqInitializer112, value114, newElementInitializers116, contextMenu119, tool120, appearanceStyle121, parentContainer123, rule131, target133, container135, element138, attribute140, audits126, childContainers128, element142, element144, metrics146, rule148, target150, container152, diagramPin157, parentMapEntry158, sharedActions161, allMenus162, palette164, smallIcon167, largeIcon168, tools171, metric155, active173, default175, items177, icon178, item180, figures184, nodes185, connections188, compartments191, labels194, default182, descriptors198, borders200, layouts202, figure204, facets206, contentPane208, accessor209, accessor211, container213, figures197, defaultSize216, descriptor217, foregroundColor219, backgroundColor221, maximumSize224, minimumSize227, preferredSize230, font233, insets235, border237, location240, size242, actualFigure245, accessors246, owner248, figure251, children253, figure255, template259, sourceDecoration261, targetDecoration262, resolvedChildren257, attributes265, typedFigure266, customChildren268, actual269, color271, insets273, outer275, inner277, owner280, sizeHint282, layoutData284, layout286, actual288, margins290, spacing292, spacing295, topLeft297, size299, properties302, areaOfInterest303, pins305},
    generalizations={gen_gmf_all_mappings_NodeReference_NeedsContainment, gen_gmf_all_mappings_ChildReference_NodeReference, gen_gmf_all_mappings_TopNodeReference_NodeReference, gen_gmf_all_mappings_NodeMapping_mappings_MappingEntry, gen_gmf_all_mappings_NodeMapping_mappings_MenuOwner, gen_gmf_all_mappings_NodeMapping_mappings_ToolOwner, gen_gmf_all_mappings_LinkMapping_mappings_MappingEntry, gen_gmf_all_mappings_LinkMapping_mappings_NeedsContainment, gen_gmf_all_mappings_LinkMapping_mappings_MenuOwner, gen_gmf_all_mappings_LinkMapping_mappings_ToolOwner, gen_gmf_all_mappings_LinkMapping_mappings_AppearanceSteward, gen_gmf_all_mappings_NodeMapping_mappings_AppearanceSteward, gen_gmf_all_mappings_FeatureLabelMapping_LabelMapping, gen_gmf_all_mappings_OclChoiceLabelMapping_LabelMapping, gen_gmf_all_mappings_DesignLabelMapping_LabelMapping, gen_gmf_all_mappings_ExpressionLabelMapping_LabelMapping, gen_gmf_all_mappings_Constraint_ValueExpression, gen_gmf_all_mappings_FeatureSeqInitializer_ElementInitializer, gen_gmf_all_mappings_FeatureValueSpec_FeatureInitializer, gen_gmf_all_mappings_ReferenceNewElementSpec_FeatureInitializer, gen_gmf_all_mappings_AuditRule_RuleBase, gen_gmf_all_mappings_DomainElementTarget_mappings_Auditable, gen_gmf_all_mappings_DomainElementTarget_mappings_Measurable, gen_gmf_all_mappings_DomainAttributeTarget_Auditable, gen_gmf_all_mappings_NotationElementTarget_mappings_Auditable, gen_gmf_all_mappings_NotationElementTarget_mappings_Measurable, gen_gmf_all_mappings_MetricRule_RuleBase, gen_gmf_all_mappings_AuditedMetricTarget_Auditable, gen_gmf_all_mappings_DiagramElementTarget_mappings_Auditable, gen_gmf_all_mappings_DiagramElementTarget_mappings_Measurable, gen_gmf_all_tooldef_ToolContainer_AbstractTool, gen_gmf_all_tooldef_Palette_ToolContainer, gen_gmf_all_tooldef_StandardTool_AbstractTool, gen_gmf_all_tooldef_CreationTool_AbstractTool, gen_gmf_all_tooldef_GenericTool_AbstractTool, gen_gmf_all_tooldef_Separator_ItemBase, gen_gmf_all_tooldef_PredefinedItem_ItemBase, gen_gmf_all_tooldef_PredefinedMenu_tooldef_Menu, gen_gmf_all_tooldef_PredefinedMenu_tooldef_PredefinedItem, gen_gmf_all_tooldef_ContributionItem_ItemBase, gen_gmf_all_tooldef_MenuAction_ContributionItem, gen_gmf_all_tooldef_ItemRef_ItemBase, gen_gmf_all_tooldef_ContextMenu_Menu, gen_gmf_all_tooldef_PaletteSeparator_AbstractTool, gen_gmf_all_tooldef_ToolGroup_ToolContainer, gen_gmf_all_tooldef_MainMenu_Menu, gen_gmf_all_tooldef_Toolbar_Menu, gen_gmf_all_tooldef_DefaultImage_Image, gen_gmf_all_tooldef_BundleImage_Image, gen_gmf_all_tooldef_GenericStyleSelector_StyleSelector, gen_gmf_all_gmfgraph_Canvas_Identity, gen_gmf_all_gmfgraph_FigureGallery_Identity, gen_gmf_all_tooldef_PopupMenu_tooldef_Menu, gen_gmf_all_tooldef_PopupMenu_tooldef_ContributionItem, gen_gmf_all_gmfgraph_DiagramElement_Identity, gen_gmf_all_gmfgraph_AbstractNode_DiagramElement, gen_gmf_all_gmfgraph_Node_AbstractNode, gen_gmf_all_gmfgraph_Connection_DiagramElement, gen_gmf_all_gmfgraph_Compartment_DiagramElement, gen_gmf_all_gmfgraph_DiagramLabel_Node, gen_gmf_all_gmfgraph_AlignmentFacet_VisualFacet, gen_gmf_all_gmfgraph_GradientFacet_VisualFacet, gen_gmf_all_gmfgraph_LabelOffsetFacet_VisualFacet, gen_gmf_all_gmfgraph_DefaultSizeFacet_VisualFacet, gen_gmf_all_gmfgraph_Figure_Layoutable, gen_gmf_all_gmfgraph_GeneralFacet_VisualFacet, gen_gmf_all_gmfgraph_RealFigure_gmfgraph_AbstractFigure, gen_gmf_all_gmfgraph_RealFigure_gmfgraph_PinOwner, gen_gmf_all_gmfgraph_RealFigure_gmfgraph_CustomAttributeOwner, gen_gmf_all_gmfgraph_FigureRef_AbstractFigure, gen_gmf_all_gmfgraph_ConnectionFigure_RealFigure, gen_gmf_all_gmfgraph_DecorationFigure_RealFigure, gen_gmf_all_gmfgraph_Shape_RealFigure, gen_gmf_all_gmfgraph_AbstractFigure_Figure, gen_gmf_all_gmfgraph_FigureDescriptor_Identity, gen_gmf_all_gmfgraph_LabeledContainer_RealFigure, gen_gmf_all_gmfgraph_VerticalLabel_RealFigure, gen_gmf_all_gmfgraph_Rectangle_Shape, gen_gmf_all_gmfgraph_InvisibleRectangle_RealFigure, gen_gmf_all_gmfgraph_RoundedRectangle_Shape, gen_gmf_all_gmfgraph_Ellipse_Shape, gen_gmf_all_gmfgraph_Polyline_Shape, gen_gmf_all_gmfgraph_Polygon_Polyline, gen_gmf_all_gmfgraph_ScalablePolygon_Polygon, gen_gmf_all_gmfgraph_PolylineConnection_gmfgraph_Polyline, gen_gmf_all_gmfgraph_PolylineConnection_gmfgraph_ConnectionFigure, gen_gmf_all_gmfgraph_PolylineDecoration_gmfgraph_Polyline, gen_gmf_all_gmfgraph_PolylineDecoration_gmfgraph_DecorationFigure, gen_gmf_all_gmfgraph_PolygonDecoration_gmfgraph_Polygon, gen_gmf_all_gmfgraph_Label_RealFigure, gen_gmf_all_gmfgraph_PolygonDecoration_gmfgraph_DecorationFigure, gen_gmf_all_gmfgraph_CustomClass_CustomAttributeOwner, gen_gmf_all_gmfgraph_CustomFigure_gmfgraph_RealFigure, gen_gmf_all_gmfgraph_CustomFigure_gmfgraph_CustomClass, gen_gmf_all_gmfgraph_RGBColor_Color, gen_gmf_all_gmfgraph_ConstantColor_Color, gen_gmf_all_gmfgraph_BasicFont_Font, gen_gmf_all_gmfgraph_CustomDecoration_gmfgraph_CustomFigure, gen_gmf_all_gmfgraph_CustomDecoration_gmfgraph_DecorationFigure, gen_gmf_all_gmfgraph_CustomConnection_gmfgraph_CustomFigure, gen_gmf_all_gmfgraph_CustomConnection_gmfgraph_ConnectionFigure, gen_gmf_all_gmfgraph_LineBorder_Border, gen_gmf_all_gmfgraph_BorderRef_Border, gen_gmf_all_gmfgraph_CompoundBorder_Border, gen_gmf_all_gmfgraph_CustomBorder_gmfgraph_Border, gen_gmf_all_gmfgraph_CustomBorder_gmfgraph_CustomClass, gen_gmf_all_gmfgraph_MarginBorder_Border, gen_gmf_all_gmfgraph_CustomLayoutData_gmfgraph_LayoutData, gen_gmf_all_gmfgraph_CustomLayoutData_gmfgraph_CustomClass, gen_gmf_all_gmfgraph_GridLayoutData_LayoutData, gen_gmf_all_gmfgraph_BorderLayoutData_LayoutData, gen_gmf_all_gmfgraph_LayoutRef_Layout, gen_gmf_all_gmfgraph_CustomLayout_gmfgraph_CustomClass, gen_gmf_all_gmfgraph_GridLayout_Layout, gen_gmf_all_gmfgraph_BorderLayout_Layout, gen_gmf_all_gmfgraph_CustomLayout_gmfgraph_Layout, gen_gmf_all_gmfgraph_XYLayout_Layout, gen_gmf_all_gmfgraph_XYLayoutData_LayoutData, gen_gmf_all_gmfgraph_StackLayout_Layout, gen_gmf_all_gmfgraph_CenterLayout_Layout, gen_gmf_all_gmfgraph_SVGFigure_RealFigure, gen_gmf_all_gmfgraph_FlowLayout_Layout, gen_gmf_all_gmfgraph_Pin_Identity, gen_gmf_all_gmfgraph_ColorPin_Pin, gen_gmf_all_gmfgraph_VisiblePin_Pin, gen_gmf_all_gmfgraph_CustomPin_Pin},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)