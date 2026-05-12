import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Association,
    persistence_AssociationWithContainment,
    persistence_AssociationWithoutContainment,
    ResourceAttribute,
    persistence_ImageAttribute,
    persistence_FileAttribute,
    PathElement,
    persistence_DatePathElement,
    persistence_StaticPathElement,
    Attribute,
    persistence_UrlAttribute,
    persistence_DateAttribute,
    persistence_LocationAttribute,
    persistence_ResourceAttribute,
    persistence_DataTypeAttribute,
    persistence_PathElement,
    Classifier,
    ModelLabelFeature,
    persistence_ModelLabelAssociation,
    persistence_ModelLabelAttribute,
    persistence_ModelLabelFeature,
    persistence_Label,
    persistence_Expression,
    Label,
    Feature,
    persistence_Attribute,
    NamedDisplayElement,
    persistence_AssociationKey,
    persistence_Association,
    NamedElement,
    persistence_ModelLabel,
    persistence_Entity,
    persistence_DataType,
    persistence_SerializationGroup,
    persistence_Persistence,
    persistence_Feature,
    Cardinality,
    DatabaseTechnologies,
    isHasChoices,
    DateDetails,
    OrmTechnologies,
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



def test_persistence_associationwithoutcontainment_is_not_abstract():
    assert not inspect.isabstract(persistence_AssociationWithoutContainment)


def test_persistence_associationwithoutcontainment_constructor_exists():
    assert callable(persistence_AssociationWithoutContainment.__init__)


def test_persistence_associationwithoutcontainment_constructor_args():
    sig = inspect.signature(persistence_AssociationWithoutContainment.__init__)
    params = list(sig.parameters.keys())
    assert "targetCardinality" in params, "Missing parameter 'targetCardinality'"
    assert "targetUnique" in params, "Missing parameter 'targetUnique'"

def test_persistence_associationwithoutcontainment_has_targetCardinality():
    assert hasattr(persistence_AssociationWithoutContainment, "targetCardinality")
    descriptor = None
    for klass in persistence_AssociationWithoutContainment.__mro__:
        if "targetCardinality" in klass.__dict__:
            descriptor = klass.__dict__["targetCardinality"]
            break
    assert isinstance(descriptor, property)

def test_persistence_associationwithoutcontainment_has_targetUnique():
    assert hasattr(persistence_AssociationWithoutContainment, "targetUnique")
    descriptor = None
    for klass in persistence_AssociationWithoutContainment.__mro__:
        if "targetUnique" in klass.__dict__:
            descriptor = klass.__dict__["targetUnique"]
            break
    assert isinstance(descriptor, property)



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



def test_attribute_is_not_abstract():
    assert not inspect.isabstract(Attribute)


def test_attribute_constructor_exists():
    assert callable(Attribute.__init__)


def test_attribute_constructor_args():
    sig = inspect.signature(Attribute.__init__)
    params = list(sig.parameters.keys())



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
    assert "details" in params, "Missing parameter 'details'"
    assert "format" in params, "Missing parameter 'format'"

def test_persistence_dateattribute_has_details():
    assert hasattr(persistence_DateAttribute, "details")
    descriptor = None
    for klass in persistence_DateAttribute.__mro__:
        if "details" in klass.__dict__:
            descriptor = klass.__dict__["details"]
            break
    assert isinstance(descriptor, property)

def test_persistence_dateattribute_has_format():
    assert hasattr(persistence_DateAttribute, "format")
    descriptor = None
    for klass in persistence_DateAttribute.__mro__:
        if "format" in klass.__dict__:
            descriptor = klass.__dict__["format"]
            break
    assert isinstance(descriptor, property)



def test_persistence_locationattribute_is_not_abstract():
    assert not inspect.isabstract(persistence_LocationAttribute)


def test_persistence_locationattribute_constructor_exists():
    assert callable(persistence_LocationAttribute.__init__)


def test_persistence_locationattribute_constructor_args():
    sig = inspect.signature(persistence_LocationAttribute.__init__)
    params = list(sig.parameters.keys())



def test_persistence_resourceattribute_is_not_abstract():
    assert not inspect.isabstract(persistence_ResourceAttribute)


def test_persistence_resourceattribute_constructor_exists():
    assert callable(persistence_ResourceAttribute.__init__)


def test_persistence_resourceattribute_constructor_args():
    sig = inspect.signature(persistence_ResourceAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "maximumUploadSize" in params, "Missing parameter 'maximumUploadSize'"
    assert "uploadsWithinWebsite" in params, "Missing parameter 'uploadsWithinWebsite'"
    assert "validUploadExtensions" in params, "Missing parameter 'validUploadExtensions'"
    assert "validUploadMimeTypes" in params, "Missing parameter 'validUploadMimeTypes'"

def test_persistence_resourceattribute_has_maximumUploadSize():
    assert hasattr(persistence_ResourceAttribute, "maximumUploadSize")
    descriptor = None
    for klass in persistence_ResourceAttribute.__mro__:
        if "maximumUploadSize" in klass.__dict__:
            descriptor = klass.__dict__["maximumUploadSize"]
            break
    assert isinstance(descriptor, property)

def test_persistence_resourceattribute_has_uploadsWithinWebsite():
    assert hasattr(persistence_ResourceAttribute, "uploadsWithinWebsite")
    descriptor = None
    for klass in persistence_ResourceAttribute.__mro__:
        if "uploadsWithinWebsite" in klass.__dict__:
            descriptor = klass.__dict__["uploadsWithinWebsite"]
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

def test_persistence_resourceattribute_has_validUploadMimeTypes():
    assert hasattr(persistence_ResourceAttribute, "validUploadMimeTypes")
    descriptor = None
    for klass in persistence_ResourceAttribute.__mro__:
        if "validUploadMimeTypes" in klass.__dict__:
            descriptor = klass.__dict__["validUploadMimeTypes"]
            break
    assert isinstance(descriptor, property)



def test_persistence_datatypeattribute_is_not_abstract():
    assert not inspect.isabstract(persistence_DataTypeAttribute)


def test_persistence_datatypeattribute_constructor_exists():
    assert callable(persistence_DataTypeAttribute.__init__)


def test_persistence_datatypeattribute_constructor_args():
    sig = inspect.signature(persistence_DataTypeAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "encrypt" in params, "Missing parameter 'encrypt'"
    assert "caseInsensitive" in params, "Missing parameter 'caseInsensitive'"
    assert "obfuscateFormFields" in params, "Missing parameter 'obfuscateFormFields'"

def test_persistence_datatypeattribute_has_encrypt():
    assert hasattr(persistence_DataTypeAttribute, "encrypt")
    descriptor = None
    for klass in persistence_DataTypeAttribute.__mro__:
        if "encrypt" in klass.__dict__:
            descriptor = klass.__dict__["encrypt"]
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

def test_persistence_datatypeattribute_has_obfuscateFormFields():
    assert hasattr(persistence_DataTypeAttribute, "obfuscateFormFields")
    descriptor = None
    for klass in persistence_DataTypeAttribute.__mro__:
        if "obfuscateFormFields" in klass.__dict__:
            descriptor = klass.__dict__["obfuscateFormFields"]
            break
    assert isinstance(descriptor, property)



def test_persistence_pathelement_is_not_abstract():
    assert not inspect.isabstract(persistence_PathElement)


def test_persistence_pathelement_constructor_exists():
    assert callable(persistence_PathElement.__init__)


def test_persistence_pathelement_constructor_args():
    sig = inspect.signature(persistence_PathElement.__init__)
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



def test_persistence_attribute_is_not_abstract():
    assert not inspect.isabstract(persistence_Attribute)


def test_persistence_attribute_constructor_exists():
    assert callable(persistence_Attribute.__init__)


def test_persistence_attribute_constructor_args():
    sig = inspect.signature(persistence_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "ormType" in params, "Missing parameter 'ormType'"
    assert "persistentType" in params, "Missing parameter 'persistentType'"
    assert "hidden" in params, "Missing parameter 'hidden'"
    assert "unique" in params, "Missing parameter 'unique'"
    assert "placeholder" in params, "Missing parameter 'placeholder'"
    assert "inputColumnClass" in params, "Missing parameter 'inputColumnClass'"
    assert "interfaceType" in params, "Missing parameter 'interfaceType'"
    assert "inputElementClass" in params, "Missing parameter 'inputElementClass'"
    assert "validationPattern" in params, "Missing parameter 'validationPattern'"
    assert "containerUnique" in params, "Missing parameter 'containerUnique'"

def test_persistence_attribute_has_ormType():
    assert hasattr(persistence_Attribute, "ormType")
    descriptor = None
    for klass in persistence_Attribute.__mro__:
        if "ormType" in klass.__dict__:
            descriptor = klass.__dict__["ormType"]
            break
    assert isinstance(descriptor, property)

def test_persistence_attribute_has_persistentType():
    assert hasattr(persistence_Attribute, "persistentType")
    descriptor = None
    for klass in persistence_Attribute.__mro__:
        if "persistentType" in klass.__dict__:
            descriptor = klass.__dict__["persistentType"]
            break
    assert isinstance(descriptor, property)

def test_persistence_attribute_has_hidden():
    assert hasattr(persistence_Attribute, "hidden")
    descriptor = None
    for klass in persistence_Attribute.__mro__:
        if "hidden" in klass.__dict__:
            descriptor = klass.__dict__["hidden"]
            break
    assert isinstance(descriptor, property)

def test_persistence_attribute_has_unique():
    assert hasattr(persistence_Attribute, "unique")
    descriptor = None
    for klass in persistence_Attribute.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
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

def test_persistence_attribute_has_inputColumnClass():
    assert hasattr(persistence_Attribute, "inputColumnClass")
    descriptor = None
    for klass in persistence_Attribute.__mro__:
        if "inputColumnClass" in klass.__dict__:
            descriptor = klass.__dict__["inputColumnClass"]
            break
    assert isinstance(descriptor, property)

def test_persistence_attribute_has_interfaceType():
    assert hasattr(persistence_Attribute, "interfaceType")
    descriptor = None
    for klass in persistence_Attribute.__mro__:
        if "interfaceType" in klass.__dict__:
            descriptor = klass.__dict__["interfaceType"]
            break
    assert isinstance(descriptor, property)

def test_persistence_attribute_has_inputElementClass():
    assert hasattr(persistence_Attribute, "inputElementClass")
    descriptor = None
    for klass in persistence_Attribute.__mro__:
        if "inputElementClass" in klass.__dict__:
            descriptor = klass.__dict__["inputElementClass"]
            break
    assert isinstance(descriptor, property)

def test_persistence_attribute_has_validationPattern():
    assert hasattr(persistence_Attribute, "validationPattern")
    descriptor = None
    for klass in persistence_Attribute.__mro__:
        if "validationPattern" in klass.__dict__:
            descriptor = klass.__dict__["validationPattern"]
            break
    assert isinstance(descriptor, property)

def test_persistence_attribute_has_containerUnique():
    assert hasattr(persistence_Attribute, "containerUnique")
    descriptor = None
    for klass in persistence_Attribute.__mro__:
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



def test_persistence_associationkey_is_not_abstract():
    assert not inspect.isabstract(persistence_AssociationKey)


def test_persistence_associationkey_constructor_exists():
    assert callable(persistence_AssociationKey.__init__)


def test_persistence_associationkey_constructor_args():
    sig = inspect.signature(persistence_AssociationKey.__init__)
    params = list(sig.parameters.keys())



def test_persistence_association_is_not_abstract():
    assert not inspect.isabstract(persistence_Association)


def test_persistence_association_constructor_exists():
    assert callable(persistence_Association.__init__)


def test_persistence_association_constructor_args():
    sig = inspect.signature(persistence_Association.__init__)
    params = list(sig.parameters.keys())
    assert "bidirectional" in params, "Missing parameter 'bidirectional'"
    assert "targetPrimaryKey" in params, "Missing parameter 'targetPrimaryKey'"
    assert "pivotTableName" in params, "Missing parameter 'pivotTableName'"
    assert "targetDisplayLabel" in params, "Missing parameter 'targetDisplayLabel'"
    assert "targetInputClass" in params, "Missing parameter 'targetInputClass'"
    assert "targetHeaderClass" in params, "Missing parameter 'targetHeaderClass'"
    assert "targetFooterClass" in params, "Missing parameter 'targetFooterClass'"
    assert "serializationMaxDepth" in params, "Missing parameter 'serializationMaxDepth'"
    assert "inputColumnClass" in params, "Missing parameter 'inputColumnClass'"
    assert "inputElementClass" in params, "Missing parameter 'inputElementClass'"
    assert "pseudo" in params, "Missing parameter 'pseudo'"
    assert "targetFeatureName" in params, "Missing parameter 'targetFeatureName'"
    assert "targetColumnName" in params, "Missing parameter 'targetColumnName'"
    assert "unique" in params, "Missing parameter 'unique'"
    assert "targetDisplayClass" in params, "Missing parameter 'targetDisplayClass'"

def test_persistence_association_has_bidirectional():
    assert hasattr(persistence_Association, "bidirectional")
    descriptor = None
    for klass in persistence_Association.__mro__:
        if "bidirectional" in klass.__dict__:
            descriptor = klass.__dict__["bidirectional"]
            break
    assert isinstance(descriptor, property)

def test_persistence_association_has_targetPrimaryKey():
    assert hasattr(persistence_Association, "targetPrimaryKey")
    descriptor = None
    for klass in persistence_Association.__mro__:
        if "targetPrimaryKey" in klass.__dict__:
            descriptor = klass.__dict__["targetPrimaryKey"]
            break
    assert isinstance(descriptor, property)

def test_persistence_association_has_pivotTableName():
    assert hasattr(persistence_Association, "pivotTableName")
    descriptor = None
    for klass in persistence_Association.__mro__:
        if "pivotTableName" in klass.__dict__:
            descriptor = klass.__dict__["pivotTableName"]
            break
    assert isinstance(descriptor, property)

def test_persistence_association_has_targetDisplayLabel():
    assert hasattr(persistence_Association, "targetDisplayLabel")
    descriptor = None
    for klass in persistence_Association.__mro__:
        if "targetDisplayLabel" in klass.__dict__:
            descriptor = klass.__dict__["targetDisplayLabel"]
            break
    assert isinstance(descriptor, property)

def test_persistence_association_has_targetInputClass():
    assert hasattr(persistence_Association, "targetInputClass")
    descriptor = None
    for klass in persistence_Association.__mro__:
        if "targetInputClass" in klass.__dict__:
            descriptor = klass.__dict__["targetInputClass"]
            break
    assert isinstance(descriptor, property)

def test_persistence_association_has_targetHeaderClass():
    assert hasattr(persistence_Association, "targetHeaderClass")
    descriptor = None
    for klass in persistence_Association.__mro__:
        if "targetHeaderClass" in klass.__dict__:
            descriptor = klass.__dict__["targetHeaderClass"]
            break
    assert isinstance(descriptor, property)

def test_persistence_association_has_targetFooterClass():
    assert hasattr(persistence_Association, "targetFooterClass")
    descriptor = None
    for klass in persistence_Association.__mro__:
        if "targetFooterClass" in klass.__dict__:
            descriptor = klass.__dict__["targetFooterClass"]
            break
    assert isinstance(descriptor, property)

def test_persistence_association_has_serializationMaxDepth():
    assert hasattr(persistence_Association, "serializationMaxDepth")
    descriptor = None
    for klass in persistence_Association.__mro__:
        if "serializationMaxDepth" in klass.__dict__:
            descriptor = klass.__dict__["serializationMaxDepth"]
            break
    assert isinstance(descriptor, property)

def test_persistence_association_has_inputColumnClass():
    assert hasattr(persistence_Association, "inputColumnClass")
    descriptor = None
    for klass in persistence_Association.__mro__:
        if "inputColumnClass" in klass.__dict__:
            descriptor = klass.__dict__["inputColumnClass"]
            break
    assert isinstance(descriptor, property)

def test_persistence_association_has_inputElementClass():
    assert hasattr(persistence_Association, "inputElementClass")
    descriptor = None
    for klass in persistence_Association.__mro__:
        if "inputElementClass" in klass.__dict__:
            descriptor = klass.__dict__["inputElementClass"]
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

def test_persistence_association_has_targetFeatureName():
    assert hasattr(persistence_Association, "targetFeatureName")
    descriptor = None
    for klass in persistence_Association.__mro__:
        if "targetFeatureName" in klass.__dict__:
            descriptor = klass.__dict__["targetFeatureName"]
            break
    assert isinstance(descriptor, property)

def test_persistence_association_has_targetColumnName():
    assert hasattr(persistence_Association, "targetColumnName")
    descriptor = None
    for klass in persistence_Association.__mro__:
        if "targetColumnName" in klass.__dict__:
            descriptor = klass.__dict__["targetColumnName"]
            break
    assert isinstance(descriptor, property)

def test_persistence_association_has_unique():
    assert hasattr(persistence_Association, "unique")
    descriptor = None
    for klass in persistence_Association.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)

def test_persistence_association_has_targetDisplayClass():
    assert hasattr(persistence_Association, "targetDisplayClass")
    descriptor = None
    for klass in persistence_Association.__mro__:
        if "targetDisplayClass" in klass.__dict__:
            descriptor = klass.__dict__["targetDisplayClass"]
            break
    assert isinstance(descriptor, property)



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
    assert "customise" in params, "Missing parameter 'customise'"

def test_persistence_modellabel_has_format():
    assert hasattr(persistence_ModelLabel, "format")
    descriptor = None
    for klass in persistence_ModelLabel.__mro__:
        if "format" in klass.__dict__:
            descriptor = klass.__dict__["format"]
            break
    assert isinstance(descriptor, property)

def test_persistence_modellabel_has_customise():
    assert hasattr(persistence_ModelLabel, "customise")
    descriptor = None
    for klass in persistence_ModelLabel.__mro__:
        if "customise" in klass.__dict__:
            descriptor = klass.__dict__["customise"]
            break
    assert isinstance(descriptor, property)



def test_persistence_entity_is_not_abstract():
    assert not inspect.isabstract(persistence_Entity)


def test_persistence_entity_constructor_exists():
    assert callable(persistence_Entity.__init__)


def test_persistence_entity_constructor_args():
    sig = inspect.signature(persistence_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "autoKeyPersistentType" in params, "Missing parameter 'autoKeyPersistentType'"
    assert "autoKeyName" in params, "Missing parameter 'autoKeyName'"
    assert "allowFormTypeCustomisation" in params, "Missing parameter 'allowFormTypeCustomisation'"
    assert "tableName" in params, "Missing parameter 'tableName'"
    assert "singletonName" in params, "Missing parameter 'singletonName'"
    assert "autoKeyGenerationStrategy" in params, "Missing parameter 'autoKeyGenerationStrategy'"
    assert "pluralisedName" in params, "Missing parameter 'pluralisedName'"
    assert "implementsUserInterface" in params, "Missing parameter 'implementsUserInterface'"

def test_persistence_entity_has_autoKeyPersistentType():
    assert hasattr(persistence_Entity, "autoKeyPersistentType")
    descriptor = None
    for klass in persistence_Entity.__mro__:
        if "autoKeyPersistentType" in klass.__dict__:
            descriptor = klass.__dict__["autoKeyPersistentType"]
            break
    assert isinstance(descriptor, property)

def test_persistence_entity_has_autoKeyName():
    assert hasattr(persistence_Entity, "autoKeyName")
    descriptor = None
    for klass in persistence_Entity.__mro__:
        if "autoKeyName" in klass.__dict__:
            descriptor = klass.__dict__["autoKeyName"]
            break
    assert isinstance(descriptor, property)

def test_persistence_entity_has_allowFormTypeCustomisation():
    assert hasattr(persistence_Entity, "allowFormTypeCustomisation")
    descriptor = None
    for klass in persistence_Entity.__mro__:
        if "allowFormTypeCustomisation" in klass.__dict__:
            descriptor = klass.__dict__["allowFormTypeCustomisation"]
            break
    assert isinstance(descriptor, property)

def test_persistence_entity_has_tableName():
    assert hasattr(persistence_Entity, "tableName")
    descriptor = None
    for klass in persistence_Entity.__mro__:
        if "tableName" in klass.__dict__:
            descriptor = klass.__dict__["tableName"]
            break
    assert isinstance(descriptor, property)

def test_persistence_entity_has_singletonName():
    assert hasattr(persistence_Entity, "singletonName")
    descriptor = None
    for klass in persistence_Entity.__mro__:
        if "singletonName" in klass.__dict__:
            descriptor = klass.__dict__["singletonName"]
            break
    assert isinstance(descriptor, property)

def test_persistence_entity_has_autoKeyGenerationStrategy():
    assert hasattr(persistence_Entity, "autoKeyGenerationStrategy")
    descriptor = None
    for klass in persistence_Entity.__mro__:
        if "autoKeyGenerationStrategy" in klass.__dict__:
            descriptor = klass.__dict__["autoKeyGenerationStrategy"]
            break
    assert isinstance(descriptor, property)

def test_persistence_entity_has_pluralisedName():
    assert hasattr(persistence_Entity, "pluralisedName")
    descriptor = None
    for klass in persistence_Entity.__mro__:
        if "pluralisedName" in klass.__dict__:
            descriptor = klass.__dict__["pluralisedName"]
            break
    assert isinstance(descriptor, property)

def test_persistence_entity_has_implementsUserInterface():
    assert hasattr(persistence_Entity, "implementsUserInterface")
    descriptor = None
    for klass in persistence_Entity.__mro__:
        if "implementsUserInterface" in klass.__dict__:
            descriptor = klass.__dict__["implementsUserInterface"]
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
    assert "databaseTechnology" in params, "Missing parameter 'databaseTechnology'"
    assert "timestampCreation" in params, "Missing parameter 'timestampCreation'"
    assert "ormTechnology" in params, "Missing parameter 'ormTechnology'"
    assert "timestampUpdates" in params, "Missing parameter 'timestampUpdates'"

def test_persistence_persistence_has_databaseTechnology():
    assert hasattr(persistence_Persistence, "databaseTechnology")
    descriptor = None
    for klass in persistence_Persistence.__mro__:
        if "databaseTechnology" in klass.__dict__:
            descriptor = klass.__dict__["databaseTechnology"]
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

def test_persistence_persistence_has_ormTechnology():
    assert hasattr(persistence_Persistence, "ormTechnology")
    descriptor = None
    for klass in persistence_Persistence.__mro__:
        if "ormTechnology" in klass.__dict__:
            descriptor = klass.__dict__["ormTechnology"]
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



def test_persistence_feature_is_not_abstract():
    assert not inspect.isabstract(persistence_Feature)


def test_persistence_feature_constructor_exists():
    assert callable(persistence_Feature.__init__)


def test_persistence_feature_constructor_args():
    sig = inspect.signature(persistence_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "singletonName" in params, "Missing parameter 'singletonName'"
    assert "pluralisedName" in params, "Missing parameter 'pluralisedName'"
    assert "primaryKey" in params, "Missing parameter 'primaryKey'"
    assert "collectionOrmAllowRemove" in params, "Missing parameter 'collectionOrmAllowRemove'"
    assert "booleanIsHasChoice" in params, "Missing parameter 'booleanIsHasChoice'"
    assert "encodeUriKey" in params, "Missing parameter 'encodeUriKey'"
    assert "footerClass" in params, "Missing parameter 'footerClass'"
    assert "collectionOrmAllowAdd" in params, "Missing parameter 'collectionOrmAllowAdd'"
    assert "headerClass" in params, "Missing parameter 'headerClass'"
    assert "columnName" in params, "Missing parameter 'columnName'"
    assert "customiseSet" in params, "Missing parameter 'customiseSet'"
    assert "derived" in params, "Missing parameter 'derived'"
    assert "displayClass" in params, "Missing parameter 'displayClass'"
    assert "emptyDisplayValue" in params, "Missing parameter 'emptyDisplayValue'"
    assert "ordered" in params, "Missing parameter 'ordered'"
    assert "defaultDisplayValue" in params, "Missing parameter 'defaultDisplayValue'"
    assert "cardinality" in params, "Missing parameter 'cardinality'"

def test_persistence_feature_has_title():
    assert hasattr(persistence_Feature, "title")
    descriptor = None
    for klass in persistence_Feature.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_persistence_feature_has_singletonName():
    assert hasattr(persistence_Feature, "singletonName")
    descriptor = None
    for klass in persistence_Feature.__mro__:
        if "singletonName" in klass.__dict__:
            descriptor = klass.__dict__["singletonName"]
            break
    assert isinstance(descriptor, property)

def test_persistence_feature_has_pluralisedName():
    assert hasattr(persistence_Feature, "pluralisedName")
    descriptor = None
    for klass in persistence_Feature.__mro__:
        if "pluralisedName" in klass.__dict__:
            descriptor = klass.__dict__["pluralisedName"]
            break
    assert isinstance(descriptor, property)

def test_persistence_feature_has_primaryKey():
    assert hasattr(persistence_Feature, "primaryKey")
    descriptor = None
    for klass in persistence_Feature.__mro__:
        if "primaryKey" in klass.__dict__:
            descriptor = klass.__dict__["primaryKey"]
            break
    assert isinstance(descriptor, property)

def test_persistence_feature_has_collectionOrmAllowRemove():
    assert hasattr(persistence_Feature, "collectionOrmAllowRemove")
    descriptor = None
    for klass in persistence_Feature.__mro__:
        if "collectionOrmAllowRemove" in klass.__dict__:
            descriptor = klass.__dict__["collectionOrmAllowRemove"]
            break
    assert isinstance(descriptor, property)

def test_persistence_feature_has_booleanIsHasChoice():
    assert hasattr(persistence_Feature, "booleanIsHasChoice")
    descriptor = None
    for klass in persistence_Feature.__mro__:
        if "booleanIsHasChoice" in klass.__dict__:
            descriptor = klass.__dict__["booleanIsHasChoice"]
            break
    assert isinstance(descriptor, property)

def test_persistence_feature_has_encodeUriKey():
    assert hasattr(persistence_Feature, "encodeUriKey")
    descriptor = None
    for klass in persistence_Feature.__mro__:
        if "encodeUriKey" in klass.__dict__:
            descriptor = klass.__dict__["encodeUriKey"]
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

def test_persistence_feature_has_collectionOrmAllowAdd():
    assert hasattr(persistence_Feature, "collectionOrmAllowAdd")
    descriptor = None
    for klass in persistence_Feature.__mro__:
        if "collectionOrmAllowAdd" in klass.__dict__:
            descriptor = klass.__dict__["collectionOrmAllowAdd"]
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

def test_persistence_feature_has_columnName():
    assert hasattr(persistence_Feature, "columnName")
    descriptor = None
    for klass in persistence_Feature.__mro__:
        if "columnName" in klass.__dict__:
            descriptor = klass.__dict__["columnName"]
            break
    assert isinstance(descriptor, property)

def test_persistence_feature_has_customiseSet():
    assert hasattr(persistence_Feature, "customiseSet")
    descriptor = None
    for klass in persistence_Feature.__mro__:
        if "customiseSet" in klass.__dict__:
            descriptor = klass.__dict__["customiseSet"]
            break
    assert isinstance(descriptor, property)

def test_persistence_feature_has_derived():
    assert hasattr(persistence_Feature, "derived")
    descriptor = None
    for klass in persistence_Feature.__mro__:
        if "derived" in klass.__dict__:
            descriptor = klass.__dict__["derived"]
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

def test_persistence_feature_has_emptyDisplayValue():
    assert hasattr(persistence_Feature, "emptyDisplayValue")
    descriptor = None
    for klass in persistence_Feature.__mro__:
        if "emptyDisplayValue" in klass.__dict__:
            descriptor = klass.__dict__["emptyDisplayValue"]
            break
    assert isinstance(descriptor, property)

def test_persistence_feature_has_ordered():
    assert hasattr(persistence_Feature, "ordered")
    descriptor = None
    for klass in persistence_Feature.__mro__:
        if "ordered" in klass.__dict__:
            descriptor = klass.__dict__["ordered"]
            break
    assert isinstance(descriptor, property)

def test_persistence_feature_has_defaultDisplayValue():
    assert hasattr(persistence_Feature, "defaultDisplayValue")
    descriptor = None
    for klass in persistence_Feature.__mro__:
        if "defaultDisplayValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultDisplayValue"]
            break
    assert isinstance(descriptor, property)

def test_persistence_feature_has_cardinality():
    assert hasattr(persistence_Feature, "cardinality")
    descriptor = None
    for klass in persistence_Feature.__mro__:
        if "cardinality" in klass.__dict__:
            descriptor = klass.__dict__["cardinality"]
            break
    assert isinstance(descriptor, property)

def test_cardinality_exists():
    # Check that the Enumeration exists
    assert Cardinality is not None

def test_cardinality_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Cardinality]
    expected_literals = [
        "Optional",
        "Many",
        "Required",
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

def test_datedetails_exists():
    # Check that the Enumeration exists
    assert DateDetails is not None

def test_datedetails_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DateDetails]
    expected_literals = [
        "TimeOnly",
        "DateOnly",
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
        "Idiorm",
        "Kohana",
        "DataMapper",
        "JPA",
        "DoctrineORM",
        "DoctrineODM",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OrmTechnologies"


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
persistence_AssociationWithContainment_strategy = st.builds(
    persistence_AssociationWithContainment,
    sourceVisible=
        st.booleans()
)
persistence_AssociationWithoutContainment_strategy = st.builds(
    persistence_AssociationWithoutContainment,
    targetCardinality=
        safe_text,
    targetUnique=
        st.booleans()
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
Attribute_strategy = st.builds(
    Attribute,
)
persistence_UrlAttribute_strategy = st.builds(
    persistence_UrlAttribute,
    displayValue=
        safe_text
)
persistence_DateAttribute_strategy = st.builds(
    persistence_DateAttribute,
    details=
        safe_text,
    format=
        safe_text
)
persistence_LocationAttribute_strategy = st.builds(
    persistence_LocationAttribute,
)
persistence_ResourceAttribute_strategy = st.builds(
    persistence_ResourceAttribute,
    maximumUploadSize=
        st.integers(),
    uploadsWithinWebsite=
        st.booleans(),
    validUploadExtensions=
        safe_text,
    validUploadMimeTypes=
        safe_text
)
persistence_DataTypeAttribute_strategy = st.builds(
    persistence_DataTypeAttribute,
    encrypt=
        st.booleans(),
    caseInsensitive=
        st.booleans(),
    obfuscateFormFields=
        st.booleans()
)
persistence_PathElement_strategy = st.builds(
    persistence_PathElement,
)
Classifier_strategy = st.builds(
    Classifier,
)
ModelLabelFeature_strategy = st.builds(
    ModelLabelFeature,
)
persistence_ModelLabelAssociation_strategy = st.builds(
    persistence_ModelLabelAssociation,
    isSourceAssociation=
        st.booleans()
)
persistence_ModelLabelAttribute_strategy = st.builds(
    persistence_ModelLabelAttribute,
    dateFormat=
        safe_text
)
persistence_ModelLabelFeature_strategy = st.builds(
    persistence_ModelLabelFeature,
)
persistence_Label_strategy = st.builds(
    persistence_Label,
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
persistence_Attribute_strategy = st.builds(
    persistence_Attribute,
    ormType=
        safe_text,
    persistentType=
        safe_text,
    hidden=
        st.booleans(),
    unique=
        st.booleans(),
    placeholder=
        safe_text,
    inputColumnClass=
        safe_text,
    interfaceType=
        safe_text,
    inputElementClass=
        safe_text,
    validationPattern=
        safe_text,
    containerUnique=
        st.booleans()
)
NamedDisplayElement_strategy = st.builds(
    NamedDisplayElement,
)
persistence_AssociationKey_strategy = st.builds(
    persistence_AssociationKey,
)
persistence_Association_strategy = st.builds(
    persistence_Association,
    bidirectional=
        st.booleans(),
    targetPrimaryKey=
        st.booleans(),
    pivotTableName=
        safe_text,
    targetDisplayLabel=
        safe_text,
    targetInputClass=
        safe_text,
    targetHeaderClass=
        safe_text,
    targetFooterClass=
        safe_text,
    serializationMaxDepth=
        st.integers(),
    inputColumnClass=
        safe_text,
    inputElementClass=
        safe_text,
    pseudo=
        st.booleans(),
    targetFeatureName=
        safe_text,
    targetColumnName=
        safe_text,
    unique=
        st.booleans(),
    targetDisplayClass=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
persistence_ModelLabel_strategy = st.builds(
    persistence_ModelLabel,
    format=
        safe_text,
    customise=
        st.booleans()
)
persistence_Entity_strategy = st.builds(
    persistence_Entity,
    autoKeyPersistentType=
        safe_text,
    autoKeyName=
        safe_text,
    allowFormTypeCustomisation=
        st.booleans(),
    tableName=
        safe_text,
    singletonName=
        safe_text,
    autoKeyGenerationStrategy=
        safe_text,
    pluralisedName=
        safe_text,
    implementsUserInterface=
        st.booleans()
)
persistence_DataType_strategy = st.builds(
    persistence_DataType,
)
persistence_SerializationGroup_strategy = st.builds(
    persistence_SerializationGroup,
)
persistence_Persistence_strategy = st.builds(
    persistence_Persistence,
    databaseTechnology=
        safe_text,
    timestampCreation=
        st.booleans(),
    ormTechnology=
        safe_text,
    timestampUpdates=
        st.booleans()
)
persistence_Feature_strategy = st.builds(
    persistence_Feature,
    title=
        safe_text,
    singletonName=
        safe_text,
    pluralisedName=
        safe_text,
    primaryKey=
        st.booleans(),
    collectionOrmAllowRemove=
        st.booleans(),
    booleanIsHasChoice=
        safe_text,
    encodeUriKey=
        st.booleans(),
    footerClass=
        safe_text,
    collectionOrmAllowAdd=
        st.booleans(),
    headerClass=
        safe_text,
    columnName=
        safe_text,
    customiseSet=
        st.booleans(),
    derived=
        st.booleans(),
    displayClass=
        safe_text,
    emptyDisplayValue=
        safe_text,
    ordered=
        st.booleans(),
    defaultDisplayValue=
        safe_text,
    cardinality=
        safe_text
)

@given(instance=Association_strategy)
@settings(max_examples=50)
def test_association_instantiation(instance):
    assert isinstance(instance, Association)

@given(instance=persistence_AssociationWithContainment_strategy)
@settings(max_examples=50)
def test_persistence_associationwithcontainment_instantiation(instance):
    assert isinstance(instance, persistence_AssociationWithContainment)



@given(instance=persistence_AssociationWithContainment_strategy)
def test_persistence_associationwithcontainment_sourceVisible_setter(instance):
    original = instance.sourceVisible
    instance.sourceVisible = original
    assert instance.sourceVisible == original

@given(instance=persistence_AssociationWithoutContainment_strategy)
@settings(max_examples=50)
def test_persistence_associationwithoutcontainment_instantiation(instance):
    assert isinstance(instance, persistence_AssociationWithoutContainment)



@given(instance=persistence_AssociationWithoutContainment_strategy)
def test_persistence_associationwithoutcontainment_targetCardinality_setter(instance):
    original = instance.targetCardinality
    instance.targetCardinality = original
    assert instance.targetCardinality == original



@given(instance=persistence_AssociationWithoutContainment_strategy)
def test_persistence_associationwithoutcontainment_targetUnique_setter(instance):
    original = instance.targetUnique
    instance.targetUnique = original
    assert instance.targetUnique == original

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

@given(instance=Attribute_strategy)
@settings(max_examples=50)
def test_attribute_instantiation(instance):
    assert isinstance(instance, Attribute)

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
def test_persistence_dateattribute_details_setter(instance):
    original = instance.details
    instance.details = original
    assert instance.details == original



@given(instance=persistence_DateAttribute_strategy)
def test_persistence_dateattribute_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original

@given(instance=persistence_LocationAttribute_strategy)
@settings(max_examples=50)
def test_persistence_locationattribute_instantiation(instance):
    assert isinstance(instance, persistence_LocationAttribute)

@given(instance=persistence_ResourceAttribute_strategy)
@settings(max_examples=50)
def test_persistence_resourceattribute_instantiation(instance):
    assert isinstance(instance, persistence_ResourceAttribute)



@given(instance=persistence_ResourceAttribute_strategy)
def test_persistence_resourceattribute_maximumUploadSize_setter(instance):
    original = instance.maximumUploadSize
    instance.maximumUploadSize = original
    assert instance.maximumUploadSize == original



@given(instance=persistence_ResourceAttribute_strategy)
def test_persistence_resourceattribute_uploadsWithinWebsite_setter(instance):
    original = instance.uploadsWithinWebsite
    instance.uploadsWithinWebsite = original
    assert instance.uploadsWithinWebsite == original



@given(instance=persistence_ResourceAttribute_strategy)
def test_persistence_resourceattribute_validUploadExtensions_setter(instance):
    original = instance.validUploadExtensions
    instance.validUploadExtensions = original
    assert instance.validUploadExtensions == original



@given(instance=persistence_ResourceAttribute_strategy)
def test_persistence_resourceattribute_validUploadMimeTypes_setter(instance):
    original = instance.validUploadMimeTypes
    instance.validUploadMimeTypes = original
    assert instance.validUploadMimeTypes == original

@given(instance=persistence_DataTypeAttribute_strategy)
@settings(max_examples=50)
def test_persistence_datatypeattribute_instantiation(instance):
    assert isinstance(instance, persistence_DataTypeAttribute)



@given(instance=persistence_DataTypeAttribute_strategy)
def test_persistence_datatypeattribute_encrypt_setter(instance):
    original = instance.encrypt
    instance.encrypt = original
    assert instance.encrypt == original



@given(instance=persistence_DataTypeAttribute_strategy)
def test_persistence_datatypeattribute_caseInsensitive_setter(instance):
    original = instance.caseInsensitive
    instance.caseInsensitive = original
    assert instance.caseInsensitive == original



@given(instance=persistence_DataTypeAttribute_strategy)
def test_persistence_datatypeattribute_obfuscateFormFields_setter(instance):
    original = instance.obfuscateFormFields
    instance.obfuscateFormFields = original
    assert instance.obfuscateFormFields == original

@given(instance=persistence_PathElement_strategy)
@settings(max_examples=50)
def test_persistence_pathelement_instantiation(instance):
    assert isinstance(instance, persistence_PathElement)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=ModelLabelFeature_strategy)
@settings(max_examples=50)
def test_modellabelfeature_instantiation(instance):
    assert isinstance(instance, ModelLabelFeature)

@given(instance=persistence_ModelLabelAssociation_strategy)
@settings(max_examples=50)
def test_persistence_modellabelassociation_instantiation(instance):
    assert isinstance(instance, persistence_ModelLabelAssociation)



@given(instance=persistence_ModelLabelAssociation_strategy)
def test_persistence_modellabelassociation_isSourceAssociation_setter(instance):
    original = instance.isSourceAssociation
    instance.isSourceAssociation = original
    assert instance.isSourceAssociation == original

@given(instance=persistence_ModelLabelAttribute_strategy)
@settings(max_examples=50)
def test_persistence_modellabelattribute_instantiation(instance):
    assert isinstance(instance, persistence_ModelLabelAttribute)



@given(instance=persistence_ModelLabelAttribute_strategy)
def test_persistence_modellabelattribute_dateFormat_setter(instance):
    original = instance.dateFormat
    instance.dateFormat = original
    assert instance.dateFormat == original

@given(instance=persistence_ModelLabelFeature_strategy)
@settings(max_examples=50)
def test_persistence_modellabelfeature_instantiation(instance):
    assert isinstance(instance, persistence_ModelLabelFeature)

@given(instance=persistence_Label_strategy)
@settings(max_examples=50)
def test_persistence_label_instantiation(instance):
    assert isinstance(instance, persistence_Label)

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

@given(instance=persistence_Attribute_strategy)
@settings(max_examples=50)
def test_persistence_attribute_instantiation(instance):
    assert isinstance(instance, persistence_Attribute)



@given(instance=persistence_Attribute_strategy)
def test_persistence_attribute_ormType_setter(instance):
    original = instance.ormType
    instance.ormType = original
    assert instance.ormType == original



@given(instance=persistence_Attribute_strategy)
def test_persistence_attribute_persistentType_setter(instance):
    original = instance.persistentType
    instance.persistentType = original
    assert instance.persistentType == original



@given(instance=persistence_Attribute_strategy)
def test_persistence_attribute_hidden_setter(instance):
    original = instance.hidden
    instance.hidden = original
    assert instance.hidden == original



@given(instance=persistence_Attribute_strategy)
def test_persistence_attribute_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original



@given(instance=persistence_Attribute_strategy)
def test_persistence_attribute_placeholder_setter(instance):
    original = instance.placeholder
    instance.placeholder = original
    assert instance.placeholder == original



@given(instance=persistence_Attribute_strategy)
def test_persistence_attribute_inputColumnClass_setter(instance):
    original = instance.inputColumnClass
    instance.inputColumnClass = original
    assert instance.inputColumnClass == original



@given(instance=persistence_Attribute_strategy)
def test_persistence_attribute_interfaceType_setter(instance):
    original = instance.interfaceType
    instance.interfaceType = original
    assert instance.interfaceType == original



@given(instance=persistence_Attribute_strategy)
def test_persistence_attribute_inputElementClass_setter(instance):
    original = instance.inputElementClass
    instance.inputElementClass = original
    assert instance.inputElementClass == original



@given(instance=persistence_Attribute_strategy)
def test_persistence_attribute_validationPattern_setter(instance):
    original = instance.validationPattern
    instance.validationPattern = original
    assert instance.validationPattern == original



@given(instance=persistence_Attribute_strategy)
def test_persistence_attribute_containerUnique_setter(instance):
    original = instance.containerUnique
    instance.containerUnique = original
    assert instance.containerUnique == original

@given(instance=NamedDisplayElement_strategy)
@settings(max_examples=50)
def test_nameddisplayelement_instantiation(instance):
    assert isinstance(instance, NamedDisplayElement)

@given(instance=persistence_AssociationKey_strategy)
@settings(max_examples=50)
def test_persistence_associationkey_instantiation(instance):
    assert isinstance(instance, persistence_AssociationKey)

@given(instance=persistence_Association_strategy)
@settings(max_examples=50)
def test_persistence_association_instantiation(instance):
    assert isinstance(instance, persistence_Association)



@given(instance=persistence_Association_strategy)
def test_persistence_association_bidirectional_setter(instance):
    original = instance.bidirectional
    instance.bidirectional = original
    assert instance.bidirectional == original



@given(instance=persistence_Association_strategy)
def test_persistence_association_targetPrimaryKey_setter(instance):
    original = instance.targetPrimaryKey
    instance.targetPrimaryKey = original
    assert instance.targetPrimaryKey == original



@given(instance=persistence_Association_strategy)
def test_persistence_association_pivotTableName_setter(instance):
    original = instance.pivotTableName
    instance.pivotTableName = original
    assert instance.pivotTableName == original



@given(instance=persistence_Association_strategy)
def test_persistence_association_targetDisplayLabel_setter(instance):
    original = instance.targetDisplayLabel
    instance.targetDisplayLabel = original
    assert instance.targetDisplayLabel == original



@given(instance=persistence_Association_strategy)
def test_persistence_association_targetInputClass_setter(instance):
    original = instance.targetInputClass
    instance.targetInputClass = original
    assert instance.targetInputClass == original



@given(instance=persistence_Association_strategy)
def test_persistence_association_targetHeaderClass_setter(instance):
    original = instance.targetHeaderClass
    instance.targetHeaderClass = original
    assert instance.targetHeaderClass == original



@given(instance=persistence_Association_strategy)
def test_persistence_association_targetFooterClass_setter(instance):
    original = instance.targetFooterClass
    instance.targetFooterClass = original
    assert instance.targetFooterClass == original



@given(instance=persistence_Association_strategy)
def test_persistence_association_serializationMaxDepth_setter(instance):
    original = instance.serializationMaxDepth
    instance.serializationMaxDepth = original
    assert instance.serializationMaxDepth == original



@given(instance=persistence_Association_strategy)
def test_persistence_association_inputColumnClass_setter(instance):
    original = instance.inputColumnClass
    instance.inputColumnClass = original
    assert instance.inputColumnClass == original



@given(instance=persistence_Association_strategy)
def test_persistence_association_inputElementClass_setter(instance):
    original = instance.inputElementClass
    instance.inputElementClass = original
    assert instance.inputElementClass == original



@given(instance=persistence_Association_strategy)
def test_persistence_association_pseudo_setter(instance):
    original = instance.pseudo
    instance.pseudo = original
    assert instance.pseudo == original



@given(instance=persistence_Association_strategy)
def test_persistence_association_targetFeatureName_setter(instance):
    original = instance.targetFeatureName
    instance.targetFeatureName = original
    assert instance.targetFeatureName == original



@given(instance=persistence_Association_strategy)
def test_persistence_association_targetColumnName_setter(instance):
    original = instance.targetColumnName
    instance.targetColumnName = original
    assert instance.targetColumnName == original



@given(instance=persistence_Association_strategy)
def test_persistence_association_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original



@given(instance=persistence_Association_strategy)
def test_persistence_association_targetDisplayClass_setter(instance):
    original = instance.targetDisplayClass
    instance.targetDisplayClass = original
    assert instance.targetDisplayClass == original

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



@given(instance=persistence_ModelLabel_strategy)
def test_persistence_modellabel_customise_setter(instance):
    original = instance.customise
    instance.customise = original
    assert instance.customise == original

@given(instance=persistence_Entity_strategy)
@settings(max_examples=50)
def test_persistence_entity_instantiation(instance):
    assert isinstance(instance, persistence_Entity)



@given(instance=persistence_Entity_strategy)
def test_persistence_entity_autoKeyPersistentType_setter(instance):
    original = instance.autoKeyPersistentType
    instance.autoKeyPersistentType = original
    assert instance.autoKeyPersistentType == original



@given(instance=persistence_Entity_strategy)
def test_persistence_entity_autoKeyName_setter(instance):
    original = instance.autoKeyName
    instance.autoKeyName = original
    assert instance.autoKeyName == original



@given(instance=persistence_Entity_strategy)
def test_persistence_entity_allowFormTypeCustomisation_setter(instance):
    original = instance.allowFormTypeCustomisation
    instance.allowFormTypeCustomisation = original
    assert instance.allowFormTypeCustomisation == original



@given(instance=persistence_Entity_strategy)
def test_persistence_entity_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original



@given(instance=persistence_Entity_strategy)
def test_persistence_entity_singletonName_setter(instance):
    original = instance.singletonName
    instance.singletonName = original
    assert instance.singletonName == original



@given(instance=persistence_Entity_strategy)
def test_persistence_entity_autoKeyGenerationStrategy_setter(instance):
    original = instance.autoKeyGenerationStrategy
    instance.autoKeyGenerationStrategy = original
    assert instance.autoKeyGenerationStrategy == original



@given(instance=persistence_Entity_strategy)
def test_persistence_entity_pluralisedName_setter(instance):
    original = instance.pluralisedName
    instance.pluralisedName = original
    assert instance.pluralisedName == original



@given(instance=persistence_Entity_strategy)
def test_persistence_entity_implementsUserInterface_setter(instance):
    original = instance.implementsUserInterface
    instance.implementsUserInterface = original
    assert instance.implementsUserInterface == original

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
def test_persistence_persistence_databaseTechnology_setter(instance):
    original = instance.databaseTechnology
    instance.databaseTechnology = original
    assert instance.databaseTechnology == original



@given(instance=persistence_Persistence_strategy)
def test_persistence_persistence_timestampCreation_setter(instance):
    original = instance.timestampCreation
    instance.timestampCreation = original
    assert instance.timestampCreation == original



@given(instance=persistence_Persistence_strategy)
def test_persistence_persistence_ormTechnology_setter(instance):
    original = instance.ormTechnology
    instance.ormTechnology = original
    assert instance.ormTechnology == original



@given(instance=persistence_Persistence_strategy)
def test_persistence_persistence_timestampUpdates_setter(instance):
    original = instance.timestampUpdates
    instance.timestampUpdates = original
    assert instance.timestampUpdates == original

@given(instance=persistence_Feature_strategy)
@settings(max_examples=50)
def test_persistence_feature_instantiation(instance):
    assert isinstance(instance, persistence_Feature)



@given(instance=persistence_Feature_strategy)
def test_persistence_feature_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=persistence_Feature_strategy)
def test_persistence_feature_singletonName_setter(instance):
    original = instance.singletonName
    instance.singletonName = original
    assert instance.singletonName == original



@given(instance=persistence_Feature_strategy)
def test_persistence_feature_pluralisedName_setter(instance):
    original = instance.pluralisedName
    instance.pluralisedName = original
    assert instance.pluralisedName == original



@given(instance=persistence_Feature_strategy)
def test_persistence_feature_primaryKey_setter(instance):
    original = instance.primaryKey
    instance.primaryKey = original
    assert instance.primaryKey == original



@given(instance=persistence_Feature_strategy)
def test_persistence_feature_collectionOrmAllowRemove_setter(instance):
    original = instance.collectionOrmAllowRemove
    instance.collectionOrmAllowRemove = original
    assert instance.collectionOrmAllowRemove == original



@given(instance=persistence_Feature_strategy)
def test_persistence_feature_booleanIsHasChoice_setter(instance):
    original = instance.booleanIsHasChoice
    instance.booleanIsHasChoice = original
    assert instance.booleanIsHasChoice == original



@given(instance=persistence_Feature_strategy)
def test_persistence_feature_encodeUriKey_setter(instance):
    original = instance.encodeUriKey
    instance.encodeUriKey = original
    assert instance.encodeUriKey == original



@given(instance=persistence_Feature_strategy)
def test_persistence_feature_footerClass_setter(instance):
    original = instance.footerClass
    instance.footerClass = original
    assert instance.footerClass == original



@given(instance=persistence_Feature_strategy)
def test_persistence_feature_collectionOrmAllowAdd_setter(instance):
    original = instance.collectionOrmAllowAdd
    instance.collectionOrmAllowAdd = original
    assert instance.collectionOrmAllowAdd == original



@given(instance=persistence_Feature_strategy)
def test_persistence_feature_headerClass_setter(instance):
    original = instance.headerClass
    instance.headerClass = original
    assert instance.headerClass == original



@given(instance=persistence_Feature_strategy)
def test_persistence_feature_columnName_setter(instance):
    original = instance.columnName
    instance.columnName = original
    assert instance.columnName == original



@given(instance=persistence_Feature_strategy)
def test_persistence_feature_customiseSet_setter(instance):
    original = instance.customiseSet
    instance.customiseSet = original
    assert instance.customiseSet == original



@given(instance=persistence_Feature_strategy)
def test_persistence_feature_derived_setter(instance):
    original = instance.derived
    instance.derived = original
    assert instance.derived == original



@given(instance=persistence_Feature_strategy)
def test_persistence_feature_displayClass_setter(instance):
    original = instance.displayClass
    instance.displayClass = original
    assert instance.displayClass == original



@given(instance=persistence_Feature_strategy)
def test_persistence_feature_emptyDisplayValue_setter(instance):
    original = instance.emptyDisplayValue
    instance.emptyDisplayValue = original
    assert instance.emptyDisplayValue == original



@given(instance=persistence_Feature_strategy)
def test_persistence_feature_ordered_setter(instance):
    original = instance.ordered
    instance.ordered = original
    assert instance.ordered == original



@given(instance=persistence_Feature_strategy)
def test_persistence_feature_defaultDisplayValue_setter(instance):
    original = instance.defaultDisplayValue
    instance.defaultDisplayValue = original
    assert instance.defaultDisplayValue == original



@given(instance=persistence_Feature_strategy)
def test_persistence_feature_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original
