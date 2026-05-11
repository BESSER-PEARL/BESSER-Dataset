import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Path,
    website::RouteParameterReference,
    website::FeatureReference,
    website::CurrentUserReference,
    website::ModelReference,
    website::ParameterReference,
    website::InlineActionContainer,
    AuthenticationUnit,
    website::AuthenticationUnit,
    EntityAttribute,
    website::DataTypeAttribute,
    Attribute,
    EntityFeature,
    website::AssociationKey,
    Association,
    website::LocationAttribute,
    ResourceAttribute,
    website::ImageAttribute,
    website::FileAttribute,
    EntityOrView,
    website::Entity,
    website::EntityAssociation,
    ModelLabelFeature,
    website::ModelLabelAssociation,
    website::ModelLabelAttribute,
    website::ModelLabelFeature,
    website::Label,
    website::EntityAttribute,
    website::Expression,
    Label,
    Feature,
    website::Association,
    website::Feature,
    DataType,
    website::EnumerationType,
    website::NamedElement,
    Authentication,
    website::CasAuthentication,
    website::LocalAuthenticationSystem,
    website::Attribute,
    Classifier,
    website::DataType,
    NamedDisplayElement,
    website::InlineAction,
    website::EnumerationLiteral,
    website::EntityFeature,
    NamedElement,
    website::ModelLabel,
    website::NamedDisplayElement,
    website::Authentication,
    website::ImageManipulation,
    website::EntityOrView,
    website::Menu,
    website::Service,
    website::Classifier,
    website::WebsiteProperties,
    website::WebGenModel,
    ImageUnit,
    website::SliderUnit,
    website::GalleryUnit,
    InlineAction,
    website::FeatureSupportAction,
    website::DeleteAction,
    website::SelectAction,
    ChildPath,
    website::ChildPathAttribute,
    FeaturePath,
    website::FeaturePathAttribute,
    website::FeaturePath,
    CollectionUnit,
    DataUnit,
    ControlUnit,
    website::LoginUnit,
    website::RegistrationUnit,
    website::ForgottenPasswordUnit,
    website::SearchUnit,
    SingletonUnit,
    DynamicUnit,
    website::ImageUnit,
    website::DataUnit,
    website::ControlUnit,
    website::EditUnit,
    EditUnit,
    website::CreateUnit,
    InterfaceField,
    website::DateField,
    website::DataTypeField,
    website::ChildPath,
    website::AssociationReference,
    SelectableUnit,
    website::CreateUpdateUnit,
    website::MapUnit,
    website::UpdateUnit,
    website::DetailsUnit,
    website::CollectionUnit,
    website::SingletonUnit,
    website::SelectableUnit,
    website::CaptchaField,
    UnitFeature,
    website::UnitElement,
    InlineActionContainer,
    website::ImageIndexUnit,
    website::IndexUnit,
    UnitField,
    website::InterfaceField,
    website::UnitFeature,
    AssociationReference,
    website::ChildPathAssociation,
    website::FeaturePathAssociation,
    ContentUnit,
    website::CreateSitemapUnit,
    website::DynamicUnit,
    website::StaticUnit,
    website::UnitContainer,
    website::UnitSupportAction,
    website::UnitField,
    website::Filter,
    website::Query,
    website::ContentUnit,
    MenuEntry,
    website::EditStaticTextMenuEntry,
    website::MenuFeature,
    website::ActionMenuEntry,
    Menu,
    website::DynamicMenu,
    website::StaticMenu,
    website::MenuEntry,
    website::QueryParameter,
    website::FilterParameter,
    UnitContainer,
    website::Page,
    website::UnitAssociation,
    ImageFilter,
    website::ThumbnailFilter,
    website::ImageFilter,
    website::Order,
    website::Predicate,
    website::PageLink,
    website::SelectionParameter,
    website::BusinessOperation,
    website::Selection,
    website::View,
    EntityAssociation,
    website::AssociationWithContainment,
    website::AssociationWithoutContainment,
    EncapsulatedFeature,
    website::EncapsulatedAssociation,
    website::EncapsulatedAttribute,
    ViewFeature,
    website::ViewAssociation,
    website::EncapsulatedFeature,
    website::ViewFeature,
    PathElement,
    website::DatePathElement,
    website::StaticPathElement,
    website::PathElement,
    website::ResourceAttribute,
    website::UrlAttribute,
    website::DateAttribute,
    FrameworkTechnologies,
    AuthenticationKeyTypes,
    AjaxTechnologies,
    PageTopMenuOptions,
    OperationResultTypes,
    IndexDisplayOption,
    CollectionDisplayOptions,
    DatabaseTechnologies,
    isHasChoices,
    OrmTechnologies,
    Cardinality,
    DateDetails,
    InputTechnologies,
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



def test_website::routeparameterreference_is_not_abstract():
    assert not inspect.isabstract(website::RouteParameterReference)


def test_website::routeparameterreference_constructor_exists():
    assert callable(website::RouteParameterReference.__init__)


def test_website::routeparameterreference_constructor_args():
    sig = inspect.signature(website::RouteParameterReference.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_website::routeparameterreference_has_name():
    assert hasattr(website::RouteParameterReference, "name")
    descriptor = None
    for klass in website::RouteParameterReference.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_website::featurereference_is_not_abstract():
    assert not inspect.isabstract(website::FeatureReference)


def test_website::featurereference_constructor_exists():
    assert callable(website::FeatureReference.__init__)


def test_website::featurereference_constructor_args():
    sig = inspect.signature(website::FeatureReference.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_website::featurereference_has_name():
    assert hasattr(website::FeatureReference, "name")
    descriptor = None
    for klass in website::FeatureReference.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_website::currentuserreference_is_not_abstract():
    assert not inspect.isabstract(website::CurrentUserReference)


def test_website::currentuserreference_constructor_exists():
    assert callable(website::CurrentUserReference.__init__)


def test_website::currentuserreference_constructor_args():
    sig = inspect.signature(website::CurrentUserReference.__init__)
    params = list(sig.parameters.keys())



def test_website::modelreference_is_not_abstract():
    assert not inspect.isabstract(website::ModelReference)


def test_website::modelreference_constructor_exists():
    assert callable(website::ModelReference.__init__)


def test_website::modelreference_constructor_args():
    sig = inspect.signature(website::ModelReference.__init__)
    params = list(sig.parameters.keys())



def test_website::parameterreference_is_not_abstract():
    assert not inspect.isabstract(website::ParameterReference)


def test_website::parameterreference_constructor_exists():
    assert callable(website::ParameterReference.__init__)


def test_website::parameterreference_constructor_args():
    sig = inspect.signature(website::ParameterReference.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_website::parameterreference_has_name():
    assert hasattr(website::ParameterReference, "name")
    descriptor = None
    for klass in website::ParameterReference.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_website::inlineactioncontainer_is_not_abstract():
    assert not inspect.isabstract(website::InlineActionContainer)


def test_website::inlineactioncontainer_constructor_exists():
    assert callable(website::InlineActionContainer.__init__)


def test_website::inlineactioncontainer_constructor_args():
    sig = inspect.signature(website::InlineActionContainer.__init__)
    params = list(sig.parameters.keys())



def test_authenticationunit_is_not_abstract():
    assert not inspect.isabstract(AuthenticationUnit)


def test_authenticationunit_constructor_exists():
    assert callable(AuthenticationUnit.__init__)


def test_authenticationunit_constructor_args():
    sig = inspect.signature(AuthenticationUnit.__init__)
    params = list(sig.parameters.keys())



def test_website::authenticationunit_is_not_abstract():
    assert not inspect.isabstract(website::AuthenticationUnit)


def test_website::authenticationunit_constructor_exists():
    assert callable(website::AuthenticationUnit.__init__)


def test_website::authenticationunit_constructor_args():
    sig = inspect.signature(website::AuthenticationUnit.__init__)
    params = list(sig.parameters.keys())



def test_entityattribute_is_not_abstract():
    assert not inspect.isabstract(EntityAttribute)


def test_entityattribute_constructor_exists():
    assert callable(EntityAttribute.__init__)


def test_entityattribute_constructor_args():
    sig = inspect.signature(EntityAttribute.__init__)
    params = list(sig.parameters.keys())



def test_website::datatypeattribute_is_not_abstract():
    assert not inspect.isabstract(website::DataTypeAttribute)


def test_website::datatypeattribute_constructor_exists():
    assert callable(website::DataTypeAttribute.__init__)


def test_website::datatypeattribute_constructor_args():
    sig = inspect.signature(website::DataTypeAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "encrypt" in params, "Missing parameter 'encrypt'"
    assert "caseInsensitive" in params, "Missing parameter 'caseInsensitive'"
    assert "obfuscateFormFields" in params, "Missing parameter 'obfuscateFormFields'"

def test_website::datatypeattribute_has_encrypt():
    assert hasattr(website::DataTypeAttribute, "encrypt")
    descriptor = None
    for klass in website::DataTypeAttribute.__mro__:
        if "encrypt" in klass.__dict__:
            descriptor = klass.__dict__["encrypt"]
            break
    assert isinstance(descriptor, property)

def test_website::datatypeattribute_has_caseInsensitive():
    assert hasattr(website::DataTypeAttribute, "caseInsensitive")
    descriptor = None
    for klass in website::DataTypeAttribute.__mro__:
        if "caseInsensitive" in klass.__dict__:
            descriptor = klass.__dict__["caseInsensitive"]
            break
    assert isinstance(descriptor, property)

def test_website::datatypeattribute_has_obfuscateFormFields():
    assert hasattr(website::DataTypeAttribute, "obfuscateFormFields")
    descriptor = None
    for klass in website::DataTypeAttribute.__mro__:
        if "obfuscateFormFields" in klass.__dict__:
            descriptor = klass.__dict__["obfuscateFormFields"]
            break
    assert isinstance(descriptor, property)



def test_attribute_is_not_abstract():
    assert not inspect.isabstract(Attribute)


def test_attribute_constructor_exists():
    assert callable(Attribute.__init__)


def test_attribute_constructor_args():
    sig = inspect.signature(Attribute.__init__)
    params = list(sig.parameters.keys())



def test_entityfeature_is_not_abstract():
    assert not inspect.isabstract(EntityFeature)


def test_entityfeature_constructor_exists():
    assert callable(EntityFeature.__init__)


def test_entityfeature_constructor_args():
    sig = inspect.signature(EntityFeature.__init__)
    params = list(sig.parameters.keys())



def test_website::associationkey_is_not_abstract():
    assert not inspect.isabstract(website::AssociationKey)


def test_website::associationkey_constructor_exists():
    assert callable(website::AssociationKey.__init__)


def test_website::associationkey_constructor_args():
    sig = inspect.signature(website::AssociationKey.__init__)
    params = list(sig.parameters.keys())
    assert "targetColumnName" in params, "Missing parameter 'targetColumnName'"

def test_website::associationkey_has_targetColumnName():
    assert hasattr(website::AssociationKey, "targetColumnName")
    descriptor = None
    for klass in website::AssociationKey.__mro__:
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



def test_website::locationattribute_is_not_abstract():
    assert not inspect.isabstract(website::LocationAttribute)


def test_website::locationattribute_constructor_exists():
    assert callable(website::LocationAttribute.__init__)


def test_website::locationattribute_constructor_args():
    sig = inspect.signature(website::LocationAttribute.__init__)
    params = list(sig.parameters.keys())



def test_resourceattribute_is_not_abstract():
    assert not inspect.isabstract(ResourceAttribute)


def test_resourceattribute_constructor_exists():
    assert callable(ResourceAttribute.__init__)


def test_resourceattribute_constructor_args():
    sig = inspect.signature(ResourceAttribute.__init__)
    params = list(sig.parameters.keys())



def test_website::imageattribute_is_not_abstract():
    assert not inspect.isabstract(website::ImageAttribute)


def test_website::imageattribute_constructor_exists():
    assert callable(website::ImageAttribute.__init__)


def test_website::imageattribute_constructor_args():
    sig = inspect.signature(website::ImageAttribute.__init__)
    params = list(sig.parameters.keys())



def test_website::fileattribute_is_not_abstract():
    assert not inspect.isabstract(website::FileAttribute)


def test_website::fileattribute_constructor_exists():
    assert callable(website::FileAttribute.__init__)


def test_website::fileattribute_constructor_args():
    sig = inspect.signature(website::FileAttribute.__init__)
    params = list(sig.parameters.keys())



def test_entityorview_is_not_abstract():
    assert not inspect.isabstract(EntityOrView)


def test_entityorview_constructor_exists():
    assert callable(EntityOrView.__init__)


def test_entityorview_constructor_args():
    sig = inspect.signature(EntityOrView.__init__)
    params = list(sig.parameters.keys())



def test_website::entity_is_not_abstract():
    assert not inspect.isabstract(website::Entity)


def test_website::entity_constructor_exists():
    assert callable(website::Entity.__init__)


def test_website::entity_constructor_args():
    sig = inspect.signature(website::Entity.__init__)
    params = list(sig.parameters.keys())



def test_website::entityassociation_is_not_abstract():
    assert not inspect.isabstract(website::EntityAssociation)


def test_website::entityassociation_constructor_exists():
    assert callable(website::EntityAssociation.__init__)


def test_website::entityassociation_constructor_args():
    sig = inspect.signature(website::EntityAssociation.__init__)
    params = list(sig.parameters.keys())
    assert "targetInputClass" in params, "Missing parameter 'targetInputClass'"
    assert "targetFeatureName" in params, "Missing parameter 'targetFeatureName'"
    assert "targetDisplayLabel" in params, "Missing parameter 'targetDisplayLabel'"
    assert "pivotTableName" in params, "Missing parameter 'pivotTableName'"
    assert "targetDisplayClass" in params, "Missing parameter 'targetDisplayClass'"
    assert "bidirectional" in params, "Missing parameter 'bidirectional'"
    assert "targetFooterClass" in params, "Missing parameter 'targetFooterClass'"
    assert "targetPrimaryKey" in params, "Missing parameter 'targetPrimaryKey'"
    assert "targetHeaderClass" in params, "Missing parameter 'targetHeaderClass'"

def test_website::entityassociation_has_targetInputClass():
    assert hasattr(website::EntityAssociation, "targetInputClass")
    descriptor = None
    for klass in website::EntityAssociation.__mro__:
        if "targetInputClass" in klass.__dict__:
            descriptor = klass.__dict__["targetInputClass"]
            break
    assert isinstance(descriptor, property)

def test_website::entityassociation_has_targetFeatureName():
    assert hasattr(website::EntityAssociation, "targetFeatureName")
    descriptor = None
    for klass in website::EntityAssociation.__mro__:
        if "targetFeatureName" in klass.__dict__:
            descriptor = klass.__dict__["targetFeatureName"]
            break
    assert isinstance(descriptor, property)

def test_website::entityassociation_has_targetDisplayLabel():
    assert hasattr(website::EntityAssociation, "targetDisplayLabel")
    descriptor = None
    for klass in website::EntityAssociation.__mro__:
        if "targetDisplayLabel" in klass.__dict__:
            descriptor = klass.__dict__["targetDisplayLabel"]
            break
    assert isinstance(descriptor, property)

def test_website::entityassociation_has_pivotTableName():
    assert hasattr(website::EntityAssociation, "pivotTableName")
    descriptor = None
    for klass in website::EntityAssociation.__mro__:
        if "pivotTableName" in klass.__dict__:
            descriptor = klass.__dict__["pivotTableName"]
            break
    assert isinstance(descriptor, property)

def test_website::entityassociation_has_targetDisplayClass():
    assert hasattr(website::EntityAssociation, "targetDisplayClass")
    descriptor = None
    for klass in website::EntityAssociation.__mro__:
        if "targetDisplayClass" in klass.__dict__:
            descriptor = klass.__dict__["targetDisplayClass"]
            break
    assert isinstance(descriptor, property)

def test_website::entityassociation_has_bidirectional():
    assert hasattr(website::EntityAssociation, "bidirectional")
    descriptor = None
    for klass in website::EntityAssociation.__mro__:
        if "bidirectional" in klass.__dict__:
            descriptor = klass.__dict__["bidirectional"]
            break
    assert isinstance(descriptor, property)

def test_website::entityassociation_has_targetFooterClass():
    assert hasattr(website::EntityAssociation, "targetFooterClass")
    descriptor = None
    for klass in website::EntityAssociation.__mro__:
        if "targetFooterClass" in klass.__dict__:
            descriptor = klass.__dict__["targetFooterClass"]
            break
    assert isinstance(descriptor, property)

def test_website::entityassociation_has_targetPrimaryKey():
    assert hasattr(website::EntityAssociation, "targetPrimaryKey")
    descriptor = None
    for klass in website::EntityAssociation.__mro__:
        if "targetPrimaryKey" in klass.__dict__:
            descriptor = klass.__dict__["targetPrimaryKey"]
            break
    assert isinstance(descriptor, property)

def test_website::entityassociation_has_targetHeaderClass():
    assert hasattr(website::EntityAssociation, "targetHeaderClass")
    descriptor = None
    for klass in website::EntityAssociation.__mro__:
        if "targetHeaderClass" in klass.__dict__:
            descriptor = klass.__dict__["targetHeaderClass"]
            break
    assert isinstance(descriptor, property)



def test_modellabelfeature_is_not_abstract():
    assert not inspect.isabstract(ModelLabelFeature)


def test_modellabelfeature_constructor_exists():
    assert callable(ModelLabelFeature.__init__)


def test_modellabelfeature_constructor_args():
    sig = inspect.signature(ModelLabelFeature.__init__)
    params = list(sig.parameters.keys())



def test_website::modellabelassociation_is_not_abstract():
    assert not inspect.isabstract(website::ModelLabelAssociation)


def test_website::modellabelassociation_constructor_exists():
    assert callable(website::ModelLabelAssociation.__init__)


def test_website::modellabelassociation_constructor_args():
    sig = inspect.signature(website::ModelLabelAssociation.__init__)
    params = list(sig.parameters.keys())
    assert "isSourceAssociation" in params, "Missing parameter 'isSourceAssociation'"

def test_website::modellabelassociation_has_isSourceAssociation():
    assert hasattr(website::ModelLabelAssociation, "isSourceAssociation")
    descriptor = None
    for klass in website::ModelLabelAssociation.__mro__:
        if "isSourceAssociation" in klass.__dict__:
            descriptor = klass.__dict__["isSourceAssociation"]
            break
    assert isinstance(descriptor, property)



def test_website::modellabelattribute_is_not_abstract():
    assert not inspect.isabstract(website::ModelLabelAttribute)


def test_website::modellabelattribute_constructor_exists():
    assert callable(website::ModelLabelAttribute.__init__)


def test_website::modellabelattribute_constructor_args():
    sig = inspect.signature(website::ModelLabelAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "dateFormat" in params, "Missing parameter 'dateFormat'"

def test_website::modellabelattribute_has_dateFormat():
    assert hasattr(website::ModelLabelAttribute, "dateFormat")
    descriptor = None
    for klass in website::ModelLabelAttribute.__mro__:
        if "dateFormat" in klass.__dict__:
            descriptor = klass.__dict__["dateFormat"]
            break
    assert isinstance(descriptor, property)



def test_website::modellabelfeature_is_not_abstract():
    assert not inspect.isabstract(website::ModelLabelFeature)


def test_website::modellabelfeature_constructor_exists():
    assert callable(website::ModelLabelFeature.__init__)


def test_website::modellabelfeature_constructor_args():
    sig = inspect.signature(website::ModelLabelFeature.__init__)
    params = list(sig.parameters.keys())



def test_website::label_is_not_abstract():
    assert not inspect.isabstract(website::Label)


def test_website::label_constructor_exists():
    assert callable(website::Label.__init__)


def test_website::label_constructor_args():
    sig = inspect.signature(website::Label.__init__)
    params = list(sig.parameters.keys())



def test_website::entityattribute_is_not_abstract():
    assert not inspect.isabstract(website::EntityAttribute)


def test_website::entityattribute_constructor_exists():
    assert callable(website::EntityAttribute.__init__)


def test_website::entityattribute_constructor_args():
    sig = inspect.signature(website::EntityAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "interfaceType" in params, "Missing parameter 'interfaceType'"
    assert "primaryKey" in params, "Missing parameter 'primaryKey'"
    assert "containerUnique" in params, "Missing parameter 'containerUnique'"
    assert "persistentType" in params, "Missing parameter 'persistentType'"
    assert "ormType" in params, "Missing parameter 'ormType'"

def test_website::entityattribute_has_interfaceType():
    assert hasattr(website::EntityAttribute, "interfaceType")
    descriptor = None
    for klass in website::EntityAttribute.__mro__:
        if "interfaceType" in klass.__dict__:
            descriptor = klass.__dict__["interfaceType"]
            break
    assert isinstance(descriptor, property)

def test_website::entityattribute_has_primaryKey():
    assert hasattr(website::EntityAttribute, "primaryKey")
    descriptor = None
    for klass in website::EntityAttribute.__mro__:
        if "primaryKey" in klass.__dict__:
            descriptor = klass.__dict__["primaryKey"]
            break
    assert isinstance(descriptor, property)

def test_website::entityattribute_has_containerUnique():
    assert hasattr(website::EntityAttribute, "containerUnique")
    descriptor = None
    for klass in website::EntityAttribute.__mro__:
        if "containerUnique" in klass.__dict__:
            descriptor = klass.__dict__["containerUnique"]
            break
    assert isinstance(descriptor, property)

def test_website::entityattribute_has_persistentType():
    assert hasattr(website::EntityAttribute, "persistentType")
    descriptor = None
    for klass in website::EntityAttribute.__mro__:
        if "persistentType" in klass.__dict__:
            descriptor = klass.__dict__["persistentType"]
            break
    assert isinstance(descriptor, property)

def test_website::entityattribute_has_ormType():
    assert hasattr(website::EntityAttribute, "ormType")
    descriptor = None
    for klass in website::EntityAttribute.__mro__:
        if "ormType" in klass.__dict__:
            descriptor = klass.__dict__["ormType"]
            break
    assert isinstance(descriptor, property)



def test_website::expression_is_not_abstract():
    assert not inspect.isabstract(website::Expression)


def test_website::expression_constructor_exists():
    assert callable(website::Expression.__init__)


def test_website::expression_constructor_args():
    sig = inspect.signature(website::Expression.__init__)
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



def test_website::association_is_not_abstract():
    assert not inspect.isabstract(website::Association)


def test_website::association_constructor_exists():
    assert callable(website::Association.__init__)


def test_website::association_constructor_args():
    sig = inspect.signature(website::Association.__init__)
    params = list(sig.parameters.keys())
    assert "serializationMaxDepth" in params, "Missing parameter 'serializationMaxDepth'"
    assert "pseudo" in params, "Missing parameter 'pseudo'"
    assert "inputClass" in params, "Missing parameter 'inputClass'"

def test_website::association_has_serializationMaxDepth():
    assert hasattr(website::Association, "serializationMaxDepth")
    descriptor = None
    for klass in website::Association.__mro__:
        if "serializationMaxDepth" in klass.__dict__:
            descriptor = klass.__dict__["serializationMaxDepth"]
            break
    assert isinstance(descriptor, property)

def test_website::association_has_pseudo():
    assert hasattr(website::Association, "pseudo")
    descriptor = None
    for klass in website::Association.__mro__:
        if "pseudo" in klass.__dict__:
            descriptor = klass.__dict__["pseudo"]
            break
    assert isinstance(descriptor, property)

def test_website::association_has_inputClass():
    assert hasattr(website::Association, "inputClass")
    descriptor = None
    for klass in website::Association.__mro__:
        if "inputClass" in klass.__dict__:
            descriptor = klass.__dict__["inputClass"]
            break
    assert isinstance(descriptor, property)



def test_website::feature_is_not_abstract():
    assert not inspect.isabstract(website::Feature)


def test_website::feature_constructor_exists():
    assert callable(website::Feature.__init__)


def test_website::feature_constructor_args():
    sig = inspect.signature(website::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "displayClass" in params, "Missing parameter 'displayClass'"
    assert "encodeUriKey" in params, "Missing parameter 'encodeUriKey'"
    assert "nullDisplayValue" in params, "Missing parameter 'nullDisplayValue'"
    assert "collectionAllowRemove" in params, "Missing parameter 'collectionAllowRemove'"
    assert "serializationExpose" in params, "Missing parameter 'serializationExpose'"
    assert "headerClass" in params, "Missing parameter 'headerClass'"
    assert "collectionAllowAdd" in params, "Missing parameter 'collectionAllowAdd'"
    assert "title" in params, "Missing parameter 'title'"
    assert "serializationGroups" in params, "Missing parameter 'serializationGroups'"
    assert "footerClass" in params, "Missing parameter 'footerClass'"

def test_website::feature_has_displayClass():
    assert hasattr(website::Feature, "displayClass")
    descriptor = None
    for klass in website::Feature.__mro__:
        if "displayClass" in klass.__dict__:
            descriptor = klass.__dict__["displayClass"]
            break
    assert isinstance(descriptor, property)

def test_website::feature_has_encodeUriKey():
    assert hasattr(website::Feature, "encodeUriKey")
    descriptor = None
    for klass in website::Feature.__mro__:
        if "encodeUriKey" in klass.__dict__:
            descriptor = klass.__dict__["encodeUriKey"]
            break
    assert isinstance(descriptor, property)

def test_website::feature_has_nullDisplayValue():
    assert hasattr(website::Feature, "nullDisplayValue")
    descriptor = None
    for klass in website::Feature.__mro__:
        if "nullDisplayValue" in klass.__dict__:
            descriptor = klass.__dict__["nullDisplayValue"]
            break
    assert isinstance(descriptor, property)

def test_website::feature_has_collectionAllowRemove():
    assert hasattr(website::Feature, "collectionAllowRemove")
    descriptor = None
    for klass in website::Feature.__mro__:
        if "collectionAllowRemove" in klass.__dict__:
            descriptor = klass.__dict__["collectionAllowRemove"]
            break
    assert isinstance(descriptor, property)

def test_website::feature_has_serializationExpose():
    assert hasattr(website::Feature, "serializationExpose")
    descriptor = None
    for klass in website::Feature.__mro__:
        if "serializationExpose" in klass.__dict__:
            descriptor = klass.__dict__["serializationExpose"]
            break
    assert isinstance(descriptor, property)

def test_website::feature_has_headerClass():
    assert hasattr(website::Feature, "headerClass")
    descriptor = None
    for klass in website::Feature.__mro__:
        if "headerClass" in klass.__dict__:
            descriptor = klass.__dict__["headerClass"]
            break
    assert isinstance(descriptor, property)

def test_website::feature_has_collectionAllowAdd():
    assert hasattr(website::Feature, "collectionAllowAdd")
    descriptor = None
    for klass in website::Feature.__mro__:
        if "collectionAllowAdd" in klass.__dict__:
            descriptor = klass.__dict__["collectionAllowAdd"]
            break
    assert isinstance(descriptor, property)

def test_website::feature_has_title():
    assert hasattr(website::Feature, "title")
    descriptor = None
    for klass in website::Feature.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_website::feature_has_serializationGroups():
    assert hasattr(website::Feature, "serializationGroups")
    descriptor = None
    for klass in website::Feature.__mro__:
        if "serializationGroups" in klass.__dict__:
            descriptor = klass.__dict__["serializationGroups"]
            break
    assert isinstance(descriptor, property)

def test_website::feature_has_footerClass():
    assert hasattr(website::Feature, "footerClass")
    descriptor = None
    for klass in website::Feature.__mro__:
        if "footerClass" in klass.__dict__:
            descriptor = klass.__dict__["footerClass"]
            break
    assert isinstance(descriptor, property)



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_website::enumerationtype_is_not_abstract():
    assert not inspect.isabstract(website::EnumerationType)


def test_website::enumerationtype_constructor_exists():
    assert callable(website::EnumerationType.__init__)


def test_website::enumerationtype_constructor_args():
    sig = inspect.signature(website::EnumerationType.__init__)
    params = list(sig.parameters.keys())



def test_website::namedelement_is_not_abstract():
    assert not inspect.isabstract(website::NamedElement)


def test_website::namedelement_constructor_exists():
    assert callable(website::NamedElement.__init__)


def test_website::namedelement_constructor_args():
    sig = inspect.signature(website::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_website::namedelement_has_name():
    assert hasattr(website::NamedElement, "name")
    descriptor = None
    for klass in website::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_authentication_is_not_abstract():
    assert not inspect.isabstract(Authentication)


def test_authentication_constructor_exists():
    assert callable(Authentication.__init__)


def test_authentication_constructor_args():
    sig = inspect.signature(Authentication.__init__)
    params = list(sig.parameters.keys())



def test_website::casauthentication_is_not_abstract():
    assert not inspect.isabstract(website::CasAuthentication)


def test_website::casauthentication_constructor_exists():
    assert callable(website::CasAuthentication.__init__)


def test_website::casauthentication_constructor_args():
    sig = inspect.signature(website::CasAuthentication.__init__)
    params = list(sig.parameters.keys())



def test_website::localauthenticationsystem_is_not_abstract():
    assert not inspect.isabstract(website::LocalAuthenticationSystem)


def test_website::localauthenticationsystem_constructor_exists():
    assert callable(website::LocalAuthenticationSystem.__init__)


def test_website::localauthenticationsystem_constructor_args():
    sig = inspect.signature(website::LocalAuthenticationSystem.__init__)
    params = list(sig.parameters.keys())
    assert "allowSelfRegistration" in params, "Missing parameter 'allowSelfRegistration'"
    assert "allowRememberMe" in params, "Missing parameter 'allowRememberMe'"
    assert "sendWelcomeEmail" in params, "Missing parameter 'sendWelcomeEmail'"
    assert "useEmailActivation" in params, "Missing parameter 'useEmailActivation'"
    assert "authenticationKey" in params, "Missing parameter 'authenticationKey'"
    assert "trackLoginAttempts" in params, "Missing parameter 'trackLoginAttempts'"
    assert "useCaptcha" in params, "Missing parameter 'useCaptcha'"

def test_website::localauthenticationsystem_has_allowSelfRegistration():
    assert hasattr(website::LocalAuthenticationSystem, "allowSelfRegistration")
    descriptor = None
    for klass in website::LocalAuthenticationSystem.__mro__:
        if "allowSelfRegistration" in klass.__dict__:
            descriptor = klass.__dict__["allowSelfRegistration"]
            break
    assert isinstance(descriptor, property)

def test_website::localauthenticationsystem_has_allowRememberMe():
    assert hasattr(website::LocalAuthenticationSystem, "allowRememberMe")
    descriptor = None
    for klass in website::LocalAuthenticationSystem.__mro__:
        if "allowRememberMe" in klass.__dict__:
            descriptor = klass.__dict__["allowRememberMe"]
            break
    assert isinstance(descriptor, property)

def test_website::localauthenticationsystem_has_sendWelcomeEmail():
    assert hasattr(website::LocalAuthenticationSystem, "sendWelcomeEmail")
    descriptor = None
    for klass in website::LocalAuthenticationSystem.__mro__:
        if "sendWelcomeEmail" in klass.__dict__:
            descriptor = klass.__dict__["sendWelcomeEmail"]
            break
    assert isinstance(descriptor, property)

def test_website::localauthenticationsystem_has_useEmailActivation():
    assert hasattr(website::LocalAuthenticationSystem, "useEmailActivation")
    descriptor = None
    for klass in website::LocalAuthenticationSystem.__mro__:
        if "useEmailActivation" in klass.__dict__:
            descriptor = klass.__dict__["useEmailActivation"]
            break
    assert isinstance(descriptor, property)

def test_website::localauthenticationsystem_has_authenticationKey():
    assert hasattr(website::LocalAuthenticationSystem, "authenticationKey")
    descriptor = None
    for klass in website::LocalAuthenticationSystem.__mro__:
        if "authenticationKey" in klass.__dict__:
            descriptor = klass.__dict__["authenticationKey"]
            break
    assert isinstance(descriptor, property)

def test_website::localauthenticationsystem_has_trackLoginAttempts():
    assert hasattr(website::LocalAuthenticationSystem, "trackLoginAttempts")
    descriptor = None
    for klass in website::LocalAuthenticationSystem.__mro__:
        if "trackLoginAttempts" in klass.__dict__:
            descriptor = klass.__dict__["trackLoginAttempts"]
            break
    assert isinstance(descriptor, property)

def test_website::localauthenticationsystem_has_useCaptcha():
    assert hasattr(website::LocalAuthenticationSystem, "useCaptcha")
    descriptor = None
    for klass in website::LocalAuthenticationSystem.__mro__:
        if "useCaptcha" in klass.__dict__:
            descriptor = klass.__dict__["useCaptcha"]
            break
    assert isinstance(descriptor, property)



def test_website::attribute_is_not_abstract():
    assert not inspect.isabstract(website::Attribute)


def test_website::attribute_constructor_exists():
    assert callable(website::Attribute.__init__)


def test_website::attribute_constructor_args():
    sig = inspect.signature(website::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "validationPattern" in params, "Missing parameter 'validationPattern'"
    assert "placeholder" in params, "Missing parameter 'placeholder'"
    assert "inputClass" in params, "Missing parameter 'inputClass'"

def test_website::attribute_has_validationPattern():
    assert hasattr(website::Attribute, "validationPattern")
    descriptor = None
    for klass in website::Attribute.__mro__:
        if "validationPattern" in klass.__dict__:
            descriptor = klass.__dict__["validationPattern"]
            break
    assert isinstance(descriptor, property)

def test_website::attribute_has_placeholder():
    assert hasattr(website::Attribute, "placeholder")
    descriptor = None
    for klass in website::Attribute.__mro__:
        if "placeholder" in klass.__dict__:
            descriptor = klass.__dict__["placeholder"]
            break
    assert isinstance(descriptor, property)

def test_website::attribute_has_inputClass():
    assert hasattr(website::Attribute, "inputClass")
    descriptor = None
    for klass in website::Attribute.__mro__:
        if "inputClass" in klass.__dict__:
            descriptor = klass.__dict__["inputClass"]
            break
    assert isinstance(descriptor, property)



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_website::datatype_is_not_abstract():
    assert not inspect.isabstract(website::DataType)


def test_website::datatype_constructor_exists():
    assert callable(website::DataType.__init__)


def test_website::datatype_constructor_args():
    sig = inspect.signature(website::DataType.__init__)
    params = list(sig.parameters.keys())
    assert "persistentType" in params, "Missing parameter 'persistentType'"
    assert "validationPattern" in params, "Missing parameter 'validationPattern'"
    assert "placeholder" in params, "Missing parameter 'placeholder'"
    assert "interfaceType" in params, "Missing parameter 'interfaceType'"
    assert "ormType" in params, "Missing parameter 'ormType'"

def test_website::datatype_has_persistentType():
    assert hasattr(website::DataType, "persistentType")
    descriptor = None
    for klass in website::DataType.__mro__:
        if "persistentType" in klass.__dict__:
            descriptor = klass.__dict__["persistentType"]
            break
    assert isinstance(descriptor, property)

def test_website::datatype_has_validationPattern():
    assert hasattr(website::DataType, "validationPattern")
    descriptor = None
    for klass in website::DataType.__mro__:
        if "validationPattern" in klass.__dict__:
            descriptor = klass.__dict__["validationPattern"]
            break
    assert isinstance(descriptor, property)

def test_website::datatype_has_placeholder():
    assert hasattr(website::DataType, "placeholder")
    descriptor = None
    for klass in website::DataType.__mro__:
        if "placeholder" in klass.__dict__:
            descriptor = klass.__dict__["placeholder"]
            break
    assert isinstance(descriptor, property)

def test_website::datatype_has_interfaceType():
    assert hasattr(website::DataType, "interfaceType")
    descriptor = None
    for klass in website::DataType.__mro__:
        if "interfaceType" in klass.__dict__:
            descriptor = klass.__dict__["interfaceType"]
            break
    assert isinstance(descriptor, property)

def test_website::datatype_has_ormType():
    assert hasattr(website::DataType, "ormType")
    descriptor = None
    for klass in website::DataType.__mro__:
        if "ormType" in klass.__dict__:
            descriptor = klass.__dict__["ormType"]
            break
    assert isinstance(descriptor, property)



def test_nameddisplayelement_is_not_abstract():
    assert not inspect.isabstract(NamedDisplayElement)


def test_nameddisplayelement_constructor_exists():
    assert callable(NamedDisplayElement.__init__)


def test_nameddisplayelement_constructor_args():
    sig = inspect.signature(NamedDisplayElement.__init__)
    params = list(sig.parameters.keys())



def test_website::inlineaction_is_not_abstract():
    assert not inspect.isabstract(website::InlineAction)


def test_website::inlineaction_constructor_exists():
    assert callable(website::InlineAction.__init__)


def test_website::inlineaction_constructor_args():
    sig = inspect.signature(website::InlineAction.__init__)
    params = list(sig.parameters.keys())
    assert "footer" in params, "Missing parameter 'footer'"
    assert "headerClass" in params, "Missing parameter 'headerClass'"
    assert "disable" in params, "Missing parameter 'disable'"
    assert "header" in params, "Missing parameter 'header'"
    assert "requiresRole" in params, "Missing parameter 'requiresRole'"
    assert "footerClass" in params, "Missing parameter 'footerClass'"

def test_website::inlineaction_has_footer():
    assert hasattr(website::InlineAction, "footer")
    descriptor = None
    for klass in website::InlineAction.__mro__:
        if "footer" in klass.__dict__:
            descriptor = klass.__dict__["footer"]
            break
    assert isinstance(descriptor, property)

def test_website::inlineaction_has_headerClass():
    assert hasattr(website::InlineAction, "headerClass")
    descriptor = None
    for klass in website::InlineAction.__mro__:
        if "headerClass" in klass.__dict__:
            descriptor = klass.__dict__["headerClass"]
            break
    assert isinstance(descriptor, property)

def test_website::inlineaction_has_disable():
    assert hasattr(website::InlineAction, "disable")
    descriptor = None
    for klass in website::InlineAction.__mro__:
        if "disable" in klass.__dict__:
            descriptor = klass.__dict__["disable"]
            break
    assert isinstance(descriptor, property)

def test_website::inlineaction_has_header():
    assert hasattr(website::InlineAction, "header")
    descriptor = None
    for klass in website::InlineAction.__mro__:
        if "header" in klass.__dict__:
            descriptor = klass.__dict__["header"]
            break
    assert isinstance(descriptor, property)

def test_website::inlineaction_has_requiresRole():
    assert hasattr(website::InlineAction, "requiresRole")
    descriptor = None
    for klass in website::InlineAction.__mro__:
        if "requiresRole" in klass.__dict__:
            descriptor = klass.__dict__["requiresRole"]
            break
    assert isinstance(descriptor, property)

def test_website::inlineaction_has_footerClass():
    assert hasattr(website::InlineAction, "footerClass")
    descriptor = None
    for klass in website::InlineAction.__mro__:
        if "footerClass" in klass.__dict__:
            descriptor = klass.__dict__["footerClass"]
            break
    assert isinstance(descriptor, property)



def test_website::enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(website::EnumerationLiteral)


def test_website::enumerationliteral_constructor_exists():
    assert callable(website::EnumerationLiteral.__init__)


def test_website::enumerationliteral_constructor_args():
    sig = inspect.signature(website::EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_website::entityfeature_is_not_abstract():
    assert not inspect.isabstract(website::EntityFeature)


def test_website::entityfeature_constructor_exists():
    assert callable(website::EntityFeature.__init__)


def test_website::entityfeature_constructor_args():
    sig = inspect.signature(website::EntityFeature.__init__)
    params = list(sig.parameters.keys())
    assert "pluralisedName" in params, "Missing parameter 'pluralisedName'"
    assert "unique" in params, "Missing parameter 'unique'"
    assert "singletonName" in params, "Missing parameter 'singletonName'"
    assert "cardinality" in params, "Missing parameter 'cardinality'"
    assert "booleanIsHasChoice" in params, "Missing parameter 'booleanIsHasChoice'"
    assert "ordered" in params, "Missing parameter 'ordered'"
    assert "columnName" in params, "Missing parameter 'columnName'"

def test_website::entityfeature_has_pluralisedName():
    assert hasattr(website::EntityFeature, "pluralisedName")
    descriptor = None
    for klass in website::EntityFeature.__mro__:
        if "pluralisedName" in klass.__dict__:
            descriptor = klass.__dict__["pluralisedName"]
            break
    assert isinstance(descriptor, property)

def test_website::entityfeature_has_unique():
    assert hasattr(website::EntityFeature, "unique")
    descriptor = None
    for klass in website::EntityFeature.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)

def test_website::entityfeature_has_singletonName():
    assert hasattr(website::EntityFeature, "singletonName")
    descriptor = None
    for klass in website::EntityFeature.__mro__:
        if "singletonName" in klass.__dict__:
            descriptor = klass.__dict__["singletonName"]
            break
    assert isinstance(descriptor, property)

def test_website::entityfeature_has_cardinality():
    assert hasattr(website::EntityFeature, "cardinality")
    descriptor = None
    for klass in website::EntityFeature.__mro__:
        if "cardinality" in klass.__dict__:
            descriptor = klass.__dict__["cardinality"]
            break
    assert isinstance(descriptor, property)

def test_website::entityfeature_has_booleanIsHasChoice():
    assert hasattr(website::EntityFeature, "booleanIsHasChoice")
    descriptor = None
    for klass in website::EntityFeature.__mro__:
        if "booleanIsHasChoice" in klass.__dict__:
            descriptor = klass.__dict__["booleanIsHasChoice"]
            break
    assert isinstance(descriptor, property)

def test_website::entityfeature_has_ordered():
    assert hasattr(website::EntityFeature, "ordered")
    descriptor = None
    for klass in website::EntityFeature.__mro__:
        if "ordered" in klass.__dict__:
            descriptor = klass.__dict__["ordered"]
            break
    assert isinstance(descriptor, property)

def test_website::entityfeature_has_columnName():
    assert hasattr(website::EntityFeature, "columnName")
    descriptor = None
    for klass in website::EntityFeature.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_website::modellabel_is_not_abstract():
    assert not inspect.isabstract(website::ModelLabel)


def test_website::modellabel_constructor_exists():
    assert callable(website::ModelLabel.__init__)


def test_website::modellabel_constructor_args():
    sig = inspect.signature(website::ModelLabel.__init__)
    params = list(sig.parameters.keys())
    assert "format" in params, "Missing parameter 'format'"

def test_website::modellabel_has_format():
    assert hasattr(website::ModelLabel, "format")
    descriptor = None
    for klass in website::ModelLabel.__mro__:
        if "format" in klass.__dict__:
            descriptor = klass.__dict__["format"]
            break
    assert isinstance(descriptor, property)



def test_website::nameddisplayelement_is_not_abstract():
    assert not inspect.isabstract(website::NamedDisplayElement)


def test_website::nameddisplayelement_constructor_exists():
    assert callable(website::NamedDisplayElement.__init__)


def test_website::nameddisplayelement_constructor_args():
    sig = inspect.signature(website::NamedDisplayElement.__init__)
    params = list(sig.parameters.keys())
    assert "displayLabel" in params, "Missing parameter 'displayLabel'"

def test_website::nameddisplayelement_has_displayLabel():
    assert hasattr(website::NamedDisplayElement, "displayLabel")
    descriptor = None
    for klass in website::NamedDisplayElement.__mro__:
        if "displayLabel" in klass.__dict__:
            descriptor = klass.__dict__["displayLabel"]
            break
    assert isinstance(descriptor, property)



def test_website::authentication_is_not_abstract():
    assert not inspect.isabstract(website::Authentication)


def test_website::authentication_constructor_exists():
    assert callable(website::Authentication.__init__)


def test_website::authentication_constructor_args():
    sig = inspect.signature(website::Authentication.__init__)
    params = list(sig.parameters.keys())
    assert "logoutLabel" in params, "Missing parameter 'logoutLabel'"
    assert "loginLabel" in params, "Missing parameter 'loginLabel'"

def test_website::authentication_has_logoutLabel():
    assert hasattr(website::Authentication, "logoutLabel")
    descriptor = None
    for klass in website::Authentication.__mro__:
        if "logoutLabel" in klass.__dict__:
            descriptor = klass.__dict__["logoutLabel"]
            break
    assert isinstance(descriptor, property)

def test_website::authentication_has_loginLabel():
    assert hasattr(website::Authentication, "loginLabel")
    descriptor = None
    for klass in website::Authentication.__mro__:
        if "loginLabel" in klass.__dict__:
            descriptor = klass.__dict__["loginLabel"]
            break
    assert isinstance(descriptor, property)



def test_website::imagemanipulation_is_not_abstract():
    assert not inspect.isabstract(website::ImageManipulation)


def test_website::imagemanipulation_constructor_exists():
    assert callable(website::ImageManipulation.__init__)


def test_website::imagemanipulation_constructor_args():
    sig = inspect.signature(website::ImageManipulation.__init__)
    params = list(sig.parameters.keys())
    assert "jpegQuality" in params, "Missing parameter 'jpegQuality'"

def test_website::imagemanipulation_has_jpegQuality():
    assert hasattr(website::ImageManipulation, "jpegQuality")
    descriptor = None
    for klass in website::ImageManipulation.__mro__:
        if "jpegQuality" in klass.__dict__:
            descriptor = klass.__dict__["jpegQuality"]
            break
    assert isinstance(descriptor, property)



def test_website::entityorview_is_not_abstract():
    assert not inspect.isabstract(website::EntityOrView)


def test_website::entityorview_constructor_exists():
    assert callable(website::EntityOrView.__init__)


def test_website::entityorview_constructor_args():
    sig = inspect.signature(website::EntityOrView.__init__)
    params = list(sig.parameters.keys())
    assert "implementsUserInterface" in params, "Missing parameter 'implementsUserInterface'"
    assert "autoKeyGenerationStrategy" in params, "Missing parameter 'autoKeyGenerationStrategy'"
    assert "singletonName" in params, "Missing parameter 'singletonName'"
    assert "autoKeyName" in params, "Missing parameter 'autoKeyName'"
    assert "serializationExcludeAll" in params, "Missing parameter 'serializationExcludeAll'"
    assert "autoKeyPersistentType" in params, "Missing parameter 'autoKeyPersistentType'"
    assert "tableName" in params, "Missing parameter 'tableName'"
    assert "pluralisedName" in params, "Missing parameter 'pluralisedName'"

def test_website::entityorview_has_implementsUserInterface():
    assert hasattr(website::EntityOrView, "implementsUserInterface")
    descriptor = None
    for klass in website::EntityOrView.__mro__:
        if "implementsUserInterface" in klass.__dict__:
            descriptor = klass.__dict__["implementsUserInterface"]
            break
    assert isinstance(descriptor, property)

def test_website::entityorview_has_autoKeyGenerationStrategy():
    assert hasattr(website::EntityOrView, "autoKeyGenerationStrategy")
    descriptor = None
    for klass in website::EntityOrView.__mro__:
        if "autoKeyGenerationStrategy" in klass.__dict__:
            descriptor = klass.__dict__["autoKeyGenerationStrategy"]
            break
    assert isinstance(descriptor, property)

def test_website::entityorview_has_singletonName():
    assert hasattr(website::EntityOrView, "singletonName")
    descriptor = None
    for klass in website::EntityOrView.__mro__:
        if "singletonName" in klass.__dict__:
            descriptor = klass.__dict__["singletonName"]
            break
    assert isinstance(descriptor, property)

def test_website::entityorview_has_autoKeyName():
    assert hasattr(website::EntityOrView, "autoKeyName")
    descriptor = None
    for klass in website::EntityOrView.__mro__:
        if "autoKeyName" in klass.__dict__:
            descriptor = klass.__dict__["autoKeyName"]
            break
    assert isinstance(descriptor, property)

def test_website::entityorview_has_serializationExcludeAll():
    assert hasattr(website::EntityOrView, "serializationExcludeAll")
    descriptor = None
    for klass in website::EntityOrView.__mro__:
        if "serializationExcludeAll" in klass.__dict__:
            descriptor = klass.__dict__["serializationExcludeAll"]
            break
    assert isinstance(descriptor, property)

def test_website::entityorview_has_autoKeyPersistentType():
    assert hasattr(website::EntityOrView, "autoKeyPersistentType")
    descriptor = None
    for klass in website::EntityOrView.__mro__:
        if "autoKeyPersistentType" in klass.__dict__:
            descriptor = klass.__dict__["autoKeyPersistentType"]
            break
    assert isinstance(descriptor, property)

def test_website::entityorview_has_tableName():
    assert hasattr(website::EntityOrView, "tableName")
    descriptor = None
    for klass in website::EntityOrView.__mro__:
        if "tableName" in klass.__dict__:
            descriptor = klass.__dict__["tableName"]
            break
    assert isinstance(descriptor, property)

def test_website::entityorview_has_pluralisedName():
    assert hasattr(website::EntityOrView, "pluralisedName")
    descriptor = None
    for klass in website::EntityOrView.__mro__:
        if "pluralisedName" in klass.__dict__:
            descriptor = klass.__dict__["pluralisedName"]
            break
    assert isinstance(descriptor, property)



def test_website::menu_is_not_abstract():
    assert not inspect.isabstract(website::Menu)


def test_website::menu_constructor_exists():
    assert callable(website::Menu.__init__)


def test_website::menu_constructor_args():
    sig = inspect.signature(website::Menu.__init__)
    params = list(sig.parameters.keys())
    assert "captionClass" in params, "Missing parameter 'captionClass'"
    assert "styleClass" in params, "Missing parameter 'styleClass'"
    assert "omitCaption" in params, "Missing parameter 'omitCaption'"
    assert "layoutClass" in params, "Missing parameter 'layoutClass'"

def test_website::menu_has_captionClass():
    assert hasattr(website::Menu, "captionClass")
    descriptor = None
    for klass in website::Menu.__mro__:
        if "captionClass" in klass.__dict__:
            descriptor = klass.__dict__["captionClass"]
            break
    assert isinstance(descriptor, property)

def test_website::menu_has_styleClass():
    assert hasattr(website::Menu, "styleClass")
    descriptor = None
    for klass in website::Menu.__mro__:
        if "styleClass" in klass.__dict__:
            descriptor = klass.__dict__["styleClass"]
            break
    assert isinstance(descriptor, property)

def test_website::menu_has_omitCaption():
    assert hasattr(website::Menu, "omitCaption")
    descriptor = None
    for klass in website::Menu.__mro__:
        if "omitCaption" in klass.__dict__:
            descriptor = klass.__dict__["omitCaption"]
            break
    assert isinstance(descriptor, property)

def test_website::menu_has_layoutClass():
    assert hasattr(website::Menu, "layoutClass")
    descriptor = None
    for klass in website::Menu.__mro__:
        if "layoutClass" in klass.__dict__:
            descriptor = klass.__dict__["layoutClass"]
            break
    assert isinstance(descriptor, property)



def test_website::service_is_not_abstract():
    assert not inspect.isabstract(website::Service)


def test_website::service_constructor_exists():
    assert callable(website::Service.__init__)


def test_website::service_constructor_args():
    sig = inspect.signature(website::Service.__init__)
    params = list(sig.parameters.keys())



def test_website::classifier_is_not_abstract():
    assert not inspect.isabstract(website::Classifier)


def test_website::classifier_constructor_exists():
    assert callable(website::Classifier.__init__)


def test_website::classifier_constructor_args():
    sig = inspect.signature(website::Classifier.__init__)
    params = list(sig.parameters.keys())



def test_website::websiteproperties_is_not_abstract():
    assert not inspect.isabstract(website::WebsiteProperties)


def test_website::websiteproperties_constructor_exists():
    assert callable(website::WebsiteProperties.__init__)


def test_website::websiteproperties_constructor_args():
    sig = inspect.signature(website::WebsiteProperties.__init__)
    params = list(sig.parameters.keys())
    assert "baseURL" in params, "Missing parameter 'baseURL'"
    assert "topNavigationId" in params, "Missing parameter 'topNavigationId'"
    assert "metaDescription" in params, "Missing parameter 'metaDescription'"
    assert "frameworkTechnology" in params, "Missing parameter 'frameworkTechnology'"
    assert "webmasterEmail" in params, "Missing parameter 'webmasterEmail'"
    assert "defaultDateFormat" in params, "Missing parameter 'defaultDateFormat'"
    assert "siteTitle" in params, "Missing parameter 'siteTitle'"
    assert "rewriteURLs" in params, "Missing parameter 'rewriteURLs'"
    assert "defaultTimeFormat" in params, "Missing parameter 'defaultTimeFormat'"
    assert "timestampCreation" in params, "Missing parameter 'timestampCreation'"
    assert "developmentVersion" in params, "Missing parameter 'developmentVersion'"
    assert "ormTechnology" in params, "Missing parameter 'ormTechnology'"
    assert "projectName" in params, "Missing parameter 'projectName'"
    assert "inputTechnology" in params, "Missing parameter 'inputTechnology'"
    assert "databaseHost" in params, "Missing parameter 'databaseHost'"
    assert "responsiveTopMenu" in params, "Missing parameter 'responsiveTopMenu'"
    assert "defaultMaximumUploadSize" in params, "Missing parameter 'defaultMaximumUploadSize'"
    assert "databasePrefix" in params, "Missing parameter 'databasePrefix'"
    assert "timestampUpdates" in params, "Missing parameter 'timestampUpdates'"
    assert "copyrightText" in params, "Missing parameter 'copyrightText'"
    assert "databasePassword" in params, "Missing parameter 'databasePassword'"
    assert "siteTemplate" in params, "Missing parameter 'siteTemplate'"
    assert "databaseTechnology" in params, "Missing parameter 'databaseTechnology'"
    assert "textEditorURL" in params, "Missing parameter 'textEditorURL'"
    assert "defaultDateTimeFormat" in params, "Missing parameter 'defaultDateTimeFormat'"
    assert "testProjectName" in params, "Missing parameter 'testProjectName'"
    assert "databaseName" in params, "Missing parameter 'databaseName'"
    assert "captchaSiteKey" in params, "Missing parameter 'captchaSiteKey'"
    assert "databasePort" in params, "Missing parameter 'databasePort'"
    assert "staticUnitsEditable" in params, "Missing parameter 'staticUnitsEditable'"
    assert "ajaxTechnology" in params, "Missing parameter 'ajaxTechnology'"
    assert "captchaSecretKey" in params, "Missing parameter 'captchaSecretKey'"
    assert "databaseUsername" in params, "Missing parameter 'databaseUsername'"

def test_website::websiteproperties_has_baseURL():
    assert hasattr(website::WebsiteProperties, "baseURL")
    descriptor = None
    for klass in website::WebsiteProperties.__mro__:
        if "baseURL" in klass.__dict__:
            descriptor = klass.__dict__["baseURL"]
            break
    assert isinstance(descriptor, property)

def test_website::websiteproperties_has_topNavigationId():
    assert hasattr(website::WebsiteProperties, "topNavigationId")
    descriptor = None
    for klass in website::WebsiteProperties.__mro__:
        if "topNavigationId" in klass.__dict__:
            descriptor = klass.__dict__["topNavigationId"]
            break
    assert isinstance(descriptor, property)

def test_website::websiteproperties_has_metaDescription():
    assert hasattr(website::WebsiteProperties, "metaDescription")
    descriptor = None
    for klass in website::WebsiteProperties.__mro__:
        if "metaDescription" in klass.__dict__:
            descriptor = klass.__dict__["metaDescription"]
            break
    assert isinstance(descriptor, property)

def test_website::websiteproperties_has_frameworkTechnology():
    assert hasattr(website::WebsiteProperties, "frameworkTechnology")
    descriptor = None
    for klass in website::WebsiteProperties.__mro__:
        if "frameworkTechnology" in klass.__dict__:
            descriptor = klass.__dict__["frameworkTechnology"]
            break
    assert isinstance(descriptor, property)

def test_website::websiteproperties_has_webmasterEmail():
    assert hasattr(website::WebsiteProperties, "webmasterEmail")
    descriptor = None
    for klass in website::WebsiteProperties.__mro__:
        if "webmasterEmail" in klass.__dict__:
            descriptor = klass.__dict__["webmasterEmail"]
            break
    assert isinstance(descriptor, property)

def test_website::websiteproperties_has_defaultDateFormat():
    assert hasattr(website::WebsiteProperties, "defaultDateFormat")
    descriptor = None
    for klass in website::WebsiteProperties.__mro__:
        if "defaultDateFormat" in klass.__dict__:
            descriptor = klass.__dict__["defaultDateFormat"]
            break
    assert isinstance(descriptor, property)

def test_website::websiteproperties_has_siteTitle():
    assert hasattr(website::WebsiteProperties, "siteTitle")
    descriptor = None
    for klass in website::WebsiteProperties.__mro__:
        if "siteTitle" in klass.__dict__:
            descriptor = klass.__dict__["siteTitle"]
            break
    assert isinstance(descriptor, property)

def test_website::websiteproperties_has_rewriteURLs():
    assert hasattr(website::WebsiteProperties, "rewriteURLs")
    descriptor = None
    for klass in website::WebsiteProperties.__mro__:
        if "rewriteURLs" in klass.__dict__:
            descriptor = klass.__dict__["rewriteURLs"]
            break
    assert isinstance(descriptor, property)

def test_website::websiteproperties_has_defaultTimeFormat():
    assert hasattr(website::WebsiteProperties, "defaultTimeFormat")
    descriptor = None
    for klass in website::WebsiteProperties.__mro__:
        if "defaultTimeFormat" in klass.__dict__:
            descriptor = klass.__dict__["defaultTimeFormat"]
            break
    assert isinstance(descriptor, property)

def test_website::websiteproperties_has_timestampCreation():
    assert hasattr(website::WebsiteProperties, "timestampCreation")
    descriptor = None
    for klass in website::WebsiteProperties.__mro__:
        if "timestampCreation" in klass.__dict__:
            descriptor = klass.__dict__["timestampCreation"]
            break
    assert isinstance(descriptor, property)

def test_website::websiteproperties_has_developmentVersion():
    assert hasattr(website::WebsiteProperties, "developmentVersion")
    descriptor = None
    for klass in website::WebsiteProperties.__mro__:
        if "developmentVersion" in klass.__dict__:
            descriptor = klass.__dict__["developmentVersion"]
            break
    assert isinstance(descriptor, property)

def test_website::websiteproperties_has_ormTechnology():
    assert hasattr(website::WebsiteProperties, "ormTechnology")
    descriptor = None
    for klass in website::WebsiteProperties.__mro__:
        if "ormTechnology" in klass.__dict__:
            descriptor = klass.__dict__["ormTechnology"]
            break
    assert isinstance(descriptor, property)

def test_website::websiteproperties_has_projectName():
    assert hasattr(website::WebsiteProperties, "projectName")
    descriptor = None
    for klass in website::WebsiteProperties.__mro__:
        if "projectName" in klass.__dict__:
            descriptor = klass.__dict__["projectName"]
            break
    assert isinstance(descriptor, property)

def test_website::websiteproperties_has_inputTechnology():
    assert hasattr(website::WebsiteProperties, "inputTechnology")
    descriptor = None
    for klass in website::WebsiteProperties.__mro__:
        if "inputTechnology" in klass.__dict__:
            descriptor = klass.__dict__["inputTechnology"]
            break
    assert isinstance(descriptor, property)

def test_website::websiteproperties_has_databaseHost():
    assert hasattr(website::WebsiteProperties, "databaseHost")
    descriptor = None
    for klass in website::WebsiteProperties.__mro__:
        if "databaseHost" in klass.__dict__:
            descriptor = klass.__dict__["databaseHost"]
            break
    assert isinstance(descriptor, property)

def test_website::websiteproperties_has_responsiveTopMenu():
    assert hasattr(website::WebsiteProperties, "responsiveTopMenu")
    descriptor = None
    for klass in website::WebsiteProperties.__mro__:
        if "responsiveTopMenu" in klass.__dict__:
            descriptor = klass.__dict__["responsiveTopMenu"]
            break
    assert isinstance(descriptor, property)

def test_website::websiteproperties_has_defaultMaximumUploadSize():
    assert hasattr(website::WebsiteProperties, "defaultMaximumUploadSize")
    descriptor = None
    for klass in website::WebsiteProperties.__mro__:
        if "defaultMaximumUploadSize" in klass.__dict__:
            descriptor = klass.__dict__["defaultMaximumUploadSize"]
            break
    assert isinstance(descriptor, property)

def test_website::websiteproperties_has_databasePrefix():
    assert hasattr(website::WebsiteProperties, "databasePrefix")
    descriptor = None
    for klass in website::WebsiteProperties.__mro__:
        if "databasePrefix" in klass.__dict__:
            descriptor = klass.__dict__["databasePrefix"]
            break
    assert isinstance(descriptor, property)

def test_website::websiteproperties_has_timestampUpdates():
    assert hasattr(website::WebsiteProperties, "timestampUpdates")
    descriptor = None
    for klass in website::WebsiteProperties.__mro__:
        if "timestampUpdates" in klass.__dict__:
            descriptor = klass.__dict__["timestampUpdates"]
            break
    assert isinstance(descriptor, property)

def test_website::websiteproperties_has_copyrightText():
    assert hasattr(website::WebsiteProperties, "copyrightText")
    descriptor = None
    for klass in website::WebsiteProperties.__mro__:
        if "copyrightText" in klass.__dict__:
            descriptor = klass.__dict__["copyrightText"]
            break
    assert isinstance(descriptor, property)

def test_website::websiteproperties_has_databasePassword():
    assert hasattr(website::WebsiteProperties, "databasePassword")
    descriptor = None
    for klass in website::WebsiteProperties.__mro__:
        if "databasePassword" in klass.__dict__:
            descriptor = klass.__dict__["databasePassword"]
            break
    assert isinstance(descriptor, property)

def test_website::websiteproperties_has_siteTemplate():
    assert hasattr(website::WebsiteProperties, "siteTemplate")
    descriptor = None
    for klass in website::WebsiteProperties.__mro__:
        if "siteTemplate" in klass.__dict__:
            descriptor = klass.__dict__["siteTemplate"]
            break
    assert isinstance(descriptor, property)

def test_website::websiteproperties_has_databaseTechnology():
    assert hasattr(website::WebsiteProperties, "databaseTechnology")
    descriptor = None
    for klass in website::WebsiteProperties.__mro__:
        if "databaseTechnology" in klass.__dict__:
            descriptor = klass.__dict__["databaseTechnology"]
            break
    assert isinstance(descriptor, property)

def test_website::websiteproperties_has_textEditorURL():
    assert hasattr(website::WebsiteProperties, "textEditorURL")
    descriptor = None
    for klass in website::WebsiteProperties.__mro__:
        if "textEditorURL" in klass.__dict__:
            descriptor = klass.__dict__["textEditorURL"]
            break
    assert isinstance(descriptor, property)

def test_website::websiteproperties_has_defaultDateTimeFormat():
    assert hasattr(website::WebsiteProperties, "defaultDateTimeFormat")
    descriptor = None
    for klass in website::WebsiteProperties.__mro__:
        if "defaultDateTimeFormat" in klass.__dict__:
            descriptor = klass.__dict__["defaultDateTimeFormat"]
            break
    assert isinstance(descriptor, property)

def test_website::websiteproperties_has_testProjectName():
    assert hasattr(website::WebsiteProperties, "testProjectName")
    descriptor = None
    for klass in website::WebsiteProperties.__mro__:
        if "testProjectName" in klass.__dict__:
            descriptor = klass.__dict__["testProjectName"]
            break
    assert isinstance(descriptor, property)

def test_website::websiteproperties_has_databaseName():
    assert hasattr(website::WebsiteProperties, "databaseName")
    descriptor = None
    for klass in website::WebsiteProperties.__mro__:
        if "databaseName" in klass.__dict__:
            descriptor = klass.__dict__["databaseName"]
            break
    assert isinstance(descriptor, property)

def test_website::websiteproperties_has_captchaSiteKey():
    assert hasattr(website::WebsiteProperties, "captchaSiteKey")
    descriptor = None
    for klass in website::WebsiteProperties.__mro__:
        if "captchaSiteKey" in klass.__dict__:
            descriptor = klass.__dict__["captchaSiteKey"]
            break
    assert isinstance(descriptor, property)

def test_website::websiteproperties_has_databasePort():
    assert hasattr(website::WebsiteProperties, "databasePort")
    descriptor = None
    for klass in website::WebsiteProperties.__mro__:
        if "databasePort" in klass.__dict__:
            descriptor = klass.__dict__["databasePort"]
            break
    assert isinstance(descriptor, property)

def test_website::websiteproperties_has_staticUnitsEditable():
    assert hasattr(website::WebsiteProperties, "staticUnitsEditable")
    descriptor = None
    for klass in website::WebsiteProperties.__mro__:
        if "staticUnitsEditable" in klass.__dict__:
            descriptor = klass.__dict__["staticUnitsEditable"]
            break
    assert isinstance(descriptor, property)

def test_website::websiteproperties_has_ajaxTechnology():
    assert hasattr(website::WebsiteProperties, "ajaxTechnology")
    descriptor = None
    for klass in website::WebsiteProperties.__mro__:
        if "ajaxTechnology" in klass.__dict__:
            descriptor = klass.__dict__["ajaxTechnology"]
            break
    assert isinstance(descriptor, property)

def test_website::websiteproperties_has_captchaSecretKey():
    assert hasattr(website::WebsiteProperties, "captchaSecretKey")
    descriptor = None
    for klass in website::WebsiteProperties.__mro__:
        if "captchaSecretKey" in klass.__dict__:
            descriptor = klass.__dict__["captchaSecretKey"]
            break
    assert isinstance(descriptor, property)

def test_website::websiteproperties_has_databaseUsername():
    assert hasattr(website::WebsiteProperties, "databaseUsername")
    descriptor = None
    for klass in website::WebsiteProperties.__mro__:
        if "databaseUsername" in klass.__dict__:
            descriptor = klass.__dict__["databaseUsername"]
            break
    assert isinstance(descriptor, property)



def test_website::webgenmodel_is_not_abstract():
    assert not inspect.isabstract(website::WebGenModel)


def test_website::webgenmodel_constructor_exists():
    assert callable(website::WebGenModel.__init__)


def test_website::webgenmodel_constructor_args():
    sig = inspect.signature(website::WebGenModel.__init__)
    params = list(sig.parameters.keys())



def test_imageunit_is_not_abstract():
    assert not inspect.isabstract(ImageUnit)


def test_imageunit_constructor_exists():
    assert callable(ImageUnit.__init__)


def test_imageunit_constructor_args():
    sig = inspect.signature(ImageUnit.__init__)
    params = list(sig.parameters.keys())



def test_website::sliderunit_is_not_abstract():
    assert not inspect.isabstract(website::SliderUnit)


def test_website::sliderunit_constructor_exists():
    assert callable(website::SliderUnit.__init__)


def test_website::sliderunit_constructor_args():
    sig = inspect.signature(website::SliderUnit.__init__)
    params = list(sig.parameters.keys())
    assert "styleClass" in params, "Missing parameter 'styleClass'"
    assert "contentClass" in params, "Missing parameter 'contentClass'"

def test_website::sliderunit_has_styleClass():
    assert hasattr(website::SliderUnit, "styleClass")
    descriptor = None
    for klass in website::SliderUnit.__mro__:
        if "styleClass" in klass.__dict__:
            descriptor = klass.__dict__["styleClass"]
            break
    assert isinstance(descriptor, property)

def test_website::sliderunit_has_contentClass():
    assert hasattr(website::SliderUnit, "contentClass")
    descriptor = None
    for klass in website::SliderUnit.__mro__:
        if "contentClass" in klass.__dict__:
            descriptor = klass.__dict__["contentClass"]
            break
    assert isinstance(descriptor, property)



def test_website::galleryunit_is_not_abstract():
    assert not inspect.isabstract(website::GalleryUnit)


def test_website::galleryunit_constructor_exists():
    assert callable(website::GalleryUnit.__init__)


def test_website::galleryunit_constructor_args():
    sig = inspect.signature(website::GalleryUnit.__init__)
    params = list(sig.parameters.keys())
    assert "contentClass" in params, "Missing parameter 'contentClass'"
    assert "styleClass" in params, "Missing parameter 'styleClass'"

def test_website::galleryunit_has_contentClass():
    assert hasattr(website::GalleryUnit, "contentClass")
    descriptor = None
    for klass in website::GalleryUnit.__mro__:
        if "contentClass" in klass.__dict__:
            descriptor = klass.__dict__["contentClass"]
            break
    assert isinstance(descriptor, property)

def test_website::galleryunit_has_styleClass():
    assert hasattr(website::GalleryUnit, "styleClass")
    descriptor = None
    for klass in website::GalleryUnit.__mro__:
        if "styleClass" in klass.__dict__:
            descriptor = klass.__dict__["styleClass"]
            break
    assert isinstance(descriptor, property)



def test_inlineaction_is_not_abstract():
    assert not inspect.isabstract(InlineAction)


def test_inlineaction_constructor_exists():
    assert callable(InlineAction.__init__)


def test_inlineaction_constructor_args():
    sig = inspect.signature(InlineAction.__init__)
    params = list(sig.parameters.keys())



def test_website::featuresupportaction_is_not_abstract():
    assert not inspect.isabstract(website::FeatureSupportAction)


def test_website::featuresupportaction_constructor_exists():
    assert callable(website::FeatureSupportAction.__init__)


def test_website::featuresupportaction_constructor_args():
    sig = inspect.signature(website::FeatureSupportAction.__init__)
    params = list(sig.parameters.keys())
    assert "confirmMessage" in params, "Missing parameter 'confirmMessage'"
    assert "fileExtension" in params, "Missing parameter 'fileExtension'"
    assert "uriElement" in params, "Missing parameter 'uriElement'"

def test_website::featuresupportaction_has_confirmMessage():
    assert hasattr(website::FeatureSupportAction, "confirmMessage")
    descriptor = None
    for klass in website::FeatureSupportAction.__mro__:
        if "confirmMessage" in klass.__dict__:
            descriptor = klass.__dict__["confirmMessage"]
            break
    assert isinstance(descriptor, property)

def test_website::featuresupportaction_has_fileExtension():
    assert hasattr(website::FeatureSupportAction, "fileExtension")
    descriptor = None
    for klass in website::FeatureSupportAction.__mro__:
        if "fileExtension" in klass.__dict__:
            descriptor = klass.__dict__["fileExtension"]
            break
    assert isinstance(descriptor, property)

def test_website::featuresupportaction_has_uriElement():
    assert hasattr(website::FeatureSupportAction, "uriElement")
    descriptor = None
    for klass in website::FeatureSupportAction.__mro__:
        if "uriElement" in klass.__dict__:
            descriptor = klass.__dict__["uriElement"]
            break
    assert isinstance(descriptor, property)



def test_website::deleteaction_is_not_abstract():
    assert not inspect.isabstract(website::DeleteAction)


def test_website::deleteaction_constructor_exists():
    assert callable(website::DeleteAction.__init__)


def test_website::deleteaction_constructor_args():
    sig = inspect.signature(website::DeleteAction.__init__)
    params = list(sig.parameters.keys())
    assert "confirmMessage" in params, "Missing parameter 'confirmMessage'"
    assert "uriElement" in params, "Missing parameter 'uriElement'"

def test_website::deleteaction_has_confirmMessage():
    assert hasattr(website::DeleteAction, "confirmMessage")
    descriptor = None
    for klass in website::DeleteAction.__mro__:
        if "confirmMessage" in klass.__dict__:
            descriptor = klass.__dict__["confirmMessage"]
            break
    assert isinstance(descriptor, property)

def test_website::deleteaction_has_uriElement():
    assert hasattr(website::DeleteAction, "uriElement")
    descriptor = None
    for klass in website::DeleteAction.__mro__:
        if "uriElement" in klass.__dict__:
            descriptor = klass.__dict__["uriElement"]
            break
    assert isinstance(descriptor, property)



def test_website::selectaction_is_not_abstract():
    assert not inspect.isabstract(website::SelectAction)


def test_website::selectaction_constructor_exists():
    assert callable(website::SelectAction.__init__)


def test_website::selectaction_constructor_args():
    sig = inspect.signature(website::SelectAction.__init__)
    params = list(sig.parameters.keys())



def test_childpath_is_not_abstract():
    assert not inspect.isabstract(ChildPath)


def test_childpath_constructor_exists():
    assert callable(ChildPath.__init__)


def test_childpath_constructor_args():
    sig = inspect.signature(ChildPath.__init__)
    params = list(sig.parameters.keys())



def test_website::childpathattribute_is_not_abstract():
    assert not inspect.isabstract(website::ChildPathAttribute)


def test_website::childpathattribute_constructor_exists():
    assert callable(website::ChildPathAttribute.__init__)


def test_website::childpathattribute_constructor_args():
    sig = inspect.signature(website::ChildPathAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_website::childpathattribute_has_name():
    assert hasattr(website::ChildPathAttribute, "name")
    descriptor = None
    for klass in website::ChildPathAttribute.__mro__:
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



def test_website::featurepathattribute_is_not_abstract():
    assert not inspect.isabstract(website::FeaturePathAttribute)


def test_website::featurepathattribute_constructor_exists():
    assert callable(website::FeaturePathAttribute.__init__)


def test_website::featurepathattribute_constructor_args():
    sig = inspect.signature(website::FeaturePathAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_website::featurepathattribute_has_name():
    assert hasattr(website::FeaturePathAttribute, "name")
    descriptor = None
    for klass in website::FeaturePathAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_website::featurepath_is_not_abstract():
    assert not inspect.isabstract(website::FeaturePath)


def test_website::featurepath_constructor_exists():
    assert callable(website::FeaturePath.__init__)


def test_website::featurepath_constructor_args():
    sig = inspect.signature(website::FeaturePath.__init__)
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



def test_website::loginunit_is_not_abstract():
    assert not inspect.isabstract(website::LoginUnit)


def test_website::loginunit_constructor_exists():
    assert callable(website::LoginUnit.__init__)


def test_website::loginunit_constructor_args():
    sig = inspect.signature(website::LoginUnit.__init__)
    params = list(sig.parameters.keys())
    assert "styleClass" in params, "Missing parameter 'styleClass'"
    assert "logoutUriElement" in params, "Missing parameter 'logoutUriElement'"

def test_website::loginunit_has_styleClass():
    assert hasattr(website::LoginUnit, "styleClass")
    descriptor = None
    for klass in website::LoginUnit.__mro__:
        if "styleClass" in klass.__dict__:
            descriptor = klass.__dict__["styleClass"]
            break
    assert isinstance(descriptor, property)

def test_website::loginunit_has_logoutUriElement():
    assert hasattr(website::LoginUnit, "logoutUriElement")
    descriptor = None
    for klass in website::LoginUnit.__mro__:
        if "logoutUriElement" in klass.__dict__:
            descriptor = klass.__dict__["logoutUriElement"]
            break
    assert isinstance(descriptor, property)



def test_website::registrationunit_is_not_abstract():
    assert not inspect.isabstract(website::RegistrationUnit)


def test_website::registrationunit_constructor_exists():
    assert callable(website::RegistrationUnit.__init__)


def test_website::registrationunit_constructor_args():
    sig = inspect.signature(website::RegistrationUnit.__init__)
    params = list(sig.parameters.keys())
    assert "styleClass" in params, "Missing parameter 'styleClass'"

def test_website::registrationunit_has_styleClass():
    assert hasattr(website::RegistrationUnit, "styleClass")
    descriptor = None
    for klass in website::RegistrationUnit.__mro__:
        if "styleClass" in klass.__dict__:
            descriptor = klass.__dict__["styleClass"]
            break
    assert isinstance(descriptor, property)



def test_website::forgottenpasswordunit_is_not_abstract():
    assert not inspect.isabstract(website::ForgottenPasswordUnit)


def test_website::forgottenpasswordunit_constructor_exists():
    assert callable(website::ForgottenPasswordUnit.__init__)


def test_website::forgottenpasswordunit_constructor_args():
    sig = inspect.signature(website::ForgottenPasswordUnit.__init__)
    params = list(sig.parameters.keys())
    assert "styleClass" in params, "Missing parameter 'styleClass'"

def test_website::forgottenpasswordunit_has_styleClass():
    assert hasattr(website::ForgottenPasswordUnit, "styleClass")
    descriptor = None
    for klass in website::ForgottenPasswordUnit.__mro__:
        if "styleClass" in klass.__dict__:
            descriptor = klass.__dict__["styleClass"]
            break
    assert isinstance(descriptor, property)



def test_website::searchunit_is_not_abstract():
    assert not inspect.isabstract(website::SearchUnit)


def test_website::searchunit_constructor_exists():
    assert callable(website::SearchUnit.__init__)


def test_website::searchunit_constructor_args():
    sig = inspect.signature(website::SearchUnit.__init__)
    params = list(sig.parameters.keys())
    assert "styleClass" in params, "Missing parameter 'styleClass'"

def test_website::searchunit_has_styleClass():
    assert hasattr(website::SearchUnit, "styleClass")
    descriptor = None
    for klass in website::SearchUnit.__mro__:
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



def test_website::imageunit_is_not_abstract():
    assert not inspect.isabstract(website::ImageUnit)


def test_website::imageunit_constructor_exists():
    assert callable(website::ImageUnit.__init__)


def test_website::imageunit_constructor_args():
    sig = inspect.signature(website::ImageUnit.__init__)
    params = list(sig.parameters.keys())
    assert "transitionTime" in params, "Missing parameter 'transitionTime'"
    assert "missingImagePath" in params, "Missing parameter 'missingImagePath'"
    assert "showTime" in params, "Missing parameter 'showTime'"

def test_website::imageunit_has_transitionTime():
    assert hasattr(website::ImageUnit, "transitionTime")
    descriptor = None
    for klass in website::ImageUnit.__mro__:
        if "transitionTime" in klass.__dict__:
            descriptor = klass.__dict__["transitionTime"]
            break
    assert isinstance(descriptor, property)

def test_website::imageunit_has_missingImagePath():
    assert hasattr(website::ImageUnit, "missingImagePath")
    descriptor = None
    for klass in website::ImageUnit.__mro__:
        if "missingImagePath" in klass.__dict__:
            descriptor = klass.__dict__["missingImagePath"]
            break
    assert isinstance(descriptor, property)

def test_website::imageunit_has_showTime():
    assert hasattr(website::ImageUnit, "showTime")
    descriptor = None
    for klass in website::ImageUnit.__mro__:
        if "showTime" in klass.__dict__:
            descriptor = klass.__dict__["showTime"]
            break
    assert isinstance(descriptor, property)



def test_website::dataunit_is_not_abstract():
    assert not inspect.isabstract(website::DataUnit)


def test_website::dataunit_constructor_exists():
    assert callable(website::DataUnit.__init__)


def test_website::dataunit_constructor_args():
    sig = inspect.signature(website::DataUnit.__init__)
    params = list(sig.parameters.keys())



def test_website::controlunit_is_not_abstract():
    assert not inspect.isabstract(website::ControlUnit)


def test_website::controlunit_constructor_exists():
    assert callable(website::ControlUnit.__init__)


def test_website::controlunit_constructor_args():
    sig = inspect.signature(website::ControlUnit.__init__)
    params = list(sig.parameters.keys())
    assert "submitLabel" in params, "Missing parameter 'submitLabel'"
    assert "cancelLabel" in params, "Missing parameter 'cancelLabel'"
    assert "contentClass" in params, "Missing parameter 'contentClass'"

def test_website::controlunit_has_submitLabel():
    assert hasattr(website::ControlUnit, "submitLabel")
    descriptor = None
    for klass in website::ControlUnit.__mro__:
        if "submitLabel" in klass.__dict__:
            descriptor = klass.__dict__["submitLabel"]
            break
    assert isinstance(descriptor, property)

def test_website::controlunit_has_cancelLabel():
    assert hasattr(website::ControlUnit, "cancelLabel")
    descriptor = None
    for klass in website::ControlUnit.__mro__:
        if "cancelLabel" in klass.__dict__:
            descriptor = klass.__dict__["cancelLabel"]
            break
    assert isinstance(descriptor, property)

def test_website::controlunit_has_contentClass():
    assert hasattr(website::ControlUnit, "contentClass")
    descriptor = None
    for klass in website::ControlUnit.__mro__:
        if "contentClass" in klass.__dict__:
            descriptor = klass.__dict__["contentClass"]
            break
    assert isinstance(descriptor, property)



def test_website::editunit_is_not_abstract():
    assert not inspect.isabstract(website::EditUnit)


def test_website::editunit_constructor_exists():
    assert callable(website::EditUnit.__init__)


def test_website::editunit_constructor_args():
    sig = inspect.signature(website::EditUnit.__init__)
    params = list(sig.parameters.keys())
    assert "cancelLabel" in params, "Missing parameter 'cancelLabel'"
    assert "confirmLabel" in params, "Missing parameter 'confirmLabel'"
    assert "contentClass" in params, "Missing parameter 'contentClass'"
    assert "customiseValues" in params, "Missing parameter 'customiseValues'"

def test_website::editunit_has_cancelLabel():
    assert hasattr(website::EditUnit, "cancelLabel")
    descriptor = None
    for klass in website::EditUnit.__mro__:
        if "cancelLabel" in klass.__dict__:
            descriptor = klass.__dict__["cancelLabel"]
            break
    assert isinstance(descriptor, property)

def test_website::editunit_has_confirmLabel():
    assert hasattr(website::EditUnit, "confirmLabel")
    descriptor = None
    for klass in website::EditUnit.__mro__:
        if "confirmLabel" in klass.__dict__:
            descriptor = klass.__dict__["confirmLabel"]
            break
    assert isinstance(descriptor, property)

def test_website::editunit_has_contentClass():
    assert hasattr(website::EditUnit, "contentClass")
    descriptor = None
    for klass in website::EditUnit.__mro__:
        if "contentClass" in klass.__dict__:
            descriptor = klass.__dict__["contentClass"]
            break
    assert isinstance(descriptor, property)

def test_website::editunit_has_customiseValues():
    assert hasattr(website::EditUnit, "customiseValues")
    descriptor = None
    for klass in website::EditUnit.__mro__:
        if "customiseValues" in klass.__dict__:
            descriptor = klass.__dict__["customiseValues"]
            break
    assert isinstance(descriptor, property)



def test_editunit_is_not_abstract():
    assert not inspect.isabstract(EditUnit)


def test_editunit_constructor_exists():
    assert callable(EditUnit.__init__)


def test_editunit_constructor_args():
    sig = inspect.signature(EditUnit.__init__)
    params = list(sig.parameters.keys())



def test_website::createunit_is_not_abstract():
    assert not inspect.isabstract(website::CreateUnit)


def test_website::createunit_constructor_exists():
    assert callable(website::CreateUnit.__init__)


def test_website::createunit_constructor_args():
    sig = inspect.signature(website::CreateUnit.__init__)
    params = list(sig.parameters.keys())
    assert "styleClass" in params, "Missing parameter 'styleClass'"

def test_website::createunit_has_styleClass():
    assert hasattr(website::CreateUnit, "styleClass")
    descriptor = None
    for klass in website::CreateUnit.__mro__:
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



def test_website::datefield_is_not_abstract():
    assert not inspect.isabstract(website::DateField)


def test_website::datefield_constructor_exists():
    assert callable(website::DateField.__init__)


def test_website::datefield_constructor_args():
    sig = inspect.signature(website::DateField.__init__)
    params = list(sig.parameters.keys())
    assert "details" in params, "Missing parameter 'details'"
    assert "format" in params, "Missing parameter 'format'"

def test_website::datefield_has_details():
    assert hasattr(website::DateField, "details")
    descriptor = None
    for klass in website::DateField.__mro__:
        if "details" in klass.__dict__:
            descriptor = klass.__dict__["details"]
            break
    assert isinstance(descriptor, property)

def test_website::datefield_has_format():
    assert hasattr(website::DateField, "format")
    descriptor = None
    for klass in website::DateField.__mro__:
        if "format" in klass.__dict__:
            descriptor = klass.__dict__["format"]
            break
    assert isinstance(descriptor, property)



def test_website::datatypefield_is_not_abstract():
    assert not inspect.isabstract(website::DataTypeField)


def test_website::datatypefield_constructor_exists():
    assert callable(website::DataTypeField.__init__)


def test_website::datatypefield_constructor_args():
    sig = inspect.signature(website::DataTypeField.__init__)
    params = list(sig.parameters.keys())
    assert "obfuscateFormFields" in params, "Missing parameter 'obfuscateFormFields'"
    assert "encrypt" in params, "Missing parameter 'encrypt'"
    assert "interfaceType" in params, "Missing parameter 'interfaceType'"

def test_website::datatypefield_has_obfuscateFormFields():
    assert hasattr(website::DataTypeField, "obfuscateFormFields")
    descriptor = None
    for klass in website::DataTypeField.__mro__:
        if "obfuscateFormFields" in klass.__dict__:
            descriptor = klass.__dict__["obfuscateFormFields"]
            break
    assert isinstance(descriptor, property)

def test_website::datatypefield_has_encrypt():
    assert hasattr(website::DataTypeField, "encrypt")
    descriptor = None
    for klass in website::DataTypeField.__mro__:
        if "encrypt" in klass.__dict__:
            descriptor = klass.__dict__["encrypt"]
            break
    assert isinstance(descriptor, property)

def test_website::datatypefield_has_interfaceType():
    assert hasattr(website::DataTypeField, "interfaceType")
    descriptor = None
    for klass in website::DataTypeField.__mro__:
        if "interfaceType" in klass.__dict__:
            descriptor = klass.__dict__["interfaceType"]
            break
    assert isinstance(descriptor, property)



def test_website::childpath_is_not_abstract():
    assert not inspect.isabstract(website::ChildPath)


def test_website::childpath_constructor_exists():
    assert callable(website::ChildPath.__init__)


def test_website::childpath_constructor_args():
    sig = inspect.signature(website::ChildPath.__init__)
    params = list(sig.parameters.keys())



def test_website::associationreference_is_not_abstract():
    assert not inspect.isabstract(website::AssociationReference)


def test_website::associationreference_constructor_exists():
    assert callable(website::AssociationReference.__init__)


def test_website::associationreference_constructor_args():
    sig = inspect.signature(website::AssociationReference.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_website::associationreference_has_name():
    assert hasattr(website::AssociationReference, "name")
    descriptor = None
    for klass in website::AssociationReference.__mro__:
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



def test_website::createupdateunit_is_not_abstract():
    assert not inspect.isabstract(website::CreateUpdateUnit)


def test_website::createupdateunit_constructor_exists():
    assert callable(website::CreateUpdateUnit.__init__)


def test_website::createupdateunit_constructor_args():
    sig = inspect.signature(website::CreateUpdateUnit.__init__)
    params = list(sig.parameters.keys())
    assert "createUriElement" in params, "Missing parameter 'createUriElement'"
    assert "clearLabel" in params, "Missing parameter 'clearLabel'"
    assert "styleClass" in params, "Missing parameter 'styleClass'"

def test_website::createupdateunit_has_createUriElement():
    assert hasattr(website::CreateUpdateUnit, "createUriElement")
    descriptor = None
    for klass in website::CreateUpdateUnit.__mro__:
        if "createUriElement" in klass.__dict__:
            descriptor = klass.__dict__["createUriElement"]
            break
    assert isinstance(descriptor, property)

def test_website::createupdateunit_has_clearLabel():
    assert hasattr(website::CreateUpdateUnit, "clearLabel")
    descriptor = None
    for klass in website::CreateUpdateUnit.__mro__:
        if "clearLabel" in klass.__dict__:
            descriptor = klass.__dict__["clearLabel"]
            break
    assert isinstance(descriptor, property)

def test_website::createupdateunit_has_styleClass():
    assert hasattr(website::CreateUpdateUnit, "styleClass")
    descriptor = None
    for klass in website::CreateUpdateUnit.__mro__:
        if "styleClass" in klass.__dict__:
            descriptor = klass.__dict__["styleClass"]
            break
    assert isinstance(descriptor, property)



def test_website::mapunit_is_not_abstract():
    assert not inspect.isabstract(website::MapUnit)


def test_website::mapunit_constructor_exists():
    assert callable(website::MapUnit.__init__)


def test_website::mapunit_constructor_args():
    sig = inspect.signature(website::MapUnit.__init__)
    params = list(sig.parameters.keys())
    assert "defaultZoomLevel" in params, "Missing parameter 'defaultZoomLevel'"
    assert "styleClass" in params, "Missing parameter 'styleClass'"
    assert "readOnly" in params, "Missing parameter 'readOnly'"

def test_website::mapunit_has_defaultZoomLevel():
    assert hasattr(website::MapUnit, "defaultZoomLevel")
    descriptor = None
    for klass in website::MapUnit.__mro__:
        if "defaultZoomLevel" in klass.__dict__:
            descriptor = klass.__dict__["defaultZoomLevel"]
            break
    assert isinstance(descriptor, property)

def test_website::mapunit_has_styleClass():
    assert hasattr(website::MapUnit, "styleClass")
    descriptor = None
    for klass in website::MapUnit.__mro__:
        if "styleClass" in klass.__dict__:
            descriptor = klass.__dict__["styleClass"]
            break
    assert isinstance(descriptor, property)

def test_website::mapunit_has_readOnly():
    assert hasattr(website::MapUnit, "readOnly")
    descriptor = None
    for klass in website::MapUnit.__mro__:
        if "readOnly" in klass.__dict__:
            descriptor = klass.__dict__["readOnly"]
            break
    assert isinstance(descriptor, property)



def test_website::updateunit_is_not_abstract():
    assert not inspect.isabstract(website::UpdateUnit)


def test_website::updateunit_constructor_exists():
    assert callable(website::UpdateUnit.__init__)


def test_website::updateunit_constructor_args():
    sig = inspect.signature(website::UpdateUnit.__init__)
    params = list(sig.parameters.keys())
    assert "styleClass" in params, "Missing parameter 'styleClass'"

def test_website::updateunit_has_styleClass():
    assert hasattr(website::UpdateUnit, "styleClass")
    descriptor = None
    for klass in website::UpdateUnit.__mro__:
        if "styleClass" in klass.__dict__:
            descriptor = klass.__dict__["styleClass"]
            break
    assert isinstance(descriptor, property)



def test_website::detailsunit_is_not_abstract():
    assert not inspect.isabstract(website::DetailsUnit)


def test_website::detailsunit_constructor_exists():
    assert callable(website::DetailsUnit.__init__)


def test_website::detailsunit_constructor_args():
    sig = inspect.signature(website::DetailsUnit.__init__)
    params = list(sig.parameters.keys())
    assert "onlyDisplayWhenNotEmpty" in params, "Missing parameter 'onlyDisplayWhenNotEmpty'"
    assert "omitFieldLabels" in params, "Missing parameter 'omitFieldLabels'"
    assert "contentClass" in params, "Missing parameter 'contentClass'"
    assert "styleClass" in params, "Missing parameter 'styleClass'"

def test_website::detailsunit_has_onlyDisplayWhenNotEmpty():
    assert hasattr(website::DetailsUnit, "onlyDisplayWhenNotEmpty")
    descriptor = None
    for klass in website::DetailsUnit.__mro__:
        if "onlyDisplayWhenNotEmpty" in klass.__dict__:
            descriptor = klass.__dict__["onlyDisplayWhenNotEmpty"]
            break
    assert isinstance(descriptor, property)

def test_website::detailsunit_has_omitFieldLabels():
    assert hasattr(website::DetailsUnit, "omitFieldLabels")
    descriptor = None
    for klass in website::DetailsUnit.__mro__:
        if "omitFieldLabels" in klass.__dict__:
            descriptor = klass.__dict__["omitFieldLabels"]
            break
    assert isinstance(descriptor, property)

def test_website::detailsunit_has_contentClass():
    assert hasattr(website::DetailsUnit, "contentClass")
    descriptor = None
    for klass in website::DetailsUnit.__mro__:
        if "contentClass" in klass.__dict__:
            descriptor = klass.__dict__["contentClass"]
            break
    assert isinstance(descriptor, property)

def test_website::detailsunit_has_styleClass():
    assert hasattr(website::DetailsUnit, "styleClass")
    descriptor = None
    for klass in website::DetailsUnit.__mro__:
        if "styleClass" in klass.__dict__:
            descriptor = klass.__dict__["styleClass"]
            break
    assert isinstance(descriptor, property)



def test_website::collectionunit_is_not_abstract():
    assert not inspect.isabstract(website::CollectionUnit)


def test_website::collectionunit_constructor_exists():
    assert callable(website::CollectionUnit.__init__)


def test_website::collectionunit_constructor_args():
    sig = inspect.signature(website::CollectionUnit.__init__)
    params = list(sig.parameters.keys())
    assert "nextNpages" in params, "Missing parameter 'nextNpages'"
    assert "firstPageLabel" in params, "Missing parameter 'firstPageLabel'"
    assert "useDisabledPageLinks" in params, "Missing parameter 'useDisabledPageLinks'"
    assert "defaultPaginationSize" in params, "Missing parameter 'defaultPaginationSize'"
    assert "previousNpages" in params, "Missing parameter 'previousNpages'"
    assert "lastPageLabel" in params, "Missing parameter 'lastPageLabel'"
    assert "previousPageLabel" in params, "Missing parameter 'previousPageLabel'"
    assert "nextPageLabel" in params, "Missing parameter 'nextPageLabel'"
    assert "useFirstLastPageLinks" in params, "Missing parameter 'useFirstLastPageLinks'"
    assert "emptyMessage" in params, "Missing parameter 'emptyMessage'"

def test_website::collectionunit_has_nextNpages():
    assert hasattr(website::CollectionUnit, "nextNpages")
    descriptor = None
    for klass in website::CollectionUnit.__mro__:
        if "nextNpages" in klass.__dict__:
            descriptor = klass.__dict__["nextNpages"]
            break
    assert isinstance(descriptor, property)

def test_website::collectionunit_has_firstPageLabel():
    assert hasattr(website::CollectionUnit, "firstPageLabel")
    descriptor = None
    for klass in website::CollectionUnit.__mro__:
        if "firstPageLabel" in klass.__dict__:
            descriptor = klass.__dict__["firstPageLabel"]
            break
    assert isinstance(descriptor, property)

def test_website::collectionunit_has_useDisabledPageLinks():
    assert hasattr(website::CollectionUnit, "useDisabledPageLinks")
    descriptor = None
    for klass in website::CollectionUnit.__mro__:
        if "useDisabledPageLinks" in klass.__dict__:
            descriptor = klass.__dict__["useDisabledPageLinks"]
            break
    assert isinstance(descriptor, property)

def test_website::collectionunit_has_defaultPaginationSize():
    assert hasattr(website::CollectionUnit, "defaultPaginationSize")
    descriptor = None
    for klass in website::CollectionUnit.__mro__:
        if "defaultPaginationSize" in klass.__dict__:
            descriptor = klass.__dict__["defaultPaginationSize"]
            break
    assert isinstance(descriptor, property)

def test_website::collectionunit_has_previousNpages():
    assert hasattr(website::CollectionUnit, "previousNpages")
    descriptor = None
    for klass in website::CollectionUnit.__mro__:
        if "previousNpages" in klass.__dict__:
            descriptor = klass.__dict__["previousNpages"]
            break
    assert isinstance(descriptor, property)

def test_website::collectionunit_has_lastPageLabel():
    assert hasattr(website::CollectionUnit, "lastPageLabel")
    descriptor = None
    for klass in website::CollectionUnit.__mro__:
        if "lastPageLabel" in klass.__dict__:
            descriptor = klass.__dict__["lastPageLabel"]
            break
    assert isinstance(descriptor, property)

def test_website::collectionunit_has_previousPageLabel():
    assert hasattr(website::CollectionUnit, "previousPageLabel")
    descriptor = None
    for klass in website::CollectionUnit.__mro__:
        if "previousPageLabel" in klass.__dict__:
            descriptor = klass.__dict__["previousPageLabel"]
            break
    assert isinstance(descriptor, property)

def test_website::collectionunit_has_nextPageLabel():
    assert hasattr(website::CollectionUnit, "nextPageLabel")
    descriptor = None
    for klass in website::CollectionUnit.__mro__:
        if "nextPageLabel" in klass.__dict__:
            descriptor = klass.__dict__["nextPageLabel"]
            break
    assert isinstance(descriptor, property)

def test_website::collectionunit_has_useFirstLastPageLinks():
    assert hasattr(website::CollectionUnit, "useFirstLastPageLinks")
    descriptor = None
    for klass in website::CollectionUnit.__mro__:
        if "useFirstLastPageLinks" in klass.__dict__:
            descriptor = klass.__dict__["useFirstLastPageLinks"]
            break
    assert isinstance(descriptor, property)

def test_website::collectionunit_has_emptyMessage():
    assert hasattr(website::CollectionUnit, "emptyMessage")
    descriptor = None
    for klass in website::CollectionUnit.__mro__:
        if "emptyMessage" in klass.__dict__:
            descriptor = klass.__dict__["emptyMessage"]
            break
    assert isinstance(descriptor, property)



def test_website::singletonunit_is_not_abstract():
    assert not inspect.isabstract(website::SingletonUnit)


def test_website::singletonunit_constructor_exists():
    assert callable(website::SingletonUnit.__init__)


def test_website::singletonunit_constructor_args():
    sig = inspect.signature(website::SingletonUnit.__init__)
    params = list(sig.parameters.keys())



def test_website::selectableunit_is_not_abstract():
    assert not inspect.isabstract(website::SelectableUnit)


def test_website::selectableunit_constructor_exists():
    assert callable(website::SelectableUnit.__init__)


def test_website::selectableunit_constructor_args():
    sig = inspect.signature(website::SelectableUnit.__init__)
    params = list(sig.parameters.keys())



def test_website::captchafield_is_not_abstract():
    assert not inspect.isabstract(website::CaptchaField)


def test_website::captchafield_constructor_exists():
    assert callable(website::CaptchaField.__init__)


def test_website::captchafield_constructor_args():
    sig = inspect.signature(website::CaptchaField.__init__)
    params = list(sig.parameters.keys())



def test_unitfeature_is_not_abstract():
    assert not inspect.isabstract(UnitFeature)


def test_unitfeature_constructor_exists():
    assert callable(UnitFeature.__init__)


def test_unitfeature_constructor_args():
    sig = inspect.signature(UnitFeature.__init__)
    params = list(sig.parameters.keys())



def test_website::unitelement_is_not_abstract():
    assert not inspect.isabstract(website::UnitElement)


def test_website::unitelement_constructor_exists():
    assert callable(website::UnitElement.__init__)


def test_website::unitelement_constructor_args():
    sig = inspect.signature(website::UnitElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "validationPattern" in params, "Missing parameter 'validationPattern'"
    assert "obfuscateFormFields" in params, "Missing parameter 'obfuscateFormFields'"
    assert "placeholder" in params, "Missing parameter 'placeholder'"

def test_website::unitelement_has_name():
    assert hasattr(website::UnitElement, "name")
    descriptor = None
    for klass in website::UnitElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_website::unitelement_has_validationPattern():
    assert hasattr(website::UnitElement, "validationPattern")
    descriptor = None
    for klass in website::UnitElement.__mro__:
        if "validationPattern" in klass.__dict__:
            descriptor = klass.__dict__["validationPattern"]
            break
    assert isinstance(descriptor, property)

def test_website::unitelement_has_obfuscateFormFields():
    assert hasattr(website::UnitElement, "obfuscateFormFields")
    descriptor = None
    for klass in website::UnitElement.__mro__:
        if "obfuscateFormFields" in klass.__dict__:
            descriptor = klass.__dict__["obfuscateFormFields"]
            break
    assert isinstance(descriptor, property)

def test_website::unitelement_has_placeholder():
    assert hasattr(website::UnitElement, "placeholder")
    descriptor = None
    for klass in website::UnitElement.__mro__:
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



def test_website::imageindexunit_is_not_abstract():
    assert not inspect.isabstract(website::ImageIndexUnit)


def test_website::imageindexunit_constructor_exists():
    assert callable(website::ImageIndexUnit.__init__)


def test_website::imageindexunit_constructor_args():
    sig = inspect.signature(website::ImageIndexUnit.__init__)
    params = list(sig.parameters.keys())
    assert "contentClass" in params, "Missing parameter 'contentClass'"
    assert "styleClass" in params, "Missing parameter 'styleClass'"

def test_website::imageindexunit_has_contentClass():
    assert hasattr(website::ImageIndexUnit, "contentClass")
    descriptor = None
    for klass in website::ImageIndexUnit.__mro__:
        if "contentClass" in klass.__dict__:
            descriptor = klass.__dict__["contentClass"]
            break
    assert isinstance(descriptor, property)

def test_website::imageindexunit_has_styleClass():
    assert hasattr(website::ImageIndexUnit, "styleClass")
    descriptor = None
    for klass in website::ImageIndexUnit.__mro__:
        if "styleClass" in klass.__dict__:
            descriptor = klass.__dict__["styleClass"]
            break
    assert isinstance(descriptor, property)



def test_website::indexunit_is_not_abstract():
    assert not inspect.isabstract(website::IndexUnit)


def test_website::indexunit_constructor_exists():
    assert callable(website::IndexUnit.__init__)


def test_website::indexunit_constructor_args():
    sig = inspect.signature(website::IndexUnit.__init__)
    params = list(sig.parameters.keys())
    assert "styleClass" in params, "Missing parameter 'styleClass'"
    assert "contentClass" in params, "Missing parameter 'contentClass'"
    assert "displayOption" in params, "Missing parameter 'displayOption'"
    assert "omitColumnLabels" in params, "Missing parameter 'omitColumnLabels'"
    assert "rowClasses" in params, "Missing parameter 'rowClasses'"

def test_website::indexunit_has_styleClass():
    assert hasattr(website::IndexUnit, "styleClass")
    descriptor = None
    for klass in website::IndexUnit.__mro__:
        if "styleClass" in klass.__dict__:
            descriptor = klass.__dict__["styleClass"]
            break
    assert isinstance(descriptor, property)

def test_website::indexunit_has_contentClass():
    assert hasattr(website::IndexUnit, "contentClass")
    descriptor = None
    for klass in website::IndexUnit.__mro__:
        if "contentClass" in klass.__dict__:
            descriptor = klass.__dict__["contentClass"]
            break
    assert isinstance(descriptor, property)

def test_website::indexunit_has_displayOption():
    assert hasattr(website::IndexUnit, "displayOption")
    descriptor = None
    for klass in website::IndexUnit.__mro__:
        if "displayOption" in klass.__dict__:
            descriptor = klass.__dict__["displayOption"]
            break
    assert isinstance(descriptor, property)

def test_website::indexunit_has_omitColumnLabels():
    assert hasattr(website::IndexUnit, "omitColumnLabels")
    descriptor = None
    for klass in website::IndexUnit.__mro__:
        if "omitColumnLabels" in klass.__dict__:
            descriptor = klass.__dict__["omitColumnLabels"]
            break
    assert isinstance(descriptor, property)

def test_website::indexunit_has_rowClasses():
    assert hasattr(website::IndexUnit, "rowClasses")
    descriptor = None
    for klass in website::IndexUnit.__mro__:
        if "rowClasses" in klass.__dict__:
            descriptor = klass.__dict__["rowClasses"]
            break
    assert isinstance(descriptor, property)



def test_unitfield_is_not_abstract():
    assert not inspect.isabstract(UnitField)


def test_unitfield_constructor_exists():
    assert callable(UnitField.__init__)


def test_unitfield_constructor_args():
    sig = inspect.signature(UnitField.__init__)
    params = list(sig.parameters.keys())



def test_website::interfacefield_is_not_abstract():
    assert not inspect.isabstract(website::InterfaceField)


def test_website::interfacefield_constructor_exists():
    assert callable(website::InterfaceField.__init__)


def test_website::interfacefield_constructor_args():
    sig = inspect.signature(website::InterfaceField.__init__)
    params = list(sig.parameters.keys())
    assert "inputClass" in params, "Missing parameter 'inputClass'"
    assert "required" in params, "Missing parameter 'required'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "placeholder" in params, "Missing parameter 'placeholder'"
    assert "validationPattern" in params, "Missing parameter 'validationPattern'"

def test_website::interfacefield_has_inputClass():
    assert hasattr(website::InterfaceField, "inputClass")
    descriptor = None
    for klass in website::InterfaceField.__mro__:
        if "inputClass" in klass.__dict__:
            descriptor = klass.__dict__["inputClass"]
            break
    assert isinstance(descriptor, property)

def test_website::interfacefield_has_required():
    assert hasattr(website::InterfaceField, "required")
    descriptor = None
    for klass in website::InterfaceField.__mro__:
        if "required" in klass.__dict__:
            descriptor = klass.__dict__["required"]
            break
    assert isinstance(descriptor, property)

def test_website::interfacefield_has_defaultValue():
    assert hasattr(website::InterfaceField, "defaultValue")
    descriptor = None
    for klass in website::InterfaceField.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)

def test_website::interfacefield_has_placeholder():
    assert hasattr(website::InterfaceField, "placeholder")
    descriptor = None
    for klass in website::InterfaceField.__mro__:
        if "placeholder" in klass.__dict__:
            descriptor = klass.__dict__["placeholder"]
            break
    assert isinstance(descriptor, property)

def test_website::interfacefield_has_validationPattern():
    assert hasattr(website::InterfaceField, "validationPattern")
    descriptor = None
    for klass in website::InterfaceField.__mro__:
        if "validationPattern" in klass.__dict__:
            descriptor = klass.__dict__["validationPattern"]
            break
    assert isinstance(descriptor, property)



def test_website::unitfeature_is_not_abstract():
    assert not inspect.isabstract(website::UnitFeature)


def test_website::unitfeature_constructor_exists():
    assert callable(website::UnitFeature.__init__)


def test_website::unitfeature_constructor_args():
    sig = inspect.signature(website::UnitFeature.__init__)
    params = list(sig.parameters.keys())
    assert "footerClass" in params, "Missing parameter 'footerClass'"
    assert "inputClass" in params, "Missing parameter 'inputClass'"
    assert "displayLabel" in params, "Missing parameter 'displayLabel'"
    assert "required" in params, "Missing parameter 'required'"
    assert "autofocus" in params, "Missing parameter 'autofocus'"
    assert "headerClass" in params, "Missing parameter 'headerClass'"
    assert "displayClass" in params, "Missing parameter 'displayClass'"
    assert "onlyDisplayWhenNotEmpty" in params, "Missing parameter 'onlyDisplayWhenNotEmpty'"
    assert "nullDisplayValue" in params, "Missing parameter 'nullDisplayValue'"
    assert "footer" in params, "Missing parameter 'footer'"

def test_website::unitfeature_has_footerClass():
    assert hasattr(website::UnitFeature, "footerClass")
    descriptor = None
    for klass in website::UnitFeature.__mro__:
        if "footerClass" in klass.__dict__:
            descriptor = klass.__dict__["footerClass"]
            break
    assert isinstance(descriptor, property)

def test_website::unitfeature_has_inputClass():
    assert hasattr(website::UnitFeature, "inputClass")
    descriptor = None
    for klass in website::UnitFeature.__mro__:
        if "inputClass" in klass.__dict__:
            descriptor = klass.__dict__["inputClass"]
            break
    assert isinstance(descriptor, property)

def test_website::unitfeature_has_displayLabel():
    assert hasattr(website::UnitFeature, "displayLabel")
    descriptor = None
    for klass in website::UnitFeature.__mro__:
        if "displayLabel" in klass.__dict__:
            descriptor = klass.__dict__["displayLabel"]
            break
    assert isinstance(descriptor, property)

def test_website::unitfeature_has_required():
    assert hasattr(website::UnitFeature, "required")
    descriptor = None
    for klass in website::UnitFeature.__mro__:
        if "required" in klass.__dict__:
            descriptor = klass.__dict__["required"]
            break
    assert isinstance(descriptor, property)

def test_website::unitfeature_has_autofocus():
    assert hasattr(website::UnitFeature, "autofocus")
    descriptor = None
    for klass in website::UnitFeature.__mro__:
        if "autofocus" in klass.__dict__:
            descriptor = klass.__dict__["autofocus"]
            break
    assert isinstance(descriptor, property)

def test_website::unitfeature_has_headerClass():
    assert hasattr(website::UnitFeature, "headerClass")
    descriptor = None
    for klass in website::UnitFeature.__mro__:
        if "headerClass" in klass.__dict__:
            descriptor = klass.__dict__["headerClass"]
            break
    assert isinstance(descriptor, property)

def test_website::unitfeature_has_displayClass():
    assert hasattr(website::UnitFeature, "displayClass")
    descriptor = None
    for klass in website::UnitFeature.__mro__:
        if "displayClass" in klass.__dict__:
            descriptor = klass.__dict__["displayClass"]
            break
    assert isinstance(descriptor, property)

def test_website::unitfeature_has_onlyDisplayWhenNotEmpty():
    assert hasattr(website::UnitFeature, "onlyDisplayWhenNotEmpty")
    descriptor = None
    for klass in website::UnitFeature.__mro__:
        if "onlyDisplayWhenNotEmpty" in klass.__dict__:
            descriptor = klass.__dict__["onlyDisplayWhenNotEmpty"]
            break
    assert isinstance(descriptor, property)

def test_website::unitfeature_has_nullDisplayValue():
    assert hasattr(website::UnitFeature, "nullDisplayValue")
    descriptor = None
    for klass in website::UnitFeature.__mro__:
        if "nullDisplayValue" in klass.__dict__:
            descriptor = klass.__dict__["nullDisplayValue"]
            break
    assert isinstance(descriptor, property)

def test_website::unitfeature_has_footer():
    assert hasattr(website::UnitFeature, "footer")
    descriptor = None
    for klass in website::UnitFeature.__mro__:
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



def test_website::childpathassociation_is_not_abstract():
    assert not inspect.isabstract(website::ChildPathAssociation)


def test_website::childpathassociation_constructor_exists():
    assert callable(website::ChildPathAssociation.__init__)


def test_website::childpathassociation_constructor_args():
    sig = inspect.signature(website::ChildPathAssociation.__init__)
    params = list(sig.parameters.keys())
    assert "isSourceAssociation" in params, "Missing parameter 'isSourceAssociation'"

def test_website::childpathassociation_has_isSourceAssociation():
    assert hasattr(website::ChildPathAssociation, "isSourceAssociation")
    descriptor = None
    for klass in website::ChildPathAssociation.__mro__:
        if "isSourceAssociation" in klass.__dict__:
            descriptor = klass.__dict__["isSourceAssociation"]
            break
    assert isinstance(descriptor, property)



def test_website::featurepathassociation_is_not_abstract():
    assert not inspect.isabstract(website::FeaturePathAssociation)


def test_website::featurepathassociation_constructor_exists():
    assert callable(website::FeaturePathAssociation.__init__)


def test_website::featurepathassociation_constructor_args():
    sig = inspect.signature(website::FeaturePathAssociation.__init__)
    params = list(sig.parameters.keys())
    assert "isSourceAssociation" in params, "Missing parameter 'isSourceAssociation'"

def test_website::featurepathassociation_has_isSourceAssociation():
    assert hasattr(website::FeaturePathAssociation, "isSourceAssociation")
    descriptor = None
    for klass in website::FeaturePathAssociation.__mro__:
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



def test_website::createsitemapunit_is_not_abstract():
    assert not inspect.isabstract(website::CreateSitemapUnit)


def test_website::createsitemapunit_constructor_exists():
    assert callable(website::CreateSitemapUnit.__init__)


def test_website::createsitemapunit_constructor_args():
    sig = inspect.signature(website::CreateSitemapUnit.__init__)
    params = list(sig.parameters.keys())
    assert "filename" in params, "Missing parameter 'filename'"
    assert "styleClass" in params, "Missing parameter 'styleClass'"
    assert "deployedURL" in params, "Missing parameter 'deployedURL'"
    assert "contentClass" in params, "Missing parameter 'contentClass'"

def test_website::createsitemapunit_has_filename():
    assert hasattr(website::CreateSitemapUnit, "filename")
    descriptor = None
    for klass in website::CreateSitemapUnit.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)

def test_website::createsitemapunit_has_styleClass():
    assert hasattr(website::CreateSitemapUnit, "styleClass")
    descriptor = None
    for klass in website::CreateSitemapUnit.__mro__:
        if "styleClass" in klass.__dict__:
            descriptor = klass.__dict__["styleClass"]
            break
    assert isinstance(descriptor, property)

def test_website::createsitemapunit_has_deployedURL():
    assert hasattr(website::CreateSitemapUnit, "deployedURL")
    descriptor = None
    for klass in website::CreateSitemapUnit.__mro__:
        if "deployedURL" in klass.__dict__:
            descriptor = klass.__dict__["deployedURL"]
            break
    assert isinstance(descriptor, property)

def test_website::createsitemapunit_has_contentClass():
    assert hasattr(website::CreateSitemapUnit, "contentClass")
    descriptor = None
    for klass in website::CreateSitemapUnit.__mro__:
        if "contentClass" in klass.__dict__:
            descriptor = klass.__dict__["contentClass"]
            break
    assert isinstance(descriptor, property)



def test_website::dynamicunit_is_not_abstract():
    assert not inspect.isabstract(website::DynamicUnit)


def test_website::dynamicunit_constructor_exists():
    assert callable(website::DynamicUnit.__init__)


def test_website::dynamicunit_constructor_args():
    sig = inspect.signature(website::DynamicUnit.__init__)
    params = list(sig.parameters.keys())
    assert "footerClass" in params, "Missing parameter 'footerClass'"
    assert "errorClass" in params, "Missing parameter 'errorClass'"
    assert "footer" in params, "Missing parameter 'footer'"
    assert "headerClass" in params, "Missing parameter 'headerClass'"
    assert "header" in params, "Missing parameter 'header'"
    assert "controlClass" in params, "Missing parameter 'controlClass'"

def test_website::dynamicunit_has_footerClass():
    assert hasattr(website::DynamicUnit, "footerClass")
    descriptor = None
    for klass in website::DynamicUnit.__mro__:
        if "footerClass" in klass.__dict__:
            descriptor = klass.__dict__["footerClass"]
            break
    assert isinstance(descriptor, property)

def test_website::dynamicunit_has_errorClass():
    assert hasattr(website::DynamicUnit, "errorClass")
    descriptor = None
    for klass in website::DynamicUnit.__mro__:
        if "errorClass" in klass.__dict__:
            descriptor = klass.__dict__["errorClass"]
            break
    assert isinstance(descriptor, property)

def test_website::dynamicunit_has_footer():
    assert hasattr(website::DynamicUnit, "footer")
    descriptor = None
    for klass in website::DynamicUnit.__mro__:
        if "footer" in klass.__dict__:
            descriptor = klass.__dict__["footer"]
            break
    assert isinstance(descriptor, property)

def test_website::dynamicunit_has_headerClass():
    assert hasattr(website::DynamicUnit, "headerClass")
    descriptor = None
    for klass in website::DynamicUnit.__mro__:
        if "headerClass" in klass.__dict__:
            descriptor = klass.__dict__["headerClass"]
            break
    assert isinstance(descriptor, property)

def test_website::dynamicunit_has_header():
    assert hasattr(website::DynamicUnit, "header")
    descriptor = None
    for klass in website::DynamicUnit.__mro__:
        if "header" in klass.__dict__:
            descriptor = klass.__dict__["header"]
            break
    assert isinstance(descriptor, property)

def test_website::dynamicunit_has_controlClass():
    assert hasattr(website::DynamicUnit, "controlClass")
    descriptor = None
    for klass in website::DynamicUnit.__mro__:
        if "controlClass" in klass.__dict__:
            descriptor = klass.__dict__["controlClass"]
            break
    assert isinstance(descriptor, property)



def test_website::staticunit_is_not_abstract():
    assert not inspect.isabstract(website::StaticUnit)


def test_website::staticunit_constructor_exists():
    assert callable(website::StaticUnit.__init__)


def test_website::staticunit_constructor_args():
    sig = inspect.signature(website::StaticUnit.__init__)
    params = list(sig.parameters.keys())
    assert "styleClass" in params, "Missing parameter 'styleClass'"
    assert "contentClass" in params, "Missing parameter 'contentClass'"
    assert "content" in params, "Missing parameter 'content'"

def test_website::staticunit_has_styleClass():
    assert hasattr(website::StaticUnit, "styleClass")
    descriptor = None
    for klass in website::StaticUnit.__mro__:
        if "styleClass" in klass.__dict__:
            descriptor = klass.__dict__["styleClass"]
            break
    assert isinstance(descriptor, property)

def test_website::staticunit_has_contentClass():
    assert hasattr(website::StaticUnit, "contentClass")
    descriptor = None
    for klass in website::StaticUnit.__mro__:
        if "contentClass" in klass.__dict__:
            descriptor = klass.__dict__["contentClass"]
            break
    assert isinstance(descriptor, property)

def test_website::staticunit_has_content():
    assert hasattr(website::StaticUnit, "content")
    descriptor = None
    for klass in website::StaticUnit.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_website::unitcontainer_is_not_abstract():
    assert not inspect.isabstract(website::UnitContainer)


def test_website::unitcontainer_constructor_exists():
    assert callable(website::UnitContainer.__init__)


def test_website::unitcontainer_constructor_args():
    sig = inspect.signature(website::UnitContainer.__init__)
    params = list(sig.parameters.keys())



def test_website::unitsupportaction_is_not_abstract():
    assert not inspect.isabstract(website::UnitSupportAction)


def test_website::unitsupportaction_constructor_exists():
    assert callable(website::UnitSupportAction.__init__)


def test_website::unitsupportaction_constructor_args():
    sig = inspect.signature(website::UnitSupportAction.__init__)
    params = list(sig.parameters.keys())
    assert "disable" in params, "Missing parameter 'disable'"
    assert "confirmMessage" in params, "Missing parameter 'confirmMessage'"

def test_website::unitsupportaction_has_disable():
    assert hasattr(website::UnitSupportAction, "disable")
    descriptor = None
    for klass in website::UnitSupportAction.__mro__:
        if "disable" in klass.__dict__:
            descriptor = klass.__dict__["disable"]
            break
    assert isinstance(descriptor, property)

def test_website::unitsupportaction_has_confirmMessage():
    assert hasattr(website::UnitSupportAction, "confirmMessage")
    descriptor = None
    for klass in website::UnitSupportAction.__mro__:
        if "confirmMessage" in klass.__dict__:
            descriptor = klass.__dict__["confirmMessage"]
            break
    assert isinstance(descriptor, property)



def test_website::unitfield_is_not_abstract():
    assert not inspect.isabstract(website::UnitField)


def test_website::unitfield_constructor_exists():
    assert callable(website::UnitField.__init__)


def test_website::unitfield_constructor_args():
    sig = inspect.signature(website::UnitField.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "dateFormat" in params, "Missing parameter 'dateFormat'"
    assert "collectionAllowRemove" in params, "Missing parameter 'collectionAllowRemove'"
    assert "collectionDisplayOption" in params, "Missing parameter 'collectionDisplayOption'"
    assert "collectionAllowAdd" in params, "Missing parameter 'collectionAllowAdd'"
    assert "maximumDisplaySize" in params, "Missing parameter 'maximumDisplaySize'"

def test_website::unitfield_has_title():
    assert hasattr(website::UnitField, "title")
    descriptor = None
    for klass in website::UnitField.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_website::unitfield_has_dateFormat():
    assert hasattr(website::UnitField, "dateFormat")
    descriptor = None
    for klass in website::UnitField.__mro__:
        if "dateFormat" in klass.__dict__:
            descriptor = klass.__dict__["dateFormat"]
            break
    assert isinstance(descriptor, property)

def test_website::unitfield_has_collectionAllowRemove():
    assert hasattr(website::UnitField, "collectionAllowRemove")
    descriptor = None
    for klass in website::UnitField.__mro__:
        if "collectionAllowRemove" in klass.__dict__:
            descriptor = klass.__dict__["collectionAllowRemove"]
            break
    assert isinstance(descriptor, property)

def test_website::unitfield_has_collectionDisplayOption():
    assert hasattr(website::UnitField, "collectionDisplayOption")
    descriptor = None
    for klass in website::UnitField.__mro__:
        if "collectionDisplayOption" in klass.__dict__:
            descriptor = klass.__dict__["collectionDisplayOption"]
            break
    assert isinstance(descriptor, property)

def test_website::unitfield_has_collectionAllowAdd():
    assert hasattr(website::UnitField, "collectionAllowAdd")
    descriptor = None
    for klass in website::UnitField.__mro__:
        if "collectionAllowAdd" in klass.__dict__:
            descriptor = klass.__dict__["collectionAllowAdd"]
            break
    assert isinstance(descriptor, property)

def test_website::unitfield_has_maximumDisplaySize():
    assert hasattr(website::UnitField, "maximumDisplaySize")
    descriptor = None
    for klass in website::UnitField.__mro__:
        if "maximumDisplaySize" in klass.__dict__:
            descriptor = klass.__dict__["maximumDisplaySize"]
            break
    assert isinstance(descriptor, property)



def test_website::filter_is_not_abstract():
    assert not inspect.isabstract(website::Filter)


def test_website::filter_constructor_exists():
    assert callable(website::Filter.__init__)


def test_website::filter_constructor_args():
    sig = inspect.signature(website::Filter.__init__)
    params = list(sig.parameters.keys())



def test_website::query_is_not_abstract():
    assert not inspect.isabstract(website::Query)


def test_website::query_constructor_exists():
    assert callable(website::Query.__init__)


def test_website::query_constructor_args():
    sig = inspect.signature(website::Query.__init__)
    params = list(sig.parameters.keys())



def test_website::contentunit_is_not_abstract():
    assert not inspect.isabstract(website::ContentUnit)


def test_website::contentunit_constructor_exists():
    assert callable(website::ContentUnit.__init__)


def test_website::contentunit_constructor_args():
    sig = inspect.signature(website::ContentUnit.__init__)
    params = list(sig.parameters.keys())
    assert "captionClass" in params, "Missing parameter 'captionClass'"
    assert "createDefaultUriElement" in params, "Missing parameter 'createDefaultUriElement'"
    assert "requiresRole" in params, "Missing parameter 'requiresRole'"
    assert "purposeSummary" in params, "Missing parameter 'purposeSummary'"
    assert "omitCaption" in params, "Missing parameter 'omitCaption'"
    assert "uriElement" in params, "Missing parameter 'uriElement'"
    assert "alternative" in params, "Missing parameter 'alternative'"

def test_website::contentunit_has_captionClass():
    assert hasattr(website::ContentUnit, "captionClass")
    descriptor = None
    for klass in website::ContentUnit.__mro__:
        if "captionClass" in klass.__dict__:
            descriptor = klass.__dict__["captionClass"]
            break
    assert isinstance(descriptor, property)

def test_website::contentunit_has_createDefaultUriElement():
    assert hasattr(website::ContentUnit, "createDefaultUriElement")
    descriptor = None
    for klass in website::ContentUnit.__mro__:
        if "createDefaultUriElement" in klass.__dict__:
            descriptor = klass.__dict__["createDefaultUriElement"]
            break
    assert isinstance(descriptor, property)

def test_website::contentunit_has_requiresRole():
    assert hasattr(website::ContentUnit, "requiresRole")
    descriptor = None
    for klass in website::ContentUnit.__mro__:
        if "requiresRole" in klass.__dict__:
            descriptor = klass.__dict__["requiresRole"]
            break
    assert isinstance(descriptor, property)

def test_website::contentunit_has_purposeSummary():
    assert hasattr(website::ContentUnit, "purposeSummary")
    descriptor = None
    for klass in website::ContentUnit.__mro__:
        if "purposeSummary" in klass.__dict__:
            descriptor = klass.__dict__["purposeSummary"]
            break
    assert isinstance(descriptor, property)

def test_website::contentunit_has_omitCaption():
    assert hasattr(website::ContentUnit, "omitCaption")
    descriptor = None
    for klass in website::ContentUnit.__mro__:
        if "omitCaption" in klass.__dict__:
            descriptor = klass.__dict__["omitCaption"]
            break
    assert isinstance(descriptor, property)

def test_website::contentunit_has_uriElement():
    assert hasattr(website::ContentUnit, "uriElement")
    descriptor = None
    for klass in website::ContentUnit.__mro__:
        if "uriElement" in klass.__dict__:
            descriptor = klass.__dict__["uriElement"]
            break
    assert isinstance(descriptor, property)

def test_website::contentunit_has_alternative():
    assert hasattr(website::ContentUnit, "alternative")
    descriptor = None
    for klass in website::ContentUnit.__mro__:
        if "alternative" in klass.__dict__:
            descriptor = klass.__dict__["alternative"]
            break
    assert isinstance(descriptor, property)



def test_menuentry_is_not_abstract():
    assert not inspect.isabstract(MenuEntry)


def test_menuentry_constructor_exists():
    assert callable(MenuEntry.__init__)


def test_menuentry_constructor_args():
    sig = inspect.signature(MenuEntry.__init__)
    params = list(sig.parameters.keys())



def test_website::editstatictextmenuentry_is_not_abstract():
    assert not inspect.isabstract(website::EditStaticTextMenuEntry)


def test_website::editstatictextmenuentry_constructor_exists():
    assert callable(website::EditStaticTextMenuEntry.__init__)


def test_website::editstatictextmenuentry_constructor_args():
    sig = inspect.signature(website::EditStaticTextMenuEntry.__init__)
    params = list(sig.parameters.keys())



def test_website::menufeature_is_not_abstract():
    assert not inspect.isabstract(website::MenuFeature)


def test_website::menufeature_constructor_exists():
    assert callable(website::MenuFeature.__init__)


def test_website::menufeature_constructor_args():
    sig = inspect.signature(website::MenuFeature.__init__)
    params = list(sig.parameters.keys())



def test_website::actionmenuentry_is_not_abstract():
    assert not inspect.isabstract(website::ActionMenuEntry)


def test_website::actionmenuentry_constructor_exists():
    assert callable(website::ActionMenuEntry.__init__)


def test_website::actionmenuentry_constructor_args():
    sig = inspect.signature(website::ActionMenuEntry.__init__)
    params = list(sig.parameters.keys())



def test_menu_is_not_abstract():
    assert not inspect.isabstract(Menu)


def test_menu_constructor_exists():
    assert callable(Menu.__init__)


def test_menu_constructor_args():
    sig = inspect.signature(Menu.__init__)
    params = list(sig.parameters.keys())



def test_website::dynamicmenu_is_not_abstract():
    assert not inspect.isabstract(website::DynamicMenu)


def test_website::dynamicmenu_constructor_exists():
    assert callable(website::DynamicMenu.__init__)


def test_website::dynamicmenu_constructor_args():
    sig = inspect.signature(website::DynamicMenu.__init__)
    params = list(sig.parameters.keys())



def test_website::staticmenu_is_not_abstract():
    assert not inspect.isabstract(website::StaticMenu)


def test_website::staticmenu_constructor_exists():
    assert callable(website::StaticMenu.__init__)


def test_website::staticmenu_constructor_args():
    sig = inspect.signature(website::StaticMenu.__init__)
    params = list(sig.parameters.keys())



def test_website::menuentry_is_not_abstract():
    assert not inspect.isabstract(website::MenuEntry)


def test_website::menuentry_constructor_exists():
    assert callable(website::MenuEntry.__init__)


def test_website::menuentry_constructor_args():
    sig = inspect.signature(website::MenuEntry.__init__)
    params = list(sig.parameters.keys())
    assert "requiresRole" in params, "Missing parameter 'requiresRole'"

def test_website::menuentry_has_requiresRole():
    assert hasattr(website::MenuEntry, "requiresRole")
    descriptor = None
    for klass in website::MenuEntry.__mro__:
        if "requiresRole" in klass.__dict__:
            descriptor = klass.__dict__["requiresRole"]
            break
    assert isinstance(descriptor, property)



def test_website::queryparameter_is_not_abstract():
    assert not inspect.isabstract(website::QueryParameter)


def test_website::queryparameter_constructor_exists():
    assert callable(website::QueryParameter.__init__)


def test_website::queryparameter_constructor_args():
    sig = inspect.signature(website::QueryParameter.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_website::queryparameter_has_value():
    assert hasattr(website::QueryParameter, "value")
    descriptor = None
    for klass in website::QueryParameter.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_website::filterparameter_is_not_abstract():
    assert not inspect.isabstract(website::FilterParameter)


def test_website::filterparameter_constructor_exists():
    assert callable(website::FilterParameter.__init__)


def test_website::filterparameter_constructor_args():
    sig = inspect.signature(website::FilterParameter.__init__)
    params = list(sig.parameters.keys())
    assert "placeholder" in params, "Missing parameter 'placeholder'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"

def test_website::filterparameter_has_placeholder():
    assert hasattr(website::FilterParameter, "placeholder")
    descriptor = None
    for klass in website::FilterParameter.__mro__:
        if "placeholder" in klass.__dict__:
            descriptor = klass.__dict__["placeholder"]
            break
    assert isinstance(descriptor, property)

def test_website::filterparameter_has_defaultValue():
    assert hasattr(website::FilterParameter, "defaultValue")
    descriptor = None
    for klass in website::FilterParameter.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)



def test_unitcontainer_is_not_abstract():
    assert not inspect.isabstract(UnitContainer)


def test_unitcontainer_constructor_exists():
    assert callable(UnitContainer.__init__)


def test_unitcontainer_constructor_args():
    sig = inspect.signature(UnitContainer.__init__)
    params = list(sig.parameters.keys())



def test_website::page_is_not_abstract():
    assert not inspect.isabstract(website::Page)


def test_website::page_constructor_exists():
    assert callable(website::Page.__init__)


def test_website::page_constructor_args():
    sig = inspect.signature(website::Page.__init__)
    params = list(sig.parameters.keys())
    assert "navigationLabel" in params, "Missing parameter 'navigationLabel'"
    assert "topMenuRank" in params, "Missing parameter 'topMenuRank'"
    assert "styleClass" in params, "Missing parameter 'styleClass'"
    assert "topMenuOption" in params, "Missing parameter 'topMenuOption'"
    assert "authenticated" in params, "Missing parameter 'authenticated'"
    assert "uriElement" in params, "Missing parameter 'uriElement'"

def test_website::page_has_navigationLabel():
    assert hasattr(website::Page, "navigationLabel")
    descriptor = None
    for klass in website::Page.__mro__:
        if "navigationLabel" in klass.__dict__:
            descriptor = klass.__dict__["navigationLabel"]
            break
    assert isinstance(descriptor, property)

def test_website::page_has_topMenuRank():
    assert hasattr(website::Page, "topMenuRank")
    descriptor = None
    for klass in website::Page.__mro__:
        if "topMenuRank" in klass.__dict__:
            descriptor = klass.__dict__["topMenuRank"]
            break
    assert isinstance(descriptor, property)

def test_website::page_has_styleClass():
    assert hasattr(website::Page, "styleClass")
    descriptor = None
    for klass in website::Page.__mro__:
        if "styleClass" in klass.__dict__:
            descriptor = klass.__dict__["styleClass"]
            break
    assert isinstance(descriptor, property)

def test_website::page_has_topMenuOption():
    assert hasattr(website::Page, "topMenuOption")
    descriptor = None
    for klass in website::Page.__mro__:
        if "topMenuOption" in klass.__dict__:
            descriptor = klass.__dict__["topMenuOption"]
            break
    assert isinstance(descriptor, property)

def test_website::page_has_authenticated():
    assert hasattr(website::Page, "authenticated")
    descriptor = None
    for klass in website::Page.__mro__:
        if "authenticated" in klass.__dict__:
            descriptor = klass.__dict__["authenticated"]
            break
    assert isinstance(descriptor, property)

def test_website::page_has_uriElement():
    assert hasattr(website::Page, "uriElement")
    descriptor = None
    for klass in website::Page.__mro__:
        if "uriElement" in klass.__dict__:
            descriptor = klass.__dict__["uriElement"]
            break
    assert isinstance(descriptor, property)



def test_website::unitassociation_is_not_abstract():
    assert not inspect.isabstract(website::UnitAssociation)


def test_website::unitassociation_constructor_exists():
    assert callable(website::UnitAssociation.__init__)


def test_website::unitassociation_constructor_args():
    sig = inspect.signature(website::UnitAssociation.__init__)
    params = list(sig.parameters.keys())
    assert "isSourceAssociation" in params, "Missing parameter 'isSourceAssociation'"

def test_website::unitassociation_has_isSourceAssociation():
    assert hasattr(website::UnitAssociation, "isSourceAssociation")
    descriptor = None
    for klass in website::UnitAssociation.__mro__:
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



def test_website::thumbnailfilter_is_not_abstract():
    assert not inspect.isabstract(website::ThumbnailFilter)


def test_website::thumbnailfilter_constructor_exists():
    assert callable(website::ThumbnailFilter.__init__)


def test_website::thumbnailfilter_constructor_args():
    sig = inspect.signature(website::ThumbnailFilter.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"

def test_website::thumbnailfilter_has_height():
    assert hasattr(website::ThumbnailFilter, "height")
    descriptor = None
    for klass in website::ThumbnailFilter.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_website::thumbnailfilter_has_width():
    assert hasattr(website::ThumbnailFilter, "width")
    descriptor = None
    for klass in website::ThumbnailFilter.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_website::imagefilter_is_not_abstract():
    assert not inspect.isabstract(website::ImageFilter)


def test_website::imagefilter_constructor_exists():
    assert callable(website::ImageFilter.__init__)


def test_website::imagefilter_constructor_args():
    sig = inspect.signature(website::ImageFilter.__init__)
    params = list(sig.parameters.keys())



def test_website::order_is_not_abstract():
    assert not inspect.isabstract(website::Order)


def test_website::order_constructor_exists():
    assert callable(website::Order.__init__)


def test_website::order_constructor_args():
    sig = inspect.signature(website::Order.__init__)
    params = list(sig.parameters.keys())



def test_website::predicate_is_not_abstract():
    assert not inspect.isabstract(website::Predicate)


def test_website::predicate_constructor_exists():
    assert callable(website::Predicate.__init__)


def test_website::predicate_constructor_args():
    sig = inspect.signature(website::Predicate.__init__)
    params = list(sig.parameters.keys())



def test_website::pagelink_is_not_abstract():
    assert not inspect.isabstract(website::PageLink)


def test_website::pagelink_constructor_exists():
    assert callable(website::PageLink.__init__)


def test_website::pagelink_constructor_args():
    sig = inspect.signature(website::PageLink.__init__)
    params = list(sig.parameters.keys())



def test_website::selectionparameter_is_not_abstract():
    assert not inspect.isabstract(website::SelectionParameter)


def test_website::selectionparameter_constructor_exists():
    assert callable(website::SelectionParameter.__init__)


def test_website::selectionparameter_constructor_args():
    sig = inspect.signature(website::SelectionParameter.__init__)
    params = list(sig.parameters.keys())
    assert "optional" in params, "Missing parameter 'optional'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"

def test_website::selectionparameter_has_optional():
    assert hasattr(website::SelectionParameter, "optional")
    descriptor = None
    for klass in website::SelectionParameter.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)

def test_website::selectionparameter_has_defaultValue():
    assert hasattr(website::SelectionParameter, "defaultValue")
    descriptor = None
    for klass in website::SelectionParameter.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)



def test_website::businessoperation_is_not_abstract():
    assert not inspect.isabstract(website::BusinessOperation)


def test_website::businessoperation_constructor_exists():
    assert callable(website::BusinessOperation.__init__)


def test_website::businessoperation_constructor_args():
    sig = inspect.signature(website::BusinessOperation.__init__)
    params = list(sig.parameters.keys())
    assert "resultType" in params, "Missing parameter 'resultType'"
    assert "resultMimeType" in params, "Missing parameter 'resultMimeType'"

def test_website::businessoperation_has_resultType():
    assert hasattr(website::BusinessOperation, "resultType")
    descriptor = None
    for klass in website::BusinessOperation.__mro__:
        if "resultType" in klass.__dict__:
            descriptor = klass.__dict__["resultType"]
            break
    assert isinstance(descriptor, property)

def test_website::businessoperation_has_resultMimeType():
    assert hasattr(website::BusinessOperation, "resultMimeType")
    descriptor = None
    for klass in website::BusinessOperation.__mro__:
        if "resultMimeType" in klass.__dict__:
            descriptor = klass.__dict__["resultMimeType"]
            break
    assert isinstance(descriptor, property)



def test_website::selection_is_not_abstract():
    assert not inspect.isabstract(website::Selection)


def test_website::selection_constructor_exists():
    assert callable(website::Selection.__init__)


def test_website::selection_constructor_args():
    sig = inspect.signature(website::Selection.__init__)
    params = list(sig.parameters.keys())
    assert "distinct" in params, "Missing parameter 'distinct'"
    assert "selected" in params, "Missing parameter 'selected'"
    assert "limit" in params, "Missing parameter 'limit'"

def test_website::selection_has_distinct():
    assert hasattr(website::Selection, "distinct")
    descriptor = None
    for klass in website::Selection.__mro__:
        if "distinct" in klass.__dict__:
            descriptor = klass.__dict__["distinct"]
            break
    assert isinstance(descriptor, property)

def test_website::selection_has_selected():
    assert hasattr(website::Selection, "selected")
    descriptor = None
    for klass in website::Selection.__mro__:
        if "selected" in klass.__dict__:
            descriptor = klass.__dict__["selected"]
            break
    assert isinstance(descriptor, property)

def test_website::selection_has_limit():
    assert hasattr(website::Selection, "limit")
    descriptor = None
    for klass in website::Selection.__mro__:
        if "limit" in klass.__dict__:
            descriptor = klass.__dict__["limit"]
            break
    assert isinstance(descriptor, property)



def test_website::view_is_not_abstract():
    assert not inspect.isabstract(website::View)


def test_website::view_constructor_exists():
    assert callable(website::View.__init__)


def test_website::view_constructor_args():
    sig = inspect.signature(website::View.__init__)
    params = list(sig.parameters.keys())



def test_entityassociation_is_not_abstract():
    assert not inspect.isabstract(EntityAssociation)


def test_entityassociation_constructor_exists():
    assert callable(EntityAssociation.__init__)


def test_entityassociation_constructor_args():
    sig = inspect.signature(EntityAssociation.__init__)
    params = list(sig.parameters.keys())



def test_website::associationwithcontainment_is_not_abstract():
    assert not inspect.isabstract(website::AssociationWithContainment)


def test_website::associationwithcontainment_constructor_exists():
    assert callable(website::AssociationWithContainment.__init__)


def test_website::associationwithcontainment_constructor_args():
    sig = inspect.signature(website::AssociationWithContainment.__init__)
    params = list(sig.parameters.keys())
    assert "sourceVisible" in params, "Missing parameter 'sourceVisible'"

def test_website::associationwithcontainment_has_sourceVisible():
    assert hasattr(website::AssociationWithContainment, "sourceVisible")
    descriptor = None
    for klass in website::AssociationWithContainment.__mro__:
        if "sourceVisible" in klass.__dict__:
            descriptor = klass.__dict__["sourceVisible"]
            break
    assert isinstance(descriptor, property)



def test_website::associationwithoutcontainment_is_not_abstract():
    assert not inspect.isabstract(website::AssociationWithoutContainment)


def test_website::associationwithoutcontainment_constructor_exists():
    assert callable(website::AssociationWithoutContainment.__init__)


def test_website::associationwithoutcontainment_constructor_args():
    sig = inspect.signature(website::AssociationWithoutContainment.__init__)
    params = list(sig.parameters.keys())
    assert "targetCardinality" in params, "Missing parameter 'targetCardinality'"
    assert "targetUnique" in params, "Missing parameter 'targetUnique'"

def test_website::associationwithoutcontainment_has_targetCardinality():
    assert hasattr(website::AssociationWithoutContainment, "targetCardinality")
    descriptor = None
    for klass in website::AssociationWithoutContainment.__mro__:
        if "targetCardinality" in klass.__dict__:
            descriptor = klass.__dict__["targetCardinality"]
            break
    assert isinstance(descriptor, property)

def test_website::associationwithoutcontainment_has_targetUnique():
    assert hasattr(website::AssociationWithoutContainment, "targetUnique")
    descriptor = None
    for klass in website::AssociationWithoutContainment.__mro__:
        if "targetUnique" in klass.__dict__:
            descriptor = klass.__dict__["targetUnique"]
            break
    assert isinstance(descriptor, property)



def test_encapsulatedfeature_is_not_abstract():
    assert not inspect.isabstract(EncapsulatedFeature)


def test_encapsulatedfeature_constructor_exists():
    assert callable(EncapsulatedFeature.__init__)


def test_encapsulatedfeature_constructor_args():
    sig = inspect.signature(EncapsulatedFeature.__init__)
    params = list(sig.parameters.keys())



def test_website::encapsulatedassociation_is_not_abstract():
    assert not inspect.isabstract(website::EncapsulatedAssociation)


def test_website::encapsulatedassociation_constructor_exists():
    assert callable(website::EncapsulatedAssociation.__init__)


def test_website::encapsulatedassociation_constructor_args():
    sig = inspect.signature(website::EncapsulatedAssociation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isSourceAssociation" in params, "Missing parameter 'isSourceAssociation'"
    assert "cardinality" in params, "Missing parameter 'cardinality'"

def test_website::encapsulatedassociation_has_name():
    assert hasattr(website::EncapsulatedAssociation, "name")
    descriptor = None
    for klass in website::EncapsulatedAssociation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_website::encapsulatedassociation_has_isSourceAssociation():
    assert hasattr(website::EncapsulatedAssociation, "isSourceAssociation")
    descriptor = None
    for klass in website::EncapsulatedAssociation.__mro__:
        if "isSourceAssociation" in klass.__dict__:
            descriptor = klass.__dict__["isSourceAssociation"]
            break
    assert isinstance(descriptor, property)

def test_website::encapsulatedassociation_has_cardinality():
    assert hasattr(website::EncapsulatedAssociation, "cardinality")
    descriptor = None
    for klass in website::EncapsulatedAssociation.__mro__:
        if "cardinality" in klass.__dict__:
            descriptor = klass.__dict__["cardinality"]
            break
    assert isinstance(descriptor, property)



def test_website::encapsulatedattribute_is_not_abstract():
    assert not inspect.isabstract(website::EncapsulatedAttribute)


def test_website::encapsulatedattribute_constructor_exists():
    assert callable(website::EncapsulatedAttribute.__init__)


def test_website::encapsulatedattribute_constructor_args():
    sig = inspect.signature(website::EncapsulatedAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "cardinality" in params, "Missing parameter 'cardinality'"

def test_website::encapsulatedattribute_has_name():
    assert hasattr(website::EncapsulatedAttribute, "name")
    descriptor = None
    for klass in website::EncapsulatedAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_website::encapsulatedattribute_has_cardinality():
    assert hasattr(website::EncapsulatedAttribute, "cardinality")
    descriptor = None
    for klass in website::EncapsulatedAttribute.__mro__:
        if "cardinality" in klass.__dict__:
            descriptor = klass.__dict__["cardinality"]
            break
    assert isinstance(descriptor, property)



def test_viewfeature_is_not_abstract():
    assert not inspect.isabstract(ViewFeature)


def test_viewfeature_constructor_exists():
    assert callable(ViewFeature.__init__)


def test_viewfeature_constructor_args():
    sig = inspect.signature(ViewFeature.__init__)
    params = list(sig.parameters.keys())



def test_website::viewassociation_is_not_abstract():
    assert not inspect.isabstract(website::ViewAssociation)


def test_website::viewassociation_constructor_exists():
    assert callable(website::ViewAssociation.__init__)


def test_website::viewassociation_constructor_args():
    sig = inspect.signature(website::ViewAssociation.__init__)
    params = list(sig.parameters.keys())
    assert "cardinality" in params, "Missing parameter 'cardinality'"

def test_website::viewassociation_has_cardinality():
    assert hasattr(website::ViewAssociation, "cardinality")
    descriptor = None
    for klass in website::ViewAssociation.__mro__:
        if "cardinality" in klass.__dict__:
            descriptor = klass.__dict__["cardinality"]
            break
    assert isinstance(descriptor, property)



def test_website::encapsulatedfeature_is_not_abstract():
    assert not inspect.isabstract(website::EncapsulatedFeature)


def test_website::encapsulatedfeature_constructor_exists():
    assert callable(website::EncapsulatedFeature.__init__)


def test_website::encapsulatedfeature_constructor_args():
    sig = inspect.signature(website::EncapsulatedFeature.__init__)
    params = list(sig.parameters.keys())
    assert "columnName" in params, "Missing parameter 'columnName'"
    assert "alias" in params, "Missing parameter 'alias'"
    assert "displayLabel" in params, "Missing parameter 'displayLabel'"

def test_website::encapsulatedfeature_has_columnName():
    assert hasattr(website::EncapsulatedFeature, "columnName")
    descriptor = None
    for klass in website::EncapsulatedFeature.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)

def test_website::encapsulatedfeature_has_alias():
    assert hasattr(website::EncapsulatedFeature, "alias")
    descriptor = None
    for klass in website::EncapsulatedFeature.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)

def test_website::encapsulatedfeature_has_displayLabel():
    assert hasattr(website::EncapsulatedFeature, "displayLabel")
    descriptor = None
    for klass in website::EncapsulatedFeature.__mro__:
        if "displayLabel" in klass.__dict__:
            descriptor = klass.__dict__["displayLabel"]
            break
    assert isinstance(descriptor, property)



def test_website::viewfeature_is_not_abstract():
    assert not inspect.isabstract(website::ViewFeature)


def test_website::viewfeature_constructor_exists():
    assert callable(website::ViewFeature.__init__)


def test_website::viewfeature_constructor_args():
    sig = inspect.signature(website::ViewFeature.__init__)
    params = list(sig.parameters.keys())



def test_pathelement_is_not_abstract():
    assert not inspect.isabstract(PathElement)


def test_pathelement_constructor_exists():
    assert callable(PathElement.__init__)


def test_pathelement_constructor_args():
    sig = inspect.signature(PathElement.__init__)
    params = list(sig.parameters.keys())



def test_website::datepathelement_is_not_abstract():
    assert not inspect.isabstract(website::DatePathElement)


def test_website::datepathelement_constructor_exists():
    assert callable(website::DatePathElement.__init__)


def test_website::datepathelement_constructor_args():
    sig = inspect.signature(website::DatePathElement.__init__)
    params = list(sig.parameters.keys())
    assert "format" in params, "Missing parameter 'format'"

def test_website::datepathelement_has_format():
    assert hasattr(website::DatePathElement, "format")
    descriptor = None
    for klass in website::DatePathElement.__mro__:
        if "format" in klass.__dict__:
            descriptor = klass.__dict__["format"]
            break
    assert isinstance(descriptor, property)



def test_website::staticpathelement_is_not_abstract():
    assert not inspect.isabstract(website::StaticPathElement)


def test_website::staticpathelement_constructor_exists():
    assert callable(website::StaticPathElement.__init__)


def test_website::staticpathelement_constructor_args():
    sig = inspect.signature(website::StaticPathElement.__init__)
    params = list(sig.parameters.keys())
    assert "element" in params, "Missing parameter 'element'"

def test_website::staticpathelement_has_element():
    assert hasattr(website::StaticPathElement, "element")
    descriptor = None
    for klass in website::StaticPathElement.__mro__:
        if "element" in klass.__dict__:
            descriptor = klass.__dict__["element"]
            break
    assert isinstance(descriptor, property)



def test_website::pathelement_is_not_abstract():
    assert not inspect.isabstract(website::PathElement)


def test_website::pathelement_constructor_exists():
    assert callable(website::PathElement.__init__)


def test_website::pathelement_constructor_args():
    sig = inspect.signature(website::PathElement.__init__)
    params = list(sig.parameters.keys())



def test_website::resourceattribute_is_not_abstract():
    assert not inspect.isabstract(website::ResourceAttribute)


def test_website::resourceattribute_constructor_exists():
    assert callable(website::ResourceAttribute.__init__)


def test_website::resourceattribute_constructor_args():
    sig = inspect.signature(website::ResourceAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "validUploadExtensions" in params, "Missing parameter 'validUploadExtensions'"
    assert "maximumUploadSize" in params, "Missing parameter 'maximumUploadSize'"
    assert "uploadsWithinWebsite" in params, "Missing parameter 'uploadsWithinWebsite'"
    assert "validUploadMimeTypes" in params, "Missing parameter 'validUploadMimeTypes'"

def test_website::resourceattribute_has_validUploadExtensions():
    assert hasattr(website::ResourceAttribute, "validUploadExtensions")
    descriptor = None
    for klass in website::ResourceAttribute.__mro__:
        if "validUploadExtensions" in klass.__dict__:
            descriptor = klass.__dict__["validUploadExtensions"]
            break
    assert isinstance(descriptor, property)

def test_website::resourceattribute_has_maximumUploadSize():
    assert hasattr(website::ResourceAttribute, "maximumUploadSize")
    descriptor = None
    for klass in website::ResourceAttribute.__mro__:
        if "maximumUploadSize" in klass.__dict__:
            descriptor = klass.__dict__["maximumUploadSize"]
            break
    assert isinstance(descriptor, property)

def test_website::resourceattribute_has_uploadsWithinWebsite():
    assert hasattr(website::ResourceAttribute, "uploadsWithinWebsite")
    descriptor = None
    for klass in website::ResourceAttribute.__mro__:
        if "uploadsWithinWebsite" in klass.__dict__:
            descriptor = klass.__dict__["uploadsWithinWebsite"]
            break
    assert isinstance(descriptor, property)

def test_website::resourceattribute_has_validUploadMimeTypes():
    assert hasattr(website::ResourceAttribute, "validUploadMimeTypes")
    descriptor = None
    for klass in website::ResourceAttribute.__mro__:
        if "validUploadMimeTypes" in klass.__dict__:
            descriptor = klass.__dict__["validUploadMimeTypes"]
            break
    assert isinstance(descriptor, property)



def test_website::urlattribute_is_not_abstract():
    assert not inspect.isabstract(website::UrlAttribute)


def test_website::urlattribute_constructor_exists():
    assert callable(website::UrlAttribute.__init__)


def test_website::urlattribute_constructor_args():
    sig = inspect.signature(website::UrlAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "displayValue" in params, "Missing parameter 'displayValue'"

def test_website::urlattribute_has_displayValue():
    assert hasattr(website::UrlAttribute, "displayValue")
    descriptor = None
    for klass in website::UrlAttribute.__mro__:
        if "displayValue" in klass.__dict__:
            descriptor = klass.__dict__["displayValue"]
            break
    assert isinstance(descriptor, property)



def test_website::dateattribute_is_not_abstract():
    assert not inspect.isabstract(website::DateAttribute)


def test_website::dateattribute_constructor_exists():
    assert callable(website::DateAttribute.__init__)


def test_website::dateattribute_constructor_args():
    sig = inspect.signature(website::DateAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "details" in params, "Missing parameter 'details'"
    assert "format" in params, "Missing parameter 'format'"

def test_website::dateattribute_has_details():
    assert hasattr(website::DateAttribute, "details")
    descriptor = None
    for klass in website::DateAttribute.__mro__:
        if "details" in klass.__dict__:
            descriptor = klass.__dict__["details"]
            break
    assert isinstance(descriptor, property)

def test_website::dateattribute_has_format():
    assert hasattr(website::DateAttribute, "format")
    descriptor = None
    for klass in website::DateAttribute.__mro__:
        if "format" in klass.__dict__:
            descriptor = klass.__dict__["format"]
            break
    assert isinstance(descriptor, property)

def test_frameworktechnologies_exists():
    # Check that the Enumeration exists
    assert FrameworkTechnologies is not None

def test_frameworktechnologies_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FrameworkTechnologies]
    expected_literals = [
        "CakePHP",
        "Symfony",
        "Laravel",
        "Kohana",
        "JSF",
        "CodeIgniter",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FrameworkTechnologies"

def test_authenticationkeytypes_exists():
    # Check that the Enumeration exists
    assert AuthenticationKeyTypes is not None

def test_authenticationkeytypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AuthenticationKeyTypes]
    expected_literals = [
        "ScreenName",
        "Username",
        "Email",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AuthenticationKeyTypes"

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

def test_pagetopmenuoptions_exists():
    # Check that the Enumeration exists
    assert PageTopMenuOptions is not None

def test_pagetopmenuoptions_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PageTopMenuOptions]
    expected_literals = [
        "NeverInclude",
        "IncludeWhenAuthenticated",
        "AlwaysInclude",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PageTopMenuOptions"

def test_operationresulttypes_exists():
    # Check that the Enumeration exists
    assert OperationResultTypes is not None

def test_operationresulttypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OperationResultTypes]
    expected_literals = [
        "File",
        "None_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OperationResultTypes"

def test_indexdisplayoption_exists():
    # Check that the Enumeration exists
    assert IndexDisplayOption is not None

def test_indexdisplayoption_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IndexDisplayOption]
    expected_literals = [
        "Grid",
        "LineDirection",
        "PageDirection",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IndexDisplayOption"

def test_collectiondisplayoptions_exists():
    # Check that the Enumeration exists
    assert CollectionDisplayOptions is not None

def test_collectiondisplayoptions_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CollectionDisplayOptions]
    expected_literals = [
        "PageDirection",
        "LineDirection",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CollectionDisplayOptions"

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

def test_ishaschoices_exists():
    # Check that the Enumeration exists
    assert isHasChoices is not None

def test_ishaschoices_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in isHasChoices]
    expected_literals = [
        "isA",
        "hasA",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in isHasChoices"

def test_ormtechnologies_exists():
    # Check that the Enumeration exists
    assert OrmTechnologies is not None

def test_ormtechnologies_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OrmTechnologies]
    expected_literals = [
        "Kohana",
        "DataMapper",
        "JPA",
        "DoctrineODM",
        "Idiorm",
        "DoctrineORM",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OrmTechnologies"

def test_cardinality_exists():
    # Check that the Enumeration exists
    assert Cardinality is not None

def test_cardinality_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Cardinality]
    expected_literals = [
        "Many",
        "Required",
        "Optional",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Cardinality"

def test_datedetails_exists():
    # Check that the Enumeration exists
    assert DateDetails is not None

def test_datedetails_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DateDetails]
    expected_literals = [
        "TimeOnly",
        "DateAndTime",
        "DateOnly",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DateDetails"

def test_inputtechnologies_exists():
    # Check that the Enumeration exists
    assert InputTechnologies is not None

def test_inputtechnologies_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InputTechnologies]
    expected_literals = [
        "jQueryUI",
        "Html",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InputTechnologies"


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
website::RouteParameterReference_strategy = st.builds(
    website::RouteParameterReference,
    name=
        safe_text
)
website::FeatureReference_strategy = st.builds(
    website::FeatureReference,
    name=
        safe_text
)
website::CurrentUserReference_strategy = st.builds(
    website::CurrentUserReference,
)
website::ModelReference_strategy = st.builds(
    website::ModelReference,
)
website::ParameterReference_strategy = st.builds(
    website::ParameterReference,
    name=
        safe_text
)
website::InlineActionContainer_strategy = st.builds(
    website::InlineActionContainer,
)
AuthenticationUnit_strategy = st.builds(
    AuthenticationUnit,
)
website::AuthenticationUnit_strategy = st.builds(
    website::AuthenticationUnit,
)
EntityAttribute_strategy = st.builds(
    EntityAttribute,
)
website::DataTypeAttribute_strategy = st.builds(
    website::DataTypeAttribute,
    encrypt=
        st.booleans(),
    caseInsensitive=
        st.booleans(),
    obfuscateFormFields=
        st.booleans()
)
Attribute_strategy = st.builds(
    Attribute,
)
EntityFeature_strategy = st.builds(
    EntityFeature,
)
website::AssociationKey_strategy = st.builds(
    website::AssociationKey,
    targetColumnName=
        safe_text
)
Association_strategy = st.builds(
    Association,
)
website::LocationAttribute_strategy = st.builds(
    website::LocationAttribute,
)
ResourceAttribute_strategy = st.builds(
    ResourceAttribute,
)
website::ImageAttribute_strategy = st.builds(
    website::ImageAttribute,
)
website::FileAttribute_strategy = st.builds(
    website::FileAttribute,
)
EntityOrView_strategy = st.builds(
    EntityOrView,
)
website::Entity_strategy = st.builds(
    website::Entity,
)
website::EntityAssociation_strategy = st.builds(
    website::EntityAssociation,
    targetInputClass=
        safe_text,
    targetFeatureName=
        safe_text,
    targetDisplayLabel=
        safe_text,
    pivotTableName=
        safe_text,
    targetDisplayClass=
        safe_text,
    bidirectional=
        st.booleans(),
    targetFooterClass=
        safe_text,
    targetPrimaryKey=
        st.booleans(),
    targetHeaderClass=
        safe_text
)
ModelLabelFeature_strategy = st.builds(
    ModelLabelFeature,
)
website::ModelLabelAssociation_strategy = st.builds(
    website::ModelLabelAssociation,
    isSourceAssociation=
        st.booleans()
)
website::ModelLabelAttribute_strategy = st.builds(
    website::ModelLabelAttribute,
    dateFormat=
        safe_text
)
website::ModelLabelFeature_strategy = st.builds(
    website::ModelLabelFeature,
)
website::Label_strategy = st.builds(
    website::Label,
)
website::EntityAttribute_strategy = st.builds(
    website::EntityAttribute,
    interfaceType=
        safe_text,
    primaryKey=
        st.booleans(),
    containerUnique=
        st.booleans(),
    persistentType=
        safe_text,
    ormType=
        safe_text
)
website::Expression_strategy = st.builds(
    website::Expression,
)
Label_strategy = st.builds(
    Label,
)
Feature_strategy = st.builds(
    Feature,
)
website::Association_strategy = st.builds(
    website::Association,
    serializationMaxDepth=
        st.integers(),
    pseudo=
        st.booleans(),
    inputClass=
        safe_text
)
website::Feature_strategy = st.builds(
    website::Feature,
    displayClass=
        safe_text,
    encodeUriKey=
        st.booleans(),
    nullDisplayValue=
        safe_text,
    collectionAllowRemove=
        st.booleans(),
    serializationExpose=
        st.booleans(),
    headerClass=
        safe_text,
    collectionAllowAdd=
        st.booleans(),
    title=
        safe_text,
    serializationGroups=
        safe_text,
    footerClass=
        safe_text
)
DataType_strategy = st.builds(
    DataType,
)
website::EnumerationType_strategy = st.builds(
    website::EnumerationType,
)
website::NamedElement_strategy = st.builds(
    website::NamedElement,
    name=
        safe_text
)
Authentication_strategy = st.builds(
    Authentication,
)
website::CasAuthentication_strategy = st.builds(
    website::CasAuthentication,
)
website::LocalAuthenticationSystem_strategy = st.builds(
    website::LocalAuthenticationSystem,
    allowSelfRegistration=
        st.booleans(),
    allowRememberMe=
        st.booleans(),
    sendWelcomeEmail=
        st.booleans(),
    useEmailActivation=
        st.booleans(),
    authenticationKey=
        safe_text,
    trackLoginAttempts=
        st.booleans(),
    useCaptcha=
        st.booleans()
)
website::Attribute_strategy = st.builds(
    website::Attribute,
    validationPattern=
        safe_text,
    placeholder=
        safe_text,
    inputClass=
        safe_text
)
Classifier_strategy = st.builds(
    Classifier,
)
website::DataType_strategy = st.builds(
    website::DataType,
    persistentType=
        safe_text,
    validationPattern=
        safe_text,
    placeholder=
        safe_text,
    interfaceType=
        safe_text,
    ormType=
        safe_text
)
NamedDisplayElement_strategy = st.builds(
    NamedDisplayElement,
)
website::InlineAction_strategy = st.builds(
    website::InlineAction,
    footer=
        safe_text,
    headerClass=
        safe_text,
    disable=
        st.booleans(),
    header=
        safe_text,
    requiresRole=
        safe_text,
    footerClass=
        safe_text
)
website::EnumerationLiteral_strategy = st.builds(
    website::EnumerationLiteral,
)
website::EntityFeature_strategy = st.builds(
    website::EntityFeature,
    pluralisedName=
        safe_text,
    unique=
        st.booleans(),
    singletonName=
        safe_text,
    cardinality=
        safe_text,
    booleanIsHasChoice=
        safe_text,
    ordered=
        st.booleans(),
    columnName=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
website::ModelLabel_strategy = st.builds(
    website::ModelLabel,
    format=
        safe_text
)
website::NamedDisplayElement_strategy = st.builds(
    website::NamedDisplayElement,
    displayLabel=
        safe_text
)
website::Authentication_strategy = st.builds(
    website::Authentication,
    logoutLabel=
        safe_text,
    loginLabel=
        safe_text
)
website::ImageManipulation_strategy = st.builds(
    website::ImageManipulation,
    jpegQuality=
        st.integers()
)
website::EntityOrView_strategy = st.builds(
    website::EntityOrView,
    implementsUserInterface=
        st.booleans(),
    autoKeyGenerationStrategy=
        safe_text,
    singletonName=
        safe_text,
    autoKeyName=
        safe_text,
    serializationExcludeAll=
        st.booleans(),
    autoKeyPersistentType=
        safe_text,
    tableName=
        safe_text,
    pluralisedName=
        safe_text
)
website::Menu_strategy = st.builds(
    website::Menu,
    captionClass=
        safe_text,
    styleClass=
        safe_text,
    omitCaption=
        st.booleans(),
    layoutClass=
        safe_text
)
website::Service_strategy = st.builds(
    website::Service,
)
website::Classifier_strategy = st.builds(
    website::Classifier,
)
website::WebsiteProperties_strategy = st.builds(
    website::WebsiteProperties,
    baseURL=
        safe_text,
    topNavigationId=
        safe_text,
    metaDescription=
        safe_text,
    frameworkTechnology=
        safe_text,
    webmasterEmail=
        safe_text,
    defaultDateFormat=
        safe_text,
    siteTitle=
        safe_text,
    rewriteURLs=
        st.booleans(),
    defaultTimeFormat=
        safe_text,
    timestampCreation=
        st.booleans(),
    developmentVersion=
        st.booleans(),
    ormTechnology=
        safe_text,
    projectName=
        safe_text,
    inputTechnology=
        safe_text,
    databaseHost=
        safe_text,
    responsiveTopMenu=
        st.booleans(),
    defaultMaximumUploadSize=
        st.integers(),
    databasePrefix=
        safe_text,
    timestampUpdates=
        st.booleans(),
    copyrightText=
        safe_text,
    databasePassword=
        safe_text,
    siteTemplate=
        safe_text,
    databaseTechnology=
        safe_text,
    textEditorURL=
        safe_text,
    defaultDateTimeFormat=
        safe_text,
    testProjectName=
        safe_text,
    databaseName=
        safe_text,
    captchaSiteKey=
        safe_text,
    databasePort=
        safe_text,
    staticUnitsEditable=
        st.booleans(),
    ajaxTechnology=
        safe_text,
    captchaSecretKey=
        safe_text,
    databaseUsername=
        safe_text
)
website::WebGenModel_strategy = st.builds(
    website::WebGenModel,
)
ImageUnit_strategy = st.builds(
    ImageUnit,
)
website::SliderUnit_strategy = st.builds(
    website::SliderUnit,
    styleClass=
        safe_text,
    contentClass=
        safe_text
)
website::GalleryUnit_strategy = st.builds(
    website::GalleryUnit,
    contentClass=
        safe_text,
    styleClass=
        safe_text
)
InlineAction_strategy = st.builds(
    InlineAction,
)
website::FeatureSupportAction_strategy = st.builds(
    website::FeatureSupportAction,
    confirmMessage=
        safe_text,
    fileExtension=
        safe_text,
    uriElement=
        safe_text
)
website::DeleteAction_strategy = st.builds(
    website::DeleteAction,
    confirmMessage=
        safe_text,
    uriElement=
        safe_text
)
website::SelectAction_strategy = st.builds(
    website::SelectAction,
)
ChildPath_strategy = st.builds(
    ChildPath,
)
website::ChildPathAttribute_strategy = st.builds(
    website::ChildPathAttribute,
    name=
        safe_text
)
FeaturePath_strategy = st.builds(
    FeaturePath,
)
website::FeaturePathAttribute_strategy = st.builds(
    website::FeaturePathAttribute,
    name=
        safe_text
)
website::FeaturePath_strategy = st.builds(
    website::FeaturePath,
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
website::LoginUnit_strategy = st.builds(
    website::LoginUnit,
    styleClass=
        safe_text,
    logoutUriElement=
        safe_text
)
website::RegistrationUnit_strategy = st.builds(
    website::RegistrationUnit,
    styleClass=
        safe_text
)
website::ForgottenPasswordUnit_strategy = st.builds(
    website::ForgottenPasswordUnit,
    styleClass=
        safe_text
)
website::SearchUnit_strategy = st.builds(
    website::SearchUnit,
    styleClass=
        safe_text
)
SingletonUnit_strategy = st.builds(
    SingletonUnit,
)
DynamicUnit_strategy = st.builds(
    DynamicUnit,
)
website::ImageUnit_strategy = st.builds(
    website::ImageUnit,
    transitionTime=
        st.integers(),
    missingImagePath=
        safe_text,
    showTime=
        st.integers()
)
website::DataUnit_strategy = st.builds(
    website::DataUnit,
)
website::ControlUnit_strategy = st.builds(
    website::ControlUnit,
    submitLabel=
        safe_text,
    cancelLabel=
        safe_text,
    contentClass=
        safe_text
)
website::EditUnit_strategy = st.builds(
    website::EditUnit,
    cancelLabel=
        safe_text,
    confirmLabel=
        safe_text,
    contentClass=
        safe_text,
    customiseValues=
        st.booleans()
)
EditUnit_strategy = st.builds(
    EditUnit,
)
website::CreateUnit_strategy = st.builds(
    website::CreateUnit,
    styleClass=
        safe_text
)
InterfaceField_strategy = st.builds(
    InterfaceField,
)
website::DateField_strategy = st.builds(
    website::DateField,
    details=
        safe_text,
    format=
        safe_text
)
website::DataTypeField_strategy = st.builds(
    website::DataTypeField,
    obfuscateFormFields=
        st.booleans(),
    encrypt=
        st.booleans(),
    interfaceType=
        safe_text
)
website::ChildPath_strategy = st.builds(
    website::ChildPath,
)
website::AssociationReference_strategy = st.builds(
    website::AssociationReference,
    name=
        safe_text
)
SelectableUnit_strategy = st.builds(
    SelectableUnit,
)
website::CreateUpdateUnit_strategy = st.builds(
    website::CreateUpdateUnit,
    createUriElement=
        safe_text,
    clearLabel=
        safe_text,
    styleClass=
        safe_text
)
website::MapUnit_strategy = st.builds(
    website::MapUnit,
    defaultZoomLevel=
        st.integers(),
    styleClass=
        safe_text,
    readOnly=
        st.booleans()
)
website::UpdateUnit_strategy = st.builds(
    website::UpdateUnit,
    styleClass=
        safe_text
)
website::DetailsUnit_strategy = st.builds(
    website::DetailsUnit,
    onlyDisplayWhenNotEmpty=
        st.booleans(),
    omitFieldLabels=
        st.booleans(),
    contentClass=
        safe_text,
    styleClass=
        safe_text
)
website::CollectionUnit_strategy = st.builds(
    website::CollectionUnit,
    nextNpages=
        st.integers(),
    firstPageLabel=
        safe_text,
    useDisabledPageLinks=
        st.booleans(),
    defaultPaginationSize=
        st.integers(),
    previousNpages=
        st.integers(),
    lastPageLabel=
        safe_text,
    previousPageLabel=
        safe_text,
    nextPageLabel=
        safe_text,
    useFirstLastPageLinks=
        st.booleans(),
    emptyMessage=
        safe_text
)
website::SingletonUnit_strategy = st.builds(
    website::SingletonUnit,
)
website::SelectableUnit_strategy = st.builds(
    website::SelectableUnit,
)
website::CaptchaField_strategy = st.builds(
    website::CaptchaField,
)
UnitFeature_strategy = st.builds(
    UnitFeature,
)
website::UnitElement_strategy = st.builds(
    website::UnitElement,
    name=
        safe_text,
    validationPattern=
        safe_text,
    obfuscateFormFields=
        st.booleans(),
    placeholder=
        safe_text
)
InlineActionContainer_strategy = st.builds(
    InlineActionContainer,
)
website::ImageIndexUnit_strategy = st.builds(
    website::ImageIndexUnit,
    contentClass=
        safe_text,
    styleClass=
        safe_text
)
website::IndexUnit_strategy = st.builds(
    website::IndexUnit,
    styleClass=
        safe_text,
    contentClass=
        safe_text,
    displayOption=
        safe_text,
    omitColumnLabels=
        st.booleans(),
    rowClasses=
        safe_text
)
UnitField_strategy = st.builds(
    UnitField,
)
website::InterfaceField_strategy = st.builds(
    website::InterfaceField,
    inputClass=
        safe_text,
    required=
        st.booleans(),
    defaultValue=
        safe_text,
    placeholder=
        safe_text,
    validationPattern=
        safe_text
)
website::UnitFeature_strategy = st.builds(
    website::UnitFeature,
    footerClass=
        safe_text,
    inputClass=
        safe_text,
    displayLabel=
        safe_text,
    required=
        st.booleans(),
    autofocus=
        st.booleans(),
    headerClass=
        safe_text,
    displayClass=
        safe_text,
    onlyDisplayWhenNotEmpty=
        st.booleans(),
    nullDisplayValue=
        safe_text,
    footer=
        safe_text
)
AssociationReference_strategy = st.builds(
    AssociationReference,
)
website::ChildPathAssociation_strategy = st.builds(
    website::ChildPathAssociation,
    isSourceAssociation=
        st.booleans()
)
website::FeaturePathAssociation_strategy = st.builds(
    website::FeaturePathAssociation,
    isSourceAssociation=
        st.booleans()
)
ContentUnit_strategy = st.builds(
    ContentUnit,
)
website::CreateSitemapUnit_strategy = st.builds(
    website::CreateSitemapUnit,
    filename=
        safe_text,
    styleClass=
        safe_text,
    deployedURL=
        safe_text,
    contentClass=
        safe_text
)
website::DynamicUnit_strategy = st.builds(
    website::DynamicUnit,
    footerClass=
        safe_text,
    errorClass=
        safe_text,
    footer=
        safe_text,
    headerClass=
        safe_text,
    header=
        safe_text,
    controlClass=
        safe_text
)
website::StaticUnit_strategy = st.builds(
    website::StaticUnit,
    styleClass=
        safe_text,
    contentClass=
        safe_text,
    content=
        safe_text
)
website::UnitContainer_strategy = st.builds(
    website::UnitContainer,
)
website::UnitSupportAction_strategy = st.builds(
    website::UnitSupportAction,
    disable=
        st.booleans(),
    confirmMessage=
        safe_text
)
website::UnitField_strategy = st.builds(
    website::UnitField,
    title=
        safe_text,
    dateFormat=
        safe_text,
    collectionAllowRemove=
        st.booleans(),
    collectionDisplayOption=
        safe_text,
    collectionAllowAdd=
        st.booleans(),
    maximumDisplaySize=
        st.integers()
)
website::Filter_strategy = st.builds(
    website::Filter,
)
website::Query_strategy = st.builds(
    website::Query,
)
website::ContentUnit_strategy = st.builds(
    website::ContentUnit,
    captionClass=
        safe_text,
    createDefaultUriElement=
        st.booleans(),
    requiresRole=
        safe_text,
    purposeSummary=
        safe_text,
    omitCaption=
        st.booleans(),
    uriElement=
        safe_text,
    alternative=
        safe_text
)
MenuEntry_strategy = st.builds(
    MenuEntry,
)
website::EditStaticTextMenuEntry_strategy = st.builds(
    website::EditStaticTextMenuEntry,
)
website::MenuFeature_strategy = st.builds(
    website::MenuFeature,
)
website::ActionMenuEntry_strategy = st.builds(
    website::ActionMenuEntry,
)
Menu_strategy = st.builds(
    Menu,
)
website::DynamicMenu_strategy = st.builds(
    website::DynamicMenu,
)
website::StaticMenu_strategy = st.builds(
    website::StaticMenu,
)
website::MenuEntry_strategy = st.builds(
    website::MenuEntry,
    requiresRole=
        safe_text
)
website::QueryParameter_strategy = st.builds(
    website::QueryParameter,
    value=
        safe_text
)
website::FilterParameter_strategy = st.builds(
    website::FilterParameter,
    placeholder=
        safe_text,
    defaultValue=
        safe_text
)
UnitContainer_strategy = st.builds(
    UnitContainer,
)
website::Page_strategy = st.builds(
    website::Page,
    navigationLabel=
        safe_text,
    topMenuRank=
        st.integers(),
    styleClass=
        safe_text,
    topMenuOption=
        safe_text,
    authenticated=
        st.booleans(),
    uriElement=
        safe_text
)
website::UnitAssociation_strategy = st.builds(
    website::UnitAssociation,
    isSourceAssociation=
        st.booleans()
)
ImageFilter_strategy = st.builds(
    ImageFilter,
)
website::ThumbnailFilter_strategy = st.builds(
    website::ThumbnailFilter,
    height=
        st.integers(),
    width=
        st.integers()
)
website::ImageFilter_strategy = st.builds(
    website::ImageFilter,
)
website::Order_strategy = st.builds(
    website::Order,
)
website::Predicate_strategy = st.builds(
    website::Predicate,
)
website::PageLink_strategy = st.builds(
    website::PageLink,
)
website::SelectionParameter_strategy = st.builds(
    website::SelectionParameter,
    optional=
        st.booleans(),
    defaultValue=
        safe_text
)
website::BusinessOperation_strategy = st.builds(
    website::BusinessOperation,
    resultType=
        safe_text,
    resultMimeType=
        safe_text
)
website::Selection_strategy = st.builds(
    website::Selection,
    distinct=
        st.booleans(),
    selected=
        st.booleans(),
    limit=
        st.integers()
)
website::View_strategy = st.builds(
    website::View,
)
EntityAssociation_strategy = st.builds(
    EntityAssociation,
)
website::AssociationWithContainment_strategy = st.builds(
    website::AssociationWithContainment,
    sourceVisible=
        st.booleans()
)
website::AssociationWithoutContainment_strategy = st.builds(
    website::AssociationWithoutContainment,
    targetCardinality=
        safe_text,
    targetUnique=
        st.booleans()
)
EncapsulatedFeature_strategy = st.builds(
    EncapsulatedFeature,
)
website::EncapsulatedAssociation_strategy = st.builds(
    website::EncapsulatedAssociation,
    name=
        safe_text,
    isSourceAssociation=
        st.booleans(),
    cardinality=
        safe_text
)
website::EncapsulatedAttribute_strategy = st.builds(
    website::EncapsulatedAttribute,
    name=
        safe_text,
    cardinality=
        safe_text
)
ViewFeature_strategy = st.builds(
    ViewFeature,
)
website::ViewAssociation_strategy = st.builds(
    website::ViewAssociation,
    cardinality=
        safe_text
)
website::EncapsulatedFeature_strategy = st.builds(
    website::EncapsulatedFeature,
    columnName=
        safe_text,
    alias=
        safe_text,
    displayLabel=
        safe_text
)
website::ViewFeature_strategy = st.builds(
    website::ViewFeature,
)
PathElement_strategy = st.builds(
    PathElement,
)
website::DatePathElement_strategy = st.builds(
    website::DatePathElement,
    format=
        safe_text
)
website::StaticPathElement_strategy = st.builds(
    website::StaticPathElement,
    element=
        safe_text
)
website::PathElement_strategy = st.builds(
    website::PathElement,
)
website::ResourceAttribute_strategy = st.builds(
    website::ResourceAttribute,
    validUploadExtensions=
        safe_text,
    maximumUploadSize=
        st.integers(),
    uploadsWithinWebsite=
        st.booleans(),
    validUploadMimeTypes=
        safe_text
)
website::UrlAttribute_strategy = st.builds(
    website::UrlAttribute,
    displayValue=
        safe_text
)
website::DateAttribute_strategy = st.builds(
    website::DateAttribute,
    details=
        safe_text,
    format=
        safe_text
)

@given(instance=Path_strategy)
@settings(max_examples=50)
def test_path_instantiation(instance):
    assert isinstance(instance, Path)

@given(instance=website::RouteParameterReference_strategy)
@settings(max_examples=50)
def test_website::routeparameterreference_instantiation(instance):
    assert isinstance(instance, website::RouteParameterReference)

@given(instance=website::RouteParameterReference_strategy)
def test_website::routeparameterreference_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=website::RouteParameterReference_strategy)
def test_website::routeparameterreference_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=website::FeatureReference_strategy)
@settings(max_examples=50)
def test_website::featurereference_instantiation(instance):
    assert isinstance(instance, website::FeatureReference)

@given(instance=website::FeatureReference_strategy)
def test_website::featurereference_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=website::FeatureReference_strategy)
def test_website::featurereference_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=website::CurrentUserReference_strategy)
@settings(max_examples=50)
def test_website::currentuserreference_instantiation(instance):
    assert isinstance(instance, website::CurrentUserReference)

@given(instance=website::ModelReference_strategy)
@settings(max_examples=50)
def test_website::modelreference_instantiation(instance):
    assert isinstance(instance, website::ModelReference)

@given(instance=website::ParameterReference_strategy)
@settings(max_examples=50)
def test_website::parameterreference_instantiation(instance):
    assert isinstance(instance, website::ParameterReference)

@given(instance=website::ParameterReference_strategy)
def test_website::parameterreference_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=website::ParameterReference_strategy)
def test_website::parameterreference_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=website::InlineActionContainer_strategy)
@settings(max_examples=50)
def test_website::inlineactioncontainer_instantiation(instance):
    assert isinstance(instance, website::InlineActionContainer)

@given(instance=AuthenticationUnit_strategy)
@settings(max_examples=50)
def test_authenticationunit_instantiation(instance):
    assert isinstance(instance, AuthenticationUnit)

@given(instance=website::AuthenticationUnit_strategy)
@settings(max_examples=50)
def test_website::authenticationunit_instantiation(instance):
    assert isinstance(instance, website::AuthenticationUnit)

@given(instance=EntityAttribute_strategy)
@settings(max_examples=50)
def test_entityattribute_instantiation(instance):
    assert isinstance(instance, EntityAttribute)

@given(instance=website::DataTypeAttribute_strategy)
@settings(max_examples=50)
def test_website::datatypeattribute_instantiation(instance):
    assert isinstance(instance, website::DataTypeAttribute)

@given(instance=website::DataTypeAttribute_strategy)
def test_website::datatypeattribute_encrypt_type(instance):
    assert isinstance(instance.encrypt, bool)


@given(instance=website::DataTypeAttribute_strategy)
def test_website::datatypeattribute_encrypt_setter(instance):
    original = instance.encrypt
    instance.encrypt = original
    assert instance.encrypt == original

@given(instance=website::DataTypeAttribute_strategy)
def test_website::datatypeattribute_caseInsensitive_type(instance):
    assert isinstance(instance.caseInsensitive, bool)


@given(instance=website::DataTypeAttribute_strategy)
def test_website::datatypeattribute_caseInsensitive_setter(instance):
    original = instance.caseInsensitive
    instance.caseInsensitive = original
    assert instance.caseInsensitive == original

@given(instance=website::DataTypeAttribute_strategy)
def test_website::datatypeattribute_obfuscateFormFields_type(instance):
    assert isinstance(instance.obfuscateFormFields, bool)


@given(instance=website::DataTypeAttribute_strategy)
def test_website::datatypeattribute_obfuscateFormFields_setter(instance):
    original = instance.obfuscateFormFields
    instance.obfuscateFormFields = original
    assert instance.obfuscateFormFields == original

@given(instance=Attribute_strategy)
@settings(max_examples=50)
def test_attribute_instantiation(instance):
    assert isinstance(instance, Attribute)

@given(instance=EntityFeature_strategy)
@settings(max_examples=50)
def test_entityfeature_instantiation(instance):
    assert isinstance(instance, EntityFeature)

@given(instance=website::AssociationKey_strategy)
@settings(max_examples=50)
def test_website::associationkey_instantiation(instance):
    assert isinstance(instance, website::AssociationKey)

@given(instance=website::AssociationKey_strategy)
def test_website::associationkey_targetColumnName_type(instance):
    assert isinstance(instance.targetColumnName, str)


@given(instance=website::AssociationKey_strategy)
def test_website::associationkey_targetColumnName_setter(instance):
    original = instance.targetColumnName
    instance.targetColumnName = original
    assert instance.targetColumnName == original

@given(instance=Association_strategy)
@settings(max_examples=50)
def test_association_instantiation(instance):
    assert isinstance(instance, Association)

@given(instance=website::LocationAttribute_strategy)
@settings(max_examples=50)
def test_website::locationattribute_instantiation(instance):
    assert isinstance(instance, website::LocationAttribute)

@given(instance=ResourceAttribute_strategy)
@settings(max_examples=50)
def test_resourceattribute_instantiation(instance):
    assert isinstance(instance, ResourceAttribute)

@given(instance=website::ImageAttribute_strategy)
@settings(max_examples=50)
def test_website::imageattribute_instantiation(instance):
    assert isinstance(instance, website::ImageAttribute)

@given(instance=website::FileAttribute_strategy)
@settings(max_examples=50)
def test_website::fileattribute_instantiation(instance):
    assert isinstance(instance, website::FileAttribute)

@given(instance=EntityOrView_strategy)
@settings(max_examples=50)
def test_entityorview_instantiation(instance):
    assert isinstance(instance, EntityOrView)

@given(instance=website::Entity_strategy)
@settings(max_examples=50)
def test_website::entity_instantiation(instance):
    assert isinstance(instance, website::Entity)

@given(instance=website::EntityAssociation_strategy)
@settings(max_examples=50)
def test_website::entityassociation_instantiation(instance):
    assert isinstance(instance, website::EntityAssociation)

@given(instance=website::EntityAssociation_strategy)
def test_website::entityassociation_targetInputClass_type(instance):
    assert isinstance(instance.targetInputClass, str)


@given(instance=website::EntityAssociation_strategy)
def test_website::entityassociation_targetInputClass_setter(instance):
    original = instance.targetInputClass
    instance.targetInputClass = original
    assert instance.targetInputClass == original

@given(instance=website::EntityAssociation_strategy)
def test_website::entityassociation_targetFeatureName_type(instance):
    assert isinstance(instance.targetFeatureName, str)


@given(instance=website::EntityAssociation_strategy)
def test_website::entityassociation_targetFeatureName_setter(instance):
    original = instance.targetFeatureName
    instance.targetFeatureName = original
    assert instance.targetFeatureName == original

@given(instance=website::EntityAssociation_strategy)
def test_website::entityassociation_targetDisplayLabel_type(instance):
    assert isinstance(instance.targetDisplayLabel, str)


@given(instance=website::EntityAssociation_strategy)
def test_website::entityassociation_targetDisplayLabel_setter(instance):
    original = instance.targetDisplayLabel
    instance.targetDisplayLabel = original
    assert instance.targetDisplayLabel == original

@given(instance=website::EntityAssociation_strategy)
def test_website::entityassociation_pivotTableName_type(instance):
    assert isinstance(instance.pivotTableName, str)


@given(instance=website::EntityAssociation_strategy)
def test_website::entityassociation_pivotTableName_setter(instance):
    original = instance.pivotTableName
    instance.pivotTableName = original
    assert instance.pivotTableName == original

@given(instance=website::EntityAssociation_strategy)
def test_website::entityassociation_targetDisplayClass_type(instance):
    assert isinstance(instance.targetDisplayClass, str)


@given(instance=website::EntityAssociation_strategy)
def test_website::entityassociation_targetDisplayClass_setter(instance):
    original = instance.targetDisplayClass
    instance.targetDisplayClass = original
    assert instance.targetDisplayClass == original

@given(instance=website::EntityAssociation_strategy)
def test_website::entityassociation_bidirectional_type(instance):
    assert isinstance(instance.bidirectional, bool)


@given(instance=website::EntityAssociation_strategy)
def test_website::entityassociation_bidirectional_setter(instance):
    original = instance.bidirectional
    instance.bidirectional = original
    assert instance.bidirectional == original

@given(instance=website::EntityAssociation_strategy)
def test_website::entityassociation_targetFooterClass_type(instance):
    assert isinstance(instance.targetFooterClass, str)


@given(instance=website::EntityAssociation_strategy)
def test_website::entityassociation_targetFooterClass_setter(instance):
    original = instance.targetFooterClass
    instance.targetFooterClass = original
    assert instance.targetFooterClass == original

@given(instance=website::EntityAssociation_strategy)
def test_website::entityassociation_targetPrimaryKey_type(instance):
    assert isinstance(instance.targetPrimaryKey, bool)


@given(instance=website::EntityAssociation_strategy)
def test_website::entityassociation_targetPrimaryKey_setter(instance):
    original = instance.targetPrimaryKey
    instance.targetPrimaryKey = original
    assert instance.targetPrimaryKey == original

@given(instance=website::EntityAssociation_strategy)
def test_website::entityassociation_targetHeaderClass_type(instance):
    assert isinstance(instance.targetHeaderClass, str)


@given(instance=website::EntityAssociation_strategy)
def test_website::entityassociation_targetHeaderClass_setter(instance):
    original = instance.targetHeaderClass
    instance.targetHeaderClass = original
    assert instance.targetHeaderClass == original

@given(instance=ModelLabelFeature_strategy)
@settings(max_examples=50)
def test_modellabelfeature_instantiation(instance):
    assert isinstance(instance, ModelLabelFeature)

@given(instance=website::ModelLabelAssociation_strategy)
@settings(max_examples=50)
def test_website::modellabelassociation_instantiation(instance):
    assert isinstance(instance, website::ModelLabelAssociation)

@given(instance=website::ModelLabelAssociation_strategy)
def test_website::modellabelassociation_isSourceAssociation_type(instance):
    assert isinstance(instance.isSourceAssociation, bool)


@given(instance=website::ModelLabelAssociation_strategy)
def test_website::modellabelassociation_isSourceAssociation_setter(instance):
    original = instance.isSourceAssociation
    instance.isSourceAssociation = original
    assert instance.isSourceAssociation == original

@given(instance=website::ModelLabelAttribute_strategy)
@settings(max_examples=50)
def test_website::modellabelattribute_instantiation(instance):
    assert isinstance(instance, website::ModelLabelAttribute)

@given(instance=website::ModelLabelAttribute_strategy)
def test_website::modellabelattribute_dateFormat_type(instance):
    assert isinstance(instance.dateFormat, str)


@given(instance=website::ModelLabelAttribute_strategy)
def test_website::modellabelattribute_dateFormat_setter(instance):
    original = instance.dateFormat
    instance.dateFormat = original
    assert instance.dateFormat == original

@given(instance=website::ModelLabelFeature_strategy)
@settings(max_examples=50)
def test_website::modellabelfeature_instantiation(instance):
    assert isinstance(instance, website::ModelLabelFeature)

@given(instance=website::Label_strategy)
@settings(max_examples=50)
def test_website::label_instantiation(instance):
    assert isinstance(instance, website::Label)

@given(instance=website::EntityAttribute_strategy)
@settings(max_examples=50)
def test_website::entityattribute_instantiation(instance):
    assert isinstance(instance, website::EntityAttribute)

@given(instance=website::EntityAttribute_strategy)
def test_website::entityattribute_interfaceType_type(instance):
    assert isinstance(instance.interfaceType, str)


@given(instance=website::EntityAttribute_strategy)
def test_website::entityattribute_interfaceType_setter(instance):
    original = instance.interfaceType
    instance.interfaceType = original
    assert instance.interfaceType == original

@given(instance=website::EntityAttribute_strategy)
def test_website::entityattribute_primaryKey_type(instance):
    assert isinstance(instance.primaryKey, bool)


@given(instance=website::EntityAttribute_strategy)
def test_website::entityattribute_primaryKey_setter(instance):
    original = instance.primaryKey
    instance.primaryKey = original
    assert instance.primaryKey == original

@given(instance=website::EntityAttribute_strategy)
def test_website::entityattribute_containerUnique_type(instance):
    assert isinstance(instance.containerUnique, bool)


@given(instance=website::EntityAttribute_strategy)
def test_website::entityattribute_containerUnique_setter(instance):
    original = instance.containerUnique
    instance.containerUnique = original
    assert instance.containerUnique == original

@given(instance=website::EntityAttribute_strategy)
def test_website::entityattribute_persistentType_type(instance):
    assert isinstance(instance.persistentType, str)


@given(instance=website::EntityAttribute_strategy)
def test_website::entityattribute_persistentType_setter(instance):
    original = instance.persistentType
    instance.persistentType = original
    assert instance.persistentType == original

@given(instance=website::EntityAttribute_strategy)
def test_website::entityattribute_ormType_type(instance):
    assert isinstance(instance.ormType, str)


@given(instance=website::EntityAttribute_strategy)
def test_website::entityattribute_ormType_setter(instance):
    original = instance.ormType
    instance.ormType = original
    assert instance.ormType == original

@given(instance=website::Expression_strategy)
@settings(max_examples=50)
def test_website::expression_instantiation(instance):
    assert isinstance(instance, website::Expression)

@given(instance=Label_strategy)
@settings(max_examples=50)
def test_label_instantiation(instance):
    assert isinstance(instance, Label)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=website::Association_strategy)
@settings(max_examples=50)
def test_website::association_instantiation(instance):
    assert isinstance(instance, website::Association)

@given(instance=website::Association_strategy)
def test_website::association_serializationMaxDepth_type(instance):
    assert isinstance(instance.serializationMaxDepth, int)


@given(instance=website::Association_strategy)
def test_website::association_serializationMaxDepth_setter(instance):
    original = instance.serializationMaxDepth
    instance.serializationMaxDepth = original
    assert instance.serializationMaxDepth == original

@given(instance=website::Association_strategy)
def test_website::association_pseudo_type(instance):
    assert isinstance(instance.pseudo, bool)


@given(instance=website::Association_strategy)
def test_website::association_pseudo_setter(instance):
    original = instance.pseudo
    instance.pseudo = original
    assert instance.pseudo == original

@given(instance=website::Association_strategy)
def test_website::association_inputClass_type(instance):
    assert isinstance(instance.inputClass, str)


@given(instance=website::Association_strategy)
def test_website::association_inputClass_setter(instance):
    original = instance.inputClass
    instance.inputClass = original
    assert instance.inputClass == original

@given(instance=website::Feature_strategy)
@settings(max_examples=50)
def test_website::feature_instantiation(instance):
    assert isinstance(instance, website::Feature)

@given(instance=website::Feature_strategy)
def test_website::feature_displayClass_type(instance):
    assert isinstance(instance.displayClass, str)


@given(instance=website::Feature_strategy)
def test_website::feature_displayClass_setter(instance):
    original = instance.displayClass
    instance.displayClass = original
    assert instance.displayClass == original

@given(instance=website::Feature_strategy)
def test_website::feature_encodeUriKey_type(instance):
    assert isinstance(instance.encodeUriKey, bool)


@given(instance=website::Feature_strategy)
def test_website::feature_encodeUriKey_setter(instance):
    original = instance.encodeUriKey
    instance.encodeUriKey = original
    assert instance.encodeUriKey == original

@given(instance=website::Feature_strategy)
def test_website::feature_nullDisplayValue_type(instance):
    assert isinstance(instance.nullDisplayValue, str)


@given(instance=website::Feature_strategy)
def test_website::feature_nullDisplayValue_setter(instance):
    original = instance.nullDisplayValue
    instance.nullDisplayValue = original
    assert instance.nullDisplayValue == original

@given(instance=website::Feature_strategy)
def test_website::feature_collectionAllowRemove_type(instance):
    assert isinstance(instance.collectionAllowRemove, bool)


@given(instance=website::Feature_strategy)
def test_website::feature_collectionAllowRemove_setter(instance):
    original = instance.collectionAllowRemove
    instance.collectionAllowRemove = original
    assert instance.collectionAllowRemove == original

@given(instance=website::Feature_strategy)
def test_website::feature_serializationExpose_type(instance):
    assert isinstance(instance.serializationExpose, bool)


@given(instance=website::Feature_strategy)
def test_website::feature_serializationExpose_setter(instance):
    original = instance.serializationExpose
    instance.serializationExpose = original
    assert instance.serializationExpose == original

@given(instance=website::Feature_strategy)
def test_website::feature_headerClass_type(instance):
    assert isinstance(instance.headerClass, str)


@given(instance=website::Feature_strategy)
def test_website::feature_headerClass_setter(instance):
    original = instance.headerClass
    instance.headerClass = original
    assert instance.headerClass == original

@given(instance=website::Feature_strategy)
def test_website::feature_collectionAllowAdd_type(instance):
    assert isinstance(instance.collectionAllowAdd, bool)


@given(instance=website::Feature_strategy)
def test_website::feature_collectionAllowAdd_setter(instance):
    original = instance.collectionAllowAdd
    instance.collectionAllowAdd = original
    assert instance.collectionAllowAdd == original

@given(instance=website::Feature_strategy)
def test_website::feature_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=website::Feature_strategy)
def test_website::feature_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=website::Feature_strategy)
def test_website::feature_serializationGroups_type(instance):
    assert isinstance(instance.serializationGroups, str)


@given(instance=website::Feature_strategy)
def test_website::feature_serializationGroups_setter(instance):
    original = instance.serializationGroups
    instance.serializationGroups = original
    assert instance.serializationGroups == original

@given(instance=website::Feature_strategy)
def test_website::feature_footerClass_type(instance):
    assert isinstance(instance.footerClass, str)


@given(instance=website::Feature_strategy)
def test_website::feature_footerClass_setter(instance):
    original = instance.footerClass
    instance.footerClass = original
    assert instance.footerClass == original

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=website::EnumerationType_strategy)
@settings(max_examples=50)
def test_website::enumerationtype_instantiation(instance):
    assert isinstance(instance, website::EnumerationType)

@given(instance=website::NamedElement_strategy)
@settings(max_examples=50)
def test_website::namedelement_instantiation(instance):
    assert isinstance(instance, website::NamedElement)

@given(instance=website::NamedElement_strategy)
def test_website::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=website::NamedElement_strategy)
def test_website::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Authentication_strategy)
@settings(max_examples=50)
def test_authentication_instantiation(instance):
    assert isinstance(instance, Authentication)

@given(instance=website::CasAuthentication_strategy)
@settings(max_examples=50)
def test_website::casauthentication_instantiation(instance):
    assert isinstance(instance, website::CasAuthentication)

@given(instance=website::LocalAuthenticationSystem_strategy)
@settings(max_examples=50)
def test_website::localauthenticationsystem_instantiation(instance):
    assert isinstance(instance, website::LocalAuthenticationSystem)

@given(instance=website::LocalAuthenticationSystem_strategy)
def test_website::localauthenticationsystem_allowSelfRegistration_type(instance):
    assert isinstance(instance.allowSelfRegistration, bool)


@given(instance=website::LocalAuthenticationSystem_strategy)
def test_website::localauthenticationsystem_allowSelfRegistration_setter(instance):
    original = instance.allowSelfRegistration
    instance.allowSelfRegistration = original
    assert instance.allowSelfRegistration == original

@given(instance=website::LocalAuthenticationSystem_strategy)
def test_website::localauthenticationsystem_allowRememberMe_type(instance):
    assert isinstance(instance.allowRememberMe, bool)


@given(instance=website::LocalAuthenticationSystem_strategy)
def test_website::localauthenticationsystem_allowRememberMe_setter(instance):
    original = instance.allowRememberMe
    instance.allowRememberMe = original
    assert instance.allowRememberMe == original

@given(instance=website::LocalAuthenticationSystem_strategy)
def test_website::localauthenticationsystem_sendWelcomeEmail_type(instance):
    assert isinstance(instance.sendWelcomeEmail, bool)


@given(instance=website::LocalAuthenticationSystem_strategy)
def test_website::localauthenticationsystem_sendWelcomeEmail_setter(instance):
    original = instance.sendWelcomeEmail
    instance.sendWelcomeEmail = original
    assert instance.sendWelcomeEmail == original

@given(instance=website::LocalAuthenticationSystem_strategy)
def test_website::localauthenticationsystem_useEmailActivation_type(instance):
    assert isinstance(instance.useEmailActivation, bool)


@given(instance=website::LocalAuthenticationSystem_strategy)
def test_website::localauthenticationsystem_useEmailActivation_setter(instance):
    original = instance.useEmailActivation
    instance.useEmailActivation = original
    assert instance.useEmailActivation == original

@given(instance=website::LocalAuthenticationSystem_strategy)
def test_website::localauthenticationsystem_authenticationKey_type(instance):
    assert isinstance(instance.authenticationKey, str)


@given(instance=website::LocalAuthenticationSystem_strategy)
def test_website::localauthenticationsystem_authenticationKey_setter(instance):
    original = instance.authenticationKey
    instance.authenticationKey = original
    assert instance.authenticationKey == original

@given(instance=website::LocalAuthenticationSystem_strategy)
def test_website::localauthenticationsystem_trackLoginAttempts_type(instance):
    assert isinstance(instance.trackLoginAttempts, bool)


@given(instance=website::LocalAuthenticationSystem_strategy)
def test_website::localauthenticationsystem_trackLoginAttempts_setter(instance):
    original = instance.trackLoginAttempts
    instance.trackLoginAttempts = original
    assert instance.trackLoginAttempts == original

@given(instance=website::LocalAuthenticationSystem_strategy)
def test_website::localauthenticationsystem_useCaptcha_type(instance):
    assert isinstance(instance.useCaptcha, bool)


@given(instance=website::LocalAuthenticationSystem_strategy)
def test_website::localauthenticationsystem_useCaptcha_setter(instance):
    original = instance.useCaptcha
    instance.useCaptcha = original
    assert instance.useCaptcha == original

@given(instance=website::Attribute_strategy)
@settings(max_examples=50)
def test_website::attribute_instantiation(instance):
    assert isinstance(instance, website::Attribute)

@given(instance=website::Attribute_strategy)
def test_website::attribute_validationPattern_type(instance):
    assert isinstance(instance.validationPattern, str)


@given(instance=website::Attribute_strategy)
def test_website::attribute_validationPattern_setter(instance):
    original = instance.validationPattern
    instance.validationPattern = original
    assert instance.validationPattern == original

@given(instance=website::Attribute_strategy)
def test_website::attribute_placeholder_type(instance):
    assert isinstance(instance.placeholder, str)


@given(instance=website::Attribute_strategy)
def test_website::attribute_placeholder_setter(instance):
    original = instance.placeholder
    instance.placeholder = original
    assert instance.placeholder == original

@given(instance=website::Attribute_strategy)
def test_website::attribute_inputClass_type(instance):
    assert isinstance(instance.inputClass, str)


@given(instance=website::Attribute_strategy)
def test_website::attribute_inputClass_setter(instance):
    original = instance.inputClass
    instance.inputClass = original
    assert instance.inputClass == original

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=website::DataType_strategy)
@settings(max_examples=50)
def test_website::datatype_instantiation(instance):
    assert isinstance(instance, website::DataType)

@given(instance=website::DataType_strategy)
def test_website::datatype_persistentType_type(instance):
    assert isinstance(instance.persistentType, str)


@given(instance=website::DataType_strategy)
def test_website::datatype_persistentType_setter(instance):
    original = instance.persistentType
    instance.persistentType = original
    assert instance.persistentType == original

@given(instance=website::DataType_strategy)
def test_website::datatype_validationPattern_type(instance):
    assert isinstance(instance.validationPattern, str)


@given(instance=website::DataType_strategy)
def test_website::datatype_validationPattern_setter(instance):
    original = instance.validationPattern
    instance.validationPattern = original
    assert instance.validationPattern == original

@given(instance=website::DataType_strategy)
def test_website::datatype_placeholder_type(instance):
    assert isinstance(instance.placeholder, str)


@given(instance=website::DataType_strategy)
def test_website::datatype_placeholder_setter(instance):
    original = instance.placeholder
    instance.placeholder = original
    assert instance.placeholder == original

@given(instance=website::DataType_strategy)
def test_website::datatype_interfaceType_type(instance):
    assert isinstance(instance.interfaceType, str)


@given(instance=website::DataType_strategy)
def test_website::datatype_interfaceType_setter(instance):
    original = instance.interfaceType
    instance.interfaceType = original
    assert instance.interfaceType == original

@given(instance=website::DataType_strategy)
def test_website::datatype_ormType_type(instance):
    assert isinstance(instance.ormType, str)


@given(instance=website::DataType_strategy)
def test_website::datatype_ormType_setter(instance):
    original = instance.ormType
    instance.ormType = original
    assert instance.ormType == original

@given(instance=NamedDisplayElement_strategy)
@settings(max_examples=50)
def test_nameddisplayelement_instantiation(instance):
    assert isinstance(instance, NamedDisplayElement)

@given(instance=website::InlineAction_strategy)
@settings(max_examples=50)
def test_website::inlineaction_instantiation(instance):
    assert isinstance(instance, website::InlineAction)

@given(instance=website::InlineAction_strategy)
def test_website::inlineaction_footer_type(instance):
    assert isinstance(instance.footer, str)


@given(instance=website::InlineAction_strategy)
def test_website::inlineaction_footer_setter(instance):
    original = instance.footer
    instance.footer = original
    assert instance.footer == original

@given(instance=website::InlineAction_strategy)
def test_website::inlineaction_headerClass_type(instance):
    assert isinstance(instance.headerClass, str)


@given(instance=website::InlineAction_strategy)
def test_website::inlineaction_headerClass_setter(instance):
    original = instance.headerClass
    instance.headerClass = original
    assert instance.headerClass == original

@given(instance=website::InlineAction_strategy)
def test_website::inlineaction_disable_type(instance):
    assert isinstance(instance.disable, bool)


@given(instance=website::InlineAction_strategy)
def test_website::inlineaction_disable_setter(instance):
    original = instance.disable
    instance.disable = original
    assert instance.disable == original

@given(instance=website::InlineAction_strategy)
def test_website::inlineaction_header_type(instance):
    assert isinstance(instance.header, str)


@given(instance=website::InlineAction_strategy)
def test_website::inlineaction_header_setter(instance):
    original = instance.header
    instance.header = original
    assert instance.header == original

@given(instance=website::InlineAction_strategy)
def test_website::inlineaction_requiresRole_type(instance):
    assert isinstance(instance.requiresRole, str)


@given(instance=website::InlineAction_strategy)
def test_website::inlineaction_requiresRole_setter(instance):
    original = instance.requiresRole
    instance.requiresRole = original
    assert instance.requiresRole == original

@given(instance=website::InlineAction_strategy)
def test_website::inlineaction_footerClass_type(instance):
    assert isinstance(instance.footerClass, str)


@given(instance=website::InlineAction_strategy)
def test_website::inlineaction_footerClass_setter(instance):
    original = instance.footerClass
    instance.footerClass = original
    assert instance.footerClass == original

@given(instance=website::EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_website::enumerationliteral_instantiation(instance):
    assert isinstance(instance, website::EnumerationLiteral)

@given(instance=website::EntityFeature_strategy)
@settings(max_examples=50)
def test_website::entityfeature_instantiation(instance):
    assert isinstance(instance, website::EntityFeature)

@given(instance=website::EntityFeature_strategy)
def test_website::entityfeature_pluralisedName_type(instance):
    assert isinstance(instance.pluralisedName, str)


@given(instance=website::EntityFeature_strategy)
def test_website::entityfeature_pluralisedName_setter(instance):
    original = instance.pluralisedName
    instance.pluralisedName = original
    assert instance.pluralisedName == original

@given(instance=website::EntityFeature_strategy)
def test_website::entityfeature_unique_type(instance):
    assert isinstance(instance.unique, bool)


@given(instance=website::EntityFeature_strategy)
def test_website::entityfeature_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original

@given(instance=website::EntityFeature_strategy)
def test_website::entityfeature_singletonName_type(instance):
    assert isinstance(instance.singletonName, str)


@given(instance=website::EntityFeature_strategy)
def test_website::entityfeature_singletonName_setter(instance):
    original = instance.singletonName
    instance.singletonName = original
    assert instance.singletonName == original

@given(instance=website::EntityFeature_strategy)
def test_website::entityfeature_cardinality_type(instance):
    assert isinstance(instance.cardinality, str)


@given(instance=website::EntityFeature_strategy)
def test_website::entityfeature_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original

@given(instance=website::EntityFeature_strategy)
def test_website::entityfeature_booleanIsHasChoice_type(instance):
    assert isinstance(instance.booleanIsHasChoice, str)


@given(instance=website::EntityFeature_strategy)
def test_website::entityfeature_booleanIsHasChoice_setter(instance):
    original = instance.booleanIsHasChoice
    instance.booleanIsHasChoice = original
    assert instance.booleanIsHasChoice == original

@given(instance=website::EntityFeature_strategy)
def test_website::entityfeature_ordered_type(instance):
    assert isinstance(instance.ordered, bool)


@given(instance=website::EntityFeature_strategy)
def test_website::entityfeature_ordered_setter(instance):
    original = instance.ordered
    instance.ordered = original
    assert instance.ordered == original

@given(instance=website::EntityFeature_strategy)
def test_website::entityfeature_columnName_type(instance):
    assert isinstance(instance.columnName, str)


@given(instance=website::EntityFeature_strategy)
def test_website::entityfeature_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=website::ModelLabel_strategy)
@settings(max_examples=50)
def test_website::modellabel_instantiation(instance):
    assert isinstance(instance, website::ModelLabel)

@given(instance=website::ModelLabel_strategy)
def test_website::modellabel_format_type(instance):
    assert isinstance(instance.format, str)


@given(instance=website::ModelLabel_strategy)
def test_website::modellabel_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original

@given(instance=website::NamedDisplayElement_strategy)
@settings(max_examples=50)
def test_website::nameddisplayelement_instantiation(instance):
    assert isinstance(instance, website::NamedDisplayElement)

@given(instance=website::NamedDisplayElement_strategy)
def test_website::nameddisplayelement_displayLabel_type(instance):
    assert isinstance(instance.displayLabel, str)


@given(instance=website::NamedDisplayElement_strategy)
def test_website::nameddisplayelement_displayLabel_setter(instance):
    original = instance.displayLabel
    instance.displayLabel = original
    assert instance.displayLabel == original

@given(instance=website::Authentication_strategy)
@settings(max_examples=50)
def test_website::authentication_instantiation(instance):
    assert isinstance(instance, website::Authentication)

@given(instance=website::Authentication_strategy)
def test_website::authentication_logoutLabel_type(instance):
    assert isinstance(instance.logoutLabel, str)


@given(instance=website::Authentication_strategy)
def test_website::authentication_logoutLabel_setter(instance):
    original = instance.logoutLabel
    instance.logoutLabel = original
    assert instance.logoutLabel == original

@given(instance=website::Authentication_strategy)
def test_website::authentication_loginLabel_type(instance):
    assert isinstance(instance.loginLabel, str)


@given(instance=website::Authentication_strategy)
def test_website::authentication_loginLabel_setter(instance):
    original = instance.loginLabel
    instance.loginLabel = original
    assert instance.loginLabel == original

@given(instance=website::ImageManipulation_strategy)
@settings(max_examples=50)
def test_website::imagemanipulation_instantiation(instance):
    assert isinstance(instance, website::ImageManipulation)

@given(instance=website::ImageManipulation_strategy)
def test_website::imagemanipulation_jpegQuality_type(instance):
    assert isinstance(instance.jpegQuality, int)


@given(instance=website::ImageManipulation_strategy)
def test_website::imagemanipulation_jpegQuality_setter(instance):
    original = instance.jpegQuality
    instance.jpegQuality = original
    assert instance.jpegQuality == original

@given(instance=website::EntityOrView_strategy)
@settings(max_examples=50)
def test_website::entityorview_instantiation(instance):
    assert isinstance(instance, website::EntityOrView)

@given(instance=website::EntityOrView_strategy)
def test_website::entityorview_implementsUserInterface_type(instance):
    assert isinstance(instance.implementsUserInterface, bool)


@given(instance=website::EntityOrView_strategy)
def test_website::entityorview_implementsUserInterface_setter(instance):
    original = instance.implementsUserInterface
    instance.implementsUserInterface = original
    assert instance.implementsUserInterface == original

@given(instance=website::EntityOrView_strategy)
def test_website::entityorview_autoKeyGenerationStrategy_type(instance):
    assert isinstance(instance.autoKeyGenerationStrategy, str)


@given(instance=website::EntityOrView_strategy)
def test_website::entityorview_autoKeyGenerationStrategy_setter(instance):
    original = instance.autoKeyGenerationStrategy
    instance.autoKeyGenerationStrategy = original
    assert instance.autoKeyGenerationStrategy == original

@given(instance=website::EntityOrView_strategy)
def test_website::entityorview_singletonName_type(instance):
    assert isinstance(instance.singletonName, str)


@given(instance=website::EntityOrView_strategy)
def test_website::entityorview_singletonName_setter(instance):
    original = instance.singletonName
    instance.singletonName = original
    assert instance.singletonName == original

@given(instance=website::EntityOrView_strategy)
def test_website::entityorview_autoKeyName_type(instance):
    assert isinstance(instance.autoKeyName, str)


@given(instance=website::EntityOrView_strategy)
def test_website::entityorview_autoKeyName_setter(instance):
    original = instance.autoKeyName
    instance.autoKeyName = original
    assert instance.autoKeyName == original

@given(instance=website::EntityOrView_strategy)
def test_website::entityorview_serializationExcludeAll_type(instance):
    assert isinstance(instance.serializationExcludeAll, bool)


@given(instance=website::EntityOrView_strategy)
def test_website::entityorview_serializationExcludeAll_setter(instance):
    original = instance.serializationExcludeAll
    instance.serializationExcludeAll = original
    assert instance.serializationExcludeAll == original

@given(instance=website::EntityOrView_strategy)
def test_website::entityorview_autoKeyPersistentType_type(instance):
    assert isinstance(instance.autoKeyPersistentType, str)


@given(instance=website::EntityOrView_strategy)
def test_website::entityorview_autoKeyPersistentType_setter(instance):
    original = instance.autoKeyPersistentType
    instance.autoKeyPersistentType = original
    assert instance.autoKeyPersistentType == original

@given(instance=website::EntityOrView_strategy)
def test_website::entityorview_tableName_type(instance):
    assert isinstance(instance.tableName, str)


@given(instance=website::EntityOrView_strategy)
def test_website::entityorview_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original

@given(instance=website::EntityOrView_strategy)
def test_website::entityorview_pluralisedName_type(instance):
    assert isinstance(instance.pluralisedName, str)


@given(instance=website::EntityOrView_strategy)
def test_website::entityorview_pluralisedName_setter(instance):
    original = instance.pluralisedName
    instance.pluralisedName = original
    assert instance.pluralisedName == original

@given(instance=website::Menu_strategy)
@settings(max_examples=50)
def test_website::menu_instantiation(instance):
    assert isinstance(instance, website::Menu)

@given(instance=website::Menu_strategy)
def test_website::menu_captionClass_type(instance):
    assert isinstance(instance.captionClass, str)


@given(instance=website::Menu_strategy)
def test_website::menu_captionClass_setter(instance):
    original = instance.captionClass
    instance.captionClass = original
    assert instance.captionClass == original

@given(instance=website::Menu_strategy)
def test_website::menu_styleClass_type(instance):
    assert isinstance(instance.styleClass, str)


@given(instance=website::Menu_strategy)
def test_website::menu_styleClass_setter(instance):
    original = instance.styleClass
    instance.styleClass = original
    assert instance.styleClass == original

@given(instance=website::Menu_strategy)
def test_website::menu_omitCaption_type(instance):
    assert isinstance(instance.omitCaption, bool)


@given(instance=website::Menu_strategy)
def test_website::menu_omitCaption_setter(instance):
    original = instance.omitCaption
    instance.omitCaption = original
    assert instance.omitCaption == original

@given(instance=website::Menu_strategy)
def test_website::menu_layoutClass_type(instance):
    assert isinstance(instance.layoutClass, str)


@given(instance=website::Menu_strategy)
def test_website::menu_layoutClass_setter(instance):
    original = instance.layoutClass
    instance.layoutClass = original
    assert instance.layoutClass == original

@given(instance=website::Service_strategy)
@settings(max_examples=50)
def test_website::service_instantiation(instance):
    assert isinstance(instance, website::Service)

@given(instance=website::Classifier_strategy)
@settings(max_examples=50)
def test_website::classifier_instantiation(instance):
    assert isinstance(instance, website::Classifier)

@given(instance=website::WebsiteProperties_strategy)
@settings(max_examples=50)
def test_website::websiteproperties_instantiation(instance):
    assert isinstance(instance, website::WebsiteProperties)

@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_baseURL_type(instance):
    assert isinstance(instance.baseURL, str)


@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_baseURL_setter(instance):
    original = instance.baseURL
    instance.baseURL = original
    assert instance.baseURL == original

@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_topNavigationId_type(instance):
    assert isinstance(instance.topNavigationId, str)


@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_topNavigationId_setter(instance):
    original = instance.topNavigationId
    instance.topNavigationId = original
    assert instance.topNavigationId == original

@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_metaDescription_type(instance):
    assert isinstance(instance.metaDescription, str)


@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_metaDescription_setter(instance):
    original = instance.metaDescription
    instance.metaDescription = original
    assert instance.metaDescription == original

@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_frameworkTechnology_type(instance):
    assert isinstance(instance.frameworkTechnology, str)


@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_frameworkTechnology_setter(instance):
    original = instance.frameworkTechnology
    instance.frameworkTechnology = original
    assert instance.frameworkTechnology == original

@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_webmasterEmail_type(instance):
    assert isinstance(instance.webmasterEmail, str)


@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_webmasterEmail_setter(instance):
    original = instance.webmasterEmail
    instance.webmasterEmail = original
    assert instance.webmasterEmail == original

@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_defaultDateFormat_type(instance):
    assert isinstance(instance.defaultDateFormat, str)


@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_defaultDateFormat_setter(instance):
    original = instance.defaultDateFormat
    instance.defaultDateFormat = original
    assert instance.defaultDateFormat == original

@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_siteTitle_type(instance):
    assert isinstance(instance.siteTitle, str)


@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_siteTitle_setter(instance):
    original = instance.siteTitle
    instance.siteTitle = original
    assert instance.siteTitle == original

@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_rewriteURLs_type(instance):
    assert isinstance(instance.rewriteURLs, bool)


@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_rewriteURLs_setter(instance):
    original = instance.rewriteURLs
    instance.rewriteURLs = original
    assert instance.rewriteURLs == original

@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_defaultTimeFormat_type(instance):
    assert isinstance(instance.defaultTimeFormat, str)


@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_defaultTimeFormat_setter(instance):
    original = instance.defaultTimeFormat
    instance.defaultTimeFormat = original
    assert instance.defaultTimeFormat == original

@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_timestampCreation_type(instance):
    assert isinstance(instance.timestampCreation, bool)


@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_timestampCreation_setter(instance):
    original = instance.timestampCreation
    instance.timestampCreation = original
    assert instance.timestampCreation == original

@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_developmentVersion_type(instance):
    assert isinstance(instance.developmentVersion, bool)


@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_developmentVersion_setter(instance):
    original = instance.developmentVersion
    instance.developmentVersion = original
    assert instance.developmentVersion == original

@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_ormTechnology_type(instance):
    assert isinstance(instance.ormTechnology, str)


@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_ormTechnology_setter(instance):
    original = instance.ormTechnology
    instance.ormTechnology = original
    assert instance.ormTechnology == original

@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_projectName_type(instance):
    assert isinstance(instance.projectName, str)


@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_projectName_setter(instance):
    original = instance.projectName
    instance.projectName = original
    assert instance.projectName == original

@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_inputTechnology_type(instance):
    assert isinstance(instance.inputTechnology, str)


@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_inputTechnology_setter(instance):
    original = instance.inputTechnology
    instance.inputTechnology = original
    assert instance.inputTechnology == original

@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_databaseHost_type(instance):
    assert isinstance(instance.databaseHost, str)


@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_databaseHost_setter(instance):
    original = instance.databaseHost
    instance.databaseHost = original
    assert instance.databaseHost == original

@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_responsiveTopMenu_type(instance):
    assert isinstance(instance.responsiveTopMenu, bool)


@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_responsiveTopMenu_setter(instance):
    original = instance.responsiveTopMenu
    instance.responsiveTopMenu = original
    assert instance.responsiveTopMenu == original

@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_defaultMaximumUploadSize_type(instance):
    assert isinstance(instance.defaultMaximumUploadSize, int)


@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_defaultMaximumUploadSize_setter(instance):
    original = instance.defaultMaximumUploadSize
    instance.defaultMaximumUploadSize = original
    assert instance.defaultMaximumUploadSize == original

@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_databasePrefix_type(instance):
    assert isinstance(instance.databasePrefix, str)


@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_databasePrefix_setter(instance):
    original = instance.databasePrefix
    instance.databasePrefix = original
    assert instance.databasePrefix == original

@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_timestampUpdates_type(instance):
    assert isinstance(instance.timestampUpdates, bool)


@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_timestampUpdates_setter(instance):
    original = instance.timestampUpdates
    instance.timestampUpdates = original
    assert instance.timestampUpdates == original

@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_copyrightText_type(instance):
    assert isinstance(instance.copyrightText, str)


@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_copyrightText_setter(instance):
    original = instance.copyrightText
    instance.copyrightText = original
    assert instance.copyrightText == original

@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_databasePassword_type(instance):
    assert isinstance(instance.databasePassword, str)


@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_databasePassword_setter(instance):
    original = instance.databasePassword
    instance.databasePassword = original
    assert instance.databasePassword == original

@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_siteTemplate_type(instance):
    assert isinstance(instance.siteTemplate, str)


@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_siteTemplate_setter(instance):
    original = instance.siteTemplate
    instance.siteTemplate = original
    assert instance.siteTemplate == original

@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_databaseTechnology_type(instance):
    assert isinstance(instance.databaseTechnology, str)


@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_databaseTechnology_setter(instance):
    original = instance.databaseTechnology
    instance.databaseTechnology = original
    assert instance.databaseTechnology == original

@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_textEditorURL_type(instance):
    assert isinstance(instance.textEditorURL, str)


@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_textEditorURL_setter(instance):
    original = instance.textEditorURL
    instance.textEditorURL = original
    assert instance.textEditorURL == original

@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_defaultDateTimeFormat_type(instance):
    assert isinstance(instance.defaultDateTimeFormat, str)


@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_defaultDateTimeFormat_setter(instance):
    original = instance.defaultDateTimeFormat
    instance.defaultDateTimeFormat = original
    assert instance.defaultDateTimeFormat == original

@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_testProjectName_type(instance):
    assert isinstance(instance.testProjectName, str)


@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_testProjectName_setter(instance):
    original = instance.testProjectName
    instance.testProjectName = original
    assert instance.testProjectName == original

@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_databaseName_type(instance):
    assert isinstance(instance.databaseName, str)


@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_databaseName_setter(instance):
    original = instance.databaseName
    instance.databaseName = original
    assert instance.databaseName == original

@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_captchaSiteKey_type(instance):
    assert isinstance(instance.captchaSiteKey, str)


@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_captchaSiteKey_setter(instance):
    original = instance.captchaSiteKey
    instance.captchaSiteKey = original
    assert instance.captchaSiteKey == original

@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_databasePort_type(instance):
    assert isinstance(instance.databasePort, str)


@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_databasePort_setter(instance):
    original = instance.databasePort
    instance.databasePort = original
    assert instance.databasePort == original

@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_staticUnitsEditable_type(instance):
    assert isinstance(instance.staticUnitsEditable, bool)


@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_staticUnitsEditable_setter(instance):
    original = instance.staticUnitsEditable
    instance.staticUnitsEditable = original
    assert instance.staticUnitsEditable == original

@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_ajaxTechnology_type(instance):
    assert isinstance(instance.ajaxTechnology, str)


@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_ajaxTechnology_setter(instance):
    original = instance.ajaxTechnology
    instance.ajaxTechnology = original
    assert instance.ajaxTechnology == original

@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_captchaSecretKey_type(instance):
    assert isinstance(instance.captchaSecretKey, str)


@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_captchaSecretKey_setter(instance):
    original = instance.captchaSecretKey
    instance.captchaSecretKey = original
    assert instance.captchaSecretKey == original

@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_databaseUsername_type(instance):
    assert isinstance(instance.databaseUsername, str)


@given(instance=website::WebsiteProperties_strategy)
def test_website::websiteproperties_databaseUsername_setter(instance):
    original = instance.databaseUsername
    instance.databaseUsername = original
    assert instance.databaseUsername == original

@given(instance=website::WebGenModel_strategy)
@settings(max_examples=50)
def test_website::webgenmodel_instantiation(instance):
    assert isinstance(instance, website::WebGenModel)

@given(instance=ImageUnit_strategy)
@settings(max_examples=50)
def test_imageunit_instantiation(instance):
    assert isinstance(instance, ImageUnit)

@given(instance=website::SliderUnit_strategy)
@settings(max_examples=50)
def test_website::sliderunit_instantiation(instance):
    assert isinstance(instance, website::SliderUnit)

@given(instance=website::SliderUnit_strategy)
def test_website::sliderunit_styleClass_type(instance):
    assert isinstance(instance.styleClass, str)


@given(instance=website::SliderUnit_strategy)
def test_website::sliderunit_styleClass_setter(instance):
    original = instance.styleClass
    instance.styleClass = original
    assert instance.styleClass == original

@given(instance=website::SliderUnit_strategy)
def test_website::sliderunit_contentClass_type(instance):
    assert isinstance(instance.contentClass, str)


@given(instance=website::SliderUnit_strategy)
def test_website::sliderunit_contentClass_setter(instance):
    original = instance.contentClass
    instance.contentClass = original
    assert instance.contentClass == original

@given(instance=website::GalleryUnit_strategy)
@settings(max_examples=50)
def test_website::galleryunit_instantiation(instance):
    assert isinstance(instance, website::GalleryUnit)

@given(instance=website::GalleryUnit_strategy)
def test_website::galleryunit_contentClass_type(instance):
    assert isinstance(instance.contentClass, str)


@given(instance=website::GalleryUnit_strategy)
def test_website::galleryunit_contentClass_setter(instance):
    original = instance.contentClass
    instance.contentClass = original
    assert instance.contentClass == original

@given(instance=website::GalleryUnit_strategy)
def test_website::galleryunit_styleClass_type(instance):
    assert isinstance(instance.styleClass, str)


@given(instance=website::GalleryUnit_strategy)
def test_website::galleryunit_styleClass_setter(instance):
    original = instance.styleClass
    instance.styleClass = original
    assert instance.styleClass == original

@given(instance=InlineAction_strategy)
@settings(max_examples=50)
def test_inlineaction_instantiation(instance):
    assert isinstance(instance, InlineAction)

@given(instance=website::FeatureSupportAction_strategy)
@settings(max_examples=50)
def test_website::featuresupportaction_instantiation(instance):
    assert isinstance(instance, website::FeatureSupportAction)

@given(instance=website::FeatureSupportAction_strategy)
def test_website::featuresupportaction_confirmMessage_type(instance):
    assert isinstance(instance.confirmMessage, str)


@given(instance=website::FeatureSupportAction_strategy)
def test_website::featuresupportaction_confirmMessage_setter(instance):
    original = instance.confirmMessage
    instance.confirmMessage = original
    assert instance.confirmMessage == original

@given(instance=website::FeatureSupportAction_strategy)
def test_website::featuresupportaction_fileExtension_type(instance):
    assert isinstance(instance.fileExtension, str)


@given(instance=website::FeatureSupportAction_strategy)
def test_website::featuresupportaction_fileExtension_setter(instance):
    original = instance.fileExtension
    instance.fileExtension = original
    assert instance.fileExtension == original

@given(instance=website::FeatureSupportAction_strategy)
def test_website::featuresupportaction_uriElement_type(instance):
    assert isinstance(instance.uriElement, str)


@given(instance=website::FeatureSupportAction_strategy)
def test_website::featuresupportaction_uriElement_setter(instance):
    original = instance.uriElement
    instance.uriElement = original
    assert instance.uriElement == original

@given(instance=website::DeleteAction_strategy)
@settings(max_examples=50)
def test_website::deleteaction_instantiation(instance):
    assert isinstance(instance, website::DeleteAction)

@given(instance=website::DeleteAction_strategy)
def test_website::deleteaction_confirmMessage_type(instance):
    assert isinstance(instance.confirmMessage, str)


@given(instance=website::DeleteAction_strategy)
def test_website::deleteaction_confirmMessage_setter(instance):
    original = instance.confirmMessage
    instance.confirmMessage = original
    assert instance.confirmMessage == original

@given(instance=website::DeleteAction_strategy)
def test_website::deleteaction_uriElement_type(instance):
    assert isinstance(instance.uriElement, str)


@given(instance=website::DeleteAction_strategy)
def test_website::deleteaction_uriElement_setter(instance):
    original = instance.uriElement
    instance.uriElement = original
    assert instance.uriElement == original

@given(instance=website::SelectAction_strategy)
@settings(max_examples=50)
def test_website::selectaction_instantiation(instance):
    assert isinstance(instance, website::SelectAction)

@given(instance=ChildPath_strategy)
@settings(max_examples=50)
def test_childpath_instantiation(instance):
    assert isinstance(instance, ChildPath)

@given(instance=website::ChildPathAttribute_strategy)
@settings(max_examples=50)
def test_website::childpathattribute_instantiation(instance):
    assert isinstance(instance, website::ChildPathAttribute)

@given(instance=website::ChildPathAttribute_strategy)
def test_website::childpathattribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=website::ChildPathAttribute_strategy)
def test_website::childpathattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=FeaturePath_strategy)
@settings(max_examples=50)
def test_featurepath_instantiation(instance):
    assert isinstance(instance, FeaturePath)

@given(instance=website::FeaturePathAttribute_strategy)
@settings(max_examples=50)
def test_website::featurepathattribute_instantiation(instance):
    assert isinstance(instance, website::FeaturePathAttribute)

@given(instance=website::FeaturePathAttribute_strategy)
def test_website::featurepathattribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=website::FeaturePathAttribute_strategy)
def test_website::featurepathattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=website::FeaturePath_strategy)
@settings(max_examples=50)
def test_website::featurepath_instantiation(instance):
    assert isinstance(instance, website::FeaturePath)

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

@given(instance=website::LoginUnit_strategy)
@settings(max_examples=50)
def test_website::loginunit_instantiation(instance):
    assert isinstance(instance, website::LoginUnit)

@given(instance=website::LoginUnit_strategy)
def test_website::loginunit_styleClass_type(instance):
    assert isinstance(instance.styleClass, str)


@given(instance=website::LoginUnit_strategy)
def test_website::loginunit_styleClass_setter(instance):
    original = instance.styleClass
    instance.styleClass = original
    assert instance.styleClass == original

@given(instance=website::LoginUnit_strategy)
def test_website::loginunit_logoutUriElement_type(instance):
    assert isinstance(instance.logoutUriElement, str)


@given(instance=website::LoginUnit_strategy)
def test_website::loginunit_logoutUriElement_setter(instance):
    original = instance.logoutUriElement
    instance.logoutUriElement = original
    assert instance.logoutUriElement == original

@given(instance=website::RegistrationUnit_strategy)
@settings(max_examples=50)
def test_website::registrationunit_instantiation(instance):
    assert isinstance(instance, website::RegistrationUnit)

@given(instance=website::RegistrationUnit_strategy)
def test_website::registrationunit_styleClass_type(instance):
    assert isinstance(instance.styleClass, str)


@given(instance=website::RegistrationUnit_strategy)
def test_website::registrationunit_styleClass_setter(instance):
    original = instance.styleClass
    instance.styleClass = original
    assert instance.styleClass == original

@given(instance=website::ForgottenPasswordUnit_strategy)
@settings(max_examples=50)
def test_website::forgottenpasswordunit_instantiation(instance):
    assert isinstance(instance, website::ForgottenPasswordUnit)

@given(instance=website::ForgottenPasswordUnit_strategy)
def test_website::forgottenpasswordunit_styleClass_type(instance):
    assert isinstance(instance.styleClass, str)


@given(instance=website::ForgottenPasswordUnit_strategy)
def test_website::forgottenpasswordunit_styleClass_setter(instance):
    original = instance.styleClass
    instance.styleClass = original
    assert instance.styleClass == original

@given(instance=website::SearchUnit_strategy)
@settings(max_examples=50)
def test_website::searchunit_instantiation(instance):
    assert isinstance(instance, website::SearchUnit)

@given(instance=website::SearchUnit_strategy)
def test_website::searchunit_styleClass_type(instance):
    assert isinstance(instance.styleClass, str)


@given(instance=website::SearchUnit_strategy)
def test_website::searchunit_styleClass_setter(instance):
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

@given(instance=website::ImageUnit_strategy)
@settings(max_examples=50)
def test_website::imageunit_instantiation(instance):
    assert isinstance(instance, website::ImageUnit)

@given(instance=website::ImageUnit_strategy)
def test_website::imageunit_transitionTime_type(instance):
    assert isinstance(instance.transitionTime, int)


@given(instance=website::ImageUnit_strategy)
def test_website::imageunit_transitionTime_setter(instance):
    original = instance.transitionTime
    instance.transitionTime = original
    assert instance.transitionTime == original

@given(instance=website::ImageUnit_strategy)
def test_website::imageunit_missingImagePath_type(instance):
    assert isinstance(instance.missingImagePath, str)


@given(instance=website::ImageUnit_strategy)
def test_website::imageunit_missingImagePath_setter(instance):
    original = instance.missingImagePath
    instance.missingImagePath = original
    assert instance.missingImagePath == original

@given(instance=website::ImageUnit_strategy)
def test_website::imageunit_showTime_type(instance):
    assert isinstance(instance.showTime, int)


@given(instance=website::ImageUnit_strategy)
def test_website::imageunit_showTime_setter(instance):
    original = instance.showTime
    instance.showTime = original
    assert instance.showTime == original

@given(instance=website::DataUnit_strategy)
@settings(max_examples=50)
def test_website::dataunit_instantiation(instance):
    assert isinstance(instance, website::DataUnit)

@given(instance=website::ControlUnit_strategy)
@settings(max_examples=50)
def test_website::controlunit_instantiation(instance):
    assert isinstance(instance, website::ControlUnit)

@given(instance=website::ControlUnit_strategy)
def test_website::controlunit_submitLabel_type(instance):
    assert isinstance(instance.submitLabel, str)


@given(instance=website::ControlUnit_strategy)
def test_website::controlunit_submitLabel_setter(instance):
    original = instance.submitLabel
    instance.submitLabel = original
    assert instance.submitLabel == original

@given(instance=website::ControlUnit_strategy)
def test_website::controlunit_cancelLabel_type(instance):
    assert isinstance(instance.cancelLabel, str)


@given(instance=website::ControlUnit_strategy)
def test_website::controlunit_cancelLabel_setter(instance):
    original = instance.cancelLabel
    instance.cancelLabel = original
    assert instance.cancelLabel == original

@given(instance=website::ControlUnit_strategy)
def test_website::controlunit_contentClass_type(instance):
    assert isinstance(instance.contentClass, str)


@given(instance=website::ControlUnit_strategy)
def test_website::controlunit_contentClass_setter(instance):
    original = instance.contentClass
    instance.contentClass = original
    assert instance.contentClass == original

@given(instance=website::EditUnit_strategy)
@settings(max_examples=50)
def test_website::editunit_instantiation(instance):
    assert isinstance(instance, website::EditUnit)

@given(instance=website::EditUnit_strategy)
def test_website::editunit_cancelLabel_type(instance):
    assert isinstance(instance.cancelLabel, str)


@given(instance=website::EditUnit_strategy)
def test_website::editunit_cancelLabel_setter(instance):
    original = instance.cancelLabel
    instance.cancelLabel = original
    assert instance.cancelLabel == original

@given(instance=website::EditUnit_strategy)
def test_website::editunit_confirmLabel_type(instance):
    assert isinstance(instance.confirmLabel, str)


@given(instance=website::EditUnit_strategy)
def test_website::editunit_confirmLabel_setter(instance):
    original = instance.confirmLabel
    instance.confirmLabel = original
    assert instance.confirmLabel == original

@given(instance=website::EditUnit_strategy)
def test_website::editunit_contentClass_type(instance):
    assert isinstance(instance.contentClass, str)


@given(instance=website::EditUnit_strategy)
def test_website::editunit_contentClass_setter(instance):
    original = instance.contentClass
    instance.contentClass = original
    assert instance.contentClass == original

@given(instance=website::EditUnit_strategy)
def test_website::editunit_customiseValues_type(instance):
    assert isinstance(instance.customiseValues, bool)


@given(instance=website::EditUnit_strategy)
def test_website::editunit_customiseValues_setter(instance):
    original = instance.customiseValues
    instance.customiseValues = original
    assert instance.customiseValues == original

@given(instance=EditUnit_strategy)
@settings(max_examples=50)
def test_editunit_instantiation(instance):
    assert isinstance(instance, EditUnit)

@given(instance=website::CreateUnit_strategy)
@settings(max_examples=50)
def test_website::createunit_instantiation(instance):
    assert isinstance(instance, website::CreateUnit)

@given(instance=website::CreateUnit_strategy)
def test_website::createunit_styleClass_type(instance):
    assert isinstance(instance.styleClass, str)


@given(instance=website::CreateUnit_strategy)
def test_website::createunit_styleClass_setter(instance):
    original = instance.styleClass
    instance.styleClass = original
    assert instance.styleClass == original

@given(instance=InterfaceField_strategy)
@settings(max_examples=50)
def test_interfacefield_instantiation(instance):
    assert isinstance(instance, InterfaceField)

@given(instance=website::DateField_strategy)
@settings(max_examples=50)
def test_website::datefield_instantiation(instance):
    assert isinstance(instance, website::DateField)

@given(instance=website::DateField_strategy)
def test_website::datefield_details_type(instance):
    assert isinstance(instance.details, str)


@given(instance=website::DateField_strategy)
def test_website::datefield_details_setter(instance):
    original = instance.details
    instance.details = original
    assert instance.details == original

@given(instance=website::DateField_strategy)
def test_website::datefield_format_type(instance):
    assert isinstance(instance.format, str)


@given(instance=website::DateField_strategy)
def test_website::datefield_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original

@given(instance=website::DataTypeField_strategy)
@settings(max_examples=50)
def test_website::datatypefield_instantiation(instance):
    assert isinstance(instance, website::DataTypeField)

@given(instance=website::DataTypeField_strategy)
def test_website::datatypefield_obfuscateFormFields_type(instance):
    assert isinstance(instance.obfuscateFormFields, bool)


@given(instance=website::DataTypeField_strategy)
def test_website::datatypefield_obfuscateFormFields_setter(instance):
    original = instance.obfuscateFormFields
    instance.obfuscateFormFields = original
    assert instance.obfuscateFormFields == original

@given(instance=website::DataTypeField_strategy)
def test_website::datatypefield_encrypt_type(instance):
    assert isinstance(instance.encrypt, bool)


@given(instance=website::DataTypeField_strategy)
def test_website::datatypefield_encrypt_setter(instance):
    original = instance.encrypt
    instance.encrypt = original
    assert instance.encrypt == original

@given(instance=website::DataTypeField_strategy)
def test_website::datatypefield_interfaceType_type(instance):
    assert isinstance(instance.interfaceType, str)


@given(instance=website::DataTypeField_strategy)
def test_website::datatypefield_interfaceType_setter(instance):
    original = instance.interfaceType
    instance.interfaceType = original
    assert instance.interfaceType == original

@given(instance=website::ChildPath_strategy)
@settings(max_examples=50)
def test_website::childpath_instantiation(instance):
    assert isinstance(instance, website::ChildPath)

@given(instance=website::AssociationReference_strategy)
@settings(max_examples=50)
def test_website::associationreference_instantiation(instance):
    assert isinstance(instance, website::AssociationReference)

@given(instance=website::AssociationReference_strategy)
def test_website::associationreference_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=website::AssociationReference_strategy)
def test_website::associationreference_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SelectableUnit_strategy)
@settings(max_examples=50)
def test_selectableunit_instantiation(instance):
    assert isinstance(instance, SelectableUnit)

@given(instance=website::CreateUpdateUnit_strategy)
@settings(max_examples=50)
def test_website::createupdateunit_instantiation(instance):
    assert isinstance(instance, website::CreateUpdateUnit)

@given(instance=website::CreateUpdateUnit_strategy)
def test_website::createupdateunit_createUriElement_type(instance):
    assert isinstance(instance.createUriElement, str)


@given(instance=website::CreateUpdateUnit_strategy)
def test_website::createupdateunit_createUriElement_setter(instance):
    original = instance.createUriElement
    instance.createUriElement = original
    assert instance.createUriElement == original

@given(instance=website::CreateUpdateUnit_strategy)
def test_website::createupdateunit_clearLabel_type(instance):
    assert isinstance(instance.clearLabel, str)


@given(instance=website::CreateUpdateUnit_strategy)
def test_website::createupdateunit_clearLabel_setter(instance):
    original = instance.clearLabel
    instance.clearLabel = original
    assert instance.clearLabel == original

@given(instance=website::CreateUpdateUnit_strategy)
def test_website::createupdateunit_styleClass_type(instance):
    assert isinstance(instance.styleClass, str)


@given(instance=website::CreateUpdateUnit_strategy)
def test_website::createupdateunit_styleClass_setter(instance):
    original = instance.styleClass
    instance.styleClass = original
    assert instance.styleClass == original

@given(instance=website::MapUnit_strategy)
@settings(max_examples=50)
def test_website::mapunit_instantiation(instance):
    assert isinstance(instance, website::MapUnit)

@given(instance=website::MapUnit_strategy)
def test_website::mapunit_defaultZoomLevel_type(instance):
    assert isinstance(instance.defaultZoomLevel, int)


@given(instance=website::MapUnit_strategy)
def test_website::mapunit_defaultZoomLevel_setter(instance):
    original = instance.defaultZoomLevel
    instance.defaultZoomLevel = original
    assert instance.defaultZoomLevel == original

@given(instance=website::MapUnit_strategy)
def test_website::mapunit_styleClass_type(instance):
    assert isinstance(instance.styleClass, str)


@given(instance=website::MapUnit_strategy)
def test_website::mapunit_styleClass_setter(instance):
    original = instance.styleClass
    instance.styleClass = original
    assert instance.styleClass == original

@given(instance=website::MapUnit_strategy)
def test_website::mapunit_readOnly_type(instance):
    assert isinstance(instance.readOnly, bool)


@given(instance=website::MapUnit_strategy)
def test_website::mapunit_readOnly_setter(instance):
    original = instance.readOnly
    instance.readOnly = original
    assert instance.readOnly == original

@given(instance=website::UpdateUnit_strategy)
@settings(max_examples=50)
def test_website::updateunit_instantiation(instance):
    assert isinstance(instance, website::UpdateUnit)

@given(instance=website::UpdateUnit_strategy)
def test_website::updateunit_styleClass_type(instance):
    assert isinstance(instance.styleClass, str)


@given(instance=website::UpdateUnit_strategy)
def test_website::updateunit_styleClass_setter(instance):
    original = instance.styleClass
    instance.styleClass = original
    assert instance.styleClass == original

@given(instance=website::DetailsUnit_strategy)
@settings(max_examples=50)
def test_website::detailsunit_instantiation(instance):
    assert isinstance(instance, website::DetailsUnit)

@given(instance=website::DetailsUnit_strategy)
def test_website::detailsunit_onlyDisplayWhenNotEmpty_type(instance):
    assert isinstance(instance.onlyDisplayWhenNotEmpty, bool)


@given(instance=website::DetailsUnit_strategy)
def test_website::detailsunit_onlyDisplayWhenNotEmpty_setter(instance):
    original = instance.onlyDisplayWhenNotEmpty
    instance.onlyDisplayWhenNotEmpty = original
    assert instance.onlyDisplayWhenNotEmpty == original

@given(instance=website::DetailsUnit_strategy)
def test_website::detailsunit_omitFieldLabels_type(instance):
    assert isinstance(instance.omitFieldLabels, bool)


@given(instance=website::DetailsUnit_strategy)
def test_website::detailsunit_omitFieldLabels_setter(instance):
    original = instance.omitFieldLabels
    instance.omitFieldLabels = original
    assert instance.omitFieldLabels == original

@given(instance=website::DetailsUnit_strategy)
def test_website::detailsunit_contentClass_type(instance):
    assert isinstance(instance.contentClass, str)


@given(instance=website::DetailsUnit_strategy)
def test_website::detailsunit_contentClass_setter(instance):
    original = instance.contentClass
    instance.contentClass = original
    assert instance.contentClass == original

@given(instance=website::DetailsUnit_strategy)
def test_website::detailsunit_styleClass_type(instance):
    assert isinstance(instance.styleClass, str)


@given(instance=website::DetailsUnit_strategy)
def test_website::detailsunit_styleClass_setter(instance):
    original = instance.styleClass
    instance.styleClass = original
    assert instance.styleClass == original

@given(instance=website::CollectionUnit_strategy)
@settings(max_examples=50)
def test_website::collectionunit_instantiation(instance):
    assert isinstance(instance, website::CollectionUnit)

@given(instance=website::CollectionUnit_strategy)
def test_website::collectionunit_nextNpages_type(instance):
    assert isinstance(instance.nextNpages, int)


@given(instance=website::CollectionUnit_strategy)
def test_website::collectionunit_nextNpages_setter(instance):
    original = instance.nextNpages
    instance.nextNpages = original
    assert instance.nextNpages == original

@given(instance=website::CollectionUnit_strategy)
def test_website::collectionunit_firstPageLabel_type(instance):
    assert isinstance(instance.firstPageLabel, str)


@given(instance=website::CollectionUnit_strategy)
def test_website::collectionunit_firstPageLabel_setter(instance):
    original = instance.firstPageLabel
    instance.firstPageLabel = original
    assert instance.firstPageLabel == original

@given(instance=website::CollectionUnit_strategy)
def test_website::collectionunit_useDisabledPageLinks_type(instance):
    assert isinstance(instance.useDisabledPageLinks, bool)


@given(instance=website::CollectionUnit_strategy)
def test_website::collectionunit_useDisabledPageLinks_setter(instance):
    original = instance.useDisabledPageLinks
    instance.useDisabledPageLinks = original
    assert instance.useDisabledPageLinks == original

@given(instance=website::CollectionUnit_strategy)
def test_website::collectionunit_defaultPaginationSize_type(instance):
    assert isinstance(instance.defaultPaginationSize, int)


@given(instance=website::CollectionUnit_strategy)
def test_website::collectionunit_defaultPaginationSize_setter(instance):
    original = instance.defaultPaginationSize
    instance.defaultPaginationSize = original
    assert instance.defaultPaginationSize == original

@given(instance=website::CollectionUnit_strategy)
def test_website::collectionunit_previousNpages_type(instance):
    assert isinstance(instance.previousNpages, int)


@given(instance=website::CollectionUnit_strategy)
def test_website::collectionunit_previousNpages_setter(instance):
    original = instance.previousNpages
    instance.previousNpages = original
    assert instance.previousNpages == original

@given(instance=website::CollectionUnit_strategy)
def test_website::collectionunit_lastPageLabel_type(instance):
    assert isinstance(instance.lastPageLabel, str)


@given(instance=website::CollectionUnit_strategy)
def test_website::collectionunit_lastPageLabel_setter(instance):
    original = instance.lastPageLabel
    instance.lastPageLabel = original
    assert instance.lastPageLabel == original

@given(instance=website::CollectionUnit_strategy)
def test_website::collectionunit_previousPageLabel_type(instance):
    assert isinstance(instance.previousPageLabel, str)


@given(instance=website::CollectionUnit_strategy)
def test_website::collectionunit_previousPageLabel_setter(instance):
    original = instance.previousPageLabel
    instance.previousPageLabel = original
    assert instance.previousPageLabel == original

@given(instance=website::CollectionUnit_strategy)
def test_website::collectionunit_nextPageLabel_type(instance):
    assert isinstance(instance.nextPageLabel, str)


@given(instance=website::CollectionUnit_strategy)
def test_website::collectionunit_nextPageLabel_setter(instance):
    original = instance.nextPageLabel
    instance.nextPageLabel = original
    assert instance.nextPageLabel == original

@given(instance=website::CollectionUnit_strategy)
def test_website::collectionunit_useFirstLastPageLinks_type(instance):
    assert isinstance(instance.useFirstLastPageLinks, bool)


@given(instance=website::CollectionUnit_strategy)
def test_website::collectionunit_useFirstLastPageLinks_setter(instance):
    original = instance.useFirstLastPageLinks
    instance.useFirstLastPageLinks = original
    assert instance.useFirstLastPageLinks == original

@given(instance=website::CollectionUnit_strategy)
def test_website::collectionunit_emptyMessage_type(instance):
    assert isinstance(instance.emptyMessage, str)


@given(instance=website::CollectionUnit_strategy)
def test_website::collectionunit_emptyMessage_setter(instance):
    original = instance.emptyMessage
    instance.emptyMessage = original
    assert instance.emptyMessage == original

@given(instance=website::SingletonUnit_strategy)
@settings(max_examples=50)
def test_website::singletonunit_instantiation(instance):
    assert isinstance(instance, website::SingletonUnit)

@given(instance=website::SelectableUnit_strategy)
@settings(max_examples=50)
def test_website::selectableunit_instantiation(instance):
    assert isinstance(instance, website::SelectableUnit)

@given(instance=website::CaptchaField_strategy)
@settings(max_examples=50)
def test_website::captchafield_instantiation(instance):
    assert isinstance(instance, website::CaptchaField)

@given(instance=UnitFeature_strategy)
@settings(max_examples=50)
def test_unitfeature_instantiation(instance):
    assert isinstance(instance, UnitFeature)

@given(instance=website::UnitElement_strategy)
@settings(max_examples=50)
def test_website::unitelement_instantiation(instance):
    assert isinstance(instance, website::UnitElement)

@given(instance=website::UnitElement_strategy)
def test_website::unitelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=website::UnitElement_strategy)
def test_website::unitelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=website::UnitElement_strategy)
def test_website::unitelement_validationPattern_type(instance):
    assert isinstance(instance.validationPattern, str)


@given(instance=website::UnitElement_strategy)
def test_website::unitelement_validationPattern_setter(instance):
    original = instance.validationPattern
    instance.validationPattern = original
    assert instance.validationPattern == original

@given(instance=website::UnitElement_strategy)
def test_website::unitelement_obfuscateFormFields_type(instance):
    assert isinstance(instance.obfuscateFormFields, bool)


@given(instance=website::UnitElement_strategy)
def test_website::unitelement_obfuscateFormFields_setter(instance):
    original = instance.obfuscateFormFields
    instance.obfuscateFormFields = original
    assert instance.obfuscateFormFields == original

@given(instance=website::UnitElement_strategy)
def test_website::unitelement_placeholder_type(instance):
    assert isinstance(instance.placeholder, str)


@given(instance=website::UnitElement_strategy)
def test_website::unitelement_placeholder_setter(instance):
    original = instance.placeholder
    instance.placeholder = original
    assert instance.placeholder == original

@given(instance=InlineActionContainer_strategy)
@settings(max_examples=50)
def test_inlineactioncontainer_instantiation(instance):
    assert isinstance(instance, InlineActionContainer)

@given(instance=website::ImageIndexUnit_strategy)
@settings(max_examples=50)
def test_website::imageindexunit_instantiation(instance):
    assert isinstance(instance, website::ImageIndexUnit)

@given(instance=website::ImageIndexUnit_strategy)
def test_website::imageindexunit_contentClass_type(instance):
    assert isinstance(instance.contentClass, str)


@given(instance=website::ImageIndexUnit_strategy)
def test_website::imageindexunit_contentClass_setter(instance):
    original = instance.contentClass
    instance.contentClass = original
    assert instance.contentClass == original

@given(instance=website::ImageIndexUnit_strategy)
def test_website::imageindexunit_styleClass_type(instance):
    assert isinstance(instance.styleClass, str)


@given(instance=website::ImageIndexUnit_strategy)
def test_website::imageindexunit_styleClass_setter(instance):
    original = instance.styleClass
    instance.styleClass = original
    assert instance.styleClass == original

@given(instance=website::IndexUnit_strategy)
@settings(max_examples=50)
def test_website::indexunit_instantiation(instance):
    assert isinstance(instance, website::IndexUnit)

@given(instance=website::IndexUnit_strategy)
def test_website::indexunit_styleClass_type(instance):
    assert isinstance(instance.styleClass, str)


@given(instance=website::IndexUnit_strategy)
def test_website::indexunit_styleClass_setter(instance):
    original = instance.styleClass
    instance.styleClass = original
    assert instance.styleClass == original

@given(instance=website::IndexUnit_strategy)
def test_website::indexunit_contentClass_type(instance):
    assert isinstance(instance.contentClass, str)


@given(instance=website::IndexUnit_strategy)
def test_website::indexunit_contentClass_setter(instance):
    original = instance.contentClass
    instance.contentClass = original
    assert instance.contentClass == original

@given(instance=website::IndexUnit_strategy)
def test_website::indexunit_displayOption_type(instance):
    assert isinstance(instance.displayOption, str)


@given(instance=website::IndexUnit_strategy)
def test_website::indexunit_displayOption_setter(instance):
    original = instance.displayOption
    instance.displayOption = original
    assert instance.displayOption == original

@given(instance=website::IndexUnit_strategy)
def test_website::indexunit_omitColumnLabels_type(instance):
    assert isinstance(instance.omitColumnLabels, bool)


@given(instance=website::IndexUnit_strategy)
def test_website::indexunit_omitColumnLabels_setter(instance):
    original = instance.omitColumnLabels
    instance.omitColumnLabels = original
    assert instance.omitColumnLabels == original

@given(instance=website::IndexUnit_strategy)
def test_website::indexunit_rowClasses_type(instance):
    assert isinstance(instance.rowClasses, str)


@given(instance=website::IndexUnit_strategy)
def test_website::indexunit_rowClasses_setter(instance):
    original = instance.rowClasses
    instance.rowClasses = original
    assert instance.rowClasses == original

@given(instance=UnitField_strategy)
@settings(max_examples=50)
def test_unitfield_instantiation(instance):
    assert isinstance(instance, UnitField)

@given(instance=website::InterfaceField_strategy)
@settings(max_examples=50)
def test_website::interfacefield_instantiation(instance):
    assert isinstance(instance, website::InterfaceField)

@given(instance=website::InterfaceField_strategy)
def test_website::interfacefield_inputClass_type(instance):
    assert isinstance(instance.inputClass, str)


@given(instance=website::InterfaceField_strategy)
def test_website::interfacefield_inputClass_setter(instance):
    original = instance.inputClass
    instance.inputClass = original
    assert instance.inputClass == original

@given(instance=website::InterfaceField_strategy)
def test_website::interfacefield_required_type(instance):
    assert isinstance(instance.required, bool)


@given(instance=website::InterfaceField_strategy)
def test_website::interfacefield_required_setter(instance):
    original = instance.required
    instance.required = original
    assert instance.required == original

@given(instance=website::InterfaceField_strategy)
def test_website::interfacefield_defaultValue_type(instance):
    assert isinstance(instance.defaultValue, str)


@given(instance=website::InterfaceField_strategy)
def test_website::interfacefield_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original

@given(instance=website::InterfaceField_strategy)
def test_website::interfacefield_placeholder_type(instance):
    assert isinstance(instance.placeholder, str)


@given(instance=website::InterfaceField_strategy)
def test_website::interfacefield_placeholder_setter(instance):
    original = instance.placeholder
    instance.placeholder = original
    assert instance.placeholder == original

@given(instance=website::InterfaceField_strategy)
def test_website::interfacefield_validationPattern_type(instance):
    assert isinstance(instance.validationPattern, str)


@given(instance=website::InterfaceField_strategy)
def test_website::interfacefield_validationPattern_setter(instance):
    original = instance.validationPattern
    instance.validationPattern = original
    assert instance.validationPattern == original

@given(instance=website::UnitFeature_strategy)
@settings(max_examples=50)
def test_website::unitfeature_instantiation(instance):
    assert isinstance(instance, website::UnitFeature)

@given(instance=website::UnitFeature_strategy)
def test_website::unitfeature_footerClass_type(instance):
    assert isinstance(instance.footerClass, str)


@given(instance=website::UnitFeature_strategy)
def test_website::unitfeature_footerClass_setter(instance):
    original = instance.footerClass
    instance.footerClass = original
    assert instance.footerClass == original

@given(instance=website::UnitFeature_strategy)
def test_website::unitfeature_inputClass_type(instance):
    assert isinstance(instance.inputClass, str)


@given(instance=website::UnitFeature_strategy)
def test_website::unitfeature_inputClass_setter(instance):
    original = instance.inputClass
    instance.inputClass = original
    assert instance.inputClass == original

@given(instance=website::UnitFeature_strategy)
def test_website::unitfeature_displayLabel_type(instance):
    assert isinstance(instance.displayLabel, str)


@given(instance=website::UnitFeature_strategy)
def test_website::unitfeature_displayLabel_setter(instance):
    original = instance.displayLabel
    instance.displayLabel = original
    assert instance.displayLabel == original

@given(instance=website::UnitFeature_strategy)
def test_website::unitfeature_required_type(instance):
    assert isinstance(instance.required, bool)


@given(instance=website::UnitFeature_strategy)
def test_website::unitfeature_required_setter(instance):
    original = instance.required
    instance.required = original
    assert instance.required == original

@given(instance=website::UnitFeature_strategy)
def test_website::unitfeature_autofocus_type(instance):
    assert isinstance(instance.autofocus, bool)


@given(instance=website::UnitFeature_strategy)
def test_website::unitfeature_autofocus_setter(instance):
    original = instance.autofocus
    instance.autofocus = original
    assert instance.autofocus == original

@given(instance=website::UnitFeature_strategy)
def test_website::unitfeature_headerClass_type(instance):
    assert isinstance(instance.headerClass, str)


@given(instance=website::UnitFeature_strategy)
def test_website::unitfeature_headerClass_setter(instance):
    original = instance.headerClass
    instance.headerClass = original
    assert instance.headerClass == original

@given(instance=website::UnitFeature_strategy)
def test_website::unitfeature_displayClass_type(instance):
    assert isinstance(instance.displayClass, str)


@given(instance=website::UnitFeature_strategy)
def test_website::unitfeature_displayClass_setter(instance):
    original = instance.displayClass
    instance.displayClass = original
    assert instance.displayClass == original

@given(instance=website::UnitFeature_strategy)
def test_website::unitfeature_onlyDisplayWhenNotEmpty_type(instance):
    assert isinstance(instance.onlyDisplayWhenNotEmpty, bool)


@given(instance=website::UnitFeature_strategy)
def test_website::unitfeature_onlyDisplayWhenNotEmpty_setter(instance):
    original = instance.onlyDisplayWhenNotEmpty
    instance.onlyDisplayWhenNotEmpty = original
    assert instance.onlyDisplayWhenNotEmpty == original

@given(instance=website::UnitFeature_strategy)
def test_website::unitfeature_nullDisplayValue_type(instance):
    assert isinstance(instance.nullDisplayValue, str)


@given(instance=website::UnitFeature_strategy)
def test_website::unitfeature_nullDisplayValue_setter(instance):
    original = instance.nullDisplayValue
    instance.nullDisplayValue = original
    assert instance.nullDisplayValue == original

@given(instance=website::UnitFeature_strategy)
def test_website::unitfeature_footer_type(instance):
    assert isinstance(instance.footer, str)


@given(instance=website::UnitFeature_strategy)
def test_website::unitfeature_footer_setter(instance):
    original = instance.footer
    instance.footer = original
    assert instance.footer == original

@given(instance=AssociationReference_strategy)
@settings(max_examples=50)
def test_associationreference_instantiation(instance):
    assert isinstance(instance, AssociationReference)

@given(instance=website::ChildPathAssociation_strategy)
@settings(max_examples=50)
def test_website::childpathassociation_instantiation(instance):
    assert isinstance(instance, website::ChildPathAssociation)

@given(instance=website::ChildPathAssociation_strategy)
def test_website::childpathassociation_isSourceAssociation_type(instance):
    assert isinstance(instance.isSourceAssociation, bool)


@given(instance=website::ChildPathAssociation_strategy)
def test_website::childpathassociation_isSourceAssociation_setter(instance):
    original = instance.isSourceAssociation
    instance.isSourceAssociation = original
    assert instance.isSourceAssociation == original

@given(instance=website::FeaturePathAssociation_strategy)
@settings(max_examples=50)
def test_website::featurepathassociation_instantiation(instance):
    assert isinstance(instance, website::FeaturePathAssociation)

@given(instance=website::FeaturePathAssociation_strategy)
def test_website::featurepathassociation_isSourceAssociation_type(instance):
    assert isinstance(instance.isSourceAssociation, bool)


@given(instance=website::FeaturePathAssociation_strategy)
def test_website::featurepathassociation_isSourceAssociation_setter(instance):
    original = instance.isSourceAssociation
    instance.isSourceAssociation = original
    assert instance.isSourceAssociation == original

@given(instance=ContentUnit_strategy)
@settings(max_examples=50)
def test_contentunit_instantiation(instance):
    assert isinstance(instance, ContentUnit)

@given(instance=website::CreateSitemapUnit_strategy)
@settings(max_examples=50)
def test_website::createsitemapunit_instantiation(instance):
    assert isinstance(instance, website::CreateSitemapUnit)

@given(instance=website::CreateSitemapUnit_strategy)
def test_website::createsitemapunit_filename_type(instance):
    assert isinstance(instance.filename, str)


@given(instance=website::CreateSitemapUnit_strategy)
def test_website::createsitemapunit_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original

@given(instance=website::CreateSitemapUnit_strategy)
def test_website::createsitemapunit_styleClass_type(instance):
    assert isinstance(instance.styleClass, str)


@given(instance=website::CreateSitemapUnit_strategy)
def test_website::createsitemapunit_styleClass_setter(instance):
    original = instance.styleClass
    instance.styleClass = original
    assert instance.styleClass == original

@given(instance=website::CreateSitemapUnit_strategy)
def test_website::createsitemapunit_deployedURL_type(instance):
    assert isinstance(instance.deployedURL, str)


@given(instance=website::CreateSitemapUnit_strategy)
def test_website::createsitemapunit_deployedURL_setter(instance):
    original = instance.deployedURL
    instance.deployedURL = original
    assert instance.deployedURL == original

@given(instance=website::CreateSitemapUnit_strategy)
def test_website::createsitemapunit_contentClass_type(instance):
    assert isinstance(instance.contentClass, str)


@given(instance=website::CreateSitemapUnit_strategy)
def test_website::createsitemapunit_contentClass_setter(instance):
    original = instance.contentClass
    instance.contentClass = original
    assert instance.contentClass == original

@given(instance=website::DynamicUnit_strategy)
@settings(max_examples=50)
def test_website::dynamicunit_instantiation(instance):
    assert isinstance(instance, website::DynamicUnit)

@given(instance=website::DynamicUnit_strategy)
def test_website::dynamicunit_footerClass_type(instance):
    assert isinstance(instance.footerClass, str)


@given(instance=website::DynamicUnit_strategy)
def test_website::dynamicunit_footerClass_setter(instance):
    original = instance.footerClass
    instance.footerClass = original
    assert instance.footerClass == original

@given(instance=website::DynamicUnit_strategy)
def test_website::dynamicunit_errorClass_type(instance):
    assert isinstance(instance.errorClass, str)


@given(instance=website::DynamicUnit_strategy)
def test_website::dynamicunit_errorClass_setter(instance):
    original = instance.errorClass
    instance.errorClass = original
    assert instance.errorClass == original

@given(instance=website::DynamicUnit_strategy)
def test_website::dynamicunit_footer_type(instance):
    assert isinstance(instance.footer, str)


@given(instance=website::DynamicUnit_strategy)
def test_website::dynamicunit_footer_setter(instance):
    original = instance.footer
    instance.footer = original
    assert instance.footer == original

@given(instance=website::DynamicUnit_strategy)
def test_website::dynamicunit_headerClass_type(instance):
    assert isinstance(instance.headerClass, str)


@given(instance=website::DynamicUnit_strategy)
def test_website::dynamicunit_headerClass_setter(instance):
    original = instance.headerClass
    instance.headerClass = original
    assert instance.headerClass == original

@given(instance=website::DynamicUnit_strategy)
def test_website::dynamicunit_header_type(instance):
    assert isinstance(instance.header, str)


@given(instance=website::DynamicUnit_strategy)
def test_website::dynamicunit_header_setter(instance):
    original = instance.header
    instance.header = original
    assert instance.header == original

@given(instance=website::DynamicUnit_strategy)
def test_website::dynamicunit_controlClass_type(instance):
    assert isinstance(instance.controlClass, str)


@given(instance=website::DynamicUnit_strategy)
def test_website::dynamicunit_controlClass_setter(instance):
    original = instance.controlClass
    instance.controlClass = original
    assert instance.controlClass == original

@given(instance=website::StaticUnit_strategy)
@settings(max_examples=50)
def test_website::staticunit_instantiation(instance):
    assert isinstance(instance, website::StaticUnit)

@given(instance=website::StaticUnit_strategy)
def test_website::staticunit_styleClass_type(instance):
    assert isinstance(instance.styleClass, str)


@given(instance=website::StaticUnit_strategy)
def test_website::staticunit_styleClass_setter(instance):
    original = instance.styleClass
    instance.styleClass = original
    assert instance.styleClass == original

@given(instance=website::StaticUnit_strategy)
def test_website::staticunit_contentClass_type(instance):
    assert isinstance(instance.contentClass, str)


@given(instance=website::StaticUnit_strategy)
def test_website::staticunit_contentClass_setter(instance):
    original = instance.contentClass
    instance.contentClass = original
    assert instance.contentClass == original

@given(instance=website::StaticUnit_strategy)
def test_website::staticunit_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=website::StaticUnit_strategy)
def test_website::staticunit_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=website::UnitContainer_strategy)
@settings(max_examples=50)
def test_website::unitcontainer_instantiation(instance):
    assert isinstance(instance, website::UnitContainer)

@given(instance=website::UnitSupportAction_strategy)
@settings(max_examples=50)
def test_website::unitsupportaction_instantiation(instance):
    assert isinstance(instance, website::UnitSupportAction)

@given(instance=website::UnitSupportAction_strategy)
def test_website::unitsupportaction_disable_type(instance):
    assert isinstance(instance.disable, bool)


@given(instance=website::UnitSupportAction_strategy)
def test_website::unitsupportaction_disable_setter(instance):
    original = instance.disable
    instance.disable = original
    assert instance.disable == original

@given(instance=website::UnitSupportAction_strategy)
def test_website::unitsupportaction_confirmMessage_type(instance):
    assert isinstance(instance.confirmMessage, str)


@given(instance=website::UnitSupportAction_strategy)
def test_website::unitsupportaction_confirmMessage_setter(instance):
    original = instance.confirmMessage
    instance.confirmMessage = original
    assert instance.confirmMessage == original

@given(instance=website::UnitField_strategy)
@settings(max_examples=50)
def test_website::unitfield_instantiation(instance):
    assert isinstance(instance, website::UnitField)

@given(instance=website::UnitField_strategy)
def test_website::unitfield_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=website::UnitField_strategy)
def test_website::unitfield_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=website::UnitField_strategy)
def test_website::unitfield_dateFormat_type(instance):
    assert isinstance(instance.dateFormat, str)


@given(instance=website::UnitField_strategy)
def test_website::unitfield_dateFormat_setter(instance):
    original = instance.dateFormat
    instance.dateFormat = original
    assert instance.dateFormat == original

@given(instance=website::UnitField_strategy)
def test_website::unitfield_collectionAllowRemove_type(instance):
    assert isinstance(instance.collectionAllowRemove, bool)


@given(instance=website::UnitField_strategy)
def test_website::unitfield_collectionAllowRemove_setter(instance):
    original = instance.collectionAllowRemove
    instance.collectionAllowRemove = original
    assert instance.collectionAllowRemove == original

@given(instance=website::UnitField_strategy)
def test_website::unitfield_collectionDisplayOption_type(instance):
    assert isinstance(instance.collectionDisplayOption, str)


@given(instance=website::UnitField_strategy)
def test_website::unitfield_collectionDisplayOption_setter(instance):
    original = instance.collectionDisplayOption
    instance.collectionDisplayOption = original
    assert instance.collectionDisplayOption == original

@given(instance=website::UnitField_strategy)
def test_website::unitfield_collectionAllowAdd_type(instance):
    assert isinstance(instance.collectionAllowAdd, bool)


@given(instance=website::UnitField_strategy)
def test_website::unitfield_collectionAllowAdd_setter(instance):
    original = instance.collectionAllowAdd
    instance.collectionAllowAdd = original
    assert instance.collectionAllowAdd == original

@given(instance=website::UnitField_strategy)
def test_website::unitfield_maximumDisplaySize_type(instance):
    assert isinstance(instance.maximumDisplaySize, int)


@given(instance=website::UnitField_strategy)
def test_website::unitfield_maximumDisplaySize_setter(instance):
    original = instance.maximumDisplaySize
    instance.maximumDisplaySize = original
    assert instance.maximumDisplaySize == original

@given(instance=website::Filter_strategy)
@settings(max_examples=50)
def test_website::filter_instantiation(instance):
    assert isinstance(instance, website::Filter)

@given(instance=website::Query_strategy)
@settings(max_examples=50)
def test_website::query_instantiation(instance):
    assert isinstance(instance, website::Query)

@given(instance=website::ContentUnit_strategy)
@settings(max_examples=50)
def test_website::contentunit_instantiation(instance):
    assert isinstance(instance, website::ContentUnit)

@given(instance=website::ContentUnit_strategy)
def test_website::contentunit_captionClass_type(instance):
    assert isinstance(instance.captionClass, str)


@given(instance=website::ContentUnit_strategy)
def test_website::contentunit_captionClass_setter(instance):
    original = instance.captionClass
    instance.captionClass = original
    assert instance.captionClass == original

@given(instance=website::ContentUnit_strategy)
def test_website::contentunit_createDefaultUriElement_type(instance):
    assert isinstance(instance.createDefaultUriElement, bool)


@given(instance=website::ContentUnit_strategy)
def test_website::contentunit_createDefaultUriElement_setter(instance):
    original = instance.createDefaultUriElement
    instance.createDefaultUriElement = original
    assert instance.createDefaultUriElement == original

@given(instance=website::ContentUnit_strategy)
def test_website::contentunit_requiresRole_type(instance):
    assert isinstance(instance.requiresRole, str)


@given(instance=website::ContentUnit_strategy)
def test_website::contentunit_requiresRole_setter(instance):
    original = instance.requiresRole
    instance.requiresRole = original
    assert instance.requiresRole == original

@given(instance=website::ContentUnit_strategy)
def test_website::contentunit_purposeSummary_type(instance):
    assert isinstance(instance.purposeSummary, str)


@given(instance=website::ContentUnit_strategy)
def test_website::contentunit_purposeSummary_setter(instance):
    original = instance.purposeSummary
    instance.purposeSummary = original
    assert instance.purposeSummary == original

@given(instance=website::ContentUnit_strategy)
def test_website::contentunit_omitCaption_type(instance):
    assert isinstance(instance.omitCaption, bool)


@given(instance=website::ContentUnit_strategy)
def test_website::contentunit_omitCaption_setter(instance):
    original = instance.omitCaption
    instance.omitCaption = original
    assert instance.omitCaption == original

@given(instance=website::ContentUnit_strategy)
def test_website::contentunit_uriElement_type(instance):
    assert isinstance(instance.uriElement, str)


@given(instance=website::ContentUnit_strategy)
def test_website::contentunit_uriElement_setter(instance):
    original = instance.uriElement
    instance.uriElement = original
    assert instance.uriElement == original

@given(instance=website::ContentUnit_strategy)
def test_website::contentunit_alternative_type(instance):
    assert isinstance(instance.alternative, str)


@given(instance=website::ContentUnit_strategy)
def test_website::contentunit_alternative_setter(instance):
    original = instance.alternative
    instance.alternative = original
    assert instance.alternative == original

@given(instance=MenuEntry_strategy)
@settings(max_examples=50)
def test_menuentry_instantiation(instance):
    assert isinstance(instance, MenuEntry)

@given(instance=website::EditStaticTextMenuEntry_strategy)
@settings(max_examples=50)
def test_website::editstatictextmenuentry_instantiation(instance):
    assert isinstance(instance, website::EditStaticTextMenuEntry)

@given(instance=website::MenuFeature_strategy)
@settings(max_examples=50)
def test_website::menufeature_instantiation(instance):
    assert isinstance(instance, website::MenuFeature)

@given(instance=website::ActionMenuEntry_strategy)
@settings(max_examples=50)
def test_website::actionmenuentry_instantiation(instance):
    assert isinstance(instance, website::ActionMenuEntry)

@given(instance=Menu_strategy)
@settings(max_examples=50)
def test_menu_instantiation(instance):
    assert isinstance(instance, Menu)

@given(instance=website::DynamicMenu_strategy)
@settings(max_examples=50)
def test_website::dynamicmenu_instantiation(instance):
    assert isinstance(instance, website::DynamicMenu)

@given(instance=website::StaticMenu_strategy)
@settings(max_examples=50)
def test_website::staticmenu_instantiation(instance):
    assert isinstance(instance, website::StaticMenu)

@given(instance=website::MenuEntry_strategy)
@settings(max_examples=50)
def test_website::menuentry_instantiation(instance):
    assert isinstance(instance, website::MenuEntry)

@given(instance=website::MenuEntry_strategy)
def test_website::menuentry_requiresRole_type(instance):
    assert isinstance(instance.requiresRole, str)


@given(instance=website::MenuEntry_strategy)
def test_website::menuentry_requiresRole_setter(instance):
    original = instance.requiresRole
    instance.requiresRole = original
    assert instance.requiresRole == original

@given(instance=website::QueryParameter_strategy)
@settings(max_examples=50)
def test_website::queryparameter_instantiation(instance):
    assert isinstance(instance, website::QueryParameter)

@given(instance=website::QueryParameter_strategy)
def test_website::queryparameter_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=website::QueryParameter_strategy)
def test_website::queryparameter_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=website::FilterParameter_strategy)
@settings(max_examples=50)
def test_website::filterparameter_instantiation(instance):
    assert isinstance(instance, website::FilterParameter)

@given(instance=website::FilterParameter_strategy)
def test_website::filterparameter_placeholder_type(instance):
    assert isinstance(instance.placeholder, str)


@given(instance=website::FilterParameter_strategy)
def test_website::filterparameter_placeholder_setter(instance):
    original = instance.placeholder
    instance.placeholder = original
    assert instance.placeholder == original

@given(instance=website::FilterParameter_strategy)
def test_website::filterparameter_defaultValue_type(instance):
    assert isinstance(instance.defaultValue, str)


@given(instance=website::FilterParameter_strategy)
def test_website::filterparameter_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original

@given(instance=UnitContainer_strategy)
@settings(max_examples=50)
def test_unitcontainer_instantiation(instance):
    assert isinstance(instance, UnitContainer)

@given(instance=website::Page_strategy)
@settings(max_examples=50)
def test_website::page_instantiation(instance):
    assert isinstance(instance, website::Page)

@given(instance=website::Page_strategy)
def test_website::page_navigationLabel_type(instance):
    assert isinstance(instance.navigationLabel, str)


@given(instance=website::Page_strategy)
def test_website::page_navigationLabel_setter(instance):
    original = instance.navigationLabel
    instance.navigationLabel = original
    assert instance.navigationLabel == original

@given(instance=website::Page_strategy)
def test_website::page_topMenuRank_type(instance):
    assert isinstance(instance.topMenuRank, int)


@given(instance=website::Page_strategy)
def test_website::page_topMenuRank_setter(instance):
    original = instance.topMenuRank
    instance.topMenuRank = original
    assert instance.topMenuRank == original

@given(instance=website::Page_strategy)
def test_website::page_styleClass_type(instance):
    assert isinstance(instance.styleClass, str)


@given(instance=website::Page_strategy)
def test_website::page_styleClass_setter(instance):
    original = instance.styleClass
    instance.styleClass = original
    assert instance.styleClass == original

@given(instance=website::Page_strategy)
def test_website::page_topMenuOption_type(instance):
    assert isinstance(instance.topMenuOption, str)


@given(instance=website::Page_strategy)
def test_website::page_topMenuOption_setter(instance):
    original = instance.topMenuOption
    instance.topMenuOption = original
    assert instance.topMenuOption == original

@given(instance=website::Page_strategy)
def test_website::page_authenticated_type(instance):
    assert isinstance(instance.authenticated, bool)


@given(instance=website::Page_strategy)
def test_website::page_authenticated_setter(instance):
    original = instance.authenticated
    instance.authenticated = original
    assert instance.authenticated == original

@given(instance=website::Page_strategy)
def test_website::page_uriElement_type(instance):
    assert isinstance(instance.uriElement, str)


@given(instance=website::Page_strategy)
def test_website::page_uriElement_setter(instance):
    original = instance.uriElement
    instance.uriElement = original
    assert instance.uriElement == original

@given(instance=website::UnitAssociation_strategy)
@settings(max_examples=50)
def test_website::unitassociation_instantiation(instance):
    assert isinstance(instance, website::UnitAssociation)

@given(instance=website::UnitAssociation_strategy)
def test_website::unitassociation_isSourceAssociation_type(instance):
    assert isinstance(instance.isSourceAssociation, bool)


@given(instance=website::UnitAssociation_strategy)
def test_website::unitassociation_isSourceAssociation_setter(instance):
    original = instance.isSourceAssociation
    instance.isSourceAssociation = original
    assert instance.isSourceAssociation == original

@given(instance=ImageFilter_strategy)
@settings(max_examples=50)
def test_imagefilter_instantiation(instance):
    assert isinstance(instance, ImageFilter)

@given(instance=website::ThumbnailFilter_strategy)
@settings(max_examples=50)
def test_website::thumbnailfilter_instantiation(instance):
    assert isinstance(instance, website::ThumbnailFilter)

@given(instance=website::ThumbnailFilter_strategy)
def test_website::thumbnailfilter_height_type(instance):
    assert isinstance(instance.height, int)


@given(instance=website::ThumbnailFilter_strategy)
def test_website::thumbnailfilter_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=website::ThumbnailFilter_strategy)
def test_website::thumbnailfilter_width_type(instance):
    assert isinstance(instance.width, int)


@given(instance=website::ThumbnailFilter_strategy)
def test_website::thumbnailfilter_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=website::ImageFilter_strategy)
@settings(max_examples=50)
def test_website::imagefilter_instantiation(instance):
    assert isinstance(instance, website::ImageFilter)

@given(instance=website::Order_strategy)
@settings(max_examples=50)
def test_website::order_instantiation(instance):
    assert isinstance(instance, website::Order)

@given(instance=website::Predicate_strategy)
@settings(max_examples=50)
def test_website::predicate_instantiation(instance):
    assert isinstance(instance, website::Predicate)

@given(instance=website::PageLink_strategy)
@settings(max_examples=50)
def test_website::pagelink_instantiation(instance):
    assert isinstance(instance, website::PageLink)

@given(instance=website::SelectionParameter_strategy)
@settings(max_examples=50)
def test_website::selectionparameter_instantiation(instance):
    assert isinstance(instance, website::SelectionParameter)

@given(instance=website::SelectionParameter_strategy)
def test_website::selectionparameter_optional_type(instance):
    assert isinstance(instance.optional, bool)


@given(instance=website::SelectionParameter_strategy)
def test_website::selectionparameter_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original

@given(instance=website::SelectionParameter_strategy)
def test_website::selectionparameter_defaultValue_type(instance):
    assert isinstance(instance.defaultValue, str)


@given(instance=website::SelectionParameter_strategy)
def test_website::selectionparameter_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original

@given(instance=website::BusinessOperation_strategy)
@settings(max_examples=50)
def test_website::businessoperation_instantiation(instance):
    assert isinstance(instance, website::BusinessOperation)

@given(instance=website::BusinessOperation_strategy)
def test_website::businessoperation_resultType_type(instance):
    assert isinstance(instance.resultType, str)


@given(instance=website::BusinessOperation_strategy)
def test_website::businessoperation_resultType_setter(instance):
    original = instance.resultType
    instance.resultType = original
    assert instance.resultType == original

@given(instance=website::BusinessOperation_strategy)
def test_website::businessoperation_resultMimeType_type(instance):
    assert isinstance(instance.resultMimeType, str)


@given(instance=website::BusinessOperation_strategy)
def test_website::businessoperation_resultMimeType_setter(instance):
    original = instance.resultMimeType
    instance.resultMimeType = original
    assert instance.resultMimeType == original

@given(instance=website::Selection_strategy)
@settings(max_examples=50)
def test_website::selection_instantiation(instance):
    assert isinstance(instance, website::Selection)

@given(instance=website::Selection_strategy)
def test_website::selection_distinct_type(instance):
    assert isinstance(instance.distinct, bool)


@given(instance=website::Selection_strategy)
def test_website::selection_distinct_setter(instance):
    original = instance.distinct
    instance.distinct = original
    assert instance.distinct == original

@given(instance=website::Selection_strategy)
def test_website::selection_selected_type(instance):
    assert isinstance(instance.selected, bool)


@given(instance=website::Selection_strategy)
def test_website::selection_selected_setter(instance):
    original = instance.selected
    instance.selected = original
    assert instance.selected == original

@given(instance=website::Selection_strategy)
def test_website::selection_limit_type(instance):
    assert isinstance(instance.limit, int)


@given(instance=website::Selection_strategy)
def test_website::selection_limit_setter(instance):
    original = instance.limit
    instance.limit = original
    assert instance.limit == original

@given(instance=website::View_strategy)
@settings(max_examples=50)
def test_website::view_instantiation(instance):
    assert isinstance(instance, website::View)

@given(instance=EntityAssociation_strategy)
@settings(max_examples=50)
def test_entityassociation_instantiation(instance):
    assert isinstance(instance, EntityAssociation)

@given(instance=website::AssociationWithContainment_strategy)
@settings(max_examples=50)
def test_website::associationwithcontainment_instantiation(instance):
    assert isinstance(instance, website::AssociationWithContainment)

@given(instance=website::AssociationWithContainment_strategy)
def test_website::associationwithcontainment_sourceVisible_type(instance):
    assert isinstance(instance.sourceVisible, bool)


@given(instance=website::AssociationWithContainment_strategy)
def test_website::associationwithcontainment_sourceVisible_setter(instance):
    original = instance.sourceVisible
    instance.sourceVisible = original
    assert instance.sourceVisible == original

@given(instance=website::AssociationWithoutContainment_strategy)
@settings(max_examples=50)
def test_website::associationwithoutcontainment_instantiation(instance):
    assert isinstance(instance, website::AssociationWithoutContainment)

@given(instance=website::AssociationWithoutContainment_strategy)
def test_website::associationwithoutcontainment_targetCardinality_type(instance):
    assert isinstance(instance.targetCardinality, str)


@given(instance=website::AssociationWithoutContainment_strategy)
def test_website::associationwithoutcontainment_targetCardinality_setter(instance):
    original = instance.targetCardinality
    instance.targetCardinality = original
    assert instance.targetCardinality == original

@given(instance=website::AssociationWithoutContainment_strategy)
def test_website::associationwithoutcontainment_targetUnique_type(instance):
    assert isinstance(instance.targetUnique, bool)


@given(instance=website::AssociationWithoutContainment_strategy)
def test_website::associationwithoutcontainment_targetUnique_setter(instance):
    original = instance.targetUnique
    instance.targetUnique = original
    assert instance.targetUnique == original

@given(instance=EncapsulatedFeature_strategy)
@settings(max_examples=50)
def test_encapsulatedfeature_instantiation(instance):
    assert isinstance(instance, EncapsulatedFeature)

@given(instance=website::EncapsulatedAssociation_strategy)
@settings(max_examples=50)
def test_website::encapsulatedassociation_instantiation(instance):
    assert isinstance(instance, website::EncapsulatedAssociation)

@given(instance=website::EncapsulatedAssociation_strategy)
def test_website::encapsulatedassociation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=website::EncapsulatedAssociation_strategy)
def test_website::encapsulatedassociation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=website::EncapsulatedAssociation_strategy)
def test_website::encapsulatedassociation_isSourceAssociation_type(instance):
    assert isinstance(instance.isSourceAssociation, bool)


@given(instance=website::EncapsulatedAssociation_strategy)
def test_website::encapsulatedassociation_isSourceAssociation_setter(instance):
    original = instance.isSourceAssociation
    instance.isSourceAssociation = original
    assert instance.isSourceAssociation == original

@given(instance=website::EncapsulatedAssociation_strategy)
def test_website::encapsulatedassociation_cardinality_type(instance):
    assert isinstance(instance.cardinality, str)


@given(instance=website::EncapsulatedAssociation_strategy)
def test_website::encapsulatedassociation_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original

@given(instance=website::EncapsulatedAttribute_strategy)
@settings(max_examples=50)
def test_website::encapsulatedattribute_instantiation(instance):
    assert isinstance(instance, website::EncapsulatedAttribute)

@given(instance=website::EncapsulatedAttribute_strategy)
def test_website::encapsulatedattribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=website::EncapsulatedAttribute_strategy)
def test_website::encapsulatedattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=website::EncapsulatedAttribute_strategy)
def test_website::encapsulatedattribute_cardinality_type(instance):
    assert isinstance(instance.cardinality, str)


@given(instance=website::EncapsulatedAttribute_strategy)
def test_website::encapsulatedattribute_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original

@given(instance=ViewFeature_strategy)
@settings(max_examples=50)
def test_viewfeature_instantiation(instance):
    assert isinstance(instance, ViewFeature)

@given(instance=website::ViewAssociation_strategy)
@settings(max_examples=50)
def test_website::viewassociation_instantiation(instance):
    assert isinstance(instance, website::ViewAssociation)

@given(instance=website::ViewAssociation_strategy)
def test_website::viewassociation_cardinality_type(instance):
    assert isinstance(instance.cardinality, str)


@given(instance=website::ViewAssociation_strategy)
def test_website::viewassociation_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original

@given(instance=website::EncapsulatedFeature_strategy)
@settings(max_examples=50)
def test_website::encapsulatedfeature_instantiation(instance):
    assert isinstance(instance, website::EncapsulatedFeature)

@given(instance=website::EncapsulatedFeature_strategy)
def test_website::encapsulatedfeature_columnName_type(instance):
    assert isinstance(instance.columnName, str)


@given(instance=website::EncapsulatedFeature_strategy)
def test_website::encapsulatedfeature_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original

@given(instance=website::EncapsulatedFeature_strategy)
def test_website::encapsulatedfeature_alias_type(instance):
    assert isinstance(instance.alias, str)


@given(instance=website::EncapsulatedFeature_strategy)
def test_website::encapsulatedfeature_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=website::EncapsulatedFeature_strategy)
def test_website::encapsulatedfeature_displayLabel_type(instance):
    assert isinstance(instance.displayLabel, str)


@given(instance=website::EncapsulatedFeature_strategy)
def test_website::encapsulatedfeature_displayLabel_setter(instance):
    original = instance.displayLabel
    instance.displayLabel = original
    assert instance.displayLabel == original

@given(instance=website::ViewFeature_strategy)
@settings(max_examples=50)
def test_website::viewfeature_instantiation(instance):
    assert isinstance(instance, website::ViewFeature)

@given(instance=PathElement_strategy)
@settings(max_examples=50)
def test_pathelement_instantiation(instance):
    assert isinstance(instance, PathElement)

@given(instance=website::DatePathElement_strategy)
@settings(max_examples=50)
def test_website::datepathelement_instantiation(instance):
    assert isinstance(instance, website::DatePathElement)

@given(instance=website::DatePathElement_strategy)
def test_website::datepathelement_format_type(instance):
    assert isinstance(instance.format, str)


@given(instance=website::DatePathElement_strategy)
def test_website::datepathelement_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original

@given(instance=website::StaticPathElement_strategy)
@settings(max_examples=50)
def test_website::staticpathelement_instantiation(instance):
    assert isinstance(instance, website::StaticPathElement)

@given(instance=website::StaticPathElement_strategy)
def test_website::staticpathelement_element_type(instance):
    assert isinstance(instance.element, str)


@given(instance=website::StaticPathElement_strategy)
def test_website::staticpathelement_element_setter(instance):
    original = instance.element
    instance.element = original
    assert instance.element == original

@given(instance=website::PathElement_strategy)
@settings(max_examples=50)
def test_website::pathelement_instantiation(instance):
    assert isinstance(instance, website::PathElement)

@given(instance=website::ResourceAttribute_strategy)
@settings(max_examples=50)
def test_website::resourceattribute_instantiation(instance):
    assert isinstance(instance, website::ResourceAttribute)

@given(instance=website::ResourceAttribute_strategy)
def test_website::resourceattribute_validUploadExtensions_type(instance):
    assert isinstance(instance.validUploadExtensions, str)


@given(instance=website::ResourceAttribute_strategy)
def test_website::resourceattribute_validUploadExtensions_setter(instance):
    original = instance.validUploadExtensions
    instance.validUploadExtensions = original
    assert instance.validUploadExtensions == original

@given(instance=website::ResourceAttribute_strategy)
def test_website::resourceattribute_maximumUploadSize_type(instance):
    assert isinstance(instance.maximumUploadSize, int)


@given(instance=website::ResourceAttribute_strategy)
def test_website::resourceattribute_maximumUploadSize_setter(instance):
    original = instance.maximumUploadSize
    instance.maximumUploadSize = original
    assert instance.maximumUploadSize == original

@given(instance=website::ResourceAttribute_strategy)
def test_website::resourceattribute_uploadsWithinWebsite_type(instance):
    assert isinstance(instance.uploadsWithinWebsite, bool)


@given(instance=website::ResourceAttribute_strategy)
def test_website::resourceattribute_uploadsWithinWebsite_setter(instance):
    original = instance.uploadsWithinWebsite
    instance.uploadsWithinWebsite = original
    assert instance.uploadsWithinWebsite == original

@given(instance=website::ResourceAttribute_strategy)
def test_website::resourceattribute_validUploadMimeTypes_type(instance):
    assert isinstance(instance.validUploadMimeTypes, str)


@given(instance=website::ResourceAttribute_strategy)
def test_website::resourceattribute_validUploadMimeTypes_setter(instance):
    original = instance.validUploadMimeTypes
    instance.validUploadMimeTypes = original
    assert instance.validUploadMimeTypes == original

@given(instance=website::UrlAttribute_strategy)
@settings(max_examples=50)
def test_website::urlattribute_instantiation(instance):
    assert isinstance(instance, website::UrlAttribute)

@given(instance=website::UrlAttribute_strategy)
def test_website::urlattribute_displayValue_type(instance):
    assert isinstance(instance.displayValue, str)


@given(instance=website::UrlAttribute_strategy)
def test_website::urlattribute_displayValue_setter(instance):
    original = instance.displayValue
    instance.displayValue = original
    assert instance.displayValue == original

@given(instance=website::DateAttribute_strategy)
@settings(max_examples=50)
def test_website::dateattribute_instantiation(instance):
    assert isinstance(instance, website::DateAttribute)

@given(instance=website::DateAttribute_strategy)
def test_website::dateattribute_details_type(instance):
    assert isinstance(instance.details, str)


@given(instance=website::DateAttribute_strategy)
def test_website::dateattribute_details_setter(instance):
    original = instance.details
    instance.details = original
    assert instance.details == original

@given(instance=website::DateAttribute_strategy)
def test_website::dateattribute_format_type(instance):
    assert isinstance(instance.format, str)


@given(instance=website::DateAttribute_strategy)
def test_website::dateattribute_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original
