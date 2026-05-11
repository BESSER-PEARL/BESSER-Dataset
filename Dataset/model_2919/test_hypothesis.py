import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Association,
    persistence::AssociationWithContainment,
    persistence::AssociationWithoutContainment,
    ResourceAttribute,
    persistence::ImageAttribute,
    persistence::FileAttribute,
    PathElement,
    persistence::DatePathElement,
    persistence::StaticPathElement,
    Attribute,
    persistence::LocationAttribute,
    persistence::UrlAttribute,
    persistence::DateAttribute,
    persistence::ResourceAttribute,
    persistence::DataTypeAttribute,
    persistence::PathElement,
    Classifier,
    ModelLabelFeature,
    persistence::ModelLabelAssociation,
    persistence::ModelLabelAttribute,
    persistence::ModelLabelFeature,
    persistence::Label,
    persistence::Expression,
    Label,
    Feature,
    persistence::Attribute,
    NamedDisplayElement,
    persistence::AssociationKey,
    persistence::Association,
    NamedElement,
    persistence::ModelLabel,
    persistence::Entity,
    persistence::DataType,
    persistence::SerializationGroup,
    persistence::Persistence,
    persistence::Feature,
    isHasChoices,
    Cardinality,
    OrmTechnologies,
    DateDetails,
    DatabaseTechnologies,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_association_is_not_abstract():
    assert not inspect.isabstract(Association)


def test_association_constructor_exists():
    assert callable(Association.__init__)


def test_association_constructor_args():
    sig = inspect.signature(Association.__init__)
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
    assert "targetUnique" in params, "Missing parameter 'targetUnique'"
    assert "targetCardinality" in params, "Missing parameter 'targetCardinality'"

def test_persistence::associationwithoutcontainment_has_targetUnique():
    assert hasattr(persistence::AssociationWithoutContainment, "targetUnique")
    descriptor = None
    for klass in persistence::AssociationWithoutContainment.__mro__:
        if "targetUnique" in klass.__dict__:
            descriptor = klass.__dict__["targetUnique"]
            break
    assert isinstance(descriptor, property)

def test_persistence::associationwithoutcontainment_has_targetCardinality():
    assert hasattr(persistence::AssociationWithoutContainment, "targetCardinality")
    descriptor = None
    for klass in persistence::AssociationWithoutContainment.__mro__:
        if "targetCardinality" in klass.__dict__:
            descriptor = klass.__dict__["targetCardinality"]
            break
    assert isinstance(descriptor, property)



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



def test_attribute_is_not_abstract():
    assert not inspect.isabstract(Attribute)


def test_attribute_constructor_exists():
    assert callable(Attribute.__init__)


def test_attribute_constructor_args():
    sig = inspect.signature(Attribute.__init__)
    params = list(sig.parameters.keys())



def test_persistence::locationattribute_is_not_abstract():
    assert not inspect.isabstract(persistence::LocationAttribute)


def test_persistence::locationattribute_constructor_exists():
    assert callable(persistence::LocationAttribute.__init__)


def test_persistence::locationattribute_constructor_args():
    sig = inspect.signature(persistence::LocationAttribute.__init__)
    params = list(sig.parameters.keys())



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



def test_persistence::dateattribute_is_not_abstract():
    assert not inspect.isabstract(persistence::DateAttribute)


def test_persistence::dateattribute_constructor_exists():
    assert callable(persistence::DateAttribute.__init__)


def test_persistence::dateattribute_constructor_args():
    sig = inspect.signature(persistence::DateAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "format" in params, "Missing parameter 'format'"
    assert "details" in params, "Missing parameter 'details'"

def test_persistence::dateattribute_has_format():
    assert hasattr(persistence::DateAttribute, "format")
    descriptor = None
    for klass in persistence::DateAttribute.__mro__:
        if "format" in klass.__dict__:
            descriptor = klass.__dict__["format"]
            break
    assert isinstance(descriptor, property)

def test_persistence::dateattribute_has_details():
    assert hasattr(persistence::DateAttribute, "details")
    descriptor = None
    for klass in persistence::DateAttribute.__mro__:
        if "details" in klass.__dict__:
            descriptor = klass.__dict__["details"]
            break
    assert isinstance(descriptor, property)



def test_persistence::resourceattribute_is_not_abstract():
    assert not inspect.isabstract(persistence::ResourceAttribute)


def test_persistence::resourceattribute_constructor_exists():
    assert callable(persistence::ResourceAttribute.__init__)


def test_persistence::resourceattribute_constructor_args():
    sig = inspect.signature(persistence::ResourceAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "uploadsWithinWebsite" in params, "Missing parameter 'uploadsWithinWebsite'"
    assert "validUploadExtensions" in params, "Missing parameter 'validUploadExtensions'"
    assert "maximumUploadSize" in params, "Missing parameter 'maximumUploadSize'"
    assert "validUploadMimeTypes" in params, "Missing parameter 'validUploadMimeTypes'"

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

def test_persistence::resourceattribute_has_maximumUploadSize():
    assert hasattr(persistence::ResourceAttribute, "maximumUploadSize")
    descriptor = None
    for klass in persistence::ResourceAttribute.__mro__:
        if "maximumUploadSize" in klass.__dict__:
            descriptor = klass.__dict__["maximumUploadSize"]
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



def test_persistence::datatypeattribute_is_not_abstract():
    assert not inspect.isabstract(persistence::DataTypeAttribute)


def test_persistence::datatypeattribute_constructor_exists():
    assert callable(persistence::DataTypeAttribute.__init__)


def test_persistence::datatypeattribute_constructor_args():
    sig = inspect.signature(persistence::DataTypeAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "obfuscateFormFields" in params, "Missing parameter 'obfuscateFormFields'"
    assert "caseInsensitive" in params, "Missing parameter 'caseInsensitive'"
    assert "encrypt" in params, "Missing parameter 'encrypt'"

def test_persistence::datatypeattribute_has_obfuscateFormFields():
    assert hasattr(persistence::DataTypeAttribute, "obfuscateFormFields")
    descriptor = None
    for klass in persistence::DataTypeAttribute.__mro__:
        if "obfuscateFormFields" in klass.__dict__:
            descriptor = klass.__dict__["obfuscateFormFields"]
            break
    assert isinstance(descriptor, property)

def test_persistence::datatypeattribute_has_caseInsensitive():
    assert hasattr(persistence::DataTypeAttribute, "caseInsensitive")
    descriptor = None
    for klass in persistence::DataTypeAttribute.__mro__:
        if "caseInsensitive" in klass.__dict__:
            descriptor = klass.__dict__["caseInsensitive"]
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



def test_persistence::pathelement_is_not_abstract():
    assert not inspect.isabstract(persistence::PathElement)


def test_persistence::pathelement_constructor_exists():
    assert callable(persistence::PathElement.__init__)


def test_persistence::pathelement_constructor_args():
    sig = inspect.signature(persistence::PathElement.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



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



def test_persistence::attribute_is_not_abstract():
    assert not inspect.isabstract(persistence::Attribute)


def test_persistence::attribute_constructor_exists():
    assert callable(persistence::Attribute.__init__)


def test_persistence::attribute_constructor_args():
    sig = inspect.signature(persistence::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "validationPattern" in params, "Missing parameter 'validationPattern'"
    assert "persistentType" in params, "Missing parameter 'persistentType'"
    assert "interfaceType" in params, "Missing parameter 'interfaceType'"
    assert "unique" in params, "Missing parameter 'unique'"
    assert "inputElementClass" in params, "Missing parameter 'inputElementClass'"
    assert "containerUnique" in params, "Missing parameter 'containerUnique'"
    assert "ormType" in params, "Missing parameter 'ormType'"
    assert "placeholder" in params, "Missing parameter 'placeholder'"
    assert "inputColumnClass" in params, "Missing parameter 'inputColumnClass'"
    assert "hidden" in params, "Missing parameter 'hidden'"

def test_persistence::attribute_has_validationPattern():
    assert hasattr(persistence::Attribute, "validationPattern")
    descriptor = None
    for klass in persistence::Attribute.__mro__:
        if "validationPattern" in klass.__dict__:
            descriptor = klass.__dict__["validationPattern"]
            break
    assert isinstance(descriptor, property)

def test_persistence::attribute_has_persistentType():
    assert hasattr(persistence::Attribute, "persistentType")
    descriptor = None
    for klass in persistence::Attribute.__mro__:
        if "persistentType" in klass.__dict__:
            descriptor = klass.__dict__["persistentType"]
            break
    assert isinstance(descriptor, property)

def test_persistence::attribute_has_interfaceType():
    assert hasattr(persistence::Attribute, "interfaceType")
    descriptor = None
    for klass in persistence::Attribute.__mro__:
        if "interfaceType" in klass.__dict__:
            descriptor = klass.__dict__["interfaceType"]
            break
    assert isinstance(descriptor, property)

def test_persistence::attribute_has_unique():
    assert hasattr(persistence::Attribute, "unique")
    descriptor = None
    for klass in persistence::Attribute.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)

def test_persistence::attribute_has_inputElementClass():
    assert hasattr(persistence::Attribute, "inputElementClass")
    descriptor = None
    for klass in persistence::Attribute.__mro__:
        if "inputElementClass" in klass.__dict__:
            descriptor = klass.__dict__["inputElementClass"]
            break
    assert isinstance(descriptor, property)

def test_persistence::attribute_has_containerUnique():
    assert hasattr(persistence::Attribute, "containerUnique")
    descriptor = None
    for klass in persistence::Attribute.__mro__:
        if "containerUnique" in klass.__dict__:
            descriptor = klass.__dict__["containerUnique"]
            break
    assert isinstance(descriptor, property)

def test_persistence::attribute_has_ormType():
    assert hasattr(persistence::Attribute, "ormType")
    descriptor = None
    for klass in persistence::Attribute.__mro__:
        if "ormType" in klass.__dict__:
            descriptor = klass.__dict__["ormType"]
            break
    assert isinstance(descriptor, property)

def test_persistence::attribute_has_placeholder():
    assert hasattr(persistence::Attribute, "placeholder")
    descriptor = None
    for klass in persistence::Attribute.__mro__:
        if "placeholder" in klass.__dict__:
            descriptor = klass.__dict__["placeholder"]
            break
    assert isinstance(descriptor, property)

def test_persistence::attribute_has_inputColumnClass():
    assert hasattr(persistence::Attribute, "inputColumnClass")
    descriptor = None
    for klass in persistence::Attribute.__mro__:
        if "inputColumnClass" in klass.__dict__:
            descriptor = klass.__dict__["inputColumnClass"]
            break
    assert isinstance(descriptor, property)

def test_persistence::attribute_has_hidden():
    assert hasattr(persistence::Attribute, "hidden")
    descriptor = None
    for klass in persistence::Attribute.__mro__:
        if "hidden" in klass.__dict__:
            descriptor = klass.__dict__["hidden"]
            break
    assert isinstance(descriptor, property)



def test_nameddisplayelement_is_not_abstract():
    assert not inspect.isabstract(NamedDisplayElement)


def test_nameddisplayelement_constructor_exists():
    assert callable(NamedDisplayElement.__init__)


def test_nameddisplayelement_constructor_args():
    sig = inspect.signature(NamedDisplayElement.__init__)
    params = list(sig.parameters.keys())



def test_persistence::associationkey_is_not_abstract():
    assert not inspect.isabstract(persistence::AssociationKey)


def test_persistence::associationkey_constructor_exists():
    assert callable(persistence::AssociationKey.__init__)


def test_persistence::associationkey_constructor_args():
    sig = inspect.signature(persistence::AssociationKey.__init__)
    params = list(sig.parameters.keys())



def test_persistence::association_is_not_abstract():
    assert not inspect.isabstract(persistence::Association)


def test_persistence::association_constructor_exists():
    assert callable(persistence::Association.__init__)


def test_persistence::association_constructor_args():
    sig = inspect.signature(persistence::Association.__init__)
    params = list(sig.parameters.keys())
    assert "serializationMaxDepth" in params, "Missing parameter 'serializationMaxDepth'"
    assert "pivotTableName" in params, "Missing parameter 'pivotTableName'"
    assert "targetPrimaryKey" in params, "Missing parameter 'targetPrimaryKey'"
    assert "targetInputClass" in params, "Missing parameter 'targetInputClass'"
    assert "bidirectional" in params, "Missing parameter 'bidirectional'"
    assert "targetFeatureName" in params, "Missing parameter 'targetFeatureName'"
    assert "targetColumnName" in params, "Missing parameter 'targetColumnName'"
    assert "unique" in params, "Missing parameter 'unique'"
    assert "inputColumnClass" in params, "Missing parameter 'inputColumnClass'"
    assert "targetDisplayLabel" in params, "Missing parameter 'targetDisplayLabel'"
    assert "targetHeaderClass" in params, "Missing parameter 'targetHeaderClass'"
    assert "pseudo" in params, "Missing parameter 'pseudo'"
    assert "targetDisplayClass" in params, "Missing parameter 'targetDisplayClass'"
    assert "targetFooterClass" in params, "Missing parameter 'targetFooterClass'"
    assert "inputElementClass" in params, "Missing parameter 'inputElementClass'"

def test_persistence::association_has_serializationMaxDepth():
    assert hasattr(persistence::Association, "serializationMaxDepth")
    descriptor = None
    for klass in persistence::Association.__mro__:
        if "serializationMaxDepth" in klass.__dict__:
            descriptor = klass.__dict__["serializationMaxDepth"]
            break
    assert isinstance(descriptor, property)

def test_persistence::association_has_pivotTableName():
    assert hasattr(persistence::Association, "pivotTableName")
    descriptor = None
    for klass in persistence::Association.__mro__:
        if "pivotTableName" in klass.__dict__:
            descriptor = klass.__dict__["pivotTableName"]
            break
    assert isinstance(descriptor, property)

def test_persistence::association_has_targetPrimaryKey():
    assert hasattr(persistence::Association, "targetPrimaryKey")
    descriptor = None
    for klass in persistence::Association.__mro__:
        if "targetPrimaryKey" in klass.__dict__:
            descriptor = klass.__dict__["targetPrimaryKey"]
            break
    assert isinstance(descriptor, property)

def test_persistence::association_has_targetInputClass():
    assert hasattr(persistence::Association, "targetInputClass")
    descriptor = None
    for klass in persistence::Association.__mro__:
        if "targetInputClass" in klass.__dict__:
            descriptor = klass.__dict__["targetInputClass"]
            break
    assert isinstance(descriptor, property)

def test_persistence::association_has_bidirectional():
    assert hasattr(persistence::Association, "bidirectional")
    descriptor = None
    for klass in persistence::Association.__mro__:
        if "bidirectional" in klass.__dict__:
            descriptor = klass.__dict__["bidirectional"]
            break
    assert isinstance(descriptor, property)

def test_persistence::association_has_targetFeatureName():
    assert hasattr(persistence::Association, "targetFeatureName")
    descriptor = None
    for klass in persistence::Association.__mro__:
        if "targetFeatureName" in klass.__dict__:
            descriptor = klass.__dict__["targetFeatureName"]
            break
    assert isinstance(descriptor, property)

def test_persistence::association_has_targetColumnName():
    assert hasattr(persistence::Association, "targetColumnName")
    descriptor = None
    for klass in persistence::Association.__mro__:
        if "targetColumnName" in klass.__dict__:
            descriptor = klass.__dict__["targetColumnName"]
            break
    assert isinstance(descriptor, property)

def test_persistence::association_has_unique():
    assert hasattr(persistence::Association, "unique")
    descriptor = None
    for klass in persistence::Association.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)

def test_persistence::association_has_inputColumnClass():
    assert hasattr(persistence::Association, "inputColumnClass")
    descriptor = None
    for klass in persistence::Association.__mro__:
        if "inputColumnClass" in klass.__dict__:
            descriptor = klass.__dict__["inputColumnClass"]
            break
    assert isinstance(descriptor, property)

def test_persistence::association_has_targetDisplayLabel():
    assert hasattr(persistence::Association, "targetDisplayLabel")
    descriptor = None
    for klass in persistence::Association.__mro__:
        if "targetDisplayLabel" in klass.__dict__:
            descriptor = klass.__dict__["targetDisplayLabel"]
            break
    assert isinstance(descriptor, property)

def test_persistence::association_has_targetHeaderClass():
    assert hasattr(persistence::Association, "targetHeaderClass")
    descriptor = None
    for klass in persistence::Association.__mro__:
        if "targetHeaderClass" in klass.__dict__:
            descriptor = klass.__dict__["targetHeaderClass"]
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

def test_persistence::association_has_targetDisplayClass():
    assert hasattr(persistence::Association, "targetDisplayClass")
    descriptor = None
    for klass in persistence::Association.__mro__:
        if "targetDisplayClass" in klass.__dict__:
            descriptor = klass.__dict__["targetDisplayClass"]
            break
    assert isinstance(descriptor, property)

def test_persistence::association_has_targetFooterClass():
    assert hasattr(persistence::Association, "targetFooterClass")
    descriptor = None
    for klass in persistence::Association.__mro__:
        if "targetFooterClass" in klass.__dict__:
            descriptor = klass.__dict__["targetFooterClass"]
            break
    assert isinstance(descriptor, property)

def test_persistence::association_has_inputElementClass():
    assert hasattr(persistence::Association, "inputElementClass")
    descriptor = None
    for klass in persistence::Association.__mro__:
        if "inputElementClass" in klass.__dict__:
            descriptor = klass.__dict__["inputElementClass"]
            break
    assert isinstance(descriptor, property)



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



def test_persistence::entity_is_not_abstract():
    assert not inspect.isabstract(persistence::Entity)


def test_persistence::entity_constructor_exists():
    assert callable(persistence::Entity.__init__)


def test_persistence::entity_constructor_args():
    sig = inspect.signature(persistence::Entity.__init__)
    params = list(sig.parameters.keys())
    assert "singletonName" in params, "Missing parameter 'singletonName'"
    assert "autoKeyName" in params, "Missing parameter 'autoKeyName'"
    assert "tableName" in params, "Missing parameter 'tableName'"
    assert "autoKeyPersistentType" in params, "Missing parameter 'autoKeyPersistentType'"
    assert "autoKeyGenerationStrategy" in params, "Missing parameter 'autoKeyGenerationStrategy'"
    assert "implementsUserInterface" in params, "Missing parameter 'implementsUserInterface'"
    assert "pluralisedName" in params, "Missing parameter 'pluralisedName'"
    assert "allowFormTypeCustomisation" in params, "Missing parameter 'allowFormTypeCustomisation'"

def test_persistence::entity_has_singletonName():
    assert hasattr(persistence::Entity, "singletonName")
    descriptor = None
    for klass in persistence::Entity.__mro__:
        if "singletonName" in klass.__dict__:
            descriptor = klass.__dict__["singletonName"]
            break
    assert isinstance(descriptor, property)

def test_persistence::entity_has_autoKeyName():
    assert hasattr(persistence::Entity, "autoKeyName")
    descriptor = None
    for klass in persistence::Entity.__mro__:
        if "autoKeyName" in klass.__dict__:
            descriptor = klass.__dict__["autoKeyName"]
            break
    assert isinstance(descriptor, property)

def test_persistence::entity_has_tableName():
    assert hasattr(persistence::Entity, "tableName")
    descriptor = None
    for klass in persistence::Entity.__mro__:
        if "tableName" in klass.__dict__:
            descriptor = klass.__dict__["tableName"]
            break
    assert isinstance(descriptor, property)

def test_persistence::entity_has_autoKeyPersistentType():
    assert hasattr(persistence::Entity, "autoKeyPersistentType")
    descriptor = None
    for klass in persistence::Entity.__mro__:
        if "autoKeyPersistentType" in klass.__dict__:
            descriptor = klass.__dict__["autoKeyPersistentType"]
            break
    assert isinstance(descriptor, property)

def test_persistence::entity_has_autoKeyGenerationStrategy():
    assert hasattr(persistence::Entity, "autoKeyGenerationStrategy")
    descriptor = None
    for klass in persistence::Entity.__mro__:
        if "autoKeyGenerationStrategy" in klass.__dict__:
            descriptor = klass.__dict__["autoKeyGenerationStrategy"]
            break
    assert isinstance(descriptor, property)

def test_persistence::entity_has_implementsUserInterface():
    assert hasattr(persistence::Entity, "implementsUserInterface")
    descriptor = None
    for klass in persistence::Entity.__mro__:
        if "implementsUserInterface" in klass.__dict__:
            descriptor = klass.__dict__["implementsUserInterface"]
            break
    assert isinstance(descriptor, property)

def test_persistence::entity_has_pluralisedName():
    assert hasattr(persistence::Entity, "pluralisedName")
    descriptor = None
    for klass in persistence::Entity.__mro__:
        if "pluralisedName" in klass.__dict__:
            descriptor = klass.__dict__["pluralisedName"]
            break
    assert isinstance(descriptor, property)

def test_persistence::entity_has_allowFormTypeCustomisation():
    assert hasattr(persistence::Entity, "allowFormTypeCustomisation")
    descriptor = None
    for klass in persistence::Entity.__mro__:
        if "allowFormTypeCustomisation" in klass.__dict__:
            descriptor = klass.__dict__["allowFormTypeCustomisation"]
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
    assert "ormTechnology" in params, "Missing parameter 'ormTechnology'"
    assert "timestampUpdates" in params, "Missing parameter 'timestampUpdates'"
    assert "databaseTechnology" in params, "Missing parameter 'databaseTechnology'"
    assert "timestampCreation" in params, "Missing parameter 'timestampCreation'"

def test_persistence::persistence_has_ormTechnology():
    assert hasattr(persistence::Persistence, "ormTechnology")
    descriptor = None
    for klass in persistence::Persistence.__mro__:
        if "ormTechnology" in klass.__dict__:
            descriptor = klass.__dict__["ormTechnology"]
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

def test_persistence::persistence_has_databaseTechnology():
    assert hasattr(persistence::Persistence, "databaseTechnology")
    descriptor = None
    for klass in persistence::Persistence.__mro__:
        if "databaseTechnology" in klass.__dict__:
            descriptor = klass.__dict__["databaseTechnology"]
            break
    assert isinstance(descriptor, property)

def test_persistence::persistence_has_timestampCreation():
    assert hasattr(persistence::Persistence, "timestampCreation")
    descriptor = None
    for klass in persistence::Persistence.__mro__:
        if "timestampCreation" in klass.__dict__:
            descriptor = klass.__dict__["timestampCreation"]
            break
    assert isinstance(descriptor, property)



def test_persistence::feature_is_not_abstract():
    assert not inspect.isabstract(persistence::Feature)


def test_persistence::feature_constructor_exists():
    assert callable(persistence::Feature.__init__)


def test_persistence::feature_constructor_args():
    sig = inspect.signature(persistence::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "cardinality" in params, "Missing parameter 'cardinality'"
    assert "singletonName" in params, "Missing parameter 'singletonName'"
    assert "collectionOrmAllowAdd" in params, "Missing parameter 'collectionOrmAllowAdd'"
    assert "headerClass" in params, "Missing parameter 'headerClass'"
    assert "ordered" in params, "Missing parameter 'ordered'"
    assert "title" in params, "Missing parameter 'title'"
    assert "footerClass" in params, "Missing parameter 'footerClass'"
    assert "emptyDisplayValue" in params, "Missing parameter 'emptyDisplayValue'"
    assert "pluralisedName" in params, "Missing parameter 'pluralisedName'"
    assert "customiseSet" in params, "Missing parameter 'customiseSet'"
    assert "defaultDisplayValue" in params, "Missing parameter 'defaultDisplayValue'"
    assert "booleanIsHasChoice" in params, "Missing parameter 'booleanIsHasChoice'"
    assert "displayClass" in params, "Missing parameter 'displayClass'"
    assert "encodeUriKey" in params, "Missing parameter 'encodeUriKey'"
    assert "collectionOrmAllowRemove" in params, "Missing parameter 'collectionOrmAllowRemove'"
    assert "primaryKey" in params, "Missing parameter 'primaryKey'"
    assert "derived" in params, "Missing parameter 'derived'"
    assert "columnName" in params, "Missing parameter 'columnName'"

def test_persistence::feature_has_cardinality():
    assert hasattr(persistence::Feature, "cardinality")
    descriptor = None
    for klass in persistence::Feature.__mro__:
        if "cardinality" in klass.__dict__:
            descriptor = klass.__dict__["cardinality"]
            break
    assert isinstance(descriptor, property)

def test_persistence::feature_has_singletonName():
    assert hasattr(persistence::Feature, "singletonName")
    descriptor = None
    for klass in persistence::Feature.__mro__:
        if "singletonName" in klass.__dict__:
            descriptor = klass.__dict__["singletonName"]
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

def test_persistence::feature_has_headerClass():
    assert hasattr(persistence::Feature, "headerClass")
    descriptor = None
    for klass in persistence::Feature.__mro__:
        if "headerClass" in klass.__dict__:
            descriptor = klass.__dict__["headerClass"]
            break
    assert isinstance(descriptor, property)

def test_persistence::feature_has_ordered():
    assert hasattr(persistence::Feature, "ordered")
    descriptor = None
    for klass in persistence::Feature.__mro__:
        if "ordered" in klass.__dict__:
            descriptor = klass.__dict__["ordered"]
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

def test_persistence::feature_has_footerClass():
    assert hasattr(persistence::Feature, "footerClass")
    descriptor = None
    for klass in persistence::Feature.__mro__:
        if "footerClass" in klass.__dict__:
            descriptor = klass.__dict__["footerClass"]
            break
    assert isinstance(descriptor, property)

def test_persistence::feature_has_emptyDisplayValue():
    assert hasattr(persistence::Feature, "emptyDisplayValue")
    descriptor = None
    for klass in persistence::Feature.__mro__:
        if "emptyDisplayValue" in klass.__dict__:
            descriptor = klass.__dict__["emptyDisplayValue"]
            break
    assert isinstance(descriptor, property)

def test_persistence::feature_has_pluralisedName():
    assert hasattr(persistence::Feature, "pluralisedName")
    descriptor = None
    for klass in persistence::Feature.__mro__:
        if "pluralisedName" in klass.__dict__:
            descriptor = klass.__dict__["pluralisedName"]
            break
    assert isinstance(descriptor, property)

def test_persistence::feature_has_customiseSet():
    assert hasattr(persistence::Feature, "customiseSet")
    descriptor = None
    for klass in persistence::Feature.__mro__:
        if "customiseSet" in klass.__dict__:
            descriptor = klass.__dict__["customiseSet"]
            break
    assert isinstance(descriptor, property)

def test_persistence::feature_has_defaultDisplayValue():
    assert hasattr(persistence::Feature, "defaultDisplayValue")
    descriptor = None
    for klass in persistence::Feature.__mro__:
        if "defaultDisplayValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultDisplayValue"]
            break
    assert isinstance(descriptor, property)

def test_persistence::feature_has_booleanIsHasChoice():
    assert hasattr(persistence::Feature, "booleanIsHasChoice")
    descriptor = None
    for klass in persistence::Feature.__mro__:
        if "booleanIsHasChoice" in klass.__dict__:
            descriptor = klass.__dict__["booleanIsHasChoice"]
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

def test_persistence::feature_has_encodeUriKey():
    assert hasattr(persistence::Feature, "encodeUriKey")
    descriptor = None
    for klass in persistence::Feature.__mro__:
        if "encodeUriKey" in klass.__dict__:
            descriptor = klass.__dict__["encodeUriKey"]
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

def test_persistence::feature_has_primaryKey():
    assert hasattr(persistence::Feature, "primaryKey")
    descriptor = None
    for klass in persistence::Feature.__mro__:
        if "primaryKey" in klass.__dict__:
            descriptor = klass.__dict__["primaryKey"]
            break
    assert isinstance(descriptor, property)

def test_persistence::feature_has_derived():
    assert hasattr(persistence::Feature, "derived")
    descriptor = None
    for klass in persistence::Feature.__mro__:
        if "derived" in klass.__dict__:
            descriptor = klass.__dict__["derived"]
            break
    assert isinstance(descriptor, property)

def test_persistence::feature_has_columnName():
    assert hasattr(persistence::Feature, "columnName")
    descriptor = None
    for klass in persistence::Feature.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)

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

def test_cardinality_exists():
    # Check that the Enumeration exists
    assert Cardinality is not None

def test_cardinality_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Cardinality]
    expected_literals = [
        "Many",
        "Optional",
        "Required",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Cardinality"

def test_ormtechnologies_exists():
    # Check that the Enumeration exists
    assert OrmTechnologies is not None

def test_ormtechnologies_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OrmTechnologies]
    expected_literals = [
        "Kohana",
        "DoctrineORM",
        "DataMapper",
        "DoctrineODM",
        "Idiorm",
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
        "DateOnly",
        "DateAndTime",
        "TimeOnly",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DateDetails"

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
Association_strategy = st.builds(
    Association,
)
persistence::AssociationWithContainment_strategy = st.builds(
    persistence::AssociationWithContainment,
    sourceVisible=
        st.booleans()
)
persistence::AssociationWithoutContainment_strategy = st.builds(
    persistence::AssociationWithoutContainment,
    targetUnique=
        st.booleans(),
    targetCardinality=
        safe_text
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
Attribute_strategy = st.builds(
    Attribute,
)
persistence::LocationAttribute_strategy = st.builds(
    persistence::LocationAttribute,
)
persistence::UrlAttribute_strategy = st.builds(
    persistence::UrlAttribute,
    displayValue=
        safe_text
)
persistence::DateAttribute_strategy = st.builds(
    persistence::DateAttribute,
    format=
        safe_text,
    details=
        safe_text
)
persistence::ResourceAttribute_strategy = st.builds(
    persistence::ResourceAttribute,
    uploadsWithinWebsite=
        st.booleans(),
    validUploadExtensions=
        safe_text,
    maximumUploadSize=
        st.integers(),
    validUploadMimeTypes=
        safe_text
)
persistence::DataTypeAttribute_strategy = st.builds(
    persistence::DataTypeAttribute,
    obfuscateFormFields=
        st.booleans(),
    caseInsensitive=
        st.booleans(),
    encrypt=
        st.booleans()
)
persistence::PathElement_strategy = st.builds(
    persistence::PathElement,
)
Classifier_strategy = st.builds(
    Classifier,
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
persistence::Expression_strategy = st.builds(
    persistence::Expression,
)
Label_strategy = st.builds(
    Label,
)
Feature_strategy = st.builds(
    Feature,
)
persistence::Attribute_strategy = st.builds(
    persistence::Attribute,
    validationPattern=
        safe_text,
    persistentType=
        safe_text,
    interfaceType=
        safe_text,
    unique=
        st.booleans(),
    inputElementClass=
        safe_text,
    containerUnique=
        st.booleans(),
    ormType=
        safe_text,
    placeholder=
        safe_text,
    inputColumnClass=
        safe_text,
    hidden=
        st.booleans()
)
NamedDisplayElement_strategy = st.builds(
    NamedDisplayElement,
)
persistence::AssociationKey_strategy = st.builds(
    persistence::AssociationKey,
)
persistence::Association_strategy = st.builds(
    persistence::Association,
    serializationMaxDepth=
        st.integers(),
    pivotTableName=
        safe_text,
    targetPrimaryKey=
        st.booleans(),
    targetInputClass=
        safe_text,
    bidirectional=
        st.booleans(),
    targetFeatureName=
        safe_text,
    targetColumnName=
        safe_text,
    unique=
        st.booleans(),
    inputColumnClass=
        safe_text,
    targetDisplayLabel=
        safe_text,
    targetHeaderClass=
        safe_text,
    pseudo=
        st.booleans(),
    targetDisplayClass=
        safe_text,
    targetFooterClass=
        safe_text,
    inputElementClass=
        safe_text
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
persistence::Entity_strategy = st.builds(
    persistence::Entity,
    singletonName=
        safe_text,
    autoKeyName=
        safe_text,
    tableName=
        safe_text,
    autoKeyPersistentType=
        safe_text,
    autoKeyGenerationStrategy=
        safe_text,
    implementsUserInterface=
        st.booleans(),
    pluralisedName=
        safe_text,
    allowFormTypeCustomisation=
        st.booleans()
)
persistence::DataType_strategy = st.builds(
    persistence::DataType,
)
persistence::SerializationGroup_strategy = st.builds(
    persistence::SerializationGroup,
)
persistence::Persistence_strategy = st.builds(
    persistence::Persistence,
    ormTechnology=
        safe_text,
    timestampUpdates=
        st.booleans(),
    databaseTechnology=
        safe_text,
    timestampCreation=
        st.booleans()
)
persistence::Feature_strategy = st.builds(
    persistence::Feature,
    cardinality=
        safe_text,
    singletonName=
        safe_text,
    collectionOrmAllowAdd=
        st.booleans(),
    headerClass=
        safe_text,
    ordered=
        st.booleans(),
    title=
        safe_text,
    footerClass=
        safe_text,
    emptyDisplayValue=
        safe_text,
    pluralisedName=
        safe_text,
    customiseSet=
        st.booleans(),
    defaultDisplayValue=
        safe_text,
    booleanIsHasChoice=
        safe_text,
    displayClass=
        safe_text,
    encodeUriKey=
        st.booleans(),
    collectionOrmAllowRemove=
        st.booleans(),
    primaryKey=
        st.booleans(),
    derived=
        st.booleans(),
    columnName=
        safe_text
)

@given(instance=Association_strategy)
@settings(max_examples=50)
def test_association_instantiation(instance):
    assert isinstance(instance, Association)

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
def test_persistence::associationwithoutcontainment_targetUnique_type(instance):
    assert isinstance(instance.targetUnique, bool)


@given(instance=persistence::AssociationWithoutContainment_strategy)
def test_persistence::associationwithoutcontainment_targetUnique_setter(instance):
    original = instance.targetUnique
    instance.targetUnique = original
    assert instance.targetUnique == original

@given(instance=persistence::AssociationWithoutContainment_strategy)
def test_persistence::associationwithoutcontainment_targetCardinality_type(instance):
    assert isinstance(instance.targetCardinality, str)


@given(instance=persistence::AssociationWithoutContainment_strategy)
def test_persistence::associationwithoutcontainment_targetCardinality_setter(instance):
    original = instance.targetCardinality
    instance.targetCardinality = original
    assert instance.targetCardinality == original

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

@given(instance=Attribute_strategy)
@settings(max_examples=50)
def test_attribute_instantiation(instance):
    assert isinstance(instance, Attribute)

@given(instance=persistence::LocationAttribute_strategy)
@settings(max_examples=50)
def test_persistence::locationattribute_instantiation(instance):
    assert isinstance(instance, persistence::LocationAttribute)

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

@given(instance=persistence::DateAttribute_strategy)
@settings(max_examples=50)
def test_persistence::dateattribute_instantiation(instance):
    assert isinstance(instance, persistence::DateAttribute)

@given(instance=persistence::DateAttribute_strategy)
def test_persistence::dateattribute_format_type(instance):
    assert isinstance(instance.format, str)


@given(instance=persistence::DateAttribute_strategy)
def test_persistence::dateattribute_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original

@given(instance=persistence::DateAttribute_strategy)
def test_persistence::dateattribute_details_type(instance):
    assert isinstance(instance.details, str)


@given(instance=persistence::DateAttribute_strategy)
def test_persistence::dateattribute_details_setter(instance):
    original = instance.details
    instance.details = original
    assert instance.details == original

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
def test_persistence::resourceattribute_maximumUploadSize_type(instance):
    assert isinstance(instance.maximumUploadSize, int)


@given(instance=persistence::ResourceAttribute_strategy)
def test_persistence::resourceattribute_maximumUploadSize_setter(instance):
    original = instance.maximumUploadSize
    instance.maximumUploadSize = original
    assert instance.maximumUploadSize == original

@given(instance=persistence::ResourceAttribute_strategy)
def test_persistence::resourceattribute_validUploadMimeTypes_type(instance):
    assert isinstance(instance.validUploadMimeTypes, str)


@given(instance=persistence::ResourceAttribute_strategy)
def test_persistence::resourceattribute_validUploadMimeTypes_setter(instance):
    original = instance.validUploadMimeTypes
    instance.validUploadMimeTypes = original
    assert instance.validUploadMimeTypes == original

@given(instance=persistence::DataTypeAttribute_strategy)
@settings(max_examples=50)
def test_persistence::datatypeattribute_instantiation(instance):
    assert isinstance(instance, persistence::DataTypeAttribute)

@given(instance=persistence::DataTypeAttribute_strategy)
def test_persistence::datatypeattribute_obfuscateFormFields_type(instance):
    assert isinstance(instance.obfuscateFormFields, bool)


@given(instance=persistence::DataTypeAttribute_strategy)
def test_persistence::datatypeattribute_obfuscateFormFields_setter(instance):
    original = instance.obfuscateFormFields
    instance.obfuscateFormFields = original
    assert instance.obfuscateFormFields == original

@given(instance=persistence::DataTypeAttribute_strategy)
def test_persistence::datatypeattribute_caseInsensitive_type(instance):
    assert isinstance(instance.caseInsensitive, bool)


@given(instance=persistence::DataTypeAttribute_strategy)
def test_persistence::datatypeattribute_caseInsensitive_setter(instance):
    original = instance.caseInsensitive
    instance.caseInsensitive = original
    assert instance.caseInsensitive == original

@given(instance=persistence::DataTypeAttribute_strategy)
def test_persistence::datatypeattribute_encrypt_type(instance):
    assert isinstance(instance.encrypt, bool)


@given(instance=persistence::DataTypeAttribute_strategy)
def test_persistence::datatypeattribute_encrypt_setter(instance):
    original = instance.encrypt
    instance.encrypt = original
    assert instance.encrypt == original

@given(instance=persistence::PathElement_strategy)
@settings(max_examples=50)
def test_persistence::pathelement_instantiation(instance):
    assert isinstance(instance, persistence::PathElement)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

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
def test_persistence::attribute_persistentType_type(instance):
    assert isinstance(instance.persistentType, str)


@given(instance=persistence::Attribute_strategy)
def test_persistence::attribute_persistentType_setter(instance):
    original = instance.persistentType
    instance.persistentType = original
    assert instance.persistentType == original

@given(instance=persistence::Attribute_strategy)
def test_persistence::attribute_interfaceType_type(instance):
    assert isinstance(instance.interfaceType, str)


@given(instance=persistence::Attribute_strategy)
def test_persistence::attribute_interfaceType_setter(instance):
    original = instance.interfaceType
    instance.interfaceType = original
    assert instance.interfaceType == original

@given(instance=persistence::Attribute_strategy)
def test_persistence::attribute_unique_type(instance):
    assert isinstance(instance.unique, bool)


@given(instance=persistence::Attribute_strategy)
def test_persistence::attribute_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original

@given(instance=persistence::Attribute_strategy)
def test_persistence::attribute_inputElementClass_type(instance):
    assert isinstance(instance.inputElementClass, str)


@given(instance=persistence::Attribute_strategy)
def test_persistence::attribute_inputElementClass_setter(instance):
    original = instance.inputElementClass
    instance.inputElementClass = original
    assert instance.inputElementClass == original

@given(instance=persistence::Attribute_strategy)
def test_persistence::attribute_containerUnique_type(instance):
    assert isinstance(instance.containerUnique, bool)


@given(instance=persistence::Attribute_strategy)
def test_persistence::attribute_containerUnique_setter(instance):
    original = instance.containerUnique
    instance.containerUnique = original
    assert instance.containerUnique == original

@given(instance=persistence::Attribute_strategy)
def test_persistence::attribute_ormType_type(instance):
    assert isinstance(instance.ormType, str)


@given(instance=persistence::Attribute_strategy)
def test_persistence::attribute_ormType_setter(instance):
    original = instance.ormType
    instance.ormType = original
    assert instance.ormType == original

@given(instance=persistence::Attribute_strategy)
def test_persistence::attribute_placeholder_type(instance):
    assert isinstance(instance.placeholder, str)


@given(instance=persistence::Attribute_strategy)
def test_persistence::attribute_placeholder_setter(instance):
    original = instance.placeholder
    instance.placeholder = original
    assert instance.placeholder == original

@given(instance=persistence::Attribute_strategy)
def test_persistence::attribute_inputColumnClass_type(instance):
    assert isinstance(instance.inputColumnClass, str)


@given(instance=persistence::Attribute_strategy)
def test_persistence::attribute_inputColumnClass_setter(instance):
    original = instance.inputColumnClass
    instance.inputColumnClass = original
    assert instance.inputColumnClass == original

@given(instance=persistence::Attribute_strategy)
def test_persistence::attribute_hidden_type(instance):
    assert isinstance(instance.hidden, bool)


@given(instance=persistence::Attribute_strategy)
def test_persistence::attribute_hidden_setter(instance):
    original = instance.hidden
    instance.hidden = original
    assert instance.hidden == original

@given(instance=NamedDisplayElement_strategy)
@settings(max_examples=50)
def test_nameddisplayelement_instantiation(instance):
    assert isinstance(instance, NamedDisplayElement)

@given(instance=persistence::AssociationKey_strategy)
@settings(max_examples=50)
def test_persistence::associationkey_instantiation(instance):
    assert isinstance(instance, persistence::AssociationKey)

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
def test_persistence::association_pivotTableName_type(instance):
    assert isinstance(instance.pivotTableName, str)


@given(instance=persistence::Association_strategy)
def test_persistence::association_pivotTableName_setter(instance):
    original = instance.pivotTableName
    instance.pivotTableName = original
    assert instance.pivotTableName == original

@given(instance=persistence::Association_strategy)
def test_persistence::association_targetPrimaryKey_type(instance):
    assert isinstance(instance.targetPrimaryKey, bool)


@given(instance=persistence::Association_strategy)
def test_persistence::association_targetPrimaryKey_setter(instance):
    original = instance.targetPrimaryKey
    instance.targetPrimaryKey = original
    assert instance.targetPrimaryKey == original

@given(instance=persistence::Association_strategy)
def test_persistence::association_targetInputClass_type(instance):
    assert isinstance(instance.targetInputClass, str)


@given(instance=persistence::Association_strategy)
def test_persistence::association_targetInputClass_setter(instance):
    original = instance.targetInputClass
    instance.targetInputClass = original
    assert instance.targetInputClass == original

@given(instance=persistence::Association_strategy)
def test_persistence::association_bidirectional_type(instance):
    assert isinstance(instance.bidirectional, bool)


@given(instance=persistence::Association_strategy)
def test_persistence::association_bidirectional_setter(instance):
    original = instance.bidirectional
    instance.bidirectional = original
    assert instance.bidirectional == original

@given(instance=persistence::Association_strategy)
def test_persistence::association_targetFeatureName_type(instance):
    assert isinstance(instance.targetFeatureName, str)


@given(instance=persistence::Association_strategy)
def test_persistence::association_targetFeatureName_setter(instance):
    original = instance.targetFeatureName
    instance.targetFeatureName = original
    assert instance.targetFeatureName == original

@given(instance=persistence::Association_strategy)
def test_persistence::association_targetColumnName_type(instance):
    assert isinstance(instance.targetColumnName, str)


@given(instance=persistence::Association_strategy)
def test_persistence::association_targetColumnName_setter(instance):
    original = instance.targetColumnName
    instance.targetColumnName = original
    assert instance.targetColumnName == original

@given(instance=persistence::Association_strategy)
def test_persistence::association_unique_type(instance):
    assert isinstance(instance.unique, bool)


@given(instance=persistence::Association_strategy)
def test_persistence::association_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original

@given(instance=persistence::Association_strategy)
def test_persistence::association_inputColumnClass_type(instance):
    assert isinstance(instance.inputColumnClass, str)


@given(instance=persistence::Association_strategy)
def test_persistence::association_inputColumnClass_setter(instance):
    original = instance.inputColumnClass
    instance.inputColumnClass = original
    assert instance.inputColumnClass == original

@given(instance=persistence::Association_strategy)
def test_persistence::association_targetDisplayLabel_type(instance):
    assert isinstance(instance.targetDisplayLabel, str)


@given(instance=persistence::Association_strategy)
def test_persistence::association_targetDisplayLabel_setter(instance):
    original = instance.targetDisplayLabel
    instance.targetDisplayLabel = original
    assert instance.targetDisplayLabel == original

@given(instance=persistence::Association_strategy)
def test_persistence::association_targetHeaderClass_type(instance):
    assert isinstance(instance.targetHeaderClass, str)


@given(instance=persistence::Association_strategy)
def test_persistence::association_targetHeaderClass_setter(instance):
    original = instance.targetHeaderClass
    instance.targetHeaderClass = original
    assert instance.targetHeaderClass == original

@given(instance=persistence::Association_strategy)
def test_persistence::association_pseudo_type(instance):
    assert isinstance(instance.pseudo, bool)


@given(instance=persistence::Association_strategy)
def test_persistence::association_pseudo_setter(instance):
    original = instance.pseudo
    instance.pseudo = original
    assert instance.pseudo == original

@given(instance=persistence::Association_strategy)
def test_persistence::association_targetDisplayClass_type(instance):
    assert isinstance(instance.targetDisplayClass, str)


@given(instance=persistence::Association_strategy)
def test_persistence::association_targetDisplayClass_setter(instance):
    original = instance.targetDisplayClass
    instance.targetDisplayClass = original
    assert instance.targetDisplayClass == original

@given(instance=persistence::Association_strategy)
def test_persistence::association_targetFooterClass_type(instance):
    assert isinstance(instance.targetFooterClass, str)


@given(instance=persistence::Association_strategy)
def test_persistence::association_targetFooterClass_setter(instance):
    original = instance.targetFooterClass
    instance.targetFooterClass = original
    assert instance.targetFooterClass == original

@given(instance=persistence::Association_strategy)
def test_persistence::association_inputElementClass_type(instance):
    assert isinstance(instance.inputElementClass, str)


@given(instance=persistence::Association_strategy)
def test_persistence::association_inputElementClass_setter(instance):
    original = instance.inputElementClass
    instance.inputElementClass = original
    assert instance.inputElementClass == original

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

@given(instance=persistence::Entity_strategy)
@settings(max_examples=50)
def test_persistence::entity_instantiation(instance):
    assert isinstance(instance, persistence::Entity)

@given(instance=persistence::Entity_strategy)
def test_persistence::entity_singletonName_type(instance):
    assert isinstance(instance.singletonName, str)


@given(instance=persistence::Entity_strategy)
def test_persistence::entity_singletonName_setter(instance):
    original = instance.singletonName
    instance.singletonName = original
    assert instance.singletonName == original

@given(instance=persistence::Entity_strategy)
def test_persistence::entity_autoKeyName_type(instance):
    assert isinstance(instance.autoKeyName, str)


@given(instance=persistence::Entity_strategy)
def test_persistence::entity_autoKeyName_setter(instance):
    original = instance.autoKeyName
    instance.autoKeyName = original
    assert instance.autoKeyName == original

@given(instance=persistence::Entity_strategy)
def test_persistence::entity_tableName_type(instance):
    assert isinstance(instance.tableName, str)


@given(instance=persistence::Entity_strategy)
def test_persistence::entity_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original

@given(instance=persistence::Entity_strategy)
def test_persistence::entity_autoKeyPersistentType_type(instance):
    assert isinstance(instance.autoKeyPersistentType, str)


@given(instance=persistence::Entity_strategy)
def test_persistence::entity_autoKeyPersistentType_setter(instance):
    original = instance.autoKeyPersistentType
    instance.autoKeyPersistentType = original
    assert instance.autoKeyPersistentType == original

@given(instance=persistence::Entity_strategy)
def test_persistence::entity_autoKeyGenerationStrategy_type(instance):
    assert isinstance(instance.autoKeyGenerationStrategy, str)


@given(instance=persistence::Entity_strategy)
def test_persistence::entity_autoKeyGenerationStrategy_setter(instance):
    original = instance.autoKeyGenerationStrategy
    instance.autoKeyGenerationStrategy = original
    assert instance.autoKeyGenerationStrategy == original

@given(instance=persistence::Entity_strategy)
def test_persistence::entity_implementsUserInterface_type(instance):
    assert isinstance(instance.implementsUserInterface, bool)


@given(instance=persistence::Entity_strategy)
def test_persistence::entity_implementsUserInterface_setter(instance):
    original = instance.implementsUserInterface
    instance.implementsUserInterface = original
    assert instance.implementsUserInterface == original

@given(instance=persistence::Entity_strategy)
def test_persistence::entity_pluralisedName_type(instance):
    assert isinstance(instance.pluralisedName, str)


@given(instance=persistence::Entity_strategy)
def test_persistence::entity_pluralisedName_setter(instance):
    original = instance.pluralisedName
    instance.pluralisedName = original
    assert instance.pluralisedName == original

@given(instance=persistence::Entity_strategy)
def test_persistence::entity_allowFormTypeCustomisation_type(instance):
    assert isinstance(instance.allowFormTypeCustomisation, bool)


@given(instance=persistence::Entity_strategy)
def test_persistence::entity_allowFormTypeCustomisation_setter(instance):
    original = instance.allowFormTypeCustomisation
    instance.allowFormTypeCustomisation = original
    assert instance.allowFormTypeCustomisation == original

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
def test_persistence::persistence_ormTechnology_type(instance):
    assert isinstance(instance.ormTechnology, str)


@given(instance=persistence::Persistence_strategy)
def test_persistence::persistence_ormTechnology_setter(instance):
    original = instance.ormTechnology
    instance.ormTechnology = original
    assert instance.ormTechnology == original

@given(instance=persistence::Persistence_strategy)
def test_persistence::persistence_timestampUpdates_type(instance):
    assert isinstance(instance.timestampUpdates, bool)


@given(instance=persistence::Persistence_strategy)
def test_persistence::persistence_timestampUpdates_setter(instance):
    original = instance.timestampUpdates
    instance.timestampUpdates = original
    assert instance.timestampUpdates == original

@given(instance=persistence::Persistence_strategy)
def test_persistence::persistence_databaseTechnology_type(instance):
    assert isinstance(instance.databaseTechnology, str)


@given(instance=persistence::Persistence_strategy)
def test_persistence::persistence_databaseTechnology_setter(instance):
    original = instance.databaseTechnology
    instance.databaseTechnology = original
    assert instance.databaseTechnology == original

@given(instance=persistence::Persistence_strategy)
def test_persistence::persistence_timestampCreation_type(instance):
    assert isinstance(instance.timestampCreation, bool)


@given(instance=persistence::Persistence_strategy)
def test_persistence::persistence_timestampCreation_setter(instance):
    original = instance.timestampCreation
    instance.timestampCreation = original
    assert instance.timestampCreation == original

@given(instance=persistence::Feature_strategy)
@settings(max_examples=50)
def test_persistence::feature_instantiation(instance):
    assert isinstance(instance, persistence::Feature)

@given(instance=persistence::Feature_strategy)
def test_persistence::feature_cardinality_type(instance):
    assert isinstance(instance.cardinality, str)


@given(instance=persistence::Feature_strategy)
def test_persistence::feature_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original

@given(instance=persistence::Feature_strategy)
def test_persistence::feature_singletonName_type(instance):
    assert isinstance(instance.singletonName, str)


@given(instance=persistence::Feature_strategy)
def test_persistence::feature_singletonName_setter(instance):
    original = instance.singletonName
    instance.singletonName = original
    assert instance.singletonName == original

@given(instance=persistence::Feature_strategy)
def test_persistence::feature_collectionOrmAllowAdd_type(instance):
    assert isinstance(instance.collectionOrmAllowAdd, bool)


@given(instance=persistence::Feature_strategy)
def test_persistence::feature_collectionOrmAllowAdd_setter(instance):
    original = instance.collectionOrmAllowAdd
    instance.collectionOrmAllowAdd = original
    assert instance.collectionOrmAllowAdd == original

@given(instance=persistence::Feature_strategy)
def test_persistence::feature_headerClass_type(instance):
    assert isinstance(instance.headerClass, str)


@given(instance=persistence::Feature_strategy)
def test_persistence::feature_headerClass_setter(instance):
    original = instance.headerClass
    instance.headerClass = original
    assert instance.headerClass == original

@given(instance=persistence::Feature_strategy)
def test_persistence::feature_ordered_type(instance):
    assert isinstance(instance.ordered, bool)


@given(instance=persistence::Feature_strategy)
def test_persistence::feature_ordered_setter(instance):
    original = instance.ordered
    instance.ordered = original
    assert instance.ordered == original

@given(instance=persistence::Feature_strategy)
def test_persistence::feature_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=persistence::Feature_strategy)
def test_persistence::feature_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=persistence::Feature_strategy)
def test_persistence::feature_footerClass_type(instance):
    assert isinstance(instance.footerClass, str)


@given(instance=persistence::Feature_strategy)
def test_persistence::feature_footerClass_setter(instance):
    original = instance.footerClass
    instance.footerClass = original
    assert instance.footerClass == original

@given(instance=persistence::Feature_strategy)
def test_persistence::feature_emptyDisplayValue_type(instance):
    assert isinstance(instance.emptyDisplayValue, str)


@given(instance=persistence::Feature_strategy)
def test_persistence::feature_emptyDisplayValue_setter(instance):
    original = instance.emptyDisplayValue
    instance.emptyDisplayValue = original
    assert instance.emptyDisplayValue == original

@given(instance=persistence::Feature_strategy)
def test_persistence::feature_pluralisedName_type(instance):
    assert isinstance(instance.pluralisedName, str)


@given(instance=persistence::Feature_strategy)
def test_persistence::feature_pluralisedName_setter(instance):
    original = instance.pluralisedName
    instance.pluralisedName = original
    assert instance.pluralisedName == original

@given(instance=persistence::Feature_strategy)
def test_persistence::feature_customiseSet_type(instance):
    assert isinstance(instance.customiseSet, bool)


@given(instance=persistence::Feature_strategy)
def test_persistence::feature_customiseSet_setter(instance):
    original = instance.customiseSet
    instance.customiseSet = original
    assert instance.customiseSet == original

@given(instance=persistence::Feature_strategy)
def test_persistence::feature_defaultDisplayValue_type(instance):
    assert isinstance(instance.defaultDisplayValue, str)


@given(instance=persistence::Feature_strategy)
def test_persistence::feature_defaultDisplayValue_setter(instance):
    original = instance.defaultDisplayValue
    instance.defaultDisplayValue = original
    assert instance.defaultDisplayValue == original

@given(instance=persistence::Feature_strategy)
def test_persistence::feature_booleanIsHasChoice_type(instance):
    assert isinstance(instance.booleanIsHasChoice, str)


@given(instance=persistence::Feature_strategy)
def test_persistence::feature_booleanIsHasChoice_setter(instance):
    original = instance.booleanIsHasChoice
    instance.booleanIsHasChoice = original
    assert instance.booleanIsHasChoice == original

@given(instance=persistence::Feature_strategy)
def test_persistence::feature_displayClass_type(instance):
    assert isinstance(instance.displayClass, str)


@given(instance=persistence::Feature_strategy)
def test_persistence::feature_displayClass_setter(instance):
    original = instance.displayClass
    instance.displayClass = original
    assert instance.displayClass == original

@given(instance=persistence::Feature_strategy)
def test_persistence::feature_encodeUriKey_type(instance):
    assert isinstance(instance.encodeUriKey, bool)


@given(instance=persistence::Feature_strategy)
def test_persistence::feature_encodeUriKey_setter(instance):
    original = instance.encodeUriKey
    instance.encodeUriKey = original
    assert instance.encodeUriKey == original

@given(instance=persistence::Feature_strategy)
def test_persistence::feature_collectionOrmAllowRemove_type(instance):
    assert isinstance(instance.collectionOrmAllowRemove, bool)


@given(instance=persistence::Feature_strategy)
def test_persistence::feature_collectionOrmAllowRemove_setter(instance):
    original = instance.collectionOrmAllowRemove
    instance.collectionOrmAllowRemove = original
    assert instance.collectionOrmAllowRemove == original

@given(instance=persistence::Feature_strategy)
def test_persistence::feature_primaryKey_type(instance):
    assert isinstance(instance.primaryKey, bool)


@given(instance=persistence::Feature_strategy)
def test_persistence::feature_primaryKey_setter(instance):
    original = instance.primaryKey
    instance.primaryKey = original
    assert instance.primaryKey == original

@given(instance=persistence::Feature_strategy)
def test_persistence::feature_derived_type(instance):
    assert isinstance(instance.derived, bool)


@given(instance=persistence::Feature_strategy)
def test_persistence::feature_derived_setter(instance):
    original = instance.derived
    instance.derived = original
    assert instance.derived == original

@given(instance=persistence::Feature_strategy)
def test_persistence::feature_columnName_type(instance):
    assert isinstance(instance.columnName, str)


@given(instance=persistence::Feature_strategy)
def test_persistence::feature_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original
