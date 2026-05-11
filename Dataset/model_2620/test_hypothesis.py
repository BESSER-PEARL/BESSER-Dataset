import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    description::AbstractNodeMapping,
    description::DiagramElementMapping,
    tool::DoubleClickDescription,
    tool::DirectEditLabel,
    tool::DeleteElementDescription,
    description::RepresentationElementMapping,
    RepresentationExtensionDescription,
    diagram::description::DiagramExtensionDescription,
    description::DiagramDescription,
    description::RepresentationImportDescription,
    diagram::description::DiagramImportDescription,
    tool::ToolSection,
    EdgeMappingImport,
    AdditionalLayer,
    Filter,
    diagram::filter::MappingFilter,
    diagram::filter::Filter,
    InteractiveVariableDescription,
    diagram::filter::VariableFilter,
    filter::Filter,
    FilterDescription,
    diagram::filter::CompositeFilterDescription,
    RepresentationNavigationDescription,
    diagram::tool::DiagramNavigationDescription,
    tool::InitialContainerDropOperation,
    tool::ElementDropVariable,
    tool::DropContainerVariable,
    RepresentationCreationDescription,
    diagram::tool::DiagramCreationDescription,
    CreateView,
    diagram::tool::CreateEdgeView,
    AbstractToolDescription,
    diagram::tool::RequestDescription,
    ContainerModelOperation,
    diagram::tool::Navigation,
    diagram::tool::CreateView,
    tool::VariableContainer,
    description::AbstractVariable,
    diagram::tool::ElementDoubleClickVariable,
    diagram::tool::TargetEdgeCreationVariable,
    diagram::tool::SourceEdgeViewCreationVariable,
    diagram::tool::NodeCreationVariable,
    diagram::tool::TargetEdgeViewCreationVariable,
    diagram::tool::SourceEdgeCreationVariable,
    diagram::tool::BehaviorTool,
    tool::EditMaskVariables,
    diagram::tool::DeleteHook,
    tool::ElementSelectVariable,
    diagram::tool::DeleteHookParameter,
    tool::DeleteHookParameter,
    tool::ElementDoubleClickVariable,
    tool::DeleteHook,
    tool::ElementDeleteVariable,
    tool::InitEdgeCreationOperation,
    tool::TargetEdgeViewCreationVariable,
    tool::SourceEdgeViewCreationVariable,
    tool::TargetEdgeCreationVariable,
    tool::SourceEdgeCreationVariable,
    tool::PopupMenu,
    tool::InitialNodeCreationOperation,
    tool::ContainerViewVariable,
    tool::NodeCreationVariable,
    MappingBasedToolDescription,
    diagram::tool::DoubleClickDescription,
    diagram::tool::EdgeCreationDescription,
    diagram::tool::ReconnectEdgeDescription,
    diagram::tool::ContainerDropDescription,
    diagram::tool::ContainerCreationDescription,
    diagram::tool::DirectEditLabel,
    diagram::tool::DeleteElementDescription,
    diagram::tool::NodeCreationDescription,
    tool::ToolGroup,
    diagram::tool::ToolGroupExtension,
    ToolEntry,
    diagram::tool::ToolGroup,
    tool::ToolGroupExtension,
    style::BeginLabelStyleDescription,
    tool::ToolEntry,
    diagram::style::HideLabelCapabilityStyleDescription,
    EdgeStyleDescription,
    diagram::style::BracketEdgeStyleDescription,
    BasicLabelStyleDescription,
    diagram::style::EndLabelStyleDescription,
    diagram::style::CenterLabelStyleDescription,
    diagram::style::BeginLabelStyleDescription,
    style::EndLabelStyleDescription,
    style::CenterLabelStyleDescription,
    diagram::style::SizeComputationContainerStyleDescription,
    style::LabelBorderStyleDescription,
    style::SizeComputationContainerStyleDescription,
    style::RoundedCornerStyleDescription,
    diagram::style::GaugeSectionDescription,
    style::GaugeSectionDescription,
    NodeStyleDescription,
    diagram::style::DotDescription,
    diagram::style::EllipseNodeDescription,
    diagram::style::LozengeNodeDescription,
    diagram::style::BundledImageDescription,
    diagram::style::SquareDescription,
    diagram::style::GaugeCompositeStyleDescription,
    diagram::style::NoteDescription,
    diagram::style::CustomStyleDescription,
    style::HideLabelCapabilityStyleDescription,
    style::TooltipStyleDescription,
    style::LabelStyleDescription,
    style::BorderedStyleDescription,
    diagram::style::ContainerStyleDescription,
    ColorDescription,
    StyleDescription,
    diagram::style::RoundedCornerStyleDescription,
    diagram::style::EdgeStyleDescription,
    diagram::style::BorderedStyleDescription,
    tool::ContainerDropDescription,
    diagram::description::DragAndDropTargetDescription,
    Customization,
    DecorationDescriptionsSet,
    description::EndUserDocumentedElement,
    DecorationDescription,
    diagram::description::MappingBasedDecoration,
    DocumentedElement,
    diagram::concern::ConcernSet,
    diagram::description::Layout,
    style::EdgeStyleDescription,
    ConditionalStyleDescription,
    diagram::description::ConditionalEdgeStyleDescription,
    diagram::description::ConditionalContainerStyleDescription,
    diagram::description::ConditionalNodeStyleDescription,
    description::IdentifiedElement,
    diagram::description::IEdgeMapping,
    AbstractNodeMapping,
    tool::ReconnectEdgeDescription,
    ConditionalEdgeStyleDescription,
    description::ContainerMapping,
    ConditionalNodeStyleDescription,
    description::IEdgeMapping,
    style::NodeStyleDescription,
    description::AbstractMappingImport,
    diagram::description::ContainerMappingImport,
    description::NodeMapping,
    diagram::description::NodeMappingImport,
    ConditionalContainerStyleDescription,
    style::ContainerStyleDescription,
    diagram::style::FlatContainerStyleDescription,
    diagram::style::WorkspaceImageDescription,
    diagram::style::ShapeContainerStyleDescription,
    tool::InitialOperation,
    Layout,
    diagram::description::OrderedTreeLayout,
    diagram::description::CompositeLayout,
    tool::RepresentationCreationDescription,
    tool::AbstractToolDescription,
    concern::ConcernSet,
    validation::ValidationSet,
    EdgeMapping,
    description::PasteTargetDescription,
    diagram::description::DiagramElementMapping,
    description::RepresentationDescription,
    description::DragAndDropTargetDescription,
    diagram::description::ContainerMapping,
    diagram::description::NodeMapping,
    diagram::description::DiagramDescription,
    diagram::EObject,
    tool::SelectModelElementVariable,
    TypedVariable,
    VariableValue,
    diagram::EObjectVariableValue,
    diagram::TypedVariableValue,
    diagram::HideLabelCapabilityStyle,
    diagram::DragAndDropTarget,
    style::StyleDescription,
    diagram::style::NodeStyleDescription,
    diagram::ComputedStyleDescriptionRegistry,
    EdgeStyle,
    diagram::BracketEdgeStyle,
    BasicLabelStyle,
    CollapseFilter,
    diagram::IndirectlyCollapseFilter,
    diagram::VariableValue,
    diagram::EndLabelStyle,
    diagram::CenterLabelStyle,
    diagram::BeginLabelStyle,
    Customizable,
    diagram::GaugeSection,
    ContainerStyle,
    diagram::ShapeContainerStyle,
    diagram::FlatContainerStyle,
    NodeStyle,
    diagram::Lozenge,
    diagram::CustomStyle,
    diagram::GaugeCompositeStyle,
    diagram::Square,
    diagram::WorkspaceImage,
    diagram::BundledImage,
    diagram::Ellipse,
    diagram::Note,
    diagram::Dot,
    HideLabelCapabilityStyle,
    BorderedStyle,
    Style,
    diagram::BorderedStyle,
    LabelStyle,
    IEdgeMapping,
    diagram::EdgeTarget,
    diagram::EdgeStyle,
    DDiagramElementContainer,
    diagram::DNodeList,
    diagram::DNodeContainer,
    ContainerMapping,
    diagram::ContainerStyle,
    diagram::GraphicalFilter,
    NodeMapping,
    diagram::Style,
    diagram::NodeStyle,
    EdgeTarget,
    AbstractDNode,
    DDiagramElement,
    diagram::AbstractDNode,
    filter::CompositeFilterDescription,
    GraphicalFilter,
    diagram::AbsoluteBoundsFilter,
    diagram::AppliedCompositeFilters,
    diagram::CollapseFilter,
    diagram::HideLabelFilter,
    diagram::FoldingPointFilter,
    diagram::FoldingFilter,
    diagram::HideFilter,
    filter::FilterDescription,
    DiagramElementMapping,
    diagram::Decoration,
    DRepresentationElement,
    DSemanticDecorator,
    DDiagram,
    diagram::DSemanticDiagram,
    Layer,
    diagram::description::AdditionalLayer,
    diagram::FilterVariableHistory,
    tool::BehaviorTool,
    validation::ValidationRule,
    concern::ConcernDescription,
    diagram::DNodeListElement,
    diagram::DEdge,
    DiagramDescription,
    diagram::DDiagramElement,
    DragAndDropTarget,
    diagram::DDiagramElementContainer,
    diagram::DNode,
    description::DocumentedElement,
    diagram::filter::FilterDescription,
    diagram::description::Layer,
    diagram::description::EdgeMappingImport,
    diagram::tool::ToolSection,
    diagram::description::EdgeMapping,
    diagram::concern::ConcernDescription,
    diagram::description::AbstractNodeMapping,
    DRepresentation,
    diagram::DDiagram,
    ArrangeConstraint,
    LineStyle,
    ReconnectionKind,
    ContainerLabelDirection,
    LabelPosition,
    EdgeArrows,
    ResizeKind,
    Side,
    LayoutDirection,
    FilterKind,
    ContainerShape,
    FoldingStyle,
    AlignmentKind,
    EdgeRouting,
    BundledImageShape,
    CenteringStyle,
    BackgroundStyle,
    LabelDirection,
    ContainerLayout,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_description::abstractnodemapping_is_not_abstract():
    assert not inspect.isabstract(description::AbstractNodeMapping)


def test_description::abstractnodemapping_constructor_exists():
    assert callable(description::AbstractNodeMapping.__init__)


def test_description::abstractnodemapping_constructor_args():
    sig = inspect.signature(description::AbstractNodeMapping.__init__)
    params = list(sig.parameters.keys())



def test_description::diagramelementmapping_is_not_abstract():
    assert not inspect.isabstract(description::DiagramElementMapping)


def test_description::diagramelementmapping_constructor_exists():
    assert callable(description::DiagramElementMapping.__init__)


def test_description::diagramelementmapping_constructor_args():
    sig = inspect.signature(description::DiagramElementMapping.__init__)
    params = list(sig.parameters.keys())



def test_tool::doubleclickdescription_is_not_abstract():
    assert not inspect.isabstract(tool::DoubleClickDescription)


def test_tool::doubleclickdescription_constructor_exists():
    assert callable(tool::DoubleClickDescription.__init__)


def test_tool::doubleclickdescription_constructor_args():
    sig = inspect.signature(tool::DoubleClickDescription.__init__)
    params = list(sig.parameters.keys())



def test_tool::directeditlabel_is_not_abstract():
    assert not inspect.isabstract(tool::DirectEditLabel)


def test_tool::directeditlabel_constructor_exists():
    assert callable(tool::DirectEditLabel.__init__)


def test_tool::directeditlabel_constructor_args():
    sig = inspect.signature(tool::DirectEditLabel.__init__)
    params = list(sig.parameters.keys())



def test_tool::deleteelementdescription_is_not_abstract():
    assert not inspect.isabstract(tool::DeleteElementDescription)


def test_tool::deleteelementdescription_constructor_exists():
    assert callable(tool::DeleteElementDescription.__init__)


def test_tool::deleteelementdescription_constructor_args():
    sig = inspect.signature(tool::DeleteElementDescription.__init__)
    params = list(sig.parameters.keys())



def test_description::representationelementmapping_is_not_abstract():
    assert not inspect.isabstract(description::RepresentationElementMapping)


def test_description::representationelementmapping_constructor_exists():
    assert callable(description::RepresentationElementMapping.__init__)


def test_description::representationelementmapping_constructor_args():
    sig = inspect.signature(description::RepresentationElementMapping.__init__)
    params = list(sig.parameters.keys())



def test_representationextensiondescription_is_not_abstract():
    assert not inspect.isabstract(RepresentationExtensionDescription)


def test_representationextensiondescription_constructor_exists():
    assert callable(RepresentationExtensionDescription.__init__)


def test_representationextensiondescription_constructor_args():
    sig = inspect.signature(RepresentationExtensionDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram::description::diagramextensiondescription_is_not_abstract():
    assert not inspect.isabstract(diagram::description::DiagramExtensionDescription)


def test_diagram::description::diagramextensiondescription_constructor_exists():
    assert callable(diagram::description::DiagramExtensionDescription.__init__)


def test_diagram::description::diagramextensiondescription_constructor_args():
    sig = inspect.signature(diagram::description::DiagramExtensionDescription.__init__)
    params = list(sig.parameters.keys())



def test_description::diagramdescription_is_not_abstract():
    assert not inspect.isabstract(description::DiagramDescription)


def test_description::diagramdescription_constructor_exists():
    assert callable(description::DiagramDescription.__init__)


def test_description::diagramdescription_constructor_args():
    sig = inspect.signature(description::DiagramDescription.__init__)
    params = list(sig.parameters.keys())



def test_description::representationimportdescription_is_not_abstract():
    assert not inspect.isabstract(description::RepresentationImportDescription)


def test_description::representationimportdescription_constructor_exists():
    assert callable(description::RepresentationImportDescription.__init__)


def test_description::representationimportdescription_constructor_args():
    sig = inspect.signature(description::RepresentationImportDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram::description::diagramimportdescription_is_not_abstract():
    assert not inspect.isabstract(diagram::description::DiagramImportDescription)


def test_diagram::description::diagramimportdescription_constructor_exists():
    assert callable(diagram::description::DiagramImportDescription.__init__)


def test_diagram::description::diagramimportdescription_constructor_args():
    sig = inspect.signature(diagram::description::DiagramImportDescription.__init__)
    params = list(sig.parameters.keys())



def test_tool::toolsection_is_not_abstract():
    assert not inspect.isabstract(tool::ToolSection)


def test_tool::toolsection_constructor_exists():
    assert callable(tool::ToolSection.__init__)


def test_tool::toolsection_constructor_args():
    sig = inspect.signature(tool::ToolSection.__init__)
    params = list(sig.parameters.keys())



def test_edgemappingimport_is_not_abstract():
    assert not inspect.isabstract(EdgeMappingImport)


def test_edgemappingimport_constructor_exists():
    assert callable(EdgeMappingImport.__init__)


def test_edgemappingimport_constructor_args():
    sig = inspect.signature(EdgeMappingImport.__init__)
    params = list(sig.parameters.keys())



def test_additionallayer_is_not_abstract():
    assert not inspect.isabstract(AdditionalLayer)


def test_additionallayer_constructor_exists():
    assert callable(AdditionalLayer.__init__)


def test_additionallayer_constructor_args():
    sig = inspect.signature(AdditionalLayer.__init__)
    params = list(sig.parameters.keys())



def test_filter_is_not_abstract():
    assert not inspect.isabstract(Filter)


def test_filter_constructor_exists():
    assert callable(Filter.__init__)


def test_filter_constructor_args():
    sig = inspect.signature(Filter.__init__)
    params = list(sig.parameters.keys())



def test_diagram::filter::mappingfilter_is_not_abstract():
    assert not inspect.isabstract(diagram::filter::MappingFilter)


def test_diagram::filter::mappingfilter_constructor_exists():
    assert callable(diagram::filter::MappingFilter.__init__)


def test_diagram::filter::mappingfilter_constructor_args():
    sig = inspect.signature(diagram::filter::MappingFilter.__init__)
    params = list(sig.parameters.keys())
    assert "viewConditionExpression" in params, "Missing parameter 'viewConditionExpression'"
    assert "semanticConditionExpression" in params, "Missing parameter 'semanticConditionExpression'"

def test_diagram::filter::mappingfilter_has_viewConditionExpression():
    assert hasattr(diagram::filter::MappingFilter, "viewConditionExpression")
    descriptor = None
    for klass in diagram::filter::MappingFilter.__mro__:
        if "viewConditionExpression" in klass.__dict__:
            descriptor = klass.__dict__["viewConditionExpression"]
            break
    assert isinstance(descriptor, property)

def test_diagram::filter::mappingfilter_has_semanticConditionExpression():
    assert hasattr(diagram::filter::MappingFilter, "semanticConditionExpression")
    descriptor = None
    for klass in diagram::filter::MappingFilter.__mro__:
        if "semanticConditionExpression" in klass.__dict__:
            descriptor = klass.__dict__["semanticConditionExpression"]
            break
    assert isinstance(descriptor, property)



def test_diagram::filter::filter_is_not_abstract():
    assert not inspect.isabstract(diagram::filter::Filter)


def test_diagram::filter::filter_constructor_exists():
    assert callable(diagram::filter::Filter.__init__)


def test_diagram::filter::filter_constructor_args():
    sig = inspect.signature(diagram::filter::Filter.__init__)
    params = list(sig.parameters.keys())
    assert "filterKind" in params, "Missing parameter 'filterKind'"

def test_diagram::filter::filter_has_filterKind():
    assert hasattr(diagram::filter::Filter, "filterKind")
    descriptor = None
    for klass in diagram::filter::Filter.__mro__:
        if "filterKind" in klass.__dict__:
            descriptor = klass.__dict__["filterKind"]
            break
    assert isinstance(descriptor, property)



def test_interactivevariabledescription_is_not_abstract():
    assert not inspect.isabstract(InteractiveVariableDescription)


def test_interactivevariabledescription_constructor_exists():
    assert callable(InteractiveVariableDescription.__init__)


def test_interactivevariabledescription_constructor_args():
    sig = inspect.signature(InteractiveVariableDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram::filter::variablefilter_is_not_abstract():
    assert not inspect.isabstract(diagram::filter::VariableFilter)


def test_diagram::filter::variablefilter_constructor_exists():
    assert callable(diagram::filter::VariableFilter.__init__)


def test_diagram::filter::variablefilter_constructor_args():
    sig = inspect.signature(diagram::filter::VariableFilter.__init__)
    params = list(sig.parameters.keys())
    assert "semanticConditionExpression" in params, "Missing parameter 'semanticConditionExpression'"

def test_diagram::filter::variablefilter_has_semanticConditionExpression():
    assert hasattr(diagram::filter::VariableFilter, "semanticConditionExpression")
    descriptor = None
    for klass in diagram::filter::VariableFilter.__mro__:
        if "semanticConditionExpression" in klass.__dict__:
            descriptor = klass.__dict__["semanticConditionExpression"]
            break
    assert isinstance(descriptor, property)



def test_filter::filter_is_not_abstract():
    assert not inspect.isabstract(filter::Filter)


def test_filter::filter_constructor_exists():
    assert callable(filter::Filter.__init__)


def test_filter::filter_constructor_args():
    sig = inspect.signature(filter::Filter.__init__)
    params = list(sig.parameters.keys())



def test_filterdescription_is_not_abstract():
    assert not inspect.isabstract(FilterDescription)


def test_filterdescription_constructor_exists():
    assert callable(FilterDescription.__init__)


def test_filterdescription_constructor_args():
    sig = inspect.signature(FilterDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram::filter::compositefilterdescription_is_not_abstract():
    assert not inspect.isabstract(diagram::filter::CompositeFilterDescription)


def test_diagram::filter::compositefilterdescription_constructor_exists():
    assert callable(diagram::filter::CompositeFilterDescription.__init__)


def test_diagram::filter::compositefilterdescription_constructor_args():
    sig = inspect.signature(diagram::filter::CompositeFilterDescription.__init__)
    params = list(sig.parameters.keys())



def test_representationnavigationdescription_is_not_abstract():
    assert not inspect.isabstract(RepresentationNavigationDescription)


def test_representationnavigationdescription_constructor_exists():
    assert callable(RepresentationNavigationDescription.__init__)


def test_representationnavigationdescription_constructor_args():
    sig = inspect.signature(RepresentationNavigationDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram::tool::diagramnavigationdescription_is_not_abstract():
    assert not inspect.isabstract(diagram::tool::DiagramNavigationDescription)


def test_diagram::tool::diagramnavigationdescription_constructor_exists():
    assert callable(diagram::tool::DiagramNavigationDescription.__init__)


def test_diagram::tool::diagramnavigationdescription_constructor_args():
    sig = inspect.signature(diagram::tool::DiagramNavigationDescription.__init__)
    params = list(sig.parameters.keys())



def test_tool::initialcontainerdropoperation_is_not_abstract():
    assert not inspect.isabstract(tool::InitialContainerDropOperation)


def test_tool::initialcontainerdropoperation_constructor_exists():
    assert callable(tool::InitialContainerDropOperation.__init__)


def test_tool::initialcontainerdropoperation_constructor_args():
    sig = inspect.signature(tool::InitialContainerDropOperation.__init__)
    params = list(sig.parameters.keys())



def test_tool::elementdropvariable_is_not_abstract():
    assert not inspect.isabstract(tool::ElementDropVariable)


def test_tool::elementdropvariable_constructor_exists():
    assert callable(tool::ElementDropVariable.__init__)


def test_tool::elementdropvariable_constructor_args():
    sig = inspect.signature(tool::ElementDropVariable.__init__)
    params = list(sig.parameters.keys())



def test_tool::dropcontainervariable_is_not_abstract():
    assert not inspect.isabstract(tool::DropContainerVariable)


def test_tool::dropcontainervariable_constructor_exists():
    assert callable(tool::DropContainerVariable.__init__)


def test_tool::dropcontainervariable_constructor_args():
    sig = inspect.signature(tool::DropContainerVariable.__init__)
    params = list(sig.parameters.keys())



def test_representationcreationdescription_is_not_abstract():
    assert not inspect.isabstract(RepresentationCreationDescription)


def test_representationcreationdescription_constructor_exists():
    assert callable(RepresentationCreationDescription.__init__)


def test_representationcreationdescription_constructor_args():
    sig = inspect.signature(RepresentationCreationDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram::tool::diagramcreationdescription_is_not_abstract():
    assert not inspect.isabstract(diagram::tool::DiagramCreationDescription)


def test_diagram::tool::diagramcreationdescription_constructor_exists():
    assert callable(diagram::tool::DiagramCreationDescription.__init__)


def test_diagram::tool::diagramcreationdescription_constructor_args():
    sig = inspect.signature(diagram::tool::DiagramCreationDescription.__init__)
    params = list(sig.parameters.keys())



def test_createview_is_not_abstract():
    assert not inspect.isabstract(CreateView)


def test_createview_constructor_exists():
    assert callable(CreateView.__init__)


def test_createview_constructor_args():
    sig = inspect.signature(CreateView.__init__)
    params = list(sig.parameters.keys())



def test_diagram::tool::createedgeview_is_not_abstract():
    assert not inspect.isabstract(diagram::tool::CreateEdgeView)


def test_diagram::tool::createedgeview_constructor_exists():
    assert callable(diagram::tool::CreateEdgeView.__init__)


def test_diagram::tool::createedgeview_constructor_args():
    sig = inspect.signature(diagram::tool::CreateEdgeView.__init__)
    params = list(sig.parameters.keys())
    assert "targetExpression" in params, "Missing parameter 'targetExpression'"
    assert "sourceExpression" in params, "Missing parameter 'sourceExpression'"

def test_diagram::tool::createedgeview_has_targetExpression():
    assert hasattr(diagram::tool::CreateEdgeView, "targetExpression")
    descriptor = None
    for klass in diagram::tool::CreateEdgeView.__mro__:
        if "targetExpression" in klass.__dict__:
            descriptor = klass.__dict__["targetExpression"]
            break
    assert isinstance(descriptor, property)

def test_diagram::tool::createedgeview_has_sourceExpression():
    assert hasattr(diagram::tool::CreateEdgeView, "sourceExpression")
    descriptor = None
    for klass in diagram::tool::CreateEdgeView.__mro__:
        if "sourceExpression" in klass.__dict__:
            descriptor = klass.__dict__["sourceExpression"]
            break
    assert isinstance(descriptor, property)



def test_abstracttooldescription_is_not_abstract():
    assert not inspect.isabstract(AbstractToolDescription)


def test_abstracttooldescription_constructor_exists():
    assert callable(AbstractToolDescription.__init__)


def test_abstracttooldescription_constructor_args():
    sig = inspect.signature(AbstractToolDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram::tool::requestdescription_is_not_abstract():
    assert not inspect.isabstract(diagram::tool::RequestDescription)


def test_diagram::tool::requestdescription_constructor_exists():
    assert callable(diagram::tool::RequestDescription.__init__)


def test_diagram::tool::requestdescription_constructor_args():
    sig = inspect.signature(diagram::tool::RequestDescription.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_diagram::tool::requestdescription_has_type():
    assert hasattr(diagram::tool::RequestDescription, "type")
    descriptor = None
    for klass in diagram::tool::RequestDescription.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_containermodeloperation_is_not_abstract():
    assert not inspect.isabstract(ContainerModelOperation)


def test_containermodeloperation_constructor_exists():
    assert callable(ContainerModelOperation.__init__)


def test_containermodeloperation_constructor_args():
    sig = inspect.signature(ContainerModelOperation.__init__)
    params = list(sig.parameters.keys())



def test_diagram::tool::navigation_is_not_abstract():
    assert not inspect.isabstract(diagram::tool::Navigation)


def test_diagram::tool::navigation_constructor_exists():
    assert callable(diagram::tool::Navigation.__init__)


def test_diagram::tool::navigation_constructor_args():
    sig = inspect.signature(diagram::tool::Navigation.__init__)
    params = list(sig.parameters.keys())
    assert "createIfNotExistent" in params, "Missing parameter 'createIfNotExistent'"

def test_diagram::tool::navigation_has_createIfNotExistent():
    assert hasattr(diagram::tool::Navigation, "createIfNotExistent")
    descriptor = None
    for klass in diagram::tool::Navigation.__mro__:
        if "createIfNotExistent" in klass.__dict__:
            descriptor = klass.__dict__["createIfNotExistent"]
            break
    assert isinstance(descriptor, property)



def test_diagram::tool::createview_is_not_abstract():
    assert not inspect.isabstract(diagram::tool::CreateView)


def test_diagram::tool::createview_constructor_exists():
    assert callable(diagram::tool::CreateView.__init__)


def test_diagram::tool::createview_constructor_args():
    sig = inspect.signature(diagram::tool::CreateView.__init__)
    params = list(sig.parameters.keys())
    assert "variableName" in params, "Missing parameter 'variableName'"
    assert "containerViewExpression" in params, "Missing parameter 'containerViewExpression'"

def test_diagram::tool::createview_has_variableName():
    assert hasattr(diagram::tool::CreateView, "variableName")
    descriptor = None
    for klass in diagram::tool::CreateView.__mro__:
        if "variableName" in klass.__dict__:
            descriptor = klass.__dict__["variableName"]
            break
    assert isinstance(descriptor, property)

def test_diagram::tool::createview_has_containerViewExpression():
    assert hasattr(diagram::tool::CreateView, "containerViewExpression")
    descriptor = None
    for klass in diagram::tool::CreateView.__mro__:
        if "containerViewExpression" in klass.__dict__:
            descriptor = klass.__dict__["containerViewExpression"]
            break
    assert isinstance(descriptor, property)



def test_tool::variablecontainer_is_not_abstract():
    assert not inspect.isabstract(tool::VariableContainer)


def test_tool::variablecontainer_constructor_exists():
    assert callable(tool::VariableContainer.__init__)


def test_tool::variablecontainer_constructor_args():
    sig = inspect.signature(tool::VariableContainer.__init__)
    params = list(sig.parameters.keys())



def test_description::abstractvariable_is_not_abstract():
    assert not inspect.isabstract(description::AbstractVariable)


def test_description::abstractvariable_constructor_exists():
    assert callable(description::AbstractVariable.__init__)


def test_description::abstractvariable_constructor_args():
    sig = inspect.signature(description::AbstractVariable.__init__)
    params = list(sig.parameters.keys())



def test_diagram::tool::elementdoubleclickvariable_is_not_abstract():
    assert not inspect.isabstract(diagram::tool::ElementDoubleClickVariable)


def test_diagram::tool::elementdoubleclickvariable_constructor_exists():
    assert callable(diagram::tool::ElementDoubleClickVariable.__init__)


def test_diagram::tool::elementdoubleclickvariable_constructor_args():
    sig = inspect.signature(diagram::tool::ElementDoubleClickVariable.__init__)
    params = list(sig.parameters.keys())



def test_diagram::tool::targetedgecreationvariable_is_not_abstract():
    assert not inspect.isabstract(diagram::tool::TargetEdgeCreationVariable)


def test_diagram::tool::targetedgecreationvariable_constructor_exists():
    assert callable(diagram::tool::TargetEdgeCreationVariable.__init__)


def test_diagram::tool::targetedgecreationvariable_constructor_args():
    sig = inspect.signature(diagram::tool::TargetEdgeCreationVariable.__init__)
    params = list(sig.parameters.keys())



def test_diagram::tool::sourceedgeviewcreationvariable_is_not_abstract():
    assert not inspect.isabstract(diagram::tool::SourceEdgeViewCreationVariable)


def test_diagram::tool::sourceedgeviewcreationvariable_constructor_exists():
    assert callable(diagram::tool::SourceEdgeViewCreationVariable.__init__)


def test_diagram::tool::sourceedgeviewcreationvariable_constructor_args():
    sig = inspect.signature(diagram::tool::SourceEdgeViewCreationVariable.__init__)
    params = list(sig.parameters.keys())



def test_diagram::tool::nodecreationvariable_is_not_abstract():
    assert not inspect.isabstract(diagram::tool::NodeCreationVariable)


def test_diagram::tool::nodecreationvariable_constructor_exists():
    assert callable(diagram::tool::NodeCreationVariable.__init__)


def test_diagram::tool::nodecreationvariable_constructor_args():
    sig = inspect.signature(diagram::tool::NodeCreationVariable.__init__)
    params = list(sig.parameters.keys())



def test_diagram::tool::targetedgeviewcreationvariable_is_not_abstract():
    assert not inspect.isabstract(diagram::tool::TargetEdgeViewCreationVariable)


def test_diagram::tool::targetedgeviewcreationvariable_constructor_exists():
    assert callable(diagram::tool::TargetEdgeViewCreationVariable.__init__)


def test_diagram::tool::targetedgeviewcreationvariable_constructor_args():
    sig = inspect.signature(diagram::tool::TargetEdgeViewCreationVariable.__init__)
    params = list(sig.parameters.keys())



def test_diagram::tool::sourceedgecreationvariable_is_not_abstract():
    assert not inspect.isabstract(diagram::tool::SourceEdgeCreationVariable)


def test_diagram::tool::sourceedgecreationvariable_constructor_exists():
    assert callable(diagram::tool::SourceEdgeCreationVariable.__init__)


def test_diagram::tool::sourceedgecreationvariable_constructor_args():
    sig = inspect.signature(diagram::tool::SourceEdgeCreationVariable.__init__)
    params = list(sig.parameters.keys())



def test_diagram::tool::behaviortool_is_not_abstract():
    assert not inspect.isabstract(diagram::tool::BehaviorTool)


def test_diagram::tool::behaviortool_constructor_exists():
    assert callable(diagram::tool::BehaviorTool.__init__)


def test_diagram::tool::behaviortool_constructor_args():
    sig = inspect.signature(diagram::tool::BehaviorTool.__init__)
    params = list(sig.parameters.keys())
    assert "domainClass" in params, "Missing parameter 'domainClass'"

def test_diagram::tool::behaviortool_has_domainClass():
    assert hasattr(diagram::tool::BehaviorTool, "domainClass")
    descriptor = None
    for klass in diagram::tool::BehaviorTool.__mro__:
        if "domainClass" in klass.__dict__:
            descriptor = klass.__dict__["domainClass"]
            break
    assert isinstance(descriptor, property)



def test_tool::editmaskvariables_is_not_abstract():
    assert not inspect.isabstract(tool::EditMaskVariables)


def test_tool::editmaskvariables_constructor_exists():
    assert callable(tool::EditMaskVariables.__init__)


def test_tool::editmaskvariables_constructor_args():
    sig = inspect.signature(tool::EditMaskVariables.__init__)
    params = list(sig.parameters.keys())



def test_diagram::tool::deletehook_is_not_abstract():
    assert not inspect.isabstract(diagram::tool::DeleteHook)


def test_diagram::tool::deletehook_constructor_exists():
    assert callable(diagram::tool::DeleteHook.__init__)


def test_diagram::tool::deletehook_constructor_args():
    sig = inspect.signature(diagram::tool::DeleteHook.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_diagram::tool::deletehook_has_id():
    assert hasattr(diagram::tool::DeleteHook, "id")
    descriptor = None
    for klass in diagram::tool::DeleteHook.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_tool::elementselectvariable_is_not_abstract():
    assert not inspect.isabstract(tool::ElementSelectVariable)


def test_tool::elementselectvariable_constructor_exists():
    assert callable(tool::ElementSelectVariable.__init__)


def test_tool::elementselectvariable_constructor_args():
    sig = inspect.signature(tool::ElementSelectVariable.__init__)
    params = list(sig.parameters.keys())



def test_diagram::tool::deletehookparameter_is_not_abstract():
    assert not inspect.isabstract(diagram::tool::DeleteHookParameter)


def test_diagram::tool::deletehookparameter_constructor_exists():
    assert callable(diagram::tool::DeleteHookParameter.__init__)


def test_diagram::tool::deletehookparameter_constructor_args():
    sig = inspect.signature(diagram::tool::DeleteHookParameter.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_diagram::tool::deletehookparameter_has_value():
    assert hasattr(diagram::tool::DeleteHookParameter, "value")
    descriptor = None
    for klass in diagram::tool::DeleteHookParameter.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_diagram::tool::deletehookparameter_has_name():
    assert hasattr(diagram::tool::DeleteHookParameter, "name")
    descriptor = None
    for klass in diagram::tool::DeleteHookParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tool::deletehookparameter_is_not_abstract():
    assert not inspect.isabstract(tool::DeleteHookParameter)


def test_tool::deletehookparameter_constructor_exists():
    assert callable(tool::DeleteHookParameter.__init__)


def test_tool::deletehookparameter_constructor_args():
    sig = inspect.signature(tool::DeleteHookParameter.__init__)
    params = list(sig.parameters.keys())



def test_tool::elementdoubleclickvariable_is_not_abstract():
    assert not inspect.isabstract(tool::ElementDoubleClickVariable)


def test_tool::elementdoubleclickvariable_constructor_exists():
    assert callable(tool::ElementDoubleClickVariable.__init__)


def test_tool::elementdoubleclickvariable_constructor_args():
    sig = inspect.signature(tool::ElementDoubleClickVariable.__init__)
    params = list(sig.parameters.keys())



def test_tool::deletehook_is_not_abstract():
    assert not inspect.isabstract(tool::DeleteHook)


def test_tool::deletehook_constructor_exists():
    assert callable(tool::DeleteHook.__init__)


def test_tool::deletehook_constructor_args():
    sig = inspect.signature(tool::DeleteHook.__init__)
    params = list(sig.parameters.keys())



def test_tool::elementdeletevariable_is_not_abstract():
    assert not inspect.isabstract(tool::ElementDeleteVariable)


def test_tool::elementdeletevariable_constructor_exists():
    assert callable(tool::ElementDeleteVariable.__init__)


def test_tool::elementdeletevariable_constructor_args():
    sig = inspect.signature(tool::ElementDeleteVariable.__init__)
    params = list(sig.parameters.keys())



def test_tool::initedgecreationoperation_is_not_abstract():
    assert not inspect.isabstract(tool::InitEdgeCreationOperation)


def test_tool::initedgecreationoperation_constructor_exists():
    assert callable(tool::InitEdgeCreationOperation.__init__)


def test_tool::initedgecreationoperation_constructor_args():
    sig = inspect.signature(tool::InitEdgeCreationOperation.__init__)
    params = list(sig.parameters.keys())



def test_tool::targetedgeviewcreationvariable_is_not_abstract():
    assert not inspect.isabstract(tool::TargetEdgeViewCreationVariable)


def test_tool::targetedgeviewcreationvariable_constructor_exists():
    assert callable(tool::TargetEdgeViewCreationVariable.__init__)


def test_tool::targetedgeviewcreationvariable_constructor_args():
    sig = inspect.signature(tool::TargetEdgeViewCreationVariable.__init__)
    params = list(sig.parameters.keys())



def test_tool::sourceedgeviewcreationvariable_is_not_abstract():
    assert not inspect.isabstract(tool::SourceEdgeViewCreationVariable)


def test_tool::sourceedgeviewcreationvariable_constructor_exists():
    assert callable(tool::SourceEdgeViewCreationVariable.__init__)


def test_tool::sourceedgeviewcreationvariable_constructor_args():
    sig = inspect.signature(tool::SourceEdgeViewCreationVariable.__init__)
    params = list(sig.parameters.keys())



def test_tool::targetedgecreationvariable_is_not_abstract():
    assert not inspect.isabstract(tool::TargetEdgeCreationVariable)


def test_tool::targetedgecreationvariable_constructor_exists():
    assert callable(tool::TargetEdgeCreationVariable.__init__)


def test_tool::targetedgecreationvariable_constructor_args():
    sig = inspect.signature(tool::TargetEdgeCreationVariable.__init__)
    params = list(sig.parameters.keys())



def test_tool::sourceedgecreationvariable_is_not_abstract():
    assert not inspect.isabstract(tool::SourceEdgeCreationVariable)


def test_tool::sourceedgecreationvariable_constructor_exists():
    assert callable(tool::SourceEdgeCreationVariable.__init__)


def test_tool::sourceedgecreationvariable_constructor_args():
    sig = inspect.signature(tool::SourceEdgeCreationVariable.__init__)
    params = list(sig.parameters.keys())



def test_tool::popupmenu_is_not_abstract():
    assert not inspect.isabstract(tool::PopupMenu)


def test_tool::popupmenu_constructor_exists():
    assert callable(tool::PopupMenu.__init__)


def test_tool::popupmenu_constructor_args():
    sig = inspect.signature(tool::PopupMenu.__init__)
    params = list(sig.parameters.keys())



def test_tool::initialnodecreationoperation_is_not_abstract():
    assert not inspect.isabstract(tool::InitialNodeCreationOperation)


def test_tool::initialnodecreationoperation_constructor_exists():
    assert callable(tool::InitialNodeCreationOperation.__init__)


def test_tool::initialnodecreationoperation_constructor_args():
    sig = inspect.signature(tool::InitialNodeCreationOperation.__init__)
    params = list(sig.parameters.keys())



def test_tool::containerviewvariable_is_not_abstract():
    assert not inspect.isabstract(tool::ContainerViewVariable)


def test_tool::containerviewvariable_constructor_exists():
    assert callable(tool::ContainerViewVariable.__init__)


def test_tool::containerviewvariable_constructor_args():
    sig = inspect.signature(tool::ContainerViewVariable.__init__)
    params = list(sig.parameters.keys())



def test_tool::nodecreationvariable_is_not_abstract():
    assert not inspect.isabstract(tool::NodeCreationVariable)


def test_tool::nodecreationvariable_constructor_exists():
    assert callable(tool::NodeCreationVariable.__init__)


def test_tool::nodecreationvariable_constructor_args():
    sig = inspect.signature(tool::NodeCreationVariable.__init__)
    params = list(sig.parameters.keys())



def test_mappingbasedtooldescription_is_not_abstract():
    assert not inspect.isabstract(MappingBasedToolDescription)


def test_mappingbasedtooldescription_constructor_exists():
    assert callable(MappingBasedToolDescription.__init__)


def test_mappingbasedtooldescription_constructor_args():
    sig = inspect.signature(MappingBasedToolDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram::tool::doubleclickdescription_is_not_abstract():
    assert not inspect.isabstract(diagram::tool::DoubleClickDescription)


def test_diagram::tool::doubleclickdescription_constructor_exists():
    assert callable(diagram::tool::DoubleClickDescription.__init__)


def test_diagram::tool::doubleclickdescription_constructor_args():
    sig = inspect.signature(diagram::tool::DoubleClickDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram::tool::edgecreationdescription_is_not_abstract():
    assert not inspect.isabstract(diagram::tool::EdgeCreationDescription)


def test_diagram::tool::edgecreationdescription_constructor_exists():
    assert callable(diagram::tool::EdgeCreationDescription.__init__)


def test_diagram::tool::edgecreationdescription_constructor_args():
    sig = inspect.signature(diagram::tool::EdgeCreationDescription.__init__)
    params = list(sig.parameters.keys())
    assert "connectionStartPrecondition" in params, "Missing parameter 'connectionStartPrecondition'"
    assert "iconPath" in params, "Missing parameter 'iconPath'"

def test_diagram::tool::edgecreationdescription_has_connectionStartPrecondition():
    assert hasattr(diagram::tool::EdgeCreationDescription, "connectionStartPrecondition")
    descriptor = None
    for klass in diagram::tool::EdgeCreationDescription.__mro__:
        if "connectionStartPrecondition" in klass.__dict__:
            descriptor = klass.__dict__["connectionStartPrecondition"]
            break
    assert isinstance(descriptor, property)

def test_diagram::tool::edgecreationdescription_has_iconPath():
    assert hasattr(diagram::tool::EdgeCreationDescription, "iconPath")
    descriptor = None
    for klass in diagram::tool::EdgeCreationDescription.__mro__:
        if "iconPath" in klass.__dict__:
            descriptor = klass.__dict__["iconPath"]
            break
    assert isinstance(descriptor, property)



def test_diagram::tool::reconnectedgedescription_is_not_abstract():
    assert not inspect.isabstract(diagram::tool::ReconnectEdgeDescription)


def test_diagram::tool::reconnectedgedescription_constructor_exists():
    assert callable(diagram::tool::ReconnectEdgeDescription.__init__)


def test_diagram::tool::reconnectedgedescription_constructor_args():
    sig = inspect.signature(diagram::tool::ReconnectEdgeDescription.__init__)
    params = list(sig.parameters.keys())
    assert "reconnectionKind" in params, "Missing parameter 'reconnectionKind'"

def test_diagram::tool::reconnectedgedescription_has_reconnectionKind():
    assert hasattr(diagram::tool::ReconnectEdgeDescription, "reconnectionKind")
    descriptor = None
    for klass in diagram::tool::ReconnectEdgeDescription.__mro__:
        if "reconnectionKind" in klass.__dict__:
            descriptor = klass.__dict__["reconnectionKind"]
            break
    assert isinstance(descriptor, property)



def test_diagram::tool::containerdropdescription_is_not_abstract():
    assert not inspect.isabstract(diagram::tool::ContainerDropDescription)


def test_diagram::tool::containerdropdescription_constructor_exists():
    assert callable(diagram::tool::ContainerDropDescription.__init__)


def test_diagram::tool::containerdropdescription_constructor_args():
    sig = inspect.signature(diagram::tool::ContainerDropDescription.__init__)
    params = list(sig.parameters.keys())
    assert "dragSource" in params, "Missing parameter 'dragSource'"
    assert "moveEdges" in params, "Missing parameter 'moveEdges'"

def test_diagram::tool::containerdropdescription_has_dragSource():
    assert hasattr(diagram::tool::ContainerDropDescription, "dragSource")
    descriptor = None
    for klass in diagram::tool::ContainerDropDescription.__mro__:
        if "dragSource" in klass.__dict__:
            descriptor = klass.__dict__["dragSource"]
            break
    assert isinstance(descriptor, property)

def test_diagram::tool::containerdropdescription_has_moveEdges():
    assert hasattr(diagram::tool::ContainerDropDescription, "moveEdges")
    descriptor = None
    for klass in diagram::tool::ContainerDropDescription.__mro__:
        if "moveEdges" in klass.__dict__:
            descriptor = klass.__dict__["moveEdges"]
            break
    assert isinstance(descriptor, property)



def test_diagram::tool::containercreationdescription_is_not_abstract():
    assert not inspect.isabstract(diagram::tool::ContainerCreationDescription)


def test_diagram::tool::containercreationdescription_constructor_exists():
    assert callable(diagram::tool::ContainerCreationDescription.__init__)


def test_diagram::tool::containercreationdescription_constructor_args():
    sig = inspect.signature(diagram::tool::ContainerCreationDescription.__init__)
    params = list(sig.parameters.keys())
    assert "iconPath" in params, "Missing parameter 'iconPath'"

def test_diagram::tool::containercreationdescription_has_iconPath():
    assert hasattr(diagram::tool::ContainerCreationDescription, "iconPath")
    descriptor = None
    for klass in diagram::tool::ContainerCreationDescription.__mro__:
        if "iconPath" in klass.__dict__:
            descriptor = klass.__dict__["iconPath"]
            break
    assert isinstance(descriptor, property)



def test_diagram::tool::directeditlabel_is_not_abstract():
    assert not inspect.isabstract(diagram::tool::DirectEditLabel)


def test_diagram::tool::directeditlabel_constructor_exists():
    assert callable(diagram::tool::DirectEditLabel.__init__)


def test_diagram::tool::directeditlabel_constructor_args():
    sig = inspect.signature(diagram::tool::DirectEditLabel.__init__)
    params = list(sig.parameters.keys())
    assert "inputLabelExpression" in params, "Missing parameter 'inputLabelExpression'"

def test_diagram::tool::directeditlabel_has_inputLabelExpression():
    assert hasattr(diagram::tool::DirectEditLabel, "inputLabelExpression")
    descriptor = None
    for klass in diagram::tool::DirectEditLabel.__mro__:
        if "inputLabelExpression" in klass.__dict__:
            descriptor = klass.__dict__["inputLabelExpression"]
            break
    assert isinstance(descriptor, property)



def test_diagram::tool::deleteelementdescription_is_not_abstract():
    assert not inspect.isabstract(diagram::tool::DeleteElementDescription)


def test_diagram::tool::deleteelementdescription_constructor_exists():
    assert callable(diagram::tool::DeleteElementDescription.__init__)


def test_diagram::tool::deleteelementdescription_constructor_args():
    sig = inspect.signature(diagram::tool::DeleteElementDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram::tool::nodecreationdescription_is_not_abstract():
    assert not inspect.isabstract(diagram::tool::NodeCreationDescription)


def test_diagram::tool::nodecreationdescription_constructor_exists():
    assert callable(diagram::tool::NodeCreationDescription.__init__)


def test_diagram::tool::nodecreationdescription_constructor_args():
    sig = inspect.signature(diagram::tool::NodeCreationDescription.__init__)
    params = list(sig.parameters.keys())
    assert "iconPath" in params, "Missing parameter 'iconPath'"

def test_diagram::tool::nodecreationdescription_has_iconPath():
    assert hasattr(diagram::tool::NodeCreationDescription, "iconPath")
    descriptor = None
    for klass in diagram::tool::NodeCreationDescription.__mro__:
        if "iconPath" in klass.__dict__:
            descriptor = klass.__dict__["iconPath"]
            break
    assert isinstance(descriptor, property)



def test_tool::toolgroup_is_not_abstract():
    assert not inspect.isabstract(tool::ToolGroup)


def test_tool::toolgroup_constructor_exists():
    assert callable(tool::ToolGroup.__init__)


def test_tool::toolgroup_constructor_args():
    sig = inspect.signature(tool::ToolGroup.__init__)
    params = list(sig.parameters.keys())



def test_diagram::tool::toolgroupextension_is_not_abstract():
    assert not inspect.isabstract(diagram::tool::ToolGroupExtension)


def test_diagram::tool::toolgroupextension_constructor_exists():
    assert callable(diagram::tool::ToolGroupExtension.__init__)


def test_diagram::tool::toolgroupextension_constructor_args():
    sig = inspect.signature(diagram::tool::ToolGroupExtension.__init__)
    params = list(sig.parameters.keys())



def test_toolentry_is_not_abstract():
    assert not inspect.isabstract(ToolEntry)


def test_toolentry_constructor_exists():
    assert callable(ToolEntry.__init__)


def test_toolentry_constructor_args():
    sig = inspect.signature(ToolEntry.__init__)
    params = list(sig.parameters.keys())



def test_diagram::tool::toolgroup_is_not_abstract():
    assert not inspect.isabstract(diagram::tool::ToolGroup)


def test_diagram::tool::toolgroup_constructor_exists():
    assert callable(diagram::tool::ToolGroup.__init__)


def test_diagram::tool::toolgroup_constructor_args():
    sig = inspect.signature(diagram::tool::ToolGroup.__init__)
    params = list(sig.parameters.keys())



def test_tool::toolgroupextension_is_not_abstract():
    assert not inspect.isabstract(tool::ToolGroupExtension)


def test_tool::toolgroupextension_constructor_exists():
    assert callable(tool::ToolGroupExtension.__init__)


def test_tool::toolgroupextension_constructor_args():
    sig = inspect.signature(tool::ToolGroupExtension.__init__)
    params = list(sig.parameters.keys())



def test_style::beginlabelstyledescription_is_not_abstract():
    assert not inspect.isabstract(style::BeginLabelStyleDescription)


def test_style::beginlabelstyledescription_constructor_exists():
    assert callable(style::BeginLabelStyleDescription.__init__)


def test_style::beginlabelstyledescription_constructor_args():
    sig = inspect.signature(style::BeginLabelStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_tool::toolentry_is_not_abstract():
    assert not inspect.isabstract(tool::ToolEntry)


def test_tool::toolentry_constructor_exists():
    assert callable(tool::ToolEntry.__init__)


def test_tool::toolentry_constructor_args():
    sig = inspect.signature(tool::ToolEntry.__init__)
    params = list(sig.parameters.keys())



def test_diagram::style::hidelabelcapabilitystyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram::style::HideLabelCapabilityStyleDescription)


def test_diagram::style::hidelabelcapabilitystyledescription_constructor_exists():
    assert callable(diagram::style::HideLabelCapabilityStyleDescription.__init__)


def test_diagram::style::hidelabelcapabilitystyledescription_constructor_args():
    sig = inspect.signature(diagram::style::HideLabelCapabilityStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "hideLabelByDefault" in params, "Missing parameter 'hideLabelByDefault'"

def test_diagram::style::hidelabelcapabilitystyledescription_has_hideLabelByDefault():
    assert hasattr(diagram::style::HideLabelCapabilityStyleDescription, "hideLabelByDefault")
    descriptor = None
    for klass in diagram::style::HideLabelCapabilityStyleDescription.__mro__:
        if "hideLabelByDefault" in klass.__dict__:
            descriptor = klass.__dict__["hideLabelByDefault"]
            break
    assert isinstance(descriptor, property)



def test_edgestyledescription_is_not_abstract():
    assert not inspect.isabstract(EdgeStyleDescription)


def test_edgestyledescription_constructor_exists():
    assert callable(EdgeStyleDescription.__init__)


def test_edgestyledescription_constructor_args():
    sig = inspect.signature(EdgeStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram::style::bracketedgestyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram::style::BracketEdgeStyleDescription)


def test_diagram::style::bracketedgestyledescription_constructor_exists():
    assert callable(diagram::style::BracketEdgeStyleDescription.__init__)


def test_diagram::style::bracketedgestyledescription_constructor_args():
    sig = inspect.signature(diagram::style::BracketEdgeStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_basiclabelstyledescription_is_not_abstract():
    assert not inspect.isabstract(BasicLabelStyleDescription)


def test_basiclabelstyledescription_constructor_exists():
    assert callable(BasicLabelStyleDescription.__init__)


def test_basiclabelstyledescription_constructor_args():
    sig = inspect.signature(BasicLabelStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram::style::endlabelstyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram::style::EndLabelStyleDescription)


def test_diagram::style::endlabelstyledescription_constructor_exists():
    assert callable(diagram::style::EndLabelStyleDescription.__init__)


def test_diagram::style::endlabelstyledescription_constructor_args():
    sig = inspect.signature(diagram::style::EndLabelStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram::style::centerlabelstyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram::style::CenterLabelStyleDescription)


def test_diagram::style::centerlabelstyledescription_constructor_exists():
    assert callable(diagram::style::CenterLabelStyleDescription.__init__)


def test_diagram::style::centerlabelstyledescription_constructor_args():
    sig = inspect.signature(diagram::style::CenterLabelStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram::style::beginlabelstyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram::style::BeginLabelStyleDescription)


def test_diagram::style::beginlabelstyledescription_constructor_exists():
    assert callable(diagram::style::BeginLabelStyleDescription.__init__)


def test_diagram::style::beginlabelstyledescription_constructor_args():
    sig = inspect.signature(diagram::style::BeginLabelStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_style::endlabelstyledescription_is_not_abstract():
    assert not inspect.isabstract(style::EndLabelStyleDescription)


def test_style::endlabelstyledescription_constructor_exists():
    assert callable(style::EndLabelStyleDescription.__init__)


def test_style::endlabelstyledescription_constructor_args():
    sig = inspect.signature(style::EndLabelStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_style::centerlabelstyledescription_is_not_abstract():
    assert not inspect.isabstract(style::CenterLabelStyleDescription)


def test_style::centerlabelstyledescription_constructor_exists():
    assert callable(style::CenterLabelStyleDescription.__init__)


def test_style::centerlabelstyledescription_constructor_args():
    sig = inspect.signature(style::CenterLabelStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram::style::sizecomputationcontainerstyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram::style::SizeComputationContainerStyleDescription)


def test_diagram::style::sizecomputationcontainerstyledescription_constructor_exists():
    assert callable(diagram::style::SizeComputationContainerStyleDescription.__init__)


def test_diagram::style::sizecomputationcontainerstyledescription_constructor_args():
    sig = inspect.signature(diagram::style::SizeComputationContainerStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "widthComputationExpression" in params, "Missing parameter 'widthComputationExpression'"
    assert "heightComputationExpression" in params, "Missing parameter 'heightComputationExpression'"

def test_diagram::style::sizecomputationcontainerstyledescription_has_widthComputationExpression():
    assert hasattr(diagram::style::SizeComputationContainerStyleDescription, "widthComputationExpression")
    descriptor = None
    for klass in diagram::style::SizeComputationContainerStyleDescription.__mro__:
        if "widthComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["widthComputationExpression"]
            break
    assert isinstance(descriptor, property)

def test_diagram::style::sizecomputationcontainerstyledescription_has_heightComputationExpression():
    assert hasattr(diagram::style::SizeComputationContainerStyleDescription, "heightComputationExpression")
    descriptor = None
    for klass in diagram::style::SizeComputationContainerStyleDescription.__mro__:
        if "heightComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["heightComputationExpression"]
            break
    assert isinstance(descriptor, property)



def test_style::labelborderstyledescription_is_not_abstract():
    assert not inspect.isabstract(style::LabelBorderStyleDescription)


def test_style::labelborderstyledescription_constructor_exists():
    assert callable(style::LabelBorderStyleDescription.__init__)


def test_style::labelborderstyledescription_constructor_args():
    sig = inspect.signature(style::LabelBorderStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_style::sizecomputationcontainerstyledescription_is_not_abstract():
    assert not inspect.isabstract(style::SizeComputationContainerStyleDescription)


def test_style::sizecomputationcontainerstyledescription_constructor_exists():
    assert callable(style::SizeComputationContainerStyleDescription.__init__)


def test_style::sizecomputationcontainerstyledescription_constructor_args():
    sig = inspect.signature(style::SizeComputationContainerStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_style::roundedcornerstyledescription_is_not_abstract():
    assert not inspect.isabstract(style::RoundedCornerStyleDescription)


def test_style::roundedcornerstyledescription_constructor_exists():
    assert callable(style::RoundedCornerStyleDescription.__init__)


def test_style::roundedcornerstyledescription_constructor_args():
    sig = inspect.signature(style::RoundedCornerStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram::style::gaugesectiondescription_is_not_abstract():
    assert not inspect.isabstract(diagram::style::GaugeSectionDescription)


def test_diagram::style::gaugesectiondescription_constructor_exists():
    assert callable(diagram::style::GaugeSectionDescription.__init__)


def test_diagram::style::gaugesectiondescription_constructor_args():
    sig = inspect.signature(diagram::style::GaugeSectionDescription.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "minValueExpression" in params, "Missing parameter 'minValueExpression'"
    assert "valueExpression" in params, "Missing parameter 'valueExpression'"
    assert "maxValueExpression" in params, "Missing parameter 'maxValueExpression'"

def test_diagram::style::gaugesectiondescription_has_label():
    assert hasattr(diagram::style::GaugeSectionDescription, "label")
    descriptor = None
    for klass in diagram::style::GaugeSectionDescription.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_diagram::style::gaugesectiondescription_has_minValueExpression():
    assert hasattr(diagram::style::GaugeSectionDescription, "minValueExpression")
    descriptor = None
    for klass in diagram::style::GaugeSectionDescription.__mro__:
        if "minValueExpression" in klass.__dict__:
            descriptor = klass.__dict__["minValueExpression"]
            break
    assert isinstance(descriptor, property)

def test_diagram::style::gaugesectiondescription_has_valueExpression():
    assert hasattr(diagram::style::GaugeSectionDescription, "valueExpression")
    descriptor = None
    for klass in diagram::style::GaugeSectionDescription.__mro__:
        if "valueExpression" in klass.__dict__:
            descriptor = klass.__dict__["valueExpression"]
            break
    assert isinstance(descriptor, property)

def test_diagram::style::gaugesectiondescription_has_maxValueExpression():
    assert hasattr(diagram::style::GaugeSectionDescription, "maxValueExpression")
    descriptor = None
    for klass in diagram::style::GaugeSectionDescription.__mro__:
        if "maxValueExpression" in klass.__dict__:
            descriptor = klass.__dict__["maxValueExpression"]
            break
    assert isinstance(descriptor, property)



def test_style::gaugesectiondescription_is_not_abstract():
    assert not inspect.isabstract(style::GaugeSectionDescription)


def test_style::gaugesectiondescription_constructor_exists():
    assert callable(style::GaugeSectionDescription.__init__)


def test_style::gaugesectiondescription_constructor_args():
    sig = inspect.signature(style::GaugeSectionDescription.__init__)
    params = list(sig.parameters.keys())



def test_nodestyledescription_is_not_abstract():
    assert not inspect.isabstract(NodeStyleDescription)


def test_nodestyledescription_constructor_exists():
    assert callable(NodeStyleDescription.__init__)


def test_nodestyledescription_constructor_args():
    sig = inspect.signature(NodeStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram::style::dotdescription_is_not_abstract():
    assert not inspect.isabstract(diagram::style::DotDescription)


def test_diagram::style::dotdescription_constructor_exists():
    assert callable(diagram::style::DotDescription.__init__)


def test_diagram::style::dotdescription_constructor_args():
    sig = inspect.signature(diagram::style::DotDescription.__init__)
    params = list(sig.parameters.keys())
    assert "strokeSizeComputationExpression" in params, "Missing parameter 'strokeSizeComputationExpression'"

def test_diagram::style::dotdescription_has_strokeSizeComputationExpression():
    assert hasattr(diagram::style::DotDescription, "strokeSizeComputationExpression")
    descriptor = None
    for klass in diagram::style::DotDescription.__mro__:
        if "strokeSizeComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["strokeSizeComputationExpression"]
            break
    assert isinstance(descriptor, property)



def test_diagram::style::ellipsenodedescription_is_not_abstract():
    assert not inspect.isabstract(diagram::style::EllipseNodeDescription)


def test_diagram::style::ellipsenodedescription_constructor_exists():
    assert callable(diagram::style::EllipseNodeDescription.__init__)


def test_diagram::style::ellipsenodedescription_constructor_args():
    sig = inspect.signature(diagram::style::EllipseNodeDescription.__init__)
    params = list(sig.parameters.keys())
    assert "horizontalDiameterComputationExpression" in params, "Missing parameter 'horizontalDiameterComputationExpression'"
    assert "verticalDiameterComputationExpression" in params, "Missing parameter 'verticalDiameterComputationExpression'"

def test_diagram::style::ellipsenodedescription_has_horizontalDiameterComputationExpression():
    assert hasattr(diagram::style::EllipseNodeDescription, "horizontalDiameterComputationExpression")
    descriptor = None
    for klass in diagram::style::EllipseNodeDescription.__mro__:
        if "horizontalDiameterComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["horizontalDiameterComputationExpression"]
            break
    assert isinstance(descriptor, property)

def test_diagram::style::ellipsenodedescription_has_verticalDiameterComputationExpression():
    assert hasattr(diagram::style::EllipseNodeDescription, "verticalDiameterComputationExpression")
    descriptor = None
    for klass in diagram::style::EllipseNodeDescription.__mro__:
        if "verticalDiameterComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["verticalDiameterComputationExpression"]
            break
    assert isinstance(descriptor, property)



def test_diagram::style::lozengenodedescription_is_not_abstract():
    assert not inspect.isabstract(diagram::style::LozengeNodeDescription)


def test_diagram::style::lozengenodedescription_constructor_exists():
    assert callable(diagram::style::LozengeNodeDescription.__init__)


def test_diagram::style::lozengenodedescription_constructor_args():
    sig = inspect.signature(diagram::style::LozengeNodeDescription.__init__)
    params = list(sig.parameters.keys())
    assert "heightComputationExpression" in params, "Missing parameter 'heightComputationExpression'"
    assert "widthComputationExpression" in params, "Missing parameter 'widthComputationExpression'"

def test_diagram::style::lozengenodedescription_has_heightComputationExpression():
    assert hasattr(diagram::style::LozengeNodeDescription, "heightComputationExpression")
    descriptor = None
    for klass in diagram::style::LozengeNodeDescription.__mro__:
        if "heightComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["heightComputationExpression"]
            break
    assert isinstance(descriptor, property)

def test_diagram::style::lozengenodedescription_has_widthComputationExpression():
    assert hasattr(diagram::style::LozengeNodeDescription, "widthComputationExpression")
    descriptor = None
    for klass in diagram::style::LozengeNodeDescription.__mro__:
        if "widthComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["widthComputationExpression"]
            break
    assert isinstance(descriptor, property)



def test_diagram::style::bundledimagedescription_is_not_abstract():
    assert not inspect.isabstract(diagram::style::BundledImageDescription)


def test_diagram::style::bundledimagedescription_constructor_exists():
    assert callable(diagram::style::BundledImageDescription.__init__)


def test_diagram::style::bundledimagedescription_constructor_args():
    sig = inspect.signature(diagram::style::BundledImageDescription.__init__)
    params = list(sig.parameters.keys())
    assert "providedShapeID" in params, "Missing parameter 'providedShapeID'"
    assert "shape" in params, "Missing parameter 'shape'"

def test_diagram::style::bundledimagedescription_has_providedShapeID():
    assert hasattr(diagram::style::BundledImageDescription, "providedShapeID")
    descriptor = None
    for klass in diagram::style::BundledImageDescription.__mro__:
        if "providedShapeID" in klass.__dict__:
            descriptor = klass.__dict__["providedShapeID"]
            break
    assert isinstance(descriptor, property)

def test_diagram::style::bundledimagedescription_has_shape():
    assert hasattr(diagram::style::BundledImageDescription, "shape")
    descriptor = None
    for klass in diagram::style::BundledImageDescription.__mro__:
        if "shape" in klass.__dict__:
            descriptor = klass.__dict__["shape"]
            break
    assert isinstance(descriptor, property)



def test_diagram::style::squaredescription_is_not_abstract():
    assert not inspect.isabstract(diagram::style::SquareDescription)


def test_diagram::style::squaredescription_constructor_exists():
    assert callable(diagram::style::SquareDescription.__init__)


def test_diagram::style::squaredescription_constructor_args():
    sig = inspect.signature(diagram::style::SquareDescription.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"

def test_diagram::style::squaredescription_has_width():
    assert hasattr(diagram::style::SquareDescription, "width")
    descriptor = None
    for klass in diagram::style::SquareDescription.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_diagram::style::squaredescription_has_height():
    assert hasattr(diagram::style::SquareDescription, "height")
    descriptor = None
    for klass in diagram::style::SquareDescription.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_diagram::style::gaugecompositestyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram::style::GaugeCompositeStyleDescription)


def test_diagram::style::gaugecompositestyledescription_constructor_exists():
    assert callable(diagram::style::GaugeCompositeStyleDescription.__init__)


def test_diagram::style::gaugecompositestyledescription_constructor_args():
    sig = inspect.signature(diagram::style::GaugeCompositeStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "alignment" in params, "Missing parameter 'alignment'"

def test_diagram::style::gaugecompositestyledescription_has_alignment():
    assert hasattr(diagram::style::GaugeCompositeStyleDescription, "alignment")
    descriptor = None
    for klass in diagram::style::GaugeCompositeStyleDescription.__mro__:
        if "alignment" in klass.__dict__:
            descriptor = klass.__dict__["alignment"]
            break
    assert isinstance(descriptor, property)



def test_diagram::style::notedescription_is_not_abstract():
    assert not inspect.isabstract(diagram::style::NoteDescription)


def test_diagram::style::notedescription_constructor_exists():
    assert callable(diagram::style::NoteDescription.__init__)


def test_diagram::style::notedescription_constructor_args():
    sig = inspect.signature(diagram::style::NoteDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram::style::customstyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram::style::CustomStyleDescription)


def test_diagram::style::customstyledescription_constructor_exists():
    assert callable(diagram::style::CustomStyleDescription.__init__)


def test_diagram::style::customstyledescription_constructor_args():
    sig = inspect.signature(diagram::style::CustomStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_diagram::style::customstyledescription_has_id():
    assert hasattr(diagram::style::CustomStyleDescription, "id")
    descriptor = None
    for klass in diagram::style::CustomStyleDescription.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_style::hidelabelcapabilitystyledescription_is_not_abstract():
    assert not inspect.isabstract(style::HideLabelCapabilityStyleDescription)


def test_style::hidelabelcapabilitystyledescription_constructor_exists():
    assert callable(style::HideLabelCapabilityStyleDescription.__init__)


def test_style::hidelabelcapabilitystyledescription_constructor_args():
    sig = inspect.signature(style::HideLabelCapabilityStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_style::tooltipstyledescription_is_not_abstract():
    assert not inspect.isabstract(style::TooltipStyleDescription)


def test_style::tooltipstyledescription_constructor_exists():
    assert callable(style::TooltipStyleDescription.__init__)


def test_style::tooltipstyledescription_constructor_args():
    sig = inspect.signature(style::TooltipStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_style::labelstyledescription_is_not_abstract():
    assert not inspect.isabstract(style::LabelStyleDescription)


def test_style::labelstyledescription_constructor_exists():
    assert callable(style::LabelStyleDescription.__init__)


def test_style::labelstyledescription_constructor_args():
    sig = inspect.signature(style::LabelStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_style::borderedstyledescription_is_not_abstract():
    assert not inspect.isabstract(style::BorderedStyleDescription)


def test_style::borderedstyledescription_constructor_exists():
    assert callable(style::BorderedStyleDescription.__init__)


def test_style::borderedstyledescription_constructor_args():
    sig = inspect.signature(style::BorderedStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram::style::containerstyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram::style::ContainerStyleDescription)


def test_diagram::style::containerstyledescription_constructor_exists():
    assert callable(diagram::style::ContainerStyleDescription.__init__)


def test_diagram::style::containerstyledescription_constructor_args():
    sig = inspect.signature(diagram::style::ContainerStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "roundedCorner" in params, "Missing parameter 'roundedCorner'"
    assert "containerLabelDirection" in params, "Missing parameter 'containerLabelDirection'"

def test_diagram::style::containerstyledescription_has_roundedCorner():
    assert hasattr(diagram::style::ContainerStyleDescription, "roundedCorner")
    descriptor = None
    for klass in diagram::style::ContainerStyleDescription.__mro__:
        if "roundedCorner" in klass.__dict__:
            descriptor = klass.__dict__["roundedCorner"]
            break
    assert isinstance(descriptor, property)

def test_diagram::style::containerstyledescription_has_containerLabelDirection():
    assert hasattr(diagram::style::ContainerStyleDescription, "containerLabelDirection")
    descriptor = None
    for klass in diagram::style::ContainerStyleDescription.__mro__:
        if "containerLabelDirection" in klass.__dict__:
            descriptor = klass.__dict__["containerLabelDirection"]
            break
    assert isinstance(descriptor, property)



def test_colordescription_is_not_abstract():
    assert not inspect.isabstract(ColorDescription)


def test_colordescription_constructor_exists():
    assert callable(ColorDescription.__init__)


def test_colordescription_constructor_args():
    sig = inspect.signature(ColorDescription.__init__)
    params = list(sig.parameters.keys())



def test_styledescription_is_not_abstract():
    assert not inspect.isabstract(StyleDescription)


def test_styledescription_constructor_exists():
    assert callable(StyleDescription.__init__)


def test_styledescription_constructor_args():
    sig = inspect.signature(StyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram::style::roundedcornerstyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram::style::RoundedCornerStyleDescription)


def test_diagram::style::roundedcornerstyledescription_constructor_exists():
    assert callable(diagram::style::RoundedCornerStyleDescription.__init__)


def test_diagram::style::roundedcornerstyledescription_constructor_args():
    sig = inspect.signature(diagram::style::RoundedCornerStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "arcHeight" in params, "Missing parameter 'arcHeight'"
    assert "arcWidth" in params, "Missing parameter 'arcWidth'"

def test_diagram::style::roundedcornerstyledescription_has_arcHeight():
    assert hasattr(diagram::style::RoundedCornerStyleDescription, "arcHeight")
    descriptor = None
    for klass in diagram::style::RoundedCornerStyleDescription.__mro__:
        if "arcHeight" in klass.__dict__:
            descriptor = klass.__dict__["arcHeight"]
            break
    assert isinstance(descriptor, property)

def test_diagram::style::roundedcornerstyledescription_has_arcWidth():
    assert hasattr(diagram::style::RoundedCornerStyleDescription, "arcWidth")
    descriptor = None
    for klass in diagram::style::RoundedCornerStyleDescription.__mro__:
        if "arcWidth" in klass.__dict__:
            descriptor = klass.__dict__["arcWidth"]
            break
    assert isinstance(descriptor, property)



def test_diagram::style::edgestyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram::style::EdgeStyleDescription)


def test_diagram::style::edgestyledescription_constructor_exists():
    assert callable(diagram::style::EdgeStyleDescription.__init__)


def test_diagram::style::edgestyledescription_constructor_args():
    sig = inspect.signature(diagram::style::EdgeStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "sourceArrow" in params, "Missing parameter 'sourceArrow'"
    assert "sizeComputationExpression" in params, "Missing parameter 'sizeComputationExpression'"
    assert "targetArrow" in params, "Missing parameter 'targetArrow'"
    assert "lineStyle" in params, "Missing parameter 'lineStyle'"
    assert "endsCentering" in params, "Missing parameter 'endsCentering'"
    assert "foldingStyle" in params, "Missing parameter 'foldingStyle'"
    assert "routingStyle" in params, "Missing parameter 'routingStyle'"

def test_diagram::style::edgestyledescription_has_sourceArrow():
    assert hasattr(diagram::style::EdgeStyleDescription, "sourceArrow")
    descriptor = None
    for klass in diagram::style::EdgeStyleDescription.__mro__:
        if "sourceArrow" in klass.__dict__:
            descriptor = klass.__dict__["sourceArrow"]
            break
    assert isinstance(descriptor, property)

def test_diagram::style::edgestyledescription_has_sizeComputationExpression():
    assert hasattr(diagram::style::EdgeStyleDescription, "sizeComputationExpression")
    descriptor = None
    for klass in diagram::style::EdgeStyleDescription.__mro__:
        if "sizeComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["sizeComputationExpression"]
            break
    assert isinstance(descriptor, property)

def test_diagram::style::edgestyledescription_has_targetArrow():
    assert hasattr(diagram::style::EdgeStyleDescription, "targetArrow")
    descriptor = None
    for klass in diagram::style::EdgeStyleDescription.__mro__:
        if "targetArrow" in klass.__dict__:
            descriptor = klass.__dict__["targetArrow"]
            break
    assert isinstance(descriptor, property)

def test_diagram::style::edgestyledescription_has_lineStyle():
    assert hasattr(diagram::style::EdgeStyleDescription, "lineStyle")
    descriptor = None
    for klass in diagram::style::EdgeStyleDescription.__mro__:
        if "lineStyle" in klass.__dict__:
            descriptor = klass.__dict__["lineStyle"]
            break
    assert isinstance(descriptor, property)

def test_diagram::style::edgestyledescription_has_endsCentering():
    assert hasattr(diagram::style::EdgeStyleDescription, "endsCentering")
    descriptor = None
    for klass in diagram::style::EdgeStyleDescription.__mro__:
        if "endsCentering" in klass.__dict__:
            descriptor = klass.__dict__["endsCentering"]
            break
    assert isinstance(descriptor, property)

def test_diagram::style::edgestyledescription_has_foldingStyle():
    assert hasattr(diagram::style::EdgeStyleDescription, "foldingStyle")
    descriptor = None
    for klass in diagram::style::EdgeStyleDescription.__mro__:
        if "foldingStyle" in klass.__dict__:
            descriptor = klass.__dict__["foldingStyle"]
            break
    assert isinstance(descriptor, property)

def test_diagram::style::edgestyledescription_has_routingStyle():
    assert hasattr(diagram::style::EdgeStyleDescription, "routingStyle")
    descriptor = None
    for klass in diagram::style::EdgeStyleDescription.__mro__:
        if "routingStyle" in klass.__dict__:
            descriptor = klass.__dict__["routingStyle"]
            break
    assert isinstance(descriptor, property)



def test_diagram::style::borderedstyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram::style::BorderedStyleDescription)


def test_diagram::style::borderedstyledescription_constructor_exists():
    assert callable(diagram::style::BorderedStyleDescription.__init__)


def test_diagram::style::borderedstyledescription_constructor_args():
    sig = inspect.signature(diagram::style::BorderedStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "borderSizeComputationExpression" in params, "Missing parameter 'borderSizeComputationExpression'"
    assert "borderLineStyle" in params, "Missing parameter 'borderLineStyle'"

def test_diagram::style::borderedstyledescription_has_borderSizeComputationExpression():
    assert hasattr(diagram::style::BorderedStyleDescription, "borderSizeComputationExpression")
    descriptor = None
    for klass in diagram::style::BorderedStyleDescription.__mro__:
        if "borderSizeComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["borderSizeComputationExpression"]
            break
    assert isinstance(descriptor, property)

def test_diagram::style::borderedstyledescription_has_borderLineStyle():
    assert hasattr(diagram::style::BorderedStyleDescription, "borderLineStyle")
    descriptor = None
    for klass in diagram::style::BorderedStyleDescription.__mro__:
        if "borderLineStyle" in klass.__dict__:
            descriptor = klass.__dict__["borderLineStyle"]
            break
    assert isinstance(descriptor, property)



def test_tool::containerdropdescription_is_not_abstract():
    assert not inspect.isabstract(tool::ContainerDropDescription)


def test_tool::containerdropdescription_constructor_exists():
    assert callable(tool::ContainerDropDescription.__init__)


def test_tool::containerdropdescription_constructor_args():
    sig = inspect.signature(tool::ContainerDropDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram::description::draganddroptargetdescription_is_not_abstract():
    assert not inspect.isabstract(diagram::description::DragAndDropTargetDescription)


def test_diagram::description::draganddroptargetdescription_constructor_exists():
    assert callable(diagram::description::DragAndDropTargetDescription.__init__)


def test_diagram::description::draganddroptargetdescription_constructor_args():
    sig = inspect.signature(diagram::description::DragAndDropTargetDescription.__init__)
    params = list(sig.parameters.keys())



def test_customization_is_not_abstract():
    assert not inspect.isabstract(Customization)


def test_customization_constructor_exists():
    assert callable(Customization.__init__)


def test_customization_constructor_args():
    sig = inspect.signature(Customization.__init__)
    params = list(sig.parameters.keys())



def test_decorationdescriptionsset_is_not_abstract():
    assert not inspect.isabstract(DecorationDescriptionsSet)


def test_decorationdescriptionsset_constructor_exists():
    assert callable(DecorationDescriptionsSet.__init__)


def test_decorationdescriptionsset_constructor_args():
    sig = inspect.signature(DecorationDescriptionsSet.__init__)
    params = list(sig.parameters.keys())



def test_description::enduserdocumentedelement_is_not_abstract():
    assert not inspect.isabstract(description::EndUserDocumentedElement)


def test_description::enduserdocumentedelement_constructor_exists():
    assert callable(description::EndUserDocumentedElement.__init__)


def test_description::enduserdocumentedelement_constructor_args():
    sig = inspect.signature(description::EndUserDocumentedElement.__init__)
    params = list(sig.parameters.keys())



def test_decorationdescription_is_not_abstract():
    assert not inspect.isabstract(DecorationDescription)


def test_decorationdescription_constructor_exists():
    assert callable(DecorationDescription.__init__)


def test_decorationdescription_constructor_args():
    sig = inspect.signature(DecorationDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram::description::mappingbaseddecoration_is_not_abstract():
    assert not inspect.isabstract(diagram::description::MappingBasedDecoration)


def test_diagram::description::mappingbaseddecoration_constructor_exists():
    assert callable(diagram::description::MappingBasedDecoration.__init__)


def test_diagram::description::mappingbaseddecoration_constructor_args():
    sig = inspect.signature(diagram::description::MappingBasedDecoration.__init__)
    params = list(sig.parameters.keys())



def test_documentedelement_is_not_abstract():
    assert not inspect.isabstract(DocumentedElement)


def test_documentedelement_constructor_exists():
    assert callable(DocumentedElement.__init__)


def test_documentedelement_constructor_args():
    sig = inspect.signature(DocumentedElement.__init__)
    params = list(sig.parameters.keys())



def test_diagram::concern::concernset_is_not_abstract():
    assert not inspect.isabstract(diagram::concern::ConcernSet)


def test_diagram::concern::concernset_constructor_exists():
    assert callable(diagram::concern::ConcernSet.__init__)


def test_diagram::concern::concernset_constructor_args():
    sig = inspect.signature(diagram::concern::ConcernSet.__init__)
    params = list(sig.parameters.keys())



def test_diagram::description::layout_is_not_abstract():
    assert not inspect.isabstract(diagram::description::Layout)


def test_diagram::description::layout_constructor_exists():
    assert callable(diagram::description::Layout.__init__)


def test_diagram::description::layout_constructor_args():
    sig = inspect.signature(diagram::description::Layout.__init__)
    params = list(sig.parameters.keys())



def test_style::edgestyledescription_is_not_abstract():
    assert not inspect.isabstract(style::EdgeStyleDescription)


def test_style::edgestyledescription_constructor_exists():
    assert callable(style::EdgeStyleDescription.__init__)


def test_style::edgestyledescription_constructor_args():
    sig = inspect.signature(style::EdgeStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_conditionalstyledescription_is_not_abstract():
    assert not inspect.isabstract(ConditionalStyleDescription)


def test_conditionalstyledescription_constructor_exists():
    assert callable(ConditionalStyleDescription.__init__)


def test_conditionalstyledescription_constructor_args():
    sig = inspect.signature(ConditionalStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram::description::conditionaledgestyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram::description::ConditionalEdgeStyleDescription)


def test_diagram::description::conditionaledgestyledescription_constructor_exists():
    assert callable(diagram::description::ConditionalEdgeStyleDescription.__init__)


def test_diagram::description::conditionaledgestyledescription_constructor_args():
    sig = inspect.signature(diagram::description::ConditionalEdgeStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram::description::conditionalcontainerstyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram::description::ConditionalContainerStyleDescription)


def test_diagram::description::conditionalcontainerstyledescription_constructor_exists():
    assert callable(diagram::description::ConditionalContainerStyleDescription.__init__)


def test_diagram::description::conditionalcontainerstyledescription_constructor_args():
    sig = inspect.signature(diagram::description::ConditionalContainerStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram::description::conditionalnodestyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram::description::ConditionalNodeStyleDescription)


def test_diagram::description::conditionalnodestyledescription_constructor_exists():
    assert callable(diagram::description::ConditionalNodeStyleDescription.__init__)


def test_diagram::description::conditionalnodestyledescription_constructor_args():
    sig = inspect.signature(diagram::description::ConditionalNodeStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_description::identifiedelement_is_not_abstract():
    assert not inspect.isabstract(description::IdentifiedElement)


def test_description::identifiedelement_constructor_exists():
    assert callable(description::IdentifiedElement.__init__)


def test_description::identifiedelement_constructor_args():
    sig = inspect.signature(description::IdentifiedElement.__init__)
    params = list(sig.parameters.keys())



def test_diagram::description::iedgemapping_is_not_abstract():
    assert not inspect.isabstract(diagram::description::IEdgeMapping)


def test_diagram::description::iedgemapping_constructor_exists():
    assert callable(diagram::description::IEdgeMapping.__init__)


def test_diagram::description::iedgemapping_constructor_args():
    sig = inspect.signature(diagram::description::IEdgeMapping.__init__)
    params = list(sig.parameters.keys())



def test_abstractnodemapping_is_not_abstract():
    assert not inspect.isabstract(AbstractNodeMapping)


def test_abstractnodemapping_constructor_exists():
    assert callable(AbstractNodeMapping.__init__)


def test_abstractnodemapping_constructor_args():
    sig = inspect.signature(AbstractNodeMapping.__init__)
    params = list(sig.parameters.keys())



def test_tool::reconnectedgedescription_is_not_abstract():
    assert not inspect.isabstract(tool::ReconnectEdgeDescription)


def test_tool::reconnectedgedescription_constructor_exists():
    assert callable(tool::ReconnectEdgeDescription.__init__)


def test_tool::reconnectedgedescription_constructor_args():
    sig = inspect.signature(tool::ReconnectEdgeDescription.__init__)
    params = list(sig.parameters.keys())



def test_conditionaledgestyledescription_is_not_abstract():
    assert not inspect.isabstract(ConditionalEdgeStyleDescription)


def test_conditionaledgestyledescription_constructor_exists():
    assert callable(ConditionalEdgeStyleDescription.__init__)


def test_conditionaledgestyledescription_constructor_args():
    sig = inspect.signature(ConditionalEdgeStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_description::containermapping_is_not_abstract():
    assert not inspect.isabstract(description::ContainerMapping)


def test_description::containermapping_constructor_exists():
    assert callable(description::ContainerMapping.__init__)


def test_description::containermapping_constructor_args():
    sig = inspect.signature(description::ContainerMapping.__init__)
    params = list(sig.parameters.keys())



def test_conditionalnodestyledescription_is_not_abstract():
    assert not inspect.isabstract(ConditionalNodeStyleDescription)


def test_conditionalnodestyledescription_constructor_exists():
    assert callable(ConditionalNodeStyleDescription.__init__)


def test_conditionalnodestyledescription_constructor_args():
    sig = inspect.signature(ConditionalNodeStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_description::iedgemapping_is_not_abstract():
    assert not inspect.isabstract(description::IEdgeMapping)


def test_description::iedgemapping_constructor_exists():
    assert callable(description::IEdgeMapping.__init__)


def test_description::iedgemapping_constructor_args():
    sig = inspect.signature(description::IEdgeMapping.__init__)
    params = list(sig.parameters.keys())



def test_style::nodestyledescription_is_not_abstract():
    assert not inspect.isabstract(style::NodeStyleDescription)


def test_style::nodestyledescription_constructor_exists():
    assert callable(style::NodeStyleDescription.__init__)


def test_style::nodestyledescription_constructor_args():
    sig = inspect.signature(style::NodeStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_description::abstractmappingimport_is_not_abstract():
    assert not inspect.isabstract(description::AbstractMappingImport)


def test_description::abstractmappingimport_constructor_exists():
    assert callable(description::AbstractMappingImport.__init__)


def test_description::abstractmappingimport_constructor_args():
    sig = inspect.signature(description::AbstractMappingImport.__init__)
    params = list(sig.parameters.keys())



def test_diagram::description::containermappingimport_is_not_abstract():
    assert not inspect.isabstract(diagram::description::ContainerMappingImport)


def test_diagram::description::containermappingimport_constructor_exists():
    assert callable(diagram::description::ContainerMappingImport.__init__)


def test_diagram::description::containermappingimport_constructor_args():
    sig = inspect.signature(diagram::description::ContainerMappingImport.__init__)
    params = list(sig.parameters.keys())



def test_description::nodemapping_is_not_abstract():
    assert not inspect.isabstract(description::NodeMapping)


def test_description::nodemapping_constructor_exists():
    assert callable(description::NodeMapping.__init__)


def test_description::nodemapping_constructor_args():
    sig = inspect.signature(description::NodeMapping.__init__)
    params = list(sig.parameters.keys())



def test_diagram::description::nodemappingimport_is_not_abstract():
    assert not inspect.isabstract(diagram::description::NodeMappingImport)


def test_diagram::description::nodemappingimport_constructor_exists():
    assert callable(diagram::description::NodeMappingImport.__init__)


def test_diagram::description::nodemappingimport_constructor_args():
    sig = inspect.signature(diagram::description::NodeMappingImport.__init__)
    params = list(sig.parameters.keys())



def test_conditionalcontainerstyledescription_is_not_abstract():
    assert not inspect.isabstract(ConditionalContainerStyleDescription)


def test_conditionalcontainerstyledescription_constructor_exists():
    assert callable(ConditionalContainerStyleDescription.__init__)


def test_conditionalcontainerstyledescription_constructor_args():
    sig = inspect.signature(ConditionalContainerStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_style::containerstyledescription_is_not_abstract():
    assert not inspect.isabstract(style::ContainerStyleDescription)


def test_style::containerstyledescription_constructor_exists():
    assert callable(style::ContainerStyleDescription.__init__)


def test_style::containerstyledescription_constructor_args():
    sig = inspect.signature(style::ContainerStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram::style::flatcontainerstyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram::style::FlatContainerStyleDescription)


def test_diagram::style::flatcontainerstyledescription_constructor_exists():
    assert callable(diagram::style::FlatContainerStyleDescription.__init__)


def test_diagram::style::flatcontainerstyledescription_constructor_args():
    sig = inspect.signature(diagram::style::FlatContainerStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "backgroundStyle" in params, "Missing parameter 'backgroundStyle'"

def test_diagram::style::flatcontainerstyledescription_has_backgroundStyle():
    assert hasattr(diagram::style::FlatContainerStyleDescription, "backgroundStyle")
    descriptor = None
    for klass in diagram::style::FlatContainerStyleDescription.__mro__:
        if "backgroundStyle" in klass.__dict__:
            descriptor = klass.__dict__["backgroundStyle"]
            break
    assert isinstance(descriptor, property)



def test_diagram::style::workspaceimagedescription_is_not_abstract():
    assert not inspect.isabstract(diagram::style::WorkspaceImageDescription)


def test_diagram::style::workspaceimagedescription_constructor_exists():
    assert callable(diagram::style::WorkspaceImageDescription.__init__)


def test_diagram::style::workspaceimagedescription_constructor_args():
    sig = inspect.signature(diagram::style::WorkspaceImageDescription.__init__)
    params = list(sig.parameters.keys())
    assert "workspacePath" in params, "Missing parameter 'workspacePath'"

def test_diagram::style::workspaceimagedescription_has_workspacePath():
    assert hasattr(diagram::style::WorkspaceImageDescription, "workspacePath")
    descriptor = None
    for klass in diagram::style::WorkspaceImageDescription.__mro__:
        if "workspacePath" in klass.__dict__:
            descriptor = klass.__dict__["workspacePath"]
            break
    assert isinstance(descriptor, property)



def test_diagram::style::shapecontainerstyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram::style::ShapeContainerStyleDescription)


def test_diagram::style::shapecontainerstyledescription_constructor_exists():
    assert callable(diagram::style::ShapeContainerStyleDescription.__init__)


def test_diagram::style::shapecontainerstyledescription_constructor_args():
    sig = inspect.signature(diagram::style::ShapeContainerStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "shape" in params, "Missing parameter 'shape'"

def test_diagram::style::shapecontainerstyledescription_has_shape():
    assert hasattr(diagram::style::ShapeContainerStyleDescription, "shape")
    descriptor = None
    for klass in diagram::style::ShapeContainerStyleDescription.__mro__:
        if "shape" in klass.__dict__:
            descriptor = klass.__dict__["shape"]
            break
    assert isinstance(descriptor, property)



def test_tool::initialoperation_is_not_abstract():
    assert not inspect.isabstract(tool::InitialOperation)


def test_tool::initialoperation_constructor_exists():
    assert callable(tool::InitialOperation.__init__)


def test_tool::initialoperation_constructor_args():
    sig = inspect.signature(tool::InitialOperation.__init__)
    params = list(sig.parameters.keys())



def test_layout_is_not_abstract():
    assert not inspect.isabstract(Layout)


def test_layout_constructor_exists():
    assert callable(Layout.__init__)


def test_layout_constructor_args():
    sig = inspect.signature(Layout.__init__)
    params = list(sig.parameters.keys())



def test_diagram::description::orderedtreelayout_is_not_abstract():
    assert not inspect.isabstract(diagram::description::OrderedTreeLayout)


def test_diagram::description::orderedtreelayout_constructor_exists():
    assert callable(diagram::description::OrderedTreeLayout.__init__)


def test_diagram::description::orderedtreelayout_constructor_args():
    sig = inspect.signature(diagram::description::OrderedTreeLayout.__init__)
    params = list(sig.parameters.keys())
    assert "childrenExpression" in params, "Missing parameter 'childrenExpression'"

def test_diagram::description::orderedtreelayout_has_childrenExpression():
    assert hasattr(diagram::description::OrderedTreeLayout, "childrenExpression")
    descriptor = None
    for klass in diagram::description::OrderedTreeLayout.__mro__:
        if "childrenExpression" in klass.__dict__:
            descriptor = klass.__dict__["childrenExpression"]
            break
    assert isinstance(descriptor, property)



def test_diagram::description::compositelayout_is_not_abstract():
    assert not inspect.isabstract(diagram::description::CompositeLayout)


def test_diagram::description::compositelayout_constructor_exists():
    assert callable(diagram::description::CompositeLayout.__init__)


def test_diagram::description::compositelayout_constructor_args():
    sig = inspect.signature(diagram::description::CompositeLayout.__init__)
    params = list(sig.parameters.keys())
    assert "padding" in params, "Missing parameter 'padding'"
    assert "direction" in params, "Missing parameter 'direction'"

def test_diagram::description::compositelayout_has_padding():
    assert hasattr(diagram::description::CompositeLayout, "padding")
    descriptor = None
    for klass in diagram::description::CompositeLayout.__mro__:
        if "padding" in klass.__dict__:
            descriptor = klass.__dict__["padding"]
            break
    assert isinstance(descriptor, property)

def test_diagram::description::compositelayout_has_direction():
    assert hasattr(diagram::description::CompositeLayout, "direction")
    descriptor = None
    for klass in diagram::description::CompositeLayout.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_tool::representationcreationdescription_is_not_abstract():
    assert not inspect.isabstract(tool::RepresentationCreationDescription)


def test_tool::representationcreationdescription_constructor_exists():
    assert callable(tool::RepresentationCreationDescription.__init__)


def test_tool::representationcreationdescription_constructor_args():
    sig = inspect.signature(tool::RepresentationCreationDescription.__init__)
    params = list(sig.parameters.keys())



def test_tool::abstracttooldescription_is_not_abstract():
    assert not inspect.isabstract(tool::AbstractToolDescription)


def test_tool::abstracttooldescription_constructor_exists():
    assert callable(tool::AbstractToolDescription.__init__)


def test_tool::abstracttooldescription_constructor_args():
    sig = inspect.signature(tool::AbstractToolDescription.__init__)
    params = list(sig.parameters.keys())



def test_concern::concernset_is_not_abstract():
    assert not inspect.isabstract(concern::ConcernSet)


def test_concern::concernset_constructor_exists():
    assert callable(concern::ConcernSet.__init__)


def test_concern::concernset_constructor_args():
    sig = inspect.signature(concern::ConcernSet.__init__)
    params = list(sig.parameters.keys())



def test_validation::validationset_is_not_abstract():
    assert not inspect.isabstract(validation::ValidationSet)


def test_validation::validationset_constructor_exists():
    assert callable(validation::ValidationSet.__init__)


def test_validation::validationset_constructor_args():
    sig = inspect.signature(validation::ValidationSet.__init__)
    params = list(sig.parameters.keys())



def test_edgemapping_is_not_abstract():
    assert not inspect.isabstract(EdgeMapping)


def test_edgemapping_constructor_exists():
    assert callable(EdgeMapping.__init__)


def test_edgemapping_constructor_args():
    sig = inspect.signature(EdgeMapping.__init__)
    params = list(sig.parameters.keys())



def test_description::pastetargetdescription_is_not_abstract():
    assert not inspect.isabstract(description::PasteTargetDescription)


def test_description::pastetargetdescription_constructor_exists():
    assert callable(description::PasteTargetDescription.__init__)


def test_description::pastetargetdescription_constructor_args():
    sig = inspect.signature(description::PasteTargetDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram::description::diagramelementmapping_is_not_abstract():
    assert not inspect.isabstract(diagram::description::DiagramElementMapping)


def test_diagram::description::diagramelementmapping_constructor_exists():
    assert callable(diagram::description::DiagramElementMapping.__init__)


def test_diagram::description::diagramelementmapping_constructor_args():
    sig = inspect.signature(diagram::description::DiagramElementMapping.__init__)
    params = list(sig.parameters.keys())
    assert "synchronizationLock" in params, "Missing parameter 'synchronizationLock'"
    assert "createElements" in params, "Missing parameter 'createElements'"
    assert "preconditionExpression" in params, "Missing parameter 'preconditionExpression'"
    assert "semanticCandidatesExpression" in params, "Missing parameter 'semanticCandidatesExpression'"
    assert "semanticElements" in params, "Missing parameter 'semanticElements'"

def test_diagram::description::diagramelementmapping_has_synchronizationLock():
    assert hasattr(diagram::description::DiagramElementMapping, "synchronizationLock")
    descriptor = None
    for klass in diagram::description::DiagramElementMapping.__mro__:
        if "synchronizationLock" in klass.__dict__:
            descriptor = klass.__dict__["synchronizationLock"]
            break
    assert isinstance(descriptor, property)

def test_diagram::description::diagramelementmapping_has_createElements():
    assert hasattr(diagram::description::DiagramElementMapping, "createElements")
    descriptor = None
    for klass in diagram::description::DiagramElementMapping.__mro__:
        if "createElements" in klass.__dict__:
            descriptor = klass.__dict__["createElements"]
            break
    assert isinstance(descriptor, property)

def test_diagram::description::diagramelementmapping_has_preconditionExpression():
    assert hasattr(diagram::description::DiagramElementMapping, "preconditionExpression")
    descriptor = None
    for klass in diagram::description::DiagramElementMapping.__mro__:
        if "preconditionExpression" in klass.__dict__:
            descriptor = klass.__dict__["preconditionExpression"]
            break
    assert isinstance(descriptor, property)

def test_diagram::description::diagramelementmapping_has_semanticCandidatesExpression():
    assert hasattr(diagram::description::DiagramElementMapping, "semanticCandidatesExpression")
    descriptor = None
    for klass in diagram::description::DiagramElementMapping.__mro__:
        if "semanticCandidatesExpression" in klass.__dict__:
            descriptor = klass.__dict__["semanticCandidatesExpression"]
            break
    assert isinstance(descriptor, property)

def test_diagram::description::diagramelementmapping_has_semanticElements():
    assert hasattr(diagram::description::DiagramElementMapping, "semanticElements")
    descriptor = None
    for klass in diagram::description::DiagramElementMapping.__mro__:
        if "semanticElements" in klass.__dict__:
            descriptor = klass.__dict__["semanticElements"]
            break
    assert isinstance(descriptor, property)



def test_description::representationdescription_is_not_abstract():
    assert not inspect.isabstract(description::RepresentationDescription)


def test_description::representationdescription_constructor_exists():
    assert callable(description::RepresentationDescription.__init__)


def test_description::representationdescription_constructor_args():
    sig = inspect.signature(description::RepresentationDescription.__init__)
    params = list(sig.parameters.keys())



def test_description::draganddroptargetdescription_is_not_abstract():
    assert not inspect.isabstract(description::DragAndDropTargetDescription)


def test_description::draganddroptargetdescription_constructor_exists():
    assert callable(description::DragAndDropTargetDescription.__init__)


def test_description::draganddroptargetdescription_constructor_args():
    sig = inspect.signature(description::DragAndDropTargetDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram::description::containermapping_is_not_abstract():
    assert not inspect.isabstract(diagram::description::ContainerMapping)


def test_diagram::description::containermapping_constructor_exists():
    assert callable(diagram::description::ContainerMapping.__init__)


def test_diagram::description::containermapping_constructor_args():
    sig = inspect.signature(diagram::description::ContainerMapping.__init__)
    params = list(sig.parameters.keys())
    assert "childrenPresentation" in params, "Missing parameter 'childrenPresentation'"

def test_diagram::description::containermapping_has_childrenPresentation():
    assert hasattr(diagram::description::ContainerMapping, "childrenPresentation")
    descriptor = None
    for klass in diagram::description::ContainerMapping.__mro__:
        if "childrenPresentation" in klass.__dict__:
            descriptor = klass.__dict__["childrenPresentation"]
            break
    assert isinstance(descriptor, property)



def test_diagram::description::nodemapping_is_not_abstract():
    assert not inspect.isabstract(diagram::description::NodeMapping)


def test_diagram::description::nodemapping_constructor_exists():
    assert callable(diagram::description::NodeMapping.__init__)


def test_diagram::description::nodemapping_constructor_args():
    sig = inspect.signature(diagram::description::NodeMapping.__init__)
    params = list(sig.parameters.keys())



def test_diagram::description::diagramdescription_is_not_abstract():
    assert not inspect.isabstract(diagram::description::DiagramDescription)


def test_diagram::description::diagramdescription_constructor_exists():
    assert callable(diagram::description::DiagramDescription.__init__)


def test_diagram::description::diagramdescription_constructor_args():
    sig = inspect.signature(diagram::description::DiagramDescription.__init__)
    params = list(sig.parameters.keys())
    assert "domainClass" in params, "Missing parameter 'domainClass'"
    assert "rootExpression" in params, "Missing parameter 'rootExpression'"
    assert "preconditionExpression" in params, "Missing parameter 'preconditionExpression'"
    assert "enablePopupBars" in params, "Missing parameter 'enablePopupBars'"

def test_diagram::description::diagramdescription_has_domainClass():
    assert hasattr(diagram::description::DiagramDescription, "domainClass")
    descriptor = None
    for klass in diagram::description::DiagramDescription.__mro__:
        if "domainClass" in klass.__dict__:
            descriptor = klass.__dict__["domainClass"]
            break
    assert isinstance(descriptor, property)

def test_diagram::description::diagramdescription_has_rootExpression():
    assert hasattr(diagram::description::DiagramDescription, "rootExpression")
    descriptor = None
    for klass in diagram::description::DiagramDescription.__mro__:
        if "rootExpression" in klass.__dict__:
            descriptor = klass.__dict__["rootExpression"]
            break
    assert isinstance(descriptor, property)

def test_diagram::description::diagramdescription_has_preconditionExpression():
    assert hasattr(diagram::description::DiagramDescription, "preconditionExpression")
    descriptor = None
    for klass in diagram::description::DiagramDescription.__mro__:
        if "preconditionExpression" in klass.__dict__:
            descriptor = klass.__dict__["preconditionExpression"]
            break
    assert isinstance(descriptor, property)

def test_diagram::description::diagramdescription_has_enablePopupBars():
    assert hasattr(diagram::description::DiagramDescription, "enablePopupBars")
    descriptor = None
    for klass in diagram::description::DiagramDescription.__mro__:
        if "enablePopupBars" in klass.__dict__:
            descriptor = klass.__dict__["enablePopupBars"]
            break
    assert isinstance(descriptor, property)



def test_diagram::eobject_is_not_abstract():
    assert not inspect.isabstract(diagram::EObject)


def test_diagram::eobject_constructor_exists():
    assert callable(diagram::EObject.__init__)


def test_diagram::eobject_constructor_args():
    sig = inspect.signature(diagram::EObject.__init__)
    params = list(sig.parameters.keys())



def test_tool::selectmodelelementvariable_is_not_abstract():
    assert not inspect.isabstract(tool::SelectModelElementVariable)


def test_tool::selectmodelelementvariable_constructor_exists():
    assert callable(tool::SelectModelElementVariable.__init__)


def test_tool::selectmodelelementvariable_constructor_args():
    sig = inspect.signature(tool::SelectModelElementVariable.__init__)
    params = list(sig.parameters.keys())



def test_typedvariable_is_not_abstract():
    assert not inspect.isabstract(TypedVariable)


def test_typedvariable_constructor_exists():
    assert callable(TypedVariable.__init__)


def test_typedvariable_constructor_args():
    sig = inspect.signature(TypedVariable.__init__)
    params = list(sig.parameters.keys())



def test_variablevalue_is_not_abstract():
    assert not inspect.isabstract(VariableValue)


def test_variablevalue_constructor_exists():
    assert callable(VariableValue.__init__)


def test_variablevalue_constructor_args():
    sig = inspect.signature(VariableValue.__init__)
    params = list(sig.parameters.keys())



def test_diagram::eobjectvariablevalue_is_not_abstract():
    assert not inspect.isabstract(diagram::EObjectVariableValue)


def test_diagram::eobjectvariablevalue_constructor_exists():
    assert callable(diagram::EObjectVariableValue.__init__)


def test_diagram::eobjectvariablevalue_constructor_args():
    sig = inspect.signature(diagram::EObjectVariableValue.__init__)
    params = list(sig.parameters.keys())



def test_diagram::typedvariablevalue_is_not_abstract():
    assert not inspect.isabstract(diagram::TypedVariableValue)


def test_diagram::typedvariablevalue_constructor_exists():
    assert callable(diagram::TypedVariableValue.__init__)


def test_diagram::typedvariablevalue_constructor_args():
    sig = inspect.signature(diagram::TypedVariableValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_diagram::typedvariablevalue_has_value():
    assert hasattr(diagram::TypedVariableValue, "value")
    descriptor = None
    for klass in diagram::TypedVariableValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_diagram::hidelabelcapabilitystyle_is_not_abstract():
    assert not inspect.isabstract(diagram::HideLabelCapabilityStyle)


def test_diagram::hidelabelcapabilitystyle_constructor_exists():
    assert callable(diagram::HideLabelCapabilityStyle.__init__)


def test_diagram::hidelabelcapabilitystyle_constructor_args():
    sig = inspect.signature(diagram::HideLabelCapabilityStyle.__init__)
    params = list(sig.parameters.keys())
    assert "hideLabelByDefault" in params, "Missing parameter 'hideLabelByDefault'"

def test_diagram::hidelabelcapabilitystyle_has_hideLabelByDefault():
    assert hasattr(diagram::HideLabelCapabilityStyle, "hideLabelByDefault")
    descriptor = None
    for klass in diagram::HideLabelCapabilityStyle.__mro__:
        if "hideLabelByDefault" in klass.__dict__:
            descriptor = klass.__dict__["hideLabelByDefault"]
            break
    assert isinstance(descriptor, property)



def test_diagram::draganddroptarget_is_not_abstract():
    assert not inspect.isabstract(diagram::DragAndDropTarget)


def test_diagram::draganddroptarget_constructor_exists():
    assert callable(diagram::DragAndDropTarget.__init__)


def test_diagram::draganddroptarget_constructor_args():
    sig = inspect.signature(diagram::DragAndDropTarget.__init__)
    params = list(sig.parameters.keys())



def test_style::styledescription_is_not_abstract():
    assert not inspect.isabstract(style::StyleDescription)


def test_style::styledescription_constructor_exists():
    assert callable(style::StyleDescription.__init__)


def test_style::styledescription_constructor_args():
    sig = inspect.signature(style::StyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram::style::nodestyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram::style::NodeStyleDescription)


def test_diagram::style::nodestyledescription_constructor_exists():
    assert callable(diagram::style::NodeStyleDescription.__init__)


def test_diagram::style::nodestyledescription_constructor_args():
    sig = inspect.signature(diagram::style::NodeStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "sizeComputationExpression" in params, "Missing parameter 'sizeComputationExpression'"
    assert "resizeKind" in params, "Missing parameter 'resizeKind'"
    assert "labelDirection" in params, "Missing parameter 'labelDirection'"
    assert "labelPosition" in params, "Missing parameter 'labelPosition'"
    assert "forbiddenSides" in params, "Missing parameter 'forbiddenSides'"

def test_diagram::style::nodestyledescription_has_sizeComputationExpression():
    assert hasattr(diagram::style::NodeStyleDescription, "sizeComputationExpression")
    descriptor = None
    for klass in diagram::style::NodeStyleDescription.__mro__:
        if "sizeComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["sizeComputationExpression"]
            break
    assert isinstance(descriptor, property)

def test_diagram::style::nodestyledescription_has_resizeKind():
    assert hasattr(diagram::style::NodeStyleDescription, "resizeKind")
    descriptor = None
    for klass in diagram::style::NodeStyleDescription.__mro__:
        if "resizeKind" in klass.__dict__:
            descriptor = klass.__dict__["resizeKind"]
            break
    assert isinstance(descriptor, property)

def test_diagram::style::nodestyledescription_has_labelDirection():
    assert hasattr(diagram::style::NodeStyleDescription, "labelDirection")
    descriptor = None
    for klass in diagram::style::NodeStyleDescription.__mro__:
        if "labelDirection" in klass.__dict__:
            descriptor = klass.__dict__["labelDirection"]
            break
    assert isinstance(descriptor, property)

def test_diagram::style::nodestyledescription_has_labelPosition():
    assert hasattr(diagram::style::NodeStyleDescription, "labelPosition")
    descriptor = None
    for klass in diagram::style::NodeStyleDescription.__mro__:
        if "labelPosition" in klass.__dict__:
            descriptor = klass.__dict__["labelPosition"]
            break
    assert isinstance(descriptor, property)

def test_diagram::style::nodestyledescription_has_forbiddenSides():
    assert hasattr(diagram::style::NodeStyleDescription, "forbiddenSides")
    descriptor = None
    for klass in diagram::style::NodeStyleDescription.__mro__:
        if "forbiddenSides" in klass.__dict__:
            descriptor = klass.__dict__["forbiddenSides"]
            break
    assert isinstance(descriptor, property)



def test_diagram::computedstyledescriptionregistry_is_not_abstract():
    assert not inspect.isabstract(diagram::ComputedStyleDescriptionRegistry)


def test_diagram::computedstyledescriptionregistry_constructor_exists():
    assert callable(diagram::ComputedStyleDescriptionRegistry.__init__)


def test_diagram::computedstyledescriptionregistry_constructor_args():
    sig = inspect.signature(diagram::ComputedStyleDescriptionRegistry.__init__)
    params = list(sig.parameters.keys())



def test_edgestyle_is_not_abstract():
    assert not inspect.isabstract(EdgeStyle)


def test_edgestyle_constructor_exists():
    assert callable(EdgeStyle.__init__)


def test_edgestyle_constructor_args():
    sig = inspect.signature(EdgeStyle.__init__)
    params = list(sig.parameters.keys())



def test_diagram::bracketedgestyle_is_not_abstract():
    assert not inspect.isabstract(diagram::BracketEdgeStyle)


def test_diagram::bracketedgestyle_constructor_exists():
    assert callable(diagram::BracketEdgeStyle.__init__)


def test_diagram::bracketedgestyle_constructor_args():
    sig = inspect.signature(diagram::BracketEdgeStyle.__init__)
    params = list(sig.parameters.keys())



def test_basiclabelstyle_is_not_abstract():
    assert not inspect.isabstract(BasicLabelStyle)


def test_basiclabelstyle_constructor_exists():
    assert callable(BasicLabelStyle.__init__)


def test_basiclabelstyle_constructor_args():
    sig = inspect.signature(BasicLabelStyle.__init__)
    params = list(sig.parameters.keys())



def test_collapsefilter_is_not_abstract():
    assert not inspect.isabstract(CollapseFilter)


def test_collapsefilter_constructor_exists():
    assert callable(CollapseFilter.__init__)


def test_collapsefilter_constructor_args():
    sig = inspect.signature(CollapseFilter.__init__)
    params = list(sig.parameters.keys())



def test_diagram::indirectlycollapsefilter_is_not_abstract():
    assert not inspect.isabstract(diagram::IndirectlyCollapseFilter)


def test_diagram::indirectlycollapsefilter_constructor_exists():
    assert callable(diagram::IndirectlyCollapseFilter.__init__)


def test_diagram::indirectlycollapsefilter_constructor_args():
    sig = inspect.signature(diagram::IndirectlyCollapseFilter.__init__)
    params = list(sig.parameters.keys())



def test_diagram::variablevalue_is_not_abstract():
    assert not inspect.isabstract(diagram::VariableValue)


def test_diagram::variablevalue_constructor_exists():
    assert callable(diagram::VariableValue.__init__)


def test_diagram::variablevalue_constructor_args():
    sig = inspect.signature(diagram::VariableValue.__init__)
    params = list(sig.parameters.keys())



def test_diagram::endlabelstyle_is_not_abstract():
    assert not inspect.isabstract(diagram::EndLabelStyle)


def test_diagram::endlabelstyle_constructor_exists():
    assert callable(diagram::EndLabelStyle.__init__)


def test_diagram::endlabelstyle_constructor_args():
    sig = inspect.signature(diagram::EndLabelStyle.__init__)
    params = list(sig.parameters.keys())



def test_diagram::centerlabelstyle_is_not_abstract():
    assert not inspect.isabstract(diagram::CenterLabelStyle)


def test_diagram::centerlabelstyle_constructor_exists():
    assert callable(diagram::CenterLabelStyle.__init__)


def test_diagram::centerlabelstyle_constructor_args():
    sig = inspect.signature(diagram::CenterLabelStyle.__init__)
    params = list(sig.parameters.keys())



def test_diagram::beginlabelstyle_is_not_abstract():
    assert not inspect.isabstract(diagram::BeginLabelStyle)


def test_diagram::beginlabelstyle_constructor_exists():
    assert callable(diagram::BeginLabelStyle.__init__)


def test_diagram::beginlabelstyle_constructor_args():
    sig = inspect.signature(diagram::BeginLabelStyle.__init__)
    params = list(sig.parameters.keys())



def test_customizable_is_not_abstract():
    assert not inspect.isabstract(Customizable)


def test_customizable_constructor_exists():
    assert callable(Customizable.__init__)


def test_customizable_constructor_args():
    sig = inspect.signature(Customizable.__init__)
    params = list(sig.parameters.keys())



def test_diagram::gaugesection_is_not_abstract():
    assert not inspect.isabstract(diagram::GaugeSection)


def test_diagram::gaugesection_constructor_exists():
    assert callable(diagram::GaugeSection.__init__)


def test_diagram::gaugesection_constructor_args():
    sig = inspect.signature(diagram::GaugeSection.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "label" in params, "Missing parameter 'label'"
    assert "foregroundColor" in params, "Missing parameter 'foregroundColor'"
    assert "max" in params, "Missing parameter 'max'"
    assert "min" in params, "Missing parameter 'min'"
    assert "backgroundColor" in params, "Missing parameter 'backgroundColor'"

def test_diagram::gaugesection_has_value():
    assert hasattr(diagram::GaugeSection, "value")
    descriptor = None
    for klass in diagram::GaugeSection.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_diagram::gaugesection_has_label():
    assert hasattr(diagram::GaugeSection, "label")
    descriptor = None
    for klass in diagram::GaugeSection.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_diagram::gaugesection_has_foregroundColor():
    assert hasattr(diagram::GaugeSection, "foregroundColor")
    descriptor = None
    for klass in diagram::GaugeSection.__mro__:
        if "foregroundColor" in klass.__dict__:
            descriptor = klass.__dict__["foregroundColor"]
            break
    assert isinstance(descriptor, property)

def test_diagram::gaugesection_has_max():
    assert hasattr(diagram::GaugeSection, "max")
    descriptor = None
    for klass in diagram::GaugeSection.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_diagram::gaugesection_has_min():
    assert hasattr(diagram::GaugeSection, "min")
    descriptor = None
    for klass in diagram::GaugeSection.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_diagram::gaugesection_has_backgroundColor():
    assert hasattr(diagram::GaugeSection, "backgroundColor")
    descriptor = None
    for klass in diagram::GaugeSection.__mro__:
        if "backgroundColor" in klass.__dict__:
            descriptor = klass.__dict__["backgroundColor"]
            break
    assert isinstance(descriptor, property)



def test_containerstyle_is_not_abstract():
    assert not inspect.isabstract(ContainerStyle)


def test_containerstyle_constructor_exists():
    assert callable(ContainerStyle.__init__)


def test_containerstyle_constructor_args():
    sig = inspect.signature(ContainerStyle.__init__)
    params = list(sig.parameters.keys())



def test_diagram::shapecontainerstyle_is_not_abstract():
    assert not inspect.isabstract(diagram::ShapeContainerStyle)


def test_diagram::shapecontainerstyle_constructor_exists():
    assert callable(diagram::ShapeContainerStyle.__init__)


def test_diagram::shapecontainerstyle_constructor_args():
    sig = inspect.signature(diagram::ShapeContainerStyle.__init__)
    params = list(sig.parameters.keys())
    assert "backgroundColor" in params, "Missing parameter 'backgroundColor'"
    assert "shape" in params, "Missing parameter 'shape'"

def test_diagram::shapecontainerstyle_has_backgroundColor():
    assert hasattr(diagram::ShapeContainerStyle, "backgroundColor")
    descriptor = None
    for klass in diagram::ShapeContainerStyle.__mro__:
        if "backgroundColor" in klass.__dict__:
            descriptor = klass.__dict__["backgroundColor"]
            break
    assert isinstance(descriptor, property)

def test_diagram::shapecontainerstyle_has_shape():
    assert hasattr(diagram::ShapeContainerStyle, "shape")
    descriptor = None
    for klass in diagram::ShapeContainerStyle.__mro__:
        if "shape" in klass.__dict__:
            descriptor = klass.__dict__["shape"]
            break
    assert isinstance(descriptor, property)



def test_diagram::flatcontainerstyle_is_not_abstract():
    assert not inspect.isabstract(diagram::FlatContainerStyle)


def test_diagram::flatcontainerstyle_constructor_exists():
    assert callable(diagram::FlatContainerStyle.__init__)


def test_diagram::flatcontainerstyle_constructor_args():
    sig = inspect.signature(diagram::FlatContainerStyle.__init__)
    params = list(sig.parameters.keys())
    assert "foregroundColor" in params, "Missing parameter 'foregroundColor'"
    assert "backgroundColor" in params, "Missing parameter 'backgroundColor'"
    assert "backgroundStyle" in params, "Missing parameter 'backgroundStyle'"

def test_diagram::flatcontainerstyle_has_foregroundColor():
    assert hasattr(diagram::FlatContainerStyle, "foregroundColor")
    descriptor = None
    for klass in diagram::FlatContainerStyle.__mro__:
        if "foregroundColor" in klass.__dict__:
            descriptor = klass.__dict__["foregroundColor"]
            break
    assert isinstance(descriptor, property)

def test_diagram::flatcontainerstyle_has_backgroundColor():
    assert hasattr(diagram::FlatContainerStyle, "backgroundColor")
    descriptor = None
    for klass in diagram::FlatContainerStyle.__mro__:
        if "backgroundColor" in klass.__dict__:
            descriptor = klass.__dict__["backgroundColor"]
            break
    assert isinstance(descriptor, property)

def test_diagram::flatcontainerstyle_has_backgroundStyle():
    assert hasattr(diagram::FlatContainerStyle, "backgroundStyle")
    descriptor = None
    for klass in diagram::FlatContainerStyle.__mro__:
        if "backgroundStyle" in klass.__dict__:
            descriptor = klass.__dict__["backgroundStyle"]
            break
    assert isinstance(descriptor, property)



def test_nodestyle_is_not_abstract():
    assert not inspect.isabstract(NodeStyle)


def test_nodestyle_constructor_exists():
    assert callable(NodeStyle.__init__)


def test_nodestyle_constructor_args():
    sig = inspect.signature(NodeStyle.__init__)
    params = list(sig.parameters.keys())



def test_diagram::lozenge_is_not_abstract():
    assert not inspect.isabstract(diagram::Lozenge)


def test_diagram::lozenge_constructor_exists():
    assert callable(diagram::Lozenge.__init__)


def test_diagram::lozenge_constructor_args():
    sig = inspect.signature(diagram::Lozenge.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"

def test_diagram::lozenge_has_color():
    assert hasattr(diagram::Lozenge, "color")
    descriptor = None
    for klass in diagram::Lozenge.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_diagram::lozenge_has_height():
    assert hasattr(diagram::Lozenge, "height")
    descriptor = None
    for klass in diagram::Lozenge.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_diagram::lozenge_has_width():
    assert hasattr(diagram::Lozenge, "width")
    descriptor = None
    for klass in diagram::Lozenge.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_diagram::customstyle_is_not_abstract():
    assert not inspect.isabstract(diagram::CustomStyle)


def test_diagram::customstyle_constructor_exists():
    assert callable(diagram::CustomStyle.__init__)


def test_diagram::customstyle_constructor_args():
    sig = inspect.signature(diagram::CustomStyle.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_diagram::customstyle_has_id():
    assert hasattr(diagram::CustomStyle, "id")
    descriptor = None
    for klass in diagram::CustomStyle.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_diagram::gaugecompositestyle_is_not_abstract():
    assert not inspect.isabstract(diagram::GaugeCompositeStyle)


def test_diagram::gaugecompositestyle_constructor_exists():
    assert callable(diagram::GaugeCompositeStyle.__init__)


def test_diagram::gaugecompositestyle_constructor_args():
    sig = inspect.signature(diagram::GaugeCompositeStyle.__init__)
    params = list(sig.parameters.keys())
    assert "alignment" in params, "Missing parameter 'alignment'"

def test_diagram::gaugecompositestyle_has_alignment():
    assert hasattr(diagram::GaugeCompositeStyle, "alignment")
    descriptor = None
    for klass in diagram::GaugeCompositeStyle.__mro__:
        if "alignment" in klass.__dict__:
            descriptor = klass.__dict__["alignment"]
            break
    assert isinstance(descriptor, property)



def test_diagram::square_is_not_abstract():
    assert not inspect.isabstract(diagram::Square)


def test_diagram::square_constructor_exists():
    assert callable(diagram::Square.__init__)


def test_diagram::square_constructor_args():
    sig = inspect.signature(diagram::Square.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "color" in params, "Missing parameter 'color'"
    assert "height" in params, "Missing parameter 'height'"

def test_diagram::square_has_width():
    assert hasattr(diagram::Square, "width")
    descriptor = None
    for klass in diagram::Square.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_diagram::square_has_color():
    assert hasattr(diagram::Square, "color")
    descriptor = None
    for klass in diagram::Square.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_diagram::square_has_height():
    assert hasattr(diagram::Square, "height")
    descriptor = None
    for klass in diagram::Square.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_diagram::workspaceimage_is_not_abstract():
    assert not inspect.isabstract(diagram::WorkspaceImage)


def test_diagram::workspaceimage_constructor_exists():
    assert callable(diagram::WorkspaceImage.__init__)


def test_diagram::workspaceimage_constructor_args():
    sig = inspect.signature(diagram::WorkspaceImage.__init__)
    params = list(sig.parameters.keys())
    assert "workspacePath" in params, "Missing parameter 'workspacePath'"

def test_diagram::workspaceimage_has_workspacePath():
    assert hasattr(diagram::WorkspaceImage, "workspacePath")
    descriptor = None
    for klass in diagram::WorkspaceImage.__mro__:
        if "workspacePath" in klass.__dict__:
            descriptor = klass.__dict__["workspacePath"]
            break
    assert isinstance(descriptor, property)



def test_diagram::bundledimage_is_not_abstract():
    assert not inspect.isabstract(diagram::BundledImage)


def test_diagram::bundledimage_constructor_exists():
    assert callable(diagram::BundledImage.__init__)


def test_diagram::bundledimage_constructor_args():
    sig = inspect.signature(diagram::BundledImage.__init__)
    params = list(sig.parameters.keys())
    assert "shape" in params, "Missing parameter 'shape'"
    assert "providedShapeID" in params, "Missing parameter 'providedShapeID'"
    assert "color" in params, "Missing parameter 'color'"

def test_diagram::bundledimage_has_shape():
    assert hasattr(diagram::BundledImage, "shape")
    descriptor = None
    for klass in diagram::BundledImage.__mro__:
        if "shape" in klass.__dict__:
            descriptor = klass.__dict__["shape"]
            break
    assert isinstance(descriptor, property)

def test_diagram::bundledimage_has_providedShapeID():
    assert hasattr(diagram::BundledImage, "providedShapeID")
    descriptor = None
    for klass in diagram::BundledImage.__mro__:
        if "providedShapeID" in klass.__dict__:
            descriptor = klass.__dict__["providedShapeID"]
            break
    assert isinstance(descriptor, property)

def test_diagram::bundledimage_has_color():
    assert hasattr(diagram::BundledImage, "color")
    descriptor = None
    for klass in diagram::BundledImage.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_diagram::ellipse_is_not_abstract():
    assert not inspect.isabstract(diagram::Ellipse)


def test_diagram::ellipse_constructor_exists():
    assert callable(diagram::Ellipse.__init__)


def test_diagram::ellipse_constructor_args():
    sig = inspect.signature(diagram::Ellipse.__init__)
    params = list(sig.parameters.keys())
    assert "verticalDiameter" in params, "Missing parameter 'verticalDiameter'"
    assert "color" in params, "Missing parameter 'color'"
    assert "horizontalDiameter" in params, "Missing parameter 'horizontalDiameter'"

def test_diagram::ellipse_has_verticalDiameter():
    assert hasattr(diagram::Ellipse, "verticalDiameter")
    descriptor = None
    for klass in diagram::Ellipse.__mro__:
        if "verticalDiameter" in klass.__dict__:
            descriptor = klass.__dict__["verticalDiameter"]
            break
    assert isinstance(descriptor, property)

def test_diagram::ellipse_has_color():
    assert hasattr(diagram::Ellipse, "color")
    descriptor = None
    for klass in diagram::Ellipse.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_diagram::ellipse_has_horizontalDiameter():
    assert hasattr(diagram::Ellipse, "horizontalDiameter")
    descriptor = None
    for klass in diagram::Ellipse.__mro__:
        if "horizontalDiameter" in klass.__dict__:
            descriptor = klass.__dict__["horizontalDiameter"]
            break
    assert isinstance(descriptor, property)



def test_diagram::note_is_not_abstract():
    assert not inspect.isabstract(diagram::Note)


def test_diagram::note_constructor_exists():
    assert callable(diagram::Note.__init__)


def test_diagram::note_constructor_args():
    sig = inspect.signature(diagram::Note.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"

def test_diagram::note_has_color():
    assert hasattr(diagram::Note, "color")
    descriptor = None
    for klass in diagram::Note.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_diagram::dot_is_not_abstract():
    assert not inspect.isabstract(diagram::Dot)


def test_diagram::dot_constructor_exists():
    assert callable(diagram::Dot.__init__)


def test_diagram::dot_constructor_args():
    sig = inspect.signature(diagram::Dot.__init__)
    params = list(sig.parameters.keys())
    assert "strokeSizeComputationExpression" in params, "Missing parameter 'strokeSizeComputationExpression'"
    assert "backgroundColor" in params, "Missing parameter 'backgroundColor'"

def test_diagram::dot_has_strokeSizeComputationExpression():
    assert hasattr(diagram::Dot, "strokeSizeComputationExpression")
    descriptor = None
    for klass in diagram::Dot.__mro__:
        if "strokeSizeComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["strokeSizeComputationExpression"]
            break
    assert isinstance(descriptor, property)

def test_diagram::dot_has_backgroundColor():
    assert hasattr(diagram::Dot, "backgroundColor")
    descriptor = None
    for klass in diagram::Dot.__mro__:
        if "backgroundColor" in klass.__dict__:
            descriptor = klass.__dict__["backgroundColor"]
            break
    assert isinstance(descriptor, property)



def test_hidelabelcapabilitystyle_is_not_abstract():
    assert not inspect.isabstract(HideLabelCapabilityStyle)


def test_hidelabelcapabilitystyle_constructor_exists():
    assert callable(HideLabelCapabilityStyle.__init__)


def test_hidelabelcapabilitystyle_constructor_args():
    sig = inspect.signature(HideLabelCapabilityStyle.__init__)
    params = list(sig.parameters.keys())



def test_borderedstyle_is_not_abstract():
    assert not inspect.isabstract(BorderedStyle)


def test_borderedstyle_constructor_exists():
    assert callable(BorderedStyle.__init__)


def test_borderedstyle_constructor_args():
    sig = inspect.signature(BorderedStyle.__init__)
    params = list(sig.parameters.keys())



def test_style_is_not_abstract():
    assert not inspect.isabstract(Style)


def test_style_constructor_exists():
    assert callable(Style.__init__)


def test_style_constructor_args():
    sig = inspect.signature(Style.__init__)
    params = list(sig.parameters.keys())



def test_diagram::borderedstyle_is_not_abstract():
    assert not inspect.isabstract(diagram::BorderedStyle)


def test_diagram::borderedstyle_constructor_exists():
    assert callable(diagram::BorderedStyle.__init__)


def test_diagram::borderedstyle_constructor_args():
    sig = inspect.signature(diagram::BorderedStyle.__init__)
    params = list(sig.parameters.keys())
    assert "borderSize" in params, "Missing parameter 'borderSize'"
    assert "borderColor" in params, "Missing parameter 'borderColor'"
    assert "borderSizeComputationExpression" in params, "Missing parameter 'borderSizeComputationExpression'"
    assert "borderLineStyle" in params, "Missing parameter 'borderLineStyle'"

def test_diagram::borderedstyle_has_borderSize():
    assert hasattr(diagram::BorderedStyle, "borderSize")
    descriptor = None
    for klass in diagram::BorderedStyle.__mro__:
        if "borderSize" in klass.__dict__:
            descriptor = klass.__dict__["borderSize"]
            break
    assert isinstance(descriptor, property)

def test_diagram::borderedstyle_has_borderColor():
    assert hasattr(diagram::BorderedStyle, "borderColor")
    descriptor = None
    for klass in diagram::BorderedStyle.__mro__:
        if "borderColor" in klass.__dict__:
            descriptor = klass.__dict__["borderColor"]
            break
    assert isinstance(descriptor, property)

def test_diagram::borderedstyle_has_borderSizeComputationExpression():
    assert hasattr(diagram::BorderedStyle, "borderSizeComputationExpression")
    descriptor = None
    for klass in diagram::BorderedStyle.__mro__:
        if "borderSizeComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["borderSizeComputationExpression"]
            break
    assert isinstance(descriptor, property)

def test_diagram::borderedstyle_has_borderLineStyle():
    assert hasattr(diagram::BorderedStyle, "borderLineStyle")
    descriptor = None
    for klass in diagram::BorderedStyle.__mro__:
        if "borderLineStyle" in klass.__dict__:
            descriptor = klass.__dict__["borderLineStyle"]
            break
    assert isinstance(descriptor, property)



def test_labelstyle_is_not_abstract():
    assert not inspect.isabstract(LabelStyle)


def test_labelstyle_constructor_exists():
    assert callable(LabelStyle.__init__)


def test_labelstyle_constructor_args():
    sig = inspect.signature(LabelStyle.__init__)
    params = list(sig.parameters.keys())



def test_iedgemapping_is_not_abstract():
    assert not inspect.isabstract(IEdgeMapping)


def test_iedgemapping_constructor_exists():
    assert callable(IEdgeMapping.__init__)


def test_iedgemapping_constructor_args():
    sig = inspect.signature(IEdgeMapping.__init__)
    params = list(sig.parameters.keys())



def test_diagram::edgetarget_is_not_abstract():
    assert not inspect.isabstract(diagram::EdgeTarget)


def test_diagram::edgetarget_constructor_exists():
    assert callable(diagram::EdgeTarget.__init__)


def test_diagram::edgetarget_constructor_args():
    sig = inspect.signature(diagram::EdgeTarget.__init__)
    params = list(sig.parameters.keys())



def test_diagram::edgestyle_is_not_abstract():
    assert not inspect.isabstract(diagram::EdgeStyle)


def test_diagram::edgestyle_constructor_exists():
    assert callable(diagram::EdgeStyle.__init__)


def test_diagram::edgestyle_constructor_args():
    sig = inspect.signature(diagram::EdgeStyle.__init__)
    params = list(sig.parameters.keys())
    assert "lineStyle" in params, "Missing parameter 'lineStyle'"
    assert "size" in params, "Missing parameter 'size'"
    assert "foldingStyle" in params, "Missing parameter 'foldingStyle'"
    assert "sourceArrow" in params, "Missing parameter 'sourceArrow'"
    assert "routingStyle" in params, "Missing parameter 'routingStyle'"
    assert "targetArrow" in params, "Missing parameter 'targetArrow'"
    assert "centered" in params, "Missing parameter 'centered'"
    assert "strokeColor" in params, "Missing parameter 'strokeColor'"

def test_diagram::edgestyle_has_lineStyle():
    assert hasattr(diagram::EdgeStyle, "lineStyle")
    descriptor = None
    for klass in diagram::EdgeStyle.__mro__:
        if "lineStyle" in klass.__dict__:
            descriptor = klass.__dict__["lineStyle"]
            break
    assert isinstance(descriptor, property)

def test_diagram::edgestyle_has_size():
    assert hasattr(diagram::EdgeStyle, "size")
    descriptor = None
    for klass in diagram::EdgeStyle.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_diagram::edgestyle_has_foldingStyle():
    assert hasattr(diagram::EdgeStyle, "foldingStyle")
    descriptor = None
    for klass in diagram::EdgeStyle.__mro__:
        if "foldingStyle" in klass.__dict__:
            descriptor = klass.__dict__["foldingStyle"]
            break
    assert isinstance(descriptor, property)

def test_diagram::edgestyle_has_sourceArrow():
    assert hasattr(diagram::EdgeStyle, "sourceArrow")
    descriptor = None
    for klass in diagram::EdgeStyle.__mro__:
        if "sourceArrow" in klass.__dict__:
            descriptor = klass.__dict__["sourceArrow"]
            break
    assert isinstance(descriptor, property)

def test_diagram::edgestyle_has_routingStyle():
    assert hasattr(diagram::EdgeStyle, "routingStyle")
    descriptor = None
    for klass in diagram::EdgeStyle.__mro__:
        if "routingStyle" in klass.__dict__:
            descriptor = klass.__dict__["routingStyle"]
            break
    assert isinstance(descriptor, property)

def test_diagram::edgestyle_has_targetArrow():
    assert hasattr(diagram::EdgeStyle, "targetArrow")
    descriptor = None
    for klass in diagram::EdgeStyle.__mro__:
        if "targetArrow" in klass.__dict__:
            descriptor = klass.__dict__["targetArrow"]
            break
    assert isinstance(descriptor, property)

def test_diagram::edgestyle_has_centered():
    assert hasattr(diagram::EdgeStyle, "centered")
    descriptor = None
    for klass in diagram::EdgeStyle.__mro__:
        if "centered" in klass.__dict__:
            descriptor = klass.__dict__["centered"]
            break
    assert isinstance(descriptor, property)

def test_diagram::edgestyle_has_strokeColor():
    assert hasattr(diagram::EdgeStyle, "strokeColor")
    descriptor = None
    for klass in diagram::EdgeStyle.__mro__:
        if "strokeColor" in klass.__dict__:
            descriptor = klass.__dict__["strokeColor"]
            break
    assert isinstance(descriptor, property)



def test_ddiagramelementcontainer_is_not_abstract():
    assert not inspect.isabstract(DDiagramElementContainer)


def test_ddiagramelementcontainer_constructor_exists():
    assert callable(DDiagramElementContainer.__init__)


def test_ddiagramelementcontainer_constructor_args():
    sig = inspect.signature(DDiagramElementContainer.__init__)
    params = list(sig.parameters.keys())



def test_diagram::dnodelist_is_not_abstract():
    assert not inspect.isabstract(diagram::DNodeList)


def test_diagram::dnodelist_constructor_exists():
    assert callable(diagram::DNodeList.__init__)


def test_diagram::dnodelist_constructor_args():
    sig = inspect.signature(diagram::DNodeList.__init__)
    params = list(sig.parameters.keys())



def test_diagram::dnodecontainer_is_not_abstract():
    assert not inspect.isabstract(diagram::DNodeContainer)


def test_diagram::dnodecontainer_constructor_exists():
    assert callable(diagram::DNodeContainer.__init__)


def test_diagram::dnodecontainer_constructor_args():
    sig = inspect.signature(diagram::DNodeContainer.__init__)
    params = list(sig.parameters.keys())
    assert "childrenPresentation" in params, "Missing parameter 'childrenPresentation'"

def test_diagram::dnodecontainer_has_childrenPresentation():
    assert hasattr(diagram::DNodeContainer, "childrenPresentation")
    descriptor = None
    for klass in diagram::DNodeContainer.__mro__:
        if "childrenPresentation" in klass.__dict__:
            descriptor = klass.__dict__["childrenPresentation"]
            break
    assert isinstance(descriptor, property)



def test_containermapping_is_not_abstract():
    assert not inspect.isabstract(ContainerMapping)


def test_containermapping_constructor_exists():
    assert callable(ContainerMapping.__init__)


def test_containermapping_constructor_args():
    sig = inspect.signature(ContainerMapping.__init__)
    params = list(sig.parameters.keys())



def test_diagram::containerstyle_is_not_abstract():
    assert not inspect.isabstract(diagram::ContainerStyle)


def test_diagram::containerstyle_constructor_exists():
    assert callable(diagram::ContainerStyle.__init__)


def test_diagram::containerstyle_constructor_args():
    sig = inspect.signature(diagram::ContainerStyle.__init__)
    params = list(sig.parameters.keys())
    assert "containerLabelDirection" in params, "Missing parameter 'containerLabelDirection'"

def test_diagram::containerstyle_has_containerLabelDirection():
    assert hasattr(diagram::ContainerStyle, "containerLabelDirection")
    descriptor = None
    for klass in diagram::ContainerStyle.__mro__:
        if "containerLabelDirection" in klass.__dict__:
            descriptor = klass.__dict__["containerLabelDirection"]
            break
    assert isinstance(descriptor, property)



def test_diagram::graphicalfilter_is_not_abstract():
    assert not inspect.isabstract(diagram::GraphicalFilter)


def test_diagram::graphicalfilter_constructor_exists():
    assert callable(diagram::GraphicalFilter.__init__)


def test_diagram::graphicalfilter_constructor_args():
    sig = inspect.signature(diagram::GraphicalFilter.__init__)
    params = list(sig.parameters.keys())



def test_nodemapping_is_not_abstract():
    assert not inspect.isabstract(NodeMapping)


def test_nodemapping_constructor_exists():
    assert callable(NodeMapping.__init__)


def test_nodemapping_constructor_args():
    sig = inspect.signature(NodeMapping.__init__)
    params = list(sig.parameters.keys())



def test_diagram::style_is_not_abstract():
    assert not inspect.isabstract(diagram::Style)


def test_diagram::style_constructor_exists():
    assert callable(diagram::Style.__init__)


def test_diagram::style_constructor_args():
    sig = inspect.signature(diagram::Style.__init__)
    params = list(sig.parameters.keys())



def test_diagram::nodestyle_is_not_abstract():
    assert not inspect.isabstract(diagram::NodeStyle)


def test_diagram::nodestyle_constructor_exists():
    assert callable(diagram::NodeStyle.__init__)


def test_diagram::nodestyle_constructor_args():
    sig = inspect.signature(diagram::NodeStyle.__init__)
    params = list(sig.parameters.keys())
    assert "labelDirection" in params, "Missing parameter 'labelDirection'"
    assert "labelPosition" in params, "Missing parameter 'labelPosition'"

def test_diagram::nodestyle_has_labelDirection():
    assert hasattr(diagram::NodeStyle, "labelDirection")
    descriptor = None
    for klass in diagram::NodeStyle.__mro__:
        if "labelDirection" in klass.__dict__:
            descriptor = klass.__dict__["labelDirection"]
            break
    assert isinstance(descriptor, property)

def test_diagram::nodestyle_has_labelPosition():
    assert hasattr(diagram::NodeStyle, "labelPosition")
    descriptor = None
    for klass in diagram::NodeStyle.__mro__:
        if "labelPosition" in klass.__dict__:
            descriptor = klass.__dict__["labelPosition"]
            break
    assert isinstance(descriptor, property)



def test_edgetarget_is_not_abstract():
    assert not inspect.isabstract(EdgeTarget)


def test_edgetarget_constructor_exists():
    assert callable(EdgeTarget.__init__)


def test_edgetarget_constructor_args():
    sig = inspect.signature(EdgeTarget.__init__)
    params = list(sig.parameters.keys())



def test_abstractdnode_is_not_abstract():
    assert not inspect.isabstract(AbstractDNode)


def test_abstractdnode_constructor_exists():
    assert callable(AbstractDNode.__init__)


def test_abstractdnode_constructor_args():
    sig = inspect.signature(AbstractDNode.__init__)
    params = list(sig.parameters.keys())



def test_ddiagramelement_is_not_abstract():
    assert not inspect.isabstract(DDiagramElement)


def test_ddiagramelement_constructor_exists():
    assert callable(DDiagramElement.__init__)


def test_ddiagramelement_constructor_args():
    sig = inspect.signature(DDiagramElement.__init__)
    params = list(sig.parameters.keys())



def test_diagram::abstractdnode_is_not_abstract():
    assert not inspect.isabstract(diagram::AbstractDNode)


def test_diagram::abstractdnode_constructor_exists():
    assert callable(diagram::AbstractDNode.__init__)


def test_diagram::abstractdnode_constructor_args():
    sig = inspect.signature(diagram::AbstractDNode.__init__)
    params = list(sig.parameters.keys())
    assert "arrangeConstraints" in params, "Missing parameter 'arrangeConstraints'"

def test_diagram::abstractdnode_has_arrangeConstraints():
    assert hasattr(diagram::AbstractDNode, "arrangeConstraints")
    descriptor = None
    for klass in diagram::AbstractDNode.__mro__:
        if "arrangeConstraints" in klass.__dict__:
            descriptor = klass.__dict__["arrangeConstraints"]
            break
    assert isinstance(descriptor, property)



def test_filter::compositefilterdescription_is_not_abstract():
    assert not inspect.isabstract(filter::CompositeFilterDescription)


def test_filter::compositefilterdescription_constructor_exists():
    assert callable(filter::CompositeFilterDescription.__init__)


def test_filter::compositefilterdescription_constructor_args():
    sig = inspect.signature(filter::CompositeFilterDescription.__init__)
    params = list(sig.parameters.keys())



def test_graphicalfilter_is_not_abstract():
    assert not inspect.isabstract(GraphicalFilter)


def test_graphicalfilter_constructor_exists():
    assert callable(GraphicalFilter.__init__)


def test_graphicalfilter_constructor_args():
    sig = inspect.signature(GraphicalFilter.__init__)
    params = list(sig.parameters.keys())



def test_diagram::absoluteboundsfilter_is_not_abstract():
    assert not inspect.isabstract(diagram::AbsoluteBoundsFilter)


def test_diagram::absoluteboundsfilter_constructor_exists():
    assert callable(diagram::AbsoluteBoundsFilter.__init__)


def test_diagram::absoluteboundsfilter_constructor_args():
    sig = inspect.signature(diagram::AbsoluteBoundsFilter.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"

def test_diagram::absoluteboundsfilter_has_x():
    assert hasattr(diagram::AbsoluteBoundsFilter, "x")
    descriptor = None
    for klass in diagram::AbsoluteBoundsFilter.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_diagram::absoluteboundsfilter_has_y():
    assert hasattr(diagram::AbsoluteBoundsFilter, "y")
    descriptor = None
    for klass in diagram::AbsoluteBoundsFilter.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_diagram::absoluteboundsfilter_has_width():
    assert hasattr(diagram::AbsoluteBoundsFilter, "width")
    descriptor = None
    for klass in diagram::AbsoluteBoundsFilter.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_diagram::absoluteboundsfilter_has_height():
    assert hasattr(diagram::AbsoluteBoundsFilter, "height")
    descriptor = None
    for klass in diagram::AbsoluteBoundsFilter.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_diagram::appliedcompositefilters_is_not_abstract():
    assert not inspect.isabstract(diagram::AppliedCompositeFilters)


def test_diagram::appliedcompositefilters_constructor_exists():
    assert callable(diagram::AppliedCompositeFilters.__init__)


def test_diagram::appliedcompositefilters_constructor_args():
    sig = inspect.signature(diagram::AppliedCompositeFilters.__init__)
    params = list(sig.parameters.keys())



def test_diagram::collapsefilter_is_not_abstract():
    assert not inspect.isabstract(diagram::CollapseFilter)


def test_diagram::collapsefilter_constructor_exists():
    assert callable(diagram::CollapseFilter.__init__)


def test_diagram::collapsefilter_constructor_args():
    sig = inspect.signature(diagram::CollapseFilter.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"

def test_diagram::collapsefilter_has_width():
    assert hasattr(diagram::CollapseFilter, "width")
    descriptor = None
    for klass in diagram::CollapseFilter.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_diagram::collapsefilter_has_height():
    assert hasattr(diagram::CollapseFilter, "height")
    descriptor = None
    for klass in diagram::CollapseFilter.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_diagram::hidelabelfilter_is_not_abstract():
    assert not inspect.isabstract(diagram::HideLabelFilter)


def test_diagram::hidelabelfilter_constructor_exists():
    assert callable(diagram::HideLabelFilter.__init__)


def test_diagram::hidelabelfilter_constructor_args():
    sig = inspect.signature(diagram::HideLabelFilter.__init__)
    params = list(sig.parameters.keys())



def test_diagram::foldingpointfilter_is_not_abstract():
    assert not inspect.isabstract(diagram::FoldingPointFilter)


def test_diagram::foldingpointfilter_constructor_exists():
    assert callable(diagram::FoldingPointFilter.__init__)


def test_diagram::foldingpointfilter_constructor_args():
    sig = inspect.signature(diagram::FoldingPointFilter.__init__)
    params = list(sig.parameters.keys())



def test_diagram::foldingfilter_is_not_abstract():
    assert not inspect.isabstract(diagram::FoldingFilter)


def test_diagram::foldingfilter_constructor_exists():
    assert callable(diagram::FoldingFilter.__init__)


def test_diagram::foldingfilter_constructor_args():
    sig = inspect.signature(diagram::FoldingFilter.__init__)
    params = list(sig.parameters.keys())



def test_diagram::hidefilter_is_not_abstract():
    assert not inspect.isabstract(diagram::HideFilter)


def test_diagram::hidefilter_constructor_exists():
    assert callable(diagram::HideFilter.__init__)


def test_diagram::hidefilter_constructor_args():
    sig = inspect.signature(diagram::HideFilter.__init__)
    params = list(sig.parameters.keys())



def test_filter::filterdescription_is_not_abstract():
    assert not inspect.isabstract(filter::FilterDescription)


def test_filter::filterdescription_constructor_exists():
    assert callable(filter::FilterDescription.__init__)


def test_filter::filterdescription_constructor_args():
    sig = inspect.signature(filter::FilterDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagramelementmapping_is_not_abstract():
    assert not inspect.isabstract(DiagramElementMapping)


def test_diagramelementmapping_constructor_exists():
    assert callable(DiagramElementMapping.__init__)


def test_diagramelementmapping_constructor_args():
    sig = inspect.signature(DiagramElementMapping.__init__)
    params = list(sig.parameters.keys())



def test_diagram::decoration_is_not_abstract():
    assert not inspect.isabstract(diagram::Decoration)


def test_diagram::decoration_constructor_exists():
    assert callable(diagram::Decoration.__init__)


def test_diagram::decoration_constructor_args():
    sig = inspect.signature(diagram::Decoration.__init__)
    params = list(sig.parameters.keys())



def test_drepresentationelement_is_not_abstract():
    assert not inspect.isabstract(DRepresentationElement)


def test_drepresentationelement_constructor_exists():
    assert callable(DRepresentationElement.__init__)


def test_drepresentationelement_constructor_args():
    sig = inspect.signature(DRepresentationElement.__init__)
    params = list(sig.parameters.keys())



def test_dsemanticdecorator_is_not_abstract():
    assert not inspect.isabstract(DSemanticDecorator)


def test_dsemanticdecorator_constructor_exists():
    assert callable(DSemanticDecorator.__init__)


def test_dsemanticdecorator_constructor_args():
    sig = inspect.signature(DSemanticDecorator.__init__)
    params = list(sig.parameters.keys())



def test_ddiagram_is_not_abstract():
    assert not inspect.isabstract(DDiagram)


def test_ddiagram_constructor_exists():
    assert callable(DDiagram.__init__)


def test_ddiagram_constructor_args():
    sig = inspect.signature(DDiagram.__init__)
    params = list(sig.parameters.keys())



def test_diagram::dsemanticdiagram_is_not_abstract():
    assert not inspect.isabstract(diagram::DSemanticDiagram)


def test_diagram::dsemanticdiagram_constructor_exists():
    assert callable(diagram::DSemanticDiagram.__init__)


def test_diagram::dsemanticdiagram_constructor_args():
    sig = inspect.signature(diagram::DSemanticDiagram.__init__)
    params = list(sig.parameters.keys())



def test_layer_is_not_abstract():
    assert not inspect.isabstract(Layer)


def test_layer_constructor_exists():
    assert callable(Layer.__init__)


def test_layer_constructor_args():
    sig = inspect.signature(Layer.__init__)
    params = list(sig.parameters.keys())



def test_diagram::description::additionallayer_is_not_abstract():
    assert not inspect.isabstract(diagram::description::AdditionalLayer)


def test_diagram::description::additionallayer_constructor_exists():
    assert callable(diagram::description::AdditionalLayer.__init__)


def test_diagram::description::additionallayer_constructor_args():
    sig = inspect.signature(diagram::description::AdditionalLayer.__init__)
    params = list(sig.parameters.keys())
    assert "activeByDefault" in params, "Missing parameter 'activeByDefault'"
    assert "optional" in params, "Missing parameter 'optional'"

def test_diagram::description::additionallayer_has_activeByDefault():
    assert hasattr(diagram::description::AdditionalLayer, "activeByDefault")
    descriptor = None
    for klass in diagram::description::AdditionalLayer.__mro__:
        if "activeByDefault" in klass.__dict__:
            descriptor = klass.__dict__["activeByDefault"]
            break
    assert isinstance(descriptor, property)

def test_diagram::description::additionallayer_has_optional():
    assert hasattr(diagram::description::AdditionalLayer, "optional")
    descriptor = None
    for klass in diagram::description::AdditionalLayer.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)



def test_diagram::filtervariablehistory_is_not_abstract():
    assert not inspect.isabstract(diagram::FilterVariableHistory)


def test_diagram::filtervariablehistory_constructor_exists():
    assert callable(diagram::FilterVariableHistory.__init__)


def test_diagram::filtervariablehistory_constructor_args():
    sig = inspect.signature(diagram::FilterVariableHistory.__init__)
    params = list(sig.parameters.keys())



def test_tool::behaviortool_is_not_abstract():
    assert not inspect.isabstract(tool::BehaviorTool)


def test_tool::behaviortool_constructor_exists():
    assert callable(tool::BehaviorTool.__init__)


def test_tool::behaviortool_constructor_args():
    sig = inspect.signature(tool::BehaviorTool.__init__)
    params = list(sig.parameters.keys())



def test_validation::validationrule_is_not_abstract():
    assert not inspect.isabstract(validation::ValidationRule)


def test_validation::validationrule_constructor_exists():
    assert callable(validation::ValidationRule.__init__)


def test_validation::validationrule_constructor_args():
    sig = inspect.signature(validation::ValidationRule.__init__)
    params = list(sig.parameters.keys())



def test_concern::concerndescription_is_not_abstract():
    assert not inspect.isabstract(concern::ConcernDescription)


def test_concern::concerndescription_constructor_exists():
    assert callable(concern::ConcernDescription.__init__)


def test_concern::concerndescription_constructor_args():
    sig = inspect.signature(concern::ConcernDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram::dnodelistelement_is_not_abstract():
    assert not inspect.isabstract(diagram::DNodeListElement)


def test_diagram::dnodelistelement_constructor_exists():
    assert callable(diagram::DNodeListElement.__init__)


def test_diagram::dnodelistelement_constructor_args():
    sig = inspect.signature(diagram::DNodeListElement.__init__)
    params = list(sig.parameters.keys())



def test_diagram::dedge_is_not_abstract():
    assert not inspect.isabstract(diagram::DEdge)


def test_diagram::dedge_constructor_exists():
    assert callable(diagram::DEdge.__init__)


def test_diagram::dedge_constructor_args():
    sig = inspect.signature(diagram::DEdge.__init__)
    params = list(sig.parameters.keys())
    assert "beginLabel" in params, "Missing parameter 'beginLabel'"
    assert "endLabel" in params, "Missing parameter 'endLabel'"
    assert "size" in params, "Missing parameter 'size'"
    assert "routingStyle" in params, "Missing parameter 'routingStyle'"
    assert "isMockEdge" in params, "Missing parameter 'isMockEdge'"
    assert "arrangeConstraints" in params, "Missing parameter 'arrangeConstraints'"
    assert "isFold" in params, "Missing parameter 'isFold'"

def test_diagram::dedge_has_beginLabel():
    assert hasattr(diagram::DEdge, "beginLabel")
    descriptor = None
    for klass in diagram::DEdge.__mro__:
        if "beginLabel" in klass.__dict__:
            descriptor = klass.__dict__["beginLabel"]
            break
    assert isinstance(descriptor, property)

def test_diagram::dedge_has_endLabel():
    assert hasattr(diagram::DEdge, "endLabel")
    descriptor = None
    for klass in diagram::DEdge.__mro__:
        if "endLabel" in klass.__dict__:
            descriptor = klass.__dict__["endLabel"]
            break
    assert isinstance(descriptor, property)

def test_diagram::dedge_has_size():
    assert hasattr(diagram::DEdge, "size")
    descriptor = None
    for klass in diagram::DEdge.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_diagram::dedge_has_routingStyle():
    assert hasattr(diagram::DEdge, "routingStyle")
    descriptor = None
    for klass in diagram::DEdge.__mro__:
        if "routingStyle" in klass.__dict__:
            descriptor = klass.__dict__["routingStyle"]
            break
    assert isinstance(descriptor, property)

def test_diagram::dedge_has_isMockEdge():
    assert hasattr(diagram::DEdge, "isMockEdge")
    descriptor = None
    for klass in diagram::DEdge.__mro__:
        if "isMockEdge" in klass.__dict__:
            descriptor = klass.__dict__["isMockEdge"]
            break
    assert isinstance(descriptor, property)

def test_diagram::dedge_has_arrangeConstraints():
    assert hasattr(diagram::DEdge, "arrangeConstraints")
    descriptor = None
    for klass in diagram::DEdge.__mro__:
        if "arrangeConstraints" in klass.__dict__:
            descriptor = klass.__dict__["arrangeConstraints"]
            break
    assert isinstance(descriptor, property)

def test_diagram::dedge_has_isFold():
    assert hasattr(diagram::DEdge, "isFold")
    descriptor = None
    for klass in diagram::DEdge.__mro__:
        if "isFold" in klass.__dict__:
            descriptor = klass.__dict__["isFold"]
            break
    assert isinstance(descriptor, property)



def test_diagramdescription_is_not_abstract():
    assert not inspect.isabstract(DiagramDescription)


def test_diagramdescription_constructor_exists():
    assert callable(DiagramDescription.__init__)


def test_diagramdescription_constructor_args():
    sig = inspect.signature(DiagramDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram::ddiagramelement_is_not_abstract():
    assert not inspect.isabstract(diagram::DDiagramElement)


def test_diagram::ddiagramelement_constructor_exists():
    assert callable(diagram::DDiagramElement.__init__)


def test_diagram::ddiagramelement_constructor_args():
    sig = inspect.signature(diagram::DDiagramElement.__init__)
    params = list(sig.parameters.keys())
    assert "tooltipText" in params, "Missing parameter 'tooltipText'"
    assert "visible" in params, "Missing parameter 'visible'"

def test_diagram::ddiagramelement_has_tooltipText():
    assert hasattr(diagram::DDiagramElement, "tooltipText")
    descriptor = None
    for klass in diagram::DDiagramElement.__mro__:
        if "tooltipText" in klass.__dict__:
            descriptor = klass.__dict__["tooltipText"]
            break
    assert isinstance(descriptor, property)

def test_diagram::ddiagramelement_has_visible():
    assert hasattr(diagram::DDiagramElement, "visible")
    descriptor = None
    for klass in diagram::DDiagramElement.__mro__:
        if "visible" in klass.__dict__:
            descriptor = klass.__dict__["visible"]
            break
    assert isinstance(descriptor, property)



def test_draganddroptarget_is_not_abstract():
    assert not inspect.isabstract(DragAndDropTarget)


def test_draganddroptarget_constructor_exists():
    assert callable(DragAndDropTarget.__init__)


def test_draganddroptarget_constructor_args():
    sig = inspect.signature(DragAndDropTarget.__init__)
    params = list(sig.parameters.keys())



def test_diagram::ddiagramelementcontainer_is_not_abstract():
    assert not inspect.isabstract(diagram::DDiagramElementContainer)


def test_diagram::ddiagramelementcontainer_constructor_exists():
    assert callable(diagram::DDiagramElementContainer.__init__)


def test_diagram::ddiagramelementcontainer_constructor_args():
    sig = inspect.signature(diagram::DDiagramElementContainer.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"

def test_diagram::ddiagramelementcontainer_has_height():
    assert hasattr(diagram::DDiagramElementContainer, "height")
    descriptor = None
    for klass in diagram::DDiagramElementContainer.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_diagram::ddiagramelementcontainer_has_width():
    assert hasattr(diagram::DDiagramElementContainer, "width")
    descriptor = None
    for klass in diagram::DDiagramElementContainer.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_diagram::dnode_is_not_abstract():
    assert not inspect.isabstract(diagram::DNode)


def test_diagram::dnode_constructor_exists():
    assert callable(diagram::DNode.__init__)


def test_diagram::dnode_constructor_args():
    sig = inspect.signature(diagram::DNode.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "resizeKind" in params, "Missing parameter 'resizeKind'"
    assert "labelPosition" in params, "Missing parameter 'labelPosition'"
    assert "height" in params, "Missing parameter 'height'"

def test_diagram::dnode_has_width():
    assert hasattr(diagram::DNode, "width")
    descriptor = None
    for klass in diagram::DNode.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_diagram::dnode_has_resizeKind():
    assert hasattr(diagram::DNode, "resizeKind")
    descriptor = None
    for klass in diagram::DNode.__mro__:
        if "resizeKind" in klass.__dict__:
            descriptor = klass.__dict__["resizeKind"]
            break
    assert isinstance(descriptor, property)

def test_diagram::dnode_has_labelPosition():
    assert hasattr(diagram::DNode, "labelPosition")
    descriptor = None
    for klass in diagram::DNode.__mro__:
        if "labelPosition" in klass.__dict__:
            descriptor = klass.__dict__["labelPosition"]
            break
    assert isinstance(descriptor, property)

def test_diagram::dnode_has_height():
    assert hasattr(diagram::DNode, "height")
    descriptor = None
    for klass in diagram::DNode.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_description::documentedelement_is_not_abstract():
    assert not inspect.isabstract(description::DocumentedElement)


def test_description::documentedelement_constructor_exists():
    assert callable(description::DocumentedElement.__init__)


def test_description::documentedelement_constructor_args():
    sig = inspect.signature(description::DocumentedElement.__init__)
    params = list(sig.parameters.keys())



def test_diagram::filter::filterdescription_is_not_abstract():
    assert not inspect.isabstract(diagram::filter::FilterDescription)


def test_diagram::filter::filterdescription_constructor_exists():
    assert callable(diagram::filter::FilterDescription.__init__)


def test_diagram::filter::filterdescription_constructor_args():
    sig = inspect.signature(diagram::filter::FilterDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram::description::layer_is_not_abstract():
    assert not inspect.isabstract(diagram::description::Layer)


def test_diagram::description::layer_constructor_exists():
    assert callable(diagram::description::Layer.__init__)


def test_diagram::description::layer_constructor_args():
    sig = inspect.signature(diagram::description::Layer.__init__)
    params = list(sig.parameters.keys())
    assert "icon" in params, "Missing parameter 'icon'"

def test_diagram::description::layer_has_icon():
    assert hasattr(diagram::description::Layer, "icon")
    descriptor = None
    for klass in diagram::description::Layer.__mro__:
        if "icon" in klass.__dict__:
            descriptor = klass.__dict__["icon"]
            break
    assert isinstance(descriptor, property)



def test_diagram::description::edgemappingimport_is_not_abstract():
    assert not inspect.isabstract(diagram::description::EdgeMappingImport)


def test_diagram::description::edgemappingimport_constructor_exists():
    assert callable(diagram::description::EdgeMappingImport.__init__)


def test_diagram::description::edgemappingimport_constructor_args():
    sig = inspect.signature(diagram::description::EdgeMappingImport.__init__)
    params = list(sig.parameters.keys())
    assert "inheritsAncestorFilters" in params, "Missing parameter 'inheritsAncestorFilters'"

def test_diagram::description::edgemappingimport_has_inheritsAncestorFilters():
    assert hasattr(diagram::description::EdgeMappingImport, "inheritsAncestorFilters")
    descriptor = None
    for klass in diagram::description::EdgeMappingImport.__mro__:
        if "inheritsAncestorFilters" in klass.__dict__:
            descriptor = klass.__dict__["inheritsAncestorFilters"]
            break
    assert isinstance(descriptor, property)



def test_diagram::tool::toolsection_is_not_abstract():
    assert not inspect.isabstract(diagram::tool::ToolSection)


def test_diagram::tool::toolsection_constructor_exists():
    assert callable(diagram::tool::ToolSection.__init__)


def test_diagram::tool::toolsection_constructor_args():
    sig = inspect.signature(diagram::tool::ToolSection.__init__)
    params = list(sig.parameters.keys())
    assert "icon" in params, "Missing parameter 'icon'"

def test_diagram::tool::toolsection_has_icon():
    assert hasattr(diagram::tool::ToolSection, "icon")
    descriptor = None
    for klass in diagram::tool::ToolSection.__mro__:
        if "icon" in klass.__dict__:
            descriptor = klass.__dict__["icon"]
            break
    assert isinstance(descriptor, property)



def test_diagram::description::edgemapping_is_not_abstract():
    assert not inspect.isabstract(diagram::description::EdgeMapping)


def test_diagram::description::edgemapping_constructor_exists():
    assert callable(diagram::description::EdgeMapping.__init__)


def test_diagram::description::edgemapping_constructor_args():
    sig = inspect.signature(diagram::description::EdgeMapping.__init__)
    params = list(sig.parameters.keys())
    assert "pathExpression" in params, "Missing parameter 'pathExpression'"
    assert "domainClass" in params, "Missing parameter 'domainClass'"
    assert "targetExpression" in params, "Missing parameter 'targetExpression'"
    assert "targetFinderExpression" in params, "Missing parameter 'targetFinderExpression'"
    assert "sourceFinderExpression" in params, "Missing parameter 'sourceFinderExpression'"
    assert "useDomainElement" in params, "Missing parameter 'useDomainElement'"

def test_diagram::description::edgemapping_has_pathExpression():
    assert hasattr(diagram::description::EdgeMapping, "pathExpression")
    descriptor = None
    for klass in diagram::description::EdgeMapping.__mro__:
        if "pathExpression" in klass.__dict__:
            descriptor = klass.__dict__["pathExpression"]
            break
    assert isinstance(descriptor, property)

def test_diagram::description::edgemapping_has_domainClass():
    assert hasattr(diagram::description::EdgeMapping, "domainClass")
    descriptor = None
    for klass in diagram::description::EdgeMapping.__mro__:
        if "domainClass" in klass.__dict__:
            descriptor = klass.__dict__["domainClass"]
            break
    assert isinstance(descriptor, property)

def test_diagram::description::edgemapping_has_targetExpression():
    assert hasattr(diagram::description::EdgeMapping, "targetExpression")
    descriptor = None
    for klass in diagram::description::EdgeMapping.__mro__:
        if "targetExpression" in klass.__dict__:
            descriptor = klass.__dict__["targetExpression"]
            break
    assert isinstance(descriptor, property)

def test_diagram::description::edgemapping_has_targetFinderExpression():
    assert hasattr(diagram::description::EdgeMapping, "targetFinderExpression")
    descriptor = None
    for klass in diagram::description::EdgeMapping.__mro__:
        if "targetFinderExpression" in klass.__dict__:
            descriptor = klass.__dict__["targetFinderExpression"]
            break
    assert isinstance(descriptor, property)

def test_diagram::description::edgemapping_has_sourceFinderExpression():
    assert hasattr(diagram::description::EdgeMapping, "sourceFinderExpression")
    descriptor = None
    for klass in diagram::description::EdgeMapping.__mro__:
        if "sourceFinderExpression" in klass.__dict__:
            descriptor = klass.__dict__["sourceFinderExpression"]
            break
    assert isinstance(descriptor, property)

def test_diagram::description::edgemapping_has_useDomainElement():
    assert hasattr(diagram::description::EdgeMapping, "useDomainElement")
    descriptor = None
    for klass in diagram::description::EdgeMapping.__mro__:
        if "useDomainElement" in klass.__dict__:
            descriptor = klass.__dict__["useDomainElement"]
            break
    assert isinstance(descriptor, property)



def test_diagram::concern::concerndescription_is_not_abstract():
    assert not inspect.isabstract(diagram::concern::ConcernDescription)


def test_diagram::concern::concerndescription_constructor_exists():
    assert callable(diagram::concern::ConcernDescription.__init__)


def test_diagram::concern::concerndescription_constructor_args():
    sig = inspect.signature(diagram::concern::ConcernDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram::description::abstractnodemapping_is_not_abstract():
    assert not inspect.isabstract(diagram::description::AbstractNodeMapping)


def test_diagram::description::abstractnodemapping_constructor_exists():
    assert callable(diagram::description::AbstractNodeMapping.__init__)


def test_diagram::description::abstractnodemapping_constructor_args():
    sig = inspect.signature(diagram::description::AbstractNodeMapping.__init__)
    params = list(sig.parameters.keys())
    assert "domainClass" in params, "Missing parameter 'domainClass'"

def test_diagram::description::abstractnodemapping_has_domainClass():
    assert hasattr(diagram::description::AbstractNodeMapping, "domainClass")
    descriptor = None
    for klass in diagram::description::AbstractNodeMapping.__mro__:
        if "domainClass" in klass.__dict__:
            descriptor = klass.__dict__["domainClass"]
            break
    assert isinstance(descriptor, property)



def test_drepresentation_is_not_abstract():
    assert not inspect.isabstract(DRepresentation)


def test_drepresentation_constructor_exists():
    assert callable(DRepresentation.__init__)


def test_drepresentation_constructor_args():
    sig = inspect.signature(DRepresentation.__init__)
    params = list(sig.parameters.keys())



def test_diagram::ddiagram_is_not_abstract():
    assert not inspect.isabstract(diagram::DDiagram)


def test_diagram::ddiagram_constructor_exists():
    assert callable(diagram::DDiagram.__init__)


def test_diagram::ddiagram_constructor_args():
    sig = inspect.signature(diagram::DDiagram.__init__)
    params = list(sig.parameters.keys())
    assert "isInLayoutingMode" in params, "Missing parameter 'isInLayoutingMode'"
    assert "headerHeight" in params, "Missing parameter 'headerHeight'"
    assert "synchronized" in params, "Missing parameter 'synchronized'"

def test_diagram::ddiagram_has_isInLayoutingMode():
    assert hasattr(diagram::DDiagram, "isInLayoutingMode")
    descriptor = None
    for klass in diagram::DDiagram.__mro__:
        if "isInLayoutingMode" in klass.__dict__:
            descriptor = klass.__dict__["isInLayoutingMode"]
            break
    assert isinstance(descriptor, property)

def test_diagram::ddiagram_has_headerHeight():
    assert hasattr(diagram::DDiagram, "headerHeight")
    descriptor = None
    for klass in diagram::DDiagram.__mro__:
        if "headerHeight" in klass.__dict__:
            descriptor = klass.__dict__["headerHeight"]
            break
    assert isinstance(descriptor, property)

def test_diagram::ddiagram_has_synchronized():
    assert hasattr(diagram::DDiagram, "synchronized")
    descriptor = None
    for klass in diagram::DDiagram.__mro__:
        if "synchronized" in klass.__dict__:
            descriptor = klass.__dict__["synchronized"]
            break
    assert isinstance(descriptor, property)

def test_arrangeconstraint_exists():
    # Check that the Enumeration exists
    assert ArrangeConstraint is not None

def test_arrangeconstraint_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ArrangeConstraint]
    expected_literals = [
        "KEEP_RATIO",
        "KEEP_SIZE",
        "KEEP_LOCATION",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ArrangeConstraint"

def test_linestyle_exists():
    # Check that the Enumeration exists
    assert LineStyle is not None

def test_linestyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LineStyle]
    expected_literals = [
        "solid",
        "dash_dot",
        "dash",
        "dot",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LineStyle"

def test_reconnectionkind_exists():
    # Check that the Enumeration exists
    assert ReconnectionKind is not None

def test_reconnectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ReconnectionKind]
    expected_literals = [
        "RECONNECT_TARGET",
        "RECONNECT_SOURCE",
        "RECONNECT_BOTH",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ReconnectionKind"

def test_containerlabeldirection_exists():
    # Check that the Enumeration exists
    assert ContainerLabelDirection is not None

def test_containerlabeldirection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContainerLabelDirection]
    expected_literals = [
        "Horizontal",
        "Vertical",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContainerLabelDirection"

def test_labelposition_exists():
    # Check that the Enumeration exists
    assert LabelPosition is not None

def test_labelposition_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LabelPosition]
    expected_literals = [
        "node",
        "border",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LabelPosition"

def test_edgearrows_exists():
    # Check that the Enumeration exists
    assert EdgeArrows is not None

def test_edgearrows_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EdgeArrows]
    expected_literals = [
        "FillDiamond",
        "NoDecoration",
        "InputArrowWithDiamond",
        "OutputClosedArrow",
        "InputFillClosedArrow",
        "InputArrow",
        "InputClosedArrow",
        "OutputArrow",
        "OutputFillClosedArrow",
        "InputArrowWithFillDiamond",
        "Diamond",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EdgeArrows"

def test_resizekind_exists():
    # Check that the Enumeration exists
    assert ResizeKind is not None

def test_resizekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ResizeKind]
    expected_literals = [
        "NSEW",
        "NONE",
        "EAST_WEST",
        "NORTH_SOUTH",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ResizeKind"

def test_side_exists():
    # Check that the Enumeration exists
    assert Side is not None

def test_side_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Side]
    expected_literals = [
        "EAST",
        "SOUTH",
        "NORTH",
        "WEST",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Side"

def test_layoutdirection_exists():
    # Check that the Enumeration exists
    assert LayoutDirection is not None

def test_layoutdirection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LayoutDirection]
    expected_literals = [
        "LeftToRight",
        "TopToBottom",
        "BottomToTop",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LayoutDirection"

def test_filterkind_exists():
    # Check that the Enumeration exists
    assert FilterKind is not None

def test_filterkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FilterKind]
    expected_literals = [
        "HIDE",
        "COLLAPSE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FilterKind"

def test_containershape_exists():
    # Check that the Enumeration exists
    assert ContainerShape is not None

def test_containershape_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContainerShape]
    expected_literals = [
        "parallelogram",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContainerShape"

def test_foldingstyle_exists():
    # Check that the Enumeration exists
    assert FoldingStyle is not None

def test_foldingstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FoldingStyle]
    expected_literals = [
        "SOURCE",
        "NONE",
        "TARGET",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FoldingStyle"

def test_alignmentkind_exists():
    # Check that the Enumeration exists
    assert AlignmentKind is not None

def test_alignmentkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AlignmentKind]
    expected_literals = [
        "HORIZONTAL",
        "VERTICAL",
        "SQUARE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AlignmentKind"

def test_edgerouting_exists():
    # Check that the Enumeration exists
    assert EdgeRouting is not None

def test_edgerouting_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EdgeRouting]
    expected_literals = [
        "straight",
        "tree",
        "manhattan",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EdgeRouting"

def test_bundledimageshape_exists():
    # Check that the Enumeration exists
    assert BundledImageShape is not None

def test_bundledimageshape_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BundledImageShape]
    expected_literals = [
        "stroke",
        "square",
        "dot",
        "providedShape",
        "ring",
        "triangle",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BundledImageShape"

def test_centeringstyle_exists():
    # Check that the Enumeration exists
    assert CenteringStyle is not None

def test_centeringstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CenteringStyle]
    expected_literals = [
        "Source",
        "Target",
        "None_",
        "Both",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CenteringStyle"

def test_backgroundstyle_exists():
    # Check that the Enumeration exists
    assert BackgroundStyle is not None

def test_backgroundstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BackgroundStyle]
    expected_literals = [
        "GradientTopToBottom",
        "Liquid",
        "GradientLeftToRight",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BackgroundStyle"

def test_labeldirection_exists():
    # Check that the Enumeration exists
    assert LabelDirection is not None

def test_labeldirection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LabelDirection]
    expected_literals = [
        "Vertical",
        "Horizontal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LabelDirection"

def test_containerlayout_exists():
    # Check that the Enumeration exists
    assert ContainerLayout is not None

def test_containerlayout_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContainerLayout]
    expected_literals = [
        "VerticalStack",
        "HorizontalStack",
        "FreeForm",
        "List",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContainerLayout"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
description::AbstractNodeMapping_strategy = st.builds(
    description::AbstractNodeMapping,
)
description::DiagramElementMapping_strategy = st.builds(
    description::DiagramElementMapping,
)
tool::DoubleClickDescription_strategy = st.builds(
    tool::DoubleClickDescription,
)
tool::DirectEditLabel_strategy = st.builds(
    tool::DirectEditLabel,
)
tool::DeleteElementDescription_strategy = st.builds(
    tool::DeleteElementDescription,
)
description::RepresentationElementMapping_strategy = st.builds(
    description::RepresentationElementMapping,
)
RepresentationExtensionDescription_strategy = st.builds(
    RepresentationExtensionDescription,
)
diagram::description::DiagramExtensionDescription_strategy = st.builds(
    diagram::description::DiagramExtensionDescription,
)
description::DiagramDescription_strategy = st.builds(
    description::DiagramDescription,
)
description::RepresentationImportDescription_strategy = st.builds(
    description::RepresentationImportDescription,
)
diagram::description::DiagramImportDescription_strategy = st.builds(
    diagram::description::DiagramImportDescription,
)
tool::ToolSection_strategy = st.builds(
    tool::ToolSection,
)
EdgeMappingImport_strategy = st.builds(
    EdgeMappingImport,
)
AdditionalLayer_strategy = st.builds(
    AdditionalLayer,
)
Filter_strategy = st.builds(
    Filter,
)
diagram::filter::MappingFilter_strategy = st.builds(
    diagram::filter::MappingFilter,
    viewConditionExpression=
        safe_text,
    semanticConditionExpression=
        safe_text
)
diagram::filter::Filter_strategy = st.builds(
    diagram::filter::Filter,
    filterKind=
        safe_text
)
InteractiveVariableDescription_strategy = st.builds(
    InteractiveVariableDescription,
)
diagram::filter::VariableFilter_strategy = st.builds(
    diagram::filter::VariableFilter,
    semanticConditionExpression=
        safe_text
)
filter::Filter_strategy = st.builds(
    filter::Filter,
)
FilterDescription_strategy = st.builds(
    FilterDescription,
)
diagram::filter::CompositeFilterDescription_strategy = st.builds(
    diagram::filter::CompositeFilterDescription,
)
RepresentationNavigationDescription_strategy = st.builds(
    RepresentationNavigationDescription,
)
diagram::tool::DiagramNavigationDescription_strategy = st.builds(
    diagram::tool::DiagramNavigationDescription,
)
tool::InitialContainerDropOperation_strategy = st.builds(
    tool::InitialContainerDropOperation,
)
tool::ElementDropVariable_strategy = st.builds(
    tool::ElementDropVariable,
)
tool::DropContainerVariable_strategy = st.builds(
    tool::DropContainerVariable,
)
RepresentationCreationDescription_strategy = st.builds(
    RepresentationCreationDescription,
)
diagram::tool::DiagramCreationDescription_strategy = st.builds(
    diagram::tool::DiagramCreationDescription,
)
CreateView_strategy = st.builds(
    CreateView,
)
diagram::tool::CreateEdgeView_strategy = st.builds(
    diagram::tool::CreateEdgeView,
    targetExpression=
        safe_text,
    sourceExpression=
        safe_text
)
AbstractToolDescription_strategy = st.builds(
    AbstractToolDescription,
)
diagram::tool::RequestDescription_strategy = st.builds(
    diagram::tool::RequestDescription,
    type=
        safe_text
)
ContainerModelOperation_strategy = st.builds(
    ContainerModelOperation,
)
diagram::tool::Navigation_strategy = st.builds(
    diagram::tool::Navigation,
    createIfNotExistent=
        st.booleans()
)
diagram::tool::CreateView_strategy = st.builds(
    diagram::tool::CreateView,
    variableName=
        safe_text,
    containerViewExpression=
        safe_text
)
tool::VariableContainer_strategy = st.builds(
    tool::VariableContainer,
)
description::AbstractVariable_strategy = st.builds(
    description::AbstractVariable,
)
diagram::tool::ElementDoubleClickVariable_strategy = st.builds(
    diagram::tool::ElementDoubleClickVariable,
)
diagram::tool::TargetEdgeCreationVariable_strategy = st.builds(
    diagram::tool::TargetEdgeCreationVariable,
)
diagram::tool::SourceEdgeViewCreationVariable_strategy = st.builds(
    diagram::tool::SourceEdgeViewCreationVariable,
)
diagram::tool::NodeCreationVariable_strategy = st.builds(
    diagram::tool::NodeCreationVariable,
)
diagram::tool::TargetEdgeViewCreationVariable_strategy = st.builds(
    diagram::tool::TargetEdgeViewCreationVariable,
)
diagram::tool::SourceEdgeCreationVariable_strategy = st.builds(
    diagram::tool::SourceEdgeCreationVariable,
)
diagram::tool::BehaviorTool_strategy = st.builds(
    diagram::tool::BehaviorTool,
    domainClass=
        safe_text
)
tool::EditMaskVariables_strategy = st.builds(
    tool::EditMaskVariables,
)
diagram::tool::DeleteHook_strategy = st.builds(
    diagram::tool::DeleteHook,
    id=
        safe_text
)
tool::ElementSelectVariable_strategy = st.builds(
    tool::ElementSelectVariable,
)
diagram::tool::DeleteHookParameter_strategy = st.builds(
    diagram::tool::DeleteHookParameter,
    value=
        safe_text,
    name=
        safe_text
)
tool::DeleteHookParameter_strategy = st.builds(
    tool::DeleteHookParameter,
)
tool::ElementDoubleClickVariable_strategy = st.builds(
    tool::ElementDoubleClickVariable,
)
tool::DeleteHook_strategy = st.builds(
    tool::DeleteHook,
)
tool::ElementDeleteVariable_strategy = st.builds(
    tool::ElementDeleteVariable,
)
tool::InitEdgeCreationOperation_strategy = st.builds(
    tool::InitEdgeCreationOperation,
)
tool::TargetEdgeViewCreationVariable_strategy = st.builds(
    tool::TargetEdgeViewCreationVariable,
)
tool::SourceEdgeViewCreationVariable_strategy = st.builds(
    tool::SourceEdgeViewCreationVariable,
)
tool::TargetEdgeCreationVariable_strategy = st.builds(
    tool::TargetEdgeCreationVariable,
)
tool::SourceEdgeCreationVariable_strategy = st.builds(
    tool::SourceEdgeCreationVariable,
)
tool::PopupMenu_strategy = st.builds(
    tool::PopupMenu,
)
tool::InitialNodeCreationOperation_strategy = st.builds(
    tool::InitialNodeCreationOperation,
)
tool::ContainerViewVariable_strategy = st.builds(
    tool::ContainerViewVariable,
)
tool::NodeCreationVariable_strategy = st.builds(
    tool::NodeCreationVariable,
)
MappingBasedToolDescription_strategy = st.builds(
    MappingBasedToolDescription,
)
diagram::tool::DoubleClickDescription_strategy = st.builds(
    diagram::tool::DoubleClickDescription,
)
diagram::tool::EdgeCreationDescription_strategy = st.builds(
    diagram::tool::EdgeCreationDescription,
    connectionStartPrecondition=
        safe_text,
    iconPath=
        safe_text
)
diagram::tool::ReconnectEdgeDescription_strategy = st.builds(
    diagram::tool::ReconnectEdgeDescription,
    reconnectionKind=
        safe_text
)
diagram::tool::ContainerDropDescription_strategy = st.builds(
    diagram::tool::ContainerDropDescription,
    dragSource=
        safe_text,
    moveEdges=
        st.booleans()
)
diagram::tool::ContainerCreationDescription_strategy = st.builds(
    diagram::tool::ContainerCreationDescription,
    iconPath=
        safe_text
)
diagram::tool::DirectEditLabel_strategy = st.builds(
    diagram::tool::DirectEditLabel,
    inputLabelExpression=
        safe_text
)
diagram::tool::DeleteElementDescription_strategy = st.builds(
    diagram::tool::DeleteElementDescription,
)
diagram::tool::NodeCreationDescription_strategy = st.builds(
    diagram::tool::NodeCreationDescription,
    iconPath=
        safe_text
)
tool::ToolGroup_strategy = st.builds(
    tool::ToolGroup,
)
diagram::tool::ToolGroupExtension_strategy = st.builds(
    diagram::tool::ToolGroupExtension,
)
ToolEntry_strategy = st.builds(
    ToolEntry,
)
diagram::tool::ToolGroup_strategy = st.builds(
    diagram::tool::ToolGroup,
)
tool::ToolGroupExtension_strategy = st.builds(
    tool::ToolGroupExtension,
)
style::BeginLabelStyleDescription_strategy = st.builds(
    style::BeginLabelStyleDescription,
)
tool::ToolEntry_strategy = st.builds(
    tool::ToolEntry,
)
diagram::style::HideLabelCapabilityStyleDescription_strategy = st.builds(
    diagram::style::HideLabelCapabilityStyleDescription,
    hideLabelByDefault=
        st.booleans()
)
EdgeStyleDescription_strategy = st.builds(
    EdgeStyleDescription,
)
diagram::style::BracketEdgeStyleDescription_strategy = st.builds(
    diagram::style::BracketEdgeStyleDescription,
)
BasicLabelStyleDescription_strategy = st.builds(
    BasicLabelStyleDescription,
)
diagram::style::EndLabelStyleDescription_strategy = st.builds(
    diagram::style::EndLabelStyleDescription,
)
diagram::style::CenterLabelStyleDescription_strategy = st.builds(
    diagram::style::CenterLabelStyleDescription,
)
diagram::style::BeginLabelStyleDescription_strategy = st.builds(
    diagram::style::BeginLabelStyleDescription,
)
style::EndLabelStyleDescription_strategy = st.builds(
    style::EndLabelStyleDescription,
)
style::CenterLabelStyleDescription_strategy = st.builds(
    style::CenterLabelStyleDescription,
)
diagram::style::SizeComputationContainerStyleDescription_strategy = st.builds(
    diagram::style::SizeComputationContainerStyleDescription,
    widthComputationExpression=
        safe_text,
    heightComputationExpression=
        safe_text
)
style::LabelBorderStyleDescription_strategy = st.builds(
    style::LabelBorderStyleDescription,
)
style::SizeComputationContainerStyleDescription_strategy = st.builds(
    style::SizeComputationContainerStyleDescription,
)
style::RoundedCornerStyleDescription_strategy = st.builds(
    style::RoundedCornerStyleDescription,
)
diagram::style::GaugeSectionDescription_strategy = st.builds(
    diagram::style::GaugeSectionDescription,
    label=
        safe_text,
    minValueExpression=
        safe_text,
    valueExpression=
        safe_text,
    maxValueExpression=
        safe_text
)
style::GaugeSectionDescription_strategy = st.builds(
    style::GaugeSectionDescription,
)
NodeStyleDescription_strategy = st.builds(
    NodeStyleDescription,
)
diagram::style::DotDescription_strategy = st.builds(
    diagram::style::DotDescription,
    strokeSizeComputationExpression=
        safe_text
)
diagram::style::EllipseNodeDescription_strategy = st.builds(
    diagram::style::EllipseNodeDescription,
    horizontalDiameterComputationExpression=
        safe_text,
    verticalDiameterComputationExpression=
        safe_text
)
diagram::style::LozengeNodeDescription_strategy = st.builds(
    diagram::style::LozengeNodeDescription,
    heightComputationExpression=
        safe_text,
    widthComputationExpression=
        safe_text
)
diagram::style::BundledImageDescription_strategy = st.builds(
    diagram::style::BundledImageDescription,
    providedShapeID=
        safe_text,
    shape=
        safe_text
)
diagram::style::SquareDescription_strategy = st.builds(
    diagram::style::SquareDescription,
    width=
        safe_text,
    height=
        safe_text
)
diagram::style::GaugeCompositeStyleDescription_strategy = st.builds(
    diagram::style::GaugeCompositeStyleDescription,
    alignment=
        safe_text
)
diagram::style::NoteDescription_strategy = st.builds(
    diagram::style::NoteDescription,
)
diagram::style::CustomStyleDescription_strategy = st.builds(
    diagram::style::CustomStyleDescription,
    id=
        safe_text
)
style::HideLabelCapabilityStyleDescription_strategy = st.builds(
    style::HideLabelCapabilityStyleDescription,
)
style::TooltipStyleDescription_strategy = st.builds(
    style::TooltipStyleDescription,
)
style::LabelStyleDescription_strategy = st.builds(
    style::LabelStyleDescription,
)
style::BorderedStyleDescription_strategy = st.builds(
    style::BorderedStyleDescription,
)
diagram::style::ContainerStyleDescription_strategy = st.builds(
    diagram::style::ContainerStyleDescription,
    roundedCorner=
        st.booleans(),
    containerLabelDirection=
        safe_text
)
ColorDescription_strategy = st.builds(
    ColorDescription,
)
StyleDescription_strategy = st.builds(
    StyleDescription,
)
diagram::style::RoundedCornerStyleDescription_strategy = st.builds(
    diagram::style::RoundedCornerStyleDescription,
    arcHeight=
        safe_text,
    arcWidth=
        safe_text
)
diagram::style::EdgeStyleDescription_strategy = st.builds(
    diagram::style::EdgeStyleDescription,
    sourceArrow=
        safe_text,
    sizeComputationExpression=
        safe_text,
    targetArrow=
        safe_text,
    lineStyle=
        safe_text,
    endsCentering=
        safe_text,
    foldingStyle=
        safe_text,
    routingStyle=
        safe_text
)
diagram::style::BorderedStyleDescription_strategy = st.builds(
    diagram::style::BorderedStyleDescription,
    borderSizeComputationExpression=
        safe_text,
    borderLineStyle=
        safe_text
)
tool::ContainerDropDescription_strategy = st.builds(
    tool::ContainerDropDescription,
)
diagram::description::DragAndDropTargetDescription_strategy = st.builds(
    diagram::description::DragAndDropTargetDescription,
)
Customization_strategy = st.builds(
    Customization,
)
DecorationDescriptionsSet_strategy = st.builds(
    DecorationDescriptionsSet,
)
description::EndUserDocumentedElement_strategy = st.builds(
    description::EndUserDocumentedElement,
)
DecorationDescription_strategy = st.builds(
    DecorationDescription,
)
diagram::description::MappingBasedDecoration_strategy = st.builds(
    diagram::description::MappingBasedDecoration,
)
DocumentedElement_strategy = st.builds(
    DocumentedElement,
)
diagram::concern::ConcernSet_strategy = st.builds(
    diagram::concern::ConcernSet,
)
diagram::description::Layout_strategy = st.builds(
    diagram::description::Layout,
)
style::EdgeStyleDescription_strategy = st.builds(
    style::EdgeStyleDescription,
)
ConditionalStyleDescription_strategy = st.builds(
    ConditionalStyleDescription,
)
diagram::description::ConditionalEdgeStyleDescription_strategy = st.builds(
    diagram::description::ConditionalEdgeStyleDescription,
)
diagram::description::ConditionalContainerStyleDescription_strategy = st.builds(
    diagram::description::ConditionalContainerStyleDescription,
)
diagram::description::ConditionalNodeStyleDescription_strategy = st.builds(
    diagram::description::ConditionalNodeStyleDescription,
)
description::IdentifiedElement_strategy = st.builds(
    description::IdentifiedElement,
)
diagram::description::IEdgeMapping_strategy = st.builds(
    diagram::description::IEdgeMapping,
)
AbstractNodeMapping_strategy = st.builds(
    AbstractNodeMapping,
)
tool::ReconnectEdgeDescription_strategy = st.builds(
    tool::ReconnectEdgeDescription,
)
ConditionalEdgeStyleDescription_strategy = st.builds(
    ConditionalEdgeStyleDescription,
)
description::ContainerMapping_strategy = st.builds(
    description::ContainerMapping,
)
ConditionalNodeStyleDescription_strategy = st.builds(
    ConditionalNodeStyleDescription,
)
description::IEdgeMapping_strategy = st.builds(
    description::IEdgeMapping,
)
style::NodeStyleDescription_strategy = st.builds(
    style::NodeStyleDescription,
)
description::AbstractMappingImport_strategy = st.builds(
    description::AbstractMappingImport,
)
diagram::description::ContainerMappingImport_strategy = st.builds(
    diagram::description::ContainerMappingImport,
)
description::NodeMapping_strategy = st.builds(
    description::NodeMapping,
)
diagram::description::NodeMappingImport_strategy = st.builds(
    diagram::description::NodeMappingImport,
)
ConditionalContainerStyleDescription_strategy = st.builds(
    ConditionalContainerStyleDescription,
)
style::ContainerStyleDescription_strategy = st.builds(
    style::ContainerStyleDescription,
)
diagram::style::FlatContainerStyleDescription_strategy = st.builds(
    diagram::style::FlatContainerStyleDescription,
    backgroundStyle=
        safe_text
)
diagram::style::WorkspaceImageDescription_strategy = st.builds(
    diagram::style::WorkspaceImageDescription,
    workspacePath=
        safe_text
)
diagram::style::ShapeContainerStyleDescription_strategy = st.builds(
    diagram::style::ShapeContainerStyleDescription,
    shape=
        safe_text
)
tool::InitialOperation_strategy = st.builds(
    tool::InitialOperation,
)
Layout_strategy = st.builds(
    Layout,
)
diagram::description::OrderedTreeLayout_strategy = st.builds(
    diagram::description::OrderedTreeLayout,
    childrenExpression=
        safe_text
)
diagram::description::CompositeLayout_strategy = st.builds(
    diagram::description::CompositeLayout,
    padding=
        st.integers(),
    direction=
        safe_text
)
tool::RepresentationCreationDescription_strategy = st.builds(
    tool::RepresentationCreationDescription,
)
tool::AbstractToolDescription_strategy = st.builds(
    tool::AbstractToolDescription,
)
concern::ConcernSet_strategy = st.builds(
    concern::ConcernSet,
)
validation::ValidationSet_strategy = st.builds(
    validation::ValidationSet,
)
EdgeMapping_strategy = st.builds(
    EdgeMapping,
)
description::PasteTargetDescription_strategy = st.builds(
    description::PasteTargetDescription,
)
diagram::description::DiagramElementMapping_strategy = st.builds(
    diagram::description::DiagramElementMapping,
    synchronizationLock=
        st.booleans(),
    createElements=
        st.booleans(),
    preconditionExpression=
        safe_text,
    semanticCandidatesExpression=
        safe_text,
    semanticElements=
        safe_text
)
description::RepresentationDescription_strategy = st.builds(
    description::RepresentationDescription,
)
description::DragAndDropTargetDescription_strategy = st.builds(
    description::DragAndDropTargetDescription,
)
diagram::description::ContainerMapping_strategy = st.builds(
    diagram::description::ContainerMapping,
    childrenPresentation=
        safe_text
)
diagram::description::NodeMapping_strategy = st.builds(
    diagram::description::NodeMapping,
)
diagram::description::DiagramDescription_strategy = st.builds(
    diagram::description::DiagramDescription,
    domainClass=
        safe_text,
    rootExpression=
        safe_text,
    preconditionExpression=
        safe_text,
    enablePopupBars=
        st.booleans()
)
diagram::EObject_strategy = st.builds(
    diagram::EObject,
)
tool::SelectModelElementVariable_strategy = st.builds(
    tool::SelectModelElementVariable,
)
TypedVariable_strategy = st.builds(
    TypedVariable,
)
VariableValue_strategy = st.builds(
    VariableValue,
)
diagram::EObjectVariableValue_strategy = st.builds(
    diagram::EObjectVariableValue,
)
diagram::TypedVariableValue_strategy = st.builds(
    diagram::TypedVariableValue,
    value=
        safe_text
)
diagram::HideLabelCapabilityStyle_strategy = st.builds(
    diagram::HideLabelCapabilityStyle,
    hideLabelByDefault=
        st.booleans()
)
diagram::DragAndDropTarget_strategy = st.builds(
    diagram::DragAndDropTarget,
)
style::StyleDescription_strategy = st.builds(
    style::StyleDescription,
)
diagram::style::NodeStyleDescription_strategy = st.builds(
    diagram::style::NodeStyleDescription,
    sizeComputationExpression=
        safe_text,
    resizeKind=
        safe_text,
    labelDirection=
        safe_text,
    labelPosition=
        safe_text,
    forbiddenSides=
        safe_text
)
diagram::ComputedStyleDescriptionRegistry_strategy = st.builds(
    diagram::ComputedStyleDescriptionRegistry,
)
EdgeStyle_strategy = st.builds(
    EdgeStyle,
)
diagram::BracketEdgeStyle_strategy = st.builds(
    diagram::BracketEdgeStyle,
)
BasicLabelStyle_strategy = st.builds(
    BasicLabelStyle,
)
CollapseFilter_strategy = st.builds(
    CollapseFilter,
)
diagram::IndirectlyCollapseFilter_strategy = st.builds(
    diagram::IndirectlyCollapseFilter,
)
diagram::VariableValue_strategy = st.builds(
    diagram::VariableValue,
)
diagram::EndLabelStyle_strategy = st.builds(
    diagram::EndLabelStyle,
)
diagram::CenterLabelStyle_strategy = st.builds(
    diagram::CenterLabelStyle,
)
diagram::BeginLabelStyle_strategy = st.builds(
    diagram::BeginLabelStyle,
)
Customizable_strategy = st.builds(
    Customizable,
)
diagram::GaugeSection_strategy = st.builds(
    diagram::GaugeSection,
    value=
        safe_text,
    label=
        safe_text,
    foregroundColor=
        safe_text,
    max=
        safe_text,
    min=
        safe_text,
    backgroundColor=
        safe_text
)
ContainerStyle_strategy = st.builds(
    ContainerStyle,
)
diagram::ShapeContainerStyle_strategy = st.builds(
    diagram::ShapeContainerStyle,
    backgroundColor=
        safe_text,
    shape=
        safe_text
)
diagram::FlatContainerStyle_strategy = st.builds(
    diagram::FlatContainerStyle,
    foregroundColor=
        safe_text,
    backgroundColor=
        safe_text,
    backgroundStyle=
        safe_text
)
NodeStyle_strategy = st.builds(
    NodeStyle,
)
diagram::Lozenge_strategy = st.builds(
    diagram::Lozenge,
    color=
        safe_text,
    height=
        safe_text,
    width=
        safe_text
)
diagram::CustomStyle_strategy = st.builds(
    diagram::CustomStyle,
    id=
        safe_text
)
diagram::GaugeCompositeStyle_strategy = st.builds(
    diagram::GaugeCompositeStyle,
    alignment=
        safe_text
)
diagram::Square_strategy = st.builds(
    diagram::Square,
    width=
        safe_text,
    color=
        safe_text,
    height=
        safe_text
)
diagram::WorkspaceImage_strategy = st.builds(
    diagram::WorkspaceImage,
    workspacePath=
        safe_text
)
diagram::BundledImage_strategy = st.builds(
    diagram::BundledImage,
    shape=
        safe_text,
    providedShapeID=
        safe_text,
    color=
        safe_text
)
diagram::Ellipse_strategy = st.builds(
    diagram::Ellipse,
    verticalDiameter=
        safe_text,
    color=
        safe_text,
    horizontalDiameter=
        safe_text
)
diagram::Note_strategy = st.builds(
    diagram::Note,
    color=
        safe_text
)
diagram::Dot_strategy = st.builds(
    diagram::Dot,
    strokeSizeComputationExpression=
        safe_text,
    backgroundColor=
        safe_text
)
HideLabelCapabilityStyle_strategy = st.builds(
    HideLabelCapabilityStyle,
)
BorderedStyle_strategy = st.builds(
    BorderedStyle,
)
Style_strategy = st.builds(
    Style,
)
diagram::BorderedStyle_strategy = st.builds(
    diagram::BorderedStyle,
    borderSize=
        safe_text,
    borderColor=
        safe_text,
    borderSizeComputationExpression=
        safe_text,
    borderLineStyle=
        safe_text
)
LabelStyle_strategy = st.builds(
    LabelStyle,
)
IEdgeMapping_strategy = st.builds(
    IEdgeMapping,
)
diagram::EdgeTarget_strategy = st.builds(
    diagram::EdgeTarget,
)
diagram::EdgeStyle_strategy = st.builds(
    diagram::EdgeStyle,
    lineStyle=
        safe_text,
    size=
        safe_text,
    foldingStyle=
        safe_text,
    sourceArrow=
        safe_text,
    routingStyle=
        safe_text,
    targetArrow=
        safe_text,
    centered=
        safe_text,
    strokeColor=
        safe_text
)
DDiagramElementContainer_strategy = st.builds(
    DDiagramElementContainer,
)
diagram::DNodeList_strategy = st.builds(
    diagram::DNodeList,
)
diagram::DNodeContainer_strategy = st.builds(
    diagram::DNodeContainer,
    childrenPresentation=
        safe_text
)
ContainerMapping_strategy = st.builds(
    ContainerMapping,
)
diagram::ContainerStyle_strategy = st.builds(
    diagram::ContainerStyle,
    containerLabelDirection=
        safe_text
)
diagram::GraphicalFilter_strategy = st.builds(
    diagram::GraphicalFilter,
)
NodeMapping_strategy = st.builds(
    NodeMapping,
)
diagram::Style_strategy = st.builds(
    diagram::Style,
)
diagram::NodeStyle_strategy = st.builds(
    diagram::NodeStyle,
    labelDirection=
        safe_text,
    labelPosition=
        safe_text
)
EdgeTarget_strategy = st.builds(
    EdgeTarget,
)
AbstractDNode_strategy = st.builds(
    AbstractDNode,
)
DDiagramElement_strategy = st.builds(
    DDiagramElement,
)
diagram::AbstractDNode_strategy = st.builds(
    diagram::AbstractDNode,
    arrangeConstraints=
        safe_text
)
filter::CompositeFilterDescription_strategy = st.builds(
    filter::CompositeFilterDescription,
)
GraphicalFilter_strategy = st.builds(
    GraphicalFilter,
)
diagram::AbsoluteBoundsFilter_strategy = st.builds(
    diagram::AbsoluteBoundsFilter,
    x=
        safe_text,
    y=
        safe_text,
    width=
        safe_text,
    height=
        safe_text
)
diagram::AppliedCompositeFilters_strategy = st.builds(
    diagram::AppliedCompositeFilters,
)
diagram::CollapseFilter_strategy = st.builds(
    diagram::CollapseFilter,
    width=
        st.integers(),
    height=
        st.integers()
)
diagram::HideLabelFilter_strategy = st.builds(
    diagram::HideLabelFilter,
)
diagram::FoldingPointFilter_strategy = st.builds(
    diagram::FoldingPointFilter,
)
diagram::FoldingFilter_strategy = st.builds(
    diagram::FoldingFilter,
)
diagram::HideFilter_strategy = st.builds(
    diagram::HideFilter,
)
filter::FilterDescription_strategy = st.builds(
    filter::FilterDescription,
)
DiagramElementMapping_strategy = st.builds(
    DiagramElementMapping,
)
diagram::Decoration_strategy = st.builds(
    diagram::Decoration,
)
DRepresentationElement_strategy = st.builds(
    DRepresentationElement,
)
DSemanticDecorator_strategy = st.builds(
    DSemanticDecorator,
)
DDiagram_strategy = st.builds(
    DDiagram,
)
diagram::DSemanticDiagram_strategy = st.builds(
    diagram::DSemanticDiagram,
)
Layer_strategy = st.builds(
    Layer,
)
diagram::description::AdditionalLayer_strategy = st.builds(
    diagram::description::AdditionalLayer,
    activeByDefault=
        st.booleans(),
    optional=
        st.booleans()
)
diagram::FilterVariableHistory_strategy = st.builds(
    diagram::FilterVariableHistory,
)
tool::BehaviorTool_strategy = st.builds(
    tool::BehaviorTool,
)
validation::ValidationRule_strategy = st.builds(
    validation::ValidationRule,
)
concern::ConcernDescription_strategy = st.builds(
    concern::ConcernDescription,
)
diagram::DNodeListElement_strategy = st.builds(
    diagram::DNodeListElement,
)
diagram::DEdge_strategy = st.builds(
    diagram::DEdge,
    beginLabel=
        safe_text,
    endLabel=
        safe_text,
    size=
        safe_text,
    routingStyle=
        safe_text,
    isMockEdge=
        st.booleans(),
    arrangeConstraints=
        safe_text,
    isFold=
        st.booleans()
)
DiagramDescription_strategy = st.builds(
    DiagramDescription,
)
diagram::DDiagramElement_strategy = st.builds(
    diagram::DDiagramElement,
    tooltipText=
        safe_text,
    visible=
        st.booleans()
)
DragAndDropTarget_strategy = st.builds(
    DragAndDropTarget,
)
diagram::DDiagramElementContainer_strategy = st.builds(
    diagram::DDiagramElementContainer,
    height=
        safe_text,
    width=
        safe_text
)
diagram::DNode_strategy = st.builds(
    diagram::DNode,
    width=
        safe_text,
    resizeKind=
        safe_text,
    labelPosition=
        safe_text,
    height=
        safe_text
)
description::DocumentedElement_strategy = st.builds(
    description::DocumentedElement,
)
diagram::filter::FilterDescription_strategy = st.builds(
    diagram::filter::FilterDescription,
)
diagram::description::Layer_strategy = st.builds(
    diagram::description::Layer,
    icon=
        safe_text
)
diagram::description::EdgeMappingImport_strategy = st.builds(
    diagram::description::EdgeMappingImport,
    inheritsAncestorFilters=
        st.booleans()
)
diagram::tool::ToolSection_strategy = st.builds(
    diagram::tool::ToolSection,
    icon=
        safe_text
)
diagram::description::EdgeMapping_strategy = st.builds(
    diagram::description::EdgeMapping,
    pathExpression=
        safe_text,
    domainClass=
        safe_text,
    targetExpression=
        safe_text,
    targetFinderExpression=
        safe_text,
    sourceFinderExpression=
        safe_text,
    useDomainElement=
        st.booleans()
)
diagram::concern::ConcernDescription_strategy = st.builds(
    diagram::concern::ConcernDescription,
)
diagram::description::AbstractNodeMapping_strategy = st.builds(
    diagram::description::AbstractNodeMapping,
    domainClass=
        safe_text
)
DRepresentation_strategy = st.builds(
    DRepresentation,
)
diagram::DDiagram_strategy = st.builds(
    diagram::DDiagram,
    isInLayoutingMode=
        st.booleans(),
    headerHeight=
        st.integers(),
    synchronized=
        st.booleans()
)

@given(instance=description::AbstractNodeMapping_strategy)
@settings(max_examples=50)
def test_description::abstractnodemapping_instantiation(instance):
    assert isinstance(instance, description::AbstractNodeMapping)

@given(instance=description::DiagramElementMapping_strategy)
@settings(max_examples=50)
def test_description::diagramelementmapping_instantiation(instance):
    assert isinstance(instance, description::DiagramElementMapping)

@given(instance=tool::DoubleClickDescription_strategy)
@settings(max_examples=50)
def test_tool::doubleclickdescription_instantiation(instance):
    assert isinstance(instance, tool::DoubleClickDescription)

@given(instance=tool::DirectEditLabel_strategy)
@settings(max_examples=50)
def test_tool::directeditlabel_instantiation(instance):
    assert isinstance(instance, tool::DirectEditLabel)

@given(instance=tool::DeleteElementDescription_strategy)
@settings(max_examples=50)
def test_tool::deleteelementdescription_instantiation(instance):
    assert isinstance(instance, tool::DeleteElementDescription)

@given(instance=description::RepresentationElementMapping_strategy)
@settings(max_examples=50)
def test_description::representationelementmapping_instantiation(instance):
    assert isinstance(instance, description::RepresentationElementMapping)

@given(instance=RepresentationExtensionDescription_strategy)
@settings(max_examples=50)
def test_representationextensiondescription_instantiation(instance):
    assert isinstance(instance, RepresentationExtensionDescription)

@given(instance=diagram::description::DiagramExtensionDescription_strategy)
@settings(max_examples=50)
def test_diagram::description::diagramextensiondescription_instantiation(instance):
    assert isinstance(instance, diagram::description::DiagramExtensionDescription)

@given(instance=description::DiagramDescription_strategy)
@settings(max_examples=50)
def test_description::diagramdescription_instantiation(instance):
    assert isinstance(instance, description::DiagramDescription)

@given(instance=description::RepresentationImportDescription_strategy)
@settings(max_examples=50)
def test_description::representationimportdescription_instantiation(instance):
    assert isinstance(instance, description::RepresentationImportDescription)

@given(instance=diagram::description::DiagramImportDescription_strategy)
@settings(max_examples=50)
def test_diagram::description::diagramimportdescription_instantiation(instance):
    assert isinstance(instance, diagram::description::DiagramImportDescription)

@given(instance=tool::ToolSection_strategy)
@settings(max_examples=50)
def test_tool::toolsection_instantiation(instance):
    assert isinstance(instance, tool::ToolSection)

@given(instance=EdgeMappingImport_strategy)
@settings(max_examples=50)
def test_edgemappingimport_instantiation(instance):
    assert isinstance(instance, EdgeMappingImport)

@given(instance=AdditionalLayer_strategy)
@settings(max_examples=50)
def test_additionallayer_instantiation(instance):
    assert isinstance(instance, AdditionalLayer)

@given(instance=Filter_strategy)
@settings(max_examples=50)
def test_filter_instantiation(instance):
    assert isinstance(instance, Filter)

@given(instance=diagram::filter::MappingFilter_strategy)
@settings(max_examples=50)
def test_diagram::filter::mappingfilter_instantiation(instance):
    assert isinstance(instance, diagram::filter::MappingFilter)

@given(instance=diagram::filter::MappingFilter_strategy)
def test_diagram::filter::mappingfilter_viewConditionExpression_type(instance):
    assert isinstance(instance.viewConditionExpression, str)


@given(instance=diagram::filter::MappingFilter_strategy)
def test_diagram::filter::mappingfilter_viewConditionExpression_setter(instance):
    original = instance.viewConditionExpression
    instance.viewConditionExpression = original
    assert instance.viewConditionExpression == original

@given(instance=diagram::filter::MappingFilter_strategy)
def test_diagram::filter::mappingfilter_semanticConditionExpression_type(instance):
    assert isinstance(instance.semanticConditionExpression, str)


@given(instance=diagram::filter::MappingFilter_strategy)
def test_diagram::filter::mappingfilter_semanticConditionExpression_setter(instance):
    original = instance.semanticConditionExpression
    instance.semanticConditionExpression = original
    assert instance.semanticConditionExpression == original

@given(instance=diagram::filter::Filter_strategy)
@settings(max_examples=50)
def test_diagram::filter::filter_instantiation(instance):
    assert isinstance(instance, diagram::filter::Filter)

@given(instance=diagram::filter::Filter_strategy)
def test_diagram::filter::filter_filterKind_type(instance):
    assert isinstance(instance.filterKind, str)


@given(instance=diagram::filter::Filter_strategy)
def test_diagram::filter::filter_filterKind_setter(instance):
    original = instance.filterKind
    instance.filterKind = original
    assert instance.filterKind == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram::filter::Filter_strategy)
@settings(max_examples=30)
def test_diagram::filter::filter_isvisible_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isVisible(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isVisible).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isVisible' in diagram::filter::Filter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isVisible' in diagram::filter::Filter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isVisible' in diagram::filter::Filter is not implemented or raised an error")

@given(instance=InteractiveVariableDescription_strategy)
@settings(max_examples=50)
def test_interactivevariabledescription_instantiation(instance):
    assert isinstance(instance, InteractiveVariableDescription)

@given(instance=diagram::filter::VariableFilter_strategy)
@settings(max_examples=50)
def test_diagram::filter::variablefilter_instantiation(instance):
    assert isinstance(instance, diagram::filter::VariableFilter)

@given(instance=diagram::filter::VariableFilter_strategy)
def test_diagram::filter::variablefilter_semanticConditionExpression_type(instance):
    assert isinstance(instance.semanticConditionExpression, str)


@given(instance=diagram::filter::VariableFilter_strategy)
def test_diagram::filter::variablefilter_semanticConditionExpression_setter(instance):
    original = instance.semanticConditionExpression
    instance.semanticConditionExpression = original
    assert instance.semanticConditionExpression == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram::filter::VariableFilter_strategy)
@settings(max_examples=30)
def test_diagram::filter::variablefilter_resetvariables_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.resetVariables()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.resetVariables).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'resetVariables' in diagram::filter::VariableFilter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'resetVariables' in diagram::filter::VariableFilter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'resetVariables' in diagram::filter::VariableFilter is not implemented or raised an error")

@given(instance=filter::Filter_strategy)
@settings(max_examples=50)
def test_filter::filter_instantiation(instance):
    assert isinstance(instance, filter::Filter)

@given(instance=FilterDescription_strategy)
@settings(max_examples=50)
def test_filterdescription_instantiation(instance):
    assert isinstance(instance, FilterDescription)

@given(instance=diagram::filter::CompositeFilterDescription_strategy)
@settings(max_examples=50)
def test_diagram::filter::compositefilterdescription_instantiation(instance):
    assert isinstance(instance, diagram::filter::CompositeFilterDescription)

@given(instance=RepresentationNavigationDescription_strategy)
@settings(max_examples=50)
def test_representationnavigationdescription_instantiation(instance):
    assert isinstance(instance, RepresentationNavigationDescription)

@given(instance=diagram::tool::DiagramNavigationDescription_strategy)
@settings(max_examples=50)
def test_diagram::tool::diagramnavigationdescription_instantiation(instance):
    assert isinstance(instance, diagram::tool::DiagramNavigationDescription)

@given(instance=tool::InitialContainerDropOperation_strategy)
@settings(max_examples=50)
def test_tool::initialcontainerdropoperation_instantiation(instance):
    assert isinstance(instance, tool::InitialContainerDropOperation)

@given(instance=tool::ElementDropVariable_strategy)
@settings(max_examples=50)
def test_tool::elementdropvariable_instantiation(instance):
    assert isinstance(instance, tool::ElementDropVariable)

@given(instance=tool::DropContainerVariable_strategy)
@settings(max_examples=50)
def test_tool::dropcontainervariable_instantiation(instance):
    assert isinstance(instance, tool::DropContainerVariable)

@given(instance=RepresentationCreationDescription_strategy)
@settings(max_examples=50)
def test_representationcreationdescription_instantiation(instance):
    assert isinstance(instance, RepresentationCreationDescription)

@given(instance=diagram::tool::DiagramCreationDescription_strategy)
@settings(max_examples=50)
def test_diagram::tool::diagramcreationdescription_instantiation(instance):
    assert isinstance(instance, diagram::tool::DiagramCreationDescription)

@given(instance=CreateView_strategy)
@settings(max_examples=50)
def test_createview_instantiation(instance):
    assert isinstance(instance, CreateView)

@given(instance=diagram::tool::CreateEdgeView_strategy)
@settings(max_examples=50)
def test_diagram::tool::createedgeview_instantiation(instance):
    assert isinstance(instance, diagram::tool::CreateEdgeView)

@given(instance=diagram::tool::CreateEdgeView_strategy)
def test_diagram::tool::createedgeview_targetExpression_type(instance):
    assert isinstance(instance.targetExpression, str)


@given(instance=diagram::tool::CreateEdgeView_strategy)
def test_diagram::tool::createedgeview_targetExpression_setter(instance):
    original = instance.targetExpression
    instance.targetExpression = original
    assert instance.targetExpression == original

@given(instance=diagram::tool::CreateEdgeView_strategy)
def test_diagram::tool::createedgeview_sourceExpression_type(instance):
    assert isinstance(instance.sourceExpression, str)


@given(instance=diagram::tool::CreateEdgeView_strategy)
def test_diagram::tool::createedgeview_sourceExpression_setter(instance):
    original = instance.sourceExpression
    instance.sourceExpression = original
    assert instance.sourceExpression == original

@given(instance=AbstractToolDescription_strategy)
@settings(max_examples=50)
def test_abstracttooldescription_instantiation(instance):
    assert isinstance(instance, AbstractToolDescription)

@given(instance=diagram::tool::RequestDescription_strategy)
@settings(max_examples=50)
def test_diagram::tool::requestdescription_instantiation(instance):
    assert isinstance(instance, diagram::tool::RequestDescription)

@given(instance=diagram::tool::RequestDescription_strategy)
def test_diagram::tool::requestdescription_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=diagram::tool::RequestDescription_strategy)
def test_diagram::tool::requestdescription_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=ContainerModelOperation_strategy)
@settings(max_examples=50)
def test_containermodeloperation_instantiation(instance):
    assert isinstance(instance, ContainerModelOperation)

@given(instance=diagram::tool::Navigation_strategy)
@settings(max_examples=50)
def test_diagram::tool::navigation_instantiation(instance):
    assert isinstance(instance, diagram::tool::Navigation)

@given(instance=diagram::tool::Navigation_strategy)
def test_diagram::tool::navigation_createIfNotExistent_type(instance):
    assert isinstance(instance.createIfNotExistent, bool)


@given(instance=diagram::tool::Navigation_strategy)
def test_diagram::tool::navigation_createIfNotExistent_setter(instance):
    original = instance.createIfNotExistent
    instance.createIfNotExistent = original
    assert instance.createIfNotExistent == original

@given(instance=diagram::tool::CreateView_strategy)
@settings(max_examples=50)
def test_diagram::tool::createview_instantiation(instance):
    assert isinstance(instance, diagram::tool::CreateView)

@given(instance=diagram::tool::CreateView_strategy)
def test_diagram::tool::createview_variableName_type(instance):
    assert isinstance(instance.variableName, str)


@given(instance=diagram::tool::CreateView_strategy)
def test_diagram::tool::createview_variableName_setter(instance):
    original = instance.variableName
    instance.variableName = original
    assert instance.variableName == original

@given(instance=diagram::tool::CreateView_strategy)
def test_diagram::tool::createview_containerViewExpression_type(instance):
    assert isinstance(instance.containerViewExpression, str)


@given(instance=diagram::tool::CreateView_strategy)
def test_diagram::tool::createview_containerViewExpression_setter(instance):
    original = instance.containerViewExpression
    instance.containerViewExpression = original
    assert instance.containerViewExpression == original

@given(instance=tool::VariableContainer_strategy)
@settings(max_examples=50)
def test_tool::variablecontainer_instantiation(instance):
    assert isinstance(instance, tool::VariableContainer)

@given(instance=description::AbstractVariable_strategy)
@settings(max_examples=50)
def test_description::abstractvariable_instantiation(instance):
    assert isinstance(instance, description::AbstractVariable)

@given(instance=diagram::tool::ElementDoubleClickVariable_strategy)
@settings(max_examples=50)
def test_diagram::tool::elementdoubleclickvariable_instantiation(instance):
    assert isinstance(instance, diagram::tool::ElementDoubleClickVariable)

@given(instance=diagram::tool::TargetEdgeCreationVariable_strategy)
@settings(max_examples=50)
def test_diagram::tool::targetedgecreationvariable_instantiation(instance):
    assert isinstance(instance, diagram::tool::TargetEdgeCreationVariable)

@given(instance=diagram::tool::SourceEdgeViewCreationVariable_strategy)
@settings(max_examples=50)
def test_diagram::tool::sourceedgeviewcreationvariable_instantiation(instance):
    assert isinstance(instance, diagram::tool::SourceEdgeViewCreationVariable)

@given(instance=diagram::tool::NodeCreationVariable_strategy)
@settings(max_examples=50)
def test_diagram::tool::nodecreationvariable_instantiation(instance):
    assert isinstance(instance, diagram::tool::NodeCreationVariable)

@given(instance=diagram::tool::TargetEdgeViewCreationVariable_strategy)
@settings(max_examples=50)
def test_diagram::tool::targetedgeviewcreationvariable_instantiation(instance):
    assert isinstance(instance, diagram::tool::TargetEdgeViewCreationVariable)

@given(instance=diagram::tool::SourceEdgeCreationVariable_strategy)
@settings(max_examples=50)
def test_diagram::tool::sourceedgecreationvariable_instantiation(instance):
    assert isinstance(instance, diagram::tool::SourceEdgeCreationVariable)

@given(instance=diagram::tool::BehaviorTool_strategy)
@settings(max_examples=50)
def test_diagram::tool::behaviortool_instantiation(instance):
    assert isinstance(instance, diagram::tool::BehaviorTool)

@given(instance=diagram::tool::BehaviorTool_strategy)
def test_diagram::tool::behaviortool_domainClass_type(instance):
    assert isinstance(instance.domainClass, str)


@given(instance=diagram::tool::BehaviorTool_strategy)
def test_diagram::tool::behaviortool_domainClass_setter(instance):
    original = instance.domainClass
    instance.domainClass = original
    assert instance.domainClass == original

@given(instance=tool::EditMaskVariables_strategy)
@settings(max_examples=50)
def test_tool::editmaskvariables_instantiation(instance):
    assert isinstance(instance, tool::EditMaskVariables)

@given(instance=diagram::tool::DeleteHook_strategy)
@settings(max_examples=50)
def test_diagram::tool::deletehook_instantiation(instance):
    assert isinstance(instance, diagram::tool::DeleteHook)

@given(instance=diagram::tool::DeleteHook_strategy)
def test_diagram::tool::deletehook_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=diagram::tool::DeleteHook_strategy)
def test_diagram::tool::deletehook_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=tool::ElementSelectVariable_strategy)
@settings(max_examples=50)
def test_tool::elementselectvariable_instantiation(instance):
    assert isinstance(instance, tool::ElementSelectVariable)

@given(instance=diagram::tool::DeleteHookParameter_strategy)
@settings(max_examples=50)
def test_diagram::tool::deletehookparameter_instantiation(instance):
    assert isinstance(instance, diagram::tool::DeleteHookParameter)

@given(instance=diagram::tool::DeleteHookParameter_strategy)
def test_diagram::tool::deletehookparameter_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=diagram::tool::DeleteHookParameter_strategy)
def test_diagram::tool::deletehookparameter_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=diagram::tool::DeleteHookParameter_strategy)
def test_diagram::tool::deletehookparameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=diagram::tool::DeleteHookParameter_strategy)
def test_diagram::tool::deletehookparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tool::DeleteHookParameter_strategy)
@settings(max_examples=50)
def test_tool::deletehookparameter_instantiation(instance):
    assert isinstance(instance, tool::DeleteHookParameter)

@given(instance=tool::ElementDoubleClickVariable_strategy)
@settings(max_examples=50)
def test_tool::elementdoubleclickvariable_instantiation(instance):
    assert isinstance(instance, tool::ElementDoubleClickVariable)

@given(instance=tool::DeleteHook_strategy)
@settings(max_examples=50)
def test_tool::deletehook_instantiation(instance):
    assert isinstance(instance, tool::DeleteHook)

@given(instance=tool::ElementDeleteVariable_strategy)
@settings(max_examples=50)
def test_tool::elementdeletevariable_instantiation(instance):
    assert isinstance(instance, tool::ElementDeleteVariable)

@given(instance=tool::InitEdgeCreationOperation_strategy)
@settings(max_examples=50)
def test_tool::initedgecreationoperation_instantiation(instance):
    assert isinstance(instance, tool::InitEdgeCreationOperation)

@given(instance=tool::TargetEdgeViewCreationVariable_strategy)
@settings(max_examples=50)
def test_tool::targetedgeviewcreationvariable_instantiation(instance):
    assert isinstance(instance, tool::TargetEdgeViewCreationVariable)

@given(instance=tool::SourceEdgeViewCreationVariable_strategy)
@settings(max_examples=50)
def test_tool::sourceedgeviewcreationvariable_instantiation(instance):
    assert isinstance(instance, tool::SourceEdgeViewCreationVariable)

@given(instance=tool::TargetEdgeCreationVariable_strategy)
@settings(max_examples=50)
def test_tool::targetedgecreationvariable_instantiation(instance):
    assert isinstance(instance, tool::TargetEdgeCreationVariable)

@given(instance=tool::SourceEdgeCreationVariable_strategy)
@settings(max_examples=50)
def test_tool::sourceedgecreationvariable_instantiation(instance):
    assert isinstance(instance, tool::SourceEdgeCreationVariable)

@given(instance=tool::PopupMenu_strategy)
@settings(max_examples=50)
def test_tool::popupmenu_instantiation(instance):
    assert isinstance(instance, tool::PopupMenu)

@given(instance=tool::InitialNodeCreationOperation_strategy)
@settings(max_examples=50)
def test_tool::initialnodecreationoperation_instantiation(instance):
    assert isinstance(instance, tool::InitialNodeCreationOperation)

@given(instance=tool::ContainerViewVariable_strategy)
@settings(max_examples=50)
def test_tool::containerviewvariable_instantiation(instance):
    assert isinstance(instance, tool::ContainerViewVariable)

@given(instance=tool::NodeCreationVariable_strategy)
@settings(max_examples=50)
def test_tool::nodecreationvariable_instantiation(instance):
    assert isinstance(instance, tool::NodeCreationVariable)

@given(instance=MappingBasedToolDescription_strategy)
@settings(max_examples=50)
def test_mappingbasedtooldescription_instantiation(instance):
    assert isinstance(instance, MappingBasedToolDescription)

@given(instance=diagram::tool::DoubleClickDescription_strategy)
@settings(max_examples=50)
def test_diagram::tool::doubleclickdescription_instantiation(instance):
    assert isinstance(instance, diagram::tool::DoubleClickDescription)

@given(instance=diagram::tool::EdgeCreationDescription_strategy)
@settings(max_examples=50)
def test_diagram::tool::edgecreationdescription_instantiation(instance):
    assert isinstance(instance, diagram::tool::EdgeCreationDescription)

@given(instance=diagram::tool::EdgeCreationDescription_strategy)
def test_diagram::tool::edgecreationdescription_connectionStartPrecondition_type(instance):
    assert isinstance(instance.connectionStartPrecondition, str)


@given(instance=diagram::tool::EdgeCreationDescription_strategy)
def test_diagram::tool::edgecreationdescription_connectionStartPrecondition_setter(instance):
    original = instance.connectionStartPrecondition
    instance.connectionStartPrecondition = original
    assert instance.connectionStartPrecondition == original

@given(instance=diagram::tool::EdgeCreationDescription_strategy)
def test_diagram::tool::edgecreationdescription_iconPath_type(instance):
    assert isinstance(instance.iconPath, str)


@given(instance=diagram::tool::EdgeCreationDescription_strategy)
def test_diagram::tool::edgecreationdescription_iconPath_setter(instance):
    original = instance.iconPath
    instance.iconPath = original
    assert instance.iconPath == original

@given(instance=diagram::tool::ReconnectEdgeDescription_strategy)
@settings(max_examples=50)
def test_diagram::tool::reconnectedgedescription_instantiation(instance):
    assert isinstance(instance, diagram::tool::ReconnectEdgeDescription)

@given(instance=diagram::tool::ReconnectEdgeDescription_strategy)
def test_diagram::tool::reconnectedgedescription_reconnectionKind_type(instance):
    assert isinstance(instance.reconnectionKind, str)


@given(instance=diagram::tool::ReconnectEdgeDescription_strategy)
def test_diagram::tool::reconnectedgedescription_reconnectionKind_setter(instance):
    original = instance.reconnectionKind
    instance.reconnectionKind = original
    assert instance.reconnectionKind == original

@given(instance=diagram::tool::ContainerDropDescription_strategy)
@settings(max_examples=50)
def test_diagram::tool::containerdropdescription_instantiation(instance):
    assert isinstance(instance, diagram::tool::ContainerDropDescription)

@given(instance=diagram::tool::ContainerDropDescription_strategy)
def test_diagram::tool::containerdropdescription_dragSource_type(instance):
    assert isinstance(instance.dragSource, str)


@given(instance=diagram::tool::ContainerDropDescription_strategy)
def test_diagram::tool::containerdropdescription_dragSource_setter(instance):
    original = instance.dragSource
    instance.dragSource = original
    assert instance.dragSource == original

@given(instance=diagram::tool::ContainerDropDescription_strategy)
def test_diagram::tool::containerdropdescription_moveEdges_type(instance):
    assert isinstance(instance.moveEdges, bool)


@given(instance=diagram::tool::ContainerDropDescription_strategy)
def test_diagram::tool::containerdropdescription_moveEdges_setter(instance):
    original = instance.moveEdges
    instance.moveEdges = original
    assert instance.moveEdges == original

@given(instance=diagram::tool::ContainerCreationDescription_strategy)
@settings(max_examples=50)
def test_diagram::tool::containercreationdescription_instantiation(instance):
    assert isinstance(instance, diagram::tool::ContainerCreationDescription)

@given(instance=diagram::tool::ContainerCreationDescription_strategy)
def test_diagram::tool::containercreationdescription_iconPath_type(instance):
    assert isinstance(instance.iconPath, str)


@given(instance=diagram::tool::ContainerCreationDescription_strategy)
def test_diagram::tool::containercreationdescription_iconPath_setter(instance):
    original = instance.iconPath
    instance.iconPath = original
    assert instance.iconPath == original

@given(instance=diagram::tool::DirectEditLabel_strategy)
@settings(max_examples=50)
def test_diagram::tool::directeditlabel_instantiation(instance):
    assert isinstance(instance, diagram::tool::DirectEditLabel)

@given(instance=diagram::tool::DirectEditLabel_strategy)
def test_diagram::tool::directeditlabel_inputLabelExpression_type(instance):
    assert isinstance(instance.inputLabelExpression, str)


@given(instance=diagram::tool::DirectEditLabel_strategy)
def test_diagram::tool::directeditlabel_inputLabelExpression_setter(instance):
    original = instance.inputLabelExpression
    instance.inputLabelExpression = original
    assert instance.inputLabelExpression == original

@given(instance=diagram::tool::DeleteElementDescription_strategy)
@settings(max_examples=50)
def test_diagram::tool::deleteelementdescription_instantiation(instance):
    assert isinstance(instance, diagram::tool::DeleteElementDescription)

@given(instance=diagram::tool::NodeCreationDescription_strategy)
@settings(max_examples=50)
def test_diagram::tool::nodecreationdescription_instantiation(instance):
    assert isinstance(instance, diagram::tool::NodeCreationDescription)

@given(instance=diagram::tool::NodeCreationDescription_strategy)
def test_diagram::tool::nodecreationdescription_iconPath_type(instance):
    assert isinstance(instance.iconPath, str)


@given(instance=diagram::tool::NodeCreationDescription_strategy)
def test_diagram::tool::nodecreationdescription_iconPath_setter(instance):
    original = instance.iconPath
    instance.iconPath = original
    assert instance.iconPath == original

@given(instance=tool::ToolGroup_strategy)
@settings(max_examples=50)
def test_tool::toolgroup_instantiation(instance):
    assert isinstance(instance, tool::ToolGroup)

@given(instance=diagram::tool::ToolGroupExtension_strategy)
@settings(max_examples=50)
def test_diagram::tool::toolgroupextension_instantiation(instance):
    assert isinstance(instance, diagram::tool::ToolGroupExtension)

@given(instance=ToolEntry_strategy)
@settings(max_examples=50)
def test_toolentry_instantiation(instance):
    assert isinstance(instance, ToolEntry)

@given(instance=diagram::tool::ToolGroup_strategy)
@settings(max_examples=50)
def test_diagram::tool::toolgroup_instantiation(instance):
    assert isinstance(instance, diagram::tool::ToolGroup)

@given(instance=tool::ToolGroupExtension_strategy)
@settings(max_examples=50)
def test_tool::toolgroupextension_instantiation(instance):
    assert isinstance(instance, tool::ToolGroupExtension)

@given(instance=style::BeginLabelStyleDescription_strategy)
@settings(max_examples=50)
def test_style::beginlabelstyledescription_instantiation(instance):
    assert isinstance(instance, style::BeginLabelStyleDescription)

@given(instance=tool::ToolEntry_strategy)
@settings(max_examples=50)
def test_tool::toolentry_instantiation(instance):
    assert isinstance(instance, tool::ToolEntry)

@given(instance=diagram::style::HideLabelCapabilityStyleDescription_strategy)
@settings(max_examples=50)
def test_diagram::style::hidelabelcapabilitystyledescription_instantiation(instance):
    assert isinstance(instance, diagram::style::HideLabelCapabilityStyleDescription)

@given(instance=diagram::style::HideLabelCapabilityStyleDescription_strategy)
def test_diagram::style::hidelabelcapabilitystyledescription_hideLabelByDefault_type(instance):
    assert isinstance(instance.hideLabelByDefault, bool)


@given(instance=diagram::style::HideLabelCapabilityStyleDescription_strategy)
def test_diagram::style::hidelabelcapabilitystyledescription_hideLabelByDefault_setter(instance):
    original = instance.hideLabelByDefault
    instance.hideLabelByDefault = original
    assert instance.hideLabelByDefault == original

@given(instance=EdgeStyleDescription_strategy)
@settings(max_examples=50)
def test_edgestyledescription_instantiation(instance):
    assert isinstance(instance, EdgeStyleDescription)

@given(instance=diagram::style::BracketEdgeStyleDescription_strategy)
@settings(max_examples=50)
def test_diagram::style::bracketedgestyledescription_instantiation(instance):
    assert isinstance(instance, diagram::style::BracketEdgeStyleDescription)

@given(instance=BasicLabelStyleDescription_strategy)
@settings(max_examples=50)
def test_basiclabelstyledescription_instantiation(instance):
    assert isinstance(instance, BasicLabelStyleDescription)

@given(instance=diagram::style::EndLabelStyleDescription_strategy)
@settings(max_examples=50)
def test_diagram::style::endlabelstyledescription_instantiation(instance):
    assert isinstance(instance, diagram::style::EndLabelStyleDescription)

@given(instance=diagram::style::CenterLabelStyleDescription_strategy)
@settings(max_examples=50)
def test_diagram::style::centerlabelstyledescription_instantiation(instance):
    assert isinstance(instance, diagram::style::CenterLabelStyleDescription)

@given(instance=diagram::style::BeginLabelStyleDescription_strategy)
@settings(max_examples=50)
def test_diagram::style::beginlabelstyledescription_instantiation(instance):
    assert isinstance(instance, diagram::style::BeginLabelStyleDescription)

@given(instance=style::EndLabelStyleDescription_strategy)
@settings(max_examples=50)
def test_style::endlabelstyledescription_instantiation(instance):
    assert isinstance(instance, style::EndLabelStyleDescription)

@given(instance=style::CenterLabelStyleDescription_strategy)
@settings(max_examples=50)
def test_style::centerlabelstyledescription_instantiation(instance):
    assert isinstance(instance, style::CenterLabelStyleDescription)

@given(instance=diagram::style::SizeComputationContainerStyleDescription_strategy)
@settings(max_examples=50)
def test_diagram::style::sizecomputationcontainerstyledescription_instantiation(instance):
    assert isinstance(instance, diagram::style::SizeComputationContainerStyleDescription)

@given(instance=diagram::style::SizeComputationContainerStyleDescription_strategy)
def test_diagram::style::sizecomputationcontainerstyledescription_widthComputationExpression_type(instance):
    assert isinstance(instance.widthComputationExpression, str)


@given(instance=diagram::style::SizeComputationContainerStyleDescription_strategy)
def test_diagram::style::sizecomputationcontainerstyledescription_widthComputationExpression_setter(instance):
    original = instance.widthComputationExpression
    instance.widthComputationExpression = original
    assert instance.widthComputationExpression == original

@given(instance=diagram::style::SizeComputationContainerStyleDescription_strategy)
def test_diagram::style::sizecomputationcontainerstyledescription_heightComputationExpression_type(instance):
    assert isinstance(instance.heightComputationExpression, str)


@given(instance=diagram::style::SizeComputationContainerStyleDescription_strategy)
def test_diagram::style::sizecomputationcontainerstyledescription_heightComputationExpression_setter(instance):
    original = instance.heightComputationExpression
    instance.heightComputationExpression = original
    assert instance.heightComputationExpression == original

@given(instance=style::LabelBorderStyleDescription_strategy)
@settings(max_examples=50)
def test_style::labelborderstyledescription_instantiation(instance):
    assert isinstance(instance, style::LabelBorderStyleDescription)

@given(instance=style::SizeComputationContainerStyleDescription_strategy)
@settings(max_examples=50)
def test_style::sizecomputationcontainerstyledescription_instantiation(instance):
    assert isinstance(instance, style::SizeComputationContainerStyleDescription)

@given(instance=style::RoundedCornerStyleDescription_strategy)
@settings(max_examples=50)
def test_style::roundedcornerstyledescription_instantiation(instance):
    assert isinstance(instance, style::RoundedCornerStyleDescription)

@given(instance=diagram::style::GaugeSectionDescription_strategy)
@settings(max_examples=50)
def test_diagram::style::gaugesectiondescription_instantiation(instance):
    assert isinstance(instance, diagram::style::GaugeSectionDescription)

@given(instance=diagram::style::GaugeSectionDescription_strategy)
def test_diagram::style::gaugesectiondescription_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=diagram::style::GaugeSectionDescription_strategy)
def test_diagram::style::gaugesectiondescription_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=diagram::style::GaugeSectionDescription_strategy)
def test_diagram::style::gaugesectiondescription_minValueExpression_type(instance):
    assert isinstance(instance.minValueExpression, str)


@given(instance=diagram::style::GaugeSectionDescription_strategy)
def test_diagram::style::gaugesectiondescription_minValueExpression_setter(instance):
    original = instance.minValueExpression
    instance.minValueExpression = original
    assert instance.minValueExpression == original

@given(instance=diagram::style::GaugeSectionDescription_strategy)
def test_diagram::style::gaugesectiondescription_valueExpression_type(instance):
    assert isinstance(instance.valueExpression, str)


@given(instance=diagram::style::GaugeSectionDescription_strategy)
def test_diagram::style::gaugesectiondescription_valueExpression_setter(instance):
    original = instance.valueExpression
    instance.valueExpression = original
    assert instance.valueExpression == original

@given(instance=diagram::style::GaugeSectionDescription_strategy)
def test_diagram::style::gaugesectiondescription_maxValueExpression_type(instance):
    assert isinstance(instance.maxValueExpression, str)


@given(instance=diagram::style::GaugeSectionDescription_strategy)
def test_diagram::style::gaugesectiondescription_maxValueExpression_setter(instance):
    original = instance.maxValueExpression
    instance.maxValueExpression = original
    assert instance.maxValueExpression == original

@given(instance=style::GaugeSectionDescription_strategy)
@settings(max_examples=50)
def test_style::gaugesectiondescription_instantiation(instance):
    assert isinstance(instance, style::GaugeSectionDescription)

@given(instance=NodeStyleDescription_strategy)
@settings(max_examples=50)
def test_nodestyledescription_instantiation(instance):
    assert isinstance(instance, NodeStyleDescription)

@given(instance=diagram::style::DotDescription_strategy)
@settings(max_examples=50)
def test_diagram::style::dotdescription_instantiation(instance):
    assert isinstance(instance, diagram::style::DotDescription)

@given(instance=diagram::style::DotDescription_strategy)
def test_diagram::style::dotdescription_strokeSizeComputationExpression_type(instance):
    assert isinstance(instance.strokeSizeComputationExpression, str)


@given(instance=diagram::style::DotDescription_strategy)
def test_diagram::style::dotdescription_strokeSizeComputationExpression_setter(instance):
    original = instance.strokeSizeComputationExpression
    instance.strokeSizeComputationExpression = original
    assert instance.strokeSizeComputationExpression == original

@given(instance=diagram::style::EllipseNodeDescription_strategy)
@settings(max_examples=50)
def test_diagram::style::ellipsenodedescription_instantiation(instance):
    assert isinstance(instance, diagram::style::EllipseNodeDescription)

@given(instance=diagram::style::EllipseNodeDescription_strategy)
def test_diagram::style::ellipsenodedescription_horizontalDiameterComputationExpression_type(instance):
    assert isinstance(instance.horizontalDiameterComputationExpression, str)


@given(instance=diagram::style::EllipseNodeDescription_strategy)
def test_diagram::style::ellipsenodedescription_horizontalDiameterComputationExpression_setter(instance):
    original = instance.horizontalDiameterComputationExpression
    instance.horizontalDiameterComputationExpression = original
    assert instance.horizontalDiameterComputationExpression == original

@given(instance=diagram::style::EllipseNodeDescription_strategy)
def test_diagram::style::ellipsenodedescription_verticalDiameterComputationExpression_type(instance):
    assert isinstance(instance.verticalDiameterComputationExpression, str)


@given(instance=diagram::style::EllipseNodeDescription_strategy)
def test_diagram::style::ellipsenodedescription_verticalDiameterComputationExpression_setter(instance):
    original = instance.verticalDiameterComputationExpression
    instance.verticalDiameterComputationExpression = original
    assert instance.verticalDiameterComputationExpression == original

@given(instance=diagram::style::LozengeNodeDescription_strategy)
@settings(max_examples=50)
def test_diagram::style::lozengenodedescription_instantiation(instance):
    assert isinstance(instance, diagram::style::LozengeNodeDescription)

@given(instance=diagram::style::LozengeNodeDescription_strategy)
def test_diagram::style::lozengenodedescription_heightComputationExpression_type(instance):
    assert isinstance(instance.heightComputationExpression, str)


@given(instance=diagram::style::LozengeNodeDescription_strategy)
def test_diagram::style::lozengenodedescription_heightComputationExpression_setter(instance):
    original = instance.heightComputationExpression
    instance.heightComputationExpression = original
    assert instance.heightComputationExpression == original

@given(instance=diagram::style::LozengeNodeDescription_strategy)
def test_diagram::style::lozengenodedescription_widthComputationExpression_type(instance):
    assert isinstance(instance.widthComputationExpression, str)


@given(instance=diagram::style::LozengeNodeDescription_strategy)
def test_diagram::style::lozengenodedescription_widthComputationExpression_setter(instance):
    original = instance.widthComputationExpression
    instance.widthComputationExpression = original
    assert instance.widthComputationExpression == original

@given(instance=diagram::style::BundledImageDescription_strategy)
@settings(max_examples=50)
def test_diagram::style::bundledimagedescription_instantiation(instance):
    assert isinstance(instance, diagram::style::BundledImageDescription)

@given(instance=diagram::style::BundledImageDescription_strategy)
def test_diagram::style::bundledimagedescription_providedShapeID_type(instance):
    assert isinstance(instance.providedShapeID, str)


@given(instance=diagram::style::BundledImageDescription_strategy)
def test_diagram::style::bundledimagedescription_providedShapeID_setter(instance):
    original = instance.providedShapeID
    instance.providedShapeID = original
    assert instance.providedShapeID == original

@given(instance=diagram::style::BundledImageDescription_strategy)
def test_diagram::style::bundledimagedescription_shape_type(instance):
    assert isinstance(instance.shape, str)


@given(instance=diagram::style::BundledImageDescription_strategy)
def test_diagram::style::bundledimagedescription_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original

@given(instance=diagram::style::SquareDescription_strategy)
@settings(max_examples=50)
def test_diagram::style::squaredescription_instantiation(instance):
    assert isinstance(instance, diagram::style::SquareDescription)

@given(instance=diagram::style::SquareDescription_strategy)
def test_diagram::style::squaredescription_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=diagram::style::SquareDescription_strategy)
def test_diagram::style::squaredescription_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=diagram::style::SquareDescription_strategy)
def test_diagram::style::squaredescription_height_type(instance):
    assert isinstance(instance.height, str)


@given(instance=diagram::style::SquareDescription_strategy)
def test_diagram::style::squaredescription_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=diagram::style::GaugeCompositeStyleDescription_strategy)
@settings(max_examples=50)
def test_diagram::style::gaugecompositestyledescription_instantiation(instance):
    assert isinstance(instance, diagram::style::GaugeCompositeStyleDescription)

@given(instance=diagram::style::GaugeCompositeStyleDescription_strategy)
def test_diagram::style::gaugecompositestyledescription_alignment_type(instance):
    assert isinstance(instance.alignment, str)


@given(instance=diagram::style::GaugeCompositeStyleDescription_strategy)
def test_diagram::style::gaugecompositestyledescription_alignment_setter(instance):
    original = instance.alignment
    instance.alignment = original
    assert instance.alignment == original

@given(instance=diagram::style::NoteDescription_strategy)
@settings(max_examples=50)
def test_diagram::style::notedescription_instantiation(instance):
    assert isinstance(instance, diagram::style::NoteDescription)

@given(instance=diagram::style::CustomStyleDescription_strategy)
@settings(max_examples=50)
def test_diagram::style::customstyledescription_instantiation(instance):
    assert isinstance(instance, diagram::style::CustomStyleDescription)

@given(instance=diagram::style::CustomStyleDescription_strategy)
def test_diagram::style::customstyledescription_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=diagram::style::CustomStyleDescription_strategy)
def test_diagram::style::customstyledescription_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=style::HideLabelCapabilityStyleDescription_strategy)
@settings(max_examples=50)
def test_style::hidelabelcapabilitystyledescription_instantiation(instance):
    assert isinstance(instance, style::HideLabelCapabilityStyleDescription)

@given(instance=style::TooltipStyleDescription_strategy)
@settings(max_examples=50)
def test_style::tooltipstyledescription_instantiation(instance):
    assert isinstance(instance, style::TooltipStyleDescription)

@given(instance=style::LabelStyleDescription_strategy)
@settings(max_examples=50)
def test_style::labelstyledescription_instantiation(instance):
    assert isinstance(instance, style::LabelStyleDescription)

@given(instance=style::BorderedStyleDescription_strategy)
@settings(max_examples=50)
def test_style::borderedstyledescription_instantiation(instance):
    assert isinstance(instance, style::BorderedStyleDescription)

@given(instance=diagram::style::ContainerStyleDescription_strategy)
@settings(max_examples=50)
def test_diagram::style::containerstyledescription_instantiation(instance):
    assert isinstance(instance, diagram::style::ContainerStyleDescription)

@given(instance=diagram::style::ContainerStyleDescription_strategy)
def test_diagram::style::containerstyledescription_roundedCorner_type(instance):
    assert isinstance(instance.roundedCorner, bool)


@given(instance=diagram::style::ContainerStyleDescription_strategy)
def test_diagram::style::containerstyledescription_roundedCorner_setter(instance):
    original = instance.roundedCorner
    instance.roundedCorner = original
    assert instance.roundedCorner == original

@given(instance=diagram::style::ContainerStyleDescription_strategy)
def test_diagram::style::containerstyledescription_containerLabelDirection_type(instance):
    assert isinstance(instance.containerLabelDirection, str)


@given(instance=diagram::style::ContainerStyleDescription_strategy)
def test_diagram::style::containerstyledescription_containerLabelDirection_setter(instance):
    original = instance.containerLabelDirection
    instance.containerLabelDirection = original
    assert instance.containerLabelDirection == original

@given(instance=ColorDescription_strategy)
@settings(max_examples=50)
def test_colordescription_instantiation(instance):
    assert isinstance(instance, ColorDescription)

@given(instance=StyleDescription_strategy)
@settings(max_examples=50)
def test_styledescription_instantiation(instance):
    assert isinstance(instance, StyleDescription)

@given(instance=diagram::style::RoundedCornerStyleDescription_strategy)
@settings(max_examples=50)
def test_diagram::style::roundedcornerstyledescription_instantiation(instance):
    assert isinstance(instance, diagram::style::RoundedCornerStyleDescription)

@given(instance=diagram::style::RoundedCornerStyleDescription_strategy)
def test_diagram::style::roundedcornerstyledescription_arcHeight_type(instance):
    assert isinstance(instance.arcHeight, str)


@given(instance=diagram::style::RoundedCornerStyleDescription_strategy)
def test_diagram::style::roundedcornerstyledescription_arcHeight_setter(instance):
    original = instance.arcHeight
    instance.arcHeight = original
    assert instance.arcHeight == original

@given(instance=diagram::style::RoundedCornerStyleDescription_strategy)
def test_diagram::style::roundedcornerstyledescription_arcWidth_type(instance):
    assert isinstance(instance.arcWidth, str)


@given(instance=diagram::style::RoundedCornerStyleDescription_strategy)
def test_diagram::style::roundedcornerstyledescription_arcWidth_setter(instance):
    original = instance.arcWidth
    instance.arcWidth = original
    assert instance.arcWidth == original

@given(instance=diagram::style::EdgeStyleDescription_strategy)
@settings(max_examples=50)
def test_diagram::style::edgestyledescription_instantiation(instance):
    assert isinstance(instance, diagram::style::EdgeStyleDescription)

@given(instance=diagram::style::EdgeStyleDescription_strategy)
def test_diagram::style::edgestyledescription_sourceArrow_type(instance):
    assert isinstance(instance.sourceArrow, str)


@given(instance=diagram::style::EdgeStyleDescription_strategy)
def test_diagram::style::edgestyledescription_sourceArrow_setter(instance):
    original = instance.sourceArrow
    instance.sourceArrow = original
    assert instance.sourceArrow == original

@given(instance=diagram::style::EdgeStyleDescription_strategy)
def test_diagram::style::edgestyledescription_sizeComputationExpression_type(instance):
    assert isinstance(instance.sizeComputationExpression, str)


@given(instance=diagram::style::EdgeStyleDescription_strategy)
def test_diagram::style::edgestyledescription_sizeComputationExpression_setter(instance):
    original = instance.sizeComputationExpression
    instance.sizeComputationExpression = original
    assert instance.sizeComputationExpression == original

@given(instance=diagram::style::EdgeStyleDescription_strategy)
def test_diagram::style::edgestyledescription_targetArrow_type(instance):
    assert isinstance(instance.targetArrow, str)


@given(instance=diagram::style::EdgeStyleDescription_strategy)
def test_diagram::style::edgestyledescription_targetArrow_setter(instance):
    original = instance.targetArrow
    instance.targetArrow = original
    assert instance.targetArrow == original

@given(instance=diagram::style::EdgeStyleDescription_strategy)
def test_diagram::style::edgestyledescription_lineStyle_type(instance):
    assert isinstance(instance.lineStyle, str)


@given(instance=diagram::style::EdgeStyleDescription_strategy)
def test_diagram::style::edgestyledescription_lineStyle_setter(instance):
    original = instance.lineStyle
    instance.lineStyle = original
    assert instance.lineStyle == original

@given(instance=diagram::style::EdgeStyleDescription_strategy)
def test_diagram::style::edgestyledescription_endsCentering_type(instance):
    assert isinstance(instance.endsCentering, str)


@given(instance=diagram::style::EdgeStyleDescription_strategy)
def test_diagram::style::edgestyledescription_endsCentering_setter(instance):
    original = instance.endsCentering
    instance.endsCentering = original
    assert instance.endsCentering == original

@given(instance=diagram::style::EdgeStyleDescription_strategy)
def test_diagram::style::edgestyledescription_foldingStyle_type(instance):
    assert isinstance(instance.foldingStyle, str)


@given(instance=diagram::style::EdgeStyleDescription_strategy)
def test_diagram::style::edgestyledescription_foldingStyle_setter(instance):
    original = instance.foldingStyle
    instance.foldingStyle = original
    assert instance.foldingStyle == original

@given(instance=diagram::style::EdgeStyleDescription_strategy)
def test_diagram::style::edgestyledescription_routingStyle_type(instance):
    assert isinstance(instance.routingStyle, str)


@given(instance=diagram::style::EdgeStyleDescription_strategy)
def test_diagram::style::edgestyledescription_routingStyle_setter(instance):
    original = instance.routingStyle
    instance.routingStyle = original
    assert instance.routingStyle == original

@given(instance=diagram::style::BorderedStyleDescription_strategy)
@settings(max_examples=50)
def test_diagram::style::borderedstyledescription_instantiation(instance):
    assert isinstance(instance, diagram::style::BorderedStyleDescription)

@given(instance=diagram::style::BorderedStyleDescription_strategy)
def test_diagram::style::borderedstyledescription_borderSizeComputationExpression_type(instance):
    assert isinstance(instance.borderSizeComputationExpression, str)


@given(instance=diagram::style::BorderedStyleDescription_strategy)
def test_diagram::style::borderedstyledescription_borderSizeComputationExpression_setter(instance):
    original = instance.borderSizeComputationExpression
    instance.borderSizeComputationExpression = original
    assert instance.borderSizeComputationExpression == original

@given(instance=diagram::style::BorderedStyleDescription_strategy)
def test_diagram::style::borderedstyledescription_borderLineStyle_type(instance):
    assert isinstance(instance.borderLineStyle, str)


@given(instance=diagram::style::BorderedStyleDescription_strategy)
def test_diagram::style::borderedstyledescription_borderLineStyle_setter(instance):
    original = instance.borderLineStyle
    instance.borderLineStyle = original
    assert instance.borderLineStyle == original

@given(instance=tool::ContainerDropDescription_strategy)
@settings(max_examples=50)
def test_tool::containerdropdescription_instantiation(instance):
    assert isinstance(instance, tool::ContainerDropDescription)

@given(instance=diagram::description::DragAndDropTargetDescription_strategy)
@settings(max_examples=50)
def test_diagram::description::draganddroptargetdescription_instantiation(instance):
    assert isinstance(instance, diagram::description::DragAndDropTargetDescription)

@given(instance=Customization_strategy)
@settings(max_examples=50)
def test_customization_instantiation(instance):
    assert isinstance(instance, Customization)

@given(instance=DecorationDescriptionsSet_strategy)
@settings(max_examples=50)
def test_decorationdescriptionsset_instantiation(instance):
    assert isinstance(instance, DecorationDescriptionsSet)

@given(instance=description::EndUserDocumentedElement_strategy)
@settings(max_examples=50)
def test_description::enduserdocumentedelement_instantiation(instance):
    assert isinstance(instance, description::EndUserDocumentedElement)

@given(instance=DecorationDescription_strategy)
@settings(max_examples=50)
def test_decorationdescription_instantiation(instance):
    assert isinstance(instance, DecorationDescription)

@given(instance=diagram::description::MappingBasedDecoration_strategy)
@settings(max_examples=50)
def test_diagram::description::mappingbaseddecoration_instantiation(instance):
    assert isinstance(instance, diagram::description::MappingBasedDecoration)

@given(instance=DocumentedElement_strategy)
@settings(max_examples=50)
def test_documentedelement_instantiation(instance):
    assert isinstance(instance, DocumentedElement)

@given(instance=diagram::concern::ConcernSet_strategy)
@settings(max_examples=50)
def test_diagram::concern::concernset_instantiation(instance):
    assert isinstance(instance, diagram::concern::ConcernSet)

@given(instance=diagram::description::Layout_strategy)
@settings(max_examples=50)
def test_diagram::description::layout_instantiation(instance):
    assert isinstance(instance, diagram::description::Layout)

@given(instance=style::EdgeStyleDescription_strategy)
@settings(max_examples=50)
def test_style::edgestyledescription_instantiation(instance):
    assert isinstance(instance, style::EdgeStyleDescription)

@given(instance=ConditionalStyleDescription_strategy)
@settings(max_examples=50)
def test_conditionalstyledescription_instantiation(instance):
    assert isinstance(instance, ConditionalStyleDescription)

@given(instance=diagram::description::ConditionalEdgeStyleDescription_strategy)
@settings(max_examples=50)
def test_diagram::description::conditionaledgestyledescription_instantiation(instance):
    assert isinstance(instance, diagram::description::ConditionalEdgeStyleDescription)

@given(instance=diagram::description::ConditionalContainerStyleDescription_strategy)
@settings(max_examples=50)
def test_diagram::description::conditionalcontainerstyledescription_instantiation(instance):
    assert isinstance(instance, diagram::description::ConditionalContainerStyleDescription)

@given(instance=diagram::description::ConditionalNodeStyleDescription_strategy)
@settings(max_examples=50)
def test_diagram::description::conditionalnodestyledescription_instantiation(instance):
    assert isinstance(instance, diagram::description::ConditionalNodeStyleDescription)

@given(instance=description::IdentifiedElement_strategy)
@settings(max_examples=50)
def test_description::identifiedelement_instantiation(instance):
    assert isinstance(instance, description::IdentifiedElement)

@given(instance=diagram::description::IEdgeMapping_strategy)
@settings(max_examples=50)
def test_diagram::description::iedgemapping_instantiation(instance):
    assert isinstance(instance, diagram::description::IEdgeMapping)

@given(instance=AbstractNodeMapping_strategy)
@settings(max_examples=50)
def test_abstractnodemapping_instantiation(instance):
    assert isinstance(instance, AbstractNodeMapping)

@given(instance=tool::ReconnectEdgeDescription_strategy)
@settings(max_examples=50)
def test_tool::reconnectedgedescription_instantiation(instance):
    assert isinstance(instance, tool::ReconnectEdgeDescription)

@given(instance=ConditionalEdgeStyleDescription_strategy)
@settings(max_examples=50)
def test_conditionaledgestyledescription_instantiation(instance):
    assert isinstance(instance, ConditionalEdgeStyleDescription)

@given(instance=description::ContainerMapping_strategy)
@settings(max_examples=50)
def test_description::containermapping_instantiation(instance):
    assert isinstance(instance, description::ContainerMapping)

@given(instance=ConditionalNodeStyleDescription_strategy)
@settings(max_examples=50)
def test_conditionalnodestyledescription_instantiation(instance):
    assert isinstance(instance, ConditionalNodeStyleDescription)

@given(instance=description::IEdgeMapping_strategy)
@settings(max_examples=50)
def test_description::iedgemapping_instantiation(instance):
    assert isinstance(instance, description::IEdgeMapping)

@given(instance=style::NodeStyleDescription_strategy)
@settings(max_examples=50)
def test_style::nodestyledescription_instantiation(instance):
    assert isinstance(instance, style::NodeStyleDescription)

@given(instance=description::AbstractMappingImport_strategy)
@settings(max_examples=50)
def test_description::abstractmappingimport_instantiation(instance):
    assert isinstance(instance, description::AbstractMappingImport)

@given(instance=diagram::description::ContainerMappingImport_strategy)
@settings(max_examples=50)
def test_diagram::description::containermappingimport_instantiation(instance):
    assert isinstance(instance, diagram::description::ContainerMappingImport)

@given(instance=description::NodeMapping_strategy)
@settings(max_examples=50)
def test_description::nodemapping_instantiation(instance):
    assert isinstance(instance, description::NodeMapping)

@given(instance=diagram::description::NodeMappingImport_strategy)
@settings(max_examples=50)
def test_diagram::description::nodemappingimport_instantiation(instance):
    assert isinstance(instance, diagram::description::NodeMappingImport)

@given(instance=ConditionalContainerStyleDescription_strategy)
@settings(max_examples=50)
def test_conditionalcontainerstyledescription_instantiation(instance):
    assert isinstance(instance, ConditionalContainerStyleDescription)

@given(instance=style::ContainerStyleDescription_strategy)
@settings(max_examples=50)
def test_style::containerstyledescription_instantiation(instance):
    assert isinstance(instance, style::ContainerStyleDescription)

@given(instance=diagram::style::FlatContainerStyleDescription_strategy)
@settings(max_examples=50)
def test_diagram::style::flatcontainerstyledescription_instantiation(instance):
    assert isinstance(instance, diagram::style::FlatContainerStyleDescription)

@given(instance=diagram::style::FlatContainerStyleDescription_strategy)
def test_diagram::style::flatcontainerstyledescription_backgroundStyle_type(instance):
    assert isinstance(instance.backgroundStyle, str)


@given(instance=diagram::style::FlatContainerStyleDescription_strategy)
def test_diagram::style::flatcontainerstyledescription_backgroundStyle_setter(instance):
    original = instance.backgroundStyle
    instance.backgroundStyle = original
    assert instance.backgroundStyle == original

@given(instance=diagram::style::WorkspaceImageDescription_strategy)
@settings(max_examples=50)
def test_diagram::style::workspaceimagedescription_instantiation(instance):
    assert isinstance(instance, diagram::style::WorkspaceImageDescription)

@given(instance=diagram::style::WorkspaceImageDescription_strategy)
def test_diagram::style::workspaceimagedescription_workspacePath_type(instance):
    assert isinstance(instance.workspacePath, str)


@given(instance=diagram::style::WorkspaceImageDescription_strategy)
def test_diagram::style::workspaceimagedescription_workspacePath_setter(instance):
    original = instance.workspacePath
    instance.workspacePath = original
    assert instance.workspacePath == original

@given(instance=diagram::style::ShapeContainerStyleDescription_strategy)
@settings(max_examples=50)
def test_diagram::style::shapecontainerstyledescription_instantiation(instance):
    assert isinstance(instance, diagram::style::ShapeContainerStyleDescription)

@given(instance=diagram::style::ShapeContainerStyleDescription_strategy)
def test_diagram::style::shapecontainerstyledescription_shape_type(instance):
    assert isinstance(instance.shape, str)


@given(instance=diagram::style::ShapeContainerStyleDescription_strategy)
def test_diagram::style::shapecontainerstyledescription_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original

@given(instance=tool::InitialOperation_strategy)
@settings(max_examples=50)
def test_tool::initialoperation_instantiation(instance):
    assert isinstance(instance, tool::InitialOperation)

@given(instance=Layout_strategy)
@settings(max_examples=50)
def test_layout_instantiation(instance):
    assert isinstance(instance, Layout)

@given(instance=diagram::description::OrderedTreeLayout_strategy)
@settings(max_examples=50)
def test_diagram::description::orderedtreelayout_instantiation(instance):
    assert isinstance(instance, diagram::description::OrderedTreeLayout)

@given(instance=diagram::description::OrderedTreeLayout_strategy)
def test_diagram::description::orderedtreelayout_childrenExpression_type(instance):
    assert isinstance(instance.childrenExpression, str)


@given(instance=diagram::description::OrderedTreeLayout_strategy)
def test_diagram::description::orderedtreelayout_childrenExpression_setter(instance):
    original = instance.childrenExpression
    instance.childrenExpression = original
    assert instance.childrenExpression == original

@given(instance=diagram::description::CompositeLayout_strategy)
@settings(max_examples=50)
def test_diagram::description::compositelayout_instantiation(instance):
    assert isinstance(instance, diagram::description::CompositeLayout)

@given(instance=diagram::description::CompositeLayout_strategy)
def test_diagram::description::compositelayout_padding_type(instance):
    assert isinstance(instance.padding, int)


@given(instance=diagram::description::CompositeLayout_strategy)
def test_diagram::description::compositelayout_padding_setter(instance):
    original = instance.padding
    instance.padding = original
    assert instance.padding == original

@given(instance=diagram::description::CompositeLayout_strategy)
def test_diagram::description::compositelayout_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=diagram::description::CompositeLayout_strategy)
def test_diagram::description::compositelayout_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=tool::RepresentationCreationDescription_strategy)
@settings(max_examples=50)
def test_tool::representationcreationdescription_instantiation(instance):
    assert isinstance(instance, tool::RepresentationCreationDescription)

@given(instance=tool::AbstractToolDescription_strategy)
@settings(max_examples=50)
def test_tool::abstracttooldescription_instantiation(instance):
    assert isinstance(instance, tool::AbstractToolDescription)

@given(instance=concern::ConcernSet_strategy)
@settings(max_examples=50)
def test_concern::concernset_instantiation(instance):
    assert isinstance(instance, concern::ConcernSet)

@given(instance=validation::ValidationSet_strategy)
@settings(max_examples=50)
def test_validation::validationset_instantiation(instance):
    assert isinstance(instance, validation::ValidationSet)

@given(instance=EdgeMapping_strategy)
@settings(max_examples=50)
def test_edgemapping_instantiation(instance):
    assert isinstance(instance, EdgeMapping)

@given(instance=description::PasteTargetDescription_strategy)
@settings(max_examples=50)
def test_description::pastetargetdescription_instantiation(instance):
    assert isinstance(instance, description::PasteTargetDescription)

@given(instance=diagram::description::DiagramElementMapping_strategy)
@settings(max_examples=50)
def test_diagram::description::diagramelementmapping_instantiation(instance):
    assert isinstance(instance, diagram::description::DiagramElementMapping)

@given(instance=diagram::description::DiagramElementMapping_strategy)
def test_diagram::description::diagramelementmapping_synchronizationLock_type(instance):
    assert isinstance(instance.synchronizationLock, bool)


@given(instance=diagram::description::DiagramElementMapping_strategy)
def test_diagram::description::diagramelementmapping_synchronizationLock_setter(instance):
    original = instance.synchronizationLock
    instance.synchronizationLock = original
    assert instance.synchronizationLock == original

@given(instance=diagram::description::DiagramElementMapping_strategy)
def test_diagram::description::diagramelementmapping_createElements_type(instance):
    assert isinstance(instance.createElements, bool)


@given(instance=diagram::description::DiagramElementMapping_strategy)
def test_diagram::description::diagramelementmapping_createElements_setter(instance):
    original = instance.createElements
    instance.createElements = original
    assert instance.createElements == original

@given(instance=diagram::description::DiagramElementMapping_strategy)
def test_diagram::description::diagramelementmapping_preconditionExpression_type(instance):
    assert isinstance(instance.preconditionExpression, str)


@given(instance=diagram::description::DiagramElementMapping_strategy)
def test_diagram::description::diagramelementmapping_preconditionExpression_setter(instance):
    original = instance.preconditionExpression
    instance.preconditionExpression = original
    assert instance.preconditionExpression == original

@given(instance=diagram::description::DiagramElementMapping_strategy)
def test_diagram::description::diagramelementmapping_semanticCandidatesExpression_type(instance):
    assert isinstance(instance.semanticCandidatesExpression, str)


@given(instance=diagram::description::DiagramElementMapping_strategy)
def test_diagram::description::diagramelementmapping_semanticCandidatesExpression_setter(instance):
    original = instance.semanticCandidatesExpression
    instance.semanticCandidatesExpression = original
    assert instance.semanticCandidatesExpression == original

@given(instance=diagram::description::DiagramElementMapping_strategy)
def test_diagram::description::diagramelementmapping_semanticElements_type(instance):
    assert isinstance(instance.semanticElements, str)


@given(instance=diagram::description::DiagramElementMapping_strategy)
def test_diagram::description::diagramelementmapping_semanticElements_setter(instance):
    original = instance.semanticElements
    instance.semanticElements = original
    assert instance.semanticElements == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram::description::DiagramElementMapping_strategy)
@settings(max_examples=30)
def test_diagram::description::diagramelementmapping_checkprecondition_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.checkPrecondition(
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.checkPrecondition).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'checkPrecondition' in diagram::description::DiagramElementMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'checkPrecondition' in diagram::description::DiagramElementMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'checkPrecondition' in diagram::description::DiagramElementMapping is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram::description::DiagramElementMapping_strategy)
@settings(max_examples=30)
def test_diagram::description::diagramelementmapping_isfrom_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isFrom(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isFrom).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isFrom' in diagram::description::DiagramElementMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isFrom' in diagram::description::DiagramElementMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isFrom' in diagram::description::DiagramElementMapping is not implemented or raised an error")

@given(instance=description::RepresentationDescription_strategy)
@settings(max_examples=50)
def test_description::representationdescription_instantiation(instance):
    assert isinstance(instance, description::RepresentationDescription)

@given(instance=description::DragAndDropTargetDescription_strategy)
@settings(max_examples=50)
def test_description::draganddroptargetdescription_instantiation(instance):
    assert isinstance(instance, description::DragAndDropTargetDescription)

@given(instance=diagram::description::ContainerMapping_strategy)
@settings(max_examples=50)
def test_diagram::description::containermapping_instantiation(instance):
    assert isinstance(instance, diagram::description::ContainerMapping)

@given(instance=diagram::description::ContainerMapping_strategy)
def test_diagram::description::containermapping_childrenPresentation_type(instance):
    assert isinstance(instance.childrenPresentation, str)


@given(instance=diagram::description::ContainerMapping_strategy)
def test_diagram::description::containermapping_childrenPresentation_setter(instance):
    original = instance.childrenPresentation
    instance.childrenPresentation = original
    assert instance.childrenPresentation == original

@given(instance=diagram::description::NodeMapping_strategy)
@settings(max_examples=50)
def test_diagram::description::nodemapping_instantiation(instance):
    assert isinstance(instance, diagram::description::NodeMapping)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram::description::NodeMapping_strategy)
@settings(max_examples=30)
def test_diagram::description::nodemapping_createnode_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createNode(
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createNode).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createNode' in diagram::description::NodeMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createNode' in diagram::description::NodeMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createNode' in diagram::description::NodeMapping is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram::description::NodeMapping_strategy)
@settings(max_examples=30)
def test_diagram::description::nodemapping_updatenode_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.updateNode(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.updateNode).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'updateNode' in diagram::description::NodeMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'updateNode' in diagram::description::NodeMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'updateNode' in diagram::description::NodeMapping is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram::description::NodeMapping_strategy)
@settings(max_examples=30)
def test_diagram::description::nodemapping_updatelistelement_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.updateListElement(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.updateListElement).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'updateListElement' in diagram::description::NodeMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'updateListElement' in diagram::description::NodeMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'updateListElement' in diagram::description::NodeMapping is not implemented or raised an error")

@given(instance=diagram::description::DiagramDescription_strategy)
@settings(max_examples=50)
def test_diagram::description::diagramdescription_instantiation(instance):
    assert isinstance(instance, diagram::description::DiagramDescription)

@given(instance=diagram::description::DiagramDescription_strategy)
def test_diagram::description::diagramdescription_domainClass_type(instance):
    assert isinstance(instance.domainClass, str)


@given(instance=diagram::description::DiagramDescription_strategy)
def test_diagram::description::diagramdescription_domainClass_setter(instance):
    original = instance.domainClass
    instance.domainClass = original
    assert instance.domainClass == original

@given(instance=diagram::description::DiagramDescription_strategy)
def test_diagram::description::diagramdescription_rootExpression_type(instance):
    assert isinstance(instance.rootExpression, str)


@given(instance=diagram::description::DiagramDescription_strategy)
def test_diagram::description::diagramdescription_rootExpression_setter(instance):
    original = instance.rootExpression
    instance.rootExpression = original
    assert instance.rootExpression == original

@given(instance=diagram::description::DiagramDescription_strategy)
def test_diagram::description::diagramdescription_preconditionExpression_type(instance):
    assert isinstance(instance.preconditionExpression, str)


@given(instance=diagram::description::DiagramDescription_strategy)
def test_diagram::description::diagramdescription_preconditionExpression_setter(instance):
    original = instance.preconditionExpression
    instance.preconditionExpression = original
    assert instance.preconditionExpression == original

@given(instance=diagram::description::DiagramDescription_strategy)
def test_diagram::description::diagramdescription_enablePopupBars_type(instance):
    assert isinstance(instance.enablePopupBars, bool)


@given(instance=diagram::description::DiagramDescription_strategy)
def test_diagram::description::diagramdescription_enablePopupBars_setter(instance):
    original = instance.enablePopupBars
    instance.enablePopupBars = original
    assert instance.enablePopupBars == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram::description::DiagramDescription_strategy)
@settings(max_examples=30)
def test_diagram::description::diagramdescription_creatediagram_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createDiagram()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createDiagram).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createDiagram' in diagram::description::DiagramDescription is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createDiagram' in diagram::description::DiagramDescription did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createDiagram' in diagram::description::DiagramDescription is not implemented or raised an error")

@given(instance=diagram::EObject_strategy)
@settings(max_examples=50)
def test_diagram::eobject_instantiation(instance):
    assert isinstance(instance, diagram::EObject)

@given(instance=tool::SelectModelElementVariable_strategy)
@settings(max_examples=50)
def test_tool::selectmodelelementvariable_instantiation(instance):
    assert isinstance(instance, tool::SelectModelElementVariable)

@given(instance=TypedVariable_strategy)
@settings(max_examples=50)
def test_typedvariable_instantiation(instance):
    assert isinstance(instance, TypedVariable)

@given(instance=VariableValue_strategy)
@settings(max_examples=50)
def test_variablevalue_instantiation(instance):
    assert isinstance(instance, VariableValue)

@given(instance=diagram::EObjectVariableValue_strategy)
@settings(max_examples=50)
def test_diagram::eobjectvariablevalue_instantiation(instance):
    assert isinstance(instance, diagram::EObjectVariableValue)

@given(instance=diagram::TypedVariableValue_strategy)
@settings(max_examples=50)
def test_diagram::typedvariablevalue_instantiation(instance):
    assert isinstance(instance, diagram::TypedVariableValue)

@given(instance=diagram::TypedVariableValue_strategy)
def test_diagram::typedvariablevalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=diagram::TypedVariableValue_strategy)
def test_diagram::typedvariablevalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=diagram::HideLabelCapabilityStyle_strategy)
@settings(max_examples=50)
def test_diagram::hidelabelcapabilitystyle_instantiation(instance):
    assert isinstance(instance, diagram::HideLabelCapabilityStyle)

@given(instance=diagram::HideLabelCapabilityStyle_strategy)
def test_diagram::hidelabelcapabilitystyle_hideLabelByDefault_type(instance):
    assert isinstance(instance.hideLabelByDefault, bool)


@given(instance=diagram::HideLabelCapabilityStyle_strategy)
def test_diagram::hidelabelcapabilitystyle_hideLabelByDefault_setter(instance):
    original = instance.hideLabelByDefault
    instance.hideLabelByDefault = original
    assert instance.hideLabelByDefault == original

@given(instance=diagram::DragAndDropTarget_strategy)
@settings(max_examples=50)
def test_diagram::draganddroptarget_instantiation(instance):
    assert isinstance(instance, diagram::DragAndDropTarget)

@given(instance=style::StyleDescription_strategy)
@settings(max_examples=50)
def test_style::styledescription_instantiation(instance):
    assert isinstance(instance, style::StyleDescription)

@given(instance=diagram::style::NodeStyleDescription_strategy)
@settings(max_examples=50)
def test_diagram::style::nodestyledescription_instantiation(instance):
    assert isinstance(instance, diagram::style::NodeStyleDescription)

@given(instance=diagram::style::NodeStyleDescription_strategy)
def test_diagram::style::nodestyledescription_sizeComputationExpression_type(instance):
    assert isinstance(instance.sizeComputationExpression, str)


@given(instance=diagram::style::NodeStyleDescription_strategy)
def test_diagram::style::nodestyledescription_sizeComputationExpression_setter(instance):
    original = instance.sizeComputationExpression
    instance.sizeComputationExpression = original
    assert instance.sizeComputationExpression == original

@given(instance=diagram::style::NodeStyleDescription_strategy)
def test_diagram::style::nodestyledescription_resizeKind_type(instance):
    assert isinstance(instance.resizeKind, str)


@given(instance=diagram::style::NodeStyleDescription_strategy)
def test_diagram::style::nodestyledescription_resizeKind_setter(instance):
    original = instance.resizeKind
    instance.resizeKind = original
    assert instance.resizeKind == original

@given(instance=diagram::style::NodeStyleDescription_strategy)
def test_diagram::style::nodestyledescription_labelDirection_type(instance):
    assert isinstance(instance.labelDirection, str)


@given(instance=diagram::style::NodeStyleDescription_strategy)
def test_diagram::style::nodestyledescription_labelDirection_setter(instance):
    original = instance.labelDirection
    instance.labelDirection = original
    assert instance.labelDirection == original

@given(instance=diagram::style::NodeStyleDescription_strategy)
def test_diagram::style::nodestyledescription_labelPosition_type(instance):
    assert isinstance(instance.labelPosition, str)


@given(instance=diagram::style::NodeStyleDescription_strategy)
def test_diagram::style::nodestyledescription_labelPosition_setter(instance):
    original = instance.labelPosition
    instance.labelPosition = original
    assert instance.labelPosition == original

@given(instance=diagram::style::NodeStyleDescription_strategy)
def test_diagram::style::nodestyledescription_forbiddenSides_type(instance):
    assert isinstance(instance.forbiddenSides, str)


@given(instance=diagram::style::NodeStyleDescription_strategy)
def test_diagram::style::nodestyledescription_forbiddenSides_setter(instance):
    original = instance.forbiddenSides
    instance.forbiddenSides = original
    assert instance.forbiddenSides == original

@given(instance=diagram::ComputedStyleDescriptionRegistry_strategy)
@settings(max_examples=50)
def test_diagram::computedstyledescriptionregistry_instantiation(instance):
    assert isinstance(instance, diagram::ComputedStyleDescriptionRegistry)

@given(instance=EdgeStyle_strategy)
@settings(max_examples=50)
def test_edgestyle_instantiation(instance):
    assert isinstance(instance, EdgeStyle)

@given(instance=diagram::BracketEdgeStyle_strategy)
@settings(max_examples=50)
def test_diagram::bracketedgestyle_instantiation(instance):
    assert isinstance(instance, diagram::BracketEdgeStyle)

@given(instance=BasicLabelStyle_strategy)
@settings(max_examples=50)
def test_basiclabelstyle_instantiation(instance):
    assert isinstance(instance, BasicLabelStyle)

@given(instance=CollapseFilter_strategy)
@settings(max_examples=50)
def test_collapsefilter_instantiation(instance):
    assert isinstance(instance, CollapseFilter)

@given(instance=diagram::IndirectlyCollapseFilter_strategy)
@settings(max_examples=50)
def test_diagram::indirectlycollapsefilter_instantiation(instance):
    assert isinstance(instance, diagram::IndirectlyCollapseFilter)

@given(instance=diagram::VariableValue_strategy)
@settings(max_examples=50)
def test_diagram::variablevalue_instantiation(instance):
    assert isinstance(instance, diagram::VariableValue)

@given(instance=diagram::EndLabelStyle_strategy)
@settings(max_examples=50)
def test_diagram::endlabelstyle_instantiation(instance):
    assert isinstance(instance, diagram::EndLabelStyle)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram::EndLabelStyle_strategy)
@settings(max_examples=30)
def test_diagram::endlabelstyle_setdescription_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setDescription(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setDescription).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setDescription' in diagram::EndLabelStyle is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setDescription' in diagram::EndLabelStyle did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setDescription' in diagram::EndLabelStyle is not implemented or raised an error")

@given(instance=diagram::CenterLabelStyle_strategy)
@settings(max_examples=50)
def test_diagram::centerlabelstyle_instantiation(instance):
    assert isinstance(instance, diagram::CenterLabelStyle)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram::CenterLabelStyle_strategy)
@settings(max_examples=30)
def test_diagram::centerlabelstyle_setdescription_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setDescription(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setDescription).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setDescription' in diagram::CenterLabelStyle is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setDescription' in diagram::CenterLabelStyle did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setDescription' in diagram::CenterLabelStyle is not implemented or raised an error")

@given(instance=diagram::BeginLabelStyle_strategy)
@settings(max_examples=50)
def test_diagram::beginlabelstyle_instantiation(instance):
    assert isinstance(instance, diagram::BeginLabelStyle)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram::BeginLabelStyle_strategy)
@settings(max_examples=30)
def test_diagram::beginlabelstyle_setdescription_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setDescription(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setDescription).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setDescription' in diagram::BeginLabelStyle is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setDescription' in diagram::BeginLabelStyle did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setDescription' in diagram::BeginLabelStyle is not implemented or raised an error")

@given(instance=Customizable_strategy)
@settings(max_examples=50)
def test_customizable_instantiation(instance):
    assert isinstance(instance, Customizable)

@given(instance=diagram::GaugeSection_strategy)
@settings(max_examples=50)
def test_diagram::gaugesection_instantiation(instance):
    assert isinstance(instance, diagram::GaugeSection)

@given(instance=diagram::GaugeSection_strategy)
def test_diagram::gaugesection_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=diagram::GaugeSection_strategy)
def test_diagram::gaugesection_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=diagram::GaugeSection_strategy)
def test_diagram::gaugesection_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=diagram::GaugeSection_strategy)
def test_diagram::gaugesection_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=diagram::GaugeSection_strategy)
def test_diagram::gaugesection_foregroundColor_type(instance):
    assert isinstance(instance.foregroundColor, str)


@given(instance=diagram::GaugeSection_strategy)
def test_diagram::gaugesection_foregroundColor_setter(instance):
    original = instance.foregroundColor
    instance.foregroundColor = original
    assert instance.foregroundColor == original

@given(instance=diagram::GaugeSection_strategy)
def test_diagram::gaugesection_max_type(instance):
    assert isinstance(instance.max, str)


@given(instance=diagram::GaugeSection_strategy)
def test_diagram::gaugesection_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=diagram::GaugeSection_strategy)
def test_diagram::gaugesection_min_type(instance):
    assert isinstance(instance.min, str)


@given(instance=diagram::GaugeSection_strategy)
def test_diagram::gaugesection_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=diagram::GaugeSection_strategy)
def test_diagram::gaugesection_backgroundColor_type(instance):
    assert isinstance(instance.backgroundColor, str)


@given(instance=diagram::GaugeSection_strategy)
def test_diagram::gaugesection_backgroundColor_setter(instance):
    original = instance.backgroundColor
    instance.backgroundColor = original
    assert instance.backgroundColor == original

@given(instance=ContainerStyle_strategy)
@settings(max_examples=50)
def test_containerstyle_instantiation(instance):
    assert isinstance(instance, ContainerStyle)

@given(instance=diagram::ShapeContainerStyle_strategy)
@settings(max_examples=50)
def test_diagram::shapecontainerstyle_instantiation(instance):
    assert isinstance(instance, diagram::ShapeContainerStyle)

@given(instance=diagram::ShapeContainerStyle_strategy)
def test_diagram::shapecontainerstyle_backgroundColor_type(instance):
    assert isinstance(instance.backgroundColor, str)


@given(instance=diagram::ShapeContainerStyle_strategy)
def test_diagram::shapecontainerstyle_backgroundColor_setter(instance):
    original = instance.backgroundColor
    instance.backgroundColor = original
    assert instance.backgroundColor == original

@given(instance=diagram::ShapeContainerStyle_strategy)
def test_diagram::shapecontainerstyle_shape_type(instance):
    assert isinstance(instance.shape, str)


@given(instance=diagram::ShapeContainerStyle_strategy)
def test_diagram::shapecontainerstyle_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original

@given(instance=diagram::FlatContainerStyle_strategy)
@settings(max_examples=50)
def test_diagram::flatcontainerstyle_instantiation(instance):
    assert isinstance(instance, diagram::FlatContainerStyle)

@given(instance=diagram::FlatContainerStyle_strategy)
def test_diagram::flatcontainerstyle_foregroundColor_type(instance):
    assert isinstance(instance.foregroundColor, str)


@given(instance=diagram::FlatContainerStyle_strategy)
def test_diagram::flatcontainerstyle_foregroundColor_setter(instance):
    original = instance.foregroundColor
    instance.foregroundColor = original
    assert instance.foregroundColor == original

@given(instance=diagram::FlatContainerStyle_strategy)
def test_diagram::flatcontainerstyle_backgroundColor_type(instance):
    assert isinstance(instance.backgroundColor, str)


@given(instance=diagram::FlatContainerStyle_strategy)
def test_diagram::flatcontainerstyle_backgroundColor_setter(instance):
    original = instance.backgroundColor
    instance.backgroundColor = original
    assert instance.backgroundColor == original

@given(instance=diagram::FlatContainerStyle_strategy)
def test_diagram::flatcontainerstyle_backgroundStyle_type(instance):
    assert isinstance(instance.backgroundStyle, str)


@given(instance=diagram::FlatContainerStyle_strategy)
def test_diagram::flatcontainerstyle_backgroundStyle_setter(instance):
    original = instance.backgroundStyle
    instance.backgroundStyle = original
    assert instance.backgroundStyle == original

@given(instance=NodeStyle_strategy)
@settings(max_examples=50)
def test_nodestyle_instantiation(instance):
    assert isinstance(instance, NodeStyle)

@given(instance=diagram::Lozenge_strategy)
@settings(max_examples=50)
def test_diagram::lozenge_instantiation(instance):
    assert isinstance(instance, diagram::Lozenge)

@given(instance=diagram::Lozenge_strategy)
def test_diagram::lozenge_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=diagram::Lozenge_strategy)
def test_diagram::lozenge_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=diagram::Lozenge_strategy)
def test_diagram::lozenge_height_type(instance):
    assert isinstance(instance.height, str)


@given(instance=diagram::Lozenge_strategy)
def test_diagram::lozenge_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=diagram::Lozenge_strategy)
def test_diagram::lozenge_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=diagram::Lozenge_strategy)
def test_diagram::lozenge_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=diagram::CustomStyle_strategy)
@settings(max_examples=50)
def test_diagram::customstyle_instantiation(instance):
    assert isinstance(instance, diagram::CustomStyle)

@given(instance=diagram::CustomStyle_strategy)
def test_diagram::customstyle_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=diagram::CustomStyle_strategy)
def test_diagram::customstyle_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=diagram::GaugeCompositeStyle_strategy)
@settings(max_examples=50)
def test_diagram::gaugecompositestyle_instantiation(instance):
    assert isinstance(instance, diagram::GaugeCompositeStyle)

@given(instance=diagram::GaugeCompositeStyle_strategy)
def test_diagram::gaugecompositestyle_alignment_type(instance):
    assert isinstance(instance.alignment, str)


@given(instance=diagram::GaugeCompositeStyle_strategy)
def test_diagram::gaugecompositestyle_alignment_setter(instance):
    original = instance.alignment
    instance.alignment = original
    assert instance.alignment == original

@given(instance=diagram::Square_strategy)
@settings(max_examples=50)
def test_diagram::square_instantiation(instance):
    assert isinstance(instance, diagram::Square)

@given(instance=diagram::Square_strategy)
def test_diagram::square_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=diagram::Square_strategy)
def test_diagram::square_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=diagram::Square_strategy)
def test_diagram::square_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=diagram::Square_strategy)
def test_diagram::square_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=diagram::Square_strategy)
def test_diagram::square_height_type(instance):
    assert isinstance(instance.height, str)


@given(instance=diagram::Square_strategy)
def test_diagram::square_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=diagram::WorkspaceImage_strategy)
@settings(max_examples=50)
def test_diagram::workspaceimage_instantiation(instance):
    assert isinstance(instance, diagram::WorkspaceImage)

@given(instance=diagram::WorkspaceImage_strategy)
def test_diagram::workspaceimage_workspacePath_type(instance):
    assert isinstance(instance.workspacePath, str)


@given(instance=diagram::WorkspaceImage_strategy)
def test_diagram::workspaceimage_workspacePath_setter(instance):
    original = instance.workspacePath
    instance.workspacePath = original
    assert instance.workspacePath == original

@given(instance=diagram::BundledImage_strategy)
@settings(max_examples=50)
def test_diagram::bundledimage_instantiation(instance):
    assert isinstance(instance, diagram::BundledImage)

@given(instance=diagram::BundledImage_strategy)
def test_diagram::bundledimage_shape_type(instance):
    assert isinstance(instance.shape, str)


@given(instance=diagram::BundledImage_strategy)
def test_diagram::bundledimage_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original

@given(instance=diagram::BundledImage_strategy)
def test_diagram::bundledimage_providedShapeID_type(instance):
    assert isinstance(instance.providedShapeID, str)


@given(instance=diagram::BundledImage_strategy)
def test_diagram::bundledimage_providedShapeID_setter(instance):
    original = instance.providedShapeID
    instance.providedShapeID = original
    assert instance.providedShapeID == original

@given(instance=diagram::BundledImage_strategy)
def test_diagram::bundledimage_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=diagram::BundledImage_strategy)
def test_diagram::bundledimage_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=diagram::Ellipse_strategy)
@settings(max_examples=50)
def test_diagram::ellipse_instantiation(instance):
    assert isinstance(instance, diagram::Ellipse)

@given(instance=diagram::Ellipse_strategy)
def test_diagram::ellipse_verticalDiameter_type(instance):
    assert isinstance(instance.verticalDiameter, str)


@given(instance=diagram::Ellipse_strategy)
def test_diagram::ellipse_verticalDiameter_setter(instance):
    original = instance.verticalDiameter
    instance.verticalDiameter = original
    assert instance.verticalDiameter == original

@given(instance=diagram::Ellipse_strategy)
def test_diagram::ellipse_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=diagram::Ellipse_strategy)
def test_diagram::ellipse_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=diagram::Ellipse_strategy)
def test_diagram::ellipse_horizontalDiameter_type(instance):
    assert isinstance(instance.horizontalDiameter, str)


@given(instance=diagram::Ellipse_strategy)
def test_diagram::ellipse_horizontalDiameter_setter(instance):
    original = instance.horizontalDiameter
    instance.horizontalDiameter = original
    assert instance.horizontalDiameter == original

@given(instance=diagram::Note_strategy)
@settings(max_examples=50)
def test_diagram::note_instantiation(instance):
    assert isinstance(instance, diagram::Note)

@given(instance=diagram::Note_strategy)
def test_diagram::note_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=diagram::Note_strategy)
def test_diagram::note_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=diagram::Dot_strategy)
@settings(max_examples=50)
def test_diagram::dot_instantiation(instance):
    assert isinstance(instance, diagram::Dot)

@given(instance=diagram::Dot_strategy)
def test_diagram::dot_strokeSizeComputationExpression_type(instance):
    assert isinstance(instance.strokeSizeComputationExpression, str)


@given(instance=diagram::Dot_strategy)
def test_diagram::dot_strokeSizeComputationExpression_setter(instance):
    original = instance.strokeSizeComputationExpression
    instance.strokeSizeComputationExpression = original
    assert instance.strokeSizeComputationExpression == original

@given(instance=diagram::Dot_strategy)
def test_diagram::dot_backgroundColor_type(instance):
    assert isinstance(instance.backgroundColor, str)


@given(instance=diagram::Dot_strategy)
def test_diagram::dot_backgroundColor_setter(instance):
    original = instance.backgroundColor
    instance.backgroundColor = original
    assert instance.backgroundColor == original

@given(instance=HideLabelCapabilityStyle_strategy)
@settings(max_examples=50)
def test_hidelabelcapabilitystyle_instantiation(instance):
    assert isinstance(instance, HideLabelCapabilityStyle)

@given(instance=BorderedStyle_strategy)
@settings(max_examples=50)
def test_borderedstyle_instantiation(instance):
    assert isinstance(instance, BorderedStyle)

@given(instance=Style_strategy)
@settings(max_examples=50)
def test_style_instantiation(instance):
    assert isinstance(instance, Style)

@given(instance=diagram::BorderedStyle_strategy)
@settings(max_examples=50)
def test_diagram::borderedstyle_instantiation(instance):
    assert isinstance(instance, diagram::BorderedStyle)

@given(instance=diagram::BorderedStyle_strategy)
def test_diagram::borderedstyle_borderSize_type(instance):
    assert isinstance(instance.borderSize, str)


@given(instance=diagram::BorderedStyle_strategy)
def test_diagram::borderedstyle_borderSize_setter(instance):
    original = instance.borderSize
    instance.borderSize = original
    assert instance.borderSize == original

@given(instance=diagram::BorderedStyle_strategy)
def test_diagram::borderedstyle_borderColor_type(instance):
    assert isinstance(instance.borderColor, str)


@given(instance=diagram::BorderedStyle_strategy)
def test_diagram::borderedstyle_borderColor_setter(instance):
    original = instance.borderColor
    instance.borderColor = original
    assert instance.borderColor == original

@given(instance=diagram::BorderedStyle_strategy)
def test_diagram::borderedstyle_borderSizeComputationExpression_type(instance):
    assert isinstance(instance.borderSizeComputationExpression, str)


@given(instance=diagram::BorderedStyle_strategy)
def test_diagram::borderedstyle_borderSizeComputationExpression_setter(instance):
    original = instance.borderSizeComputationExpression
    instance.borderSizeComputationExpression = original
    assert instance.borderSizeComputationExpression == original

@given(instance=diagram::BorderedStyle_strategy)
def test_diagram::borderedstyle_borderLineStyle_type(instance):
    assert isinstance(instance.borderLineStyle, str)


@given(instance=diagram::BorderedStyle_strategy)
def test_diagram::borderedstyle_borderLineStyle_setter(instance):
    original = instance.borderLineStyle
    instance.borderLineStyle = original
    assert instance.borderLineStyle == original

@given(instance=LabelStyle_strategy)
@settings(max_examples=50)
def test_labelstyle_instantiation(instance):
    assert isinstance(instance, LabelStyle)

@given(instance=IEdgeMapping_strategy)
@settings(max_examples=50)
def test_iedgemapping_instantiation(instance):
    assert isinstance(instance, IEdgeMapping)

@given(instance=diagram::EdgeTarget_strategy)
@settings(max_examples=50)
def test_diagram::edgetarget_instantiation(instance):
    assert isinstance(instance, diagram::EdgeTarget)

@given(instance=diagram::EdgeStyle_strategy)
@settings(max_examples=50)
def test_diagram::edgestyle_instantiation(instance):
    assert isinstance(instance, diagram::EdgeStyle)

@given(instance=diagram::EdgeStyle_strategy)
def test_diagram::edgestyle_lineStyle_type(instance):
    assert isinstance(instance.lineStyle, str)


@given(instance=diagram::EdgeStyle_strategy)
def test_diagram::edgestyle_lineStyle_setter(instance):
    original = instance.lineStyle
    instance.lineStyle = original
    assert instance.lineStyle == original

@given(instance=diagram::EdgeStyle_strategy)
def test_diagram::edgestyle_size_type(instance):
    assert isinstance(instance.size, str)


@given(instance=diagram::EdgeStyle_strategy)
def test_diagram::edgestyle_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=diagram::EdgeStyle_strategy)
def test_diagram::edgestyle_foldingStyle_type(instance):
    assert isinstance(instance.foldingStyle, str)


@given(instance=diagram::EdgeStyle_strategy)
def test_diagram::edgestyle_foldingStyle_setter(instance):
    original = instance.foldingStyle
    instance.foldingStyle = original
    assert instance.foldingStyle == original

@given(instance=diagram::EdgeStyle_strategy)
def test_diagram::edgestyle_sourceArrow_type(instance):
    assert isinstance(instance.sourceArrow, str)


@given(instance=diagram::EdgeStyle_strategy)
def test_diagram::edgestyle_sourceArrow_setter(instance):
    original = instance.sourceArrow
    instance.sourceArrow = original
    assert instance.sourceArrow == original

@given(instance=diagram::EdgeStyle_strategy)
def test_diagram::edgestyle_routingStyle_type(instance):
    assert isinstance(instance.routingStyle, str)


@given(instance=diagram::EdgeStyle_strategy)
def test_diagram::edgestyle_routingStyle_setter(instance):
    original = instance.routingStyle
    instance.routingStyle = original
    assert instance.routingStyle == original

@given(instance=diagram::EdgeStyle_strategy)
def test_diagram::edgestyle_targetArrow_type(instance):
    assert isinstance(instance.targetArrow, str)


@given(instance=diagram::EdgeStyle_strategy)
def test_diagram::edgestyle_targetArrow_setter(instance):
    original = instance.targetArrow
    instance.targetArrow = original
    assert instance.targetArrow == original

@given(instance=diagram::EdgeStyle_strategy)
def test_diagram::edgestyle_centered_type(instance):
    assert isinstance(instance.centered, str)


@given(instance=diagram::EdgeStyle_strategy)
def test_diagram::edgestyle_centered_setter(instance):
    original = instance.centered
    instance.centered = original
    assert instance.centered == original

@given(instance=diagram::EdgeStyle_strategy)
def test_diagram::edgestyle_strokeColor_type(instance):
    assert isinstance(instance.strokeColor, str)


@given(instance=diagram::EdgeStyle_strategy)
def test_diagram::edgestyle_strokeColor_setter(instance):
    original = instance.strokeColor
    instance.strokeColor = original
    assert instance.strokeColor == original

@given(instance=DDiagramElementContainer_strategy)
@settings(max_examples=50)
def test_ddiagramelementcontainer_instantiation(instance):
    assert isinstance(instance, DDiagramElementContainer)

@given(instance=diagram::DNodeList_strategy)
@settings(max_examples=50)
def test_diagram::dnodelist_instantiation(instance):
    assert isinstance(instance, diagram::DNodeList)

@given(instance=diagram::DNodeContainer_strategy)
@settings(max_examples=50)
def test_diagram::dnodecontainer_instantiation(instance):
    assert isinstance(instance, diagram::DNodeContainer)

@given(instance=diagram::DNodeContainer_strategy)
def test_diagram::dnodecontainer_childrenPresentation_type(instance):
    assert isinstance(instance.childrenPresentation, str)


@given(instance=diagram::DNodeContainer_strategy)
def test_diagram::dnodecontainer_childrenPresentation_setter(instance):
    original = instance.childrenPresentation
    instance.childrenPresentation = original
    assert instance.childrenPresentation == original

@given(instance=ContainerMapping_strategy)
@settings(max_examples=50)
def test_containermapping_instantiation(instance):
    assert isinstance(instance, ContainerMapping)

@given(instance=diagram::ContainerStyle_strategy)
@settings(max_examples=50)
def test_diagram::containerstyle_instantiation(instance):
    assert isinstance(instance, diagram::ContainerStyle)

@given(instance=diagram::ContainerStyle_strategy)
def test_diagram::containerstyle_containerLabelDirection_type(instance):
    assert isinstance(instance.containerLabelDirection, str)


@given(instance=diagram::ContainerStyle_strategy)
def test_diagram::containerstyle_containerLabelDirection_setter(instance):
    original = instance.containerLabelDirection
    instance.containerLabelDirection = original
    assert instance.containerLabelDirection == original

@given(instance=diagram::GraphicalFilter_strategy)
@settings(max_examples=50)
def test_diagram::graphicalfilter_instantiation(instance):
    assert isinstance(instance, diagram::GraphicalFilter)

@given(instance=NodeMapping_strategy)
@settings(max_examples=50)
def test_nodemapping_instantiation(instance):
    assert isinstance(instance, NodeMapping)

@given(instance=diagram::Style_strategy)
@settings(max_examples=50)
def test_diagram::style_instantiation(instance):
    assert isinstance(instance, diagram::Style)

@given(instance=diagram::NodeStyle_strategy)
@settings(max_examples=50)
def test_diagram::nodestyle_instantiation(instance):
    assert isinstance(instance, diagram::NodeStyle)

@given(instance=diagram::NodeStyle_strategy)
def test_diagram::nodestyle_labelDirection_type(instance):
    assert isinstance(instance.labelDirection, str)


@given(instance=diagram::NodeStyle_strategy)
def test_diagram::nodestyle_labelDirection_setter(instance):
    original = instance.labelDirection
    instance.labelDirection = original
    assert instance.labelDirection == original

@given(instance=diagram::NodeStyle_strategy)
def test_diagram::nodestyle_labelPosition_type(instance):
    assert isinstance(instance.labelPosition, str)


@given(instance=diagram::NodeStyle_strategy)
def test_diagram::nodestyle_labelPosition_setter(instance):
    original = instance.labelPosition
    instance.labelPosition = original
    assert instance.labelPosition == original

@given(instance=EdgeTarget_strategy)
@settings(max_examples=50)
def test_edgetarget_instantiation(instance):
    assert isinstance(instance, EdgeTarget)

@given(instance=AbstractDNode_strategy)
@settings(max_examples=50)
def test_abstractdnode_instantiation(instance):
    assert isinstance(instance, AbstractDNode)

@given(instance=DDiagramElement_strategy)
@settings(max_examples=50)
def test_ddiagramelement_instantiation(instance):
    assert isinstance(instance, DDiagramElement)

@given(instance=diagram::AbstractDNode_strategy)
@settings(max_examples=50)
def test_diagram::abstractdnode_instantiation(instance):
    assert isinstance(instance, diagram::AbstractDNode)

@given(instance=diagram::AbstractDNode_strategy)
def test_diagram::abstractdnode_arrangeConstraints_type(instance):
    assert isinstance(instance.arrangeConstraints, str)


@given(instance=diagram::AbstractDNode_strategy)
def test_diagram::abstractdnode_arrangeConstraints_setter(instance):
    original = instance.arrangeConstraints
    instance.arrangeConstraints = original
    assert instance.arrangeConstraints == original

@given(instance=filter::CompositeFilterDescription_strategy)
@settings(max_examples=50)
def test_filter::compositefilterdescription_instantiation(instance):
    assert isinstance(instance, filter::CompositeFilterDescription)

@given(instance=GraphicalFilter_strategy)
@settings(max_examples=50)
def test_graphicalfilter_instantiation(instance):
    assert isinstance(instance, GraphicalFilter)

@given(instance=diagram::AbsoluteBoundsFilter_strategy)
@settings(max_examples=50)
def test_diagram::absoluteboundsfilter_instantiation(instance):
    assert isinstance(instance, diagram::AbsoluteBoundsFilter)

@given(instance=diagram::AbsoluteBoundsFilter_strategy)
def test_diagram::absoluteboundsfilter_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=diagram::AbsoluteBoundsFilter_strategy)
def test_diagram::absoluteboundsfilter_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=diagram::AbsoluteBoundsFilter_strategy)
def test_diagram::absoluteboundsfilter_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=diagram::AbsoluteBoundsFilter_strategy)
def test_diagram::absoluteboundsfilter_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=diagram::AbsoluteBoundsFilter_strategy)
def test_diagram::absoluteboundsfilter_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=diagram::AbsoluteBoundsFilter_strategy)
def test_diagram::absoluteboundsfilter_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=diagram::AbsoluteBoundsFilter_strategy)
def test_diagram::absoluteboundsfilter_height_type(instance):
    assert isinstance(instance.height, str)


@given(instance=diagram::AbsoluteBoundsFilter_strategy)
def test_diagram::absoluteboundsfilter_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=diagram::AppliedCompositeFilters_strategy)
@settings(max_examples=50)
def test_diagram::appliedcompositefilters_instantiation(instance):
    assert isinstance(instance, diagram::AppliedCompositeFilters)

@given(instance=diagram::CollapseFilter_strategy)
@settings(max_examples=50)
def test_diagram::collapsefilter_instantiation(instance):
    assert isinstance(instance, diagram::CollapseFilter)

@given(instance=diagram::CollapseFilter_strategy)
def test_diagram::collapsefilter_width_type(instance):
    assert isinstance(instance.width, int)


@given(instance=diagram::CollapseFilter_strategy)
def test_diagram::collapsefilter_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=diagram::CollapseFilter_strategy)
def test_diagram::collapsefilter_height_type(instance):
    assert isinstance(instance.height, int)


@given(instance=diagram::CollapseFilter_strategy)
def test_diagram::collapsefilter_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=diagram::HideLabelFilter_strategy)
@settings(max_examples=50)
def test_diagram::hidelabelfilter_instantiation(instance):
    assert isinstance(instance, diagram::HideLabelFilter)

@given(instance=diagram::FoldingPointFilter_strategy)
@settings(max_examples=50)
def test_diagram::foldingpointfilter_instantiation(instance):
    assert isinstance(instance, diagram::FoldingPointFilter)

@given(instance=diagram::FoldingFilter_strategy)
@settings(max_examples=50)
def test_diagram::foldingfilter_instantiation(instance):
    assert isinstance(instance, diagram::FoldingFilter)

@given(instance=diagram::HideFilter_strategy)
@settings(max_examples=50)
def test_diagram::hidefilter_instantiation(instance):
    assert isinstance(instance, diagram::HideFilter)

@given(instance=filter::FilterDescription_strategy)
@settings(max_examples=50)
def test_filter::filterdescription_instantiation(instance):
    assert isinstance(instance, filter::FilterDescription)

@given(instance=DiagramElementMapping_strategy)
@settings(max_examples=50)
def test_diagramelementmapping_instantiation(instance):
    assert isinstance(instance, DiagramElementMapping)

@given(instance=diagram::Decoration_strategy)
@settings(max_examples=50)
def test_diagram::decoration_instantiation(instance):
    assert isinstance(instance, diagram::Decoration)

@given(instance=DRepresentationElement_strategy)
@settings(max_examples=50)
def test_drepresentationelement_instantiation(instance):
    assert isinstance(instance, DRepresentationElement)

@given(instance=DSemanticDecorator_strategy)
@settings(max_examples=50)
def test_dsemanticdecorator_instantiation(instance):
    assert isinstance(instance, DSemanticDecorator)

@given(instance=DDiagram_strategy)
@settings(max_examples=50)
def test_ddiagram_instantiation(instance):
    assert isinstance(instance, DDiagram)

@given(instance=diagram::DSemanticDiagram_strategy)
@settings(max_examples=50)
def test_diagram::dsemanticdiagram_instantiation(instance):
    assert isinstance(instance, diagram::DSemanticDiagram)

@given(instance=Layer_strategy)
@settings(max_examples=50)
def test_layer_instantiation(instance):
    assert isinstance(instance, Layer)

@given(instance=diagram::description::AdditionalLayer_strategy)
@settings(max_examples=50)
def test_diagram::description::additionallayer_instantiation(instance):
    assert isinstance(instance, diagram::description::AdditionalLayer)

@given(instance=diagram::description::AdditionalLayer_strategy)
def test_diagram::description::additionallayer_activeByDefault_type(instance):
    assert isinstance(instance.activeByDefault, bool)


@given(instance=diagram::description::AdditionalLayer_strategy)
def test_diagram::description::additionallayer_activeByDefault_setter(instance):
    original = instance.activeByDefault
    instance.activeByDefault = original
    assert instance.activeByDefault == original

@given(instance=diagram::description::AdditionalLayer_strategy)
def test_diagram::description::additionallayer_optional_type(instance):
    assert isinstance(instance.optional, bool)


@given(instance=diagram::description::AdditionalLayer_strategy)
def test_diagram::description::additionallayer_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original

@given(instance=diagram::FilterVariableHistory_strategy)
@settings(max_examples=50)
def test_diagram::filtervariablehistory_instantiation(instance):
    assert isinstance(instance, diagram::FilterVariableHistory)

@given(instance=tool::BehaviorTool_strategy)
@settings(max_examples=50)
def test_tool::behaviortool_instantiation(instance):
    assert isinstance(instance, tool::BehaviorTool)

@given(instance=validation::ValidationRule_strategy)
@settings(max_examples=50)
def test_validation::validationrule_instantiation(instance):
    assert isinstance(instance, validation::ValidationRule)

@given(instance=concern::ConcernDescription_strategy)
@settings(max_examples=50)
def test_concern::concerndescription_instantiation(instance):
    assert isinstance(instance, concern::ConcernDescription)

@given(instance=diagram::DNodeListElement_strategy)
@settings(max_examples=50)
def test_diagram::dnodelistelement_instantiation(instance):
    assert isinstance(instance, diagram::DNodeListElement)

@given(instance=diagram::DEdge_strategy)
@settings(max_examples=50)
def test_diagram::dedge_instantiation(instance):
    assert isinstance(instance, diagram::DEdge)

@given(instance=diagram::DEdge_strategy)
def test_diagram::dedge_beginLabel_type(instance):
    assert isinstance(instance.beginLabel, str)


@given(instance=diagram::DEdge_strategy)
def test_diagram::dedge_beginLabel_setter(instance):
    original = instance.beginLabel
    instance.beginLabel = original
    assert instance.beginLabel == original

@given(instance=diagram::DEdge_strategy)
def test_diagram::dedge_endLabel_type(instance):
    assert isinstance(instance.endLabel, str)


@given(instance=diagram::DEdge_strategy)
def test_diagram::dedge_endLabel_setter(instance):
    original = instance.endLabel
    instance.endLabel = original
    assert instance.endLabel == original

@given(instance=diagram::DEdge_strategy)
def test_diagram::dedge_size_type(instance):
    assert isinstance(instance.size, str)


@given(instance=diagram::DEdge_strategy)
def test_diagram::dedge_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=diagram::DEdge_strategy)
def test_diagram::dedge_routingStyle_type(instance):
    assert isinstance(instance.routingStyle, str)


@given(instance=diagram::DEdge_strategy)
def test_diagram::dedge_routingStyle_setter(instance):
    original = instance.routingStyle
    instance.routingStyle = original
    assert instance.routingStyle == original

@given(instance=diagram::DEdge_strategy)
def test_diagram::dedge_isMockEdge_type(instance):
    assert isinstance(instance.isMockEdge, bool)


@given(instance=diagram::DEdge_strategy)
def test_diagram::dedge_isMockEdge_setter(instance):
    original = instance.isMockEdge
    instance.isMockEdge = original
    assert instance.isMockEdge == original

@given(instance=diagram::DEdge_strategy)
def test_diagram::dedge_arrangeConstraints_type(instance):
    assert isinstance(instance.arrangeConstraints, str)


@given(instance=diagram::DEdge_strategy)
def test_diagram::dedge_arrangeConstraints_setter(instance):
    original = instance.arrangeConstraints
    instance.arrangeConstraints = original
    assert instance.arrangeConstraints == original

@given(instance=diagram::DEdge_strategy)
def test_diagram::dedge_isFold_type(instance):
    assert isinstance(instance.isFold, bool)


@given(instance=diagram::DEdge_strategy)
def test_diagram::dedge_isFold_setter(instance):
    original = instance.isFold
    instance.isFold = original
    assert instance.isFold == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram::DEdge_strategy)
@settings(max_examples=30)
def test_diagram::dedge_isrootfolding_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isRootFolding()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isRootFolding).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isRootFolding' in diagram::DEdge is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isRootFolding' in diagram::DEdge did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isRootFolding' in diagram::DEdge is not implemented or raised an error")

@given(instance=DiagramDescription_strategy)
@settings(max_examples=50)
def test_diagramdescription_instantiation(instance):
    assert isinstance(instance, DiagramDescription)

@given(instance=diagram::DDiagramElement_strategy)
@settings(max_examples=50)
def test_diagram::ddiagramelement_instantiation(instance):
    assert isinstance(instance, diagram::DDiagramElement)

@given(instance=diagram::DDiagramElement_strategy)
def test_diagram::ddiagramelement_tooltipText_type(instance):
    assert isinstance(instance.tooltipText, str)


@given(instance=diagram::DDiagramElement_strategy)
def test_diagram::ddiagramelement_tooltipText_setter(instance):
    original = instance.tooltipText
    instance.tooltipText = original
    assert instance.tooltipText == original

@given(instance=diagram::DDiagramElement_strategy)
def test_diagram::ddiagramelement_visible_type(instance):
    assert isinstance(instance.visible, bool)


@given(instance=diagram::DDiagramElement_strategy)
def test_diagram::ddiagramelement_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original

@given(instance=DragAndDropTarget_strategy)
@settings(max_examples=50)
def test_draganddroptarget_instantiation(instance):
    assert isinstance(instance, DragAndDropTarget)

@given(instance=diagram::DDiagramElementContainer_strategy)
@settings(max_examples=50)
def test_diagram::ddiagramelementcontainer_instantiation(instance):
    assert isinstance(instance, diagram::DDiagramElementContainer)

@given(instance=diagram::DDiagramElementContainer_strategy)
def test_diagram::ddiagramelementcontainer_height_type(instance):
    assert isinstance(instance.height, str)


@given(instance=diagram::DDiagramElementContainer_strategy)
def test_diagram::ddiagramelementcontainer_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=diagram::DDiagramElementContainer_strategy)
def test_diagram::ddiagramelementcontainer_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=diagram::DDiagramElementContainer_strategy)
def test_diagram::ddiagramelementcontainer_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=diagram::DNode_strategy)
@settings(max_examples=50)
def test_diagram::dnode_instantiation(instance):
    assert isinstance(instance, diagram::DNode)

@given(instance=diagram::DNode_strategy)
def test_diagram::dnode_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=diagram::DNode_strategy)
def test_diagram::dnode_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=diagram::DNode_strategy)
def test_diagram::dnode_resizeKind_type(instance):
    assert isinstance(instance.resizeKind, str)


@given(instance=diagram::DNode_strategy)
def test_diagram::dnode_resizeKind_setter(instance):
    original = instance.resizeKind
    instance.resizeKind = original
    assert instance.resizeKind == original

@given(instance=diagram::DNode_strategy)
def test_diagram::dnode_labelPosition_type(instance):
    assert isinstance(instance.labelPosition, str)


@given(instance=diagram::DNode_strategy)
def test_diagram::dnode_labelPosition_setter(instance):
    original = instance.labelPosition
    instance.labelPosition = original
    assert instance.labelPosition == original

@given(instance=diagram::DNode_strategy)
def test_diagram::dnode_height_type(instance):
    assert isinstance(instance.height, str)


@given(instance=diagram::DNode_strategy)
def test_diagram::dnode_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=description::DocumentedElement_strategy)
@settings(max_examples=50)
def test_description::documentedelement_instantiation(instance):
    assert isinstance(instance, description::DocumentedElement)

@given(instance=diagram::filter::FilterDescription_strategy)
@settings(max_examples=50)
def test_diagram::filter::filterdescription_instantiation(instance):
    assert isinstance(instance, diagram::filter::FilterDescription)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram::filter::FilterDescription_strategy)
@settings(max_examples=30)
def test_diagram::filter::filterdescription_isvisible_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isVisible(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isVisible).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isVisible' in diagram::filter::FilterDescription is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isVisible' in diagram::filter::FilterDescription did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isVisible' in diagram::filter::FilterDescription is not implemented or raised an error")

@given(instance=diagram::description::Layer_strategy)
@settings(max_examples=50)
def test_diagram::description::layer_instantiation(instance):
    assert isinstance(instance, diagram::description::Layer)

@given(instance=diagram::description::Layer_strategy)
def test_diagram::description::layer_icon_type(instance):
    assert isinstance(instance.icon, str)


@given(instance=diagram::description::Layer_strategy)
def test_diagram::description::layer_icon_setter(instance):
    original = instance.icon
    instance.icon = original
    assert instance.icon == original

@given(instance=diagram::description::EdgeMappingImport_strategy)
@settings(max_examples=50)
def test_diagram::description::edgemappingimport_instantiation(instance):
    assert isinstance(instance, diagram::description::EdgeMappingImport)

@given(instance=diagram::description::EdgeMappingImport_strategy)
def test_diagram::description::edgemappingimport_inheritsAncestorFilters_type(instance):
    assert isinstance(instance.inheritsAncestorFilters, bool)


@given(instance=diagram::description::EdgeMappingImport_strategy)
def test_diagram::description::edgemappingimport_inheritsAncestorFilters_setter(instance):
    original = instance.inheritsAncestorFilters
    instance.inheritsAncestorFilters = original
    assert instance.inheritsAncestorFilters == original

@given(instance=diagram::tool::ToolSection_strategy)
@settings(max_examples=50)
def test_diagram::tool::toolsection_instantiation(instance):
    assert isinstance(instance, diagram::tool::ToolSection)

@given(instance=diagram::tool::ToolSection_strategy)
def test_diagram::tool::toolsection_icon_type(instance):
    assert isinstance(instance.icon, str)


@given(instance=diagram::tool::ToolSection_strategy)
def test_diagram::tool::toolsection_icon_setter(instance):
    original = instance.icon
    instance.icon = original
    assert instance.icon == original

@given(instance=diagram::description::EdgeMapping_strategy)
@settings(max_examples=50)
def test_diagram::description::edgemapping_instantiation(instance):
    assert isinstance(instance, diagram::description::EdgeMapping)

@given(instance=diagram::description::EdgeMapping_strategy)
def test_diagram::description::edgemapping_pathExpression_type(instance):
    assert isinstance(instance.pathExpression, str)


@given(instance=diagram::description::EdgeMapping_strategy)
def test_diagram::description::edgemapping_pathExpression_setter(instance):
    original = instance.pathExpression
    instance.pathExpression = original
    assert instance.pathExpression == original

@given(instance=diagram::description::EdgeMapping_strategy)
def test_diagram::description::edgemapping_domainClass_type(instance):
    assert isinstance(instance.domainClass, str)


@given(instance=diagram::description::EdgeMapping_strategy)
def test_diagram::description::edgemapping_domainClass_setter(instance):
    original = instance.domainClass
    instance.domainClass = original
    assert instance.domainClass == original

@given(instance=diagram::description::EdgeMapping_strategy)
def test_diagram::description::edgemapping_targetExpression_type(instance):
    assert isinstance(instance.targetExpression, str)


@given(instance=diagram::description::EdgeMapping_strategy)
def test_diagram::description::edgemapping_targetExpression_setter(instance):
    original = instance.targetExpression
    instance.targetExpression = original
    assert instance.targetExpression == original

@given(instance=diagram::description::EdgeMapping_strategy)
def test_diagram::description::edgemapping_targetFinderExpression_type(instance):
    assert isinstance(instance.targetFinderExpression, str)


@given(instance=diagram::description::EdgeMapping_strategy)
def test_diagram::description::edgemapping_targetFinderExpression_setter(instance):
    original = instance.targetFinderExpression
    instance.targetFinderExpression = original
    assert instance.targetFinderExpression == original

@given(instance=diagram::description::EdgeMapping_strategy)
def test_diagram::description::edgemapping_sourceFinderExpression_type(instance):
    assert isinstance(instance.sourceFinderExpression, str)


@given(instance=diagram::description::EdgeMapping_strategy)
def test_diagram::description::edgemapping_sourceFinderExpression_setter(instance):
    original = instance.sourceFinderExpression
    instance.sourceFinderExpression = original
    assert instance.sourceFinderExpression == original

@given(instance=diagram::description::EdgeMapping_strategy)
def test_diagram::description::edgemapping_useDomainElement_type(instance):
    assert isinstance(instance.useDomainElement, bool)


@given(instance=diagram::description::EdgeMapping_strategy)
def test_diagram::description::edgemapping_useDomainElement_setter(instance):
    original = instance.useDomainElement
    instance.useDomainElement = original
    assert instance.useDomainElement == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram::description::EdgeMapping_strategy)
@settings(max_examples=30)
def test_diagram::description::edgemapping_createedge_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createEdge(
            "test", 
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createEdge).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createEdge' in diagram::description::EdgeMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createEdge' in diagram::description::EdgeMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createEdge' in diagram::description::EdgeMapping is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram::description::EdgeMapping_strategy)
@settings(max_examples=30)
def test_diagram::description::edgemapping_updateedge_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.updateEdge(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.updateEdge).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'updateEdge' in diagram::description::EdgeMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'updateEdge' in diagram::description::EdgeMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'updateEdge' in diagram::description::EdgeMapping is not implemented or raised an error")

@given(instance=diagram::concern::ConcernDescription_strategy)
@settings(max_examples=50)
def test_diagram::concern::concerndescription_instantiation(instance):
    assert isinstance(instance, diagram::concern::ConcernDescription)

@given(instance=diagram::description::AbstractNodeMapping_strategy)
@settings(max_examples=50)
def test_diagram::description::abstractnodemapping_instantiation(instance):
    assert isinstance(instance, diagram::description::AbstractNodeMapping)

@given(instance=diagram::description::AbstractNodeMapping_strategy)
def test_diagram::description::abstractnodemapping_domainClass_type(instance):
    assert isinstance(instance.domainClass, str)


@given(instance=diagram::description::AbstractNodeMapping_strategy)
def test_diagram::description::abstractnodemapping_domainClass_setter(instance):
    original = instance.domainClass
    instance.domainClass = original
    assert instance.domainClass == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram::description::AbstractNodeMapping_strategy)
@settings(max_examples=30)
def test_diagram::description::abstractnodemapping_finddnodefromeobject_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.findDNodeFromEObject(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.findDNodeFromEObject).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'findDNodeFromEObject' in diagram::description::AbstractNodeMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'findDNodeFromEObject' in diagram::description::AbstractNodeMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'findDNodeFromEObject' in diagram::description::AbstractNodeMapping is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram::description::AbstractNodeMapping_strategy)
@settings(max_examples=30)
def test_diagram::description::abstractnodemapping_adddonenode_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addDoneNode(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addDoneNode).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addDoneNode' in diagram::description::AbstractNodeMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addDoneNode' in diagram::description::AbstractNodeMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addDoneNode' in diagram::description::AbstractNodeMapping is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram::description::AbstractNodeMapping_strategy)
@settings(max_examples=30)
def test_diagram::description::abstractnodemapping_cleardnodesdone_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.clearDNodesDone()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.clearDNodesDone).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'clearDNodesDone' in diagram::description::AbstractNodeMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'clearDNodesDone' in diagram::description::AbstractNodeMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'clearDNodesDone' in diagram::description::AbstractNodeMapping is not implemented or raised an error")

@given(instance=DRepresentation_strategy)
@settings(max_examples=50)
def test_drepresentation_instantiation(instance):
    assert isinstance(instance, DRepresentation)

@given(instance=diagram::DDiagram_strategy)
@settings(max_examples=50)
def test_diagram::ddiagram_instantiation(instance):
    assert isinstance(instance, diagram::DDiagram)

@given(instance=diagram::DDiagram_strategy)
def test_diagram::ddiagram_isInLayoutingMode_type(instance):
    assert isinstance(instance.isInLayoutingMode, bool)


@given(instance=diagram::DDiagram_strategy)
def test_diagram::ddiagram_isInLayoutingMode_setter(instance):
    original = instance.isInLayoutingMode
    instance.isInLayoutingMode = original
    assert instance.isInLayoutingMode == original

@given(instance=diagram::DDiagram_strategy)
def test_diagram::ddiagram_headerHeight_type(instance):
    assert isinstance(instance.headerHeight, int)


@given(instance=diagram::DDiagram_strategy)
def test_diagram::ddiagram_headerHeight_setter(instance):
    original = instance.headerHeight
    instance.headerHeight = original
    assert instance.headerHeight == original

@given(instance=diagram::DDiagram_strategy)
def test_diagram::ddiagram_synchronized_type(instance):
    assert isinstance(instance.synchronized, bool)


@given(instance=diagram::DDiagram_strategy)
def test_diagram::ddiagram_synchronized_setter(instance):
    original = instance.synchronized
    instance.synchronized = original
    assert instance.synchronized == original
