import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    EntityAssociation,
    persistence_AssociationWithoutContainment,
    EncapsulatedFeature,
    ViewFeature,
    persistence_EncapsulatedFeature,
    persistence_AssociationWithContainment,
    EntityAttribute,
    persistence_DataTypeAttribute,
    persistence_AssociationKey,
    Association,
    persistence_LocationAttribute,
    ResourceAttribute,
    persistence_ImageAttribute,
    persistence_FileAttribute,
    PathElement,
    persistence_DatePathElement,
    persistence_StaticPathElement,
    persistence_PathElement,
    persistence_ResourceAttribute,
    persistence_UrlAttribute,
    persistence_DateAttribute,
    ModelLabelFeature,
    persistence_ModelLabelAttribute,
    Attribute,
    persistence_EncapsulatedAttribute,
    EntityFeature,
    persistence_EntityAttribute,
    NamedDisplayElement,
    persistence_ViewAssociation,
    EntityOrView,
    persistence_View,
    persistence_Entity,
    persistence_EntityAssociation,
    persistence_ModelLabelAssociation,
    persistence_ModelLabelFeature,
    persistence_Label,
    persistence_EncapsulatedAssociation,
    persistence_Expression,
    Label,
    Feature,
    persistence_ViewFeature,
    persistence_EntityFeature,
    persistence_Association,
    persistence_Attribute,
    persistence_Feature,
    Classifier,
    NamedElement,
    persistence_ModelLabel,
    persistence_EntityOrView,
    persistence_DataType,
    persistence_SerializationGroup,
    persistence_Persistence,
    DatabaseTechnologies,
    DateDetails,
    OrmTechnologies,
    Cardinality,
    isHasChoices,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_entityassociation_is_not_abstract():
    assert not inspect.isabstract(EntityAssociation)


def test_entityassociation_constructor_exists():
    assert callable(EntityAssociation.__init__)


def test_entityassociation_constructor_args():
    sig = inspect.signature(EntityAssociation.__init__)
    params = list(sig.parameters.keys())



def test_persistence_associationwithoutcontainment_is_not_abstract():
    assert not inspect.isabstract(persistence_AssociationWithoutContainment)


def test_persistence_associationwithoutcontainment_constructor_exists():
    assert callable(persistence_AssociationWithoutContainment.__init__)


def test_persistence_associationwithoutcontainment_constructor_args():
    sig = inspect.signature(persistence_AssociationWithoutContainment.__init__)
    params = list(sig.parameters.keys())
    assert "targetUnique" in params, "Missing parameter 'targetUnique'"
    assert "targetCardinality" in params, "Missing parameter 'targetCardinality'"

def test_persistence_associationwithoutcontainment_has_targetUnique():
    assert hasattr(persistence_AssociationWithoutContainment, "targetUnique")
    descriptor = None
    for klass in persistence_AssociationWithoutContainment.__mro__:
        if "targetUnique" in klass.__dict__:
            descriptor = klass.__dict__["targetUnique"]
            break
    assert isinstance(descriptor, property)

def test_persistence_associationwithoutcontainment_has_targetCardinality():
    assert hasattr(persistence_AssociationWithoutContainment, "targetCardinality")
    descriptor = None
    for klass in persistence_AssociationWithoutContainment.__mro__:
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



def test_persistence_encapsulatedfeature_is_not_abstract():
    assert not inspect.isabstract(persistence_EncapsulatedFeature)


def test_persistence_encapsulatedfeature_constructor_exists():
    assert callable(persistence_EncapsulatedFeature.__init__)


def test_persistence_encapsulatedfeature_constructor_args():
    sig = inspect.signature(persistence_EncapsulatedFeature.__init__)
    params = list(sig.parameters.keys())
    assert "columnName" in params, "Missing parameter 'columnName'"
    assert "alias" in params, "Missing parameter 'alias'"
    assert "displayLabel" in params, "Missing parameter 'displayLabel'"

def test_persistence_encapsulatedfeature_has_columnName():
    assert hasattr(persistence_EncapsulatedFeature, "columnName")
    descriptor = None
    for klass in persistence_EncapsulatedFeature.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)

def test_persistence_encapsulatedfeature_has_alias():
    assert hasattr(persistence_EncapsulatedFeature, "alias")
    descriptor = None
    for klass in persistence_EncapsulatedFeature.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)

def test_persistence_encapsulatedfeature_has_displayLabel():
    assert hasattr(persistence_EncapsulatedFeature, "displayLabel")
    descriptor = None
    for klass in persistence_EncapsulatedFeature.__mro__:
        if "displayLabel" in klass.__dict__:
            descriptor = klass.__dict__["displayLabel"]
            break
    assert isinstance(descriptor, property)



def test_persistence_associationwithcontainment_is_not_abstract():
    assert not inspect.isabstract(persistence_AssociationWithContainment)


def test_persistence_associationwithcontainment_constructor_exists():
    assert callable(persistence_AssociationWithContainment.__init__)


def test_persistence_associationwithcontainment_constructor_args():
    sig = inspect.signature(persistence_AssociationWithContainment.__init__)
    params = list(sig.parameters.keys())
    assert "sourceVisible" in params, "Missing parameter 'sourceVisible'"

def test_persistence_associationwithcontainment_has_sourceVisible():
    assert hasattr(persistence_AssociationWithContainment, "sourceVisible")
    descriptor = None
    for klass in persistence_AssociationWithContainment.__mro__:
        if "sourceVisible" in klass.__dict__:
            descriptor = klass.__dict__["sourceVisible"]
            break
    assert isinstance(descriptor, property)



def test_entityattribute_is_not_abstract():
    assert not inspect.isabstract(EntityAttribute)


def test_entityattribute_constructor_exists():
    assert callable(EntityAttribute.__init__)


def test_entityattribute_constructor_args():
    sig = inspect.signature(EntityAttribute.__init__)
    params = list(sig.parameters.keys())



def test_persistence_datatypeattribute_is_not_abstract():
    assert not inspect.isabstract(persistence_DataTypeAttribute)


def test_persistence_datatypeattribute_constructor_exists():
    assert callable(persistence_DataTypeAttribute.__init__)


def test_persistence_datatypeattribute_constructor_args():
    sig = inspect.signature(persistence_DataTypeAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "obfuscateFormFields" in params, "Missing parameter 'obfuscateFormFields'"
    assert "caseInsensitive" in params, "Missing parameter 'caseInsensitive'"
    assert "encrypt" in params, "Missing parameter 'encrypt'"

def test_persistence_datatypeattribute_has_obfuscateFormFields():
    assert hasattr(persistence_DataTypeAttribute, "obfuscateFormFields")
    descriptor = None
    for klass in persistence_DataTypeAttribute.__mro__:
        if "obfuscateFormFields" in klass.__dict__:
            descriptor = klass.__dict__["obfuscateFormFields"]
            break
    assert isinstance(descriptor, property)

def test_persistence_datatypeattribute_has_caseInsensitive():
    assert hasattr(persistence_DataTypeAttribute, "caseInsensitive")
    descriptor = None
    for klass in persistence_DataTypeAttribute.__mro__:
        if "caseInsensitive" in klass.__dict__:
            descriptor = klass.__dict__["caseInsensitive"]
            break
    assert isinstance(descriptor, property)

def test_persistence_datatypeattribute_has_encrypt():
    assert hasattr(persistence_DataTypeAttribute, "encrypt")
    descriptor = None
    for klass in persistence_DataTypeAttribute.__mro__:
        if "encrypt" in klass.__dict__:
            descriptor = klass.__dict__["encrypt"]
            break
    assert isinstance(descriptor, property)



def test_persistence_associationkey_is_not_abstract():
    assert not inspect.isabstract(persistence_AssociationKey)


def test_persistence_associationkey_constructor_exists():
    assert callable(persistence_AssociationKey.__init__)


def test_persistence_associationkey_constructor_args():
    sig = inspect.signature(persistence_AssociationKey.__init__)
    params = list(sig.parameters.keys())
    assert "targetColumnName" in params, "Missing parameter 'targetColumnName'"

def test_persistence_associationkey_has_targetColumnName():
    assert hasattr(persistence_AssociationKey, "targetColumnName")
    descriptor = None
    for klass in persistence_AssociationKey.__mro__:
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



def test_persistence_locationattribute_is_not_abstract():
    assert not inspect.isabstract(persistence_LocationAttribute)


def test_persistence_locationattribute_constructor_exists():
    assert callable(persistence_LocationAttribute.__init__)


def test_persistence_locationattribute_constructor_args():
    sig = inspect.signature(persistence_LocationAttribute.__init__)
    params = list(sig.parameters.keys())



def test_resourceattribute_is_not_abstract():
    assert not inspect.isabstract(ResourceAttribute)


def test_resourceattribute_constructor_exists():
    assert callable(ResourceAttribute.__init__)


def test_resourceattribute_constructor_args():
    sig = inspect.signature(ResourceAttribute.__init__)
    params = list(sig.parameters.keys())



def test_persistence_imageattribute_is_not_abstract():
    assert not inspect.isabstract(persistence_ImageAttribute)


def test_persistence_imageattribute_constructor_exists():
    assert callable(persistence_ImageAttribute.__init__)


def test_persistence_imageattribute_constructor_args():
    sig = inspect.signature(persistence_ImageAttribute.__init__)
    params = list(sig.parameters.keys())



def test_persistence_fileattribute_is_not_abstract():
    assert not inspect.isabstract(persistence_FileAttribute)


def test_persistence_fileattribute_constructor_exists():
    assert callable(persistence_FileAttribute.__init__)


def test_persistence_fileattribute_constructor_args():
    sig = inspect.signature(persistence_FileAttribute.__init__)
    params = list(sig.parameters.keys())



def test_pathelement_is_not_abstract():
    assert not inspect.isabstract(PathElement)


def test_pathelement_constructor_exists():
    assert callable(PathElement.__init__)


def test_pathelement_constructor_args():
    sig = inspect.signature(PathElement.__init__)
    params = list(sig.parameters.keys())



def test_persistence_datepathelement_is_not_abstract():
    assert not inspect.isabstract(persistence_DatePathElement)


def test_persistence_datepathelement_constructor_exists():
    assert callable(persistence_DatePathElement.__init__)


def test_persistence_datepathelement_constructor_args():
    sig = inspect.signature(persistence_DatePathElement.__init__)
    params = list(sig.parameters.keys())
    assert "format" in params, "Missing parameter 'format'"

def test_persistence_datepathelement_has_format():
    assert hasattr(persistence_DatePathElement, "format")
    descriptor = None
    for klass in persistence_DatePathElement.__mro__:
        if "format" in klass.__dict__:
            descriptor = klass.__dict__["format"]
            break
    assert isinstance(descriptor, property)



def test_persistence_staticpathelement_is_not_abstract():
    assert not inspect.isabstract(persistence_StaticPathElement)


def test_persistence_staticpathelement_constructor_exists():
    assert callable(persistence_StaticPathElement.__init__)


def test_persistence_staticpathelement_constructor_args():
    sig = inspect.signature(persistence_StaticPathElement.__init__)
    params = list(sig.parameters.keys())
    assert "element" in params, "Missing parameter 'element'"

def test_persistence_staticpathelement_has_element():
    assert hasattr(persistence_StaticPathElement, "element")
    descriptor = None
    for klass in persistence_StaticPathElement.__mro__:
        if "element" in klass.__dict__:
            descriptor = klass.__dict__["element"]
            break
    assert isinstance(descriptor, property)



def test_persistence_pathelement_is_not_abstract():
    assert not inspect.isabstract(persistence_PathElement)


def test_persistence_pathelement_constructor_exists():
    assert callable(persistence_PathElement.__init__)


def test_persistence_pathelement_constructor_args():
    sig = inspect.signature(persistence_PathElement.__init__)
    params = list(sig.parameters.keys())



def test_persistence_resourceattribute_is_not_abstract():
    assert not inspect.isabstract(persistence_ResourceAttribute)


def test_persistence_resourceattribute_constructor_exists():
    assert callable(persistence_ResourceAttribute.__init__)


def test_persistence_resourceattribute_constructor_args():
    sig = inspect.signature(persistence_ResourceAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "uploadsWithinWebsite" in params, "Missing parameter 'uploadsWithinWebsite'"
    assert "maximumUploadSize" in params, "Missing parameter 'maximumUploadSize'"
    assert "validUploadMimeTypes" in params, "Missing parameter 'validUploadMimeTypes'"
    assert "validUploadExtensions" in params, "Missing parameter 'validUploadExtensions'"

def test_persistence_resourceattribute_has_uploadsWithinWebsite():
    assert hasattr(persistence_ResourceAttribute, "uploadsWithinWebsite")
    descriptor = None
    for klass in persistence_ResourceAttribute.__mro__:
        if "uploadsWithinWebsite" in klass.__dict__:
            descriptor = klass.__dict__["uploadsWithinWebsite"]
            break
    assert isinstance(descriptor, property)

def test_persistence_resourceattribute_has_maximumUploadSize():
    assert hasattr(persistence_ResourceAttribute, "maximumUploadSize")
    descriptor = None
    for klass in persistence_ResourceAttribute.__mro__:
        if "maximumUploadSize" in klass.__dict__:
            descriptor = klass.__dict__["maximumUploadSize"]
            break
    assert isinstance(descriptor, property)

def test_persistence_resourceattribute_has_validUploadMimeTypes():
    assert hasattr(persistence_ResourceAttribute, "validUploadMimeTypes")
    descriptor = None
    for klass in persistence_ResourceAttribute.__mro__:
        if "validUploadMimeTypes" in klass.__dict__:
            descriptor = klass.__dict__["validUploadMimeTypes"]
            break
    assert isinstance(descriptor, property)

def test_persistence_resourceattribute_has_validUploadExtensions():
    assert hasattr(persistence_ResourceAttribute, "validUploadExtensions")
    descriptor = None
    for klass in persistence_ResourceAttribute.__mro__:
        if "validUploadExtensions" in klass.__dict__:
            descriptor = klass.__dict__["validUploadExtensions"]
            break
    assert isinstance(descriptor, property)



def test_persistence_urlattribute_is_not_abstract():
    assert not inspect.isabstract(persistence_UrlAttribute)


def test_persistence_urlattribute_constructor_exists():
    assert callable(persistence_UrlAttribute.__init__)


def test_persistence_urlattribute_constructor_args():
    sig = inspect.signature(persistence_UrlAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "displayValue" in params, "Missing parameter 'displayValue'"

def test_persistence_urlattribute_has_displayValue():
    assert hasattr(persistence_UrlAttribute, "displayValue")
    descriptor = None
    for klass in persistence_UrlAttribute.__mro__:
        if "displayValue" in klass.__dict__:
            descriptor = klass.__dict__["displayValue"]
            break
    assert isinstance(descriptor, property)



def test_persistence_dateattribute_is_not_abstract():
    assert not inspect.isabstract(persistence_DateAttribute)


def test_persistence_dateattribute_constructor_exists():
    assert callable(persistence_DateAttribute.__init__)


def test_persistence_dateattribute_constructor_args():
    sig = inspect.signature(persistence_DateAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "format" in params, "Missing parameter 'format'"
    assert "details" in params, "Missing parameter 'details'"

def test_persistence_dateattribute_has_format():
    assert hasattr(persistence_DateAttribute, "format")
    descriptor = None
    for klass in persistence_DateAttribute.__mro__:
        if "format" in klass.__dict__:
            descriptor = klass.__dict__["format"]
            break
    assert isinstance(descriptor, property)

def test_persistence_dateattribute_has_details():
    assert hasattr(persistence_DateAttribute, "details")
    descriptor = None
    for klass in persistence_DateAttribute.__mro__:
        if "details" in klass.__dict__:
            descriptor = klass.__dict__["details"]
            break
    assert isinstance(descriptor, property)



def test_modellabelfeature_is_not_abstract():
    assert not inspect.isabstract(ModelLabelFeature)


def test_modellabelfeature_constructor_exists():
    assert callable(ModelLabelFeature.__init__)


def test_modellabelfeature_constructor_args():
    sig = inspect.signature(ModelLabelFeature.__init__)
    params = list(sig.parameters.keys())



def test_persistence_modellabelattribute_is_not_abstract():
    assert not inspect.isabstract(persistence_ModelLabelAttribute)


def test_persistence_modellabelattribute_constructor_exists():
    assert callable(persistence_ModelLabelAttribute.__init__)


def test_persistence_modellabelattribute_constructor_args():
    sig = inspect.signature(persistence_ModelLabelAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "dateFormat" in params, "Missing parameter 'dateFormat'"

def test_persistence_modellabelattribute_has_dateFormat():
    assert hasattr(persistence_ModelLabelAttribute, "dateFormat")
    descriptor = None
    for klass in persistence_ModelLabelAttribute.__mro__:
        if "dateFormat" in klass.__dict__:
            descriptor = klass.__dict__["dateFormat"]
            break
    assert isinstance(descriptor, property)



def test_attribute_is_not_abstract():
    assert not inspect.isabstract(Attribute)


def test_attribute_constructor_exists():
    assert callable(Attribute.__init__)


def test_attribute_constructor_args():
    sig = inspect.signature(Attribute.__init__)
    params = list(sig.parameters.keys())



def test_persistence_encapsulatedattribute_is_not_abstract():
    assert not inspect.isabstract(persistence_EncapsulatedAttribute)


def test_persistence_encapsulatedattribute_constructor_exists():
    assert callable(persistence_EncapsulatedAttribute.__init__)


def test_persistence_encapsulatedattribute_constructor_args():
    sig = inspect.signature(persistence_EncapsulatedAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "cardinality" in params, "Missing parameter 'cardinality'"

def test_persistence_encapsulatedattribute_has_name():
    assert hasattr(persistence_EncapsulatedAttribute, "name")
    descriptor = None
    for klass in persistence_EncapsulatedAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_persistence_encapsulatedattribute_has_cardinality():
    assert hasattr(persistence_EncapsulatedAttribute, "cardinality")
    descriptor = None
    for klass in persistence_EncapsulatedAttribute.__mro__:
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



def test_persistence_entityattribute_is_not_abstract():
    assert not inspect.isabstract(persistence_EntityAttribute)


def test_persistence_entityattribute_constructor_exists():
    assert callable(persistence_EntityAttribute.__init__)


def test_persistence_entityattribute_constructor_args():
    sig = inspect.signature(persistence_EntityAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "persistentType" in params, "Missing parameter 'persistentType'"
    assert "primaryKey" in params, "Missing parameter 'primaryKey'"
    assert "ormType" in params, "Missing parameter 'ormType'"
    assert "interfaceType" in params, "Missing parameter 'interfaceType'"
    assert "containerUnique" in params, "Missing parameter 'containerUnique'"

def test_persistence_entityattribute_has_persistentType():
    assert hasattr(persistence_EntityAttribute, "persistentType")
    descriptor = None
    for klass in persistence_EntityAttribute.__mro__:
        if "persistentType" in klass.__dict__:
            descriptor = klass.__dict__["persistentType"]
            break
    assert isinstance(descriptor, property)

def test_persistence_entityattribute_has_primaryKey():
    assert hasattr(persistence_EntityAttribute, "primaryKey")
    descriptor = None
    for klass in persistence_EntityAttribute.__mro__:
        if "primaryKey" in klass.__dict__:
            descriptor = klass.__dict__["primaryKey"]
            break
    assert isinstance(descriptor, property)

def test_persistence_entityattribute_has_ormType():
    assert hasattr(persistence_EntityAttribute, "ormType")
    descriptor = None
    for klass in persistence_EntityAttribute.__mro__:
        if "ormType" in klass.__dict__:
            descriptor = klass.__dict__["ormType"]
            break
    assert isinstance(descriptor, property)

def test_persistence_entityattribute_has_interfaceType():
    assert hasattr(persistence_EntityAttribute, "interfaceType")
    descriptor = None
    for klass in persistence_EntityAttribute.__mro__:
        if "interfaceType" in klass.__dict__:
            descriptor = klass.__dict__["interfaceType"]
            break
    assert isinstance(descriptor, property)

def test_persistence_entityattribute_has_containerUnique():
    assert hasattr(persistence_EntityAttribute, "containerUnique")
    descriptor = None
    for klass in persistence_EntityAttribute.__mro__:
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



def test_persistence_viewassociation_is_not_abstract():
    assert not inspect.isabstract(persistence_ViewAssociation)


def test_persistence_viewassociation_constructor_exists():
    assert callable(persistence_ViewAssociation.__init__)


def test_persistence_viewassociation_constructor_args():
    sig = inspect.signature(persistence_ViewAssociation.__init__)
    params = list(sig.parameters.keys())
    assert "cardinality" in params, "Missing parameter 'cardinality'"

def test_persistence_viewassociation_has_cardinality():
    assert hasattr(persistence_ViewAssociation, "cardinality")
    descriptor = None
    for klass in persistence_ViewAssociation.__mro__:
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



def test_persistence_view_is_not_abstract():
    assert not inspect.isabstract(persistence_View)


def test_persistence_view_constructor_exists():
    assert callable(persistence_View.__init__)


def test_persistence_view_constructor_args():
    sig = inspect.signature(persistence_View.__init__)
    params = list(sig.parameters.keys())



def test_persistence_entity_is_not_abstract():
    assert not inspect.isabstract(persistence_Entity)


def test_persistence_entity_constructor_exists():
    assert callable(persistence_Entity.__init__)


def test_persistence_entity_constructor_args():
    sig = inspect.signature(persistence_Entity.__init__)
    params = list(sig.parameters.keys())



def test_persistence_entityassociation_is_not_abstract():
    assert not inspect.isabstract(persistence_EntityAssociation)


def test_persistence_entityassociation_constructor_exists():
    assert callable(persistence_EntityAssociation.__init__)


def test_persistence_entityassociation_constructor_args():
    sig = inspect.signature(persistence_EntityAssociation.__init__)
    params = list(sig.parameters.keys())
    assert "targetInputClass" in params, "Missing parameter 'targetInputClass'"
    assert "pivotTableName" in params, "Missing parameter 'pivotTableName'"
    assert "targetPrimaryKey" in params, "Missing parameter 'targetPrimaryKey'"
    assert "targetFeatureName" in params, "Missing parameter 'targetFeatureName'"
    assert "targetHeaderClass" in params, "Missing parameter 'targetHeaderClass'"
    assert "targetDisplayLabel" in params, "Missing parameter 'targetDisplayLabel'"
    assert "bidirectional" in params, "Missing parameter 'bidirectional'"
    assert "targetDisplayClass" in params, "Missing parameter 'targetDisplayClass'"
    assert "targetFooterClass" in params, "Missing parameter 'targetFooterClass'"

def test_persistence_entityassociation_has_targetInputClass():
    assert hasattr(persistence_EntityAssociation, "targetInputClass")
    descriptor = None
    for klass in persistence_EntityAssociation.__mro__:
        if "targetInputClass" in klass.__dict__:
            descriptor = klass.__dict__["targetInputClass"]
            break
    assert isinstance(descriptor, property)

def test_persistence_entityassociation_has_pivotTableName():
    assert hasattr(persistence_EntityAssociation, "pivotTableName")
    descriptor = None
    for klass in persistence_EntityAssociation.__mro__:
        if "pivotTableName" in klass.__dict__:
            descriptor = klass.__dict__["pivotTableName"]
            break
    assert isinstance(descriptor, property)

def test_persistence_entityassociation_has_targetPrimaryKey():
    assert hasattr(persistence_EntityAssociation, "targetPrimaryKey")
    descriptor = None
    for klass in persistence_EntityAssociation.__mro__:
        if "targetPrimaryKey" in klass.__dict__:
            descriptor = klass.__dict__["targetPrimaryKey"]
            break
    assert isinstance(descriptor, property)

def test_persistence_entityassociation_has_targetFeatureName():
    assert hasattr(persistence_EntityAssociation, "targetFeatureName")
    descriptor = None
    for klass in persistence_EntityAssociation.__mro__:
        if "targetFeatureName" in klass.__dict__:
            descriptor = klass.__dict__["targetFeatureName"]
            break
    assert isinstance(descriptor, property)

def test_persistence_entityassociation_has_targetHeaderClass():
    assert hasattr(persistence_EntityAssociation, "targetHeaderClass")
    descriptor = None
    for klass in persistence_EntityAssociation.__mro__:
        if "targetHeaderClass" in klass.__dict__:
            descriptor = klass.__dict__["targetHeaderClass"]
            break
    assert isinstance(descriptor, property)

def test_persistence_entityassociation_has_targetDisplayLabel():
    assert hasattr(persistence_EntityAssociation, "targetDisplayLabel")
    descriptor = None
    for klass in persistence_EntityAssociation.__mro__:
        if "targetDisplayLabel" in klass.__dict__:
            descriptor = klass.__dict__["targetDisplayLabel"]
            break
    assert isinstance(descriptor, property)

def test_persistence_entityassociation_has_bidirectional():
    assert hasattr(persistence_EntityAssociation, "bidirectional")
    descriptor = None
    for klass in persistence_EntityAssociation.__mro__:
        if "bidirectional" in klass.__dict__:
            descriptor = klass.__dict__["bidirectional"]
            break
    assert isinstance(descriptor, property)

def test_persistence_entityassociation_has_targetDisplayClass():
    assert hasattr(persistence_EntityAssociation, "targetDisplayClass")
    descriptor = None
    for klass in persistence_EntityAssociation.__mro__:
        if "targetDisplayClass" in klass.__dict__:
            descriptor = klass.__dict__["targetDisplayClass"]
            break
    assert isinstance(descriptor, property)

def test_persistence_entityassociation_has_targetFooterClass():
    assert hasattr(persistence_EntityAssociation, "targetFooterClass")
    descriptor = None
    for klass in persistence_EntityAssociation.__mro__:
        if "targetFooterClass" in klass.__dict__:
            descriptor = klass.__dict__["targetFooterClass"]
            break
    assert isinstance(descriptor, property)



def test_persistence_modellabelassociation_is_not_abstract():
    assert not inspect.isabstract(persistence_ModelLabelAssociation)


def test_persistence_modellabelassociation_constructor_exists():
    assert callable(persistence_ModelLabelAssociation.__init__)


def test_persistence_modellabelassociation_constructor_args():
    sig = inspect.signature(persistence_ModelLabelAssociation.__init__)
    params = list(sig.parameters.keys())
    assert "isSourceAssociation" in params, "Missing parameter 'isSourceAssociation'"

def test_persistence_modellabelassociation_has_isSourceAssociation():
    assert hasattr(persistence_ModelLabelAssociation, "isSourceAssociation")
    descriptor = None
    for klass in persistence_ModelLabelAssociation.__mro__:
        if "isSourceAssociation" in klass.__dict__:
            descriptor = klass.__dict__["isSourceAssociation"]
            break
    assert isinstance(descriptor, property)



def test_persistence_modellabelfeature_is_not_abstract():
    assert not inspect.isabstract(persistence_ModelLabelFeature)


def test_persistence_modellabelfeature_constructor_exists():
    assert callable(persistence_ModelLabelFeature.__init__)


def test_persistence_modellabelfeature_constructor_args():
    sig = inspect.signature(persistence_ModelLabelFeature.__init__)
    params = list(sig.parameters.keys())



def test_persistence_label_is_not_abstract():
    assert not inspect.isabstract(persistence_Label)


def test_persistence_label_constructor_exists():
    assert callable(persistence_Label.__init__)


def test_persistence_label_constructor_args():
    sig = inspect.signature(persistence_Label.__init__)
    params = list(sig.parameters.keys())



def test_persistence_encapsulatedassociation_is_not_abstract():
    assert not inspect.isabstract(persistence_EncapsulatedAssociation)


def test_persistence_encapsulatedassociation_constructor_exists():
    assert callable(persistence_EncapsulatedAssociation.__init__)


def test_persistence_encapsulatedassociation_constructor_args():
    sig = inspect.signature(persistence_EncapsulatedAssociation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isSourceAssociation" in params, "Missing parameter 'isSourceAssociation'"
    assert "cardinality" in params, "Missing parameter 'cardinality'"

def test_persistence_encapsulatedassociation_has_name():
    assert hasattr(persistence_EncapsulatedAssociation, "name")
    descriptor = None
    for klass in persistence_EncapsulatedAssociation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_persistence_encapsulatedassociation_has_isSourceAssociation():
    assert hasattr(persistence_EncapsulatedAssociation, "isSourceAssociation")
    descriptor = None
    for klass in persistence_EncapsulatedAssociation.__mro__:
        if "isSourceAssociation" in klass.__dict__:
            descriptor = klass.__dict__["isSourceAssociation"]
            break
    assert isinstance(descriptor, property)

def test_persistence_encapsulatedassociation_has_cardinality():
    assert hasattr(persistence_EncapsulatedAssociation, "cardinality")
    descriptor = None
    for klass in persistence_EncapsulatedAssociation.__mro__:
        if "cardinality" in klass.__dict__:
            descriptor = klass.__dict__["cardinality"]
            break
    assert isinstance(descriptor, property)



def test_persistence_expression_is_not_abstract():
    assert not inspect.isabstract(persistence_Expression)


def test_persistence_expression_constructor_exists():
    assert callable(persistence_Expression.__init__)


def test_persistence_expression_constructor_args():
    sig = inspect.signature(persistence_Expression.__init__)
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



def test_persistence_viewfeature_is_not_abstract():
    assert not inspect.isabstract(persistence_ViewFeature)


def test_persistence_viewfeature_constructor_exists():
    assert callable(persistence_ViewFeature.__init__)


def test_persistence_viewfeature_constructor_args():
    sig = inspect.signature(persistence_ViewFeature.__init__)
    params = list(sig.parameters.keys())



def test_persistence_entityfeature_is_not_abstract():
    assert not inspect.isabstract(persistence_EntityFeature)


def test_persistence_entityfeature_constructor_exists():
    assert callable(persistence_EntityFeature.__init__)


def test_persistence_entityfeature_constructor_args():
    sig = inspect.signature(persistence_EntityFeature.__init__)
    params = list(sig.parameters.keys())
    assert "singletonName" in params, "Missing parameter 'singletonName'"
    assert "pluralisedName" in params, "Missing parameter 'pluralisedName'"
    assert "columnName" in params, "Missing parameter 'columnName'"
    assert "booleanIsHasChoice" in params, "Missing parameter 'booleanIsHasChoice'"
    assert "ordered" in params, "Missing parameter 'ordered'"
    assert "unique" in params, "Missing parameter 'unique'"
    assert "cardinality" in params, "Missing parameter 'cardinality'"

def test_persistence_entityfeature_has_singletonName():
    assert hasattr(persistence_EntityFeature, "singletonName")
    descriptor = None
    for klass in persistence_EntityFeature.__mro__:
        if "singletonName" in klass.__dict__:
            descriptor = klass.__dict__["singletonName"]
            break
    assert isinstance(descriptor, property)

def test_persistence_entityfeature_has_pluralisedName():
    assert hasattr(persistence_EntityFeature, "pluralisedName")
    descriptor = None
    for klass in persistence_EntityFeature.__mro__:
        if "pluralisedName" in klass.__dict__:
            descriptor = klass.__dict__["pluralisedName"]
            break
    assert isinstance(descriptor, property)

def test_persistence_entityfeature_has_columnName():
    assert hasattr(persistence_EntityFeature, "columnName")
    descriptor = None
    for klass in persistence_EntityFeature.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)

def test_persistence_entityfeature_has_booleanIsHasChoice():
    assert hasattr(persistence_EntityFeature, "booleanIsHasChoice")
    descriptor = None
    for klass in persistence_EntityFeature.__mro__:
        if "booleanIsHasChoice" in klass.__dict__:
            descriptor = klass.__dict__["booleanIsHasChoice"]
            break
    assert isinstance(descriptor, property)

def test_persistence_entityfeature_has_ordered():
    assert hasattr(persistence_EntityFeature, "ordered")
    descriptor = None
    for klass in persistence_EntityFeature.__mro__:
        if "ordered" in klass.__dict__:
            descriptor = klass.__dict__["ordered"]
            break
    assert isinstance(descriptor, property)

def test_persistence_entityfeature_has_unique():
    assert hasattr(persistence_EntityFeature, "unique")
    descriptor = None
    for klass in persistence_EntityFeature.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)

def test_persistence_entityfeature_has_cardinality():
    assert hasattr(persistence_EntityFeature, "cardinality")
    descriptor = None
    for klass in persistence_EntityFeature.__mro__:
        if "cardinality" in klass.__dict__:
            descriptor = klass.__dict__["cardinality"]
            break
    assert isinstance(descriptor, property)



def test_persistence_association_is_not_abstract():
    assert not inspect.isabstract(persistence_Association)


def test_persistence_association_constructor_exists():
    assert callable(persistence_Association.__init__)


def test_persistence_association_constructor_args():
    sig = inspect.signature(persistence_Association.__init__)
    params = list(sig.parameters.keys())
    assert "serializationMaxDepth" in params, "Missing parameter 'serializationMaxDepth'"
    assert "pseudo" in params, "Missing parameter 'pseudo'"
    assert "inputClass" in params, "Missing parameter 'inputClass'"

def test_persistence_association_has_serializationMaxDepth():
    assert hasattr(persistence_Association, "serializationMaxDepth")
    descriptor = None
    for klass in persistence_Association.__mro__:
        if "serializationMaxDepth" in klass.__dict__:
            descriptor = klass.__dict__["serializationMaxDepth"]
            break
    assert isinstance(descriptor, property)

def test_persistence_association_has_pseudo():
    assert hasattr(persistence_Association, "pseudo")
    descriptor = None
    for klass in persistence_Association.__mro__:
        if "pseudo" in klass.__dict__:
            descriptor = klass.__dict__["pseudo"]
            break
    assert isinstance(descriptor, property)

def test_persistence_association_has_inputClass():
    assert hasattr(persistence_Association, "inputClass")
    descriptor = None
    for klass in persistence_Association.__mro__:
        if "inputClass" in klass.__dict__:
            descriptor = klass.__dict__["inputClass"]
            break
    assert isinstance(descriptor, property)



def test_persistence_attribute_is_not_abstract():
    assert not inspect.isabstract(persistence_Attribute)


def test_persistence_attribute_constructor_exists():
    assert callable(persistence_Attribute.__init__)


def test_persistence_attribute_constructor_args():
    sig = inspect.signature(persistence_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "validationPattern" in params, "Missing parameter 'validationPattern'"
    assert "placeholder" in params, "Missing parameter 'placeholder'"
    assert "inputClass" in params, "Missing parameter 'inputClass'"

def test_persistence_attribute_has_validationPattern():
    assert hasattr(persistence_Attribute, "validationPattern")
    descriptor = None
    for klass in persistence_Attribute.__mro__:
        if "validationPattern" in klass.__dict__:
            descriptor = klass.__dict__["validationPattern"]
            break
    assert isinstance(descriptor, property)

def test_persistence_attribute_has_placeholder():
    assert hasattr(persistence_Attribute, "placeholder")
    descriptor = None
    for klass in persistence_Attribute.__mro__:
        if "placeholder" in klass.__dict__:
            descriptor = klass.__dict__["placeholder"]
            break
    assert isinstance(descriptor, property)

def test_persistence_attribute_has_inputClass():
    assert hasattr(persistence_Attribute, "inputClass")
    descriptor = None
    for klass in persistence_Attribute.__mro__:
        if "inputClass" in klass.__dict__:
            descriptor = klass.__dict__["inputClass"]
            break
    assert isinstance(descriptor, property)



def test_persistence_feature_is_not_abstract():
    assert not inspect.isabstract(persistence_Feature)


def test_persistence_feature_constructor_exists():
    assert callable(persistence_Feature.__init__)


def test_persistence_feature_constructor_args():
    sig = inspect.signature(persistence_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "encodeUriKey" in params, "Missing parameter 'encodeUriKey'"
    assert "displayClass" in params, "Missing parameter 'displayClass'"
    assert "collectionAllowRemove" in params, "Missing parameter 'collectionAllowRemove'"
    assert "title" in params, "Missing parameter 'title'"
    assert "collectionAllowAdd" in params, "Missing parameter 'collectionAllowAdd'"
    assert "headerClass" in params, "Missing parameter 'headerClass'"
    assert "footerClass" in params, "Missing parameter 'footerClass'"
    assert "nullDisplayValue" in params, "Missing parameter 'nullDisplayValue'"

def test_persistence_feature_has_encodeUriKey():
    assert hasattr(persistence_Feature, "encodeUriKey")
    descriptor = None
    for klass in persistence_Feature.__mro__:
        if "encodeUriKey" in klass.__dict__:
            descriptor = klass.__dict__["encodeUriKey"]
            break
    assert isinstance(descriptor, property)

def test_persistence_feature_has_displayClass():
    assert hasattr(persistence_Feature, "displayClass")
    descriptor = None
    for klass in persistence_Feature.__mro__:
        if "displayClass" in klass.__dict__:
            descriptor = klass.__dict__["displayClass"]
            break
    assert isinstance(descriptor, property)

def test_persistence_feature_has_collectionAllowRemove():
    assert hasattr(persistence_Feature, "collectionAllowRemove")
    descriptor = None
    for klass in persistence_Feature.__mro__:
        if "collectionAllowRemove" in klass.__dict__:
            descriptor = klass.__dict__["collectionAllowRemove"]
            break
    assert isinstance(descriptor, property)

def test_persistence_feature_has_title():
    assert hasattr(persistence_Feature, "title")
    descriptor = None
    for klass in persistence_Feature.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_persistence_feature_has_collectionAllowAdd():
    assert hasattr(persistence_Feature, "collectionAllowAdd")
    descriptor = None
    for klass in persistence_Feature.__mro__:
        if "collectionAllowAdd" in klass.__dict__:
            descriptor = klass.__dict__["collectionAllowAdd"]
            break
    assert isinstance(descriptor, property)

def test_persistence_feature_has_headerClass():
    assert hasattr(persistence_Feature, "headerClass")
    descriptor = None
    for klass in persistence_Feature.__mro__:
        if "headerClass" in klass.__dict__:
            descriptor = klass.__dict__["headerClass"]
            break
    assert isinstance(descriptor, property)

def test_persistence_feature_has_footerClass():
    assert hasattr(persistence_Feature, "footerClass")
    descriptor = None
    for klass in persistence_Feature.__mro__:
        if "footerClass" in klass.__dict__:
            descriptor = klass.__dict__["footerClass"]
            break
    assert isinstance(descriptor, property)

def test_persistence_feature_has_nullDisplayValue():
    assert hasattr(persistence_Feature, "nullDisplayValue")
    descriptor = None
    for klass in persistence_Feature.__mro__:
        if "nullDisplayValue" in klass.__dict__:
            descriptor = klass.__dict__["nullDisplayValue"]
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



def test_persistence_modellabel_is_not_abstract():
    assert not inspect.isabstract(persistence_ModelLabel)


def test_persistence_modellabel_constructor_exists():
    assert callable(persistence_ModelLabel.__init__)


def test_persistence_modellabel_constructor_args():
    sig = inspect.signature(persistence_ModelLabel.__init__)
    params = list(sig.parameters.keys())
    assert "format" in params, "Missing parameter 'format'"

def test_persistence_modellabel_has_format():
    assert hasattr(persistence_ModelLabel, "format")
    descriptor = None
    for klass in persistence_ModelLabel.__mro__:
        if "format" in klass.__dict__:
            descriptor = klass.__dict__["format"]
            break
    assert isinstance(descriptor, property)



def test_persistence_entityorview_is_not_abstract():
    assert not inspect.isabstract(persistence_EntityOrView)


def test_persistence_entityorview_constructor_exists():
    assert callable(persistence_EntityOrView.__init__)


def test_persistence_entityorview_constructor_args():
    sig = inspect.signature(persistence_EntityOrView.__init__)
    params = list(sig.parameters.keys())
    assert "autoKeyGenerationStrategy" in params, "Missing parameter 'autoKeyGenerationStrategy'"
    assert "autoKeyName" in params, "Missing parameter 'autoKeyName'"
    assert "pluralisedName" in params, "Missing parameter 'pluralisedName'"
    assert "autoKeyPersistentType" in params, "Missing parameter 'autoKeyPersistentType'"
    assert "implementsUserInterface" in params, "Missing parameter 'implementsUserInterface'"
    assert "singletonName" in params, "Missing parameter 'singletonName'"
    assert "tableName" in params, "Missing parameter 'tableName'"

def test_persistence_entityorview_has_autoKeyGenerationStrategy():
    assert hasattr(persistence_EntityOrView, "autoKeyGenerationStrategy")
    descriptor = None
    for klass in persistence_EntityOrView.__mro__:
        if "autoKeyGenerationStrategy" in klass.__dict__:
            descriptor = klass.__dict__["autoKeyGenerationStrategy"]
            break
    assert isinstance(descriptor, property)

def test_persistence_entityorview_has_autoKeyName():
    assert hasattr(persistence_EntityOrView, "autoKeyName")
    descriptor = None
    for klass in persistence_EntityOrView.__mro__:
        if "autoKeyName" in klass.__dict__:
            descriptor = klass.__dict__["autoKeyName"]
            break
    assert isinstance(descriptor, property)

def test_persistence_entityorview_has_pluralisedName():
    assert hasattr(persistence_EntityOrView, "pluralisedName")
    descriptor = None
    for klass in persistence_EntityOrView.__mro__:
        if "pluralisedName" in klass.__dict__:
            descriptor = klass.__dict__["pluralisedName"]
            break
    assert isinstance(descriptor, property)

def test_persistence_entityorview_has_autoKeyPersistentType():
    assert hasattr(persistence_EntityOrView, "autoKeyPersistentType")
    descriptor = None
    for klass in persistence_EntityOrView.__mro__:
        if "autoKeyPersistentType" in klass.__dict__:
            descriptor = klass.__dict__["autoKeyPersistentType"]
            break
    assert isinstance(descriptor, property)

def test_persistence_entityorview_has_implementsUserInterface():
    assert hasattr(persistence_EntityOrView, "implementsUserInterface")
    descriptor = None
    for klass in persistence_EntityOrView.__mro__:
        if "implementsUserInterface" in klass.__dict__:
            descriptor = klass.__dict__["implementsUserInterface"]
            break
    assert isinstance(descriptor, property)

def test_persistence_entityorview_has_singletonName():
    assert hasattr(persistence_EntityOrView, "singletonName")
    descriptor = None
    for klass in persistence_EntityOrView.__mro__:
        if "singletonName" in klass.__dict__:
            descriptor = klass.__dict__["singletonName"]
            break
    assert isinstance(descriptor, property)

def test_persistence_entityorview_has_tableName():
    assert hasattr(persistence_EntityOrView, "tableName")
    descriptor = None
    for klass in persistence_EntityOrView.__mro__:
        if "tableName" in klass.__dict__:
            descriptor = klass.__dict__["tableName"]
            break
    assert isinstance(descriptor, property)



def test_persistence_datatype_is_not_abstract():
    assert not inspect.isabstract(persistence_DataType)


def test_persistence_datatype_constructor_exists():
    assert callable(persistence_DataType.__init__)


def test_persistence_datatype_constructor_args():
    sig = inspect.signature(persistence_DataType.__init__)
    params = list(sig.parameters.keys())



def test_persistence_serializationgroup_is_not_abstract():
    assert not inspect.isabstract(persistence_SerializationGroup)


def test_persistence_serializationgroup_constructor_exists():
    assert callable(persistence_SerializationGroup.__init__)


def test_persistence_serializationgroup_constructor_args():
    sig = inspect.signature(persistence_SerializationGroup.__init__)
    params = list(sig.parameters.keys())



def test_persistence_persistence_is_not_abstract():
    assert not inspect.isabstract(persistence_Persistence)


def test_persistence_persistence_constructor_exists():
    assert callable(persistence_Persistence.__init__)


def test_persistence_persistence_constructor_args():
    sig = inspect.signature(persistence_Persistence.__init__)
    params = list(sig.parameters.keys())
    assert "databaseName" in params, "Missing parameter 'databaseName'"
    assert "databasePassword" in params, "Missing parameter 'databasePassword'"
    assert "ormTechnology" in params, "Missing parameter 'ormTechnology'"
    assert "timestampCreation" in params, "Missing parameter 'timestampCreation'"
    assert "databaseUsername" in params, "Missing parameter 'databaseUsername'"
    assert "databaseHost" in params, "Missing parameter 'databaseHost'"
    assert "databasePrefix" in params, "Missing parameter 'databasePrefix'"
    assert "databasePort" in params, "Missing parameter 'databasePort'"
    assert "databaseTechnology" in params, "Missing parameter 'databaseTechnology'"
    assert "timestampUpdates" in params, "Missing parameter 'timestampUpdates'"

def test_persistence_persistence_has_databaseName():
    assert hasattr(persistence_Persistence, "databaseName")
    descriptor = None
    for klass in persistence_Persistence.__mro__:
        if "databaseName" in klass.__dict__:
            descriptor = klass.__dict__["databaseName"]
            break
    assert isinstance(descriptor, property)

def test_persistence_persistence_has_databasePassword():
    assert hasattr(persistence_Persistence, "databasePassword")
    descriptor = None
    for klass in persistence_Persistence.__mro__:
        if "databasePassword" in klass.__dict__:
            descriptor = klass.__dict__["databasePassword"]
            break
    assert isinstance(descriptor, property)

def test_persistence_persistence_has_ormTechnology():
    assert hasattr(persistence_Persistence, "ormTechnology")
    descriptor = None
    for klass in persistence_Persistence.__mro__:
        if "ormTechnology" in klass.__dict__:
            descriptor = klass.__dict__["ormTechnology"]
            break
    assert isinstance(descriptor, property)

def test_persistence_persistence_has_timestampCreation():
    assert hasattr(persistence_Persistence, "timestampCreation")
    descriptor = None
    for klass in persistence_Persistence.__mro__:
        if "timestampCreation" in klass.__dict__:
            descriptor = klass.__dict__["timestampCreation"]
            break
    assert isinstance(descriptor, property)

def test_persistence_persistence_has_databaseUsername():
    assert hasattr(persistence_Persistence, "databaseUsername")
    descriptor = None
    for klass in persistence_Persistence.__mro__:
        if "databaseUsername" in klass.__dict__:
            descriptor = klass.__dict__["databaseUsername"]
            break
    assert isinstance(descriptor, property)

def test_persistence_persistence_has_databaseHost():
    assert hasattr(persistence_Persistence, "databaseHost")
    descriptor = None
    for klass in persistence_Persistence.__mro__:
        if "databaseHost" in klass.__dict__:
            descriptor = klass.__dict__["databaseHost"]
            break
    assert isinstance(descriptor, property)

def test_persistence_persistence_has_databasePrefix():
    assert hasattr(persistence_Persistence, "databasePrefix")
    descriptor = None
    for klass in persistence_Persistence.__mro__:
        if "databasePrefix" in klass.__dict__:
            descriptor = klass.__dict__["databasePrefix"]
            break
    assert isinstance(descriptor, property)

def test_persistence_persistence_has_databasePort():
    assert hasattr(persistence_Persistence, "databasePort")
    descriptor = None
    for klass in persistence_Persistence.__mro__:
        if "databasePort" in klass.__dict__:
            descriptor = klass.__dict__["databasePort"]
            break
    assert isinstance(descriptor, property)

def test_persistence_persistence_has_databaseTechnology():
    assert hasattr(persistence_Persistence, "databaseTechnology")
    descriptor = None
    for klass in persistence_Persistence.__mro__:
        if "databaseTechnology" in klass.__dict__:
            descriptor = klass.__dict__["databaseTechnology"]
            break
    assert isinstance(descriptor, property)

def test_persistence_persistence_has_timestampUpdates():
    assert hasattr(persistence_Persistence, "timestampUpdates")
    descriptor = None
    for klass in persistence_Persistence.__mro__:
        if "timestampUpdates" in klass.__dict__:
            descriptor = klass.__dict__["timestampUpdates"]
            break
    assert isinstance(descriptor, property)

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
        "DateOnly",
        "TimeOnly",
        "DateAndTime",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DateDetails"

def test_ormtechnologies_exists():
    # Check that the Enumeration exists
    assert OrmTechnologies is not None

def test_ormtechnologies_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OrmTechnologies]
    expected_literals = [
        "DoctrineODM",
        "DoctrineORM",
        "DataMapper",
        "JPA",
        "Idiorm",
        "Kohana",
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
EntityAssociation_strategy = st.builds(
    EntityAssociation,
)
persistence_AssociationWithoutContainment_strategy = st.builds(
    persistence_AssociationWithoutContainment,
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
persistence_EncapsulatedFeature_strategy = st.builds(
    persistence_EncapsulatedFeature,
    columnName=
        safe_text,
    alias=
        safe_text,
    displayLabel=
        safe_text
)
persistence_AssociationWithContainment_strategy = st.builds(
    persistence_AssociationWithContainment,
    sourceVisible=
        st.booleans()
)
EntityAttribute_strategy = st.builds(
    EntityAttribute,
)
persistence_DataTypeAttribute_strategy = st.builds(
    persistence_DataTypeAttribute,
    obfuscateFormFields=
        st.booleans(),
    caseInsensitive=
        st.booleans(),
    encrypt=
        st.booleans()
)
persistence_AssociationKey_strategy = st.builds(
    persistence_AssociationKey,
    targetColumnName=
        safe_text
)
Association_strategy = st.builds(
    Association,
)
persistence_LocationAttribute_strategy = st.builds(
    persistence_LocationAttribute,
)
ResourceAttribute_strategy = st.builds(
    ResourceAttribute,
)
persistence_ImageAttribute_strategy = st.builds(
    persistence_ImageAttribute,
)
persistence_FileAttribute_strategy = st.builds(
    persistence_FileAttribute,
)
PathElement_strategy = st.builds(
    PathElement,
)
persistence_DatePathElement_strategy = st.builds(
    persistence_DatePathElement,
    format=
        safe_text
)
persistence_StaticPathElement_strategy = st.builds(
    persistence_StaticPathElement,
    element=
        safe_text
)
persistence_PathElement_strategy = st.builds(
    persistence_PathElement,
)
persistence_ResourceAttribute_strategy = st.builds(
    persistence_ResourceAttribute,
    uploadsWithinWebsite=
        st.booleans(),
    maximumUploadSize=
        st.integers(),
    validUploadMimeTypes=
        safe_text,
    validUploadExtensions=
        safe_text
)
persistence_UrlAttribute_strategy = st.builds(
    persistence_UrlAttribute,
    displayValue=
        safe_text
)
persistence_DateAttribute_strategy = st.builds(
    persistence_DateAttribute,
    format=
        safe_text,
    details=
        safe_text
)
ModelLabelFeature_strategy = st.builds(
    ModelLabelFeature,
)
persistence_ModelLabelAttribute_strategy = st.builds(
    persistence_ModelLabelAttribute,
    dateFormat=
        safe_text
)
Attribute_strategy = st.builds(
    Attribute,
)
persistence_EncapsulatedAttribute_strategy = st.builds(
    persistence_EncapsulatedAttribute,
    name=
        safe_text,
    cardinality=
        safe_text
)
EntityFeature_strategy = st.builds(
    EntityFeature,
)
persistence_EntityAttribute_strategy = st.builds(
    persistence_EntityAttribute,
    persistentType=
        safe_text,
    primaryKey=
        st.booleans(),
    ormType=
        safe_text,
    interfaceType=
        safe_text,
    containerUnique=
        st.booleans()
)
NamedDisplayElement_strategy = st.builds(
    NamedDisplayElement,
)
persistence_ViewAssociation_strategy = st.builds(
    persistence_ViewAssociation,
    cardinality=
        safe_text
)
EntityOrView_strategy = st.builds(
    EntityOrView,
)
persistence_View_strategy = st.builds(
    persistence_View,
)
persistence_Entity_strategy = st.builds(
    persistence_Entity,
)
persistence_EntityAssociation_strategy = st.builds(
    persistence_EntityAssociation,
    targetInputClass=
        safe_text,
    pivotTableName=
        safe_text,
    targetPrimaryKey=
        st.booleans(),
    targetFeatureName=
        safe_text,
    targetHeaderClass=
        safe_text,
    targetDisplayLabel=
        safe_text,
    bidirectional=
        st.booleans(),
    targetDisplayClass=
        safe_text,
    targetFooterClass=
        safe_text
)
persistence_ModelLabelAssociation_strategy = st.builds(
    persistence_ModelLabelAssociation,
    isSourceAssociation=
        st.booleans()
)
persistence_ModelLabelFeature_strategy = st.builds(
    persistence_ModelLabelFeature,
)
persistence_Label_strategy = st.builds(
    persistence_Label,
)
persistence_EncapsulatedAssociation_strategy = st.builds(
    persistence_EncapsulatedAssociation,
    name=
        safe_text,
    isSourceAssociation=
        st.booleans(),
    cardinality=
        safe_text
)
persistence_Expression_strategy = st.builds(
    persistence_Expression,
)
Label_strategy = st.builds(
    Label,
)
Feature_strategy = st.builds(
    Feature,
)
persistence_ViewFeature_strategy = st.builds(
    persistence_ViewFeature,
)
persistence_EntityFeature_strategy = st.builds(
    persistence_EntityFeature,
    singletonName=
        safe_text,
    pluralisedName=
        safe_text,
    columnName=
        safe_text,
    booleanIsHasChoice=
        safe_text,
    ordered=
        st.booleans(),
    unique=
        st.booleans(),
    cardinality=
        safe_text
)
persistence_Association_strategy = st.builds(
    persistence_Association,
    serializationMaxDepth=
        st.integers(),
    pseudo=
        st.booleans(),
    inputClass=
        safe_text
)
persistence_Attribute_strategy = st.builds(
    persistence_Attribute,
    validationPattern=
        safe_text,
    placeholder=
        safe_text,
    inputClass=
        safe_text
)
persistence_Feature_strategy = st.builds(
    persistence_Feature,
    encodeUriKey=
        st.booleans(),
    displayClass=
        safe_text,
    collectionAllowRemove=
        st.booleans(),
    title=
        safe_text,
    collectionAllowAdd=
        st.booleans(),
    headerClass=
        safe_text,
    footerClass=
        safe_text,
    nullDisplayValue=
        safe_text
)
Classifier_strategy = st.builds(
    Classifier,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
persistence_ModelLabel_strategy = st.builds(
    persistence_ModelLabel,
    format=
        safe_text
)
persistence_EntityOrView_strategy = st.builds(
    persistence_EntityOrView,
    autoKeyGenerationStrategy=
        safe_text,
    autoKeyName=
        safe_text,
    pluralisedName=
        safe_text,
    autoKeyPersistentType=
        safe_text,
    implementsUserInterface=
        st.booleans(),
    singletonName=
        safe_text,
    tableName=
        safe_text
)
persistence_DataType_strategy = st.builds(
    persistence_DataType,
)
persistence_SerializationGroup_strategy = st.builds(
    persistence_SerializationGroup,
)
persistence_Persistence_strategy = st.builds(
    persistence_Persistence,
    databaseName=
        safe_text,
    databasePassword=
        safe_text,
    ormTechnology=
        safe_text,
    timestampCreation=
        st.booleans(),
    databaseUsername=
        safe_text,
    databaseHost=
        safe_text,
    databasePrefix=
        safe_text,
    databasePort=
        safe_text,
    databaseTechnology=
        safe_text,
    timestampUpdates=
        st.booleans()
)

@given(instance=EntityAssociation_strategy)
@settings(max_examples=50)
def test_entityassociation_instantiation(instance):
    assert isinstance(instance, EntityAssociation)

@given(instance=persistence_AssociationWithoutContainment_strategy)
@settings(max_examples=50)
def test_persistence_associationwithoutcontainment_instantiation(instance):
    assert isinstance(instance, persistence_AssociationWithoutContainment)



@given(instance=persistence_AssociationWithoutContainment_strategy)
def test_persistence_associationwithoutcontainment_targetUnique_setter(instance):
    original = instance.targetUnique
    instance.targetUnique = original
    assert instance.targetUnique == original



@given(instance=persistence_AssociationWithoutContainment_strategy)
def test_persistence_associationwithoutcontainment_targetCardinality_setter(instance):
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

@given(instance=persistence_EncapsulatedFeature_strategy)
@settings(max_examples=50)
def test_persistence_encapsulatedfeature_instantiation(instance):
    assert isinstance(instance, persistence_EncapsulatedFeature)



@given(instance=persistence_EncapsulatedFeature_strategy)
def test_persistence_encapsulatedfeature_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original



@given(instance=persistence_EncapsulatedFeature_strategy)
def test_persistence_encapsulatedfeature_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original



@given(instance=persistence_EncapsulatedFeature_strategy)
def test_persistence_encapsulatedfeature_displayLabel_setter(instance):
    original = instance.displayLabel
    instance.displayLabel = original
    assert instance.displayLabel == original

@given(instance=persistence_AssociationWithContainment_strategy)
@settings(max_examples=50)
def test_persistence_associationwithcontainment_instantiation(instance):
    assert isinstance(instance, persistence_AssociationWithContainment)



@given(instance=persistence_AssociationWithContainment_strategy)
def test_persistence_associationwithcontainment_sourceVisible_setter(instance):
    original = instance.sourceVisible
    instance.sourceVisible = original
    assert instance.sourceVisible == original

@given(instance=EntityAttribute_strategy)
@settings(max_examples=50)
def test_entityattribute_instantiation(instance):
    assert isinstance(instance, EntityAttribute)

@given(instance=persistence_DataTypeAttribute_strategy)
@settings(max_examples=50)
def test_persistence_datatypeattribute_instantiation(instance):
    assert isinstance(instance, persistence_DataTypeAttribute)



@given(instance=persistence_DataTypeAttribute_strategy)
def test_persistence_datatypeattribute_obfuscateFormFields_setter(instance):
    original = instance.obfuscateFormFields
    instance.obfuscateFormFields = original
    assert instance.obfuscateFormFields == original



@given(instance=persistence_DataTypeAttribute_strategy)
def test_persistence_datatypeattribute_caseInsensitive_setter(instance):
    original = instance.caseInsensitive
    instance.caseInsensitive = original
    assert instance.caseInsensitive == original



@given(instance=persistence_DataTypeAttribute_strategy)
def test_persistence_datatypeattribute_encrypt_setter(instance):
    original = instance.encrypt
    instance.encrypt = original
    assert instance.encrypt == original

@given(instance=persistence_AssociationKey_strategy)
@settings(max_examples=50)
def test_persistence_associationkey_instantiation(instance):
    assert isinstance(instance, persistence_AssociationKey)



@given(instance=persistence_AssociationKey_strategy)
def test_persistence_associationkey_targetColumnName_setter(instance):
    original = instance.targetColumnName
    instance.targetColumnName = original
    assert instance.targetColumnName == original

@given(instance=Association_strategy)
@settings(max_examples=50)
def test_association_instantiation(instance):
    assert isinstance(instance, Association)

@given(instance=persistence_LocationAttribute_strategy)
@settings(max_examples=50)
def test_persistence_locationattribute_instantiation(instance):
    assert isinstance(instance, persistence_LocationAttribute)

@given(instance=ResourceAttribute_strategy)
@settings(max_examples=50)
def test_resourceattribute_instantiation(instance):
    assert isinstance(instance, ResourceAttribute)

@given(instance=persistence_ImageAttribute_strategy)
@settings(max_examples=50)
def test_persistence_imageattribute_instantiation(instance):
    assert isinstance(instance, persistence_ImageAttribute)

@given(instance=persistence_FileAttribute_strategy)
@settings(max_examples=50)
def test_persistence_fileattribute_instantiation(instance):
    assert isinstance(instance, persistence_FileAttribute)

@given(instance=PathElement_strategy)
@settings(max_examples=50)
def test_pathelement_instantiation(instance):
    assert isinstance(instance, PathElement)

@given(instance=persistence_DatePathElement_strategy)
@settings(max_examples=50)
def test_persistence_datepathelement_instantiation(instance):
    assert isinstance(instance, persistence_DatePathElement)



@given(instance=persistence_DatePathElement_strategy)
def test_persistence_datepathelement_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original

@given(instance=persistence_StaticPathElement_strategy)
@settings(max_examples=50)
def test_persistence_staticpathelement_instantiation(instance):
    assert isinstance(instance, persistence_StaticPathElement)



@given(instance=persistence_StaticPathElement_strategy)
def test_persistence_staticpathelement_element_setter(instance):
    original = instance.element
    instance.element = original
    assert instance.element == original

@given(instance=persistence_PathElement_strategy)
@settings(max_examples=50)
def test_persistence_pathelement_instantiation(instance):
    assert isinstance(instance, persistence_PathElement)

@given(instance=persistence_ResourceAttribute_strategy)
@settings(max_examples=50)
def test_persistence_resourceattribute_instantiation(instance):
    assert isinstance(instance, persistence_ResourceAttribute)



@given(instance=persistence_ResourceAttribute_strategy)
def test_persistence_resourceattribute_uploadsWithinWebsite_setter(instance):
    original = instance.uploadsWithinWebsite
    instance.uploadsWithinWebsite = original
    assert instance.uploadsWithinWebsite == original



@given(instance=persistence_ResourceAttribute_strategy)
def test_persistence_resourceattribute_maximumUploadSize_setter(instance):
    original = instance.maximumUploadSize
    instance.maximumUploadSize = original
    assert instance.maximumUploadSize == original



@given(instance=persistence_ResourceAttribute_strategy)
def test_persistence_resourceattribute_validUploadMimeTypes_setter(instance):
    original = instance.validUploadMimeTypes
    instance.validUploadMimeTypes = original
    assert instance.validUploadMimeTypes == original



@given(instance=persistence_ResourceAttribute_strategy)
def test_persistence_resourceattribute_validUploadExtensions_setter(instance):
    original = instance.validUploadExtensions
    instance.validUploadExtensions = original
    assert instance.validUploadExtensions == original

@given(instance=persistence_UrlAttribute_strategy)
@settings(max_examples=50)
def test_persistence_urlattribute_instantiation(instance):
    assert isinstance(instance, persistence_UrlAttribute)



@given(instance=persistence_UrlAttribute_strategy)
def test_persistence_urlattribute_displayValue_setter(instance):
    original = instance.displayValue
    instance.displayValue = original
    assert instance.displayValue == original

@given(instance=persistence_DateAttribute_strategy)
@settings(max_examples=50)
def test_persistence_dateattribute_instantiation(instance):
    assert isinstance(instance, persistence_DateAttribute)



@given(instance=persistence_DateAttribute_strategy)
def test_persistence_dateattribute_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original



@given(instance=persistence_DateAttribute_strategy)
def test_persistence_dateattribute_details_setter(instance):
    original = instance.details
    instance.details = original
    assert instance.details == original

@given(instance=ModelLabelFeature_strategy)
@settings(max_examples=50)
def test_modellabelfeature_instantiation(instance):
    assert isinstance(instance, ModelLabelFeature)

@given(instance=persistence_ModelLabelAttribute_strategy)
@settings(max_examples=50)
def test_persistence_modellabelattribute_instantiation(instance):
    assert isinstance(instance, persistence_ModelLabelAttribute)



@given(instance=persistence_ModelLabelAttribute_strategy)
def test_persistence_modellabelattribute_dateFormat_setter(instance):
    original = instance.dateFormat
    instance.dateFormat = original
    assert instance.dateFormat == original

@given(instance=Attribute_strategy)
@settings(max_examples=50)
def test_attribute_instantiation(instance):
    assert isinstance(instance, Attribute)

@given(instance=persistence_EncapsulatedAttribute_strategy)
@settings(max_examples=50)
def test_persistence_encapsulatedattribute_instantiation(instance):
    assert isinstance(instance, persistence_EncapsulatedAttribute)



@given(instance=persistence_EncapsulatedAttribute_strategy)
def test_persistence_encapsulatedattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=persistence_EncapsulatedAttribute_strategy)
def test_persistence_encapsulatedattribute_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original

@given(instance=EntityFeature_strategy)
@settings(max_examples=50)
def test_entityfeature_instantiation(instance):
    assert isinstance(instance, EntityFeature)

@given(instance=persistence_EntityAttribute_strategy)
@settings(max_examples=50)
def test_persistence_entityattribute_instantiation(instance):
    assert isinstance(instance, persistence_EntityAttribute)



@given(instance=persistence_EntityAttribute_strategy)
def test_persistence_entityattribute_persistentType_setter(instance):
    original = instance.persistentType
    instance.persistentType = original
    assert instance.persistentType == original



@given(instance=persistence_EntityAttribute_strategy)
def test_persistence_entityattribute_primaryKey_setter(instance):
    original = instance.primaryKey
    instance.primaryKey = original
    assert instance.primaryKey == original



@given(instance=persistence_EntityAttribute_strategy)
def test_persistence_entityattribute_ormType_setter(instance):
    original = instance.ormType
    instance.ormType = original
    assert instance.ormType == original



@given(instance=persistence_EntityAttribute_strategy)
def test_persistence_entityattribute_interfaceType_setter(instance):
    original = instance.interfaceType
    instance.interfaceType = original
    assert instance.interfaceType == original



@given(instance=persistence_EntityAttribute_strategy)
def test_persistence_entityattribute_containerUnique_setter(instance):
    original = instance.containerUnique
    instance.containerUnique = original
    assert instance.containerUnique == original

@given(instance=NamedDisplayElement_strategy)
@settings(max_examples=50)
def test_nameddisplayelement_instantiation(instance):
    assert isinstance(instance, NamedDisplayElement)

@given(instance=persistence_ViewAssociation_strategy)
@settings(max_examples=50)
def test_persistence_viewassociation_instantiation(instance):
    assert isinstance(instance, persistence_ViewAssociation)



@given(instance=persistence_ViewAssociation_strategy)
def test_persistence_viewassociation_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original

@given(instance=EntityOrView_strategy)
@settings(max_examples=50)
def test_entityorview_instantiation(instance):
    assert isinstance(instance, EntityOrView)

@given(instance=persistence_View_strategy)
@settings(max_examples=50)
def test_persistence_view_instantiation(instance):
    assert isinstance(instance, persistence_View)

@given(instance=persistence_Entity_strategy)
@settings(max_examples=50)
def test_persistence_entity_instantiation(instance):
    assert isinstance(instance, persistence_Entity)

@given(instance=persistence_EntityAssociation_strategy)
@settings(max_examples=50)
def test_persistence_entityassociation_instantiation(instance):
    assert isinstance(instance, persistence_EntityAssociation)



@given(instance=persistence_EntityAssociation_strategy)
def test_persistence_entityassociation_targetInputClass_setter(instance):
    original = instance.targetInputClass
    instance.targetInputClass = original
    assert instance.targetInputClass == original



@given(instance=persistence_EntityAssociation_strategy)
def test_persistence_entityassociation_pivotTableName_setter(instance):
    original = instance.pivotTableName
    instance.pivotTableName = original
    assert instance.pivotTableName == original



@given(instance=persistence_EntityAssociation_strategy)
def test_persistence_entityassociation_targetPrimaryKey_setter(instance):
    original = instance.targetPrimaryKey
    instance.targetPrimaryKey = original
    assert instance.targetPrimaryKey == original



@given(instance=persistence_EntityAssociation_strategy)
def test_persistence_entityassociation_targetFeatureName_setter(instance):
    original = instance.targetFeatureName
    instance.targetFeatureName = original
    assert instance.targetFeatureName == original



@given(instance=persistence_EntityAssociation_strategy)
def test_persistence_entityassociation_targetHeaderClass_setter(instance):
    original = instance.targetHeaderClass
    instance.targetHeaderClass = original
    assert instance.targetHeaderClass == original



@given(instance=persistence_EntityAssociation_strategy)
def test_persistence_entityassociation_targetDisplayLabel_setter(instance):
    original = instance.targetDisplayLabel
    instance.targetDisplayLabel = original
    assert instance.targetDisplayLabel == original



@given(instance=persistence_EntityAssociation_strategy)
def test_persistence_entityassociation_bidirectional_setter(instance):
    original = instance.bidirectional
    instance.bidirectional = original
    assert instance.bidirectional == original



@given(instance=persistence_EntityAssociation_strategy)
def test_persistence_entityassociation_targetDisplayClass_setter(instance):
    original = instance.targetDisplayClass
    instance.targetDisplayClass = original
    assert instance.targetDisplayClass == original



@given(instance=persistence_EntityAssociation_strategy)
def test_persistence_entityassociation_targetFooterClass_setter(instance):
    original = instance.targetFooterClass
    instance.targetFooterClass = original
    assert instance.targetFooterClass == original

@given(instance=persistence_ModelLabelAssociation_strategy)
@settings(max_examples=50)
def test_persistence_modellabelassociation_instantiation(instance):
    assert isinstance(instance, persistence_ModelLabelAssociation)



@given(instance=persistence_ModelLabelAssociation_strategy)
def test_persistence_modellabelassociation_isSourceAssociation_setter(instance):
    original = instance.isSourceAssociation
    instance.isSourceAssociation = original
    assert instance.isSourceAssociation == original

@given(instance=persistence_ModelLabelFeature_strategy)
@settings(max_examples=50)
def test_persistence_modellabelfeature_instantiation(instance):
    assert isinstance(instance, persistence_ModelLabelFeature)

@given(instance=persistence_Label_strategy)
@settings(max_examples=50)
def test_persistence_label_instantiation(instance):
    assert isinstance(instance, persistence_Label)

@given(instance=persistence_EncapsulatedAssociation_strategy)
@settings(max_examples=50)
def test_persistence_encapsulatedassociation_instantiation(instance):
    assert isinstance(instance, persistence_EncapsulatedAssociation)



@given(instance=persistence_EncapsulatedAssociation_strategy)
def test_persistence_encapsulatedassociation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=persistence_EncapsulatedAssociation_strategy)
def test_persistence_encapsulatedassociation_isSourceAssociation_setter(instance):
    original = instance.isSourceAssociation
    instance.isSourceAssociation = original
    assert instance.isSourceAssociation == original



@given(instance=persistence_EncapsulatedAssociation_strategy)
def test_persistence_encapsulatedassociation_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original

@given(instance=persistence_Expression_strategy)
@settings(max_examples=50)
def test_persistence_expression_instantiation(instance):
    assert isinstance(instance, persistence_Expression)

@given(instance=Label_strategy)
@settings(max_examples=50)
def test_label_instantiation(instance):
    assert isinstance(instance, Label)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=persistence_ViewFeature_strategy)
@settings(max_examples=50)
def test_persistence_viewfeature_instantiation(instance):
    assert isinstance(instance, persistence_ViewFeature)

@given(instance=persistence_EntityFeature_strategy)
@settings(max_examples=50)
def test_persistence_entityfeature_instantiation(instance):
    assert isinstance(instance, persistence_EntityFeature)



@given(instance=persistence_EntityFeature_strategy)
def test_persistence_entityfeature_singletonName_setter(instance):
    original = instance.singletonName
    instance.singletonName = original
    assert instance.singletonName == original



@given(instance=persistence_EntityFeature_strategy)
def test_persistence_entityfeature_pluralisedName_setter(instance):
    original = instance.pluralisedName
    instance.pluralisedName = original
    assert instance.pluralisedName == original



@given(instance=persistence_EntityFeature_strategy)
def test_persistence_entityfeature_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original



@given(instance=persistence_EntityFeature_strategy)
def test_persistence_entityfeature_booleanIsHasChoice_setter(instance):
    original = instance.booleanIsHasChoice
    instance.booleanIsHasChoice = original
    assert instance.booleanIsHasChoice == original



@given(instance=persistence_EntityFeature_strategy)
def test_persistence_entityfeature_ordered_setter(instance):
    original = instance.ordered
    instance.ordered = original
    assert instance.ordered == original



@given(instance=persistence_EntityFeature_strategy)
def test_persistence_entityfeature_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original



@given(instance=persistence_EntityFeature_strategy)
def test_persistence_entityfeature_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original

@given(instance=persistence_Association_strategy)
@settings(max_examples=50)
def test_persistence_association_instantiation(instance):
    assert isinstance(instance, persistence_Association)



@given(instance=persistence_Association_strategy)
def test_persistence_association_serializationMaxDepth_setter(instance):
    original = instance.serializationMaxDepth
    instance.serializationMaxDepth = original
    assert instance.serializationMaxDepth == original



@given(instance=persistence_Association_strategy)
def test_persistence_association_pseudo_setter(instance):
    original = instance.pseudo
    instance.pseudo = original
    assert instance.pseudo == original



@given(instance=persistence_Association_strategy)
def test_persistence_association_inputClass_setter(instance):
    original = instance.inputClass
    instance.inputClass = original
    assert instance.inputClass == original

@given(instance=persistence_Attribute_strategy)
@settings(max_examples=50)
def test_persistence_attribute_instantiation(instance):
    assert isinstance(instance, persistence_Attribute)



@given(instance=persistence_Attribute_strategy)
def test_persistence_attribute_validationPattern_setter(instance):
    original = instance.validationPattern
    instance.validationPattern = original
    assert instance.validationPattern == original



@given(instance=persistence_Attribute_strategy)
def test_persistence_attribute_placeholder_setter(instance):
    original = instance.placeholder
    instance.placeholder = original
    assert instance.placeholder == original



@given(instance=persistence_Attribute_strategy)
def test_persistence_attribute_inputClass_setter(instance):
    original = instance.inputClass
    instance.inputClass = original
    assert instance.inputClass == original

@given(instance=persistence_Feature_strategy)
@settings(max_examples=50)
def test_persistence_feature_instantiation(instance):
    assert isinstance(instance, persistence_Feature)



@given(instance=persistence_Feature_strategy)
def test_persistence_feature_encodeUriKey_setter(instance):
    original = instance.encodeUriKey
    instance.encodeUriKey = original
    assert instance.encodeUriKey == original



@given(instance=persistence_Feature_strategy)
def test_persistence_feature_displayClass_setter(instance):
    original = instance.displayClass
    instance.displayClass = original
    assert instance.displayClass == original



@given(instance=persistence_Feature_strategy)
def test_persistence_feature_collectionAllowRemove_setter(instance):
    original = instance.collectionAllowRemove
    instance.collectionAllowRemove = original
    assert instance.collectionAllowRemove == original



@given(instance=persistence_Feature_strategy)
def test_persistence_feature_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=persistence_Feature_strategy)
def test_persistence_feature_collectionAllowAdd_setter(instance):
    original = instance.collectionAllowAdd
    instance.collectionAllowAdd = original
    assert instance.collectionAllowAdd == original



@given(instance=persistence_Feature_strategy)
def test_persistence_feature_headerClass_setter(instance):
    original = instance.headerClass
    instance.headerClass = original
    assert instance.headerClass == original



@given(instance=persistence_Feature_strategy)
def test_persistence_feature_footerClass_setter(instance):
    original = instance.footerClass
    instance.footerClass = original
    assert instance.footerClass == original



@given(instance=persistence_Feature_strategy)
def test_persistence_feature_nullDisplayValue_setter(instance):
    original = instance.nullDisplayValue
    instance.nullDisplayValue = original
    assert instance.nullDisplayValue == original

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=persistence_ModelLabel_strategy)
@settings(max_examples=50)
def test_persistence_modellabel_instantiation(instance):
    assert isinstance(instance, persistence_ModelLabel)



@given(instance=persistence_ModelLabel_strategy)
def test_persistence_modellabel_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original

@given(instance=persistence_EntityOrView_strategy)
@settings(max_examples=50)
def test_persistence_entityorview_instantiation(instance):
    assert isinstance(instance, persistence_EntityOrView)



@given(instance=persistence_EntityOrView_strategy)
def test_persistence_entityorview_autoKeyGenerationStrategy_setter(instance):
    original = instance.autoKeyGenerationStrategy
    instance.autoKeyGenerationStrategy = original
    assert instance.autoKeyGenerationStrategy == original



@given(instance=persistence_EntityOrView_strategy)
def test_persistence_entityorview_autoKeyName_setter(instance):
    original = instance.autoKeyName
    instance.autoKeyName = original
    assert instance.autoKeyName == original



@given(instance=persistence_EntityOrView_strategy)
def test_persistence_entityorview_pluralisedName_setter(instance):
    original = instance.pluralisedName
    instance.pluralisedName = original
    assert instance.pluralisedName == original



@given(instance=persistence_EntityOrView_strategy)
def test_persistence_entityorview_autoKeyPersistentType_setter(instance):
    original = instance.autoKeyPersistentType
    instance.autoKeyPersistentType = original
    assert instance.autoKeyPersistentType == original



@given(instance=persistence_EntityOrView_strategy)
def test_persistence_entityorview_implementsUserInterface_setter(instance):
    original = instance.implementsUserInterface
    instance.implementsUserInterface = original
    assert instance.implementsUserInterface == original



@given(instance=persistence_EntityOrView_strategy)
def test_persistence_entityorview_singletonName_setter(instance):
    original = instance.singletonName
    instance.singletonName = original
    assert instance.singletonName == original



@given(instance=persistence_EntityOrView_strategy)
def test_persistence_entityorview_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original

@given(instance=persistence_DataType_strategy)
@settings(max_examples=50)
def test_persistence_datatype_instantiation(instance):
    assert isinstance(instance, persistence_DataType)

@given(instance=persistence_SerializationGroup_strategy)
@settings(max_examples=50)
def test_persistence_serializationgroup_instantiation(instance):
    assert isinstance(instance, persistence_SerializationGroup)

@given(instance=persistence_Persistence_strategy)
@settings(max_examples=50)
def test_persistence_persistence_instantiation(instance):
    assert isinstance(instance, persistence_Persistence)



@given(instance=persistence_Persistence_strategy)
def test_persistence_persistence_databaseName_setter(instance):
    original = instance.databaseName
    instance.databaseName = original
    assert instance.databaseName == original



@given(instance=persistence_Persistence_strategy)
def test_persistence_persistence_databasePassword_setter(instance):
    original = instance.databasePassword
    instance.databasePassword = original
    assert instance.databasePassword == original



@given(instance=persistence_Persistence_strategy)
def test_persistence_persistence_ormTechnology_setter(instance):
    original = instance.ormTechnology
    instance.ormTechnology = original
    assert instance.ormTechnology == original



@given(instance=persistence_Persistence_strategy)
def test_persistence_persistence_timestampCreation_setter(instance):
    original = instance.timestampCreation
    instance.timestampCreation = original
    assert instance.timestampCreation == original



@given(instance=persistence_Persistence_strategy)
def test_persistence_persistence_databaseUsername_setter(instance):
    original = instance.databaseUsername
    instance.databaseUsername = original
    assert instance.databaseUsername == original



@given(instance=persistence_Persistence_strategy)
def test_persistence_persistence_databaseHost_setter(instance):
    original = instance.databaseHost
    instance.databaseHost = original
    assert instance.databaseHost == original



@given(instance=persistence_Persistence_strategy)
def test_persistence_persistence_databasePrefix_setter(instance):
    original = instance.databasePrefix
    instance.databasePrefix = original
    assert instance.databasePrefix == original



@given(instance=persistence_Persistence_strategy)
def test_persistence_persistence_databasePort_setter(instance):
    original = instance.databasePort
    instance.databasePort = original
    assert instance.databasePort == original



@given(instance=persistence_Persistence_strategy)
def test_persistence_persistence_databaseTechnology_setter(instance):
    original = instance.databaseTechnology
    instance.databaseTechnology = original
    assert instance.databaseTechnology == original



@given(instance=persistence_Persistence_strategy)
def test_persistence_persistence_timestampUpdates_setter(instance):
    original = instance.timestampUpdates
    instance.timestampUpdates = original
    assert instance.timestampUpdates == original
