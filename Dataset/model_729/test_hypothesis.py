import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    rif12_DataTypes_XmlContent,
    rif12_DataTypes_XhtmlContent,
    rif12_DataTypes_BinaryContent,
    rif12_ExchangeFile_RIFToolExtension,
    AccessPolicy,
    rif12_ExchangeFile_RIFContent,
    rif12_ExchangeFile_RIFHeader,
    RIFToolExtension,
    RIFContent,
    RIFHeader,
    rif12_ExchangeFile_RIF,
    AttributeValueSimple,
    DatatypeDefinitionSimple,
    rif12_ExchangeFile_DatatypeDefinitionInteger,
    rif12_ExchangeFile_DatatypeDefinitionString,
    rif12_ExchangeFile_DatatypeDefinitionReal,
    AttributeDefinitionEnumeration,
    rif12_ExchangeFile_DatatypeDefinitionDate,
    rif12_ExchangeFile_DatatypeDefinitionBoolean,
    DataTypes_XmlContent,
    DataTypes_BinaryContent,
    DataTypes_XhtmlContent,
    AttributeDefinitionComplex,
    AttributeDefinitionSimple,
    SpecHierarchyRoot,
    DatatypeDefinition,
    rif12_ExchangeFile_DatatypeDefinitionSimple,
    rif12_ExchangeFile_EmbeddedValue,
    EmbeddedValue,
    EnumValue,
    rif12_ExchangeFile_DatatypeDefinitionEnumeration,
    AttributeValueEnumeration,
    DatatypeDefinitionEnumeration,
    rif12_ExchangeFile_DatatypeDefinitionComplex,
    AttributeValueComplex,
    rif12_ExchangeFile_AttributeValueEmbeddedFile,
    rif12_ExchangeFile_AttributeValueEmbeddedDocument,
    rif12_ExchangeFile_AttributeValueFileReference,
    rif12_ExchangeFile_AttributeValueXmlData,
    DatatypeDefinitionComplex,
    rif12_ExchangeFile_DatatypeDefinitionDocument,
    rif12_ExchangeFile_DatatypeDefinitionBinaryFile,
    rif12_ExchangeFile_DatatypeDefinitionXmlData,
    SpecGroupHierarchy,
    SpecObject,
    AttributeDefinition,
    rif12_ExchangeFile_AttributeDefinitionEnumeration,
    rif12_ExchangeFile_AttributeDefinitionComplex,
    rif12_ExchangeFile_AttributeDefinitionSimple,
    SpecGroup,
    SpecGroupHierarchyRoot,
    SpecRelation,
    RelationGroup,
    rif12_ExchangeFile_Identifiable,
    AttributeValue,
    rif12_ExchangeFile_AttributeValueEnumeration,
    rif12_ExchangeFile_AttributeValueSimple,
    rif12_ExchangeFile_AttributeValueComplex,
    SpecType,
    Identifiable,
    rif12_ExchangeFile_AttributeDefinition,
    rif12_ExchangeFile_SpecGroupHierarchy,
    rif12_ExchangeFile_DatatypeDefinition,
    rif12_ExchangeFile_SpecType,
    rif12_ExchangeFile_RelationGroup,
    rif12_ExchangeFile_AttributeValue,
    rif12_ExchangeFile_SpecHierarchy,
    rif12_ExchangeFile_AccessPolicy,
    rif12_ExchangeFile_EnumValue,
    rif12_ExchangeFile_SpecElementWithUserDefinedAttributes,
    SpecHierarchy,
    SpecElementWithUserDefinedAttributes,
    rif12_ExchangeFile_SpecGroup,
    rif12_ExchangeFile_SpecGroupHierarchyRoot,
    rif12_ExchangeFile_SpecRelation,
    rif12_ExchangeFile_SpecObject,
    rif12_ExchangeFile_SpecHierarchyRoot,
    DatatypeDefinitionDateFormatEnum,
    AccessPolicyAccessModeEnum,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rif12_datatypes_xmlcontent_is_not_abstract():
    assert not inspect.isabstract(rif12_DataTypes_XmlContent)


def test_rif12_datatypes_xmlcontent_constructor_exists():
    assert callable(rif12_DataTypes_XmlContent.__init__)


def test_rif12_datatypes_xmlcontent_constructor_args():
    sig = inspect.signature(rif12_DataTypes_XmlContent.__init__)
    params = list(sig.parameters.keys())



def test_rif12_datatypes_xhtmlcontent_is_not_abstract():
    assert not inspect.isabstract(rif12_DataTypes_XhtmlContent)


def test_rif12_datatypes_xhtmlcontent_constructor_exists():
    assert callable(rif12_DataTypes_XhtmlContent.__init__)


def test_rif12_datatypes_xhtmlcontent_constructor_args():
    sig = inspect.signature(rif12_DataTypes_XhtmlContent.__init__)
    params = list(sig.parameters.keys())



def test_rif12_datatypes_binarycontent_is_not_abstract():
    assert not inspect.isabstract(rif12_DataTypes_BinaryContent)


def test_rif12_datatypes_binarycontent_constructor_exists():
    assert callable(rif12_DataTypes_BinaryContent.__init__)


def test_rif12_datatypes_binarycontent_constructor_args():
    sig = inspect.signature(rif12_DataTypes_BinaryContent.__init__)
    params = list(sig.parameters.keys())



def test_rif12_exchangefile_riftoolextension_is_not_abstract():
    assert not inspect.isabstract(rif12_ExchangeFile_RIFToolExtension)


def test_rif12_exchangefile_riftoolextension_constructor_exists():
    assert callable(rif12_ExchangeFile_RIFToolExtension.__init__)


def test_rif12_exchangefile_riftoolextension_constructor_args():
    sig = inspect.signature(rif12_ExchangeFile_RIFToolExtension.__init__)
    params = list(sig.parameters.keys())



def test_accesspolicy_is_not_abstract():
    assert not inspect.isabstract(AccessPolicy)


def test_accesspolicy_constructor_exists():
    assert callable(AccessPolicy.__init__)


def test_accesspolicy_constructor_args():
    sig = inspect.signature(AccessPolicy.__init__)
    params = list(sig.parameters.keys())



def test_rif12_exchangefile_rifcontent_is_not_abstract():
    assert not inspect.isabstract(rif12_ExchangeFile_RIFContent)


def test_rif12_exchangefile_rifcontent_constructor_exists():
    assert callable(rif12_ExchangeFile_RIFContent.__init__)


def test_rif12_exchangefile_rifcontent_constructor_args():
    sig = inspect.signature(rif12_ExchangeFile_RIFContent.__init__)
    params = list(sig.parameters.keys())



def test_rif12_exchangefile_rifheader_is_not_abstract():
    assert not inspect.isabstract(rif12_ExchangeFile_RIFHeader)


def test_rif12_exchangefile_rifheader_constructor_exists():
    assert callable(rif12_ExchangeFile_RIFHeader.__init__)


def test_rif12_exchangefile_rifheader_constructor_args():
    sig = inspect.signature(rif12_ExchangeFile_RIFHeader.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "creationTime" in params, "Missing parameter 'creationTime'"
    assert "title" in params, "Missing parameter 'title'"
    assert "sourceToolId" in params, "Missing parameter 'sourceToolId'"
    assert "author" in params, "Missing parameter 'author'"
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_rif12_exchangefile_rifheader_has_comment():
    assert hasattr(rif12_ExchangeFile_RIFHeader, "comment")
    descriptor = None
    for klass in rif12_ExchangeFile_RIFHeader.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_rif12_exchangefile_rifheader_has_creationTime():
    assert hasattr(rif12_ExchangeFile_RIFHeader, "creationTime")
    descriptor = None
    for klass in rif12_ExchangeFile_RIFHeader.__mro__:
        if "creationTime" in klass.__dict__:
            descriptor = klass.__dict__["creationTime"]
            break
    assert isinstance(descriptor, property)

def test_rif12_exchangefile_rifheader_has_title():
    assert hasattr(rif12_ExchangeFile_RIFHeader, "title")
    descriptor = None
    for klass in rif12_ExchangeFile_RIFHeader.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_rif12_exchangefile_rifheader_has_sourceToolId():
    assert hasattr(rif12_ExchangeFile_RIFHeader, "sourceToolId")
    descriptor = None
    for klass in rif12_ExchangeFile_RIFHeader.__mro__:
        if "sourceToolId" in klass.__dict__:
            descriptor = klass.__dict__["sourceToolId"]
            break
    assert isinstance(descriptor, property)

def test_rif12_exchangefile_rifheader_has_author():
    assert hasattr(rif12_ExchangeFile_RIFHeader, "author")
    descriptor = None
    for klass in rif12_ExchangeFile_RIFHeader.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_rif12_exchangefile_rifheader_has_identifier():
    assert hasattr(rif12_ExchangeFile_RIFHeader, "identifier")
    descriptor = None
    for klass in rif12_ExchangeFile_RIFHeader.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_riftoolextension_is_not_abstract():
    assert not inspect.isabstract(RIFToolExtension)


def test_riftoolextension_constructor_exists():
    assert callable(RIFToolExtension.__init__)


def test_riftoolextension_constructor_args():
    sig = inspect.signature(RIFToolExtension.__init__)
    params = list(sig.parameters.keys())



def test_rifcontent_is_not_abstract():
    assert not inspect.isabstract(RIFContent)


def test_rifcontent_constructor_exists():
    assert callable(RIFContent.__init__)


def test_rifcontent_constructor_args():
    sig = inspect.signature(RIFContent.__init__)
    params = list(sig.parameters.keys())



def test_rifheader_is_not_abstract():
    assert not inspect.isabstract(RIFHeader)


def test_rifheader_constructor_exists():
    assert callable(RIFHeader.__init__)


def test_rifheader_constructor_args():
    sig = inspect.signature(RIFHeader.__init__)
    params = list(sig.parameters.keys())



def test_rif12_exchangefile_rif_is_not_abstract():
    assert not inspect.isabstract(rif12_ExchangeFile_RIF)


def test_rif12_exchangefile_rif_constructor_exists():
    assert callable(rif12_ExchangeFile_RIF.__init__)


def test_rif12_exchangefile_rif_constructor_args():
    sig = inspect.signature(rif12_ExchangeFile_RIF.__init__)
    params = list(sig.parameters.keys())



def test_attributevaluesimple_is_not_abstract():
    assert not inspect.isabstract(AttributeValueSimple)


def test_attributevaluesimple_constructor_exists():
    assert callable(AttributeValueSimple.__init__)


def test_attributevaluesimple_constructor_args():
    sig = inspect.signature(AttributeValueSimple.__init__)
    params = list(sig.parameters.keys())



def test_datatypedefinitionsimple_is_not_abstract():
    assert not inspect.isabstract(DatatypeDefinitionSimple)


def test_datatypedefinitionsimple_constructor_exists():
    assert callable(DatatypeDefinitionSimple.__init__)


def test_datatypedefinitionsimple_constructor_args():
    sig = inspect.signature(DatatypeDefinitionSimple.__init__)
    params = list(sig.parameters.keys())



def test_rif12_exchangefile_datatypedefinitioninteger_is_not_abstract():
    assert not inspect.isabstract(rif12_ExchangeFile_DatatypeDefinitionInteger)


def test_rif12_exchangefile_datatypedefinitioninteger_constructor_exists():
    assert callable(rif12_ExchangeFile_DatatypeDefinitionInteger.__init__)


def test_rif12_exchangefile_datatypedefinitioninteger_constructor_args():
    sig = inspect.signature(rif12_ExchangeFile_DatatypeDefinitionInteger.__init__)
    params = list(sig.parameters.keys())
    assert "max" in params, "Missing parameter 'max'"
    assert "min" in params, "Missing parameter 'min'"

def test_rif12_exchangefile_datatypedefinitioninteger_has_max():
    assert hasattr(rif12_ExchangeFile_DatatypeDefinitionInteger, "max")
    descriptor = None
    for klass in rif12_ExchangeFile_DatatypeDefinitionInteger.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_rif12_exchangefile_datatypedefinitioninteger_has_min():
    assert hasattr(rif12_ExchangeFile_DatatypeDefinitionInteger, "min")
    descriptor = None
    for klass in rif12_ExchangeFile_DatatypeDefinitionInteger.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)



def test_rif12_exchangefile_datatypedefinitionstring_is_not_abstract():
    assert not inspect.isabstract(rif12_ExchangeFile_DatatypeDefinitionString)


def test_rif12_exchangefile_datatypedefinitionstring_constructor_exists():
    assert callable(rif12_ExchangeFile_DatatypeDefinitionString.__init__)


def test_rif12_exchangefile_datatypedefinitionstring_constructor_args():
    sig = inspect.signature(rif12_ExchangeFile_DatatypeDefinitionString.__init__)
    params = list(sig.parameters.keys())
    assert "maxLength" in params, "Missing parameter 'maxLength'"

def test_rif12_exchangefile_datatypedefinitionstring_has_maxLength():
    assert hasattr(rif12_ExchangeFile_DatatypeDefinitionString, "maxLength")
    descriptor = None
    for klass in rif12_ExchangeFile_DatatypeDefinitionString.__mro__:
        if "maxLength" in klass.__dict__:
            descriptor = klass.__dict__["maxLength"]
            break
    assert isinstance(descriptor, property)



def test_rif12_exchangefile_datatypedefinitionreal_is_not_abstract():
    assert not inspect.isabstract(rif12_ExchangeFile_DatatypeDefinitionReal)


def test_rif12_exchangefile_datatypedefinitionreal_constructor_exists():
    assert callable(rif12_ExchangeFile_DatatypeDefinitionReal.__init__)


def test_rif12_exchangefile_datatypedefinitionreal_constructor_args():
    sig = inspect.signature(rif12_ExchangeFile_DatatypeDefinitionReal.__init__)
    params = list(sig.parameters.keys())
    assert "max" in params, "Missing parameter 'max'"
    assert "accuracy" in params, "Missing parameter 'accuracy'"
    assert "min" in params, "Missing parameter 'min'"

def test_rif12_exchangefile_datatypedefinitionreal_has_max():
    assert hasattr(rif12_ExchangeFile_DatatypeDefinitionReal, "max")
    descriptor = None
    for klass in rif12_ExchangeFile_DatatypeDefinitionReal.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_rif12_exchangefile_datatypedefinitionreal_has_accuracy():
    assert hasattr(rif12_ExchangeFile_DatatypeDefinitionReal, "accuracy")
    descriptor = None
    for klass in rif12_ExchangeFile_DatatypeDefinitionReal.__mro__:
        if "accuracy" in klass.__dict__:
            descriptor = klass.__dict__["accuracy"]
            break
    assert isinstance(descriptor, property)

def test_rif12_exchangefile_datatypedefinitionreal_has_min():
    assert hasattr(rif12_ExchangeFile_DatatypeDefinitionReal, "min")
    descriptor = None
    for klass in rif12_ExchangeFile_DatatypeDefinitionReal.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)



def test_attributedefinitionenumeration_is_not_abstract():
    assert not inspect.isabstract(AttributeDefinitionEnumeration)


def test_attributedefinitionenumeration_constructor_exists():
    assert callable(AttributeDefinitionEnumeration.__init__)


def test_attributedefinitionenumeration_constructor_args():
    sig = inspect.signature(AttributeDefinitionEnumeration.__init__)
    params = list(sig.parameters.keys())



def test_rif12_exchangefile_datatypedefinitiondate_is_not_abstract():
    assert not inspect.isabstract(rif12_ExchangeFile_DatatypeDefinitionDate)


def test_rif12_exchangefile_datatypedefinitiondate_constructor_exists():
    assert callable(rif12_ExchangeFile_DatatypeDefinitionDate.__init__)


def test_rif12_exchangefile_datatypedefinitiondate_constructor_args():
    sig = inspect.signature(rif12_ExchangeFile_DatatypeDefinitionDate.__init__)
    params = list(sig.parameters.keys())
    assert "format" in params, "Missing parameter 'format'"

def test_rif12_exchangefile_datatypedefinitiondate_has_format():
    assert hasattr(rif12_ExchangeFile_DatatypeDefinitionDate, "format")
    descriptor = None
    for klass in rif12_ExchangeFile_DatatypeDefinitionDate.__mro__:
        if "format" in klass.__dict__:
            descriptor = klass.__dict__["format"]
            break
    assert isinstance(descriptor, property)



def test_rif12_exchangefile_datatypedefinitionboolean_is_not_abstract():
    assert not inspect.isabstract(rif12_ExchangeFile_DatatypeDefinitionBoolean)


def test_rif12_exchangefile_datatypedefinitionboolean_constructor_exists():
    assert callable(rif12_ExchangeFile_DatatypeDefinitionBoolean.__init__)


def test_rif12_exchangefile_datatypedefinitionboolean_constructor_args():
    sig = inspect.signature(rif12_ExchangeFile_DatatypeDefinitionBoolean.__init__)
    params = list(sig.parameters.keys())



def test_datatypes_xmlcontent_is_not_abstract():
    assert not inspect.isabstract(DataTypes_XmlContent)


def test_datatypes_xmlcontent_constructor_exists():
    assert callable(DataTypes_XmlContent.__init__)


def test_datatypes_xmlcontent_constructor_args():
    sig = inspect.signature(DataTypes_XmlContent.__init__)
    params = list(sig.parameters.keys())



def test_datatypes_binarycontent_is_not_abstract():
    assert not inspect.isabstract(DataTypes_BinaryContent)


def test_datatypes_binarycontent_constructor_exists():
    assert callable(DataTypes_BinaryContent.__init__)


def test_datatypes_binarycontent_constructor_args():
    sig = inspect.signature(DataTypes_BinaryContent.__init__)
    params = list(sig.parameters.keys())



def test_datatypes_xhtmlcontent_is_not_abstract():
    assert not inspect.isabstract(DataTypes_XhtmlContent)


def test_datatypes_xhtmlcontent_constructor_exists():
    assert callable(DataTypes_XhtmlContent.__init__)


def test_datatypes_xhtmlcontent_constructor_args():
    sig = inspect.signature(DataTypes_XhtmlContent.__init__)
    params = list(sig.parameters.keys())



def test_attributedefinitioncomplex_is_not_abstract():
    assert not inspect.isabstract(AttributeDefinitionComplex)


def test_attributedefinitioncomplex_constructor_exists():
    assert callable(AttributeDefinitionComplex.__init__)


def test_attributedefinitioncomplex_constructor_args():
    sig = inspect.signature(AttributeDefinitionComplex.__init__)
    params = list(sig.parameters.keys())



def test_attributedefinitionsimple_is_not_abstract():
    assert not inspect.isabstract(AttributeDefinitionSimple)


def test_attributedefinitionsimple_constructor_exists():
    assert callable(AttributeDefinitionSimple.__init__)


def test_attributedefinitionsimple_constructor_args():
    sig = inspect.signature(AttributeDefinitionSimple.__init__)
    params = list(sig.parameters.keys())



def test_spechierarchyroot_is_not_abstract():
    assert not inspect.isabstract(SpecHierarchyRoot)


def test_spechierarchyroot_constructor_exists():
    assert callable(SpecHierarchyRoot.__init__)


def test_spechierarchyroot_constructor_args():
    sig = inspect.signature(SpecHierarchyRoot.__init__)
    params = list(sig.parameters.keys())



def test_datatypedefinition_is_not_abstract():
    assert not inspect.isabstract(DatatypeDefinition)


def test_datatypedefinition_constructor_exists():
    assert callable(DatatypeDefinition.__init__)


def test_datatypedefinition_constructor_args():
    sig = inspect.signature(DatatypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_rif12_exchangefile_datatypedefinitionsimple_is_not_abstract():
    assert not inspect.isabstract(rif12_ExchangeFile_DatatypeDefinitionSimple)


def test_rif12_exchangefile_datatypedefinitionsimple_constructor_exists():
    assert callable(rif12_ExchangeFile_DatatypeDefinitionSimple.__init__)


def test_rif12_exchangefile_datatypedefinitionsimple_constructor_args():
    sig = inspect.signature(rif12_ExchangeFile_DatatypeDefinitionSimple.__init__)
    params = list(sig.parameters.keys())



def test_rif12_exchangefile_embeddedvalue_is_not_abstract():
    assert not inspect.isabstract(rif12_ExchangeFile_EmbeddedValue)


def test_rif12_exchangefile_embeddedvalue_constructor_exists():
    assert callable(rif12_ExchangeFile_EmbeddedValue.__init__)


def test_rif12_exchangefile_embeddedvalue_constructor_args():
    sig = inspect.signature(rif12_ExchangeFile_EmbeddedValue.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "otherContent" in params, "Missing parameter 'otherContent'"

def test_rif12_exchangefile_embeddedvalue_has_key():
    assert hasattr(rif12_ExchangeFile_EmbeddedValue, "key")
    descriptor = None
    for klass in rif12_ExchangeFile_EmbeddedValue.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_rif12_exchangefile_embeddedvalue_has_otherContent():
    assert hasattr(rif12_ExchangeFile_EmbeddedValue, "otherContent")
    descriptor = None
    for klass in rif12_ExchangeFile_EmbeddedValue.__mro__:
        if "otherContent" in klass.__dict__:
            descriptor = klass.__dict__["otherContent"]
            break
    assert isinstance(descriptor, property)



def test_embeddedvalue_is_not_abstract():
    assert not inspect.isabstract(EmbeddedValue)


def test_embeddedvalue_constructor_exists():
    assert callable(EmbeddedValue.__init__)


def test_embeddedvalue_constructor_args():
    sig = inspect.signature(EmbeddedValue.__init__)
    params = list(sig.parameters.keys())



def test_enumvalue_is_not_abstract():
    assert not inspect.isabstract(EnumValue)


def test_enumvalue_constructor_exists():
    assert callable(EnumValue.__init__)


def test_enumvalue_constructor_args():
    sig = inspect.signature(EnumValue.__init__)
    params = list(sig.parameters.keys())



def test_rif12_exchangefile_datatypedefinitionenumeration_is_not_abstract():
    assert not inspect.isabstract(rif12_ExchangeFile_DatatypeDefinitionEnumeration)


def test_rif12_exchangefile_datatypedefinitionenumeration_constructor_exists():
    assert callable(rif12_ExchangeFile_DatatypeDefinitionEnumeration.__init__)


def test_rif12_exchangefile_datatypedefinitionenumeration_constructor_args():
    sig = inspect.signature(rif12_ExchangeFile_DatatypeDefinitionEnumeration.__init__)
    params = list(sig.parameters.keys())



def test_attributevalueenumeration_is_not_abstract():
    assert not inspect.isabstract(AttributeValueEnumeration)


def test_attributevalueenumeration_constructor_exists():
    assert callable(AttributeValueEnumeration.__init__)


def test_attributevalueenumeration_constructor_args():
    sig = inspect.signature(AttributeValueEnumeration.__init__)
    params = list(sig.parameters.keys())



def test_datatypedefinitionenumeration_is_not_abstract():
    assert not inspect.isabstract(DatatypeDefinitionEnumeration)


def test_datatypedefinitionenumeration_constructor_exists():
    assert callable(DatatypeDefinitionEnumeration.__init__)


def test_datatypedefinitionenumeration_constructor_args():
    sig = inspect.signature(DatatypeDefinitionEnumeration.__init__)
    params = list(sig.parameters.keys())



def test_rif12_exchangefile_datatypedefinitioncomplex_is_not_abstract():
    assert not inspect.isabstract(rif12_ExchangeFile_DatatypeDefinitionComplex)


def test_rif12_exchangefile_datatypedefinitioncomplex_constructor_exists():
    assert callable(rif12_ExchangeFile_DatatypeDefinitionComplex.__init__)


def test_rif12_exchangefile_datatypedefinitioncomplex_constructor_args():
    sig = inspect.signature(rif12_ExchangeFile_DatatypeDefinitionComplex.__init__)
    params = list(sig.parameters.keys())
    assert "embedded" in params, "Missing parameter 'embedded'"

def test_rif12_exchangefile_datatypedefinitioncomplex_has_embedded():
    assert hasattr(rif12_ExchangeFile_DatatypeDefinitionComplex, "embedded")
    descriptor = None
    for klass in rif12_ExchangeFile_DatatypeDefinitionComplex.__mro__:
        if "embedded" in klass.__dict__:
            descriptor = klass.__dict__["embedded"]
            break
    assert isinstance(descriptor, property)



def test_attributevaluecomplex_is_not_abstract():
    assert not inspect.isabstract(AttributeValueComplex)


def test_attributevaluecomplex_constructor_exists():
    assert callable(AttributeValueComplex.__init__)


def test_attributevaluecomplex_constructor_args():
    sig = inspect.signature(AttributeValueComplex.__init__)
    params = list(sig.parameters.keys())



def test_rif12_exchangefile_attributevalueembeddedfile_is_not_abstract():
    assert not inspect.isabstract(rif12_ExchangeFile_AttributeValueEmbeddedFile)


def test_rif12_exchangefile_attributevalueembeddedfile_constructor_exists():
    assert callable(rif12_ExchangeFile_AttributeValueEmbeddedFile.__init__)


def test_rif12_exchangefile_attributevalueembeddedfile_constructor_args():
    sig = inspect.signature(rif12_ExchangeFile_AttributeValueEmbeddedFile.__init__)
    params = list(sig.parameters.keys())



def test_rif12_exchangefile_attributevalueembeddeddocument_is_not_abstract():
    assert not inspect.isabstract(rif12_ExchangeFile_AttributeValueEmbeddedDocument)


def test_rif12_exchangefile_attributevalueembeddeddocument_constructor_exists():
    assert callable(rif12_ExchangeFile_AttributeValueEmbeddedDocument.__init__)


def test_rif12_exchangefile_attributevalueembeddeddocument_constructor_args():
    sig = inspect.signature(rif12_ExchangeFile_AttributeValueEmbeddedDocument.__init__)
    params = list(sig.parameters.keys())



def test_rif12_exchangefile_attributevaluefilereference_is_not_abstract():
    assert not inspect.isabstract(rif12_ExchangeFile_AttributeValueFileReference)


def test_rif12_exchangefile_attributevaluefilereference_constructor_exists():
    assert callable(rif12_ExchangeFile_AttributeValueFileReference.__init__)


def test_rif12_exchangefile_attributevaluefilereference_constructor_args():
    sig = inspect.signature(rif12_ExchangeFile_AttributeValueFileReference.__init__)
    params = list(sig.parameters.keys())
    assert "pathToFile" in params, "Missing parameter 'pathToFile'"

def test_rif12_exchangefile_attributevaluefilereference_has_pathToFile():
    assert hasattr(rif12_ExchangeFile_AttributeValueFileReference, "pathToFile")
    descriptor = None
    for klass in rif12_ExchangeFile_AttributeValueFileReference.__mro__:
        if "pathToFile" in klass.__dict__:
            descriptor = klass.__dict__["pathToFile"]
            break
    assert isinstance(descriptor, property)



def test_rif12_exchangefile_attributevaluexmldata_is_not_abstract():
    assert not inspect.isabstract(rif12_ExchangeFile_AttributeValueXmlData)


def test_rif12_exchangefile_attributevaluexmldata_constructor_exists():
    assert callable(rif12_ExchangeFile_AttributeValueXmlData.__init__)


def test_rif12_exchangefile_attributevaluexmldata_constructor_args():
    sig = inspect.signature(rif12_ExchangeFile_AttributeValueXmlData.__init__)
    params = list(sig.parameters.keys())



def test_datatypedefinitioncomplex_is_not_abstract():
    assert not inspect.isabstract(DatatypeDefinitionComplex)


def test_datatypedefinitioncomplex_constructor_exists():
    assert callable(DatatypeDefinitionComplex.__init__)


def test_datatypedefinitioncomplex_constructor_args():
    sig = inspect.signature(DatatypeDefinitionComplex.__init__)
    params = list(sig.parameters.keys())



def test_rif12_exchangefile_datatypedefinitiondocument_is_not_abstract():
    assert not inspect.isabstract(rif12_ExchangeFile_DatatypeDefinitionDocument)


def test_rif12_exchangefile_datatypedefinitiondocument_constructor_exists():
    assert callable(rif12_ExchangeFile_DatatypeDefinitionDocument.__init__)


def test_rif12_exchangefile_datatypedefinitiondocument_constructor_args():
    sig = inspect.signature(rif12_ExchangeFile_DatatypeDefinitionDocument.__init__)
    params = list(sig.parameters.keys())



def test_rif12_exchangefile_datatypedefinitionbinaryfile_is_not_abstract():
    assert not inspect.isabstract(rif12_ExchangeFile_DatatypeDefinitionBinaryFile)


def test_rif12_exchangefile_datatypedefinitionbinaryfile_constructor_exists():
    assert callable(rif12_ExchangeFile_DatatypeDefinitionBinaryFile.__init__)


def test_rif12_exchangefile_datatypedefinitionbinaryfile_constructor_args():
    sig = inspect.signature(rif12_ExchangeFile_DatatypeDefinitionBinaryFile.__init__)
    params = list(sig.parameters.keys())
    assert "formatName" in params, "Missing parameter 'formatName'"
    assert "filenameSuffix" in params, "Missing parameter 'filenameSuffix'"
    assert "application" in params, "Missing parameter 'application'"
    assert "mimeType" in params, "Missing parameter 'mimeType'"

def test_rif12_exchangefile_datatypedefinitionbinaryfile_has_formatName():
    assert hasattr(rif12_ExchangeFile_DatatypeDefinitionBinaryFile, "formatName")
    descriptor = None
    for klass in rif12_ExchangeFile_DatatypeDefinitionBinaryFile.__mro__:
        if "formatName" in klass.__dict__:
            descriptor = klass.__dict__["formatName"]
            break
    assert isinstance(descriptor, property)

def test_rif12_exchangefile_datatypedefinitionbinaryfile_has_filenameSuffix():
    assert hasattr(rif12_ExchangeFile_DatatypeDefinitionBinaryFile, "filenameSuffix")
    descriptor = None
    for klass in rif12_ExchangeFile_DatatypeDefinitionBinaryFile.__mro__:
        if "filenameSuffix" in klass.__dict__:
            descriptor = klass.__dict__["filenameSuffix"]
            break
    assert isinstance(descriptor, property)

def test_rif12_exchangefile_datatypedefinitionbinaryfile_has_application():
    assert hasattr(rif12_ExchangeFile_DatatypeDefinitionBinaryFile, "application")
    descriptor = None
    for klass in rif12_ExchangeFile_DatatypeDefinitionBinaryFile.__mro__:
        if "application" in klass.__dict__:
            descriptor = klass.__dict__["application"]
            break
    assert isinstance(descriptor, property)

def test_rif12_exchangefile_datatypedefinitionbinaryfile_has_mimeType():
    assert hasattr(rif12_ExchangeFile_DatatypeDefinitionBinaryFile, "mimeType")
    descriptor = None
    for klass in rif12_ExchangeFile_DatatypeDefinitionBinaryFile.__mro__:
        if "mimeType" in klass.__dict__:
            descriptor = klass.__dict__["mimeType"]
            break
    assert isinstance(descriptor, property)



def test_rif12_exchangefile_datatypedefinitionxmldata_is_not_abstract():
    assert not inspect.isabstract(rif12_ExchangeFile_DatatypeDefinitionXmlData)


def test_rif12_exchangefile_datatypedefinitionxmldata_constructor_exists():
    assert callable(rif12_ExchangeFile_DatatypeDefinitionXmlData.__init__)


def test_rif12_exchangefile_datatypedefinitionxmldata_constructor_args():
    sig = inspect.signature(rif12_ExchangeFile_DatatypeDefinitionXmlData.__init__)
    params = list(sig.parameters.keys())
    assert "schemaLocation" in params, "Missing parameter 'schemaLocation'"
    assert "nameSpaceURI" in params, "Missing parameter 'nameSpaceURI'"

def test_rif12_exchangefile_datatypedefinitionxmldata_has_schemaLocation():
    assert hasattr(rif12_ExchangeFile_DatatypeDefinitionXmlData, "schemaLocation")
    descriptor = None
    for klass in rif12_ExchangeFile_DatatypeDefinitionXmlData.__mro__:
        if "schemaLocation" in klass.__dict__:
            descriptor = klass.__dict__["schemaLocation"]
            break
    assert isinstance(descriptor, property)

def test_rif12_exchangefile_datatypedefinitionxmldata_has_nameSpaceURI():
    assert hasattr(rif12_ExchangeFile_DatatypeDefinitionXmlData, "nameSpaceURI")
    descriptor = None
    for klass in rif12_ExchangeFile_DatatypeDefinitionXmlData.__mro__:
        if "nameSpaceURI" in klass.__dict__:
            descriptor = klass.__dict__["nameSpaceURI"]
            break
    assert isinstance(descriptor, property)



def test_specgrouphierarchy_is_not_abstract():
    assert not inspect.isabstract(SpecGroupHierarchy)


def test_specgrouphierarchy_constructor_exists():
    assert callable(SpecGroupHierarchy.__init__)


def test_specgrouphierarchy_constructor_args():
    sig = inspect.signature(SpecGroupHierarchy.__init__)
    params = list(sig.parameters.keys())



def test_specobject_is_not_abstract():
    assert not inspect.isabstract(SpecObject)


def test_specobject_constructor_exists():
    assert callable(SpecObject.__init__)


def test_specobject_constructor_args():
    sig = inspect.signature(SpecObject.__init__)
    params = list(sig.parameters.keys())



def test_attributedefinition_is_not_abstract():
    assert not inspect.isabstract(AttributeDefinition)


def test_attributedefinition_constructor_exists():
    assert callable(AttributeDefinition.__init__)


def test_attributedefinition_constructor_args():
    sig = inspect.signature(AttributeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_rif12_exchangefile_attributedefinitionenumeration_is_not_abstract():
    assert not inspect.isabstract(rif12_ExchangeFile_AttributeDefinitionEnumeration)


def test_rif12_exchangefile_attributedefinitionenumeration_constructor_exists():
    assert callable(rif12_ExchangeFile_AttributeDefinitionEnumeration.__init__)


def test_rif12_exchangefile_attributedefinitionenumeration_constructor_args():
    sig = inspect.signature(rif12_ExchangeFile_AttributeDefinitionEnumeration.__init__)
    params = list(sig.parameters.keys())
    assert "multiValued" in params, "Missing parameter 'multiValued'"

def test_rif12_exchangefile_attributedefinitionenumeration_has_multiValued():
    assert hasattr(rif12_ExchangeFile_AttributeDefinitionEnumeration, "multiValued")
    descriptor = None
    for klass in rif12_ExchangeFile_AttributeDefinitionEnumeration.__mro__:
        if "multiValued" in klass.__dict__:
            descriptor = klass.__dict__["multiValued"]
            break
    assert isinstance(descriptor, property)



def test_rif12_exchangefile_attributedefinitioncomplex_is_not_abstract():
    assert not inspect.isabstract(rif12_ExchangeFile_AttributeDefinitionComplex)


def test_rif12_exchangefile_attributedefinitioncomplex_constructor_exists():
    assert callable(rif12_ExchangeFile_AttributeDefinitionComplex.__init__)


def test_rif12_exchangefile_attributedefinitioncomplex_constructor_args():
    sig = inspect.signature(rif12_ExchangeFile_AttributeDefinitionComplex.__init__)
    params = list(sig.parameters.keys())



def test_rif12_exchangefile_attributedefinitionsimple_is_not_abstract():
    assert not inspect.isabstract(rif12_ExchangeFile_AttributeDefinitionSimple)


def test_rif12_exchangefile_attributedefinitionsimple_constructor_exists():
    assert callable(rif12_ExchangeFile_AttributeDefinitionSimple.__init__)


def test_rif12_exchangefile_attributedefinitionsimple_constructor_args():
    sig = inspect.signature(rif12_ExchangeFile_AttributeDefinitionSimple.__init__)
    params = list(sig.parameters.keys())



def test_specgroup_is_not_abstract():
    assert not inspect.isabstract(SpecGroup)


def test_specgroup_constructor_exists():
    assert callable(SpecGroup.__init__)


def test_specgroup_constructor_args():
    sig = inspect.signature(SpecGroup.__init__)
    params = list(sig.parameters.keys())



def test_specgrouphierarchyroot_is_not_abstract():
    assert not inspect.isabstract(SpecGroupHierarchyRoot)


def test_specgrouphierarchyroot_constructor_exists():
    assert callable(SpecGroupHierarchyRoot.__init__)


def test_specgrouphierarchyroot_constructor_args():
    sig = inspect.signature(SpecGroupHierarchyRoot.__init__)
    params = list(sig.parameters.keys())



def test_specrelation_is_not_abstract():
    assert not inspect.isabstract(SpecRelation)


def test_specrelation_constructor_exists():
    assert callable(SpecRelation.__init__)


def test_specrelation_constructor_args():
    sig = inspect.signature(SpecRelation.__init__)
    params = list(sig.parameters.keys())



def test_relationgroup_is_not_abstract():
    assert not inspect.isabstract(RelationGroup)


def test_relationgroup_constructor_exists():
    assert callable(RelationGroup.__init__)


def test_relationgroup_constructor_args():
    sig = inspect.signature(RelationGroup.__init__)
    params = list(sig.parameters.keys())



def test_rif12_exchangefile_identifiable_is_not_abstract():
    assert not inspect.isabstract(rif12_ExchangeFile_Identifiable)


def test_rif12_exchangefile_identifiable_constructor_exists():
    assert callable(rif12_ExchangeFile_Identifiable.__init__)


def test_rif12_exchangefile_identifiable_constructor_args():
    sig = inspect.signature(rif12_ExchangeFile_Identifiable.__init__)
    params = list(sig.parameters.keys())
    assert "lastChange" in params, "Missing parameter 'lastChange'"
    assert "longName" in params, "Missing parameter 'longName'"
    assert "desc" in params, "Missing parameter 'desc'"
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_rif12_exchangefile_identifiable_has_lastChange():
    assert hasattr(rif12_ExchangeFile_Identifiable, "lastChange")
    descriptor = None
    for klass in rif12_ExchangeFile_Identifiable.__mro__:
        if "lastChange" in klass.__dict__:
            descriptor = klass.__dict__["lastChange"]
            break
    assert isinstance(descriptor, property)

def test_rif12_exchangefile_identifiable_has_longName():
    assert hasattr(rif12_ExchangeFile_Identifiable, "longName")
    descriptor = None
    for klass in rif12_ExchangeFile_Identifiable.__mro__:
        if "longName" in klass.__dict__:
            descriptor = klass.__dict__["longName"]
            break
    assert isinstance(descriptor, property)

def test_rif12_exchangefile_identifiable_has_desc():
    assert hasattr(rif12_ExchangeFile_Identifiable, "desc")
    descriptor = None
    for klass in rif12_ExchangeFile_Identifiable.__mro__:
        if "desc" in klass.__dict__:
            descriptor = klass.__dict__["desc"]
            break
    assert isinstance(descriptor, property)

def test_rif12_exchangefile_identifiable_has_identifier():
    assert hasattr(rif12_ExchangeFile_Identifiable, "identifier")
    descriptor = None
    for klass in rif12_ExchangeFile_Identifiable.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_attributevalue_is_not_abstract():
    assert not inspect.isabstract(AttributeValue)


def test_attributevalue_constructor_exists():
    assert callable(AttributeValue.__init__)


def test_attributevalue_constructor_args():
    sig = inspect.signature(AttributeValue.__init__)
    params = list(sig.parameters.keys())



def test_rif12_exchangefile_attributevalueenumeration_is_not_abstract():
    assert not inspect.isabstract(rif12_ExchangeFile_AttributeValueEnumeration)


def test_rif12_exchangefile_attributevalueenumeration_constructor_exists():
    assert callable(rif12_ExchangeFile_AttributeValueEnumeration.__init__)


def test_rif12_exchangefile_attributevalueenumeration_constructor_args():
    sig = inspect.signature(rif12_ExchangeFile_AttributeValueEnumeration.__init__)
    params = list(sig.parameters.keys())



def test_rif12_exchangefile_attributevaluesimple_is_not_abstract():
    assert not inspect.isabstract(rif12_ExchangeFile_AttributeValueSimple)


def test_rif12_exchangefile_attributevaluesimple_constructor_exists():
    assert callable(rif12_ExchangeFile_AttributeValueSimple.__init__)


def test_rif12_exchangefile_attributevaluesimple_constructor_args():
    sig = inspect.signature(rif12_ExchangeFile_AttributeValueSimple.__init__)
    params = list(sig.parameters.keys())
    assert "theValue" in params, "Missing parameter 'theValue'"

def test_rif12_exchangefile_attributevaluesimple_has_theValue():
    assert hasattr(rif12_ExchangeFile_AttributeValueSimple, "theValue")
    descriptor = None
    for klass in rif12_ExchangeFile_AttributeValueSimple.__mro__:
        if "theValue" in klass.__dict__:
            descriptor = klass.__dict__["theValue"]
            break
    assert isinstance(descriptor, property)



def test_rif12_exchangefile_attributevaluecomplex_is_not_abstract():
    assert not inspect.isabstract(rif12_ExchangeFile_AttributeValueComplex)


def test_rif12_exchangefile_attributevaluecomplex_constructor_exists():
    assert callable(rif12_ExchangeFile_AttributeValueComplex.__init__)


def test_rif12_exchangefile_attributevaluecomplex_constructor_args():
    sig = inspect.signature(rif12_ExchangeFile_AttributeValueComplex.__init__)
    params = list(sig.parameters.keys())



def test_spectype_is_not_abstract():
    assert not inspect.isabstract(SpecType)


def test_spectype_constructor_exists():
    assert callable(SpecType.__init__)


def test_spectype_constructor_args():
    sig = inspect.signature(SpecType.__init__)
    params = list(sig.parameters.keys())



def test_identifiable_is_not_abstract():
    assert not inspect.isabstract(Identifiable)


def test_identifiable_constructor_exists():
    assert callable(Identifiable.__init__)


def test_identifiable_constructor_args():
    sig = inspect.signature(Identifiable.__init__)
    params = list(sig.parameters.keys())



def test_rif12_exchangefile_attributedefinition_is_not_abstract():
    assert not inspect.isabstract(rif12_ExchangeFile_AttributeDefinition)


def test_rif12_exchangefile_attributedefinition_constructor_exists():
    assert callable(rif12_ExchangeFile_AttributeDefinition.__init__)


def test_rif12_exchangefile_attributedefinition_constructor_args():
    sig = inspect.signature(rif12_ExchangeFile_AttributeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_rif12_exchangefile_specgrouphierarchy_is_not_abstract():
    assert not inspect.isabstract(rif12_ExchangeFile_SpecGroupHierarchy)


def test_rif12_exchangefile_specgrouphierarchy_constructor_exists():
    assert callable(rif12_ExchangeFile_SpecGroupHierarchy.__init__)


def test_rif12_exchangefile_specgrouphierarchy_constructor_args():
    sig = inspect.signature(rif12_ExchangeFile_SpecGroupHierarchy.__init__)
    params = list(sig.parameters.keys())



def test_rif12_exchangefile_datatypedefinition_is_not_abstract():
    assert not inspect.isabstract(rif12_ExchangeFile_DatatypeDefinition)


def test_rif12_exchangefile_datatypedefinition_constructor_exists():
    assert callable(rif12_ExchangeFile_DatatypeDefinition.__init__)


def test_rif12_exchangefile_datatypedefinition_constructor_args():
    sig = inspect.signature(rif12_ExchangeFile_DatatypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_rif12_exchangefile_spectype_is_not_abstract():
    assert not inspect.isabstract(rif12_ExchangeFile_SpecType)


def test_rif12_exchangefile_spectype_constructor_exists():
    assert callable(rif12_ExchangeFile_SpecType.__init__)


def test_rif12_exchangefile_spectype_constructor_args():
    sig = inspect.signature(rif12_ExchangeFile_SpecType.__init__)
    params = list(sig.parameters.keys())



def test_rif12_exchangefile_relationgroup_is_not_abstract():
    assert not inspect.isabstract(rif12_ExchangeFile_RelationGroup)


def test_rif12_exchangefile_relationgroup_constructor_exists():
    assert callable(rif12_ExchangeFile_RelationGroup.__init__)


def test_rif12_exchangefile_relationgroup_constructor_args():
    sig = inspect.signature(rif12_ExchangeFile_RelationGroup.__init__)
    params = list(sig.parameters.keys())



def test_rif12_exchangefile_attributevalue_is_not_abstract():
    assert not inspect.isabstract(rif12_ExchangeFile_AttributeValue)


def test_rif12_exchangefile_attributevalue_constructor_exists():
    assert callable(rif12_ExchangeFile_AttributeValue.__init__)


def test_rif12_exchangefile_attributevalue_constructor_args():
    sig = inspect.signature(rif12_ExchangeFile_AttributeValue.__init__)
    params = list(sig.parameters.keys())



def test_rif12_exchangefile_spechierarchy_is_not_abstract():
    assert not inspect.isabstract(rif12_ExchangeFile_SpecHierarchy)


def test_rif12_exchangefile_spechierarchy_constructor_exists():
    assert callable(rif12_ExchangeFile_SpecHierarchy.__init__)


def test_rif12_exchangefile_spechierarchy_constructor_args():
    sig = inspect.signature(rif12_ExchangeFile_SpecHierarchy.__init__)
    params = list(sig.parameters.keys())



def test_rif12_exchangefile_accesspolicy_is_not_abstract():
    assert not inspect.isabstract(rif12_ExchangeFile_AccessPolicy)


def test_rif12_exchangefile_accesspolicy_constructor_exists():
    assert callable(rif12_ExchangeFile_AccessPolicy.__init__)


def test_rif12_exchangefile_accesspolicy_constructor_args():
    sig = inspect.signature(rif12_ExchangeFile_AccessPolicy.__init__)
    params = list(sig.parameters.keys())
    assert "accessMode" in params, "Missing parameter 'accessMode'"

def test_rif12_exchangefile_accesspolicy_has_accessMode():
    assert hasattr(rif12_ExchangeFile_AccessPolicy, "accessMode")
    descriptor = None
    for klass in rif12_ExchangeFile_AccessPolicy.__mro__:
        if "accessMode" in klass.__dict__:
            descriptor = klass.__dict__["accessMode"]
            break
    assert isinstance(descriptor, property)



def test_rif12_exchangefile_enumvalue_is_not_abstract():
    assert not inspect.isabstract(rif12_ExchangeFile_EnumValue)


def test_rif12_exchangefile_enumvalue_constructor_exists():
    assert callable(rif12_ExchangeFile_EnumValue.__init__)


def test_rif12_exchangefile_enumvalue_constructor_args():
    sig = inspect.signature(rif12_ExchangeFile_EnumValue.__init__)
    params = list(sig.parameters.keys())



def test_rif12_exchangefile_specelementwithuserdefinedattributes_is_not_abstract():
    assert not inspect.isabstract(rif12_ExchangeFile_SpecElementWithUserDefinedAttributes)


def test_rif12_exchangefile_specelementwithuserdefinedattributes_constructor_exists():
    assert callable(rif12_ExchangeFile_SpecElementWithUserDefinedAttributes.__init__)


def test_rif12_exchangefile_specelementwithuserdefinedattributes_constructor_args():
    sig = inspect.signature(rif12_ExchangeFile_SpecElementWithUserDefinedAttributes.__init__)
    params = list(sig.parameters.keys())



def test_spechierarchy_is_not_abstract():
    assert not inspect.isabstract(SpecHierarchy)


def test_spechierarchy_constructor_exists():
    assert callable(SpecHierarchy.__init__)


def test_spechierarchy_constructor_args():
    sig = inspect.signature(SpecHierarchy.__init__)
    params = list(sig.parameters.keys())



def test_specelementwithuserdefinedattributes_is_not_abstract():
    assert not inspect.isabstract(SpecElementWithUserDefinedAttributes)


def test_specelementwithuserdefinedattributes_constructor_exists():
    assert callable(SpecElementWithUserDefinedAttributes.__init__)


def test_specelementwithuserdefinedattributes_constructor_args():
    sig = inspect.signature(SpecElementWithUserDefinedAttributes.__init__)
    params = list(sig.parameters.keys())



def test_rif12_exchangefile_specgroup_is_not_abstract():
    assert not inspect.isabstract(rif12_ExchangeFile_SpecGroup)


def test_rif12_exchangefile_specgroup_constructor_exists():
    assert callable(rif12_ExchangeFile_SpecGroup.__init__)


def test_rif12_exchangefile_specgroup_constructor_args():
    sig = inspect.signature(rif12_ExchangeFile_SpecGroup.__init__)
    params = list(sig.parameters.keys())



def test_rif12_exchangefile_specgrouphierarchyroot_is_not_abstract():
    assert not inspect.isabstract(rif12_ExchangeFile_SpecGroupHierarchyRoot)


def test_rif12_exchangefile_specgrouphierarchyroot_constructor_exists():
    assert callable(rif12_ExchangeFile_SpecGroupHierarchyRoot.__init__)


def test_rif12_exchangefile_specgrouphierarchyroot_constructor_args():
    sig = inspect.signature(rif12_ExchangeFile_SpecGroupHierarchyRoot.__init__)
    params = list(sig.parameters.keys())



def test_rif12_exchangefile_specrelation_is_not_abstract():
    assert not inspect.isabstract(rif12_ExchangeFile_SpecRelation)


def test_rif12_exchangefile_specrelation_constructor_exists():
    assert callable(rif12_ExchangeFile_SpecRelation.__init__)


def test_rif12_exchangefile_specrelation_constructor_args():
    sig = inspect.signature(rif12_ExchangeFile_SpecRelation.__init__)
    params = list(sig.parameters.keys())



def test_rif12_exchangefile_specobject_is_not_abstract():
    assert not inspect.isabstract(rif12_ExchangeFile_SpecObject)


def test_rif12_exchangefile_specobject_constructor_exists():
    assert callable(rif12_ExchangeFile_SpecObject.__init__)


def test_rif12_exchangefile_specobject_constructor_args():
    sig = inspect.signature(rif12_ExchangeFile_SpecObject.__init__)
    params = list(sig.parameters.keys())



def test_rif12_exchangefile_spechierarchyroot_is_not_abstract():
    assert not inspect.isabstract(rif12_ExchangeFile_SpecHierarchyRoot)


def test_rif12_exchangefile_spechierarchyroot_constructor_exists():
    assert callable(rif12_ExchangeFile_SpecHierarchyRoot.__init__)


def test_rif12_exchangefile_spechierarchyroot_constructor_args():
    sig = inspect.signature(rif12_ExchangeFile_SpecHierarchyRoot.__init__)
    params = list(sig.parameters.keys())

def test_datatypedefinitiondateformatenum_exists():
    # Check that the Enumeration exists
    assert DatatypeDefinitionDateFormatEnum is not None

def test_datatypedefinitiondateformatenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DatatypeDefinitionDateFormatEnum]
    expected_literals = [
        "W3C",
        "CUSTOM",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DatatypeDefinitionDateFormatEnum"

def test_accesspolicyaccessmodeenum_exists():
    # Check that the Enumeration exists
    assert AccessPolicyAccessModeEnum is not None

def test_accesspolicyaccessmodeenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AccessPolicyAccessModeEnum]
    expected_literals = [
        "CREATE",
        "EDIT",
        "DELETE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AccessPolicyAccessModeEnum"


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
rif12_DataTypes_XmlContent_strategy = st.builds(
    rif12_DataTypes_XmlContent,
)
rif12_DataTypes_XhtmlContent_strategy = st.builds(
    rif12_DataTypes_XhtmlContent,
)
rif12_DataTypes_BinaryContent_strategy = st.builds(
    rif12_DataTypes_BinaryContent,
)
rif12_ExchangeFile_RIFToolExtension_strategy = st.builds(
    rif12_ExchangeFile_RIFToolExtension,
)
AccessPolicy_strategy = st.builds(
    AccessPolicy,
)
rif12_ExchangeFile_RIFContent_strategy = st.builds(
    rif12_ExchangeFile_RIFContent,
)
rif12_ExchangeFile_RIFHeader_strategy = st.builds(
    rif12_ExchangeFile_RIFHeader,
    comment=
        safe_text,
    creationTime=
        safe_text,
    title=
        safe_text,
    sourceToolId=
        safe_text,
    author=
        safe_text,
    identifier=
        safe_text
)
RIFToolExtension_strategy = st.builds(
    RIFToolExtension,
)
RIFContent_strategy = st.builds(
    RIFContent,
)
RIFHeader_strategy = st.builds(
    RIFHeader,
)
rif12_ExchangeFile_RIF_strategy = st.builds(
    rif12_ExchangeFile_RIF,
)
AttributeValueSimple_strategy = st.builds(
    AttributeValueSimple,
)
DatatypeDefinitionSimple_strategy = st.builds(
    DatatypeDefinitionSimple,
)
rif12_ExchangeFile_DatatypeDefinitionInteger_strategy = st.builds(
    rif12_ExchangeFile_DatatypeDefinitionInteger,
    max=
        safe_text,
    min=
        safe_text
)
rif12_ExchangeFile_DatatypeDefinitionString_strategy = st.builds(
    rif12_ExchangeFile_DatatypeDefinitionString,
    maxLength=
        safe_text
)
rif12_ExchangeFile_DatatypeDefinitionReal_strategy = st.builds(
    rif12_ExchangeFile_DatatypeDefinitionReal,
    max=
        safe_text,
    accuracy=
        safe_text,
    min=
        safe_text
)
AttributeDefinitionEnumeration_strategy = st.builds(
    AttributeDefinitionEnumeration,
)
rif12_ExchangeFile_DatatypeDefinitionDate_strategy = st.builds(
    rif12_ExchangeFile_DatatypeDefinitionDate,
    format=
        safe_text
)
rif12_ExchangeFile_DatatypeDefinitionBoolean_strategy = st.builds(
    rif12_ExchangeFile_DatatypeDefinitionBoolean,
)
DataTypes_XmlContent_strategy = st.builds(
    DataTypes_XmlContent,
)
DataTypes_BinaryContent_strategy = st.builds(
    DataTypes_BinaryContent,
)
DataTypes_XhtmlContent_strategy = st.builds(
    DataTypes_XhtmlContent,
)
AttributeDefinitionComplex_strategy = st.builds(
    AttributeDefinitionComplex,
)
AttributeDefinitionSimple_strategy = st.builds(
    AttributeDefinitionSimple,
)
SpecHierarchyRoot_strategy = st.builds(
    SpecHierarchyRoot,
)
DatatypeDefinition_strategy = st.builds(
    DatatypeDefinition,
)
rif12_ExchangeFile_DatatypeDefinitionSimple_strategy = st.builds(
    rif12_ExchangeFile_DatatypeDefinitionSimple,
)
rif12_ExchangeFile_EmbeddedValue_strategy = st.builds(
    rif12_ExchangeFile_EmbeddedValue,
    key=
        safe_text,
    otherContent=
        safe_text
)
EmbeddedValue_strategy = st.builds(
    EmbeddedValue,
)
EnumValue_strategy = st.builds(
    EnumValue,
)
rif12_ExchangeFile_DatatypeDefinitionEnumeration_strategy = st.builds(
    rif12_ExchangeFile_DatatypeDefinitionEnumeration,
)
AttributeValueEnumeration_strategy = st.builds(
    AttributeValueEnumeration,
)
DatatypeDefinitionEnumeration_strategy = st.builds(
    DatatypeDefinitionEnumeration,
)
rif12_ExchangeFile_DatatypeDefinitionComplex_strategy = st.builds(
    rif12_ExchangeFile_DatatypeDefinitionComplex,
    embedded=
        safe_text
)
AttributeValueComplex_strategy = st.builds(
    AttributeValueComplex,
)
rif12_ExchangeFile_AttributeValueEmbeddedFile_strategy = st.builds(
    rif12_ExchangeFile_AttributeValueEmbeddedFile,
)
rif12_ExchangeFile_AttributeValueEmbeddedDocument_strategy = st.builds(
    rif12_ExchangeFile_AttributeValueEmbeddedDocument,
)
rif12_ExchangeFile_AttributeValueFileReference_strategy = st.builds(
    rif12_ExchangeFile_AttributeValueFileReference,
    pathToFile=
        safe_text
)
rif12_ExchangeFile_AttributeValueXmlData_strategy = st.builds(
    rif12_ExchangeFile_AttributeValueXmlData,
)
DatatypeDefinitionComplex_strategy = st.builds(
    DatatypeDefinitionComplex,
)
rif12_ExchangeFile_DatatypeDefinitionDocument_strategy = st.builds(
    rif12_ExchangeFile_DatatypeDefinitionDocument,
)
rif12_ExchangeFile_DatatypeDefinitionBinaryFile_strategy = st.builds(
    rif12_ExchangeFile_DatatypeDefinitionBinaryFile,
    formatName=
        safe_text,
    filenameSuffix=
        safe_text,
    application=
        safe_text,
    mimeType=
        safe_text
)
rif12_ExchangeFile_DatatypeDefinitionXmlData_strategy = st.builds(
    rif12_ExchangeFile_DatatypeDefinitionXmlData,
    schemaLocation=
        safe_text,
    nameSpaceURI=
        safe_text
)
SpecGroupHierarchy_strategy = st.builds(
    SpecGroupHierarchy,
)
SpecObject_strategy = st.builds(
    SpecObject,
)
AttributeDefinition_strategy = st.builds(
    AttributeDefinition,
)
rif12_ExchangeFile_AttributeDefinitionEnumeration_strategy = st.builds(
    rif12_ExchangeFile_AttributeDefinitionEnumeration,
    multiValued=
        safe_text
)
rif12_ExchangeFile_AttributeDefinitionComplex_strategy = st.builds(
    rif12_ExchangeFile_AttributeDefinitionComplex,
)
rif12_ExchangeFile_AttributeDefinitionSimple_strategy = st.builds(
    rif12_ExchangeFile_AttributeDefinitionSimple,
)
SpecGroup_strategy = st.builds(
    SpecGroup,
)
SpecGroupHierarchyRoot_strategy = st.builds(
    SpecGroupHierarchyRoot,
)
SpecRelation_strategy = st.builds(
    SpecRelation,
)
RelationGroup_strategy = st.builds(
    RelationGroup,
)
rif12_ExchangeFile_Identifiable_strategy = st.builds(
    rif12_ExchangeFile_Identifiable,
    lastChange=
        safe_text,
    longName=
        safe_text,
    desc=
        safe_text,
    identifier=
        safe_text
)
AttributeValue_strategy = st.builds(
    AttributeValue,
)
rif12_ExchangeFile_AttributeValueEnumeration_strategy = st.builds(
    rif12_ExchangeFile_AttributeValueEnumeration,
)
rif12_ExchangeFile_AttributeValueSimple_strategy = st.builds(
    rif12_ExchangeFile_AttributeValueSimple,
    theValue=
        safe_text
)
rif12_ExchangeFile_AttributeValueComplex_strategy = st.builds(
    rif12_ExchangeFile_AttributeValueComplex,
)
SpecType_strategy = st.builds(
    SpecType,
)
Identifiable_strategy = st.builds(
    Identifiable,
)
rif12_ExchangeFile_AttributeDefinition_strategy = st.builds(
    rif12_ExchangeFile_AttributeDefinition,
)
rif12_ExchangeFile_SpecGroupHierarchy_strategy = st.builds(
    rif12_ExchangeFile_SpecGroupHierarchy,
)
rif12_ExchangeFile_DatatypeDefinition_strategy = st.builds(
    rif12_ExchangeFile_DatatypeDefinition,
)
rif12_ExchangeFile_SpecType_strategy = st.builds(
    rif12_ExchangeFile_SpecType,
)
rif12_ExchangeFile_RelationGroup_strategy = st.builds(
    rif12_ExchangeFile_RelationGroup,
)
rif12_ExchangeFile_AttributeValue_strategy = st.builds(
    rif12_ExchangeFile_AttributeValue,
)
rif12_ExchangeFile_SpecHierarchy_strategy = st.builds(
    rif12_ExchangeFile_SpecHierarchy,
)
rif12_ExchangeFile_AccessPolicy_strategy = st.builds(
    rif12_ExchangeFile_AccessPolicy,
    accessMode=
        safe_text
)
rif12_ExchangeFile_EnumValue_strategy = st.builds(
    rif12_ExchangeFile_EnumValue,
)
rif12_ExchangeFile_SpecElementWithUserDefinedAttributes_strategy = st.builds(
    rif12_ExchangeFile_SpecElementWithUserDefinedAttributes,
)
SpecHierarchy_strategy = st.builds(
    SpecHierarchy,
)
SpecElementWithUserDefinedAttributes_strategy = st.builds(
    SpecElementWithUserDefinedAttributes,
)
rif12_ExchangeFile_SpecGroup_strategy = st.builds(
    rif12_ExchangeFile_SpecGroup,
)
rif12_ExchangeFile_SpecGroupHierarchyRoot_strategy = st.builds(
    rif12_ExchangeFile_SpecGroupHierarchyRoot,
)
rif12_ExchangeFile_SpecRelation_strategy = st.builds(
    rif12_ExchangeFile_SpecRelation,
)
rif12_ExchangeFile_SpecObject_strategy = st.builds(
    rif12_ExchangeFile_SpecObject,
)
rif12_ExchangeFile_SpecHierarchyRoot_strategy = st.builds(
    rif12_ExchangeFile_SpecHierarchyRoot,
)

@given(instance=rif12_DataTypes_XmlContent_strategy)
@settings(max_examples=50)
def test_rif12_datatypes_xmlcontent_instantiation(instance):
    assert isinstance(instance, rif12_DataTypes_XmlContent)

@given(instance=rif12_DataTypes_XhtmlContent_strategy)
@settings(max_examples=50)
def test_rif12_datatypes_xhtmlcontent_instantiation(instance):
    assert isinstance(instance, rif12_DataTypes_XhtmlContent)

@given(instance=rif12_DataTypes_BinaryContent_strategy)
@settings(max_examples=50)
def test_rif12_datatypes_binarycontent_instantiation(instance):
    assert isinstance(instance, rif12_DataTypes_BinaryContent)

@given(instance=rif12_ExchangeFile_RIFToolExtension_strategy)
@settings(max_examples=50)
def test_rif12_exchangefile_riftoolextension_instantiation(instance):
    assert isinstance(instance, rif12_ExchangeFile_RIFToolExtension)

@given(instance=AccessPolicy_strategy)
@settings(max_examples=50)
def test_accesspolicy_instantiation(instance):
    assert isinstance(instance, AccessPolicy)

@given(instance=rif12_ExchangeFile_RIFContent_strategy)
@settings(max_examples=50)
def test_rif12_exchangefile_rifcontent_instantiation(instance):
    assert isinstance(instance, rif12_ExchangeFile_RIFContent)

@given(instance=rif12_ExchangeFile_RIFHeader_strategy)
@settings(max_examples=50)
def test_rif12_exchangefile_rifheader_instantiation(instance):
    assert isinstance(instance, rif12_ExchangeFile_RIFHeader)



@given(instance=rif12_ExchangeFile_RIFHeader_strategy)
def test_rif12_exchangefile_rifheader_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=rif12_ExchangeFile_RIFHeader_strategy)
def test_rif12_exchangefile_rifheader_creationTime_setter(instance):
    original = instance.creationTime
    instance.creationTime = original
    assert instance.creationTime == original



@given(instance=rif12_ExchangeFile_RIFHeader_strategy)
def test_rif12_exchangefile_rifheader_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=rif12_ExchangeFile_RIFHeader_strategy)
def test_rif12_exchangefile_rifheader_sourceToolId_setter(instance):
    original = instance.sourceToolId
    instance.sourceToolId = original
    assert instance.sourceToolId == original



@given(instance=rif12_ExchangeFile_RIFHeader_strategy)
def test_rif12_exchangefile_rifheader_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=rif12_ExchangeFile_RIFHeader_strategy)
def test_rif12_exchangefile_rifheader_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=RIFToolExtension_strategy)
@settings(max_examples=50)
def test_riftoolextension_instantiation(instance):
    assert isinstance(instance, RIFToolExtension)

@given(instance=RIFContent_strategy)
@settings(max_examples=50)
def test_rifcontent_instantiation(instance):
    assert isinstance(instance, RIFContent)

@given(instance=RIFHeader_strategy)
@settings(max_examples=50)
def test_rifheader_instantiation(instance):
    assert isinstance(instance, RIFHeader)

@given(instance=rif12_ExchangeFile_RIF_strategy)
@settings(max_examples=50)
def test_rif12_exchangefile_rif_instantiation(instance):
    assert isinstance(instance, rif12_ExchangeFile_RIF)

@given(instance=AttributeValueSimple_strategy)
@settings(max_examples=50)
def test_attributevaluesimple_instantiation(instance):
    assert isinstance(instance, AttributeValueSimple)

@given(instance=DatatypeDefinitionSimple_strategy)
@settings(max_examples=50)
def test_datatypedefinitionsimple_instantiation(instance):
    assert isinstance(instance, DatatypeDefinitionSimple)

@given(instance=rif12_ExchangeFile_DatatypeDefinitionInteger_strategy)
@settings(max_examples=50)
def test_rif12_exchangefile_datatypedefinitioninteger_instantiation(instance):
    assert isinstance(instance, rif12_ExchangeFile_DatatypeDefinitionInteger)



@given(instance=rif12_ExchangeFile_DatatypeDefinitionInteger_strategy)
def test_rif12_exchangefile_datatypedefinitioninteger_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original



@given(instance=rif12_ExchangeFile_DatatypeDefinitionInteger_strategy)
def test_rif12_exchangefile_datatypedefinitioninteger_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=rif12_ExchangeFile_DatatypeDefinitionString_strategy)
@settings(max_examples=50)
def test_rif12_exchangefile_datatypedefinitionstring_instantiation(instance):
    assert isinstance(instance, rif12_ExchangeFile_DatatypeDefinitionString)



@given(instance=rif12_ExchangeFile_DatatypeDefinitionString_strategy)
def test_rif12_exchangefile_datatypedefinitionstring_maxLength_setter(instance):
    original = instance.maxLength
    instance.maxLength = original
    assert instance.maxLength == original

@given(instance=rif12_ExchangeFile_DatatypeDefinitionReal_strategy)
@settings(max_examples=50)
def test_rif12_exchangefile_datatypedefinitionreal_instantiation(instance):
    assert isinstance(instance, rif12_ExchangeFile_DatatypeDefinitionReal)



@given(instance=rif12_ExchangeFile_DatatypeDefinitionReal_strategy)
def test_rif12_exchangefile_datatypedefinitionreal_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original



@given(instance=rif12_ExchangeFile_DatatypeDefinitionReal_strategy)
def test_rif12_exchangefile_datatypedefinitionreal_accuracy_setter(instance):
    original = instance.accuracy
    instance.accuracy = original
    assert instance.accuracy == original



@given(instance=rif12_ExchangeFile_DatatypeDefinitionReal_strategy)
def test_rif12_exchangefile_datatypedefinitionreal_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=AttributeDefinitionEnumeration_strategy)
@settings(max_examples=50)
def test_attributedefinitionenumeration_instantiation(instance):
    assert isinstance(instance, AttributeDefinitionEnumeration)

@given(instance=rif12_ExchangeFile_DatatypeDefinitionDate_strategy)
@settings(max_examples=50)
def test_rif12_exchangefile_datatypedefinitiondate_instantiation(instance):
    assert isinstance(instance, rif12_ExchangeFile_DatatypeDefinitionDate)



@given(instance=rif12_ExchangeFile_DatatypeDefinitionDate_strategy)
def test_rif12_exchangefile_datatypedefinitiondate_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original

@given(instance=rif12_ExchangeFile_DatatypeDefinitionBoolean_strategy)
@settings(max_examples=50)
def test_rif12_exchangefile_datatypedefinitionboolean_instantiation(instance):
    assert isinstance(instance, rif12_ExchangeFile_DatatypeDefinitionBoolean)

@given(instance=DataTypes_XmlContent_strategy)
@settings(max_examples=50)
def test_datatypes_xmlcontent_instantiation(instance):
    assert isinstance(instance, DataTypes_XmlContent)

@given(instance=DataTypes_BinaryContent_strategy)
@settings(max_examples=50)
def test_datatypes_binarycontent_instantiation(instance):
    assert isinstance(instance, DataTypes_BinaryContent)

@given(instance=DataTypes_XhtmlContent_strategy)
@settings(max_examples=50)
def test_datatypes_xhtmlcontent_instantiation(instance):
    assert isinstance(instance, DataTypes_XhtmlContent)

@given(instance=AttributeDefinitionComplex_strategy)
@settings(max_examples=50)
def test_attributedefinitioncomplex_instantiation(instance):
    assert isinstance(instance, AttributeDefinitionComplex)

@given(instance=AttributeDefinitionSimple_strategy)
@settings(max_examples=50)
def test_attributedefinitionsimple_instantiation(instance):
    assert isinstance(instance, AttributeDefinitionSimple)

@given(instance=SpecHierarchyRoot_strategy)
@settings(max_examples=50)
def test_spechierarchyroot_instantiation(instance):
    assert isinstance(instance, SpecHierarchyRoot)

@given(instance=DatatypeDefinition_strategy)
@settings(max_examples=50)
def test_datatypedefinition_instantiation(instance):
    assert isinstance(instance, DatatypeDefinition)

@given(instance=rif12_ExchangeFile_DatatypeDefinitionSimple_strategy)
@settings(max_examples=50)
def test_rif12_exchangefile_datatypedefinitionsimple_instantiation(instance):
    assert isinstance(instance, rif12_ExchangeFile_DatatypeDefinitionSimple)

@given(instance=rif12_ExchangeFile_EmbeddedValue_strategy)
@settings(max_examples=50)
def test_rif12_exchangefile_embeddedvalue_instantiation(instance):
    assert isinstance(instance, rif12_ExchangeFile_EmbeddedValue)



@given(instance=rif12_ExchangeFile_EmbeddedValue_strategy)
def test_rif12_exchangefile_embeddedvalue_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=rif12_ExchangeFile_EmbeddedValue_strategy)
def test_rif12_exchangefile_embeddedvalue_otherContent_setter(instance):
    original = instance.otherContent
    instance.otherContent = original
    assert instance.otherContent == original

@given(instance=EmbeddedValue_strategy)
@settings(max_examples=50)
def test_embeddedvalue_instantiation(instance):
    assert isinstance(instance, EmbeddedValue)

@given(instance=EnumValue_strategy)
@settings(max_examples=50)
def test_enumvalue_instantiation(instance):
    assert isinstance(instance, EnumValue)

@given(instance=rif12_ExchangeFile_DatatypeDefinitionEnumeration_strategy)
@settings(max_examples=50)
def test_rif12_exchangefile_datatypedefinitionenumeration_instantiation(instance):
    assert isinstance(instance, rif12_ExchangeFile_DatatypeDefinitionEnumeration)

@given(instance=AttributeValueEnumeration_strategy)
@settings(max_examples=50)
def test_attributevalueenumeration_instantiation(instance):
    assert isinstance(instance, AttributeValueEnumeration)

@given(instance=DatatypeDefinitionEnumeration_strategy)
@settings(max_examples=50)
def test_datatypedefinitionenumeration_instantiation(instance):
    assert isinstance(instance, DatatypeDefinitionEnumeration)

@given(instance=rif12_ExchangeFile_DatatypeDefinitionComplex_strategy)
@settings(max_examples=50)
def test_rif12_exchangefile_datatypedefinitioncomplex_instantiation(instance):
    assert isinstance(instance, rif12_ExchangeFile_DatatypeDefinitionComplex)



@given(instance=rif12_ExchangeFile_DatatypeDefinitionComplex_strategy)
def test_rif12_exchangefile_datatypedefinitioncomplex_embedded_setter(instance):
    original = instance.embedded
    instance.embedded = original
    assert instance.embedded == original

@given(instance=AttributeValueComplex_strategy)
@settings(max_examples=50)
def test_attributevaluecomplex_instantiation(instance):
    assert isinstance(instance, AttributeValueComplex)

@given(instance=rif12_ExchangeFile_AttributeValueEmbeddedFile_strategy)
@settings(max_examples=50)
def test_rif12_exchangefile_attributevalueembeddedfile_instantiation(instance):
    assert isinstance(instance, rif12_ExchangeFile_AttributeValueEmbeddedFile)

@given(instance=rif12_ExchangeFile_AttributeValueEmbeddedDocument_strategy)
@settings(max_examples=50)
def test_rif12_exchangefile_attributevalueembeddeddocument_instantiation(instance):
    assert isinstance(instance, rif12_ExchangeFile_AttributeValueEmbeddedDocument)

@given(instance=rif12_ExchangeFile_AttributeValueFileReference_strategy)
@settings(max_examples=50)
def test_rif12_exchangefile_attributevaluefilereference_instantiation(instance):
    assert isinstance(instance, rif12_ExchangeFile_AttributeValueFileReference)



@given(instance=rif12_ExchangeFile_AttributeValueFileReference_strategy)
def test_rif12_exchangefile_attributevaluefilereference_pathToFile_setter(instance):
    original = instance.pathToFile
    instance.pathToFile = original
    assert instance.pathToFile == original

@given(instance=rif12_ExchangeFile_AttributeValueXmlData_strategy)
@settings(max_examples=50)
def test_rif12_exchangefile_attributevaluexmldata_instantiation(instance):
    assert isinstance(instance, rif12_ExchangeFile_AttributeValueXmlData)

@given(instance=DatatypeDefinitionComplex_strategy)
@settings(max_examples=50)
def test_datatypedefinitioncomplex_instantiation(instance):
    assert isinstance(instance, DatatypeDefinitionComplex)

@given(instance=rif12_ExchangeFile_DatatypeDefinitionDocument_strategy)
@settings(max_examples=50)
def test_rif12_exchangefile_datatypedefinitiondocument_instantiation(instance):
    assert isinstance(instance, rif12_ExchangeFile_DatatypeDefinitionDocument)

@given(instance=rif12_ExchangeFile_DatatypeDefinitionBinaryFile_strategy)
@settings(max_examples=50)
def test_rif12_exchangefile_datatypedefinitionbinaryfile_instantiation(instance):
    assert isinstance(instance, rif12_ExchangeFile_DatatypeDefinitionBinaryFile)



@given(instance=rif12_ExchangeFile_DatatypeDefinitionBinaryFile_strategy)
def test_rif12_exchangefile_datatypedefinitionbinaryfile_formatName_setter(instance):
    original = instance.formatName
    instance.formatName = original
    assert instance.formatName == original



@given(instance=rif12_ExchangeFile_DatatypeDefinitionBinaryFile_strategy)
def test_rif12_exchangefile_datatypedefinitionbinaryfile_filenameSuffix_setter(instance):
    original = instance.filenameSuffix
    instance.filenameSuffix = original
    assert instance.filenameSuffix == original



@given(instance=rif12_ExchangeFile_DatatypeDefinitionBinaryFile_strategy)
def test_rif12_exchangefile_datatypedefinitionbinaryfile_application_setter(instance):
    original = instance.application
    instance.application = original
    assert instance.application == original



@given(instance=rif12_ExchangeFile_DatatypeDefinitionBinaryFile_strategy)
def test_rif12_exchangefile_datatypedefinitionbinaryfile_mimeType_setter(instance):
    original = instance.mimeType
    instance.mimeType = original
    assert instance.mimeType == original

@given(instance=rif12_ExchangeFile_DatatypeDefinitionXmlData_strategy)
@settings(max_examples=50)
def test_rif12_exchangefile_datatypedefinitionxmldata_instantiation(instance):
    assert isinstance(instance, rif12_ExchangeFile_DatatypeDefinitionXmlData)



@given(instance=rif12_ExchangeFile_DatatypeDefinitionXmlData_strategy)
def test_rif12_exchangefile_datatypedefinitionxmldata_schemaLocation_setter(instance):
    original = instance.schemaLocation
    instance.schemaLocation = original
    assert instance.schemaLocation == original



@given(instance=rif12_ExchangeFile_DatatypeDefinitionXmlData_strategy)
def test_rif12_exchangefile_datatypedefinitionxmldata_nameSpaceURI_setter(instance):
    original = instance.nameSpaceURI
    instance.nameSpaceURI = original
    assert instance.nameSpaceURI == original

@given(instance=SpecGroupHierarchy_strategy)
@settings(max_examples=50)
def test_specgrouphierarchy_instantiation(instance):
    assert isinstance(instance, SpecGroupHierarchy)

@given(instance=SpecObject_strategy)
@settings(max_examples=50)
def test_specobject_instantiation(instance):
    assert isinstance(instance, SpecObject)

@given(instance=AttributeDefinition_strategy)
@settings(max_examples=50)
def test_attributedefinition_instantiation(instance):
    assert isinstance(instance, AttributeDefinition)

@given(instance=rif12_ExchangeFile_AttributeDefinitionEnumeration_strategy)
@settings(max_examples=50)
def test_rif12_exchangefile_attributedefinitionenumeration_instantiation(instance):
    assert isinstance(instance, rif12_ExchangeFile_AttributeDefinitionEnumeration)



@given(instance=rif12_ExchangeFile_AttributeDefinitionEnumeration_strategy)
def test_rif12_exchangefile_attributedefinitionenumeration_multiValued_setter(instance):
    original = instance.multiValued
    instance.multiValued = original
    assert instance.multiValued == original

@given(instance=rif12_ExchangeFile_AttributeDefinitionComplex_strategy)
@settings(max_examples=50)
def test_rif12_exchangefile_attributedefinitioncomplex_instantiation(instance):
    assert isinstance(instance, rif12_ExchangeFile_AttributeDefinitionComplex)

@given(instance=rif12_ExchangeFile_AttributeDefinitionSimple_strategy)
@settings(max_examples=50)
def test_rif12_exchangefile_attributedefinitionsimple_instantiation(instance):
    assert isinstance(instance, rif12_ExchangeFile_AttributeDefinitionSimple)

@given(instance=SpecGroup_strategy)
@settings(max_examples=50)
def test_specgroup_instantiation(instance):
    assert isinstance(instance, SpecGroup)

@given(instance=SpecGroupHierarchyRoot_strategy)
@settings(max_examples=50)
def test_specgrouphierarchyroot_instantiation(instance):
    assert isinstance(instance, SpecGroupHierarchyRoot)

@given(instance=SpecRelation_strategy)
@settings(max_examples=50)
def test_specrelation_instantiation(instance):
    assert isinstance(instance, SpecRelation)

@given(instance=RelationGroup_strategy)
@settings(max_examples=50)
def test_relationgroup_instantiation(instance):
    assert isinstance(instance, RelationGroup)

@given(instance=rif12_ExchangeFile_Identifiable_strategy)
@settings(max_examples=50)
def test_rif12_exchangefile_identifiable_instantiation(instance):
    assert isinstance(instance, rif12_ExchangeFile_Identifiable)



@given(instance=rif12_ExchangeFile_Identifiable_strategy)
def test_rif12_exchangefile_identifiable_lastChange_setter(instance):
    original = instance.lastChange
    instance.lastChange = original
    assert instance.lastChange == original



@given(instance=rif12_ExchangeFile_Identifiable_strategy)
def test_rif12_exchangefile_identifiable_longName_setter(instance):
    original = instance.longName
    instance.longName = original
    assert instance.longName == original



@given(instance=rif12_ExchangeFile_Identifiable_strategy)
def test_rif12_exchangefile_identifiable_desc_setter(instance):
    original = instance.desc
    instance.desc = original
    assert instance.desc == original



@given(instance=rif12_ExchangeFile_Identifiable_strategy)
def test_rif12_exchangefile_identifiable_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=AttributeValue_strategy)
@settings(max_examples=50)
def test_attributevalue_instantiation(instance):
    assert isinstance(instance, AttributeValue)

@given(instance=rif12_ExchangeFile_AttributeValueEnumeration_strategy)
@settings(max_examples=50)
def test_rif12_exchangefile_attributevalueenumeration_instantiation(instance):
    assert isinstance(instance, rif12_ExchangeFile_AttributeValueEnumeration)

@given(instance=rif12_ExchangeFile_AttributeValueSimple_strategy)
@settings(max_examples=50)
def test_rif12_exchangefile_attributevaluesimple_instantiation(instance):
    assert isinstance(instance, rif12_ExchangeFile_AttributeValueSimple)



@given(instance=rif12_ExchangeFile_AttributeValueSimple_strategy)
def test_rif12_exchangefile_attributevaluesimple_theValue_setter(instance):
    original = instance.theValue
    instance.theValue = original
    assert instance.theValue == original

@given(instance=rif12_ExchangeFile_AttributeValueComplex_strategy)
@settings(max_examples=50)
def test_rif12_exchangefile_attributevaluecomplex_instantiation(instance):
    assert isinstance(instance, rif12_ExchangeFile_AttributeValueComplex)

@given(instance=SpecType_strategy)
@settings(max_examples=50)
def test_spectype_instantiation(instance):
    assert isinstance(instance, SpecType)

@given(instance=Identifiable_strategy)
@settings(max_examples=50)
def test_identifiable_instantiation(instance):
    assert isinstance(instance, Identifiable)

@given(instance=rif12_ExchangeFile_AttributeDefinition_strategy)
@settings(max_examples=50)
def test_rif12_exchangefile_attributedefinition_instantiation(instance):
    assert isinstance(instance, rif12_ExchangeFile_AttributeDefinition)

@given(instance=rif12_ExchangeFile_SpecGroupHierarchy_strategy)
@settings(max_examples=50)
def test_rif12_exchangefile_specgrouphierarchy_instantiation(instance):
    assert isinstance(instance, rif12_ExchangeFile_SpecGroupHierarchy)

@given(instance=rif12_ExchangeFile_DatatypeDefinition_strategy)
@settings(max_examples=50)
def test_rif12_exchangefile_datatypedefinition_instantiation(instance):
    assert isinstance(instance, rif12_ExchangeFile_DatatypeDefinition)

@given(instance=rif12_ExchangeFile_SpecType_strategy)
@settings(max_examples=50)
def test_rif12_exchangefile_spectype_instantiation(instance):
    assert isinstance(instance, rif12_ExchangeFile_SpecType)

@given(instance=rif12_ExchangeFile_RelationGroup_strategy)
@settings(max_examples=50)
def test_rif12_exchangefile_relationgroup_instantiation(instance):
    assert isinstance(instance, rif12_ExchangeFile_RelationGroup)

@given(instance=rif12_ExchangeFile_AttributeValue_strategy)
@settings(max_examples=50)
def test_rif12_exchangefile_attributevalue_instantiation(instance):
    assert isinstance(instance, rif12_ExchangeFile_AttributeValue)

@given(instance=rif12_ExchangeFile_SpecHierarchy_strategy)
@settings(max_examples=50)
def test_rif12_exchangefile_spechierarchy_instantiation(instance):
    assert isinstance(instance, rif12_ExchangeFile_SpecHierarchy)

@given(instance=rif12_ExchangeFile_AccessPolicy_strategy)
@settings(max_examples=50)
def test_rif12_exchangefile_accesspolicy_instantiation(instance):
    assert isinstance(instance, rif12_ExchangeFile_AccessPolicy)



@given(instance=rif12_ExchangeFile_AccessPolicy_strategy)
def test_rif12_exchangefile_accesspolicy_accessMode_setter(instance):
    original = instance.accessMode
    instance.accessMode = original
    assert instance.accessMode == original

@given(instance=rif12_ExchangeFile_EnumValue_strategy)
@settings(max_examples=50)
def test_rif12_exchangefile_enumvalue_instantiation(instance):
    assert isinstance(instance, rif12_ExchangeFile_EnumValue)

@given(instance=rif12_ExchangeFile_SpecElementWithUserDefinedAttributes_strategy)
@settings(max_examples=50)
def test_rif12_exchangefile_specelementwithuserdefinedattributes_instantiation(instance):
    assert isinstance(instance, rif12_ExchangeFile_SpecElementWithUserDefinedAttributes)

@given(instance=SpecHierarchy_strategy)
@settings(max_examples=50)
def test_spechierarchy_instantiation(instance):
    assert isinstance(instance, SpecHierarchy)

@given(instance=SpecElementWithUserDefinedAttributes_strategy)
@settings(max_examples=50)
def test_specelementwithuserdefinedattributes_instantiation(instance):
    assert isinstance(instance, SpecElementWithUserDefinedAttributes)

@given(instance=rif12_ExchangeFile_SpecGroup_strategy)
@settings(max_examples=50)
def test_rif12_exchangefile_specgroup_instantiation(instance):
    assert isinstance(instance, rif12_ExchangeFile_SpecGroup)

@given(instance=rif12_ExchangeFile_SpecGroupHierarchyRoot_strategy)
@settings(max_examples=50)
def test_rif12_exchangefile_specgrouphierarchyroot_instantiation(instance):
    assert isinstance(instance, rif12_ExchangeFile_SpecGroupHierarchyRoot)

@given(instance=rif12_ExchangeFile_SpecRelation_strategy)
@settings(max_examples=50)
def test_rif12_exchangefile_specrelation_instantiation(instance):
    assert isinstance(instance, rif12_ExchangeFile_SpecRelation)

@given(instance=rif12_ExchangeFile_SpecObject_strategy)
@settings(max_examples=50)
def test_rif12_exchangefile_specobject_instantiation(instance):
    assert isinstance(instance, rif12_ExchangeFile_SpecObject)

@given(instance=rif12_ExchangeFile_SpecHierarchyRoot_strategy)
@settings(max_examples=50)
def test_rif12_exchangefile_spechierarchyroot_instantiation(instance):
    assert isinstance(instance, rif12_ExchangeFile_SpecHierarchyRoot)
