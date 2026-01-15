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
			EnumerationLiteral(name="ring")
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

EdgeArrows: Enumeration = Enumeration(
    name="EdgeArrows",
    literals={
            EnumerationLiteral(name="InputClosedArrow"),
			EnumerationLiteral(name="OutputFillClosedArrow"),
			EnumerationLiteral(name="InputFillClosedArrow"),
			EnumerationLiteral(name="Diamond"),
			EnumerationLiteral(name="FillDiamond"),
			EnumerationLiteral(name="InputArrowWithDiamond"),
			EnumerationLiteral(name="InputArrowWithFillDiamond"),
			EnumerationLiteral(name="NoDecoration"),
			EnumerationLiteral(name="OutputArrow"),
			EnumerationLiteral(name="InputArrow"),
			EnumerationLiteral(name="OutputClosedArrow")
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
diagram_DDiagramElement = Class(name="diagram::DDiagramElement", is_abstract=True)
diagram_DDiagram = Class(name="diagram::DDiagram")
DRepresentation = Class(name="DRepresentation")
description_DocumentedElement = Class(name="description::DocumentedElement")
DragAndDropTarget = Class(name="DragAndDropTarget")
DValidable = Class(name="DValidable")
DContainer = Class(name="DContainer")
diagram_DNode = Class(name="diagram::DNode")
diagram_DNodeListElement = Class(name="diagram::DNodeListElement")
diagram_DDiagramElementContainer = Class(name="diagram::DDiagramElementContainer", is_abstract=True)
concern_ConcernDescription = Class(name="concern::ConcernDescription")
filter_FilterDescription = Class(name="filter::FilterDescription")
DiagramDescription = Class(name="DiagramDescription")
diagram_DEdge = Class(name="diagram::DEdge")
validation_ValidationRule = Class(name="validation::ValidationRule")
tool_BehaviorTool = Class(name="tool::BehaviorTool")
diagram_FilterVariableHistory = Class(name="diagram::FilterVariableHistory")
Layer = Class(name="Layer")
diagram_Decoration = Class(name="diagram::Decoration")
DiagramElementMapping = Class(name="DiagramElementMapping")
diagram_GraphicalFilter = Class(name="diagram::GraphicalFilter", is_abstract=True)
diagram_HideFilter = Class(name="diagram::HideFilter")
GraphicalFilter = Class(name="GraphicalFilter")
diagram_HideLabelFilter = Class(name="diagram::HideLabelFilter")
diagram_FoldingPointFilter = Class(name="diagram::FoldingPointFilter")
diagram_FoldingFilter = Class(name="diagram::FoldingFilter")
diagram_AppliedCompositeFilters = Class(name="diagram::AppliedCompositeFilters")
diagram_DSemanticDiagram = Class(name="diagram::DSemanticDiagram")
DDiagram = Class(name="DDiagram")
DSemanticDecorator = Class(name="DSemanticDecorator")
DRepresentationElement = Class(name="DRepresentationElement")
DNavigable = Class(name="DNavigable")
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
diagram_EdgeStyle = Class(name="diagram::EdgeStyle")
diagram_EdgeTarget = Class(name="diagram::EdgeTarget", is_abstract=True)
IEdgeMapping = Class(name="IEdgeMapping")
diagram_DNodeList = Class(name="diagram::DNodeList")
LabelStyle = Class(name="LabelStyle")
Style = Class(name="Style")
BorderedStyle = Class(name="BorderedStyle")
diagram_Dot = Class(name="diagram::Dot")
NodeStyle = Class(name="NodeStyle")
diagram_RGBValues = Class(name="diagram::RGBValues")
diagram_FlatContainerStyle = Class(name="diagram::FlatContainerStyle")
ContainerStyle = Class(name="ContainerStyle")
diagram_ShapeContainerStyle = Class(name="diagram::ShapeContainerStyle")
diagram_GaugeSection = Class(name="diagram::GaugeSection")
Customizable = Class(name="Customizable")
diagram_Lozenge = Class(name="diagram::Lozenge")
diagram_BundledImage = Class(name="diagram::BundledImage")
diagram_WorkspaceImage = Class(name="diagram::WorkspaceImage")
diagram_CustomStyle = Class(name="diagram::CustomStyle")
diagram_Square = Class(name="diagram::Square")
diagram_Ellipse = Class(name="diagram::Ellipse")
diagram_BeginLabelStyle = Class(name="diagram::BeginLabelStyle")
diagram_CenterLabelStyle = Class(name="diagram::CenterLabelStyle")
diagram_EndLabelStyle = Class(name="diagram::EndLabelStyle")
diagram_GaugeCompositeStyle = Class(name="diagram::GaugeCompositeStyle")
filter_FilterVariable = Class(name="filter::FilterVariable")
diagram_EObject = Class(name="diagram::EObject")
diagram_CollapseFilter = Class(name="diagram::CollapseFilter")
diagram_IndirectlyCollapseFilter = Class(name="diagram::IndirectlyCollapseFilter")
CollapseFilter = Class(name="CollapseFilter")
BasicLabelStyle = Class(name="BasicLabelStyle")
diagram_BorderedStyle = Class(name="diagram::BorderedStyle")
diagram_Note = Class(name="diagram::Note")
diagram_FilterVariableValue = Class(name="diagram::FilterVariableValue")
diagram_ComputedStyleDescriptionRegistry = Class(name="diagram::ComputedStyleDescriptionRegistry")
style_StyleDescription = Class(name="style::StyleDescription")
diagram_DiagramElementMapping2ModelElement = Class(name="diagram::DiagramElementMapping2ModelElement")
diagram_ModelElement2ViewVariable = Class(name="diagram::ModelElement2ViewVariable")
diagram_ViewVariable2ContainerVariable = Class(name="diagram::ViewVariable2ContainerVariable")
diagram_ContainerVariable2StyleDescription = Class(name="diagram::ContainerVariable2StyleDescription")
diagram_BracketEdgeStyle = Class(name="diagram::BracketEdgeStyle")
EdgeStyle = Class(name="EdgeStyle")
EdgeMapping = Class(name="EdgeMapping")
validation_ValidationSet = Class(name="validation::ValidationSet")
concern_ConcernSet = Class(name="concern::ConcernSet")
diagram_DragAndDropTarget = Class(name="diagram::DragAndDropTarget")
diagram_description_DiagramDescription = Class(name="diagram::description::DiagramDescription")
description_DragAndDropTargetDescription = Class(name="description::DragAndDropTargetDescription")
description_RepresentationDescription = Class(name="description::RepresentationDescription")
description_PasteTargetDescription = Class(name="description::PasteTargetDescription")
tool_RepresentationCreationDescription = Class(name="tool::RepresentationCreationDescription")
Layout = Class(name="Layout")
tool_InitialOperation = Class(name="tool::InitialOperation")
AdditionalLayer = Class(name="AdditionalLayer")
tool_AbstractToolDescription = Class(name="tool::AbstractToolDescription")
EdgeMappingImport = Class(name="EdgeMappingImport")
tool_ToolSection = Class(name="tool::ToolSection")
diagram_description_DiagramImportDescription = Class(name="diagram::description::DiagramImportDescription")
description_RepresentationImportDescription = Class(name="description::RepresentationImportDescription")
description_DiagramDescription = Class(name="description::DiagramDescription")
diagram_description_DiagramElementMapping = Class(name="diagram::description::DiagramElementMapping", is_abstract=True)
description_RepresentationElementMapping = Class(name="description::RepresentationElementMapping")
diagram_description_DiagramExtensionDescription = Class(name="diagram::description::DiagramExtensionDescription")
RepresentationExtensionDescription = Class(name="RepresentationExtensionDescription")
tool_DirectEditLabel = Class(name="tool::DirectEditLabel")
tool_DeleteElementDescription = Class(name="tool::DeleteElementDescription")
diagram_description_NodeMapping = Class(name="diagram::description::NodeMapping")
description_AbstractNodeMapping = Class(name="description::AbstractNodeMapping")
tool_DoubleClickDescription = Class(name="tool::DoubleClickDescription")
diagram_description_AbstractNodeMapping = Class(name="diagram::description::AbstractNodeMapping", is_abstract=True)
description_DiagramElementMapping = Class(name="description::DiagramElementMapping")
style_NodeStyleDescription = Class(name="style::NodeStyleDescription")
ConditionalNodeStyleDescription = Class(name="ConditionalNodeStyleDescription")
diagram_description_ContainerMapping = Class(name="diagram::description::ContainerMapping")
diagram_description_ContainerMappingImport = Class(name="diagram::description::ContainerMappingImport")
description_ContainerMapping = Class(name="description::ContainerMapping")
diagram_description_EdgeMapping = Class(name="diagram::description::EdgeMapping")
description_IEdgeMapping = Class(name="description::IEdgeMapping")
style_ContainerStyleDescription = Class(name="style::ContainerStyleDescription")
ConditionalContainerStyleDescription = Class(name="ConditionalContainerStyleDescription")
diagram_description_NodeMappingImport = Class(name="diagram::description::NodeMappingImport")
description_NodeMapping = Class(name="description::NodeMapping")
description_AbstractMappingImport = Class(name="description::AbstractMappingImport")
style_EdgeStyleDescription = Class(name="style::EdgeStyleDescription")
ConditionalEdgeStyleDescription = Class(name="ConditionalEdgeStyleDescription")
tool_ReconnectEdgeDescription = Class(name="tool::ReconnectEdgeDescription")
AbstractNodeMapping = Class(name="AbstractNodeMapping")
diagram_description_ConditionalNodeStyleDescription = Class(name="diagram::description::ConditionalNodeStyleDescription")
ConditionalStyleDescription = Class(name="ConditionalStyleDescription")
diagram_description_ConditionalEdgeStyleDescription = Class(name="diagram::description::ConditionalEdgeStyleDescription")
diagram_description_ConditionalContainerStyleDescription = Class(name="diagram::description::ConditionalContainerStyleDescription")
diagram_description_Layout = Class(name="diagram::description::Layout", is_abstract=True)
DocumentedElement = Class(name="DocumentedElement")
diagram_description_OrderedTreeLayout = Class(name="diagram::description::OrderedTreeLayout")
diagram_description_CompositeLayout = Class(name="diagram::description::CompositeLayout")
diagram_description_IEdgeMapping = Class(name="diagram::description::IEdgeMapping", is_abstract=True)
diagram_description_EdgeMappingImport = Class(name="diagram::description::EdgeMappingImport")
description_IdentifiedElement = Class(name="description::IdentifiedElement")
DecorationDescriptionsSet = Class(name="DecorationDescriptionsSet")
diagram_description_MappingBasedDecoration = Class(name="diagram::description::MappingBasedDecoration")
DecorationDescription = Class(name="DecorationDescription")
diagram_description_Layer = Class(name="diagram::description::Layer")
description_EndUserDocumentedElement = Class(name="description::EndUserDocumentedElement")
diagram_style_BorderedStyleDescription = Class(name="diagram::style::BorderedStyleDescription")
StyleDescription = Class(name="StyleDescription")
ColorDescription = Class(name="ColorDescription")
diagram_style_NodeStyleDescription = Class(name="diagram::style::NodeStyleDescription", is_abstract=True)
style_BorderedStyleDescription = Class(name="style::BorderedStyleDescription")
style_LabelStyleDescription = Class(name="style::LabelStyleDescription")
style_TooltipStyleDescription = Class(name="style::TooltipStyleDescription")
diagram_style_CustomStyleDescription = Class(name="diagram::style::CustomStyleDescription")
NodeStyleDescription = Class(name="NodeStyleDescription")
diagram_style_SquareDescription = Class(name="diagram::style::SquareDescription")
Customization = Class(name="Customization")
diagram_description_AdditionalLayer = Class(name="diagram::description::AdditionalLayer")
diagram_description_DragAndDropTargetDescription = Class(name="diagram::description::DragAndDropTargetDescription", is_abstract=True)
tool_ContainerDropDescription = Class(name="tool::ContainerDropDescription")
diagram_style_EllipseNodeDescription = Class(name="diagram::style::EllipseNodeDescription")
diagram_style_BundledImageDescription = Class(name="diagram::style::BundledImageDescription")
diagram_style_NoteDescription = Class(name="diagram::style::NoteDescription")
diagram_style_DotDescription = Class(name="diagram::style::DotDescription")
diagram_style_LozengeNodeDescription = Class(name="diagram::style::LozengeNodeDescription")
style_GaugeSectionDescription = Class(name="style::GaugeSectionDescription")
diagram_style_GaugeSectionDescription = Class(name="diagram::style::GaugeSectionDescription")
diagram_style_SizeComputationContainerStyleDescription = Class(name="diagram::style::SizeComputationContainerStyleDescription", is_abstract=True)
diagram_style_GaugeCompositeStyleDescription = Class(name="diagram::style::GaugeCompositeStyleDescription")
diagram_style_FlatContainerStyleDescription = Class(name="diagram::style::FlatContainerStyleDescription")
style_SizeComputationContainerStyleDescription = Class(name="style::SizeComputationContainerStyleDescription")
diagram_style_RoundedCornerStyleDescription = Class(name="diagram::style::RoundedCornerStyleDescription", is_abstract=True)
diagram_style_ContainerStyleDescription = Class(name="diagram::style::ContainerStyleDescription", is_abstract=True)
style_RoundedCornerStyleDescription = Class(name="style::RoundedCornerStyleDescription")
diagram_style_WorkspaceImageDescription = Class(name="diagram::style::WorkspaceImageDescription")
diagram_style_EdgeStyleDescription = Class(name="diagram::style::EdgeStyleDescription")
style_LabelBorderStyleDescription = Class(name="style::LabelBorderStyleDescription")
diagram_style_ShapeContainerStyleDescription = Class(name="diagram::style::ShapeContainerStyleDescription")
diagram_style_CenterLabelStyleDescription = Class(name="diagram::style::CenterLabelStyleDescription")
diagram_style_EndLabelStyleDescription = Class(name="diagram::style::EndLabelStyleDescription")
diagram_style_BracketEdgeStyleDescription = Class(name="diagram::style::BracketEdgeStyleDescription")
EdgeStyleDescription = Class(name="EdgeStyleDescription")
diagram_tool_ToolSection = Class(name="diagram::tool::ToolSection")
tool_ToolEntry = Class(name="tool::ToolEntry")
tool_PopupMenu = Class(name="tool::PopupMenu")
tool_ToolGroupExtension = Class(name="tool::ToolGroupExtension")
style_BeginLabelStyleDescription = Class(name="style::BeginLabelStyleDescription")
style_CenterLabelStyleDescription = Class(name="style::CenterLabelStyleDescription")
style_EndLabelStyleDescription = Class(name="style::EndLabelStyleDescription")
diagram_style_BeginLabelStyleDescription = Class(name="diagram::style::BeginLabelStyleDescription")
BasicLabelStyleDescription = Class(name="BasicLabelStyleDescription")
tool_NodeCreationVariable = Class(name="tool::NodeCreationVariable")
tool_ContainerViewVariable = Class(name="tool::ContainerViewVariable")
tool_InitialNodeCreationOperation = Class(name="tool::InitialNodeCreationOperation")
diagram_tool_EdgeCreationDescription = Class(name="diagram::tool::EdgeCreationDescription")
diagram_tool_ToolGroup = Class(name="diagram::tool::ToolGroup")
ToolEntry = Class(name="ToolEntry")
diagram_tool_ToolGroupExtension = Class(name="diagram::tool::ToolGroupExtension")
tool_ToolGroup = Class(name="tool::ToolGroup")
diagram_tool_NodeCreationDescription = Class(name="diagram::tool::NodeCreationDescription")
MappingBasedToolDescription = Class(name="MappingBasedToolDescription")
tool_SourceEdgeViewCreationVariable = Class(name="tool::SourceEdgeViewCreationVariable")
tool_TargetEdgeViewCreationVariable = Class(name="tool::TargetEdgeViewCreationVariable")
tool_InitEdgeCreationOperation = Class(name="tool::InitEdgeCreationOperation")
diagram_tool_ContainerCreationDescription = Class(name="diagram::tool::ContainerCreationDescription")
tool_SourceEdgeCreationVariable = Class(name="tool::SourceEdgeCreationVariable")
tool_TargetEdgeCreationVariable = Class(name="tool::TargetEdgeCreationVariable")
diagram_tool_DeleteElementDescription = Class(name="diagram::tool::DeleteElementDescription")
tool_ElementDeleteVariable = Class(name="tool::ElementDeleteVariable")
tool_DeleteHook = Class(name="tool::DeleteHook")
diagram_tool_DoubleClickDescription = Class(name="diagram::tool::DoubleClickDescription")
diagram_tool_ReconnectEdgeDescription = Class(name="diagram::tool::ReconnectEdgeDescription")
tool_ElementSelectVariable = Class(name="tool::ElementSelectVariable")
tool_ElementDoubleClickVariable = Class(name="tool::ElementDoubleClickVariable")
diagram_tool_DeleteHook = Class(name="diagram::tool::DeleteHook")
tool_DeleteHookParameter = Class(name="tool::DeleteHookParameter")
diagram_tool_DeleteHookParameter = Class(name="diagram::tool::DeleteHookParameter")
tool_EditMaskVariables = Class(name="tool::EditMaskVariables")
diagram_tool_BehaviorTool = Class(name="diagram::tool::BehaviorTool")
diagram_tool_RequestDescription = Class(name="diagram::tool::RequestDescription")
AbstractToolDescription = Class(name="AbstractToolDescription")
diagram_tool_DirectEditLabel = Class(name="diagram::tool::DirectEditLabel")
diagram_tool_SourceEdgeCreationVariable = Class(name="diagram::tool::SourceEdgeCreationVariable")
tool_AbstractVariable = Class(name="tool::AbstractVariable")
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
diagram_tool_DiagramCreationDescription = Class(name="diagram::tool::DiagramCreationDescription")
RepresentationCreationDescription = Class(name="RepresentationCreationDescription")
diagram_tool_DiagramNavigationDescription = Class(name="diagram::tool::DiagramNavigationDescription")
RepresentationNavigationDescription = Class(name="RepresentationNavigationDescription")
diagram_tool_ContainerDropDescription = Class(name="diagram::tool::ContainerDropDescription")
tool_DropContainerVariable = Class(name="tool::DropContainerVariable")
diagram_tool_Navigation = Class(name="diagram::tool::Navigation")
diagram_filter_FilterDescription = Class(name="diagram::filter::FilterDescription", is_abstract=True)
diagram_filter_Filter = Class(name="diagram::filter::Filter", is_abstract=True)
diagram_filter_MappingFilter = Class(name="diagram::filter::MappingFilter")
Filter = Class(name="Filter")
diagram_filter_CompositeFilterDescription = Class(name="diagram::filter::CompositeFilterDescription")
FilterDescription = Class(name="FilterDescription")
tool_ElementDropVariable = Class(name="tool::ElementDropVariable")
tool_InitialContainerDropOperation = Class(name="tool::InitialContainerDropOperation")
diagram_filter_FilterVariable = Class(name="diagram::filter::FilterVariable")
SelectionDescription = Class(name="SelectionDescription")
diagram_concern_ConcernSet = Class(name="diagram::concern::ConcernSet")
diagram_concern_ConcernDescription = Class(name="diagram::concern::ConcernDescription")
filter_Filter = Class(name="filter::Filter")
diagram_filter_VariableFilter = Class(name="diagram::filter::VariableFilter")

# diagram_DDiagramElement class attributes and methods
diagram_DDiagramElement_tooltipText: Property = Property(name="tooltipText", type=StringType)
diagram_DDiagramElement_visible: Property = Property(name="visible", type=BooleanType)
diagram_DDiagramElement_m_getParentDiagram: Method = Method(name="getParentDiagram", parameters={}, type=DDiagram)
diagram_DDiagramElement.attributes={diagram_DDiagramElement_visible, diagram_DDiagramElement_tooltipText}
diagram_DDiagramElement.methods={diagram_DDiagramElement_m_getParentDiagram}

# diagram_DDiagram class attributes and methods
diagram_DDiagram_synchronized: Property = Property(name="synchronized", type=BooleanType)
diagram_DDiagram_isInLayoutingMode: Property = Property(name="isInLayoutingMode", type=BooleanType)
diagram_DDiagram_headerHeight: Property = Property(name="headerHeight", type=IntegerType)
diagram_DDiagram_m_getEdgesFromMapping: Method = Method(name="getEdgesFromMapping", parameters={Parameter(name='mapping')}, type=StringType)
diagram_DDiagram_m_getContainersFromMapping: Method = Method(name="getContainersFromMapping", parameters={Parameter(name='mapping')}, type=StringType)
diagram_DDiagram_m_getNodesFromMapping: Method = Method(name="getNodesFromMapping", parameters={Parameter(name='mapping')}, type=StringType)
diagram_DDiagram.attributes={diagram_DDiagram_synchronized, diagram_DDiagram_isInLayoutingMode, diagram_DDiagram_headerHeight}
diagram_DDiagram.methods={diagram_DDiagram_m_getNodesFromMapping, diagram_DDiagram_m_getEdgesFromMapping, diagram_DDiagram_m_getContainersFromMapping}

# DRepresentation class attributes and methods

# description_DocumentedElement class attributes and methods

# DragAndDropTarget class attributes and methods

# DValidable class attributes and methods

# DContainer class attributes and methods

# diagram_DNode class attributes and methods
diagram_DNode_width: Property = Property(name="width", type=StringType)
diagram_DNode_height: Property = Property(name="height", type=StringType)
diagram_DNode_labelPosition: Property = Property(name="labelPosition", type=StringType)
diagram_DNode_resizeKind: Property = Property(name="resizeKind", type=StringType)
diagram_DNode.attributes={diagram_DNode_resizeKind, diagram_DNode_height, diagram_DNode_labelPosition, diagram_DNode_width}

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

# DiagramDescription class attributes and methods

# diagram_DEdge class attributes and methods
diagram_DEdge_size: Property = Property(name="size", type=StringType)
diagram_DEdge_arrangeConstraints: Property = Property(name="arrangeConstraints", type=StringType)
diagram_DEdge_beginLabel: Property = Property(name="beginLabel", type=StringType)
diagram_DEdge_endLabel: Property = Property(name="endLabel", type=StringType)
diagram_DEdge_routingStyle: Property = Property(name="routingStyle", type=StringType)
diagram_DEdge_isFold: Property = Property(name="isFold", type=BooleanType)
diagram_DEdge_isMockEdge: Property = Property(name="isMockEdge", type=BooleanType)
diagram_DEdge_m_isRootFolding: Method = Method(name="isRootFolding", parameters={}, type=BooleanType)
diagram_DEdge.attributes={diagram_DEdge_beginLabel, diagram_DEdge_isFold, diagram_DEdge_size, diagram_DEdge_endLabel, diagram_DEdge_routingStyle, diagram_DEdge_isMockEdge, diagram_DEdge_arrangeConstraints}
diagram_DEdge.methods={diagram_DEdge_m_isRootFolding}

# validation_ValidationRule class attributes and methods

# tool_BehaviorTool class attributes and methods

# diagram_FilterVariableHistory class attributes and methods

# Layer class attributes and methods

# diagram_Decoration class attributes and methods

# DiagramElementMapping class attributes and methods

# diagram_GraphicalFilter class attributes and methods

# diagram_HideFilter class attributes and methods

# GraphicalFilter class attributes and methods

# diagram_HideLabelFilter class attributes and methods

# diagram_FoldingPointFilter class attributes and methods

# diagram_FoldingFilter class attributes and methods

# diagram_AppliedCompositeFilters class attributes and methods

# diagram_DSemanticDiagram class attributes and methods

# DDiagram class attributes and methods

# DSemanticDecorator class attributes and methods

# DRepresentationElement class attributes and methods

# DNavigable class attributes and methods

# AbstractDNode class attributes and methods

# EdgeTarget class attributes and methods

# diagram_NodeStyle class attributes and methods
diagram_NodeStyle_labelPosition: Property = Property(name="labelPosition", type=StringType)
diagram_NodeStyle_hideLabelByDefault: Property = Property(name="hideLabelByDefault", type=BooleanType)
diagram_NodeStyle.attributes={diagram_NodeStyle_hideLabelByDefault, diagram_NodeStyle_labelPosition}

# diagram_Style class attributes and methods

# NodeMapping class attributes and methods

# filter_CompositeFilterDescription class attributes and methods

# diagram_AbsoluteBoundsFilter class attributes and methods
diagram_AbsoluteBoundsFilter_x: Property = Property(name="x", type=StringType)
diagram_AbsoluteBoundsFilter_y: Property = Property(name="y", type=StringType)
diagram_AbsoluteBoundsFilter_height: Property = Property(name="height", type=StringType)
diagram_AbsoluteBoundsFilter_width: Property = Property(name="width", type=StringType)
diagram_AbsoluteBoundsFilter.attributes={diagram_AbsoluteBoundsFilter_x, diagram_AbsoluteBoundsFilter_y, diagram_AbsoluteBoundsFilter_width, diagram_AbsoluteBoundsFilter_height}

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

# diagram_EdgeStyle class attributes and methods
diagram_EdgeStyle_lineStyle: Property = Property(name="lineStyle", type=StringType)
diagram_EdgeStyle_sourceArrow: Property = Property(name="sourceArrow", type=StringType)
diagram_EdgeStyle_targetArrow: Property = Property(name="targetArrow", type=StringType)
diagram_EdgeStyle_foldingStyle: Property = Property(name="foldingStyle", type=StringType)
diagram_EdgeStyle_size: Property = Property(name="size", type=StringType)
diagram_EdgeStyle_routingStyle: Property = Property(name="routingStyle", type=StringType)
diagram_EdgeStyle.attributes={diagram_EdgeStyle_size, diagram_EdgeStyle_lineStyle, diagram_EdgeStyle_sourceArrow, diagram_EdgeStyle_foldingStyle, diagram_EdgeStyle_routingStyle, diagram_EdgeStyle_targetArrow}

# diagram_EdgeTarget class attributes and methods

# IEdgeMapping class attributes and methods

# diagram_DNodeList class attributes and methods
diagram_DNodeList_lineWidth: Property = Property(name="lineWidth", type=IntegerType)
diagram_DNodeList.attributes={diagram_DNodeList_lineWidth}

# LabelStyle class attributes and methods

# Style class attributes and methods

# BorderedStyle class attributes and methods

# diagram_Dot class attributes and methods
diagram_Dot_strokeSizeComputationExpression: Property = Property(name="strokeSizeComputationExpression", type=StringType)
diagram_Dot.attributes={diagram_Dot_strokeSizeComputationExpression}

# NodeStyle class attributes and methods

# diagram_RGBValues class attributes and methods

# diagram_FlatContainerStyle class attributes and methods
diagram_FlatContainerStyle_backgroundStyle: Property = Property(name="backgroundStyle", type=StringType)
diagram_FlatContainerStyle.attributes={diagram_FlatContainerStyle_backgroundStyle}

# ContainerStyle class attributes and methods

# diagram_ShapeContainerStyle class attributes and methods
diagram_ShapeContainerStyle_shape: Property = Property(name="shape", type=StringType)
diagram_ShapeContainerStyle.attributes={diagram_ShapeContainerStyle_shape}

# diagram_GaugeSection class attributes and methods
diagram_GaugeSection_min: Property = Property(name="min", type=StringType)
diagram_GaugeSection_max: Property = Property(name="max", type=StringType)
diagram_GaugeSection_value: Property = Property(name="value", type=StringType)
diagram_GaugeSection_label: Property = Property(name="label", type=StringType)
diagram_GaugeSection.attributes={diagram_GaugeSection_value, diagram_GaugeSection_label, diagram_GaugeSection_max, diagram_GaugeSection_min}

# Customizable class attributes and methods

# diagram_Lozenge class attributes and methods
diagram_Lozenge_width: Property = Property(name="width", type=StringType)
diagram_Lozenge_height: Property = Property(name="height", type=StringType)
diagram_Lozenge.attributes={diagram_Lozenge_width, diagram_Lozenge_height}

# diagram_BundledImage class attributes and methods
diagram_BundledImage_shape: Property = Property(name="shape", type=StringType)
diagram_BundledImage.attributes={diagram_BundledImage_shape}

# diagram_WorkspaceImage class attributes and methods
diagram_WorkspaceImage_workspacePath: Property = Property(name="workspacePath", type=StringType)
diagram_WorkspaceImage.attributes={diagram_WorkspaceImage_workspacePath}

# diagram_CustomStyle class attributes and methods
diagram_CustomStyle_id: Property = Property(name="id", type=StringType)
diagram_CustomStyle.attributes={diagram_CustomStyle_id}

# diagram_Square class attributes and methods
diagram_Square_width: Property = Property(name="width", type=StringType)
diagram_Square_height: Property = Property(name="height", type=StringType)
diagram_Square.attributes={diagram_Square_width, diagram_Square_height}

# diagram_Ellipse class attributes and methods
diagram_Ellipse_verticalDiameter: Property = Property(name="verticalDiameter", type=StringType)
diagram_Ellipse_horizontalDiameter: Property = Property(name="horizontalDiameter", type=StringType)
diagram_Ellipse.attributes={diagram_Ellipse_verticalDiameter, diagram_Ellipse_horizontalDiameter}

# diagram_BeginLabelStyle class attributes and methods
diagram_BeginLabelStyle_m_getDescription: Method = Method(name="getDescription", parameters={}, type=StringType)
diagram_BeginLabelStyle_m_setDescription: Method = Method(name="setDescription", parameters={Parameter(name='description')})
diagram_BeginLabelStyle.methods={diagram_BeginLabelStyle_m_setDescription, diagram_BeginLabelStyle_m_getDescription}

# diagram_CenterLabelStyle class attributes and methods
diagram_CenterLabelStyle_m_getDescription: Method = Method(name="getDescription", parameters={}, type=StringType)
diagram_CenterLabelStyle_m_setDescription: Method = Method(name="setDescription", parameters={Parameter(name='description')})
diagram_CenterLabelStyle.methods={diagram_CenterLabelStyle_m_getDescription, diagram_CenterLabelStyle_m_setDescription}

# diagram_EndLabelStyle class attributes and methods
diagram_EndLabelStyle_m_getDescription: Method = Method(name="getDescription", parameters={}, type=StringType)
diagram_EndLabelStyle_m_setDescription: Method = Method(name="setDescription", parameters={Parameter(name='description')})
diagram_EndLabelStyle.methods={diagram_EndLabelStyle_m_getDescription, diagram_EndLabelStyle_m_setDescription}

# diagram_GaugeCompositeStyle class attributes and methods
diagram_GaugeCompositeStyle_alignment: Property = Property(name="alignment", type=StringType)
diagram_GaugeCompositeStyle.attributes={diagram_GaugeCompositeStyle_alignment}

# filter_FilterVariable class attributes and methods

# diagram_EObject class attributes and methods

# diagram_CollapseFilter class attributes and methods
diagram_CollapseFilter_width: Property = Property(name="width", type=IntegerType)
diagram_CollapseFilter_height: Property = Property(name="height", type=IntegerType)
diagram_CollapseFilter.attributes={diagram_CollapseFilter_height, diagram_CollapseFilter_width}

# diagram_IndirectlyCollapseFilter class attributes and methods

# CollapseFilter class attributes and methods

# BasicLabelStyle class attributes and methods

# diagram_BorderedStyle class attributes and methods
diagram_BorderedStyle_borderSize: Property = Property(name="borderSize", type=StringType)
diagram_BorderedStyle_borderSizeComputationExpression: Property = Property(name="borderSizeComputationExpression", type=StringType)
diagram_BorderedStyle.attributes={diagram_BorderedStyle_borderSize, diagram_BorderedStyle_borderSizeComputationExpression}

# diagram_Note class attributes and methods

# diagram_FilterVariableValue class attributes and methods

# diagram_ComputedStyleDescriptionRegistry class attributes and methods

# style_StyleDescription class attributes and methods

# diagram_DiagramElementMapping2ModelElement class attributes and methods

# diagram_ModelElement2ViewVariable class attributes and methods

# diagram_ViewVariable2ContainerVariable class attributes and methods

# diagram_ContainerVariable2StyleDescription class attributes and methods

# diagram_BracketEdgeStyle class attributes and methods

# EdgeStyle class attributes and methods

# EdgeMapping class attributes and methods

# validation_ValidationSet class attributes and methods

# concern_ConcernSet class attributes and methods

# diagram_DragAndDropTarget class attributes and methods
diagram_DragAndDropTarget_m_getDragAndDropDescription: Method = Method(name="getDragAndDropDescription", parameters={}, type=StringType)
diagram_DragAndDropTarget.methods={diagram_DragAndDropTarget_m_getDragAndDropDescription}

# diagram_description_DiagramDescription class attributes and methods
diagram_description_DiagramDescription_rootExpression: Property = Property(name="rootExpression", type=StringType)
diagram_description_DiagramDescription_domainClass: Property = Property(name="domainClass", type=StringType)
diagram_description_DiagramDescription_preconditionExpression: Property = Property(name="preconditionExpression", type=StringType)
diagram_description_DiagramDescription_enablePopupBars: Property = Property(name="enablePopupBars", type=BooleanType)
diagram_description_DiagramDescription_m_createDiagram: Method = Method(name="createDiagram", parameters={}, type=StringType)
diagram_description_DiagramDescription.attributes={diagram_description_DiagramDescription_domainClass, diagram_description_DiagramDescription_preconditionExpression, diagram_description_DiagramDescription_enablePopupBars, diagram_description_DiagramDescription_rootExpression}
diagram_description_DiagramDescription.methods={diagram_description_DiagramDescription_m_createDiagram}

# description_DragAndDropTargetDescription class attributes and methods

# description_RepresentationDescription class attributes and methods

# description_PasteTargetDescription class attributes and methods

# tool_RepresentationCreationDescription class attributes and methods

# Layout class attributes and methods

# tool_InitialOperation class attributes and methods

# AdditionalLayer class attributes and methods

# tool_AbstractToolDescription class attributes and methods

# EdgeMappingImport class attributes and methods

# tool_ToolSection class attributes and methods

# diagram_description_DiagramImportDescription class attributes and methods

# description_RepresentationImportDescription class attributes and methods

# description_DiagramDescription class attributes and methods

# diagram_description_DiagramElementMapping class attributes and methods
diagram_description_DiagramElementMapping_preconditionExpression: Property = Property(name="preconditionExpression", type=StringType)
diagram_description_DiagramElementMapping_semanticCandidatesExpression: Property = Property(name="semanticCandidatesExpression", type=StringType)
diagram_description_DiagramElementMapping_createElements: Property = Property(name="createElements", type=BooleanType)
diagram_description_DiagramElementMapping_semanticElements: Property = Property(name="semanticElements", type=StringType)
diagram_description_DiagramElementMapping_synchronizationLock: Property = Property(name="synchronizationLock", type=BooleanType)
diagram_description_DiagramElementMapping_m_checkPrecondition: Method = Method(name="checkPrecondition", parameters={Parameter(name='container'), Parameter(name='modelElement'), Parameter(name='containerView')}, type=BooleanType)
diagram_description_DiagramElementMapping_m_getAllMappings: Method = Method(name="getAllMappings", parameters={}, type=StringType)
diagram_description_DiagramElementMapping_m_isFrom: Method = Method(name="isFrom", parameters={Parameter(name='element')}, type=BooleanType)
diagram_description_DiagramElementMapping.attributes={diagram_description_DiagramElementMapping_createElements, diagram_description_DiagramElementMapping_synchronizationLock, diagram_description_DiagramElementMapping_semanticElements, diagram_description_DiagramElementMapping_preconditionExpression, diagram_description_DiagramElementMapping_semanticCandidatesExpression}
diagram_description_DiagramElementMapping.methods={diagram_description_DiagramElementMapping_m_isFrom, diagram_description_DiagramElementMapping_m_getAllMappings, diagram_description_DiagramElementMapping_m_checkPrecondition}

# description_RepresentationElementMapping class attributes and methods

# diagram_description_DiagramExtensionDescription class attributes and methods

# RepresentationExtensionDescription class attributes and methods

# tool_DirectEditLabel class attributes and methods

# tool_DeleteElementDescription class attributes and methods

# diagram_description_NodeMapping class attributes and methods
diagram_description_NodeMapping_m_createNode: Method = Method(name="createNode", parameters={Parameter(name='viewPoint'), Parameter(name='container'), Parameter(name='modelElement')}, type=StringType)
diagram_description_NodeMapping_m_updateNode: Method = Method(name="updateNode", parameters={Parameter(name='node')})
diagram_description_NodeMapping_m_updateListElement: Method = Method(name="updateListElement", parameters={Parameter(name='listElement')})
diagram_description_NodeMapping_m_getNodesCandidates: Method = Method(name="getNodesCandidates", parameters={Parameter(name='semanticOrigin'), Parameter(name='container')}, type=StringType)
diagram_description_NodeMapping_m_getNodesCandidates: Method = Method(name="getNodesCandidates", parameters={Parameter(name='containerView'), Parameter(name='container'), Parameter(name='semanticOrigin')}, type=StringType)
diagram_description_NodeMapping.methods={diagram_description_NodeMapping_m_getNodesCandidates, diagram_description_NodeMapping_m_getNodesCandidates, diagram_description_NodeMapping_m_updateNode, diagram_description_NodeMapping_m_createNode, diagram_description_NodeMapping_m_updateListElement}

# description_AbstractNodeMapping class attributes and methods

# tool_DoubleClickDescription class attributes and methods

# diagram_description_AbstractNodeMapping class attributes and methods
diagram_description_AbstractNodeMapping_domainClass: Property = Property(name="domainClass", type=StringType)
diagram_description_AbstractNodeMapping_m_clearDNodesDone: Method = Method(name="clearDNodesDone", parameters={})
diagram_description_AbstractNodeMapping_m_addDoneNode: Method = Method(name="addDoneNode", parameters={Parameter(name='node')})
diagram_description_AbstractNodeMapping_m_getAllBorderedNodeMappings: Method = Method(name="getAllBorderedNodeMappings", parameters={}, type=StringType)
diagram_description_AbstractNodeMapping_m_findDNodeFromEObject: Method = Method(name="findDNodeFromEObject", parameters={Parameter(name='eObject')}, type=DDiagramElement)
diagram_description_AbstractNodeMapping.attributes={diagram_description_AbstractNodeMapping_domainClass}
diagram_description_AbstractNodeMapping.methods={diagram_description_AbstractNodeMapping_m_findDNodeFromEObject, diagram_description_AbstractNodeMapping_m_getAllBorderedNodeMappings, diagram_description_AbstractNodeMapping_m_clearDNodesDone, diagram_description_AbstractNodeMapping_m_addDoneNode}

# description_DiagramElementMapping class attributes and methods

# style_NodeStyleDescription class attributes and methods

# ConditionalNodeStyleDescription class attributes and methods

# diagram_description_ContainerMapping class attributes and methods
diagram_description_ContainerMapping_childrenPresentation: Property = Property(name="childrenPresentation", type=StringType)
diagram_description_ContainerMapping_m_getBestStyle: Method = Method(name="getBestStyle", parameters={Parameter(name='containerVariable'), Parameter(name='modelElement'), Parameter(name='viewVariable')}, type=ContainerStyle)
diagram_description_ContainerMapping.attributes={diagram_description_ContainerMapping_childrenPresentation}
diagram_description_ContainerMapping.methods={diagram_description_ContainerMapping_m_getBestStyle}

# diagram_description_ContainerMappingImport class attributes and methods

# description_ContainerMapping class attributes and methods

# diagram_description_EdgeMapping class attributes and methods
diagram_description_EdgeMapping_sourceFinderExpression: Property = Property(name="sourceFinderExpression", type=StringType)
diagram_description_EdgeMapping_targetExpression: Property = Property(name="targetExpression", type=StringType)
diagram_description_EdgeMapping_domainClass: Property = Property(name="domainClass", type=StringType)
diagram_description_EdgeMapping_useDomainElement: Property = Property(name="useDomainElement", type=BooleanType)
diagram_description_EdgeMapping_pathExpression: Property = Property(name="pathExpression", type=StringType)
diagram_description_EdgeMapping_targetFinderExpression: Property = Property(name="targetFinderExpression", type=StringType)
diagram_description_EdgeMapping_m_createEdge: Method = Method(name="createEdge", parameters={Parameter(name='source'), Parameter(name='target'), Parameter(name='semanticTarget')}, type=StringType)
diagram_description_EdgeMapping_m_createEdge: Method = Method(name="createEdge", parameters={Parameter(name='semanticTarget'), Parameter(name='container'), Parameter(name='source'), Parameter(name='target')}, type=StringType)
diagram_description_EdgeMapping_m_getBestStyle: Method = Method(name="getBestStyle", parameters={Parameter(name='viewVariable'), Parameter(name='modelElement'), Parameter(name='containerVariable')}, type=EdgeStyle)
diagram_description_EdgeMapping_m_updateEdge: Method = Method(name="updateEdge", parameters={Parameter(name='viewEdge')})
diagram_description_EdgeMapping_m_getEdgeTargetCandidates: Method = Method(name="getEdgeTargetCandidates", parameters={Parameter(name='semanticOrigin'), Parameter(name='viewPoint')}, type=StringType)
diagram_description_EdgeMapping_m_getEdgeSourceCandidates: Method = Method(name="getEdgeSourceCandidates", parameters={Parameter(name='semanticOrigin'), Parameter(name='viewPoint')}, type=StringType)
diagram_description_EdgeMapping_m_getEdgeTargetCandidates: Method = Method(name="getEdgeTargetCandidates", parameters={Parameter(name='containerView'), Parameter(name='semanticOrigin'), Parameter(name='container')}, type=StringType)
diagram_description_EdgeMapping.attributes={diagram_description_EdgeMapping_domainClass, diagram_description_EdgeMapping_targetExpression, diagram_description_EdgeMapping_sourceFinderExpression, diagram_description_EdgeMapping_targetFinderExpression, diagram_description_EdgeMapping_pathExpression, diagram_description_EdgeMapping_useDomainElement}
diagram_description_EdgeMapping.methods={diagram_description_EdgeMapping_m_updateEdge, diagram_description_EdgeMapping_m_getBestStyle, diagram_description_EdgeMapping_m_getEdgeTargetCandidates, diagram_description_EdgeMapping_m_getEdgeTargetCandidates, diagram_description_EdgeMapping_m_getEdgeSourceCandidates, diagram_description_EdgeMapping_m_createEdge, diagram_description_EdgeMapping_m_createEdge}

# description_IEdgeMapping class attributes and methods

# style_ContainerStyleDescription class attributes and methods

# ConditionalContainerStyleDescription class attributes and methods

# diagram_description_NodeMappingImport class attributes and methods

# description_NodeMapping class attributes and methods

# description_AbstractMappingImport class attributes and methods

# style_EdgeStyleDescription class attributes and methods

# ConditionalEdgeStyleDescription class attributes and methods

# tool_ReconnectEdgeDescription class attributes and methods

# AbstractNodeMapping class attributes and methods

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
diagram_description_CompositeLayout.attributes={diagram_description_CompositeLayout_direction, diagram_description_CompositeLayout_padding}

# diagram_description_IEdgeMapping class attributes and methods
diagram_description_IEdgeMapping_m_getBestStyle: Method = Method(name="getBestStyle", parameters={Parameter(name='modelElement'), Parameter(name='viewVariable'), Parameter(name='containerVariable')}, type=EdgeStyle)
diagram_description_IEdgeMapping.methods={diagram_description_IEdgeMapping_m_getBestStyle}

# diagram_description_EdgeMappingImport class attributes and methods
diagram_description_EdgeMappingImport_inheritsAncestorFilters: Property = Property(name="inheritsAncestorFilters", type=BooleanType)
diagram_description_EdgeMappingImport.attributes={diagram_description_EdgeMappingImport_inheritsAncestorFilters}

# description_IdentifiedElement class attributes and methods

# DecorationDescriptionsSet class attributes and methods

# diagram_description_MappingBasedDecoration class attributes and methods

# DecorationDescription class attributes and methods

# diagram_description_Layer class attributes and methods
diagram_description_Layer_icon: Property = Property(name="icon", type=StringType)
diagram_description_Layer.attributes={diagram_description_Layer_icon}

# description_EndUserDocumentedElement class attributes and methods

# diagram_style_BorderedStyleDescription class attributes and methods
diagram_style_BorderedStyleDescription_borderSizeComputationExpression: Property = Property(name="borderSizeComputationExpression", type=StringType)
diagram_style_BorderedStyleDescription.attributes={diagram_style_BorderedStyleDescription_borderSizeComputationExpression}

# StyleDescription class attributes and methods

# ColorDescription class attributes and methods

# diagram_style_NodeStyleDescription class attributes and methods
diagram_style_NodeStyleDescription_sizeComputationExpression: Property = Property(name="sizeComputationExpression", type=StringType)
diagram_style_NodeStyleDescription_labelPosition: Property = Property(name="labelPosition", type=StringType)
diagram_style_NodeStyleDescription_hideLabelByDefault: Property = Property(name="hideLabelByDefault", type=BooleanType)
diagram_style_NodeStyleDescription_resizeKind: Property = Property(name="resizeKind", type=StringType)
diagram_style_NodeStyleDescription.attributes={diagram_style_NodeStyleDescription_labelPosition, diagram_style_NodeStyleDescription_sizeComputationExpression, diagram_style_NodeStyleDescription_resizeKind, diagram_style_NodeStyleDescription_hideLabelByDefault}

# style_BorderedStyleDescription class attributes and methods

# style_LabelStyleDescription class attributes and methods

# style_TooltipStyleDescription class attributes and methods

# diagram_style_CustomStyleDescription class attributes and methods
diagram_style_CustomStyleDescription_id: Property = Property(name="id", type=StringType)
diagram_style_CustomStyleDescription.attributes={diagram_style_CustomStyleDescription_id}

# NodeStyleDescription class attributes and methods

# diagram_style_SquareDescription class attributes and methods
diagram_style_SquareDescription_width: Property = Property(name="width", type=StringType)
diagram_style_SquareDescription_height: Property = Property(name="height", type=StringType)
diagram_style_SquareDescription.attributes={diagram_style_SquareDescription_width, diagram_style_SquareDescription_height}

# Customization class attributes and methods

# diagram_description_AdditionalLayer class attributes and methods
diagram_description_AdditionalLayer_activeByDefault: Property = Property(name="activeByDefault", type=BooleanType)
diagram_description_AdditionalLayer_optional: Property = Property(name="optional", type=BooleanType)
diagram_description_AdditionalLayer.attributes={diagram_description_AdditionalLayer_activeByDefault, diagram_description_AdditionalLayer_optional}

# diagram_description_DragAndDropTargetDescription class attributes and methods

# tool_ContainerDropDescription class attributes and methods

# diagram_style_EllipseNodeDescription class attributes and methods
diagram_style_EllipseNodeDescription_horizontalDiameterComputationExpression: Property = Property(name="horizontalDiameterComputationExpression", type=StringType)
diagram_style_EllipseNodeDescription_verticalDiameterComputationExpression: Property = Property(name="verticalDiameterComputationExpression", type=StringType)
diagram_style_EllipseNodeDescription.attributes={diagram_style_EllipseNodeDescription_verticalDiameterComputationExpression, diagram_style_EllipseNodeDescription_horizontalDiameterComputationExpression}

# diagram_style_BundledImageDescription class attributes and methods
diagram_style_BundledImageDescription_shape: Property = Property(name="shape", type=StringType)
diagram_style_BundledImageDescription.attributes={diagram_style_BundledImageDescription_shape}

# diagram_style_NoteDescription class attributes and methods

# diagram_style_DotDescription class attributes and methods
diagram_style_DotDescription_strokeSizeComputationExpression: Property = Property(name="strokeSizeComputationExpression", type=StringType)
diagram_style_DotDescription.attributes={diagram_style_DotDescription_strokeSizeComputationExpression}

# diagram_style_LozengeNodeDescription class attributes and methods
diagram_style_LozengeNodeDescription_widthComputationExpression: Property = Property(name="widthComputationExpression", type=StringType)
diagram_style_LozengeNodeDescription_heightComputationExpression: Property = Property(name="heightComputationExpression", type=StringType)
diagram_style_LozengeNodeDescription.attributes={diagram_style_LozengeNodeDescription_heightComputationExpression, diagram_style_LozengeNodeDescription_widthComputationExpression}

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
diagram_style_SizeComputationContainerStyleDescription.attributes={diagram_style_SizeComputationContainerStyleDescription_heightComputationExpression, diagram_style_SizeComputationContainerStyleDescription_widthComputationExpression}

# diagram_style_GaugeCompositeStyleDescription class attributes and methods
diagram_style_GaugeCompositeStyleDescription_alignment: Property = Property(name="alignment", type=StringType)
diagram_style_GaugeCompositeStyleDescription.attributes={diagram_style_GaugeCompositeStyleDescription_alignment}

# diagram_style_FlatContainerStyleDescription class attributes and methods
diagram_style_FlatContainerStyleDescription_backgroundStyle: Property = Property(name="backgroundStyle", type=StringType)
diagram_style_FlatContainerStyleDescription.attributes={diagram_style_FlatContainerStyleDescription_backgroundStyle}

# style_SizeComputationContainerStyleDescription class attributes and methods

# diagram_style_RoundedCornerStyleDescription class attributes and methods
diagram_style_RoundedCornerStyleDescription_arcWidth: Property = Property(name="arcWidth", type=StringType)
diagram_style_RoundedCornerStyleDescription_arcHeight: Property = Property(name="arcHeight", type=StringType)
diagram_style_RoundedCornerStyleDescription.attributes={diagram_style_RoundedCornerStyleDescription_arcHeight, diagram_style_RoundedCornerStyleDescription_arcWidth}

# diagram_style_ContainerStyleDescription class attributes and methods
diagram_style_ContainerStyleDescription_roundedCorner: Property = Property(name="roundedCorner", type=BooleanType)
diagram_style_ContainerStyleDescription.attributes={diagram_style_ContainerStyleDescription_roundedCorner}

# style_RoundedCornerStyleDescription class attributes and methods

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
diagram_style_EdgeStyleDescription.attributes={diagram_style_EdgeStyleDescription_sourceArrow, diagram_style_EdgeStyleDescription_routingStyle, diagram_style_EdgeStyleDescription_foldingStyle, diagram_style_EdgeStyleDescription_lineStyle, diagram_style_EdgeStyleDescription_sizeComputationExpression, diagram_style_EdgeStyleDescription_targetArrow}

# style_LabelBorderStyleDescription class attributes and methods

# diagram_style_ShapeContainerStyleDescription class attributes and methods
diagram_style_ShapeContainerStyleDescription_shape: Property = Property(name="shape", type=StringType)
diagram_style_ShapeContainerStyleDescription.attributes={diagram_style_ShapeContainerStyleDescription_shape}

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

# style_BeginLabelStyleDescription class attributes and methods

# style_CenterLabelStyleDescription class attributes and methods

# style_EndLabelStyleDescription class attributes and methods

# diagram_style_BeginLabelStyleDescription class attributes and methods

# BasicLabelStyleDescription class attributes and methods

# tool_NodeCreationVariable class attributes and methods

# tool_ContainerViewVariable class attributes and methods

# tool_InitialNodeCreationOperation class attributes and methods

# diagram_tool_EdgeCreationDescription class attributes and methods
diagram_tool_EdgeCreationDescription_iconPath: Property = Property(name="iconPath", type=StringType)
diagram_tool_EdgeCreationDescription_connectionStartPrecondition: Property = Property(name="connectionStartPrecondition", type=StringType)
diagram_tool_EdgeCreationDescription_m_getBestMapping: Method = Method(name="getBestMapping", parameters={Parameter(name='createdElements'), Parameter(name='source'), Parameter(name='target')}, type=StringType)
diagram_tool_EdgeCreationDescription.attributes={diagram_tool_EdgeCreationDescription_connectionStartPrecondition, diagram_tool_EdgeCreationDescription_iconPath}
diagram_tool_EdgeCreationDescription.methods={diagram_tool_EdgeCreationDescription_m_getBestMapping}

# diagram_tool_ToolGroup class attributes and methods

# ToolEntry class attributes and methods

# diagram_tool_ToolGroupExtension class attributes and methods

# tool_ToolGroup class attributes and methods

# diagram_tool_NodeCreationDescription class attributes and methods
diagram_tool_NodeCreationDescription_iconPath: Property = Property(name="iconPath", type=StringType)
diagram_tool_NodeCreationDescription.attributes={diagram_tool_NodeCreationDescription_iconPath}

# MappingBasedToolDescription class attributes and methods

# tool_SourceEdgeViewCreationVariable class attributes and methods

# tool_TargetEdgeViewCreationVariable class attributes and methods

# tool_InitEdgeCreationOperation class attributes and methods

# diagram_tool_ContainerCreationDescription class attributes and methods
diagram_tool_ContainerCreationDescription_iconPath: Property = Property(name="iconPath", type=StringType)
diagram_tool_ContainerCreationDescription.attributes={diagram_tool_ContainerCreationDescription_iconPath}

# tool_SourceEdgeCreationVariable class attributes and methods

# tool_TargetEdgeCreationVariable class attributes and methods

# diagram_tool_DeleteElementDescription class attributes and methods
diagram_tool_DeleteElementDescription_m_getMappings: Method = Method(name="getMappings", parameters={}, type=StringType)
diagram_tool_DeleteElementDescription.methods={diagram_tool_DeleteElementDescription_m_getMappings}

# tool_ElementDeleteVariable class attributes and methods

# tool_DeleteHook class attributes and methods

# diagram_tool_DoubleClickDescription class attributes and methods

# diagram_tool_ReconnectEdgeDescription class attributes and methods
diagram_tool_ReconnectEdgeDescription_reconnectionKind: Property = Property(name="reconnectionKind", type=StringType)
diagram_tool_ReconnectEdgeDescription_m_getMappings: Method = Method(name="getMappings", parameters={}, type=StringType)
diagram_tool_ReconnectEdgeDescription.attributes={diagram_tool_ReconnectEdgeDescription_reconnectionKind}
diagram_tool_ReconnectEdgeDescription.methods={diagram_tool_ReconnectEdgeDescription_m_getMappings}

# tool_ElementSelectVariable class attributes and methods

# tool_ElementDoubleClickVariable class attributes and methods

# diagram_tool_DeleteHook class attributes and methods
diagram_tool_DeleteHook_id: Property = Property(name="id", type=StringType)
diagram_tool_DeleteHook.attributes={diagram_tool_DeleteHook_id}

# tool_DeleteHookParameter class attributes and methods

# diagram_tool_DeleteHookParameter class attributes and methods
diagram_tool_DeleteHookParameter_name: Property = Property(name="name", type=StringType)
diagram_tool_DeleteHookParameter_value: Property = Property(name="value", type=StringType)
diagram_tool_DeleteHookParameter.attributes={diagram_tool_DeleteHookParameter_value, diagram_tool_DeleteHookParameter_name}

# tool_EditMaskVariables class attributes and methods

# diagram_tool_BehaviorTool class attributes and methods
diagram_tool_BehaviorTool_domainClass: Property = Property(name="domainClass", type=StringType)
diagram_tool_BehaviorTool.attributes={diagram_tool_BehaviorTool_domainClass}

# diagram_tool_RequestDescription class attributes and methods
diagram_tool_RequestDescription_type: Property = Property(name="type", type=StringType)
diagram_tool_RequestDescription.attributes={diagram_tool_RequestDescription_type}

# AbstractToolDescription class attributes and methods

# diagram_tool_DirectEditLabel class attributes and methods
diagram_tool_DirectEditLabel_inputLabelExpression: Property = Property(name="inputLabelExpression", type=StringType)
diagram_tool_DirectEditLabel_m_getMapping: Method = Method(name="getMapping", parameters={}, type=StringType)
diagram_tool_DirectEditLabel.attributes={diagram_tool_DirectEditLabel_inputLabelExpression}
diagram_tool_DirectEditLabel.methods={diagram_tool_DirectEditLabel_m_getMapping}

# diagram_tool_SourceEdgeCreationVariable class attributes and methods

# tool_AbstractVariable class attributes and methods

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

# diagram_tool_DiagramCreationDescription class attributes and methods

# RepresentationCreationDescription class attributes and methods

# diagram_tool_DiagramNavigationDescription class attributes and methods

# RepresentationNavigationDescription class attributes and methods

# diagram_tool_ContainerDropDescription class attributes and methods
diagram_tool_ContainerDropDescription_dragSource: Property = Property(name="dragSource", type=StringType)
diagram_tool_ContainerDropDescription_moveEdges: Property = Property(name="moveEdges", type=BooleanType)
diagram_tool_ContainerDropDescription_m_getBestMapping: Method = Method(name="getBestMapping", parameters={Parameter(name='droppedElement'), Parameter(name='targetContainer')}, type=StringType)
diagram_tool_ContainerDropDescription_m_getContainers: Method = Method(name="getContainers", parameters={}, type=StringType)
diagram_tool_ContainerDropDescription.attributes={diagram_tool_ContainerDropDescription_moveEdges, diagram_tool_ContainerDropDescription_dragSource}
diagram_tool_ContainerDropDescription.methods={diagram_tool_ContainerDropDescription_m_getContainers, diagram_tool_ContainerDropDescription_m_getBestMapping}

# tool_DropContainerVariable class attributes and methods

# diagram_tool_Navigation class attributes and methods
diagram_tool_Navigation_createIfNotExistent: Property = Property(name="createIfNotExistent", type=BooleanType)
diagram_tool_Navigation.attributes={diagram_tool_Navigation_createIfNotExistent}

# diagram_filter_FilterDescription class attributes and methods
diagram_filter_FilterDescription_m_isVisible: Method = Method(name="isVisible", parameters={Parameter(name='element')}, type=BooleanType)
diagram_filter_FilterDescription.methods={diagram_filter_FilterDescription_m_isVisible}

# diagram_filter_Filter class attributes and methods
diagram_filter_Filter_filterKind: Property = Property(name="filterKind", type=StringType)
diagram_filter_Filter_m_isVisible: Method = Method(name="isVisible", parameters={Parameter(name='element')}, type=BooleanType)
diagram_filter_Filter.attributes={diagram_filter_Filter_filterKind}
diagram_filter_Filter.methods={diagram_filter_Filter_m_isVisible}

# diagram_filter_MappingFilter class attributes and methods
diagram_filter_MappingFilter_semanticConditionExpression: Property = Property(name="semanticConditionExpression", type=StringType)
diagram_filter_MappingFilter_viewConditionExpression: Property = Property(name="viewConditionExpression", type=StringType)
diagram_filter_MappingFilter.attributes={diagram_filter_MappingFilter_semanticConditionExpression, diagram_filter_MappingFilter_viewConditionExpression}

# Filter class attributes and methods

# diagram_filter_CompositeFilterDescription class attributes and methods

# FilterDescription class attributes and methods

# tool_ElementDropVariable class attributes and methods

# tool_InitialContainerDropOperation class attributes and methods

# diagram_filter_FilterVariable class attributes and methods
diagram_filter_FilterVariable_name: Property = Property(name="name", type=StringType)
diagram_filter_FilterVariable.attributes={diagram_filter_FilterVariable_name}

# SelectionDescription class attributes and methods

# diagram_concern_ConcernSet class attributes and methods

# diagram_concern_ConcernDescription class attributes and methods

# filter_Filter class attributes and methods

# diagram_filter_VariableFilter class attributes and methods
diagram_filter_VariableFilter_semanticConditionExpression: Property = Property(name="semanticConditionExpression", type=StringType)
diagram_filter_VariableFilter_m_setFilterContext: Method = Method(name="setFilterContext", parameters={Parameter(name='variables')})
diagram_filter_VariableFilter.attributes={diagram_filter_VariableFilter_semanticConditionExpression}
diagram_filter_VariableFilter.methods={diagram_filter_VariableFilter_m_setFilterContext}

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
nodes8: BinaryAssociation = BinaryAssociation(
    name="nodes8",
    ends={
        Property(name="diagram_DNode", type=diagram_DDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagram9", type=diagram_DNode, multiplicity=Multiplicity(0, 9999))
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
hiddenElements29: BinaryAssociation = BinaryAssociation(
    name="hiddenElements29",
    ends={
        Property(name="diagram_DDiagramElement31", type=diagram_DDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DDiagram30", type=diagram_DDiagramElement, multiplicity=Multiplicity(0, 9999))
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
compositeFilterDescriptions41: BinaryAssociation = BinaryAssociation(
    name="compositeFilterDescriptions41",
    ends={
        Property(name="filter_CompositeFilterDescription", type=diagram_AppliedCompositeFilters, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_AppliedCompositeFilters", type=filter_CompositeFilterDescription, multiplicity=Multiplicity(0, 9999))
    }
)
ownedBorderedNodes42: BinaryAssociation = BinaryAssociation(
    name="ownedBorderedNodes42",
    ends={
        Property(name="diagram_DNode43", type=diagram_AbstractDNode, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_AbstractDNode", type=diagram_DNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
targetNode91: BinaryAssociation = BinaryAssociation(
    name="targetNode91",
    ends={
        Property(name="EdgeTarget92", type=diagram_DEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingEdges", type=diagram_EdgeTarget, multiplicity=Multiplicity(1, 1))
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
backgroundColor100: BinaryAssociation = BinaryAssociation(
    name="backgroundColor100",
    ends={
        Property(name="diagram_RGBValues", type=diagram_Dot, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_Dot", type=diagram_RGBValues, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actualMapping93: BinaryAssociation = BinaryAssociation(
    name="actualMapping93",
    ends={
        Property(name="IEdgeMapping", type=diagram_DEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DEdge94", type=IEdgeMapping, multiplicity=Multiplicity(1, 1))
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
foregroundColor103: BinaryAssociation = BinaryAssociation(
    name="foregroundColor103",
    ends={
        Property(name="diagram_RGBValues105", type=diagram_GaugeSection, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_GaugeSection104", type=diagram_RGBValues, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
backgroundColor106: BinaryAssociation = BinaryAssociation(
    name="backgroundColor106",
    ends={
        Property(name="diagram_RGBValues107", type=diagram_FlatContainerStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_FlatContainerStyle", type=diagram_RGBValues, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
foregroundColor108: BinaryAssociation = BinaryAssociation(
    name="foregroundColor108",
    ends={
        Property(name="diagram_RGBValues110", type=diagram_FlatContainerStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_FlatContainerStyle109", type=diagram_RGBValues, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
backgroundColor111: BinaryAssociation = BinaryAssociation(
    name="backgroundColor111",
    ends={
        Property(name="diagram_RGBValues112", type=diagram_ShapeContainerStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_ShapeContainerStyle", type=diagram_RGBValues, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
backgroundColor101: BinaryAssociation = BinaryAssociation(
    name="backgroundColor101",
    ends={
        Property(name="diagram_RGBValues102", type=diagram_GaugeSection, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_GaugeSection", type=diagram_RGBValues, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
color115: BinaryAssociation = BinaryAssociation(
    name="color115",
    ends={
        Property(name="diagram_RGBValues116", type=diagram_Ellipse, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_Ellipse", type=diagram_RGBValues, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
color117: BinaryAssociation = BinaryAssociation(
    name="color117",
    ends={
        Property(name="diagram_RGBValues118", type=diagram_Lozenge, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_Lozenge", type=diagram_RGBValues, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
color119: BinaryAssociation = BinaryAssociation(
    name="color119",
    ends={
        Property(name="diagram_RGBValues120", type=diagram_BundledImage, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_BundledImage", type=diagram_RGBValues, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
color113: BinaryAssociation = BinaryAssociation(
    name="color113",
    ends={
        Property(name="diagram_RGBValues114", type=diagram_Square, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_Square", type=diagram_RGBValues, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
strokeColor124: BinaryAssociation = BinaryAssociation(
    name="strokeColor124",
    ends={
        Property(name="diagram_RGBValues126", type=diagram_EdgeStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_EdgeStyle125", type=diagram_RGBValues, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
beginLabelStyle127: BinaryAssociation = BinaryAssociation(
    name="beginLabelStyle127",
    ends={
        Property(name="diagram_BeginLabelStyle", type=diagram_EdgeStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_EdgeStyle128", type=diagram_BeginLabelStyle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
centerLabelStyle129: BinaryAssociation = BinaryAssociation(
    name="centerLabelStyle129",
    ends={
        Property(name="diagram_CenterLabelStyle", type=diagram_EdgeStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_EdgeStyle130", type=diagram_CenterLabelStyle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
endLabelStyle131: BinaryAssociation = BinaryAssociation(
    name="endLabelStyle131",
    ends={
        Property(name="diagram_EndLabelStyle", type=diagram_EdgeStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_EdgeStyle132", type=diagram_EndLabelStyle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
outgoingEdges121: BinaryAssociation = BinaryAssociation(
    name="outgoingEdges121",
    ends={
        Property(name="DEdge", type=diagram_EdgeTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceNode", type=diagram_DEdge, multiplicity=Multiplicity(0, 9999))
    }
)
incomingEdges122: BinaryAssociation = BinaryAssociation(
    name="incomingEdges122",
    ends={
        Property(name="DEdge123", type=diagram_EdgeTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="targetNode", type=diagram_DEdge, multiplicity=Multiplicity(0, 9999))
    }
)
sections133: BinaryAssociation = BinaryAssociation(
    name="sections133",
    ends={
        Property(name="diagram_GaugeSection134", type=diagram_GaugeCompositeStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_GaugeCompositeStyle", type=diagram_GaugeSection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variableDefinition141: BinaryAssociation = BinaryAssociation(
    name="variableDefinition141",
    ends={
        Property(name="filter_FilterVariable", type=diagram_FilterVariableValue, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_FilterVariableValue142", type=filter_FilterVariable, multiplicity=Multiplicity(1, 1))
    }
)
modelElement143: BinaryAssociation = BinaryAssociation(
    name="modelElement143",
    ends={
        Property(name="diagram_EObject", type=diagram_FilterVariableValue, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_FilterVariableValue144", type=diagram_EObject, multiplicity=Multiplicity(1, 1))
    }
)
borderColor135: BinaryAssociation = BinaryAssociation(
    name="borderColor135",
    ends={
        Property(name="diagram_RGBValues136", type=diagram_BorderedStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_BorderedStyle", type=diagram_RGBValues, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
color137: BinaryAssociation = BinaryAssociation(
    name="color137",
    ends={
        Property(name="diagram_RGBValues138", type=diagram_Note, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_Note", type=diagram_RGBValues, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedValues139: BinaryAssociation = BinaryAssociation(
    name="ownedValues139",
    ends={
        Property(name="diagram_FilterVariableValue", type=diagram_FilterVariableHistory, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_FilterVariableHistory140", type=diagram_FilterVariableValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
computedStyleDescriptions145: BinaryAssociation = BinaryAssociation(
    name="computedStyleDescriptions145",
    ends={
        Property(name="style_StyleDescription", type=diagram_ComputedStyleDescriptionRegistry, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_ComputedStyleDescriptionRegistry", type=style_StyleDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cache146: BinaryAssociation = BinaryAssociation(
    name="cache146",
    ends={
        Property(name="diagram_DiagramElementMapping2ModelElement", type=diagram_ComputedStyleDescriptionRegistry, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_ComputedStyleDescriptionRegistry147", type=diagram_DiagramElementMapping2ModelElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key148: BinaryAssociation = BinaryAssociation(
    name="key148",
    ends={
        Property(name="DiagramElementMapping150", type=diagram_DiagramElementMapping2ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DiagramElementMapping2ModelElement149", type=DiagramElementMapping, multiplicity=Multiplicity(1, 1))
    }
)
value151: BinaryAssociation = BinaryAssociation(
    name="value151",
    ends={
        Property(name="diagram_ModelElement2ViewVariable", type=diagram_DiagramElementMapping2ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_DiagramElementMapping2ModelElement152", type=diagram_ModelElement2ViewVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key153: BinaryAssociation = BinaryAssociation(
    name="key153",
    ends={
        Property(name="diagram_EObject155", type=diagram_ModelElement2ViewVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_ModelElement2ViewVariable154", type=diagram_EObject, multiplicity=Multiplicity(1, 1))
    }
)
value156: BinaryAssociation = BinaryAssociation(
    name="value156",
    ends={
        Property(name="diagram_ViewVariable2ContainerVariable", type=diagram_ModelElement2ViewVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_ModelElement2ViewVariable157", type=diagram_ViewVariable2ContainerVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key158: BinaryAssociation = BinaryAssociation(
    name="key158",
    ends={
        Property(name="diagram_EObject160", type=diagram_ViewVariable2ContainerVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_ViewVariable2ContainerVariable159", type=diagram_EObject, multiplicity=Multiplicity(1, 1))
    }
)
value161: BinaryAssociation = BinaryAssociation(
    name="value161",
    ends={
        Property(name="diagram_ContainerVariable2StyleDescription", type=diagram_ViewVariable2ContainerVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_ViewVariable2ContainerVariable162", type=diagram_ContainerVariable2StyleDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
filters169: BinaryAssociation = BinaryAssociation(
    name="filters169",
    ends={
        Property(name="filter_FilterDescription170", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription", type=filter_FilterDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allEdgeMappings171: BinaryAssociation = BinaryAssociation(
    name="allEdgeMappings171",
    ends={
        Property(name="EdgeMapping", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription172", type=EdgeMapping, multiplicity=Multiplicity(0, 9999))
    }
)
allNodeMappings173: BinaryAssociation = BinaryAssociation(
    name="allNodeMappings173",
    ends={
        Property(name="NodeMapping175", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription174", type=NodeMapping, multiplicity=Multiplicity(0, 9999))
    }
)
allContainerMappings176: BinaryAssociation = BinaryAssociation(
    name="allContainerMappings176",
    ends={
        Property(name="ContainerMapping178", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription177", type=ContainerMapping, multiplicity=Multiplicity(0, 9999))
    }
)
validationSet179: BinaryAssociation = BinaryAssociation(
    name="validationSet179",
    ends={
        Property(name="validation_ValidationSet", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription180", type=validation_ValidationSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
concerns181: BinaryAssociation = BinaryAssociation(
    name="concerns181",
    ends={
        Property(name="concern_ConcernSet", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription182", type=concern_ConcernSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
key163: BinaryAssociation = BinaryAssociation(
    name="key163",
    ends={
        Property(name="diagram_EObject165", type=diagram_ContainerVariable2StyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_ContainerVariable2StyleDescription164", type=diagram_EObject, multiplicity=Multiplicity(1, 1))
    }
)
value166: BinaryAssociation = BinaryAssociation(
    name="value166",
    ends={
        Property(name="style_StyleDescription168", type=diagram_ContainerVariable2StyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_ContainerVariable2StyleDescription167", type=style_StyleDescription, multiplicity=Multiplicity(0, 1))
    }
)
defaultConcern185: BinaryAssociation = BinaryAssociation(
    name="defaultConcern185",
    ends={
        Property(name="concern_ConcernDescription187", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription186", type=concern_ConcernDescription, multiplicity=Multiplicity(0, 1))
    }
)
init188: BinaryAssociation = BinaryAssociation(
    name="init188",
    ends={
        Property(name="tool_RepresentationCreationDescription", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription189", type=tool_RepresentationCreationDescription, multiplicity=Multiplicity(0, 1))
    }
)
layout190: BinaryAssociation = BinaryAssociation(
    name="layout190",
    ends={
        Property(name="Layout", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription191", type=Layout, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
diagramInitialisation192: BinaryAssociation = BinaryAssociation(
    name="diagramInitialisation192",
    ends={
        Property(name="tool_InitialOperation", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription193", type=tool_InitialOperation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultLayer194: BinaryAssociation = BinaryAssociation(
    name="defaultLayer194",
    ends={
        Property(name="Layer196", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription195", type=Layer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
additionalLayers197: BinaryAssociation = BinaryAssociation(
    name="additionalLayers197",
    ends={
        Property(name="AdditionalLayer", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription198", type=AdditionalLayer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allLayers199: BinaryAssociation = BinaryAssociation(
    name="allLayers199",
    ends={
        Property(name="Layer201", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription200", type=Layer, multiplicity=Multiplicity(0, 9999))
    }
)
allTools183: BinaryAssociation = BinaryAssociation(
    name="allTools183",
    ends={
        Property(name="tool_AbstractToolDescription", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription184", type=tool_AbstractToolDescription, multiplicity=Multiplicity(0, 9999))
    }
)
edgeMappingImports211: BinaryAssociation = BinaryAssociation(
    name="edgeMappingImports211",
    ends={
        Property(name="EdgeMappingImport", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription212", type=EdgeMappingImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containerMappings213: BinaryAssociation = BinaryAssociation(
    name="containerMappings213",
    ends={
        Property(name="ContainerMapping215", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription214", type=ContainerMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reusedMappings216: BinaryAssociation = BinaryAssociation(
    name="reusedMappings216",
    ends={
        Property(name="DiagramElementMapping218", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription217", type=DiagramElementMapping, multiplicity=Multiplicity(0, 9999))
    }
)
toolSection219: BinaryAssociation = BinaryAssociation(
    name="toolSection219",
    ends={
        Property(name="tool_ToolSection", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription220", type=tool_ToolSection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
reusedTools221: BinaryAssociation = BinaryAssociation(
    name="reusedTools221",
    ends={
        Property(name="tool_AbstractToolDescription223", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription222", type=tool_AbstractToolDescription, multiplicity=Multiplicity(0, 9999))
    }
)
allActivatedTools202: BinaryAssociation = BinaryAssociation(
    name="allActivatedTools202",
    ends={
        Property(name="tool_AbstractToolDescription204", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription203", type=tool_AbstractToolDescription, multiplicity=Multiplicity(0, 9999))
    }
)
nodeMappings205: BinaryAssociation = BinaryAssociation(
    name="nodeMappings205",
    ends={
        Property(name="NodeMapping207", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription206", type=NodeMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edgeMappings208: BinaryAssociation = BinaryAssociation(
    name="edgeMappings208",
    ends={
        Property(name="EdgeMapping210", type=diagram_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramDescription209", type=EdgeMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedDiagram224: BinaryAssociation = BinaryAssociation(
    name="importedDiagram224",
    ends={
        Property(name="DiagramDescription225", type=diagram_description_DiagramImportDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramImportDescription", type=DiagramDescription, multiplicity=Multiplicity(0, 1))
    }
)
layers226: BinaryAssociation = BinaryAssociation(
    name="layers226",
    ends={
        Property(name="AdditionalLayer227", type=diagram_description_DiagramExtensionDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramExtensionDescription", type=AdditionalLayer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
validationSet228: BinaryAssociation = BinaryAssociation(
    name="validationSet228",
    ends={
        Property(name="validation_ValidationSet230", type=diagram_description_DiagramExtensionDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramExtensionDescription229", type=validation_ValidationSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
concerns231: BinaryAssociation = BinaryAssociation(
    name="concerns231",
    ends={
        Property(name="concern_ConcernSet233", type=diagram_description_DiagramExtensionDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramExtensionDescription232", type=concern_ConcernSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
labelDirectEdit235: BinaryAssociation = BinaryAssociation(
    name="labelDirectEdit235",
    ends={
        Property(name="tool_DirectEditLabel", type=diagram_description_DiagramElementMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramElementMapping236", type=tool_DirectEditLabel, multiplicity=Multiplicity(0, 1))
    }
)
deletionDescription234: BinaryAssociation = BinaryAssociation(
    name="deletionDescription234",
    ends={
        Property(name="tool_DeleteElementDescription", type=diagram_description_DiagramElementMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DiagramElementMapping", type=tool_DeleteElementDescription, multiplicity=Multiplicity(0, 1))
    }
)
borderedNodeMappings238: BinaryAssociation = BinaryAssociation(
    name="borderedNodeMappings238",
    ends={
        Property(name="NodeMapping239", type=diagram_description_AbstractNodeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_AbstractNodeMapping", type=NodeMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reusedBorderedNodeMappings240: BinaryAssociation = BinaryAssociation(
    name="reusedBorderedNodeMappings240",
    ends={
        Property(name="NodeMapping242", type=diagram_description_AbstractNodeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_AbstractNodeMapping241", type=NodeMapping, multiplicity=Multiplicity(0, 9999))
    }
)
doubleClickDescription237: BinaryAssociation = BinaryAssociation(
    name="doubleClickDescription237",
    ends={
        Property(name="description", type=diagram_description_DiagramElementMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="tool", type=tool_DoubleClickDescription, multiplicity=Multiplicity(0, 1))
    }
)
style243: BinaryAssociation = BinaryAssociation(
    name="style243",
    ends={
        Property(name="style_NodeStyleDescription", type=diagram_description_NodeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_NodeMapping", type=style_NodeStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditionnalStyles244: BinaryAssociation = BinaryAssociation(
    name="conditionnalStyles244",
    ends={
        Property(name="ConditionalNodeStyleDescription", type=diagram_description_NodeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_NodeMapping245", type=ConditionalNodeStyleDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subNodeMappings246: BinaryAssociation = BinaryAssociation(
    name="subNodeMappings246",
    ends={
        Property(name="NodeMapping247", type=diagram_description_ContainerMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_ContainerMapping", type=NodeMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allNodeMappings248: BinaryAssociation = BinaryAssociation(
    name="allNodeMappings248",
    ends={
        Property(name="NodeMapping250", type=diagram_description_ContainerMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_ContainerMapping249", type=NodeMapping, multiplicity=Multiplicity(0, 9999))
    }
)
reusedNodeMappings251: BinaryAssociation = BinaryAssociation(
    name="reusedNodeMappings251",
    ends={
        Property(name="NodeMapping253", type=diagram_description_ContainerMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_ContainerMapping252", type=NodeMapping, multiplicity=Multiplicity(0, 9999))
    }
)
subContainerMappings254: BinaryAssociation = BinaryAssociation(
    name="subContainerMappings254",
    ends={
        Property(name="ContainerMapping256", type=diagram_description_ContainerMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_ContainerMapping255", type=ContainerMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reusedContainerMappings257: BinaryAssociation = BinaryAssociation(
    name="reusedContainerMappings257",
    ends={
        Property(name="ContainerMapping259", type=diagram_description_ContainerMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_ContainerMapping258", type=ContainerMapping, multiplicity=Multiplicity(0, 9999))
    }
)
importedMapping269: BinaryAssociation = BinaryAssociation(
    name="importedMapping269",
    ends={
        Property(name="ContainerMapping270", type=diagram_description_ContainerMappingImport, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_ContainerMappingImport", type=ContainerMapping, multiplicity=Multiplicity(1, 1))
    }
)
allContainerMappings260: BinaryAssociation = BinaryAssociation(
    name="allContainerMappings260",
    ends={
        Property(name="ContainerMapping262", type=diagram_description_ContainerMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_ContainerMapping261", type=ContainerMapping, multiplicity=Multiplicity(0, 9999))
    }
)
style263: BinaryAssociation = BinaryAssociation(
    name="style263",
    ends={
        Property(name="style_ContainerStyleDescription", type=diagram_description_ContainerMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_ContainerMapping264", type=style_ContainerStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditionnalStyles265: BinaryAssociation = BinaryAssociation(
    name="conditionnalStyles265",
    ends={
        Property(name="ConditionalContainerStyleDescription", type=diagram_description_ContainerMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_ContainerMapping266", type=ConditionalContainerStyleDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedMapping267: BinaryAssociation = BinaryAssociation(
    name="importedMapping267",
    ends={
        Property(name="NodeMapping268", type=diagram_description_NodeMappingImport, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_NodeMappingImport", type=NodeMapping, multiplicity=Multiplicity(1, 1))
    }
)
style276: BinaryAssociation = BinaryAssociation(
    name="style276",
    ends={
        Property(name="style_EdgeStyleDescription", type=diagram_description_EdgeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_EdgeMapping277", type=style_EdgeStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditionnalStyles278: BinaryAssociation = BinaryAssociation(
    name="conditionnalStyles278",
    ends={
        Property(name="ConditionalEdgeStyleDescription", type=diagram_description_EdgeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_EdgeMapping279", type=ConditionalEdgeStyleDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reconnections280: BinaryAssociation = BinaryAssociation(
    name="reconnections280",
    ends={
        Property(name="tool_ReconnectEdgeDescription", type=diagram_description_EdgeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_EdgeMapping281", type=tool_ReconnectEdgeDescription, multiplicity=Multiplicity(0, 9999))
    }
)
pathNodeMapping282: BinaryAssociation = BinaryAssociation(
    name="pathNodeMapping282",
    ends={
        Property(name="AbstractNodeMapping", type=diagram_description_EdgeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_EdgeMapping283", type=AbstractNodeMapping, multiplicity=Multiplicity(0, 9999))
    }
)
sourceMapping271: BinaryAssociation = BinaryAssociation(
    name="sourceMapping271",
    ends={
        Property(name="DiagramElementMapping272", type=diagram_description_EdgeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_EdgeMapping", type=DiagramElementMapping, multiplicity=Multiplicity(1, 9999))
    }
)
targetMapping273: BinaryAssociation = BinaryAssociation(
    name="targetMapping273",
    ends={
        Property(name="DiagramElementMapping275", type=diagram_description_EdgeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_EdgeMapping274", type=DiagramElementMapping, multiplicity=Multiplicity(1, 9999))
    }
)
style289: BinaryAssociation = BinaryAssociation(
    name="style289",
    ends={
        Property(name="style_NodeStyleDescription290", type=diagram_description_ConditionalNodeStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_ConditionalNodeStyleDescription", type=style_NodeStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
style291: BinaryAssociation = BinaryAssociation(
    name="style291",
    ends={
        Property(name="style_EdgeStyleDescription292", type=diagram_description_ConditionalEdgeStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_ConditionalEdgeStyleDescription", type=style_EdgeStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
style293: BinaryAssociation = BinaryAssociation(
    name="style293",
    ends={
        Property(name="style_ContainerStyleDescription294", type=diagram_description_ConditionalContainerStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_ConditionalContainerStyleDescription", type=style_ContainerStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nodeMapping295: BinaryAssociation = BinaryAssociation(
    name="nodeMapping295",
    ends={
        Property(name="AbstractNodeMapping296", type=diagram_description_OrderedTreeLayout, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_OrderedTreeLayout", type=AbstractNodeMapping, multiplicity=Multiplicity(1, 9999))
    }
)
importedMapping284: BinaryAssociation = BinaryAssociation(
    name="importedMapping284",
    ends={
        Property(name="IEdgeMapping285", type=diagram_description_EdgeMappingImport, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_EdgeMappingImport", type=IEdgeMapping, multiplicity=Multiplicity(1, 1))
    }
)
conditionnalStyles286: BinaryAssociation = BinaryAssociation(
    name="conditionnalStyles286",
    ends={
        Property(name="ConditionalEdgeStyleDescription288", type=diagram_description_EdgeMappingImport, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_EdgeMappingImport287", type=ConditionalEdgeStyleDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edgeMappings301: BinaryAssociation = BinaryAssociation(
    name="edgeMappings301",
    ends={
        Property(name="EdgeMapping303", type=diagram_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_Layer302", type=EdgeMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edgeMappingImports304: BinaryAssociation = BinaryAssociation(
    name="edgeMappingImports304",
    ends={
        Property(name="EdgeMappingImport306", type=diagram_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_Layer305", type=EdgeMappingImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containerMappings307: BinaryAssociation = BinaryAssociation(
    name="containerMappings307",
    ends={
        Property(name="ContainerMapping309", type=diagram_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_Layer308", type=ContainerMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reusedMappings310: BinaryAssociation = BinaryAssociation(
    name="reusedMappings310",
    ends={
        Property(name="DiagramElementMapping312", type=diagram_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_Layer311", type=DiagramElementMapping, multiplicity=Multiplicity(0, 9999))
    }
)
allTools313: BinaryAssociation = BinaryAssociation(
    name="allTools313",
    ends={
        Property(name="tool_AbstractToolDescription315", type=diagram_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_Layer314", type=tool_AbstractToolDescription, multiplicity=Multiplicity(0, 9999))
    }
)
toolSections316: BinaryAssociation = BinaryAssociation(
    name="toolSections316",
    ends={
        Property(name="tool_ToolSection318", type=diagram_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_Layer317", type=tool_ToolSection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reusedTools319: BinaryAssociation = BinaryAssociation(
    name="reusedTools319",
    ends={
        Property(name="tool_AbstractToolDescription321", type=diagram_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_Layer320", type=tool_AbstractToolDescription, multiplicity=Multiplicity(0, 9999))
    }
)
decorationDescriptionsSet322: BinaryAssociation = BinaryAssociation(
    name="decorationDescriptionsSet322",
    ends={
        Property(name="DecorationDescriptionsSet", type=diagram_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_Layer323", type=DecorationDescriptionsSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mappings297: BinaryAssociation = BinaryAssociation(
    name="mappings297",
    ends={
        Property(name="DiagramElementMapping298", type=diagram_description_MappingBasedDecoration, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_MappingBasedDecoration", type=DiagramElementMapping, multiplicity=Multiplicity(1, 9999))
    }
)
nodeMappings299: BinaryAssociation = BinaryAssociation(
    name="nodeMappings299",
    ends={
        Property(name="NodeMapping300", type=diagram_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_Layer", type=NodeMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
borderColor330: BinaryAssociation = BinaryAssociation(
    name="borderColor330",
    ends={
        Property(name="ColorDescription", type=diagram_style_BorderedStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_BorderedStyleDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
allEdgeMappings324: BinaryAssociation = BinaryAssociation(
    name="allEdgeMappings324",
    ends={
        Property(name="EdgeMapping326", type=diagram_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_Layer325", type=EdgeMapping, multiplicity=Multiplicity(0, 9999))
    }
)
customization327: BinaryAssociation = BinaryAssociation(
    name="customization327",
    ends={
        Property(name="Customization", type=diagram_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_Layer328", type=Customization, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dropDescriptions329: BinaryAssociation = BinaryAssociation(
    name="dropDescriptions329",
    ends={
        Property(name="tool_ContainerDropDescription", type=diagram_description_DragAndDropTargetDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_description_DragAndDropTargetDescription", type=tool_ContainerDropDescription, multiplicity=Multiplicity(0, 9999))
    }
)
color333: BinaryAssociation = BinaryAssociation(
    name="color333",
    ends={
        Property(name="ColorDescription334", type=diagram_style_LozengeNodeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_LozengeNodeDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
color335: BinaryAssociation = BinaryAssociation(
    name="color335",
    ends={
        Property(name="ColorDescription336", type=diagram_style_EllipseNodeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_EllipseNodeDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
color337: BinaryAssociation = BinaryAssociation(
    name="color337",
    ends={
        Property(name="ColorDescription338", type=diagram_style_BundledImageDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_BundledImageDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
color339: BinaryAssociation = BinaryAssociation(
    name="color339",
    ends={
        Property(name="ColorDescription340", type=diagram_style_NoteDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_NoteDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
color331: BinaryAssociation = BinaryAssociation(
    name="color331",
    ends={
        Property(name="ColorDescription332", type=diagram_style_SquareDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_SquareDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
sections343: BinaryAssociation = BinaryAssociation(
    name="sections343",
    ends={
        Property(name="style_GaugeSectionDescription", type=diagram_style_GaugeCompositeStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_GaugeCompositeStyleDescription", type=style_GaugeSectionDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
backgroundColor344: BinaryAssociation = BinaryAssociation(
    name="backgroundColor344",
    ends={
        Property(name="ColorDescription345", type=diagram_style_GaugeSectionDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_GaugeSectionDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
foregroundColor346: BinaryAssociation = BinaryAssociation(
    name="foregroundColor346",
    ends={
        Property(name="ColorDescription348", type=diagram_style_GaugeSectionDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_GaugeSectionDescription347", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
backgroundColor341: BinaryAssociation = BinaryAssociation(
    name="backgroundColor341",
    ends={
        Property(name="ColorDescription342", type=diagram_style_DotDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_DotDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
backgroundColor349: BinaryAssociation = BinaryAssociation(
    name="backgroundColor349",
    ends={
        Property(name="ColorDescription350", type=diagram_style_FlatContainerStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_FlatContainerStyleDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
backgroundColor356: BinaryAssociation = BinaryAssociation(
    name="backgroundColor356",
    ends={
        Property(name="ColorDescription357", type=diagram_style_ShapeContainerStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_ShapeContainerStyleDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
strokeColor358: BinaryAssociation = BinaryAssociation(
    name="strokeColor358",
    ends={
        Property(name="ColorDescription359", type=diagram_style_EdgeStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_EdgeStyleDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
foregroundColor351: BinaryAssociation = BinaryAssociation(
    name="foregroundColor351",
    ends={
        Property(name="ColorDescription353", type=diagram_style_FlatContainerStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_FlatContainerStyleDescription352", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
labelBorderStyle354: BinaryAssociation = BinaryAssociation(
    name="labelBorderStyle354",
    ends={
        Property(name="style_LabelBorderStyleDescription", type=diagram_style_FlatContainerStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_FlatContainerStyleDescription355", type=style_LabelBorderStyleDescription, multiplicity=Multiplicity(0, 1))
    }
)
ownedTools366: BinaryAssociation = BinaryAssociation(
    name="ownedTools366",
    ends={
        Property(name="tool_ToolEntry", type=diagram_tool_ToolSection, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ToolSection", type=tool_ToolEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subSections367: BinaryAssociation = BinaryAssociation(
    name="subSections367",
    ends={
        Property(name="tool_ToolSection369", type=diagram_tool_ToolSection, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ToolSection368", type=tool_ToolSection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
popupMenus370: BinaryAssociation = BinaryAssociation(
    name="popupMenus370",
    ends={
        Property(name="tool_PopupMenu", type=diagram_tool_ToolSection, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ToolSection371", type=tool_PopupMenu, multiplicity=Multiplicity(0, 9999))
    }
)
reusedTools372: BinaryAssociation = BinaryAssociation(
    name="reusedTools372",
    ends={
        Property(name="tool_ToolEntry374", type=diagram_tool_ToolSection, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ToolSection373", type=tool_ToolEntry, multiplicity=Multiplicity(0, 9999))
    }
)
groupExtensions375: BinaryAssociation = BinaryAssociation(
    name="groupExtensions375",
    ends={
        Property(name="tool_ToolGroupExtension", type=diagram_tool_ToolSection, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ToolSection376", type=tool_ToolGroupExtension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
beginLabelStyleDescription360: BinaryAssociation = BinaryAssociation(
    name="beginLabelStyleDescription360",
    ends={
        Property(name="style_BeginLabelStyleDescription", type=diagram_style_EdgeStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_EdgeStyleDescription361", type=style_BeginLabelStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
centerLabelStyleDescription362: BinaryAssociation = BinaryAssociation(
    name="centerLabelStyleDescription362",
    ends={
        Property(name="style_CenterLabelStyleDescription", type=diagram_style_EdgeStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_EdgeStyleDescription363", type=style_CenterLabelStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
endLabelStyleDescription364: BinaryAssociation = BinaryAssociation(
    name="endLabelStyleDescription364",
    ends={
        Property(name="style_EndLabelStyleDescription", type=diagram_style_EdgeStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_style_EdgeStyleDescription365", type=style_EndLabelStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable385: BinaryAssociation = BinaryAssociation(
    name="variable385",
    ends={
        Property(name="tool_NodeCreationVariable", type=diagram_tool_NodeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_NodeCreationDescription386", type=tool_NodeCreationVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
viewVariable387: BinaryAssociation = BinaryAssociation(
    name="viewVariable387",
    ends={
        Property(name="tool_ContainerViewVariable", type=diagram_tool_NodeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_NodeCreationDescription388", type=tool_ContainerViewVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialOperation389: BinaryAssociation = BinaryAssociation(
    name="initialOperation389",
    ends={
        Property(name="tool_InitialNodeCreationOperation", type=diagram_tool_NodeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_NodeCreationDescription390", type=tool_InitialNodeCreationOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
extraMappings391: BinaryAssociation = BinaryAssociation(
    name="extraMappings391",
    ends={
        Property(name="AbstractNodeMapping393", type=diagram_tool_NodeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_NodeCreationDescription392", type=AbstractNodeMapping, multiplicity=Multiplicity(0, 9999))
    }
)
tools377: BinaryAssociation = BinaryAssociation(
    name="tools377",
    ends={
        Property(name="tool_AbstractToolDescription378", type=diagram_tool_ToolGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ToolGroup", type=tool_AbstractToolDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
group379: BinaryAssociation = BinaryAssociation(
    name="group379",
    ends={
        Property(name="tool_ToolGroup", type=diagram_tool_ToolGroupExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ToolGroupExtension", type=tool_ToolGroup, multiplicity=Multiplicity(1, 1))
    }
)
tools380: BinaryAssociation = BinaryAssociation(
    name="tools380",
    ends={
        Property(name="tool_AbstractToolDescription382", type=diagram_tool_ToolGroupExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ToolGroupExtension381", type=tool_AbstractToolDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodeMappings383: BinaryAssociation = BinaryAssociation(
    name="nodeMappings383",
    ends={
        Property(name="NodeMapping384", type=diagram_tool_NodeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_NodeCreationDescription", type=NodeMapping, multiplicity=Multiplicity(1, 9999))
    }
)
sourceViewVariable400: BinaryAssociation = BinaryAssociation(
    name="sourceViewVariable400",
    ends={
        Property(name="tool_SourceEdgeViewCreationVariable", type=diagram_tool_EdgeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_EdgeCreationDescription401", type=tool_SourceEdgeViewCreationVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
targetViewVariable402: BinaryAssociation = BinaryAssociation(
    name="targetViewVariable402",
    ends={
        Property(name="tool_TargetEdgeViewCreationVariable", type=diagram_tool_EdgeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_EdgeCreationDescription403", type=tool_TargetEdgeViewCreationVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialOperation404: BinaryAssociation = BinaryAssociation(
    name="initialOperation404",
    ends={
        Property(name="tool_InitEdgeCreationOperation", type=diagram_tool_EdgeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_EdgeCreationDescription405", type=tool_InitEdgeCreationOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
extraSourceMappings406: BinaryAssociation = BinaryAssociation(
    name="extraSourceMappings406",
    ends={
        Property(name="DiagramElementMapping408", type=diagram_tool_EdgeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_EdgeCreationDescription407", type=DiagramElementMapping, multiplicity=Multiplicity(0, 9999))
    }
)
extraTargetMappings409: BinaryAssociation = BinaryAssociation(
    name="extraTargetMappings409",
    ends={
        Property(name="DiagramElementMapping411", type=diagram_tool_EdgeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_EdgeCreationDescription410", type=DiagramElementMapping, multiplicity=Multiplicity(0, 9999))
    }
)
edgeMappings394: BinaryAssociation = BinaryAssociation(
    name="edgeMappings394",
    ends={
        Property(name="EdgeMapping395", type=diagram_tool_EdgeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_EdgeCreationDescription", type=EdgeMapping, multiplicity=Multiplicity(1, 9999))
    }
)
sourceVariable396: BinaryAssociation = BinaryAssociation(
    name="sourceVariable396",
    ends={
        Property(name="tool_SourceEdgeCreationVariable", type=diagram_tool_EdgeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_EdgeCreationDescription397", type=tool_SourceEdgeCreationVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
targetVariable398: BinaryAssociation = BinaryAssociation(
    name="targetVariable398",
    ends={
        Property(name="tool_TargetEdgeCreationVariable", type=diagram_tool_EdgeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_EdgeCreationDescription399", type=tool_TargetEdgeCreationVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
extraMappings423: BinaryAssociation = BinaryAssociation(
    name="extraMappings423",
    ends={
        Property(name="AbstractNodeMapping425", type=diagram_tool_ContainerCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ContainerCreationDescription424", type=AbstractNodeMapping, multiplicity=Multiplicity(0, 9999))
    }
)
element426: BinaryAssociation = BinaryAssociation(
    name="element426",
    ends={
        Property(name="tool_ElementDeleteVariable", type=diagram_tool_DeleteElementDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DeleteElementDescription", type=tool_ElementDeleteVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elementView427: BinaryAssociation = BinaryAssociation(
    name="elementView427",
    ends={
        Property(name="tool_ElementDeleteVariable429", type=diagram_tool_DeleteElementDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DeleteElementDescription428", type=tool_ElementDeleteVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
containerView430: BinaryAssociation = BinaryAssociation(
    name="containerView430",
    ends={
        Property(name="tool_ContainerViewVariable432", type=diagram_tool_DeleteElementDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DeleteElementDescription431", type=tool_ContainerViewVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialOperation433: BinaryAssociation = BinaryAssociation(
    name="initialOperation433",
    ends={
        Property(name="tool_InitialOperation435", type=diagram_tool_DeleteElementDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DeleteElementDescription434", type=tool_InitialOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
hook436: BinaryAssociation = BinaryAssociation(
    name="hook436",
    ends={
        Property(name="tool_DeleteHook", type=diagram_tool_DeleteElementDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DeleteElementDescription437", type=tool_DeleteHook, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mappings438: BinaryAssociation = BinaryAssociation(
    name="mappings438",
    ends={
        Property(name="description440", type=diagram_tool_DoubleClickDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="DiagramElementMapping439", type=DiagramElementMapping, multiplicity=Multiplicity(1, 9999))
    }
)
containerMappings412: BinaryAssociation = BinaryAssociation(
    name="containerMappings412",
    ends={
        Property(name="ContainerMapping413", type=diagram_tool_ContainerCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ContainerCreationDescription", type=ContainerMapping, multiplicity=Multiplicity(1, 9999))
    }
)
variable414: BinaryAssociation = BinaryAssociation(
    name="variable414",
    ends={
        Property(name="tool_NodeCreationVariable416", type=diagram_tool_ContainerCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ContainerCreationDescription415", type=tool_NodeCreationVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
viewVariable417: BinaryAssociation = BinaryAssociation(
    name="viewVariable417",
    ends={
        Property(name="tool_ContainerViewVariable419", type=diagram_tool_ContainerCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ContainerCreationDescription418", type=tool_ContainerViewVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialOperation420: BinaryAssociation = BinaryAssociation(
    name="initialOperation420",
    ends={
        Property(name="tool_InitialNodeCreationOperation422", type=diagram_tool_ContainerCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ContainerCreationDescription421", type=tool_InitialNodeCreationOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source449: BinaryAssociation = BinaryAssociation(
    name="source449",
    ends={
        Property(name="tool_SourceEdgeCreationVariable450", type=diagram_tool_ReconnectEdgeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ReconnectEdgeDescription", type=tool_SourceEdgeCreationVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target451: BinaryAssociation = BinaryAssociation(
    name="target451",
    ends={
        Property(name="tool_TargetEdgeCreationVariable453", type=diagram_tool_ReconnectEdgeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ReconnectEdgeDescription452", type=tool_TargetEdgeCreationVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sourceView454: BinaryAssociation = BinaryAssociation(
    name="sourceView454",
    ends={
        Property(name="tool_SourceEdgeViewCreationVariable456", type=diagram_tool_ReconnectEdgeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ReconnectEdgeDescription455", type=tool_SourceEdgeViewCreationVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
targetView457: BinaryAssociation = BinaryAssociation(
    name="targetView457",
    ends={
        Property(name="tool_TargetEdgeViewCreationVariable459", type=diagram_tool_ReconnectEdgeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ReconnectEdgeDescription458", type=tool_TargetEdgeViewCreationVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
element460: BinaryAssociation = BinaryAssociation(
    name="element460",
    ends={
        Property(name="tool_ElementSelectVariable", type=diagram_tool_ReconnectEdgeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ReconnectEdgeDescription461", type=tool_ElementSelectVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
element441: BinaryAssociation = BinaryAssociation(
    name="element441",
    ends={
        Property(name="tool_ElementDoubleClickVariable", type=diagram_tool_DoubleClickDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DoubleClickDescription", type=tool_ElementDoubleClickVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elementView442: BinaryAssociation = BinaryAssociation(
    name="elementView442",
    ends={
        Property(name="tool_ElementDoubleClickVariable444", type=diagram_tool_DoubleClickDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DoubleClickDescription443", type=tool_ElementDoubleClickVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initialOperation445: BinaryAssociation = BinaryAssociation(
    name="initialOperation445",
    ends={
        Property(name="tool_InitialOperation447", type=diagram_tool_DoubleClickDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DoubleClickDescription446", type=tool_InitialOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters448: BinaryAssociation = BinaryAssociation(
    name="parameters448",
    ends={
        Property(name="tool_DeleteHookParameter", type=diagram_tool_DeleteHook, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DeleteHook", type=tool_DeleteHookParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mask468: BinaryAssociation = BinaryAssociation(
    name="mask468",
    ends={
        Property(name="tool_EditMaskVariables", type=diagram_tool_DirectEditLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DirectEditLabel", type=tool_EditMaskVariables, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialOperation469: BinaryAssociation = BinaryAssociation(
    name="initialOperation469",
    ends={
        Property(name="tool_InitialOperation471", type=diagram_tool_DirectEditLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DirectEditLabel470", type=tool_InitialOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialOperation472: BinaryAssociation = BinaryAssociation(
    name="initialOperation472",
    ends={
        Property(name="tool_InitialOperation473", type=diagram_tool_BehaviorTool, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_BehaviorTool", type=tool_InitialOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialOperation462: BinaryAssociation = BinaryAssociation(
    name="initialOperation462",
    ends={
        Property(name="tool_InitialOperation464", type=diagram_tool_ReconnectEdgeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ReconnectEdgeDescription463", type=tool_InitialOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
edgeView465: BinaryAssociation = BinaryAssociation(
    name="edgeView465",
    ends={
        Property(name="tool_ElementSelectVariable467", type=diagram_tool_ReconnectEdgeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ReconnectEdgeDescription466", type=tool_ElementSelectVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mapping474: BinaryAssociation = BinaryAssociation(
    name="mapping474",
    ends={
        Property(name="DiagramElementMapping475", type=diagram_tool_CreateView, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_CreateView", type=DiagramElementMapping, multiplicity=Multiplicity(1, 1))
    }
)
diagramDescription476: BinaryAssociation = BinaryAssociation(
    name="diagramDescription476",
    ends={
        Property(name="DiagramDescription477", type=diagram_tool_Navigation, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_Navigation", type=DiagramDescription, multiplicity=Multiplicity(1, 1))
    }
)
diagramDescription478: BinaryAssociation = BinaryAssociation(
    name="diagramDescription478",
    ends={
        Property(name="DiagramDescription479", type=diagram_tool_DiagramCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DiagramCreationDescription", type=DiagramDescription, multiplicity=Multiplicity(1, 1))
    }
)
diagramDescription480: BinaryAssociation = BinaryAssociation(
    name="diagramDescription480",
    ends={
        Property(name="DiagramDescription481", type=diagram_tool_DiagramNavigationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_DiagramNavigationDescription", type=DiagramDescription, multiplicity=Multiplicity(1, 1))
    }
)
mappings482: BinaryAssociation = BinaryAssociation(
    name="mappings482",
    ends={
        Property(name="DiagramElementMapping483", type=diagram_tool_ContainerDropDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ContainerDropDescription", type=DiagramElementMapping, multiplicity=Multiplicity(0, 9999))
    }
)
oldContainer484: BinaryAssociation = BinaryAssociation(
    name="oldContainer484",
    ends={
        Property(name="tool_DropContainerVariable", type=diagram_tool_ContainerDropDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ContainerDropDescription485", type=tool_DropContainerVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mappings496: BinaryAssociation = BinaryAssociation(
    name="mappings496",
    ends={
        Property(name="DiagramElementMapping497", type=diagram_filter_MappingFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_filter_MappingFilter", type=DiagramElementMapping, multiplicity=Multiplicity(0, 9999))
    }
)
newContainer486: BinaryAssociation = BinaryAssociation(
    name="newContainer486",
    ends={
        Property(name="tool_DropContainerVariable488", type=diagram_tool_ContainerDropDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ContainerDropDescription487", type=tool_DropContainerVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
element489: BinaryAssociation = BinaryAssociation(
    name="element489",
    ends={
        Property(name="tool_ElementDropVariable", type=diagram_tool_ContainerDropDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ContainerDropDescription490", type=tool_ElementDropVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
newViewContainer491: BinaryAssociation = BinaryAssociation(
    name="newViewContainer491",
    ends={
        Property(name="tool_ContainerViewVariable493", type=diagram_tool_ContainerDropDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ContainerDropDescription492", type=tool_ContainerViewVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialOperation494: BinaryAssociation = BinaryAssociation(
    name="initialOperation494",
    ends={
        Property(name="tool_InitialContainerDropOperation", type=diagram_tool_ContainerDropDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_tool_ContainerDropDescription495", type=tool_InitialContainerDropOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedConcernDescriptions501: BinaryAssociation = BinaryAssociation(
    name="ownedConcernDescriptions501",
    ends={
        Property(name="concern_ConcernDescription502", type=diagram_concern_ConcernSet, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_concern_ConcernSet", type=concern_ConcernDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
filters503: BinaryAssociation = BinaryAssociation(
    name="filters503",
    ends={
        Property(name="filter_FilterDescription504", type=diagram_concern_ConcernDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_concern_ConcernDescription", type=filter_FilterDescription, multiplicity=Multiplicity(0, 9999))
    }
)
rules505: BinaryAssociation = BinaryAssociation(
    name="rules505",
    ends={
        Property(name="validation_ValidationRule507", type=diagram_concern_ConcernDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_concern_ConcernDescription506", type=validation_ValidationRule, multiplicity=Multiplicity(0, 9999))
    }
)
behaviors508: BinaryAssociation = BinaryAssociation(
    name="behaviors508",
    ends={
        Property(name="tool_BehaviorTool510", type=diagram_concern_ConcernDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_concern_ConcernDescription509", type=tool_BehaviorTool, multiplicity=Multiplicity(0, 9999))
    }
)
filters498: BinaryAssociation = BinaryAssociation(
    name="filters498",
    ends={
        Property(name="filter_Filter", type=diagram_filter_CompositeFilterDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_filter_CompositeFilterDescription", type=filter_Filter, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ownedVariables499: BinaryAssociation = BinaryAssociation(
    name="ownedVariables499",
    ends={
        Property(name="filter_FilterVariable500", type=diagram_filter_VariableFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram_filter_VariableFilter", type=filter_FilterVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_diagram_DDiagram_DRepresentation = Generalization(general=DRepresentation, specific=diagram_DDiagram)
gen_diagram_DDiagram_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=diagram_DDiagram)
gen_diagram_DDiagram_DragAndDropTarget = Generalization(general=DragAndDropTarget, specific=diagram_DDiagram)
gen_diagram_DDiagram_DValidable = Generalization(general=DValidable, specific=diagram_DDiagram)
gen_diagram_DDiagram_DContainer = Generalization(general=DContainer, specific=diagram_DDiagram)
gen_diagram_HideFilter_GraphicalFilter = Generalization(general=GraphicalFilter, specific=diagram_HideFilter)
gen_diagram_HideLabelFilter_GraphicalFilter = Generalization(general=GraphicalFilter, specific=diagram_HideLabelFilter)
gen_diagram_FoldingPointFilter_GraphicalFilter = Generalization(general=GraphicalFilter, specific=diagram_FoldingPointFilter)
gen_diagram_FoldingFilter_GraphicalFilter = Generalization(general=GraphicalFilter, specific=diagram_FoldingFilter)
gen_diagram_AppliedCompositeFilters_GraphicalFilter = Generalization(general=GraphicalFilter, specific=diagram_AppliedCompositeFilters)
gen_diagram_DSemanticDiagram_DDiagram = Generalization(general=DDiagram, specific=diagram_DSemanticDiagram)
gen_diagram_DSemanticDiagram_DSemanticDecorator = Generalization(general=DSemanticDecorator, specific=diagram_DSemanticDiagram)
gen_diagram_DDiagramElement_DRepresentationElement = Generalization(general=DRepresentationElement, specific=diagram_DDiagramElement)
gen_diagram_DDiagramElement_DValidable = Generalization(general=DValidable, specific=diagram_DDiagramElement)
gen_diagram_DDiagramElement_DNavigable = Generalization(general=DNavigable, specific=diagram_DDiagramElement)
gen_diagram_DNode_AbstractDNode = Generalization(general=AbstractDNode, specific=diagram_DNode)
gen_diagram_DNode_EdgeTarget = Generalization(general=EdgeTarget, specific=diagram_DNode)
gen_diagram_DNode_DragAndDropTarget = Generalization(general=DragAndDropTarget, specific=diagram_DNode)
gen_diagram_DDiagramElementContainer_AbstractDNode = Generalization(general=AbstractDNode, specific=diagram_DDiagramElementContainer)
gen_diagram_DDiagramElementContainer_EdgeTarget = Generalization(general=EdgeTarget, specific=diagram_DDiagramElementContainer)
gen_diagram_DDiagramElementContainer_DragAndDropTarget = Generalization(general=DragAndDropTarget, specific=diagram_DDiagramElementContainer)
gen_diagram_DDiagramElementContainer_DContainer = Generalization(general=DContainer, specific=diagram_DDiagramElementContainer)
gen_diagram_AbsoluteBoundsFilter_GraphicalFilter = Generalization(general=GraphicalFilter, specific=diagram_AbsoluteBoundsFilter)
gen_diagram_AbstractDNode_DDiagramElement = Generalization(general=DDiagramElement, specific=diagram_AbstractDNode)
gen_diagram_DNodeContainer_DDiagramElementContainer = Generalization(general=DDiagramElementContainer, specific=diagram_DNodeContainer)
gen_diagram_DEdge_DDiagramElement = Generalization(general=DDiagramElement, specific=diagram_DEdge)
gen_diagram_DEdge_EdgeTarget = Generalization(general=EdgeTarget, specific=diagram_DEdge)
gen_diagram_DNodeList_DDiagramElementContainer = Generalization(general=DDiagramElementContainer, specific=diagram_DNodeList)
gen_diagram_DNodeListElement_AbstractDNode = Generalization(general=AbstractDNode, specific=diagram_DNodeListElement)
gen_diagram_NodeStyle_LabelStyle = Generalization(general=LabelStyle, specific=diagram_NodeStyle)
gen_diagram_NodeStyle_Style = Generalization(general=Style, specific=diagram_NodeStyle)
gen_diagram_NodeStyle_BorderedStyle = Generalization(general=BorderedStyle, specific=diagram_NodeStyle)
gen_diagram_Dot_NodeStyle = Generalization(general=NodeStyle, specific=diagram_Dot)
gen_diagram_ContainerStyle_LabelStyle = Generalization(general=LabelStyle, specific=diagram_ContainerStyle)
gen_diagram_ContainerStyle_Style = Generalization(general=Style, specific=diagram_ContainerStyle)
gen_diagram_ContainerStyle_BorderedStyle = Generalization(general=BorderedStyle, specific=diagram_ContainerStyle)
gen_diagram_FlatContainerStyle_ContainerStyle = Generalization(general=ContainerStyle, specific=diagram_FlatContainerStyle)
gen_diagram_ShapeContainerStyle_ContainerStyle = Generalization(general=ContainerStyle, specific=diagram_ShapeContainerStyle)
gen_diagram_GaugeSection_Customizable = Generalization(general=Customizable, specific=diagram_GaugeSection)
gen_diagram_Lozenge_NodeStyle = Generalization(general=NodeStyle, specific=diagram_Lozenge)
gen_diagram_BundledImage_NodeStyle = Generalization(general=NodeStyle, specific=diagram_BundledImage)
gen_diagram_WorkspaceImage_NodeStyle = Generalization(general=NodeStyle, specific=diagram_WorkspaceImage)
gen_diagram_WorkspaceImage_ContainerStyle = Generalization(general=ContainerStyle, specific=diagram_WorkspaceImage)
gen_diagram_CustomStyle_NodeStyle = Generalization(general=NodeStyle, specific=diagram_CustomStyle)
gen_diagram_Square_NodeStyle = Generalization(general=NodeStyle, specific=diagram_Square)
gen_diagram_Ellipse_NodeStyle = Generalization(general=NodeStyle, specific=diagram_Ellipse)
gen_diagram_EdgeStyle_Style = Generalization(general=Style, specific=diagram_EdgeStyle)
gen_diagram_GaugeCompositeStyle_NodeStyle = Generalization(general=NodeStyle, specific=diagram_GaugeCompositeStyle)
gen_diagram_CollapseFilter_GraphicalFilter = Generalization(general=GraphicalFilter, specific=diagram_CollapseFilter)
gen_diagram_IndirectlyCollapseFilter_CollapseFilter = Generalization(general=CollapseFilter, specific=diagram_IndirectlyCollapseFilter)
gen_diagram_BeginLabelStyle_BasicLabelStyle = Generalization(general=BasicLabelStyle, specific=diagram_BeginLabelStyle)
gen_diagram_CenterLabelStyle_BasicLabelStyle = Generalization(general=BasicLabelStyle, specific=diagram_CenterLabelStyle)
gen_diagram_EndLabelStyle_BasicLabelStyle = Generalization(general=BasicLabelStyle, specific=diagram_EndLabelStyle)
gen_diagram_BorderedStyle_Style = Generalization(general=Style, specific=diagram_BorderedStyle)
gen_diagram_Note_NodeStyle = Generalization(general=NodeStyle, specific=diagram_Note)
gen_diagram_BracketEdgeStyle_EdgeStyle = Generalization(general=EdgeStyle, specific=diagram_BracketEdgeStyle)
gen_diagram_description_DiagramDescription_description_DragAndDropTargetDescription = Generalization(general=description_DragAndDropTargetDescription, specific=diagram_description_DiagramDescription)
gen_diagram_description_DiagramDescription_description_RepresentationDescription = Generalization(general=description_RepresentationDescription, specific=diagram_description_DiagramDescription)
gen_diagram_description_DiagramDescription_description_PasteTargetDescription = Generalization(general=description_PasteTargetDescription, specific=diagram_description_DiagramDescription)
gen_diagram_description_DiagramImportDescription_description_RepresentationImportDescription = Generalization(general=description_RepresentationImportDescription, specific=diagram_description_DiagramImportDescription)
gen_diagram_description_DiagramImportDescription_description_DiagramDescription = Generalization(general=description_DiagramDescription, specific=diagram_description_DiagramImportDescription)
gen_diagram_description_DiagramElementMapping_description_RepresentationElementMapping = Generalization(general=description_RepresentationElementMapping, specific=diagram_description_DiagramElementMapping)
gen_diagram_description_DiagramElementMapping_description_PasteTargetDescription = Generalization(general=description_PasteTargetDescription, specific=diagram_description_DiagramElementMapping)
gen_diagram_description_DiagramExtensionDescription_RepresentationExtensionDescription = Generalization(general=RepresentationExtensionDescription, specific=diagram_description_DiagramExtensionDescription)
gen_diagram_description_NodeMapping_description_AbstractNodeMapping = Generalization(general=description_AbstractNodeMapping, specific=diagram_description_NodeMapping)
gen_diagram_description_NodeMapping_description_DragAndDropTargetDescription = Generalization(general=description_DragAndDropTargetDescription, specific=diagram_description_NodeMapping)
gen_diagram_description_AbstractNodeMapping_description_DiagramElementMapping = Generalization(general=description_DiagramElementMapping, specific=diagram_description_AbstractNodeMapping)
gen_diagram_description_AbstractNodeMapping_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=diagram_description_AbstractNodeMapping)
gen_diagram_description_ContainerMapping_description_AbstractNodeMapping = Generalization(general=description_AbstractNodeMapping, specific=diagram_description_ContainerMapping)
gen_diagram_description_ContainerMapping_description_DragAndDropTargetDescription = Generalization(general=description_DragAndDropTargetDescription, specific=diagram_description_ContainerMapping)
gen_diagram_description_ContainerMappingImport_description_ContainerMapping = Generalization(general=description_ContainerMapping, specific=diagram_description_ContainerMappingImport)
gen_diagram_description_ContainerMappingImport_description_AbstractMappingImport = Generalization(general=description_AbstractMappingImport, specific=diagram_description_ContainerMappingImport)
gen_diagram_description_EdgeMapping_description_DiagramElementMapping = Generalization(general=description_DiagramElementMapping, specific=diagram_description_EdgeMapping)
gen_diagram_description_EdgeMapping_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=diagram_description_EdgeMapping)
gen_diagram_description_EdgeMapping_description_IEdgeMapping = Generalization(general=description_IEdgeMapping, specific=diagram_description_EdgeMapping)
gen_diagram_description_NodeMappingImport_description_NodeMapping = Generalization(general=description_NodeMapping, specific=diagram_description_NodeMappingImport)
gen_diagram_description_NodeMappingImport_description_AbstractMappingImport = Generalization(general=description_AbstractMappingImport, specific=diagram_description_NodeMappingImport)
gen_diagram_description_ConditionalNodeStyleDescription_ConditionalStyleDescription = Generalization(general=ConditionalStyleDescription, specific=diagram_description_ConditionalNodeStyleDescription)
gen_diagram_description_ConditionalEdgeStyleDescription_ConditionalStyleDescription = Generalization(general=ConditionalStyleDescription, specific=diagram_description_ConditionalEdgeStyleDescription)
gen_diagram_description_ConditionalContainerStyleDescription_ConditionalStyleDescription = Generalization(general=ConditionalStyleDescription, specific=diagram_description_ConditionalContainerStyleDescription)
gen_diagram_description_Layout_DocumentedElement = Generalization(general=DocumentedElement, specific=diagram_description_Layout)
gen_diagram_description_OrderedTreeLayout_Layout = Generalization(general=Layout, specific=diagram_description_OrderedTreeLayout)
gen_diagram_description_CompositeLayout_Layout = Generalization(general=Layout, specific=diagram_description_CompositeLayout)
gen_diagram_description_EdgeMappingImport_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=diagram_description_EdgeMappingImport)
gen_diagram_description_EdgeMappingImport_description_IEdgeMapping = Generalization(general=description_IEdgeMapping, specific=diagram_description_EdgeMappingImport)
gen_diagram_description_EdgeMappingImport_description_IdentifiedElement = Generalization(general=description_IdentifiedElement, specific=diagram_description_EdgeMappingImport)
gen_diagram_description_MappingBasedDecoration_DecorationDescription = Generalization(general=DecorationDescription, specific=diagram_description_MappingBasedDecoration)
gen_diagram_description_Layer_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=diagram_description_Layer)
gen_diagram_description_Layer_description_EndUserDocumentedElement = Generalization(general=description_EndUserDocumentedElement, specific=diagram_description_Layer)
gen_diagram_description_Layer_description_IdentifiedElement = Generalization(general=description_IdentifiedElement, specific=diagram_description_Layer)
gen_diagram_style_BorderedStyleDescription_StyleDescription = Generalization(general=StyleDescription, specific=diagram_style_BorderedStyleDescription)
gen_diagram_style_NodeStyleDescription_style_StyleDescription = Generalization(general=style_StyleDescription, specific=diagram_style_NodeStyleDescription)
gen_diagram_style_NodeStyleDescription_style_BorderedStyleDescription = Generalization(general=style_BorderedStyleDescription, specific=diagram_style_NodeStyleDescription)
gen_diagram_style_NodeStyleDescription_style_LabelStyleDescription = Generalization(general=style_LabelStyleDescription, specific=diagram_style_NodeStyleDescription)
gen_diagram_style_NodeStyleDescription_style_TooltipStyleDescription = Generalization(general=style_TooltipStyleDescription, specific=diagram_style_NodeStyleDescription)
gen_diagram_style_CustomStyleDescription_NodeStyleDescription = Generalization(general=NodeStyleDescription, specific=diagram_style_CustomStyleDescription)
gen_diagram_style_SquareDescription_NodeStyleDescription = Generalization(general=NodeStyleDescription, specific=diagram_style_SquareDescription)
gen_diagram_description_AdditionalLayer_Layer = Generalization(general=Layer, specific=diagram_description_AdditionalLayer)
gen_diagram_style_EllipseNodeDescription_NodeStyleDescription = Generalization(general=NodeStyleDescription, specific=diagram_style_EllipseNodeDescription)
gen_diagram_style_BundledImageDescription_NodeStyleDescription = Generalization(general=NodeStyleDescription, specific=diagram_style_BundledImageDescription)
gen_diagram_style_NoteDescription_NodeStyleDescription = Generalization(general=NodeStyleDescription, specific=diagram_style_NoteDescription)
gen_diagram_style_DotDescription_NodeStyleDescription = Generalization(general=NodeStyleDescription, specific=diagram_style_DotDescription)
gen_diagram_style_LozengeNodeDescription_NodeStyleDescription = Generalization(general=NodeStyleDescription, specific=diagram_style_LozengeNodeDescription)
gen_diagram_style_GaugeCompositeStyleDescription_NodeStyleDescription = Generalization(general=NodeStyleDescription, specific=diagram_style_GaugeCompositeStyleDescription)
gen_diagram_style_ContainerStyleDescription_style_LabelStyleDescription = Generalization(general=style_LabelStyleDescription, specific=diagram_style_ContainerStyleDescription)
gen_diagram_style_ContainerStyleDescription_style_TooltipStyleDescription = Generalization(general=style_TooltipStyleDescription, specific=diagram_style_ContainerStyleDescription)
gen_diagram_style_FlatContainerStyleDescription_style_ContainerStyleDescription = Generalization(general=style_ContainerStyleDescription, specific=diagram_style_FlatContainerStyleDescription)
gen_diagram_style_FlatContainerStyleDescription_style_SizeComputationContainerStyleDescription = Generalization(general=style_SizeComputationContainerStyleDescription, specific=diagram_style_FlatContainerStyleDescription)
gen_diagram_style_RoundedCornerStyleDescription_StyleDescription = Generalization(general=StyleDescription, specific=diagram_style_RoundedCornerStyleDescription)
gen_diagram_style_ContainerStyleDescription_style_RoundedCornerStyleDescription = Generalization(general=style_RoundedCornerStyleDescription, specific=diagram_style_ContainerStyleDescription)
gen_diagram_style_ContainerStyleDescription_style_BorderedStyleDescription = Generalization(general=style_BorderedStyleDescription, specific=diagram_style_ContainerStyleDescription)
gen_diagram_style_WorkspaceImageDescription_style_NodeStyleDescription = Generalization(general=style_NodeStyleDescription, specific=diagram_style_WorkspaceImageDescription)
gen_diagram_style_WorkspaceImageDescription_style_ContainerStyleDescription = Generalization(general=style_ContainerStyleDescription, specific=diagram_style_WorkspaceImageDescription)
gen_diagram_style_EdgeStyleDescription_StyleDescription = Generalization(general=StyleDescription, specific=diagram_style_EdgeStyleDescription)
gen_diagram_style_ShapeContainerStyleDescription_style_ContainerStyleDescription = Generalization(general=style_ContainerStyleDescription, specific=diagram_style_ShapeContainerStyleDescription)
gen_diagram_style_ShapeContainerStyleDescription_style_SizeComputationContainerStyleDescription = Generalization(general=style_SizeComputationContainerStyleDescription, specific=diagram_style_ShapeContainerStyleDescription)
gen_diagram_style_CenterLabelStyleDescription_BasicLabelStyleDescription = Generalization(general=BasicLabelStyleDescription, specific=diagram_style_CenterLabelStyleDescription)
gen_diagram_style_EndLabelStyleDescription_BasicLabelStyleDescription = Generalization(general=BasicLabelStyleDescription, specific=diagram_style_EndLabelStyleDescription)
gen_diagram_style_BracketEdgeStyleDescription_EdgeStyleDescription = Generalization(general=EdgeStyleDescription, specific=diagram_style_BracketEdgeStyleDescription)
gen_diagram_tool_ToolSection_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=diagram_tool_ToolSection)
gen_diagram_tool_ToolSection_description_IdentifiedElement = Generalization(general=description_IdentifiedElement, specific=diagram_tool_ToolSection)
gen_diagram_style_BeginLabelStyleDescription_BasicLabelStyleDescription = Generalization(general=BasicLabelStyleDescription, specific=diagram_style_BeginLabelStyleDescription)
gen_diagram_tool_EdgeCreationDescription_MappingBasedToolDescription = Generalization(general=MappingBasedToolDescription, specific=diagram_tool_EdgeCreationDescription)
gen_diagram_tool_ToolGroup_ToolEntry = Generalization(general=ToolEntry, specific=diagram_tool_ToolGroup)
gen_diagram_tool_NodeCreationDescription_MappingBasedToolDescription = Generalization(general=MappingBasedToolDescription, specific=diagram_tool_NodeCreationDescription)
gen_diagram_tool_ContainerCreationDescription_MappingBasedToolDescription = Generalization(general=MappingBasedToolDescription, specific=diagram_tool_ContainerCreationDescription)
gen_diagram_tool_DeleteElementDescription_MappingBasedToolDescription = Generalization(general=MappingBasedToolDescription, specific=diagram_tool_DeleteElementDescription)
gen_diagram_tool_DoubleClickDescription_MappingBasedToolDescription = Generalization(general=MappingBasedToolDescription, specific=diagram_tool_DoubleClickDescription)
gen_diagram_tool_ReconnectEdgeDescription_MappingBasedToolDescription = Generalization(general=MappingBasedToolDescription, specific=diagram_tool_ReconnectEdgeDescription)
gen_diagram_tool_BehaviorTool_AbstractToolDescription = Generalization(general=AbstractToolDescription, specific=diagram_tool_BehaviorTool)
gen_diagram_tool_RequestDescription_AbstractToolDescription = Generalization(general=AbstractToolDescription, specific=diagram_tool_RequestDescription)
gen_diagram_tool_DirectEditLabel_MappingBasedToolDescription = Generalization(general=MappingBasedToolDescription, specific=diagram_tool_DirectEditLabel)
gen_diagram_tool_SourceEdgeCreationVariable_tool_AbstractVariable = Generalization(general=tool_AbstractVariable, specific=diagram_tool_SourceEdgeCreationVariable)
gen_diagram_tool_SourceEdgeCreationVariable_tool_VariableContainer = Generalization(general=tool_VariableContainer, specific=diagram_tool_SourceEdgeCreationVariable)
gen_diagram_tool_SourceEdgeViewCreationVariable_tool_AbstractVariable = Generalization(general=tool_AbstractVariable, specific=diagram_tool_SourceEdgeViewCreationVariable)
gen_diagram_tool_SourceEdgeViewCreationVariable_tool_VariableContainer = Generalization(general=tool_VariableContainer, specific=diagram_tool_SourceEdgeViewCreationVariable)
gen_diagram_tool_TargetEdgeCreationVariable_tool_AbstractVariable = Generalization(general=tool_AbstractVariable, specific=diagram_tool_TargetEdgeCreationVariable)
gen_diagram_tool_TargetEdgeCreationVariable_tool_VariableContainer = Generalization(general=tool_VariableContainer, specific=diagram_tool_TargetEdgeCreationVariable)
gen_diagram_tool_TargetEdgeViewCreationVariable_tool_AbstractVariable = Generalization(general=tool_AbstractVariable, specific=diagram_tool_TargetEdgeViewCreationVariable)
gen_diagram_tool_TargetEdgeViewCreationVariable_tool_VariableContainer = Generalization(general=tool_VariableContainer, specific=diagram_tool_TargetEdgeViewCreationVariable)
gen_diagram_tool_ElementDoubleClickVariable_tool_AbstractVariable = Generalization(general=tool_AbstractVariable, specific=diagram_tool_ElementDoubleClickVariable)
gen_diagram_tool_ElementDoubleClickVariable_tool_VariableContainer = Generalization(general=tool_VariableContainer, specific=diagram_tool_ElementDoubleClickVariable)
gen_diagram_tool_NodeCreationVariable_tool_AbstractVariable = Generalization(general=tool_AbstractVariable, specific=diagram_tool_NodeCreationVariable)
gen_diagram_tool_NodeCreationVariable_tool_VariableContainer = Generalization(general=tool_VariableContainer, specific=diagram_tool_NodeCreationVariable)
gen_diagram_tool_CreateView_ContainerModelOperation = Generalization(general=ContainerModelOperation, specific=diagram_tool_CreateView)
gen_diagram_tool_CreateEdgeView_CreateView = Generalization(general=CreateView, specific=diagram_tool_CreateEdgeView)
gen_diagram_tool_DiagramCreationDescription_RepresentationCreationDescription = Generalization(general=RepresentationCreationDescription, specific=diagram_tool_DiagramCreationDescription)
gen_diagram_tool_DiagramNavigationDescription_RepresentationNavigationDescription = Generalization(general=RepresentationNavigationDescription, specific=diagram_tool_DiagramNavigationDescription)
gen_diagram_tool_ContainerDropDescription_MappingBasedToolDescription = Generalization(general=MappingBasedToolDescription, specific=diagram_tool_ContainerDropDescription)
gen_diagram_tool_Navigation_ContainerModelOperation = Generalization(general=ContainerModelOperation, specific=diagram_tool_Navigation)
gen_diagram_filter_FilterDescription_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=diagram_filter_FilterDescription)
gen_diagram_filter_FilterDescription_description_IdentifiedElement = Generalization(general=description_IdentifiedElement, specific=diagram_filter_FilterDescription)
gen_diagram_filter_MappingFilter_Filter = Generalization(general=Filter, specific=diagram_filter_MappingFilter)
gen_diagram_filter_CompositeFilterDescription_FilterDescription = Generalization(general=FilterDescription, specific=diagram_filter_CompositeFilterDescription)
gen_diagram_filter_FilterVariable_SelectionDescription = Generalization(general=SelectionDescription, specific=diagram_filter_FilterVariable)
gen_diagram_concern_ConcernSet_DocumentedElement = Generalization(general=DocumentedElement, specific=diagram_concern_ConcernSet)
gen_diagram_concern_ConcernDescription_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=diagram_concern_ConcernDescription)
gen_diagram_concern_ConcernDescription_description_IdentifiedElement = Generalization(general=description_IdentifiedElement, specific=diagram_concern_ConcernDescription)
gen_diagram_filter_VariableFilter_Filter = Generalization(general=Filter, specific=diagram_filter_VariableFilter)

# Domain Model
domain_model = DomainModel(
    name="diagram",
    types={diagram_DDiagramElement, diagram_DDiagram, DRepresentation, description_DocumentedElement, DragAndDropTarget, DValidable, DContainer, diagram_DNode, diagram_DNodeListElement, diagram_DDiagramElementContainer, concern_ConcernDescription, filter_FilterDescription, DiagramDescription, diagram_DEdge, validation_ValidationRule, tool_BehaviorTool, diagram_FilterVariableHistory, Layer, diagram_Decoration, DiagramElementMapping, diagram_GraphicalFilter, diagram_HideFilter, GraphicalFilter, diagram_HideLabelFilter, diagram_FoldingPointFilter, diagram_FoldingFilter, diagram_AppliedCompositeFilters, diagram_DSemanticDiagram, DDiagram, DSemanticDecorator, DRepresentationElement, DNavigable, AbstractDNode, EdgeTarget, diagram_NodeStyle, diagram_Style, NodeMapping, filter_CompositeFilterDescription, diagram_AbsoluteBoundsFilter, diagram_AbstractDNode, DDiagramElement, diagram_ContainerStyle, ContainerMapping, diagram_DNodeContainer, DDiagramElementContainer, diagram_EdgeStyle, diagram_EdgeTarget, IEdgeMapping, diagram_DNodeList, LabelStyle, Style, BorderedStyle, diagram_Dot, NodeStyle, diagram_RGBValues, diagram_FlatContainerStyle, ContainerStyle, diagram_ShapeContainerStyle, diagram_GaugeSection, Customizable, diagram_Lozenge, diagram_BundledImage, diagram_WorkspaceImage, diagram_CustomStyle, diagram_Square, diagram_Ellipse, diagram_BeginLabelStyle, diagram_CenterLabelStyle, diagram_EndLabelStyle, diagram_GaugeCompositeStyle, filter_FilterVariable, diagram_EObject, diagram_CollapseFilter, diagram_IndirectlyCollapseFilter, CollapseFilter, BasicLabelStyle, diagram_BorderedStyle, diagram_Note, diagram_FilterVariableValue, diagram_ComputedStyleDescriptionRegistry, style_StyleDescription, diagram_DiagramElementMapping2ModelElement, diagram_ModelElement2ViewVariable, diagram_ViewVariable2ContainerVariable, diagram_ContainerVariable2StyleDescription, diagram_BracketEdgeStyle, EdgeStyle, EdgeMapping, validation_ValidationSet, concern_ConcernSet, diagram_DragAndDropTarget, diagram_description_DiagramDescription, description_DragAndDropTargetDescription, description_RepresentationDescription, description_PasteTargetDescription, tool_RepresentationCreationDescription, Layout, tool_InitialOperation, AdditionalLayer, tool_AbstractToolDescription, EdgeMappingImport, tool_ToolSection, diagram_description_DiagramImportDescription, description_RepresentationImportDescription, description_DiagramDescription, diagram_description_DiagramElementMapping, description_RepresentationElementMapping, diagram_description_DiagramExtensionDescription, RepresentationExtensionDescription, tool_DirectEditLabel, tool_DeleteElementDescription, diagram_description_NodeMapping, description_AbstractNodeMapping, tool_DoubleClickDescription, diagram_description_AbstractNodeMapping, description_DiagramElementMapping, style_NodeStyleDescription, ConditionalNodeStyleDescription, diagram_description_ContainerMapping, diagram_description_ContainerMappingImport, description_ContainerMapping, diagram_description_EdgeMapping, description_IEdgeMapping, style_ContainerStyleDescription, ConditionalContainerStyleDescription, diagram_description_NodeMappingImport, description_NodeMapping, description_AbstractMappingImport, style_EdgeStyleDescription, ConditionalEdgeStyleDescription, tool_ReconnectEdgeDescription, AbstractNodeMapping, diagram_description_ConditionalNodeStyleDescription, ConditionalStyleDescription, diagram_description_ConditionalEdgeStyleDescription, diagram_description_ConditionalContainerStyleDescription, diagram_description_Layout, DocumentedElement, diagram_description_OrderedTreeLayout, diagram_description_CompositeLayout, diagram_description_IEdgeMapping, diagram_description_EdgeMappingImport, description_IdentifiedElement, DecorationDescriptionsSet, diagram_description_MappingBasedDecoration, DecorationDescription, diagram_description_Layer, description_EndUserDocumentedElement, diagram_style_BorderedStyleDescription, StyleDescription, ColorDescription, diagram_style_NodeStyleDescription, style_BorderedStyleDescription, style_LabelStyleDescription, style_TooltipStyleDescription, diagram_style_CustomStyleDescription, NodeStyleDescription, diagram_style_SquareDescription, Customization, diagram_description_AdditionalLayer, diagram_description_DragAndDropTargetDescription, tool_ContainerDropDescription, diagram_style_EllipseNodeDescription, diagram_style_BundledImageDescription, diagram_style_NoteDescription, diagram_style_DotDescription, diagram_style_LozengeNodeDescription, style_GaugeSectionDescription, diagram_style_GaugeSectionDescription, diagram_style_SizeComputationContainerStyleDescription, diagram_style_GaugeCompositeStyleDescription, diagram_style_FlatContainerStyleDescription, style_SizeComputationContainerStyleDescription, diagram_style_RoundedCornerStyleDescription, diagram_style_ContainerStyleDescription, style_RoundedCornerStyleDescription, diagram_style_WorkspaceImageDescription, diagram_style_EdgeStyleDescription, style_LabelBorderStyleDescription, diagram_style_ShapeContainerStyleDescription, diagram_style_CenterLabelStyleDescription, diagram_style_EndLabelStyleDescription, diagram_style_BracketEdgeStyleDescription, EdgeStyleDescription, diagram_tool_ToolSection, tool_ToolEntry, tool_PopupMenu, tool_ToolGroupExtension, style_BeginLabelStyleDescription, style_CenterLabelStyleDescription, style_EndLabelStyleDescription, diagram_style_BeginLabelStyleDescription, BasicLabelStyleDescription, tool_NodeCreationVariable, tool_ContainerViewVariable, tool_InitialNodeCreationOperation, diagram_tool_EdgeCreationDescription, diagram_tool_ToolGroup, ToolEntry, diagram_tool_ToolGroupExtension, tool_ToolGroup, diagram_tool_NodeCreationDescription, MappingBasedToolDescription, tool_SourceEdgeViewCreationVariable, tool_TargetEdgeViewCreationVariable, tool_InitEdgeCreationOperation, diagram_tool_ContainerCreationDescription, tool_SourceEdgeCreationVariable, tool_TargetEdgeCreationVariable, diagram_tool_DeleteElementDescription, tool_ElementDeleteVariable, tool_DeleteHook, diagram_tool_DoubleClickDescription, diagram_tool_ReconnectEdgeDescription, tool_ElementSelectVariable, tool_ElementDoubleClickVariable, diagram_tool_DeleteHook, tool_DeleteHookParameter, diagram_tool_DeleteHookParameter, tool_EditMaskVariables, diagram_tool_BehaviorTool, diagram_tool_RequestDescription, AbstractToolDescription, diagram_tool_DirectEditLabel, diagram_tool_SourceEdgeCreationVariable, tool_AbstractVariable, tool_VariableContainer, diagram_tool_SourceEdgeViewCreationVariable, diagram_tool_TargetEdgeCreationVariable, diagram_tool_TargetEdgeViewCreationVariable, diagram_tool_ElementDoubleClickVariable, diagram_tool_NodeCreationVariable, diagram_tool_CreateView, ContainerModelOperation, diagram_tool_CreateEdgeView, CreateView, diagram_tool_DiagramCreationDescription, RepresentationCreationDescription, diagram_tool_DiagramNavigationDescription, RepresentationNavigationDescription, diagram_tool_ContainerDropDescription, tool_DropContainerVariable, diagram_tool_Navigation, diagram_filter_FilterDescription, diagram_filter_Filter, diagram_filter_MappingFilter, Filter, diagram_filter_CompositeFilterDescription, FilterDescription, tool_ElementDropVariable, tool_InitialContainerDropOperation, diagram_filter_FilterVariable, SelectionDescription, diagram_concern_ConcernSet, diagram_concern_ConcernDescription, filter_Filter, diagram_filter_VariableFilter, ContainerLayout, LabelPosition, ContainerShape, BackgroundStyle, BundledImageShape, LineStyle, EdgeRouting, AlignmentKind, EdgeArrows, ResizeKind, ArrangeConstraint, FoldingStyle, LayoutDirection, ReconnectionKind, FilterKind},
    associations={ownedDiagramElements0, diagramElements1, nodes8, nodeListElements10, containers12, currentConcern14, description4, edges6, activatedRules21, activateBehaviors23, filterVariableHistory25, activatedLayers27, hiddenElements29, activatedFilters16, allFilters18, parentLayers32, decorations35, diagramElementMapping37, graphicalFilters39, ownedStyle44, originalStyle46, actualMapping48, candidatesMapping50, compositeFilterDescriptions41, ownedBorderedNodes42, elements59, ownedStyle62, originalStyle64, actualMapping67, candidatesMapping69, ownedDiagramElements72, nodes53, containers57, originalStyle79, actualMapping82, candidatesMapping85, ownedStyle88, sourceNode90, targetNode91, ownedElements74, ownedStyle76, backgroundColor100, actualMapping93, originalStyle95, path98, foregroundColor103, backgroundColor106, foregroundColor108, backgroundColor111, backgroundColor101, color115, color117, color119, color113, strokeColor124, beginLabelStyle127, centerLabelStyle129, endLabelStyle131, outgoingEdges121, incomingEdges122, sections133, variableDefinition141, modelElement143, borderColor135, color137, ownedValues139, computedStyleDescriptions145, cache146, key148, value151, key153, value156, key158, value161, filters169, allEdgeMappings171, allNodeMappings173, allContainerMappings176, validationSet179, concerns181, key163, value166, defaultConcern185, init188, layout190, diagramInitialisation192, defaultLayer194, additionalLayers197, allLayers199, allTools183, edgeMappingImports211, containerMappings213, reusedMappings216, toolSection219, reusedTools221, allActivatedTools202, nodeMappings205, edgeMappings208, importedDiagram224, layers226, validationSet228, concerns231, labelDirectEdit235, deletionDescription234, borderedNodeMappings238, reusedBorderedNodeMappings240, doubleClickDescription237, style243, conditionnalStyles244, subNodeMappings246, allNodeMappings248, reusedNodeMappings251, subContainerMappings254, reusedContainerMappings257, importedMapping269, allContainerMappings260, style263, conditionnalStyles265, importedMapping267, style276, conditionnalStyles278, reconnections280, pathNodeMapping282, sourceMapping271, targetMapping273, style289, style291, style293, nodeMapping295, importedMapping284, conditionnalStyles286, edgeMappings301, edgeMappingImports304, containerMappings307, reusedMappings310, allTools313, toolSections316, reusedTools319, decorationDescriptionsSet322, mappings297, nodeMappings299, borderColor330, allEdgeMappings324, customization327, dropDescriptions329, color333, color335, color337, color339, color331, sections343, backgroundColor344, foregroundColor346, backgroundColor341, backgroundColor349, backgroundColor356, strokeColor358, foregroundColor351, labelBorderStyle354, ownedTools366, subSections367, popupMenus370, reusedTools372, groupExtensions375, beginLabelStyleDescription360, centerLabelStyleDescription362, endLabelStyleDescription364, variable385, viewVariable387, initialOperation389, extraMappings391, tools377, group379, tools380, nodeMappings383, sourceViewVariable400, targetViewVariable402, initialOperation404, extraSourceMappings406, extraTargetMappings409, edgeMappings394, sourceVariable396, targetVariable398, extraMappings423, element426, elementView427, containerView430, initialOperation433, hook436, mappings438, containerMappings412, variable414, viewVariable417, initialOperation420, source449, target451, sourceView454, targetView457, element460, element441, elementView442, initialOperation445, parameters448, mask468, initialOperation469, initialOperation472, initialOperation462, edgeView465, mapping474, diagramDescription476, diagramDescription478, diagramDescription480, mappings482, oldContainer484, mappings496, newContainer486, element489, newViewContainer491, initialOperation494, ownedConcernDescriptions501, filters503, rules505, behaviors508, filters498, ownedVariables499},
    generalizations={gen_diagram_DDiagram_DRepresentation, gen_diagram_DDiagram_description_DocumentedElement, gen_diagram_DDiagram_DragAndDropTarget, gen_diagram_DDiagram_DValidable, gen_diagram_DDiagram_DContainer, gen_diagram_HideFilter_GraphicalFilter, gen_diagram_HideLabelFilter_GraphicalFilter, gen_diagram_FoldingPointFilter_GraphicalFilter, gen_diagram_FoldingFilter_GraphicalFilter, gen_diagram_AppliedCompositeFilters_GraphicalFilter, gen_diagram_DSemanticDiagram_DDiagram, gen_diagram_DSemanticDiagram_DSemanticDecorator, gen_diagram_DDiagramElement_DRepresentationElement, gen_diagram_DDiagramElement_DValidable, gen_diagram_DDiagramElement_DNavigable, gen_diagram_DNode_AbstractDNode, gen_diagram_DNode_EdgeTarget, gen_diagram_DNode_DragAndDropTarget, gen_diagram_DDiagramElementContainer_AbstractDNode, gen_diagram_DDiagramElementContainer_EdgeTarget, gen_diagram_DDiagramElementContainer_DragAndDropTarget, gen_diagram_DDiagramElementContainer_DContainer, gen_diagram_AbsoluteBoundsFilter_GraphicalFilter, gen_diagram_AbstractDNode_DDiagramElement, gen_diagram_DNodeContainer_DDiagramElementContainer, gen_diagram_DEdge_DDiagramElement, gen_diagram_DEdge_EdgeTarget, gen_diagram_DNodeList_DDiagramElementContainer, gen_diagram_DNodeListElement_AbstractDNode, gen_diagram_NodeStyle_LabelStyle, gen_diagram_NodeStyle_Style, gen_diagram_NodeStyle_BorderedStyle, gen_diagram_Dot_NodeStyle, gen_diagram_ContainerStyle_LabelStyle, gen_diagram_ContainerStyle_Style, gen_diagram_ContainerStyle_BorderedStyle, gen_diagram_FlatContainerStyle_ContainerStyle, gen_diagram_ShapeContainerStyle_ContainerStyle, gen_diagram_GaugeSection_Customizable, gen_diagram_Lozenge_NodeStyle, gen_diagram_BundledImage_NodeStyle, gen_diagram_WorkspaceImage_NodeStyle, gen_diagram_WorkspaceImage_ContainerStyle, gen_diagram_CustomStyle_NodeStyle, gen_diagram_Square_NodeStyle, gen_diagram_Ellipse_NodeStyle, gen_diagram_EdgeStyle_Style, gen_diagram_GaugeCompositeStyle_NodeStyle, gen_diagram_CollapseFilter_GraphicalFilter, gen_diagram_IndirectlyCollapseFilter_CollapseFilter, gen_diagram_BeginLabelStyle_BasicLabelStyle, gen_diagram_CenterLabelStyle_BasicLabelStyle, gen_diagram_EndLabelStyle_BasicLabelStyle, gen_diagram_BorderedStyle_Style, gen_diagram_Note_NodeStyle, gen_diagram_BracketEdgeStyle_EdgeStyle, gen_diagram_description_DiagramDescription_description_DragAndDropTargetDescription, gen_diagram_description_DiagramDescription_description_RepresentationDescription, gen_diagram_description_DiagramDescription_description_PasteTargetDescription, gen_diagram_description_DiagramImportDescription_description_RepresentationImportDescription, gen_diagram_description_DiagramImportDescription_description_DiagramDescription, gen_diagram_description_DiagramElementMapping_description_RepresentationElementMapping, gen_diagram_description_DiagramElementMapping_description_PasteTargetDescription, gen_diagram_description_DiagramExtensionDescription_RepresentationExtensionDescription, gen_diagram_description_NodeMapping_description_AbstractNodeMapping, gen_diagram_description_NodeMapping_description_DragAndDropTargetDescription, gen_diagram_description_AbstractNodeMapping_description_DiagramElementMapping, gen_diagram_description_AbstractNodeMapping_description_DocumentedElement, gen_diagram_description_ContainerMapping_description_AbstractNodeMapping, gen_diagram_description_ContainerMapping_description_DragAndDropTargetDescription, gen_diagram_description_ContainerMappingImport_description_ContainerMapping, gen_diagram_description_ContainerMappingImport_description_AbstractMappingImport, gen_diagram_description_EdgeMapping_description_DiagramElementMapping, gen_diagram_description_EdgeMapping_description_DocumentedElement, gen_diagram_description_EdgeMapping_description_IEdgeMapping, gen_diagram_description_NodeMappingImport_description_NodeMapping, gen_diagram_description_NodeMappingImport_description_AbstractMappingImport, gen_diagram_description_ConditionalNodeStyleDescription_ConditionalStyleDescription, gen_diagram_description_ConditionalEdgeStyleDescription_ConditionalStyleDescription, gen_diagram_description_ConditionalContainerStyleDescription_ConditionalStyleDescription, gen_diagram_description_Layout_DocumentedElement, gen_diagram_description_OrderedTreeLayout_Layout, gen_diagram_description_CompositeLayout_Layout, gen_diagram_description_EdgeMappingImport_description_DocumentedElement, gen_diagram_description_EdgeMappingImport_description_IEdgeMapping, gen_diagram_description_EdgeMappingImport_description_IdentifiedElement, gen_diagram_description_MappingBasedDecoration_DecorationDescription, gen_diagram_description_Layer_description_DocumentedElement, gen_diagram_description_Layer_description_EndUserDocumentedElement, gen_diagram_description_Layer_description_IdentifiedElement, gen_diagram_style_BorderedStyleDescription_StyleDescription, gen_diagram_style_NodeStyleDescription_style_StyleDescription, gen_diagram_style_NodeStyleDescription_style_BorderedStyleDescription, gen_diagram_style_NodeStyleDescription_style_LabelStyleDescription, gen_diagram_style_NodeStyleDescription_style_TooltipStyleDescription, gen_diagram_style_CustomStyleDescription_NodeStyleDescription, gen_diagram_style_SquareDescription_NodeStyleDescription, gen_diagram_description_AdditionalLayer_Layer, gen_diagram_style_EllipseNodeDescription_NodeStyleDescription, gen_diagram_style_BundledImageDescription_NodeStyleDescription, gen_diagram_style_NoteDescription_NodeStyleDescription, gen_diagram_style_DotDescription_NodeStyleDescription, gen_diagram_style_LozengeNodeDescription_NodeStyleDescription, gen_diagram_style_GaugeCompositeStyleDescription_NodeStyleDescription, gen_diagram_style_ContainerStyleDescription_style_LabelStyleDescription, gen_diagram_style_ContainerStyleDescription_style_TooltipStyleDescription, gen_diagram_style_FlatContainerStyleDescription_style_ContainerStyleDescription, gen_diagram_style_FlatContainerStyleDescription_style_SizeComputationContainerStyleDescription, gen_diagram_style_RoundedCornerStyleDescription_StyleDescription, gen_diagram_style_ContainerStyleDescription_style_RoundedCornerStyleDescription, gen_diagram_style_ContainerStyleDescription_style_BorderedStyleDescription, gen_diagram_style_WorkspaceImageDescription_style_NodeStyleDescription, gen_diagram_style_WorkspaceImageDescription_style_ContainerStyleDescription, gen_diagram_style_EdgeStyleDescription_StyleDescription, gen_diagram_style_ShapeContainerStyleDescription_style_ContainerStyleDescription, gen_diagram_style_ShapeContainerStyleDescription_style_SizeComputationContainerStyleDescription, gen_diagram_style_CenterLabelStyleDescription_BasicLabelStyleDescription, gen_diagram_style_EndLabelStyleDescription_BasicLabelStyleDescription, gen_diagram_style_BracketEdgeStyleDescription_EdgeStyleDescription, gen_diagram_tool_ToolSection_description_DocumentedElement, gen_diagram_tool_ToolSection_description_IdentifiedElement, gen_diagram_style_BeginLabelStyleDescription_BasicLabelStyleDescription, gen_diagram_tool_EdgeCreationDescription_MappingBasedToolDescription, gen_diagram_tool_ToolGroup_ToolEntry, gen_diagram_tool_NodeCreationDescription_MappingBasedToolDescription, gen_diagram_tool_ContainerCreationDescription_MappingBasedToolDescription, gen_diagram_tool_DeleteElementDescription_MappingBasedToolDescription, gen_diagram_tool_DoubleClickDescription_MappingBasedToolDescription, gen_diagram_tool_ReconnectEdgeDescription_MappingBasedToolDescription, gen_diagram_tool_BehaviorTool_AbstractToolDescription, gen_diagram_tool_RequestDescription_AbstractToolDescription, gen_diagram_tool_DirectEditLabel_MappingBasedToolDescription, gen_diagram_tool_SourceEdgeCreationVariable_tool_AbstractVariable, gen_diagram_tool_SourceEdgeCreationVariable_tool_VariableContainer, gen_diagram_tool_SourceEdgeViewCreationVariable_tool_AbstractVariable, gen_diagram_tool_SourceEdgeViewCreationVariable_tool_VariableContainer, gen_diagram_tool_TargetEdgeCreationVariable_tool_AbstractVariable, gen_diagram_tool_TargetEdgeCreationVariable_tool_VariableContainer, gen_diagram_tool_TargetEdgeViewCreationVariable_tool_AbstractVariable, gen_diagram_tool_TargetEdgeViewCreationVariable_tool_VariableContainer, gen_diagram_tool_ElementDoubleClickVariable_tool_AbstractVariable, gen_diagram_tool_ElementDoubleClickVariable_tool_VariableContainer, gen_diagram_tool_NodeCreationVariable_tool_AbstractVariable, gen_diagram_tool_NodeCreationVariable_tool_VariableContainer, gen_diagram_tool_CreateView_ContainerModelOperation, gen_diagram_tool_CreateEdgeView_CreateView, gen_diagram_tool_DiagramCreationDescription_RepresentationCreationDescription, gen_diagram_tool_DiagramNavigationDescription_RepresentationNavigationDescription, gen_diagram_tool_ContainerDropDescription_MappingBasedToolDescription, gen_diagram_tool_Navigation_ContainerModelOperation, gen_diagram_filter_FilterDescription_description_DocumentedElement, gen_diagram_filter_FilterDescription_description_IdentifiedElement, gen_diagram_filter_MappingFilter_Filter, gen_diagram_filter_CompositeFilterDescription_FilterDescription, gen_diagram_filter_FilterVariable_SelectionDescription, gen_diagram_concern_ConcernSet_DocumentedElement, gen_diagram_concern_ConcernDescription_description_DocumentedElement, gen_diagram_concern_ConcernDescription_description_IdentifiedElement, gen_diagram_filter_VariableFilter_Filter},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)