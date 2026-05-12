import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Path,
    website_CurrentUserReference,
    website_RouteParameterReference,
    website_FeatureReference,
    website_ModelReference,
    website_ParameterReference,
    website_InlineActionContainer,
    AuthenticationUnit,
    website_AuthenticationUnit,
    ImageUnit,
    website_GalleryUnit,
    website_SliderUnit,
    InlineAction,
    website_DeleteAction,
    website_FeatureSupportAction,
    website_SelectAction,
    ChildPath,
    website_ChildPathAttribute,
    FeaturePath,
    website_FeaturePathAttribute,
    website_FeaturePath,
    CollectionUnit,
    DataUnit,
    ControlUnit,
    website_SearchUnit,
    SingletonUnit,
    DynamicUnit,
    website_DataUnit,
    website_ImageUnit,
    website_ControlUnit,
    website_EditUnit,
    EditUnit,
    website_CreateUnit,
    InterfaceField,
    website_DateField,
    website_DataTypeField,
    website_ChildPath,
    website_AssociationReference,
    SelectableUnit,
    website_DetailsUnit,
    website_UpdateUnit,
    website_CreateUpdateUnit,
    website_MapUnit,
    website_CollectionUnit,
    website_SingletonUnit,
    website_SelectableUnit,
    website_CaptchaField,
    UnitFeature,
    website_UnitElement,
    InlineActionContainer,
    website_IndexUnit,
    website_ImageIndexUnit,
    UnitField,
    website_UnitFeature,
    AssociationReference,
    website_ChildPathAssociation,
    website_FeaturePathAssociation,
    ContentUnit,
    website_CreateSitemapUnit,
    website_DynamicUnit,
    website_StaticUnit,
    website_UnitContainer,
    website_UnitField,
    website_Query,
    MenuEntry,
    website_MenuFeature,
    Menu,
    website_DynamicMenu,
    website_StaticMenu,
    website_MenuEntry,
    website_QueryParameter,
    UnitContainer,
    website_UnitAssociation,
    ImageFilter,
    website_ThumbnailFilter,
    website_ImageFilter,
    website_Order,
    website_Predicate,
    website_PageLink,
    EntityAssociation,
    website_AssociationWithContainment,
    website_AssociationWithoutContainment,
    EncapsulatedFeature,
    ViewFeature,
    website_EncapsulatedFeature,
    PathElement,
    website_DatePathElement,
    website_StaticPathElement,
    website_PathElement,
    EntityAttribute,
    website_DateAttribute,
    website_UrlAttribute,
    website_ResourceAttribute,
    website_DataTypeAttribute,
    Attribute,
    website_EncapsulatedAttribute,
    EntityFeature,
    website_AssociationKey,
    Association,
    website_LocationAttribute,
    ResourceAttribute,
    website_ImageAttribute,
    website_FileAttribute,
    EntityOrView,
    website_View,
    website_Entity,
    website_EntityAssociation,
    ModelLabelFeature,
    website_ModelLabelAssociation,
    website_ModelLabelAttribute,
    website_ModelLabelFeature,
    website_Label,
    website_EntityAttribute,
    website_Expression,
    Label,
    Feature,
    website_ViewFeature,
    website_Association,
    website_EncapsulatedAssociation,
    website_Feature,
    DataType,
    website_EnumerationType,
    website_NamedElement,
    website_ForgottenPasswordUnit,
    website_LoginUnit,
    website_RegistrationUnit,
    Authentication,
    website_CasAuthentication,
    website_LocalAuthenticationSystem,
    website_Attribute,
    Classifier,
    website_DataType,
    NamedDisplayElement,
    website_ContentUnit,
    website_InterfaceField,
    website_EditStaticTextMenuEntry,
    website_EntityFeature,
    website_InlineAction,
    website_EnumerationLiteral,
    website_Filter,
    website_ActionMenuEntry,
    website_ViewAssociation,
    website_UnitSupportAction,
    NamedElement,
    website_FilterParameter,
    website_Selection,
    website_BusinessOperation,
    website_SelectionParameter,
    website_ModelLabel,
    website_NamedDisplayElement,
    website_Authentication,
    website_ImageManipulation,
    website_EntityOrView,
    website_Menu,
    website_Page,
    website_Service,
    website_Classifier,
    website_WebsiteProperties,
    website_WebGenModel,
    PageTopMenuOptions,
    CollectionDisplayOptions,
    OperationResultTypes,
    OrmTechnologies,
    DatabaseTechnologies,
    DateDetails,
    AjaxTechnologies,
    InputTechnologies,
    AuthenticationKeyTypes,
    IndexDisplayOption,
    FrameworkTechnologies,
    Cardinality,
    isHasChoices,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_path_is_not_abstract():
    assert not inspect.isabstract(Path)


def test_path_constructor_exists():
    assert callable(Path.__init__)


def test_path_constructor_args():
    sig = inspect.signature(Path.__init__)
    params = list(sig.parameters.keys())



def test_website_currentuserreference_is_not_abstract():
    assert not inspect.isabstract(website_CurrentUserReference)


def test_website_currentuserreference_constructor_exists():
    assert callable(website_CurrentUserReference.__init__)


def test_website_currentuserreference_constructor_args():
    sig = inspect.signature(website_CurrentUserReference.__init__)
    params = list(sig.parameters.keys())



def test_website_routeparameterreference_is_not_abstract():
    assert not inspect.isabstract(website_RouteParameterReference)


def test_website_routeparameterreference_constructor_exists():
    assert callable(website_RouteParameterReference.__init__)


def test_website_routeparameterreference_constructor_args():
    sig = inspect.signature(website_RouteParameterReference.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_website_routeparameterreference_has_name():
    assert hasattr(website_RouteParameterReference, "name")
    descriptor = None
    for klass in website_RouteParameterReference.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_website_featurereference_is_not_abstract():
    assert not inspect.isabstract(website_FeatureReference)


def test_website_featurereference_constructor_exists():
    assert callable(website_FeatureReference.__init__)


def test_website_featurereference_constructor_args():
    sig = inspect.signature(website_FeatureReference.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_website_featurereference_has_name():
    assert hasattr(website_FeatureReference, "name")
    descriptor = None
    for klass in website_FeatureReference.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_website_modelreference_is_not_abstract():
    assert not inspect.isabstract(website_ModelReference)


def test_website_modelreference_constructor_exists():
    assert callable(website_ModelReference.__init__)


def test_website_modelreference_constructor_args():
    sig = inspect.signature(website_ModelReference.__init__)
    params = list(sig.parameters.keys())



def test_website_parameterreference_is_not_abstract():
    assert not inspect.isabstract(website_ParameterReference)


def test_website_parameterreference_constructor_exists():
    assert callable(website_ParameterReference.__init__)


def test_website_parameterreference_constructor_args():
    sig = inspect.signature(website_ParameterReference.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_website_parameterreference_has_name():
    assert hasattr(website_ParameterReference, "name")
    descriptor = None
    for klass in website_ParameterReference.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_website_inlineactioncontainer_is_not_abstract():
    assert not inspect.isabstract(website_InlineActionContainer)


def test_website_inlineactioncontainer_constructor_exists():
    assert callable(website_InlineActionContainer.__init__)


def test_website_inlineactioncontainer_constructor_args():
    sig = inspect.signature(website_InlineActionContainer.__init__)
    params = list(sig.parameters.keys())



def test_authenticationunit_is_not_abstract():
    assert not inspect.isabstract(AuthenticationUnit)


def test_authenticationunit_constructor_exists():
    assert callable(AuthenticationUnit.__init__)


def test_authenticationunit_constructor_args():
    sig = inspect.signature(AuthenticationUnit.__init__)
    params = list(sig.parameters.keys())



def test_website_authenticationunit_is_not_abstract():
    assert not inspect.isabstract(website_AuthenticationUnit)


def test_website_authenticationunit_constructor_exists():
    assert callable(website_AuthenticationUnit.__init__)


def test_website_authenticationunit_constructor_args():
    sig = inspect.signature(website_AuthenticationUnit.__init__)
    params = list(sig.parameters.keys())



def test_imageunit_is_not_abstract():
    assert not inspect.isabstract(ImageUnit)


def test_imageunit_constructor_exists():
    assert callable(ImageUnit.__init__)


def test_imageunit_constructor_args():
    sig = inspect.signature(ImageUnit.__init__)
    params = list(sig.parameters.keys())



def test_website_galleryunit_is_not_abstract():
    assert not inspect.isabstract(website_GalleryUnit)


def test_website_galleryunit_constructor_exists():
    assert callable(website_GalleryUnit.__init__)


def test_website_galleryunit_constructor_args():
    sig = inspect.signature(website_GalleryUnit.__init__)
    params = list(sig.parameters.keys())
    assert "contentClass" in params, "Missing parameter 'contentClass'"
    assert "styleClass" in params, "Missing parameter 'styleClass'"

def test_website_galleryunit_has_contentClass():
    assert hasattr(website_GalleryUnit, "contentClass")
    descriptor = None
    for klass in website_GalleryUnit.__mro__:
        if "contentClass" in klass.__dict__:
            descriptor = klass.__dict__["contentClass"]
            break
    assert isinstance(descriptor, property)

def test_website_galleryunit_has_styleClass():
    assert hasattr(website_GalleryUnit, "styleClass")
    descriptor = None
    for klass in website_GalleryUnit.__mro__:
        if "styleClass" in klass.__dict__:
            descriptor = klass.__dict__["styleClass"]
            break
    assert isinstance(descriptor, property)



def test_website_sliderunit_is_not_abstract():
    assert not inspect.isabstract(website_SliderUnit)


def test_website_sliderunit_constructor_exists():
    assert callable(website_SliderUnit.__init__)


def test_website_sliderunit_constructor_args():
    sig = inspect.signature(website_SliderUnit.__init__)
    params = list(sig.parameters.keys())
    assert "styleClass" in params, "Missing parameter 'styleClass'"
    assert "contentClass" in params, "Missing parameter 'contentClass'"

def test_website_sliderunit_has_styleClass():
    assert hasattr(website_SliderUnit, "styleClass")
    descriptor = None
    for klass in website_SliderUnit.__mro__:
        if "styleClass" in klass.__dict__:
            descriptor = klass.__dict__["styleClass"]
            break
    assert isinstance(descriptor, property)

def test_website_sliderunit_has_contentClass():
    assert hasattr(website_SliderUnit, "contentClass")
    descriptor = None
    for klass in website_SliderUnit.__mro__:
        if "contentClass" in klass.__dict__:
            descriptor = klass.__dict__["contentClass"]
            break
    assert isinstance(descriptor, property)



def test_inlineaction_is_not_abstract():
    assert not inspect.isabstract(InlineAction)


def test_inlineaction_constructor_exists():
    assert callable(InlineAction.__init__)


def test_inlineaction_constructor_args():
    sig = inspect.signature(InlineAction.__init__)
    params = list(sig.parameters.keys())



def test_website_deleteaction_is_not_abstract():
    assert not inspect.isabstract(website_DeleteAction)


def test_website_deleteaction_constructor_exists():
    assert callable(website_DeleteAction.__init__)


def test_website_deleteaction_constructor_args():
    sig = inspect.signature(website_DeleteAction.__init__)
    params = list(sig.parameters.keys())
    assert "confirmMessage" in params, "Missing parameter 'confirmMessage'"
    assert "uriElement" in params, "Missing parameter 'uriElement'"

def test_website_deleteaction_has_confirmMessage():
    assert hasattr(website_DeleteAction, "confirmMessage")
    descriptor = None
    for klass in website_DeleteAction.__mro__:
        if "confirmMessage" in klass.__dict__:
            descriptor = klass.__dict__["confirmMessage"]
            break
    assert isinstance(descriptor, property)

def test_website_deleteaction_has_uriElement():
    assert hasattr(website_DeleteAction, "uriElement")
    descriptor = None
    for klass in website_DeleteAction.__mro__:
        if "uriElement" in klass.__dict__:
            descriptor = klass.__dict__["uriElement"]
            break
    assert isinstance(descriptor, property)



def test_website_featuresupportaction_is_not_abstract():
    assert not inspect.isabstract(website_FeatureSupportAction)


def test_website_featuresupportaction_constructor_exists():
    assert callable(website_FeatureSupportAction.__init__)


def test_website_featuresupportaction_constructor_args():
    sig = inspect.signature(website_FeatureSupportAction.__init__)
    params = list(sig.parameters.keys())
    assert "fileExtension" in params, "Missing parameter 'fileExtension'"
    assert "uriElement" in params, "Missing parameter 'uriElement'"
    assert "confirmMessage" in params, "Missing parameter 'confirmMessage'"

def test_website_featuresupportaction_has_fileExtension():
    assert hasattr(website_FeatureSupportAction, "fileExtension")
    descriptor = None
    for klass in website_FeatureSupportAction.__mro__:
        if "fileExtension" in klass.__dict__:
            descriptor = klass.__dict__["fileExtension"]
            break
    assert isinstance(descriptor, property)

def test_website_featuresupportaction_has_uriElement():
    assert hasattr(website_FeatureSupportAction, "uriElement")
    descriptor = None
    for klass in website_FeatureSupportAction.__mro__:
        if "uriElement" in klass.__dict__:
            descriptor = klass.__dict__["uriElement"]
            break
    assert isinstance(descriptor, property)

def test_website_featuresupportaction_has_confirmMessage():
    assert hasattr(website_FeatureSupportAction, "confirmMessage")
    descriptor = None
    for klass in website_FeatureSupportAction.__mro__:
        if "confirmMessage" in klass.__dict__:
            descriptor = klass.__dict__["confirmMessage"]
            break
    assert isinstance(descriptor, property)



def test_website_selectaction_is_not_abstract():
    assert not inspect.isabstract(website_SelectAction)


def test_website_selectaction_constructor_exists():
    assert callable(website_SelectAction.__init__)


def test_website_selectaction_constructor_args():
    sig = inspect.signature(website_SelectAction.__init__)
    params = list(sig.parameters.keys())



def test_childpath_is_not_abstract():
    assert not inspect.isabstract(ChildPath)


def test_childpath_constructor_exists():
    assert callable(ChildPath.__init__)


def test_childpath_constructor_args():
    sig = inspect.signature(ChildPath.__init__)
    params = list(sig.parameters.keys())



def test_website_childpathattribute_is_not_abstract():
    assert not inspect.isabstract(website_ChildPathAttribute)


def test_website_childpathattribute_constructor_exists():
    assert callable(website_ChildPathAttribute.__init__)


def test_website_childpathattribute_constructor_args():
    sig = inspect.signature(website_ChildPathAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_website_childpathattribute_has_name():
    assert hasattr(website_ChildPathAttribute, "name")
    descriptor = None
    for klass in website_ChildPathAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_featurepath_is_not_abstract():
    assert not inspect.isabstract(FeaturePath)


def test_featurepath_constructor_exists():
    assert callable(FeaturePath.__init__)


def test_featurepath_constructor_args():
    sig = inspect.signature(FeaturePath.__init__)
    params = list(sig.parameters.keys())



def test_website_featurepathattribute_is_not_abstract():
    assert not inspect.isabstract(website_FeaturePathAttribute)


def test_website_featurepathattribute_constructor_exists():
    assert callable(website_FeaturePathAttribute.__init__)


def test_website_featurepathattribute_constructor_args():
    sig = inspect.signature(website_FeaturePathAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_website_featurepathattribute_has_name():
    assert hasattr(website_FeaturePathAttribute, "name")
    descriptor = None
    for klass in website_FeaturePathAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_website_featurepath_is_not_abstract():
    assert not inspect.isabstract(website_FeaturePath)


def test_website_featurepath_constructor_exists():
    assert callable(website_FeaturePath.__init__)


def test_website_featurepath_constructor_args():
    sig = inspect.signature(website_FeaturePath.__init__)
    params = list(sig.parameters.keys())



def test_collectionunit_is_not_abstract():
    assert not inspect.isabstract(CollectionUnit)


def test_collectionunit_constructor_exists():
    assert callable(CollectionUnit.__init__)


def test_collectionunit_constructor_args():
    sig = inspect.signature(CollectionUnit.__init__)
    params = list(sig.parameters.keys())



def test_dataunit_is_not_abstract():
    assert not inspect.isabstract(DataUnit)


def test_dataunit_constructor_exists():
    assert callable(DataUnit.__init__)


def test_dataunit_constructor_args():
    sig = inspect.signature(DataUnit.__init__)
    params = list(sig.parameters.keys())



def test_controlunit_is_not_abstract():
    assert not inspect.isabstract(ControlUnit)


def test_controlunit_constructor_exists():
    assert callable(ControlUnit.__init__)


def test_controlunit_constructor_args():
    sig = inspect.signature(ControlUnit.__init__)
    params = list(sig.parameters.keys())



def test_website_searchunit_is_not_abstract():
    assert not inspect.isabstract(website_SearchUnit)


def test_website_searchunit_constructor_exists():
    assert callable(website_SearchUnit.__init__)


def test_website_searchunit_constructor_args():
    sig = inspect.signature(website_SearchUnit.__init__)
    params = list(sig.parameters.keys())
    assert "styleClass" in params, "Missing parameter 'styleClass'"

def test_website_searchunit_has_styleClass():
    assert hasattr(website_SearchUnit, "styleClass")
    descriptor = None
    for klass in website_SearchUnit.__mro__:
        if "styleClass" in klass.__dict__:
            descriptor = klass.__dict__["styleClass"]
            break
    assert isinstance(descriptor, property)



def test_singletonunit_is_not_abstract():
    assert not inspect.isabstract(SingletonUnit)


def test_singletonunit_constructor_exists():
    assert callable(SingletonUnit.__init__)


def test_singletonunit_constructor_args():
    sig = inspect.signature(SingletonUnit.__init__)
    params = list(sig.parameters.keys())



def test_dynamicunit_is_not_abstract():
    assert not inspect.isabstract(DynamicUnit)


def test_dynamicunit_constructor_exists():
    assert callable(DynamicUnit.__init__)


def test_dynamicunit_constructor_args():
    sig = inspect.signature(DynamicUnit.__init__)
    params = list(sig.parameters.keys())



def test_website_dataunit_is_not_abstract():
    assert not inspect.isabstract(website_DataUnit)


def test_website_dataunit_constructor_exists():
    assert callable(website_DataUnit.__init__)


def test_website_dataunit_constructor_args():
    sig = inspect.signature(website_DataUnit.__init__)
    params = list(sig.parameters.keys())



def test_website_imageunit_is_not_abstract():
    assert not inspect.isabstract(website_ImageUnit)


def test_website_imageunit_constructor_exists():
    assert callable(website_ImageUnit.__init__)


def test_website_imageunit_constructor_args():
    sig = inspect.signature(website_ImageUnit.__init__)
    params = list(sig.parameters.keys())
    assert "showTime" in params, "Missing parameter 'showTime'"
    assert "transitionTime" in params, "Missing parameter 'transitionTime'"
    assert "missingImagePath" in params, "Missing parameter 'missingImagePath'"

def test_website_imageunit_has_showTime():
    assert hasattr(website_ImageUnit, "showTime")
    descriptor = None
    for klass in website_ImageUnit.__mro__:
        if "showTime" in klass.__dict__:
            descriptor = klass.__dict__["showTime"]
            break
    assert isinstance(descriptor, property)

def test_website_imageunit_has_transitionTime():
    assert hasattr(website_ImageUnit, "transitionTime")
    descriptor = None
    for klass in website_ImageUnit.__mro__:
        if "transitionTime" in klass.__dict__:
            descriptor = klass.__dict__["transitionTime"]
            break
    assert isinstance(descriptor, property)

def test_website_imageunit_has_missingImagePath():
    assert hasattr(website_ImageUnit, "missingImagePath")
    descriptor = None
    for klass in website_ImageUnit.__mro__:
        if "missingImagePath" in klass.__dict__:
            descriptor = klass.__dict__["missingImagePath"]
            break
    assert isinstance(descriptor, property)



def test_website_controlunit_is_not_abstract():
    assert not inspect.isabstract(website_ControlUnit)


def test_website_controlunit_constructor_exists():
    assert callable(website_ControlUnit.__init__)


def test_website_controlunit_constructor_args():
    sig = inspect.signature(website_ControlUnit.__init__)
    params = list(sig.parameters.keys())
    assert "submitLabel" in params, "Missing parameter 'submitLabel'"
    assert "cancelLabel" in params, "Missing parameter 'cancelLabel'"
    assert "contentClass" in params, "Missing parameter 'contentClass'"

def test_website_controlunit_has_submitLabel():
    assert hasattr(website_ControlUnit, "submitLabel")
    descriptor = None
    for klass in website_ControlUnit.__mro__:
        if "submitLabel" in klass.__dict__:
            descriptor = klass.__dict__["submitLabel"]
            break
    assert isinstance(descriptor, property)

def test_website_controlunit_has_cancelLabel():
    assert hasattr(website_ControlUnit, "cancelLabel")
    descriptor = None
    for klass in website_ControlUnit.__mro__:
        if "cancelLabel" in klass.__dict__:
            descriptor = klass.__dict__["cancelLabel"]
            break
    assert isinstance(descriptor, property)

def test_website_controlunit_has_contentClass():
    assert hasattr(website_ControlUnit, "contentClass")
    descriptor = None
    for klass in website_ControlUnit.__mro__:
        if "contentClass" in klass.__dict__:
            descriptor = klass.__dict__["contentClass"]
            break
    assert isinstance(descriptor, property)



def test_website_editunit_is_not_abstract():
    assert not inspect.isabstract(website_EditUnit)


def test_website_editunit_constructor_exists():
    assert callable(website_EditUnit.__init__)


def test_website_editunit_constructor_args():
    sig = inspect.signature(website_EditUnit.__init__)
    params = list(sig.parameters.keys())
    assert "cancelLabel" in params, "Missing parameter 'cancelLabel'"
    assert "contentClass" in params, "Missing parameter 'contentClass'"
    assert "customiseValues" in params, "Missing parameter 'customiseValues'"
    assert "confirmLabel" in params, "Missing parameter 'confirmLabel'"

def test_website_editunit_has_cancelLabel():
    assert hasattr(website_EditUnit, "cancelLabel")
    descriptor = None
    for klass in website_EditUnit.__mro__:
        if "cancelLabel" in klass.__dict__:
            descriptor = klass.__dict__["cancelLabel"]
            break
    assert isinstance(descriptor, property)

def test_website_editunit_has_contentClass():
    assert hasattr(website_EditUnit, "contentClass")
    descriptor = None
    for klass in website_EditUnit.__mro__:
        if "contentClass" in klass.__dict__:
            descriptor = klass.__dict__["contentClass"]
            break
    assert isinstance(descriptor, property)

def test_website_editunit_has_customiseValues():
    assert hasattr(website_EditUnit, "customiseValues")
    descriptor = None
    for klass in website_EditUnit.__mro__:
        if "customiseValues" in klass.__dict__:
            descriptor = klass.__dict__["customiseValues"]
            break
    assert isinstance(descriptor, property)

def test_website_editunit_has_confirmLabel():
    assert hasattr(website_EditUnit, "confirmLabel")
    descriptor = None
    for klass in website_EditUnit.__mro__:
        if "confirmLabel" in klass.__dict__:
            descriptor = klass.__dict__["confirmLabel"]
            break
    assert isinstance(descriptor, property)



def test_editunit_is_not_abstract():
    assert not inspect.isabstract(EditUnit)


def test_editunit_constructor_exists():
    assert callable(EditUnit.__init__)


def test_editunit_constructor_args():
    sig = inspect.signature(EditUnit.__init__)
    params = list(sig.parameters.keys())



def test_website_createunit_is_not_abstract():
    assert not inspect.isabstract(website_CreateUnit)


def test_website_createunit_constructor_exists():
    assert callable(website_CreateUnit.__init__)


def test_website_createunit_constructor_args():
    sig = inspect.signature(website_CreateUnit.__init__)
    params = list(sig.parameters.keys())
    assert "styleClass" in params, "Missing parameter 'styleClass'"

def test_website_createunit_has_styleClass():
    assert hasattr(website_CreateUnit, "styleClass")
    descriptor = None
    for klass in website_CreateUnit.__mro__:
        if "styleClass" in klass.__dict__:
            descriptor = klass.__dict__["styleClass"]
            break
    assert isinstance(descriptor, property)



def test_interfacefield_is_not_abstract():
    assert not inspect.isabstract(InterfaceField)


def test_interfacefield_constructor_exists():
    assert callable(InterfaceField.__init__)


def test_interfacefield_constructor_args():
    sig = inspect.signature(InterfaceField.__init__)
    params = list(sig.parameters.keys())



def test_website_datefield_is_not_abstract():
    assert not inspect.isabstract(website_DateField)


def test_website_datefield_constructor_exists():
    assert callable(website_DateField.__init__)


def test_website_datefield_constructor_args():
    sig = inspect.signature(website_DateField.__init__)
    params = list(sig.parameters.keys())
    assert "format" in params, "Missing parameter 'format'"
    assert "details" in params, "Missing parameter 'details'"

def test_website_datefield_has_format():
    assert hasattr(website_DateField, "format")
    descriptor = None
    for klass in website_DateField.__mro__:
        if "format" in klass.__dict__:
            descriptor = klass.__dict__["format"]
            break
    assert isinstance(descriptor, property)

def test_website_datefield_has_details():
    assert hasattr(website_DateField, "details")
    descriptor = None
    for klass in website_DateField.__mro__:
        if "details" in klass.__dict__:
            descriptor = klass.__dict__["details"]
            break
    assert isinstance(descriptor, property)



def test_website_datatypefield_is_not_abstract():
    assert not inspect.isabstract(website_DataTypeField)


def test_website_datatypefield_constructor_exists():
    assert callable(website_DataTypeField.__init__)


def test_website_datatypefield_constructor_args():
    sig = inspect.signature(website_DataTypeField.__init__)
    params = list(sig.parameters.keys())
    assert "encrypt" in params, "Missing parameter 'encrypt'"
    assert "interfaceType" in params, "Missing parameter 'interfaceType'"
    assert "obfuscateFormFields" in params, "Missing parameter 'obfuscateFormFields'"

def test_website_datatypefield_has_encrypt():
    assert hasattr(website_DataTypeField, "encrypt")
    descriptor = None
    for klass in website_DataTypeField.__mro__:
        if "encrypt" in klass.__dict__:
            descriptor = klass.__dict__["encrypt"]
            break
    assert isinstance(descriptor, property)

def test_website_datatypefield_has_interfaceType():
    assert hasattr(website_DataTypeField, "interfaceType")
    descriptor = None
    for klass in website_DataTypeField.__mro__:
        if "interfaceType" in klass.__dict__:
            descriptor = klass.__dict__["interfaceType"]
            break
    assert isinstance(descriptor, property)

def test_website_datatypefield_has_obfuscateFormFields():
    assert hasattr(website_DataTypeField, "obfuscateFormFields")
    descriptor = None
    for klass in website_DataTypeField.__mro__:
        if "obfuscateFormFields" in klass.__dict__:
            descriptor = klass.__dict__["obfuscateFormFields"]
            break
    assert isinstance(descriptor, property)



def test_website_childpath_is_not_abstract():
    assert not inspect.isabstract(website_ChildPath)


def test_website_childpath_constructor_exists():
    assert callable(website_ChildPath.__init__)


def test_website_childpath_constructor_args():
    sig = inspect.signature(website_ChildPath.__init__)
    params = list(sig.parameters.keys())



def test_website_associationreference_is_not_abstract():
    assert not inspect.isabstract(website_AssociationReference)


def test_website_associationreference_constructor_exists():
    assert callable(website_AssociationReference.__init__)


def test_website_associationreference_constructor_args():
    sig = inspect.signature(website_AssociationReference.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_website_associationreference_has_name():
    assert hasattr(website_AssociationReference, "name")
    descriptor = None
    for klass in website_AssociationReference.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_selectableunit_is_not_abstract():
    assert not inspect.isabstract(SelectableUnit)


def test_selectableunit_constructor_exists():
    assert callable(SelectableUnit.__init__)


def test_selectableunit_constructor_args():
    sig = inspect.signature(SelectableUnit.__init__)
    params = list(sig.parameters.keys())



def test_website_detailsunit_is_not_abstract():
    assert not inspect.isabstract(website_DetailsUnit)


def test_website_detailsunit_constructor_exists():
    assert callable(website_DetailsUnit.__init__)


def test_website_detailsunit_constructor_args():
    sig = inspect.signature(website_DetailsUnit.__init__)
    params = list(sig.parameters.keys())
    assert "contentClass" in params, "Missing parameter 'contentClass'"
    assert "omitFieldLabels" in params, "Missing parameter 'omitFieldLabels'"
    assert "styleClass" in params, "Missing parameter 'styleClass'"
    assert "onlyDisplayWhenNotEmpty" in params, "Missing parameter 'onlyDisplayWhenNotEmpty'"

def test_website_detailsunit_has_contentClass():
    assert hasattr(website_DetailsUnit, "contentClass")
    descriptor = None
    for klass in website_DetailsUnit.__mro__:
        if "contentClass" in klass.__dict__:
            descriptor = klass.__dict__["contentClass"]
            break
    assert isinstance(descriptor, property)

def test_website_detailsunit_has_omitFieldLabels():
    assert hasattr(website_DetailsUnit, "omitFieldLabels")
    descriptor = None
    for klass in website_DetailsUnit.__mro__:
        if "omitFieldLabels" in klass.__dict__:
            descriptor = klass.__dict__["omitFieldLabels"]
            break
    assert isinstance(descriptor, property)

def test_website_detailsunit_has_styleClass():
    assert hasattr(website_DetailsUnit, "styleClass")
    descriptor = None
    for klass in website_DetailsUnit.__mro__:
        if "styleClass" in klass.__dict__:
            descriptor = klass.__dict__["styleClass"]
            break
    assert isinstance(descriptor, property)

def test_website_detailsunit_has_onlyDisplayWhenNotEmpty():
    assert hasattr(website_DetailsUnit, "onlyDisplayWhenNotEmpty")
    descriptor = None
    for klass in website_DetailsUnit.__mro__:
        if "onlyDisplayWhenNotEmpty" in klass.__dict__:
            descriptor = klass.__dict__["onlyDisplayWhenNotEmpty"]
            break
    assert isinstance(descriptor, property)



def test_website_updateunit_is_not_abstract():
    assert not inspect.isabstract(website_UpdateUnit)


def test_website_updateunit_constructor_exists():
    assert callable(website_UpdateUnit.__init__)


def test_website_updateunit_constructor_args():
    sig = inspect.signature(website_UpdateUnit.__init__)
    params = list(sig.parameters.keys())
    assert "styleClass" in params, "Missing parameter 'styleClass'"

def test_website_updateunit_has_styleClass():
    assert hasattr(website_UpdateUnit, "styleClass")
    descriptor = None
    for klass in website_UpdateUnit.__mro__:
        if "styleClass" in klass.__dict__:
            descriptor = klass.__dict__["styleClass"]
            break
    assert isinstance(descriptor, property)



def test_website_createupdateunit_is_not_abstract():
    assert not inspect.isabstract(website_CreateUpdateUnit)


def test_website_createupdateunit_constructor_exists():
    assert callable(website_CreateUpdateUnit.__init__)


def test_website_createupdateunit_constructor_args():
    sig = inspect.signature(website_CreateUpdateUnit.__init__)
    params = list(sig.parameters.keys())
    assert "styleClass" in params, "Missing parameter 'styleClass'"
    assert "clearLabel" in params, "Missing parameter 'clearLabel'"
    assert "createUriElement" in params, "Missing parameter 'createUriElement'"

def test_website_createupdateunit_has_styleClass():
    assert hasattr(website_CreateUpdateUnit, "styleClass")
    descriptor = None
    for klass in website_CreateUpdateUnit.__mro__:
        if "styleClass" in klass.__dict__:
            descriptor = klass.__dict__["styleClass"]
            break
    assert isinstance(descriptor, property)

def test_website_createupdateunit_has_clearLabel():
    assert hasattr(website_CreateUpdateUnit, "clearLabel")
    descriptor = None
    for klass in website_CreateUpdateUnit.__mro__:
        if "clearLabel" in klass.__dict__:
            descriptor = klass.__dict__["clearLabel"]
            break
    assert isinstance(descriptor, property)

def test_website_createupdateunit_has_createUriElement():
    assert hasattr(website_CreateUpdateUnit, "createUriElement")
    descriptor = None
    for klass in website_CreateUpdateUnit.__mro__:
        if "createUriElement" in klass.__dict__:
            descriptor = klass.__dict__["createUriElement"]
            break
    assert isinstance(descriptor, property)



def test_website_mapunit_is_not_abstract():
    assert not inspect.isabstract(website_MapUnit)


def test_website_mapunit_constructor_exists():
    assert callable(website_MapUnit.__init__)


def test_website_mapunit_constructor_args():
    sig = inspect.signature(website_MapUnit.__init__)
    params = list(sig.parameters.keys())
    assert "defaultZoomLevel" in params, "Missing parameter 'defaultZoomLevel'"
    assert "readOnly" in params, "Missing parameter 'readOnly'"
    assert "styleClass" in params, "Missing parameter 'styleClass'"

def test_website_mapunit_has_defaultZoomLevel():
    assert hasattr(website_MapUnit, "defaultZoomLevel")
    descriptor = None
    for klass in website_MapUnit.__mro__:
        if "defaultZoomLevel" in klass.__dict__:
            descriptor = klass.__dict__["defaultZoomLevel"]
            break
    assert isinstance(descriptor, property)

def test_website_mapunit_has_readOnly():
    assert hasattr(website_MapUnit, "readOnly")
    descriptor = None
    for klass in website_MapUnit.__mro__:
        if "readOnly" in klass.__dict__:
            descriptor = klass.__dict__["readOnly"]
            break
    assert isinstance(descriptor, property)

def test_website_mapunit_has_styleClass():
    assert hasattr(website_MapUnit, "styleClass")
    descriptor = None
    for klass in website_MapUnit.__mro__:
        if "styleClass" in klass.__dict__:
            descriptor = klass.__dict__["styleClass"]
            break
    assert isinstance(descriptor, property)



def test_website_collectionunit_is_not_abstract():
    assert not inspect.isabstract(website_CollectionUnit)


def test_website_collectionunit_constructor_exists():
    assert callable(website_CollectionUnit.__init__)


def test_website_collectionunit_constructor_args():
    sig = inspect.signature(website_CollectionUnit.__init__)
    params = list(sig.parameters.keys())
    assert "useFirstLastPageLinks" in params, "Missing parameter 'useFirstLastPageLinks'"
    assert "nextNpages" in params, "Missing parameter 'nextNpages'"
    assert "lastPageLabel" in params, "Missing parameter 'lastPageLabel'"
    assert "useDisabledPageLinks" in params, "Missing parameter 'useDisabledPageLinks'"
    assert "nextPageLabel" in params, "Missing parameter 'nextPageLabel'"
    assert "defaultPaginationSize" in params, "Missing parameter 'defaultPaginationSize'"
    assert "previousNpages" in params, "Missing parameter 'previousNpages'"
    assert "previousPageLabel" in params, "Missing parameter 'previousPageLabel'"
    assert "firstPageLabel" in params, "Missing parameter 'firstPageLabel'"
    assert "emptyMessage" in params, "Missing parameter 'emptyMessage'"

def test_website_collectionunit_has_useFirstLastPageLinks():
    assert hasattr(website_CollectionUnit, "useFirstLastPageLinks")
    descriptor = None
    for klass in website_CollectionUnit.__mro__:
        if "useFirstLastPageLinks" in klass.__dict__:
            descriptor = klass.__dict__["useFirstLastPageLinks"]
            break
    assert isinstance(descriptor, property)

def test_website_collectionunit_has_nextNpages():
    assert hasattr(website_CollectionUnit, "nextNpages")
    descriptor = None
    for klass in website_CollectionUnit.__mro__:
        if "nextNpages" in klass.__dict__:
            descriptor = klass.__dict__["nextNpages"]
            break
    assert isinstance(descriptor, property)

def test_website_collectionunit_has_lastPageLabel():
    assert hasattr(website_CollectionUnit, "lastPageLabel")
    descriptor = None
    for klass in website_CollectionUnit.__mro__:
        if "lastPageLabel" in klass.__dict__:
            descriptor = klass.__dict__["lastPageLabel"]
            break
    assert isinstance(descriptor, property)

def test_website_collectionunit_has_useDisabledPageLinks():
    assert hasattr(website_CollectionUnit, "useDisabledPageLinks")
    descriptor = None
    for klass in website_CollectionUnit.__mro__:
        if "useDisabledPageLinks" in klass.__dict__:
            descriptor = klass.__dict__["useDisabledPageLinks"]
            break
    assert isinstance(descriptor, property)

def test_website_collectionunit_has_nextPageLabel():
    assert hasattr(website_CollectionUnit, "nextPageLabel")
    descriptor = None
    for klass in website_CollectionUnit.__mro__:
        if "nextPageLabel" in klass.__dict__:
            descriptor = klass.__dict__["nextPageLabel"]
            break
    assert isinstance(descriptor, property)

def test_website_collectionunit_has_defaultPaginationSize():
    assert hasattr(website_CollectionUnit, "defaultPaginationSize")
    descriptor = None
    for klass in website_CollectionUnit.__mro__:
        if "defaultPaginationSize" in klass.__dict__:
            descriptor = klass.__dict__["defaultPaginationSize"]
            break
    assert isinstance(descriptor, property)

def test_website_collectionunit_has_previousNpages():
    assert hasattr(website_CollectionUnit, "previousNpages")
    descriptor = None
    for klass in website_CollectionUnit.__mro__:
        if "previousNpages" in klass.__dict__:
            descriptor = klass.__dict__["previousNpages"]
            break
    assert isinstance(descriptor, property)

def test_website_collectionunit_has_previousPageLabel():
    assert hasattr(website_CollectionUnit, "previousPageLabel")
    descriptor = None
    for klass in website_CollectionUnit.__mro__:
        if "previousPageLabel" in klass.__dict__:
            descriptor = klass.__dict__["previousPageLabel"]
            break
    assert isinstance(descriptor, property)

def test_website_collectionunit_has_firstPageLabel():
    assert hasattr(website_CollectionUnit, "firstPageLabel")
    descriptor = None
    for klass in website_CollectionUnit.__mro__:
        if "firstPageLabel" in klass.__dict__:
            descriptor = klass.__dict__["firstPageLabel"]
            break
    assert isinstance(descriptor, property)

def test_website_collectionunit_has_emptyMessage():
    assert hasattr(website_CollectionUnit, "emptyMessage")
    descriptor = None
    for klass in website_CollectionUnit.__mro__:
        if "emptyMessage" in klass.__dict__:
            descriptor = klass.__dict__["emptyMessage"]
            break
    assert isinstance(descriptor, property)



def test_website_singletonunit_is_not_abstract():
    assert not inspect.isabstract(website_SingletonUnit)


def test_website_singletonunit_constructor_exists():
    assert callable(website_SingletonUnit.__init__)


def test_website_singletonunit_constructor_args():
    sig = inspect.signature(website_SingletonUnit.__init__)
    params = list(sig.parameters.keys())



def test_website_selectableunit_is_not_abstract():
    assert not inspect.isabstract(website_SelectableUnit)


def test_website_selectableunit_constructor_exists():
    assert callable(website_SelectableUnit.__init__)


def test_website_selectableunit_constructor_args():
    sig = inspect.signature(website_SelectableUnit.__init__)
    params = list(sig.parameters.keys())



def test_website_captchafield_is_not_abstract():
    assert not inspect.isabstract(website_CaptchaField)


def test_website_captchafield_constructor_exists():
    assert callable(website_CaptchaField.__init__)


def test_website_captchafield_constructor_args():
    sig = inspect.signature(website_CaptchaField.__init__)
    params = list(sig.parameters.keys())



def test_unitfeature_is_not_abstract():
    assert not inspect.isabstract(UnitFeature)


def test_unitfeature_constructor_exists():
    assert callable(UnitFeature.__init__)


def test_unitfeature_constructor_args():
    sig = inspect.signature(UnitFeature.__init__)
    params = list(sig.parameters.keys())



def test_website_unitelement_is_not_abstract():
    assert not inspect.isabstract(website_UnitElement)


def test_website_unitelement_constructor_exists():
    assert callable(website_UnitElement.__init__)


def test_website_unitelement_constructor_args():
    sig = inspect.signature(website_UnitElement.__init__)
    params = list(sig.parameters.keys())
    assert "validationPattern" in params, "Missing parameter 'validationPattern'"
    assert "obfuscateFormFields" in params, "Missing parameter 'obfuscateFormFields'"
    assert "name" in params, "Missing parameter 'name'"
    assert "placeholder" in params, "Missing parameter 'placeholder'"

def test_website_unitelement_has_validationPattern():
    assert hasattr(website_UnitElement, "validationPattern")
    descriptor = None
    for klass in website_UnitElement.__mro__:
        if "validationPattern" in klass.__dict__:
            descriptor = klass.__dict__["validationPattern"]
            break
    assert isinstance(descriptor, property)

def test_website_unitelement_has_obfuscateFormFields():
    assert hasattr(website_UnitElement, "obfuscateFormFields")
    descriptor = None
    for klass in website_UnitElement.__mro__:
        if "obfuscateFormFields" in klass.__dict__:
            descriptor = klass.__dict__["obfuscateFormFields"]
            break
    assert isinstance(descriptor, property)

def test_website_unitelement_has_name():
    assert hasattr(website_UnitElement, "name")
    descriptor = None
    for klass in website_UnitElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_website_unitelement_has_placeholder():
    assert hasattr(website_UnitElement, "placeholder")
    descriptor = None
    for klass in website_UnitElement.__mro__:
        if "placeholder" in klass.__dict__:
            descriptor = klass.__dict__["placeholder"]
            break
    assert isinstance(descriptor, property)



def test_inlineactioncontainer_is_not_abstract():
    assert not inspect.isabstract(InlineActionContainer)


def test_inlineactioncontainer_constructor_exists():
    assert callable(InlineActionContainer.__init__)


def test_inlineactioncontainer_constructor_args():
    sig = inspect.signature(InlineActionContainer.__init__)
    params = list(sig.parameters.keys())



def test_website_indexunit_is_not_abstract():
    assert not inspect.isabstract(website_IndexUnit)


def test_website_indexunit_constructor_exists():
    assert callable(website_IndexUnit.__init__)


def test_website_indexunit_constructor_args():
    sig = inspect.signature(website_IndexUnit.__init__)
    params = list(sig.parameters.keys())
    assert "omitColumnLabels" in params, "Missing parameter 'omitColumnLabels'"
    assert "styleClass" in params, "Missing parameter 'styleClass'"
    assert "displayOption" in params, "Missing parameter 'displayOption'"
    assert "contentClass" in params, "Missing parameter 'contentClass'"
    assert "rowClasses" in params, "Missing parameter 'rowClasses'"

def test_website_indexunit_has_omitColumnLabels():
    assert hasattr(website_IndexUnit, "omitColumnLabels")
    descriptor = None
    for klass in website_IndexUnit.__mro__:
        if "omitColumnLabels" in klass.__dict__:
            descriptor = klass.__dict__["omitColumnLabels"]
            break
    assert isinstance(descriptor, property)

def test_website_indexunit_has_styleClass():
    assert hasattr(website_IndexUnit, "styleClass")
    descriptor = None
    for klass in website_IndexUnit.__mro__:
        if "styleClass" in klass.__dict__:
            descriptor = klass.__dict__["styleClass"]
            break
    assert isinstance(descriptor, property)

def test_website_indexunit_has_displayOption():
    assert hasattr(website_IndexUnit, "displayOption")
    descriptor = None
    for klass in website_IndexUnit.__mro__:
        if "displayOption" in klass.__dict__:
            descriptor = klass.__dict__["displayOption"]
            break
    assert isinstance(descriptor, property)

def test_website_indexunit_has_contentClass():
    assert hasattr(website_IndexUnit, "contentClass")
    descriptor = None
    for klass in website_IndexUnit.__mro__:
        if "contentClass" in klass.__dict__:
            descriptor = klass.__dict__["contentClass"]
            break
    assert isinstance(descriptor, property)

def test_website_indexunit_has_rowClasses():
    assert hasattr(website_IndexUnit, "rowClasses")
    descriptor = None
    for klass in website_IndexUnit.__mro__:
        if "rowClasses" in klass.__dict__:
            descriptor = klass.__dict__["rowClasses"]
            break
    assert isinstance(descriptor, property)



def test_website_imageindexunit_is_not_abstract():
    assert not inspect.isabstract(website_ImageIndexUnit)


def test_website_imageindexunit_constructor_exists():
    assert callable(website_ImageIndexUnit.__init__)


def test_website_imageindexunit_constructor_args():
    sig = inspect.signature(website_ImageIndexUnit.__init__)
    params = list(sig.parameters.keys())
    assert "contentClass" in params, "Missing parameter 'contentClass'"
    assert "styleClass" in params, "Missing parameter 'styleClass'"

def test_website_imageindexunit_has_contentClass():
    assert hasattr(website_ImageIndexUnit, "contentClass")
    descriptor = None
    for klass in website_ImageIndexUnit.__mro__:
        if "contentClass" in klass.__dict__:
            descriptor = klass.__dict__["contentClass"]
            break
    assert isinstance(descriptor, property)

def test_website_imageindexunit_has_styleClass():
    assert hasattr(website_ImageIndexUnit, "styleClass")
    descriptor = None
    for klass in website_ImageIndexUnit.__mro__:
        if "styleClass" in klass.__dict__:
            descriptor = klass.__dict__["styleClass"]
            break
    assert isinstance(descriptor, property)



def test_unitfield_is_not_abstract():
    assert not inspect.isabstract(UnitField)


def test_unitfield_constructor_exists():
    assert callable(UnitField.__init__)


def test_unitfield_constructor_args():
    sig = inspect.signature(UnitField.__init__)
    params = list(sig.parameters.keys())



def test_website_unitfeature_is_not_abstract():
    assert not inspect.isabstract(website_UnitFeature)


def test_website_unitfeature_constructor_exists():
    assert callable(website_UnitFeature.__init__)


def test_website_unitfeature_constructor_args():
    sig = inspect.signature(website_UnitFeature.__init__)
    params = list(sig.parameters.keys())
    assert "displayLabel" in params, "Missing parameter 'displayLabel'"
    assert "displayClass" in params, "Missing parameter 'displayClass'"
    assert "headerClass" in params, "Missing parameter 'headerClass'"
    assert "onlyDisplayWhenNotEmpty" in params, "Missing parameter 'onlyDisplayWhenNotEmpty'"
    assert "footerClass" in params, "Missing parameter 'footerClass'"
    assert "required" in params, "Missing parameter 'required'"
    assert "autofocus" in params, "Missing parameter 'autofocus'"
    assert "inputClass" in params, "Missing parameter 'inputClass'"
    assert "nullDisplayValue" in params, "Missing parameter 'nullDisplayValue'"
    assert "footer" in params, "Missing parameter 'footer'"

def test_website_unitfeature_has_displayLabel():
    assert hasattr(website_UnitFeature, "displayLabel")
    descriptor = None
    for klass in website_UnitFeature.__mro__:
        if "displayLabel" in klass.__dict__:
            descriptor = klass.__dict__["displayLabel"]
            break
    assert isinstance(descriptor, property)

def test_website_unitfeature_has_displayClass():
    assert hasattr(website_UnitFeature, "displayClass")
    descriptor = None
    for klass in website_UnitFeature.__mro__:
        if "displayClass" in klass.__dict__:
            descriptor = klass.__dict__["displayClass"]
            break
    assert isinstance(descriptor, property)

def test_website_unitfeature_has_headerClass():
    assert hasattr(website_UnitFeature, "headerClass")
    descriptor = None
    for klass in website_UnitFeature.__mro__:
        if "headerClass" in klass.__dict__:
            descriptor = klass.__dict__["headerClass"]
            break
    assert isinstance(descriptor, property)

def test_website_unitfeature_has_onlyDisplayWhenNotEmpty():
    assert hasattr(website_UnitFeature, "onlyDisplayWhenNotEmpty")
    descriptor = None
    for klass in website_UnitFeature.__mro__:
        if "onlyDisplayWhenNotEmpty" in klass.__dict__:
            descriptor = klass.__dict__["onlyDisplayWhenNotEmpty"]
            break
    assert isinstance(descriptor, property)

def test_website_unitfeature_has_footerClass():
    assert hasattr(website_UnitFeature, "footerClass")
    descriptor = None
    for klass in website_UnitFeature.__mro__:
        if "footerClass" in klass.__dict__:
            descriptor = klass.__dict__["footerClass"]
            break
    assert isinstance(descriptor, property)

def test_website_unitfeature_has_required():
    assert hasattr(website_UnitFeature, "required")
    descriptor = None
    for klass in website_UnitFeature.__mro__:
        if "required" in klass.__dict__:
            descriptor = klass.__dict__["required"]
            break
    assert isinstance(descriptor, property)

def test_website_unitfeature_has_autofocus():
    assert hasattr(website_UnitFeature, "autofocus")
    descriptor = None
    for klass in website_UnitFeature.__mro__:
        if "autofocus" in klass.__dict__:
            descriptor = klass.__dict__["autofocus"]
            break
    assert isinstance(descriptor, property)

def test_website_unitfeature_has_inputClass():
    assert hasattr(website_UnitFeature, "inputClass")
    descriptor = None
    for klass in website_UnitFeature.__mro__:
        if "inputClass" in klass.__dict__:
            descriptor = klass.__dict__["inputClass"]
            break
    assert isinstance(descriptor, property)

def test_website_unitfeature_has_nullDisplayValue():
    assert hasattr(website_UnitFeature, "nullDisplayValue")
    descriptor = None
    for klass in website_UnitFeature.__mro__:
        if "nullDisplayValue" in klass.__dict__:
            descriptor = klass.__dict__["nullDisplayValue"]
            break
    assert isinstance(descriptor, property)

def test_website_unitfeature_has_footer():
    assert hasattr(website_UnitFeature, "footer")
    descriptor = None
    for klass in website_UnitFeature.__mro__:
        if "footer" in klass.__dict__:
            descriptor = klass.__dict__["footer"]
            break
    assert isinstance(descriptor, property)



def test_associationreference_is_not_abstract():
    assert not inspect.isabstract(AssociationReference)


def test_associationreference_constructor_exists():
    assert callable(AssociationReference.__init__)


def test_associationreference_constructor_args():
    sig = inspect.signature(AssociationReference.__init__)
    params = list(sig.parameters.keys())



def test_website_childpathassociation_is_not_abstract():
    assert not inspect.isabstract(website_ChildPathAssociation)


def test_website_childpathassociation_constructor_exists():
    assert callable(website_ChildPathAssociation.__init__)


def test_website_childpathassociation_constructor_args():
    sig = inspect.signature(website_ChildPathAssociation.__init__)
    params = list(sig.parameters.keys())
    assert "isSourceAssociation" in params, "Missing parameter 'isSourceAssociation'"

def test_website_childpathassociation_has_isSourceAssociation():
    assert hasattr(website_ChildPathAssociation, "isSourceAssociation")
    descriptor = None
    for klass in website_ChildPathAssociation.__mro__:
        if "isSourceAssociation" in klass.__dict__:
            descriptor = klass.__dict__["isSourceAssociation"]
            break
    assert isinstance(descriptor, property)



def test_website_featurepathassociation_is_not_abstract():
    assert not inspect.isabstract(website_FeaturePathAssociation)


def test_website_featurepathassociation_constructor_exists():
    assert callable(website_FeaturePathAssociation.__init__)


def test_website_featurepathassociation_constructor_args():
    sig = inspect.signature(website_FeaturePathAssociation.__init__)
    params = list(sig.parameters.keys())
    assert "isSourceAssociation" in params, "Missing parameter 'isSourceAssociation'"

def test_website_featurepathassociation_has_isSourceAssociation():
    assert hasattr(website_FeaturePathAssociation, "isSourceAssociation")
    descriptor = None
    for klass in website_FeaturePathAssociation.__mro__:
        if "isSourceAssociation" in klass.__dict__:
            descriptor = klass.__dict__["isSourceAssociation"]
            break
    assert isinstance(descriptor, property)



def test_contentunit_is_not_abstract():
    assert not inspect.isabstract(ContentUnit)


def test_contentunit_constructor_exists():
    assert callable(ContentUnit.__init__)


def test_contentunit_constructor_args():
    sig = inspect.signature(ContentUnit.__init__)
    params = list(sig.parameters.keys())



def test_website_createsitemapunit_is_not_abstract():
    assert not inspect.isabstract(website_CreateSitemapUnit)


def test_website_createsitemapunit_constructor_exists():
    assert callable(website_CreateSitemapUnit.__init__)


def test_website_createsitemapunit_constructor_args():
    sig = inspect.signature(website_CreateSitemapUnit.__init__)
    params = list(sig.parameters.keys())
    assert "contentClass" in params, "Missing parameter 'contentClass'"
    assert "styleClass" in params, "Missing parameter 'styleClass'"
    assert "deployedURL" in params, "Missing parameter 'deployedURL'"
    assert "filename" in params, "Missing parameter 'filename'"

def test_website_createsitemapunit_has_contentClass():
    assert hasattr(website_CreateSitemapUnit, "contentClass")
    descriptor = None
    for klass in website_CreateSitemapUnit.__mro__:
        if "contentClass" in klass.__dict__:
            descriptor = klass.__dict__["contentClass"]
            break
    assert isinstance(descriptor, property)

def test_website_createsitemapunit_has_styleClass():
    assert hasattr(website_CreateSitemapUnit, "styleClass")
    descriptor = None
    for klass in website_CreateSitemapUnit.__mro__:
        if "styleClass" in klass.__dict__:
            descriptor = klass.__dict__["styleClass"]
            break
    assert isinstance(descriptor, property)

def test_website_createsitemapunit_has_deployedURL():
    assert hasattr(website_CreateSitemapUnit, "deployedURL")
    descriptor = None
    for klass in website_CreateSitemapUnit.__mro__:
        if "deployedURL" in klass.__dict__:
            descriptor = klass.__dict__["deployedURL"]
            break
    assert isinstance(descriptor, property)

def test_website_createsitemapunit_has_filename():
    assert hasattr(website_CreateSitemapUnit, "filename")
    descriptor = None
    for klass in website_CreateSitemapUnit.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)



def test_website_dynamicunit_is_not_abstract():
    assert not inspect.isabstract(website_DynamicUnit)


def test_website_dynamicunit_constructor_exists():
    assert callable(website_DynamicUnit.__init__)


def test_website_dynamicunit_constructor_args():
    sig = inspect.signature(website_DynamicUnit.__init__)
    params = list(sig.parameters.keys())
    assert "footerClass" in params, "Missing parameter 'footerClass'"
    assert "errorClass" in params, "Missing parameter 'errorClass'"
    assert "controlClass" in params, "Missing parameter 'controlClass'"
    assert "header" in params, "Missing parameter 'header'"
    assert "headerClass" in params, "Missing parameter 'headerClass'"
    assert "footer" in params, "Missing parameter 'footer'"

def test_website_dynamicunit_has_footerClass():
    assert hasattr(website_DynamicUnit, "footerClass")
    descriptor = None
    for klass in website_DynamicUnit.__mro__:
        if "footerClass" in klass.__dict__:
            descriptor = klass.__dict__["footerClass"]
            break
    assert isinstance(descriptor, property)

def test_website_dynamicunit_has_errorClass():
    assert hasattr(website_DynamicUnit, "errorClass")
    descriptor = None
    for klass in website_DynamicUnit.__mro__:
        if "errorClass" in klass.__dict__:
            descriptor = klass.__dict__["errorClass"]
            break
    assert isinstance(descriptor, property)

def test_website_dynamicunit_has_controlClass():
    assert hasattr(website_DynamicUnit, "controlClass")
    descriptor = None
    for klass in website_DynamicUnit.__mro__:
        if "controlClass" in klass.__dict__:
            descriptor = klass.__dict__["controlClass"]
            break
    assert isinstance(descriptor, property)

def test_website_dynamicunit_has_header():
    assert hasattr(website_DynamicUnit, "header")
    descriptor = None
    for klass in website_DynamicUnit.__mro__:
        if "header" in klass.__dict__:
            descriptor = klass.__dict__["header"]
            break
    assert isinstance(descriptor, property)

def test_website_dynamicunit_has_headerClass():
    assert hasattr(website_DynamicUnit, "headerClass")
    descriptor = None
    for klass in website_DynamicUnit.__mro__:
        if "headerClass" in klass.__dict__:
            descriptor = klass.__dict__["headerClass"]
            break
    assert isinstance(descriptor, property)

def test_website_dynamicunit_has_footer():
    assert hasattr(website_DynamicUnit, "footer")
    descriptor = None
    for klass in website_DynamicUnit.__mro__:
        if "footer" in klass.__dict__:
            descriptor = klass.__dict__["footer"]
            break
    assert isinstance(descriptor, property)



def test_website_staticunit_is_not_abstract():
    assert not inspect.isabstract(website_StaticUnit)


def test_website_staticunit_constructor_exists():
    assert callable(website_StaticUnit.__init__)


def test_website_staticunit_constructor_args():
    sig = inspect.signature(website_StaticUnit.__init__)
    params = list(sig.parameters.keys())
    assert "styleClass" in params, "Missing parameter 'styleClass'"
    assert "contentClass" in params, "Missing parameter 'contentClass'"
    assert "content" in params, "Missing parameter 'content'"

def test_website_staticunit_has_styleClass():
    assert hasattr(website_StaticUnit, "styleClass")
    descriptor = None
    for klass in website_StaticUnit.__mro__:
        if "styleClass" in klass.__dict__:
            descriptor = klass.__dict__["styleClass"]
            break
    assert isinstance(descriptor, property)

def test_website_staticunit_has_contentClass():
    assert hasattr(website_StaticUnit, "contentClass")
    descriptor = None
    for klass in website_StaticUnit.__mro__:
        if "contentClass" in klass.__dict__:
            descriptor = klass.__dict__["contentClass"]
            break
    assert isinstance(descriptor, property)

def test_website_staticunit_has_content():
    assert hasattr(website_StaticUnit, "content")
    descriptor = None
    for klass in website_StaticUnit.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_website_unitcontainer_is_not_abstract():
    assert not inspect.isabstract(website_UnitContainer)


def test_website_unitcontainer_constructor_exists():
    assert callable(website_UnitContainer.__init__)


def test_website_unitcontainer_constructor_args():
    sig = inspect.signature(website_UnitContainer.__init__)
    params = list(sig.parameters.keys())



def test_website_unitfield_is_not_abstract():
    assert not inspect.isabstract(website_UnitField)


def test_website_unitfield_constructor_exists():
    assert callable(website_UnitField.__init__)


def test_website_unitfield_constructor_args():
    sig = inspect.signature(website_UnitField.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "collectionAllowRemove" in params, "Missing parameter 'collectionAllowRemove'"
    assert "maximumDisplaySize" in params, "Missing parameter 'maximumDisplaySize'"
    assert "collectionAllowAdd" in params, "Missing parameter 'collectionAllowAdd'"
    assert "collectionDisplayOption" in params, "Missing parameter 'collectionDisplayOption'"
    assert "dateFormat" in params, "Missing parameter 'dateFormat'"

def test_website_unitfield_has_title():
    assert hasattr(website_UnitField, "title")
    descriptor = None
    for klass in website_UnitField.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_website_unitfield_has_collectionAllowRemove():
    assert hasattr(website_UnitField, "collectionAllowRemove")
    descriptor = None
    for klass in website_UnitField.__mro__:
        if "collectionAllowRemove" in klass.__dict__:
            descriptor = klass.__dict__["collectionAllowRemove"]
            break
    assert isinstance(descriptor, property)

def test_website_unitfield_has_maximumDisplaySize():
    assert hasattr(website_UnitField, "maximumDisplaySize")
    descriptor = None
    for klass in website_UnitField.__mro__:
        if "maximumDisplaySize" in klass.__dict__:
            descriptor = klass.__dict__["maximumDisplaySize"]
            break
    assert isinstance(descriptor, property)

def test_website_unitfield_has_collectionAllowAdd():
    assert hasattr(website_UnitField, "collectionAllowAdd")
    descriptor = None
    for klass in website_UnitField.__mro__:
        if "collectionAllowAdd" in klass.__dict__:
            descriptor = klass.__dict__["collectionAllowAdd"]
            break
    assert isinstance(descriptor, property)

def test_website_unitfield_has_collectionDisplayOption():
    assert hasattr(website_UnitField, "collectionDisplayOption")
    descriptor = None
    for klass in website_UnitField.__mro__:
        if "collectionDisplayOption" in klass.__dict__:
            descriptor = klass.__dict__["collectionDisplayOption"]
            break
    assert isinstance(descriptor, property)

def test_website_unitfield_has_dateFormat():
    assert hasattr(website_UnitField, "dateFormat")
    descriptor = None
    for klass in website_UnitField.__mro__:
        if "dateFormat" in klass.__dict__:
            descriptor = klass.__dict__["dateFormat"]
            break
    assert isinstance(descriptor, property)



def test_website_query_is_not_abstract():
    assert not inspect.isabstract(website_Query)


def test_website_query_constructor_exists():
    assert callable(website_Query.__init__)


def test_website_query_constructor_args():
    sig = inspect.signature(website_Query.__init__)
    params = list(sig.parameters.keys())



def test_menuentry_is_not_abstract():
    assert not inspect.isabstract(MenuEntry)


def test_menuentry_constructor_exists():
    assert callable(MenuEntry.__init__)


def test_menuentry_constructor_args():
    sig = inspect.signature(MenuEntry.__init__)
    params = list(sig.parameters.keys())



def test_website_menufeature_is_not_abstract():
    assert not inspect.isabstract(website_MenuFeature)


def test_website_menufeature_constructor_exists():
    assert callable(website_MenuFeature.__init__)


def test_website_menufeature_constructor_args():
    sig = inspect.signature(website_MenuFeature.__init__)
    params = list(sig.parameters.keys())



def test_menu_is_not_abstract():
    assert not inspect.isabstract(Menu)


def test_menu_constructor_exists():
    assert callable(Menu.__init__)


def test_menu_constructor_args():
    sig = inspect.signature(Menu.__init__)
    params = list(sig.parameters.keys())



def test_website_dynamicmenu_is_not_abstract():
    assert not inspect.isabstract(website_DynamicMenu)


def test_website_dynamicmenu_constructor_exists():
    assert callable(website_DynamicMenu.__init__)


def test_website_dynamicmenu_constructor_args():
    sig = inspect.signature(website_DynamicMenu.__init__)
    params = list(sig.parameters.keys())



def test_website_staticmenu_is_not_abstract():
    assert not inspect.isabstract(website_StaticMenu)


def test_website_staticmenu_constructor_exists():
    assert callable(website_StaticMenu.__init__)


def test_website_staticmenu_constructor_args():
    sig = inspect.signature(website_StaticMenu.__init__)
    params = list(sig.parameters.keys())



def test_website_menuentry_is_not_abstract():
    assert not inspect.isabstract(website_MenuEntry)


def test_website_menuentry_constructor_exists():
    assert callable(website_MenuEntry.__init__)


def test_website_menuentry_constructor_args():
    sig = inspect.signature(website_MenuEntry.__init__)
    params = list(sig.parameters.keys())
    assert "requiresRole" in params, "Missing parameter 'requiresRole'"

def test_website_menuentry_has_requiresRole():
    assert hasattr(website_MenuEntry, "requiresRole")
    descriptor = None
    for klass in website_MenuEntry.__mro__:
        if "requiresRole" in klass.__dict__:
            descriptor = klass.__dict__["requiresRole"]
            break
    assert isinstance(descriptor, property)



def test_website_queryparameter_is_not_abstract():
    assert not inspect.isabstract(website_QueryParameter)


def test_website_queryparameter_constructor_exists():
    assert callable(website_QueryParameter.__init__)


def test_website_queryparameter_constructor_args():
    sig = inspect.signature(website_QueryParameter.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_website_queryparameter_has_value():
    assert hasattr(website_QueryParameter, "value")
    descriptor = None
    for klass in website_QueryParameter.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_unitcontainer_is_not_abstract():
    assert not inspect.isabstract(UnitContainer)


def test_unitcontainer_constructor_exists():
    assert callable(UnitContainer.__init__)


def test_unitcontainer_constructor_args():
    sig = inspect.signature(UnitContainer.__init__)
    params = list(sig.parameters.keys())



def test_website_unitassociation_is_not_abstract():
    assert not inspect.isabstract(website_UnitAssociation)


def test_website_unitassociation_constructor_exists():
    assert callable(website_UnitAssociation.__init__)


def test_website_unitassociation_constructor_args():
    sig = inspect.signature(website_UnitAssociation.__init__)
    params = list(sig.parameters.keys())
    assert "isSourceAssociation" in params, "Missing parameter 'isSourceAssociation'"

def test_website_unitassociation_has_isSourceAssociation():
    assert hasattr(website_UnitAssociation, "isSourceAssociation")
    descriptor = None
    for klass in website_UnitAssociation.__mro__:
        if "isSourceAssociation" in klass.__dict__:
            descriptor = klass.__dict__["isSourceAssociation"]
            break
    assert isinstance(descriptor, property)



def test_imagefilter_is_not_abstract():
    assert not inspect.isabstract(ImageFilter)


def test_imagefilter_constructor_exists():
    assert callable(ImageFilter.__init__)


def test_imagefilter_constructor_args():
    sig = inspect.signature(ImageFilter.__init__)
    params = list(sig.parameters.keys())



def test_website_thumbnailfilter_is_not_abstract():
    assert not inspect.isabstract(website_ThumbnailFilter)


def test_website_thumbnailfilter_constructor_exists():
    assert callable(website_ThumbnailFilter.__init__)


def test_website_thumbnailfilter_constructor_args():
    sig = inspect.signature(website_ThumbnailFilter.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"

def test_website_thumbnailfilter_has_height():
    assert hasattr(website_ThumbnailFilter, "height")
    descriptor = None
    for klass in website_ThumbnailFilter.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_website_thumbnailfilter_has_width():
    assert hasattr(website_ThumbnailFilter, "width")
    descriptor = None
    for klass in website_ThumbnailFilter.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_website_imagefilter_is_not_abstract():
    assert not inspect.isabstract(website_ImageFilter)


def test_website_imagefilter_constructor_exists():
    assert callable(website_ImageFilter.__init__)


def test_website_imagefilter_constructor_args():
    sig = inspect.signature(website_ImageFilter.__init__)
    params = list(sig.parameters.keys())



def test_website_order_is_not_abstract():
    assert not inspect.isabstract(website_Order)


def test_website_order_constructor_exists():
    assert callable(website_Order.__init__)


def test_website_order_constructor_args():
    sig = inspect.signature(website_Order.__init__)
    params = list(sig.parameters.keys())



def test_website_predicate_is_not_abstract():
    assert not inspect.isabstract(website_Predicate)


def test_website_predicate_constructor_exists():
    assert callable(website_Predicate.__init__)


def test_website_predicate_constructor_args():
    sig = inspect.signature(website_Predicate.__init__)
    params = list(sig.parameters.keys())



def test_website_pagelink_is_not_abstract():
    assert not inspect.isabstract(website_PageLink)


def test_website_pagelink_constructor_exists():
    assert callable(website_PageLink.__init__)


def test_website_pagelink_constructor_args():
    sig = inspect.signature(website_PageLink.__init__)
    params = list(sig.parameters.keys())



def test_entityassociation_is_not_abstract():
    assert not inspect.isabstract(EntityAssociation)


def test_entityassociation_constructor_exists():
    assert callable(EntityAssociation.__init__)


def test_entityassociation_constructor_args():
    sig = inspect.signature(EntityAssociation.__init__)
    params = list(sig.parameters.keys())



def test_website_associationwithcontainment_is_not_abstract():
    assert not inspect.isabstract(website_AssociationWithContainment)


def test_website_associationwithcontainment_constructor_exists():
    assert callable(website_AssociationWithContainment.__init__)


def test_website_associationwithcontainment_constructor_args():
    sig = inspect.signature(website_AssociationWithContainment.__init__)
    params = list(sig.parameters.keys())
    assert "sourceVisible" in params, "Missing parameter 'sourceVisible'"

def test_website_associationwithcontainment_has_sourceVisible():
    assert hasattr(website_AssociationWithContainment, "sourceVisible")
    descriptor = None
    for klass in website_AssociationWithContainment.__mro__:
        if "sourceVisible" in klass.__dict__:
            descriptor = klass.__dict__["sourceVisible"]
            break
    assert isinstance(descriptor, property)



def test_website_associationwithoutcontainment_is_not_abstract():
    assert not inspect.isabstract(website_AssociationWithoutContainment)


def test_website_associationwithoutcontainment_constructor_exists():
    assert callable(website_AssociationWithoutContainment.__init__)


def test_website_associationwithoutcontainment_constructor_args():
    sig = inspect.signature(website_AssociationWithoutContainment.__init__)
    params = list(sig.parameters.keys())
    assert "targetUnique" in params, "Missing parameter 'targetUnique'"
    assert "targetCardinality" in params, "Missing parameter 'targetCardinality'"

def test_website_associationwithoutcontainment_has_targetUnique():
    assert hasattr(website_AssociationWithoutContainment, "targetUnique")
    descriptor = None
    for klass in website_AssociationWithoutContainment.__mro__:
        if "targetUnique" in klass.__dict__:
            descriptor = klass.__dict__["targetUnique"]
            break
    assert isinstance(descriptor, property)

def test_website_associationwithoutcontainment_has_targetCardinality():
    assert hasattr(website_AssociationWithoutContainment, "targetCardinality")
    descriptor = None
    for klass in website_AssociationWithoutContainment.__mro__:
        if "targetCardinality" in klass.__dict__:
            descriptor = klass.__dict__["targetCardinality"]
            break
    assert isinstance(descriptor, property)



def test_encapsulatedfeature_is_not_abstract():
    assert not inspect.isabstract(EncapsulatedFeature)


def test_encapsulatedfeature_constructor_exists():
    assert callable(EncapsulatedFeature.__init__)


def test_encapsulatedfeature_constructor_args():
    sig = inspect.signature(EncapsulatedFeature.__init__)
    params = list(sig.parameters.keys())



def test_viewfeature_is_not_abstract():
    assert not inspect.isabstract(ViewFeature)


def test_viewfeature_constructor_exists():
    assert callable(ViewFeature.__init__)


def test_viewfeature_constructor_args():
    sig = inspect.signature(ViewFeature.__init__)
    params = list(sig.parameters.keys())



def test_website_encapsulatedfeature_is_not_abstract():
    assert not inspect.isabstract(website_EncapsulatedFeature)


def test_website_encapsulatedfeature_constructor_exists():
    assert callable(website_EncapsulatedFeature.__init__)


def test_website_encapsulatedfeature_constructor_args():
    sig = inspect.signature(website_EncapsulatedFeature.__init__)
    params = list(sig.parameters.keys())
    assert "columnName" in params, "Missing parameter 'columnName'"
    assert "displayLabel" in params, "Missing parameter 'displayLabel'"
    assert "alias" in params, "Missing parameter 'alias'"

def test_website_encapsulatedfeature_has_columnName():
    assert hasattr(website_EncapsulatedFeature, "columnName")
    descriptor = None
    for klass in website_EncapsulatedFeature.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)

def test_website_encapsulatedfeature_has_displayLabel():
    assert hasattr(website_EncapsulatedFeature, "displayLabel")
    descriptor = None
    for klass in website_EncapsulatedFeature.__mro__:
        if "displayLabel" in klass.__dict__:
            descriptor = klass.__dict__["displayLabel"]
            break
    assert isinstance(descriptor, property)

def test_website_encapsulatedfeature_has_alias():
    assert hasattr(website_EncapsulatedFeature, "alias")
    descriptor = None
    for klass in website_EncapsulatedFeature.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)



def test_pathelement_is_not_abstract():
    assert not inspect.isabstract(PathElement)


def test_pathelement_constructor_exists():
    assert callable(PathElement.__init__)


def test_pathelement_constructor_args():
    sig = inspect.signature(PathElement.__init__)
    params = list(sig.parameters.keys())



def test_website_datepathelement_is_not_abstract():
    assert not inspect.isabstract(website_DatePathElement)


def test_website_datepathelement_constructor_exists():
    assert callable(website_DatePathElement.__init__)


def test_website_datepathelement_constructor_args():
    sig = inspect.signature(website_DatePathElement.__init__)
    params = list(sig.parameters.keys())
    assert "format" in params, "Missing parameter 'format'"

def test_website_datepathelement_has_format():
    assert hasattr(website_DatePathElement, "format")
    descriptor = None
    for klass in website_DatePathElement.__mro__:
        if "format" in klass.__dict__:
            descriptor = klass.__dict__["format"]
            break
    assert isinstance(descriptor, property)



def test_website_staticpathelement_is_not_abstract():
    assert not inspect.isabstract(website_StaticPathElement)


def test_website_staticpathelement_constructor_exists():
    assert callable(website_StaticPathElement.__init__)


def test_website_staticpathelement_constructor_args():
    sig = inspect.signature(website_StaticPathElement.__init__)
    params = list(sig.parameters.keys())
    assert "element" in params, "Missing parameter 'element'"

def test_website_staticpathelement_has_element():
    assert hasattr(website_StaticPathElement, "element")
    descriptor = None
    for klass in website_StaticPathElement.__mro__:
        if "element" in klass.__dict__:
            descriptor = klass.__dict__["element"]
            break
    assert isinstance(descriptor, property)



def test_website_pathelement_is_not_abstract():
    assert not inspect.isabstract(website_PathElement)


def test_website_pathelement_constructor_exists():
    assert callable(website_PathElement.__init__)


def test_website_pathelement_constructor_args():
    sig = inspect.signature(website_PathElement.__init__)
    params = list(sig.parameters.keys())



def test_entityattribute_is_not_abstract():
    assert not inspect.isabstract(EntityAttribute)


def test_entityattribute_constructor_exists():
    assert callable(EntityAttribute.__init__)


def test_entityattribute_constructor_args():
    sig = inspect.signature(EntityAttribute.__init__)
    params = list(sig.parameters.keys())



def test_website_dateattribute_is_not_abstract():
    assert not inspect.isabstract(website_DateAttribute)


def test_website_dateattribute_constructor_exists():
    assert callable(website_DateAttribute.__init__)


def test_website_dateattribute_constructor_args():
    sig = inspect.signature(website_DateAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "format" in params, "Missing parameter 'format'"
    assert "details" in params, "Missing parameter 'details'"

def test_website_dateattribute_has_format():
    assert hasattr(website_DateAttribute, "format")
    descriptor = None
    for klass in website_DateAttribute.__mro__:
        if "format" in klass.__dict__:
            descriptor = klass.__dict__["format"]
            break
    assert isinstance(descriptor, property)

def test_website_dateattribute_has_details():
    assert hasattr(website_DateAttribute, "details")
    descriptor = None
    for klass in website_DateAttribute.__mro__:
        if "details" in klass.__dict__:
            descriptor = klass.__dict__["details"]
            break
    assert isinstance(descriptor, property)



def test_website_urlattribute_is_not_abstract():
    assert not inspect.isabstract(website_UrlAttribute)


def test_website_urlattribute_constructor_exists():
    assert callable(website_UrlAttribute.__init__)


def test_website_urlattribute_constructor_args():
    sig = inspect.signature(website_UrlAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "displayValue" in params, "Missing parameter 'displayValue'"

def test_website_urlattribute_has_displayValue():
    assert hasattr(website_UrlAttribute, "displayValue")
    descriptor = None
    for klass in website_UrlAttribute.__mro__:
        if "displayValue" in klass.__dict__:
            descriptor = klass.__dict__["displayValue"]
            break
    assert isinstance(descriptor, property)



def test_website_resourceattribute_is_not_abstract():
    assert not inspect.isabstract(website_ResourceAttribute)


def test_website_resourceattribute_constructor_exists():
    assert callable(website_ResourceAttribute.__init__)


def test_website_resourceattribute_constructor_args():
    sig = inspect.signature(website_ResourceAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "validUploadMimeTypes" in params, "Missing parameter 'validUploadMimeTypes'"
    assert "uploadsWithinWebsite" in params, "Missing parameter 'uploadsWithinWebsite'"
    assert "validUploadExtensions" in params, "Missing parameter 'validUploadExtensions'"
    assert "maximumUploadSize" in params, "Missing parameter 'maximumUploadSize'"

def test_website_resourceattribute_has_validUploadMimeTypes():
    assert hasattr(website_ResourceAttribute, "validUploadMimeTypes")
    descriptor = None
    for klass in website_ResourceAttribute.__mro__:
        if "validUploadMimeTypes" in klass.__dict__:
            descriptor = klass.__dict__["validUploadMimeTypes"]
            break
    assert isinstance(descriptor, property)

def test_website_resourceattribute_has_uploadsWithinWebsite():
    assert hasattr(website_ResourceAttribute, "uploadsWithinWebsite")
    descriptor = None
    for klass in website_ResourceAttribute.__mro__:
        if "uploadsWithinWebsite" in klass.__dict__:
            descriptor = klass.__dict__["uploadsWithinWebsite"]
            break
    assert isinstance(descriptor, property)

def test_website_resourceattribute_has_validUploadExtensions():
    assert hasattr(website_ResourceAttribute, "validUploadExtensions")
    descriptor = None
    for klass in website_ResourceAttribute.__mro__:
        if "validUploadExtensions" in klass.__dict__:
            descriptor = klass.__dict__["validUploadExtensions"]
            break
    assert isinstance(descriptor, property)

def test_website_resourceattribute_has_maximumUploadSize():
    assert hasattr(website_ResourceAttribute, "maximumUploadSize")
    descriptor = None
    for klass in website_ResourceAttribute.__mro__:
        if "maximumUploadSize" in klass.__dict__:
            descriptor = klass.__dict__["maximumUploadSize"]
            break
    assert isinstance(descriptor, property)



def test_website_datatypeattribute_is_not_abstract():
    assert not inspect.isabstract(website_DataTypeAttribute)


def test_website_datatypeattribute_constructor_exists():
    assert callable(website_DataTypeAttribute.__init__)


def test_website_datatypeattribute_constructor_args():
    sig = inspect.signature(website_DataTypeAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "obfuscateFormFields" in params, "Missing parameter 'obfuscateFormFields'"
    assert "encrypt" in params, "Missing parameter 'encrypt'"
    assert "caseInsensitive" in params, "Missing parameter 'caseInsensitive'"

def test_website_datatypeattribute_has_obfuscateFormFields():
    assert hasattr(website_DataTypeAttribute, "obfuscateFormFields")
    descriptor = None
    for klass in website_DataTypeAttribute.__mro__:
        if "obfuscateFormFields" in klass.__dict__:
            descriptor = klass.__dict__["obfuscateFormFields"]
            break
    assert isinstance(descriptor, property)

def test_website_datatypeattribute_has_encrypt():
    assert hasattr(website_DataTypeAttribute, "encrypt")
    descriptor = None
    for klass in website_DataTypeAttribute.__mro__:
        if "encrypt" in klass.__dict__:
            descriptor = klass.__dict__["encrypt"]
            break
    assert isinstance(descriptor, property)

def test_website_datatypeattribute_has_caseInsensitive():
    assert hasattr(website_DataTypeAttribute, "caseInsensitive")
    descriptor = None
    for klass in website_DataTypeAttribute.__mro__:
        if "caseInsensitive" in klass.__dict__:
            descriptor = klass.__dict__["caseInsensitive"]
            break
    assert isinstance(descriptor, property)



def test_attribute_is_not_abstract():
    assert not inspect.isabstract(Attribute)


def test_attribute_constructor_exists():
    assert callable(Attribute.__init__)


def test_attribute_constructor_args():
    sig = inspect.signature(Attribute.__init__)
    params = list(sig.parameters.keys())



def test_website_encapsulatedattribute_is_not_abstract():
    assert not inspect.isabstract(website_EncapsulatedAttribute)


def test_website_encapsulatedattribute_constructor_exists():
    assert callable(website_EncapsulatedAttribute.__init__)


def test_website_encapsulatedattribute_constructor_args():
    sig = inspect.signature(website_EncapsulatedAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "cardinality" in params, "Missing parameter 'cardinality'"

def test_website_encapsulatedattribute_has_name():
    assert hasattr(website_EncapsulatedAttribute, "name")
    descriptor = None
    for klass in website_EncapsulatedAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_website_encapsulatedattribute_has_cardinality():
    assert hasattr(website_EncapsulatedAttribute, "cardinality")
    descriptor = None
    for klass in website_EncapsulatedAttribute.__mro__:
        if "cardinality" in klass.__dict__:
            descriptor = klass.__dict__["cardinality"]
            break
    assert isinstance(descriptor, property)



def test_entityfeature_is_not_abstract():
    assert not inspect.isabstract(EntityFeature)


def test_entityfeature_constructor_exists():
    assert callable(EntityFeature.__init__)


def test_entityfeature_constructor_args():
    sig = inspect.signature(EntityFeature.__init__)
    params = list(sig.parameters.keys())



def test_website_associationkey_is_not_abstract():
    assert not inspect.isabstract(website_AssociationKey)


def test_website_associationkey_constructor_exists():
    assert callable(website_AssociationKey.__init__)


def test_website_associationkey_constructor_args():
    sig = inspect.signature(website_AssociationKey.__init__)
    params = list(sig.parameters.keys())
    assert "targetColumnName" in params, "Missing parameter 'targetColumnName'"

def test_website_associationkey_has_targetColumnName():
    assert hasattr(website_AssociationKey, "targetColumnName")
    descriptor = None
    for klass in website_AssociationKey.__mro__:
        if "targetColumnName" in klass.__dict__:
            descriptor = klass.__dict__["targetColumnName"]
            break
    assert isinstance(descriptor, property)



def test_association_is_not_abstract():
    assert not inspect.isabstract(Association)


def test_association_constructor_exists():
    assert callable(Association.__init__)


def test_association_constructor_args():
    sig = inspect.signature(Association.__init__)
    params = list(sig.parameters.keys())



def test_website_locationattribute_is_not_abstract():
    assert not inspect.isabstract(website_LocationAttribute)


def test_website_locationattribute_constructor_exists():
    assert callable(website_LocationAttribute.__init__)


def test_website_locationattribute_constructor_args():
    sig = inspect.signature(website_LocationAttribute.__init__)
    params = list(sig.parameters.keys())



def test_resourceattribute_is_not_abstract():
    assert not inspect.isabstract(ResourceAttribute)


def test_resourceattribute_constructor_exists():
    assert callable(ResourceAttribute.__init__)


def test_resourceattribute_constructor_args():
    sig = inspect.signature(ResourceAttribute.__init__)
    params = list(sig.parameters.keys())



def test_website_imageattribute_is_not_abstract():
    assert not inspect.isabstract(website_ImageAttribute)


def test_website_imageattribute_constructor_exists():
    assert callable(website_ImageAttribute.__init__)


def test_website_imageattribute_constructor_args():
    sig = inspect.signature(website_ImageAttribute.__init__)
    params = list(sig.parameters.keys())



def test_website_fileattribute_is_not_abstract():
    assert not inspect.isabstract(website_FileAttribute)


def test_website_fileattribute_constructor_exists():
    assert callable(website_FileAttribute.__init__)


def test_website_fileattribute_constructor_args():
    sig = inspect.signature(website_FileAttribute.__init__)
    params = list(sig.parameters.keys())



def test_entityorview_is_not_abstract():
    assert not inspect.isabstract(EntityOrView)


def test_entityorview_constructor_exists():
    assert callable(EntityOrView.__init__)


def test_entityorview_constructor_args():
    sig = inspect.signature(EntityOrView.__init__)
    params = list(sig.parameters.keys())



def test_website_view_is_not_abstract():
    assert not inspect.isabstract(website_View)


def test_website_view_constructor_exists():
    assert callable(website_View.__init__)


def test_website_view_constructor_args():
    sig = inspect.signature(website_View.__init__)
    params = list(sig.parameters.keys())



def test_website_entity_is_not_abstract():
    assert not inspect.isabstract(website_Entity)


def test_website_entity_constructor_exists():
    assert callable(website_Entity.__init__)


def test_website_entity_constructor_args():
    sig = inspect.signature(website_Entity.__init__)
    params = list(sig.parameters.keys())



def test_website_entityassociation_is_not_abstract():
    assert not inspect.isabstract(website_EntityAssociation)


def test_website_entityassociation_constructor_exists():
    assert callable(website_EntityAssociation.__init__)


def test_website_entityassociation_constructor_args():
    sig = inspect.signature(website_EntityAssociation.__init__)
    params = list(sig.parameters.keys())
    assert "targetDisplayClass" in params, "Missing parameter 'targetDisplayClass'"
    assert "targetInputClass" in params, "Missing parameter 'targetInputClass'"
    assert "targetPrimaryKey" in params, "Missing parameter 'targetPrimaryKey'"
    assert "pivotTableName" in params, "Missing parameter 'pivotTableName'"
    assert "targetFooterClass" in params, "Missing parameter 'targetFooterClass'"
    assert "targetDisplayLabel" in params, "Missing parameter 'targetDisplayLabel'"
    assert "targetHeaderClass" in params, "Missing parameter 'targetHeaderClass'"
    assert "bidirectional" in params, "Missing parameter 'bidirectional'"
    assert "targetFeatureName" in params, "Missing parameter 'targetFeatureName'"

def test_website_entityassociation_has_targetDisplayClass():
    assert hasattr(website_EntityAssociation, "targetDisplayClass")
    descriptor = None
    for klass in website_EntityAssociation.__mro__:
        if "targetDisplayClass" in klass.__dict__:
            descriptor = klass.__dict__["targetDisplayClass"]
            break
    assert isinstance(descriptor, property)

def test_website_entityassociation_has_targetInputClass():
    assert hasattr(website_EntityAssociation, "targetInputClass")
    descriptor = None
    for klass in website_EntityAssociation.__mro__:
        if "targetInputClass" in klass.__dict__:
            descriptor = klass.__dict__["targetInputClass"]
            break
    assert isinstance(descriptor, property)

def test_website_entityassociation_has_targetPrimaryKey():
    assert hasattr(website_EntityAssociation, "targetPrimaryKey")
    descriptor = None
    for klass in website_EntityAssociation.__mro__:
        if "targetPrimaryKey" in klass.__dict__:
            descriptor = klass.__dict__["targetPrimaryKey"]
            break
    assert isinstance(descriptor, property)

def test_website_entityassociation_has_pivotTableName():
    assert hasattr(website_EntityAssociation, "pivotTableName")
    descriptor = None
    for klass in website_EntityAssociation.__mro__:
        if "pivotTableName" in klass.__dict__:
            descriptor = klass.__dict__["pivotTableName"]
            break
    assert isinstance(descriptor, property)

def test_website_entityassociation_has_targetFooterClass():
    assert hasattr(website_EntityAssociation, "targetFooterClass")
    descriptor = None
    for klass in website_EntityAssociation.__mro__:
        if "targetFooterClass" in klass.__dict__:
            descriptor = klass.__dict__["targetFooterClass"]
            break
    assert isinstance(descriptor, property)

def test_website_entityassociation_has_targetDisplayLabel():
    assert hasattr(website_EntityAssociation, "targetDisplayLabel")
    descriptor = None
    for klass in website_EntityAssociation.__mro__:
        if "targetDisplayLabel" in klass.__dict__:
            descriptor = klass.__dict__["targetDisplayLabel"]
            break
    assert isinstance(descriptor, property)

def test_website_entityassociation_has_targetHeaderClass():
    assert hasattr(website_EntityAssociation, "targetHeaderClass")
    descriptor = None
    for klass in website_EntityAssociation.__mro__:
        if "targetHeaderClass" in klass.__dict__:
            descriptor = klass.__dict__["targetHeaderClass"]
            break
    assert isinstance(descriptor, property)

def test_website_entityassociation_has_bidirectional():
    assert hasattr(website_EntityAssociation, "bidirectional")
    descriptor = None
    for klass in website_EntityAssociation.__mro__:
        if "bidirectional" in klass.__dict__:
            descriptor = klass.__dict__["bidirectional"]
            break
    assert isinstance(descriptor, property)

def test_website_entityassociation_has_targetFeatureName():
    assert hasattr(website_EntityAssociation, "targetFeatureName")
    descriptor = None
    for klass in website_EntityAssociation.__mro__:
        if "targetFeatureName" in klass.__dict__:
            descriptor = klass.__dict__["targetFeatureName"]
            break
    assert isinstance(descriptor, property)



def test_modellabelfeature_is_not_abstract():
    assert not inspect.isabstract(ModelLabelFeature)


def test_modellabelfeature_constructor_exists():
    assert callable(ModelLabelFeature.__init__)


def test_modellabelfeature_constructor_args():
    sig = inspect.signature(ModelLabelFeature.__init__)
    params = list(sig.parameters.keys())



def test_website_modellabelassociation_is_not_abstract():
    assert not inspect.isabstract(website_ModelLabelAssociation)


def test_website_modellabelassociation_constructor_exists():
    assert callable(website_ModelLabelAssociation.__init__)


def test_website_modellabelassociation_constructor_args():
    sig = inspect.signature(website_ModelLabelAssociation.__init__)
    params = list(sig.parameters.keys())
    assert "isSourceAssociation" in params, "Missing parameter 'isSourceAssociation'"

def test_website_modellabelassociation_has_isSourceAssociation():
    assert hasattr(website_ModelLabelAssociation, "isSourceAssociation")
    descriptor = None
    for klass in website_ModelLabelAssociation.__mro__:
        if "isSourceAssociation" in klass.__dict__:
            descriptor = klass.__dict__["isSourceAssociation"]
            break
    assert isinstance(descriptor, property)



def test_website_modellabelattribute_is_not_abstract():
    assert not inspect.isabstract(website_ModelLabelAttribute)


def test_website_modellabelattribute_constructor_exists():
    assert callable(website_ModelLabelAttribute.__init__)


def test_website_modellabelattribute_constructor_args():
    sig = inspect.signature(website_ModelLabelAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "dateFormat" in params, "Missing parameter 'dateFormat'"

def test_website_modellabelattribute_has_dateFormat():
    assert hasattr(website_ModelLabelAttribute, "dateFormat")
    descriptor = None
    for klass in website_ModelLabelAttribute.__mro__:
        if "dateFormat" in klass.__dict__:
            descriptor = klass.__dict__["dateFormat"]
            break
    assert isinstance(descriptor, property)



def test_website_modellabelfeature_is_not_abstract():
    assert not inspect.isabstract(website_ModelLabelFeature)


def test_website_modellabelfeature_constructor_exists():
    assert callable(website_ModelLabelFeature.__init__)


def test_website_modellabelfeature_constructor_args():
    sig = inspect.signature(website_ModelLabelFeature.__init__)
    params = list(sig.parameters.keys())



def test_website_label_is_not_abstract():
    assert not inspect.isabstract(website_Label)


def test_website_label_constructor_exists():
    assert callable(website_Label.__init__)


def test_website_label_constructor_args():
    sig = inspect.signature(website_Label.__init__)
    params = list(sig.parameters.keys())



def test_website_entityattribute_is_not_abstract():
    assert not inspect.isabstract(website_EntityAttribute)


def test_website_entityattribute_constructor_exists():
    assert callable(website_EntityAttribute.__init__)


def test_website_entityattribute_constructor_args():
    sig = inspect.signature(website_EntityAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "persistentType" in params, "Missing parameter 'persistentType'"
    assert "interfaceType" in params, "Missing parameter 'interfaceType'"
    assert "containerUnique" in params, "Missing parameter 'containerUnique'"
    assert "primaryKey" in params, "Missing parameter 'primaryKey'"
    assert "ormType" in params, "Missing parameter 'ormType'"

def test_website_entityattribute_has_persistentType():
    assert hasattr(website_EntityAttribute, "persistentType")
    descriptor = None
    for klass in website_EntityAttribute.__mro__:
        if "persistentType" in klass.__dict__:
            descriptor = klass.__dict__["persistentType"]
            break
    assert isinstance(descriptor, property)

def test_website_entityattribute_has_interfaceType():
    assert hasattr(website_EntityAttribute, "interfaceType")
    descriptor = None
    for klass in website_EntityAttribute.__mro__:
        if "interfaceType" in klass.__dict__:
            descriptor = klass.__dict__["interfaceType"]
            break
    assert isinstance(descriptor, property)

def test_website_entityattribute_has_containerUnique():
    assert hasattr(website_EntityAttribute, "containerUnique")
    descriptor = None
    for klass in website_EntityAttribute.__mro__:
        if "containerUnique" in klass.__dict__:
            descriptor = klass.__dict__["containerUnique"]
            break
    assert isinstance(descriptor, property)

def test_website_entityattribute_has_primaryKey():
    assert hasattr(website_EntityAttribute, "primaryKey")
    descriptor = None
    for klass in website_EntityAttribute.__mro__:
        if "primaryKey" in klass.__dict__:
            descriptor = klass.__dict__["primaryKey"]
            break
    assert isinstance(descriptor, property)

def test_website_entityattribute_has_ormType():
    assert hasattr(website_EntityAttribute, "ormType")
    descriptor = None
    for klass in website_EntityAttribute.__mro__:
        if "ormType" in klass.__dict__:
            descriptor = klass.__dict__["ormType"]
            break
    assert isinstance(descriptor, property)



def test_website_expression_is_not_abstract():
    assert not inspect.isabstract(website_Expression)


def test_website_expression_constructor_exists():
    assert callable(website_Expression.__init__)


def test_website_expression_constructor_args():
    sig = inspect.signature(website_Expression.__init__)
    params = list(sig.parameters.keys())



def test_label_is_not_abstract():
    assert not inspect.isabstract(Label)


def test_label_constructor_exists():
    assert callable(Label.__init__)


def test_label_constructor_args():
    sig = inspect.signature(Label.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_website_viewfeature_is_not_abstract():
    assert not inspect.isabstract(website_ViewFeature)


def test_website_viewfeature_constructor_exists():
    assert callable(website_ViewFeature.__init__)


def test_website_viewfeature_constructor_args():
    sig = inspect.signature(website_ViewFeature.__init__)
    params = list(sig.parameters.keys())



def test_website_association_is_not_abstract():
    assert not inspect.isabstract(website_Association)


def test_website_association_constructor_exists():
    assert callable(website_Association.__init__)


def test_website_association_constructor_args():
    sig = inspect.signature(website_Association.__init__)
    params = list(sig.parameters.keys())
    assert "pseudo" in params, "Missing parameter 'pseudo'"
    assert "inputClass" in params, "Missing parameter 'inputClass'"
    assert "serializationMaxDepth" in params, "Missing parameter 'serializationMaxDepth'"

def test_website_association_has_pseudo():
    assert hasattr(website_Association, "pseudo")
    descriptor = None
    for klass in website_Association.__mro__:
        if "pseudo" in klass.__dict__:
            descriptor = klass.__dict__["pseudo"]
            break
    assert isinstance(descriptor, property)

def test_website_association_has_inputClass():
    assert hasattr(website_Association, "inputClass")
    descriptor = None
    for klass in website_Association.__mro__:
        if "inputClass" in klass.__dict__:
            descriptor = klass.__dict__["inputClass"]
            break
    assert isinstance(descriptor, property)

def test_website_association_has_serializationMaxDepth():
    assert hasattr(website_Association, "serializationMaxDepth")
    descriptor = None
    for klass in website_Association.__mro__:
        if "serializationMaxDepth" in klass.__dict__:
            descriptor = klass.__dict__["serializationMaxDepth"]
            break
    assert isinstance(descriptor, property)



def test_website_encapsulatedassociation_is_not_abstract():
    assert not inspect.isabstract(website_EncapsulatedAssociation)


def test_website_encapsulatedassociation_constructor_exists():
    assert callable(website_EncapsulatedAssociation.__init__)


def test_website_encapsulatedassociation_constructor_args():
    sig = inspect.signature(website_EncapsulatedAssociation.__init__)
    params = list(sig.parameters.keys())
    assert "cardinality" in params, "Missing parameter 'cardinality'"
    assert "name" in params, "Missing parameter 'name'"
    assert "isSourceAssociation" in params, "Missing parameter 'isSourceAssociation'"

def test_website_encapsulatedassociation_has_cardinality():
    assert hasattr(website_EncapsulatedAssociation, "cardinality")
    descriptor = None
    for klass in website_EncapsulatedAssociation.__mro__:
        if "cardinality" in klass.__dict__:
            descriptor = klass.__dict__["cardinality"]
            break
    assert isinstance(descriptor, property)

def test_website_encapsulatedassociation_has_name():
    assert hasattr(website_EncapsulatedAssociation, "name")
    descriptor = None
    for klass in website_EncapsulatedAssociation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_website_encapsulatedassociation_has_isSourceAssociation():
    assert hasattr(website_EncapsulatedAssociation, "isSourceAssociation")
    descriptor = None
    for klass in website_EncapsulatedAssociation.__mro__:
        if "isSourceAssociation" in klass.__dict__:
            descriptor = klass.__dict__["isSourceAssociation"]
            break
    assert isinstance(descriptor, property)



def test_website_feature_is_not_abstract():
    assert not inspect.isabstract(website_Feature)


def test_website_feature_constructor_exists():
    assert callable(website_Feature.__init__)


def test_website_feature_constructor_args():
    sig = inspect.signature(website_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "serializationExpose" in params, "Missing parameter 'serializationExpose'"
    assert "displayClass" in params, "Missing parameter 'displayClass'"
    assert "collectionAllowAdd" in params, "Missing parameter 'collectionAllowAdd'"
    assert "encodeUriKey" in params, "Missing parameter 'encodeUriKey'"
    assert "nullDisplayValue" in params, "Missing parameter 'nullDisplayValue'"
    assert "serializationGroups" in params, "Missing parameter 'serializationGroups'"
    assert "headerClass" in params, "Missing parameter 'headerClass'"
    assert "footerClass" in params, "Missing parameter 'footerClass'"
    assert "collectionAllowRemove" in params, "Missing parameter 'collectionAllowRemove'"
    assert "title" in params, "Missing parameter 'title'"

def test_website_feature_has_serializationExpose():
    assert hasattr(website_Feature, "serializationExpose")
    descriptor = None
    for klass in website_Feature.__mro__:
        if "serializationExpose" in klass.__dict__:
            descriptor = klass.__dict__["serializationExpose"]
            break
    assert isinstance(descriptor, property)

def test_website_feature_has_displayClass():
    assert hasattr(website_Feature, "displayClass")
    descriptor = None
    for klass in website_Feature.__mro__:
        if "displayClass" in klass.__dict__:
            descriptor = klass.__dict__["displayClass"]
            break
    assert isinstance(descriptor, property)

def test_website_feature_has_collectionAllowAdd():
    assert hasattr(website_Feature, "collectionAllowAdd")
    descriptor = None
    for klass in website_Feature.__mro__:
        if "collectionAllowAdd" in klass.__dict__:
            descriptor = klass.__dict__["collectionAllowAdd"]
            break
    assert isinstance(descriptor, property)

def test_website_feature_has_encodeUriKey():
    assert hasattr(website_Feature, "encodeUriKey")
    descriptor = None
    for klass in website_Feature.__mro__:
        if "encodeUriKey" in klass.__dict__:
            descriptor = klass.__dict__["encodeUriKey"]
            break
    assert isinstance(descriptor, property)

def test_website_feature_has_nullDisplayValue():
    assert hasattr(website_Feature, "nullDisplayValue")
    descriptor = None
    for klass in website_Feature.__mro__:
        if "nullDisplayValue" in klass.__dict__:
            descriptor = klass.__dict__["nullDisplayValue"]
            break
    assert isinstance(descriptor, property)

def test_website_feature_has_serializationGroups():
    assert hasattr(website_Feature, "serializationGroups")
    descriptor = None
    for klass in website_Feature.__mro__:
        if "serializationGroups" in klass.__dict__:
            descriptor = klass.__dict__["serializationGroups"]
            break
    assert isinstance(descriptor, property)

def test_website_feature_has_headerClass():
    assert hasattr(website_Feature, "headerClass")
    descriptor = None
    for klass in website_Feature.__mro__:
        if "headerClass" in klass.__dict__:
            descriptor = klass.__dict__["headerClass"]
            break
    assert isinstance(descriptor, property)

def test_website_feature_has_footerClass():
    assert hasattr(website_Feature, "footerClass")
    descriptor = None
    for klass in website_Feature.__mro__:
        if "footerClass" in klass.__dict__:
            descriptor = klass.__dict__["footerClass"]
            break
    assert isinstance(descriptor, property)

def test_website_feature_has_collectionAllowRemove():
    assert hasattr(website_Feature, "collectionAllowRemove")
    descriptor = None
    for klass in website_Feature.__mro__:
        if "collectionAllowRemove" in klass.__dict__:
            descriptor = klass.__dict__["collectionAllowRemove"]
            break
    assert isinstance(descriptor, property)

def test_website_feature_has_title():
    assert hasattr(website_Feature, "title")
    descriptor = None
    for klass in website_Feature.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_website_enumerationtype_is_not_abstract():
    assert not inspect.isabstract(website_EnumerationType)


def test_website_enumerationtype_constructor_exists():
    assert callable(website_EnumerationType.__init__)


def test_website_enumerationtype_constructor_args():
    sig = inspect.signature(website_EnumerationType.__init__)
    params = list(sig.parameters.keys())



def test_website_namedelement_is_not_abstract():
    assert not inspect.isabstract(website_NamedElement)


def test_website_namedelement_constructor_exists():
    assert callable(website_NamedElement.__init__)


def test_website_namedelement_constructor_args():
    sig = inspect.signature(website_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_website_namedelement_has_name():
    assert hasattr(website_NamedElement, "name")
    descriptor = None
    for klass in website_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_website_forgottenpasswordunit_is_not_abstract():
    assert not inspect.isabstract(website_ForgottenPasswordUnit)


def test_website_forgottenpasswordunit_constructor_exists():
    assert callable(website_ForgottenPasswordUnit.__init__)


def test_website_forgottenpasswordunit_constructor_args():
    sig = inspect.signature(website_ForgottenPasswordUnit.__init__)
    params = list(sig.parameters.keys())
    assert "styleClass" in params, "Missing parameter 'styleClass'"

def test_website_forgottenpasswordunit_has_styleClass():
    assert hasattr(website_ForgottenPasswordUnit, "styleClass")
    descriptor = None
    for klass in website_ForgottenPasswordUnit.__mro__:
        if "styleClass" in klass.__dict__:
            descriptor = klass.__dict__["styleClass"]
            break
    assert isinstance(descriptor, property)



def test_website_loginunit_is_not_abstract():
    assert not inspect.isabstract(website_LoginUnit)


def test_website_loginunit_constructor_exists():
    assert callable(website_LoginUnit.__init__)


def test_website_loginunit_constructor_args():
    sig = inspect.signature(website_LoginUnit.__init__)
    params = list(sig.parameters.keys())
    assert "styleClass" in params, "Missing parameter 'styleClass'"
    assert "logoutUriElement" in params, "Missing parameter 'logoutUriElement'"

def test_website_loginunit_has_styleClass():
    assert hasattr(website_LoginUnit, "styleClass")
    descriptor = None
    for klass in website_LoginUnit.__mro__:
        if "styleClass" in klass.__dict__:
            descriptor = klass.__dict__["styleClass"]
            break
    assert isinstance(descriptor, property)

def test_website_loginunit_has_logoutUriElement():
    assert hasattr(website_LoginUnit, "logoutUriElement")
    descriptor = None
    for klass in website_LoginUnit.__mro__:
        if "logoutUriElement" in klass.__dict__:
            descriptor = klass.__dict__["logoutUriElement"]
            break
    assert isinstance(descriptor, property)



def test_website_registrationunit_is_not_abstract():
    assert not inspect.isabstract(website_RegistrationUnit)


def test_website_registrationunit_constructor_exists():
    assert callable(website_RegistrationUnit.__init__)


def test_website_registrationunit_constructor_args():
    sig = inspect.signature(website_RegistrationUnit.__init__)
    params = list(sig.parameters.keys())
    assert "styleClass" in params, "Missing parameter 'styleClass'"

def test_website_registrationunit_has_styleClass():
    assert hasattr(website_RegistrationUnit, "styleClass")
    descriptor = None
    for klass in website_RegistrationUnit.__mro__:
        if "styleClass" in klass.__dict__:
            descriptor = klass.__dict__["styleClass"]
            break
    assert isinstance(descriptor, property)



def test_authentication_is_not_abstract():
    assert not inspect.isabstract(Authentication)


def test_authentication_constructor_exists():
    assert callable(Authentication.__init__)


def test_authentication_constructor_args():
    sig = inspect.signature(Authentication.__init__)
    params = list(sig.parameters.keys())



def test_website_casauthentication_is_not_abstract():
    assert not inspect.isabstract(website_CasAuthentication)


def test_website_casauthentication_constructor_exists():
    assert callable(website_CasAuthentication.__init__)


def test_website_casauthentication_constructor_args():
    sig = inspect.signature(website_CasAuthentication.__init__)
    params = list(sig.parameters.keys())



def test_website_localauthenticationsystem_is_not_abstract():
    assert not inspect.isabstract(website_LocalAuthenticationSystem)


def test_website_localauthenticationsystem_constructor_exists():
    assert callable(website_LocalAuthenticationSystem.__init__)


def test_website_localauthenticationsystem_constructor_args():
    sig = inspect.signature(website_LocalAuthenticationSystem.__init__)
    params = list(sig.parameters.keys())
    assert "authenticationKey" in params, "Missing parameter 'authenticationKey'"
    assert "sendWelcomeEmail" in params, "Missing parameter 'sendWelcomeEmail'"
    assert "allowRememberMe" in params, "Missing parameter 'allowRememberMe'"
    assert "useCaptcha" in params, "Missing parameter 'useCaptcha'"
    assert "trackLoginAttempts" in params, "Missing parameter 'trackLoginAttempts'"
    assert "useEmailActivation" in params, "Missing parameter 'useEmailActivation'"
    assert "allowSelfRegistration" in params, "Missing parameter 'allowSelfRegistration'"

def test_website_localauthenticationsystem_has_authenticationKey():
    assert hasattr(website_LocalAuthenticationSystem, "authenticationKey")
    descriptor = None
    for klass in website_LocalAuthenticationSystem.__mro__:
        if "authenticationKey" in klass.__dict__:
            descriptor = klass.__dict__["authenticationKey"]
            break
    assert isinstance(descriptor, property)

def test_website_localauthenticationsystem_has_sendWelcomeEmail():
    assert hasattr(website_LocalAuthenticationSystem, "sendWelcomeEmail")
    descriptor = None
    for klass in website_LocalAuthenticationSystem.__mro__:
        if "sendWelcomeEmail" in klass.__dict__:
            descriptor = klass.__dict__["sendWelcomeEmail"]
            break
    assert isinstance(descriptor, property)

def test_website_localauthenticationsystem_has_allowRememberMe():
    assert hasattr(website_LocalAuthenticationSystem, "allowRememberMe")
    descriptor = None
    for klass in website_LocalAuthenticationSystem.__mro__:
        if "allowRememberMe" in klass.__dict__:
            descriptor = klass.__dict__["allowRememberMe"]
            break
    assert isinstance(descriptor, property)

def test_website_localauthenticationsystem_has_useCaptcha():
    assert hasattr(website_LocalAuthenticationSystem, "useCaptcha")
    descriptor = None
    for klass in website_LocalAuthenticationSystem.__mro__:
        if "useCaptcha" in klass.__dict__:
            descriptor = klass.__dict__["useCaptcha"]
            break
    assert isinstance(descriptor, property)

def test_website_localauthenticationsystem_has_trackLoginAttempts():
    assert hasattr(website_LocalAuthenticationSystem, "trackLoginAttempts")
    descriptor = None
    for klass in website_LocalAuthenticationSystem.__mro__:
        if "trackLoginAttempts" in klass.__dict__:
            descriptor = klass.__dict__["trackLoginAttempts"]
            break
    assert isinstance(descriptor, property)

def test_website_localauthenticationsystem_has_useEmailActivation():
    assert hasattr(website_LocalAuthenticationSystem, "useEmailActivation")
    descriptor = None
    for klass in website_LocalAuthenticationSystem.__mro__:
        if "useEmailActivation" in klass.__dict__:
            descriptor = klass.__dict__["useEmailActivation"]
            break
    assert isinstance(descriptor, property)

def test_website_localauthenticationsystem_has_allowSelfRegistration():
    assert hasattr(website_LocalAuthenticationSystem, "allowSelfRegistration")
    descriptor = None
    for klass in website_LocalAuthenticationSystem.__mro__:
        if "allowSelfRegistration" in klass.__dict__:
            descriptor = klass.__dict__["allowSelfRegistration"]
            break
    assert isinstance(descriptor, property)



def test_website_attribute_is_not_abstract():
    assert not inspect.isabstract(website_Attribute)


def test_website_attribute_constructor_exists():
    assert callable(website_Attribute.__init__)


def test_website_attribute_constructor_args():
    sig = inspect.signature(website_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "inputClass" in params, "Missing parameter 'inputClass'"
    assert "placeholder" in params, "Missing parameter 'placeholder'"
    assert "validationPattern" in params, "Missing parameter 'validationPattern'"

def test_website_attribute_has_inputClass():
    assert hasattr(website_Attribute, "inputClass")
    descriptor = None
    for klass in website_Attribute.__mro__:
        if "inputClass" in klass.__dict__:
            descriptor = klass.__dict__["inputClass"]
            break
    assert isinstance(descriptor, property)

def test_website_attribute_has_placeholder():
    assert hasattr(website_Attribute, "placeholder")
    descriptor = None
    for klass in website_Attribute.__mro__:
        if "placeholder" in klass.__dict__:
            descriptor = klass.__dict__["placeholder"]
            break
    assert isinstance(descriptor, property)

def test_website_attribute_has_validationPattern():
    assert hasattr(website_Attribute, "validationPattern")
    descriptor = None
    for klass in website_Attribute.__mro__:
        if "validationPattern" in klass.__dict__:
            descriptor = klass.__dict__["validationPattern"]
            break
    assert isinstance(descriptor, property)



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_website_datatype_is_not_abstract():
    assert not inspect.isabstract(website_DataType)


def test_website_datatype_constructor_exists():
    assert callable(website_DataType.__init__)


def test_website_datatype_constructor_args():
    sig = inspect.signature(website_DataType.__init__)
    params = list(sig.parameters.keys())
    assert "interfaceType" in params, "Missing parameter 'interfaceType'"
    assert "persistentType" in params, "Missing parameter 'persistentType'"
    assert "placeholder" in params, "Missing parameter 'placeholder'"
    assert "ormType" in params, "Missing parameter 'ormType'"
    assert "validationPattern" in params, "Missing parameter 'validationPattern'"

def test_website_datatype_has_interfaceType():
    assert hasattr(website_DataType, "interfaceType")
    descriptor = None
    for klass in website_DataType.__mro__:
        if "interfaceType" in klass.__dict__:
            descriptor = klass.__dict__["interfaceType"]
            break
    assert isinstance(descriptor, property)

def test_website_datatype_has_persistentType():
    assert hasattr(website_DataType, "persistentType")
    descriptor = None
    for klass in website_DataType.__mro__:
        if "persistentType" in klass.__dict__:
            descriptor = klass.__dict__["persistentType"]
            break
    assert isinstance(descriptor, property)

def test_website_datatype_has_placeholder():
    assert hasattr(website_DataType, "placeholder")
    descriptor = None
    for klass in website_DataType.__mro__:
        if "placeholder" in klass.__dict__:
            descriptor = klass.__dict__["placeholder"]
            break
    assert isinstance(descriptor, property)

def test_website_datatype_has_ormType():
    assert hasattr(website_DataType, "ormType")
    descriptor = None
    for klass in website_DataType.__mro__:
        if "ormType" in klass.__dict__:
            descriptor = klass.__dict__["ormType"]
            break
    assert isinstance(descriptor, property)

def test_website_datatype_has_validationPattern():
    assert hasattr(website_DataType, "validationPattern")
    descriptor = None
    for klass in website_DataType.__mro__:
        if "validationPattern" in klass.__dict__:
            descriptor = klass.__dict__["validationPattern"]
            break
    assert isinstance(descriptor, property)



def test_nameddisplayelement_is_not_abstract():
    assert not inspect.isabstract(NamedDisplayElement)


def test_nameddisplayelement_constructor_exists():
    assert callable(NamedDisplayElement.__init__)


def test_nameddisplayelement_constructor_args():
    sig = inspect.signature(NamedDisplayElement.__init__)
    params = list(sig.parameters.keys())



def test_website_contentunit_is_not_abstract():
    assert not inspect.isabstract(website_ContentUnit)


def test_website_contentunit_constructor_exists():
    assert callable(website_ContentUnit.__init__)


def test_website_contentunit_constructor_args():
    sig = inspect.signature(website_ContentUnit.__init__)
    params = list(sig.parameters.keys())
    assert "alternative" in params, "Missing parameter 'alternative'"
    assert "requiresRole" in params, "Missing parameter 'requiresRole'"
    assert "purposeSummary" in params, "Missing parameter 'purposeSummary'"
    assert "uriElement" in params, "Missing parameter 'uriElement'"
    assert "captionClass" in params, "Missing parameter 'captionClass'"
    assert "omitCaption" in params, "Missing parameter 'omitCaption'"
    assert "createDefaultUriElement" in params, "Missing parameter 'createDefaultUriElement'"

def test_website_contentunit_has_alternative():
    assert hasattr(website_ContentUnit, "alternative")
    descriptor = None
    for klass in website_ContentUnit.__mro__:
        if "alternative" in klass.__dict__:
            descriptor = klass.__dict__["alternative"]
            break
    assert isinstance(descriptor, property)

def test_website_contentunit_has_requiresRole():
    assert hasattr(website_ContentUnit, "requiresRole")
    descriptor = None
    for klass in website_ContentUnit.__mro__:
        if "requiresRole" in klass.__dict__:
            descriptor = klass.__dict__["requiresRole"]
            break
    assert isinstance(descriptor, property)

def test_website_contentunit_has_purposeSummary():
    assert hasattr(website_ContentUnit, "purposeSummary")
    descriptor = None
    for klass in website_ContentUnit.__mro__:
        if "purposeSummary" in klass.__dict__:
            descriptor = klass.__dict__["purposeSummary"]
            break
    assert isinstance(descriptor, property)

def test_website_contentunit_has_uriElement():
    assert hasattr(website_ContentUnit, "uriElement")
    descriptor = None
    for klass in website_ContentUnit.__mro__:
        if "uriElement" in klass.__dict__:
            descriptor = klass.__dict__["uriElement"]
            break
    assert isinstance(descriptor, property)

def test_website_contentunit_has_captionClass():
    assert hasattr(website_ContentUnit, "captionClass")
    descriptor = None
    for klass in website_ContentUnit.__mro__:
        if "captionClass" in klass.__dict__:
            descriptor = klass.__dict__["captionClass"]
            break
    assert isinstance(descriptor, property)

def test_website_contentunit_has_omitCaption():
    assert hasattr(website_ContentUnit, "omitCaption")
    descriptor = None
    for klass in website_ContentUnit.__mro__:
        if "omitCaption" in klass.__dict__:
            descriptor = klass.__dict__["omitCaption"]
            break
    assert isinstance(descriptor, property)

def test_website_contentunit_has_createDefaultUriElement():
    assert hasattr(website_ContentUnit, "createDefaultUriElement")
    descriptor = None
    for klass in website_ContentUnit.__mro__:
        if "createDefaultUriElement" in klass.__dict__:
            descriptor = klass.__dict__["createDefaultUriElement"]
            break
    assert isinstance(descriptor, property)



def test_website_interfacefield_is_not_abstract():
    assert not inspect.isabstract(website_InterfaceField)


def test_website_interfacefield_constructor_exists():
    assert callable(website_InterfaceField.__init__)


def test_website_interfacefield_constructor_args():
    sig = inspect.signature(website_InterfaceField.__init__)
    params = list(sig.parameters.keys())
    assert "inputClass" in params, "Missing parameter 'inputClass'"
    assert "required" in params, "Missing parameter 'required'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "validationPattern" in params, "Missing parameter 'validationPattern'"
    assert "placeholder" in params, "Missing parameter 'placeholder'"

def test_website_interfacefield_has_inputClass():
    assert hasattr(website_InterfaceField, "inputClass")
    descriptor = None
    for klass in website_InterfaceField.__mro__:
        if "inputClass" in klass.__dict__:
            descriptor = klass.__dict__["inputClass"]
            break
    assert isinstance(descriptor, property)

def test_website_interfacefield_has_required():
    assert hasattr(website_InterfaceField, "required")
    descriptor = None
    for klass in website_InterfaceField.__mro__:
        if "required" in klass.__dict__:
            descriptor = klass.__dict__["required"]
            break
    assert isinstance(descriptor, property)

def test_website_interfacefield_has_defaultValue():
    assert hasattr(website_InterfaceField, "defaultValue")
    descriptor = None
    for klass in website_InterfaceField.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)

def test_website_interfacefield_has_validationPattern():
    assert hasattr(website_InterfaceField, "validationPattern")
    descriptor = None
    for klass in website_InterfaceField.__mro__:
        if "validationPattern" in klass.__dict__:
            descriptor = klass.__dict__["validationPattern"]
            break
    assert isinstance(descriptor, property)

def test_website_interfacefield_has_placeholder():
    assert hasattr(website_InterfaceField, "placeholder")
    descriptor = None
    for klass in website_InterfaceField.__mro__:
        if "placeholder" in klass.__dict__:
            descriptor = klass.__dict__["placeholder"]
            break
    assert isinstance(descriptor, property)



def test_website_editstatictextmenuentry_is_not_abstract():
    assert not inspect.isabstract(website_EditStaticTextMenuEntry)


def test_website_editstatictextmenuentry_constructor_exists():
    assert callable(website_EditStaticTextMenuEntry.__init__)


def test_website_editstatictextmenuentry_constructor_args():
    sig = inspect.signature(website_EditStaticTextMenuEntry.__init__)
    params = list(sig.parameters.keys())



def test_website_entityfeature_is_not_abstract():
    assert not inspect.isabstract(website_EntityFeature)


def test_website_entityfeature_constructor_exists():
    assert callable(website_EntityFeature.__init__)


def test_website_entityfeature_constructor_args():
    sig = inspect.signature(website_EntityFeature.__init__)
    params = list(sig.parameters.keys())
    assert "columnName" in params, "Missing parameter 'columnName'"
    assert "singletonName" in params, "Missing parameter 'singletonName'"
    assert "cardinality" in params, "Missing parameter 'cardinality'"
    assert "pluralisedName" in params, "Missing parameter 'pluralisedName'"
    assert "ordered" in params, "Missing parameter 'ordered'"
    assert "booleanIsHasChoice" in params, "Missing parameter 'booleanIsHasChoice'"
    assert "unique" in params, "Missing parameter 'unique'"

def test_website_entityfeature_has_columnName():
    assert hasattr(website_EntityFeature, "columnName")
    descriptor = None
    for klass in website_EntityFeature.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)

def test_website_entityfeature_has_singletonName():
    assert hasattr(website_EntityFeature, "singletonName")
    descriptor = None
    for klass in website_EntityFeature.__mro__:
        if "singletonName" in klass.__dict__:
            descriptor = klass.__dict__["singletonName"]
            break
    assert isinstance(descriptor, property)

def test_website_entityfeature_has_cardinality():
    assert hasattr(website_EntityFeature, "cardinality")
    descriptor = None
    for klass in website_EntityFeature.__mro__:
        if "cardinality" in klass.__dict__:
            descriptor = klass.__dict__["cardinality"]
            break
    assert isinstance(descriptor, property)

def test_website_entityfeature_has_pluralisedName():
    assert hasattr(website_EntityFeature, "pluralisedName")
    descriptor = None
    for klass in website_EntityFeature.__mro__:
        if "pluralisedName" in klass.__dict__:
            descriptor = klass.__dict__["pluralisedName"]
            break
    assert isinstance(descriptor, property)

def test_website_entityfeature_has_ordered():
    assert hasattr(website_EntityFeature, "ordered")
    descriptor = None
    for klass in website_EntityFeature.__mro__:
        if "ordered" in klass.__dict__:
            descriptor = klass.__dict__["ordered"]
            break
    assert isinstance(descriptor, property)

def test_website_entityfeature_has_booleanIsHasChoice():
    assert hasattr(website_EntityFeature, "booleanIsHasChoice")
    descriptor = None
    for klass in website_EntityFeature.__mro__:
        if "booleanIsHasChoice" in klass.__dict__:
            descriptor = klass.__dict__["booleanIsHasChoice"]
            break
    assert isinstance(descriptor, property)

def test_website_entityfeature_has_unique():
    assert hasattr(website_EntityFeature, "unique")
    descriptor = None
    for klass in website_EntityFeature.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)



def test_website_inlineaction_is_not_abstract():
    assert not inspect.isabstract(website_InlineAction)


def test_website_inlineaction_constructor_exists():
    assert callable(website_InlineAction.__init__)


def test_website_inlineaction_constructor_args():
    sig = inspect.signature(website_InlineAction.__init__)
    params = list(sig.parameters.keys())
    assert "header" in params, "Missing parameter 'header'"
    assert "headerClass" in params, "Missing parameter 'headerClass'"
    assert "footer" in params, "Missing parameter 'footer'"
    assert "footerClass" in params, "Missing parameter 'footerClass'"
    assert "disable" in params, "Missing parameter 'disable'"
    assert "requiresRole" in params, "Missing parameter 'requiresRole'"

def test_website_inlineaction_has_header():
    assert hasattr(website_InlineAction, "header")
    descriptor = None
    for klass in website_InlineAction.__mro__:
        if "header" in klass.__dict__:
            descriptor = klass.__dict__["header"]
            break
    assert isinstance(descriptor, property)

def test_website_inlineaction_has_headerClass():
    assert hasattr(website_InlineAction, "headerClass")
    descriptor = None
    for klass in website_InlineAction.__mro__:
        if "headerClass" in klass.__dict__:
            descriptor = klass.__dict__["headerClass"]
            break
    assert isinstance(descriptor, property)

def test_website_inlineaction_has_footer():
    assert hasattr(website_InlineAction, "footer")
    descriptor = None
    for klass in website_InlineAction.__mro__:
        if "footer" in klass.__dict__:
            descriptor = klass.__dict__["footer"]
            break
    assert isinstance(descriptor, property)

def test_website_inlineaction_has_footerClass():
    assert hasattr(website_InlineAction, "footerClass")
    descriptor = None
    for klass in website_InlineAction.__mro__:
        if "footerClass" in klass.__dict__:
            descriptor = klass.__dict__["footerClass"]
            break
    assert isinstance(descriptor, property)

def test_website_inlineaction_has_disable():
    assert hasattr(website_InlineAction, "disable")
    descriptor = None
    for klass in website_InlineAction.__mro__:
        if "disable" in klass.__dict__:
            descriptor = klass.__dict__["disable"]
            break
    assert isinstance(descriptor, property)

def test_website_inlineaction_has_requiresRole():
    assert hasattr(website_InlineAction, "requiresRole")
    descriptor = None
    for klass in website_InlineAction.__mro__:
        if "requiresRole" in klass.__dict__:
            descriptor = klass.__dict__["requiresRole"]
            break
    assert isinstance(descriptor, property)



def test_website_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(website_EnumerationLiteral)


def test_website_enumerationliteral_constructor_exists():
    assert callable(website_EnumerationLiteral.__init__)


def test_website_enumerationliteral_constructor_args():
    sig = inspect.signature(website_EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_website_filter_is_not_abstract():
    assert not inspect.isabstract(website_Filter)


def test_website_filter_constructor_exists():
    assert callable(website_Filter.__init__)


def test_website_filter_constructor_args():
    sig = inspect.signature(website_Filter.__init__)
    params = list(sig.parameters.keys())



def test_website_actionmenuentry_is_not_abstract():
    assert not inspect.isabstract(website_ActionMenuEntry)


def test_website_actionmenuentry_constructor_exists():
    assert callable(website_ActionMenuEntry.__init__)


def test_website_actionmenuentry_constructor_args():
    sig = inspect.signature(website_ActionMenuEntry.__init__)
    params = list(sig.parameters.keys())



def test_website_viewassociation_is_not_abstract():
    assert not inspect.isabstract(website_ViewAssociation)


def test_website_viewassociation_constructor_exists():
    assert callable(website_ViewAssociation.__init__)


def test_website_viewassociation_constructor_args():
    sig = inspect.signature(website_ViewAssociation.__init__)
    params = list(sig.parameters.keys())
    assert "cardinality" in params, "Missing parameter 'cardinality'"

def test_website_viewassociation_has_cardinality():
    assert hasattr(website_ViewAssociation, "cardinality")
    descriptor = None
    for klass in website_ViewAssociation.__mro__:
        if "cardinality" in klass.__dict__:
            descriptor = klass.__dict__["cardinality"]
            break
    assert isinstance(descriptor, property)



def test_website_unitsupportaction_is_not_abstract():
    assert not inspect.isabstract(website_UnitSupportAction)


def test_website_unitsupportaction_constructor_exists():
    assert callable(website_UnitSupportAction.__init__)


def test_website_unitsupportaction_constructor_args():
    sig = inspect.signature(website_UnitSupportAction.__init__)
    params = list(sig.parameters.keys())
    assert "confirmMessage" in params, "Missing parameter 'confirmMessage'"
    assert "disable" in params, "Missing parameter 'disable'"

def test_website_unitsupportaction_has_confirmMessage():
    assert hasattr(website_UnitSupportAction, "confirmMessage")
    descriptor = None
    for klass in website_UnitSupportAction.__mro__:
        if "confirmMessage" in klass.__dict__:
            descriptor = klass.__dict__["confirmMessage"]
            break
    assert isinstance(descriptor, property)

def test_website_unitsupportaction_has_disable():
    assert hasattr(website_UnitSupportAction, "disable")
    descriptor = None
    for klass in website_UnitSupportAction.__mro__:
        if "disable" in klass.__dict__:
            descriptor = klass.__dict__["disable"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_website_filterparameter_is_not_abstract():
    assert not inspect.isabstract(website_FilterParameter)


def test_website_filterparameter_constructor_exists():
    assert callable(website_FilterParameter.__init__)


def test_website_filterparameter_constructor_args():
    sig = inspect.signature(website_FilterParameter.__init__)
    params = list(sig.parameters.keys())
    assert "placeholder" in params, "Missing parameter 'placeholder'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"

def test_website_filterparameter_has_placeholder():
    assert hasattr(website_FilterParameter, "placeholder")
    descriptor = None
    for klass in website_FilterParameter.__mro__:
        if "placeholder" in klass.__dict__:
            descriptor = klass.__dict__["placeholder"]
            break
    assert isinstance(descriptor, property)

def test_website_filterparameter_has_defaultValue():
    assert hasattr(website_FilterParameter, "defaultValue")
    descriptor = None
    for klass in website_FilterParameter.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)



def test_website_selection_is_not_abstract():
    assert not inspect.isabstract(website_Selection)


def test_website_selection_constructor_exists():
    assert callable(website_Selection.__init__)


def test_website_selection_constructor_args():
    sig = inspect.signature(website_Selection.__init__)
    params = list(sig.parameters.keys())
    assert "limit" in params, "Missing parameter 'limit'"
    assert "distinct" in params, "Missing parameter 'distinct'"
    assert "selected" in params, "Missing parameter 'selected'"

def test_website_selection_has_limit():
    assert hasattr(website_Selection, "limit")
    descriptor = None
    for klass in website_Selection.__mro__:
        if "limit" in klass.__dict__:
            descriptor = klass.__dict__["limit"]
            break
    assert isinstance(descriptor, property)

def test_website_selection_has_distinct():
    assert hasattr(website_Selection, "distinct")
    descriptor = None
    for klass in website_Selection.__mro__:
        if "distinct" in klass.__dict__:
            descriptor = klass.__dict__["distinct"]
            break
    assert isinstance(descriptor, property)

def test_website_selection_has_selected():
    assert hasattr(website_Selection, "selected")
    descriptor = None
    for klass in website_Selection.__mro__:
        if "selected" in klass.__dict__:
            descriptor = klass.__dict__["selected"]
            break
    assert isinstance(descriptor, property)



def test_website_businessoperation_is_not_abstract():
    assert not inspect.isabstract(website_BusinessOperation)


def test_website_businessoperation_constructor_exists():
    assert callable(website_BusinessOperation.__init__)


def test_website_businessoperation_constructor_args():
    sig = inspect.signature(website_BusinessOperation.__init__)
    params = list(sig.parameters.keys())
    assert "resultType" in params, "Missing parameter 'resultType'"
    assert "resultMimeType" in params, "Missing parameter 'resultMimeType'"

def test_website_businessoperation_has_resultType():
    assert hasattr(website_BusinessOperation, "resultType")
    descriptor = None
    for klass in website_BusinessOperation.__mro__:
        if "resultType" in klass.__dict__:
            descriptor = klass.__dict__["resultType"]
            break
    assert isinstance(descriptor, property)

def test_website_businessoperation_has_resultMimeType():
    assert hasattr(website_BusinessOperation, "resultMimeType")
    descriptor = None
    for klass in website_BusinessOperation.__mro__:
        if "resultMimeType" in klass.__dict__:
            descriptor = klass.__dict__["resultMimeType"]
            break
    assert isinstance(descriptor, property)



def test_website_selectionparameter_is_not_abstract():
    assert not inspect.isabstract(website_SelectionParameter)


def test_website_selectionparameter_constructor_exists():
    assert callable(website_SelectionParameter.__init__)


def test_website_selectionparameter_constructor_args():
    sig = inspect.signature(website_SelectionParameter.__init__)
    params = list(sig.parameters.keys())
    assert "optional" in params, "Missing parameter 'optional'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"

def test_website_selectionparameter_has_optional():
    assert hasattr(website_SelectionParameter, "optional")
    descriptor = None
    for klass in website_SelectionParameter.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)

def test_website_selectionparameter_has_defaultValue():
    assert hasattr(website_SelectionParameter, "defaultValue")
    descriptor = None
    for klass in website_SelectionParameter.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)



def test_website_modellabel_is_not_abstract():
    assert not inspect.isabstract(website_ModelLabel)


def test_website_modellabel_constructor_exists():
    assert callable(website_ModelLabel.__init__)


def test_website_modellabel_constructor_args():
    sig = inspect.signature(website_ModelLabel.__init__)
    params = list(sig.parameters.keys())
    assert "format" in params, "Missing parameter 'format'"

def test_website_modellabel_has_format():
    assert hasattr(website_ModelLabel, "format")
    descriptor = None
    for klass in website_ModelLabel.__mro__:
        if "format" in klass.__dict__:
            descriptor = klass.__dict__["format"]
            break
    assert isinstance(descriptor, property)



def test_website_nameddisplayelement_is_not_abstract():
    assert not inspect.isabstract(website_NamedDisplayElement)


def test_website_nameddisplayelement_constructor_exists():
    assert callable(website_NamedDisplayElement.__init__)


def test_website_nameddisplayelement_constructor_args():
    sig = inspect.signature(website_NamedDisplayElement.__init__)
    params = list(sig.parameters.keys())
    assert "displayLabel" in params, "Missing parameter 'displayLabel'"

def test_website_nameddisplayelement_has_displayLabel():
    assert hasattr(website_NamedDisplayElement, "displayLabel")
    descriptor = None
    for klass in website_NamedDisplayElement.__mro__:
        if "displayLabel" in klass.__dict__:
            descriptor = klass.__dict__["displayLabel"]
            break
    assert isinstance(descriptor, property)



def test_website_authentication_is_not_abstract():
    assert not inspect.isabstract(website_Authentication)


def test_website_authentication_constructor_exists():
    assert callable(website_Authentication.__init__)


def test_website_authentication_constructor_args():
    sig = inspect.signature(website_Authentication.__init__)
    params = list(sig.parameters.keys())
    assert "loginLabel" in params, "Missing parameter 'loginLabel'"
    assert "logoutLabel" in params, "Missing parameter 'logoutLabel'"

def test_website_authentication_has_loginLabel():
    assert hasattr(website_Authentication, "loginLabel")
    descriptor = None
    for klass in website_Authentication.__mro__:
        if "loginLabel" in klass.__dict__:
            descriptor = klass.__dict__["loginLabel"]
            break
    assert isinstance(descriptor, property)

def test_website_authentication_has_logoutLabel():
    assert hasattr(website_Authentication, "logoutLabel")
    descriptor = None
    for klass in website_Authentication.__mro__:
        if "logoutLabel" in klass.__dict__:
            descriptor = klass.__dict__["logoutLabel"]
            break
    assert isinstance(descriptor, property)



def test_website_imagemanipulation_is_not_abstract():
    assert not inspect.isabstract(website_ImageManipulation)


def test_website_imagemanipulation_constructor_exists():
    assert callable(website_ImageManipulation.__init__)


def test_website_imagemanipulation_constructor_args():
    sig = inspect.signature(website_ImageManipulation.__init__)
    params = list(sig.parameters.keys())
    assert "jpegQuality" in params, "Missing parameter 'jpegQuality'"

def test_website_imagemanipulation_has_jpegQuality():
    assert hasattr(website_ImageManipulation, "jpegQuality")
    descriptor = None
    for klass in website_ImageManipulation.__mro__:
        if "jpegQuality" in klass.__dict__:
            descriptor = klass.__dict__["jpegQuality"]
            break
    assert isinstance(descriptor, property)



def test_website_entityorview_is_not_abstract():
    assert not inspect.isabstract(website_EntityOrView)


def test_website_entityorview_constructor_exists():
    assert callable(website_EntityOrView.__init__)


def test_website_entityorview_constructor_args():
    sig = inspect.signature(website_EntityOrView.__init__)
    params = list(sig.parameters.keys())
    assert "tableName" in params, "Missing parameter 'tableName'"
    assert "serializationExcludeAll" in params, "Missing parameter 'serializationExcludeAll'"
    assert "pluralisedName" in params, "Missing parameter 'pluralisedName'"
    assert "implementsUserInterface" in params, "Missing parameter 'implementsUserInterface'"
    assert "autoKeyName" in params, "Missing parameter 'autoKeyName'"
    assert "autoKeyPersistentType" in params, "Missing parameter 'autoKeyPersistentType'"
    assert "autoKeyGenerationStrategy" in params, "Missing parameter 'autoKeyGenerationStrategy'"
    assert "singletonName" in params, "Missing parameter 'singletonName'"

def test_website_entityorview_has_tableName():
    assert hasattr(website_EntityOrView, "tableName")
    descriptor = None
    for klass in website_EntityOrView.__mro__:
        if "tableName" in klass.__dict__:
            descriptor = klass.__dict__["tableName"]
            break
    assert isinstance(descriptor, property)

def test_website_entityorview_has_serializationExcludeAll():
    assert hasattr(website_EntityOrView, "serializationExcludeAll")
    descriptor = None
    for klass in website_EntityOrView.__mro__:
        if "serializationExcludeAll" in klass.__dict__:
            descriptor = klass.__dict__["serializationExcludeAll"]
            break
    assert isinstance(descriptor, property)

def test_website_entityorview_has_pluralisedName():
    assert hasattr(website_EntityOrView, "pluralisedName")
    descriptor = None
    for klass in website_EntityOrView.__mro__:
        if "pluralisedName" in klass.__dict__:
            descriptor = klass.__dict__["pluralisedName"]
            break
    assert isinstance(descriptor, property)

def test_website_entityorview_has_implementsUserInterface():
    assert hasattr(website_EntityOrView, "implementsUserInterface")
    descriptor = None
    for klass in website_EntityOrView.__mro__:
        if "implementsUserInterface" in klass.__dict__:
            descriptor = klass.__dict__["implementsUserInterface"]
            break
    assert isinstance(descriptor, property)

def test_website_entityorview_has_autoKeyName():
    assert hasattr(website_EntityOrView, "autoKeyName")
    descriptor = None
    for klass in website_EntityOrView.__mro__:
        if "autoKeyName" in klass.__dict__:
            descriptor = klass.__dict__["autoKeyName"]
            break
    assert isinstance(descriptor, property)

def test_website_entityorview_has_autoKeyPersistentType():
    assert hasattr(website_EntityOrView, "autoKeyPersistentType")
    descriptor = None
    for klass in website_EntityOrView.__mro__:
        if "autoKeyPersistentType" in klass.__dict__:
            descriptor = klass.__dict__["autoKeyPersistentType"]
            break
    assert isinstance(descriptor, property)

def test_website_entityorview_has_autoKeyGenerationStrategy():
    assert hasattr(website_EntityOrView, "autoKeyGenerationStrategy")
    descriptor = None
    for klass in website_EntityOrView.__mro__:
        if "autoKeyGenerationStrategy" in klass.__dict__:
            descriptor = klass.__dict__["autoKeyGenerationStrategy"]
            break
    assert isinstance(descriptor, property)

def test_website_entityorview_has_singletonName():
    assert hasattr(website_EntityOrView, "singletonName")
    descriptor = None
    for klass in website_EntityOrView.__mro__:
        if "singletonName" in klass.__dict__:
            descriptor = klass.__dict__["singletonName"]
            break
    assert isinstance(descriptor, property)



def test_website_menu_is_not_abstract():
    assert not inspect.isabstract(website_Menu)


def test_website_menu_constructor_exists():
    assert callable(website_Menu.__init__)


def test_website_menu_constructor_args():
    sig = inspect.signature(website_Menu.__init__)
    params = list(sig.parameters.keys())
    assert "captionClass" in params, "Missing parameter 'captionClass'"
    assert "styleClass" in params, "Missing parameter 'styleClass'"
    assert "layoutClass" in params, "Missing parameter 'layoutClass'"
    assert "omitCaption" in params, "Missing parameter 'omitCaption'"

def test_website_menu_has_captionClass():
    assert hasattr(website_Menu, "captionClass")
    descriptor = None
    for klass in website_Menu.__mro__:
        if "captionClass" in klass.__dict__:
            descriptor = klass.__dict__["captionClass"]
            break
    assert isinstance(descriptor, property)

def test_website_menu_has_styleClass():
    assert hasattr(website_Menu, "styleClass")
    descriptor = None
    for klass in website_Menu.__mro__:
        if "styleClass" in klass.__dict__:
            descriptor = klass.__dict__["styleClass"]
            break
    assert isinstance(descriptor, property)

def test_website_menu_has_layoutClass():
    assert hasattr(website_Menu, "layoutClass")
    descriptor = None
    for klass in website_Menu.__mro__:
        if "layoutClass" in klass.__dict__:
            descriptor = klass.__dict__["layoutClass"]
            break
    assert isinstance(descriptor, property)

def test_website_menu_has_omitCaption():
    assert hasattr(website_Menu, "omitCaption")
    descriptor = None
    for klass in website_Menu.__mro__:
        if "omitCaption" in klass.__dict__:
            descriptor = klass.__dict__["omitCaption"]
            break
    assert isinstance(descriptor, property)



def test_website_page_is_not_abstract():
    assert not inspect.isabstract(website_Page)


def test_website_page_constructor_exists():
    assert callable(website_Page.__init__)


def test_website_page_constructor_args():
    sig = inspect.signature(website_Page.__init__)
    params = list(sig.parameters.keys())
    assert "authenticated" in params, "Missing parameter 'authenticated'"
    assert "topMenuOption" in params, "Missing parameter 'topMenuOption'"
    assert "styleClass" in params, "Missing parameter 'styleClass'"
    assert "uriElement" in params, "Missing parameter 'uriElement'"
    assert "navigationLabel" in params, "Missing parameter 'navigationLabel'"
    assert "topMenuRank" in params, "Missing parameter 'topMenuRank'"

def test_website_page_has_authenticated():
    assert hasattr(website_Page, "authenticated")
    descriptor = None
    for klass in website_Page.__mro__:
        if "authenticated" in klass.__dict__:
            descriptor = klass.__dict__["authenticated"]
            break
    assert isinstance(descriptor, property)

def test_website_page_has_topMenuOption():
    assert hasattr(website_Page, "topMenuOption")
    descriptor = None
    for klass in website_Page.__mro__:
        if "topMenuOption" in klass.__dict__:
            descriptor = klass.__dict__["topMenuOption"]
            break
    assert isinstance(descriptor, property)

def test_website_page_has_styleClass():
    assert hasattr(website_Page, "styleClass")
    descriptor = None
    for klass in website_Page.__mro__:
        if "styleClass" in klass.__dict__:
            descriptor = klass.__dict__["styleClass"]
            break
    assert isinstance(descriptor, property)

def test_website_page_has_uriElement():
    assert hasattr(website_Page, "uriElement")
    descriptor = None
    for klass in website_Page.__mro__:
        if "uriElement" in klass.__dict__:
            descriptor = klass.__dict__["uriElement"]
            break
    assert isinstance(descriptor, property)

def test_website_page_has_navigationLabel():
    assert hasattr(website_Page, "navigationLabel")
    descriptor = None
    for klass in website_Page.__mro__:
        if "navigationLabel" in klass.__dict__:
            descriptor = klass.__dict__["navigationLabel"]
            break
    assert isinstance(descriptor, property)

def test_website_page_has_topMenuRank():
    assert hasattr(website_Page, "topMenuRank")
    descriptor = None
    for klass in website_Page.__mro__:
        if "topMenuRank" in klass.__dict__:
            descriptor = klass.__dict__["topMenuRank"]
            break
    assert isinstance(descriptor, property)



def test_website_service_is_not_abstract():
    assert not inspect.isabstract(website_Service)


def test_website_service_constructor_exists():
    assert callable(website_Service.__init__)


def test_website_service_constructor_args():
    sig = inspect.signature(website_Service.__init__)
    params = list(sig.parameters.keys())



def test_website_classifier_is_not_abstract():
    assert not inspect.isabstract(website_Classifier)


def test_website_classifier_constructor_exists():
    assert callable(website_Classifier.__init__)


def test_website_classifier_constructor_args():
    sig = inspect.signature(website_Classifier.__init__)
    params = list(sig.parameters.keys())



def test_website_websiteproperties_is_not_abstract():
    assert not inspect.isabstract(website_WebsiteProperties)


def test_website_websiteproperties_constructor_exists():
    assert callable(website_WebsiteProperties.__init__)


def test_website_websiteproperties_constructor_args():
    sig = inspect.signature(website_WebsiteProperties.__init__)
    params = list(sig.parameters.keys())
    assert "staticUnitsEditable" in params, "Missing parameter 'staticUnitsEditable'"
    assert "databasePrefix" in params, "Missing parameter 'databasePrefix'"
    assert "inputTechnology" in params, "Missing parameter 'inputTechnology'"
    assert "rewriteURLs" in params, "Missing parameter 'rewriteURLs'"
    assert "frameworkTechnology" in params, "Missing parameter 'frameworkTechnology'"
    assert "databaseTechnology" in params, "Missing parameter 'databaseTechnology'"
    assert "ormTechnology" in params, "Missing parameter 'ormTechnology'"
    assert "topNavigationId" in params, "Missing parameter 'topNavigationId'"
    assert "siteTemplate" in params, "Missing parameter 'siteTemplate'"
    assert "projectName" in params, "Missing parameter 'projectName'"
    assert "metaDescription" in params, "Missing parameter 'metaDescription'"
    assert "defaultTimeFormat" in params, "Missing parameter 'defaultTimeFormat'"
    assert "captchaSecretKey" in params, "Missing parameter 'captchaSecretKey'"
    assert "databaseHost" in params, "Missing parameter 'databaseHost'"
    assert "databaseName" in params, "Missing parameter 'databaseName'"
    assert "timestampCreation" in params, "Missing parameter 'timestampCreation'"
    assert "responsiveTopMenu" in params, "Missing parameter 'responsiveTopMenu'"
    assert "textEditorURL" in params, "Missing parameter 'textEditorURL'"
    assert "captchaSiteKey" in params, "Missing parameter 'captchaSiteKey'"
    assert "defaultMaximumUploadSize" in params, "Missing parameter 'defaultMaximumUploadSize'"
    assert "webmasterEmail" in params, "Missing parameter 'webmasterEmail'"
    assert "defaultDateTimeFormat" in params, "Missing parameter 'defaultDateTimeFormat'"
    assert "databasePassword" in params, "Missing parameter 'databasePassword'"
    assert "databaseUsername" in params, "Missing parameter 'databaseUsername'"
    assert "ajaxTechnology" in params, "Missing parameter 'ajaxTechnology'"
    assert "defaultDateFormat" in params, "Missing parameter 'defaultDateFormat'"
    assert "developmentVersion" in params, "Missing parameter 'developmentVersion'"
    assert "copyrightText" in params, "Missing parameter 'copyrightText'"
    assert "baseURL" in params, "Missing parameter 'baseURL'"
    assert "testProjectName" in params, "Missing parameter 'testProjectName'"
    assert "databasePort" in params, "Missing parameter 'databasePort'"
    assert "timestampUpdates" in params, "Missing parameter 'timestampUpdates'"
    assert "siteTitle" in params, "Missing parameter 'siteTitle'"

def test_website_websiteproperties_has_staticUnitsEditable():
    assert hasattr(website_WebsiteProperties, "staticUnitsEditable")
    descriptor = None
    for klass in website_WebsiteProperties.__mro__:
        if "staticUnitsEditable" in klass.__dict__:
            descriptor = klass.__dict__["staticUnitsEditable"]
            break
    assert isinstance(descriptor, property)

def test_website_websiteproperties_has_databasePrefix():
    assert hasattr(website_WebsiteProperties, "databasePrefix")
    descriptor = None
    for klass in website_WebsiteProperties.__mro__:
        if "databasePrefix" in klass.__dict__:
            descriptor = klass.__dict__["databasePrefix"]
            break
    assert isinstance(descriptor, property)

def test_website_websiteproperties_has_inputTechnology():
    assert hasattr(website_WebsiteProperties, "inputTechnology")
    descriptor = None
    for klass in website_WebsiteProperties.__mro__:
        if "inputTechnology" in klass.__dict__:
            descriptor = klass.__dict__["inputTechnology"]
            break
    assert isinstance(descriptor, property)

def test_website_websiteproperties_has_rewriteURLs():
    assert hasattr(website_WebsiteProperties, "rewriteURLs")
    descriptor = None
    for klass in website_WebsiteProperties.__mro__:
        if "rewriteURLs" in klass.__dict__:
            descriptor = klass.__dict__["rewriteURLs"]
            break
    assert isinstance(descriptor, property)

def test_website_websiteproperties_has_frameworkTechnology():
    assert hasattr(website_WebsiteProperties, "frameworkTechnology")
    descriptor = None
    for klass in website_WebsiteProperties.__mro__:
        if "frameworkTechnology" in klass.__dict__:
            descriptor = klass.__dict__["frameworkTechnology"]
            break
    assert isinstance(descriptor, property)

def test_website_websiteproperties_has_databaseTechnology():
    assert hasattr(website_WebsiteProperties, "databaseTechnology")
    descriptor = None
    for klass in website_WebsiteProperties.__mro__:
        if "databaseTechnology" in klass.__dict__:
            descriptor = klass.__dict__["databaseTechnology"]
            break
    assert isinstance(descriptor, property)

def test_website_websiteproperties_has_ormTechnology():
    assert hasattr(website_WebsiteProperties, "ormTechnology")
    descriptor = None
    for klass in website_WebsiteProperties.__mro__:
        if "ormTechnology" in klass.__dict__:
            descriptor = klass.__dict__["ormTechnology"]
            break
    assert isinstance(descriptor, property)

def test_website_websiteproperties_has_topNavigationId():
    assert hasattr(website_WebsiteProperties, "topNavigationId")
    descriptor = None
    for klass in website_WebsiteProperties.__mro__:
        if "topNavigationId" in klass.__dict__:
            descriptor = klass.__dict__["topNavigationId"]
            break
    assert isinstance(descriptor, property)

def test_website_websiteproperties_has_siteTemplate():
    assert hasattr(website_WebsiteProperties, "siteTemplate")
    descriptor = None
    for klass in website_WebsiteProperties.__mro__:
        if "siteTemplate" in klass.__dict__:
            descriptor = klass.__dict__["siteTemplate"]
            break
    assert isinstance(descriptor, property)

def test_website_websiteproperties_has_projectName():
    assert hasattr(website_WebsiteProperties, "projectName")
    descriptor = None
    for klass in website_WebsiteProperties.__mro__:
        if "projectName" in klass.__dict__:
            descriptor = klass.__dict__["projectName"]
            break
    assert isinstance(descriptor, property)

def test_website_websiteproperties_has_metaDescription():
    assert hasattr(website_WebsiteProperties, "metaDescription")
    descriptor = None
    for klass in website_WebsiteProperties.__mro__:
        if "metaDescription" in klass.__dict__:
            descriptor = klass.__dict__["metaDescription"]
            break
    assert isinstance(descriptor, property)

def test_website_websiteproperties_has_defaultTimeFormat():
    assert hasattr(website_WebsiteProperties, "defaultTimeFormat")
    descriptor = None
    for klass in website_WebsiteProperties.__mro__:
        if "defaultTimeFormat" in klass.__dict__:
            descriptor = klass.__dict__["defaultTimeFormat"]
            break
    assert isinstance(descriptor, property)

def test_website_websiteproperties_has_captchaSecretKey():
    assert hasattr(website_WebsiteProperties, "captchaSecretKey")
    descriptor = None
    for klass in website_WebsiteProperties.__mro__:
        if "captchaSecretKey" in klass.__dict__:
            descriptor = klass.__dict__["captchaSecretKey"]
            break
    assert isinstance(descriptor, property)

def test_website_websiteproperties_has_databaseHost():
    assert hasattr(website_WebsiteProperties, "databaseHost")
    descriptor = None
    for klass in website_WebsiteProperties.__mro__:
        if "databaseHost" in klass.__dict__:
            descriptor = klass.__dict__["databaseHost"]
            break
    assert isinstance(descriptor, property)

def test_website_websiteproperties_has_databaseName():
    assert hasattr(website_WebsiteProperties, "databaseName")
    descriptor = None
    for klass in website_WebsiteProperties.__mro__:
        if "databaseName" in klass.__dict__:
            descriptor = klass.__dict__["databaseName"]
            break
    assert isinstance(descriptor, property)

def test_website_websiteproperties_has_timestampCreation():
    assert hasattr(website_WebsiteProperties, "timestampCreation")
    descriptor = None
    for klass in website_WebsiteProperties.__mro__:
        if "timestampCreation" in klass.__dict__:
            descriptor = klass.__dict__["timestampCreation"]
            break
    assert isinstance(descriptor, property)

def test_website_websiteproperties_has_responsiveTopMenu():
    assert hasattr(website_WebsiteProperties, "responsiveTopMenu")
    descriptor = None
    for klass in website_WebsiteProperties.__mro__:
        if "responsiveTopMenu" in klass.__dict__:
            descriptor = klass.__dict__["responsiveTopMenu"]
            break
    assert isinstance(descriptor, property)

def test_website_websiteproperties_has_textEditorURL():
    assert hasattr(website_WebsiteProperties, "textEditorURL")
    descriptor = None
    for klass in website_WebsiteProperties.__mro__:
        if "textEditorURL" in klass.__dict__:
            descriptor = klass.__dict__["textEditorURL"]
            break
    assert isinstance(descriptor, property)

def test_website_websiteproperties_has_captchaSiteKey():
    assert hasattr(website_WebsiteProperties, "captchaSiteKey")
    descriptor = None
    for klass in website_WebsiteProperties.__mro__:
        if "captchaSiteKey" in klass.__dict__:
            descriptor = klass.__dict__["captchaSiteKey"]
            break
    assert isinstance(descriptor, property)

def test_website_websiteproperties_has_defaultMaximumUploadSize():
    assert hasattr(website_WebsiteProperties, "defaultMaximumUploadSize")
    descriptor = None
    for klass in website_WebsiteProperties.__mro__:
        if "defaultMaximumUploadSize" in klass.__dict__:
            descriptor = klass.__dict__["defaultMaximumUploadSize"]
            break
    assert isinstance(descriptor, property)

def test_website_websiteproperties_has_webmasterEmail():
    assert hasattr(website_WebsiteProperties, "webmasterEmail")
    descriptor = None
    for klass in website_WebsiteProperties.__mro__:
        if "webmasterEmail" in klass.__dict__:
            descriptor = klass.__dict__["webmasterEmail"]
            break
    assert isinstance(descriptor, property)

def test_website_websiteproperties_has_defaultDateTimeFormat():
    assert hasattr(website_WebsiteProperties, "defaultDateTimeFormat")
    descriptor = None
    for klass in website_WebsiteProperties.__mro__:
        if "defaultDateTimeFormat" in klass.__dict__:
            descriptor = klass.__dict__["defaultDateTimeFormat"]
            break
    assert isinstance(descriptor, property)

def test_website_websiteproperties_has_databasePassword():
    assert hasattr(website_WebsiteProperties, "databasePassword")
    descriptor = None
    for klass in website_WebsiteProperties.__mro__:
        if "databasePassword" in klass.__dict__:
            descriptor = klass.__dict__["databasePassword"]
            break
    assert isinstance(descriptor, property)

def test_website_websiteproperties_has_databaseUsername():
    assert hasattr(website_WebsiteProperties, "databaseUsername")
    descriptor = None
    for klass in website_WebsiteProperties.__mro__:
        if "databaseUsername" in klass.__dict__:
            descriptor = klass.__dict__["databaseUsername"]
            break
    assert isinstance(descriptor, property)

def test_website_websiteproperties_has_ajaxTechnology():
    assert hasattr(website_WebsiteProperties, "ajaxTechnology")
    descriptor = None
    for klass in website_WebsiteProperties.__mro__:
        if "ajaxTechnology" in klass.__dict__:
            descriptor = klass.__dict__["ajaxTechnology"]
            break
    assert isinstance(descriptor, property)

def test_website_websiteproperties_has_defaultDateFormat():
    assert hasattr(website_WebsiteProperties, "defaultDateFormat")
    descriptor = None
    for klass in website_WebsiteProperties.__mro__:
        if "defaultDateFormat" in klass.__dict__:
            descriptor = klass.__dict__["defaultDateFormat"]
            break
    assert isinstance(descriptor, property)

def test_website_websiteproperties_has_developmentVersion():
    assert hasattr(website_WebsiteProperties, "developmentVersion")
    descriptor = None
    for klass in website_WebsiteProperties.__mro__:
        if "developmentVersion" in klass.__dict__:
            descriptor = klass.__dict__["developmentVersion"]
            break
    assert isinstance(descriptor, property)

def test_website_websiteproperties_has_copyrightText():
    assert hasattr(website_WebsiteProperties, "copyrightText")
    descriptor = None
    for klass in website_WebsiteProperties.__mro__:
        if "copyrightText" in klass.__dict__:
            descriptor = klass.__dict__["copyrightText"]
            break
    assert isinstance(descriptor, property)

def test_website_websiteproperties_has_baseURL():
    assert hasattr(website_WebsiteProperties, "baseURL")
    descriptor = None
    for klass in website_WebsiteProperties.__mro__:
        if "baseURL" in klass.__dict__:
            descriptor = klass.__dict__["baseURL"]
            break
    assert isinstance(descriptor, property)

def test_website_websiteproperties_has_testProjectName():
    assert hasattr(website_WebsiteProperties, "testProjectName")
    descriptor = None
    for klass in website_WebsiteProperties.__mro__:
        if "testProjectName" in klass.__dict__:
            descriptor = klass.__dict__["testProjectName"]
            break
    assert isinstance(descriptor, property)

def test_website_websiteproperties_has_databasePort():
    assert hasattr(website_WebsiteProperties, "databasePort")
    descriptor = None
    for klass in website_WebsiteProperties.__mro__:
        if "databasePort" in klass.__dict__:
            descriptor = klass.__dict__["databasePort"]
            break
    assert isinstance(descriptor, property)

def test_website_websiteproperties_has_timestampUpdates():
    assert hasattr(website_WebsiteProperties, "timestampUpdates")
    descriptor = None
    for klass in website_WebsiteProperties.__mro__:
        if "timestampUpdates" in klass.__dict__:
            descriptor = klass.__dict__["timestampUpdates"]
            break
    assert isinstance(descriptor, property)

def test_website_websiteproperties_has_siteTitle():
    assert hasattr(website_WebsiteProperties, "siteTitle")
    descriptor = None
    for klass in website_WebsiteProperties.__mro__:
        if "siteTitle" in klass.__dict__:
            descriptor = klass.__dict__["siteTitle"]
            break
    assert isinstance(descriptor, property)



def test_website_webgenmodel_is_not_abstract():
    assert not inspect.isabstract(website_WebGenModel)


def test_website_webgenmodel_constructor_exists():
    assert callable(website_WebGenModel.__init__)


def test_website_webgenmodel_constructor_args():
    sig = inspect.signature(website_WebGenModel.__init__)
    params = list(sig.parameters.keys())

def test_pagetopmenuoptions_exists():
    # Check that the Enumeration exists
    assert PageTopMenuOptions is not None

def test_pagetopmenuoptions_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PageTopMenuOptions]
    expected_literals = [
        "IncludeWhenAuthenticated",
        "AlwaysInclude",
        "NeverInclude",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PageTopMenuOptions"

def test_collectiondisplayoptions_exists():
    # Check that the Enumeration exists
    assert CollectionDisplayOptions is not None

def test_collectiondisplayoptions_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CollectionDisplayOptions]
    expected_literals = [
        "LineDirection",
        "PageDirection",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CollectionDisplayOptions"

def test_operationresulttypes_exists():
    # Check that the Enumeration exists
    assert OperationResultTypes is not None

def test_operationresulttypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OperationResultTypes]
    expected_literals = [
        "None_",
        "File",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OperationResultTypes"

def test_ormtechnologies_exists():
    # Check that the Enumeration exists
    assert OrmTechnologies is not None

def test_ormtechnologies_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OrmTechnologies]
    expected_literals = [
        "Kohana",
        "DataMapper",
        "DoctrineORM",
        "Idiorm",
        "JPA",
        "DoctrineODM",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OrmTechnologies"

def test_databasetechnologies_exists():
    # Check that the Enumeration exists
    assert DatabaseTechnologies is not None

def test_databasetechnologies_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DatabaseTechnologies]
    expected_literals = [
        "MySql",
        "Oracle",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DatabaseTechnologies"

def test_datedetails_exists():
    # Check that the Enumeration exists
    assert DateDetails is not None

def test_datedetails_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DateDetails]
    expected_literals = [
        "DateAndTime",
        "TimeOnly",
        "DateOnly",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DateDetails"

def test_ajaxtechnologies_exists():
    # Check that the Enumeration exists
    assert AjaxTechnologies is not None

def test_ajaxtechnologies_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AjaxTechnologies]
    expected_literals = [
        "None_",
        "AngularJS",
        "jQuery",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AjaxTechnologies"

def test_inputtechnologies_exists():
    # Check that the Enumeration exists
    assert InputTechnologies is not None

def test_inputtechnologies_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InputTechnologies]
    expected_literals = [
        "Html",
        "jQueryUI",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InputTechnologies"

def test_authenticationkeytypes_exists():
    # Check that the Enumeration exists
    assert AuthenticationKeyTypes is not None

def test_authenticationkeytypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AuthenticationKeyTypes]
    expected_literals = [
        "Email",
        "Username",
        "ScreenName",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AuthenticationKeyTypes"

def test_indexdisplayoption_exists():
    # Check that the Enumeration exists
    assert IndexDisplayOption is not None

def test_indexdisplayoption_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IndexDisplayOption]
    expected_literals = [
        "PageDirection",
        "LineDirection",
        "Grid",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IndexDisplayOption"

def test_frameworktechnologies_exists():
    # Check that the Enumeration exists
    assert FrameworkTechnologies is not None

def test_frameworktechnologies_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FrameworkTechnologies]
    expected_literals = [
        "CakePHP",
        "JSF",
        "CodeIgniter",
        "Laravel",
        "Symfony",
        "Kohana",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FrameworkTechnologies"

def test_cardinality_exists():
    # Check that the Enumeration exists
    assert Cardinality is not None

def test_cardinality_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Cardinality]
    expected_literals = [
        "Required",
        "Optional",
        "Many",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Cardinality"

def test_ishaschoices_exists():
    # Check that the Enumeration exists
    assert isHasChoices is not None

def test_ishaschoices_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in isHasChoices]
    expected_literals = [
        "hasA",
        "isA",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in isHasChoices"


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
Path_strategy = st.builds(
    Path,
)
website_CurrentUserReference_strategy = st.builds(
    website_CurrentUserReference,
)
website_RouteParameterReference_strategy = st.builds(
    website_RouteParameterReference,
    name=
        safe_text
)
website_FeatureReference_strategy = st.builds(
    website_FeatureReference,
    name=
        safe_text
)
website_ModelReference_strategy = st.builds(
    website_ModelReference,
)
website_ParameterReference_strategy = st.builds(
    website_ParameterReference,
    name=
        safe_text
)
website_InlineActionContainer_strategy = st.builds(
    website_InlineActionContainer,
)
AuthenticationUnit_strategy = st.builds(
    AuthenticationUnit,
)
website_AuthenticationUnit_strategy = st.builds(
    website_AuthenticationUnit,
)
ImageUnit_strategy = st.builds(
    ImageUnit,
)
website_GalleryUnit_strategy = st.builds(
    website_GalleryUnit,
    contentClass=
        safe_text,
    styleClass=
        safe_text
)
website_SliderUnit_strategy = st.builds(
    website_SliderUnit,
    styleClass=
        safe_text,
    contentClass=
        safe_text
)
InlineAction_strategy = st.builds(
    InlineAction,
)
website_DeleteAction_strategy = st.builds(
    website_DeleteAction,
    confirmMessage=
        safe_text,
    uriElement=
        safe_text
)
website_FeatureSupportAction_strategy = st.builds(
    website_FeatureSupportAction,
    fileExtension=
        safe_text,
    uriElement=
        safe_text,
    confirmMessage=
        safe_text
)
website_SelectAction_strategy = st.builds(
    website_SelectAction,
)
ChildPath_strategy = st.builds(
    ChildPath,
)
website_ChildPathAttribute_strategy = st.builds(
    website_ChildPathAttribute,
    name=
        safe_text
)
FeaturePath_strategy = st.builds(
    FeaturePath,
)
website_FeaturePathAttribute_strategy = st.builds(
    website_FeaturePathAttribute,
    name=
        safe_text
)
website_FeaturePath_strategy = st.builds(
    website_FeaturePath,
)
CollectionUnit_strategy = st.builds(
    CollectionUnit,
)
DataUnit_strategy = st.builds(
    DataUnit,
)
ControlUnit_strategy = st.builds(
    ControlUnit,
)
website_SearchUnit_strategy = st.builds(
    website_SearchUnit,
    styleClass=
        safe_text
)
SingletonUnit_strategy = st.builds(
    SingletonUnit,
)
DynamicUnit_strategy = st.builds(
    DynamicUnit,
)
website_DataUnit_strategy = st.builds(
    website_DataUnit,
)
website_ImageUnit_strategy = st.builds(
    website_ImageUnit,
    showTime=
        st.integers(),
    transitionTime=
        st.integers(),
    missingImagePath=
        safe_text
)
website_ControlUnit_strategy = st.builds(
    website_ControlUnit,
    submitLabel=
        safe_text,
    cancelLabel=
        safe_text,
    contentClass=
        safe_text
)
website_EditUnit_strategy = st.builds(
    website_EditUnit,
    cancelLabel=
        safe_text,
    contentClass=
        safe_text,
    customiseValues=
        st.booleans(),
    confirmLabel=
        safe_text
)
EditUnit_strategy = st.builds(
    EditUnit,
)
website_CreateUnit_strategy = st.builds(
    website_CreateUnit,
    styleClass=
        safe_text
)
InterfaceField_strategy = st.builds(
    InterfaceField,
)
website_DateField_strategy = st.builds(
    website_DateField,
    format=
        safe_text,
    details=
        safe_text
)
website_DataTypeField_strategy = st.builds(
    website_DataTypeField,
    encrypt=
        st.booleans(),
    interfaceType=
        safe_text,
    obfuscateFormFields=
        st.booleans()
)
website_ChildPath_strategy = st.builds(
    website_ChildPath,
)
website_AssociationReference_strategy = st.builds(
    website_AssociationReference,
    name=
        safe_text
)
SelectableUnit_strategy = st.builds(
    SelectableUnit,
)
website_DetailsUnit_strategy = st.builds(
    website_DetailsUnit,
    contentClass=
        safe_text,
    omitFieldLabels=
        st.booleans(),
    styleClass=
        safe_text,
    onlyDisplayWhenNotEmpty=
        st.booleans()
)
website_UpdateUnit_strategy = st.builds(
    website_UpdateUnit,
    styleClass=
        safe_text
)
website_CreateUpdateUnit_strategy = st.builds(
    website_CreateUpdateUnit,
    styleClass=
        safe_text,
    clearLabel=
        safe_text,
    createUriElement=
        safe_text
)
website_MapUnit_strategy = st.builds(
    website_MapUnit,
    defaultZoomLevel=
        st.integers(),
    readOnly=
        st.booleans(),
    styleClass=
        safe_text
)
website_CollectionUnit_strategy = st.builds(
    website_CollectionUnit,
    useFirstLastPageLinks=
        st.booleans(),
    nextNpages=
        st.integers(),
    lastPageLabel=
        safe_text,
    useDisabledPageLinks=
        st.booleans(),
    nextPageLabel=
        safe_text,
    defaultPaginationSize=
        st.integers(),
    previousNpages=
        st.integers(),
    previousPageLabel=
        safe_text,
    firstPageLabel=
        safe_text,
    emptyMessage=
        safe_text
)
website_SingletonUnit_strategy = st.builds(
    website_SingletonUnit,
)
website_SelectableUnit_strategy = st.builds(
    website_SelectableUnit,
)
website_CaptchaField_strategy = st.builds(
    website_CaptchaField,
)
UnitFeature_strategy = st.builds(
    UnitFeature,
)
website_UnitElement_strategy = st.builds(
    website_UnitElement,
    validationPattern=
        safe_text,
    obfuscateFormFields=
        st.booleans(),
    name=
        safe_text,
    placeholder=
        safe_text
)
InlineActionContainer_strategy = st.builds(
    InlineActionContainer,
)
website_IndexUnit_strategy = st.builds(
    website_IndexUnit,
    omitColumnLabels=
        st.booleans(),
    styleClass=
        safe_text,
    displayOption=
        safe_text,
    contentClass=
        safe_text,
    rowClasses=
        safe_text
)
website_ImageIndexUnit_strategy = st.builds(
    website_ImageIndexUnit,
    contentClass=
        safe_text,
    styleClass=
        safe_text
)
UnitField_strategy = st.builds(
    UnitField,
)
website_UnitFeature_strategy = st.builds(
    website_UnitFeature,
    displayLabel=
        safe_text,
    displayClass=
        safe_text,
    headerClass=
        safe_text,
    onlyDisplayWhenNotEmpty=
        st.booleans(),
    footerClass=
        safe_text,
    required=
        st.booleans(),
    autofocus=
        st.booleans(),
    inputClass=
        safe_text,
    nullDisplayValue=
        safe_text,
    footer=
        safe_text
)
AssociationReference_strategy = st.builds(
    AssociationReference,
)
website_ChildPathAssociation_strategy = st.builds(
    website_ChildPathAssociation,
    isSourceAssociation=
        st.booleans()
)
website_FeaturePathAssociation_strategy = st.builds(
    website_FeaturePathAssociation,
    isSourceAssociation=
        st.booleans()
)
ContentUnit_strategy = st.builds(
    ContentUnit,
)
website_CreateSitemapUnit_strategy = st.builds(
    website_CreateSitemapUnit,
    contentClass=
        safe_text,
    styleClass=
        safe_text,
    deployedURL=
        safe_text,
    filename=
        safe_text
)
website_DynamicUnit_strategy = st.builds(
    website_DynamicUnit,
    footerClass=
        safe_text,
    errorClass=
        safe_text,
    controlClass=
        safe_text,
    header=
        safe_text,
    headerClass=
        safe_text,
    footer=
        safe_text
)
website_StaticUnit_strategy = st.builds(
    website_StaticUnit,
    styleClass=
        safe_text,
    contentClass=
        safe_text,
    content=
        safe_text
)
website_UnitContainer_strategy = st.builds(
    website_UnitContainer,
)
website_UnitField_strategy = st.builds(
    website_UnitField,
    title=
        safe_text,
    collectionAllowRemove=
        st.booleans(),
    maximumDisplaySize=
        st.integers(),
    collectionAllowAdd=
        st.booleans(),
    collectionDisplayOption=
        safe_text,
    dateFormat=
        safe_text
)
website_Query_strategy = st.builds(
    website_Query,
)
MenuEntry_strategy = st.builds(
    MenuEntry,
)
website_MenuFeature_strategy = st.builds(
    website_MenuFeature,
)
Menu_strategy = st.builds(
    Menu,
)
website_DynamicMenu_strategy = st.builds(
    website_DynamicMenu,
)
website_StaticMenu_strategy = st.builds(
    website_StaticMenu,
)
website_MenuEntry_strategy = st.builds(
    website_MenuEntry,
    requiresRole=
        safe_text
)
website_QueryParameter_strategy = st.builds(
    website_QueryParameter,
    value=
        safe_text
)
UnitContainer_strategy = st.builds(
    UnitContainer,
)
website_UnitAssociation_strategy = st.builds(
    website_UnitAssociation,
    isSourceAssociation=
        st.booleans()
)
ImageFilter_strategy = st.builds(
    ImageFilter,
)
website_ThumbnailFilter_strategy = st.builds(
    website_ThumbnailFilter,
    height=
        st.integers(),
    width=
        st.integers()
)
website_ImageFilter_strategy = st.builds(
    website_ImageFilter,
)
website_Order_strategy = st.builds(
    website_Order,
)
website_Predicate_strategy = st.builds(
    website_Predicate,
)
website_PageLink_strategy = st.builds(
    website_PageLink,
)
EntityAssociation_strategy = st.builds(
    EntityAssociation,
)
website_AssociationWithContainment_strategy = st.builds(
    website_AssociationWithContainment,
    sourceVisible=
        st.booleans()
)
website_AssociationWithoutContainment_strategy = st.builds(
    website_AssociationWithoutContainment,
    targetUnique=
        st.booleans(),
    targetCardinality=
        safe_text
)
EncapsulatedFeature_strategy = st.builds(
    EncapsulatedFeature,
)
ViewFeature_strategy = st.builds(
    ViewFeature,
)
website_EncapsulatedFeature_strategy = st.builds(
    website_EncapsulatedFeature,
    columnName=
        safe_text,
    displayLabel=
        safe_text,
    alias=
        safe_text
)
PathElement_strategy = st.builds(
    PathElement,
)
website_DatePathElement_strategy = st.builds(
    website_DatePathElement,
    format=
        safe_text
)
website_StaticPathElement_strategy = st.builds(
    website_StaticPathElement,
    element=
        safe_text
)
website_PathElement_strategy = st.builds(
    website_PathElement,
)
EntityAttribute_strategy = st.builds(
    EntityAttribute,
)
website_DateAttribute_strategy = st.builds(
    website_DateAttribute,
    format=
        safe_text,
    details=
        safe_text
)
website_UrlAttribute_strategy = st.builds(
    website_UrlAttribute,
    displayValue=
        safe_text
)
website_ResourceAttribute_strategy = st.builds(
    website_ResourceAttribute,
    validUploadMimeTypes=
        safe_text,
    uploadsWithinWebsite=
        st.booleans(),
    validUploadExtensions=
        safe_text,
    maximumUploadSize=
        st.integers()
)
website_DataTypeAttribute_strategy = st.builds(
    website_DataTypeAttribute,
    obfuscateFormFields=
        st.booleans(),
    encrypt=
        st.booleans(),
    caseInsensitive=
        st.booleans()
)
Attribute_strategy = st.builds(
    Attribute,
)
website_EncapsulatedAttribute_strategy = st.builds(
    website_EncapsulatedAttribute,
    name=
        safe_text,
    cardinality=
        safe_text
)
EntityFeature_strategy = st.builds(
    EntityFeature,
)
website_AssociationKey_strategy = st.builds(
    website_AssociationKey,
    targetColumnName=
        safe_text
)
Association_strategy = st.builds(
    Association,
)
website_LocationAttribute_strategy = st.builds(
    website_LocationAttribute,
)
ResourceAttribute_strategy = st.builds(
    ResourceAttribute,
)
website_ImageAttribute_strategy = st.builds(
    website_ImageAttribute,
)
website_FileAttribute_strategy = st.builds(
    website_FileAttribute,
)
EntityOrView_strategy = st.builds(
    EntityOrView,
)
website_View_strategy = st.builds(
    website_View,
)
website_Entity_strategy = st.builds(
    website_Entity,
)
website_EntityAssociation_strategy = st.builds(
    website_EntityAssociation,
    targetDisplayClass=
        safe_text,
    targetInputClass=
        safe_text,
    targetPrimaryKey=
        st.booleans(),
    pivotTableName=
        safe_text,
    targetFooterClass=
        safe_text,
    targetDisplayLabel=
        safe_text,
    targetHeaderClass=
        safe_text,
    bidirectional=
        st.booleans(),
    targetFeatureName=
        safe_text
)
ModelLabelFeature_strategy = st.builds(
    ModelLabelFeature,
)
website_ModelLabelAssociation_strategy = st.builds(
    website_ModelLabelAssociation,
    isSourceAssociation=
        st.booleans()
)
website_ModelLabelAttribute_strategy = st.builds(
    website_ModelLabelAttribute,
    dateFormat=
        safe_text
)
website_ModelLabelFeature_strategy = st.builds(
    website_ModelLabelFeature,
)
website_Label_strategy = st.builds(
    website_Label,
)
website_EntityAttribute_strategy = st.builds(
    website_EntityAttribute,
    persistentType=
        safe_text,
    interfaceType=
        safe_text,
    containerUnique=
        st.booleans(),
    primaryKey=
        st.booleans(),
    ormType=
        safe_text
)
website_Expression_strategy = st.builds(
    website_Expression,
)
Label_strategy = st.builds(
    Label,
)
Feature_strategy = st.builds(
    Feature,
)
website_ViewFeature_strategy = st.builds(
    website_ViewFeature,
)
website_Association_strategy = st.builds(
    website_Association,
    pseudo=
        st.booleans(),
    inputClass=
        safe_text,
    serializationMaxDepth=
        st.integers()
)
website_EncapsulatedAssociation_strategy = st.builds(
    website_EncapsulatedAssociation,
    cardinality=
        safe_text,
    name=
        safe_text,
    isSourceAssociation=
        st.booleans()
)
website_Feature_strategy = st.builds(
    website_Feature,
    serializationExpose=
        st.booleans(),
    displayClass=
        safe_text,
    collectionAllowAdd=
        st.booleans(),
    encodeUriKey=
        st.booleans(),
    nullDisplayValue=
        safe_text,
    serializationGroups=
        safe_text,
    headerClass=
        safe_text,
    footerClass=
        safe_text,
    collectionAllowRemove=
        st.booleans(),
    title=
        safe_text
)
DataType_strategy = st.builds(
    DataType,
)
website_EnumerationType_strategy = st.builds(
    website_EnumerationType,
)
website_NamedElement_strategy = st.builds(
    website_NamedElement,
    name=
        safe_text
)
website_ForgottenPasswordUnit_strategy = st.builds(
    website_ForgottenPasswordUnit,
    styleClass=
        safe_text
)
website_LoginUnit_strategy = st.builds(
    website_LoginUnit,
    styleClass=
        safe_text,
    logoutUriElement=
        safe_text
)
website_RegistrationUnit_strategy = st.builds(
    website_RegistrationUnit,
    styleClass=
        safe_text
)
Authentication_strategy = st.builds(
    Authentication,
)
website_CasAuthentication_strategy = st.builds(
    website_CasAuthentication,
)
website_LocalAuthenticationSystem_strategy = st.builds(
    website_LocalAuthenticationSystem,
    authenticationKey=
        safe_text,
    sendWelcomeEmail=
        st.booleans(),
    allowRememberMe=
        st.booleans(),
    useCaptcha=
        st.booleans(),
    trackLoginAttempts=
        st.booleans(),
    useEmailActivation=
        st.booleans(),
    allowSelfRegistration=
        st.booleans()
)
website_Attribute_strategy = st.builds(
    website_Attribute,
    inputClass=
        safe_text,
    placeholder=
        safe_text,
    validationPattern=
        safe_text
)
Classifier_strategy = st.builds(
    Classifier,
)
website_DataType_strategy = st.builds(
    website_DataType,
    interfaceType=
        safe_text,
    persistentType=
        safe_text,
    placeholder=
        safe_text,
    ormType=
        safe_text,
    validationPattern=
        safe_text
)
NamedDisplayElement_strategy = st.builds(
    NamedDisplayElement,
)
website_ContentUnit_strategy = st.builds(
    website_ContentUnit,
    alternative=
        safe_text,
    requiresRole=
        safe_text,
    purposeSummary=
        safe_text,
    uriElement=
        safe_text,
    captionClass=
        safe_text,
    omitCaption=
        st.booleans(),
    createDefaultUriElement=
        st.booleans()
)
website_InterfaceField_strategy = st.builds(
    website_InterfaceField,
    inputClass=
        safe_text,
    required=
        st.booleans(),
    defaultValue=
        safe_text,
    validationPattern=
        safe_text,
    placeholder=
        safe_text
)
website_EditStaticTextMenuEntry_strategy = st.builds(
    website_EditStaticTextMenuEntry,
)
website_EntityFeature_strategy = st.builds(
    website_EntityFeature,
    columnName=
        safe_text,
    singletonName=
        safe_text,
    cardinality=
        safe_text,
    pluralisedName=
        safe_text,
    ordered=
        st.booleans(),
    booleanIsHasChoice=
        safe_text,
    unique=
        st.booleans()
)
website_InlineAction_strategy = st.builds(
    website_InlineAction,
    header=
        safe_text,
    headerClass=
        safe_text,
    footer=
        safe_text,
    footerClass=
        safe_text,
    disable=
        st.booleans(),
    requiresRole=
        safe_text
)
website_EnumerationLiteral_strategy = st.builds(
    website_EnumerationLiteral,
)
website_Filter_strategy = st.builds(
    website_Filter,
)
website_ActionMenuEntry_strategy = st.builds(
    website_ActionMenuEntry,
)
website_ViewAssociation_strategy = st.builds(
    website_ViewAssociation,
    cardinality=
        safe_text
)
website_UnitSupportAction_strategy = st.builds(
    website_UnitSupportAction,
    confirmMessage=
        safe_text,
    disable=
        st.booleans()
)
NamedElement_strategy = st.builds(
    NamedElement,
)
website_FilterParameter_strategy = st.builds(
    website_FilterParameter,
    placeholder=
        safe_text,
    defaultValue=
        safe_text
)
website_Selection_strategy = st.builds(
    website_Selection,
    limit=
        st.integers(),
    distinct=
        st.booleans(),
    selected=
        st.booleans()
)
website_BusinessOperation_strategy = st.builds(
    website_BusinessOperation,
    resultType=
        safe_text,
    resultMimeType=
        safe_text
)
website_SelectionParameter_strategy = st.builds(
    website_SelectionParameter,
    optional=
        st.booleans(),
    defaultValue=
        safe_text
)
website_ModelLabel_strategy = st.builds(
    website_ModelLabel,
    format=
        safe_text
)
website_NamedDisplayElement_strategy = st.builds(
    website_NamedDisplayElement,
    displayLabel=
        safe_text
)
website_Authentication_strategy = st.builds(
    website_Authentication,
    loginLabel=
        safe_text,
    logoutLabel=
        safe_text
)
website_ImageManipulation_strategy = st.builds(
    website_ImageManipulation,
    jpegQuality=
        st.integers()
)
website_EntityOrView_strategy = st.builds(
    website_EntityOrView,
    tableName=
        safe_text,
    serializationExcludeAll=
        st.booleans(),
    pluralisedName=
        safe_text,
    implementsUserInterface=
        st.booleans(),
    autoKeyName=
        safe_text,
    autoKeyPersistentType=
        safe_text,
    autoKeyGenerationStrategy=
        safe_text,
    singletonName=
        safe_text
)
website_Menu_strategy = st.builds(
    website_Menu,
    captionClass=
        safe_text,
    styleClass=
        safe_text,
    layoutClass=
        safe_text,
    omitCaption=
        st.booleans()
)
website_Page_strategy = st.builds(
    website_Page,
    authenticated=
        st.booleans(),
    topMenuOption=
        safe_text,
    styleClass=
        safe_text,
    uriElement=
        safe_text,
    navigationLabel=
        safe_text,
    topMenuRank=
        st.integers()
)
website_Service_strategy = st.builds(
    website_Service,
)
website_Classifier_strategy = st.builds(
    website_Classifier,
)
website_WebsiteProperties_strategy = st.builds(
    website_WebsiteProperties,
    staticUnitsEditable=
        st.booleans(),
    databasePrefix=
        safe_text,
    inputTechnology=
        safe_text,
    rewriteURLs=
        st.booleans(),
    frameworkTechnology=
        safe_text,
    databaseTechnology=
        safe_text,
    ormTechnology=
        safe_text,
    topNavigationId=
        safe_text,
    siteTemplate=
        safe_text,
    projectName=
        safe_text,
    metaDescription=
        safe_text,
    defaultTimeFormat=
        safe_text,
    captchaSecretKey=
        safe_text,
    databaseHost=
        safe_text,
    databaseName=
        safe_text,
    timestampCreation=
        st.booleans(),
    responsiveTopMenu=
        st.booleans(),
    textEditorURL=
        safe_text,
    captchaSiteKey=
        safe_text,
    defaultMaximumUploadSize=
        st.integers(),
    webmasterEmail=
        safe_text,
    defaultDateTimeFormat=
        safe_text,
    databasePassword=
        safe_text,
    databaseUsername=
        safe_text,
    ajaxTechnology=
        safe_text,
    defaultDateFormat=
        safe_text,
    developmentVersion=
        st.booleans(),
    copyrightText=
        safe_text,
    baseURL=
        safe_text,
    testProjectName=
        safe_text,
    databasePort=
        safe_text,
    timestampUpdates=
        st.booleans(),
    siteTitle=
        safe_text
)
website_WebGenModel_strategy = st.builds(
    website_WebGenModel,
)

@given(instance=Path_strategy)
@settings(max_examples=50)
def test_path_instantiation(instance):
    assert isinstance(instance, Path)

@given(instance=website_CurrentUserReference_strategy)
@settings(max_examples=50)
def test_website_currentuserreference_instantiation(instance):
    assert isinstance(instance, website_CurrentUserReference)

@given(instance=website_RouteParameterReference_strategy)
@settings(max_examples=50)
def test_website_routeparameterreference_instantiation(instance):
    assert isinstance(instance, website_RouteParameterReference)



@given(instance=website_RouteParameterReference_strategy)
def test_website_routeparameterreference_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=website_FeatureReference_strategy)
@settings(max_examples=50)
def test_website_featurereference_instantiation(instance):
    assert isinstance(instance, website_FeatureReference)



@given(instance=website_FeatureReference_strategy)
def test_website_featurereference_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=website_ModelReference_strategy)
@settings(max_examples=50)
def test_website_modelreference_instantiation(instance):
    assert isinstance(instance, website_ModelReference)

@given(instance=website_ParameterReference_strategy)
@settings(max_examples=50)
def test_website_parameterreference_instantiation(instance):
    assert isinstance(instance, website_ParameterReference)



@given(instance=website_ParameterReference_strategy)
def test_website_parameterreference_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=website_InlineActionContainer_strategy)
@settings(max_examples=50)
def test_website_inlineactioncontainer_instantiation(instance):
    assert isinstance(instance, website_InlineActionContainer)

@given(instance=AuthenticationUnit_strategy)
@settings(max_examples=50)
def test_authenticationunit_instantiation(instance):
    assert isinstance(instance, AuthenticationUnit)

@given(instance=website_AuthenticationUnit_strategy)
@settings(max_examples=50)
def test_website_authenticationunit_instantiation(instance):
    assert isinstance(instance, website_AuthenticationUnit)

@given(instance=ImageUnit_strategy)
@settings(max_examples=50)
def test_imageunit_instantiation(instance):
    assert isinstance(instance, ImageUnit)

@given(instance=website_GalleryUnit_strategy)
@settings(max_examples=50)
def test_website_galleryunit_instantiation(instance):
    assert isinstance(instance, website_GalleryUnit)



@given(instance=website_GalleryUnit_strategy)
def test_website_galleryunit_contentClass_setter(instance):
    original = instance.contentClass
    instance.contentClass = original
    assert instance.contentClass == original



@given(instance=website_GalleryUnit_strategy)
def test_website_galleryunit_styleClass_setter(instance):
    original = instance.styleClass
    instance.styleClass = original
    assert instance.styleClass == original

@given(instance=website_SliderUnit_strategy)
@settings(max_examples=50)
def test_website_sliderunit_instantiation(instance):
    assert isinstance(instance, website_SliderUnit)



@given(instance=website_SliderUnit_strategy)
def test_website_sliderunit_styleClass_setter(instance):
    original = instance.styleClass
    instance.styleClass = original
    assert instance.styleClass == original



@given(instance=website_SliderUnit_strategy)
def test_website_sliderunit_contentClass_setter(instance):
    original = instance.contentClass
    instance.contentClass = original
    assert instance.contentClass == original

@given(instance=InlineAction_strategy)
@settings(max_examples=50)
def test_inlineaction_instantiation(instance):
    assert isinstance(instance, InlineAction)

@given(instance=website_DeleteAction_strategy)
@settings(max_examples=50)
def test_website_deleteaction_instantiation(instance):
    assert isinstance(instance, website_DeleteAction)



@given(instance=website_DeleteAction_strategy)
def test_website_deleteaction_confirmMessage_setter(instance):
    original = instance.confirmMessage
    instance.confirmMessage = original
    assert instance.confirmMessage == original



@given(instance=website_DeleteAction_strategy)
def test_website_deleteaction_uriElement_setter(instance):
    original = instance.uriElement
    instance.uriElement = original
    assert instance.uriElement == original

@given(instance=website_FeatureSupportAction_strategy)
@settings(max_examples=50)
def test_website_featuresupportaction_instantiation(instance):
    assert isinstance(instance, website_FeatureSupportAction)



@given(instance=website_FeatureSupportAction_strategy)
def test_website_featuresupportaction_fileExtension_setter(instance):
    original = instance.fileExtension
    instance.fileExtension = original
    assert instance.fileExtension == original



@given(instance=website_FeatureSupportAction_strategy)
def test_website_featuresupportaction_uriElement_setter(instance):
    original = instance.uriElement
    instance.uriElement = original
    assert instance.uriElement == original



@given(instance=website_FeatureSupportAction_strategy)
def test_website_featuresupportaction_confirmMessage_setter(instance):
    original = instance.confirmMessage
    instance.confirmMessage = original
    assert instance.confirmMessage == original

@given(instance=website_SelectAction_strategy)
@settings(max_examples=50)
def test_website_selectaction_instantiation(instance):
    assert isinstance(instance, website_SelectAction)

@given(instance=ChildPath_strategy)
@settings(max_examples=50)
def test_childpath_instantiation(instance):
    assert isinstance(instance, ChildPath)

@given(instance=website_ChildPathAttribute_strategy)
@settings(max_examples=50)
def test_website_childpathattribute_instantiation(instance):
    assert isinstance(instance, website_ChildPathAttribute)



@given(instance=website_ChildPathAttribute_strategy)
def test_website_childpathattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=FeaturePath_strategy)
@settings(max_examples=50)
def test_featurepath_instantiation(instance):
    assert isinstance(instance, FeaturePath)

@given(instance=website_FeaturePathAttribute_strategy)
@settings(max_examples=50)
def test_website_featurepathattribute_instantiation(instance):
    assert isinstance(instance, website_FeaturePathAttribute)



@given(instance=website_FeaturePathAttribute_strategy)
def test_website_featurepathattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=website_FeaturePath_strategy)
@settings(max_examples=50)
def test_website_featurepath_instantiation(instance):
    assert isinstance(instance, website_FeaturePath)

@given(instance=CollectionUnit_strategy)
@settings(max_examples=50)
def test_collectionunit_instantiation(instance):
    assert isinstance(instance, CollectionUnit)

@given(instance=DataUnit_strategy)
@settings(max_examples=50)
def test_dataunit_instantiation(instance):
    assert isinstance(instance, DataUnit)

@given(instance=ControlUnit_strategy)
@settings(max_examples=50)
def test_controlunit_instantiation(instance):
    assert isinstance(instance, ControlUnit)

@given(instance=website_SearchUnit_strategy)
@settings(max_examples=50)
def test_website_searchunit_instantiation(instance):
    assert isinstance(instance, website_SearchUnit)



@given(instance=website_SearchUnit_strategy)
def test_website_searchunit_styleClass_setter(instance):
    original = instance.styleClass
    instance.styleClass = original
    assert instance.styleClass == original

@given(instance=SingletonUnit_strategy)
@settings(max_examples=50)
def test_singletonunit_instantiation(instance):
    assert isinstance(instance, SingletonUnit)

@given(instance=DynamicUnit_strategy)
@settings(max_examples=50)
def test_dynamicunit_instantiation(instance):
    assert isinstance(instance, DynamicUnit)

@given(instance=website_DataUnit_strategy)
@settings(max_examples=50)
def test_website_dataunit_instantiation(instance):
    assert isinstance(instance, website_DataUnit)

@given(instance=website_ImageUnit_strategy)
@settings(max_examples=50)
def test_website_imageunit_instantiation(instance):
    assert isinstance(instance, website_ImageUnit)



@given(instance=website_ImageUnit_strategy)
def test_website_imageunit_showTime_setter(instance):
    original = instance.showTime
    instance.showTime = original
    assert instance.showTime == original



@given(instance=website_ImageUnit_strategy)
def test_website_imageunit_transitionTime_setter(instance):
    original = instance.transitionTime
    instance.transitionTime = original
    assert instance.transitionTime == original



@given(instance=website_ImageUnit_strategy)
def test_website_imageunit_missingImagePath_setter(instance):
    original = instance.missingImagePath
    instance.missingImagePath = original
    assert instance.missingImagePath == original

@given(instance=website_ControlUnit_strategy)
@settings(max_examples=50)
def test_website_controlunit_instantiation(instance):
    assert isinstance(instance, website_ControlUnit)



@given(instance=website_ControlUnit_strategy)
def test_website_controlunit_submitLabel_setter(instance):
    original = instance.submitLabel
    instance.submitLabel = original
    assert instance.submitLabel == original



@given(instance=website_ControlUnit_strategy)
def test_website_controlunit_cancelLabel_setter(instance):
    original = instance.cancelLabel
    instance.cancelLabel = original
    assert instance.cancelLabel == original



@given(instance=website_ControlUnit_strategy)
def test_website_controlunit_contentClass_setter(instance):
    original = instance.contentClass
    instance.contentClass = original
    assert instance.contentClass == original

@given(instance=website_EditUnit_strategy)
@settings(max_examples=50)
def test_website_editunit_instantiation(instance):
    assert isinstance(instance, website_EditUnit)



@given(instance=website_EditUnit_strategy)
def test_website_editunit_cancelLabel_setter(instance):
    original = instance.cancelLabel
    instance.cancelLabel = original
    assert instance.cancelLabel == original



@given(instance=website_EditUnit_strategy)
def test_website_editunit_contentClass_setter(instance):
    original = instance.contentClass
    instance.contentClass = original
    assert instance.contentClass == original



@given(instance=website_EditUnit_strategy)
def test_website_editunit_customiseValues_setter(instance):
    original = instance.customiseValues
    instance.customiseValues = original
    assert instance.customiseValues == original



@given(instance=website_EditUnit_strategy)
def test_website_editunit_confirmLabel_setter(instance):
    original = instance.confirmLabel
    instance.confirmLabel = original
    assert instance.confirmLabel == original

@given(instance=EditUnit_strategy)
@settings(max_examples=50)
def test_editunit_instantiation(instance):
    assert isinstance(instance, EditUnit)

@given(instance=website_CreateUnit_strategy)
@settings(max_examples=50)
def test_website_createunit_instantiation(instance):
    assert isinstance(instance, website_CreateUnit)



@given(instance=website_CreateUnit_strategy)
def test_website_createunit_styleClass_setter(instance):
    original = instance.styleClass
    instance.styleClass = original
    assert instance.styleClass == original

@given(instance=InterfaceField_strategy)
@settings(max_examples=50)
def test_interfacefield_instantiation(instance):
    assert isinstance(instance, InterfaceField)

@given(instance=website_DateField_strategy)
@settings(max_examples=50)
def test_website_datefield_instantiation(instance):
    assert isinstance(instance, website_DateField)



@given(instance=website_DateField_strategy)
def test_website_datefield_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original



@given(instance=website_DateField_strategy)
def test_website_datefield_details_setter(instance):
    original = instance.details
    instance.details = original
    assert instance.details == original

@given(instance=website_DataTypeField_strategy)
@settings(max_examples=50)
def test_website_datatypefield_instantiation(instance):
    assert isinstance(instance, website_DataTypeField)



@given(instance=website_DataTypeField_strategy)
def test_website_datatypefield_encrypt_setter(instance):
    original = instance.encrypt
    instance.encrypt = original
    assert instance.encrypt == original



@given(instance=website_DataTypeField_strategy)
def test_website_datatypefield_interfaceType_setter(instance):
    original = instance.interfaceType
    instance.interfaceType = original
    assert instance.interfaceType == original



@given(instance=website_DataTypeField_strategy)
def test_website_datatypefield_obfuscateFormFields_setter(instance):
    original = instance.obfuscateFormFields
    instance.obfuscateFormFields = original
    assert instance.obfuscateFormFields == original

@given(instance=website_ChildPath_strategy)
@settings(max_examples=50)
def test_website_childpath_instantiation(instance):
    assert isinstance(instance, website_ChildPath)

@given(instance=website_AssociationReference_strategy)
@settings(max_examples=50)
def test_website_associationreference_instantiation(instance):
    assert isinstance(instance, website_AssociationReference)



@given(instance=website_AssociationReference_strategy)
def test_website_associationreference_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SelectableUnit_strategy)
@settings(max_examples=50)
def test_selectableunit_instantiation(instance):
    assert isinstance(instance, SelectableUnit)

@given(instance=website_DetailsUnit_strategy)
@settings(max_examples=50)
def test_website_detailsunit_instantiation(instance):
    assert isinstance(instance, website_DetailsUnit)



@given(instance=website_DetailsUnit_strategy)
def test_website_detailsunit_contentClass_setter(instance):
    original = instance.contentClass
    instance.contentClass = original
    assert instance.contentClass == original



@given(instance=website_DetailsUnit_strategy)
def test_website_detailsunit_omitFieldLabels_setter(instance):
    original = instance.omitFieldLabels
    instance.omitFieldLabels = original
    assert instance.omitFieldLabels == original



@given(instance=website_DetailsUnit_strategy)
def test_website_detailsunit_styleClass_setter(instance):
    original = instance.styleClass
    instance.styleClass = original
    assert instance.styleClass == original



@given(instance=website_DetailsUnit_strategy)
def test_website_detailsunit_onlyDisplayWhenNotEmpty_setter(instance):
    original = instance.onlyDisplayWhenNotEmpty
    instance.onlyDisplayWhenNotEmpty = original
    assert instance.onlyDisplayWhenNotEmpty == original

@given(instance=website_UpdateUnit_strategy)
@settings(max_examples=50)
def test_website_updateunit_instantiation(instance):
    assert isinstance(instance, website_UpdateUnit)



@given(instance=website_UpdateUnit_strategy)
def test_website_updateunit_styleClass_setter(instance):
    original = instance.styleClass
    instance.styleClass = original
    assert instance.styleClass == original

@given(instance=website_CreateUpdateUnit_strategy)
@settings(max_examples=50)
def test_website_createupdateunit_instantiation(instance):
    assert isinstance(instance, website_CreateUpdateUnit)



@given(instance=website_CreateUpdateUnit_strategy)
def test_website_createupdateunit_styleClass_setter(instance):
    original = instance.styleClass
    instance.styleClass = original
    assert instance.styleClass == original



@given(instance=website_CreateUpdateUnit_strategy)
def test_website_createupdateunit_clearLabel_setter(instance):
    original = instance.clearLabel
    instance.clearLabel = original
    assert instance.clearLabel == original



@given(instance=website_CreateUpdateUnit_strategy)
def test_website_createupdateunit_createUriElement_setter(instance):
    original = instance.createUriElement
    instance.createUriElement = original
    assert instance.createUriElement == original

@given(instance=website_MapUnit_strategy)
@settings(max_examples=50)
def test_website_mapunit_instantiation(instance):
    assert isinstance(instance, website_MapUnit)



@given(instance=website_MapUnit_strategy)
def test_website_mapunit_defaultZoomLevel_setter(instance):
    original = instance.defaultZoomLevel
    instance.defaultZoomLevel = original
    assert instance.defaultZoomLevel == original



@given(instance=website_MapUnit_strategy)
def test_website_mapunit_readOnly_setter(instance):
    original = instance.readOnly
    instance.readOnly = original
    assert instance.readOnly == original



@given(instance=website_MapUnit_strategy)
def test_website_mapunit_styleClass_setter(instance):
    original = instance.styleClass
    instance.styleClass = original
    assert instance.styleClass == original

@given(instance=website_CollectionUnit_strategy)
@settings(max_examples=50)
def test_website_collectionunit_instantiation(instance):
    assert isinstance(instance, website_CollectionUnit)



@given(instance=website_CollectionUnit_strategy)
def test_website_collectionunit_useFirstLastPageLinks_setter(instance):
    original = instance.useFirstLastPageLinks
    instance.useFirstLastPageLinks = original
    assert instance.useFirstLastPageLinks == original



@given(instance=website_CollectionUnit_strategy)
def test_website_collectionunit_nextNpages_setter(instance):
    original = instance.nextNpages
    instance.nextNpages = original
    assert instance.nextNpages == original



@given(instance=website_CollectionUnit_strategy)
def test_website_collectionunit_lastPageLabel_setter(instance):
    original = instance.lastPageLabel
    instance.lastPageLabel = original
    assert instance.lastPageLabel == original



@given(instance=website_CollectionUnit_strategy)
def test_website_collectionunit_useDisabledPageLinks_setter(instance):
    original = instance.useDisabledPageLinks
    instance.useDisabledPageLinks = original
    assert instance.useDisabledPageLinks == original



@given(instance=website_CollectionUnit_strategy)
def test_website_collectionunit_nextPageLabel_setter(instance):
    original = instance.nextPageLabel
    instance.nextPageLabel = original
    assert instance.nextPageLabel == original



@given(instance=website_CollectionUnit_strategy)
def test_website_collectionunit_defaultPaginationSize_setter(instance):
    original = instance.defaultPaginationSize
    instance.defaultPaginationSize = original
    assert instance.defaultPaginationSize == original



@given(instance=website_CollectionUnit_strategy)
def test_website_collectionunit_previousNpages_setter(instance):
    original = instance.previousNpages
    instance.previousNpages = original
    assert instance.previousNpages == original



@given(instance=website_CollectionUnit_strategy)
def test_website_collectionunit_previousPageLabel_setter(instance):
    original = instance.previousPageLabel
    instance.previousPageLabel = original
    assert instance.previousPageLabel == original



@given(instance=website_CollectionUnit_strategy)
def test_website_collectionunit_firstPageLabel_setter(instance):
    original = instance.firstPageLabel
    instance.firstPageLabel = original
    assert instance.firstPageLabel == original



@given(instance=website_CollectionUnit_strategy)
def test_website_collectionunit_emptyMessage_setter(instance):
    original = instance.emptyMessage
    instance.emptyMessage = original
    assert instance.emptyMessage == original

@given(instance=website_SingletonUnit_strategy)
@settings(max_examples=50)
def test_website_singletonunit_instantiation(instance):
    assert isinstance(instance, website_SingletonUnit)

@given(instance=website_SelectableUnit_strategy)
@settings(max_examples=50)
def test_website_selectableunit_instantiation(instance):
    assert isinstance(instance, website_SelectableUnit)

@given(instance=website_CaptchaField_strategy)
@settings(max_examples=50)
def test_website_captchafield_instantiation(instance):
    assert isinstance(instance, website_CaptchaField)

@given(instance=UnitFeature_strategy)
@settings(max_examples=50)
def test_unitfeature_instantiation(instance):
    assert isinstance(instance, UnitFeature)

@given(instance=website_UnitElement_strategy)
@settings(max_examples=50)
def test_website_unitelement_instantiation(instance):
    assert isinstance(instance, website_UnitElement)



@given(instance=website_UnitElement_strategy)
def test_website_unitelement_validationPattern_setter(instance):
    original = instance.validationPattern
    instance.validationPattern = original
    assert instance.validationPattern == original



@given(instance=website_UnitElement_strategy)
def test_website_unitelement_obfuscateFormFields_setter(instance):
    original = instance.obfuscateFormFields
    instance.obfuscateFormFields = original
    assert instance.obfuscateFormFields == original



@given(instance=website_UnitElement_strategy)
def test_website_unitelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=website_UnitElement_strategy)
def test_website_unitelement_placeholder_setter(instance):
    original = instance.placeholder
    instance.placeholder = original
    assert instance.placeholder == original

@given(instance=InlineActionContainer_strategy)
@settings(max_examples=50)
def test_inlineactioncontainer_instantiation(instance):
    assert isinstance(instance, InlineActionContainer)

@given(instance=website_IndexUnit_strategy)
@settings(max_examples=50)
def test_website_indexunit_instantiation(instance):
    assert isinstance(instance, website_IndexUnit)



@given(instance=website_IndexUnit_strategy)
def test_website_indexunit_omitColumnLabels_setter(instance):
    original = instance.omitColumnLabels
    instance.omitColumnLabels = original
    assert instance.omitColumnLabels == original



@given(instance=website_IndexUnit_strategy)
def test_website_indexunit_styleClass_setter(instance):
    original = instance.styleClass
    instance.styleClass = original
    assert instance.styleClass == original



@given(instance=website_IndexUnit_strategy)
def test_website_indexunit_displayOption_setter(instance):
    original = instance.displayOption
    instance.displayOption = original
    assert instance.displayOption == original



@given(instance=website_IndexUnit_strategy)
def test_website_indexunit_contentClass_setter(instance):
    original = instance.contentClass
    instance.contentClass = original
    assert instance.contentClass == original



@given(instance=website_IndexUnit_strategy)
def test_website_indexunit_rowClasses_setter(instance):
    original = instance.rowClasses
    instance.rowClasses = original
    assert instance.rowClasses == original

@given(instance=website_ImageIndexUnit_strategy)
@settings(max_examples=50)
def test_website_imageindexunit_instantiation(instance):
    assert isinstance(instance, website_ImageIndexUnit)



@given(instance=website_ImageIndexUnit_strategy)
def test_website_imageindexunit_contentClass_setter(instance):
    original = instance.contentClass
    instance.contentClass = original
    assert instance.contentClass == original



@given(instance=website_ImageIndexUnit_strategy)
def test_website_imageindexunit_styleClass_setter(instance):
    original = instance.styleClass
    instance.styleClass = original
    assert instance.styleClass == original

@given(instance=UnitField_strategy)
@settings(max_examples=50)
def test_unitfield_instantiation(instance):
    assert isinstance(instance, UnitField)

@given(instance=website_UnitFeature_strategy)
@settings(max_examples=50)
def test_website_unitfeature_instantiation(instance):
    assert isinstance(instance, website_UnitFeature)



@given(instance=website_UnitFeature_strategy)
def test_website_unitfeature_displayLabel_setter(instance):
    original = instance.displayLabel
    instance.displayLabel = original
    assert instance.displayLabel == original



@given(instance=website_UnitFeature_strategy)
def test_website_unitfeature_displayClass_setter(instance):
    original = instance.displayClass
    instance.displayClass = original
    assert instance.displayClass == original



@given(instance=website_UnitFeature_strategy)
def test_website_unitfeature_headerClass_setter(instance):
    original = instance.headerClass
    instance.headerClass = original
    assert instance.headerClass == original



@given(instance=website_UnitFeature_strategy)
def test_website_unitfeature_onlyDisplayWhenNotEmpty_setter(instance):
    original = instance.onlyDisplayWhenNotEmpty
    instance.onlyDisplayWhenNotEmpty = original
    assert instance.onlyDisplayWhenNotEmpty == original



@given(instance=website_UnitFeature_strategy)
def test_website_unitfeature_footerClass_setter(instance):
    original = instance.footerClass
    instance.footerClass = original
    assert instance.footerClass == original



@given(instance=website_UnitFeature_strategy)
def test_website_unitfeature_required_setter(instance):
    original = instance.required
    instance.required = original
    assert instance.required == original



@given(instance=website_UnitFeature_strategy)
def test_website_unitfeature_autofocus_setter(instance):
    original = instance.autofocus
    instance.autofocus = original
    assert instance.autofocus == original



@given(instance=website_UnitFeature_strategy)
def test_website_unitfeature_inputClass_setter(instance):
    original = instance.inputClass
    instance.inputClass = original
    assert instance.inputClass == original



@given(instance=website_UnitFeature_strategy)
def test_website_unitfeature_nullDisplayValue_setter(instance):
    original = instance.nullDisplayValue
    instance.nullDisplayValue = original
    assert instance.nullDisplayValue == original



@given(instance=website_UnitFeature_strategy)
def test_website_unitfeature_footer_setter(instance):
    original = instance.footer
    instance.footer = original
    assert instance.footer == original

@given(instance=AssociationReference_strategy)
@settings(max_examples=50)
def test_associationreference_instantiation(instance):
    assert isinstance(instance, AssociationReference)

@given(instance=website_ChildPathAssociation_strategy)
@settings(max_examples=50)
def test_website_childpathassociation_instantiation(instance):
    assert isinstance(instance, website_ChildPathAssociation)



@given(instance=website_ChildPathAssociation_strategy)
def test_website_childpathassociation_isSourceAssociation_setter(instance):
    original = instance.isSourceAssociation
    instance.isSourceAssociation = original
    assert instance.isSourceAssociation == original

@given(instance=website_FeaturePathAssociation_strategy)
@settings(max_examples=50)
def test_website_featurepathassociation_instantiation(instance):
    assert isinstance(instance, website_FeaturePathAssociation)



@given(instance=website_FeaturePathAssociation_strategy)
def test_website_featurepathassociation_isSourceAssociation_setter(instance):
    original = instance.isSourceAssociation
    instance.isSourceAssociation = original
    assert instance.isSourceAssociation == original

@given(instance=ContentUnit_strategy)
@settings(max_examples=50)
def test_contentunit_instantiation(instance):
    assert isinstance(instance, ContentUnit)

@given(instance=website_CreateSitemapUnit_strategy)
@settings(max_examples=50)
def test_website_createsitemapunit_instantiation(instance):
    assert isinstance(instance, website_CreateSitemapUnit)



@given(instance=website_CreateSitemapUnit_strategy)
def test_website_createsitemapunit_contentClass_setter(instance):
    original = instance.contentClass
    instance.contentClass = original
    assert instance.contentClass == original



@given(instance=website_CreateSitemapUnit_strategy)
def test_website_createsitemapunit_styleClass_setter(instance):
    original = instance.styleClass
    instance.styleClass = original
    assert instance.styleClass == original



@given(instance=website_CreateSitemapUnit_strategy)
def test_website_createsitemapunit_deployedURL_setter(instance):
    original = instance.deployedURL
    instance.deployedURL = original
    assert instance.deployedURL == original



@given(instance=website_CreateSitemapUnit_strategy)
def test_website_createsitemapunit_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original

@given(instance=website_DynamicUnit_strategy)
@settings(max_examples=50)
def test_website_dynamicunit_instantiation(instance):
    assert isinstance(instance, website_DynamicUnit)



@given(instance=website_DynamicUnit_strategy)
def test_website_dynamicunit_footerClass_setter(instance):
    original = instance.footerClass
    instance.footerClass = original
    assert instance.footerClass == original



@given(instance=website_DynamicUnit_strategy)
def test_website_dynamicunit_errorClass_setter(instance):
    original = instance.errorClass
    instance.errorClass = original
    assert instance.errorClass == original



@given(instance=website_DynamicUnit_strategy)
def test_website_dynamicunit_controlClass_setter(instance):
    original = instance.controlClass
    instance.controlClass = original
    assert instance.controlClass == original



@given(instance=website_DynamicUnit_strategy)
def test_website_dynamicunit_header_setter(instance):
    original = instance.header
    instance.header = original
    assert instance.header == original



@given(instance=website_DynamicUnit_strategy)
def test_website_dynamicunit_headerClass_setter(instance):
    original = instance.headerClass
    instance.headerClass = original
    assert instance.headerClass == original



@given(instance=website_DynamicUnit_strategy)
def test_website_dynamicunit_footer_setter(instance):
    original = instance.footer
    instance.footer = original
    assert instance.footer == original

@given(instance=website_StaticUnit_strategy)
@settings(max_examples=50)
def test_website_staticunit_instantiation(instance):
    assert isinstance(instance, website_StaticUnit)



@given(instance=website_StaticUnit_strategy)
def test_website_staticunit_styleClass_setter(instance):
    original = instance.styleClass
    instance.styleClass = original
    assert instance.styleClass == original



@given(instance=website_StaticUnit_strategy)
def test_website_staticunit_contentClass_setter(instance):
    original = instance.contentClass
    instance.contentClass = original
    assert instance.contentClass == original



@given(instance=website_StaticUnit_strategy)
def test_website_staticunit_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=website_UnitContainer_strategy)
@settings(max_examples=50)
def test_website_unitcontainer_instantiation(instance):
    assert isinstance(instance, website_UnitContainer)

@given(instance=website_UnitField_strategy)
@settings(max_examples=50)
def test_website_unitfield_instantiation(instance):
    assert isinstance(instance, website_UnitField)



@given(instance=website_UnitField_strategy)
def test_website_unitfield_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=website_UnitField_strategy)
def test_website_unitfield_collectionAllowRemove_setter(instance):
    original = instance.collectionAllowRemove
    instance.collectionAllowRemove = original
    assert instance.collectionAllowRemove == original



@given(instance=website_UnitField_strategy)
def test_website_unitfield_maximumDisplaySize_setter(instance):
    original = instance.maximumDisplaySize
    instance.maximumDisplaySize = original
    assert instance.maximumDisplaySize == original



@given(instance=website_UnitField_strategy)
def test_website_unitfield_collectionAllowAdd_setter(instance):
    original = instance.collectionAllowAdd
    instance.collectionAllowAdd = original
    assert instance.collectionAllowAdd == original



@given(instance=website_UnitField_strategy)
def test_website_unitfield_collectionDisplayOption_setter(instance):
    original = instance.collectionDisplayOption
    instance.collectionDisplayOption = original
    assert instance.collectionDisplayOption == original



@given(instance=website_UnitField_strategy)
def test_website_unitfield_dateFormat_setter(instance):
    original = instance.dateFormat
    instance.dateFormat = original
    assert instance.dateFormat == original

@given(instance=website_Query_strategy)
@settings(max_examples=50)
def test_website_query_instantiation(instance):
    assert isinstance(instance, website_Query)

@given(instance=MenuEntry_strategy)
@settings(max_examples=50)
def test_menuentry_instantiation(instance):
    assert isinstance(instance, MenuEntry)

@given(instance=website_MenuFeature_strategy)
@settings(max_examples=50)
def test_website_menufeature_instantiation(instance):
    assert isinstance(instance, website_MenuFeature)

@given(instance=Menu_strategy)
@settings(max_examples=50)
def test_menu_instantiation(instance):
    assert isinstance(instance, Menu)

@given(instance=website_DynamicMenu_strategy)
@settings(max_examples=50)
def test_website_dynamicmenu_instantiation(instance):
    assert isinstance(instance, website_DynamicMenu)

@given(instance=website_StaticMenu_strategy)
@settings(max_examples=50)
def test_website_staticmenu_instantiation(instance):
    assert isinstance(instance, website_StaticMenu)

@given(instance=website_MenuEntry_strategy)
@settings(max_examples=50)
def test_website_menuentry_instantiation(instance):
    assert isinstance(instance, website_MenuEntry)



@given(instance=website_MenuEntry_strategy)
def test_website_menuentry_requiresRole_setter(instance):
    original = instance.requiresRole
    instance.requiresRole = original
    assert instance.requiresRole == original

@given(instance=website_QueryParameter_strategy)
@settings(max_examples=50)
def test_website_queryparameter_instantiation(instance):
    assert isinstance(instance, website_QueryParameter)



@given(instance=website_QueryParameter_strategy)
def test_website_queryparameter_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=UnitContainer_strategy)
@settings(max_examples=50)
def test_unitcontainer_instantiation(instance):
    assert isinstance(instance, UnitContainer)

@given(instance=website_UnitAssociation_strategy)
@settings(max_examples=50)
def test_website_unitassociation_instantiation(instance):
    assert isinstance(instance, website_UnitAssociation)



@given(instance=website_UnitAssociation_strategy)
def test_website_unitassociation_isSourceAssociation_setter(instance):
    original = instance.isSourceAssociation
    instance.isSourceAssociation = original
    assert instance.isSourceAssociation == original

@given(instance=ImageFilter_strategy)
@settings(max_examples=50)
def test_imagefilter_instantiation(instance):
    assert isinstance(instance, ImageFilter)

@given(instance=website_ThumbnailFilter_strategy)
@settings(max_examples=50)
def test_website_thumbnailfilter_instantiation(instance):
    assert isinstance(instance, website_ThumbnailFilter)



@given(instance=website_ThumbnailFilter_strategy)
def test_website_thumbnailfilter_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=website_ThumbnailFilter_strategy)
def test_website_thumbnailfilter_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=website_ImageFilter_strategy)
@settings(max_examples=50)
def test_website_imagefilter_instantiation(instance):
    assert isinstance(instance, website_ImageFilter)

@given(instance=website_Order_strategy)
@settings(max_examples=50)
def test_website_order_instantiation(instance):
    assert isinstance(instance, website_Order)

@given(instance=website_Predicate_strategy)
@settings(max_examples=50)
def test_website_predicate_instantiation(instance):
    assert isinstance(instance, website_Predicate)

@given(instance=website_PageLink_strategy)
@settings(max_examples=50)
def test_website_pagelink_instantiation(instance):
    assert isinstance(instance, website_PageLink)

@given(instance=EntityAssociation_strategy)
@settings(max_examples=50)
def test_entityassociation_instantiation(instance):
    assert isinstance(instance, EntityAssociation)

@given(instance=website_AssociationWithContainment_strategy)
@settings(max_examples=50)
def test_website_associationwithcontainment_instantiation(instance):
    assert isinstance(instance, website_AssociationWithContainment)



@given(instance=website_AssociationWithContainment_strategy)
def test_website_associationwithcontainment_sourceVisible_setter(instance):
    original = instance.sourceVisible
    instance.sourceVisible = original
    assert instance.sourceVisible == original

@given(instance=website_AssociationWithoutContainment_strategy)
@settings(max_examples=50)
def test_website_associationwithoutcontainment_instantiation(instance):
    assert isinstance(instance, website_AssociationWithoutContainment)



@given(instance=website_AssociationWithoutContainment_strategy)
def test_website_associationwithoutcontainment_targetUnique_setter(instance):
    original = instance.targetUnique
    instance.targetUnique = original
    assert instance.targetUnique == original



@given(instance=website_AssociationWithoutContainment_strategy)
def test_website_associationwithoutcontainment_targetCardinality_setter(instance):
    original = instance.targetCardinality
    instance.targetCardinality = original
    assert instance.targetCardinality == original

@given(instance=EncapsulatedFeature_strategy)
@settings(max_examples=50)
def test_encapsulatedfeature_instantiation(instance):
    assert isinstance(instance, EncapsulatedFeature)

@given(instance=ViewFeature_strategy)
@settings(max_examples=50)
def test_viewfeature_instantiation(instance):
    assert isinstance(instance, ViewFeature)

@given(instance=website_EncapsulatedFeature_strategy)
@settings(max_examples=50)
def test_website_encapsulatedfeature_instantiation(instance):
    assert isinstance(instance, website_EncapsulatedFeature)



@given(instance=website_EncapsulatedFeature_strategy)
def test_website_encapsulatedfeature_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original



@given(instance=website_EncapsulatedFeature_strategy)
def test_website_encapsulatedfeature_displayLabel_setter(instance):
    original = instance.displayLabel
    instance.displayLabel = original
    assert instance.displayLabel == original



@given(instance=website_EncapsulatedFeature_strategy)
def test_website_encapsulatedfeature_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=PathElement_strategy)
@settings(max_examples=50)
def test_pathelement_instantiation(instance):
    assert isinstance(instance, PathElement)

@given(instance=website_DatePathElement_strategy)
@settings(max_examples=50)
def test_website_datepathelement_instantiation(instance):
    assert isinstance(instance, website_DatePathElement)



@given(instance=website_DatePathElement_strategy)
def test_website_datepathelement_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original

@given(instance=website_StaticPathElement_strategy)
@settings(max_examples=50)
def test_website_staticpathelement_instantiation(instance):
    assert isinstance(instance, website_StaticPathElement)



@given(instance=website_StaticPathElement_strategy)
def test_website_staticpathelement_element_setter(instance):
    original = instance.element
    instance.element = original
    assert instance.element == original

@given(instance=website_PathElement_strategy)
@settings(max_examples=50)
def test_website_pathelement_instantiation(instance):
    assert isinstance(instance, website_PathElement)

@given(instance=EntityAttribute_strategy)
@settings(max_examples=50)
def test_entityattribute_instantiation(instance):
    assert isinstance(instance, EntityAttribute)

@given(instance=website_DateAttribute_strategy)
@settings(max_examples=50)
def test_website_dateattribute_instantiation(instance):
    assert isinstance(instance, website_DateAttribute)



@given(instance=website_DateAttribute_strategy)
def test_website_dateattribute_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original



@given(instance=website_DateAttribute_strategy)
def test_website_dateattribute_details_setter(instance):
    original = instance.details
    instance.details = original
    assert instance.details == original

@given(instance=website_UrlAttribute_strategy)
@settings(max_examples=50)
def test_website_urlattribute_instantiation(instance):
    assert isinstance(instance, website_UrlAttribute)



@given(instance=website_UrlAttribute_strategy)
def test_website_urlattribute_displayValue_setter(instance):
    original = instance.displayValue
    instance.displayValue = original
    assert instance.displayValue == original

@given(instance=website_ResourceAttribute_strategy)
@settings(max_examples=50)
def test_website_resourceattribute_instantiation(instance):
    assert isinstance(instance, website_ResourceAttribute)



@given(instance=website_ResourceAttribute_strategy)
def test_website_resourceattribute_validUploadMimeTypes_setter(instance):
    original = instance.validUploadMimeTypes
    instance.validUploadMimeTypes = original
    assert instance.validUploadMimeTypes == original



@given(instance=website_ResourceAttribute_strategy)
def test_website_resourceattribute_uploadsWithinWebsite_setter(instance):
    original = instance.uploadsWithinWebsite
    instance.uploadsWithinWebsite = original
    assert instance.uploadsWithinWebsite == original



@given(instance=website_ResourceAttribute_strategy)
def test_website_resourceattribute_validUploadExtensions_setter(instance):
    original = instance.validUploadExtensions
    instance.validUploadExtensions = original
    assert instance.validUploadExtensions == original



@given(instance=website_ResourceAttribute_strategy)
def test_website_resourceattribute_maximumUploadSize_setter(instance):
    original = instance.maximumUploadSize
    instance.maximumUploadSize = original
    assert instance.maximumUploadSize == original

@given(instance=website_DataTypeAttribute_strategy)
@settings(max_examples=50)
def test_website_datatypeattribute_instantiation(instance):
    assert isinstance(instance, website_DataTypeAttribute)



@given(instance=website_DataTypeAttribute_strategy)
def test_website_datatypeattribute_obfuscateFormFields_setter(instance):
    original = instance.obfuscateFormFields
    instance.obfuscateFormFields = original
    assert instance.obfuscateFormFields == original



@given(instance=website_DataTypeAttribute_strategy)
def test_website_datatypeattribute_encrypt_setter(instance):
    original = instance.encrypt
    instance.encrypt = original
    assert instance.encrypt == original



@given(instance=website_DataTypeAttribute_strategy)
def test_website_datatypeattribute_caseInsensitive_setter(instance):
    original = instance.caseInsensitive
    instance.caseInsensitive = original
    assert instance.caseInsensitive == original

@given(instance=Attribute_strategy)
@settings(max_examples=50)
def test_attribute_instantiation(instance):
    assert isinstance(instance, Attribute)

@given(instance=website_EncapsulatedAttribute_strategy)
@settings(max_examples=50)
def test_website_encapsulatedattribute_instantiation(instance):
    assert isinstance(instance, website_EncapsulatedAttribute)



@given(instance=website_EncapsulatedAttribute_strategy)
def test_website_encapsulatedattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=website_EncapsulatedAttribute_strategy)
def test_website_encapsulatedattribute_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original

@given(instance=EntityFeature_strategy)
@settings(max_examples=50)
def test_entityfeature_instantiation(instance):
    assert isinstance(instance, EntityFeature)

@given(instance=website_AssociationKey_strategy)
@settings(max_examples=50)
def test_website_associationkey_instantiation(instance):
    assert isinstance(instance, website_AssociationKey)



@given(instance=website_AssociationKey_strategy)
def test_website_associationkey_targetColumnName_setter(instance):
    original = instance.targetColumnName
    instance.targetColumnName = original
    assert instance.targetColumnName == original

@given(instance=Association_strategy)
@settings(max_examples=50)
def test_association_instantiation(instance):
    assert isinstance(instance, Association)

@given(instance=website_LocationAttribute_strategy)
@settings(max_examples=50)
def test_website_locationattribute_instantiation(instance):
    assert isinstance(instance, website_LocationAttribute)

@given(instance=ResourceAttribute_strategy)
@settings(max_examples=50)
def test_resourceattribute_instantiation(instance):
    assert isinstance(instance, ResourceAttribute)

@given(instance=website_ImageAttribute_strategy)
@settings(max_examples=50)
def test_website_imageattribute_instantiation(instance):
    assert isinstance(instance, website_ImageAttribute)

@given(instance=website_FileAttribute_strategy)
@settings(max_examples=50)
def test_website_fileattribute_instantiation(instance):
    assert isinstance(instance, website_FileAttribute)

@given(instance=EntityOrView_strategy)
@settings(max_examples=50)
def test_entityorview_instantiation(instance):
    assert isinstance(instance, EntityOrView)

@given(instance=website_View_strategy)
@settings(max_examples=50)
def test_website_view_instantiation(instance):
    assert isinstance(instance, website_View)

@given(instance=website_Entity_strategy)
@settings(max_examples=50)
def test_website_entity_instantiation(instance):
    assert isinstance(instance, website_Entity)

@given(instance=website_EntityAssociation_strategy)
@settings(max_examples=50)
def test_website_entityassociation_instantiation(instance):
    assert isinstance(instance, website_EntityAssociation)



@given(instance=website_EntityAssociation_strategy)
def test_website_entityassociation_targetDisplayClass_setter(instance):
    original = instance.targetDisplayClass
    instance.targetDisplayClass = original
    assert instance.targetDisplayClass == original



@given(instance=website_EntityAssociation_strategy)
def test_website_entityassociation_targetInputClass_setter(instance):
    original = instance.targetInputClass
    instance.targetInputClass = original
    assert instance.targetInputClass == original



@given(instance=website_EntityAssociation_strategy)
def test_website_entityassociation_targetPrimaryKey_setter(instance):
    original = instance.targetPrimaryKey
    instance.targetPrimaryKey = original
    assert instance.targetPrimaryKey == original



@given(instance=website_EntityAssociation_strategy)
def test_website_entityassociation_pivotTableName_setter(instance):
    original = instance.pivotTableName
    instance.pivotTableName = original
    assert instance.pivotTableName == original



@given(instance=website_EntityAssociation_strategy)
def test_website_entityassociation_targetFooterClass_setter(instance):
    original = instance.targetFooterClass
    instance.targetFooterClass = original
    assert instance.targetFooterClass == original



@given(instance=website_EntityAssociation_strategy)
def test_website_entityassociation_targetDisplayLabel_setter(instance):
    original = instance.targetDisplayLabel
    instance.targetDisplayLabel = original
    assert instance.targetDisplayLabel == original



@given(instance=website_EntityAssociation_strategy)
def test_website_entityassociation_targetHeaderClass_setter(instance):
    original = instance.targetHeaderClass
    instance.targetHeaderClass = original
    assert instance.targetHeaderClass == original



@given(instance=website_EntityAssociation_strategy)
def test_website_entityassociation_bidirectional_setter(instance):
    original = instance.bidirectional
    instance.bidirectional = original
    assert instance.bidirectional == original



@given(instance=website_EntityAssociation_strategy)
def test_website_entityassociation_targetFeatureName_setter(instance):
    original = instance.targetFeatureName
    instance.targetFeatureName = original
    assert instance.targetFeatureName == original

@given(instance=ModelLabelFeature_strategy)
@settings(max_examples=50)
def test_modellabelfeature_instantiation(instance):
    assert isinstance(instance, ModelLabelFeature)

@given(instance=website_ModelLabelAssociation_strategy)
@settings(max_examples=50)
def test_website_modellabelassociation_instantiation(instance):
    assert isinstance(instance, website_ModelLabelAssociation)



@given(instance=website_ModelLabelAssociation_strategy)
def test_website_modellabelassociation_isSourceAssociation_setter(instance):
    original = instance.isSourceAssociation
    instance.isSourceAssociation = original
    assert instance.isSourceAssociation == original

@given(instance=website_ModelLabelAttribute_strategy)
@settings(max_examples=50)
def test_website_modellabelattribute_instantiation(instance):
    assert isinstance(instance, website_ModelLabelAttribute)



@given(instance=website_ModelLabelAttribute_strategy)
def test_website_modellabelattribute_dateFormat_setter(instance):
    original = instance.dateFormat
    instance.dateFormat = original
    assert instance.dateFormat == original

@given(instance=website_ModelLabelFeature_strategy)
@settings(max_examples=50)
def test_website_modellabelfeature_instantiation(instance):
    assert isinstance(instance, website_ModelLabelFeature)

@given(instance=website_Label_strategy)
@settings(max_examples=50)
def test_website_label_instantiation(instance):
    assert isinstance(instance, website_Label)

@given(instance=website_EntityAttribute_strategy)
@settings(max_examples=50)
def test_website_entityattribute_instantiation(instance):
    assert isinstance(instance, website_EntityAttribute)



@given(instance=website_EntityAttribute_strategy)
def test_website_entityattribute_persistentType_setter(instance):
    original = instance.persistentType
    instance.persistentType = original
    assert instance.persistentType == original



@given(instance=website_EntityAttribute_strategy)
def test_website_entityattribute_interfaceType_setter(instance):
    original = instance.interfaceType
    instance.interfaceType = original
    assert instance.interfaceType == original



@given(instance=website_EntityAttribute_strategy)
def test_website_entityattribute_containerUnique_setter(instance):
    original = instance.containerUnique
    instance.containerUnique = original
    assert instance.containerUnique == original



@given(instance=website_EntityAttribute_strategy)
def test_website_entityattribute_primaryKey_setter(instance):
    original = instance.primaryKey
    instance.primaryKey = original
    assert instance.primaryKey == original



@given(instance=website_EntityAttribute_strategy)
def test_website_entityattribute_ormType_setter(instance):
    original = instance.ormType
    instance.ormType = original
    assert instance.ormType == original

@given(instance=website_Expression_strategy)
@settings(max_examples=50)
def test_website_expression_instantiation(instance):
    assert isinstance(instance, website_Expression)

@given(instance=Label_strategy)
@settings(max_examples=50)
def test_label_instantiation(instance):
    assert isinstance(instance, Label)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=website_ViewFeature_strategy)
@settings(max_examples=50)
def test_website_viewfeature_instantiation(instance):
    assert isinstance(instance, website_ViewFeature)

@given(instance=website_Association_strategy)
@settings(max_examples=50)
def test_website_association_instantiation(instance):
    assert isinstance(instance, website_Association)



@given(instance=website_Association_strategy)
def test_website_association_pseudo_setter(instance):
    original = instance.pseudo
    instance.pseudo = original
    assert instance.pseudo == original



@given(instance=website_Association_strategy)
def test_website_association_inputClass_setter(instance):
    original = instance.inputClass
    instance.inputClass = original
    assert instance.inputClass == original



@given(instance=website_Association_strategy)
def test_website_association_serializationMaxDepth_setter(instance):
    original = instance.serializationMaxDepth
    instance.serializationMaxDepth = original
    assert instance.serializationMaxDepth == original

@given(instance=website_EncapsulatedAssociation_strategy)
@settings(max_examples=50)
def test_website_encapsulatedassociation_instantiation(instance):
    assert isinstance(instance, website_EncapsulatedAssociation)



@given(instance=website_EncapsulatedAssociation_strategy)
def test_website_encapsulatedassociation_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original



@given(instance=website_EncapsulatedAssociation_strategy)
def test_website_encapsulatedassociation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=website_EncapsulatedAssociation_strategy)
def test_website_encapsulatedassociation_isSourceAssociation_setter(instance):
    original = instance.isSourceAssociation
    instance.isSourceAssociation = original
    assert instance.isSourceAssociation == original

@given(instance=website_Feature_strategy)
@settings(max_examples=50)
def test_website_feature_instantiation(instance):
    assert isinstance(instance, website_Feature)



@given(instance=website_Feature_strategy)
def test_website_feature_serializationExpose_setter(instance):
    original = instance.serializationExpose
    instance.serializationExpose = original
    assert instance.serializationExpose == original



@given(instance=website_Feature_strategy)
def test_website_feature_displayClass_setter(instance):
    original = instance.displayClass
    instance.displayClass = original
    assert instance.displayClass == original



@given(instance=website_Feature_strategy)
def test_website_feature_collectionAllowAdd_setter(instance):
    original = instance.collectionAllowAdd
    instance.collectionAllowAdd = original
    assert instance.collectionAllowAdd == original



@given(instance=website_Feature_strategy)
def test_website_feature_encodeUriKey_setter(instance):
    original = instance.encodeUriKey
    instance.encodeUriKey = original
    assert instance.encodeUriKey == original



@given(instance=website_Feature_strategy)
def test_website_feature_nullDisplayValue_setter(instance):
    original = instance.nullDisplayValue
    instance.nullDisplayValue = original
    assert instance.nullDisplayValue == original



@given(instance=website_Feature_strategy)
def test_website_feature_serializationGroups_setter(instance):
    original = instance.serializationGroups
    instance.serializationGroups = original
    assert instance.serializationGroups == original



@given(instance=website_Feature_strategy)
def test_website_feature_headerClass_setter(instance):
    original = instance.headerClass
    instance.headerClass = original
    assert instance.headerClass == original



@given(instance=website_Feature_strategy)
def test_website_feature_footerClass_setter(instance):
    original = instance.footerClass
    instance.footerClass = original
    assert instance.footerClass == original



@given(instance=website_Feature_strategy)
def test_website_feature_collectionAllowRemove_setter(instance):
    original = instance.collectionAllowRemove
    instance.collectionAllowRemove = original
    assert instance.collectionAllowRemove == original



@given(instance=website_Feature_strategy)
def test_website_feature_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=website_EnumerationType_strategy)
@settings(max_examples=50)
def test_website_enumerationtype_instantiation(instance):
    assert isinstance(instance, website_EnumerationType)

@given(instance=website_NamedElement_strategy)
@settings(max_examples=50)
def test_website_namedelement_instantiation(instance):
    assert isinstance(instance, website_NamedElement)



@given(instance=website_NamedElement_strategy)
def test_website_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=website_ForgottenPasswordUnit_strategy)
@settings(max_examples=50)
def test_website_forgottenpasswordunit_instantiation(instance):
    assert isinstance(instance, website_ForgottenPasswordUnit)



@given(instance=website_ForgottenPasswordUnit_strategy)
def test_website_forgottenpasswordunit_styleClass_setter(instance):
    original = instance.styleClass
    instance.styleClass = original
    assert instance.styleClass == original

@given(instance=website_LoginUnit_strategy)
@settings(max_examples=50)
def test_website_loginunit_instantiation(instance):
    assert isinstance(instance, website_LoginUnit)



@given(instance=website_LoginUnit_strategy)
def test_website_loginunit_styleClass_setter(instance):
    original = instance.styleClass
    instance.styleClass = original
    assert instance.styleClass == original



@given(instance=website_LoginUnit_strategy)
def test_website_loginunit_logoutUriElement_setter(instance):
    original = instance.logoutUriElement
    instance.logoutUriElement = original
    assert instance.logoutUriElement == original

@given(instance=website_RegistrationUnit_strategy)
@settings(max_examples=50)
def test_website_registrationunit_instantiation(instance):
    assert isinstance(instance, website_RegistrationUnit)



@given(instance=website_RegistrationUnit_strategy)
def test_website_registrationunit_styleClass_setter(instance):
    original = instance.styleClass
    instance.styleClass = original
    assert instance.styleClass == original

@given(instance=Authentication_strategy)
@settings(max_examples=50)
def test_authentication_instantiation(instance):
    assert isinstance(instance, Authentication)

@given(instance=website_CasAuthentication_strategy)
@settings(max_examples=50)
def test_website_casauthentication_instantiation(instance):
    assert isinstance(instance, website_CasAuthentication)

@given(instance=website_LocalAuthenticationSystem_strategy)
@settings(max_examples=50)
def test_website_localauthenticationsystem_instantiation(instance):
    assert isinstance(instance, website_LocalAuthenticationSystem)



@given(instance=website_LocalAuthenticationSystem_strategy)
def test_website_localauthenticationsystem_authenticationKey_setter(instance):
    original = instance.authenticationKey
    instance.authenticationKey = original
    assert instance.authenticationKey == original



@given(instance=website_LocalAuthenticationSystem_strategy)
def test_website_localauthenticationsystem_sendWelcomeEmail_setter(instance):
    original = instance.sendWelcomeEmail
    instance.sendWelcomeEmail = original
    assert instance.sendWelcomeEmail == original



@given(instance=website_LocalAuthenticationSystem_strategy)
def test_website_localauthenticationsystem_allowRememberMe_setter(instance):
    original = instance.allowRememberMe
    instance.allowRememberMe = original
    assert instance.allowRememberMe == original



@given(instance=website_LocalAuthenticationSystem_strategy)
def test_website_localauthenticationsystem_useCaptcha_setter(instance):
    original = instance.useCaptcha
    instance.useCaptcha = original
    assert instance.useCaptcha == original



@given(instance=website_LocalAuthenticationSystem_strategy)
def test_website_localauthenticationsystem_trackLoginAttempts_setter(instance):
    original = instance.trackLoginAttempts
    instance.trackLoginAttempts = original
    assert instance.trackLoginAttempts == original



@given(instance=website_LocalAuthenticationSystem_strategy)
def test_website_localauthenticationsystem_useEmailActivation_setter(instance):
    original = instance.useEmailActivation
    instance.useEmailActivation = original
    assert instance.useEmailActivation == original



@given(instance=website_LocalAuthenticationSystem_strategy)
def test_website_localauthenticationsystem_allowSelfRegistration_setter(instance):
    original = instance.allowSelfRegistration
    instance.allowSelfRegistration = original
    assert instance.allowSelfRegistration == original

@given(instance=website_Attribute_strategy)
@settings(max_examples=50)
def test_website_attribute_instantiation(instance):
    assert isinstance(instance, website_Attribute)



@given(instance=website_Attribute_strategy)
def test_website_attribute_inputClass_setter(instance):
    original = instance.inputClass
    instance.inputClass = original
    assert instance.inputClass == original



@given(instance=website_Attribute_strategy)
def test_website_attribute_placeholder_setter(instance):
    original = instance.placeholder
    instance.placeholder = original
    assert instance.placeholder == original



@given(instance=website_Attribute_strategy)
def test_website_attribute_validationPattern_setter(instance):
    original = instance.validationPattern
    instance.validationPattern = original
    assert instance.validationPattern == original

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=website_DataType_strategy)
@settings(max_examples=50)
def test_website_datatype_instantiation(instance):
    assert isinstance(instance, website_DataType)



@given(instance=website_DataType_strategy)
def test_website_datatype_interfaceType_setter(instance):
    original = instance.interfaceType
    instance.interfaceType = original
    assert instance.interfaceType == original



@given(instance=website_DataType_strategy)
def test_website_datatype_persistentType_setter(instance):
    original = instance.persistentType
    instance.persistentType = original
    assert instance.persistentType == original



@given(instance=website_DataType_strategy)
def test_website_datatype_placeholder_setter(instance):
    original = instance.placeholder
    instance.placeholder = original
    assert instance.placeholder == original



@given(instance=website_DataType_strategy)
def test_website_datatype_ormType_setter(instance):
    original = instance.ormType
    instance.ormType = original
    assert instance.ormType == original



@given(instance=website_DataType_strategy)
def test_website_datatype_validationPattern_setter(instance):
    original = instance.validationPattern
    instance.validationPattern = original
    assert instance.validationPattern == original

@given(instance=NamedDisplayElement_strategy)
@settings(max_examples=50)
def test_nameddisplayelement_instantiation(instance):
    assert isinstance(instance, NamedDisplayElement)

@given(instance=website_ContentUnit_strategy)
@settings(max_examples=50)
def test_website_contentunit_instantiation(instance):
    assert isinstance(instance, website_ContentUnit)



@given(instance=website_ContentUnit_strategy)
def test_website_contentunit_alternative_setter(instance):
    original = instance.alternative
    instance.alternative = original
    assert instance.alternative == original



@given(instance=website_ContentUnit_strategy)
def test_website_contentunit_requiresRole_setter(instance):
    original = instance.requiresRole
    instance.requiresRole = original
    assert instance.requiresRole == original



@given(instance=website_ContentUnit_strategy)
def test_website_contentunit_purposeSummary_setter(instance):
    original = instance.purposeSummary
    instance.purposeSummary = original
    assert instance.purposeSummary == original



@given(instance=website_ContentUnit_strategy)
def test_website_contentunit_uriElement_setter(instance):
    original = instance.uriElement
    instance.uriElement = original
    assert instance.uriElement == original



@given(instance=website_ContentUnit_strategy)
def test_website_contentunit_captionClass_setter(instance):
    original = instance.captionClass
    instance.captionClass = original
    assert instance.captionClass == original



@given(instance=website_ContentUnit_strategy)
def test_website_contentunit_omitCaption_setter(instance):
    original = instance.omitCaption
    instance.omitCaption = original
    assert instance.omitCaption == original



@given(instance=website_ContentUnit_strategy)
def test_website_contentunit_createDefaultUriElement_setter(instance):
    original = instance.createDefaultUriElement
    instance.createDefaultUriElement = original
    assert instance.createDefaultUriElement == original

@given(instance=website_InterfaceField_strategy)
@settings(max_examples=50)
def test_website_interfacefield_instantiation(instance):
    assert isinstance(instance, website_InterfaceField)



@given(instance=website_InterfaceField_strategy)
def test_website_interfacefield_inputClass_setter(instance):
    original = instance.inputClass
    instance.inputClass = original
    assert instance.inputClass == original



@given(instance=website_InterfaceField_strategy)
def test_website_interfacefield_required_setter(instance):
    original = instance.required
    instance.required = original
    assert instance.required == original



@given(instance=website_InterfaceField_strategy)
def test_website_interfacefield_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original



@given(instance=website_InterfaceField_strategy)
def test_website_interfacefield_validationPattern_setter(instance):
    original = instance.validationPattern
    instance.validationPattern = original
    assert instance.validationPattern == original



@given(instance=website_InterfaceField_strategy)
def test_website_interfacefield_placeholder_setter(instance):
    original = instance.placeholder
    instance.placeholder = original
    assert instance.placeholder == original

@given(instance=website_EditStaticTextMenuEntry_strategy)
@settings(max_examples=50)
def test_website_editstatictextmenuentry_instantiation(instance):
    assert isinstance(instance, website_EditStaticTextMenuEntry)

@given(instance=website_EntityFeature_strategy)
@settings(max_examples=50)
def test_website_entityfeature_instantiation(instance):
    assert isinstance(instance, website_EntityFeature)



@given(instance=website_EntityFeature_strategy)
def test_website_entityfeature_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original



@given(instance=website_EntityFeature_strategy)
def test_website_entityfeature_singletonName_setter(instance):
    original = instance.singletonName
    instance.singletonName = original
    assert instance.singletonName == original



@given(instance=website_EntityFeature_strategy)
def test_website_entityfeature_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original



@given(instance=website_EntityFeature_strategy)
def test_website_entityfeature_pluralisedName_setter(instance):
    original = instance.pluralisedName
    instance.pluralisedName = original
    assert instance.pluralisedName == original



@given(instance=website_EntityFeature_strategy)
def test_website_entityfeature_ordered_setter(instance):
    original = instance.ordered
    instance.ordered = original
    assert instance.ordered == original



@given(instance=website_EntityFeature_strategy)
def test_website_entityfeature_booleanIsHasChoice_setter(instance):
    original = instance.booleanIsHasChoice
    instance.booleanIsHasChoice = original
    assert instance.booleanIsHasChoice == original



@given(instance=website_EntityFeature_strategy)
def test_website_entityfeature_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original

@given(instance=website_InlineAction_strategy)
@settings(max_examples=50)
def test_website_inlineaction_instantiation(instance):
    assert isinstance(instance, website_InlineAction)



@given(instance=website_InlineAction_strategy)
def test_website_inlineaction_header_setter(instance):
    original = instance.header
    instance.header = original
    assert instance.header == original



@given(instance=website_InlineAction_strategy)
def test_website_inlineaction_headerClass_setter(instance):
    original = instance.headerClass
    instance.headerClass = original
    assert instance.headerClass == original



@given(instance=website_InlineAction_strategy)
def test_website_inlineaction_footer_setter(instance):
    original = instance.footer
    instance.footer = original
    assert instance.footer == original



@given(instance=website_InlineAction_strategy)
def test_website_inlineaction_footerClass_setter(instance):
    original = instance.footerClass
    instance.footerClass = original
    assert instance.footerClass == original



@given(instance=website_InlineAction_strategy)
def test_website_inlineaction_disable_setter(instance):
    original = instance.disable
    instance.disable = original
    assert instance.disable == original



@given(instance=website_InlineAction_strategy)
def test_website_inlineaction_requiresRole_setter(instance):
    original = instance.requiresRole
    instance.requiresRole = original
    assert instance.requiresRole == original

@given(instance=website_EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_website_enumerationliteral_instantiation(instance):
    assert isinstance(instance, website_EnumerationLiteral)

@given(instance=website_Filter_strategy)
@settings(max_examples=50)
def test_website_filter_instantiation(instance):
    assert isinstance(instance, website_Filter)

@given(instance=website_ActionMenuEntry_strategy)
@settings(max_examples=50)
def test_website_actionmenuentry_instantiation(instance):
    assert isinstance(instance, website_ActionMenuEntry)

@given(instance=website_ViewAssociation_strategy)
@settings(max_examples=50)
def test_website_viewassociation_instantiation(instance):
    assert isinstance(instance, website_ViewAssociation)



@given(instance=website_ViewAssociation_strategy)
def test_website_viewassociation_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original

@given(instance=website_UnitSupportAction_strategy)
@settings(max_examples=50)
def test_website_unitsupportaction_instantiation(instance):
    assert isinstance(instance, website_UnitSupportAction)



@given(instance=website_UnitSupportAction_strategy)
def test_website_unitsupportaction_confirmMessage_setter(instance):
    original = instance.confirmMessage
    instance.confirmMessage = original
    assert instance.confirmMessage == original



@given(instance=website_UnitSupportAction_strategy)
def test_website_unitsupportaction_disable_setter(instance):
    original = instance.disable
    instance.disable = original
    assert instance.disable == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=website_FilterParameter_strategy)
@settings(max_examples=50)
def test_website_filterparameter_instantiation(instance):
    assert isinstance(instance, website_FilterParameter)



@given(instance=website_FilterParameter_strategy)
def test_website_filterparameter_placeholder_setter(instance):
    original = instance.placeholder
    instance.placeholder = original
    assert instance.placeholder == original



@given(instance=website_FilterParameter_strategy)
def test_website_filterparameter_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original

@given(instance=website_Selection_strategy)
@settings(max_examples=50)
def test_website_selection_instantiation(instance):
    assert isinstance(instance, website_Selection)



@given(instance=website_Selection_strategy)
def test_website_selection_limit_setter(instance):
    original = instance.limit
    instance.limit = original
    assert instance.limit == original



@given(instance=website_Selection_strategy)
def test_website_selection_distinct_setter(instance):
    original = instance.distinct
    instance.distinct = original
    assert instance.distinct == original



@given(instance=website_Selection_strategy)
def test_website_selection_selected_setter(instance):
    original = instance.selected
    instance.selected = original
    assert instance.selected == original

@given(instance=website_BusinessOperation_strategy)
@settings(max_examples=50)
def test_website_businessoperation_instantiation(instance):
    assert isinstance(instance, website_BusinessOperation)



@given(instance=website_BusinessOperation_strategy)
def test_website_businessoperation_resultType_setter(instance):
    original = instance.resultType
    instance.resultType = original
    assert instance.resultType == original



@given(instance=website_BusinessOperation_strategy)
def test_website_businessoperation_resultMimeType_setter(instance):
    original = instance.resultMimeType
    instance.resultMimeType = original
    assert instance.resultMimeType == original

@given(instance=website_SelectionParameter_strategy)
@settings(max_examples=50)
def test_website_selectionparameter_instantiation(instance):
    assert isinstance(instance, website_SelectionParameter)



@given(instance=website_SelectionParameter_strategy)
def test_website_selectionparameter_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original



@given(instance=website_SelectionParameter_strategy)
def test_website_selectionparameter_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original

@given(instance=website_ModelLabel_strategy)
@settings(max_examples=50)
def test_website_modellabel_instantiation(instance):
    assert isinstance(instance, website_ModelLabel)



@given(instance=website_ModelLabel_strategy)
def test_website_modellabel_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original

@given(instance=website_NamedDisplayElement_strategy)
@settings(max_examples=50)
def test_website_nameddisplayelement_instantiation(instance):
    assert isinstance(instance, website_NamedDisplayElement)



@given(instance=website_NamedDisplayElement_strategy)
def test_website_nameddisplayelement_displayLabel_setter(instance):
    original = instance.displayLabel
    instance.displayLabel = original
    assert instance.displayLabel == original

@given(instance=website_Authentication_strategy)
@settings(max_examples=50)
def test_website_authentication_instantiation(instance):
    assert isinstance(instance, website_Authentication)



@given(instance=website_Authentication_strategy)
def test_website_authentication_loginLabel_setter(instance):
    original = instance.loginLabel
    instance.loginLabel = original
    assert instance.loginLabel == original



@given(instance=website_Authentication_strategy)
def test_website_authentication_logoutLabel_setter(instance):
    original = instance.logoutLabel
    instance.logoutLabel = original
    assert instance.logoutLabel == original

@given(instance=website_ImageManipulation_strategy)
@settings(max_examples=50)
def test_website_imagemanipulation_instantiation(instance):
    assert isinstance(instance, website_ImageManipulation)



@given(instance=website_ImageManipulation_strategy)
def test_website_imagemanipulation_jpegQuality_setter(instance):
    original = instance.jpegQuality
    instance.jpegQuality = original
    assert instance.jpegQuality == original

@given(instance=website_EntityOrView_strategy)
@settings(max_examples=50)
def test_website_entityorview_instantiation(instance):
    assert isinstance(instance, website_EntityOrView)



@given(instance=website_EntityOrView_strategy)
def test_website_entityorview_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original



@given(instance=website_EntityOrView_strategy)
def test_website_entityorview_serializationExcludeAll_setter(instance):
    original = instance.serializationExcludeAll
    instance.serializationExcludeAll = original
    assert instance.serializationExcludeAll == original



@given(instance=website_EntityOrView_strategy)
def test_website_entityorview_pluralisedName_setter(instance):
    original = instance.pluralisedName
    instance.pluralisedName = original
    assert instance.pluralisedName == original



@given(instance=website_EntityOrView_strategy)
def test_website_entityorview_implementsUserInterface_setter(instance):
    original = instance.implementsUserInterface
    instance.implementsUserInterface = original
    assert instance.implementsUserInterface == original



@given(instance=website_EntityOrView_strategy)
def test_website_entityorview_autoKeyName_setter(instance):
    original = instance.autoKeyName
    instance.autoKeyName = original
    assert instance.autoKeyName == original



@given(instance=website_EntityOrView_strategy)
def test_website_entityorview_autoKeyPersistentType_setter(instance):
    original = instance.autoKeyPersistentType
    instance.autoKeyPersistentType = original
    assert instance.autoKeyPersistentType == original



@given(instance=website_EntityOrView_strategy)
def test_website_entityorview_autoKeyGenerationStrategy_setter(instance):
    original = instance.autoKeyGenerationStrategy
    instance.autoKeyGenerationStrategy = original
    assert instance.autoKeyGenerationStrategy == original



@given(instance=website_EntityOrView_strategy)
def test_website_entityorview_singletonName_setter(instance):
    original = instance.singletonName
    instance.singletonName = original
    assert instance.singletonName == original

@given(instance=website_Menu_strategy)
@settings(max_examples=50)
def test_website_menu_instantiation(instance):
    assert isinstance(instance, website_Menu)



@given(instance=website_Menu_strategy)
def test_website_menu_captionClass_setter(instance):
    original = instance.captionClass
    instance.captionClass = original
    assert instance.captionClass == original



@given(instance=website_Menu_strategy)
def test_website_menu_styleClass_setter(instance):
    original = instance.styleClass
    instance.styleClass = original
    assert instance.styleClass == original



@given(instance=website_Menu_strategy)
def test_website_menu_layoutClass_setter(instance):
    original = instance.layoutClass
    instance.layoutClass = original
    assert instance.layoutClass == original



@given(instance=website_Menu_strategy)
def test_website_menu_omitCaption_setter(instance):
    original = instance.omitCaption
    instance.omitCaption = original
    assert instance.omitCaption == original

@given(instance=website_Page_strategy)
@settings(max_examples=50)
def test_website_page_instantiation(instance):
    assert isinstance(instance, website_Page)



@given(instance=website_Page_strategy)
def test_website_page_authenticated_setter(instance):
    original = instance.authenticated
    instance.authenticated = original
    assert instance.authenticated == original



@given(instance=website_Page_strategy)
def test_website_page_topMenuOption_setter(instance):
    original = instance.topMenuOption
    instance.topMenuOption = original
    assert instance.topMenuOption == original



@given(instance=website_Page_strategy)
def test_website_page_styleClass_setter(instance):
    original = instance.styleClass
    instance.styleClass = original
    assert instance.styleClass == original



@given(instance=website_Page_strategy)
def test_website_page_uriElement_setter(instance):
    original = instance.uriElement
    instance.uriElement = original
    assert instance.uriElement == original



@given(instance=website_Page_strategy)
def test_website_page_navigationLabel_setter(instance):
    original = instance.navigationLabel
    instance.navigationLabel = original
    assert instance.navigationLabel == original



@given(instance=website_Page_strategy)
def test_website_page_topMenuRank_setter(instance):
    original = instance.topMenuRank
    instance.topMenuRank = original
    assert instance.topMenuRank == original

@given(instance=website_Service_strategy)
@settings(max_examples=50)
def test_website_service_instantiation(instance):
    assert isinstance(instance, website_Service)

@given(instance=website_Classifier_strategy)
@settings(max_examples=50)
def test_website_classifier_instantiation(instance):
    assert isinstance(instance, website_Classifier)

@given(instance=website_WebsiteProperties_strategy)
@settings(max_examples=50)
def test_website_websiteproperties_instantiation(instance):
    assert isinstance(instance, website_WebsiteProperties)



@given(instance=website_WebsiteProperties_strategy)
def test_website_websiteproperties_staticUnitsEditable_setter(instance):
    original = instance.staticUnitsEditable
    instance.staticUnitsEditable = original
    assert instance.staticUnitsEditable == original



@given(instance=website_WebsiteProperties_strategy)
def test_website_websiteproperties_databasePrefix_setter(instance):
    original = instance.databasePrefix
    instance.databasePrefix = original
    assert instance.databasePrefix == original



@given(instance=website_WebsiteProperties_strategy)
def test_website_websiteproperties_inputTechnology_setter(instance):
    original = instance.inputTechnology
    instance.inputTechnology = original
    assert instance.inputTechnology == original



@given(instance=website_WebsiteProperties_strategy)
def test_website_websiteproperties_rewriteURLs_setter(instance):
    original = instance.rewriteURLs
    instance.rewriteURLs = original
    assert instance.rewriteURLs == original



@given(instance=website_WebsiteProperties_strategy)
def test_website_websiteproperties_frameworkTechnology_setter(instance):
    original = instance.frameworkTechnology
    instance.frameworkTechnology = original
    assert instance.frameworkTechnology == original



@given(instance=website_WebsiteProperties_strategy)
def test_website_websiteproperties_databaseTechnology_setter(instance):
    original = instance.databaseTechnology
    instance.databaseTechnology = original
    assert instance.databaseTechnology == original



@given(instance=website_WebsiteProperties_strategy)
def test_website_websiteproperties_ormTechnology_setter(instance):
    original = instance.ormTechnology
    instance.ormTechnology = original
    assert instance.ormTechnology == original



@given(instance=website_WebsiteProperties_strategy)
def test_website_websiteproperties_topNavigationId_setter(instance):
    original = instance.topNavigationId
    instance.topNavigationId = original
    assert instance.topNavigationId == original



@given(instance=website_WebsiteProperties_strategy)
def test_website_websiteproperties_siteTemplate_setter(instance):
    original = instance.siteTemplate
    instance.siteTemplate = original
    assert instance.siteTemplate == original



@given(instance=website_WebsiteProperties_strategy)
def test_website_websiteproperties_projectName_setter(instance):
    original = instance.projectName
    instance.projectName = original
    assert instance.projectName == original



@given(instance=website_WebsiteProperties_strategy)
def test_website_websiteproperties_metaDescription_setter(instance):
    original = instance.metaDescription
    instance.metaDescription = original
    assert instance.metaDescription == original



@given(instance=website_WebsiteProperties_strategy)
def test_website_websiteproperties_defaultTimeFormat_setter(instance):
    original = instance.defaultTimeFormat
    instance.defaultTimeFormat = original
    assert instance.defaultTimeFormat == original



@given(instance=website_WebsiteProperties_strategy)
def test_website_websiteproperties_captchaSecretKey_setter(instance):
    original = instance.captchaSecretKey
    instance.captchaSecretKey = original
    assert instance.captchaSecretKey == original



@given(instance=website_WebsiteProperties_strategy)
def test_website_websiteproperties_databaseHost_setter(instance):
    original = instance.databaseHost
    instance.databaseHost = original
    assert instance.databaseHost == original



@given(instance=website_WebsiteProperties_strategy)
def test_website_websiteproperties_databaseName_setter(instance):
    original = instance.databaseName
    instance.databaseName = original
    assert instance.databaseName == original



@given(instance=website_WebsiteProperties_strategy)
def test_website_websiteproperties_timestampCreation_setter(instance):
    original = instance.timestampCreation
    instance.timestampCreation = original
    assert instance.timestampCreation == original



@given(instance=website_WebsiteProperties_strategy)
def test_website_websiteproperties_responsiveTopMenu_setter(instance):
    original = instance.responsiveTopMenu
    instance.responsiveTopMenu = original
    assert instance.responsiveTopMenu == original



@given(instance=website_WebsiteProperties_strategy)
def test_website_websiteproperties_textEditorURL_setter(instance):
    original = instance.textEditorURL
    instance.textEditorURL = original
    assert instance.textEditorURL == original



@given(instance=website_WebsiteProperties_strategy)
def test_website_websiteproperties_captchaSiteKey_setter(instance):
    original = instance.captchaSiteKey
    instance.captchaSiteKey = original
    assert instance.captchaSiteKey == original



@given(instance=website_WebsiteProperties_strategy)
def test_website_websiteproperties_defaultMaximumUploadSize_setter(instance):
    original = instance.defaultMaximumUploadSize
    instance.defaultMaximumUploadSize = original
    assert instance.defaultMaximumUploadSize == original



@given(instance=website_WebsiteProperties_strategy)
def test_website_websiteproperties_webmasterEmail_setter(instance):
    original = instance.webmasterEmail
    instance.webmasterEmail = original
    assert instance.webmasterEmail == original



@given(instance=website_WebsiteProperties_strategy)
def test_website_websiteproperties_defaultDateTimeFormat_setter(instance):
    original = instance.defaultDateTimeFormat
    instance.defaultDateTimeFormat = original
    assert instance.defaultDateTimeFormat == original



@given(instance=website_WebsiteProperties_strategy)
def test_website_websiteproperties_databasePassword_setter(instance):
    original = instance.databasePassword
    instance.databasePassword = original
    assert instance.databasePassword == original



@given(instance=website_WebsiteProperties_strategy)
def test_website_websiteproperties_databaseUsername_setter(instance):
    original = instance.databaseUsername
    instance.databaseUsername = original
    assert instance.databaseUsername == original



@given(instance=website_WebsiteProperties_strategy)
def test_website_websiteproperties_ajaxTechnology_setter(instance):
    original = instance.ajaxTechnology
    instance.ajaxTechnology = original
    assert instance.ajaxTechnology == original



@given(instance=website_WebsiteProperties_strategy)
def test_website_websiteproperties_defaultDateFormat_setter(instance):
    original = instance.defaultDateFormat
    instance.defaultDateFormat = original
    assert instance.defaultDateFormat == original



@given(instance=website_WebsiteProperties_strategy)
def test_website_websiteproperties_developmentVersion_setter(instance):
    original = instance.developmentVersion
    instance.developmentVersion = original
    assert instance.developmentVersion == original



@given(instance=website_WebsiteProperties_strategy)
def test_website_websiteproperties_copyrightText_setter(instance):
    original = instance.copyrightText
    instance.copyrightText = original
    assert instance.copyrightText == original



@given(instance=website_WebsiteProperties_strategy)
def test_website_websiteproperties_baseURL_setter(instance):
    original = instance.baseURL
    instance.baseURL = original
    assert instance.baseURL == original



@given(instance=website_WebsiteProperties_strategy)
def test_website_websiteproperties_testProjectName_setter(instance):
    original = instance.testProjectName
    instance.testProjectName = original
    assert instance.testProjectName == original



@given(instance=website_WebsiteProperties_strategy)
def test_website_websiteproperties_databasePort_setter(instance):
    original = instance.databasePort
    instance.databasePort = original
    assert instance.databasePort == original



@given(instance=website_WebsiteProperties_strategy)
def test_website_websiteproperties_timestampUpdates_setter(instance):
    original = instance.timestampUpdates
    instance.timestampUpdates = original
    assert instance.timestampUpdates == original



@given(instance=website_WebsiteProperties_strategy)
def test_website_websiteproperties_siteTitle_setter(instance):
    original = instance.siteTitle
    instance.siteTitle = original
    assert instance.siteTitle == original

@given(instance=website_WebGenModel_strategy)
@settings(max_examples=50)
def test_website_webgenmodel_instantiation(instance):
    assert isinstance(instance, website_WebGenModel)
