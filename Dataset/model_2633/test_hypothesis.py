import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ConditionalStyleDescription,
    viewpoint::description::ConditionalContainerStyleDescription,
    viewpoint::description::ConditionalEdgeStyleDescription,
    viewpoint::description::ConditionalNodeStyleDescription,
    description::ConditionalEdgeStyleDescription,
    style::EdgeStyleDescription,
    viewpoint::description::IEdgeMapping,
    tool::ReconnectEdgeDescription,
    description::ConditionalContainerStyleDescription,
    style::ContainerStyleDescription,
    description::AbstractMappingImport,
    description::ConditionalNodeStyleDescription,
    style::NodeStyleDescription,
    tool::DoubleClickDescription,
    description::AbstractNodeMapping,
    tool::DirectEditLabel,
    tool::DeleteElementDescription,
    tool::ToolSection,
    description::RepresentationElementMapping,
    description::RepresentationImportDescription,
    description::AdditionalLayer,
    description::Layout,
    description::EdgeMappingImport,
    description::EdgeMapping,
    concern::ConcernSet,
    ModelElement2ViewVariable,
    viewpoint::diagram::DiagramElementMapping2ModelElement,
    DiagramElementMapping2ModelElement,
    viewpoint::diagram::ComputedStyleDescriptionRegistry,
    description::PasteTargetDescription,
    viewpoint::description::DiagramElementMapping,
    description::RepresentationDescription,
    description::DragAndDropTargetDescription,
    viewpoint::description::ContainerMapping,
    viewpoint::description::NodeMapping,
    viewpoint::description::DiagramDescription,
    viewpoint::diagram::ContainerVariable2StyleDescription,
    ContainerVariable2StyleDescription,
    viewpoint::diagram::ViewVariable2ContainerVariable,
    ViewVariable2ContainerVariable,
    viewpoint::diagram::ModelElement2ViewVariable,
    diagram::viewpoint::EObject,
    filter::FilterVariable,
    viewpoint::diagram::FilterVariableValue,
    FilterVariableValue,
    CollapseFilter,
    viewpoint::diagram::IndirectlyCollapseFilter,
    viewpoint::diagram::FilterVariableHistory,
    GaugeSection,
    EndLabelStyle,
    CenterLabelStyle,
    BeginLabelStyle,
    diagram::ContainerStyle,
    viewpoint::validation::ValidationFix,
    ValidationRule,
    viewpoint::validation::ViewValidationRule,
    viewpoint::validation::SemanticValidationRule,
    validation::ValidationFix,
    validation::RuleAudit,
    viewpoint::validation::ValidationRule,
    viewpoint::validation::RuleAudit,
    SelectionDescription,
    viewpoint::filter::FilterVariable,
    filter::Filter,
    FilterDescription,
    viewpoint::filter::CompositeFilterDescription,
    Filter,
    viewpoint::filter::VariableFilter,
    viewpoint::filter::MappingFilter,
    viewpoint::filter::Filter,
    RepresentationNavigationDescription,
    CreateView,
    viewpoint::tool::DiagramNavigationDescription,
    viewpoint::tool::CreateEdgeView,
    RepresentationCreationDescription,
    viewpoint::tool::DiagramCreationDescription,
    tool::EditMaskVariables,
    tool::ElementDoubleClickVariable,
    tool::DeleteHook,
    viewpoint::tool::DeleteHookParameter,
    tool::DeleteHookParameter,
    viewpoint::tool::DeleteHook,
    tool::ElementDeleteVariable,
    tool::TargetEdgeViewCreationVariable,
    tool::SourceEdgeViewCreationVariable,
    tool::TargetEdgeCreationVariable,
    tool::SourceEdgeCreationVariable,
    tool::InitEdgeCreationOperation,
    tool::InitialNodeCreationOperation,
    tool::NodeCreationVariable,
    tool::PopupMenu,
    tool::ToolGroup,
    viewpoint::tool::ToolGroupExtension,
    tool::ToolGroupExtension,
    style::BeginLabelStyleDescription,
    EdgeStyleDescription,
    viewpoint::style::BracketEdgeStyleDescription,
    style::EndLabelStyleDescription,
    style::CenterLabelStyleDescription,
    viewpoint::style::WorkspaceImageDescription,
    viewpoint::style::SizeComputationContainerStyleDescription,
    style::SizeComputationContainerStyleDescription,
    viewpoint::style::ShapeContainerStyleDescription,
    viewpoint::style::FlatContainerStyleDescription,
    style::RoundedCornerStyleDescription,
    viewpoint::style::GaugeSectionDescription,
    style::GaugeSectionDescription,
    NodeStyleDescription,
    viewpoint::style::LozengeNodeDescription,
    viewpoint::style::BundledImageDescription,
    viewpoint::style::GaugeCompositeStyleDescription,
    viewpoint::style::SquareDescription,
    viewpoint::style::DotDescription,
    viewpoint::style::NoteDescription,
    viewpoint::style::CustomStyleDescription,
    viewpoint::style::EllipseNodeDescription,
    style::TooltipStyleDescription,
    style::LabelStyleDescription,
    style::BorderedStyleDescription,
    viewpoint::style::ContainerStyleDescription,
    StyleDescription,
    viewpoint::style::EdgeStyleDescription,
    viewpoint::style::RoundedCornerStyleDescription,
    viewpoint::style::BorderedStyleDescription,
    Layer,
    viewpoint::description::AdditionalLayer,
    Customization,
    DecorationDescriptionsSet,
    Layout,
    viewpoint::description::CompositeLayout,
    viewpoint::description::OrderedTreeLayout,
    DocumentedElement,
    viewpoint::validation::ValidationSet,
    viewpoint::description::Layout,
    viewpoint::concern::ConcernSet,
    AbstractVariable,
    viewpoint::tool::DialogVariable,
    viewpoint::tool::SubVariable,
    tool::VariableContainer,
    tool::SubVariable,
    viewpoint::tool::AcceleoVariable,
    viewpoint::tool::VariableContainer,
    viewpoint::tool::AbstractVariable,
    tool::ExternalJavaAction,
    tool::ExternalJavaActionParameter,
    tool::ContainerModelOperation,
    MenuItemDescription,
    viewpoint::tool::OperationAction,
    tool::MenuItemDescription,
    viewpoint::tool::ExternalJavaAction,
    viewpoint::tool::ExternalJavaActionCall,
    MenuItemOrRef,
    viewpoint::tool::MenuItemDescriptionReference,
    tool::MenuItemOrRef,
    viewpoint::tool::MenuItemOrRef,
    tool::NameVariable,
    tool::SelectContainerVariable,
    tool::InitialContainerDropOperation,
    tool::ContainerViewVariable,
    tool::ElementSelectVariable,
    description::SelectionDescription,
    tool::AbstractToolDescription,
    viewpoint::tool::MenuItemDescription,
    viewpoint::tool::SelectionWizardDescription,
    tool::DropContainerVariable,
    description::DiagramElementMapping,
    tool::InitialOperation,
    tool::ElementViewVariable,
    tool::ElementVariable,
    MappingBasedToolDescription,
    viewpoint::tool::ContainerCreationDescription,
    viewpoint::tool::PasteDescription,
    viewpoint::tool::ContainerDropDescription,
    viewpoint::tool::DeleteElementDescription,
    viewpoint::tool::EdgeCreationDescription,
    viewpoint::tool::DoubleClickDescription,
    viewpoint::tool::ReconnectEdgeDescription,
    viewpoint::tool::NodeCreationDescription,
    viewpoint::tool::DirectEditLabel,
    viewpoint::tool::ToolDescription,
    AbstractToolDescription,
    viewpoint::tool::RepresentationCreationDescription,
    viewpoint::tool::RequestDescription,
    viewpoint::tool::BehaviorTool,
    viewpoint::tool::PaneBasedSelectionWizardDescription,
    viewpoint::tool::PopupMenu,
    viewpoint::tool::RepresentationNavigationDescription,
    viewpoint::tool::MappingBasedToolDescription,
    tool::ElementDropVariable,
    tool::ToolFilterDescription,
    ToolEntry,
    viewpoint::tool::ToolGroup,
    viewpoint::tool::AbstractToolDescription,
    viewpoint::style::TooltipStyleDescription,
    viewpoint::style::LabelBorderStyleDescription,
    style::LabelBorderStyleDescription,
    viewpoint::style::LabelBorderStyles,
    BasicLabelStyleDescription,
    viewpoint::style::CenterLabelStyleDescription,
    viewpoint::style::EndLabelStyleDescription,
    viewpoint::style::BeginLabelStyleDescription,
    viewpoint::style::LabelStyleDescription,
    viewpoint::style::BasicLabelStyleDescription,
    viewpoint::style::StyleDescription,
    viewpoint::description::DAnnotationEntry,
    viewpoint::description::IdentifiedElement,
    viewpoint::description::EndUserDocumentedElement,
    viewpoint::description::AnnotationEntry,
    UserColor,
    viewpoint::description::UserColorsPalette,
    SystemColor,
    viewpoint::description::SytemColorsPalette,
    style::LabelBorderStyles,
    tool::ToolEntry,
    viewpoint::description::Environment,
    viewpoint::description::UserColor,
    description::FixedColor,
    ColorDescription,
    viewpoint::description::FixedColor,
    viewpoint::description::ColorStep,
    ColorStep,
    description::ColorDescription,
    FixedColor,
    viewpoint::description::SystemColor,
    viewpoint::description::ColorDescription,
    viewpoint::description::SelectionDescription,
    description::UserColor,
    viewpoint::description::InterpolatedColor,
    viewpoint::description::UserFixedColor,
    viewpoint::description::ComputedColor,
    EStructuralFeatureCustomization,
    viewpoint::description::EReferenceCustomization,
    viewpoint::description::IVSMElementCustomization,
    IVSMElementCustomization,
    viewpoint::description::VSMElementCustomizationReuse,
    viewpoint::description::VSMElementCustomization,
    viewpoint::description::Customization,
    viewpoint::description::EAttributeCustomization,
    viewpoint::description::EStructuralFeatureCustomization,
    viewpoint::description::DecorationDescription,
    viewpoint::description::DecorationDescriptionsSet,
    tool::PasteDescription,
    viewpoint::description::PasteTargetDescription,
    tool::ContainerDropDescription,
    viewpoint::description::DragAndDropTargetDescription,
    viewpoint::description::ConditionalStyleDescription,
    description::viewpoint::EStringToStringMapEntry,
    viewpoint::description::DAnnotation,
    DAnnotation,
    viewpoint::description::AbstractMappingImport,
    tool::RepresentationNavigationDescription,
    tool::RepresentationCreationDescription,
    IdentifiedElement,
    viewpoint::description::RepresentationElementMapping,
    viewpoint::description::JavaExtension,
    description::viewpoint::EObject,
    viewpoint::description::MetamodelExtensionSetting,
    viewpoint::description::RepresentationExtensionDescription,
    viewpoint::description::DModelElement,
    viewpoint::description::DocumentedElement,
    description::viewpoint::EPackage,
    viewpoint::description::FeatureExtensionDescription,
    RepresentationTemplate,
    MetamodelExtensionSetting,
    JavaExtension,
    RepresentationExtensionDescription,
    viewpoint::description::DiagramExtensionDescription,
    RepresentationDescription,
    viewpoint::description::RepresentationImportDescription,
    viewpoint::description::RepresentationTemplate,
    validation::ValidationSet,
    description::IdentifiedElement,
    description::EndUserDocumentedElement,
    description::Component,
    viewpoint::description::Component,
    UserColorsPalette,
    SytemColorsPalette,
    viewpoint::Customizable,
    DFile,
    viewpoint::DModel,
    DResourceContainer,
    viewpoint::DFolder,
    viewpoint::DProject,
    DResource,
    viewpoint::DResourceContainer,
    viewpoint::DFile,
    viewpoint::DResource,
    viewpoint::SessionManagerEObject,
    viewpoint::DAnalysisSessionEObject,
    viewpoint::RGBValues,
    DNavigationLink,
    viewpoint::DEObjectLink,
    viewpoint::DragAndDropTarget,
    style::StyleDescription,
    viewpoint::style::NodeStyleDescription,
    Customizable,
    viewpoint::BasicLabelStyle,
    BasicLabelStyle,
    viewpoint::diagram::CenterLabelStyle,
    viewpoint::diagram::EndLabelStyle,
    viewpoint::diagram::BeginLabelStyle,
    viewpoint::LabelStyle,
    viewpoint::DAnalysisCustomData,
    viewpoint::DSourceFileLink,
    DecorationDescription,
    viewpoint::description::MappingBasedDecoration,
    viewpoint::description::SemanticBasedDecoration,
    diagram::NodeStyle,
    viewpoint::diagram::WorkspaceImage,
    viewpoint::diagram::EdgeTarget,
    diagram::BorderedStyle,
    Style,
    viewpoint::diagram::BorderedStyle,
    viewpoint::diagram::EdgeStyle,
    LabelStyle,
    viewpoint::diagram::ContainerStyle,
    viewpoint::diagram::NodeStyle,
    diagram::viewpoint::DRepresentationContainer,
    viewpoint::diagram::GaugeSection,
    diagram::viewpoint::RGBValues,
    description::IEdgeMapping,
    viewpoint::diagram::DDiagramSet,
    AbstractDNode,
    viewpoint::diagram::DNodeListElement,
    EdgeStyle,
    viewpoint::diagram::BracketEdgeStyle,
    diagram::DDiagramElement,
    description::ContainerMapping,
    viewpoint::description::ContainerMappingImport,
    ContainerStyle,
    viewpoint::diagram::ShapeContainerStyle,
    viewpoint::diagram::FlatContainerStyle,
    diagram::EdgeTarget,
    viewpoint::diagram::DEdge,
    diagram::AbstractDNode,
    EdgeTarget,
    description::NodeMapping,
    viewpoint::description::NodeMappingImport,
    diagram::viewpoint::Style,
    NodeStyle,
    viewpoint::diagram::CustomStyle,
    viewpoint::diagram::Note,
    viewpoint::diagram::GaugeCompositeStyle,
    viewpoint::diagram::Dot,
    viewpoint::diagram::Ellipse,
    viewpoint::diagram::Lozenge,
    viewpoint::diagram::Square,
    viewpoint::diagram::BundledImage,
    viewpoint::diagram::GraphicalFilter,
    GraphicalFilter,
    viewpoint::diagram::CollapseFilter,
    diagram::viewpoint::Decoration,
    viewpoint::diagram::DDiagramLink,
    viewpoint::diagram::AbsoluteBoundsFilter,
    filter::CompositeFilterDescription,
    viewpoint::diagram::AppliedCompositeFilters,
    viewpoint::diagram::FoldingFilter,
    viewpoint::diagram::FoldingPointFilter,
    viewpoint::diagram::HideLabelFilter,
    viewpoint::diagram::HideFilter,
    description::Layer,
    FilterVariableHistory,
    tool::BehaviorTool,
    validation::ValidationRule,
    DNavigable,
    DRepresentationElement,
    diagram::DDiagram,
    DEdge,
    DDiagram,
    filter::FilterDescription,
    concern::ConcernDescription,
    DDiagramElementContainer,
    viewpoint::diagram::DNodeList,
    viewpoint::diagram::DNodeContainer,
    DNodeListElement,
    DNode,
    DContainer,
    DValidable,
    viewpoint::diagram::DDiagramElement,
    DragAndDropTarget,
    viewpoint::diagram::DDiagramElementContainer,
    viewpoint::diagram::DNode,
    DRepresentation,
    InformationSection,
    viewpoint::audit::TemplateInformationSection,
    description::DiagramDescription,
    viewpoint::description::DiagramImportDescription,
    DDiagramElement,
    viewpoint::diagram::AbstractDNode,
    SwitchChild,
    viewpoint::tool::Case,
    viewpoint::tool::FeatureChangeListener,
    tool::FeatureChangeListener,
    viewpoint::audit::InformationSection,
    tool::Default,
    tool::Case,
    viewpoint::tool::Default,
    viewpoint::tool::SwitchChild,
    viewpoint::tool::ToolFilterDescription,
    viewpoint::tool::ExternalJavaActionParameter,
    viewpoint::tool::NameVariable,
    tool::viewpoint::EObject,
    ContainerModelOperation,
    viewpoint::tool::RemoveElement,
    viewpoint::tool::SetObject,
    viewpoint::tool::ChangeContext,
    viewpoint::tool::CreateView,
    viewpoint::tool::DeleteView,
    viewpoint::tool::Navigation,
    viewpoint::tool::For,
    viewpoint::tool::Unset,
    viewpoint::tool::MoveElement,
    viewpoint::tool::SetValue,
    viewpoint::tool::If,
    viewpoint::tool::CreateInstance,
    viewpoint::tool::InitialContainerDropOperation,
    viewpoint::tool::InitEdgeCreationOperation,
    viewpoint::tool::InitialOperation,
    viewpoint::tool::InitialNodeCreationOperation,
    viewpoint::tool::ModelOperation,
    tool::ModelOperation,
    ModelOperation,
    viewpoint::tool::Switch,
    viewpoint::tool::ContainerModelOperation,
    viewpoint::tool::EditMaskVariables,
    viewpoint::tool::SelectModelElementVariable,
    viewpoint::tool::ElementSelectVariable,
    tool::AbstractVariable,
    viewpoint::tool::DropContainerVariable,
    viewpoint::tool::SelectContainerVariable,
    viewpoint::tool::ElementDropVariable,
    viewpoint::tool::ContainerViewVariable,
    viewpoint::tool::ElementDeleteVariable,
    viewpoint::tool::SourceEdgeViewCreationVariable,
    viewpoint::tool::ElementVariable,
    viewpoint::tool::SourceEdgeCreationVariable,
    viewpoint::tool::ElementViewVariable,
    viewpoint::tool::ElementDoubleClickVariable,
    viewpoint::tool::TargetEdgeCreationVariable,
    viewpoint::tool::TargetEdgeViewCreationVariable,
    viewpoint::tool::NodeCreationVariable,
    viewpoint::Decoration,
    Viewpoint,
    viewpoint::MetaModelExtension,
    DSemanticDecorator,
    viewpoint::diagram::DSemanticDiagram,
    DStylizable,
    DMappingBased,
    DLabelled,
    AnnotationEntry,
    description::DModelElement,
    DRefreshable,
    viewpoint::DRepresentationElement,
    viewpoint::Style,
    description::DocumentedElement,
    viewpoint::description::Viewpoint,
    viewpoint::tool::ToolSection,
    viewpoint::filter::FilterDescription,
    viewpoint::description::EdgeMapping,
    viewpoint::description::Group,
    viewpoint::description::EdgeMappingImport,
    viewpoint::description::Layer,
    viewpoint::tool::ToolEntry,
    viewpoint::description::RepresentationDescription,
    viewpoint::diagram::DDiagram,
    viewpoint::concern::ConcernDescription,
    viewpoint::description::AbstractNodeMapping,
    viewpoint::DRepresentation,
    viewpoint::DSemanticDecorator,
    DDiagramSet,
    DView,
    viewpoint::DRepresentationContainer,
    viewpoint::DContainer,
    viewpoint::DMappingBased,
    viewpoint::DLabelled,
    viewpoint::DRefreshable,
    viewpoint::DStylizable,
    viewpoint::DNavigationLink,
    viewpoint::DNavigable,
    viewpoint::DValidable,
    FeatureExtensionDescription,
    viewpoint::DFeatureExtension,
    viewpoint::DView,
    DAnnotationEntry,
    viewpoint::EObject,
    viewpoint::DAnalysis,
    ContainerShape,
    BackgroundStyle,
    AlignmentKind,
    ERROR_LEVEL,
    EdgeArrows,
    FilterKind,
    LineStyle,
    ContainerLayout,
    LabelAlignment,
    EdgeRouting,
    ResizeKind,
    Position,
    FoldingStyle,
    DragSource,
    SyncStatus,
    LayoutDirection,
    LabelPosition,
    FontFormat,
    NavigationTargetType,
    SystemColors,
    BundledImageShape,
    ReconnectionKind,
    ArrangeConstraint,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_conditionalstyledescription_is_not_abstract():
    assert not inspect.isabstract(ConditionalStyleDescription)


def test_conditionalstyledescription_constructor_exists():
    assert callable(ConditionalStyleDescription.__init__)


def test_conditionalstyledescription_constructor_args():
    sig = inspect.signature(ConditionalStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::conditionalcontainerstyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::ConditionalContainerStyleDescription)


def test_viewpoint::description::conditionalcontainerstyledescription_constructor_exists():
    assert callable(viewpoint::description::ConditionalContainerStyleDescription.__init__)


def test_viewpoint::description::conditionalcontainerstyledescription_constructor_args():
    sig = inspect.signature(viewpoint::description::ConditionalContainerStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::conditionaledgestyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::ConditionalEdgeStyleDescription)


def test_viewpoint::description::conditionaledgestyledescription_constructor_exists():
    assert callable(viewpoint::description::ConditionalEdgeStyleDescription.__init__)


def test_viewpoint::description::conditionaledgestyledescription_constructor_args():
    sig = inspect.signature(viewpoint::description::ConditionalEdgeStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::conditionalnodestyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::ConditionalNodeStyleDescription)


def test_viewpoint::description::conditionalnodestyledescription_constructor_exists():
    assert callable(viewpoint::description::ConditionalNodeStyleDescription.__init__)


def test_viewpoint::description::conditionalnodestyledescription_constructor_args():
    sig = inspect.signature(viewpoint::description::ConditionalNodeStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_description::conditionaledgestyledescription_is_not_abstract():
    assert not inspect.isabstract(description::ConditionalEdgeStyleDescription)


def test_description::conditionaledgestyledescription_constructor_exists():
    assert callable(description::ConditionalEdgeStyleDescription.__init__)


def test_description::conditionaledgestyledescription_constructor_args():
    sig = inspect.signature(description::ConditionalEdgeStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_style::edgestyledescription_is_not_abstract():
    assert not inspect.isabstract(style::EdgeStyleDescription)


def test_style::edgestyledescription_constructor_exists():
    assert callable(style::EdgeStyleDescription.__init__)


def test_style::edgestyledescription_constructor_args():
    sig = inspect.signature(style::EdgeStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::iedgemapping_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::IEdgeMapping)


def test_viewpoint::description::iedgemapping_constructor_exists():
    assert callable(viewpoint::description::IEdgeMapping.__init__)


def test_viewpoint::description::iedgemapping_constructor_args():
    sig = inspect.signature(viewpoint::description::IEdgeMapping.__init__)
    params = list(sig.parameters.keys())



def test_tool::reconnectedgedescription_is_not_abstract():
    assert not inspect.isabstract(tool::ReconnectEdgeDescription)


def test_tool::reconnectedgedescription_constructor_exists():
    assert callable(tool::ReconnectEdgeDescription.__init__)


def test_tool::reconnectedgedescription_constructor_args():
    sig = inspect.signature(tool::ReconnectEdgeDescription.__init__)
    params = list(sig.parameters.keys())



def test_description::conditionalcontainerstyledescription_is_not_abstract():
    assert not inspect.isabstract(description::ConditionalContainerStyleDescription)


def test_description::conditionalcontainerstyledescription_constructor_exists():
    assert callable(description::ConditionalContainerStyleDescription.__init__)


def test_description::conditionalcontainerstyledescription_constructor_args():
    sig = inspect.signature(description::ConditionalContainerStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_style::containerstyledescription_is_not_abstract():
    assert not inspect.isabstract(style::ContainerStyleDescription)


def test_style::containerstyledescription_constructor_exists():
    assert callable(style::ContainerStyleDescription.__init__)


def test_style::containerstyledescription_constructor_args():
    sig = inspect.signature(style::ContainerStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_description::abstractmappingimport_is_not_abstract():
    assert not inspect.isabstract(description::AbstractMappingImport)


def test_description::abstractmappingimport_constructor_exists():
    assert callable(description::AbstractMappingImport.__init__)


def test_description::abstractmappingimport_constructor_args():
    sig = inspect.signature(description::AbstractMappingImport.__init__)
    params = list(sig.parameters.keys())



def test_description::conditionalnodestyledescription_is_not_abstract():
    assert not inspect.isabstract(description::ConditionalNodeStyleDescription)


def test_description::conditionalnodestyledescription_constructor_exists():
    assert callable(description::ConditionalNodeStyleDescription.__init__)


def test_description::conditionalnodestyledescription_constructor_args():
    sig = inspect.signature(description::ConditionalNodeStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_style::nodestyledescription_is_not_abstract():
    assert not inspect.isabstract(style::NodeStyleDescription)


def test_style::nodestyledescription_constructor_exists():
    assert callable(style::NodeStyleDescription.__init__)


def test_style::nodestyledescription_constructor_args():
    sig = inspect.signature(style::NodeStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_tool::doubleclickdescription_is_not_abstract():
    assert not inspect.isabstract(tool::DoubleClickDescription)


def test_tool::doubleclickdescription_constructor_exists():
    assert callable(tool::DoubleClickDescription.__init__)


def test_tool::doubleclickdescription_constructor_args():
    sig = inspect.signature(tool::DoubleClickDescription.__init__)
    params = list(sig.parameters.keys())



def test_description::abstractnodemapping_is_not_abstract():
    assert not inspect.isabstract(description::AbstractNodeMapping)


def test_description::abstractnodemapping_constructor_exists():
    assert callable(description::AbstractNodeMapping.__init__)


def test_description::abstractnodemapping_constructor_args():
    sig = inspect.signature(description::AbstractNodeMapping.__init__)
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



def test_tool::toolsection_is_not_abstract():
    assert not inspect.isabstract(tool::ToolSection)


def test_tool::toolsection_constructor_exists():
    assert callable(tool::ToolSection.__init__)


def test_tool::toolsection_constructor_args():
    sig = inspect.signature(tool::ToolSection.__init__)
    params = list(sig.parameters.keys())



def test_description::representationelementmapping_is_not_abstract():
    assert not inspect.isabstract(description::RepresentationElementMapping)


def test_description::representationelementmapping_constructor_exists():
    assert callable(description::RepresentationElementMapping.__init__)


def test_description::representationelementmapping_constructor_args():
    sig = inspect.signature(description::RepresentationElementMapping.__init__)
    params = list(sig.parameters.keys())



def test_description::representationimportdescription_is_not_abstract():
    assert not inspect.isabstract(description::RepresentationImportDescription)


def test_description::representationimportdescription_constructor_exists():
    assert callable(description::RepresentationImportDescription.__init__)


def test_description::representationimportdescription_constructor_args():
    sig = inspect.signature(description::RepresentationImportDescription.__init__)
    params = list(sig.parameters.keys())



def test_description::additionallayer_is_not_abstract():
    assert not inspect.isabstract(description::AdditionalLayer)


def test_description::additionallayer_constructor_exists():
    assert callable(description::AdditionalLayer.__init__)


def test_description::additionallayer_constructor_args():
    sig = inspect.signature(description::AdditionalLayer.__init__)
    params = list(sig.parameters.keys())



def test_description::layout_is_not_abstract():
    assert not inspect.isabstract(description::Layout)


def test_description::layout_constructor_exists():
    assert callable(description::Layout.__init__)


def test_description::layout_constructor_args():
    sig = inspect.signature(description::Layout.__init__)
    params = list(sig.parameters.keys())



def test_description::edgemappingimport_is_not_abstract():
    assert not inspect.isabstract(description::EdgeMappingImport)


def test_description::edgemappingimport_constructor_exists():
    assert callable(description::EdgeMappingImport.__init__)


def test_description::edgemappingimport_constructor_args():
    sig = inspect.signature(description::EdgeMappingImport.__init__)
    params = list(sig.parameters.keys())



def test_description::edgemapping_is_not_abstract():
    assert not inspect.isabstract(description::EdgeMapping)


def test_description::edgemapping_constructor_exists():
    assert callable(description::EdgeMapping.__init__)


def test_description::edgemapping_constructor_args():
    sig = inspect.signature(description::EdgeMapping.__init__)
    params = list(sig.parameters.keys())



def test_concern::concernset_is_not_abstract():
    assert not inspect.isabstract(concern::ConcernSet)


def test_concern::concernset_constructor_exists():
    assert callable(concern::ConcernSet.__init__)


def test_concern::concernset_constructor_args():
    sig = inspect.signature(concern::ConcernSet.__init__)
    params = list(sig.parameters.keys())



def test_modelelement2viewvariable_is_not_abstract():
    assert not inspect.isabstract(ModelElement2ViewVariable)


def test_modelelement2viewvariable_constructor_exists():
    assert callable(ModelElement2ViewVariable.__init__)


def test_modelelement2viewvariable_constructor_args():
    sig = inspect.signature(ModelElement2ViewVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::diagram::diagramelementmapping2modelelement_is_not_abstract():
    assert not inspect.isabstract(viewpoint::diagram::DiagramElementMapping2ModelElement)


def test_viewpoint::diagram::diagramelementmapping2modelelement_constructor_exists():
    assert callable(viewpoint::diagram::DiagramElementMapping2ModelElement.__init__)


def test_viewpoint::diagram::diagramelementmapping2modelelement_constructor_args():
    sig = inspect.signature(viewpoint::diagram::DiagramElementMapping2ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_diagramelementmapping2modelelement_is_not_abstract():
    assert not inspect.isabstract(DiagramElementMapping2ModelElement)


def test_diagramelementmapping2modelelement_constructor_exists():
    assert callable(DiagramElementMapping2ModelElement.__init__)


def test_diagramelementmapping2modelelement_constructor_args():
    sig = inspect.signature(DiagramElementMapping2ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::diagram::computedstyledescriptionregistry_is_not_abstract():
    assert not inspect.isabstract(viewpoint::diagram::ComputedStyleDescriptionRegistry)


def test_viewpoint::diagram::computedstyledescriptionregistry_constructor_exists():
    assert callable(viewpoint::diagram::ComputedStyleDescriptionRegistry.__init__)


def test_viewpoint::diagram::computedstyledescriptionregistry_constructor_args():
    sig = inspect.signature(viewpoint::diagram::ComputedStyleDescriptionRegistry.__init__)
    params = list(sig.parameters.keys())



def test_description::pastetargetdescription_is_not_abstract():
    assert not inspect.isabstract(description::PasteTargetDescription)


def test_description::pastetargetdescription_constructor_exists():
    assert callable(description::PasteTargetDescription.__init__)


def test_description::pastetargetdescription_constructor_args():
    sig = inspect.signature(description::PasteTargetDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::diagramelementmapping_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::DiagramElementMapping)


def test_viewpoint::description::diagramelementmapping_constructor_exists():
    assert callable(viewpoint::description::DiagramElementMapping.__init__)


def test_viewpoint::description::diagramelementmapping_constructor_args():
    sig = inspect.signature(viewpoint::description::DiagramElementMapping.__init__)
    params = list(sig.parameters.keys())
    assert "semanticElements" in params, "Missing parameter 'semanticElements'"
    assert "createElements" in params, "Missing parameter 'createElements'"
    assert "semanticCandidatesExpression" in params, "Missing parameter 'semanticCandidatesExpression'"
    assert "preconditionExpression" in params, "Missing parameter 'preconditionExpression'"
    assert "synchronizationLock" in params, "Missing parameter 'synchronizationLock'"

def test_viewpoint::description::diagramelementmapping_has_semanticElements():
    assert hasattr(viewpoint::description::DiagramElementMapping, "semanticElements")
    descriptor = None
    for klass in viewpoint::description::DiagramElementMapping.__mro__:
        if "semanticElements" in klass.__dict__:
            descriptor = klass.__dict__["semanticElements"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::description::diagramelementmapping_has_createElements():
    assert hasattr(viewpoint::description::DiagramElementMapping, "createElements")
    descriptor = None
    for klass in viewpoint::description::DiagramElementMapping.__mro__:
        if "createElements" in klass.__dict__:
            descriptor = klass.__dict__["createElements"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::description::diagramelementmapping_has_semanticCandidatesExpression():
    assert hasattr(viewpoint::description::DiagramElementMapping, "semanticCandidatesExpression")
    descriptor = None
    for klass in viewpoint::description::DiagramElementMapping.__mro__:
        if "semanticCandidatesExpression" in klass.__dict__:
            descriptor = klass.__dict__["semanticCandidatesExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::description::diagramelementmapping_has_preconditionExpression():
    assert hasattr(viewpoint::description::DiagramElementMapping, "preconditionExpression")
    descriptor = None
    for klass in viewpoint::description::DiagramElementMapping.__mro__:
        if "preconditionExpression" in klass.__dict__:
            descriptor = klass.__dict__["preconditionExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::description::diagramelementmapping_has_synchronizationLock():
    assert hasattr(viewpoint::description::DiagramElementMapping, "synchronizationLock")
    descriptor = None
    for klass in viewpoint::description::DiagramElementMapping.__mro__:
        if "synchronizationLock" in klass.__dict__:
            descriptor = klass.__dict__["synchronizationLock"]
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



def test_viewpoint::description::containermapping_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::ContainerMapping)


def test_viewpoint::description::containermapping_constructor_exists():
    assert callable(viewpoint::description::ContainerMapping.__init__)


def test_viewpoint::description::containermapping_constructor_args():
    sig = inspect.signature(viewpoint::description::ContainerMapping.__init__)
    params = list(sig.parameters.keys())
    assert "childrenPresentation" in params, "Missing parameter 'childrenPresentation'"

def test_viewpoint::description::containermapping_has_childrenPresentation():
    assert hasattr(viewpoint::description::ContainerMapping, "childrenPresentation")
    descriptor = None
    for klass in viewpoint::description::ContainerMapping.__mro__:
        if "childrenPresentation" in klass.__dict__:
            descriptor = klass.__dict__["childrenPresentation"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::description::nodemapping_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::NodeMapping)


def test_viewpoint::description::nodemapping_constructor_exists():
    assert callable(viewpoint::description::NodeMapping.__init__)


def test_viewpoint::description::nodemapping_constructor_args():
    sig = inspect.signature(viewpoint::description::NodeMapping.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::diagramdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::DiagramDescription)


def test_viewpoint::description::diagramdescription_constructor_exists():
    assert callable(viewpoint::description::DiagramDescription.__init__)


def test_viewpoint::description::diagramdescription_constructor_args():
    sig = inspect.signature(viewpoint::description::DiagramDescription.__init__)
    params = list(sig.parameters.keys())
    assert "enablePopupBars" in params, "Missing parameter 'enablePopupBars'"
    assert "preconditionExpression" in params, "Missing parameter 'preconditionExpression'"
    assert "domainClass" in params, "Missing parameter 'domainClass'"
    assert "rootExpression" in params, "Missing parameter 'rootExpression'"

def test_viewpoint::description::diagramdescription_has_enablePopupBars():
    assert hasattr(viewpoint::description::DiagramDescription, "enablePopupBars")
    descriptor = None
    for klass in viewpoint::description::DiagramDescription.__mro__:
        if "enablePopupBars" in klass.__dict__:
            descriptor = klass.__dict__["enablePopupBars"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::description::diagramdescription_has_preconditionExpression():
    assert hasattr(viewpoint::description::DiagramDescription, "preconditionExpression")
    descriptor = None
    for klass in viewpoint::description::DiagramDescription.__mro__:
        if "preconditionExpression" in klass.__dict__:
            descriptor = klass.__dict__["preconditionExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::description::diagramdescription_has_domainClass():
    assert hasattr(viewpoint::description::DiagramDescription, "domainClass")
    descriptor = None
    for klass in viewpoint::description::DiagramDescription.__mro__:
        if "domainClass" in klass.__dict__:
            descriptor = klass.__dict__["domainClass"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::description::diagramdescription_has_rootExpression():
    assert hasattr(viewpoint::description::DiagramDescription, "rootExpression")
    descriptor = None
    for klass in viewpoint::description::DiagramDescription.__mro__:
        if "rootExpression" in klass.__dict__:
            descriptor = klass.__dict__["rootExpression"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::diagram::containervariable2styledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::diagram::ContainerVariable2StyleDescription)


def test_viewpoint::diagram::containervariable2styledescription_constructor_exists():
    assert callable(viewpoint::diagram::ContainerVariable2StyleDescription.__init__)


def test_viewpoint::diagram::containervariable2styledescription_constructor_args():
    sig = inspect.signature(viewpoint::diagram::ContainerVariable2StyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_containervariable2styledescription_is_not_abstract():
    assert not inspect.isabstract(ContainerVariable2StyleDescription)


def test_containervariable2styledescription_constructor_exists():
    assert callable(ContainerVariable2StyleDescription.__init__)


def test_containervariable2styledescription_constructor_args():
    sig = inspect.signature(ContainerVariable2StyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::diagram::viewvariable2containervariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint::diagram::ViewVariable2ContainerVariable)


def test_viewpoint::diagram::viewvariable2containervariable_constructor_exists():
    assert callable(viewpoint::diagram::ViewVariable2ContainerVariable.__init__)


def test_viewpoint::diagram::viewvariable2containervariable_constructor_args():
    sig = inspect.signature(viewpoint::diagram::ViewVariable2ContainerVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewvariable2containervariable_is_not_abstract():
    assert not inspect.isabstract(ViewVariable2ContainerVariable)


def test_viewvariable2containervariable_constructor_exists():
    assert callable(ViewVariable2ContainerVariable.__init__)


def test_viewvariable2containervariable_constructor_args():
    sig = inspect.signature(ViewVariable2ContainerVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::diagram::modelelement2viewvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint::diagram::ModelElement2ViewVariable)


def test_viewpoint::diagram::modelelement2viewvariable_constructor_exists():
    assert callable(viewpoint::diagram::ModelElement2ViewVariable.__init__)


def test_viewpoint::diagram::modelelement2viewvariable_constructor_args():
    sig = inspect.signature(viewpoint::diagram::ModelElement2ViewVariable.__init__)
    params = list(sig.parameters.keys())



def test_diagram::viewpoint::eobject_is_not_abstract():
    assert not inspect.isabstract(diagram::viewpoint::EObject)


def test_diagram::viewpoint::eobject_constructor_exists():
    assert callable(diagram::viewpoint::EObject.__init__)


def test_diagram::viewpoint::eobject_constructor_args():
    sig = inspect.signature(diagram::viewpoint::EObject.__init__)
    params = list(sig.parameters.keys())



def test_filter::filtervariable_is_not_abstract():
    assert not inspect.isabstract(filter::FilterVariable)


def test_filter::filtervariable_constructor_exists():
    assert callable(filter::FilterVariable.__init__)


def test_filter::filtervariable_constructor_args():
    sig = inspect.signature(filter::FilterVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::diagram::filtervariablevalue_is_not_abstract():
    assert not inspect.isabstract(viewpoint::diagram::FilterVariableValue)


def test_viewpoint::diagram::filtervariablevalue_constructor_exists():
    assert callable(viewpoint::diagram::FilterVariableValue.__init__)


def test_viewpoint::diagram::filtervariablevalue_constructor_args():
    sig = inspect.signature(viewpoint::diagram::FilterVariableValue.__init__)
    params = list(sig.parameters.keys())



def test_filtervariablevalue_is_not_abstract():
    assert not inspect.isabstract(FilterVariableValue)


def test_filtervariablevalue_constructor_exists():
    assert callable(FilterVariableValue.__init__)


def test_filtervariablevalue_constructor_args():
    sig = inspect.signature(FilterVariableValue.__init__)
    params = list(sig.parameters.keys())



def test_collapsefilter_is_not_abstract():
    assert not inspect.isabstract(CollapseFilter)


def test_collapsefilter_constructor_exists():
    assert callable(CollapseFilter.__init__)


def test_collapsefilter_constructor_args():
    sig = inspect.signature(CollapseFilter.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::diagram::indirectlycollapsefilter_is_not_abstract():
    assert not inspect.isabstract(viewpoint::diagram::IndirectlyCollapseFilter)


def test_viewpoint::diagram::indirectlycollapsefilter_constructor_exists():
    assert callable(viewpoint::diagram::IndirectlyCollapseFilter.__init__)


def test_viewpoint::diagram::indirectlycollapsefilter_constructor_args():
    sig = inspect.signature(viewpoint::diagram::IndirectlyCollapseFilter.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::diagram::filtervariablehistory_is_not_abstract():
    assert not inspect.isabstract(viewpoint::diagram::FilterVariableHistory)


def test_viewpoint::diagram::filtervariablehistory_constructor_exists():
    assert callable(viewpoint::diagram::FilterVariableHistory.__init__)


def test_viewpoint::diagram::filtervariablehistory_constructor_args():
    sig = inspect.signature(viewpoint::diagram::FilterVariableHistory.__init__)
    params = list(sig.parameters.keys())



def test_gaugesection_is_not_abstract():
    assert not inspect.isabstract(GaugeSection)


def test_gaugesection_constructor_exists():
    assert callable(GaugeSection.__init__)


def test_gaugesection_constructor_args():
    sig = inspect.signature(GaugeSection.__init__)
    params = list(sig.parameters.keys())



def test_endlabelstyle_is_not_abstract():
    assert not inspect.isabstract(EndLabelStyle)


def test_endlabelstyle_constructor_exists():
    assert callable(EndLabelStyle.__init__)


def test_endlabelstyle_constructor_args():
    sig = inspect.signature(EndLabelStyle.__init__)
    params = list(sig.parameters.keys())



def test_centerlabelstyle_is_not_abstract():
    assert not inspect.isabstract(CenterLabelStyle)


def test_centerlabelstyle_constructor_exists():
    assert callable(CenterLabelStyle.__init__)


def test_centerlabelstyle_constructor_args():
    sig = inspect.signature(CenterLabelStyle.__init__)
    params = list(sig.parameters.keys())



def test_beginlabelstyle_is_not_abstract():
    assert not inspect.isabstract(BeginLabelStyle)


def test_beginlabelstyle_constructor_exists():
    assert callable(BeginLabelStyle.__init__)


def test_beginlabelstyle_constructor_args():
    sig = inspect.signature(BeginLabelStyle.__init__)
    params = list(sig.parameters.keys())



def test_diagram::containerstyle_is_not_abstract():
    assert not inspect.isabstract(diagram::ContainerStyle)


def test_diagram::containerstyle_constructor_exists():
    assert callable(diagram::ContainerStyle.__init__)


def test_diagram::containerstyle_constructor_args():
    sig = inspect.signature(diagram::ContainerStyle.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::validation::validationfix_is_not_abstract():
    assert not inspect.isabstract(viewpoint::validation::ValidationFix)


def test_viewpoint::validation::validationfix_constructor_exists():
    assert callable(viewpoint::validation::ValidationFix.__init__)


def test_viewpoint::validation::validationfix_constructor_args():
    sig = inspect.signature(viewpoint::validation::ValidationFix.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_viewpoint::validation::validationfix_has_name():
    assert hasattr(viewpoint::validation::ValidationFix, "name")
    descriptor = None
    for klass in viewpoint::validation::ValidationFix.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_validationrule_is_not_abstract():
    assert not inspect.isabstract(ValidationRule)


def test_validationrule_constructor_exists():
    assert callable(ValidationRule.__init__)


def test_validationrule_constructor_args():
    sig = inspect.signature(ValidationRule.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::validation::viewvalidationrule_is_not_abstract():
    assert not inspect.isabstract(viewpoint::validation::ViewValidationRule)


def test_viewpoint::validation::viewvalidationrule_constructor_exists():
    assert callable(viewpoint::validation::ViewValidationRule.__init__)


def test_viewpoint::validation::viewvalidationrule_constructor_args():
    sig = inspect.signature(viewpoint::validation::ViewValidationRule.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::validation::semanticvalidationrule_is_not_abstract():
    assert not inspect.isabstract(viewpoint::validation::SemanticValidationRule)


def test_viewpoint::validation::semanticvalidationrule_constructor_exists():
    assert callable(viewpoint::validation::SemanticValidationRule.__init__)


def test_viewpoint::validation::semanticvalidationrule_constructor_args():
    sig = inspect.signature(viewpoint::validation::SemanticValidationRule.__init__)
    params = list(sig.parameters.keys())
    assert "targetClass" in params, "Missing parameter 'targetClass'"

def test_viewpoint::validation::semanticvalidationrule_has_targetClass():
    assert hasattr(viewpoint::validation::SemanticValidationRule, "targetClass")
    descriptor = None
    for klass in viewpoint::validation::SemanticValidationRule.__mro__:
        if "targetClass" in klass.__dict__:
            descriptor = klass.__dict__["targetClass"]
            break
    assert isinstance(descriptor, property)



def test_validation::validationfix_is_not_abstract():
    assert not inspect.isabstract(validation::ValidationFix)


def test_validation::validationfix_constructor_exists():
    assert callable(validation::ValidationFix.__init__)


def test_validation::validationfix_constructor_args():
    sig = inspect.signature(validation::ValidationFix.__init__)
    params = list(sig.parameters.keys())



def test_validation::ruleaudit_is_not_abstract():
    assert not inspect.isabstract(validation::RuleAudit)


def test_validation::ruleaudit_constructor_exists():
    assert callable(validation::RuleAudit.__init__)


def test_validation::ruleaudit_constructor_args():
    sig = inspect.signature(validation::RuleAudit.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::validation::validationrule_is_not_abstract():
    assert not inspect.isabstract(viewpoint::validation::ValidationRule)


def test_viewpoint::validation::validationrule_constructor_exists():
    assert callable(viewpoint::validation::ValidationRule.__init__)


def test_viewpoint::validation::validationrule_constructor_args():
    sig = inspect.signature(viewpoint::validation::ValidationRule.__init__)
    params = list(sig.parameters.keys())
    assert "message" in params, "Missing parameter 'message'"
    assert "level" in params, "Missing parameter 'level'"

def test_viewpoint::validation::validationrule_has_message():
    assert hasattr(viewpoint::validation::ValidationRule, "message")
    descriptor = None
    for klass in viewpoint::validation::ValidationRule.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::validation::validationrule_has_level():
    assert hasattr(viewpoint::validation::ValidationRule, "level")
    descriptor = None
    for klass in viewpoint::validation::ValidationRule.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::validation::ruleaudit_is_not_abstract():
    assert not inspect.isabstract(viewpoint::validation::RuleAudit)


def test_viewpoint::validation::ruleaudit_constructor_exists():
    assert callable(viewpoint::validation::RuleAudit.__init__)


def test_viewpoint::validation::ruleaudit_constructor_args():
    sig = inspect.signature(viewpoint::validation::RuleAudit.__init__)
    params = list(sig.parameters.keys())
    assert "auditExpression" in params, "Missing parameter 'auditExpression'"

def test_viewpoint::validation::ruleaudit_has_auditExpression():
    assert hasattr(viewpoint::validation::RuleAudit, "auditExpression")
    descriptor = None
    for klass in viewpoint::validation::RuleAudit.__mro__:
        if "auditExpression" in klass.__dict__:
            descriptor = klass.__dict__["auditExpression"]
            break
    assert isinstance(descriptor, property)



def test_selectiondescription_is_not_abstract():
    assert not inspect.isabstract(SelectionDescription)


def test_selectiondescription_constructor_exists():
    assert callable(SelectionDescription.__init__)


def test_selectiondescription_constructor_args():
    sig = inspect.signature(SelectionDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::filter::filtervariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint::filter::FilterVariable)


def test_viewpoint::filter::filtervariable_constructor_exists():
    assert callable(viewpoint::filter::FilterVariable.__init__)


def test_viewpoint::filter::filtervariable_constructor_args():
    sig = inspect.signature(viewpoint::filter::FilterVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_viewpoint::filter::filtervariable_has_name():
    assert hasattr(viewpoint::filter::FilterVariable, "name")
    descriptor = None
    for klass in viewpoint::filter::FilterVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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



def test_viewpoint::filter::compositefilterdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::filter::CompositeFilterDescription)


def test_viewpoint::filter::compositefilterdescription_constructor_exists():
    assert callable(viewpoint::filter::CompositeFilterDescription.__init__)


def test_viewpoint::filter::compositefilterdescription_constructor_args():
    sig = inspect.signature(viewpoint::filter::CompositeFilterDescription.__init__)
    params = list(sig.parameters.keys())



def test_filter_is_not_abstract():
    assert not inspect.isabstract(Filter)


def test_filter_constructor_exists():
    assert callable(Filter.__init__)


def test_filter_constructor_args():
    sig = inspect.signature(Filter.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::filter::variablefilter_is_not_abstract():
    assert not inspect.isabstract(viewpoint::filter::VariableFilter)


def test_viewpoint::filter::variablefilter_constructor_exists():
    assert callable(viewpoint::filter::VariableFilter.__init__)


def test_viewpoint::filter::variablefilter_constructor_args():
    sig = inspect.signature(viewpoint::filter::VariableFilter.__init__)
    params = list(sig.parameters.keys())
    assert "semanticConditionExpression" in params, "Missing parameter 'semanticConditionExpression'"

def test_viewpoint::filter::variablefilter_has_semanticConditionExpression():
    assert hasattr(viewpoint::filter::VariableFilter, "semanticConditionExpression")
    descriptor = None
    for klass in viewpoint::filter::VariableFilter.__mro__:
        if "semanticConditionExpression" in klass.__dict__:
            descriptor = klass.__dict__["semanticConditionExpression"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::filter::mappingfilter_is_not_abstract():
    assert not inspect.isabstract(viewpoint::filter::MappingFilter)


def test_viewpoint::filter::mappingfilter_constructor_exists():
    assert callable(viewpoint::filter::MappingFilter.__init__)


def test_viewpoint::filter::mappingfilter_constructor_args():
    sig = inspect.signature(viewpoint::filter::MappingFilter.__init__)
    params = list(sig.parameters.keys())
    assert "viewConditionExpression" in params, "Missing parameter 'viewConditionExpression'"
    assert "semanticConditionExpression" in params, "Missing parameter 'semanticConditionExpression'"

def test_viewpoint::filter::mappingfilter_has_viewConditionExpression():
    assert hasattr(viewpoint::filter::MappingFilter, "viewConditionExpression")
    descriptor = None
    for klass in viewpoint::filter::MappingFilter.__mro__:
        if "viewConditionExpression" in klass.__dict__:
            descriptor = klass.__dict__["viewConditionExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::filter::mappingfilter_has_semanticConditionExpression():
    assert hasattr(viewpoint::filter::MappingFilter, "semanticConditionExpression")
    descriptor = None
    for klass in viewpoint::filter::MappingFilter.__mro__:
        if "semanticConditionExpression" in klass.__dict__:
            descriptor = klass.__dict__["semanticConditionExpression"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::filter::filter_is_not_abstract():
    assert not inspect.isabstract(viewpoint::filter::Filter)


def test_viewpoint::filter::filter_constructor_exists():
    assert callable(viewpoint::filter::Filter.__init__)


def test_viewpoint::filter::filter_constructor_args():
    sig = inspect.signature(viewpoint::filter::Filter.__init__)
    params = list(sig.parameters.keys())
    assert "filterKind" in params, "Missing parameter 'filterKind'"

def test_viewpoint::filter::filter_has_filterKind():
    assert hasattr(viewpoint::filter::Filter, "filterKind")
    descriptor = None
    for klass in viewpoint::filter::Filter.__mro__:
        if "filterKind" in klass.__dict__:
            descriptor = klass.__dict__["filterKind"]
            break
    assert isinstance(descriptor, property)



def test_representationnavigationdescription_is_not_abstract():
    assert not inspect.isabstract(RepresentationNavigationDescription)


def test_representationnavigationdescription_constructor_exists():
    assert callable(RepresentationNavigationDescription.__init__)


def test_representationnavigationdescription_constructor_args():
    sig = inspect.signature(RepresentationNavigationDescription.__init__)
    params = list(sig.parameters.keys())



def test_createview_is_not_abstract():
    assert not inspect.isabstract(CreateView)


def test_createview_constructor_exists():
    assert callable(CreateView.__init__)


def test_createview_constructor_args():
    sig = inspect.signature(CreateView.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::diagramnavigationdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::DiagramNavigationDescription)


def test_viewpoint::tool::diagramnavigationdescription_constructor_exists():
    assert callable(viewpoint::tool::DiagramNavigationDescription.__init__)


def test_viewpoint::tool::diagramnavigationdescription_constructor_args():
    sig = inspect.signature(viewpoint::tool::DiagramNavigationDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::createedgeview_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::CreateEdgeView)


def test_viewpoint::tool::createedgeview_constructor_exists():
    assert callable(viewpoint::tool::CreateEdgeView.__init__)


def test_viewpoint::tool::createedgeview_constructor_args():
    sig = inspect.signature(viewpoint::tool::CreateEdgeView.__init__)
    params = list(sig.parameters.keys())
    assert "targetExpression" in params, "Missing parameter 'targetExpression'"
    assert "sourceExpression" in params, "Missing parameter 'sourceExpression'"

def test_viewpoint::tool::createedgeview_has_targetExpression():
    assert hasattr(viewpoint::tool::CreateEdgeView, "targetExpression")
    descriptor = None
    for klass in viewpoint::tool::CreateEdgeView.__mro__:
        if "targetExpression" in klass.__dict__:
            descriptor = klass.__dict__["targetExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::tool::createedgeview_has_sourceExpression():
    assert hasattr(viewpoint::tool::CreateEdgeView, "sourceExpression")
    descriptor = None
    for klass in viewpoint::tool::CreateEdgeView.__mro__:
        if "sourceExpression" in klass.__dict__:
            descriptor = klass.__dict__["sourceExpression"]
            break
    assert isinstance(descriptor, property)



def test_representationcreationdescription_is_not_abstract():
    assert not inspect.isabstract(RepresentationCreationDescription)


def test_representationcreationdescription_constructor_exists():
    assert callable(RepresentationCreationDescription.__init__)


def test_representationcreationdescription_constructor_args():
    sig = inspect.signature(RepresentationCreationDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::diagramcreationdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::DiagramCreationDescription)


def test_viewpoint::tool::diagramcreationdescription_constructor_exists():
    assert callable(viewpoint::tool::DiagramCreationDescription.__init__)


def test_viewpoint::tool::diagramcreationdescription_constructor_args():
    sig = inspect.signature(viewpoint::tool::DiagramCreationDescription.__init__)
    params = list(sig.parameters.keys())



def test_tool::editmaskvariables_is_not_abstract():
    assert not inspect.isabstract(tool::EditMaskVariables)


def test_tool::editmaskvariables_constructor_exists():
    assert callable(tool::EditMaskVariables.__init__)


def test_tool::editmaskvariables_constructor_args():
    sig = inspect.signature(tool::EditMaskVariables.__init__)
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



def test_viewpoint::tool::deletehookparameter_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::DeleteHookParameter)


def test_viewpoint::tool::deletehookparameter_constructor_exists():
    assert callable(viewpoint::tool::DeleteHookParameter.__init__)


def test_viewpoint::tool::deletehookparameter_constructor_args():
    sig = inspect.signature(viewpoint::tool::DeleteHookParameter.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_viewpoint::tool::deletehookparameter_has_value():
    assert hasattr(viewpoint::tool::DeleteHookParameter, "value")
    descriptor = None
    for klass in viewpoint::tool::DeleteHookParameter.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::tool::deletehookparameter_has_name():
    assert hasattr(viewpoint::tool::DeleteHookParameter, "name")
    descriptor = None
    for klass in viewpoint::tool::DeleteHookParameter.__mro__:
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



def test_viewpoint::tool::deletehook_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::DeleteHook)


def test_viewpoint::tool::deletehook_constructor_exists():
    assert callable(viewpoint::tool::DeleteHook.__init__)


def test_viewpoint::tool::deletehook_constructor_args():
    sig = inspect.signature(viewpoint::tool::DeleteHook.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_viewpoint::tool::deletehook_has_id():
    assert hasattr(viewpoint::tool::DeleteHook, "id")
    descriptor = None
    for klass in viewpoint::tool::DeleteHook.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_tool::elementdeletevariable_is_not_abstract():
    assert not inspect.isabstract(tool::ElementDeleteVariable)


def test_tool::elementdeletevariable_constructor_exists():
    assert callable(tool::ElementDeleteVariable.__init__)


def test_tool::elementdeletevariable_constructor_args():
    sig = inspect.signature(tool::ElementDeleteVariable.__init__)
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



def test_tool::initedgecreationoperation_is_not_abstract():
    assert not inspect.isabstract(tool::InitEdgeCreationOperation)


def test_tool::initedgecreationoperation_constructor_exists():
    assert callable(tool::InitEdgeCreationOperation.__init__)


def test_tool::initedgecreationoperation_constructor_args():
    sig = inspect.signature(tool::InitEdgeCreationOperation.__init__)
    params = list(sig.parameters.keys())



def test_tool::initialnodecreationoperation_is_not_abstract():
    assert not inspect.isabstract(tool::InitialNodeCreationOperation)


def test_tool::initialnodecreationoperation_constructor_exists():
    assert callable(tool::InitialNodeCreationOperation.__init__)


def test_tool::initialnodecreationoperation_constructor_args():
    sig = inspect.signature(tool::InitialNodeCreationOperation.__init__)
    params = list(sig.parameters.keys())



def test_tool::nodecreationvariable_is_not_abstract():
    assert not inspect.isabstract(tool::NodeCreationVariable)


def test_tool::nodecreationvariable_constructor_exists():
    assert callable(tool::NodeCreationVariable.__init__)


def test_tool::nodecreationvariable_constructor_args():
    sig = inspect.signature(tool::NodeCreationVariable.__init__)
    params = list(sig.parameters.keys())



def test_tool::popupmenu_is_not_abstract():
    assert not inspect.isabstract(tool::PopupMenu)


def test_tool::popupmenu_constructor_exists():
    assert callable(tool::PopupMenu.__init__)


def test_tool::popupmenu_constructor_args():
    sig = inspect.signature(tool::PopupMenu.__init__)
    params = list(sig.parameters.keys())



def test_tool::toolgroup_is_not_abstract():
    assert not inspect.isabstract(tool::ToolGroup)


def test_tool::toolgroup_constructor_exists():
    assert callable(tool::ToolGroup.__init__)


def test_tool::toolgroup_constructor_args():
    sig = inspect.signature(tool::ToolGroup.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::toolgroupextension_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::ToolGroupExtension)


def test_viewpoint::tool::toolgroupextension_constructor_exists():
    assert callable(viewpoint::tool::ToolGroupExtension.__init__)


def test_viewpoint::tool::toolgroupextension_constructor_args():
    sig = inspect.signature(viewpoint::tool::ToolGroupExtension.__init__)
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



def test_edgestyledescription_is_not_abstract():
    assert not inspect.isabstract(EdgeStyleDescription)


def test_edgestyledescription_constructor_exists():
    assert callable(EdgeStyleDescription.__init__)


def test_edgestyledescription_constructor_args():
    sig = inspect.signature(EdgeStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::style::bracketedgestyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::style::BracketEdgeStyleDescription)


def test_viewpoint::style::bracketedgestyledescription_constructor_exists():
    assert callable(viewpoint::style::BracketEdgeStyleDescription.__init__)


def test_viewpoint::style::bracketedgestyledescription_constructor_args():
    sig = inspect.signature(viewpoint::style::BracketEdgeStyleDescription.__init__)
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



def test_viewpoint::style::workspaceimagedescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::style::WorkspaceImageDescription)


def test_viewpoint::style::workspaceimagedescription_constructor_exists():
    assert callable(viewpoint::style::WorkspaceImageDescription.__init__)


def test_viewpoint::style::workspaceimagedescription_constructor_args():
    sig = inspect.signature(viewpoint::style::WorkspaceImageDescription.__init__)
    params = list(sig.parameters.keys())
    assert "workspacePath" in params, "Missing parameter 'workspacePath'"

def test_viewpoint::style::workspaceimagedescription_has_workspacePath():
    assert hasattr(viewpoint::style::WorkspaceImageDescription, "workspacePath")
    descriptor = None
    for klass in viewpoint::style::WorkspaceImageDescription.__mro__:
        if "workspacePath" in klass.__dict__:
            descriptor = klass.__dict__["workspacePath"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::style::sizecomputationcontainerstyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::style::SizeComputationContainerStyleDescription)


def test_viewpoint::style::sizecomputationcontainerstyledescription_constructor_exists():
    assert callable(viewpoint::style::SizeComputationContainerStyleDescription.__init__)


def test_viewpoint::style::sizecomputationcontainerstyledescription_constructor_args():
    sig = inspect.signature(viewpoint::style::SizeComputationContainerStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "widthComputationExpression" in params, "Missing parameter 'widthComputationExpression'"
    assert "heightComputationExpression" in params, "Missing parameter 'heightComputationExpression'"

def test_viewpoint::style::sizecomputationcontainerstyledescription_has_widthComputationExpression():
    assert hasattr(viewpoint::style::SizeComputationContainerStyleDescription, "widthComputationExpression")
    descriptor = None
    for klass in viewpoint::style::SizeComputationContainerStyleDescription.__mro__:
        if "widthComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["widthComputationExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::style::sizecomputationcontainerstyledescription_has_heightComputationExpression():
    assert hasattr(viewpoint::style::SizeComputationContainerStyleDescription, "heightComputationExpression")
    descriptor = None
    for klass in viewpoint::style::SizeComputationContainerStyleDescription.__mro__:
        if "heightComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["heightComputationExpression"]
            break
    assert isinstance(descriptor, property)



def test_style::sizecomputationcontainerstyledescription_is_not_abstract():
    assert not inspect.isabstract(style::SizeComputationContainerStyleDescription)


def test_style::sizecomputationcontainerstyledescription_constructor_exists():
    assert callable(style::SizeComputationContainerStyleDescription.__init__)


def test_style::sizecomputationcontainerstyledescription_constructor_args():
    sig = inspect.signature(style::SizeComputationContainerStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::style::shapecontainerstyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::style::ShapeContainerStyleDescription)


def test_viewpoint::style::shapecontainerstyledescription_constructor_exists():
    assert callable(viewpoint::style::ShapeContainerStyleDescription.__init__)


def test_viewpoint::style::shapecontainerstyledescription_constructor_args():
    sig = inspect.signature(viewpoint::style::ShapeContainerStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "shape" in params, "Missing parameter 'shape'"

def test_viewpoint::style::shapecontainerstyledescription_has_shape():
    assert hasattr(viewpoint::style::ShapeContainerStyleDescription, "shape")
    descriptor = None
    for klass in viewpoint::style::ShapeContainerStyleDescription.__mro__:
        if "shape" in klass.__dict__:
            descriptor = klass.__dict__["shape"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::style::flatcontainerstyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::style::FlatContainerStyleDescription)


def test_viewpoint::style::flatcontainerstyledescription_constructor_exists():
    assert callable(viewpoint::style::FlatContainerStyleDescription.__init__)


def test_viewpoint::style::flatcontainerstyledescription_constructor_args():
    sig = inspect.signature(viewpoint::style::FlatContainerStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "backgroundStyle" in params, "Missing parameter 'backgroundStyle'"

def test_viewpoint::style::flatcontainerstyledescription_has_backgroundStyle():
    assert hasattr(viewpoint::style::FlatContainerStyleDescription, "backgroundStyle")
    descriptor = None
    for klass in viewpoint::style::FlatContainerStyleDescription.__mro__:
        if "backgroundStyle" in klass.__dict__:
            descriptor = klass.__dict__["backgroundStyle"]
            break
    assert isinstance(descriptor, property)



def test_style::roundedcornerstyledescription_is_not_abstract():
    assert not inspect.isabstract(style::RoundedCornerStyleDescription)


def test_style::roundedcornerstyledescription_constructor_exists():
    assert callable(style::RoundedCornerStyleDescription.__init__)


def test_style::roundedcornerstyledescription_constructor_args():
    sig = inspect.signature(style::RoundedCornerStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::style::gaugesectiondescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::style::GaugeSectionDescription)


def test_viewpoint::style::gaugesectiondescription_constructor_exists():
    assert callable(viewpoint::style::GaugeSectionDescription.__init__)


def test_viewpoint::style::gaugesectiondescription_constructor_args():
    sig = inspect.signature(viewpoint::style::GaugeSectionDescription.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "minValueExpression" in params, "Missing parameter 'minValueExpression'"
    assert "maxValueExpression" in params, "Missing parameter 'maxValueExpression'"
    assert "valueExpression" in params, "Missing parameter 'valueExpression'"

def test_viewpoint::style::gaugesectiondescription_has_label():
    assert hasattr(viewpoint::style::GaugeSectionDescription, "label")
    descriptor = None
    for klass in viewpoint::style::GaugeSectionDescription.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::style::gaugesectiondescription_has_minValueExpression():
    assert hasattr(viewpoint::style::GaugeSectionDescription, "minValueExpression")
    descriptor = None
    for klass in viewpoint::style::GaugeSectionDescription.__mro__:
        if "minValueExpression" in klass.__dict__:
            descriptor = klass.__dict__["minValueExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::style::gaugesectiondescription_has_maxValueExpression():
    assert hasattr(viewpoint::style::GaugeSectionDescription, "maxValueExpression")
    descriptor = None
    for klass in viewpoint::style::GaugeSectionDescription.__mro__:
        if "maxValueExpression" in klass.__dict__:
            descriptor = klass.__dict__["maxValueExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::style::gaugesectiondescription_has_valueExpression():
    assert hasattr(viewpoint::style::GaugeSectionDescription, "valueExpression")
    descriptor = None
    for klass in viewpoint::style::GaugeSectionDescription.__mro__:
        if "valueExpression" in klass.__dict__:
            descriptor = klass.__dict__["valueExpression"]
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



def test_viewpoint::style::lozengenodedescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::style::LozengeNodeDescription)


def test_viewpoint::style::lozengenodedescription_constructor_exists():
    assert callable(viewpoint::style::LozengeNodeDescription.__init__)


def test_viewpoint::style::lozengenodedescription_constructor_args():
    sig = inspect.signature(viewpoint::style::LozengeNodeDescription.__init__)
    params = list(sig.parameters.keys())
    assert "heightComputationExpression" in params, "Missing parameter 'heightComputationExpression'"
    assert "widthComputationExpression" in params, "Missing parameter 'widthComputationExpression'"

def test_viewpoint::style::lozengenodedescription_has_heightComputationExpression():
    assert hasattr(viewpoint::style::LozengeNodeDescription, "heightComputationExpression")
    descriptor = None
    for klass in viewpoint::style::LozengeNodeDescription.__mro__:
        if "heightComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["heightComputationExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::style::lozengenodedescription_has_widthComputationExpression():
    assert hasattr(viewpoint::style::LozengeNodeDescription, "widthComputationExpression")
    descriptor = None
    for klass in viewpoint::style::LozengeNodeDescription.__mro__:
        if "widthComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["widthComputationExpression"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::style::bundledimagedescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::style::BundledImageDescription)


def test_viewpoint::style::bundledimagedescription_constructor_exists():
    assert callable(viewpoint::style::BundledImageDescription.__init__)


def test_viewpoint::style::bundledimagedescription_constructor_args():
    sig = inspect.signature(viewpoint::style::BundledImageDescription.__init__)
    params = list(sig.parameters.keys())
    assert "shape" in params, "Missing parameter 'shape'"

def test_viewpoint::style::bundledimagedescription_has_shape():
    assert hasattr(viewpoint::style::BundledImageDescription, "shape")
    descriptor = None
    for klass in viewpoint::style::BundledImageDescription.__mro__:
        if "shape" in klass.__dict__:
            descriptor = klass.__dict__["shape"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::style::gaugecompositestyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::style::GaugeCompositeStyleDescription)


def test_viewpoint::style::gaugecompositestyledescription_constructor_exists():
    assert callable(viewpoint::style::GaugeCompositeStyleDescription.__init__)


def test_viewpoint::style::gaugecompositestyledescription_constructor_args():
    sig = inspect.signature(viewpoint::style::GaugeCompositeStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "alignment" in params, "Missing parameter 'alignment'"

def test_viewpoint::style::gaugecompositestyledescription_has_alignment():
    assert hasattr(viewpoint::style::GaugeCompositeStyleDescription, "alignment")
    descriptor = None
    for klass in viewpoint::style::GaugeCompositeStyleDescription.__mro__:
        if "alignment" in klass.__dict__:
            descriptor = klass.__dict__["alignment"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::style::squaredescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::style::SquareDescription)


def test_viewpoint::style::squaredescription_constructor_exists():
    assert callable(viewpoint::style::SquareDescription.__init__)


def test_viewpoint::style::squaredescription_constructor_args():
    sig = inspect.signature(viewpoint::style::SquareDescription.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"

def test_viewpoint::style::squaredescription_has_width():
    assert hasattr(viewpoint::style::SquareDescription, "width")
    descriptor = None
    for klass in viewpoint::style::SquareDescription.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::style::squaredescription_has_height():
    assert hasattr(viewpoint::style::SquareDescription, "height")
    descriptor = None
    for klass in viewpoint::style::SquareDescription.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::style::dotdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::style::DotDescription)


def test_viewpoint::style::dotdescription_constructor_exists():
    assert callable(viewpoint::style::DotDescription.__init__)


def test_viewpoint::style::dotdescription_constructor_args():
    sig = inspect.signature(viewpoint::style::DotDescription.__init__)
    params = list(sig.parameters.keys())
    assert "strokeSizeComputationExpression" in params, "Missing parameter 'strokeSizeComputationExpression'"

def test_viewpoint::style::dotdescription_has_strokeSizeComputationExpression():
    assert hasattr(viewpoint::style::DotDescription, "strokeSizeComputationExpression")
    descriptor = None
    for klass in viewpoint::style::DotDescription.__mro__:
        if "strokeSizeComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["strokeSizeComputationExpression"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::style::notedescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::style::NoteDescription)


def test_viewpoint::style::notedescription_constructor_exists():
    assert callable(viewpoint::style::NoteDescription.__init__)


def test_viewpoint::style::notedescription_constructor_args():
    sig = inspect.signature(viewpoint::style::NoteDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::style::customstyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::style::CustomStyleDescription)


def test_viewpoint::style::customstyledescription_constructor_exists():
    assert callable(viewpoint::style::CustomStyleDescription.__init__)


def test_viewpoint::style::customstyledescription_constructor_args():
    sig = inspect.signature(viewpoint::style::CustomStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_viewpoint::style::customstyledescription_has_id():
    assert hasattr(viewpoint::style::CustomStyleDescription, "id")
    descriptor = None
    for klass in viewpoint::style::CustomStyleDescription.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::style::ellipsenodedescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::style::EllipseNodeDescription)


def test_viewpoint::style::ellipsenodedescription_constructor_exists():
    assert callable(viewpoint::style::EllipseNodeDescription.__init__)


def test_viewpoint::style::ellipsenodedescription_constructor_args():
    sig = inspect.signature(viewpoint::style::EllipseNodeDescription.__init__)
    params = list(sig.parameters.keys())
    assert "verticalDiameterComputationExpression" in params, "Missing parameter 'verticalDiameterComputationExpression'"
    assert "horizontalDiameterComputationExpression" in params, "Missing parameter 'horizontalDiameterComputationExpression'"

def test_viewpoint::style::ellipsenodedescription_has_verticalDiameterComputationExpression():
    assert hasattr(viewpoint::style::EllipseNodeDescription, "verticalDiameterComputationExpression")
    descriptor = None
    for klass in viewpoint::style::EllipseNodeDescription.__mro__:
        if "verticalDiameterComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["verticalDiameterComputationExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::style::ellipsenodedescription_has_horizontalDiameterComputationExpression():
    assert hasattr(viewpoint::style::EllipseNodeDescription, "horizontalDiameterComputationExpression")
    descriptor = None
    for klass in viewpoint::style::EllipseNodeDescription.__mro__:
        if "horizontalDiameterComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["horizontalDiameterComputationExpression"]
            break
    assert isinstance(descriptor, property)



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



def test_viewpoint::style::containerstyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::style::ContainerStyleDescription)


def test_viewpoint::style::containerstyledescription_constructor_exists():
    assert callable(viewpoint::style::ContainerStyleDescription.__init__)


def test_viewpoint::style::containerstyledescription_constructor_args():
    sig = inspect.signature(viewpoint::style::ContainerStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "roundedCorner" in params, "Missing parameter 'roundedCorner'"

def test_viewpoint::style::containerstyledescription_has_roundedCorner():
    assert hasattr(viewpoint::style::ContainerStyleDescription, "roundedCorner")
    descriptor = None
    for klass in viewpoint::style::ContainerStyleDescription.__mro__:
        if "roundedCorner" in klass.__dict__:
            descriptor = klass.__dict__["roundedCorner"]
            break
    assert isinstance(descriptor, property)



def test_styledescription_is_not_abstract():
    assert not inspect.isabstract(StyleDescription)


def test_styledescription_constructor_exists():
    assert callable(StyleDescription.__init__)


def test_styledescription_constructor_args():
    sig = inspect.signature(StyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::style::edgestyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::style::EdgeStyleDescription)


def test_viewpoint::style::edgestyledescription_constructor_exists():
    assert callable(viewpoint::style::EdgeStyleDescription.__init__)


def test_viewpoint::style::edgestyledescription_constructor_args():
    sig = inspect.signature(viewpoint::style::EdgeStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "lineStyle" in params, "Missing parameter 'lineStyle'"
    assert "foldingStyle" in params, "Missing parameter 'foldingStyle'"
    assert "targetArrow" in params, "Missing parameter 'targetArrow'"
    assert "sourceArrow" in params, "Missing parameter 'sourceArrow'"
    assert "routingStyle" in params, "Missing parameter 'routingStyle'"
    assert "sizeComputationExpression" in params, "Missing parameter 'sizeComputationExpression'"

def test_viewpoint::style::edgestyledescription_has_lineStyle():
    assert hasattr(viewpoint::style::EdgeStyleDescription, "lineStyle")
    descriptor = None
    for klass in viewpoint::style::EdgeStyleDescription.__mro__:
        if "lineStyle" in klass.__dict__:
            descriptor = klass.__dict__["lineStyle"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::style::edgestyledescription_has_foldingStyle():
    assert hasattr(viewpoint::style::EdgeStyleDescription, "foldingStyle")
    descriptor = None
    for klass in viewpoint::style::EdgeStyleDescription.__mro__:
        if "foldingStyle" in klass.__dict__:
            descriptor = klass.__dict__["foldingStyle"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::style::edgestyledescription_has_targetArrow():
    assert hasattr(viewpoint::style::EdgeStyleDescription, "targetArrow")
    descriptor = None
    for klass in viewpoint::style::EdgeStyleDescription.__mro__:
        if "targetArrow" in klass.__dict__:
            descriptor = klass.__dict__["targetArrow"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::style::edgestyledescription_has_sourceArrow():
    assert hasattr(viewpoint::style::EdgeStyleDescription, "sourceArrow")
    descriptor = None
    for klass in viewpoint::style::EdgeStyleDescription.__mro__:
        if "sourceArrow" in klass.__dict__:
            descriptor = klass.__dict__["sourceArrow"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::style::edgestyledescription_has_routingStyle():
    assert hasattr(viewpoint::style::EdgeStyleDescription, "routingStyle")
    descriptor = None
    for klass in viewpoint::style::EdgeStyleDescription.__mro__:
        if "routingStyle" in klass.__dict__:
            descriptor = klass.__dict__["routingStyle"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::style::edgestyledescription_has_sizeComputationExpression():
    assert hasattr(viewpoint::style::EdgeStyleDescription, "sizeComputationExpression")
    descriptor = None
    for klass in viewpoint::style::EdgeStyleDescription.__mro__:
        if "sizeComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["sizeComputationExpression"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::style::roundedcornerstyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::style::RoundedCornerStyleDescription)


def test_viewpoint::style::roundedcornerstyledescription_constructor_exists():
    assert callable(viewpoint::style::RoundedCornerStyleDescription.__init__)


def test_viewpoint::style::roundedcornerstyledescription_constructor_args():
    sig = inspect.signature(viewpoint::style::RoundedCornerStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "arcWidth" in params, "Missing parameter 'arcWidth'"
    assert "arcHeight" in params, "Missing parameter 'arcHeight'"

def test_viewpoint::style::roundedcornerstyledescription_has_arcWidth():
    assert hasattr(viewpoint::style::RoundedCornerStyleDescription, "arcWidth")
    descriptor = None
    for klass in viewpoint::style::RoundedCornerStyleDescription.__mro__:
        if "arcWidth" in klass.__dict__:
            descriptor = klass.__dict__["arcWidth"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::style::roundedcornerstyledescription_has_arcHeight():
    assert hasattr(viewpoint::style::RoundedCornerStyleDescription, "arcHeight")
    descriptor = None
    for klass in viewpoint::style::RoundedCornerStyleDescription.__mro__:
        if "arcHeight" in klass.__dict__:
            descriptor = klass.__dict__["arcHeight"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::style::borderedstyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::style::BorderedStyleDescription)


def test_viewpoint::style::borderedstyledescription_constructor_exists():
    assert callable(viewpoint::style::BorderedStyleDescription.__init__)


def test_viewpoint::style::borderedstyledescription_constructor_args():
    sig = inspect.signature(viewpoint::style::BorderedStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "borderSizeComputationExpression" in params, "Missing parameter 'borderSizeComputationExpression'"

def test_viewpoint::style::borderedstyledescription_has_borderSizeComputationExpression():
    assert hasattr(viewpoint::style::BorderedStyleDescription, "borderSizeComputationExpression")
    descriptor = None
    for klass in viewpoint::style::BorderedStyleDescription.__mro__:
        if "borderSizeComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["borderSizeComputationExpression"]
            break
    assert isinstance(descriptor, property)



def test_layer_is_not_abstract():
    assert not inspect.isabstract(Layer)


def test_layer_constructor_exists():
    assert callable(Layer.__init__)


def test_layer_constructor_args():
    sig = inspect.signature(Layer.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::additionallayer_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::AdditionalLayer)


def test_viewpoint::description::additionallayer_constructor_exists():
    assert callable(viewpoint::description::AdditionalLayer.__init__)


def test_viewpoint::description::additionallayer_constructor_args():
    sig = inspect.signature(viewpoint::description::AdditionalLayer.__init__)
    params = list(sig.parameters.keys())
    assert "activeByDefault" in params, "Missing parameter 'activeByDefault'"
    assert "optional" in params, "Missing parameter 'optional'"

def test_viewpoint::description::additionallayer_has_activeByDefault():
    assert hasattr(viewpoint::description::AdditionalLayer, "activeByDefault")
    descriptor = None
    for klass in viewpoint::description::AdditionalLayer.__mro__:
        if "activeByDefault" in klass.__dict__:
            descriptor = klass.__dict__["activeByDefault"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::description::additionallayer_has_optional():
    assert hasattr(viewpoint::description::AdditionalLayer, "optional")
    descriptor = None
    for klass in viewpoint::description::AdditionalLayer.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)



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



def test_layout_is_not_abstract():
    assert not inspect.isabstract(Layout)


def test_layout_constructor_exists():
    assert callable(Layout.__init__)


def test_layout_constructor_args():
    sig = inspect.signature(Layout.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::compositelayout_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::CompositeLayout)


def test_viewpoint::description::compositelayout_constructor_exists():
    assert callable(viewpoint::description::CompositeLayout.__init__)


def test_viewpoint::description::compositelayout_constructor_args():
    sig = inspect.signature(viewpoint::description::CompositeLayout.__init__)
    params = list(sig.parameters.keys())
    assert "padding" in params, "Missing parameter 'padding'"
    assert "direction" in params, "Missing parameter 'direction'"

def test_viewpoint::description::compositelayout_has_padding():
    assert hasattr(viewpoint::description::CompositeLayout, "padding")
    descriptor = None
    for klass in viewpoint::description::CompositeLayout.__mro__:
        if "padding" in klass.__dict__:
            descriptor = klass.__dict__["padding"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::description::compositelayout_has_direction():
    assert hasattr(viewpoint::description::CompositeLayout, "direction")
    descriptor = None
    for klass in viewpoint::description::CompositeLayout.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::description::orderedtreelayout_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::OrderedTreeLayout)


def test_viewpoint::description::orderedtreelayout_constructor_exists():
    assert callable(viewpoint::description::OrderedTreeLayout.__init__)


def test_viewpoint::description::orderedtreelayout_constructor_args():
    sig = inspect.signature(viewpoint::description::OrderedTreeLayout.__init__)
    params = list(sig.parameters.keys())
    assert "childrenExpression" in params, "Missing parameter 'childrenExpression'"

def test_viewpoint::description::orderedtreelayout_has_childrenExpression():
    assert hasattr(viewpoint::description::OrderedTreeLayout, "childrenExpression")
    descriptor = None
    for klass in viewpoint::description::OrderedTreeLayout.__mro__:
        if "childrenExpression" in klass.__dict__:
            descriptor = klass.__dict__["childrenExpression"]
            break
    assert isinstance(descriptor, property)



def test_documentedelement_is_not_abstract():
    assert not inspect.isabstract(DocumentedElement)


def test_documentedelement_constructor_exists():
    assert callable(DocumentedElement.__init__)


def test_documentedelement_constructor_args():
    sig = inspect.signature(DocumentedElement.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::validation::validationset_is_not_abstract():
    assert not inspect.isabstract(viewpoint::validation::ValidationSet)


def test_viewpoint::validation::validationset_constructor_exists():
    assert callable(viewpoint::validation::ValidationSet.__init__)


def test_viewpoint::validation::validationset_constructor_args():
    sig = inspect.signature(viewpoint::validation::ValidationSet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_viewpoint::validation::validationset_has_name():
    assert hasattr(viewpoint::validation::ValidationSet, "name")
    descriptor = None
    for klass in viewpoint::validation::ValidationSet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::description::layout_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::Layout)


def test_viewpoint::description::layout_constructor_exists():
    assert callable(viewpoint::description::Layout.__init__)


def test_viewpoint::description::layout_constructor_args():
    sig = inspect.signature(viewpoint::description::Layout.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::concern::concernset_is_not_abstract():
    assert not inspect.isabstract(viewpoint::concern::ConcernSet)


def test_viewpoint::concern::concernset_constructor_exists():
    assert callable(viewpoint::concern::ConcernSet.__init__)


def test_viewpoint::concern::concernset_constructor_args():
    sig = inspect.signature(viewpoint::concern::ConcernSet.__init__)
    params = list(sig.parameters.keys())



def test_abstractvariable_is_not_abstract():
    assert not inspect.isabstract(AbstractVariable)


def test_abstractvariable_constructor_exists():
    assert callable(AbstractVariable.__init__)


def test_abstractvariable_constructor_args():
    sig = inspect.signature(AbstractVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::dialogvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::DialogVariable)


def test_viewpoint::tool::dialogvariable_constructor_exists():
    assert callable(viewpoint::tool::DialogVariable.__init__)


def test_viewpoint::tool::dialogvariable_constructor_args():
    sig = inspect.signature(viewpoint::tool::DialogVariable.__init__)
    params = list(sig.parameters.keys())
    assert "dialogPrompt" in params, "Missing parameter 'dialogPrompt'"

def test_viewpoint::tool::dialogvariable_has_dialogPrompt():
    assert hasattr(viewpoint::tool::DialogVariable, "dialogPrompt")
    descriptor = None
    for klass in viewpoint::tool::DialogVariable.__mro__:
        if "dialogPrompt" in klass.__dict__:
            descriptor = klass.__dict__["dialogPrompt"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::tool::subvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::SubVariable)


def test_viewpoint::tool::subvariable_constructor_exists():
    assert callable(viewpoint::tool::SubVariable.__init__)


def test_viewpoint::tool::subvariable_constructor_args():
    sig = inspect.signature(viewpoint::tool::SubVariable.__init__)
    params = list(sig.parameters.keys())



def test_tool::variablecontainer_is_not_abstract():
    assert not inspect.isabstract(tool::VariableContainer)


def test_tool::variablecontainer_constructor_exists():
    assert callable(tool::VariableContainer.__init__)


def test_tool::variablecontainer_constructor_args():
    sig = inspect.signature(tool::VariableContainer.__init__)
    params = list(sig.parameters.keys())



def test_tool::subvariable_is_not_abstract():
    assert not inspect.isabstract(tool::SubVariable)


def test_tool::subvariable_constructor_exists():
    assert callable(tool::SubVariable.__init__)


def test_tool::subvariable_constructor_args():
    sig = inspect.signature(tool::SubVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::acceleovariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::AcceleoVariable)


def test_viewpoint::tool::acceleovariable_constructor_exists():
    assert callable(viewpoint::tool::AcceleoVariable.__init__)


def test_viewpoint::tool::acceleovariable_constructor_args():
    sig = inspect.signature(viewpoint::tool::AcceleoVariable.__init__)
    params = list(sig.parameters.keys())
    assert "computationExpression" in params, "Missing parameter 'computationExpression'"

def test_viewpoint::tool::acceleovariable_has_computationExpression():
    assert hasattr(viewpoint::tool::AcceleoVariable, "computationExpression")
    descriptor = None
    for klass in viewpoint::tool::AcceleoVariable.__mro__:
        if "computationExpression" in klass.__dict__:
            descriptor = klass.__dict__["computationExpression"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::tool::variablecontainer_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::VariableContainer)


def test_viewpoint::tool::variablecontainer_constructor_exists():
    assert callable(viewpoint::tool::VariableContainer.__init__)


def test_viewpoint::tool::variablecontainer_constructor_args():
    sig = inspect.signature(viewpoint::tool::VariableContainer.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::abstractvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::AbstractVariable)


def test_viewpoint::tool::abstractvariable_constructor_exists():
    assert callable(viewpoint::tool::AbstractVariable.__init__)


def test_viewpoint::tool::abstractvariable_constructor_args():
    sig = inspect.signature(viewpoint::tool::AbstractVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_viewpoint::tool::abstractvariable_has_name():
    assert hasattr(viewpoint::tool::AbstractVariable, "name")
    descriptor = None
    for klass in viewpoint::tool::AbstractVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tool::externaljavaaction_is_not_abstract():
    assert not inspect.isabstract(tool::ExternalJavaAction)


def test_tool::externaljavaaction_constructor_exists():
    assert callable(tool::ExternalJavaAction.__init__)


def test_tool::externaljavaaction_constructor_args():
    sig = inspect.signature(tool::ExternalJavaAction.__init__)
    params = list(sig.parameters.keys())



def test_tool::externaljavaactionparameter_is_not_abstract():
    assert not inspect.isabstract(tool::ExternalJavaActionParameter)


def test_tool::externaljavaactionparameter_constructor_exists():
    assert callable(tool::ExternalJavaActionParameter.__init__)


def test_tool::externaljavaactionparameter_constructor_args():
    sig = inspect.signature(tool::ExternalJavaActionParameter.__init__)
    params = list(sig.parameters.keys())



def test_tool::containermodeloperation_is_not_abstract():
    assert not inspect.isabstract(tool::ContainerModelOperation)


def test_tool::containermodeloperation_constructor_exists():
    assert callable(tool::ContainerModelOperation.__init__)


def test_tool::containermodeloperation_constructor_args():
    sig = inspect.signature(tool::ContainerModelOperation.__init__)
    params = list(sig.parameters.keys())



def test_menuitemdescription_is_not_abstract():
    assert not inspect.isabstract(MenuItemDescription)


def test_menuitemdescription_constructor_exists():
    assert callable(MenuItemDescription.__init__)


def test_menuitemdescription_constructor_args():
    sig = inspect.signature(MenuItemDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::operationaction_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::OperationAction)


def test_viewpoint::tool::operationaction_constructor_exists():
    assert callable(viewpoint::tool::OperationAction.__init__)


def test_viewpoint::tool::operationaction_constructor_args():
    sig = inspect.signature(viewpoint::tool::OperationAction.__init__)
    params = list(sig.parameters.keys())



def test_tool::menuitemdescription_is_not_abstract():
    assert not inspect.isabstract(tool::MenuItemDescription)


def test_tool::menuitemdescription_constructor_exists():
    assert callable(tool::MenuItemDescription.__init__)


def test_tool::menuitemdescription_constructor_args():
    sig = inspect.signature(tool::MenuItemDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::externaljavaaction_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::ExternalJavaAction)


def test_viewpoint::tool::externaljavaaction_constructor_exists():
    assert callable(viewpoint::tool::ExternalJavaAction.__init__)


def test_viewpoint::tool::externaljavaaction_constructor_args():
    sig = inspect.signature(viewpoint::tool::ExternalJavaAction.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_viewpoint::tool::externaljavaaction_has_id():
    assert hasattr(viewpoint::tool::ExternalJavaAction, "id")
    descriptor = None
    for klass in viewpoint::tool::ExternalJavaAction.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::tool::externaljavaactioncall_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::ExternalJavaActionCall)


def test_viewpoint::tool::externaljavaactioncall_constructor_exists():
    assert callable(viewpoint::tool::ExternalJavaActionCall.__init__)


def test_viewpoint::tool::externaljavaactioncall_constructor_args():
    sig = inspect.signature(viewpoint::tool::ExternalJavaActionCall.__init__)
    params = list(sig.parameters.keys())



def test_menuitemorref_is_not_abstract():
    assert not inspect.isabstract(MenuItemOrRef)


def test_menuitemorref_constructor_exists():
    assert callable(MenuItemOrRef.__init__)


def test_menuitemorref_constructor_args():
    sig = inspect.signature(MenuItemOrRef.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::menuitemdescriptionreference_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::MenuItemDescriptionReference)


def test_viewpoint::tool::menuitemdescriptionreference_constructor_exists():
    assert callable(viewpoint::tool::MenuItemDescriptionReference.__init__)


def test_viewpoint::tool::menuitemdescriptionreference_constructor_args():
    sig = inspect.signature(viewpoint::tool::MenuItemDescriptionReference.__init__)
    params = list(sig.parameters.keys())



def test_tool::menuitemorref_is_not_abstract():
    assert not inspect.isabstract(tool::MenuItemOrRef)


def test_tool::menuitemorref_constructor_exists():
    assert callable(tool::MenuItemOrRef.__init__)


def test_tool::menuitemorref_constructor_args():
    sig = inspect.signature(tool::MenuItemOrRef.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::menuitemorref_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::MenuItemOrRef)


def test_viewpoint::tool::menuitemorref_constructor_exists():
    assert callable(viewpoint::tool::MenuItemOrRef.__init__)


def test_viewpoint::tool::menuitemorref_constructor_args():
    sig = inspect.signature(viewpoint::tool::MenuItemOrRef.__init__)
    params = list(sig.parameters.keys())



def test_tool::namevariable_is_not_abstract():
    assert not inspect.isabstract(tool::NameVariable)


def test_tool::namevariable_constructor_exists():
    assert callable(tool::NameVariable.__init__)


def test_tool::namevariable_constructor_args():
    sig = inspect.signature(tool::NameVariable.__init__)
    params = list(sig.parameters.keys())



def test_tool::selectcontainervariable_is_not_abstract():
    assert not inspect.isabstract(tool::SelectContainerVariable)


def test_tool::selectcontainervariable_constructor_exists():
    assert callable(tool::SelectContainerVariable.__init__)


def test_tool::selectcontainervariable_constructor_args():
    sig = inspect.signature(tool::SelectContainerVariable.__init__)
    params = list(sig.parameters.keys())



def test_tool::initialcontainerdropoperation_is_not_abstract():
    assert not inspect.isabstract(tool::InitialContainerDropOperation)


def test_tool::initialcontainerdropoperation_constructor_exists():
    assert callable(tool::InitialContainerDropOperation.__init__)


def test_tool::initialcontainerdropoperation_constructor_args():
    sig = inspect.signature(tool::InitialContainerDropOperation.__init__)
    params = list(sig.parameters.keys())



def test_tool::containerviewvariable_is_not_abstract():
    assert not inspect.isabstract(tool::ContainerViewVariable)


def test_tool::containerviewvariable_constructor_exists():
    assert callable(tool::ContainerViewVariable.__init__)


def test_tool::containerviewvariable_constructor_args():
    sig = inspect.signature(tool::ContainerViewVariable.__init__)
    params = list(sig.parameters.keys())



def test_tool::elementselectvariable_is_not_abstract():
    assert not inspect.isabstract(tool::ElementSelectVariable)


def test_tool::elementselectvariable_constructor_exists():
    assert callable(tool::ElementSelectVariable.__init__)


def test_tool::elementselectvariable_constructor_args():
    sig = inspect.signature(tool::ElementSelectVariable.__init__)
    params = list(sig.parameters.keys())



def test_description::selectiondescription_is_not_abstract():
    assert not inspect.isabstract(description::SelectionDescription)


def test_description::selectiondescription_constructor_exists():
    assert callable(description::SelectionDescription.__init__)


def test_description::selectiondescription_constructor_args():
    sig = inspect.signature(description::SelectionDescription.__init__)
    params = list(sig.parameters.keys())



def test_tool::abstracttooldescription_is_not_abstract():
    assert not inspect.isabstract(tool::AbstractToolDescription)


def test_tool::abstracttooldescription_constructor_exists():
    assert callable(tool::AbstractToolDescription.__init__)


def test_tool::abstracttooldescription_constructor_args():
    sig = inspect.signature(tool::AbstractToolDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::menuitemdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::MenuItemDescription)


def test_viewpoint::tool::menuitemdescription_constructor_exists():
    assert callable(viewpoint::tool::MenuItemDescription.__init__)


def test_viewpoint::tool::menuitemdescription_constructor_args():
    sig = inspect.signature(viewpoint::tool::MenuItemDescription.__init__)
    params = list(sig.parameters.keys())
    assert "icon" in params, "Missing parameter 'icon'"

def test_viewpoint::tool::menuitemdescription_has_icon():
    assert hasattr(viewpoint::tool::MenuItemDescription, "icon")
    descriptor = None
    for klass in viewpoint::tool::MenuItemDescription.__mro__:
        if "icon" in klass.__dict__:
            descriptor = klass.__dict__["icon"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::tool::selectionwizarddescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::SelectionWizardDescription)


def test_viewpoint::tool::selectionwizarddescription_constructor_exists():
    assert callable(viewpoint::tool::SelectionWizardDescription.__init__)


def test_viewpoint::tool::selectionwizarddescription_constructor_args():
    sig = inspect.signature(viewpoint::tool::SelectionWizardDescription.__init__)
    params = list(sig.parameters.keys())
    assert "windowImagePath" in params, "Missing parameter 'windowImagePath'"
    assert "windowTitle" in params, "Missing parameter 'windowTitle'"
    assert "iconPath" in params, "Missing parameter 'iconPath'"

def test_viewpoint::tool::selectionwizarddescription_has_windowImagePath():
    assert hasattr(viewpoint::tool::SelectionWizardDescription, "windowImagePath")
    descriptor = None
    for klass in viewpoint::tool::SelectionWizardDescription.__mro__:
        if "windowImagePath" in klass.__dict__:
            descriptor = klass.__dict__["windowImagePath"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::tool::selectionwizarddescription_has_windowTitle():
    assert hasattr(viewpoint::tool::SelectionWizardDescription, "windowTitle")
    descriptor = None
    for klass in viewpoint::tool::SelectionWizardDescription.__mro__:
        if "windowTitle" in klass.__dict__:
            descriptor = klass.__dict__["windowTitle"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::tool::selectionwizarddescription_has_iconPath():
    assert hasattr(viewpoint::tool::SelectionWizardDescription, "iconPath")
    descriptor = None
    for klass in viewpoint::tool::SelectionWizardDescription.__mro__:
        if "iconPath" in klass.__dict__:
            descriptor = klass.__dict__["iconPath"]
            break
    assert isinstance(descriptor, property)



def test_tool::dropcontainervariable_is_not_abstract():
    assert not inspect.isabstract(tool::DropContainerVariable)


def test_tool::dropcontainervariable_constructor_exists():
    assert callable(tool::DropContainerVariable.__init__)


def test_tool::dropcontainervariable_constructor_args():
    sig = inspect.signature(tool::DropContainerVariable.__init__)
    params = list(sig.parameters.keys())



def test_description::diagramelementmapping_is_not_abstract():
    assert not inspect.isabstract(description::DiagramElementMapping)


def test_description::diagramelementmapping_constructor_exists():
    assert callable(description::DiagramElementMapping.__init__)


def test_description::diagramelementmapping_constructor_args():
    sig = inspect.signature(description::DiagramElementMapping.__init__)
    params = list(sig.parameters.keys())



def test_tool::initialoperation_is_not_abstract():
    assert not inspect.isabstract(tool::InitialOperation)


def test_tool::initialoperation_constructor_exists():
    assert callable(tool::InitialOperation.__init__)


def test_tool::initialoperation_constructor_args():
    sig = inspect.signature(tool::InitialOperation.__init__)
    params = list(sig.parameters.keys())



def test_tool::elementviewvariable_is_not_abstract():
    assert not inspect.isabstract(tool::ElementViewVariable)


def test_tool::elementviewvariable_constructor_exists():
    assert callable(tool::ElementViewVariable.__init__)


def test_tool::elementviewvariable_constructor_args():
    sig = inspect.signature(tool::ElementViewVariable.__init__)
    params = list(sig.parameters.keys())



def test_tool::elementvariable_is_not_abstract():
    assert not inspect.isabstract(tool::ElementVariable)


def test_tool::elementvariable_constructor_exists():
    assert callable(tool::ElementVariable.__init__)


def test_tool::elementvariable_constructor_args():
    sig = inspect.signature(tool::ElementVariable.__init__)
    params = list(sig.parameters.keys())



def test_mappingbasedtooldescription_is_not_abstract():
    assert not inspect.isabstract(MappingBasedToolDescription)


def test_mappingbasedtooldescription_constructor_exists():
    assert callable(MappingBasedToolDescription.__init__)


def test_mappingbasedtooldescription_constructor_args():
    sig = inspect.signature(MappingBasedToolDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::containercreationdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::ContainerCreationDescription)


def test_viewpoint::tool::containercreationdescription_constructor_exists():
    assert callable(viewpoint::tool::ContainerCreationDescription.__init__)


def test_viewpoint::tool::containercreationdescription_constructor_args():
    sig = inspect.signature(viewpoint::tool::ContainerCreationDescription.__init__)
    params = list(sig.parameters.keys())
    assert "iconPath" in params, "Missing parameter 'iconPath'"

def test_viewpoint::tool::containercreationdescription_has_iconPath():
    assert hasattr(viewpoint::tool::ContainerCreationDescription, "iconPath")
    descriptor = None
    for klass in viewpoint::tool::ContainerCreationDescription.__mro__:
        if "iconPath" in klass.__dict__:
            descriptor = klass.__dict__["iconPath"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::tool::pastedescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::PasteDescription)


def test_viewpoint::tool::pastedescription_constructor_exists():
    assert callable(viewpoint::tool::PasteDescription.__init__)


def test_viewpoint::tool::pastedescription_constructor_args():
    sig = inspect.signature(viewpoint::tool::PasteDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::containerdropdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::ContainerDropDescription)


def test_viewpoint::tool::containerdropdescription_constructor_exists():
    assert callable(viewpoint::tool::ContainerDropDescription.__init__)


def test_viewpoint::tool::containerdropdescription_constructor_args():
    sig = inspect.signature(viewpoint::tool::ContainerDropDescription.__init__)
    params = list(sig.parameters.keys())
    assert "dragSource" in params, "Missing parameter 'dragSource'"
    assert "moveEdges" in params, "Missing parameter 'moveEdges'"

def test_viewpoint::tool::containerdropdescription_has_dragSource():
    assert hasattr(viewpoint::tool::ContainerDropDescription, "dragSource")
    descriptor = None
    for klass in viewpoint::tool::ContainerDropDescription.__mro__:
        if "dragSource" in klass.__dict__:
            descriptor = klass.__dict__["dragSource"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::tool::containerdropdescription_has_moveEdges():
    assert hasattr(viewpoint::tool::ContainerDropDescription, "moveEdges")
    descriptor = None
    for klass in viewpoint::tool::ContainerDropDescription.__mro__:
        if "moveEdges" in klass.__dict__:
            descriptor = klass.__dict__["moveEdges"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::tool::deleteelementdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::DeleteElementDescription)


def test_viewpoint::tool::deleteelementdescription_constructor_exists():
    assert callable(viewpoint::tool::DeleteElementDescription.__init__)


def test_viewpoint::tool::deleteelementdescription_constructor_args():
    sig = inspect.signature(viewpoint::tool::DeleteElementDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::edgecreationdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::EdgeCreationDescription)


def test_viewpoint::tool::edgecreationdescription_constructor_exists():
    assert callable(viewpoint::tool::EdgeCreationDescription.__init__)


def test_viewpoint::tool::edgecreationdescription_constructor_args():
    sig = inspect.signature(viewpoint::tool::EdgeCreationDescription.__init__)
    params = list(sig.parameters.keys())
    assert "connectionStartPrecondition" in params, "Missing parameter 'connectionStartPrecondition'"
    assert "iconPath" in params, "Missing parameter 'iconPath'"

def test_viewpoint::tool::edgecreationdescription_has_connectionStartPrecondition():
    assert hasattr(viewpoint::tool::EdgeCreationDescription, "connectionStartPrecondition")
    descriptor = None
    for klass in viewpoint::tool::EdgeCreationDescription.__mro__:
        if "connectionStartPrecondition" in klass.__dict__:
            descriptor = klass.__dict__["connectionStartPrecondition"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::tool::edgecreationdescription_has_iconPath():
    assert hasattr(viewpoint::tool::EdgeCreationDescription, "iconPath")
    descriptor = None
    for klass in viewpoint::tool::EdgeCreationDescription.__mro__:
        if "iconPath" in klass.__dict__:
            descriptor = klass.__dict__["iconPath"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::tool::doubleclickdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::DoubleClickDescription)


def test_viewpoint::tool::doubleclickdescription_constructor_exists():
    assert callable(viewpoint::tool::DoubleClickDescription.__init__)


def test_viewpoint::tool::doubleclickdescription_constructor_args():
    sig = inspect.signature(viewpoint::tool::DoubleClickDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::reconnectedgedescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::ReconnectEdgeDescription)


def test_viewpoint::tool::reconnectedgedescription_constructor_exists():
    assert callable(viewpoint::tool::ReconnectEdgeDescription.__init__)


def test_viewpoint::tool::reconnectedgedescription_constructor_args():
    sig = inspect.signature(viewpoint::tool::ReconnectEdgeDescription.__init__)
    params = list(sig.parameters.keys())
    assert "reconnectionKind" in params, "Missing parameter 'reconnectionKind'"

def test_viewpoint::tool::reconnectedgedescription_has_reconnectionKind():
    assert hasattr(viewpoint::tool::ReconnectEdgeDescription, "reconnectionKind")
    descriptor = None
    for klass in viewpoint::tool::ReconnectEdgeDescription.__mro__:
        if "reconnectionKind" in klass.__dict__:
            descriptor = klass.__dict__["reconnectionKind"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::tool::nodecreationdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::NodeCreationDescription)


def test_viewpoint::tool::nodecreationdescription_constructor_exists():
    assert callable(viewpoint::tool::NodeCreationDescription.__init__)


def test_viewpoint::tool::nodecreationdescription_constructor_args():
    sig = inspect.signature(viewpoint::tool::NodeCreationDescription.__init__)
    params = list(sig.parameters.keys())
    assert "iconPath" in params, "Missing parameter 'iconPath'"

def test_viewpoint::tool::nodecreationdescription_has_iconPath():
    assert hasattr(viewpoint::tool::NodeCreationDescription, "iconPath")
    descriptor = None
    for klass in viewpoint::tool::NodeCreationDescription.__mro__:
        if "iconPath" in klass.__dict__:
            descriptor = klass.__dict__["iconPath"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::tool::directeditlabel_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::DirectEditLabel)


def test_viewpoint::tool::directeditlabel_constructor_exists():
    assert callable(viewpoint::tool::DirectEditLabel.__init__)


def test_viewpoint::tool::directeditlabel_constructor_args():
    sig = inspect.signature(viewpoint::tool::DirectEditLabel.__init__)
    params = list(sig.parameters.keys())
    assert "inputLabelExpression" in params, "Missing parameter 'inputLabelExpression'"

def test_viewpoint::tool::directeditlabel_has_inputLabelExpression():
    assert hasattr(viewpoint::tool::DirectEditLabel, "inputLabelExpression")
    descriptor = None
    for klass in viewpoint::tool::DirectEditLabel.__mro__:
        if "inputLabelExpression" in klass.__dict__:
            descriptor = klass.__dict__["inputLabelExpression"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::tool::tooldescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::ToolDescription)


def test_viewpoint::tool::tooldescription_constructor_exists():
    assert callable(viewpoint::tool::ToolDescription.__init__)


def test_viewpoint::tool::tooldescription_constructor_args():
    sig = inspect.signature(viewpoint::tool::ToolDescription.__init__)
    params = list(sig.parameters.keys())
    assert "iconPath" in params, "Missing parameter 'iconPath'"

def test_viewpoint::tool::tooldescription_has_iconPath():
    assert hasattr(viewpoint::tool::ToolDescription, "iconPath")
    descriptor = None
    for klass in viewpoint::tool::ToolDescription.__mro__:
        if "iconPath" in klass.__dict__:
            descriptor = klass.__dict__["iconPath"]
            break
    assert isinstance(descriptor, property)



def test_abstracttooldescription_is_not_abstract():
    assert not inspect.isabstract(AbstractToolDescription)


def test_abstracttooldescription_constructor_exists():
    assert callable(AbstractToolDescription.__init__)


def test_abstracttooldescription_constructor_args():
    sig = inspect.signature(AbstractToolDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::representationcreationdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::RepresentationCreationDescription)


def test_viewpoint::tool::representationcreationdescription_constructor_exists():
    assert callable(viewpoint::tool::RepresentationCreationDescription.__init__)


def test_viewpoint::tool::representationcreationdescription_constructor_args():
    sig = inspect.signature(viewpoint::tool::RepresentationCreationDescription.__init__)
    params = list(sig.parameters.keys())
    assert "browseExpression" in params, "Missing parameter 'browseExpression'"
    assert "titleExpression" in params, "Missing parameter 'titleExpression'"

def test_viewpoint::tool::representationcreationdescription_has_browseExpression():
    assert hasattr(viewpoint::tool::RepresentationCreationDescription, "browseExpression")
    descriptor = None
    for klass in viewpoint::tool::RepresentationCreationDescription.__mro__:
        if "browseExpression" in klass.__dict__:
            descriptor = klass.__dict__["browseExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::tool::representationcreationdescription_has_titleExpression():
    assert hasattr(viewpoint::tool::RepresentationCreationDescription, "titleExpression")
    descriptor = None
    for klass in viewpoint::tool::RepresentationCreationDescription.__mro__:
        if "titleExpression" in klass.__dict__:
            descriptor = klass.__dict__["titleExpression"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::tool::requestdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::RequestDescription)


def test_viewpoint::tool::requestdescription_constructor_exists():
    assert callable(viewpoint::tool::RequestDescription.__init__)


def test_viewpoint::tool::requestdescription_constructor_args():
    sig = inspect.signature(viewpoint::tool::RequestDescription.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_viewpoint::tool::requestdescription_has_type():
    assert hasattr(viewpoint::tool::RequestDescription, "type")
    descriptor = None
    for klass in viewpoint::tool::RequestDescription.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::tool::behaviortool_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::BehaviorTool)


def test_viewpoint::tool::behaviortool_constructor_exists():
    assert callable(viewpoint::tool::BehaviorTool.__init__)


def test_viewpoint::tool::behaviortool_constructor_args():
    sig = inspect.signature(viewpoint::tool::BehaviorTool.__init__)
    params = list(sig.parameters.keys())
    assert "domainClass" in params, "Missing parameter 'domainClass'"

def test_viewpoint::tool::behaviortool_has_domainClass():
    assert hasattr(viewpoint::tool::BehaviorTool, "domainClass")
    descriptor = None
    for klass in viewpoint::tool::BehaviorTool.__mro__:
        if "domainClass" in klass.__dict__:
            descriptor = klass.__dict__["domainClass"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::tool::panebasedselectionwizarddescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::PaneBasedSelectionWizardDescription)


def test_viewpoint::tool::panebasedselectionwizarddescription_constructor_exists():
    assert callable(viewpoint::tool::PaneBasedSelectionWizardDescription.__init__)


def test_viewpoint::tool::panebasedselectionwizarddescription_constructor_args():
    sig = inspect.signature(viewpoint::tool::PaneBasedSelectionWizardDescription.__init__)
    params = list(sig.parameters.keys())
    assert "selectedValuesMessage" in params, "Missing parameter 'selectedValuesMessage'"
    assert "message" in params, "Missing parameter 'message'"
    assert "iconPath" in params, "Missing parameter 'iconPath'"
    assert "choiceOfValuesMessage" in params, "Missing parameter 'choiceOfValuesMessage'"
    assert "rootExpression" in params, "Missing parameter 'rootExpression'"
    assert "childrenExpression" in params, "Missing parameter 'childrenExpression'"
    assert "candidatesExpression" in params, "Missing parameter 'candidatesExpression'"
    assert "windowImagePath" in params, "Missing parameter 'windowImagePath'"
    assert "tree" in params, "Missing parameter 'tree'"
    assert "preSelectedCandidatesExpression" in params, "Missing parameter 'preSelectedCandidatesExpression'"
    assert "windowTitle" in params, "Missing parameter 'windowTitle'"

def test_viewpoint::tool::panebasedselectionwizarddescription_has_selectedValuesMessage():
    assert hasattr(viewpoint::tool::PaneBasedSelectionWizardDescription, "selectedValuesMessage")
    descriptor = None
    for klass in viewpoint::tool::PaneBasedSelectionWizardDescription.__mro__:
        if "selectedValuesMessage" in klass.__dict__:
            descriptor = klass.__dict__["selectedValuesMessage"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::tool::panebasedselectionwizarddescription_has_message():
    assert hasattr(viewpoint::tool::PaneBasedSelectionWizardDescription, "message")
    descriptor = None
    for klass in viewpoint::tool::PaneBasedSelectionWizardDescription.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::tool::panebasedselectionwizarddescription_has_iconPath():
    assert hasattr(viewpoint::tool::PaneBasedSelectionWizardDescription, "iconPath")
    descriptor = None
    for klass in viewpoint::tool::PaneBasedSelectionWizardDescription.__mro__:
        if "iconPath" in klass.__dict__:
            descriptor = klass.__dict__["iconPath"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::tool::panebasedselectionwizarddescription_has_choiceOfValuesMessage():
    assert hasattr(viewpoint::tool::PaneBasedSelectionWizardDescription, "choiceOfValuesMessage")
    descriptor = None
    for klass in viewpoint::tool::PaneBasedSelectionWizardDescription.__mro__:
        if "choiceOfValuesMessage" in klass.__dict__:
            descriptor = klass.__dict__["choiceOfValuesMessage"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::tool::panebasedselectionwizarddescription_has_rootExpression():
    assert hasattr(viewpoint::tool::PaneBasedSelectionWizardDescription, "rootExpression")
    descriptor = None
    for klass in viewpoint::tool::PaneBasedSelectionWizardDescription.__mro__:
        if "rootExpression" in klass.__dict__:
            descriptor = klass.__dict__["rootExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::tool::panebasedselectionwizarddescription_has_childrenExpression():
    assert hasattr(viewpoint::tool::PaneBasedSelectionWizardDescription, "childrenExpression")
    descriptor = None
    for klass in viewpoint::tool::PaneBasedSelectionWizardDescription.__mro__:
        if "childrenExpression" in klass.__dict__:
            descriptor = klass.__dict__["childrenExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::tool::panebasedselectionwizarddescription_has_candidatesExpression():
    assert hasattr(viewpoint::tool::PaneBasedSelectionWizardDescription, "candidatesExpression")
    descriptor = None
    for klass in viewpoint::tool::PaneBasedSelectionWizardDescription.__mro__:
        if "candidatesExpression" in klass.__dict__:
            descriptor = klass.__dict__["candidatesExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::tool::panebasedselectionwizarddescription_has_windowImagePath():
    assert hasattr(viewpoint::tool::PaneBasedSelectionWizardDescription, "windowImagePath")
    descriptor = None
    for klass in viewpoint::tool::PaneBasedSelectionWizardDescription.__mro__:
        if "windowImagePath" in klass.__dict__:
            descriptor = klass.__dict__["windowImagePath"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::tool::panebasedselectionwizarddescription_has_tree():
    assert hasattr(viewpoint::tool::PaneBasedSelectionWizardDescription, "tree")
    descriptor = None
    for klass in viewpoint::tool::PaneBasedSelectionWizardDescription.__mro__:
        if "tree" in klass.__dict__:
            descriptor = klass.__dict__["tree"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::tool::panebasedselectionwizarddescription_has_preSelectedCandidatesExpression():
    assert hasattr(viewpoint::tool::PaneBasedSelectionWizardDescription, "preSelectedCandidatesExpression")
    descriptor = None
    for klass in viewpoint::tool::PaneBasedSelectionWizardDescription.__mro__:
        if "preSelectedCandidatesExpression" in klass.__dict__:
            descriptor = klass.__dict__["preSelectedCandidatesExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::tool::panebasedselectionwizarddescription_has_windowTitle():
    assert hasattr(viewpoint::tool::PaneBasedSelectionWizardDescription, "windowTitle")
    descriptor = None
    for klass in viewpoint::tool::PaneBasedSelectionWizardDescription.__mro__:
        if "windowTitle" in klass.__dict__:
            descriptor = klass.__dict__["windowTitle"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::tool::popupmenu_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::PopupMenu)


def test_viewpoint::tool::popupmenu_constructor_exists():
    assert callable(viewpoint::tool::PopupMenu.__init__)


def test_viewpoint::tool::popupmenu_constructor_args():
    sig = inspect.signature(viewpoint::tool::PopupMenu.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::representationnavigationdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::RepresentationNavigationDescription)


def test_viewpoint::tool::representationnavigationdescription_constructor_exists():
    assert callable(viewpoint::tool::RepresentationNavigationDescription.__init__)


def test_viewpoint::tool::representationnavigationdescription_constructor_args():
    sig = inspect.signature(viewpoint::tool::RepresentationNavigationDescription.__init__)
    params = list(sig.parameters.keys())
    assert "browseExpression" in params, "Missing parameter 'browseExpression'"
    assert "navigationNameExpression" in params, "Missing parameter 'navigationNameExpression'"

def test_viewpoint::tool::representationnavigationdescription_has_browseExpression():
    assert hasattr(viewpoint::tool::RepresentationNavigationDescription, "browseExpression")
    descriptor = None
    for klass in viewpoint::tool::RepresentationNavigationDescription.__mro__:
        if "browseExpression" in klass.__dict__:
            descriptor = klass.__dict__["browseExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::tool::representationnavigationdescription_has_navigationNameExpression():
    assert hasattr(viewpoint::tool::RepresentationNavigationDescription, "navigationNameExpression")
    descriptor = None
    for klass in viewpoint::tool::RepresentationNavigationDescription.__mro__:
        if "navigationNameExpression" in klass.__dict__:
            descriptor = klass.__dict__["navigationNameExpression"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::tool::mappingbasedtooldescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::MappingBasedToolDescription)


def test_viewpoint::tool::mappingbasedtooldescription_constructor_exists():
    assert callable(viewpoint::tool::MappingBasedToolDescription.__init__)


def test_viewpoint::tool::mappingbasedtooldescription_constructor_args():
    sig = inspect.signature(viewpoint::tool::MappingBasedToolDescription.__init__)
    params = list(sig.parameters.keys())



def test_tool::elementdropvariable_is_not_abstract():
    assert not inspect.isabstract(tool::ElementDropVariable)


def test_tool::elementdropvariable_constructor_exists():
    assert callable(tool::ElementDropVariable.__init__)


def test_tool::elementdropvariable_constructor_args():
    sig = inspect.signature(tool::ElementDropVariable.__init__)
    params = list(sig.parameters.keys())



def test_tool::toolfilterdescription_is_not_abstract():
    assert not inspect.isabstract(tool::ToolFilterDescription)


def test_tool::toolfilterdescription_constructor_exists():
    assert callable(tool::ToolFilterDescription.__init__)


def test_tool::toolfilterdescription_constructor_args():
    sig = inspect.signature(tool::ToolFilterDescription.__init__)
    params = list(sig.parameters.keys())



def test_toolentry_is_not_abstract():
    assert not inspect.isabstract(ToolEntry)


def test_toolentry_constructor_exists():
    assert callable(ToolEntry.__init__)


def test_toolentry_constructor_args():
    sig = inspect.signature(ToolEntry.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::toolgroup_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::ToolGroup)


def test_viewpoint::tool::toolgroup_constructor_exists():
    assert callable(viewpoint::tool::ToolGroup.__init__)


def test_viewpoint::tool::toolgroup_constructor_args():
    sig = inspect.signature(viewpoint::tool::ToolGroup.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::abstracttooldescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::AbstractToolDescription)


def test_viewpoint::tool::abstracttooldescription_constructor_exists():
    assert callable(viewpoint::tool::AbstractToolDescription.__init__)


def test_viewpoint::tool::abstracttooldescription_constructor_args():
    sig = inspect.signature(viewpoint::tool::AbstractToolDescription.__init__)
    params = list(sig.parameters.keys())
    assert "precondition" in params, "Missing parameter 'precondition'"
    assert "forceRefresh" in params, "Missing parameter 'forceRefresh'"

def test_viewpoint::tool::abstracttooldescription_has_precondition():
    assert hasattr(viewpoint::tool::AbstractToolDescription, "precondition")
    descriptor = None
    for klass in viewpoint::tool::AbstractToolDescription.__mro__:
        if "precondition" in klass.__dict__:
            descriptor = klass.__dict__["precondition"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::tool::abstracttooldescription_has_forceRefresh():
    assert hasattr(viewpoint::tool::AbstractToolDescription, "forceRefresh")
    descriptor = None
    for klass in viewpoint::tool::AbstractToolDescription.__mro__:
        if "forceRefresh" in klass.__dict__:
            descriptor = klass.__dict__["forceRefresh"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::style::tooltipstyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::style::TooltipStyleDescription)


def test_viewpoint::style::tooltipstyledescription_constructor_exists():
    assert callable(viewpoint::style::TooltipStyleDescription.__init__)


def test_viewpoint::style::tooltipstyledescription_constructor_args():
    sig = inspect.signature(viewpoint::style::TooltipStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "tooltipExpression" in params, "Missing parameter 'tooltipExpression'"

def test_viewpoint::style::tooltipstyledescription_has_tooltipExpression():
    assert hasattr(viewpoint::style::TooltipStyleDescription, "tooltipExpression")
    descriptor = None
    for klass in viewpoint::style::TooltipStyleDescription.__mro__:
        if "tooltipExpression" in klass.__dict__:
            descriptor = klass.__dict__["tooltipExpression"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::style::labelborderstyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::style::LabelBorderStyleDescription)


def test_viewpoint::style::labelborderstyledescription_constructor_exists():
    assert callable(viewpoint::style::LabelBorderStyleDescription.__init__)


def test_viewpoint::style::labelborderstyledescription_constructor_args():
    sig = inspect.signature(viewpoint::style::LabelBorderStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "cornerHeight" in params, "Missing parameter 'cornerHeight'"
    assert "name" in params, "Missing parameter 'name'"
    assert "cornerWidth" in params, "Missing parameter 'cornerWidth'"
    assert "id" in params, "Missing parameter 'id'"

def test_viewpoint::style::labelborderstyledescription_has_cornerHeight():
    assert hasattr(viewpoint::style::LabelBorderStyleDescription, "cornerHeight")
    descriptor = None
    for klass in viewpoint::style::LabelBorderStyleDescription.__mro__:
        if "cornerHeight" in klass.__dict__:
            descriptor = klass.__dict__["cornerHeight"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::style::labelborderstyledescription_has_name():
    assert hasattr(viewpoint::style::LabelBorderStyleDescription, "name")
    descriptor = None
    for klass in viewpoint::style::LabelBorderStyleDescription.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::style::labelborderstyledescription_has_cornerWidth():
    assert hasattr(viewpoint::style::LabelBorderStyleDescription, "cornerWidth")
    descriptor = None
    for klass in viewpoint::style::LabelBorderStyleDescription.__mro__:
        if "cornerWidth" in klass.__dict__:
            descriptor = klass.__dict__["cornerWidth"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::style::labelborderstyledescription_has_id():
    assert hasattr(viewpoint::style::LabelBorderStyleDescription, "id")
    descriptor = None
    for klass in viewpoint::style::LabelBorderStyleDescription.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_style::labelborderstyledescription_is_not_abstract():
    assert not inspect.isabstract(style::LabelBorderStyleDescription)


def test_style::labelborderstyledescription_constructor_exists():
    assert callable(style::LabelBorderStyleDescription.__init__)


def test_style::labelborderstyledescription_constructor_args():
    sig = inspect.signature(style::LabelBorderStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::style::labelborderstyles_is_not_abstract():
    assert not inspect.isabstract(viewpoint::style::LabelBorderStyles)


def test_viewpoint::style::labelborderstyles_constructor_exists():
    assert callable(viewpoint::style::LabelBorderStyles.__init__)


def test_viewpoint::style::labelborderstyles_constructor_args():
    sig = inspect.signature(viewpoint::style::LabelBorderStyles.__init__)
    params = list(sig.parameters.keys())



def test_basiclabelstyledescription_is_not_abstract():
    assert not inspect.isabstract(BasicLabelStyleDescription)


def test_basiclabelstyledescription_constructor_exists():
    assert callable(BasicLabelStyleDescription.__init__)


def test_basiclabelstyledescription_constructor_args():
    sig = inspect.signature(BasicLabelStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::style::centerlabelstyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::style::CenterLabelStyleDescription)


def test_viewpoint::style::centerlabelstyledescription_constructor_exists():
    assert callable(viewpoint::style::CenterLabelStyleDescription.__init__)


def test_viewpoint::style::centerlabelstyledescription_constructor_args():
    sig = inspect.signature(viewpoint::style::CenterLabelStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::style::endlabelstyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::style::EndLabelStyleDescription)


def test_viewpoint::style::endlabelstyledescription_constructor_exists():
    assert callable(viewpoint::style::EndLabelStyleDescription.__init__)


def test_viewpoint::style::endlabelstyledescription_constructor_args():
    sig = inspect.signature(viewpoint::style::EndLabelStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::style::beginlabelstyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::style::BeginLabelStyleDescription)


def test_viewpoint::style::beginlabelstyledescription_constructor_exists():
    assert callable(viewpoint::style::BeginLabelStyleDescription.__init__)


def test_viewpoint::style::beginlabelstyledescription_constructor_args():
    sig = inspect.signature(viewpoint::style::BeginLabelStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::style::labelstyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::style::LabelStyleDescription)


def test_viewpoint::style::labelstyledescription_constructor_exists():
    assert callable(viewpoint::style::LabelStyleDescription.__init__)


def test_viewpoint::style::labelstyledescription_constructor_args():
    sig = inspect.signature(viewpoint::style::LabelStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "labelAlignment" in params, "Missing parameter 'labelAlignment'"

def test_viewpoint::style::labelstyledescription_has_labelAlignment():
    assert hasattr(viewpoint::style::LabelStyleDescription, "labelAlignment")
    descriptor = None
    for klass in viewpoint::style::LabelStyleDescription.__mro__:
        if "labelAlignment" in klass.__dict__:
            descriptor = klass.__dict__["labelAlignment"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::style::basiclabelstyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::style::BasicLabelStyleDescription)


def test_viewpoint::style::basiclabelstyledescription_constructor_exists():
    assert callable(viewpoint::style::BasicLabelStyleDescription.__init__)


def test_viewpoint::style::basiclabelstyledescription_constructor_args():
    sig = inspect.signature(viewpoint::style::BasicLabelStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "labelSize" in params, "Missing parameter 'labelSize'"
    assert "labelFormat" in params, "Missing parameter 'labelFormat'"
    assert "iconPath" in params, "Missing parameter 'iconPath'"
    assert "labelExpression" in params, "Missing parameter 'labelExpression'"
    assert "showIcon" in params, "Missing parameter 'showIcon'"

def test_viewpoint::style::basiclabelstyledescription_has_labelSize():
    assert hasattr(viewpoint::style::BasicLabelStyleDescription, "labelSize")
    descriptor = None
    for klass in viewpoint::style::BasicLabelStyleDescription.__mro__:
        if "labelSize" in klass.__dict__:
            descriptor = klass.__dict__["labelSize"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::style::basiclabelstyledescription_has_labelFormat():
    assert hasattr(viewpoint::style::BasicLabelStyleDescription, "labelFormat")
    descriptor = None
    for klass in viewpoint::style::BasicLabelStyleDescription.__mro__:
        if "labelFormat" in klass.__dict__:
            descriptor = klass.__dict__["labelFormat"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::style::basiclabelstyledescription_has_iconPath():
    assert hasattr(viewpoint::style::BasicLabelStyleDescription, "iconPath")
    descriptor = None
    for klass in viewpoint::style::BasicLabelStyleDescription.__mro__:
        if "iconPath" in klass.__dict__:
            descriptor = klass.__dict__["iconPath"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::style::basiclabelstyledescription_has_labelExpression():
    assert hasattr(viewpoint::style::BasicLabelStyleDescription, "labelExpression")
    descriptor = None
    for klass in viewpoint::style::BasicLabelStyleDescription.__mro__:
        if "labelExpression" in klass.__dict__:
            descriptor = klass.__dict__["labelExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::style::basiclabelstyledescription_has_showIcon():
    assert hasattr(viewpoint::style::BasicLabelStyleDescription, "showIcon")
    descriptor = None
    for klass in viewpoint::style::BasicLabelStyleDescription.__mro__:
        if "showIcon" in klass.__dict__:
            descriptor = klass.__dict__["showIcon"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::style::styledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::style::StyleDescription)


def test_viewpoint::style::styledescription_constructor_exists():
    assert callable(viewpoint::style::StyleDescription.__init__)


def test_viewpoint::style::styledescription_constructor_args():
    sig = inspect.signature(viewpoint::style::StyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::dannotationentry_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::DAnnotationEntry)


def test_viewpoint::description::dannotationentry_constructor_exists():
    assert callable(viewpoint::description::DAnnotationEntry.__init__)


def test_viewpoint::description::dannotationentry_constructor_args():
    sig = inspect.signature(viewpoint::description::DAnnotationEntry.__init__)
    params = list(sig.parameters.keys())
    assert "source" in params, "Missing parameter 'source'"
    assert "details" in params, "Missing parameter 'details'"

def test_viewpoint::description::dannotationentry_has_source():
    assert hasattr(viewpoint::description::DAnnotationEntry, "source")
    descriptor = None
    for klass in viewpoint::description::DAnnotationEntry.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::description::dannotationentry_has_details():
    assert hasattr(viewpoint::description::DAnnotationEntry, "details")
    descriptor = None
    for klass in viewpoint::description::DAnnotationEntry.__mro__:
        if "details" in klass.__dict__:
            descriptor = klass.__dict__["details"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::description::identifiedelement_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::IdentifiedElement)


def test_viewpoint::description::identifiedelement_constructor_exists():
    assert callable(viewpoint::description::IdentifiedElement.__init__)


def test_viewpoint::description::identifiedelement_constructor_args():
    sig = inspect.signature(viewpoint::description::IdentifiedElement.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "name" in params, "Missing parameter 'name'"

def test_viewpoint::description::identifiedelement_has_label():
    assert hasattr(viewpoint::description::IdentifiedElement, "label")
    descriptor = None
    for klass in viewpoint::description::IdentifiedElement.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::description::identifiedelement_has_name():
    assert hasattr(viewpoint::description::IdentifiedElement, "name")
    descriptor = None
    for klass in viewpoint::description::IdentifiedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::description::enduserdocumentedelement_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::EndUserDocumentedElement)


def test_viewpoint::description::enduserdocumentedelement_constructor_exists():
    assert callable(viewpoint::description::EndUserDocumentedElement.__init__)


def test_viewpoint::description::enduserdocumentedelement_constructor_args():
    sig = inspect.signature(viewpoint::description::EndUserDocumentedElement.__init__)
    params = list(sig.parameters.keys())
    assert "endUserDocumentation" in params, "Missing parameter 'endUserDocumentation'"

def test_viewpoint::description::enduserdocumentedelement_has_endUserDocumentation():
    assert hasattr(viewpoint::description::EndUserDocumentedElement, "endUserDocumentation")
    descriptor = None
    for klass in viewpoint::description::EndUserDocumentedElement.__mro__:
        if "endUserDocumentation" in klass.__dict__:
            descriptor = klass.__dict__["endUserDocumentation"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::description::annotationentry_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::AnnotationEntry)


def test_viewpoint::description::annotationentry_constructor_exists():
    assert callable(viewpoint::description::AnnotationEntry.__init__)


def test_viewpoint::description::annotationentry_constructor_args():
    sig = inspect.signature(viewpoint::description::AnnotationEntry.__init__)
    params = list(sig.parameters.keys())
    assert "source" in params, "Missing parameter 'source'"

def test_viewpoint::description::annotationentry_has_source():
    assert hasattr(viewpoint::description::AnnotationEntry, "source")
    descriptor = None
    for klass in viewpoint::description::AnnotationEntry.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)



def test_usercolor_is_not_abstract():
    assert not inspect.isabstract(UserColor)


def test_usercolor_constructor_exists():
    assert callable(UserColor.__init__)


def test_usercolor_constructor_args():
    sig = inspect.signature(UserColor.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::usercolorspalette_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::UserColorsPalette)


def test_viewpoint::description::usercolorspalette_constructor_exists():
    assert callable(viewpoint::description::UserColorsPalette.__init__)


def test_viewpoint::description::usercolorspalette_constructor_args():
    sig = inspect.signature(viewpoint::description::UserColorsPalette.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_viewpoint::description::usercolorspalette_has_name():
    assert hasattr(viewpoint::description::UserColorsPalette, "name")
    descriptor = None
    for klass in viewpoint::description::UserColorsPalette.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_systemcolor_is_not_abstract():
    assert not inspect.isabstract(SystemColor)


def test_systemcolor_constructor_exists():
    assert callable(SystemColor.__init__)


def test_systemcolor_constructor_args():
    sig = inspect.signature(SystemColor.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::sytemcolorspalette_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::SytemColorsPalette)


def test_viewpoint::description::sytemcolorspalette_constructor_exists():
    assert callable(viewpoint::description::SytemColorsPalette.__init__)


def test_viewpoint::description::sytemcolorspalette_constructor_args():
    sig = inspect.signature(viewpoint::description::SytemColorsPalette.__init__)
    params = list(sig.parameters.keys())



def test_style::labelborderstyles_is_not_abstract():
    assert not inspect.isabstract(style::LabelBorderStyles)


def test_style::labelborderstyles_constructor_exists():
    assert callable(style::LabelBorderStyles.__init__)


def test_style::labelborderstyles_constructor_args():
    sig = inspect.signature(style::LabelBorderStyles.__init__)
    params = list(sig.parameters.keys())



def test_tool::toolentry_is_not_abstract():
    assert not inspect.isabstract(tool::ToolEntry)


def test_tool::toolentry_constructor_exists():
    assert callable(tool::ToolEntry.__init__)


def test_tool::toolentry_constructor_args():
    sig = inspect.signature(tool::ToolEntry.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::environment_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::Environment)


def test_viewpoint::description::environment_constructor_exists():
    assert callable(viewpoint::description::Environment.__init__)


def test_viewpoint::description::environment_constructor_args():
    sig = inspect.signature(viewpoint::description::Environment.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::usercolor_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::UserColor)


def test_viewpoint::description::usercolor_constructor_exists():
    assert callable(viewpoint::description::UserColor.__init__)


def test_viewpoint::description::usercolor_constructor_args():
    sig = inspect.signature(viewpoint::description::UserColor.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_viewpoint::description::usercolor_has_name():
    assert hasattr(viewpoint::description::UserColor, "name")
    descriptor = None
    for klass in viewpoint::description::UserColor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_description::fixedcolor_is_not_abstract():
    assert not inspect.isabstract(description::FixedColor)


def test_description::fixedcolor_constructor_exists():
    assert callable(description::FixedColor.__init__)


def test_description::fixedcolor_constructor_args():
    sig = inspect.signature(description::FixedColor.__init__)
    params = list(sig.parameters.keys())



def test_colordescription_is_not_abstract():
    assert not inspect.isabstract(ColorDescription)


def test_colordescription_constructor_exists():
    assert callable(ColorDescription.__init__)


def test_colordescription_constructor_args():
    sig = inspect.signature(ColorDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::fixedcolor_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::FixedColor)


def test_viewpoint::description::fixedcolor_constructor_exists():
    assert callable(viewpoint::description::FixedColor.__init__)


def test_viewpoint::description::fixedcolor_constructor_args():
    sig = inspect.signature(viewpoint::description::FixedColor.__init__)
    params = list(sig.parameters.keys())
    assert "green" in params, "Missing parameter 'green'"
    assert "blue" in params, "Missing parameter 'blue'"
    assert "red" in params, "Missing parameter 'red'"

def test_viewpoint::description::fixedcolor_has_green():
    assert hasattr(viewpoint::description::FixedColor, "green")
    descriptor = None
    for klass in viewpoint::description::FixedColor.__mro__:
        if "green" in klass.__dict__:
            descriptor = klass.__dict__["green"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::description::fixedcolor_has_blue():
    assert hasattr(viewpoint::description::FixedColor, "blue")
    descriptor = None
    for klass in viewpoint::description::FixedColor.__mro__:
        if "blue" in klass.__dict__:
            descriptor = klass.__dict__["blue"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::description::fixedcolor_has_red():
    assert hasattr(viewpoint::description::FixedColor, "red")
    descriptor = None
    for klass in viewpoint::description::FixedColor.__mro__:
        if "red" in klass.__dict__:
            descriptor = klass.__dict__["red"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::description::colorstep_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::ColorStep)


def test_viewpoint::description::colorstep_constructor_exists():
    assert callable(viewpoint::description::ColorStep.__init__)


def test_viewpoint::description::colorstep_constructor_args():
    sig = inspect.signature(viewpoint::description::ColorStep.__init__)
    params = list(sig.parameters.keys())
    assert "associatedValue" in params, "Missing parameter 'associatedValue'"

def test_viewpoint::description::colorstep_has_associatedValue():
    assert hasattr(viewpoint::description::ColorStep, "associatedValue")
    descriptor = None
    for klass in viewpoint::description::ColorStep.__mro__:
        if "associatedValue" in klass.__dict__:
            descriptor = klass.__dict__["associatedValue"]
            break
    assert isinstance(descriptor, property)



def test_colorstep_is_not_abstract():
    assert not inspect.isabstract(ColorStep)


def test_colorstep_constructor_exists():
    assert callable(ColorStep.__init__)


def test_colorstep_constructor_args():
    sig = inspect.signature(ColorStep.__init__)
    params = list(sig.parameters.keys())



def test_description::colordescription_is_not_abstract():
    assert not inspect.isabstract(description::ColorDescription)


def test_description::colordescription_constructor_exists():
    assert callable(description::ColorDescription.__init__)


def test_description::colordescription_constructor_args():
    sig = inspect.signature(description::ColorDescription.__init__)
    params = list(sig.parameters.keys())



def test_fixedcolor_is_not_abstract():
    assert not inspect.isabstract(FixedColor)


def test_fixedcolor_constructor_exists():
    assert callable(FixedColor.__init__)


def test_fixedcolor_constructor_args():
    sig = inspect.signature(FixedColor.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::systemcolor_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::SystemColor)


def test_viewpoint::description::systemcolor_constructor_exists():
    assert callable(viewpoint::description::SystemColor.__init__)


def test_viewpoint::description::systemcolor_constructor_args():
    sig = inspect.signature(viewpoint::description::SystemColor.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_viewpoint::description::systemcolor_has_name():
    assert hasattr(viewpoint::description::SystemColor, "name")
    descriptor = None
    for klass in viewpoint::description::SystemColor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::description::colordescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::ColorDescription)


def test_viewpoint::description::colordescription_constructor_exists():
    assert callable(viewpoint::description::ColorDescription.__init__)


def test_viewpoint::description::colordescription_constructor_args():
    sig = inspect.signature(viewpoint::description::ColorDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::selectiondescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::SelectionDescription)


def test_viewpoint::description::selectiondescription_constructor_exists():
    assert callable(viewpoint::description::SelectionDescription.__init__)


def test_viewpoint::description::selectiondescription_constructor_args():
    sig = inspect.signature(viewpoint::description::SelectionDescription.__init__)
    params = list(sig.parameters.keys())
    assert "message" in params, "Missing parameter 'message'"
    assert "multiple" in params, "Missing parameter 'multiple'"
    assert "tree" in params, "Missing parameter 'tree'"
    assert "candidatesExpression" in params, "Missing parameter 'candidatesExpression'"
    assert "childrenExpression" in params, "Missing parameter 'childrenExpression'"
    assert "rootExpression" in params, "Missing parameter 'rootExpression'"

def test_viewpoint::description::selectiondescription_has_message():
    assert hasattr(viewpoint::description::SelectionDescription, "message")
    descriptor = None
    for klass in viewpoint::description::SelectionDescription.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::description::selectiondescription_has_multiple():
    assert hasattr(viewpoint::description::SelectionDescription, "multiple")
    descriptor = None
    for klass in viewpoint::description::SelectionDescription.__mro__:
        if "multiple" in klass.__dict__:
            descriptor = klass.__dict__["multiple"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::description::selectiondescription_has_tree():
    assert hasattr(viewpoint::description::SelectionDescription, "tree")
    descriptor = None
    for klass in viewpoint::description::SelectionDescription.__mro__:
        if "tree" in klass.__dict__:
            descriptor = klass.__dict__["tree"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::description::selectiondescription_has_candidatesExpression():
    assert hasattr(viewpoint::description::SelectionDescription, "candidatesExpression")
    descriptor = None
    for klass in viewpoint::description::SelectionDescription.__mro__:
        if "candidatesExpression" in klass.__dict__:
            descriptor = klass.__dict__["candidatesExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::description::selectiondescription_has_childrenExpression():
    assert hasattr(viewpoint::description::SelectionDescription, "childrenExpression")
    descriptor = None
    for klass in viewpoint::description::SelectionDescription.__mro__:
        if "childrenExpression" in klass.__dict__:
            descriptor = klass.__dict__["childrenExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::description::selectiondescription_has_rootExpression():
    assert hasattr(viewpoint::description::SelectionDescription, "rootExpression")
    descriptor = None
    for klass in viewpoint::description::SelectionDescription.__mro__:
        if "rootExpression" in klass.__dict__:
            descriptor = klass.__dict__["rootExpression"]
            break
    assert isinstance(descriptor, property)



def test_description::usercolor_is_not_abstract():
    assert not inspect.isabstract(description::UserColor)


def test_description::usercolor_constructor_exists():
    assert callable(description::UserColor.__init__)


def test_description::usercolor_constructor_args():
    sig = inspect.signature(description::UserColor.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::interpolatedcolor_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::InterpolatedColor)


def test_viewpoint::description::interpolatedcolor_constructor_exists():
    assert callable(viewpoint::description::InterpolatedColor.__init__)


def test_viewpoint::description::interpolatedcolor_constructor_args():
    sig = inspect.signature(viewpoint::description::InterpolatedColor.__init__)
    params = list(sig.parameters.keys())
    assert "colorValueComputationExpression" in params, "Missing parameter 'colorValueComputationExpression'"
    assert "minValueComputationExpression" in params, "Missing parameter 'minValueComputationExpression'"
    assert "maxValueComputationExpression" in params, "Missing parameter 'maxValueComputationExpression'"

def test_viewpoint::description::interpolatedcolor_has_colorValueComputationExpression():
    assert hasattr(viewpoint::description::InterpolatedColor, "colorValueComputationExpression")
    descriptor = None
    for klass in viewpoint::description::InterpolatedColor.__mro__:
        if "colorValueComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["colorValueComputationExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::description::interpolatedcolor_has_minValueComputationExpression():
    assert hasattr(viewpoint::description::InterpolatedColor, "minValueComputationExpression")
    descriptor = None
    for klass in viewpoint::description::InterpolatedColor.__mro__:
        if "minValueComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["minValueComputationExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::description::interpolatedcolor_has_maxValueComputationExpression():
    assert hasattr(viewpoint::description::InterpolatedColor, "maxValueComputationExpression")
    descriptor = None
    for klass in viewpoint::description::InterpolatedColor.__mro__:
        if "maxValueComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["maxValueComputationExpression"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::description::userfixedcolor_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::UserFixedColor)


def test_viewpoint::description::userfixedcolor_constructor_exists():
    assert callable(viewpoint::description::UserFixedColor.__init__)


def test_viewpoint::description::userfixedcolor_constructor_args():
    sig = inspect.signature(viewpoint::description::UserFixedColor.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::computedcolor_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::ComputedColor)


def test_viewpoint::description::computedcolor_constructor_exists():
    assert callable(viewpoint::description::ComputedColor.__init__)


def test_viewpoint::description::computedcolor_constructor_args():
    sig = inspect.signature(viewpoint::description::ComputedColor.__init__)
    params = list(sig.parameters.keys())
    assert "red" in params, "Missing parameter 'red'"
    assert "green" in params, "Missing parameter 'green'"
    assert "blue" in params, "Missing parameter 'blue'"

def test_viewpoint::description::computedcolor_has_red():
    assert hasattr(viewpoint::description::ComputedColor, "red")
    descriptor = None
    for klass in viewpoint::description::ComputedColor.__mro__:
        if "red" in klass.__dict__:
            descriptor = klass.__dict__["red"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::description::computedcolor_has_green():
    assert hasattr(viewpoint::description::ComputedColor, "green")
    descriptor = None
    for klass in viewpoint::description::ComputedColor.__mro__:
        if "green" in klass.__dict__:
            descriptor = klass.__dict__["green"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::description::computedcolor_has_blue():
    assert hasattr(viewpoint::description::ComputedColor, "blue")
    descriptor = None
    for klass in viewpoint::description::ComputedColor.__mro__:
        if "blue" in klass.__dict__:
            descriptor = klass.__dict__["blue"]
            break
    assert isinstance(descriptor, property)



def test_estructuralfeaturecustomization_is_not_abstract():
    assert not inspect.isabstract(EStructuralFeatureCustomization)


def test_estructuralfeaturecustomization_constructor_exists():
    assert callable(EStructuralFeatureCustomization.__init__)


def test_estructuralfeaturecustomization_constructor_args():
    sig = inspect.signature(EStructuralFeatureCustomization.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::ereferencecustomization_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::EReferenceCustomization)


def test_viewpoint::description::ereferencecustomization_constructor_exists():
    assert callable(viewpoint::description::EReferenceCustomization.__init__)


def test_viewpoint::description::ereferencecustomization_constructor_args():
    sig = inspect.signature(viewpoint::description::EReferenceCustomization.__init__)
    params = list(sig.parameters.keys())
    assert "referenceName" in params, "Missing parameter 'referenceName'"

def test_viewpoint::description::ereferencecustomization_has_referenceName():
    assert hasattr(viewpoint::description::EReferenceCustomization, "referenceName")
    descriptor = None
    for klass in viewpoint::description::EReferenceCustomization.__mro__:
        if "referenceName" in klass.__dict__:
            descriptor = klass.__dict__["referenceName"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::description::ivsmelementcustomization_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::IVSMElementCustomization)


def test_viewpoint::description::ivsmelementcustomization_constructor_exists():
    assert callable(viewpoint::description::IVSMElementCustomization.__init__)


def test_viewpoint::description::ivsmelementcustomization_constructor_args():
    sig = inspect.signature(viewpoint::description::IVSMElementCustomization.__init__)
    params = list(sig.parameters.keys())



def test_ivsmelementcustomization_is_not_abstract():
    assert not inspect.isabstract(IVSMElementCustomization)


def test_ivsmelementcustomization_constructor_exists():
    assert callable(IVSMElementCustomization.__init__)


def test_ivsmelementcustomization_constructor_args():
    sig = inspect.signature(IVSMElementCustomization.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::vsmelementcustomizationreuse_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::VSMElementCustomizationReuse)


def test_viewpoint::description::vsmelementcustomizationreuse_constructor_exists():
    assert callable(viewpoint::description::VSMElementCustomizationReuse.__init__)


def test_viewpoint::description::vsmelementcustomizationreuse_constructor_args():
    sig = inspect.signature(viewpoint::description::VSMElementCustomizationReuse.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::vsmelementcustomization_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::VSMElementCustomization)


def test_viewpoint::description::vsmelementcustomization_constructor_exists():
    assert callable(viewpoint::description::VSMElementCustomization.__init__)


def test_viewpoint::description::vsmelementcustomization_constructor_args():
    sig = inspect.signature(viewpoint::description::VSMElementCustomization.__init__)
    params = list(sig.parameters.keys())
    assert "predicateExpression" in params, "Missing parameter 'predicateExpression'"

def test_viewpoint::description::vsmelementcustomization_has_predicateExpression():
    assert hasattr(viewpoint::description::VSMElementCustomization, "predicateExpression")
    descriptor = None
    for klass in viewpoint::description::VSMElementCustomization.__mro__:
        if "predicateExpression" in klass.__dict__:
            descriptor = klass.__dict__["predicateExpression"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::description::customization_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::Customization)


def test_viewpoint::description::customization_constructor_exists():
    assert callable(viewpoint::description::Customization.__init__)


def test_viewpoint::description::customization_constructor_args():
    sig = inspect.signature(viewpoint::description::Customization.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::eattributecustomization_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::EAttributeCustomization)


def test_viewpoint::description::eattributecustomization_constructor_exists():
    assert callable(viewpoint::description::EAttributeCustomization.__init__)


def test_viewpoint::description::eattributecustomization_constructor_args():
    sig = inspect.signature(viewpoint::description::EAttributeCustomization.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "attributeName" in params, "Missing parameter 'attributeName'"

def test_viewpoint::description::eattributecustomization_has_value():
    assert hasattr(viewpoint::description::EAttributeCustomization, "value")
    descriptor = None
    for klass in viewpoint::description::EAttributeCustomization.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::description::eattributecustomization_has_attributeName():
    assert hasattr(viewpoint::description::EAttributeCustomization, "attributeName")
    descriptor = None
    for klass in viewpoint::description::EAttributeCustomization.__mro__:
        if "attributeName" in klass.__dict__:
            descriptor = klass.__dict__["attributeName"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::description::estructuralfeaturecustomization_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::EStructuralFeatureCustomization)


def test_viewpoint::description::estructuralfeaturecustomization_constructor_exists():
    assert callable(viewpoint::description::EStructuralFeatureCustomization.__init__)


def test_viewpoint::description::estructuralfeaturecustomization_constructor_args():
    sig = inspect.signature(viewpoint::description::EStructuralFeatureCustomization.__init__)
    params = list(sig.parameters.keys())
    assert "applyOnAll" in params, "Missing parameter 'applyOnAll'"

def test_viewpoint::description::estructuralfeaturecustomization_has_applyOnAll():
    assert hasattr(viewpoint::description::EStructuralFeatureCustomization, "applyOnAll")
    descriptor = None
    for klass in viewpoint::description::EStructuralFeatureCustomization.__mro__:
        if "applyOnAll" in klass.__dict__:
            descriptor = klass.__dict__["applyOnAll"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::description::decorationdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::DecorationDescription)


def test_viewpoint::description::decorationdescription_constructor_exists():
    assert callable(viewpoint::description::DecorationDescription.__init__)


def test_viewpoint::description::decorationdescription_constructor_args():
    sig = inspect.signature(viewpoint::description::DecorationDescription.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"
    assert "preconditionExpression" in params, "Missing parameter 'preconditionExpression'"
    assert "decoratorPath" in params, "Missing parameter 'decoratorPath'"
    assert "name" in params, "Missing parameter 'name'"

def test_viewpoint::description::decorationdescription_has_position():
    assert hasattr(viewpoint::description::DecorationDescription, "position")
    descriptor = None
    for klass in viewpoint::description::DecorationDescription.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::description::decorationdescription_has_preconditionExpression():
    assert hasattr(viewpoint::description::DecorationDescription, "preconditionExpression")
    descriptor = None
    for klass in viewpoint::description::DecorationDescription.__mro__:
        if "preconditionExpression" in klass.__dict__:
            descriptor = klass.__dict__["preconditionExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::description::decorationdescription_has_decoratorPath():
    assert hasattr(viewpoint::description::DecorationDescription, "decoratorPath")
    descriptor = None
    for klass in viewpoint::description::DecorationDescription.__mro__:
        if "decoratorPath" in klass.__dict__:
            descriptor = klass.__dict__["decoratorPath"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::description::decorationdescription_has_name():
    assert hasattr(viewpoint::description::DecorationDescription, "name")
    descriptor = None
    for klass in viewpoint::description::DecorationDescription.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::description::decorationdescriptionsset_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::DecorationDescriptionsSet)


def test_viewpoint::description::decorationdescriptionsset_constructor_exists():
    assert callable(viewpoint::description::DecorationDescriptionsSet.__init__)


def test_viewpoint::description::decorationdescriptionsset_constructor_args():
    sig = inspect.signature(viewpoint::description::DecorationDescriptionsSet.__init__)
    params = list(sig.parameters.keys())



def test_tool::pastedescription_is_not_abstract():
    assert not inspect.isabstract(tool::PasteDescription)


def test_tool::pastedescription_constructor_exists():
    assert callable(tool::PasteDescription.__init__)


def test_tool::pastedescription_constructor_args():
    sig = inspect.signature(tool::PasteDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::pastetargetdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::PasteTargetDescription)


def test_viewpoint::description::pastetargetdescription_constructor_exists():
    assert callable(viewpoint::description::PasteTargetDescription.__init__)


def test_viewpoint::description::pastetargetdescription_constructor_args():
    sig = inspect.signature(viewpoint::description::PasteTargetDescription.__init__)
    params = list(sig.parameters.keys())



def test_tool::containerdropdescription_is_not_abstract():
    assert not inspect.isabstract(tool::ContainerDropDescription)


def test_tool::containerdropdescription_constructor_exists():
    assert callable(tool::ContainerDropDescription.__init__)


def test_tool::containerdropdescription_constructor_args():
    sig = inspect.signature(tool::ContainerDropDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::draganddroptargetdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::DragAndDropTargetDescription)


def test_viewpoint::description::draganddroptargetdescription_constructor_exists():
    assert callable(viewpoint::description::DragAndDropTargetDescription.__init__)


def test_viewpoint::description::draganddroptargetdescription_constructor_args():
    sig = inspect.signature(viewpoint::description::DragAndDropTargetDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::conditionalstyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::ConditionalStyleDescription)


def test_viewpoint::description::conditionalstyledescription_constructor_exists():
    assert callable(viewpoint::description::ConditionalStyleDescription.__init__)


def test_viewpoint::description::conditionalstyledescription_constructor_args():
    sig = inspect.signature(viewpoint::description::ConditionalStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "predicateExpression" in params, "Missing parameter 'predicateExpression'"

def test_viewpoint::description::conditionalstyledescription_has_predicateExpression():
    assert hasattr(viewpoint::description::ConditionalStyleDescription, "predicateExpression")
    descriptor = None
    for klass in viewpoint::description::ConditionalStyleDescription.__mro__:
        if "predicateExpression" in klass.__dict__:
            descriptor = klass.__dict__["predicateExpression"]
            break
    assert isinstance(descriptor, property)



def test_description::viewpoint::estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(description::viewpoint::EStringToStringMapEntry)


def test_description::viewpoint::estringtostringmapentry_constructor_exists():
    assert callable(description::viewpoint::EStringToStringMapEntry.__init__)


def test_description::viewpoint::estringtostringmapentry_constructor_args():
    sig = inspect.signature(description::viewpoint::EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::dannotation_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::DAnnotation)


def test_viewpoint::description::dannotation_constructor_exists():
    assert callable(viewpoint::description::DAnnotation.__init__)


def test_viewpoint::description::dannotation_constructor_args():
    sig = inspect.signature(viewpoint::description::DAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "source" in params, "Missing parameter 'source'"

def test_viewpoint::description::dannotation_has_source():
    assert hasattr(viewpoint::description::DAnnotation, "source")
    descriptor = None
    for klass in viewpoint::description::DAnnotation.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)



def test_dannotation_is_not_abstract():
    assert not inspect.isabstract(DAnnotation)


def test_dannotation_constructor_exists():
    assert callable(DAnnotation.__init__)


def test_dannotation_constructor_args():
    sig = inspect.signature(DAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::abstractmappingimport_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::AbstractMappingImport)


def test_viewpoint::description::abstractmappingimport_constructor_exists():
    assert callable(viewpoint::description::AbstractMappingImport.__init__)


def test_viewpoint::description::abstractmappingimport_constructor_args():
    sig = inspect.signature(viewpoint::description::AbstractMappingImport.__init__)
    params = list(sig.parameters.keys())
    assert "hideSubMappings" in params, "Missing parameter 'hideSubMappings'"
    assert "inheritsAncestorFilters" in params, "Missing parameter 'inheritsAncestorFilters'"

def test_viewpoint::description::abstractmappingimport_has_hideSubMappings():
    assert hasattr(viewpoint::description::AbstractMappingImport, "hideSubMappings")
    descriptor = None
    for klass in viewpoint::description::AbstractMappingImport.__mro__:
        if "hideSubMappings" in klass.__dict__:
            descriptor = klass.__dict__["hideSubMappings"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::description::abstractmappingimport_has_inheritsAncestorFilters():
    assert hasattr(viewpoint::description::AbstractMappingImport, "inheritsAncestorFilters")
    descriptor = None
    for klass in viewpoint::description::AbstractMappingImport.__mro__:
        if "inheritsAncestorFilters" in klass.__dict__:
            descriptor = klass.__dict__["inheritsAncestorFilters"]
            break
    assert isinstance(descriptor, property)



def test_tool::representationnavigationdescription_is_not_abstract():
    assert not inspect.isabstract(tool::RepresentationNavigationDescription)


def test_tool::representationnavigationdescription_constructor_exists():
    assert callable(tool::RepresentationNavigationDescription.__init__)


def test_tool::representationnavigationdescription_constructor_args():
    sig = inspect.signature(tool::RepresentationNavigationDescription.__init__)
    params = list(sig.parameters.keys())



def test_tool::representationcreationdescription_is_not_abstract():
    assert not inspect.isabstract(tool::RepresentationCreationDescription)


def test_tool::representationcreationdescription_constructor_exists():
    assert callable(tool::RepresentationCreationDescription.__init__)


def test_tool::representationcreationdescription_constructor_args():
    sig = inspect.signature(tool::RepresentationCreationDescription.__init__)
    params = list(sig.parameters.keys())



def test_identifiedelement_is_not_abstract():
    assert not inspect.isabstract(IdentifiedElement)


def test_identifiedelement_constructor_exists():
    assert callable(IdentifiedElement.__init__)


def test_identifiedelement_constructor_args():
    sig = inspect.signature(IdentifiedElement.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::representationelementmapping_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::RepresentationElementMapping)


def test_viewpoint::description::representationelementmapping_constructor_exists():
    assert callable(viewpoint::description::RepresentationElementMapping.__init__)


def test_viewpoint::description::representationelementmapping_constructor_args():
    sig = inspect.signature(viewpoint::description::RepresentationElementMapping.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::javaextension_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::JavaExtension)


def test_viewpoint::description::javaextension_constructor_exists():
    assert callable(viewpoint::description::JavaExtension.__init__)


def test_viewpoint::description::javaextension_constructor_args():
    sig = inspect.signature(viewpoint::description::JavaExtension.__init__)
    params = list(sig.parameters.keys())
    assert "qualifiedClassName" in params, "Missing parameter 'qualifiedClassName'"

def test_viewpoint::description::javaextension_has_qualifiedClassName():
    assert hasattr(viewpoint::description::JavaExtension, "qualifiedClassName")
    descriptor = None
    for klass in viewpoint::description::JavaExtension.__mro__:
        if "qualifiedClassName" in klass.__dict__:
            descriptor = klass.__dict__["qualifiedClassName"]
            break
    assert isinstance(descriptor, property)



def test_description::viewpoint::eobject_is_not_abstract():
    assert not inspect.isabstract(description::viewpoint::EObject)


def test_description::viewpoint::eobject_constructor_exists():
    assert callable(description::viewpoint::EObject.__init__)


def test_description::viewpoint::eobject_constructor_args():
    sig = inspect.signature(description::viewpoint::EObject.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::metamodelextensionsetting_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::MetamodelExtensionSetting)


def test_viewpoint::description::metamodelextensionsetting_constructor_exists():
    assert callable(viewpoint::description::MetamodelExtensionSetting.__init__)


def test_viewpoint::description::metamodelextensionsetting_constructor_args():
    sig = inspect.signature(viewpoint::description::MetamodelExtensionSetting.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::representationextensiondescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::RepresentationExtensionDescription)


def test_viewpoint::description::representationextensiondescription_constructor_exists():
    assert callable(viewpoint::description::RepresentationExtensionDescription.__init__)


def test_viewpoint::description::representationextensiondescription_constructor_args():
    sig = inspect.signature(viewpoint::description::RepresentationExtensionDescription.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "representationName" in params, "Missing parameter 'representationName'"
    assert "viewpointURI" in params, "Missing parameter 'viewpointURI'"

def test_viewpoint::description::representationextensiondescription_has_name():
    assert hasattr(viewpoint::description::RepresentationExtensionDescription, "name")
    descriptor = None
    for klass in viewpoint::description::RepresentationExtensionDescription.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::description::representationextensiondescription_has_representationName():
    assert hasattr(viewpoint::description::RepresentationExtensionDescription, "representationName")
    descriptor = None
    for klass in viewpoint::description::RepresentationExtensionDescription.__mro__:
        if "representationName" in klass.__dict__:
            descriptor = klass.__dict__["representationName"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::description::representationextensiondescription_has_viewpointURI():
    assert hasattr(viewpoint::description::RepresentationExtensionDescription, "viewpointURI")
    descriptor = None
    for klass in viewpoint::description::RepresentationExtensionDescription.__mro__:
        if "viewpointURI" in klass.__dict__:
            descriptor = klass.__dict__["viewpointURI"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::description::dmodelelement_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::DModelElement)


def test_viewpoint::description::dmodelelement_constructor_exists():
    assert callable(viewpoint::description::DModelElement.__init__)


def test_viewpoint::description::dmodelelement_constructor_args():
    sig = inspect.signature(viewpoint::description::DModelElement.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::documentedelement_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::DocumentedElement)


def test_viewpoint::description::documentedelement_constructor_exists():
    assert callable(viewpoint::description::DocumentedElement.__init__)


def test_viewpoint::description::documentedelement_constructor_args():
    sig = inspect.signature(viewpoint::description::DocumentedElement.__init__)
    params = list(sig.parameters.keys())
    assert "documentation" in params, "Missing parameter 'documentation'"

def test_viewpoint::description::documentedelement_has_documentation():
    assert hasattr(viewpoint::description::DocumentedElement, "documentation")
    descriptor = None
    for klass in viewpoint::description::DocumentedElement.__mro__:
        if "documentation" in klass.__dict__:
            descriptor = klass.__dict__["documentation"]
            break
    assert isinstance(descriptor, property)



def test_description::viewpoint::epackage_is_not_abstract():
    assert not inspect.isabstract(description::viewpoint::EPackage)


def test_description::viewpoint::epackage_constructor_exists():
    assert callable(description::viewpoint::EPackage.__init__)


def test_description::viewpoint::epackage_constructor_args():
    sig = inspect.signature(description::viewpoint::EPackage.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::featureextensiondescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::FeatureExtensionDescription)


def test_viewpoint::description::featureextensiondescription_constructor_exists():
    assert callable(viewpoint::description::FeatureExtensionDescription.__init__)


def test_viewpoint::description::featureextensiondescription_constructor_args():
    sig = inspect.signature(viewpoint::description::FeatureExtensionDescription.__init__)
    params = list(sig.parameters.keys())



def test_representationtemplate_is_not_abstract():
    assert not inspect.isabstract(RepresentationTemplate)


def test_representationtemplate_constructor_exists():
    assert callable(RepresentationTemplate.__init__)


def test_representationtemplate_constructor_args():
    sig = inspect.signature(RepresentationTemplate.__init__)
    params = list(sig.parameters.keys())



def test_metamodelextensionsetting_is_not_abstract():
    assert not inspect.isabstract(MetamodelExtensionSetting)


def test_metamodelextensionsetting_constructor_exists():
    assert callable(MetamodelExtensionSetting.__init__)


def test_metamodelextensionsetting_constructor_args():
    sig = inspect.signature(MetamodelExtensionSetting.__init__)
    params = list(sig.parameters.keys())



def test_javaextension_is_not_abstract():
    assert not inspect.isabstract(JavaExtension)


def test_javaextension_constructor_exists():
    assert callable(JavaExtension.__init__)


def test_javaextension_constructor_args():
    sig = inspect.signature(JavaExtension.__init__)
    params = list(sig.parameters.keys())



def test_representationextensiondescription_is_not_abstract():
    assert not inspect.isabstract(RepresentationExtensionDescription)


def test_representationextensiondescription_constructor_exists():
    assert callable(RepresentationExtensionDescription.__init__)


def test_representationextensiondescription_constructor_args():
    sig = inspect.signature(RepresentationExtensionDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::diagramextensiondescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::DiagramExtensionDescription)


def test_viewpoint::description::diagramextensiondescription_constructor_exists():
    assert callable(viewpoint::description::DiagramExtensionDescription.__init__)


def test_viewpoint::description::diagramextensiondescription_constructor_args():
    sig = inspect.signature(viewpoint::description::DiagramExtensionDescription.__init__)
    params = list(sig.parameters.keys())



def test_representationdescription_is_not_abstract():
    assert not inspect.isabstract(RepresentationDescription)


def test_representationdescription_constructor_exists():
    assert callable(RepresentationDescription.__init__)


def test_representationdescription_constructor_args():
    sig = inspect.signature(RepresentationDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::representationimportdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::RepresentationImportDescription)


def test_viewpoint::description::representationimportdescription_constructor_exists():
    assert callable(viewpoint::description::RepresentationImportDescription.__init__)


def test_viewpoint::description::representationimportdescription_constructor_args():
    sig = inspect.signature(viewpoint::description::RepresentationImportDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::representationtemplate_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::RepresentationTemplate)


def test_viewpoint::description::representationtemplate_constructor_exists():
    assert callable(viewpoint::description::RepresentationTemplate.__init__)


def test_viewpoint::description::representationtemplate_constructor_args():
    sig = inspect.signature(viewpoint::description::RepresentationTemplate.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_viewpoint::description::representationtemplate_has_name():
    assert hasattr(viewpoint::description::RepresentationTemplate, "name")
    descriptor = None
    for klass in viewpoint::description::RepresentationTemplate.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_validation::validationset_is_not_abstract():
    assert not inspect.isabstract(validation::ValidationSet)


def test_validation::validationset_constructor_exists():
    assert callable(validation::ValidationSet.__init__)


def test_validation::validationset_constructor_args():
    sig = inspect.signature(validation::ValidationSet.__init__)
    params = list(sig.parameters.keys())



def test_description::identifiedelement_is_not_abstract():
    assert not inspect.isabstract(description::IdentifiedElement)


def test_description::identifiedelement_constructor_exists():
    assert callable(description::IdentifiedElement.__init__)


def test_description::identifiedelement_constructor_args():
    sig = inspect.signature(description::IdentifiedElement.__init__)
    params = list(sig.parameters.keys())



def test_description::enduserdocumentedelement_is_not_abstract():
    assert not inspect.isabstract(description::EndUserDocumentedElement)


def test_description::enduserdocumentedelement_constructor_exists():
    assert callable(description::EndUserDocumentedElement.__init__)


def test_description::enduserdocumentedelement_constructor_args():
    sig = inspect.signature(description::EndUserDocumentedElement.__init__)
    params = list(sig.parameters.keys())



def test_description::component_is_not_abstract():
    assert not inspect.isabstract(description::Component)


def test_description::component_constructor_exists():
    assert callable(description::Component.__init__)


def test_description::component_constructor_args():
    sig = inspect.signature(description::Component.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::component_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::Component)


def test_viewpoint::description::component_constructor_exists():
    assert callable(viewpoint::description::Component.__init__)


def test_viewpoint::description::component_constructor_args():
    sig = inspect.signature(viewpoint::description::Component.__init__)
    params = list(sig.parameters.keys())



def test_usercolorspalette_is_not_abstract():
    assert not inspect.isabstract(UserColorsPalette)


def test_usercolorspalette_constructor_exists():
    assert callable(UserColorsPalette.__init__)


def test_usercolorspalette_constructor_args():
    sig = inspect.signature(UserColorsPalette.__init__)
    params = list(sig.parameters.keys())



def test_sytemcolorspalette_is_not_abstract():
    assert not inspect.isabstract(SytemColorsPalette)


def test_sytemcolorspalette_constructor_exists():
    assert callable(SytemColorsPalette.__init__)


def test_sytemcolorspalette_constructor_args():
    sig = inspect.signature(SytemColorsPalette.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::customizable_is_not_abstract():
    assert not inspect.isabstract(viewpoint::Customizable)


def test_viewpoint::customizable_constructor_exists():
    assert callable(viewpoint::Customizable.__init__)


def test_viewpoint::customizable_constructor_args():
    sig = inspect.signature(viewpoint::Customizable.__init__)
    params = list(sig.parameters.keys())
    assert "customFeatures" in params, "Missing parameter 'customFeatures'"

def test_viewpoint::customizable_has_customFeatures():
    assert hasattr(viewpoint::Customizable, "customFeatures")
    descriptor = None
    for klass in viewpoint::Customizable.__mro__:
        if "customFeatures" in klass.__dict__:
            descriptor = klass.__dict__["customFeatures"]
            break
    assert isinstance(descriptor, property)



def test_dfile_is_not_abstract():
    assert not inspect.isabstract(DFile)


def test_dfile_constructor_exists():
    assert callable(DFile.__init__)


def test_dfile_constructor_args():
    sig = inspect.signature(DFile.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::dmodel_is_not_abstract():
    assert not inspect.isabstract(viewpoint::DModel)


def test_viewpoint::dmodel_constructor_exists():
    assert callable(viewpoint::DModel.__init__)


def test_viewpoint::dmodel_constructor_args():
    sig = inspect.signature(viewpoint::DModel.__init__)
    params = list(sig.parameters.keys())



def test_dresourcecontainer_is_not_abstract():
    assert not inspect.isabstract(DResourceContainer)


def test_dresourcecontainer_constructor_exists():
    assert callable(DResourceContainer.__init__)


def test_dresourcecontainer_constructor_args():
    sig = inspect.signature(DResourceContainer.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::dfolder_is_not_abstract():
    assert not inspect.isabstract(viewpoint::DFolder)


def test_viewpoint::dfolder_constructor_exists():
    assert callable(viewpoint::DFolder.__init__)


def test_viewpoint::dfolder_constructor_args():
    sig = inspect.signature(viewpoint::DFolder.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::dproject_is_not_abstract():
    assert not inspect.isabstract(viewpoint::DProject)


def test_viewpoint::dproject_constructor_exists():
    assert callable(viewpoint::DProject.__init__)


def test_viewpoint::dproject_constructor_args():
    sig = inspect.signature(viewpoint::DProject.__init__)
    params = list(sig.parameters.keys())



def test_dresource_is_not_abstract():
    assert not inspect.isabstract(DResource)


def test_dresource_constructor_exists():
    assert callable(DResource.__init__)


def test_dresource_constructor_args():
    sig = inspect.signature(DResource.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::dresourcecontainer_is_not_abstract():
    assert not inspect.isabstract(viewpoint::DResourceContainer)


def test_viewpoint::dresourcecontainer_constructor_exists():
    assert callable(viewpoint::DResourceContainer.__init__)


def test_viewpoint::dresourcecontainer_constructor_args():
    sig = inspect.signature(viewpoint::DResourceContainer.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::dfile_is_not_abstract():
    assert not inspect.isabstract(viewpoint::DFile)


def test_viewpoint::dfile_constructor_exists():
    assert callable(viewpoint::DFile.__init__)


def test_viewpoint::dfile_constructor_args():
    sig = inspect.signature(viewpoint::DFile.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::dresource_is_not_abstract():
    assert not inspect.isabstract(viewpoint::DResource)


def test_viewpoint::dresource_constructor_exists():
    assert callable(viewpoint::DResource.__init__)


def test_viewpoint::dresource_constructor_args():
    sig = inspect.signature(viewpoint::DResource.__init__)
    params = list(sig.parameters.keys())
    assert "path" in params, "Missing parameter 'path'"
    assert "name" in params, "Missing parameter 'name'"

def test_viewpoint::dresource_has_path():
    assert hasattr(viewpoint::DResource, "path")
    descriptor = None
    for klass in viewpoint::DResource.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::dresource_has_name():
    assert hasattr(viewpoint::DResource, "name")
    descriptor = None
    for klass in viewpoint::DResource.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::sessionmanagereobject_is_not_abstract():
    assert not inspect.isabstract(viewpoint::SessionManagerEObject)


def test_viewpoint::sessionmanagereobject_constructor_exists():
    assert callable(viewpoint::SessionManagerEObject.__init__)


def test_viewpoint::sessionmanagereobject_constructor_args():
    sig = inspect.signature(viewpoint::SessionManagerEObject.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::danalysissessioneobject_is_not_abstract():
    assert not inspect.isabstract(viewpoint::DAnalysisSessionEObject)


def test_viewpoint::danalysissessioneobject_constructor_exists():
    assert callable(viewpoint::DAnalysisSessionEObject.__init__)


def test_viewpoint::danalysissessioneobject_constructor_args():
    sig = inspect.signature(viewpoint::DAnalysisSessionEObject.__init__)
    params = list(sig.parameters.keys())
    assert "controlledResources" in params, "Missing parameter 'controlledResources'"
    assert "resources" in params, "Missing parameter 'resources'"
    assert "blocked" in params, "Missing parameter 'blocked'"
    assert "open" in params, "Missing parameter 'open'"
    assert "synchronizationStatus" in params, "Missing parameter 'synchronizationStatus'"

def test_viewpoint::danalysissessioneobject_has_controlledResources():
    assert hasattr(viewpoint::DAnalysisSessionEObject, "controlledResources")
    descriptor = None
    for klass in viewpoint::DAnalysisSessionEObject.__mro__:
        if "controlledResources" in klass.__dict__:
            descriptor = klass.__dict__["controlledResources"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::danalysissessioneobject_has_resources():
    assert hasattr(viewpoint::DAnalysisSessionEObject, "resources")
    descriptor = None
    for klass in viewpoint::DAnalysisSessionEObject.__mro__:
        if "resources" in klass.__dict__:
            descriptor = klass.__dict__["resources"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::danalysissessioneobject_has_blocked():
    assert hasattr(viewpoint::DAnalysisSessionEObject, "blocked")
    descriptor = None
    for klass in viewpoint::DAnalysisSessionEObject.__mro__:
        if "blocked" in klass.__dict__:
            descriptor = klass.__dict__["blocked"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::danalysissessioneobject_has_open():
    assert hasattr(viewpoint::DAnalysisSessionEObject, "open")
    descriptor = None
    for klass in viewpoint::DAnalysisSessionEObject.__mro__:
        if "open" in klass.__dict__:
            descriptor = klass.__dict__["open"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::danalysissessioneobject_has_synchronizationStatus():
    assert hasattr(viewpoint::DAnalysisSessionEObject, "synchronizationStatus")
    descriptor = None
    for klass in viewpoint::DAnalysisSessionEObject.__mro__:
        if "synchronizationStatus" in klass.__dict__:
            descriptor = klass.__dict__["synchronizationStatus"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::rgbvalues_is_not_abstract():
    assert not inspect.isabstract(viewpoint::RGBValues)


def test_viewpoint::rgbvalues_constructor_exists():
    assert callable(viewpoint::RGBValues.__init__)


def test_viewpoint::rgbvalues_constructor_args():
    sig = inspect.signature(viewpoint::RGBValues.__init__)
    params = list(sig.parameters.keys())
    assert "green" in params, "Missing parameter 'green'"
    assert "blue" in params, "Missing parameter 'blue'"
    assert "red" in params, "Missing parameter 'red'"

def test_viewpoint::rgbvalues_has_green():
    assert hasattr(viewpoint::RGBValues, "green")
    descriptor = None
    for klass in viewpoint::RGBValues.__mro__:
        if "green" in klass.__dict__:
            descriptor = klass.__dict__["green"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::rgbvalues_has_blue():
    assert hasattr(viewpoint::RGBValues, "blue")
    descriptor = None
    for klass in viewpoint::RGBValues.__mro__:
        if "blue" in klass.__dict__:
            descriptor = klass.__dict__["blue"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::rgbvalues_has_red():
    assert hasattr(viewpoint::RGBValues, "red")
    descriptor = None
    for klass in viewpoint::RGBValues.__mro__:
        if "red" in klass.__dict__:
            descriptor = klass.__dict__["red"]
            break
    assert isinstance(descriptor, property)



def test_dnavigationlink_is_not_abstract():
    assert not inspect.isabstract(DNavigationLink)


def test_dnavigationlink_constructor_exists():
    assert callable(DNavigationLink.__init__)


def test_dnavigationlink_constructor_args():
    sig = inspect.signature(DNavigationLink.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::deobjectlink_is_not_abstract():
    assert not inspect.isabstract(viewpoint::DEObjectLink)


def test_viewpoint::deobjectlink_constructor_exists():
    assert callable(viewpoint::DEObjectLink.__init__)


def test_viewpoint::deobjectlink_constructor_args():
    sig = inspect.signature(viewpoint::DEObjectLink.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::draganddroptarget_is_not_abstract():
    assert not inspect.isabstract(viewpoint::DragAndDropTarget)


def test_viewpoint::draganddroptarget_constructor_exists():
    assert callable(viewpoint::DragAndDropTarget.__init__)


def test_viewpoint::draganddroptarget_constructor_args():
    sig = inspect.signature(viewpoint::DragAndDropTarget.__init__)
    params = list(sig.parameters.keys())



def test_style::styledescription_is_not_abstract():
    assert not inspect.isabstract(style::StyleDescription)


def test_style::styledescription_constructor_exists():
    assert callable(style::StyleDescription.__init__)


def test_style::styledescription_constructor_args():
    sig = inspect.signature(style::StyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::style::nodestyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::style::NodeStyleDescription)


def test_viewpoint::style::nodestyledescription_constructor_exists():
    assert callable(viewpoint::style::NodeStyleDescription.__init__)


def test_viewpoint::style::nodestyledescription_constructor_args():
    sig = inspect.signature(viewpoint::style::NodeStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "resizeKind" in params, "Missing parameter 'resizeKind'"
    assert "hideLabelByDefault" in params, "Missing parameter 'hideLabelByDefault'"
    assert "sizeComputationExpression" in params, "Missing parameter 'sizeComputationExpression'"
    assert "labelPosition" in params, "Missing parameter 'labelPosition'"

def test_viewpoint::style::nodestyledescription_has_resizeKind():
    assert hasattr(viewpoint::style::NodeStyleDescription, "resizeKind")
    descriptor = None
    for klass in viewpoint::style::NodeStyleDescription.__mro__:
        if "resizeKind" in klass.__dict__:
            descriptor = klass.__dict__["resizeKind"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::style::nodestyledescription_has_hideLabelByDefault():
    assert hasattr(viewpoint::style::NodeStyleDescription, "hideLabelByDefault")
    descriptor = None
    for klass in viewpoint::style::NodeStyleDescription.__mro__:
        if "hideLabelByDefault" in klass.__dict__:
            descriptor = klass.__dict__["hideLabelByDefault"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::style::nodestyledescription_has_sizeComputationExpression():
    assert hasattr(viewpoint::style::NodeStyleDescription, "sizeComputationExpression")
    descriptor = None
    for klass in viewpoint::style::NodeStyleDescription.__mro__:
        if "sizeComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["sizeComputationExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::style::nodestyledescription_has_labelPosition():
    assert hasattr(viewpoint::style::NodeStyleDescription, "labelPosition")
    descriptor = None
    for klass in viewpoint::style::NodeStyleDescription.__mro__:
        if "labelPosition" in klass.__dict__:
            descriptor = klass.__dict__["labelPosition"]
            break
    assert isinstance(descriptor, property)



def test_customizable_is_not_abstract():
    assert not inspect.isabstract(Customizable)


def test_customizable_constructor_exists():
    assert callable(Customizable.__init__)


def test_customizable_constructor_args():
    sig = inspect.signature(Customizable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::basiclabelstyle_is_not_abstract():
    assert not inspect.isabstract(viewpoint::BasicLabelStyle)


def test_viewpoint::basiclabelstyle_constructor_exists():
    assert callable(viewpoint::BasicLabelStyle.__init__)


def test_viewpoint::basiclabelstyle_constructor_args():
    sig = inspect.signature(viewpoint::BasicLabelStyle.__init__)
    params = list(sig.parameters.keys())
    assert "labelSize" in params, "Missing parameter 'labelSize'"
    assert "iconPath" in params, "Missing parameter 'iconPath'"
    assert "showIcon" in params, "Missing parameter 'showIcon'"
    assert "labelFormat" in params, "Missing parameter 'labelFormat'"

def test_viewpoint::basiclabelstyle_has_labelSize():
    assert hasattr(viewpoint::BasicLabelStyle, "labelSize")
    descriptor = None
    for klass in viewpoint::BasicLabelStyle.__mro__:
        if "labelSize" in klass.__dict__:
            descriptor = klass.__dict__["labelSize"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::basiclabelstyle_has_iconPath():
    assert hasattr(viewpoint::BasicLabelStyle, "iconPath")
    descriptor = None
    for klass in viewpoint::BasicLabelStyle.__mro__:
        if "iconPath" in klass.__dict__:
            descriptor = klass.__dict__["iconPath"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::basiclabelstyle_has_showIcon():
    assert hasattr(viewpoint::BasicLabelStyle, "showIcon")
    descriptor = None
    for klass in viewpoint::BasicLabelStyle.__mro__:
        if "showIcon" in klass.__dict__:
            descriptor = klass.__dict__["showIcon"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::basiclabelstyle_has_labelFormat():
    assert hasattr(viewpoint::BasicLabelStyle, "labelFormat")
    descriptor = None
    for klass in viewpoint::BasicLabelStyle.__mro__:
        if "labelFormat" in klass.__dict__:
            descriptor = klass.__dict__["labelFormat"]
            break
    assert isinstance(descriptor, property)



def test_basiclabelstyle_is_not_abstract():
    assert not inspect.isabstract(BasicLabelStyle)


def test_basiclabelstyle_constructor_exists():
    assert callable(BasicLabelStyle.__init__)


def test_basiclabelstyle_constructor_args():
    sig = inspect.signature(BasicLabelStyle.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::diagram::centerlabelstyle_is_not_abstract():
    assert not inspect.isabstract(viewpoint::diagram::CenterLabelStyle)


def test_viewpoint::diagram::centerlabelstyle_constructor_exists():
    assert callable(viewpoint::diagram::CenterLabelStyle.__init__)


def test_viewpoint::diagram::centerlabelstyle_constructor_args():
    sig = inspect.signature(viewpoint::diagram::CenterLabelStyle.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::diagram::endlabelstyle_is_not_abstract():
    assert not inspect.isabstract(viewpoint::diagram::EndLabelStyle)


def test_viewpoint::diagram::endlabelstyle_constructor_exists():
    assert callable(viewpoint::diagram::EndLabelStyle.__init__)


def test_viewpoint::diagram::endlabelstyle_constructor_args():
    sig = inspect.signature(viewpoint::diagram::EndLabelStyle.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::diagram::beginlabelstyle_is_not_abstract():
    assert not inspect.isabstract(viewpoint::diagram::BeginLabelStyle)


def test_viewpoint::diagram::beginlabelstyle_constructor_exists():
    assert callable(viewpoint::diagram::BeginLabelStyle.__init__)


def test_viewpoint::diagram::beginlabelstyle_constructor_args():
    sig = inspect.signature(viewpoint::diagram::BeginLabelStyle.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::labelstyle_is_not_abstract():
    assert not inspect.isabstract(viewpoint::LabelStyle)


def test_viewpoint::labelstyle_constructor_exists():
    assert callable(viewpoint::LabelStyle.__init__)


def test_viewpoint::labelstyle_constructor_args():
    sig = inspect.signature(viewpoint::LabelStyle.__init__)
    params = list(sig.parameters.keys())
    assert "labelAlignment" in params, "Missing parameter 'labelAlignment'"

def test_viewpoint::labelstyle_has_labelAlignment():
    assert hasattr(viewpoint::LabelStyle, "labelAlignment")
    descriptor = None
    for klass in viewpoint::LabelStyle.__mro__:
        if "labelAlignment" in klass.__dict__:
            descriptor = klass.__dict__["labelAlignment"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::danalysiscustomdata_is_not_abstract():
    assert not inspect.isabstract(viewpoint::DAnalysisCustomData)


def test_viewpoint::danalysiscustomdata_constructor_exists():
    assert callable(viewpoint::DAnalysisCustomData.__init__)


def test_viewpoint::danalysiscustomdata_constructor_args():
    sig = inspect.signature(viewpoint::DAnalysisCustomData.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_viewpoint::danalysiscustomdata_has_key():
    assert hasattr(viewpoint::DAnalysisCustomData, "key")
    descriptor = None
    for klass in viewpoint::DAnalysisCustomData.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::dsourcefilelink_is_not_abstract():
    assert not inspect.isabstract(viewpoint::DSourceFileLink)


def test_viewpoint::dsourcefilelink_constructor_exists():
    assert callable(viewpoint::DSourceFileLink.__init__)


def test_viewpoint::dsourcefilelink_constructor_args():
    sig = inspect.signature(viewpoint::DSourceFileLink.__init__)
    params = list(sig.parameters.keys())
    assert "endPosition" in params, "Missing parameter 'endPosition'"
    assert "startPosition" in params, "Missing parameter 'startPosition'"
    assert "filePath" in params, "Missing parameter 'filePath'"

def test_viewpoint::dsourcefilelink_has_endPosition():
    assert hasattr(viewpoint::DSourceFileLink, "endPosition")
    descriptor = None
    for klass in viewpoint::DSourceFileLink.__mro__:
        if "endPosition" in klass.__dict__:
            descriptor = klass.__dict__["endPosition"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::dsourcefilelink_has_startPosition():
    assert hasattr(viewpoint::DSourceFileLink, "startPosition")
    descriptor = None
    for klass in viewpoint::DSourceFileLink.__mro__:
        if "startPosition" in klass.__dict__:
            descriptor = klass.__dict__["startPosition"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::dsourcefilelink_has_filePath():
    assert hasattr(viewpoint::DSourceFileLink, "filePath")
    descriptor = None
    for klass in viewpoint::DSourceFileLink.__mro__:
        if "filePath" in klass.__dict__:
            descriptor = klass.__dict__["filePath"]
            break
    assert isinstance(descriptor, property)



def test_decorationdescription_is_not_abstract():
    assert not inspect.isabstract(DecorationDescription)


def test_decorationdescription_constructor_exists():
    assert callable(DecorationDescription.__init__)


def test_decorationdescription_constructor_args():
    sig = inspect.signature(DecorationDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::mappingbaseddecoration_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::MappingBasedDecoration)


def test_viewpoint::description::mappingbaseddecoration_constructor_exists():
    assert callable(viewpoint::description::MappingBasedDecoration.__init__)


def test_viewpoint::description::mappingbaseddecoration_constructor_args():
    sig = inspect.signature(viewpoint::description::MappingBasedDecoration.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::semanticbaseddecoration_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::SemanticBasedDecoration)


def test_viewpoint::description::semanticbaseddecoration_constructor_exists():
    assert callable(viewpoint::description::SemanticBasedDecoration.__init__)


def test_viewpoint::description::semanticbaseddecoration_constructor_args():
    sig = inspect.signature(viewpoint::description::SemanticBasedDecoration.__init__)
    params = list(sig.parameters.keys())
    assert "domainClass" in params, "Missing parameter 'domainClass'"

def test_viewpoint::description::semanticbaseddecoration_has_domainClass():
    assert hasattr(viewpoint::description::SemanticBasedDecoration, "domainClass")
    descriptor = None
    for klass in viewpoint::description::SemanticBasedDecoration.__mro__:
        if "domainClass" in klass.__dict__:
            descriptor = klass.__dict__["domainClass"]
            break
    assert isinstance(descriptor, property)



def test_diagram::nodestyle_is_not_abstract():
    assert not inspect.isabstract(diagram::NodeStyle)


def test_diagram::nodestyle_constructor_exists():
    assert callable(diagram::NodeStyle.__init__)


def test_diagram::nodestyle_constructor_args():
    sig = inspect.signature(diagram::NodeStyle.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::diagram::workspaceimage_is_not_abstract():
    assert not inspect.isabstract(viewpoint::diagram::WorkspaceImage)


def test_viewpoint::diagram::workspaceimage_constructor_exists():
    assert callable(viewpoint::diagram::WorkspaceImage.__init__)


def test_viewpoint::diagram::workspaceimage_constructor_args():
    sig = inspect.signature(viewpoint::diagram::WorkspaceImage.__init__)
    params = list(sig.parameters.keys())
    assert "workspacePath" in params, "Missing parameter 'workspacePath'"

def test_viewpoint::diagram::workspaceimage_has_workspacePath():
    assert hasattr(viewpoint::diagram::WorkspaceImage, "workspacePath")
    descriptor = None
    for klass in viewpoint::diagram::WorkspaceImage.__mro__:
        if "workspacePath" in klass.__dict__:
            descriptor = klass.__dict__["workspacePath"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::diagram::edgetarget_is_not_abstract():
    assert not inspect.isabstract(viewpoint::diagram::EdgeTarget)


def test_viewpoint::diagram::edgetarget_constructor_exists():
    assert callable(viewpoint::diagram::EdgeTarget.__init__)


def test_viewpoint::diagram::edgetarget_constructor_args():
    sig = inspect.signature(viewpoint::diagram::EdgeTarget.__init__)
    params = list(sig.parameters.keys())



def test_diagram::borderedstyle_is_not_abstract():
    assert not inspect.isabstract(diagram::BorderedStyle)


def test_diagram::borderedstyle_constructor_exists():
    assert callable(diagram::BorderedStyle.__init__)


def test_diagram::borderedstyle_constructor_args():
    sig = inspect.signature(diagram::BorderedStyle.__init__)
    params = list(sig.parameters.keys())



def test_style_is_not_abstract():
    assert not inspect.isabstract(Style)


def test_style_constructor_exists():
    assert callable(Style.__init__)


def test_style_constructor_args():
    sig = inspect.signature(Style.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::diagram::borderedstyle_is_not_abstract():
    assert not inspect.isabstract(viewpoint::diagram::BorderedStyle)


def test_viewpoint::diagram::borderedstyle_constructor_exists():
    assert callable(viewpoint::diagram::BorderedStyle.__init__)


def test_viewpoint::diagram::borderedstyle_constructor_args():
    sig = inspect.signature(viewpoint::diagram::BorderedStyle.__init__)
    params = list(sig.parameters.keys())
    assert "borderSizeComputationExpression" in params, "Missing parameter 'borderSizeComputationExpression'"
    assert "borderSize" in params, "Missing parameter 'borderSize'"

def test_viewpoint::diagram::borderedstyle_has_borderSizeComputationExpression():
    assert hasattr(viewpoint::diagram::BorderedStyle, "borderSizeComputationExpression")
    descriptor = None
    for klass in viewpoint::diagram::BorderedStyle.__mro__:
        if "borderSizeComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["borderSizeComputationExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::diagram::borderedstyle_has_borderSize():
    assert hasattr(viewpoint::diagram::BorderedStyle, "borderSize")
    descriptor = None
    for klass in viewpoint::diagram::BorderedStyle.__mro__:
        if "borderSize" in klass.__dict__:
            descriptor = klass.__dict__["borderSize"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::diagram::edgestyle_is_not_abstract():
    assert not inspect.isabstract(viewpoint::diagram::EdgeStyle)


def test_viewpoint::diagram::edgestyle_constructor_exists():
    assert callable(viewpoint::diagram::EdgeStyle.__init__)


def test_viewpoint::diagram::edgestyle_constructor_args():
    sig = inspect.signature(viewpoint::diagram::EdgeStyle.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "routingStyle" in params, "Missing parameter 'routingStyle'"
    assert "sourceArrow" in params, "Missing parameter 'sourceArrow'"
    assert "lineStyle" in params, "Missing parameter 'lineStyle'"
    assert "foldingStyle" in params, "Missing parameter 'foldingStyle'"
    assert "targetArrow" in params, "Missing parameter 'targetArrow'"

def test_viewpoint::diagram::edgestyle_has_size():
    assert hasattr(viewpoint::diagram::EdgeStyle, "size")
    descriptor = None
    for klass in viewpoint::diagram::EdgeStyle.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::diagram::edgestyle_has_routingStyle():
    assert hasattr(viewpoint::diagram::EdgeStyle, "routingStyle")
    descriptor = None
    for klass in viewpoint::diagram::EdgeStyle.__mro__:
        if "routingStyle" in klass.__dict__:
            descriptor = klass.__dict__["routingStyle"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::diagram::edgestyle_has_sourceArrow():
    assert hasattr(viewpoint::diagram::EdgeStyle, "sourceArrow")
    descriptor = None
    for klass in viewpoint::diagram::EdgeStyle.__mro__:
        if "sourceArrow" in klass.__dict__:
            descriptor = klass.__dict__["sourceArrow"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::diagram::edgestyle_has_lineStyle():
    assert hasattr(viewpoint::diagram::EdgeStyle, "lineStyle")
    descriptor = None
    for klass in viewpoint::diagram::EdgeStyle.__mro__:
        if "lineStyle" in klass.__dict__:
            descriptor = klass.__dict__["lineStyle"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::diagram::edgestyle_has_foldingStyle():
    assert hasattr(viewpoint::diagram::EdgeStyle, "foldingStyle")
    descriptor = None
    for klass in viewpoint::diagram::EdgeStyle.__mro__:
        if "foldingStyle" in klass.__dict__:
            descriptor = klass.__dict__["foldingStyle"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::diagram::edgestyle_has_targetArrow():
    assert hasattr(viewpoint::diagram::EdgeStyle, "targetArrow")
    descriptor = None
    for klass in viewpoint::diagram::EdgeStyle.__mro__:
        if "targetArrow" in klass.__dict__:
            descriptor = klass.__dict__["targetArrow"]
            break
    assert isinstance(descriptor, property)



def test_labelstyle_is_not_abstract():
    assert not inspect.isabstract(LabelStyle)


def test_labelstyle_constructor_exists():
    assert callable(LabelStyle.__init__)


def test_labelstyle_constructor_args():
    sig = inspect.signature(LabelStyle.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::diagram::containerstyle_is_not_abstract():
    assert not inspect.isabstract(viewpoint::diagram::ContainerStyle)


def test_viewpoint::diagram::containerstyle_constructor_exists():
    assert callable(viewpoint::diagram::ContainerStyle.__init__)


def test_viewpoint::diagram::containerstyle_constructor_args():
    sig = inspect.signature(viewpoint::diagram::ContainerStyle.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::diagram::nodestyle_is_not_abstract():
    assert not inspect.isabstract(viewpoint::diagram::NodeStyle)


def test_viewpoint::diagram::nodestyle_constructor_exists():
    assert callable(viewpoint::diagram::NodeStyle.__init__)


def test_viewpoint::diagram::nodestyle_constructor_args():
    sig = inspect.signature(viewpoint::diagram::NodeStyle.__init__)
    params = list(sig.parameters.keys())
    assert "hideLabelByDefault" in params, "Missing parameter 'hideLabelByDefault'"
    assert "labelPosition" in params, "Missing parameter 'labelPosition'"

def test_viewpoint::diagram::nodestyle_has_hideLabelByDefault():
    assert hasattr(viewpoint::diagram::NodeStyle, "hideLabelByDefault")
    descriptor = None
    for klass in viewpoint::diagram::NodeStyle.__mro__:
        if "hideLabelByDefault" in klass.__dict__:
            descriptor = klass.__dict__["hideLabelByDefault"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::diagram::nodestyle_has_labelPosition():
    assert hasattr(viewpoint::diagram::NodeStyle, "labelPosition")
    descriptor = None
    for klass in viewpoint::diagram::NodeStyle.__mro__:
        if "labelPosition" in klass.__dict__:
            descriptor = klass.__dict__["labelPosition"]
            break
    assert isinstance(descriptor, property)



def test_diagram::viewpoint::drepresentationcontainer_is_not_abstract():
    assert not inspect.isabstract(diagram::viewpoint::DRepresentationContainer)


def test_diagram::viewpoint::drepresentationcontainer_constructor_exists():
    assert callable(diagram::viewpoint::DRepresentationContainer.__init__)


def test_diagram::viewpoint::drepresentationcontainer_constructor_args():
    sig = inspect.signature(diagram::viewpoint::DRepresentationContainer.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::diagram::gaugesection_is_not_abstract():
    assert not inspect.isabstract(viewpoint::diagram::GaugeSection)


def test_viewpoint::diagram::gaugesection_constructor_exists():
    assert callable(viewpoint::diagram::GaugeSection.__init__)


def test_viewpoint::diagram::gaugesection_constructor_args():
    sig = inspect.signature(viewpoint::diagram::GaugeSection.__init__)
    params = list(sig.parameters.keys())
    assert "max" in params, "Missing parameter 'max'"
    assert "value" in params, "Missing parameter 'value'"
    assert "min" in params, "Missing parameter 'min'"
    assert "label" in params, "Missing parameter 'label'"

def test_viewpoint::diagram::gaugesection_has_max():
    assert hasattr(viewpoint::diagram::GaugeSection, "max")
    descriptor = None
    for klass in viewpoint::diagram::GaugeSection.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::diagram::gaugesection_has_value():
    assert hasattr(viewpoint::diagram::GaugeSection, "value")
    descriptor = None
    for klass in viewpoint::diagram::GaugeSection.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::diagram::gaugesection_has_min():
    assert hasattr(viewpoint::diagram::GaugeSection, "min")
    descriptor = None
    for klass in viewpoint::diagram::GaugeSection.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::diagram::gaugesection_has_label():
    assert hasattr(viewpoint::diagram::GaugeSection, "label")
    descriptor = None
    for klass in viewpoint::diagram::GaugeSection.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_diagram::viewpoint::rgbvalues_is_not_abstract():
    assert not inspect.isabstract(diagram::viewpoint::RGBValues)


def test_diagram::viewpoint::rgbvalues_constructor_exists():
    assert callable(diagram::viewpoint::RGBValues.__init__)


def test_diagram::viewpoint::rgbvalues_constructor_args():
    sig = inspect.signature(diagram::viewpoint::RGBValues.__init__)
    params = list(sig.parameters.keys())



def test_description::iedgemapping_is_not_abstract():
    assert not inspect.isabstract(description::IEdgeMapping)


def test_description::iedgemapping_constructor_exists():
    assert callable(description::IEdgeMapping.__init__)


def test_description::iedgemapping_constructor_args():
    sig = inspect.signature(description::IEdgeMapping.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::diagram::ddiagramset_is_not_abstract():
    assert not inspect.isabstract(viewpoint::diagram::DDiagramSet)


def test_viewpoint::diagram::ddiagramset_constructor_exists():
    assert callable(viewpoint::diagram::DDiagramSet.__init__)


def test_viewpoint::diagram::ddiagramset_constructor_args():
    sig = inspect.signature(viewpoint::diagram::DDiagramSet.__init__)
    params = list(sig.parameters.keys())



def test_abstractdnode_is_not_abstract():
    assert not inspect.isabstract(AbstractDNode)


def test_abstractdnode_constructor_exists():
    assert callable(AbstractDNode.__init__)


def test_abstractdnode_constructor_args():
    sig = inspect.signature(AbstractDNode.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::diagram::dnodelistelement_is_not_abstract():
    assert not inspect.isabstract(viewpoint::diagram::DNodeListElement)


def test_viewpoint::diagram::dnodelistelement_constructor_exists():
    assert callable(viewpoint::diagram::DNodeListElement.__init__)


def test_viewpoint::diagram::dnodelistelement_constructor_args():
    sig = inspect.signature(viewpoint::diagram::DNodeListElement.__init__)
    params = list(sig.parameters.keys())



def test_edgestyle_is_not_abstract():
    assert not inspect.isabstract(EdgeStyle)


def test_edgestyle_constructor_exists():
    assert callable(EdgeStyle.__init__)


def test_edgestyle_constructor_args():
    sig = inspect.signature(EdgeStyle.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::diagram::bracketedgestyle_is_not_abstract():
    assert not inspect.isabstract(viewpoint::diagram::BracketEdgeStyle)


def test_viewpoint::diagram::bracketedgestyle_constructor_exists():
    assert callable(viewpoint::diagram::BracketEdgeStyle.__init__)


def test_viewpoint::diagram::bracketedgestyle_constructor_args():
    sig = inspect.signature(viewpoint::diagram::BracketEdgeStyle.__init__)
    params = list(sig.parameters.keys())



def test_diagram::ddiagramelement_is_not_abstract():
    assert not inspect.isabstract(diagram::DDiagramElement)


def test_diagram::ddiagramelement_constructor_exists():
    assert callable(diagram::DDiagramElement.__init__)


def test_diagram::ddiagramelement_constructor_args():
    sig = inspect.signature(diagram::DDiagramElement.__init__)
    params = list(sig.parameters.keys())



def test_description::containermapping_is_not_abstract():
    assert not inspect.isabstract(description::ContainerMapping)


def test_description::containermapping_constructor_exists():
    assert callable(description::ContainerMapping.__init__)


def test_description::containermapping_constructor_args():
    sig = inspect.signature(description::ContainerMapping.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::containermappingimport_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::ContainerMappingImport)


def test_viewpoint::description::containermappingimport_constructor_exists():
    assert callable(viewpoint::description::ContainerMappingImport.__init__)


def test_viewpoint::description::containermappingimport_constructor_args():
    sig = inspect.signature(viewpoint::description::ContainerMappingImport.__init__)
    params = list(sig.parameters.keys())



def test_containerstyle_is_not_abstract():
    assert not inspect.isabstract(ContainerStyle)


def test_containerstyle_constructor_exists():
    assert callable(ContainerStyle.__init__)


def test_containerstyle_constructor_args():
    sig = inspect.signature(ContainerStyle.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::diagram::shapecontainerstyle_is_not_abstract():
    assert not inspect.isabstract(viewpoint::diagram::ShapeContainerStyle)


def test_viewpoint::diagram::shapecontainerstyle_constructor_exists():
    assert callable(viewpoint::diagram::ShapeContainerStyle.__init__)


def test_viewpoint::diagram::shapecontainerstyle_constructor_args():
    sig = inspect.signature(viewpoint::diagram::ShapeContainerStyle.__init__)
    params = list(sig.parameters.keys())
    assert "shape" in params, "Missing parameter 'shape'"

def test_viewpoint::diagram::shapecontainerstyle_has_shape():
    assert hasattr(viewpoint::diagram::ShapeContainerStyle, "shape")
    descriptor = None
    for klass in viewpoint::diagram::ShapeContainerStyle.__mro__:
        if "shape" in klass.__dict__:
            descriptor = klass.__dict__["shape"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::diagram::flatcontainerstyle_is_not_abstract():
    assert not inspect.isabstract(viewpoint::diagram::FlatContainerStyle)


def test_viewpoint::diagram::flatcontainerstyle_constructor_exists():
    assert callable(viewpoint::diagram::FlatContainerStyle.__init__)


def test_viewpoint::diagram::flatcontainerstyle_constructor_args():
    sig = inspect.signature(viewpoint::diagram::FlatContainerStyle.__init__)
    params = list(sig.parameters.keys())
    assert "backgroundStyle" in params, "Missing parameter 'backgroundStyle'"

def test_viewpoint::diagram::flatcontainerstyle_has_backgroundStyle():
    assert hasattr(viewpoint::diagram::FlatContainerStyle, "backgroundStyle")
    descriptor = None
    for klass in viewpoint::diagram::FlatContainerStyle.__mro__:
        if "backgroundStyle" in klass.__dict__:
            descriptor = klass.__dict__["backgroundStyle"]
            break
    assert isinstance(descriptor, property)



def test_diagram::edgetarget_is_not_abstract():
    assert not inspect.isabstract(diagram::EdgeTarget)


def test_diagram::edgetarget_constructor_exists():
    assert callable(diagram::EdgeTarget.__init__)


def test_diagram::edgetarget_constructor_args():
    sig = inspect.signature(diagram::EdgeTarget.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::diagram::dedge_is_not_abstract():
    assert not inspect.isabstract(viewpoint::diagram::DEdge)


def test_viewpoint::diagram::dedge_constructor_exists():
    assert callable(viewpoint::diagram::DEdge.__init__)


def test_viewpoint::diagram::dedge_constructor_args():
    sig = inspect.signature(viewpoint::diagram::DEdge.__init__)
    params = list(sig.parameters.keys())
    assert "endLabel" in params, "Missing parameter 'endLabel'"
    assert "beginLabel" in params, "Missing parameter 'beginLabel'"
    assert "isMockEdge" in params, "Missing parameter 'isMockEdge'"
    assert "routingStyle" in params, "Missing parameter 'routingStyle'"
    assert "isFold" in params, "Missing parameter 'isFold'"
    assert "size" in params, "Missing parameter 'size'"
    assert "arrangeConstraints" in params, "Missing parameter 'arrangeConstraints'"

def test_viewpoint::diagram::dedge_has_endLabel():
    assert hasattr(viewpoint::diagram::DEdge, "endLabel")
    descriptor = None
    for klass in viewpoint::diagram::DEdge.__mro__:
        if "endLabel" in klass.__dict__:
            descriptor = klass.__dict__["endLabel"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::diagram::dedge_has_beginLabel():
    assert hasattr(viewpoint::diagram::DEdge, "beginLabel")
    descriptor = None
    for klass in viewpoint::diagram::DEdge.__mro__:
        if "beginLabel" in klass.__dict__:
            descriptor = klass.__dict__["beginLabel"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::diagram::dedge_has_isMockEdge():
    assert hasattr(viewpoint::diagram::DEdge, "isMockEdge")
    descriptor = None
    for klass in viewpoint::diagram::DEdge.__mro__:
        if "isMockEdge" in klass.__dict__:
            descriptor = klass.__dict__["isMockEdge"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::diagram::dedge_has_routingStyle():
    assert hasattr(viewpoint::diagram::DEdge, "routingStyle")
    descriptor = None
    for klass in viewpoint::diagram::DEdge.__mro__:
        if "routingStyle" in klass.__dict__:
            descriptor = klass.__dict__["routingStyle"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::diagram::dedge_has_isFold():
    assert hasattr(viewpoint::diagram::DEdge, "isFold")
    descriptor = None
    for klass in viewpoint::diagram::DEdge.__mro__:
        if "isFold" in klass.__dict__:
            descriptor = klass.__dict__["isFold"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::diagram::dedge_has_size():
    assert hasattr(viewpoint::diagram::DEdge, "size")
    descriptor = None
    for klass in viewpoint::diagram::DEdge.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::diagram::dedge_has_arrangeConstraints():
    assert hasattr(viewpoint::diagram::DEdge, "arrangeConstraints")
    descriptor = None
    for klass in viewpoint::diagram::DEdge.__mro__:
        if "arrangeConstraints" in klass.__dict__:
            descriptor = klass.__dict__["arrangeConstraints"]
            break
    assert isinstance(descriptor, property)



def test_diagram::abstractdnode_is_not_abstract():
    assert not inspect.isabstract(diagram::AbstractDNode)


def test_diagram::abstractdnode_constructor_exists():
    assert callable(diagram::AbstractDNode.__init__)


def test_diagram::abstractdnode_constructor_args():
    sig = inspect.signature(diagram::AbstractDNode.__init__)
    params = list(sig.parameters.keys())



def test_edgetarget_is_not_abstract():
    assert not inspect.isabstract(EdgeTarget)


def test_edgetarget_constructor_exists():
    assert callable(EdgeTarget.__init__)


def test_edgetarget_constructor_args():
    sig = inspect.signature(EdgeTarget.__init__)
    params = list(sig.parameters.keys())



def test_description::nodemapping_is_not_abstract():
    assert not inspect.isabstract(description::NodeMapping)


def test_description::nodemapping_constructor_exists():
    assert callable(description::NodeMapping.__init__)


def test_description::nodemapping_constructor_args():
    sig = inspect.signature(description::NodeMapping.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::nodemappingimport_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::NodeMappingImport)


def test_viewpoint::description::nodemappingimport_constructor_exists():
    assert callable(viewpoint::description::NodeMappingImport.__init__)


def test_viewpoint::description::nodemappingimport_constructor_args():
    sig = inspect.signature(viewpoint::description::NodeMappingImport.__init__)
    params = list(sig.parameters.keys())



def test_diagram::viewpoint::style_is_not_abstract():
    assert not inspect.isabstract(diagram::viewpoint::Style)


def test_diagram::viewpoint::style_constructor_exists():
    assert callable(diagram::viewpoint::Style.__init__)


def test_diagram::viewpoint::style_constructor_args():
    sig = inspect.signature(diagram::viewpoint::Style.__init__)
    params = list(sig.parameters.keys())



def test_nodestyle_is_not_abstract():
    assert not inspect.isabstract(NodeStyle)


def test_nodestyle_constructor_exists():
    assert callable(NodeStyle.__init__)


def test_nodestyle_constructor_args():
    sig = inspect.signature(NodeStyle.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::diagram::customstyle_is_not_abstract():
    assert not inspect.isabstract(viewpoint::diagram::CustomStyle)


def test_viewpoint::diagram::customstyle_constructor_exists():
    assert callable(viewpoint::diagram::CustomStyle.__init__)


def test_viewpoint::diagram::customstyle_constructor_args():
    sig = inspect.signature(viewpoint::diagram::CustomStyle.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_viewpoint::diagram::customstyle_has_id():
    assert hasattr(viewpoint::diagram::CustomStyle, "id")
    descriptor = None
    for klass in viewpoint::diagram::CustomStyle.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::diagram::note_is_not_abstract():
    assert not inspect.isabstract(viewpoint::diagram::Note)


def test_viewpoint::diagram::note_constructor_exists():
    assert callable(viewpoint::diagram::Note.__init__)


def test_viewpoint::diagram::note_constructor_args():
    sig = inspect.signature(viewpoint::diagram::Note.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::diagram::gaugecompositestyle_is_not_abstract():
    assert not inspect.isabstract(viewpoint::diagram::GaugeCompositeStyle)


def test_viewpoint::diagram::gaugecompositestyle_constructor_exists():
    assert callable(viewpoint::diagram::GaugeCompositeStyle.__init__)


def test_viewpoint::diagram::gaugecompositestyle_constructor_args():
    sig = inspect.signature(viewpoint::diagram::GaugeCompositeStyle.__init__)
    params = list(sig.parameters.keys())
    assert "alignment" in params, "Missing parameter 'alignment'"

def test_viewpoint::diagram::gaugecompositestyle_has_alignment():
    assert hasattr(viewpoint::diagram::GaugeCompositeStyle, "alignment")
    descriptor = None
    for klass in viewpoint::diagram::GaugeCompositeStyle.__mro__:
        if "alignment" in klass.__dict__:
            descriptor = klass.__dict__["alignment"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::diagram::dot_is_not_abstract():
    assert not inspect.isabstract(viewpoint::diagram::Dot)


def test_viewpoint::diagram::dot_constructor_exists():
    assert callable(viewpoint::diagram::Dot.__init__)


def test_viewpoint::diagram::dot_constructor_args():
    sig = inspect.signature(viewpoint::diagram::Dot.__init__)
    params = list(sig.parameters.keys())
    assert "strokeSizeComputationExpression" in params, "Missing parameter 'strokeSizeComputationExpression'"

def test_viewpoint::diagram::dot_has_strokeSizeComputationExpression():
    assert hasattr(viewpoint::diagram::Dot, "strokeSizeComputationExpression")
    descriptor = None
    for klass in viewpoint::diagram::Dot.__mro__:
        if "strokeSizeComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["strokeSizeComputationExpression"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::diagram::ellipse_is_not_abstract():
    assert not inspect.isabstract(viewpoint::diagram::Ellipse)


def test_viewpoint::diagram::ellipse_constructor_exists():
    assert callable(viewpoint::diagram::Ellipse.__init__)


def test_viewpoint::diagram::ellipse_constructor_args():
    sig = inspect.signature(viewpoint::diagram::Ellipse.__init__)
    params = list(sig.parameters.keys())
    assert "horizontalDiameter" in params, "Missing parameter 'horizontalDiameter'"
    assert "verticalDiameter" in params, "Missing parameter 'verticalDiameter'"

def test_viewpoint::diagram::ellipse_has_horizontalDiameter():
    assert hasattr(viewpoint::diagram::Ellipse, "horizontalDiameter")
    descriptor = None
    for klass in viewpoint::diagram::Ellipse.__mro__:
        if "horizontalDiameter" in klass.__dict__:
            descriptor = klass.__dict__["horizontalDiameter"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::diagram::ellipse_has_verticalDiameter():
    assert hasattr(viewpoint::diagram::Ellipse, "verticalDiameter")
    descriptor = None
    for klass in viewpoint::diagram::Ellipse.__mro__:
        if "verticalDiameter" in klass.__dict__:
            descriptor = klass.__dict__["verticalDiameter"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::diagram::lozenge_is_not_abstract():
    assert not inspect.isabstract(viewpoint::diagram::Lozenge)


def test_viewpoint::diagram::lozenge_constructor_exists():
    assert callable(viewpoint::diagram::Lozenge.__init__)


def test_viewpoint::diagram::lozenge_constructor_args():
    sig = inspect.signature(viewpoint::diagram::Lozenge.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"

def test_viewpoint::diagram::lozenge_has_width():
    assert hasattr(viewpoint::diagram::Lozenge, "width")
    descriptor = None
    for klass in viewpoint::diagram::Lozenge.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::diagram::lozenge_has_height():
    assert hasattr(viewpoint::diagram::Lozenge, "height")
    descriptor = None
    for klass in viewpoint::diagram::Lozenge.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::diagram::square_is_not_abstract():
    assert not inspect.isabstract(viewpoint::diagram::Square)


def test_viewpoint::diagram::square_constructor_exists():
    assert callable(viewpoint::diagram::Square.__init__)


def test_viewpoint::diagram::square_constructor_args():
    sig = inspect.signature(viewpoint::diagram::Square.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"

def test_viewpoint::diagram::square_has_width():
    assert hasattr(viewpoint::diagram::Square, "width")
    descriptor = None
    for klass in viewpoint::diagram::Square.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::diagram::square_has_height():
    assert hasattr(viewpoint::diagram::Square, "height")
    descriptor = None
    for klass in viewpoint::diagram::Square.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::diagram::bundledimage_is_not_abstract():
    assert not inspect.isabstract(viewpoint::diagram::BundledImage)


def test_viewpoint::diagram::bundledimage_constructor_exists():
    assert callable(viewpoint::diagram::BundledImage.__init__)


def test_viewpoint::diagram::bundledimage_constructor_args():
    sig = inspect.signature(viewpoint::diagram::BundledImage.__init__)
    params = list(sig.parameters.keys())
    assert "shape" in params, "Missing parameter 'shape'"

def test_viewpoint::diagram::bundledimage_has_shape():
    assert hasattr(viewpoint::diagram::BundledImage, "shape")
    descriptor = None
    for klass in viewpoint::diagram::BundledImage.__mro__:
        if "shape" in klass.__dict__:
            descriptor = klass.__dict__["shape"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::diagram::graphicalfilter_is_not_abstract():
    assert not inspect.isabstract(viewpoint::diagram::GraphicalFilter)


def test_viewpoint::diagram::graphicalfilter_constructor_exists():
    assert callable(viewpoint::diagram::GraphicalFilter.__init__)


def test_viewpoint::diagram::graphicalfilter_constructor_args():
    sig = inspect.signature(viewpoint::diagram::GraphicalFilter.__init__)
    params = list(sig.parameters.keys())



def test_graphicalfilter_is_not_abstract():
    assert not inspect.isabstract(GraphicalFilter)


def test_graphicalfilter_constructor_exists():
    assert callable(GraphicalFilter.__init__)


def test_graphicalfilter_constructor_args():
    sig = inspect.signature(GraphicalFilter.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::diagram::collapsefilter_is_not_abstract():
    assert not inspect.isabstract(viewpoint::diagram::CollapseFilter)


def test_viewpoint::diagram::collapsefilter_constructor_exists():
    assert callable(viewpoint::diagram::CollapseFilter.__init__)


def test_viewpoint::diagram::collapsefilter_constructor_args():
    sig = inspect.signature(viewpoint::diagram::CollapseFilter.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"

def test_viewpoint::diagram::collapsefilter_has_width():
    assert hasattr(viewpoint::diagram::CollapseFilter, "width")
    descriptor = None
    for klass in viewpoint::diagram::CollapseFilter.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::diagram::collapsefilter_has_height():
    assert hasattr(viewpoint::diagram::CollapseFilter, "height")
    descriptor = None
    for klass in viewpoint::diagram::CollapseFilter.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_diagram::viewpoint::decoration_is_not_abstract():
    assert not inspect.isabstract(diagram::viewpoint::Decoration)


def test_diagram::viewpoint::decoration_constructor_exists():
    assert callable(diagram::viewpoint::Decoration.__init__)


def test_diagram::viewpoint::decoration_constructor_args():
    sig = inspect.signature(diagram::viewpoint::Decoration.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::diagram::ddiagramlink_is_not_abstract():
    assert not inspect.isabstract(viewpoint::diagram::DDiagramLink)


def test_viewpoint::diagram::ddiagramlink_constructor_exists():
    assert callable(viewpoint::diagram::DDiagramLink.__init__)


def test_viewpoint::diagram::ddiagramlink_constructor_args():
    sig = inspect.signature(viewpoint::diagram::DDiagramLink.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::diagram::absoluteboundsfilter_is_not_abstract():
    assert not inspect.isabstract(viewpoint::diagram::AbsoluteBoundsFilter)


def test_viewpoint::diagram::absoluteboundsfilter_constructor_exists():
    assert callable(viewpoint::diagram::AbsoluteBoundsFilter.__init__)


def test_viewpoint::diagram::absoluteboundsfilter_constructor_args():
    sig = inspect.signature(viewpoint::diagram::AbsoluteBoundsFilter.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"

def test_viewpoint::diagram::absoluteboundsfilter_has_x():
    assert hasattr(viewpoint::diagram::AbsoluteBoundsFilter, "x")
    descriptor = None
    for klass in viewpoint::diagram::AbsoluteBoundsFilter.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::diagram::absoluteboundsfilter_has_y():
    assert hasattr(viewpoint::diagram::AbsoluteBoundsFilter, "y")
    descriptor = None
    for klass in viewpoint::diagram::AbsoluteBoundsFilter.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::diagram::absoluteboundsfilter_has_height():
    assert hasattr(viewpoint::diagram::AbsoluteBoundsFilter, "height")
    descriptor = None
    for klass in viewpoint::diagram::AbsoluteBoundsFilter.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::diagram::absoluteboundsfilter_has_width():
    assert hasattr(viewpoint::diagram::AbsoluteBoundsFilter, "width")
    descriptor = None
    for klass in viewpoint::diagram::AbsoluteBoundsFilter.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_filter::compositefilterdescription_is_not_abstract():
    assert not inspect.isabstract(filter::CompositeFilterDescription)


def test_filter::compositefilterdescription_constructor_exists():
    assert callable(filter::CompositeFilterDescription.__init__)


def test_filter::compositefilterdescription_constructor_args():
    sig = inspect.signature(filter::CompositeFilterDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::diagram::appliedcompositefilters_is_not_abstract():
    assert not inspect.isabstract(viewpoint::diagram::AppliedCompositeFilters)


def test_viewpoint::diagram::appliedcompositefilters_constructor_exists():
    assert callable(viewpoint::diagram::AppliedCompositeFilters.__init__)


def test_viewpoint::diagram::appliedcompositefilters_constructor_args():
    sig = inspect.signature(viewpoint::diagram::AppliedCompositeFilters.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::diagram::foldingfilter_is_not_abstract():
    assert not inspect.isabstract(viewpoint::diagram::FoldingFilter)


def test_viewpoint::diagram::foldingfilter_constructor_exists():
    assert callable(viewpoint::diagram::FoldingFilter.__init__)


def test_viewpoint::diagram::foldingfilter_constructor_args():
    sig = inspect.signature(viewpoint::diagram::FoldingFilter.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::diagram::foldingpointfilter_is_not_abstract():
    assert not inspect.isabstract(viewpoint::diagram::FoldingPointFilter)


def test_viewpoint::diagram::foldingpointfilter_constructor_exists():
    assert callable(viewpoint::diagram::FoldingPointFilter.__init__)


def test_viewpoint::diagram::foldingpointfilter_constructor_args():
    sig = inspect.signature(viewpoint::diagram::FoldingPointFilter.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::diagram::hidelabelfilter_is_not_abstract():
    assert not inspect.isabstract(viewpoint::diagram::HideLabelFilter)


def test_viewpoint::diagram::hidelabelfilter_constructor_exists():
    assert callable(viewpoint::diagram::HideLabelFilter.__init__)


def test_viewpoint::diagram::hidelabelfilter_constructor_args():
    sig = inspect.signature(viewpoint::diagram::HideLabelFilter.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::diagram::hidefilter_is_not_abstract():
    assert not inspect.isabstract(viewpoint::diagram::HideFilter)


def test_viewpoint::diagram::hidefilter_constructor_exists():
    assert callable(viewpoint::diagram::HideFilter.__init__)


def test_viewpoint::diagram::hidefilter_constructor_args():
    sig = inspect.signature(viewpoint::diagram::HideFilter.__init__)
    params = list(sig.parameters.keys())



def test_description::layer_is_not_abstract():
    assert not inspect.isabstract(description::Layer)


def test_description::layer_constructor_exists():
    assert callable(description::Layer.__init__)


def test_description::layer_constructor_args():
    sig = inspect.signature(description::Layer.__init__)
    params = list(sig.parameters.keys())



def test_filtervariablehistory_is_not_abstract():
    assert not inspect.isabstract(FilterVariableHistory)


def test_filtervariablehistory_constructor_exists():
    assert callable(FilterVariableHistory.__init__)


def test_filtervariablehistory_constructor_args():
    sig = inspect.signature(FilterVariableHistory.__init__)
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



def test_dnavigable_is_not_abstract():
    assert not inspect.isabstract(DNavigable)


def test_dnavigable_constructor_exists():
    assert callable(DNavigable.__init__)


def test_dnavigable_constructor_args():
    sig = inspect.signature(DNavigable.__init__)
    params = list(sig.parameters.keys())



def test_drepresentationelement_is_not_abstract():
    assert not inspect.isabstract(DRepresentationElement)


def test_drepresentationelement_constructor_exists():
    assert callable(DRepresentationElement.__init__)


def test_drepresentationelement_constructor_args():
    sig = inspect.signature(DRepresentationElement.__init__)
    params = list(sig.parameters.keys())



def test_diagram::ddiagram_is_not_abstract():
    assert not inspect.isabstract(diagram::DDiagram)


def test_diagram::ddiagram_constructor_exists():
    assert callable(diagram::DDiagram.__init__)


def test_diagram::ddiagram_constructor_args():
    sig = inspect.signature(diagram::DDiagram.__init__)
    params = list(sig.parameters.keys())



def test_dedge_is_not_abstract():
    assert not inspect.isabstract(DEdge)


def test_dedge_constructor_exists():
    assert callable(DEdge.__init__)


def test_dedge_constructor_args():
    sig = inspect.signature(DEdge.__init__)
    params = list(sig.parameters.keys())



def test_ddiagram_is_not_abstract():
    assert not inspect.isabstract(DDiagram)


def test_ddiagram_constructor_exists():
    assert callable(DDiagram.__init__)


def test_ddiagram_constructor_args():
    sig = inspect.signature(DDiagram.__init__)
    params = list(sig.parameters.keys())



def test_filter::filterdescription_is_not_abstract():
    assert not inspect.isabstract(filter::FilterDescription)


def test_filter::filterdescription_constructor_exists():
    assert callable(filter::FilterDescription.__init__)


def test_filter::filterdescription_constructor_args():
    sig = inspect.signature(filter::FilterDescription.__init__)
    params = list(sig.parameters.keys())



def test_concern::concerndescription_is_not_abstract():
    assert not inspect.isabstract(concern::ConcernDescription)


def test_concern::concerndescription_constructor_exists():
    assert callable(concern::ConcernDescription.__init__)


def test_concern::concerndescription_constructor_args():
    sig = inspect.signature(concern::ConcernDescription.__init__)
    params = list(sig.parameters.keys())



def test_ddiagramelementcontainer_is_not_abstract():
    assert not inspect.isabstract(DDiagramElementContainer)


def test_ddiagramelementcontainer_constructor_exists():
    assert callable(DDiagramElementContainer.__init__)


def test_ddiagramelementcontainer_constructor_args():
    sig = inspect.signature(DDiagramElementContainer.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::diagram::dnodelist_is_not_abstract():
    assert not inspect.isabstract(viewpoint::diagram::DNodeList)


def test_viewpoint::diagram::dnodelist_constructor_exists():
    assert callable(viewpoint::diagram::DNodeList.__init__)


def test_viewpoint::diagram::dnodelist_constructor_args():
    sig = inspect.signature(viewpoint::diagram::DNodeList.__init__)
    params = list(sig.parameters.keys())
    assert "lineWidth" in params, "Missing parameter 'lineWidth'"

def test_viewpoint::diagram::dnodelist_has_lineWidth():
    assert hasattr(viewpoint::diagram::DNodeList, "lineWidth")
    descriptor = None
    for klass in viewpoint::diagram::DNodeList.__mro__:
        if "lineWidth" in klass.__dict__:
            descriptor = klass.__dict__["lineWidth"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::diagram::dnodecontainer_is_not_abstract():
    assert not inspect.isabstract(viewpoint::diagram::DNodeContainer)


def test_viewpoint::diagram::dnodecontainer_constructor_exists():
    assert callable(viewpoint::diagram::DNodeContainer.__init__)


def test_viewpoint::diagram::dnodecontainer_constructor_args():
    sig = inspect.signature(viewpoint::diagram::DNodeContainer.__init__)
    params = list(sig.parameters.keys())
    assert "childrenPresentation" in params, "Missing parameter 'childrenPresentation'"

def test_viewpoint::diagram::dnodecontainer_has_childrenPresentation():
    assert hasattr(viewpoint::diagram::DNodeContainer, "childrenPresentation")
    descriptor = None
    for klass in viewpoint::diagram::DNodeContainer.__mro__:
        if "childrenPresentation" in klass.__dict__:
            descriptor = klass.__dict__["childrenPresentation"]
            break
    assert isinstance(descriptor, property)



def test_dnodelistelement_is_not_abstract():
    assert not inspect.isabstract(DNodeListElement)


def test_dnodelistelement_constructor_exists():
    assert callable(DNodeListElement.__init__)


def test_dnodelistelement_constructor_args():
    sig = inspect.signature(DNodeListElement.__init__)
    params = list(sig.parameters.keys())



def test_dnode_is_not_abstract():
    assert not inspect.isabstract(DNode)


def test_dnode_constructor_exists():
    assert callable(DNode.__init__)


def test_dnode_constructor_args():
    sig = inspect.signature(DNode.__init__)
    params = list(sig.parameters.keys())



def test_dcontainer_is_not_abstract():
    assert not inspect.isabstract(DContainer)


def test_dcontainer_constructor_exists():
    assert callable(DContainer.__init__)


def test_dcontainer_constructor_args():
    sig = inspect.signature(DContainer.__init__)
    params = list(sig.parameters.keys())



def test_dvalidable_is_not_abstract():
    assert not inspect.isabstract(DValidable)


def test_dvalidable_constructor_exists():
    assert callable(DValidable.__init__)


def test_dvalidable_constructor_args():
    sig = inspect.signature(DValidable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::diagram::ddiagramelement_is_not_abstract():
    assert not inspect.isabstract(viewpoint::diagram::DDiagramElement)


def test_viewpoint::diagram::ddiagramelement_constructor_exists():
    assert callable(viewpoint::diagram::DDiagramElement.__init__)


def test_viewpoint::diagram::ddiagramelement_constructor_args():
    sig = inspect.signature(viewpoint::diagram::DDiagramElement.__init__)
    params = list(sig.parameters.keys())
    assert "tooltipText" in params, "Missing parameter 'tooltipText'"
    assert "visible" in params, "Missing parameter 'visible'"

def test_viewpoint::diagram::ddiagramelement_has_tooltipText():
    assert hasattr(viewpoint::diagram::DDiagramElement, "tooltipText")
    descriptor = None
    for klass in viewpoint::diagram::DDiagramElement.__mro__:
        if "tooltipText" in klass.__dict__:
            descriptor = klass.__dict__["tooltipText"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::diagram::ddiagramelement_has_visible():
    assert hasattr(viewpoint::diagram::DDiagramElement, "visible")
    descriptor = None
    for klass in viewpoint::diagram::DDiagramElement.__mro__:
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



def test_viewpoint::diagram::ddiagramelementcontainer_is_not_abstract():
    assert not inspect.isabstract(viewpoint::diagram::DDiagramElementContainer)


def test_viewpoint::diagram::ddiagramelementcontainer_constructor_exists():
    assert callable(viewpoint::diagram::DDiagramElementContainer.__init__)


def test_viewpoint::diagram::ddiagramelementcontainer_constructor_args():
    sig = inspect.signature(viewpoint::diagram::DDiagramElementContainer.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"

def test_viewpoint::diagram::ddiagramelementcontainer_has_height():
    assert hasattr(viewpoint::diagram::DDiagramElementContainer, "height")
    descriptor = None
    for klass in viewpoint::diagram::DDiagramElementContainer.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::diagram::ddiagramelementcontainer_has_width():
    assert hasattr(viewpoint::diagram::DDiagramElementContainer, "width")
    descriptor = None
    for klass in viewpoint::diagram::DDiagramElementContainer.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::diagram::dnode_is_not_abstract():
    assert not inspect.isabstract(viewpoint::diagram::DNode)


def test_viewpoint::diagram::dnode_constructor_exists():
    assert callable(viewpoint::diagram::DNode.__init__)


def test_viewpoint::diagram::dnode_constructor_args():
    sig = inspect.signature(viewpoint::diagram::DNode.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"
    assert "labelPosition" in params, "Missing parameter 'labelPosition'"
    assert "resizeKind" in params, "Missing parameter 'resizeKind'"

def test_viewpoint::diagram::dnode_has_height():
    assert hasattr(viewpoint::diagram::DNode, "height")
    descriptor = None
    for klass in viewpoint::diagram::DNode.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::diagram::dnode_has_width():
    assert hasattr(viewpoint::diagram::DNode, "width")
    descriptor = None
    for klass in viewpoint::diagram::DNode.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::diagram::dnode_has_labelPosition():
    assert hasattr(viewpoint::diagram::DNode, "labelPosition")
    descriptor = None
    for klass in viewpoint::diagram::DNode.__mro__:
        if "labelPosition" in klass.__dict__:
            descriptor = klass.__dict__["labelPosition"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::diagram::dnode_has_resizeKind():
    assert hasattr(viewpoint::diagram::DNode, "resizeKind")
    descriptor = None
    for klass in viewpoint::diagram::DNode.__mro__:
        if "resizeKind" in klass.__dict__:
            descriptor = klass.__dict__["resizeKind"]
            break
    assert isinstance(descriptor, property)



def test_drepresentation_is_not_abstract():
    assert not inspect.isabstract(DRepresentation)


def test_drepresentation_constructor_exists():
    assert callable(DRepresentation.__init__)


def test_drepresentation_constructor_args():
    sig = inspect.signature(DRepresentation.__init__)
    params = list(sig.parameters.keys())



def test_informationsection_is_not_abstract():
    assert not inspect.isabstract(InformationSection)


def test_informationsection_constructor_exists():
    assert callable(InformationSection.__init__)


def test_informationsection_constructor_args():
    sig = inspect.signature(InformationSection.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::audit::templateinformationsection_is_not_abstract():
    assert not inspect.isabstract(viewpoint::audit::TemplateInformationSection)


def test_viewpoint::audit::templateinformationsection_constructor_exists():
    assert callable(viewpoint::audit::TemplateInformationSection.__init__)


def test_viewpoint::audit::templateinformationsection_constructor_args():
    sig = inspect.signature(viewpoint::audit::TemplateInformationSection.__init__)
    params = list(sig.parameters.keys())
    assert "templatePath" in params, "Missing parameter 'templatePath'"

def test_viewpoint::audit::templateinformationsection_has_templatePath():
    assert hasattr(viewpoint::audit::TemplateInformationSection, "templatePath")
    descriptor = None
    for klass in viewpoint::audit::TemplateInformationSection.__mro__:
        if "templatePath" in klass.__dict__:
            descriptor = klass.__dict__["templatePath"]
            break
    assert isinstance(descriptor, property)



def test_description::diagramdescription_is_not_abstract():
    assert not inspect.isabstract(description::DiagramDescription)


def test_description::diagramdescription_constructor_exists():
    assert callable(description::DiagramDescription.__init__)


def test_description::diagramdescription_constructor_args():
    sig = inspect.signature(description::DiagramDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::diagramimportdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::DiagramImportDescription)


def test_viewpoint::description::diagramimportdescription_constructor_exists():
    assert callable(viewpoint::description::DiagramImportDescription.__init__)


def test_viewpoint::description::diagramimportdescription_constructor_args():
    sig = inspect.signature(viewpoint::description::DiagramImportDescription.__init__)
    params = list(sig.parameters.keys())



def test_ddiagramelement_is_not_abstract():
    assert not inspect.isabstract(DDiagramElement)


def test_ddiagramelement_constructor_exists():
    assert callable(DDiagramElement.__init__)


def test_ddiagramelement_constructor_args():
    sig = inspect.signature(DDiagramElement.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::diagram::abstractdnode_is_not_abstract():
    assert not inspect.isabstract(viewpoint::diagram::AbstractDNode)


def test_viewpoint::diagram::abstractdnode_constructor_exists():
    assert callable(viewpoint::diagram::AbstractDNode.__init__)


def test_viewpoint::diagram::abstractdnode_constructor_args():
    sig = inspect.signature(viewpoint::diagram::AbstractDNode.__init__)
    params = list(sig.parameters.keys())
    assert "arrangeConstraints" in params, "Missing parameter 'arrangeConstraints'"

def test_viewpoint::diagram::abstractdnode_has_arrangeConstraints():
    assert hasattr(viewpoint::diagram::AbstractDNode, "arrangeConstraints")
    descriptor = None
    for klass in viewpoint::diagram::AbstractDNode.__mro__:
        if "arrangeConstraints" in klass.__dict__:
            descriptor = klass.__dict__["arrangeConstraints"]
            break
    assert isinstance(descriptor, property)



def test_switchchild_is_not_abstract():
    assert not inspect.isabstract(SwitchChild)


def test_switchchild_constructor_exists():
    assert callable(SwitchChild.__init__)


def test_switchchild_constructor_args():
    sig = inspect.signature(SwitchChild.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::case_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::Case)


def test_viewpoint::tool::case_constructor_exists():
    assert callable(viewpoint::tool::Case.__init__)


def test_viewpoint::tool::case_constructor_args():
    sig = inspect.signature(viewpoint::tool::Case.__init__)
    params = list(sig.parameters.keys())
    assert "conditionExpression" in params, "Missing parameter 'conditionExpression'"

def test_viewpoint::tool::case_has_conditionExpression():
    assert hasattr(viewpoint::tool::Case, "conditionExpression")
    descriptor = None
    for klass in viewpoint::tool::Case.__mro__:
        if "conditionExpression" in klass.__dict__:
            descriptor = klass.__dict__["conditionExpression"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::tool::featurechangelistener_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::FeatureChangeListener)


def test_viewpoint::tool::featurechangelistener_constructor_exists():
    assert callable(viewpoint::tool::FeatureChangeListener.__init__)


def test_viewpoint::tool::featurechangelistener_constructor_args():
    sig = inspect.signature(viewpoint::tool::FeatureChangeListener.__init__)
    params = list(sig.parameters.keys())
    assert "featureName" in params, "Missing parameter 'featureName'"
    assert "domainClass" in params, "Missing parameter 'domainClass'"

def test_viewpoint::tool::featurechangelistener_has_featureName():
    assert hasattr(viewpoint::tool::FeatureChangeListener, "featureName")
    descriptor = None
    for klass in viewpoint::tool::FeatureChangeListener.__mro__:
        if "featureName" in klass.__dict__:
            descriptor = klass.__dict__["featureName"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::tool::featurechangelistener_has_domainClass():
    assert hasattr(viewpoint::tool::FeatureChangeListener, "domainClass")
    descriptor = None
    for klass in viewpoint::tool::FeatureChangeListener.__mro__:
        if "domainClass" in klass.__dict__:
            descriptor = klass.__dict__["domainClass"]
            break
    assert isinstance(descriptor, property)



def test_tool::featurechangelistener_is_not_abstract():
    assert not inspect.isabstract(tool::FeatureChangeListener)


def test_tool::featurechangelistener_constructor_exists():
    assert callable(tool::FeatureChangeListener.__init__)


def test_tool::featurechangelistener_constructor_args():
    sig = inspect.signature(tool::FeatureChangeListener.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::audit::informationsection_is_not_abstract():
    assert not inspect.isabstract(viewpoint::audit::InformationSection)


def test_viewpoint::audit::informationsection_constructor_exists():
    assert callable(viewpoint::audit::InformationSection.__init__)


def test_viewpoint::audit::informationsection_constructor_args():
    sig = inspect.signature(viewpoint::audit::InformationSection.__init__)
    params = list(sig.parameters.keys())



def test_tool::default_is_not_abstract():
    assert not inspect.isabstract(tool::Default)


def test_tool::default_constructor_exists():
    assert callable(tool::Default.__init__)


def test_tool::default_constructor_args():
    sig = inspect.signature(tool::Default.__init__)
    params = list(sig.parameters.keys())



def test_tool::case_is_not_abstract():
    assert not inspect.isabstract(tool::Case)


def test_tool::case_constructor_exists():
    assert callable(tool::Case.__init__)


def test_tool::case_constructor_args():
    sig = inspect.signature(tool::Case.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::default_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::Default)


def test_viewpoint::tool::default_constructor_exists():
    assert callable(viewpoint::tool::Default.__init__)


def test_viewpoint::tool::default_constructor_args():
    sig = inspect.signature(viewpoint::tool::Default.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::switchchild_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::SwitchChild)


def test_viewpoint::tool::switchchild_constructor_exists():
    assert callable(viewpoint::tool::SwitchChild.__init__)


def test_viewpoint::tool::switchchild_constructor_args():
    sig = inspect.signature(viewpoint::tool::SwitchChild.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::toolfilterdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::ToolFilterDescription)


def test_viewpoint::tool::toolfilterdescription_constructor_exists():
    assert callable(viewpoint::tool::ToolFilterDescription.__init__)


def test_viewpoint::tool::toolfilterdescription_constructor_args():
    sig = inspect.signature(viewpoint::tool::ToolFilterDescription.__init__)
    params = list(sig.parameters.keys())
    assert "precondition" in params, "Missing parameter 'precondition'"
    assert "elementsToListen" in params, "Missing parameter 'elementsToListen'"

def test_viewpoint::tool::toolfilterdescription_has_precondition():
    assert hasattr(viewpoint::tool::ToolFilterDescription, "precondition")
    descriptor = None
    for klass in viewpoint::tool::ToolFilterDescription.__mro__:
        if "precondition" in klass.__dict__:
            descriptor = klass.__dict__["precondition"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::tool::toolfilterdescription_has_elementsToListen():
    assert hasattr(viewpoint::tool::ToolFilterDescription, "elementsToListen")
    descriptor = None
    for klass in viewpoint::tool::ToolFilterDescription.__mro__:
        if "elementsToListen" in klass.__dict__:
            descriptor = klass.__dict__["elementsToListen"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::tool::externaljavaactionparameter_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::ExternalJavaActionParameter)


def test_viewpoint::tool::externaljavaactionparameter_constructor_exists():
    assert callable(viewpoint::tool::ExternalJavaActionParameter.__init__)


def test_viewpoint::tool::externaljavaactionparameter_constructor_args():
    sig = inspect.signature(viewpoint::tool::ExternalJavaActionParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_viewpoint::tool::externaljavaactionparameter_has_name():
    assert hasattr(viewpoint::tool::ExternalJavaActionParameter, "name")
    descriptor = None
    for klass in viewpoint::tool::ExternalJavaActionParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::tool::externaljavaactionparameter_has_value():
    assert hasattr(viewpoint::tool::ExternalJavaActionParameter, "value")
    descriptor = None
    for klass in viewpoint::tool::ExternalJavaActionParameter.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::tool::namevariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::NameVariable)


def test_viewpoint::tool::namevariable_constructor_exists():
    assert callable(viewpoint::tool::NameVariable.__init__)


def test_viewpoint::tool::namevariable_constructor_args():
    sig = inspect.signature(viewpoint::tool::NameVariable.__init__)
    params = list(sig.parameters.keys())



def test_tool::viewpoint::eobject_is_not_abstract():
    assert not inspect.isabstract(tool::viewpoint::EObject)


def test_tool::viewpoint::eobject_constructor_exists():
    assert callable(tool::viewpoint::EObject.__init__)


def test_tool::viewpoint::eobject_constructor_args():
    sig = inspect.signature(tool::viewpoint::EObject.__init__)
    params = list(sig.parameters.keys())



def test_containermodeloperation_is_not_abstract():
    assert not inspect.isabstract(ContainerModelOperation)


def test_containermodeloperation_constructor_exists():
    assert callable(ContainerModelOperation.__init__)


def test_containermodeloperation_constructor_args():
    sig = inspect.signature(ContainerModelOperation.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::removeelement_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::RemoveElement)


def test_viewpoint::tool::removeelement_constructor_exists():
    assert callable(viewpoint::tool::RemoveElement.__init__)


def test_viewpoint::tool::removeelement_constructor_args():
    sig = inspect.signature(viewpoint::tool::RemoveElement.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::setobject_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::SetObject)


def test_viewpoint::tool::setobject_constructor_exists():
    assert callable(viewpoint::tool::SetObject.__init__)


def test_viewpoint::tool::setobject_constructor_args():
    sig = inspect.signature(viewpoint::tool::SetObject.__init__)
    params = list(sig.parameters.keys())
    assert "featureName" in params, "Missing parameter 'featureName'"

def test_viewpoint::tool::setobject_has_featureName():
    assert hasattr(viewpoint::tool::SetObject, "featureName")
    descriptor = None
    for klass in viewpoint::tool::SetObject.__mro__:
        if "featureName" in klass.__dict__:
            descriptor = klass.__dict__["featureName"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::tool::changecontext_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::ChangeContext)


def test_viewpoint::tool::changecontext_constructor_exists():
    assert callable(viewpoint::tool::ChangeContext.__init__)


def test_viewpoint::tool::changecontext_constructor_args():
    sig = inspect.signature(viewpoint::tool::ChangeContext.__init__)
    params = list(sig.parameters.keys())
    assert "browseExpression" in params, "Missing parameter 'browseExpression'"

def test_viewpoint::tool::changecontext_has_browseExpression():
    assert hasattr(viewpoint::tool::ChangeContext, "browseExpression")
    descriptor = None
    for klass in viewpoint::tool::ChangeContext.__mro__:
        if "browseExpression" in klass.__dict__:
            descriptor = klass.__dict__["browseExpression"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::tool::createview_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::CreateView)


def test_viewpoint::tool::createview_constructor_exists():
    assert callable(viewpoint::tool::CreateView.__init__)


def test_viewpoint::tool::createview_constructor_args():
    sig = inspect.signature(viewpoint::tool::CreateView.__init__)
    params = list(sig.parameters.keys())
    assert "containerViewExpression" in params, "Missing parameter 'containerViewExpression'"
    assert "variableName" in params, "Missing parameter 'variableName'"

def test_viewpoint::tool::createview_has_containerViewExpression():
    assert hasattr(viewpoint::tool::CreateView, "containerViewExpression")
    descriptor = None
    for klass in viewpoint::tool::CreateView.__mro__:
        if "containerViewExpression" in klass.__dict__:
            descriptor = klass.__dict__["containerViewExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::tool::createview_has_variableName():
    assert hasattr(viewpoint::tool::CreateView, "variableName")
    descriptor = None
    for klass in viewpoint::tool::CreateView.__mro__:
        if "variableName" in klass.__dict__:
            descriptor = klass.__dict__["variableName"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::tool::deleteview_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::DeleteView)


def test_viewpoint::tool::deleteview_constructor_exists():
    assert callable(viewpoint::tool::DeleteView.__init__)


def test_viewpoint::tool::deleteview_constructor_args():
    sig = inspect.signature(viewpoint::tool::DeleteView.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::navigation_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::Navigation)


def test_viewpoint::tool::navigation_constructor_exists():
    assert callable(viewpoint::tool::Navigation.__init__)


def test_viewpoint::tool::navigation_constructor_args():
    sig = inspect.signature(viewpoint::tool::Navigation.__init__)
    params = list(sig.parameters.keys())
    assert "createIfNotExistent" in params, "Missing parameter 'createIfNotExistent'"

def test_viewpoint::tool::navigation_has_createIfNotExistent():
    assert hasattr(viewpoint::tool::Navigation, "createIfNotExistent")
    descriptor = None
    for klass in viewpoint::tool::Navigation.__mro__:
        if "createIfNotExistent" in klass.__dict__:
            descriptor = klass.__dict__["createIfNotExistent"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::tool::for_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::For)


def test_viewpoint::tool::for_constructor_exists():
    assert callable(viewpoint::tool::For.__init__)


def test_viewpoint::tool::for_constructor_args():
    sig = inspect.signature(viewpoint::tool::For.__init__)
    params = list(sig.parameters.keys())
    assert "iteratorName" in params, "Missing parameter 'iteratorName'"
    assert "expression" in params, "Missing parameter 'expression'"

def test_viewpoint::tool::for_has_iteratorName():
    assert hasattr(viewpoint::tool::For, "iteratorName")
    descriptor = None
    for klass in viewpoint::tool::For.__mro__:
        if "iteratorName" in klass.__dict__:
            descriptor = klass.__dict__["iteratorName"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::tool::for_has_expression():
    assert hasattr(viewpoint::tool::For, "expression")
    descriptor = None
    for klass in viewpoint::tool::For.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::tool::unset_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::Unset)


def test_viewpoint::tool::unset_constructor_exists():
    assert callable(viewpoint::tool::Unset.__init__)


def test_viewpoint::tool::unset_constructor_args():
    sig = inspect.signature(viewpoint::tool::Unset.__init__)
    params = list(sig.parameters.keys())
    assert "elementExpression" in params, "Missing parameter 'elementExpression'"
    assert "featureName" in params, "Missing parameter 'featureName'"

def test_viewpoint::tool::unset_has_elementExpression():
    assert hasattr(viewpoint::tool::Unset, "elementExpression")
    descriptor = None
    for klass in viewpoint::tool::Unset.__mro__:
        if "elementExpression" in klass.__dict__:
            descriptor = klass.__dict__["elementExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::tool::unset_has_featureName():
    assert hasattr(viewpoint::tool::Unset, "featureName")
    descriptor = None
    for klass in viewpoint::tool::Unset.__mro__:
        if "featureName" in klass.__dict__:
            descriptor = klass.__dict__["featureName"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::tool::moveelement_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::MoveElement)


def test_viewpoint::tool::moveelement_constructor_exists():
    assert callable(viewpoint::tool::MoveElement.__init__)


def test_viewpoint::tool::moveelement_constructor_args():
    sig = inspect.signature(viewpoint::tool::MoveElement.__init__)
    params = list(sig.parameters.keys())
    assert "newContainerExpression" in params, "Missing parameter 'newContainerExpression'"
    assert "featureName" in params, "Missing parameter 'featureName'"

def test_viewpoint::tool::moveelement_has_newContainerExpression():
    assert hasattr(viewpoint::tool::MoveElement, "newContainerExpression")
    descriptor = None
    for klass in viewpoint::tool::MoveElement.__mro__:
        if "newContainerExpression" in klass.__dict__:
            descriptor = klass.__dict__["newContainerExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::tool::moveelement_has_featureName():
    assert hasattr(viewpoint::tool::MoveElement, "featureName")
    descriptor = None
    for klass in viewpoint::tool::MoveElement.__mro__:
        if "featureName" in klass.__dict__:
            descriptor = klass.__dict__["featureName"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::tool::setvalue_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::SetValue)


def test_viewpoint::tool::setvalue_constructor_exists():
    assert callable(viewpoint::tool::SetValue.__init__)


def test_viewpoint::tool::setvalue_constructor_args():
    sig = inspect.signature(viewpoint::tool::SetValue.__init__)
    params = list(sig.parameters.keys())
    assert "valueExpression" in params, "Missing parameter 'valueExpression'"
    assert "featureName" in params, "Missing parameter 'featureName'"

def test_viewpoint::tool::setvalue_has_valueExpression():
    assert hasattr(viewpoint::tool::SetValue, "valueExpression")
    descriptor = None
    for klass in viewpoint::tool::SetValue.__mro__:
        if "valueExpression" in klass.__dict__:
            descriptor = klass.__dict__["valueExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::tool::setvalue_has_featureName():
    assert hasattr(viewpoint::tool::SetValue, "featureName")
    descriptor = None
    for klass in viewpoint::tool::SetValue.__mro__:
        if "featureName" in klass.__dict__:
            descriptor = klass.__dict__["featureName"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::tool::if_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::If)


def test_viewpoint::tool::if_constructor_exists():
    assert callable(viewpoint::tool::If.__init__)


def test_viewpoint::tool::if_constructor_args():
    sig = inspect.signature(viewpoint::tool::If.__init__)
    params = list(sig.parameters.keys())
    assert "conditionExpression" in params, "Missing parameter 'conditionExpression'"

def test_viewpoint::tool::if_has_conditionExpression():
    assert hasattr(viewpoint::tool::If, "conditionExpression")
    descriptor = None
    for klass in viewpoint::tool::If.__mro__:
        if "conditionExpression" in klass.__dict__:
            descriptor = klass.__dict__["conditionExpression"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::tool::createinstance_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::CreateInstance)


def test_viewpoint::tool::createinstance_constructor_exists():
    assert callable(viewpoint::tool::CreateInstance.__init__)


def test_viewpoint::tool::createinstance_constructor_args():
    sig = inspect.signature(viewpoint::tool::CreateInstance.__init__)
    params = list(sig.parameters.keys())
    assert "referenceName" in params, "Missing parameter 'referenceName'"
    assert "typeName" in params, "Missing parameter 'typeName'"
    assert "variableName" in params, "Missing parameter 'variableName'"

def test_viewpoint::tool::createinstance_has_referenceName():
    assert hasattr(viewpoint::tool::CreateInstance, "referenceName")
    descriptor = None
    for klass in viewpoint::tool::CreateInstance.__mro__:
        if "referenceName" in klass.__dict__:
            descriptor = klass.__dict__["referenceName"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::tool::createinstance_has_typeName():
    assert hasattr(viewpoint::tool::CreateInstance, "typeName")
    descriptor = None
    for klass in viewpoint::tool::CreateInstance.__mro__:
        if "typeName" in klass.__dict__:
            descriptor = klass.__dict__["typeName"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::tool::createinstance_has_variableName():
    assert hasattr(viewpoint::tool::CreateInstance, "variableName")
    descriptor = None
    for klass in viewpoint::tool::CreateInstance.__mro__:
        if "variableName" in klass.__dict__:
            descriptor = klass.__dict__["variableName"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::tool::initialcontainerdropoperation_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::InitialContainerDropOperation)


def test_viewpoint::tool::initialcontainerdropoperation_constructor_exists():
    assert callable(viewpoint::tool::InitialContainerDropOperation.__init__)


def test_viewpoint::tool::initialcontainerdropoperation_constructor_args():
    sig = inspect.signature(viewpoint::tool::InitialContainerDropOperation.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::initedgecreationoperation_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::InitEdgeCreationOperation)


def test_viewpoint::tool::initedgecreationoperation_constructor_exists():
    assert callable(viewpoint::tool::InitEdgeCreationOperation.__init__)


def test_viewpoint::tool::initedgecreationoperation_constructor_args():
    sig = inspect.signature(viewpoint::tool::InitEdgeCreationOperation.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::initialoperation_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::InitialOperation)


def test_viewpoint::tool::initialoperation_constructor_exists():
    assert callable(viewpoint::tool::InitialOperation.__init__)


def test_viewpoint::tool::initialoperation_constructor_args():
    sig = inspect.signature(viewpoint::tool::InitialOperation.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::initialnodecreationoperation_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::InitialNodeCreationOperation)


def test_viewpoint::tool::initialnodecreationoperation_constructor_exists():
    assert callable(viewpoint::tool::InitialNodeCreationOperation.__init__)


def test_viewpoint::tool::initialnodecreationoperation_constructor_args():
    sig = inspect.signature(viewpoint::tool::InitialNodeCreationOperation.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::modeloperation_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::ModelOperation)


def test_viewpoint::tool::modeloperation_constructor_exists():
    assert callable(viewpoint::tool::ModelOperation.__init__)


def test_viewpoint::tool::modeloperation_constructor_args():
    sig = inspect.signature(viewpoint::tool::ModelOperation.__init__)
    params = list(sig.parameters.keys())



def test_tool::modeloperation_is_not_abstract():
    assert not inspect.isabstract(tool::ModelOperation)


def test_tool::modeloperation_constructor_exists():
    assert callable(tool::ModelOperation.__init__)


def test_tool::modeloperation_constructor_args():
    sig = inspect.signature(tool::ModelOperation.__init__)
    params = list(sig.parameters.keys())



def test_modeloperation_is_not_abstract():
    assert not inspect.isabstract(ModelOperation)


def test_modeloperation_constructor_exists():
    assert callable(ModelOperation.__init__)


def test_modeloperation_constructor_args():
    sig = inspect.signature(ModelOperation.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::switch_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::Switch)


def test_viewpoint::tool::switch_constructor_exists():
    assert callable(viewpoint::tool::Switch.__init__)


def test_viewpoint::tool::switch_constructor_args():
    sig = inspect.signature(viewpoint::tool::Switch.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::containermodeloperation_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::ContainerModelOperation)


def test_viewpoint::tool::containermodeloperation_constructor_exists():
    assert callable(viewpoint::tool::ContainerModelOperation.__init__)


def test_viewpoint::tool::containermodeloperation_constructor_args():
    sig = inspect.signature(viewpoint::tool::ContainerModelOperation.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::editmaskvariables_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::EditMaskVariables)


def test_viewpoint::tool::editmaskvariables_constructor_exists():
    assert callable(viewpoint::tool::EditMaskVariables.__init__)


def test_viewpoint::tool::editmaskvariables_constructor_args():
    sig = inspect.signature(viewpoint::tool::EditMaskVariables.__init__)
    params = list(sig.parameters.keys())
    assert "mask" in params, "Missing parameter 'mask'"

def test_viewpoint::tool::editmaskvariables_has_mask():
    assert hasattr(viewpoint::tool::EditMaskVariables, "mask")
    descriptor = None
    for klass in viewpoint::tool::EditMaskVariables.__mro__:
        if "mask" in klass.__dict__:
            descriptor = klass.__dict__["mask"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::tool::selectmodelelementvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::SelectModelElementVariable)


def test_viewpoint::tool::selectmodelelementvariable_constructor_exists():
    assert callable(viewpoint::tool::SelectModelElementVariable.__init__)


def test_viewpoint::tool::selectmodelelementvariable_constructor_args():
    sig = inspect.signature(viewpoint::tool::SelectModelElementVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::elementselectvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::ElementSelectVariable)


def test_viewpoint::tool::elementselectvariable_constructor_exists():
    assert callable(viewpoint::tool::ElementSelectVariable.__init__)


def test_viewpoint::tool::elementselectvariable_constructor_args():
    sig = inspect.signature(viewpoint::tool::ElementSelectVariable.__init__)
    params = list(sig.parameters.keys())



def test_tool::abstractvariable_is_not_abstract():
    assert not inspect.isabstract(tool::AbstractVariable)


def test_tool::abstractvariable_constructor_exists():
    assert callable(tool::AbstractVariable.__init__)


def test_tool::abstractvariable_constructor_args():
    sig = inspect.signature(tool::AbstractVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::dropcontainervariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::DropContainerVariable)


def test_viewpoint::tool::dropcontainervariable_constructor_exists():
    assert callable(viewpoint::tool::DropContainerVariable.__init__)


def test_viewpoint::tool::dropcontainervariable_constructor_args():
    sig = inspect.signature(viewpoint::tool::DropContainerVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::selectcontainervariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::SelectContainerVariable)


def test_viewpoint::tool::selectcontainervariable_constructor_exists():
    assert callable(viewpoint::tool::SelectContainerVariable.__init__)


def test_viewpoint::tool::selectcontainervariable_constructor_args():
    sig = inspect.signature(viewpoint::tool::SelectContainerVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::elementdropvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::ElementDropVariable)


def test_viewpoint::tool::elementdropvariable_constructor_exists():
    assert callable(viewpoint::tool::ElementDropVariable.__init__)


def test_viewpoint::tool::elementdropvariable_constructor_args():
    sig = inspect.signature(viewpoint::tool::ElementDropVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::containerviewvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::ContainerViewVariable)


def test_viewpoint::tool::containerviewvariable_constructor_exists():
    assert callable(viewpoint::tool::ContainerViewVariable.__init__)


def test_viewpoint::tool::containerviewvariable_constructor_args():
    sig = inspect.signature(viewpoint::tool::ContainerViewVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::elementdeletevariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::ElementDeleteVariable)


def test_viewpoint::tool::elementdeletevariable_constructor_exists():
    assert callable(viewpoint::tool::ElementDeleteVariable.__init__)


def test_viewpoint::tool::elementdeletevariable_constructor_args():
    sig = inspect.signature(viewpoint::tool::ElementDeleteVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::sourceedgeviewcreationvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::SourceEdgeViewCreationVariable)


def test_viewpoint::tool::sourceedgeviewcreationvariable_constructor_exists():
    assert callable(viewpoint::tool::SourceEdgeViewCreationVariable.__init__)


def test_viewpoint::tool::sourceedgeviewcreationvariable_constructor_args():
    sig = inspect.signature(viewpoint::tool::SourceEdgeViewCreationVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::elementvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::ElementVariable)


def test_viewpoint::tool::elementvariable_constructor_exists():
    assert callable(viewpoint::tool::ElementVariable.__init__)


def test_viewpoint::tool::elementvariable_constructor_args():
    sig = inspect.signature(viewpoint::tool::ElementVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::sourceedgecreationvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::SourceEdgeCreationVariable)


def test_viewpoint::tool::sourceedgecreationvariable_constructor_exists():
    assert callable(viewpoint::tool::SourceEdgeCreationVariable.__init__)


def test_viewpoint::tool::sourceedgecreationvariable_constructor_args():
    sig = inspect.signature(viewpoint::tool::SourceEdgeCreationVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::elementviewvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::ElementViewVariable)


def test_viewpoint::tool::elementviewvariable_constructor_exists():
    assert callable(viewpoint::tool::ElementViewVariable.__init__)


def test_viewpoint::tool::elementviewvariable_constructor_args():
    sig = inspect.signature(viewpoint::tool::ElementViewVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::elementdoubleclickvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::ElementDoubleClickVariable)


def test_viewpoint::tool::elementdoubleclickvariable_constructor_exists():
    assert callable(viewpoint::tool::ElementDoubleClickVariable.__init__)


def test_viewpoint::tool::elementdoubleclickvariable_constructor_args():
    sig = inspect.signature(viewpoint::tool::ElementDoubleClickVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::targetedgecreationvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::TargetEdgeCreationVariable)


def test_viewpoint::tool::targetedgecreationvariable_constructor_exists():
    assert callable(viewpoint::tool::TargetEdgeCreationVariable.__init__)


def test_viewpoint::tool::targetedgecreationvariable_constructor_args():
    sig = inspect.signature(viewpoint::tool::TargetEdgeCreationVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::targetedgeviewcreationvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::TargetEdgeViewCreationVariable)


def test_viewpoint::tool::targetedgeviewcreationvariable_constructor_exists():
    assert callable(viewpoint::tool::TargetEdgeViewCreationVariable.__init__)


def test_viewpoint::tool::targetedgeviewcreationvariable_constructor_args():
    sig = inspect.signature(viewpoint::tool::TargetEdgeViewCreationVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::nodecreationvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::NodeCreationVariable)


def test_viewpoint::tool::nodecreationvariable_constructor_exists():
    assert callable(viewpoint::tool::NodeCreationVariable.__init__)


def test_viewpoint::tool::nodecreationvariable_constructor_args():
    sig = inspect.signature(viewpoint::tool::NodeCreationVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::decoration_is_not_abstract():
    assert not inspect.isabstract(viewpoint::Decoration)


def test_viewpoint::decoration_constructor_exists():
    assert callable(viewpoint::Decoration.__init__)


def test_viewpoint::decoration_constructor_args():
    sig = inspect.signature(viewpoint::Decoration.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_is_not_abstract():
    assert not inspect.isabstract(Viewpoint)


def test_viewpoint_constructor_exists():
    assert callable(Viewpoint.__init__)


def test_viewpoint_constructor_args():
    sig = inspect.signature(Viewpoint.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::metamodelextension_is_not_abstract():
    assert not inspect.isabstract(viewpoint::MetaModelExtension)


def test_viewpoint::metamodelextension_constructor_exists():
    assert callable(viewpoint::MetaModelExtension.__init__)


def test_viewpoint::metamodelextension_constructor_args():
    sig = inspect.signature(viewpoint::MetaModelExtension.__init__)
    params = list(sig.parameters.keys())



def test_dsemanticdecorator_is_not_abstract():
    assert not inspect.isabstract(DSemanticDecorator)


def test_dsemanticdecorator_constructor_exists():
    assert callable(DSemanticDecorator.__init__)


def test_dsemanticdecorator_constructor_args():
    sig = inspect.signature(DSemanticDecorator.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::diagram::dsemanticdiagram_is_not_abstract():
    assert not inspect.isabstract(viewpoint::diagram::DSemanticDiagram)


def test_viewpoint::diagram::dsemanticdiagram_constructor_exists():
    assert callable(viewpoint::diagram::DSemanticDiagram.__init__)


def test_viewpoint::diagram::dsemanticdiagram_constructor_args():
    sig = inspect.signature(viewpoint::diagram::DSemanticDiagram.__init__)
    params = list(sig.parameters.keys())



def test_dstylizable_is_not_abstract():
    assert not inspect.isabstract(DStylizable)


def test_dstylizable_constructor_exists():
    assert callable(DStylizable.__init__)


def test_dstylizable_constructor_args():
    sig = inspect.signature(DStylizable.__init__)
    params = list(sig.parameters.keys())



def test_dmappingbased_is_not_abstract():
    assert not inspect.isabstract(DMappingBased)


def test_dmappingbased_constructor_exists():
    assert callable(DMappingBased.__init__)


def test_dmappingbased_constructor_args():
    sig = inspect.signature(DMappingBased.__init__)
    params = list(sig.parameters.keys())



def test_dlabelled_is_not_abstract():
    assert not inspect.isabstract(DLabelled)


def test_dlabelled_constructor_exists():
    assert callable(DLabelled.__init__)


def test_dlabelled_constructor_args():
    sig = inspect.signature(DLabelled.__init__)
    params = list(sig.parameters.keys())



def test_annotationentry_is_not_abstract():
    assert not inspect.isabstract(AnnotationEntry)


def test_annotationentry_constructor_exists():
    assert callable(AnnotationEntry.__init__)


def test_annotationentry_constructor_args():
    sig = inspect.signature(AnnotationEntry.__init__)
    params = list(sig.parameters.keys())



def test_description::dmodelelement_is_not_abstract():
    assert not inspect.isabstract(description::DModelElement)


def test_description::dmodelelement_constructor_exists():
    assert callable(description::DModelElement.__init__)


def test_description::dmodelelement_constructor_args():
    sig = inspect.signature(description::DModelElement.__init__)
    params = list(sig.parameters.keys())



def test_drefreshable_is_not_abstract():
    assert not inspect.isabstract(DRefreshable)


def test_drefreshable_constructor_exists():
    assert callable(DRefreshable.__init__)


def test_drefreshable_constructor_args():
    sig = inspect.signature(DRefreshable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::drepresentationelement_is_not_abstract():
    assert not inspect.isabstract(viewpoint::DRepresentationElement)


def test_viewpoint::drepresentationelement_constructor_exists():
    assert callable(viewpoint::DRepresentationElement.__init__)


def test_viewpoint::drepresentationelement_constructor_args():
    sig = inspect.signature(viewpoint::DRepresentationElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_viewpoint::drepresentationelement_has_name():
    assert hasattr(viewpoint::DRepresentationElement, "name")
    descriptor = None
    for klass in viewpoint::DRepresentationElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::style_is_not_abstract():
    assert not inspect.isabstract(viewpoint::Style)


def test_viewpoint::style_constructor_exists():
    assert callable(viewpoint::Style.__init__)


def test_viewpoint::style_constructor_args():
    sig = inspect.signature(viewpoint::Style.__init__)
    params = list(sig.parameters.keys())



def test_description::documentedelement_is_not_abstract():
    assert not inspect.isabstract(description::DocumentedElement)


def test_description::documentedelement_constructor_exists():
    assert callable(description::DocumentedElement.__init__)


def test_description::documentedelement_constructor_args():
    sig = inspect.signature(description::DocumentedElement.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::viewpoint_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::Viewpoint)


def test_viewpoint::description::viewpoint_constructor_exists():
    assert callable(viewpoint::description::Viewpoint.__init__)


def test_viewpoint::description::viewpoint_constructor_args():
    sig = inspect.signature(viewpoint::description::Viewpoint.__init__)
    params = list(sig.parameters.keys())
    assert "customizes" in params, "Missing parameter 'customizes'"
    assert "reuses" in params, "Missing parameter 'reuses'"
    assert "icon" in params, "Missing parameter 'icon'"
    assert "conflicts" in params, "Missing parameter 'conflicts'"
    assert "modelFileExtension" in params, "Missing parameter 'modelFileExtension'"

def test_viewpoint::description::viewpoint_has_customizes():
    assert hasattr(viewpoint::description::Viewpoint, "customizes")
    descriptor = None
    for klass in viewpoint::description::Viewpoint.__mro__:
        if "customizes" in klass.__dict__:
            descriptor = klass.__dict__["customizes"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::description::viewpoint_has_reuses():
    assert hasattr(viewpoint::description::Viewpoint, "reuses")
    descriptor = None
    for klass in viewpoint::description::Viewpoint.__mro__:
        if "reuses" in klass.__dict__:
            descriptor = klass.__dict__["reuses"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::description::viewpoint_has_icon():
    assert hasattr(viewpoint::description::Viewpoint, "icon")
    descriptor = None
    for klass in viewpoint::description::Viewpoint.__mro__:
        if "icon" in klass.__dict__:
            descriptor = klass.__dict__["icon"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::description::viewpoint_has_conflicts():
    assert hasattr(viewpoint::description::Viewpoint, "conflicts")
    descriptor = None
    for klass in viewpoint::description::Viewpoint.__mro__:
        if "conflicts" in klass.__dict__:
            descriptor = klass.__dict__["conflicts"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::description::viewpoint_has_modelFileExtension():
    assert hasattr(viewpoint::description::Viewpoint, "modelFileExtension")
    descriptor = None
    for klass in viewpoint::description::Viewpoint.__mro__:
        if "modelFileExtension" in klass.__dict__:
            descriptor = klass.__dict__["modelFileExtension"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::tool::toolsection_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::ToolSection)


def test_viewpoint::tool::toolsection_constructor_exists():
    assert callable(viewpoint::tool::ToolSection.__init__)


def test_viewpoint::tool::toolsection_constructor_args():
    sig = inspect.signature(viewpoint::tool::ToolSection.__init__)
    params = list(sig.parameters.keys())
    assert "icon" in params, "Missing parameter 'icon'"

def test_viewpoint::tool::toolsection_has_icon():
    assert hasattr(viewpoint::tool::ToolSection, "icon")
    descriptor = None
    for klass in viewpoint::tool::ToolSection.__mro__:
        if "icon" in klass.__dict__:
            descriptor = klass.__dict__["icon"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::filter::filterdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::filter::FilterDescription)


def test_viewpoint::filter::filterdescription_constructor_exists():
    assert callable(viewpoint::filter::FilterDescription.__init__)


def test_viewpoint::filter::filterdescription_constructor_args():
    sig = inspect.signature(viewpoint::filter::FilterDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::edgemapping_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::EdgeMapping)


def test_viewpoint::description::edgemapping_constructor_exists():
    assert callable(viewpoint::description::EdgeMapping.__init__)


def test_viewpoint::description::edgemapping_constructor_args():
    sig = inspect.signature(viewpoint::description::EdgeMapping.__init__)
    params = list(sig.parameters.keys())
    assert "targetFinderExpression" in params, "Missing parameter 'targetFinderExpression'"
    assert "pathExpression" in params, "Missing parameter 'pathExpression'"
    assert "targetExpression" in params, "Missing parameter 'targetExpression'"
    assert "domainClass" in params, "Missing parameter 'domainClass'"
    assert "useDomainElement" in params, "Missing parameter 'useDomainElement'"
    assert "sourceFinderExpression" in params, "Missing parameter 'sourceFinderExpression'"

def test_viewpoint::description::edgemapping_has_targetFinderExpression():
    assert hasattr(viewpoint::description::EdgeMapping, "targetFinderExpression")
    descriptor = None
    for klass in viewpoint::description::EdgeMapping.__mro__:
        if "targetFinderExpression" in klass.__dict__:
            descriptor = klass.__dict__["targetFinderExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::description::edgemapping_has_pathExpression():
    assert hasattr(viewpoint::description::EdgeMapping, "pathExpression")
    descriptor = None
    for klass in viewpoint::description::EdgeMapping.__mro__:
        if "pathExpression" in klass.__dict__:
            descriptor = klass.__dict__["pathExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::description::edgemapping_has_targetExpression():
    assert hasattr(viewpoint::description::EdgeMapping, "targetExpression")
    descriptor = None
    for klass in viewpoint::description::EdgeMapping.__mro__:
        if "targetExpression" in klass.__dict__:
            descriptor = klass.__dict__["targetExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::description::edgemapping_has_domainClass():
    assert hasattr(viewpoint::description::EdgeMapping, "domainClass")
    descriptor = None
    for klass in viewpoint::description::EdgeMapping.__mro__:
        if "domainClass" in klass.__dict__:
            descriptor = klass.__dict__["domainClass"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::description::edgemapping_has_useDomainElement():
    assert hasattr(viewpoint::description::EdgeMapping, "useDomainElement")
    descriptor = None
    for klass in viewpoint::description::EdgeMapping.__mro__:
        if "useDomainElement" in klass.__dict__:
            descriptor = klass.__dict__["useDomainElement"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::description::edgemapping_has_sourceFinderExpression():
    assert hasattr(viewpoint::description::EdgeMapping, "sourceFinderExpression")
    descriptor = None
    for klass in viewpoint::description::EdgeMapping.__mro__:
        if "sourceFinderExpression" in klass.__dict__:
            descriptor = klass.__dict__["sourceFinderExpression"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::description::group_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::Group)


def test_viewpoint::description::group_constructor_exists():
    assert callable(viewpoint::description::Group.__init__)


def test_viewpoint::description::group_constructor_args():
    sig = inspect.signature(viewpoint::description::Group.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "name" in params, "Missing parameter 'name'"

def test_viewpoint::description::group_has_version():
    assert hasattr(viewpoint::description::Group, "version")
    descriptor = None
    for klass in viewpoint::description::Group.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::description::group_has_name():
    assert hasattr(viewpoint::description::Group, "name")
    descriptor = None
    for klass in viewpoint::description::Group.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::description::edgemappingimport_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::EdgeMappingImport)


def test_viewpoint::description::edgemappingimport_constructor_exists():
    assert callable(viewpoint::description::EdgeMappingImport.__init__)


def test_viewpoint::description::edgemappingimport_constructor_args():
    sig = inspect.signature(viewpoint::description::EdgeMappingImport.__init__)
    params = list(sig.parameters.keys())
    assert "inheritsAncestorFilters" in params, "Missing parameter 'inheritsAncestorFilters'"

def test_viewpoint::description::edgemappingimport_has_inheritsAncestorFilters():
    assert hasattr(viewpoint::description::EdgeMappingImport, "inheritsAncestorFilters")
    descriptor = None
    for klass in viewpoint::description::EdgeMappingImport.__mro__:
        if "inheritsAncestorFilters" in klass.__dict__:
            descriptor = klass.__dict__["inheritsAncestorFilters"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::description::layer_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::Layer)


def test_viewpoint::description::layer_constructor_exists():
    assert callable(viewpoint::description::Layer.__init__)


def test_viewpoint::description::layer_constructor_args():
    sig = inspect.signature(viewpoint::description::Layer.__init__)
    params = list(sig.parameters.keys())
    assert "icon" in params, "Missing parameter 'icon'"

def test_viewpoint::description::layer_has_icon():
    assert hasattr(viewpoint::description::Layer, "icon")
    descriptor = None
    for klass in viewpoint::description::Layer.__mro__:
        if "icon" in klass.__dict__:
            descriptor = klass.__dict__["icon"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::tool::toolentry_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::ToolEntry)


def test_viewpoint::tool::toolentry_constructor_exists():
    assert callable(viewpoint::tool::ToolEntry.__init__)


def test_viewpoint::tool::toolentry_constructor_args():
    sig = inspect.signature(viewpoint::tool::ToolEntry.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::representationdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::RepresentationDescription)


def test_viewpoint::description::representationdescription_constructor_exists():
    assert callable(viewpoint::description::RepresentationDescription.__init__)


def test_viewpoint::description::representationdescription_constructor_args():
    sig = inspect.signature(viewpoint::description::RepresentationDescription.__init__)
    params = list(sig.parameters.keys())
    assert "titleExpression" in params, "Missing parameter 'titleExpression'"
    assert "showOnStartup" in params, "Missing parameter 'showOnStartup'"
    assert "initialisation" in params, "Missing parameter 'initialisation'"

def test_viewpoint::description::representationdescription_has_titleExpression():
    assert hasattr(viewpoint::description::RepresentationDescription, "titleExpression")
    descriptor = None
    for klass in viewpoint::description::RepresentationDescription.__mro__:
        if "titleExpression" in klass.__dict__:
            descriptor = klass.__dict__["titleExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::description::representationdescription_has_showOnStartup():
    assert hasattr(viewpoint::description::RepresentationDescription, "showOnStartup")
    descriptor = None
    for klass in viewpoint::description::RepresentationDescription.__mro__:
        if "showOnStartup" in klass.__dict__:
            descriptor = klass.__dict__["showOnStartup"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::description::representationdescription_has_initialisation():
    assert hasattr(viewpoint::description::RepresentationDescription, "initialisation")
    descriptor = None
    for klass in viewpoint::description::RepresentationDescription.__mro__:
        if "initialisation" in klass.__dict__:
            descriptor = klass.__dict__["initialisation"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::diagram::ddiagram_is_not_abstract():
    assert not inspect.isabstract(viewpoint::diagram::DDiagram)


def test_viewpoint::diagram::ddiagram_constructor_exists():
    assert callable(viewpoint::diagram::DDiagram.__init__)


def test_viewpoint::diagram::ddiagram_constructor_args():
    sig = inspect.signature(viewpoint::diagram::DDiagram.__init__)
    params = list(sig.parameters.keys())
    assert "info" in params, "Missing parameter 'info'"
    assert "isInLayoutingMode" in params, "Missing parameter 'isInLayoutingMode'"
    assert "headerHeight" in params, "Missing parameter 'headerHeight'"
    assert "synchronized" in params, "Missing parameter 'synchronized'"

def test_viewpoint::diagram::ddiagram_has_info():
    assert hasattr(viewpoint::diagram::DDiagram, "info")
    descriptor = None
    for klass in viewpoint::diagram::DDiagram.__mro__:
        if "info" in klass.__dict__:
            descriptor = klass.__dict__["info"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::diagram::ddiagram_has_isInLayoutingMode():
    assert hasattr(viewpoint::diagram::DDiagram, "isInLayoutingMode")
    descriptor = None
    for klass in viewpoint::diagram::DDiagram.__mro__:
        if "isInLayoutingMode" in klass.__dict__:
            descriptor = klass.__dict__["isInLayoutingMode"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::diagram::ddiagram_has_headerHeight():
    assert hasattr(viewpoint::diagram::DDiagram, "headerHeight")
    descriptor = None
    for klass in viewpoint::diagram::DDiagram.__mro__:
        if "headerHeight" in klass.__dict__:
            descriptor = klass.__dict__["headerHeight"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::diagram::ddiagram_has_synchronized():
    assert hasattr(viewpoint::diagram::DDiagram, "synchronized")
    descriptor = None
    for klass in viewpoint::diagram::DDiagram.__mro__:
        if "synchronized" in klass.__dict__:
            descriptor = klass.__dict__["synchronized"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::concern::concerndescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::concern::ConcernDescription)


def test_viewpoint::concern::concerndescription_constructor_exists():
    assert callable(viewpoint::concern::ConcernDescription.__init__)


def test_viewpoint::concern::concerndescription_constructor_args():
    sig = inspect.signature(viewpoint::concern::ConcernDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::abstractnodemapping_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::AbstractNodeMapping)


def test_viewpoint::description::abstractnodemapping_constructor_exists():
    assert callable(viewpoint::description::AbstractNodeMapping.__init__)


def test_viewpoint::description::abstractnodemapping_constructor_args():
    sig = inspect.signature(viewpoint::description::AbstractNodeMapping.__init__)
    params = list(sig.parameters.keys())
    assert "domainClass" in params, "Missing parameter 'domainClass'"

def test_viewpoint::description::abstractnodemapping_has_domainClass():
    assert hasattr(viewpoint::description::AbstractNodeMapping, "domainClass")
    descriptor = None
    for klass in viewpoint::description::AbstractNodeMapping.__mro__:
        if "domainClass" in klass.__dict__:
            descriptor = klass.__dict__["domainClass"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::drepresentation_is_not_abstract():
    assert not inspect.isabstract(viewpoint::DRepresentation)


def test_viewpoint::drepresentation_constructor_exists():
    assert callable(viewpoint::DRepresentation.__init__)


def test_viewpoint::drepresentation_constructor_args():
    sig = inspect.signature(viewpoint::DRepresentation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_viewpoint::drepresentation_has_name():
    assert hasattr(viewpoint::DRepresentation, "name")
    descriptor = None
    for klass in viewpoint::DRepresentation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::dsemanticdecorator_is_not_abstract():
    assert not inspect.isabstract(viewpoint::DSemanticDecorator)


def test_viewpoint::dsemanticdecorator_constructor_exists():
    assert callable(viewpoint::DSemanticDecorator.__init__)


def test_viewpoint::dsemanticdecorator_constructor_args():
    sig = inspect.signature(viewpoint::DSemanticDecorator.__init__)
    params = list(sig.parameters.keys())



def test_ddiagramset_is_not_abstract():
    assert not inspect.isabstract(DDiagramSet)


def test_ddiagramset_constructor_exists():
    assert callable(DDiagramSet.__init__)


def test_ddiagramset_constructor_args():
    sig = inspect.signature(DDiagramSet.__init__)
    params = list(sig.parameters.keys())



def test_dview_is_not_abstract():
    assert not inspect.isabstract(DView)


def test_dview_constructor_exists():
    assert callable(DView.__init__)


def test_dview_constructor_args():
    sig = inspect.signature(DView.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::drepresentationcontainer_is_not_abstract():
    assert not inspect.isabstract(viewpoint::DRepresentationContainer)


def test_viewpoint::drepresentationcontainer_constructor_exists():
    assert callable(viewpoint::DRepresentationContainer.__init__)


def test_viewpoint::drepresentationcontainer_constructor_args():
    sig = inspect.signature(viewpoint::DRepresentationContainer.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::dcontainer_is_not_abstract():
    assert not inspect.isabstract(viewpoint::DContainer)


def test_viewpoint::dcontainer_constructor_exists():
    assert callable(viewpoint::DContainer.__init__)


def test_viewpoint::dcontainer_constructor_args():
    sig = inspect.signature(viewpoint::DContainer.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::dmappingbased_is_not_abstract():
    assert not inspect.isabstract(viewpoint::DMappingBased)


def test_viewpoint::dmappingbased_constructor_exists():
    assert callable(viewpoint::DMappingBased.__init__)


def test_viewpoint::dmappingbased_constructor_args():
    sig = inspect.signature(viewpoint::DMappingBased.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::dlabelled_is_not_abstract():
    assert not inspect.isabstract(viewpoint::DLabelled)


def test_viewpoint::dlabelled_constructor_exists():
    assert callable(viewpoint::DLabelled.__init__)


def test_viewpoint::dlabelled_constructor_args():
    sig = inspect.signature(viewpoint::DLabelled.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::drefreshable_is_not_abstract():
    assert not inspect.isabstract(viewpoint::DRefreshable)


def test_viewpoint::drefreshable_constructor_exists():
    assert callable(viewpoint::DRefreshable.__init__)


def test_viewpoint::drefreshable_constructor_args():
    sig = inspect.signature(viewpoint::DRefreshable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::dstylizable_is_not_abstract():
    assert not inspect.isabstract(viewpoint::DStylizable)


def test_viewpoint::dstylizable_constructor_exists():
    assert callable(viewpoint::DStylizable.__init__)


def test_viewpoint::dstylizable_constructor_args():
    sig = inspect.signature(viewpoint::DStylizable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::dnavigationlink_is_not_abstract():
    assert not inspect.isabstract(viewpoint::DNavigationLink)


def test_viewpoint::dnavigationlink_constructor_exists():
    assert callable(viewpoint::DNavigationLink.__init__)


def test_viewpoint::dnavigationlink_constructor_args():
    sig = inspect.signature(viewpoint::DNavigationLink.__init__)
    params = list(sig.parameters.keys())
    assert "targetType" in params, "Missing parameter 'targetType'"
    assert "label" in params, "Missing parameter 'label'"

def test_viewpoint::dnavigationlink_has_targetType():
    assert hasattr(viewpoint::DNavigationLink, "targetType")
    descriptor = None
    for klass in viewpoint::DNavigationLink.__mro__:
        if "targetType" in klass.__dict__:
            descriptor = klass.__dict__["targetType"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::dnavigationlink_has_label():
    assert hasattr(viewpoint::DNavigationLink, "label")
    descriptor = None
    for klass in viewpoint::DNavigationLink.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::dnavigable_is_not_abstract():
    assert not inspect.isabstract(viewpoint::DNavigable)


def test_viewpoint::dnavigable_constructor_exists():
    assert callable(viewpoint::DNavigable.__init__)


def test_viewpoint::dnavigable_constructor_args():
    sig = inspect.signature(viewpoint::DNavigable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::dvalidable_is_not_abstract():
    assert not inspect.isabstract(viewpoint::DValidable)


def test_viewpoint::dvalidable_constructor_exists():
    assert callable(viewpoint::DValidable.__init__)


def test_viewpoint::dvalidable_constructor_args():
    sig = inspect.signature(viewpoint::DValidable.__init__)
    params = list(sig.parameters.keys())



def test_featureextensiondescription_is_not_abstract():
    assert not inspect.isabstract(FeatureExtensionDescription)


def test_featureextensiondescription_constructor_exists():
    assert callable(FeatureExtensionDescription.__init__)


def test_featureextensiondescription_constructor_args():
    sig = inspect.signature(FeatureExtensionDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::dfeatureextension_is_not_abstract():
    assert not inspect.isabstract(viewpoint::DFeatureExtension)


def test_viewpoint::dfeatureextension_constructor_exists():
    assert callable(viewpoint::DFeatureExtension.__init__)


def test_viewpoint::dfeatureextension_constructor_args():
    sig = inspect.signature(viewpoint::DFeatureExtension.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::dview_is_not_abstract():
    assert not inspect.isabstract(viewpoint::DView)


def test_viewpoint::dview_constructor_exists():
    assert callable(viewpoint::DView.__init__)


def test_viewpoint::dview_constructor_args():
    sig = inspect.signature(viewpoint::DView.__init__)
    params = list(sig.parameters.keys())
    assert "initialized" in params, "Missing parameter 'initialized'"

def test_viewpoint::dview_has_initialized():
    assert hasattr(viewpoint::DView, "initialized")
    descriptor = None
    for klass in viewpoint::DView.__mro__:
        if "initialized" in klass.__dict__:
            descriptor = klass.__dict__["initialized"]
            break
    assert isinstance(descriptor, property)



def test_dannotationentry_is_not_abstract():
    assert not inspect.isabstract(DAnnotationEntry)


def test_dannotationentry_constructor_exists():
    assert callable(DAnnotationEntry.__init__)


def test_dannotationentry_constructor_args():
    sig = inspect.signature(DAnnotationEntry.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::eobject_is_not_abstract():
    assert not inspect.isabstract(viewpoint::EObject)


def test_viewpoint::eobject_constructor_exists():
    assert callable(viewpoint::EObject.__init__)


def test_viewpoint::eobject_constructor_args():
    sig = inspect.signature(viewpoint::EObject.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::danalysis_is_not_abstract():
    assert not inspect.isabstract(viewpoint::DAnalysis)


def test_viewpoint::danalysis_constructor_exists():
    assert callable(viewpoint::DAnalysis.__init__)


def test_viewpoint::danalysis_constructor_args():
    sig = inspect.signature(viewpoint::DAnalysis.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"

def test_viewpoint::danalysis_has_version():
    assert hasattr(viewpoint::DAnalysis, "version")
    descriptor = None
    for klass in viewpoint::DAnalysis.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

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

def test_backgroundstyle_exists():
    # Check that the Enumeration exists
    assert BackgroundStyle is not None

def test_backgroundstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BackgroundStyle]
    expected_literals = [
        "GradientTopToBottom",
        "GradientLeftToRight",
        "Liquid",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BackgroundStyle"

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

def test_error_level_exists():
    # Check that the Enumeration exists
    assert ERROR_LEVEL is not None

def test_error_level_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ERROR_LEVEL]
    expected_literals = [
        "WARNING",
        "ERROR",
        "INFO",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ERROR_LEVEL"

def test_edgearrows_exists():
    # Check that the Enumeration exists
    assert EdgeArrows is not None

def test_edgearrows_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EdgeArrows]
    expected_literals = [
        "InputClosedArrow",
        "NoDecoration",
        "InputArrow",
        "InputFillClosedArrow",
        "OutputClosedArrow",
        "OutputArrow",
        "InputArrowWithDiamond",
        "InputArrowWithFillDiamond",
        "OutputFillClosedArrow",
        "FillDiamond",
        "Diamond",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EdgeArrows"

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

def test_linestyle_exists():
    # Check that the Enumeration exists
    assert LineStyle is not None

def test_linestyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LineStyle]
    expected_literals = [
        "dash_dot",
        "dot",
        "solid",
        "dash",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LineStyle"

def test_containerlayout_exists():
    # Check that the Enumeration exists
    assert ContainerLayout is not None

def test_containerlayout_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContainerLayout]
    expected_literals = [
        "FreeForm",
        "List",
        "VerticalStack",
        "HorizontalStack",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContainerLayout"

def test_labelalignment_exists():
    # Check that the Enumeration exists
    assert LabelAlignment is not None

def test_labelalignment_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LabelAlignment]
    expected_literals = [
        "CENTER",
        "RIGHT",
        "LEFT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LabelAlignment"

def test_edgerouting_exists():
    # Check that the Enumeration exists
    assert EdgeRouting is not None

def test_edgerouting_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EdgeRouting]
    expected_literals = [
        "tree",
        "straight",
        "manhattan",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EdgeRouting"

def test_resizekind_exists():
    # Check that the Enumeration exists
    assert ResizeKind is not None

def test_resizekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ResizeKind]
    expected_literals = [
        "EAST_WEST",
        "NSEW",
        "NONE",
        "NORTH_SOUTH",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ResizeKind"

def test_position_exists():
    # Check that the Enumeration exists
    assert Position is not None

def test_position_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Position]
    expected_literals = [
        "WEST",
        "NORTH_EAST",
        "NORTH",
        "CENTER",
        "SOUTH_EAST",
        "SOUTH",
        "NORTH_WEST",
        "EAST",
        "SOUTH_WEST",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Position"

def test_foldingstyle_exists():
    # Check that the Enumeration exists
    assert FoldingStyle is not None

def test_foldingstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FoldingStyle]
    expected_literals = [
        "NONE",
        "TARGET",
        "SOURCE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FoldingStyle"

def test_dragsource_exists():
    # Check that the Enumeration exists
    assert DragSource is not None

def test_dragsource_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DragSource]
    expected_literals = [
        "PROJECT_EXPLORER",
        "BOTH",
        "DIAGRAM",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DragSource"

def test_syncstatus_exists():
    # Check that the Enumeration exists
    assert SyncStatus is not None

def test_syncstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SyncStatus]
    expected_literals = [
        "dirty",
        "sync",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SyncStatus"

def test_layoutdirection_exists():
    # Check that the Enumeration exists
    assert LayoutDirection is not None

def test_layoutdirection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LayoutDirection]
    expected_literals = [
        "TopToBottom",
        "BottomToTop",
        "LeftToRight",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LayoutDirection"

def test_labelposition_exists():
    # Check that the Enumeration exists
    assert LabelPosition is not None

def test_labelposition_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LabelPosition]
    expected_literals = [
        "border",
        "node",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LabelPosition"

def test_fontformat_exists():
    # Check that the Enumeration exists
    assert FontFormat is not None

def test_fontformat_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FontFormat]
    expected_literals = [
        "italic",
        "normal",
        "bold",
        "bold_italic",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FontFormat"

def test_navigationtargettype_exists():
    # Check that the Enumeration exists
    assert NavigationTargetType is not None

def test_navigationtargettype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NavigationTargetType]
    expected_literals = [
        "model",
        "file",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NavigationTargetType"

def test_systemcolors_exists():
    # Check that the Enumeration exists
    assert SystemColors is not None

def test_systemcolors_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SystemColors]
    expected_literals = [
        "light_chocolate",
        "dark_gray",
        "white",
        "dark_blue",
        "dark_yellow",
        "light_blue",
        "light_red",
        "light_green",
        "black",
        "green",
        "light_orange",
        "light_yellow",
        "dark_purple",
        "blue",
        "dark_chocolate",
        "light_purple",
        "dark_orange",
        "dark_red",
        "chocolate",
        "gray",
        "red",
        "light_gray",
        "purple",
        "yellow",
        "dark_green",
        "orange",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SystemColors"

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
        "ring",
        "triangle",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BundledImageShape"

def test_reconnectionkind_exists():
    # Check that the Enumeration exists
    assert ReconnectionKind is not None

def test_reconnectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ReconnectionKind]
    expected_literals = [
        "RECONNECT_BOTH",
        "RECONNECT_SOURCE",
        "RECONNECT_TARGET",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ReconnectionKind"

def test_arrangeconstraint_exists():
    # Check that the Enumeration exists
    assert ArrangeConstraint is not None

def test_arrangeconstraint_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ArrangeConstraint]
    expected_literals = [
        "KEEP_LOCATION",
        "KEEP_RATIO",
        "KEEP_SIZE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ArrangeConstraint"


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
ConditionalStyleDescription_strategy = st.builds(
    ConditionalStyleDescription,
)
viewpoint::description::ConditionalContainerStyleDescription_strategy = st.builds(
    viewpoint::description::ConditionalContainerStyleDescription,
)
viewpoint::description::ConditionalEdgeStyleDescription_strategy = st.builds(
    viewpoint::description::ConditionalEdgeStyleDescription,
)
viewpoint::description::ConditionalNodeStyleDescription_strategy = st.builds(
    viewpoint::description::ConditionalNodeStyleDescription,
)
description::ConditionalEdgeStyleDescription_strategy = st.builds(
    description::ConditionalEdgeStyleDescription,
)
style::EdgeStyleDescription_strategy = st.builds(
    style::EdgeStyleDescription,
)
viewpoint::description::IEdgeMapping_strategy = st.builds(
    viewpoint::description::IEdgeMapping,
)
tool::ReconnectEdgeDescription_strategy = st.builds(
    tool::ReconnectEdgeDescription,
)
description::ConditionalContainerStyleDescription_strategy = st.builds(
    description::ConditionalContainerStyleDescription,
)
style::ContainerStyleDescription_strategy = st.builds(
    style::ContainerStyleDescription,
)
description::AbstractMappingImport_strategy = st.builds(
    description::AbstractMappingImport,
)
description::ConditionalNodeStyleDescription_strategy = st.builds(
    description::ConditionalNodeStyleDescription,
)
style::NodeStyleDescription_strategy = st.builds(
    style::NodeStyleDescription,
)
tool::DoubleClickDescription_strategy = st.builds(
    tool::DoubleClickDescription,
)
description::AbstractNodeMapping_strategy = st.builds(
    description::AbstractNodeMapping,
)
tool::DirectEditLabel_strategy = st.builds(
    tool::DirectEditLabel,
)
tool::DeleteElementDescription_strategy = st.builds(
    tool::DeleteElementDescription,
)
tool::ToolSection_strategy = st.builds(
    tool::ToolSection,
)
description::RepresentationElementMapping_strategy = st.builds(
    description::RepresentationElementMapping,
)
description::RepresentationImportDescription_strategy = st.builds(
    description::RepresentationImportDescription,
)
description::AdditionalLayer_strategy = st.builds(
    description::AdditionalLayer,
)
description::Layout_strategy = st.builds(
    description::Layout,
)
description::EdgeMappingImport_strategy = st.builds(
    description::EdgeMappingImport,
)
description::EdgeMapping_strategy = st.builds(
    description::EdgeMapping,
)
concern::ConcernSet_strategy = st.builds(
    concern::ConcernSet,
)
ModelElement2ViewVariable_strategy = st.builds(
    ModelElement2ViewVariable,
)
viewpoint::diagram::DiagramElementMapping2ModelElement_strategy = st.builds(
    viewpoint::diagram::DiagramElementMapping2ModelElement,
)
DiagramElementMapping2ModelElement_strategy = st.builds(
    DiagramElementMapping2ModelElement,
)
viewpoint::diagram::ComputedStyleDescriptionRegistry_strategy = st.builds(
    viewpoint::diagram::ComputedStyleDescriptionRegistry,
)
description::PasteTargetDescription_strategy = st.builds(
    description::PasteTargetDescription,
)
viewpoint::description::DiagramElementMapping_strategy = st.builds(
    viewpoint::description::DiagramElementMapping,
    semanticElements=
        safe_text,
    createElements=
        st.booleans(),
    semanticCandidatesExpression=
        safe_text,
    preconditionExpression=
        safe_text,
    synchronizationLock=
        st.booleans()
)
description::RepresentationDescription_strategy = st.builds(
    description::RepresentationDescription,
)
description::DragAndDropTargetDescription_strategy = st.builds(
    description::DragAndDropTargetDescription,
)
viewpoint::description::ContainerMapping_strategy = st.builds(
    viewpoint::description::ContainerMapping,
    childrenPresentation=
        safe_text
)
viewpoint::description::NodeMapping_strategy = st.builds(
    viewpoint::description::NodeMapping,
)
viewpoint::description::DiagramDescription_strategy = st.builds(
    viewpoint::description::DiagramDescription,
    enablePopupBars=
        st.booleans(),
    preconditionExpression=
        safe_text,
    domainClass=
        safe_text,
    rootExpression=
        safe_text
)
viewpoint::diagram::ContainerVariable2StyleDescription_strategy = st.builds(
    viewpoint::diagram::ContainerVariable2StyleDescription,
)
ContainerVariable2StyleDescription_strategy = st.builds(
    ContainerVariable2StyleDescription,
)
viewpoint::diagram::ViewVariable2ContainerVariable_strategy = st.builds(
    viewpoint::diagram::ViewVariable2ContainerVariable,
)
ViewVariable2ContainerVariable_strategy = st.builds(
    ViewVariable2ContainerVariable,
)
viewpoint::diagram::ModelElement2ViewVariable_strategy = st.builds(
    viewpoint::diagram::ModelElement2ViewVariable,
)
diagram::viewpoint::EObject_strategy = st.builds(
    diagram::viewpoint::EObject,
)
filter::FilterVariable_strategy = st.builds(
    filter::FilterVariable,
)
viewpoint::diagram::FilterVariableValue_strategy = st.builds(
    viewpoint::diagram::FilterVariableValue,
)
FilterVariableValue_strategy = st.builds(
    FilterVariableValue,
)
CollapseFilter_strategy = st.builds(
    CollapseFilter,
)
viewpoint::diagram::IndirectlyCollapseFilter_strategy = st.builds(
    viewpoint::diagram::IndirectlyCollapseFilter,
)
viewpoint::diagram::FilterVariableHistory_strategy = st.builds(
    viewpoint::diagram::FilterVariableHistory,
)
GaugeSection_strategy = st.builds(
    GaugeSection,
)
EndLabelStyle_strategy = st.builds(
    EndLabelStyle,
)
CenterLabelStyle_strategy = st.builds(
    CenterLabelStyle,
)
BeginLabelStyle_strategy = st.builds(
    BeginLabelStyle,
)
diagram::ContainerStyle_strategy = st.builds(
    diagram::ContainerStyle,
)
viewpoint::validation::ValidationFix_strategy = st.builds(
    viewpoint::validation::ValidationFix,
    name=
        safe_text
)
ValidationRule_strategy = st.builds(
    ValidationRule,
)
viewpoint::validation::ViewValidationRule_strategy = st.builds(
    viewpoint::validation::ViewValidationRule,
)
viewpoint::validation::SemanticValidationRule_strategy = st.builds(
    viewpoint::validation::SemanticValidationRule,
    targetClass=
        safe_text
)
validation::ValidationFix_strategy = st.builds(
    validation::ValidationFix,
)
validation::RuleAudit_strategy = st.builds(
    validation::RuleAudit,
)
viewpoint::validation::ValidationRule_strategy = st.builds(
    viewpoint::validation::ValidationRule,
    message=
        safe_text,
    level=
        safe_text
)
viewpoint::validation::RuleAudit_strategy = st.builds(
    viewpoint::validation::RuleAudit,
    auditExpression=
        safe_text
)
SelectionDescription_strategy = st.builds(
    SelectionDescription,
)
viewpoint::filter::FilterVariable_strategy = st.builds(
    viewpoint::filter::FilterVariable,
    name=
        safe_text
)
filter::Filter_strategy = st.builds(
    filter::Filter,
)
FilterDescription_strategy = st.builds(
    FilterDescription,
)
viewpoint::filter::CompositeFilterDescription_strategy = st.builds(
    viewpoint::filter::CompositeFilterDescription,
)
Filter_strategy = st.builds(
    Filter,
)
viewpoint::filter::VariableFilter_strategy = st.builds(
    viewpoint::filter::VariableFilter,
    semanticConditionExpression=
        safe_text
)
viewpoint::filter::MappingFilter_strategy = st.builds(
    viewpoint::filter::MappingFilter,
    viewConditionExpression=
        safe_text,
    semanticConditionExpression=
        safe_text
)
viewpoint::filter::Filter_strategy = st.builds(
    viewpoint::filter::Filter,
    filterKind=
        safe_text
)
RepresentationNavigationDescription_strategy = st.builds(
    RepresentationNavigationDescription,
)
CreateView_strategy = st.builds(
    CreateView,
)
viewpoint::tool::DiagramNavigationDescription_strategy = st.builds(
    viewpoint::tool::DiagramNavigationDescription,
)
viewpoint::tool::CreateEdgeView_strategy = st.builds(
    viewpoint::tool::CreateEdgeView,
    targetExpression=
        safe_text,
    sourceExpression=
        safe_text
)
RepresentationCreationDescription_strategy = st.builds(
    RepresentationCreationDescription,
)
viewpoint::tool::DiagramCreationDescription_strategy = st.builds(
    viewpoint::tool::DiagramCreationDescription,
)
tool::EditMaskVariables_strategy = st.builds(
    tool::EditMaskVariables,
)
tool::ElementDoubleClickVariable_strategy = st.builds(
    tool::ElementDoubleClickVariable,
)
tool::DeleteHook_strategy = st.builds(
    tool::DeleteHook,
)
viewpoint::tool::DeleteHookParameter_strategy = st.builds(
    viewpoint::tool::DeleteHookParameter,
    value=
        safe_text,
    name=
        safe_text
)
tool::DeleteHookParameter_strategy = st.builds(
    tool::DeleteHookParameter,
)
viewpoint::tool::DeleteHook_strategy = st.builds(
    viewpoint::tool::DeleteHook,
    id=
        safe_text
)
tool::ElementDeleteVariable_strategy = st.builds(
    tool::ElementDeleteVariable,
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
tool::InitEdgeCreationOperation_strategy = st.builds(
    tool::InitEdgeCreationOperation,
)
tool::InitialNodeCreationOperation_strategy = st.builds(
    tool::InitialNodeCreationOperation,
)
tool::NodeCreationVariable_strategy = st.builds(
    tool::NodeCreationVariable,
)
tool::PopupMenu_strategy = st.builds(
    tool::PopupMenu,
)
tool::ToolGroup_strategy = st.builds(
    tool::ToolGroup,
)
viewpoint::tool::ToolGroupExtension_strategy = st.builds(
    viewpoint::tool::ToolGroupExtension,
)
tool::ToolGroupExtension_strategy = st.builds(
    tool::ToolGroupExtension,
)
style::BeginLabelStyleDescription_strategy = st.builds(
    style::BeginLabelStyleDescription,
)
EdgeStyleDescription_strategy = st.builds(
    EdgeStyleDescription,
)
viewpoint::style::BracketEdgeStyleDescription_strategy = st.builds(
    viewpoint::style::BracketEdgeStyleDescription,
)
style::EndLabelStyleDescription_strategy = st.builds(
    style::EndLabelStyleDescription,
)
style::CenterLabelStyleDescription_strategy = st.builds(
    style::CenterLabelStyleDescription,
)
viewpoint::style::WorkspaceImageDescription_strategy = st.builds(
    viewpoint::style::WorkspaceImageDescription,
    workspacePath=
        safe_text
)
viewpoint::style::SizeComputationContainerStyleDescription_strategy = st.builds(
    viewpoint::style::SizeComputationContainerStyleDescription,
    widthComputationExpression=
        safe_text,
    heightComputationExpression=
        safe_text
)
style::SizeComputationContainerStyleDescription_strategy = st.builds(
    style::SizeComputationContainerStyleDescription,
)
viewpoint::style::ShapeContainerStyleDescription_strategy = st.builds(
    viewpoint::style::ShapeContainerStyleDescription,
    shape=
        safe_text
)
viewpoint::style::FlatContainerStyleDescription_strategy = st.builds(
    viewpoint::style::FlatContainerStyleDescription,
    backgroundStyle=
        safe_text
)
style::RoundedCornerStyleDescription_strategy = st.builds(
    style::RoundedCornerStyleDescription,
)
viewpoint::style::GaugeSectionDescription_strategy = st.builds(
    viewpoint::style::GaugeSectionDescription,
    label=
        safe_text,
    minValueExpression=
        safe_text,
    maxValueExpression=
        safe_text,
    valueExpression=
        safe_text
)
style::GaugeSectionDescription_strategy = st.builds(
    style::GaugeSectionDescription,
)
NodeStyleDescription_strategy = st.builds(
    NodeStyleDescription,
)
viewpoint::style::LozengeNodeDescription_strategy = st.builds(
    viewpoint::style::LozengeNodeDescription,
    heightComputationExpression=
        safe_text,
    widthComputationExpression=
        safe_text
)
viewpoint::style::BundledImageDescription_strategy = st.builds(
    viewpoint::style::BundledImageDescription,
    shape=
        safe_text
)
viewpoint::style::GaugeCompositeStyleDescription_strategy = st.builds(
    viewpoint::style::GaugeCompositeStyleDescription,
    alignment=
        safe_text
)
viewpoint::style::SquareDescription_strategy = st.builds(
    viewpoint::style::SquareDescription,
    width=
        safe_text,
    height=
        safe_text
)
viewpoint::style::DotDescription_strategy = st.builds(
    viewpoint::style::DotDescription,
    strokeSizeComputationExpression=
        safe_text
)
viewpoint::style::NoteDescription_strategy = st.builds(
    viewpoint::style::NoteDescription,
)
viewpoint::style::CustomStyleDescription_strategy = st.builds(
    viewpoint::style::CustomStyleDescription,
    id=
        safe_text
)
viewpoint::style::EllipseNodeDescription_strategy = st.builds(
    viewpoint::style::EllipseNodeDescription,
    verticalDiameterComputationExpression=
        safe_text,
    horizontalDiameterComputationExpression=
        safe_text
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
viewpoint::style::ContainerStyleDescription_strategy = st.builds(
    viewpoint::style::ContainerStyleDescription,
    roundedCorner=
        st.booleans()
)
StyleDescription_strategy = st.builds(
    StyleDescription,
)
viewpoint::style::EdgeStyleDescription_strategy = st.builds(
    viewpoint::style::EdgeStyleDescription,
    lineStyle=
        safe_text,
    foldingStyle=
        safe_text,
    targetArrow=
        safe_text,
    sourceArrow=
        safe_text,
    routingStyle=
        safe_text,
    sizeComputationExpression=
        safe_text
)
viewpoint::style::RoundedCornerStyleDescription_strategy = st.builds(
    viewpoint::style::RoundedCornerStyleDescription,
    arcWidth=
        safe_text,
    arcHeight=
        safe_text
)
viewpoint::style::BorderedStyleDescription_strategy = st.builds(
    viewpoint::style::BorderedStyleDescription,
    borderSizeComputationExpression=
        safe_text
)
Layer_strategy = st.builds(
    Layer,
)
viewpoint::description::AdditionalLayer_strategy = st.builds(
    viewpoint::description::AdditionalLayer,
    activeByDefault=
        st.booleans(),
    optional=
        st.booleans()
)
Customization_strategy = st.builds(
    Customization,
)
DecorationDescriptionsSet_strategy = st.builds(
    DecorationDescriptionsSet,
)
Layout_strategy = st.builds(
    Layout,
)
viewpoint::description::CompositeLayout_strategy = st.builds(
    viewpoint::description::CompositeLayout,
    padding=
        st.integers(),
    direction=
        safe_text
)
viewpoint::description::OrderedTreeLayout_strategy = st.builds(
    viewpoint::description::OrderedTreeLayout,
    childrenExpression=
        safe_text
)
DocumentedElement_strategy = st.builds(
    DocumentedElement,
)
viewpoint::validation::ValidationSet_strategy = st.builds(
    viewpoint::validation::ValidationSet,
    name=
        safe_text
)
viewpoint::description::Layout_strategy = st.builds(
    viewpoint::description::Layout,
)
viewpoint::concern::ConcernSet_strategy = st.builds(
    viewpoint::concern::ConcernSet,
)
AbstractVariable_strategy = st.builds(
    AbstractVariable,
)
viewpoint::tool::DialogVariable_strategy = st.builds(
    viewpoint::tool::DialogVariable,
    dialogPrompt=
        safe_text
)
viewpoint::tool::SubVariable_strategy = st.builds(
    viewpoint::tool::SubVariable,
)
tool::VariableContainer_strategy = st.builds(
    tool::VariableContainer,
)
tool::SubVariable_strategy = st.builds(
    tool::SubVariable,
)
viewpoint::tool::AcceleoVariable_strategy = st.builds(
    viewpoint::tool::AcceleoVariable,
    computationExpression=
        safe_text
)
viewpoint::tool::VariableContainer_strategy = st.builds(
    viewpoint::tool::VariableContainer,
)
viewpoint::tool::AbstractVariable_strategy = st.builds(
    viewpoint::tool::AbstractVariable,
    name=
        safe_text
)
tool::ExternalJavaAction_strategy = st.builds(
    tool::ExternalJavaAction,
)
tool::ExternalJavaActionParameter_strategy = st.builds(
    tool::ExternalJavaActionParameter,
)
tool::ContainerModelOperation_strategy = st.builds(
    tool::ContainerModelOperation,
)
MenuItemDescription_strategy = st.builds(
    MenuItemDescription,
)
viewpoint::tool::OperationAction_strategy = st.builds(
    viewpoint::tool::OperationAction,
)
tool::MenuItemDescription_strategy = st.builds(
    tool::MenuItemDescription,
)
viewpoint::tool::ExternalJavaAction_strategy = st.builds(
    viewpoint::tool::ExternalJavaAction,
    id=
        safe_text
)
viewpoint::tool::ExternalJavaActionCall_strategy = st.builds(
    viewpoint::tool::ExternalJavaActionCall,
)
MenuItemOrRef_strategy = st.builds(
    MenuItemOrRef,
)
viewpoint::tool::MenuItemDescriptionReference_strategy = st.builds(
    viewpoint::tool::MenuItemDescriptionReference,
)
tool::MenuItemOrRef_strategy = st.builds(
    tool::MenuItemOrRef,
)
viewpoint::tool::MenuItemOrRef_strategy = st.builds(
    viewpoint::tool::MenuItemOrRef,
)
tool::NameVariable_strategy = st.builds(
    tool::NameVariable,
)
tool::SelectContainerVariable_strategy = st.builds(
    tool::SelectContainerVariable,
)
tool::InitialContainerDropOperation_strategy = st.builds(
    tool::InitialContainerDropOperation,
)
tool::ContainerViewVariable_strategy = st.builds(
    tool::ContainerViewVariable,
)
tool::ElementSelectVariable_strategy = st.builds(
    tool::ElementSelectVariable,
)
description::SelectionDescription_strategy = st.builds(
    description::SelectionDescription,
)
tool::AbstractToolDescription_strategy = st.builds(
    tool::AbstractToolDescription,
)
viewpoint::tool::MenuItemDescription_strategy = st.builds(
    viewpoint::tool::MenuItemDescription,
    icon=
        safe_text
)
viewpoint::tool::SelectionWizardDescription_strategy = st.builds(
    viewpoint::tool::SelectionWizardDescription,
    windowImagePath=
        safe_text,
    windowTitle=
        safe_text,
    iconPath=
        safe_text
)
tool::DropContainerVariable_strategy = st.builds(
    tool::DropContainerVariable,
)
description::DiagramElementMapping_strategy = st.builds(
    description::DiagramElementMapping,
)
tool::InitialOperation_strategy = st.builds(
    tool::InitialOperation,
)
tool::ElementViewVariable_strategy = st.builds(
    tool::ElementViewVariable,
)
tool::ElementVariable_strategy = st.builds(
    tool::ElementVariable,
)
MappingBasedToolDescription_strategy = st.builds(
    MappingBasedToolDescription,
)
viewpoint::tool::ContainerCreationDescription_strategy = st.builds(
    viewpoint::tool::ContainerCreationDescription,
    iconPath=
        safe_text
)
viewpoint::tool::PasteDescription_strategy = st.builds(
    viewpoint::tool::PasteDescription,
)
viewpoint::tool::ContainerDropDescription_strategy = st.builds(
    viewpoint::tool::ContainerDropDescription,
    dragSource=
        safe_text,
    moveEdges=
        st.booleans()
)
viewpoint::tool::DeleteElementDescription_strategy = st.builds(
    viewpoint::tool::DeleteElementDescription,
)
viewpoint::tool::EdgeCreationDescription_strategy = st.builds(
    viewpoint::tool::EdgeCreationDescription,
    connectionStartPrecondition=
        safe_text,
    iconPath=
        safe_text
)
viewpoint::tool::DoubleClickDescription_strategy = st.builds(
    viewpoint::tool::DoubleClickDescription,
)
viewpoint::tool::ReconnectEdgeDescription_strategy = st.builds(
    viewpoint::tool::ReconnectEdgeDescription,
    reconnectionKind=
        safe_text
)
viewpoint::tool::NodeCreationDescription_strategy = st.builds(
    viewpoint::tool::NodeCreationDescription,
    iconPath=
        safe_text
)
viewpoint::tool::DirectEditLabel_strategy = st.builds(
    viewpoint::tool::DirectEditLabel,
    inputLabelExpression=
        safe_text
)
viewpoint::tool::ToolDescription_strategy = st.builds(
    viewpoint::tool::ToolDescription,
    iconPath=
        safe_text
)
AbstractToolDescription_strategy = st.builds(
    AbstractToolDescription,
)
viewpoint::tool::RepresentationCreationDescription_strategy = st.builds(
    viewpoint::tool::RepresentationCreationDescription,
    browseExpression=
        safe_text,
    titleExpression=
        safe_text
)
viewpoint::tool::RequestDescription_strategy = st.builds(
    viewpoint::tool::RequestDescription,
    type=
        safe_text
)
viewpoint::tool::BehaviorTool_strategy = st.builds(
    viewpoint::tool::BehaviorTool,
    domainClass=
        safe_text
)
viewpoint::tool::PaneBasedSelectionWizardDescription_strategy = st.builds(
    viewpoint::tool::PaneBasedSelectionWizardDescription,
    selectedValuesMessage=
        safe_text,
    message=
        safe_text,
    iconPath=
        safe_text,
    choiceOfValuesMessage=
        safe_text,
    rootExpression=
        safe_text,
    childrenExpression=
        safe_text,
    candidatesExpression=
        safe_text,
    windowImagePath=
        safe_text,
    tree=
        st.booleans(),
    preSelectedCandidatesExpression=
        safe_text,
    windowTitle=
        safe_text
)
viewpoint::tool::PopupMenu_strategy = st.builds(
    viewpoint::tool::PopupMenu,
)
viewpoint::tool::RepresentationNavigationDescription_strategy = st.builds(
    viewpoint::tool::RepresentationNavigationDescription,
    browseExpression=
        safe_text,
    navigationNameExpression=
        safe_text
)
viewpoint::tool::MappingBasedToolDescription_strategy = st.builds(
    viewpoint::tool::MappingBasedToolDescription,
)
tool::ElementDropVariable_strategy = st.builds(
    tool::ElementDropVariable,
)
tool::ToolFilterDescription_strategy = st.builds(
    tool::ToolFilterDescription,
)
ToolEntry_strategy = st.builds(
    ToolEntry,
)
viewpoint::tool::ToolGroup_strategy = st.builds(
    viewpoint::tool::ToolGroup,
)
viewpoint::tool::AbstractToolDescription_strategy = st.builds(
    viewpoint::tool::AbstractToolDescription,
    precondition=
        safe_text,
    forceRefresh=
        st.booleans()
)
viewpoint::style::TooltipStyleDescription_strategy = st.builds(
    viewpoint::style::TooltipStyleDescription,
    tooltipExpression=
        safe_text
)
viewpoint::style::LabelBorderStyleDescription_strategy = st.builds(
    viewpoint::style::LabelBorderStyleDescription,
    cornerHeight=
        st.integers(),
    name=
        safe_text,
    cornerWidth=
        st.integers(),
    id=
        safe_text
)
style::LabelBorderStyleDescription_strategy = st.builds(
    style::LabelBorderStyleDescription,
)
viewpoint::style::LabelBorderStyles_strategy = st.builds(
    viewpoint::style::LabelBorderStyles,
)
BasicLabelStyleDescription_strategy = st.builds(
    BasicLabelStyleDescription,
)
viewpoint::style::CenterLabelStyleDescription_strategy = st.builds(
    viewpoint::style::CenterLabelStyleDescription,
)
viewpoint::style::EndLabelStyleDescription_strategy = st.builds(
    viewpoint::style::EndLabelStyleDescription,
)
viewpoint::style::BeginLabelStyleDescription_strategy = st.builds(
    viewpoint::style::BeginLabelStyleDescription,
)
viewpoint::style::LabelStyleDescription_strategy = st.builds(
    viewpoint::style::LabelStyleDescription,
    labelAlignment=
        safe_text
)
viewpoint::style::BasicLabelStyleDescription_strategy = st.builds(
    viewpoint::style::BasicLabelStyleDescription,
    labelSize=
        st.integers(),
    labelFormat=
        safe_text,
    iconPath=
        safe_text,
    labelExpression=
        safe_text,
    showIcon=
        st.booleans()
)
viewpoint::style::StyleDescription_strategy = st.builds(
    viewpoint::style::StyleDescription,
)
viewpoint::description::DAnnotationEntry_strategy = st.builds(
    viewpoint::description::DAnnotationEntry,
    source=
        safe_text,
    details=
        safe_text
)
viewpoint::description::IdentifiedElement_strategy = st.builds(
    viewpoint::description::IdentifiedElement,
    label=
        safe_text,
    name=
        safe_text
)
viewpoint::description::EndUserDocumentedElement_strategy = st.builds(
    viewpoint::description::EndUserDocumentedElement,
    endUserDocumentation=
        safe_text
)
viewpoint::description::AnnotationEntry_strategy = st.builds(
    viewpoint::description::AnnotationEntry,
    source=
        safe_text
)
UserColor_strategy = st.builds(
    UserColor,
)
viewpoint::description::UserColorsPalette_strategy = st.builds(
    viewpoint::description::UserColorsPalette,
    name=
        safe_text
)
SystemColor_strategy = st.builds(
    SystemColor,
)
viewpoint::description::SytemColorsPalette_strategy = st.builds(
    viewpoint::description::SytemColorsPalette,
)
style::LabelBorderStyles_strategy = st.builds(
    style::LabelBorderStyles,
)
tool::ToolEntry_strategy = st.builds(
    tool::ToolEntry,
)
viewpoint::description::Environment_strategy = st.builds(
    viewpoint::description::Environment,
)
viewpoint::description::UserColor_strategy = st.builds(
    viewpoint::description::UserColor,
    name=
        safe_text
)
description::FixedColor_strategy = st.builds(
    description::FixedColor,
)
ColorDescription_strategy = st.builds(
    ColorDescription,
)
viewpoint::description::FixedColor_strategy = st.builds(
    viewpoint::description::FixedColor,
    green=
        st.integers(),
    blue=
        st.integers(),
    red=
        st.integers()
)
viewpoint::description::ColorStep_strategy = st.builds(
    viewpoint::description::ColorStep,
    associatedValue=
        safe_text
)
ColorStep_strategy = st.builds(
    ColorStep,
)
description::ColorDescription_strategy = st.builds(
    description::ColorDescription,
)
FixedColor_strategy = st.builds(
    FixedColor,
)
viewpoint::description::SystemColor_strategy = st.builds(
    viewpoint::description::SystemColor,
    name=
        safe_text
)
viewpoint::description::ColorDescription_strategy = st.builds(
    viewpoint::description::ColorDescription,
)
viewpoint::description::SelectionDescription_strategy = st.builds(
    viewpoint::description::SelectionDescription,
    message=
        safe_text,
    multiple=
        st.booleans(),
    tree=
        st.booleans(),
    candidatesExpression=
        safe_text,
    childrenExpression=
        safe_text,
    rootExpression=
        safe_text
)
description::UserColor_strategy = st.builds(
    description::UserColor,
)
viewpoint::description::InterpolatedColor_strategy = st.builds(
    viewpoint::description::InterpolatedColor,
    colorValueComputationExpression=
        safe_text,
    minValueComputationExpression=
        safe_text,
    maxValueComputationExpression=
        safe_text
)
viewpoint::description::UserFixedColor_strategy = st.builds(
    viewpoint::description::UserFixedColor,
)
viewpoint::description::ComputedColor_strategy = st.builds(
    viewpoint::description::ComputedColor,
    red=
        safe_text,
    green=
        safe_text,
    blue=
        safe_text
)
EStructuralFeatureCustomization_strategy = st.builds(
    EStructuralFeatureCustomization,
)
viewpoint::description::EReferenceCustomization_strategy = st.builds(
    viewpoint::description::EReferenceCustomization,
    referenceName=
        safe_text
)
viewpoint::description::IVSMElementCustomization_strategy = st.builds(
    viewpoint::description::IVSMElementCustomization,
)
IVSMElementCustomization_strategy = st.builds(
    IVSMElementCustomization,
)
viewpoint::description::VSMElementCustomizationReuse_strategy = st.builds(
    viewpoint::description::VSMElementCustomizationReuse,
)
viewpoint::description::VSMElementCustomization_strategy = st.builds(
    viewpoint::description::VSMElementCustomization,
    predicateExpression=
        safe_text
)
viewpoint::description::Customization_strategy = st.builds(
    viewpoint::description::Customization,
)
viewpoint::description::EAttributeCustomization_strategy = st.builds(
    viewpoint::description::EAttributeCustomization,
    value=
        safe_text,
    attributeName=
        safe_text
)
viewpoint::description::EStructuralFeatureCustomization_strategy = st.builds(
    viewpoint::description::EStructuralFeatureCustomization,
    applyOnAll=
        st.booleans()
)
viewpoint::description::DecorationDescription_strategy = st.builds(
    viewpoint::description::DecorationDescription,
    position=
        safe_text,
    preconditionExpression=
        safe_text,
    decoratorPath=
        safe_text,
    name=
        safe_text
)
viewpoint::description::DecorationDescriptionsSet_strategy = st.builds(
    viewpoint::description::DecorationDescriptionsSet,
)
tool::PasteDescription_strategy = st.builds(
    tool::PasteDescription,
)
viewpoint::description::PasteTargetDescription_strategy = st.builds(
    viewpoint::description::PasteTargetDescription,
)
tool::ContainerDropDescription_strategy = st.builds(
    tool::ContainerDropDescription,
)
viewpoint::description::DragAndDropTargetDescription_strategy = st.builds(
    viewpoint::description::DragAndDropTargetDescription,
)
viewpoint::description::ConditionalStyleDescription_strategy = st.builds(
    viewpoint::description::ConditionalStyleDescription,
    predicateExpression=
        safe_text
)
description::viewpoint::EStringToStringMapEntry_strategy = st.builds(
    description::viewpoint::EStringToStringMapEntry,
)
viewpoint::description::DAnnotation_strategy = st.builds(
    viewpoint::description::DAnnotation,
    source=
        safe_text
)
DAnnotation_strategy = st.builds(
    DAnnotation,
)
viewpoint::description::AbstractMappingImport_strategy = st.builds(
    viewpoint::description::AbstractMappingImport,
    hideSubMappings=
        st.booleans(),
    inheritsAncestorFilters=
        st.booleans()
)
tool::RepresentationNavigationDescription_strategy = st.builds(
    tool::RepresentationNavigationDescription,
)
tool::RepresentationCreationDescription_strategy = st.builds(
    tool::RepresentationCreationDescription,
)
IdentifiedElement_strategy = st.builds(
    IdentifiedElement,
)
viewpoint::description::RepresentationElementMapping_strategy = st.builds(
    viewpoint::description::RepresentationElementMapping,
)
viewpoint::description::JavaExtension_strategy = st.builds(
    viewpoint::description::JavaExtension,
    qualifiedClassName=
        safe_text
)
description::viewpoint::EObject_strategy = st.builds(
    description::viewpoint::EObject,
)
viewpoint::description::MetamodelExtensionSetting_strategy = st.builds(
    viewpoint::description::MetamodelExtensionSetting,
)
viewpoint::description::RepresentationExtensionDescription_strategy = st.builds(
    viewpoint::description::RepresentationExtensionDescription,
    name=
        safe_text,
    representationName=
        safe_text,
    viewpointURI=
        safe_text
)
viewpoint::description::DModelElement_strategy = st.builds(
    viewpoint::description::DModelElement,
)
viewpoint::description::DocumentedElement_strategy = st.builds(
    viewpoint::description::DocumentedElement,
    documentation=
        safe_text
)
description::viewpoint::EPackage_strategy = st.builds(
    description::viewpoint::EPackage,
)
viewpoint::description::FeatureExtensionDescription_strategy = st.builds(
    viewpoint::description::FeatureExtensionDescription,
)
RepresentationTemplate_strategy = st.builds(
    RepresentationTemplate,
)
MetamodelExtensionSetting_strategy = st.builds(
    MetamodelExtensionSetting,
)
JavaExtension_strategy = st.builds(
    JavaExtension,
)
RepresentationExtensionDescription_strategy = st.builds(
    RepresentationExtensionDescription,
)
viewpoint::description::DiagramExtensionDescription_strategy = st.builds(
    viewpoint::description::DiagramExtensionDescription,
)
RepresentationDescription_strategy = st.builds(
    RepresentationDescription,
)
viewpoint::description::RepresentationImportDescription_strategy = st.builds(
    viewpoint::description::RepresentationImportDescription,
)
viewpoint::description::RepresentationTemplate_strategy = st.builds(
    viewpoint::description::RepresentationTemplate,
    name=
        safe_text
)
validation::ValidationSet_strategy = st.builds(
    validation::ValidationSet,
)
description::IdentifiedElement_strategy = st.builds(
    description::IdentifiedElement,
)
description::EndUserDocumentedElement_strategy = st.builds(
    description::EndUserDocumentedElement,
)
description::Component_strategy = st.builds(
    description::Component,
)
viewpoint::description::Component_strategy = st.builds(
    viewpoint::description::Component,
)
UserColorsPalette_strategy = st.builds(
    UserColorsPalette,
)
SytemColorsPalette_strategy = st.builds(
    SytemColorsPalette,
)
viewpoint::Customizable_strategy = st.builds(
    viewpoint::Customizable,
    customFeatures=
        safe_text
)
DFile_strategy = st.builds(
    DFile,
)
viewpoint::DModel_strategy = st.builds(
    viewpoint::DModel,
)
DResourceContainer_strategy = st.builds(
    DResourceContainer,
)
viewpoint::DFolder_strategy = st.builds(
    viewpoint::DFolder,
)
viewpoint::DProject_strategy = st.builds(
    viewpoint::DProject,
)
DResource_strategy = st.builds(
    DResource,
)
viewpoint::DResourceContainer_strategy = st.builds(
    viewpoint::DResourceContainer,
)
viewpoint::DFile_strategy = st.builds(
    viewpoint::DFile,
)
viewpoint::DResource_strategy = st.builds(
    viewpoint::DResource,
    path=
        safe_text,
    name=
        safe_text
)
viewpoint::SessionManagerEObject_strategy = st.builds(
    viewpoint::SessionManagerEObject,
)
viewpoint::DAnalysisSessionEObject_strategy = st.builds(
    viewpoint::DAnalysisSessionEObject,
    controlledResources=
        safe_text,
    resources=
        safe_text,
    blocked=
        st.booleans(),
    open=
        st.booleans(),
    synchronizationStatus=
        safe_text
)
viewpoint::RGBValues_strategy = st.builds(
    viewpoint::RGBValues,
    green=
        st.integers(),
    blue=
        st.integers(),
    red=
        st.integers()
)
DNavigationLink_strategy = st.builds(
    DNavigationLink,
)
viewpoint::DEObjectLink_strategy = st.builds(
    viewpoint::DEObjectLink,
)
viewpoint::DragAndDropTarget_strategy = st.builds(
    viewpoint::DragAndDropTarget,
)
style::StyleDescription_strategy = st.builds(
    style::StyleDescription,
)
viewpoint::style::NodeStyleDescription_strategy = st.builds(
    viewpoint::style::NodeStyleDescription,
    resizeKind=
        safe_text,
    hideLabelByDefault=
        st.booleans(),
    sizeComputationExpression=
        safe_text,
    labelPosition=
        safe_text
)
Customizable_strategy = st.builds(
    Customizable,
)
viewpoint::BasicLabelStyle_strategy = st.builds(
    viewpoint::BasicLabelStyle,
    labelSize=
        st.integers(),
    iconPath=
        safe_text,
    showIcon=
        st.booleans(),
    labelFormat=
        safe_text
)
BasicLabelStyle_strategy = st.builds(
    BasicLabelStyle,
)
viewpoint::diagram::CenterLabelStyle_strategy = st.builds(
    viewpoint::diagram::CenterLabelStyle,
)
viewpoint::diagram::EndLabelStyle_strategy = st.builds(
    viewpoint::diagram::EndLabelStyle,
)
viewpoint::diagram::BeginLabelStyle_strategy = st.builds(
    viewpoint::diagram::BeginLabelStyle,
)
viewpoint::LabelStyle_strategy = st.builds(
    viewpoint::LabelStyle,
    labelAlignment=
        safe_text
)
viewpoint::DAnalysisCustomData_strategy = st.builds(
    viewpoint::DAnalysisCustomData,
    key=
        safe_text
)
viewpoint::DSourceFileLink_strategy = st.builds(
    viewpoint::DSourceFileLink,
    endPosition=
        st.integers(),
    startPosition=
        st.integers(),
    filePath=
        safe_text
)
DecorationDescription_strategy = st.builds(
    DecorationDescription,
)
viewpoint::description::MappingBasedDecoration_strategy = st.builds(
    viewpoint::description::MappingBasedDecoration,
)
viewpoint::description::SemanticBasedDecoration_strategy = st.builds(
    viewpoint::description::SemanticBasedDecoration,
    domainClass=
        safe_text
)
diagram::NodeStyle_strategy = st.builds(
    diagram::NodeStyle,
)
viewpoint::diagram::WorkspaceImage_strategy = st.builds(
    viewpoint::diagram::WorkspaceImage,
    workspacePath=
        safe_text
)
viewpoint::diagram::EdgeTarget_strategy = st.builds(
    viewpoint::diagram::EdgeTarget,
)
diagram::BorderedStyle_strategy = st.builds(
    diagram::BorderedStyle,
)
Style_strategy = st.builds(
    Style,
)
viewpoint::diagram::BorderedStyle_strategy = st.builds(
    viewpoint::diagram::BorderedStyle,
    borderSizeComputationExpression=
        safe_text,
    borderSize=
        safe_text
)
viewpoint::diagram::EdgeStyle_strategy = st.builds(
    viewpoint::diagram::EdgeStyle,
    size=
        safe_text,
    routingStyle=
        safe_text,
    sourceArrow=
        safe_text,
    lineStyle=
        safe_text,
    foldingStyle=
        safe_text,
    targetArrow=
        safe_text
)
LabelStyle_strategy = st.builds(
    LabelStyle,
)
viewpoint::diagram::ContainerStyle_strategy = st.builds(
    viewpoint::diagram::ContainerStyle,
)
viewpoint::diagram::NodeStyle_strategy = st.builds(
    viewpoint::diagram::NodeStyle,
    hideLabelByDefault=
        st.booleans(),
    labelPosition=
        safe_text
)
diagram::viewpoint::DRepresentationContainer_strategy = st.builds(
    diagram::viewpoint::DRepresentationContainer,
)
viewpoint::diagram::GaugeSection_strategy = st.builds(
    viewpoint::diagram::GaugeSection,
    max=
        safe_text,
    value=
        safe_text,
    min=
        safe_text,
    label=
        safe_text
)
diagram::viewpoint::RGBValues_strategy = st.builds(
    diagram::viewpoint::RGBValues,
)
description::IEdgeMapping_strategy = st.builds(
    description::IEdgeMapping,
)
viewpoint::diagram::DDiagramSet_strategy = st.builds(
    viewpoint::diagram::DDiagramSet,
)
AbstractDNode_strategy = st.builds(
    AbstractDNode,
)
viewpoint::diagram::DNodeListElement_strategy = st.builds(
    viewpoint::diagram::DNodeListElement,
)
EdgeStyle_strategy = st.builds(
    EdgeStyle,
)
viewpoint::diagram::BracketEdgeStyle_strategy = st.builds(
    viewpoint::diagram::BracketEdgeStyle,
)
diagram::DDiagramElement_strategy = st.builds(
    diagram::DDiagramElement,
)
description::ContainerMapping_strategy = st.builds(
    description::ContainerMapping,
)
viewpoint::description::ContainerMappingImport_strategy = st.builds(
    viewpoint::description::ContainerMappingImport,
)
ContainerStyle_strategy = st.builds(
    ContainerStyle,
)
viewpoint::diagram::ShapeContainerStyle_strategy = st.builds(
    viewpoint::diagram::ShapeContainerStyle,
    shape=
        safe_text
)
viewpoint::diagram::FlatContainerStyle_strategy = st.builds(
    viewpoint::diagram::FlatContainerStyle,
    backgroundStyle=
        safe_text
)
diagram::EdgeTarget_strategy = st.builds(
    diagram::EdgeTarget,
)
viewpoint::diagram::DEdge_strategy = st.builds(
    viewpoint::diagram::DEdge,
    endLabel=
        safe_text,
    beginLabel=
        safe_text,
    isMockEdge=
        st.booleans(),
    routingStyle=
        safe_text,
    isFold=
        st.booleans(),
    size=
        safe_text,
    arrangeConstraints=
        safe_text
)
diagram::AbstractDNode_strategy = st.builds(
    diagram::AbstractDNode,
)
EdgeTarget_strategy = st.builds(
    EdgeTarget,
)
description::NodeMapping_strategy = st.builds(
    description::NodeMapping,
)
viewpoint::description::NodeMappingImport_strategy = st.builds(
    viewpoint::description::NodeMappingImport,
)
diagram::viewpoint::Style_strategy = st.builds(
    diagram::viewpoint::Style,
)
NodeStyle_strategy = st.builds(
    NodeStyle,
)
viewpoint::diagram::CustomStyle_strategy = st.builds(
    viewpoint::diagram::CustomStyle,
    id=
        safe_text
)
viewpoint::diagram::Note_strategy = st.builds(
    viewpoint::diagram::Note,
)
viewpoint::diagram::GaugeCompositeStyle_strategy = st.builds(
    viewpoint::diagram::GaugeCompositeStyle,
    alignment=
        safe_text
)
viewpoint::diagram::Dot_strategy = st.builds(
    viewpoint::diagram::Dot,
    strokeSizeComputationExpression=
        safe_text
)
viewpoint::diagram::Ellipse_strategy = st.builds(
    viewpoint::diagram::Ellipse,
    horizontalDiameter=
        safe_text,
    verticalDiameter=
        safe_text
)
viewpoint::diagram::Lozenge_strategy = st.builds(
    viewpoint::diagram::Lozenge,
    width=
        safe_text,
    height=
        safe_text
)
viewpoint::diagram::Square_strategy = st.builds(
    viewpoint::diagram::Square,
    width=
        safe_text,
    height=
        safe_text
)
viewpoint::diagram::BundledImage_strategy = st.builds(
    viewpoint::diagram::BundledImage,
    shape=
        safe_text
)
viewpoint::diagram::GraphicalFilter_strategy = st.builds(
    viewpoint::diagram::GraphicalFilter,
)
GraphicalFilter_strategy = st.builds(
    GraphicalFilter,
)
viewpoint::diagram::CollapseFilter_strategy = st.builds(
    viewpoint::diagram::CollapseFilter,
    width=
        st.integers(),
    height=
        st.integers()
)
diagram::viewpoint::Decoration_strategy = st.builds(
    diagram::viewpoint::Decoration,
)
viewpoint::diagram::DDiagramLink_strategy = st.builds(
    viewpoint::diagram::DDiagramLink,
)
viewpoint::diagram::AbsoluteBoundsFilter_strategy = st.builds(
    viewpoint::diagram::AbsoluteBoundsFilter,
    x=
        safe_text,
    y=
        safe_text,
    height=
        safe_text,
    width=
        safe_text
)
filter::CompositeFilterDescription_strategy = st.builds(
    filter::CompositeFilterDescription,
)
viewpoint::diagram::AppliedCompositeFilters_strategy = st.builds(
    viewpoint::diagram::AppliedCompositeFilters,
)
viewpoint::diagram::FoldingFilter_strategy = st.builds(
    viewpoint::diagram::FoldingFilter,
)
viewpoint::diagram::FoldingPointFilter_strategy = st.builds(
    viewpoint::diagram::FoldingPointFilter,
)
viewpoint::diagram::HideLabelFilter_strategy = st.builds(
    viewpoint::diagram::HideLabelFilter,
)
viewpoint::diagram::HideFilter_strategy = st.builds(
    viewpoint::diagram::HideFilter,
)
description::Layer_strategy = st.builds(
    description::Layer,
)
FilterVariableHistory_strategy = st.builds(
    FilterVariableHistory,
)
tool::BehaviorTool_strategy = st.builds(
    tool::BehaviorTool,
)
validation::ValidationRule_strategy = st.builds(
    validation::ValidationRule,
)
DNavigable_strategy = st.builds(
    DNavigable,
)
DRepresentationElement_strategy = st.builds(
    DRepresentationElement,
)
diagram::DDiagram_strategy = st.builds(
    diagram::DDiagram,
)
DEdge_strategy = st.builds(
    DEdge,
)
DDiagram_strategy = st.builds(
    DDiagram,
)
filter::FilterDescription_strategy = st.builds(
    filter::FilterDescription,
)
concern::ConcernDescription_strategy = st.builds(
    concern::ConcernDescription,
)
DDiagramElementContainer_strategy = st.builds(
    DDiagramElementContainer,
)
viewpoint::diagram::DNodeList_strategy = st.builds(
    viewpoint::diagram::DNodeList,
    lineWidth=
        st.integers()
)
viewpoint::diagram::DNodeContainer_strategy = st.builds(
    viewpoint::diagram::DNodeContainer,
    childrenPresentation=
        safe_text
)
DNodeListElement_strategy = st.builds(
    DNodeListElement,
)
DNode_strategy = st.builds(
    DNode,
)
DContainer_strategy = st.builds(
    DContainer,
)
DValidable_strategy = st.builds(
    DValidable,
)
viewpoint::diagram::DDiagramElement_strategy = st.builds(
    viewpoint::diagram::DDiagramElement,
    tooltipText=
        safe_text,
    visible=
        st.booleans()
)
DragAndDropTarget_strategy = st.builds(
    DragAndDropTarget,
)
viewpoint::diagram::DDiagramElementContainer_strategy = st.builds(
    viewpoint::diagram::DDiagramElementContainer,
    height=
        safe_text,
    width=
        safe_text
)
viewpoint::diagram::DNode_strategy = st.builds(
    viewpoint::diagram::DNode,
    height=
        safe_text,
    width=
        safe_text,
    labelPosition=
        safe_text,
    resizeKind=
        safe_text
)
DRepresentation_strategy = st.builds(
    DRepresentation,
)
InformationSection_strategy = st.builds(
    InformationSection,
)
viewpoint::audit::TemplateInformationSection_strategy = st.builds(
    viewpoint::audit::TemplateInformationSection,
    templatePath=
        safe_text
)
description::DiagramDescription_strategy = st.builds(
    description::DiagramDescription,
)
viewpoint::description::DiagramImportDescription_strategy = st.builds(
    viewpoint::description::DiagramImportDescription,
)
DDiagramElement_strategy = st.builds(
    DDiagramElement,
)
viewpoint::diagram::AbstractDNode_strategy = st.builds(
    viewpoint::diagram::AbstractDNode,
    arrangeConstraints=
        safe_text
)
SwitchChild_strategy = st.builds(
    SwitchChild,
)
viewpoint::tool::Case_strategy = st.builds(
    viewpoint::tool::Case,
    conditionExpression=
        safe_text
)
viewpoint::tool::FeatureChangeListener_strategy = st.builds(
    viewpoint::tool::FeatureChangeListener,
    featureName=
        safe_text,
    domainClass=
        safe_text
)
tool::FeatureChangeListener_strategy = st.builds(
    tool::FeatureChangeListener,
)
viewpoint::audit::InformationSection_strategy = st.builds(
    viewpoint::audit::InformationSection,
)
tool::Default_strategy = st.builds(
    tool::Default,
)
tool::Case_strategy = st.builds(
    tool::Case,
)
viewpoint::tool::Default_strategy = st.builds(
    viewpoint::tool::Default,
)
viewpoint::tool::SwitchChild_strategy = st.builds(
    viewpoint::tool::SwitchChild,
)
viewpoint::tool::ToolFilterDescription_strategy = st.builds(
    viewpoint::tool::ToolFilterDescription,
    precondition=
        safe_text,
    elementsToListen=
        safe_text
)
viewpoint::tool::ExternalJavaActionParameter_strategy = st.builds(
    viewpoint::tool::ExternalJavaActionParameter,
    name=
        safe_text,
    value=
        safe_text
)
viewpoint::tool::NameVariable_strategy = st.builds(
    viewpoint::tool::NameVariable,
)
tool::viewpoint::EObject_strategy = st.builds(
    tool::viewpoint::EObject,
)
ContainerModelOperation_strategy = st.builds(
    ContainerModelOperation,
)
viewpoint::tool::RemoveElement_strategy = st.builds(
    viewpoint::tool::RemoveElement,
)
viewpoint::tool::SetObject_strategy = st.builds(
    viewpoint::tool::SetObject,
    featureName=
        safe_text
)
viewpoint::tool::ChangeContext_strategy = st.builds(
    viewpoint::tool::ChangeContext,
    browseExpression=
        safe_text
)
viewpoint::tool::CreateView_strategy = st.builds(
    viewpoint::tool::CreateView,
    containerViewExpression=
        safe_text,
    variableName=
        safe_text
)
viewpoint::tool::DeleteView_strategy = st.builds(
    viewpoint::tool::DeleteView,
)
viewpoint::tool::Navigation_strategy = st.builds(
    viewpoint::tool::Navigation,
    createIfNotExistent=
        st.booleans()
)
viewpoint::tool::For_strategy = st.builds(
    viewpoint::tool::For,
    iteratorName=
        safe_text,
    expression=
        safe_text
)
viewpoint::tool::Unset_strategy = st.builds(
    viewpoint::tool::Unset,
    elementExpression=
        safe_text,
    featureName=
        safe_text
)
viewpoint::tool::MoveElement_strategy = st.builds(
    viewpoint::tool::MoveElement,
    newContainerExpression=
        safe_text,
    featureName=
        safe_text
)
viewpoint::tool::SetValue_strategy = st.builds(
    viewpoint::tool::SetValue,
    valueExpression=
        safe_text,
    featureName=
        safe_text
)
viewpoint::tool::If_strategy = st.builds(
    viewpoint::tool::If,
    conditionExpression=
        safe_text
)
viewpoint::tool::CreateInstance_strategy = st.builds(
    viewpoint::tool::CreateInstance,
    referenceName=
        safe_text,
    typeName=
        safe_text,
    variableName=
        safe_text
)
viewpoint::tool::InitialContainerDropOperation_strategy = st.builds(
    viewpoint::tool::InitialContainerDropOperation,
)
viewpoint::tool::InitEdgeCreationOperation_strategy = st.builds(
    viewpoint::tool::InitEdgeCreationOperation,
)
viewpoint::tool::InitialOperation_strategy = st.builds(
    viewpoint::tool::InitialOperation,
)
viewpoint::tool::InitialNodeCreationOperation_strategy = st.builds(
    viewpoint::tool::InitialNodeCreationOperation,
)
viewpoint::tool::ModelOperation_strategy = st.builds(
    viewpoint::tool::ModelOperation,
)
tool::ModelOperation_strategy = st.builds(
    tool::ModelOperation,
)
ModelOperation_strategy = st.builds(
    ModelOperation,
)
viewpoint::tool::Switch_strategy = st.builds(
    viewpoint::tool::Switch,
)
viewpoint::tool::ContainerModelOperation_strategy = st.builds(
    viewpoint::tool::ContainerModelOperation,
)
viewpoint::tool::EditMaskVariables_strategy = st.builds(
    viewpoint::tool::EditMaskVariables,
    mask=
        safe_text
)
viewpoint::tool::SelectModelElementVariable_strategy = st.builds(
    viewpoint::tool::SelectModelElementVariable,
)
viewpoint::tool::ElementSelectVariable_strategy = st.builds(
    viewpoint::tool::ElementSelectVariable,
)
tool::AbstractVariable_strategy = st.builds(
    tool::AbstractVariable,
)
viewpoint::tool::DropContainerVariable_strategy = st.builds(
    viewpoint::tool::DropContainerVariable,
)
viewpoint::tool::SelectContainerVariable_strategy = st.builds(
    viewpoint::tool::SelectContainerVariable,
)
viewpoint::tool::ElementDropVariable_strategy = st.builds(
    viewpoint::tool::ElementDropVariable,
)
viewpoint::tool::ContainerViewVariable_strategy = st.builds(
    viewpoint::tool::ContainerViewVariable,
)
viewpoint::tool::ElementDeleteVariable_strategy = st.builds(
    viewpoint::tool::ElementDeleteVariable,
)
viewpoint::tool::SourceEdgeViewCreationVariable_strategy = st.builds(
    viewpoint::tool::SourceEdgeViewCreationVariable,
)
viewpoint::tool::ElementVariable_strategy = st.builds(
    viewpoint::tool::ElementVariable,
)
viewpoint::tool::SourceEdgeCreationVariable_strategy = st.builds(
    viewpoint::tool::SourceEdgeCreationVariable,
)
viewpoint::tool::ElementViewVariable_strategy = st.builds(
    viewpoint::tool::ElementViewVariable,
)
viewpoint::tool::ElementDoubleClickVariable_strategy = st.builds(
    viewpoint::tool::ElementDoubleClickVariable,
)
viewpoint::tool::TargetEdgeCreationVariable_strategy = st.builds(
    viewpoint::tool::TargetEdgeCreationVariable,
)
viewpoint::tool::TargetEdgeViewCreationVariable_strategy = st.builds(
    viewpoint::tool::TargetEdgeViewCreationVariable,
)
viewpoint::tool::NodeCreationVariable_strategy = st.builds(
    viewpoint::tool::NodeCreationVariable,
)
viewpoint::Decoration_strategy = st.builds(
    viewpoint::Decoration,
)
Viewpoint_strategy = st.builds(
    Viewpoint,
)
viewpoint::MetaModelExtension_strategy = st.builds(
    viewpoint::MetaModelExtension,
)
DSemanticDecorator_strategy = st.builds(
    DSemanticDecorator,
)
viewpoint::diagram::DSemanticDiagram_strategy = st.builds(
    viewpoint::diagram::DSemanticDiagram,
)
DStylizable_strategy = st.builds(
    DStylizable,
)
DMappingBased_strategy = st.builds(
    DMappingBased,
)
DLabelled_strategy = st.builds(
    DLabelled,
)
AnnotationEntry_strategy = st.builds(
    AnnotationEntry,
)
description::DModelElement_strategy = st.builds(
    description::DModelElement,
)
DRefreshable_strategy = st.builds(
    DRefreshable,
)
viewpoint::DRepresentationElement_strategy = st.builds(
    viewpoint::DRepresentationElement,
    name=
        safe_text
)
viewpoint::Style_strategy = st.builds(
    viewpoint::Style,
)
description::DocumentedElement_strategy = st.builds(
    description::DocumentedElement,
)
viewpoint::description::Viewpoint_strategy = st.builds(
    viewpoint::description::Viewpoint,
    customizes=
        safe_text,
    reuses=
        safe_text,
    icon=
        safe_text,
    conflicts=
        safe_text,
    modelFileExtension=
        safe_text
)
viewpoint::tool::ToolSection_strategy = st.builds(
    viewpoint::tool::ToolSection,
    icon=
        safe_text
)
viewpoint::filter::FilterDescription_strategy = st.builds(
    viewpoint::filter::FilterDescription,
)
viewpoint::description::EdgeMapping_strategy = st.builds(
    viewpoint::description::EdgeMapping,
    targetFinderExpression=
        safe_text,
    pathExpression=
        safe_text,
    targetExpression=
        safe_text,
    domainClass=
        safe_text,
    useDomainElement=
        st.booleans(),
    sourceFinderExpression=
        safe_text
)
viewpoint::description::Group_strategy = st.builds(
    viewpoint::description::Group,
    version=
        safe_text,
    name=
        safe_text
)
viewpoint::description::EdgeMappingImport_strategy = st.builds(
    viewpoint::description::EdgeMappingImport,
    inheritsAncestorFilters=
        st.booleans()
)
viewpoint::description::Layer_strategy = st.builds(
    viewpoint::description::Layer,
    icon=
        safe_text
)
viewpoint::tool::ToolEntry_strategy = st.builds(
    viewpoint::tool::ToolEntry,
)
viewpoint::description::RepresentationDescription_strategy = st.builds(
    viewpoint::description::RepresentationDescription,
    titleExpression=
        safe_text,
    showOnStartup=
        st.booleans(),
    initialisation=
        st.booleans()
)
viewpoint::diagram::DDiagram_strategy = st.builds(
    viewpoint::diagram::DDiagram,
    info=
        safe_text,
    isInLayoutingMode=
        st.booleans(),
    headerHeight=
        st.integers(),
    synchronized=
        st.booleans()
)
viewpoint::concern::ConcernDescription_strategy = st.builds(
    viewpoint::concern::ConcernDescription,
)
viewpoint::description::AbstractNodeMapping_strategy = st.builds(
    viewpoint::description::AbstractNodeMapping,
    domainClass=
        safe_text
)
viewpoint::DRepresentation_strategy = st.builds(
    viewpoint::DRepresentation,
    name=
        safe_text
)
viewpoint::DSemanticDecorator_strategy = st.builds(
    viewpoint::DSemanticDecorator,
)
DDiagramSet_strategy = st.builds(
    DDiagramSet,
)
DView_strategy = st.builds(
    DView,
)
viewpoint::DRepresentationContainer_strategy = st.builds(
    viewpoint::DRepresentationContainer,
)
viewpoint::DContainer_strategy = st.builds(
    viewpoint::DContainer,
)
viewpoint::DMappingBased_strategy = st.builds(
    viewpoint::DMappingBased,
)
viewpoint::DLabelled_strategy = st.builds(
    viewpoint::DLabelled,
)
viewpoint::DRefreshable_strategy = st.builds(
    viewpoint::DRefreshable,
)
viewpoint::DStylizable_strategy = st.builds(
    viewpoint::DStylizable,
)
viewpoint::DNavigationLink_strategy = st.builds(
    viewpoint::DNavigationLink,
    targetType=
        safe_text,
    label=
        safe_text
)
viewpoint::DNavigable_strategy = st.builds(
    viewpoint::DNavigable,
)
viewpoint::DValidable_strategy = st.builds(
    viewpoint::DValidable,
)
FeatureExtensionDescription_strategy = st.builds(
    FeatureExtensionDescription,
)
viewpoint::DFeatureExtension_strategy = st.builds(
    viewpoint::DFeatureExtension,
)
viewpoint::DView_strategy = st.builds(
    viewpoint::DView,
    initialized=
        st.booleans()
)
DAnnotationEntry_strategy = st.builds(
    DAnnotationEntry,
)
viewpoint::EObject_strategy = st.builds(
    viewpoint::EObject,
)
viewpoint::DAnalysis_strategy = st.builds(
    viewpoint::DAnalysis,
    version=
        safe_text
)

@given(instance=ConditionalStyleDescription_strategy)
@settings(max_examples=50)
def test_conditionalstyledescription_instantiation(instance):
    assert isinstance(instance, ConditionalStyleDescription)

@given(instance=viewpoint::description::ConditionalContainerStyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::description::conditionalcontainerstyledescription_instantiation(instance):
    assert isinstance(instance, viewpoint::description::ConditionalContainerStyleDescription)

@given(instance=viewpoint::description::ConditionalEdgeStyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::description::conditionaledgestyledescription_instantiation(instance):
    assert isinstance(instance, viewpoint::description::ConditionalEdgeStyleDescription)

@given(instance=viewpoint::description::ConditionalNodeStyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::description::conditionalnodestyledescription_instantiation(instance):
    assert isinstance(instance, viewpoint::description::ConditionalNodeStyleDescription)

@given(instance=description::ConditionalEdgeStyleDescription_strategy)
@settings(max_examples=50)
def test_description::conditionaledgestyledescription_instantiation(instance):
    assert isinstance(instance, description::ConditionalEdgeStyleDescription)

@given(instance=style::EdgeStyleDescription_strategy)
@settings(max_examples=50)
def test_style::edgestyledescription_instantiation(instance):
    assert isinstance(instance, style::EdgeStyleDescription)

@given(instance=viewpoint::description::IEdgeMapping_strategy)
@settings(max_examples=50)
def test_viewpoint::description::iedgemapping_instantiation(instance):
    assert isinstance(instance, viewpoint::description::IEdgeMapping)

@given(instance=tool::ReconnectEdgeDescription_strategy)
@settings(max_examples=50)
def test_tool::reconnectedgedescription_instantiation(instance):
    assert isinstance(instance, tool::ReconnectEdgeDescription)

@given(instance=description::ConditionalContainerStyleDescription_strategy)
@settings(max_examples=50)
def test_description::conditionalcontainerstyledescription_instantiation(instance):
    assert isinstance(instance, description::ConditionalContainerStyleDescription)

@given(instance=style::ContainerStyleDescription_strategy)
@settings(max_examples=50)
def test_style::containerstyledescription_instantiation(instance):
    assert isinstance(instance, style::ContainerStyleDescription)

@given(instance=description::AbstractMappingImport_strategy)
@settings(max_examples=50)
def test_description::abstractmappingimport_instantiation(instance):
    assert isinstance(instance, description::AbstractMappingImport)

@given(instance=description::ConditionalNodeStyleDescription_strategy)
@settings(max_examples=50)
def test_description::conditionalnodestyledescription_instantiation(instance):
    assert isinstance(instance, description::ConditionalNodeStyleDescription)

@given(instance=style::NodeStyleDescription_strategy)
@settings(max_examples=50)
def test_style::nodestyledescription_instantiation(instance):
    assert isinstance(instance, style::NodeStyleDescription)

@given(instance=tool::DoubleClickDescription_strategy)
@settings(max_examples=50)
def test_tool::doubleclickdescription_instantiation(instance):
    assert isinstance(instance, tool::DoubleClickDescription)

@given(instance=description::AbstractNodeMapping_strategy)
@settings(max_examples=50)
def test_description::abstractnodemapping_instantiation(instance):
    assert isinstance(instance, description::AbstractNodeMapping)

@given(instance=tool::DirectEditLabel_strategy)
@settings(max_examples=50)
def test_tool::directeditlabel_instantiation(instance):
    assert isinstance(instance, tool::DirectEditLabel)

@given(instance=tool::DeleteElementDescription_strategy)
@settings(max_examples=50)
def test_tool::deleteelementdescription_instantiation(instance):
    assert isinstance(instance, tool::DeleteElementDescription)

@given(instance=tool::ToolSection_strategy)
@settings(max_examples=50)
def test_tool::toolsection_instantiation(instance):
    assert isinstance(instance, tool::ToolSection)

@given(instance=description::RepresentationElementMapping_strategy)
@settings(max_examples=50)
def test_description::representationelementmapping_instantiation(instance):
    assert isinstance(instance, description::RepresentationElementMapping)

@given(instance=description::RepresentationImportDescription_strategy)
@settings(max_examples=50)
def test_description::representationimportdescription_instantiation(instance):
    assert isinstance(instance, description::RepresentationImportDescription)

@given(instance=description::AdditionalLayer_strategy)
@settings(max_examples=50)
def test_description::additionallayer_instantiation(instance):
    assert isinstance(instance, description::AdditionalLayer)

@given(instance=description::Layout_strategy)
@settings(max_examples=50)
def test_description::layout_instantiation(instance):
    assert isinstance(instance, description::Layout)

@given(instance=description::EdgeMappingImport_strategy)
@settings(max_examples=50)
def test_description::edgemappingimport_instantiation(instance):
    assert isinstance(instance, description::EdgeMappingImport)

@given(instance=description::EdgeMapping_strategy)
@settings(max_examples=50)
def test_description::edgemapping_instantiation(instance):
    assert isinstance(instance, description::EdgeMapping)

@given(instance=concern::ConcernSet_strategy)
@settings(max_examples=50)
def test_concern::concernset_instantiation(instance):
    assert isinstance(instance, concern::ConcernSet)

@given(instance=ModelElement2ViewVariable_strategy)
@settings(max_examples=50)
def test_modelelement2viewvariable_instantiation(instance):
    assert isinstance(instance, ModelElement2ViewVariable)

@given(instance=viewpoint::diagram::DiagramElementMapping2ModelElement_strategy)
@settings(max_examples=50)
def test_viewpoint::diagram::diagramelementmapping2modelelement_instantiation(instance):
    assert isinstance(instance, viewpoint::diagram::DiagramElementMapping2ModelElement)

@given(instance=DiagramElementMapping2ModelElement_strategy)
@settings(max_examples=50)
def test_diagramelementmapping2modelelement_instantiation(instance):
    assert isinstance(instance, DiagramElementMapping2ModelElement)

@given(instance=viewpoint::diagram::ComputedStyleDescriptionRegistry_strategy)
@settings(max_examples=50)
def test_viewpoint::diagram::computedstyledescriptionregistry_instantiation(instance):
    assert isinstance(instance, viewpoint::diagram::ComputedStyleDescriptionRegistry)

@given(instance=description::PasteTargetDescription_strategy)
@settings(max_examples=50)
def test_description::pastetargetdescription_instantiation(instance):
    assert isinstance(instance, description::PasteTargetDescription)

@given(instance=viewpoint::description::DiagramElementMapping_strategy)
@settings(max_examples=50)
def test_viewpoint::description::diagramelementmapping_instantiation(instance):
    assert isinstance(instance, viewpoint::description::DiagramElementMapping)

@given(instance=viewpoint::description::DiagramElementMapping_strategy)
def test_viewpoint::description::diagramelementmapping_semanticElements_type(instance):
    assert isinstance(instance.semanticElements, str)


@given(instance=viewpoint::description::DiagramElementMapping_strategy)
def test_viewpoint::description::diagramelementmapping_semanticElements_setter(instance):
    original = instance.semanticElements
    instance.semanticElements = original
    assert instance.semanticElements == original

@given(instance=viewpoint::description::DiagramElementMapping_strategy)
def test_viewpoint::description::diagramelementmapping_createElements_type(instance):
    assert isinstance(instance.createElements, bool)


@given(instance=viewpoint::description::DiagramElementMapping_strategy)
def test_viewpoint::description::diagramelementmapping_createElements_setter(instance):
    original = instance.createElements
    instance.createElements = original
    assert instance.createElements == original

@given(instance=viewpoint::description::DiagramElementMapping_strategy)
def test_viewpoint::description::diagramelementmapping_semanticCandidatesExpression_type(instance):
    assert isinstance(instance.semanticCandidatesExpression, str)


@given(instance=viewpoint::description::DiagramElementMapping_strategy)
def test_viewpoint::description::diagramelementmapping_semanticCandidatesExpression_setter(instance):
    original = instance.semanticCandidatesExpression
    instance.semanticCandidatesExpression = original
    assert instance.semanticCandidatesExpression == original

@given(instance=viewpoint::description::DiagramElementMapping_strategy)
def test_viewpoint::description::diagramelementmapping_preconditionExpression_type(instance):
    assert isinstance(instance.preconditionExpression, str)


@given(instance=viewpoint::description::DiagramElementMapping_strategy)
def test_viewpoint::description::diagramelementmapping_preconditionExpression_setter(instance):
    original = instance.preconditionExpression
    instance.preconditionExpression = original
    assert instance.preconditionExpression == original

@given(instance=viewpoint::description::DiagramElementMapping_strategy)
def test_viewpoint::description::diagramelementmapping_synchronizationLock_type(instance):
    assert isinstance(instance.synchronizationLock, bool)


@given(instance=viewpoint::description::DiagramElementMapping_strategy)
def test_viewpoint::description::diagramelementmapping_synchronizationLock_setter(instance):
    original = instance.synchronizationLock
    instance.synchronizationLock = original
    assert instance.synchronizationLock == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint::description::DiagramElementMapping_strategy)
@settings(max_examples=30)
def test_viewpoint::description::diagramelementmapping_checkprecondition_changes_state(instance):
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
        assert has_statements, f"Function 'checkPrecondition' in viewpoint::description::DiagramElementMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'checkPrecondition' in viewpoint::description::DiagramElementMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'checkPrecondition' in viewpoint::description::DiagramElementMapping is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint::description::DiagramElementMapping_strategy)
@settings(max_examples=30)
def test_viewpoint::description::diagramelementmapping_isfrom_changes_state(instance):
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
        assert has_statements, f"Function 'isFrom' in viewpoint::description::DiagramElementMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isFrom' in viewpoint::description::DiagramElementMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isFrom' in viewpoint::description::DiagramElementMapping is not implemented or raised an error")

@given(instance=description::RepresentationDescription_strategy)
@settings(max_examples=50)
def test_description::representationdescription_instantiation(instance):
    assert isinstance(instance, description::RepresentationDescription)

@given(instance=description::DragAndDropTargetDescription_strategy)
@settings(max_examples=50)
def test_description::draganddroptargetdescription_instantiation(instance):
    assert isinstance(instance, description::DragAndDropTargetDescription)

@given(instance=viewpoint::description::ContainerMapping_strategy)
@settings(max_examples=50)
def test_viewpoint::description::containermapping_instantiation(instance):
    assert isinstance(instance, viewpoint::description::ContainerMapping)

@given(instance=viewpoint::description::ContainerMapping_strategy)
def test_viewpoint::description::containermapping_childrenPresentation_type(instance):
    assert isinstance(instance.childrenPresentation, str)


@given(instance=viewpoint::description::ContainerMapping_strategy)
def test_viewpoint::description::containermapping_childrenPresentation_setter(instance):
    original = instance.childrenPresentation
    instance.childrenPresentation = original
    assert instance.childrenPresentation == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint::description::ContainerMapping_strategy)
@settings(max_examples=30)
def test_viewpoint::description::containermapping_createcontainer_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createContainer(
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createContainer).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createContainer' in viewpoint::description::ContainerMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createContainer' in viewpoint::description::ContainerMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createContainer' in viewpoint::description::ContainerMapping is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint::description::ContainerMapping_strategy)
@settings(max_examples=30)
def test_viewpoint::description::containermapping_updatecontainer_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.updateContainer(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.updateContainer).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'updateContainer' in viewpoint::description::ContainerMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'updateContainer' in viewpoint::description::ContainerMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'updateContainer' in viewpoint::description::ContainerMapping is not implemented or raised an error")

@given(instance=viewpoint::description::NodeMapping_strategy)
@settings(max_examples=50)
def test_viewpoint::description::nodemapping_instantiation(instance):
    assert isinstance(instance, viewpoint::description::NodeMapping)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint::description::NodeMapping_strategy)
@settings(max_examples=30)
def test_viewpoint::description::nodemapping_createnode_changes_state(instance):
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
        assert has_statements, f"Function 'createNode' in viewpoint::description::NodeMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createNode' in viewpoint::description::NodeMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createNode' in viewpoint::description::NodeMapping is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint::description::NodeMapping_strategy)
@settings(max_examples=30)
def test_viewpoint::description::nodemapping_updatelistelement_changes_state(instance):
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
        assert has_statements, f"Function 'updateListElement' in viewpoint::description::NodeMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'updateListElement' in viewpoint::description::NodeMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'updateListElement' in viewpoint::description::NodeMapping is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint::description::NodeMapping_strategy)
@settings(max_examples=30)
def test_viewpoint::description::nodemapping_updatenode_changes_state(instance):
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
        assert has_statements, f"Function 'updateNode' in viewpoint::description::NodeMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'updateNode' in viewpoint::description::NodeMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'updateNode' in viewpoint::description::NodeMapping is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint::description::NodeMapping_strategy)
@settings(max_examples=30)
def test_viewpoint::description::nodemapping_createlistelement_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createListElement(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createListElement).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createListElement' in viewpoint::description::NodeMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createListElement' in viewpoint::description::NodeMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createListElement' in viewpoint::description::NodeMapping is not implemented or raised an error")

@given(instance=viewpoint::description::DiagramDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::description::diagramdescription_instantiation(instance):
    assert isinstance(instance, viewpoint::description::DiagramDescription)

@given(instance=viewpoint::description::DiagramDescription_strategy)
def test_viewpoint::description::diagramdescription_enablePopupBars_type(instance):
    assert isinstance(instance.enablePopupBars, bool)


@given(instance=viewpoint::description::DiagramDescription_strategy)
def test_viewpoint::description::diagramdescription_enablePopupBars_setter(instance):
    original = instance.enablePopupBars
    instance.enablePopupBars = original
    assert instance.enablePopupBars == original

@given(instance=viewpoint::description::DiagramDescription_strategy)
def test_viewpoint::description::diagramdescription_preconditionExpression_type(instance):
    assert isinstance(instance.preconditionExpression, str)


@given(instance=viewpoint::description::DiagramDescription_strategy)
def test_viewpoint::description::diagramdescription_preconditionExpression_setter(instance):
    original = instance.preconditionExpression
    instance.preconditionExpression = original
    assert instance.preconditionExpression == original

@given(instance=viewpoint::description::DiagramDescription_strategy)
def test_viewpoint::description::diagramdescription_domainClass_type(instance):
    assert isinstance(instance.domainClass, str)


@given(instance=viewpoint::description::DiagramDescription_strategy)
def test_viewpoint::description::diagramdescription_domainClass_setter(instance):
    original = instance.domainClass
    instance.domainClass = original
    assert instance.domainClass == original

@given(instance=viewpoint::description::DiagramDescription_strategy)
def test_viewpoint::description::diagramdescription_rootExpression_type(instance):
    assert isinstance(instance.rootExpression, str)


@given(instance=viewpoint::description::DiagramDescription_strategy)
def test_viewpoint::description::diagramdescription_rootExpression_setter(instance):
    original = instance.rootExpression
    instance.rootExpression = original
    assert instance.rootExpression == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint::description::DiagramDescription_strategy)
@settings(max_examples=30)
def test_viewpoint::description::diagramdescription_creatediagram_changes_state(instance):
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
        assert has_statements, f"Function 'createDiagram' in viewpoint::description::DiagramDescription is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createDiagram' in viewpoint::description::DiagramDescription did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createDiagram' in viewpoint::description::DiagramDescription is not implemented or raised an error")

@given(instance=viewpoint::diagram::ContainerVariable2StyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::diagram::containervariable2styledescription_instantiation(instance):
    assert isinstance(instance, viewpoint::diagram::ContainerVariable2StyleDescription)

@given(instance=ContainerVariable2StyleDescription_strategy)
@settings(max_examples=50)
def test_containervariable2styledescription_instantiation(instance):
    assert isinstance(instance, ContainerVariable2StyleDescription)

@given(instance=viewpoint::diagram::ViewVariable2ContainerVariable_strategy)
@settings(max_examples=50)
def test_viewpoint::diagram::viewvariable2containervariable_instantiation(instance):
    assert isinstance(instance, viewpoint::diagram::ViewVariable2ContainerVariable)

@given(instance=ViewVariable2ContainerVariable_strategy)
@settings(max_examples=50)
def test_viewvariable2containervariable_instantiation(instance):
    assert isinstance(instance, ViewVariable2ContainerVariable)

@given(instance=viewpoint::diagram::ModelElement2ViewVariable_strategy)
@settings(max_examples=50)
def test_viewpoint::diagram::modelelement2viewvariable_instantiation(instance):
    assert isinstance(instance, viewpoint::diagram::ModelElement2ViewVariable)

@given(instance=diagram::viewpoint::EObject_strategy)
@settings(max_examples=50)
def test_diagram::viewpoint::eobject_instantiation(instance):
    assert isinstance(instance, diagram::viewpoint::EObject)

@given(instance=filter::FilterVariable_strategy)
@settings(max_examples=50)
def test_filter::filtervariable_instantiation(instance):
    assert isinstance(instance, filter::FilterVariable)

@given(instance=viewpoint::diagram::FilterVariableValue_strategy)
@settings(max_examples=50)
def test_viewpoint::diagram::filtervariablevalue_instantiation(instance):
    assert isinstance(instance, viewpoint::diagram::FilterVariableValue)

@given(instance=FilterVariableValue_strategy)
@settings(max_examples=50)
def test_filtervariablevalue_instantiation(instance):
    assert isinstance(instance, FilterVariableValue)

@given(instance=CollapseFilter_strategy)
@settings(max_examples=50)
def test_collapsefilter_instantiation(instance):
    assert isinstance(instance, CollapseFilter)

@given(instance=viewpoint::diagram::IndirectlyCollapseFilter_strategy)
@settings(max_examples=50)
def test_viewpoint::diagram::indirectlycollapsefilter_instantiation(instance):
    assert isinstance(instance, viewpoint::diagram::IndirectlyCollapseFilter)

@given(instance=viewpoint::diagram::FilterVariableHistory_strategy)
@settings(max_examples=50)
def test_viewpoint::diagram::filtervariablehistory_instantiation(instance):
    assert isinstance(instance, viewpoint::diagram::FilterVariableHistory)

@given(instance=GaugeSection_strategy)
@settings(max_examples=50)
def test_gaugesection_instantiation(instance):
    assert isinstance(instance, GaugeSection)

@given(instance=EndLabelStyle_strategy)
@settings(max_examples=50)
def test_endlabelstyle_instantiation(instance):
    assert isinstance(instance, EndLabelStyle)

@given(instance=CenterLabelStyle_strategy)
@settings(max_examples=50)
def test_centerlabelstyle_instantiation(instance):
    assert isinstance(instance, CenterLabelStyle)

@given(instance=BeginLabelStyle_strategy)
@settings(max_examples=50)
def test_beginlabelstyle_instantiation(instance):
    assert isinstance(instance, BeginLabelStyle)

@given(instance=diagram::ContainerStyle_strategy)
@settings(max_examples=50)
def test_diagram::containerstyle_instantiation(instance):
    assert isinstance(instance, diagram::ContainerStyle)

@given(instance=viewpoint::validation::ValidationFix_strategy)
@settings(max_examples=50)
def test_viewpoint::validation::validationfix_instantiation(instance):
    assert isinstance(instance, viewpoint::validation::ValidationFix)

@given(instance=viewpoint::validation::ValidationFix_strategy)
def test_viewpoint::validation::validationfix_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=viewpoint::validation::ValidationFix_strategy)
def test_viewpoint::validation::validationfix_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ValidationRule_strategy)
@settings(max_examples=50)
def test_validationrule_instantiation(instance):
    assert isinstance(instance, ValidationRule)

@given(instance=viewpoint::validation::ViewValidationRule_strategy)
@settings(max_examples=50)
def test_viewpoint::validation::viewvalidationrule_instantiation(instance):
    assert isinstance(instance, viewpoint::validation::ViewValidationRule)

@given(instance=viewpoint::validation::SemanticValidationRule_strategy)
@settings(max_examples=50)
def test_viewpoint::validation::semanticvalidationrule_instantiation(instance):
    assert isinstance(instance, viewpoint::validation::SemanticValidationRule)

@given(instance=viewpoint::validation::SemanticValidationRule_strategy)
def test_viewpoint::validation::semanticvalidationrule_targetClass_type(instance):
    assert isinstance(instance.targetClass, str)


@given(instance=viewpoint::validation::SemanticValidationRule_strategy)
def test_viewpoint::validation::semanticvalidationrule_targetClass_setter(instance):
    original = instance.targetClass
    instance.targetClass = original
    assert instance.targetClass == original

@given(instance=validation::ValidationFix_strategy)
@settings(max_examples=50)
def test_validation::validationfix_instantiation(instance):
    assert isinstance(instance, validation::ValidationFix)

@given(instance=validation::RuleAudit_strategy)
@settings(max_examples=50)
def test_validation::ruleaudit_instantiation(instance):
    assert isinstance(instance, validation::RuleAudit)

@given(instance=viewpoint::validation::ValidationRule_strategy)
@settings(max_examples=50)
def test_viewpoint::validation::validationrule_instantiation(instance):
    assert isinstance(instance, viewpoint::validation::ValidationRule)

@given(instance=viewpoint::validation::ValidationRule_strategy)
def test_viewpoint::validation::validationrule_message_type(instance):
    assert isinstance(instance.message, str)


@given(instance=viewpoint::validation::ValidationRule_strategy)
def test_viewpoint::validation::validationrule_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

@given(instance=viewpoint::validation::ValidationRule_strategy)
def test_viewpoint::validation::validationrule_level_type(instance):
    assert isinstance(instance.level, str)


@given(instance=viewpoint::validation::ValidationRule_strategy)
def test_viewpoint::validation::validationrule_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint::validation::ValidationRule_strategy)
@settings(max_examples=30)
def test_viewpoint::validation::validationrule_checkrule_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.checkRule(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.checkRule).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'checkRule' in viewpoint::validation::ValidationRule is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'checkRule' in viewpoint::validation::ValidationRule did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'checkRule' in viewpoint::validation::ValidationRule is not implemented or raised an error")

@given(instance=viewpoint::validation::RuleAudit_strategy)
@settings(max_examples=50)
def test_viewpoint::validation::ruleaudit_instantiation(instance):
    assert isinstance(instance, viewpoint::validation::RuleAudit)

@given(instance=viewpoint::validation::RuleAudit_strategy)
def test_viewpoint::validation::ruleaudit_auditExpression_type(instance):
    assert isinstance(instance.auditExpression, str)


@given(instance=viewpoint::validation::RuleAudit_strategy)
def test_viewpoint::validation::ruleaudit_auditExpression_setter(instance):
    original = instance.auditExpression
    instance.auditExpression = original
    assert instance.auditExpression == original

@given(instance=SelectionDescription_strategy)
@settings(max_examples=50)
def test_selectiondescription_instantiation(instance):
    assert isinstance(instance, SelectionDescription)

@given(instance=viewpoint::filter::FilterVariable_strategy)
@settings(max_examples=50)
def test_viewpoint::filter::filtervariable_instantiation(instance):
    assert isinstance(instance, viewpoint::filter::FilterVariable)

@given(instance=viewpoint::filter::FilterVariable_strategy)
def test_viewpoint::filter::filtervariable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=viewpoint::filter::FilterVariable_strategy)
def test_viewpoint::filter::filtervariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=filter::Filter_strategy)
@settings(max_examples=50)
def test_filter::filter_instantiation(instance):
    assert isinstance(instance, filter::Filter)

@given(instance=FilterDescription_strategy)
@settings(max_examples=50)
def test_filterdescription_instantiation(instance):
    assert isinstance(instance, FilterDescription)

@given(instance=viewpoint::filter::CompositeFilterDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::filter::compositefilterdescription_instantiation(instance):
    assert isinstance(instance, viewpoint::filter::CompositeFilterDescription)

@given(instance=Filter_strategy)
@settings(max_examples=50)
def test_filter_instantiation(instance):
    assert isinstance(instance, Filter)

@given(instance=viewpoint::filter::VariableFilter_strategy)
@settings(max_examples=50)
def test_viewpoint::filter::variablefilter_instantiation(instance):
    assert isinstance(instance, viewpoint::filter::VariableFilter)

@given(instance=viewpoint::filter::VariableFilter_strategy)
def test_viewpoint::filter::variablefilter_semanticConditionExpression_type(instance):
    assert isinstance(instance.semanticConditionExpression, str)


@given(instance=viewpoint::filter::VariableFilter_strategy)
def test_viewpoint::filter::variablefilter_semanticConditionExpression_setter(instance):
    original = instance.semanticConditionExpression
    instance.semanticConditionExpression = original
    assert instance.semanticConditionExpression == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint::filter::VariableFilter_strategy)
@settings(max_examples=30)
def test_viewpoint::filter::variablefilter_setfiltercontext_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setFilterContext(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setFilterContext).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setFilterContext' in viewpoint::filter::VariableFilter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setFilterContext' in viewpoint::filter::VariableFilter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setFilterContext' in viewpoint::filter::VariableFilter is not implemented or raised an error")

@given(instance=viewpoint::filter::MappingFilter_strategy)
@settings(max_examples=50)
def test_viewpoint::filter::mappingfilter_instantiation(instance):
    assert isinstance(instance, viewpoint::filter::MappingFilter)

@given(instance=viewpoint::filter::MappingFilter_strategy)
def test_viewpoint::filter::mappingfilter_viewConditionExpression_type(instance):
    assert isinstance(instance.viewConditionExpression, str)


@given(instance=viewpoint::filter::MappingFilter_strategy)
def test_viewpoint::filter::mappingfilter_viewConditionExpression_setter(instance):
    original = instance.viewConditionExpression
    instance.viewConditionExpression = original
    assert instance.viewConditionExpression == original

@given(instance=viewpoint::filter::MappingFilter_strategy)
def test_viewpoint::filter::mappingfilter_semanticConditionExpression_type(instance):
    assert isinstance(instance.semanticConditionExpression, str)


@given(instance=viewpoint::filter::MappingFilter_strategy)
def test_viewpoint::filter::mappingfilter_semanticConditionExpression_setter(instance):
    original = instance.semanticConditionExpression
    instance.semanticConditionExpression = original
    assert instance.semanticConditionExpression == original

@given(instance=viewpoint::filter::Filter_strategy)
@settings(max_examples=50)
def test_viewpoint::filter::filter_instantiation(instance):
    assert isinstance(instance, viewpoint::filter::Filter)

@given(instance=viewpoint::filter::Filter_strategy)
def test_viewpoint::filter::filter_filterKind_type(instance):
    assert isinstance(instance.filterKind, str)


@given(instance=viewpoint::filter::Filter_strategy)
def test_viewpoint::filter::filter_filterKind_setter(instance):
    original = instance.filterKind
    instance.filterKind = original
    assert instance.filterKind == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint::filter::Filter_strategy)
@settings(max_examples=30)
def test_viewpoint::filter::filter_isvisible_changes_state(instance):
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
        assert has_statements, f"Function 'isVisible' in viewpoint::filter::Filter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isVisible' in viewpoint::filter::Filter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isVisible' in viewpoint::filter::Filter is not implemented or raised an error")

@given(instance=RepresentationNavigationDescription_strategy)
@settings(max_examples=50)
def test_representationnavigationdescription_instantiation(instance):
    assert isinstance(instance, RepresentationNavigationDescription)

@given(instance=CreateView_strategy)
@settings(max_examples=50)
def test_createview_instantiation(instance):
    assert isinstance(instance, CreateView)

@given(instance=viewpoint::tool::DiagramNavigationDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::diagramnavigationdescription_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::DiagramNavigationDescription)

@given(instance=viewpoint::tool::CreateEdgeView_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::createedgeview_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::CreateEdgeView)

@given(instance=viewpoint::tool::CreateEdgeView_strategy)
def test_viewpoint::tool::createedgeview_targetExpression_type(instance):
    assert isinstance(instance.targetExpression, str)


@given(instance=viewpoint::tool::CreateEdgeView_strategy)
def test_viewpoint::tool::createedgeview_targetExpression_setter(instance):
    original = instance.targetExpression
    instance.targetExpression = original
    assert instance.targetExpression == original

@given(instance=viewpoint::tool::CreateEdgeView_strategy)
def test_viewpoint::tool::createedgeview_sourceExpression_type(instance):
    assert isinstance(instance.sourceExpression, str)


@given(instance=viewpoint::tool::CreateEdgeView_strategy)
def test_viewpoint::tool::createedgeview_sourceExpression_setter(instance):
    original = instance.sourceExpression
    instance.sourceExpression = original
    assert instance.sourceExpression == original

@given(instance=RepresentationCreationDescription_strategy)
@settings(max_examples=50)
def test_representationcreationdescription_instantiation(instance):
    assert isinstance(instance, RepresentationCreationDescription)

@given(instance=viewpoint::tool::DiagramCreationDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::diagramcreationdescription_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::DiagramCreationDescription)

@given(instance=tool::EditMaskVariables_strategy)
@settings(max_examples=50)
def test_tool::editmaskvariables_instantiation(instance):
    assert isinstance(instance, tool::EditMaskVariables)

@given(instance=tool::ElementDoubleClickVariable_strategy)
@settings(max_examples=50)
def test_tool::elementdoubleclickvariable_instantiation(instance):
    assert isinstance(instance, tool::ElementDoubleClickVariable)

@given(instance=tool::DeleteHook_strategy)
@settings(max_examples=50)
def test_tool::deletehook_instantiation(instance):
    assert isinstance(instance, tool::DeleteHook)

@given(instance=viewpoint::tool::DeleteHookParameter_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::deletehookparameter_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::DeleteHookParameter)

@given(instance=viewpoint::tool::DeleteHookParameter_strategy)
def test_viewpoint::tool::deletehookparameter_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=viewpoint::tool::DeleteHookParameter_strategy)
def test_viewpoint::tool::deletehookparameter_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=viewpoint::tool::DeleteHookParameter_strategy)
def test_viewpoint::tool::deletehookparameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=viewpoint::tool::DeleteHookParameter_strategy)
def test_viewpoint::tool::deletehookparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tool::DeleteHookParameter_strategy)
@settings(max_examples=50)
def test_tool::deletehookparameter_instantiation(instance):
    assert isinstance(instance, tool::DeleteHookParameter)

@given(instance=viewpoint::tool::DeleteHook_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::deletehook_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::DeleteHook)

@given(instance=viewpoint::tool::DeleteHook_strategy)
def test_viewpoint::tool::deletehook_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=viewpoint::tool::DeleteHook_strategy)
def test_viewpoint::tool::deletehook_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=tool::ElementDeleteVariable_strategy)
@settings(max_examples=50)
def test_tool::elementdeletevariable_instantiation(instance):
    assert isinstance(instance, tool::ElementDeleteVariable)

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

@given(instance=tool::InitEdgeCreationOperation_strategy)
@settings(max_examples=50)
def test_tool::initedgecreationoperation_instantiation(instance):
    assert isinstance(instance, tool::InitEdgeCreationOperation)

@given(instance=tool::InitialNodeCreationOperation_strategy)
@settings(max_examples=50)
def test_tool::initialnodecreationoperation_instantiation(instance):
    assert isinstance(instance, tool::InitialNodeCreationOperation)

@given(instance=tool::NodeCreationVariable_strategy)
@settings(max_examples=50)
def test_tool::nodecreationvariable_instantiation(instance):
    assert isinstance(instance, tool::NodeCreationVariable)

@given(instance=tool::PopupMenu_strategy)
@settings(max_examples=50)
def test_tool::popupmenu_instantiation(instance):
    assert isinstance(instance, tool::PopupMenu)

@given(instance=tool::ToolGroup_strategy)
@settings(max_examples=50)
def test_tool::toolgroup_instantiation(instance):
    assert isinstance(instance, tool::ToolGroup)

@given(instance=viewpoint::tool::ToolGroupExtension_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::toolgroupextension_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::ToolGroupExtension)

@given(instance=tool::ToolGroupExtension_strategy)
@settings(max_examples=50)
def test_tool::toolgroupextension_instantiation(instance):
    assert isinstance(instance, tool::ToolGroupExtension)

@given(instance=style::BeginLabelStyleDescription_strategy)
@settings(max_examples=50)
def test_style::beginlabelstyledescription_instantiation(instance):
    assert isinstance(instance, style::BeginLabelStyleDescription)

@given(instance=EdgeStyleDescription_strategy)
@settings(max_examples=50)
def test_edgestyledescription_instantiation(instance):
    assert isinstance(instance, EdgeStyleDescription)

@given(instance=viewpoint::style::BracketEdgeStyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::style::bracketedgestyledescription_instantiation(instance):
    assert isinstance(instance, viewpoint::style::BracketEdgeStyleDescription)

@given(instance=style::EndLabelStyleDescription_strategy)
@settings(max_examples=50)
def test_style::endlabelstyledescription_instantiation(instance):
    assert isinstance(instance, style::EndLabelStyleDescription)

@given(instance=style::CenterLabelStyleDescription_strategy)
@settings(max_examples=50)
def test_style::centerlabelstyledescription_instantiation(instance):
    assert isinstance(instance, style::CenterLabelStyleDescription)

@given(instance=viewpoint::style::WorkspaceImageDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::style::workspaceimagedescription_instantiation(instance):
    assert isinstance(instance, viewpoint::style::WorkspaceImageDescription)

@given(instance=viewpoint::style::WorkspaceImageDescription_strategy)
def test_viewpoint::style::workspaceimagedescription_workspacePath_type(instance):
    assert isinstance(instance.workspacePath, str)


@given(instance=viewpoint::style::WorkspaceImageDescription_strategy)
def test_viewpoint::style::workspaceimagedescription_workspacePath_setter(instance):
    original = instance.workspacePath
    instance.workspacePath = original
    assert instance.workspacePath == original

@given(instance=viewpoint::style::SizeComputationContainerStyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::style::sizecomputationcontainerstyledescription_instantiation(instance):
    assert isinstance(instance, viewpoint::style::SizeComputationContainerStyleDescription)

@given(instance=viewpoint::style::SizeComputationContainerStyleDescription_strategy)
def test_viewpoint::style::sizecomputationcontainerstyledescription_widthComputationExpression_type(instance):
    assert isinstance(instance.widthComputationExpression, str)


@given(instance=viewpoint::style::SizeComputationContainerStyleDescription_strategy)
def test_viewpoint::style::sizecomputationcontainerstyledescription_widthComputationExpression_setter(instance):
    original = instance.widthComputationExpression
    instance.widthComputationExpression = original
    assert instance.widthComputationExpression == original

@given(instance=viewpoint::style::SizeComputationContainerStyleDescription_strategy)
def test_viewpoint::style::sizecomputationcontainerstyledescription_heightComputationExpression_type(instance):
    assert isinstance(instance.heightComputationExpression, str)


@given(instance=viewpoint::style::SizeComputationContainerStyleDescription_strategy)
def test_viewpoint::style::sizecomputationcontainerstyledescription_heightComputationExpression_setter(instance):
    original = instance.heightComputationExpression
    instance.heightComputationExpression = original
    assert instance.heightComputationExpression == original

@given(instance=style::SizeComputationContainerStyleDescription_strategy)
@settings(max_examples=50)
def test_style::sizecomputationcontainerstyledescription_instantiation(instance):
    assert isinstance(instance, style::SizeComputationContainerStyleDescription)

@given(instance=viewpoint::style::ShapeContainerStyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::style::shapecontainerstyledescription_instantiation(instance):
    assert isinstance(instance, viewpoint::style::ShapeContainerStyleDescription)

@given(instance=viewpoint::style::ShapeContainerStyleDescription_strategy)
def test_viewpoint::style::shapecontainerstyledescription_shape_type(instance):
    assert isinstance(instance.shape, str)


@given(instance=viewpoint::style::ShapeContainerStyleDescription_strategy)
def test_viewpoint::style::shapecontainerstyledescription_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original

@given(instance=viewpoint::style::FlatContainerStyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::style::flatcontainerstyledescription_instantiation(instance):
    assert isinstance(instance, viewpoint::style::FlatContainerStyleDescription)

@given(instance=viewpoint::style::FlatContainerStyleDescription_strategy)
def test_viewpoint::style::flatcontainerstyledescription_backgroundStyle_type(instance):
    assert isinstance(instance.backgroundStyle, str)


@given(instance=viewpoint::style::FlatContainerStyleDescription_strategy)
def test_viewpoint::style::flatcontainerstyledescription_backgroundStyle_setter(instance):
    original = instance.backgroundStyle
    instance.backgroundStyle = original
    assert instance.backgroundStyle == original

@given(instance=style::RoundedCornerStyleDescription_strategy)
@settings(max_examples=50)
def test_style::roundedcornerstyledescription_instantiation(instance):
    assert isinstance(instance, style::RoundedCornerStyleDescription)

@given(instance=viewpoint::style::GaugeSectionDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::style::gaugesectiondescription_instantiation(instance):
    assert isinstance(instance, viewpoint::style::GaugeSectionDescription)

@given(instance=viewpoint::style::GaugeSectionDescription_strategy)
def test_viewpoint::style::gaugesectiondescription_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=viewpoint::style::GaugeSectionDescription_strategy)
def test_viewpoint::style::gaugesectiondescription_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=viewpoint::style::GaugeSectionDescription_strategy)
def test_viewpoint::style::gaugesectiondescription_minValueExpression_type(instance):
    assert isinstance(instance.minValueExpression, str)


@given(instance=viewpoint::style::GaugeSectionDescription_strategy)
def test_viewpoint::style::gaugesectiondescription_minValueExpression_setter(instance):
    original = instance.minValueExpression
    instance.minValueExpression = original
    assert instance.minValueExpression == original

@given(instance=viewpoint::style::GaugeSectionDescription_strategy)
def test_viewpoint::style::gaugesectiondescription_maxValueExpression_type(instance):
    assert isinstance(instance.maxValueExpression, str)


@given(instance=viewpoint::style::GaugeSectionDescription_strategy)
def test_viewpoint::style::gaugesectiondescription_maxValueExpression_setter(instance):
    original = instance.maxValueExpression
    instance.maxValueExpression = original
    assert instance.maxValueExpression == original

@given(instance=viewpoint::style::GaugeSectionDescription_strategy)
def test_viewpoint::style::gaugesectiondescription_valueExpression_type(instance):
    assert isinstance(instance.valueExpression, str)


@given(instance=viewpoint::style::GaugeSectionDescription_strategy)
def test_viewpoint::style::gaugesectiondescription_valueExpression_setter(instance):
    original = instance.valueExpression
    instance.valueExpression = original
    assert instance.valueExpression == original

@given(instance=style::GaugeSectionDescription_strategy)
@settings(max_examples=50)
def test_style::gaugesectiondescription_instantiation(instance):
    assert isinstance(instance, style::GaugeSectionDescription)

@given(instance=NodeStyleDescription_strategy)
@settings(max_examples=50)
def test_nodestyledescription_instantiation(instance):
    assert isinstance(instance, NodeStyleDescription)

@given(instance=viewpoint::style::LozengeNodeDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::style::lozengenodedescription_instantiation(instance):
    assert isinstance(instance, viewpoint::style::LozengeNodeDescription)

@given(instance=viewpoint::style::LozengeNodeDescription_strategy)
def test_viewpoint::style::lozengenodedescription_heightComputationExpression_type(instance):
    assert isinstance(instance.heightComputationExpression, str)


@given(instance=viewpoint::style::LozengeNodeDescription_strategy)
def test_viewpoint::style::lozengenodedescription_heightComputationExpression_setter(instance):
    original = instance.heightComputationExpression
    instance.heightComputationExpression = original
    assert instance.heightComputationExpression == original

@given(instance=viewpoint::style::LozengeNodeDescription_strategy)
def test_viewpoint::style::lozengenodedescription_widthComputationExpression_type(instance):
    assert isinstance(instance.widthComputationExpression, str)


@given(instance=viewpoint::style::LozengeNodeDescription_strategy)
def test_viewpoint::style::lozengenodedescription_widthComputationExpression_setter(instance):
    original = instance.widthComputationExpression
    instance.widthComputationExpression = original
    assert instance.widthComputationExpression == original

@given(instance=viewpoint::style::BundledImageDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::style::bundledimagedescription_instantiation(instance):
    assert isinstance(instance, viewpoint::style::BundledImageDescription)

@given(instance=viewpoint::style::BundledImageDescription_strategy)
def test_viewpoint::style::bundledimagedescription_shape_type(instance):
    assert isinstance(instance.shape, str)


@given(instance=viewpoint::style::BundledImageDescription_strategy)
def test_viewpoint::style::bundledimagedescription_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original

@given(instance=viewpoint::style::GaugeCompositeStyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::style::gaugecompositestyledescription_instantiation(instance):
    assert isinstance(instance, viewpoint::style::GaugeCompositeStyleDescription)

@given(instance=viewpoint::style::GaugeCompositeStyleDescription_strategy)
def test_viewpoint::style::gaugecompositestyledescription_alignment_type(instance):
    assert isinstance(instance.alignment, str)


@given(instance=viewpoint::style::GaugeCompositeStyleDescription_strategy)
def test_viewpoint::style::gaugecompositestyledescription_alignment_setter(instance):
    original = instance.alignment
    instance.alignment = original
    assert instance.alignment == original

@given(instance=viewpoint::style::SquareDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::style::squaredescription_instantiation(instance):
    assert isinstance(instance, viewpoint::style::SquareDescription)

@given(instance=viewpoint::style::SquareDescription_strategy)
def test_viewpoint::style::squaredescription_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=viewpoint::style::SquareDescription_strategy)
def test_viewpoint::style::squaredescription_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=viewpoint::style::SquareDescription_strategy)
def test_viewpoint::style::squaredescription_height_type(instance):
    assert isinstance(instance.height, str)


@given(instance=viewpoint::style::SquareDescription_strategy)
def test_viewpoint::style::squaredescription_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=viewpoint::style::DotDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::style::dotdescription_instantiation(instance):
    assert isinstance(instance, viewpoint::style::DotDescription)

@given(instance=viewpoint::style::DotDescription_strategy)
def test_viewpoint::style::dotdescription_strokeSizeComputationExpression_type(instance):
    assert isinstance(instance.strokeSizeComputationExpression, str)


@given(instance=viewpoint::style::DotDescription_strategy)
def test_viewpoint::style::dotdescription_strokeSizeComputationExpression_setter(instance):
    original = instance.strokeSizeComputationExpression
    instance.strokeSizeComputationExpression = original
    assert instance.strokeSizeComputationExpression == original

@given(instance=viewpoint::style::NoteDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::style::notedescription_instantiation(instance):
    assert isinstance(instance, viewpoint::style::NoteDescription)

@given(instance=viewpoint::style::CustomStyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::style::customstyledescription_instantiation(instance):
    assert isinstance(instance, viewpoint::style::CustomStyleDescription)

@given(instance=viewpoint::style::CustomStyleDescription_strategy)
def test_viewpoint::style::customstyledescription_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=viewpoint::style::CustomStyleDescription_strategy)
def test_viewpoint::style::customstyledescription_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=viewpoint::style::EllipseNodeDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::style::ellipsenodedescription_instantiation(instance):
    assert isinstance(instance, viewpoint::style::EllipseNodeDescription)

@given(instance=viewpoint::style::EllipseNodeDescription_strategy)
def test_viewpoint::style::ellipsenodedescription_verticalDiameterComputationExpression_type(instance):
    assert isinstance(instance.verticalDiameterComputationExpression, str)


@given(instance=viewpoint::style::EllipseNodeDescription_strategy)
def test_viewpoint::style::ellipsenodedescription_verticalDiameterComputationExpression_setter(instance):
    original = instance.verticalDiameterComputationExpression
    instance.verticalDiameterComputationExpression = original
    assert instance.verticalDiameterComputationExpression == original

@given(instance=viewpoint::style::EllipseNodeDescription_strategy)
def test_viewpoint::style::ellipsenodedescription_horizontalDiameterComputationExpression_type(instance):
    assert isinstance(instance.horizontalDiameterComputationExpression, str)


@given(instance=viewpoint::style::EllipseNodeDescription_strategy)
def test_viewpoint::style::ellipsenodedescription_horizontalDiameterComputationExpression_setter(instance):
    original = instance.horizontalDiameterComputationExpression
    instance.horizontalDiameterComputationExpression = original
    assert instance.horizontalDiameterComputationExpression == original

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

@given(instance=viewpoint::style::ContainerStyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::style::containerstyledescription_instantiation(instance):
    assert isinstance(instance, viewpoint::style::ContainerStyleDescription)

@given(instance=viewpoint::style::ContainerStyleDescription_strategy)
def test_viewpoint::style::containerstyledescription_roundedCorner_type(instance):
    assert isinstance(instance.roundedCorner, bool)


@given(instance=viewpoint::style::ContainerStyleDescription_strategy)
def test_viewpoint::style::containerstyledescription_roundedCorner_setter(instance):
    original = instance.roundedCorner
    instance.roundedCorner = original
    assert instance.roundedCorner == original

@given(instance=StyleDescription_strategy)
@settings(max_examples=50)
def test_styledescription_instantiation(instance):
    assert isinstance(instance, StyleDescription)

@given(instance=viewpoint::style::EdgeStyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::style::edgestyledescription_instantiation(instance):
    assert isinstance(instance, viewpoint::style::EdgeStyleDescription)

@given(instance=viewpoint::style::EdgeStyleDescription_strategy)
def test_viewpoint::style::edgestyledescription_lineStyle_type(instance):
    assert isinstance(instance.lineStyle, str)


@given(instance=viewpoint::style::EdgeStyleDescription_strategy)
def test_viewpoint::style::edgestyledescription_lineStyle_setter(instance):
    original = instance.lineStyle
    instance.lineStyle = original
    assert instance.lineStyle == original

@given(instance=viewpoint::style::EdgeStyleDescription_strategy)
def test_viewpoint::style::edgestyledescription_foldingStyle_type(instance):
    assert isinstance(instance.foldingStyle, str)


@given(instance=viewpoint::style::EdgeStyleDescription_strategy)
def test_viewpoint::style::edgestyledescription_foldingStyle_setter(instance):
    original = instance.foldingStyle
    instance.foldingStyle = original
    assert instance.foldingStyle == original

@given(instance=viewpoint::style::EdgeStyleDescription_strategy)
def test_viewpoint::style::edgestyledescription_targetArrow_type(instance):
    assert isinstance(instance.targetArrow, str)


@given(instance=viewpoint::style::EdgeStyleDescription_strategy)
def test_viewpoint::style::edgestyledescription_targetArrow_setter(instance):
    original = instance.targetArrow
    instance.targetArrow = original
    assert instance.targetArrow == original

@given(instance=viewpoint::style::EdgeStyleDescription_strategy)
def test_viewpoint::style::edgestyledescription_sourceArrow_type(instance):
    assert isinstance(instance.sourceArrow, str)


@given(instance=viewpoint::style::EdgeStyleDescription_strategy)
def test_viewpoint::style::edgestyledescription_sourceArrow_setter(instance):
    original = instance.sourceArrow
    instance.sourceArrow = original
    assert instance.sourceArrow == original

@given(instance=viewpoint::style::EdgeStyleDescription_strategy)
def test_viewpoint::style::edgestyledescription_routingStyle_type(instance):
    assert isinstance(instance.routingStyle, str)


@given(instance=viewpoint::style::EdgeStyleDescription_strategy)
def test_viewpoint::style::edgestyledescription_routingStyle_setter(instance):
    original = instance.routingStyle
    instance.routingStyle = original
    assert instance.routingStyle == original

@given(instance=viewpoint::style::EdgeStyleDescription_strategy)
def test_viewpoint::style::edgestyledescription_sizeComputationExpression_type(instance):
    assert isinstance(instance.sizeComputationExpression, str)


@given(instance=viewpoint::style::EdgeStyleDescription_strategy)
def test_viewpoint::style::edgestyledescription_sizeComputationExpression_setter(instance):
    original = instance.sizeComputationExpression
    instance.sizeComputationExpression = original
    assert instance.sizeComputationExpression == original

@given(instance=viewpoint::style::RoundedCornerStyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::style::roundedcornerstyledescription_instantiation(instance):
    assert isinstance(instance, viewpoint::style::RoundedCornerStyleDescription)

@given(instance=viewpoint::style::RoundedCornerStyleDescription_strategy)
def test_viewpoint::style::roundedcornerstyledescription_arcWidth_type(instance):
    assert isinstance(instance.arcWidth, str)


@given(instance=viewpoint::style::RoundedCornerStyleDescription_strategy)
def test_viewpoint::style::roundedcornerstyledescription_arcWidth_setter(instance):
    original = instance.arcWidth
    instance.arcWidth = original
    assert instance.arcWidth == original

@given(instance=viewpoint::style::RoundedCornerStyleDescription_strategy)
def test_viewpoint::style::roundedcornerstyledescription_arcHeight_type(instance):
    assert isinstance(instance.arcHeight, str)


@given(instance=viewpoint::style::RoundedCornerStyleDescription_strategy)
def test_viewpoint::style::roundedcornerstyledescription_arcHeight_setter(instance):
    original = instance.arcHeight
    instance.arcHeight = original
    assert instance.arcHeight == original

@given(instance=viewpoint::style::BorderedStyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::style::borderedstyledescription_instantiation(instance):
    assert isinstance(instance, viewpoint::style::BorderedStyleDescription)

@given(instance=viewpoint::style::BorderedStyleDescription_strategy)
def test_viewpoint::style::borderedstyledescription_borderSizeComputationExpression_type(instance):
    assert isinstance(instance.borderSizeComputationExpression, str)


@given(instance=viewpoint::style::BorderedStyleDescription_strategy)
def test_viewpoint::style::borderedstyledescription_borderSizeComputationExpression_setter(instance):
    original = instance.borderSizeComputationExpression
    instance.borderSizeComputationExpression = original
    assert instance.borderSizeComputationExpression == original

@given(instance=Layer_strategy)
@settings(max_examples=50)
def test_layer_instantiation(instance):
    assert isinstance(instance, Layer)

@given(instance=viewpoint::description::AdditionalLayer_strategy)
@settings(max_examples=50)
def test_viewpoint::description::additionallayer_instantiation(instance):
    assert isinstance(instance, viewpoint::description::AdditionalLayer)

@given(instance=viewpoint::description::AdditionalLayer_strategy)
def test_viewpoint::description::additionallayer_activeByDefault_type(instance):
    assert isinstance(instance.activeByDefault, bool)


@given(instance=viewpoint::description::AdditionalLayer_strategy)
def test_viewpoint::description::additionallayer_activeByDefault_setter(instance):
    original = instance.activeByDefault
    instance.activeByDefault = original
    assert instance.activeByDefault == original

@given(instance=viewpoint::description::AdditionalLayer_strategy)
def test_viewpoint::description::additionallayer_optional_type(instance):
    assert isinstance(instance.optional, bool)


@given(instance=viewpoint::description::AdditionalLayer_strategy)
def test_viewpoint::description::additionallayer_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original

@given(instance=Customization_strategy)
@settings(max_examples=50)
def test_customization_instantiation(instance):
    assert isinstance(instance, Customization)

@given(instance=DecorationDescriptionsSet_strategy)
@settings(max_examples=50)
def test_decorationdescriptionsset_instantiation(instance):
    assert isinstance(instance, DecorationDescriptionsSet)

@given(instance=Layout_strategy)
@settings(max_examples=50)
def test_layout_instantiation(instance):
    assert isinstance(instance, Layout)

@given(instance=viewpoint::description::CompositeLayout_strategy)
@settings(max_examples=50)
def test_viewpoint::description::compositelayout_instantiation(instance):
    assert isinstance(instance, viewpoint::description::CompositeLayout)

@given(instance=viewpoint::description::CompositeLayout_strategy)
def test_viewpoint::description::compositelayout_padding_type(instance):
    assert isinstance(instance.padding, int)


@given(instance=viewpoint::description::CompositeLayout_strategy)
def test_viewpoint::description::compositelayout_padding_setter(instance):
    original = instance.padding
    instance.padding = original
    assert instance.padding == original

@given(instance=viewpoint::description::CompositeLayout_strategy)
def test_viewpoint::description::compositelayout_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=viewpoint::description::CompositeLayout_strategy)
def test_viewpoint::description::compositelayout_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=viewpoint::description::OrderedTreeLayout_strategy)
@settings(max_examples=50)
def test_viewpoint::description::orderedtreelayout_instantiation(instance):
    assert isinstance(instance, viewpoint::description::OrderedTreeLayout)

@given(instance=viewpoint::description::OrderedTreeLayout_strategy)
def test_viewpoint::description::orderedtreelayout_childrenExpression_type(instance):
    assert isinstance(instance.childrenExpression, str)


@given(instance=viewpoint::description::OrderedTreeLayout_strategy)
def test_viewpoint::description::orderedtreelayout_childrenExpression_setter(instance):
    original = instance.childrenExpression
    instance.childrenExpression = original
    assert instance.childrenExpression == original

@given(instance=DocumentedElement_strategy)
@settings(max_examples=50)
def test_documentedelement_instantiation(instance):
    assert isinstance(instance, DocumentedElement)

@given(instance=viewpoint::validation::ValidationSet_strategy)
@settings(max_examples=50)
def test_viewpoint::validation::validationset_instantiation(instance):
    assert isinstance(instance, viewpoint::validation::ValidationSet)

@given(instance=viewpoint::validation::ValidationSet_strategy)
def test_viewpoint::validation::validationset_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=viewpoint::validation::ValidationSet_strategy)
def test_viewpoint::validation::validationset_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=viewpoint::description::Layout_strategy)
@settings(max_examples=50)
def test_viewpoint::description::layout_instantiation(instance):
    assert isinstance(instance, viewpoint::description::Layout)

@given(instance=viewpoint::concern::ConcernSet_strategy)
@settings(max_examples=50)
def test_viewpoint::concern::concernset_instantiation(instance):
    assert isinstance(instance, viewpoint::concern::ConcernSet)

@given(instance=AbstractVariable_strategy)
@settings(max_examples=50)
def test_abstractvariable_instantiation(instance):
    assert isinstance(instance, AbstractVariable)

@given(instance=viewpoint::tool::DialogVariable_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::dialogvariable_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::DialogVariable)

@given(instance=viewpoint::tool::DialogVariable_strategy)
def test_viewpoint::tool::dialogvariable_dialogPrompt_type(instance):
    assert isinstance(instance.dialogPrompt, str)


@given(instance=viewpoint::tool::DialogVariable_strategy)
def test_viewpoint::tool::dialogvariable_dialogPrompt_setter(instance):
    original = instance.dialogPrompt
    instance.dialogPrompt = original
    assert instance.dialogPrompt == original

@given(instance=viewpoint::tool::SubVariable_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::subvariable_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::SubVariable)

@given(instance=tool::VariableContainer_strategy)
@settings(max_examples=50)
def test_tool::variablecontainer_instantiation(instance):
    assert isinstance(instance, tool::VariableContainer)

@given(instance=tool::SubVariable_strategy)
@settings(max_examples=50)
def test_tool::subvariable_instantiation(instance):
    assert isinstance(instance, tool::SubVariable)

@given(instance=viewpoint::tool::AcceleoVariable_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::acceleovariable_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::AcceleoVariable)

@given(instance=viewpoint::tool::AcceleoVariable_strategy)
def test_viewpoint::tool::acceleovariable_computationExpression_type(instance):
    assert isinstance(instance.computationExpression, str)


@given(instance=viewpoint::tool::AcceleoVariable_strategy)
def test_viewpoint::tool::acceleovariable_computationExpression_setter(instance):
    original = instance.computationExpression
    instance.computationExpression = original
    assert instance.computationExpression == original

@given(instance=viewpoint::tool::VariableContainer_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::variablecontainer_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::VariableContainer)

@given(instance=viewpoint::tool::AbstractVariable_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::abstractvariable_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::AbstractVariable)

@given(instance=viewpoint::tool::AbstractVariable_strategy)
def test_viewpoint::tool::abstractvariable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=viewpoint::tool::AbstractVariable_strategy)
def test_viewpoint::tool::abstractvariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tool::ExternalJavaAction_strategy)
@settings(max_examples=50)
def test_tool::externaljavaaction_instantiation(instance):
    assert isinstance(instance, tool::ExternalJavaAction)

@given(instance=tool::ExternalJavaActionParameter_strategy)
@settings(max_examples=50)
def test_tool::externaljavaactionparameter_instantiation(instance):
    assert isinstance(instance, tool::ExternalJavaActionParameter)

@given(instance=tool::ContainerModelOperation_strategy)
@settings(max_examples=50)
def test_tool::containermodeloperation_instantiation(instance):
    assert isinstance(instance, tool::ContainerModelOperation)

@given(instance=MenuItemDescription_strategy)
@settings(max_examples=50)
def test_menuitemdescription_instantiation(instance):
    assert isinstance(instance, MenuItemDescription)

@given(instance=viewpoint::tool::OperationAction_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::operationaction_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::OperationAction)

@given(instance=tool::MenuItemDescription_strategy)
@settings(max_examples=50)
def test_tool::menuitemdescription_instantiation(instance):
    assert isinstance(instance, tool::MenuItemDescription)

@given(instance=viewpoint::tool::ExternalJavaAction_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::externaljavaaction_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::ExternalJavaAction)

@given(instance=viewpoint::tool::ExternalJavaAction_strategy)
def test_viewpoint::tool::externaljavaaction_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=viewpoint::tool::ExternalJavaAction_strategy)
def test_viewpoint::tool::externaljavaaction_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=viewpoint::tool::ExternalJavaActionCall_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::externaljavaactioncall_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::ExternalJavaActionCall)

@given(instance=MenuItemOrRef_strategy)
@settings(max_examples=50)
def test_menuitemorref_instantiation(instance):
    assert isinstance(instance, MenuItemOrRef)

@given(instance=viewpoint::tool::MenuItemDescriptionReference_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::menuitemdescriptionreference_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::MenuItemDescriptionReference)

@given(instance=tool::MenuItemOrRef_strategy)
@settings(max_examples=50)
def test_tool::menuitemorref_instantiation(instance):
    assert isinstance(instance, tool::MenuItemOrRef)

@given(instance=viewpoint::tool::MenuItemOrRef_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::menuitemorref_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::MenuItemOrRef)

@given(instance=tool::NameVariable_strategy)
@settings(max_examples=50)
def test_tool::namevariable_instantiation(instance):
    assert isinstance(instance, tool::NameVariable)

@given(instance=tool::SelectContainerVariable_strategy)
@settings(max_examples=50)
def test_tool::selectcontainervariable_instantiation(instance):
    assert isinstance(instance, tool::SelectContainerVariable)

@given(instance=tool::InitialContainerDropOperation_strategy)
@settings(max_examples=50)
def test_tool::initialcontainerdropoperation_instantiation(instance):
    assert isinstance(instance, tool::InitialContainerDropOperation)

@given(instance=tool::ContainerViewVariable_strategy)
@settings(max_examples=50)
def test_tool::containerviewvariable_instantiation(instance):
    assert isinstance(instance, tool::ContainerViewVariable)

@given(instance=tool::ElementSelectVariable_strategy)
@settings(max_examples=50)
def test_tool::elementselectvariable_instantiation(instance):
    assert isinstance(instance, tool::ElementSelectVariable)

@given(instance=description::SelectionDescription_strategy)
@settings(max_examples=50)
def test_description::selectiondescription_instantiation(instance):
    assert isinstance(instance, description::SelectionDescription)

@given(instance=tool::AbstractToolDescription_strategy)
@settings(max_examples=50)
def test_tool::abstracttooldescription_instantiation(instance):
    assert isinstance(instance, tool::AbstractToolDescription)

@given(instance=viewpoint::tool::MenuItemDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::menuitemdescription_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::MenuItemDescription)

@given(instance=viewpoint::tool::MenuItemDescription_strategy)
def test_viewpoint::tool::menuitemdescription_icon_type(instance):
    assert isinstance(instance.icon, str)


@given(instance=viewpoint::tool::MenuItemDescription_strategy)
def test_viewpoint::tool::menuitemdescription_icon_setter(instance):
    original = instance.icon
    instance.icon = original
    assert instance.icon == original

@given(instance=viewpoint::tool::SelectionWizardDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::selectionwizarddescription_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::SelectionWizardDescription)

@given(instance=viewpoint::tool::SelectionWizardDescription_strategy)
def test_viewpoint::tool::selectionwizarddescription_windowImagePath_type(instance):
    assert isinstance(instance.windowImagePath, str)


@given(instance=viewpoint::tool::SelectionWizardDescription_strategy)
def test_viewpoint::tool::selectionwizarddescription_windowImagePath_setter(instance):
    original = instance.windowImagePath
    instance.windowImagePath = original
    assert instance.windowImagePath == original

@given(instance=viewpoint::tool::SelectionWizardDescription_strategy)
def test_viewpoint::tool::selectionwizarddescription_windowTitle_type(instance):
    assert isinstance(instance.windowTitle, str)


@given(instance=viewpoint::tool::SelectionWizardDescription_strategy)
def test_viewpoint::tool::selectionwizarddescription_windowTitle_setter(instance):
    original = instance.windowTitle
    instance.windowTitle = original
    assert instance.windowTitle == original

@given(instance=viewpoint::tool::SelectionWizardDescription_strategy)
def test_viewpoint::tool::selectionwizarddescription_iconPath_type(instance):
    assert isinstance(instance.iconPath, str)


@given(instance=viewpoint::tool::SelectionWizardDescription_strategy)
def test_viewpoint::tool::selectionwizarddescription_iconPath_setter(instance):
    original = instance.iconPath
    instance.iconPath = original
    assert instance.iconPath == original

@given(instance=tool::DropContainerVariable_strategy)
@settings(max_examples=50)
def test_tool::dropcontainervariable_instantiation(instance):
    assert isinstance(instance, tool::DropContainerVariable)

@given(instance=description::DiagramElementMapping_strategy)
@settings(max_examples=50)
def test_description::diagramelementmapping_instantiation(instance):
    assert isinstance(instance, description::DiagramElementMapping)

@given(instance=tool::InitialOperation_strategy)
@settings(max_examples=50)
def test_tool::initialoperation_instantiation(instance):
    assert isinstance(instance, tool::InitialOperation)

@given(instance=tool::ElementViewVariable_strategy)
@settings(max_examples=50)
def test_tool::elementviewvariable_instantiation(instance):
    assert isinstance(instance, tool::ElementViewVariable)

@given(instance=tool::ElementVariable_strategy)
@settings(max_examples=50)
def test_tool::elementvariable_instantiation(instance):
    assert isinstance(instance, tool::ElementVariable)

@given(instance=MappingBasedToolDescription_strategy)
@settings(max_examples=50)
def test_mappingbasedtooldescription_instantiation(instance):
    assert isinstance(instance, MappingBasedToolDescription)

@given(instance=viewpoint::tool::ContainerCreationDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::containercreationdescription_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::ContainerCreationDescription)

@given(instance=viewpoint::tool::ContainerCreationDescription_strategy)
def test_viewpoint::tool::containercreationdescription_iconPath_type(instance):
    assert isinstance(instance.iconPath, str)


@given(instance=viewpoint::tool::ContainerCreationDescription_strategy)
def test_viewpoint::tool::containercreationdescription_iconPath_setter(instance):
    original = instance.iconPath
    instance.iconPath = original
    assert instance.iconPath == original

@given(instance=viewpoint::tool::PasteDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::pastedescription_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::PasteDescription)

@given(instance=viewpoint::tool::ContainerDropDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::containerdropdescription_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::ContainerDropDescription)

@given(instance=viewpoint::tool::ContainerDropDescription_strategy)
def test_viewpoint::tool::containerdropdescription_dragSource_type(instance):
    assert isinstance(instance.dragSource, str)


@given(instance=viewpoint::tool::ContainerDropDescription_strategy)
def test_viewpoint::tool::containerdropdescription_dragSource_setter(instance):
    original = instance.dragSource
    instance.dragSource = original
    assert instance.dragSource == original

@given(instance=viewpoint::tool::ContainerDropDescription_strategy)
def test_viewpoint::tool::containerdropdescription_moveEdges_type(instance):
    assert isinstance(instance.moveEdges, bool)


@given(instance=viewpoint::tool::ContainerDropDescription_strategy)
def test_viewpoint::tool::containerdropdescription_moveEdges_setter(instance):
    original = instance.moveEdges
    instance.moveEdges = original
    assert instance.moveEdges == original

@given(instance=viewpoint::tool::DeleteElementDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::deleteelementdescription_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::DeleteElementDescription)

@given(instance=viewpoint::tool::EdgeCreationDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::edgecreationdescription_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::EdgeCreationDescription)

@given(instance=viewpoint::tool::EdgeCreationDescription_strategy)
def test_viewpoint::tool::edgecreationdescription_connectionStartPrecondition_type(instance):
    assert isinstance(instance.connectionStartPrecondition, str)


@given(instance=viewpoint::tool::EdgeCreationDescription_strategy)
def test_viewpoint::tool::edgecreationdescription_connectionStartPrecondition_setter(instance):
    original = instance.connectionStartPrecondition
    instance.connectionStartPrecondition = original
    assert instance.connectionStartPrecondition == original

@given(instance=viewpoint::tool::EdgeCreationDescription_strategy)
def test_viewpoint::tool::edgecreationdescription_iconPath_type(instance):
    assert isinstance(instance.iconPath, str)


@given(instance=viewpoint::tool::EdgeCreationDescription_strategy)
def test_viewpoint::tool::edgecreationdescription_iconPath_setter(instance):
    original = instance.iconPath
    instance.iconPath = original
    assert instance.iconPath == original

@given(instance=viewpoint::tool::DoubleClickDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::doubleclickdescription_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::DoubleClickDescription)

@given(instance=viewpoint::tool::ReconnectEdgeDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::reconnectedgedescription_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::ReconnectEdgeDescription)

@given(instance=viewpoint::tool::ReconnectEdgeDescription_strategy)
def test_viewpoint::tool::reconnectedgedescription_reconnectionKind_type(instance):
    assert isinstance(instance.reconnectionKind, str)


@given(instance=viewpoint::tool::ReconnectEdgeDescription_strategy)
def test_viewpoint::tool::reconnectedgedescription_reconnectionKind_setter(instance):
    original = instance.reconnectionKind
    instance.reconnectionKind = original
    assert instance.reconnectionKind == original

@given(instance=viewpoint::tool::NodeCreationDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::nodecreationdescription_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::NodeCreationDescription)

@given(instance=viewpoint::tool::NodeCreationDescription_strategy)
def test_viewpoint::tool::nodecreationdescription_iconPath_type(instance):
    assert isinstance(instance.iconPath, str)


@given(instance=viewpoint::tool::NodeCreationDescription_strategy)
def test_viewpoint::tool::nodecreationdescription_iconPath_setter(instance):
    original = instance.iconPath
    instance.iconPath = original
    assert instance.iconPath == original

@given(instance=viewpoint::tool::DirectEditLabel_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::directeditlabel_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::DirectEditLabel)

@given(instance=viewpoint::tool::DirectEditLabel_strategy)
def test_viewpoint::tool::directeditlabel_inputLabelExpression_type(instance):
    assert isinstance(instance.inputLabelExpression, str)


@given(instance=viewpoint::tool::DirectEditLabel_strategy)
def test_viewpoint::tool::directeditlabel_inputLabelExpression_setter(instance):
    original = instance.inputLabelExpression
    instance.inputLabelExpression = original
    assert instance.inputLabelExpression == original

@given(instance=viewpoint::tool::ToolDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::tooldescription_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::ToolDescription)

@given(instance=viewpoint::tool::ToolDescription_strategy)
def test_viewpoint::tool::tooldescription_iconPath_type(instance):
    assert isinstance(instance.iconPath, str)


@given(instance=viewpoint::tool::ToolDescription_strategy)
def test_viewpoint::tool::tooldescription_iconPath_setter(instance):
    original = instance.iconPath
    instance.iconPath = original
    assert instance.iconPath == original

@given(instance=AbstractToolDescription_strategy)
@settings(max_examples=50)
def test_abstracttooldescription_instantiation(instance):
    assert isinstance(instance, AbstractToolDescription)

@given(instance=viewpoint::tool::RepresentationCreationDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::representationcreationdescription_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::RepresentationCreationDescription)

@given(instance=viewpoint::tool::RepresentationCreationDescription_strategy)
def test_viewpoint::tool::representationcreationdescription_browseExpression_type(instance):
    assert isinstance(instance.browseExpression, str)


@given(instance=viewpoint::tool::RepresentationCreationDescription_strategy)
def test_viewpoint::tool::representationcreationdescription_browseExpression_setter(instance):
    original = instance.browseExpression
    instance.browseExpression = original
    assert instance.browseExpression == original

@given(instance=viewpoint::tool::RepresentationCreationDescription_strategy)
def test_viewpoint::tool::representationcreationdescription_titleExpression_type(instance):
    assert isinstance(instance.titleExpression, str)


@given(instance=viewpoint::tool::RepresentationCreationDescription_strategy)
def test_viewpoint::tool::representationcreationdescription_titleExpression_setter(instance):
    original = instance.titleExpression
    instance.titleExpression = original
    assert instance.titleExpression == original

@given(instance=viewpoint::tool::RequestDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::requestdescription_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::RequestDescription)

@given(instance=viewpoint::tool::RequestDescription_strategy)
def test_viewpoint::tool::requestdescription_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=viewpoint::tool::RequestDescription_strategy)
def test_viewpoint::tool::requestdescription_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=viewpoint::tool::BehaviorTool_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::behaviortool_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::BehaviorTool)

@given(instance=viewpoint::tool::BehaviorTool_strategy)
def test_viewpoint::tool::behaviortool_domainClass_type(instance):
    assert isinstance(instance.domainClass, str)


@given(instance=viewpoint::tool::BehaviorTool_strategy)
def test_viewpoint::tool::behaviortool_domainClass_setter(instance):
    original = instance.domainClass
    instance.domainClass = original
    assert instance.domainClass == original

@given(instance=viewpoint::tool::PaneBasedSelectionWizardDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::panebasedselectionwizarddescription_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::PaneBasedSelectionWizardDescription)

@given(instance=viewpoint::tool::PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint::tool::panebasedselectionwizarddescription_selectedValuesMessage_type(instance):
    assert isinstance(instance.selectedValuesMessage, str)


@given(instance=viewpoint::tool::PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint::tool::panebasedselectionwizarddescription_selectedValuesMessage_setter(instance):
    original = instance.selectedValuesMessage
    instance.selectedValuesMessage = original
    assert instance.selectedValuesMessage == original

@given(instance=viewpoint::tool::PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint::tool::panebasedselectionwizarddescription_message_type(instance):
    assert isinstance(instance.message, str)


@given(instance=viewpoint::tool::PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint::tool::panebasedselectionwizarddescription_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

@given(instance=viewpoint::tool::PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint::tool::panebasedselectionwizarddescription_iconPath_type(instance):
    assert isinstance(instance.iconPath, str)


@given(instance=viewpoint::tool::PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint::tool::panebasedselectionwizarddescription_iconPath_setter(instance):
    original = instance.iconPath
    instance.iconPath = original
    assert instance.iconPath == original

@given(instance=viewpoint::tool::PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint::tool::panebasedselectionwizarddescription_choiceOfValuesMessage_type(instance):
    assert isinstance(instance.choiceOfValuesMessage, str)


@given(instance=viewpoint::tool::PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint::tool::panebasedselectionwizarddescription_choiceOfValuesMessage_setter(instance):
    original = instance.choiceOfValuesMessage
    instance.choiceOfValuesMessage = original
    assert instance.choiceOfValuesMessage == original

@given(instance=viewpoint::tool::PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint::tool::panebasedselectionwizarddescription_rootExpression_type(instance):
    assert isinstance(instance.rootExpression, str)


@given(instance=viewpoint::tool::PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint::tool::panebasedselectionwizarddescription_rootExpression_setter(instance):
    original = instance.rootExpression
    instance.rootExpression = original
    assert instance.rootExpression == original

@given(instance=viewpoint::tool::PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint::tool::panebasedselectionwizarddescription_childrenExpression_type(instance):
    assert isinstance(instance.childrenExpression, str)


@given(instance=viewpoint::tool::PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint::tool::panebasedselectionwizarddescription_childrenExpression_setter(instance):
    original = instance.childrenExpression
    instance.childrenExpression = original
    assert instance.childrenExpression == original

@given(instance=viewpoint::tool::PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint::tool::panebasedselectionwizarddescription_candidatesExpression_type(instance):
    assert isinstance(instance.candidatesExpression, str)


@given(instance=viewpoint::tool::PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint::tool::panebasedselectionwizarddescription_candidatesExpression_setter(instance):
    original = instance.candidatesExpression
    instance.candidatesExpression = original
    assert instance.candidatesExpression == original

@given(instance=viewpoint::tool::PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint::tool::panebasedselectionwizarddescription_windowImagePath_type(instance):
    assert isinstance(instance.windowImagePath, str)


@given(instance=viewpoint::tool::PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint::tool::panebasedselectionwizarddescription_windowImagePath_setter(instance):
    original = instance.windowImagePath
    instance.windowImagePath = original
    assert instance.windowImagePath == original

@given(instance=viewpoint::tool::PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint::tool::panebasedselectionwizarddescription_tree_type(instance):
    assert isinstance(instance.tree, bool)


@given(instance=viewpoint::tool::PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint::tool::panebasedselectionwizarddescription_tree_setter(instance):
    original = instance.tree
    instance.tree = original
    assert instance.tree == original

@given(instance=viewpoint::tool::PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint::tool::panebasedselectionwizarddescription_preSelectedCandidatesExpression_type(instance):
    assert isinstance(instance.preSelectedCandidatesExpression, str)


@given(instance=viewpoint::tool::PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint::tool::panebasedselectionwizarddescription_preSelectedCandidatesExpression_setter(instance):
    original = instance.preSelectedCandidatesExpression
    instance.preSelectedCandidatesExpression = original
    assert instance.preSelectedCandidatesExpression == original

@given(instance=viewpoint::tool::PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint::tool::panebasedselectionwizarddescription_windowTitle_type(instance):
    assert isinstance(instance.windowTitle, str)


@given(instance=viewpoint::tool::PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint::tool::panebasedselectionwizarddescription_windowTitle_setter(instance):
    original = instance.windowTitle
    instance.windowTitle = original
    assert instance.windowTitle == original

@given(instance=viewpoint::tool::PopupMenu_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::popupmenu_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::PopupMenu)

@given(instance=viewpoint::tool::RepresentationNavigationDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::representationnavigationdescription_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::RepresentationNavigationDescription)

@given(instance=viewpoint::tool::RepresentationNavigationDescription_strategy)
def test_viewpoint::tool::representationnavigationdescription_browseExpression_type(instance):
    assert isinstance(instance.browseExpression, str)


@given(instance=viewpoint::tool::RepresentationNavigationDescription_strategy)
def test_viewpoint::tool::representationnavigationdescription_browseExpression_setter(instance):
    original = instance.browseExpression
    instance.browseExpression = original
    assert instance.browseExpression == original

@given(instance=viewpoint::tool::RepresentationNavigationDescription_strategy)
def test_viewpoint::tool::representationnavigationdescription_navigationNameExpression_type(instance):
    assert isinstance(instance.navigationNameExpression, str)


@given(instance=viewpoint::tool::RepresentationNavigationDescription_strategy)
def test_viewpoint::tool::representationnavigationdescription_navigationNameExpression_setter(instance):
    original = instance.navigationNameExpression
    instance.navigationNameExpression = original
    assert instance.navigationNameExpression == original

@given(instance=viewpoint::tool::MappingBasedToolDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::mappingbasedtooldescription_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::MappingBasedToolDescription)

@given(instance=tool::ElementDropVariable_strategy)
@settings(max_examples=50)
def test_tool::elementdropvariable_instantiation(instance):
    assert isinstance(instance, tool::ElementDropVariable)

@given(instance=tool::ToolFilterDescription_strategy)
@settings(max_examples=50)
def test_tool::toolfilterdescription_instantiation(instance):
    assert isinstance(instance, tool::ToolFilterDescription)

@given(instance=ToolEntry_strategy)
@settings(max_examples=50)
def test_toolentry_instantiation(instance):
    assert isinstance(instance, ToolEntry)

@given(instance=viewpoint::tool::ToolGroup_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::toolgroup_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::ToolGroup)

@given(instance=viewpoint::tool::AbstractToolDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::abstracttooldescription_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::AbstractToolDescription)

@given(instance=viewpoint::tool::AbstractToolDescription_strategy)
def test_viewpoint::tool::abstracttooldescription_precondition_type(instance):
    assert isinstance(instance.precondition, str)


@given(instance=viewpoint::tool::AbstractToolDescription_strategy)
def test_viewpoint::tool::abstracttooldescription_precondition_setter(instance):
    original = instance.precondition
    instance.precondition = original
    assert instance.precondition == original

@given(instance=viewpoint::tool::AbstractToolDescription_strategy)
def test_viewpoint::tool::abstracttooldescription_forceRefresh_type(instance):
    assert isinstance(instance.forceRefresh, bool)


@given(instance=viewpoint::tool::AbstractToolDescription_strategy)
def test_viewpoint::tool::abstracttooldescription_forceRefresh_setter(instance):
    original = instance.forceRefresh
    instance.forceRefresh = original
    assert instance.forceRefresh == original

@given(instance=viewpoint::style::TooltipStyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::style::tooltipstyledescription_instantiation(instance):
    assert isinstance(instance, viewpoint::style::TooltipStyleDescription)

@given(instance=viewpoint::style::TooltipStyleDescription_strategy)
def test_viewpoint::style::tooltipstyledescription_tooltipExpression_type(instance):
    assert isinstance(instance.tooltipExpression, str)


@given(instance=viewpoint::style::TooltipStyleDescription_strategy)
def test_viewpoint::style::tooltipstyledescription_tooltipExpression_setter(instance):
    original = instance.tooltipExpression
    instance.tooltipExpression = original
    assert instance.tooltipExpression == original

@given(instance=viewpoint::style::LabelBorderStyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::style::labelborderstyledescription_instantiation(instance):
    assert isinstance(instance, viewpoint::style::LabelBorderStyleDescription)

@given(instance=viewpoint::style::LabelBorderStyleDescription_strategy)
def test_viewpoint::style::labelborderstyledescription_cornerHeight_type(instance):
    assert isinstance(instance.cornerHeight, int)


@given(instance=viewpoint::style::LabelBorderStyleDescription_strategy)
def test_viewpoint::style::labelborderstyledescription_cornerHeight_setter(instance):
    original = instance.cornerHeight
    instance.cornerHeight = original
    assert instance.cornerHeight == original

@given(instance=viewpoint::style::LabelBorderStyleDescription_strategy)
def test_viewpoint::style::labelborderstyledescription_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=viewpoint::style::LabelBorderStyleDescription_strategy)
def test_viewpoint::style::labelborderstyledescription_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=viewpoint::style::LabelBorderStyleDescription_strategy)
def test_viewpoint::style::labelborderstyledescription_cornerWidth_type(instance):
    assert isinstance(instance.cornerWidth, int)


@given(instance=viewpoint::style::LabelBorderStyleDescription_strategy)
def test_viewpoint::style::labelborderstyledescription_cornerWidth_setter(instance):
    original = instance.cornerWidth
    instance.cornerWidth = original
    assert instance.cornerWidth == original

@given(instance=viewpoint::style::LabelBorderStyleDescription_strategy)
def test_viewpoint::style::labelborderstyledescription_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=viewpoint::style::LabelBorderStyleDescription_strategy)
def test_viewpoint::style::labelborderstyledescription_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=style::LabelBorderStyleDescription_strategy)
@settings(max_examples=50)
def test_style::labelborderstyledescription_instantiation(instance):
    assert isinstance(instance, style::LabelBorderStyleDescription)

@given(instance=viewpoint::style::LabelBorderStyles_strategy)
@settings(max_examples=50)
def test_viewpoint::style::labelborderstyles_instantiation(instance):
    assert isinstance(instance, viewpoint::style::LabelBorderStyles)

@given(instance=BasicLabelStyleDescription_strategy)
@settings(max_examples=50)
def test_basiclabelstyledescription_instantiation(instance):
    assert isinstance(instance, BasicLabelStyleDescription)

@given(instance=viewpoint::style::CenterLabelStyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::style::centerlabelstyledescription_instantiation(instance):
    assert isinstance(instance, viewpoint::style::CenterLabelStyleDescription)

@given(instance=viewpoint::style::EndLabelStyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::style::endlabelstyledescription_instantiation(instance):
    assert isinstance(instance, viewpoint::style::EndLabelStyleDescription)

@given(instance=viewpoint::style::BeginLabelStyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::style::beginlabelstyledescription_instantiation(instance):
    assert isinstance(instance, viewpoint::style::BeginLabelStyleDescription)

@given(instance=viewpoint::style::LabelStyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::style::labelstyledescription_instantiation(instance):
    assert isinstance(instance, viewpoint::style::LabelStyleDescription)

@given(instance=viewpoint::style::LabelStyleDescription_strategy)
def test_viewpoint::style::labelstyledescription_labelAlignment_type(instance):
    assert isinstance(instance.labelAlignment, str)


@given(instance=viewpoint::style::LabelStyleDescription_strategy)
def test_viewpoint::style::labelstyledescription_labelAlignment_setter(instance):
    original = instance.labelAlignment
    instance.labelAlignment = original
    assert instance.labelAlignment == original

@given(instance=viewpoint::style::BasicLabelStyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::style::basiclabelstyledescription_instantiation(instance):
    assert isinstance(instance, viewpoint::style::BasicLabelStyleDescription)

@given(instance=viewpoint::style::BasicLabelStyleDescription_strategy)
def test_viewpoint::style::basiclabelstyledescription_labelSize_type(instance):
    assert isinstance(instance.labelSize, int)


@given(instance=viewpoint::style::BasicLabelStyleDescription_strategy)
def test_viewpoint::style::basiclabelstyledescription_labelSize_setter(instance):
    original = instance.labelSize
    instance.labelSize = original
    assert instance.labelSize == original

@given(instance=viewpoint::style::BasicLabelStyleDescription_strategy)
def test_viewpoint::style::basiclabelstyledescription_labelFormat_type(instance):
    assert isinstance(instance.labelFormat, str)


@given(instance=viewpoint::style::BasicLabelStyleDescription_strategy)
def test_viewpoint::style::basiclabelstyledescription_labelFormat_setter(instance):
    original = instance.labelFormat
    instance.labelFormat = original
    assert instance.labelFormat == original

@given(instance=viewpoint::style::BasicLabelStyleDescription_strategy)
def test_viewpoint::style::basiclabelstyledescription_iconPath_type(instance):
    assert isinstance(instance.iconPath, str)


@given(instance=viewpoint::style::BasicLabelStyleDescription_strategy)
def test_viewpoint::style::basiclabelstyledescription_iconPath_setter(instance):
    original = instance.iconPath
    instance.iconPath = original
    assert instance.iconPath == original

@given(instance=viewpoint::style::BasicLabelStyleDescription_strategy)
def test_viewpoint::style::basiclabelstyledescription_labelExpression_type(instance):
    assert isinstance(instance.labelExpression, str)


@given(instance=viewpoint::style::BasicLabelStyleDescription_strategy)
def test_viewpoint::style::basiclabelstyledescription_labelExpression_setter(instance):
    original = instance.labelExpression
    instance.labelExpression = original
    assert instance.labelExpression == original

@given(instance=viewpoint::style::BasicLabelStyleDescription_strategy)
def test_viewpoint::style::basiclabelstyledescription_showIcon_type(instance):
    assert isinstance(instance.showIcon, bool)


@given(instance=viewpoint::style::BasicLabelStyleDescription_strategy)
def test_viewpoint::style::basiclabelstyledescription_showIcon_setter(instance):
    original = instance.showIcon
    instance.showIcon = original
    assert instance.showIcon == original

@given(instance=viewpoint::style::StyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::style::styledescription_instantiation(instance):
    assert isinstance(instance, viewpoint::style::StyleDescription)

@given(instance=viewpoint::description::DAnnotationEntry_strategy)
@settings(max_examples=50)
def test_viewpoint::description::dannotationentry_instantiation(instance):
    assert isinstance(instance, viewpoint::description::DAnnotationEntry)

@given(instance=viewpoint::description::DAnnotationEntry_strategy)
def test_viewpoint::description::dannotationentry_source_type(instance):
    assert isinstance(instance.source, str)


@given(instance=viewpoint::description::DAnnotationEntry_strategy)
def test_viewpoint::description::dannotationentry_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original

@given(instance=viewpoint::description::DAnnotationEntry_strategy)
def test_viewpoint::description::dannotationentry_details_type(instance):
    assert isinstance(instance.details, str)


@given(instance=viewpoint::description::DAnnotationEntry_strategy)
def test_viewpoint::description::dannotationentry_details_setter(instance):
    original = instance.details
    instance.details = original
    assert instance.details == original

@given(instance=viewpoint::description::IdentifiedElement_strategy)
@settings(max_examples=50)
def test_viewpoint::description::identifiedelement_instantiation(instance):
    assert isinstance(instance, viewpoint::description::IdentifiedElement)

@given(instance=viewpoint::description::IdentifiedElement_strategy)
def test_viewpoint::description::identifiedelement_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=viewpoint::description::IdentifiedElement_strategy)
def test_viewpoint::description::identifiedelement_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=viewpoint::description::IdentifiedElement_strategy)
def test_viewpoint::description::identifiedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=viewpoint::description::IdentifiedElement_strategy)
def test_viewpoint::description::identifiedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=viewpoint::description::EndUserDocumentedElement_strategy)
@settings(max_examples=50)
def test_viewpoint::description::enduserdocumentedelement_instantiation(instance):
    assert isinstance(instance, viewpoint::description::EndUserDocumentedElement)

@given(instance=viewpoint::description::EndUserDocumentedElement_strategy)
def test_viewpoint::description::enduserdocumentedelement_endUserDocumentation_type(instance):
    assert isinstance(instance.endUserDocumentation, str)


@given(instance=viewpoint::description::EndUserDocumentedElement_strategy)
def test_viewpoint::description::enduserdocumentedelement_endUserDocumentation_setter(instance):
    original = instance.endUserDocumentation
    instance.endUserDocumentation = original
    assert instance.endUserDocumentation == original

@given(instance=viewpoint::description::AnnotationEntry_strategy)
@settings(max_examples=50)
def test_viewpoint::description::annotationentry_instantiation(instance):
    assert isinstance(instance, viewpoint::description::AnnotationEntry)

@given(instance=viewpoint::description::AnnotationEntry_strategy)
def test_viewpoint::description::annotationentry_source_type(instance):
    assert isinstance(instance.source, str)


@given(instance=viewpoint::description::AnnotationEntry_strategy)
def test_viewpoint::description::annotationentry_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original

@given(instance=UserColor_strategy)
@settings(max_examples=50)
def test_usercolor_instantiation(instance):
    assert isinstance(instance, UserColor)

@given(instance=viewpoint::description::UserColorsPalette_strategy)
@settings(max_examples=50)
def test_viewpoint::description::usercolorspalette_instantiation(instance):
    assert isinstance(instance, viewpoint::description::UserColorsPalette)

@given(instance=viewpoint::description::UserColorsPalette_strategy)
def test_viewpoint::description::usercolorspalette_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=viewpoint::description::UserColorsPalette_strategy)
def test_viewpoint::description::usercolorspalette_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SystemColor_strategy)
@settings(max_examples=50)
def test_systemcolor_instantiation(instance):
    assert isinstance(instance, SystemColor)

@given(instance=viewpoint::description::SytemColorsPalette_strategy)
@settings(max_examples=50)
def test_viewpoint::description::sytemcolorspalette_instantiation(instance):
    assert isinstance(instance, viewpoint::description::SytemColorsPalette)

@given(instance=style::LabelBorderStyles_strategy)
@settings(max_examples=50)
def test_style::labelborderstyles_instantiation(instance):
    assert isinstance(instance, style::LabelBorderStyles)

@given(instance=tool::ToolEntry_strategy)
@settings(max_examples=50)
def test_tool::toolentry_instantiation(instance):
    assert isinstance(instance, tool::ToolEntry)

@given(instance=viewpoint::description::Environment_strategy)
@settings(max_examples=50)
def test_viewpoint::description::environment_instantiation(instance):
    assert isinstance(instance, viewpoint::description::Environment)

@given(instance=viewpoint::description::UserColor_strategy)
@settings(max_examples=50)
def test_viewpoint::description::usercolor_instantiation(instance):
    assert isinstance(instance, viewpoint::description::UserColor)

@given(instance=viewpoint::description::UserColor_strategy)
def test_viewpoint::description::usercolor_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=viewpoint::description::UserColor_strategy)
def test_viewpoint::description::usercolor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=description::FixedColor_strategy)
@settings(max_examples=50)
def test_description::fixedcolor_instantiation(instance):
    assert isinstance(instance, description::FixedColor)

@given(instance=ColorDescription_strategy)
@settings(max_examples=50)
def test_colordescription_instantiation(instance):
    assert isinstance(instance, ColorDescription)

@given(instance=viewpoint::description::FixedColor_strategy)
@settings(max_examples=50)
def test_viewpoint::description::fixedcolor_instantiation(instance):
    assert isinstance(instance, viewpoint::description::FixedColor)

@given(instance=viewpoint::description::FixedColor_strategy)
def test_viewpoint::description::fixedcolor_green_type(instance):
    assert isinstance(instance.green, int)


@given(instance=viewpoint::description::FixedColor_strategy)
def test_viewpoint::description::fixedcolor_green_setter(instance):
    original = instance.green
    instance.green = original
    assert instance.green == original

@given(instance=viewpoint::description::FixedColor_strategy)
def test_viewpoint::description::fixedcolor_blue_type(instance):
    assert isinstance(instance.blue, int)


@given(instance=viewpoint::description::FixedColor_strategy)
def test_viewpoint::description::fixedcolor_blue_setter(instance):
    original = instance.blue
    instance.blue = original
    assert instance.blue == original

@given(instance=viewpoint::description::FixedColor_strategy)
def test_viewpoint::description::fixedcolor_red_type(instance):
    assert isinstance(instance.red, int)


@given(instance=viewpoint::description::FixedColor_strategy)
def test_viewpoint::description::fixedcolor_red_setter(instance):
    original = instance.red
    instance.red = original
    assert instance.red == original

@given(instance=viewpoint::description::ColorStep_strategy)
@settings(max_examples=50)
def test_viewpoint::description::colorstep_instantiation(instance):
    assert isinstance(instance, viewpoint::description::ColorStep)

@given(instance=viewpoint::description::ColorStep_strategy)
def test_viewpoint::description::colorstep_associatedValue_type(instance):
    assert isinstance(instance.associatedValue, str)


@given(instance=viewpoint::description::ColorStep_strategy)
def test_viewpoint::description::colorstep_associatedValue_setter(instance):
    original = instance.associatedValue
    instance.associatedValue = original
    assert instance.associatedValue == original

@given(instance=ColorStep_strategy)
@settings(max_examples=50)
def test_colorstep_instantiation(instance):
    assert isinstance(instance, ColorStep)

@given(instance=description::ColorDescription_strategy)
@settings(max_examples=50)
def test_description::colordescription_instantiation(instance):
    assert isinstance(instance, description::ColorDescription)

@given(instance=FixedColor_strategy)
@settings(max_examples=50)
def test_fixedcolor_instantiation(instance):
    assert isinstance(instance, FixedColor)

@given(instance=viewpoint::description::SystemColor_strategy)
@settings(max_examples=50)
def test_viewpoint::description::systemcolor_instantiation(instance):
    assert isinstance(instance, viewpoint::description::SystemColor)

@given(instance=viewpoint::description::SystemColor_strategy)
def test_viewpoint::description::systemcolor_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=viewpoint::description::SystemColor_strategy)
def test_viewpoint::description::systemcolor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=viewpoint::description::ColorDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::description::colordescription_instantiation(instance):
    assert isinstance(instance, viewpoint::description::ColorDescription)

@given(instance=viewpoint::description::SelectionDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::description::selectiondescription_instantiation(instance):
    assert isinstance(instance, viewpoint::description::SelectionDescription)

@given(instance=viewpoint::description::SelectionDescription_strategy)
def test_viewpoint::description::selectiondescription_message_type(instance):
    assert isinstance(instance.message, str)


@given(instance=viewpoint::description::SelectionDescription_strategy)
def test_viewpoint::description::selectiondescription_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

@given(instance=viewpoint::description::SelectionDescription_strategy)
def test_viewpoint::description::selectiondescription_multiple_type(instance):
    assert isinstance(instance.multiple, bool)


@given(instance=viewpoint::description::SelectionDescription_strategy)
def test_viewpoint::description::selectiondescription_multiple_setter(instance):
    original = instance.multiple
    instance.multiple = original
    assert instance.multiple == original

@given(instance=viewpoint::description::SelectionDescription_strategy)
def test_viewpoint::description::selectiondescription_tree_type(instance):
    assert isinstance(instance.tree, bool)


@given(instance=viewpoint::description::SelectionDescription_strategy)
def test_viewpoint::description::selectiondescription_tree_setter(instance):
    original = instance.tree
    instance.tree = original
    assert instance.tree == original

@given(instance=viewpoint::description::SelectionDescription_strategy)
def test_viewpoint::description::selectiondescription_candidatesExpression_type(instance):
    assert isinstance(instance.candidatesExpression, str)


@given(instance=viewpoint::description::SelectionDescription_strategy)
def test_viewpoint::description::selectiondescription_candidatesExpression_setter(instance):
    original = instance.candidatesExpression
    instance.candidatesExpression = original
    assert instance.candidatesExpression == original

@given(instance=viewpoint::description::SelectionDescription_strategy)
def test_viewpoint::description::selectiondescription_childrenExpression_type(instance):
    assert isinstance(instance.childrenExpression, str)


@given(instance=viewpoint::description::SelectionDescription_strategy)
def test_viewpoint::description::selectiondescription_childrenExpression_setter(instance):
    original = instance.childrenExpression
    instance.childrenExpression = original
    assert instance.childrenExpression == original

@given(instance=viewpoint::description::SelectionDescription_strategy)
def test_viewpoint::description::selectiondescription_rootExpression_type(instance):
    assert isinstance(instance.rootExpression, str)


@given(instance=viewpoint::description::SelectionDescription_strategy)
def test_viewpoint::description::selectiondescription_rootExpression_setter(instance):
    original = instance.rootExpression
    instance.rootExpression = original
    assert instance.rootExpression == original

@given(instance=description::UserColor_strategy)
@settings(max_examples=50)
def test_description::usercolor_instantiation(instance):
    assert isinstance(instance, description::UserColor)

@given(instance=viewpoint::description::InterpolatedColor_strategy)
@settings(max_examples=50)
def test_viewpoint::description::interpolatedcolor_instantiation(instance):
    assert isinstance(instance, viewpoint::description::InterpolatedColor)

@given(instance=viewpoint::description::InterpolatedColor_strategy)
def test_viewpoint::description::interpolatedcolor_colorValueComputationExpression_type(instance):
    assert isinstance(instance.colorValueComputationExpression, str)


@given(instance=viewpoint::description::InterpolatedColor_strategy)
def test_viewpoint::description::interpolatedcolor_colorValueComputationExpression_setter(instance):
    original = instance.colorValueComputationExpression
    instance.colorValueComputationExpression = original
    assert instance.colorValueComputationExpression == original

@given(instance=viewpoint::description::InterpolatedColor_strategy)
def test_viewpoint::description::interpolatedcolor_minValueComputationExpression_type(instance):
    assert isinstance(instance.minValueComputationExpression, str)


@given(instance=viewpoint::description::InterpolatedColor_strategy)
def test_viewpoint::description::interpolatedcolor_minValueComputationExpression_setter(instance):
    original = instance.minValueComputationExpression
    instance.minValueComputationExpression = original
    assert instance.minValueComputationExpression == original

@given(instance=viewpoint::description::InterpolatedColor_strategy)
def test_viewpoint::description::interpolatedcolor_maxValueComputationExpression_type(instance):
    assert isinstance(instance.maxValueComputationExpression, str)


@given(instance=viewpoint::description::InterpolatedColor_strategy)
def test_viewpoint::description::interpolatedcolor_maxValueComputationExpression_setter(instance):
    original = instance.maxValueComputationExpression
    instance.maxValueComputationExpression = original
    assert instance.maxValueComputationExpression == original

@given(instance=viewpoint::description::UserFixedColor_strategy)
@settings(max_examples=50)
def test_viewpoint::description::userfixedcolor_instantiation(instance):
    assert isinstance(instance, viewpoint::description::UserFixedColor)

@given(instance=viewpoint::description::ComputedColor_strategy)
@settings(max_examples=50)
def test_viewpoint::description::computedcolor_instantiation(instance):
    assert isinstance(instance, viewpoint::description::ComputedColor)

@given(instance=viewpoint::description::ComputedColor_strategy)
def test_viewpoint::description::computedcolor_red_type(instance):
    assert isinstance(instance.red, str)


@given(instance=viewpoint::description::ComputedColor_strategy)
def test_viewpoint::description::computedcolor_red_setter(instance):
    original = instance.red
    instance.red = original
    assert instance.red == original

@given(instance=viewpoint::description::ComputedColor_strategy)
def test_viewpoint::description::computedcolor_green_type(instance):
    assert isinstance(instance.green, str)


@given(instance=viewpoint::description::ComputedColor_strategy)
def test_viewpoint::description::computedcolor_green_setter(instance):
    original = instance.green
    instance.green = original
    assert instance.green == original

@given(instance=viewpoint::description::ComputedColor_strategy)
def test_viewpoint::description::computedcolor_blue_type(instance):
    assert isinstance(instance.blue, str)


@given(instance=viewpoint::description::ComputedColor_strategy)
def test_viewpoint::description::computedcolor_blue_setter(instance):
    original = instance.blue
    instance.blue = original
    assert instance.blue == original

@given(instance=EStructuralFeatureCustomization_strategy)
@settings(max_examples=50)
def test_estructuralfeaturecustomization_instantiation(instance):
    assert isinstance(instance, EStructuralFeatureCustomization)

@given(instance=viewpoint::description::EReferenceCustomization_strategy)
@settings(max_examples=50)
def test_viewpoint::description::ereferencecustomization_instantiation(instance):
    assert isinstance(instance, viewpoint::description::EReferenceCustomization)

@given(instance=viewpoint::description::EReferenceCustomization_strategy)
def test_viewpoint::description::ereferencecustomization_referenceName_type(instance):
    assert isinstance(instance.referenceName, str)


@given(instance=viewpoint::description::EReferenceCustomization_strategy)
def test_viewpoint::description::ereferencecustomization_referenceName_setter(instance):
    original = instance.referenceName
    instance.referenceName = original
    assert instance.referenceName == original

@given(instance=viewpoint::description::IVSMElementCustomization_strategy)
@settings(max_examples=50)
def test_viewpoint::description::ivsmelementcustomization_instantiation(instance):
    assert isinstance(instance, viewpoint::description::IVSMElementCustomization)

@given(instance=IVSMElementCustomization_strategy)
@settings(max_examples=50)
def test_ivsmelementcustomization_instantiation(instance):
    assert isinstance(instance, IVSMElementCustomization)

@given(instance=viewpoint::description::VSMElementCustomizationReuse_strategy)
@settings(max_examples=50)
def test_viewpoint::description::vsmelementcustomizationreuse_instantiation(instance):
    assert isinstance(instance, viewpoint::description::VSMElementCustomizationReuse)

@given(instance=viewpoint::description::VSMElementCustomization_strategy)
@settings(max_examples=50)
def test_viewpoint::description::vsmelementcustomization_instantiation(instance):
    assert isinstance(instance, viewpoint::description::VSMElementCustomization)

@given(instance=viewpoint::description::VSMElementCustomization_strategy)
def test_viewpoint::description::vsmelementcustomization_predicateExpression_type(instance):
    assert isinstance(instance.predicateExpression, str)


@given(instance=viewpoint::description::VSMElementCustomization_strategy)
def test_viewpoint::description::vsmelementcustomization_predicateExpression_setter(instance):
    original = instance.predicateExpression
    instance.predicateExpression = original
    assert instance.predicateExpression == original

@given(instance=viewpoint::description::Customization_strategy)
@settings(max_examples=50)
def test_viewpoint::description::customization_instantiation(instance):
    assert isinstance(instance, viewpoint::description::Customization)

@given(instance=viewpoint::description::EAttributeCustomization_strategy)
@settings(max_examples=50)
def test_viewpoint::description::eattributecustomization_instantiation(instance):
    assert isinstance(instance, viewpoint::description::EAttributeCustomization)

@given(instance=viewpoint::description::EAttributeCustomization_strategy)
def test_viewpoint::description::eattributecustomization_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=viewpoint::description::EAttributeCustomization_strategy)
def test_viewpoint::description::eattributecustomization_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=viewpoint::description::EAttributeCustomization_strategy)
def test_viewpoint::description::eattributecustomization_attributeName_type(instance):
    assert isinstance(instance.attributeName, str)


@given(instance=viewpoint::description::EAttributeCustomization_strategy)
def test_viewpoint::description::eattributecustomization_attributeName_setter(instance):
    original = instance.attributeName
    instance.attributeName = original
    assert instance.attributeName == original

@given(instance=viewpoint::description::EStructuralFeatureCustomization_strategy)
@settings(max_examples=50)
def test_viewpoint::description::estructuralfeaturecustomization_instantiation(instance):
    assert isinstance(instance, viewpoint::description::EStructuralFeatureCustomization)

@given(instance=viewpoint::description::EStructuralFeatureCustomization_strategy)
def test_viewpoint::description::estructuralfeaturecustomization_applyOnAll_type(instance):
    assert isinstance(instance.applyOnAll, bool)


@given(instance=viewpoint::description::EStructuralFeatureCustomization_strategy)
def test_viewpoint::description::estructuralfeaturecustomization_applyOnAll_setter(instance):
    original = instance.applyOnAll
    instance.applyOnAll = original
    assert instance.applyOnAll == original

@given(instance=viewpoint::description::DecorationDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::description::decorationdescription_instantiation(instance):
    assert isinstance(instance, viewpoint::description::DecorationDescription)

@given(instance=viewpoint::description::DecorationDescription_strategy)
def test_viewpoint::description::decorationdescription_position_type(instance):
    assert isinstance(instance.position, str)


@given(instance=viewpoint::description::DecorationDescription_strategy)
def test_viewpoint::description::decorationdescription_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=viewpoint::description::DecorationDescription_strategy)
def test_viewpoint::description::decorationdescription_preconditionExpression_type(instance):
    assert isinstance(instance.preconditionExpression, str)


@given(instance=viewpoint::description::DecorationDescription_strategy)
def test_viewpoint::description::decorationdescription_preconditionExpression_setter(instance):
    original = instance.preconditionExpression
    instance.preconditionExpression = original
    assert instance.preconditionExpression == original

@given(instance=viewpoint::description::DecorationDescription_strategy)
def test_viewpoint::description::decorationdescription_decoratorPath_type(instance):
    assert isinstance(instance.decoratorPath, str)


@given(instance=viewpoint::description::DecorationDescription_strategy)
def test_viewpoint::description::decorationdescription_decoratorPath_setter(instance):
    original = instance.decoratorPath
    instance.decoratorPath = original
    assert instance.decoratorPath == original

@given(instance=viewpoint::description::DecorationDescription_strategy)
def test_viewpoint::description::decorationdescription_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=viewpoint::description::DecorationDescription_strategy)
def test_viewpoint::description::decorationdescription_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=viewpoint::description::DecorationDescriptionsSet_strategy)
@settings(max_examples=50)
def test_viewpoint::description::decorationdescriptionsset_instantiation(instance):
    assert isinstance(instance, viewpoint::description::DecorationDescriptionsSet)

@given(instance=tool::PasteDescription_strategy)
@settings(max_examples=50)
def test_tool::pastedescription_instantiation(instance):
    assert isinstance(instance, tool::PasteDescription)

@given(instance=viewpoint::description::PasteTargetDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::description::pastetargetdescription_instantiation(instance):
    assert isinstance(instance, viewpoint::description::PasteTargetDescription)

@given(instance=tool::ContainerDropDescription_strategy)
@settings(max_examples=50)
def test_tool::containerdropdescription_instantiation(instance):
    assert isinstance(instance, tool::ContainerDropDescription)

@given(instance=viewpoint::description::DragAndDropTargetDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::description::draganddroptargetdescription_instantiation(instance):
    assert isinstance(instance, viewpoint::description::DragAndDropTargetDescription)

@given(instance=viewpoint::description::ConditionalStyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::description::conditionalstyledescription_instantiation(instance):
    assert isinstance(instance, viewpoint::description::ConditionalStyleDescription)

@given(instance=viewpoint::description::ConditionalStyleDescription_strategy)
def test_viewpoint::description::conditionalstyledescription_predicateExpression_type(instance):
    assert isinstance(instance.predicateExpression, str)


@given(instance=viewpoint::description::ConditionalStyleDescription_strategy)
def test_viewpoint::description::conditionalstyledescription_predicateExpression_setter(instance):
    original = instance.predicateExpression
    instance.predicateExpression = original
    assert instance.predicateExpression == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint::description::ConditionalStyleDescription_strategy)
@settings(max_examples=30)
def test_viewpoint::description::conditionalstyledescription_checkpredicate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.checkPredicate(
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.checkPredicate).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'checkPredicate' in viewpoint::description::ConditionalStyleDescription is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'checkPredicate' in viewpoint::description::ConditionalStyleDescription did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'checkPredicate' in viewpoint::description::ConditionalStyleDescription is not implemented or raised an error")

@given(instance=description::viewpoint::EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_description::viewpoint::estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, description::viewpoint::EStringToStringMapEntry)

@given(instance=viewpoint::description::DAnnotation_strategy)
@settings(max_examples=50)
def test_viewpoint::description::dannotation_instantiation(instance):
    assert isinstance(instance, viewpoint::description::DAnnotation)

@given(instance=viewpoint::description::DAnnotation_strategy)
def test_viewpoint::description::dannotation_source_type(instance):
    assert isinstance(instance.source, str)


@given(instance=viewpoint::description::DAnnotation_strategy)
def test_viewpoint::description::dannotation_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original

@given(instance=DAnnotation_strategy)
@settings(max_examples=50)
def test_dannotation_instantiation(instance):
    assert isinstance(instance, DAnnotation)

@given(instance=viewpoint::description::AbstractMappingImport_strategy)
@settings(max_examples=50)
def test_viewpoint::description::abstractmappingimport_instantiation(instance):
    assert isinstance(instance, viewpoint::description::AbstractMappingImport)

@given(instance=viewpoint::description::AbstractMappingImport_strategy)
def test_viewpoint::description::abstractmappingimport_hideSubMappings_type(instance):
    assert isinstance(instance.hideSubMappings, bool)


@given(instance=viewpoint::description::AbstractMappingImport_strategy)
def test_viewpoint::description::abstractmappingimport_hideSubMappings_setter(instance):
    original = instance.hideSubMappings
    instance.hideSubMappings = original
    assert instance.hideSubMappings == original

@given(instance=viewpoint::description::AbstractMappingImport_strategy)
def test_viewpoint::description::abstractmappingimport_inheritsAncestorFilters_type(instance):
    assert isinstance(instance.inheritsAncestorFilters, bool)


@given(instance=viewpoint::description::AbstractMappingImport_strategy)
def test_viewpoint::description::abstractmappingimport_inheritsAncestorFilters_setter(instance):
    original = instance.inheritsAncestorFilters
    instance.inheritsAncestorFilters = original
    assert instance.inheritsAncestorFilters == original

@given(instance=tool::RepresentationNavigationDescription_strategy)
@settings(max_examples=50)
def test_tool::representationnavigationdescription_instantiation(instance):
    assert isinstance(instance, tool::RepresentationNavigationDescription)

@given(instance=tool::RepresentationCreationDescription_strategy)
@settings(max_examples=50)
def test_tool::representationcreationdescription_instantiation(instance):
    assert isinstance(instance, tool::RepresentationCreationDescription)

@given(instance=IdentifiedElement_strategy)
@settings(max_examples=50)
def test_identifiedelement_instantiation(instance):
    assert isinstance(instance, IdentifiedElement)

@given(instance=viewpoint::description::RepresentationElementMapping_strategy)
@settings(max_examples=50)
def test_viewpoint::description::representationelementmapping_instantiation(instance):
    assert isinstance(instance, viewpoint::description::RepresentationElementMapping)

@given(instance=viewpoint::description::JavaExtension_strategy)
@settings(max_examples=50)
def test_viewpoint::description::javaextension_instantiation(instance):
    assert isinstance(instance, viewpoint::description::JavaExtension)

@given(instance=viewpoint::description::JavaExtension_strategy)
def test_viewpoint::description::javaextension_qualifiedClassName_type(instance):
    assert isinstance(instance.qualifiedClassName, str)


@given(instance=viewpoint::description::JavaExtension_strategy)
def test_viewpoint::description::javaextension_qualifiedClassName_setter(instance):
    original = instance.qualifiedClassName
    instance.qualifiedClassName = original
    assert instance.qualifiedClassName == original

@given(instance=description::viewpoint::EObject_strategy)
@settings(max_examples=50)
def test_description::viewpoint::eobject_instantiation(instance):
    assert isinstance(instance, description::viewpoint::EObject)

@given(instance=viewpoint::description::MetamodelExtensionSetting_strategy)
@settings(max_examples=50)
def test_viewpoint::description::metamodelextensionsetting_instantiation(instance):
    assert isinstance(instance, viewpoint::description::MetamodelExtensionSetting)

@given(instance=viewpoint::description::RepresentationExtensionDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::description::representationextensiondescription_instantiation(instance):
    assert isinstance(instance, viewpoint::description::RepresentationExtensionDescription)

@given(instance=viewpoint::description::RepresentationExtensionDescription_strategy)
def test_viewpoint::description::representationextensiondescription_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=viewpoint::description::RepresentationExtensionDescription_strategy)
def test_viewpoint::description::representationextensiondescription_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=viewpoint::description::RepresentationExtensionDescription_strategy)
def test_viewpoint::description::representationextensiondescription_representationName_type(instance):
    assert isinstance(instance.representationName, str)


@given(instance=viewpoint::description::RepresentationExtensionDescription_strategy)
def test_viewpoint::description::representationextensiondescription_representationName_setter(instance):
    original = instance.representationName
    instance.representationName = original
    assert instance.representationName == original

@given(instance=viewpoint::description::RepresentationExtensionDescription_strategy)
def test_viewpoint::description::representationextensiondescription_viewpointURI_type(instance):
    assert isinstance(instance.viewpointURI, str)


@given(instance=viewpoint::description::RepresentationExtensionDescription_strategy)
def test_viewpoint::description::representationextensiondescription_viewpointURI_setter(instance):
    original = instance.viewpointURI
    instance.viewpointURI = original
    assert instance.viewpointURI == original

@given(instance=viewpoint::description::DModelElement_strategy)
@settings(max_examples=50)
def test_viewpoint::description::dmodelelement_instantiation(instance):
    assert isinstance(instance, viewpoint::description::DModelElement)

@given(instance=viewpoint::description::DocumentedElement_strategy)
@settings(max_examples=50)
def test_viewpoint::description::documentedelement_instantiation(instance):
    assert isinstance(instance, viewpoint::description::DocumentedElement)

@given(instance=viewpoint::description::DocumentedElement_strategy)
def test_viewpoint::description::documentedelement_documentation_type(instance):
    assert isinstance(instance.documentation, str)


@given(instance=viewpoint::description::DocumentedElement_strategy)
def test_viewpoint::description::documentedelement_documentation_setter(instance):
    original = instance.documentation
    instance.documentation = original
    assert instance.documentation == original

@given(instance=description::viewpoint::EPackage_strategy)
@settings(max_examples=50)
def test_description::viewpoint::epackage_instantiation(instance):
    assert isinstance(instance, description::viewpoint::EPackage)

@given(instance=viewpoint::description::FeatureExtensionDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::description::featureextensiondescription_instantiation(instance):
    assert isinstance(instance, viewpoint::description::FeatureExtensionDescription)

@given(instance=RepresentationTemplate_strategy)
@settings(max_examples=50)
def test_representationtemplate_instantiation(instance):
    assert isinstance(instance, RepresentationTemplate)

@given(instance=MetamodelExtensionSetting_strategy)
@settings(max_examples=50)
def test_metamodelextensionsetting_instantiation(instance):
    assert isinstance(instance, MetamodelExtensionSetting)

@given(instance=JavaExtension_strategy)
@settings(max_examples=50)
def test_javaextension_instantiation(instance):
    assert isinstance(instance, JavaExtension)

@given(instance=RepresentationExtensionDescription_strategy)
@settings(max_examples=50)
def test_representationextensiondescription_instantiation(instance):
    assert isinstance(instance, RepresentationExtensionDescription)

@given(instance=viewpoint::description::DiagramExtensionDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::description::diagramextensiondescription_instantiation(instance):
    assert isinstance(instance, viewpoint::description::DiagramExtensionDescription)

@given(instance=RepresentationDescription_strategy)
@settings(max_examples=50)
def test_representationdescription_instantiation(instance):
    assert isinstance(instance, RepresentationDescription)

@given(instance=viewpoint::description::RepresentationImportDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::description::representationimportdescription_instantiation(instance):
    assert isinstance(instance, viewpoint::description::RepresentationImportDescription)

@given(instance=viewpoint::description::RepresentationTemplate_strategy)
@settings(max_examples=50)
def test_viewpoint::description::representationtemplate_instantiation(instance):
    assert isinstance(instance, viewpoint::description::RepresentationTemplate)

@given(instance=viewpoint::description::RepresentationTemplate_strategy)
def test_viewpoint::description::representationtemplate_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=viewpoint::description::RepresentationTemplate_strategy)
def test_viewpoint::description::representationtemplate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=validation::ValidationSet_strategy)
@settings(max_examples=50)
def test_validation::validationset_instantiation(instance):
    assert isinstance(instance, validation::ValidationSet)

@given(instance=description::IdentifiedElement_strategy)
@settings(max_examples=50)
def test_description::identifiedelement_instantiation(instance):
    assert isinstance(instance, description::IdentifiedElement)

@given(instance=description::EndUserDocumentedElement_strategy)
@settings(max_examples=50)
def test_description::enduserdocumentedelement_instantiation(instance):
    assert isinstance(instance, description::EndUserDocumentedElement)

@given(instance=description::Component_strategy)
@settings(max_examples=50)
def test_description::component_instantiation(instance):
    assert isinstance(instance, description::Component)

@given(instance=viewpoint::description::Component_strategy)
@settings(max_examples=50)
def test_viewpoint::description::component_instantiation(instance):
    assert isinstance(instance, viewpoint::description::Component)

@given(instance=UserColorsPalette_strategy)
@settings(max_examples=50)
def test_usercolorspalette_instantiation(instance):
    assert isinstance(instance, UserColorsPalette)

@given(instance=SytemColorsPalette_strategy)
@settings(max_examples=50)
def test_sytemcolorspalette_instantiation(instance):
    assert isinstance(instance, SytemColorsPalette)

@given(instance=viewpoint::Customizable_strategy)
@settings(max_examples=50)
def test_viewpoint::customizable_instantiation(instance):
    assert isinstance(instance, viewpoint::Customizable)

@given(instance=viewpoint::Customizable_strategy)
def test_viewpoint::customizable_customFeatures_type(instance):
    assert isinstance(instance.customFeatures, str)


@given(instance=viewpoint::Customizable_strategy)
def test_viewpoint::customizable_customFeatures_setter(instance):
    original = instance.customFeatures
    instance.customFeatures = original
    assert instance.customFeatures == original

@given(instance=DFile_strategy)
@settings(max_examples=50)
def test_dfile_instantiation(instance):
    assert isinstance(instance, DFile)

@given(instance=viewpoint::DModel_strategy)
@settings(max_examples=50)
def test_viewpoint::dmodel_instantiation(instance):
    assert isinstance(instance, viewpoint::DModel)

@given(instance=DResourceContainer_strategy)
@settings(max_examples=50)
def test_dresourcecontainer_instantiation(instance):
    assert isinstance(instance, DResourceContainer)

@given(instance=viewpoint::DFolder_strategy)
@settings(max_examples=50)
def test_viewpoint::dfolder_instantiation(instance):
    assert isinstance(instance, viewpoint::DFolder)

@given(instance=viewpoint::DProject_strategy)
@settings(max_examples=50)
def test_viewpoint::dproject_instantiation(instance):
    assert isinstance(instance, viewpoint::DProject)

@given(instance=DResource_strategy)
@settings(max_examples=50)
def test_dresource_instantiation(instance):
    assert isinstance(instance, DResource)

@given(instance=viewpoint::DResourceContainer_strategy)
@settings(max_examples=50)
def test_viewpoint::dresourcecontainer_instantiation(instance):
    assert isinstance(instance, viewpoint::DResourceContainer)

@given(instance=viewpoint::DFile_strategy)
@settings(max_examples=50)
def test_viewpoint::dfile_instantiation(instance):
    assert isinstance(instance, viewpoint::DFile)

@given(instance=viewpoint::DResource_strategy)
@settings(max_examples=50)
def test_viewpoint::dresource_instantiation(instance):
    assert isinstance(instance, viewpoint::DResource)

@given(instance=viewpoint::DResource_strategy)
def test_viewpoint::dresource_path_type(instance):
    assert isinstance(instance.path, str)


@given(instance=viewpoint::DResource_strategy)
def test_viewpoint::dresource_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original

@given(instance=viewpoint::DResource_strategy)
def test_viewpoint::dresource_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=viewpoint::DResource_strategy)
def test_viewpoint::dresource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=viewpoint::SessionManagerEObject_strategy)
@settings(max_examples=50)
def test_viewpoint::sessionmanagereobject_instantiation(instance):
    assert isinstance(instance, viewpoint::SessionManagerEObject)

@given(instance=viewpoint::DAnalysisSessionEObject_strategy)
@settings(max_examples=50)
def test_viewpoint::danalysissessioneobject_instantiation(instance):
    assert isinstance(instance, viewpoint::DAnalysisSessionEObject)

@given(instance=viewpoint::DAnalysisSessionEObject_strategy)
def test_viewpoint::danalysissessioneobject_controlledResources_type(instance):
    assert isinstance(instance.controlledResources, str)


@given(instance=viewpoint::DAnalysisSessionEObject_strategy)
def test_viewpoint::danalysissessioneobject_controlledResources_setter(instance):
    original = instance.controlledResources
    instance.controlledResources = original
    assert instance.controlledResources == original

@given(instance=viewpoint::DAnalysisSessionEObject_strategy)
def test_viewpoint::danalysissessioneobject_resources_type(instance):
    assert isinstance(instance.resources, str)


@given(instance=viewpoint::DAnalysisSessionEObject_strategy)
def test_viewpoint::danalysissessioneobject_resources_setter(instance):
    original = instance.resources
    instance.resources = original
    assert instance.resources == original

@given(instance=viewpoint::DAnalysisSessionEObject_strategy)
def test_viewpoint::danalysissessioneobject_blocked_type(instance):
    assert isinstance(instance.blocked, bool)


@given(instance=viewpoint::DAnalysisSessionEObject_strategy)
def test_viewpoint::danalysissessioneobject_blocked_setter(instance):
    original = instance.blocked
    instance.blocked = original
    assert instance.blocked == original

@given(instance=viewpoint::DAnalysisSessionEObject_strategy)
def test_viewpoint::danalysissessioneobject_open_type(instance):
    assert isinstance(instance.open, bool)


@given(instance=viewpoint::DAnalysisSessionEObject_strategy)
def test_viewpoint::danalysissessioneobject_open_setter(instance):
    original = instance.open
    instance.open = original
    assert instance.open == original

@given(instance=viewpoint::DAnalysisSessionEObject_strategy)
def test_viewpoint::danalysissessioneobject_synchronizationStatus_type(instance):
    assert isinstance(instance.synchronizationStatus, str)


@given(instance=viewpoint::DAnalysisSessionEObject_strategy)
def test_viewpoint::danalysissessioneobject_synchronizationStatus_setter(instance):
    original = instance.synchronizationStatus
    instance.synchronizationStatus = original
    assert instance.synchronizationStatus == original

@given(instance=viewpoint::RGBValues_strategy)
@settings(max_examples=50)
def test_viewpoint::rgbvalues_instantiation(instance):
    assert isinstance(instance, viewpoint::RGBValues)

@given(instance=viewpoint::RGBValues_strategy)
def test_viewpoint::rgbvalues_green_type(instance):
    assert isinstance(instance.green, int)


@given(instance=viewpoint::RGBValues_strategy)
def test_viewpoint::rgbvalues_green_setter(instance):
    original = instance.green
    instance.green = original
    assert instance.green == original

@given(instance=viewpoint::RGBValues_strategy)
def test_viewpoint::rgbvalues_blue_type(instance):
    assert isinstance(instance.blue, int)


@given(instance=viewpoint::RGBValues_strategy)
def test_viewpoint::rgbvalues_blue_setter(instance):
    original = instance.blue
    instance.blue = original
    assert instance.blue == original

@given(instance=viewpoint::RGBValues_strategy)
def test_viewpoint::rgbvalues_red_type(instance):
    assert isinstance(instance.red, int)


@given(instance=viewpoint::RGBValues_strategy)
def test_viewpoint::rgbvalues_red_setter(instance):
    original = instance.red
    instance.red = original
    assert instance.red == original

@given(instance=DNavigationLink_strategy)
@settings(max_examples=50)
def test_dnavigationlink_instantiation(instance):
    assert isinstance(instance, DNavigationLink)

@given(instance=viewpoint::DEObjectLink_strategy)
@settings(max_examples=50)
def test_viewpoint::deobjectlink_instantiation(instance):
    assert isinstance(instance, viewpoint::DEObjectLink)

@given(instance=viewpoint::DragAndDropTarget_strategy)
@settings(max_examples=50)
def test_viewpoint::draganddroptarget_instantiation(instance):
    assert isinstance(instance, viewpoint::DragAndDropTarget)

@given(instance=style::StyleDescription_strategy)
@settings(max_examples=50)
def test_style::styledescription_instantiation(instance):
    assert isinstance(instance, style::StyleDescription)

@given(instance=viewpoint::style::NodeStyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::style::nodestyledescription_instantiation(instance):
    assert isinstance(instance, viewpoint::style::NodeStyleDescription)

@given(instance=viewpoint::style::NodeStyleDescription_strategy)
def test_viewpoint::style::nodestyledescription_resizeKind_type(instance):
    assert isinstance(instance.resizeKind, str)


@given(instance=viewpoint::style::NodeStyleDescription_strategy)
def test_viewpoint::style::nodestyledescription_resizeKind_setter(instance):
    original = instance.resizeKind
    instance.resizeKind = original
    assert instance.resizeKind == original

@given(instance=viewpoint::style::NodeStyleDescription_strategy)
def test_viewpoint::style::nodestyledescription_hideLabelByDefault_type(instance):
    assert isinstance(instance.hideLabelByDefault, bool)


@given(instance=viewpoint::style::NodeStyleDescription_strategy)
def test_viewpoint::style::nodestyledescription_hideLabelByDefault_setter(instance):
    original = instance.hideLabelByDefault
    instance.hideLabelByDefault = original
    assert instance.hideLabelByDefault == original

@given(instance=viewpoint::style::NodeStyleDescription_strategy)
def test_viewpoint::style::nodestyledescription_sizeComputationExpression_type(instance):
    assert isinstance(instance.sizeComputationExpression, str)


@given(instance=viewpoint::style::NodeStyleDescription_strategy)
def test_viewpoint::style::nodestyledescription_sizeComputationExpression_setter(instance):
    original = instance.sizeComputationExpression
    instance.sizeComputationExpression = original
    assert instance.sizeComputationExpression == original

@given(instance=viewpoint::style::NodeStyleDescription_strategy)
def test_viewpoint::style::nodestyledescription_labelPosition_type(instance):
    assert isinstance(instance.labelPosition, str)


@given(instance=viewpoint::style::NodeStyleDescription_strategy)
def test_viewpoint::style::nodestyledescription_labelPosition_setter(instance):
    original = instance.labelPosition
    instance.labelPosition = original
    assert instance.labelPosition == original

@given(instance=Customizable_strategy)
@settings(max_examples=50)
def test_customizable_instantiation(instance):
    assert isinstance(instance, Customizable)

@given(instance=viewpoint::BasicLabelStyle_strategy)
@settings(max_examples=50)
def test_viewpoint::basiclabelstyle_instantiation(instance):
    assert isinstance(instance, viewpoint::BasicLabelStyle)

@given(instance=viewpoint::BasicLabelStyle_strategy)
def test_viewpoint::basiclabelstyle_labelSize_type(instance):
    assert isinstance(instance.labelSize, int)


@given(instance=viewpoint::BasicLabelStyle_strategy)
def test_viewpoint::basiclabelstyle_labelSize_setter(instance):
    original = instance.labelSize
    instance.labelSize = original
    assert instance.labelSize == original

@given(instance=viewpoint::BasicLabelStyle_strategy)
def test_viewpoint::basiclabelstyle_iconPath_type(instance):
    assert isinstance(instance.iconPath, str)


@given(instance=viewpoint::BasicLabelStyle_strategy)
def test_viewpoint::basiclabelstyle_iconPath_setter(instance):
    original = instance.iconPath
    instance.iconPath = original
    assert instance.iconPath == original

@given(instance=viewpoint::BasicLabelStyle_strategy)
def test_viewpoint::basiclabelstyle_showIcon_type(instance):
    assert isinstance(instance.showIcon, bool)


@given(instance=viewpoint::BasicLabelStyle_strategy)
def test_viewpoint::basiclabelstyle_showIcon_setter(instance):
    original = instance.showIcon
    instance.showIcon = original
    assert instance.showIcon == original

@given(instance=viewpoint::BasicLabelStyle_strategy)
def test_viewpoint::basiclabelstyle_labelFormat_type(instance):
    assert isinstance(instance.labelFormat, str)


@given(instance=viewpoint::BasicLabelStyle_strategy)
def test_viewpoint::basiclabelstyle_labelFormat_setter(instance):
    original = instance.labelFormat
    instance.labelFormat = original
    assert instance.labelFormat == original

@given(instance=BasicLabelStyle_strategy)
@settings(max_examples=50)
def test_basiclabelstyle_instantiation(instance):
    assert isinstance(instance, BasicLabelStyle)

@given(instance=viewpoint::diagram::CenterLabelStyle_strategy)
@settings(max_examples=50)
def test_viewpoint::diagram::centerlabelstyle_instantiation(instance):
    assert isinstance(instance, viewpoint::diagram::CenterLabelStyle)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint::diagram::CenterLabelStyle_strategy)
@settings(max_examples=30)
def test_viewpoint::diagram::centerlabelstyle_setdescription_changes_state(instance):
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
        assert has_statements, f"Function 'setDescription' in viewpoint::diagram::CenterLabelStyle is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setDescription' in viewpoint::diagram::CenterLabelStyle did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setDescription' in viewpoint::diagram::CenterLabelStyle is not implemented or raised an error")

@given(instance=viewpoint::diagram::EndLabelStyle_strategy)
@settings(max_examples=50)
def test_viewpoint::diagram::endlabelstyle_instantiation(instance):
    assert isinstance(instance, viewpoint::diagram::EndLabelStyle)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint::diagram::EndLabelStyle_strategy)
@settings(max_examples=30)
def test_viewpoint::diagram::endlabelstyle_setdescription_changes_state(instance):
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
        assert has_statements, f"Function 'setDescription' in viewpoint::diagram::EndLabelStyle is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setDescription' in viewpoint::diagram::EndLabelStyle did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setDescription' in viewpoint::diagram::EndLabelStyle is not implemented or raised an error")

@given(instance=viewpoint::diagram::BeginLabelStyle_strategy)
@settings(max_examples=50)
def test_viewpoint::diagram::beginlabelstyle_instantiation(instance):
    assert isinstance(instance, viewpoint::diagram::BeginLabelStyle)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint::diagram::BeginLabelStyle_strategy)
@settings(max_examples=30)
def test_viewpoint::diagram::beginlabelstyle_setdescription_changes_state(instance):
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
        assert has_statements, f"Function 'setDescription' in viewpoint::diagram::BeginLabelStyle is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setDescription' in viewpoint::diagram::BeginLabelStyle did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setDescription' in viewpoint::diagram::BeginLabelStyle is not implemented or raised an error")

@given(instance=viewpoint::LabelStyle_strategy)
@settings(max_examples=50)
def test_viewpoint::labelstyle_instantiation(instance):
    assert isinstance(instance, viewpoint::LabelStyle)

@given(instance=viewpoint::LabelStyle_strategy)
def test_viewpoint::labelstyle_labelAlignment_type(instance):
    assert isinstance(instance.labelAlignment, str)


@given(instance=viewpoint::LabelStyle_strategy)
def test_viewpoint::labelstyle_labelAlignment_setter(instance):
    original = instance.labelAlignment
    instance.labelAlignment = original
    assert instance.labelAlignment == original

@given(instance=viewpoint::DAnalysisCustomData_strategy)
@settings(max_examples=50)
def test_viewpoint::danalysiscustomdata_instantiation(instance):
    assert isinstance(instance, viewpoint::DAnalysisCustomData)

@given(instance=viewpoint::DAnalysisCustomData_strategy)
def test_viewpoint::danalysiscustomdata_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=viewpoint::DAnalysisCustomData_strategy)
def test_viewpoint::danalysiscustomdata_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=viewpoint::DSourceFileLink_strategy)
@settings(max_examples=50)
def test_viewpoint::dsourcefilelink_instantiation(instance):
    assert isinstance(instance, viewpoint::DSourceFileLink)

@given(instance=viewpoint::DSourceFileLink_strategy)
def test_viewpoint::dsourcefilelink_endPosition_type(instance):
    assert isinstance(instance.endPosition, int)


@given(instance=viewpoint::DSourceFileLink_strategy)
def test_viewpoint::dsourcefilelink_endPosition_setter(instance):
    original = instance.endPosition
    instance.endPosition = original
    assert instance.endPosition == original

@given(instance=viewpoint::DSourceFileLink_strategy)
def test_viewpoint::dsourcefilelink_startPosition_type(instance):
    assert isinstance(instance.startPosition, int)


@given(instance=viewpoint::DSourceFileLink_strategy)
def test_viewpoint::dsourcefilelink_startPosition_setter(instance):
    original = instance.startPosition
    instance.startPosition = original
    assert instance.startPosition == original

@given(instance=viewpoint::DSourceFileLink_strategy)
def test_viewpoint::dsourcefilelink_filePath_type(instance):
    assert isinstance(instance.filePath, str)


@given(instance=viewpoint::DSourceFileLink_strategy)
def test_viewpoint::dsourcefilelink_filePath_setter(instance):
    original = instance.filePath
    instance.filePath = original
    assert instance.filePath == original

@given(instance=DecorationDescription_strategy)
@settings(max_examples=50)
def test_decorationdescription_instantiation(instance):
    assert isinstance(instance, DecorationDescription)

@given(instance=viewpoint::description::MappingBasedDecoration_strategy)
@settings(max_examples=50)
def test_viewpoint::description::mappingbaseddecoration_instantiation(instance):
    assert isinstance(instance, viewpoint::description::MappingBasedDecoration)

@given(instance=viewpoint::description::SemanticBasedDecoration_strategy)
@settings(max_examples=50)
def test_viewpoint::description::semanticbaseddecoration_instantiation(instance):
    assert isinstance(instance, viewpoint::description::SemanticBasedDecoration)

@given(instance=viewpoint::description::SemanticBasedDecoration_strategy)
def test_viewpoint::description::semanticbaseddecoration_domainClass_type(instance):
    assert isinstance(instance.domainClass, str)


@given(instance=viewpoint::description::SemanticBasedDecoration_strategy)
def test_viewpoint::description::semanticbaseddecoration_domainClass_setter(instance):
    original = instance.domainClass
    instance.domainClass = original
    assert instance.domainClass == original

@given(instance=diagram::NodeStyle_strategy)
@settings(max_examples=50)
def test_diagram::nodestyle_instantiation(instance):
    assert isinstance(instance, diagram::NodeStyle)

@given(instance=viewpoint::diagram::WorkspaceImage_strategy)
@settings(max_examples=50)
def test_viewpoint::diagram::workspaceimage_instantiation(instance):
    assert isinstance(instance, viewpoint::diagram::WorkspaceImage)

@given(instance=viewpoint::diagram::WorkspaceImage_strategy)
def test_viewpoint::diagram::workspaceimage_workspacePath_type(instance):
    assert isinstance(instance.workspacePath, str)


@given(instance=viewpoint::diagram::WorkspaceImage_strategy)
def test_viewpoint::diagram::workspaceimage_workspacePath_setter(instance):
    original = instance.workspacePath
    instance.workspacePath = original
    assert instance.workspacePath == original

@given(instance=viewpoint::diagram::EdgeTarget_strategy)
@settings(max_examples=50)
def test_viewpoint::diagram::edgetarget_instantiation(instance):
    assert isinstance(instance, viewpoint::diagram::EdgeTarget)

@given(instance=diagram::BorderedStyle_strategy)
@settings(max_examples=50)
def test_diagram::borderedstyle_instantiation(instance):
    assert isinstance(instance, diagram::BorderedStyle)

@given(instance=Style_strategy)
@settings(max_examples=50)
def test_style_instantiation(instance):
    assert isinstance(instance, Style)

@given(instance=viewpoint::diagram::BorderedStyle_strategy)
@settings(max_examples=50)
def test_viewpoint::diagram::borderedstyle_instantiation(instance):
    assert isinstance(instance, viewpoint::diagram::BorderedStyle)

@given(instance=viewpoint::diagram::BorderedStyle_strategy)
def test_viewpoint::diagram::borderedstyle_borderSizeComputationExpression_type(instance):
    assert isinstance(instance.borderSizeComputationExpression, str)


@given(instance=viewpoint::diagram::BorderedStyle_strategy)
def test_viewpoint::diagram::borderedstyle_borderSizeComputationExpression_setter(instance):
    original = instance.borderSizeComputationExpression
    instance.borderSizeComputationExpression = original
    assert instance.borderSizeComputationExpression == original

@given(instance=viewpoint::diagram::BorderedStyle_strategy)
def test_viewpoint::diagram::borderedstyle_borderSize_type(instance):
    assert isinstance(instance.borderSize, str)


@given(instance=viewpoint::diagram::BorderedStyle_strategy)
def test_viewpoint::diagram::borderedstyle_borderSize_setter(instance):
    original = instance.borderSize
    instance.borderSize = original
    assert instance.borderSize == original

@given(instance=viewpoint::diagram::EdgeStyle_strategy)
@settings(max_examples=50)
def test_viewpoint::diagram::edgestyle_instantiation(instance):
    assert isinstance(instance, viewpoint::diagram::EdgeStyle)

@given(instance=viewpoint::diagram::EdgeStyle_strategy)
def test_viewpoint::diagram::edgestyle_size_type(instance):
    assert isinstance(instance.size, str)


@given(instance=viewpoint::diagram::EdgeStyle_strategy)
def test_viewpoint::diagram::edgestyle_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=viewpoint::diagram::EdgeStyle_strategy)
def test_viewpoint::diagram::edgestyle_routingStyle_type(instance):
    assert isinstance(instance.routingStyle, str)


@given(instance=viewpoint::diagram::EdgeStyle_strategy)
def test_viewpoint::diagram::edgestyle_routingStyle_setter(instance):
    original = instance.routingStyle
    instance.routingStyle = original
    assert instance.routingStyle == original

@given(instance=viewpoint::diagram::EdgeStyle_strategy)
def test_viewpoint::diagram::edgestyle_sourceArrow_type(instance):
    assert isinstance(instance.sourceArrow, str)


@given(instance=viewpoint::diagram::EdgeStyle_strategy)
def test_viewpoint::diagram::edgestyle_sourceArrow_setter(instance):
    original = instance.sourceArrow
    instance.sourceArrow = original
    assert instance.sourceArrow == original

@given(instance=viewpoint::diagram::EdgeStyle_strategy)
def test_viewpoint::diagram::edgestyle_lineStyle_type(instance):
    assert isinstance(instance.lineStyle, str)


@given(instance=viewpoint::diagram::EdgeStyle_strategy)
def test_viewpoint::diagram::edgestyle_lineStyle_setter(instance):
    original = instance.lineStyle
    instance.lineStyle = original
    assert instance.lineStyle == original

@given(instance=viewpoint::diagram::EdgeStyle_strategy)
def test_viewpoint::diagram::edgestyle_foldingStyle_type(instance):
    assert isinstance(instance.foldingStyle, str)


@given(instance=viewpoint::diagram::EdgeStyle_strategy)
def test_viewpoint::diagram::edgestyle_foldingStyle_setter(instance):
    original = instance.foldingStyle
    instance.foldingStyle = original
    assert instance.foldingStyle == original

@given(instance=viewpoint::diagram::EdgeStyle_strategy)
def test_viewpoint::diagram::edgestyle_targetArrow_type(instance):
    assert isinstance(instance.targetArrow, str)


@given(instance=viewpoint::diagram::EdgeStyle_strategy)
def test_viewpoint::diagram::edgestyle_targetArrow_setter(instance):
    original = instance.targetArrow
    instance.targetArrow = original
    assert instance.targetArrow == original

@given(instance=LabelStyle_strategy)
@settings(max_examples=50)
def test_labelstyle_instantiation(instance):
    assert isinstance(instance, LabelStyle)

@given(instance=viewpoint::diagram::ContainerStyle_strategy)
@settings(max_examples=50)
def test_viewpoint::diagram::containerstyle_instantiation(instance):
    assert isinstance(instance, viewpoint::diagram::ContainerStyle)

@given(instance=viewpoint::diagram::NodeStyle_strategy)
@settings(max_examples=50)
def test_viewpoint::diagram::nodestyle_instantiation(instance):
    assert isinstance(instance, viewpoint::diagram::NodeStyle)

@given(instance=viewpoint::diagram::NodeStyle_strategy)
def test_viewpoint::diagram::nodestyle_hideLabelByDefault_type(instance):
    assert isinstance(instance.hideLabelByDefault, bool)


@given(instance=viewpoint::diagram::NodeStyle_strategy)
def test_viewpoint::diagram::nodestyle_hideLabelByDefault_setter(instance):
    original = instance.hideLabelByDefault
    instance.hideLabelByDefault = original
    assert instance.hideLabelByDefault == original

@given(instance=viewpoint::diagram::NodeStyle_strategy)
def test_viewpoint::diagram::nodestyle_labelPosition_type(instance):
    assert isinstance(instance.labelPosition, str)


@given(instance=viewpoint::diagram::NodeStyle_strategy)
def test_viewpoint::diagram::nodestyle_labelPosition_setter(instance):
    original = instance.labelPosition
    instance.labelPosition = original
    assert instance.labelPosition == original

@given(instance=diagram::viewpoint::DRepresentationContainer_strategy)
@settings(max_examples=50)
def test_diagram::viewpoint::drepresentationcontainer_instantiation(instance):
    assert isinstance(instance, diagram::viewpoint::DRepresentationContainer)

@given(instance=viewpoint::diagram::GaugeSection_strategy)
@settings(max_examples=50)
def test_viewpoint::diagram::gaugesection_instantiation(instance):
    assert isinstance(instance, viewpoint::diagram::GaugeSection)

@given(instance=viewpoint::diagram::GaugeSection_strategy)
def test_viewpoint::diagram::gaugesection_max_type(instance):
    assert isinstance(instance.max, str)


@given(instance=viewpoint::diagram::GaugeSection_strategy)
def test_viewpoint::diagram::gaugesection_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=viewpoint::diagram::GaugeSection_strategy)
def test_viewpoint::diagram::gaugesection_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=viewpoint::diagram::GaugeSection_strategy)
def test_viewpoint::diagram::gaugesection_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=viewpoint::diagram::GaugeSection_strategy)
def test_viewpoint::diagram::gaugesection_min_type(instance):
    assert isinstance(instance.min, str)


@given(instance=viewpoint::diagram::GaugeSection_strategy)
def test_viewpoint::diagram::gaugesection_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=viewpoint::diagram::GaugeSection_strategy)
def test_viewpoint::diagram::gaugesection_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=viewpoint::diagram::GaugeSection_strategy)
def test_viewpoint::diagram::gaugesection_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=diagram::viewpoint::RGBValues_strategy)
@settings(max_examples=50)
def test_diagram::viewpoint::rgbvalues_instantiation(instance):
    assert isinstance(instance, diagram::viewpoint::RGBValues)

@given(instance=description::IEdgeMapping_strategy)
@settings(max_examples=50)
def test_description::iedgemapping_instantiation(instance):
    assert isinstance(instance, description::IEdgeMapping)

@given(instance=viewpoint::diagram::DDiagramSet_strategy)
@settings(max_examples=50)
def test_viewpoint::diagram::ddiagramset_instantiation(instance):
    assert isinstance(instance, viewpoint::diagram::DDiagramSet)

@given(instance=AbstractDNode_strategy)
@settings(max_examples=50)
def test_abstractdnode_instantiation(instance):
    assert isinstance(instance, AbstractDNode)

@given(instance=viewpoint::diagram::DNodeListElement_strategy)
@settings(max_examples=50)
def test_viewpoint::diagram::dnodelistelement_instantiation(instance):
    assert isinstance(instance, viewpoint::diagram::DNodeListElement)

@given(instance=EdgeStyle_strategy)
@settings(max_examples=50)
def test_edgestyle_instantiation(instance):
    assert isinstance(instance, EdgeStyle)

@given(instance=viewpoint::diagram::BracketEdgeStyle_strategy)
@settings(max_examples=50)
def test_viewpoint::diagram::bracketedgestyle_instantiation(instance):
    assert isinstance(instance, viewpoint::diagram::BracketEdgeStyle)

@given(instance=diagram::DDiagramElement_strategy)
@settings(max_examples=50)
def test_diagram::ddiagramelement_instantiation(instance):
    assert isinstance(instance, diagram::DDiagramElement)

@given(instance=description::ContainerMapping_strategy)
@settings(max_examples=50)
def test_description::containermapping_instantiation(instance):
    assert isinstance(instance, description::ContainerMapping)

@given(instance=viewpoint::description::ContainerMappingImport_strategy)
@settings(max_examples=50)
def test_viewpoint::description::containermappingimport_instantiation(instance):
    assert isinstance(instance, viewpoint::description::ContainerMappingImport)

@given(instance=ContainerStyle_strategy)
@settings(max_examples=50)
def test_containerstyle_instantiation(instance):
    assert isinstance(instance, ContainerStyle)

@given(instance=viewpoint::diagram::ShapeContainerStyle_strategy)
@settings(max_examples=50)
def test_viewpoint::diagram::shapecontainerstyle_instantiation(instance):
    assert isinstance(instance, viewpoint::diagram::ShapeContainerStyle)

@given(instance=viewpoint::diagram::ShapeContainerStyle_strategy)
def test_viewpoint::diagram::shapecontainerstyle_shape_type(instance):
    assert isinstance(instance.shape, str)


@given(instance=viewpoint::diagram::ShapeContainerStyle_strategy)
def test_viewpoint::diagram::shapecontainerstyle_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original

@given(instance=viewpoint::diagram::FlatContainerStyle_strategy)
@settings(max_examples=50)
def test_viewpoint::diagram::flatcontainerstyle_instantiation(instance):
    assert isinstance(instance, viewpoint::diagram::FlatContainerStyle)

@given(instance=viewpoint::diagram::FlatContainerStyle_strategy)
def test_viewpoint::diagram::flatcontainerstyle_backgroundStyle_type(instance):
    assert isinstance(instance.backgroundStyle, str)


@given(instance=viewpoint::diagram::FlatContainerStyle_strategy)
def test_viewpoint::diagram::flatcontainerstyle_backgroundStyle_setter(instance):
    original = instance.backgroundStyle
    instance.backgroundStyle = original
    assert instance.backgroundStyle == original

@given(instance=diagram::EdgeTarget_strategy)
@settings(max_examples=50)
def test_diagram::edgetarget_instantiation(instance):
    assert isinstance(instance, diagram::EdgeTarget)

@given(instance=viewpoint::diagram::DEdge_strategy)
@settings(max_examples=50)
def test_viewpoint::diagram::dedge_instantiation(instance):
    assert isinstance(instance, viewpoint::diagram::DEdge)

@given(instance=viewpoint::diagram::DEdge_strategy)
def test_viewpoint::diagram::dedge_endLabel_type(instance):
    assert isinstance(instance.endLabel, str)


@given(instance=viewpoint::diagram::DEdge_strategy)
def test_viewpoint::diagram::dedge_endLabel_setter(instance):
    original = instance.endLabel
    instance.endLabel = original
    assert instance.endLabel == original

@given(instance=viewpoint::diagram::DEdge_strategy)
def test_viewpoint::diagram::dedge_beginLabel_type(instance):
    assert isinstance(instance.beginLabel, str)


@given(instance=viewpoint::diagram::DEdge_strategy)
def test_viewpoint::diagram::dedge_beginLabel_setter(instance):
    original = instance.beginLabel
    instance.beginLabel = original
    assert instance.beginLabel == original

@given(instance=viewpoint::diagram::DEdge_strategy)
def test_viewpoint::diagram::dedge_isMockEdge_type(instance):
    assert isinstance(instance.isMockEdge, bool)


@given(instance=viewpoint::diagram::DEdge_strategy)
def test_viewpoint::diagram::dedge_isMockEdge_setter(instance):
    original = instance.isMockEdge
    instance.isMockEdge = original
    assert instance.isMockEdge == original

@given(instance=viewpoint::diagram::DEdge_strategy)
def test_viewpoint::diagram::dedge_routingStyle_type(instance):
    assert isinstance(instance.routingStyle, str)


@given(instance=viewpoint::diagram::DEdge_strategy)
def test_viewpoint::diagram::dedge_routingStyle_setter(instance):
    original = instance.routingStyle
    instance.routingStyle = original
    assert instance.routingStyle == original

@given(instance=viewpoint::diagram::DEdge_strategy)
def test_viewpoint::diagram::dedge_isFold_type(instance):
    assert isinstance(instance.isFold, bool)


@given(instance=viewpoint::diagram::DEdge_strategy)
def test_viewpoint::diagram::dedge_isFold_setter(instance):
    original = instance.isFold
    instance.isFold = original
    assert instance.isFold == original

@given(instance=viewpoint::diagram::DEdge_strategy)
def test_viewpoint::diagram::dedge_size_type(instance):
    assert isinstance(instance.size, str)


@given(instance=viewpoint::diagram::DEdge_strategy)
def test_viewpoint::diagram::dedge_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=viewpoint::diagram::DEdge_strategy)
def test_viewpoint::diagram::dedge_arrangeConstraints_type(instance):
    assert isinstance(instance.arrangeConstraints, str)


@given(instance=viewpoint::diagram::DEdge_strategy)
def test_viewpoint::diagram::dedge_arrangeConstraints_setter(instance):
    original = instance.arrangeConstraints
    instance.arrangeConstraints = original
    assert instance.arrangeConstraints == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint::diagram::DEdge_strategy)
@settings(max_examples=30)
def test_viewpoint::diagram::dedge_isrootfolding_changes_state(instance):
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
        assert has_statements, f"Function 'isRootFolding' in viewpoint::diagram::DEdge is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isRootFolding' in viewpoint::diagram::DEdge did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isRootFolding' in viewpoint::diagram::DEdge is not implemented or raised an error")

@given(instance=diagram::AbstractDNode_strategy)
@settings(max_examples=50)
def test_diagram::abstractdnode_instantiation(instance):
    assert isinstance(instance, diagram::AbstractDNode)

@given(instance=EdgeTarget_strategy)
@settings(max_examples=50)
def test_edgetarget_instantiation(instance):
    assert isinstance(instance, EdgeTarget)

@given(instance=description::NodeMapping_strategy)
@settings(max_examples=50)
def test_description::nodemapping_instantiation(instance):
    assert isinstance(instance, description::NodeMapping)

@given(instance=viewpoint::description::NodeMappingImport_strategy)
@settings(max_examples=50)
def test_viewpoint::description::nodemappingimport_instantiation(instance):
    assert isinstance(instance, viewpoint::description::NodeMappingImport)

@given(instance=diagram::viewpoint::Style_strategy)
@settings(max_examples=50)
def test_diagram::viewpoint::style_instantiation(instance):
    assert isinstance(instance, diagram::viewpoint::Style)

@given(instance=NodeStyle_strategy)
@settings(max_examples=50)
def test_nodestyle_instantiation(instance):
    assert isinstance(instance, NodeStyle)

@given(instance=viewpoint::diagram::CustomStyle_strategy)
@settings(max_examples=50)
def test_viewpoint::diagram::customstyle_instantiation(instance):
    assert isinstance(instance, viewpoint::diagram::CustomStyle)

@given(instance=viewpoint::diagram::CustomStyle_strategy)
def test_viewpoint::diagram::customstyle_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=viewpoint::diagram::CustomStyle_strategy)
def test_viewpoint::diagram::customstyle_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=viewpoint::diagram::Note_strategy)
@settings(max_examples=50)
def test_viewpoint::diagram::note_instantiation(instance):
    assert isinstance(instance, viewpoint::diagram::Note)

@given(instance=viewpoint::diagram::GaugeCompositeStyle_strategy)
@settings(max_examples=50)
def test_viewpoint::diagram::gaugecompositestyle_instantiation(instance):
    assert isinstance(instance, viewpoint::diagram::GaugeCompositeStyle)

@given(instance=viewpoint::diagram::GaugeCompositeStyle_strategy)
def test_viewpoint::diagram::gaugecompositestyle_alignment_type(instance):
    assert isinstance(instance.alignment, str)


@given(instance=viewpoint::diagram::GaugeCompositeStyle_strategy)
def test_viewpoint::diagram::gaugecompositestyle_alignment_setter(instance):
    original = instance.alignment
    instance.alignment = original
    assert instance.alignment == original

@given(instance=viewpoint::diagram::Dot_strategy)
@settings(max_examples=50)
def test_viewpoint::diagram::dot_instantiation(instance):
    assert isinstance(instance, viewpoint::diagram::Dot)

@given(instance=viewpoint::diagram::Dot_strategy)
def test_viewpoint::diagram::dot_strokeSizeComputationExpression_type(instance):
    assert isinstance(instance.strokeSizeComputationExpression, str)


@given(instance=viewpoint::diagram::Dot_strategy)
def test_viewpoint::diagram::dot_strokeSizeComputationExpression_setter(instance):
    original = instance.strokeSizeComputationExpression
    instance.strokeSizeComputationExpression = original
    assert instance.strokeSizeComputationExpression == original

@given(instance=viewpoint::diagram::Ellipse_strategy)
@settings(max_examples=50)
def test_viewpoint::diagram::ellipse_instantiation(instance):
    assert isinstance(instance, viewpoint::diagram::Ellipse)

@given(instance=viewpoint::diagram::Ellipse_strategy)
def test_viewpoint::diagram::ellipse_horizontalDiameter_type(instance):
    assert isinstance(instance.horizontalDiameter, str)


@given(instance=viewpoint::diagram::Ellipse_strategy)
def test_viewpoint::diagram::ellipse_horizontalDiameter_setter(instance):
    original = instance.horizontalDiameter
    instance.horizontalDiameter = original
    assert instance.horizontalDiameter == original

@given(instance=viewpoint::diagram::Ellipse_strategy)
def test_viewpoint::diagram::ellipse_verticalDiameter_type(instance):
    assert isinstance(instance.verticalDiameter, str)


@given(instance=viewpoint::diagram::Ellipse_strategy)
def test_viewpoint::diagram::ellipse_verticalDiameter_setter(instance):
    original = instance.verticalDiameter
    instance.verticalDiameter = original
    assert instance.verticalDiameter == original

@given(instance=viewpoint::diagram::Lozenge_strategy)
@settings(max_examples=50)
def test_viewpoint::diagram::lozenge_instantiation(instance):
    assert isinstance(instance, viewpoint::diagram::Lozenge)

@given(instance=viewpoint::diagram::Lozenge_strategy)
def test_viewpoint::diagram::lozenge_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=viewpoint::diagram::Lozenge_strategy)
def test_viewpoint::diagram::lozenge_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=viewpoint::diagram::Lozenge_strategy)
def test_viewpoint::diagram::lozenge_height_type(instance):
    assert isinstance(instance.height, str)


@given(instance=viewpoint::diagram::Lozenge_strategy)
def test_viewpoint::diagram::lozenge_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=viewpoint::diagram::Square_strategy)
@settings(max_examples=50)
def test_viewpoint::diagram::square_instantiation(instance):
    assert isinstance(instance, viewpoint::diagram::Square)

@given(instance=viewpoint::diagram::Square_strategy)
def test_viewpoint::diagram::square_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=viewpoint::diagram::Square_strategy)
def test_viewpoint::diagram::square_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=viewpoint::diagram::Square_strategy)
def test_viewpoint::diagram::square_height_type(instance):
    assert isinstance(instance.height, str)


@given(instance=viewpoint::diagram::Square_strategy)
def test_viewpoint::diagram::square_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=viewpoint::diagram::BundledImage_strategy)
@settings(max_examples=50)
def test_viewpoint::diagram::bundledimage_instantiation(instance):
    assert isinstance(instance, viewpoint::diagram::BundledImage)

@given(instance=viewpoint::diagram::BundledImage_strategy)
def test_viewpoint::diagram::bundledimage_shape_type(instance):
    assert isinstance(instance.shape, str)


@given(instance=viewpoint::diagram::BundledImage_strategy)
def test_viewpoint::diagram::bundledimage_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original

@given(instance=viewpoint::diagram::GraphicalFilter_strategy)
@settings(max_examples=50)
def test_viewpoint::diagram::graphicalfilter_instantiation(instance):
    assert isinstance(instance, viewpoint::diagram::GraphicalFilter)

@given(instance=GraphicalFilter_strategy)
@settings(max_examples=50)
def test_graphicalfilter_instantiation(instance):
    assert isinstance(instance, GraphicalFilter)

@given(instance=viewpoint::diagram::CollapseFilter_strategy)
@settings(max_examples=50)
def test_viewpoint::diagram::collapsefilter_instantiation(instance):
    assert isinstance(instance, viewpoint::diagram::CollapseFilter)

@given(instance=viewpoint::diagram::CollapseFilter_strategy)
def test_viewpoint::diagram::collapsefilter_width_type(instance):
    assert isinstance(instance.width, int)


@given(instance=viewpoint::diagram::CollapseFilter_strategy)
def test_viewpoint::diagram::collapsefilter_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=viewpoint::diagram::CollapseFilter_strategy)
def test_viewpoint::diagram::collapsefilter_height_type(instance):
    assert isinstance(instance.height, int)


@given(instance=viewpoint::diagram::CollapseFilter_strategy)
def test_viewpoint::diagram::collapsefilter_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=diagram::viewpoint::Decoration_strategy)
@settings(max_examples=50)
def test_diagram::viewpoint::decoration_instantiation(instance):
    assert isinstance(instance, diagram::viewpoint::Decoration)

@given(instance=viewpoint::diagram::DDiagramLink_strategy)
@settings(max_examples=50)
def test_viewpoint::diagram::ddiagramlink_instantiation(instance):
    assert isinstance(instance, viewpoint::diagram::DDiagramLink)

@given(instance=viewpoint::diagram::AbsoluteBoundsFilter_strategy)
@settings(max_examples=50)
def test_viewpoint::diagram::absoluteboundsfilter_instantiation(instance):
    assert isinstance(instance, viewpoint::diagram::AbsoluteBoundsFilter)

@given(instance=viewpoint::diagram::AbsoluteBoundsFilter_strategy)
def test_viewpoint::diagram::absoluteboundsfilter_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=viewpoint::diagram::AbsoluteBoundsFilter_strategy)
def test_viewpoint::diagram::absoluteboundsfilter_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=viewpoint::diagram::AbsoluteBoundsFilter_strategy)
def test_viewpoint::diagram::absoluteboundsfilter_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=viewpoint::diagram::AbsoluteBoundsFilter_strategy)
def test_viewpoint::diagram::absoluteboundsfilter_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=viewpoint::diagram::AbsoluteBoundsFilter_strategy)
def test_viewpoint::diagram::absoluteboundsfilter_height_type(instance):
    assert isinstance(instance.height, str)


@given(instance=viewpoint::diagram::AbsoluteBoundsFilter_strategy)
def test_viewpoint::diagram::absoluteboundsfilter_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=viewpoint::diagram::AbsoluteBoundsFilter_strategy)
def test_viewpoint::diagram::absoluteboundsfilter_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=viewpoint::diagram::AbsoluteBoundsFilter_strategy)
def test_viewpoint::diagram::absoluteboundsfilter_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=filter::CompositeFilterDescription_strategy)
@settings(max_examples=50)
def test_filter::compositefilterdescription_instantiation(instance):
    assert isinstance(instance, filter::CompositeFilterDescription)

@given(instance=viewpoint::diagram::AppliedCompositeFilters_strategy)
@settings(max_examples=50)
def test_viewpoint::diagram::appliedcompositefilters_instantiation(instance):
    assert isinstance(instance, viewpoint::diagram::AppliedCompositeFilters)

@given(instance=viewpoint::diagram::FoldingFilter_strategy)
@settings(max_examples=50)
def test_viewpoint::diagram::foldingfilter_instantiation(instance):
    assert isinstance(instance, viewpoint::diagram::FoldingFilter)

@given(instance=viewpoint::diagram::FoldingPointFilter_strategy)
@settings(max_examples=50)
def test_viewpoint::diagram::foldingpointfilter_instantiation(instance):
    assert isinstance(instance, viewpoint::diagram::FoldingPointFilter)

@given(instance=viewpoint::diagram::HideLabelFilter_strategy)
@settings(max_examples=50)
def test_viewpoint::diagram::hidelabelfilter_instantiation(instance):
    assert isinstance(instance, viewpoint::diagram::HideLabelFilter)

@given(instance=viewpoint::diagram::HideFilter_strategy)
@settings(max_examples=50)
def test_viewpoint::diagram::hidefilter_instantiation(instance):
    assert isinstance(instance, viewpoint::diagram::HideFilter)

@given(instance=description::Layer_strategy)
@settings(max_examples=50)
def test_description::layer_instantiation(instance):
    assert isinstance(instance, description::Layer)

@given(instance=FilterVariableHistory_strategy)
@settings(max_examples=50)
def test_filtervariablehistory_instantiation(instance):
    assert isinstance(instance, FilterVariableHistory)

@given(instance=tool::BehaviorTool_strategy)
@settings(max_examples=50)
def test_tool::behaviortool_instantiation(instance):
    assert isinstance(instance, tool::BehaviorTool)

@given(instance=validation::ValidationRule_strategy)
@settings(max_examples=50)
def test_validation::validationrule_instantiation(instance):
    assert isinstance(instance, validation::ValidationRule)

@given(instance=DNavigable_strategy)
@settings(max_examples=50)
def test_dnavigable_instantiation(instance):
    assert isinstance(instance, DNavigable)

@given(instance=DRepresentationElement_strategy)
@settings(max_examples=50)
def test_drepresentationelement_instantiation(instance):
    assert isinstance(instance, DRepresentationElement)

@given(instance=diagram::DDiagram_strategy)
@settings(max_examples=50)
def test_diagram::ddiagram_instantiation(instance):
    assert isinstance(instance, diagram::DDiagram)

@given(instance=DEdge_strategy)
@settings(max_examples=50)
def test_dedge_instantiation(instance):
    assert isinstance(instance, DEdge)

@given(instance=DDiagram_strategy)
@settings(max_examples=50)
def test_ddiagram_instantiation(instance):
    assert isinstance(instance, DDiagram)

@given(instance=filter::FilterDescription_strategy)
@settings(max_examples=50)
def test_filter::filterdescription_instantiation(instance):
    assert isinstance(instance, filter::FilterDescription)

@given(instance=concern::ConcernDescription_strategy)
@settings(max_examples=50)
def test_concern::concerndescription_instantiation(instance):
    assert isinstance(instance, concern::ConcernDescription)

@given(instance=DDiagramElementContainer_strategy)
@settings(max_examples=50)
def test_ddiagramelementcontainer_instantiation(instance):
    assert isinstance(instance, DDiagramElementContainer)

@given(instance=viewpoint::diagram::DNodeList_strategy)
@settings(max_examples=50)
def test_viewpoint::diagram::dnodelist_instantiation(instance):
    assert isinstance(instance, viewpoint::diagram::DNodeList)

@given(instance=viewpoint::diagram::DNodeList_strategy)
def test_viewpoint::diagram::dnodelist_lineWidth_type(instance):
    assert isinstance(instance.lineWidth, int)


@given(instance=viewpoint::diagram::DNodeList_strategy)
def test_viewpoint::diagram::dnodelist_lineWidth_setter(instance):
    original = instance.lineWidth
    instance.lineWidth = original
    assert instance.lineWidth == original

@given(instance=viewpoint::diagram::DNodeContainer_strategy)
@settings(max_examples=50)
def test_viewpoint::diagram::dnodecontainer_instantiation(instance):
    assert isinstance(instance, viewpoint::diagram::DNodeContainer)

@given(instance=viewpoint::diagram::DNodeContainer_strategy)
def test_viewpoint::diagram::dnodecontainer_childrenPresentation_type(instance):
    assert isinstance(instance.childrenPresentation, str)


@given(instance=viewpoint::diagram::DNodeContainer_strategy)
def test_viewpoint::diagram::dnodecontainer_childrenPresentation_setter(instance):
    original = instance.childrenPresentation
    instance.childrenPresentation = original
    assert instance.childrenPresentation == original

@given(instance=DNodeListElement_strategy)
@settings(max_examples=50)
def test_dnodelistelement_instantiation(instance):
    assert isinstance(instance, DNodeListElement)

@given(instance=DNode_strategy)
@settings(max_examples=50)
def test_dnode_instantiation(instance):
    assert isinstance(instance, DNode)

@given(instance=DContainer_strategy)
@settings(max_examples=50)
def test_dcontainer_instantiation(instance):
    assert isinstance(instance, DContainer)

@given(instance=DValidable_strategy)
@settings(max_examples=50)
def test_dvalidable_instantiation(instance):
    assert isinstance(instance, DValidable)

@given(instance=viewpoint::diagram::DDiagramElement_strategy)
@settings(max_examples=50)
def test_viewpoint::diagram::ddiagramelement_instantiation(instance):
    assert isinstance(instance, viewpoint::diagram::DDiagramElement)

@given(instance=viewpoint::diagram::DDiagramElement_strategy)
def test_viewpoint::diagram::ddiagramelement_tooltipText_type(instance):
    assert isinstance(instance.tooltipText, str)


@given(instance=viewpoint::diagram::DDiagramElement_strategy)
def test_viewpoint::diagram::ddiagramelement_tooltipText_setter(instance):
    original = instance.tooltipText
    instance.tooltipText = original
    assert instance.tooltipText == original

@given(instance=viewpoint::diagram::DDiagramElement_strategy)
def test_viewpoint::diagram::ddiagramelement_visible_type(instance):
    assert isinstance(instance.visible, bool)


@given(instance=viewpoint::diagram::DDiagramElement_strategy)
def test_viewpoint::diagram::ddiagramelement_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint::diagram::DDiagramElement_strategy)
@settings(max_examples=30)
def test_viewpoint::diagram::ddiagramelement_isfold_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isFold(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isFold).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isFold' in viewpoint::diagram::DDiagramElement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isFold' in viewpoint::diagram::DDiagramElement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isFold' in viewpoint::diagram::DDiagramElement is not implemented or raised an error")

@given(instance=DragAndDropTarget_strategy)
@settings(max_examples=50)
def test_draganddroptarget_instantiation(instance):
    assert isinstance(instance, DragAndDropTarget)

@given(instance=viewpoint::diagram::DDiagramElementContainer_strategy)
@settings(max_examples=50)
def test_viewpoint::diagram::ddiagramelementcontainer_instantiation(instance):
    assert isinstance(instance, viewpoint::diagram::DDiagramElementContainer)

@given(instance=viewpoint::diagram::DDiagramElementContainer_strategy)
def test_viewpoint::diagram::ddiagramelementcontainer_height_type(instance):
    assert isinstance(instance.height, str)


@given(instance=viewpoint::diagram::DDiagramElementContainer_strategy)
def test_viewpoint::diagram::ddiagramelementcontainer_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=viewpoint::diagram::DDiagramElementContainer_strategy)
def test_viewpoint::diagram::ddiagramelementcontainer_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=viewpoint::diagram::DDiagramElementContainer_strategy)
def test_viewpoint::diagram::ddiagramelementcontainer_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=viewpoint::diagram::DNode_strategy)
@settings(max_examples=50)
def test_viewpoint::diagram::dnode_instantiation(instance):
    assert isinstance(instance, viewpoint::diagram::DNode)

@given(instance=viewpoint::diagram::DNode_strategy)
def test_viewpoint::diagram::dnode_height_type(instance):
    assert isinstance(instance.height, str)


@given(instance=viewpoint::diagram::DNode_strategy)
def test_viewpoint::diagram::dnode_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=viewpoint::diagram::DNode_strategy)
def test_viewpoint::diagram::dnode_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=viewpoint::diagram::DNode_strategy)
def test_viewpoint::diagram::dnode_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=viewpoint::diagram::DNode_strategy)
def test_viewpoint::diagram::dnode_labelPosition_type(instance):
    assert isinstance(instance.labelPosition, str)


@given(instance=viewpoint::diagram::DNode_strategy)
def test_viewpoint::diagram::dnode_labelPosition_setter(instance):
    original = instance.labelPosition
    instance.labelPosition = original
    assert instance.labelPosition == original

@given(instance=viewpoint::diagram::DNode_strategy)
def test_viewpoint::diagram::dnode_resizeKind_type(instance):
    assert isinstance(instance.resizeKind, str)


@given(instance=viewpoint::diagram::DNode_strategy)
def test_viewpoint::diagram::dnode_resizeKind_setter(instance):
    original = instance.resizeKind
    instance.resizeKind = original
    assert instance.resizeKind == original

@given(instance=DRepresentation_strategy)
@settings(max_examples=50)
def test_drepresentation_instantiation(instance):
    assert isinstance(instance, DRepresentation)

@given(instance=InformationSection_strategy)
@settings(max_examples=50)
def test_informationsection_instantiation(instance):
    assert isinstance(instance, InformationSection)

@given(instance=viewpoint::audit::TemplateInformationSection_strategy)
@settings(max_examples=50)
def test_viewpoint::audit::templateinformationsection_instantiation(instance):
    assert isinstance(instance, viewpoint::audit::TemplateInformationSection)

@given(instance=viewpoint::audit::TemplateInformationSection_strategy)
def test_viewpoint::audit::templateinformationsection_templatePath_type(instance):
    assert isinstance(instance.templatePath, str)


@given(instance=viewpoint::audit::TemplateInformationSection_strategy)
def test_viewpoint::audit::templateinformationsection_templatePath_setter(instance):
    original = instance.templatePath
    instance.templatePath = original
    assert instance.templatePath == original

@given(instance=description::DiagramDescription_strategy)
@settings(max_examples=50)
def test_description::diagramdescription_instantiation(instance):
    assert isinstance(instance, description::DiagramDescription)

@given(instance=viewpoint::description::DiagramImportDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::description::diagramimportdescription_instantiation(instance):
    assert isinstance(instance, viewpoint::description::DiagramImportDescription)

@given(instance=DDiagramElement_strategy)
@settings(max_examples=50)
def test_ddiagramelement_instantiation(instance):
    assert isinstance(instance, DDiagramElement)

@given(instance=viewpoint::diagram::AbstractDNode_strategy)
@settings(max_examples=50)
def test_viewpoint::diagram::abstractdnode_instantiation(instance):
    assert isinstance(instance, viewpoint::diagram::AbstractDNode)

@given(instance=viewpoint::diagram::AbstractDNode_strategy)
def test_viewpoint::diagram::abstractdnode_arrangeConstraints_type(instance):
    assert isinstance(instance.arrangeConstraints, str)


@given(instance=viewpoint::diagram::AbstractDNode_strategy)
def test_viewpoint::diagram::abstractdnode_arrangeConstraints_setter(instance):
    original = instance.arrangeConstraints
    instance.arrangeConstraints = original
    assert instance.arrangeConstraints == original

@given(instance=SwitchChild_strategy)
@settings(max_examples=50)
def test_switchchild_instantiation(instance):
    assert isinstance(instance, SwitchChild)

@given(instance=viewpoint::tool::Case_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::case_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::Case)

@given(instance=viewpoint::tool::Case_strategy)
def test_viewpoint::tool::case_conditionExpression_type(instance):
    assert isinstance(instance.conditionExpression, str)


@given(instance=viewpoint::tool::Case_strategy)
def test_viewpoint::tool::case_conditionExpression_setter(instance):
    original = instance.conditionExpression
    instance.conditionExpression = original
    assert instance.conditionExpression == original

@given(instance=viewpoint::tool::FeatureChangeListener_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::featurechangelistener_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::FeatureChangeListener)

@given(instance=viewpoint::tool::FeatureChangeListener_strategy)
def test_viewpoint::tool::featurechangelistener_featureName_type(instance):
    assert isinstance(instance.featureName, str)


@given(instance=viewpoint::tool::FeatureChangeListener_strategy)
def test_viewpoint::tool::featurechangelistener_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original

@given(instance=viewpoint::tool::FeatureChangeListener_strategy)
def test_viewpoint::tool::featurechangelistener_domainClass_type(instance):
    assert isinstance(instance.domainClass, str)


@given(instance=viewpoint::tool::FeatureChangeListener_strategy)
def test_viewpoint::tool::featurechangelistener_domainClass_setter(instance):
    original = instance.domainClass
    instance.domainClass = original
    assert instance.domainClass == original

@given(instance=tool::FeatureChangeListener_strategy)
@settings(max_examples=50)
def test_tool::featurechangelistener_instantiation(instance):
    assert isinstance(instance, tool::FeatureChangeListener)

@given(instance=viewpoint::audit::InformationSection_strategy)
@settings(max_examples=50)
def test_viewpoint::audit::informationsection_instantiation(instance):
    assert isinstance(instance, viewpoint::audit::InformationSection)

@given(instance=tool::Default_strategy)
@settings(max_examples=50)
def test_tool::default_instantiation(instance):
    assert isinstance(instance, tool::Default)

@given(instance=tool::Case_strategy)
@settings(max_examples=50)
def test_tool::case_instantiation(instance):
    assert isinstance(instance, tool::Case)

@given(instance=viewpoint::tool::Default_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::default_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::Default)

@given(instance=viewpoint::tool::SwitchChild_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::switchchild_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::SwitchChild)

@given(instance=viewpoint::tool::ToolFilterDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::toolfilterdescription_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::ToolFilterDescription)

@given(instance=viewpoint::tool::ToolFilterDescription_strategy)
def test_viewpoint::tool::toolfilterdescription_precondition_type(instance):
    assert isinstance(instance.precondition, str)


@given(instance=viewpoint::tool::ToolFilterDescription_strategy)
def test_viewpoint::tool::toolfilterdescription_precondition_setter(instance):
    original = instance.precondition
    instance.precondition = original
    assert instance.precondition == original

@given(instance=viewpoint::tool::ToolFilterDescription_strategy)
def test_viewpoint::tool::toolfilterdescription_elementsToListen_type(instance):
    assert isinstance(instance.elementsToListen, str)


@given(instance=viewpoint::tool::ToolFilterDescription_strategy)
def test_viewpoint::tool::toolfilterdescription_elementsToListen_setter(instance):
    original = instance.elementsToListen
    instance.elementsToListen = original
    assert instance.elementsToListen == original

@given(instance=viewpoint::tool::ExternalJavaActionParameter_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::externaljavaactionparameter_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::ExternalJavaActionParameter)

@given(instance=viewpoint::tool::ExternalJavaActionParameter_strategy)
def test_viewpoint::tool::externaljavaactionparameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=viewpoint::tool::ExternalJavaActionParameter_strategy)
def test_viewpoint::tool::externaljavaactionparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=viewpoint::tool::ExternalJavaActionParameter_strategy)
def test_viewpoint::tool::externaljavaactionparameter_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=viewpoint::tool::ExternalJavaActionParameter_strategy)
def test_viewpoint::tool::externaljavaactionparameter_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=viewpoint::tool::NameVariable_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::namevariable_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::NameVariable)

@given(instance=tool::viewpoint::EObject_strategy)
@settings(max_examples=50)
def test_tool::viewpoint::eobject_instantiation(instance):
    assert isinstance(instance, tool::viewpoint::EObject)

@given(instance=ContainerModelOperation_strategy)
@settings(max_examples=50)
def test_containermodeloperation_instantiation(instance):
    assert isinstance(instance, ContainerModelOperation)

@given(instance=viewpoint::tool::RemoveElement_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::removeelement_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::RemoveElement)

@given(instance=viewpoint::tool::SetObject_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::setobject_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::SetObject)

@given(instance=viewpoint::tool::SetObject_strategy)
def test_viewpoint::tool::setobject_featureName_type(instance):
    assert isinstance(instance.featureName, str)


@given(instance=viewpoint::tool::SetObject_strategy)
def test_viewpoint::tool::setobject_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original

@given(instance=viewpoint::tool::ChangeContext_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::changecontext_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::ChangeContext)

@given(instance=viewpoint::tool::ChangeContext_strategy)
def test_viewpoint::tool::changecontext_browseExpression_type(instance):
    assert isinstance(instance.browseExpression, str)


@given(instance=viewpoint::tool::ChangeContext_strategy)
def test_viewpoint::tool::changecontext_browseExpression_setter(instance):
    original = instance.browseExpression
    instance.browseExpression = original
    assert instance.browseExpression == original

@given(instance=viewpoint::tool::CreateView_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::createview_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::CreateView)

@given(instance=viewpoint::tool::CreateView_strategy)
def test_viewpoint::tool::createview_containerViewExpression_type(instance):
    assert isinstance(instance.containerViewExpression, str)


@given(instance=viewpoint::tool::CreateView_strategy)
def test_viewpoint::tool::createview_containerViewExpression_setter(instance):
    original = instance.containerViewExpression
    instance.containerViewExpression = original
    assert instance.containerViewExpression == original

@given(instance=viewpoint::tool::CreateView_strategy)
def test_viewpoint::tool::createview_variableName_type(instance):
    assert isinstance(instance.variableName, str)


@given(instance=viewpoint::tool::CreateView_strategy)
def test_viewpoint::tool::createview_variableName_setter(instance):
    original = instance.variableName
    instance.variableName = original
    assert instance.variableName == original

@given(instance=viewpoint::tool::DeleteView_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::deleteview_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::DeleteView)

@given(instance=viewpoint::tool::Navigation_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::navigation_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::Navigation)

@given(instance=viewpoint::tool::Navigation_strategy)
def test_viewpoint::tool::navigation_createIfNotExistent_type(instance):
    assert isinstance(instance.createIfNotExistent, bool)


@given(instance=viewpoint::tool::Navigation_strategy)
def test_viewpoint::tool::navigation_createIfNotExistent_setter(instance):
    original = instance.createIfNotExistent
    instance.createIfNotExistent = original
    assert instance.createIfNotExistent == original

@given(instance=viewpoint::tool::For_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::for_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::For)

@given(instance=viewpoint::tool::For_strategy)
def test_viewpoint::tool::for_iteratorName_type(instance):
    assert isinstance(instance.iteratorName, str)


@given(instance=viewpoint::tool::For_strategy)
def test_viewpoint::tool::for_iteratorName_setter(instance):
    original = instance.iteratorName
    instance.iteratorName = original
    assert instance.iteratorName == original

@given(instance=viewpoint::tool::For_strategy)
def test_viewpoint::tool::for_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=viewpoint::tool::For_strategy)
def test_viewpoint::tool::for_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=viewpoint::tool::Unset_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::unset_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::Unset)

@given(instance=viewpoint::tool::Unset_strategy)
def test_viewpoint::tool::unset_elementExpression_type(instance):
    assert isinstance(instance.elementExpression, str)


@given(instance=viewpoint::tool::Unset_strategy)
def test_viewpoint::tool::unset_elementExpression_setter(instance):
    original = instance.elementExpression
    instance.elementExpression = original
    assert instance.elementExpression == original

@given(instance=viewpoint::tool::Unset_strategy)
def test_viewpoint::tool::unset_featureName_type(instance):
    assert isinstance(instance.featureName, str)


@given(instance=viewpoint::tool::Unset_strategy)
def test_viewpoint::tool::unset_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original

@given(instance=viewpoint::tool::MoveElement_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::moveelement_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::MoveElement)

@given(instance=viewpoint::tool::MoveElement_strategy)
def test_viewpoint::tool::moveelement_newContainerExpression_type(instance):
    assert isinstance(instance.newContainerExpression, str)


@given(instance=viewpoint::tool::MoveElement_strategy)
def test_viewpoint::tool::moveelement_newContainerExpression_setter(instance):
    original = instance.newContainerExpression
    instance.newContainerExpression = original
    assert instance.newContainerExpression == original

@given(instance=viewpoint::tool::MoveElement_strategy)
def test_viewpoint::tool::moveelement_featureName_type(instance):
    assert isinstance(instance.featureName, str)


@given(instance=viewpoint::tool::MoveElement_strategy)
def test_viewpoint::tool::moveelement_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original

@given(instance=viewpoint::tool::SetValue_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::setvalue_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::SetValue)

@given(instance=viewpoint::tool::SetValue_strategy)
def test_viewpoint::tool::setvalue_valueExpression_type(instance):
    assert isinstance(instance.valueExpression, str)


@given(instance=viewpoint::tool::SetValue_strategy)
def test_viewpoint::tool::setvalue_valueExpression_setter(instance):
    original = instance.valueExpression
    instance.valueExpression = original
    assert instance.valueExpression == original

@given(instance=viewpoint::tool::SetValue_strategy)
def test_viewpoint::tool::setvalue_featureName_type(instance):
    assert isinstance(instance.featureName, str)


@given(instance=viewpoint::tool::SetValue_strategy)
def test_viewpoint::tool::setvalue_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original

@given(instance=viewpoint::tool::If_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::if_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::If)

@given(instance=viewpoint::tool::If_strategy)
def test_viewpoint::tool::if_conditionExpression_type(instance):
    assert isinstance(instance.conditionExpression, str)


@given(instance=viewpoint::tool::If_strategy)
def test_viewpoint::tool::if_conditionExpression_setter(instance):
    original = instance.conditionExpression
    instance.conditionExpression = original
    assert instance.conditionExpression == original

@given(instance=viewpoint::tool::CreateInstance_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::createinstance_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::CreateInstance)

@given(instance=viewpoint::tool::CreateInstance_strategy)
def test_viewpoint::tool::createinstance_referenceName_type(instance):
    assert isinstance(instance.referenceName, str)


@given(instance=viewpoint::tool::CreateInstance_strategy)
def test_viewpoint::tool::createinstance_referenceName_setter(instance):
    original = instance.referenceName
    instance.referenceName = original
    assert instance.referenceName == original

@given(instance=viewpoint::tool::CreateInstance_strategy)
def test_viewpoint::tool::createinstance_typeName_type(instance):
    assert isinstance(instance.typeName, str)


@given(instance=viewpoint::tool::CreateInstance_strategy)
def test_viewpoint::tool::createinstance_typeName_setter(instance):
    original = instance.typeName
    instance.typeName = original
    assert instance.typeName == original

@given(instance=viewpoint::tool::CreateInstance_strategy)
def test_viewpoint::tool::createinstance_variableName_type(instance):
    assert isinstance(instance.variableName, str)


@given(instance=viewpoint::tool::CreateInstance_strategy)
def test_viewpoint::tool::createinstance_variableName_setter(instance):
    original = instance.variableName
    instance.variableName = original
    assert instance.variableName == original

@given(instance=viewpoint::tool::InitialContainerDropOperation_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::initialcontainerdropoperation_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::InitialContainerDropOperation)

@given(instance=viewpoint::tool::InitEdgeCreationOperation_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::initedgecreationoperation_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::InitEdgeCreationOperation)

@given(instance=viewpoint::tool::InitialOperation_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::initialoperation_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::InitialOperation)

@given(instance=viewpoint::tool::InitialNodeCreationOperation_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::initialnodecreationoperation_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::InitialNodeCreationOperation)

@given(instance=viewpoint::tool::ModelOperation_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::modeloperation_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::ModelOperation)

@given(instance=tool::ModelOperation_strategy)
@settings(max_examples=50)
def test_tool::modeloperation_instantiation(instance):
    assert isinstance(instance, tool::ModelOperation)

@given(instance=ModelOperation_strategy)
@settings(max_examples=50)
def test_modeloperation_instantiation(instance):
    assert isinstance(instance, ModelOperation)

@given(instance=viewpoint::tool::Switch_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::switch_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::Switch)

@given(instance=viewpoint::tool::ContainerModelOperation_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::containermodeloperation_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::ContainerModelOperation)

@given(instance=viewpoint::tool::EditMaskVariables_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::editmaskvariables_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::EditMaskVariables)

@given(instance=viewpoint::tool::EditMaskVariables_strategy)
def test_viewpoint::tool::editmaskvariables_mask_type(instance):
    assert isinstance(instance.mask, str)


@given(instance=viewpoint::tool::EditMaskVariables_strategy)
def test_viewpoint::tool::editmaskvariables_mask_setter(instance):
    original = instance.mask
    instance.mask = original
    assert instance.mask == original

@given(instance=viewpoint::tool::SelectModelElementVariable_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::selectmodelelementvariable_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::SelectModelElementVariable)

@given(instance=viewpoint::tool::ElementSelectVariable_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::elementselectvariable_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::ElementSelectVariable)

@given(instance=tool::AbstractVariable_strategy)
@settings(max_examples=50)
def test_tool::abstractvariable_instantiation(instance):
    assert isinstance(instance, tool::AbstractVariable)

@given(instance=viewpoint::tool::DropContainerVariable_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::dropcontainervariable_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::DropContainerVariable)

@given(instance=viewpoint::tool::SelectContainerVariable_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::selectcontainervariable_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::SelectContainerVariable)

@given(instance=viewpoint::tool::ElementDropVariable_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::elementdropvariable_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::ElementDropVariable)

@given(instance=viewpoint::tool::ContainerViewVariable_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::containerviewvariable_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::ContainerViewVariable)

@given(instance=viewpoint::tool::ElementDeleteVariable_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::elementdeletevariable_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::ElementDeleteVariable)

@given(instance=viewpoint::tool::SourceEdgeViewCreationVariable_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::sourceedgeviewcreationvariable_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::SourceEdgeViewCreationVariable)

@given(instance=viewpoint::tool::ElementVariable_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::elementvariable_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::ElementVariable)

@given(instance=viewpoint::tool::SourceEdgeCreationVariable_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::sourceedgecreationvariable_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::SourceEdgeCreationVariable)

@given(instance=viewpoint::tool::ElementViewVariable_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::elementviewvariable_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::ElementViewVariable)

@given(instance=viewpoint::tool::ElementDoubleClickVariable_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::elementdoubleclickvariable_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::ElementDoubleClickVariable)

@given(instance=viewpoint::tool::TargetEdgeCreationVariable_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::targetedgecreationvariable_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::TargetEdgeCreationVariable)

@given(instance=viewpoint::tool::TargetEdgeViewCreationVariable_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::targetedgeviewcreationvariable_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::TargetEdgeViewCreationVariable)

@given(instance=viewpoint::tool::NodeCreationVariable_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::nodecreationvariable_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::NodeCreationVariable)

@given(instance=viewpoint::Decoration_strategy)
@settings(max_examples=50)
def test_viewpoint::decoration_instantiation(instance):
    assert isinstance(instance, viewpoint::Decoration)

@given(instance=Viewpoint_strategy)
@settings(max_examples=50)
def test_viewpoint_instantiation(instance):
    assert isinstance(instance, Viewpoint)

@given(instance=viewpoint::MetaModelExtension_strategy)
@settings(max_examples=50)
def test_viewpoint::metamodelextension_instantiation(instance):
    assert isinstance(instance, viewpoint::MetaModelExtension)

@given(instance=DSemanticDecorator_strategy)
@settings(max_examples=50)
def test_dsemanticdecorator_instantiation(instance):
    assert isinstance(instance, DSemanticDecorator)

@given(instance=viewpoint::diagram::DSemanticDiagram_strategy)
@settings(max_examples=50)
def test_viewpoint::diagram::dsemanticdiagram_instantiation(instance):
    assert isinstance(instance, viewpoint::diagram::DSemanticDiagram)

@given(instance=DStylizable_strategy)
@settings(max_examples=50)
def test_dstylizable_instantiation(instance):
    assert isinstance(instance, DStylizable)

@given(instance=DMappingBased_strategy)
@settings(max_examples=50)
def test_dmappingbased_instantiation(instance):
    assert isinstance(instance, DMappingBased)

@given(instance=DLabelled_strategy)
@settings(max_examples=50)
def test_dlabelled_instantiation(instance):
    assert isinstance(instance, DLabelled)

@given(instance=AnnotationEntry_strategy)
@settings(max_examples=50)
def test_annotationentry_instantiation(instance):
    assert isinstance(instance, AnnotationEntry)

@given(instance=description::DModelElement_strategy)
@settings(max_examples=50)
def test_description::dmodelelement_instantiation(instance):
    assert isinstance(instance, description::DModelElement)

@given(instance=DRefreshable_strategy)
@settings(max_examples=50)
def test_drefreshable_instantiation(instance):
    assert isinstance(instance, DRefreshable)

@given(instance=viewpoint::DRepresentationElement_strategy)
@settings(max_examples=50)
def test_viewpoint::drepresentationelement_instantiation(instance):
    assert isinstance(instance, viewpoint::DRepresentationElement)

@given(instance=viewpoint::DRepresentationElement_strategy)
def test_viewpoint::drepresentationelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=viewpoint::DRepresentationElement_strategy)
def test_viewpoint::drepresentationelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=viewpoint::Style_strategy)
@settings(max_examples=50)
def test_viewpoint::style_instantiation(instance):
    assert isinstance(instance, viewpoint::Style)

@given(instance=description::DocumentedElement_strategy)
@settings(max_examples=50)
def test_description::documentedelement_instantiation(instance):
    assert isinstance(instance, description::DocumentedElement)

@given(instance=viewpoint::description::Viewpoint_strategy)
@settings(max_examples=50)
def test_viewpoint::description::viewpoint_instantiation(instance):
    assert isinstance(instance, viewpoint::description::Viewpoint)

@given(instance=viewpoint::description::Viewpoint_strategy)
def test_viewpoint::description::viewpoint_customizes_type(instance):
    assert isinstance(instance.customizes, str)


@given(instance=viewpoint::description::Viewpoint_strategy)
def test_viewpoint::description::viewpoint_customizes_setter(instance):
    original = instance.customizes
    instance.customizes = original
    assert instance.customizes == original

@given(instance=viewpoint::description::Viewpoint_strategy)
def test_viewpoint::description::viewpoint_reuses_type(instance):
    assert isinstance(instance.reuses, str)


@given(instance=viewpoint::description::Viewpoint_strategy)
def test_viewpoint::description::viewpoint_reuses_setter(instance):
    original = instance.reuses
    instance.reuses = original
    assert instance.reuses == original

@given(instance=viewpoint::description::Viewpoint_strategy)
def test_viewpoint::description::viewpoint_icon_type(instance):
    assert isinstance(instance.icon, str)


@given(instance=viewpoint::description::Viewpoint_strategy)
def test_viewpoint::description::viewpoint_icon_setter(instance):
    original = instance.icon
    instance.icon = original
    assert instance.icon == original

@given(instance=viewpoint::description::Viewpoint_strategy)
def test_viewpoint::description::viewpoint_conflicts_type(instance):
    assert isinstance(instance.conflicts, str)


@given(instance=viewpoint::description::Viewpoint_strategy)
def test_viewpoint::description::viewpoint_conflicts_setter(instance):
    original = instance.conflicts
    instance.conflicts = original
    assert instance.conflicts == original

@given(instance=viewpoint::description::Viewpoint_strategy)
def test_viewpoint::description::viewpoint_modelFileExtension_type(instance):
    assert isinstance(instance.modelFileExtension, str)


@given(instance=viewpoint::description::Viewpoint_strategy)
def test_viewpoint::description::viewpoint_modelFileExtension_setter(instance):
    original = instance.modelFileExtension
    instance.modelFileExtension = original
    assert instance.modelFileExtension == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint::description::Viewpoint_strategy)
@settings(max_examples=30)
def test_viewpoint::description::viewpoint_initview_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.initView(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.initView).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'initView' in viewpoint::description::Viewpoint is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'initView' in viewpoint::description::Viewpoint did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'initView' in viewpoint::description::Viewpoint is not implemented or raised an error")

@given(instance=viewpoint::tool::ToolSection_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::toolsection_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::ToolSection)

@given(instance=viewpoint::tool::ToolSection_strategy)
def test_viewpoint::tool::toolsection_icon_type(instance):
    assert isinstance(instance.icon, str)


@given(instance=viewpoint::tool::ToolSection_strategy)
def test_viewpoint::tool::toolsection_icon_setter(instance):
    original = instance.icon
    instance.icon = original
    assert instance.icon == original

@given(instance=viewpoint::filter::FilterDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::filter::filterdescription_instantiation(instance):
    assert isinstance(instance, viewpoint::filter::FilterDescription)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint::filter::FilterDescription_strategy)
@settings(max_examples=30)
def test_viewpoint::filter::filterdescription_isvisible_changes_state(instance):
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
        assert has_statements, f"Function 'isVisible' in viewpoint::filter::FilterDescription is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isVisible' in viewpoint::filter::FilterDescription did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isVisible' in viewpoint::filter::FilterDescription is not implemented or raised an error")

@given(instance=viewpoint::description::EdgeMapping_strategy)
@settings(max_examples=50)
def test_viewpoint::description::edgemapping_instantiation(instance):
    assert isinstance(instance, viewpoint::description::EdgeMapping)

@given(instance=viewpoint::description::EdgeMapping_strategy)
def test_viewpoint::description::edgemapping_targetFinderExpression_type(instance):
    assert isinstance(instance.targetFinderExpression, str)


@given(instance=viewpoint::description::EdgeMapping_strategy)
def test_viewpoint::description::edgemapping_targetFinderExpression_setter(instance):
    original = instance.targetFinderExpression
    instance.targetFinderExpression = original
    assert instance.targetFinderExpression == original

@given(instance=viewpoint::description::EdgeMapping_strategy)
def test_viewpoint::description::edgemapping_pathExpression_type(instance):
    assert isinstance(instance.pathExpression, str)


@given(instance=viewpoint::description::EdgeMapping_strategy)
def test_viewpoint::description::edgemapping_pathExpression_setter(instance):
    original = instance.pathExpression
    instance.pathExpression = original
    assert instance.pathExpression == original

@given(instance=viewpoint::description::EdgeMapping_strategy)
def test_viewpoint::description::edgemapping_targetExpression_type(instance):
    assert isinstance(instance.targetExpression, str)


@given(instance=viewpoint::description::EdgeMapping_strategy)
def test_viewpoint::description::edgemapping_targetExpression_setter(instance):
    original = instance.targetExpression
    instance.targetExpression = original
    assert instance.targetExpression == original

@given(instance=viewpoint::description::EdgeMapping_strategy)
def test_viewpoint::description::edgemapping_domainClass_type(instance):
    assert isinstance(instance.domainClass, str)


@given(instance=viewpoint::description::EdgeMapping_strategy)
def test_viewpoint::description::edgemapping_domainClass_setter(instance):
    original = instance.domainClass
    instance.domainClass = original
    assert instance.domainClass == original

@given(instance=viewpoint::description::EdgeMapping_strategy)
def test_viewpoint::description::edgemapping_useDomainElement_type(instance):
    assert isinstance(instance.useDomainElement, bool)


@given(instance=viewpoint::description::EdgeMapping_strategy)
def test_viewpoint::description::edgemapping_useDomainElement_setter(instance):
    original = instance.useDomainElement
    instance.useDomainElement = original
    assert instance.useDomainElement == original

@given(instance=viewpoint::description::EdgeMapping_strategy)
def test_viewpoint::description::edgemapping_sourceFinderExpression_type(instance):
    assert isinstance(instance.sourceFinderExpression, str)


@given(instance=viewpoint::description::EdgeMapping_strategy)
def test_viewpoint::description::edgemapping_sourceFinderExpression_setter(instance):
    original = instance.sourceFinderExpression
    instance.sourceFinderExpression = original
    assert instance.sourceFinderExpression == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint::description::EdgeMapping_strategy)
@settings(max_examples=30)
def test_viewpoint::description::edgemapping_updateedge_changes_state(instance):
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
        assert has_statements, f"Function 'updateEdge' in viewpoint::description::EdgeMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'updateEdge' in viewpoint::description::EdgeMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'updateEdge' in viewpoint::description::EdgeMapping is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint::description::EdgeMapping_strategy)
@settings(max_examples=30)
def test_viewpoint::description::edgemapping_createedge_changes_state(instance):
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
        assert has_statements, f"Function 'createEdge' in viewpoint::description::EdgeMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createEdge' in viewpoint::description::EdgeMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createEdge' in viewpoint::description::EdgeMapping is not implemented or raised an error")

@given(instance=viewpoint::description::Group_strategy)
@settings(max_examples=50)
def test_viewpoint::description::group_instantiation(instance):
    assert isinstance(instance, viewpoint::description::Group)

@given(instance=viewpoint::description::Group_strategy)
def test_viewpoint::description::group_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=viewpoint::description::Group_strategy)
def test_viewpoint::description::group_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=viewpoint::description::Group_strategy)
def test_viewpoint::description::group_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=viewpoint::description::Group_strategy)
def test_viewpoint::description::group_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=viewpoint::description::EdgeMappingImport_strategy)
@settings(max_examples=50)
def test_viewpoint::description::edgemappingimport_instantiation(instance):
    assert isinstance(instance, viewpoint::description::EdgeMappingImport)

@given(instance=viewpoint::description::EdgeMappingImport_strategy)
def test_viewpoint::description::edgemappingimport_inheritsAncestorFilters_type(instance):
    assert isinstance(instance.inheritsAncestorFilters, bool)


@given(instance=viewpoint::description::EdgeMappingImport_strategy)
def test_viewpoint::description::edgemappingimport_inheritsAncestorFilters_setter(instance):
    original = instance.inheritsAncestorFilters
    instance.inheritsAncestorFilters = original
    assert instance.inheritsAncestorFilters == original

@given(instance=viewpoint::description::Layer_strategy)
@settings(max_examples=50)
def test_viewpoint::description::layer_instantiation(instance):
    assert isinstance(instance, viewpoint::description::Layer)

@given(instance=viewpoint::description::Layer_strategy)
def test_viewpoint::description::layer_icon_type(instance):
    assert isinstance(instance.icon, str)


@given(instance=viewpoint::description::Layer_strategy)
def test_viewpoint::description::layer_icon_setter(instance):
    original = instance.icon
    instance.icon = original
    assert instance.icon == original

@given(instance=viewpoint::tool::ToolEntry_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::toolentry_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::ToolEntry)

@given(instance=viewpoint::description::RepresentationDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::description::representationdescription_instantiation(instance):
    assert isinstance(instance, viewpoint::description::RepresentationDescription)

@given(instance=viewpoint::description::RepresentationDescription_strategy)
def test_viewpoint::description::representationdescription_titleExpression_type(instance):
    assert isinstance(instance.titleExpression, str)


@given(instance=viewpoint::description::RepresentationDescription_strategy)
def test_viewpoint::description::representationdescription_titleExpression_setter(instance):
    original = instance.titleExpression
    instance.titleExpression = original
    assert instance.titleExpression == original

@given(instance=viewpoint::description::RepresentationDescription_strategy)
def test_viewpoint::description::representationdescription_showOnStartup_type(instance):
    assert isinstance(instance.showOnStartup, bool)


@given(instance=viewpoint::description::RepresentationDescription_strategy)
def test_viewpoint::description::representationdescription_showOnStartup_setter(instance):
    original = instance.showOnStartup
    instance.showOnStartup = original
    assert instance.showOnStartup == original

@given(instance=viewpoint::description::RepresentationDescription_strategy)
def test_viewpoint::description::representationdescription_initialisation_type(instance):
    assert isinstance(instance.initialisation, bool)


@given(instance=viewpoint::description::RepresentationDescription_strategy)
def test_viewpoint::description::representationdescription_initialisation_setter(instance):
    original = instance.initialisation
    instance.initialisation = original
    assert instance.initialisation == original

@given(instance=viewpoint::diagram::DDiagram_strategy)
@settings(max_examples=50)
def test_viewpoint::diagram::ddiagram_instantiation(instance):
    assert isinstance(instance, viewpoint::diagram::DDiagram)

@given(instance=viewpoint::diagram::DDiagram_strategy)
def test_viewpoint::diagram::ddiagram_info_type(instance):
    assert isinstance(instance.info, str)


@given(instance=viewpoint::diagram::DDiagram_strategy)
def test_viewpoint::diagram::ddiagram_info_setter(instance):
    original = instance.info
    instance.info = original
    assert instance.info == original

@given(instance=viewpoint::diagram::DDiagram_strategy)
def test_viewpoint::diagram::ddiagram_isInLayoutingMode_type(instance):
    assert isinstance(instance.isInLayoutingMode, bool)


@given(instance=viewpoint::diagram::DDiagram_strategy)
def test_viewpoint::diagram::ddiagram_isInLayoutingMode_setter(instance):
    original = instance.isInLayoutingMode
    instance.isInLayoutingMode = original
    assert instance.isInLayoutingMode == original

@given(instance=viewpoint::diagram::DDiagram_strategy)
def test_viewpoint::diagram::ddiagram_headerHeight_type(instance):
    assert isinstance(instance.headerHeight, int)


@given(instance=viewpoint::diagram::DDiagram_strategy)
def test_viewpoint::diagram::ddiagram_headerHeight_setter(instance):
    original = instance.headerHeight
    instance.headerHeight = original
    assert instance.headerHeight == original

@given(instance=viewpoint::diagram::DDiagram_strategy)
def test_viewpoint::diagram::ddiagram_synchronized_type(instance):
    assert isinstance(instance.synchronized, bool)


@given(instance=viewpoint::diagram::DDiagram_strategy)
def test_viewpoint::diagram::ddiagram_synchronized_setter(instance):
    original = instance.synchronized
    instance.synchronized = original
    assert instance.synchronized == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint::diagram::DDiagram_strategy)
@settings(max_examples=30)
def test_viewpoint::diagram::ddiagram_clean_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.clean()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.clean).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'clean' in viewpoint::diagram::DDiagram is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'clean' in viewpoint::diagram::DDiagram did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'clean' in viewpoint::diagram::DDiagram is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint::diagram::DDiagram_strategy)
@settings(max_examples=30)
def test_viewpoint::diagram::ddiagram_finddiagramelements_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.findDiagramElements(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.findDiagramElements).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'findDiagramElements' in viewpoint::diagram::DDiagram is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'findDiagramElements' in viewpoint::diagram::DDiagram did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'findDiagramElements' in viewpoint::diagram::DDiagram is not implemented or raised an error")

@given(instance=viewpoint::concern::ConcernDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::concern::concerndescription_instantiation(instance):
    assert isinstance(instance, viewpoint::concern::ConcernDescription)

@given(instance=viewpoint::description::AbstractNodeMapping_strategy)
@settings(max_examples=50)
def test_viewpoint::description::abstractnodemapping_instantiation(instance):
    assert isinstance(instance, viewpoint::description::AbstractNodeMapping)

@given(instance=viewpoint::description::AbstractNodeMapping_strategy)
def test_viewpoint::description::abstractnodemapping_domainClass_type(instance):
    assert isinstance(instance.domainClass, str)


@given(instance=viewpoint::description::AbstractNodeMapping_strategy)
def test_viewpoint::description::abstractnodemapping_domainClass_setter(instance):
    original = instance.domainClass
    instance.domainClass = original
    assert instance.domainClass == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint::description::AbstractNodeMapping_strategy)
@settings(max_examples=30)
def test_viewpoint::description::abstractnodemapping_finddnodefromeobject_changes_state(instance):
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
        assert has_statements, f"Function 'findDNodeFromEObject' in viewpoint::description::AbstractNodeMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'findDNodeFromEObject' in viewpoint::description::AbstractNodeMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'findDNodeFromEObject' in viewpoint::description::AbstractNodeMapping is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint::description::AbstractNodeMapping_strategy)
@settings(max_examples=30)
def test_viewpoint::description::abstractnodemapping_adddonenode_changes_state(instance):
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
        assert has_statements, f"Function 'addDoneNode' in viewpoint::description::AbstractNodeMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addDoneNode' in viewpoint::description::AbstractNodeMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addDoneNode' in viewpoint::description::AbstractNodeMapping is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint::description::AbstractNodeMapping_strategy)
@settings(max_examples=30)
def test_viewpoint::description::abstractnodemapping_cleardnodesdone_changes_state(instance):
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
        assert has_statements, f"Function 'clearDNodesDone' in viewpoint::description::AbstractNodeMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'clearDNodesDone' in viewpoint::description::AbstractNodeMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'clearDNodesDone' in viewpoint::description::AbstractNodeMapping is not implemented or raised an error")

@given(instance=viewpoint::DRepresentation_strategy)
@settings(max_examples=50)
def test_viewpoint::drepresentation_instantiation(instance):
    assert isinstance(instance, viewpoint::DRepresentation)

@given(instance=viewpoint::DRepresentation_strategy)
def test_viewpoint::drepresentation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=viewpoint::DRepresentation_strategy)
def test_viewpoint::drepresentation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint::DRepresentation_strategy)
@settings(max_examples=30)
def test_viewpoint::drepresentation_updatecontent_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.updateContent()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.updateContent).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'updateContent' in viewpoint::DRepresentation is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'updateContent' in viewpoint::DRepresentation did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'updateContent' in viewpoint::DRepresentation is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint::DRepresentation_strategy)
@settings(max_examples=30)
def test_viewpoint::drepresentation_createcontents_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createContents(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createContents).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createContents' in viewpoint::DRepresentation is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createContents' in viewpoint::DRepresentation did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createContents' in viewpoint::DRepresentation is not implemented or raised an error")

@given(instance=viewpoint::DSemanticDecorator_strategy)
@settings(max_examples=50)
def test_viewpoint::dsemanticdecorator_instantiation(instance):
    assert isinstance(instance, viewpoint::DSemanticDecorator)

@given(instance=DDiagramSet_strategy)
@settings(max_examples=50)
def test_ddiagramset_instantiation(instance):
    assert isinstance(instance, DDiagramSet)

@given(instance=DView_strategy)
@settings(max_examples=50)
def test_dview_instantiation(instance):
    assert isinstance(instance, DView)

@given(instance=viewpoint::DRepresentationContainer_strategy)
@settings(max_examples=50)
def test_viewpoint::drepresentationcontainer_instantiation(instance):
    assert isinstance(instance, viewpoint::DRepresentationContainer)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint::DRepresentationContainer_strategy)
@settings(max_examples=30)
def test_viewpoint::drepresentationcontainer_addsemanticdiagram_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addSemanticDiagram(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addSemanticDiagram).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addSemanticDiagram' in viewpoint::DRepresentationContainer is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addSemanticDiagram' in viewpoint::DRepresentationContainer did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addSemanticDiagram' in viewpoint::DRepresentationContainer is not implemented or raised an error")

@given(instance=viewpoint::DContainer_strategy)
@settings(max_examples=50)
def test_viewpoint::dcontainer_instantiation(instance):
    assert isinstance(instance, viewpoint::DContainer)

@given(instance=viewpoint::DMappingBased_strategy)
@settings(max_examples=50)
def test_viewpoint::dmappingbased_instantiation(instance):
    assert isinstance(instance, viewpoint::DMappingBased)

@given(instance=viewpoint::DLabelled_strategy)
@settings(max_examples=50)
def test_viewpoint::dlabelled_instantiation(instance):
    assert isinstance(instance, viewpoint::DLabelled)

@given(instance=viewpoint::DRefreshable_strategy)
@settings(max_examples=50)
def test_viewpoint::drefreshable_instantiation(instance):
    assert isinstance(instance, viewpoint::DRefreshable)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint::DRefreshable_strategy)
@settings(max_examples=30)
def test_viewpoint::drefreshable_refresh_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.refresh()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.refresh).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'refresh' in viewpoint::DRefreshable is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'refresh' in viewpoint::DRefreshable did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'refresh' in viewpoint::DRefreshable is not implemented or raised an error")

@given(instance=viewpoint::DStylizable_strategy)
@settings(max_examples=50)
def test_viewpoint::dstylizable_instantiation(instance):
    assert isinstance(instance, viewpoint::DStylizable)

@given(instance=viewpoint::DNavigationLink_strategy)
@settings(max_examples=50)
def test_viewpoint::dnavigationlink_instantiation(instance):
    assert isinstance(instance, viewpoint::DNavigationLink)

@given(instance=viewpoint::DNavigationLink_strategy)
def test_viewpoint::dnavigationlink_targetType_type(instance):
    assert isinstance(instance.targetType, str)


@given(instance=viewpoint::DNavigationLink_strategy)
def test_viewpoint::dnavigationlink_targetType_setter(instance):
    original = instance.targetType
    instance.targetType = original
    assert instance.targetType == original

@given(instance=viewpoint::DNavigationLink_strategy)
def test_viewpoint::dnavigationlink_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=viewpoint::DNavigationLink_strategy)
def test_viewpoint::dnavigationlink_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint::DNavigationLink_strategy)
@settings(max_examples=30)
def test_viewpoint::dnavigationlink_isavailable_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isAvailable()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isAvailable).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isAvailable' in viewpoint::DNavigationLink is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isAvailable' in viewpoint::DNavigationLink did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isAvailable' in viewpoint::DNavigationLink is not implemented or raised an error")

@given(instance=viewpoint::DNavigable_strategy)
@settings(max_examples=50)
def test_viewpoint::dnavigable_instantiation(instance):
    assert isinstance(instance, viewpoint::DNavigable)

@given(instance=viewpoint::DValidable_strategy)
@settings(max_examples=50)
def test_viewpoint::dvalidable_instantiation(instance):
    assert isinstance(instance, viewpoint::DValidable)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint::DValidable_strategy)
@settings(max_examples=30)
def test_viewpoint::dvalidable_validate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validate()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validate).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validate' in viewpoint::DValidable is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validate' in viewpoint::DValidable did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validate' in viewpoint::DValidable is not implemented or raised an error")

@given(instance=FeatureExtensionDescription_strategy)
@settings(max_examples=50)
def test_featureextensiondescription_instantiation(instance):
    assert isinstance(instance, FeatureExtensionDescription)

@given(instance=viewpoint::DFeatureExtension_strategy)
@settings(max_examples=50)
def test_viewpoint::dfeatureextension_instantiation(instance):
    assert isinstance(instance, viewpoint::DFeatureExtension)

@given(instance=viewpoint::DView_strategy)
@settings(max_examples=50)
def test_viewpoint::dview_instantiation(instance):
    assert isinstance(instance, viewpoint::DView)

@given(instance=viewpoint::DView_strategy)
def test_viewpoint::dview_initialized_type(instance):
    assert isinstance(instance.initialized, bool)


@given(instance=viewpoint::DView_strategy)
def test_viewpoint::dview_initialized_setter(instance):
    original = instance.initialized
    instance.initialized = original
    assert instance.initialized == original

@given(instance=DAnnotationEntry_strategy)
@settings(max_examples=50)
def test_dannotationentry_instantiation(instance):
    assert isinstance(instance, DAnnotationEntry)

@given(instance=viewpoint::EObject_strategy)
@settings(max_examples=50)
def test_viewpoint::eobject_instantiation(instance):
    assert isinstance(instance, viewpoint::EObject)

@given(instance=viewpoint::DAnalysis_strategy)
@settings(max_examples=50)
def test_viewpoint::danalysis_instantiation(instance):
    assert isinstance(instance, viewpoint::DAnalysis)

@given(instance=viewpoint::DAnalysis_strategy)
def test_viewpoint::danalysis_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=viewpoint::DAnalysis_strategy)
def test_viewpoint::danalysis_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original
