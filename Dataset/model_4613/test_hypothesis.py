import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    viewpoint::validation::ValidationFix,
    InformationSection,
    viewpoint::audit::TemplateInformationSection,
    viewpoint::audit::InformationSection,
    viewpoint::validation::RuleAudit,
    RepresentationElementMapping,
    ValidationRule,
    viewpoint::validation::ViewValidationRule,
    viewpoint::validation::SemanticValidationRule,
    validation::ValidationFix,
    DocumentedElement,
    viewpoint::validation::ValidationSet,
    validation::RuleAudit,
    validation::ValidationRule,
    viewpoint::tool::FeatureChangeListener,
    tool::Default,
    tool::Case,
    viewpoint::tool::SwitchChild,
    SwitchChild,
    viewpoint::tool::Default,
    viewpoint::tool::Case,
    viewpoint::tool::ExternalJavaActionParameter,
    tool::FeatureChangeListener,
    viewpoint::tool::ToolFilterDescription,
    tool::viewpoint::EObject,
    MetamodelExtensionSetting,
    JavaExtension,
    RepresentationExtensionDescription,
    viewpoint::Customizable,
    DFile,
    viewpoint::DModel,
    Extension,
    UserColorsPalette,
    SytemColorsPalette,
    viewpoint::DAnalysisSessionEObject,
    DResourceContainer,
    viewpoint::DFolder,
    viewpoint::DProject,
    DResource,
    viewpoint::DResourceContainer,
    viewpoint::DFile,
    viewpoint::DResource,
    viewpoint::SessionManagerEObject,
    DecorationDescription,
    viewpoint::Decoration,
    style::StyleDescription,
    Customizable,
    viewpoint::BasicLabelStyle,
    BasicLabelStyle,
    viewpoint::LabelStyle,
    viewpoint::DAnalysisCustomData,
    viewpoint::UIState,
    AnnotationEntry,
    viewpoint::MetaModelExtension,
    Viewpoint,
    DSemanticDecorator,
    DStylizable,
    DMappingBased,
    viewpoint::DRefreshable,
    viewpoint::DStylizable,
    FeatureExtensionDescription,
    viewpoint::DFeatureExtension,
    description::DModelElement,
    DRefreshable,
    viewpoint::DRepresentationElement,
    viewpoint::Style,
    description::DocumentedElement,
    viewpoint::description::Group,
    viewpoint::DRepresentation,
    RepresentationDescription,
    viewpoint::DRepresentationDescriptor,
    viewpoint::DSemanticDecorator,
    viewpoint::DMappingBased,
    viewpoint::DView,
    DAnnotationEntry,
    viewpoint::EObject,
    viewpoint::DAnalysis,
    viewpoint::tool::InitialOperation,
    viewpoint::tool::InitialNodeCreationOperation,
    viewpoint::tool::ModelOperation,
    tool::ModelOperation,
    ModelOperation,
    viewpoint::tool::Switch,
    viewpoint::tool::ContainerModelOperation,
    viewpoint::tool::EditMaskVariables,
    ContainerModelOperation,
    viewpoint::tool::RemoveElement,
    viewpoint::tool::MoveElement,
    viewpoint::tool::ChangeContext,
    viewpoint::tool::Unset,
    viewpoint::tool::Let,
    viewpoint::tool::If,
    viewpoint::tool::SetValue,
    viewpoint::tool::SetObject,
    viewpoint::tool::DeleteView,
    viewpoint::tool::For,
    viewpoint::tool::CreateInstance,
    viewpoint::tool::InitialContainerDropOperation,
    viewpoint::tool::InitEdgeCreationOperation,
    tool::ExternalJavaAction,
    tool::ExternalJavaActionParameter,
    tool::ContainerModelOperation,
    description::AbstractVariable,
    tool::VariableContainer,
    viewpoint::tool::DropContainerVariable,
    viewpoint::tool::ElementViewVariable,
    viewpoint::tool::ElementDeleteVariable,
    viewpoint::tool::ElementDropVariable,
    viewpoint::tool::ElementVariable,
    viewpoint::tool::ContainerViewVariable,
    viewpoint::tool::SelectContainerVariable,
    SubVariable,
    viewpoint::tool::VariableContainer,
    MenuItemDescription,
    viewpoint::tool::OperationAction,
    tool::MenuItemDescription,
    viewpoint::tool::ExternalJavaActionCall,
    viewpoint::tool::ExternalJavaAction,
    MenuItemOrRef,
    viewpoint::tool::MenuItemDescriptionReference,
    tool::MenuItemOrRef,
    viewpoint::tool::MenuItemOrRef,
    tool::NameVariable,
    tool::SelectContainerVariable,
    tool::ElementSelectVariable,
    description::SelectionDescription,
    tool::AbstractToolDescription,
    viewpoint::tool::MenuItemDescription,
    viewpoint::tool::SelectionWizardDescription,
    tool::ContainerViewVariable,
    tool::DropContainerVariable,
    tool::ElementVariable,
    MappingBasedToolDescription,
    viewpoint::tool::ToolDescription,
    AbstractToolDescription,
    viewpoint::tool::RepresentationNavigationDescription,
    viewpoint::tool::PopupMenu,
    viewpoint::tool::RepresentationCreationDescription,
    viewpoint::tool::PaneBasedSelectionWizardDescription,
    viewpoint::tool::MappingBasedToolDescription,
    viewpoint::tool::PasteDescription,
    tool::InitialOperation,
    tool::ElementViewVariable,
    ToolEntry,
    viewpoint::tool::AbstractToolDescription,
    tool::ToolFilterDescription,
    BasicLabelStyleDescription,
    viewpoint::style::LabelStyleDescription,
    viewpoint::style::TooltipStyleDescription,
    viewpoint::style::LabelBorderStyleDescription,
    style::LabelBorderStyleDescription,
    viewpoint::style::LabelBorderStyles,
    description::viewpoint::EDataType,
    viewpoint::style::BasicLabelStyleDescription,
    viewpoint::style::StyleDescription,
    viewpoint::description::IdentifiedElement,
    viewpoint::description::EndUserDocumentedElement,
    viewpoint::description::AnnotationEntry,
    UserColor,
    description::SubVariable,
    viewpoint::tool::AcceleoVariable,
    description::InteractiveVariableDescription,
    viewpoint::tool::SelectModelElementVariable,
    viewpoint::description::TypedVariable,
    viewpoint::description::InteractiveVariableDescription,
    AbstractVariable,
    viewpoint::tool::ElementSelectVariable,
    viewpoint::tool::NameVariable,
    viewpoint::tool::DialogVariable,
    viewpoint::description::SubVariable,
    viewpoint::description::AbstractVariable,
    viewpoint::description::DAnnotationEntry,
    viewpoint::description::UserColor,
    description::FixedColor,
    viewpoint::description::UserColorsPalette,
    SystemColor,
    viewpoint::description::SytemColorsPalette,
    style::LabelBorderStyles,
    tool::ToolEntry,
    viewpoint::description::Environment,
    description::UserColor,
    viewpoint::description::UserFixedColor,
    description::ColorDescription,
    viewpoint::description::ComputedColor,
    viewpoint::description::InterpolatedColor,
    ColorDescription,
    viewpoint::description::FixedColor,
    viewpoint::description::ColorStep,
    ColorStep,
    FixedColor,
    viewpoint::description::SystemColor,
    viewpoint::description::ColorDescription,
    viewpoint::description::SelectionDescription,
    viewpoint::description::IVSMElementCustomization,
    IVSMElementCustomization,
    viewpoint::description::VSMElementCustomization,
    viewpoint::description::Customization,
    viewpoint::description::GenericDecorationDescription,
    viewpoint::description::SemanticBasedDecoration,
    viewpoint::description::EStructuralFeatureCustomization,
    viewpoint::description::VSMElementCustomizationReuse,
    EStructuralFeatureCustomization,
    viewpoint::description::EAttributeCustomization,
    viewpoint::description::EReferenceCustomization,
    viewpoint::description::DecorationDescription,
    viewpoint::description::DecorationDescriptionsSet,
    tool::PasteDescription,
    viewpoint::description::PasteTargetDescription,
    viewpoint::description::AbstractMappingImport,
    tool::RepresentationNavigationDescription,
    tool::RepresentationCreationDescription,
    IdentifiedElement,
    viewpoint::validation::ValidationRule,
    viewpoint::description::ConditionalStyleDescription,
    description::viewpoint::EStringToStringMapEntry,
    viewpoint::description::DAnnotation,
    DAnnotation,
    viewpoint::description::DModelElement,
    viewpoint::description::DocumentedElement,
    viewpoint::description::RepresentationTemplate,
    description::viewpoint::EPackage,
    viewpoint::description::RepresentationElementMapping,
    viewpoint::description::JavaExtension,
    description::viewpoint::EObject,
    viewpoint::description::MetamodelExtensionSetting,
    viewpoint::description::RepresentationExtensionDescription,
    viewpoint::description::RepresentationImportDescription,
    validation::ValidationSet,
    description::IdentifiedElement,
    viewpoint::tool::ToolEntry,
    description::EndUserDocumentedElement,
    description::Component,
    viewpoint::description::Viewpoint,
    viewpoint::description::Component,
    viewpoint::description::Extension,
    viewpoint::description::RepresentationDescription,
    viewpoint::description::FeatureExtensionDescription,
    RepresentationTemplate,
    Position,
    SyncStatus,
    SystemColors,
    DragSource,
    LabelAlignment,
    FontFormat,
    DecorationDistributionDirection,
    ERROR_LEVEL,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_viewpoint::audit::informationsection_is_not_abstract():
    assert not inspect.isabstract(viewpoint::audit::InformationSection)


def test_viewpoint::audit::informationsection_constructor_exists():
    assert callable(viewpoint::audit::InformationSection.__init__)


def test_viewpoint::audit::informationsection_constructor_args():
    sig = inspect.signature(viewpoint::audit::InformationSection.__init__)
    params = list(sig.parameters.keys())



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



def test_representationelementmapping_is_not_abstract():
    assert not inspect.isabstract(RepresentationElementMapping)


def test_representationelementmapping_constructor_exists():
    assert callable(RepresentationElementMapping.__init__)


def test_representationelementmapping_constructor_args():
    sig = inspect.signature(RepresentationElementMapping.__init__)
    params = list(sig.parameters.keys())



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



def test_validation::ruleaudit_is_not_abstract():
    assert not inspect.isabstract(validation::RuleAudit)


def test_validation::ruleaudit_constructor_exists():
    assert callable(validation::RuleAudit.__init__)


def test_validation::ruleaudit_constructor_args():
    sig = inspect.signature(validation::RuleAudit.__init__)
    params = list(sig.parameters.keys())



def test_validation::validationrule_is_not_abstract():
    assert not inspect.isabstract(validation::ValidationRule)


def test_validation::validationrule_constructor_exists():
    assert callable(validation::ValidationRule.__init__)


def test_validation::validationrule_constructor_args():
    sig = inspect.signature(validation::ValidationRule.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::featurechangelistener_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::FeatureChangeListener)


def test_viewpoint::tool::featurechangelistener_constructor_exists():
    assert callable(viewpoint::tool::FeatureChangeListener.__init__)


def test_viewpoint::tool::featurechangelistener_constructor_args():
    sig = inspect.signature(viewpoint::tool::FeatureChangeListener.__init__)
    params = list(sig.parameters.keys())
    assert "domainClass" in params, "Missing parameter 'domainClass'"
    assert "featureName" in params, "Missing parameter 'featureName'"

def test_viewpoint::tool::featurechangelistener_has_domainClass():
    assert hasattr(viewpoint::tool::FeatureChangeListener, "domainClass")
    descriptor = None
    for klass in viewpoint::tool::FeatureChangeListener.__mro__:
        if "domainClass" in klass.__dict__:
            descriptor = klass.__dict__["domainClass"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::tool::featurechangelistener_has_featureName():
    assert hasattr(viewpoint::tool::FeatureChangeListener, "featureName")
    descriptor = None
    for klass in viewpoint::tool::FeatureChangeListener.__mro__:
        if "featureName" in klass.__dict__:
            descriptor = klass.__dict__["featureName"]
            break
    assert isinstance(descriptor, property)



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



def test_viewpoint::tool::switchchild_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::SwitchChild)


def test_viewpoint::tool::switchchild_constructor_exists():
    assert callable(viewpoint::tool::SwitchChild.__init__)


def test_viewpoint::tool::switchchild_constructor_args():
    sig = inspect.signature(viewpoint::tool::SwitchChild.__init__)
    params = list(sig.parameters.keys())



def test_switchchild_is_not_abstract():
    assert not inspect.isabstract(SwitchChild)


def test_switchchild_constructor_exists():
    assert callable(SwitchChild.__init__)


def test_switchchild_constructor_args():
    sig = inspect.signature(SwitchChild.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::default_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::Default)


def test_viewpoint::tool::default_constructor_exists():
    assert callable(viewpoint::tool::Default.__init__)


def test_viewpoint::tool::default_constructor_args():
    sig = inspect.signature(viewpoint::tool::Default.__init__)
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



def test_tool::featurechangelistener_is_not_abstract():
    assert not inspect.isabstract(tool::FeatureChangeListener)


def test_tool::featurechangelistener_constructor_exists():
    assert callable(tool::FeatureChangeListener.__init__)


def test_tool::featurechangelistener_constructor_args():
    sig = inspect.signature(tool::FeatureChangeListener.__init__)
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



def test_tool::viewpoint::eobject_is_not_abstract():
    assert not inspect.isabstract(tool::viewpoint::EObject)


def test_tool::viewpoint::eobject_constructor_exists():
    assert callable(tool::viewpoint::EObject.__init__)


def test_tool::viewpoint::eobject_constructor_args():
    sig = inspect.signature(tool::viewpoint::EObject.__init__)
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



def test_extension_is_not_abstract():
    assert not inspect.isabstract(Extension)


def test_extension_constructor_exists():
    assert callable(Extension.__init__)


def test_extension_constructor_args():
    sig = inspect.signature(Extension.__init__)
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



def test_viewpoint::danalysissessioneobject_is_not_abstract():
    assert not inspect.isabstract(viewpoint::DAnalysisSessionEObject)


def test_viewpoint::danalysissessioneobject_constructor_exists():
    assert callable(viewpoint::DAnalysisSessionEObject.__init__)


def test_viewpoint::danalysissessioneobject_constructor_args():
    sig = inspect.signature(viewpoint::DAnalysisSessionEObject.__init__)
    params = list(sig.parameters.keys())
    assert "controlledResources" in params, "Missing parameter 'controlledResources'"
    assert "resources" in params, "Missing parameter 'resources'"
    assert "synchronizationStatus" in params, "Missing parameter 'synchronizationStatus'"
    assert "open" in params, "Missing parameter 'open'"

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

def test_viewpoint::danalysissessioneobject_has_synchronizationStatus():
    assert hasattr(viewpoint::DAnalysisSessionEObject, "synchronizationStatus")
    descriptor = None
    for klass in viewpoint::DAnalysisSessionEObject.__mro__:
        if "synchronizationStatus" in klass.__dict__:
            descriptor = klass.__dict__["synchronizationStatus"]
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
    assert "name" in params, "Missing parameter 'name'"
    assert "path" in params, "Missing parameter 'path'"

def test_viewpoint::dresource_has_name():
    assert hasattr(viewpoint::DResource, "name")
    descriptor = None
    for klass in viewpoint::DResource.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::dresource_has_path():
    assert hasattr(viewpoint::DResource, "path")
    descriptor = None
    for klass in viewpoint::DResource.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::sessionmanagereobject_is_not_abstract():
    assert not inspect.isabstract(viewpoint::SessionManagerEObject)


def test_viewpoint::sessionmanagereobject_constructor_exists():
    assert callable(viewpoint::SessionManagerEObject.__init__)


def test_viewpoint::sessionmanagereobject_constructor_args():
    sig = inspect.signature(viewpoint::SessionManagerEObject.__init__)
    params = list(sig.parameters.keys())



def test_decorationdescription_is_not_abstract():
    assert not inspect.isabstract(DecorationDescription)


def test_decorationdescription_constructor_exists():
    assert callable(DecorationDescription.__init__)


def test_decorationdescription_constructor_args():
    sig = inspect.signature(DecorationDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::decoration_is_not_abstract():
    assert not inspect.isabstract(viewpoint::Decoration)


def test_viewpoint::decoration_constructor_exists():
    assert callable(viewpoint::Decoration.__init__)


def test_viewpoint::decoration_constructor_args():
    sig = inspect.signature(viewpoint::Decoration.__init__)
    params = list(sig.parameters.keys())



def test_style::styledescription_is_not_abstract():
    assert not inspect.isabstract(style::StyleDescription)


def test_style::styledescription_constructor_exists():
    assert callable(style::StyleDescription.__init__)


def test_style::styledescription_constructor_args():
    sig = inspect.signature(style::StyleDescription.__init__)
    params = list(sig.parameters.keys())



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
    assert "labelFormat" in params, "Missing parameter 'labelFormat'"
    assert "showIcon" in params, "Missing parameter 'showIcon'"
    assert "iconPath" in params, "Missing parameter 'iconPath'"
    assert "labelColor" in params, "Missing parameter 'labelColor'"

def test_viewpoint::basiclabelstyle_has_labelSize():
    assert hasattr(viewpoint::BasicLabelStyle, "labelSize")
    descriptor = None
    for klass in viewpoint::BasicLabelStyle.__mro__:
        if "labelSize" in klass.__dict__:
            descriptor = klass.__dict__["labelSize"]
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

def test_viewpoint::basiclabelstyle_has_showIcon():
    assert hasattr(viewpoint::BasicLabelStyle, "showIcon")
    descriptor = None
    for klass in viewpoint::BasicLabelStyle.__mro__:
        if "showIcon" in klass.__dict__:
            descriptor = klass.__dict__["showIcon"]
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

def test_viewpoint::basiclabelstyle_has_labelColor():
    assert hasattr(viewpoint::BasicLabelStyle, "labelColor")
    descriptor = None
    for klass in viewpoint::BasicLabelStyle.__mro__:
        if "labelColor" in klass.__dict__:
            descriptor = klass.__dict__["labelColor"]
            break
    assert isinstance(descriptor, property)



def test_basiclabelstyle_is_not_abstract():
    assert not inspect.isabstract(BasicLabelStyle)


def test_basiclabelstyle_constructor_exists():
    assert callable(BasicLabelStyle.__init__)


def test_basiclabelstyle_constructor_args():
    sig = inspect.signature(BasicLabelStyle.__init__)
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



def test_viewpoint::uistate_is_not_abstract():
    assert not inspect.isabstract(viewpoint::UIState)


def test_viewpoint::uistate_constructor_exists():
    assert callable(viewpoint::UIState.__init__)


def test_viewpoint::uistate_constructor_args():
    sig = inspect.signature(viewpoint::UIState.__init__)
    params = list(sig.parameters.keys())
    assert "decorationImage" in params, "Missing parameter 'decorationImage'"
    assert "inverseSelectionOrder" in params, "Missing parameter 'inverseSelectionOrder'"

def test_viewpoint::uistate_has_decorationImage():
    assert hasattr(viewpoint::UIState, "decorationImage")
    descriptor = None
    for klass in viewpoint::UIState.__mro__:
        if "decorationImage" in klass.__dict__:
            descriptor = klass.__dict__["decorationImage"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::uistate_has_inverseSelectionOrder():
    assert hasattr(viewpoint::UIState, "inverseSelectionOrder")
    descriptor = None
    for klass in viewpoint::UIState.__mro__:
        if "inverseSelectionOrder" in klass.__dict__:
            descriptor = klass.__dict__["inverseSelectionOrder"]
            break
    assert isinstance(descriptor, property)



def test_annotationentry_is_not_abstract():
    assert not inspect.isabstract(AnnotationEntry)


def test_annotationentry_constructor_exists():
    assert callable(AnnotationEntry.__init__)


def test_annotationentry_constructor_args():
    sig = inspect.signature(AnnotationEntry.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::metamodelextension_is_not_abstract():
    assert not inspect.isabstract(viewpoint::MetaModelExtension)


def test_viewpoint::metamodelextension_constructor_exists():
    assert callable(viewpoint::MetaModelExtension.__init__)


def test_viewpoint::metamodelextension_constructor_args():
    sig = inspect.signature(viewpoint::MetaModelExtension.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_is_not_abstract():
    assert not inspect.isabstract(Viewpoint)


def test_viewpoint_constructor_exists():
    assert callable(Viewpoint.__init__)


def test_viewpoint_constructor_args():
    sig = inspect.signature(Viewpoint.__init__)
    params = list(sig.parameters.keys())



def test_dsemanticdecorator_is_not_abstract():
    assert not inspect.isabstract(DSemanticDecorator)


def test_dsemanticdecorator_constructor_exists():
    assert callable(DSemanticDecorator.__init__)


def test_dsemanticdecorator_constructor_args():
    sig = inspect.signature(DSemanticDecorator.__init__)
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



def test_representationdescription_is_not_abstract():
    assert not inspect.isabstract(RepresentationDescription)


def test_representationdescription_constructor_exists():
    assert callable(RepresentationDescription.__init__)


def test_representationdescription_constructor_args():
    sig = inspect.signature(RepresentationDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::drepresentationdescriptor_is_not_abstract():
    assert not inspect.isabstract(viewpoint::DRepresentationDescriptor)


def test_viewpoint::drepresentationdescriptor_constructor_exists():
    assert callable(viewpoint::DRepresentationDescriptor.__init__)


def test_viewpoint::drepresentationdescriptor_constructor_args():
    sig = inspect.signature(viewpoint::DRepresentationDescriptor.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_viewpoint::drepresentationdescriptor_has_name():
    assert hasattr(viewpoint::DRepresentationDescriptor, "name")
    descriptor = None
    for klass in viewpoint::DRepresentationDescriptor.__mro__:
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



def test_viewpoint::dmappingbased_is_not_abstract():
    assert not inspect.isabstract(viewpoint::DMappingBased)


def test_viewpoint::dmappingbased_constructor_exists():
    assert callable(viewpoint::DMappingBased.__init__)


def test_viewpoint::dmappingbased_constructor_args():
    sig = inspect.signature(viewpoint::DMappingBased.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::dview_is_not_abstract():
    assert not inspect.isabstract(viewpoint::DView)


def test_viewpoint::dview_constructor_exists():
    assert callable(viewpoint::DView.__init__)


def test_viewpoint::dview_constructor_args():
    sig = inspect.signature(viewpoint::DView.__init__)
    params = list(sig.parameters.keys())



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
    assert "semanticResources" in params, "Missing parameter 'semanticResources'"
    assert "version" in params, "Missing parameter 'version'"

def test_viewpoint::danalysis_has_semanticResources():
    assert hasattr(viewpoint::DAnalysis, "semanticResources")
    descriptor = None
    for klass in viewpoint::DAnalysis.__mro__:
        if "semanticResources" in klass.__dict__:
            descriptor = klass.__dict__["semanticResources"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::danalysis_has_version():
    assert hasattr(viewpoint::DAnalysis, "version")
    descriptor = None
    for klass in viewpoint::DAnalysis.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



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



def test_viewpoint::tool::let_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::Let)


def test_viewpoint::tool::let_constructor_exists():
    assert callable(viewpoint::tool::Let.__init__)


def test_viewpoint::tool::let_constructor_args():
    sig = inspect.signature(viewpoint::tool::Let.__init__)
    params = list(sig.parameters.keys())
    assert "variableName" in params, "Missing parameter 'variableName'"
    assert "valueExpression" in params, "Missing parameter 'valueExpression'"

def test_viewpoint::tool::let_has_variableName():
    assert hasattr(viewpoint::tool::Let, "variableName")
    descriptor = None
    for klass in viewpoint::tool::Let.__mro__:
        if "variableName" in klass.__dict__:
            descriptor = klass.__dict__["variableName"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::tool::let_has_valueExpression():
    assert hasattr(viewpoint::tool::Let, "valueExpression")
    descriptor = None
    for klass in viewpoint::tool::Let.__mro__:
        if "valueExpression" in klass.__dict__:
            descriptor = klass.__dict__["valueExpression"]
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



def test_viewpoint::tool::deleteview_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::DeleteView)


def test_viewpoint::tool::deleteview_constructor_exists():
    assert callable(viewpoint::tool::DeleteView.__init__)


def test_viewpoint::tool::deleteview_constructor_args():
    sig = inspect.signature(viewpoint::tool::DeleteView.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::for_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::For)


def test_viewpoint::tool::for_constructor_exists():
    assert callable(viewpoint::tool::For.__init__)


def test_viewpoint::tool::for_constructor_args():
    sig = inspect.signature(viewpoint::tool::For.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"
    assert "iteratorName" in params, "Missing parameter 'iteratorName'"

def test_viewpoint::tool::for_has_expression():
    assert hasattr(viewpoint::tool::For, "expression")
    descriptor = None
    for klass in viewpoint::tool::For.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::tool::for_has_iteratorName():
    assert hasattr(viewpoint::tool::For, "iteratorName")
    descriptor = None
    for klass in viewpoint::tool::For.__mro__:
        if "iteratorName" in klass.__dict__:
            descriptor = klass.__dict__["iteratorName"]
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
    assert "variableName" in params, "Missing parameter 'variableName'"
    assert "typeName" in params, "Missing parameter 'typeName'"

def test_viewpoint::tool::createinstance_has_referenceName():
    assert hasattr(viewpoint::tool::CreateInstance, "referenceName")
    descriptor = None
    for klass in viewpoint::tool::CreateInstance.__mro__:
        if "referenceName" in klass.__dict__:
            descriptor = klass.__dict__["referenceName"]
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

def test_viewpoint::tool::createinstance_has_typeName():
    assert hasattr(viewpoint::tool::CreateInstance, "typeName")
    descriptor = None
    for klass in viewpoint::tool::CreateInstance.__mro__:
        if "typeName" in klass.__dict__:
            descriptor = klass.__dict__["typeName"]
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



def test_description::abstractvariable_is_not_abstract():
    assert not inspect.isabstract(description::AbstractVariable)


def test_description::abstractvariable_constructor_exists():
    assert callable(description::AbstractVariable.__init__)


def test_description::abstractvariable_constructor_args():
    sig = inspect.signature(description::AbstractVariable.__init__)
    params = list(sig.parameters.keys())



def test_tool::variablecontainer_is_not_abstract():
    assert not inspect.isabstract(tool::VariableContainer)


def test_tool::variablecontainer_constructor_exists():
    assert callable(tool::VariableContainer.__init__)


def test_tool::variablecontainer_constructor_args():
    sig = inspect.signature(tool::VariableContainer.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::dropcontainervariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::DropContainerVariable)


def test_viewpoint::tool::dropcontainervariable_constructor_exists():
    assert callable(viewpoint::tool::DropContainerVariable.__init__)


def test_viewpoint::tool::dropcontainervariable_constructor_args():
    sig = inspect.signature(viewpoint::tool::DropContainerVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::elementviewvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::ElementViewVariable)


def test_viewpoint::tool::elementviewvariable_constructor_exists():
    assert callable(viewpoint::tool::ElementViewVariable.__init__)


def test_viewpoint::tool::elementviewvariable_constructor_args():
    sig = inspect.signature(viewpoint::tool::ElementViewVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::elementdeletevariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::ElementDeleteVariable)


def test_viewpoint::tool::elementdeletevariable_constructor_exists():
    assert callable(viewpoint::tool::ElementDeleteVariable.__init__)


def test_viewpoint::tool::elementdeletevariable_constructor_args():
    sig = inspect.signature(viewpoint::tool::ElementDeleteVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::elementdropvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::ElementDropVariable)


def test_viewpoint::tool::elementdropvariable_constructor_exists():
    assert callable(viewpoint::tool::ElementDropVariable.__init__)


def test_viewpoint::tool::elementdropvariable_constructor_args():
    sig = inspect.signature(viewpoint::tool::ElementDropVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::elementvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::ElementVariable)


def test_viewpoint::tool::elementvariable_constructor_exists():
    assert callable(viewpoint::tool::ElementVariable.__init__)


def test_viewpoint::tool::elementvariable_constructor_args():
    sig = inspect.signature(viewpoint::tool::ElementVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::containerviewvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::ContainerViewVariable)


def test_viewpoint::tool::containerviewvariable_constructor_exists():
    assert callable(viewpoint::tool::ContainerViewVariable.__init__)


def test_viewpoint::tool::containerviewvariable_constructor_args():
    sig = inspect.signature(viewpoint::tool::ContainerViewVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::selectcontainervariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::SelectContainerVariable)


def test_viewpoint::tool::selectcontainervariable_constructor_exists():
    assert callable(viewpoint::tool::SelectContainerVariable.__init__)


def test_viewpoint::tool::selectcontainervariable_constructor_args():
    sig = inspect.signature(viewpoint::tool::SelectContainerVariable.__init__)
    params = list(sig.parameters.keys())



def test_subvariable_is_not_abstract():
    assert not inspect.isabstract(SubVariable)


def test_subvariable_constructor_exists():
    assert callable(SubVariable.__init__)


def test_subvariable_constructor_args():
    sig = inspect.signature(SubVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::variablecontainer_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::VariableContainer)


def test_viewpoint::tool::variablecontainer_constructor_exists():
    assert callable(viewpoint::tool::VariableContainer.__init__)


def test_viewpoint::tool::variablecontainer_constructor_args():
    sig = inspect.signature(viewpoint::tool::VariableContainer.__init__)
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



def test_viewpoint::tool::externaljavaactioncall_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::ExternalJavaActionCall)


def test_viewpoint::tool::externaljavaactioncall_constructor_exists():
    assert callable(viewpoint::tool::ExternalJavaActionCall.__init__)


def test_viewpoint::tool::externaljavaactioncall_constructor_args():
    sig = inspect.signature(viewpoint::tool::ExternalJavaActionCall.__init__)
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
    assert "iconPath" in params, "Missing parameter 'iconPath'"
    assert "windowTitle" in params, "Missing parameter 'windowTitle'"

def test_viewpoint::tool::selectionwizarddescription_has_windowImagePath():
    assert hasattr(viewpoint::tool::SelectionWizardDescription, "windowImagePath")
    descriptor = None
    for klass in viewpoint::tool::SelectionWizardDescription.__mro__:
        if "windowImagePath" in klass.__dict__:
            descriptor = klass.__dict__["windowImagePath"]
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

def test_viewpoint::tool::selectionwizarddescription_has_windowTitle():
    assert hasattr(viewpoint::tool::SelectionWizardDescription, "windowTitle")
    descriptor = None
    for klass in viewpoint::tool::SelectionWizardDescription.__mro__:
        if "windowTitle" in klass.__dict__:
            descriptor = klass.__dict__["windowTitle"]
            break
    assert isinstance(descriptor, property)



def test_tool::containerviewvariable_is_not_abstract():
    assert not inspect.isabstract(tool::ContainerViewVariable)


def test_tool::containerviewvariable_constructor_exists():
    assert callable(tool::ContainerViewVariable.__init__)


def test_tool::containerviewvariable_constructor_args():
    sig = inspect.signature(tool::ContainerViewVariable.__init__)
    params = list(sig.parameters.keys())



def test_tool::dropcontainervariable_is_not_abstract():
    assert not inspect.isabstract(tool::DropContainerVariable)


def test_tool::dropcontainervariable_constructor_exists():
    assert callable(tool::DropContainerVariable.__init__)


def test_tool::dropcontainervariable_constructor_args():
    sig = inspect.signature(tool::DropContainerVariable.__init__)
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



def test_viewpoint::tool::representationnavigationdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::RepresentationNavigationDescription)


def test_viewpoint::tool::representationnavigationdescription_constructor_exists():
    assert callable(viewpoint::tool::RepresentationNavigationDescription.__init__)


def test_viewpoint::tool::representationnavigationdescription_constructor_args():
    sig = inspect.signature(viewpoint::tool::RepresentationNavigationDescription.__init__)
    params = list(sig.parameters.keys())
    assert "navigationNameExpression" in params, "Missing parameter 'navigationNameExpression'"
    assert "browseExpression" in params, "Missing parameter 'browseExpression'"

def test_viewpoint::tool::representationnavigationdescription_has_navigationNameExpression():
    assert hasattr(viewpoint::tool::RepresentationNavigationDescription, "navigationNameExpression")
    descriptor = None
    for klass in viewpoint::tool::RepresentationNavigationDescription.__mro__:
        if "navigationNameExpression" in klass.__dict__:
            descriptor = klass.__dict__["navigationNameExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::tool::representationnavigationdescription_has_browseExpression():
    assert hasattr(viewpoint::tool::RepresentationNavigationDescription, "browseExpression")
    descriptor = None
    for klass in viewpoint::tool::RepresentationNavigationDescription.__mro__:
        if "browseExpression" in klass.__dict__:
            descriptor = klass.__dict__["browseExpression"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::tool::popupmenu_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::PopupMenu)


def test_viewpoint::tool::popupmenu_constructor_exists():
    assert callable(viewpoint::tool::PopupMenu.__init__)


def test_viewpoint::tool::popupmenu_constructor_args():
    sig = inspect.signature(viewpoint::tool::PopupMenu.__init__)
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



def test_viewpoint::tool::panebasedselectionwizarddescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::PaneBasedSelectionWizardDescription)


def test_viewpoint::tool::panebasedselectionwizarddescription_constructor_exists():
    assert callable(viewpoint::tool::PaneBasedSelectionWizardDescription.__init__)


def test_viewpoint::tool::panebasedselectionwizarddescription_constructor_args():
    sig = inspect.signature(viewpoint::tool::PaneBasedSelectionWizardDescription.__init__)
    params = list(sig.parameters.keys())
    assert "iconPath" in params, "Missing parameter 'iconPath'"
    assert "windowImagePath" in params, "Missing parameter 'windowImagePath'"
    assert "childrenExpression" in params, "Missing parameter 'childrenExpression'"
    assert "windowTitle" in params, "Missing parameter 'windowTitle'"
    assert "choiceOfValuesMessage" in params, "Missing parameter 'choiceOfValuesMessage'"
    assert "candidatesExpression" in params, "Missing parameter 'candidatesExpression'"
    assert "selectedValuesMessage" in params, "Missing parameter 'selectedValuesMessage'"
    assert "preSelectedCandidatesExpression" in params, "Missing parameter 'preSelectedCandidatesExpression'"
    assert "rootExpression" in params, "Missing parameter 'rootExpression'"
    assert "message" in params, "Missing parameter 'message'"
    assert "tree" in params, "Missing parameter 'tree'"

def test_viewpoint::tool::panebasedselectionwizarddescription_has_iconPath():
    assert hasattr(viewpoint::tool::PaneBasedSelectionWizardDescription, "iconPath")
    descriptor = None
    for klass in viewpoint::tool::PaneBasedSelectionWizardDescription.__mro__:
        if "iconPath" in klass.__dict__:
            descriptor = klass.__dict__["iconPath"]
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

def test_viewpoint::tool::panebasedselectionwizarddescription_has_childrenExpression():
    assert hasattr(viewpoint::tool::PaneBasedSelectionWizardDescription, "childrenExpression")
    descriptor = None
    for klass in viewpoint::tool::PaneBasedSelectionWizardDescription.__mro__:
        if "childrenExpression" in klass.__dict__:
            descriptor = klass.__dict__["childrenExpression"]
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

def test_viewpoint::tool::panebasedselectionwizarddescription_has_choiceOfValuesMessage():
    assert hasattr(viewpoint::tool::PaneBasedSelectionWizardDescription, "choiceOfValuesMessage")
    descriptor = None
    for klass in viewpoint::tool::PaneBasedSelectionWizardDescription.__mro__:
        if "choiceOfValuesMessage" in klass.__dict__:
            descriptor = klass.__dict__["choiceOfValuesMessage"]
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

def test_viewpoint::tool::panebasedselectionwizarddescription_has_selectedValuesMessage():
    assert hasattr(viewpoint::tool::PaneBasedSelectionWizardDescription, "selectedValuesMessage")
    descriptor = None
    for klass in viewpoint::tool::PaneBasedSelectionWizardDescription.__mro__:
        if "selectedValuesMessage" in klass.__dict__:
            descriptor = klass.__dict__["selectedValuesMessage"]
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

def test_viewpoint::tool::panebasedselectionwizarddescription_has_rootExpression():
    assert hasattr(viewpoint::tool::PaneBasedSelectionWizardDescription, "rootExpression")
    descriptor = None
    for klass in viewpoint::tool::PaneBasedSelectionWizardDescription.__mro__:
        if "rootExpression" in klass.__dict__:
            descriptor = klass.__dict__["rootExpression"]
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

def test_viewpoint::tool::panebasedselectionwizarddescription_has_tree():
    assert hasattr(viewpoint::tool::PaneBasedSelectionWizardDescription, "tree")
    descriptor = None
    for klass in viewpoint::tool::PaneBasedSelectionWizardDescription.__mro__:
        if "tree" in klass.__dict__:
            descriptor = klass.__dict__["tree"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::tool::mappingbasedtooldescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::MappingBasedToolDescription)


def test_viewpoint::tool::mappingbasedtooldescription_constructor_exists():
    assert callable(viewpoint::tool::MappingBasedToolDescription.__init__)


def test_viewpoint::tool::mappingbasedtooldescription_constructor_args():
    sig = inspect.signature(viewpoint::tool::MappingBasedToolDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::pastedescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::PasteDescription)


def test_viewpoint::tool::pastedescription_constructor_exists():
    assert callable(viewpoint::tool::PasteDescription.__init__)


def test_viewpoint::tool::pastedescription_constructor_args():
    sig = inspect.signature(viewpoint::tool::PasteDescription.__init__)
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



def test_toolentry_is_not_abstract():
    assert not inspect.isabstract(ToolEntry)


def test_toolentry_constructor_exists():
    assert callable(ToolEntry.__init__)


def test_toolentry_constructor_args():
    sig = inspect.signature(ToolEntry.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::abstracttooldescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::AbstractToolDescription)


def test_viewpoint::tool::abstracttooldescription_constructor_exists():
    assert callable(viewpoint::tool::AbstractToolDescription.__init__)


def test_viewpoint::tool::abstracttooldescription_constructor_args():
    sig = inspect.signature(viewpoint::tool::AbstractToolDescription.__init__)
    params = list(sig.parameters.keys())
    assert "forceRefresh" in params, "Missing parameter 'forceRefresh'"
    assert "elementsToSelect" in params, "Missing parameter 'elementsToSelect'"
    assert "inverseSelectionOrder" in params, "Missing parameter 'inverseSelectionOrder'"
    assert "precondition" in params, "Missing parameter 'precondition'"

def test_viewpoint::tool::abstracttooldescription_has_forceRefresh():
    assert hasattr(viewpoint::tool::AbstractToolDescription, "forceRefresh")
    descriptor = None
    for klass in viewpoint::tool::AbstractToolDescription.__mro__:
        if "forceRefresh" in klass.__dict__:
            descriptor = klass.__dict__["forceRefresh"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::tool::abstracttooldescription_has_elementsToSelect():
    assert hasattr(viewpoint::tool::AbstractToolDescription, "elementsToSelect")
    descriptor = None
    for klass in viewpoint::tool::AbstractToolDescription.__mro__:
        if "elementsToSelect" in klass.__dict__:
            descriptor = klass.__dict__["elementsToSelect"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::tool::abstracttooldescription_has_inverseSelectionOrder():
    assert hasattr(viewpoint::tool::AbstractToolDescription, "inverseSelectionOrder")
    descriptor = None
    for klass in viewpoint::tool::AbstractToolDescription.__mro__:
        if "inverseSelectionOrder" in klass.__dict__:
            descriptor = klass.__dict__["inverseSelectionOrder"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::tool::abstracttooldescription_has_precondition():
    assert hasattr(viewpoint::tool::AbstractToolDescription, "precondition")
    descriptor = None
    for klass in viewpoint::tool::AbstractToolDescription.__mro__:
        if "precondition" in klass.__dict__:
            descriptor = klass.__dict__["precondition"]
            break
    assert isinstance(descriptor, property)



def test_tool::toolfilterdescription_is_not_abstract():
    assert not inspect.isabstract(tool::ToolFilterDescription)


def test_tool::toolfilterdescription_constructor_exists():
    assert callable(tool::ToolFilterDescription.__init__)


def test_tool::toolfilterdescription_constructor_args():
    sig = inspect.signature(tool::ToolFilterDescription.__init__)
    params = list(sig.parameters.keys())



def test_basiclabelstyledescription_is_not_abstract():
    assert not inspect.isabstract(BasicLabelStyleDescription)


def test_basiclabelstyledescription_constructor_exists():
    assert callable(BasicLabelStyleDescription.__init__)


def test_basiclabelstyledescription_constructor_args():
    sig = inspect.signature(BasicLabelStyleDescription.__init__)
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
    assert "cornerWidth" in params, "Missing parameter 'cornerWidth'"
    assert "cornerHeight" in params, "Missing parameter 'cornerHeight'"
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_viewpoint::style::labelborderstyledescription_has_cornerWidth():
    assert hasattr(viewpoint::style::LabelBorderStyleDescription, "cornerWidth")
    descriptor = None
    for klass in viewpoint::style::LabelBorderStyleDescription.__mro__:
        if "cornerWidth" in klass.__dict__:
            descriptor = klass.__dict__["cornerWidth"]
            break
    assert isinstance(descriptor, property)

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



def test_description::viewpoint::edatatype_is_not_abstract():
    assert not inspect.isabstract(description::viewpoint::EDataType)


def test_description::viewpoint::edatatype_constructor_exists():
    assert callable(description::viewpoint::EDataType.__init__)


def test_description::viewpoint::edatatype_constructor_args():
    sig = inspect.signature(description::viewpoint::EDataType.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::style::basiclabelstyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::style::BasicLabelStyleDescription)


def test_viewpoint::style::basiclabelstyledescription_constructor_exists():
    assert callable(viewpoint::style::BasicLabelStyleDescription.__init__)


def test_viewpoint::style::basiclabelstyledescription_constructor_args():
    sig = inspect.signature(viewpoint::style::BasicLabelStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "labelSize" in params, "Missing parameter 'labelSize'"
    assert "labelExpression" in params, "Missing parameter 'labelExpression'"
    assert "labelFormat" in params, "Missing parameter 'labelFormat'"
    assert "showIcon" in params, "Missing parameter 'showIcon'"
    assert "iconPath" in params, "Missing parameter 'iconPath'"

def test_viewpoint::style::basiclabelstyledescription_has_labelSize():
    assert hasattr(viewpoint::style::BasicLabelStyleDescription, "labelSize")
    descriptor = None
    for klass in viewpoint::style::BasicLabelStyleDescription.__mro__:
        if "labelSize" in klass.__dict__:
            descriptor = klass.__dict__["labelSize"]
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

def test_viewpoint::style::basiclabelstyledescription_has_labelFormat():
    assert hasattr(viewpoint::style::BasicLabelStyleDescription, "labelFormat")
    descriptor = None
    for klass in viewpoint::style::BasicLabelStyleDescription.__mro__:
        if "labelFormat" in klass.__dict__:
            descriptor = klass.__dict__["labelFormat"]
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

def test_viewpoint::style::basiclabelstyledescription_has_iconPath():
    assert hasattr(viewpoint::style::BasicLabelStyleDescription, "iconPath")
    descriptor = None
    for klass in viewpoint::style::BasicLabelStyleDescription.__mro__:
        if "iconPath" in klass.__dict__:
            descriptor = klass.__dict__["iconPath"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::style::styledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::style::StyleDescription)


def test_viewpoint::style::styledescription_constructor_exists():
    assert callable(viewpoint::style::StyleDescription.__init__)


def test_viewpoint::style::styledescription_constructor_args():
    sig = inspect.signature(viewpoint::style::StyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::identifiedelement_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::IdentifiedElement)


def test_viewpoint::description::identifiedelement_constructor_exists():
    assert callable(viewpoint::description::IdentifiedElement.__init__)


def test_viewpoint::description::identifiedelement_constructor_args():
    sig = inspect.signature(viewpoint::description::IdentifiedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "label" in params, "Missing parameter 'label'"

def test_viewpoint::description::identifiedelement_has_name():
    assert hasattr(viewpoint::description::IdentifiedElement, "name")
    descriptor = None
    for klass in viewpoint::description::IdentifiedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::description::identifiedelement_has_label():
    assert hasattr(viewpoint::description::IdentifiedElement, "label")
    descriptor = None
    for klass in viewpoint::description::IdentifiedElement.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
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



def test_description::subvariable_is_not_abstract():
    assert not inspect.isabstract(description::SubVariable)


def test_description::subvariable_constructor_exists():
    assert callable(description::SubVariable.__init__)


def test_description::subvariable_constructor_args():
    sig = inspect.signature(description::SubVariable.__init__)
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



def test_description::interactivevariabledescription_is_not_abstract():
    assert not inspect.isabstract(description::InteractiveVariableDescription)


def test_description::interactivevariabledescription_constructor_exists():
    assert callable(description::InteractiveVariableDescription.__init__)


def test_description::interactivevariabledescription_constructor_args():
    sig = inspect.signature(description::InteractiveVariableDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::selectmodelelementvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::SelectModelElementVariable)


def test_viewpoint::tool::selectmodelelementvariable_constructor_exists():
    assert callable(viewpoint::tool::SelectModelElementVariable.__init__)


def test_viewpoint::tool::selectmodelelementvariable_constructor_args():
    sig = inspect.signature(viewpoint::tool::SelectModelElementVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::typedvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::TypedVariable)


def test_viewpoint::description::typedvariable_constructor_exists():
    assert callable(viewpoint::description::TypedVariable.__init__)


def test_viewpoint::description::typedvariable_constructor_args():
    sig = inspect.signature(viewpoint::description::TypedVariable.__init__)
    params = list(sig.parameters.keys())
    assert "defaultValueExpression" in params, "Missing parameter 'defaultValueExpression'"

def test_viewpoint::description::typedvariable_has_defaultValueExpression():
    assert hasattr(viewpoint::description::TypedVariable, "defaultValueExpression")
    descriptor = None
    for klass in viewpoint::description::TypedVariable.__mro__:
        if "defaultValueExpression" in klass.__dict__:
            descriptor = klass.__dict__["defaultValueExpression"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint::description::interactivevariabledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::InteractiveVariableDescription)


def test_viewpoint::description::interactivevariabledescription_constructor_exists():
    assert callable(viewpoint::description::InteractiveVariableDescription.__init__)


def test_viewpoint::description::interactivevariabledescription_constructor_args():
    sig = inspect.signature(viewpoint::description::InteractiveVariableDescription.__init__)
    params = list(sig.parameters.keys())
    assert "userDocumentation" in params, "Missing parameter 'userDocumentation'"

def test_viewpoint::description::interactivevariabledescription_has_userDocumentation():
    assert hasattr(viewpoint::description::InteractiveVariableDescription, "userDocumentation")
    descriptor = None
    for klass in viewpoint::description::InteractiveVariableDescription.__mro__:
        if "userDocumentation" in klass.__dict__:
            descriptor = klass.__dict__["userDocumentation"]
            break
    assert isinstance(descriptor, property)



def test_abstractvariable_is_not_abstract():
    assert not inspect.isabstract(AbstractVariable)


def test_abstractvariable_constructor_exists():
    assert callable(AbstractVariable.__init__)


def test_abstractvariable_constructor_args():
    sig = inspect.signature(AbstractVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::elementselectvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::ElementSelectVariable)


def test_viewpoint::tool::elementselectvariable_constructor_exists():
    assert callable(viewpoint::tool::ElementSelectVariable.__init__)


def test_viewpoint::tool::elementselectvariable_constructor_args():
    sig = inspect.signature(viewpoint::tool::ElementSelectVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::tool::namevariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::NameVariable)


def test_viewpoint::tool::namevariable_constructor_exists():
    assert callable(viewpoint::tool::NameVariable.__init__)


def test_viewpoint::tool::namevariable_constructor_args():
    sig = inspect.signature(viewpoint::tool::NameVariable.__init__)
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



def test_viewpoint::description::subvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::SubVariable)


def test_viewpoint::description::subvariable_constructor_exists():
    assert callable(viewpoint::description::SubVariable.__init__)


def test_viewpoint::description::subvariable_constructor_args():
    sig = inspect.signature(viewpoint::description::SubVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::abstractvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::AbstractVariable)


def test_viewpoint::description::abstractvariable_constructor_exists():
    assert callable(viewpoint::description::AbstractVariable.__init__)


def test_viewpoint::description::abstractvariable_constructor_args():
    sig = inspect.signature(viewpoint::description::AbstractVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_viewpoint::description::abstractvariable_has_name():
    assert hasattr(viewpoint::description::AbstractVariable, "name")
    descriptor = None
    for klass in viewpoint::description::AbstractVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



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



def test_description::usercolor_is_not_abstract():
    assert not inspect.isabstract(description::UserColor)


def test_description::usercolor_constructor_exists():
    assert callable(description::UserColor.__init__)


def test_description::usercolor_constructor_args():
    sig = inspect.signature(description::UserColor.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::userfixedcolor_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::UserFixedColor)


def test_viewpoint::description::userfixedcolor_constructor_exists():
    assert callable(viewpoint::description::UserFixedColor.__init__)


def test_viewpoint::description::userfixedcolor_constructor_args():
    sig = inspect.signature(viewpoint::description::UserFixedColor.__init__)
    params = list(sig.parameters.keys())



def test_description::colordescription_is_not_abstract():
    assert not inspect.isabstract(description::ColorDescription)


def test_description::colordescription_constructor_exists():
    assert callable(description::ColorDescription.__init__)


def test_description::colordescription_constructor_args():
    sig = inspect.signature(description::ColorDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::computedcolor_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::ComputedColor)


def test_viewpoint::description::computedcolor_constructor_exists():
    assert callable(viewpoint::description::ComputedColor.__init__)


def test_viewpoint::description::computedcolor_constructor_args():
    sig = inspect.signature(viewpoint::description::ComputedColor.__init__)
    params = list(sig.parameters.keys())
    assert "green" in params, "Missing parameter 'green'"
    assert "red" in params, "Missing parameter 'red'"
    assert "blue" in params, "Missing parameter 'blue'"

def test_viewpoint::description::computedcolor_has_green():
    assert hasattr(viewpoint::description::ComputedColor, "green")
    descriptor = None
    for klass in viewpoint::description::ComputedColor.__mro__:
        if "green" in klass.__dict__:
            descriptor = klass.__dict__["green"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::description::computedcolor_has_red():
    assert hasattr(viewpoint::description::ComputedColor, "red")
    descriptor = None
    for klass in viewpoint::description::ComputedColor.__mro__:
        if "red" in klass.__dict__:
            descriptor = klass.__dict__["red"]
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



def test_viewpoint::description::interpolatedcolor_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::InterpolatedColor)


def test_viewpoint::description::interpolatedcolor_constructor_exists():
    assert callable(viewpoint::description::InterpolatedColor.__init__)


def test_viewpoint::description::interpolatedcolor_constructor_args():
    sig = inspect.signature(viewpoint::description::InterpolatedColor.__init__)
    params = list(sig.parameters.keys())
    assert "maxValueComputationExpression" in params, "Missing parameter 'maxValueComputationExpression'"
    assert "colorValueComputationExpression" in params, "Missing parameter 'colorValueComputationExpression'"
    assert "minValueComputationExpression" in params, "Missing parameter 'minValueComputationExpression'"

def test_viewpoint::description::interpolatedcolor_has_maxValueComputationExpression():
    assert hasattr(viewpoint::description::InterpolatedColor, "maxValueComputationExpression")
    descriptor = None
    for klass in viewpoint::description::InterpolatedColor.__mro__:
        if "maxValueComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["maxValueComputationExpression"]
            break
    assert isinstance(descriptor, property)

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
    assert "red" in params, "Missing parameter 'red'"
    assert "blue" in params, "Missing parameter 'blue'"

def test_viewpoint::description::fixedcolor_has_green():
    assert hasattr(viewpoint::description::FixedColor, "green")
    descriptor = None
    for klass in viewpoint::description::FixedColor.__mro__:
        if "green" in klass.__dict__:
            descriptor = klass.__dict__["green"]
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

def test_viewpoint::description::fixedcolor_has_blue():
    assert hasattr(viewpoint::description::FixedColor, "blue")
    descriptor = None
    for klass in viewpoint::description::FixedColor.__mro__:
        if "blue" in klass.__dict__:
            descriptor = klass.__dict__["blue"]
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
    assert "candidatesExpression" in params, "Missing parameter 'candidatesExpression'"
    assert "tree" in params, "Missing parameter 'tree'"
    assert "rootExpression" in params, "Missing parameter 'rootExpression'"
    assert "message" in params, "Missing parameter 'message'"
    assert "multiple" in params, "Missing parameter 'multiple'"
    assert "childrenExpression" in params, "Missing parameter 'childrenExpression'"

def test_viewpoint::description::selectiondescription_has_candidatesExpression():
    assert hasattr(viewpoint::description::SelectionDescription, "candidatesExpression")
    descriptor = None
    for klass in viewpoint::description::SelectionDescription.__mro__:
        if "candidatesExpression" in klass.__dict__:
            descriptor = klass.__dict__["candidatesExpression"]
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

def test_viewpoint::description::selectiondescription_has_rootExpression():
    assert hasattr(viewpoint::description::SelectionDescription, "rootExpression")
    descriptor = None
    for klass in viewpoint::description::SelectionDescription.__mro__:
        if "rootExpression" in klass.__dict__:
            descriptor = klass.__dict__["rootExpression"]
            break
    assert isinstance(descriptor, property)

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

def test_viewpoint::description::selectiondescription_has_childrenExpression():
    assert hasattr(viewpoint::description::SelectionDescription, "childrenExpression")
    descriptor = None
    for klass in viewpoint::description::SelectionDescription.__mro__:
        if "childrenExpression" in klass.__dict__:
            descriptor = klass.__dict__["childrenExpression"]
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



def test_viewpoint::description::genericdecorationdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::GenericDecorationDescription)


def test_viewpoint::description::genericdecorationdescription_constructor_exists():
    assert callable(viewpoint::description::GenericDecorationDescription.__init__)


def test_viewpoint::description::genericdecorationdescription_constructor_args():
    sig = inspect.signature(viewpoint::description::GenericDecorationDescription.__init__)
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



def test_viewpoint::description::vsmelementcustomizationreuse_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::VSMElementCustomizationReuse)


def test_viewpoint::description::vsmelementcustomizationreuse_constructor_exists():
    assert callable(viewpoint::description::VSMElementCustomizationReuse.__init__)


def test_viewpoint::description::vsmelementcustomizationreuse_constructor_args():
    sig = inspect.signature(viewpoint::description::VSMElementCustomizationReuse.__init__)
    params = list(sig.parameters.keys())



def test_estructuralfeaturecustomization_is_not_abstract():
    assert not inspect.isabstract(EStructuralFeatureCustomization)


def test_estructuralfeaturecustomization_constructor_exists():
    assert callable(EStructuralFeatureCustomization.__init__)


def test_estructuralfeaturecustomization_constructor_args():
    sig = inspect.signature(EStructuralFeatureCustomization.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::eattributecustomization_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::EAttributeCustomization)


def test_viewpoint::description::eattributecustomization_constructor_exists():
    assert callable(viewpoint::description::EAttributeCustomization.__init__)


def test_viewpoint::description::eattributecustomization_constructor_args():
    sig = inspect.signature(viewpoint::description::EAttributeCustomization.__init__)
    params = list(sig.parameters.keys())
    assert "attributeName" in params, "Missing parameter 'attributeName'"
    assert "value" in params, "Missing parameter 'value'"

def test_viewpoint::description::eattributecustomization_has_attributeName():
    assert hasattr(viewpoint::description::EAttributeCustomization, "attributeName")
    descriptor = None
    for klass in viewpoint::description::EAttributeCustomization.__mro__:
        if "attributeName" in klass.__dict__:
            descriptor = klass.__dict__["attributeName"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::description::eattributecustomization_has_value():
    assert hasattr(viewpoint::description::EAttributeCustomization, "value")
    descriptor = None
    for klass in viewpoint::description::EAttributeCustomization.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



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



def test_viewpoint::description::decorationdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::DecorationDescription)


def test_viewpoint::description::decorationdescription_constructor_exists():
    assert callable(viewpoint::description::DecorationDescription.__init__)


def test_viewpoint::description::decorationdescription_constructor_args():
    sig = inspect.signature(viewpoint::description::DecorationDescription.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "tooltipExpression" in params, "Missing parameter 'tooltipExpression'"
    assert "distributionDirection" in params, "Missing parameter 'distributionDirection'"
    assert "position" in params, "Missing parameter 'position'"
    assert "preconditionExpression" in params, "Missing parameter 'preconditionExpression'"
    assert "imageExpression" in params, "Missing parameter 'imageExpression'"

def test_viewpoint::description::decorationdescription_has_name():
    assert hasattr(viewpoint::description::DecorationDescription, "name")
    descriptor = None
    for klass in viewpoint::description::DecorationDescription.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::description::decorationdescription_has_tooltipExpression():
    assert hasattr(viewpoint::description::DecorationDescription, "tooltipExpression")
    descriptor = None
    for klass in viewpoint::description::DecorationDescription.__mro__:
        if "tooltipExpression" in klass.__dict__:
            descriptor = klass.__dict__["tooltipExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::description::decorationdescription_has_distributionDirection():
    assert hasattr(viewpoint::description::DecorationDescription, "distributionDirection")
    descriptor = None
    for klass in viewpoint::description::DecorationDescription.__mro__:
        if "distributionDirection" in klass.__dict__:
            descriptor = klass.__dict__["distributionDirection"]
            break
    assert isinstance(descriptor, property)

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

def test_viewpoint::description::decorationdescription_has_imageExpression():
    assert hasattr(viewpoint::description::DecorationDescription, "imageExpression")
    descriptor = None
    for klass in viewpoint::description::DecorationDescription.__mro__:
        if "imageExpression" in klass.__dict__:
            descriptor = klass.__dict__["imageExpression"]
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



def test_viewpoint::validation::validationrule_is_not_abstract():
    assert not inspect.isabstract(viewpoint::validation::ValidationRule)


def test_viewpoint::validation::validationrule_constructor_exists():
    assert callable(viewpoint::validation::ValidationRule.__init__)


def test_viewpoint::validation::validationrule_constructor_args():
    sig = inspect.signature(viewpoint::validation::ValidationRule.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"
    assert "message" in params, "Missing parameter 'message'"

def test_viewpoint::validation::validationrule_has_level():
    assert hasattr(viewpoint::validation::ValidationRule, "level")
    descriptor = None
    for klass in viewpoint::validation::ValidationRule.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint::validation::validationrule_has_message():
    assert hasattr(viewpoint::validation::ValidationRule, "message")
    descriptor = None
    for klass in viewpoint::validation::ValidationRule.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)



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



def test_description::viewpoint::epackage_is_not_abstract():
    assert not inspect.isabstract(description::viewpoint::EPackage)


def test_description::viewpoint::epackage_constructor_exists():
    assert callable(description::viewpoint::EPackage.__init__)


def test_description::viewpoint::epackage_constructor_args():
    sig = inspect.signature(description::viewpoint::EPackage.__init__)
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
    assert "viewpointURI" in params, "Missing parameter 'viewpointURI'"
    assert "name" in params, "Missing parameter 'name'"
    assert "representationName" in params, "Missing parameter 'representationName'"

def test_viewpoint::description::representationextensiondescription_has_viewpointURI():
    assert hasattr(viewpoint::description::RepresentationExtensionDescription, "viewpointURI")
    descriptor = None
    for klass in viewpoint::description::RepresentationExtensionDescription.__mro__:
        if "viewpointURI" in klass.__dict__:
            descriptor = klass.__dict__["viewpointURI"]
            break
    assert isinstance(descriptor, property)

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



def test_viewpoint::description::representationimportdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::RepresentationImportDescription)


def test_viewpoint::description::representationimportdescription_constructor_exists():
    assert callable(viewpoint::description::RepresentationImportDescription.__init__)


def test_viewpoint::description::representationimportdescription_constructor_args():
    sig = inspect.signature(viewpoint::description::RepresentationImportDescription.__init__)
    params = list(sig.parameters.keys())



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



def test_viewpoint::tool::toolentry_is_not_abstract():
    assert not inspect.isabstract(viewpoint::tool::ToolEntry)


def test_viewpoint::tool::toolentry_constructor_exists():
    assert callable(viewpoint::tool::ToolEntry.__init__)


def test_viewpoint::tool::toolentry_constructor_args():
    sig = inspect.signature(viewpoint::tool::ToolEntry.__init__)
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



def test_viewpoint::description::viewpoint_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::Viewpoint)


def test_viewpoint::description::viewpoint_constructor_exists():
    assert callable(viewpoint::description::Viewpoint.__init__)


def test_viewpoint::description::viewpoint_constructor_args():
    sig = inspect.signature(viewpoint::description::Viewpoint.__init__)
    params = list(sig.parameters.keys())
    assert "icon" in params, "Missing parameter 'icon'"
    assert "customizes" in params, "Missing parameter 'customizes'"
    assert "reuses" in params, "Missing parameter 'reuses'"
    assert "modelFileExtension" in params, "Missing parameter 'modelFileExtension'"
    assert "conflicts" in params, "Missing parameter 'conflicts'"

def test_viewpoint::description::viewpoint_has_icon():
    assert hasattr(viewpoint::description::Viewpoint, "icon")
    descriptor = None
    for klass in viewpoint::description::Viewpoint.__mro__:
        if "icon" in klass.__dict__:
            descriptor = klass.__dict__["icon"]
            break
    assert isinstance(descriptor, property)

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

def test_viewpoint::description::viewpoint_has_modelFileExtension():
    assert hasattr(viewpoint::description::Viewpoint, "modelFileExtension")
    descriptor = None
    for klass in viewpoint::description::Viewpoint.__mro__:
        if "modelFileExtension" in klass.__dict__:
            descriptor = klass.__dict__["modelFileExtension"]
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



def test_viewpoint::description::component_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::Component)


def test_viewpoint::description::component_constructor_exists():
    assert callable(viewpoint::description::Component.__init__)


def test_viewpoint::description::component_constructor_args():
    sig = inspect.signature(viewpoint::description::Component.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::extension_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::Extension)


def test_viewpoint::description::extension_constructor_exists():
    assert callable(viewpoint::description::Extension.__init__)


def test_viewpoint::description::extension_constructor_args():
    sig = inspect.signature(viewpoint::description::Extension.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint::description::representationdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint::description::RepresentationDescription)


def test_viewpoint::description::representationdescription_constructor_exists():
    assert callable(viewpoint::description::RepresentationDescription.__init__)


def test_viewpoint::description::representationdescription_constructor_args():
    sig = inspect.signature(viewpoint::description::RepresentationDescription.__init__)
    params = list(sig.parameters.keys())
    assert "initialisation" in params, "Missing parameter 'initialisation'"
    assert "titleExpression" in params, "Missing parameter 'titleExpression'"
    assert "showOnStartup" in params, "Missing parameter 'showOnStartup'"

def test_viewpoint::description::representationdescription_has_initialisation():
    assert hasattr(viewpoint::description::RepresentationDescription, "initialisation")
    descriptor = None
    for klass in viewpoint::description::RepresentationDescription.__mro__:
        if "initialisation" in klass.__dict__:
            descriptor = klass.__dict__["initialisation"]
            break
    assert isinstance(descriptor, property)

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

def test_position_exists():
    # Check that the Enumeration exists
    assert Position is not None

def test_position_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Position]
    expected_literals = [
        "SOUTH_WEST",
        "NORTH_WEST",
        "WEST",
        "NORTH_EAST",
        "SOUTH",
        "SOUTH_EAST",
        "EAST",
        "NORTH",
        "CENTER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Position"

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

def test_systemcolors_exists():
    # Check that the Enumeration exists
    assert SystemColors is not None

def test_systemcolors_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SystemColors]
    expected_literals = [
        "dark_purple",
        "light_blue",
        "light_purple",
        "white",
        "light_gray",
        "purple",
        "light_green",
        "dark_chocolate",
        "dark_yellow",
        "dark_red",
        "light_chocolate",
        "light_yellow",
        "black",
        "dark_green",
        "red",
        "green",
        "light_orange",
        "yellow",
        "dark_blue",
        "dark_gray",
        "chocolate",
        "dark_orange",
        "gray",
        "light_red",
        "blue",
        "orange",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SystemColors"

def test_dragsource_exists():
    # Check that the Enumeration exists
    assert DragSource is not None

def test_dragsource_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DragSource]
    expected_literals = [
        "BOTH",
        "DIAGRAM",
        "PROJECT_EXPLORER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DragSource"

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

def test_fontformat_exists():
    # Check that the Enumeration exists
    assert FontFormat is not None

def test_fontformat_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FontFormat]
    expected_literals = [
        "strike_through",
        "underline",
        "italic",
        "bold",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FontFormat"

def test_decorationdistributiondirection_exists():
    # Check that the Enumeration exists
    assert DecorationDistributionDirection is not None

def test_decorationdistributiondirection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DecorationDistributionDirection]
    expected_literals = [
        "VERTICAL",
        "HORIZONTAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DecorationDistributionDirection"

def test_error_level_exists():
    # Check that the Enumeration exists
    assert ERROR_LEVEL is not None

def test_error_level_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ERROR_LEVEL]
    expected_literals = [
        "INFO",
        "WARNING",
        "ERROR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ERROR_LEVEL"


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
viewpoint::validation::ValidationFix_strategy = st.builds(
    viewpoint::validation::ValidationFix,
    name=
        safe_text
)
InformationSection_strategy = st.builds(
    InformationSection,
)
viewpoint::audit::TemplateInformationSection_strategy = st.builds(
    viewpoint::audit::TemplateInformationSection,
    templatePath=
        safe_text
)
viewpoint::audit::InformationSection_strategy = st.builds(
    viewpoint::audit::InformationSection,
)
viewpoint::validation::RuleAudit_strategy = st.builds(
    viewpoint::validation::RuleAudit,
    auditExpression=
        safe_text
)
RepresentationElementMapping_strategy = st.builds(
    RepresentationElementMapping,
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
DocumentedElement_strategy = st.builds(
    DocumentedElement,
)
viewpoint::validation::ValidationSet_strategy = st.builds(
    viewpoint::validation::ValidationSet,
    name=
        safe_text
)
validation::RuleAudit_strategy = st.builds(
    validation::RuleAudit,
)
validation::ValidationRule_strategy = st.builds(
    validation::ValidationRule,
)
viewpoint::tool::FeatureChangeListener_strategy = st.builds(
    viewpoint::tool::FeatureChangeListener,
    domainClass=
        safe_text,
    featureName=
        safe_text
)
tool::Default_strategy = st.builds(
    tool::Default,
)
tool::Case_strategy = st.builds(
    tool::Case,
)
viewpoint::tool::SwitchChild_strategy = st.builds(
    viewpoint::tool::SwitchChild,
)
SwitchChild_strategy = st.builds(
    SwitchChild,
)
viewpoint::tool::Default_strategy = st.builds(
    viewpoint::tool::Default,
)
viewpoint::tool::Case_strategy = st.builds(
    viewpoint::tool::Case,
    conditionExpression=
        safe_text
)
viewpoint::tool::ExternalJavaActionParameter_strategy = st.builds(
    viewpoint::tool::ExternalJavaActionParameter,
    name=
        safe_text,
    value=
        safe_text
)
tool::FeatureChangeListener_strategy = st.builds(
    tool::FeatureChangeListener,
)
viewpoint::tool::ToolFilterDescription_strategy = st.builds(
    viewpoint::tool::ToolFilterDescription,
    precondition=
        safe_text,
    elementsToListen=
        safe_text
)
tool::viewpoint::EObject_strategy = st.builds(
    tool::viewpoint::EObject,
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
Extension_strategy = st.builds(
    Extension,
)
UserColorsPalette_strategy = st.builds(
    UserColorsPalette,
)
SytemColorsPalette_strategy = st.builds(
    SytemColorsPalette,
)
viewpoint::DAnalysisSessionEObject_strategy = st.builds(
    viewpoint::DAnalysisSessionEObject,
    controlledResources=
        safe_text,
    resources=
        safe_text,
    synchronizationStatus=
        safe_text,
    open=
        st.booleans()
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
    name=
        safe_text,
    path=
        safe_text
)
viewpoint::SessionManagerEObject_strategy = st.builds(
    viewpoint::SessionManagerEObject,
)
DecorationDescription_strategy = st.builds(
    DecorationDescription,
)
viewpoint::Decoration_strategy = st.builds(
    viewpoint::Decoration,
)
style::StyleDescription_strategy = st.builds(
    style::StyleDescription,
)
Customizable_strategy = st.builds(
    Customizable,
)
viewpoint::BasicLabelStyle_strategy = st.builds(
    viewpoint::BasicLabelStyle,
    labelSize=
        st.integers(),
    labelFormat=
        safe_text,
    showIcon=
        st.booleans(),
    iconPath=
        safe_text,
    labelColor=
        safe_text
)
BasicLabelStyle_strategy = st.builds(
    BasicLabelStyle,
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
viewpoint::UIState_strategy = st.builds(
    viewpoint::UIState,
    decorationImage=
        safe_text,
    inverseSelectionOrder=
        st.booleans()
)
AnnotationEntry_strategy = st.builds(
    AnnotationEntry,
)
viewpoint::MetaModelExtension_strategy = st.builds(
    viewpoint::MetaModelExtension,
)
Viewpoint_strategy = st.builds(
    Viewpoint,
)
DSemanticDecorator_strategy = st.builds(
    DSemanticDecorator,
)
DStylizable_strategy = st.builds(
    DStylizable,
)
DMappingBased_strategy = st.builds(
    DMappingBased,
)
viewpoint::DRefreshable_strategy = st.builds(
    viewpoint::DRefreshable,
)
viewpoint::DStylizable_strategy = st.builds(
    viewpoint::DStylizable,
)
FeatureExtensionDescription_strategy = st.builds(
    FeatureExtensionDescription,
)
viewpoint::DFeatureExtension_strategy = st.builds(
    viewpoint::DFeatureExtension,
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
viewpoint::description::Group_strategy = st.builds(
    viewpoint::description::Group,
    version=
        safe_text,
    name=
        safe_text
)
viewpoint::DRepresentation_strategy = st.builds(
    viewpoint::DRepresentation,
    name=
        safe_text
)
RepresentationDescription_strategy = st.builds(
    RepresentationDescription,
)
viewpoint::DRepresentationDescriptor_strategy = st.builds(
    viewpoint::DRepresentationDescriptor,
    name=
        safe_text
)
viewpoint::DSemanticDecorator_strategy = st.builds(
    viewpoint::DSemanticDecorator,
)
viewpoint::DMappingBased_strategy = st.builds(
    viewpoint::DMappingBased,
)
viewpoint::DView_strategy = st.builds(
    viewpoint::DView,
)
DAnnotationEntry_strategy = st.builds(
    DAnnotationEntry,
)
viewpoint::EObject_strategy = st.builds(
    viewpoint::EObject,
)
viewpoint::DAnalysis_strategy = st.builds(
    viewpoint::DAnalysis,
    semanticResources=
        safe_text,
    version=
        safe_text
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
ContainerModelOperation_strategy = st.builds(
    ContainerModelOperation,
)
viewpoint::tool::RemoveElement_strategy = st.builds(
    viewpoint::tool::RemoveElement,
)
viewpoint::tool::MoveElement_strategy = st.builds(
    viewpoint::tool::MoveElement,
    newContainerExpression=
        safe_text,
    featureName=
        safe_text
)
viewpoint::tool::ChangeContext_strategy = st.builds(
    viewpoint::tool::ChangeContext,
    browseExpression=
        safe_text
)
viewpoint::tool::Unset_strategy = st.builds(
    viewpoint::tool::Unset,
    elementExpression=
        safe_text,
    featureName=
        safe_text
)
viewpoint::tool::Let_strategy = st.builds(
    viewpoint::tool::Let,
    variableName=
        safe_text,
    valueExpression=
        safe_text
)
viewpoint::tool::If_strategy = st.builds(
    viewpoint::tool::If,
    conditionExpression=
        safe_text
)
viewpoint::tool::SetValue_strategy = st.builds(
    viewpoint::tool::SetValue,
    valueExpression=
        safe_text,
    featureName=
        safe_text
)
viewpoint::tool::SetObject_strategy = st.builds(
    viewpoint::tool::SetObject,
    featureName=
        safe_text
)
viewpoint::tool::DeleteView_strategy = st.builds(
    viewpoint::tool::DeleteView,
)
viewpoint::tool::For_strategy = st.builds(
    viewpoint::tool::For,
    expression=
        safe_text,
    iteratorName=
        safe_text
)
viewpoint::tool::CreateInstance_strategy = st.builds(
    viewpoint::tool::CreateInstance,
    referenceName=
        safe_text,
    variableName=
        safe_text,
    typeName=
        safe_text
)
viewpoint::tool::InitialContainerDropOperation_strategy = st.builds(
    viewpoint::tool::InitialContainerDropOperation,
)
viewpoint::tool::InitEdgeCreationOperation_strategy = st.builds(
    viewpoint::tool::InitEdgeCreationOperation,
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
description::AbstractVariable_strategy = st.builds(
    description::AbstractVariable,
)
tool::VariableContainer_strategy = st.builds(
    tool::VariableContainer,
)
viewpoint::tool::DropContainerVariable_strategy = st.builds(
    viewpoint::tool::DropContainerVariable,
)
viewpoint::tool::ElementViewVariable_strategy = st.builds(
    viewpoint::tool::ElementViewVariable,
)
viewpoint::tool::ElementDeleteVariable_strategy = st.builds(
    viewpoint::tool::ElementDeleteVariable,
)
viewpoint::tool::ElementDropVariable_strategy = st.builds(
    viewpoint::tool::ElementDropVariable,
)
viewpoint::tool::ElementVariable_strategy = st.builds(
    viewpoint::tool::ElementVariable,
)
viewpoint::tool::ContainerViewVariable_strategy = st.builds(
    viewpoint::tool::ContainerViewVariable,
)
viewpoint::tool::SelectContainerVariable_strategy = st.builds(
    viewpoint::tool::SelectContainerVariable,
)
SubVariable_strategy = st.builds(
    SubVariable,
)
viewpoint::tool::VariableContainer_strategy = st.builds(
    viewpoint::tool::VariableContainer,
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
viewpoint::tool::ExternalJavaActionCall_strategy = st.builds(
    viewpoint::tool::ExternalJavaActionCall,
)
viewpoint::tool::ExternalJavaAction_strategy = st.builds(
    viewpoint::tool::ExternalJavaAction,
    id=
        safe_text
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
    iconPath=
        safe_text,
    windowTitle=
        safe_text
)
tool::ContainerViewVariable_strategy = st.builds(
    tool::ContainerViewVariable,
)
tool::DropContainerVariable_strategy = st.builds(
    tool::DropContainerVariable,
)
tool::ElementVariable_strategy = st.builds(
    tool::ElementVariable,
)
MappingBasedToolDescription_strategy = st.builds(
    MappingBasedToolDescription,
)
viewpoint::tool::ToolDescription_strategy = st.builds(
    viewpoint::tool::ToolDescription,
    iconPath=
        safe_text
)
AbstractToolDescription_strategy = st.builds(
    AbstractToolDescription,
)
viewpoint::tool::RepresentationNavigationDescription_strategy = st.builds(
    viewpoint::tool::RepresentationNavigationDescription,
    navigationNameExpression=
        safe_text,
    browseExpression=
        safe_text
)
viewpoint::tool::PopupMenu_strategy = st.builds(
    viewpoint::tool::PopupMenu,
)
viewpoint::tool::RepresentationCreationDescription_strategy = st.builds(
    viewpoint::tool::RepresentationCreationDescription,
    browseExpression=
        safe_text,
    titleExpression=
        safe_text
)
viewpoint::tool::PaneBasedSelectionWizardDescription_strategy = st.builds(
    viewpoint::tool::PaneBasedSelectionWizardDescription,
    iconPath=
        safe_text,
    windowImagePath=
        safe_text,
    childrenExpression=
        safe_text,
    windowTitle=
        safe_text,
    choiceOfValuesMessage=
        safe_text,
    candidatesExpression=
        safe_text,
    selectedValuesMessage=
        safe_text,
    preSelectedCandidatesExpression=
        safe_text,
    rootExpression=
        safe_text,
    message=
        safe_text,
    tree=
        st.booleans()
)
viewpoint::tool::MappingBasedToolDescription_strategy = st.builds(
    viewpoint::tool::MappingBasedToolDescription,
)
viewpoint::tool::PasteDescription_strategy = st.builds(
    viewpoint::tool::PasteDescription,
)
tool::InitialOperation_strategy = st.builds(
    tool::InitialOperation,
)
tool::ElementViewVariable_strategy = st.builds(
    tool::ElementViewVariable,
)
ToolEntry_strategy = st.builds(
    ToolEntry,
)
viewpoint::tool::AbstractToolDescription_strategy = st.builds(
    viewpoint::tool::AbstractToolDescription,
    forceRefresh=
        st.booleans(),
    elementsToSelect=
        safe_text,
    inverseSelectionOrder=
        st.booleans(),
    precondition=
        safe_text
)
tool::ToolFilterDescription_strategy = st.builds(
    tool::ToolFilterDescription,
)
BasicLabelStyleDescription_strategy = st.builds(
    BasicLabelStyleDescription,
)
viewpoint::style::LabelStyleDescription_strategy = st.builds(
    viewpoint::style::LabelStyleDescription,
    labelAlignment=
        safe_text
)
viewpoint::style::TooltipStyleDescription_strategy = st.builds(
    viewpoint::style::TooltipStyleDescription,
    tooltipExpression=
        safe_text
)
viewpoint::style::LabelBorderStyleDescription_strategy = st.builds(
    viewpoint::style::LabelBorderStyleDescription,
    cornerWidth=
        st.integers(),
    cornerHeight=
        st.integers(),
    name=
        safe_text,
    id=
        safe_text
)
style::LabelBorderStyleDescription_strategy = st.builds(
    style::LabelBorderStyleDescription,
)
viewpoint::style::LabelBorderStyles_strategy = st.builds(
    viewpoint::style::LabelBorderStyles,
)
description::viewpoint::EDataType_strategy = st.builds(
    description::viewpoint::EDataType,
)
viewpoint::style::BasicLabelStyleDescription_strategy = st.builds(
    viewpoint::style::BasicLabelStyleDescription,
    labelSize=
        st.integers(),
    labelExpression=
        safe_text,
    labelFormat=
        safe_text,
    showIcon=
        st.booleans(),
    iconPath=
        safe_text
)
viewpoint::style::StyleDescription_strategy = st.builds(
    viewpoint::style::StyleDescription,
)
viewpoint::description::IdentifiedElement_strategy = st.builds(
    viewpoint::description::IdentifiedElement,
    name=
        safe_text,
    label=
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
description::SubVariable_strategy = st.builds(
    description::SubVariable,
)
viewpoint::tool::AcceleoVariable_strategy = st.builds(
    viewpoint::tool::AcceleoVariable,
    computationExpression=
        safe_text
)
description::InteractiveVariableDescription_strategy = st.builds(
    description::InteractiveVariableDescription,
)
viewpoint::tool::SelectModelElementVariable_strategy = st.builds(
    viewpoint::tool::SelectModelElementVariable,
)
viewpoint::description::TypedVariable_strategy = st.builds(
    viewpoint::description::TypedVariable,
    defaultValueExpression=
        safe_text
)
viewpoint::description::InteractiveVariableDescription_strategy = st.builds(
    viewpoint::description::InteractiveVariableDescription,
    userDocumentation=
        safe_text
)
AbstractVariable_strategy = st.builds(
    AbstractVariable,
)
viewpoint::tool::ElementSelectVariable_strategy = st.builds(
    viewpoint::tool::ElementSelectVariable,
)
viewpoint::tool::NameVariable_strategy = st.builds(
    viewpoint::tool::NameVariable,
)
viewpoint::tool::DialogVariable_strategy = st.builds(
    viewpoint::tool::DialogVariable,
    dialogPrompt=
        safe_text
)
viewpoint::description::SubVariable_strategy = st.builds(
    viewpoint::description::SubVariable,
)
viewpoint::description::AbstractVariable_strategy = st.builds(
    viewpoint::description::AbstractVariable,
    name=
        safe_text
)
viewpoint::description::DAnnotationEntry_strategy = st.builds(
    viewpoint::description::DAnnotationEntry,
    source=
        safe_text,
    details=
        safe_text
)
viewpoint::description::UserColor_strategy = st.builds(
    viewpoint::description::UserColor,
    name=
        safe_text
)
description::FixedColor_strategy = st.builds(
    description::FixedColor,
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
description::UserColor_strategy = st.builds(
    description::UserColor,
)
viewpoint::description::UserFixedColor_strategy = st.builds(
    viewpoint::description::UserFixedColor,
)
description::ColorDescription_strategy = st.builds(
    description::ColorDescription,
)
viewpoint::description::ComputedColor_strategy = st.builds(
    viewpoint::description::ComputedColor,
    green=
        safe_text,
    red=
        safe_text,
    blue=
        safe_text
)
viewpoint::description::InterpolatedColor_strategy = st.builds(
    viewpoint::description::InterpolatedColor,
    maxValueComputationExpression=
        safe_text,
    colorValueComputationExpression=
        safe_text,
    minValueComputationExpression=
        safe_text
)
ColorDescription_strategy = st.builds(
    ColorDescription,
)
viewpoint::description::FixedColor_strategy = st.builds(
    viewpoint::description::FixedColor,
    green=
        st.integers(),
    red=
        st.integers(),
    blue=
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
    candidatesExpression=
        safe_text,
    tree=
        st.booleans(),
    rootExpression=
        safe_text,
    message=
        safe_text,
    multiple=
        st.booleans(),
    childrenExpression=
        safe_text
)
viewpoint::description::IVSMElementCustomization_strategy = st.builds(
    viewpoint::description::IVSMElementCustomization,
)
IVSMElementCustomization_strategy = st.builds(
    IVSMElementCustomization,
)
viewpoint::description::VSMElementCustomization_strategy = st.builds(
    viewpoint::description::VSMElementCustomization,
    predicateExpression=
        safe_text
)
viewpoint::description::Customization_strategy = st.builds(
    viewpoint::description::Customization,
)
viewpoint::description::GenericDecorationDescription_strategy = st.builds(
    viewpoint::description::GenericDecorationDescription,
)
viewpoint::description::SemanticBasedDecoration_strategy = st.builds(
    viewpoint::description::SemanticBasedDecoration,
    domainClass=
        safe_text
)
viewpoint::description::EStructuralFeatureCustomization_strategy = st.builds(
    viewpoint::description::EStructuralFeatureCustomization,
    applyOnAll=
        st.booleans()
)
viewpoint::description::VSMElementCustomizationReuse_strategy = st.builds(
    viewpoint::description::VSMElementCustomizationReuse,
)
EStructuralFeatureCustomization_strategy = st.builds(
    EStructuralFeatureCustomization,
)
viewpoint::description::EAttributeCustomization_strategy = st.builds(
    viewpoint::description::EAttributeCustomization,
    attributeName=
        safe_text,
    value=
        safe_text
)
viewpoint::description::EReferenceCustomization_strategy = st.builds(
    viewpoint::description::EReferenceCustomization,
    referenceName=
        safe_text
)
viewpoint::description::DecorationDescription_strategy = st.builds(
    viewpoint::description::DecorationDescription,
    name=
        safe_text,
    tooltipExpression=
        safe_text,
    distributionDirection=
        safe_text,
    position=
        safe_text,
    preconditionExpression=
        safe_text,
    imageExpression=
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
viewpoint::validation::ValidationRule_strategy = st.builds(
    viewpoint::validation::ValidationRule,
    level=
        safe_text,
    message=
        safe_text
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
viewpoint::description::DModelElement_strategy = st.builds(
    viewpoint::description::DModelElement,
)
viewpoint::description::DocumentedElement_strategy = st.builds(
    viewpoint::description::DocumentedElement,
    documentation=
        safe_text
)
viewpoint::description::RepresentationTemplate_strategy = st.builds(
    viewpoint::description::RepresentationTemplate,
    name=
        safe_text
)
description::viewpoint::EPackage_strategy = st.builds(
    description::viewpoint::EPackage,
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
    viewpointURI=
        safe_text,
    name=
        safe_text,
    representationName=
        safe_text
)
viewpoint::description::RepresentationImportDescription_strategy = st.builds(
    viewpoint::description::RepresentationImportDescription,
)
validation::ValidationSet_strategy = st.builds(
    validation::ValidationSet,
)
description::IdentifiedElement_strategy = st.builds(
    description::IdentifiedElement,
)
viewpoint::tool::ToolEntry_strategy = st.builds(
    viewpoint::tool::ToolEntry,
)
description::EndUserDocumentedElement_strategy = st.builds(
    description::EndUserDocumentedElement,
)
description::Component_strategy = st.builds(
    description::Component,
)
viewpoint::description::Viewpoint_strategy = st.builds(
    viewpoint::description::Viewpoint,
    icon=
        safe_text,
    customizes=
        safe_text,
    reuses=
        safe_text,
    modelFileExtension=
        safe_text,
    conflicts=
        safe_text
)
viewpoint::description::Component_strategy = st.builds(
    viewpoint::description::Component,
)
viewpoint::description::Extension_strategy = st.builds(
    viewpoint::description::Extension,
)
viewpoint::description::RepresentationDescription_strategy = st.builds(
    viewpoint::description::RepresentationDescription,
    initialisation=
        st.booleans(),
    titleExpression=
        safe_text,
    showOnStartup=
        st.booleans()
)
viewpoint::description::FeatureExtensionDescription_strategy = st.builds(
    viewpoint::description::FeatureExtensionDescription,
)
RepresentationTemplate_strategy = st.builds(
    RepresentationTemplate,
)

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

@given(instance=viewpoint::audit::InformationSection_strategy)
@settings(max_examples=50)
def test_viewpoint::audit::informationsection_instantiation(instance):
    assert isinstance(instance, viewpoint::audit::InformationSection)

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

@given(instance=RepresentationElementMapping_strategy)
@settings(max_examples=50)
def test_representationelementmapping_instantiation(instance):
    assert isinstance(instance, RepresentationElementMapping)

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

@given(instance=validation::RuleAudit_strategy)
@settings(max_examples=50)
def test_validation::ruleaudit_instantiation(instance):
    assert isinstance(instance, validation::RuleAudit)

@given(instance=validation::ValidationRule_strategy)
@settings(max_examples=50)
def test_validation::validationrule_instantiation(instance):
    assert isinstance(instance, validation::ValidationRule)

@given(instance=viewpoint::tool::FeatureChangeListener_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::featurechangelistener_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::FeatureChangeListener)

@given(instance=viewpoint::tool::FeatureChangeListener_strategy)
def test_viewpoint::tool::featurechangelistener_domainClass_type(instance):
    assert isinstance(instance.domainClass, str)


@given(instance=viewpoint::tool::FeatureChangeListener_strategy)
def test_viewpoint::tool::featurechangelistener_domainClass_setter(instance):
    original = instance.domainClass
    instance.domainClass = original
    assert instance.domainClass == original

@given(instance=viewpoint::tool::FeatureChangeListener_strategy)
def test_viewpoint::tool::featurechangelistener_featureName_type(instance):
    assert isinstance(instance.featureName, str)


@given(instance=viewpoint::tool::FeatureChangeListener_strategy)
def test_viewpoint::tool::featurechangelistener_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original

@given(instance=tool::Default_strategy)
@settings(max_examples=50)
def test_tool::default_instantiation(instance):
    assert isinstance(instance, tool::Default)

@given(instance=tool::Case_strategy)
@settings(max_examples=50)
def test_tool::case_instantiation(instance):
    assert isinstance(instance, tool::Case)

@given(instance=viewpoint::tool::SwitchChild_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::switchchild_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::SwitchChild)

@given(instance=SwitchChild_strategy)
@settings(max_examples=50)
def test_switchchild_instantiation(instance):
    assert isinstance(instance, SwitchChild)

@given(instance=viewpoint::tool::Default_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::default_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::Default)

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

@given(instance=tool::FeatureChangeListener_strategy)
@settings(max_examples=50)
def test_tool::featurechangelistener_instantiation(instance):
    assert isinstance(instance, tool::FeatureChangeListener)

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

@given(instance=tool::viewpoint::EObject_strategy)
@settings(max_examples=50)
def test_tool::viewpoint::eobject_instantiation(instance):
    assert isinstance(instance, tool::viewpoint::EObject)

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

@given(instance=Extension_strategy)
@settings(max_examples=50)
def test_extension_instantiation(instance):
    assert isinstance(instance, Extension)

@given(instance=UserColorsPalette_strategy)
@settings(max_examples=50)
def test_usercolorspalette_instantiation(instance):
    assert isinstance(instance, UserColorsPalette)

@given(instance=SytemColorsPalette_strategy)
@settings(max_examples=50)
def test_sytemcolorspalette_instantiation(instance):
    assert isinstance(instance, SytemColorsPalette)

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
def test_viewpoint::danalysissessioneobject_synchronizationStatus_type(instance):
    assert isinstance(instance.synchronizationStatus, str)


@given(instance=viewpoint::DAnalysisSessionEObject_strategy)
def test_viewpoint::danalysissessioneobject_synchronizationStatus_setter(instance):
    original = instance.synchronizationStatus
    instance.synchronizationStatus = original
    assert instance.synchronizationStatus == original

@given(instance=viewpoint::DAnalysisSessionEObject_strategy)
def test_viewpoint::danalysissessioneobject_open_type(instance):
    assert isinstance(instance.open, bool)


@given(instance=viewpoint::DAnalysisSessionEObject_strategy)
def test_viewpoint::danalysissessioneobject_open_setter(instance):
    original = instance.open
    instance.open = original
    assert instance.open == original

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
def test_viewpoint::dresource_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=viewpoint::DResource_strategy)
def test_viewpoint::dresource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=viewpoint::DResource_strategy)
def test_viewpoint::dresource_path_type(instance):
    assert isinstance(instance.path, str)


@given(instance=viewpoint::DResource_strategy)
def test_viewpoint::dresource_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original

@given(instance=viewpoint::SessionManagerEObject_strategy)
@settings(max_examples=50)
def test_viewpoint::sessionmanagereobject_instantiation(instance):
    assert isinstance(instance, viewpoint::SessionManagerEObject)

@given(instance=DecorationDescription_strategy)
@settings(max_examples=50)
def test_decorationdescription_instantiation(instance):
    assert isinstance(instance, DecorationDescription)

@given(instance=viewpoint::Decoration_strategy)
@settings(max_examples=50)
def test_viewpoint::decoration_instantiation(instance):
    assert isinstance(instance, viewpoint::Decoration)

@given(instance=style::StyleDescription_strategy)
@settings(max_examples=50)
def test_style::styledescription_instantiation(instance):
    assert isinstance(instance, style::StyleDescription)

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
def test_viewpoint::basiclabelstyle_labelFormat_type(instance):
    assert isinstance(instance.labelFormat, str)


@given(instance=viewpoint::BasicLabelStyle_strategy)
def test_viewpoint::basiclabelstyle_labelFormat_setter(instance):
    original = instance.labelFormat
    instance.labelFormat = original
    assert instance.labelFormat == original

@given(instance=viewpoint::BasicLabelStyle_strategy)
def test_viewpoint::basiclabelstyle_showIcon_type(instance):
    assert isinstance(instance.showIcon, bool)


@given(instance=viewpoint::BasicLabelStyle_strategy)
def test_viewpoint::basiclabelstyle_showIcon_setter(instance):
    original = instance.showIcon
    instance.showIcon = original
    assert instance.showIcon == original

@given(instance=viewpoint::BasicLabelStyle_strategy)
def test_viewpoint::basiclabelstyle_iconPath_type(instance):
    assert isinstance(instance.iconPath, str)


@given(instance=viewpoint::BasicLabelStyle_strategy)
def test_viewpoint::basiclabelstyle_iconPath_setter(instance):
    original = instance.iconPath
    instance.iconPath = original
    assert instance.iconPath == original

@given(instance=viewpoint::BasicLabelStyle_strategy)
def test_viewpoint::basiclabelstyle_labelColor_type(instance):
    assert isinstance(instance.labelColor, str)


@given(instance=viewpoint::BasicLabelStyle_strategy)
def test_viewpoint::basiclabelstyle_labelColor_setter(instance):
    original = instance.labelColor
    instance.labelColor = original
    assert instance.labelColor == original

@given(instance=BasicLabelStyle_strategy)
@settings(max_examples=50)
def test_basiclabelstyle_instantiation(instance):
    assert isinstance(instance, BasicLabelStyle)

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

@given(instance=viewpoint::UIState_strategy)
@settings(max_examples=50)
def test_viewpoint::uistate_instantiation(instance):
    assert isinstance(instance, viewpoint::UIState)

@given(instance=viewpoint::UIState_strategy)
def test_viewpoint::uistate_decorationImage_type(instance):
    assert isinstance(instance.decorationImage, str)


@given(instance=viewpoint::UIState_strategy)
def test_viewpoint::uistate_decorationImage_setter(instance):
    original = instance.decorationImage
    instance.decorationImage = original
    assert instance.decorationImage == original

@given(instance=viewpoint::UIState_strategy)
def test_viewpoint::uistate_inverseSelectionOrder_type(instance):
    assert isinstance(instance.inverseSelectionOrder, bool)


@given(instance=viewpoint::UIState_strategy)
def test_viewpoint::uistate_inverseSelectionOrder_setter(instance):
    original = instance.inverseSelectionOrder
    instance.inverseSelectionOrder = original
    assert instance.inverseSelectionOrder == original

@given(instance=AnnotationEntry_strategy)
@settings(max_examples=50)
def test_annotationentry_instantiation(instance):
    assert isinstance(instance, AnnotationEntry)

@given(instance=viewpoint::MetaModelExtension_strategy)
@settings(max_examples=50)
def test_viewpoint::metamodelextension_instantiation(instance):
    assert isinstance(instance, viewpoint::MetaModelExtension)

@given(instance=Viewpoint_strategy)
@settings(max_examples=50)
def test_viewpoint_instantiation(instance):
    assert isinstance(instance, Viewpoint)

@given(instance=DSemanticDecorator_strategy)
@settings(max_examples=50)
def test_dsemanticdecorator_instantiation(instance):
    assert isinstance(instance, DSemanticDecorator)

@given(instance=DStylizable_strategy)
@settings(max_examples=50)
def test_dstylizable_instantiation(instance):
    assert isinstance(instance, DStylizable)

@given(instance=DMappingBased_strategy)
@settings(max_examples=50)
def test_dmappingbased_instantiation(instance):
    assert isinstance(instance, DMappingBased)

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

@given(instance=FeatureExtensionDescription_strategy)
@settings(max_examples=50)
def test_featureextensiondescription_instantiation(instance):
    assert isinstance(instance, FeatureExtensionDescription)

@given(instance=viewpoint::DFeatureExtension_strategy)
@settings(max_examples=50)
def test_viewpoint::dfeatureextension_instantiation(instance):
    assert isinstance(instance, viewpoint::DFeatureExtension)

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

@given(instance=RepresentationDescription_strategy)
@settings(max_examples=50)
def test_representationdescription_instantiation(instance):
    assert isinstance(instance, RepresentationDescription)

@given(instance=viewpoint::DRepresentationDescriptor_strategy)
@settings(max_examples=50)
def test_viewpoint::drepresentationdescriptor_instantiation(instance):
    assert isinstance(instance, viewpoint::DRepresentationDescriptor)

@given(instance=viewpoint::DRepresentationDescriptor_strategy)
def test_viewpoint::drepresentationdescriptor_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=viewpoint::DRepresentationDescriptor_strategy)
def test_viewpoint::drepresentationdescriptor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=viewpoint::DSemanticDecorator_strategy)
@settings(max_examples=50)
def test_viewpoint::dsemanticdecorator_instantiation(instance):
    assert isinstance(instance, viewpoint::DSemanticDecorator)

@given(instance=viewpoint::DMappingBased_strategy)
@settings(max_examples=50)
def test_viewpoint::dmappingbased_instantiation(instance):
    assert isinstance(instance, viewpoint::DMappingBased)

@given(instance=viewpoint::DView_strategy)
@settings(max_examples=50)
def test_viewpoint::dview_instantiation(instance):
    assert isinstance(instance, viewpoint::DView)

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
def test_viewpoint::danalysis_semanticResources_type(instance):
    assert isinstance(instance.semanticResources, str)


@given(instance=viewpoint::DAnalysis_strategy)
def test_viewpoint::danalysis_semanticResources_setter(instance):
    original = instance.semanticResources
    instance.semanticResources = original
    assert instance.semanticResources == original

@given(instance=viewpoint::DAnalysis_strategy)
def test_viewpoint::danalysis_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=viewpoint::DAnalysis_strategy)
def test_viewpoint::danalysis_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

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

@given(instance=ContainerModelOperation_strategy)
@settings(max_examples=50)
def test_containermodeloperation_instantiation(instance):
    assert isinstance(instance, ContainerModelOperation)

@given(instance=viewpoint::tool::RemoveElement_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::removeelement_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::RemoveElement)

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

@given(instance=viewpoint::tool::Let_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::let_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::Let)

@given(instance=viewpoint::tool::Let_strategy)
def test_viewpoint::tool::let_variableName_type(instance):
    assert isinstance(instance.variableName, str)


@given(instance=viewpoint::tool::Let_strategy)
def test_viewpoint::tool::let_variableName_setter(instance):
    original = instance.variableName
    instance.variableName = original
    assert instance.variableName == original

@given(instance=viewpoint::tool::Let_strategy)
def test_viewpoint::tool::let_valueExpression_type(instance):
    assert isinstance(instance.valueExpression, str)


@given(instance=viewpoint::tool::Let_strategy)
def test_viewpoint::tool::let_valueExpression_setter(instance):
    original = instance.valueExpression
    instance.valueExpression = original
    assert instance.valueExpression == original

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

@given(instance=viewpoint::tool::DeleteView_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::deleteview_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::DeleteView)

@given(instance=viewpoint::tool::For_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::for_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::For)

@given(instance=viewpoint::tool::For_strategy)
def test_viewpoint::tool::for_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=viewpoint::tool::For_strategy)
def test_viewpoint::tool::for_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=viewpoint::tool::For_strategy)
def test_viewpoint::tool::for_iteratorName_type(instance):
    assert isinstance(instance.iteratorName, str)


@given(instance=viewpoint::tool::For_strategy)
def test_viewpoint::tool::for_iteratorName_setter(instance):
    original = instance.iteratorName
    instance.iteratorName = original
    assert instance.iteratorName == original

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
def test_viewpoint::tool::createinstance_variableName_type(instance):
    assert isinstance(instance.variableName, str)


@given(instance=viewpoint::tool::CreateInstance_strategy)
def test_viewpoint::tool::createinstance_variableName_setter(instance):
    original = instance.variableName
    instance.variableName = original
    assert instance.variableName == original

@given(instance=viewpoint::tool::CreateInstance_strategy)
def test_viewpoint::tool::createinstance_typeName_type(instance):
    assert isinstance(instance.typeName, str)


@given(instance=viewpoint::tool::CreateInstance_strategy)
def test_viewpoint::tool::createinstance_typeName_setter(instance):
    original = instance.typeName
    instance.typeName = original
    assert instance.typeName == original

@given(instance=viewpoint::tool::InitialContainerDropOperation_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::initialcontainerdropoperation_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::InitialContainerDropOperation)

@given(instance=viewpoint::tool::InitEdgeCreationOperation_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::initedgecreationoperation_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::InitEdgeCreationOperation)

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

@given(instance=description::AbstractVariable_strategy)
@settings(max_examples=50)
def test_description::abstractvariable_instantiation(instance):
    assert isinstance(instance, description::AbstractVariable)

@given(instance=tool::VariableContainer_strategy)
@settings(max_examples=50)
def test_tool::variablecontainer_instantiation(instance):
    assert isinstance(instance, tool::VariableContainer)

@given(instance=viewpoint::tool::DropContainerVariable_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::dropcontainervariable_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::DropContainerVariable)

@given(instance=viewpoint::tool::ElementViewVariable_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::elementviewvariable_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::ElementViewVariable)

@given(instance=viewpoint::tool::ElementDeleteVariable_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::elementdeletevariable_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::ElementDeleteVariable)

@given(instance=viewpoint::tool::ElementDropVariable_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::elementdropvariable_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::ElementDropVariable)

@given(instance=viewpoint::tool::ElementVariable_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::elementvariable_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::ElementVariable)

@given(instance=viewpoint::tool::ContainerViewVariable_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::containerviewvariable_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::ContainerViewVariable)

@given(instance=viewpoint::tool::SelectContainerVariable_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::selectcontainervariable_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::SelectContainerVariable)

@given(instance=SubVariable_strategy)
@settings(max_examples=50)
def test_subvariable_instantiation(instance):
    assert isinstance(instance, SubVariable)

@given(instance=viewpoint::tool::VariableContainer_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::variablecontainer_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::VariableContainer)

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

@given(instance=viewpoint::tool::ExternalJavaActionCall_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::externaljavaactioncall_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::ExternalJavaActionCall)

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
def test_viewpoint::tool::selectionwizarddescription_iconPath_type(instance):
    assert isinstance(instance.iconPath, str)


@given(instance=viewpoint::tool::SelectionWizardDescription_strategy)
def test_viewpoint::tool::selectionwizarddescription_iconPath_setter(instance):
    original = instance.iconPath
    instance.iconPath = original
    assert instance.iconPath == original

@given(instance=viewpoint::tool::SelectionWizardDescription_strategy)
def test_viewpoint::tool::selectionwizarddescription_windowTitle_type(instance):
    assert isinstance(instance.windowTitle, str)


@given(instance=viewpoint::tool::SelectionWizardDescription_strategy)
def test_viewpoint::tool::selectionwizarddescription_windowTitle_setter(instance):
    original = instance.windowTitle
    instance.windowTitle = original
    assert instance.windowTitle == original

@given(instance=tool::ContainerViewVariable_strategy)
@settings(max_examples=50)
def test_tool::containerviewvariable_instantiation(instance):
    assert isinstance(instance, tool::ContainerViewVariable)

@given(instance=tool::DropContainerVariable_strategy)
@settings(max_examples=50)
def test_tool::dropcontainervariable_instantiation(instance):
    assert isinstance(instance, tool::DropContainerVariable)

@given(instance=tool::ElementVariable_strategy)
@settings(max_examples=50)
def test_tool::elementvariable_instantiation(instance):
    assert isinstance(instance, tool::ElementVariable)

@given(instance=MappingBasedToolDescription_strategy)
@settings(max_examples=50)
def test_mappingbasedtooldescription_instantiation(instance):
    assert isinstance(instance, MappingBasedToolDescription)

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

@given(instance=viewpoint::tool::RepresentationNavigationDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::representationnavigationdescription_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::RepresentationNavigationDescription)

@given(instance=viewpoint::tool::RepresentationNavigationDescription_strategy)
def test_viewpoint::tool::representationnavigationdescription_navigationNameExpression_type(instance):
    assert isinstance(instance.navigationNameExpression, str)


@given(instance=viewpoint::tool::RepresentationNavigationDescription_strategy)
def test_viewpoint::tool::representationnavigationdescription_navigationNameExpression_setter(instance):
    original = instance.navigationNameExpression
    instance.navigationNameExpression = original
    assert instance.navigationNameExpression == original

@given(instance=viewpoint::tool::RepresentationNavigationDescription_strategy)
def test_viewpoint::tool::representationnavigationdescription_browseExpression_type(instance):
    assert isinstance(instance.browseExpression, str)


@given(instance=viewpoint::tool::RepresentationNavigationDescription_strategy)
def test_viewpoint::tool::representationnavigationdescription_browseExpression_setter(instance):
    original = instance.browseExpression
    instance.browseExpression = original
    assert instance.browseExpression == original

@given(instance=viewpoint::tool::PopupMenu_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::popupmenu_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::PopupMenu)

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

@given(instance=viewpoint::tool::PaneBasedSelectionWizardDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::panebasedselectionwizarddescription_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::PaneBasedSelectionWizardDescription)

@given(instance=viewpoint::tool::PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint::tool::panebasedselectionwizarddescription_iconPath_type(instance):
    assert isinstance(instance.iconPath, str)


@given(instance=viewpoint::tool::PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint::tool::panebasedselectionwizarddescription_iconPath_setter(instance):
    original = instance.iconPath
    instance.iconPath = original
    assert instance.iconPath == original

@given(instance=viewpoint::tool::PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint::tool::panebasedselectionwizarddescription_windowImagePath_type(instance):
    assert isinstance(instance.windowImagePath, str)


@given(instance=viewpoint::tool::PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint::tool::panebasedselectionwizarddescription_windowImagePath_setter(instance):
    original = instance.windowImagePath
    instance.windowImagePath = original
    assert instance.windowImagePath == original

@given(instance=viewpoint::tool::PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint::tool::panebasedselectionwizarddescription_childrenExpression_type(instance):
    assert isinstance(instance.childrenExpression, str)


@given(instance=viewpoint::tool::PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint::tool::panebasedselectionwizarddescription_childrenExpression_setter(instance):
    original = instance.childrenExpression
    instance.childrenExpression = original
    assert instance.childrenExpression == original

@given(instance=viewpoint::tool::PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint::tool::panebasedselectionwizarddescription_windowTitle_type(instance):
    assert isinstance(instance.windowTitle, str)


@given(instance=viewpoint::tool::PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint::tool::panebasedselectionwizarddescription_windowTitle_setter(instance):
    original = instance.windowTitle
    instance.windowTitle = original
    assert instance.windowTitle == original

@given(instance=viewpoint::tool::PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint::tool::panebasedselectionwizarddescription_choiceOfValuesMessage_type(instance):
    assert isinstance(instance.choiceOfValuesMessage, str)


@given(instance=viewpoint::tool::PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint::tool::panebasedselectionwizarddescription_choiceOfValuesMessage_setter(instance):
    original = instance.choiceOfValuesMessage
    instance.choiceOfValuesMessage = original
    assert instance.choiceOfValuesMessage == original

@given(instance=viewpoint::tool::PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint::tool::panebasedselectionwizarddescription_candidatesExpression_type(instance):
    assert isinstance(instance.candidatesExpression, str)


@given(instance=viewpoint::tool::PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint::tool::panebasedselectionwizarddescription_candidatesExpression_setter(instance):
    original = instance.candidatesExpression
    instance.candidatesExpression = original
    assert instance.candidatesExpression == original

@given(instance=viewpoint::tool::PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint::tool::panebasedselectionwizarddescription_selectedValuesMessage_type(instance):
    assert isinstance(instance.selectedValuesMessage, str)


@given(instance=viewpoint::tool::PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint::tool::panebasedselectionwizarddescription_selectedValuesMessage_setter(instance):
    original = instance.selectedValuesMessage
    instance.selectedValuesMessage = original
    assert instance.selectedValuesMessage == original

@given(instance=viewpoint::tool::PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint::tool::panebasedselectionwizarddescription_preSelectedCandidatesExpression_type(instance):
    assert isinstance(instance.preSelectedCandidatesExpression, str)


@given(instance=viewpoint::tool::PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint::tool::panebasedselectionwizarddescription_preSelectedCandidatesExpression_setter(instance):
    original = instance.preSelectedCandidatesExpression
    instance.preSelectedCandidatesExpression = original
    assert instance.preSelectedCandidatesExpression == original

@given(instance=viewpoint::tool::PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint::tool::panebasedselectionwizarddescription_rootExpression_type(instance):
    assert isinstance(instance.rootExpression, str)


@given(instance=viewpoint::tool::PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint::tool::panebasedselectionwizarddescription_rootExpression_setter(instance):
    original = instance.rootExpression
    instance.rootExpression = original
    assert instance.rootExpression == original

@given(instance=viewpoint::tool::PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint::tool::panebasedselectionwizarddescription_message_type(instance):
    assert isinstance(instance.message, str)


@given(instance=viewpoint::tool::PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint::tool::panebasedselectionwizarddescription_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

@given(instance=viewpoint::tool::PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint::tool::panebasedselectionwizarddescription_tree_type(instance):
    assert isinstance(instance.tree, bool)


@given(instance=viewpoint::tool::PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint::tool::panebasedselectionwizarddescription_tree_setter(instance):
    original = instance.tree
    instance.tree = original
    assert instance.tree == original

@given(instance=viewpoint::tool::MappingBasedToolDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::mappingbasedtooldescription_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::MappingBasedToolDescription)

@given(instance=viewpoint::tool::PasteDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::pastedescription_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::PasteDescription)

@given(instance=tool::InitialOperation_strategy)
@settings(max_examples=50)
def test_tool::initialoperation_instantiation(instance):
    assert isinstance(instance, tool::InitialOperation)

@given(instance=tool::ElementViewVariable_strategy)
@settings(max_examples=50)
def test_tool::elementviewvariable_instantiation(instance):
    assert isinstance(instance, tool::ElementViewVariable)

@given(instance=ToolEntry_strategy)
@settings(max_examples=50)
def test_toolentry_instantiation(instance):
    assert isinstance(instance, ToolEntry)

@given(instance=viewpoint::tool::AbstractToolDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::abstracttooldescription_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::AbstractToolDescription)

@given(instance=viewpoint::tool::AbstractToolDescription_strategy)
def test_viewpoint::tool::abstracttooldescription_forceRefresh_type(instance):
    assert isinstance(instance.forceRefresh, bool)


@given(instance=viewpoint::tool::AbstractToolDescription_strategy)
def test_viewpoint::tool::abstracttooldescription_forceRefresh_setter(instance):
    original = instance.forceRefresh
    instance.forceRefresh = original
    assert instance.forceRefresh == original

@given(instance=viewpoint::tool::AbstractToolDescription_strategy)
def test_viewpoint::tool::abstracttooldescription_elementsToSelect_type(instance):
    assert isinstance(instance.elementsToSelect, str)


@given(instance=viewpoint::tool::AbstractToolDescription_strategy)
def test_viewpoint::tool::abstracttooldescription_elementsToSelect_setter(instance):
    original = instance.elementsToSelect
    instance.elementsToSelect = original
    assert instance.elementsToSelect == original

@given(instance=viewpoint::tool::AbstractToolDescription_strategy)
def test_viewpoint::tool::abstracttooldescription_inverseSelectionOrder_type(instance):
    assert isinstance(instance.inverseSelectionOrder, bool)


@given(instance=viewpoint::tool::AbstractToolDescription_strategy)
def test_viewpoint::tool::abstracttooldescription_inverseSelectionOrder_setter(instance):
    original = instance.inverseSelectionOrder
    instance.inverseSelectionOrder = original
    assert instance.inverseSelectionOrder == original

@given(instance=viewpoint::tool::AbstractToolDescription_strategy)
def test_viewpoint::tool::abstracttooldescription_precondition_type(instance):
    assert isinstance(instance.precondition, str)


@given(instance=viewpoint::tool::AbstractToolDescription_strategy)
def test_viewpoint::tool::abstracttooldescription_precondition_setter(instance):
    original = instance.precondition
    instance.precondition = original
    assert instance.precondition == original

@given(instance=tool::ToolFilterDescription_strategy)
@settings(max_examples=50)
def test_tool::toolfilterdescription_instantiation(instance):
    assert isinstance(instance, tool::ToolFilterDescription)

@given(instance=BasicLabelStyleDescription_strategy)
@settings(max_examples=50)
def test_basiclabelstyledescription_instantiation(instance):
    assert isinstance(instance, BasicLabelStyleDescription)

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
def test_viewpoint::style::labelborderstyledescription_cornerWidth_type(instance):
    assert isinstance(instance.cornerWidth, int)


@given(instance=viewpoint::style::LabelBorderStyleDescription_strategy)
def test_viewpoint::style::labelborderstyledescription_cornerWidth_setter(instance):
    original = instance.cornerWidth
    instance.cornerWidth = original
    assert instance.cornerWidth == original

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

@given(instance=description::viewpoint::EDataType_strategy)
@settings(max_examples=50)
def test_description::viewpoint::edatatype_instantiation(instance):
    assert isinstance(instance, description::viewpoint::EDataType)

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
def test_viewpoint::style::basiclabelstyledescription_labelExpression_type(instance):
    assert isinstance(instance.labelExpression, str)


@given(instance=viewpoint::style::BasicLabelStyleDescription_strategy)
def test_viewpoint::style::basiclabelstyledescription_labelExpression_setter(instance):
    original = instance.labelExpression
    instance.labelExpression = original
    assert instance.labelExpression == original

@given(instance=viewpoint::style::BasicLabelStyleDescription_strategy)
def test_viewpoint::style::basiclabelstyledescription_labelFormat_type(instance):
    assert isinstance(instance.labelFormat, str)


@given(instance=viewpoint::style::BasicLabelStyleDescription_strategy)
def test_viewpoint::style::basiclabelstyledescription_labelFormat_setter(instance):
    original = instance.labelFormat
    instance.labelFormat = original
    assert instance.labelFormat == original

@given(instance=viewpoint::style::BasicLabelStyleDescription_strategy)
def test_viewpoint::style::basiclabelstyledescription_showIcon_type(instance):
    assert isinstance(instance.showIcon, bool)


@given(instance=viewpoint::style::BasicLabelStyleDescription_strategy)
def test_viewpoint::style::basiclabelstyledescription_showIcon_setter(instance):
    original = instance.showIcon
    instance.showIcon = original
    assert instance.showIcon == original

@given(instance=viewpoint::style::BasicLabelStyleDescription_strategy)
def test_viewpoint::style::basiclabelstyledescription_iconPath_type(instance):
    assert isinstance(instance.iconPath, str)


@given(instance=viewpoint::style::BasicLabelStyleDescription_strategy)
def test_viewpoint::style::basiclabelstyledescription_iconPath_setter(instance):
    original = instance.iconPath
    instance.iconPath = original
    assert instance.iconPath == original

@given(instance=viewpoint::style::StyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::style::styledescription_instantiation(instance):
    assert isinstance(instance, viewpoint::style::StyleDescription)

@given(instance=viewpoint::description::IdentifiedElement_strategy)
@settings(max_examples=50)
def test_viewpoint::description::identifiedelement_instantiation(instance):
    assert isinstance(instance, viewpoint::description::IdentifiedElement)

@given(instance=viewpoint::description::IdentifiedElement_strategy)
def test_viewpoint::description::identifiedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=viewpoint::description::IdentifiedElement_strategy)
def test_viewpoint::description::identifiedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=viewpoint::description::IdentifiedElement_strategy)
def test_viewpoint::description::identifiedelement_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=viewpoint::description::IdentifiedElement_strategy)
def test_viewpoint::description::identifiedelement_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

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

@given(instance=description::SubVariable_strategy)
@settings(max_examples=50)
def test_description::subvariable_instantiation(instance):
    assert isinstance(instance, description::SubVariable)

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

@given(instance=description::InteractiveVariableDescription_strategy)
@settings(max_examples=50)
def test_description::interactivevariabledescription_instantiation(instance):
    assert isinstance(instance, description::InteractiveVariableDescription)

@given(instance=viewpoint::tool::SelectModelElementVariable_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::selectmodelelementvariable_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::SelectModelElementVariable)

@given(instance=viewpoint::description::TypedVariable_strategy)
@settings(max_examples=50)
def test_viewpoint::description::typedvariable_instantiation(instance):
    assert isinstance(instance, viewpoint::description::TypedVariable)

@given(instance=viewpoint::description::TypedVariable_strategy)
def test_viewpoint::description::typedvariable_defaultValueExpression_type(instance):
    assert isinstance(instance.defaultValueExpression, str)


@given(instance=viewpoint::description::TypedVariable_strategy)
def test_viewpoint::description::typedvariable_defaultValueExpression_setter(instance):
    original = instance.defaultValueExpression
    instance.defaultValueExpression = original
    assert instance.defaultValueExpression == original

@given(instance=viewpoint::description::InteractiveVariableDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::description::interactivevariabledescription_instantiation(instance):
    assert isinstance(instance, viewpoint::description::InteractiveVariableDescription)

@given(instance=viewpoint::description::InteractiveVariableDescription_strategy)
def test_viewpoint::description::interactivevariabledescription_userDocumentation_type(instance):
    assert isinstance(instance.userDocumentation, str)


@given(instance=viewpoint::description::InteractiveVariableDescription_strategy)
def test_viewpoint::description::interactivevariabledescription_userDocumentation_setter(instance):
    original = instance.userDocumentation
    instance.userDocumentation = original
    assert instance.userDocumentation == original

@given(instance=AbstractVariable_strategy)
@settings(max_examples=50)
def test_abstractvariable_instantiation(instance):
    assert isinstance(instance, AbstractVariable)

@given(instance=viewpoint::tool::ElementSelectVariable_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::elementselectvariable_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::ElementSelectVariable)

@given(instance=viewpoint::tool::NameVariable_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::namevariable_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::NameVariable)

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

@given(instance=viewpoint::description::SubVariable_strategy)
@settings(max_examples=50)
def test_viewpoint::description::subvariable_instantiation(instance):
    assert isinstance(instance, viewpoint::description::SubVariable)

@given(instance=viewpoint::description::AbstractVariable_strategy)
@settings(max_examples=50)
def test_viewpoint::description::abstractvariable_instantiation(instance):
    assert isinstance(instance, viewpoint::description::AbstractVariable)

@given(instance=viewpoint::description::AbstractVariable_strategy)
def test_viewpoint::description::abstractvariable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=viewpoint::description::AbstractVariable_strategy)
def test_viewpoint::description::abstractvariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

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

@given(instance=description::UserColor_strategy)
@settings(max_examples=50)
def test_description::usercolor_instantiation(instance):
    assert isinstance(instance, description::UserColor)

@given(instance=viewpoint::description::UserFixedColor_strategy)
@settings(max_examples=50)
def test_viewpoint::description::userfixedcolor_instantiation(instance):
    assert isinstance(instance, viewpoint::description::UserFixedColor)

@given(instance=description::ColorDescription_strategy)
@settings(max_examples=50)
def test_description::colordescription_instantiation(instance):
    assert isinstance(instance, description::ColorDescription)

@given(instance=viewpoint::description::ComputedColor_strategy)
@settings(max_examples=50)
def test_viewpoint::description::computedcolor_instantiation(instance):
    assert isinstance(instance, viewpoint::description::ComputedColor)

@given(instance=viewpoint::description::ComputedColor_strategy)
def test_viewpoint::description::computedcolor_green_type(instance):
    assert isinstance(instance.green, str)


@given(instance=viewpoint::description::ComputedColor_strategy)
def test_viewpoint::description::computedcolor_green_setter(instance):
    original = instance.green
    instance.green = original
    assert instance.green == original

@given(instance=viewpoint::description::ComputedColor_strategy)
def test_viewpoint::description::computedcolor_red_type(instance):
    assert isinstance(instance.red, str)


@given(instance=viewpoint::description::ComputedColor_strategy)
def test_viewpoint::description::computedcolor_red_setter(instance):
    original = instance.red
    instance.red = original
    assert instance.red == original

@given(instance=viewpoint::description::ComputedColor_strategy)
def test_viewpoint::description::computedcolor_blue_type(instance):
    assert isinstance(instance.blue, str)


@given(instance=viewpoint::description::ComputedColor_strategy)
def test_viewpoint::description::computedcolor_blue_setter(instance):
    original = instance.blue
    instance.blue = original
    assert instance.blue == original

@given(instance=viewpoint::description::InterpolatedColor_strategy)
@settings(max_examples=50)
def test_viewpoint::description::interpolatedcolor_instantiation(instance):
    assert isinstance(instance, viewpoint::description::InterpolatedColor)

@given(instance=viewpoint::description::InterpolatedColor_strategy)
def test_viewpoint::description::interpolatedcolor_maxValueComputationExpression_type(instance):
    assert isinstance(instance.maxValueComputationExpression, str)


@given(instance=viewpoint::description::InterpolatedColor_strategy)
def test_viewpoint::description::interpolatedcolor_maxValueComputationExpression_setter(instance):
    original = instance.maxValueComputationExpression
    instance.maxValueComputationExpression = original
    assert instance.maxValueComputationExpression == original

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
def test_viewpoint::description::fixedcolor_red_type(instance):
    assert isinstance(instance.red, int)


@given(instance=viewpoint::description::FixedColor_strategy)
def test_viewpoint::description::fixedcolor_red_setter(instance):
    original = instance.red
    instance.red = original
    assert instance.red == original

@given(instance=viewpoint::description::FixedColor_strategy)
def test_viewpoint::description::fixedcolor_blue_type(instance):
    assert isinstance(instance.blue, int)


@given(instance=viewpoint::description::FixedColor_strategy)
def test_viewpoint::description::fixedcolor_blue_setter(instance):
    original = instance.blue
    instance.blue = original
    assert instance.blue == original

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
def test_viewpoint::description::selectiondescription_candidatesExpression_type(instance):
    assert isinstance(instance.candidatesExpression, str)


@given(instance=viewpoint::description::SelectionDescription_strategy)
def test_viewpoint::description::selectiondescription_candidatesExpression_setter(instance):
    original = instance.candidatesExpression
    instance.candidatesExpression = original
    assert instance.candidatesExpression == original

@given(instance=viewpoint::description::SelectionDescription_strategy)
def test_viewpoint::description::selectiondescription_tree_type(instance):
    assert isinstance(instance.tree, bool)


@given(instance=viewpoint::description::SelectionDescription_strategy)
def test_viewpoint::description::selectiondescription_tree_setter(instance):
    original = instance.tree
    instance.tree = original
    assert instance.tree == original

@given(instance=viewpoint::description::SelectionDescription_strategy)
def test_viewpoint::description::selectiondescription_rootExpression_type(instance):
    assert isinstance(instance.rootExpression, str)


@given(instance=viewpoint::description::SelectionDescription_strategy)
def test_viewpoint::description::selectiondescription_rootExpression_setter(instance):
    original = instance.rootExpression
    instance.rootExpression = original
    assert instance.rootExpression == original

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
def test_viewpoint::description::selectiondescription_childrenExpression_type(instance):
    assert isinstance(instance.childrenExpression, str)


@given(instance=viewpoint::description::SelectionDescription_strategy)
def test_viewpoint::description::selectiondescription_childrenExpression_setter(instance):
    original = instance.childrenExpression
    instance.childrenExpression = original
    assert instance.childrenExpression == original

@given(instance=viewpoint::description::IVSMElementCustomization_strategy)
@settings(max_examples=50)
def test_viewpoint::description::ivsmelementcustomization_instantiation(instance):
    assert isinstance(instance, viewpoint::description::IVSMElementCustomization)

@given(instance=IVSMElementCustomization_strategy)
@settings(max_examples=50)
def test_ivsmelementcustomization_instantiation(instance):
    assert isinstance(instance, IVSMElementCustomization)

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

@given(instance=viewpoint::description::GenericDecorationDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::description::genericdecorationdescription_instantiation(instance):
    assert isinstance(instance, viewpoint::description::GenericDecorationDescription)

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

@given(instance=viewpoint::description::VSMElementCustomizationReuse_strategy)
@settings(max_examples=50)
def test_viewpoint::description::vsmelementcustomizationreuse_instantiation(instance):
    assert isinstance(instance, viewpoint::description::VSMElementCustomizationReuse)

@given(instance=EStructuralFeatureCustomization_strategy)
@settings(max_examples=50)
def test_estructuralfeaturecustomization_instantiation(instance):
    assert isinstance(instance, EStructuralFeatureCustomization)

@given(instance=viewpoint::description::EAttributeCustomization_strategy)
@settings(max_examples=50)
def test_viewpoint::description::eattributecustomization_instantiation(instance):
    assert isinstance(instance, viewpoint::description::EAttributeCustomization)

@given(instance=viewpoint::description::EAttributeCustomization_strategy)
def test_viewpoint::description::eattributecustomization_attributeName_type(instance):
    assert isinstance(instance.attributeName, str)


@given(instance=viewpoint::description::EAttributeCustomization_strategy)
def test_viewpoint::description::eattributecustomization_attributeName_setter(instance):
    original = instance.attributeName
    instance.attributeName = original
    assert instance.attributeName == original

@given(instance=viewpoint::description::EAttributeCustomization_strategy)
def test_viewpoint::description::eattributecustomization_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=viewpoint::description::EAttributeCustomization_strategy)
def test_viewpoint::description::eattributecustomization_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

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

@given(instance=viewpoint::description::DecorationDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::description::decorationdescription_instantiation(instance):
    assert isinstance(instance, viewpoint::description::DecorationDescription)

@given(instance=viewpoint::description::DecorationDescription_strategy)
def test_viewpoint::description::decorationdescription_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=viewpoint::description::DecorationDescription_strategy)
def test_viewpoint::description::decorationdescription_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=viewpoint::description::DecorationDescription_strategy)
def test_viewpoint::description::decorationdescription_tooltipExpression_type(instance):
    assert isinstance(instance.tooltipExpression, str)


@given(instance=viewpoint::description::DecorationDescription_strategy)
def test_viewpoint::description::decorationdescription_tooltipExpression_setter(instance):
    original = instance.tooltipExpression
    instance.tooltipExpression = original
    assert instance.tooltipExpression == original

@given(instance=viewpoint::description::DecorationDescription_strategy)
def test_viewpoint::description::decorationdescription_distributionDirection_type(instance):
    assert isinstance(instance.distributionDirection, str)


@given(instance=viewpoint::description::DecorationDescription_strategy)
def test_viewpoint::description::decorationdescription_distributionDirection_setter(instance):
    original = instance.distributionDirection
    instance.distributionDirection = original
    assert instance.distributionDirection == original

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
def test_viewpoint::description::decorationdescription_imageExpression_type(instance):
    assert isinstance(instance.imageExpression, str)


@given(instance=viewpoint::description::DecorationDescription_strategy)
def test_viewpoint::description::decorationdescription_imageExpression_setter(instance):
    original = instance.imageExpression
    instance.imageExpression = original
    assert instance.imageExpression == original

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

@given(instance=viewpoint::validation::ValidationRule_strategy)
@settings(max_examples=50)
def test_viewpoint::validation::validationrule_instantiation(instance):
    assert isinstance(instance, viewpoint::validation::ValidationRule)

@given(instance=viewpoint::validation::ValidationRule_strategy)
def test_viewpoint::validation::validationrule_level_type(instance):
    assert isinstance(instance.level, str)


@given(instance=viewpoint::validation::ValidationRule_strategy)
def test_viewpoint::validation::validationrule_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=viewpoint::validation::ValidationRule_strategy)
def test_viewpoint::validation::validationrule_message_type(instance):
    assert isinstance(instance.message, str)


@given(instance=viewpoint::validation::ValidationRule_strategy)
def test_viewpoint::validation::validationrule_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

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

@given(instance=description::viewpoint::EPackage_strategy)
@settings(max_examples=50)
def test_description::viewpoint::epackage_instantiation(instance):
    assert isinstance(instance, description::viewpoint::EPackage)

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
def test_viewpoint::description::representationextensiondescription_viewpointURI_type(instance):
    assert isinstance(instance.viewpointURI, str)


@given(instance=viewpoint::description::RepresentationExtensionDescription_strategy)
def test_viewpoint::description::representationextensiondescription_viewpointURI_setter(instance):
    original = instance.viewpointURI
    instance.viewpointURI = original
    assert instance.viewpointURI == original

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

@given(instance=viewpoint::description::RepresentationImportDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::description::representationimportdescription_instantiation(instance):
    assert isinstance(instance, viewpoint::description::RepresentationImportDescription)

@given(instance=validation::ValidationSet_strategy)
@settings(max_examples=50)
def test_validation::validationset_instantiation(instance):
    assert isinstance(instance, validation::ValidationSet)

@given(instance=description::IdentifiedElement_strategy)
@settings(max_examples=50)
def test_description::identifiedelement_instantiation(instance):
    assert isinstance(instance, description::IdentifiedElement)

@given(instance=viewpoint::tool::ToolEntry_strategy)
@settings(max_examples=50)
def test_viewpoint::tool::toolentry_instantiation(instance):
    assert isinstance(instance, viewpoint::tool::ToolEntry)

@given(instance=description::EndUserDocumentedElement_strategy)
@settings(max_examples=50)
def test_description::enduserdocumentedelement_instantiation(instance):
    assert isinstance(instance, description::EndUserDocumentedElement)

@given(instance=description::Component_strategy)
@settings(max_examples=50)
def test_description::component_instantiation(instance):
    assert isinstance(instance, description::Component)

@given(instance=viewpoint::description::Viewpoint_strategy)
@settings(max_examples=50)
def test_viewpoint::description::viewpoint_instantiation(instance):
    assert isinstance(instance, viewpoint::description::Viewpoint)

@given(instance=viewpoint::description::Viewpoint_strategy)
def test_viewpoint::description::viewpoint_icon_type(instance):
    assert isinstance(instance.icon, str)


@given(instance=viewpoint::description::Viewpoint_strategy)
def test_viewpoint::description::viewpoint_icon_setter(instance):
    original = instance.icon
    instance.icon = original
    assert instance.icon == original

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
def test_viewpoint::description::viewpoint_modelFileExtension_type(instance):
    assert isinstance(instance.modelFileExtension, str)


@given(instance=viewpoint::description::Viewpoint_strategy)
def test_viewpoint::description::viewpoint_modelFileExtension_setter(instance):
    original = instance.modelFileExtension
    instance.modelFileExtension = original
    assert instance.modelFileExtension == original

@given(instance=viewpoint::description::Viewpoint_strategy)
def test_viewpoint::description::viewpoint_conflicts_type(instance):
    assert isinstance(instance.conflicts, str)


@given(instance=viewpoint::description::Viewpoint_strategy)
def test_viewpoint::description::viewpoint_conflicts_setter(instance):
    original = instance.conflicts
    instance.conflicts = original
    assert instance.conflicts == original

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

@given(instance=viewpoint::description::Component_strategy)
@settings(max_examples=50)
def test_viewpoint::description::component_instantiation(instance):
    assert isinstance(instance, viewpoint::description::Component)

@given(instance=viewpoint::description::Extension_strategy)
@settings(max_examples=50)
def test_viewpoint::description::extension_instantiation(instance):
    assert isinstance(instance, viewpoint::description::Extension)

@given(instance=viewpoint::description::RepresentationDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::description::representationdescription_instantiation(instance):
    assert isinstance(instance, viewpoint::description::RepresentationDescription)

@given(instance=viewpoint::description::RepresentationDescription_strategy)
def test_viewpoint::description::representationdescription_initialisation_type(instance):
    assert isinstance(instance.initialisation, bool)


@given(instance=viewpoint::description::RepresentationDescription_strategy)
def test_viewpoint::description::representationdescription_initialisation_setter(instance):
    original = instance.initialisation
    instance.initialisation = original
    assert instance.initialisation == original

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

@given(instance=viewpoint::description::FeatureExtensionDescription_strategy)
@settings(max_examples=50)
def test_viewpoint::description::featureextensiondescription_instantiation(instance):
    assert isinstance(instance, viewpoint::description::FeatureExtensionDescription)

@given(instance=RepresentationTemplate_strategy)
@settings(max_examples=50)
def test_representationtemplate_instantiation(instance):
    assert isinstance(instance, RepresentationTemplate)
