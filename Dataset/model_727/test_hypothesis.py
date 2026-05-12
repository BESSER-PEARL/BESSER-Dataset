import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    rif11a_DataTypes_BinaryContent,
    ExchangeFile_AccessPolicy,
    rif11a_DataTypes_XhtmlContent,
    rif11a_DataTypes_XmlContent,
    DatatypeDefinitionSimple,
    rif11a_ExchangeFile_DatatypeDefinitionDate,
    rif11a_ExchangeFile_DatatypeDefinitionBoolean,
    DatatypeDefinitionComplex,
    rif11a_ExchangeFile_DatatypeDefinitionDocument,
    rif11a_ExchangeFile_DatatypeDefinitionBinaryFile,
    DataTypes_XmlContent,
    DataTypes_BinaryContent,
    rif11a_ExchangeFile_RIF,
    rif11a_ExchangeFile_DatatypeDefinitionXmlData,
    rif11a_ExchangeFile_DatatypeDefinitionString,
    rif11a_ExchangeFile_DatatypeDefinitionReal,
    rif11a_ExchangeFile_DatatypeDefinitionInteger,
    ExchangeFile_AttributeDefinitionEnumeration,
    rif11a_ExchangeFile_EmbeddedValue,
    ExchangeFile_EmbeddedValue,
    ExchangeFile_EnumValue,
    ExchangeFile_AttributeValueEnumeration,
    ExchangeFile_DatatypeDefinitionEnumeration,
    DataTypes_XhtmlContent,
    ExchangeFile_AttributeDefinitionComplex,
    AttributeValueComplex,
    rif11a_ExchangeFile_AttributeValueEmbeddedFile,
    rif11a_ExchangeFile_AttributeValueXmlData,
    rif11a_ExchangeFile_AttributeValueFileReference,
    rif11a_ExchangeFile_AttributeValueEmbeddedDocument,
    ExchangeFile_AttributeDefinitionSimple,
    ExchangeFile_AttributeValueSimple,
    ExchangeFile_DatatypeDefinitionSimple,
    ExchangeFile_DatatypeDefinition,
    ExchangeFile_SpecGroup,
    AttributeValue,
    rif11a_ExchangeFile_AttributeValueSimple,
    rif11a_ExchangeFile_AttributeValueEnumeration,
    rif11a_ExchangeFile_AttributeValueComplex,
    DatatypeDefinition,
    rif11a_ExchangeFile_DatatypeDefinitionSimple,
    rif11a_ExchangeFile_DatatypeDefinitionEnumeration,
    rif11a_ExchangeFile_DatatypeDefinitionComplex,
    ExchangeFile_AttributeValueComplex,
    ExchangeFile_DatatypeDefinitionComplex,
    AttributeDefinition,
    rif11a_ExchangeFile_AttributeDefinitionSimple,
    rif11a_ExchangeFile_AttributeDefinitionEnumeration,
    rif11a_ExchangeFile_AttributeDefinitionComplex,
    ExchangeFile_SpecHierarchyRoot,
    ExchangeFile_AttributeDefinition,
    rif11a_ExchangeFile_Identifiable,
    ExchangeFile_AttributeValue,
    ExchangeFile_SpecType,
    Identifiable,
    rif11a_ExchangeFile_DatatypeDefinition,
    rif11a_ExchangeFile_AttributeDefinition,
    rif11a_ExchangeFile_SpecType,
    rif11a_ExchangeFile_AttributeValue,
    rif11a_ExchangeFile_AccessPolicy,
    rif11a_ExchangeFile_EnumValue,
    rif11a_ExchangeFile_SpecElementWithUserDefinedAttributes,
    ExchangeFile_SpecHierarchy,
    ExchangeFile_SpecRelation,
    rif11a_ExchangeFile_RelationGroup,
    ExchangeFile_RelationGroup,
    ExchangeFile_SpecObject,
    rif11a_ExchangeFile_SpecHierarchy,
    SpecElementWithUserDefinedAttributes,
    rif11a_ExchangeFile_SpecGroup,
    rif11a_ExchangeFile_SpecRelation,
    rif11a_ExchangeFile_SpecObject,
    rif11a_ExchangeFile_SpecHierarchyRoot,
    DatatypeDefinitionDateFormatEnum,
    AccessPolicyAccessModeEnum,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rif11a_datatypes_binarycontent_is_not_abstract():
    assert not inspect.isabstract(rif11a_DataTypes_BinaryContent)


def test_rif11a_datatypes_binarycontent_constructor_exists():
    assert callable(rif11a_DataTypes_BinaryContent.__init__)


def test_rif11a_datatypes_binarycontent_constructor_args():
    sig = inspect.signature(rif11a_DataTypes_BinaryContent.__init__)
    params = list(sig.parameters.keys())



def test_exchangefile_accesspolicy_is_not_abstract():
    assert not inspect.isabstract(ExchangeFile_AccessPolicy)


def test_exchangefile_accesspolicy_constructor_exists():
    assert callable(ExchangeFile_AccessPolicy.__init__)


def test_exchangefile_accesspolicy_constructor_args():
    sig = inspect.signature(ExchangeFile_AccessPolicy.__init__)
    params = list(sig.parameters.keys())



def test_rif11a_datatypes_xhtmlcontent_is_not_abstract():
    assert not inspect.isabstract(rif11a_DataTypes_XhtmlContent)


def test_rif11a_datatypes_xhtmlcontent_constructor_exists():
    assert callable(rif11a_DataTypes_XhtmlContent.__init__)


def test_rif11a_datatypes_xhtmlcontent_constructor_args():
    sig = inspect.signature(rif11a_DataTypes_XhtmlContent.__init__)
    params = list(sig.parameters.keys())



def test_rif11a_datatypes_xmlcontent_is_not_abstract():
    assert not inspect.isabstract(rif11a_DataTypes_XmlContent)


def test_rif11a_datatypes_xmlcontent_constructor_exists():
    assert callable(rif11a_DataTypes_XmlContent.__init__)


def test_rif11a_datatypes_xmlcontent_constructor_args():
    sig = inspect.signature(rif11a_DataTypes_XmlContent.__init__)
    params = list(sig.parameters.keys())



def test_datatypedefinitionsimple_is_not_abstract():
    assert not inspect.isabstract(DatatypeDefinitionSimple)


def test_datatypedefinitionsimple_constructor_exists():
    assert callable(DatatypeDefinitionSimple.__init__)


def test_datatypedefinitionsimple_constructor_args():
    sig = inspect.signature(DatatypeDefinitionSimple.__init__)
    params = list(sig.parameters.keys())



def test_rif11a_exchangefile_datatypedefinitiondate_is_not_abstract():
    assert not inspect.isabstract(rif11a_ExchangeFile_DatatypeDefinitionDate)


def test_rif11a_exchangefile_datatypedefinitiondate_constructor_exists():
    assert callable(rif11a_ExchangeFile_DatatypeDefinitionDate.__init__)


def test_rif11a_exchangefile_datatypedefinitiondate_constructor_args():
    sig = inspect.signature(rif11a_ExchangeFile_DatatypeDefinitionDate.__init__)
    params = list(sig.parameters.keys())
    assert "format" in params, "Missing parameter 'format'"

def test_rif11a_exchangefile_datatypedefinitiondate_has_format():
    assert hasattr(rif11a_ExchangeFile_DatatypeDefinitionDate, "format")
    descriptor = None
    for klass in rif11a_ExchangeFile_DatatypeDefinitionDate.__mro__:
        if "format" in klass.__dict__:
            descriptor = klass.__dict__["format"]
            break
    assert isinstance(descriptor, property)



def test_rif11a_exchangefile_datatypedefinitionboolean_is_not_abstract():
    assert not inspect.isabstract(rif11a_ExchangeFile_DatatypeDefinitionBoolean)


def test_rif11a_exchangefile_datatypedefinitionboolean_constructor_exists():
    assert callable(rif11a_ExchangeFile_DatatypeDefinitionBoolean.__init__)


def test_rif11a_exchangefile_datatypedefinitionboolean_constructor_args():
    sig = inspect.signature(rif11a_ExchangeFile_DatatypeDefinitionBoolean.__init__)
    params = list(sig.parameters.keys())



def test_datatypedefinitioncomplex_is_not_abstract():
    assert not inspect.isabstract(DatatypeDefinitionComplex)


def test_datatypedefinitioncomplex_constructor_exists():
    assert callable(DatatypeDefinitionComplex.__init__)


def test_datatypedefinitioncomplex_constructor_args():
    sig = inspect.signature(DatatypeDefinitionComplex.__init__)
    params = list(sig.parameters.keys())



def test_rif11a_exchangefile_datatypedefinitiondocument_is_not_abstract():
    assert not inspect.isabstract(rif11a_ExchangeFile_DatatypeDefinitionDocument)


def test_rif11a_exchangefile_datatypedefinitiondocument_constructor_exists():
    assert callable(rif11a_ExchangeFile_DatatypeDefinitionDocument.__init__)


def test_rif11a_exchangefile_datatypedefinitiondocument_constructor_args():
    sig = inspect.signature(rif11a_ExchangeFile_DatatypeDefinitionDocument.__init__)
    params = list(sig.parameters.keys())



def test_rif11a_exchangefile_datatypedefinitionbinaryfile_is_not_abstract():
    assert not inspect.isabstract(rif11a_ExchangeFile_DatatypeDefinitionBinaryFile)


def test_rif11a_exchangefile_datatypedefinitionbinaryfile_constructor_exists():
    assert callable(rif11a_ExchangeFile_DatatypeDefinitionBinaryFile.__init__)


def test_rif11a_exchangefile_datatypedefinitionbinaryfile_constructor_args():
    sig = inspect.signature(rif11a_ExchangeFile_DatatypeDefinitionBinaryFile.__init__)
    params = list(sig.parameters.keys())
    assert "mimeType" in params, "Missing parameter 'mimeType'"
    assert "application" in params, "Missing parameter 'application'"
    assert "filenameSuffix" in params, "Missing parameter 'filenameSuffix'"
    assert "formatName" in params, "Missing parameter 'formatName'"

def test_rif11a_exchangefile_datatypedefinitionbinaryfile_has_mimeType():
    assert hasattr(rif11a_ExchangeFile_DatatypeDefinitionBinaryFile, "mimeType")
    descriptor = None
    for klass in rif11a_ExchangeFile_DatatypeDefinitionBinaryFile.__mro__:
        if "mimeType" in klass.__dict__:
            descriptor = klass.__dict__["mimeType"]
            break
    assert isinstance(descriptor, property)

def test_rif11a_exchangefile_datatypedefinitionbinaryfile_has_application():
    assert hasattr(rif11a_ExchangeFile_DatatypeDefinitionBinaryFile, "application")
    descriptor = None
    for klass in rif11a_ExchangeFile_DatatypeDefinitionBinaryFile.__mro__:
        if "application" in klass.__dict__:
            descriptor = klass.__dict__["application"]
            break
    assert isinstance(descriptor, property)

def test_rif11a_exchangefile_datatypedefinitionbinaryfile_has_filenameSuffix():
    assert hasattr(rif11a_ExchangeFile_DatatypeDefinitionBinaryFile, "filenameSuffix")
    descriptor = None
    for klass in rif11a_ExchangeFile_DatatypeDefinitionBinaryFile.__mro__:
        if "filenameSuffix" in klass.__dict__:
            descriptor = klass.__dict__["filenameSuffix"]
            break
    assert isinstance(descriptor, property)

def test_rif11a_exchangefile_datatypedefinitionbinaryfile_has_formatName():
    assert hasattr(rif11a_ExchangeFile_DatatypeDefinitionBinaryFile, "formatName")
    descriptor = None
    for klass in rif11a_ExchangeFile_DatatypeDefinitionBinaryFile.__mro__:
        if "formatName" in klass.__dict__:
            descriptor = klass.__dict__["formatName"]
            break
    assert isinstance(descriptor, property)



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



def test_rif11a_exchangefile_rif_is_not_abstract():
    assert not inspect.isabstract(rif11a_ExchangeFile_RIF)


def test_rif11a_exchangefile_rif_constructor_exists():
    assert callable(rif11a_ExchangeFile_RIF.__init__)


def test_rif11a_exchangefile_rif_constructor_args():
    sig = inspect.signature(rif11a_ExchangeFile_RIF.__init__)
    params = list(sig.parameters.keys())
    assert "author" in params, "Missing parameter 'author'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "version" in params, "Missing parameter 'version'"
    assert "creationTime" in params, "Missing parameter 'creationTime'"
    assert "title" in params, "Missing parameter 'title'"
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "sourceToolId" in params, "Missing parameter 'sourceToolId'"
    assert "countryCode" in params, "Missing parameter 'countryCode'"

def test_rif11a_exchangefile_rif_has_author():
    assert hasattr(rif11a_ExchangeFile_RIF, "author")
    descriptor = None
    for klass in rif11a_ExchangeFile_RIF.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_rif11a_exchangefile_rif_has_comment():
    assert hasattr(rif11a_ExchangeFile_RIF, "comment")
    descriptor = None
    for klass in rif11a_ExchangeFile_RIF.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_rif11a_exchangefile_rif_has_version():
    assert hasattr(rif11a_ExchangeFile_RIF, "version")
    descriptor = None
    for klass in rif11a_ExchangeFile_RIF.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_rif11a_exchangefile_rif_has_creationTime():
    assert hasattr(rif11a_ExchangeFile_RIF, "creationTime")
    descriptor = None
    for klass in rif11a_ExchangeFile_RIF.__mro__:
        if "creationTime" in klass.__dict__:
            descriptor = klass.__dict__["creationTime"]
            break
    assert isinstance(descriptor, property)

def test_rif11a_exchangefile_rif_has_title():
    assert hasattr(rif11a_ExchangeFile_RIF, "title")
    descriptor = None
    for klass in rif11a_ExchangeFile_RIF.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_rif11a_exchangefile_rif_has_identifier():
    assert hasattr(rif11a_ExchangeFile_RIF, "identifier")
    descriptor = None
    for klass in rif11a_ExchangeFile_RIF.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)

def test_rif11a_exchangefile_rif_has_sourceToolId():
    assert hasattr(rif11a_ExchangeFile_RIF, "sourceToolId")
    descriptor = None
    for klass in rif11a_ExchangeFile_RIF.__mro__:
        if "sourceToolId" in klass.__dict__:
            descriptor = klass.__dict__["sourceToolId"]
            break
    assert isinstance(descriptor, property)

def test_rif11a_exchangefile_rif_has_countryCode():
    assert hasattr(rif11a_ExchangeFile_RIF, "countryCode")
    descriptor = None
    for klass in rif11a_ExchangeFile_RIF.__mro__:
        if "countryCode" in klass.__dict__:
            descriptor = klass.__dict__["countryCode"]
            break
    assert isinstance(descriptor, property)



def test_rif11a_exchangefile_datatypedefinitionxmldata_is_not_abstract():
    assert not inspect.isabstract(rif11a_ExchangeFile_DatatypeDefinitionXmlData)


def test_rif11a_exchangefile_datatypedefinitionxmldata_constructor_exists():
    assert callable(rif11a_ExchangeFile_DatatypeDefinitionXmlData.__init__)


def test_rif11a_exchangefile_datatypedefinitionxmldata_constructor_args():
    sig = inspect.signature(rif11a_ExchangeFile_DatatypeDefinitionXmlData.__init__)
    params = list(sig.parameters.keys())
    assert "schemaLocation" in params, "Missing parameter 'schemaLocation'"
    assert "nameSpaceURI" in params, "Missing parameter 'nameSpaceURI'"

def test_rif11a_exchangefile_datatypedefinitionxmldata_has_schemaLocation():
    assert hasattr(rif11a_ExchangeFile_DatatypeDefinitionXmlData, "schemaLocation")
    descriptor = None
    for klass in rif11a_ExchangeFile_DatatypeDefinitionXmlData.__mro__:
        if "schemaLocation" in klass.__dict__:
            descriptor = klass.__dict__["schemaLocation"]
            break
    assert isinstance(descriptor, property)

def test_rif11a_exchangefile_datatypedefinitionxmldata_has_nameSpaceURI():
    assert hasattr(rif11a_ExchangeFile_DatatypeDefinitionXmlData, "nameSpaceURI")
    descriptor = None
    for klass in rif11a_ExchangeFile_DatatypeDefinitionXmlData.__mro__:
        if "nameSpaceURI" in klass.__dict__:
            descriptor = klass.__dict__["nameSpaceURI"]
            break
    assert isinstance(descriptor, property)



def test_rif11a_exchangefile_datatypedefinitionstring_is_not_abstract():
    assert not inspect.isabstract(rif11a_ExchangeFile_DatatypeDefinitionString)


def test_rif11a_exchangefile_datatypedefinitionstring_constructor_exists():
    assert callable(rif11a_ExchangeFile_DatatypeDefinitionString.__init__)


def test_rif11a_exchangefile_datatypedefinitionstring_constructor_args():
    sig = inspect.signature(rif11a_ExchangeFile_DatatypeDefinitionString.__init__)
    params = list(sig.parameters.keys())
    assert "maxLength" in params, "Missing parameter 'maxLength'"

def test_rif11a_exchangefile_datatypedefinitionstring_has_maxLength():
    assert hasattr(rif11a_ExchangeFile_DatatypeDefinitionString, "maxLength")
    descriptor = None
    for klass in rif11a_ExchangeFile_DatatypeDefinitionString.__mro__:
        if "maxLength" in klass.__dict__:
            descriptor = klass.__dict__["maxLength"]
            break
    assert isinstance(descriptor, property)



def test_rif11a_exchangefile_datatypedefinitionreal_is_not_abstract():
    assert not inspect.isabstract(rif11a_ExchangeFile_DatatypeDefinitionReal)


def test_rif11a_exchangefile_datatypedefinitionreal_constructor_exists():
    assert callable(rif11a_ExchangeFile_DatatypeDefinitionReal.__init__)


def test_rif11a_exchangefile_datatypedefinitionreal_constructor_args():
    sig = inspect.signature(rif11a_ExchangeFile_DatatypeDefinitionReal.__init__)
    params = list(sig.parameters.keys())
    assert "max" in params, "Missing parameter 'max'"
    assert "min" in params, "Missing parameter 'min'"
    assert "accuracy" in params, "Missing parameter 'accuracy'"

def test_rif11a_exchangefile_datatypedefinitionreal_has_max():
    assert hasattr(rif11a_ExchangeFile_DatatypeDefinitionReal, "max")
    descriptor = None
    for klass in rif11a_ExchangeFile_DatatypeDefinitionReal.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_rif11a_exchangefile_datatypedefinitionreal_has_min():
    assert hasattr(rif11a_ExchangeFile_DatatypeDefinitionReal, "min")
    descriptor = None
    for klass in rif11a_ExchangeFile_DatatypeDefinitionReal.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_rif11a_exchangefile_datatypedefinitionreal_has_accuracy():
    assert hasattr(rif11a_ExchangeFile_DatatypeDefinitionReal, "accuracy")
    descriptor = None
    for klass in rif11a_ExchangeFile_DatatypeDefinitionReal.__mro__:
        if "accuracy" in klass.__dict__:
            descriptor = klass.__dict__["accuracy"]
            break
    assert isinstance(descriptor, property)



def test_rif11a_exchangefile_datatypedefinitioninteger_is_not_abstract():
    assert not inspect.isabstract(rif11a_ExchangeFile_DatatypeDefinitionInteger)


def test_rif11a_exchangefile_datatypedefinitioninteger_constructor_exists():
    assert callable(rif11a_ExchangeFile_DatatypeDefinitionInteger.__init__)


def test_rif11a_exchangefile_datatypedefinitioninteger_constructor_args():
    sig = inspect.signature(rif11a_ExchangeFile_DatatypeDefinitionInteger.__init__)
    params = list(sig.parameters.keys())
    assert "min" in params, "Missing parameter 'min'"
    assert "max" in params, "Missing parameter 'max'"

def test_rif11a_exchangefile_datatypedefinitioninteger_has_min():
    assert hasattr(rif11a_ExchangeFile_DatatypeDefinitionInteger, "min")
    descriptor = None
    for klass in rif11a_ExchangeFile_DatatypeDefinitionInteger.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_rif11a_exchangefile_datatypedefinitioninteger_has_max():
    assert hasattr(rif11a_ExchangeFile_DatatypeDefinitionInteger, "max")
    descriptor = None
    for klass in rif11a_ExchangeFile_DatatypeDefinitionInteger.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)



def test_exchangefile_attributedefinitionenumeration_is_not_abstract():
    assert not inspect.isabstract(ExchangeFile_AttributeDefinitionEnumeration)


def test_exchangefile_attributedefinitionenumeration_constructor_exists():
    assert callable(ExchangeFile_AttributeDefinitionEnumeration.__init__)


def test_exchangefile_attributedefinitionenumeration_constructor_args():
    sig = inspect.signature(ExchangeFile_AttributeDefinitionEnumeration.__init__)
    params = list(sig.parameters.keys())



def test_rif11a_exchangefile_embeddedvalue_is_not_abstract():
    assert not inspect.isabstract(rif11a_ExchangeFile_EmbeddedValue)


def test_rif11a_exchangefile_embeddedvalue_constructor_exists():
    assert callable(rif11a_ExchangeFile_EmbeddedValue.__init__)


def test_rif11a_exchangefile_embeddedvalue_constructor_args():
    sig = inspect.signature(rif11a_ExchangeFile_EmbeddedValue.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "otherContent" in params, "Missing parameter 'otherContent'"

def test_rif11a_exchangefile_embeddedvalue_has_key():
    assert hasattr(rif11a_ExchangeFile_EmbeddedValue, "key")
    descriptor = None
    for klass in rif11a_ExchangeFile_EmbeddedValue.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_rif11a_exchangefile_embeddedvalue_has_otherContent():
    assert hasattr(rif11a_ExchangeFile_EmbeddedValue, "otherContent")
    descriptor = None
    for klass in rif11a_ExchangeFile_EmbeddedValue.__mro__:
        if "otherContent" in klass.__dict__:
            descriptor = klass.__dict__["otherContent"]
            break
    assert isinstance(descriptor, property)



def test_exchangefile_embeddedvalue_is_not_abstract():
    assert not inspect.isabstract(ExchangeFile_EmbeddedValue)


def test_exchangefile_embeddedvalue_constructor_exists():
    assert callable(ExchangeFile_EmbeddedValue.__init__)


def test_exchangefile_embeddedvalue_constructor_args():
    sig = inspect.signature(ExchangeFile_EmbeddedValue.__init__)
    params = list(sig.parameters.keys())



def test_exchangefile_enumvalue_is_not_abstract():
    assert not inspect.isabstract(ExchangeFile_EnumValue)


def test_exchangefile_enumvalue_constructor_exists():
    assert callable(ExchangeFile_EnumValue.__init__)


def test_exchangefile_enumvalue_constructor_args():
    sig = inspect.signature(ExchangeFile_EnumValue.__init__)
    params = list(sig.parameters.keys())



def test_exchangefile_attributevalueenumeration_is_not_abstract():
    assert not inspect.isabstract(ExchangeFile_AttributeValueEnumeration)


def test_exchangefile_attributevalueenumeration_constructor_exists():
    assert callable(ExchangeFile_AttributeValueEnumeration.__init__)


def test_exchangefile_attributevalueenumeration_constructor_args():
    sig = inspect.signature(ExchangeFile_AttributeValueEnumeration.__init__)
    params = list(sig.parameters.keys())



def test_exchangefile_datatypedefinitionenumeration_is_not_abstract():
    assert not inspect.isabstract(ExchangeFile_DatatypeDefinitionEnumeration)


def test_exchangefile_datatypedefinitionenumeration_constructor_exists():
    assert callable(ExchangeFile_DatatypeDefinitionEnumeration.__init__)


def test_exchangefile_datatypedefinitionenumeration_constructor_args():
    sig = inspect.signature(ExchangeFile_DatatypeDefinitionEnumeration.__init__)
    params = list(sig.parameters.keys())



def test_datatypes_xhtmlcontent_is_not_abstract():
    assert not inspect.isabstract(DataTypes_XhtmlContent)


def test_datatypes_xhtmlcontent_constructor_exists():
    assert callable(DataTypes_XhtmlContent.__init__)


def test_datatypes_xhtmlcontent_constructor_args():
    sig = inspect.signature(DataTypes_XhtmlContent.__init__)
    params = list(sig.parameters.keys())



def test_exchangefile_attributedefinitioncomplex_is_not_abstract():
    assert not inspect.isabstract(ExchangeFile_AttributeDefinitionComplex)


def test_exchangefile_attributedefinitioncomplex_constructor_exists():
    assert callable(ExchangeFile_AttributeDefinitionComplex.__init__)


def test_exchangefile_attributedefinitioncomplex_constructor_args():
    sig = inspect.signature(ExchangeFile_AttributeDefinitionComplex.__init__)
    params = list(sig.parameters.keys())



def test_attributevaluecomplex_is_not_abstract():
    assert not inspect.isabstract(AttributeValueComplex)


def test_attributevaluecomplex_constructor_exists():
    assert callable(AttributeValueComplex.__init__)


def test_attributevaluecomplex_constructor_args():
    sig = inspect.signature(AttributeValueComplex.__init__)
    params = list(sig.parameters.keys())



def test_rif11a_exchangefile_attributevalueembeddedfile_is_not_abstract():
    assert not inspect.isabstract(rif11a_ExchangeFile_AttributeValueEmbeddedFile)


def test_rif11a_exchangefile_attributevalueembeddedfile_constructor_exists():
    assert callable(rif11a_ExchangeFile_AttributeValueEmbeddedFile.__init__)


def test_rif11a_exchangefile_attributevalueembeddedfile_constructor_args():
    sig = inspect.signature(rif11a_ExchangeFile_AttributeValueEmbeddedFile.__init__)
    params = list(sig.parameters.keys())



def test_rif11a_exchangefile_attributevaluexmldata_is_not_abstract():
    assert not inspect.isabstract(rif11a_ExchangeFile_AttributeValueXmlData)


def test_rif11a_exchangefile_attributevaluexmldata_constructor_exists():
    assert callable(rif11a_ExchangeFile_AttributeValueXmlData.__init__)


def test_rif11a_exchangefile_attributevaluexmldata_constructor_args():
    sig = inspect.signature(rif11a_ExchangeFile_AttributeValueXmlData.__init__)
    params = list(sig.parameters.keys())



def test_rif11a_exchangefile_attributevaluefilereference_is_not_abstract():
    assert not inspect.isabstract(rif11a_ExchangeFile_AttributeValueFileReference)


def test_rif11a_exchangefile_attributevaluefilereference_constructor_exists():
    assert callable(rif11a_ExchangeFile_AttributeValueFileReference.__init__)


def test_rif11a_exchangefile_attributevaluefilereference_constructor_args():
    sig = inspect.signature(rif11a_ExchangeFile_AttributeValueFileReference.__init__)
    params = list(sig.parameters.keys())
    assert "pathToFile" in params, "Missing parameter 'pathToFile'"

def test_rif11a_exchangefile_attributevaluefilereference_has_pathToFile():
    assert hasattr(rif11a_ExchangeFile_AttributeValueFileReference, "pathToFile")
    descriptor = None
    for klass in rif11a_ExchangeFile_AttributeValueFileReference.__mro__:
        if "pathToFile" in klass.__dict__:
            descriptor = klass.__dict__["pathToFile"]
            break
    assert isinstance(descriptor, property)



def test_rif11a_exchangefile_attributevalueembeddeddocument_is_not_abstract():
    assert not inspect.isabstract(rif11a_ExchangeFile_AttributeValueEmbeddedDocument)


def test_rif11a_exchangefile_attributevalueembeddeddocument_constructor_exists():
    assert callable(rif11a_ExchangeFile_AttributeValueEmbeddedDocument.__init__)


def test_rif11a_exchangefile_attributevalueembeddeddocument_constructor_args():
    sig = inspect.signature(rif11a_ExchangeFile_AttributeValueEmbeddedDocument.__init__)
    params = list(sig.parameters.keys())



def test_exchangefile_attributedefinitionsimple_is_not_abstract():
    assert not inspect.isabstract(ExchangeFile_AttributeDefinitionSimple)


def test_exchangefile_attributedefinitionsimple_constructor_exists():
    assert callable(ExchangeFile_AttributeDefinitionSimple.__init__)


def test_exchangefile_attributedefinitionsimple_constructor_args():
    sig = inspect.signature(ExchangeFile_AttributeDefinitionSimple.__init__)
    params = list(sig.parameters.keys())



def test_exchangefile_attributevaluesimple_is_not_abstract():
    assert not inspect.isabstract(ExchangeFile_AttributeValueSimple)


def test_exchangefile_attributevaluesimple_constructor_exists():
    assert callable(ExchangeFile_AttributeValueSimple.__init__)


def test_exchangefile_attributevaluesimple_constructor_args():
    sig = inspect.signature(ExchangeFile_AttributeValueSimple.__init__)
    params = list(sig.parameters.keys())



def test_exchangefile_datatypedefinitionsimple_is_not_abstract():
    assert not inspect.isabstract(ExchangeFile_DatatypeDefinitionSimple)


def test_exchangefile_datatypedefinitionsimple_constructor_exists():
    assert callable(ExchangeFile_DatatypeDefinitionSimple.__init__)


def test_exchangefile_datatypedefinitionsimple_constructor_args():
    sig = inspect.signature(ExchangeFile_DatatypeDefinitionSimple.__init__)
    params = list(sig.parameters.keys())



def test_exchangefile_datatypedefinition_is_not_abstract():
    assert not inspect.isabstract(ExchangeFile_DatatypeDefinition)


def test_exchangefile_datatypedefinition_constructor_exists():
    assert callable(ExchangeFile_DatatypeDefinition.__init__)


def test_exchangefile_datatypedefinition_constructor_args():
    sig = inspect.signature(ExchangeFile_DatatypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_exchangefile_specgroup_is_not_abstract():
    assert not inspect.isabstract(ExchangeFile_SpecGroup)


def test_exchangefile_specgroup_constructor_exists():
    assert callable(ExchangeFile_SpecGroup.__init__)


def test_exchangefile_specgroup_constructor_args():
    sig = inspect.signature(ExchangeFile_SpecGroup.__init__)
    params = list(sig.parameters.keys())



def test_attributevalue_is_not_abstract():
    assert not inspect.isabstract(AttributeValue)


def test_attributevalue_constructor_exists():
    assert callable(AttributeValue.__init__)


def test_attributevalue_constructor_args():
    sig = inspect.signature(AttributeValue.__init__)
    params = list(sig.parameters.keys())



def test_rif11a_exchangefile_attributevaluesimple_is_not_abstract():
    assert not inspect.isabstract(rif11a_ExchangeFile_AttributeValueSimple)


def test_rif11a_exchangefile_attributevaluesimple_constructor_exists():
    assert callable(rif11a_ExchangeFile_AttributeValueSimple.__init__)


def test_rif11a_exchangefile_attributevaluesimple_constructor_args():
    sig = inspect.signature(rif11a_ExchangeFile_AttributeValueSimple.__init__)
    params = list(sig.parameters.keys())
    assert "theValue" in params, "Missing parameter 'theValue'"

def test_rif11a_exchangefile_attributevaluesimple_has_theValue():
    assert hasattr(rif11a_ExchangeFile_AttributeValueSimple, "theValue")
    descriptor = None
    for klass in rif11a_ExchangeFile_AttributeValueSimple.__mro__:
        if "theValue" in klass.__dict__:
            descriptor = klass.__dict__["theValue"]
            break
    assert isinstance(descriptor, property)



def test_rif11a_exchangefile_attributevalueenumeration_is_not_abstract():
    assert not inspect.isabstract(rif11a_ExchangeFile_AttributeValueEnumeration)


def test_rif11a_exchangefile_attributevalueenumeration_constructor_exists():
    assert callable(rif11a_ExchangeFile_AttributeValueEnumeration.__init__)


def test_rif11a_exchangefile_attributevalueenumeration_constructor_args():
    sig = inspect.signature(rif11a_ExchangeFile_AttributeValueEnumeration.__init__)
    params = list(sig.parameters.keys())



def test_rif11a_exchangefile_attributevaluecomplex_is_not_abstract():
    assert not inspect.isabstract(rif11a_ExchangeFile_AttributeValueComplex)


def test_rif11a_exchangefile_attributevaluecomplex_constructor_exists():
    assert callable(rif11a_ExchangeFile_AttributeValueComplex.__init__)


def test_rif11a_exchangefile_attributevaluecomplex_constructor_args():
    sig = inspect.signature(rif11a_ExchangeFile_AttributeValueComplex.__init__)
    params = list(sig.parameters.keys())



def test_datatypedefinition_is_not_abstract():
    assert not inspect.isabstract(DatatypeDefinition)


def test_datatypedefinition_constructor_exists():
    assert callable(DatatypeDefinition.__init__)


def test_datatypedefinition_constructor_args():
    sig = inspect.signature(DatatypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_rif11a_exchangefile_datatypedefinitionsimple_is_not_abstract():
    assert not inspect.isabstract(rif11a_ExchangeFile_DatatypeDefinitionSimple)


def test_rif11a_exchangefile_datatypedefinitionsimple_constructor_exists():
    assert callable(rif11a_ExchangeFile_DatatypeDefinitionSimple.__init__)


def test_rif11a_exchangefile_datatypedefinitionsimple_constructor_args():
    sig = inspect.signature(rif11a_ExchangeFile_DatatypeDefinitionSimple.__init__)
    params = list(sig.parameters.keys())



def test_rif11a_exchangefile_datatypedefinitionenumeration_is_not_abstract():
    assert not inspect.isabstract(rif11a_ExchangeFile_DatatypeDefinitionEnumeration)


def test_rif11a_exchangefile_datatypedefinitionenumeration_constructor_exists():
    assert callable(rif11a_ExchangeFile_DatatypeDefinitionEnumeration.__init__)


def test_rif11a_exchangefile_datatypedefinitionenumeration_constructor_args():
    sig = inspect.signature(rif11a_ExchangeFile_DatatypeDefinitionEnumeration.__init__)
    params = list(sig.parameters.keys())



def test_rif11a_exchangefile_datatypedefinitioncomplex_is_not_abstract():
    assert not inspect.isabstract(rif11a_ExchangeFile_DatatypeDefinitionComplex)


def test_rif11a_exchangefile_datatypedefinitioncomplex_constructor_exists():
    assert callable(rif11a_ExchangeFile_DatatypeDefinitionComplex.__init__)


def test_rif11a_exchangefile_datatypedefinitioncomplex_constructor_args():
    sig = inspect.signature(rif11a_ExchangeFile_DatatypeDefinitionComplex.__init__)
    params = list(sig.parameters.keys())
    assert "embedded" in params, "Missing parameter 'embedded'"

def test_rif11a_exchangefile_datatypedefinitioncomplex_has_embedded():
    assert hasattr(rif11a_ExchangeFile_DatatypeDefinitionComplex, "embedded")
    descriptor = None
    for klass in rif11a_ExchangeFile_DatatypeDefinitionComplex.__mro__:
        if "embedded" in klass.__dict__:
            descriptor = klass.__dict__["embedded"]
            break
    assert isinstance(descriptor, property)



def test_exchangefile_attributevaluecomplex_is_not_abstract():
    assert not inspect.isabstract(ExchangeFile_AttributeValueComplex)


def test_exchangefile_attributevaluecomplex_constructor_exists():
    assert callable(ExchangeFile_AttributeValueComplex.__init__)


def test_exchangefile_attributevaluecomplex_constructor_args():
    sig = inspect.signature(ExchangeFile_AttributeValueComplex.__init__)
    params = list(sig.parameters.keys())



def test_exchangefile_datatypedefinitioncomplex_is_not_abstract():
    assert not inspect.isabstract(ExchangeFile_DatatypeDefinitionComplex)


def test_exchangefile_datatypedefinitioncomplex_constructor_exists():
    assert callable(ExchangeFile_DatatypeDefinitionComplex.__init__)


def test_exchangefile_datatypedefinitioncomplex_constructor_args():
    sig = inspect.signature(ExchangeFile_DatatypeDefinitionComplex.__init__)
    params = list(sig.parameters.keys())



def test_attributedefinition_is_not_abstract():
    assert not inspect.isabstract(AttributeDefinition)


def test_attributedefinition_constructor_exists():
    assert callable(AttributeDefinition.__init__)


def test_attributedefinition_constructor_args():
    sig = inspect.signature(AttributeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_rif11a_exchangefile_attributedefinitionsimple_is_not_abstract():
    assert not inspect.isabstract(rif11a_ExchangeFile_AttributeDefinitionSimple)


def test_rif11a_exchangefile_attributedefinitionsimple_constructor_exists():
    assert callable(rif11a_ExchangeFile_AttributeDefinitionSimple.__init__)


def test_rif11a_exchangefile_attributedefinitionsimple_constructor_args():
    sig = inspect.signature(rif11a_ExchangeFile_AttributeDefinitionSimple.__init__)
    params = list(sig.parameters.keys())



def test_rif11a_exchangefile_attributedefinitionenumeration_is_not_abstract():
    assert not inspect.isabstract(rif11a_ExchangeFile_AttributeDefinitionEnumeration)


def test_rif11a_exchangefile_attributedefinitionenumeration_constructor_exists():
    assert callable(rif11a_ExchangeFile_AttributeDefinitionEnumeration.__init__)


def test_rif11a_exchangefile_attributedefinitionenumeration_constructor_args():
    sig = inspect.signature(rif11a_ExchangeFile_AttributeDefinitionEnumeration.__init__)
    params = list(sig.parameters.keys())
    assert "multiValued" in params, "Missing parameter 'multiValued'"

def test_rif11a_exchangefile_attributedefinitionenumeration_has_multiValued():
    assert hasattr(rif11a_ExchangeFile_AttributeDefinitionEnumeration, "multiValued")
    descriptor = None
    for klass in rif11a_ExchangeFile_AttributeDefinitionEnumeration.__mro__:
        if "multiValued" in klass.__dict__:
            descriptor = klass.__dict__["multiValued"]
            break
    assert isinstance(descriptor, property)



def test_rif11a_exchangefile_attributedefinitioncomplex_is_not_abstract():
    assert not inspect.isabstract(rif11a_ExchangeFile_AttributeDefinitionComplex)


def test_rif11a_exchangefile_attributedefinitioncomplex_constructor_exists():
    assert callable(rif11a_ExchangeFile_AttributeDefinitionComplex.__init__)


def test_rif11a_exchangefile_attributedefinitioncomplex_constructor_args():
    sig = inspect.signature(rif11a_ExchangeFile_AttributeDefinitionComplex.__init__)
    params = list(sig.parameters.keys())



def test_exchangefile_spechierarchyroot_is_not_abstract():
    assert not inspect.isabstract(ExchangeFile_SpecHierarchyRoot)


def test_exchangefile_spechierarchyroot_constructor_exists():
    assert callable(ExchangeFile_SpecHierarchyRoot.__init__)


def test_exchangefile_spechierarchyroot_constructor_args():
    sig = inspect.signature(ExchangeFile_SpecHierarchyRoot.__init__)
    params = list(sig.parameters.keys())



def test_exchangefile_attributedefinition_is_not_abstract():
    assert not inspect.isabstract(ExchangeFile_AttributeDefinition)


def test_exchangefile_attributedefinition_constructor_exists():
    assert callable(ExchangeFile_AttributeDefinition.__init__)


def test_exchangefile_attributedefinition_constructor_args():
    sig = inspect.signature(ExchangeFile_AttributeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_rif11a_exchangefile_identifiable_is_not_abstract():
    assert not inspect.isabstract(rif11a_ExchangeFile_Identifiable)


def test_rif11a_exchangefile_identifiable_constructor_exists():
    assert callable(rif11a_ExchangeFile_Identifiable.__init__)


def test_rif11a_exchangefile_identifiable_constructor_args():
    sig = inspect.signature(rif11a_ExchangeFile_Identifiable.__init__)
    params = list(sig.parameters.keys())
    assert "longName" in params, "Missing parameter 'longName'"
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "desc" in params, "Missing parameter 'desc'"
    assert "lastChange" in params, "Missing parameter 'lastChange'"

def test_rif11a_exchangefile_identifiable_has_longName():
    assert hasattr(rif11a_ExchangeFile_Identifiable, "longName")
    descriptor = None
    for klass in rif11a_ExchangeFile_Identifiable.__mro__:
        if "longName" in klass.__dict__:
            descriptor = klass.__dict__["longName"]
            break
    assert isinstance(descriptor, property)

def test_rif11a_exchangefile_identifiable_has_identifier():
    assert hasattr(rif11a_ExchangeFile_Identifiable, "identifier")
    descriptor = None
    for klass in rif11a_ExchangeFile_Identifiable.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)

def test_rif11a_exchangefile_identifiable_has_desc():
    assert hasattr(rif11a_ExchangeFile_Identifiable, "desc")
    descriptor = None
    for klass in rif11a_ExchangeFile_Identifiable.__mro__:
        if "desc" in klass.__dict__:
            descriptor = klass.__dict__["desc"]
            break
    assert isinstance(descriptor, property)

def test_rif11a_exchangefile_identifiable_has_lastChange():
    assert hasattr(rif11a_ExchangeFile_Identifiable, "lastChange")
    descriptor = None
    for klass in rif11a_ExchangeFile_Identifiable.__mro__:
        if "lastChange" in klass.__dict__:
            descriptor = klass.__dict__["lastChange"]
            break
    assert isinstance(descriptor, property)



def test_exchangefile_attributevalue_is_not_abstract():
    assert not inspect.isabstract(ExchangeFile_AttributeValue)


def test_exchangefile_attributevalue_constructor_exists():
    assert callable(ExchangeFile_AttributeValue.__init__)


def test_exchangefile_attributevalue_constructor_args():
    sig = inspect.signature(ExchangeFile_AttributeValue.__init__)
    params = list(sig.parameters.keys())



def test_exchangefile_spectype_is_not_abstract():
    assert not inspect.isabstract(ExchangeFile_SpecType)


def test_exchangefile_spectype_constructor_exists():
    assert callable(ExchangeFile_SpecType.__init__)


def test_exchangefile_spectype_constructor_args():
    sig = inspect.signature(ExchangeFile_SpecType.__init__)
    params = list(sig.parameters.keys())



def test_identifiable_is_not_abstract():
    assert not inspect.isabstract(Identifiable)


def test_identifiable_constructor_exists():
    assert callable(Identifiable.__init__)


def test_identifiable_constructor_args():
    sig = inspect.signature(Identifiable.__init__)
    params = list(sig.parameters.keys())



def test_rif11a_exchangefile_datatypedefinition_is_not_abstract():
    assert not inspect.isabstract(rif11a_ExchangeFile_DatatypeDefinition)


def test_rif11a_exchangefile_datatypedefinition_constructor_exists():
    assert callable(rif11a_ExchangeFile_DatatypeDefinition.__init__)


def test_rif11a_exchangefile_datatypedefinition_constructor_args():
    sig = inspect.signature(rif11a_ExchangeFile_DatatypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_rif11a_exchangefile_attributedefinition_is_not_abstract():
    assert not inspect.isabstract(rif11a_ExchangeFile_AttributeDefinition)


def test_rif11a_exchangefile_attributedefinition_constructor_exists():
    assert callable(rif11a_ExchangeFile_AttributeDefinition.__init__)


def test_rif11a_exchangefile_attributedefinition_constructor_args():
    sig = inspect.signature(rif11a_ExchangeFile_AttributeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_rif11a_exchangefile_spectype_is_not_abstract():
    assert not inspect.isabstract(rif11a_ExchangeFile_SpecType)


def test_rif11a_exchangefile_spectype_constructor_exists():
    assert callable(rif11a_ExchangeFile_SpecType.__init__)


def test_rif11a_exchangefile_spectype_constructor_args():
    sig = inspect.signature(rif11a_ExchangeFile_SpecType.__init__)
    params = list(sig.parameters.keys())



def test_rif11a_exchangefile_attributevalue_is_not_abstract():
    assert not inspect.isabstract(rif11a_ExchangeFile_AttributeValue)


def test_rif11a_exchangefile_attributevalue_constructor_exists():
    assert callable(rif11a_ExchangeFile_AttributeValue.__init__)


def test_rif11a_exchangefile_attributevalue_constructor_args():
    sig = inspect.signature(rif11a_ExchangeFile_AttributeValue.__init__)
    params = list(sig.parameters.keys())



def test_rif11a_exchangefile_accesspolicy_is_not_abstract():
    assert not inspect.isabstract(rif11a_ExchangeFile_AccessPolicy)


def test_rif11a_exchangefile_accesspolicy_constructor_exists():
    assert callable(rif11a_ExchangeFile_AccessPolicy.__init__)


def test_rif11a_exchangefile_accesspolicy_constructor_args():
    sig = inspect.signature(rif11a_ExchangeFile_AccessPolicy.__init__)
    params = list(sig.parameters.keys())
    assert "accessMode" in params, "Missing parameter 'accessMode'"

def test_rif11a_exchangefile_accesspolicy_has_accessMode():
    assert hasattr(rif11a_ExchangeFile_AccessPolicy, "accessMode")
    descriptor = None
    for klass in rif11a_ExchangeFile_AccessPolicy.__mro__:
        if "accessMode" in klass.__dict__:
            descriptor = klass.__dict__["accessMode"]
            break
    assert isinstance(descriptor, property)



def test_rif11a_exchangefile_enumvalue_is_not_abstract():
    assert not inspect.isabstract(rif11a_ExchangeFile_EnumValue)


def test_rif11a_exchangefile_enumvalue_constructor_exists():
    assert callable(rif11a_ExchangeFile_EnumValue.__init__)


def test_rif11a_exchangefile_enumvalue_constructor_args():
    sig = inspect.signature(rif11a_ExchangeFile_EnumValue.__init__)
    params = list(sig.parameters.keys())



def test_rif11a_exchangefile_specelementwithuserdefinedattributes_is_not_abstract():
    assert not inspect.isabstract(rif11a_ExchangeFile_SpecElementWithUserDefinedAttributes)


def test_rif11a_exchangefile_specelementwithuserdefinedattributes_constructor_exists():
    assert callable(rif11a_ExchangeFile_SpecElementWithUserDefinedAttributes.__init__)


def test_rif11a_exchangefile_specelementwithuserdefinedattributes_constructor_args():
    sig = inspect.signature(rif11a_ExchangeFile_SpecElementWithUserDefinedAttributes.__init__)
    params = list(sig.parameters.keys())



def test_exchangefile_spechierarchy_is_not_abstract():
    assert not inspect.isabstract(ExchangeFile_SpecHierarchy)


def test_exchangefile_spechierarchy_constructor_exists():
    assert callable(ExchangeFile_SpecHierarchy.__init__)


def test_exchangefile_spechierarchy_constructor_args():
    sig = inspect.signature(ExchangeFile_SpecHierarchy.__init__)
    params = list(sig.parameters.keys())



def test_exchangefile_specrelation_is_not_abstract():
    assert not inspect.isabstract(ExchangeFile_SpecRelation)


def test_exchangefile_specrelation_constructor_exists():
    assert callable(ExchangeFile_SpecRelation.__init__)


def test_exchangefile_specrelation_constructor_args():
    sig = inspect.signature(ExchangeFile_SpecRelation.__init__)
    params = list(sig.parameters.keys())



def test_rif11a_exchangefile_relationgroup_is_not_abstract():
    assert not inspect.isabstract(rif11a_ExchangeFile_RelationGroup)


def test_rif11a_exchangefile_relationgroup_constructor_exists():
    assert callable(rif11a_ExchangeFile_RelationGroup.__init__)


def test_rif11a_exchangefile_relationgroup_constructor_args():
    sig = inspect.signature(rif11a_ExchangeFile_RelationGroup.__init__)
    params = list(sig.parameters.keys())



def test_exchangefile_relationgroup_is_not_abstract():
    assert not inspect.isabstract(ExchangeFile_RelationGroup)


def test_exchangefile_relationgroup_constructor_exists():
    assert callable(ExchangeFile_RelationGroup.__init__)


def test_exchangefile_relationgroup_constructor_args():
    sig = inspect.signature(ExchangeFile_RelationGroup.__init__)
    params = list(sig.parameters.keys())



def test_exchangefile_specobject_is_not_abstract():
    assert not inspect.isabstract(ExchangeFile_SpecObject)


def test_exchangefile_specobject_constructor_exists():
    assert callable(ExchangeFile_SpecObject.__init__)


def test_exchangefile_specobject_constructor_args():
    sig = inspect.signature(ExchangeFile_SpecObject.__init__)
    params = list(sig.parameters.keys())



def test_rif11a_exchangefile_spechierarchy_is_not_abstract():
    assert not inspect.isabstract(rif11a_ExchangeFile_SpecHierarchy)


def test_rif11a_exchangefile_spechierarchy_constructor_exists():
    assert callable(rif11a_ExchangeFile_SpecHierarchy.__init__)


def test_rif11a_exchangefile_spechierarchy_constructor_args():
    sig = inspect.signature(rif11a_ExchangeFile_SpecHierarchy.__init__)
    params = list(sig.parameters.keys())



def test_specelementwithuserdefinedattributes_is_not_abstract():
    assert not inspect.isabstract(SpecElementWithUserDefinedAttributes)


def test_specelementwithuserdefinedattributes_constructor_exists():
    assert callable(SpecElementWithUserDefinedAttributes.__init__)


def test_specelementwithuserdefinedattributes_constructor_args():
    sig = inspect.signature(SpecElementWithUserDefinedAttributes.__init__)
    params = list(sig.parameters.keys())



def test_rif11a_exchangefile_specgroup_is_not_abstract():
    assert not inspect.isabstract(rif11a_ExchangeFile_SpecGroup)


def test_rif11a_exchangefile_specgroup_constructor_exists():
    assert callable(rif11a_ExchangeFile_SpecGroup.__init__)


def test_rif11a_exchangefile_specgroup_constructor_args():
    sig = inspect.signature(rif11a_ExchangeFile_SpecGroup.__init__)
    params = list(sig.parameters.keys())



def test_rif11a_exchangefile_specrelation_is_not_abstract():
    assert not inspect.isabstract(rif11a_ExchangeFile_SpecRelation)


def test_rif11a_exchangefile_specrelation_constructor_exists():
    assert callable(rif11a_ExchangeFile_SpecRelation.__init__)


def test_rif11a_exchangefile_specrelation_constructor_args():
    sig = inspect.signature(rif11a_ExchangeFile_SpecRelation.__init__)
    params = list(sig.parameters.keys())



def test_rif11a_exchangefile_specobject_is_not_abstract():
    assert not inspect.isabstract(rif11a_ExchangeFile_SpecObject)


def test_rif11a_exchangefile_specobject_constructor_exists():
    assert callable(rif11a_ExchangeFile_SpecObject.__init__)


def test_rif11a_exchangefile_specobject_constructor_args():
    sig = inspect.signature(rif11a_ExchangeFile_SpecObject.__init__)
    params = list(sig.parameters.keys())



def test_rif11a_exchangefile_spechierarchyroot_is_not_abstract():
    assert not inspect.isabstract(rif11a_ExchangeFile_SpecHierarchyRoot)


def test_rif11a_exchangefile_spechierarchyroot_constructor_exists():
    assert callable(rif11a_ExchangeFile_SpecHierarchyRoot.__init__)


def test_rif11a_exchangefile_spechierarchyroot_constructor_args():
    sig = inspect.signature(rif11a_ExchangeFile_SpecHierarchyRoot.__init__)
    params = list(sig.parameters.keys())

def test_datatypedefinitiondateformatenum_exists():
    # Check that the Enumeration exists
    assert DatatypeDefinitionDateFormatEnum is not None

def test_datatypedefinitiondateformatenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DatatypeDefinitionDateFormatEnum]
    expected_literals = [
        "CUSTOM",
        "W3C",
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
        "EDIT",
        "DELETE",
        "CREATE",
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
rif11a_DataTypes_BinaryContent_strategy = st.builds(
    rif11a_DataTypes_BinaryContent,
)
ExchangeFile_AccessPolicy_strategy = st.builds(
    ExchangeFile_AccessPolicy,
)
rif11a_DataTypes_XhtmlContent_strategy = st.builds(
    rif11a_DataTypes_XhtmlContent,
)
rif11a_DataTypes_XmlContent_strategy = st.builds(
    rif11a_DataTypes_XmlContent,
)
DatatypeDefinitionSimple_strategy = st.builds(
    DatatypeDefinitionSimple,
)
rif11a_ExchangeFile_DatatypeDefinitionDate_strategy = st.builds(
    rif11a_ExchangeFile_DatatypeDefinitionDate,
    format=
        safe_text
)
rif11a_ExchangeFile_DatatypeDefinitionBoolean_strategy = st.builds(
    rif11a_ExchangeFile_DatatypeDefinitionBoolean,
)
DatatypeDefinitionComplex_strategy = st.builds(
    DatatypeDefinitionComplex,
)
rif11a_ExchangeFile_DatatypeDefinitionDocument_strategy = st.builds(
    rif11a_ExchangeFile_DatatypeDefinitionDocument,
)
rif11a_ExchangeFile_DatatypeDefinitionBinaryFile_strategy = st.builds(
    rif11a_ExchangeFile_DatatypeDefinitionBinaryFile,
    mimeType=
        safe_text,
    application=
        safe_text,
    filenameSuffix=
        safe_text,
    formatName=
        safe_text
)
DataTypes_XmlContent_strategy = st.builds(
    DataTypes_XmlContent,
)
DataTypes_BinaryContent_strategy = st.builds(
    DataTypes_BinaryContent,
)
rif11a_ExchangeFile_RIF_strategy = st.builds(
    rif11a_ExchangeFile_RIF,
    author=
        safe_text,
    comment=
        safe_text,
    version=
        safe_text,
    creationTime=
        safe_text,
    title=
        safe_text,
    identifier=
        safe_text,
    sourceToolId=
        safe_text,
    countryCode=
        safe_text
)
rif11a_ExchangeFile_DatatypeDefinitionXmlData_strategy = st.builds(
    rif11a_ExchangeFile_DatatypeDefinitionXmlData,
    schemaLocation=
        safe_text,
    nameSpaceURI=
        safe_text
)
rif11a_ExchangeFile_DatatypeDefinitionString_strategy = st.builds(
    rif11a_ExchangeFile_DatatypeDefinitionString,
    maxLength=
        safe_text
)
rif11a_ExchangeFile_DatatypeDefinitionReal_strategy = st.builds(
    rif11a_ExchangeFile_DatatypeDefinitionReal,
    max=
        safe_text,
    min=
        safe_text,
    accuracy=
        safe_text
)
rif11a_ExchangeFile_DatatypeDefinitionInteger_strategy = st.builds(
    rif11a_ExchangeFile_DatatypeDefinitionInteger,
    min=
        safe_text,
    max=
        safe_text
)
ExchangeFile_AttributeDefinitionEnumeration_strategy = st.builds(
    ExchangeFile_AttributeDefinitionEnumeration,
)
rif11a_ExchangeFile_EmbeddedValue_strategy = st.builds(
    rif11a_ExchangeFile_EmbeddedValue,
    key=
        safe_text,
    otherContent=
        safe_text
)
ExchangeFile_EmbeddedValue_strategy = st.builds(
    ExchangeFile_EmbeddedValue,
)
ExchangeFile_EnumValue_strategy = st.builds(
    ExchangeFile_EnumValue,
)
ExchangeFile_AttributeValueEnumeration_strategy = st.builds(
    ExchangeFile_AttributeValueEnumeration,
)
ExchangeFile_DatatypeDefinitionEnumeration_strategy = st.builds(
    ExchangeFile_DatatypeDefinitionEnumeration,
)
DataTypes_XhtmlContent_strategy = st.builds(
    DataTypes_XhtmlContent,
)
ExchangeFile_AttributeDefinitionComplex_strategy = st.builds(
    ExchangeFile_AttributeDefinitionComplex,
)
AttributeValueComplex_strategy = st.builds(
    AttributeValueComplex,
)
rif11a_ExchangeFile_AttributeValueEmbeddedFile_strategy = st.builds(
    rif11a_ExchangeFile_AttributeValueEmbeddedFile,
)
rif11a_ExchangeFile_AttributeValueXmlData_strategy = st.builds(
    rif11a_ExchangeFile_AttributeValueXmlData,
)
rif11a_ExchangeFile_AttributeValueFileReference_strategy = st.builds(
    rif11a_ExchangeFile_AttributeValueFileReference,
    pathToFile=
        safe_text
)
rif11a_ExchangeFile_AttributeValueEmbeddedDocument_strategy = st.builds(
    rif11a_ExchangeFile_AttributeValueEmbeddedDocument,
)
ExchangeFile_AttributeDefinitionSimple_strategy = st.builds(
    ExchangeFile_AttributeDefinitionSimple,
)
ExchangeFile_AttributeValueSimple_strategy = st.builds(
    ExchangeFile_AttributeValueSimple,
)
ExchangeFile_DatatypeDefinitionSimple_strategy = st.builds(
    ExchangeFile_DatatypeDefinitionSimple,
)
ExchangeFile_DatatypeDefinition_strategy = st.builds(
    ExchangeFile_DatatypeDefinition,
)
ExchangeFile_SpecGroup_strategy = st.builds(
    ExchangeFile_SpecGroup,
)
AttributeValue_strategy = st.builds(
    AttributeValue,
)
rif11a_ExchangeFile_AttributeValueSimple_strategy = st.builds(
    rif11a_ExchangeFile_AttributeValueSimple,
    theValue=
        safe_text
)
rif11a_ExchangeFile_AttributeValueEnumeration_strategy = st.builds(
    rif11a_ExchangeFile_AttributeValueEnumeration,
)
rif11a_ExchangeFile_AttributeValueComplex_strategy = st.builds(
    rif11a_ExchangeFile_AttributeValueComplex,
)
DatatypeDefinition_strategy = st.builds(
    DatatypeDefinition,
)
rif11a_ExchangeFile_DatatypeDefinitionSimple_strategy = st.builds(
    rif11a_ExchangeFile_DatatypeDefinitionSimple,
)
rif11a_ExchangeFile_DatatypeDefinitionEnumeration_strategy = st.builds(
    rif11a_ExchangeFile_DatatypeDefinitionEnumeration,
)
rif11a_ExchangeFile_DatatypeDefinitionComplex_strategy = st.builds(
    rif11a_ExchangeFile_DatatypeDefinitionComplex,
    embedded=
        safe_text
)
ExchangeFile_AttributeValueComplex_strategy = st.builds(
    ExchangeFile_AttributeValueComplex,
)
ExchangeFile_DatatypeDefinitionComplex_strategy = st.builds(
    ExchangeFile_DatatypeDefinitionComplex,
)
AttributeDefinition_strategy = st.builds(
    AttributeDefinition,
)
rif11a_ExchangeFile_AttributeDefinitionSimple_strategy = st.builds(
    rif11a_ExchangeFile_AttributeDefinitionSimple,
)
rif11a_ExchangeFile_AttributeDefinitionEnumeration_strategy = st.builds(
    rif11a_ExchangeFile_AttributeDefinitionEnumeration,
    multiValued=
        safe_text
)
rif11a_ExchangeFile_AttributeDefinitionComplex_strategy = st.builds(
    rif11a_ExchangeFile_AttributeDefinitionComplex,
)
ExchangeFile_SpecHierarchyRoot_strategy = st.builds(
    ExchangeFile_SpecHierarchyRoot,
)
ExchangeFile_AttributeDefinition_strategy = st.builds(
    ExchangeFile_AttributeDefinition,
)
rif11a_ExchangeFile_Identifiable_strategy = st.builds(
    rif11a_ExchangeFile_Identifiable,
    longName=
        safe_text,
    identifier=
        safe_text,
    desc=
        safe_text,
    lastChange=
        safe_text
)
ExchangeFile_AttributeValue_strategy = st.builds(
    ExchangeFile_AttributeValue,
)
ExchangeFile_SpecType_strategy = st.builds(
    ExchangeFile_SpecType,
)
Identifiable_strategy = st.builds(
    Identifiable,
)
rif11a_ExchangeFile_DatatypeDefinition_strategy = st.builds(
    rif11a_ExchangeFile_DatatypeDefinition,
)
rif11a_ExchangeFile_AttributeDefinition_strategy = st.builds(
    rif11a_ExchangeFile_AttributeDefinition,
)
rif11a_ExchangeFile_SpecType_strategy = st.builds(
    rif11a_ExchangeFile_SpecType,
)
rif11a_ExchangeFile_AttributeValue_strategy = st.builds(
    rif11a_ExchangeFile_AttributeValue,
)
rif11a_ExchangeFile_AccessPolicy_strategy = st.builds(
    rif11a_ExchangeFile_AccessPolicy,
    accessMode=
        safe_text
)
rif11a_ExchangeFile_EnumValue_strategy = st.builds(
    rif11a_ExchangeFile_EnumValue,
)
rif11a_ExchangeFile_SpecElementWithUserDefinedAttributes_strategy = st.builds(
    rif11a_ExchangeFile_SpecElementWithUserDefinedAttributes,
)
ExchangeFile_SpecHierarchy_strategy = st.builds(
    ExchangeFile_SpecHierarchy,
)
ExchangeFile_SpecRelation_strategy = st.builds(
    ExchangeFile_SpecRelation,
)
rif11a_ExchangeFile_RelationGroup_strategy = st.builds(
    rif11a_ExchangeFile_RelationGroup,
)
ExchangeFile_RelationGroup_strategy = st.builds(
    ExchangeFile_RelationGroup,
)
ExchangeFile_SpecObject_strategy = st.builds(
    ExchangeFile_SpecObject,
)
rif11a_ExchangeFile_SpecHierarchy_strategy = st.builds(
    rif11a_ExchangeFile_SpecHierarchy,
)
SpecElementWithUserDefinedAttributes_strategy = st.builds(
    SpecElementWithUserDefinedAttributes,
)
rif11a_ExchangeFile_SpecGroup_strategy = st.builds(
    rif11a_ExchangeFile_SpecGroup,
)
rif11a_ExchangeFile_SpecRelation_strategy = st.builds(
    rif11a_ExchangeFile_SpecRelation,
)
rif11a_ExchangeFile_SpecObject_strategy = st.builds(
    rif11a_ExchangeFile_SpecObject,
)
rif11a_ExchangeFile_SpecHierarchyRoot_strategy = st.builds(
    rif11a_ExchangeFile_SpecHierarchyRoot,
)

@given(instance=rif11a_DataTypes_BinaryContent_strategy)
@settings(max_examples=50)
def test_rif11a_datatypes_binarycontent_instantiation(instance):
    assert isinstance(instance, rif11a_DataTypes_BinaryContent)

@given(instance=ExchangeFile_AccessPolicy_strategy)
@settings(max_examples=50)
def test_exchangefile_accesspolicy_instantiation(instance):
    assert isinstance(instance, ExchangeFile_AccessPolicy)

@given(instance=rif11a_DataTypes_XhtmlContent_strategy)
@settings(max_examples=50)
def test_rif11a_datatypes_xhtmlcontent_instantiation(instance):
    assert isinstance(instance, rif11a_DataTypes_XhtmlContent)

@given(instance=rif11a_DataTypes_XmlContent_strategy)
@settings(max_examples=50)
def test_rif11a_datatypes_xmlcontent_instantiation(instance):
    assert isinstance(instance, rif11a_DataTypes_XmlContent)

@given(instance=DatatypeDefinitionSimple_strategy)
@settings(max_examples=50)
def test_datatypedefinitionsimple_instantiation(instance):
    assert isinstance(instance, DatatypeDefinitionSimple)

@given(instance=rif11a_ExchangeFile_DatatypeDefinitionDate_strategy)
@settings(max_examples=50)
def test_rif11a_exchangefile_datatypedefinitiondate_instantiation(instance):
    assert isinstance(instance, rif11a_ExchangeFile_DatatypeDefinitionDate)



@given(instance=rif11a_ExchangeFile_DatatypeDefinitionDate_strategy)
def test_rif11a_exchangefile_datatypedefinitiondate_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original

@given(instance=rif11a_ExchangeFile_DatatypeDefinitionBoolean_strategy)
@settings(max_examples=50)
def test_rif11a_exchangefile_datatypedefinitionboolean_instantiation(instance):
    assert isinstance(instance, rif11a_ExchangeFile_DatatypeDefinitionBoolean)

@given(instance=DatatypeDefinitionComplex_strategy)
@settings(max_examples=50)
def test_datatypedefinitioncomplex_instantiation(instance):
    assert isinstance(instance, DatatypeDefinitionComplex)

@given(instance=rif11a_ExchangeFile_DatatypeDefinitionDocument_strategy)
@settings(max_examples=50)
def test_rif11a_exchangefile_datatypedefinitiondocument_instantiation(instance):
    assert isinstance(instance, rif11a_ExchangeFile_DatatypeDefinitionDocument)

@given(instance=rif11a_ExchangeFile_DatatypeDefinitionBinaryFile_strategy)
@settings(max_examples=50)
def test_rif11a_exchangefile_datatypedefinitionbinaryfile_instantiation(instance):
    assert isinstance(instance, rif11a_ExchangeFile_DatatypeDefinitionBinaryFile)



@given(instance=rif11a_ExchangeFile_DatatypeDefinitionBinaryFile_strategy)
def test_rif11a_exchangefile_datatypedefinitionbinaryfile_mimeType_setter(instance):
    original = instance.mimeType
    instance.mimeType = original
    assert instance.mimeType == original



@given(instance=rif11a_ExchangeFile_DatatypeDefinitionBinaryFile_strategy)
def test_rif11a_exchangefile_datatypedefinitionbinaryfile_application_setter(instance):
    original = instance.application
    instance.application = original
    assert instance.application == original



@given(instance=rif11a_ExchangeFile_DatatypeDefinitionBinaryFile_strategy)
def test_rif11a_exchangefile_datatypedefinitionbinaryfile_filenameSuffix_setter(instance):
    original = instance.filenameSuffix
    instance.filenameSuffix = original
    assert instance.filenameSuffix == original



@given(instance=rif11a_ExchangeFile_DatatypeDefinitionBinaryFile_strategy)
def test_rif11a_exchangefile_datatypedefinitionbinaryfile_formatName_setter(instance):
    original = instance.formatName
    instance.formatName = original
    assert instance.formatName == original

@given(instance=DataTypes_XmlContent_strategy)
@settings(max_examples=50)
def test_datatypes_xmlcontent_instantiation(instance):
    assert isinstance(instance, DataTypes_XmlContent)

@given(instance=DataTypes_BinaryContent_strategy)
@settings(max_examples=50)
def test_datatypes_binarycontent_instantiation(instance):
    assert isinstance(instance, DataTypes_BinaryContent)

@given(instance=rif11a_ExchangeFile_RIF_strategy)
@settings(max_examples=50)
def test_rif11a_exchangefile_rif_instantiation(instance):
    assert isinstance(instance, rif11a_ExchangeFile_RIF)



@given(instance=rif11a_ExchangeFile_RIF_strategy)
def test_rif11a_exchangefile_rif_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=rif11a_ExchangeFile_RIF_strategy)
def test_rif11a_exchangefile_rif_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=rif11a_ExchangeFile_RIF_strategy)
def test_rif11a_exchangefile_rif_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=rif11a_ExchangeFile_RIF_strategy)
def test_rif11a_exchangefile_rif_creationTime_setter(instance):
    original = instance.creationTime
    instance.creationTime = original
    assert instance.creationTime == original



@given(instance=rif11a_ExchangeFile_RIF_strategy)
def test_rif11a_exchangefile_rif_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=rif11a_ExchangeFile_RIF_strategy)
def test_rif11a_exchangefile_rif_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original



@given(instance=rif11a_ExchangeFile_RIF_strategy)
def test_rif11a_exchangefile_rif_sourceToolId_setter(instance):
    original = instance.sourceToolId
    instance.sourceToolId = original
    assert instance.sourceToolId == original



@given(instance=rif11a_ExchangeFile_RIF_strategy)
def test_rif11a_exchangefile_rif_countryCode_setter(instance):
    original = instance.countryCode
    instance.countryCode = original
    assert instance.countryCode == original

@given(instance=rif11a_ExchangeFile_DatatypeDefinitionXmlData_strategy)
@settings(max_examples=50)
def test_rif11a_exchangefile_datatypedefinitionxmldata_instantiation(instance):
    assert isinstance(instance, rif11a_ExchangeFile_DatatypeDefinitionXmlData)



@given(instance=rif11a_ExchangeFile_DatatypeDefinitionXmlData_strategy)
def test_rif11a_exchangefile_datatypedefinitionxmldata_schemaLocation_setter(instance):
    original = instance.schemaLocation
    instance.schemaLocation = original
    assert instance.schemaLocation == original



@given(instance=rif11a_ExchangeFile_DatatypeDefinitionXmlData_strategy)
def test_rif11a_exchangefile_datatypedefinitionxmldata_nameSpaceURI_setter(instance):
    original = instance.nameSpaceURI
    instance.nameSpaceURI = original
    assert instance.nameSpaceURI == original

@given(instance=rif11a_ExchangeFile_DatatypeDefinitionString_strategy)
@settings(max_examples=50)
def test_rif11a_exchangefile_datatypedefinitionstring_instantiation(instance):
    assert isinstance(instance, rif11a_ExchangeFile_DatatypeDefinitionString)



@given(instance=rif11a_ExchangeFile_DatatypeDefinitionString_strategy)
def test_rif11a_exchangefile_datatypedefinitionstring_maxLength_setter(instance):
    original = instance.maxLength
    instance.maxLength = original
    assert instance.maxLength == original

@given(instance=rif11a_ExchangeFile_DatatypeDefinitionReal_strategy)
@settings(max_examples=50)
def test_rif11a_exchangefile_datatypedefinitionreal_instantiation(instance):
    assert isinstance(instance, rif11a_ExchangeFile_DatatypeDefinitionReal)



@given(instance=rif11a_ExchangeFile_DatatypeDefinitionReal_strategy)
def test_rif11a_exchangefile_datatypedefinitionreal_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original



@given(instance=rif11a_ExchangeFile_DatatypeDefinitionReal_strategy)
def test_rif11a_exchangefile_datatypedefinitionreal_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original



@given(instance=rif11a_ExchangeFile_DatatypeDefinitionReal_strategy)
def test_rif11a_exchangefile_datatypedefinitionreal_accuracy_setter(instance):
    original = instance.accuracy
    instance.accuracy = original
    assert instance.accuracy == original

@given(instance=rif11a_ExchangeFile_DatatypeDefinitionInteger_strategy)
@settings(max_examples=50)
def test_rif11a_exchangefile_datatypedefinitioninteger_instantiation(instance):
    assert isinstance(instance, rif11a_ExchangeFile_DatatypeDefinitionInteger)



@given(instance=rif11a_ExchangeFile_DatatypeDefinitionInteger_strategy)
def test_rif11a_exchangefile_datatypedefinitioninteger_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original



@given(instance=rif11a_ExchangeFile_DatatypeDefinitionInteger_strategy)
def test_rif11a_exchangefile_datatypedefinitioninteger_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=ExchangeFile_AttributeDefinitionEnumeration_strategy)
@settings(max_examples=50)
def test_exchangefile_attributedefinitionenumeration_instantiation(instance):
    assert isinstance(instance, ExchangeFile_AttributeDefinitionEnumeration)

@given(instance=rif11a_ExchangeFile_EmbeddedValue_strategy)
@settings(max_examples=50)
def test_rif11a_exchangefile_embeddedvalue_instantiation(instance):
    assert isinstance(instance, rif11a_ExchangeFile_EmbeddedValue)



@given(instance=rif11a_ExchangeFile_EmbeddedValue_strategy)
def test_rif11a_exchangefile_embeddedvalue_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=rif11a_ExchangeFile_EmbeddedValue_strategy)
def test_rif11a_exchangefile_embeddedvalue_otherContent_setter(instance):
    original = instance.otherContent
    instance.otherContent = original
    assert instance.otherContent == original

@given(instance=ExchangeFile_EmbeddedValue_strategy)
@settings(max_examples=50)
def test_exchangefile_embeddedvalue_instantiation(instance):
    assert isinstance(instance, ExchangeFile_EmbeddedValue)

@given(instance=ExchangeFile_EnumValue_strategy)
@settings(max_examples=50)
def test_exchangefile_enumvalue_instantiation(instance):
    assert isinstance(instance, ExchangeFile_EnumValue)

@given(instance=ExchangeFile_AttributeValueEnumeration_strategy)
@settings(max_examples=50)
def test_exchangefile_attributevalueenumeration_instantiation(instance):
    assert isinstance(instance, ExchangeFile_AttributeValueEnumeration)

@given(instance=ExchangeFile_DatatypeDefinitionEnumeration_strategy)
@settings(max_examples=50)
def test_exchangefile_datatypedefinitionenumeration_instantiation(instance):
    assert isinstance(instance, ExchangeFile_DatatypeDefinitionEnumeration)

@given(instance=DataTypes_XhtmlContent_strategy)
@settings(max_examples=50)
def test_datatypes_xhtmlcontent_instantiation(instance):
    assert isinstance(instance, DataTypes_XhtmlContent)

@given(instance=ExchangeFile_AttributeDefinitionComplex_strategy)
@settings(max_examples=50)
def test_exchangefile_attributedefinitioncomplex_instantiation(instance):
    assert isinstance(instance, ExchangeFile_AttributeDefinitionComplex)

@given(instance=AttributeValueComplex_strategy)
@settings(max_examples=50)
def test_attributevaluecomplex_instantiation(instance):
    assert isinstance(instance, AttributeValueComplex)

@given(instance=rif11a_ExchangeFile_AttributeValueEmbeddedFile_strategy)
@settings(max_examples=50)
def test_rif11a_exchangefile_attributevalueembeddedfile_instantiation(instance):
    assert isinstance(instance, rif11a_ExchangeFile_AttributeValueEmbeddedFile)

@given(instance=rif11a_ExchangeFile_AttributeValueXmlData_strategy)
@settings(max_examples=50)
def test_rif11a_exchangefile_attributevaluexmldata_instantiation(instance):
    assert isinstance(instance, rif11a_ExchangeFile_AttributeValueXmlData)

@given(instance=rif11a_ExchangeFile_AttributeValueFileReference_strategy)
@settings(max_examples=50)
def test_rif11a_exchangefile_attributevaluefilereference_instantiation(instance):
    assert isinstance(instance, rif11a_ExchangeFile_AttributeValueFileReference)



@given(instance=rif11a_ExchangeFile_AttributeValueFileReference_strategy)
def test_rif11a_exchangefile_attributevaluefilereference_pathToFile_setter(instance):
    original = instance.pathToFile
    instance.pathToFile = original
    assert instance.pathToFile == original

@given(instance=rif11a_ExchangeFile_AttributeValueEmbeddedDocument_strategy)
@settings(max_examples=50)
def test_rif11a_exchangefile_attributevalueembeddeddocument_instantiation(instance):
    assert isinstance(instance, rif11a_ExchangeFile_AttributeValueEmbeddedDocument)

@given(instance=ExchangeFile_AttributeDefinitionSimple_strategy)
@settings(max_examples=50)
def test_exchangefile_attributedefinitionsimple_instantiation(instance):
    assert isinstance(instance, ExchangeFile_AttributeDefinitionSimple)

@given(instance=ExchangeFile_AttributeValueSimple_strategy)
@settings(max_examples=50)
def test_exchangefile_attributevaluesimple_instantiation(instance):
    assert isinstance(instance, ExchangeFile_AttributeValueSimple)

@given(instance=ExchangeFile_DatatypeDefinitionSimple_strategy)
@settings(max_examples=50)
def test_exchangefile_datatypedefinitionsimple_instantiation(instance):
    assert isinstance(instance, ExchangeFile_DatatypeDefinitionSimple)

@given(instance=ExchangeFile_DatatypeDefinition_strategy)
@settings(max_examples=50)
def test_exchangefile_datatypedefinition_instantiation(instance):
    assert isinstance(instance, ExchangeFile_DatatypeDefinition)

@given(instance=ExchangeFile_SpecGroup_strategy)
@settings(max_examples=50)
def test_exchangefile_specgroup_instantiation(instance):
    assert isinstance(instance, ExchangeFile_SpecGroup)

@given(instance=AttributeValue_strategy)
@settings(max_examples=50)
def test_attributevalue_instantiation(instance):
    assert isinstance(instance, AttributeValue)

@given(instance=rif11a_ExchangeFile_AttributeValueSimple_strategy)
@settings(max_examples=50)
def test_rif11a_exchangefile_attributevaluesimple_instantiation(instance):
    assert isinstance(instance, rif11a_ExchangeFile_AttributeValueSimple)



@given(instance=rif11a_ExchangeFile_AttributeValueSimple_strategy)
def test_rif11a_exchangefile_attributevaluesimple_theValue_setter(instance):
    original = instance.theValue
    instance.theValue = original
    assert instance.theValue == original

@given(instance=rif11a_ExchangeFile_AttributeValueEnumeration_strategy)
@settings(max_examples=50)
def test_rif11a_exchangefile_attributevalueenumeration_instantiation(instance):
    assert isinstance(instance, rif11a_ExchangeFile_AttributeValueEnumeration)

@given(instance=rif11a_ExchangeFile_AttributeValueComplex_strategy)
@settings(max_examples=50)
def test_rif11a_exchangefile_attributevaluecomplex_instantiation(instance):
    assert isinstance(instance, rif11a_ExchangeFile_AttributeValueComplex)

@given(instance=DatatypeDefinition_strategy)
@settings(max_examples=50)
def test_datatypedefinition_instantiation(instance):
    assert isinstance(instance, DatatypeDefinition)

@given(instance=rif11a_ExchangeFile_DatatypeDefinitionSimple_strategy)
@settings(max_examples=50)
def test_rif11a_exchangefile_datatypedefinitionsimple_instantiation(instance):
    assert isinstance(instance, rif11a_ExchangeFile_DatatypeDefinitionSimple)

@given(instance=rif11a_ExchangeFile_DatatypeDefinitionEnumeration_strategy)
@settings(max_examples=50)
def test_rif11a_exchangefile_datatypedefinitionenumeration_instantiation(instance):
    assert isinstance(instance, rif11a_ExchangeFile_DatatypeDefinitionEnumeration)

@given(instance=rif11a_ExchangeFile_DatatypeDefinitionComplex_strategy)
@settings(max_examples=50)
def test_rif11a_exchangefile_datatypedefinitioncomplex_instantiation(instance):
    assert isinstance(instance, rif11a_ExchangeFile_DatatypeDefinitionComplex)



@given(instance=rif11a_ExchangeFile_DatatypeDefinitionComplex_strategy)
def test_rif11a_exchangefile_datatypedefinitioncomplex_embedded_setter(instance):
    original = instance.embedded
    instance.embedded = original
    assert instance.embedded == original

@given(instance=ExchangeFile_AttributeValueComplex_strategy)
@settings(max_examples=50)
def test_exchangefile_attributevaluecomplex_instantiation(instance):
    assert isinstance(instance, ExchangeFile_AttributeValueComplex)

@given(instance=ExchangeFile_DatatypeDefinitionComplex_strategy)
@settings(max_examples=50)
def test_exchangefile_datatypedefinitioncomplex_instantiation(instance):
    assert isinstance(instance, ExchangeFile_DatatypeDefinitionComplex)

@given(instance=AttributeDefinition_strategy)
@settings(max_examples=50)
def test_attributedefinition_instantiation(instance):
    assert isinstance(instance, AttributeDefinition)

@given(instance=rif11a_ExchangeFile_AttributeDefinitionSimple_strategy)
@settings(max_examples=50)
def test_rif11a_exchangefile_attributedefinitionsimple_instantiation(instance):
    assert isinstance(instance, rif11a_ExchangeFile_AttributeDefinitionSimple)

@given(instance=rif11a_ExchangeFile_AttributeDefinitionEnumeration_strategy)
@settings(max_examples=50)
def test_rif11a_exchangefile_attributedefinitionenumeration_instantiation(instance):
    assert isinstance(instance, rif11a_ExchangeFile_AttributeDefinitionEnumeration)



@given(instance=rif11a_ExchangeFile_AttributeDefinitionEnumeration_strategy)
def test_rif11a_exchangefile_attributedefinitionenumeration_multiValued_setter(instance):
    original = instance.multiValued
    instance.multiValued = original
    assert instance.multiValued == original

@given(instance=rif11a_ExchangeFile_AttributeDefinitionComplex_strategy)
@settings(max_examples=50)
def test_rif11a_exchangefile_attributedefinitioncomplex_instantiation(instance):
    assert isinstance(instance, rif11a_ExchangeFile_AttributeDefinitionComplex)

@given(instance=ExchangeFile_SpecHierarchyRoot_strategy)
@settings(max_examples=50)
def test_exchangefile_spechierarchyroot_instantiation(instance):
    assert isinstance(instance, ExchangeFile_SpecHierarchyRoot)

@given(instance=ExchangeFile_AttributeDefinition_strategy)
@settings(max_examples=50)
def test_exchangefile_attributedefinition_instantiation(instance):
    assert isinstance(instance, ExchangeFile_AttributeDefinition)

@given(instance=rif11a_ExchangeFile_Identifiable_strategy)
@settings(max_examples=50)
def test_rif11a_exchangefile_identifiable_instantiation(instance):
    assert isinstance(instance, rif11a_ExchangeFile_Identifiable)



@given(instance=rif11a_ExchangeFile_Identifiable_strategy)
def test_rif11a_exchangefile_identifiable_longName_setter(instance):
    original = instance.longName
    instance.longName = original
    assert instance.longName == original



@given(instance=rif11a_ExchangeFile_Identifiable_strategy)
def test_rif11a_exchangefile_identifiable_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original



@given(instance=rif11a_ExchangeFile_Identifiable_strategy)
def test_rif11a_exchangefile_identifiable_desc_setter(instance):
    original = instance.desc
    instance.desc = original
    assert instance.desc == original



@given(instance=rif11a_ExchangeFile_Identifiable_strategy)
def test_rif11a_exchangefile_identifiable_lastChange_setter(instance):
    original = instance.lastChange
    instance.lastChange = original
    assert instance.lastChange == original

@given(instance=ExchangeFile_AttributeValue_strategy)
@settings(max_examples=50)
def test_exchangefile_attributevalue_instantiation(instance):
    assert isinstance(instance, ExchangeFile_AttributeValue)

@given(instance=ExchangeFile_SpecType_strategy)
@settings(max_examples=50)
def test_exchangefile_spectype_instantiation(instance):
    assert isinstance(instance, ExchangeFile_SpecType)

@given(instance=Identifiable_strategy)
@settings(max_examples=50)
def test_identifiable_instantiation(instance):
    assert isinstance(instance, Identifiable)

@given(instance=rif11a_ExchangeFile_DatatypeDefinition_strategy)
@settings(max_examples=50)
def test_rif11a_exchangefile_datatypedefinition_instantiation(instance):
    assert isinstance(instance, rif11a_ExchangeFile_DatatypeDefinition)

@given(instance=rif11a_ExchangeFile_AttributeDefinition_strategy)
@settings(max_examples=50)
def test_rif11a_exchangefile_attributedefinition_instantiation(instance):
    assert isinstance(instance, rif11a_ExchangeFile_AttributeDefinition)

@given(instance=rif11a_ExchangeFile_SpecType_strategy)
@settings(max_examples=50)
def test_rif11a_exchangefile_spectype_instantiation(instance):
    assert isinstance(instance, rif11a_ExchangeFile_SpecType)

@given(instance=rif11a_ExchangeFile_AttributeValue_strategy)
@settings(max_examples=50)
def test_rif11a_exchangefile_attributevalue_instantiation(instance):
    assert isinstance(instance, rif11a_ExchangeFile_AttributeValue)

@given(instance=rif11a_ExchangeFile_AccessPolicy_strategy)
@settings(max_examples=50)
def test_rif11a_exchangefile_accesspolicy_instantiation(instance):
    assert isinstance(instance, rif11a_ExchangeFile_AccessPolicy)



@given(instance=rif11a_ExchangeFile_AccessPolicy_strategy)
def test_rif11a_exchangefile_accesspolicy_accessMode_setter(instance):
    original = instance.accessMode
    instance.accessMode = original
    assert instance.accessMode == original

@given(instance=rif11a_ExchangeFile_EnumValue_strategy)
@settings(max_examples=50)
def test_rif11a_exchangefile_enumvalue_instantiation(instance):
    assert isinstance(instance, rif11a_ExchangeFile_EnumValue)

@given(instance=rif11a_ExchangeFile_SpecElementWithUserDefinedAttributes_strategy)
@settings(max_examples=50)
def test_rif11a_exchangefile_specelementwithuserdefinedattributes_instantiation(instance):
    assert isinstance(instance, rif11a_ExchangeFile_SpecElementWithUserDefinedAttributes)

@given(instance=ExchangeFile_SpecHierarchy_strategy)
@settings(max_examples=50)
def test_exchangefile_spechierarchy_instantiation(instance):
    assert isinstance(instance, ExchangeFile_SpecHierarchy)

@given(instance=ExchangeFile_SpecRelation_strategy)
@settings(max_examples=50)
def test_exchangefile_specrelation_instantiation(instance):
    assert isinstance(instance, ExchangeFile_SpecRelation)

@given(instance=rif11a_ExchangeFile_RelationGroup_strategy)
@settings(max_examples=50)
def test_rif11a_exchangefile_relationgroup_instantiation(instance):
    assert isinstance(instance, rif11a_ExchangeFile_RelationGroup)

@given(instance=ExchangeFile_RelationGroup_strategy)
@settings(max_examples=50)
def test_exchangefile_relationgroup_instantiation(instance):
    assert isinstance(instance, ExchangeFile_RelationGroup)

@given(instance=ExchangeFile_SpecObject_strategy)
@settings(max_examples=50)
def test_exchangefile_specobject_instantiation(instance):
    assert isinstance(instance, ExchangeFile_SpecObject)

@given(instance=rif11a_ExchangeFile_SpecHierarchy_strategy)
@settings(max_examples=50)
def test_rif11a_exchangefile_spechierarchy_instantiation(instance):
    assert isinstance(instance, rif11a_ExchangeFile_SpecHierarchy)

@given(instance=SpecElementWithUserDefinedAttributes_strategy)
@settings(max_examples=50)
def test_specelementwithuserdefinedattributes_instantiation(instance):
    assert isinstance(instance, SpecElementWithUserDefinedAttributes)

@given(instance=rif11a_ExchangeFile_SpecGroup_strategy)
@settings(max_examples=50)
def test_rif11a_exchangefile_specgroup_instantiation(instance):
    assert isinstance(instance, rif11a_ExchangeFile_SpecGroup)

@given(instance=rif11a_ExchangeFile_SpecRelation_strategy)
@settings(max_examples=50)
def test_rif11a_exchangefile_specrelation_instantiation(instance):
    assert isinstance(instance, rif11a_ExchangeFile_SpecRelation)

@given(instance=rif11a_ExchangeFile_SpecObject_strategy)
@settings(max_examples=50)
def test_rif11a_exchangefile_specobject_instantiation(instance):
    assert isinstance(instance, rif11a_ExchangeFile_SpecObject)

@given(instance=rif11a_ExchangeFile_SpecHierarchyRoot_strategy)
@settings(max_examples=50)
def test_rif11a_exchangefile_spechierarchyroot_instantiation(instance):
    assert isinstance(instance, rif11a_ExchangeFile_SpecHierarchyRoot)
