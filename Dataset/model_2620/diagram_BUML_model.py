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
ContainerLayout: Enumeration = Enumeration(
    name="ContainerLayout",
    literals={
            EnumerationLiteral(name="FreeForm"),
			EnumerationLiteral(name="List"),
			EnumerationLiteral(name="HorizontalStack"),
			EnumerationLiteral(name="VerticalStack")
    }
)

LabelPosition: Enumeration = Enumeration(
    name="LabelPosition",
    literals={
            EnumerationLiteral(name="border"),
			EnumerationLiteral(name="node")
    }
)

ContainerShape: Enumeration = Enumeration(
    name="ContainerShape",
    literals={
            EnumerationLiteral(name="parallelogram")
    }
)

BackgroundStyle: Enumeration = Enumeration(
    name="BackgroundStyle",
    literals={
            EnumerationLiteral(name="GradientLeftToRight"),
			EnumerationLiteral(name="Liquid"),
			EnumerationLiteral(name="GradientTopToBottom")
    }
)

BundledImageShape: Enumeration = Enumeration(
    name="BundledImageShape",
    literals={
            EnumerationLiteral(name="square"),
			EnumerationLiteral(name="stroke"),
			EnumerationLiteral(name="triangle"),
			EnumerationLiteral(name="dot"),
			EnumerationLiteral(name="ring"),
			EnumerationLiteral(name="providedShape")
    }
)

LineStyle: Enumeration = Enumeration(
    name="LineStyle",
    literals={
            EnumerationLiteral(name="solid"),
			EnumerationLiteral(name="dash"),
			EnumerationLiteral(name="dot"),
			EnumerationLiteral(name="dash_dot")
    }
)

EdgeArrows: Enumeration = Enumeration(
    name="EdgeArrows",
    literals={
            EnumerationLiteral(name="NoDecoration"),
			EnumerationLiteral(name="OutputArrow"),
			EnumerationLiteral(name="InputArrow"),
			EnumerationLiteral(name="OutputClosedArrow"),
			EnumerationLiteral(name="InputClosedArrow"),
			EnumerationLiteral(name="OutputFillClosedArrow"),
			EnumerationLiteral(name="InputArrowWithDiamond"),
			EnumerationLiteral(name="InputArrowWithFillDiamond"),
			EnumerationLiteral(name="InputFillClosedArrow"),
			EnumerationLiteral(name="Diamond"),
			EnumerationLiteral(name="FillDiamond")
    }
)

EdgeRouting: Enumeration = Enumeration(
    name="EdgeRouting",
    literals={
            EnumerationLiteral(name="straight"),
			EnumerationLiteral(name="manhattan"),
			EnumerationLiteral(name="tree")
    }
)

AlignmentKind: Enumeration = Enumeration(
    name="AlignmentKind",
    literals={
            EnumerationLiteral(name="VERTICAL"),
			EnumerationLiteral(name="HORIZONTAL"),
			EnumerationLiteral(name="SQUARE")
    }
)

ResizeKind: Enumeration = Enumeration(
    name="ResizeKind",
    literals={
            EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="NSEW"),
			EnumerationLiteral(name="NORTH_SOUTH"),
			EnumerationLiteral(name="EAST_WEST")
    }
)

ArrangeConstraint: Enumeration = Enumeration(
    name="ArrangeConstraint",
    literals={
            EnumerationLiteral(name="KEEP_LOCATION"),
			EnumerationLiteral(name="KEEP_SIZE"),
			EnumerationLiteral(name="KEEP_RATIO")
    }
)

FoldingStyle: Enumeration = Enumeration(
    name="FoldingStyle",
    literals={
            EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="SOURCE"),
			EnumerationLiteral(name="TARGET")
    }
)

LayoutDirection: Enumeration = Enumeration(
    name="LayoutDirection",
    literals={
            EnumerationLiteral(name="TopToBottom"),
			EnumerationLiteral(name="LeftToRight"),
			EnumerationLiteral(name="BottomToTop")
    }
)

CenteringStyle: Enumeration = Enumeration(
    name="CenteringStyle",
    literals={
            EnumerationLiteral(name="None"),
			EnumerationLiteral(name="Both"),
			EnumerationLiteral(name="Source"),
			EnumerationLiteral(name="Target")
    }
)

LayoutOptionTarget: Enumeration = Enumeration(
    name="LayoutOptionTarget",
    literals={
            EnumerationLiteral(name="PARENT"),
			EnumerationLiteral(name="NODE"),
			EnumerationLiteral(name="EDGE"),
			EnumerationLiteral(name="PORTS"),
			EnumerationLiteral(name="LABEL")
    }
)

Side: Enumeration = Enumeration(
    name="Side",
    literals={
            EnumerationLiteral(name="WEST"),
			EnumerationLiteral(name="SOUTH"),
			EnumerationLiteral(name="EAST"),
			EnumerationLiteral(name="NORTH")
    }
)

ReconnectionKind: Enumeration = Enumeration(
    name="ReconnectionKind",
    literals={
            EnumerationLiteral(name="RECONNECT_TARGET"),
			EnumerationLiteral(name="RECONNECT_SOURCE"),
			EnumerationLiteral(name="RECONNECT_BOTH")
    }
)

FilterKind: Enumeration = Enumeration(
    name="FilterKind",
    literals={
            EnumerationLiteral(name="HIDE"),
			EnumerationLiteral(name="COLLAPSE")
    }
)

# Classes
diagram_DDiagram = Class(name="diagram::DDiagram")
DRepresentation = Class(name="DRepresentation")
DragAndDropTarget = Class(name="DragAndDropTarget")
diagram_DDiagramElement = Class(name="diagram::DDiagramElement", is_abstract=True)
DiagramDescription = Class(name="DiagramDescription")
diagram_DEdge = Class(name="diagram::DEdge")
diagram_DNode = Class(name="diagram::DNode")
diagram_DNodeListElement = Class(name="diagram::DNodeListElement")
diagram_DDiagramElementContainer = Class(name="diagram::DDiagramElementContainer", is_abstract=True)
concern_ConcernDescription = Class(name="concern::ConcernDescription")
filter_FilterDescription = Class(name="filter::FilterDescription")
AdditionalLayer = Class(name="AdditionalLayer")
validation_ValidationRule = Class(name="validation::ValidationRule")
tool_BehaviorTool = Class(name="tool::BehaviorTool")
diagram_FilterVariableHistory = Class(name="diagram::FilterVariableHistory")
Layer = Class(name="Layer")
diagram_DSemanticDiagram = Class(name="diagram::DSemanticDiagram")
DDiagram = Class(name="DDiagram")
DSemanticDecorator = Class(name="DSemanticDecorator")
DRepresentationElement = Class(name="DRepresentationElement")
diagram_Decoration = Class(name="diagram::Decoration")
DiagramElementMapping = Class(name="DiagramElementMapping")
diagram_GraphicalFilter = Class(name="diagram::GraphicalFilter", is_abstract=True)
IdentifiedElement = Class(name="IdentifiedElement")
diagram_HideFilter = Class(name="diagram::HideFilter")
GraphicalFilter = Class(name="GraphicalFilter")
diagram_HideLabelFilter = Class(name="diagram::HideLabelFilter")
diagram_FoldingPointFilter = Class(name="diagram::FoldingPointFilter")
diagram_FoldingFilter = Class(name="diagram::FoldingFilter")
diagram_AppliedCompositeFilters = Class(name="diagram::AppliedCompositeFilters")
AbstractDNode = Class(name="AbstractDNode")
EdgeTarget = Class(name="EdgeTarget")
diagram_NodeStyle = Class(name="diagram::NodeStyle", is_abstract=True)
diagram_Style = Class(name="diagram::Style")
NodeMapping = Class(name="NodeMapping")
filter_CompositeFilterDescription = Class(name="filter::CompositeFilterDescription")
diagram_AbsoluteBoundsFilter = Class(name="diagram::AbsoluteBoundsFilter")
diagram_AbstractDNode = Class(name="diagram::AbstractDNode", is_abstract=True)
DDiagramElement = Class(name="DDiagramElement")
diagram_ContainerStyle = Class(name="diagram::ContainerStyle", is_abstract=True)
ContainerMapping = Class(name="ContainerMapping")
diagram_DNodeContainer = Class(name="diagram::DNodeContainer")
DDiagramElementContainer = Class(name="DDiagramElementContainer")
diagram_DNodeList = Class(name="diagram::DNodeList")
diagram_EdgeStyle = Class(name="diagram::EdgeStyle")
diagram_EdgeTarget = Class(name="diagram::EdgeTarget", is_abstract=True)
IEdgeMapping = Class(name="IEdgeMapping")
LabelStyle = Class(name="LabelStyle")
Style = Class(name="Style")
BorderedStyle = Class(name="BorderedStyle")
HideLabelCapabilityStyle = Class(name="HideLabelCapabilityStyle")
diagram_Dot = Class(name="diagram::Dot")
NodeStyle = Class(name="NodeStyle")
diagram_GaugeSection = Class(name="diagram::GaugeSection")
Customizable = Class(name="Customizable")
diagram_FlatContainerStyle = Class(name="diagram::FlatContainerStyle")
ContainerStyle = Class(name="ContainerStyle")
diagram_ShapeContainerStyle = Class(name="diagram::ShapeContainerStyle")
diagram_Square = Class(name="diagram::Square")
diagram_Ellipse = Class(name="diagram::Ellipse")
diagram_BundledImage = Class(name="diagram::BundledImage")
diagram_WorkspaceImage = Class(name="diagram::WorkspaceImage")
diagram_CustomStyle = Class(name="diagram::CustomStyle")
diagram_Lozenge = Class(name="diagram::Lozenge")
diagram_CenterLabelStyle = Class(name="diagram::CenterLabelStyle")
diagram_EndLabelStyle = Class(name="diagram::EndLabelStyle")
diagram_BeginLabelStyle = Class(name="diagram::BeginLabelStyle")
diagram_GaugeCompositeStyle = Class(name="diagram::GaugeCompositeStyle")
diagram_BorderedStyle = Class(name="diagram::BorderedStyle")
diagram_Note = Class(name="diagram::Note")
diagram_VariableValue = Class(name="diagram::VariableValue", is_abstract=True)
diagram_CollapseFilter = Class(name="diagram::CollapseFilter")
diagram_IndirectlyCollapseFilter = Class(name="diagram::IndirectlyCollapseFilter")
CollapseFilter = Class(name="CollapseFilter")
BasicLabelStyle = Class(name="BasicLabelStyle")
diagram_EObjectVariableValue = Class(name="diagram::EObjectVariableValue")
diagram_BracketEdgeStyle = Class(name="diagram::BracketEdgeStyle")
EdgeStyle = Class(name="EdgeStyle")
diagram_ComputedStyleDescriptionRegistry = Class(name="diagram::ComputedStyleDescriptionRegistry")
style_StyleDescription = Class(name="style::StyleDescription")
diagram_DragAndDropTarget = Class(name="diagram::DragAndDropTarget")
diagram_HideLabelCapabilityStyle = Class(name="diagram::HideLabelCapabilityStyle", is_abstract=True)
diagram_TypedVariableValue = Class(name="diagram::TypedVariableValue")
VariableValue = Class(name="VariableValue")
TypedVariable = Class(name="TypedVariable")
concern_ConcernSet = Class(name="concern::ConcernSet")
tool_SelectModelElementVariable = Class(name="tool::SelectModelElementVariable")
diagram_EObject = Class(name="diagram::EObject")
diagram_description_DiagramDescription = Class(name="diagram::description::DiagramDescription")
description_DragAndDropTargetDescription = Class(name="description::DragAndDropTargetDescription")
description_RepresentationDescription = Class(name="description::RepresentationDescription")
description_PasteTargetDescription = Class(name="description::PasteTargetDescription")
EdgeMapping = Class(name="EdgeMapping")
validation_ValidationSet = Class(name="validation::ValidationSet")
tool_AbstractToolDescription = Class(name="tool::AbstractToolDescription")
tool_RepresentationCreationDescription = Class(name="tool::RepresentationCreationDescription")
Layout = Class(name="Layout")
tool_InitialOperation = Class(name="tool::InitialOperation")
EdgeMappingImport = Class(name="EdgeMappingImport")
tool_DirectEditLabel = Class(name="tool::DirectEditLabel")
tool_ToolSection = Class(name="tool::ToolSection")
ColorDescription = Class(name="ColorDescription")
diagram_description_DiagramImportDescription = Class(name="diagram::description::DiagramImportDescription")
description_RepresentationImportDescription = Class(name="description::RepresentationImportDescription")
description_DiagramDescription = Class(name="description::DiagramDescription")
diagram_description_DiagramExtensionDescription = Class(name="diagram::description::DiagramExtensionDescription")
RepresentationExtensionDescription = Class(name="RepresentationExtensionDescription")
diagram_description_DiagramElementMapping = Class(name="diagram::description::DiagramElementMapping", is_abstract=True)
description_RepresentationElementMapping = Class(name="description::RepresentationElementMapping")
tool_DeleteElementDescription = Class(name="tool::DeleteElementDescription")
style_NodeStyleDescription = Class(name="style::NodeStyleDescription")
tool_DoubleClickDescription = Class(name="tool::DoubleClickDescription")
diagram_description_AbstractNodeMapping = Class(name="diagram::description::AbstractNodeMapping", is_abstract=True)
description_DiagramElementMapping = Class(name="description::DiagramElementMapping")
description_DocumentedElement = Class(name="description::DocumentedElement")
diagram_description_NodeMapping = Class(name="diagram::description::NodeMapping")
description_AbstractNodeMapping = Class(name="description::AbstractNodeMapping")
ConditionalNodeStyleDescription = Class(name="ConditionalNodeStyleDescription")
diagram_description_ContainerMapping = Class(name="diagram::description::ContainerMapping")
style_ContainerStyleDescription = Class(name="style::ContainerStyleDescription")
ConditionalContainerStyleDescription = Class(name="ConditionalContainerStyleDescription")
diagram_description_NodeMappingImport = Class(name="diagram::description::NodeMappingImport")
description_NodeMapping = Class(name="description::NodeMapping")
description_AbstractMappingImport = Class(name="description::AbstractMappingImport")
diagram_description_ContainerMappingImport = Class(name="diagram::description::ContainerMappingImport")
description_ContainerMapping = Class(name="description::ContainerMapping")
diagram_description_EdgeMapping = Class(name="diagram::description::EdgeMapping")
description_IEdgeMapping = Class(name="description::IEdgeMapping")
diagram_description_IEdgeMapping = Class(name="diagram::description::IEdgeMapping", is_abstract=True)
diagram_description_EdgeMappingImport = Class(name="diagram::description::EdgeMappingImport")
style_EdgeStyleDescription = Class(name="style::EdgeStyleDescription")
ConditionalEdgeStyleDescription = Class(name="ConditionalEdgeStyleDescription")
tool_ReconnectEdgeDescription = Class(name="tool::ReconnectEdgeDescription")
AbstractNodeMapping = Class(name="AbstractNodeMapping")
LayoutOption = Class(name="LayoutOption")
description_IdentifiedElement = Class(name="description::IdentifiedElement")
diagram_description_ConditionalNodeStyleDescription = Class(name="diagram::description::ConditionalNodeStyleDescription")
ConditionalStyleDescription = Class(name="ConditionalStyleDescription")
diagram_description_ConditionalEdgeStyleDescription = Class(name="diagram::description::ConditionalEdgeStyleDescription")
diagram_description_ConditionalContainerStyleDescription = Class(name="diagram::description::ConditionalContainerStyleDescription")
diagram_description_Layout = Class(name="diagram::description::Layout", is_abstract=True)
DocumentedElement = Class(name="DocumentedElement")
diagram_description_OrderedTreeLayout = Class(name="diagram::description::OrderedTreeLayout")
diagram_description_CompositeLayout = Class(name="diagram::description::CompositeLayout")
diagram_description_CustomLayoutConfiguration = Class(name="diagram::description::CustomLayoutConfiguration")
diagram_description_Layer = Class(name="diagram::description::Layer")
description_EndUserDocumentedElement = Class(name="description::EndUserDocumentedElement")
diagram_description_LayoutOption = Class(name="diagram::description::LayoutOption", is_abstract=True)
diagram_description_BooleanLayoutOption = Class(name="diagram::description::BooleanLayoutOption")
diagram_description_StringLayoutOption = Class(name="diagram::description::StringLayoutOption")
diagram_description_IntegerLayoutOption = Class(name="diagram::description::IntegerLayoutOption")
diagram_description_DoubleLayoutOption = Class(name="diagram::description::DoubleLayoutOption")
diagram_description_EnumLayoutOption = Class(name="diagram::description::EnumLayoutOption")
EnumOption = Class(name="EnumOption")
EnumLayoutValue = Class(name="EnumLayoutValue")
diagram_description_EnumSetLayoutOption = Class(name="diagram::description::EnumSetLayoutOption")
diagram_description_EnumOption = Class(name="diagram::description::EnumOption", is_abstract=True)
diagram_description_EnumLayoutValue = Class(name="diagram::description::EnumLayoutValue")
diagram_description_MappingBasedDecoration = Class(name="diagram::description::MappingBasedDecoration")
DecorationDescription = Class(name="DecorationDescription")
diagram_description_DragAndDropTargetDescription = Class(name="diagram::description::DragAndDropTargetDescription", is_abstract=True)
tool_ContainerDropDescription = Class(name="tool::ContainerDropDescription")
DecorationDescriptionsSet = Class(name="DecorationDescriptionsSet")
Customization = Class(name="Customization")
diagram_description_AdditionalLayer = Class(name="diagram::description::AdditionalLayer")
diagram_style_BorderedStyleDescription = Class(name="diagram::style::BorderedStyleDescription")
StyleDescription = Class(name="StyleDescription")
diagram_style_NodeStyleDescription = Class(name="diagram::style::NodeStyleDescription", is_abstract=True)
style_BorderedStyleDescription = Class(name="style::BorderedStyleDescription")
style_LabelStyleDescription = Class(name="style::LabelStyleDescription")
style_TooltipStyleDescription = Class(name="style::TooltipStyleDescription")
style_HideLabelCapabilityStyleDescription = Class(name="style::HideLabelCapabilityStyleDescription")
diagram_style_CustomStyleDescription = Class(name="diagram::style::CustomStyleDescription")
NodeStyleDescription = Class(name="NodeStyleDescription")
diagram_style_SquareDescription = Class(name="diagram::style::SquareDescription")
diagram_style_DotDescription = Class(name="diagram::style::DotDescription")
diagram_style_LozengeNodeDescription = Class(name="diagram::style::LozengeNodeDescription")
diagram_style_EllipseNodeDescription = Class(name="diagram::style::EllipseNodeDescription")
diagram_style_BundledImageDescription = Class(name="diagram::style::BundledImageDescription")
diagram_style_NoteDescription = Class(name="diagram::style::NoteDescription")
diagram_style_GaugeCompositeStyleDescription = Class(name="diagram::style::GaugeCompositeStyleDescription")
style_GaugeSectionDescription = Class(name="style::GaugeSectionDescription")
diagram_style_GaugeSectionDescription = Class(name="diagram::style::GaugeSectionDescription")
diagram_style_SizeComputationContainerStyleDescription = Class(name="diagram::style::SizeComputationContainerStyleDescription", is_abstract=True)
diagram_style_RoundedCornerStyleDescription = Class(name="diagram::style::RoundedCornerStyleDescription", is_abstract=True)
diagram_style_ContainerStyleDescription = Class(name="diagram::style::ContainerStyleDescription", is_abstract=True)
style_RoundedCornerStyleDescription = Class(name="style::RoundedCornerStyleDescription")
diagram_style_FlatContainerStyleDescription = Class(name="diagram::style::FlatContainerStyleDescription")
style_SizeComputationContainerStyleDescription = Class(name="style::SizeComputationContainerStyleDescription")
style_LabelBorderStyleDescription = Class(name="style::LabelBorderStyleDescription")
diagram_style_ShapeContainerStyleDescription = Class(name="diagram::style::ShapeContainerStyleDescription")
diagram_style_WorkspaceImageDescription = Class(name="diagram::style::WorkspaceImageDescription")
diagram_style_EdgeStyleDescription = Class(name="diagram::style::EdgeStyleDescription")
style_EndLabelStyleDescription = Class(name="style::EndLabelStyleDescription")
style_BeginLabelStyleDescription = Class(name="style::BeginLabelStyleDescription")
style_CenterLabelStyleDescription = Class(name="style::CenterLabelStyleDescription")
diagram_style_HideLabelCapabilityStyleDescription = Class(name="diagram::style::HideLabelCapabilityStyleDescription", is_abstract=True)
diagram_style_BeginLabelStyleDescription = Class(name="diagram::style::BeginLabelStyleDescription")
BasicLabelStyleDescription = Class(name="BasicLabelStyleDescription")
diagram_style_CenterLabelStyleDescription = Class(name="diagram::style::CenterLabelStyleDescription")
diagram_style_EndLabelStyleDescription = Class(name="diagram::style::EndLabelStyleDescription")
diagram_style_BracketEdgeStyleDescription = Class(name="diagram::style::BracketEdgeStyleDescription")
EdgeStyleDescription = Class(name="EdgeStyleDescription")
diagram_tool_ToolSection = Class(name="diagram::tool::ToolSection")
tool_ToolEntry = Class(name="tool::ToolEntry")
tool_PopupMenu = Class(name="tool::PopupMenu")
tool_ToolGroupExtension = Class(name="tool::ToolGroupExtension")
tool_GroupMenu = Class(name="tool::GroupMenu")
diagram_tool_ToolGroup = Class(name="diagram::tool::ToolGroup")
ToolEntry = Class(name="ToolEntry")
diagram_tool_ToolGroupExtension = Class(name="diagram::tool::ToolGroupExtension")
tool_ToolGroup = Class(name="tool::ToolGroup")
diagram_tool_NodeCreationDescription = Class(name="diagram::tool::NodeCreationDescription")
MappingBasedToolDescription = Class(name="MappingBasedToolDescription")
tool_NodeCreationVariable = Class(name="tool::NodeCreationVariable")
tool_ContainerViewVariable = Class(name="tool::ContainerViewVariable")
tool_InitialNodeCreationOperation = Class(name="tool::InitialNodeCreationOperation")
diagram_tool_EdgeCreationDescription = Class(name="diagram::tool::EdgeCreationDescription")
tool_SourceEdgeCreationVariable = Class(name="tool::SourceEdgeCreationVariable")
tool_TargetEdgeCreationVariable = Class(name="tool::TargetEdgeCreationVariable")
tool_SourceEdgeViewCreationVariable = Class(name="tool::SourceEdgeViewCreationVariable")
tool_TargetEdgeViewCreationVariable = Class(name="tool::TargetEdgeViewCreationVariable")
tool_InitEdgeCreationOperation = Class(name="tool::InitEdgeCreationOperation")
diagram_tool_ContainerCreationDescription = Class(name="diagram::tool::ContainerCreationDescription")
diagram_tool_DeleteElementDescription = Class(name="diagram::tool::DeleteElementDescription")
tool_ElementDeleteVariable = Class(name="tool::ElementDeleteVariable")
tool_DeleteHookParameter = Class(name="tool::DeleteHookParameter")
tool_DeleteHook = Class(name="tool::DeleteHook")
diagram_tool_DoubleClickDescription = Class(name="diagram::tool::DoubleClickDescription")
tool_ElementDoubleClickVariable = Class(name="tool::ElementDoubleClickVariable")
diagram_tool_DeleteHook = Class(name="diagram::tool::DeleteHook")
diagram_tool_DeleteHookParameter = Class(name="diagram::tool::DeleteHookParameter")
diagram_tool_ReconnectEdgeDescription = Class(name="diagram::tool::ReconnectEdgeDescription")
tool_ElementSelectVariable = Class(name="tool::ElementSelectVariable")
diagram_tool_RequestDescription = Class(name="diagram::tool::RequestDescription")
AbstractToolDescription = Class(name="AbstractToolDescription")
diagram_tool_DirectEditLabel = Class(name="diagram::tool::DirectEditLabel")
tool_EditMaskVariables = Class(name="tool::EditMaskVariables")
diagram_tool_BehaviorTool = Class(name="diagram::tool::BehaviorTool")
diagram_tool_SourceEdgeCreationVariable = Class(name="diagram::tool::SourceEdgeCreationVariable")
description_AbstractVariable = Class(name="description::AbstractVariable")
tool_VariableContainer = Class(name="tool::VariableContainer")
diagram_tool_SourceEdgeViewCreationVariable = Class(name="diagram::tool::SourceEdgeViewCreationVariable")
diagram_tool_TargetEdgeCreationVariable = Class(name="diagram::tool::TargetEdgeCreationVariable")
diagram_tool_TargetEdgeViewCreationVariable = Class(name="diagram::tool::TargetEdgeViewCreationVariable")
diagram_tool_ElementDoubleClickVariable = Class(name="diagram::tool::ElementDoubleClickVariable")
diagram_tool_NodeCreationVariable = Class(name="diagram::tool::NodeCreationVariable")
diagram_tool_CreateView = Class(name="diagram::tool::CreateView")
ContainerModelOperation = Class(name="ContainerModelOperation")
diagram_tool_CreateEdgeView = Class(name="diagram::tool::CreateEdgeView")
CreateView = Class(name="CreateView")
diagram_tool_Navigation = Class(name="diagram::tool::Navigation")
diagram_tool_DiagramCreationDescription = Class(name="diagram::tool::DiagramCreationDescription")
RepresentationCreationDescription = Class(name="RepresentationCreationDescription")
diagram_tool_DiagramNavigationDescription = Class(name="diagram::tool::DiagramNavigationDescription")
RepresentationNavigationDescription = Class(name="RepresentationNavigationDescription")
diagram_tool_ContainerDropDescription = Class(name="diagram::tool::ContainerDropDescription")
tool_DropContainerVariable = Class(name="tool::DropContainerVariable")
tool_ElementDropVariable = Class(name="tool::ElementDropVariable")
InteractiveVariableDescription = Class(name="InteractiveVariableDescription")
tool_InitialContainerDropOperation = Class(name="tool::InitialContainerDropOperation")
diagram_filter_FilterDescription = Class(name="diagram::filter::FilterDescription", is_abstract=True)
diagram_filter_Filter = Class(name="diagram::filter::Filter", is_abstract=True)
diagram_filter_MappingFilter = Class(name="diagram::filter::MappingFilter")
Filter = Class(name="Filter")
diagram_filter_CompositeFilterDescription = Class(name="diagram::filter::CompositeFilterDescription")
FilterDescription = Class(name="FilterDescription")
filter_Filter = Class(name="filter::Filter")
diagram_filter_VariableFilter = Class(name="diagram::filter::VariableFilter")
diagram_concern_ConcernSet = Class(name="diagram::concern::ConcernSet")
diagram_concern_ConcernDescription = Class(name="diagram::concern::ConcernDescription")

# diagram_DDiagram class attributes and methods
diagram_DDiagram_headerHeight: Property = Property(name="headerHeight", type=IntegerType)
diagram_DDiagram_synchronized: Property = Property(name="synchronized", type=BooleanType)
diagram_DDiagram_isInLayoutingMode: Property = Property(name="isInLayoutingMode", type=BooleanType)
diagram_DDiagram_isInShowingMode: Property = Property(name="isInShowingMode", type=BooleanType)
diagram_DDiagram.attributes={diagram_DDiagram_isInShowingMode, diagram_DDiagram_synchronized, diagram_DDiagram_headerHeight, diagram_DDiagram_isInLayoutingMode}

# DRepresentation class attributes and methods

# DragAndDropTarget class attributes and methods

# diagram_DDiagramElement class attributes and methods
diagram_DDiagramElement_visible: Property = Property(name="visible", type=BooleanType)
diagram_DDiagramElement_tooltipText: Property = Property(name="tooltipText", type=StringType)
diagram_DDiagramElement_m_getParentDiagram: Method = Method(name="getParentDiagram", parameters={}, type=DDiagram)
diagram_DDiagramElement.attributes={diagram_DDiagramElement_visible, diagram_DDiagramElement_tooltipText}
diagram_DDiagramElement.methods={diagram_DDiagramElement_m_getParentDiagram}

# DiagramDescription class attributes and methods

# diagram_DEdge class attributes and methods
diagram_DEdge_size: Property = Property(name="size", type=StringType)
diagram_DEdge_routingStyle: Property = Property(name="routingStyle", type=StringType)
diagram_DEdge_isFold: Property = Property(name="isFold", type=BooleanType)
diagram_DEdge_isMockEdge: Property = Property(name="isMockEdge", type=BooleanType)
diagram_DEdge_beginLabel: Property = Property(name="beginLabel", type=StringType)
diagram_DEdge_endLabel: Property = Property(name="endLabel", type=StringType)
diagram_DEdge_arrangeConstraints: Property = Property(name="arrangeConstraints", type=StringType)
diagram_DEdge.attributes={diagram_DEdge_isFold, diagram_DEdge_size, diagram_DEdge_isMockEdge, diagram_DEdge_beginLabel, diagram_DEdge_routingStyle, diagram_DEdge_arrangeConstraints, diagram_DEdge_endLabel}

# diagram_DNode class attributes and methods
diagram_DNode_width: Property = Property(name="width", type=StringType)
diagram_DNode_height: Property = Property(name="height", type=StringType)
diagram_DNode_labelPosition: Property = Property(name="labelPosition", type=StringType)
diagram_DNode_resizeKind: Property = Property(name="resizeKind", type=StringType)
diagram_DNode.attributes={diagram_DNode_labelPosition, diagram_DNode_resizeKind, diagram_DNode_height, diagram_DNode_width}

# diagram_DNodeListElement class attributes and methods

# diagram_DDiagramElementContainer class attributes and methods
diagram_DDiagramElementContainer_width: Property = Property(name="width", type=StringType)
diagram_DDiagramElementContainer_height: Property = Property(name="height", type=StringType)
diagram_DDiagramElementContainer_m_getNodesFromMapping: Method = Method(name="getNodesFromMapping", parameters={Parameter(name='mapping')}, type=StringType)
diagram_DDiagramElementContainer_m_getContainersFromMapping: Method = Method(name="getContainersFromMapping", parameters={Parameter(name='mapping')}, type=StringType)
diagram_DDiagramElementContainer.attributes={diagram_DDiagramElementContainer_width, diagram_DDiagramElementContainer_height}
diagram_DDiagramElementContainer.methods={diagram_DDiagramElementContainer_m_getContainersFromMapping, diagram_DDiagramElementContainer_m_getNodesFromMapping}

# concern_ConcernDescription class attributes and methods

# filter_FilterDescription class attributes and methods

# AdditionalLayer class attributes and methods

# validation_ValidationRule class attributes and methods

# tool_BehaviorTool class attributes and methods

# diagram_FilterVariableHistory class attributes and methods

# Layer class attributes and methods

# diagram_DSemanticDiagram class attributes and methods

# DDiagram class attributes and methods

# DSemanticDecorator class attributes and methods

# DRepresentationElement class attributes and methods

# diagram_Decoration class attributes and methods

# DiagramElementMapping class attributes and methods

# diagram_GraphicalFilter class attributes and methods

# IdentifiedElement class attributes and methods

# diagram_HideFilter class attributes and methods

# GraphicalFilter class attributes and methods

# diagram_HideLabelFilter class attributes and methods

# diagram_FoldingPointFilter class attributes and methods

# diagram_FoldingFilter class attributes and methods

# diagram_AppliedCompositeFilters class attributes and methods

# AbstractDNode class attributes and methods

# EdgeTarget class attributes and methods

# diagram_NodeStyle class attributes and methods
diagram_NodeStyle_labelPosition: Property = Property(name="labelPosition", type=StringType)
diagram_NodeStyle.attributes={diagram_NodeStyle_labelPosition}

# diagram_Style class attributes and methods

# NodeMapping class attributes and methods

# filter_CompositeFilterDescription class attributes and methods

# diagram_AbsoluteBoundsFilter class attributes and methods
diagram_AbsoluteBoundsFilter_x: Property = Property(name="x", type=StringType)
diagram_AbsoluteBoundsFilter_y: Property = Property(name="y", type=StringType)
diagram_AbsoluteBoundsFilter_height: Property = Property(name="height", type=StringType)
diagram_AbsoluteBoundsFilter_width: Property = Property(name="width", type=StringType)
diagram_AbsoluteBoundsFilter.attributes={diagram_AbsoluteBoundsFilter_width, diagram_AbsoluteBoundsFilter_y, diagram_AbsoluteBoundsFilter_height, diagram_AbsoluteBoundsFilter_x}

# diagram_AbstractDNode class attributes and methods
diagram_AbstractDNode_arrangeConstraints: Property = Property(name="arrangeConstraints", type=StringType)
diagram_AbstractDNode.attributes={diagram_AbstractDNode_arrangeConstraints}

# DDiagramElement class attributes and methods

# diagram_ContainerStyle class attributes and methods

# ContainerMapping class attributes and methods

# diagram_DNodeContainer class attributes and methods
diagram_DNodeContainer_childrenPresentation: Property = Property(name="childrenPresentation", type=StringType)
diagram_DNodeContainer.attributes={diagram_DNodeContainer_childrenPresentation}

# DDiagramElementContainer class attributes and methods

# diagram_DNodeList class attributes and methods

# diagram_EdgeStyle class attributes and methods
diagram_EdgeStyle_lineStyle: Property = Property(name="lineStyle", type=StringType)
diagram_EdgeStyle_sourceArrow: Property = Property(name="sourceArrow", type=StringType)
diagram_EdgeStyle_targetArrow: Property = Property(name="targetArrow", type=StringType)
diagram_EdgeStyle_centered: Property = Property(name="centered", type=StringType)
diagram_EdgeStyle_strokeColor: Property = Property(name="strokeColor", type=StringType)
diagram_EdgeStyle_foldingStyle: Property = Property(name="foldingStyle", type=StringType)
diagram_EdgeStyle_size: Property = Property(name="size", type=StringType)
diagram_EdgeStyle_routingStyle: Property = Property(name="routingStyle", type=StringType)
diagram_EdgeStyle.attributes={diagram_EdgeStyle_size, diagram_EdgeStyle_routingStyle, diagram_EdgeStyle_lineStyle, diagram_EdgeStyle_foldingStyle, diagram_EdgeStyle_strokeColor, diagram_EdgeStyle_sourceArrow, diagram_EdgeStyle_targetArrow, diagram_EdgeStyle_centered}

# diagram_EdgeTarget class attributes and methods

# IEdgeMapping class attributes and methods

# LabelStyle class attributes and methods

# Style class attributes and methods

# BorderedStyle class attributes and methods

# HideLabelCapabilityStyle class attributes and methods

# diagram_Dot class attributes and methods
diagram_Dot_strokeSizeComputationExpression: Property = Property(name="strokeSizeComputationExpression", type=StringType)
diagram_Dot_backgroundColor: Property = Property(name="backgroundColor", type=StringType)
diagram_Dot.attributes={diagram_Dot_backgroundColor, diagram_Dot_strokeSizeComputationExpression}

# NodeStyle class attributes and methods

# diagram_GaugeSection class attributes and methods
diagram_GaugeSection_min: Property = Property(name="min", type=StringType)
diagram_GaugeSection_max: Property = Property(name="max", type=StringType)
diagram_GaugeSection_value: Property = Property(name="value", type=StringType)
diagram_GaugeSection_label: Property = Property(name="label", type=StringType)
diagram_GaugeSection_backgroundColor: Property = Property(name="backgroundColor", type=StringType)
diagram_GaugeSection_foregroundColor: Property = Property(name="foregroundColor", type=StringType)
diagram_GaugeSection.attributes={diagram_GaugeSection_label, diagram_GaugeSection_foregroundColor, diagram_GaugeSection_min, diagram_GaugeSection_value, diagram_GaugeSection_max, diagram_GaugeSection_backgroundColor}

# Customizable class attributes and methods

# diagram_FlatContainerStyle class attributes and methods
diagram_FlatContainerStyle_backgroundStyle: Property = Property(name="backgroundStyle", type=StringType)
diagram_FlatContainerStyle_backgroundColor: Property = Property(name="backgroundColor", type=StringType)
diagram_FlatContainerStyle_foregroundColor: Property = Property(name="foregroundColor", type=StringType)
diagram_FlatContainerStyle.attributes={diagram_FlatContainerStyle_backgroundStyle, diagram_FlatContainerStyle_foregroundColor, diagram_FlatContainerStyle_backgroundColor}

# ContainerStyle class attributes and methods

# diagram_ShapeContainerStyle class attributes and methods
diagram_ShapeContainerStyle_shape: Property = Property(name="shape", type=StringType)
diagram_ShapeContainerStyle_backgroundColor: Property = Property(name="backgroundColor", type=StringType)
diagram_ShapeContainerStyle.attributes={diagram_ShapeContainerStyle_backgroundColor, diagram_ShapeContainerStyle_shape}

# diagram_Square class attributes and methods
diagram_Square_width: Property = Property(name="width", type=StringType)
diagram_Square_height: Property = Property(name="height", type=StringType)
diagram_Square_color: Property = Property(name="color", type=StringType)
diagram_Square.attributes={diagram_Square_color, diagram_Square_height, diagram_Square_width}

# diagram_Ellipse class attributes and methods
diagram_Ellipse_horizontalDiameter: Property = Property(name="horizontalDiameter", type=StringType)
diagram_Ellipse_verticalDiameter: Property = Property(name="verticalDiameter", type=StringType)
diagram_Ellipse_color: Property = Property(name="color", type=StringType)
diagram_Ellipse.attributes={diagram_Ellipse_verticalDiameter, diagram_Ellipse_color, diagram_Ellipse_horizontalDiameter}

# diagram_BundledImage class attributes and methods
diagram_BundledImage_shape: Property = Property(name="shape", type=StringType)
diagram_BundledImage_color: Property = Property(name="color", type=StringType)
diagram_BundledImage_providedShapeID: Property = Property(name="providedShapeID", type=StringType)
diagram_BundledImage.attributes={diagram_BundledImage_color, diagram_BundledImage_shape, diagram_BundledImage_providedShapeID}

# diagram_WorkspaceImage class attributes and methods
diagram_WorkspaceImage_workspacePath: Property = Property(name="workspacePath", type=StringType)
diagram_WorkspaceImage.attributes={diagram_WorkspaceImage_workspacePath}

# diagram_CustomStyle class attributes and methods
diagram_CustomStyle_id: Property = Property(name="id", type=StringType)
diagram_CustomStyle.attributes={diagram_CustomStyle_id}

# diagram_Lozenge class attributes and methods
diagram_Lozenge_width: Property = Property(name="width", type=StringType)
diagram_Lozenge_height: Property = Property(name="height", type=StringType)
diagram_Lozenge_color: Property = Property(name="color", type=StringType)
diagram_Lozenge.attributes={diagram_Lozenge_color, diagram_Lozenge_width, diagram_Lozenge_height}

# diagram_CenterLabelStyle class attributes and methods
diagram_CenterLabelStyle_m_getDescription: Method = Method(name="getDescription", parameters={}, type=StringType)
diagram_CenterLabelStyle_m_setDescription: Method = Method(name="setDescription", parameters={Parameter(name='description')})
diagram_CenterLabelStyle.methods={diagram_CenterLabelStyle_m_getDescription, diagram_CenterLabelStyle_m_setDescription}

# diagram_EndLabelStyle class attributes and methods
diagram_EndLabelStyle_m_getDescription: Method = Method(name="getDescription", parameters={}, type=StringType)
diagram_EndLabelStyle_m_setDescription: Method = Method(name="setDescription", parameters={Parameter(name='description')})
diagram_EndLabelStyle.methods={diagram_EndLabelStyle_m_setDescription, diagram_EndLabelStyle_m_getDescription}

# diagram_BeginLabelStyle class attributes and methods
diagram_BeginLabelStyle_m_getDescription: Method = Method(name="getDescription", parameters={}, type=StringType)
diagram_BeginLabelStyle_m_setDescription: Method = Method(name="setDescription", parameters={Parameter(name='description')})
diagram_BeginLabelStyle.methods={diagram_BeginLabelStyle_m_getDescription, diagram_BeginLabelStyle_m_setDescription}

# diagram_GaugeCompositeStyle class attributes and methods
diagram_GaugeCompositeStyle_alignment: Property = Property(name="alignment", type=StringType)
diagram_GaugeCompositeStyle.attributes={diagram_GaugeCompositeStyle_alignment}

# diagram_BorderedStyle class attributes and methods
diagram_BorderedStyle_borderSize: Property = Property(name="borderSize", type=StringType)
diagram_BorderedStyle_borderSizeComputationExpression: Property = Property(name="borderSizeComputationExpression", type=StringType)
diagram_BorderedStyle_borderColor: Property = Property(name="borderColor", type=StringType)
diagram_BorderedStyle_borderLineStyle: Property = Property(name="borderLineStyle", type=StringType)
diagram_BorderedStyle.attributes={diagram_BorderedStyle_borderColor, diagram_BorderedStyle_borderSize, diagram_BorderedStyle_borderSizeComputationExpression, diagram_BorderedStyle_borderLineStyle}

# diagram_Note class attributes and methods
diagram_Note_color: Property = Property(name="color", type=StringType)
diagram_Note.attributes={diagram_Note_color}

# diagram_VariableValue class attributes and methods

# diagram_CollapseFilter class attributes and methods
diagram_CollapseFilter_width: Property = Property(name="width", type=IntegerType)
diagram_CollapseFilter_height: Property = Property(name="height", type=IntegerType)
diagram_CollapseFilter.attributes={diagram_CollapseFilter_width, diagram_CollapseFilter_height}

# diagram_IndirectlyCollapseFilter class attributes and methods

# CollapseFilter class attributes and methods

# BasicLabelStyle class attributes and methods

# diagram_EObjectVariableValue class attributes and methods

# diagram_BracketEdgeStyle class attributes and methods

# EdgeStyle class attributes and methods

# diagram_ComputedStyleDescriptionRegistry class attributes and methods

# style_StyleDescription class attributes and methods

# diagram_DragAndDropTarget class attributes and methods
diagram_DragAndDropTarget_m_getDragAndDropDescription: Method = Method(name="getDragAndDropDescription", parameters={}, type=StringType)
diagram_DragAndDropTarget.methods={diagram_DragAndDropTarget_m_getDragAndDropDescription}

# diagram_HideLabelCapabilityStyle class attributes and methods
diagram_HideLabelCapabilityStyle_hideLabelByDefault: Property = Property(name="hideLabelByDefault", type=BooleanType)
diagram_HideLabelCapabilityStyle.attributes={diagram_HideLabelCapabilityStyle_hideLabelByDefault}

# diagram_TypedVariableValue class attributes and methods
diagram_TypedVariableValue_value: Property = Property(name="value", type=StringType)
diagram_TypedVariableValue.attributes={diagram_TypedVariableValue_value}

# VariableValue class attributes and methods

# TypedVariable class attributes and methods

# concern_ConcernSet class attributes and methods

# tool_SelectModelElementVariable class attributes and methods

# diagram_EObject class attributes and methods

# diagram_description_DiagramDescription class attributes and methods
diagram_description_DiagramDescription_domainClass: Property = Property(name="domainClass", type=StringType)
diagram_description_DiagramDescription_preconditionExpression: Property = Property(name="preconditionExpression", type=StringType)
diagram_description_DiagramDescription_rootExpression: Property = Property(name="rootExpression", type=StringType)
diagram_description_DiagramDescription_enablePopupBars: Property = Property(name="enablePopupBars", type=BooleanType)
diagram_description_DiagramDescription_m_createDiagram: Method = Method(name="createDiagram", parameters={}, type=StringType)
diagram_description_DiagramDescription.attributes={diagram_description_DiagramDescription_preconditionExpression, diagram_description_DiagramDescription_domainClass, diagram_description_DiagramDescription_enablePopupBars, diagram_description_DiagramDescription_rootExpression}
diagram_description_DiagramDescription.methods={diagram_description_DiagramDescription_m_createDiagram}

# description_DragAndDropTargetDescription class attributes and methods

# description_RepresentationDescription class attributes and methods

# description_PasteTargetDescription class attributes and methods

# EdgeMapping class attributes and methods

# validation_ValidationSet class attributes and methods

# tool_AbstractToolDescription class attributes and methods

# tool_RepresentationCreationDescription class attributes and methods

# Layout class attributes and methods

# tool_InitialOperation class attributes and methods

# EdgeMappingImport class attributes and methods

# tool_DirectEditLabel class attributes and methods

# tool_ToolSection class attributes and methods

# ColorDescription class attributes and methods

# diagram_description_DiagramImportDescription class attributes and methods

# description_RepresentationImportDescription class attributes and methods

# description_DiagramDescription class attributes and methods

# diagram_description_DiagramExtensionDescription class attributes and methods

# RepresentationExtensionDescription class attributes and methods

# diagram_description_DiagramElementMapping class attributes and methods
diagram_description_DiagramElementMapping_preconditionExpression: Property = Property(name="preconditionExpression", type=StringType)
diagram_description_DiagramElementMapping_semanticCandidatesExpression: Property = Property(name="semanticCandidatesExpression", type=StringType)
diagram_description_DiagramElementMapping_createElements: Property = Property(name="createElements", type=BooleanType)
diagram_description_DiagramElementMapping_semanticElements: Property = Property(name="semanticElements", type=StringType)
diagram_description_DiagramElementMapping_synchronizationLock: Property = Property(name="synchronizationLock", type=BooleanType)
diagram_description_DiagramElementMapping.attributes={diagram_description_DiagramElementMapping_preconditionExpression, diagram_description_DiagramElementMapping_semanticCandidatesExpression, diagram_description_DiagramElementMapping_createElements, diagram_description_DiagramElementMapping_semanticElements, diagram_description_DiagramElementMapping_synchronizationLock}

# description_RepresentationElementMapping class attributes and methods

# tool_DeleteElementDescription class attributes and methods

# style_NodeStyleDescription class attributes and methods

# tool_DoubleClickDescription class attributes and methods

# diagram_description_AbstractNodeMapping class attributes and methods
diagram_description_AbstractNodeMapping_domainClass: Property = Property(name="domainClass", type=StringType)
diagram_description_AbstractNodeMapping_m_findDNodeFromEObject: Method = Method(name="findDNodeFromEObject", parameters={Parameter(name='eObject')}, type=DDiagramElement)
diagram_description_AbstractNodeMapping.attributes={diagram_description_AbstractNodeMapping_domainClass}
diagram_description_AbstractNodeMapping.methods={diagram_description_AbstractNodeMapping_m_findDNodeFromEObject}

# description_DiagramElementMapping class attributes and methods

# description_DocumentedElement class attributes and methods

# diagram_description_NodeMapping class attributes and methods

# description_AbstractNodeMapping class attributes and methods

# ConditionalNodeStyleDescription class attributes and methods

# diagram_description_ContainerMapping class attributes and methods
diagram_description_ContainerMapping_childrenPresentation: Property = Property(name="childrenPresentation", type=StringType)
diagram_description_ContainerMapping.attributes={diagram_description_ContainerMapping_childrenPresentation}

# style_ContainerStyleDescription class attributes and methods

# ConditionalContainerStyleDescription class attributes and methods

# diagram_description_NodeMappingImport class attributes and methods

# description_NodeMapping class attributes and methods

# description_AbstractMappingImport class attributes and methods

# diagram_description_ContainerMappingImport class attributes and methods

# description_ContainerMapping class attributes and methods

# diagram_description_EdgeMapping class attributes and methods
diagram_description_EdgeMapping_targetFinderExpression: Property = Property(name="targetFinderExpression", type=StringType)
diagram_description_EdgeMapping_sourceFinderExpression: Property = Property(name="sourceFinderExpression", type=StringType)
diagram_description_EdgeMapping_targetExpression: Property = Property(name="targetExpression", type=StringType)
diagram_description_EdgeMapping_domainClass: Property = Property(name="domainClass", type=StringType)
diagram_description_EdgeMapping_useDomainElement: Property = Property(name="useDomainElement", type=BooleanType)
diagram_description_EdgeMapping_pathExpression: Property = Property(name="pathExpression", type=StringType)
diagram_description_EdgeMapping.attributes={diagram_description_EdgeMapping_targetExpression, diagram_description_EdgeMapping_sourceFinderExpression, diagram_description_EdgeMapping_useDomainElement, diagram_description_EdgeMapping_targetFinderExpression, diagram_description_EdgeMapping_pathExpression, diagram_description_EdgeMapping_domainClass}

# description_IEdgeMapping class attributes and methods

# diagram_description_IEdgeMapping class attributes and methods

# diagram_description_EdgeMappingImport class attributes and methods
diagram_description_EdgeMappingImport_inheritsAncestorFilters: Property = Property(name="inheritsAncestorFilters", type=BooleanType)
diagram_description_EdgeMappingImport.attributes={diagram_description_EdgeMappingImport_inheritsAncestorFilters}

# style_EdgeStyleDescription class attributes and methods

# ConditionalEdgeStyleDescription class attributes and methods

# tool_ReconnectEdgeDescription class attributes and methods

# AbstractNodeMapping class attributes and methods

# LayoutOption class attributes and methods

# description_IdentifiedElement class attributes and methods

# diagram_description_ConditionalNodeStyleDescription class attributes and methods

# ConditionalStyleDescription class attributes and methods

# diagram_description_ConditionalEdgeStyleDescription class attributes and methods

# diagram_description_ConditionalContainerStyleDescription class attributes and methods

# diagram_description_Layout class attributes and methods

# DocumentedElement class attributes and methods

# diagram_description_OrderedTreeLayout class attributes and methods
diagram_description_OrderedTreeLayout_childrenExpression: Property = Property(name="childrenExpression", type=StringType)
diagram_description_OrderedTreeLayout.attributes={diagram_description_OrderedTreeLayout_childrenExpression}

# diagram_description_CompositeLayout class attributes and methods
diagram_description_CompositeLayout_padding: Property = Property(name="padding", type=IntegerType)
diagram_description_CompositeLayout_direction: Property = Property(name="direction", type=StringType)
diagram_description_CompositeLayout.attributes={diagram_description_CompositeLayout_padding, diagram_description_CompositeLayout_direction}

# diagram_description_CustomLayoutConfiguration class attributes and methods
diagram_description_CustomLayoutConfiguration_id: Property = Property(name="id", type=StringType)
diagram_description_CustomLayoutConfiguration_label: Property = Property(name="label", type=StringType)
diagram_description_CustomLayoutConfiguration_description: Property = Property(name="description", type=StringType)
diagram_description_CustomLayoutConfiguration.attributes={diagram_description_CustomLayoutConfiguration_description, diagram_description_CustomLayoutConfiguration_id, diagram_description_CustomLayoutConfiguration_label}

# diagram_description_Layer class attributes and methods
diagram_description_Layer_icon: Property = Property(name="icon", type=StringType)
diagram_description_Layer.attributes={diagram_description_Layer_icon}

# description_EndUserDocumentedElement class attributes and methods

# diagram_description_LayoutOption class attributes and methods
diagram_description_LayoutOption_id: Property = Property(name="id", type=StringType)
diagram_description_LayoutOption_label: Property = Property(name="label", type=StringType)
diagram_description_LayoutOption_description: Property = Property(name="description", type=StringType)
diagram_description_LayoutOption_targets: Property = Property(name="targets", type=StringType)
diagram_description_LayoutOption.attributes={diagram_description_LayoutOption_description, diagram_description_LayoutOption_id, diagram_description_LayoutOption_label, diagram_description_LayoutOption_targets}

# diagram_description_BooleanLayoutOption class attributes and methods
diagram_description_BooleanLayoutOption_value: Property = Property(name="value", type=BooleanType)
diagram_description_BooleanLayoutOption.attributes={diagram_description_BooleanLayoutOption_value}

# diagram_description_StringLayoutOption class attributes and methods
diagram_description_StringLayoutOption_value: Property = Property(name="value", type=StringType)
diagram_description_StringLayoutOption.attributes={diagram_description_StringLayoutOption_value}

# diagram_description_IntegerLayoutOption class attributes and methods
diagram_description_IntegerLayoutOption_value: Property = Property(name="value", type=IntegerType)
diagram_description_IntegerLayoutOption.attributes={diagram_description_IntegerLayoutOption_value}

# diagram_description_DoubleLayoutOption class attributes and methods
diagram_description_DoubleLayoutOption_value: Property = Property(name="value", type=FloatType)
diagram_description_DoubleLayoutOption.attributes={diagram_description_DoubleLayoutOption_value}

# diagram_description_EnumLayoutOption class attributes and methods

# EnumOption class attributes and methods

# EnumLayoutValue class attributes and methods

# diagram_description_EnumSetLayoutOption class attributes and methods

# diagram_description_EnumOption class attributes and methods

# diagram_description_EnumLayoutValue class attributes and methods
diagram_description_EnumLayoutValue_name: Property = Property(name="name", type=StringType)
diagram_description_EnumLayoutValue_description: Property = Property(name="description", type=StringType)
diagram_description_EnumLayoutValue.attributes={diagram_description_EnumLayoutValue_description, diagram_description_EnumLayoutValue_name}

# diagram_description_MappingBasedDecoration class attributes and methods

# DecorationDescription class attributes and methods

# diagram_description_DragAndDropTargetDescription class attributes and methods

# tool_ContainerDropDescription class attributes and methods

# DecorationDescriptionsSet class attributes and methods

# Customization class attributes and methods

# diagram_description_AdditionalLayer class attributes and methods
diagram_description_AdditionalLayer_activeByDefault: Property = Property(name="activeByDefault", type=BooleanType)
diagram_description_AdditionalLayer_optional: Property = Property(name="optional", type=BooleanType)
diagram_description_AdditionalLayer.attributes={diagram_description_AdditionalLayer_optional, diagram_description_AdditionalLayer_activeByDefault}

# diagram_style_BorderedStyleDescription class attributes and methods
diagram_style_BorderedStyleDescription_borderSizeComputationExpression: Property = Property(name="borderSizeComputationExpression", type=StringType)
diagram_style_BorderedStyleDescription_borderLineStyle: Property = Property(name="borderLineStyle", type=StringType)
diagram_style_BorderedStyleDescription.attributes={diagram_style_BorderedStyleDescription_borderLineStyle, diagram_style_BorderedStyleDescription_borderSizeComputationExpression}

# StyleDescription class attributes and methods

# diagram_style_NodeStyleDescription class attributes and methods
diagram_style_NodeStyleDescription_sizeComputationExpression: Property = Property(name="sizeComputationExpression", type=StringType)
diagram_style_NodeStyleDescription_labelPosition: Property = Property(name="labelPosition", type=StringType)
diagram_style_NodeStyleDescription_resizeKind: Property = Property(name="resizeKind", type=StringType)
diagram_style_NodeStyleDescription_forbiddenSides: Property = Property(name="forbiddenSides", type=StringType)
diagram_style_NodeStyleDescription.attributes={diagram_style_NodeStyleDescription_sizeComputationExpression, diagram_style_NodeStyleDescription_resizeKind, diagram_style_NodeStyleDescription_labelPosition, diagram_style_NodeStyleDescription_forbiddenSides}

# style_BorderedStyleDescription class attributes and methods

# style_LabelStyleDescription class attributes and methods

# style_TooltipStyleDescription class attributes and methods

# style_HideLabelCapabilityStyleDescription class attributes and methods

# diagram_style_CustomStyleDescription class attributes and methods
diagram_style_CustomStyleDescription_id: Property = Property(name="id", type=StringType)
diagram_style_CustomStyleDescription.attributes={diagram_style_CustomStyleDescription_id}

# NodeStyleDescription class attributes and methods

# diagram_style_SquareDescription class attributes and methods
diagram_style_SquareDescription_width: Property = Property(name="width", type=StringType)
diagram_style_SquareDescription_height: Property = Property(name="height", type=StringType)
diagram_style_SquareDescription.attributes={diagram_style_SquareDescription_width, diagram_style_SquareDescription_height}

# diagram_style_DotDescription class attributes and methods
diagram_style_DotDescription_strokeSizeComputationExpression: Property = Property(name="strokeSizeComputationExpression", type=StringType)
diagram_style_DotDescription.attributes={diagram_style_DotDescription_strokeSizeComputationExpression}

# diagram_style_LozengeNodeDescription class attributes and methods
diagram_style_LozengeNodeDescription_widthComputationExpression: Property = Property(name="widthComputationExpression", type=StringType)
diagram_style_LozengeNodeDescription_heightComputationExpression: Property = Property(name="heightComputationExpression", type=StringType)
diagram_style_LozengeNodeDescription.attributes={diagram_style_LozengeNodeDescription_heightComputationExpression, diagram_style_LozengeNodeDescription_widthComputationExpression}

# diagram_style_EllipseNodeDescription class attributes and methods
diagram_style_EllipseNodeDescription_horizontalDiameterComputationExpression: Property = Property(name="horizontalDiameterComputationExpression", type=StringType)
diagram_style_EllipseNodeDescription_verticalDiameterComputationExpression: Property = Property(name="verticalDiameterComputationExpression", type=StringType)
diagram_style_EllipseNodeDescription.attributes={diagram_style_EllipseNodeDescription_horizontalDiameterComputationExpression, diagram_style_EllipseNodeDescription_verticalDiameterComputationExpression}

# diagram_style_BundledImageDescription class attributes and methods
diagram_style_BundledImageDescription_shape: Property = Property(name="shape", type=StringType)
diagram_style_BundledImageDescription_providedShapeID: Property = Property(name="providedShapeID", type=StringType)
diagram_style_BundledImageDescription.attributes={diagram_style_BundledImageDescription_providedShapeID, diagram_style_BundledImageDescription_shape}

# diagram_style_NoteDescription class attributes and methods

# diagram_style_GaugeCompositeStyleDescription class attributes and methods
diagram_style_GaugeCompositeStyleDescription_alignment: Property = Property(name="alignment", type=StringType)
diagram_style_GaugeCompositeStyleDescription.attributes={diagram_style_GaugeCompositeStyleDescription_alignment}

# style_GaugeSectionDescription class attributes and methods

# diagram_style_GaugeSectionDescription class attributes and methods
diagram_style_GaugeSectionDescription_minValueExpression: Property = Property(name="minValueExpression", type=StringType)
diagram_style_GaugeSectionDescription_maxValueExpression: Property = Property(name="maxValueExpression", type=StringType)
diagram_style_GaugeSectionDescription_valueExpression: Property = Property(name="valueExpression", type=StringType)
diagram_style_GaugeSectionDescription_label: Property = Property(name="label", type=StringType)
diagram_style_GaugeSectionDescription.attributes={diagram_style_GaugeSectionDescription_label, diagram_style_GaugeSectionDescription_maxValueExpression, diagram_style_GaugeSectionDescription_valueExpression, diagram_style_GaugeSectionDescription_minValueExpression}

# diagram_style_SizeComputationContainerStyleDescription class attributes and methods
diagram_style_SizeComputationContainerStyleDescription_widthComputationExpression: Property = Property(name="widthComputationExpression", type=StringType)
diagram_style_SizeComputationContainerStyleDescription_heightComputationExpression: Property = Property(name="heightComputationExpression", type=StringType)
diagram_style_SizeComputationContainerStyleDescription.attributes={diagram_style_SizeComputationContainerStyleDescription_widthComputationExpression, diagram_style_SizeComputationContainerStyleDescription_heightComputationExpression}

# diagram_style_RoundedCornerStyleDescription class attributes and methods
diagram_style_RoundedCornerStyleDescription_arcWidth: Property = Property(name="arcWidth", type=StringType)
diagram_style_RoundedCornerStyleDescription_arcHeight: Property = Property(name="arcHeight", type=StringType)
diagram_style_RoundedCornerStyleDescription.attributes={diagram_style_RoundedCornerStyleDescription_arcHeight, diagram_style_RoundedCornerStyleDescription_arcWidth}

# diagram_style_ContainerStyleDescription class attributes and methods
diagram_style_ContainerStyleDescription_roundedCorner: Property = Property(name="roundedCorner", type=BooleanType)
diagram_style_ContainerStyleDescription.attributes={diagram_style_ContainerStyleDescription_roundedCorner}

# style_RoundedCornerStyleDescription class attributes and methods

# diagram_style_FlatContainerStyleDescription class attributes and methods
diagram_style_FlatContainerStyleDescription_backgroundStyle: Property = Property(name="backgroundStyle", type=StringType)
diagram_style_FlatContainerStyleDescription.attributes={diagram_style_FlatContainerStyleDescription_backgroundStyle}

# style_SizeComputationContainerStyleDescription class attributes and methods

# style_LabelBorderStyleDescription class attributes and methods

# diagram_style_ShapeContainerStyleDescription class attributes and methods
diagram_style_ShapeContainerStyleDescription_shape: Property = Property(name="shape", type=StringType)
diagram_style_ShapeContainerStyleDescription.attributes={diagram_style_ShapeContainerStyleDescription_shape}

# diagram_style_WorkspaceImageDescription class attributes and methods
diagram_style_WorkspaceImageDescription_workspacePath: Property = Property(name="workspacePath", type=StringType)
diagram_style_WorkspaceImageDescription.attributes={diagram_style_WorkspaceImageDescription_workspacePath}

# diagram_style_EdgeStyleDescription class attributes and methods
diagram_style_EdgeStyleDescription_lineStyle: Property = Property(name="lineStyle", type=StringType)
diagram_style_EdgeStyleDescription_sourceArrow: Property = Property(name="sourceArrow", type=StringType)
diagram_style_EdgeStyleDescription_targetArrow: Property = Property(name="targetArrow", type=StringType)
diagram_style_EdgeStyleDescription_sizeComputationExpression: Property = Property(name="sizeComputationExpression", type=StringType)
diagram_style_EdgeStyleDescription_routingStyle: Property = Property(name="routingStyle", type=StringType)
diagram_style_EdgeStyleDescription_foldingStyle: Property = Property(name="foldingStyle", type=StringType)
diagram_style_EdgeStyleDescription_endsCentering: Property = Property(name="endsCentering", type=StringType)
diagram_style_EdgeStyleDescription.attributes={diagram_style_EdgeStyleDescription_foldingStyle, diagram_style_EdgeStyleDescription_endsCentering, diagram_style_EdgeStyleDescription_targetArrow, diagram_style_EdgeStyleDescription_sizeComputationExpression, diagram_style_EdgeStyleDescription_routingStyle, diagram_style_EdgeStyleDescription_sourceArrow, diagram_style_EdgeStyleDescription_lineStyle}

# style_EndLabelStyleDescription class attributes and methods

# style_BeginLabelStyleDescription class attributes and methods

# style_CenterLabelStyleDescription class attributes and methods

# diagram_style_HideLabelCapabilityStyleDescription class attributes and methods
diagram_style_HideLabelCapabilityStyleDescription_hideLabelByDefault: Property = Property(name="hideLabelByDefault", type=BooleanType)
diagram_style_HideLabelCapabilityStyleDescription.attributes={diagram_style_HideLabelCapabilityStyleDescription_hideLabelByDefault}

# diagram_style_BeginLabelStyleDescription class attributes and methods

# BasicLabelStyleDescription class attributes and methods

# diagram_style_CenterLabelStyleDescription class attributes and methods

# diagram_style_EndLabelStyleDescription class attributes and methods

# diagram_style_BracketEdgeStyleDescription class attributes and methods

# EdgeStyleDescription class attributes and methods

# diagram_tool_ToolSection class attributes and methods
diagram_tool_ToolSection_icon: Property = Property(name="icon", type=StringType)
diagram_tool_ToolSection.attributes={diagram_tool_ToolSection_icon}

# tool_ToolEntry class attributes and methods

# tool_PopupMenu class attributes and methods

# tool_ToolGroupExtension class attributes and methods

# tool_GroupMenu class attributes and methods

# diagram_tool_ToolGroup class attributes and methods

# ToolEntry class attributes and methods

# diagram_tool_ToolGroupExtension class attributes and methods

# tool_ToolGroup class attributes and methods

# diagram_tool_NodeCreationDescription class attributes and methods
diagram_tool_NodeCreationDescription_iconPath: Property = Property(name="iconPath", type=StringType)
diagram_tool_NodeCreationDescription.attributes={diagram_tool_NodeCreationDescription_iconPath}

# MappingBasedToolDescription class attributes and methods

# tool_NodeCreationVariable class attributes and methods

# tool_ContainerViewVariable class attributes and methods

# tool_InitialNodeCreationOperation class attributes and methods

# diagram_tool_EdgeCreationDescription class attributes and methods
diagram_tool_EdgeCreationDescription_iconPath: Property = Property(name="iconPath", type=StringType)
diagram_tool_EdgeCreationDescription_connectionStartPrecondition: Property = Property(name="connectionStartPrecondition", type=StringType)
diagram_tool_EdgeCreationDescription.attributes={diagram_tool_EdgeCreationDescription_iconPath, diagram_tool_EdgeCreationDescription_connectionStartPrecondition}

# tool_SourceEdgeCreationVariable class attributes and methods

# tool_TargetEdgeCreationVariable class attributes and methods

# tool_SourceEdgeViewCreationVariable class attributes and methods

# tool_TargetEdgeViewCreationVariable class attributes and methods

# tool_InitEdgeCreationOperation class attributes and methods

# diagram_tool_ContainerCreationDescription class attributes and methods
diagram_tool_ContainerCreationDescription_iconPath: Property = Property(name="iconPath", type=StringType)
diagram_tool_ContainerCreationDescription.attributes={diagram_tool_ContainerCreationDescription_iconPath}

# diagram_tool_DeleteElementDescription class attributes and methods
diagram_tool_DeleteElementDescription_m_getMappings: Method = Method(name="getMappings", parameters={}, type=StringType)
diagram_tool_DeleteElementDescription.methods={diagram_tool_DeleteElementDescription_m_getMappings}

# tool_ElementDeleteVariable class attributes and methods

# tool_DeleteHookParameter class attributes and methods

# tool_DeleteHook class attributes and methods

# diagram_tool_DoubleClickDescription class attributes and methods

# tool_ElementDoubleClickVariable class attributes and methods

# diagram_tool_DeleteHook class attributes and methods
diagram_tool_DeleteHook_id: Property = Property(name="id", type=StringType)
diagram_tool_DeleteHook.attributes={diagram_tool_DeleteHook_id}

# diagram_tool_DeleteHookParameter class attributes and methods
diagram_tool_DeleteHookParameter_name: Property = Property(name="name", type=StringType)
diagram_tool_DeleteHookParameter_value: Property = Property(name="value", type=StringType)
diagram_tool_DeleteHookParameter.attributes={diagram_tool_DeleteHookParameter_value, diagram_tool_DeleteHookParameter_name}

# diagram_tool_ReconnectEdgeDescription class attributes and methods
diagram_tool_ReconnectEdgeDescription_reconnectionKind: Property = Property(name="reconnectionKind", type=StringType)
diagram_tool_ReconnectEdgeDescription_m_getMappings: Method = Method(name="getMappings", parameters={}, type=StringType)
diagram_tool_ReconnectEdgeDescription.attributes={diagram_tool_ReconnectEdgeDescription_reconnectionKind}
diagram_tool_ReconnectEdgeDescription.methods={diagram_tool_ReconnectEdgeDescription_m_getMappings}

# tool_ElementSelectVariable class attributes and methods

# diagram_tool_RequestDescription class attributes and methods
diagram_tool_RequestDescription_type: Property = Property(name="type", type=StringType)
diagram_tool_RequestDescription.attributes={diagram_tool_RequestDescription_type}

# AbstractToolDescription class attributes and methods

# diagram_tool_DirectEditLabel class attributes and methods
diagram_tool_DirectEditLabel_inputLabelExpression: Property = Property(name="inputLabelExpression", type=StringType)
diagram_tool_DirectEditLabel_m_getMapping: Method = Method(name="getMapping", parameters={}, type=StringType)
diagram_tool_DirectEditLabel.attributes={diagram_tool_DirectEditLabel_inputLabelExpression}
diagram_tool_DirectEditLabel.methods={diagram_tool_DirectEditLabel_m_getMapping}

# tool_EditMaskVariables class attributes and methods

# diagram_tool_BehaviorTool class attributes and methods
diagram_tool_BehaviorTool_domainClass: Property = Property(name="domainClass", type=StringType)
diagram_tool_BehaviorTool.attributes={diagram_tool_BehaviorTool_domainClass}

# diagram_tool_SourceEdgeCreationVariable class attributes and methods

# description_AbstractVariable class attributes and methods

# tool_VariableContainer class attributes and methods

# diagram_tool_SourceEdgeViewCreationVariable class attributes and methods

# diagram_tool_TargetEdgeCreationVariable class attributes and methods

# diagram_tool_TargetEdgeViewCreationVariable class attributes and methods

# diagram_tool_ElementDoubleClickVariable class attributes and methods

# diagram_tool_NodeCreationVariable class attributes and methods

# diagram_tool_CreateView class attributes and methods
diagram_tool_CreateView_containerViewExpression: Property = Property(name="containerViewExpression", type=StringType)
diagram_tool_CreateView_variableName: Property = Property(name="variableName", type=StringType)
diagram_tool_CreateView.attributes={diagram_tool_CreateView_variableName, diagram_tool_CreateView_containerViewExpression}

# ContainerModelOperation class attributes and methods

# diagram_tool_CreateEdgeView class attributes and methods
diagram_tool_CreateEdgeView_sourceExpression: Property = Property(name="sourceExpression", type=StringType)
diagram_tool_CreateEdgeView_targetExpression: Property = Property(name="targetExpression", type=StringType)
diagram_tool_CreateEdgeView.attributes={diagram_tool_CreateEdgeView_sourceExpression, diagram_tool_CreateEdgeView_targetExpression}

# CreateView class attributes and methods

# diagram_tool_Navigation class attributes and methods
diagram_tool_Navigation_createIfNotExistent: Property = Property(name="createIfNotExistent", type=BooleanType)
diagram_tool_Navigation.attributes={diagram_tool_Navigation_createIfNotExistent}

# diagram_tool_DiagramCreationDescription class attributes and methods

# RepresentationCreationDescription class attributes and methods

# diagram_tool_DiagramNavigationDescription class attributes and methods

# RepresentationNavigationDescription class attributes and methods

# diagram_tool_ContainerDropDescription class attributes and methods
diagram_tool_ContainerDropDescription_dragSource: Property = Property(name="dragSource", type=StringType)
diagram_tool_ContainerDropDescription_moveEdges: Property = Property(name="moveEdges", type=BooleanType)
diagram_tool_ContainerDropDescription_m_getContainers: Method = Method(name="getContainers", parameters={}, type=StringType)
diagram_tool_ContainerDropDescription.attributes={diagram_tool_ContainerDropDescription_dragSource, diagram_tool_ContainerDropDescription_moveEdges}
diagram_tool_ContainerDropDescription.methods={diagram_tool_ContainerDropDescription_m_getContainers}

# tool_DropContainerVariable class attributes and methods

# tool_ElementDropVariable class attributes and methods

# InteractiveVariableDescription class attributes and methods

# tool_InitialContainerDropOperation class attributes and methods

# diagram_filter_FilterDescription class attributes and methods
diagram_filter_FilterDescription_m_isVisible: Method = Method(name="isVisible", parameters={Parameter(name='element')}, type=BooleanType)
diagram_filter_FilterDescription.methods={diagram_filter_FilterDescription_m_isVisible}

# diagram_filter_Filter class attributes and methods
diagram_filter_Filter_filterKind: Property = Property(name="filterKind", type=StringType)
diagram_filter_Filter.attributes={diagram_filter_Filter_filterKind}

# diagram_filter_MappingFilter class attributes and methods
diagram_filter_MappingFilter_semanticConditionExpression: Property = Property(name="semanticConditionExpression", type=StringType)
diagram_filter_MappingFilter_viewConditionExpression: Property = Property(name="viewConditionExpression", type=StringType)
diagram_filter_MappingFilter.attributes={diagram_filter_MappingFilter_viewConditionExpression, diagram_filter_MappingFilter_semanticConditionExpression}

# Filter class attributes and methods

# diagram_filter_CompositeFilterDescription class attributes and methods

# FilterDescription class attributes and methods

# filter_Filter class attributes and methods

# diagram_filter_VariableFilter class attributes and methods
diagram_filter_VariableFilter_semanticConditionExpression: Property = Property(name="semanticConditionExpression", type=StringType)
diagram_filter_VariableFilter.attributes={diagram_filter_VariableFilter_semanticConditionExpression}

# diagram_concern_ConcernSet class attributes and methods

# diagram_concern_ConcernDescription class attributes and methods

# Relationships
ownedDiagramElements0: BinaryAssociation = BinaryAssociation(
    name="ownedDiagramElements0",
    ends={
        Property(name="diagram_DDiagramElement", type=diagram_DDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagram", type=diagram_DDiagramElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
diagramElements1: BinaryAssociation = BinaryAssociation(
    name="diagramElements1",
    ends={
        Property(name="diagram_DDiagramElement3", type=diagram_DDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagram2", type=diagram_DDiagramElement, multiplicity=Multiplicity(0, 9999))
    }
)
description4: BinaryAssociation = BinaryAssociation(
    name="description4",
    ends={
        Property(name="DiagramDescription", type=diagram_DDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagram5", type=DiagramDescription, multiplicity=Multiplicity(0, 1))
    }
)
edges6: BinaryAssociation = BinaryAssociation(
    name="edges6",
    ends={
        Property(name="diagram_DEdge", type=diagram_DDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagram7", type=diagram_DEdge, multiplicity=Multiplicity(0, 9999))
    }
)
nodes8: BinaryAssociation = BinaryAssociation(
    name="nodes8",
    ends={
        Property(name="diagram_DNode", type=diagram_DDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagram9", type=diagram_DNode, multiplicity=Multiplicity(0, 9999))
    }
)
containers12: BinaryAssociation = BinaryAssociation(
    name="containers12",
    ends={
        Property(name="diagram_DDiagramElementContainer", type=diagram_DDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagram13", type=diagram_DDiagramElementContainer, multiplicity=Multiplicity(0, 9999))
    }
)
currentConcern14: BinaryAssociation = BinaryAssociation(
    name="currentConcern14",
    ends={
        Property(name="concern_ConcernDescription", type=diagram_DDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagram15", type=concern_ConcernDescription, multiplicity=Multiplicity(0, 1))
    }
)
activatedFilters16: BinaryAssociation = BinaryAssociation(
    name="activatedFilters16",
    ends={
        Property(name="filter_FilterDescription", type=diagram_DDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagram17", type=filter_FilterDescription, multiplicity=Multiplicity(0, 9999))
    }
)
activatedTransientLayers18: BinaryAssociation = BinaryAssociation(
    name="activatedTransientLayers18",
    ends={
        Property(name="AdditionalLayer", type=diagram_DDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagram19", type=AdditionalLayer, multiplicity=Multiplicity(0, 9999))
    }
)
allFilters20: BinaryAssociation = BinaryAssociation(
    name="allFilters20",
    ends={
        Property(name="filter_FilterDescription22", type=diagram_DDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagram21", type=filter_FilterDescription, multiplicity=Multiplicity(0, 9999))
    }
)
activatedRules23: BinaryAssociation = BinaryAssociation(
    name="activatedRules23",
    ends={
        Property(name="validation_ValidationRule", type=diagram_DDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagram24", type=validation_ValidationRule, multiplicity=Multiplicity(0, 9999))
    }
)
activateBehaviors25: BinaryAssociation = BinaryAssociation(
    name="activateBehaviors25",
    ends={
        Property(name="tool_BehaviorTool", type=diagram_DDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagram26", type=tool_BehaviorTool, multiplicity=Multiplicity(0, 9999))
    }
)
filterVariableHistory27: BinaryAssociation = BinaryAssociation(
    name="filterVariableHistory27",
    ends={
        Property(name="diagram_FilterVariableHistory", type=diagram_DDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagram28", type=diagram_FilterVariableHistory, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
nodeListElements10: BinaryAssociation = BinaryAssociation(
    name="nodeListElements10",
    ends={
        Property(name="diagram_DNodeListElement", type=diagram_DDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagram11", type=diagram_DNodeListElement, multiplicity=Multiplicity(0, 9999))
    }
)
parentLayers34: BinaryAssociation = BinaryAssociation(
    name="parentLayers34",
    ends={
        Property(name="Layer36", type=diagram_DDiagramElement, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagramElement35", type=Layer, multiplicity=Multiplicity(0, 9999))
    }
)
decorations37: BinaryAssociation = BinaryAssociation(
    name="decorations37",
    ends={
        Property(name="diagram_Decoration", type=diagram_DDiagramElement, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagramElement38", type=diagram_Decoration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transientDecorations39: BinaryAssociation = BinaryAssociation(
    name="transientDecorations39",
    ends={
        Property(name="diagram_Decoration41", type=diagram_DDiagramElement, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagramElement40", type=diagram_Decoration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
diagramElementMapping42: BinaryAssociation = BinaryAssociation(
    name="diagramElementMapping42",
    ends={
        Property(name="DiagramElementMapping", type=diagram_DDiagramElement, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagramElement43", type=DiagramElementMapping, multiplicity=Multiplicity(0, 1))
    }
)
graphicalFilters44: BinaryAssociation = BinaryAssociation(
    name="graphicalFilters44",
    ends={
        Property(name="diagram_GraphicalFilter", type=diagram_DDiagramElement, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagramElement45", type=diagram_GraphicalFilter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activatedLayers29: BinaryAssociation = BinaryAssociation(
    name="activatedLayers29",
    ends={
        Property(name="Layer", type=diagram_DDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagram30", type=Layer, multiplicity=Multiplicity(0, 9999))
    }
)
hiddenElements31: BinaryAssociation = BinaryAssociation(
    name="hiddenElements31",
    ends={
        Property(name="diagram_DDiagramElement33", type=diagram_DDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagram32", type=diagram_DDiagramElement, multiplicity=Multiplicity(0, 9999))
    }
)
ownedStyle49: BinaryAssociation = BinaryAssociation(
    name="ownedStyle49",
    ends={
        Property(name="diagram_NodeStyle", type=diagram_DNode, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DNode50", type=diagram_NodeStyle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
originalStyle51: BinaryAssociation = BinaryAssociation(
    name="originalStyle51",
    ends={
        Property(name="diagram_Style", type=diagram_DNode, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DNode52", type=diagram_Style, multiplicity=Multiplicity(0, 1))
    }
)
actualMapping53: BinaryAssociation = BinaryAssociation(
    name="actualMapping53",
    ends={
        Property(name="NodeMapping", type=diagram_DNode, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DNode54", type=NodeMapping, multiplicity=Multiplicity(1, 1))
    }
)
candidatesMapping55: BinaryAssociation = BinaryAssociation(
    name="candidatesMapping55",
    ends={
        Property(name="NodeMapping57", type=diagram_DNode, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DNode56", type=NodeMapping, multiplicity=Multiplicity(0, 9999))
    }
)
compositeFilterDescriptions46: BinaryAssociation = BinaryAssociation(
    name="compositeFilterDescriptions46",
    ends={
        Property(name="filter_CompositeFilterDescription", type=diagram_AppliedCompositeFilters, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_AppliedCompositeFilters", type=filter_CompositeFilterDescription, multiplicity=Multiplicity(0, 9999))
    }
)
ownedBorderedNodes47: BinaryAssociation = BinaryAssociation(
    name="ownedBorderedNodes47",
    ends={
        Property(name="diagram_DNode48", type=diagram_AbstractDNode, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_AbstractDNode", type=diagram_DNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containers62: BinaryAssociation = BinaryAssociation(
    name="containers62",
    ends={
        Property(name="diagram_DDiagramElementContainer63", type=diagram_DDiagramElementContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagramElementContainer61", type=diagram_DDiagramElementContainer, multiplicity=Multiplicity(0, 9999))
    }
)
elements64: BinaryAssociation = BinaryAssociation(
    name="elements64",
    ends={
        Property(name="diagram_DDiagramElement66", type=diagram_DDiagramElementContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagramElementContainer65", type=diagram_DDiagramElement, multiplicity=Multiplicity(0, 9999))
    }
)
ownedStyle67: BinaryAssociation = BinaryAssociation(
    name="ownedStyle67",
    ends={
        Property(name="diagram_ContainerStyle", type=diagram_DDiagramElementContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagramElementContainer68", type=diagram_ContainerStyle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
originalStyle69: BinaryAssociation = BinaryAssociation(
    name="originalStyle69",
    ends={
        Property(name="diagram_Style71", type=diagram_DDiagramElementContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagramElementContainer70", type=diagram_Style, multiplicity=Multiplicity(0, 1))
    }
)
actualMapping72: BinaryAssociation = BinaryAssociation(
    name="actualMapping72",
    ends={
        Property(name="ContainerMapping", type=diagram_DDiagramElementContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagramElementContainer73", type=ContainerMapping, multiplicity=Multiplicity(1, 1))
    }
)
candidatesMapping74: BinaryAssociation = BinaryAssociation(
    name="candidatesMapping74",
    ends={
        Property(name="ContainerMapping76", type=diagram_DDiagramElementContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagramElementContainer75", type=ContainerMapping, multiplicity=Multiplicity(0, 9999))
    }
)
ownedDiagramElements77: BinaryAssociation = BinaryAssociation(
    name="ownedDiagramElements77",
    ends={
        Property(name="diagram_DDiagramElement78", type=diagram_DNodeContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DNodeContainer", type=diagram_DDiagramElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodes58: BinaryAssociation = BinaryAssociation(
    name="nodes58",
    ends={
        Property(name="diagram_DNode60", type=diagram_DDiagramElementContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagramElementContainer59", type=diagram_DNode, multiplicity=Multiplicity(0, 9999))
    }
)
originalStyle84: BinaryAssociation = BinaryAssociation(
    name="originalStyle84",
    ends={
        Property(name="diagram_Style86", type=diagram_DNodeListElement, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DNodeListElement85", type=diagram_Style, multiplicity=Multiplicity(0, 1))
    }
)
actualMapping87: BinaryAssociation = BinaryAssociation(
    name="actualMapping87",
    ends={
        Property(name="NodeMapping89", type=diagram_DNodeListElement, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DNodeListElement88", type=NodeMapping, multiplicity=Multiplicity(1, 1))
    }
)
candidatesMapping90: BinaryAssociation = BinaryAssociation(
    name="candidatesMapping90",
    ends={
        Property(name="NodeMapping92", type=diagram_DNodeListElement, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DNodeListElement91", type=NodeMapping, multiplicity=Multiplicity(0, 9999))
    }
)
ownedStyle93: BinaryAssociation = BinaryAssociation(
    name="ownedStyle93",
    ends={
        Property(name="diagram_EdgeStyle", type=diagram_DEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DEdge94", type=diagram_EdgeStyle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sourceNode95: BinaryAssociation = BinaryAssociation(
    name="sourceNode95",
    ends={
        Property(name="EdgeTarget", type=diagram_DEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingEdges", type=diagram_EdgeTarget, multiplicity=Multiplicity(1, 1))
    }
)
targetNode96: BinaryAssociation = BinaryAssociation(
    name="targetNode96",
    ends={
        Property(name="EdgeTarget97", type=diagram_DEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingEdges", type=diagram_EdgeTarget, multiplicity=Multiplicity(1, 1))
    }
)
actualMapping98: BinaryAssociation = BinaryAssociation(
    name="actualMapping98",
    ends={
        Property(name="IEdgeMapping", type=diagram_DEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DEdge99", type=IEdgeMapping, multiplicity=Multiplicity(1, 1))
    }
)
ownedElements79: BinaryAssociation = BinaryAssociation(
    name="ownedElements79",
    ends={
        Property(name="diagram_DNodeListElement80", type=diagram_DNodeList, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DNodeList", type=diagram_DNodeListElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedStyle81: BinaryAssociation = BinaryAssociation(
    name="ownedStyle81",
    ends={
        Property(name="diagram_NodeStyle83", type=diagram_DNodeListElement, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DNodeListElement82", type=diagram_NodeStyle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
originalStyle100: BinaryAssociation = BinaryAssociation(
    name="originalStyle100",
    ends={
        Property(name="diagram_Style102", type=diagram_DEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DEdge101", type=diagram_Style, multiplicity=Multiplicity(0, 1))
    }
)
path103: BinaryAssociation = BinaryAssociation(
    name="path103",
    ends={
        Property(name="diagram_EdgeTarget", type=diagram_DEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DEdge104", type=diagram_EdgeTarget, multiplicity=Multiplicity(0, 9999))
    }
)
outgoingEdges105: BinaryAssociation = BinaryAssociation(
    name="outgoingEdges105",
    ends={
        Property(name="DEdge", type=diagram_EdgeTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceNode", type=diagram_DEdge, multiplicity=Multiplicity(0, 9999))
    }
)
incomingEdges106: BinaryAssociation = BinaryAssociation(
    name="incomingEdges106",
    ends={
        Property(name="DEdge107", type=diagram_EdgeTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="targetNode", type=diagram_DEdge, multiplicity=Multiplicity(0, 9999))
    }
)
beginLabelStyle108: BinaryAssociation = BinaryAssociation(
    name="beginLabelStyle108",
    ends={
        Property(name="diagram_BeginLabelStyle", type=diagram_EdgeStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_EdgeStyle109", type=diagram_BeginLabelStyle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
centerLabelStyle110: BinaryAssociation = BinaryAssociation(
    name="centerLabelStyle110",
    ends={
        Property(name="diagram_CenterLabelStyle", type=diagram_EdgeStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_EdgeStyle111", type=diagram_CenterLabelStyle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
endLabelStyle112: BinaryAssociation = BinaryAssociation(
    name="endLabelStyle112",
    ends={
        Property(name="diagram_EndLabelStyle", type=diagram_EdgeStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_EdgeStyle113", type=diagram_EndLabelStyle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sections114: BinaryAssociation = BinaryAssociation(
    name="sections114",
    ends={
        Property(name="diagram_GaugeSection", type=diagram_GaugeCompositeStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_GaugeCompositeStyle", type=diagram_GaugeSection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedValues115: BinaryAssociation = BinaryAssociation(
    name="ownedValues115",
    ends={
        Property(name="diagram_VariableValue", type=diagram_FilterVariableHistory, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_FilterVariableHistory116", type=diagram_VariableValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
computedStyleDescriptions117: BinaryAssociation = BinaryAssociation(
    name="computedStyleDescriptions117",
    ends={
        Property(name="style_StyleDescription", type=diagram_ComputedStyleDescriptionRegistry, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_ComputedStyleDescriptionRegistry", type=style_StyleDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variableDefinition118: BinaryAssociation = BinaryAssociation(
    name="variableDefinition118",
    ends={
        Property(name="TypedVariable", type=diagram_TypedVariableValue, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_TypedVariableValue", type=TypedVariable, multiplicity=Multiplicity(1, 1))
    }
)
concerns128: BinaryAssociation = BinaryAssociation(
    name="concerns128",
    ends={
        Property(name="concern_ConcernSet", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription129", type=concern_ConcernSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variableDefinition119: BinaryAssociation = BinaryAssociation(
    name="variableDefinition119",
    ends={
        Property(name="tool_SelectModelElementVariable", type=diagram_EObjectVariableValue, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_EObjectVariableValue", type=tool_SelectModelElementVariable, multiplicity=Multiplicity(1, 1))
    }
)
modelElement120: BinaryAssociation = BinaryAssociation(
    name="modelElement120",
    ends={
        Property(name="diagram_EObject", type=diagram_EObjectVariableValue, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_EObjectVariableValue121", type=diagram_EObject, multiplicity=Multiplicity(1, 1))
    }
)
filters122: BinaryAssociation = BinaryAssociation(
    name="filters122",
    ends={
        Property(name="filter_FilterDescription123", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription", type=filter_FilterDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allEdgeMappings124: BinaryAssociation = BinaryAssociation(
    name="allEdgeMappings124",
    ends={
        Property(name="EdgeMapping", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription125", type=EdgeMapping, multiplicity=Multiplicity(0, 9999))
    }
)
validationSet126: BinaryAssociation = BinaryAssociation(
    name="validationSet126",
    ends={
        Property(name="validation_ValidationSet", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription127", type=validation_ValidationSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
layout137: BinaryAssociation = BinaryAssociation(
    name="layout137",
    ends={
        Property(name="Layout", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription138", type=Layout, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
allTools130: BinaryAssociation = BinaryAssociation(
    name="allTools130",
    ends={
        Property(name="tool_AbstractToolDescription", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription131", type=tool_AbstractToolDescription, multiplicity=Multiplicity(0, 9999))
    }
)
defaultConcern132: BinaryAssociation = BinaryAssociation(
    name="defaultConcern132",
    ends={
        Property(name="concern_ConcernDescription134", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription133", type=concern_ConcernDescription, multiplicity=Multiplicity(0, 1))
    }
)
init135: BinaryAssociation = BinaryAssociation(
    name="init135",
    ends={
        Property(name="tool_RepresentationCreationDescription", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription136", type=tool_RepresentationCreationDescription, multiplicity=Multiplicity(0, 1))
    }
)
diagramInitialisation139: BinaryAssociation = BinaryAssociation(
    name="diagramInitialisation139",
    ends={
        Property(name="tool_InitialOperation", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription140", type=tool_InitialOperation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultLayer141: BinaryAssociation = BinaryAssociation(
    name="defaultLayer141",
    ends={
        Property(name="Layer143", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription142", type=Layer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
additionalLayers144: BinaryAssociation = BinaryAssociation(
    name="additionalLayers144",
    ends={
        Property(name="AdditionalLayer146", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription145", type=AdditionalLayer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodeMappings147: BinaryAssociation = BinaryAssociation(
    name="nodeMappings147",
    ends={
        Property(name="NodeMapping149", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription148", type=NodeMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edgeMappings150: BinaryAssociation = BinaryAssociation(
    name="edgeMappings150",
    ends={
        Property(name="EdgeMapping152", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription151", type=EdgeMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edgeMappingImports153: BinaryAssociation = BinaryAssociation(
    name="edgeMappingImports153",
    ends={
        Property(name="EdgeMappingImport", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription154", type=EdgeMappingImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containerMappings155: BinaryAssociation = BinaryAssociation(
    name="containerMappings155",
    ends={
        Property(name="ContainerMapping157", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription156", type=ContainerMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
labelDirectEdit179: BinaryAssociation = BinaryAssociation(
    name="labelDirectEdit179",
    ends={
        Property(name="tool_DirectEditLabel", type=diagram_description_DiagramElementMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramElementMapping180", type=tool_DirectEditLabel, multiplicity=Multiplicity(0, 1))
    }
)
reusedMappings158: BinaryAssociation = BinaryAssociation(
    name="reusedMappings158",
    ends={
        Property(name="DiagramElementMapping160", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription159", type=DiagramElementMapping, multiplicity=Multiplicity(0, 9999))
    }
)
toolSection161: BinaryAssociation = BinaryAssociation(
    name="toolSection161",
    ends={
        Property(name="tool_ToolSection", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription162", type=tool_ToolSection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
reusedTools163: BinaryAssociation = BinaryAssociation(
    name="reusedTools163",
    ends={
        Property(name="tool_AbstractToolDescription165", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription164", type=tool_AbstractToolDescription, multiplicity=Multiplicity(0, 9999))
    }
)
backgroundColor166: BinaryAssociation = BinaryAssociation(
    name="backgroundColor166",
    ends={
        Property(name="ColorDescription", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription167", type=ColorDescription, multiplicity=Multiplicity(0, 1))
    }
)
importedDiagram168: BinaryAssociation = BinaryAssociation(
    name="importedDiagram168",
    ends={
        Property(name="DiagramDescription169", type=diagram_description_DiagramImportDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramImportDescription", type=DiagramDescription, multiplicity=Multiplicity(0, 1))
    }
)
layers170: BinaryAssociation = BinaryAssociation(
    name="layers170",
    ends={
        Property(name="AdditionalLayer171", type=diagram_description_DiagramExtensionDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramExtensionDescription", type=AdditionalLayer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
validationSet172: BinaryAssociation = BinaryAssociation(
    name="validationSet172",
    ends={
        Property(name="validation_ValidationSet174", type=diagram_description_DiagramExtensionDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramExtensionDescription173", type=validation_ValidationSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
concerns175: BinaryAssociation = BinaryAssociation(
    name="concerns175",
    ends={
        Property(name="concern_ConcernSet177", type=diagram_description_DiagramExtensionDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramExtensionDescription176", type=concern_ConcernSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
deletionDescription178: BinaryAssociation = BinaryAssociation(
    name="deletionDescription178",
    ends={
        Property(name="tool_DeleteElementDescription", type=diagram_description_DiagramElementMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramElementMapping", type=tool_DeleteElementDescription, multiplicity=Multiplicity(0, 1))
    }
)
style187: BinaryAssociation = BinaryAssociation(
    name="style187",
    ends={
        Property(name="style_NodeStyleDescription", type=diagram_description_NodeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_NodeMapping", type=style_NodeStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
doubleClickDescription181: BinaryAssociation = BinaryAssociation(
    name="doubleClickDescription181",
    ends={
        Property(name="description", type=diagram_description_DiagramElementMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="tool", type=tool_DoubleClickDescription, multiplicity=Multiplicity(0, 1))
    }
)
borderedNodeMappings182: BinaryAssociation = BinaryAssociation(
    name="borderedNodeMappings182",
    ends={
        Property(name="NodeMapping183", type=diagram_description_AbstractNodeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_AbstractNodeMapping", type=NodeMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reusedBorderedNodeMappings184: BinaryAssociation = BinaryAssociation(
    name="reusedBorderedNodeMappings184",
    ends={
        Property(name="NodeMapping186", type=diagram_description_AbstractNodeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_AbstractNodeMapping185", type=NodeMapping, multiplicity=Multiplicity(0, 9999))
    }
)
sourceMapping209: BinaryAssociation = BinaryAssociation(
    name="sourceMapping209",
    ends={
        Property(name="DiagramElementMapping210", type=diagram_description_EdgeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_EdgeMapping", type=DiagramElementMapping, multiplicity=Multiplicity(1, 9999))
    }
)
conditionnalStyles188: BinaryAssociation = BinaryAssociation(
    name="conditionnalStyles188",
    ends={
        Property(name="ConditionalNodeStyleDescription", type=diagram_description_NodeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_NodeMapping189", type=ConditionalNodeStyleDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subNodeMappings190: BinaryAssociation = BinaryAssociation(
    name="subNodeMappings190",
    ends={
        Property(name="NodeMapping191", type=diagram_description_ContainerMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_ContainerMapping", type=NodeMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reusedNodeMappings192: BinaryAssociation = BinaryAssociation(
    name="reusedNodeMappings192",
    ends={
        Property(name="NodeMapping194", type=diagram_description_ContainerMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_ContainerMapping193", type=NodeMapping, multiplicity=Multiplicity(0, 9999))
    }
)
subContainerMappings195: BinaryAssociation = BinaryAssociation(
    name="subContainerMappings195",
    ends={
        Property(name="ContainerMapping197", type=diagram_description_ContainerMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_ContainerMapping196", type=ContainerMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reusedContainerMappings198: BinaryAssociation = BinaryAssociation(
    name="reusedContainerMappings198",
    ends={
        Property(name="ContainerMapping200", type=diagram_description_ContainerMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_ContainerMapping199", type=ContainerMapping, multiplicity=Multiplicity(0, 9999))
    }
)
style201: BinaryAssociation = BinaryAssociation(
    name="style201",
    ends={
        Property(name="style_ContainerStyleDescription", type=diagram_description_ContainerMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_ContainerMapping202", type=style_ContainerStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditionnalStyles203: BinaryAssociation = BinaryAssociation(
    name="conditionnalStyles203",
    ends={
        Property(name="ConditionalContainerStyleDescription", type=diagram_description_ContainerMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_ContainerMapping204", type=ConditionalContainerStyleDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedMapping205: BinaryAssociation = BinaryAssociation(
    name="importedMapping205",
    ends={
        Property(name="NodeMapping206", type=diagram_description_NodeMappingImport, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_NodeMappingImport", type=NodeMapping, multiplicity=Multiplicity(1, 1))
    }
)
importedMapping207: BinaryAssociation = BinaryAssociation(
    name="importedMapping207",
    ends={
        Property(name="ContainerMapping208", type=diagram_description_ContainerMappingImport, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_ContainerMappingImport", type=ContainerMapping, multiplicity=Multiplicity(1, 1))
    }
)
targetMapping211: BinaryAssociation = BinaryAssociation(
    name="targetMapping211",
    ends={
        Property(name="DiagramElementMapping213", type=diagram_description_EdgeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_EdgeMapping212", type=DiagramElementMapping, multiplicity=Multiplicity(1, 9999))
    }
)
style214: BinaryAssociation = BinaryAssociation(
    name="style214",
    ends={
        Property(name="style_EdgeStyleDescription", type=diagram_description_EdgeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_EdgeMapping215", type=style_EdgeStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditionnalStyles216: BinaryAssociation = BinaryAssociation(
    name="conditionnalStyles216",
    ends={
        Property(name="ConditionalEdgeStyleDescription", type=diagram_description_EdgeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_EdgeMapping217", type=ConditionalEdgeStyleDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reconnections218: BinaryAssociation = BinaryAssociation(
    name="reconnections218",
    ends={
        Property(name="tool_ReconnectEdgeDescription", type=diagram_description_EdgeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_EdgeMapping219", type=tool_ReconnectEdgeDescription, multiplicity=Multiplicity(0, 9999))
    }
)
pathNodeMapping220: BinaryAssociation = BinaryAssociation(
    name="pathNodeMapping220",
    ends={
        Property(name="AbstractNodeMapping", type=diagram_description_EdgeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_EdgeMapping221", type=AbstractNodeMapping, multiplicity=Multiplicity(0, 9999))
    }
)
importedMapping222: BinaryAssociation = BinaryAssociation(
    name="importedMapping222",
    ends={
        Property(name="IEdgeMapping223", type=diagram_description_EdgeMappingImport, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_EdgeMappingImport", type=IEdgeMapping, multiplicity=Multiplicity(1, 1))
    }
)
conditionnalStyles224: BinaryAssociation = BinaryAssociation(
    name="conditionnalStyles224",
    ends={
        Property(name="ConditionalEdgeStyleDescription226", type=diagram_description_EdgeMappingImport, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_EdgeMappingImport225", type=ConditionalEdgeStyleDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
style227: BinaryAssociation = BinaryAssociation(
    name="style227",
    ends={
        Property(name="style_NodeStyleDescription228", type=diagram_description_ConditionalNodeStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_ConditionalNodeStyleDescription", type=style_NodeStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
style229: BinaryAssociation = BinaryAssociation(
    name="style229",
    ends={
        Property(name="style_EdgeStyleDescription230", type=diagram_description_ConditionalEdgeStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_ConditionalEdgeStyleDescription", type=style_EdgeStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
style231: BinaryAssociation = BinaryAssociation(
    name="style231",
    ends={
        Property(name="style_ContainerStyleDescription232", type=diagram_description_ConditionalContainerStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_ConditionalContainerStyleDescription", type=style_ContainerStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nodeMapping233: BinaryAssociation = BinaryAssociation(
    name="nodeMapping233",
    ends={
        Property(name="AbstractNodeMapping234", type=diagram_description_OrderedTreeLayout, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_OrderedTreeLayout", type=AbstractNodeMapping, multiplicity=Multiplicity(1, 9999))
    }
)
mappings241: BinaryAssociation = BinaryAssociation(
    name="mappings241",
    ends={
        Property(name="diagram_description_MappingBasedDecoration", type=DiagramElementMapping, multiplicity=Multiplicity(1, 9999)),
        Property(name="DiagramElementMapping242", type=diagram_description_MappingBasedDecoration, multiplicity=Multiplicity(1, 1))
    }
)
layoutOptions235: BinaryAssociation = BinaryAssociation(
    name="layoutOptions235",
    ends={
        Property(name="LayoutOption", type=diagram_description_CustomLayoutConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_CustomLayoutConfiguration", type=LayoutOption, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value236: BinaryAssociation = BinaryAssociation(
    name="value236",
    ends={
        Property(name="EnumLayoutValue", type=diagram_description_EnumLayoutOption, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_EnumLayoutOption", type=EnumLayoutValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
values237: BinaryAssociation = BinaryAssociation(
    name="values237",
    ends={
        Property(name="EnumLayoutValue238", type=diagram_description_EnumSetLayoutOption, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_EnumSetLayoutOption", type=EnumLayoutValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
choices239: BinaryAssociation = BinaryAssociation(
    name="choices239",
    ends={
        Property(name="EnumLayoutValue240", type=diagram_description_EnumOption, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_EnumOption", type=EnumLayoutValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dropDescriptions270: BinaryAssociation = BinaryAssociation(
    name="dropDescriptions270",
    ends={
        Property(name="tool_ContainerDropDescription", type=diagram_description_DragAndDropTargetDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DragAndDropTargetDescription", type=tool_ContainerDropDescription, multiplicity=Multiplicity(0, 9999))
    }
)
nodeMappings243: BinaryAssociation = BinaryAssociation(
    name="nodeMappings243",
    ends={
        Property(name="NodeMapping244", type=diagram_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_Layer", type=NodeMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edgeMappings245: BinaryAssociation = BinaryAssociation(
    name="edgeMappings245",
    ends={
        Property(name="EdgeMapping247", type=diagram_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_Layer246", type=EdgeMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edgeMappingImports248: BinaryAssociation = BinaryAssociation(
    name="edgeMappingImports248",
    ends={
        Property(name="EdgeMappingImport250", type=diagram_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_Layer249", type=EdgeMappingImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containerMappings251: BinaryAssociation = BinaryAssociation(
    name="containerMappings251",
    ends={
        Property(name="ContainerMapping253", type=diagram_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_Layer252", type=ContainerMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reusedMappings254: BinaryAssociation = BinaryAssociation(
    name="reusedMappings254",
    ends={
        Property(name="DiagramElementMapping256", type=diagram_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_Layer255", type=DiagramElementMapping, multiplicity=Multiplicity(0, 9999))
    }
)
allTools257: BinaryAssociation = BinaryAssociation(
    name="allTools257",
    ends={
        Property(name="tool_AbstractToolDescription259", type=diagram_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_Layer258", type=tool_AbstractToolDescription, multiplicity=Multiplicity(0, 9999))
    }
)
toolSections260: BinaryAssociation = BinaryAssociation(
    name="toolSections260",
    ends={
        Property(name="tool_ToolSection262", type=diagram_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_Layer261", type=tool_ToolSection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reusedTools263: BinaryAssociation = BinaryAssociation(
    name="reusedTools263",
    ends={
        Property(name="tool_AbstractToolDescription265", type=diagram_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_Layer264", type=tool_AbstractToolDescription, multiplicity=Multiplicity(0, 9999))
    }
)
decorationDescriptionsSet266: BinaryAssociation = BinaryAssociation(
    name="decorationDescriptionsSet266",
    ends={
        Property(name="DecorationDescriptionsSet", type=diagram_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_Layer267", type=DecorationDescriptionsSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
customization268: BinaryAssociation = BinaryAssociation(
    name="customization268",
    ends={
        Property(name="Customization", type=diagram_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_Layer269", type=Customization, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
borderColor271: BinaryAssociation = BinaryAssociation(
    name="borderColor271",
    ends={
        Property(name="ColorDescription272", type=diagram_style_BorderedStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_BorderedStyleDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
color281: BinaryAssociation = BinaryAssociation(
    name="color281",
    ends={
        Property(name="diagram_style_NoteDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="ColorDescription282", type=diagram_style_NoteDescription, multiplicity=Multiplicity(1, 1))
    }
)
color273: BinaryAssociation = BinaryAssociation(
    name="color273",
    ends={
        Property(name="ColorDescription274", type=diagram_style_SquareDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_SquareDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
color275: BinaryAssociation = BinaryAssociation(
    name="color275",
    ends={
        Property(name="ColorDescription276", type=diagram_style_LozengeNodeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_LozengeNodeDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
color277: BinaryAssociation = BinaryAssociation(
    name="color277",
    ends={
        Property(name="ColorDescription278", type=diagram_style_EllipseNodeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_EllipseNodeDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
color279: BinaryAssociation = BinaryAssociation(
    name="color279",
    ends={
        Property(name="ColorDescription280", type=diagram_style_BundledImageDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_BundledImageDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
backgroundColor283: BinaryAssociation = BinaryAssociation(
    name="backgroundColor283",
    ends={
        Property(name="ColorDescription284", type=diagram_style_DotDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_DotDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
sections285: BinaryAssociation = BinaryAssociation(
    name="sections285",
    ends={
        Property(name="style_GaugeSectionDescription", type=diagram_style_GaugeCompositeStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_GaugeCompositeStyleDescription", type=style_GaugeSectionDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
backgroundColor286: BinaryAssociation = BinaryAssociation(
    name="backgroundColor286",
    ends={
        Property(name="ColorDescription287", type=diagram_style_GaugeSectionDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_GaugeSectionDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
foregroundColor288: BinaryAssociation = BinaryAssociation(
    name="foregroundColor288",
    ends={
        Property(name="ColorDescription290", type=diagram_style_GaugeSectionDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_GaugeSectionDescription289", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
backgroundColor291: BinaryAssociation = BinaryAssociation(
    name="backgroundColor291",
    ends={
        Property(name="ColorDescription292", type=diagram_style_FlatContainerStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_FlatContainerStyleDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
foregroundColor293: BinaryAssociation = BinaryAssociation(
    name="foregroundColor293",
    ends={
        Property(name="ColorDescription295", type=diagram_style_FlatContainerStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_FlatContainerStyleDescription294", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
labelBorderStyle296: BinaryAssociation = BinaryAssociation(
    name="labelBorderStyle296",
    ends={
        Property(name="style_LabelBorderStyleDescription", type=diagram_style_FlatContainerStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_FlatContainerStyleDescription297", type=style_LabelBorderStyleDescription, multiplicity=Multiplicity(0, 1))
    }
)
backgroundColor298: BinaryAssociation = BinaryAssociation(
    name="backgroundColor298",
    ends={
        Property(name="ColorDescription299", type=diagram_style_ShapeContainerStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_ShapeContainerStyleDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
strokeColor300: BinaryAssociation = BinaryAssociation(
    name="strokeColor300",
    ends={
        Property(name="ColorDescription301", type=diagram_style_EdgeStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_EdgeStyleDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
centerLabelStyleDescription304: BinaryAssociation = BinaryAssociation(
    name="centerLabelStyleDescription304",
    ends={
        Property(name="style_CenterLabelStyleDescription", type=diagram_style_EdgeStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_EdgeStyleDescription305", type=style_CenterLabelStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
beginLabelStyleDescription302: BinaryAssociation = BinaryAssociation(
    name="beginLabelStyleDescription302",
    ends={
        Property(name="style_BeginLabelStyleDescription", type=diagram_style_EdgeStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_EdgeStyleDescription303", type=style_BeginLabelStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
endLabelStyleDescription306: BinaryAssociation = BinaryAssociation(
    name="endLabelStyleDescription306",
    ends={
        Property(name="style_EndLabelStyleDescription", type=diagram_style_EdgeStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_EdgeStyleDescription307", type=style_EndLabelStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
centeredSourceMappings308: BinaryAssociation = BinaryAssociation(
    name="centeredSourceMappings308",
    ends={
        Property(name="DiagramElementMapping310", type=diagram_style_EdgeStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_EdgeStyleDescription309", type=DiagramElementMapping, multiplicity=Multiplicity(0, 9999))
    }
)
centeredTargetMappings311: BinaryAssociation = BinaryAssociation(
    name="centeredTargetMappings311",
    ends={
        Property(name="DiagramElementMapping313", type=diagram_style_EdgeStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_EdgeStyleDescription312", type=DiagramElementMapping, multiplicity=Multiplicity(0, 9999))
    }
)
reusedTools320: BinaryAssociation = BinaryAssociation(
    name="reusedTools320",
    ends={
        Property(name="tool_ToolEntry322", type=diagram_tool_ToolSection, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ToolSection321", type=tool_ToolEntry, multiplicity=Multiplicity(0, 9999))
    }
)
ownedTools314: BinaryAssociation = BinaryAssociation(
    name="ownedTools314",
    ends={
        Property(name="tool_ToolEntry", type=diagram_tool_ToolSection, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ToolSection", type=tool_ToolEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subSections315: BinaryAssociation = BinaryAssociation(
    name="subSections315",
    ends={
        Property(name="tool_ToolSection317", type=diagram_tool_ToolSection, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ToolSection316", type=tool_ToolSection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
popupMenus318: BinaryAssociation = BinaryAssociation(
    name="popupMenus318",
    ends={
        Property(name="tool_PopupMenu", type=diagram_tool_ToolSection, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ToolSection319", type=tool_PopupMenu, multiplicity=Multiplicity(0, 9999))
    }
)
groupExtensions323: BinaryAssociation = BinaryAssociation(
    name="groupExtensions323",
    ends={
        Property(name="tool_ToolGroupExtension", type=diagram_tool_ToolSection, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ToolSection324", type=tool_ToolGroupExtension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
groups325: BinaryAssociation = BinaryAssociation(
    name="groups325",
    ends={
        Property(name="tool_GroupMenu", type=diagram_tool_ToolSection, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ToolSection326", type=tool_GroupMenu, multiplicity=Multiplicity(0, 9999))
    }
)
tools327: BinaryAssociation = BinaryAssociation(
    name="tools327",
    ends={
        Property(name="tool_AbstractToolDescription328", type=diagram_tool_ToolGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ToolGroup", type=tool_AbstractToolDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
group329: BinaryAssociation = BinaryAssociation(
    name="group329",
    ends={
        Property(name="tool_ToolGroup", type=diagram_tool_ToolGroupExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ToolGroupExtension", type=tool_ToolGroup, multiplicity=Multiplicity(1, 1))
    }
)
tools330: BinaryAssociation = BinaryAssociation(
    name="tools330",
    ends={
        Property(name="tool_AbstractToolDescription332", type=diagram_tool_ToolGroupExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ToolGroupExtension331", type=tool_AbstractToolDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodeMappings333: BinaryAssociation = BinaryAssociation(
    name="nodeMappings333",
    ends={
        Property(name="NodeMapping334", type=diagram_tool_NodeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_NodeCreationDescription", type=NodeMapping, multiplicity=Multiplicity(1, 9999))
    }
)
edgeMappings344: BinaryAssociation = BinaryAssociation(
    name="edgeMappings344",
    ends={
        Property(name="EdgeMapping345", type=diagram_tool_EdgeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_EdgeCreationDescription", type=EdgeMapping, multiplicity=Multiplicity(1, 9999))
    }
)
variable335: BinaryAssociation = BinaryAssociation(
    name="variable335",
    ends={
        Property(name="tool_NodeCreationVariable", type=diagram_tool_NodeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_NodeCreationDescription336", type=tool_NodeCreationVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
viewVariable337: BinaryAssociation = BinaryAssociation(
    name="viewVariable337",
    ends={
        Property(name="tool_ContainerViewVariable", type=diagram_tool_NodeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_NodeCreationDescription338", type=tool_ContainerViewVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialOperation339: BinaryAssociation = BinaryAssociation(
    name="initialOperation339",
    ends={
        Property(name="tool_InitialNodeCreationOperation", type=diagram_tool_NodeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_NodeCreationDescription340", type=tool_InitialNodeCreationOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
extraMappings341: BinaryAssociation = BinaryAssociation(
    name="extraMappings341",
    ends={
        Property(name="AbstractNodeMapping343", type=diagram_tool_NodeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_NodeCreationDescription342", type=AbstractNodeMapping, multiplicity=Multiplicity(0, 9999))
    }
)
sourceVariable346: BinaryAssociation = BinaryAssociation(
    name="sourceVariable346",
    ends={
        Property(name="tool_SourceEdgeCreationVariable", type=diagram_tool_EdgeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_EdgeCreationDescription347", type=tool_SourceEdgeCreationVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
targetVariable348: BinaryAssociation = BinaryAssociation(
    name="targetVariable348",
    ends={
        Property(name="tool_TargetEdgeCreationVariable", type=diagram_tool_EdgeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_EdgeCreationDescription349", type=tool_TargetEdgeCreationVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sourceViewVariable350: BinaryAssociation = BinaryAssociation(
    name="sourceViewVariable350",
    ends={
        Property(name="tool_SourceEdgeViewCreationVariable", type=diagram_tool_EdgeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_EdgeCreationDescription351", type=tool_SourceEdgeViewCreationVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
targetViewVariable352: BinaryAssociation = BinaryAssociation(
    name="targetViewVariable352",
    ends={
        Property(name="tool_TargetEdgeViewCreationVariable", type=diagram_tool_EdgeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_EdgeCreationDescription353", type=tool_TargetEdgeViewCreationVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialOperation354: BinaryAssociation = BinaryAssociation(
    name="initialOperation354",
    ends={
        Property(name="tool_InitEdgeCreationOperation", type=diagram_tool_EdgeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_EdgeCreationDescription355", type=tool_InitEdgeCreationOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
viewVariable367: BinaryAssociation = BinaryAssociation(
    name="viewVariable367",
    ends={
        Property(name="tool_ContainerViewVariable369", type=diagram_tool_ContainerCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ContainerCreationDescription368", type=tool_ContainerViewVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
extraSourceMappings356: BinaryAssociation = BinaryAssociation(
    name="extraSourceMappings356",
    ends={
        Property(name="DiagramElementMapping358", type=diagram_tool_EdgeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_EdgeCreationDescription357", type=DiagramElementMapping, multiplicity=Multiplicity(0, 9999))
    }
)
extraTargetMappings359: BinaryAssociation = BinaryAssociation(
    name="extraTargetMappings359",
    ends={
        Property(name="DiagramElementMapping361", type=diagram_tool_EdgeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_EdgeCreationDescription360", type=DiagramElementMapping, multiplicity=Multiplicity(0, 9999))
    }
)
containerMappings362: BinaryAssociation = BinaryAssociation(
    name="containerMappings362",
    ends={
        Property(name="ContainerMapping363", type=diagram_tool_ContainerCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ContainerCreationDescription", type=ContainerMapping, multiplicity=Multiplicity(1, 9999))
    }
)
variable364: BinaryAssociation = BinaryAssociation(
    name="variable364",
    ends={
        Property(name="tool_NodeCreationVariable366", type=diagram_tool_ContainerCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ContainerCreationDescription365", type=tool_NodeCreationVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialOperation383: BinaryAssociation = BinaryAssociation(
    name="initialOperation383",
    ends={
        Property(name="tool_InitialOperation385", type=diagram_tool_DeleteElementDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DeleteElementDescription384", type=tool_InitialOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialOperation370: BinaryAssociation = BinaryAssociation(
    name="initialOperation370",
    ends={
        Property(name="tool_InitialNodeCreationOperation372", type=diagram_tool_ContainerCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ContainerCreationDescription371", type=tool_InitialNodeCreationOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
extraMappings373: BinaryAssociation = BinaryAssociation(
    name="extraMappings373",
    ends={
        Property(name="AbstractNodeMapping375", type=diagram_tool_ContainerCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ContainerCreationDescription374", type=AbstractNodeMapping, multiplicity=Multiplicity(0, 9999))
    }
)
element376: BinaryAssociation = BinaryAssociation(
    name="element376",
    ends={
        Property(name="tool_ElementDeleteVariable", type=diagram_tool_DeleteElementDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DeleteElementDescription", type=tool_ElementDeleteVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elementView377: BinaryAssociation = BinaryAssociation(
    name="elementView377",
    ends={
        Property(name="tool_ElementDeleteVariable379", type=diagram_tool_DeleteElementDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DeleteElementDescription378", type=tool_ElementDeleteVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
containerView380: BinaryAssociation = BinaryAssociation(
    name="containerView380",
    ends={
        Property(name="tool_ContainerViewVariable382", type=diagram_tool_DeleteElementDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DeleteElementDescription381", type=tool_ContainerViewVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters398: BinaryAssociation = BinaryAssociation(
    name="parameters398",
    ends={
        Property(name="tool_DeleteHookParameter", type=diagram_tool_DeleteHook, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DeleteHook", type=tool_DeleteHookParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hook386: BinaryAssociation = BinaryAssociation(
    name="hook386",
    ends={
        Property(name="tool_DeleteHook", type=diagram_tool_DeleteElementDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DeleteElementDescription387", type=tool_DeleteHook, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mappings388: BinaryAssociation = BinaryAssociation(
    name="mappings388",
    ends={
        Property(name="description390", type=diagram_tool_DoubleClickDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="DiagramElementMapping389", type=DiagramElementMapping, multiplicity=Multiplicity(1, 9999))
    }
)
element391: BinaryAssociation = BinaryAssociation(
    name="element391",
    ends={
        Property(name="tool_ElementDoubleClickVariable", type=diagram_tool_DoubleClickDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DoubleClickDescription", type=tool_ElementDoubleClickVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elementView392: BinaryAssociation = BinaryAssociation(
    name="elementView392",
    ends={
        Property(name="tool_ElementDoubleClickVariable394", type=diagram_tool_DoubleClickDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DoubleClickDescription393", type=tool_ElementDoubleClickVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initialOperation395: BinaryAssociation = BinaryAssociation(
    name="initialOperation395",
    ends={
        Property(name="tool_InitialOperation397", type=diagram_tool_DoubleClickDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DoubleClickDescription396", type=tool_InitialOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source399: BinaryAssociation = BinaryAssociation(
    name="source399",
    ends={
        Property(name="tool_SourceEdgeCreationVariable400", type=diagram_tool_ReconnectEdgeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ReconnectEdgeDescription", type=tool_SourceEdgeCreationVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target401: BinaryAssociation = BinaryAssociation(
    name="target401",
    ends={
        Property(name="tool_TargetEdgeCreationVariable403", type=diagram_tool_ReconnectEdgeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ReconnectEdgeDescription402", type=tool_TargetEdgeCreationVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sourceView404: BinaryAssociation = BinaryAssociation(
    name="sourceView404",
    ends={
        Property(name="tool_SourceEdgeViewCreationVariable406", type=diagram_tool_ReconnectEdgeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ReconnectEdgeDescription405", type=tool_SourceEdgeViewCreationVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
targetView407: BinaryAssociation = BinaryAssociation(
    name="targetView407",
    ends={
        Property(name="tool_TargetEdgeViewCreationVariable409", type=diagram_tool_ReconnectEdgeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ReconnectEdgeDescription408", type=tool_TargetEdgeViewCreationVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
element410: BinaryAssociation = BinaryAssociation(
    name="element410",
    ends={
        Property(name="tool_ElementSelectVariable", type=diagram_tool_ReconnectEdgeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ReconnectEdgeDescription411", type=tool_ElementSelectVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialOperation412: BinaryAssociation = BinaryAssociation(
    name="initialOperation412",
    ends={
        Property(name="tool_InitialOperation414", type=diagram_tool_ReconnectEdgeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ReconnectEdgeDescription413", type=tool_InitialOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
edgeView415: BinaryAssociation = BinaryAssociation(
    name="edgeView415",
    ends={
        Property(name="tool_ElementSelectVariable417", type=diagram_tool_ReconnectEdgeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ReconnectEdgeDescription416", type=tool_ElementSelectVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mask418: BinaryAssociation = BinaryAssociation(
    name="mask418",
    ends={
        Property(name="tool_EditMaskVariables", type=diagram_tool_DirectEditLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DirectEditLabel", type=tool_EditMaskVariables, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialOperation419: BinaryAssociation = BinaryAssociation(
    name="initialOperation419",
    ends={
        Property(name="tool_InitialOperation421", type=diagram_tool_DirectEditLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DirectEditLabel420", type=tool_InitialOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialOperation422: BinaryAssociation = BinaryAssociation(
    name="initialOperation422",
    ends={
        Property(name="tool_InitialOperation423", type=diagram_tool_BehaviorTool, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_BehaviorTool", type=tool_InitialOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mapping424: BinaryAssociation = BinaryAssociation(
    name="mapping424",
    ends={
        Property(name="DiagramElementMapping425", type=diagram_tool_CreateView, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_CreateView", type=DiagramElementMapping, multiplicity=Multiplicity(1, 1))
    }
)
diagramDescription426: BinaryAssociation = BinaryAssociation(
    name="diagramDescription426",
    ends={
        Property(name="DiagramDescription427", type=diagram_tool_Navigation, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_Navigation", type=DiagramDescription, multiplicity=Multiplicity(1, 1))
    }
)
diagramDescription428: BinaryAssociation = BinaryAssociation(
    name="diagramDescription428",
    ends={
        Property(name="DiagramDescription429", type=diagram_tool_DiagramCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DiagramCreationDescription", type=DiagramDescription, multiplicity=Multiplicity(1, 1))
    }
)
diagramDescription430: BinaryAssociation = BinaryAssociation(
    name="diagramDescription430",
    ends={
        Property(name="DiagramDescription431", type=diagram_tool_DiagramNavigationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DiagramNavigationDescription", type=DiagramDescription, multiplicity=Multiplicity(1, 1))
    }
)
mappings432: BinaryAssociation = BinaryAssociation(
    name="mappings432",
    ends={
        Property(name="DiagramElementMapping433", type=diagram_tool_ContainerDropDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ContainerDropDescription", type=DiagramElementMapping, multiplicity=Multiplicity(0, 9999))
    }
)
oldContainer434: BinaryAssociation = BinaryAssociation(
    name="oldContainer434",
    ends={
        Property(name="tool_DropContainerVariable", type=diagram_tool_ContainerDropDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ContainerDropDescription435", type=tool_DropContainerVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
newContainer436: BinaryAssociation = BinaryAssociation(
    name="newContainer436",
    ends={
        Property(name="tool_DropContainerVariable438", type=diagram_tool_ContainerDropDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ContainerDropDescription437", type=tool_DropContainerVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
element439: BinaryAssociation = BinaryAssociation(
    name="element439",
    ends={
        Property(name="tool_ElementDropVariable", type=diagram_tool_ContainerDropDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ContainerDropDescription440", type=tool_ElementDropVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
newViewContainer441: BinaryAssociation = BinaryAssociation(
    name="newViewContainer441",
    ends={
        Property(name="tool_ContainerViewVariable443", type=diagram_tool_ContainerDropDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ContainerDropDescription442", type=tool_ContainerViewVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedVariables449: BinaryAssociation = BinaryAssociation(
    name="ownedVariables449",
    ends={
        Property(name="InteractiveVariableDescription", type=diagram_filter_VariableFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_filter_VariableFilter", type=InteractiveVariableDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialOperation444: BinaryAssociation = BinaryAssociation(
    name="initialOperation444",
    ends={
        Property(name="tool_InitialContainerDropOperation", type=diagram_tool_ContainerDropDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ContainerDropDescription445", type=tool_InitialContainerDropOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mappings446: BinaryAssociation = BinaryAssociation(
    name="mappings446",
    ends={
        Property(name="DiagramElementMapping447", type=diagram_filter_MappingFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_filter_MappingFilter", type=DiagramElementMapping, multiplicity=Multiplicity(0, 9999))
    }
)
filters448: BinaryAssociation = BinaryAssociation(
    name="filters448",
    ends={
        Property(name="filter_Filter", type=diagram_filter_CompositeFilterDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_filter_CompositeFilterDescription", type=filter_Filter, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ownedConcernDescriptions450: BinaryAssociation = BinaryAssociation(
    name="ownedConcernDescriptions450",
    ends={
        Property(name="concern_ConcernDescription451", type=diagram_concern_ConcernSet, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_concern_ConcernSet", type=concern_ConcernDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
filters452: BinaryAssociation = BinaryAssociation(
    name="filters452",
    ends={
        Property(name="filter_FilterDescription453", type=diagram_concern_ConcernDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_concern_ConcernDescription", type=filter_FilterDescription, multiplicity=Multiplicity(0, 9999))
    }
)
rules454: BinaryAssociation = BinaryAssociation(
    name="rules454",
    ends={
        Property(name="validation_ValidationRule456", type=diagram_concern_ConcernDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_concern_ConcernDescription455", type=validation_ValidationRule, multiplicity=Multiplicity(0, 9999))
    }
)
behaviors457: BinaryAssociation = BinaryAssociation(
    name="behaviors457",
    ends={
        Property(name="tool_BehaviorTool459", type=diagram_concern_ConcernDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_concern_ConcernDescription458", type=tool_BehaviorTool, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_diagram_DDiagram_DRepresentation = Generalization(general=DRepresentation, specific=diagram_DDiagram)
gen_diagram_DDiagram_DragAndDropTarget = Generalization(general=DragAndDropTarget, specific=diagram_DDiagram)
gen_diagram_DSemanticDiagram_DDiagram = Generalization(general=DDiagram, specific=diagram_DSemanticDiagram)
gen_diagram_DSemanticDiagram_DSemanticDecorator = Generalization(general=DSemanticDecorator, specific=diagram_DSemanticDiagram)
gen_diagram_DDiagramElement_DRepresentationElement = Generalization(general=DRepresentationElement, specific=diagram_DDiagramElement)
gen_diagram_GraphicalFilter_IdentifiedElement = Generalization(general=IdentifiedElement, specific=diagram_GraphicalFilter)
gen_diagram_HideFilter_GraphicalFilter = Generalization(general=GraphicalFilter, specific=diagram_HideFilter)
gen_diagram_HideLabelFilter_GraphicalFilter = Generalization(general=GraphicalFilter, specific=diagram_HideLabelFilter)
gen_diagram_FoldingPointFilter_GraphicalFilter = Generalization(general=GraphicalFilter, specific=diagram_FoldingPointFilter)
gen_diagram_FoldingFilter_GraphicalFilter = Generalization(general=GraphicalFilter, specific=diagram_FoldingFilter)
gen_diagram_AppliedCompositeFilters_GraphicalFilter = Generalization(general=GraphicalFilter, specific=diagram_AppliedCompositeFilters)
gen_diagram_DNode_AbstractDNode = Generalization(general=AbstractDNode, specific=diagram_DNode)
gen_diagram_DNode_EdgeTarget = Generalization(general=EdgeTarget, specific=diagram_DNode)
gen_diagram_DNode_DragAndDropTarget = Generalization(general=DragAndDropTarget, specific=diagram_DNode)
gen_diagram_DDiagramElementContainer_AbstractDNode = Generalization(general=AbstractDNode, specific=diagram_DDiagramElementContainer)
gen_diagram_DDiagramElementContainer_EdgeTarget = Generalization(general=EdgeTarget, specific=diagram_DDiagramElementContainer)
gen_diagram_DDiagramElementContainer_DragAndDropTarget = Generalization(general=DragAndDropTarget, specific=diagram_DDiagramElementContainer)
gen_diagram_AbsoluteBoundsFilter_GraphicalFilter = Generalization(general=GraphicalFilter, specific=diagram_AbsoluteBoundsFilter)
gen_diagram_AbstractDNode_DDiagramElement = Generalization(general=DDiagramElement, specific=diagram_AbstractDNode)
gen_diagram_DNodeContainer_DDiagramElementContainer = Generalization(general=DDiagramElementContainer, specific=diagram_DNodeContainer)
gen_diagram_DNodeList_DDiagramElementContainer = Generalization(general=DDiagramElementContainer, specific=diagram_DNodeList)
gen_diagram_DEdge_DDiagramElement = Generalization(general=DDiagramElement, specific=diagram_DEdge)
gen_diagram_DEdge_EdgeTarget = Generalization(general=EdgeTarget, specific=diagram_DEdge)
gen_diagram_DNodeListElement_AbstractDNode = Generalization(general=AbstractDNode, specific=diagram_DNodeListElement)
gen_diagram_NodeStyle_LabelStyle = Generalization(general=LabelStyle, specific=diagram_NodeStyle)
gen_diagram_NodeStyle_Style = Generalization(general=Style, specific=diagram_NodeStyle)
gen_diagram_NodeStyle_BorderedStyle = Generalization(general=BorderedStyle, specific=diagram_NodeStyle)
gen_diagram_NodeStyle_HideLabelCapabilityStyle = Generalization(general=HideLabelCapabilityStyle, specific=diagram_NodeStyle)
gen_diagram_Dot_NodeStyle = Generalization(general=NodeStyle, specific=diagram_Dot)
gen_diagram_GaugeSection_Customizable = Generalization(general=Customizable, specific=diagram_GaugeSection)
gen_diagram_FlatContainerStyle_ContainerStyle = Generalization(general=ContainerStyle, specific=diagram_FlatContainerStyle)
gen_diagram_ShapeContainerStyle_ContainerStyle = Generalization(general=ContainerStyle, specific=diagram_ShapeContainerStyle)
gen_diagram_Square_NodeStyle = Generalization(general=NodeStyle, specific=diagram_Square)
gen_diagram_Ellipse_NodeStyle = Generalization(general=NodeStyle, specific=diagram_Ellipse)
gen_diagram_ContainerStyle_LabelStyle = Generalization(general=LabelStyle, specific=diagram_ContainerStyle)
gen_diagram_ContainerStyle_Style = Generalization(general=Style, specific=diagram_ContainerStyle)
gen_diagram_ContainerStyle_BorderedStyle = Generalization(general=BorderedStyle, specific=diagram_ContainerStyle)
gen_diagram_ContainerStyle_HideLabelCapabilityStyle = Generalization(general=HideLabelCapabilityStyle, specific=diagram_ContainerStyle)
gen_diagram_BundledImage_NodeStyle = Generalization(general=NodeStyle, specific=diagram_BundledImage)
gen_diagram_WorkspaceImage_NodeStyle = Generalization(general=NodeStyle, specific=diagram_WorkspaceImage)
gen_diagram_WorkspaceImage_ContainerStyle = Generalization(general=ContainerStyle, specific=diagram_WorkspaceImage)
gen_diagram_CustomStyle_NodeStyle = Generalization(general=NodeStyle, specific=diagram_CustomStyle)
gen_diagram_EdgeTarget_IdentifiedElement = Generalization(general=IdentifiedElement, specific=diagram_EdgeTarget)
gen_diagram_EdgeStyle_Style = Generalization(general=Style, specific=diagram_EdgeStyle)
gen_diagram_Lozenge_NodeStyle = Generalization(general=NodeStyle, specific=diagram_Lozenge)
gen_diagram_GaugeCompositeStyle_NodeStyle = Generalization(general=NodeStyle, specific=diagram_GaugeCompositeStyle)
gen_diagram_BorderedStyle_Style = Generalization(general=Style, specific=diagram_BorderedStyle)
gen_diagram_Note_NodeStyle = Generalization(general=NodeStyle, specific=diagram_Note)
gen_diagram_FilterVariableHistory_IdentifiedElement = Generalization(general=IdentifiedElement, specific=diagram_FilterVariableHistory)
gen_diagram_EndLabelStyle_BasicLabelStyle = Generalization(general=BasicLabelStyle, specific=diagram_EndLabelStyle)
gen_diagram_CollapseFilter_GraphicalFilter = Generalization(general=GraphicalFilter, specific=diagram_CollapseFilter)
gen_diagram_IndirectlyCollapseFilter_CollapseFilter = Generalization(general=CollapseFilter, specific=diagram_IndirectlyCollapseFilter)
gen_diagram_BeginLabelStyle_BasicLabelStyle = Generalization(general=BasicLabelStyle, specific=diagram_BeginLabelStyle)
gen_diagram_CenterLabelStyle_BasicLabelStyle = Generalization(general=BasicLabelStyle, specific=diagram_CenterLabelStyle)
gen_diagram_EObjectVariableValue_VariableValue = Generalization(general=VariableValue, specific=diagram_EObjectVariableValue)
gen_diagram_BracketEdgeStyle_EdgeStyle = Generalization(general=EdgeStyle, specific=diagram_BracketEdgeStyle)
gen_diagram_ComputedStyleDescriptionRegistry_IdentifiedElement = Generalization(general=IdentifiedElement, specific=diagram_ComputedStyleDescriptionRegistry)
gen_diagram_DragAndDropTarget_IdentifiedElement = Generalization(general=IdentifiedElement, specific=diagram_DragAndDropTarget)
gen_diagram_VariableValue_IdentifiedElement = Generalization(general=IdentifiedElement, specific=diagram_VariableValue)
gen_diagram_TypedVariableValue_VariableValue = Generalization(general=VariableValue, specific=diagram_TypedVariableValue)
gen_diagram_description_DiagramDescription_description_DragAndDropTargetDescription = Generalization(general=description_DragAndDropTargetDescription, specific=diagram_description_DiagramDescription)
gen_diagram_description_DiagramDescription_description_RepresentationDescription = Generalization(general=description_RepresentationDescription, specific=diagram_description_DiagramDescription)
gen_diagram_description_DiagramDescription_description_PasteTargetDescription = Generalization(general=description_PasteTargetDescription, specific=diagram_description_DiagramDescription)
gen_diagram_description_DiagramImportDescription_description_RepresentationImportDescription = Generalization(general=description_RepresentationImportDescription, specific=diagram_description_DiagramImportDescription)
gen_diagram_description_DiagramImportDescription_description_DiagramDescription = Generalization(general=description_DiagramDescription, specific=diagram_description_DiagramImportDescription)
gen_diagram_description_DiagramExtensionDescription_RepresentationExtensionDescription = Generalization(general=RepresentationExtensionDescription, specific=diagram_description_DiagramExtensionDescription)
gen_diagram_description_DiagramElementMapping_description_RepresentationElementMapping = Generalization(general=description_RepresentationElementMapping, specific=diagram_description_DiagramElementMapping)
gen_diagram_description_DiagramElementMapping_description_PasteTargetDescription = Generalization(general=description_PasteTargetDescription, specific=diagram_description_DiagramElementMapping)
gen_diagram_description_AbstractNodeMapping_description_DiagramElementMapping = Generalization(general=description_DiagramElementMapping, specific=diagram_description_AbstractNodeMapping)
gen_diagram_description_AbstractNodeMapping_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=diagram_description_AbstractNodeMapping)
gen_diagram_description_NodeMapping_description_AbstractNodeMapping = Generalization(general=description_AbstractNodeMapping, specific=diagram_description_NodeMapping)
gen_diagram_description_NodeMapping_description_DragAndDropTargetDescription = Generalization(general=description_DragAndDropTargetDescription, specific=diagram_description_NodeMapping)
gen_diagram_description_ContainerMapping_description_AbstractNodeMapping = Generalization(general=description_AbstractNodeMapping, specific=diagram_description_ContainerMapping)
gen_diagram_description_ContainerMapping_description_DragAndDropTargetDescription = Generalization(general=description_DragAndDropTargetDescription, specific=diagram_description_ContainerMapping)
gen_diagram_description_NodeMappingImport_description_NodeMapping = Generalization(general=description_NodeMapping, specific=diagram_description_NodeMappingImport)
gen_diagram_description_NodeMappingImport_description_AbstractMappingImport = Generalization(general=description_AbstractMappingImport, specific=diagram_description_NodeMappingImport)
gen_diagram_description_ContainerMappingImport_description_ContainerMapping = Generalization(general=description_ContainerMapping, specific=diagram_description_ContainerMappingImport)
gen_diagram_description_ContainerMappingImport_description_AbstractMappingImport = Generalization(general=description_AbstractMappingImport, specific=diagram_description_ContainerMappingImport)
gen_diagram_description_EdgeMapping_description_DiagramElementMapping = Generalization(general=description_DiagramElementMapping, specific=diagram_description_EdgeMapping)
gen_diagram_description_EdgeMapping_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=diagram_description_EdgeMapping)
gen_diagram_description_EdgeMapping_description_IEdgeMapping = Generalization(general=description_IEdgeMapping, specific=diagram_description_EdgeMapping)
gen_diagram_description_EdgeMappingImport_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=diagram_description_EdgeMappingImport)
gen_diagram_description_EdgeMappingImport_description_IEdgeMapping = Generalization(general=description_IEdgeMapping, specific=diagram_description_EdgeMappingImport)
gen_diagram_description_EdgeMappingImport_description_IdentifiedElement = Generalization(general=description_IdentifiedElement, specific=diagram_description_EdgeMappingImport)
gen_diagram_description_ConditionalNodeStyleDescription_ConditionalStyleDescription = Generalization(general=ConditionalStyleDescription, specific=diagram_description_ConditionalNodeStyleDescription)
gen_diagram_description_ConditionalEdgeStyleDescription_ConditionalStyleDescription = Generalization(general=ConditionalStyleDescription, specific=diagram_description_ConditionalEdgeStyleDescription)
gen_diagram_description_ConditionalContainerStyleDescription_ConditionalStyleDescription = Generalization(general=ConditionalStyleDescription, specific=diagram_description_ConditionalContainerStyleDescription)
gen_diagram_description_Layout_DocumentedElement = Generalization(general=DocumentedElement, specific=diagram_description_Layout)
gen_diagram_description_OrderedTreeLayout_Layout = Generalization(general=Layout, specific=diagram_description_OrderedTreeLayout)
gen_diagram_description_CompositeLayout_Layout = Generalization(general=Layout, specific=diagram_description_CompositeLayout)
gen_diagram_description_CustomLayoutConfiguration_Layout = Generalization(general=Layout, specific=diagram_description_CustomLayoutConfiguration)
gen_diagram_description_Layer_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=diagram_description_Layer)
gen_diagram_description_Layer_description_EndUserDocumentedElement = Generalization(general=description_EndUserDocumentedElement, specific=diagram_description_Layer)
gen_diagram_description_Layer_description_IdentifiedElement = Generalization(general=description_IdentifiedElement, specific=diagram_description_Layer)
gen_diagram_description_BooleanLayoutOption_LayoutOption = Generalization(general=LayoutOption, specific=diagram_description_BooleanLayoutOption)
gen_diagram_description_StringLayoutOption_LayoutOption = Generalization(general=LayoutOption, specific=diagram_description_StringLayoutOption)
gen_diagram_description_IntegerLayoutOption_LayoutOption = Generalization(general=LayoutOption, specific=diagram_description_IntegerLayoutOption)
gen_diagram_description_DoubleLayoutOption_LayoutOption = Generalization(general=LayoutOption, specific=diagram_description_DoubleLayoutOption)
gen_diagram_description_EnumLayoutOption_EnumOption = Generalization(general=EnumOption, specific=diagram_description_EnumLayoutOption)
gen_diagram_description_EnumSetLayoutOption_EnumOption = Generalization(general=EnumOption, specific=diagram_description_EnumSetLayoutOption)
gen_diagram_description_EnumOption_LayoutOption = Generalization(general=LayoutOption, specific=diagram_description_EnumOption)
gen_diagram_description_MappingBasedDecoration_DecorationDescription = Generalization(general=DecorationDescription, specific=diagram_description_MappingBasedDecoration)
gen_diagram_description_AdditionalLayer_Layer = Generalization(general=Layer, specific=diagram_description_AdditionalLayer)
gen_diagram_style_BorderedStyleDescription_StyleDescription = Generalization(general=StyleDescription, specific=diagram_style_BorderedStyleDescription)
gen_diagram_style_NodeStyleDescription_style_StyleDescription = Generalization(general=style_StyleDescription, specific=diagram_style_NodeStyleDescription)
gen_diagram_style_NodeStyleDescription_style_BorderedStyleDescription = Generalization(general=style_BorderedStyleDescription, specific=diagram_style_NodeStyleDescription)
gen_diagram_style_NodeStyleDescription_style_LabelStyleDescription = Generalization(general=style_LabelStyleDescription, specific=diagram_style_NodeStyleDescription)
gen_diagram_style_NodeStyleDescription_style_TooltipStyleDescription = Generalization(general=style_TooltipStyleDescription, specific=diagram_style_NodeStyleDescription)
gen_diagram_style_NodeStyleDescription_style_HideLabelCapabilityStyleDescription = Generalization(general=style_HideLabelCapabilityStyleDescription, specific=diagram_style_NodeStyleDescription)
gen_diagram_style_CustomStyleDescription_NodeStyleDescription = Generalization(general=NodeStyleDescription, specific=diagram_style_CustomStyleDescription)
gen_diagram_style_SquareDescription_NodeStyleDescription = Generalization(general=NodeStyleDescription, specific=diagram_style_SquareDescription)
gen_diagram_style_DotDescription_NodeStyleDescription = Generalization(general=NodeStyleDescription, specific=diagram_style_DotDescription)
gen_diagram_style_LozengeNodeDescription_NodeStyleDescription = Generalization(general=NodeStyleDescription, specific=diagram_style_LozengeNodeDescription)
gen_diagram_style_EllipseNodeDescription_NodeStyleDescription = Generalization(general=NodeStyleDescription, specific=diagram_style_EllipseNodeDescription)
gen_diagram_style_BundledImageDescription_NodeStyleDescription = Generalization(general=NodeStyleDescription, specific=diagram_style_BundledImageDescription)
gen_diagram_style_NoteDescription_NodeStyleDescription = Generalization(general=NodeStyleDescription, specific=diagram_style_NoteDescription)
gen_diagram_style_GaugeCompositeStyleDescription_NodeStyleDescription = Generalization(general=NodeStyleDescription, specific=diagram_style_GaugeCompositeStyleDescription)
gen_diagram_style_RoundedCornerStyleDescription_StyleDescription = Generalization(general=StyleDescription, specific=diagram_style_RoundedCornerStyleDescription)
gen_diagram_style_ContainerStyleDescription_style_RoundedCornerStyleDescription = Generalization(general=style_RoundedCornerStyleDescription, specific=diagram_style_ContainerStyleDescription)
gen_diagram_style_ContainerStyleDescription_style_BorderedStyleDescription = Generalization(general=style_BorderedStyleDescription, specific=diagram_style_ContainerStyleDescription)
gen_diagram_style_ContainerStyleDescription_style_LabelStyleDescription = Generalization(general=style_LabelStyleDescription, specific=diagram_style_ContainerStyleDescription)
gen_diagram_style_ContainerStyleDescription_style_TooltipStyleDescription = Generalization(general=style_TooltipStyleDescription, specific=diagram_style_ContainerStyleDescription)
gen_diagram_style_ContainerStyleDescription_style_HideLabelCapabilityStyleDescription = Generalization(general=style_HideLabelCapabilityStyleDescription, specific=diagram_style_ContainerStyleDescription)
gen_diagram_style_FlatContainerStyleDescription_style_ContainerStyleDescription = Generalization(general=style_ContainerStyleDescription, specific=diagram_style_FlatContainerStyleDescription)
gen_diagram_style_FlatContainerStyleDescription_style_SizeComputationContainerStyleDescription = Generalization(general=style_SizeComputationContainerStyleDescription, specific=diagram_style_FlatContainerStyleDescription)
gen_diagram_style_ShapeContainerStyleDescription_style_ContainerStyleDescription = Generalization(general=style_ContainerStyleDescription, specific=diagram_style_ShapeContainerStyleDescription)
gen_diagram_style_ShapeContainerStyleDescription_style_SizeComputationContainerStyleDescription = Generalization(general=style_SizeComputationContainerStyleDescription, specific=diagram_style_ShapeContainerStyleDescription)
gen_diagram_style_WorkspaceImageDescription_style_NodeStyleDescription = Generalization(general=style_NodeStyleDescription, specific=diagram_style_WorkspaceImageDescription)
gen_diagram_style_WorkspaceImageDescription_style_ContainerStyleDescription = Generalization(general=style_ContainerStyleDescription, specific=diagram_style_WorkspaceImageDescription)
gen_diagram_style_EdgeStyleDescription_StyleDescription = Generalization(general=StyleDescription, specific=diagram_style_EdgeStyleDescription)
gen_diagram_style_BeginLabelStyleDescription_BasicLabelStyleDescription = Generalization(general=BasicLabelStyleDescription, specific=diagram_style_BeginLabelStyleDescription)
gen_diagram_style_CenterLabelStyleDescription_BasicLabelStyleDescription = Generalization(general=BasicLabelStyleDescription, specific=diagram_style_CenterLabelStyleDescription)
gen_diagram_style_EndLabelStyleDescription_BasicLabelStyleDescription = Generalization(general=BasicLabelStyleDescription, specific=diagram_style_EndLabelStyleDescription)
gen_diagram_style_BracketEdgeStyleDescription_EdgeStyleDescription = Generalization(general=EdgeStyleDescription, specific=diagram_style_BracketEdgeStyleDescription)
gen_diagram_tool_ToolSection_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=diagram_tool_ToolSection)
gen_diagram_tool_ToolSection_description_IdentifiedElement = Generalization(general=description_IdentifiedElement, specific=diagram_tool_ToolSection)
gen_diagram_tool_ToolGroup_ToolEntry = Generalization(general=ToolEntry, specific=diagram_tool_ToolGroup)
gen_diagram_tool_NodeCreationDescription_MappingBasedToolDescription = Generalization(general=MappingBasedToolDescription, specific=diagram_tool_NodeCreationDescription)
gen_diagram_tool_EdgeCreationDescription_MappingBasedToolDescription = Generalization(general=MappingBasedToolDescription, specific=diagram_tool_EdgeCreationDescription)
gen_diagram_tool_ContainerCreationDescription_MappingBasedToolDescription = Generalization(general=MappingBasedToolDescription, specific=diagram_tool_ContainerCreationDescription)
gen_diagram_tool_DeleteElementDescription_MappingBasedToolDescription = Generalization(general=MappingBasedToolDescription, specific=diagram_tool_DeleteElementDescription)
gen_diagram_tool_DoubleClickDescription_MappingBasedToolDescription = Generalization(general=MappingBasedToolDescription, specific=diagram_tool_DoubleClickDescription)
gen_diagram_tool_ReconnectEdgeDescription_MappingBasedToolDescription = Generalization(general=MappingBasedToolDescription, specific=diagram_tool_ReconnectEdgeDescription)
gen_diagram_tool_RequestDescription_AbstractToolDescription = Generalization(general=AbstractToolDescription, specific=diagram_tool_RequestDescription)
gen_diagram_tool_DirectEditLabel_MappingBasedToolDescription = Generalization(general=MappingBasedToolDescription, specific=diagram_tool_DirectEditLabel)
gen_diagram_tool_BehaviorTool_AbstractToolDescription = Generalization(general=AbstractToolDescription, specific=diagram_tool_BehaviorTool)
gen_diagram_tool_SourceEdgeCreationVariable_description_AbstractVariable = Generalization(general=description_AbstractVariable, specific=diagram_tool_SourceEdgeCreationVariable)
gen_diagram_tool_SourceEdgeCreationVariable_tool_VariableContainer = Generalization(general=tool_VariableContainer, specific=diagram_tool_SourceEdgeCreationVariable)
gen_diagram_tool_SourceEdgeViewCreationVariable_description_AbstractVariable = Generalization(general=description_AbstractVariable, specific=diagram_tool_SourceEdgeViewCreationVariable)
gen_diagram_tool_SourceEdgeViewCreationVariable_tool_VariableContainer = Generalization(general=tool_VariableContainer, specific=diagram_tool_SourceEdgeViewCreationVariable)
gen_diagram_tool_TargetEdgeCreationVariable_description_AbstractVariable = Generalization(general=description_AbstractVariable, specific=diagram_tool_TargetEdgeCreationVariable)
gen_diagram_tool_TargetEdgeCreationVariable_tool_VariableContainer = Generalization(general=tool_VariableContainer, specific=diagram_tool_TargetEdgeCreationVariable)
gen_diagram_tool_TargetEdgeViewCreationVariable_description_AbstractVariable = Generalization(general=description_AbstractVariable, specific=diagram_tool_TargetEdgeViewCreationVariable)
gen_diagram_tool_TargetEdgeViewCreationVariable_tool_VariableContainer = Generalization(general=tool_VariableContainer, specific=diagram_tool_TargetEdgeViewCreationVariable)
gen_diagram_tool_ElementDoubleClickVariable_description_AbstractVariable = Generalization(general=description_AbstractVariable, specific=diagram_tool_ElementDoubleClickVariable)
gen_diagram_tool_ElementDoubleClickVariable_tool_VariableContainer = Generalization(general=tool_VariableContainer, specific=diagram_tool_ElementDoubleClickVariable)
gen_diagram_tool_NodeCreationVariable_description_AbstractVariable = Generalization(general=description_AbstractVariable, specific=diagram_tool_NodeCreationVariable)
gen_diagram_tool_NodeCreationVariable_tool_VariableContainer = Generalization(general=tool_VariableContainer, specific=diagram_tool_NodeCreationVariable)
gen_diagram_tool_CreateView_ContainerModelOperation = Generalization(general=ContainerModelOperation, specific=diagram_tool_CreateView)
gen_diagram_tool_CreateEdgeView_CreateView = Generalization(general=CreateView, specific=diagram_tool_CreateEdgeView)
gen_diagram_tool_Navigation_ContainerModelOperation = Generalization(general=ContainerModelOperation, specific=diagram_tool_Navigation)
gen_diagram_tool_DiagramCreationDescription_RepresentationCreationDescription = Generalization(general=RepresentationCreationDescription, specific=diagram_tool_DiagramCreationDescription)
gen_diagram_tool_DiagramNavigationDescription_RepresentationNavigationDescription = Generalization(general=RepresentationNavigationDescription, specific=diagram_tool_DiagramNavigationDescription)
gen_diagram_tool_ContainerDropDescription_MappingBasedToolDescription = Generalization(general=MappingBasedToolDescription, specific=diagram_tool_ContainerDropDescription)
gen_diagram_filter_FilterDescription_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=diagram_filter_FilterDescription)
gen_diagram_filter_FilterDescription_description_IdentifiedElement = Generalization(general=description_IdentifiedElement, specific=diagram_filter_FilterDescription)
gen_diagram_filter_MappingFilter_Filter = Generalization(general=Filter, specific=diagram_filter_MappingFilter)
gen_diagram_filter_CompositeFilterDescription_FilterDescription = Generalization(general=FilterDescription, specific=diagram_filter_CompositeFilterDescription)
gen_diagram_filter_VariableFilter_Filter = Generalization(general=Filter, specific=diagram_filter_VariableFilter)
gen_diagram_concern_ConcernSet_DocumentedElement = Generalization(general=DocumentedElement, specific=diagram_concern_ConcernSet)
gen_diagram_concern_ConcernDescription_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=diagram_concern_ConcernDescription)
gen_diagram_concern_ConcernDescription_description_IdentifiedElement = Generalization(general=description_IdentifiedElement, specific=diagram_concern_ConcernDescription)

# Domain Model
domain_model = DomainModel(
    name="diagram",
    types={diagram_DDiagram, DRepresentation, DragAndDropTarget, diagram_DDiagramElement, DiagramDescription, diagram_DEdge, diagram_DNode, diagram_DNodeListElement, diagram_DDiagramElementContainer, concern_ConcernDescription, filter_FilterDescription, AdditionalLayer, validation_ValidationRule, tool_BehaviorTool, diagram_FilterVariableHistory, Layer, diagram_DSemanticDiagram, DDiagram, DSemanticDecorator, DRepresentationElement, diagram_Decoration, DiagramElementMapping, diagram_GraphicalFilter, IdentifiedElement, diagram_HideFilter, GraphicalFilter, diagram_HideLabelFilter, diagram_FoldingPointFilter, diagram_FoldingFilter, diagram_AppliedCompositeFilters, AbstractDNode, EdgeTarget, diagram_NodeStyle, diagram_Style, NodeMapping, filter_CompositeFilterDescription, diagram_AbsoluteBoundsFilter, diagram_AbstractDNode, DDiagramElement, diagram_ContainerStyle, ContainerMapping, diagram_DNodeContainer, DDiagramElementContainer, diagram_DNodeList, diagram_EdgeStyle, diagram_EdgeTarget, IEdgeMapping, LabelStyle, Style, BorderedStyle, HideLabelCapabilityStyle, diagram_Dot, NodeStyle, diagram_GaugeSection, Customizable, diagram_FlatContainerStyle, ContainerStyle, diagram_ShapeContainerStyle, diagram_Square, diagram_Ellipse, diagram_BundledImage, diagram_WorkspaceImage, diagram_CustomStyle, diagram_Lozenge, diagram_CenterLabelStyle, diagram_EndLabelStyle, diagram_BeginLabelStyle, diagram_GaugeCompositeStyle, diagram_BorderedStyle, diagram_Note, diagram_VariableValue, diagram_CollapseFilter, diagram_IndirectlyCollapseFilter, CollapseFilter, BasicLabelStyle, diagram_EObjectVariableValue, diagram_BracketEdgeStyle, EdgeStyle, diagram_ComputedStyleDescriptionRegistry, style_StyleDescription, diagram_DragAndDropTarget, diagram_HideLabelCapabilityStyle, diagram_TypedVariableValue, VariableValue, TypedVariable, concern_ConcernSet, tool_SelectModelElementVariable, diagram_EObject, diagram_description_DiagramDescription, description_DragAndDropTargetDescription, description_RepresentationDescription, description_PasteTargetDescription, EdgeMapping, validation_ValidationSet, tool_AbstractToolDescription, tool_RepresentationCreationDescription, Layout, tool_InitialOperation, EdgeMappingImport, tool_DirectEditLabel, tool_ToolSection, ColorDescription, diagram_description_DiagramImportDescription, description_RepresentationImportDescription, description_DiagramDescription, diagram_description_DiagramExtensionDescription, RepresentationExtensionDescription, diagram_description_DiagramElementMapping, description_RepresentationElementMapping, tool_DeleteElementDescription, style_NodeStyleDescription, tool_DoubleClickDescription, diagram_description_AbstractNodeMapping, description_DiagramElementMapping, description_DocumentedElement, diagram_description_NodeMapping, description_AbstractNodeMapping, ConditionalNodeStyleDescription, diagram_description_ContainerMapping, style_ContainerStyleDescription, ConditionalContainerStyleDescription, diagram_description_NodeMappingImport, description_NodeMapping, description_AbstractMappingImport, diagram_description_ContainerMappingImport, description_ContainerMapping, diagram_description_EdgeMapping, description_IEdgeMapping, diagram_description_IEdgeMapping, diagram_description_EdgeMappingImport, style_EdgeStyleDescription, ConditionalEdgeStyleDescription, tool_ReconnectEdgeDescription, AbstractNodeMapping, LayoutOption, description_IdentifiedElement, diagram_description_ConditionalNodeStyleDescription, ConditionalStyleDescription, diagram_description_ConditionalEdgeStyleDescription, diagram_description_ConditionalContainerStyleDescription, diagram_description_Layout, DocumentedElement, diagram_description_OrderedTreeLayout, diagram_description_CompositeLayout, diagram_description_CustomLayoutConfiguration, diagram_description_Layer, description_EndUserDocumentedElement, diagram_description_LayoutOption, diagram_description_BooleanLayoutOption, diagram_description_StringLayoutOption, diagram_description_IntegerLayoutOption, diagram_description_DoubleLayoutOption, diagram_description_EnumLayoutOption, EnumOption, EnumLayoutValue, diagram_description_EnumSetLayoutOption, diagram_description_EnumOption, diagram_description_EnumLayoutValue, diagram_description_MappingBasedDecoration, DecorationDescription, diagram_description_DragAndDropTargetDescription, tool_ContainerDropDescription, DecorationDescriptionsSet, Customization, diagram_description_AdditionalLayer, diagram_style_BorderedStyleDescription, StyleDescription, diagram_style_NodeStyleDescription, style_BorderedStyleDescription, style_LabelStyleDescription, style_TooltipStyleDescription, style_HideLabelCapabilityStyleDescription, diagram_style_CustomStyleDescription, NodeStyleDescription, diagram_style_SquareDescription, diagram_style_DotDescription, diagram_style_LozengeNodeDescription, diagram_style_EllipseNodeDescription, diagram_style_BundledImageDescription, diagram_style_NoteDescription, diagram_style_GaugeCompositeStyleDescription, style_GaugeSectionDescription, diagram_style_GaugeSectionDescription, diagram_style_SizeComputationContainerStyleDescription, diagram_style_RoundedCornerStyleDescription, diagram_style_ContainerStyleDescription, style_RoundedCornerStyleDescription, diagram_style_FlatContainerStyleDescription, style_SizeComputationContainerStyleDescription, style_LabelBorderStyleDescription, diagram_style_ShapeContainerStyleDescription, diagram_style_WorkspaceImageDescription, diagram_style_EdgeStyleDescription, style_EndLabelStyleDescription, style_BeginLabelStyleDescription, style_CenterLabelStyleDescription, diagram_style_HideLabelCapabilityStyleDescription, diagram_style_BeginLabelStyleDescription, BasicLabelStyleDescription, diagram_style_CenterLabelStyleDescription, diagram_style_EndLabelStyleDescription, diagram_style_BracketEdgeStyleDescription, EdgeStyleDescription, diagram_tool_ToolSection, tool_ToolEntry, tool_PopupMenu, tool_ToolGroupExtension, tool_GroupMenu, diagram_tool_ToolGroup, ToolEntry, diagram_tool_ToolGroupExtension, tool_ToolGroup, diagram_tool_NodeCreationDescription, MappingBasedToolDescription, tool_NodeCreationVariable, tool_ContainerViewVariable, tool_InitialNodeCreationOperation, diagram_tool_EdgeCreationDescription, tool_SourceEdgeCreationVariable, tool_TargetEdgeCreationVariable, tool_SourceEdgeViewCreationVariable, tool_TargetEdgeViewCreationVariable, tool_InitEdgeCreationOperation, diagram_tool_ContainerCreationDescription, diagram_tool_DeleteElementDescription, tool_ElementDeleteVariable, tool_DeleteHookParameter, tool_DeleteHook, diagram_tool_DoubleClickDescription, tool_ElementDoubleClickVariable, diagram_tool_DeleteHook, diagram_tool_DeleteHookParameter, diagram_tool_ReconnectEdgeDescription, tool_ElementSelectVariable, diagram_tool_RequestDescription, AbstractToolDescription, diagram_tool_DirectEditLabel, tool_EditMaskVariables, diagram_tool_BehaviorTool, diagram_tool_SourceEdgeCreationVariable, description_AbstractVariable, tool_VariableContainer, diagram_tool_SourceEdgeViewCreationVariable, diagram_tool_TargetEdgeCreationVariable, diagram_tool_TargetEdgeViewCreationVariable, diagram_tool_ElementDoubleClickVariable, diagram_tool_NodeCreationVariable, diagram_tool_CreateView, ContainerModelOperation, diagram_tool_CreateEdgeView, CreateView, diagram_tool_Navigation, diagram_tool_DiagramCreationDescription, RepresentationCreationDescription, diagram_tool_DiagramNavigationDescription, RepresentationNavigationDescription, diagram_tool_ContainerDropDescription, tool_DropContainerVariable, tool_ElementDropVariable, InteractiveVariableDescription, tool_InitialContainerDropOperation, diagram_filter_FilterDescription, diagram_filter_Filter, diagram_filter_MappingFilter, Filter, diagram_filter_CompositeFilterDescription, FilterDescription, filter_Filter, diagram_filter_VariableFilter, diagram_concern_ConcernSet, diagram_concern_ConcernDescription, ContainerLayout, LabelPosition, ContainerShape, BackgroundStyle, BundledImageShape, LineStyle, EdgeArrows, EdgeRouting, AlignmentKind, ResizeKind, ArrangeConstraint, FoldingStyle, LayoutDirection, CenteringStyle, LayoutOptionTarget, Side, ReconnectionKind, FilterKind},
    associations={ownedDiagramElements0, diagramElements1, description4, edges6, nodes8, containers12, currentConcern14, activatedFilters16, activatedTransientLayers18, allFilters20, activatedRules23, activateBehaviors25, filterVariableHistory27, nodeListElements10, parentLayers34, decorations37, transientDecorations39, diagramElementMapping42, graphicalFilters44, activatedLayers29, hiddenElements31, ownedStyle49, originalStyle51, actualMapping53, candidatesMapping55, compositeFilterDescriptions46, ownedBorderedNodes47, containers62, elements64, ownedStyle67, originalStyle69, actualMapping72, candidatesMapping74, ownedDiagramElements77, nodes58, originalStyle84, actualMapping87, candidatesMapping90, ownedStyle93, sourceNode95, targetNode96, actualMapping98, ownedElements79, ownedStyle81, originalStyle100, path103, outgoingEdges105, incomingEdges106, beginLabelStyle108, centerLabelStyle110, endLabelStyle112, sections114, ownedValues115, computedStyleDescriptions117, variableDefinition118, concerns128, variableDefinition119, modelElement120, filters122, allEdgeMappings124, validationSet126, layout137, allTools130, defaultConcern132, init135, diagramInitialisation139, defaultLayer141, additionalLayers144, nodeMappings147, edgeMappings150, edgeMappingImports153, containerMappings155, labelDirectEdit179, reusedMappings158, toolSection161, reusedTools163, backgroundColor166, importedDiagram168, layers170, validationSet172, concerns175, deletionDescription178, style187, doubleClickDescription181, borderedNodeMappings182, reusedBorderedNodeMappings184, sourceMapping209, conditionnalStyles188, subNodeMappings190, reusedNodeMappings192, subContainerMappings195, reusedContainerMappings198, style201, conditionnalStyles203, importedMapping205, importedMapping207, targetMapping211, style214, conditionnalStyles216, reconnections218, pathNodeMapping220, importedMapping222, conditionnalStyles224, style227, style229, style231, nodeMapping233, mappings241, layoutOptions235, value236, values237, choices239, dropDescriptions270, nodeMappings243, edgeMappings245, edgeMappingImports248, containerMappings251, reusedMappings254, allTools257, toolSections260, reusedTools263, decorationDescriptionsSet266, customization268, borderColor271, color281, color273, color275, color277, color279, backgroundColor283, sections285, backgroundColor286, foregroundColor288, backgroundColor291, foregroundColor293, labelBorderStyle296, backgroundColor298, strokeColor300, centerLabelStyleDescription304, beginLabelStyleDescription302, endLabelStyleDescription306, centeredSourceMappings308, centeredTargetMappings311, reusedTools320, ownedTools314, subSections315, popupMenus318, groupExtensions323, groups325, tools327, group329, tools330, nodeMappings333, edgeMappings344, variable335, viewVariable337, initialOperation339, extraMappings341, sourceVariable346, targetVariable348, sourceViewVariable350, targetViewVariable352, initialOperation354, viewVariable367, extraSourceMappings356, extraTargetMappings359, containerMappings362, variable364, initialOperation383, initialOperation370, extraMappings373, element376, elementView377, containerView380, parameters398, hook386, mappings388, element391, elementView392, initialOperation395, source399, target401, sourceView404, targetView407, element410, initialOperation412, edgeView415, mask418, initialOperation419, initialOperation422, mapping424, diagramDescription426, diagramDescription428, diagramDescription430, mappings432, oldContainer434, newContainer436, element439, newViewContainer441, ownedVariables449, initialOperation444, mappings446, filters448, ownedConcernDescriptions450, filters452, rules454, behaviors457},
    generalizations={gen_diagram_DDiagram_DRepresentation, gen_diagram_DDiagram_DragAndDropTarget, gen_diagram_DSemanticDiagram_DDiagram, gen_diagram_DSemanticDiagram_DSemanticDecorator, gen_diagram_DDiagramElement_DRepresentationElement, gen_diagram_GraphicalFilter_IdentifiedElement, gen_diagram_HideFilter_GraphicalFilter, gen_diagram_HideLabelFilter_GraphicalFilter, gen_diagram_FoldingPointFilter_GraphicalFilter, gen_diagram_FoldingFilter_GraphicalFilter, gen_diagram_AppliedCompositeFilters_GraphicalFilter, gen_diagram_DNode_AbstractDNode, gen_diagram_DNode_EdgeTarget, gen_diagram_DNode_DragAndDropTarget, gen_diagram_DDiagramElementContainer_AbstractDNode, gen_diagram_DDiagramElementContainer_EdgeTarget, gen_diagram_DDiagramElementContainer_DragAndDropTarget, gen_diagram_AbsoluteBoundsFilter_GraphicalFilter, gen_diagram_AbstractDNode_DDiagramElement, gen_diagram_DNodeContainer_DDiagramElementContainer, gen_diagram_DNodeList_DDiagramElementContainer, gen_diagram_DEdge_DDiagramElement, gen_diagram_DEdge_EdgeTarget, gen_diagram_DNodeListElement_AbstractDNode, gen_diagram_NodeStyle_LabelStyle, gen_diagram_NodeStyle_Style, gen_diagram_NodeStyle_BorderedStyle, gen_diagram_NodeStyle_HideLabelCapabilityStyle, gen_diagram_Dot_NodeStyle, gen_diagram_GaugeSection_Customizable, gen_diagram_FlatContainerStyle_ContainerStyle, gen_diagram_ShapeContainerStyle_ContainerStyle, gen_diagram_Square_NodeStyle, gen_diagram_Ellipse_NodeStyle, gen_diagram_ContainerStyle_LabelStyle, gen_diagram_ContainerStyle_Style, gen_diagram_ContainerStyle_BorderedStyle, gen_diagram_ContainerStyle_HideLabelCapabilityStyle, gen_diagram_BundledImage_NodeStyle, gen_diagram_WorkspaceImage_NodeStyle, gen_diagram_WorkspaceImage_ContainerStyle, gen_diagram_CustomStyle_NodeStyle, gen_diagram_EdgeTarget_IdentifiedElement, gen_diagram_EdgeStyle_Style, gen_diagram_Lozenge_NodeStyle, gen_diagram_GaugeCompositeStyle_NodeStyle, gen_diagram_BorderedStyle_Style, gen_diagram_Note_NodeStyle, gen_diagram_FilterVariableHistory_IdentifiedElement, gen_diagram_EndLabelStyle_BasicLabelStyle, gen_diagram_CollapseFilter_GraphicalFilter, gen_diagram_IndirectlyCollapseFilter_CollapseFilter, gen_diagram_BeginLabelStyle_BasicLabelStyle, gen_diagram_CenterLabelStyle_BasicLabelStyle, gen_diagram_EObjectVariableValue_VariableValue, gen_diagram_BracketEdgeStyle_EdgeStyle, gen_diagram_ComputedStyleDescriptionRegistry_IdentifiedElement, gen_diagram_DragAndDropTarget_IdentifiedElement, gen_diagram_VariableValue_IdentifiedElement, gen_diagram_TypedVariableValue_VariableValue, gen_diagram_description_DiagramDescription_description_DragAndDropTargetDescription, gen_diagram_description_DiagramDescription_description_RepresentationDescription, gen_diagram_description_DiagramDescription_description_PasteTargetDescription, gen_diagram_description_DiagramImportDescription_description_RepresentationImportDescription, gen_diagram_description_DiagramImportDescription_description_DiagramDescription, gen_diagram_description_DiagramExtensionDescription_RepresentationExtensionDescription, gen_diagram_description_DiagramElementMapping_description_RepresentationElementMapping, gen_diagram_description_DiagramElementMapping_description_PasteTargetDescription, gen_diagram_description_AbstractNodeMapping_description_DiagramElementMapping, gen_diagram_description_AbstractNodeMapping_description_DocumentedElement, gen_diagram_description_NodeMapping_description_AbstractNodeMapping, gen_diagram_description_NodeMapping_description_DragAndDropTargetDescription, gen_diagram_description_ContainerMapping_description_AbstractNodeMapping, gen_diagram_description_ContainerMapping_description_DragAndDropTargetDescription, gen_diagram_description_NodeMappingImport_description_NodeMapping, gen_diagram_description_NodeMappingImport_description_AbstractMappingImport, gen_diagram_description_ContainerMappingImport_description_ContainerMapping, gen_diagram_description_ContainerMappingImport_description_AbstractMappingImport, gen_diagram_description_EdgeMapping_description_DiagramElementMapping, gen_diagram_description_EdgeMapping_description_DocumentedElement, gen_diagram_description_EdgeMapping_description_IEdgeMapping, gen_diagram_description_EdgeMappingImport_description_DocumentedElement, gen_diagram_description_EdgeMappingImport_description_IEdgeMapping, gen_diagram_description_EdgeMappingImport_description_IdentifiedElement, gen_diagram_description_ConditionalNodeStyleDescription_ConditionalStyleDescription, gen_diagram_description_ConditionalEdgeStyleDescription_ConditionalStyleDescription, gen_diagram_description_ConditionalContainerStyleDescription_ConditionalStyleDescription, gen_diagram_description_Layout_DocumentedElement, gen_diagram_description_OrderedTreeLayout_Layout, gen_diagram_description_CompositeLayout_Layout, gen_diagram_description_CustomLayoutConfiguration_Layout, gen_diagram_description_Layer_description_DocumentedElement, gen_diagram_description_Layer_description_EndUserDocumentedElement, gen_diagram_description_Layer_description_IdentifiedElement, gen_diagram_description_BooleanLayoutOption_LayoutOption, gen_diagram_description_StringLayoutOption_LayoutOption, gen_diagram_description_IntegerLayoutOption_LayoutOption, gen_diagram_description_DoubleLayoutOption_LayoutOption, gen_diagram_description_EnumLayoutOption_EnumOption, gen_diagram_description_EnumSetLayoutOption_EnumOption, gen_diagram_description_EnumOption_LayoutOption, gen_diagram_description_MappingBasedDecoration_DecorationDescription, gen_diagram_description_AdditionalLayer_Layer, gen_diagram_style_BorderedStyleDescription_StyleDescription, gen_diagram_style_NodeStyleDescription_style_StyleDescription, gen_diagram_style_NodeStyleDescription_style_BorderedStyleDescription, gen_diagram_style_NodeStyleDescription_style_LabelStyleDescription, gen_diagram_style_NodeStyleDescription_style_TooltipStyleDescription, gen_diagram_style_NodeStyleDescription_style_HideLabelCapabilityStyleDescription, gen_diagram_style_CustomStyleDescription_NodeStyleDescription, gen_diagram_style_SquareDescription_NodeStyleDescription, gen_diagram_style_DotDescription_NodeStyleDescription, gen_diagram_style_LozengeNodeDescription_NodeStyleDescription, gen_diagram_style_EllipseNodeDescription_NodeStyleDescription, gen_diagram_style_BundledImageDescription_NodeStyleDescription, gen_diagram_style_NoteDescription_NodeStyleDescription, gen_diagram_style_GaugeCompositeStyleDescription_NodeStyleDescription, gen_diagram_style_RoundedCornerStyleDescription_StyleDescription, gen_diagram_style_ContainerStyleDescription_style_RoundedCornerStyleDescription, gen_diagram_style_ContainerStyleDescription_style_BorderedStyleDescription, gen_diagram_style_ContainerStyleDescription_style_LabelStyleDescription, gen_diagram_style_ContainerStyleDescription_style_TooltipStyleDescription, gen_diagram_style_ContainerStyleDescription_style_HideLabelCapabilityStyleDescription, gen_diagram_style_FlatContainerStyleDescription_style_ContainerStyleDescription, gen_diagram_style_FlatContainerStyleDescription_style_SizeComputationContainerStyleDescription, gen_diagram_style_ShapeContainerStyleDescription_style_ContainerStyleDescription, gen_diagram_style_ShapeContainerStyleDescription_style_SizeComputationContainerStyleDescription, gen_diagram_style_WorkspaceImageDescription_style_NodeStyleDescription, gen_diagram_style_WorkspaceImageDescription_style_ContainerStyleDescription, gen_diagram_style_EdgeStyleDescription_StyleDescription, gen_diagram_style_BeginLabelStyleDescription_BasicLabelStyleDescription, gen_diagram_style_CenterLabelStyleDescription_BasicLabelStyleDescription, gen_diagram_style_EndLabelStyleDescription_BasicLabelStyleDescription, gen_diagram_style_BracketEdgeStyleDescription_EdgeStyleDescription, gen_diagram_tool_ToolSection_description_DocumentedElement, gen_diagram_tool_ToolSection_description_IdentifiedElement, gen_diagram_tool_ToolGroup_ToolEntry, gen_diagram_tool_NodeCreationDescription_MappingBasedToolDescription, gen_diagram_tool_EdgeCreationDescription_MappingBasedToolDescription, gen_diagram_tool_ContainerCreationDescription_MappingBasedToolDescription, gen_diagram_tool_DeleteElementDescription_MappingBasedToolDescription, gen_diagram_tool_DoubleClickDescription_MappingBasedToolDescription, gen_diagram_tool_ReconnectEdgeDescription_MappingBasedToolDescription, gen_diagram_tool_RequestDescription_AbstractToolDescription, gen_diagram_tool_DirectEditLabel_MappingBasedToolDescription, gen_diagram_tool_BehaviorTool_AbstractToolDescription, gen_diagram_tool_SourceEdgeCreationVariable_description_AbstractVariable, gen_diagram_tool_SourceEdgeCreationVariable_tool_VariableContainer, gen_diagram_tool_SourceEdgeViewCreationVariable_description_AbstractVariable, gen_diagram_tool_SourceEdgeViewCreationVariable_tool_VariableContainer, gen_diagram_tool_TargetEdgeCreationVariable_description_AbstractVariable, gen_diagram_tool_TargetEdgeCreationVariable_tool_VariableContainer, gen_diagram_tool_TargetEdgeViewCreationVariable_description_AbstractVariable, gen_diagram_tool_TargetEdgeViewCreationVariable_tool_VariableContainer, gen_diagram_tool_ElementDoubleClickVariable_description_AbstractVariable, gen_diagram_tool_ElementDoubleClickVariable_tool_VariableContainer, gen_diagram_tool_NodeCreationVariable_description_AbstractVariable, gen_diagram_tool_NodeCreationVariable_tool_VariableContainer, gen_diagram_tool_CreateView_ContainerModelOperation, gen_diagram_tool_CreateEdgeView_CreateView, gen_diagram_tool_Navigation_ContainerModelOperation, gen_diagram_tool_DiagramCreationDescription_RepresentationCreationDescription, gen_diagram_tool_DiagramNavigationDescription_RepresentationNavigationDescription, gen_diagram_tool_ContainerDropDescription_MappingBasedToolDescription, gen_diagram_filter_FilterDescription_description_DocumentedElement, gen_diagram_filter_FilterDescription_description_IdentifiedElement, gen_diagram_filter_MappingFilter_Filter, gen_diagram_filter_CompositeFilterDescription_FilterDescription, gen_diagram_filter_VariableFilter_Filter, gen_diagram_concern_ConcernSet_DocumentedElement, gen_diagram_concern_ConcernDescription_description_DocumentedElement, gen_diagram_concern_ConcernDescription_description_IdentifiedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)