import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    EncapsulatedFeature,
    ViewFeature,
    persistence::EncapsulatedFeature,
    EntityAssociation,
    persistence::AssociationWithContainment,
    persistence::AssociationWithoutContainment,
    persistence::AssociationKey,
    Association,
    ResourceAttribute,
    persistence::ImageAttribute,
    persistence::FileAttribute,
    PathElement,
    persistence::DatePathElement,
    persistence::StaticPathElement,
    persistence::PathElement,
    EntityAttribute,
    persistence::LocationAttribute,
    persistence::ResourceAttribute,
    persistence::DateAttribute,
    persistence::UrlAttribute,
    persistence::DataTypeAttribute,
    Attribute,
    persistence::EncapsulatedAttribute,
    EntityFeature,
    persistence::EntityAttribute,
    NamedDisplayElement,
    persistence::ViewAssociation,
    EntityOrView,
    persistence::View,
    persistence::Entity,
    persistence::EntityAssociation,
    ModelLabelFeature,
    persistence::ModelLabelAssociation,
    persistence::ModelLabelAttribute,
    persistence::ModelLabelFeature,
    persistence::Label,
    persistence::EncapsulatedAssociation,
    persistence::Expression,
    Label,
    Feature,
    persistence::EntityFeature,
    persistence::ViewFeature,
    persistence::Attribute,
    persistence::Association,
    persistence::Feature,
    Classifier,
    NamedElement,
    persistence::ModelLabel,
    persistence::EntityOrView,
    persistence::DataType,
    persistence::SerializationGroup,
    persistence::Persistence,
    OrmTechnologies,
    DateDetails,
    isHasChoices,
    Cardinality,
    DatabaseTechnologies,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_persistence::encapsulatedfeature_is_not_abstract():
    assert not inspect.isabstract(persistence::EncapsulatedFeature)


def test_persistence::encapsulatedfeature_constructor_exists():
    assert callable(persistence::EncapsulatedFeature.__init__)


def test_persistence::encapsulatedfeature_constructor_args():
    sig = inspect.signature(persistence::EncapsulatedFeature.__init__)
    params = list(sig.parameters.keys())
    assert "displayLabel" in params, "Missing parameter 'displayLabel'"
    assert "alias" in params, "Missing parameter 'alias'"
    assert "columnName" in params, "Missing parameter 'columnName'"

def test_persistence::encapsulatedfeature_has_displayLabel():
    assert hasattr(persistence::EncapsulatedFeature, "displayLabel")
    descriptor = None
    for klass in persistence::EncapsulatedFeature.__mro__:
        if "displayLabel" in klass.__dict__:
            descriptor = klass.__dict__["displayLabel"]
            break
    assert isinstance(descriptor, property)

def test_persistence::encapsulatedfeature_has_alias():
    assert hasattr(persistence::EncapsulatedFeature, "alias")
    descriptor = None
    for klass in persistence::EncapsulatedFeature.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)

def test_persistence::encapsulatedfeature_has_columnName():
    assert hasattr(persistence::EncapsulatedFeature, "columnName")
    descriptor = None
    for klass in persistence::EncapsulatedFeature.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)



def test_entityassociation_is_not_abstract():
    assert not inspect.isabstract(EntityAssociation)


def test_entityassociation_constructor_exists():
    assert callable(EntityAssociation.__init__)


def test_entityassociation_constructor_args():
    sig = inspect.signature(EntityAssociation.__init__)
    params = list(sig.parameters.keys())



def test_persistence::associationwithcontainment_is_not_abstract():
    assert not inspect.isabstract(persistence::AssociationWithContainment)


def test_persistence::associationwithcontainment_constructor_exists():
    assert callable(persistence::AssociationWithContainment.__init__)


def test_persistence::associationwithcontainment_constructor_args():
    sig = inspect.signature(persistence::AssociationWithContainment.__init__)
    params = list(sig.parameters.keys())
    assert "sourceVisible" in params, "Missing parameter 'sourceVisible'"

def test_persistence::associationwithcontainment_has_sourceVisible():
    assert hasattr(persistence::AssociationWithContainment, "sourceVisible")
    descriptor = None
    for klass in persistence::AssociationWithContainment.__mro__:
        if "sourceVisible" in klass.__dict__:
            descriptor = klass.__dict__["sourceVisible"]
            break
    assert isinstance(descriptor, property)



def test_persistence::associationwithoutcontainment_is_not_abstract():
    assert not inspect.isabstract(persistence::AssociationWithoutContainment)


def test_persistence::associationwithoutcontainment_constructor_exists():
    assert callable(persistence::AssociationWithoutContainment.__init__)


def test_persistence::associationwithoutcontainment_constructor_args():
    sig = inspect.signature(persistence::AssociationWithoutContainment.__init__)
    params = list(sig.parameters.keys())
    assert "targetCardinality" in params, "Missing parameter 'targetCardinality'"
    assert "targetUnique" in params, "Missing parameter 'targetUnique'"

def test_persistence::associationwithoutcontainment_has_targetCardinality():
    assert hasattr(persistence::AssociationWithoutContainment, "targetCardinality")
    descriptor = None
    for klass in persistence::AssociationWithoutContainment.__mro__:
        if "targetCardinality" in klass.__dict__:
            descriptor = klass.__dict__["targetCardinality"]
            break
    assert isinstance(descriptor, property)

def test_persistence::associationwithoutcontainment_has_targetUnique():
    assert hasattr(persistence::AssociationWithoutContainment, "targetUnique")
    descriptor = None
    for klass in persistence::AssociationWithoutContainment.__mro__:
        if "targetUnique" in klass.__dict__:
            descriptor = klass.__dict__["targetUnique"]
            break
    assert isinstance(descriptor, property)



def test_persistence::associationkey_is_not_abstract():
    assert not inspect.isabstract(persistence::AssociationKey)


def test_persistence::associationkey_constructor_exists():
    assert callable(persistence::AssociationKey.__init__)


def test_persistence::associationkey_constructor_args():
    sig = inspect.signature(persistence::AssociationKey.__init__)
    params = list(sig.parameters.keys())



def test_association_is_not_abstract():
    assert not inspect.isabstract(Association)


def test_association_constructor_exists():
    assert callable(Association.__init__)


def test_association_constructor_args():
    sig = inspect.signature(Association.__init__)
    params = list(sig.parameters.keys())



def test_resourceattribute_is_not_abstract():
    assert not inspect.isabstract(ResourceAttribute)


def test_resourceattribute_constructor_exists():
    assert callable(ResourceAttribute.__init__)


def test_resourceattribute_constructor_args():
    sig = inspect.signature(ResourceAttribute.__init__)
    params = list(sig.parameters.keys())



def test_persistence::imageattribute_is_not_abstract():
    assert not inspect.isabstract(persistence::ImageAttribute)


def test_persistence::imageattribute_constructor_exists():
    assert callable(persistence::ImageAttribute.__init__)


def test_persistence::imageattribute_constructor_args():
    sig = inspect.signature(persistence::ImageAttribute.__init__)
    params = list(sig.parameters.keys())



def test_persistence::fileattribute_is_not_abstract():
    assert not inspect.isabstract(persistence::FileAttribute)


def test_persistence::fileattribute_constructor_exists():
    assert callable(persistence::FileAttribute.__init__)


def test_persistence::fileattribute_constructor_args():
    sig = inspect.signature(persistence::FileAttribute.__init__)
    params = list(sig.parameters.keys())



def test_pathelement_is_not_abstract():
    assert not inspect.isabstract(PathElement)


def test_pathelement_constructor_exists():
    assert callable(PathElement.__init__)


def test_pathelement_constructor_args():
    sig = inspect.signature(PathElement.__init__)
    params = list(sig.parameters.keys())



def test_persistence::datepathelement_is_not_abstract():
    assert not inspect.isabstract(persistence::DatePathElement)


def test_persistence::datepathelement_constructor_exists():
    assert callable(persistence::DatePathElement.__init__)


def test_persistence::datepathelement_constructor_args():
    sig = inspect.signature(persistence::DatePathElement.__init__)
    params = list(sig.parameters.keys())
    assert "format" in params, "Missing parameter 'format'"

def test_persistence::datepathelement_has_format():
    assert hasattr(persistence::DatePathElement, "format")
    descriptor = None
    for klass in persistence::DatePathElement.__mro__:
        if "format" in klass.__dict__:
            descriptor = klass.__dict__["format"]
            break
    assert isinstance(descriptor, property)



def test_persistence::staticpathelement_is_not_abstract():
    assert not inspect.isabstract(persistence::StaticPathElement)


def test_persistence::staticpathelement_constructor_exists():
    assert callable(persistence::StaticPathElement.__init__)


def test_persistence::staticpathelement_constructor_args():
    sig = inspect.signature(persistence::StaticPathElement.__init__)
    params = list(sig.parameters.keys())
    assert "element" in params, "Missing parameter 'element'"

def test_persistence::staticpathelement_has_element():
    assert hasattr(persistence::StaticPathElement, "element")
    descriptor = None
    for klass in persistence::StaticPathElement.__mro__:
        if "element" in klass.__dict__:
            descriptor = klass.__dict__["element"]
            break
    assert isinstance(descriptor, property)



def test_persistence::pathelement_is_not_abstract():
    assert not inspect.isabstract(persistence::PathElement)


def test_persistence::pathelement_constructor_exists():
    assert callable(persistence::PathElement.__init__)


def test_persistence::pathelement_constructor_args():
    sig = inspect.signature(persistence::PathElement.__init__)
    params = list(sig.parameters.keys())



def test_entityattribute_is_not_abstract():
    assert not inspect.isabstract(EntityAttribute)


def test_entityattribute_constructor_exists():
    assert callable(EntityAttribute.__init__)


def test_entityattribute_constructor_args():
    sig = inspect.signature(EntityAttribute.__init__)
    params = list(sig.parameters.keys())



def test_persistence::locationattribute_is_not_abstract():
    assert not inspect.isabstract(persistence::LocationAttribute)


def test_persistence::locationattribute_constructor_exists():
    assert callable(persistence::LocationAttribute.__init__)


def test_persistence::locationattribute_constructor_args():
    sig = inspect.signature(persistence::LocationAttribute.__init__)
    params = list(sig.parameters.keys())



def test_persistence::resourceattribute_is_not_abstract():
    assert not inspect.isabstract(persistence::ResourceAttribute)


def test_persistence::resourceattribute_constructor_exists():
    assert callable(persistence::ResourceAttribute.__init__)


def test_persistence::resourceattribute_constructor_args():
    sig = inspect.signature(persistence::ResourceAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "uploadsWithinWebsite" in params, "Missing parameter 'uploadsWithinWebsite'"
    assert "validUploadExtensions" in params, "Missing parameter 'validUploadExtensions'"
    assert "validUploadMimeTypes" in params, "Missing parameter 'validUploadMimeTypes'"
    assert "maximumUploadSize" in params, "Missing parameter 'maximumUploadSize'"

def test_persistence::resourceattribute_has_uploadsWithinWebsite():
    assert hasattr(persistence::ResourceAttribute, "uploadsWithinWebsite")
    descriptor = None
    for klass in persistence::ResourceAttribute.__mro__:
        if "uploadsWithinWebsite" in klass.__dict__:
            descriptor = klass.__dict__["uploadsWithinWebsite"]
            break
    assert isinstance(descriptor, property)

def test_persistence::resourceattribute_has_validUploadExtensions():
    assert hasattr(persistence::ResourceAttribute, "validUploadExtensions")
    descriptor = None
    for klass in persistence::ResourceAttribute.__mro__:
        if "validUploadExtensions" in klass.__dict__:
            descriptor = klass.__dict__["validUploadExtensions"]
            break
    assert isinstance(descriptor, property)

def test_persistence::resourceattribute_has_validUploadMimeTypes():
    assert hasattr(persistence::ResourceAttribute, "validUploadMimeTypes")
    descriptor = None
    for klass in persistence::ResourceAttribute.__mro__:
        if "validUploadMimeTypes" in klass.__dict__:
            descriptor = klass.__dict__["validUploadMimeTypes"]
            break
    assert isinstance(descriptor, property)

def test_persistence::resourceattribute_has_maximumUploadSize():
    assert hasattr(persistence::ResourceAttribute, "maximumUploadSize")
    descriptor = None
    for klass in persistence::ResourceAttribute.__mro__:
        if "maximumUploadSize" in klass.__dict__:
            descriptor = klass.__dict__["maximumUploadSize"]
            break
    assert isinstance(descriptor, property)



def test_persistence::dateattribute_is_not_abstract():
    assert not inspect.isabstract(persistence::DateAttribute)


def test_persistence::dateattribute_constructor_exists():
    assert callable(persistence::DateAttribute.__init__)


def test_persistence::dateattribute_constructor_args():
    sig = inspect.signature(persistence::DateAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "details" in params, "Missing parameter 'details'"
    assert "format" in params, "Missing parameter 'format'"

def test_persistence::dateattribute_has_details():
    assert hasattr(persistence::DateAttribute, "details")
    descriptor = None
    for klass in persistence::DateAttribute.__mro__:
        if "details" in klass.__dict__:
            descriptor = klass.__dict__["details"]
            break
    assert isinstance(descriptor, property)

def test_persistence::dateattribute_has_format():
    assert hasattr(persistence::DateAttribute, "format")
    descriptor = None
    for klass in persistence::DateAttribute.__mro__:
        if "format" in klass.__dict__:
            descriptor = klass.__dict__["format"]
            break
    assert isinstance(descriptor, property)



def test_persistence::urlattribute_is_not_abstract():
    assert not inspect.isabstract(persistence::UrlAttribute)


def test_persistence::urlattribute_constructor_exists():
    assert callable(persistence::UrlAttribute.__init__)


def test_persistence::urlattribute_constructor_args():
    sig = inspect.signature(persistence::UrlAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "displayValue" in params, "Missing parameter 'displayValue'"

def test_persistence::urlattribute_has_displayValue():
    assert hasattr(persistence::UrlAttribute, "displayValue")
    descriptor = None
    for klass in persistence::UrlAttribute.__mro__:
        if "displayValue" in klass.__dict__:
            descriptor = klass.__dict__["displayValue"]
            break
    assert isinstance(descriptor, property)



def test_persistence::datatypeattribute_is_not_abstract():
    assert not inspect.isabstract(persistence::DataTypeAttribute)


def test_persistence::datatypeattribute_constructor_exists():
    assert callable(persistence::DataTypeAttribute.__init__)


def test_persistence::datatypeattribute_constructor_args():
    sig = inspect.signature(persistence::DataTypeAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "caseInsensitive" in params, "Missing parameter 'caseInsensitive'"
    assert "obfuscateFormFields" in params, "Missing parameter 'obfuscateFormFields'"
    assert "encrypt" in params, "Missing parameter 'encrypt'"

def test_persistence::datatypeattribute_has_caseInsensitive():
    assert hasattr(persistence::DataTypeAttribute, "caseInsensitive")
    descriptor = None
    for klass in persistence::DataTypeAttribute.__mro__:
        if "caseInsensitive" in klass.__dict__:
            descriptor = klass.__dict__["caseInsensitive"]
            break
    assert isinstance(descriptor, property)

def test_persistence::datatypeattribute_has_obfuscateFormFields():
    assert hasattr(persistence::DataTypeAttribute, "obfuscateFormFields")
    descriptor = None
    for klass in persistence::DataTypeAttribute.__mro__:
        if "obfuscateFormFields" in klass.__dict__:
            descriptor = klass.__dict__["obfuscateFormFields"]
            break
    assert isinstance(descriptor, property)

def test_persistence::datatypeattribute_has_encrypt():
    assert hasattr(persistence::DataTypeAttribute, "encrypt")
    descriptor = None
    for klass in persistence::DataTypeAttribute.__mro__:
        if "encrypt" in klass.__dict__:
            descriptor = klass.__dict__["encrypt"]
            break
    assert isinstance(descriptor, property)



def test_attribute_is_not_abstract():
    assert not inspect.isabstract(Attribute)


def test_attribute_constructor_exists():
    assert callable(Attribute.__init__)


def test_attribute_constructor_args():
    sig = inspect.signature(Attribute.__init__)
    params = list(sig.parameters.keys())



def test_persistence::encapsulatedattribute_is_not_abstract():
    assert not inspect.isabstract(persistence::EncapsulatedAttribute)


def test_persistence::encapsulatedattribute_constructor_exists():
    assert callable(persistence::EncapsulatedAttribute.__init__)


def test_persistence::encapsulatedattribute_constructor_args():
    sig = inspect.signature(persistence::EncapsulatedAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "cardinality" in params, "Missing parameter 'cardinality'"
    assert "name" in params, "Missing parameter 'name'"

def test_persistence::encapsulatedattribute_has_cardinality():
    assert hasattr(persistence::EncapsulatedAttribute, "cardinality")
    descriptor = None
    for klass in persistence::EncapsulatedAttribute.__mro__:
        if "cardinality" in klass.__dict__:
            descriptor = klass.__dict__["cardinality"]
            break
    assert isinstance(descriptor, property)

def test_persistence::encapsulatedattribute_has_name():
    assert hasattr(persistence::EncapsulatedAttribute, "name")
    descriptor = None
    for klass in persistence::EncapsulatedAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_entityfeature_is_not_abstract():
    assert not inspect.isabstract(EntityFeature)


def test_entityfeature_constructor_exists():
    assert callable(EntityFeature.__init__)


def test_entityfeature_constructor_args():
    sig = inspect.signature(EntityFeature.__init__)
    params = list(sig.parameters.keys())



def test_persistence::entityattribute_is_not_abstract():
    assert not inspect.isabstract(persistence::EntityAttribute)


def test_persistence::entityattribute_constructor_exists():
    assert callable(persistence::EntityAttribute.__init__)


def test_persistence::entityattribute_constructor_args():
    sig = inspect.signature(persistence::EntityAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "unique" in params, "Missing parameter 'unique'"
    assert "ormType" in params, "Missing parameter 'ormType'"
    assert "hidden" in params, "Missing parameter 'hidden'"
    assert "interfaceType" in params, "Missing parameter 'interfaceType'"
    assert "persistentType" in params, "Missing parameter 'persistentType'"
    assert "containerUnique" in params, "Missing parameter 'containerUnique'"

def test_persistence::entityattribute_has_unique():
    assert hasattr(persistence::EntityAttribute, "unique")
    descriptor = None
    for klass in persistence::EntityAttribute.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)

def test_persistence::entityattribute_has_ormType():
    assert hasattr(persistence::EntityAttribute, "ormType")
    descriptor = None
    for klass in persistence::EntityAttribute.__mro__:
        if "ormType" in klass.__dict__:
            descriptor = klass.__dict__["ormType"]
            break
    assert isinstance(descriptor, property)

def test_persistence::entityattribute_has_hidden():
    assert hasattr(persistence::EntityAttribute, "hidden")
    descriptor = None
    for klass in persistence::EntityAttribute.__mro__:
        if "hidden" in klass.__dict__:
            descriptor = klass.__dict__["hidden"]
            break
    assert isinstance(descriptor, property)

def test_persistence::entityattribute_has_interfaceType():
    assert hasattr(persistence::EntityAttribute, "interfaceType")
    descriptor = None
    for klass in persistence::EntityAttribute.__mro__:
        if "interfaceType" in klass.__dict__:
            descriptor = klass.__dict__["interfaceType"]
            break
    assert isinstance(descriptor, property)

def test_persistence::entityattribute_has_persistentType():
    assert hasattr(persistence::EntityAttribute, "persistentType")
    descriptor = None
    for klass in persistence::EntityAttribute.__mro__:
        if "persistentType" in klass.__dict__:
            descriptor = klass.__dict__["persistentType"]
            break
    assert isinstance(descriptor, property)

def test_persistence::entityattribute_has_containerUnique():
    assert hasattr(persistence::EntityAttribute, "containerUnique")
    descriptor = None
    for klass in persistence::EntityAttribute.__mro__:
        if "containerUnique" in klass.__dict__:
            descriptor = klass.__dict__["containerUnique"]
            break
    assert isinstance(descriptor, property)



def test_nameddisplayelement_is_not_abstract():
    assert not inspect.isabstract(NamedDisplayElement)


def test_nameddisplayelement_constructor_exists():
    assert callable(NamedDisplayElement.__init__)


def test_nameddisplayelement_constructor_args():
    sig = inspect.signature(NamedDisplayElement.__init__)
    params = list(sig.parameters.keys())



def test_persistence::viewassociation_is_not_abstract():
    assert not inspect.isabstract(persistence::ViewAssociation)


def test_persistence::viewassociation_constructor_exists():
    assert callable(persistence::ViewAssociation.__init__)


def test_persistence::viewassociation_constructor_args():
    sig = inspect.signature(persistence::ViewAssociation.__init__)
    params = list(sig.parameters.keys())
    assert "cardinality" in params, "Missing parameter 'cardinality'"

def test_persistence::viewassociation_has_cardinality():
    assert hasattr(persistence::ViewAssociation, "cardinality")
    descriptor = None
    for klass in persistence::ViewAssociation.__mro__:
        if "cardinality" in klass.__dict__:
            descriptor = klass.__dict__["cardinality"]
            break
    assert isinstance(descriptor, property)



def test_entityorview_is_not_abstract():
    assert not inspect.isabstract(EntityOrView)


def test_entityorview_constructor_exists():
    assert callable(EntityOrView.__init__)


def test_entityorview_constructor_args():
    sig = inspect.signature(EntityOrView.__init__)
    params = list(sig.parameters.keys())



def test_persistence::view_is_not_abstract():
    assert not inspect.isabstract(persistence::View)


def test_persistence::view_constructor_exists():
    assert callable(persistence::View.__init__)


def test_persistence::view_constructor_args():
    sig = inspect.signature(persistence::View.__init__)
    params = list(sig.parameters.keys())



def test_persistence::entity_is_not_abstract():
    assert not inspect.isabstract(persistence::Entity)


def test_persistence::entity_constructor_exists():
    assert callable(persistence::Entity.__init__)


def test_persistence::entity_constructor_args():
    sig = inspect.signature(persistence::Entity.__init__)
    params = list(sig.parameters.keys())



def test_persistence::entityassociation_is_not_abstract():
    assert not inspect.isabstract(persistence::EntityAssociation)


def test_persistence::entityassociation_constructor_exists():
    assert callable(persistence::EntityAssociation.__init__)


def test_persistence::entityassociation_constructor_args():
    sig = inspect.signature(persistence::EntityAssociation.__init__)
    params = list(sig.parameters.keys())
    assert "pivotTableName" in params, "Missing parameter 'pivotTableName'"
    assert "targetFeatureName" in params, "Missing parameter 'targetFeatureName'"
    assert "targetColumnName" in params, "Missing parameter 'targetColumnName'"
    assert "targetFooterClass" in params, "Missing parameter 'targetFooterClass'"
    assert "targetInputClass" in params, "Missing parameter 'targetInputClass'"
    assert "unique" in params, "Missing parameter 'unique'"
    assert "targetDisplayLabel" in params, "Missing parameter 'targetDisplayLabel'"
    assert "targetPrimaryKey" in params, "Missing parameter 'targetPrimaryKey'"
    assert "targetDisplayClass" in params, "Missing parameter 'targetDisplayClass'"
    assert "targetHeaderClass" in params, "Missing parameter 'targetHeaderClass'"
    assert "bidirectional" in params, "Missing parameter 'bidirectional'"

def test_persistence::entityassociation_has_pivotTableName():
    assert hasattr(persistence::EntityAssociation, "pivotTableName")
    descriptor = None
    for klass in persistence::EntityAssociation.__mro__:
        if "pivotTableName" in klass.__dict__:
            descriptor = klass.__dict__["pivotTableName"]
            break
    assert isinstance(descriptor, property)

def test_persistence::entityassociation_has_targetFeatureName():
    assert hasattr(persistence::EntityAssociation, "targetFeatureName")
    descriptor = None
    for klass in persistence::EntityAssociation.__mro__:
        if "targetFeatureName" in klass.__dict__:
            descriptor = klass.__dict__["targetFeatureName"]
            break
    assert isinstance(descriptor, property)

def test_persistence::entityassociation_has_targetColumnName():
    assert hasattr(persistence::EntityAssociation, "targetColumnName")
    descriptor = None
    for klass in persistence::EntityAssociation.__mro__:
        if "targetColumnName" in klass.__dict__:
            descriptor = klass.__dict__["targetColumnName"]
            break
    assert isinstance(descriptor, property)

def test_persistence::entityassociation_has_targetFooterClass():
    assert hasattr(persistence::EntityAssociation, "targetFooterClass")
    descriptor = None
    for klass in persistence::EntityAssociation.__mro__:
        if "targetFooterClass" in klass.__dict__:
            descriptor = klass.__dict__["targetFooterClass"]
            break
    assert isinstance(descriptor, property)

def test_persistence::entityassociation_has_targetInputClass():
    assert hasattr(persistence::EntityAssociation, "targetInputClass")
    descriptor = None
    for klass in persistence::EntityAssociation.__mro__:
        if "targetInputClass" in klass.__dict__:
            descriptor = klass.__dict__["targetInputClass"]
            break
    assert isinstance(descriptor, property)

def test_persistence::entityassociation_has_unique():
    assert hasattr(persistence::EntityAssociation, "unique")
    descriptor = None
    for klass in persistence::EntityAssociation.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)

def test_persistence::entityassociation_has_targetDisplayLabel():
    assert hasattr(persistence::EntityAssociation, "targetDisplayLabel")
    descriptor = None
    for klass in persistence::EntityAssociation.__mro__:
        if "targetDisplayLabel" in klass.__dict__:
            descriptor = klass.__dict__["targetDisplayLabel"]
            break
    assert isinstance(descriptor, property)

def test_persistence::entityassociation_has_targetPrimaryKey():
    assert hasattr(persistence::EntityAssociation, "targetPrimaryKey")
    descriptor = None
    for klass in persistence::EntityAssociation.__mro__:
        if "targetPrimaryKey" in klass.__dict__:
            descriptor = klass.__dict__["targetPrimaryKey"]
            break
    assert isinstance(descriptor, property)

def test_persistence::entityassociation_has_targetDisplayClass():
    assert hasattr(persistence::EntityAssociation, "targetDisplayClass")
    descriptor = None
    for klass in persistence::EntityAssociation.__mro__:
        if "targetDisplayClass" in klass.__dict__:
            descriptor = klass.__dict__["targetDisplayClass"]
            break
    assert isinstance(descriptor, property)

def test_persistence::entityassociation_has_targetHeaderClass():
    assert hasattr(persistence::EntityAssociation, "targetHeaderClass")
    descriptor = None
    for klass in persistence::EntityAssociation.__mro__:
        if "targetHeaderClass" in klass.__dict__:
            descriptor = klass.__dict__["targetHeaderClass"]
            break
    assert isinstance(descriptor, property)

def test_persistence::entityassociation_has_bidirectional():
    assert hasattr(persistence::EntityAssociation, "bidirectional")
    descriptor = None
    for klass in persistence::EntityAssociation.__mro__:
        if "bidirectional" in klass.__dict__:
            descriptor = klass.__dict__["bidirectional"]
            break
    assert isinstance(descriptor, property)



def test_modellabelfeature_is_not_abstract():
    assert not inspect.isabstract(ModelLabelFeature)


def test_modellabelfeature_constructor_exists():
    assert callable(ModelLabelFeature.__init__)


def test_modellabelfeature_constructor_args():
    sig = inspect.signature(ModelLabelFeature.__init__)
    params = list(sig.parameters.keys())



def test_persistence::modellabelassociation_is_not_abstract():
    assert not inspect.isabstract(persistence::ModelLabelAssociation)


def test_persistence::modellabelassociation_constructor_exists():
    assert callable(persistence::ModelLabelAssociation.__init__)


def test_persistence::modellabelassociation_constructor_args():
    sig = inspect.signature(persistence::ModelLabelAssociation.__init__)
    params = list(sig.parameters.keys())
    assert "isSourceAssociation" in params, "Missing parameter 'isSourceAssociation'"

def test_persistence::modellabelassociation_has_isSourceAssociation():
    assert hasattr(persistence::ModelLabelAssociation, "isSourceAssociation")
    descriptor = None
    for klass in persistence::ModelLabelAssociation.__mro__:
        if "isSourceAssociation" in klass.__dict__:
            descriptor = klass.__dict__["isSourceAssociation"]
            break
    assert isinstance(descriptor, property)



def test_persistence::modellabelattribute_is_not_abstract():
    assert not inspect.isabstract(persistence::ModelLabelAttribute)


def test_persistence::modellabelattribute_constructor_exists():
    assert callable(persistence::ModelLabelAttribute.__init__)


def test_persistence::modellabelattribute_constructor_args():
    sig = inspect.signature(persistence::ModelLabelAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "dateFormat" in params, "Missing parameter 'dateFormat'"

def test_persistence::modellabelattribute_has_dateFormat():
    assert hasattr(persistence::ModelLabelAttribute, "dateFormat")
    descriptor = None
    for klass in persistence::ModelLabelAttribute.__mro__:
        if "dateFormat" in klass.__dict__:
            descriptor = klass.__dict__["dateFormat"]
            break
    assert isinstance(descriptor, property)



def test_persistence::modellabelfeature_is_not_abstract():
    assert not inspect.isabstract(persistence::ModelLabelFeature)


def test_persistence::modellabelfeature_constructor_exists():
    assert callable(persistence::ModelLabelFeature.__init__)


def test_persistence::modellabelfeature_constructor_args():
    sig = inspect.signature(persistence::ModelLabelFeature.__init__)
    params = list(sig.parameters.keys())



def test_persistence::label_is_not_abstract():
    assert not inspect.isabstract(persistence::Label)


def test_persistence::label_constructor_exists():
    assert callable(persistence::Label.__init__)


def test_persistence::label_constructor_args():
    sig = inspect.signature(persistence::Label.__init__)
    params = list(sig.parameters.keys())



def test_persistence::encapsulatedassociation_is_not_abstract():
    assert not inspect.isabstract(persistence::EncapsulatedAssociation)


def test_persistence::encapsulatedassociation_constructor_exists():
    assert callable(persistence::EncapsulatedAssociation.__init__)


def test_persistence::encapsulatedassociation_constructor_args():
    sig = inspect.signature(persistence::EncapsulatedAssociation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "cardinality" in params, "Missing parameter 'cardinality'"
    assert "isSourceAssociation" in params, "Missing parameter 'isSourceAssociation'"

def test_persistence::encapsulatedassociation_has_name():
    assert hasattr(persistence::EncapsulatedAssociation, "name")
    descriptor = None
    for klass in persistence::EncapsulatedAssociation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_persistence::encapsulatedassociation_has_cardinality():
    assert hasattr(persistence::EncapsulatedAssociation, "cardinality")
    descriptor = None
    for klass in persistence::EncapsulatedAssociation.__mro__:
        if "cardinality" in klass.__dict__:
            descriptor = klass.__dict__["cardinality"]
            break
    assert isinstance(descriptor, property)

def test_persistence::encapsulatedassociation_has_isSourceAssociation():
    assert hasattr(persistence::EncapsulatedAssociation, "isSourceAssociation")
    descriptor = None
    for klass in persistence::EncapsulatedAssociation.__mro__:
        if "isSourceAssociation" in klass.__dict__:
            descriptor = klass.__dict__["isSourceAssociation"]
            break
    assert isinstance(descriptor, property)



def test_persistence::expression_is_not_abstract():
    assert not inspect.isabstract(persistence::Expression)


def test_persistence::expression_constructor_exists():
    assert callable(persistence::Expression.__init__)


def test_persistence::expression_constructor_args():
    sig = inspect.signature(persistence::Expression.__init__)
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



def test_persistence::entityfeature_is_not_abstract():
    assert not inspect.isabstract(persistence::EntityFeature)


def test_persistence::entityfeature_constructor_exists():
    assert callable(persistence::EntityFeature.__init__)


def test_persistence::entityfeature_constructor_args():
    sig = inspect.signature(persistence::EntityFeature.__init__)
    params = list(sig.parameters.keys())
    assert "customiseSet" in params, "Missing parameter 'customiseSet'"
    assert "cardinality" in params, "Missing parameter 'cardinality'"
    assert "ordered" in params, "Missing parameter 'ordered'"
    assert "singletonName" in params, "Missing parameter 'singletonName'"
    assert "columnName" in params, "Missing parameter 'columnName'"
    assert "pluralisedName" in params, "Missing parameter 'pluralisedName'"
    assert "primaryKey" in params, "Missing parameter 'primaryKey'"
    assert "booleanIsHasChoice" in params, "Missing parameter 'booleanIsHasChoice'"
    assert "derived" in params, "Missing parameter 'derived'"

def test_persistence::entityfeature_has_customiseSet():
    assert hasattr(persistence::EntityFeature, "customiseSet")
    descriptor = None
    for klass in persistence::EntityFeature.__mro__:
        if "customiseSet" in klass.__dict__:
            descriptor = klass.__dict__["customiseSet"]
            break
    assert isinstance(descriptor, property)

def test_persistence::entityfeature_has_cardinality():
    assert hasattr(persistence::EntityFeature, "cardinality")
    descriptor = None
    for klass in persistence::EntityFeature.__mro__:
        if "cardinality" in klass.__dict__:
            descriptor = klass.__dict__["cardinality"]
            break
    assert isinstance(descriptor, property)

def test_persistence::entityfeature_has_ordered():
    assert hasattr(persistence::EntityFeature, "ordered")
    descriptor = None
    for klass in persistence::EntityFeature.__mro__:
        if "ordered" in klass.__dict__:
            descriptor = klass.__dict__["ordered"]
            break
    assert isinstance(descriptor, property)

def test_persistence::entityfeature_has_singletonName():
    assert hasattr(persistence::EntityFeature, "singletonName")
    descriptor = None
    for klass in persistence::EntityFeature.__mro__:
        if "singletonName" in klass.__dict__:
            descriptor = klass.__dict__["singletonName"]
            break
    assert isinstance(descriptor, property)

def test_persistence::entityfeature_has_columnName():
    assert hasattr(persistence::EntityFeature, "columnName")
    descriptor = None
    for klass in persistence::EntityFeature.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)

def test_persistence::entityfeature_has_pluralisedName():
    assert hasattr(persistence::EntityFeature, "pluralisedName")
    descriptor = None
    for klass in persistence::EntityFeature.__mro__:
        if "pluralisedName" in klass.__dict__:
            descriptor = klass.__dict__["pluralisedName"]
            break
    assert isinstance(descriptor, property)

def test_persistence::entityfeature_has_primaryKey():
    assert hasattr(persistence::EntityFeature, "primaryKey")
    descriptor = None
    for klass in persistence::EntityFeature.__mro__:
        if "primaryKey" in klass.__dict__:
            descriptor = klass.__dict__["primaryKey"]
            break
    assert isinstance(descriptor, property)

def test_persistence::entityfeature_has_booleanIsHasChoice():
    assert hasattr(persistence::EntityFeature, "booleanIsHasChoice")
    descriptor = None
    for klass in persistence::EntityFeature.__mro__:
        if "booleanIsHasChoice" in klass.__dict__:
            descriptor = klass.__dict__["booleanIsHasChoice"]
            break
    assert isinstance(descriptor, property)

def test_persistence::entityfeature_has_derived():
    assert hasattr(persistence::EntityFeature, "derived")
    descriptor = None
    for klass in persistence::EntityFeature.__mro__:
        if "derived" in klass.__dict__:
            descriptor = klass.__dict__["derived"]
            break
    assert isinstance(descriptor, property)



def test_persistence::viewfeature_is_not_abstract():
    assert not inspect.isabstract(persistence::ViewFeature)


def test_persistence::viewfeature_constructor_exists():
    assert callable(persistence::ViewFeature.__init__)


def test_persistence::viewfeature_constructor_args():
    sig = inspect.signature(persistence::ViewFeature.__init__)
    params = list(sig.parameters.keys())



def test_persistence::attribute_is_not_abstract():
    assert not inspect.isabstract(persistence::Attribute)


def test_persistence::attribute_constructor_exists():
    assert callable(persistence::Attribute.__init__)


def test_persistence::attribute_constructor_args():
    sig = inspect.signature(persistence::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "validationPattern" in params, "Missing parameter 'validationPattern'"
    assert "inputClass" in params, "Missing parameter 'inputClass'"

def test_persistence::attribute_has_validationPattern():
    assert hasattr(persistence::Attribute, "validationPattern")
    descriptor = None
    for klass in persistence::Attribute.__mro__:
        if "validationPattern" in klass.__dict__:
            descriptor = klass.__dict__["validationPattern"]
            break
    assert isinstance(descriptor, property)

def test_persistence::attribute_has_inputClass():
    assert hasattr(persistence::Attribute, "inputClass")
    descriptor = None
    for klass in persistence::Attribute.__mro__:
        if "inputClass" in klass.__dict__:
            descriptor = klass.__dict__["inputClass"]
            break
    assert isinstance(descriptor, property)



def test_persistence::association_is_not_abstract():
    assert not inspect.isabstract(persistence::Association)


def test_persistence::association_constructor_exists():
    assert callable(persistence::Association.__init__)


def test_persistence::association_constructor_args():
    sig = inspect.signature(persistence::Association.__init__)
    params = list(sig.parameters.keys())
    assert "serializationMaxDepth" in params, "Missing parameter 'serializationMaxDepth'"
    assert "pseudo" in params, "Missing parameter 'pseudo'"
    assert "inputClass" in params, "Missing parameter 'inputClass'"

def test_persistence::association_has_serializationMaxDepth():
    assert hasattr(persistence::Association, "serializationMaxDepth")
    descriptor = None
    for klass in persistence::Association.__mro__:
        if "serializationMaxDepth" in klass.__dict__:
            descriptor = klass.__dict__["serializationMaxDepth"]
            break
    assert isinstance(descriptor, property)

def test_persistence::association_has_pseudo():
    assert hasattr(persistence::Association, "pseudo")
    descriptor = None
    for klass in persistence::Association.__mro__:
        if "pseudo" in klass.__dict__:
            descriptor = klass.__dict__["pseudo"]
            break
    assert isinstance(descriptor, property)

def test_persistence::association_has_inputClass():
    assert hasattr(persistence::Association, "inputClass")
    descriptor = None
    for klass in persistence::Association.__mro__:
        if "inputClass" in klass.__dict__:
            descriptor = klass.__dict__["inputClass"]
            break
    assert isinstance(descriptor, property)



def test_persistence::feature_is_not_abstract():
    assert not inspect.isabstract(persistence::Feature)


def test_persistence::feature_constructor_exists():
    assert callable(persistence::Feature.__init__)


def test_persistence::feature_constructor_args():
    sig = inspect.signature(persistence::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "footerClass" in params, "Missing parameter 'footerClass'"
    assert "nullDisplayValue" in params, "Missing parameter 'nullDisplayValue'"
    assert "encodeUriKey" in params, "Missing parameter 'encodeUriKey'"
    assert "title" in params, "Missing parameter 'title'"
    assert "collectionOrmAllowAdd" in params, "Missing parameter 'collectionOrmAllowAdd'"
    assert "displayClass" in params, "Missing parameter 'displayClass'"
    assert "placeholder" in params, "Missing parameter 'placeholder'"
    assert "headerClass" in params, "Missing parameter 'headerClass'"
    assert "collectionOrmAllowRemove" in params, "Missing parameter 'collectionOrmAllowRemove'"

def test_persistence::feature_has_footerClass():
    assert hasattr(persistence::Feature, "footerClass")
    descriptor = None
    for klass in persistence::Feature.__mro__:
        if "footerClass" in klass.__dict__:
            descriptor = klass.__dict__["footerClass"]
            break
    assert isinstance(descriptor, property)

def test_persistence::feature_has_nullDisplayValue():
    assert hasattr(persistence::Feature, "nullDisplayValue")
    descriptor = None
    for klass in persistence::Feature.__mro__:
        if "nullDisplayValue" in klass.__dict__:
            descriptor = klass.__dict__["nullDisplayValue"]
            break
    assert isinstance(descriptor, property)

def test_persistence::feature_has_encodeUriKey():
    assert hasattr(persistence::Feature, "encodeUriKey")
    descriptor = None
    for klass in persistence::Feature.__mro__:
        if "encodeUriKey" in klass.__dict__:
            descriptor = klass.__dict__["encodeUriKey"]
            break
    assert isinstance(descriptor, property)

def test_persistence::feature_has_title():
    assert hasattr(persistence::Feature, "title")
    descriptor = None
    for klass in persistence::Feature.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_persistence::feature_has_collectionOrmAllowAdd():
    assert hasattr(persistence::Feature, "collectionOrmAllowAdd")
    descriptor = None
    for klass in persistence::Feature.__mro__:
        if "collectionOrmAllowAdd" in klass.__dict__:
            descriptor = klass.__dict__["collectionOrmAllowAdd"]
            break
    assert isinstance(descriptor, property)

def test_persistence::feature_has_displayClass():
    assert hasattr(persistence::Feature, "displayClass")
    descriptor = None
    for klass in persistence::Feature.__mro__:
        if "displayClass" in klass.__dict__:
            descriptor = klass.__dict__["displayClass"]
            break
    assert isinstance(descriptor, property)

def test_persistence::feature_has_placeholder():
    assert hasattr(persistence::Feature, "placeholder")
    descriptor = None
    for klass in persistence::Feature.__mro__:
        if "placeholder" in klass.__dict__:
            descriptor = klass.__dict__["placeholder"]
            break
    assert isinstance(descriptor, property)

def test_persistence::feature_has_headerClass():
    assert hasattr(persistence::Feature, "headerClass")
    descriptor = None
    for klass in persistence::Feature.__mro__:
        if "headerClass" in klass.__dict__:
            descriptor = klass.__dict__["headerClass"]
            break
    assert isinstance(descriptor, property)

def test_persistence::feature_has_collectionOrmAllowRemove():
    assert hasattr(persistence::Feature, "collectionOrmAllowRemove")
    descriptor = None
    for klass in persistence::Feature.__mro__:
        if "collectionOrmAllowRemove" in klass.__dict__:
            descriptor = klass.__dict__["collectionOrmAllowRemove"]
            break
    assert isinstance(descriptor, property)



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_persistence::modellabel_is_not_abstract():
    assert not inspect.isabstract(persistence::ModelLabel)


def test_persistence::modellabel_constructor_exists():
    assert callable(persistence::ModelLabel.__init__)


def test_persistence::modellabel_constructor_args():
    sig = inspect.signature(persistence::ModelLabel.__init__)
    params = list(sig.parameters.keys())
    assert "format" in params, "Missing parameter 'format'"
    assert "customise" in params, "Missing parameter 'customise'"

def test_persistence::modellabel_has_format():
    assert hasattr(persistence::ModelLabel, "format")
    descriptor = None
    for klass in persistence::ModelLabel.__mro__:
        if "format" in klass.__dict__:
            descriptor = klass.__dict__["format"]
            break
    assert isinstance(descriptor, property)

def test_persistence::modellabel_has_customise():
    assert hasattr(persistence::ModelLabel, "customise")
    descriptor = None
    for klass in persistence::ModelLabel.__mro__:
        if "customise" in klass.__dict__:
            descriptor = klass.__dict__["customise"]
            break
    assert isinstance(descriptor, property)



def test_persistence::entityorview_is_not_abstract():
    assert not inspect.isabstract(persistence::EntityOrView)


def test_persistence::entityorview_constructor_exists():
    assert callable(persistence::EntityOrView.__init__)


def test_persistence::entityorview_constructor_args():
    sig = inspect.signature(persistence::EntityOrView.__init__)
    params = list(sig.parameters.keys())
    assert "autoKeyName" in params, "Missing parameter 'autoKeyName'"
    assert "implementsUserInterface" in params, "Missing parameter 'implementsUserInterface'"
    assert "tableName" in params, "Missing parameter 'tableName'"
    assert "pluralisedName" in params, "Missing parameter 'pluralisedName'"
    assert "autoKeyGenerationStrategy" in params, "Missing parameter 'autoKeyGenerationStrategy'"
    assert "autoKeyPersistentType" in params, "Missing parameter 'autoKeyPersistentType'"
    assert "allowFormTypeCustomisation" in params, "Missing parameter 'allowFormTypeCustomisation'"
    assert "singletonName" in params, "Missing parameter 'singletonName'"

def test_persistence::entityorview_has_autoKeyName():
    assert hasattr(persistence::EntityOrView, "autoKeyName")
    descriptor = None
    for klass in persistence::EntityOrView.__mro__:
        if "autoKeyName" in klass.__dict__:
            descriptor = klass.__dict__["autoKeyName"]
            break
    assert isinstance(descriptor, property)

def test_persistence::entityorview_has_implementsUserInterface():
    assert hasattr(persistence::EntityOrView, "implementsUserInterface")
    descriptor = None
    for klass in persistence::EntityOrView.__mro__:
        if "implementsUserInterface" in klass.__dict__:
            descriptor = klass.__dict__["implementsUserInterface"]
            break
    assert isinstance(descriptor, property)

def test_persistence::entityorview_has_tableName():
    assert hasattr(persistence::EntityOrView, "tableName")
    descriptor = None
    for klass in persistence::EntityOrView.__mro__:
        if "tableName" in klass.__dict__:
            descriptor = klass.__dict__["tableName"]
            break
    assert isinstance(descriptor, property)

def test_persistence::entityorview_has_pluralisedName():
    assert hasattr(persistence::EntityOrView, "pluralisedName")
    descriptor = None
    for klass in persistence::EntityOrView.__mro__:
        if "pluralisedName" in klass.__dict__:
            descriptor = klass.__dict__["pluralisedName"]
            break
    assert isinstance(descriptor, property)

def test_persistence::entityorview_has_autoKeyGenerationStrategy():
    assert hasattr(persistence::EntityOrView, "autoKeyGenerationStrategy")
    descriptor = None
    for klass in persistence::EntityOrView.__mro__:
        if "autoKeyGenerationStrategy" in klass.__dict__:
            descriptor = klass.__dict__["autoKeyGenerationStrategy"]
            break
    assert isinstance(descriptor, property)

def test_persistence::entityorview_has_autoKeyPersistentType():
    assert hasattr(persistence::EntityOrView, "autoKeyPersistentType")
    descriptor = None
    for klass in persistence::EntityOrView.__mro__:
        if "autoKeyPersistentType" in klass.__dict__:
            descriptor = klass.__dict__["autoKeyPersistentType"]
            break
    assert isinstance(descriptor, property)

def test_persistence::entityorview_has_allowFormTypeCustomisation():
    assert hasattr(persistence::EntityOrView, "allowFormTypeCustomisation")
    descriptor = None
    for klass in persistence::EntityOrView.__mro__:
        if "allowFormTypeCustomisation" in klass.__dict__:
            descriptor = klass.__dict__["allowFormTypeCustomisation"]
            break
    assert isinstance(descriptor, property)

def test_persistence::entityorview_has_singletonName():
    assert hasattr(persistence::EntityOrView, "singletonName")
    descriptor = None
    for klass in persistence::EntityOrView.__mro__:
        if "singletonName" in klass.__dict__:
            descriptor = klass.__dict__["singletonName"]
            break
    assert isinstance(descriptor, property)



def test_persistence::datatype_is_not_abstract():
    assert not inspect.isabstract(persistence::DataType)


def test_persistence::datatype_constructor_exists():
    assert callable(persistence::DataType.__init__)


def test_persistence::datatype_constructor_args():
    sig = inspect.signature(persistence::DataType.__init__)
    params = list(sig.parameters.keys())



def test_persistence::serializationgroup_is_not_abstract():
    assert not inspect.isabstract(persistence::SerializationGroup)


def test_persistence::serializationgroup_constructor_exists():
    assert callable(persistence::SerializationGroup.__init__)


def test_persistence::serializationgroup_constructor_args():
    sig = inspect.signature(persistence::SerializationGroup.__init__)
    params = list(sig.parameters.keys())



def test_persistence::persistence_is_not_abstract():
    assert not inspect.isabstract(persistence::Persistence)


def test_persistence::persistence_constructor_exists():
    assert callable(persistence::Persistence.__init__)


def test_persistence::persistence_constructor_args():
    sig = inspect.signature(persistence::Persistence.__init__)
    params = list(sig.parameters.keys())
    assert "timestampCreation" in params, "Missing parameter 'timestampCreation'"
    assert "databaseTechnology" in params, "Missing parameter 'databaseTechnology'"
    assert "timestampUpdates" in params, "Missing parameter 'timestampUpdates'"
    assert "ormTechnology" in params, "Missing parameter 'ormTechnology'"

def test_persistence::persistence_has_timestampCreation():
    assert hasattr(persistence::Persistence, "timestampCreation")
    descriptor = None
    for klass in persistence::Persistence.__mro__:
        if "timestampCreation" in klass.__dict__:
            descriptor = klass.__dict__["timestampCreation"]
            break
    assert isinstance(descriptor, property)

def test_persistence::persistence_has_databaseTechnology():
    assert hasattr(persistence::Persistence, "databaseTechnology")
    descriptor = None
    for klass in persistence::Persistence.__mro__:
        if "databaseTechnology" in klass.__dict__:
            descriptor = klass.__dict__["databaseTechnology"]
            break
    assert isinstance(descriptor, property)

def test_persistence::persistence_has_timestampUpdates():
    assert hasattr(persistence::Persistence, "timestampUpdates")
    descriptor = None
    for klass in persistence::Persistence.__mro__:
        if "timestampUpdates" in klass.__dict__:
            descriptor = klass.__dict__["timestampUpdates"]
            break
    assert isinstance(descriptor, property)

def test_persistence::persistence_has_ormTechnology():
    assert hasattr(persistence::Persistence, "ormTechnology")
    descriptor = None
    for klass in persistence::Persistence.__mro__:
        if "ormTechnology" in klass.__dict__:
            descriptor = klass.__dict__["ormTechnology"]
            break
    assert isinstance(descriptor, property)

def test_ormtechnologies_exists():
    # Check that the Enumeration exists
    assert OrmTechnologies is not None

def test_ormtechnologies_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OrmTechnologies]
    expected_literals = [
        "DoctrineORM",
        "Idiorm",
        "Kohana",
        "DoctrineODM",
        "DataMapper",
        "JPA",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OrmTechnologies"

def test_datedetails_exists():
    # Check that the Enumeration exists
    assert DateDetails is not None

def test_datedetails_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DateDetails]
    expected_literals = [
        "DateAndTime",
        "DateOnly",
        "TimeOnly",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DateDetails"

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

def test_cardinality_exists():
    # Check that the Enumeration exists
    assert Cardinality is not None

def test_cardinality_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Cardinality]
    expected_literals = [
        "Required",
        "Many",
        "Optional",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Cardinality"

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
EncapsulatedFeature_strategy = st.builds(
    EncapsulatedFeature,
)
ViewFeature_strategy = st.builds(
    ViewFeature,
)
persistence::EncapsulatedFeature_strategy = st.builds(
    persistence::EncapsulatedFeature,
    displayLabel=
        safe_text,
    alias=
        safe_text,
    columnName=
        safe_text
)
EntityAssociation_strategy = st.builds(
    EntityAssociation,
)
persistence::AssociationWithContainment_strategy = st.builds(
    persistence::AssociationWithContainment,
    sourceVisible=
        st.booleans()
)
persistence::AssociationWithoutContainment_strategy = st.builds(
    persistence::AssociationWithoutContainment,
    targetCardinality=
        safe_text,
    targetUnique=
        st.booleans()
)
persistence::AssociationKey_strategy = st.builds(
    persistence::AssociationKey,
)
Association_strategy = st.builds(
    Association,
)
ResourceAttribute_strategy = st.builds(
    ResourceAttribute,
)
persistence::ImageAttribute_strategy = st.builds(
    persistence::ImageAttribute,
)
persistence::FileAttribute_strategy = st.builds(
    persistence::FileAttribute,
)
PathElement_strategy = st.builds(
    PathElement,
)
persistence::DatePathElement_strategy = st.builds(
    persistence::DatePathElement,
    format=
        safe_text
)
persistence::StaticPathElement_strategy = st.builds(
    persistence::StaticPathElement,
    element=
        safe_text
)
persistence::PathElement_strategy = st.builds(
    persistence::PathElement,
)
EntityAttribute_strategy = st.builds(
    EntityAttribute,
)
persistence::LocationAttribute_strategy = st.builds(
    persistence::LocationAttribute,
)
persistence::ResourceAttribute_strategy = st.builds(
    persistence::ResourceAttribute,
    uploadsWithinWebsite=
        st.booleans(),
    validUploadExtensions=
        safe_text,
    validUploadMimeTypes=
        safe_text,
    maximumUploadSize=
        st.integers()
)
persistence::DateAttribute_strategy = st.builds(
    persistence::DateAttribute,
    details=
        safe_text,
    format=
        safe_text
)
persistence::UrlAttribute_strategy = st.builds(
    persistence::UrlAttribute,
    displayValue=
        safe_text
)
persistence::DataTypeAttribute_strategy = st.builds(
    persistence::DataTypeAttribute,
    caseInsensitive=
        st.booleans(),
    obfuscateFormFields=
        st.booleans(),
    encrypt=
        st.booleans()
)
Attribute_strategy = st.builds(
    Attribute,
)
persistence::EncapsulatedAttribute_strategy = st.builds(
    persistence::EncapsulatedAttribute,
    cardinality=
        safe_text,
    name=
        safe_text
)
EntityFeature_strategy = st.builds(
    EntityFeature,
)
persistence::EntityAttribute_strategy = st.builds(
    persistence::EntityAttribute,
    unique=
        st.booleans(),
    ormType=
        safe_text,
    hidden=
        st.booleans(),
    interfaceType=
        safe_text,
    persistentType=
        safe_text,
    containerUnique=
        st.booleans()
)
NamedDisplayElement_strategy = st.builds(
    NamedDisplayElement,
)
persistence::ViewAssociation_strategy = st.builds(
    persistence::ViewAssociation,
    cardinality=
        safe_text
)
EntityOrView_strategy = st.builds(
    EntityOrView,
)
persistence::View_strategy = st.builds(
    persistence::View,
)
persistence::Entity_strategy = st.builds(
    persistence::Entity,
)
persistence::EntityAssociation_strategy = st.builds(
    persistence::EntityAssociation,
    pivotTableName=
        safe_text,
    targetFeatureName=
        safe_text,
    targetColumnName=
        safe_text,
    targetFooterClass=
        safe_text,
    targetInputClass=
        safe_text,
    unique=
        st.booleans(),
    targetDisplayLabel=
        safe_text,
    targetPrimaryKey=
        st.booleans(),
    targetDisplayClass=
        safe_text,
    targetHeaderClass=
        safe_text,
    bidirectional=
        st.booleans()
)
ModelLabelFeature_strategy = st.builds(
    ModelLabelFeature,
)
persistence::ModelLabelAssociation_strategy = st.builds(
    persistence::ModelLabelAssociation,
    isSourceAssociation=
        st.booleans()
)
persistence::ModelLabelAttribute_strategy = st.builds(
    persistence::ModelLabelAttribute,
    dateFormat=
        safe_text
)
persistence::ModelLabelFeature_strategy = st.builds(
    persistence::ModelLabelFeature,
)
persistence::Label_strategy = st.builds(
    persistence::Label,
)
persistence::EncapsulatedAssociation_strategy = st.builds(
    persistence::EncapsulatedAssociation,
    name=
        safe_text,
    cardinality=
        safe_text,
    isSourceAssociation=
        st.booleans()
)
persistence::Expression_strategy = st.builds(
    persistence::Expression,
)
Label_strategy = st.builds(
    Label,
)
Feature_strategy = st.builds(
    Feature,
)
persistence::EntityFeature_strategy = st.builds(
    persistence::EntityFeature,
    customiseSet=
        st.booleans(),
    cardinality=
        safe_text,
    ordered=
        st.booleans(),
    singletonName=
        safe_text,
    columnName=
        safe_text,
    pluralisedName=
        safe_text,
    primaryKey=
        st.booleans(),
    booleanIsHasChoice=
        safe_text,
    derived=
        st.booleans()
)
persistence::ViewFeature_strategy = st.builds(
    persistence::ViewFeature,
)
persistence::Attribute_strategy = st.builds(
    persistence::Attribute,
    validationPattern=
        safe_text,
    inputClass=
        safe_text
)
persistence::Association_strategy = st.builds(
    persistence::Association,
    serializationMaxDepth=
        st.integers(),
    pseudo=
        st.booleans(),
    inputClass=
        safe_text
)
persistence::Feature_strategy = st.builds(
    persistence::Feature,
    footerClass=
        safe_text,
    nullDisplayValue=
        safe_text,
    encodeUriKey=
        st.booleans(),
    title=
        safe_text,
    collectionOrmAllowAdd=
        st.booleans(),
    displayClass=
        safe_text,
    placeholder=
        safe_text,
    headerClass=
        safe_text,
    collectionOrmAllowRemove=
        st.booleans()
)
Classifier_strategy = st.builds(
    Classifier,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
persistence::ModelLabel_strategy = st.builds(
    persistence::ModelLabel,
    format=
        safe_text,
    customise=
        st.booleans()
)
persistence::EntityOrView_strategy = st.builds(
    persistence::EntityOrView,
    autoKeyName=
        safe_text,
    implementsUserInterface=
        st.booleans(),
    tableName=
        safe_text,
    pluralisedName=
        safe_text,
    autoKeyGenerationStrategy=
        safe_text,
    autoKeyPersistentType=
        safe_text,
    allowFormTypeCustomisation=
        st.booleans(),
    singletonName=
        safe_text
)
persistence::DataType_strategy = st.builds(
    persistence::DataType,
)
persistence::SerializationGroup_strategy = st.builds(
    persistence::SerializationGroup,
)
persistence::Persistence_strategy = st.builds(
    persistence::Persistence,
    timestampCreation=
        st.booleans(),
    databaseTechnology=
        safe_text,
    timestampUpdates=
        st.booleans(),
    ormTechnology=
        safe_text
)

@given(instance=EncapsulatedFeature_strategy)
@settings(max_examples=50)
def test_encapsulatedfeature_instantiation(instance):
    assert isinstance(instance, EncapsulatedFeature)

@given(instance=ViewFeature_strategy)
@settings(max_examples=50)
def test_viewfeature_instantiation(instance):
    assert isinstance(instance, ViewFeature)

@given(instance=persistence::EncapsulatedFeature_strategy)
@settings(max_examples=50)
def test_persistence::encapsulatedfeature_instantiation(instance):
    assert isinstance(instance, persistence::EncapsulatedFeature)

@given(instance=persistence::EncapsulatedFeature_strategy)
def test_persistence::encapsulatedfeature_displayLabel_type(instance):
    assert isinstance(instance.displayLabel, str)


@given(instance=persistence::EncapsulatedFeature_strategy)
def test_persistence::encapsulatedfeature_displayLabel_setter(instance):
    original = instance.displayLabel
    instance.displayLabel = original
    assert instance.displayLabel == original

@given(instance=persistence::EncapsulatedFeature_strategy)
def test_persistence::encapsulatedfeature_alias_type(instance):
    assert isinstance(instance.alias, str)


@given(instance=persistence::EncapsulatedFeature_strategy)
def test_persistence::encapsulatedfeature_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=persistence::EncapsulatedFeature_strategy)
def test_persistence::encapsulatedfeature_columnName_type(instance):
    assert isinstance(instance.columnName, str)


@given(instance=persistence::EncapsulatedFeature_strategy)
def test_persistence::encapsulatedfeature_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original

@given(instance=EntityAssociation_strategy)
@settings(max_examples=50)
def test_entityassociation_instantiation(instance):
    assert isinstance(instance, EntityAssociation)

@given(instance=persistence::AssociationWithContainment_strategy)
@settings(max_examples=50)
def test_persistence::associationwithcontainment_instantiation(instance):
    assert isinstance(instance, persistence::AssociationWithContainment)

@given(instance=persistence::AssociationWithContainment_strategy)
def test_persistence::associationwithcontainment_sourceVisible_type(instance):
    assert isinstance(instance.sourceVisible, bool)


@given(instance=persistence::AssociationWithContainment_strategy)
def test_persistence::associationwithcontainment_sourceVisible_setter(instance):
    original = instance.sourceVisible
    instance.sourceVisible = original
    assert instance.sourceVisible == original

@given(instance=persistence::AssociationWithoutContainment_strategy)
@settings(max_examples=50)
def test_persistence::associationwithoutcontainment_instantiation(instance):
    assert isinstance(instance, persistence::AssociationWithoutContainment)

@given(instance=persistence::AssociationWithoutContainment_strategy)
def test_persistence::associationwithoutcontainment_targetCardinality_type(instance):
    assert isinstance(instance.targetCardinality, str)


@given(instance=persistence::AssociationWithoutContainment_strategy)
def test_persistence::associationwithoutcontainment_targetCardinality_setter(instance):
    original = instance.targetCardinality
    instance.targetCardinality = original
    assert instance.targetCardinality == original

@given(instance=persistence::AssociationWithoutContainment_strategy)
def test_persistence::associationwithoutcontainment_targetUnique_type(instance):
    assert isinstance(instance.targetUnique, bool)


@given(instance=persistence::AssociationWithoutContainment_strategy)
def test_persistence::associationwithoutcontainment_targetUnique_setter(instance):
    original = instance.targetUnique
    instance.targetUnique = original
    assert instance.targetUnique == original

@given(instance=persistence::AssociationKey_strategy)
@settings(max_examples=50)
def test_persistence::associationkey_instantiation(instance):
    assert isinstance(instance, persistence::AssociationKey)

@given(instance=Association_strategy)
@settings(max_examples=50)
def test_association_instantiation(instance):
    assert isinstance(instance, Association)

@given(instance=ResourceAttribute_strategy)
@settings(max_examples=50)
def test_resourceattribute_instantiation(instance):
    assert isinstance(instance, ResourceAttribute)

@given(instance=persistence::ImageAttribute_strategy)
@settings(max_examples=50)
def test_persistence::imageattribute_instantiation(instance):
    assert isinstance(instance, persistence::ImageAttribute)

@given(instance=persistence::FileAttribute_strategy)
@settings(max_examples=50)
def test_persistence::fileattribute_instantiation(instance):
    assert isinstance(instance, persistence::FileAttribute)

@given(instance=PathElement_strategy)
@settings(max_examples=50)
def test_pathelement_instantiation(instance):
    assert isinstance(instance, PathElement)

@given(instance=persistence::DatePathElement_strategy)
@settings(max_examples=50)
def test_persistence::datepathelement_instantiation(instance):
    assert isinstance(instance, persistence::DatePathElement)

@given(instance=persistence::DatePathElement_strategy)
def test_persistence::datepathelement_format_type(instance):
    assert isinstance(instance.format, str)


@given(instance=persistence::DatePathElement_strategy)
def test_persistence::datepathelement_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original

@given(instance=persistence::StaticPathElement_strategy)
@settings(max_examples=50)
def test_persistence::staticpathelement_instantiation(instance):
    assert isinstance(instance, persistence::StaticPathElement)

@given(instance=persistence::StaticPathElement_strategy)
def test_persistence::staticpathelement_element_type(instance):
    assert isinstance(instance.element, str)


@given(instance=persistence::StaticPathElement_strategy)
def test_persistence::staticpathelement_element_setter(instance):
    original = instance.element
    instance.element = original
    assert instance.element == original

@given(instance=persistence::PathElement_strategy)
@settings(max_examples=50)
def test_persistence::pathelement_instantiation(instance):
    assert isinstance(instance, persistence::PathElement)

@given(instance=EntityAttribute_strategy)
@settings(max_examples=50)
def test_entityattribute_instantiation(instance):
    assert isinstance(instance, EntityAttribute)

@given(instance=persistence::LocationAttribute_strategy)
@settings(max_examples=50)
def test_persistence::locationattribute_instantiation(instance):
    assert isinstance(instance, persistence::LocationAttribute)

@given(instance=persistence::ResourceAttribute_strategy)
@settings(max_examples=50)
def test_persistence::resourceattribute_instantiation(instance):
    assert isinstance(instance, persistence::ResourceAttribute)

@given(instance=persistence::ResourceAttribute_strategy)
def test_persistence::resourceattribute_uploadsWithinWebsite_type(instance):
    assert isinstance(instance.uploadsWithinWebsite, bool)


@given(instance=persistence::ResourceAttribute_strategy)
def test_persistence::resourceattribute_uploadsWithinWebsite_setter(instance):
    original = instance.uploadsWithinWebsite
    instance.uploadsWithinWebsite = original
    assert instance.uploadsWithinWebsite == original

@given(instance=persistence::ResourceAttribute_strategy)
def test_persistence::resourceattribute_validUploadExtensions_type(instance):
    assert isinstance(instance.validUploadExtensions, str)


@given(instance=persistence::ResourceAttribute_strategy)
def test_persistence::resourceattribute_validUploadExtensions_setter(instance):
    original = instance.validUploadExtensions
    instance.validUploadExtensions = original
    assert instance.validUploadExtensions == original

@given(instance=persistence::ResourceAttribute_strategy)
def test_persistence::resourceattribute_validUploadMimeTypes_type(instance):
    assert isinstance(instance.validUploadMimeTypes, str)


@given(instance=persistence::ResourceAttribute_strategy)
def test_persistence::resourceattribute_validUploadMimeTypes_setter(instance):
    original = instance.validUploadMimeTypes
    instance.validUploadMimeTypes = original
    assert instance.validUploadMimeTypes == original

@given(instance=persistence::ResourceAttribute_strategy)
def test_persistence::resourceattribute_maximumUploadSize_type(instance):
    assert isinstance(instance.maximumUploadSize, int)


@given(instance=persistence::ResourceAttribute_strategy)
def test_persistence::resourceattribute_maximumUploadSize_setter(instance):
    original = instance.maximumUploadSize
    instance.maximumUploadSize = original
    assert instance.maximumUploadSize == original

@given(instance=persistence::DateAttribute_strategy)
@settings(max_examples=50)
def test_persistence::dateattribute_instantiation(instance):
    assert isinstance(instance, persistence::DateAttribute)

@given(instance=persistence::DateAttribute_strategy)
def test_persistence::dateattribute_details_type(instance):
    assert isinstance(instance.details, str)


@given(instance=persistence::DateAttribute_strategy)
def test_persistence::dateattribute_details_setter(instance):
    original = instance.details
    instance.details = original
    assert instance.details == original

@given(instance=persistence::DateAttribute_strategy)
def test_persistence::dateattribute_format_type(instance):
    assert isinstance(instance.format, str)


@given(instance=persistence::DateAttribute_strategy)
def test_persistence::dateattribute_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original

@given(instance=persistence::UrlAttribute_strategy)
@settings(max_examples=50)
def test_persistence::urlattribute_instantiation(instance):
    assert isinstance(instance, persistence::UrlAttribute)

@given(instance=persistence::UrlAttribute_strategy)
def test_persistence::urlattribute_displayValue_type(instance):
    assert isinstance(instance.displayValue, str)


@given(instance=persistence::UrlAttribute_strategy)
def test_persistence::urlattribute_displayValue_setter(instance):
    original = instance.displayValue
    instance.displayValue = original
    assert instance.displayValue == original

@given(instance=persistence::DataTypeAttribute_strategy)
@settings(max_examples=50)
def test_persistence::datatypeattribute_instantiation(instance):
    assert isinstance(instance, persistence::DataTypeAttribute)

@given(instance=persistence::DataTypeAttribute_strategy)
def test_persistence::datatypeattribute_caseInsensitive_type(instance):
    assert isinstance(instance.caseInsensitive, bool)


@given(instance=persistence::DataTypeAttribute_strategy)
def test_persistence::datatypeattribute_caseInsensitive_setter(instance):
    original = instance.caseInsensitive
    instance.caseInsensitive = original
    assert instance.caseInsensitive == original

@given(instance=persistence::DataTypeAttribute_strategy)
def test_persistence::datatypeattribute_obfuscateFormFields_type(instance):
    assert isinstance(instance.obfuscateFormFields, bool)


@given(instance=persistence::DataTypeAttribute_strategy)
def test_persistence::datatypeattribute_obfuscateFormFields_setter(instance):
    original = instance.obfuscateFormFields
    instance.obfuscateFormFields = original
    assert instance.obfuscateFormFields == original

@given(instance=persistence::DataTypeAttribute_strategy)
def test_persistence::datatypeattribute_encrypt_type(instance):
    assert isinstance(instance.encrypt, bool)


@given(instance=persistence::DataTypeAttribute_strategy)
def test_persistence::datatypeattribute_encrypt_setter(instance):
    original = instance.encrypt
    instance.encrypt = original
    assert instance.encrypt == original

@given(instance=Attribute_strategy)
@settings(max_examples=50)
def test_attribute_instantiation(instance):
    assert isinstance(instance, Attribute)

@given(instance=persistence::EncapsulatedAttribute_strategy)
@settings(max_examples=50)
def test_persistence::encapsulatedattribute_instantiation(instance):
    assert isinstance(instance, persistence::EncapsulatedAttribute)

@given(instance=persistence::EncapsulatedAttribute_strategy)
def test_persistence::encapsulatedattribute_cardinality_type(instance):
    assert isinstance(instance.cardinality, str)


@given(instance=persistence::EncapsulatedAttribute_strategy)
def test_persistence::encapsulatedattribute_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original

@given(instance=persistence::EncapsulatedAttribute_strategy)
def test_persistence::encapsulatedattribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=persistence::EncapsulatedAttribute_strategy)
def test_persistence::encapsulatedattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=EntityFeature_strategy)
@settings(max_examples=50)
def test_entityfeature_instantiation(instance):
    assert isinstance(instance, EntityFeature)

@given(instance=persistence::EntityAttribute_strategy)
@settings(max_examples=50)
def test_persistence::entityattribute_instantiation(instance):
    assert isinstance(instance, persistence::EntityAttribute)

@given(instance=persistence::EntityAttribute_strategy)
def test_persistence::entityattribute_unique_type(instance):
    assert isinstance(instance.unique, bool)


@given(instance=persistence::EntityAttribute_strategy)
def test_persistence::entityattribute_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original

@given(instance=persistence::EntityAttribute_strategy)
def test_persistence::entityattribute_ormType_type(instance):
    assert isinstance(instance.ormType, str)


@given(instance=persistence::EntityAttribute_strategy)
def test_persistence::entityattribute_ormType_setter(instance):
    original = instance.ormType
    instance.ormType = original
    assert instance.ormType == original

@given(instance=persistence::EntityAttribute_strategy)
def test_persistence::entityattribute_hidden_type(instance):
    assert isinstance(instance.hidden, bool)


@given(instance=persistence::EntityAttribute_strategy)
def test_persistence::entityattribute_hidden_setter(instance):
    original = instance.hidden
    instance.hidden = original
    assert instance.hidden == original

@given(instance=persistence::EntityAttribute_strategy)
def test_persistence::entityattribute_interfaceType_type(instance):
    assert isinstance(instance.interfaceType, str)


@given(instance=persistence::EntityAttribute_strategy)
def test_persistence::entityattribute_interfaceType_setter(instance):
    original = instance.interfaceType
    instance.interfaceType = original
    assert instance.interfaceType == original

@given(instance=persistence::EntityAttribute_strategy)
def test_persistence::entityattribute_persistentType_type(instance):
    assert isinstance(instance.persistentType, str)


@given(instance=persistence::EntityAttribute_strategy)
def test_persistence::entityattribute_persistentType_setter(instance):
    original = instance.persistentType
    instance.persistentType = original
    assert instance.persistentType == original

@given(instance=persistence::EntityAttribute_strategy)
def test_persistence::entityattribute_containerUnique_type(instance):
    assert isinstance(instance.containerUnique, bool)


@given(instance=persistence::EntityAttribute_strategy)
def test_persistence::entityattribute_containerUnique_setter(instance):
    original = instance.containerUnique
    instance.containerUnique = original
    assert instance.containerUnique == original

@given(instance=NamedDisplayElement_strategy)
@settings(max_examples=50)
def test_nameddisplayelement_instantiation(instance):
    assert isinstance(instance, NamedDisplayElement)

@given(instance=persistence::ViewAssociation_strategy)
@settings(max_examples=50)
def test_persistence::viewassociation_instantiation(instance):
    assert isinstance(instance, persistence::ViewAssociation)

@given(instance=persistence::ViewAssociation_strategy)
def test_persistence::viewassociation_cardinality_type(instance):
    assert isinstance(instance.cardinality, str)


@given(instance=persistence::ViewAssociation_strategy)
def test_persistence::viewassociation_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original

@given(instance=EntityOrView_strategy)
@settings(max_examples=50)
def test_entityorview_instantiation(instance):
    assert isinstance(instance, EntityOrView)

@given(instance=persistence::View_strategy)
@settings(max_examples=50)
def test_persistence::view_instantiation(instance):
    assert isinstance(instance, persistence::View)

@given(instance=persistence::Entity_strategy)
@settings(max_examples=50)
def test_persistence::entity_instantiation(instance):
    assert isinstance(instance, persistence::Entity)

@given(instance=persistence::EntityAssociation_strategy)
@settings(max_examples=50)
def test_persistence::entityassociation_instantiation(instance):
    assert isinstance(instance, persistence::EntityAssociation)

@given(instance=persistence::EntityAssociation_strategy)
def test_persistence::entityassociation_pivotTableName_type(instance):
    assert isinstance(instance.pivotTableName, str)


@given(instance=persistence::EntityAssociation_strategy)
def test_persistence::entityassociation_pivotTableName_setter(instance):
    original = instance.pivotTableName
    instance.pivotTableName = original
    assert instance.pivotTableName == original

@given(instance=persistence::EntityAssociation_strategy)
def test_persistence::entityassociation_targetFeatureName_type(instance):
    assert isinstance(instance.targetFeatureName, str)


@given(instance=persistence::EntityAssociation_strategy)
def test_persistence::entityassociation_targetFeatureName_setter(instance):
    original = instance.targetFeatureName
    instance.targetFeatureName = original
    assert instance.targetFeatureName == original

@given(instance=persistence::EntityAssociation_strategy)
def test_persistence::entityassociation_targetColumnName_type(instance):
    assert isinstance(instance.targetColumnName, str)


@given(instance=persistence::EntityAssociation_strategy)
def test_persistence::entityassociation_targetColumnName_setter(instance):
    original = instance.targetColumnName
    instance.targetColumnName = original
    assert instance.targetColumnName == original

@given(instance=persistence::EntityAssociation_strategy)
def test_persistence::entityassociation_targetFooterClass_type(instance):
    assert isinstance(instance.targetFooterClass, str)


@given(instance=persistence::EntityAssociation_strategy)
def test_persistence::entityassociation_targetFooterClass_setter(instance):
    original = instance.targetFooterClass
    instance.targetFooterClass = original
    assert instance.targetFooterClass == original

@given(instance=persistence::EntityAssociation_strategy)
def test_persistence::entityassociation_targetInputClass_type(instance):
    assert isinstance(instance.targetInputClass, str)


@given(instance=persistence::EntityAssociation_strategy)
def test_persistence::entityassociation_targetInputClass_setter(instance):
    original = instance.targetInputClass
    instance.targetInputClass = original
    assert instance.targetInputClass == original

@given(instance=persistence::EntityAssociation_strategy)
def test_persistence::entityassociation_unique_type(instance):
    assert isinstance(instance.unique, bool)


@given(instance=persistence::EntityAssociation_strategy)
def test_persistence::entityassociation_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original

@given(instance=persistence::EntityAssociation_strategy)
def test_persistence::entityassociation_targetDisplayLabel_type(instance):
    assert isinstance(instance.targetDisplayLabel, str)


@given(instance=persistence::EntityAssociation_strategy)
def test_persistence::entityassociation_targetDisplayLabel_setter(instance):
    original = instance.targetDisplayLabel
    instance.targetDisplayLabel = original
    assert instance.targetDisplayLabel == original

@given(instance=persistence::EntityAssociation_strategy)
def test_persistence::entityassociation_targetPrimaryKey_type(instance):
    assert isinstance(instance.targetPrimaryKey, bool)


@given(instance=persistence::EntityAssociation_strategy)
def test_persistence::entityassociation_targetPrimaryKey_setter(instance):
    original = instance.targetPrimaryKey
    instance.targetPrimaryKey = original
    assert instance.targetPrimaryKey == original

@given(instance=persistence::EntityAssociation_strategy)
def test_persistence::entityassociation_targetDisplayClass_type(instance):
    assert isinstance(instance.targetDisplayClass, str)


@given(instance=persistence::EntityAssociation_strategy)
def test_persistence::entityassociation_targetDisplayClass_setter(instance):
    original = instance.targetDisplayClass
    instance.targetDisplayClass = original
    assert instance.targetDisplayClass == original

@given(instance=persistence::EntityAssociation_strategy)
def test_persistence::entityassociation_targetHeaderClass_type(instance):
    assert isinstance(instance.targetHeaderClass, str)


@given(instance=persistence::EntityAssociation_strategy)
def test_persistence::entityassociation_targetHeaderClass_setter(instance):
    original = instance.targetHeaderClass
    instance.targetHeaderClass = original
    assert instance.targetHeaderClass == original

@given(instance=persistence::EntityAssociation_strategy)
def test_persistence::entityassociation_bidirectional_type(instance):
    assert isinstance(instance.bidirectional, bool)


@given(instance=persistence::EntityAssociation_strategy)
def test_persistence::entityassociation_bidirectional_setter(instance):
    original = instance.bidirectional
    instance.bidirectional = original
    assert instance.bidirectional == original

@given(instance=ModelLabelFeature_strategy)
@settings(max_examples=50)
def test_modellabelfeature_instantiation(instance):
    assert isinstance(instance, ModelLabelFeature)

@given(instance=persistence::ModelLabelAssociation_strategy)
@settings(max_examples=50)
def test_persistence::modellabelassociation_instantiation(instance):
    assert isinstance(instance, persistence::ModelLabelAssociation)

@given(instance=persistence::ModelLabelAssociation_strategy)
def test_persistence::modellabelassociation_isSourceAssociation_type(instance):
    assert isinstance(instance.isSourceAssociation, bool)


@given(instance=persistence::ModelLabelAssociation_strategy)
def test_persistence::modellabelassociation_isSourceAssociation_setter(instance):
    original = instance.isSourceAssociation
    instance.isSourceAssociation = original
    assert instance.isSourceAssociation == original

@given(instance=persistence::ModelLabelAttribute_strategy)
@settings(max_examples=50)
def test_persistence::modellabelattribute_instantiation(instance):
    assert isinstance(instance, persistence::ModelLabelAttribute)

@given(instance=persistence::ModelLabelAttribute_strategy)
def test_persistence::modellabelattribute_dateFormat_type(instance):
    assert isinstance(instance.dateFormat, str)


@given(instance=persistence::ModelLabelAttribute_strategy)
def test_persistence::modellabelattribute_dateFormat_setter(instance):
    original = instance.dateFormat
    instance.dateFormat = original
    assert instance.dateFormat == original

@given(instance=persistence::ModelLabelFeature_strategy)
@settings(max_examples=50)
def test_persistence::modellabelfeature_instantiation(instance):
    assert isinstance(instance, persistence::ModelLabelFeature)

@given(instance=persistence::Label_strategy)
@settings(max_examples=50)
def test_persistence::label_instantiation(instance):
    assert isinstance(instance, persistence::Label)

@given(instance=persistence::EncapsulatedAssociation_strategy)
@settings(max_examples=50)
def test_persistence::encapsulatedassociation_instantiation(instance):
    assert isinstance(instance, persistence::EncapsulatedAssociation)

@given(instance=persistence::EncapsulatedAssociation_strategy)
def test_persistence::encapsulatedassociation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=persistence::EncapsulatedAssociation_strategy)
def test_persistence::encapsulatedassociation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=persistence::EncapsulatedAssociation_strategy)
def test_persistence::encapsulatedassociation_cardinality_type(instance):
    assert isinstance(instance.cardinality, str)


@given(instance=persistence::EncapsulatedAssociation_strategy)
def test_persistence::encapsulatedassociation_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original

@given(instance=persistence::EncapsulatedAssociation_strategy)
def test_persistence::encapsulatedassociation_isSourceAssociation_type(instance):
    assert isinstance(instance.isSourceAssociation, bool)


@given(instance=persistence::EncapsulatedAssociation_strategy)
def test_persistence::encapsulatedassociation_isSourceAssociation_setter(instance):
    original = instance.isSourceAssociation
    instance.isSourceAssociation = original
    assert instance.isSourceAssociation == original

@given(instance=persistence::Expression_strategy)
@settings(max_examples=50)
def test_persistence::expression_instantiation(instance):
    assert isinstance(instance, persistence::Expression)

@given(instance=Label_strategy)
@settings(max_examples=50)
def test_label_instantiation(instance):
    assert isinstance(instance, Label)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=persistence::EntityFeature_strategy)
@settings(max_examples=50)
def test_persistence::entityfeature_instantiation(instance):
    assert isinstance(instance, persistence::EntityFeature)

@given(instance=persistence::EntityFeature_strategy)
def test_persistence::entityfeature_customiseSet_type(instance):
    assert isinstance(instance.customiseSet, bool)


@given(instance=persistence::EntityFeature_strategy)
def test_persistence::entityfeature_customiseSet_setter(instance):
    original = instance.customiseSet
    instance.customiseSet = original
    assert instance.customiseSet == original

@given(instance=persistence::EntityFeature_strategy)
def test_persistence::entityfeature_cardinality_type(instance):
    assert isinstance(instance.cardinality, str)


@given(instance=persistence::EntityFeature_strategy)
def test_persistence::entityfeature_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original

@given(instance=persistence::EntityFeature_strategy)
def test_persistence::entityfeature_ordered_type(instance):
    assert isinstance(instance.ordered, bool)


@given(instance=persistence::EntityFeature_strategy)
def test_persistence::entityfeature_ordered_setter(instance):
    original = instance.ordered
    instance.ordered = original
    assert instance.ordered == original

@given(instance=persistence::EntityFeature_strategy)
def test_persistence::entityfeature_singletonName_type(instance):
    assert isinstance(instance.singletonName, str)


@given(instance=persistence::EntityFeature_strategy)
def test_persistence::entityfeature_singletonName_setter(instance):
    original = instance.singletonName
    instance.singletonName = original
    assert instance.singletonName == original

@given(instance=persistence::EntityFeature_strategy)
def test_persistence::entityfeature_columnName_type(instance):
    assert isinstance(instance.columnName, str)


@given(instance=persistence::EntityFeature_strategy)
def test_persistence::entityfeature_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original

@given(instance=persistence::EntityFeature_strategy)
def test_persistence::entityfeature_pluralisedName_type(instance):
    assert isinstance(instance.pluralisedName, str)


@given(instance=persistence::EntityFeature_strategy)
def test_persistence::entityfeature_pluralisedName_setter(instance):
    original = instance.pluralisedName
    instance.pluralisedName = original
    assert instance.pluralisedName == original

@given(instance=persistence::EntityFeature_strategy)
def test_persistence::entityfeature_primaryKey_type(instance):
    assert isinstance(instance.primaryKey, bool)


@given(instance=persistence::EntityFeature_strategy)
def test_persistence::entityfeature_primaryKey_setter(instance):
    original = instance.primaryKey
    instance.primaryKey = original
    assert instance.primaryKey == original

@given(instance=persistence::EntityFeature_strategy)
def test_persistence::entityfeature_booleanIsHasChoice_type(instance):
    assert isinstance(instance.booleanIsHasChoice, str)


@given(instance=persistence::EntityFeature_strategy)
def test_persistence::entityfeature_booleanIsHasChoice_setter(instance):
    original = instance.booleanIsHasChoice
    instance.booleanIsHasChoice = original
    assert instance.booleanIsHasChoice == original

@given(instance=persistence::EntityFeature_strategy)
def test_persistence::entityfeature_derived_type(instance):
    assert isinstance(instance.derived, bool)


@given(instance=persistence::EntityFeature_strategy)
def test_persistence::entityfeature_derived_setter(instance):
    original = instance.derived
    instance.derived = original
    assert instance.derived == original

@given(instance=persistence::ViewFeature_strategy)
@settings(max_examples=50)
def test_persistence::viewfeature_instantiation(instance):
    assert isinstance(instance, persistence::ViewFeature)

@given(instance=persistence::Attribute_strategy)
@settings(max_examples=50)
def test_persistence::attribute_instantiation(instance):
    assert isinstance(instance, persistence::Attribute)

@given(instance=persistence::Attribute_strategy)
def test_persistence::attribute_validationPattern_type(instance):
    assert isinstance(instance.validationPattern, str)


@given(instance=persistence::Attribute_strategy)
def test_persistence::attribute_validationPattern_setter(instance):
    original = instance.validationPattern
    instance.validationPattern = original
    assert instance.validationPattern == original

@given(instance=persistence::Attribute_strategy)
def test_persistence::attribute_inputClass_type(instance):
    assert isinstance(instance.inputClass, str)


@given(instance=persistence::Attribute_strategy)
def test_persistence::attribute_inputClass_setter(instance):
    original = instance.inputClass
    instance.inputClass = original
    assert instance.inputClass == original

@given(instance=persistence::Association_strategy)
@settings(max_examples=50)
def test_persistence::association_instantiation(instance):
    assert isinstance(instance, persistence::Association)

@given(instance=persistence::Association_strategy)
def test_persistence::association_serializationMaxDepth_type(instance):
    assert isinstance(instance.serializationMaxDepth, int)


@given(instance=persistence::Association_strategy)
def test_persistence::association_serializationMaxDepth_setter(instance):
    original = instance.serializationMaxDepth
    instance.serializationMaxDepth = original
    assert instance.serializationMaxDepth == original

@given(instance=persistence::Association_strategy)
def test_persistence::association_pseudo_type(instance):
    assert isinstance(instance.pseudo, bool)


@given(instance=persistence::Association_strategy)
def test_persistence::association_pseudo_setter(instance):
    original = instance.pseudo
    instance.pseudo = original
    assert instance.pseudo == original

@given(instance=persistence::Association_strategy)
def test_persistence::association_inputClass_type(instance):
    assert isinstance(instance.inputClass, str)


@given(instance=persistence::Association_strategy)
def test_persistence::association_inputClass_setter(instance):
    original = instance.inputClass
    instance.inputClass = original
    assert instance.inputClass == original

@given(instance=persistence::Feature_strategy)
@settings(max_examples=50)
def test_persistence::feature_instantiation(instance):
    assert isinstance(instance, persistence::Feature)

@given(instance=persistence::Feature_strategy)
def test_persistence::feature_footerClass_type(instance):
    assert isinstance(instance.footerClass, str)


@given(instance=persistence::Feature_strategy)
def test_persistence::feature_footerClass_setter(instance):
    original = instance.footerClass
    instance.footerClass = original
    assert instance.footerClass == original

@given(instance=persistence::Feature_strategy)
def test_persistence::feature_nullDisplayValue_type(instance):
    assert isinstance(instance.nullDisplayValue, str)


@given(instance=persistence::Feature_strategy)
def test_persistence::feature_nullDisplayValue_setter(instance):
    original = instance.nullDisplayValue
    instance.nullDisplayValue = original
    assert instance.nullDisplayValue == original

@given(instance=persistence::Feature_strategy)
def test_persistence::feature_encodeUriKey_type(instance):
    assert isinstance(instance.encodeUriKey, bool)


@given(instance=persistence::Feature_strategy)
def test_persistence::feature_encodeUriKey_setter(instance):
    original = instance.encodeUriKey
    instance.encodeUriKey = original
    assert instance.encodeUriKey == original

@given(instance=persistence::Feature_strategy)
def test_persistence::feature_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=persistence::Feature_strategy)
def test_persistence::feature_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=persistence::Feature_strategy)
def test_persistence::feature_collectionOrmAllowAdd_type(instance):
    assert isinstance(instance.collectionOrmAllowAdd, bool)


@given(instance=persistence::Feature_strategy)
def test_persistence::feature_collectionOrmAllowAdd_setter(instance):
    original = instance.collectionOrmAllowAdd
    instance.collectionOrmAllowAdd = original
    assert instance.collectionOrmAllowAdd == original

@given(instance=persistence::Feature_strategy)
def test_persistence::feature_displayClass_type(instance):
    assert isinstance(instance.displayClass, str)


@given(instance=persistence::Feature_strategy)
def test_persistence::feature_displayClass_setter(instance):
    original = instance.displayClass
    instance.displayClass = original
    assert instance.displayClass == original

@given(instance=persistence::Feature_strategy)
def test_persistence::feature_placeholder_type(instance):
    assert isinstance(instance.placeholder, str)


@given(instance=persistence::Feature_strategy)
def test_persistence::feature_placeholder_setter(instance):
    original = instance.placeholder
    instance.placeholder = original
    assert instance.placeholder == original

@given(instance=persistence::Feature_strategy)
def test_persistence::feature_headerClass_type(instance):
    assert isinstance(instance.headerClass, str)


@given(instance=persistence::Feature_strategy)
def test_persistence::feature_headerClass_setter(instance):
    original = instance.headerClass
    instance.headerClass = original
    assert instance.headerClass == original

@given(instance=persistence::Feature_strategy)
def test_persistence::feature_collectionOrmAllowRemove_type(instance):
    assert isinstance(instance.collectionOrmAllowRemove, bool)


@given(instance=persistence::Feature_strategy)
def test_persistence::feature_collectionOrmAllowRemove_setter(instance):
    original = instance.collectionOrmAllowRemove
    instance.collectionOrmAllowRemove = original
    assert instance.collectionOrmAllowRemove == original

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=persistence::ModelLabel_strategy)
@settings(max_examples=50)
def test_persistence::modellabel_instantiation(instance):
    assert isinstance(instance, persistence::ModelLabel)

@given(instance=persistence::ModelLabel_strategy)
def test_persistence::modellabel_format_type(instance):
    assert isinstance(instance.format, str)


@given(instance=persistence::ModelLabel_strategy)
def test_persistence::modellabel_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original

@given(instance=persistence::ModelLabel_strategy)
def test_persistence::modellabel_customise_type(instance):
    assert isinstance(instance.customise, bool)


@given(instance=persistence::ModelLabel_strategy)
def test_persistence::modellabel_customise_setter(instance):
    original = instance.customise
    instance.customise = original
    assert instance.customise == original

@given(instance=persistence::EntityOrView_strategy)
@settings(max_examples=50)
def test_persistence::entityorview_instantiation(instance):
    assert isinstance(instance, persistence::EntityOrView)

@given(instance=persistence::EntityOrView_strategy)
def test_persistence::entityorview_autoKeyName_type(instance):
    assert isinstance(instance.autoKeyName, str)


@given(instance=persistence::EntityOrView_strategy)
def test_persistence::entityorview_autoKeyName_setter(instance):
    original = instance.autoKeyName
    instance.autoKeyName = original
    assert instance.autoKeyName == original

@given(instance=persistence::EntityOrView_strategy)
def test_persistence::entityorview_implementsUserInterface_type(instance):
    assert isinstance(instance.implementsUserInterface, bool)


@given(instance=persistence::EntityOrView_strategy)
def test_persistence::entityorview_implementsUserInterface_setter(instance):
    original = instance.implementsUserInterface
    instance.implementsUserInterface = original
    assert instance.implementsUserInterface == original

@given(instance=persistence::EntityOrView_strategy)
def test_persistence::entityorview_tableName_type(instance):
    assert isinstance(instance.tableName, str)


@given(instance=persistence::EntityOrView_strategy)
def test_persistence::entityorview_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original

@given(instance=persistence::EntityOrView_strategy)
def test_persistence::entityorview_pluralisedName_type(instance):
    assert isinstance(instance.pluralisedName, str)


@given(instance=persistence::EntityOrView_strategy)
def test_persistence::entityorview_pluralisedName_setter(instance):
    original = instance.pluralisedName
    instance.pluralisedName = original
    assert instance.pluralisedName == original

@given(instance=persistence::EntityOrView_strategy)
def test_persistence::entityorview_autoKeyGenerationStrategy_type(instance):
    assert isinstance(instance.autoKeyGenerationStrategy, str)


@given(instance=persistence::EntityOrView_strategy)
def test_persistence::entityorview_autoKeyGenerationStrategy_setter(instance):
    original = instance.autoKeyGenerationStrategy
    instance.autoKeyGenerationStrategy = original
    assert instance.autoKeyGenerationStrategy == original

@given(instance=persistence::EntityOrView_strategy)
def test_persistence::entityorview_autoKeyPersistentType_type(instance):
    assert isinstance(instance.autoKeyPersistentType, str)


@given(instance=persistence::EntityOrView_strategy)
def test_persistence::entityorview_autoKeyPersistentType_setter(instance):
    original = instance.autoKeyPersistentType
    instance.autoKeyPersistentType = original
    assert instance.autoKeyPersistentType == original

@given(instance=persistence::EntityOrView_strategy)
def test_persistence::entityorview_allowFormTypeCustomisation_type(instance):
    assert isinstance(instance.allowFormTypeCustomisation, bool)


@given(instance=persistence::EntityOrView_strategy)
def test_persistence::entityorview_allowFormTypeCustomisation_setter(instance):
    original = instance.allowFormTypeCustomisation
    instance.allowFormTypeCustomisation = original
    assert instance.allowFormTypeCustomisation == original

@given(instance=persistence::EntityOrView_strategy)
def test_persistence::entityorview_singletonName_type(instance):
    assert isinstance(instance.singletonName, str)


@given(instance=persistence::EntityOrView_strategy)
def test_persistence::entityorview_singletonName_setter(instance):
    original = instance.singletonName
    instance.singletonName = original
    assert instance.singletonName == original

@given(instance=persistence::DataType_strategy)
@settings(max_examples=50)
def test_persistence::datatype_instantiation(instance):
    assert isinstance(instance, persistence::DataType)

@given(instance=persistence::SerializationGroup_strategy)
@settings(max_examples=50)
def test_persistence::serializationgroup_instantiation(instance):
    assert isinstance(instance, persistence::SerializationGroup)

@given(instance=persistence::Persistence_strategy)
@settings(max_examples=50)
def test_persistence::persistence_instantiation(instance):
    assert isinstance(instance, persistence::Persistence)

@given(instance=persistence::Persistence_strategy)
def test_persistence::persistence_timestampCreation_type(instance):
    assert isinstance(instance.timestampCreation, bool)


@given(instance=persistence::Persistence_strategy)
def test_persistence::persistence_timestampCreation_setter(instance):
    original = instance.timestampCreation
    instance.timestampCreation = original
    assert instance.timestampCreation == original

@given(instance=persistence::Persistence_strategy)
def test_persistence::persistence_databaseTechnology_type(instance):
    assert isinstance(instance.databaseTechnology, str)


@given(instance=persistence::Persistence_strategy)
def test_persistence::persistence_databaseTechnology_setter(instance):
    original = instance.databaseTechnology
    instance.databaseTechnology = original
    assert instance.databaseTechnology == original

@given(instance=persistence::Persistence_strategy)
def test_persistence::persistence_timestampUpdates_type(instance):
    assert isinstance(instance.timestampUpdates, bool)


@given(instance=persistence::Persistence_strategy)
def test_persistence::persistence_timestampUpdates_setter(instance):
    original = instance.timestampUpdates
    instance.timestampUpdates = original
    assert instance.timestampUpdates == original

@given(instance=persistence::Persistence_strategy)
def test_persistence::persistence_ormTechnology_type(instance):
    assert isinstance(instance.ormTechnology, str)


@given(instance=persistence::Persistence_strategy)
def test_persistence::persistence_ormTechnology_setter(instance):
    original = instance.ormTechnology
    instance.ormTechnology = original
    assert instance.ormTechnology == original
