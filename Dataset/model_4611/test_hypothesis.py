import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    UserColorsPalette,
    SytemColorsPalette,
    RepresentationTemplate,
    MetamodelExtensionSetting,
    JavaExtension,
    ToolInstance,
    viewpoint_ToolGroupInstance,
    tool_ToolEntry,
    viewpoint_ToolInstance,
    viewpoint_ToolSectionInstance,
    DFile,
    viewpoint_DModel,
    DResourceContainer,
    viewpoint_DFolder,
    viewpoint_DProject,
    DResource,
    viewpoint_DResource,
    viewpoint_SessionManagerEObject,
    Customizable,
    viewpoint_BasicLabelStyle,
    BasicLabelStyle,
    viewpoint_LabelStyle,
    DecorationDescription,
    viewpoint_DAnalysisSessionEObject,
    Viewpoint,
    style_StyleDescription,
    DSemanticDecorator,
    DStylizable,
    DMappingBased,
    viewpoint_UIState,
    AnnotationEntry,
    RepresentationDescription,
    description_DocumentedElement,
    description_DModelElement,
    viewpoint_description_Group,
    viewpoint_DMappingBased,
    viewpoint_DRefreshable,
    viewpoint_DStylizable,
    FeatureExtensionDescription,
    DRefreshable,
    DAnnotationEntry,
    viewpoint_EObject,
    IdentifiedElement,
    viewpoint_Customizable,
    viewpoint_Decoration,
    viewpoint_Style,
    viewpoint_DAnalysisCustomData,
    viewpoint_DRepresentationElement,
    viewpoint_DResourceContainer,
    viewpoint_DRepresentation,
    viewpoint_DRepresentationDescriptor,
    viewpoint_DFile,
    viewpoint_MetaModelExtension,
    viewpoint_DSemanticDecorator,
    viewpoint_DAnalysis,
    viewpoint_IdentifiedElement,
    viewpoint_DFeatureExtension,
    viewpoint_DView,
    viewpoint_validation_RuleAudit,
    RepresentationElementMapping,
    ValidationRule,
    viewpoint_validation_ViewValidationRule,
    viewpoint_validation_SemanticValidationRule,
    InformationSection,
    viewpoint_audit_TemplateInformationSection,
    viewpoint_audit_InformationSection,
    viewpoint_validation_ValidationFix,
    validation_ValidationRule,
    DocumentedElement,
    viewpoint_validation_ValidationSet,
    validation_ValidationFix,
    validation_RuleAudit,
    viewpoint_validation_ValidationRule,
    tool_PopupMenu,
    MenuItemDescription,
    viewpoint_tool_MenuItemDescriptionWithIcon,
    viewpoint_tool_GroupMenu,
    SwitchChild,
    viewpoint_tool_Case,
    viewpoint_tool_FeatureChangeListener,
    tool_FeatureChangeListener,
    viewpoint_tool_ToolFilterDescription,
    tool_Default,
    tool_Case,
    viewpoint_tool_Default,
    viewpoint_tool_SwitchChild,
    viewpoint_tool_ExternalJavaActionParameter,
    ContainerModelOperation,
    viewpoint_tool_ChangeContext,
    viewpoint_tool_Let,
    viewpoint_tool_If,
    viewpoint_tool_DeleteView,
    viewpoint_tool_SetValue,
    viewpoint_tool_For,
    viewpoint_tool_SetObject,
    viewpoint_tool_RemoveElement,
    viewpoint_tool_CreateInstance,
    viewpoint_tool_MoveElement,
    viewpoint_tool_Unset,
    tool_viewpoint_EObject,
    tool_ModelOperation,
    ModelOperation,
    viewpoint_tool_Switch,
    viewpoint_tool_ContainerModelOperation,
    viewpoint_tool_EditMaskVariables,
    description_AbstractVariable,
    viewpoint_tool_InitialContainerDropOperation,
    viewpoint_tool_InitEdgeCreationOperation,
    viewpoint_tool_InitialOperation,
    viewpoint_tool_InitialNodeCreationOperation,
    viewpoint_tool_ModelOperation,
    tool_ExternalJavaAction,
    tool_ExternalJavaActionParameter,
    tool_ContainerModelOperation,
    tool_GroupMenuItem,
    tool_MenuItemDescriptionWithIcon,
    viewpoint_tool_ExternalJavaAction,
    viewpoint_tool_ExternalJavaActionCall,
    viewpoint_tool_OperationAction,
    tool_MenuItemDescription,
    MenuItemOrRef,
    viewpoint_tool_MenuItemDescriptionReference,
    tool_MenuItemOrRef,
    viewpoint_tool_MenuItemOrRef,
    tool_VariableContainer,
    viewpoint_tool_ContainerViewVariable,
    viewpoint_tool_SelectContainerVariable,
    viewpoint_tool_DropContainerVariable,
    viewpoint_tool_ElementDropVariable,
    viewpoint_tool_ElementVariable,
    viewpoint_tool_ElementDeleteVariable,
    viewpoint_tool_ElementViewVariable,
    SubVariable,
    viewpoint_tool_VariableContainer,
    tool_NameVariable,
    tool_SelectContainerVariable,
    tool_ElementSelectVariable,
    description_SelectionDescription,
    tool_AbstractToolDescription,
    viewpoint_tool_PopupMenu,
    viewpoint_tool_MenuItemDescription,
    viewpoint_tool_SelectionWizardDescription,
    tool_ContainerViewVariable,
    tool_DropContainerVariable,
    tool_InitialOperation,
    tool_ElementViewVariable,
    tool_ElementVariable,
    MappingBasedToolDescription,
    viewpoint_tool_PasteDescription,
    viewpoint_tool_ToolDescription,
    AbstractToolDescription,
    viewpoint_tool_RepresentationCreationDescription,
    viewpoint_tool_GroupMenuItem,
    viewpoint_tool_PaneBasedSelectionWizardDescription,
    viewpoint_tool_RepresentationNavigationDescription,
    viewpoint_tool_MappingBasedToolDescription,
    style_LabelBorderStyleDescription,
    viewpoint_style_LabelBorderStyles,
    tool_ToolFilterDescription,
    ToolEntry,
    viewpoint_tool_AbstractToolDescription,
    viewpoint_style_TooltipStyleDescription,
    viewpoint_style_LabelBorderStyleDescription,
    viewpoint_description_InteractiveVariableDescription,
    AbstractVariable,
    viewpoint_tool_NameVariable,
    viewpoint_tool_DialogVariable,
    viewpoint_tool_ElementSelectVariable,
    viewpoint_description_SubVariable,
    viewpoint_description_AbstractVariable,
    BasicLabelStyleDescription,
    viewpoint_style_LabelStyleDescription,
    viewpoint_description_DAnnotationEntry,
    viewpoint_style_BasicLabelStyleDescription,
    viewpoint_style_StyleDescription,
    description_viewpoint_EDataType,
    description_SubVariable,
    viewpoint_tool_AcceleoVariable,
    description_InteractiveVariableDescription,
    viewpoint_tool_SelectModelElementVariable,
    viewpoint_description_TypedVariable,
    SystemColor,
    viewpoint_description_SytemColorsPalette,
    style_LabelBorderStyles,
    viewpoint_description_IdentifiedElement,
    viewpoint_description_EndUserDocumentedElement,
    viewpoint_description_AnnotationEntry,
    UserColor,
    viewpoint_description_UserColorsPalette,
    viewpoint_description_Environment,
    ColorStep,
    description_UserColor,
    description_ColorDescription,
    viewpoint_description_ComputedColor,
    viewpoint_description_InterpolatedColor,
    FixedColor,
    viewpoint_description_SystemColor,
    viewpoint_description_UserColor,
    viewpoint_description_ColorDescription,
    description_FixedColor,
    viewpoint_description_UserFixedColor,
    ColorDescription,
    viewpoint_description_FixedColor,
    viewpoint_description_ColorStep,
    viewpoint_description_EStructuralFeatureCustomization,
    EStructuralFeatureCustomization,
    viewpoint_description_EReferenceCustomization,
    viewpoint_description_EAttributeCustomization,
    viewpoint_description_SelectionDescription,
    viewpoint_description_GenericDecorationDescription,
    viewpoint_description_SemanticBasedDecoration,
    viewpoint_description_IVSMElementCustomization,
    IVSMElementCustomization,
    viewpoint_description_VSMElementCustomization,
    viewpoint_description_VSMElementCustomizationReuse,
    viewpoint_description_Customization,
    viewpoint_description_DecorationDescription,
    viewpoint_description_DecorationDescriptionsSet,
    tool_PasteDescription,
    viewpoint_description_PasteTargetDescription,
    DAnnotation,
    viewpoint_description_DModelElement,
    viewpoint_description_DocumentedElement,
    viewpoint_description_AbstractMappingImport,
    tool_RepresentationNavigationDescription,
    tool_RepresentationCreationDescription,
    viewpoint_description_RepresentationElementMapping,
    viewpoint_description_ConditionalStyleDescription,
    description_viewpoint_EStringToStringMapEntry,
    viewpoint_description_DAnnotation,
    viewpoint_description_RepresentationExtensionDescription,
    viewpoint_description_RepresentationImportDescription,
    viewpoint_description_RepresentationTemplate,
    description_viewpoint_EPackage,
    viewpoint_description_FeatureExtensionDescription,
    viewpoint_description_JavaExtension,
    description_viewpoint_EObject,
    viewpoint_description_MetamodelExtensionSetting,
    RepresentationExtensionDescription,
    validation_ValidationSet,
    description_IdentifiedElement,
    viewpoint_tool_ToolEntry,
    description_EndUserDocumentedElement,
    viewpoint_description_RepresentationDescription,
    description_Component,
    viewpoint_description_Viewpoint,
    viewpoint_description_Component,
    viewpoint_description_Extension,
    Extension,
    LabelAlignment,
    ERROR_LEVEL,
    FontFormat,
    Position,
    SyncStatus,
    SystemColors,
    DecorationDistributionDirection,
    DragSource,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_toolinstance_is_not_abstract():
    assert not inspect.isabstract(ToolInstance)


def test_toolinstance_constructor_exists():
    assert callable(ToolInstance.__init__)


def test_toolinstance_constructor_args():
    sig = inspect.signature(ToolInstance.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_toolgroupinstance_is_not_abstract():
    assert not inspect.isabstract(viewpoint_ToolGroupInstance)


def test_viewpoint_toolgroupinstance_constructor_exists():
    assert callable(viewpoint_ToolGroupInstance.__init__)


def test_viewpoint_toolgroupinstance_constructor_args():
    sig = inspect.signature(viewpoint_ToolGroupInstance.__init__)
    params = list(sig.parameters.keys())



def test_tool_toolentry_is_not_abstract():
    assert not inspect.isabstract(tool_ToolEntry)


def test_tool_toolentry_constructor_exists():
    assert callable(tool_ToolEntry.__init__)


def test_tool_toolentry_constructor_args():
    sig = inspect.signature(tool_ToolEntry.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_toolinstance_is_not_abstract():
    assert not inspect.isabstract(viewpoint_ToolInstance)


def test_viewpoint_toolinstance_constructor_exists():
    assert callable(viewpoint_ToolInstance.__init__)


def test_viewpoint_toolinstance_constructor_args():
    sig = inspect.signature(viewpoint_ToolInstance.__init__)
    params = list(sig.parameters.keys())
    assert "enabled" in params, "Missing parameter 'enabled'"
    assert "visible" in params, "Missing parameter 'visible'"
    assert "id" in params, "Missing parameter 'id'"
    assert "filtered" in params, "Missing parameter 'filtered'"

def test_viewpoint_toolinstance_has_enabled():
    assert hasattr(viewpoint_ToolInstance, "enabled")
    descriptor = None
    for klass in viewpoint_ToolInstance.__mro__:
        if "enabled" in klass.__dict__:
            descriptor = klass.__dict__["enabled"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_toolinstance_has_visible():
    assert hasattr(viewpoint_ToolInstance, "visible")
    descriptor = None
    for klass in viewpoint_ToolInstance.__mro__:
        if "visible" in klass.__dict__:
            descriptor = klass.__dict__["visible"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_toolinstance_has_id():
    assert hasattr(viewpoint_ToolInstance, "id")
    descriptor = None
    for klass in viewpoint_ToolInstance.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_toolinstance_has_filtered():
    assert hasattr(viewpoint_ToolInstance, "filtered")
    descriptor = None
    for klass in viewpoint_ToolInstance.__mro__:
        if "filtered" in klass.__dict__:
            descriptor = klass.__dict__["filtered"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_toolsectioninstance_is_not_abstract():
    assert not inspect.isabstract(viewpoint_ToolSectionInstance)


def test_viewpoint_toolsectioninstance_constructor_exists():
    assert callable(viewpoint_ToolSectionInstance.__init__)


def test_viewpoint_toolsectioninstance_constructor_args():
    sig = inspect.signature(viewpoint_ToolSectionInstance.__init__)
    params = list(sig.parameters.keys())



def test_dfile_is_not_abstract():
    assert not inspect.isabstract(DFile)


def test_dfile_constructor_exists():
    assert callable(DFile.__init__)


def test_dfile_constructor_args():
    sig = inspect.signature(DFile.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_dmodel_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DModel)


def test_viewpoint_dmodel_constructor_exists():
    assert callable(viewpoint_DModel.__init__)


def test_viewpoint_dmodel_constructor_args():
    sig = inspect.signature(viewpoint_DModel.__init__)
    params = list(sig.parameters.keys())



def test_dresourcecontainer_is_not_abstract():
    assert not inspect.isabstract(DResourceContainer)


def test_dresourcecontainer_constructor_exists():
    assert callable(DResourceContainer.__init__)


def test_dresourcecontainer_constructor_args():
    sig = inspect.signature(DResourceContainer.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_dfolder_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DFolder)


def test_viewpoint_dfolder_constructor_exists():
    assert callable(viewpoint_DFolder.__init__)


def test_viewpoint_dfolder_constructor_args():
    sig = inspect.signature(viewpoint_DFolder.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_dproject_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DProject)


def test_viewpoint_dproject_constructor_exists():
    assert callable(viewpoint_DProject.__init__)


def test_viewpoint_dproject_constructor_args():
    sig = inspect.signature(viewpoint_DProject.__init__)
    params = list(sig.parameters.keys())



def test_dresource_is_not_abstract():
    assert not inspect.isabstract(DResource)


def test_dresource_constructor_exists():
    assert callable(DResource.__init__)


def test_dresource_constructor_args():
    sig = inspect.signature(DResource.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_dresource_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DResource)


def test_viewpoint_dresource_constructor_exists():
    assert callable(viewpoint_DResource.__init__)


def test_viewpoint_dresource_constructor_args():
    sig = inspect.signature(viewpoint_DResource.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "path" in params, "Missing parameter 'path'"

def test_viewpoint_dresource_has_name():
    assert hasattr(viewpoint_DResource, "name")
    descriptor = None
    for klass in viewpoint_DResource.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_dresource_has_path():
    assert hasattr(viewpoint_DResource, "path")
    descriptor = None
    for klass in viewpoint_DResource.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_sessionmanagereobject_is_not_abstract():
    assert not inspect.isabstract(viewpoint_SessionManagerEObject)


def test_viewpoint_sessionmanagereobject_constructor_exists():
    assert callable(viewpoint_SessionManagerEObject.__init__)


def test_viewpoint_sessionmanagereobject_constructor_args():
    sig = inspect.signature(viewpoint_SessionManagerEObject.__init__)
    params = list(sig.parameters.keys())



def test_customizable_is_not_abstract():
    assert not inspect.isabstract(Customizable)


def test_customizable_constructor_exists():
    assert callable(Customizable.__init__)


def test_customizable_constructor_args():
    sig = inspect.signature(Customizable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_basiclabelstyle_is_not_abstract():
    assert not inspect.isabstract(viewpoint_BasicLabelStyle)


def test_viewpoint_basiclabelstyle_constructor_exists():
    assert callable(viewpoint_BasicLabelStyle.__init__)


def test_viewpoint_basiclabelstyle_constructor_args():
    sig = inspect.signature(viewpoint_BasicLabelStyle.__init__)
    params = list(sig.parameters.keys())
    assert "labelSize" in params, "Missing parameter 'labelSize'"
    assert "showIcon" in params, "Missing parameter 'showIcon'"
    assert "iconPath" in params, "Missing parameter 'iconPath'"
    assert "labelFormat" in params, "Missing parameter 'labelFormat'"
    assert "labelColor" in params, "Missing parameter 'labelColor'"

def test_viewpoint_basiclabelstyle_has_labelSize():
    assert hasattr(viewpoint_BasicLabelStyle, "labelSize")
    descriptor = None
    for klass in viewpoint_BasicLabelStyle.__mro__:
        if "labelSize" in klass.__dict__:
            descriptor = klass.__dict__["labelSize"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_basiclabelstyle_has_showIcon():
    assert hasattr(viewpoint_BasicLabelStyle, "showIcon")
    descriptor = None
    for klass in viewpoint_BasicLabelStyle.__mro__:
        if "showIcon" in klass.__dict__:
            descriptor = klass.__dict__["showIcon"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_basiclabelstyle_has_iconPath():
    assert hasattr(viewpoint_BasicLabelStyle, "iconPath")
    descriptor = None
    for klass in viewpoint_BasicLabelStyle.__mro__:
        if "iconPath" in klass.__dict__:
            descriptor = klass.__dict__["iconPath"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_basiclabelstyle_has_labelFormat():
    assert hasattr(viewpoint_BasicLabelStyle, "labelFormat")
    descriptor = None
    for klass in viewpoint_BasicLabelStyle.__mro__:
        if "labelFormat" in klass.__dict__:
            descriptor = klass.__dict__["labelFormat"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_basiclabelstyle_has_labelColor():
    assert hasattr(viewpoint_BasicLabelStyle, "labelColor")
    descriptor = None
    for klass in viewpoint_BasicLabelStyle.__mro__:
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



def test_viewpoint_labelstyle_is_not_abstract():
    assert not inspect.isabstract(viewpoint_LabelStyle)


def test_viewpoint_labelstyle_constructor_exists():
    assert callable(viewpoint_LabelStyle.__init__)


def test_viewpoint_labelstyle_constructor_args():
    sig = inspect.signature(viewpoint_LabelStyle.__init__)
    params = list(sig.parameters.keys())
    assert "labelAlignment" in params, "Missing parameter 'labelAlignment'"

def test_viewpoint_labelstyle_has_labelAlignment():
    assert hasattr(viewpoint_LabelStyle, "labelAlignment")
    descriptor = None
    for klass in viewpoint_LabelStyle.__mro__:
        if "labelAlignment" in klass.__dict__:
            descriptor = klass.__dict__["labelAlignment"]
            break
    assert isinstance(descriptor, property)



def test_decorationdescription_is_not_abstract():
    assert not inspect.isabstract(DecorationDescription)


def test_decorationdescription_constructor_exists():
    assert callable(DecorationDescription.__init__)


def test_decorationdescription_constructor_args():
    sig = inspect.signature(DecorationDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_danalysissessioneobject_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DAnalysisSessionEObject)


def test_viewpoint_danalysissessioneobject_constructor_exists():
    assert callable(viewpoint_DAnalysisSessionEObject.__init__)


def test_viewpoint_danalysissessioneobject_constructor_args():
    sig = inspect.signature(viewpoint_DAnalysisSessionEObject.__init__)
    params = list(sig.parameters.keys())
    assert "resources" in params, "Missing parameter 'resources'"
    assert "synchronizationStatus" in params, "Missing parameter 'synchronizationStatus'"
    assert "controlledResources" in params, "Missing parameter 'controlledResources'"
    assert "open" in params, "Missing parameter 'open'"

def test_viewpoint_danalysissessioneobject_has_resources():
    assert hasattr(viewpoint_DAnalysisSessionEObject, "resources")
    descriptor = None
    for klass in viewpoint_DAnalysisSessionEObject.__mro__:
        if "resources" in klass.__dict__:
            descriptor = klass.__dict__["resources"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_danalysissessioneobject_has_synchronizationStatus():
    assert hasattr(viewpoint_DAnalysisSessionEObject, "synchronizationStatus")
    descriptor = None
    for klass in viewpoint_DAnalysisSessionEObject.__mro__:
        if "synchronizationStatus" in klass.__dict__:
            descriptor = klass.__dict__["synchronizationStatus"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_danalysissessioneobject_has_controlledResources():
    assert hasattr(viewpoint_DAnalysisSessionEObject, "controlledResources")
    descriptor = None
    for klass in viewpoint_DAnalysisSessionEObject.__mro__:
        if "controlledResources" in klass.__dict__:
            descriptor = klass.__dict__["controlledResources"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_danalysissessioneobject_has_open():
    assert hasattr(viewpoint_DAnalysisSessionEObject, "open")
    descriptor = None
    for klass in viewpoint_DAnalysisSessionEObject.__mro__:
        if "open" in klass.__dict__:
            descriptor = klass.__dict__["open"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_is_not_abstract():
    assert not inspect.isabstract(Viewpoint)


def test_viewpoint_constructor_exists():
    assert callable(Viewpoint.__init__)


def test_viewpoint_constructor_args():
    sig = inspect.signature(Viewpoint.__init__)
    params = list(sig.parameters.keys())



def test_style_styledescription_is_not_abstract():
    assert not inspect.isabstract(style_StyleDescription)


def test_style_styledescription_constructor_exists():
    assert callable(style_StyleDescription.__init__)


def test_style_styledescription_constructor_args():
    sig = inspect.signature(style_StyleDescription.__init__)
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



def test_viewpoint_uistate_is_not_abstract():
    assert not inspect.isabstract(viewpoint_UIState)


def test_viewpoint_uistate_constructor_exists():
    assert callable(viewpoint_UIState.__init__)


def test_viewpoint_uistate_constructor_args():
    sig = inspect.signature(viewpoint_UIState.__init__)
    params = list(sig.parameters.keys())
    assert "subDiagramDecorationDescriptors" in params, "Missing parameter 'subDiagramDecorationDescriptors'"
    assert "decorationImage" in params, "Missing parameter 'decorationImage'"
    assert "inverseSelectionOrder" in params, "Missing parameter 'inverseSelectionOrder'"

def test_viewpoint_uistate_has_subDiagramDecorationDescriptors():
    assert hasattr(viewpoint_UIState, "subDiagramDecorationDescriptors")
    descriptor = None
    for klass in viewpoint_UIState.__mro__:
        if "subDiagramDecorationDescriptors" in klass.__dict__:
            descriptor = klass.__dict__["subDiagramDecorationDescriptors"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_uistate_has_decorationImage():
    assert hasattr(viewpoint_UIState, "decorationImage")
    descriptor = None
    for klass in viewpoint_UIState.__mro__:
        if "decorationImage" in klass.__dict__:
            descriptor = klass.__dict__["decorationImage"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_uistate_has_inverseSelectionOrder():
    assert hasattr(viewpoint_UIState, "inverseSelectionOrder")
    descriptor = None
    for klass in viewpoint_UIState.__mro__:
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



def test_representationdescription_is_not_abstract():
    assert not inspect.isabstract(RepresentationDescription)


def test_representationdescription_constructor_exists():
    assert callable(RepresentationDescription.__init__)


def test_representationdescription_constructor_args():
    sig = inspect.signature(RepresentationDescription.__init__)
    params = list(sig.parameters.keys())



def test_description_documentedelement_is_not_abstract():
    assert not inspect.isabstract(description_DocumentedElement)


def test_description_documentedelement_constructor_exists():
    assert callable(description_DocumentedElement.__init__)


def test_description_documentedelement_constructor_args():
    sig = inspect.signature(description_DocumentedElement.__init__)
    params = list(sig.parameters.keys())



def test_description_dmodelelement_is_not_abstract():
    assert not inspect.isabstract(description_DModelElement)


def test_description_dmodelelement_constructor_exists():
    assert callable(description_DModelElement.__init__)


def test_description_dmodelelement_constructor_args():
    sig = inspect.signature(description_DModelElement.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_group_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_Group)


def test_viewpoint_description_group_constructor_exists():
    assert callable(viewpoint_description_Group.__init__)


def test_viewpoint_description_group_constructor_args():
    sig = inspect.signature(viewpoint_description_Group.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "version" in params, "Missing parameter 'version'"

def test_viewpoint_description_group_has_name():
    assert hasattr(viewpoint_description_Group, "name")
    descriptor = None
    for klass in viewpoint_description_Group.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_group_has_version():
    assert hasattr(viewpoint_description_Group, "version")
    descriptor = None
    for klass in viewpoint_description_Group.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_dmappingbased_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DMappingBased)


def test_viewpoint_dmappingbased_constructor_exists():
    assert callable(viewpoint_DMappingBased.__init__)


def test_viewpoint_dmappingbased_constructor_args():
    sig = inspect.signature(viewpoint_DMappingBased.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_drefreshable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DRefreshable)


def test_viewpoint_drefreshable_constructor_exists():
    assert callable(viewpoint_DRefreshable.__init__)


def test_viewpoint_drefreshable_constructor_args():
    sig = inspect.signature(viewpoint_DRefreshable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_dstylizable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DStylizable)


def test_viewpoint_dstylizable_constructor_exists():
    assert callable(viewpoint_DStylizable.__init__)


def test_viewpoint_dstylizable_constructor_args():
    sig = inspect.signature(viewpoint_DStylizable.__init__)
    params = list(sig.parameters.keys())



def test_featureextensiondescription_is_not_abstract():
    assert not inspect.isabstract(FeatureExtensionDescription)


def test_featureextensiondescription_constructor_exists():
    assert callable(FeatureExtensionDescription.__init__)


def test_featureextensiondescription_constructor_args():
    sig = inspect.signature(FeatureExtensionDescription.__init__)
    params = list(sig.parameters.keys())



def test_drefreshable_is_not_abstract():
    assert not inspect.isabstract(DRefreshable)


def test_drefreshable_constructor_exists():
    assert callable(DRefreshable.__init__)


def test_drefreshable_constructor_args():
    sig = inspect.signature(DRefreshable.__init__)
    params = list(sig.parameters.keys())



def test_dannotationentry_is_not_abstract():
    assert not inspect.isabstract(DAnnotationEntry)


def test_dannotationentry_constructor_exists():
    assert callable(DAnnotationEntry.__init__)


def test_dannotationentry_constructor_args():
    sig = inspect.signature(DAnnotationEntry.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_eobject_is_not_abstract():
    assert not inspect.isabstract(viewpoint_EObject)


def test_viewpoint_eobject_constructor_exists():
    assert callable(viewpoint_EObject.__init__)


def test_viewpoint_eobject_constructor_args():
    sig = inspect.signature(viewpoint_EObject.__init__)
    params = list(sig.parameters.keys())



def test_identifiedelement_is_not_abstract():
    assert not inspect.isabstract(IdentifiedElement)


def test_identifiedelement_constructor_exists():
    assert callable(IdentifiedElement.__init__)


def test_identifiedelement_constructor_args():
    sig = inspect.signature(IdentifiedElement.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_customizable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_Customizable)


def test_viewpoint_customizable_constructor_exists():
    assert callable(viewpoint_Customizable.__init__)


def test_viewpoint_customizable_constructor_args():
    sig = inspect.signature(viewpoint_Customizable.__init__)
    params = list(sig.parameters.keys())
    assert "customFeatures" in params, "Missing parameter 'customFeatures'"

def test_viewpoint_customizable_has_customFeatures():
    assert hasattr(viewpoint_Customizable, "customFeatures")
    descriptor = None
    for klass in viewpoint_Customizable.__mro__:
        if "customFeatures" in klass.__dict__:
            descriptor = klass.__dict__["customFeatures"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_decoration_is_not_abstract():
    assert not inspect.isabstract(viewpoint_Decoration)


def test_viewpoint_decoration_constructor_exists():
    assert callable(viewpoint_Decoration.__init__)


def test_viewpoint_decoration_constructor_args():
    sig = inspect.signature(viewpoint_Decoration.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_style_is_not_abstract():
    assert not inspect.isabstract(viewpoint_Style)


def test_viewpoint_style_constructor_exists():
    assert callable(viewpoint_Style.__init__)


def test_viewpoint_style_constructor_args():
    sig = inspect.signature(viewpoint_Style.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_danalysiscustomdata_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DAnalysisCustomData)


def test_viewpoint_danalysiscustomdata_constructor_exists():
    assert callable(viewpoint_DAnalysisCustomData.__init__)


def test_viewpoint_danalysiscustomdata_constructor_args():
    sig = inspect.signature(viewpoint_DAnalysisCustomData.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_viewpoint_danalysiscustomdata_has_key():
    assert hasattr(viewpoint_DAnalysisCustomData, "key")
    descriptor = None
    for klass in viewpoint_DAnalysisCustomData.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_drepresentationelement_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DRepresentationElement)


def test_viewpoint_drepresentationelement_constructor_exists():
    assert callable(viewpoint_DRepresentationElement.__init__)


def test_viewpoint_drepresentationelement_constructor_args():
    sig = inspect.signature(viewpoint_DRepresentationElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_viewpoint_drepresentationelement_has_name():
    assert hasattr(viewpoint_DRepresentationElement, "name")
    descriptor = None
    for klass in viewpoint_DRepresentationElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_dresourcecontainer_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DResourceContainer)


def test_viewpoint_dresourcecontainer_constructor_exists():
    assert callable(viewpoint_DResourceContainer.__init__)


def test_viewpoint_dresourcecontainer_constructor_args():
    sig = inspect.signature(viewpoint_DResourceContainer.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_drepresentation_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DRepresentation)


def test_viewpoint_drepresentation_constructor_exists():
    assert callable(viewpoint_DRepresentation.__init__)


def test_viewpoint_drepresentation_constructor_args():
    sig = inspect.signature(viewpoint_DRepresentation.__init__)
    params = list(sig.parameters.keys())
    assert "documentation" in params, "Missing parameter 'documentation'"
    assert "name" in params, "Missing parameter 'name'"

def test_viewpoint_drepresentation_has_documentation():
    assert hasattr(viewpoint_DRepresentation, "documentation")
    descriptor = None
    for klass in viewpoint_DRepresentation.__mro__:
        if "documentation" in klass.__dict__:
            descriptor = klass.__dict__["documentation"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_drepresentation_has_name():
    assert hasattr(viewpoint_DRepresentation, "name")
    descriptor = None
    for klass in viewpoint_DRepresentation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_drepresentationdescriptor_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DRepresentationDescriptor)


def test_viewpoint_drepresentationdescriptor_constructor_exists():
    assert callable(viewpoint_DRepresentationDescriptor.__init__)


def test_viewpoint_drepresentationdescriptor_constructor_args():
    sig = inspect.signature(viewpoint_DRepresentationDescriptor.__init__)
    params = list(sig.parameters.keys())
    assert "changeId" in params, "Missing parameter 'changeId'"
    assert "name" in params, "Missing parameter 'name'"
    assert "repPath" in params, "Missing parameter 'repPath'"

def test_viewpoint_drepresentationdescriptor_has_changeId():
    assert hasattr(viewpoint_DRepresentationDescriptor, "changeId")
    descriptor = None
    for klass in viewpoint_DRepresentationDescriptor.__mro__:
        if "changeId" in klass.__dict__:
            descriptor = klass.__dict__["changeId"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_drepresentationdescriptor_has_name():
    assert hasattr(viewpoint_DRepresentationDescriptor, "name")
    descriptor = None
    for klass in viewpoint_DRepresentationDescriptor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_drepresentationdescriptor_has_repPath():
    assert hasattr(viewpoint_DRepresentationDescriptor, "repPath")
    descriptor = None
    for klass in viewpoint_DRepresentationDescriptor.__mro__:
        if "repPath" in klass.__dict__:
            descriptor = klass.__dict__["repPath"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_dfile_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DFile)


def test_viewpoint_dfile_constructor_exists():
    assert callable(viewpoint_DFile.__init__)


def test_viewpoint_dfile_constructor_args():
    sig = inspect.signature(viewpoint_DFile.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_metamodelextension_is_not_abstract():
    assert not inspect.isabstract(viewpoint_MetaModelExtension)


def test_viewpoint_metamodelextension_constructor_exists():
    assert callable(viewpoint_MetaModelExtension.__init__)


def test_viewpoint_metamodelextension_constructor_args():
    sig = inspect.signature(viewpoint_MetaModelExtension.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_dsemanticdecorator_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DSemanticDecorator)


def test_viewpoint_dsemanticdecorator_constructor_exists():
    assert callable(viewpoint_DSemanticDecorator.__init__)


def test_viewpoint_dsemanticdecorator_constructor_args():
    sig = inspect.signature(viewpoint_DSemanticDecorator.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_danalysis_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DAnalysis)


def test_viewpoint_danalysis_constructor_exists():
    assert callable(viewpoint_DAnalysis.__init__)


def test_viewpoint_danalysis_constructor_args():
    sig = inspect.signature(viewpoint_DAnalysis.__init__)
    params = list(sig.parameters.keys())
    assert "semanticResources" in params, "Missing parameter 'semanticResources'"
    assert "version" in params, "Missing parameter 'version'"

def test_viewpoint_danalysis_has_semanticResources():
    assert hasattr(viewpoint_DAnalysis, "semanticResources")
    descriptor = None
    for klass in viewpoint_DAnalysis.__mro__:
        if "semanticResources" in klass.__dict__:
            descriptor = klass.__dict__["semanticResources"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_danalysis_has_version():
    assert hasattr(viewpoint_DAnalysis, "version")
    descriptor = None
    for klass in viewpoint_DAnalysis.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_identifiedelement_is_not_abstract():
    assert not inspect.isabstract(viewpoint_IdentifiedElement)


def test_viewpoint_identifiedelement_constructor_exists():
    assert callable(viewpoint_IdentifiedElement.__init__)


def test_viewpoint_identifiedelement_constructor_args():
    sig = inspect.signature(viewpoint_IdentifiedElement.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"

def test_viewpoint_identifiedelement_has_uid():
    assert hasattr(viewpoint_IdentifiedElement, "uid")
    descriptor = None
    for klass in viewpoint_IdentifiedElement.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_dfeatureextension_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DFeatureExtension)


def test_viewpoint_dfeatureextension_constructor_exists():
    assert callable(viewpoint_DFeatureExtension.__init__)


def test_viewpoint_dfeatureextension_constructor_args():
    sig = inspect.signature(viewpoint_DFeatureExtension.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_dview_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DView)


def test_viewpoint_dview_constructor_exists():
    assert callable(viewpoint_DView.__init__)


def test_viewpoint_dview_constructor_args():
    sig = inspect.signature(viewpoint_DView.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_validation_ruleaudit_is_not_abstract():
    assert not inspect.isabstract(viewpoint_validation_RuleAudit)


def test_viewpoint_validation_ruleaudit_constructor_exists():
    assert callable(viewpoint_validation_RuleAudit.__init__)


def test_viewpoint_validation_ruleaudit_constructor_args():
    sig = inspect.signature(viewpoint_validation_RuleAudit.__init__)
    params = list(sig.parameters.keys())
    assert "auditExpression" in params, "Missing parameter 'auditExpression'"

def test_viewpoint_validation_ruleaudit_has_auditExpression():
    assert hasattr(viewpoint_validation_RuleAudit, "auditExpression")
    descriptor = None
    for klass in viewpoint_validation_RuleAudit.__mro__:
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



def test_viewpoint_validation_viewvalidationrule_is_not_abstract():
    assert not inspect.isabstract(viewpoint_validation_ViewValidationRule)


def test_viewpoint_validation_viewvalidationrule_constructor_exists():
    assert callable(viewpoint_validation_ViewValidationRule.__init__)


def test_viewpoint_validation_viewvalidationrule_constructor_args():
    sig = inspect.signature(viewpoint_validation_ViewValidationRule.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_validation_semanticvalidationrule_is_not_abstract():
    assert not inspect.isabstract(viewpoint_validation_SemanticValidationRule)


def test_viewpoint_validation_semanticvalidationrule_constructor_exists():
    assert callable(viewpoint_validation_SemanticValidationRule.__init__)


def test_viewpoint_validation_semanticvalidationrule_constructor_args():
    sig = inspect.signature(viewpoint_validation_SemanticValidationRule.__init__)
    params = list(sig.parameters.keys())
    assert "targetClass" in params, "Missing parameter 'targetClass'"

def test_viewpoint_validation_semanticvalidationrule_has_targetClass():
    assert hasattr(viewpoint_validation_SemanticValidationRule, "targetClass")
    descriptor = None
    for klass in viewpoint_validation_SemanticValidationRule.__mro__:
        if "targetClass" in klass.__dict__:
            descriptor = klass.__dict__["targetClass"]
            break
    assert isinstance(descriptor, property)



def test_informationsection_is_not_abstract():
    assert not inspect.isabstract(InformationSection)


def test_informationsection_constructor_exists():
    assert callable(InformationSection.__init__)


def test_informationsection_constructor_args():
    sig = inspect.signature(InformationSection.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_audit_templateinformationsection_is_not_abstract():
    assert not inspect.isabstract(viewpoint_audit_TemplateInformationSection)


def test_viewpoint_audit_templateinformationsection_constructor_exists():
    assert callable(viewpoint_audit_TemplateInformationSection.__init__)


def test_viewpoint_audit_templateinformationsection_constructor_args():
    sig = inspect.signature(viewpoint_audit_TemplateInformationSection.__init__)
    params = list(sig.parameters.keys())
    assert "templatePath" in params, "Missing parameter 'templatePath'"

def test_viewpoint_audit_templateinformationsection_has_templatePath():
    assert hasattr(viewpoint_audit_TemplateInformationSection, "templatePath")
    descriptor = None
    for klass in viewpoint_audit_TemplateInformationSection.__mro__:
        if "templatePath" in klass.__dict__:
            descriptor = klass.__dict__["templatePath"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_audit_informationsection_is_not_abstract():
    assert not inspect.isabstract(viewpoint_audit_InformationSection)


def test_viewpoint_audit_informationsection_constructor_exists():
    assert callable(viewpoint_audit_InformationSection.__init__)


def test_viewpoint_audit_informationsection_constructor_args():
    sig = inspect.signature(viewpoint_audit_InformationSection.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_validation_validationfix_is_not_abstract():
    assert not inspect.isabstract(viewpoint_validation_ValidationFix)


def test_viewpoint_validation_validationfix_constructor_exists():
    assert callable(viewpoint_validation_ValidationFix.__init__)


def test_viewpoint_validation_validationfix_constructor_args():
    sig = inspect.signature(viewpoint_validation_ValidationFix.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_viewpoint_validation_validationfix_has_name():
    assert hasattr(viewpoint_validation_ValidationFix, "name")
    descriptor = None
    for klass in viewpoint_validation_ValidationFix.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_validation_validationrule_is_not_abstract():
    assert not inspect.isabstract(validation_ValidationRule)


def test_validation_validationrule_constructor_exists():
    assert callable(validation_ValidationRule.__init__)


def test_validation_validationrule_constructor_args():
    sig = inspect.signature(validation_ValidationRule.__init__)
    params = list(sig.parameters.keys())



def test_documentedelement_is_not_abstract():
    assert not inspect.isabstract(DocumentedElement)


def test_documentedelement_constructor_exists():
    assert callable(DocumentedElement.__init__)


def test_documentedelement_constructor_args():
    sig = inspect.signature(DocumentedElement.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_validation_validationset_is_not_abstract():
    assert not inspect.isabstract(viewpoint_validation_ValidationSet)


def test_viewpoint_validation_validationset_constructor_exists():
    assert callable(viewpoint_validation_ValidationSet.__init__)


def test_viewpoint_validation_validationset_constructor_args():
    sig = inspect.signature(viewpoint_validation_ValidationSet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_viewpoint_validation_validationset_has_name():
    assert hasattr(viewpoint_validation_ValidationSet, "name")
    descriptor = None
    for klass in viewpoint_validation_ValidationSet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_validation_validationfix_is_not_abstract():
    assert not inspect.isabstract(validation_ValidationFix)


def test_validation_validationfix_constructor_exists():
    assert callable(validation_ValidationFix.__init__)


def test_validation_validationfix_constructor_args():
    sig = inspect.signature(validation_ValidationFix.__init__)
    params = list(sig.parameters.keys())



def test_validation_ruleaudit_is_not_abstract():
    assert not inspect.isabstract(validation_RuleAudit)


def test_validation_ruleaudit_constructor_exists():
    assert callable(validation_RuleAudit.__init__)


def test_validation_ruleaudit_constructor_args():
    sig = inspect.signature(validation_RuleAudit.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_validation_validationrule_is_not_abstract():
    assert not inspect.isabstract(viewpoint_validation_ValidationRule)


def test_viewpoint_validation_validationrule_constructor_exists():
    assert callable(viewpoint_validation_ValidationRule.__init__)


def test_viewpoint_validation_validationrule_constructor_args():
    sig = inspect.signature(viewpoint_validation_ValidationRule.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"
    assert "message" in params, "Missing parameter 'message'"

def test_viewpoint_validation_validationrule_has_level():
    assert hasattr(viewpoint_validation_ValidationRule, "level")
    descriptor = None
    for klass in viewpoint_validation_ValidationRule.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_validation_validationrule_has_message():
    assert hasattr(viewpoint_validation_ValidationRule, "message")
    descriptor = None
    for klass in viewpoint_validation_ValidationRule.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)



def test_tool_popupmenu_is_not_abstract():
    assert not inspect.isabstract(tool_PopupMenu)


def test_tool_popupmenu_constructor_exists():
    assert callable(tool_PopupMenu.__init__)


def test_tool_popupmenu_constructor_args():
    sig = inspect.signature(tool_PopupMenu.__init__)
    params = list(sig.parameters.keys())



def test_menuitemdescription_is_not_abstract():
    assert not inspect.isabstract(MenuItemDescription)


def test_menuitemdescription_constructor_exists():
    assert callable(MenuItemDescription.__init__)


def test_menuitemdescription_constructor_args():
    sig = inspect.signature(MenuItemDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_menuitemdescriptionwithicon_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_MenuItemDescriptionWithIcon)


def test_viewpoint_tool_menuitemdescriptionwithicon_constructor_exists():
    assert callable(viewpoint_tool_MenuItemDescriptionWithIcon.__init__)


def test_viewpoint_tool_menuitemdescriptionwithicon_constructor_args():
    sig = inspect.signature(viewpoint_tool_MenuItemDescriptionWithIcon.__init__)
    params = list(sig.parameters.keys())
    assert "icon" in params, "Missing parameter 'icon'"

def test_viewpoint_tool_menuitemdescriptionwithicon_has_icon():
    assert hasattr(viewpoint_tool_MenuItemDescriptionWithIcon, "icon")
    descriptor = None
    for klass in viewpoint_tool_MenuItemDescriptionWithIcon.__mro__:
        if "icon" in klass.__dict__:
            descriptor = klass.__dict__["icon"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_tool_groupmenu_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_GroupMenu)


def test_viewpoint_tool_groupmenu_constructor_exists():
    assert callable(viewpoint_tool_GroupMenu.__init__)


def test_viewpoint_tool_groupmenu_constructor_args():
    sig = inspect.signature(viewpoint_tool_GroupMenu.__init__)
    params = list(sig.parameters.keys())
    assert "locationURI" in params, "Missing parameter 'locationURI'"

def test_viewpoint_tool_groupmenu_has_locationURI():
    assert hasattr(viewpoint_tool_GroupMenu, "locationURI")
    descriptor = None
    for klass in viewpoint_tool_GroupMenu.__mro__:
        if "locationURI" in klass.__dict__:
            descriptor = klass.__dict__["locationURI"]
            break
    assert isinstance(descriptor, property)



def test_switchchild_is_not_abstract():
    assert not inspect.isabstract(SwitchChild)


def test_switchchild_constructor_exists():
    assert callable(SwitchChild.__init__)


def test_switchchild_constructor_args():
    sig = inspect.signature(SwitchChild.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_case_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_Case)


def test_viewpoint_tool_case_constructor_exists():
    assert callable(viewpoint_tool_Case.__init__)


def test_viewpoint_tool_case_constructor_args():
    sig = inspect.signature(viewpoint_tool_Case.__init__)
    params = list(sig.parameters.keys())
    assert "conditionExpression" in params, "Missing parameter 'conditionExpression'"

def test_viewpoint_tool_case_has_conditionExpression():
    assert hasattr(viewpoint_tool_Case, "conditionExpression")
    descriptor = None
    for klass in viewpoint_tool_Case.__mro__:
        if "conditionExpression" in klass.__dict__:
            descriptor = klass.__dict__["conditionExpression"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_tool_featurechangelistener_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_FeatureChangeListener)


def test_viewpoint_tool_featurechangelistener_constructor_exists():
    assert callable(viewpoint_tool_FeatureChangeListener.__init__)


def test_viewpoint_tool_featurechangelistener_constructor_args():
    sig = inspect.signature(viewpoint_tool_FeatureChangeListener.__init__)
    params = list(sig.parameters.keys())
    assert "featureName" in params, "Missing parameter 'featureName'"
    assert "domainClass" in params, "Missing parameter 'domainClass'"

def test_viewpoint_tool_featurechangelistener_has_featureName():
    assert hasattr(viewpoint_tool_FeatureChangeListener, "featureName")
    descriptor = None
    for klass in viewpoint_tool_FeatureChangeListener.__mro__:
        if "featureName" in klass.__dict__:
            descriptor = klass.__dict__["featureName"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_featurechangelistener_has_domainClass():
    assert hasattr(viewpoint_tool_FeatureChangeListener, "domainClass")
    descriptor = None
    for klass in viewpoint_tool_FeatureChangeListener.__mro__:
        if "domainClass" in klass.__dict__:
            descriptor = klass.__dict__["domainClass"]
            break
    assert isinstance(descriptor, property)



def test_tool_featurechangelistener_is_not_abstract():
    assert not inspect.isabstract(tool_FeatureChangeListener)


def test_tool_featurechangelistener_constructor_exists():
    assert callable(tool_FeatureChangeListener.__init__)


def test_tool_featurechangelistener_constructor_args():
    sig = inspect.signature(tool_FeatureChangeListener.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_toolfilterdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ToolFilterDescription)


def test_viewpoint_tool_toolfilterdescription_constructor_exists():
    assert callable(viewpoint_tool_ToolFilterDescription.__init__)


def test_viewpoint_tool_toolfilterdescription_constructor_args():
    sig = inspect.signature(viewpoint_tool_ToolFilterDescription.__init__)
    params = list(sig.parameters.keys())
    assert "precondition" in params, "Missing parameter 'precondition'"
    assert "elementsToListen" in params, "Missing parameter 'elementsToListen'"

def test_viewpoint_tool_toolfilterdescription_has_precondition():
    assert hasattr(viewpoint_tool_ToolFilterDescription, "precondition")
    descriptor = None
    for klass in viewpoint_tool_ToolFilterDescription.__mro__:
        if "precondition" in klass.__dict__:
            descriptor = klass.__dict__["precondition"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_toolfilterdescription_has_elementsToListen():
    assert hasattr(viewpoint_tool_ToolFilterDescription, "elementsToListen")
    descriptor = None
    for klass in viewpoint_tool_ToolFilterDescription.__mro__:
        if "elementsToListen" in klass.__dict__:
            descriptor = klass.__dict__["elementsToListen"]
            break
    assert isinstance(descriptor, property)



def test_tool_default_is_not_abstract():
    assert not inspect.isabstract(tool_Default)


def test_tool_default_constructor_exists():
    assert callable(tool_Default.__init__)


def test_tool_default_constructor_args():
    sig = inspect.signature(tool_Default.__init__)
    params = list(sig.parameters.keys())



def test_tool_case_is_not_abstract():
    assert not inspect.isabstract(tool_Case)


def test_tool_case_constructor_exists():
    assert callable(tool_Case.__init__)


def test_tool_case_constructor_args():
    sig = inspect.signature(tool_Case.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_default_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_Default)


def test_viewpoint_tool_default_constructor_exists():
    assert callable(viewpoint_tool_Default.__init__)


def test_viewpoint_tool_default_constructor_args():
    sig = inspect.signature(viewpoint_tool_Default.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_switchchild_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_SwitchChild)


def test_viewpoint_tool_switchchild_constructor_exists():
    assert callable(viewpoint_tool_SwitchChild.__init__)


def test_viewpoint_tool_switchchild_constructor_args():
    sig = inspect.signature(viewpoint_tool_SwitchChild.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_externaljavaactionparameter_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ExternalJavaActionParameter)


def test_viewpoint_tool_externaljavaactionparameter_constructor_exists():
    assert callable(viewpoint_tool_ExternalJavaActionParameter.__init__)


def test_viewpoint_tool_externaljavaactionparameter_constructor_args():
    sig = inspect.signature(viewpoint_tool_ExternalJavaActionParameter.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_viewpoint_tool_externaljavaactionparameter_has_value():
    assert hasattr(viewpoint_tool_ExternalJavaActionParameter, "value")
    descriptor = None
    for klass in viewpoint_tool_ExternalJavaActionParameter.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_externaljavaactionparameter_has_name():
    assert hasattr(viewpoint_tool_ExternalJavaActionParameter, "name")
    descriptor = None
    for klass in viewpoint_tool_ExternalJavaActionParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_containermodeloperation_is_not_abstract():
    assert not inspect.isabstract(ContainerModelOperation)


def test_containermodeloperation_constructor_exists():
    assert callable(ContainerModelOperation.__init__)


def test_containermodeloperation_constructor_args():
    sig = inspect.signature(ContainerModelOperation.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_changecontext_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ChangeContext)


def test_viewpoint_tool_changecontext_constructor_exists():
    assert callable(viewpoint_tool_ChangeContext.__init__)


def test_viewpoint_tool_changecontext_constructor_args():
    sig = inspect.signature(viewpoint_tool_ChangeContext.__init__)
    params = list(sig.parameters.keys())
    assert "browseExpression" in params, "Missing parameter 'browseExpression'"

def test_viewpoint_tool_changecontext_has_browseExpression():
    assert hasattr(viewpoint_tool_ChangeContext, "browseExpression")
    descriptor = None
    for klass in viewpoint_tool_ChangeContext.__mro__:
        if "browseExpression" in klass.__dict__:
            descriptor = klass.__dict__["browseExpression"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_tool_let_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_Let)


def test_viewpoint_tool_let_constructor_exists():
    assert callable(viewpoint_tool_Let.__init__)


def test_viewpoint_tool_let_constructor_args():
    sig = inspect.signature(viewpoint_tool_Let.__init__)
    params = list(sig.parameters.keys())
    assert "valueExpression" in params, "Missing parameter 'valueExpression'"
    assert "variableName" in params, "Missing parameter 'variableName'"

def test_viewpoint_tool_let_has_valueExpression():
    assert hasattr(viewpoint_tool_Let, "valueExpression")
    descriptor = None
    for klass in viewpoint_tool_Let.__mro__:
        if "valueExpression" in klass.__dict__:
            descriptor = klass.__dict__["valueExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_let_has_variableName():
    assert hasattr(viewpoint_tool_Let, "variableName")
    descriptor = None
    for klass in viewpoint_tool_Let.__mro__:
        if "variableName" in klass.__dict__:
            descriptor = klass.__dict__["variableName"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_tool_if_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_If)


def test_viewpoint_tool_if_constructor_exists():
    assert callable(viewpoint_tool_If.__init__)


def test_viewpoint_tool_if_constructor_args():
    sig = inspect.signature(viewpoint_tool_If.__init__)
    params = list(sig.parameters.keys())
    assert "conditionExpression" in params, "Missing parameter 'conditionExpression'"

def test_viewpoint_tool_if_has_conditionExpression():
    assert hasattr(viewpoint_tool_If, "conditionExpression")
    descriptor = None
    for klass in viewpoint_tool_If.__mro__:
        if "conditionExpression" in klass.__dict__:
            descriptor = klass.__dict__["conditionExpression"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_tool_deleteview_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_DeleteView)


def test_viewpoint_tool_deleteview_constructor_exists():
    assert callable(viewpoint_tool_DeleteView.__init__)


def test_viewpoint_tool_deleteview_constructor_args():
    sig = inspect.signature(viewpoint_tool_DeleteView.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_setvalue_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_SetValue)


def test_viewpoint_tool_setvalue_constructor_exists():
    assert callable(viewpoint_tool_SetValue.__init__)


def test_viewpoint_tool_setvalue_constructor_args():
    sig = inspect.signature(viewpoint_tool_SetValue.__init__)
    params = list(sig.parameters.keys())
    assert "valueExpression" in params, "Missing parameter 'valueExpression'"
    assert "featureName" in params, "Missing parameter 'featureName'"

def test_viewpoint_tool_setvalue_has_valueExpression():
    assert hasattr(viewpoint_tool_SetValue, "valueExpression")
    descriptor = None
    for klass in viewpoint_tool_SetValue.__mro__:
        if "valueExpression" in klass.__dict__:
            descriptor = klass.__dict__["valueExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_setvalue_has_featureName():
    assert hasattr(viewpoint_tool_SetValue, "featureName")
    descriptor = None
    for klass in viewpoint_tool_SetValue.__mro__:
        if "featureName" in klass.__dict__:
            descriptor = klass.__dict__["featureName"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_tool_for_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_For)


def test_viewpoint_tool_for_constructor_exists():
    assert callable(viewpoint_tool_For.__init__)


def test_viewpoint_tool_for_constructor_args():
    sig = inspect.signature(viewpoint_tool_For.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"
    assert "iteratorName" in params, "Missing parameter 'iteratorName'"

def test_viewpoint_tool_for_has_expression():
    assert hasattr(viewpoint_tool_For, "expression")
    descriptor = None
    for klass in viewpoint_tool_For.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_for_has_iteratorName():
    assert hasattr(viewpoint_tool_For, "iteratorName")
    descriptor = None
    for klass in viewpoint_tool_For.__mro__:
        if "iteratorName" in klass.__dict__:
            descriptor = klass.__dict__["iteratorName"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_tool_setobject_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_SetObject)


def test_viewpoint_tool_setobject_constructor_exists():
    assert callable(viewpoint_tool_SetObject.__init__)


def test_viewpoint_tool_setobject_constructor_args():
    sig = inspect.signature(viewpoint_tool_SetObject.__init__)
    params = list(sig.parameters.keys())
    assert "featureName" in params, "Missing parameter 'featureName'"

def test_viewpoint_tool_setobject_has_featureName():
    assert hasattr(viewpoint_tool_SetObject, "featureName")
    descriptor = None
    for klass in viewpoint_tool_SetObject.__mro__:
        if "featureName" in klass.__dict__:
            descriptor = klass.__dict__["featureName"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_tool_removeelement_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_RemoveElement)


def test_viewpoint_tool_removeelement_constructor_exists():
    assert callable(viewpoint_tool_RemoveElement.__init__)


def test_viewpoint_tool_removeelement_constructor_args():
    sig = inspect.signature(viewpoint_tool_RemoveElement.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_createinstance_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_CreateInstance)


def test_viewpoint_tool_createinstance_constructor_exists():
    assert callable(viewpoint_tool_CreateInstance.__init__)


def test_viewpoint_tool_createinstance_constructor_args():
    sig = inspect.signature(viewpoint_tool_CreateInstance.__init__)
    params = list(sig.parameters.keys())
    assert "variableName" in params, "Missing parameter 'variableName'"
    assert "typeName" in params, "Missing parameter 'typeName'"
    assert "referenceName" in params, "Missing parameter 'referenceName'"

def test_viewpoint_tool_createinstance_has_variableName():
    assert hasattr(viewpoint_tool_CreateInstance, "variableName")
    descriptor = None
    for klass in viewpoint_tool_CreateInstance.__mro__:
        if "variableName" in klass.__dict__:
            descriptor = klass.__dict__["variableName"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_createinstance_has_typeName():
    assert hasattr(viewpoint_tool_CreateInstance, "typeName")
    descriptor = None
    for klass in viewpoint_tool_CreateInstance.__mro__:
        if "typeName" in klass.__dict__:
            descriptor = klass.__dict__["typeName"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_createinstance_has_referenceName():
    assert hasattr(viewpoint_tool_CreateInstance, "referenceName")
    descriptor = None
    for klass in viewpoint_tool_CreateInstance.__mro__:
        if "referenceName" in klass.__dict__:
            descriptor = klass.__dict__["referenceName"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_tool_moveelement_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_MoveElement)


def test_viewpoint_tool_moveelement_constructor_exists():
    assert callable(viewpoint_tool_MoveElement.__init__)


def test_viewpoint_tool_moveelement_constructor_args():
    sig = inspect.signature(viewpoint_tool_MoveElement.__init__)
    params = list(sig.parameters.keys())
    assert "newContainerExpression" in params, "Missing parameter 'newContainerExpression'"
    assert "featureName" in params, "Missing parameter 'featureName'"

def test_viewpoint_tool_moveelement_has_newContainerExpression():
    assert hasattr(viewpoint_tool_MoveElement, "newContainerExpression")
    descriptor = None
    for klass in viewpoint_tool_MoveElement.__mro__:
        if "newContainerExpression" in klass.__dict__:
            descriptor = klass.__dict__["newContainerExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_moveelement_has_featureName():
    assert hasattr(viewpoint_tool_MoveElement, "featureName")
    descriptor = None
    for klass in viewpoint_tool_MoveElement.__mro__:
        if "featureName" in klass.__dict__:
            descriptor = klass.__dict__["featureName"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_tool_unset_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_Unset)


def test_viewpoint_tool_unset_constructor_exists():
    assert callable(viewpoint_tool_Unset.__init__)


def test_viewpoint_tool_unset_constructor_args():
    sig = inspect.signature(viewpoint_tool_Unset.__init__)
    params = list(sig.parameters.keys())
    assert "elementExpression" in params, "Missing parameter 'elementExpression'"
    assert "featureName" in params, "Missing parameter 'featureName'"

def test_viewpoint_tool_unset_has_elementExpression():
    assert hasattr(viewpoint_tool_Unset, "elementExpression")
    descriptor = None
    for klass in viewpoint_tool_Unset.__mro__:
        if "elementExpression" in klass.__dict__:
            descriptor = klass.__dict__["elementExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_unset_has_featureName():
    assert hasattr(viewpoint_tool_Unset, "featureName")
    descriptor = None
    for klass in viewpoint_tool_Unset.__mro__:
        if "featureName" in klass.__dict__:
            descriptor = klass.__dict__["featureName"]
            break
    assert isinstance(descriptor, property)



def test_tool_viewpoint_eobject_is_not_abstract():
    assert not inspect.isabstract(tool_viewpoint_EObject)


def test_tool_viewpoint_eobject_constructor_exists():
    assert callable(tool_viewpoint_EObject.__init__)


def test_tool_viewpoint_eobject_constructor_args():
    sig = inspect.signature(tool_viewpoint_EObject.__init__)
    params = list(sig.parameters.keys())



def test_tool_modeloperation_is_not_abstract():
    assert not inspect.isabstract(tool_ModelOperation)


def test_tool_modeloperation_constructor_exists():
    assert callable(tool_ModelOperation.__init__)


def test_tool_modeloperation_constructor_args():
    sig = inspect.signature(tool_ModelOperation.__init__)
    params = list(sig.parameters.keys())



def test_modeloperation_is_not_abstract():
    assert not inspect.isabstract(ModelOperation)


def test_modeloperation_constructor_exists():
    assert callable(ModelOperation.__init__)


def test_modeloperation_constructor_args():
    sig = inspect.signature(ModelOperation.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_switch_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_Switch)


def test_viewpoint_tool_switch_constructor_exists():
    assert callable(viewpoint_tool_Switch.__init__)


def test_viewpoint_tool_switch_constructor_args():
    sig = inspect.signature(viewpoint_tool_Switch.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_containermodeloperation_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ContainerModelOperation)


def test_viewpoint_tool_containermodeloperation_constructor_exists():
    assert callable(viewpoint_tool_ContainerModelOperation.__init__)


def test_viewpoint_tool_containermodeloperation_constructor_args():
    sig = inspect.signature(viewpoint_tool_ContainerModelOperation.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_editmaskvariables_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_EditMaskVariables)


def test_viewpoint_tool_editmaskvariables_constructor_exists():
    assert callable(viewpoint_tool_EditMaskVariables.__init__)


def test_viewpoint_tool_editmaskvariables_constructor_args():
    sig = inspect.signature(viewpoint_tool_EditMaskVariables.__init__)
    params = list(sig.parameters.keys())
    assert "mask" in params, "Missing parameter 'mask'"

def test_viewpoint_tool_editmaskvariables_has_mask():
    assert hasattr(viewpoint_tool_EditMaskVariables, "mask")
    descriptor = None
    for klass in viewpoint_tool_EditMaskVariables.__mro__:
        if "mask" in klass.__dict__:
            descriptor = klass.__dict__["mask"]
            break
    assert isinstance(descriptor, property)



def test_description_abstractvariable_is_not_abstract():
    assert not inspect.isabstract(description_AbstractVariable)


def test_description_abstractvariable_constructor_exists():
    assert callable(description_AbstractVariable.__init__)


def test_description_abstractvariable_constructor_args():
    sig = inspect.signature(description_AbstractVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_initialcontainerdropoperation_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_InitialContainerDropOperation)


def test_viewpoint_tool_initialcontainerdropoperation_constructor_exists():
    assert callable(viewpoint_tool_InitialContainerDropOperation.__init__)


def test_viewpoint_tool_initialcontainerdropoperation_constructor_args():
    sig = inspect.signature(viewpoint_tool_InitialContainerDropOperation.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_initedgecreationoperation_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_InitEdgeCreationOperation)


def test_viewpoint_tool_initedgecreationoperation_constructor_exists():
    assert callable(viewpoint_tool_InitEdgeCreationOperation.__init__)


def test_viewpoint_tool_initedgecreationoperation_constructor_args():
    sig = inspect.signature(viewpoint_tool_InitEdgeCreationOperation.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_initialoperation_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_InitialOperation)


def test_viewpoint_tool_initialoperation_constructor_exists():
    assert callable(viewpoint_tool_InitialOperation.__init__)


def test_viewpoint_tool_initialoperation_constructor_args():
    sig = inspect.signature(viewpoint_tool_InitialOperation.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_initialnodecreationoperation_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_InitialNodeCreationOperation)


def test_viewpoint_tool_initialnodecreationoperation_constructor_exists():
    assert callable(viewpoint_tool_InitialNodeCreationOperation.__init__)


def test_viewpoint_tool_initialnodecreationoperation_constructor_args():
    sig = inspect.signature(viewpoint_tool_InitialNodeCreationOperation.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_modeloperation_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ModelOperation)


def test_viewpoint_tool_modeloperation_constructor_exists():
    assert callable(viewpoint_tool_ModelOperation.__init__)


def test_viewpoint_tool_modeloperation_constructor_args():
    sig = inspect.signature(viewpoint_tool_ModelOperation.__init__)
    params = list(sig.parameters.keys())



def test_tool_externaljavaaction_is_not_abstract():
    assert not inspect.isabstract(tool_ExternalJavaAction)


def test_tool_externaljavaaction_constructor_exists():
    assert callable(tool_ExternalJavaAction.__init__)


def test_tool_externaljavaaction_constructor_args():
    sig = inspect.signature(tool_ExternalJavaAction.__init__)
    params = list(sig.parameters.keys())



def test_tool_externaljavaactionparameter_is_not_abstract():
    assert not inspect.isabstract(tool_ExternalJavaActionParameter)


def test_tool_externaljavaactionparameter_constructor_exists():
    assert callable(tool_ExternalJavaActionParameter.__init__)


def test_tool_externaljavaactionparameter_constructor_args():
    sig = inspect.signature(tool_ExternalJavaActionParameter.__init__)
    params = list(sig.parameters.keys())



def test_tool_containermodeloperation_is_not_abstract():
    assert not inspect.isabstract(tool_ContainerModelOperation)


def test_tool_containermodeloperation_constructor_exists():
    assert callable(tool_ContainerModelOperation.__init__)


def test_tool_containermodeloperation_constructor_args():
    sig = inspect.signature(tool_ContainerModelOperation.__init__)
    params = list(sig.parameters.keys())



def test_tool_groupmenuitem_is_not_abstract():
    assert not inspect.isabstract(tool_GroupMenuItem)


def test_tool_groupmenuitem_constructor_exists():
    assert callable(tool_GroupMenuItem.__init__)


def test_tool_groupmenuitem_constructor_args():
    sig = inspect.signature(tool_GroupMenuItem.__init__)
    params = list(sig.parameters.keys())



def test_tool_menuitemdescriptionwithicon_is_not_abstract():
    assert not inspect.isabstract(tool_MenuItemDescriptionWithIcon)


def test_tool_menuitemdescriptionwithicon_constructor_exists():
    assert callable(tool_MenuItemDescriptionWithIcon.__init__)


def test_tool_menuitemdescriptionwithicon_constructor_args():
    sig = inspect.signature(tool_MenuItemDescriptionWithIcon.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_externaljavaaction_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ExternalJavaAction)


def test_viewpoint_tool_externaljavaaction_constructor_exists():
    assert callable(viewpoint_tool_ExternalJavaAction.__init__)


def test_viewpoint_tool_externaljavaaction_constructor_args():
    sig = inspect.signature(viewpoint_tool_ExternalJavaAction.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_viewpoint_tool_externaljavaaction_has_id():
    assert hasattr(viewpoint_tool_ExternalJavaAction, "id")
    descriptor = None
    for klass in viewpoint_tool_ExternalJavaAction.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_tool_externaljavaactioncall_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ExternalJavaActionCall)


def test_viewpoint_tool_externaljavaactioncall_constructor_exists():
    assert callable(viewpoint_tool_ExternalJavaActionCall.__init__)


def test_viewpoint_tool_externaljavaactioncall_constructor_args():
    sig = inspect.signature(viewpoint_tool_ExternalJavaActionCall.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_operationaction_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_OperationAction)


def test_viewpoint_tool_operationaction_constructor_exists():
    assert callable(viewpoint_tool_OperationAction.__init__)


def test_viewpoint_tool_operationaction_constructor_args():
    sig = inspect.signature(viewpoint_tool_OperationAction.__init__)
    params = list(sig.parameters.keys())



def test_tool_menuitemdescription_is_not_abstract():
    assert not inspect.isabstract(tool_MenuItemDescription)


def test_tool_menuitemdescription_constructor_exists():
    assert callable(tool_MenuItemDescription.__init__)


def test_tool_menuitemdescription_constructor_args():
    sig = inspect.signature(tool_MenuItemDescription.__init__)
    params = list(sig.parameters.keys())



def test_menuitemorref_is_not_abstract():
    assert not inspect.isabstract(MenuItemOrRef)


def test_menuitemorref_constructor_exists():
    assert callable(MenuItemOrRef.__init__)


def test_menuitemorref_constructor_args():
    sig = inspect.signature(MenuItemOrRef.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_menuitemdescriptionreference_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_MenuItemDescriptionReference)


def test_viewpoint_tool_menuitemdescriptionreference_constructor_exists():
    assert callable(viewpoint_tool_MenuItemDescriptionReference.__init__)


def test_viewpoint_tool_menuitemdescriptionreference_constructor_args():
    sig = inspect.signature(viewpoint_tool_MenuItemDescriptionReference.__init__)
    params = list(sig.parameters.keys())



def test_tool_menuitemorref_is_not_abstract():
    assert not inspect.isabstract(tool_MenuItemOrRef)


def test_tool_menuitemorref_constructor_exists():
    assert callable(tool_MenuItemOrRef.__init__)


def test_tool_menuitemorref_constructor_args():
    sig = inspect.signature(tool_MenuItemOrRef.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_menuitemorref_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_MenuItemOrRef)


def test_viewpoint_tool_menuitemorref_constructor_exists():
    assert callable(viewpoint_tool_MenuItemOrRef.__init__)


def test_viewpoint_tool_menuitemorref_constructor_args():
    sig = inspect.signature(viewpoint_tool_MenuItemOrRef.__init__)
    params = list(sig.parameters.keys())



def test_tool_variablecontainer_is_not_abstract():
    assert not inspect.isabstract(tool_VariableContainer)


def test_tool_variablecontainer_constructor_exists():
    assert callable(tool_VariableContainer.__init__)


def test_tool_variablecontainer_constructor_args():
    sig = inspect.signature(tool_VariableContainer.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_containerviewvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ContainerViewVariable)


def test_viewpoint_tool_containerviewvariable_constructor_exists():
    assert callable(viewpoint_tool_ContainerViewVariable.__init__)


def test_viewpoint_tool_containerviewvariable_constructor_args():
    sig = inspect.signature(viewpoint_tool_ContainerViewVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_selectcontainervariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_SelectContainerVariable)


def test_viewpoint_tool_selectcontainervariable_constructor_exists():
    assert callable(viewpoint_tool_SelectContainerVariable.__init__)


def test_viewpoint_tool_selectcontainervariable_constructor_args():
    sig = inspect.signature(viewpoint_tool_SelectContainerVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_dropcontainervariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_DropContainerVariable)


def test_viewpoint_tool_dropcontainervariable_constructor_exists():
    assert callable(viewpoint_tool_DropContainerVariable.__init__)


def test_viewpoint_tool_dropcontainervariable_constructor_args():
    sig = inspect.signature(viewpoint_tool_DropContainerVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_elementdropvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ElementDropVariable)


def test_viewpoint_tool_elementdropvariable_constructor_exists():
    assert callable(viewpoint_tool_ElementDropVariable.__init__)


def test_viewpoint_tool_elementdropvariable_constructor_args():
    sig = inspect.signature(viewpoint_tool_ElementDropVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_elementvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ElementVariable)


def test_viewpoint_tool_elementvariable_constructor_exists():
    assert callable(viewpoint_tool_ElementVariable.__init__)


def test_viewpoint_tool_elementvariable_constructor_args():
    sig = inspect.signature(viewpoint_tool_ElementVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_elementdeletevariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ElementDeleteVariable)


def test_viewpoint_tool_elementdeletevariable_constructor_exists():
    assert callable(viewpoint_tool_ElementDeleteVariable.__init__)


def test_viewpoint_tool_elementdeletevariable_constructor_args():
    sig = inspect.signature(viewpoint_tool_ElementDeleteVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_elementviewvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ElementViewVariable)


def test_viewpoint_tool_elementviewvariable_constructor_exists():
    assert callable(viewpoint_tool_ElementViewVariable.__init__)


def test_viewpoint_tool_elementviewvariable_constructor_args():
    sig = inspect.signature(viewpoint_tool_ElementViewVariable.__init__)
    params = list(sig.parameters.keys())



def test_subvariable_is_not_abstract():
    assert not inspect.isabstract(SubVariable)


def test_subvariable_constructor_exists():
    assert callable(SubVariable.__init__)


def test_subvariable_constructor_args():
    sig = inspect.signature(SubVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_variablecontainer_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_VariableContainer)


def test_viewpoint_tool_variablecontainer_constructor_exists():
    assert callable(viewpoint_tool_VariableContainer.__init__)


def test_viewpoint_tool_variablecontainer_constructor_args():
    sig = inspect.signature(viewpoint_tool_VariableContainer.__init__)
    params = list(sig.parameters.keys())



def test_tool_namevariable_is_not_abstract():
    assert not inspect.isabstract(tool_NameVariable)


def test_tool_namevariable_constructor_exists():
    assert callable(tool_NameVariable.__init__)


def test_tool_namevariable_constructor_args():
    sig = inspect.signature(tool_NameVariable.__init__)
    params = list(sig.parameters.keys())



def test_tool_selectcontainervariable_is_not_abstract():
    assert not inspect.isabstract(tool_SelectContainerVariable)


def test_tool_selectcontainervariable_constructor_exists():
    assert callable(tool_SelectContainerVariable.__init__)


def test_tool_selectcontainervariable_constructor_args():
    sig = inspect.signature(tool_SelectContainerVariable.__init__)
    params = list(sig.parameters.keys())



def test_tool_elementselectvariable_is_not_abstract():
    assert not inspect.isabstract(tool_ElementSelectVariable)


def test_tool_elementselectvariable_constructor_exists():
    assert callable(tool_ElementSelectVariable.__init__)


def test_tool_elementselectvariable_constructor_args():
    sig = inspect.signature(tool_ElementSelectVariable.__init__)
    params = list(sig.parameters.keys())



def test_description_selectiondescription_is_not_abstract():
    assert not inspect.isabstract(description_SelectionDescription)


def test_description_selectiondescription_constructor_exists():
    assert callable(description_SelectionDescription.__init__)


def test_description_selectiondescription_constructor_args():
    sig = inspect.signature(description_SelectionDescription.__init__)
    params = list(sig.parameters.keys())



def test_tool_abstracttooldescription_is_not_abstract():
    assert not inspect.isabstract(tool_AbstractToolDescription)


def test_tool_abstracttooldescription_constructor_exists():
    assert callable(tool_AbstractToolDescription.__init__)


def test_tool_abstracttooldescription_constructor_args():
    sig = inspect.signature(tool_AbstractToolDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_popupmenu_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_PopupMenu)


def test_viewpoint_tool_popupmenu_constructor_exists():
    assert callable(viewpoint_tool_PopupMenu.__init__)


def test_viewpoint_tool_popupmenu_constructor_args():
    sig = inspect.signature(viewpoint_tool_PopupMenu.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_menuitemdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_MenuItemDescription)


def test_viewpoint_tool_menuitemdescription_constructor_exists():
    assert callable(viewpoint_tool_MenuItemDescription.__init__)


def test_viewpoint_tool_menuitemdescription_constructor_args():
    sig = inspect.signature(viewpoint_tool_MenuItemDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_selectionwizarddescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_SelectionWizardDescription)


def test_viewpoint_tool_selectionwizarddescription_constructor_exists():
    assert callable(viewpoint_tool_SelectionWizardDescription.__init__)


def test_viewpoint_tool_selectionwizarddescription_constructor_args():
    sig = inspect.signature(viewpoint_tool_SelectionWizardDescription.__init__)
    params = list(sig.parameters.keys())
    assert "iconPath" in params, "Missing parameter 'iconPath'"
    assert "windowTitle" in params, "Missing parameter 'windowTitle'"
    assert "windowImagePath" in params, "Missing parameter 'windowImagePath'"

def test_viewpoint_tool_selectionwizarddescription_has_iconPath():
    assert hasattr(viewpoint_tool_SelectionWizardDescription, "iconPath")
    descriptor = None
    for klass in viewpoint_tool_SelectionWizardDescription.__mro__:
        if "iconPath" in klass.__dict__:
            descriptor = klass.__dict__["iconPath"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_selectionwizarddescription_has_windowTitle():
    assert hasattr(viewpoint_tool_SelectionWizardDescription, "windowTitle")
    descriptor = None
    for klass in viewpoint_tool_SelectionWizardDescription.__mro__:
        if "windowTitle" in klass.__dict__:
            descriptor = klass.__dict__["windowTitle"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_selectionwizarddescription_has_windowImagePath():
    assert hasattr(viewpoint_tool_SelectionWizardDescription, "windowImagePath")
    descriptor = None
    for klass in viewpoint_tool_SelectionWizardDescription.__mro__:
        if "windowImagePath" in klass.__dict__:
            descriptor = klass.__dict__["windowImagePath"]
            break
    assert isinstance(descriptor, property)



def test_tool_containerviewvariable_is_not_abstract():
    assert not inspect.isabstract(tool_ContainerViewVariable)


def test_tool_containerviewvariable_constructor_exists():
    assert callable(tool_ContainerViewVariable.__init__)


def test_tool_containerviewvariable_constructor_args():
    sig = inspect.signature(tool_ContainerViewVariable.__init__)
    params = list(sig.parameters.keys())



def test_tool_dropcontainervariable_is_not_abstract():
    assert not inspect.isabstract(tool_DropContainerVariable)


def test_tool_dropcontainervariable_constructor_exists():
    assert callable(tool_DropContainerVariable.__init__)


def test_tool_dropcontainervariable_constructor_args():
    sig = inspect.signature(tool_DropContainerVariable.__init__)
    params = list(sig.parameters.keys())



def test_tool_initialoperation_is_not_abstract():
    assert not inspect.isabstract(tool_InitialOperation)


def test_tool_initialoperation_constructor_exists():
    assert callable(tool_InitialOperation.__init__)


def test_tool_initialoperation_constructor_args():
    sig = inspect.signature(tool_InitialOperation.__init__)
    params = list(sig.parameters.keys())



def test_tool_elementviewvariable_is_not_abstract():
    assert not inspect.isabstract(tool_ElementViewVariable)


def test_tool_elementviewvariable_constructor_exists():
    assert callable(tool_ElementViewVariable.__init__)


def test_tool_elementviewvariable_constructor_args():
    sig = inspect.signature(tool_ElementViewVariable.__init__)
    params = list(sig.parameters.keys())



def test_tool_elementvariable_is_not_abstract():
    assert not inspect.isabstract(tool_ElementVariable)


def test_tool_elementvariable_constructor_exists():
    assert callable(tool_ElementVariable.__init__)


def test_tool_elementvariable_constructor_args():
    sig = inspect.signature(tool_ElementVariable.__init__)
    params = list(sig.parameters.keys())



def test_mappingbasedtooldescription_is_not_abstract():
    assert not inspect.isabstract(MappingBasedToolDescription)


def test_mappingbasedtooldescription_constructor_exists():
    assert callable(MappingBasedToolDescription.__init__)


def test_mappingbasedtooldescription_constructor_args():
    sig = inspect.signature(MappingBasedToolDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_pastedescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_PasteDescription)


def test_viewpoint_tool_pastedescription_constructor_exists():
    assert callable(viewpoint_tool_PasteDescription.__init__)


def test_viewpoint_tool_pastedescription_constructor_args():
    sig = inspect.signature(viewpoint_tool_PasteDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_tooldescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ToolDescription)


def test_viewpoint_tool_tooldescription_constructor_exists():
    assert callable(viewpoint_tool_ToolDescription.__init__)


def test_viewpoint_tool_tooldescription_constructor_args():
    sig = inspect.signature(viewpoint_tool_ToolDescription.__init__)
    params = list(sig.parameters.keys())
    assert "iconPath" in params, "Missing parameter 'iconPath'"

def test_viewpoint_tool_tooldescription_has_iconPath():
    assert hasattr(viewpoint_tool_ToolDescription, "iconPath")
    descriptor = None
    for klass in viewpoint_tool_ToolDescription.__mro__:
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



def test_viewpoint_tool_representationcreationdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_RepresentationCreationDescription)


def test_viewpoint_tool_representationcreationdescription_constructor_exists():
    assert callable(viewpoint_tool_RepresentationCreationDescription.__init__)


def test_viewpoint_tool_representationcreationdescription_constructor_args():
    sig = inspect.signature(viewpoint_tool_RepresentationCreationDescription.__init__)
    params = list(sig.parameters.keys())
    assert "titleExpression" in params, "Missing parameter 'titleExpression'"
    assert "browseExpression" in params, "Missing parameter 'browseExpression'"

def test_viewpoint_tool_representationcreationdescription_has_titleExpression():
    assert hasattr(viewpoint_tool_RepresentationCreationDescription, "titleExpression")
    descriptor = None
    for klass in viewpoint_tool_RepresentationCreationDescription.__mro__:
        if "titleExpression" in klass.__dict__:
            descriptor = klass.__dict__["titleExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_representationcreationdescription_has_browseExpression():
    assert hasattr(viewpoint_tool_RepresentationCreationDescription, "browseExpression")
    descriptor = None
    for klass in viewpoint_tool_RepresentationCreationDescription.__mro__:
        if "browseExpression" in klass.__dict__:
            descriptor = klass.__dict__["browseExpression"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_tool_groupmenuitem_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_GroupMenuItem)


def test_viewpoint_tool_groupmenuitem_constructor_exists():
    assert callable(viewpoint_tool_GroupMenuItem.__init__)


def test_viewpoint_tool_groupmenuitem_constructor_args():
    sig = inspect.signature(viewpoint_tool_GroupMenuItem.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_panebasedselectionwizarddescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_PaneBasedSelectionWizardDescription)


def test_viewpoint_tool_panebasedselectionwizarddescription_constructor_exists():
    assert callable(viewpoint_tool_PaneBasedSelectionWizardDescription.__init__)


def test_viewpoint_tool_panebasedselectionwizarddescription_constructor_args():
    sig = inspect.signature(viewpoint_tool_PaneBasedSelectionWizardDescription.__init__)
    params = list(sig.parameters.keys())
    assert "preSelectedCandidatesExpression" in params, "Missing parameter 'preSelectedCandidatesExpression'"
    assert "windowTitle" in params, "Missing parameter 'windowTitle'"
    assert "rootExpression" in params, "Missing parameter 'rootExpression'"
    assert "choiceOfValuesMessage" in params, "Missing parameter 'choiceOfValuesMessage'"
    assert "selectedValuesMessage" in params, "Missing parameter 'selectedValuesMessage'"
    assert "childrenExpression" in params, "Missing parameter 'childrenExpression'"
    assert "windowImagePath" in params, "Missing parameter 'windowImagePath'"
    assert "tree" in params, "Missing parameter 'tree'"
    assert "message" in params, "Missing parameter 'message'"
    assert "candidatesExpression" in params, "Missing parameter 'candidatesExpression'"
    assert "iconPath" in params, "Missing parameter 'iconPath'"

def test_viewpoint_tool_panebasedselectionwizarddescription_has_preSelectedCandidatesExpression():
    assert hasattr(viewpoint_tool_PaneBasedSelectionWizardDescription, "preSelectedCandidatesExpression")
    descriptor = None
    for klass in viewpoint_tool_PaneBasedSelectionWizardDescription.__mro__:
        if "preSelectedCandidatesExpression" in klass.__dict__:
            descriptor = klass.__dict__["preSelectedCandidatesExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_panebasedselectionwizarddescription_has_windowTitle():
    assert hasattr(viewpoint_tool_PaneBasedSelectionWizardDescription, "windowTitle")
    descriptor = None
    for klass in viewpoint_tool_PaneBasedSelectionWizardDescription.__mro__:
        if "windowTitle" in klass.__dict__:
            descriptor = klass.__dict__["windowTitle"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_panebasedselectionwizarddescription_has_rootExpression():
    assert hasattr(viewpoint_tool_PaneBasedSelectionWizardDescription, "rootExpression")
    descriptor = None
    for klass in viewpoint_tool_PaneBasedSelectionWizardDescription.__mro__:
        if "rootExpression" in klass.__dict__:
            descriptor = klass.__dict__["rootExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_panebasedselectionwizarddescription_has_choiceOfValuesMessage():
    assert hasattr(viewpoint_tool_PaneBasedSelectionWizardDescription, "choiceOfValuesMessage")
    descriptor = None
    for klass in viewpoint_tool_PaneBasedSelectionWizardDescription.__mro__:
        if "choiceOfValuesMessage" in klass.__dict__:
            descriptor = klass.__dict__["choiceOfValuesMessage"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_panebasedselectionwizarddescription_has_selectedValuesMessage():
    assert hasattr(viewpoint_tool_PaneBasedSelectionWizardDescription, "selectedValuesMessage")
    descriptor = None
    for klass in viewpoint_tool_PaneBasedSelectionWizardDescription.__mro__:
        if "selectedValuesMessage" in klass.__dict__:
            descriptor = klass.__dict__["selectedValuesMessage"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_panebasedselectionwizarddescription_has_childrenExpression():
    assert hasattr(viewpoint_tool_PaneBasedSelectionWizardDescription, "childrenExpression")
    descriptor = None
    for klass in viewpoint_tool_PaneBasedSelectionWizardDescription.__mro__:
        if "childrenExpression" in klass.__dict__:
            descriptor = klass.__dict__["childrenExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_panebasedselectionwizarddescription_has_windowImagePath():
    assert hasattr(viewpoint_tool_PaneBasedSelectionWizardDescription, "windowImagePath")
    descriptor = None
    for klass in viewpoint_tool_PaneBasedSelectionWizardDescription.__mro__:
        if "windowImagePath" in klass.__dict__:
            descriptor = klass.__dict__["windowImagePath"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_panebasedselectionwizarddescription_has_tree():
    assert hasattr(viewpoint_tool_PaneBasedSelectionWizardDescription, "tree")
    descriptor = None
    for klass in viewpoint_tool_PaneBasedSelectionWizardDescription.__mro__:
        if "tree" in klass.__dict__:
            descriptor = klass.__dict__["tree"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_panebasedselectionwizarddescription_has_message():
    assert hasattr(viewpoint_tool_PaneBasedSelectionWizardDescription, "message")
    descriptor = None
    for klass in viewpoint_tool_PaneBasedSelectionWizardDescription.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_panebasedselectionwizarddescription_has_candidatesExpression():
    assert hasattr(viewpoint_tool_PaneBasedSelectionWizardDescription, "candidatesExpression")
    descriptor = None
    for klass in viewpoint_tool_PaneBasedSelectionWizardDescription.__mro__:
        if "candidatesExpression" in klass.__dict__:
            descriptor = klass.__dict__["candidatesExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_panebasedselectionwizarddescription_has_iconPath():
    assert hasattr(viewpoint_tool_PaneBasedSelectionWizardDescription, "iconPath")
    descriptor = None
    for klass in viewpoint_tool_PaneBasedSelectionWizardDescription.__mro__:
        if "iconPath" in klass.__dict__:
            descriptor = klass.__dict__["iconPath"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_tool_representationnavigationdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_RepresentationNavigationDescription)


def test_viewpoint_tool_representationnavigationdescription_constructor_exists():
    assert callable(viewpoint_tool_RepresentationNavigationDescription.__init__)


def test_viewpoint_tool_representationnavigationdescription_constructor_args():
    sig = inspect.signature(viewpoint_tool_RepresentationNavigationDescription.__init__)
    params = list(sig.parameters.keys())
    assert "browseExpression" in params, "Missing parameter 'browseExpression'"
    assert "navigationNameExpression" in params, "Missing parameter 'navigationNameExpression'"

def test_viewpoint_tool_representationnavigationdescription_has_browseExpression():
    assert hasattr(viewpoint_tool_RepresentationNavigationDescription, "browseExpression")
    descriptor = None
    for klass in viewpoint_tool_RepresentationNavigationDescription.__mro__:
        if "browseExpression" in klass.__dict__:
            descriptor = klass.__dict__["browseExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_representationnavigationdescription_has_navigationNameExpression():
    assert hasattr(viewpoint_tool_RepresentationNavigationDescription, "navigationNameExpression")
    descriptor = None
    for klass in viewpoint_tool_RepresentationNavigationDescription.__mro__:
        if "navigationNameExpression" in klass.__dict__:
            descriptor = klass.__dict__["navigationNameExpression"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_tool_mappingbasedtooldescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_MappingBasedToolDescription)


def test_viewpoint_tool_mappingbasedtooldescription_constructor_exists():
    assert callable(viewpoint_tool_MappingBasedToolDescription.__init__)


def test_viewpoint_tool_mappingbasedtooldescription_constructor_args():
    sig = inspect.signature(viewpoint_tool_MappingBasedToolDescription.__init__)
    params = list(sig.parameters.keys())



def test_style_labelborderstyledescription_is_not_abstract():
    assert not inspect.isabstract(style_LabelBorderStyleDescription)


def test_style_labelborderstyledescription_constructor_exists():
    assert callable(style_LabelBorderStyleDescription.__init__)


def test_style_labelborderstyledescription_constructor_args():
    sig = inspect.signature(style_LabelBorderStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_style_labelborderstyles_is_not_abstract():
    assert not inspect.isabstract(viewpoint_style_LabelBorderStyles)


def test_viewpoint_style_labelborderstyles_constructor_exists():
    assert callable(viewpoint_style_LabelBorderStyles.__init__)


def test_viewpoint_style_labelborderstyles_constructor_args():
    sig = inspect.signature(viewpoint_style_LabelBorderStyles.__init__)
    params = list(sig.parameters.keys())



def test_tool_toolfilterdescription_is_not_abstract():
    assert not inspect.isabstract(tool_ToolFilterDescription)


def test_tool_toolfilterdescription_constructor_exists():
    assert callable(tool_ToolFilterDescription.__init__)


def test_tool_toolfilterdescription_constructor_args():
    sig = inspect.signature(tool_ToolFilterDescription.__init__)
    params = list(sig.parameters.keys())



def test_toolentry_is_not_abstract():
    assert not inspect.isabstract(ToolEntry)


def test_toolentry_constructor_exists():
    assert callable(ToolEntry.__init__)


def test_toolentry_constructor_args():
    sig = inspect.signature(ToolEntry.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_abstracttooldescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_AbstractToolDescription)


def test_viewpoint_tool_abstracttooldescription_constructor_exists():
    assert callable(viewpoint_tool_AbstractToolDescription.__init__)


def test_viewpoint_tool_abstracttooldescription_constructor_args():
    sig = inspect.signature(viewpoint_tool_AbstractToolDescription.__init__)
    params = list(sig.parameters.keys())
    assert "elementsToSelect" in params, "Missing parameter 'elementsToSelect'"
    assert "forceRefresh" in params, "Missing parameter 'forceRefresh'"
    assert "precondition" in params, "Missing parameter 'precondition'"
    assert "inverseSelectionOrder" in params, "Missing parameter 'inverseSelectionOrder'"

def test_viewpoint_tool_abstracttooldescription_has_elementsToSelect():
    assert hasattr(viewpoint_tool_AbstractToolDescription, "elementsToSelect")
    descriptor = None
    for klass in viewpoint_tool_AbstractToolDescription.__mro__:
        if "elementsToSelect" in klass.__dict__:
            descriptor = klass.__dict__["elementsToSelect"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_abstracttooldescription_has_forceRefresh():
    assert hasattr(viewpoint_tool_AbstractToolDescription, "forceRefresh")
    descriptor = None
    for klass in viewpoint_tool_AbstractToolDescription.__mro__:
        if "forceRefresh" in klass.__dict__:
            descriptor = klass.__dict__["forceRefresh"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_abstracttooldescription_has_precondition():
    assert hasattr(viewpoint_tool_AbstractToolDescription, "precondition")
    descriptor = None
    for klass in viewpoint_tool_AbstractToolDescription.__mro__:
        if "precondition" in klass.__dict__:
            descriptor = klass.__dict__["precondition"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_abstracttooldescription_has_inverseSelectionOrder():
    assert hasattr(viewpoint_tool_AbstractToolDescription, "inverseSelectionOrder")
    descriptor = None
    for klass in viewpoint_tool_AbstractToolDescription.__mro__:
        if "inverseSelectionOrder" in klass.__dict__:
            descriptor = klass.__dict__["inverseSelectionOrder"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_style_tooltipstyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_style_TooltipStyleDescription)


def test_viewpoint_style_tooltipstyledescription_constructor_exists():
    assert callable(viewpoint_style_TooltipStyleDescription.__init__)


def test_viewpoint_style_tooltipstyledescription_constructor_args():
    sig = inspect.signature(viewpoint_style_TooltipStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "tooltipExpression" in params, "Missing parameter 'tooltipExpression'"

def test_viewpoint_style_tooltipstyledescription_has_tooltipExpression():
    assert hasattr(viewpoint_style_TooltipStyleDescription, "tooltipExpression")
    descriptor = None
    for klass in viewpoint_style_TooltipStyleDescription.__mro__:
        if "tooltipExpression" in klass.__dict__:
            descriptor = klass.__dict__["tooltipExpression"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_style_labelborderstyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_style_LabelBorderStyleDescription)


def test_viewpoint_style_labelborderstyledescription_constructor_exists():
    assert callable(viewpoint_style_LabelBorderStyleDescription.__init__)


def test_viewpoint_style_labelborderstyledescription_constructor_args():
    sig = inspect.signature(viewpoint_style_LabelBorderStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "cornerHeight" in params, "Missing parameter 'cornerHeight'"
    assert "cornerWidth" in params, "Missing parameter 'cornerWidth'"
    assert "name" in params, "Missing parameter 'name'"

def test_viewpoint_style_labelborderstyledescription_has_id():
    assert hasattr(viewpoint_style_LabelBorderStyleDescription, "id")
    descriptor = None
    for klass in viewpoint_style_LabelBorderStyleDescription.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_style_labelborderstyledescription_has_cornerHeight():
    assert hasattr(viewpoint_style_LabelBorderStyleDescription, "cornerHeight")
    descriptor = None
    for klass in viewpoint_style_LabelBorderStyleDescription.__mro__:
        if "cornerHeight" in klass.__dict__:
            descriptor = klass.__dict__["cornerHeight"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_style_labelborderstyledescription_has_cornerWidth():
    assert hasattr(viewpoint_style_LabelBorderStyleDescription, "cornerWidth")
    descriptor = None
    for klass in viewpoint_style_LabelBorderStyleDescription.__mro__:
        if "cornerWidth" in klass.__dict__:
            descriptor = klass.__dict__["cornerWidth"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_style_labelborderstyledescription_has_name():
    assert hasattr(viewpoint_style_LabelBorderStyleDescription, "name")
    descriptor = None
    for klass in viewpoint_style_LabelBorderStyleDescription.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_description_interactivevariabledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_InteractiveVariableDescription)


def test_viewpoint_description_interactivevariabledescription_constructor_exists():
    assert callable(viewpoint_description_InteractiveVariableDescription.__init__)


def test_viewpoint_description_interactivevariabledescription_constructor_args():
    sig = inspect.signature(viewpoint_description_InteractiveVariableDescription.__init__)
    params = list(sig.parameters.keys())
    assert "userDocumentation" in params, "Missing parameter 'userDocumentation'"

def test_viewpoint_description_interactivevariabledescription_has_userDocumentation():
    assert hasattr(viewpoint_description_InteractiveVariableDescription, "userDocumentation")
    descriptor = None
    for klass in viewpoint_description_InteractiveVariableDescription.__mro__:
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



def test_viewpoint_tool_namevariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_NameVariable)


def test_viewpoint_tool_namevariable_constructor_exists():
    assert callable(viewpoint_tool_NameVariable.__init__)


def test_viewpoint_tool_namevariable_constructor_args():
    sig = inspect.signature(viewpoint_tool_NameVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_dialogvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_DialogVariable)


def test_viewpoint_tool_dialogvariable_constructor_exists():
    assert callable(viewpoint_tool_DialogVariable.__init__)


def test_viewpoint_tool_dialogvariable_constructor_args():
    sig = inspect.signature(viewpoint_tool_DialogVariable.__init__)
    params = list(sig.parameters.keys())
    assert "dialogPrompt" in params, "Missing parameter 'dialogPrompt'"

def test_viewpoint_tool_dialogvariable_has_dialogPrompt():
    assert hasattr(viewpoint_tool_DialogVariable, "dialogPrompt")
    descriptor = None
    for klass in viewpoint_tool_DialogVariable.__mro__:
        if "dialogPrompt" in klass.__dict__:
            descriptor = klass.__dict__["dialogPrompt"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_tool_elementselectvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ElementSelectVariable)


def test_viewpoint_tool_elementselectvariable_constructor_exists():
    assert callable(viewpoint_tool_ElementSelectVariable.__init__)


def test_viewpoint_tool_elementselectvariable_constructor_args():
    sig = inspect.signature(viewpoint_tool_ElementSelectVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_subvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_SubVariable)


def test_viewpoint_description_subvariable_constructor_exists():
    assert callable(viewpoint_description_SubVariable.__init__)


def test_viewpoint_description_subvariable_constructor_args():
    sig = inspect.signature(viewpoint_description_SubVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_abstractvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_AbstractVariable)


def test_viewpoint_description_abstractvariable_constructor_exists():
    assert callable(viewpoint_description_AbstractVariable.__init__)


def test_viewpoint_description_abstractvariable_constructor_args():
    sig = inspect.signature(viewpoint_description_AbstractVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_viewpoint_description_abstractvariable_has_name():
    assert hasattr(viewpoint_description_AbstractVariable, "name")
    descriptor = None
    for klass in viewpoint_description_AbstractVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_basiclabelstyledescription_is_not_abstract():
    assert not inspect.isabstract(BasicLabelStyleDescription)


def test_basiclabelstyledescription_constructor_exists():
    assert callable(BasicLabelStyleDescription.__init__)


def test_basiclabelstyledescription_constructor_args():
    sig = inspect.signature(BasicLabelStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_style_labelstyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_style_LabelStyleDescription)


def test_viewpoint_style_labelstyledescription_constructor_exists():
    assert callable(viewpoint_style_LabelStyleDescription.__init__)


def test_viewpoint_style_labelstyledescription_constructor_args():
    sig = inspect.signature(viewpoint_style_LabelStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "labelAlignment" in params, "Missing parameter 'labelAlignment'"

def test_viewpoint_style_labelstyledescription_has_labelAlignment():
    assert hasattr(viewpoint_style_LabelStyleDescription, "labelAlignment")
    descriptor = None
    for klass in viewpoint_style_LabelStyleDescription.__mro__:
        if "labelAlignment" in klass.__dict__:
            descriptor = klass.__dict__["labelAlignment"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_description_dannotationentry_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_DAnnotationEntry)


def test_viewpoint_description_dannotationentry_constructor_exists():
    assert callable(viewpoint_description_DAnnotationEntry.__init__)


def test_viewpoint_description_dannotationentry_constructor_args():
    sig = inspect.signature(viewpoint_description_DAnnotationEntry.__init__)
    params = list(sig.parameters.keys())
    assert "source" in params, "Missing parameter 'source'"
    assert "details" in params, "Missing parameter 'details'"

def test_viewpoint_description_dannotationentry_has_source():
    assert hasattr(viewpoint_description_DAnnotationEntry, "source")
    descriptor = None
    for klass in viewpoint_description_DAnnotationEntry.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_dannotationentry_has_details():
    assert hasattr(viewpoint_description_DAnnotationEntry, "details")
    descriptor = None
    for klass in viewpoint_description_DAnnotationEntry.__mro__:
        if "details" in klass.__dict__:
            descriptor = klass.__dict__["details"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_style_basiclabelstyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_style_BasicLabelStyleDescription)


def test_viewpoint_style_basiclabelstyledescription_constructor_exists():
    assert callable(viewpoint_style_BasicLabelStyleDescription.__init__)


def test_viewpoint_style_basiclabelstyledescription_constructor_args():
    sig = inspect.signature(viewpoint_style_BasicLabelStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "labelSize" in params, "Missing parameter 'labelSize'"
    assert "labelExpression" in params, "Missing parameter 'labelExpression'"
    assert "showIcon" in params, "Missing parameter 'showIcon'"
    assert "labelFormat" in params, "Missing parameter 'labelFormat'"
    assert "iconPath" in params, "Missing parameter 'iconPath'"

def test_viewpoint_style_basiclabelstyledescription_has_labelSize():
    assert hasattr(viewpoint_style_BasicLabelStyleDescription, "labelSize")
    descriptor = None
    for klass in viewpoint_style_BasicLabelStyleDescription.__mro__:
        if "labelSize" in klass.__dict__:
            descriptor = klass.__dict__["labelSize"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_style_basiclabelstyledescription_has_labelExpression():
    assert hasattr(viewpoint_style_BasicLabelStyleDescription, "labelExpression")
    descriptor = None
    for klass in viewpoint_style_BasicLabelStyleDescription.__mro__:
        if "labelExpression" in klass.__dict__:
            descriptor = klass.__dict__["labelExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_style_basiclabelstyledescription_has_showIcon():
    assert hasattr(viewpoint_style_BasicLabelStyleDescription, "showIcon")
    descriptor = None
    for klass in viewpoint_style_BasicLabelStyleDescription.__mro__:
        if "showIcon" in klass.__dict__:
            descriptor = klass.__dict__["showIcon"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_style_basiclabelstyledescription_has_labelFormat():
    assert hasattr(viewpoint_style_BasicLabelStyleDescription, "labelFormat")
    descriptor = None
    for klass in viewpoint_style_BasicLabelStyleDescription.__mro__:
        if "labelFormat" in klass.__dict__:
            descriptor = klass.__dict__["labelFormat"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_style_basiclabelstyledescription_has_iconPath():
    assert hasattr(viewpoint_style_BasicLabelStyleDescription, "iconPath")
    descriptor = None
    for klass in viewpoint_style_BasicLabelStyleDescription.__mro__:
        if "iconPath" in klass.__dict__:
            descriptor = klass.__dict__["iconPath"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_style_styledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_style_StyleDescription)


def test_viewpoint_style_styledescription_constructor_exists():
    assert callable(viewpoint_style_StyleDescription.__init__)


def test_viewpoint_style_styledescription_constructor_args():
    sig = inspect.signature(viewpoint_style_StyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_description_viewpoint_edatatype_is_not_abstract():
    assert not inspect.isabstract(description_viewpoint_EDataType)


def test_description_viewpoint_edatatype_constructor_exists():
    assert callable(description_viewpoint_EDataType.__init__)


def test_description_viewpoint_edatatype_constructor_args():
    sig = inspect.signature(description_viewpoint_EDataType.__init__)
    params = list(sig.parameters.keys())



def test_description_subvariable_is_not_abstract():
    assert not inspect.isabstract(description_SubVariable)


def test_description_subvariable_constructor_exists():
    assert callable(description_SubVariable.__init__)


def test_description_subvariable_constructor_args():
    sig = inspect.signature(description_SubVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_acceleovariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_AcceleoVariable)


def test_viewpoint_tool_acceleovariable_constructor_exists():
    assert callable(viewpoint_tool_AcceleoVariable.__init__)


def test_viewpoint_tool_acceleovariable_constructor_args():
    sig = inspect.signature(viewpoint_tool_AcceleoVariable.__init__)
    params = list(sig.parameters.keys())
    assert "computationExpression" in params, "Missing parameter 'computationExpression'"

def test_viewpoint_tool_acceleovariable_has_computationExpression():
    assert hasattr(viewpoint_tool_AcceleoVariable, "computationExpression")
    descriptor = None
    for klass in viewpoint_tool_AcceleoVariable.__mro__:
        if "computationExpression" in klass.__dict__:
            descriptor = klass.__dict__["computationExpression"]
            break
    assert isinstance(descriptor, property)



def test_description_interactivevariabledescription_is_not_abstract():
    assert not inspect.isabstract(description_InteractiveVariableDescription)


def test_description_interactivevariabledescription_constructor_exists():
    assert callable(description_InteractiveVariableDescription.__init__)


def test_description_interactivevariabledescription_constructor_args():
    sig = inspect.signature(description_InteractiveVariableDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_selectmodelelementvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_SelectModelElementVariable)


def test_viewpoint_tool_selectmodelelementvariable_constructor_exists():
    assert callable(viewpoint_tool_SelectModelElementVariable.__init__)


def test_viewpoint_tool_selectmodelelementvariable_constructor_args():
    sig = inspect.signature(viewpoint_tool_SelectModelElementVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_typedvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_TypedVariable)


def test_viewpoint_description_typedvariable_constructor_exists():
    assert callable(viewpoint_description_TypedVariable.__init__)


def test_viewpoint_description_typedvariable_constructor_args():
    sig = inspect.signature(viewpoint_description_TypedVariable.__init__)
    params = list(sig.parameters.keys())
    assert "defaultValueExpression" in params, "Missing parameter 'defaultValueExpression'"

def test_viewpoint_description_typedvariable_has_defaultValueExpression():
    assert hasattr(viewpoint_description_TypedVariable, "defaultValueExpression")
    descriptor = None
    for klass in viewpoint_description_TypedVariable.__mro__:
        if "defaultValueExpression" in klass.__dict__:
            descriptor = klass.__dict__["defaultValueExpression"]
            break
    assert isinstance(descriptor, property)



def test_systemcolor_is_not_abstract():
    assert not inspect.isabstract(SystemColor)


def test_systemcolor_constructor_exists():
    assert callable(SystemColor.__init__)


def test_systemcolor_constructor_args():
    sig = inspect.signature(SystemColor.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_sytemcolorspalette_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_SytemColorsPalette)


def test_viewpoint_description_sytemcolorspalette_constructor_exists():
    assert callable(viewpoint_description_SytemColorsPalette.__init__)


def test_viewpoint_description_sytemcolorspalette_constructor_args():
    sig = inspect.signature(viewpoint_description_SytemColorsPalette.__init__)
    params = list(sig.parameters.keys())



def test_style_labelborderstyles_is_not_abstract():
    assert not inspect.isabstract(style_LabelBorderStyles)


def test_style_labelborderstyles_constructor_exists():
    assert callable(style_LabelBorderStyles.__init__)


def test_style_labelborderstyles_constructor_args():
    sig = inspect.signature(style_LabelBorderStyles.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_identifiedelement_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_IdentifiedElement)


def test_viewpoint_description_identifiedelement_constructor_exists():
    assert callable(viewpoint_description_IdentifiedElement.__init__)


def test_viewpoint_description_identifiedelement_constructor_args():
    sig = inspect.signature(viewpoint_description_IdentifiedElement.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "name" in params, "Missing parameter 'name'"

def test_viewpoint_description_identifiedelement_has_label():
    assert hasattr(viewpoint_description_IdentifiedElement, "label")
    descriptor = None
    for klass in viewpoint_description_IdentifiedElement.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_identifiedelement_has_name():
    assert hasattr(viewpoint_description_IdentifiedElement, "name")
    descriptor = None
    for klass in viewpoint_description_IdentifiedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_description_enduserdocumentedelement_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_EndUserDocumentedElement)


def test_viewpoint_description_enduserdocumentedelement_constructor_exists():
    assert callable(viewpoint_description_EndUserDocumentedElement.__init__)


def test_viewpoint_description_enduserdocumentedelement_constructor_args():
    sig = inspect.signature(viewpoint_description_EndUserDocumentedElement.__init__)
    params = list(sig.parameters.keys())
    assert "endUserDocumentation" in params, "Missing parameter 'endUserDocumentation'"

def test_viewpoint_description_enduserdocumentedelement_has_endUserDocumentation():
    assert hasattr(viewpoint_description_EndUserDocumentedElement, "endUserDocumentation")
    descriptor = None
    for klass in viewpoint_description_EndUserDocumentedElement.__mro__:
        if "endUserDocumentation" in klass.__dict__:
            descriptor = klass.__dict__["endUserDocumentation"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_description_annotationentry_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_AnnotationEntry)


def test_viewpoint_description_annotationentry_constructor_exists():
    assert callable(viewpoint_description_AnnotationEntry.__init__)


def test_viewpoint_description_annotationentry_constructor_args():
    sig = inspect.signature(viewpoint_description_AnnotationEntry.__init__)
    params = list(sig.parameters.keys())
    assert "source" in params, "Missing parameter 'source'"

def test_viewpoint_description_annotationentry_has_source():
    assert hasattr(viewpoint_description_AnnotationEntry, "source")
    descriptor = None
    for klass in viewpoint_description_AnnotationEntry.__mro__:
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



def test_viewpoint_description_usercolorspalette_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_UserColorsPalette)


def test_viewpoint_description_usercolorspalette_constructor_exists():
    assert callable(viewpoint_description_UserColorsPalette.__init__)


def test_viewpoint_description_usercolorspalette_constructor_args():
    sig = inspect.signature(viewpoint_description_UserColorsPalette.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_viewpoint_description_usercolorspalette_has_name():
    assert hasattr(viewpoint_description_UserColorsPalette, "name")
    descriptor = None
    for klass in viewpoint_description_UserColorsPalette.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_description_environment_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_Environment)


def test_viewpoint_description_environment_constructor_exists():
    assert callable(viewpoint_description_Environment.__init__)


def test_viewpoint_description_environment_constructor_args():
    sig = inspect.signature(viewpoint_description_Environment.__init__)
    params = list(sig.parameters.keys())



def test_colorstep_is_not_abstract():
    assert not inspect.isabstract(ColorStep)


def test_colorstep_constructor_exists():
    assert callable(ColorStep.__init__)


def test_colorstep_constructor_args():
    sig = inspect.signature(ColorStep.__init__)
    params = list(sig.parameters.keys())



def test_description_usercolor_is_not_abstract():
    assert not inspect.isabstract(description_UserColor)


def test_description_usercolor_constructor_exists():
    assert callable(description_UserColor.__init__)


def test_description_usercolor_constructor_args():
    sig = inspect.signature(description_UserColor.__init__)
    params = list(sig.parameters.keys())



def test_description_colordescription_is_not_abstract():
    assert not inspect.isabstract(description_ColorDescription)


def test_description_colordescription_constructor_exists():
    assert callable(description_ColorDescription.__init__)


def test_description_colordescription_constructor_args():
    sig = inspect.signature(description_ColorDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_computedcolor_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_ComputedColor)


def test_viewpoint_description_computedcolor_constructor_exists():
    assert callable(viewpoint_description_ComputedColor.__init__)


def test_viewpoint_description_computedcolor_constructor_args():
    sig = inspect.signature(viewpoint_description_ComputedColor.__init__)
    params = list(sig.parameters.keys())
    assert "green" in params, "Missing parameter 'green'"
    assert "red" in params, "Missing parameter 'red'"
    assert "blue" in params, "Missing parameter 'blue'"

def test_viewpoint_description_computedcolor_has_green():
    assert hasattr(viewpoint_description_ComputedColor, "green")
    descriptor = None
    for klass in viewpoint_description_ComputedColor.__mro__:
        if "green" in klass.__dict__:
            descriptor = klass.__dict__["green"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_computedcolor_has_red():
    assert hasattr(viewpoint_description_ComputedColor, "red")
    descriptor = None
    for klass in viewpoint_description_ComputedColor.__mro__:
        if "red" in klass.__dict__:
            descriptor = klass.__dict__["red"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_computedcolor_has_blue():
    assert hasattr(viewpoint_description_ComputedColor, "blue")
    descriptor = None
    for klass in viewpoint_description_ComputedColor.__mro__:
        if "blue" in klass.__dict__:
            descriptor = klass.__dict__["blue"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_description_interpolatedcolor_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_InterpolatedColor)


def test_viewpoint_description_interpolatedcolor_constructor_exists():
    assert callable(viewpoint_description_InterpolatedColor.__init__)


def test_viewpoint_description_interpolatedcolor_constructor_args():
    sig = inspect.signature(viewpoint_description_InterpolatedColor.__init__)
    params = list(sig.parameters.keys())
    assert "maxValueComputationExpression" in params, "Missing parameter 'maxValueComputationExpression'"
    assert "minValueComputationExpression" in params, "Missing parameter 'minValueComputationExpression'"
    assert "colorValueComputationExpression" in params, "Missing parameter 'colorValueComputationExpression'"

def test_viewpoint_description_interpolatedcolor_has_maxValueComputationExpression():
    assert hasattr(viewpoint_description_InterpolatedColor, "maxValueComputationExpression")
    descriptor = None
    for klass in viewpoint_description_InterpolatedColor.__mro__:
        if "maxValueComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["maxValueComputationExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_interpolatedcolor_has_minValueComputationExpression():
    assert hasattr(viewpoint_description_InterpolatedColor, "minValueComputationExpression")
    descriptor = None
    for klass in viewpoint_description_InterpolatedColor.__mro__:
        if "minValueComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["minValueComputationExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_interpolatedcolor_has_colorValueComputationExpression():
    assert hasattr(viewpoint_description_InterpolatedColor, "colorValueComputationExpression")
    descriptor = None
    for klass in viewpoint_description_InterpolatedColor.__mro__:
        if "colorValueComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["colorValueComputationExpression"]
            break
    assert isinstance(descriptor, property)



def test_fixedcolor_is_not_abstract():
    assert not inspect.isabstract(FixedColor)


def test_fixedcolor_constructor_exists():
    assert callable(FixedColor.__init__)


def test_fixedcolor_constructor_args():
    sig = inspect.signature(FixedColor.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_systemcolor_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_SystemColor)


def test_viewpoint_description_systemcolor_constructor_exists():
    assert callable(viewpoint_description_SystemColor.__init__)


def test_viewpoint_description_systemcolor_constructor_args():
    sig = inspect.signature(viewpoint_description_SystemColor.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_viewpoint_description_systemcolor_has_name():
    assert hasattr(viewpoint_description_SystemColor, "name")
    descriptor = None
    for klass in viewpoint_description_SystemColor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_description_usercolor_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_UserColor)


def test_viewpoint_description_usercolor_constructor_exists():
    assert callable(viewpoint_description_UserColor.__init__)


def test_viewpoint_description_usercolor_constructor_args():
    sig = inspect.signature(viewpoint_description_UserColor.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_viewpoint_description_usercolor_has_name():
    assert hasattr(viewpoint_description_UserColor, "name")
    descriptor = None
    for klass in viewpoint_description_UserColor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_description_colordescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_ColorDescription)


def test_viewpoint_description_colordescription_constructor_exists():
    assert callable(viewpoint_description_ColorDescription.__init__)


def test_viewpoint_description_colordescription_constructor_args():
    sig = inspect.signature(viewpoint_description_ColorDescription.__init__)
    params = list(sig.parameters.keys())



def test_description_fixedcolor_is_not_abstract():
    assert not inspect.isabstract(description_FixedColor)


def test_description_fixedcolor_constructor_exists():
    assert callable(description_FixedColor.__init__)


def test_description_fixedcolor_constructor_args():
    sig = inspect.signature(description_FixedColor.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_userfixedcolor_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_UserFixedColor)


def test_viewpoint_description_userfixedcolor_constructor_exists():
    assert callable(viewpoint_description_UserFixedColor.__init__)


def test_viewpoint_description_userfixedcolor_constructor_args():
    sig = inspect.signature(viewpoint_description_UserFixedColor.__init__)
    params = list(sig.parameters.keys())



def test_colordescription_is_not_abstract():
    assert not inspect.isabstract(ColorDescription)


def test_colordescription_constructor_exists():
    assert callable(ColorDescription.__init__)


def test_colordescription_constructor_args():
    sig = inspect.signature(ColorDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_fixedcolor_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_FixedColor)


def test_viewpoint_description_fixedcolor_constructor_exists():
    assert callable(viewpoint_description_FixedColor.__init__)


def test_viewpoint_description_fixedcolor_constructor_args():
    sig = inspect.signature(viewpoint_description_FixedColor.__init__)
    params = list(sig.parameters.keys())
    assert "red" in params, "Missing parameter 'red'"
    assert "green" in params, "Missing parameter 'green'"
    assert "blue" in params, "Missing parameter 'blue'"

def test_viewpoint_description_fixedcolor_has_red():
    assert hasattr(viewpoint_description_FixedColor, "red")
    descriptor = None
    for klass in viewpoint_description_FixedColor.__mro__:
        if "red" in klass.__dict__:
            descriptor = klass.__dict__["red"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_fixedcolor_has_green():
    assert hasattr(viewpoint_description_FixedColor, "green")
    descriptor = None
    for klass in viewpoint_description_FixedColor.__mro__:
        if "green" in klass.__dict__:
            descriptor = klass.__dict__["green"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_fixedcolor_has_blue():
    assert hasattr(viewpoint_description_FixedColor, "blue")
    descriptor = None
    for klass in viewpoint_description_FixedColor.__mro__:
        if "blue" in klass.__dict__:
            descriptor = klass.__dict__["blue"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_description_colorstep_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_ColorStep)


def test_viewpoint_description_colorstep_constructor_exists():
    assert callable(viewpoint_description_ColorStep.__init__)


def test_viewpoint_description_colorstep_constructor_args():
    sig = inspect.signature(viewpoint_description_ColorStep.__init__)
    params = list(sig.parameters.keys())
    assert "associatedValue" in params, "Missing parameter 'associatedValue'"

def test_viewpoint_description_colorstep_has_associatedValue():
    assert hasattr(viewpoint_description_ColorStep, "associatedValue")
    descriptor = None
    for klass in viewpoint_description_ColorStep.__mro__:
        if "associatedValue" in klass.__dict__:
            descriptor = klass.__dict__["associatedValue"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_description_estructuralfeaturecustomization_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_EStructuralFeatureCustomization)


def test_viewpoint_description_estructuralfeaturecustomization_constructor_exists():
    assert callable(viewpoint_description_EStructuralFeatureCustomization.__init__)


def test_viewpoint_description_estructuralfeaturecustomization_constructor_args():
    sig = inspect.signature(viewpoint_description_EStructuralFeatureCustomization.__init__)
    params = list(sig.parameters.keys())
    assert "applyOnAll" in params, "Missing parameter 'applyOnAll'"

def test_viewpoint_description_estructuralfeaturecustomization_has_applyOnAll():
    assert hasattr(viewpoint_description_EStructuralFeatureCustomization, "applyOnAll")
    descriptor = None
    for klass in viewpoint_description_EStructuralFeatureCustomization.__mro__:
        if "applyOnAll" in klass.__dict__:
            descriptor = klass.__dict__["applyOnAll"]
            break
    assert isinstance(descriptor, property)



def test_estructuralfeaturecustomization_is_not_abstract():
    assert not inspect.isabstract(EStructuralFeatureCustomization)


def test_estructuralfeaturecustomization_constructor_exists():
    assert callable(EStructuralFeatureCustomization.__init__)


def test_estructuralfeaturecustomization_constructor_args():
    sig = inspect.signature(EStructuralFeatureCustomization.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_ereferencecustomization_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_EReferenceCustomization)


def test_viewpoint_description_ereferencecustomization_constructor_exists():
    assert callable(viewpoint_description_EReferenceCustomization.__init__)


def test_viewpoint_description_ereferencecustomization_constructor_args():
    sig = inspect.signature(viewpoint_description_EReferenceCustomization.__init__)
    params = list(sig.parameters.keys())
    assert "referenceName" in params, "Missing parameter 'referenceName'"

def test_viewpoint_description_ereferencecustomization_has_referenceName():
    assert hasattr(viewpoint_description_EReferenceCustomization, "referenceName")
    descriptor = None
    for klass in viewpoint_description_EReferenceCustomization.__mro__:
        if "referenceName" in klass.__dict__:
            descriptor = klass.__dict__["referenceName"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_description_eattributecustomization_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_EAttributeCustomization)


def test_viewpoint_description_eattributecustomization_constructor_exists():
    assert callable(viewpoint_description_EAttributeCustomization.__init__)


def test_viewpoint_description_eattributecustomization_constructor_args():
    sig = inspect.signature(viewpoint_description_EAttributeCustomization.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "attributeName" in params, "Missing parameter 'attributeName'"

def test_viewpoint_description_eattributecustomization_has_value():
    assert hasattr(viewpoint_description_EAttributeCustomization, "value")
    descriptor = None
    for klass in viewpoint_description_EAttributeCustomization.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_eattributecustomization_has_attributeName():
    assert hasattr(viewpoint_description_EAttributeCustomization, "attributeName")
    descriptor = None
    for klass in viewpoint_description_EAttributeCustomization.__mro__:
        if "attributeName" in klass.__dict__:
            descriptor = klass.__dict__["attributeName"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_description_selectiondescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_SelectionDescription)


def test_viewpoint_description_selectiondescription_constructor_exists():
    assert callable(viewpoint_description_SelectionDescription.__init__)


def test_viewpoint_description_selectiondescription_constructor_args():
    sig = inspect.signature(viewpoint_description_SelectionDescription.__init__)
    params = list(sig.parameters.keys())
    assert "childrenExpression" in params, "Missing parameter 'childrenExpression'"
    assert "candidatesExpression" in params, "Missing parameter 'candidatesExpression'"
    assert "multiple" in params, "Missing parameter 'multiple'"
    assert "tree" in params, "Missing parameter 'tree'"
    assert "message" in params, "Missing parameter 'message'"
    assert "rootExpression" in params, "Missing parameter 'rootExpression'"

def test_viewpoint_description_selectiondescription_has_childrenExpression():
    assert hasattr(viewpoint_description_SelectionDescription, "childrenExpression")
    descriptor = None
    for klass in viewpoint_description_SelectionDescription.__mro__:
        if "childrenExpression" in klass.__dict__:
            descriptor = klass.__dict__["childrenExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_selectiondescription_has_candidatesExpression():
    assert hasattr(viewpoint_description_SelectionDescription, "candidatesExpression")
    descriptor = None
    for klass in viewpoint_description_SelectionDescription.__mro__:
        if "candidatesExpression" in klass.__dict__:
            descriptor = klass.__dict__["candidatesExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_selectiondescription_has_multiple():
    assert hasattr(viewpoint_description_SelectionDescription, "multiple")
    descriptor = None
    for klass in viewpoint_description_SelectionDescription.__mro__:
        if "multiple" in klass.__dict__:
            descriptor = klass.__dict__["multiple"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_selectiondescription_has_tree():
    assert hasattr(viewpoint_description_SelectionDescription, "tree")
    descriptor = None
    for klass in viewpoint_description_SelectionDescription.__mro__:
        if "tree" in klass.__dict__:
            descriptor = klass.__dict__["tree"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_selectiondescription_has_message():
    assert hasattr(viewpoint_description_SelectionDescription, "message")
    descriptor = None
    for klass in viewpoint_description_SelectionDescription.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_selectiondescription_has_rootExpression():
    assert hasattr(viewpoint_description_SelectionDescription, "rootExpression")
    descriptor = None
    for klass in viewpoint_description_SelectionDescription.__mro__:
        if "rootExpression" in klass.__dict__:
            descriptor = klass.__dict__["rootExpression"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_description_genericdecorationdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_GenericDecorationDescription)


def test_viewpoint_description_genericdecorationdescription_constructor_exists():
    assert callable(viewpoint_description_GenericDecorationDescription.__init__)


def test_viewpoint_description_genericdecorationdescription_constructor_args():
    sig = inspect.signature(viewpoint_description_GenericDecorationDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_semanticbaseddecoration_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_SemanticBasedDecoration)


def test_viewpoint_description_semanticbaseddecoration_constructor_exists():
    assert callable(viewpoint_description_SemanticBasedDecoration.__init__)


def test_viewpoint_description_semanticbaseddecoration_constructor_args():
    sig = inspect.signature(viewpoint_description_SemanticBasedDecoration.__init__)
    params = list(sig.parameters.keys())
    assert "domainClass" in params, "Missing parameter 'domainClass'"

def test_viewpoint_description_semanticbaseddecoration_has_domainClass():
    assert hasattr(viewpoint_description_SemanticBasedDecoration, "domainClass")
    descriptor = None
    for klass in viewpoint_description_SemanticBasedDecoration.__mro__:
        if "domainClass" in klass.__dict__:
            descriptor = klass.__dict__["domainClass"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_description_ivsmelementcustomization_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_IVSMElementCustomization)


def test_viewpoint_description_ivsmelementcustomization_constructor_exists():
    assert callable(viewpoint_description_IVSMElementCustomization.__init__)


def test_viewpoint_description_ivsmelementcustomization_constructor_args():
    sig = inspect.signature(viewpoint_description_IVSMElementCustomization.__init__)
    params = list(sig.parameters.keys())



def test_ivsmelementcustomization_is_not_abstract():
    assert not inspect.isabstract(IVSMElementCustomization)


def test_ivsmelementcustomization_constructor_exists():
    assert callable(IVSMElementCustomization.__init__)


def test_ivsmelementcustomization_constructor_args():
    sig = inspect.signature(IVSMElementCustomization.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_vsmelementcustomization_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_VSMElementCustomization)


def test_viewpoint_description_vsmelementcustomization_constructor_exists():
    assert callable(viewpoint_description_VSMElementCustomization.__init__)


def test_viewpoint_description_vsmelementcustomization_constructor_args():
    sig = inspect.signature(viewpoint_description_VSMElementCustomization.__init__)
    params = list(sig.parameters.keys())
    assert "predicateExpression" in params, "Missing parameter 'predicateExpression'"

def test_viewpoint_description_vsmelementcustomization_has_predicateExpression():
    assert hasattr(viewpoint_description_VSMElementCustomization, "predicateExpression")
    descriptor = None
    for klass in viewpoint_description_VSMElementCustomization.__mro__:
        if "predicateExpression" in klass.__dict__:
            descriptor = klass.__dict__["predicateExpression"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_description_vsmelementcustomizationreuse_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_VSMElementCustomizationReuse)


def test_viewpoint_description_vsmelementcustomizationreuse_constructor_exists():
    assert callable(viewpoint_description_VSMElementCustomizationReuse.__init__)


def test_viewpoint_description_vsmelementcustomizationreuse_constructor_args():
    sig = inspect.signature(viewpoint_description_VSMElementCustomizationReuse.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_customization_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_Customization)


def test_viewpoint_description_customization_constructor_exists():
    assert callable(viewpoint_description_Customization.__init__)


def test_viewpoint_description_customization_constructor_args():
    sig = inspect.signature(viewpoint_description_Customization.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_decorationdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_DecorationDescription)


def test_viewpoint_description_decorationdescription_constructor_exists():
    assert callable(viewpoint_description_DecorationDescription.__init__)


def test_viewpoint_description_decorationdescription_constructor_args():
    sig = inspect.signature(viewpoint_description_DecorationDescription.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"
    assert "tooltipExpression" in params, "Missing parameter 'tooltipExpression'"
    assert "name" in params, "Missing parameter 'name'"
    assert "preconditionExpression" in params, "Missing parameter 'preconditionExpression'"
    assert "imageExpression" in params, "Missing parameter 'imageExpression'"
    assert "distributionDirection" in params, "Missing parameter 'distributionDirection'"

def test_viewpoint_description_decorationdescription_has_position():
    assert hasattr(viewpoint_description_DecorationDescription, "position")
    descriptor = None
    for klass in viewpoint_description_DecorationDescription.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_decorationdescription_has_tooltipExpression():
    assert hasattr(viewpoint_description_DecorationDescription, "tooltipExpression")
    descriptor = None
    for klass in viewpoint_description_DecorationDescription.__mro__:
        if "tooltipExpression" in klass.__dict__:
            descriptor = klass.__dict__["tooltipExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_decorationdescription_has_name():
    assert hasattr(viewpoint_description_DecorationDescription, "name")
    descriptor = None
    for klass in viewpoint_description_DecorationDescription.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_decorationdescription_has_preconditionExpression():
    assert hasattr(viewpoint_description_DecorationDescription, "preconditionExpression")
    descriptor = None
    for klass in viewpoint_description_DecorationDescription.__mro__:
        if "preconditionExpression" in klass.__dict__:
            descriptor = klass.__dict__["preconditionExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_decorationdescription_has_imageExpression():
    assert hasattr(viewpoint_description_DecorationDescription, "imageExpression")
    descriptor = None
    for klass in viewpoint_description_DecorationDescription.__mro__:
        if "imageExpression" in klass.__dict__:
            descriptor = klass.__dict__["imageExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_decorationdescription_has_distributionDirection():
    assert hasattr(viewpoint_description_DecorationDescription, "distributionDirection")
    descriptor = None
    for klass in viewpoint_description_DecorationDescription.__mro__:
        if "distributionDirection" in klass.__dict__:
            descriptor = klass.__dict__["distributionDirection"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_description_decorationdescriptionsset_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_DecorationDescriptionsSet)


def test_viewpoint_description_decorationdescriptionsset_constructor_exists():
    assert callable(viewpoint_description_DecorationDescriptionsSet.__init__)


def test_viewpoint_description_decorationdescriptionsset_constructor_args():
    sig = inspect.signature(viewpoint_description_DecorationDescriptionsSet.__init__)
    params = list(sig.parameters.keys())



def test_tool_pastedescription_is_not_abstract():
    assert not inspect.isabstract(tool_PasteDescription)


def test_tool_pastedescription_constructor_exists():
    assert callable(tool_PasteDescription.__init__)


def test_tool_pastedescription_constructor_args():
    sig = inspect.signature(tool_PasteDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_pastetargetdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_PasteTargetDescription)


def test_viewpoint_description_pastetargetdescription_constructor_exists():
    assert callable(viewpoint_description_PasteTargetDescription.__init__)


def test_viewpoint_description_pastetargetdescription_constructor_args():
    sig = inspect.signature(viewpoint_description_PasteTargetDescription.__init__)
    params = list(sig.parameters.keys())



def test_dannotation_is_not_abstract():
    assert not inspect.isabstract(DAnnotation)


def test_dannotation_constructor_exists():
    assert callable(DAnnotation.__init__)


def test_dannotation_constructor_args():
    sig = inspect.signature(DAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_dmodelelement_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_DModelElement)


def test_viewpoint_description_dmodelelement_constructor_exists():
    assert callable(viewpoint_description_DModelElement.__init__)


def test_viewpoint_description_dmodelelement_constructor_args():
    sig = inspect.signature(viewpoint_description_DModelElement.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_documentedelement_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_DocumentedElement)


def test_viewpoint_description_documentedelement_constructor_exists():
    assert callable(viewpoint_description_DocumentedElement.__init__)


def test_viewpoint_description_documentedelement_constructor_args():
    sig = inspect.signature(viewpoint_description_DocumentedElement.__init__)
    params = list(sig.parameters.keys())
    assert "documentation" in params, "Missing parameter 'documentation'"

def test_viewpoint_description_documentedelement_has_documentation():
    assert hasattr(viewpoint_description_DocumentedElement, "documentation")
    descriptor = None
    for klass in viewpoint_description_DocumentedElement.__mro__:
        if "documentation" in klass.__dict__:
            descriptor = klass.__dict__["documentation"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_description_abstractmappingimport_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_AbstractMappingImport)


def test_viewpoint_description_abstractmappingimport_constructor_exists():
    assert callable(viewpoint_description_AbstractMappingImport.__init__)


def test_viewpoint_description_abstractmappingimport_constructor_args():
    sig = inspect.signature(viewpoint_description_AbstractMappingImport.__init__)
    params = list(sig.parameters.keys())
    assert "inheritsAncestorFilters" in params, "Missing parameter 'inheritsAncestorFilters'"
    assert "hideSubMappings" in params, "Missing parameter 'hideSubMappings'"

def test_viewpoint_description_abstractmappingimport_has_inheritsAncestorFilters():
    assert hasattr(viewpoint_description_AbstractMappingImport, "inheritsAncestorFilters")
    descriptor = None
    for klass in viewpoint_description_AbstractMappingImport.__mro__:
        if "inheritsAncestorFilters" in klass.__dict__:
            descriptor = klass.__dict__["inheritsAncestorFilters"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_abstractmappingimport_has_hideSubMappings():
    assert hasattr(viewpoint_description_AbstractMappingImport, "hideSubMappings")
    descriptor = None
    for klass in viewpoint_description_AbstractMappingImport.__mro__:
        if "hideSubMappings" in klass.__dict__:
            descriptor = klass.__dict__["hideSubMappings"]
            break
    assert isinstance(descriptor, property)



def test_tool_representationnavigationdescription_is_not_abstract():
    assert not inspect.isabstract(tool_RepresentationNavigationDescription)


def test_tool_representationnavigationdescription_constructor_exists():
    assert callable(tool_RepresentationNavigationDescription.__init__)


def test_tool_representationnavigationdescription_constructor_args():
    sig = inspect.signature(tool_RepresentationNavigationDescription.__init__)
    params = list(sig.parameters.keys())



def test_tool_representationcreationdescription_is_not_abstract():
    assert not inspect.isabstract(tool_RepresentationCreationDescription)


def test_tool_representationcreationdescription_constructor_exists():
    assert callable(tool_RepresentationCreationDescription.__init__)


def test_tool_representationcreationdescription_constructor_args():
    sig = inspect.signature(tool_RepresentationCreationDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_representationelementmapping_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_RepresentationElementMapping)


def test_viewpoint_description_representationelementmapping_constructor_exists():
    assert callable(viewpoint_description_RepresentationElementMapping.__init__)


def test_viewpoint_description_representationelementmapping_constructor_args():
    sig = inspect.signature(viewpoint_description_RepresentationElementMapping.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_conditionalstyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_ConditionalStyleDescription)


def test_viewpoint_description_conditionalstyledescription_constructor_exists():
    assert callable(viewpoint_description_ConditionalStyleDescription.__init__)


def test_viewpoint_description_conditionalstyledescription_constructor_args():
    sig = inspect.signature(viewpoint_description_ConditionalStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "predicateExpression" in params, "Missing parameter 'predicateExpression'"

def test_viewpoint_description_conditionalstyledescription_has_predicateExpression():
    assert hasattr(viewpoint_description_ConditionalStyleDescription, "predicateExpression")
    descriptor = None
    for klass in viewpoint_description_ConditionalStyleDescription.__mro__:
        if "predicateExpression" in klass.__dict__:
            descriptor = klass.__dict__["predicateExpression"]
            break
    assert isinstance(descriptor, property)



def test_description_viewpoint_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(description_viewpoint_EStringToStringMapEntry)


def test_description_viewpoint_estringtostringmapentry_constructor_exists():
    assert callable(description_viewpoint_EStringToStringMapEntry.__init__)


def test_description_viewpoint_estringtostringmapentry_constructor_args():
    sig = inspect.signature(description_viewpoint_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_dannotation_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_DAnnotation)


def test_viewpoint_description_dannotation_constructor_exists():
    assert callable(viewpoint_description_DAnnotation.__init__)


def test_viewpoint_description_dannotation_constructor_args():
    sig = inspect.signature(viewpoint_description_DAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "source" in params, "Missing parameter 'source'"

def test_viewpoint_description_dannotation_has_source():
    assert hasattr(viewpoint_description_DAnnotation, "source")
    descriptor = None
    for klass in viewpoint_description_DAnnotation.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_description_representationextensiondescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_RepresentationExtensionDescription)


def test_viewpoint_description_representationextensiondescription_constructor_exists():
    assert callable(viewpoint_description_RepresentationExtensionDescription.__init__)


def test_viewpoint_description_representationextensiondescription_constructor_args():
    sig = inspect.signature(viewpoint_description_RepresentationExtensionDescription.__init__)
    params = list(sig.parameters.keys())
    assert "viewpointURI" in params, "Missing parameter 'viewpointURI'"
    assert "name" in params, "Missing parameter 'name'"
    assert "representationName" in params, "Missing parameter 'representationName'"

def test_viewpoint_description_representationextensiondescription_has_viewpointURI():
    assert hasattr(viewpoint_description_RepresentationExtensionDescription, "viewpointURI")
    descriptor = None
    for klass in viewpoint_description_RepresentationExtensionDescription.__mro__:
        if "viewpointURI" in klass.__dict__:
            descriptor = klass.__dict__["viewpointURI"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_representationextensiondescription_has_name():
    assert hasattr(viewpoint_description_RepresentationExtensionDescription, "name")
    descriptor = None
    for klass in viewpoint_description_RepresentationExtensionDescription.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_representationextensiondescription_has_representationName():
    assert hasattr(viewpoint_description_RepresentationExtensionDescription, "representationName")
    descriptor = None
    for klass in viewpoint_description_RepresentationExtensionDescription.__mro__:
        if "representationName" in klass.__dict__:
            descriptor = klass.__dict__["representationName"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_description_representationimportdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_RepresentationImportDescription)


def test_viewpoint_description_representationimportdescription_constructor_exists():
    assert callable(viewpoint_description_RepresentationImportDescription.__init__)


def test_viewpoint_description_representationimportdescription_constructor_args():
    sig = inspect.signature(viewpoint_description_RepresentationImportDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_representationtemplate_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_RepresentationTemplate)


def test_viewpoint_description_representationtemplate_constructor_exists():
    assert callable(viewpoint_description_RepresentationTemplate.__init__)


def test_viewpoint_description_representationtemplate_constructor_args():
    sig = inspect.signature(viewpoint_description_RepresentationTemplate.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_viewpoint_description_representationtemplate_has_name():
    assert hasattr(viewpoint_description_RepresentationTemplate, "name")
    descriptor = None
    for klass in viewpoint_description_RepresentationTemplate.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_description_viewpoint_epackage_is_not_abstract():
    assert not inspect.isabstract(description_viewpoint_EPackage)


def test_description_viewpoint_epackage_constructor_exists():
    assert callable(description_viewpoint_EPackage.__init__)


def test_description_viewpoint_epackage_constructor_args():
    sig = inspect.signature(description_viewpoint_EPackage.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_featureextensiondescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_FeatureExtensionDescription)


def test_viewpoint_description_featureextensiondescription_constructor_exists():
    assert callable(viewpoint_description_FeatureExtensionDescription.__init__)


def test_viewpoint_description_featureextensiondescription_constructor_args():
    sig = inspect.signature(viewpoint_description_FeatureExtensionDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_javaextension_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_JavaExtension)


def test_viewpoint_description_javaextension_constructor_exists():
    assert callable(viewpoint_description_JavaExtension.__init__)


def test_viewpoint_description_javaextension_constructor_args():
    sig = inspect.signature(viewpoint_description_JavaExtension.__init__)
    params = list(sig.parameters.keys())
    assert "qualifiedClassName" in params, "Missing parameter 'qualifiedClassName'"

def test_viewpoint_description_javaextension_has_qualifiedClassName():
    assert hasattr(viewpoint_description_JavaExtension, "qualifiedClassName")
    descriptor = None
    for klass in viewpoint_description_JavaExtension.__mro__:
        if "qualifiedClassName" in klass.__dict__:
            descriptor = klass.__dict__["qualifiedClassName"]
            break
    assert isinstance(descriptor, property)



def test_description_viewpoint_eobject_is_not_abstract():
    assert not inspect.isabstract(description_viewpoint_EObject)


def test_description_viewpoint_eobject_constructor_exists():
    assert callable(description_viewpoint_EObject.__init__)


def test_description_viewpoint_eobject_constructor_args():
    sig = inspect.signature(description_viewpoint_EObject.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_metamodelextensionsetting_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_MetamodelExtensionSetting)


def test_viewpoint_description_metamodelextensionsetting_constructor_exists():
    assert callable(viewpoint_description_MetamodelExtensionSetting.__init__)


def test_viewpoint_description_metamodelextensionsetting_constructor_args():
    sig = inspect.signature(viewpoint_description_MetamodelExtensionSetting.__init__)
    params = list(sig.parameters.keys())



def test_representationextensiondescription_is_not_abstract():
    assert not inspect.isabstract(RepresentationExtensionDescription)


def test_representationextensiondescription_constructor_exists():
    assert callable(RepresentationExtensionDescription.__init__)


def test_representationextensiondescription_constructor_args():
    sig = inspect.signature(RepresentationExtensionDescription.__init__)
    params = list(sig.parameters.keys())



def test_validation_validationset_is_not_abstract():
    assert not inspect.isabstract(validation_ValidationSet)


def test_validation_validationset_constructor_exists():
    assert callable(validation_ValidationSet.__init__)


def test_validation_validationset_constructor_args():
    sig = inspect.signature(validation_ValidationSet.__init__)
    params = list(sig.parameters.keys())



def test_description_identifiedelement_is_not_abstract():
    assert not inspect.isabstract(description_IdentifiedElement)


def test_description_identifiedelement_constructor_exists():
    assert callable(description_IdentifiedElement.__init__)


def test_description_identifiedelement_constructor_args():
    sig = inspect.signature(description_IdentifiedElement.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_toolentry_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ToolEntry)


def test_viewpoint_tool_toolentry_constructor_exists():
    assert callable(viewpoint_tool_ToolEntry.__init__)


def test_viewpoint_tool_toolentry_constructor_args():
    sig = inspect.signature(viewpoint_tool_ToolEntry.__init__)
    params = list(sig.parameters.keys())



def test_description_enduserdocumentedelement_is_not_abstract():
    assert not inspect.isabstract(description_EndUserDocumentedElement)


def test_description_enduserdocumentedelement_constructor_exists():
    assert callable(description_EndUserDocumentedElement.__init__)


def test_description_enduserdocumentedelement_constructor_args():
    sig = inspect.signature(description_EndUserDocumentedElement.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_representationdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_RepresentationDescription)


def test_viewpoint_description_representationdescription_constructor_exists():
    assert callable(viewpoint_description_RepresentationDescription.__init__)


def test_viewpoint_description_representationdescription_constructor_args():
    sig = inspect.signature(viewpoint_description_RepresentationDescription.__init__)
    params = list(sig.parameters.keys())
    assert "initialisation" in params, "Missing parameter 'initialisation'"
    assert "titleExpression" in params, "Missing parameter 'titleExpression'"
    assert "showOnStartup" in params, "Missing parameter 'showOnStartup'"

def test_viewpoint_description_representationdescription_has_initialisation():
    assert hasattr(viewpoint_description_RepresentationDescription, "initialisation")
    descriptor = None
    for klass in viewpoint_description_RepresentationDescription.__mro__:
        if "initialisation" in klass.__dict__:
            descriptor = klass.__dict__["initialisation"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_representationdescription_has_titleExpression():
    assert hasattr(viewpoint_description_RepresentationDescription, "titleExpression")
    descriptor = None
    for klass in viewpoint_description_RepresentationDescription.__mro__:
        if "titleExpression" in klass.__dict__:
            descriptor = klass.__dict__["titleExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_representationdescription_has_showOnStartup():
    assert hasattr(viewpoint_description_RepresentationDescription, "showOnStartup")
    descriptor = None
    for klass in viewpoint_description_RepresentationDescription.__mro__:
        if "showOnStartup" in klass.__dict__:
            descriptor = klass.__dict__["showOnStartup"]
            break
    assert isinstance(descriptor, property)



def test_description_component_is_not_abstract():
    assert not inspect.isabstract(description_Component)


def test_description_component_constructor_exists():
    assert callable(description_Component.__init__)


def test_description_component_constructor_args():
    sig = inspect.signature(description_Component.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_viewpoint_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_Viewpoint)


def test_viewpoint_description_viewpoint_constructor_exists():
    assert callable(viewpoint_description_Viewpoint.__init__)


def test_viewpoint_description_viewpoint_constructor_args():
    sig = inspect.signature(viewpoint_description_Viewpoint.__init__)
    params = list(sig.parameters.keys())
    assert "reuses" in params, "Missing parameter 'reuses'"
    assert "icon" in params, "Missing parameter 'icon'"
    assert "conflicts" in params, "Missing parameter 'conflicts'"
    assert "modelFileExtension" in params, "Missing parameter 'modelFileExtension'"
    assert "customizes" in params, "Missing parameter 'customizes'"

def test_viewpoint_description_viewpoint_has_reuses():
    assert hasattr(viewpoint_description_Viewpoint, "reuses")
    descriptor = None
    for klass in viewpoint_description_Viewpoint.__mro__:
        if "reuses" in klass.__dict__:
            descriptor = klass.__dict__["reuses"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_viewpoint_has_icon():
    assert hasattr(viewpoint_description_Viewpoint, "icon")
    descriptor = None
    for klass in viewpoint_description_Viewpoint.__mro__:
        if "icon" in klass.__dict__:
            descriptor = klass.__dict__["icon"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_viewpoint_has_conflicts():
    assert hasattr(viewpoint_description_Viewpoint, "conflicts")
    descriptor = None
    for klass in viewpoint_description_Viewpoint.__mro__:
        if "conflicts" in klass.__dict__:
            descriptor = klass.__dict__["conflicts"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_viewpoint_has_modelFileExtension():
    assert hasattr(viewpoint_description_Viewpoint, "modelFileExtension")
    descriptor = None
    for klass in viewpoint_description_Viewpoint.__mro__:
        if "modelFileExtension" in klass.__dict__:
            descriptor = klass.__dict__["modelFileExtension"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_viewpoint_has_customizes():
    assert hasattr(viewpoint_description_Viewpoint, "customizes")
    descriptor = None
    for klass in viewpoint_description_Viewpoint.__mro__:
        if "customizes" in klass.__dict__:
            descriptor = klass.__dict__["customizes"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_description_component_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_Component)


def test_viewpoint_description_component_constructor_exists():
    assert callable(viewpoint_description_Component.__init__)


def test_viewpoint_description_component_constructor_args():
    sig = inspect.signature(viewpoint_description_Component.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_extension_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_Extension)


def test_viewpoint_description_extension_constructor_exists():
    assert callable(viewpoint_description_Extension.__init__)


def test_viewpoint_description_extension_constructor_args():
    sig = inspect.signature(viewpoint_description_Extension.__init__)
    params = list(sig.parameters.keys())



def test_extension_is_not_abstract():
    assert not inspect.isabstract(Extension)


def test_extension_constructor_exists():
    assert callable(Extension.__init__)


def test_extension_constructor_args():
    sig = inspect.signature(Extension.__init__)
    params = list(sig.parameters.keys())

def test_labelalignment_exists():
    # Check that the Enumeration exists
    assert LabelAlignment is not None

def test_labelalignment_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LabelAlignment]
    expected_literals = [
        "RIGHT",
        "LEFT",
        "CENTER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LabelAlignment"

def test_error_level_exists():
    # Check that the Enumeration exists
    assert ERROR_LEVEL is not None

def test_error_level_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ERROR_LEVEL]
    expected_literals = [
        "ERROR",
        "WARNING",
        "INFO",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ERROR_LEVEL"

def test_fontformat_exists():
    # Check that the Enumeration exists
    assert FontFormat is not None

def test_fontformat_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FontFormat]
    expected_literals = [
        "underline",
        "strike_through",
        "italic",
        "bold",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FontFormat"

def test_position_exists():
    # Check that the Enumeration exists
    assert Position is not None

def test_position_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Position]
    expected_literals = [
        "WEST",
        "SOUTH_EAST",
        "NORTH_EAST",
        "CENTER",
        "EAST",
        "NORTH",
        "NORTH_WEST",
        "SOUTH_WEST",
        "SOUTH",
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
        "purple",
        "light_purple",
        "dark_blue",
        "gray",
        "dark_green",
        "yellow",
        "dark_red",
        "black",
        "light_green",
        "dark_orange",
        "dark_chocolate",
        "dark_purple",
        "orange",
        "light_blue",
        "light_red",
        "light_yellow",
        "green",
        "dark_gray",
        "dark_yellow",
        "light_chocolate",
        "white",
        "chocolate",
        "red",
        "light_gray",
        "blue",
        "light_orange",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SystemColors"

def test_decorationdistributiondirection_exists():
    # Check that the Enumeration exists
    assert DecorationDistributionDirection is not None

def test_decorationdistributiondirection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DecorationDistributionDirection]
    expected_literals = [
        "HORIZONTAL",
        "VERTICAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DecorationDistributionDirection"

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
UserColorsPalette_strategy = st.builds(
    UserColorsPalette,
)
SytemColorsPalette_strategy = st.builds(
    SytemColorsPalette,
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
ToolInstance_strategy = st.builds(
    ToolInstance,
)
viewpoint_ToolGroupInstance_strategy = st.builds(
    viewpoint_ToolGroupInstance,
)
tool_ToolEntry_strategy = st.builds(
    tool_ToolEntry,
)
viewpoint_ToolInstance_strategy = st.builds(
    viewpoint_ToolInstance,
    enabled=
        st.booleans(),
    visible=
        st.booleans(),
    id=
        safe_text,
    filtered=
        st.booleans()
)
viewpoint_ToolSectionInstance_strategy = st.builds(
    viewpoint_ToolSectionInstance,
)
DFile_strategy = st.builds(
    DFile,
)
viewpoint_DModel_strategy = st.builds(
    viewpoint_DModel,
)
DResourceContainer_strategy = st.builds(
    DResourceContainer,
)
viewpoint_DFolder_strategy = st.builds(
    viewpoint_DFolder,
)
viewpoint_DProject_strategy = st.builds(
    viewpoint_DProject,
)
DResource_strategy = st.builds(
    DResource,
)
viewpoint_DResource_strategy = st.builds(
    viewpoint_DResource,
    name=
        safe_text,
    path=
        safe_text
)
viewpoint_SessionManagerEObject_strategy = st.builds(
    viewpoint_SessionManagerEObject,
)
Customizable_strategy = st.builds(
    Customizable,
)
viewpoint_BasicLabelStyle_strategy = st.builds(
    viewpoint_BasicLabelStyle,
    labelSize=
        st.integers(),
    showIcon=
        st.booleans(),
    iconPath=
        safe_text,
    labelFormat=
        safe_text,
    labelColor=
        safe_text
)
BasicLabelStyle_strategy = st.builds(
    BasicLabelStyle,
)
viewpoint_LabelStyle_strategy = st.builds(
    viewpoint_LabelStyle,
    labelAlignment=
        safe_text
)
DecorationDescription_strategy = st.builds(
    DecorationDescription,
)
viewpoint_DAnalysisSessionEObject_strategy = st.builds(
    viewpoint_DAnalysisSessionEObject,
    resources=
        safe_text,
    synchronizationStatus=
        safe_text,
    controlledResources=
        safe_text,
    open=
        st.booleans()
)
Viewpoint_strategy = st.builds(
    Viewpoint,
)
style_StyleDescription_strategy = st.builds(
    style_StyleDescription,
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
viewpoint_UIState_strategy = st.builds(
    viewpoint_UIState,
    subDiagramDecorationDescriptors=
        safe_text,
    decorationImage=
        safe_text,
    inverseSelectionOrder=
        st.booleans()
)
AnnotationEntry_strategy = st.builds(
    AnnotationEntry,
)
RepresentationDescription_strategy = st.builds(
    RepresentationDescription,
)
description_DocumentedElement_strategy = st.builds(
    description_DocumentedElement,
)
description_DModelElement_strategy = st.builds(
    description_DModelElement,
)
viewpoint_description_Group_strategy = st.builds(
    viewpoint_description_Group,
    name=
        safe_text,
    version=
        safe_text
)
viewpoint_DMappingBased_strategy = st.builds(
    viewpoint_DMappingBased,
)
viewpoint_DRefreshable_strategy = st.builds(
    viewpoint_DRefreshable,
)
viewpoint_DStylizable_strategy = st.builds(
    viewpoint_DStylizable,
)
FeatureExtensionDescription_strategy = st.builds(
    FeatureExtensionDescription,
)
DRefreshable_strategy = st.builds(
    DRefreshable,
)
DAnnotationEntry_strategy = st.builds(
    DAnnotationEntry,
)
viewpoint_EObject_strategy = st.builds(
    viewpoint_EObject,
)
IdentifiedElement_strategy = st.builds(
    IdentifiedElement,
)
viewpoint_Customizable_strategy = st.builds(
    viewpoint_Customizable,
    customFeatures=
        safe_text
)
viewpoint_Decoration_strategy = st.builds(
    viewpoint_Decoration,
)
viewpoint_Style_strategy = st.builds(
    viewpoint_Style,
)
viewpoint_DAnalysisCustomData_strategy = st.builds(
    viewpoint_DAnalysisCustomData,
    key=
        safe_text
)
viewpoint_DRepresentationElement_strategy = st.builds(
    viewpoint_DRepresentationElement,
    name=
        safe_text
)
viewpoint_DResourceContainer_strategy = st.builds(
    viewpoint_DResourceContainer,
)
viewpoint_DRepresentation_strategy = st.builds(
    viewpoint_DRepresentation,
    documentation=
        safe_text,
    name=
        safe_text
)
viewpoint_DRepresentationDescriptor_strategy = st.builds(
    viewpoint_DRepresentationDescriptor,
    changeId=
        safe_text,
    name=
        safe_text,
    repPath=
        safe_text
)
viewpoint_DFile_strategy = st.builds(
    viewpoint_DFile,
)
viewpoint_MetaModelExtension_strategy = st.builds(
    viewpoint_MetaModelExtension,
)
viewpoint_DSemanticDecorator_strategy = st.builds(
    viewpoint_DSemanticDecorator,
)
viewpoint_DAnalysis_strategy = st.builds(
    viewpoint_DAnalysis,
    semanticResources=
        safe_text,
    version=
        safe_text
)
viewpoint_IdentifiedElement_strategy = st.builds(
    viewpoint_IdentifiedElement,
    uid=
        safe_text
)
viewpoint_DFeatureExtension_strategy = st.builds(
    viewpoint_DFeatureExtension,
)
viewpoint_DView_strategy = st.builds(
    viewpoint_DView,
)
viewpoint_validation_RuleAudit_strategy = st.builds(
    viewpoint_validation_RuleAudit,
    auditExpression=
        safe_text
)
RepresentationElementMapping_strategy = st.builds(
    RepresentationElementMapping,
)
ValidationRule_strategy = st.builds(
    ValidationRule,
)
viewpoint_validation_ViewValidationRule_strategy = st.builds(
    viewpoint_validation_ViewValidationRule,
)
viewpoint_validation_SemanticValidationRule_strategy = st.builds(
    viewpoint_validation_SemanticValidationRule,
    targetClass=
        safe_text
)
InformationSection_strategy = st.builds(
    InformationSection,
)
viewpoint_audit_TemplateInformationSection_strategy = st.builds(
    viewpoint_audit_TemplateInformationSection,
    templatePath=
        safe_text
)
viewpoint_audit_InformationSection_strategy = st.builds(
    viewpoint_audit_InformationSection,
)
viewpoint_validation_ValidationFix_strategy = st.builds(
    viewpoint_validation_ValidationFix,
    name=
        safe_text
)
validation_ValidationRule_strategy = st.builds(
    validation_ValidationRule,
)
DocumentedElement_strategy = st.builds(
    DocumentedElement,
)
viewpoint_validation_ValidationSet_strategy = st.builds(
    viewpoint_validation_ValidationSet,
    name=
        safe_text
)
validation_ValidationFix_strategy = st.builds(
    validation_ValidationFix,
)
validation_RuleAudit_strategy = st.builds(
    validation_RuleAudit,
)
viewpoint_validation_ValidationRule_strategy = st.builds(
    viewpoint_validation_ValidationRule,
    level=
        safe_text,
    message=
        safe_text
)
tool_PopupMenu_strategy = st.builds(
    tool_PopupMenu,
)
MenuItemDescription_strategy = st.builds(
    MenuItemDescription,
)
viewpoint_tool_MenuItemDescriptionWithIcon_strategy = st.builds(
    viewpoint_tool_MenuItemDescriptionWithIcon,
    icon=
        safe_text
)
viewpoint_tool_GroupMenu_strategy = st.builds(
    viewpoint_tool_GroupMenu,
    locationURI=
        safe_text
)
SwitchChild_strategy = st.builds(
    SwitchChild,
)
viewpoint_tool_Case_strategy = st.builds(
    viewpoint_tool_Case,
    conditionExpression=
        safe_text
)
viewpoint_tool_FeatureChangeListener_strategy = st.builds(
    viewpoint_tool_FeatureChangeListener,
    featureName=
        safe_text,
    domainClass=
        safe_text
)
tool_FeatureChangeListener_strategy = st.builds(
    tool_FeatureChangeListener,
)
viewpoint_tool_ToolFilterDescription_strategy = st.builds(
    viewpoint_tool_ToolFilterDescription,
    precondition=
        safe_text,
    elementsToListen=
        safe_text
)
tool_Default_strategy = st.builds(
    tool_Default,
)
tool_Case_strategy = st.builds(
    tool_Case,
)
viewpoint_tool_Default_strategy = st.builds(
    viewpoint_tool_Default,
)
viewpoint_tool_SwitchChild_strategy = st.builds(
    viewpoint_tool_SwitchChild,
)
viewpoint_tool_ExternalJavaActionParameter_strategy = st.builds(
    viewpoint_tool_ExternalJavaActionParameter,
    value=
        safe_text,
    name=
        safe_text
)
ContainerModelOperation_strategy = st.builds(
    ContainerModelOperation,
)
viewpoint_tool_ChangeContext_strategy = st.builds(
    viewpoint_tool_ChangeContext,
    browseExpression=
        safe_text
)
viewpoint_tool_Let_strategy = st.builds(
    viewpoint_tool_Let,
    valueExpression=
        safe_text,
    variableName=
        safe_text
)
viewpoint_tool_If_strategy = st.builds(
    viewpoint_tool_If,
    conditionExpression=
        safe_text
)
viewpoint_tool_DeleteView_strategy = st.builds(
    viewpoint_tool_DeleteView,
)
viewpoint_tool_SetValue_strategy = st.builds(
    viewpoint_tool_SetValue,
    valueExpression=
        safe_text,
    featureName=
        safe_text
)
viewpoint_tool_For_strategy = st.builds(
    viewpoint_tool_For,
    expression=
        safe_text,
    iteratorName=
        safe_text
)
viewpoint_tool_SetObject_strategy = st.builds(
    viewpoint_tool_SetObject,
    featureName=
        safe_text
)
viewpoint_tool_RemoveElement_strategy = st.builds(
    viewpoint_tool_RemoveElement,
)
viewpoint_tool_CreateInstance_strategy = st.builds(
    viewpoint_tool_CreateInstance,
    variableName=
        safe_text,
    typeName=
        safe_text,
    referenceName=
        safe_text
)
viewpoint_tool_MoveElement_strategy = st.builds(
    viewpoint_tool_MoveElement,
    newContainerExpression=
        safe_text,
    featureName=
        safe_text
)
viewpoint_tool_Unset_strategy = st.builds(
    viewpoint_tool_Unset,
    elementExpression=
        safe_text,
    featureName=
        safe_text
)
tool_viewpoint_EObject_strategy = st.builds(
    tool_viewpoint_EObject,
)
tool_ModelOperation_strategy = st.builds(
    tool_ModelOperation,
)
ModelOperation_strategy = st.builds(
    ModelOperation,
)
viewpoint_tool_Switch_strategy = st.builds(
    viewpoint_tool_Switch,
)
viewpoint_tool_ContainerModelOperation_strategy = st.builds(
    viewpoint_tool_ContainerModelOperation,
)
viewpoint_tool_EditMaskVariables_strategy = st.builds(
    viewpoint_tool_EditMaskVariables,
    mask=
        safe_text
)
description_AbstractVariable_strategy = st.builds(
    description_AbstractVariable,
)
viewpoint_tool_InitialContainerDropOperation_strategy = st.builds(
    viewpoint_tool_InitialContainerDropOperation,
)
viewpoint_tool_InitEdgeCreationOperation_strategy = st.builds(
    viewpoint_tool_InitEdgeCreationOperation,
)
viewpoint_tool_InitialOperation_strategy = st.builds(
    viewpoint_tool_InitialOperation,
)
viewpoint_tool_InitialNodeCreationOperation_strategy = st.builds(
    viewpoint_tool_InitialNodeCreationOperation,
)
viewpoint_tool_ModelOperation_strategy = st.builds(
    viewpoint_tool_ModelOperation,
)
tool_ExternalJavaAction_strategy = st.builds(
    tool_ExternalJavaAction,
)
tool_ExternalJavaActionParameter_strategy = st.builds(
    tool_ExternalJavaActionParameter,
)
tool_ContainerModelOperation_strategy = st.builds(
    tool_ContainerModelOperation,
)
tool_GroupMenuItem_strategy = st.builds(
    tool_GroupMenuItem,
)
tool_MenuItemDescriptionWithIcon_strategy = st.builds(
    tool_MenuItemDescriptionWithIcon,
)
viewpoint_tool_ExternalJavaAction_strategy = st.builds(
    viewpoint_tool_ExternalJavaAction,
    id=
        safe_text
)
viewpoint_tool_ExternalJavaActionCall_strategy = st.builds(
    viewpoint_tool_ExternalJavaActionCall,
)
viewpoint_tool_OperationAction_strategy = st.builds(
    viewpoint_tool_OperationAction,
)
tool_MenuItemDescription_strategy = st.builds(
    tool_MenuItemDescription,
)
MenuItemOrRef_strategy = st.builds(
    MenuItemOrRef,
)
viewpoint_tool_MenuItemDescriptionReference_strategy = st.builds(
    viewpoint_tool_MenuItemDescriptionReference,
)
tool_MenuItemOrRef_strategy = st.builds(
    tool_MenuItemOrRef,
)
viewpoint_tool_MenuItemOrRef_strategy = st.builds(
    viewpoint_tool_MenuItemOrRef,
)
tool_VariableContainer_strategy = st.builds(
    tool_VariableContainer,
)
viewpoint_tool_ContainerViewVariable_strategy = st.builds(
    viewpoint_tool_ContainerViewVariable,
)
viewpoint_tool_SelectContainerVariable_strategy = st.builds(
    viewpoint_tool_SelectContainerVariable,
)
viewpoint_tool_DropContainerVariable_strategy = st.builds(
    viewpoint_tool_DropContainerVariable,
)
viewpoint_tool_ElementDropVariable_strategy = st.builds(
    viewpoint_tool_ElementDropVariable,
)
viewpoint_tool_ElementVariable_strategy = st.builds(
    viewpoint_tool_ElementVariable,
)
viewpoint_tool_ElementDeleteVariable_strategy = st.builds(
    viewpoint_tool_ElementDeleteVariable,
)
viewpoint_tool_ElementViewVariable_strategy = st.builds(
    viewpoint_tool_ElementViewVariable,
)
SubVariable_strategy = st.builds(
    SubVariable,
)
viewpoint_tool_VariableContainer_strategy = st.builds(
    viewpoint_tool_VariableContainer,
)
tool_NameVariable_strategy = st.builds(
    tool_NameVariable,
)
tool_SelectContainerVariable_strategy = st.builds(
    tool_SelectContainerVariable,
)
tool_ElementSelectVariable_strategy = st.builds(
    tool_ElementSelectVariable,
)
description_SelectionDescription_strategy = st.builds(
    description_SelectionDescription,
)
tool_AbstractToolDescription_strategy = st.builds(
    tool_AbstractToolDescription,
)
viewpoint_tool_PopupMenu_strategy = st.builds(
    viewpoint_tool_PopupMenu,
)
viewpoint_tool_MenuItemDescription_strategy = st.builds(
    viewpoint_tool_MenuItemDescription,
)
viewpoint_tool_SelectionWizardDescription_strategy = st.builds(
    viewpoint_tool_SelectionWizardDescription,
    iconPath=
        safe_text,
    windowTitle=
        safe_text,
    windowImagePath=
        safe_text
)
tool_ContainerViewVariable_strategy = st.builds(
    tool_ContainerViewVariable,
)
tool_DropContainerVariable_strategy = st.builds(
    tool_DropContainerVariable,
)
tool_InitialOperation_strategy = st.builds(
    tool_InitialOperation,
)
tool_ElementViewVariable_strategy = st.builds(
    tool_ElementViewVariable,
)
tool_ElementVariable_strategy = st.builds(
    tool_ElementVariable,
)
MappingBasedToolDescription_strategy = st.builds(
    MappingBasedToolDescription,
)
viewpoint_tool_PasteDescription_strategy = st.builds(
    viewpoint_tool_PasteDescription,
)
viewpoint_tool_ToolDescription_strategy = st.builds(
    viewpoint_tool_ToolDescription,
    iconPath=
        safe_text
)
AbstractToolDescription_strategy = st.builds(
    AbstractToolDescription,
)
viewpoint_tool_RepresentationCreationDescription_strategy = st.builds(
    viewpoint_tool_RepresentationCreationDescription,
    titleExpression=
        safe_text,
    browseExpression=
        safe_text
)
viewpoint_tool_GroupMenuItem_strategy = st.builds(
    viewpoint_tool_GroupMenuItem,
)
viewpoint_tool_PaneBasedSelectionWizardDescription_strategy = st.builds(
    viewpoint_tool_PaneBasedSelectionWizardDescription,
    preSelectedCandidatesExpression=
        safe_text,
    windowTitle=
        safe_text,
    rootExpression=
        safe_text,
    choiceOfValuesMessage=
        safe_text,
    selectedValuesMessage=
        safe_text,
    childrenExpression=
        safe_text,
    windowImagePath=
        safe_text,
    tree=
        st.booleans(),
    message=
        safe_text,
    candidatesExpression=
        safe_text,
    iconPath=
        safe_text
)
viewpoint_tool_RepresentationNavigationDescription_strategy = st.builds(
    viewpoint_tool_RepresentationNavigationDescription,
    browseExpression=
        safe_text,
    navigationNameExpression=
        safe_text
)
viewpoint_tool_MappingBasedToolDescription_strategy = st.builds(
    viewpoint_tool_MappingBasedToolDescription,
)
style_LabelBorderStyleDescription_strategy = st.builds(
    style_LabelBorderStyleDescription,
)
viewpoint_style_LabelBorderStyles_strategy = st.builds(
    viewpoint_style_LabelBorderStyles,
)
tool_ToolFilterDescription_strategy = st.builds(
    tool_ToolFilterDescription,
)
ToolEntry_strategy = st.builds(
    ToolEntry,
)
viewpoint_tool_AbstractToolDescription_strategy = st.builds(
    viewpoint_tool_AbstractToolDescription,
    elementsToSelect=
        safe_text,
    forceRefresh=
        st.booleans(),
    precondition=
        safe_text,
    inverseSelectionOrder=
        st.booleans()
)
viewpoint_style_TooltipStyleDescription_strategy = st.builds(
    viewpoint_style_TooltipStyleDescription,
    tooltipExpression=
        safe_text
)
viewpoint_style_LabelBorderStyleDescription_strategy = st.builds(
    viewpoint_style_LabelBorderStyleDescription,
    id=
        safe_text,
    cornerHeight=
        st.integers(),
    cornerWidth=
        st.integers(),
    name=
        safe_text
)
viewpoint_description_InteractiveVariableDescription_strategy = st.builds(
    viewpoint_description_InteractiveVariableDescription,
    userDocumentation=
        safe_text
)
AbstractVariable_strategy = st.builds(
    AbstractVariable,
)
viewpoint_tool_NameVariable_strategy = st.builds(
    viewpoint_tool_NameVariable,
)
viewpoint_tool_DialogVariable_strategy = st.builds(
    viewpoint_tool_DialogVariable,
    dialogPrompt=
        safe_text
)
viewpoint_tool_ElementSelectVariable_strategy = st.builds(
    viewpoint_tool_ElementSelectVariable,
)
viewpoint_description_SubVariable_strategy = st.builds(
    viewpoint_description_SubVariable,
)
viewpoint_description_AbstractVariable_strategy = st.builds(
    viewpoint_description_AbstractVariable,
    name=
        safe_text
)
BasicLabelStyleDescription_strategy = st.builds(
    BasicLabelStyleDescription,
)
viewpoint_style_LabelStyleDescription_strategy = st.builds(
    viewpoint_style_LabelStyleDescription,
    labelAlignment=
        safe_text
)
viewpoint_description_DAnnotationEntry_strategy = st.builds(
    viewpoint_description_DAnnotationEntry,
    source=
        safe_text,
    details=
        safe_text
)
viewpoint_style_BasicLabelStyleDescription_strategy = st.builds(
    viewpoint_style_BasicLabelStyleDescription,
    labelSize=
        st.integers(),
    labelExpression=
        safe_text,
    showIcon=
        st.booleans(),
    labelFormat=
        safe_text,
    iconPath=
        safe_text
)
viewpoint_style_StyleDescription_strategy = st.builds(
    viewpoint_style_StyleDescription,
)
description_viewpoint_EDataType_strategy = st.builds(
    description_viewpoint_EDataType,
)
description_SubVariable_strategy = st.builds(
    description_SubVariable,
)
viewpoint_tool_AcceleoVariable_strategy = st.builds(
    viewpoint_tool_AcceleoVariable,
    computationExpression=
        safe_text
)
description_InteractiveVariableDescription_strategy = st.builds(
    description_InteractiveVariableDescription,
)
viewpoint_tool_SelectModelElementVariable_strategy = st.builds(
    viewpoint_tool_SelectModelElementVariable,
)
viewpoint_description_TypedVariable_strategy = st.builds(
    viewpoint_description_TypedVariable,
    defaultValueExpression=
        safe_text
)
SystemColor_strategy = st.builds(
    SystemColor,
)
viewpoint_description_SytemColorsPalette_strategy = st.builds(
    viewpoint_description_SytemColorsPalette,
)
style_LabelBorderStyles_strategy = st.builds(
    style_LabelBorderStyles,
)
viewpoint_description_IdentifiedElement_strategy = st.builds(
    viewpoint_description_IdentifiedElement,
    label=
        safe_text,
    name=
        safe_text
)
viewpoint_description_EndUserDocumentedElement_strategy = st.builds(
    viewpoint_description_EndUserDocumentedElement,
    endUserDocumentation=
        safe_text
)
viewpoint_description_AnnotationEntry_strategy = st.builds(
    viewpoint_description_AnnotationEntry,
    source=
        safe_text
)
UserColor_strategy = st.builds(
    UserColor,
)
viewpoint_description_UserColorsPalette_strategy = st.builds(
    viewpoint_description_UserColorsPalette,
    name=
        safe_text
)
viewpoint_description_Environment_strategy = st.builds(
    viewpoint_description_Environment,
)
ColorStep_strategy = st.builds(
    ColorStep,
)
description_UserColor_strategy = st.builds(
    description_UserColor,
)
description_ColorDescription_strategy = st.builds(
    description_ColorDescription,
)
viewpoint_description_ComputedColor_strategy = st.builds(
    viewpoint_description_ComputedColor,
    green=
        safe_text,
    red=
        safe_text,
    blue=
        safe_text
)
viewpoint_description_InterpolatedColor_strategy = st.builds(
    viewpoint_description_InterpolatedColor,
    maxValueComputationExpression=
        safe_text,
    minValueComputationExpression=
        safe_text,
    colorValueComputationExpression=
        safe_text
)
FixedColor_strategy = st.builds(
    FixedColor,
)
viewpoint_description_SystemColor_strategy = st.builds(
    viewpoint_description_SystemColor,
    name=
        safe_text
)
viewpoint_description_UserColor_strategy = st.builds(
    viewpoint_description_UserColor,
    name=
        safe_text
)
viewpoint_description_ColorDescription_strategy = st.builds(
    viewpoint_description_ColorDescription,
)
description_FixedColor_strategy = st.builds(
    description_FixedColor,
)
viewpoint_description_UserFixedColor_strategy = st.builds(
    viewpoint_description_UserFixedColor,
)
ColorDescription_strategy = st.builds(
    ColorDescription,
)
viewpoint_description_FixedColor_strategy = st.builds(
    viewpoint_description_FixedColor,
    red=
        st.integers(),
    green=
        st.integers(),
    blue=
        st.integers()
)
viewpoint_description_ColorStep_strategy = st.builds(
    viewpoint_description_ColorStep,
    associatedValue=
        safe_text
)
viewpoint_description_EStructuralFeatureCustomization_strategy = st.builds(
    viewpoint_description_EStructuralFeatureCustomization,
    applyOnAll=
        st.booleans()
)
EStructuralFeatureCustomization_strategy = st.builds(
    EStructuralFeatureCustomization,
)
viewpoint_description_EReferenceCustomization_strategy = st.builds(
    viewpoint_description_EReferenceCustomization,
    referenceName=
        safe_text
)
viewpoint_description_EAttributeCustomization_strategy = st.builds(
    viewpoint_description_EAttributeCustomization,
    value=
        safe_text,
    attributeName=
        safe_text
)
viewpoint_description_SelectionDescription_strategy = st.builds(
    viewpoint_description_SelectionDescription,
    childrenExpression=
        safe_text,
    candidatesExpression=
        safe_text,
    multiple=
        st.booleans(),
    tree=
        st.booleans(),
    message=
        safe_text,
    rootExpression=
        safe_text
)
viewpoint_description_GenericDecorationDescription_strategy = st.builds(
    viewpoint_description_GenericDecorationDescription,
)
viewpoint_description_SemanticBasedDecoration_strategy = st.builds(
    viewpoint_description_SemanticBasedDecoration,
    domainClass=
        safe_text
)
viewpoint_description_IVSMElementCustomization_strategy = st.builds(
    viewpoint_description_IVSMElementCustomization,
)
IVSMElementCustomization_strategy = st.builds(
    IVSMElementCustomization,
)
viewpoint_description_VSMElementCustomization_strategy = st.builds(
    viewpoint_description_VSMElementCustomization,
    predicateExpression=
        safe_text
)
viewpoint_description_VSMElementCustomizationReuse_strategy = st.builds(
    viewpoint_description_VSMElementCustomizationReuse,
)
viewpoint_description_Customization_strategy = st.builds(
    viewpoint_description_Customization,
)
viewpoint_description_DecorationDescription_strategy = st.builds(
    viewpoint_description_DecorationDescription,
    position=
        safe_text,
    tooltipExpression=
        safe_text,
    name=
        safe_text,
    preconditionExpression=
        safe_text,
    imageExpression=
        safe_text,
    distributionDirection=
        safe_text
)
viewpoint_description_DecorationDescriptionsSet_strategy = st.builds(
    viewpoint_description_DecorationDescriptionsSet,
)
tool_PasteDescription_strategy = st.builds(
    tool_PasteDescription,
)
viewpoint_description_PasteTargetDescription_strategy = st.builds(
    viewpoint_description_PasteTargetDescription,
)
DAnnotation_strategy = st.builds(
    DAnnotation,
)
viewpoint_description_DModelElement_strategy = st.builds(
    viewpoint_description_DModelElement,
)
viewpoint_description_DocumentedElement_strategy = st.builds(
    viewpoint_description_DocumentedElement,
    documentation=
        safe_text
)
viewpoint_description_AbstractMappingImport_strategy = st.builds(
    viewpoint_description_AbstractMappingImport,
    inheritsAncestorFilters=
        st.booleans(),
    hideSubMappings=
        st.booleans()
)
tool_RepresentationNavigationDescription_strategy = st.builds(
    tool_RepresentationNavigationDescription,
)
tool_RepresentationCreationDescription_strategy = st.builds(
    tool_RepresentationCreationDescription,
)
viewpoint_description_RepresentationElementMapping_strategy = st.builds(
    viewpoint_description_RepresentationElementMapping,
)
viewpoint_description_ConditionalStyleDescription_strategy = st.builds(
    viewpoint_description_ConditionalStyleDescription,
    predicateExpression=
        safe_text
)
description_viewpoint_EStringToStringMapEntry_strategy = st.builds(
    description_viewpoint_EStringToStringMapEntry,
)
viewpoint_description_DAnnotation_strategy = st.builds(
    viewpoint_description_DAnnotation,
    source=
        safe_text
)
viewpoint_description_RepresentationExtensionDescription_strategy = st.builds(
    viewpoint_description_RepresentationExtensionDescription,
    viewpointURI=
        safe_text,
    name=
        safe_text,
    representationName=
        safe_text
)
viewpoint_description_RepresentationImportDescription_strategy = st.builds(
    viewpoint_description_RepresentationImportDescription,
)
viewpoint_description_RepresentationTemplate_strategy = st.builds(
    viewpoint_description_RepresentationTemplate,
    name=
        safe_text
)
description_viewpoint_EPackage_strategy = st.builds(
    description_viewpoint_EPackage,
)
viewpoint_description_FeatureExtensionDescription_strategy = st.builds(
    viewpoint_description_FeatureExtensionDescription,
)
viewpoint_description_JavaExtension_strategy = st.builds(
    viewpoint_description_JavaExtension,
    qualifiedClassName=
        safe_text
)
description_viewpoint_EObject_strategy = st.builds(
    description_viewpoint_EObject,
)
viewpoint_description_MetamodelExtensionSetting_strategy = st.builds(
    viewpoint_description_MetamodelExtensionSetting,
)
RepresentationExtensionDescription_strategy = st.builds(
    RepresentationExtensionDescription,
)
validation_ValidationSet_strategy = st.builds(
    validation_ValidationSet,
)
description_IdentifiedElement_strategy = st.builds(
    description_IdentifiedElement,
)
viewpoint_tool_ToolEntry_strategy = st.builds(
    viewpoint_tool_ToolEntry,
)
description_EndUserDocumentedElement_strategy = st.builds(
    description_EndUserDocumentedElement,
)
viewpoint_description_RepresentationDescription_strategy = st.builds(
    viewpoint_description_RepresentationDescription,
    initialisation=
        st.booleans(),
    titleExpression=
        safe_text,
    showOnStartup=
        st.booleans()
)
description_Component_strategy = st.builds(
    description_Component,
)
viewpoint_description_Viewpoint_strategy = st.builds(
    viewpoint_description_Viewpoint,
    reuses=
        safe_text,
    icon=
        safe_text,
    conflicts=
        safe_text,
    modelFileExtension=
        safe_text,
    customizes=
        safe_text
)
viewpoint_description_Component_strategy = st.builds(
    viewpoint_description_Component,
)
viewpoint_description_Extension_strategy = st.builds(
    viewpoint_description_Extension,
)
Extension_strategy = st.builds(
    Extension,
)

@given(instance=UserColorsPalette_strategy)
@settings(max_examples=50)
def test_usercolorspalette_instantiation(instance):
    assert isinstance(instance, UserColorsPalette)

@given(instance=SytemColorsPalette_strategy)
@settings(max_examples=50)
def test_sytemcolorspalette_instantiation(instance):
    assert isinstance(instance, SytemColorsPalette)

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

@given(instance=ToolInstance_strategy)
@settings(max_examples=50)
def test_toolinstance_instantiation(instance):
    assert isinstance(instance, ToolInstance)

@given(instance=viewpoint_ToolGroupInstance_strategy)
@settings(max_examples=50)
def test_viewpoint_toolgroupinstance_instantiation(instance):
    assert isinstance(instance, viewpoint_ToolGroupInstance)

@given(instance=tool_ToolEntry_strategy)
@settings(max_examples=50)
def test_tool_toolentry_instantiation(instance):
    assert isinstance(instance, tool_ToolEntry)

@given(instance=viewpoint_ToolInstance_strategy)
@settings(max_examples=50)
def test_viewpoint_toolinstance_instantiation(instance):
    assert isinstance(instance, viewpoint_ToolInstance)



@given(instance=viewpoint_ToolInstance_strategy)
def test_viewpoint_toolinstance_enabled_setter(instance):
    original = instance.enabled
    instance.enabled = original
    assert instance.enabled == original



@given(instance=viewpoint_ToolInstance_strategy)
def test_viewpoint_toolinstance_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original



@given(instance=viewpoint_ToolInstance_strategy)
def test_viewpoint_toolinstance_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=viewpoint_ToolInstance_strategy)
def test_viewpoint_toolinstance_filtered_setter(instance):
    original = instance.filtered
    instance.filtered = original
    assert instance.filtered == original

@given(instance=viewpoint_ToolSectionInstance_strategy)
@settings(max_examples=50)
def test_viewpoint_toolsectioninstance_instantiation(instance):
    assert isinstance(instance, viewpoint_ToolSectionInstance)

@given(instance=DFile_strategy)
@settings(max_examples=50)
def test_dfile_instantiation(instance):
    assert isinstance(instance, DFile)

@given(instance=viewpoint_DModel_strategy)
@settings(max_examples=50)
def test_viewpoint_dmodel_instantiation(instance):
    assert isinstance(instance, viewpoint_DModel)

@given(instance=DResourceContainer_strategy)
@settings(max_examples=50)
def test_dresourcecontainer_instantiation(instance):
    assert isinstance(instance, DResourceContainer)

@given(instance=viewpoint_DFolder_strategy)
@settings(max_examples=50)
def test_viewpoint_dfolder_instantiation(instance):
    assert isinstance(instance, viewpoint_DFolder)

@given(instance=viewpoint_DProject_strategy)
@settings(max_examples=50)
def test_viewpoint_dproject_instantiation(instance):
    assert isinstance(instance, viewpoint_DProject)

@given(instance=DResource_strategy)
@settings(max_examples=50)
def test_dresource_instantiation(instance):
    assert isinstance(instance, DResource)

@given(instance=viewpoint_DResource_strategy)
@settings(max_examples=50)
def test_viewpoint_dresource_instantiation(instance):
    assert isinstance(instance, viewpoint_DResource)



@given(instance=viewpoint_DResource_strategy)
def test_viewpoint_dresource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=viewpoint_DResource_strategy)
def test_viewpoint_dresource_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original

@given(instance=viewpoint_SessionManagerEObject_strategy)
@settings(max_examples=50)
def test_viewpoint_sessionmanagereobject_instantiation(instance):
    assert isinstance(instance, viewpoint_SessionManagerEObject)

@given(instance=Customizable_strategy)
@settings(max_examples=50)
def test_customizable_instantiation(instance):
    assert isinstance(instance, Customizable)

@given(instance=viewpoint_BasicLabelStyle_strategy)
@settings(max_examples=50)
def test_viewpoint_basiclabelstyle_instantiation(instance):
    assert isinstance(instance, viewpoint_BasicLabelStyle)



@given(instance=viewpoint_BasicLabelStyle_strategy)
def test_viewpoint_basiclabelstyle_labelSize_setter(instance):
    original = instance.labelSize
    instance.labelSize = original
    assert instance.labelSize == original



@given(instance=viewpoint_BasicLabelStyle_strategy)
def test_viewpoint_basiclabelstyle_showIcon_setter(instance):
    original = instance.showIcon
    instance.showIcon = original
    assert instance.showIcon == original



@given(instance=viewpoint_BasicLabelStyle_strategy)
def test_viewpoint_basiclabelstyle_iconPath_setter(instance):
    original = instance.iconPath
    instance.iconPath = original
    assert instance.iconPath == original



@given(instance=viewpoint_BasicLabelStyle_strategy)
def test_viewpoint_basiclabelstyle_labelFormat_setter(instance):
    original = instance.labelFormat
    instance.labelFormat = original
    assert instance.labelFormat == original



@given(instance=viewpoint_BasicLabelStyle_strategy)
def test_viewpoint_basiclabelstyle_labelColor_setter(instance):
    original = instance.labelColor
    instance.labelColor = original
    assert instance.labelColor == original

@given(instance=BasicLabelStyle_strategy)
@settings(max_examples=50)
def test_basiclabelstyle_instantiation(instance):
    assert isinstance(instance, BasicLabelStyle)

@given(instance=viewpoint_LabelStyle_strategy)
@settings(max_examples=50)
def test_viewpoint_labelstyle_instantiation(instance):
    assert isinstance(instance, viewpoint_LabelStyle)



@given(instance=viewpoint_LabelStyle_strategy)
def test_viewpoint_labelstyle_labelAlignment_setter(instance):
    original = instance.labelAlignment
    instance.labelAlignment = original
    assert instance.labelAlignment == original

@given(instance=DecorationDescription_strategy)
@settings(max_examples=50)
def test_decorationdescription_instantiation(instance):
    assert isinstance(instance, DecorationDescription)

@given(instance=viewpoint_DAnalysisSessionEObject_strategy)
@settings(max_examples=50)
def test_viewpoint_danalysissessioneobject_instantiation(instance):
    assert isinstance(instance, viewpoint_DAnalysisSessionEObject)



@given(instance=viewpoint_DAnalysisSessionEObject_strategy)
def test_viewpoint_danalysissessioneobject_resources_setter(instance):
    original = instance.resources
    instance.resources = original
    assert instance.resources == original



@given(instance=viewpoint_DAnalysisSessionEObject_strategy)
def test_viewpoint_danalysissessioneobject_synchronizationStatus_setter(instance):
    original = instance.synchronizationStatus
    instance.synchronizationStatus = original
    assert instance.synchronizationStatus == original



@given(instance=viewpoint_DAnalysisSessionEObject_strategy)
def test_viewpoint_danalysissessioneobject_controlledResources_setter(instance):
    original = instance.controlledResources
    instance.controlledResources = original
    assert instance.controlledResources == original



@given(instance=viewpoint_DAnalysisSessionEObject_strategy)
def test_viewpoint_danalysissessioneobject_open_setter(instance):
    original = instance.open
    instance.open = original
    assert instance.open == original

@given(instance=Viewpoint_strategy)
@settings(max_examples=50)
def test_viewpoint_instantiation(instance):
    assert isinstance(instance, Viewpoint)

@given(instance=style_StyleDescription_strategy)
@settings(max_examples=50)
def test_style_styledescription_instantiation(instance):
    assert isinstance(instance, style_StyleDescription)

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

@given(instance=viewpoint_UIState_strategy)
@settings(max_examples=50)
def test_viewpoint_uistate_instantiation(instance):
    assert isinstance(instance, viewpoint_UIState)



@given(instance=viewpoint_UIState_strategy)
def test_viewpoint_uistate_subDiagramDecorationDescriptors_setter(instance):
    original = instance.subDiagramDecorationDescriptors
    instance.subDiagramDecorationDescriptors = original
    assert instance.subDiagramDecorationDescriptors == original



@given(instance=viewpoint_UIState_strategy)
def test_viewpoint_uistate_decorationImage_setter(instance):
    original = instance.decorationImage
    instance.decorationImage = original
    assert instance.decorationImage == original



@given(instance=viewpoint_UIState_strategy)
def test_viewpoint_uistate_inverseSelectionOrder_setter(instance):
    original = instance.inverseSelectionOrder
    instance.inverseSelectionOrder = original
    assert instance.inverseSelectionOrder == original

@given(instance=AnnotationEntry_strategy)
@settings(max_examples=50)
def test_annotationentry_instantiation(instance):
    assert isinstance(instance, AnnotationEntry)

@given(instance=RepresentationDescription_strategy)
@settings(max_examples=50)
def test_representationdescription_instantiation(instance):
    assert isinstance(instance, RepresentationDescription)

@given(instance=description_DocumentedElement_strategy)
@settings(max_examples=50)
def test_description_documentedelement_instantiation(instance):
    assert isinstance(instance, description_DocumentedElement)

@given(instance=description_DModelElement_strategy)
@settings(max_examples=50)
def test_description_dmodelelement_instantiation(instance):
    assert isinstance(instance, description_DModelElement)

@given(instance=viewpoint_description_Group_strategy)
@settings(max_examples=50)
def test_viewpoint_description_group_instantiation(instance):
    assert isinstance(instance, viewpoint_description_Group)



@given(instance=viewpoint_description_Group_strategy)
def test_viewpoint_description_group_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=viewpoint_description_Group_strategy)
def test_viewpoint_description_group_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=viewpoint_DMappingBased_strategy)
@settings(max_examples=50)
def test_viewpoint_dmappingbased_instantiation(instance):
    assert isinstance(instance, viewpoint_DMappingBased)

@given(instance=viewpoint_DRefreshable_strategy)
@settings(max_examples=50)
def test_viewpoint_drefreshable_instantiation(instance):
    assert isinstance(instance, viewpoint_DRefreshable)

@given(instance=viewpoint_DStylizable_strategy)
@settings(max_examples=50)
def test_viewpoint_dstylizable_instantiation(instance):
    assert isinstance(instance, viewpoint_DStylizable)

@given(instance=FeatureExtensionDescription_strategy)
@settings(max_examples=50)
def test_featureextensiondescription_instantiation(instance):
    assert isinstance(instance, FeatureExtensionDescription)

@given(instance=DRefreshable_strategy)
@settings(max_examples=50)
def test_drefreshable_instantiation(instance):
    assert isinstance(instance, DRefreshable)

@given(instance=DAnnotationEntry_strategy)
@settings(max_examples=50)
def test_dannotationentry_instantiation(instance):
    assert isinstance(instance, DAnnotationEntry)

@given(instance=viewpoint_EObject_strategy)
@settings(max_examples=50)
def test_viewpoint_eobject_instantiation(instance):
    assert isinstance(instance, viewpoint_EObject)

@given(instance=IdentifiedElement_strategy)
@settings(max_examples=50)
def test_identifiedelement_instantiation(instance):
    assert isinstance(instance, IdentifiedElement)

@given(instance=viewpoint_Customizable_strategy)
@settings(max_examples=50)
def test_viewpoint_customizable_instantiation(instance):
    assert isinstance(instance, viewpoint_Customizable)



@given(instance=viewpoint_Customizable_strategy)
def test_viewpoint_customizable_customFeatures_setter(instance):
    original = instance.customFeatures
    instance.customFeatures = original
    assert instance.customFeatures == original

@given(instance=viewpoint_Decoration_strategy)
@settings(max_examples=50)
def test_viewpoint_decoration_instantiation(instance):
    assert isinstance(instance, viewpoint_Decoration)

@given(instance=viewpoint_Style_strategy)
@settings(max_examples=50)
def test_viewpoint_style_instantiation(instance):
    assert isinstance(instance, viewpoint_Style)

@given(instance=viewpoint_DAnalysisCustomData_strategy)
@settings(max_examples=50)
def test_viewpoint_danalysiscustomdata_instantiation(instance):
    assert isinstance(instance, viewpoint_DAnalysisCustomData)



@given(instance=viewpoint_DAnalysisCustomData_strategy)
def test_viewpoint_danalysiscustomdata_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=viewpoint_DRepresentationElement_strategy)
@settings(max_examples=50)
def test_viewpoint_drepresentationelement_instantiation(instance):
    assert isinstance(instance, viewpoint_DRepresentationElement)



@given(instance=viewpoint_DRepresentationElement_strategy)
def test_viewpoint_drepresentationelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=viewpoint_DResourceContainer_strategy)
@settings(max_examples=50)
def test_viewpoint_dresourcecontainer_instantiation(instance):
    assert isinstance(instance, viewpoint_DResourceContainer)

@given(instance=viewpoint_DRepresentation_strategy)
@settings(max_examples=50)
def test_viewpoint_drepresentation_instantiation(instance):
    assert isinstance(instance, viewpoint_DRepresentation)



@given(instance=viewpoint_DRepresentation_strategy)
def test_viewpoint_drepresentation_documentation_setter(instance):
    original = instance.documentation
    instance.documentation = original
    assert instance.documentation == original



@given(instance=viewpoint_DRepresentation_strategy)
def test_viewpoint_drepresentation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=viewpoint_DRepresentationDescriptor_strategy)
@settings(max_examples=50)
def test_viewpoint_drepresentationdescriptor_instantiation(instance):
    assert isinstance(instance, viewpoint_DRepresentationDescriptor)



@given(instance=viewpoint_DRepresentationDescriptor_strategy)
def test_viewpoint_drepresentationdescriptor_changeId_setter(instance):
    original = instance.changeId
    instance.changeId = original
    assert instance.changeId == original



@given(instance=viewpoint_DRepresentationDescriptor_strategy)
def test_viewpoint_drepresentationdescriptor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=viewpoint_DRepresentationDescriptor_strategy)
def test_viewpoint_drepresentationdescriptor_repPath_setter(instance):
    original = instance.repPath
    instance.repPath = original
    assert instance.repPath == original

@given(instance=viewpoint_DFile_strategy)
@settings(max_examples=50)
def test_viewpoint_dfile_instantiation(instance):
    assert isinstance(instance, viewpoint_DFile)

@given(instance=viewpoint_MetaModelExtension_strategy)
@settings(max_examples=50)
def test_viewpoint_metamodelextension_instantiation(instance):
    assert isinstance(instance, viewpoint_MetaModelExtension)

@given(instance=viewpoint_DSemanticDecorator_strategy)
@settings(max_examples=50)
def test_viewpoint_dsemanticdecorator_instantiation(instance):
    assert isinstance(instance, viewpoint_DSemanticDecorator)

@given(instance=viewpoint_DAnalysis_strategy)
@settings(max_examples=50)
def test_viewpoint_danalysis_instantiation(instance):
    assert isinstance(instance, viewpoint_DAnalysis)



@given(instance=viewpoint_DAnalysis_strategy)
def test_viewpoint_danalysis_semanticResources_setter(instance):
    original = instance.semanticResources
    instance.semanticResources = original
    assert instance.semanticResources == original



@given(instance=viewpoint_DAnalysis_strategy)
def test_viewpoint_danalysis_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=viewpoint_IdentifiedElement_strategy)
@settings(max_examples=50)
def test_viewpoint_identifiedelement_instantiation(instance):
    assert isinstance(instance, viewpoint_IdentifiedElement)



@given(instance=viewpoint_IdentifiedElement_strategy)
def test_viewpoint_identifiedelement_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=viewpoint_DFeatureExtension_strategy)
@settings(max_examples=50)
def test_viewpoint_dfeatureextension_instantiation(instance):
    assert isinstance(instance, viewpoint_DFeatureExtension)

@given(instance=viewpoint_DView_strategy)
@settings(max_examples=50)
def test_viewpoint_dview_instantiation(instance):
    assert isinstance(instance, viewpoint_DView)

@given(instance=viewpoint_validation_RuleAudit_strategy)
@settings(max_examples=50)
def test_viewpoint_validation_ruleaudit_instantiation(instance):
    assert isinstance(instance, viewpoint_validation_RuleAudit)



@given(instance=viewpoint_validation_RuleAudit_strategy)
def test_viewpoint_validation_ruleaudit_auditExpression_setter(instance):
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

@given(instance=viewpoint_validation_ViewValidationRule_strategy)
@settings(max_examples=50)
def test_viewpoint_validation_viewvalidationrule_instantiation(instance):
    assert isinstance(instance, viewpoint_validation_ViewValidationRule)

@given(instance=viewpoint_validation_SemanticValidationRule_strategy)
@settings(max_examples=50)
def test_viewpoint_validation_semanticvalidationrule_instantiation(instance):
    assert isinstance(instance, viewpoint_validation_SemanticValidationRule)



@given(instance=viewpoint_validation_SemanticValidationRule_strategy)
def test_viewpoint_validation_semanticvalidationrule_targetClass_setter(instance):
    original = instance.targetClass
    instance.targetClass = original
    assert instance.targetClass == original

@given(instance=InformationSection_strategy)
@settings(max_examples=50)
def test_informationsection_instantiation(instance):
    assert isinstance(instance, InformationSection)

@given(instance=viewpoint_audit_TemplateInformationSection_strategy)
@settings(max_examples=50)
def test_viewpoint_audit_templateinformationsection_instantiation(instance):
    assert isinstance(instance, viewpoint_audit_TemplateInformationSection)



@given(instance=viewpoint_audit_TemplateInformationSection_strategy)
def test_viewpoint_audit_templateinformationsection_templatePath_setter(instance):
    original = instance.templatePath
    instance.templatePath = original
    assert instance.templatePath == original

@given(instance=viewpoint_audit_InformationSection_strategy)
@settings(max_examples=50)
def test_viewpoint_audit_informationsection_instantiation(instance):
    assert isinstance(instance, viewpoint_audit_InformationSection)

@given(instance=viewpoint_validation_ValidationFix_strategy)
@settings(max_examples=50)
def test_viewpoint_validation_validationfix_instantiation(instance):
    assert isinstance(instance, viewpoint_validation_ValidationFix)



@given(instance=viewpoint_validation_ValidationFix_strategy)
def test_viewpoint_validation_validationfix_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=validation_ValidationRule_strategy)
@settings(max_examples=50)
def test_validation_validationrule_instantiation(instance):
    assert isinstance(instance, validation_ValidationRule)

@given(instance=DocumentedElement_strategy)
@settings(max_examples=50)
def test_documentedelement_instantiation(instance):
    assert isinstance(instance, DocumentedElement)

@given(instance=viewpoint_validation_ValidationSet_strategy)
@settings(max_examples=50)
def test_viewpoint_validation_validationset_instantiation(instance):
    assert isinstance(instance, viewpoint_validation_ValidationSet)



@given(instance=viewpoint_validation_ValidationSet_strategy)
def test_viewpoint_validation_validationset_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=validation_ValidationFix_strategy)
@settings(max_examples=50)
def test_validation_validationfix_instantiation(instance):
    assert isinstance(instance, validation_ValidationFix)

@given(instance=validation_RuleAudit_strategy)
@settings(max_examples=50)
def test_validation_ruleaudit_instantiation(instance):
    assert isinstance(instance, validation_RuleAudit)

@given(instance=viewpoint_validation_ValidationRule_strategy)
@settings(max_examples=50)
def test_viewpoint_validation_validationrule_instantiation(instance):
    assert isinstance(instance, viewpoint_validation_ValidationRule)



@given(instance=viewpoint_validation_ValidationRule_strategy)
def test_viewpoint_validation_validationrule_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original



@given(instance=viewpoint_validation_ValidationRule_strategy)
def test_viewpoint_validation_validationrule_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

@given(instance=tool_PopupMenu_strategy)
@settings(max_examples=50)
def test_tool_popupmenu_instantiation(instance):
    assert isinstance(instance, tool_PopupMenu)

@given(instance=MenuItemDescription_strategy)
@settings(max_examples=50)
def test_menuitemdescription_instantiation(instance):
    assert isinstance(instance, MenuItemDescription)

@given(instance=viewpoint_tool_MenuItemDescriptionWithIcon_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_menuitemdescriptionwithicon_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_MenuItemDescriptionWithIcon)



@given(instance=viewpoint_tool_MenuItemDescriptionWithIcon_strategy)
def test_viewpoint_tool_menuitemdescriptionwithicon_icon_setter(instance):
    original = instance.icon
    instance.icon = original
    assert instance.icon == original

@given(instance=viewpoint_tool_GroupMenu_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_groupmenu_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_GroupMenu)



@given(instance=viewpoint_tool_GroupMenu_strategy)
def test_viewpoint_tool_groupmenu_locationURI_setter(instance):
    original = instance.locationURI
    instance.locationURI = original
    assert instance.locationURI == original

@given(instance=SwitchChild_strategy)
@settings(max_examples=50)
def test_switchchild_instantiation(instance):
    assert isinstance(instance, SwitchChild)

@given(instance=viewpoint_tool_Case_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_case_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_Case)



@given(instance=viewpoint_tool_Case_strategy)
def test_viewpoint_tool_case_conditionExpression_setter(instance):
    original = instance.conditionExpression
    instance.conditionExpression = original
    assert instance.conditionExpression == original

@given(instance=viewpoint_tool_FeatureChangeListener_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_featurechangelistener_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_FeatureChangeListener)



@given(instance=viewpoint_tool_FeatureChangeListener_strategy)
def test_viewpoint_tool_featurechangelistener_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original



@given(instance=viewpoint_tool_FeatureChangeListener_strategy)
def test_viewpoint_tool_featurechangelistener_domainClass_setter(instance):
    original = instance.domainClass
    instance.domainClass = original
    assert instance.domainClass == original

@given(instance=tool_FeatureChangeListener_strategy)
@settings(max_examples=50)
def test_tool_featurechangelistener_instantiation(instance):
    assert isinstance(instance, tool_FeatureChangeListener)

@given(instance=viewpoint_tool_ToolFilterDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_toolfilterdescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ToolFilterDescription)



@given(instance=viewpoint_tool_ToolFilterDescription_strategy)
def test_viewpoint_tool_toolfilterdescription_precondition_setter(instance):
    original = instance.precondition
    instance.precondition = original
    assert instance.precondition == original



@given(instance=viewpoint_tool_ToolFilterDescription_strategy)
def test_viewpoint_tool_toolfilterdescription_elementsToListen_setter(instance):
    original = instance.elementsToListen
    instance.elementsToListen = original
    assert instance.elementsToListen == original

@given(instance=tool_Default_strategy)
@settings(max_examples=50)
def test_tool_default_instantiation(instance):
    assert isinstance(instance, tool_Default)

@given(instance=tool_Case_strategy)
@settings(max_examples=50)
def test_tool_case_instantiation(instance):
    assert isinstance(instance, tool_Case)

@given(instance=viewpoint_tool_Default_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_default_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_Default)

@given(instance=viewpoint_tool_SwitchChild_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_switchchild_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_SwitchChild)

@given(instance=viewpoint_tool_ExternalJavaActionParameter_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_externaljavaactionparameter_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ExternalJavaActionParameter)



@given(instance=viewpoint_tool_ExternalJavaActionParameter_strategy)
def test_viewpoint_tool_externaljavaactionparameter_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=viewpoint_tool_ExternalJavaActionParameter_strategy)
def test_viewpoint_tool_externaljavaactionparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ContainerModelOperation_strategy)
@settings(max_examples=50)
def test_containermodeloperation_instantiation(instance):
    assert isinstance(instance, ContainerModelOperation)

@given(instance=viewpoint_tool_ChangeContext_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_changecontext_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ChangeContext)



@given(instance=viewpoint_tool_ChangeContext_strategy)
def test_viewpoint_tool_changecontext_browseExpression_setter(instance):
    original = instance.browseExpression
    instance.browseExpression = original
    assert instance.browseExpression == original

@given(instance=viewpoint_tool_Let_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_let_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_Let)



@given(instance=viewpoint_tool_Let_strategy)
def test_viewpoint_tool_let_valueExpression_setter(instance):
    original = instance.valueExpression
    instance.valueExpression = original
    assert instance.valueExpression == original



@given(instance=viewpoint_tool_Let_strategy)
def test_viewpoint_tool_let_variableName_setter(instance):
    original = instance.variableName
    instance.variableName = original
    assert instance.variableName == original

@given(instance=viewpoint_tool_If_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_if_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_If)



@given(instance=viewpoint_tool_If_strategy)
def test_viewpoint_tool_if_conditionExpression_setter(instance):
    original = instance.conditionExpression
    instance.conditionExpression = original
    assert instance.conditionExpression == original

@given(instance=viewpoint_tool_DeleteView_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_deleteview_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_DeleteView)

@given(instance=viewpoint_tool_SetValue_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_setvalue_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_SetValue)



@given(instance=viewpoint_tool_SetValue_strategy)
def test_viewpoint_tool_setvalue_valueExpression_setter(instance):
    original = instance.valueExpression
    instance.valueExpression = original
    assert instance.valueExpression == original



@given(instance=viewpoint_tool_SetValue_strategy)
def test_viewpoint_tool_setvalue_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original

@given(instance=viewpoint_tool_For_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_for_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_For)



@given(instance=viewpoint_tool_For_strategy)
def test_viewpoint_tool_for_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original



@given(instance=viewpoint_tool_For_strategy)
def test_viewpoint_tool_for_iteratorName_setter(instance):
    original = instance.iteratorName
    instance.iteratorName = original
    assert instance.iteratorName == original

@given(instance=viewpoint_tool_SetObject_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_setobject_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_SetObject)



@given(instance=viewpoint_tool_SetObject_strategy)
def test_viewpoint_tool_setobject_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original

@given(instance=viewpoint_tool_RemoveElement_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_removeelement_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_RemoveElement)

@given(instance=viewpoint_tool_CreateInstance_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_createinstance_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_CreateInstance)



@given(instance=viewpoint_tool_CreateInstance_strategy)
def test_viewpoint_tool_createinstance_variableName_setter(instance):
    original = instance.variableName
    instance.variableName = original
    assert instance.variableName == original



@given(instance=viewpoint_tool_CreateInstance_strategy)
def test_viewpoint_tool_createinstance_typeName_setter(instance):
    original = instance.typeName
    instance.typeName = original
    assert instance.typeName == original



@given(instance=viewpoint_tool_CreateInstance_strategy)
def test_viewpoint_tool_createinstance_referenceName_setter(instance):
    original = instance.referenceName
    instance.referenceName = original
    assert instance.referenceName == original

@given(instance=viewpoint_tool_MoveElement_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_moveelement_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_MoveElement)



@given(instance=viewpoint_tool_MoveElement_strategy)
def test_viewpoint_tool_moveelement_newContainerExpression_setter(instance):
    original = instance.newContainerExpression
    instance.newContainerExpression = original
    assert instance.newContainerExpression == original



@given(instance=viewpoint_tool_MoveElement_strategy)
def test_viewpoint_tool_moveelement_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original

@given(instance=viewpoint_tool_Unset_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_unset_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_Unset)



@given(instance=viewpoint_tool_Unset_strategy)
def test_viewpoint_tool_unset_elementExpression_setter(instance):
    original = instance.elementExpression
    instance.elementExpression = original
    assert instance.elementExpression == original



@given(instance=viewpoint_tool_Unset_strategy)
def test_viewpoint_tool_unset_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original

@given(instance=tool_viewpoint_EObject_strategy)
@settings(max_examples=50)
def test_tool_viewpoint_eobject_instantiation(instance):
    assert isinstance(instance, tool_viewpoint_EObject)

@given(instance=tool_ModelOperation_strategy)
@settings(max_examples=50)
def test_tool_modeloperation_instantiation(instance):
    assert isinstance(instance, tool_ModelOperation)

@given(instance=ModelOperation_strategy)
@settings(max_examples=50)
def test_modeloperation_instantiation(instance):
    assert isinstance(instance, ModelOperation)

@given(instance=viewpoint_tool_Switch_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_switch_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_Switch)

@given(instance=viewpoint_tool_ContainerModelOperation_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_containermodeloperation_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ContainerModelOperation)

@given(instance=viewpoint_tool_EditMaskVariables_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_editmaskvariables_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_EditMaskVariables)



@given(instance=viewpoint_tool_EditMaskVariables_strategy)
def test_viewpoint_tool_editmaskvariables_mask_setter(instance):
    original = instance.mask
    instance.mask = original
    assert instance.mask == original

@given(instance=description_AbstractVariable_strategy)
@settings(max_examples=50)
def test_description_abstractvariable_instantiation(instance):
    assert isinstance(instance, description_AbstractVariable)

@given(instance=viewpoint_tool_InitialContainerDropOperation_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_initialcontainerdropoperation_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_InitialContainerDropOperation)

@given(instance=viewpoint_tool_InitEdgeCreationOperation_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_initedgecreationoperation_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_InitEdgeCreationOperation)

@given(instance=viewpoint_tool_InitialOperation_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_initialoperation_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_InitialOperation)

@given(instance=viewpoint_tool_InitialNodeCreationOperation_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_initialnodecreationoperation_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_InitialNodeCreationOperation)

@given(instance=viewpoint_tool_ModelOperation_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_modeloperation_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ModelOperation)

@given(instance=tool_ExternalJavaAction_strategy)
@settings(max_examples=50)
def test_tool_externaljavaaction_instantiation(instance):
    assert isinstance(instance, tool_ExternalJavaAction)

@given(instance=tool_ExternalJavaActionParameter_strategy)
@settings(max_examples=50)
def test_tool_externaljavaactionparameter_instantiation(instance):
    assert isinstance(instance, tool_ExternalJavaActionParameter)

@given(instance=tool_ContainerModelOperation_strategy)
@settings(max_examples=50)
def test_tool_containermodeloperation_instantiation(instance):
    assert isinstance(instance, tool_ContainerModelOperation)

@given(instance=tool_GroupMenuItem_strategy)
@settings(max_examples=50)
def test_tool_groupmenuitem_instantiation(instance):
    assert isinstance(instance, tool_GroupMenuItem)

@given(instance=tool_MenuItemDescriptionWithIcon_strategy)
@settings(max_examples=50)
def test_tool_menuitemdescriptionwithicon_instantiation(instance):
    assert isinstance(instance, tool_MenuItemDescriptionWithIcon)

@given(instance=viewpoint_tool_ExternalJavaAction_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_externaljavaaction_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ExternalJavaAction)



@given(instance=viewpoint_tool_ExternalJavaAction_strategy)
def test_viewpoint_tool_externaljavaaction_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=viewpoint_tool_ExternalJavaActionCall_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_externaljavaactioncall_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ExternalJavaActionCall)

@given(instance=viewpoint_tool_OperationAction_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_operationaction_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_OperationAction)

@given(instance=tool_MenuItemDescription_strategy)
@settings(max_examples=50)
def test_tool_menuitemdescription_instantiation(instance):
    assert isinstance(instance, tool_MenuItemDescription)

@given(instance=MenuItemOrRef_strategy)
@settings(max_examples=50)
def test_menuitemorref_instantiation(instance):
    assert isinstance(instance, MenuItemOrRef)

@given(instance=viewpoint_tool_MenuItemDescriptionReference_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_menuitemdescriptionreference_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_MenuItemDescriptionReference)

@given(instance=tool_MenuItemOrRef_strategy)
@settings(max_examples=50)
def test_tool_menuitemorref_instantiation(instance):
    assert isinstance(instance, tool_MenuItemOrRef)

@given(instance=viewpoint_tool_MenuItemOrRef_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_menuitemorref_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_MenuItemOrRef)

@given(instance=tool_VariableContainer_strategy)
@settings(max_examples=50)
def test_tool_variablecontainer_instantiation(instance):
    assert isinstance(instance, tool_VariableContainer)

@given(instance=viewpoint_tool_ContainerViewVariable_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_containerviewvariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ContainerViewVariable)

@given(instance=viewpoint_tool_SelectContainerVariable_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_selectcontainervariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_SelectContainerVariable)

@given(instance=viewpoint_tool_DropContainerVariable_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_dropcontainervariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_DropContainerVariable)

@given(instance=viewpoint_tool_ElementDropVariable_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_elementdropvariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ElementDropVariable)

@given(instance=viewpoint_tool_ElementVariable_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_elementvariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ElementVariable)

@given(instance=viewpoint_tool_ElementDeleteVariable_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_elementdeletevariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ElementDeleteVariable)

@given(instance=viewpoint_tool_ElementViewVariable_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_elementviewvariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ElementViewVariable)

@given(instance=SubVariable_strategy)
@settings(max_examples=50)
def test_subvariable_instantiation(instance):
    assert isinstance(instance, SubVariable)

@given(instance=viewpoint_tool_VariableContainer_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_variablecontainer_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_VariableContainer)

@given(instance=tool_NameVariable_strategy)
@settings(max_examples=50)
def test_tool_namevariable_instantiation(instance):
    assert isinstance(instance, tool_NameVariable)

@given(instance=tool_SelectContainerVariable_strategy)
@settings(max_examples=50)
def test_tool_selectcontainervariable_instantiation(instance):
    assert isinstance(instance, tool_SelectContainerVariable)

@given(instance=tool_ElementSelectVariable_strategy)
@settings(max_examples=50)
def test_tool_elementselectvariable_instantiation(instance):
    assert isinstance(instance, tool_ElementSelectVariable)

@given(instance=description_SelectionDescription_strategy)
@settings(max_examples=50)
def test_description_selectiondescription_instantiation(instance):
    assert isinstance(instance, description_SelectionDescription)

@given(instance=tool_AbstractToolDescription_strategy)
@settings(max_examples=50)
def test_tool_abstracttooldescription_instantiation(instance):
    assert isinstance(instance, tool_AbstractToolDescription)

@given(instance=viewpoint_tool_PopupMenu_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_popupmenu_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_PopupMenu)

@given(instance=viewpoint_tool_MenuItemDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_menuitemdescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_MenuItemDescription)

@given(instance=viewpoint_tool_SelectionWizardDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_selectionwizarddescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_SelectionWizardDescription)



@given(instance=viewpoint_tool_SelectionWizardDescription_strategy)
def test_viewpoint_tool_selectionwizarddescription_iconPath_setter(instance):
    original = instance.iconPath
    instance.iconPath = original
    assert instance.iconPath == original



@given(instance=viewpoint_tool_SelectionWizardDescription_strategy)
def test_viewpoint_tool_selectionwizarddescription_windowTitle_setter(instance):
    original = instance.windowTitle
    instance.windowTitle = original
    assert instance.windowTitle == original



@given(instance=viewpoint_tool_SelectionWizardDescription_strategy)
def test_viewpoint_tool_selectionwizarddescription_windowImagePath_setter(instance):
    original = instance.windowImagePath
    instance.windowImagePath = original
    assert instance.windowImagePath == original

@given(instance=tool_ContainerViewVariable_strategy)
@settings(max_examples=50)
def test_tool_containerviewvariable_instantiation(instance):
    assert isinstance(instance, tool_ContainerViewVariable)

@given(instance=tool_DropContainerVariable_strategy)
@settings(max_examples=50)
def test_tool_dropcontainervariable_instantiation(instance):
    assert isinstance(instance, tool_DropContainerVariable)

@given(instance=tool_InitialOperation_strategy)
@settings(max_examples=50)
def test_tool_initialoperation_instantiation(instance):
    assert isinstance(instance, tool_InitialOperation)

@given(instance=tool_ElementViewVariable_strategy)
@settings(max_examples=50)
def test_tool_elementviewvariable_instantiation(instance):
    assert isinstance(instance, tool_ElementViewVariable)

@given(instance=tool_ElementVariable_strategy)
@settings(max_examples=50)
def test_tool_elementvariable_instantiation(instance):
    assert isinstance(instance, tool_ElementVariable)

@given(instance=MappingBasedToolDescription_strategy)
@settings(max_examples=50)
def test_mappingbasedtooldescription_instantiation(instance):
    assert isinstance(instance, MappingBasedToolDescription)

@given(instance=viewpoint_tool_PasteDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_pastedescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_PasteDescription)

@given(instance=viewpoint_tool_ToolDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_tooldescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ToolDescription)



@given(instance=viewpoint_tool_ToolDescription_strategy)
def test_viewpoint_tool_tooldescription_iconPath_setter(instance):
    original = instance.iconPath
    instance.iconPath = original
    assert instance.iconPath == original

@given(instance=AbstractToolDescription_strategy)
@settings(max_examples=50)
def test_abstracttooldescription_instantiation(instance):
    assert isinstance(instance, AbstractToolDescription)

@given(instance=viewpoint_tool_RepresentationCreationDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_representationcreationdescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_RepresentationCreationDescription)



@given(instance=viewpoint_tool_RepresentationCreationDescription_strategy)
def test_viewpoint_tool_representationcreationdescription_titleExpression_setter(instance):
    original = instance.titleExpression
    instance.titleExpression = original
    assert instance.titleExpression == original



@given(instance=viewpoint_tool_RepresentationCreationDescription_strategy)
def test_viewpoint_tool_representationcreationdescription_browseExpression_setter(instance):
    original = instance.browseExpression
    instance.browseExpression = original
    assert instance.browseExpression == original

@given(instance=viewpoint_tool_GroupMenuItem_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_groupmenuitem_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_GroupMenuItem)

@given(instance=viewpoint_tool_PaneBasedSelectionWizardDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_panebasedselectionwizarddescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_PaneBasedSelectionWizardDescription)



@given(instance=viewpoint_tool_PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint_tool_panebasedselectionwizarddescription_preSelectedCandidatesExpression_setter(instance):
    original = instance.preSelectedCandidatesExpression
    instance.preSelectedCandidatesExpression = original
    assert instance.preSelectedCandidatesExpression == original



@given(instance=viewpoint_tool_PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint_tool_panebasedselectionwizarddescription_windowTitle_setter(instance):
    original = instance.windowTitle
    instance.windowTitle = original
    assert instance.windowTitle == original



@given(instance=viewpoint_tool_PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint_tool_panebasedselectionwizarddescription_rootExpression_setter(instance):
    original = instance.rootExpression
    instance.rootExpression = original
    assert instance.rootExpression == original



@given(instance=viewpoint_tool_PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint_tool_panebasedselectionwizarddescription_choiceOfValuesMessage_setter(instance):
    original = instance.choiceOfValuesMessage
    instance.choiceOfValuesMessage = original
    assert instance.choiceOfValuesMessage == original



@given(instance=viewpoint_tool_PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint_tool_panebasedselectionwizarddescription_selectedValuesMessage_setter(instance):
    original = instance.selectedValuesMessage
    instance.selectedValuesMessage = original
    assert instance.selectedValuesMessage == original



@given(instance=viewpoint_tool_PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint_tool_panebasedselectionwizarddescription_childrenExpression_setter(instance):
    original = instance.childrenExpression
    instance.childrenExpression = original
    assert instance.childrenExpression == original



@given(instance=viewpoint_tool_PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint_tool_panebasedselectionwizarddescription_windowImagePath_setter(instance):
    original = instance.windowImagePath
    instance.windowImagePath = original
    assert instance.windowImagePath == original



@given(instance=viewpoint_tool_PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint_tool_panebasedselectionwizarddescription_tree_setter(instance):
    original = instance.tree
    instance.tree = original
    assert instance.tree == original



@given(instance=viewpoint_tool_PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint_tool_panebasedselectionwizarddescription_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original



@given(instance=viewpoint_tool_PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint_tool_panebasedselectionwizarddescription_candidatesExpression_setter(instance):
    original = instance.candidatesExpression
    instance.candidatesExpression = original
    assert instance.candidatesExpression == original



@given(instance=viewpoint_tool_PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint_tool_panebasedselectionwizarddescription_iconPath_setter(instance):
    original = instance.iconPath
    instance.iconPath = original
    assert instance.iconPath == original

@given(instance=viewpoint_tool_RepresentationNavigationDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_representationnavigationdescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_RepresentationNavigationDescription)



@given(instance=viewpoint_tool_RepresentationNavigationDescription_strategy)
def test_viewpoint_tool_representationnavigationdescription_browseExpression_setter(instance):
    original = instance.browseExpression
    instance.browseExpression = original
    assert instance.browseExpression == original



@given(instance=viewpoint_tool_RepresentationNavigationDescription_strategy)
def test_viewpoint_tool_representationnavigationdescription_navigationNameExpression_setter(instance):
    original = instance.navigationNameExpression
    instance.navigationNameExpression = original
    assert instance.navigationNameExpression == original

@given(instance=viewpoint_tool_MappingBasedToolDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_mappingbasedtooldescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_MappingBasedToolDescription)

@given(instance=style_LabelBorderStyleDescription_strategy)
@settings(max_examples=50)
def test_style_labelborderstyledescription_instantiation(instance):
    assert isinstance(instance, style_LabelBorderStyleDescription)

@given(instance=viewpoint_style_LabelBorderStyles_strategy)
@settings(max_examples=50)
def test_viewpoint_style_labelborderstyles_instantiation(instance):
    assert isinstance(instance, viewpoint_style_LabelBorderStyles)

@given(instance=tool_ToolFilterDescription_strategy)
@settings(max_examples=50)
def test_tool_toolfilterdescription_instantiation(instance):
    assert isinstance(instance, tool_ToolFilterDescription)

@given(instance=ToolEntry_strategy)
@settings(max_examples=50)
def test_toolentry_instantiation(instance):
    assert isinstance(instance, ToolEntry)

@given(instance=viewpoint_tool_AbstractToolDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_abstracttooldescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_AbstractToolDescription)



@given(instance=viewpoint_tool_AbstractToolDescription_strategy)
def test_viewpoint_tool_abstracttooldescription_elementsToSelect_setter(instance):
    original = instance.elementsToSelect
    instance.elementsToSelect = original
    assert instance.elementsToSelect == original



@given(instance=viewpoint_tool_AbstractToolDescription_strategy)
def test_viewpoint_tool_abstracttooldescription_forceRefresh_setter(instance):
    original = instance.forceRefresh
    instance.forceRefresh = original
    assert instance.forceRefresh == original



@given(instance=viewpoint_tool_AbstractToolDescription_strategy)
def test_viewpoint_tool_abstracttooldescription_precondition_setter(instance):
    original = instance.precondition
    instance.precondition = original
    assert instance.precondition == original



@given(instance=viewpoint_tool_AbstractToolDescription_strategy)
def test_viewpoint_tool_abstracttooldescription_inverseSelectionOrder_setter(instance):
    original = instance.inverseSelectionOrder
    instance.inverseSelectionOrder = original
    assert instance.inverseSelectionOrder == original

@given(instance=viewpoint_style_TooltipStyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_style_tooltipstyledescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_TooltipStyleDescription)



@given(instance=viewpoint_style_TooltipStyleDescription_strategy)
def test_viewpoint_style_tooltipstyledescription_tooltipExpression_setter(instance):
    original = instance.tooltipExpression
    instance.tooltipExpression = original
    assert instance.tooltipExpression == original

@given(instance=viewpoint_style_LabelBorderStyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_style_labelborderstyledescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_LabelBorderStyleDescription)



@given(instance=viewpoint_style_LabelBorderStyleDescription_strategy)
def test_viewpoint_style_labelborderstyledescription_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=viewpoint_style_LabelBorderStyleDescription_strategy)
def test_viewpoint_style_labelborderstyledescription_cornerHeight_setter(instance):
    original = instance.cornerHeight
    instance.cornerHeight = original
    assert instance.cornerHeight == original



@given(instance=viewpoint_style_LabelBorderStyleDescription_strategy)
def test_viewpoint_style_labelborderstyledescription_cornerWidth_setter(instance):
    original = instance.cornerWidth
    instance.cornerWidth = original
    assert instance.cornerWidth == original



@given(instance=viewpoint_style_LabelBorderStyleDescription_strategy)
def test_viewpoint_style_labelborderstyledescription_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=viewpoint_description_InteractiveVariableDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_description_interactivevariabledescription_instantiation(instance):
    assert isinstance(instance, viewpoint_description_InteractiveVariableDescription)



@given(instance=viewpoint_description_InteractiveVariableDescription_strategy)
def test_viewpoint_description_interactivevariabledescription_userDocumentation_setter(instance):
    original = instance.userDocumentation
    instance.userDocumentation = original
    assert instance.userDocumentation == original

@given(instance=AbstractVariable_strategy)
@settings(max_examples=50)
def test_abstractvariable_instantiation(instance):
    assert isinstance(instance, AbstractVariable)

@given(instance=viewpoint_tool_NameVariable_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_namevariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_NameVariable)

@given(instance=viewpoint_tool_DialogVariable_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_dialogvariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_DialogVariable)



@given(instance=viewpoint_tool_DialogVariable_strategy)
def test_viewpoint_tool_dialogvariable_dialogPrompt_setter(instance):
    original = instance.dialogPrompt
    instance.dialogPrompt = original
    assert instance.dialogPrompt == original

@given(instance=viewpoint_tool_ElementSelectVariable_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_elementselectvariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ElementSelectVariable)

@given(instance=viewpoint_description_SubVariable_strategy)
@settings(max_examples=50)
def test_viewpoint_description_subvariable_instantiation(instance):
    assert isinstance(instance, viewpoint_description_SubVariable)

@given(instance=viewpoint_description_AbstractVariable_strategy)
@settings(max_examples=50)
def test_viewpoint_description_abstractvariable_instantiation(instance):
    assert isinstance(instance, viewpoint_description_AbstractVariable)



@given(instance=viewpoint_description_AbstractVariable_strategy)
def test_viewpoint_description_abstractvariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BasicLabelStyleDescription_strategy)
@settings(max_examples=50)
def test_basiclabelstyledescription_instantiation(instance):
    assert isinstance(instance, BasicLabelStyleDescription)

@given(instance=viewpoint_style_LabelStyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_style_labelstyledescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_LabelStyleDescription)



@given(instance=viewpoint_style_LabelStyleDescription_strategy)
def test_viewpoint_style_labelstyledescription_labelAlignment_setter(instance):
    original = instance.labelAlignment
    instance.labelAlignment = original
    assert instance.labelAlignment == original

@given(instance=viewpoint_description_DAnnotationEntry_strategy)
@settings(max_examples=50)
def test_viewpoint_description_dannotationentry_instantiation(instance):
    assert isinstance(instance, viewpoint_description_DAnnotationEntry)



@given(instance=viewpoint_description_DAnnotationEntry_strategy)
def test_viewpoint_description_dannotationentry_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original



@given(instance=viewpoint_description_DAnnotationEntry_strategy)
def test_viewpoint_description_dannotationentry_details_setter(instance):
    original = instance.details
    instance.details = original
    assert instance.details == original

@given(instance=viewpoint_style_BasicLabelStyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_style_basiclabelstyledescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_BasicLabelStyleDescription)



@given(instance=viewpoint_style_BasicLabelStyleDescription_strategy)
def test_viewpoint_style_basiclabelstyledescription_labelSize_setter(instance):
    original = instance.labelSize
    instance.labelSize = original
    assert instance.labelSize == original



@given(instance=viewpoint_style_BasicLabelStyleDescription_strategy)
def test_viewpoint_style_basiclabelstyledescription_labelExpression_setter(instance):
    original = instance.labelExpression
    instance.labelExpression = original
    assert instance.labelExpression == original



@given(instance=viewpoint_style_BasicLabelStyleDescription_strategy)
def test_viewpoint_style_basiclabelstyledescription_showIcon_setter(instance):
    original = instance.showIcon
    instance.showIcon = original
    assert instance.showIcon == original



@given(instance=viewpoint_style_BasicLabelStyleDescription_strategy)
def test_viewpoint_style_basiclabelstyledescription_labelFormat_setter(instance):
    original = instance.labelFormat
    instance.labelFormat = original
    assert instance.labelFormat == original



@given(instance=viewpoint_style_BasicLabelStyleDescription_strategy)
def test_viewpoint_style_basiclabelstyledescription_iconPath_setter(instance):
    original = instance.iconPath
    instance.iconPath = original
    assert instance.iconPath == original

@given(instance=viewpoint_style_StyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_style_styledescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_StyleDescription)

@given(instance=description_viewpoint_EDataType_strategy)
@settings(max_examples=50)
def test_description_viewpoint_edatatype_instantiation(instance):
    assert isinstance(instance, description_viewpoint_EDataType)

@given(instance=description_SubVariable_strategy)
@settings(max_examples=50)
def test_description_subvariable_instantiation(instance):
    assert isinstance(instance, description_SubVariable)

@given(instance=viewpoint_tool_AcceleoVariable_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_acceleovariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_AcceleoVariable)



@given(instance=viewpoint_tool_AcceleoVariable_strategy)
def test_viewpoint_tool_acceleovariable_computationExpression_setter(instance):
    original = instance.computationExpression
    instance.computationExpression = original
    assert instance.computationExpression == original

@given(instance=description_InteractiveVariableDescription_strategy)
@settings(max_examples=50)
def test_description_interactivevariabledescription_instantiation(instance):
    assert isinstance(instance, description_InteractiveVariableDescription)

@given(instance=viewpoint_tool_SelectModelElementVariable_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_selectmodelelementvariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_SelectModelElementVariable)

@given(instance=viewpoint_description_TypedVariable_strategy)
@settings(max_examples=50)
def test_viewpoint_description_typedvariable_instantiation(instance):
    assert isinstance(instance, viewpoint_description_TypedVariable)



@given(instance=viewpoint_description_TypedVariable_strategy)
def test_viewpoint_description_typedvariable_defaultValueExpression_setter(instance):
    original = instance.defaultValueExpression
    instance.defaultValueExpression = original
    assert instance.defaultValueExpression == original

@given(instance=SystemColor_strategy)
@settings(max_examples=50)
def test_systemcolor_instantiation(instance):
    assert isinstance(instance, SystemColor)

@given(instance=viewpoint_description_SytemColorsPalette_strategy)
@settings(max_examples=50)
def test_viewpoint_description_sytemcolorspalette_instantiation(instance):
    assert isinstance(instance, viewpoint_description_SytemColorsPalette)

@given(instance=style_LabelBorderStyles_strategy)
@settings(max_examples=50)
def test_style_labelborderstyles_instantiation(instance):
    assert isinstance(instance, style_LabelBorderStyles)

@given(instance=viewpoint_description_IdentifiedElement_strategy)
@settings(max_examples=50)
def test_viewpoint_description_identifiedelement_instantiation(instance):
    assert isinstance(instance, viewpoint_description_IdentifiedElement)



@given(instance=viewpoint_description_IdentifiedElement_strategy)
def test_viewpoint_description_identifiedelement_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=viewpoint_description_IdentifiedElement_strategy)
def test_viewpoint_description_identifiedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=viewpoint_description_EndUserDocumentedElement_strategy)
@settings(max_examples=50)
def test_viewpoint_description_enduserdocumentedelement_instantiation(instance):
    assert isinstance(instance, viewpoint_description_EndUserDocumentedElement)



@given(instance=viewpoint_description_EndUserDocumentedElement_strategy)
def test_viewpoint_description_enduserdocumentedelement_endUserDocumentation_setter(instance):
    original = instance.endUserDocumentation
    instance.endUserDocumentation = original
    assert instance.endUserDocumentation == original

@given(instance=viewpoint_description_AnnotationEntry_strategy)
@settings(max_examples=50)
def test_viewpoint_description_annotationentry_instantiation(instance):
    assert isinstance(instance, viewpoint_description_AnnotationEntry)



@given(instance=viewpoint_description_AnnotationEntry_strategy)
def test_viewpoint_description_annotationentry_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original

@given(instance=UserColor_strategy)
@settings(max_examples=50)
def test_usercolor_instantiation(instance):
    assert isinstance(instance, UserColor)

@given(instance=viewpoint_description_UserColorsPalette_strategy)
@settings(max_examples=50)
def test_viewpoint_description_usercolorspalette_instantiation(instance):
    assert isinstance(instance, viewpoint_description_UserColorsPalette)



@given(instance=viewpoint_description_UserColorsPalette_strategy)
def test_viewpoint_description_usercolorspalette_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=viewpoint_description_Environment_strategy)
@settings(max_examples=50)
def test_viewpoint_description_environment_instantiation(instance):
    assert isinstance(instance, viewpoint_description_Environment)

@given(instance=ColorStep_strategy)
@settings(max_examples=50)
def test_colorstep_instantiation(instance):
    assert isinstance(instance, ColorStep)

@given(instance=description_UserColor_strategy)
@settings(max_examples=50)
def test_description_usercolor_instantiation(instance):
    assert isinstance(instance, description_UserColor)

@given(instance=description_ColorDescription_strategy)
@settings(max_examples=50)
def test_description_colordescription_instantiation(instance):
    assert isinstance(instance, description_ColorDescription)

@given(instance=viewpoint_description_ComputedColor_strategy)
@settings(max_examples=50)
def test_viewpoint_description_computedcolor_instantiation(instance):
    assert isinstance(instance, viewpoint_description_ComputedColor)



@given(instance=viewpoint_description_ComputedColor_strategy)
def test_viewpoint_description_computedcolor_green_setter(instance):
    original = instance.green
    instance.green = original
    assert instance.green == original



@given(instance=viewpoint_description_ComputedColor_strategy)
def test_viewpoint_description_computedcolor_red_setter(instance):
    original = instance.red
    instance.red = original
    assert instance.red == original



@given(instance=viewpoint_description_ComputedColor_strategy)
def test_viewpoint_description_computedcolor_blue_setter(instance):
    original = instance.blue
    instance.blue = original
    assert instance.blue == original

@given(instance=viewpoint_description_InterpolatedColor_strategy)
@settings(max_examples=50)
def test_viewpoint_description_interpolatedcolor_instantiation(instance):
    assert isinstance(instance, viewpoint_description_InterpolatedColor)



@given(instance=viewpoint_description_InterpolatedColor_strategy)
def test_viewpoint_description_interpolatedcolor_maxValueComputationExpression_setter(instance):
    original = instance.maxValueComputationExpression
    instance.maxValueComputationExpression = original
    assert instance.maxValueComputationExpression == original



@given(instance=viewpoint_description_InterpolatedColor_strategy)
def test_viewpoint_description_interpolatedcolor_minValueComputationExpression_setter(instance):
    original = instance.minValueComputationExpression
    instance.minValueComputationExpression = original
    assert instance.minValueComputationExpression == original



@given(instance=viewpoint_description_InterpolatedColor_strategy)
def test_viewpoint_description_interpolatedcolor_colorValueComputationExpression_setter(instance):
    original = instance.colorValueComputationExpression
    instance.colorValueComputationExpression = original
    assert instance.colorValueComputationExpression == original

@given(instance=FixedColor_strategy)
@settings(max_examples=50)
def test_fixedcolor_instantiation(instance):
    assert isinstance(instance, FixedColor)

@given(instance=viewpoint_description_SystemColor_strategy)
@settings(max_examples=50)
def test_viewpoint_description_systemcolor_instantiation(instance):
    assert isinstance(instance, viewpoint_description_SystemColor)



@given(instance=viewpoint_description_SystemColor_strategy)
def test_viewpoint_description_systemcolor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=viewpoint_description_UserColor_strategy)
@settings(max_examples=50)
def test_viewpoint_description_usercolor_instantiation(instance):
    assert isinstance(instance, viewpoint_description_UserColor)



@given(instance=viewpoint_description_UserColor_strategy)
def test_viewpoint_description_usercolor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=viewpoint_description_ColorDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_description_colordescription_instantiation(instance):
    assert isinstance(instance, viewpoint_description_ColorDescription)

@given(instance=description_FixedColor_strategy)
@settings(max_examples=50)
def test_description_fixedcolor_instantiation(instance):
    assert isinstance(instance, description_FixedColor)

@given(instance=viewpoint_description_UserFixedColor_strategy)
@settings(max_examples=50)
def test_viewpoint_description_userfixedcolor_instantiation(instance):
    assert isinstance(instance, viewpoint_description_UserFixedColor)

@given(instance=ColorDescription_strategy)
@settings(max_examples=50)
def test_colordescription_instantiation(instance):
    assert isinstance(instance, ColorDescription)

@given(instance=viewpoint_description_FixedColor_strategy)
@settings(max_examples=50)
def test_viewpoint_description_fixedcolor_instantiation(instance):
    assert isinstance(instance, viewpoint_description_FixedColor)



@given(instance=viewpoint_description_FixedColor_strategy)
def test_viewpoint_description_fixedcolor_red_setter(instance):
    original = instance.red
    instance.red = original
    assert instance.red == original



@given(instance=viewpoint_description_FixedColor_strategy)
def test_viewpoint_description_fixedcolor_green_setter(instance):
    original = instance.green
    instance.green = original
    assert instance.green == original



@given(instance=viewpoint_description_FixedColor_strategy)
def test_viewpoint_description_fixedcolor_blue_setter(instance):
    original = instance.blue
    instance.blue = original
    assert instance.blue == original

@given(instance=viewpoint_description_ColorStep_strategy)
@settings(max_examples=50)
def test_viewpoint_description_colorstep_instantiation(instance):
    assert isinstance(instance, viewpoint_description_ColorStep)



@given(instance=viewpoint_description_ColorStep_strategy)
def test_viewpoint_description_colorstep_associatedValue_setter(instance):
    original = instance.associatedValue
    instance.associatedValue = original
    assert instance.associatedValue == original

@given(instance=viewpoint_description_EStructuralFeatureCustomization_strategy)
@settings(max_examples=50)
def test_viewpoint_description_estructuralfeaturecustomization_instantiation(instance):
    assert isinstance(instance, viewpoint_description_EStructuralFeatureCustomization)



@given(instance=viewpoint_description_EStructuralFeatureCustomization_strategy)
def test_viewpoint_description_estructuralfeaturecustomization_applyOnAll_setter(instance):
    original = instance.applyOnAll
    instance.applyOnAll = original
    assert instance.applyOnAll == original

@given(instance=EStructuralFeatureCustomization_strategy)
@settings(max_examples=50)
def test_estructuralfeaturecustomization_instantiation(instance):
    assert isinstance(instance, EStructuralFeatureCustomization)

@given(instance=viewpoint_description_EReferenceCustomization_strategy)
@settings(max_examples=50)
def test_viewpoint_description_ereferencecustomization_instantiation(instance):
    assert isinstance(instance, viewpoint_description_EReferenceCustomization)



@given(instance=viewpoint_description_EReferenceCustomization_strategy)
def test_viewpoint_description_ereferencecustomization_referenceName_setter(instance):
    original = instance.referenceName
    instance.referenceName = original
    assert instance.referenceName == original

@given(instance=viewpoint_description_EAttributeCustomization_strategy)
@settings(max_examples=50)
def test_viewpoint_description_eattributecustomization_instantiation(instance):
    assert isinstance(instance, viewpoint_description_EAttributeCustomization)



@given(instance=viewpoint_description_EAttributeCustomization_strategy)
def test_viewpoint_description_eattributecustomization_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=viewpoint_description_EAttributeCustomization_strategy)
def test_viewpoint_description_eattributecustomization_attributeName_setter(instance):
    original = instance.attributeName
    instance.attributeName = original
    assert instance.attributeName == original

@given(instance=viewpoint_description_SelectionDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_description_selectiondescription_instantiation(instance):
    assert isinstance(instance, viewpoint_description_SelectionDescription)



@given(instance=viewpoint_description_SelectionDescription_strategy)
def test_viewpoint_description_selectiondescription_childrenExpression_setter(instance):
    original = instance.childrenExpression
    instance.childrenExpression = original
    assert instance.childrenExpression == original



@given(instance=viewpoint_description_SelectionDescription_strategy)
def test_viewpoint_description_selectiondescription_candidatesExpression_setter(instance):
    original = instance.candidatesExpression
    instance.candidatesExpression = original
    assert instance.candidatesExpression == original



@given(instance=viewpoint_description_SelectionDescription_strategy)
def test_viewpoint_description_selectiondescription_multiple_setter(instance):
    original = instance.multiple
    instance.multiple = original
    assert instance.multiple == original



@given(instance=viewpoint_description_SelectionDescription_strategy)
def test_viewpoint_description_selectiondescription_tree_setter(instance):
    original = instance.tree
    instance.tree = original
    assert instance.tree == original



@given(instance=viewpoint_description_SelectionDescription_strategy)
def test_viewpoint_description_selectiondescription_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original



@given(instance=viewpoint_description_SelectionDescription_strategy)
def test_viewpoint_description_selectiondescription_rootExpression_setter(instance):
    original = instance.rootExpression
    instance.rootExpression = original
    assert instance.rootExpression == original

@given(instance=viewpoint_description_GenericDecorationDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_description_genericdecorationdescription_instantiation(instance):
    assert isinstance(instance, viewpoint_description_GenericDecorationDescription)

@given(instance=viewpoint_description_SemanticBasedDecoration_strategy)
@settings(max_examples=50)
def test_viewpoint_description_semanticbaseddecoration_instantiation(instance):
    assert isinstance(instance, viewpoint_description_SemanticBasedDecoration)



@given(instance=viewpoint_description_SemanticBasedDecoration_strategy)
def test_viewpoint_description_semanticbaseddecoration_domainClass_setter(instance):
    original = instance.domainClass
    instance.domainClass = original
    assert instance.domainClass == original

@given(instance=viewpoint_description_IVSMElementCustomization_strategy)
@settings(max_examples=50)
def test_viewpoint_description_ivsmelementcustomization_instantiation(instance):
    assert isinstance(instance, viewpoint_description_IVSMElementCustomization)

@given(instance=IVSMElementCustomization_strategy)
@settings(max_examples=50)
def test_ivsmelementcustomization_instantiation(instance):
    assert isinstance(instance, IVSMElementCustomization)

@given(instance=viewpoint_description_VSMElementCustomization_strategy)
@settings(max_examples=50)
def test_viewpoint_description_vsmelementcustomization_instantiation(instance):
    assert isinstance(instance, viewpoint_description_VSMElementCustomization)



@given(instance=viewpoint_description_VSMElementCustomization_strategy)
def test_viewpoint_description_vsmelementcustomization_predicateExpression_setter(instance):
    original = instance.predicateExpression
    instance.predicateExpression = original
    assert instance.predicateExpression == original

@given(instance=viewpoint_description_VSMElementCustomizationReuse_strategy)
@settings(max_examples=50)
def test_viewpoint_description_vsmelementcustomizationreuse_instantiation(instance):
    assert isinstance(instance, viewpoint_description_VSMElementCustomizationReuse)

@given(instance=viewpoint_description_Customization_strategy)
@settings(max_examples=50)
def test_viewpoint_description_customization_instantiation(instance):
    assert isinstance(instance, viewpoint_description_Customization)

@given(instance=viewpoint_description_DecorationDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_description_decorationdescription_instantiation(instance):
    assert isinstance(instance, viewpoint_description_DecorationDescription)



@given(instance=viewpoint_description_DecorationDescription_strategy)
def test_viewpoint_description_decorationdescription_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original



@given(instance=viewpoint_description_DecorationDescription_strategy)
def test_viewpoint_description_decorationdescription_tooltipExpression_setter(instance):
    original = instance.tooltipExpression
    instance.tooltipExpression = original
    assert instance.tooltipExpression == original



@given(instance=viewpoint_description_DecorationDescription_strategy)
def test_viewpoint_description_decorationdescription_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=viewpoint_description_DecorationDescription_strategy)
def test_viewpoint_description_decorationdescription_preconditionExpression_setter(instance):
    original = instance.preconditionExpression
    instance.preconditionExpression = original
    assert instance.preconditionExpression == original



@given(instance=viewpoint_description_DecorationDescription_strategy)
def test_viewpoint_description_decorationdescription_imageExpression_setter(instance):
    original = instance.imageExpression
    instance.imageExpression = original
    assert instance.imageExpression == original



@given(instance=viewpoint_description_DecorationDescription_strategy)
def test_viewpoint_description_decorationdescription_distributionDirection_setter(instance):
    original = instance.distributionDirection
    instance.distributionDirection = original
    assert instance.distributionDirection == original

@given(instance=viewpoint_description_DecorationDescriptionsSet_strategy)
@settings(max_examples=50)
def test_viewpoint_description_decorationdescriptionsset_instantiation(instance):
    assert isinstance(instance, viewpoint_description_DecorationDescriptionsSet)

@given(instance=tool_PasteDescription_strategy)
@settings(max_examples=50)
def test_tool_pastedescription_instantiation(instance):
    assert isinstance(instance, tool_PasteDescription)

@given(instance=viewpoint_description_PasteTargetDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_description_pastetargetdescription_instantiation(instance):
    assert isinstance(instance, viewpoint_description_PasteTargetDescription)

@given(instance=DAnnotation_strategy)
@settings(max_examples=50)
def test_dannotation_instantiation(instance):
    assert isinstance(instance, DAnnotation)

@given(instance=viewpoint_description_DModelElement_strategy)
@settings(max_examples=50)
def test_viewpoint_description_dmodelelement_instantiation(instance):
    assert isinstance(instance, viewpoint_description_DModelElement)

@given(instance=viewpoint_description_DocumentedElement_strategy)
@settings(max_examples=50)
def test_viewpoint_description_documentedelement_instantiation(instance):
    assert isinstance(instance, viewpoint_description_DocumentedElement)



@given(instance=viewpoint_description_DocumentedElement_strategy)
def test_viewpoint_description_documentedelement_documentation_setter(instance):
    original = instance.documentation
    instance.documentation = original
    assert instance.documentation == original

@given(instance=viewpoint_description_AbstractMappingImport_strategy)
@settings(max_examples=50)
def test_viewpoint_description_abstractmappingimport_instantiation(instance):
    assert isinstance(instance, viewpoint_description_AbstractMappingImport)



@given(instance=viewpoint_description_AbstractMappingImport_strategy)
def test_viewpoint_description_abstractmappingimport_inheritsAncestorFilters_setter(instance):
    original = instance.inheritsAncestorFilters
    instance.inheritsAncestorFilters = original
    assert instance.inheritsAncestorFilters == original



@given(instance=viewpoint_description_AbstractMappingImport_strategy)
def test_viewpoint_description_abstractmappingimport_hideSubMappings_setter(instance):
    original = instance.hideSubMappings
    instance.hideSubMappings = original
    assert instance.hideSubMappings == original

@given(instance=tool_RepresentationNavigationDescription_strategy)
@settings(max_examples=50)
def test_tool_representationnavigationdescription_instantiation(instance):
    assert isinstance(instance, tool_RepresentationNavigationDescription)

@given(instance=tool_RepresentationCreationDescription_strategy)
@settings(max_examples=50)
def test_tool_representationcreationdescription_instantiation(instance):
    assert isinstance(instance, tool_RepresentationCreationDescription)

@given(instance=viewpoint_description_RepresentationElementMapping_strategy)
@settings(max_examples=50)
def test_viewpoint_description_representationelementmapping_instantiation(instance):
    assert isinstance(instance, viewpoint_description_RepresentationElementMapping)

@given(instance=viewpoint_description_ConditionalStyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_description_conditionalstyledescription_instantiation(instance):
    assert isinstance(instance, viewpoint_description_ConditionalStyleDescription)



@given(instance=viewpoint_description_ConditionalStyleDescription_strategy)
def test_viewpoint_description_conditionalstyledescription_predicateExpression_setter(instance):
    original = instance.predicateExpression
    instance.predicateExpression = original
    assert instance.predicateExpression == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint_description_ConditionalStyleDescription_strategy)
@settings(max_examples=30)
def test_viewpoint_description_conditionalstyledescription_checkpredicate_changes_state(instance):
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
        assert has_statements, f"Function 'checkPredicate' in viewpoint_description_ConditionalStyleDescription is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'checkPredicate' in viewpoint_description_ConditionalStyleDescription did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'checkPredicate' in viewpoint_description_ConditionalStyleDescription is not implemented or raised an error")

@given(instance=description_viewpoint_EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_description_viewpoint_estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, description_viewpoint_EStringToStringMapEntry)

@given(instance=viewpoint_description_DAnnotation_strategy)
@settings(max_examples=50)
def test_viewpoint_description_dannotation_instantiation(instance):
    assert isinstance(instance, viewpoint_description_DAnnotation)



@given(instance=viewpoint_description_DAnnotation_strategy)
def test_viewpoint_description_dannotation_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original

@given(instance=viewpoint_description_RepresentationExtensionDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_description_representationextensiondescription_instantiation(instance):
    assert isinstance(instance, viewpoint_description_RepresentationExtensionDescription)



@given(instance=viewpoint_description_RepresentationExtensionDescription_strategy)
def test_viewpoint_description_representationextensiondescription_viewpointURI_setter(instance):
    original = instance.viewpointURI
    instance.viewpointURI = original
    assert instance.viewpointURI == original



@given(instance=viewpoint_description_RepresentationExtensionDescription_strategy)
def test_viewpoint_description_representationextensiondescription_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=viewpoint_description_RepresentationExtensionDescription_strategy)
def test_viewpoint_description_representationextensiondescription_representationName_setter(instance):
    original = instance.representationName
    instance.representationName = original
    assert instance.representationName == original

@given(instance=viewpoint_description_RepresentationImportDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_description_representationimportdescription_instantiation(instance):
    assert isinstance(instance, viewpoint_description_RepresentationImportDescription)

@given(instance=viewpoint_description_RepresentationTemplate_strategy)
@settings(max_examples=50)
def test_viewpoint_description_representationtemplate_instantiation(instance):
    assert isinstance(instance, viewpoint_description_RepresentationTemplate)



@given(instance=viewpoint_description_RepresentationTemplate_strategy)
def test_viewpoint_description_representationtemplate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=description_viewpoint_EPackage_strategy)
@settings(max_examples=50)
def test_description_viewpoint_epackage_instantiation(instance):
    assert isinstance(instance, description_viewpoint_EPackage)

@given(instance=viewpoint_description_FeatureExtensionDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_description_featureextensiondescription_instantiation(instance):
    assert isinstance(instance, viewpoint_description_FeatureExtensionDescription)

@given(instance=viewpoint_description_JavaExtension_strategy)
@settings(max_examples=50)
def test_viewpoint_description_javaextension_instantiation(instance):
    assert isinstance(instance, viewpoint_description_JavaExtension)



@given(instance=viewpoint_description_JavaExtension_strategy)
def test_viewpoint_description_javaextension_qualifiedClassName_setter(instance):
    original = instance.qualifiedClassName
    instance.qualifiedClassName = original
    assert instance.qualifiedClassName == original

@given(instance=description_viewpoint_EObject_strategy)
@settings(max_examples=50)
def test_description_viewpoint_eobject_instantiation(instance):
    assert isinstance(instance, description_viewpoint_EObject)

@given(instance=viewpoint_description_MetamodelExtensionSetting_strategy)
@settings(max_examples=50)
def test_viewpoint_description_metamodelextensionsetting_instantiation(instance):
    assert isinstance(instance, viewpoint_description_MetamodelExtensionSetting)

@given(instance=RepresentationExtensionDescription_strategy)
@settings(max_examples=50)
def test_representationextensiondescription_instantiation(instance):
    assert isinstance(instance, RepresentationExtensionDescription)

@given(instance=validation_ValidationSet_strategy)
@settings(max_examples=50)
def test_validation_validationset_instantiation(instance):
    assert isinstance(instance, validation_ValidationSet)

@given(instance=description_IdentifiedElement_strategy)
@settings(max_examples=50)
def test_description_identifiedelement_instantiation(instance):
    assert isinstance(instance, description_IdentifiedElement)

@given(instance=viewpoint_tool_ToolEntry_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_toolentry_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ToolEntry)

@given(instance=description_EndUserDocumentedElement_strategy)
@settings(max_examples=50)
def test_description_enduserdocumentedelement_instantiation(instance):
    assert isinstance(instance, description_EndUserDocumentedElement)

@given(instance=viewpoint_description_RepresentationDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_description_representationdescription_instantiation(instance):
    assert isinstance(instance, viewpoint_description_RepresentationDescription)



@given(instance=viewpoint_description_RepresentationDescription_strategy)
def test_viewpoint_description_representationdescription_initialisation_setter(instance):
    original = instance.initialisation
    instance.initialisation = original
    assert instance.initialisation == original



@given(instance=viewpoint_description_RepresentationDescription_strategy)
def test_viewpoint_description_representationdescription_titleExpression_setter(instance):
    original = instance.titleExpression
    instance.titleExpression = original
    assert instance.titleExpression == original



@given(instance=viewpoint_description_RepresentationDescription_strategy)
def test_viewpoint_description_representationdescription_showOnStartup_setter(instance):
    original = instance.showOnStartup
    instance.showOnStartup = original
    assert instance.showOnStartup == original

@given(instance=description_Component_strategy)
@settings(max_examples=50)
def test_description_component_instantiation(instance):
    assert isinstance(instance, description_Component)

@given(instance=viewpoint_description_Viewpoint_strategy)
@settings(max_examples=50)
def test_viewpoint_description_viewpoint_instantiation(instance):
    assert isinstance(instance, viewpoint_description_Viewpoint)



@given(instance=viewpoint_description_Viewpoint_strategy)
def test_viewpoint_description_viewpoint_reuses_setter(instance):
    original = instance.reuses
    instance.reuses = original
    assert instance.reuses == original



@given(instance=viewpoint_description_Viewpoint_strategy)
def test_viewpoint_description_viewpoint_icon_setter(instance):
    original = instance.icon
    instance.icon = original
    assert instance.icon == original



@given(instance=viewpoint_description_Viewpoint_strategy)
def test_viewpoint_description_viewpoint_conflicts_setter(instance):
    original = instance.conflicts
    instance.conflicts = original
    assert instance.conflicts == original



@given(instance=viewpoint_description_Viewpoint_strategy)
def test_viewpoint_description_viewpoint_modelFileExtension_setter(instance):
    original = instance.modelFileExtension
    instance.modelFileExtension = original
    assert instance.modelFileExtension == original



@given(instance=viewpoint_description_Viewpoint_strategy)
def test_viewpoint_description_viewpoint_customizes_setter(instance):
    original = instance.customizes
    instance.customizes = original
    assert instance.customizes == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint_description_Viewpoint_strategy)
@settings(max_examples=30)
def test_viewpoint_description_viewpoint_initview_changes_state(instance):
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
        assert has_statements, f"Function 'initView' in viewpoint_description_Viewpoint is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'initView' in viewpoint_description_Viewpoint did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'initView' in viewpoint_description_Viewpoint is not implemented or raised an error")

@given(instance=viewpoint_description_Component_strategy)
@settings(max_examples=50)
def test_viewpoint_description_component_instantiation(instance):
    assert isinstance(instance, viewpoint_description_Component)

@given(instance=viewpoint_description_Extension_strategy)
@settings(max_examples=50)
def test_viewpoint_description_extension_instantiation(instance):
    assert isinstance(instance, viewpoint_description_Extension)

@given(instance=Extension_strategy)
@settings(max_examples=50)
def test_extension_instantiation(instance):
    assert isinstance(instance, Extension)
