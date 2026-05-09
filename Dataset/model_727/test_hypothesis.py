import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    rif11a::DataTypes::BinaryContent,
    ExchangeFile::AccessPolicy,
    rif11a::DataTypes::XhtmlContent,
    rif11a::DataTypes::XmlContent,
    DatatypeDefinitionSimple,
    rif11a::ExchangeFile::DatatypeDefinitionDate,
    rif11a::ExchangeFile::DatatypeDefinitionBoolean,
    DatatypeDefinitionComplex,
    rif11a::ExchangeFile::DatatypeDefinitionDocument,
    rif11a::ExchangeFile::DatatypeDefinitionBinaryFile,
    DataTypes::XmlContent,
    DataTypes::BinaryContent,
    rif11a::ExchangeFile::RIF,
    rif11a::ExchangeFile::DatatypeDefinitionXmlData,
    rif11a::ExchangeFile::DatatypeDefinitionString,
    rif11a::ExchangeFile::DatatypeDefinitionReal,
    rif11a::ExchangeFile::DatatypeDefinitionInteger,
    ExchangeFile::AttributeDefinitionEnumeration,
    rif11a::ExchangeFile::EmbeddedValue,
    ExchangeFile::EmbeddedValue,
    ExchangeFile::EnumValue,
    ExchangeFile::AttributeValueEnumeration,
    ExchangeFile::DatatypeDefinitionEnumeration,
    DataTypes::XhtmlContent,
    ExchangeFile::AttributeDefinitionComplex,
    AttributeValueComplex,
    rif11a::ExchangeFile::AttributeValueFileReference,
    rif11a::ExchangeFile::AttributeValueEmbeddedFile,
    rif11a::ExchangeFile::AttributeValueXmlData,
    rif11a::ExchangeFile::AttributeValueEmbeddedDocument,
    ExchangeFile::AttributeDefinitionSimple,
    ExchangeFile::AttributeValueSimple,
    ExchangeFile::DatatypeDefinitionSimple,
    ExchangeFile::DatatypeDefinition,
    ExchangeFile::SpecGroup,
    AttributeValue,
    rif11a::ExchangeFile::AttributeValueSimple,
    rif11a::ExchangeFile::AttributeValueEnumeration,
    rif11a::ExchangeFile::AttributeValueComplex,
    DatatypeDefinition,
    rif11a::ExchangeFile::DatatypeDefinitionSimple,
    rif11a::ExchangeFile::DatatypeDefinitionEnumeration,
    rif11a::ExchangeFile::DatatypeDefinitionComplex,
    ExchangeFile::AttributeValueComplex,
    ExchangeFile::DatatypeDefinitionComplex,
    AttributeDefinition,
    rif11a::ExchangeFile::AttributeDefinitionEnumeration,
    rif11a::ExchangeFile::AttributeDefinitionSimple,
    rif11a::ExchangeFile::AttributeDefinitionComplex,
    ExchangeFile::SpecHierarchyRoot,
    ExchangeFile::AttributeDefinition,
    rif11a::ExchangeFile::Identifiable,
    ExchangeFile::AttributeValue,
    ExchangeFile::SpecType,
    Identifiable,
    rif11a::ExchangeFile::AttributeDefinition,
    rif11a::ExchangeFile::DatatypeDefinition,
    rif11a::ExchangeFile::AccessPolicy,
    rif11a::ExchangeFile::AttributeValue,
    rif11a::ExchangeFile::SpecType,
    rif11a::ExchangeFile::EnumValue,
    rif11a::ExchangeFile::SpecElementWithUserDefinedAttributes,
    ExchangeFile::SpecHierarchy,
    ExchangeFile::SpecRelation,
    rif11a::ExchangeFile::RelationGroup,
    ExchangeFile::RelationGroup,
    ExchangeFile::SpecObject,
    rif11a::ExchangeFile::SpecHierarchy,
    SpecElementWithUserDefinedAttributes,
    rif11a::ExchangeFile::SpecRelation,
    rif11a::ExchangeFile::SpecGroup,
    rif11a::ExchangeFile::SpecObject,
    rif11a::ExchangeFile::SpecHierarchyRoot,
    AccessPolicyAccessModeEnum,
    DatatypeDefinitionDateFormatEnum,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rif11a::datatypes::binarycontent_is_not_abstract():
    assert not inspect.isabstract(rif11a::DataTypes::BinaryContent)


def test_rif11a::datatypes::binarycontent_constructor_exists():
    assert callable(rif11a::DataTypes::BinaryContent.__init__)


def test_rif11a::datatypes::binarycontent_constructor_args():
    sig = inspect.signature(rif11a::DataTypes::BinaryContent.__init__)
    params = list(sig.parameters.keys())



def test_exchangefile::accesspolicy_is_not_abstract():
    assert not inspect.isabstract(ExchangeFile::AccessPolicy)


def test_exchangefile::accesspolicy_constructor_exists():
    assert callable(ExchangeFile::AccessPolicy.__init__)


def test_exchangefile::accesspolicy_constructor_args():
    sig = inspect.signature(ExchangeFile::AccessPolicy.__init__)
    params = list(sig.parameters.keys())



def test_rif11a::datatypes::xhtmlcontent_is_not_abstract():
    assert not inspect.isabstract(rif11a::DataTypes::XhtmlContent)


def test_rif11a::datatypes::xhtmlcontent_constructor_exists():
    assert callable(rif11a::DataTypes::XhtmlContent.__init__)


def test_rif11a::datatypes::xhtmlcontent_constructor_args():
    sig = inspect.signature(rif11a::DataTypes::XhtmlContent.__init__)
    params = list(sig.parameters.keys())



def test_rif11a::datatypes::xmlcontent_is_not_abstract():
    assert not inspect.isabstract(rif11a::DataTypes::XmlContent)


def test_rif11a::datatypes::xmlcontent_constructor_exists():
    assert callable(rif11a::DataTypes::XmlContent.__init__)


def test_rif11a::datatypes::xmlcontent_constructor_args():
    sig = inspect.signature(rif11a::DataTypes::XmlContent.__init__)
    params = list(sig.parameters.keys())



def test_datatypedefinitionsimple_is_not_abstract():
    assert not inspect.isabstract(DatatypeDefinitionSimple)


def test_datatypedefinitionsimple_constructor_exists():
    assert callable(DatatypeDefinitionSimple.__init__)


def test_datatypedefinitionsimple_constructor_args():
    sig = inspect.signature(DatatypeDefinitionSimple.__init__)
    params = list(sig.parameters.keys())



def test_rif11a::exchangefile::datatypedefinitiondate_is_not_abstract():
    assert not inspect.isabstract(rif11a::ExchangeFile::DatatypeDefinitionDate)


def test_rif11a::exchangefile::datatypedefinitiondate_constructor_exists():
    assert callable(rif11a::ExchangeFile::DatatypeDefinitionDate.__init__)


def test_rif11a::exchangefile::datatypedefinitiondate_constructor_args():
    sig = inspect.signature(rif11a::ExchangeFile::DatatypeDefinitionDate.__init__)
    params = list(sig.parameters.keys())
    assert "format" in params, "Missing parameter 'format'"

def test_rif11a::exchangefile::datatypedefinitiondate_has_format():
    assert hasattr(rif11a::ExchangeFile::DatatypeDefinitionDate, "format")
    descriptor = None
    for klass in rif11a::ExchangeFile::DatatypeDefinitionDate.__mro__:
        if "format" in klass.__dict__:
            descriptor = klass.__dict__["format"]
            break
    assert isinstance(descriptor, property)



def test_rif11a::exchangefile::datatypedefinitionboolean_is_not_abstract():
    assert not inspect.isabstract(rif11a::ExchangeFile::DatatypeDefinitionBoolean)


def test_rif11a::exchangefile::datatypedefinitionboolean_constructor_exists():
    assert callable(rif11a::ExchangeFile::DatatypeDefinitionBoolean.__init__)


def test_rif11a::exchangefile::datatypedefinitionboolean_constructor_args():
    sig = inspect.signature(rif11a::ExchangeFile::DatatypeDefinitionBoolean.__init__)
    params = list(sig.parameters.keys())



def test_datatypedefinitioncomplex_is_not_abstract():
    assert not inspect.isabstract(DatatypeDefinitionComplex)


def test_datatypedefinitioncomplex_constructor_exists():
    assert callable(DatatypeDefinitionComplex.__init__)


def test_datatypedefinitioncomplex_constructor_args():
    sig = inspect.signature(DatatypeDefinitionComplex.__init__)
    params = list(sig.parameters.keys())



def test_rif11a::exchangefile::datatypedefinitiondocument_is_not_abstract():
    assert not inspect.isabstract(rif11a::ExchangeFile::DatatypeDefinitionDocument)


def test_rif11a::exchangefile::datatypedefinitiondocument_constructor_exists():
    assert callable(rif11a::ExchangeFile::DatatypeDefinitionDocument.__init__)


def test_rif11a::exchangefile::datatypedefinitiondocument_constructor_args():
    sig = inspect.signature(rif11a::ExchangeFile::DatatypeDefinitionDocument.__init__)
    params = list(sig.parameters.keys())



def test_rif11a::exchangefile::datatypedefinitionbinaryfile_is_not_abstract():
    assert not inspect.isabstract(rif11a::ExchangeFile::DatatypeDefinitionBinaryFile)


def test_rif11a::exchangefile::datatypedefinitionbinaryfile_constructor_exists():
    assert callable(rif11a::ExchangeFile::DatatypeDefinitionBinaryFile.__init__)


def test_rif11a::exchangefile::datatypedefinitionbinaryfile_constructor_args():
    sig = inspect.signature(rif11a::ExchangeFile::DatatypeDefinitionBinaryFile.__init__)
    params = list(sig.parameters.keys())
    assert "mimeType" in params, "Missing parameter 'mimeType'"
    assert "filenameSuffix" in params, "Missing parameter 'filenameSuffix'"
    assert "formatName" in params, "Missing parameter 'formatName'"
    assert "application" in params, "Missing parameter 'application'"

def test_rif11a::exchangefile::datatypedefinitionbinaryfile_has_mimeType():
    assert hasattr(rif11a::ExchangeFile::DatatypeDefinitionBinaryFile, "mimeType")
    descriptor = None
    for klass in rif11a::ExchangeFile::DatatypeDefinitionBinaryFile.__mro__:
        if "mimeType" in klass.__dict__:
            descriptor = klass.__dict__["mimeType"]
            break
    assert isinstance(descriptor, property)

def test_rif11a::exchangefile::datatypedefinitionbinaryfile_has_filenameSuffix():
    assert hasattr(rif11a::ExchangeFile::DatatypeDefinitionBinaryFile, "filenameSuffix")
    descriptor = None
    for klass in rif11a::ExchangeFile::DatatypeDefinitionBinaryFile.__mro__:
        if "filenameSuffix" in klass.__dict__:
            descriptor = klass.__dict__["filenameSuffix"]
            break
    assert isinstance(descriptor, property)

def test_rif11a::exchangefile::datatypedefinitionbinaryfile_has_formatName():
    assert hasattr(rif11a::ExchangeFile::DatatypeDefinitionBinaryFile, "formatName")
    descriptor = None
    for klass in rif11a::ExchangeFile::DatatypeDefinitionBinaryFile.__mro__:
        if "formatName" in klass.__dict__:
            descriptor = klass.__dict__["formatName"]
            break
    assert isinstance(descriptor, property)

def test_rif11a::exchangefile::datatypedefinitionbinaryfile_has_application():
    assert hasattr(rif11a::ExchangeFile::DatatypeDefinitionBinaryFile, "application")
    descriptor = None
    for klass in rif11a::ExchangeFile::DatatypeDefinitionBinaryFile.__mro__:
        if "application" in klass.__dict__:
            descriptor = klass.__dict__["application"]
            break
    assert isinstance(descriptor, property)



def test_datatypes::xmlcontent_is_not_abstract():
    assert not inspect.isabstract(DataTypes::XmlContent)


def test_datatypes::xmlcontent_constructor_exists():
    assert callable(DataTypes::XmlContent.__init__)


def test_datatypes::xmlcontent_constructor_args():
    sig = inspect.signature(DataTypes::XmlContent.__init__)
    params = list(sig.parameters.keys())



def test_datatypes::binarycontent_is_not_abstract():
    assert not inspect.isabstract(DataTypes::BinaryContent)


def test_datatypes::binarycontent_constructor_exists():
    assert callable(DataTypes::BinaryContent.__init__)


def test_datatypes::binarycontent_constructor_args():
    sig = inspect.signature(DataTypes::BinaryContent.__init__)
    params = list(sig.parameters.keys())



def test_rif11a::exchangefile::rif_is_not_abstract():
    assert not inspect.isabstract(rif11a::ExchangeFile::RIF)


def test_rif11a::exchangefile::rif_constructor_exists():
    assert callable(rif11a::ExchangeFile::RIF.__init__)


def test_rif11a::exchangefile::rif_constructor_args():
    sig = inspect.signature(rif11a::ExchangeFile::RIF.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "creationTime" in params, "Missing parameter 'creationTime'"
    assert "title" in params, "Missing parameter 'title'"
    assert "countryCode" in params, "Missing parameter 'countryCode'"
    assert "version" in params, "Missing parameter 'version'"
    assert "sourceToolId" in params, "Missing parameter 'sourceToolId'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "author" in params, "Missing parameter 'author'"

def test_rif11a::exchangefile::rif_has_identifier():
    assert hasattr(rif11a::ExchangeFile::RIF, "identifier")
    descriptor = None
    for klass in rif11a::ExchangeFile::RIF.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)

def test_rif11a::exchangefile::rif_has_creationTime():
    assert hasattr(rif11a::ExchangeFile::RIF, "creationTime")
    descriptor = None
    for klass in rif11a::ExchangeFile::RIF.__mro__:
        if "creationTime" in klass.__dict__:
            descriptor = klass.__dict__["creationTime"]
            break
    assert isinstance(descriptor, property)

def test_rif11a::exchangefile::rif_has_title():
    assert hasattr(rif11a::ExchangeFile::RIF, "title")
    descriptor = None
    for klass in rif11a::ExchangeFile::RIF.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_rif11a::exchangefile::rif_has_countryCode():
    assert hasattr(rif11a::ExchangeFile::RIF, "countryCode")
    descriptor = None
    for klass in rif11a::ExchangeFile::RIF.__mro__:
        if "countryCode" in klass.__dict__:
            descriptor = klass.__dict__["countryCode"]
            break
    assert isinstance(descriptor, property)

def test_rif11a::exchangefile::rif_has_version():
    assert hasattr(rif11a::ExchangeFile::RIF, "version")
    descriptor = None
    for klass in rif11a::ExchangeFile::RIF.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_rif11a::exchangefile::rif_has_sourceToolId():
    assert hasattr(rif11a::ExchangeFile::RIF, "sourceToolId")
    descriptor = None
    for klass in rif11a::ExchangeFile::RIF.__mro__:
        if "sourceToolId" in klass.__dict__:
            descriptor = klass.__dict__["sourceToolId"]
            break
    assert isinstance(descriptor, property)

def test_rif11a::exchangefile::rif_has_comment():
    assert hasattr(rif11a::ExchangeFile::RIF, "comment")
    descriptor = None
    for klass in rif11a::ExchangeFile::RIF.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_rif11a::exchangefile::rif_has_author():
    assert hasattr(rif11a::ExchangeFile::RIF, "author")
    descriptor = None
    for klass in rif11a::ExchangeFile::RIF.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)



def test_rif11a::exchangefile::datatypedefinitionxmldata_is_not_abstract():
    assert not inspect.isabstract(rif11a::ExchangeFile::DatatypeDefinitionXmlData)


def test_rif11a::exchangefile::datatypedefinitionxmldata_constructor_exists():
    assert callable(rif11a::ExchangeFile::DatatypeDefinitionXmlData.__init__)


def test_rif11a::exchangefile::datatypedefinitionxmldata_constructor_args():
    sig = inspect.signature(rif11a::ExchangeFile::DatatypeDefinitionXmlData.__init__)
    params = list(sig.parameters.keys())
    assert "nameSpaceURI" in params, "Missing parameter 'nameSpaceURI'"
    assert "schemaLocation" in params, "Missing parameter 'schemaLocation'"

def test_rif11a::exchangefile::datatypedefinitionxmldata_has_nameSpaceURI():
    assert hasattr(rif11a::ExchangeFile::DatatypeDefinitionXmlData, "nameSpaceURI")
    descriptor = None
    for klass in rif11a::ExchangeFile::DatatypeDefinitionXmlData.__mro__:
        if "nameSpaceURI" in klass.__dict__:
            descriptor = klass.__dict__["nameSpaceURI"]
            break
    assert isinstance(descriptor, property)

def test_rif11a::exchangefile::datatypedefinitionxmldata_has_schemaLocation():
    assert hasattr(rif11a::ExchangeFile::DatatypeDefinitionXmlData, "schemaLocation")
    descriptor = None
    for klass in rif11a::ExchangeFile::DatatypeDefinitionXmlData.__mro__:
        if "schemaLocation" in klass.__dict__:
            descriptor = klass.__dict__["schemaLocation"]
            break
    assert isinstance(descriptor, property)



def test_rif11a::exchangefile::datatypedefinitionstring_is_not_abstract():
    assert not inspect.isabstract(rif11a::ExchangeFile::DatatypeDefinitionString)


def test_rif11a::exchangefile::datatypedefinitionstring_constructor_exists():
    assert callable(rif11a::ExchangeFile::DatatypeDefinitionString.__init__)


def test_rif11a::exchangefile::datatypedefinitionstring_constructor_args():
    sig = inspect.signature(rif11a::ExchangeFile::DatatypeDefinitionString.__init__)
    params = list(sig.parameters.keys())
    assert "maxLength" in params, "Missing parameter 'maxLength'"

def test_rif11a::exchangefile::datatypedefinitionstring_has_maxLength():
    assert hasattr(rif11a::ExchangeFile::DatatypeDefinitionString, "maxLength")
    descriptor = None
    for klass in rif11a::ExchangeFile::DatatypeDefinitionString.__mro__:
        if "maxLength" in klass.__dict__:
            descriptor = klass.__dict__["maxLength"]
            break
    assert isinstance(descriptor, property)



def test_rif11a::exchangefile::datatypedefinitionreal_is_not_abstract():
    assert not inspect.isabstract(rif11a::ExchangeFile::DatatypeDefinitionReal)


def test_rif11a::exchangefile::datatypedefinitionreal_constructor_exists():
    assert callable(rif11a::ExchangeFile::DatatypeDefinitionReal.__init__)


def test_rif11a::exchangefile::datatypedefinitionreal_constructor_args():
    sig = inspect.signature(rif11a::ExchangeFile::DatatypeDefinitionReal.__init__)
    params = list(sig.parameters.keys())
    assert "min" in params, "Missing parameter 'min'"
    assert "max" in params, "Missing parameter 'max'"
    assert "accuracy" in params, "Missing parameter 'accuracy'"

def test_rif11a::exchangefile::datatypedefinitionreal_has_min():
    assert hasattr(rif11a::ExchangeFile::DatatypeDefinitionReal, "min")
    descriptor = None
    for klass in rif11a::ExchangeFile::DatatypeDefinitionReal.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_rif11a::exchangefile::datatypedefinitionreal_has_max():
    assert hasattr(rif11a::ExchangeFile::DatatypeDefinitionReal, "max")
    descriptor = None
    for klass in rif11a::ExchangeFile::DatatypeDefinitionReal.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_rif11a::exchangefile::datatypedefinitionreal_has_accuracy():
    assert hasattr(rif11a::ExchangeFile::DatatypeDefinitionReal, "accuracy")
    descriptor = None
    for klass in rif11a::ExchangeFile::DatatypeDefinitionReal.__mro__:
        if "accuracy" in klass.__dict__:
            descriptor = klass.__dict__["accuracy"]
            break
    assert isinstance(descriptor, property)



def test_rif11a::exchangefile::datatypedefinitioninteger_is_not_abstract():
    assert not inspect.isabstract(rif11a::ExchangeFile::DatatypeDefinitionInteger)


def test_rif11a::exchangefile::datatypedefinitioninteger_constructor_exists():
    assert callable(rif11a::ExchangeFile::DatatypeDefinitionInteger.__init__)


def test_rif11a::exchangefile::datatypedefinitioninteger_constructor_args():
    sig = inspect.signature(rif11a::ExchangeFile::DatatypeDefinitionInteger.__init__)
    params = list(sig.parameters.keys())
    assert "max" in params, "Missing parameter 'max'"
    assert "min" in params, "Missing parameter 'min'"

def test_rif11a::exchangefile::datatypedefinitioninteger_has_max():
    assert hasattr(rif11a::ExchangeFile::DatatypeDefinitionInteger, "max")
    descriptor = None
    for klass in rif11a::ExchangeFile::DatatypeDefinitionInteger.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_rif11a::exchangefile::datatypedefinitioninteger_has_min():
    assert hasattr(rif11a::ExchangeFile::DatatypeDefinitionInteger, "min")
    descriptor = None
    for klass in rif11a::ExchangeFile::DatatypeDefinitionInteger.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)



def test_exchangefile::attributedefinitionenumeration_is_not_abstract():
    assert not inspect.isabstract(ExchangeFile::AttributeDefinitionEnumeration)


def test_exchangefile::attributedefinitionenumeration_constructor_exists():
    assert callable(ExchangeFile::AttributeDefinitionEnumeration.__init__)


def test_exchangefile::attributedefinitionenumeration_constructor_args():
    sig = inspect.signature(ExchangeFile::AttributeDefinitionEnumeration.__init__)
    params = list(sig.parameters.keys())



def test_rif11a::exchangefile::embeddedvalue_is_not_abstract():
    assert not inspect.isabstract(rif11a::ExchangeFile::EmbeddedValue)


def test_rif11a::exchangefile::embeddedvalue_constructor_exists():
    assert callable(rif11a::ExchangeFile::EmbeddedValue.__init__)


def test_rif11a::exchangefile::embeddedvalue_constructor_args():
    sig = inspect.signature(rif11a::ExchangeFile::EmbeddedValue.__init__)
    params = list(sig.parameters.keys())
    assert "otherContent" in params, "Missing parameter 'otherContent'"
    assert "key" in params, "Missing parameter 'key'"

def test_rif11a::exchangefile::embeddedvalue_has_otherContent():
    assert hasattr(rif11a::ExchangeFile::EmbeddedValue, "otherContent")
    descriptor = None
    for klass in rif11a::ExchangeFile::EmbeddedValue.__mro__:
        if "otherContent" in klass.__dict__:
            descriptor = klass.__dict__["otherContent"]
            break
    assert isinstance(descriptor, property)

def test_rif11a::exchangefile::embeddedvalue_has_key():
    assert hasattr(rif11a::ExchangeFile::EmbeddedValue, "key")
    descriptor = None
    for klass in rif11a::ExchangeFile::EmbeddedValue.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_exchangefile::embeddedvalue_is_not_abstract():
    assert not inspect.isabstract(ExchangeFile::EmbeddedValue)


def test_exchangefile::embeddedvalue_constructor_exists():
    assert callable(ExchangeFile::EmbeddedValue.__init__)


def test_exchangefile::embeddedvalue_constructor_args():
    sig = inspect.signature(ExchangeFile::EmbeddedValue.__init__)
    params = list(sig.parameters.keys())



def test_exchangefile::enumvalue_is_not_abstract():
    assert not inspect.isabstract(ExchangeFile::EnumValue)


def test_exchangefile::enumvalue_constructor_exists():
    assert callable(ExchangeFile::EnumValue.__init__)


def test_exchangefile::enumvalue_constructor_args():
    sig = inspect.signature(ExchangeFile::EnumValue.__init__)
    params = list(sig.parameters.keys())



def test_exchangefile::attributevalueenumeration_is_not_abstract():
    assert not inspect.isabstract(ExchangeFile::AttributeValueEnumeration)


def test_exchangefile::attributevalueenumeration_constructor_exists():
    assert callable(ExchangeFile::AttributeValueEnumeration.__init__)


def test_exchangefile::attributevalueenumeration_constructor_args():
    sig = inspect.signature(ExchangeFile::AttributeValueEnumeration.__init__)
    params = list(sig.parameters.keys())



def test_exchangefile::datatypedefinitionenumeration_is_not_abstract():
    assert not inspect.isabstract(ExchangeFile::DatatypeDefinitionEnumeration)


def test_exchangefile::datatypedefinitionenumeration_constructor_exists():
    assert callable(ExchangeFile::DatatypeDefinitionEnumeration.__init__)


def test_exchangefile::datatypedefinitionenumeration_constructor_args():
    sig = inspect.signature(ExchangeFile::DatatypeDefinitionEnumeration.__init__)
    params = list(sig.parameters.keys())



def test_datatypes::xhtmlcontent_is_not_abstract():
    assert not inspect.isabstract(DataTypes::XhtmlContent)


def test_datatypes::xhtmlcontent_constructor_exists():
    assert callable(DataTypes::XhtmlContent.__init__)


def test_datatypes::xhtmlcontent_constructor_args():
    sig = inspect.signature(DataTypes::XhtmlContent.__init__)
    params = list(sig.parameters.keys())



def test_exchangefile::attributedefinitioncomplex_is_not_abstract():
    assert not inspect.isabstract(ExchangeFile::AttributeDefinitionComplex)


def test_exchangefile::attributedefinitioncomplex_constructor_exists():
    assert callable(ExchangeFile::AttributeDefinitionComplex.__init__)


def test_exchangefile::attributedefinitioncomplex_constructor_args():
    sig = inspect.signature(ExchangeFile::AttributeDefinitionComplex.__init__)
    params = list(sig.parameters.keys())



def test_attributevaluecomplex_is_not_abstract():
    assert not inspect.isabstract(AttributeValueComplex)


def test_attributevaluecomplex_constructor_exists():
    assert callable(AttributeValueComplex.__init__)


def test_attributevaluecomplex_constructor_args():
    sig = inspect.signature(AttributeValueComplex.__init__)
    params = list(sig.parameters.keys())



def test_rif11a::exchangefile::attributevaluefilereference_is_not_abstract():
    assert not inspect.isabstract(rif11a::ExchangeFile::AttributeValueFileReference)


def test_rif11a::exchangefile::attributevaluefilereference_constructor_exists():
    assert callable(rif11a::ExchangeFile::AttributeValueFileReference.__init__)


def test_rif11a::exchangefile::attributevaluefilereference_constructor_args():
    sig = inspect.signature(rif11a::ExchangeFile::AttributeValueFileReference.__init__)
    params = list(sig.parameters.keys())
    assert "pathToFile" in params, "Missing parameter 'pathToFile'"

def test_rif11a::exchangefile::attributevaluefilereference_has_pathToFile():
    assert hasattr(rif11a::ExchangeFile::AttributeValueFileReference, "pathToFile")
    descriptor = None
    for klass in rif11a::ExchangeFile::AttributeValueFileReference.__mro__:
        if "pathToFile" in klass.__dict__:
            descriptor = klass.__dict__["pathToFile"]
            break
    assert isinstance(descriptor, property)



def test_rif11a::exchangefile::attributevalueembeddedfile_is_not_abstract():
    assert not inspect.isabstract(rif11a::ExchangeFile::AttributeValueEmbeddedFile)


def test_rif11a::exchangefile::attributevalueembeddedfile_constructor_exists():
    assert callable(rif11a::ExchangeFile::AttributeValueEmbeddedFile.__init__)


def test_rif11a::exchangefile::attributevalueembeddedfile_constructor_args():
    sig = inspect.signature(rif11a::ExchangeFile::AttributeValueEmbeddedFile.__init__)
    params = list(sig.parameters.keys())



def test_rif11a::exchangefile::attributevaluexmldata_is_not_abstract():
    assert not inspect.isabstract(rif11a::ExchangeFile::AttributeValueXmlData)


def test_rif11a::exchangefile::attributevaluexmldata_constructor_exists():
    assert callable(rif11a::ExchangeFile::AttributeValueXmlData.__init__)


def test_rif11a::exchangefile::attributevaluexmldata_constructor_args():
    sig = inspect.signature(rif11a::ExchangeFile::AttributeValueXmlData.__init__)
    params = list(sig.parameters.keys())



def test_rif11a::exchangefile::attributevalueembeddeddocument_is_not_abstract():
    assert not inspect.isabstract(rif11a::ExchangeFile::AttributeValueEmbeddedDocument)


def test_rif11a::exchangefile::attributevalueembeddeddocument_constructor_exists():
    assert callable(rif11a::ExchangeFile::AttributeValueEmbeddedDocument.__init__)


def test_rif11a::exchangefile::attributevalueembeddeddocument_constructor_args():
    sig = inspect.signature(rif11a::ExchangeFile::AttributeValueEmbeddedDocument.__init__)
    params = list(sig.parameters.keys())



def test_exchangefile::attributedefinitionsimple_is_not_abstract():
    assert not inspect.isabstract(ExchangeFile::AttributeDefinitionSimple)


def test_exchangefile::attributedefinitionsimple_constructor_exists():
    assert callable(ExchangeFile::AttributeDefinitionSimple.__init__)


def test_exchangefile::attributedefinitionsimple_constructor_args():
    sig = inspect.signature(ExchangeFile::AttributeDefinitionSimple.__init__)
    params = list(sig.parameters.keys())



def test_exchangefile::attributevaluesimple_is_not_abstract():
    assert not inspect.isabstract(ExchangeFile::AttributeValueSimple)


def test_exchangefile::attributevaluesimple_constructor_exists():
    assert callable(ExchangeFile::AttributeValueSimple.__init__)


def test_exchangefile::attributevaluesimple_constructor_args():
    sig = inspect.signature(ExchangeFile::AttributeValueSimple.__init__)
    params = list(sig.parameters.keys())



def test_exchangefile::datatypedefinitionsimple_is_not_abstract():
    assert not inspect.isabstract(ExchangeFile::DatatypeDefinitionSimple)


def test_exchangefile::datatypedefinitionsimple_constructor_exists():
    assert callable(ExchangeFile::DatatypeDefinitionSimple.__init__)


def test_exchangefile::datatypedefinitionsimple_constructor_args():
    sig = inspect.signature(ExchangeFile::DatatypeDefinitionSimple.__init__)
    params = list(sig.parameters.keys())



def test_exchangefile::datatypedefinition_is_not_abstract():
    assert not inspect.isabstract(ExchangeFile::DatatypeDefinition)


def test_exchangefile::datatypedefinition_constructor_exists():
    assert callable(ExchangeFile::DatatypeDefinition.__init__)


def test_exchangefile::datatypedefinition_constructor_args():
    sig = inspect.signature(ExchangeFile::DatatypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_exchangefile::specgroup_is_not_abstract():
    assert not inspect.isabstract(ExchangeFile::SpecGroup)


def test_exchangefile::specgroup_constructor_exists():
    assert callable(ExchangeFile::SpecGroup.__init__)


def test_exchangefile::specgroup_constructor_args():
    sig = inspect.signature(ExchangeFile::SpecGroup.__init__)
    params = list(sig.parameters.keys())



def test_attributevalue_is_not_abstract():
    assert not inspect.isabstract(AttributeValue)


def test_attributevalue_constructor_exists():
    assert callable(AttributeValue.__init__)


def test_attributevalue_constructor_args():
    sig = inspect.signature(AttributeValue.__init__)
    params = list(sig.parameters.keys())



def test_rif11a::exchangefile::attributevaluesimple_is_not_abstract():
    assert not inspect.isabstract(rif11a::ExchangeFile::AttributeValueSimple)


def test_rif11a::exchangefile::attributevaluesimple_constructor_exists():
    assert callable(rif11a::ExchangeFile::AttributeValueSimple.__init__)


def test_rif11a::exchangefile::attributevaluesimple_constructor_args():
    sig = inspect.signature(rif11a::ExchangeFile::AttributeValueSimple.__init__)
    params = list(sig.parameters.keys())
    assert "theValue" in params, "Missing parameter 'theValue'"

def test_rif11a::exchangefile::attributevaluesimple_has_theValue():
    assert hasattr(rif11a::ExchangeFile::AttributeValueSimple, "theValue")
    descriptor = None
    for klass in rif11a::ExchangeFile::AttributeValueSimple.__mro__:
        if "theValue" in klass.__dict__:
            descriptor = klass.__dict__["theValue"]
            break
    assert isinstance(descriptor, property)



def test_rif11a::exchangefile::attributevalueenumeration_is_not_abstract():
    assert not inspect.isabstract(rif11a::ExchangeFile::AttributeValueEnumeration)


def test_rif11a::exchangefile::attributevalueenumeration_constructor_exists():
    assert callable(rif11a::ExchangeFile::AttributeValueEnumeration.__init__)


def test_rif11a::exchangefile::attributevalueenumeration_constructor_args():
    sig = inspect.signature(rif11a::ExchangeFile::AttributeValueEnumeration.__init__)
    params = list(sig.parameters.keys())



def test_rif11a::exchangefile::attributevaluecomplex_is_not_abstract():
    assert not inspect.isabstract(rif11a::ExchangeFile::AttributeValueComplex)


def test_rif11a::exchangefile::attributevaluecomplex_constructor_exists():
    assert callable(rif11a::ExchangeFile::AttributeValueComplex.__init__)


def test_rif11a::exchangefile::attributevaluecomplex_constructor_args():
    sig = inspect.signature(rif11a::ExchangeFile::AttributeValueComplex.__init__)
    params = list(sig.parameters.keys())



def test_datatypedefinition_is_not_abstract():
    assert not inspect.isabstract(DatatypeDefinition)


def test_datatypedefinition_constructor_exists():
    assert callable(DatatypeDefinition.__init__)


def test_datatypedefinition_constructor_args():
    sig = inspect.signature(DatatypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_rif11a::exchangefile::datatypedefinitionsimple_is_not_abstract():
    assert not inspect.isabstract(rif11a::ExchangeFile::DatatypeDefinitionSimple)


def test_rif11a::exchangefile::datatypedefinitionsimple_constructor_exists():
    assert callable(rif11a::ExchangeFile::DatatypeDefinitionSimple.__init__)


def test_rif11a::exchangefile::datatypedefinitionsimple_constructor_args():
    sig = inspect.signature(rif11a::ExchangeFile::DatatypeDefinitionSimple.__init__)
    params = list(sig.parameters.keys())



def test_rif11a::exchangefile::datatypedefinitionenumeration_is_not_abstract():
    assert not inspect.isabstract(rif11a::ExchangeFile::DatatypeDefinitionEnumeration)


def test_rif11a::exchangefile::datatypedefinitionenumeration_constructor_exists():
    assert callable(rif11a::ExchangeFile::DatatypeDefinitionEnumeration.__init__)


def test_rif11a::exchangefile::datatypedefinitionenumeration_constructor_args():
    sig = inspect.signature(rif11a::ExchangeFile::DatatypeDefinitionEnumeration.__init__)
    params = list(sig.parameters.keys())



def test_rif11a::exchangefile::datatypedefinitioncomplex_is_not_abstract():
    assert not inspect.isabstract(rif11a::ExchangeFile::DatatypeDefinitionComplex)


def test_rif11a::exchangefile::datatypedefinitioncomplex_constructor_exists():
    assert callable(rif11a::ExchangeFile::DatatypeDefinitionComplex.__init__)


def test_rif11a::exchangefile::datatypedefinitioncomplex_constructor_args():
    sig = inspect.signature(rif11a::ExchangeFile::DatatypeDefinitionComplex.__init__)
    params = list(sig.parameters.keys())
    assert "embedded" in params, "Missing parameter 'embedded'"

def test_rif11a::exchangefile::datatypedefinitioncomplex_has_embedded():
    assert hasattr(rif11a::ExchangeFile::DatatypeDefinitionComplex, "embedded")
    descriptor = None
    for klass in rif11a::ExchangeFile::DatatypeDefinitionComplex.__mro__:
        if "embedded" in klass.__dict__:
            descriptor = klass.__dict__["embedded"]
            break
    assert isinstance(descriptor, property)



def test_exchangefile::attributevaluecomplex_is_not_abstract():
    assert not inspect.isabstract(ExchangeFile::AttributeValueComplex)


def test_exchangefile::attributevaluecomplex_constructor_exists():
    assert callable(ExchangeFile::AttributeValueComplex.__init__)


def test_exchangefile::attributevaluecomplex_constructor_args():
    sig = inspect.signature(ExchangeFile::AttributeValueComplex.__init__)
    params = list(sig.parameters.keys())



def test_exchangefile::datatypedefinitioncomplex_is_not_abstract():
    assert not inspect.isabstract(ExchangeFile::DatatypeDefinitionComplex)


def test_exchangefile::datatypedefinitioncomplex_constructor_exists():
    assert callable(ExchangeFile::DatatypeDefinitionComplex.__init__)


def test_exchangefile::datatypedefinitioncomplex_constructor_args():
    sig = inspect.signature(ExchangeFile::DatatypeDefinitionComplex.__init__)
    params = list(sig.parameters.keys())



def test_attributedefinition_is_not_abstract():
    assert not inspect.isabstract(AttributeDefinition)


def test_attributedefinition_constructor_exists():
    assert callable(AttributeDefinition.__init__)


def test_attributedefinition_constructor_args():
    sig = inspect.signature(AttributeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_rif11a::exchangefile::attributedefinitionenumeration_is_not_abstract():
    assert not inspect.isabstract(rif11a::ExchangeFile::AttributeDefinitionEnumeration)


def test_rif11a::exchangefile::attributedefinitionenumeration_constructor_exists():
    assert callable(rif11a::ExchangeFile::AttributeDefinitionEnumeration.__init__)


def test_rif11a::exchangefile::attributedefinitionenumeration_constructor_args():
    sig = inspect.signature(rif11a::ExchangeFile::AttributeDefinitionEnumeration.__init__)
    params = list(sig.parameters.keys())
    assert "multiValued" in params, "Missing parameter 'multiValued'"

def test_rif11a::exchangefile::attributedefinitionenumeration_has_multiValued():
    assert hasattr(rif11a::ExchangeFile::AttributeDefinitionEnumeration, "multiValued")
    descriptor = None
    for klass in rif11a::ExchangeFile::AttributeDefinitionEnumeration.__mro__:
        if "multiValued" in klass.__dict__:
            descriptor = klass.__dict__["multiValued"]
            break
    assert isinstance(descriptor, property)



def test_rif11a::exchangefile::attributedefinitionsimple_is_not_abstract():
    assert not inspect.isabstract(rif11a::ExchangeFile::AttributeDefinitionSimple)


def test_rif11a::exchangefile::attributedefinitionsimple_constructor_exists():
    assert callable(rif11a::ExchangeFile::AttributeDefinitionSimple.__init__)


def test_rif11a::exchangefile::attributedefinitionsimple_constructor_args():
    sig = inspect.signature(rif11a::ExchangeFile::AttributeDefinitionSimple.__init__)
    params = list(sig.parameters.keys())



def test_rif11a::exchangefile::attributedefinitioncomplex_is_not_abstract():
    assert not inspect.isabstract(rif11a::ExchangeFile::AttributeDefinitionComplex)


def test_rif11a::exchangefile::attributedefinitioncomplex_constructor_exists():
    assert callable(rif11a::ExchangeFile::AttributeDefinitionComplex.__init__)


def test_rif11a::exchangefile::attributedefinitioncomplex_constructor_args():
    sig = inspect.signature(rif11a::ExchangeFile::AttributeDefinitionComplex.__init__)
    params = list(sig.parameters.keys())



def test_exchangefile::spechierarchyroot_is_not_abstract():
    assert not inspect.isabstract(ExchangeFile::SpecHierarchyRoot)


def test_exchangefile::spechierarchyroot_constructor_exists():
    assert callable(ExchangeFile::SpecHierarchyRoot.__init__)


def test_exchangefile::spechierarchyroot_constructor_args():
    sig = inspect.signature(ExchangeFile::SpecHierarchyRoot.__init__)
    params = list(sig.parameters.keys())



def test_exchangefile::attributedefinition_is_not_abstract():
    assert not inspect.isabstract(ExchangeFile::AttributeDefinition)


def test_exchangefile::attributedefinition_constructor_exists():
    assert callable(ExchangeFile::AttributeDefinition.__init__)


def test_exchangefile::attributedefinition_constructor_args():
    sig = inspect.signature(ExchangeFile::AttributeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_rif11a::exchangefile::identifiable_is_not_abstract():
    assert not inspect.isabstract(rif11a::ExchangeFile::Identifiable)


def test_rif11a::exchangefile::identifiable_constructor_exists():
    assert callable(rif11a::ExchangeFile::Identifiable.__init__)


def test_rif11a::exchangefile::identifiable_constructor_args():
    sig = inspect.signature(rif11a::ExchangeFile::Identifiable.__init__)
    params = list(sig.parameters.keys())
    assert "lastChange" in params, "Missing parameter 'lastChange'"
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "desc" in params, "Missing parameter 'desc'"
    assert "longName" in params, "Missing parameter 'longName'"

def test_rif11a::exchangefile::identifiable_has_lastChange():
    assert hasattr(rif11a::ExchangeFile::Identifiable, "lastChange")
    descriptor = None
    for klass in rif11a::ExchangeFile::Identifiable.__mro__:
        if "lastChange" in klass.__dict__:
            descriptor = klass.__dict__["lastChange"]
            break
    assert isinstance(descriptor, property)

def test_rif11a::exchangefile::identifiable_has_identifier():
    assert hasattr(rif11a::ExchangeFile::Identifiable, "identifier")
    descriptor = None
    for klass in rif11a::ExchangeFile::Identifiable.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)

def test_rif11a::exchangefile::identifiable_has_desc():
    assert hasattr(rif11a::ExchangeFile::Identifiable, "desc")
    descriptor = None
    for klass in rif11a::ExchangeFile::Identifiable.__mro__:
        if "desc" in klass.__dict__:
            descriptor = klass.__dict__["desc"]
            break
    assert isinstance(descriptor, property)

def test_rif11a::exchangefile::identifiable_has_longName():
    assert hasattr(rif11a::ExchangeFile::Identifiable, "longName")
    descriptor = None
    for klass in rif11a::ExchangeFile::Identifiable.__mro__:
        if "longName" in klass.__dict__:
            descriptor = klass.__dict__["longName"]
            break
    assert isinstance(descriptor, property)



def test_exchangefile::attributevalue_is_not_abstract():
    assert not inspect.isabstract(ExchangeFile::AttributeValue)


def test_exchangefile::attributevalue_constructor_exists():
    assert callable(ExchangeFile::AttributeValue.__init__)


def test_exchangefile::attributevalue_constructor_args():
    sig = inspect.signature(ExchangeFile::AttributeValue.__init__)
    params = list(sig.parameters.keys())



def test_exchangefile::spectype_is_not_abstract():
    assert not inspect.isabstract(ExchangeFile::SpecType)


def test_exchangefile::spectype_constructor_exists():
    assert callable(ExchangeFile::SpecType.__init__)


def test_exchangefile::spectype_constructor_args():
    sig = inspect.signature(ExchangeFile::SpecType.__init__)
    params = list(sig.parameters.keys())



def test_identifiable_is_not_abstract():
    assert not inspect.isabstract(Identifiable)


def test_identifiable_constructor_exists():
    assert callable(Identifiable.__init__)


def test_identifiable_constructor_args():
    sig = inspect.signature(Identifiable.__init__)
    params = list(sig.parameters.keys())



def test_rif11a::exchangefile::attributedefinition_is_not_abstract():
    assert not inspect.isabstract(rif11a::ExchangeFile::AttributeDefinition)


def test_rif11a::exchangefile::attributedefinition_constructor_exists():
    assert callable(rif11a::ExchangeFile::AttributeDefinition.__init__)


def test_rif11a::exchangefile::attributedefinition_constructor_args():
    sig = inspect.signature(rif11a::ExchangeFile::AttributeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_rif11a::exchangefile::datatypedefinition_is_not_abstract():
    assert not inspect.isabstract(rif11a::ExchangeFile::DatatypeDefinition)


def test_rif11a::exchangefile::datatypedefinition_constructor_exists():
    assert callable(rif11a::ExchangeFile::DatatypeDefinition.__init__)


def test_rif11a::exchangefile::datatypedefinition_constructor_args():
    sig = inspect.signature(rif11a::ExchangeFile::DatatypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_rif11a::exchangefile::accesspolicy_is_not_abstract():
    assert not inspect.isabstract(rif11a::ExchangeFile::AccessPolicy)


def test_rif11a::exchangefile::accesspolicy_constructor_exists():
    assert callable(rif11a::ExchangeFile::AccessPolicy.__init__)


def test_rif11a::exchangefile::accesspolicy_constructor_args():
    sig = inspect.signature(rif11a::ExchangeFile::AccessPolicy.__init__)
    params = list(sig.parameters.keys())
    assert "accessMode" in params, "Missing parameter 'accessMode'"

def test_rif11a::exchangefile::accesspolicy_has_accessMode():
    assert hasattr(rif11a::ExchangeFile::AccessPolicy, "accessMode")
    descriptor = None
    for klass in rif11a::ExchangeFile::AccessPolicy.__mro__:
        if "accessMode" in klass.__dict__:
            descriptor = klass.__dict__["accessMode"]
            break
    assert isinstance(descriptor, property)



def test_rif11a::exchangefile::attributevalue_is_not_abstract():
    assert not inspect.isabstract(rif11a::ExchangeFile::AttributeValue)


def test_rif11a::exchangefile::attributevalue_constructor_exists():
    assert callable(rif11a::ExchangeFile::AttributeValue.__init__)


def test_rif11a::exchangefile::attributevalue_constructor_args():
    sig = inspect.signature(rif11a::ExchangeFile::AttributeValue.__init__)
    params = list(sig.parameters.keys())



def test_rif11a::exchangefile::spectype_is_not_abstract():
    assert not inspect.isabstract(rif11a::ExchangeFile::SpecType)


def test_rif11a::exchangefile::spectype_constructor_exists():
    assert callable(rif11a::ExchangeFile::SpecType.__init__)


def test_rif11a::exchangefile::spectype_constructor_args():
    sig = inspect.signature(rif11a::ExchangeFile::SpecType.__init__)
    params = list(sig.parameters.keys())



def test_rif11a::exchangefile::enumvalue_is_not_abstract():
    assert not inspect.isabstract(rif11a::ExchangeFile::EnumValue)


def test_rif11a::exchangefile::enumvalue_constructor_exists():
    assert callable(rif11a::ExchangeFile::EnumValue.__init__)


def test_rif11a::exchangefile::enumvalue_constructor_args():
    sig = inspect.signature(rif11a::ExchangeFile::EnumValue.__init__)
    params = list(sig.parameters.keys())



def test_rif11a::exchangefile::specelementwithuserdefinedattributes_is_not_abstract():
    assert not inspect.isabstract(rif11a::ExchangeFile::SpecElementWithUserDefinedAttributes)


def test_rif11a::exchangefile::specelementwithuserdefinedattributes_constructor_exists():
    assert callable(rif11a::ExchangeFile::SpecElementWithUserDefinedAttributes.__init__)


def test_rif11a::exchangefile::specelementwithuserdefinedattributes_constructor_args():
    sig = inspect.signature(rif11a::ExchangeFile::SpecElementWithUserDefinedAttributes.__init__)
    params = list(sig.parameters.keys())



def test_exchangefile::spechierarchy_is_not_abstract():
    assert not inspect.isabstract(ExchangeFile::SpecHierarchy)


def test_exchangefile::spechierarchy_constructor_exists():
    assert callable(ExchangeFile::SpecHierarchy.__init__)


def test_exchangefile::spechierarchy_constructor_args():
    sig = inspect.signature(ExchangeFile::SpecHierarchy.__init__)
    params = list(sig.parameters.keys())



def test_exchangefile::specrelation_is_not_abstract():
    assert not inspect.isabstract(ExchangeFile::SpecRelation)


def test_exchangefile::specrelation_constructor_exists():
    assert callable(ExchangeFile::SpecRelation.__init__)


def test_exchangefile::specrelation_constructor_args():
    sig = inspect.signature(ExchangeFile::SpecRelation.__init__)
    params = list(sig.parameters.keys())



def test_rif11a::exchangefile::relationgroup_is_not_abstract():
    assert not inspect.isabstract(rif11a::ExchangeFile::RelationGroup)


def test_rif11a::exchangefile::relationgroup_constructor_exists():
    assert callable(rif11a::ExchangeFile::RelationGroup.__init__)


def test_rif11a::exchangefile::relationgroup_constructor_args():
    sig = inspect.signature(rif11a::ExchangeFile::RelationGroup.__init__)
    params = list(sig.parameters.keys())



def test_exchangefile::relationgroup_is_not_abstract():
    assert not inspect.isabstract(ExchangeFile::RelationGroup)


def test_exchangefile::relationgroup_constructor_exists():
    assert callable(ExchangeFile::RelationGroup.__init__)


def test_exchangefile::relationgroup_constructor_args():
    sig = inspect.signature(ExchangeFile::RelationGroup.__init__)
    params = list(sig.parameters.keys())



def test_exchangefile::specobject_is_not_abstract():
    assert not inspect.isabstract(ExchangeFile::SpecObject)


def test_exchangefile::specobject_constructor_exists():
    assert callable(ExchangeFile::SpecObject.__init__)


def test_exchangefile::specobject_constructor_args():
    sig = inspect.signature(ExchangeFile::SpecObject.__init__)
    params = list(sig.parameters.keys())



def test_rif11a::exchangefile::spechierarchy_is_not_abstract():
    assert not inspect.isabstract(rif11a::ExchangeFile::SpecHierarchy)


def test_rif11a::exchangefile::spechierarchy_constructor_exists():
    assert callable(rif11a::ExchangeFile::SpecHierarchy.__init__)


def test_rif11a::exchangefile::spechierarchy_constructor_args():
    sig = inspect.signature(rif11a::ExchangeFile::SpecHierarchy.__init__)
    params = list(sig.parameters.keys())



def test_specelementwithuserdefinedattributes_is_not_abstract():
    assert not inspect.isabstract(SpecElementWithUserDefinedAttributes)


def test_specelementwithuserdefinedattributes_constructor_exists():
    assert callable(SpecElementWithUserDefinedAttributes.__init__)


def test_specelementwithuserdefinedattributes_constructor_args():
    sig = inspect.signature(SpecElementWithUserDefinedAttributes.__init__)
    params = list(sig.parameters.keys())



def test_rif11a::exchangefile::specrelation_is_not_abstract():
    assert not inspect.isabstract(rif11a::ExchangeFile::SpecRelation)


def test_rif11a::exchangefile::specrelation_constructor_exists():
    assert callable(rif11a::ExchangeFile::SpecRelation.__init__)


def test_rif11a::exchangefile::specrelation_constructor_args():
    sig = inspect.signature(rif11a::ExchangeFile::SpecRelation.__init__)
    params = list(sig.parameters.keys())



def test_rif11a::exchangefile::specgroup_is_not_abstract():
    assert not inspect.isabstract(rif11a::ExchangeFile::SpecGroup)


def test_rif11a::exchangefile::specgroup_constructor_exists():
    assert callable(rif11a::ExchangeFile::SpecGroup.__init__)


def test_rif11a::exchangefile::specgroup_constructor_args():
    sig = inspect.signature(rif11a::ExchangeFile::SpecGroup.__init__)
    params = list(sig.parameters.keys())



def test_rif11a::exchangefile::specobject_is_not_abstract():
    assert not inspect.isabstract(rif11a::ExchangeFile::SpecObject)


def test_rif11a::exchangefile::specobject_constructor_exists():
    assert callable(rif11a::ExchangeFile::SpecObject.__init__)


def test_rif11a::exchangefile::specobject_constructor_args():
    sig = inspect.signature(rif11a::ExchangeFile::SpecObject.__init__)
    params = list(sig.parameters.keys())



def test_rif11a::exchangefile::spechierarchyroot_is_not_abstract():
    assert not inspect.isabstract(rif11a::ExchangeFile::SpecHierarchyRoot)


def test_rif11a::exchangefile::spechierarchyroot_constructor_exists():
    assert callable(rif11a::ExchangeFile::SpecHierarchyRoot.__init__)


def test_rif11a::exchangefile::spechierarchyroot_constructor_args():
    sig = inspect.signature(rif11a::ExchangeFile::SpecHierarchyRoot.__init__)
    params = list(sig.parameters.keys())

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
rif11a::DataTypes::BinaryContent_strategy = st.builds(
    rif11a::DataTypes::BinaryContent,
)
ExchangeFile::AccessPolicy_strategy = st.builds(
    ExchangeFile::AccessPolicy,
)
rif11a::DataTypes::XhtmlContent_strategy = st.builds(
    rif11a::DataTypes::XhtmlContent,
)
rif11a::DataTypes::XmlContent_strategy = st.builds(
    rif11a::DataTypes::XmlContent,
)
DatatypeDefinitionSimple_strategy = st.builds(
    DatatypeDefinitionSimple,
)
rif11a::ExchangeFile::DatatypeDefinitionDate_strategy = st.builds(
    rif11a::ExchangeFile::DatatypeDefinitionDate,
    format=
        safe_text
)
rif11a::ExchangeFile::DatatypeDefinitionBoolean_strategy = st.builds(
    rif11a::ExchangeFile::DatatypeDefinitionBoolean,
)
DatatypeDefinitionComplex_strategy = st.builds(
    DatatypeDefinitionComplex,
)
rif11a::ExchangeFile::DatatypeDefinitionDocument_strategy = st.builds(
    rif11a::ExchangeFile::DatatypeDefinitionDocument,
)
rif11a::ExchangeFile::DatatypeDefinitionBinaryFile_strategy = st.builds(
    rif11a::ExchangeFile::DatatypeDefinitionBinaryFile,
    mimeType=
        safe_text,
    filenameSuffix=
        safe_text,
    formatName=
        safe_text,
    application=
        safe_text
)
DataTypes::XmlContent_strategy = st.builds(
    DataTypes::XmlContent,
)
DataTypes::BinaryContent_strategy = st.builds(
    DataTypes::BinaryContent,
)
rif11a::ExchangeFile::RIF_strategy = st.builds(
    rif11a::ExchangeFile::RIF,
    identifier=
        safe_text,
    creationTime=
        safe_text,
    title=
        safe_text,
    countryCode=
        safe_text,
    version=
        safe_text,
    sourceToolId=
        safe_text,
    comment=
        safe_text,
    author=
        safe_text
)
rif11a::ExchangeFile::DatatypeDefinitionXmlData_strategy = st.builds(
    rif11a::ExchangeFile::DatatypeDefinitionXmlData,
    nameSpaceURI=
        safe_text,
    schemaLocation=
        safe_text
)
rif11a::ExchangeFile::DatatypeDefinitionString_strategy = st.builds(
    rif11a::ExchangeFile::DatatypeDefinitionString,
    maxLength=
        safe_text
)
rif11a::ExchangeFile::DatatypeDefinitionReal_strategy = st.builds(
    rif11a::ExchangeFile::DatatypeDefinitionReal,
    min=
        safe_text,
    max=
        safe_text,
    accuracy=
        safe_text
)
rif11a::ExchangeFile::DatatypeDefinitionInteger_strategy = st.builds(
    rif11a::ExchangeFile::DatatypeDefinitionInteger,
    max=
        safe_text,
    min=
        safe_text
)
ExchangeFile::AttributeDefinitionEnumeration_strategy = st.builds(
    ExchangeFile::AttributeDefinitionEnumeration,
)
rif11a::ExchangeFile::EmbeddedValue_strategy = st.builds(
    rif11a::ExchangeFile::EmbeddedValue,
    otherContent=
        safe_text,
    key=
        safe_text
)
ExchangeFile::EmbeddedValue_strategy = st.builds(
    ExchangeFile::EmbeddedValue,
)
ExchangeFile::EnumValue_strategy = st.builds(
    ExchangeFile::EnumValue,
)
ExchangeFile::AttributeValueEnumeration_strategy = st.builds(
    ExchangeFile::AttributeValueEnumeration,
)
ExchangeFile::DatatypeDefinitionEnumeration_strategy = st.builds(
    ExchangeFile::DatatypeDefinitionEnumeration,
)
DataTypes::XhtmlContent_strategy = st.builds(
    DataTypes::XhtmlContent,
)
ExchangeFile::AttributeDefinitionComplex_strategy = st.builds(
    ExchangeFile::AttributeDefinitionComplex,
)
AttributeValueComplex_strategy = st.builds(
    AttributeValueComplex,
)
rif11a::ExchangeFile::AttributeValueFileReference_strategy = st.builds(
    rif11a::ExchangeFile::AttributeValueFileReference,
    pathToFile=
        safe_text
)
rif11a::ExchangeFile::AttributeValueEmbeddedFile_strategy = st.builds(
    rif11a::ExchangeFile::AttributeValueEmbeddedFile,
)
rif11a::ExchangeFile::AttributeValueXmlData_strategy = st.builds(
    rif11a::ExchangeFile::AttributeValueXmlData,
)
rif11a::ExchangeFile::AttributeValueEmbeddedDocument_strategy = st.builds(
    rif11a::ExchangeFile::AttributeValueEmbeddedDocument,
)
ExchangeFile::AttributeDefinitionSimple_strategy = st.builds(
    ExchangeFile::AttributeDefinitionSimple,
)
ExchangeFile::AttributeValueSimple_strategy = st.builds(
    ExchangeFile::AttributeValueSimple,
)
ExchangeFile::DatatypeDefinitionSimple_strategy = st.builds(
    ExchangeFile::DatatypeDefinitionSimple,
)
ExchangeFile::DatatypeDefinition_strategy = st.builds(
    ExchangeFile::DatatypeDefinition,
)
ExchangeFile::SpecGroup_strategy = st.builds(
    ExchangeFile::SpecGroup,
)
AttributeValue_strategy = st.builds(
    AttributeValue,
)
rif11a::ExchangeFile::AttributeValueSimple_strategy = st.builds(
    rif11a::ExchangeFile::AttributeValueSimple,
    theValue=
        safe_text
)
rif11a::ExchangeFile::AttributeValueEnumeration_strategy = st.builds(
    rif11a::ExchangeFile::AttributeValueEnumeration,
)
rif11a::ExchangeFile::AttributeValueComplex_strategy = st.builds(
    rif11a::ExchangeFile::AttributeValueComplex,
)
DatatypeDefinition_strategy = st.builds(
    DatatypeDefinition,
)
rif11a::ExchangeFile::DatatypeDefinitionSimple_strategy = st.builds(
    rif11a::ExchangeFile::DatatypeDefinitionSimple,
)
rif11a::ExchangeFile::DatatypeDefinitionEnumeration_strategy = st.builds(
    rif11a::ExchangeFile::DatatypeDefinitionEnumeration,
)
rif11a::ExchangeFile::DatatypeDefinitionComplex_strategy = st.builds(
    rif11a::ExchangeFile::DatatypeDefinitionComplex,
    embedded=
        safe_text
)
ExchangeFile::AttributeValueComplex_strategy = st.builds(
    ExchangeFile::AttributeValueComplex,
)
ExchangeFile::DatatypeDefinitionComplex_strategy = st.builds(
    ExchangeFile::DatatypeDefinitionComplex,
)
AttributeDefinition_strategy = st.builds(
    AttributeDefinition,
)
rif11a::ExchangeFile::AttributeDefinitionEnumeration_strategy = st.builds(
    rif11a::ExchangeFile::AttributeDefinitionEnumeration,
    multiValued=
        safe_text
)
rif11a::ExchangeFile::AttributeDefinitionSimple_strategy = st.builds(
    rif11a::ExchangeFile::AttributeDefinitionSimple,
)
rif11a::ExchangeFile::AttributeDefinitionComplex_strategy = st.builds(
    rif11a::ExchangeFile::AttributeDefinitionComplex,
)
ExchangeFile::SpecHierarchyRoot_strategy = st.builds(
    ExchangeFile::SpecHierarchyRoot,
)
ExchangeFile::AttributeDefinition_strategy = st.builds(
    ExchangeFile::AttributeDefinition,
)
rif11a::ExchangeFile::Identifiable_strategy = st.builds(
    rif11a::ExchangeFile::Identifiable,
    lastChange=
        safe_text,
    identifier=
        safe_text,
    desc=
        safe_text,
    longName=
        safe_text
)
ExchangeFile::AttributeValue_strategy = st.builds(
    ExchangeFile::AttributeValue,
)
ExchangeFile::SpecType_strategy = st.builds(
    ExchangeFile::SpecType,
)
Identifiable_strategy = st.builds(
    Identifiable,
)
rif11a::ExchangeFile::AttributeDefinition_strategy = st.builds(
    rif11a::ExchangeFile::AttributeDefinition,
)
rif11a::ExchangeFile::DatatypeDefinition_strategy = st.builds(
    rif11a::ExchangeFile::DatatypeDefinition,
)
rif11a::ExchangeFile::AccessPolicy_strategy = st.builds(
    rif11a::ExchangeFile::AccessPolicy,
    accessMode=
        safe_text
)
rif11a::ExchangeFile::AttributeValue_strategy = st.builds(
    rif11a::ExchangeFile::AttributeValue,
)
rif11a::ExchangeFile::SpecType_strategy = st.builds(
    rif11a::ExchangeFile::SpecType,
)
rif11a::ExchangeFile::EnumValue_strategy = st.builds(
    rif11a::ExchangeFile::EnumValue,
)
rif11a::ExchangeFile::SpecElementWithUserDefinedAttributes_strategy = st.builds(
    rif11a::ExchangeFile::SpecElementWithUserDefinedAttributes,
)
ExchangeFile::SpecHierarchy_strategy = st.builds(
    ExchangeFile::SpecHierarchy,
)
ExchangeFile::SpecRelation_strategy = st.builds(
    ExchangeFile::SpecRelation,
)
rif11a::ExchangeFile::RelationGroup_strategy = st.builds(
    rif11a::ExchangeFile::RelationGroup,
)
ExchangeFile::RelationGroup_strategy = st.builds(
    ExchangeFile::RelationGroup,
)
ExchangeFile::SpecObject_strategy = st.builds(
    ExchangeFile::SpecObject,
)
rif11a::ExchangeFile::SpecHierarchy_strategy = st.builds(
    rif11a::ExchangeFile::SpecHierarchy,
)
SpecElementWithUserDefinedAttributes_strategy = st.builds(
    SpecElementWithUserDefinedAttributes,
)
rif11a::ExchangeFile::SpecRelation_strategy = st.builds(
    rif11a::ExchangeFile::SpecRelation,
)
rif11a::ExchangeFile::SpecGroup_strategy = st.builds(
    rif11a::ExchangeFile::SpecGroup,
)
rif11a::ExchangeFile::SpecObject_strategy = st.builds(
    rif11a::ExchangeFile::SpecObject,
)
rif11a::ExchangeFile::SpecHierarchyRoot_strategy = st.builds(
    rif11a::ExchangeFile::SpecHierarchyRoot,
)

@given(instance=rif11a::DataTypes::BinaryContent_strategy)
@settings(max_examples=50)
def test_rif11a::datatypes::binarycontent_instantiation(instance):
    assert isinstance(instance, rif11a::DataTypes::BinaryContent)

@given(instance=ExchangeFile::AccessPolicy_strategy)
@settings(max_examples=50)
def test_exchangefile::accesspolicy_instantiation(instance):
    assert isinstance(instance, ExchangeFile::AccessPolicy)

@given(instance=rif11a::DataTypes::XhtmlContent_strategy)
@settings(max_examples=50)
def test_rif11a::datatypes::xhtmlcontent_instantiation(instance):
    assert isinstance(instance, rif11a::DataTypes::XhtmlContent)

@given(instance=rif11a::DataTypes::XmlContent_strategy)
@settings(max_examples=50)
def test_rif11a::datatypes::xmlcontent_instantiation(instance):
    assert isinstance(instance, rif11a::DataTypes::XmlContent)

@given(instance=DatatypeDefinitionSimple_strategy)
@settings(max_examples=50)
def test_datatypedefinitionsimple_instantiation(instance):
    assert isinstance(instance, DatatypeDefinitionSimple)

@given(instance=rif11a::ExchangeFile::DatatypeDefinitionDate_strategy)
@settings(max_examples=50)
def test_rif11a::exchangefile::datatypedefinitiondate_instantiation(instance):
    assert isinstance(instance, rif11a::ExchangeFile::DatatypeDefinitionDate)

@given(instance=rif11a::ExchangeFile::DatatypeDefinitionDate_strategy)
def test_rif11a::exchangefile::datatypedefinitiondate_format_type(instance):
    assert isinstance(instance.format, str)


@given(instance=rif11a::ExchangeFile::DatatypeDefinitionDate_strategy)
def test_rif11a::exchangefile::datatypedefinitiondate_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original

@given(instance=rif11a::ExchangeFile::DatatypeDefinitionBoolean_strategy)
@settings(max_examples=50)
def test_rif11a::exchangefile::datatypedefinitionboolean_instantiation(instance):
    assert isinstance(instance, rif11a::ExchangeFile::DatatypeDefinitionBoolean)

@given(instance=DatatypeDefinitionComplex_strategy)
@settings(max_examples=50)
def test_datatypedefinitioncomplex_instantiation(instance):
    assert isinstance(instance, DatatypeDefinitionComplex)

@given(instance=rif11a::ExchangeFile::DatatypeDefinitionDocument_strategy)
@settings(max_examples=50)
def test_rif11a::exchangefile::datatypedefinitiondocument_instantiation(instance):
    assert isinstance(instance, rif11a::ExchangeFile::DatatypeDefinitionDocument)

@given(instance=rif11a::ExchangeFile::DatatypeDefinitionBinaryFile_strategy)
@settings(max_examples=50)
def test_rif11a::exchangefile::datatypedefinitionbinaryfile_instantiation(instance):
    assert isinstance(instance, rif11a::ExchangeFile::DatatypeDefinitionBinaryFile)

@given(instance=rif11a::ExchangeFile::DatatypeDefinitionBinaryFile_strategy)
def test_rif11a::exchangefile::datatypedefinitionbinaryfile_mimeType_type(instance):
    assert isinstance(instance.mimeType, str)


@given(instance=rif11a::ExchangeFile::DatatypeDefinitionBinaryFile_strategy)
def test_rif11a::exchangefile::datatypedefinitionbinaryfile_mimeType_setter(instance):
    original = instance.mimeType
    instance.mimeType = original
    assert instance.mimeType == original

@given(instance=rif11a::ExchangeFile::DatatypeDefinitionBinaryFile_strategy)
def test_rif11a::exchangefile::datatypedefinitionbinaryfile_filenameSuffix_type(instance):
    assert isinstance(instance.filenameSuffix, str)


@given(instance=rif11a::ExchangeFile::DatatypeDefinitionBinaryFile_strategy)
def test_rif11a::exchangefile::datatypedefinitionbinaryfile_filenameSuffix_setter(instance):
    original = instance.filenameSuffix
    instance.filenameSuffix = original
    assert instance.filenameSuffix == original

@given(instance=rif11a::ExchangeFile::DatatypeDefinitionBinaryFile_strategy)
def test_rif11a::exchangefile::datatypedefinitionbinaryfile_formatName_type(instance):
    assert isinstance(instance.formatName, str)


@given(instance=rif11a::ExchangeFile::DatatypeDefinitionBinaryFile_strategy)
def test_rif11a::exchangefile::datatypedefinitionbinaryfile_formatName_setter(instance):
    original = instance.formatName
    instance.formatName = original
    assert instance.formatName == original

@given(instance=rif11a::ExchangeFile::DatatypeDefinitionBinaryFile_strategy)
def test_rif11a::exchangefile::datatypedefinitionbinaryfile_application_type(instance):
    assert isinstance(instance.application, str)


@given(instance=rif11a::ExchangeFile::DatatypeDefinitionBinaryFile_strategy)
def test_rif11a::exchangefile::datatypedefinitionbinaryfile_application_setter(instance):
    original = instance.application
    instance.application = original
    assert instance.application == original

@given(instance=DataTypes::XmlContent_strategy)
@settings(max_examples=50)
def test_datatypes::xmlcontent_instantiation(instance):
    assert isinstance(instance, DataTypes::XmlContent)

@given(instance=DataTypes::BinaryContent_strategy)
@settings(max_examples=50)
def test_datatypes::binarycontent_instantiation(instance):
    assert isinstance(instance, DataTypes::BinaryContent)

@given(instance=rif11a::ExchangeFile::RIF_strategy)
@settings(max_examples=50)
def test_rif11a::exchangefile::rif_instantiation(instance):
    assert isinstance(instance, rif11a::ExchangeFile::RIF)

@given(instance=rif11a::ExchangeFile::RIF_strategy)
def test_rif11a::exchangefile::rif_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=rif11a::ExchangeFile::RIF_strategy)
def test_rif11a::exchangefile::rif_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=rif11a::ExchangeFile::RIF_strategy)
def test_rif11a::exchangefile::rif_creationTime_type(instance):
    assert isinstance(instance.creationTime, str)


@given(instance=rif11a::ExchangeFile::RIF_strategy)
def test_rif11a::exchangefile::rif_creationTime_setter(instance):
    original = instance.creationTime
    instance.creationTime = original
    assert instance.creationTime == original

@given(instance=rif11a::ExchangeFile::RIF_strategy)
def test_rif11a::exchangefile::rif_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=rif11a::ExchangeFile::RIF_strategy)
def test_rif11a::exchangefile::rif_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=rif11a::ExchangeFile::RIF_strategy)
def test_rif11a::exchangefile::rif_countryCode_type(instance):
    assert isinstance(instance.countryCode, str)


@given(instance=rif11a::ExchangeFile::RIF_strategy)
def test_rif11a::exchangefile::rif_countryCode_setter(instance):
    original = instance.countryCode
    instance.countryCode = original
    assert instance.countryCode == original

@given(instance=rif11a::ExchangeFile::RIF_strategy)
def test_rif11a::exchangefile::rif_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=rif11a::ExchangeFile::RIF_strategy)
def test_rif11a::exchangefile::rif_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=rif11a::ExchangeFile::RIF_strategy)
def test_rif11a::exchangefile::rif_sourceToolId_type(instance):
    assert isinstance(instance.sourceToolId, str)


@given(instance=rif11a::ExchangeFile::RIF_strategy)
def test_rif11a::exchangefile::rif_sourceToolId_setter(instance):
    original = instance.sourceToolId
    instance.sourceToolId = original
    assert instance.sourceToolId == original

@given(instance=rif11a::ExchangeFile::RIF_strategy)
def test_rif11a::exchangefile::rif_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=rif11a::ExchangeFile::RIF_strategy)
def test_rif11a::exchangefile::rif_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=rif11a::ExchangeFile::RIF_strategy)
def test_rif11a::exchangefile::rif_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=rif11a::ExchangeFile::RIF_strategy)
def test_rif11a::exchangefile::rif_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=rif11a::ExchangeFile::DatatypeDefinitionXmlData_strategy)
@settings(max_examples=50)
def test_rif11a::exchangefile::datatypedefinitionxmldata_instantiation(instance):
    assert isinstance(instance, rif11a::ExchangeFile::DatatypeDefinitionXmlData)

@given(instance=rif11a::ExchangeFile::DatatypeDefinitionXmlData_strategy)
def test_rif11a::exchangefile::datatypedefinitionxmldata_nameSpaceURI_type(instance):
    assert isinstance(instance.nameSpaceURI, str)


@given(instance=rif11a::ExchangeFile::DatatypeDefinitionXmlData_strategy)
def test_rif11a::exchangefile::datatypedefinitionxmldata_nameSpaceURI_setter(instance):
    original = instance.nameSpaceURI
    instance.nameSpaceURI = original
    assert instance.nameSpaceURI == original

@given(instance=rif11a::ExchangeFile::DatatypeDefinitionXmlData_strategy)
def test_rif11a::exchangefile::datatypedefinitionxmldata_schemaLocation_type(instance):
    assert isinstance(instance.schemaLocation, str)


@given(instance=rif11a::ExchangeFile::DatatypeDefinitionXmlData_strategy)
def test_rif11a::exchangefile::datatypedefinitionxmldata_schemaLocation_setter(instance):
    original = instance.schemaLocation
    instance.schemaLocation = original
    assert instance.schemaLocation == original

@given(instance=rif11a::ExchangeFile::DatatypeDefinitionString_strategy)
@settings(max_examples=50)
def test_rif11a::exchangefile::datatypedefinitionstring_instantiation(instance):
    assert isinstance(instance, rif11a::ExchangeFile::DatatypeDefinitionString)

@given(instance=rif11a::ExchangeFile::DatatypeDefinitionString_strategy)
def test_rif11a::exchangefile::datatypedefinitionstring_maxLength_type(instance):
    assert isinstance(instance.maxLength, str)


@given(instance=rif11a::ExchangeFile::DatatypeDefinitionString_strategy)
def test_rif11a::exchangefile::datatypedefinitionstring_maxLength_setter(instance):
    original = instance.maxLength
    instance.maxLength = original
    assert instance.maxLength == original

@given(instance=rif11a::ExchangeFile::DatatypeDefinitionReal_strategy)
@settings(max_examples=50)
def test_rif11a::exchangefile::datatypedefinitionreal_instantiation(instance):
    assert isinstance(instance, rif11a::ExchangeFile::DatatypeDefinitionReal)

@given(instance=rif11a::ExchangeFile::DatatypeDefinitionReal_strategy)
def test_rif11a::exchangefile::datatypedefinitionreal_min_type(instance):
    assert isinstance(instance.min, str)


@given(instance=rif11a::ExchangeFile::DatatypeDefinitionReal_strategy)
def test_rif11a::exchangefile::datatypedefinitionreal_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=rif11a::ExchangeFile::DatatypeDefinitionReal_strategy)
def test_rif11a::exchangefile::datatypedefinitionreal_max_type(instance):
    assert isinstance(instance.max, str)


@given(instance=rif11a::ExchangeFile::DatatypeDefinitionReal_strategy)
def test_rif11a::exchangefile::datatypedefinitionreal_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=rif11a::ExchangeFile::DatatypeDefinitionReal_strategy)
def test_rif11a::exchangefile::datatypedefinitionreal_accuracy_type(instance):
    assert isinstance(instance.accuracy, str)


@given(instance=rif11a::ExchangeFile::DatatypeDefinitionReal_strategy)
def test_rif11a::exchangefile::datatypedefinitionreal_accuracy_setter(instance):
    original = instance.accuracy
    instance.accuracy = original
    assert instance.accuracy == original

@given(instance=rif11a::ExchangeFile::DatatypeDefinitionInteger_strategy)
@settings(max_examples=50)
def test_rif11a::exchangefile::datatypedefinitioninteger_instantiation(instance):
    assert isinstance(instance, rif11a::ExchangeFile::DatatypeDefinitionInteger)

@given(instance=rif11a::ExchangeFile::DatatypeDefinitionInteger_strategy)
def test_rif11a::exchangefile::datatypedefinitioninteger_max_type(instance):
    assert isinstance(instance.max, str)


@given(instance=rif11a::ExchangeFile::DatatypeDefinitionInteger_strategy)
def test_rif11a::exchangefile::datatypedefinitioninteger_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=rif11a::ExchangeFile::DatatypeDefinitionInteger_strategy)
def test_rif11a::exchangefile::datatypedefinitioninteger_min_type(instance):
    assert isinstance(instance.min, str)


@given(instance=rif11a::ExchangeFile::DatatypeDefinitionInteger_strategy)
def test_rif11a::exchangefile::datatypedefinitioninteger_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=ExchangeFile::AttributeDefinitionEnumeration_strategy)
@settings(max_examples=50)
def test_exchangefile::attributedefinitionenumeration_instantiation(instance):
    assert isinstance(instance, ExchangeFile::AttributeDefinitionEnumeration)

@given(instance=rif11a::ExchangeFile::EmbeddedValue_strategy)
@settings(max_examples=50)
def test_rif11a::exchangefile::embeddedvalue_instantiation(instance):
    assert isinstance(instance, rif11a::ExchangeFile::EmbeddedValue)

@given(instance=rif11a::ExchangeFile::EmbeddedValue_strategy)
def test_rif11a::exchangefile::embeddedvalue_otherContent_type(instance):
    assert isinstance(instance.otherContent, str)


@given(instance=rif11a::ExchangeFile::EmbeddedValue_strategy)
def test_rif11a::exchangefile::embeddedvalue_otherContent_setter(instance):
    original = instance.otherContent
    instance.otherContent = original
    assert instance.otherContent == original

@given(instance=rif11a::ExchangeFile::EmbeddedValue_strategy)
def test_rif11a::exchangefile::embeddedvalue_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=rif11a::ExchangeFile::EmbeddedValue_strategy)
def test_rif11a::exchangefile::embeddedvalue_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=ExchangeFile::EmbeddedValue_strategy)
@settings(max_examples=50)
def test_exchangefile::embeddedvalue_instantiation(instance):
    assert isinstance(instance, ExchangeFile::EmbeddedValue)

@given(instance=ExchangeFile::EnumValue_strategy)
@settings(max_examples=50)
def test_exchangefile::enumvalue_instantiation(instance):
    assert isinstance(instance, ExchangeFile::EnumValue)

@given(instance=ExchangeFile::AttributeValueEnumeration_strategy)
@settings(max_examples=50)
def test_exchangefile::attributevalueenumeration_instantiation(instance):
    assert isinstance(instance, ExchangeFile::AttributeValueEnumeration)

@given(instance=ExchangeFile::DatatypeDefinitionEnumeration_strategy)
@settings(max_examples=50)
def test_exchangefile::datatypedefinitionenumeration_instantiation(instance):
    assert isinstance(instance, ExchangeFile::DatatypeDefinitionEnumeration)

@given(instance=DataTypes::XhtmlContent_strategy)
@settings(max_examples=50)
def test_datatypes::xhtmlcontent_instantiation(instance):
    assert isinstance(instance, DataTypes::XhtmlContent)

@given(instance=ExchangeFile::AttributeDefinitionComplex_strategy)
@settings(max_examples=50)
def test_exchangefile::attributedefinitioncomplex_instantiation(instance):
    assert isinstance(instance, ExchangeFile::AttributeDefinitionComplex)

@given(instance=AttributeValueComplex_strategy)
@settings(max_examples=50)
def test_attributevaluecomplex_instantiation(instance):
    assert isinstance(instance, AttributeValueComplex)

@given(instance=rif11a::ExchangeFile::AttributeValueFileReference_strategy)
@settings(max_examples=50)
def test_rif11a::exchangefile::attributevaluefilereference_instantiation(instance):
    assert isinstance(instance, rif11a::ExchangeFile::AttributeValueFileReference)

@given(instance=rif11a::ExchangeFile::AttributeValueFileReference_strategy)
def test_rif11a::exchangefile::attributevaluefilereference_pathToFile_type(instance):
    assert isinstance(instance.pathToFile, str)


@given(instance=rif11a::ExchangeFile::AttributeValueFileReference_strategy)
def test_rif11a::exchangefile::attributevaluefilereference_pathToFile_setter(instance):
    original = instance.pathToFile
    instance.pathToFile = original
    assert instance.pathToFile == original

@given(instance=rif11a::ExchangeFile::AttributeValueEmbeddedFile_strategy)
@settings(max_examples=50)
def test_rif11a::exchangefile::attributevalueembeddedfile_instantiation(instance):
    assert isinstance(instance, rif11a::ExchangeFile::AttributeValueEmbeddedFile)

@given(instance=rif11a::ExchangeFile::AttributeValueXmlData_strategy)
@settings(max_examples=50)
def test_rif11a::exchangefile::attributevaluexmldata_instantiation(instance):
    assert isinstance(instance, rif11a::ExchangeFile::AttributeValueXmlData)

@given(instance=rif11a::ExchangeFile::AttributeValueEmbeddedDocument_strategy)
@settings(max_examples=50)
def test_rif11a::exchangefile::attributevalueembeddeddocument_instantiation(instance):
    assert isinstance(instance, rif11a::ExchangeFile::AttributeValueEmbeddedDocument)

@given(instance=ExchangeFile::AttributeDefinitionSimple_strategy)
@settings(max_examples=50)
def test_exchangefile::attributedefinitionsimple_instantiation(instance):
    assert isinstance(instance, ExchangeFile::AttributeDefinitionSimple)

@given(instance=ExchangeFile::AttributeValueSimple_strategy)
@settings(max_examples=50)
def test_exchangefile::attributevaluesimple_instantiation(instance):
    assert isinstance(instance, ExchangeFile::AttributeValueSimple)

@given(instance=ExchangeFile::DatatypeDefinitionSimple_strategy)
@settings(max_examples=50)
def test_exchangefile::datatypedefinitionsimple_instantiation(instance):
    assert isinstance(instance, ExchangeFile::DatatypeDefinitionSimple)

@given(instance=ExchangeFile::DatatypeDefinition_strategy)
@settings(max_examples=50)
def test_exchangefile::datatypedefinition_instantiation(instance):
    assert isinstance(instance, ExchangeFile::DatatypeDefinition)

@given(instance=ExchangeFile::SpecGroup_strategy)
@settings(max_examples=50)
def test_exchangefile::specgroup_instantiation(instance):
    assert isinstance(instance, ExchangeFile::SpecGroup)

@given(instance=AttributeValue_strategy)
@settings(max_examples=50)
def test_attributevalue_instantiation(instance):
    assert isinstance(instance, AttributeValue)

@given(instance=rif11a::ExchangeFile::AttributeValueSimple_strategy)
@settings(max_examples=50)
def test_rif11a::exchangefile::attributevaluesimple_instantiation(instance):
    assert isinstance(instance, rif11a::ExchangeFile::AttributeValueSimple)

@given(instance=rif11a::ExchangeFile::AttributeValueSimple_strategy)
def test_rif11a::exchangefile::attributevaluesimple_theValue_type(instance):
    assert isinstance(instance.theValue, str)


@given(instance=rif11a::ExchangeFile::AttributeValueSimple_strategy)
def test_rif11a::exchangefile::attributevaluesimple_theValue_setter(instance):
    original = instance.theValue
    instance.theValue = original
    assert instance.theValue == original

@given(instance=rif11a::ExchangeFile::AttributeValueEnumeration_strategy)
@settings(max_examples=50)
def test_rif11a::exchangefile::attributevalueenumeration_instantiation(instance):
    assert isinstance(instance, rif11a::ExchangeFile::AttributeValueEnumeration)

@given(instance=rif11a::ExchangeFile::AttributeValueComplex_strategy)
@settings(max_examples=50)
def test_rif11a::exchangefile::attributevaluecomplex_instantiation(instance):
    assert isinstance(instance, rif11a::ExchangeFile::AttributeValueComplex)

@given(instance=DatatypeDefinition_strategy)
@settings(max_examples=50)
def test_datatypedefinition_instantiation(instance):
    assert isinstance(instance, DatatypeDefinition)

@given(instance=rif11a::ExchangeFile::DatatypeDefinitionSimple_strategy)
@settings(max_examples=50)
def test_rif11a::exchangefile::datatypedefinitionsimple_instantiation(instance):
    assert isinstance(instance, rif11a::ExchangeFile::DatatypeDefinitionSimple)

@given(instance=rif11a::ExchangeFile::DatatypeDefinitionEnumeration_strategy)
@settings(max_examples=50)
def test_rif11a::exchangefile::datatypedefinitionenumeration_instantiation(instance):
    assert isinstance(instance, rif11a::ExchangeFile::DatatypeDefinitionEnumeration)

@given(instance=rif11a::ExchangeFile::DatatypeDefinitionComplex_strategy)
@settings(max_examples=50)
def test_rif11a::exchangefile::datatypedefinitioncomplex_instantiation(instance):
    assert isinstance(instance, rif11a::ExchangeFile::DatatypeDefinitionComplex)

@given(instance=rif11a::ExchangeFile::DatatypeDefinitionComplex_strategy)
def test_rif11a::exchangefile::datatypedefinitioncomplex_embedded_type(instance):
    assert isinstance(instance.embedded, str)


@given(instance=rif11a::ExchangeFile::DatatypeDefinitionComplex_strategy)
def test_rif11a::exchangefile::datatypedefinitioncomplex_embedded_setter(instance):
    original = instance.embedded
    instance.embedded = original
    assert instance.embedded == original

@given(instance=ExchangeFile::AttributeValueComplex_strategy)
@settings(max_examples=50)
def test_exchangefile::attributevaluecomplex_instantiation(instance):
    assert isinstance(instance, ExchangeFile::AttributeValueComplex)

@given(instance=ExchangeFile::DatatypeDefinitionComplex_strategy)
@settings(max_examples=50)
def test_exchangefile::datatypedefinitioncomplex_instantiation(instance):
    assert isinstance(instance, ExchangeFile::DatatypeDefinitionComplex)

@given(instance=AttributeDefinition_strategy)
@settings(max_examples=50)
def test_attributedefinition_instantiation(instance):
    assert isinstance(instance, AttributeDefinition)

@given(instance=rif11a::ExchangeFile::AttributeDefinitionEnumeration_strategy)
@settings(max_examples=50)
def test_rif11a::exchangefile::attributedefinitionenumeration_instantiation(instance):
    assert isinstance(instance, rif11a::ExchangeFile::AttributeDefinitionEnumeration)

@given(instance=rif11a::ExchangeFile::AttributeDefinitionEnumeration_strategy)
def test_rif11a::exchangefile::attributedefinitionenumeration_multiValued_type(instance):
    assert isinstance(instance.multiValued, str)


@given(instance=rif11a::ExchangeFile::AttributeDefinitionEnumeration_strategy)
def test_rif11a::exchangefile::attributedefinitionenumeration_multiValued_setter(instance):
    original = instance.multiValued
    instance.multiValued = original
    assert instance.multiValued == original

@given(instance=rif11a::ExchangeFile::AttributeDefinitionSimple_strategy)
@settings(max_examples=50)
def test_rif11a::exchangefile::attributedefinitionsimple_instantiation(instance):
    assert isinstance(instance, rif11a::ExchangeFile::AttributeDefinitionSimple)

@given(instance=rif11a::ExchangeFile::AttributeDefinitionComplex_strategy)
@settings(max_examples=50)
def test_rif11a::exchangefile::attributedefinitioncomplex_instantiation(instance):
    assert isinstance(instance, rif11a::ExchangeFile::AttributeDefinitionComplex)

@given(instance=ExchangeFile::SpecHierarchyRoot_strategy)
@settings(max_examples=50)
def test_exchangefile::spechierarchyroot_instantiation(instance):
    assert isinstance(instance, ExchangeFile::SpecHierarchyRoot)

@given(instance=ExchangeFile::AttributeDefinition_strategy)
@settings(max_examples=50)
def test_exchangefile::attributedefinition_instantiation(instance):
    assert isinstance(instance, ExchangeFile::AttributeDefinition)

@given(instance=rif11a::ExchangeFile::Identifiable_strategy)
@settings(max_examples=50)
def test_rif11a::exchangefile::identifiable_instantiation(instance):
    assert isinstance(instance, rif11a::ExchangeFile::Identifiable)

@given(instance=rif11a::ExchangeFile::Identifiable_strategy)
def test_rif11a::exchangefile::identifiable_lastChange_type(instance):
    assert isinstance(instance.lastChange, str)


@given(instance=rif11a::ExchangeFile::Identifiable_strategy)
def test_rif11a::exchangefile::identifiable_lastChange_setter(instance):
    original = instance.lastChange
    instance.lastChange = original
    assert instance.lastChange == original

@given(instance=rif11a::ExchangeFile::Identifiable_strategy)
def test_rif11a::exchangefile::identifiable_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=rif11a::ExchangeFile::Identifiable_strategy)
def test_rif11a::exchangefile::identifiable_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=rif11a::ExchangeFile::Identifiable_strategy)
def test_rif11a::exchangefile::identifiable_desc_type(instance):
    assert isinstance(instance.desc, str)


@given(instance=rif11a::ExchangeFile::Identifiable_strategy)
def test_rif11a::exchangefile::identifiable_desc_setter(instance):
    original = instance.desc
    instance.desc = original
    assert instance.desc == original

@given(instance=rif11a::ExchangeFile::Identifiable_strategy)
def test_rif11a::exchangefile::identifiable_longName_type(instance):
    assert isinstance(instance.longName, str)


@given(instance=rif11a::ExchangeFile::Identifiable_strategy)
def test_rif11a::exchangefile::identifiable_longName_setter(instance):
    original = instance.longName
    instance.longName = original
    assert instance.longName == original

@given(instance=ExchangeFile::AttributeValue_strategy)
@settings(max_examples=50)
def test_exchangefile::attributevalue_instantiation(instance):
    assert isinstance(instance, ExchangeFile::AttributeValue)

@given(instance=ExchangeFile::SpecType_strategy)
@settings(max_examples=50)
def test_exchangefile::spectype_instantiation(instance):
    assert isinstance(instance, ExchangeFile::SpecType)

@given(instance=Identifiable_strategy)
@settings(max_examples=50)
def test_identifiable_instantiation(instance):
    assert isinstance(instance, Identifiable)

@given(instance=rif11a::ExchangeFile::AttributeDefinition_strategy)
@settings(max_examples=50)
def test_rif11a::exchangefile::attributedefinition_instantiation(instance):
    assert isinstance(instance, rif11a::ExchangeFile::AttributeDefinition)

@given(instance=rif11a::ExchangeFile::DatatypeDefinition_strategy)
@settings(max_examples=50)
def test_rif11a::exchangefile::datatypedefinition_instantiation(instance):
    assert isinstance(instance, rif11a::ExchangeFile::DatatypeDefinition)

@given(instance=rif11a::ExchangeFile::AccessPolicy_strategy)
@settings(max_examples=50)
def test_rif11a::exchangefile::accesspolicy_instantiation(instance):
    assert isinstance(instance, rif11a::ExchangeFile::AccessPolicy)

@given(instance=rif11a::ExchangeFile::AccessPolicy_strategy)
def test_rif11a::exchangefile::accesspolicy_accessMode_type(instance):
    assert isinstance(instance.accessMode, str)


@given(instance=rif11a::ExchangeFile::AccessPolicy_strategy)
def test_rif11a::exchangefile::accesspolicy_accessMode_setter(instance):
    original = instance.accessMode
    instance.accessMode = original
    assert instance.accessMode == original

@given(instance=rif11a::ExchangeFile::AttributeValue_strategy)
@settings(max_examples=50)
def test_rif11a::exchangefile::attributevalue_instantiation(instance):
    assert isinstance(instance, rif11a::ExchangeFile::AttributeValue)

@given(instance=rif11a::ExchangeFile::SpecType_strategy)
@settings(max_examples=50)
def test_rif11a::exchangefile::spectype_instantiation(instance):
    assert isinstance(instance, rif11a::ExchangeFile::SpecType)

@given(instance=rif11a::ExchangeFile::EnumValue_strategy)
@settings(max_examples=50)
def test_rif11a::exchangefile::enumvalue_instantiation(instance):
    assert isinstance(instance, rif11a::ExchangeFile::EnumValue)

@given(instance=rif11a::ExchangeFile::SpecElementWithUserDefinedAttributes_strategy)
@settings(max_examples=50)
def test_rif11a::exchangefile::specelementwithuserdefinedattributes_instantiation(instance):
    assert isinstance(instance, rif11a::ExchangeFile::SpecElementWithUserDefinedAttributes)

@given(instance=ExchangeFile::SpecHierarchy_strategy)
@settings(max_examples=50)
def test_exchangefile::spechierarchy_instantiation(instance):
    assert isinstance(instance, ExchangeFile::SpecHierarchy)

@given(instance=ExchangeFile::SpecRelation_strategy)
@settings(max_examples=50)
def test_exchangefile::specrelation_instantiation(instance):
    assert isinstance(instance, ExchangeFile::SpecRelation)

@given(instance=rif11a::ExchangeFile::RelationGroup_strategy)
@settings(max_examples=50)
def test_rif11a::exchangefile::relationgroup_instantiation(instance):
    assert isinstance(instance, rif11a::ExchangeFile::RelationGroup)

@given(instance=ExchangeFile::RelationGroup_strategy)
@settings(max_examples=50)
def test_exchangefile::relationgroup_instantiation(instance):
    assert isinstance(instance, ExchangeFile::RelationGroup)

@given(instance=ExchangeFile::SpecObject_strategy)
@settings(max_examples=50)
def test_exchangefile::specobject_instantiation(instance):
    assert isinstance(instance, ExchangeFile::SpecObject)

@given(instance=rif11a::ExchangeFile::SpecHierarchy_strategy)
@settings(max_examples=50)
def test_rif11a::exchangefile::spechierarchy_instantiation(instance):
    assert isinstance(instance, rif11a::ExchangeFile::SpecHierarchy)

@given(instance=SpecElementWithUserDefinedAttributes_strategy)
@settings(max_examples=50)
def test_specelementwithuserdefinedattributes_instantiation(instance):
    assert isinstance(instance, SpecElementWithUserDefinedAttributes)

@given(instance=rif11a::ExchangeFile::SpecRelation_strategy)
@settings(max_examples=50)
def test_rif11a::exchangefile::specrelation_instantiation(instance):
    assert isinstance(instance, rif11a::ExchangeFile::SpecRelation)

@given(instance=rif11a::ExchangeFile::SpecGroup_strategy)
@settings(max_examples=50)
def test_rif11a::exchangefile::specgroup_instantiation(instance):
    assert isinstance(instance, rif11a::ExchangeFile::SpecGroup)

@given(instance=rif11a::ExchangeFile::SpecObject_strategy)
@settings(max_examples=50)
def test_rif11a::exchangefile::specobject_instantiation(instance):
    assert isinstance(instance, rif11a::ExchangeFile::SpecObject)

@given(instance=rif11a::ExchangeFile::SpecHierarchyRoot_strategy)
@settings(max_examples=50)
def test_rif11a::exchangefile::spechierarchyroot_instantiation(instance):
    assert isinstance(instance, rif11a::ExchangeFile::SpecHierarchyRoot)
