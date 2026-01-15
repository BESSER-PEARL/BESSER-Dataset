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
            EnumerationLiteral(name="Liquid"),
			EnumerationLiteral(name="GradientTopToBottom"),
			EnumerationLiteral(name="GradientLeftToRight")
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
			EnumerationLiteral(name="OutputClosedArrow"),
			EnumerationLiteral(name="InputClosedArrow"),
			EnumerationLiteral(name="OutputFillClosedArrow"),
			EnumerationLiteral(name="InputFillClosedArrow"),
			EnumerationLiteral(name="Diamond"),
			EnumerationLiteral(name="OutputArrow"),
			EnumerationLiteral(name="FillDiamond"),
			EnumerationLiteral(name="InputArrow"),
			EnumerationLiteral(name="InputArrowWithDiamond"),
			EnumerationLiteral(name="InputArrowWithFillDiamond")
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

EdgeRouting: Enumeration = Enumeration(
    name="EdgeRouting",
    literals={
            EnumerationLiteral(name="straight"),
			EnumerationLiteral(name="manhattan"),
			EnumerationLiteral(name="tree")
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
            EnumerationLiteral(name="LeftToRight"),
			EnumerationLiteral(name="BottomToTop"),
			EnumerationLiteral(name="TopToBottom")
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
diagram_DDiagram = Class(name="diagram::DDiagram")
DRepresentation = Class(name="DRepresentation")
description_DocumentedElement = Class(name="description::DocumentedElement")
DragAndDropTarget = Class(name="DragAndDropTarget")
diagram_DDiagramElement = Class(name="diagram::DDiagramElement", is_abstract=True)
DiagramDescription = Class(name="DiagramDescription")
diagram_DEdge = Class(name="diagram::DEdge")
diagram_DNode = Class(name="diagram::DNode")
diagram_DNodeListElement = Class(name="diagram::DNodeListElement")
tool_BehaviorTool = Class(name="tool::BehaviorTool")
diagram_DDiagramElementContainer = Class(name="diagram::DDiagramElementContainer", is_abstract=True)
concern_ConcernDescription = Class(name="concern::ConcernDescription")
filter_FilterDescription = Class(name="filter::FilterDescription")
AdditionalLayer = Class(name="AdditionalLayer")
validation_ValidationRule = Class(name="validation::ValidationRule")
diagram_FilterVariableHistory = Class(name="diagram::FilterVariableHistory")
Layer = Class(name="Layer")
diagram_DSemanticDiagram = Class(name="diagram::DSemanticDiagram")
DDiagram = Class(name="DDiagram")
DSemanticDecorator = Class(name="DSemanticDecorator")
DRepresentationElement = Class(name="DRepresentationElement")
diagram_FoldingPointFilter = Class(name="diagram::FoldingPointFilter")
diagram_FoldingFilter = Class(name="diagram::FoldingFilter")
diagram_Decoration = Class(name="diagram::Decoration")
DiagramElementMapping = Class(name="DiagramElementMapping")
diagram_GraphicalFilter = Class(name="diagram::GraphicalFilter", is_abstract=True)
diagram_HideFilter = Class(name="diagram::HideFilter")
GraphicalFilter = Class(name="GraphicalFilter")
diagram_HideLabelFilter = Class(name="diagram::HideLabelFilter")
EdgeTarget = Class(name="EdgeTarget")
diagram_AppliedCompositeFilters = Class(name="diagram::AppliedCompositeFilters")
filter_CompositeFilterDescription = Class(name="filter::CompositeFilterDescription")
diagram_AbsoluteBoundsFilter = Class(name="diagram::AbsoluteBoundsFilter")
diagram_AbstractDNode = Class(name="diagram::AbstractDNode", is_abstract=True)
DDiagramElement = Class(name="DDiagramElement")
AbstractDNode = Class(name="AbstractDNode")
diagram_NodeStyle = Class(name="diagram::NodeStyle", is_abstract=True)
diagram_Style = Class(name="diagram::Style")
NodeMapping = Class(name="NodeMapping")
diagram_ContainerStyle = Class(name="diagram::ContainerStyle", is_abstract=True)
diagram_DNodeList = Class(name="diagram::DNodeList")
ContainerMapping = Class(name="ContainerMapping")
diagram_DNodeContainer = Class(name="diagram::DNodeContainer")
DDiagramElementContainer = Class(name="DDiagramElementContainer")
diagram_EdgeStyle = Class(name="diagram::EdgeStyle")
diagram_EdgeTarget = Class(name="diagram::EdgeTarget", is_abstract=True)
IEdgeMapping = Class(name="IEdgeMapping")
diagram_Dot = Class(name="diagram::Dot")
LabelStyle = Class(name="LabelStyle")
Style = Class(name="Style")
BorderedStyle = Class(name="BorderedStyle")
HideLabelCapabilityStyle = Class(name="HideLabelCapabilityStyle")
NodeStyle = Class(name="NodeStyle")
diagram_FlatContainerStyle = Class(name="diagram::FlatContainerStyle")
ContainerStyle = Class(name="ContainerStyle")
diagram_GaugeSection = Class(name="diagram::GaugeSection")
Customizable = Class(name="Customizable")
diagram_ShapeContainerStyle = Class(name="diagram::ShapeContainerStyle")
diagram_Square = Class(name="diagram::Square")
diagram_Ellipse = Class(name="diagram::Ellipse")
diagram_Lozenge = Class(name="diagram::Lozenge")
diagram_BundledImage = Class(name="diagram::BundledImage")
diagram_WorkspaceImage = Class(name="diagram::WorkspaceImage")
diagram_CustomStyle = Class(name="diagram::CustomStyle")
diagram_BeginLabelStyle = Class(name="diagram::BeginLabelStyle")
diagram_CenterLabelStyle = Class(name="diagram::CenterLabelStyle")
diagram_EndLabelStyle = Class(name="diagram::EndLabelStyle")
diagram_BorderedStyle = Class(name="diagram::BorderedStyle")
diagram_GaugeCompositeStyle = Class(name="diagram::GaugeCompositeStyle")
diagram_CollapseFilter = Class(name="diagram::CollapseFilter")
diagram_Note = Class(name="diagram::Note")
diagram_VariableValue = Class(name="diagram::VariableValue", is_abstract=True)
diagram_BracketEdgeStyle = Class(name="diagram::BracketEdgeStyle")
EdgeStyle = Class(name="EdgeStyle")
diagram_ComputedStyleDescriptionRegistry = Class(name="diagram::ComputedStyleDescriptionRegistry")
style_StyleDescription = Class(name="style::StyleDescription")
diagram_DragAndDropTarget = Class(name="diagram::DragAndDropTarget")
diagram_IndirectlyCollapseFilter = Class(name="diagram::IndirectlyCollapseFilter")
CollapseFilter = Class(name="CollapseFilter")
BasicLabelStyle = Class(name="BasicLabelStyle")
tool_SelectModelElementVariable = Class(name="tool::SelectModelElementVariable")
diagram_EObject = Class(name="diagram::EObject")
diagram_description_DiagramDescription = Class(name="diagram::description::DiagramDescription")
description_DragAndDropTargetDescription = Class(name="description::DragAndDropTargetDescription")
description_RepresentationDescription = Class(name="description::RepresentationDescription")
description_PasteTargetDescription = Class(name="description::PasteTargetDescription")
diagram_HideLabelCapabilityStyle = Class(name="diagram::HideLabelCapabilityStyle", is_abstract=True)
diagram_TypedVariableValue = Class(name="diagram::TypedVariableValue")
VariableValue = Class(name="VariableValue")
TypedVariable = Class(name="TypedVariable")
diagram_EObjectVariableValue = Class(name="diagram::EObjectVariableValue")
validation_ValidationSet = Class(name="validation::ValidationSet")
concern_ConcernSet = Class(name="concern::ConcernSet")
tool_AbstractToolDescription = Class(name="tool::AbstractToolDescription")
EdgeMapping = Class(name="EdgeMapping")
tool_RepresentationCreationDescription = Class(name="tool::RepresentationCreationDescription")
Layout = Class(name="Layout")
tool_InitialOperation = Class(name="tool::InitialOperation")
EdgeMappingImport = Class(name="EdgeMappingImport")
diagram_description_DiagramImportDescription = Class(name="diagram::description::DiagramImportDescription")
description_RepresentationImportDescription = Class(name="description::RepresentationImportDescription")
description_DiagramDescription = Class(name="description::DiagramDescription")
diagram_description_DiagramExtensionDescription = Class(name="diagram::description::DiagramExtensionDescription")
RepresentationExtensionDescription = Class(name="RepresentationExtensionDescription")
tool_ToolSection = Class(name="tool::ToolSection")
diagram_description_DiagramElementMapping = Class(name="diagram::description::DiagramElementMapping", is_abstract=True)
description_RepresentationElementMapping = Class(name="description::RepresentationElementMapping")
tool_DeleteElementDescription = Class(name="tool::DeleteElementDescription")
tool_DirectEditLabel = Class(name="tool::DirectEditLabel")
tool_DoubleClickDescription = Class(name="tool::DoubleClickDescription")
diagram_description_AbstractNodeMapping = Class(name="diagram::description::AbstractNodeMapping", is_abstract=True)
description_DiagramElementMapping = Class(name="description::DiagramElementMapping")
diagram_description_NodeMapping = Class(name="diagram::description::NodeMapping")
description_AbstractNodeMapping = Class(name="description::AbstractNodeMapping")
style_NodeStyleDescription = Class(name="style::NodeStyleDescription")
ConditionalNodeStyleDescription = Class(name="ConditionalNodeStyleDescription")
diagram_description_ContainerMapping = Class(name="diagram::description::ContainerMapping")
style_ContainerStyleDescription = Class(name="style::ContainerStyleDescription")
ConditionalContainerStyleDescription = Class(name="ConditionalContainerStyleDescription")
diagram_description_EdgeMapping = Class(name="diagram::description::EdgeMapping")
description_IEdgeMapping = Class(name="description::IEdgeMapping")
diagram_description_NodeMappingImport = Class(name="diagram::description::NodeMappingImport")
description_NodeMapping = Class(name="description::NodeMapping")
description_AbstractMappingImport = Class(name="description::AbstractMappingImport")
diagram_description_ContainerMappingImport = Class(name="diagram::description::ContainerMappingImport")
description_ContainerMapping = Class(name="description::ContainerMapping")
ConditionalEdgeStyleDescription = Class(name="ConditionalEdgeStyleDescription")
tool_ReconnectEdgeDescription = Class(name="tool::ReconnectEdgeDescription")
style_EdgeStyleDescription = Class(name="style::EdgeStyleDescription")
diagram_description_EdgeMappingImport = Class(name="diagram::description::EdgeMappingImport")
description_IdentifiedElement = Class(name="description::IdentifiedElement")
AbstractNodeMapping = Class(name="AbstractNodeMapping")
diagram_description_IEdgeMapping = Class(name="diagram::description::IEdgeMapping", is_abstract=True)
diagram_description_Layout = Class(name="diagram::description::Layout", is_abstract=True)
DocumentedElement = Class(name="DocumentedElement")
diagram_description_OrderedTreeLayout = Class(name="diagram::description::OrderedTreeLayout")
diagram_description_ConditionalNodeStyleDescription = Class(name="diagram::description::ConditionalNodeStyleDescription")
ConditionalStyleDescription = Class(name="ConditionalStyleDescription")
diagram_description_ConditionalEdgeStyleDescription = Class(name="diagram::description::ConditionalEdgeStyleDescription")
diagram_description_ConditionalContainerStyleDescription = Class(name="diagram::description::ConditionalContainerStyleDescription")
diagram_description_MappingBasedDecoration = Class(name="diagram::description::MappingBasedDecoration")
DecorationDescription = Class(name="DecorationDescription")
diagram_description_Layer = Class(name="diagram::description::Layer")
description_EndUserDocumentedElement = Class(name="description::EndUserDocumentedElement")
diagram_description_CompositeLayout = Class(name="diagram::description::CompositeLayout")
diagram_description_AdditionalLayer = Class(name="diagram::description::AdditionalLayer")
diagram_description_DragAndDropTargetDescription = Class(name="diagram::description::DragAndDropTargetDescription", is_abstract=True)
tool_ContainerDropDescription = Class(name="tool::ContainerDropDescription")
diagram_style_BorderedStyleDescription = Class(name="diagram::style::BorderedStyleDescription")
StyleDescription = Class(name="StyleDescription")
DecorationDescriptionsSet = Class(name="DecorationDescriptionsSet")
Customization = Class(name="Customization")
style_LabelStyleDescription = Class(name="style::LabelStyleDescription")
style_TooltipStyleDescription = Class(name="style::TooltipStyleDescription")
style_HideLabelCapabilityStyleDescription = Class(name="style::HideLabelCapabilityStyleDescription")
ColorDescription = Class(name="ColorDescription")
diagram_style_NodeStyleDescription = Class(name="diagram::style::NodeStyleDescription", is_abstract=True)
style_BorderedStyleDescription = Class(name="style::BorderedStyleDescription")
diagram_style_LozengeNodeDescription = Class(name="diagram::style::LozengeNodeDescription")
diagram_style_CustomStyleDescription = Class(name="diagram::style::CustomStyleDescription")
NodeStyleDescription = Class(name="NodeStyleDescription")
diagram_style_SquareDescription = Class(name="diagram::style::SquareDescription")
diagram_style_BundledImageDescription = Class(name="diagram::style::BundledImageDescription")
diagram_style_NoteDescription = Class(name="diagram::style::NoteDescription")
diagram_style_EllipseNodeDescription = Class(name="diagram::style::EllipseNodeDescription")
diagram_style_GaugeCompositeStyleDescription = Class(name="diagram::style::GaugeCompositeStyleDescription")
style_GaugeSectionDescription = Class(name="style::GaugeSectionDescription")
diagram_style_GaugeSectionDescription = Class(name="diagram::style::GaugeSectionDescription")
diagram_style_DotDescription = Class(name="diagram::style::DotDescription")
diagram_style_SizeComputationContainerStyleDescription = Class(name="diagram::style::SizeComputationContainerStyleDescription", is_abstract=True)
diagram_style_FlatContainerStyleDescription = Class(name="diagram::style::FlatContainerStyleDescription")
style_SizeComputationContainerStyleDescription = Class(name="style::SizeComputationContainerStyleDescription")
diagram_style_RoundedCornerStyleDescription = Class(name="diagram::style::RoundedCornerStyleDescription", is_abstract=True)
diagram_style_ContainerStyleDescription = Class(name="diagram::style::ContainerStyleDescription", is_abstract=True)
style_RoundedCornerStyleDescription = Class(name="style::RoundedCornerStyleDescription")
diagram_style_EdgeStyleDescription = Class(name="diagram::style::EdgeStyleDescription")
style_LabelBorderStyleDescription = Class(name="style::LabelBorderStyleDescription")
diagram_style_ShapeContainerStyleDescription = Class(name="diagram::style::ShapeContainerStyleDescription")
diagram_style_WorkspaceImageDescription = Class(name="diagram::style::WorkspaceImageDescription")
style_BeginLabelStyleDescription = Class(name="style::BeginLabelStyleDescription")
style_CenterLabelStyleDescription = Class(name="style::CenterLabelStyleDescription")
style_EndLabelStyleDescription = Class(name="style::EndLabelStyleDescription")
diagram_style_EndLabelStyleDescription = Class(name="diagram::style::EndLabelStyleDescription")
diagram_style_BracketEdgeStyleDescription = Class(name="diagram::style::BracketEdgeStyleDescription")
EdgeStyleDescription = Class(name="EdgeStyleDescription")
diagram_style_HideLabelCapabilityStyleDescription = Class(name="diagram::style::HideLabelCapabilityStyleDescription", is_abstract=True)
diagram_style_BeginLabelStyleDescription = Class(name="diagram::style::BeginLabelStyleDescription")
BasicLabelStyleDescription = Class(name="BasicLabelStyleDescription")
diagram_style_CenterLabelStyleDescription = Class(name="diagram::style::CenterLabelStyleDescription")
tool_PopupMenu = Class(name="tool::PopupMenu")
tool_ToolGroupExtension = Class(name="tool::ToolGroupExtension")
diagram_tool_ToolGroup = Class(name="diagram::tool::ToolGroup")
ToolEntry = Class(name="ToolEntry")
diagram_tool_ToolSection = Class(name="diagram::tool::ToolSection")
tool_ToolEntry = Class(name="tool::ToolEntry")
tool_NodeCreationVariable = Class(name="tool::NodeCreationVariable")
tool_ContainerViewVariable = Class(name="tool::ContainerViewVariable")
diagram_tool_ToolGroupExtension = Class(name="diagram::tool::ToolGroupExtension")
tool_ToolGroup = Class(name="tool::ToolGroup")
diagram_tool_NodeCreationDescription = Class(name="diagram::tool::NodeCreationDescription")
MappingBasedToolDescription = Class(name="MappingBasedToolDescription")
tool_InitialNodeCreationOperation = Class(name="tool::InitialNodeCreationOperation")
diagram_tool_EdgeCreationDescription = Class(name="diagram::tool::EdgeCreationDescription")
tool_TargetEdgeViewCreationVariable = Class(name="tool::TargetEdgeViewCreationVariable")
tool_InitEdgeCreationOperation = Class(name="tool::InitEdgeCreationOperation")
tool_SourceEdgeCreationVariable = Class(name="tool::SourceEdgeCreationVariable")
tool_TargetEdgeCreationVariable = Class(name="tool::TargetEdgeCreationVariable")
tool_SourceEdgeViewCreationVariable = Class(name="tool::SourceEdgeViewCreationVariable")
diagram_tool_ContainerCreationDescription = Class(name="diagram::tool::ContainerCreationDescription")
tool_DeleteHook = Class(name="tool::DeleteHook")
diagram_tool_DoubleClickDescription = Class(name="diagram::tool::DoubleClickDescription")
tool_ElementDoubleClickVariable = Class(name="tool::ElementDoubleClickVariable")
diagram_tool_DeleteHook = Class(name="diagram::tool::DeleteHook")
tool_DeleteHookParameter = Class(name="tool::DeleteHookParameter")
diagram_tool_DeleteHookParameter = Class(name="diagram::tool::DeleteHookParameter")
diagram_tool_DeleteElementDescription = Class(name="diagram::tool::DeleteElementDescription")
tool_ElementDeleteVariable = Class(name="tool::ElementDeleteVariable")
diagram_tool_ReconnectEdgeDescription = Class(name="diagram::tool::ReconnectEdgeDescription")
diagram_tool_RequestDescription = Class(name="diagram::tool::RequestDescription")
AbstractToolDescription = Class(name="AbstractToolDescription")
diagram_tool_DirectEditLabel = Class(name="diagram::tool::DirectEditLabel")
tool_EditMaskVariables = Class(name="tool::EditMaskVariables")
tool_ElementSelectVariable = Class(name="tool::ElementSelectVariable")
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
diagram_tool_BehaviorTool = Class(name="diagram::tool::BehaviorTool")
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
tool_InitialContainerDropOperation = Class(name="tool::InitialContainerDropOperation")
diagram_filter_MappingFilter = Class(name="diagram::filter::MappingFilter")
Filter = Class(name="Filter")
diagram_filter_FilterDescription = Class(name="diagram::filter::FilterDescription", is_abstract=True)
diagram_filter_Filter = Class(name="diagram::filter::Filter", is_abstract=True)
diagram_filter_CompositeFilterDescription = Class(name="diagram::filter::CompositeFilterDescription")
FilterDescription = Class(name="FilterDescription")
filter_Filter = Class(name="filter::Filter")
diagram_filter_VariableFilter = Class(name="diagram::filter::VariableFilter")
InteractiveVariableDescription = Class(name="InteractiveVariableDescription")
diagram_concern_ConcernSet = Class(name="diagram::concern::ConcernSet")
diagram_concern_ConcernDescription = Class(name="diagram::concern::ConcernDescription")

# diagram_DDiagram class attributes and methods
diagram_DDiagram_synchronized: Property = Property(name="synchronized", type=BooleanType)
diagram_DDiagram_isInLayoutingMode: Property = Property(name="isInLayoutingMode", type=BooleanType)
diagram_DDiagram_headerHeight: Property = Property(name="headerHeight", type=IntegerType)
diagram_DDiagram_m_getContainersFromMapping: Method = Method(name="getContainersFromMapping", parameters={Parameter(name='mapping')}, type=StringType)
diagram_DDiagram_m_getNodesFromMapping: Method = Method(name="getNodesFromMapping", parameters={Parameter(name='mapping')}, type=StringType)
diagram_DDiagram_m_getEdgesFromMapping: Method = Method(name="getEdgesFromMapping", parameters={Parameter(name='mapping')}, type=StringType)
diagram_DDiagram.attributes={diagram_DDiagram_synchronized, diagram_DDiagram_isInLayoutingMode, diagram_DDiagram_headerHeight}
diagram_DDiagram.methods={diagram_DDiagram_m_getNodesFromMapping, diagram_DDiagram_m_getContainersFromMapping, diagram_DDiagram_m_getEdgesFromMapping}

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

# diagram_DEdge class attributes and methods
diagram_DEdge_isMockEdge: Property = Property(name="isMockEdge", type=BooleanType)
diagram_DEdge_size: Property = Property(name="size", type=StringType)
diagram_DEdge_routingStyle: Property = Property(name="routingStyle", type=StringType)
diagram_DEdge_isFold: Property = Property(name="isFold", type=BooleanType)
diagram_DEdge_arrangeConstraints: Property = Property(name="arrangeConstraints", type=StringType)
diagram_DEdge_beginLabel: Property = Property(name="beginLabel", type=StringType)
diagram_DEdge_endLabel: Property = Property(name="endLabel", type=StringType)
diagram_DEdge_m_isRootFolding: Method = Method(name="isRootFolding", parameters={}, type=BooleanType)
diagram_DEdge.attributes={diagram_DEdge_size, diagram_DEdge_beginLabel, diagram_DEdge_routingStyle, diagram_DEdge_isMockEdge, diagram_DEdge_isFold, diagram_DEdge_endLabel, diagram_DEdge_arrangeConstraints}
diagram_DEdge.methods={diagram_DEdge_m_isRootFolding}

# diagram_DNode class attributes and methods
diagram_DNode_width: Property = Property(name="width", type=StringType)
diagram_DNode_height: Property = Property(name="height", type=StringType)
diagram_DNode_labelPosition: Property = Property(name="labelPosition", type=StringType)
diagram_DNode_resizeKind: Property = Property(name="resizeKind", type=StringType)
diagram_DNode.attributes={diagram_DNode_width, diagram_DNode_height, diagram_DNode_resizeKind, diagram_DNode_labelPosition}

# diagram_DNodeListElement class attributes and methods

# tool_BehaviorTool class attributes and methods

# diagram_DDiagramElementContainer class attributes and methods
diagram_DDiagramElementContainer_width: Property = Property(name="width", type=StringType)
diagram_DDiagramElementContainer_height: Property = Property(name="height", type=StringType)
diagram_DDiagramElementContainer_m_getNodesFromMapping: Method = Method(name="getNodesFromMapping", parameters={Parameter(name='mapping')}, type=StringType)
diagram_DDiagramElementContainer_m_getContainersFromMapping: Method = Method(name="getContainersFromMapping", parameters={Parameter(name='mapping')}, type=StringType)
diagram_DDiagramElementContainer.attributes={diagram_DDiagramElementContainer_height, diagram_DDiagramElementContainer_width}
diagram_DDiagramElementContainer.methods={diagram_DDiagramElementContainer_m_getContainersFromMapping, diagram_DDiagramElementContainer_m_getNodesFromMapping}

# concern_ConcernDescription class attributes and methods

# filter_FilterDescription class attributes and methods

# AdditionalLayer class attributes and methods

# validation_ValidationRule class attributes and methods

# diagram_FilterVariableHistory class attributes and methods

# Layer class attributes and methods

# diagram_DSemanticDiagram class attributes and methods

# DDiagram class attributes and methods

# DSemanticDecorator class attributes and methods

# DRepresentationElement class attributes and methods

# diagram_FoldingPointFilter class attributes and methods

# diagram_FoldingFilter class attributes and methods

# diagram_Decoration class attributes and methods

# DiagramElementMapping class attributes and methods

# diagram_GraphicalFilter class attributes and methods

# diagram_HideFilter class attributes and methods

# GraphicalFilter class attributes and methods

# diagram_HideLabelFilter class attributes and methods

# EdgeTarget class attributes and methods

# diagram_AppliedCompositeFilters class attributes and methods

# filter_CompositeFilterDescription class attributes and methods

# diagram_AbsoluteBoundsFilter class attributes and methods
diagram_AbsoluteBoundsFilter_x: Property = Property(name="x", type=StringType)
diagram_AbsoluteBoundsFilter_y: Property = Property(name="y", type=StringType)
diagram_AbsoluteBoundsFilter_height: Property = Property(name="height", type=StringType)
diagram_AbsoluteBoundsFilter_width: Property = Property(name="width", type=StringType)
diagram_AbsoluteBoundsFilter.attributes={diagram_AbsoluteBoundsFilter_x, diagram_AbsoluteBoundsFilter_width, diagram_AbsoluteBoundsFilter_y, diagram_AbsoluteBoundsFilter_height}

# diagram_AbstractDNode class attributes and methods
diagram_AbstractDNode_arrangeConstraints: Property = Property(name="arrangeConstraints", type=StringType)
diagram_AbstractDNode.attributes={diagram_AbstractDNode_arrangeConstraints}

# DDiagramElement class attributes and methods

# AbstractDNode class attributes and methods

# diagram_NodeStyle class attributes and methods
diagram_NodeStyle_labelPosition: Property = Property(name="labelPosition", type=StringType)
diagram_NodeStyle.attributes={diagram_NodeStyle_labelPosition}

# diagram_Style class attributes and methods

# NodeMapping class attributes and methods

# diagram_ContainerStyle class attributes and methods

# diagram_DNodeList class attributes and methods

# ContainerMapping class attributes and methods

# diagram_DNodeContainer class attributes and methods
diagram_DNodeContainer_childrenPresentation: Property = Property(name="childrenPresentation", type=StringType)
diagram_DNodeContainer.attributes={diagram_DNodeContainer_childrenPresentation}

# DDiagramElementContainer class attributes and methods

# diagram_EdgeStyle class attributes and methods
diagram_EdgeStyle_lineStyle: Property = Property(name="lineStyle", type=StringType)
diagram_EdgeStyle_sourceArrow: Property = Property(name="sourceArrow", type=StringType)
diagram_EdgeStyle_targetArrow: Property = Property(name="targetArrow", type=StringType)
diagram_EdgeStyle_foldingStyle: Property = Property(name="foldingStyle", type=StringType)
diagram_EdgeStyle_size: Property = Property(name="size", type=StringType)
diagram_EdgeStyle_centered: Property = Property(name="centered", type=StringType)
diagram_EdgeStyle_strokeColor: Property = Property(name="strokeColor", type=StringType)
diagram_EdgeStyle_routingStyle: Property = Property(name="routingStyle", type=StringType)
diagram_EdgeStyle.attributes={diagram_EdgeStyle_targetArrow, diagram_EdgeStyle_sourceArrow, diagram_EdgeStyle_size, diagram_EdgeStyle_foldingStyle, diagram_EdgeStyle_lineStyle, diagram_EdgeStyle_routingStyle, diagram_EdgeStyle_centered, diagram_EdgeStyle_strokeColor}

# diagram_EdgeTarget class attributes and methods

# IEdgeMapping class attributes and methods

# diagram_Dot class attributes and methods
diagram_Dot_strokeSizeComputationExpression: Property = Property(name="strokeSizeComputationExpression", type=StringType)
diagram_Dot_backgroundColor: Property = Property(name="backgroundColor", type=StringType)
diagram_Dot.attributes={diagram_Dot_backgroundColor, diagram_Dot_strokeSizeComputationExpression}

# LabelStyle class attributes and methods

# Style class attributes and methods

# BorderedStyle class attributes and methods

# HideLabelCapabilityStyle class attributes and methods

# NodeStyle class attributes and methods

# diagram_FlatContainerStyle class attributes and methods
diagram_FlatContainerStyle_backgroundStyle: Property = Property(name="backgroundStyle", type=StringType)
diagram_FlatContainerStyle_backgroundColor: Property = Property(name="backgroundColor", type=StringType)
diagram_FlatContainerStyle_foregroundColor: Property = Property(name="foregroundColor", type=StringType)
diagram_FlatContainerStyle.attributes={diagram_FlatContainerStyle_backgroundStyle, diagram_FlatContainerStyle_foregroundColor, diagram_FlatContainerStyle_backgroundColor}

# ContainerStyle class attributes and methods

# diagram_GaugeSection class attributes and methods
diagram_GaugeSection_foregroundColor: Property = Property(name="foregroundColor", type=StringType)
diagram_GaugeSection_min: Property = Property(name="min", type=StringType)
diagram_GaugeSection_max: Property = Property(name="max", type=StringType)
diagram_GaugeSection_value: Property = Property(name="value", type=StringType)
diagram_GaugeSection_label: Property = Property(name="label", type=StringType)
diagram_GaugeSection_backgroundColor: Property = Property(name="backgroundColor", type=StringType)
diagram_GaugeSection.attributes={diagram_GaugeSection_backgroundColor, diagram_GaugeSection_label, diagram_GaugeSection_value, diagram_GaugeSection_max, diagram_GaugeSection_foregroundColor, diagram_GaugeSection_min}

# Customizable class attributes and methods

# diagram_ShapeContainerStyle class attributes and methods
diagram_ShapeContainerStyle_shape: Property = Property(name="shape", type=StringType)
diagram_ShapeContainerStyle_backgroundColor: Property = Property(name="backgroundColor", type=StringType)
diagram_ShapeContainerStyle.attributes={diagram_ShapeContainerStyle_backgroundColor, diagram_ShapeContainerStyle_shape}

# diagram_Square class attributes and methods
diagram_Square_width: Property = Property(name="width", type=StringType)
diagram_Square_height: Property = Property(name="height", type=StringType)
diagram_Square_color: Property = Property(name="color", type=StringType)
diagram_Square.attributes={diagram_Square_height, diagram_Square_color, diagram_Square_width}

# diagram_Ellipse class attributes and methods
diagram_Ellipse_horizontalDiameter: Property = Property(name="horizontalDiameter", type=StringType)
diagram_Ellipse_verticalDiameter: Property = Property(name="verticalDiameter", type=StringType)
diagram_Ellipse_color: Property = Property(name="color", type=StringType)
diagram_Ellipse.attributes={diagram_Ellipse_horizontalDiameter, diagram_Ellipse_color, diagram_Ellipse_verticalDiameter}

# diagram_Lozenge class attributes and methods
diagram_Lozenge_height: Property = Property(name="height", type=StringType)
diagram_Lozenge_color: Property = Property(name="color", type=StringType)
diagram_Lozenge_width: Property = Property(name="width", type=StringType)
diagram_Lozenge.attributes={diagram_Lozenge_color, diagram_Lozenge_height, diagram_Lozenge_width}

# diagram_BundledImage class attributes and methods
diagram_BundledImage_shape: Property = Property(name="shape", type=StringType)
diagram_BundledImage_color: Property = Property(name="color", type=StringType)
diagram_BundledImage_providedShapeID: Property = Property(name="providedShapeID", type=StringType)
diagram_BundledImage.attributes={diagram_BundledImage_shape, diagram_BundledImage_providedShapeID, diagram_BundledImage_color}

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
diagram_CenterLabelStyle.methods={diagram_CenterLabelStyle_m_setDescription, diagram_CenterLabelStyle_m_getDescription}

# diagram_EndLabelStyle class attributes and methods
diagram_EndLabelStyle_m_getDescription: Method = Method(name="getDescription", parameters={}, type=StringType)
diagram_EndLabelStyle_m_setDescription: Method = Method(name="setDescription", parameters={Parameter(name='description')})
diagram_EndLabelStyle.methods={diagram_EndLabelStyle_m_setDescription, diagram_EndLabelStyle_m_getDescription}

# diagram_BorderedStyle class attributes and methods
diagram_BorderedStyle_borderSize: Property = Property(name="borderSize", type=StringType)
diagram_BorderedStyle_borderSizeComputationExpression: Property = Property(name="borderSizeComputationExpression", type=StringType)
diagram_BorderedStyle_borderColor: Property = Property(name="borderColor", type=StringType)
diagram_BorderedStyle_borderLineStyle: Property = Property(name="borderLineStyle", type=StringType)
diagram_BorderedStyle.attributes={diagram_BorderedStyle_borderSizeComputationExpression, diagram_BorderedStyle_borderSize, diagram_BorderedStyle_borderLineStyle, diagram_BorderedStyle_borderColor}

# diagram_GaugeCompositeStyle class attributes and methods
diagram_GaugeCompositeStyle_alignment: Property = Property(name="alignment", type=StringType)
diagram_GaugeCompositeStyle.attributes={diagram_GaugeCompositeStyle_alignment}

# diagram_CollapseFilter class attributes and methods
diagram_CollapseFilter_width: Property = Property(name="width", type=IntegerType)
diagram_CollapseFilter_height: Property = Property(name="height", type=IntegerType)
diagram_CollapseFilter.attributes={diagram_CollapseFilter_width, diagram_CollapseFilter_height}

# diagram_Note class attributes and methods
diagram_Note_color: Property = Property(name="color", type=StringType)
diagram_Note.attributes={diagram_Note_color}

# diagram_VariableValue class attributes and methods

# diagram_BracketEdgeStyle class attributes and methods

# EdgeStyle class attributes and methods

# diagram_ComputedStyleDescriptionRegistry class attributes and methods

# style_StyleDescription class attributes and methods

# diagram_DragAndDropTarget class attributes and methods
diagram_DragAndDropTarget_m_getDragAndDropDescription: Method = Method(name="getDragAndDropDescription", parameters={}, type=StringType)
diagram_DragAndDropTarget.methods={diagram_DragAndDropTarget_m_getDragAndDropDescription}

# diagram_IndirectlyCollapseFilter class attributes and methods

# CollapseFilter class attributes and methods

# BasicLabelStyle class attributes and methods

# tool_SelectModelElementVariable class attributes and methods

# diagram_EObject class attributes and methods

# diagram_description_DiagramDescription class attributes and methods
diagram_description_DiagramDescription_domainClass: Property = Property(name="domainClass", type=StringType)
diagram_description_DiagramDescription_preconditionExpression: Property = Property(name="preconditionExpression", type=StringType)
diagram_description_DiagramDescription_rootExpression: Property = Property(name="rootExpression", type=StringType)
diagram_description_DiagramDescription_enablePopupBars: Property = Property(name="enablePopupBars", type=BooleanType)
diagram_description_DiagramDescription_m_createDiagram: Method = Method(name="createDiagram", parameters={}, type=StringType)
diagram_description_DiagramDescription.attributes={diagram_description_DiagramDescription_preconditionExpression, diagram_description_DiagramDescription_enablePopupBars, diagram_description_DiagramDescription_rootExpression, diagram_description_DiagramDescription_domainClass}
diagram_description_DiagramDescription.methods={diagram_description_DiagramDescription_m_createDiagram}

# description_DragAndDropTargetDescription class attributes and methods

# description_RepresentationDescription class attributes and methods

# description_PasteTargetDescription class attributes and methods

# diagram_HideLabelCapabilityStyle class attributes and methods
diagram_HideLabelCapabilityStyle_hideLabelByDefault: Property = Property(name="hideLabelByDefault", type=BooleanType)
diagram_HideLabelCapabilityStyle.attributes={diagram_HideLabelCapabilityStyle_hideLabelByDefault}

# diagram_TypedVariableValue class attributes and methods
diagram_TypedVariableValue_value: Property = Property(name="value", type=StringType)
diagram_TypedVariableValue.attributes={diagram_TypedVariableValue_value}

# VariableValue class attributes and methods

# TypedVariable class attributes and methods

# diagram_EObjectVariableValue class attributes and methods

# validation_ValidationSet class attributes and methods

# concern_ConcernSet class attributes and methods

# tool_AbstractToolDescription class attributes and methods

# EdgeMapping class attributes and methods

# tool_RepresentationCreationDescription class attributes and methods

# Layout class attributes and methods

# tool_InitialOperation class attributes and methods

# EdgeMappingImport class attributes and methods

# diagram_description_DiagramImportDescription class attributes and methods

# description_RepresentationImportDescription class attributes and methods

# description_DiagramDescription class attributes and methods

# diagram_description_DiagramExtensionDescription class attributes and methods

# RepresentationExtensionDescription class attributes and methods

# tool_ToolSection class attributes and methods

# diagram_description_DiagramElementMapping class attributes and methods
diagram_description_DiagramElementMapping_semanticCandidatesExpression: Property = Property(name="semanticCandidatesExpression", type=StringType)
diagram_description_DiagramElementMapping_createElements: Property = Property(name="createElements", type=BooleanType)
diagram_description_DiagramElementMapping_preconditionExpression: Property = Property(name="preconditionExpression", type=StringType)
diagram_description_DiagramElementMapping_semanticElements: Property = Property(name="semanticElements", type=StringType)
diagram_description_DiagramElementMapping_synchronizationLock: Property = Property(name="synchronizationLock", type=BooleanType)
diagram_description_DiagramElementMapping_m_getAllMappings: Method = Method(name="getAllMappings", parameters={}, type=StringType)
diagram_description_DiagramElementMapping_m_isFrom: Method = Method(name="isFrom", parameters={Parameter(name='element')}, type=BooleanType)
diagram_description_DiagramElementMapping_m_checkPrecondition: Method = Method(name="checkPrecondition", parameters={Parameter(name='modelElement'), Parameter(name='container'), Parameter(name='containerView')}, type=BooleanType)
diagram_description_DiagramElementMapping.attributes={diagram_description_DiagramElementMapping_synchronizationLock, diagram_description_DiagramElementMapping_createElements, diagram_description_DiagramElementMapping_preconditionExpression, diagram_description_DiagramElementMapping_semanticCandidatesExpression, diagram_description_DiagramElementMapping_semanticElements}
diagram_description_DiagramElementMapping.methods={diagram_description_DiagramElementMapping_m_checkPrecondition, diagram_description_DiagramElementMapping_m_isFrom, diagram_description_DiagramElementMapping_m_getAllMappings}

# description_RepresentationElementMapping class attributes and methods

# tool_DeleteElementDescription class attributes and methods

# tool_DirectEditLabel class attributes and methods

# tool_DoubleClickDescription class attributes and methods

# diagram_description_AbstractNodeMapping class attributes and methods
diagram_description_AbstractNodeMapping_domainClass: Property = Property(name="domainClass", type=StringType)
diagram_description_AbstractNodeMapping_m_findDNodeFromEObject: Method = Method(name="findDNodeFromEObject", parameters={Parameter(name='eObject')}, type=DDiagramElement)
diagram_description_AbstractNodeMapping_m_clearDNodesDone: Method = Method(name="clearDNodesDone", parameters={})
diagram_description_AbstractNodeMapping_m_addDoneNode: Method = Method(name="addDoneNode", parameters={Parameter(name='node')})
diagram_description_AbstractNodeMapping_m_getAllBorderedNodeMappings: Method = Method(name="getAllBorderedNodeMappings", parameters={}, type=StringType)
diagram_description_AbstractNodeMapping.attributes={diagram_description_AbstractNodeMapping_domainClass}
diagram_description_AbstractNodeMapping.methods={diagram_description_AbstractNodeMapping_m_clearDNodesDone, diagram_description_AbstractNodeMapping_m_findDNodeFromEObject, diagram_description_AbstractNodeMapping_m_addDoneNode, diagram_description_AbstractNodeMapping_m_getAllBorderedNodeMappings}

# description_DiagramElementMapping class attributes and methods

# diagram_description_NodeMapping class attributes and methods
diagram_description_NodeMapping_m_updateNode: Method = Method(name="updateNode", parameters={Parameter(name='node')})
diagram_description_NodeMapping_m_updateListElement: Method = Method(name="updateListElement", parameters={Parameter(name='listElement')})
diagram_description_NodeMapping_m_createNode: Method = Method(name="createNode", parameters={Parameter(name='modelElement'), Parameter(name='viewPoint'), Parameter(name='container')}, type=StringType)
diagram_description_NodeMapping_m_getNodesCandidates: Method = Method(name="getNodesCandidates", parameters={Parameter(name='semanticOrigin'), Parameter(name='container')}, type=StringType)
diagram_description_NodeMapping_m_getNodesCandidates: Method = Method(name="getNodesCandidates", parameters={Parameter(name='containerView'), Parameter(name='container'), Parameter(name='semanticOrigin')}, type=StringType)
diagram_description_NodeMapping.methods={diagram_description_NodeMapping_m_getNodesCandidates, diagram_description_NodeMapping_m_createNode, diagram_description_NodeMapping_m_getNodesCandidates, diagram_description_NodeMapping_m_updateListElement, diagram_description_NodeMapping_m_updateNode}

# description_AbstractNodeMapping class attributes and methods

# style_NodeStyleDescription class attributes and methods

# ConditionalNodeStyleDescription class attributes and methods

# diagram_description_ContainerMapping class attributes and methods
diagram_description_ContainerMapping_childrenPresentation: Property = Property(name="childrenPresentation", type=StringType)
diagram_description_ContainerMapping_m_getBestStyle: Method = Method(name="getBestStyle", parameters={Parameter(name='modelElement'), Parameter(name='containerVariable'), Parameter(name='viewVariable')}, type=ContainerStyle)
diagram_description_ContainerMapping.attributes={diagram_description_ContainerMapping_childrenPresentation}
diagram_description_ContainerMapping.methods={diagram_description_ContainerMapping_m_getBestStyle}

# style_ContainerStyleDescription class attributes and methods

# ConditionalContainerStyleDescription class attributes and methods

# diagram_description_EdgeMapping class attributes and methods
diagram_description_EdgeMapping_targetFinderExpression: Property = Property(name="targetFinderExpression", type=StringType)
diagram_description_EdgeMapping_targetExpression: Property = Property(name="targetExpression", type=StringType)
diagram_description_EdgeMapping_domainClass: Property = Property(name="domainClass", type=StringType)
diagram_description_EdgeMapping_useDomainElement: Property = Property(name="useDomainElement", type=BooleanType)
diagram_description_EdgeMapping_sourceFinderExpression: Property = Property(name="sourceFinderExpression", type=StringType)
diagram_description_EdgeMapping_pathExpression: Property = Property(name="pathExpression", type=StringType)
diagram_description_EdgeMapping_m_createEdge: Method = Method(name="createEdge", parameters={Parameter(name='semanticTarget'), Parameter(name='target'), Parameter(name='source')}, type=StringType)
diagram_description_EdgeMapping_m_createEdge: Method = Method(name="createEdge", parameters={Parameter(name='container'), Parameter(name='source'), Parameter(name='semanticTarget'), Parameter(name='target')}, type=StringType)
diagram_description_EdgeMapping_m_getEdgeTargetCandidates: Method = Method(name="getEdgeTargetCandidates", parameters={Parameter(name='semanticOrigin'), Parameter(name='containerView'), Parameter(name='container')}, type=StringType)
diagram_description_EdgeMapping_m_getBestStyle: Method = Method(name="getBestStyle", parameters={Parameter(name='viewVariable'), Parameter(name='modelElement'), Parameter(name='containerVariable')}, type=EdgeStyle)
diagram_description_EdgeMapping_m_updateEdge: Method = Method(name="updateEdge", parameters={Parameter(name='viewEdge')})
diagram_description_EdgeMapping_m_getEdgeTargetCandidates: Method = Method(name="getEdgeTargetCandidates", parameters={Parameter(name='semanticOrigin'), Parameter(name='viewPoint')}, type=StringType)
diagram_description_EdgeMapping_m_getEdgeSourceCandidates: Method = Method(name="getEdgeSourceCandidates", parameters={Parameter(name='viewPoint'), Parameter(name='semanticOrigin')}, type=StringType)
diagram_description_EdgeMapping.attributes={diagram_description_EdgeMapping_pathExpression, diagram_description_EdgeMapping_sourceFinderExpression, diagram_description_EdgeMapping_useDomainElement, diagram_description_EdgeMapping_domainClass, diagram_description_EdgeMapping_targetFinderExpression, diagram_description_EdgeMapping_targetExpression}
diagram_description_EdgeMapping.methods={diagram_description_EdgeMapping_m_getEdgeTargetCandidates, diagram_description_EdgeMapping_m_updateEdge, diagram_description_EdgeMapping_m_getEdgeSourceCandidates, diagram_description_EdgeMapping_m_createEdge, diagram_description_EdgeMapping_m_getEdgeTargetCandidates, diagram_description_EdgeMapping_m_createEdge, diagram_description_EdgeMapping_m_getBestStyle}

# description_IEdgeMapping class attributes and methods

# diagram_description_NodeMappingImport class attributes and methods

# description_NodeMapping class attributes and methods

# description_AbstractMappingImport class attributes and methods

# diagram_description_ContainerMappingImport class attributes and methods

# description_ContainerMapping class attributes and methods

# ConditionalEdgeStyleDescription class attributes and methods

# tool_ReconnectEdgeDescription class attributes and methods

# style_EdgeStyleDescription class attributes and methods

# diagram_description_EdgeMappingImport class attributes and methods
diagram_description_EdgeMappingImport_inheritsAncestorFilters: Property = Property(name="inheritsAncestorFilters", type=BooleanType)
diagram_description_EdgeMappingImport.attributes={diagram_description_EdgeMappingImport_inheritsAncestorFilters}

# description_IdentifiedElement class attributes and methods

# AbstractNodeMapping class attributes and methods

# diagram_description_IEdgeMapping class attributes and methods
diagram_description_IEdgeMapping_m_getBestStyle: Method = Method(name="getBestStyle", parameters={Parameter(name='viewVariable'), Parameter(name='containerVariable'), Parameter(name='modelElement')}, type=EdgeStyle)
diagram_description_IEdgeMapping.methods={diagram_description_IEdgeMapping_m_getBestStyle}

# diagram_description_Layout class attributes and methods

# DocumentedElement class attributes and methods

# diagram_description_OrderedTreeLayout class attributes and methods
diagram_description_OrderedTreeLayout_childrenExpression: Property = Property(name="childrenExpression", type=StringType)
diagram_description_OrderedTreeLayout.attributes={diagram_description_OrderedTreeLayout_childrenExpression}

# diagram_description_ConditionalNodeStyleDescription class attributes and methods

# ConditionalStyleDescription class attributes and methods

# diagram_description_ConditionalEdgeStyleDescription class attributes and methods

# diagram_description_ConditionalContainerStyleDescription class attributes and methods

# diagram_description_MappingBasedDecoration class attributes and methods

# DecorationDescription class attributes and methods

# diagram_description_Layer class attributes and methods
diagram_description_Layer_icon: Property = Property(name="icon", type=StringType)
diagram_description_Layer.attributes={diagram_description_Layer_icon}

# description_EndUserDocumentedElement class attributes and methods

# diagram_description_CompositeLayout class attributes and methods
diagram_description_CompositeLayout_padding: Property = Property(name="padding", type=IntegerType)
diagram_description_CompositeLayout_direction: Property = Property(name="direction", type=StringType)
diagram_description_CompositeLayout.attributes={diagram_description_CompositeLayout_direction, diagram_description_CompositeLayout_padding}

# diagram_description_AdditionalLayer class attributes and methods
diagram_description_AdditionalLayer_activeByDefault: Property = Property(name="activeByDefault", type=BooleanType)
diagram_description_AdditionalLayer_optional: Property = Property(name="optional", type=BooleanType)
diagram_description_AdditionalLayer.attributes={diagram_description_AdditionalLayer_optional, diagram_description_AdditionalLayer_activeByDefault}

# diagram_description_DragAndDropTargetDescription class attributes and methods

# tool_ContainerDropDescription class attributes and methods

# diagram_style_BorderedStyleDescription class attributes and methods
diagram_style_BorderedStyleDescription_borderSizeComputationExpression: Property = Property(name="borderSizeComputationExpression", type=StringType)
diagram_style_BorderedStyleDescription_borderLineStyle: Property = Property(name="borderLineStyle", type=StringType)
diagram_style_BorderedStyleDescription.attributes={diagram_style_BorderedStyleDescription_borderLineStyle, diagram_style_BorderedStyleDescription_borderSizeComputationExpression}

# StyleDescription class attributes and methods

# DecorationDescriptionsSet class attributes and methods

# Customization class attributes and methods

# style_LabelStyleDescription class attributes and methods

# style_TooltipStyleDescription class attributes and methods

# style_HideLabelCapabilityStyleDescription class attributes and methods

# ColorDescription class attributes and methods

# diagram_style_NodeStyleDescription class attributes and methods
diagram_style_NodeStyleDescription_sizeComputationExpression: Property = Property(name="sizeComputationExpression", type=StringType)
diagram_style_NodeStyleDescription_labelPosition: Property = Property(name="labelPosition", type=StringType)
diagram_style_NodeStyleDescription_resizeKind: Property = Property(name="resizeKind", type=StringType)
diagram_style_NodeStyleDescription_forbiddenSides: Property = Property(name="forbiddenSides", type=StringType)
diagram_style_NodeStyleDescription.attributes={diagram_style_NodeStyleDescription_labelPosition, diagram_style_NodeStyleDescription_forbiddenSides, diagram_style_NodeStyleDescription_resizeKind, diagram_style_NodeStyleDescription_sizeComputationExpression}

# style_BorderedStyleDescription class attributes and methods

# diagram_style_LozengeNodeDescription class attributes and methods
diagram_style_LozengeNodeDescription_widthComputationExpression: Property = Property(name="widthComputationExpression", type=StringType)
diagram_style_LozengeNodeDescription_heightComputationExpression: Property = Property(name="heightComputationExpression", type=StringType)
diagram_style_LozengeNodeDescription.attributes={diagram_style_LozengeNodeDescription_heightComputationExpression, diagram_style_LozengeNodeDescription_widthComputationExpression}

# diagram_style_CustomStyleDescription class attributes and methods
diagram_style_CustomStyleDescription_id: Property = Property(name="id", type=StringType)
diagram_style_CustomStyleDescription.attributes={diagram_style_CustomStyleDescription_id}

# NodeStyleDescription class attributes and methods

# diagram_style_SquareDescription class attributes and methods
diagram_style_SquareDescription_width: Property = Property(name="width", type=StringType)
diagram_style_SquareDescription_height: Property = Property(name="height", type=StringType)
diagram_style_SquareDescription.attributes={diagram_style_SquareDescription_height, diagram_style_SquareDescription_width}

# diagram_style_BundledImageDescription class attributes and methods
diagram_style_BundledImageDescription_shape: Property = Property(name="shape", type=StringType)
diagram_style_BundledImageDescription_providedShapeID: Property = Property(name="providedShapeID", type=StringType)
diagram_style_BundledImageDescription.attributes={diagram_style_BundledImageDescription_providedShapeID, diagram_style_BundledImageDescription_shape}

# diagram_style_NoteDescription class attributes and methods

# diagram_style_EllipseNodeDescription class attributes and methods
diagram_style_EllipseNodeDescription_verticalDiameterComputationExpression: Property = Property(name="verticalDiameterComputationExpression", type=StringType)
diagram_style_EllipseNodeDescription_horizontalDiameterComputationExpression: Property = Property(name="horizontalDiameterComputationExpression", type=StringType)
diagram_style_EllipseNodeDescription.attributes={diagram_style_EllipseNodeDescription_verticalDiameterComputationExpression, diagram_style_EllipseNodeDescription_horizontalDiameterComputationExpression}

# diagram_style_GaugeCompositeStyleDescription class attributes and methods
diagram_style_GaugeCompositeStyleDescription_alignment: Property = Property(name="alignment", type=StringType)
diagram_style_GaugeCompositeStyleDescription.attributes={diagram_style_GaugeCompositeStyleDescription_alignment}

# style_GaugeSectionDescription class attributes and methods

# diagram_style_GaugeSectionDescription class attributes and methods
diagram_style_GaugeSectionDescription_minValueExpression: Property = Property(name="minValueExpression", type=StringType)
diagram_style_GaugeSectionDescription_label: Property = Property(name="label", type=StringType)
diagram_style_GaugeSectionDescription_maxValueExpression: Property = Property(name="maxValueExpression", type=StringType)
diagram_style_GaugeSectionDescription_valueExpression: Property = Property(name="valueExpression", type=StringType)
diagram_style_GaugeSectionDescription.attributes={diagram_style_GaugeSectionDescription_minValueExpression, diagram_style_GaugeSectionDescription_label, diagram_style_GaugeSectionDescription_valueExpression, diagram_style_GaugeSectionDescription_maxValueExpression}

# diagram_style_DotDescription class attributes and methods
diagram_style_DotDescription_strokeSizeComputationExpression: Property = Property(name="strokeSizeComputationExpression", type=StringType)
diagram_style_DotDescription.attributes={diagram_style_DotDescription_strokeSizeComputationExpression}

# diagram_style_SizeComputationContainerStyleDescription class attributes and methods
diagram_style_SizeComputationContainerStyleDescription_widthComputationExpression: Property = Property(name="widthComputationExpression", type=StringType)
diagram_style_SizeComputationContainerStyleDescription_heightComputationExpression: Property = Property(name="heightComputationExpression", type=StringType)
diagram_style_SizeComputationContainerStyleDescription.attributes={diagram_style_SizeComputationContainerStyleDescription_heightComputationExpression, diagram_style_SizeComputationContainerStyleDescription_widthComputationExpression}

# diagram_style_FlatContainerStyleDescription class attributes and methods
diagram_style_FlatContainerStyleDescription_backgroundStyle: Property = Property(name="backgroundStyle", type=StringType)
diagram_style_FlatContainerStyleDescription.attributes={diagram_style_FlatContainerStyleDescription_backgroundStyle}

# style_SizeComputationContainerStyleDescription class attributes and methods

# diagram_style_RoundedCornerStyleDescription class attributes and methods
diagram_style_RoundedCornerStyleDescription_arcWidth: Property = Property(name="arcWidth", type=StringType)
diagram_style_RoundedCornerStyleDescription_arcHeight: Property = Property(name="arcHeight", type=StringType)
diagram_style_RoundedCornerStyleDescription.attributes={diagram_style_RoundedCornerStyleDescription_arcWidth, diagram_style_RoundedCornerStyleDescription_arcHeight}

# diagram_style_ContainerStyleDescription class attributes and methods
diagram_style_ContainerStyleDescription_roundedCorner: Property = Property(name="roundedCorner", type=BooleanType)
diagram_style_ContainerStyleDescription.attributes={diagram_style_ContainerStyleDescription_roundedCorner}

# style_RoundedCornerStyleDescription class attributes and methods

# diagram_style_EdgeStyleDescription class attributes and methods
diagram_style_EdgeStyleDescription_lineStyle: Property = Property(name="lineStyle", type=StringType)
diagram_style_EdgeStyleDescription_sourceArrow: Property = Property(name="sourceArrow", type=StringType)
diagram_style_EdgeStyleDescription_foldingStyle: Property = Property(name="foldingStyle", type=StringType)
diagram_style_EdgeStyleDescription_endsCentering: Property = Property(name="endsCentering", type=StringType)
diagram_style_EdgeStyleDescription_targetArrow: Property = Property(name="targetArrow", type=StringType)
diagram_style_EdgeStyleDescription_sizeComputationExpression: Property = Property(name="sizeComputationExpression", type=StringType)
diagram_style_EdgeStyleDescription_routingStyle: Property = Property(name="routingStyle", type=StringType)
diagram_style_EdgeStyleDescription.attributes={diagram_style_EdgeStyleDescription_foldingStyle, diagram_style_EdgeStyleDescription_endsCentering, diagram_style_EdgeStyleDescription_routingStyle, diagram_style_EdgeStyleDescription_sourceArrow, diagram_style_EdgeStyleDescription_targetArrow, diagram_style_EdgeStyleDescription_lineStyle, diagram_style_EdgeStyleDescription_sizeComputationExpression}

# style_LabelBorderStyleDescription class attributes and methods

# diagram_style_ShapeContainerStyleDescription class attributes and methods
diagram_style_ShapeContainerStyleDescription_shape: Property = Property(name="shape", type=StringType)
diagram_style_ShapeContainerStyleDescription.attributes={diagram_style_ShapeContainerStyleDescription_shape}

# diagram_style_WorkspaceImageDescription class attributes and methods
diagram_style_WorkspaceImageDescription_workspacePath: Property = Property(name="workspacePath", type=StringType)
diagram_style_WorkspaceImageDescription.attributes={diagram_style_WorkspaceImageDescription_workspacePath}

# style_BeginLabelStyleDescription class attributes and methods

# style_CenterLabelStyleDescription class attributes and methods

# style_EndLabelStyleDescription class attributes and methods

# diagram_style_EndLabelStyleDescription class attributes and methods

# diagram_style_BracketEdgeStyleDescription class attributes and methods

# EdgeStyleDescription class attributes and methods

# diagram_style_HideLabelCapabilityStyleDescription class attributes and methods
diagram_style_HideLabelCapabilityStyleDescription_hideLabelByDefault: Property = Property(name="hideLabelByDefault", type=BooleanType)
diagram_style_HideLabelCapabilityStyleDescription.attributes={diagram_style_HideLabelCapabilityStyleDescription_hideLabelByDefault}

# diagram_style_BeginLabelStyleDescription class attributes and methods

# BasicLabelStyleDescription class attributes and methods

# diagram_style_CenterLabelStyleDescription class attributes and methods

# tool_PopupMenu class attributes and methods

# tool_ToolGroupExtension class attributes and methods

# diagram_tool_ToolGroup class attributes and methods

# ToolEntry class attributes and methods

# diagram_tool_ToolSection class attributes and methods
diagram_tool_ToolSection_icon: Property = Property(name="icon", type=StringType)
diagram_tool_ToolSection.attributes={diagram_tool_ToolSection_icon}

# tool_ToolEntry class attributes and methods

# tool_NodeCreationVariable class attributes and methods

# tool_ContainerViewVariable class attributes and methods

# diagram_tool_ToolGroupExtension class attributes and methods

# tool_ToolGroup class attributes and methods

# diagram_tool_NodeCreationDescription class attributes and methods
diagram_tool_NodeCreationDescription_iconPath: Property = Property(name="iconPath", type=StringType)
diagram_tool_NodeCreationDescription.attributes={diagram_tool_NodeCreationDescription_iconPath}

# MappingBasedToolDescription class attributes and methods

# tool_InitialNodeCreationOperation class attributes and methods

# diagram_tool_EdgeCreationDescription class attributes and methods
diagram_tool_EdgeCreationDescription_connectionStartPrecondition: Property = Property(name="connectionStartPrecondition", type=StringType)
diagram_tool_EdgeCreationDescription_iconPath: Property = Property(name="iconPath", type=StringType)
diagram_tool_EdgeCreationDescription_m_getBestMapping: Method = Method(name="getBestMapping", parameters={Parameter(name='createdElements'), Parameter(name='source'), Parameter(name='target')}, type=StringType)
diagram_tool_EdgeCreationDescription.attributes={diagram_tool_EdgeCreationDescription_connectionStartPrecondition, diagram_tool_EdgeCreationDescription_iconPath}
diagram_tool_EdgeCreationDescription.methods={diagram_tool_EdgeCreationDescription_m_getBestMapping}

# tool_TargetEdgeViewCreationVariable class attributes and methods

# tool_InitEdgeCreationOperation class attributes and methods

# tool_SourceEdgeCreationVariable class attributes and methods

# tool_TargetEdgeCreationVariable class attributes and methods

# tool_SourceEdgeViewCreationVariable class attributes and methods

# diagram_tool_ContainerCreationDescription class attributes and methods
diagram_tool_ContainerCreationDescription_iconPath: Property = Property(name="iconPath", type=StringType)
diagram_tool_ContainerCreationDescription.attributes={diagram_tool_ContainerCreationDescription_iconPath}

# tool_DeleteHook class attributes and methods

# diagram_tool_DoubleClickDescription class attributes and methods

# tool_ElementDoubleClickVariable class attributes and methods

# diagram_tool_DeleteHook class attributes and methods
diagram_tool_DeleteHook_id: Property = Property(name="id", type=StringType)
diagram_tool_DeleteHook.attributes={diagram_tool_DeleteHook_id}

# tool_DeleteHookParameter class attributes and methods

# diagram_tool_DeleteHookParameter class attributes and methods
diagram_tool_DeleteHookParameter_name: Property = Property(name="name", type=StringType)
diagram_tool_DeleteHookParameter_value: Property = Property(name="value", type=StringType)
diagram_tool_DeleteHookParameter.attributes={diagram_tool_DeleteHookParameter_value, diagram_tool_DeleteHookParameter_name}

# diagram_tool_DeleteElementDescription class attributes and methods
diagram_tool_DeleteElementDescription_m_getMappings: Method = Method(name="getMappings", parameters={}, type=StringType)
diagram_tool_DeleteElementDescription.methods={diagram_tool_DeleteElementDescription_m_getMappings}

# tool_ElementDeleteVariable class attributes and methods

# diagram_tool_ReconnectEdgeDescription class attributes and methods
diagram_tool_ReconnectEdgeDescription_reconnectionKind: Property = Property(name="reconnectionKind", type=StringType)
diagram_tool_ReconnectEdgeDescription_m_getMappings: Method = Method(name="getMappings", parameters={}, type=StringType)
diagram_tool_ReconnectEdgeDescription.attributes={diagram_tool_ReconnectEdgeDescription_reconnectionKind}
diagram_tool_ReconnectEdgeDescription.methods={diagram_tool_ReconnectEdgeDescription_m_getMappings}

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

# tool_ElementSelectVariable class attributes and methods

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

# diagram_tool_BehaviorTool class attributes and methods
diagram_tool_BehaviorTool_domainClass: Property = Property(name="domainClass", type=StringType)
diagram_tool_BehaviorTool.attributes={diagram_tool_BehaviorTool_domainClass}

# diagram_tool_CreateEdgeView class attributes and methods
diagram_tool_CreateEdgeView_sourceExpression: Property = Property(name="sourceExpression", type=StringType)
diagram_tool_CreateEdgeView_targetExpression: Property = Property(name="targetExpression", type=StringType)
diagram_tool_CreateEdgeView.attributes={diagram_tool_CreateEdgeView_targetExpression, diagram_tool_CreateEdgeView_sourceExpression}

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
diagram_tool_ContainerDropDescription_m_getBestMapping: Method = Method(name="getBestMapping", parameters={Parameter(name='targetContainer'), Parameter(name='droppedElement')}, type=StringType)
diagram_tool_ContainerDropDescription_m_getContainers: Method = Method(name="getContainers", parameters={}, type=StringType)
diagram_tool_ContainerDropDescription.attributes={diagram_tool_ContainerDropDescription_moveEdges, diagram_tool_ContainerDropDescription_dragSource}
diagram_tool_ContainerDropDescription.methods={diagram_tool_ContainerDropDescription_m_getContainers, diagram_tool_ContainerDropDescription_m_getBestMapping}

# tool_DropContainerVariable class attributes and methods

# tool_ElementDropVariable class attributes and methods

# tool_InitialContainerDropOperation class attributes and methods

# diagram_filter_MappingFilter class attributes and methods
diagram_filter_MappingFilter_semanticConditionExpression: Property = Property(name="semanticConditionExpression", type=StringType)
diagram_filter_MappingFilter_viewConditionExpression: Property = Property(name="viewConditionExpression", type=StringType)
diagram_filter_MappingFilter.attributes={diagram_filter_MappingFilter_viewConditionExpression, diagram_filter_MappingFilter_semanticConditionExpression}

# Filter class attributes and methods

# diagram_filter_FilterDescription class attributes and methods
diagram_filter_FilterDescription_m_isVisible: Method = Method(name="isVisible", parameters={Parameter(name='element')}, type=BooleanType)
diagram_filter_FilterDescription.methods={diagram_filter_FilterDescription_m_isVisible}

# diagram_filter_Filter class attributes and methods
diagram_filter_Filter_filterKind: Property = Property(name="filterKind", type=StringType)
diagram_filter_Filter_m_isVisible: Method = Method(name="isVisible", parameters={Parameter(name='element')}, type=BooleanType)
diagram_filter_Filter.attributes={diagram_filter_Filter_filterKind}
diagram_filter_Filter.methods={diagram_filter_Filter_m_isVisible}

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

# diagram_concern_ConcernDescription class attributes and methods

# Relationships
nodeListElements10: BinaryAssociation = BinaryAssociation(
    name="nodeListElements10",
    ends={
        Property(name="diagram_DNodeListElement", type=diagram_DDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagram11", type=diagram_DNodeListElement, multiplicity=Multiplicity(0, 9999))
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
activateBehaviors25: BinaryAssociation = BinaryAssociation(
    name="activateBehaviors25",
    ends={
        Property(name="tool_BehaviorTool", type=diagram_DDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagram26", type=tool_BehaviorTool, multiplicity=Multiplicity(0, 9999))
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
filterVariableHistory27: BinaryAssociation = BinaryAssociation(
    name="filterVariableHistory27",
    ends={
        Property(name="diagram_FilterVariableHistory", type=diagram_DDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagram28", type=diagram_FilterVariableHistory, multiplicity=Multiplicity(1, 1), is_composite=True)
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
nodes58: BinaryAssociation = BinaryAssociation(
    name="nodes58",
    ends={
        Property(name="diagram_DNode60", type=diagram_DDiagramElementContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagramElementContainer59", type=diagram_DNode, multiplicity=Multiplicity(0, 9999))
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
originalStyle100: BinaryAssociation = BinaryAssociation(
    name="originalStyle100",
    ends={
        Property(name="diagram_Style102", type=diagram_DEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DEdge101", type=diagram_Style, multiplicity=Multiplicity(0, 1))
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
variableDefinition118: BinaryAssociation = BinaryAssociation(
    name="variableDefinition118",
    ends={
        Property(name="TypedVariable", type=diagram_TypedVariableValue, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_TypedVariableValue", type=TypedVariable, multiplicity=Multiplicity(1, 1))
    }
)
allContainerMappings129: BinaryAssociation = BinaryAssociation(
    name="allContainerMappings129",
    ends={
        Property(name="ContainerMapping131", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription130", type=ContainerMapping, multiplicity=Multiplicity(0, 9999))
    }
)
validationSet132: BinaryAssociation = BinaryAssociation(
    name="validationSet132",
    ends={
        Property(name="validation_ValidationSet", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription133", type=validation_ValidationSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
concerns134: BinaryAssociation = BinaryAssociation(
    name="concerns134",
    ends={
        Property(name="concern_ConcernSet", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription135", type=concern_ConcernSet, multiplicity=Multiplicity(0, 1), is_composite=True)
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
allNodeMappings126: BinaryAssociation = BinaryAssociation(
    name="allNodeMappings126",
    ends={
        Property(name="NodeMapping128", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription127", type=NodeMapping, multiplicity=Multiplicity(0, 9999))
    }
)
init141: BinaryAssociation = BinaryAssociation(
    name="init141",
    ends={
        Property(name="tool_RepresentationCreationDescription", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription142", type=tool_RepresentationCreationDescription, multiplicity=Multiplicity(0, 1))
    }
)
layout143: BinaryAssociation = BinaryAssociation(
    name="layout143",
    ends={
        Property(name="Layout", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription144", type=Layout, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
diagramInitialisation145: BinaryAssociation = BinaryAssociation(
    name="diagramInitialisation145",
    ends={
        Property(name="tool_InitialOperation", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription146", type=tool_InitialOperation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
allTools136: BinaryAssociation = BinaryAssociation(
    name="allTools136",
    ends={
        Property(name="tool_AbstractToolDescription", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription137", type=tool_AbstractToolDescription, multiplicity=Multiplicity(0, 9999))
    }
)
defaultConcern138: BinaryAssociation = BinaryAssociation(
    name="defaultConcern138",
    ends={
        Property(name="concern_ConcernDescription140", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription139", type=concern_ConcernDescription, multiplicity=Multiplicity(0, 1))
    }
)
edgeMappings162: BinaryAssociation = BinaryAssociation(
    name="edgeMappings162",
    ends={
        Property(name="EdgeMapping164", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription163", type=EdgeMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edgeMappingImports165: BinaryAssociation = BinaryAssociation(
    name="edgeMappingImports165",
    ends={
        Property(name="EdgeMappingImport", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription166", type=EdgeMappingImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containerMappings167: BinaryAssociation = BinaryAssociation(
    name="containerMappings167",
    ends={
        Property(name="ContainerMapping169", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription168", type=ContainerMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultLayer147: BinaryAssociation = BinaryAssociation(
    name="defaultLayer147",
    ends={
        Property(name="Layer149", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription148", type=Layer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
additionalLayers150: BinaryAssociation = BinaryAssociation(
    name="additionalLayers150",
    ends={
        Property(name="AdditionalLayer152", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription151", type=AdditionalLayer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allLayers153: BinaryAssociation = BinaryAssociation(
    name="allLayers153",
    ends={
        Property(name="Layer155", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription154", type=Layer, multiplicity=Multiplicity(0, 9999))
    }
)
allActivatedTools156: BinaryAssociation = BinaryAssociation(
    name="allActivatedTools156",
    ends={
        Property(name="tool_AbstractToolDescription158", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription157", type=tool_AbstractToolDescription, multiplicity=Multiplicity(0, 9999))
    }
)
nodeMappings159: BinaryAssociation = BinaryAssociation(
    name="nodeMappings159",
    ends={
        Property(name="NodeMapping161", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription160", type=NodeMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedDiagram178: BinaryAssociation = BinaryAssociation(
    name="importedDiagram178",
    ends={
        Property(name="DiagramDescription179", type=diagram_description_DiagramImportDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramImportDescription", type=DiagramDescription, multiplicity=Multiplicity(0, 1))
    }
)
reusedMappings170: BinaryAssociation = BinaryAssociation(
    name="reusedMappings170",
    ends={
        Property(name="DiagramElementMapping172", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription171", type=DiagramElementMapping, multiplicity=Multiplicity(0, 9999))
    }
)
toolSection173: BinaryAssociation = BinaryAssociation(
    name="toolSection173",
    ends={
        Property(name="tool_ToolSection", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription174", type=tool_ToolSection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
reusedTools175: BinaryAssociation = BinaryAssociation(
    name="reusedTools175",
    ends={
        Property(name="tool_AbstractToolDescription177", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription176", type=tool_AbstractToolDescription, multiplicity=Multiplicity(0, 9999))
    }
)
layers180: BinaryAssociation = BinaryAssociation(
    name="layers180",
    ends={
        Property(name="AdditionalLayer181", type=diagram_description_DiagramExtensionDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramExtensionDescription", type=AdditionalLayer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
validationSet182: BinaryAssociation = BinaryAssociation(
    name="validationSet182",
    ends={
        Property(name="validation_ValidationSet184", type=diagram_description_DiagramExtensionDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramExtensionDescription183", type=validation_ValidationSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
concerns185: BinaryAssociation = BinaryAssociation(
    name="concerns185",
    ends={
        Property(name="concern_ConcernSet187", type=diagram_description_DiagramExtensionDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramExtensionDescription186", type=concern_ConcernSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
labelDirectEdit189: BinaryAssociation = BinaryAssociation(
    name="labelDirectEdit189",
    ends={
        Property(name="tool_DirectEditLabel", type=diagram_description_DiagramElementMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramElementMapping190", type=tool_DirectEditLabel, multiplicity=Multiplicity(0, 1))
    }
)
deletionDescription188: BinaryAssociation = BinaryAssociation(
    name="deletionDescription188",
    ends={
        Property(name="tool_DeleteElementDescription", type=diagram_description_DiagramElementMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramElementMapping", type=tool_DeleteElementDescription, multiplicity=Multiplicity(0, 1))
    }
)
doubleClickDescription191: BinaryAssociation = BinaryAssociation(
    name="doubleClickDescription191",
    ends={
        Property(name="description", type=diagram_description_DiagramElementMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="tool", type=tool_DoubleClickDescription, multiplicity=Multiplicity(0, 1))
    }
)
borderedNodeMappings192: BinaryAssociation = BinaryAssociation(
    name="borderedNodeMappings192",
    ends={
        Property(name="NodeMapping193", type=diagram_description_AbstractNodeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_AbstractNodeMapping", type=NodeMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reusedBorderedNodeMappings194: BinaryAssociation = BinaryAssociation(
    name="reusedBorderedNodeMappings194",
    ends={
        Property(name="NodeMapping196", type=diagram_description_AbstractNodeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_AbstractNodeMapping195", type=NodeMapping, multiplicity=Multiplicity(0, 9999))
    }
)
style197: BinaryAssociation = BinaryAssociation(
    name="style197",
    ends={
        Property(name="style_NodeStyleDescription", type=diagram_description_NodeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_NodeMapping", type=style_NodeStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditionnalStyles198: BinaryAssociation = BinaryAssociation(
    name="conditionnalStyles198",
    ends={
        Property(name="ConditionalNodeStyleDescription", type=diagram_description_NodeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_NodeMapping199", type=ConditionalNodeStyleDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reusedContainerMappings211: BinaryAssociation = BinaryAssociation(
    name="reusedContainerMappings211",
    ends={
        Property(name="ContainerMapping213", type=diagram_description_ContainerMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_ContainerMapping212", type=ContainerMapping, multiplicity=Multiplicity(0, 9999))
    }
)
allContainerMappings214: BinaryAssociation = BinaryAssociation(
    name="allContainerMappings214",
    ends={
        Property(name="ContainerMapping216", type=diagram_description_ContainerMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_ContainerMapping215", type=ContainerMapping, multiplicity=Multiplicity(0, 9999))
    }
)
style217: BinaryAssociation = BinaryAssociation(
    name="style217",
    ends={
        Property(name="style_ContainerStyleDescription", type=diagram_description_ContainerMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_ContainerMapping218", type=style_ContainerStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditionnalStyles219: BinaryAssociation = BinaryAssociation(
    name="conditionnalStyles219",
    ends={
        Property(name="ConditionalContainerStyleDescription", type=diagram_description_ContainerMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_ContainerMapping220", type=ConditionalContainerStyleDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subNodeMappings200: BinaryAssociation = BinaryAssociation(
    name="subNodeMappings200",
    ends={
        Property(name="NodeMapping201", type=diagram_description_ContainerMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_ContainerMapping", type=NodeMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allNodeMappings202: BinaryAssociation = BinaryAssociation(
    name="allNodeMappings202",
    ends={
        Property(name="NodeMapping204", type=diagram_description_ContainerMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_ContainerMapping203", type=NodeMapping, multiplicity=Multiplicity(0, 9999))
    }
)
reusedNodeMappings205: BinaryAssociation = BinaryAssociation(
    name="reusedNodeMappings205",
    ends={
        Property(name="NodeMapping207", type=diagram_description_ContainerMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_ContainerMapping206", type=NodeMapping, multiplicity=Multiplicity(0, 9999))
    }
)
subContainerMappings208: BinaryAssociation = BinaryAssociation(
    name="subContainerMappings208",
    ends={
        Property(name="ContainerMapping210", type=diagram_description_ContainerMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_ContainerMapping209", type=ContainerMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedMapping221: BinaryAssociation = BinaryAssociation(
    name="importedMapping221",
    ends={
        Property(name="NodeMapping222", type=diagram_description_NodeMappingImport, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_NodeMappingImport", type=NodeMapping, multiplicity=Multiplicity(1, 1))
    }
)
importedMapping223: BinaryAssociation = BinaryAssociation(
    name="importedMapping223",
    ends={
        Property(name="ContainerMapping224", type=diagram_description_ContainerMappingImport, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_ContainerMappingImport", type=ContainerMapping, multiplicity=Multiplicity(1, 1))
    }
)
sourceMapping225: BinaryAssociation = BinaryAssociation(
    name="sourceMapping225",
    ends={
        Property(name="DiagramElementMapping226", type=diagram_description_EdgeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_EdgeMapping", type=DiagramElementMapping, multiplicity=Multiplicity(1, 9999))
    }
)
targetMapping227: BinaryAssociation = BinaryAssociation(
    name="targetMapping227",
    ends={
        Property(name="DiagramElementMapping229", type=diagram_description_EdgeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_EdgeMapping228", type=DiagramElementMapping, multiplicity=Multiplicity(1, 9999))
    }
)
conditionnalStyles232: BinaryAssociation = BinaryAssociation(
    name="conditionnalStyles232",
    ends={
        Property(name="ConditionalEdgeStyleDescription", type=diagram_description_EdgeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_EdgeMapping233", type=ConditionalEdgeStyleDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
style230: BinaryAssociation = BinaryAssociation(
    name="style230",
    ends={
        Property(name="style_EdgeStyleDescription", type=diagram_description_EdgeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_EdgeMapping231", type=style_EdgeStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
importedMapping238: BinaryAssociation = BinaryAssociation(
    name="importedMapping238",
    ends={
        Property(name="IEdgeMapping239", type=diagram_description_EdgeMappingImport, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_EdgeMappingImport", type=IEdgeMapping, multiplicity=Multiplicity(1, 1))
    }
)
conditionnalStyles240: BinaryAssociation = BinaryAssociation(
    name="conditionnalStyles240",
    ends={
        Property(name="ConditionalEdgeStyleDescription242", type=diagram_description_EdgeMappingImport, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_EdgeMappingImport241", type=ConditionalEdgeStyleDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reconnections234: BinaryAssociation = BinaryAssociation(
    name="reconnections234",
    ends={
        Property(name="tool_ReconnectEdgeDescription", type=diagram_description_EdgeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_EdgeMapping235", type=tool_ReconnectEdgeDescription, multiplicity=Multiplicity(0, 9999))
    }
)
pathNodeMapping236: BinaryAssociation = BinaryAssociation(
    name="pathNodeMapping236",
    ends={
        Property(name="AbstractNodeMapping", type=diagram_description_EdgeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_EdgeMapping237", type=AbstractNodeMapping, multiplicity=Multiplicity(0, 9999))
    }
)
style247: BinaryAssociation = BinaryAssociation(
    name="style247",
    ends={
        Property(name="style_ContainerStyleDescription248", type=diagram_description_ConditionalContainerStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_ConditionalContainerStyleDescription", type=style_ContainerStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
style243: BinaryAssociation = BinaryAssociation(
    name="style243",
    ends={
        Property(name="style_NodeStyleDescription244", type=diagram_description_ConditionalNodeStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_ConditionalNodeStyleDescription", type=style_NodeStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
style245: BinaryAssociation = BinaryAssociation(
    name="style245",
    ends={
        Property(name="style_EdgeStyleDescription246", type=diagram_description_ConditionalEdgeStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_ConditionalEdgeStyleDescription", type=style_EdgeStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mappings251: BinaryAssociation = BinaryAssociation(
    name="mappings251",
    ends={
        Property(name="DiagramElementMapping252", type=diagram_description_MappingBasedDecoration, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_MappingBasedDecoration", type=DiagramElementMapping, multiplicity=Multiplicity(1, 9999))
    }
)
nodeMappings253: BinaryAssociation = BinaryAssociation(
    name="nodeMappings253",
    ends={
        Property(name="NodeMapping254", type=diagram_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_Layer", type=NodeMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodeMapping249: BinaryAssociation = BinaryAssociation(
    name="nodeMapping249",
    ends={
        Property(name="AbstractNodeMapping250", type=diagram_description_OrderedTreeLayout, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_OrderedTreeLayout", type=AbstractNodeMapping, multiplicity=Multiplicity(1, 9999))
    }
)
reusedMappings264: BinaryAssociation = BinaryAssociation(
    name="reusedMappings264",
    ends={
        Property(name="DiagramElementMapping266", type=diagram_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_Layer265", type=DiagramElementMapping, multiplicity=Multiplicity(0, 9999))
    }
)
allTools267: BinaryAssociation = BinaryAssociation(
    name="allTools267",
    ends={
        Property(name="tool_AbstractToolDescription269", type=diagram_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_Layer268", type=tool_AbstractToolDescription, multiplicity=Multiplicity(0, 9999))
    }
)
toolSections270: BinaryAssociation = BinaryAssociation(
    name="toolSections270",
    ends={
        Property(name="tool_ToolSection272", type=diagram_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_Layer271", type=tool_ToolSection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reusedTools273: BinaryAssociation = BinaryAssociation(
    name="reusedTools273",
    ends={
        Property(name="tool_AbstractToolDescription275", type=diagram_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_Layer274", type=tool_AbstractToolDescription, multiplicity=Multiplicity(0, 9999))
    }
)
edgeMappings255: BinaryAssociation = BinaryAssociation(
    name="edgeMappings255",
    ends={
        Property(name="EdgeMapping257", type=diagram_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_Layer256", type=EdgeMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edgeMappingImports258: BinaryAssociation = BinaryAssociation(
    name="edgeMappingImports258",
    ends={
        Property(name="EdgeMappingImport260", type=diagram_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_Layer259", type=EdgeMappingImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containerMappings261: BinaryAssociation = BinaryAssociation(
    name="containerMappings261",
    ends={
        Property(name="ContainerMapping263", type=diagram_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_Layer262", type=ContainerMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dropDescriptions283: BinaryAssociation = BinaryAssociation(
    name="dropDescriptions283",
    ends={
        Property(name="tool_ContainerDropDescription", type=diagram_description_DragAndDropTargetDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DragAndDropTargetDescription", type=tool_ContainerDropDescription, multiplicity=Multiplicity(0, 9999))
    }
)
decorationDescriptionsSet276: BinaryAssociation = BinaryAssociation(
    name="decorationDescriptionsSet276",
    ends={
        Property(name="DecorationDescriptionsSet", type=diagram_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_Layer277", type=DecorationDescriptionsSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
allEdgeMappings278: BinaryAssociation = BinaryAssociation(
    name="allEdgeMappings278",
    ends={
        Property(name="EdgeMapping280", type=diagram_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_Layer279", type=EdgeMapping, multiplicity=Multiplicity(0, 9999))
    }
)
customization281: BinaryAssociation = BinaryAssociation(
    name="customization281",
    ends={
        Property(name="Customization", type=diagram_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_Layer282", type=Customization, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
borderColor284: BinaryAssociation = BinaryAssociation(
    name="borderColor284",
    ends={
        Property(name="ColorDescription", type=diagram_style_BorderedStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_BorderedStyleDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
color285: BinaryAssociation = BinaryAssociation(
    name="color285",
    ends={
        Property(name="ColorDescription286", type=diagram_style_SquareDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_SquareDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
color287: BinaryAssociation = BinaryAssociation(
    name="color287",
    ends={
        Property(name="ColorDescription288", type=diagram_style_LozengeNodeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_LozengeNodeDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
color291: BinaryAssociation = BinaryAssociation(
    name="color291",
    ends={
        Property(name="ColorDescription292", type=diagram_style_BundledImageDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_BundledImageDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
color289: BinaryAssociation = BinaryAssociation(
    name="color289",
    ends={
        Property(name="ColorDescription290", type=diagram_style_EllipseNodeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_EllipseNodeDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
sections297: BinaryAssociation = BinaryAssociation(
    name="sections297",
    ends={
        Property(name="style_GaugeSectionDescription", type=diagram_style_GaugeCompositeStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_GaugeCompositeStyleDescription", type=style_GaugeSectionDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
color293: BinaryAssociation = BinaryAssociation(
    name="color293",
    ends={
        Property(name="ColorDescription294", type=diagram_style_NoteDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_NoteDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
backgroundColor295: BinaryAssociation = BinaryAssociation(
    name="backgroundColor295",
    ends={
        Property(name="ColorDescription296", type=diagram_style_DotDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_DotDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
foregroundColor300: BinaryAssociation = BinaryAssociation(
    name="foregroundColor300",
    ends={
        Property(name="ColorDescription302", type=diagram_style_GaugeSectionDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_GaugeSectionDescription301", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
backgroundColor298: BinaryAssociation = BinaryAssociation(
    name="backgroundColor298",
    ends={
        Property(name="ColorDescription299", type=diagram_style_GaugeSectionDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_GaugeSectionDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
backgroundColor303: BinaryAssociation = BinaryAssociation(
    name="backgroundColor303",
    ends={
        Property(name="ColorDescription304", type=diagram_style_FlatContainerStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_FlatContainerStyleDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
foregroundColor305: BinaryAssociation = BinaryAssociation(
    name="foregroundColor305",
    ends={
        Property(name="ColorDescription307", type=diagram_style_FlatContainerStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_FlatContainerStyleDescription306", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
strokeColor312: BinaryAssociation = BinaryAssociation(
    name="strokeColor312",
    ends={
        Property(name="ColorDescription313", type=diagram_style_EdgeStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_EdgeStyleDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
labelBorderStyle308: BinaryAssociation = BinaryAssociation(
    name="labelBorderStyle308",
    ends={
        Property(name="style_LabelBorderStyleDescription", type=diagram_style_FlatContainerStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_FlatContainerStyleDescription309", type=style_LabelBorderStyleDescription, multiplicity=Multiplicity(0, 1))
    }
)
backgroundColor310: BinaryAssociation = BinaryAssociation(
    name="backgroundColor310",
    ends={
        Property(name="ColorDescription311", type=diagram_style_ShapeContainerStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_ShapeContainerStyleDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
beginLabelStyleDescription314: BinaryAssociation = BinaryAssociation(
    name="beginLabelStyleDescription314",
    ends={
        Property(name="style_BeginLabelStyleDescription", type=diagram_style_EdgeStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_EdgeStyleDescription315", type=style_BeginLabelStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
centerLabelStyleDescription316: BinaryAssociation = BinaryAssociation(
    name="centerLabelStyleDescription316",
    ends={
        Property(name="style_CenterLabelStyleDescription", type=diagram_style_EdgeStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_EdgeStyleDescription317", type=style_CenterLabelStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
endLabelStyleDescription318: BinaryAssociation = BinaryAssociation(
    name="endLabelStyleDescription318",
    ends={
        Property(name="style_EndLabelStyleDescription", type=diagram_style_EdgeStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_EdgeStyleDescription319", type=style_EndLabelStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
centeredSourceMappings320: BinaryAssociation = BinaryAssociation(
    name="centeredSourceMappings320",
    ends={
        Property(name="DiagramElementMapping322", type=diagram_style_EdgeStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_EdgeStyleDescription321", type=DiagramElementMapping, multiplicity=Multiplicity(0, 9999))
    }
)
centeredTargetMappings323: BinaryAssociation = BinaryAssociation(
    name="centeredTargetMappings323",
    ends={
        Property(name="DiagramElementMapping325", type=diagram_style_EdgeStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_EdgeStyleDescription324", type=DiagramElementMapping, multiplicity=Multiplicity(0, 9999))
    }
)
popupMenus330: BinaryAssociation = BinaryAssociation(
    name="popupMenus330",
    ends={
        Property(name="tool_PopupMenu", type=diagram_tool_ToolSection, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ToolSection331", type=tool_PopupMenu, multiplicity=Multiplicity(0, 9999))
    }
)
reusedTools332: BinaryAssociation = BinaryAssociation(
    name="reusedTools332",
    ends={
        Property(name="tool_ToolEntry334", type=diagram_tool_ToolSection, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ToolSection333", type=tool_ToolEntry, multiplicity=Multiplicity(0, 9999))
    }
)
groupExtensions335: BinaryAssociation = BinaryAssociation(
    name="groupExtensions335",
    ends={
        Property(name="tool_ToolGroupExtension", type=diagram_tool_ToolSection, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ToolSection336", type=tool_ToolGroupExtension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tools337: BinaryAssociation = BinaryAssociation(
    name="tools337",
    ends={
        Property(name="tool_AbstractToolDescription338", type=diagram_tool_ToolGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ToolGroup", type=tool_AbstractToolDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedTools326: BinaryAssociation = BinaryAssociation(
    name="ownedTools326",
    ends={
        Property(name="tool_ToolEntry", type=diagram_tool_ToolSection, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ToolSection", type=tool_ToolEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subSections327: BinaryAssociation = BinaryAssociation(
    name="subSections327",
    ends={
        Property(name="tool_ToolSection329", type=diagram_tool_ToolSection, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ToolSection328", type=tool_ToolSection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable345: BinaryAssociation = BinaryAssociation(
    name="variable345",
    ends={
        Property(name="tool_NodeCreationVariable", type=diagram_tool_NodeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_NodeCreationDescription346", type=tool_NodeCreationVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
viewVariable347: BinaryAssociation = BinaryAssociation(
    name="viewVariable347",
    ends={
        Property(name="tool_ContainerViewVariable", type=diagram_tool_NodeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_NodeCreationDescription348", type=tool_ContainerViewVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
group339: BinaryAssociation = BinaryAssociation(
    name="group339",
    ends={
        Property(name="tool_ToolGroup", type=diagram_tool_ToolGroupExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ToolGroupExtension", type=tool_ToolGroup, multiplicity=Multiplicity(1, 1))
    }
)
tools340: BinaryAssociation = BinaryAssociation(
    name="tools340",
    ends={
        Property(name="tool_AbstractToolDescription342", type=diagram_tool_ToolGroupExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ToolGroupExtension341", type=tool_AbstractToolDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodeMappings343: BinaryAssociation = BinaryAssociation(
    name="nodeMappings343",
    ends={
        Property(name="NodeMapping344", type=diagram_tool_NodeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_NodeCreationDescription", type=NodeMapping, multiplicity=Multiplicity(1, 9999))
    }
)
initialOperation349: BinaryAssociation = BinaryAssociation(
    name="initialOperation349",
    ends={
        Property(name="tool_InitialNodeCreationOperation", type=diagram_tool_NodeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_NodeCreationDescription350", type=tool_InitialNodeCreationOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
extraMappings351: BinaryAssociation = BinaryAssociation(
    name="extraMappings351",
    ends={
        Property(name="AbstractNodeMapping353", type=diagram_tool_NodeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_NodeCreationDescription352", type=AbstractNodeMapping, multiplicity=Multiplicity(0, 9999))
    }
)
sourceViewVariable360: BinaryAssociation = BinaryAssociation(
    name="sourceViewVariable360",
    ends={
        Property(name="diagram_tool_EdgeCreationDescription361", type=tool_SourceEdgeViewCreationVariable, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="tool_SourceEdgeViewCreationVariable", type=diagram_tool_EdgeCreationDescription, multiplicity=Multiplicity(1, 1))
    }
)
targetViewVariable362: BinaryAssociation = BinaryAssociation(
    name="targetViewVariable362",
    ends={
        Property(name="tool_TargetEdgeViewCreationVariable", type=diagram_tool_EdgeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_EdgeCreationDescription363", type=tool_TargetEdgeViewCreationVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
edgeMappings354: BinaryAssociation = BinaryAssociation(
    name="edgeMappings354",
    ends={
        Property(name="EdgeMapping355", type=diagram_tool_EdgeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_EdgeCreationDescription", type=EdgeMapping, multiplicity=Multiplicity(1, 9999))
    }
)
sourceVariable356: BinaryAssociation = BinaryAssociation(
    name="sourceVariable356",
    ends={
        Property(name="tool_SourceEdgeCreationVariable", type=diagram_tool_EdgeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_EdgeCreationDescription357", type=tool_SourceEdgeCreationVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
targetVariable358: BinaryAssociation = BinaryAssociation(
    name="targetVariable358",
    ends={
        Property(name="tool_TargetEdgeCreationVariable", type=diagram_tool_EdgeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_EdgeCreationDescription359", type=tool_TargetEdgeCreationVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
containerMappings372: BinaryAssociation = BinaryAssociation(
    name="containerMappings372",
    ends={
        Property(name="ContainerMapping373", type=diagram_tool_ContainerCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ContainerCreationDescription", type=ContainerMapping, multiplicity=Multiplicity(1, 9999))
    }
)
variable374: BinaryAssociation = BinaryAssociation(
    name="variable374",
    ends={
        Property(name="tool_NodeCreationVariable376", type=diagram_tool_ContainerCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ContainerCreationDescription375", type=tool_NodeCreationVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
viewVariable377: BinaryAssociation = BinaryAssociation(
    name="viewVariable377",
    ends={
        Property(name="tool_ContainerViewVariable379", type=diagram_tool_ContainerCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ContainerCreationDescription378", type=tool_ContainerViewVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialOperation380: BinaryAssociation = BinaryAssociation(
    name="initialOperation380",
    ends={
        Property(name="tool_InitialNodeCreationOperation382", type=diagram_tool_ContainerCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ContainerCreationDescription381", type=tool_InitialNodeCreationOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialOperation364: BinaryAssociation = BinaryAssociation(
    name="initialOperation364",
    ends={
        Property(name="tool_InitEdgeCreationOperation", type=diagram_tool_EdgeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_EdgeCreationDescription365", type=tool_InitEdgeCreationOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
extraSourceMappings366: BinaryAssociation = BinaryAssociation(
    name="extraSourceMappings366",
    ends={
        Property(name="DiagramElementMapping368", type=diagram_tool_EdgeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_EdgeCreationDescription367", type=DiagramElementMapping, multiplicity=Multiplicity(0, 9999))
    }
)
extraTargetMappings369: BinaryAssociation = BinaryAssociation(
    name="extraTargetMappings369",
    ends={
        Property(name="DiagramElementMapping371", type=diagram_tool_EdgeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_EdgeCreationDescription370", type=DiagramElementMapping, multiplicity=Multiplicity(0, 9999))
    }
)
hook396: BinaryAssociation = BinaryAssociation(
    name="hook396",
    ends={
        Property(name="tool_DeleteHook", type=diagram_tool_DeleteElementDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DeleteElementDescription397", type=tool_DeleteHook, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mappings398: BinaryAssociation = BinaryAssociation(
    name="mappings398",
    ends={
        Property(name="description400", type=diagram_tool_DoubleClickDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="DiagramElementMapping399", type=DiagramElementMapping, multiplicity=Multiplicity(1, 9999))
    }
)
element401: BinaryAssociation = BinaryAssociation(
    name="element401",
    ends={
        Property(name="tool_ElementDoubleClickVariable", type=diagram_tool_DoubleClickDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DoubleClickDescription", type=tool_ElementDoubleClickVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elementView402: BinaryAssociation = BinaryAssociation(
    name="elementView402",
    ends={
        Property(name="tool_ElementDoubleClickVariable404", type=diagram_tool_DoubleClickDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DoubleClickDescription403", type=tool_ElementDoubleClickVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initialOperation405: BinaryAssociation = BinaryAssociation(
    name="initialOperation405",
    ends={
        Property(name="tool_InitialOperation407", type=diagram_tool_DoubleClickDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DoubleClickDescription406", type=tool_InitialOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters408: BinaryAssociation = BinaryAssociation(
    name="parameters408",
    ends={
        Property(name="tool_DeleteHookParameter", type=diagram_tool_DeleteHook, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DeleteHook", type=tool_DeleteHookParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extraMappings383: BinaryAssociation = BinaryAssociation(
    name="extraMappings383",
    ends={
        Property(name="AbstractNodeMapping385", type=diagram_tool_ContainerCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ContainerCreationDescription384", type=AbstractNodeMapping, multiplicity=Multiplicity(0, 9999))
    }
)
element386: BinaryAssociation = BinaryAssociation(
    name="element386",
    ends={
        Property(name="tool_ElementDeleteVariable", type=diagram_tool_DeleteElementDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DeleteElementDescription", type=tool_ElementDeleteVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elementView387: BinaryAssociation = BinaryAssociation(
    name="elementView387",
    ends={
        Property(name="tool_ElementDeleteVariable389", type=diagram_tool_DeleteElementDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DeleteElementDescription388", type=tool_ElementDeleteVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
containerView390: BinaryAssociation = BinaryAssociation(
    name="containerView390",
    ends={
        Property(name="tool_ContainerViewVariable392", type=diagram_tool_DeleteElementDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DeleteElementDescription391", type=tool_ContainerViewVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialOperation393: BinaryAssociation = BinaryAssociation(
    name="initialOperation393",
    ends={
        Property(name="tool_InitialOperation395", type=diagram_tool_DeleteElementDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DeleteElementDescription394", type=tool_InitialOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target411: BinaryAssociation = BinaryAssociation(
    name="target411",
    ends={
        Property(name="tool_TargetEdgeCreationVariable413", type=diagram_tool_ReconnectEdgeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ReconnectEdgeDescription412", type=tool_TargetEdgeCreationVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sourceView414: BinaryAssociation = BinaryAssociation(
    name="sourceView414",
    ends={
        Property(name="tool_SourceEdgeViewCreationVariable416", type=diagram_tool_ReconnectEdgeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ReconnectEdgeDescription415", type=tool_SourceEdgeViewCreationVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
targetView417: BinaryAssociation = BinaryAssociation(
    name="targetView417",
    ends={
        Property(name="tool_TargetEdgeViewCreationVariable419", type=diagram_tool_ReconnectEdgeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ReconnectEdgeDescription418", type=tool_TargetEdgeViewCreationVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source409: BinaryAssociation = BinaryAssociation(
    name="source409",
    ends={
        Property(name="tool_SourceEdgeCreationVariable410", type=diagram_tool_ReconnectEdgeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ReconnectEdgeDescription", type=tool_SourceEdgeCreationVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mask428: BinaryAssociation = BinaryAssociation(
    name="mask428",
    ends={
        Property(name="tool_EditMaskVariables", type=diagram_tool_DirectEditLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DirectEditLabel", type=tool_EditMaskVariables, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
element420: BinaryAssociation = BinaryAssociation(
    name="element420",
    ends={
        Property(name="tool_ElementSelectVariable", type=diagram_tool_ReconnectEdgeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ReconnectEdgeDescription421", type=tool_ElementSelectVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialOperation422: BinaryAssociation = BinaryAssociation(
    name="initialOperation422",
    ends={
        Property(name="tool_InitialOperation424", type=diagram_tool_ReconnectEdgeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ReconnectEdgeDescription423", type=tool_InitialOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
edgeView425: BinaryAssociation = BinaryAssociation(
    name="edgeView425",
    ends={
        Property(name="tool_ElementSelectVariable427", type=diagram_tool_ReconnectEdgeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ReconnectEdgeDescription426", type=tool_ElementSelectVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialOperation432: BinaryAssociation = BinaryAssociation(
    name="initialOperation432",
    ends={
        Property(name="tool_InitialOperation433", type=diagram_tool_BehaviorTool, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_BehaviorTool", type=tool_InitialOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialOperation429: BinaryAssociation = BinaryAssociation(
    name="initialOperation429",
    ends={
        Property(name="tool_InitialOperation431", type=diagram_tool_DirectEditLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DirectEditLabel430", type=tool_InitialOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mapping434: BinaryAssociation = BinaryAssociation(
    name="mapping434",
    ends={
        Property(name="DiagramElementMapping435", type=diagram_tool_CreateView, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_CreateView", type=DiagramElementMapping, multiplicity=Multiplicity(1, 1))
    }
)
diagramDescription436: BinaryAssociation = BinaryAssociation(
    name="diagramDescription436",
    ends={
        Property(name="DiagramDescription437", type=diagram_tool_Navigation, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_Navigation", type=DiagramDescription, multiplicity=Multiplicity(1, 1))
    }
)
diagramDescription438: BinaryAssociation = BinaryAssociation(
    name="diagramDescription438",
    ends={
        Property(name="DiagramDescription439", type=diagram_tool_DiagramCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DiagramCreationDescription", type=DiagramDescription, multiplicity=Multiplicity(1, 1))
    }
)
diagramDescription440: BinaryAssociation = BinaryAssociation(
    name="diagramDescription440",
    ends={
        Property(name="DiagramDescription441", type=diagram_tool_DiagramNavigationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DiagramNavigationDescription", type=DiagramDescription, multiplicity=Multiplicity(1, 1))
    }
)
initialOperation454: BinaryAssociation = BinaryAssociation(
    name="initialOperation454",
    ends={
        Property(name="tool_InitialContainerDropOperation", type=diagram_tool_ContainerDropDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ContainerDropDescription455", type=tool_InitialContainerDropOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mappings442: BinaryAssociation = BinaryAssociation(
    name="mappings442",
    ends={
        Property(name="DiagramElementMapping443", type=diagram_tool_ContainerDropDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ContainerDropDescription", type=DiagramElementMapping, multiplicity=Multiplicity(0, 9999))
    }
)
oldContainer444: BinaryAssociation = BinaryAssociation(
    name="oldContainer444",
    ends={
        Property(name="tool_DropContainerVariable", type=diagram_tool_ContainerDropDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ContainerDropDescription445", type=tool_DropContainerVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
newContainer446: BinaryAssociation = BinaryAssociation(
    name="newContainer446",
    ends={
        Property(name="tool_DropContainerVariable448", type=diagram_tool_ContainerDropDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ContainerDropDescription447", type=tool_DropContainerVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
element449: BinaryAssociation = BinaryAssociation(
    name="element449",
    ends={
        Property(name="tool_ElementDropVariable", type=diagram_tool_ContainerDropDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ContainerDropDescription450", type=tool_ElementDropVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
newViewContainer451: BinaryAssociation = BinaryAssociation(
    name="newViewContainer451",
    ends={
        Property(name="tool_ContainerViewVariable453", type=diagram_tool_ContainerDropDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ContainerDropDescription452", type=tool_ContainerViewVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mappings456: BinaryAssociation = BinaryAssociation(
    name="mappings456",
    ends={
        Property(name="DiagramElementMapping457", type=diagram_filter_MappingFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_filter_MappingFilter", type=DiagramElementMapping, multiplicity=Multiplicity(0, 9999))
    }
)
filters458: BinaryAssociation = BinaryAssociation(
    name="filters458",
    ends={
        Property(name="filter_Filter", type=diagram_filter_CompositeFilterDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_filter_CompositeFilterDescription", type=filter_Filter, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ownedVariables459: BinaryAssociation = BinaryAssociation(
    name="ownedVariables459",
    ends={
        Property(name="InteractiveVariableDescription", type=diagram_filter_VariableFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_filter_VariableFilter", type=InteractiveVariableDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedConcernDescriptions460: BinaryAssociation = BinaryAssociation(
    name="ownedConcernDescriptions460",
    ends={
        Property(name="concern_ConcernDescription461", type=diagram_concern_ConcernSet, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_concern_ConcernSet", type=concern_ConcernDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
filters462: BinaryAssociation = BinaryAssociation(
    name="filters462",
    ends={
        Property(name="filter_FilterDescription463", type=diagram_concern_ConcernDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_concern_ConcernDescription", type=filter_FilterDescription, multiplicity=Multiplicity(0, 9999))
    }
)
rules464: BinaryAssociation = BinaryAssociation(
    name="rules464",
    ends={
        Property(name="validation_ValidationRule466", type=diagram_concern_ConcernDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_concern_ConcernDescription465", type=validation_ValidationRule, multiplicity=Multiplicity(0, 9999))
    }
)
behaviors467: BinaryAssociation = BinaryAssociation(
    name="behaviors467",
    ends={
        Property(name="tool_BehaviorTool469", type=diagram_concern_ConcernDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_concern_ConcernDescription468", type=tool_BehaviorTool, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_diagram_DDiagram_DRepresentation = Generalization(general=DRepresentation, specific=diagram_DDiagram)
gen_diagram_DDiagram_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=diagram_DDiagram)
gen_diagram_DDiagram_DragAndDropTarget = Generalization(general=DragAndDropTarget, specific=diagram_DDiagram)
gen_diagram_DSemanticDiagram_DDiagram = Generalization(general=DDiagram, specific=diagram_DSemanticDiagram)
gen_diagram_DSemanticDiagram_DSemanticDecorator = Generalization(general=DSemanticDecorator, specific=diagram_DSemanticDiagram)
gen_diagram_DDiagramElement_DRepresentationElement = Generalization(general=DRepresentationElement, specific=diagram_DDiagramElement)
gen_diagram_FoldingPointFilter_GraphicalFilter = Generalization(general=GraphicalFilter, specific=diagram_FoldingPointFilter)
gen_diagram_FoldingFilter_GraphicalFilter = Generalization(general=GraphicalFilter, specific=diagram_FoldingFilter)
gen_diagram_HideFilter_GraphicalFilter = Generalization(general=GraphicalFilter, specific=diagram_HideFilter)
gen_diagram_HideLabelFilter_GraphicalFilter = Generalization(general=GraphicalFilter, specific=diagram_HideLabelFilter)
gen_diagram_DNode_EdgeTarget = Generalization(general=EdgeTarget, specific=diagram_DNode)
gen_diagram_DNode_DragAndDropTarget = Generalization(general=DragAndDropTarget, specific=diagram_DNode)
gen_diagram_AppliedCompositeFilters_GraphicalFilter = Generalization(general=GraphicalFilter, specific=diagram_AppliedCompositeFilters)
gen_diagram_AbsoluteBoundsFilter_GraphicalFilter = Generalization(general=GraphicalFilter, specific=diagram_AbsoluteBoundsFilter)
gen_diagram_AbstractDNode_DDiagramElement = Generalization(general=DDiagramElement, specific=diagram_AbstractDNode)
gen_diagram_DNode_AbstractDNode = Generalization(general=AbstractDNode, specific=diagram_DNode)
gen_diagram_DDiagramElementContainer_AbstractDNode = Generalization(general=AbstractDNode, specific=diagram_DDiagramElementContainer)
gen_diagram_DDiagramElementContainer_EdgeTarget = Generalization(general=EdgeTarget, specific=diagram_DDiagramElementContainer)
gen_diagram_DDiagramElementContainer_DragAndDropTarget = Generalization(general=DragAndDropTarget, specific=diagram_DDiagramElementContainer)
gen_diagram_DNodeList_DDiagramElementContainer = Generalization(general=DDiagramElementContainer, specific=diagram_DNodeList)
gen_diagram_DNodeContainer_DDiagramElementContainer = Generalization(general=DDiagramElementContainer, specific=diagram_DNodeContainer)
gen_diagram_DEdge_DDiagramElement = Generalization(general=DDiagramElement, specific=diagram_DEdge)
gen_diagram_DEdge_EdgeTarget = Generalization(general=EdgeTarget, specific=diagram_DEdge)
gen_diagram_DNodeListElement_AbstractDNode = Generalization(general=AbstractDNode, specific=diagram_DNodeListElement)
gen_diagram_NodeStyle_LabelStyle = Generalization(general=LabelStyle, specific=diagram_NodeStyle)
gen_diagram_NodeStyle_Style = Generalization(general=Style, specific=diagram_NodeStyle)
gen_diagram_NodeStyle_BorderedStyle = Generalization(general=BorderedStyle, specific=diagram_NodeStyle)
gen_diagram_NodeStyle_HideLabelCapabilityStyle = Generalization(general=HideLabelCapabilityStyle, specific=diagram_NodeStyle)
gen_diagram_ContainerStyle_LabelStyle = Generalization(general=LabelStyle, specific=diagram_ContainerStyle)
gen_diagram_Dot_NodeStyle = Generalization(general=NodeStyle, specific=diagram_Dot)
gen_diagram_ContainerStyle_Style = Generalization(general=Style, specific=diagram_ContainerStyle)
gen_diagram_ContainerStyle_BorderedStyle = Generalization(general=BorderedStyle, specific=diagram_ContainerStyle)
gen_diagram_ContainerStyle_HideLabelCapabilityStyle = Generalization(general=HideLabelCapabilityStyle, specific=diagram_ContainerStyle)
gen_diagram_FlatContainerStyle_ContainerStyle = Generalization(general=ContainerStyle, specific=diagram_FlatContainerStyle)
gen_diagram_GaugeSection_Customizable = Generalization(general=Customizable, specific=diagram_GaugeSection)
gen_diagram_Square_NodeStyle = Generalization(general=NodeStyle, specific=diagram_Square)
gen_diagram_Ellipse_NodeStyle = Generalization(general=NodeStyle, specific=diagram_Ellipse)
gen_diagram_ShapeContainerStyle_ContainerStyle = Generalization(general=ContainerStyle, specific=diagram_ShapeContainerStyle)
gen_diagram_Lozenge_NodeStyle = Generalization(general=NodeStyle, specific=diagram_Lozenge)
gen_diagram_BundledImage_NodeStyle = Generalization(general=NodeStyle, specific=diagram_BundledImage)
gen_diagram_WorkspaceImage_NodeStyle = Generalization(general=NodeStyle, specific=diagram_WorkspaceImage)
gen_diagram_WorkspaceImage_ContainerStyle = Generalization(general=ContainerStyle, specific=diagram_WorkspaceImage)
gen_diagram_CustomStyle_NodeStyle = Generalization(general=NodeStyle, specific=diagram_CustomStyle)
gen_diagram_EdgeStyle_Style = Generalization(general=Style, specific=diagram_EdgeStyle)
gen_diagram_BorderedStyle_Style = Generalization(general=Style, specific=diagram_BorderedStyle)
gen_diagram_GaugeCompositeStyle_NodeStyle = Generalization(general=NodeStyle, specific=diagram_GaugeCompositeStyle)
gen_diagram_CollapseFilter_GraphicalFilter = Generalization(general=GraphicalFilter, specific=diagram_CollapseFilter)
gen_diagram_Note_NodeStyle = Generalization(general=NodeStyle, specific=diagram_Note)
gen_diagram_EndLabelStyle_BasicLabelStyle = Generalization(general=BasicLabelStyle, specific=diagram_EndLabelStyle)
gen_diagram_BracketEdgeStyle_EdgeStyle = Generalization(general=EdgeStyle, specific=diagram_BracketEdgeStyle)
gen_diagram_IndirectlyCollapseFilter_CollapseFilter = Generalization(general=CollapseFilter, specific=diagram_IndirectlyCollapseFilter)
gen_diagram_BeginLabelStyle_BasicLabelStyle = Generalization(general=BasicLabelStyle, specific=diagram_BeginLabelStyle)
gen_diagram_CenterLabelStyle_BasicLabelStyle = Generalization(general=BasicLabelStyle, specific=diagram_CenterLabelStyle)
gen_diagram_description_DiagramDescription_description_DragAndDropTargetDescription = Generalization(general=description_DragAndDropTargetDescription, specific=diagram_description_DiagramDescription)
gen_diagram_description_DiagramDescription_description_RepresentationDescription = Generalization(general=description_RepresentationDescription, specific=diagram_description_DiagramDescription)
gen_diagram_description_DiagramDescription_description_PasteTargetDescription = Generalization(general=description_PasteTargetDescription, specific=diagram_description_DiagramDescription)
gen_diagram_TypedVariableValue_VariableValue = Generalization(general=VariableValue, specific=diagram_TypedVariableValue)
gen_diagram_EObjectVariableValue_VariableValue = Generalization(general=VariableValue, specific=diagram_EObjectVariableValue)
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
gen_diagram_description_EdgeMapping_description_DiagramElementMapping = Generalization(general=description_DiagramElementMapping, specific=diagram_description_EdgeMapping)
gen_diagram_description_EdgeMapping_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=diagram_description_EdgeMapping)
gen_diagram_description_EdgeMapping_description_IEdgeMapping = Generalization(general=description_IEdgeMapping, specific=diagram_description_EdgeMapping)
gen_diagram_description_NodeMappingImport_description_NodeMapping = Generalization(general=description_NodeMapping, specific=diagram_description_NodeMappingImport)
gen_diagram_description_NodeMappingImport_description_AbstractMappingImport = Generalization(general=description_AbstractMappingImport, specific=diagram_description_NodeMappingImport)
gen_diagram_description_ContainerMappingImport_description_ContainerMapping = Generalization(general=description_ContainerMapping, specific=diagram_description_ContainerMappingImport)
gen_diagram_description_ContainerMappingImport_description_AbstractMappingImport = Generalization(general=description_AbstractMappingImport, specific=diagram_description_ContainerMappingImport)
gen_diagram_description_EdgeMappingImport_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=diagram_description_EdgeMappingImport)
gen_diagram_description_EdgeMappingImport_description_IEdgeMapping = Generalization(general=description_IEdgeMapping, specific=diagram_description_EdgeMappingImport)
gen_diagram_description_EdgeMappingImport_description_IdentifiedElement = Generalization(general=description_IdentifiedElement, specific=diagram_description_EdgeMappingImport)
gen_diagram_description_ConditionalContainerStyleDescription_ConditionalStyleDescription = Generalization(general=ConditionalStyleDescription, specific=diagram_description_ConditionalContainerStyleDescription)
gen_diagram_description_Layout_DocumentedElement = Generalization(general=DocumentedElement, specific=diagram_description_Layout)
gen_diagram_description_OrderedTreeLayout_Layout = Generalization(general=Layout, specific=diagram_description_OrderedTreeLayout)
gen_diagram_description_ConditionalNodeStyleDescription_ConditionalStyleDescription = Generalization(general=ConditionalStyleDescription, specific=diagram_description_ConditionalNodeStyleDescription)
gen_diagram_description_ConditionalEdgeStyleDescription_ConditionalStyleDescription = Generalization(general=ConditionalStyleDescription, specific=diagram_description_ConditionalEdgeStyleDescription)
gen_diagram_description_MappingBasedDecoration_DecorationDescription = Generalization(general=DecorationDescription, specific=diagram_description_MappingBasedDecoration)
gen_diagram_description_Layer_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=diagram_description_Layer)
gen_diagram_description_Layer_description_EndUserDocumentedElement = Generalization(general=description_EndUserDocumentedElement, specific=diagram_description_Layer)
gen_diagram_description_Layer_description_IdentifiedElement = Generalization(general=description_IdentifiedElement, specific=diagram_description_Layer)
gen_diagram_description_CompositeLayout_Layout = Generalization(general=Layout, specific=diagram_description_CompositeLayout)
gen_diagram_description_AdditionalLayer_Layer = Generalization(general=Layer, specific=diagram_description_AdditionalLayer)
gen_diagram_style_BorderedStyleDescription_StyleDescription = Generalization(general=StyleDescription, specific=diagram_style_BorderedStyleDescription)
gen_diagram_style_NodeStyleDescription_style_LabelStyleDescription = Generalization(general=style_LabelStyleDescription, specific=diagram_style_NodeStyleDescription)
gen_diagram_style_NodeStyleDescription_style_TooltipStyleDescription = Generalization(general=style_TooltipStyleDescription, specific=diagram_style_NodeStyleDescription)
gen_diagram_style_NodeStyleDescription_style_HideLabelCapabilityStyleDescription = Generalization(general=style_HideLabelCapabilityStyleDescription, specific=diagram_style_NodeStyleDescription)
gen_diagram_style_NodeStyleDescription_style_StyleDescription = Generalization(general=style_StyleDescription, specific=diagram_style_NodeStyleDescription)
gen_diagram_style_NodeStyleDescription_style_BorderedStyleDescription = Generalization(general=style_BorderedStyleDescription, specific=diagram_style_NodeStyleDescription)
gen_diagram_style_LozengeNodeDescription_NodeStyleDescription = Generalization(general=NodeStyleDescription, specific=diagram_style_LozengeNodeDescription)
gen_diagram_style_CustomStyleDescription_NodeStyleDescription = Generalization(general=NodeStyleDescription, specific=diagram_style_CustomStyleDescription)
gen_diagram_style_SquareDescription_NodeStyleDescription = Generalization(general=NodeStyleDescription, specific=diagram_style_SquareDescription)
gen_diagram_style_BundledImageDescription_NodeStyleDescription = Generalization(general=NodeStyleDescription, specific=diagram_style_BundledImageDescription)
gen_diagram_style_NoteDescription_NodeStyleDescription = Generalization(general=NodeStyleDescription, specific=diagram_style_NoteDescription)
gen_diagram_style_EllipseNodeDescription_NodeStyleDescription = Generalization(general=NodeStyleDescription, specific=diagram_style_EllipseNodeDescription)
gen_diagram_style_GaugeCompositeStyleDescription_NodeStyleDescription = Generalization(general=NodeStyleDescription, specific=diagram_style_GaugeCompositeStyleDescription)
gen_diagram_style_DotDescription_NodeStyleDescription = Generalization(general=NodeStyleDescription, specific=diagram_style_DotDescription)
gen_diagram_style_FlatContainerStyleDescription_style_ContainerStyleDescription = Generalization(general=style_ContainerStyleDescription, specific=diagram_style_FlatContainerStyleDescription)
gen_diagram_style_FlatContainerStyleDescription_style_SizeComputationContainerStyleDescription = Generalization(general=style_SizeComputationContainerStyleDescription, specific=diagram_style_FlatContainerStyleDescription)
gen_diagram_style_RoundedCornerStyleDescription_StyleDescription = Generalization(general=StyleDescription, specific=diagram_style_RoundedCornerStyleDescription)
gen_diagram_style_ContainerStyleDescription_style_RoundedCornerStyleDescription = Generalization(general=style_RoundedCornerStyleDescription, specific=diagram_style_ContainerStyleDescription)
gen_diagram_style_ContainerStyleDescription_style_BorderedStyleDescription = Generalization(general=style_BorderedStyleDescription, specific=diagram_style_ContainerStyleDescription)
gen_diagram_style_ContainerStyleDescription_style_LabelStyleDescription = Generalization(general=style_LabelStyleDescription, specific=diagram_style_ContainerStyleDescription)
gen_diagram_style_ContainerStyleDescription_style_TooltipStyleDescription = Generalization(general=style_TooltipStyleDescription, specific=diagram_style_ContainerStyleDescription)
gen_diagram_style_ContainerStyleDescription_style_HideLabelCapabilityStyleDescription = Generalization(general=style_HideLabelCapabilityStyleDescription, specific=diagram_style_ContainerStyleDescription)
gen_diagram_style_WorkspaceImageDescription_style_ContainerStyleDescription = Generalization(general=style_ContainerStyleDescription, specific=diagram_style_WorkspaceImageDescription)
gen_diagram_style_EdgeStyleDescription_StyleDescription = Generalization(general=StyleDescription, specific=diagram_style_EdgeStyleDescription)
gen_diagram_style_ShapeContainerStyleDescription_style_ContainerStyleDescription = Generalization(general=style_ContainerStyleDescription, specific=diagram_style_ShapeContainerStyleDescription)
gen_diagram_style_ShapeContainerStyleDescription_style_SizeComputationContainerStyleDescription = Generalization(general=style_SizeComputationContainerStyleDescription, specific=diagram_style_ShapeContainerStyleDescription)
gen_diagram_style_WorkspaceImageDescription_style_NodeStyleDescription = Generalization(general=style_NodeStyleDescription, specific=diagram_style_WorkspaceImageDescription)
gen_diagram_style_EndLabelStyleDescription_BasicLabelStyleDescription = Generalization(general=BasicLabelStyleDescription, specific=diagram_style_EndLabelStyleDescription)
gen_diagram_style_BracketEdgeStyleDescription_EdgeStyleDescription = Generalization(general=EdgeStyleDescription, specific=diagram_style_BracketEdgeStyleDescription)
gen_diagram_style_BeginLabelStyleDescription_BasicLabelStyleDescription = Generalization(general=BasicLabelStyleDescription, specific=diagram_style_BeginLabelStyleDescription)
gen_diagram_style_CenterLabelStyleDescription_BasicLabelStyleDescription = Generalization(general=BasicLabelStyleDescription, specific=diagram_style_CenterLabelStyleDescription)
gen_diagram_tool_ToolGroup_ToolEntry = Generalization(general=ToolEntry, specific=diagram_tool_ToolGroup)
gen_diagram_tool_ToolSection_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=diagram_tool_ToolSection)
gen_diagram_tool_ToolSection_description_IdentifiedElement = Generalization(general=description_IdentifiedElement, specific=diagram_tool_ToolSection)
gen_diagram_tool_NodeCreationDescription_MappingBasedToolDescription = Generalization(general=MappingBasedToolDescription, specific=diagram_tool_NodeCreationDescription)
gen_diagram_tool_EdgeCreationDescription_MappingBasedToolDescription = Generalization(general=MappingBasedToolDescription, specific=diagram_tool_EdgeCreationDescription)
gen_diagram_tool_ContainerCreationDescription_MappingBasedToolDescription = Generalization(general=MappingBasedToolDescription, specific=diagram_tool_ContainerCreationDescription)
gen_diagram_tool_DoubleClickDescription_MappingBasedToolDescription = Generalization(general=MappingBasedToolDescription, specific=diagram_tool_DoubleClickDescription)
gen_diagram_tool_DeleteElementDescription_MappingBasedToolDescription = Generalization(general=MappingBasedToolDescription, specific=diagram_tool_DeleteElementDescription)
gen_diagram_tool_ReconnectEdgeDescription_MappingBasedToolDescription = Generalization(general=MappingBasedToolDescription, specific=diagram_tool_ReconnectEdgeDescription)
gen_diagram_tool_RequestDescription_AbstractToolDescription = Generalization(general=AbstractToolDescription, specific=diagram_tool_RequestDescription)
gen_diagram_tool_DirectEditLabel_MappingBasedToolDescription = Generalization(general=MappingBasedToolDescription, specific=diagram_tool_DirectEditLabel)
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
gen_diagram_tool_BehaviorTool_AbstractToolDescription = Generalization(general=AbstractToolDescription, specific=diagram_tool_BehaviorTool)
gen_diagram_tool_CreateEdgeView_CreateView = Generalization(general=CreateView, specific=diagram_tool_CreateEdgeView)
gen_diagram_tool_Navigation_ContainerModelOperation = Generalization(general=ContainerModelOperation, specific=diagram_tool_Navigation)
gen_diagram_tool_DiagramCreationDescription_RepresentationCreationDescription = Generalization(general=RepresentationCreationDescription, specific=diagram_tool_DiagramCreationDescription)
gen_diagram_tool_DiagramNavigationDescription_RepresentationNavigationDescription = Generalization(general=RepresentationNavigationDescription, specific=diagram_tool_DiagramNavigationDescription)
gen_diagram_tool_ContainerDropDescription_MappingBasedToolDescription = Generalization(general=MappingBasedToolDescription, specific=diagram_tool_ContainerDropDescription)
gen_diagram_filter_MappingFilter_Filter = Generalization(general=Filter, specific=diagram_filter_MappingFilter)
gen_diagram_filter_FilterDescription_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=diagram_filter_FilterDescription)
gen_diagram_filter_FilterDescription_description_IdentifiedElement = Generalization(general=description_IdentifiedElement, specific=diagram_filter_FilterDescription)
gen_diagram_filter_CompositeFilterDescription_FilterDescription = Generalization(general=FilterDescription, specific=diagram_filter_CompositeFilterDescription)
gen_diagram_filter_VariableFilter_Filter = Generalization(general=Filter, specific=diagram_filter_VariableFilter)
gen_diagram_concern_ConcernSet_DocumentedElement = Generalization(general=DocumentedElement, specific=diagram_concern_ConcernSet)
gen_diagram_concern_ConcernDescription_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=diagram_concern_ConcernDescription)
gen_diagram_concern_ConcernDescription_description_IdentifiedElement = Generalization(general=description_IdentifiedElement, specific=diagram_concern_ConcernDescription)

# Domain Model
domain_model = DomainModel(
    name="diagram",
    types={diagram_DDiagram, DRepresentation, description_DocumentedElement, DragAndDropTarget, diagram_DDiagramElement, DiagramDescription, diagram_DEdge, diagram_DNode, diagram_DNodeListElement, tool_BehaviorTool, diagram_DDiagramElementContainer, concern_ConcernDescription, filter_FilterDescription, AdditionalLayer, validation_ValidationRule, diagram_FilterVariableHistory, Layer, diagram_DSemanticDiagram, DDiagram, DSemanticDecorator, DRepresentationElement, diagram_FoldingPointFilter, diagram_FoldingFilter, diagram_Decoration, DiagramElementMapping, diagram_GraphicalFilter, diagram_HideFilter, GraphicalFilter, diagram_HideLabelFilter, EdgeTarget, diagram_AppliedCompositeFilters, filter_CompositeFilterDescription, diagram_AbsoluteBoundsFilter, diagram_AbstractDNode, DDiagramElement, AbstractDNode, diagram_NodeStyle, diagram_Style, NodeMapping, diagram_ContainerStyle, diagram_DNodeList, ContainerMapping, diagram_DNodeContainer, DDiagramElementContainer, diagram_EdgeStyle, diagram_EdgeTarget, IEdgeMapping, diagram_Dot, LabelStyle, Style, BorderedStyle, HideLabelCapabilityStyle, NodeStyle, diagram_FlatContainerStyle, ContainerStyle, diagram_GaugeSection, Customizable, diagram_ShapeContainerStyle, diagram_Square, diagram_Ellipse, diagram_Lozenge, diagram_BundledImage, diagram_WorkspaceImage, diagram_CustomStyle, diagram_BeginLabelStyle, diagram_CenterLabelStyle, diagram_EndLabelStyle, diagram_BorderedStyle, diagram_GaugeCompositeStyle, diagram_CollapseFilter, diagram_Note, diagram_VariableValue, diagram_BracketEdgeStyle, EdgeStyle, diagram_ComputedStyleDescriptionRegistry, style_StyleDescription, diagram_DragAndDropTarget, diagram_IndirectlyCollapseFilter, CollapseFilter, BasicLabelStyle, tool_SelectModelElementVariable, diagram_EObject, diagram_description_DiagramDescription, description_DragAndDropTargetDescription, description_RepresentationDescription, description_PasteTargetDescription, diagram_HideLabelCapabilityStyle, diagram_TypedVariableValue, VariableValue, TypedVariable, diagram_EObjectVariableValue, validation_ValidationSet, concern_ConcernSet, tool_AbstractToolDescription, EdgeMapping, tool_RepresentationCreationDescription, Layout, tool_InitialOperation, EdgeMappingImport, diagram_description_DiagramImportDescription, description_RepresentationImportDescription, description_DiagramDescription, diagram_description_DiagramExtensionDescription, RepresentationExtensionDescription, tool_ToolSection, diagram_description_DiagramElementMapping, description_RepresentationElementMapping, tool_DeleteElementDescription, tool_DirectEditLabel, tool_DoubleClickDescription, diagram_description_AbstractNodeMapping, description_DiagramElementMapping, diagram_description_NodeMapping, description_AbstractNodeMapping, style_NodeStyleDescription, ConditionalNodeStyleDescription, diagram_description_ContainerMapping, style_ContainerStyleDescription, ConditionalContainerStyleDescription, diagram_description_EdgeMapping, description_IEdgeMapping, diagram_description_NodeMappingImport, description_NodeMapping, description_AbstractMappingImport, diagram_description_ContainerMappingImport, description_ContainerMapping, ConditionalEdgeStyleDescription, tool_ReconnectEdgeDescription, style_EdgeStyleDescription, diagram_description_EdgeMappingImport, description_IdentifiedElement, AbstractNodeMapping, diagram_description_IEdgeMapping, diagram_description_Layout, DocumentedElement, diagram_description_OrderedTreeLayout, diagram_description_ConditionalNodeStyleDescription, ConditionalStyleDescription, diagram_description_ConditionalEdgeStyleDescription, diagram_description_ConditionalContainerStyleDescription, diagram_description_MappingBasedDecoration, DecorationDescription, diagram_description_Layer, description_EndUserDocumentedElement, diagram_description_CompositeLayout, diagram_description_AdditionalLayer, diagram_description_DragAndDropTargetDescription, tool_ContainerDropDescription, diagram_style_BorderedStyleDescription, StyleDescription, DecorationDescriptionsSet, Customization, style_LabelStyleDescription, style_TooltipStyleDescription, style_HideLabelCapabilityStyleDescription, ColorDescription, diagram_style_NodeStyleDescription, style_BorderedStyleDescription, diagram_style_LozengeNodeDescription, diagram_style_CustomStyleDescription, NodeStyleDescription, diagram_style_SquareDescription, diagram_style_BundledImageDescription, diagram_style_NoteDescription, diagram_style_EllipseNodeDescription, diagram_style_GaugeCompositeStyleDescription, style_GaugeSectionDescription, diagram_style_GaugeSectionDescription, diagram_style_DotDescription, diagram_style_SizeComputationContainerStyleDescription, diagram_style_FlatContainerStyleDescription, style_SizeComputationContainerStyleDescription, diagram_style_RoundedCornerStyleDescription, diagram_style_ContainerStyleDescription, style_RoundedCornerStyleDescription, diagram_style_EdgeStyleDescription, style_LabelBorderStyleDescription, diagram_style_ShapeContainerStyleDescription, diagram_style_WorkspaceImageDescription, style_BeginLabelStyleDescription, style_CenterLabelStyleDescription, style_EndLabelStyleDescription, diagram_style_EndLabelStyleDescription, diagram_style_BracketEdgeStyleDescription, EdgeStyleDescription, diagram_style_HideLabelCapabilityStyleDescription, diagram_style_BeginLabelStyleDescription, BasicLabelStyleDescription, diagram_style_CenterLabelStyleDescription, tool_PopupMenu, tool_ToolGroupExtension, diagram_tool_ToolGroup, ToolEntry, diagram_tool_ToolSection, tool_ToolEntry, tool_NodeCreationVariable, tool_ContainerViewVariable, diagram_tool_ToolGroupExtension, tool_ToolGroup, diagram_tool_NodeCreationDescription, MappingBasedToolDescription, tool_InitialNodeCreationOperation, diagram_tool_EdgeCreationDescription, tool_TargetEdgeViewCreationVariable, tool_InitEdgeCreationOperation, tool_SourceEdgeCreationVariable, tool_TargetEdgeCreationVariable, tool_SourceEdgeViewCreationVariable, diagram_tool_ContainerCreationDescription, tool_DeleteHook, diagram_tool_DoubleClickDescription, tool_ElementDoubleClickVariable, diagram_tool_DeleteHook, tool_DeleteHookParameter, diagram_tool_DeleteHookParameter, diagram_tool_DeleteElementDescription, tool_ElementDeleteVariable, diagram_tool_ReconnectEdgeDescription, diagram_tool_RequestDescription, AbstractToolDescription, diagram_tool_DirectEditLabel, tool_EditMaskVariables, tool_ElementSelectVariable, diagram_tool_SourceEdgeCreationVariable, description_AbstractVariable, tool_VariableContainer, diagram_tool_SourceEdgeViewCreationVariable, diagram_tool_TargetEdgeCreationVariable, diagram_tool_TargetEdgeViewCreationVariable, diagram_tool_ElementDoubleClickVariable, diagram_tool_NodeCreationVariable, diagram_tool_CreateView, ContainerModelOperation, diagram_tool_BehaviorTool, diagram_tool_CreateEdgeView, CreateView, diagram_tool_Navigation, diagram_tool_DiagramCreationDescription, RepresentationCreationDescription, diagram_tool_DiagramNavigationDescription, RepresentationNavigationDescription, diagram_tool_ContainerDropDescription, tool_DropContainerVariable, tool_ElementDropVariable, tool_InitialContainerDropOperation, diagram_filter_MappingFilter, Filter, diagram_filter_FilterDescription, diagram_filter_Filter, diagram_filter_CompositeFilterDescription, FilterDescription, filter_Filter, diagram_filter_VariableFilter, InteractiveVariableDescription, diagram_concern_ConcernSet, diagram_concern_ConcernDescription, ContainerLayout, LabelPosition, ContainerShape, BackgroundStyle, BundledImageShape, LineStyle, EdgeArrows, AlignmentKind, EdgeRouting, ResizeKind, ArrangeConstraint, FoldingStyle, LayoutDirection, CenteringStyle, Side, ReconnectionKind, FilterKind},
    associations={nodeListElements10, ownedDiagramElements0, diagramElements1, description4, edges6, nodes8, activateBehaviors25, containers12, currentConcern14, activatedFilters16, activatedTransientLayers18, allFilters20, activatedRules23, filterVariableHistory27, activatedLayers29, hiddenElements31, parentLayers34, decorations37, transientDecorations39, diagramElementMapping42, graphicalFilters44, compositeFilterDescriptions46, ownedBorderedNodes47, ownedStyle49, originalStyle51, actualMapping53, candidatesMapping55, ownedStyle67, originalStyle69, nodes58, containers62, elements64, actualMapping72, candidatesMapping74, ownedDiagramElements77, ownedElements79, ownedStyle81, originalStyle84, actualMapping87, candidatesMapping90, originalStyle100, ownedStyle93, sourceNode95, targetNode96, actualMapping98, path103, outgoingEdges105, incomingEdges106, beginLabelStyle108, centerLabelStyle110, endLabelStyle112, sections114, ownedValues115, computedStyleDescriptions117, variableDefinition119, modelElement120, variableDefinition118, allContainerMappings129, validationSet132, concerns134, filters122, allEdgeMappings124, allNodeMappings126, init141, layout143, diagramInitialisation145, allTools136, defaultConcern138, edgeMappings162, edgeMappingImports165, containerMappings167, defaultLayer147, additionalLayers150, allLayers153, allActivatedTools156, nodeMappings159, importedDiagram178, reusedMappings170, toolSection173, reusedTools175, layers180, validationSet182, concerns185, labelDirectEdit189, deletionDescription188, doubleClickDescription191, borderedNodeMappings192, reusedBorderedNodeMappings194, style197, conditionnalStyles198, reusedContainerMappings211, allContainerMappings214, style217, conditionnalStyles219, subNodeMappings200, allNodeMappings202, reusedNodeMappings205, subContainerMappings208, importedMapping221, importedMapping223, sourceMapping225, targetMapping227, conditionnalStyles232, style230, importedMapping238, conditionnalStyles240, reconnections234, pathNodeMapping236, style247, style243, style245, mappings251, nodeMappings253, nodeMapping249, reusedMappings264, allTools267, toolSections270, reusedTools273, edgeMappings255, edgeMappingImports258, containerMappings261, dropDescriptions283, decorationDescriptionsSet276, allEdgeMappings278, customization281, borderColor284, color285, color287, color291, color289, sections297, color293, backgroundColor295, foregroundColor300, backgroundColor298, backgroundColor303, foregroundColor305, strokeColor312, labelBorderStyle308, backgroundColor310, beginLabelStyleDescription314, centerLabelStyleDescription316, endLabelStyleDescription318, centeredSourceMappings320, centeredTargetMappings323, popupMenus330, reusedTools332, groupExtensions335, tools337, ownedTools326, subSections327, variable345, viewVariable347, group339, tools340, nodeMappings343, initialOperation349, extraMappings351, sourceViewVariable360, targetViewVariable362, edgeMappings354, sourceVariable356, targetVariable358, containerMappings372, variable374, viewVariable377, initialOperation380, initialOperation364, extraSourceMappings366, extraTargetMappings369, hook396, mappings398, element401, elementView402, initialOperation405, parameters408, extraMappings383, element386, elementView387, containerView390, initialOperation393, target411, sourceView414, targetView417, source409, mask428, element420, initialOperation422, edgeView425, initialOperation432, initialOperation429, mapping434, diagramDescription436, diagramDescription438, diagramDescription440, initialOperation454, mappings442, oldContainer444, newContainer446, element449, newViewContainer451, mappings456, filters458, ownedVariables459, ownedConcernDescriptions460, filters462, rules464, behaviors467},
    generalizations={gen_diagram_DDiagram_DRepresentation, gen_diagram_DDiagram_description_DocumentedElement, gen_diagram_DDiagram_DragAndDropTarget, gen_diagram_DSemanticDiagram_DDiagram, gen_diagram_DSemanticDiagram_DSemanticDecorator, gen_diagram_DDiagramElement_DRepresentationElement, gen_diagram_FoldingPointFilter_GraphicalFilter, gen_diagram_FoldingFilter_GraphicalFilter, gen_diagram_HideFilter_GraphicalFilter, gen_diagram_HideLabelFilter_GraphicalFilter, gen_diagram_DNode_EdgeTarget, gen_diagram_DNode_DragAndDropTarget, gen_diagram_AppliedCompositeFilters_GraphicalFilter, gen_diagram_AbsoluteBoundsFilter_GraphicalFilter, gen_diagram_AbstractDNode_DDiagramElement, gen_diagram_DNode_AbstractDNode, gen_diagram_DDiagramElementContainer_AbstractDNode, gen_diagram_DDiagramElementContainer_EdgeTarget, gen_diagram_DDiagramElementContainer_DragAndDropTarget, gen_diagram_DNodeList_DDiagramElementContainer, gen_diagram_DNodeContainer_DDiagramElementContainer, gen_diagram_DEdge_DDiagramElement, gen_diagram_DEdge_EdgeTarget, gen_diagram_DNodeListElement_AbstractDNode, gen_diagram_NodeStyle_LabelStyle, gen_diagram_NodeStyle_Style, gen_diagram_NodeStyle_BorderedStyle, gen_diagram_NodeStyle_HideLabelCapabilityStyle, gen_diagram_ContainerStyle_LabelStyle, gen_diagram_Dot_NodeStyle, gen_diagram_ContainerStyle_Style, gen_diagram_ContainerStyle_BorderedStyle, gen_diagram_ContainerStyle_HideLabelCapabilityStyle, gen_diagram_FlatContainerStyle_ContainerStyle, gen_diagram_GaugeSection_Customizable, gen_diagram_Square_NodeStyle, gen_diagram_Ellipse_NodeStyle, gen_diagram_ShapeContainerStyle_ContainerStyle, gen_diagram_Lozenge_NodeStyle, gen_diagram_BundledImage_NodeStyle, gen_diagram_WorkspaceImage_NodeStyle, gen_diagram_WorkspaceImage_ContainerStyle, gen_diagram_CustomStyle_NodeStyle, gen_diagram_EdgeStyle_Style, gen_diagram_BorderedStyle_Style, gen_diagram_GaugeCompositeStyle_NodeStyle, gen_diagram_CollapseFilter_GraphicalFilter, gen_diagram_Note_NodeStyle, gen_diagram_EndLabelStyle_BasicLabelStyle, gen_diagram_BracketEdgeStyle_EdgeStyle, gen_diagram_IndirectlyCollapseFilter_CollapseFilter, gen_diagram_BeginLabelStyle_BasicLabelStyle, gen_diagram_CenterLabelStyle_BasicLabelStyle, gen_diagram_description_DiagramDescription_description_DragAndDropTargetDescription, gen_diagram_description_DiagramDescription_description_RepresentationDescription, gen_diagram_description_DiagramDescription_description_PasteTargetDescription, gen_diagram_TypedVariableValue_VariableValue, gen_diagram_EObjectVariableValue_VariableValue, gen_diagram_description_DiagramImportDescription_description_RepresentationImportDescription, gen_diagram_description_DiagramImportDescription_description_DiagramDescription, gen_diagram_description_DiagramExtensionDescription_RepresentationExtensionDescription, gen_diagram_description_DiagramElementMapping_description_RepresentationElementMapping, gen_diagram_description_DiagramElementMapping_description_PasteTargetDescription, gen_diagram_description_AbstractNodeMapping_description_DiagramElementMapping, gen_diagram_description_AbstractNodeMapping_description_DocumentedElement, gen_diagram_description_NodeMapping_description_AbstractNodeMapping, gen_diagram_description_NodeMapping_description_DragAndDropTargetDescription, gen_diagram_description_ContainerMapping_description_AbstractNodeMapping, gen_diagram_description_ContainerMapping_description_DragAndDropTargetDescription, gen_diagram_description_EdgeMapping_description_DiagramElementMapping, gen_diagram_description_EdgeMapping_description_DocumentedElement, gen_diagram_description_EdgeMapping_description_IEdgeMapping, gen_diagram_description_NodeMappingImport_description_NodeMapping, gen_diagram_description_NodeMappingImport_description_AbstractMappingImport, gen_diagram_description_ContainerMappingImport_description_ContainerMapping, gen_diagram_description_ContainerMappingImport_description_AbstractMappingImport, gen_diagram_description_EdgeMappingImport_description_DocumentedElement, gen_diagram_description_EdgeMappingImport_description_IEdgeMapping, gen_diagram_description_EdgeMappingImport_description_IdentifiedElement, gen_diagram_description_ConditionalContainerStyleDescription_ConditionalStyleDescription, gen_diagram_description_Layout_DocumentedElement, gen_diagram_description_OrderedTreeLayout_Layout, gen_diagram_description_ConditionalNodeStyleDescription_ConditionalStyleDescription, gen_diagram_description_ConditionalEdgeStyleDescription_ConditionalStyleDescription, gen_diagram_description_MappingBasedDecoration_DecorationDescription, gen_diagram_description_Layer_description_DocumentedElement, gen_diagram_description_Layer_description_EndUserDocumentedElement, gen_diagram_description_Layer_description_IdentifiedElement, gen_diagram_description_CompositeLayout_Layout, gen_diagram_description_AdditionalLayer_Layer, gen_diagram_style_BorderedStyleDescription_StyleDescription, gen_diagram_style_NodeStyleDescription_style_LabelStyleDescription, gen_diagram_style_NodeStyleDescription_style_TooltipStyleDescription, gen_diagram_style_NodeStyleDescription_style_HideLabelCapabilityStyleDescription, gen_diagram_style_NodeStyleDescription_style_StyleDescription, gen_diagram_style_NodeStyleDescription_style_BorderedStyleDescription, gen_diagram_style_LozengeNodeDescription_NodeStyleDescription, gen_diagram_style_CustomStyleDescription_NodeStyleDescription, gen_diagram_style_SquareDescription_NodeStyleDescription, gen_diagram_style_BundledImageDescription_NodeStyleDescription, gen_diagram_style_NoteDescription_NodeStyleDescription, gen_diagram_style_EllipseNodeDescription_NodeStyleDescription, gen_diagram_style_GaugeCompositeStyleDescription_NodeStyleDescription, gen_diagram_style_DotDescription_NodeStyleDescription, gen_diagram_style_FlatContainerStyleDescription_style_ContainerStyleDescription, gen_diagram_style_FlatContainerStyleDescription_style_SizeComputationContainerStyleDescription, gen_diagram_style_RoundedCornerStyleDescription_StyleDescription, gen_diagram_style_ContainerStyleDescription_style_RoundedCornerStyleDescription, gen_diagram_style_ContainerStyleDescription_style_BorderedStyleDescription, gen_diagram_style_ContainerStyleDescription_style_LabelStyleDescription, gen_diagram_style_ContainerStyleDescription_style_TooltipStyleDescription, gen_diagram_style_ContainerStyleDescription_style_HideLabelCapabilityStyleDescription, gen_diagram_style_WorkspaceImageDescription_style_ContainerStyleDescription, gen_diagram_style_EdgeStyleDescription_StyleDescription, gen_diagram_style_ShapeContainerStyleDescription_style_ContainerStyleDescription, gen_diagram_style_ShapeContainerStyleDescription_style_SizeComputationContainerStyleDescription, gen_diagram_style_WorkspaceImageDescription_style_NodeStyleDescription, gen_diagram_style_EndLabelStyleDescription_BasicLabelStyleDescription, gen_diagram_style_BracketEdgeStyleDescription_EdgeStyleDescription, gen_diagram_style_BeginLabelStyleDescription_BasicLabelStyleDescription, gen_diagram_style_CenterLabelStyleDescription_BasicLabelStyleDescription, gen_diagram_tool_ToolGroup_ToolEntry, gen_diagram_tool_ToolSection_description_DocumentedElement, gen_diagram_tool_ToolSection_description_IdentifiedElement, gen_diagram_tool_NodeCreationDescription_MappingBasedToolDescription, gen_diagram_tool_EdgeCreationDescription_MappingBasedToolDescription, gen_diagram_tool_ContainerCreationDescription_MappingBasedToolDescription, gen_diagram_tool_DoubleClickDescription_MappingBasedToolDescription, gen_diagram_tool_DeleteElementDescription_MappingBasedToolDescription, gen_diagram_tool_ReconnectEdgeDescription_MappingBasedToolDescription, gen_diagram_tool_RequestDescription_AbstractToolDescription, gen_diagram_tool_DirectEditLabel_MappingBasedToolDescription, gen_diagram_tool_SourceEdgeCreationVariable_description_AbstractVariable, gen_diagram_tool_SourceEdgeCreationVariable_tool_VariableContainer, gen_diagram_tool_SourceEdgeViewCreationVariable_description_AbstractVariable, gen_diagram_tool_SourceEdgeViewCreationVariable_tool_VariableContainer, gen_diagram_tool_TargetEdgeCreationVariable_description_AbstractVariable, gen_diagram_tool_TargetEdgeCreationVariable_tool_VariableContainer, gen_diagram_tool_TargetEdgeViewCreationVariable_description_AbstractVariable, gen_diagram_tool_TargetEdgeViewCreationVariable_tool_VariableContainer, gen_diagram_tool_ElementDoubleClickVariable_description_AbstractVariable, gen_diagram_tool_ElementDoubleClickVariable_tool_VariableContainer, gen_diagram_tool_NodeCreationVariable_description_AbstractVariable, gen_diagram_tool_NodeCreationVariable_tool_VariableContainer, gen_diagram_tool_CreateView_ContainerModelOperation, gen_diagram_tool_BehaviorTool_AbstractToolDescription, gen_diagram_tool_CreateEdgeView_CreateView, gen_diagram_tool_Navigation_ContainerModelOperation, gen_diagram_tool_DiagramCreationDescription_RepresentationCreationDescription, gen_diagram_tool_DiagramNavigationDescription_RepresentationNavigationDescription, gen_diagram_tool_ContainerDropDescription_MappingBasedToolDescription, gen_diagram_filter_MappingFilter_Filter, gen_diagram_filter_FilterDescription_description_DocumentedElement, gen_diagram_filter_FilterDescription_description_IdentifiedElement, gen_diagram_filter_CompositeFilterDescription_FilterDescription, gen_diagram_filter_VariableFilter_Filter, gen_diagram_concern_ConcernSet_DocumentedElement, gen_diagram_concern_ConcernDescription_description_DocumentedElement, gen_diagram_concern_ConcernDescription_description_IdentifiedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)