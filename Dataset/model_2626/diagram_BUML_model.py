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
			EnumerationLiteral(name="InputFillClosedArrow"),
			EnumerationLiteral(name="Diamond"),
			EnumerationLiteral(name="FillDiamond"),
			EnumerationLiteral(name="InputArrowWithDiamond"),
			EnumerationLiteral(name="InputArrowWithFillDiamond")
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
diagram_DEdge = Class(name="diagram::DEdge")
diagram_DNode = Class(name="diagram::DNode")
diagram_DDiagram = Class(name="diagram::DDiagram")
DRepresentation = Class(name="DRepresentation")
description_DocumentedElement = Class(name="description::DocumentedElement")
DragAndDropTarget = Class(name="DragAndDropTarget")
diagram_DDiagramElement = Class(name="diagram::DDiagramElement", is_abstract=True)
DiagramDescription = Class(name="DiagramDescription")
diagram_DNodeListElement = Class(name="diagram::DNodeListElement")
diagram_DDiagramElementContainer = Class(name="diagram::DDiagramElementContainer", is_abstract=True)
concern_ConcernDescription = Class(name="concern::ConcernDescription")
filter_FilterDescription = Class(name="filter::FilterDescription")
validation_ValidationRule = Class(name="validation::ValidationRule")
tool_BehaviorTool = Class(name="tool::BehaviorTool")
diagram_FilterVariableHistory = Class(name="diagram::FilterVariableHistory")
Layer = Class(name="Layer")
diagram_AbsoluteBoundsFilter = Class(name="diagram::AbsoluteBoundsFilter")
diagram_DSemanticDiagram = Class(name="diagram::DSemanticDiagram")
DDiagram = Class(name="DDiagram")
DSemanticDecorator = Class(name="DSemanticDecorator")
DRepresentationElement = Class(name="DRepresentationElement")
diagram_Decoration = Class(name="diagram::Decoration")
DiagramElementMapping = Class(name="DiagramElementMapping")
diagram_GraphicalFilter = Class(name="diagram::GraphicalFilter", is_abstract=True)
diagram_HideFilter = Class(name="diagram::HideFilter")
GraphicalFilter = Class(name="GraphicalFilter")
diagram_HideLabelFilter = Class(name="diagram::HideLabelFilter")
diagram_FoldingPointFilter = Class(name="diagram::FoldingPointFilter")
diagram_FoldingFilter = Class(name="diagram::FoldingFilter")
diagram_AppliedCompositeFilters = Class(name="diagram::AppliedCompositeFilters")
filter_CompositeFilterDescription = Class(name="filter::CompositeFilterDescription")
diagram_AbstractDNode = Class(name="diagram::AbstractDNode", is_abstract=True)
DDiagramElement = Class(name="DDiagramElement")
AbstractDNode = Class(name="AbstractDNode")
EdgeTarget = Class(name="EdgeTarget")
diagram_NodeStyle = Class(name="diagram::NodeStyle", is_abstract=True)
diagram_Style = Class(name="diagram::Style")
NodeMapping = Class(name="NodeMapping")
diagram_DNodeList = Class(name="diagram::DNodeList")
diagram_ContainerStyle = Class(name="diagram::ContainerStyle", is_abstract=True)
ContainerMapping = Class(name="ContainerMapping")
diagram_DNodeContainer = Class(name="diagram::DNodeContainer")
DDiagramElementContainer = Class(name="DDiagramElementContainer")
IEdgeMapping = Class(name="IEdgeMapping")
diagram_EdgeStyle = Class(name="diagram::EdgeStyle")
diagram_EdgeTarget = Class(name="diagram::EdgeTarget", is_abstract=True)
diagram_GaugeSection = Class(name="diagram::GaugeSection")
Customizable = Class(name="Customizable")
LabelStyle = Class(name="LabelStyle")
Style = Class(name="Style")
BorderedStyle = Class(name="BorderedStyle")
HideLabelCapabilityStyle = Class(name="HideLabelCapabilityStyle")
diagram_Dot = Class(name="diagram::Dot")
NodeStyle = Class(name="NodeStyle")
diagram_Square = Class(name="diagram::Square")
diagram_FlatContainerStyle = Class(name="diagram::FlatContainerStyle")
ContainerStyle = Class(name="ContainerStyle")
diagram_ShapeContainerStyle = Class(name="diagram::ShapeContainerStyle")
diagram_Ellipse = Class(name="diagram::Ellipse")
diagram_Lozenge = Class(name="diagram::Lozenge")
diagram_BundledImage = Class(name="diagram::BundledImage")
diagram_WorkspaceImage = Class(name="diagram::WorkspaceImage")
diagram_CustomStyle = Class(name="diagram::CustomStyle")
diagram_BeginLabelStyle = Class(name="diagram::BeginLabelStyle")
diagram_CenterLabelStyle = Class(name="diagram::CenterLabelStyle")
diagram_EndLabelStyle = Class(name="diagram::EndLabelStyle")
diagram_Note = Class(name="diagram::Note")
diagram_GaugeCompositeStyle = Class(name="diagram::GaugeCompositeStyle")
diagram_BorderedStyle = Class(name="diagram::BorderedStyle")
diagram_HideLabelCapabilityStyle = Class(name="diagram::HideLabelCapabilityStyle", is_abstract=True)
diagram_VariableValue = Class(name="diagram::VariableValue", is_abstract=True)
diagram_TypedVariableValue = Class(name="diagram::TypedVariableValue")
VariableValue = Class(name="VariableValue")
TypedVariable = Class(name="TypedVariable")
diagram_EObjectVariableValue = Class(name="diagram::EObjectVariableValue")
tool_SelectModelElementVariable = Class(name="tool::SelectModelElementVariable")
diagram_CollapseFilter = Class(name="diagram::CollapseFilter")
diagram_EObject = Class(name="diagram::EObject")
diagram_description_DiagramDescription = Class(name="diagram::description::DiagramDescription")
description_DragAndDropTargetDescription = Class(name="description::DragAndDropTargetDescription")
diagram_IndirectlyCollapseFilter = Class(name="diagram::IndirectlyCollapseFilter")
description_RepresentationDescription = Class(name="description::RepresentationDescription")
CollapseFilter = Class(name="CollapseFilter")
description_PasteTargetDescription = Class(name="description::PasteTargetDescription")
BasicLabelStyle = Class(name="BasicLabelStyle")
diagram_BracketEdgeStyle = Class(name="diagram::BracketEdgeStyle")
EdgeStyle = Class(name="EdgeStyle")
diagram_ComputedStyleDescriptionRegistry = Class(name="diagram::ComputedStyleDescriptionRegistry")
style_StyleDescription = Class(name="style::StyleDescription")
diagram_DragAndDropTarget = Class(name="diagram::DragAndDropTarget")
validation_ValidationSet = Class(name="validation::ValidationSet")
concern_ConcernSet = Class(name="concern::ConcernSet")
tool_AbstractToolDescription = Class(name="tool::AbstractToolDescription")
EdgeMapping = Class(name="EdgeMapping")
tool_RepresentationCreationDescription = Class(name="tool::RepresentationCreationDescription")
Layout = Class(name="Layout")
tool_InitialOperation = Class(name="tool::InitialOperation")
diagram_description_DiagramImportDescription = Class(name="diagram::description::DiagramImportDescription")
AdditionalLayer = Class(name="AdditionalLayer")
EdgeMappingImport = Class(name="EdgeMappingImport")
tool_ToolSection = Class(name="tool::ToolSection")
tool_DeleteElementDescription = Class(name="tool::DeleteElementDescription")
description_RepresentationImportDescription = Class(name="description::RepresentationImportDescription")
description_DiagramDescription = Class(name="description::DiagramDescription")
diagram_description_DiagramExtensionDescription = Class(name="diagram::description::DiagramExtensionDescription")
RepresentationExtensionDescription = Class(name="RepresentationExtensionDescription")
diagram_description_DiagramElementMapping = Class(name="diagram::description::DiagramElementMapping", is_abstract=True)
description_RepresentationElementMapping = Class(name="description::RepresentationElementMapping")
diagram_description_NodeMapping = Class(name="diagram::description::NodeMapping")
description_AbstractNodeMapping = Class(name="description::AbstractNodeMapping")
tool_DirectEditLabel = Class(name="tool::DirectEditLabel")
tool_DoubleClickDescription = Class(name="tool::DoubleClickDescription")
diagram_description_AbstractNodeMapping = Class(name="diagram::description::AbstractNodeMapping", is_abstract=True)
description_DiagramElementMapping = Class(name="description::DiagramElementMapping")
diagram_description_ContainerMapping = Class(name="diagram::description::ContainerMapping")
style_NodeStyleDescription = Class(name="style::NodeStyleDescription")
ConditionalNodeStyleDescription = Class(name="ConditionalNodeStyleDescription")
diagram_description_EdgeMapping = Class(name="diagram::description::EdgeMapping")
description_IEdgeMapping = Class(name="description::IEdgeMapping")
style_ContainerStyleDescription = Class(name="style::ContainerStyleDescription")
ConditionalContainerStyleDescription = Class(name="ConditionalContainerStyleDescription")
diagram_description_NodeMappingImport = Class(name="diagram::description::NodeMappingImport")
description_NodeMapping = Class(name="description::NodeMapping")
description_AbstractMappingImport = Class(name="description::AbstractMappingImport")
diagram_description_ContainerMappingImport = Class(name="diagram::description::ContainerMappingImport")
description_ContainerMapping = Class(name="description::ContainerMapping")
ConditionalEdgeStyleDescription = Class(name="ConditionalEdgeStyleDescription")
diagram_description_OrderedTreeLayout = Class(name="diagram::description::OrderedTreeLayout")
style_EdgeStyleDescription = Class(name="style::EdgeStyleDescription")
tool_ReconnectEdgeDescription = Class(name="tool::ReconnectEdgeDescription")
AbstractNodeMapping = Class(name="AbstractNodeMapping")
diagram_description_IEdgeMapping = Class(name="diagram::description::IEdgeMapping", is_abstract=True)
diagram_description_EdgeMappingImport = Class(name="diagram::description::EdgeMappingImport")
description_IdentifiedElement = Class(name="description::IdentifiedElement")
diagram_description_ConditionalNodeStyleDescription = Class(name="diagram::description::ConditionalNodeStyleDescription")
ConditionalStyleDescription = Class(name="ConditionalStyleDescription")
diagram_description_ConditionalEdgeStyleDescription = Class(name="diagram::description::ConditionalEdgeStyleDescription")
diagram_description_ConditionalContainerStyleDescription = Class(name="diagram::description::ConditionalContainerStyleDescription")
diagram_description_Layout = Class(name="diagram::description::Layout", is_abstract=True)
DocumentedElement = Class(name="DocumentedElement")
DecorationDescriptionsSet = Class(name="DecorationDescriptionsSet")
diagram_description_CompositeLayout = Class(name="diagram::description::CompositeLayout")
diagram_description_MappingBasedDecoration = Class(name="diagram::description::MappingBasedDecoration")
DecorationDescription = Class(name="DecorationDescription")
diagram_description_Layer = Class(name="diagram::description::Layer")
description_EndUserDocumentedElement = Class(name="description::EndUserDocumentedElement")
diagram_style_NodeStyleDescription = Class(name="diagram::style::NodeStyleDescription", is_abstract=True)
style_BorderedStyleDescription = Class(name="style::BorderedStyleDescription")
style_LabelStyleDescription = Class(name="style::LabelStyleDescription")
style_TooltipStyleDescription = Class(name="style::TooltipStyleDescription")
style_HideLabelCapabilityStyleDescription = Class(name="style::HideLabelCapabilityStyleDescription")
Customization = Class(name="Customization")
diagram_style_CustomStyleDescription = Class(name="diagram::style::CustomStyleDescription")
NodeStyleDescription = Class(name="NodeStyleDescription")
diagram_description_AdditionalLayer = Class(name="diagram::description::AdditionalLayer")
diagram_description_DragAndDropTargetDescription = Class(name="diagram::description::DragAndDropTargetDescription", is_abstract=True)
tool_ContainerDropDescription = Class(name="tool::ContainerDropDescription")
diagram_style_BorderedStyleDescription = Class(name="diagram::style::BorderedStyleDescription")
StyleDescription = Class(name="StyleDescription")
ColorDescription = Class(name="ColorDescription")
diagram_style_BundledImageDescription = Class(name="diagram::style::BundledImageDescription")
diagram_style_SquareDescription = Class(name="diagram::style::SquareDescription")
diagram_style_LozengeNodeDescription = Class(name="diagram::style::LozengeNodeDescription")
diagram_style_EllipseNodeDescription = Class(name="diagram::style::EllipseNodeDescription")
diagram_style_NoteDescription = Class(name="diagram::style::NoteDescription")
diagram_style_DotDescription = Class(name="diagram::style::DotDescription")
diagram_style_GaugeCompositeStyleDescription = Class(name="diagram::style::GaugeCompositeStyleDescription")
style_GaugeSectionDescription = Class(name="style::GaugeSectionDescription")
diagram_style_GaugeSectionDescription = Class(name="diagram::style::GaugeSectionDescription")
style_LabelBorderStyleDescription = Class(name="style::LabelBorderStyleDescription")
diagram_style_ShapeContainerStyleDescription = Class(name="diagram::style::ShapeContainerStyleDescription")
diagram_style_WorkspaceImageDescription = Class(name="diagram::style::WorkspaceImageDescription")
diagram_style_SizeComputationContainerStyleDescription = Class(name="diagram::style::SizeComputationContainerStyleDescription", is_abstract=True)
diagram_style_RoundedCornerStyleDescription = Class(name="diagram::style::RoundedCornerStyleDescription", is_abstract=True)
diagram_style_ContainerStyleDescription = Class(name="diagram::style::ContainerStyleDescription", is_abstract=True)
style_RoundedCornerStyleDescription = Class(name="style::RoundedCornerStyleDescription")
diagram_style_FlatContainerStyleDescription = Class(name="diagram::style::FlatContainerStyleDescription")
style_SizeComputationContainerStyleDescription = Class(name="style::SizeComputationContainerStyleDescription")
style_BeginLabelStyleDescription = Class(name="style::BeginLabelStyleDescription")
style_CenterLabelStyleDescription = Class(name="style::CenterLabelStyleDescription")
style_EndLabelStyleDescription = Class(name="style::EndLabelStyleDescription")
diagram_style_BeginLabelStyleDescription = Class(name="diagram::style::BeginLabelStyleDescription")
BasicLabelStyleDescription = Class(name="BasicLabelStyleDescription")
diagram_style_EdgeStyleDescription = Class(name="diagram::style::EdgeStyleDescription")
tool_PopupMenu = Class(name="tool::PopupMenu")
tool_ToolGroupExtension = Class(name="tool::ToolGroupExtension")
diagram_tool_ToolGroup = Class(name="diagram::tool::ToolGroup")
ToolEntry = Class(name="ToolEntry")
diagram_tool_ToolGroupExtension = Class(name="diagram::tool::ToolGroupExtension")
tool_ToolGroup = Class(name="tool::ToolGroup")
diagram_style_CenterLabelStyleDescription = Class(name="diagram::style::CenterLabelStyleDescription")
diagram_style_EndLabelStyleDescription = Class(name="diagram::style::EndLabelStyleDescription")
diagram_style_BracketEdgeStyleDescription = Class(name="diagram::style::BracketEdgeStyleDescription")
EdgeStyleDescription = Class(name="EdgeStyleDescription")
diagram_style_HideLabelCapabilityStyleDescription = Class(name="diagram::style::HideLabelCapabilityStyleDescription", is_abstract=True)
diagram_tool_ToolSection = Class(name="diagram::tool::ToolSection")
tool_ToolEntry = Class(name="tool::ToolEntry")
tool_InitialNodeCreationOperation = Class(name="tool::InitialNodeCreationOperation")
diagram_tool_NodeCreationDescription = Class(name="diagram::tool::NodeCreationDescription")
MappingBasedToolDescription = Class(name="MappingBasedToolDescription")
tool_NodeCreationVariable = Class(name="tool::NodeCreationVariable")
tool_ContainerViewVariable = Class(name="tool::ContainerViewVariable")
tool_TargetEdgeCreationVariable = Class(name="tool::TargetEdgeCreationVariable")
tool_SourceEdgeViewCreationVariable = Class(name="tool::SourceEdgeViewCreationVariable")
tool_TargetEdgeViewCreationVariable = Class(name="tool::TargetEdgeViewCreationVariable")
tool_InitEdgeCreationOperation = Class(name="tool::InitEdgeCreationOperation")
diagram_tool_EdgeCreationDescription = Class(name="diagram::tool::EdgeCreationDescription")
tool_SourceEdgeCreationVariable = Class(name="tool::SourceEdgeCreationVariable")
diagram_tool_DeleteElementDescription = Class(name="diagram::tool::DeleteElementDescription")
tool_ElementDeleteVariable = Class(name="tool::ElementDeleteVariable")
diagram_tool_ContainerCreationDescription = Class(name="diagram::tool::ContainerCreationDescription")
tool_DeleteHookParameter = Class(name="tool::DeleteHookParameter")
diagram_tool_DeleteHookParameter = Class(name="diagram::tool::DeleteHookParameter")
diagram_tool_ReconnectEdgeDescription = Class(name="diagram::tool::ReconnectEdgeDescription")
tool_DeleteHook = Class(name="tool::DeleteHook")
diagram_tool_DoubleClickDescription = Class(name="diagram::tool::DoubleClickDescription")
tool_ElementDoubleClickVariable = Class(name="tool::ElementDoubleClickVariable")
diagram_tool_DeleteHook = Class(name="diagram::tool::DeleteHook")
AbstractToolDescription = Class(name="AbstractToolDescription")
diagram_tool_DirectEditLabel = Class(name="diagram::tool::DirectEditLabel")
tool_EditMaskVariables = Class(name="tool::EditMaskVariables")
diagram_tool_BehaviorTool = Class(name="diagram::tool::BehaviorTool")
tool_ElementSelectVariable = Class(name="tool::ElementSelectVariable")
diagram_tool_RequestDescription = Class(name="diagram::tool::RequestDescription")
diagram_tool_CreateEdgeView = Class(name="diagram::tool::CreateEdgeView")
CreateView = Class(name="CreateView")
diagram_tool_Navigation = Class(name="diagram::tool::Navigation")
diagram_tool_DiagramCreationDescription = Class(name="diagram::tool::DiagramCreationDescription")
RepresentationCreationDescription = Class(name="RepresentationCreationDescription")
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
tool_ElementDropVariable = Class(name="tool::ElementDropVariable")
tool_InitialContainerDropOperation = Class(name="tool::InitialContainerDropOperation")
diagram_filter_FilterDescription = Class(name="diagram::filter::FilterDescription", is_abstract=True)
diagram_tool_DiagramNavigationDescription = Class(name="diagram::tool::DiagramNavigationDescription")
RepresentationNavigationDescription = Class(name="RepresentationNavigationDescription")
diagram_tool_ContainerDropDescription = Class(name="diagram::tool::ContainerDropDescription")
tool_DropContainerVariable = Class(name="tool::DropContainerVariable")
diagram_filter_CompositeFilterDescription = Class(name="diagram::filter::CompositeFilterDescription")
FilterDescription = Class(name="FilterDescription")
filter_Filter = Class(name="filter::Filter")
diagram_filter_VariableFilter = Class(name="diagram::filter::VariableFilter")
InteractiveVariableDescription = Class(name="InteractiveVariableDescription")
diagram_concern_ConcernSet = Class(name="diagram::concern::ConcernSet")
diagram_filter_Filter = Class(name="diagram::filter::Filter", is_abstract=True)
diagram_concern_ConcernDescription = Class(name="diagram::concern::ConcernDescription")
diagram_filter_MappingFilter = Class(name="diagram::filter::MappingFilter")
Filter = Class(name="Filter")

# diagram_DEdge class attributes and methods
diagram_DEdge_routingStyle: Property = Property(name="routingStyle", type=StringType)
diagram_DEdge_size: Property = Property(name="size", type=StringType)
diagram_DEdge_isFold: Property = Property(name="isFold", type=BooleanType)
diagram_DEdge_isMockEdge: Property = Property(name="isMockEdge", type=BooleanType)
diagram_DEdge_arrangeConstraints: Property = Property(name="arrangeConstraints", type=StringType)
diagram_DEdge_beginLabel: Property = Property(name="beginLabel", type=StringType)
diagram_DEdge_endLabel: Property = Property(name="endLabel", type=StringType)
diagram_DEdge_m_isRootFolding: Method = Method(name="isRootFolding", parameters={}, type=BooleanType)
diagram_DEdge.attributes={diagram_DEdge_isMockEdge, diagram_DEdge_isFold, diagram_DEdge_beginLabel, diagram_DEdge_routingStyle, diagram_DEdge_endLabel, diagram_DEdge_size, diagram_DEdge_arrangeConstraints}
diagram_DEdge.methods={diagram_DEdge_m_isRootFolding}

# diagram_DNode class attributes and methods
diagram_DNode_width: Property = Property(name="width", type=StringType)
diagram_DNode_height: Property = Property(name="height", type=StringType)
diagram_DNode_labelPosition: Property = Property(name="labelPosition", type=StringType)
diagram_DNode_resizeKind: Property = Property(name="resizeKind", type=StringType)
diagram_DNode.attributes={diagram_DNode_height, diagram_DNode_labelPosition, diagram_DNode_width, diagram_DNode_resizeKind}

# diagram_DDiagram class attributes and methods
diagram_DDiagram_isInLayoutingMode: Property = Property(name="isInLayoutingMode", type=BooleanType)
diagram_DDiagram_headerHeight: Property = Property(name="headerHeight", type=IntegerType)
diagram_DDiagram_synchronized: Property = Property(name="synchronized", type=BooleanType)
diagram_DDiagram_m_getNodesFromMapping: Method = Method(name="getNodesFromMapping", parameters={Parameter(name='mapping')}, type=StringType)
diagram_DDiagram_m_getEdgesFromMapping: Method = Method(name="getEdgesFromMapping", parameters={Parameter(name='mapping')}, type=StringType)
diagram_DDiagram_m_getContainersFromMapping: Method = Method(name="getContainersFromMapping", parameters={Parameter(name='mapping')}, type=StringType)
diagram_DDiagram.attributes={diagram_DDiagram_isInLayoutingMode, diagram_DDiagram_headerHeight, diagram_DDiagram_synchronized}
diagram_DDiagram.methods={diagram_DDiagram_m_getNodesFromMapping, diagram_DDiagram_m_getEdgesFromMapping, diagram_DDiagram_m_getContainersFromMapping}

# DRepresentation class attributes and methods

# description_DocumentedElement class attributes and methods

# DragAndDropTarget class attributes and methods

# diagram_DDiagramElement class attributes and methods
diagram_DDiagramElement_visible: Property = Property(name="visible", type=BooleanType)
diagram_DDiagramElement_tooltipText: Property = Property(name="tooltipText", type=StringType)
diagram_DDiagramElement_m_getParentDiagram: Method = Method(name="getParentDiagram", parameters={}, type=DDiagram)
diagram_DDiagramElement.attributes={diagram_DDiagramElement_tooltipText, diagram_DDiagramElement_visible}
diagram_DDiagramElement.methods={diagram_DDiagramElement_m_getParentDiagram}

# DiagramDescription class attributes and methods

# diagram_DNodeListElement class attributes and methods

# diagram_DDiagramElementContainer class attributes and methods
diagram_DDiagramElementContainer_width: Property = Property(name="width", type=StringType)
diagram_DDiagramElementContainer_height: Property = Property(name="height", type=StringType)
diagram_DDiagramElementContainer_m_getContainersFromMapping: Method = Method(name="getContainersFromMapping", parameters={Parameter(name='mapping')}, type=StringType)
diagram_DDiagramElementContainer_m_getNodesFromMapping: Method = Method(name="getNodesFromMapping", parameters={Parameter(name='mapping')}, type=StringType)
diagram_DDiagramElementContainer.attributes={diagram_DDiagramElementContainer_height, diagram_DDiagramElementContainer_width}
diagram_DDiagramElementContainer.methods={diagram_DDiagramElementContainer_m_getContainersFromMapping, diagram_DDiagramElementContainer_m_getNodesFromMapping}

# concern_ConcernDescription class attributes and methods

# filter_FilterDescription class attributes and methods

# validation_ValidationRule class attributes and methods

# tool_BehaviorTool class attributes and methods

# diagram_FilterVariableHistory class attributes and methods

# Layer class attributes and methods

# diagram_AbsoluteBoundsFilter class attributes and methods
diagram_AbsoluteBoundsFilter_x: Property = Property(name="x", type=StringType)
diagram_AbsoluteBoundsFilter_y: Property = Property(name="y", type=StringType)
diagram_AbsoluteBoundsFilter_height: Property = Property(name="height", type=StringType)
diagram_AbsoluteBoundsFilter_width: Property = Property(name="width", type=StringType)
diagram_AbsoluteBoundsFilter.attributes={diagram_AbsoluteBoundsFilter_height, diagram_AbsoluteBoundsFilter_y, diagram_AbsoluteBoundsFilter_width, diagram_AbsoluteBoundsFilter_x}

# diagram_DSemanticDiagram class attributes and methods

# DDiagram class attributes and methods

# DSemanticDecorator class attributes and methods

# DRepresentationElement class attributes and methods

# diagram_Decoration class attributes and methods

# DiagramElementMapping class attributes and methods

# diagram_GraphicalFilter class attributes and methods

# diagram_HideFilter class attributes and methods

# GraphicalFilter class attributes and methods

# diagram_HideLabelFilter class attributes and methods

# diagram_FoldingPointFilter class attributes and methods

# diagram_FoldingFilter class attributes and methods

# diagram_AppliedCompositeFilters class attributes and methods

# filter_CompositeFilterDescription class attributes and methods

# diagram_AbstractDNode class attributes and methods
diagram_AbstractDNode_arrangeConstraints: Property = Property(name="arrangeConstraints", type=StringType)
diagram_AbstractDNode.attributes={diagram_AbstractDNode_arrangeConstraints}

# DDiagramElement class attributes and methods

# AbstractDNode class attributes and methods

# EdgeTarget class attributes and methods

# diagram_NodeStyle class attributes and methods
diagram_NodeStyle_labelPosition: Property = Property(name="labelPosition", type=StringType)
diagram_NodeStyle.attributes={diagram_NodeStyle_labelPosition}

# diagram_Style class attributes and methods

# NodeMapping class attributes and methods

# diagram_DNodeList class attributes and methods

# diagram_ContainerStyle class attributes and methods

# ContainerMapping class attributes and methods

# diagram_DNodeContainer class attributes and methods
diagram_DNodeContainer_childrenPresentation: Property = Property(name="childrenPresentation", type=StringType)
diagram_DNodeContainer.attributes={diagram_DNodeContainer_childrenPresentation}

# DDiagramElementContainer class attributes and methods

# IEdgeMapping class attributes and methods

# diagram_EdgeStyle class attributes and methods
diagram_EdgeStyle_lineStyle: Property = Property(name="lineStyle", type=StringType)
diagram_EdgeStyle_sourceArrow: Property = Property(name="sourceArrow", type=StringType)
diagram_EdgeStyle_targetArrow: Property = Property(name="targetArrow", type=StringType)
diagram_EdgeStyle_foldingStyle: Property = Property(name="foldingStyle", type=StringType)
diagram_EdgeStyle_size: Property = Property(name="size", type=StringType)
diagram_EdgeStyle_routingStyle: Property = Property(name="routingStyle", type=StringType)
diagram_EdgeStyle_centered: Property = Property(name="centered", type=StringType)
diagram_EdgeStyle_strokeColor: Property = Property(name="strokeColor", type=StringType)
diagram_EdgeStyle.attributes={diagram_EdgeStyle_centered, diagram_EdgeStyle_targetArrow, diagram_EdgeStyle_sourceArrow, diagram_EdgeStyle_strokeColor, diagram_EdgeStyle_foldingStyle, diagram_EdgeStyle_size, diagram_EdgeStyle_routingStyle, diagram_EdgeStyle_lineStyle}

# diagram_EdgeTarget class attributes and methods

# diagram_GaugeSection class attributes and methods
diagram_GaugeSection_min: Property = Property(name="min", type=StringType)
diagram_GaugeSection_max: Property = Property(name="max", type=StringType)
diagram_GaugeSection_value: Property = Property(name="value", type=StringType)
diagram_GaugeSection_label: Property = Property(name="label", type=StringType)
diagram_GaugeSection_backgroundColor: Property = Property(name="backgroundColor", type=StringType)
diagram_GaugeSection_foregroundColor: Property = Property(name="foregroundColor", type=StringType)
diagram_GaugeSection.attributes={diagram_GaugeSection_backgroundColor, diagram_GaugeSection_foregroundColor, diagram_GaugeSection_label, diagram_GaugeSection_value, diagram_GaugeSection_max, diagram_GaugeSection_min}

# Customizable class attributes and methods

# LabelStyle class attributes and methods

# Style class attributes and methods

# BorderedStyle class attributes and methods

# HideLabelCapabilityStyle class attributes and methods

# diagram_Dot class attributes and methods
diagram_Dot_strokeSizeComputationExpression: Property = Property(name="strokeSizeComputationExpression", type=StringType)
diagram_Dot_backgroundColor: Property = Property(name="backgroundColor", type=StringType)
diagram_Dot.attributes={diagram_Dot_strokeSizeComputationExpression, diagram_Dot_backgroundColor}

# NodeStyle class attributes and methods

# diagram_Square class attributes and methods
diagram_Square_width: Property = Property(name="width", type=StringType)
diagram_Square_height: Property = Property(name="height", type=StringType)
diagram_Square_color: Property = Property(name="color", type=StringType)
diagram_Square.attributes={diagram_Square_height, diagram_Square_color, diagram_Square_width}

# diagram_FlatContainerStyle class attributes and methods
diagram_FlatContainerStyle_backgroundStyle: Property = Property(name="backgroundStyle", type=StringType)
diagram_FlatContainerStyle_backgroundColor: Property = Property(name="backgroundColor", type=StringType)
diagram_FlatContainerStyle_foregroundColor: Property = Property(name="foregroundColor", type=StringType)
diagram_FlatContainerStyle.attributes={diagram_FlatContainerStyle_backgroundColor, diagram_FlatContainerStyle_foregroundColor, diagram_FlatContainerStyle_backgroundStyle}

# ContainerStyle class attributes and methods

# diagram_ShapeContainerStyle class attributes and methods
diagram_ShapeContainerStyle_shape: Property = Property(name="shape", type=StringType)
diagram_ShapeContainerStyle_backgroundColor: Property = Property(name="backgroundColor", type=StringType)
diagram_ShapeContainerStyle.attributes={diagram_ShapeContainerStyle_shape, diagram_ShapeContainerStyle_backgroundColor}

# diagram_Ellipse class attributes and methods
diagram_Ellipse_horizontalDiameter: Property = Property(name="horizontalDiameter", type=StringType)
diagram_Ellipse_verticalDiameter: Property = Property(name="verticalDiameter", type=StringType)
diagram_Ellipse_color: Property = Property(name="color", type=StringType)
diagram_Ellipse.attributes={diagram_Ellipse_horizontalDiameter, diagram_Ellipse_color, diagram_Ellipse_verticalDiameter}

# diagram_Lozenge class attributes and methods
diagram_Lozenge_width: Property = Property(name="width", type=StringType)
diagram_Lozenge_height: Property = Property(name="height", type=StringType)
diagram_Lozenge_color: Property = Property(name="color", type=StringType)
diagram_Lozenge.attributes={diagram_Lozenge_height, diagram_Lozenge_width, diagram_Lozenge_color}

# diagram_BundledImage class attributes and methods
diagram_BundledImage_shape: Property = Property(name="shape", type=StringType)
diagram_BundledImage_color: Property = Property(name="color", type=StringType)
diagram_BundledImage_providedShapeID: Property = Property(name="providedShapeID", type=StringType)
diagram_BundledImage.attributes={diagram_BundledImage_providedShapeID, diagram_BundledImage_color, diagram_BundledImage_shape}

# diagram_WorkspaceImage class attributes and methods
diagram_WorkspaceImage_workspacePath: Property = Property(name="workspacePath", type=StringType)
diagram_WorkspaceImage.attributes={diagram_WorkspaceImage_workspacePath}

# diagram_CustomStyle class attributes and methods
diagram_CustomStyle_id: Property = Property(name="id", type=StringType)
diagram_CustomStyle.attributes={diagram_CustomStyle_id}

# diagram_BeginLabelStyle class attributes and methods
diagram_BeginLabelStyle_m_getDescription: Method = Method(name="getDescription", parameters={}, type=StringType)
diagram_BeginLabelStyle_m_setDescription: Method = Method(name="setDescription", parameters={Parameter(name='description')})
diagram_BeginLabelStyle.methods={diagram_BeginLabelStyle_m_getDescription, diagram_BeginLabelStyle_m_setDescription}

# diagram_CenterLabelStyle class attributes and methods
diagram_CenterLabelStyle_m_getDescription: Method = Method(name="getDescription", parameters={}, type=StringType)
diagram_CenterLabelStyle_m_setDescription: Method = Method(name="setDescription", parameters={Parameter(name='description')})
diagram_CenterLabelStyle.methods={diagram_CenterLabelStyle_m_getDescription, diagram_CenterLabelStyle_m_setDescription}

# diagram_EndLabelStyle class attributes and methods
diagram_EndLabelStyle_m_getDescription: Method = Method(name="getDescription", parameters={}, type=StringType)
diagram_EndLabelStyle_m_setDescription: Method = Method(name="setDescription", parameters={Parameter(name='description')})
diagram_EndLabelStyle.methods={diagram_EndLabelStyle_m_setDescription, diagram_EndLabelStyle_m_getDescription}

# diagram_Note class attributes and methods
diagram_Note_color: Property = Property(name="color", type=StringType)
diagram_Note.attributes={diagram_Note_color}

# diagram_GaugeCompositeStyle class attributes and methods
diagram_GaugeCompositeStyle_alignment: Property = Property(name="alignment", type=StringType)
diagram_GaugeCompositeStyle.attributes={diagram_GaugeCompositeStyle_alignment}

# diagram_BorderedStyle class attributes and methods
diagram_BorderedStyle_borderColor: Property = Property(name="borderColor", type=StringType)
diagram_BorderedStyle_borderLineStyle: Property = Property(name="borderLineStyle", type=StringType)
diagram_BorderedStyle_borderSize: Property = Property(name="borderSize", type=StringType)
diagram_BorderedStyle_borderSizeComputationExpression: Property = Property(name="borderSizeComputationExpression", type=StringType)
diagram_BorderedStyle.attributes={diagram_BorderedStyle_borderLineStyle, diagram_BorderedStyle_borderSize, diagram_BorderedStyle_borderSizeComputationExpression, diagram_BorderedStyle_borderColor}

# diagram_HideLabelCapabilityStyle class attributes and methods
diagram_HideLabelCapabilityStyle_hideLabelByDefault: Property = Property(name="hideLabelByDefault", type=BooleanType)
diagram_HideLabelCapabilityStyle.attributes={diagram_HideLabelCapabilityStyle_hideLabelByDefault}

# diagram_VariableValue class attributes and methods

# diagram_TypedVariableValue class attributes and methods
diagram_TypedVariableValue_value: Property = Property(name="value", type=StringType)
diagram_TypedVariableValue.attributes={diagram_TypedVariableValue_value}

# VariableValue class attributes and methods

# TypedVariable class attributes and methods

# diagram_EObjectVariableValue class attributes and methods

# tool_SelectModelElementVariable class attributes and methods

# diagram_CollapseFilter class attributes and methods
diagram_CollapseFilter_width: Property = Property(name="width", type=IntegerType)
diagram_CollapseFilter_height: Property = Property(name="height", type=IntegerType)
diagram_CollapseFilter.attributes={diagram_CollapseFilter_height, diagram_CollapseFilter_width}

# diagram_EObject class attributes and methods

# diagram_description_DiagramDescription class attributes and methods
diagram_description_DiagramDescription_domainClass: Property = Property(name="domainClass", type=StringType)
diagram_description_DiagramDescription_preconditionExpression: Property = Property(name="preconditionExpression", type=StringType)
diagram_description_DiagramDescription_enablePopupBars: Property = Property(name="enablePopupBars", type=BooleanType)
diagram_description_DiagramDescription_rootExpression: Property = Property(name="rootExpression", type=StringType)
diagram_description_DiagramDescription_m_createDiagram: Method = Method(name="createDiagram", parameters={}, type=StringType)
diagram_description_DiagramDescription.attributes={diagram_description_DiagramDescription_preconditionExpression, diagram_description_DiagramDescription_rootExpression, diagram_description_DiagramDescription_enablePopupBars, diagram_description_DiagramDescription_domainClass}
diagram_description_DiagramDescription.methods={diagram_description_DiagramDescription_m_createDiagram}

# description_DragAndDropTargetDescription class attributes and methods

# diagram_IndirectlyCollapseFilter class attributes and methods

# description_RepresentationDescription class attributes and methods

# CollapseFilter class attributes and methods

# description_PasteTargetDescription class attributes and methods

# BasicLabelStyle class attributes and methods

# diagram_BracketEdgeStyle class attributes and methods

# EdgeStyle class attributes and methods

# diagram_ComputedStyleDescriptionRegistry class attributes and methods

# style_StyleDescription class attributes and methods

# diagram_DragAndDropTarget class attributes and methods
diagram_DragAndDropTarget_m_getDragAndDropDescription: Method = Method(name="getDragAndDropDescription", parameters={}, type=StringType)
diagram_DragAndDropTarget.methods={diagram_DragAndDropTarget_m_getDragAndDropDescription}

# validation_ValidationSet class attributes and methods

# concern_ConcernSet class attributes and methods

# tool_AbstractToolDescription class attributes and methods

# EdgeMapping class attributes and methods

# tool_RepresentationCreationDescription class attributes and methods

# Layout class attributes and methods

# tool_InitialOperation class attributes and methods

# diagram_description_DiagramImportDescription class attributes and methods

# AdditionalLayer class attributes and methods

# EdgeMappingImport class attributes and methods

# tool_ToolSection class attributes and methods

# tool_DeleteElementDescription class attributes and methods

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
diagram_description_DiagramElementMapping_m_checkPrecondition: Method = Method(name="checkPrecondition", parameters={Parameter(name='container'), Parameter(name='modelElement'), Parameter(name='containerView')}, type=BooleanType)
diagram_description_DiagramElementMapping_m_getAllMappings: Method = Method(name="getAllMappings", parameters={}, type=StringType)
diagram_description_DiagramElementMapping_m_isFrom: Method = Method(name="isFrom", parameters={Parameter(name='element')}, type=BooleanType)
diagram_description_DiagramElementMapping.attributes={diagram_description_DiagramElementMapping_createElements, diagram_description_DiagramElementMapping_semanticElements, diagram_description_DiagramElementMapping_synchronizationLock, diagram_description_DiagramElementMapping_semanticCandidatesExpression, diagram_description_DiagramElementMapping_preconditionExpression}
diagram_description_DiagramElementMapping.methods={diagram_description_DiagramElementMapping_m_getAllMappings, diagram_description_DiagramElementMapping_m_isFrom, diagram_description_DiagramElementMapping_m_checkPrecondition}

# description_RepresentationElementMapping class attributes and methods

# diagram_description_NodeMapping class attributes and methods
diagram_description_NodeMapping_m_createNode: Method = Method(name="createNode", parameters={Parameter(name='container'), Parameter(name='modelElement'), Parameter(name='viewPoint')}, type=StringType)
diagram_description_NodeMapping_m_updateNode: Method = Method(name="updateNode", parameters={Parameter(name='node')})
diagram_description_NodeMapping_m_updateListElement: Method = Method(name="updateListElement", parameters={Parameter(name='listElement')})
diagram_description_NodeMapping_m_getNodesCandidates: Method = Method(name="getNodesCandidates", parameters={Parameter(name='semanticOrigin'), Parameter(name='container')}, type=StringType)
diagram_description_NodeMapping_m_getNodesCandidates: Method = Method(name="getNodesCandidates", parameters={Parameter(name='containerView'), Parameter(name='semanticOrigin'), Parameter(name='container')}, type=StringType)
diagram_description_NodeMapping.methods={diagram_description_NodeMapping_m_getNodesCandidates, diagram_description_NodeMapping_m_updateNode, diagram_description_NodeMapping_m_getNodesCandidates, diagram_description_NodeMapping_m_updateListElement, diagram_description_NodeMapping_m_createNode}

# description_AbstractNodeMapping class attributes and methods

# tool_DirectEditLabel class attributes and methods

# tool_DoubleClickDescription class attributes and methods

# diagram_description_AbstractNodeMapping class attributes and methods
diagram_description_AbstractNodeMapping_domainClass: Property = Property(name="domainClass", type=StringType)
diagram_description_AbstractNodeMapping_m_findDNodeFromEObject: Method = Method(name="findDNodeFromEObject", parameters={Parameter(name='eObject')}, type=DDiagramElement)
diagram_description_AbstractNodeMapping_m_clearDNodesDone: Method = Method(name="clearDNodesDone", parameters={})
diagram_description_AbstractNodeMapping_m_addDoneNode: Method = Method(name="addDoneNode", parameters={Parameter(name='node')})
diagram_description_AbstractNodeMapping_m_getAllBorderedNodeMappings: Method = Method(name="getAllBorderedNodeMappings", parameters={}, type=StringType)
diagram_description_AbstractNodeMapping.attributes={diagram_description_AbstractNodeMapping_domainClass}
diagram_description_AbstractNodeMapping.methods={diagram_description_AbstractNodeMapping_m_getAllBorderedNodeMappings, diagram_description_AbstractNodeMapping_m_clearDNodesDone, diagram_description_AbstractNodeMapping_m_addDoneNode, diagram_description_AbstractNodeMapping_m_findDNodeFromEObject}

# description_DiagramElementMapping class attributes and methods

# diagram_description_ContainerMapping class attributes and methods
diagram_description_ContainerMapping_childrenPresentation: Property = Property(name="childrenPresentation", type=StringType)
diagram_description_ContainerMapping_m_getBestStyle: Method = Method(name="getBestStyle", parameters={Parameter(name='modelElement'), Parameter(name='containerVariable'), Parameter(name='viewVariable')}, type=ContainerStyle)
diagram_description_ContainerMapping.attributes={diagram_description_ContainerMapping_childrenPresentation}
diagram_description_ContainerMapping.methods={diagram_description_ContainerMapping_m_getBestStyle}

# style_NodeStyleDescription class attributes and methods

# ConditionalNodeStyleDescription class attributes and methods

# diagram_description_EdgeMapping class attributes and methods
diagram_description_EdgeMapping_targetExpression: Property = Property(name="targetExpression", type=StringType)
diagram_description_EdgeMapping_targetFinderExpression: Property = Property(name="targetFinderExpression", type=StringType)
diagram_description_EdgeMapping_sourceFinderExpression: Property = Property(name="sourceFinderExpression", type=StringType)
diagram_description_EdgeMapping_domainClass: Property = Property(name="domainClass", type=StringType)
diagram_description_EdgeMapping_useDomainElement: Property = Property(name="useDomainElement", type=BooleanType)
diagram_description_EdgeMapping_pathExpression: Property = Property(name="pathExpression", type=StringType)
diagram_description_EdgeMapping_m_createEdge: Method = Method(name="createEdge", parameters={Parameter(name='semanticTarget'), Parameter(name='target'), Parameter(name='source')}, type=StringType)
diagram_description_EdgeMapping_m_createEdge: Method = Method(name="createEdge", parameters={Parameter(name='semanticTarget'), Parameter(name='container'), Parameter(name='target'), Parameter(name='source')}, type=StringType)
diagram_description_EdgeMapping_m_getBestStyle: Method = Method(name="getBestStyle", parameters={Parameter(name='viewVariable'), Parameter(name='modelElement'), Parameter(name='containerVariable')}, type=EdgeStyle)
diagram_description_EdgeMapping_m_updateEdge: Method = Method(name="updateEdge", parameters={Parameter(name='viewEdge')})
diagram_description_EdgeMapping_m_getEdgeTargetCandidates: Method = Method(name="getEdgeTargetCandidates", parameters={Parameter(name='semanticOrigin'), Parameter(name='viewPoint')}, type=StringType)
diagram_description_EdgeMapping_m_getEdgeSourceCandidates: Method = Method(name="getEdgeSourceCandidates", parameters={Parameter(name='viewPoint'), Parameter(name='semanticOrigin')}, type=StringType)
diagram_description_EdgeMapping_m_getEdgeTargetCandidates: Method = Method(name="getEdgeTargetCandidates", parameters={Parameter(name='semanticOrigin'), Parameter(name='containerView'), Parameter(name='container')}, type=StringType)
diagram_description_EdgeMapping.attributes={diagram_description_EdgeMapping_useDomainElement, diagram_description_EdgeMapping_targetFinderExpression, diagram_description_EdgeMapping_domainClass, diagram_description_EdgeMapping_pathExpression, diagram_description_EdgeMapping_sourceFinderExpression, diagram_description_EdgeMapping_targetExpression}
diagram_description_EdgeMapping.methods={diagram_description_EdgeMapping_m_getEdgeTargetCandidates, diagram_description_EdgeMapping_m_getEdgeSourceCandidates, diagram_description_EdgeMapping_m_createEdge, diagram_description_EdgeMapping_m_getBestStyle, diagram_description_EdgeMapping_m_createEdge, diagram_description_EdgeMapping_m_getEdgeTargetCandidates, diagram_description_EdgeMapping_m_updateEdge}

# description_IEdgeMapping class attributes and methods

# style_ContainerStyleDescription class attributes and methods

# ConditionalContainerStyleDescription class attributes and methods

# diagram_description_NodeMappingImport class attributes and methods

# description_NodeMapping class attributes and methods

# description_AbstractMappingImport class attributes and methods

# diagram_description_ContainerMappingImport class attributes and methods

# description_ContainerMapping class attributes and methods

# ConditionalEdgeStyleDescription class attributes and methods

# diagram_description_OrderedTreeLayout class attributes and methods
diagram_description_OrderedTreeLayout_childrenExpression: Property = Property(name="childrenExpression", type=StringType)
diagram_description_OrderedTreeLayout.attributes={diagram_description_OrderedTreeLayout_childrenExpression}

# style_EdgeStyleDescription class attributes and methods

# tool_ReconnectEdgeDescription class attributes and methods

# AbstractNodeMapping class attributes and methods

# diagram_description_IEdgeMapping class attributes and methods
diagram_description_IEdgeMapping_m_getBestStyle: Method = Method(name="getBestStyle", parameters={Parameter(name='containerVariable'), Parameter(name='modelElement'), Parameter(name='viewVariable')}, type=EdgeStyle)
diagram_description_IEdgeMapping.methods={diagram_description_IEdgeMapping_m_getBestStyle}

# diagram_description_EdgeMappingImport class attributes and methods
diagram_description_EdgeMappingImport_inheritsAncestorFilters: Property = Property(name="inheritsAncestorFilters", type=BooleanType)
diagram_description_EdgeMappingImport.attributes={diagram_description_EdgeMappingImport_inheritsAncestorFilters}

# description_IdentifiedElement class attributes and methods

# diagram_description_ConditionalNodeStyleDescription class attributes and methods

# ConditionalStyleDescription class attributes and methods

# diagram_description_ConditionalEdgeStyleDescription class attributes and methods

# diagram_description_ConditionalContainerStyleDescription class attributes and methods

# diagram_description_Layout class attributes and methods

# DocumentedElement class attributes and methods

# DecorationDescriptionsSet class attributes and methods

# diagram_description_CompositeLayout class attributes and methods
diagram_description_CompositeLayout_padding: Property = Property(name="padding", type=IntegerType)
diagram_description_CompositeLayout_direction: Property = Property(name="direction", type=StringType)
diagram_description_CompositeLayout.attributes={diagram_description_CompositeLayout_padding, diagram_description_CompositeLayout_direction}

# diagram_description_MappingBasedDecoration class attributes and methods

# DecorationDescription class attributes and methods

# diagram_description_Layer class attributes and methods
diagram_description_Layer_icon: Property = Property(name="icon", type=StringType)
diagram_description_Layer.attributes={diagram_description_Layer_icon}

# description_EndUserDocumentedElement class attributes and methods

# diagram_style_NodeStyleDescription class attributes and methods
diagram_style_NodeStyleDescription_sizeComputationExpression: Property = Property(name="sizeComputationExpression", type=StringType)
diagram_style_NodeStyleDescription_labelPosition: Property = Property(name="labelPosition", type=StringType)
diagram_style_NodeStyleDescription_resizeKind: Property = Property(name="resizeKind", type=StringType)
diagram_style_NodeStyleDescription_forbiddenSides: Property = Property(name="forbiddenSides", type=StringType)
diagram_style_NodeStyleDescription.attributes={diagram_style_NodeStyleDescription_forbiddenSides, diagram_style_NodeStyleDescription_sizeComputationExpression, diagram_style_NodeStyleDescription_resizeKind, diagram_style_NodeStyleDescription_labelPosition}

# style_BorderedStyleDescription class attributes and methods

# style_LabelStyleDescription class attributes and methods

# style_TooltipStyleDescription class attributes and methods

# style_HideLabelCapabilityStyleDescription class attributes and methods

# Customization class attributes and methods

# diagram_style_CustomStyleDescription class attributes and methods
diagram_style_CustomStyleDescription_id: Property = Property(name="id", type=StringType)
diagram_style_CustomStyleDescription.attributes={diagram_style_CustomStyleDescription_id}

# NodeStyleDescription class attributes and methods

# diagram_description_AdditionalLayer class attributes and methods
diagram_description_AdditionalLayer_activeByDefault: Property = Property(name="activeByDefault", type=BooleanType)
diagram_description_AdditionalLayer_optional: Property = Property(name="optional", type=BooleanType)
diagram_description_AdditionalLayer.attributes={diagram_description_AdditionalLayer_activeByDefault, diagram_description_AdditionalLayer_optional}

# diagram_description_DragAndDropTargetDescription class attributes and methods

# tool_ContainerDropDescription class attributes and methods

# diagram_style_BorderedStyleDescription class attributes and methods
diagram_style_BorderedStyleDescription_borderSizeComputationExpression: Property = Property(name="borderSizeComputationExpression", type=StringType)
diagram_style_BorderedStyleDescription_borderLineStyle: Property = Property(name="borderLineStyle", type=StringType)
diagram_style_BorderedStyleDescription.attributes={diagram_style_BorderedStyleDescription_borderLineStyle, diagram_style_BorderedStyleDescription_borderSizeComputationExpression}

# StyleDescription class attributes and methods

# ColorDescription class attributes and methods

# diagram_style_BundledImageDescription class attributes and methods
diagram_style_BundledImageDescription_shape: Property = Property(name="shape", type=StringType)
diagram_style_BundledImageDescription_providedShapeID: Property = Property(name="providedShapeID", type=StringType)
diagram_style_BundledImageDescription.attributes={diagram_style_BundledImageDescription_providedShapeID, diagram_style_BundledImageDescription_shape}

# diagram_style_SquareDescription class attributes and methods
diagram_style_SquareDescription_width: Property = Property(name="width", type=StringType)
diagram_style_SquareDescription_height: Property = Property(name="height", type=StringType)
diagram_style_SquareDescription.attributes={diagram_style_SquareDescription_height, diagram_style_SquareDescription_width}

# diagram_style_LozengeNodeDescription class attributes and methods
diagram_style_LozengeNodeDescription_widthComputationExpression: Property = Property(name="widthComputationExpression", type=StringType)
diagram_style_LozengeNodeDescription_heightComputationExpression: Property = Property(name="heightComputationExpression", type=StringType)
diagram_style_LozengeNodeDescription.attributes={diagram_style_LozengeNodeDescription_widthComputationExpression, diagram_style_LozengeNodeDescription_heightComputationExpression}

# diagram_style_EllipseNodeDescription class attributes and methods
diagram_style_EllipseNodeDescription_horizontalDiameterComputationExpression: Property = Property(name="horizontalDiameterComputationExpression", type=StringType)
diagram_style_EllipseNodeDescription_verticalDiameterComputationExpression: Property = Property(name="verticalDiameterComputationExpression", type=StringType)
diagram_style_EllipseNodeDescription.attributes={diagram_style_EllipseNodeDescription_verticalDiameterComputationExpression, diagram_style_EllipseNodeDescription_horizontalDiameterComputationExpression}

# diagram_style_NoteDescription class attributes and methods

# diagram_style_DotDescription class attributes and methods
diagram_style_DotDescription_strokeSizeComputationExpression: Property = Property(name="strokeSizeComputationExpression", type=StringType)
diagram_style_DotDescription.attributes={diagram_style_DotDescription_strokeSizeComputationExpression}

# diagram_style_GaugeCompositeStyleDescription class attributes and methods
diagram_style_GaugeCompositeStyleDescription_alignment: Property = Property(name="alignment", type=StringType)
diagram_style_GaugeCompositeStyleDescription.attributes={diagram_style_GaugeCompositeStyleDescription_alignment}

# style_GaugeSectionDescription class attributes and methods

# diagram_style_GaugeSectionDescription class attributes and methods
diagram_style_GaugeSectionDescription_minValueExpression: Property = Property(name="minValueExpression", type=StringType)
diagram_style_GaugeSectionDescription_maxValueExpression: Property = Property(name="maxValueExpression", type=StringType)
diagram_style_GaugeSectionDescription_valueExpression: Property = Property(name="valueExpression", type=StringType)
diagram_style_GaugeSectionDescription_label: Property = Property(name="label", type=StringType)
diagram_style_GaugeSectionDescription.attributes={diagram_style_GaugeSectionDescription_valueExpression, diagram_style_GaugeSectionDescription_label, diagram_style_GaugeSectionDescription_maxValueExpression, diagram_style_GaugeSectionDescription_minValueExpression}

# style_LabelBorderStyleDescription class attributes and methods

# diagram_style_ShapeContainerStyleDescription class attributes and methods
diagram_style_ShapeContainerStyleDescription_shape: Property = Property(name="shape", type=StringType)
diagram_style_ShapeContainerStyleDescription.attributes={diagram_style_ShapeContainerStyleDescription_shape}

# diagram_style_WorkspaceImageDescription class attributes and methods
diagram_style_WorkspaceImageDescription_workspacePath: Property = Property(name="workspacePath", type=StringType)
diagram_style_WorkspaceImageDescription.attributes={diagram_style_WorkspaceImageDescription_workspacePath}

# diagram_style_SizeComputationContainerStyleDescription class attributes and methods
diagram_style_SizeComputationContainerStyleDescription_widthComputationExpression: Property = Property(name="widthComputationExpression", type=StringType)
diagram_style_SizeComputationContainerStyleDescription_heightComputationExpression: Property = Property(name="heightComputationExpression", type=StringType)
diagram_style_SizeComputationContainerStyleDescription.attributes={diagram_style_SizeComputationContainerStyleDescription_heightComputationExpression, diagram_style_SizeComputationContainerStyleDescription_widthComputationExpression}

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

# style_BeginLabelStyleDescription class attributes and methods

# style_CenterLabelStyleDescription class attributes and methods

# style_EndLabelStyleDescription class attributes and methods

# diagram_style_BeginLabelStyleDescription class attributes and methods

# BasicLabelStyleDescription class attributes and methods

# diagram_style_EdgeStyleDescription class attributes and methods
diagram_style_EdgeStyleDescription_endsCentering: Property = Property(name="endsCentering", type=StringType)
diagram_style_EdgeStyleDescription_lineStyle: Property = Property(name="lineStyle", type=StringType)
diagram_style_EdgeStyleDescription_sourceArrow: Property = Property(name="sourceArrow", type=StringType)
diagram_style_EdgeStyleDescription_targetArrow: Property = Property(name="targetArrow", type=StringType)
diagram_style_EdgeStyleDescription_sizeComputationExpression: Property = Property(name="sizeComputationExpression", type=StringType)
diagram_style_EdgeStyleDescription_routingStyle: Property = Property(name="routingStyle", type=StringType)
diagram_style_EdgeStyleDescription_foldingStyle: Property = Property(name="foldingStyle", type=StringType)
diagram_style_EdgeStyleDescription.attributes={diagram_style_EdgeStyleDescription_sizeComputationExpression, diagram_style_EdgeStyleDescription_endsCentering, diagram_style_EdgeStyleDescription_sourceArrow, diagram_style_EdgeStyleDescription_lineStyle, diagram_style_EdgeStyleDescription_targetArrow, diagram_style_EdgeStyleDescription_foldingStyle, diagram_style_EdgeStyleDescription_routingStyle}

# tool_PopupMenu class attributes and methods

# tool_ToolGroupExtension class attributes and methods

# diagram_tool_ToolGroup class attributes and methods

# ToolEntry class attributes and methods

# diagram_tool_ToolGroupExtension class attributes and methods

# tool_ToolGroup class attributes and methods

# diagram_style_CenterLabelStyleDescription class attributes and methods

# diagram_style_EndLabelStyleDescription class attributes and methods

# diagram_style_BracketEdgeStyleDescription class attributes and methods

# EdgeStyleDescription class attributes and methods

# diagram_style_HideLabelCapabilityStyleDescription class attributes and methods
diagram_style_HideLabelCapabilityStyleDescription_hideLabelByDefault: Property = Property(name="hideLabelByDefault", type=BooleanType)
diagram_style_HideLabelCapabilityStyleDescription.attributes={diagram_style_HideLabelCapabilityStyleDescription_hideLabelByDefault}

# diagram_tool_ToolSection class attributes and methods
diagram_tool_ToolSection_icon: Property = Property(name="icon", type=StringType)
diagram_tool_ToolSection.attributes={diagram_tool_ToolSection_icon}

# tool_ToolEntry class attributes and methods

# tool_InitialNodeCreationOperation class attributes and methods

# diagram_tool_NodeCreationDescription class attributes and methods
diagram_tool_NodeCreationDescription_iconPath: Property = Property(name="iconPath", type=StringType)
diagram_tool_NodeCreationDescription.attributes={diagram_tool_NodeCreationDescription_iconPath}

# MappingBasedToolDescription class attributes and methods

# tool_NodeCreationVariable class attributes and methods

# tool_ContainerViewVariable class attributes and methods

# tool_TargetEdgeCreationVariable class attributes and methods

# tool_SourceEdgeViewCreationVariable class attributes and methods

# tool_TargetEdgeViewCreationVariable class attributes and methods

# tool_InitEdgeCreationOperation class attributes and methods

# diagram_tool_EdgeCreationDescription class attributes and methods
diagram_tool_EdgeCreationDescription_iconPath: Property = Property(name="iconPath", type=StringType)
diagram_tool_EdgeCreationDescription_connectionStartPrecondition: Property = Property(name="connectionStartPrecondition", type=StringType)
diagram_tool_EdgeCreationDescription_m_getBestMapping: Method = Method(name="getBestMapping", parameters={Parameter(name='createdElements'), Parameter(name='target'), Parameter(name='source')}, type=StringType)
diagram_tool_EdgeCreationDescription.attributes={diagram_tool_EdgeCreationDescription_iconPath, diagram_tool_EdgeCreationDescription_connectionStartPrecondition}
diagram_tool_EdgeCreationDescription.methods={diagram_tool_EdgeCreationDescription_m_getBestMapping}

# tool_SourceEdgeCreationVariable class attributes and methods

# diagram_tool_DeleteElementDescription class attributes and methods
diagram_tool_DeleteElementDescription_m_getMappings: Method = Method(name="getMappings", parameters={}, type=StringType)
diagram_tool_DeleteElementDescription.methods={diagram_tool_DeleteElementDescription_m_getMappings}

# tool_ElementDeleteVariable class attributes and methods

# diagram_tool_ContainerCreationDescription class attributes and methods
diagram_tool_ContainerCreationDescription_iconPath: Property = Property(name="iconPath", type=StringType)
diagram_tool_ContainerCreationDescription.attributes={diagram_tool_ContainerCreationDescription_iconPath}

# tool_DeleteHookParameter class attributes and methods

# diagram_tool_DeleteHookParameter class attributes and methods
diagram_tool_DeleteHookParameter_name: Property = Property(name="name", type=StringType)
diagram_tool_DeleteHookParameter_value: Property = Property(name="value", type=StringType)
diagram_tool_DeleteHookParameter.attributes={diagram_tool_DeleteHookParameter_value, diagram_tool_DeleteHookParameter_name}

# diagram_tool_ReconnectEdgeDescription class attributes and methods
diagram_tool_ReconnectEdgeDescription_reconnectionKind: Property = Property(name="reconnectionKind", type=StringType)
diagram_tool_ReconnectEdgeDescription_m_getMappings: Method = Method(name="getMappings", parameters={}, type=StringType)
diagram_tool_ReconnectEdgeDescription.attributes={diagram_tool_ReconnectEdgeDescription_reconnectionKind}
diagram_tool_ReconnectEdgeDescription.methods={diagram_tool_ReconnectEdgeDescription_m_getMappings}

# tool_DeleteHook class attributes and methods

# diagram_tool_DoubleClickDescription class attributes and methods

# tool_ElementDoubleClickVariable class attributes and methods

# diagram_tool_DeleteHook class attributes and methods
diagram_tool_DeleteHook_id: Property = Property(name="id", type=StringType)
diagram_tool_DeleteHook.attributes={diagram_tool_DeleteHook_id}

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

# tool_ElementSelectVariable class attributes and methods

# diagram_tool_RequestDescription class attributes and methods
diagram_tool_RequestDescription_type: Property = Property(name="type", type=StringType)
diagram_tool_RequestDescription.attributes={diagram_tool_RequestDescription_type}

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
diagram_tool_CreateView.attributes={diagram_tool_CreateView_containerViewExpression, diagram_tool_CreateView_variableName}

# ContainerModelOperation class attributes and methods

# tool_ElementDropVariable class attributes and methods

# tool_InitialContainerDropOperation class attributes and methods

# diagram_filter_FilterDescription class attributes and methods
diagram_filter_FilterDescription_m_isVisible: Method = Method(name="isVisible", parameters={Parameter(name='element')}, type=BooleanType)
diagram_filter_FilterDescription.methods={diagram_filter_FilterDescription_m_isVisible}

# diagram_tool_DiagramNavigationDescription class attributes and methods

# RepresentationNavigationDescription class attributes and methods

# diagram_tool_ContainerDropDescription class attributes and methods
diagram_tool_ContainerDropDescription_dragSource: Property = Property(name="dragSource", type=StringType)
diagram_tool_ContainerDropDescription_moveEdges: Property = Property(name="moveEdges", type=BooleanType)
diagram_tool_ContainerDropDescription_m_getBestMapping: Method = Method(name="getBestMapping", parameters={Parameter(name='targetContainer'), Parameter(name='droppedElement')}, type=StringType)
diagram_tool_ContainerDropDescription_m_getContainers: Method = Method(name="getContainers", parameters={}, type=StringType)
diagram_tool_ContainerDropDescription.attributes={diagram_tool_ContainerDropDescription_moveEdges, diagram_tool_ContainerDropDescription_dragSource}
diagram_tool_ContainerDropDescription.methods={diagram_tool_ContainerDropDescription_m_getBestMapping, diagram_tool_ContainerDropDescription_m_getContainers}

# tool_DropContainerVariable class attributes and methods

# diagram_filter_CompositeFilterDescription class attributes and methods

# FilterDescription class attributes and methods

# filter_Filter class attributes and methods

# diagram_filter_VariableFilter class attributes and methods
diagram_filter_VariableFilter_semanticConditionExpression: Property = Property(name="semanticConditionExpression", type=StringType)
diagram_filter_VariableFilter_m_resetVariables: Method = Method(name="resetVariables", parameters={})
diagram_filter_VariableFilter.attributes={diagram_filter_VariableFilter_semanticConditionExpression}
diagram_filter_VariableFilter.methods={diagram_filter_VariableFilter_m_resetVariables}

# InteractiveVariableDescription class attributes and methods

# diagram_concern_ConcernSet class attributes and methods

# diagram_filter_Filter class attributes and methods
diagram_filter_Filter_filterKind: Property = Property(name="filterKind", type=StringType)
diagram_filter_Filter_m_isVisible: Method = Method(name="isVisible", parameters={Parameter(name='element')}, type=BooleanType)
diagram_filter_Filter.attributes={diagram_filter_Filter_filterKind}
diagram_filter_Filter.methods={diagram_filter_Filter_m_isVisible}

# diagram_concern_ConcernDescription class attributes and methods

# diagram_filter_MappingFilter class attributes and methods
diagram_filter_MappingFilter_semanticConditionExpression: Property = Property(name="semanticConditionExpression", type=StringType)
diagram_filter_MappingFilter_viewConditionExpression: Property = Property(name="viewConditionExpression", type=StringType)
diagram_filter_MappingFilter.attributes={diagram_filter_MappingFilter_semanticConditionExpression, diagram_filter_MappingFilter_viewConditionExpression}

# Filter class attributes and methods

# Relationships
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
hiddenElements29: BinaryAssociation = BinaryAssociation(
    name="hiddenElements29",
    ends={
        Property(name="diagram_DDiagramElement31", type=diagram_DDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagram30", type=diagram_DDiagramElement, multiplicity=Multiplicity(0, 9999))
    }
)
nodeListElements10: BinaryAssociation = BinaryAssociation(
    name="nodeListElements10",
    ends={
        Property(name="diagram_DNodeListElement", type=diagram_DDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagram11", type=diagram_DNodeListElement, multiplicity=Multiplicity(0, 9999))
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
allFilters18: BinaryAssociation = BinaryAssociation(
    name="allFilters18",
    ends={
        Property(name="filter_FilterDescription20", type=diagram_DDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagram19", type=filter_FilterDescription, multiplicity=Multiplicity(0, 9999))
    }
)
activatedRules21: BinaryAssociation = BinaryAssociation(
    name="activatedRules21",
    ends={
        Property(name="validation_ValidationRule", type=diagram_DDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagram22", type=validation_ValidationRule, multiplicity=Multiplicity(0, 9999))
    }
)
activateBehaviors23: BinaryAssociation = BinaryAssociation(
    name="activateBehaviors23",
    ends={
        Property(name="tool_BehaviorTool", type=diagram_DDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagram24", type=tool_BehaviorTool, multiplicity=Multiplicity(0, 9999))
    }
)
filterVariableHistory25: BinaryAssociation = BinaryAssociation(
    name="filterVariableHistory25",
    ends={
        Property(name="diagram_FilterVariableHistory", type=diagram_DDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagram26", type=diagram_FilterVariableHistory, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
activatedLayers27: BinaryAssociation = BinaryAssociation(
    name="activatedLayers27",
    ends={
        Property(name="Layer", type=diagram_DDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagram28", type=Layer, multiplicity=Multiplicity(0, 9999))
    }
)
compositeFilterDescriptions41: BinaryAssociation = BinaryAssociation(
    name="compositeFilterDescriptions41",
    ends={
        Property(name="filter_CompositeFilterDescription", type=diagram_AppliedCompositeFilters, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_AppliedCompositeFilters", type=filter_CompositeFilterDescription, multiplicity=Multiplicity(0, 9999))
    }
)
parentLayers32: BinaryAssociation = BinaryAssociation(
    name="parentLayers32",
    ends={
        Property(name="Layer34", type=diagram_DDiagramElement, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagramElement33", type=Layer, multiplicity=Multiplicity(0, 9999))
    }
)
decorations35: BinaryAssociation = BinaryAssociation(
    name="decorations35",
    ends={
        Property(name="diagram_Decoration", type=diagram_DDiagramElement, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagramElement36", type=diagram_Decoration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
diagramElementMapping37: BinaryAssociation = BinaryAssociation(
    name="diagramElementMapping37",
    ends={
        Property(name="DiagramElementMapping", type=diagram_DDiagramElement, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagramElement38", type=DiagramElementMapping, multiplicity=Multiplicity(0, 1))
    }
)
graphicalFilters39: BinaryAssociation = BinaryAssociation(
    name="graphicalFilters39",
    ends={
        Property(name="diagram_GraphicalFilter", type=diagram_DDiagramElement, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagramElement40", type=diagram_GraphicalFilter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBorderedNodes42: BinaryAssociation = BinaryAssociation(
    name="ownedBorderedNodes42",
    ends={
        Property(name="diagram_DNode43", type=diagram_AbstractDNode, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_AbstractDNode", type=diagram_DNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedStyle44: BinaryAssociation = BinaryAssociation(
    name="ownedStyle44",
    ends={
        Property(name="diagram_NodeStyle", type=diagram_DNode, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DNode45", type=diagram_NodeStyle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
originalStyle46: BinaryAssociation = BinaryAssociation(
    name="originalStyle46",
    ends={
        Property(name="diagram_Style", type=diagram_DNode, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DNode47", type=diagram_Style, multiplicity=Multiplicity(0, 1))
    }
)
actualMapping48: BinaryAssociation = BinaryAssociation(
    name="actualMapping48",
    ends={
        Property(name="NodeMapping", type=diagram_DNode, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DNode49", type=NodeMapping, multiplicity=Multiplicity(1, 1))
    }
)
candidatesMapping50: BinaryAssociation = BinaryAssociation(
    name="candidatesMapping50",
    ends={
        Property(name="NodeMapping52", type=diagram_DNode, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DNode51", type=NodeMapping, multiplicity=Multiplicity(0, 9999))
    }
)
nodes53: BinaryAssociation = BinaryAssociation(
    name="nodes53",
    ends={
        Property(name="diagram_DNode55", type=diagram_DDiagramElementContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagramElementContainer54", type=diagram_DNode, multiplicity=Multiplicity(0, 9999))
    }
)
containers57: BinaryAssociation = BinaryAssociation(
    name="containers57",
    ends={
        Property(name="diagram_DDiagramElementContainer58", type=diagram_DDiagramElementContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagramElementContainer56", type=diagram_DDiagramElementContainer, multiplicity=Multiplicity(0, 9999))
    }
)
elements59: BinaryAssociation = BinaryAssociation(
    name="elements59",
    ends={
        Property(name="diagram_DDiagramElement61", type=diagram_DDiagramElementContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagramElementContainer60", type=diagram_DDiagramElement, multiplicity=Multiplicity(0, 9999))
    }
)
ownedStyle62: BinaryAssociation = BinaryAssociation(
    name="ownedStyle62",
    ends={
        Property(name="diagram_ContainerStyle", type=diagram_DDiagramElementContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagramElementContainer63", type=diagram_ContainerStyle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
originalStyle64: BinaryAssociation = BinaryAssociation(
    name="originalStyle64",
    ends={
        Property(name="diagram_Style66", type=diagram_DDiagramElementContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagramElementContainer65", type=diagram_Style, multiplicity=Multiplicity(0, 1))
    }
)
actualMapping67: BinaryAssociation = BinaryAssociation(
    name="actualMapping67",
    ends={
        Property(name="ContainerMapping", type=diagram_DDiagramElementContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagramElementContainer68", type=ContainerMapping, multiplicity=Multiplicity(1, 1))
    }
)
candidatesMapping69: BinaryAssociation = BinaryAssociation(
    name="candidatesMapping69",
    ends={
        Property(name="ContainerMapping71", type=diagram_DDiagramElementContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagramElementContainer70", type=ContainerMapping, multiplicity=Multiplicity(0, 9999))
    }
)
ownedDiagramElements72: BinaryAssociation = BinaryAssociation(
    name="ownedDiagramElements72",
    ends={
        Property(name="diagram_DDiagramElement73", type=diagram_DNodeContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DNodeContainer", type=diagram_DDiagramElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
targetNode91: BinaryAssociation = BinaryAssociation(
    name="targetNode91",
    ends={
        Property(name="EdgeTarget92", type=diagram_DEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingEdges", type=diagram_EdgeTarget, multiplicity=Multiplicity(1, 1))
    }
)
actualMapping93: BinaryAssociation = BinaryAssociation(
    name="actualMapping93",
    ends={
        Property(name="IEdgeMapping", type=diagram_DEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DEdge94", type=IEdgeMapping, multiplicity=Multiplicity(1, 1))
    }
)
ownedElements74: BinaryAssociation = BinaryAssociation(
    name="ownedElements74",
    ends={
        Property(name="diagram_DNodeListElement75", type=diagram_DNodeList, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DNodeList", type=diagram_DNodeListElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedStyle76: BinaryAssociation = BinaryAssociation(
    name="ownedStyle76",
    ends={
        Property(name="diagram_NodeStyle78", type=diagram_DNodeListElement, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DNodeListElement77", type=diagram_NodeStyle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
originalStyle79: BinaryAssociation = BinaryAssociation(
    name="originalStyle79",
    ends={
        Property(name="diagram_Style81", type=diagram_DNodeListElement, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DNodeListElement80", type=diagram_Style, multiplicity=Multiplicity(0, 1))
    }
)
actualMapping82: BinaryAssociation = BinaryAssociation(
    name="actualMapping82",
    ends={
        Property(name="NodeMapping84", type=diagram_DNodeListElement, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DNodeListElement83", type=NodeMapping, multiplicity=Multiplicity(1, 1))
    }
)
candidatesMapping85: BinaryAssociation = BinaryAssociation(
    name="candidatesMapping85",
    ends={
        Property(name="NodeMapping87", type=diagram_DNodeListElement, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DNodeListElement86", type=NodeMapping, multiplicity=Multiplicity(0, 9999))
    }
)
ownedStyle88: BinaryAssociation = BinaryAssociation(
    name="ownedStyle88",
    ends={
        Property(name="diagram_EdgeStyle", type=diagram_DEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DEdge89", type=diagram_EdgeStyle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sourceNode90: BinaryAssociation = BinaryAssociation(
    name="sourceNode90",
    ends={
        Property(name="EdgeTarget", type=diagram_DEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingEdges", type=diagram_EdgeTarget, multiplicity=Multiplicity(1, 1))
    }
)
originalStyle95: BinaryAssociation = BinaryAssociation(
    name="originalStyle95",
    ends={
        Property(name="diagram_Style97", type=diagram_DEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DEdge96", type=diagram_Style, multiplicity=Multiplicity(0, 1))
    }
)
path98: BinaryAssociation = BinaryAssociation(
    name="path98",
    ends={
        Property(name="diagram_EdgeTarget", type=diagram_DEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DEdge99", type=diagram_EdgeTarget, multiplicity=Multiplicity(0, 9999))
    }
)
outgoingEdges100: BinaryAssociation = BinaryAssociation(
    name="outgoingEdges100",
    ends={
        Property(name="DEdge", type=diagram_EdgeTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceNode", type=diagram_DEdge, multiplicity=Multiplicity(0, 9999))
    }
)
incomingEdges101: BinaryAssociation = BinaryAssociation(
    name="incomingEdges101",
    ends={
        Property(name="DEdge102", type=diagram_EdgeTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="targetNode", type=diagram_DEdge, multiplicity=Multiplicity(0, 9999))
    }
)
beginLabelStyle103: BinaryAssociation = BinaryAssociation(
    name="beginLabelStyle103",
    ends={
        Property(name="diagram_BeginLabelStyle", type=diagram_EdgeStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_EdgeStyle104", type=diagram_BeginLabelStyle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
centerLabelStyle105: BinaryAssociation = BinaryAssociation(
    name="centerLabelStyle105",
    ends={
        Property(name="diagram_CenterLabelStyle", type=diagram_EdgeStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_EdgeStyle106", type=diagram_CenterLabelStyle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
endLabelStyle107: BinaryAssociation = BinaryAssociation(
    name="endLabelStyle107",
    ends={
        Property(name="diagram_EndLabelStyle", type=diagram_EdgeStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_EdgeStyle108", type=diagram_EndLabelStyle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sections109: BinaryAssociation = BinaryAssociation(
    name="sections109",
    ends={
        Property(name="diagram_GaugeSection", type=diagram_GaugeCompositeStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_GaugeCompositeStyle", type=diagram_GaugeSection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedValues110: BinaryAssociation = BinaryAssociation(
    name="ownedValues110",
    ends={
        Property(name="diagram_VariableValue", type=diagram_FilterVariableHistory, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_FilterVariableHistory111", type=diagram_VariableValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variableDefinition113: BinaryAssociation = BinaryAssociation(
    name="variableDefinition113",
    ends={
        Property(name="TypedVariable", type=diagram_TypedVariableValue, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_TypedVariableValue", type=TypedVariable, multiplicity=Multiplicity(1, 1))
    }
)
variableDefinition114: BinaryAssociation = BinaryAssociation(
    name="variableDefinition114",
    ends={
        Property(name="tool_SelectModelElementVariable", type=diagram_EObjectVariableValue, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_EObjectVariableValue", type=tool_SelectModelElementVariable, multiplicity=Multiplicity(1, 1))
    }
)
modelElement115: BinaryAssociation = BinaryAssociation(
    name="modelElement115",
    ends={
        Property(name="diagram_EObject", type=diagram_EObjectVariableValue, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_EObjectVariableValue116", type=diagram_EObject, multiplicity=Multiplicity(1, 1))
    }
)
filters117: BinaryAssociation = BinaryAssociation(
    name="filters117",
    ends={
        Property(name="filter_FilterDescription118", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription", type=filter_FilterDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
computedStyleDescriptions112: BinaryAssociation = BinaryAssociation(
    name="computedStyleDescriptions112",
    ends={
        Property(name="style_StyleDescription", type=diagram_ComputedStyleDescriptionRegistry, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_ComputedStyleDescriptionRegistry", type=style_StyleDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
validationSet127: BinaryAssociation = BinaryAssociation(
    name="validationSet127",
    ends={
        Property(name="validation_ValidationSet", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription128", type=validation_ValidationSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
concerns129: BinaryAssociation = BinaryAssociation(
    name="concerns129",
    ends={
        Property(name="concern_ConcernSet", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription130", type=concern_ConcernSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
allTools131: BinaryAssociation = BinaryAssociation(
    name="allTools131",
    ends={
        Property(name="tool_AbstractToolDescription", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription132", type=tool_AbstractToolDescription, multiplicity=Multiplicity(0, 9999))
    }
)
allEdgeMappings119: BinaryAssociation = BinaryAssociation(
    name="allEdgeMappings119",
    ends={
        Property(name="EdgeMapping", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription120", type=EdgeMapping, multiplicity=Multiplicity(0, 9999))
    }
)
allNodeMappings121: BinaryAssociation = BinaryAssociation(
    name="allNodeMappings121",
    ends={
        Property(name="NodeMapping123", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription122", type=NodeMapping, multiplicity=Multiplicity(0, 9999))
    }
)
allContainerMappings124: BinaryAssociation = BinaryAssociation(
    name="allContainerMappings124",
    ends={
        Property(name="ContainerMapping126", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription125", type=ContainerMapping, multiplicity=Multiplicity(0, 9999))
    }
)
init136: BinaryAssociation = BinaryAssociation(
    name="init136",
    ends={
        Property(name="tool_RepresentationCreationDescription", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription137", type=tool_RepresentationCreationDescription, multiplicity=Multiplicity(0, 1))
    }
)
reusedTools169: BinaryAssociation = BinaryAssociation(
    name="reusedTools169",
    ends={
        Property(name="tool_AbstractToolDescription171", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription170", type=tool_AbstractToolDescription, multiplicity=Multiplicity(0, 9999))
    }
)
layout138: BinaryAssociation = BinaryAssociation(
    name="layout138",
    ends={
        Property(name="Layout", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription139", type=Layout, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
diagramInitialisation140: BinaryAssociation = BinaryAssociation(
    name="diagramInitialisation140",
    ends={
        Property(name="tool_InitialOperation", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription141", type=tool_InitialOperation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultLayer142: BinaryAssociation = BinaryAssociation(
    name="defaultLayer142",
    ends={
        Property(name="Layer144", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription143", type=Layer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultConcern133: BinaryAssociation = BinaryAssociation(
    name="defaultConcern133",
    ends={
        Property(name="concern_ConcernDescription135", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription134", type=concern_ConcernDescription, multiplicity=Multiplicity(0, 1))
    }
)
additionalLayers145: BinaryAssociation = BinaryAssociation(
    name="additionalLayers145",
    ends={
        Property(name="AdditionalLayer", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription146", type=AdditionalLayer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allLayers147: BinaryAssociation = BinaryAssociation(
    name="allLayers147",
    ends={
        Property(name="Layer149", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription148", type=Layer, multiplicity=Multiplicity(0, 9999))
    }
)
allActivatedTools150: BinaryAssociation = BinaryAssociation(
    name="allActivatedTools150",
    ends={
        Property(name="tool_AbstractToolDescription152", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription151", type=tool_AbstractToolDescription, multiplicity=Multiplicity(0, 9999))
    }
)
nodeMappings153: BinaryAssociation = BinaryAssociation(
    name="nodeMappings153",
    ends={
        Property(name="NodeMapping155", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription154", type=NodeMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edgeMappings156: BinaryAssociation = BinaryAssociation(
    name="edgeMappings156",
    ends={
        Property(name="EdgeMapping158", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription157", type=EdgeMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edgeMappingImports159: BinaryAssociation = BinaryAssociation(
    name="edgeMappingImports159",
    ends={
        Property(name="EdgeMappingImport", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription160", type=EdgeMappingImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containerMappings161: BinaryAssociation = BinaryAssociation(
    name="containerMappings161",
    ends={
        Property(name="ContainerMapping163", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription162", type=ContainerMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reusedMappings164: BinaryAssociation = BinaryAssociation(
    name="reusedMappings164",
    ends={
        Property(name="DiagramElementMapping166", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription165", type=DiagramElementMapping, multiplicity=Multiplicity(0, 9999))
    }
)
toolSection167: BinaryAssociation = BinaryAssociation(
    name="toolSection167",
    ends={
        Property(name="tool_ToolSection", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription168", type=tool_ToolSection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
deletionDescription182: BinaryAssociation = BinaryAssociation(
    name="deletionDescription182",
    ends={
        Property(name="tool_DeleteElementDescription", type=diagram_description_DiagramElementMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramElementMapping", type=tool_DeleteElementDescription, multiplicity=Multiplicity(0, 1))
    }
)
importedDiagram172: BinaryAssociation = BinaryAssociation(
    name="importedDiagram172",
    ends={
        Property(name="DiagramDescription173", type=diagram_description_DiagramImportDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramImportDescription", type=DiagramDescription, multiplicity=Multiplicity(0, 1))
    }
)
layers174: BinaryAssociation = BinaryAssociation(
    name="layers174",
    ends={
        Property(name="AdditionalLayer175", type=diagram_description_DiagramExtensionDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramExtensionDescription", type=AdditionalLayer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
validationSet176: BinaryAssociation = BinaryAssociation(
    name="validationSet176",
    ends={
        Property(name="validation_ValidationSet178", type=diagram_description_DiagramExtensionDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramExtensionDescription177", type=validation_ValidationSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
concerns179: BinaryAssociation = BinaryAssociation(
    name="concerns179",
    ends={
        Property(name="concern_ConcernSet181", type=diagram_description_DiagramExtensionDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramExtensionDescription180", type=concern_ConcernSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
reusedBorderedNodeMappings188: BinaryAssociation = BinaryAssociation(
    name="reusedBorderedNodeMappings188",
    ends={
        Property(name="NodeMapping190", type=diagram_description_AbstractNodeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_AbstractNodeMapping189", type=NodeMapping, multiplicity=Multiplicity(0, 9999))
    }
)
labelDirectEdit183: BinaryAssociation = BinaryAssociation(
    name="labelDirectEdit183",
    ends={
        Property(name="tool_DirectEditLabel", type=diagram_description_DiagramElementMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramElementMapping184", type=tool_DirectEditLabel, multiplicity=Multiplicity(0, 1))
    }
)
doubleClickDescription185: BinaryAssociation = BinaryAssociation(
    name="doubleClickDescription185",
    ends={
        Property(name="description", type=diagram_description_DiagramElementMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="tool", type=tool_DoubleClickDescription, multiplicity=Multiplicity(0, 1))
    }
)
borderedNodeMappings186: BinaryAssociation = BinaryAssociation(
    name="borderedNodeMappings186",
    ends={
        Property(name="NodeMapping187", type=diagram_description_AbstractNodeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_AbstractNodeMapping", type=NodeMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
style191: BinaryAssociation = BinaryAssociation(
    name="style191",
    ends={
        Property(name="style_NodeStyleDescription", type=diagram_description_NodeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_NodeMapping", type=style_NodeStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditionnalStyles192: BinaryAssociation = BinaryAssociation(
    name="conditionnalStyles192",
    ends={
        Property(name="ConditionalNodeStyleDescription", type=diagram_description_NodeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_NodeMapping193", type=ConditionalNodeStyleDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subNodeMappings194: BinaryAssociation = BinaryAssociation(
    name="subNodeMappings194",
    ends={
        Property(name="NodeMapping195", type=diagram_description_ContainerMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_ContainerMapping", type=NodeMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allNodeMappings196: BinaryAssociation = BinaryAssociation(
    name="allNodeMappings196",
    ends={
        Property(name="NodeMapping198", type=diagram_description_ContainerMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_ContainerMapping197", type=NodeMapping, multiplicity=Multiplicity(0, 9999))
    }
)
reusedNodeMappings199: BinaryAssociation = BinaryAssociation(
    name="reusedNodeMappings199",
    ends={
        Property(name="NodeMapping201", type=diagram_description_ContainerMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_ContainerMapping200", type=NodeMapping, multiplicity=Multiplicity(0, 9999))
    }
)
subContainerMappings202: BinaryAssociation = BinaryAssociation(
    name="subContainerMappings202",
    ends={
        Property(name="ContainerMapping204", type=diagram_description_ContainerMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_ContainerMapping203", type=ContainerMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reusedContainerMappings205: BinaryAssociation = BinaryAssociation(
    name="reusedContainerMappings205",
    ends={
        Property(name="ContainerMapping207", type=diagram_description_ContainerMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_ContainerMapping206", type=ContainerMapping, multiplicity=Multiplicity(0, 9999))
    }
)
allContainerMappings208: BinaryAssociation = BinaryAssociation(
    name="allContainerMappings208",
    ends={
        Property(name="ContainerMapping210", type=diagram_description_ContainerMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_ContainerMapping209", type=ContainerMapping, multiplicity=Multiplicity(0, 9999))
    }
)
style211: BinaryAssociation = BinaryAssociation(
    name="style211",
    ends={
        Property(name="style_ContainerStyleDescription", type=diagram_description_ContainerMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_ContainerMapping212", type=style_ContainerStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditionnalStyles213: BinaryAssociation = BinaryAssociation(
    name="conditionnalStyles213",
    ends={
        Property(name="ConditionalContainerStyleDescription", type=diagram_description_ContainerMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_ContainerMapping214", type=ConditionalContainerStyleDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedMapping215: BinaryAssociation = BinaryAssociation(
    name="importedMapping215",
    ends={
        Property(name="NodeMapping216", type=diagram_description_NodeMappingImport, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_NodeMappingImport", type=NodeMapping, multiplicity=Multiplicity(1, 1))
    }
)
importedMapping217: BinaryAssociation = BinaryAssociation(
    name="importedMapping217",
    ends={
        Property(name="ContainerMapping218", type=diagram_description_ContainerMappingImport, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_ContainerMappingImport", type=ContainerMapping, multiplicity=Multiplicity(1, 1))
    }
)
conditionnalStyles226: BinaryAssociation = BinaryAssociation(
    name="conditionnalStyles226",
    ends={
        Property(name="ConditionalEdgeStyleDescription", type=diagram_description_EdgeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_EdgeMapping227", type=ConditionalEdgeStyleDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sourceMapping219: BinaryAssociation = BinaryAssociation(
    name="sourceMapping219",
    ends={
        Property(name="DiagramElementMapping220", type=diagram_description_EdgeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_EdgeMapping", type=DiagramElementMapping, multiplicity=Multiplicity(1, 9999))
    }
)
targetMapping221: BinaryAssociation = BinaryAssociation(
    name="targetMapping221",
    ends={
        Property(name="DiagramElementMapping223", type=diagram_description_EdgeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_EdgeMapping222", type=DiagramElementMapping, multiplicity=Multiplicity(1, 9999))
    }
)
style224: BinaryAssociation = BinaryAssociation(
    name="style224",
    ends={
        Property(name="style_EdgeStyleDescription", type=diagram_description_EdgeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_EdgeMapping225", type=style_EdgeStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nodeMapping243: BinaryAssociation = BinaryAssociation(
    name="nodeMapping243",
    ends={
        Property(name="AbstractNodeMapping244", type=diagram_description_OrderedTreeLayout, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_OrderedTreeLayout", type=AbstractNodeMapping, multiplicity=Multiplicity(1, 9999))
    }
)
reconnections228: BinaryAssociation = BinaryAssociation(
    name="reconnections228",
    ends={
        Property(name="tool_ReconnectEdgeDescription", type=diagram_description_EdgeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_EdgeMapping229", type=tool_ReconnectEdgeDescription, multiplicity=Multiplicity(0, 9999))
    }
)
pathNodeMapping230: BinaryAssociation = BinaryAssociation(
    name="pathNodeMapping230",
    ends={
        Property(name="AbstractNodeMapping", type=diagram_description_EdgeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_EdgeMapping231", type=AbstractNodeMapping, multiplicity=Multiplicity(0, 9999))
    }
)
importedMapping232: BinaryAssociation = BinaryAssociation(
    name="importedMapping232",
    ends={
        Property(name="IEdgeMapping233", type=diagram_description_EdgeMappingImport, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_EdgeMappingImport", type=IEdgeMapping, multiplicity=Multiplicity(1, 1))
    }
)
conditionnalStyles234: BinaryAssociation = BinaryAssociation(
    name="conditionnalStyles234",
    ends={
        Property(name="ConditionalEdgeStyleDescription236", type=diagram_description_EdgeMappingImport, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_EdgeMappingImport235", type=ConditionalEdgeStyleDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
style237: BinaryAssociation = BinaryAssociation(
    name="style237",
    ends={
        Property(name="style_NodeStyleDescription238", type=diagram_description_ConditionalNodeStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_ConditionalNodeStyleDescription", type=style_NodeStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
style239: BinaryAssociation = BinaryAssociation(
    name="style239",
    ends={
        Property(name="style_EdgeStyleDescription240", type=diagram_description_ConditionalEdgeStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_ConditionalEdgeStyleDescription", type=style_EdgeStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
style241: BinaryAssociation = BinaryAssociation(
    name="style241",
    ends={
        Property(name="style_ContainerStyleDescription242", type=diagram_description_ConditionalContainerStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_ConditionalContainerStyleDescription", type=style_ContainerStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
reusedTools267: BinaryAssociation = BinaryAssociation(
    name="reusedTools267",
    ends={
        Property(name="tool_AbstractToolDescription269", type=diagram_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_Layer268", type=tool_AbstractToolDescription, multiplicity=Multiplicity(0, 9999))
    }
)
decorationDescriptionsSet270: BinaryAssociation = BinaryAssociation(
    name="decorationDescriptionsSet270",
    ends={
        Property(name="DecorationDescriptionsSet", type=diagram_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_Layer271", type=DecorationDescriptionsSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
allEdgeMappings272: BinaryAssociation = BinaryAssociation(
    name="allEdgeMappings272",
    ends={
        Property(name="EdgeMapping274", type=diagram_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_Layer273", type=EdgeMapping, multiplicity=Multiplicity(0, 9999))
    }
)
mappings245: BinaryAssociation = BinaryAssociation(
    name="mappings245",
    ends={
        Property(name="DiagramElementMapping246", type=diagram_description_MappingBasedDecoration, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_MappingBasedDecoration", type=DiagramElementMapping, multiplicity=Multiplicity(1, 9999))
    }
)
nodeMappings247: BinaryAssociation = BinaryAssociation(
    name="nodeMappings247",
    ends={
        Property(name="NodeMapping248", type=diagram_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_Layer", type=NodeMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edgeMappings249: BinaryAssociation = BinaryAssociation(
    name="edgeMappings249",
    ends={
        Property(name="EdgeMapping251", type=diagram_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_Layer250", type=EdgeMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edgeMappingImports252: BinaryAssociation = BinaryAssociation(
    name="edgeMappingImports252",
    ends={
        Property(name="EdgeMappingImport254", type=diagram_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_Layer253", type=EdgeMappingImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containerMappings255: BinaryAssociation = BinaryAssociation(
    name="containerMappings255",
    ends={
        Property(name="ContainerMapping257", type=diagram_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_Layer256", type=ContainerMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reusedMappings258: BinaryAssociation = BinaryAssociation(
    name="reusedMappings258",
    ends={
        Property(name="DiagramElementMapping260", type=diagram_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_Layer259", type=DiagramElementMapping, multiplicity=Multiplicity(0, 9999))
    }
)
allTools261: BinaryAssociation = BinaryAssociation(
    name="allTools261",
    ends={
        Property(name="tool_AbstractToolDescription263", type=diagram_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_Layer262", type=tool_AbstractToolDescription, multiplicity=Multiplicity(0, 9999))
    }
)
toolSections264: BinaryAssociation = BinaryAssociation(
    name="toolSections264",
    ends={
        Property(name="tool_ToolSection266", type=diagram_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_Layer265", type=tool_ToolSection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
customization275: BinaryAssociation = BinaryAssociation(
    name="customization275",
    ends={
        Property(name="Customization", type=diagram_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_Layer276", type=Customization, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dropDescriptions277: BinaryAssociation = BinaryAssociation(
    name="dropDescriptions277",
    ends={
        Property(name="tool_ContainerDropDescription", type=diagram_description_DragAndDropTargetDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DragAndDropTargetDescription", type=tool_ContainerDropDescription, multiplicity=Multiplicity(0, 9999))
    }
)
borderColor278: BinaryAssociation = BinaryAssociation(
    name="borderColor278",
    ends={
        Property(name="ColorDescription", type=diagram_style_BorderedStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_BorderedStyleDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
color283: BinaryAssociation = BinaryAssociation(
    name="color283",
    ends={
        Property(name="diagram_style_EllipseNodeDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="ColorDescription284", type=diagram_style_EllipseNodeDescription, multiplicity=Multiplicity(1, 1))
    }
)
color279: BinaryAssociation = BinaryAssociation(
    name="color279",
    ends={
        Property(name="ColorDescription280", type=diagram_style_SquareDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_SquareDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
color281: BinaryAssociation = BinaryAssociation(
    name="color281",
    ends={
        Property(name="ColorDescription282", type=diagram_style_LozengeNodeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_LozengeNodeDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
backgroundColor292: BinaryAssociation = BinaryAssociation(
    name="backgroundColor292",
    ends={
        Property(name="ColorDescription293", type=diagram_style_GaugeSectionDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_GaugeSectionDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
foregroundColor294: BinaryAssociation = BinaryAssociation(
    name="foregroundColor294",
    ends={
        Property(name="ColorDescription296", type=diagram_style_GaugeSectionDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_GaugeSectionDescription295", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
color285: BinaryAssociation = BinaryAssociation(
    name="color285",
    ends={
        Property(name="ColorDescription286", type=diagram_style_BundledImageDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_BundledImageDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
color287: BinaryAssociation = BinaryAssociation(
    name="color287",
    ends={
        Property(name="ColorDescription288", type=diagram_style_NoteDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_NoteDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
backgroundColor289: BinaryAssociation = BinaryAssociation(
    name="backgroundColor289",
    ends={
        Property(name="ColorDescription290", type=diagram_style_DotDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_DotDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
sections291: BinaryAssociation = BinaryAssociation(
    name="sections291",
    ends={
        Property(name="style_GaugeSectionDescription", type=diagram_style_GaugeCompositeStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_GaugeCompositeStyleDescription", type=style_GaugeSectionDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
foregroundColor299: BinaryAssociation = BinaryAssociation(
    name="foregroundColor299",
    ends={
        Property(name="ColorDescription301", type=diagram_style_FlatContainerStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_FlatContainerStyleDescription300", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
labelBorderStyle302: BinaryAssociation = BinaryAssociation(
    name="labelBorderStyle302",
    ends={
        Property(name="style_LabelBorderStyleDescription", type=diagram_style_FlatContainerStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_FlatContainerStyleDescription303", type=style_LabelBorderStyleDescription, multiplicity=Multiplicity(0, 1))
    }
)
backgroundColor304: BinaryAssociation = BinaryAssociation(
    name="backgroundColor304",
    ends={
        Property(name="ColorDescription305", type=diagram_style_ShapeContainerStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_ShapeContainerStyleDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
backgroundColor297: BinaryAssociation = BinaryAssociation(
    name="backgroundColor297",
    ends={
        Property(name="ColorDescription298", type=diagram_style_FlatContainerStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_FlatContainerStyleDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
beginLabelStyleDescription308: BinaryAssociation = BinaryAssociation(
    name="beginLabelStyleDescription308",
    ends={
        Property(name="style_BeginLabelStyleDescription", type=diagram_style_EdgeStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_EdgeStyleDescription309", type=style_BeginLabelStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
centerLabelStyleDescription310: BinaryAssociation = BinaryAssociation(
    name="centerLabelStyleDescription310",
    ends={
        Property(name="style_CenterLabelStyleDescription", type=diagram_style_EdgeStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_EdgeStyleDescription311", type=style_CenterLabelStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
endLabelStyleDescription312: BinaryAssociation = BinaryAssociation(
    name="endLabelStyleDescription312",
    ends={
        Property(name="style_EndLabelStyleDescription", type=diagram_style_EdgeStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_EdgeStyleDescription313", type=style_EndLabelStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
centeredSourceMappings314: BinaryAssociation = BinaryAssociation(
    name="centeredSourceMappings314",
    ends={
        Property(name="DiagramElementMapping316", type=diagram_style_EdgeStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_EdgeStyleDescription315", type=DiagramElementMapping, multiplicity=Multiplicity(0, 9999))
    }
)
centeredTargetMappings317: BinaryAssociation = BinaryAssociation(
    name="centeredTargetMappings317",
    ends={
        Property(name="DiagramElementMapping319", type=diagram_style_EdgeStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_EdgeStyleDescription318", type=DiagramElementMapping, multiplicity=Multiplicity(0, 9999))
    }
)
strokeColor306: BinaryAssociation = BinaryAssociation(
    name="strokeColor306",
    ends={
        Property(name="ColorDescription307", type=diagram_style_EdgeStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_EdgeStyleDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
popupMenus324: BinaryAssociation = BinaryAssociation(
    name="popupMenus324",
    ends={
        Property(name="tool_PopupMenu", type=diagram_tool_ToolSection, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ToolSection325", type=tool_PopupMenu, multiplicity=Multiplicity(0, 9999))
    }
)
reusedTools326: BinaryAssociation = BinaryAssociation(
    name="reusedTools326",
    ends={
        Property(name="tool_ToolEntry328", type=diagram_tool_ToolSection, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ToolSection327", type=tool_ToolEntry, multiplicity=Multiplicity(0, 9999))
    }
)
groupExtensions329: BinaryAssociation = BinaryAssociation(
    name="groupExtensions329",
    ends={
        Property(name="tool_ToolGroupExtension", type=diagram_tool_ToolSection, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ToolSection330", type=tool_ToolGroupExtension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tools331: BinaryAssociation = BinaryAssociation(
    name="tools331",
    ends={
        Property(name="tool_AbstractToolDescription332", type=diagram_tool_ToolGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ToolGroup", type=tool_AbstractToolDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
group333: BinaryAssociation = BinaryAssociation(
    name="group333",
    ends={
        Property(name="tool_ToolGroup", type=diagram_tool_ToolGroupExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ToolGroupExtension", type=tool_ToolGroup, multiplicity=Multiplicity(1, 1))
    }
)
ownedTools320: BinaryAssociation = BinaryAssociation(
    name="ownedTools320",
    ends={
        Property(name="tool_ToolEntry", type=diagram_tool_ToolSection, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ToolSection", type=tool_ToolEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subSections321: BinaryAssociation = BinaryAssociation(
    name="subSections321",
    ends={
        Property(name="tool_ToolSection323", type=diagram_tool_ToolSection, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ToolSection322", type=tool_ToolSection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
viewVariable341: BinaryAssociation = BinaryAssociation(
    name="viewVariable341",
    ends={
        Property(name="diagram_tool_NodeCreationDescription342", type=tool_ContainerViewVariable, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="tool_ContainerViewVariable", type=diagram_tool_NodeCreationDescription, multiplicity=Multiplicity(1, 1))
    }
)
initialOperation343: BinaryAssociation = BinaryAssociation(
    name="initialOperation343",
    ends={
        Property(name="tool_InitialNodeCreationOperation", type=diagram_tool_NodeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_NodeCreationDescription344", type=tool_InitialNodeCreationOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
extraMappings345: BinaryAssociation = BinaryAssociation(
    name="extraMappings345",
    ends={
        Property(name="AbstractNodeMapping347", type=diagram_tool_NodeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_NodeCreationDescription346", type=AbstractNodeMapping, multiplicity=Multiplicity(0, 9999))
    }
)
tools334: BinaryAssociation = BinaryAssociation(
    name="tools334",
    ends={
        Property(name="tool_AbstractToolDescription336", type=diagram_tool_ToolGroupExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ToolGroupExtension335", type=tool_AbstractToolDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodeMappings337: BinaryAssociation = BinaryAssociation(
    name="nodeMappings337",
    ends={
        Property(name="NodeMapping338", type=diagram_tool_NodeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_NodeCreationDescription", type=NodeMapping, multiplicity=Multiplicity(1, 9999))
    }
)
variable339: BinaryAssociation = BinaryAssociation(
    name="variable339",
    ends={
        Property(name="tool_NodeCreationVariable", type=diagram_tool_NodeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_NodeCreationDescription340", type=tool_NodeCreationVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
targetVariable352: BinaryAssociation = BinaryAssociation(
    name="targetVariable352",
    ends={
        Property(name="tool_TargetEdgeCreationVariable", type=diagram_tool_EdgeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_EdgeCreationDescription353", type=tool_TargetEdgeCreationVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sourceViewVariable354: BinaryAssociation = BinaryAssociation(
    name="sourceViewVariable354",
    ends={
        Property(name="tool_SourceEdgeViewCreationVariable", type=diagram_tool_EdgeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_EdgeCreationDescription355", type=tool_SourceEdgeViewCreationVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
targetViewVariable356: BinaryAssociation = BinaryAssociation(
    name="targetViewVariable356",
    ends={
        Property(name="tool_TargetEdgeViewCreationVariable", type=diagram_tool_EdgeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_EdgeCreationDescription357", type=tool_TargetEdgeViewCreationVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialOperation358: BinaryAssociation = BinaryAssociation(
    name="initialOperation358",
    ends={
        Property(name="tool_InitEdgeCreationOperation", type=diagram_tool_EdgeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_EdgeCreationDescription359", type=tool_InitEdgeCreationOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
edgeMappings348: BinaryAssociation = BinaryAssociation(
    name="edgeMappings348",
    ends={
        Property(name="EdgeMapping349", type=diagram_tool_EdgeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_EdgeCreationDescription", type=EdgeMapping, multiplicity=Multiplicity(1, 9999))
    }
)
sourceVariable350: BinaryAssociation = BinaryAssociation(
    name="sourceVariable350",
    ends={
        Property(name="tool_SourceEdgeCreationVariable", type=diagram_tool_EdgeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_EdgeCreationDescription351", type=tool_SourceEdgeCreationVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialOperation374: BinaryAssociation = BinaryAssociation(
    name="initialOperation374",
    ends={
        Property(name="tool_InitialNodeCreationOperation376", type=diagram_tool_ContainerCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ContainerCreationDescription375", type=tool_InitialNodeCreationOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
extraMappings377: BinaryAssociation = BinaryAssociation(
    name="extraMappings377",
    ends={
        Property(name="AbstractNodeMapping379", type=diagram_tool_ContainerCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ContainerCreationDescription378", type=AbstractNodeMapping, multiplicity=Multiplicity(0, 9999))
    }
)
element380: BinaryAssociation = BinaryAssociation(
    name="element380",
    ends={
        Property(name="tool_ElementDeleteVariable", type=diagram_tool_DeleteElementDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DeleteElementDescription", type=tool_ElementDeleteVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elementView381: BinaryAssociation = BinaryAssociation(
    name="elementView381",
    ends={
        Property(name="tool_ElementDeleteVariable383", type=diagram_tool_DeleteElementDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DeleteElementDescription382", type=tool_ElementDeleteVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
containerView384: BinaryAssociation = BinaryAssociation(
    name="containerView384",
    ends={
        Property(name="tool_ContainerViewVariable386", type=diagram_tool_DeleteElementDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DeleteElementDescription385", type=tool_ContainerViewVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
extraSourceMappings360: BinaryAssociation = BinaryAssociation(
    name="extraSourceMappings360",
    ends={
        Property(name="DiagramElementMapping362", type=diagram_tool_EdgeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_EdgeCreationDescription361", type=DiagramElementMapping, multiplicity=Multiplicity(0, 9999))
    }
)
extraTargetMappings363: BinaryAssociation = BinaryAssociation(
    name="extraTargetMappings363",
    ends={
        Property(name="DiagramElementMapping365", type=diagram_tool_EdgeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_EdgeCreationDescription364", type=DiagramElementMapping, multiplicity=Multiplicity(0, 9999))
    }
)
containerMappings366: BinaryAssociation = BinaryAssociation(
    name="containerMappings366",
    ends={
        Property(name="ContainerMapping367", type=diagram_tool_ContainerCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ContainerCreationDescription", type=ContainerMapping, multiplicity=Multiplicity(1, 9999))
    }
)
variable368: BinaryAssociation = BinaryAssociation(
    name="variable368",
    ends={
        Property(name="tool_NodeCreationVariable370", type=diagram_tool_ContainerCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ContainerCreationDescription369", type=tool_NodeCreationVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
viewVariable371: BinaryAssociation = BinaryAssociation(
    name="viewVariable371",
    ends={
        Property(name="tool_ContainerViewVariable373", type=diagram_tool_ContainerCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ContainerCreationDescription372", type=tool_ContainerViewVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters402: BinaryAssociation = BinaryAssociation(
    name="parameters402",
    ends={
        Property(name="tool_DeleteHookParameter", type=diagram_tool_DeleteHook, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DeleteHook", type=tool_DeleteHookParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source403: BinaryAssociation = BinaryAssociation(
    name="source403",
    ends={
        Property(name="tool_SourceEdgeCreationVariable404", type=diagram_tool_ReconnectEdgeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ReconnectEdgeDescription", type=tool_SourceEdgeCreationVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialOperation387: BinaryAssociation = BinaryAssociation(
    name="initialOperation387",
    ends={
        Property(name="tool_InitialOperation389", type=diagram_tool_DeleteElementDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DeleteElementDescription388", type=tool_InitialOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
hook390: BinaryAssociation = BinaryAssociation(
    name="hook390",
    ends={
        Property(name="tool_DeleteHook", type=diagram_tool_DeleteElementDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DeleteElementDescription391", type=tool_DeleteHook, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mappings392: BinaryAssociation = BinaryAssociation(
    name="mappings392",
    ends={
        Property(name="description394", type=diagram_tool_DoubleClickDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="DiagramElementMapping393", type=DiagramElementMapping, multiplicity=Multiplicity(1, 9999))
    }
)
element395: BinaryAssociation = BinaryAssociation(
    name="element395",
    ends={
        Property(name="tool_ElementDoubleClickVariable", type=diagram_tool_DoubleClickDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DoubleClickDescription", type=tool_ElementDoubleClickVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elementView396: BinaryAssociation = BinaryAssociation(
    name="elementView396",
    ends={
        Property(name="tool_ElementDoubleClickVariable398", type=diagram_tool_DoubleClickDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DoubleClickDescription397", type=tool_ElementDoubleClickVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initialOperation399: BinaryAssociation = BinaryAssociation(
    name="initialOperation399",
    ends={
        Property(name="tool_InitialOperation401", type=diagram_tool_DoubleClickDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DoubleClickDescription400", type=tool_InitialOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mask422: BinaryAssociation = BinaryAssociation(
    name="mask422",
    ends={
        Property(name="tool_EditMaskVariables", type=diagram_tool_DirectEditLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DirectEditLabel", type=tool_EditMaskVariables, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialOperation423: BinaryAssociation = BinaryAssociation(
    name="initialOperation423",
    ends={
        Property(name="tool_InitialOperation425", type=diagram_tool_DirectEditLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DirectEditLabel424", type=tool_InitialOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target405: BinaryAssociation = BinaryAssociation(
    name="target405",
    ends={
        Property(name="tool_TargetEdgeCreationVariable407", type=diagram_tool_ReconnectEdgeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ReconnectEdgeDescription406", type=tool_TargetEdgeCreationVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sourceView408: BinaryAssociation = BinaryAssociation(
    name="sourceView408",
    ends={
        Property(name="tool_SourceEdgeViewCreationVariable410", type=diagram_tool_ReconnectEdgeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ReconnectEdgeDescription409", type=tool_SourceEdgeViewCreationVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
targetView411: BinaryAssociation = BinaryAssociation(
    name="targetView411",
    ends={
        Property(name="tool_TargetEdgeViewCreationVariable413", type=diagram_tool_ReconnectEdgeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ReconnectEdgeDescription412", type=tool_TargetEdgeViewCreationVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
element414: BinaryAssociation = BinaryAssociation(
    name="element414",
    ends={
        Property(name="tool_ElementSelectVariable", type=diagram_tool_ReconnectEdgeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ReconnectEdgeDescription415", type=tool_ElementSelectVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialOperation416: BinaryAssociation = BinaryAssociation(
    name="initialOperation416",
    ends={
        Property(name="tool_InitialOperation418", type=diagram_tool_ReconnectEdgeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ReconnectEdgeDescription417", type=tool_InitialOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
edgeView419: BinaryAssociation = BinaryAssociation(
    name="edgeView419",
    ends={
        Property(name="tool_ElementSelectVariable421", type=diagram_tool_ReconnectEdgeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ReconnectEdgeDescription420", type=tool_ElementSelectVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
diagramDescription430: BinaryAssociation = BinaryAssociation(
    name="diagramDescription430",
    ends={
        Property(name="DiagramDescription431", type=diagram_tool_Navigation, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_Navigation", type=DiagramDescription, multiplicity=Multiplicity(1, 1))
    }
)
initialOperation426: BinaryAssociation = BinaryAssociation(
    name="initialOperation426",
    ends={
        Property(name="tool_InitialOperation427", type=diagram_tool_BehaviorTool, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_BehaviorTool", type=tool_InitialOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mapping428: BinaryAssociation = BinaryAssociation(
    name="mapping428",
    ends={
        Property(name="DiagramElementMapping429", type=diagram_tool_CreateView, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_CreateView", type=DiagramElementMapping, multiplicity=Multiplicity(1, 1))
    }
)
element443: BinaryAssociation = BinaryAssociation(
    name="element443",
    ends={
        Property(name="tool_ElementDropVariable", type=diagram_tool_ContainerDropDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ContainerDropDescription444", type=tool_ElementDropVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
newViewContainer445: BinaryAssociation = BinaryAssociation(
    name="newViewContainer445",
    ends={
        Property(name="tool_ContainerViewVariable447", type=diagram_tool_ContainerDropDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ContainerDropDescription446", type=tool_ContainerViewVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialOperation448: BinaryAssociation = BinaryAssociation(
    name="initialOperation448",
    ends={
        Property(name="tool_InitialContainerDropOperation", type=diagram_tool_ContainerDropDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ContainerDropDescription449", type=tool_InitialContainerDropOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
diagramDescription432: BinaryAssociation = BinaryAssociation(
    name="diagramDescription432",
    ends={
        Property(name="DiagramDescription433", type=diagram_tool_DiagramCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DiagramCreationDescription", type=DiagramDescription, multiplicity=Multiplicity(1, 1))
    }
)
diagramDescription434: BinaryAssociation = BinaryAssociation(
    name="diagramDescription434",
    ends={
        Property(name="DiagramDescription435", type=diagram_tool_DiagramNavigationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DiagramNavigationDescription", type=DiagramDescription, multiplicity=Multiplicity(1, 1))
    }
)
mappings436: BinaryAssociation = BinaryAssociation(
    name="mappings436",
    ends={
        Property(name="DiagramElementMapping437", type=diagram_tool_ContainerDropDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ContainerDropDescription", type=DiagramElementMapping, multiplicity=Multiplicity(0, 9999))
    }
)
oldContainer438: BinaryAssociation = BinaryAssociation(
    name="oldContainer438",
    ends={
        Property(name="tool_DropContainerVariable", type=diagram_tool_ContainerDropDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ContainerDropDescription439", type=tool_DropContainerVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
newContainer440: BinaryAssociation = BinaryAssociation(
    name="newContainer440",
    ends={
        Property(name="tool_DropContainerVariable442", type=diagram_tool_ContainerDropDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ContainerDropDescription441", type=tool_DropContainerVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
filters452: BinaryAssociation = BinaryAssociation(
    name="filters452",
    ends={
        Property(name="filter_Filter", type=diagram_filter_CompositeFilterDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_filter_CompositeFilterDescription", type=filter_Filter, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ownedVariables453: BinaryAssociation = BinaryAssociation(
    name="ownedVariables453",
    ends={
        Property(name="InteractiveVariableDescription", type=diagram_filter_VariableFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_filter_VariableFilter", type=InteractiveVariableDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedConcernDescriptions454: BinaryAssociation = BinaryAssociation(
    name="ownedConcernDescriptions454",
    ends={
        Property(name="concern_ConcernDescription455", type=diagram_concern_ConcernSet, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_concern_ConcernSet", type=concern_ConcernDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
filters456: BinaryAssociation = BinaryAssociation(
    name="filters456",
    ends={
        Property(name="filter_FilterDescription457", type=diagram_concern_ConcernDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_concern_ConcernDescription", type=filter_FilterDescription, multiplicity=Multiplicity(0, 9999))
    }
)
rules458: BinaryAssociation = BinaryAssociation(
    name="rules458",
    ends={
        Property(name="validation_ValidationRule460", type=diagram_concern_ConcernDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_concern_ConcernDescription459", type=validation_ValidationRule, multiplicity=Multiplicity(0, 9999))
    }
)
mappings450: BinaryAssociation = BinaryAssociation(
    name="mappings450",
    ends={
        Property(name="DiagramElementMapping451", type=diagram_filter_MappingFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_filter_MappingFilter", type=DiagramElementMapping, multiplicity=Multiplicity(0, 9999))
    }
)
behaviors461: BinaryAssociation = BinaryAssociation(
    name="behaviors461",
    ends={
        Property(name="tool_BehaviorTool463", type=diagram_concern_ConcernDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_concern_ConcernDescription462", type=tool_BehaviorTool, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_diagram_DDiagram_DRepresentation = Generalization(general=DRepresentation, specific=diagram_DDiagram)
gen_diagram_DDiagram_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=diagram_DDiagram)
gen_diagram_DDiagram_DragAndDropTarget = Generalization(general=DragAndDropTarget, specific=diagram_DDiagram)
gen_diagram_AbsoluteBoundsFilter_GraphicalFilter = Generalization(general=GraphicalFilter, specific=diagram_AbsoluteBoundsFilter)
gen_diagram_DSemanticDiagram_DDiagram = Generalization(general=DDiagram, specific=diagram_DSemanticDiagram)
gen_diagram_DSemanticDiagram_DSemanticDecorator = Generalization(general=DSemanticDecorator, specific=diagram_DSemanticDiagram)
gen_diagram_DDiagramElement_DRepresentationElement = Generalization(general=DRepresentationElement, specific=diagram_DDiagramElement)
gen_diagram_HideFilter_GraphicalFilter = Generalization(general=GraphicalFilter, specific=diagram_HideFilter)
gen_diagram_HideLabelFilter_GraphicalFilter = Generalization(general=GraphicalFilter, specific=diagram_HideLabelFilter)
gen_diagram_FoldingPointFilter_GraphicalFilter = Generalization(general=GraphicalFilter, specific=diagram_FoldingPointFilter)
gen_diagram_FoldingFilter_GraphicalFilter = Generalization(general=GraphicalFilter, specific=diagram_FoldingFilter)
gen_diagram_AppliedCompositeFilters_GraphicalFilter = Generalization(general=GraphicalFilter, specific=diagram_AppliedCompositeFilters)
gen_diagram_AbstractDNode_DDiagramElement = Generalization(general=DDiagramElement, specific=diagram_AbstractDNode)
gen_diagram_DNode_AbstractDNode = Generalization(general=AbstractDNode, specific=diagram_DNode)
gen_diagram_DNode_EdgeTarget = Generalization(general=EdgeTarget, specific=diagram_DNode)
gen_diagram_DNode_DragAndDropTarget = Generalization(general=DragAndDropTarget, specific=diagram_DNode)
gen_diagram_DDiagramElementContainer_AbstractDNode = Generalization(general=AbstractDNode, specific=diagram_DDiagramElementContainer)
gen_diagram_DDiagramElementContainer_EdgeTarget = Generalization(general=EdgeTarget, specific=diagram_DDiagramElementContainer)
gen_diagram_DDiagramElementContainer_DragAndDropTarget = Generalization(general=DragAndDropTarget, specific=diagram_DDiagramElementContainer)
gen_diagram_DNodeList_DDiagramElementContainer = Generalization(general=DDiagramElementContainer, specific=diagram_DNodeList)
gen_diagram_DNodeContainer_DDiagramElementContainer = Generalization(general=DDiagramElementContainer, specific=diagram_DNodeContainer)
gen_diagram_DNodeListElement_AbstractDNode = Generalization(general=AbstractDNode, specific=diagram_DNodeListElement)
gen_diagram_DEdge_DDiagramElement = Generalization(general=DDiagramElement, specific=diagram_DEdge)
gen_diagram_DEdge_EdgeTarget = Generalization(general=EdgeTarget, specific=diagram_DEdge)
gen_diagram_GaugeSection_Customizable = Generalization(general=Customizable, specific=diagram_GaugeSection)
gen_diagram_NodeStyle_LabelStyle = Generalization(general=LabelStyle, specific=diagram_NodeStyle)
gen_diagram_NodeStyle_Style = Generalization(general=Style, specific=diagram_NodeStyle)
gen_diagram_NodeStyle_BorderedStyle = Generalization(general=BorderedStyle, specific=diagram_NodeStyle)
gen_diagram_NodeStyle_HideLabelCapabilityStyle = Generalization(general=HideLabelCapabilityStyle, specific=diagram_NodeStyle)
gen_diagram_Dot_NodeStyle = Generalization(general=NodeStyle, specific=diagram_Dot)
gen_diagram_Square_NodeStyle = Generalization(general=NodeStyle, specific=diagram_Square)
gen_diagram_ContainerStyle_LabelStyle = Generalization(general=LabelStyle, specific=diagram_ContainerStyle)
gen_diagram_ContainerStyle_Style = Generalization(general=Style, specific=diagram_ContainerStyle)
gen_diagram_ContainerStyle_BorderedStyle = Generalization(general=BorderedStyle, specific=diagram_ContainerStyle)
gen_diagram_ContainerStyle_HideLabelCapabilityStyle = Generalization(general=HideLabelCapabilityStyle, specific=diagram_ContainerStyle)
gen_diagram_FlatContainerStyle_ContainerStyle = Generalization(general=ContainerStyle, specific=diagram_FlatContainerStyle)
gen_diagram_ShapeContainerStyle_ContainerStyle = Generalization(general=ContainerStyle, specific=diagram_ShapeContainerStyle)
gen_diagram_Ellipse_NodeStyle = Generalization(general=NodeStyle, specific=diagram_Ellipse)
gen_diagram_Lozenge_NodeStyle = Generalization(general=NodeStyle, specific=diagram_Lozenge)
gen_diagram_BundledImage_NodeStyle = Generalization(general=NodeStyle, specific=diagram_BundledImage)
gen_diagram_WorkspaceImage_NodeStyle = Generalization(general=NodeStyle, specific=diagram_WorkspaceImage)
gen_diagram_WorkspaceImage_ContainerStyle = Generalization(general=ContainerStyle, specific=diagram_WorkspaceImage)
gen_diagram_CustomStyle_NodeStyle = Generalization(general=NodeStyle, specific=diagram_CustomStyle)
gen_diagram_EdgeStyle_Style = Generalization(general=Style, specific=diagram_EdgeStyle)
gen_diagram_Note_NodeStyle = Generalization(general=NodeStyle, specific=diagram_Note)
gen_diagram_GaugeCompositeStyle_NodeStyle = Generalization(general=NodeStyle, specific=diagram_GaugeCompositeStyle)
gen_diagram_BorderedStyle_Style = Generalization(general=Style, specific=diagram_BorderedStyle)
gen_diagram_TypedVariableValue_VariableValue = Generalization(general=VariableValue, specific=diagram_TypedVariableValue)
gen_diagram_EObjectVariableValue_VariableValue = Generalization(general=VariableValue, specific=diagram_EObjectVariableValue)
gen_diagram_CollapseFilter_GraphicalFilter = Generalization(general=GraphicalFilter, specific=diagram_CollapseFilter)
gen_diagram_description_DiagramDescription_description_DragAndDropTargetDescription = Generalization(general=description_DragAndDropTargetDescription, specific=diagram_description_DiagramDescription)
gen_diagram_IndirectlyCollapseFilter_CollapseFilter = Generalization(general=CollapseFilter, specific=diagram_IndirectlyCollapseFilter)
gen_diagram_description_DiagramDescription_description_RepresentationDescription = Generalization(general=description_RepresentationDescription, specific=diagram_description_DiagramDescription)
gen_diagram_description_DiagramDescription_description_PasteTargetDescription = Generalization(general=description_PasteTargetDescription, specific=diagram_description_DiagramDescription)
gen_diagram_BeginLabelStyle_BasicLabelStyle = Generalization(general=BasicLabelStyle, specific=diagram_BeginLabelStyle)
gen_diagram_CenterLabelStyle_BasicLabelStyle = Generalization(general=BasicLabelStyle, specific=diagram_CenterLabelStyle)
gen_diagram_EndLabelStyle_BasicLabelStyle = Generalization(general=BasicLabelStyle, specific=diagram_EndLabelStyle)
gen_diagram_BracketEdgeStyle_EdgeStyle = Generalization(general=EdgeStyle, specific=diagram_BracketEdgeStyle)
gen_diagram_description_DiagramImportDescription_description_RepresentationImportDescription = Generalization(general=description_RepresentationImportDescription, specific=diagram_description_DiagramImportDescription)
gen_diagram_description_DiagramImportDescription_description_DiagramDescription = Generalization(general=description_DiagramDescription, specific=diagram_description_DiagramImportDescription)
gen_diagram_description_DiagramExtensionDescription_RepresentationExtensionDescription = Generalization(general=RepresentationExtensionDescription, specific=diagram_description_DiagramExtensionDescription)
gen_diagram_description_DiagramElementMapping_description_RepresentationElementMapping = Generalization(general=description_RepresentationElementMapping, specific=diagram_description_DiagramElementMapping)
gen_diagram_description_DiagramElementMapping_description_PasteTargetDescription = Generalization(general=description_PasteTargetDescription, specific=diagram_description_DiagramElementMapping)
gen_diagram_description_NodeMapping_description_AbstractNodeMapping = Generalization(general=description_AbstractNodeMapping, specific=diagram_description_NodeMapping)
gen_diagram_description_NodeMapping_description_DragAndDropTargetDescription = Generalization(general=description_DragAndDropTargetDescription, specific=diagram_description_NodeMapping)
gen_diagram_description_AbstractNodeMapping_description_DiagramElementMapping = Generalization(general=description_DiagramElementMapping, specific=diagram_description_AbstractNodeMapping)
gen_diagram_description_AbstractNodeMapping_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=diagram_description_AbstractNodeMapping)
gen_diagram_description_ContainerMapping_description_AbstractNodeMapping = Generalization(general=description_AbstractNodeMapping, specific=diagram_description_ContainerMapping)
gen_diagram_description_ContainerMapping_description_DragAndDropTargetDescription = Generalization(general=description_DragAndDropTargetDescription, specific=diagram_description_ContainerMapping)
gen_diagram_description_EdgeMapping_description_DiagramElementMapping = Generalization(general=description_DiagramElementMapping, specific=diagram_description_EdgeMapping)
gen_diagram_description_EdgeMapping_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=diagram_description_EdgeMapping)
gen_diagram_description_EdgeMapping_description_IEdgeMapping = Generalization(general=description_IEdgeMapping, specific=diagram_description_EdgeMapping)
gen_diagram_description_NodeMappingImport_description_NodeMapping = Generalization(general=description_NodeMapping, specific=diagram_description_NodeMappingImport)
gen_diagram_description_NodeMappingImport_description_AbstractMappingImport = Generalization(general=description_AbstractMappingImport, specific=diagram_description_NodeMappingImport)
gen_diagram_description_ContainerMappingImport_description_ContainerMapping = Generalization(general=description_ContainerMapping, specific=diagram_description_ContainerMappingImport)
gen_diagram_description_ContainerMappingImport_description_AbstractMappingImport = Generalization(general=description_AbstractMappingImport, specific=diagram_description_ContainerMappingImport)
gen_diagram_description_OrderedTreeLayout_Layout = Generalization(general=Layout, specific=diagram_description_OrderedTreeLayout)
gen_diagram_description_EdgeMappingImport_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=diagram_description_EdgeMappingImport)
gen_diagram_description_EdgeMappingImport_description_IEdgeMapping = Generalization(general=description_IEdgeMapping, specific=diagram_description_EdgeMappingImport)
gen_diagram_description_EdgeMappingImport_description_IdentifiedElement = Generalization(general=description_IdentifiedElement, specific=diagram_description_EdgeMappingImport)
gen_diagram_description_ConditionalNodeStyleDescription_ConditionalStyleDescription = Generalization(general=ConditionalStyleDescription, specific=diagram_description_ConditionalNodeStyleDescription)
gen_diagram_description_ConditionalEdgeStyleDescription_ConditionalStyleDescription = Generalization(general=ConditionalStyleDescription, specific=diagram_description_ConditionalEdgeStyleDescription)
gen_diagram_description_ConditionalContainerStyleDescription_ConditionalStyleDescription = Generalization(general=ConditionalStyleDescription, specific=diagram_description_ConditionalContainerStyleDescription)
gen_diagram_description_Layout_DocumentedElement = Generalization(general=DocumentedElement, specific=diagram_description_Layout)
gen_diagram_description_CompositeLayout_Layout = Generalization(general=Layout, specific=diagram_description_CompositeLayout)
gen_diagram_description_MappingBasedDecoration_DecorationDescription = Generalization(general=DecorationDescription, specific=diagram_description_MappingBasedDecoration)
gen_diagram_description_Layer_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=diagram_description_Layer)
gen_diagram_description_Layer_description_EndUserDocumentedElement = Generalization(general=description_EndUserDocumentedElement, specific=diagram_description_Layer)
gen_diagram_description_Layer_description_IdentifiedElement = Generalization(general=description_IdentifiedElement, specific=diagram_description_Layer)
gen_diagram_style_NodeStyleDescription_style_StyleDescription = Generalization(general=style_StyleDescription, specific=diagram_style_NodeStyleDescription)
gen_diagram_style_NodeStyleDescription_style_BorderedStyleDescription = Generalization(general=style_BorderedStyleDescription, specific=diagram_style_NodeStyleDescription)
gen_diagram_style_NodeStyleDescription_style_LabelStyleDescription = Generalization(general=style_LabelStyleDescription, specific=diagram_style_NodeStyleDescription)
gen_diagram_style_NodeStyleDescription_style_TooltipStyleDescription = Generalization(general=style_TooltipStyleDescription, specific=diagram_style_NodeStyleDescription)
gen_diagram_style_NodeStyleDescription_style_HideLabelCapabilityStyleDescription = Generalization(general=style_HideLabelCapabilityStyleDescription, specific=diagram_style_NodeStyleDescription)
gen_diagram_style_CustomStyleDescription_NodeStyleDescription = Generalization(general=NodeStyleDescription, specific=diagram_style_CustomStyleDescription)
gen_diagram_description_AdditionalLayer_Layer = Generalization(general=Layer, specific=diagram_description_AdditionalLayer)
gen_diagram_style_BorderedStyleDescription_StyleDescription = Generalization(general=StyleDescription, specific=diagram_style_BorderedStyleDescription)
gen_diagram_style_BundledImageDescription_NodeStyleDescription = Generalization(general=NodeStyleDescription, specific=diagram_style_BundledImageDescription)
gen_diagram_style_SquareDescription_NodeStyleDescription = Generalization(general=NodeStyleDescription, specific=diagram_style_SquareDescription)
gen_diagram_style_LozengeNodeDescription_NodeStyleDescription = Generalization(general=NodeStyleDescription, specific=diagram_style_LozengeNodeDescription)
gen_diagram_style_EllipseNodeDescription_NodeStyleDescription = Generalization(general=NodeStyleDescription, specific=diagram_style_EllipseNodeDescription)
gen_diagram_style_NoteDescription_NodeStyleDescription = Generalization(general=NodeStyleDescription, specific=diagram_style_NoteDescription)
gen_diagram_style_DotDescription_NodeStyleDescription = Generalization(general=NodeStyleDescription, specific=diagram_style_DotDescription)
gen_diagram_style_GaugeCompositeStyleDescription_NodeStyleDescription = Generalization(general=NodeStyleDescription, specific=diagram_style_GaugeCompositeStyleDescription)
gen_diagram_style_ShapeContainerStyleDescription_style_ContainerStyleDescription = Generalization(general=style_ContainerStyleDescription, specific=diagram_style_ShapeContainerStyleDescription)
gen_diagram_style_ShapeContainerStyleDescription_style_SizeComputationContainerStyleDescription = Generalization(general=style_SizeComputationContainerStyleDescription, specific=diagram_style_ShapeContainerStyleDescription)
gen_diagram_style_WorkspaceImageDescription_style_NodeStyleDescription = Generalization(general=style_NodeStyleDescription, specific=diagram_style_WorkspaceImageDescription)
gen_diagram_style_WorkspaceImageDescription_style_ContainerStyleDescription = Generalization(general=style_ContainerStyleDescription, specific=diagram_style_WorkspaceImageDescription)
gen_diagram_style_RoundedCornerStyleDescription_StyleDescription = Generalization(general=StyleDescription, specific=diagram_style_RoundedCornerStyleDescription)
gen_diagram_style_ContainerStyleDescription_style_RoundedCornerStyleDescription = Generalization(general=style_RoundedCornerStyleDescription, specific=diagram_style_ContainerStyleDescription)
gen_diagram_style_ContainerStyleDescription_style_BorderedStyleDescription = Generalization(general=style_BorderedStyleDescription, specific=diagram_style_ContainerStyleDescription)
gen_diagram_style_ContainerStyleDescription_style_LabelStyleDescription = Generalization(general=style_LabelStyleDescription, specific=diagram_style_ContainerStyleDescription)
gen_diagram_style_ContainerStyleDescription_style_TooltipStyleDescription = Generalization(general=style_TooltipStyleDescription, specific=diagram_style_ContainerStyleDescription)
gen_diagram_style_ContainerStyleDescription_style_HideLabelCapabilityStyleDescription = Generalization(general=style_HideLabelCapabilityStyleDescription, specific=diagram_style_ContainerStyleDescription)
gen_diagram_style_FlatContainerStyleDescription_style_ContainerStyleDescription = Generalization(general=style_ContainerStyleDescription, specific=diagram_style_FlatContainerStyleDescription)
gen_diagram_style_FlatContainerStyleDescription_style_SizeComputationContainerStyleDescription = Generalization(general=style_SizeComputationContainerStyleDescription, specific=diagram_style_FlatContainerStyleDescription)
gen_diagram_style_EdgeStyleDescription_StyleDescription = Generalization(general=StyleDescription, specific=diagram_style_EdgeStyleDescription)
gen_diagram_tool_ToolGroup_ToolEntry = Generalization(general=ToolEntry, specific=diagram_tool_ToolGroup)
gen_diagram_style_BeginLabelStyleDescription_BasicLabelStyleDescription = Generalization(general=BasicLabelStyleDescription, specific=diagram_style_BeginLabelStyleDescription)
gen_diagram_style_CenterLabelStyleDescription_BasicLabelStyleDescription = Generalization(general=BasicLabelStyleDescription, specific=diagram_style_CenterLabelStyleDescription)
gen_diagram_style_EndLabelStyleDescription_BasicLabelStyleDescription = Generalization(general=BasicLabelStyleDescription, specific=diagram_style_EndLabelStyleDescription)
gen_diagram_style_BracketEdgeStyleDescription_EdgeStyleDescription = Generalization(general=EdgeStyleDescription, specific=diagram_style_BracketEdgeStyleDescription)
gen_diagram_tool_ToolSection_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=diagram_tool_ToolSection)
gen_diagram_tool_ToolSection_description_IdentifiedElement = Generalization(general=description_IdentifiedElement, specific=diagram_tool_ToolSection)
gen_diagram_tool_NodeCreationDescription_MappingBasedToolDescription = Generalization(general=MappingBasedToolDescription, specific=diagram_tool_NodeCreationDescription)
gen_diagram_tool_EdgeCreationDescription_MappingBasedToolDescription = Generalization(general=MappingBasedToolDescription, specific=diagram_tool_EdgeCreationDescription)
gen_diagram_tool_DeleteElementDescription_MappingBasedToolDescription = Generalization(general=MappingBasedToolDescription, specific=diagram_tool_DeleteElementDescription)
gen_diagram_tool_ContainerCreationDescription_MappingBasedToolDescription = Generalization(general=MappingBasedToolDescription, specific=diagram_tool_ContainerCreationDescription)
gen_diagram_tool_ReconnectEdgeDescription_MappingBasedToolDescription = Generalization(general=MappingBasedToolDescription, specific=diagram_tool_ReconnectEdgeDescription)
gen_diagram_tool_DoubleClickDescription_MappingBasedToolDescription = Generalization(general=MappingBasedToolDescription, specific=diagram_tool_DoubleClickDescription)
gen_diagram_tool_RequestDescription_AbstractToolDescription = Generalization(general=AbstractToolDescription, specific=diagram_tool_RequestDescription)
gen_diagram_tool_DirectEditLabel_MappingBasedToolDescription = Generalization(general=MappingBasedToolDescription, specific=diagram_tool_DirectEditLabel)
gen_diagram_tool_BehaviorTool_AbstractToolDescription = Generalization(general=AbstractToolDescription, specific=diagram_tool_BehaviorTool)
gen_diagram_tool_CreateEdgeView_CreateView = Generalization(general=CreateView, specific=diagram_tool_CreateEdgeView)
gen_diagram_tool_Navigation_ContainerModelOperation = Generalization(general=ContainerModelOperation, specific=diagram_tool_Navigation)
gen_diagram_tool_DiagramCreationDescription_RepresentationCreationDescription = Generalization(general=RepresentationCreationDescription, specific=diagram_tool_DiagramCreationDescription)
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
gen_diagram_filter_FilterDescription_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=diagram_filter_FilterDescription)
gen_diagram_filter_FilterDescription_description_IdentifiedElement = Generalization(general=description_IdentifiedElement, specific=diagram_filter_FilterDescription)
gen_diagram_tool_DiagramNavigationDescription_RepresentationNavigationDescription = Generalization(general=RepresentationNavigationDescription, specific=diagram_tool_DiagramNavigationDescription)
gen_diagram_tool_ContainerDropDescription_MappingBasedToolDescription = Generalization(general=MappingBasedToolDescription, specific=diagram_tool_ContainerDropDescription)
gen_diagram_filter_CompositeFilterDescription_FilterDescription = Generalization(general=FilterDescription, specific=diagram_filter_CompositeFilterDescription)
gen_diagram_filter_VariableFilter_Filter = Generalization(general=Filter, specific=diagram_filter_VariableFilter)
gen_diagram_concern_ConcernSet_DocumentedElement = Generalization(general=DocumentedElement, specific=diagram_concern_ConcernSet)
gen_diagram_concern_ConcernDescription_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=diagram_concern_ConcernDescription)
gen_diagram_concern_ConcernDescription_description_IdentifiedElement = Generalization(general=description_IdentifiedElement, specific=diagram_concern_ConcernDescription)
gen_diagram_filter_MappingFilter_Filter = Generalization(general=Filter, specific=diagram_filter_MappingFilter)

# Domain Model
domain_model = DomainModel(
    name="diagram",
    types={diagram_DEdge, diagram_DNode, diagram_DDiagram, DRepresentation, description_DocumentedElement, DragAndDropTarget, diagram_DDiagramElement, DiagramDescription, diagram_DNodeListElement, diagram_DDiagramElementContainer, concern_ConcernDescription, filter_FilterDescription, validation_ValidationRule, tool_BehaviorTool, diagram_FilterVariableHistory, Layer, diagram_AbsoluteBoundsFilter, diagram_DSemanticDiagram, DDiagram, DSemanticDecorator, DRepresentationElement, diagram_Decoration, DiagramElementMapping, diagram_GraphicalFilter, diagram_HideFilter, GraphicalFilter, diagram_HideLabelFilter, diagram_FoldingPointFilter, diagram_FoldingFilter, diagram_AppliedCompositeFilters, filter_CompositeFilterDescription, diagram_AbstractDNode, DDiagramElement, AbstractDNode, EdgeTarget, diagram_NodeStyle, diagram_Style, NodeMapping, diagram_DNodeList, diagram_ContainerStyle, ContainerMapping, diagram_DNodeContainer, DDiagramElementContainer, IEdgeMapping, diagram_EdgeStyle, diagram_EdgeTarget, diagram_GaugeSection, Customizable, LabelStyle, Style, BorderedStyle, HideLabelCapabilityStyle, diagram_Dot, NodeStyle, diagram_Square, diagram_FlatContainerStyle, ContainerStyle, diagram_ShapeContainerStyle, diagram_Ellipse, diagram_Lozenge, diagram_BundledImage, diagram_WorkspaceImage, diagram_CustomStyle, diagram_BeginLabelStyle, diagram_CenterLabelStyle, diagram_EndLabelStyle, diagram_Note, diagram_GaugeCompositeStyle, diagram_BorderedStyle, diagram_HideLabelCapabilityStyle, diagram_VariableValue, diagram_TypedVariableValue, VariableValue, TypedVariable, diagram_EObjectVariableValue, tool_SelectModelElementVariable, diagram_CollapseFilter, diagram_EObject, diagram_description_DiagramDescription, description_DragAndDropTargetDescription, diagram_IndirectlyCollapseFilter, description_RepresentationDescription, CollapseFilter, description_PasteTargetDescription, BasicLabelStyle, diagram_BracketEdgeStyle, EdgeStyle, diagram_ComputedStyleDescriptionRegistry, style_StyleDescription, diagram_DragAndDropTarget, validation_ValidationSet, concern_ConcernSet, tool_AbstractToolDescription, EdgeMapping, tool_RepresentationCreationDescription, Layout, tool_InitialOperation, diagram_description_DiagramImportDescription, AdditionalLayer, EdgeMappingImport, tool_ToolSection, tool_DeleteElementDescription, description_RepresentationImportDescription, description_DiagramDescription, diagram_description_DiagramExtensionDescription, RepresentationExtensionDescription, diagram_description_DiagramElementMapping, description_RepresentationElementMapping, diagram_description_NodeMapping, description_AbstractNodeMapping, tool_DirectEditLabel, tool_DoubleClickDescription, diagram_description_AbstractNodeMapping, description_DiagramElementMapping, diagram_description_ContainerMapping, style_NodeStyleDescription, ConditionalNodeStyleDescription, diagram_description_EdgeMapping, description_IEdgeMapping, style_ContainerStyleDescription, ConditionalContainerStyleDescription, diagram_description_NodeMappingImport, description_NodeMapping, description_AbstractMappingImport, diagram_description_ContainerMappingImport, description_ContainerMapping, ConditionalEdgeStyleDescription, diagram_description_OrderedTreeLayout, style_EdgeStyleDescription, tool_ReconnectEdgeDescription, AbstractNodeMapping, diagram_description_IEdgeMapping, diagram_description_EdgeMappingImport, description_IdentifiedElement, diagram_description_ConditionalNodeStyleDescription, ConditionalStyleDescription, diagram_description_ConditionalEdgeStyleDescription, diagram_description_ConditionalContainerStyleDescription, diagram_description_Layout, DocumentedElement, DecorationDescriptionsSet, diagram_description_CompositeLayout, diagram_description_MappingBasedDecoration, DecorationDescription, diagram_description_Layer, description_EndUserDocumentedElement, diagram_style_NodeStyleDescription, style_BorderedStyleDescription, style_LabelStyleDescription, style_TooltipStyleDescription, style_HideLabelCapabilityStyleDescription, Customization, diagram_style_CustomStyleDescription, NodeStyleDescription, diagram_description_AdditionalLayer, diagram_description_DragAndDropTargetDescription, tool_ContainerDropDescription, diagram_style_BorderedStyleDescription, StyleDescription, ColorDescription, diagram_style_BundledImageDescription, diagram_style_SquareDescription, diagram_style_LozengeNodeDescription, diagram_style_EllipseNodeDescription, diagram_style_NoteDescription, diagram_style_DotDescription, diagram_style_GaugeCompositeStyleDescription, style_GaugeSectionDescription, diagram_style_GaugeSectionDescription, style_LabelBorderStyleDescription, diagram_style_ShapeContainerStyleDescription, diagram_style_WorkspaceImageDescription, diagram_style_SizeComputationContainerStyleDescription, diagram_style_RoundedCornerStyleDescription, diagram_style_ContainerStyleDescription, style_RoundedCornerStyleDescription, diagram_style_FlatContainerStyleDescription, style_SizeComputationContainerStyleDescription, style_BeginLabelStyleDescription, style_CenterLabelStyleDescription, style_EndLabelStyleDescription, diagram_style_BeginLabelStyleDescription, BasicLabelStyleDescription, diagram_style_EdgeStyleDescription, tool_PopupMenu, tool_ToolGroupExtension, diagram_tool_ToolGroup, ToolEntry, diagram_tool_ToolGroupExtension, tool_ToolGroup, diagram_style_CenterLabelStyleDescription, diagram_style_EndLabelStyleDescription, diagram_style_BracketEdgeStyleDescription, EdgeStyleDescription, diagram_style_HideLabelCapabilityStyleDescription, diagram_tool_ToolSection, tool_ToolEntry, tool_InitialNodeCreationOperation, diagram_tool_NodeCreationDescription, MappingBasedToolDescription, tool_NodeCreationVariable, tool_ContainerViewVariable, tool_TargetEdgeCreationVariable, tool_SourceEdgeViewCreationVariable, tool_TargetEdgeViewCreationVariable, tool_InitEdgeCreationOperation, diagram_tool_EdgeCreationDescription, tool_SourceEdgeCreationVariable, diagram_tool_DeleteElementDescription, tool_ElementDeleteVariable, diagram_tool_ContainerCreationDescription, tool_DeleteHookParameter, diagram_tool_DeleteHookParameter, diagram_tool_ReconnectEdgeDescription, tool_DeleteHook, diagram_tool_DoubleClickDescription, tool_ElementDoubleClickVariable, diagram_tool_DeleteHook, AbstractToolDescription, diagram_tool_DirectEditLabel, tool_EditMaskVariables, diagram_tool_BehaviorTool, tool_ElementSelectVariable, diagram_tool_RequestDescription, diagram_tool_CreateEdgeView, CreateView, diagram_tool_Navigation, diagram_tool_DiagramCreationDescription, RepresentationCreationDescription, diagram_tool_SourceEdgeCreationVariable, description_AbstractVariable, tool_VariableContainer, diagram_tool_SourceEdgeViewCreationVariable, diagram_tool_TargetEdgeCreationVariable, diagram_tool_TargetEdgeViewCreationVariable, diagram_tool_ElementDoubleClickVariable, diagram_tool_NodeCreationVariable, diagram_tool_CreateView, ContainerModelOperation, tool_ElementDropVariable, tool_InitialContainerDropOperation, diagram_filter_FilterDescription, diagram_tool_DiagramNavigationDescription, RepresentationNavigationDescription, diagram_tool_ContainerDropDescription, tool_DropContainerVariable, diagram_filter_CompositeFilterDescription, FilterDescription, filter_Filter, diagram_filter_VariableFilter, InteractiveVariableDescription, diagram_concern_ConcernSet, diagram_filter_Filter, diagram_concern_ConcernDescription, diagram_filter_MappingFilter, Filter, ContainerLayout, LabelPosition, ContainerShape, BackgroundStyle, BundledImageShape, LineStyle, EdgeArrows, EdgeRouting, AlignmentKind, ResizeKind, ArrangeConstraint, FoldingStyle, LayoutDirection, CenteringStyle, Side, ReconnectionKind, FilterKind},
    associations={edges6, nodes8, ownedDiagramElements0, diagramElements1, description4, hiddenElements29, nodeListElements10, containers12, currentConcern14, activatedFilters16, allFilters18, activatedRules21, activateBehaviors23, filterVariableHistory25, activatedLayers27, compositeFilterDescriptions41, parentLayers32, decorations35, diagramElementMapping37, graphicalFilters39, ownedBorderedNodes42, ownedStyle44, originalStyle46, actualMapping48, candidatesMapping50, nodes53, containers57, elements59, ownedStyle62, originalStyle64, actualMapping67, candidatesMapping69, ownedDiagramElements72, targetNode91, actualMapping93, ownedElements74, ownedStyle76, originalStyle79, actualMapping82, candidatesMapping85, ownedStyle88, sourceNode90, originalStyle95, path98, outgoingEdges100, incomingEdges101, beginLabelStyle103, centerLabelStyle105, endLabelStyle107, sections109, ownedValues110, variableDefinition113, variableDefinition114, modelElement115, filters117, computedStyleDescriptions112, validationSet127, concerns129, allTools131, allEdgeMappings119, allNodeMappings121, allContainerMappings124, init136, reusedTools169, layout138, diagramInitialisation140, defaultLayer142, defaultConcern133, additionalLayers145, allLayers147, allActivatedTools150, nodeMappings153, edgeMappings156, edgeMappingImports159, containerMappings161, reusedMappings164, toolSection167, deletionDescription182, importedDiagram172, layers174, validationSet176, concerns179, reusedBorderedNodeMappings188, labelDirectEdit183, doubleClickDescription185, borderedNodeMappings186, style191, conditionnalStyles192, subNodeMappings194, allNodeMappings196, reusedNodeMappings199, subContainerMappings202, reusedContainerMappings205, allContainerMappings208, style211, conditionnalStyles213, importedMapping215, importedMapping217, conditionnalStyles226, sourceMapping219, targetMapping221, style224, nodeMapping243, reconnections228, pathNodeMapping230, importedMapping232, conditionnalStyles234, style237, style239, style241, reusedTools267, decorationDescriptionsSet270, allEdgeMappings272, mappings245, nodeMappings247, edgeMappings249, edgeMappingImports252, containerMappings255, reusedMappings258, allTools261, toolSections264, customization275, dropDescriptions277, borderColor278, color283, color279, color281, backgroundColor292, foregroundColor294, color285, color287, backgroundColor289, sections291, foregroundColor299, labelBorderStyle302, backgroundColor304, backgroundColor297, beginLabelStyleDescription308, centerLabelStyleDescription310, endLabelStyleDescription312, centeredSourceMappings314, centeredTargetMappings317, strokeColor306, popupMenus324, reusedTools326, groupExtensions329, tools331, group333, ownedTools320, subSections321, viewVariable341, initialOperation343, extraMappings345, tools334, nodeMappings337, variable339, targetVariable352, sourceViewVariable354, targetViewVariable356, initialOperation358, edgeMappings348, sourceVariable350, initialOperation374, extraMappings377, element380, elementView381, containerView384, extraSourceMappings360, extraTargetMappings363, containerMappings366, variable368, viewVariable371, parameters402, source403, initialOperation387, hook390, mappings392, element395, elementView396, initialOperation399, mask422, initialOperation423, target405, sourceView408, targetView411, element414, initialOperation416, edgeView419, diagramDescription430, initialOperation426, mapping428, element443, newViewContainer445, initialOperation448, diagramDescription432, diagramDescription434, mappings436, oldContainer438, newContainer440, filters452, ownedVariables453, ownedConcernDescriptions454, filters456, rules458, mappings450, behaviors461},
    generalizations={gen_diagram_DDiagram_DRepresentation, gen_diagram_DDiagram_description_DocumentedElement, gen_diagram_DDiagram_DragAndDropTarget, gen_diagram_AbsoluteBoundsFilter_GraphicalFilter, gen_diagram_DSemanticDiagram_DDiagram, gen_diagram_DSemanticDiagram_DSemanticDecorator, gen_diagram_DDiagramElement_DRepresentationElement, gen_diagram_HideFilter_GraphicalFilter, gen_diagram_HideLabelFilter_GraphicalFilter, gen_diagram_FoldingPointFilter_GraphicalFilter, gen_diagram_FoldingFilter_GraphicalFilter, gen_diagram_AppliedCompositeFilters_GraphicalFilter, gen_diagram_AbstractDNode_DDiagramElement, gen_diagram_DNode_AbstractDNode, gen_diagram_DNode_EdgeTarget, gen_diagram_DNode_DragAndDropTarget, gen_diagram_DDiagramElementContainer_AbstractDNode, gen_diagram_DDiagramElementContainer_EdgeTarget, gen_diagram_DDiagramElementContainer_DragAndDropTarget, gen_diagram_DNodeList_DDiagramElementContainer, gen_diagram_DNodeContainer_DDiagramElementContainer, gen_diagram_DNodeListElement_AbstractDNode, gen_diagram_DEdge_DDiagramElement, gen_diagram_DEdge_EdgeTarget, gen_diagram_GaugeSection_Customizable, gen_diagram_NodeStyle_LabelStyle, gen_diagram_NodeStyle_Style, gen_diagram_NodeStyle_BorderedStyle, gen_diagram_NodeStyle_HideLabelCapabilityStyle, gen_diagram_Dot_NodeStyle, gen_diagram_Square_NodeStyle, gen_diagram_ContainerStyle_LabelStyle, gen_diagram_ContainerStyle_Style, gen_diagram_ContainerStyle_BorderedStyle, gen_diagram_ContainerStyle_HideLabelCapabilityStyle, gen_diagram_FlatContainerStyle_ContainerStyle, gen_diagram_ShapeContainerStyle_ContainerStyle, gen_diagram_Ellipse_NodeStyle, gen_diagram_Lozenge_NodeStyle, gen_diagram_BundledImage_NodeStyle, gen_diagram_WorkspaceImage_NodeStyle, gen_diagram_WorkspaceImage_ContainerStyle, gen_diagram_CustomStyle_NodeStyle, gen_diagram_EdgeStyle_Style, gen_diagram_Note_NodeStyle, gen_diagram_GaugeCompositeStyle_NodeStyle, gen_diagram_BorderedStyle_Style, gen_diagram_TypedVariableValue_VariableValue, gen_diagram_EObjectVariableValue_VariableValue, gen_diagram_CollapseFilter_GraphicalFilter, gen_diagram_description_DiagramDescription_description_DragAndDropTargetDescription, gen_diagram_IndirectlyCollapseFilter_CollapseFilter, gen_diagram_description_DiagramDescription_description_RepresentationDescription, gen_diagram_description_DiagramDescription_description_PasteTargetDescription, gen_diagram_BeginLabelStyle_BasicLabelStyle, gen_diagram_CenterLabelStyle_BasicLabelStyle, gen_diagram_EndLabelStyle_BasicLabelStyle, gen_diagram_BracketEdgeStyle_EdgeStyle, gen_diagram_description_DiagramImportDescription_description_RepresentationImportDescription, gen_diagram_description_DiagramImportDescription_description_DiagramDescription, gen_diagram_description_DiagramExtensionDescription_RepresentationExtensionDescription, gen_diagram_description_DiagramElementMapping_description_RepresentationElementMapping, gen_diagram_description_DiagramElementMapping_description_PasteTargetDescription, gen_diagram_description_NodeMapping_description_AbstractNodeMapping, gen_diagram_description_NodeMapping_description_DragAndDropTargetDescription, gen_diagram_description_AbstractNodeMapping_description_DiagramElementMapping, gen_diagram_description_AbstractNodeMapping_description_DocumentedElement, gen_diagram_description_ContainerMapping_description_AbstractNodeMapping, gen_diagram_description_ContainerMapping_description_DragAndDropTargetDescription, gen_diagram_description_EdgeMapping_description_DiagramElementMapping, gen_diagram_description_EdgeMapping_description_DocumentedElement, gen_diagram_description_EdgeMapping_description_IEdgeMapping, gen_diagram_description_NodeMappingImport_description_NodeMapping, gen_diagram_description_NodeMappingImport_description_AbstractMappingImport, gen_diagram_description_ContainerMappingImport_description_ContainerMapping, gen_diagram_description_ContainerMappingImport_description_AbstractMappingImport, gen_diagram_description_OrderedTreeLayout_Layout, gen_diagram_description_EdgeMappingImport_description_DocumentedElement, gen_diagram_description_EdgeMappingImport_description_IEdgeMapping, gen_diagram_description_EdgeMappingImport_description_IdentifiedElement, gen_diagram_description_ConditionalNodeStyleDescription_ConditionalStyleDescription, gen_diagram_description_ConditionalEdgeStyleDescription_ConditionalStyleDescription, gen_diagram_description_ConditionalContainerStyleDescription_ConditionalStyleDescription, gen_diagram_description_Layout_DocumentedElement, gen_diagram_description_CompositeLayout_Layout, gen_diagram_description_MappingBasedDecoration_DecorationDescription, gen_diagram_description_Layer_description_DocumentedElement, gen_diagram_description_Layer_description_EndUserDocumentedElement, gen_diagram_description_Layer_description_IdentifiedElement, gen_diagram_style_NodeStyleDescription_style_StyleDescription, gen_diagram_style_NodeStyleDescription_style_BorderedStyleDescription, gen_diagram_style_NodeStyleDescription_style_LabelStyleDescription, gen_diagram_style_NodeStyleDescription_style_TooltipStyleDescription, gen_diagram_style_NodeStyleDescription_style_HideLabelCapabilityStyleDescription, gen_diagram_style_CustomStyleDescription_NodeStyleDescription, gen_diagram_description_AdditionalLayer_Layer, gen_diagram_style_BorderedStyleDescription_StyleDescription, gen_diagram_style_BundledImageDescription_NodeStyleDescription, gen_diagram_style_SquareDescription_NodeStyleDescription, gen_diagram_style_LozengeNodeDescription_NodeStyleDescription, gen_diagram_style_EllipseNodeDescription_NodeStyleDescription, gen_diagram_style_NoteDescription_NodeStyleDescription, gen_diagram_style_DotDescription_NodeStyleDescription, gen_diagram_style_GaugeCompositeStyleDescription_NodeStyleDescription, gen_diagram_style_ShapeContainerStyleDescription_style_ContainerStyleDescription, gen_diagram_style_ShapeContainerStyleDescription_style_SizeComputationContainerStyleDescription, gen_diagram_style_WorkspaceImageDescription_style_NodeStyleDescription, gen_diagram_style_WorkspaceImageDescription_style_ContainerStyleDescription, gen_diagram_style_RoundedCornerStyleDescription_StyleDescription, gen_diagram_style_ContainerStyleDescription_style_RoundedCornerStyleDescription, gen_diagram_style_ContainerStyleDescription_style_BorderedStyleDescription, gen_diagram_style_ContainerStyleDescription_style_LabelStyleDescription, gen_diagram_style_ContainerStyleDescription_style_TooltipStyleDescription, gen_diagram_style_ContainerStyleDescription_style_HideLabelCapabilityStyleDescription, gen_diagram_style_FlatContainerStyleDescription_style_ContainerStyleDescription, gen_diagram_style_FlatContainerStyleDescription_style_SizeComputationContainerStyleDescription, gen_diagram_style_EdgeStyleDescription_StyleDescription, gen_diagram_tool_ToolGroup_ToolEntry, gen_diagram_style_BeginLabelStyleDescription_BasicLabelStyleDescription, gen_diagram_style_CenterLabelStyleDescription_BasicLabelStyleDescription, gen_diagram_style_EndLabelStyleDescription_BasicLabelStyleDescription, gen_diagram_style_BracketEdgeStyleDescription_EdgeStyleDescription, gen_diagram_tool_ToolSection_description_DocumentedElement, gen_diagram_tool_ToolSection_description_IdentifiedElement, gen_diagram_tool_NodeCreationDescription_MappingBasedToolDescription, gen_diagram_tool_EdgeCreationDescription_MappingBasedToolDescription, gen_diagram_tool_DeleteElementDescription_MappingBasedToolDescription, gen_diagram_tool_ContainerCreationDescription_MappingBasedToolDescription, gen_diagram_tool_ReconnectEdgeDescription_MappingBasedToolDescription, gen_diagram_tool_DoubleClickDescription_MappingBasedToolDescription, gen_diagram_tool_RequestDescription_AbstractToolDescription, gen_diagram_tool_DirectEditLabel_MappingBasedToolDescription, gen_diagram_tool_BehaviorTool_AbstractToolDescription, gen_diagram_tool_CreateEdgeView_CreateView, gen_diagram_tool_Navigation_ContainerModelOperation, gen_diagram_tool_DiagramCreationDescription_RepresentationCreationDescription, gen_diagram_tool_SourceEdgeCreationVariable_description_AbstractVariable, gen_diagram_tool_SourceEdgeCreationVariable_tool_VariableContainer, gen_diagram_tool_SourceEdgeViewCreationVariable_description_AbstractVariable, gen_diagram_tool_SourceEdgeViewCreationVariable_tool_VariableContainer, gen_diagram_tool_TargetEdgeCreationVariable_description_AbstractVariable, gen_diagram_tool_TargetEdgeCreationVariable_tool_VariableContainer, gen_diagram_tool_TargetEdgeViewCreationVariable_description_AbstractVariable, gen_diagram_tool_TargetEdgeViewCreationVariable_tool_VariableContainer, gen_diagram_tool_ElementDoubleClickVariable_description_AbstractVariable, gen_diagram_tool_ElementDoubleClickVariable_tool_VariableContainer, gen_diagram_tool_NodeCreationVariable_description_AbstractVariable, gen_diagram_tool_NodeCreationVariable_tool_VariableContainer, gen_diagram_tool_CreateView_ContainerModelOperation, gen_diagram_filter_FilterDescription_description_DocumentedElement, gen_diagram_filter_FilterDescription_description_IdentifiedElement, gen_diagram_tool_DiagramNavigationDescription_RepresentationNavigationDescription, gen_diagram_tool_ContainerDropDescription_MappingBasedToolDescription, gen_diagram_filter_CompositeFilterDescription_FilterDescription, gen_diagram_filter_VariableFilter_Filter, gen_diagram_concern_ConcernSet_DocumentedElement, gen_diagram_concern_ConcernDescription_description_DocumentedElement, gen_diagram_concern_ConcernDescription_description_IdentifiedElement, gen_diagram_filter_MappingFilter_Filter},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)