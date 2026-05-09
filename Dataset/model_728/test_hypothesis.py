import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    rif12::DataTypes::XmlContent,
    rif12::DataTypes::XhtmlContent,
    rif12::DataTypes::BinaryContent,
    rif12::ExchangeFile::RIFToolExtension,
    rif12::ExchangeFile::RIFHeader,
    RIFToolExtension,
    RIFContent,
    RIFHeader,
    rif12::ExchangeFile::RIF,
    AccessPolicy,
    rif12::ExchangeFile::RIFContent,
    DataTypes::BinaryContent,
    DataTypes::XhtmlContent,
    AttributeDefinitionComplex,
    AttributeDefinitionSimple,
    AttributeValueSimple,
    DataTypes::XmlContent,
    EmbeddedValue,
    EnumValue,
    AttributeValueEnumeration,
    DatatypeDefinitionEnumeration,
    AttributeValueComplex,
    rif12::ExchangeFile::AttributeValueEmbeddedDocument,
    rif12::ExchangeFile::AttributeValueXmlData,
    rif12::ExchangeFile::AttributeValueFileReference,
    rif12::ExchangeFile::AttributeValueEmbeddedFile,
    DatatypeDefinitionComplex,
    rif12::ExchangeFile::DatatypeDefinitionXmlData,
    rif12::ExchangeFile::DatatypeDefinitionBinaryFile,
    rif12::ExchangeFile::DatatypeDefinitionDocument,
    DatatypeDefinitionSimple,
    rif12::ExchangeFile::DatatypeDefinitionInteger,
    rif12::ExchangeFile::DatatypeDefinitionBoolean,
    rif12::ExchangeFile::DatatypeDefinitionDate,
    rif12::ExchangeFile::DatatypeDefinitionString,
    rif12::ExchangeFile::DatatypeDefinitionReal,
    AttributeDefinitionEnumeration,
    rif12::ExchangeFile::EmbeddedValue,
    DatatypeDefinition,
    rif12::ExchangeFile::DatatypeDefinitionComplex,
    rif12::ExchangeFile::DatatypeDefinitionSimple,
    rif12::ExchangeFile::DatatypeDefinitionEnumeration,
    SpecGroup,
    SpecGroupHierarchyRoot,
    SpecRelation,
    SpecGroupHierarchy,
    SpecHierarchyRoot,
    SpecObject,
    AttributeDefinition,
    rif12::ExchangeFile::AttributeDefinitionComplex,
    rif12::ExchangeFile::AttributeDefinitionSimple,
    rif12::ExchangeFile::AttributeDefinitionEnumeration,
    rif12::ExchangeFile::Identifiable,
    RelationGroup,
    SpecElementWithUserDefinedAttributes,
    rif12::ExchangeFile::SpecGroupHierarchyRoot,
    rif12::ExchangeFile::SpecGroup,
    rif12::ExchangeFile::SpecRelation,
    rif12::ExchangeFile::SpecObject,
    rif12::ExchangeFile::SpecHierarchyRoot,
    AttributeValue,
    rif12::ExchangeFile::AttributeValueComplex,
    rif12::ExchangeFile::AttributeValueSimple,
    rif12::ExchangeFile::AttributeValueEnumeration,
    SpecType,
    Identifiable,
    rif12::ExchangeFile::AccessPolicy,
    rif12::ExchangeFile::EnumValue,
    rif12::ExchangeFile::SpecType,
    rif12::ExchangeFile::AttributeValue,
    rif12::ExchangeFile::DatatypeDefinition,
    rif12::ExchangeFile::SpecHierarchy,
    rif12::ExchangeFile::SpecGroupHierarchy,
    rif12::ExchangeFile::AttributeDefinition,
    rif12::ExchangeFile::RelationGroup,
    rif12::ExchangeFile::SpecElementWithUserDefinedAttributes,
    SpecHierarchy,
    AccessPolicyAccessModeEnum,
    DatatypeDefinitionDateFormatEnum,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rif12::datatypes::xmlcontent_is_not_abstract():
    assert not inspect.isabstract(rif12::DataTypes::XmlContent)


def test_rif12::datatypes::xmlcontent_constructor_exists():
    assert callable(rif12::DataTypes::XmlContent.__init__)


def test_rif12::datatypes::xmlcontent_constructor_args():
    sig = inspect.signature(rif12::DataTypes::XmlContent.__init__)
    params = list(sig.parameters.keys())



def test_rif12::datatypes::xhtmlcontent_is_not_abstract():
    assert not inspect.isabstract(rif12::DataTypes::XhtmlContent)


def test_rif12::datatypes::xhtmlcontent_constructor_exists():
    assert callable(rif12::DataTypes::XhtmlContent.__init__)


def test_rif12::datatypes::xhtmlcontent_constructor_args():
    sig = inspect.signature(rif12::DataTypes::XhtmlContent.__init__)
    params = list(sig.parameters.keys())



def test_rif12::datatypes::binarycontent_is_not_abstract():
    assert not inspect.isabstract(rif12::DataTypes::BinaryContent)


def test_rif12::datatypes::binarycontent_constructor_exists():
    assert callable(rif12::DataTypes::BinaryContent.__init__)


def test_rif12::datatypes::binarycontent_constructor_args():
    sig = inspect.signature(rif12::DataTypes::BinaryContent.__init__)
    params = list(sig.parameters.keys())



def test_rif12::exchangefile::riftoolextension_is_not_abstract():
    assert not inspect.isabstract(rif12::ExchangeFile::RIFToolExtension)


def test_rif12::exchangefile::riftoolextension_constructor_exists():
    assert callable(rif12::ExchangeFile::RIFToolExtension.__init__)


def test_rif12::exchangefile::riftoolextension_constructor_args():
    sig = inspect.signature(rif12::ExchangeFile::RIFToolExtension.__init__)
    params = list(sig.parameters.keys())



def test_rif12::exchangefile::rifheader_is_not_abstract():
    assert not inspect.isabstract(rif12::ExchangeFile::RIFHeader)


def test_rif12::exchangefile::rifheader_constructor_exists():
    assert callable(rif12::ExchangeFile::RIFHeader.__init__)


def test_rif12::exchangefile::rifheader_constructor_args():
    sig = inspect.signature(rif12::ExchangeFile::RIFHeader.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "creationTime" in params, "Missing parameter 'creationTime'"
    assert "sourceToolId" in params, "Missing parameter 'sourceToolId'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "author" in params, "Missing parameter 'author'"
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_rif12::exchangefile::rifheader_has_title():
    assert hasattr(rif12::ExchangeFile::RIFHeader, "title")
    descriptor = None
    for klass in rif12::ExchangeFile::RIFHeader.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_rif12::exchangefile::rifheader_has_creationTime():
    assert hasattr(rif12::ExchangeFile::RIFHeader, "creationTime")
    descriptor = None
    for klass in rif12::ExchangeFile::RIFHeader.__mro__:
        if "creationTime" in klass.__dict__:
            descriptor = klass.__dict__["creationTime"]
            break
    assert isinstance(descriptor, property)

def test_rif12::exchangefile::rifheader_has_sourceToolId():
    assert hasattr(rif12::ExchangeFile::RIFHeader, "sourceToolId")
    descriptor = None
    for klass in rif12::ExchangeFile::RIFHeader.__mro__:
        if "sourceToolId" in klass.__dict__:
            descriptor = klass.__dict__["sourceToolId"]
            break
    assert isinstance(descriptor, property)

def test_rif12::exchangefile::rifheader_has_comment():
    assert hasattr(rif12::ExchangeFile::RIFHeader, "comment")
    descriptor = None
    for klass in rif12::ExchangeFile::RIFHeader.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_rif12::exchangefile::rifheader_has_author():
    assert hasattr(rif12::ExchangeFile::RIFHeader, "author")
    descriptor = None
    for klass in rif12::ExchangeFile::RIFHeader.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_rif12::exchangefile::rifheader_has_identifier():
    assert hasattr(rif12::ExchangeFile::RIFHeader, "identifier")
    descriptor = None
    for klass in rif12::ExchangeFile::RIFHeader.__mro__:
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



def test_rif12::exchangefile::rif_is_not_abstract():
    assert not inspect.isabstract(rif12::ExchangeFile::RIF)


def test_rif12::exchangefile::rif_constructor_exists():
    assert callable(rif12::ExchangeFile::RIF.__init__)


def test_rif12::exchangefile::rif_constructor_args():
    sig = inspect.signature(rif12::ExchangeFile::RIF.__init__)
    params = list(sig.parameters.keys())



def test_accesspolicy_is_not_abstract():
    assert not inspect.isabstract(AccessPolicy)


def test_accesspolicy_constructor_exists():
    assert callable(AccessPolicy.__init__)


def test_accesspolicy_constructor_args():
    sig = inspect.signature(AccessPolicy.__init__)
    params = list(sig.parameters.keys())



def test_rif12::exchangefile::rifcontent_is_not_abstract():
    assert not inspect.isabstract(rif12::ExchangeFile::RIFContent)


def test_rif12::exchangefile::rifcontent_constructor_exists():
    assert callable(rif12::ExchangeFile::RIFContent.__init__)


def test_rif12::exchangefile::rifcontent_constructor_args():
    sig = inspect.signature(rif12::ExchangeFile::RIFContent.__init__)
    params = list(sig.parameters.keys())



def test_datatypes::binarycontent_is_not_abstract():
    assert not inspect.isabstract(DataTypes::BinaryContent)


def test_datatypes::binarycontent_constructor_exists():
    assert callable(DataTypes::BinaryContent.__init__)


def test_datatypes::binarycontent_constructor_args():
    sig = inspect.signature(DataTypes::BinaryContent.__init__)
    params = list(sig.parameters.keys())



def test_datatypes::xhtmlcontent_is_not_abstract():
    assert not inspect.isabstract(DataTypes::XhtmlContent)


def test_datatypes::xhtmlcontent_constructor_exists():
    assert callable(DataTypes::XhtmlContent.__init__)


def test_datatypes::xhtmlcontent_constructor_args():
    sig = inspect.signature(DataTypes::XhtmlContent.__init__)
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



def test_attributevaluesimple_is_not_abstract():
    assert not inspect.isabstract(AttributeValueSimple)


def test_attributevaluesimple_constructor_exists():
    assert callable(AttributeValueSimple.__init__)


def test_attributevaluesimple_constructor_args():
    sig = inspect.signature(AttributeValueSimple.__init__)
    params = list(sig.parameters.keys())



def test_datatypes::xmlcontent_is_not_abstract():
    assert not inspect.isabstract(DataTypes::XmlContent)


def test_datatypes::xmlcontent_constructor_exists():
    assert callable(DataTypes::XmlContent.__init__)


def test_datatypes::xmlcontent_constructor_args():
    sig = inspect.signature(DataTypes::XmlContent.__init__)
    params = list(sig.parameters.keys())



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



def test_attributevaluecomplex_is_not_abstract():
    assert not inspect.isabstract(AttributeValueComplex)


def test_attributevaluecomplex_constructor_exists():
    assert callable(AttributeValueComplex.__init__)


def test_attributevaluecomplex_constructor_args():
    sig = inspect.signature(AttributeValueComplex.__init__)
    params = list(sig.parameters.keys())



def test_rif12::exchangefile::attributevalueembeddeddocument_is_not_abstract():
    assert not inspect.isabstract(rif12::ExchangeFile::AttributeValueEmbeddedDocument)


def test_rif12::exchangefile::attributevalueembeddeddocument_constructor_exists():
    assert callable(rif12::ExchangeFile::AttributeValueEmbeddedDocument.__init__)


def test_rif12::exchangefile::attributevalueembeddeddocument_constructor_args():
    sig = inspect.signature(rif12::ExchangeFile::AttributeValueEmbeddedDocument.__init__)
    params = list(sig.parameters.keys())



def test_rif12::exchangefile::attributevaluexmldata_is_not_abstract():
    assert not inspect.isabstract(rif12::ExchangeFile::AttributeValueXmlData)


def test_rif12::exchangefile::attributevaluexmldata_constructor_exists():
    assert callable(rif12::ExchangeFile::AttributeValueXmlData.__init__)


def test_rif12::exchangefile::attributevaluexmldata_constructor_args():
    sig = inspect.signature(rif12::ExchangeFile::AttributeValueXmlData.__init__)
    params = list(sig.parameters.keys())



def test_rif12::exchangefile::attributevaluefilereference_is_not_abstract():
    assert not inspect.isabstract(rif12::ExchangeFile::AttributeValueFileReference)


def test_rif12::exchangefile::attributevaluefilereference_constructor_exists():
    assert callable(rif12::ExchangeFile::AttributeValueFileReference.__init__)


def test_rif12::exchangefile::attributevaluefilereference_constructor_args():
    sig = inspect.signature(rif12::ExchangeFile::AttributeValueFileReference.__init__)
    params = list(sig.parameters.keys())
    assert "pathToFile" in params, "Missing parameter 'pathToFile'"

def test_rif12::exchangefile::attributevaluefilereference_has_pathToFile():
    assert hasattr(rif12::ExchangeFile::AttributeValueFileReference, "pathToFile")
    descriptor = None
    for klass in rif12::ExchangeFile::AttributeValueFileReference.__mro__:
        if "pathToFile" in klass.__dict__:
            descriptor = klass.__dict__["pathToFile"]
            break
    assert isinstance(descriptor, property)



def test_rif12::exchangefile::attributevalueembeddedfile_is_not_abstract():
    assert not inspect.isabstract(rif12::ExchangeFile::AttributeValueEmbeddedFile)


def test_rif12::exchangefile::attributevalueembeddedfile_constructor_exists():
    assert callable(rif12::ExchangeFile::AttributeValueEmbeddedFile.__init__)


def test_rif12::exchangefile::attributevalueembeddedfile_constructor_args():
    sig = inspect.signature(rif12::ExchangeFile::AttributeValueEmbeddedFile.__init__)
    params = list(sig.parameters.keys())



def test_datatypedefinitioncomplex_is_not_abstract():
    assert not inspect.isabstract(DatatypeDefinitionComplex)


def test_datatypedefinitioncomplex_constructor_exists():
    assert callable(DatatypeDefinitionComplex.__init__)


def test_datatypedefinitioncomplex_constructor_args():
    sig = inspect.signature(DatatypeDefinitionComplex.__init__)
    params = list(sig.parameters.keys())



def test_rif12::exchangefile::datatypedefinitionxmldata_is_not_abstract():
    assert not inspect.isabstract(rif12::ExchangeFile::DatatypeDefinitionXmlData)


def test_rif12::exchangefile::datatypedefinitionxmldata_constructor_exists():
    assert callable(rif12::ExchangeFile::DatatypeDefinitionXmlData.__init__)


def test_rif12::exchangefile::datatypedefinitionxmldata_constructor_args():
    sig = inspect.signature(rif12::ExchangeFile::DatatypeDefinitionXmlData.__init__)
    params = list(sig.parameters.keys())
    assert "nameSpaceURI" in params, "Missing parameter 'nameSpaceURI'"
    assert "schemaLocation" in params, "Missing parameter 'schemaLocation'"

def test_rif12::exchangefile::datatypedefinitionxmldata_has_nameSpaceURI():
    assert hasattr(rif12::ExchangeFile::DatatypeDefinitionXmlData, "nameSpaceURI")
    descriptor = None
    for klass in rif12::ExchangeFile::DatatypeDefinitionXmlData.__mro__:
        if "nameSpaceURI" in klass.__dict__:
            descriptor = klass.__dict__["nameSpaceURI"]
            break
    assert isinstance(descriptor, property)

def test_rif12::exchangefile::datatypedefinitionxmldata_has_schemaLocation():
    assert hasattr(rif12::ExchangeFile::DatatypeDefinitionXmlData, "schemaLocation")
    descriptor = None
    for klass in rif12::ExchangeFile::DatatypeDefinitionXmlData.__mro__:
        if "schemaLocation" in klass.__dict__:
            descriptor = klass.__dict__["schemaLocation"]
            break
    assert isinstance(descriptor, property)



def test_rif12::exchangefile::datatypedefinitionbinaryfile_is_not_abstract():
    assert not inspect.isabstract(rif12::ExchangeFile::DatatypeDefinitionBinaryFile)


def test_rif12::exchangefile::datatypedefinitionbinaryfile_constructor_exists():
    assert callable(rif12::ExchangeFile::DatatypeDefinitionBinaryFile.__init__)


def test_rif12::exchangefile::datatypedefinitionbinaryfile_constructor_args():
    sig = inspect.signature(rif12::ExchangeFile::DatatypeDefinitionBinaryFile.__init__)
    params = list(sig.parameters.keys())
    assert "mimeType" in params, "Missing parameter 'mimeType'"
    assert "formatName" in params, "Missing parameter 'formatName'"
    assert "filenameSuffix" in params, "Missing parameter 'filenameSuffix'"
    assert "application" in params, "Missing parameter 'application'"

def test_rif12::exchangefile::datatypedefinitionbinaryfile_has_mimeType():
    assert hasattr(rif12::ExchangeFile::DatatypeDefinitionBinaryFile, "mimeType")
    descriptor = None
    for klass in rif12::ExchangeFile::DatatypeDefinitionBinaryFile.__mro__:
        if "mimeType" in klass.__dict__:
            descriptor = klass.__dict__["mimeType"]
            break
    assert isinstance(descriptor, property)

def test_rif12::exchangefile::datatypedefinitionbinaryfile_has_formatName():
    assert hasattr(rif12::ExchangeFile::DatatypeDefinitionBinaryFile, "formatName")
    descriptor = None
    for klass in rif12::ExchangeFile::DatatypeDefinitionBinaryFile.__mro__:
        if "formatName" in klass.__dict__:
            descriptor = klass.__dict__["formatName"]
            break
    assert isinstance(descriptor, property)

def test_rif12::exchangefile::datatypedefinitionbinaryfile_has_filenameSuffix():
    assert hasattr(rif12::ExchangeFile::DatatypeDefinitionBinaryFile, "filenameSuffix")
    descriptor = None
    for klass in rif12::ExchangeFile::DatatypeDefinitionBinaryFile.__mro__:
        if "filenameSuffix" in klass.__dict__:
            descriptor = klass.__dict__["filenameSuffix"]
            break
    assert isinstance(descriptor, property)

def test_rif12::exchangefile::datatypedefinitionbinaryfile_has_application():
    assert hasattr(rif12::ExchangeFile::DatatypeDefinitionBinaryFile, "application")
    descriptor = None
    for klass in rif12::ExchangeFile::DatatypeDefinitionBinaryFile.__mro__:
        if "application" in klass.__dict__:
            descriptor = klass.__dict__["application"]
            break
    assert isinstance(descriptor, property)



def test_rif12::exchangefile::datatypedefinitiondocument_is_not_abstract():
    assert not inspect.isabstract(rif12::ExchangeFile::DatatypeDefinitionDocument)


def test_rif12::exchangefile::datatypedefinitiondocument_constructor_exists():
    assert callable(rif12::ExchangeFile::DatatypeDefinitionDocument.__init__)


def test_rif12::exchangefile::datatypedefinitiondocument_constructor_args():
    sig = inspect.signature(rif12::ExchangeFile::DatatypeDefinitionDocument.__init__)
    params = list(sig.parameters.keys())



def test_datatypedefinitionsimple_is_not_abstract():
    assert not inspect.isabstract(DatatypeDefinitionSimple)


def test_datatypedefinitionsimple_constructor_exists():
    assert callable(DatatypeDefinitionSimple.__init__)


def test_datatypedefinitionsimple_constructor_args():
    sig = inspect.signature(DatatypeDefinitionSimple.__init__)
    params = list(sig.parameters.keys())



def test_rif12::exchangefile::datatypedefinitioninteger_is_not_abstract():
    assert not inspect.isabstract(rif12::ExchangeFile::DatatypeDefinitionInteger)


def test_rif12::exchangefile::datatypedefinitioninteger_constructor_exists():
    assert callable(rif12::ExchangeFile::DatatypeDefinitionInteger.__init__)


def test_rif12::exchangefile::datatypedefinitioninteger_constructor_args():
    sig = inspect.signature(rif12::ExchangeFile::DatatypeDefinitionInteger.__init__)
    params = list(sig.parameters.keys())
    assert "max" in params, "Missing parameter 'max'"
    assert "min" in params, "Missing parameter 'min'"

def test_rif12::exchangefile::datatypedefinitioninteger_has_max():
    assert hasattr(rif12::ExchangeFile::DatatypeDefinitionInteger, "max")
    descriptor = None
    for klass in rif12::ExchangeFile::DatatypeDefinitionInteger.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_rif12::exchangefile::datatypedefinitioninteger_has_min():
    assert hasattr(rif12::ExchangeFile::DatatypeDefinitionInteger, "min")
    descriptor = None
    for klass in rif12::ExchangeFile::DatatypeDefinitionInteger.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)



def test_rif12::exchangefile::datatypedefinitionboolean_is_not_abstract():
    assert not inspect.isabstract(rif12::ExchangeFile::DatatypeDefinitionBoolean)


def test_rif12::exchangefile::datatypedefinitionboolean_constructor_exists():
    assert callable(rif12::ExchangeFile::DatatypeDefinitionBoolean.__init__)


def test_rif12::exchangefile::datatypedefinitionboolean_constructor_args():
    sig = inspect.signature(rif12::ExchangeFile::DatatypeDefinitionBoolean.__init__)
    params = list(sig.parameters.keys())



def test_rif12::exchangefile::datatypedefinitiondate_is_not_abstract():
    assert not inspect.isabstract(rif12::ExchangeFile::DatatypeDefinitionDate)


def test_rif12::exchangefile::datatypedefinitiondate_constructor_exists():
    assert callable(rif12::ExchangeFile::DatatypeDefinitionDate.__init__)


def test_rif12::exchangefile::datatypedefinitiondate_constructor_args():
    sig = inspect.signature(rif12::ExchangeFile::DatatypeDefinitionDate.__init__)
    params = list(sig.parameters.keys())
    assert "format" in params, "Missing parameter 'format'"

def test_rif12::exchangefile::datatypedefinitiondate_has_format():
    assert hasattr(rif12::ExchangeFile::DatatypeDefinitionDate, "format")
    descriptor = None
    for klass in rif12::ExchangeFile::DatatypeDefinitionDate.__mro__:
        if "format" in klass.__dict__:
            descriptor = klass.__dict__["format"]
            break
    assert isinstance(descriptor, property)



def test_rif12::exchangefile::datatypedefinitionstring_is_not_abstract():
    assert not inspect.isabstract(rif12::ExchangeFile::DatatypeDefinitionString)


def test_rif12::exchangefile::datatypedefinitionstring_constructor_exists():
    assert callable(rif12::ExchangeFile::DatatypeDefinitionString.__init__)


def test_rif12::exchangefile::datatypedefinitionstring_constructor_args():
    sig = inspect.signature(rif12::ExchangeFile::DatatypeDefinitionString.__init__)
    params = list(sig.parameters.keys())
    assert "maxLength" in params, "Missing parameter 'maxLength'"

def test_rif12::exchangefile::datatypedefinitionstring_has_maxLength():
    assert hasattr(rif12::ExchangeFile::DatatypeDefinitionString, "maxLength")
    descriptor = None
    for klass in rif12::ExchangeFile::DatatypeDefinitionString.__mro__:
        if "maxLength" in klass.__dict__:
            descriptor = klass.__dict__["maxLength"]
            break
    assert isinstance(descriptor, property)



def test_rif12::exchangefile::datatypedefinitionreal_is_not_abstract():
    assert not inspect.isabstract(rif12::ExchangeFile::DatatypeDefinitionReal)


def test_rif12::exchangefile::datatypedefinitionreal_constructor_exists():
    assert callable(rif12::ExchangeFile::DatatypeDefinitionReal.__init__)


def test_rif12::exchangefile::datatypedefinitionreal_constructor_args():
    sig = inspect.signature(rif12::ExchangeFile::DatatypeDefinitionReal.__init__)
    params = list(sig.parameters.keys())
    assert "accuracy" in params, "Missing parameter 'accuracy'"
    assert "max" in params, "Missing parameter 'max'"
    assert "min" in params, "Missing parameter 'min'"

def test_rif12::exchangefile::datatypedefinitionreal_has_accuracy():
    assert hasattr(rif12::ExchangeFile::DatatypeDefinitionReal, "accuracy")
    descriptor = None
    for klass in rif12::ExchangeFile::DatatypeDefinitionReal.__mro__:
        if "accuracy" in klass.__dict__:
            descriptor = klass.__dict__["accuracy"]
            break
    assert isinstance(descriptor, property)

def test_rif12::exchangefile::datatypedefinitionreal_has_max():
    assert hasattr(rif12::ExchangeFile::DatatypeDefinitionReal, "max")
    descriptor = None
    for klass in rif12::ExchangeFile::DatatypeDefinitionReal.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_rif12::exchangefile::datatypedefinitionreal_has_min():
    assert hasattr(rif12::ExchangeFile::DatatypeDefinitionReal, "min")
    descriptor = None
    for klass in rif12::ExchangeFile::DatatypeDefinitionReal.__mro__:
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



def test_rif12::exchangefile::embeddedvalue_is_not_abstract():
    assert not inspect.isabstract(rif12::ExchangeFile::EmbeddedValue)


def test_rif12::exchangefile::embeddedvalue_constructor_exists():
    assert callable(rif12::ExchangeFile::EmbeddedValue.__init__)


def test_rif12::exchangefile::embeddedvalue_constructor_args():
    sig = inspect.signature(rif12::ExchangeFile::EmbeddedValue.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "otherContent" in params, "Missing parameter 'otherContent'"

def test_rif12::exchangefile::embeddedvalue_has_key():
    assert hasattr(rif12::ExchangeFile::EmbeddedValue, "key")
    descriptor = None
    for klass in rif12::ExchangeFile::EmbeddedValue.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_rif12::exchangefile::embeddedvalue_has_otherContent():
    assert hasattr(rif12::ExchangeFile::EmbeddedValue, "otherContent")
    descriptor = None
    for klass in rif12::ExchangeFile::EmbeddedValue.__mro__:
        if "otherContent" in klass.__dict__:
            descriptor = klass.__dict__["otherContent"]
            break
    assert isinstance(descriptor, property)



def test_datatypedefinition_is_not_abstract():
    assert not inspect.isabstract(DatatypeDefinition)


def test_datatypedefinition_constructor_exists():
    assert callable(DatatypeDefinition.__init__)


def test_datatypedefinition_constructor_args():
    sig = inspect.signature(DatatypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_rif12::exchangefile::datatypedefinitioncomplex_is_not_abstract():
    assert not inspect.isabstract(rif12::ExchangeFile::DatatypeDefinitionComplex)


def test_rif12::exchangefile::datatypedefinitioncomplex_constructor_exists():
    assert callable(rif12::ExchangeFile::DatatypeDefinitionComplex.__init__)


def test_rif12::exchangefile::datatypedefinitioncomplex_constructor_args():
    sig = inspect.signature(rif12::ExchangeFile::DatatypeDefinitionComplex.__init__)
    params = list(sig.parameters.keys())
    assert "embedded" in params, "Missing parameter 'embedded'"

def test_rif12::exchangefile::datatypedefinitioncomplex_has_embedded():
    assert hasattr(rif12::ExchangeFile::DatatypeDefinitionComplex, "embedded")
    descriptor = None
    for klass in rif12::ExchangeFile::DatatypeDefinitionComplex.__mro__:
        if "embedded" in klass.__dict__:
            descriptor = klass.__dict__["embedded"]
            break
    assert isinstance(descriptor, property)



def test_rif12::exchangefile::datatypedefinitionsimple_is_not_abstract():
    assert not inspect.isabstract(rif12::ExchangeFile::DatatypeDefinitionSimple)


def test_rif12::exchangefile::datatypedefinitionsimple_constructor_exists():
    assert callable(rif12::ExchangeFile::DatatypeDefinitionSimple.__init__)


def test_rif12::exchangefile::datatypedefinitionsimple_constructor_args():
    sig = inspect.signature(rif12::ExchangeFile::DatatypeDefinitionSimple.__init__)
    params = list(sig.parameters.keys())



def test_rif12::exchangefile::datatypedefinitionenumeration_is_not_abstract():
    assert not inspect.isabstract(rif12::ExchangeFile::DatatypeDefinitionEnumeration)


def test_rif12::exchangefile::datatypedefinitionenumeration_constructor_exists():
    assert callable(rif12::ExchangeFile::DatatypeDefinitionEnumeration.__init__)


def test_rif12::exchangefile::datatypedefinitionenumeration_constructor_args():
    sig = inspect.signature(rif12::ExchangeFile::DatatypeDefinitionEnumeration.__init__)
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



def test_specgrouphierarchy_is_not_abstract():
    assert not inspect.isabstract(SpecGroupHierarchy)


def test_specgrouphierarchy_constructor_exists():
    assert callable(SpecGroupHierarchy.__init__)


def test_specgrouphierarchy_constructor_args():
    sig = inspect.signature(SpecGroupHierarchy.__init__)
    params = list(sig.parameters.keys())



def test_spechierarchyroot_is_not_abstract():
    assert not inspect.isabstract(SpecHierarchyRoot)


def test_spechierarchyroot_constructor_exists():
    assert callable(SpecHierarchyRoot.__init__)


def test_spechierarchyroot_constructor_args():
    sig = inspect.signature(SpecHierarchyRoot.__init__)
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



def test_rif12::exchangefile::attributedefinitioncomplex_is_not_abstract():
    assert not inspect.isabstract(rif12::ExchangeFile::AttributeDefinitionComplex)


def test_rif12::exchangefile::attributedefinitioncomplex_constructor_exists():
    assert callable(rif12::ExchangeFile::AttributeDefinitionComplex.__init__)


def test_rif12::exchangefile::attributedefinitioncomplex_constructor_args():
    sig = inspect.signature(rif12::ExchangeFile::AttributeDefinitionComplex.__init__)
    params = list(sig.parameters.keys())



def test_rif12::exchangefile::attributedefinitionsimple_is_not_abstract():
    assert not inspect.isabstract(rif12::ExchangeFile::AttributeDefinitionSimple)


def test_rif12::exchangefile::attributedefinitionsimple_constructor_exists():
    assert callable(rif12::ExchangeFile::AttributeDefinitionSimple.__init__)


def test_rif12::exchangefile::attributedefinitionsimple_constructor_args():
    sig = inspect.signature(rif12::ExchangeFile::AttributeDefinitionSimple.__init__)
    params = list(sig.parameters.keys())



def test_rif12::exchangefile::attributedefinitionenumeration_is_not_abstract():
    assert not inspect.isabstract(rif12::ExchangeFile::AttributeDefinitionEnumeration)


def test_rif12::exchangefile::attributedefinitionenumeration_constructor_exists():
    assert callable(rif12::ExchangeFile::AttributeDefinitionEnumeration.__init__)


def test_rif12::exchangefile::attributedefinitionenumeration_constructor_args():
    sig = inspect.signature(rif12::ExchangeFile::AttributeDefinitionEnumeration.__init__)
    params = list(sig.parameters.keys())
    assert "multiValued" in params, "Missing parameter 'multiValued'"

def test_rif12::exchangefile::attributedefinitionenumeration_has_multiValued():
    assert hasattr(rif12::ExchangeFile::AttributeDefinitionEnumeration, "multiValued")
    descriptor = None
    for klass in rif12::ExchangeFile::AttributeDefinitionEnumeration.__mro__:
        if "multiValued" in klass.__dict__:
            descriptor = klass.__dict__["multiValued"]
            break
    assert isinstance(descriptor, property)



def test_rif12::exchangefile::identifiable_is_not_abstract():
    assert not inspect.isabstract(rif12::ExchangeFile::Identifiable)


def test_rif12::exchangefile::identifiable_constructor_exists():
    assert callable(rif12::ExchangeFile::Identifiable.__init__)


def test_rif12::exchangefile::identifiable_constructor_args():
    sig = inspect.signature(rif12::ExchangeFile::Identifiable.__init__)
    params = list(sig.parameters.keys())
    assert "lastChange" in params, "Missing parameter 'lastChange'"
    assert "longName" in params, "Missing parameter 'longName'"
    assert "desc" in params, "Missing parameter 'desc'"
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_rif12::exchangefile::identifiable_has_lastChange():
    assert hasattr(rif12::ExchangeFile::Identifiable, "lastChange")
    descriptor = None
    for klass in rif12::ExchangeFile::Identifiable.__mro__:
        if "lastChange" in klass.__dict__:
            descriptor = klass.__dict__["lastChange"]
            break
    assert isinstance(descriptor, property)

def test_rif12::exchangefile::identifiable_has_longName():
    assert hasattr(rif12::ExchangeFile::Identifiable, "longName")
    descriptor = None
    for klass in rif12::ExchangeFile::Identifiable.__mro__:
        if "longName" in klass.__dict__:
            descriptor = klass.__dict__["longName"]
            break
    assert isinstance(descriptor, property)

def test_rif12::exchangefile::identifiable_has_desc():
    assert hasattr(rif12::ExchangeFile::Identifiable, "desc")
    descriptor = None
    for klass in rif12::ExchangeFile::Identifiable.__mro__:
        if "desc" in klass.__dict__:
            descriptor = klass.__dict__["desc"]
            break
    assert isinstance(descriptor, property)

def test_rif12::exchangefile::identifiable_has_identifier():
    assert hasattr(rif12::ExchangeFile::Identifiable, "identifier")
    descriptor = None
    for klass in rif12::ExchangeFile::Identifiable.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_relationgroup_is_not_abstract():
    assert not inspect.isabstract(RelationGroup)


def test_relationgroup_constructor_exists():
    assert callable(RelationGroup.__init__)


def test_relationgroup_constructor_args():
    sig = inspect.signature(RelationGroup.__init__)
    params = list(sig.parameters.keys())



def test_specelementwithuserdefinedattributes_is_not_abstract():
    assert not inspect.isabstract(SpecElementWithUserDefinedAttributes)


def test_specelementwithuserdefinedattributes_constructor_exists():
    assert callable(SpecElementWithUserDefinedAttributes.__init__)


def test_specelementwithuserdefinedattributes_constructor_args():
    sig = inspect.signature(SpecElementWithUserDefinedAttributes.__init__)
    params = list(sig.parameters.keys())



def test_rif12::exchangefile::specgrouphierarchyroot_is_not_abstract():
    assert not inspect.isabstract(rif12::ExchangeFile::SpecGroupHierarchyRoot)


def test_rif12::exchangefile::specgrouphierarchyroot_constructor_exists():
    assert callable(rif12::ExchangeFile::SpecGroupHierarchyRoot.__init__)


def test_rif12::exchangefile::specgrouphierarchyroot_constructor_args():
    sig = inspect.signature(rif12::ExchangeFile::SpecGroupHierarchyRoot.__init__)
    params = list(sig.parameters.keys())



def test_rif12::exchangefile::specgroup_is_not_abstract():
    assert not inspect.isabstract(rif12::ExchangeFile::SpecGroup)


def test_rif12::exchangefile::specgroup_constructor_exists():
    assert callable(rif12::ExchangeFile::SpecGroup.__init__)


def test_rif12::exchangefile::specgroup_constructor_args():
    sig = inspect.signature(rif12::ExchangeFile::SpecGroup.__init__)
    params = list(sig.parameters.keys())



def test_rif12::exchangefile::specrelation_is_not_abstract():
    assert not inspect.isabstract(rif12::ExchangeFile::SpecRelation)


def test_rif12::exchangefile::specrelation_constructor_exists():
    assert callable(rif12::ExchangeFile::SpecRelation.__init__)


def test_rif12::exchangefile::specrelation_constructor_args():
    sig = inspect.signature(rif12::ExchangeFile::SpecRelation.__init__)
    params = list(sig.parameters.keys())



def test_rif12::exchangefile::specobject_is_not_abstract():
    assert not inspect.isabstract(rif12::ExchangeFile::SpecObject)


def test_rif12::exchangefile::specobject_constructor_exists():
    assert callable(rif12::ExchangeFile::SpecObject.__init__)


def test_rif12::exchangefile::specobject_constructor_args():
    sig = inspect.signature(rif12::ExchangeFile::SpecObject.__init__)
    params = list(sig.parameters.keys())



def test_rif12::exchangefile::spechierarchyroot_is_not_abstract():
    assert not inspect.isabstract(rif12::ExchangeFile::SpecHierarchyRoot)


def test_rif12::exchangefile::spechierarchyroot_constructor_exists():
    assert callable(rif12::ExchangeFile::SpecHierarchyRoot.__init__)


def test_rif12::exchangefile::spechierarchyroot_constructor_args():
    sig = inspect.signature(rif12::ExchangeFile::SpecHierarchyRoot.__init__)
    params = list(sig.parameters.keys())



def test_attributevalue_is_not_abstract():
    assert not inspect.isabstract(AttributeValue)


def test_attributevalue_constructor_exists():
    assert callable(AttributeValue.__init__)


def test_attributevalue_constructor_args():
    sig = inspect.signature(AttributeValue.__init__)
    params = list(sig.parameters.keys())



def test_rif12::exchangefile::attributevaluecomplex_is_not_abstract():
    assert not inspect.isabstract(rif12::ExchangeFile::AttributeValueComplex)


def test_rif12::exchangefile::attributevaluecomplex_constructor_exists():
    assert callable(rif12::ExchangeFile::AttributeValueComplex.__init__)


def test_rif12::exchangefile::attributevaluecomplex_constructor_args():
    sig = inspect.signature(rif12::ExchangeFile::AttributeValueComplex.__init__)
    params = list(sig.parameters.keys())



def test_rif12::exchangefile::attributevaluesimple_is_not_abstract():
    assert not inspect.isabstract(rif12::ExchangeFile::AttributeValueSimple)


def test_rif12::exchangefile::attributevaluesimple_constructor_exists():
    assert callable(rif12::ExchangeFile::AttributeValueSimple.__init__)


def test_rif12::exchangefile::attributevaluesimple_constructor_args():
    sig = inspect.signature(rif12::ExchangeFile::AttributeValueSimple.__init__)
    params = list(sig.parameters.keys())
    assert "theValue" in params, "Missing parameter 'theValue'"

def test_rif12::exchangefile::attributevaluesimple_has_theValue():
    assert hasattr(rif12::ExchangeFile::AttributeValueSimple, "theValue")
    descriptor = None
    for klass in rif12::ExchangeFile::AttributeValueSimple.__mro__:
        if "theValue" in klass.__dict__:
            descriptor = klass.__dict__["theValue"]
            break
    assert isinstance(descriptor, property)



def test_rif12::exchangefile::attributevalueenumeration_is_not_abstract():
    assert not inspect.isabstract(rif12::ExchangeFile::AttributeValueEnumeration)


def test_rif12::exchangefile::attributevalueenumeration_constructor_exists():
    assert callable(rif12::ExchangeFile::AttributeValueEnumeration.__init__)


def test_rif12::exchangefile::attributevalueenumeration_constructor_args():
    sig = inspect.signature(rif12::ExchangeFile::AttributeValueEnumeration.__init__)
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



def test_rif12::exchangefile::accesspolicy_is_not_abstract():
    assert not inspect.isabstract(rif12::ExchangeFile::AccessPolicy)


def test_rif12::exchangefile::accesspolicy_constructor_exists():
    assert callable(rif12::ExchangeFile::AccessPolicy.__init__)


def test_rif12::exchangefile::accesspolicy_constructor_args():
    sig = inspect.signature(rif12::ExchangeFile::AccessPolicy.__init__)
    params = list(sig.parameters.keys())
    assert "accessMode" in params, "Missing parameter 'accessMode'"

def test_rif12::exchangefile::accesspolicy_has_accessMode():
    assert hasattr(rif12::ExchangeFile::AccessPolicy, "accessMode")
    descriptor = None
    for klass in rif12::ExchangeFile::AccessPolicy.__mro__:
        if "accessMode" in klass.__dict__:
            descriptor = klass.__dict__["accessMode"]
            break
    assert isinstance(descriptor, property)



def test_rif12::exchangefile::enumvalue_is_not_abstract():
    assert not inspect.isabstract(rif12::ExchangeFile::EnumValue)


def test_rif12::exchangefile::enumvalue_constructor_exists():
    assert callable(rif12::ExchangeFile::EnumValue.__init__)


def test_rif12::exchangefile::enumvalue_constructor_args():
    sig = inspect.signature(rif12::ExchangeFile::EnumValue.__init__)
    params = list(sig.parameters.keys())



def test_rif12::exchangefile::spectype_is_not_abstract():
    assert not inspect.isabstract(rif12::ExchangeFile::SpecType)


def test_rif12::exchangefile::spectype_constructor_exists():
    assert callable(rif12::ExchangeFile::SpecType.__init__)


def test_rif12::exchangefile::spectype_constructor_args():
    sig = inspect.signature(rif12::ExchangeFile::SpecType.__init__)
    params = list(sig.parameters.keys())



def test_rif12::exchangefile::attributevalue_is_not_abstract():
    assert not inspect.isabstract(rif12::ExchangeFile::AttributeValue)


def test_rif12::exchangefile::attributevalue_constructor_exists():
    assert callable(rif12::ExchangeFile::AttributeValue.__init__)


def test_rif12::exchangefile::attributevalue_constructor_args():
    sig = inspect.signature(rif12::ExchangeFile::AttributeValue.__init__)
    params = list(sig.parameters.keys())



def test_rif12::exchangefile::datatypedefinition_is_not_abstract():
    assert not inspect.isabstract(rif12::ExchangeFile::DatatypeDefinition)


def test_rif12::exchangefile::datatypedefinition_constructor_exists():
    assert callable(rif12::ExchangeFile::DatatypeDefinition.__init__)


def test_rif12::exchangefile::datatypedefinition_constructor_args():
    sig = inspect.signature(rif12::ExchangeFile::DatatypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_rif12::exchangefile::spechierarchy_is_not_abstract():
    assert not inspect.isabstract(rif12::ExchangeFile::SpecHierarchy)


def test_rif12::exchangefile::spechierarchy_constructor_exists():
    assert callable(rif12::ExchangeFile::SpecHierarchy.__init__)


def test_rif12::exchangefile::spechierarchy_constructor_args():
    sig = inspect.signature(rif12::ExchangeFile::SpecHierarchy.__init__)
    params = list(sig.parameters.keys())



def test_rif12::exchangefile::specgrouphierarchy_is_not_abstract():
    assert not inspect.isabstract(rif12::ExchangeFile::SpecGroupHierarchy)


def test_rif12::exchangefile::specgrouphierarchy_constructor_exists():
    assert callable(rif12::ExchangeFile::SpecGroupHierarchy.__init__)


def test_rif12::exchangefile::specgrouphierarchy_constructor_args():
    sig = inspect.signature(rif12::ExchangeFile::SpecGroupHierarchy.__init__)
    params = list(sig.parameters.keys())



def test_rif12::exchangefile::attributedefinition_is_not_abstract():
    assert not inspect.isabstract(rif12::ExchangeFile::AttributeDefinition)


def test_rif12::exchangefile::attributedefinition_constructor_exists():
    assert callable(rif12::ExchangeFile::AttributeDefinition.__init__)


def test_rif12::exchangefile::attributedefinition_constructor_args():
    sig = inspect.signature(rif12::ExchangeFile::AttributeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_rif12::exchangefile::relationgroup_is_not_abstract():
    assert not inspect.isabstract(rif12::ExchangeFile::RelationGroup)


def test_rif12::exchangefile::relationgroup_constructor_exists():
    assert callable(rif12::ExchangeFile::RelationGroup.__init__)


def test_rif12::exchangefile::relationgroup_constructor_args():
    sig = inspect.signature(rif12::ExchangeFile::RelationGroup.__init__)
    params = list(sig.parameters.keys())



def test_rif12::exchangefile::specelementwithuserdefinedattributes_is_not_abstract():
    assert not inspect.isabstract(rif12::ExchangeFile::SpecElementWithUserDefinedAttributes)


def test_rif12::exchangefile::specelementwithuserdefinedattributes_constructor_exists():
    assert callable(rif12::ExchangeFile::SpecElementWithUserDefinedAttributes.__init__)


def test_rif12::exchangefile::specelementwithuserdefinedattributes_constructor_args():
    sig = inspect.signature(rif12::ExchangeFile::SpecElementWithUserDefinedAttributes.__init__)
    params = list(sig.parameters.keys())



def test_spechierarchy_is_not_abstract():
    assert not inspect.isabstract(SpecHierarchy)


def test_spechierarchy_constructor_exists():
    assert callable(SpecHierarchy.__init__)


def test_spechierarchy_constructor_args():
    sig = inspect.signature(SpecHierarchy.__init__)
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
rif12::DataTypes::XmlContent_strategy = st.builds(
    rif12::DataTypes::XmlContent,
)
rif12::DataTypes::XhtmlContent_strategy = st.builds(
    rif12::DataTypes::XhtmlContent,
)
rif12::DataTypes::BinaryContent_strategy = st.builds(
    rif12::DataTypes::BinaryContent,
)
rif12::ExchangeFile::RIFToolExtension_strategy = st.builds(
    rif12::ExchangeFile::RIFToolExtension,
)
rif12::ExchangeFile::RIFHeader_strategy = st.builds(
    rif12::ExchangeFile::RIFHeader,
    title=
        safe_text,
    creationTime=
        safe_text,
    sourceToolId=
        safe_text,
    comment=
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
rif12::ExchangeFile::RIF_strategy = st.builds(
    rif12::ExchangeFile::RIF,
)
AccessPolicy_strategy = st.builds(
    AccessPolicy,
)
rif12::ExchangeFile::RIFContent_strategy = st.builds(
    rif12::ExchangeFile::RIFContent,
)
DataTypes::BinaryContent_strategy = st.builds(
    DataTypes::BinaryContent,
)
DataTypes::XhtmlContent_strategy = st.builds(
    DataTypes::XhtmlContent,
)
AttributeDefinitionComplex_strategy = st.builds(
    AttributeDefinitionComplex,
)
AttributeDefinitionSimple_strategy = st.builds(
    AttributeDefinitionSimple,
)
AttributeValueSimple_strategy = st.builds(
    AttributeValueSimple,
)
DataTypes::XmlContent_strategy = st.builds(
    DataTypes::XmlContent,
)
EmbeddedValue_strategy = st.builds(
    EmbeddedValue,
)
EnumValue_strategy = st.builds(
    EnumValue,
)
AttributeValueEnumeration_strategy = st.builds(
    AttributeValueEnumeration,
)
DatatypeDefinitionEnumeration_strategy = st.builds(
    DatatypeDefinitionEnumeration,
)
AttributeValueComplex_strategy = st.builds(
    AttributeValueComplex,
)
rif12::ExchangeFile::AttributeValueEmbeddedDocument_strategy = st.builds(
    rif12::ExchangeFile::AttributeValueEmbeddedDocument,
)
rif12::ExchangeFile::AttributeValueXmlData_strategy = st.builds(
    rif12::ExchangeFile::AttributeValueXmlData,
)
rif12::ExchangeFile::AttributeValueFileReference_strategy = st.builds(
    rif12::ExchangeFile::AttributeValueFileReference,
    pathToFile=
        safe_text
)
rif12::ExchangeFile::AttributeValueEmbeddedFile_strategy = st.builds(
    rif12::ExchangeFile::AttributeValueEmbeddedFile,
)
DatatypeDefinitionComplex_strategy = st.builds(
    DatatypeDefinitionComplex,
)
rif12::ExchangeFile::DatatypeDefinitionXmlData_strategy = st.builds(
    rif12::ExchangeFile::DatatypeDefinitionXmlData,
    nameSpaceURI=
        safe_text,
    schemaLocation=
        safe_text
)
rif12::ExchangeFile::DatatypeDefinitionBinaryFile_strategy = st.builds(
    rif12::ExchangeFile::DatatypeDefinitionBinaryFile,
    mimeType=
        safe_text,
    formatName=
        safe_text,
    filenameSuffix=
        safe_text,
    application=
        safe_text
)
rif12::ExchangeFile::DatatypeDefinitionDocument_strategy = st.builds(
    rif12::ExchangeFile::DatatypeDefinitionDocument,
)
DatatypeDefinitionSimple_strategy = st.builds(
    DatatypeDefinitionSimple,
)
rif12::ExchangeFile::DatatypeDefinitionInteger_strategy = st.builds(
    rif12::ExchangeFile::DatatypeDefinitionInteger,
    max=
        safe_text,
    min=
        safe_text
)
rif12::ExchangeFile::DatatypeDefinitionBoolean_strategy = st.builds(
    rif12::ExchangeFile::DatatypeDefinitionBoolean,
)
rif12::ExchangeFile::DatatypeDefinitionDate_strategy = st.builds(
    rif12::ExchangeFile::DatatypeDefinitionDate,
    format=
        safe_text
)
rif12::ExchangeFile::DatatypeDefinitionString_strategy = st.builds(
    rif12::ExchangeFile::DatatypeDefinitionString,
    maxLength=
        safe_text
)
rif12::ExchangeFile::DatatypeDefinitionReal_strategy = st.builds(
    rif12::ExchangeFile::DatatypeDefinitionReal,
    accuracy=
        safe_text,
    max=
        safe_text,
    min=
        safe_text
)
AttributeDefinitionEnumeration_strategy = st.builds(
    AttributeDefinitionEnumeration,
)
rif12::ExchangeFile::EmbeddedValue_strategy = st.builds(
    rif12::ExchangeFile::EmbeddedValue,
    key=
        safe_text,
    otherContent=
        safe_text
)
DatatypeDefinition_strategy = st.builds(
    DatatypeDefinition,
)
rif12::ExchangeFile::DatatypeDefinitionComplex_strategy = st.builds(
    rif12::ExchangeFile::DatatypeDefinitionComplex,
    embedded=
        safe_text
)
rif12::ExchangeFile::DatatypeDefinitionSimple_strategy = st.builds(
    rif12::ExchangeFile::DatatypeDefinitionSimple,
)
rif12::ExchangeFile::DatatypeDefinitionEnumeration_strategy = st.builds(
    rif12::ExchangeFile::DatatypeDefinitionEnumeration,
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
SpecGroupHierarchy_strategy = st.builds(
    SpecGroupHierarchy,
)
SpecHierarchyRoot_strategy = st.builds(
    SpecHierarchyRoot,
)
SpecObject_strategy = st.builds(
    SpecObject,
)
AttributeDefinition_strategy = st.builds(
    AttributeDefinition,
)
rif12::ExchangeFile::AttributeDefinitionComplex_strategy = st.builds(
    rif12::ExchangeFile::AttributeDefinitionComplex,
)
rif12::ExchangeFile::AttributeDefinitionSimple_strategy = st.builds(
    rif12::ExchangeFile::AttributeDefinitionSimple,
)
rif12::ExchangeFile::AttributeDefinitionEnumeration_strategy = st.builds(
    rif12::ExchangeFile::AttributeDefinitionEnumeration,
    multiValued=
        safe_text
)
rif12::ExchangeFile::Identifiable_strategy = st.builds(
    rif12::ExchangeFile::Identifiable,
    lastChange=
        safe_text,
    longName=
        safe_text,
    desc=
        safe_text,
    identifier=
        safe_text
)
RelationGroup_strategy = st.builds(
    RelationGroup,
)
SpecElementWithUserDefinedAttributes_strategy = st.builds(
    SpecElementWithUserDefinedAttributes,
)
rif12::ExchangeFile::SpecGroupHierarchyRoot_strategy = st.builds(
    rif12::ExchangeFile::SpecGroupHierarchyRoot,
)
rif12::ExchangeFile::SpecGroup_strategy = st.builds(
    rif12::ExchangeFile::SpecGroup,
)
rif12::ExchangeFile::SpecRelation_strategy = st.builds(
    rif12::ExchangeFile::SpecRelation,
)
rif12::ExchangeFile::SpecObject_strategy = st.builds(
    rif12::ExchangeFile::SpecObject,
)
rif12::ExchangeFile::SpecHierarchyRoot_strategy = st.builds(
    rif12::ExchangeFile::SpecHierarchyRoot,
)
AttributeValue_strategy = st.builds(
    AttributeValue,
)
rif12::ExchangeFile::AttributeValueComplex_strategy = st.builds(
    rif12::ExchangeFile::AttributeValueComplex,
)
rif12::ExchangeFile::AttributeValueSimple_strategy = st.builds(
    rif12::ExchangeFile::AttributeValueSimple,
    theValue=
        safe_text
)
rif12::ExchangeFile::AttributeValueEnumeration_strategy = st.builds(
    rif12::ExchangeFile::AttributeValueEnumeration,
)
SpecType_strategy = st.builds(
    SpecType,
)
Identifiable_strategy = st.builds(
    Identifiable,
)
rif12::ExchangeFile::AccessPolicy_strategy = st.builds(
    rif12::ExchangeFile::AccessPolicy,
    accessMode=
        safe_text
)
rif12::ExchangeFile::EnumValue_strategy = st.builds(
    rif12::ExchangeFile::EnumValue,
)
rif12::ExchangeFile::SpecType_strategy = st.builds(
    rif12::ExchangeFile::SpecType,
)
rif12::ExchangeFile::AttributeValue_strategy = st.builds(
    rif12::ExchangeFile::AttributeValue,
)
rif12::ExchangeFile::DatatypeDefinition_strategy = st.builds(
    rif12::ExchangeFile::DatatypeDefinition,
)
rif12::ExchangeFile::SpecHierarchy_strategy = st.builds(
    rif12::ExchangeFile::SpecHierarchy,
)
rif12::ExchangeFile::SpecGroupHierarchy_strategy = st.builds(
    rif12::ExchangeFile::SpecGroupHierarchy,
)
rif12::ExchangeFile::AttributeDefinition_strategy = st.builds(
    rif12::ExchangeFile::AttributeDefinition,
)
rif12::ExchangeFile::RelationGroup_strategy = st.builds(
    rif12::ExchangeFile::RelationGroup,
)
rif12::ExchangeFile::SpecElementWithUserDefinedAttributes_strategy = st.builds(
    rif12::ExchangeFile::SpecElementWithUserDefinedAttributes,
)
SpecHierarchy_strategy = st.builds(
    SpecHierarchy,
)

@given(instance=rif12::DataTypes::XmlContent_strategy)
@settings(max_examples=50)
def test_rif12::datatypes::xmlcontent_instantiation(instance):
    assert isinstance(instance, rif12::DataTypes::XmlContent)

@given(instance=rif12::DataTypes::XhtmlContent_strategy)
@settings(max_examples=50)
def test_rif12::datatypes::xhtmlcontent_instantiation(instance):
    assert isinstance(instance, rif12::DataTypes::XhtmlContent)

@given(instance=rif12::DataTypes::BinaryContent_strategy)
@settings(max_examples=50)
def test_rif12::datatypes::binarycontent_instantiation(instance):
    assert isinstance(instance, rif12::DataTypes::BinaryContent)

@given(instance=rif12::ExchangeFile::RIFToolExtension_strategy)
@settings(max_examples=50)
def test_rif12::exchangefile::riftoolextension_instantiation(instance):
    assert isinstance(instance, rif12::ExchangeFile::RIFToolExtension)

@given(instance=rif12::ExchangeFile::RIFHeader_strategy)
@settings(max_examples=50)
def test_rif12::exchangefile::rifheader_instantiation(instance):
    assert isinstance(instance, rif12::ExchangeFile::RIFHeader)

@given(instance=rif12::ExchangeFile::RIFHeader_strategy)
def test_rif12::exchangefile::rifheader_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=rif12::ExchangeFile::RIFHeader_strategy)
def test_rif12::exchangefile::rifheader_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=rif12::ExchangeFile::RIFHeader_strategy)
def test_rif12::exchangefile::rifheader_creationTime_type(instance):
    assert isinstance(instance.creationTime, str)


@given(instance=rif12::ExchangeFile::RIFHeader_strategy)
def test_rif12::exchangefile::rifheader_creationTime_setter(instance):
    original = instance.creationTime
    instance.creationTime = original
    assert instance.creationTime == original

@given(instance=rif12::ExchangeFile::RIFHeader_strategy)
def test_rif12::exchangefile::rifheader_sourceToolId_type(instance):
    assert isinstance(instance.sourceToolId, str)


@given(instance=rif12::ExchangeFile::RIFHeader_strategy)
def test_rif12::exchangefile::rifheader_sourceToolId_setter(instance):
    original = instance.sourceToolId
    instance.sourceToolId = original
    assert instance.sourceToolId == original

@given(instance=rif12::ExchangeFile::RIFHeader_strategy)
def test_rif12::exchangefile::rifheader_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=rif12::ExchangeFile::RIFHeader_strategy)
def test_rif12::exchangefile::rifheader_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=rif12::ExchangeFile::RIFHeader_strategy)
def test_rif12::exchangefile::rifheader_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=rif12::ExchangeFile::RIFHeader_strategy)
def test_rif12::exchangefile::rifheader_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=rif12::ExchangeFile::RIFHeader_strategy)
def test_rif12::exchangefile::rifheader_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=rif12::ExchangeFile::RIFHeader_strategy)
def test_rif12::exchangefile::rifheader_identifier_setter(instance):
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

@given(instance=rif12::ExchangeFile::RIF_strategy)
@settings(max_examples=50)
def test_rif12::exchangefile::rif_instantiation(instance):
    assert isinstance(instance, rif12::ExchangeFile::RIF)

@given(instance=AccessPolicy_strategy)
@settings(max_examples=50)
def test_accesspolicy_instantiation(instance):
    assert isinstance(instance, AccessPolicy)

@given(instance=rif12::ExchangeFile::RIFContent_strategy)
@settings(max_examples=50)
def test_rif12::exchangefile::rifcontent_instantiation(instance):
    assert isinstance(instance, rif12::ExchangeFile::RIFContent)

@given(instance=DataTypes::BinaryContent_strategy)
@settings(max_examples=50)
def test_datatypes::binarycontent_instantiation(instance):
    assert isinstance(instance, DataTypes::BinaryContent)

@given(instance=DataTypes::XhtmlContent_strategy)
@settings(max_examples=50)
def test_datatypes::xhtmlcontent_instantiation(instance):
    assert isinstance(instance, DataTypes::XhtmlContent)

@given(instance=AttributeDefinitionComplex_strategy)
@settings(max_examples=50)
def test_attributedefinitioncomplex_instantiation(instance):
    assert isinstance(instance, AttributeDefinitionComplex)

@given(instance=AttributeDefinitionSimple_strategy)
@settings(max_examples=50)
def test_attributedefinitionsimple_instantiation(instance):
    assert isinstance(instance, AttributeDefinitionSimple)

@given(instance=AttributeValueSimple_strategy)
@settings(max_examples=50)
def test_attributevaluesimple_instantiation(instance):
    assert isinstance(instance, AttributeValueSimple)

@given(instance=DataTypes::XmlContent_strategy)
@settings(max_examples=50)
def test_datatypes::xmlcontent_instantiation(instance):
    assert isinstance(instance, DataTypes::XmlContent)

@given(instance=EmbeddedValue_strategy)
@settings(max_examples=50)
def test_embeddedvalue_instantiation(instance):
    assert isinstance(instance, EmbeddedValue)

@given(instance=EnumValue_strategy)
@settings(max_examples=50)
def test_enumvalue_instantiation(instance):
    assert isinstance(instance, EnumValue)

@given(instance=AttributeValueEnumeration_strategy)
@settings(max_examples=50)
def test_attributevalueenumeration_instantiation(instance):
    assert isinstance(instance, AttributeValueEnumeration)

@given(instance=DatatypeDefinitionEnumeration_strategy)
@settings(max_examples=50)
def test_datatypedefinitionenumeration_instantiation(instance):
    assert isinstance(instance, DatatypeDefinitionEnumeration)

@given(instance=AttributeValueComplex_strategy)
@settings(max_examples=50)
def test_attributevaluecomplex_instantiation(instance):
    assert isinstance(instance, AttributeValueComplex)

@given(instance=rif12::ExchangeFile::AttributeValueEmbeddedDocument_strategy)
@settings(max_examples=50)
def test_rif12::exchangefile::attributevalueembeddeddocument_instantiation(instance):
    assert isinstance(instance, rif12::ExchangeFile::AttributeValueEmbeddedDocument)

@given(instance=rif12::ExchangeFile::AttributeValueXmlData_strategy)
@settings(max_examples=50)
def test_rif12::exchangefile::attributevaluexmldata_instantiation(instance):
    assert isinstance(instance, rif12::ExchangeFile::AttributeValueXmlData)

@given(instance=rif12::ExchangeFile::AttributeValueFileReference_strategy)
@settings(max_examples=50)
def test_rif12::exchangefile::attributevaluefilereference_instantiation(instance):
    assert isinstance(instance, rif12::ExchangeFile::AttributeValueFileReference)

@given(instance=rif12::ExchangeFile::AttributeValueFileReference_strategy)
def test_rif12::exchangefile::attributevaluefilereference_pathToFile_type(instance):
    assert isinstance(instance.pathToFile, str)


@given(instance=rif12::ExchangeFile::AttributeValueFileReference_strategy)
def test_rif12::exchangefile::attributevaluefilereference_pathToFile_setter(instance):
    original = instance.pathToFile
    instance.pathToFile = original
    assert instance.pathToFile == original

@given(instance=rif12::ExchangeFile::AttributeValueEmbeddedFile_strategy)
@settings(max_examples=50)
def test_rif12::exchangefile::attributevalueembeddedfile_instantiation(instance):
    assert isinstance(instance, rif12::ExchangeFile::AttributeValueEmbeddedFile)

@given(instance=DatatypeDefinitionComplex_strategy)
@settings(max_examples=50)
def test_datatypedefinitioncomplex_instantiation(instance):
    assert isinstance(instance, DatatypeDefinitionComplex)

@given(instance=rif12::ExchangeFile::DatatypeDefinitionXmlData_strategy)
@settings(max_examples=50)
def test_rif12::exchangefile::datatypedefinitionxmldata_instantiation(instance):
    assert isinstance(instance, rif12::ExchangeFile::DatatypeDefinitionXmlData)

@given(instance=rif12::ExchangeFile::DatatypeDefinitionXmlData_strategy)
def test_rif12::exchangefile::datatypedefinitionxmldata_nameSpaceURI_type(instance):
    assert isinstance(instance.nameSpaceURI, str)


@given(instance=rif12::ExchangeFile::DatatypeDefinitionXmlData_strategy)
def test_rif12::exchangefile::datatypedefinitionxmldata_nameSpaceURI_setter(instance):
    original = instance.nameSpaceURI
    instance.nameSpaceURI = original
    assert instance.nameSpaceURI == original

@given(instance=rif12::ExchangeFile::DatatypeDefinitionXmlData_strategy)
def test_rif12::exchangefile::datatypedefinitionxmldata_schemaLocation_type(instance):
    assert isinstance(instance.schemaLocation, str)


@given(instance=rif12::ExchangeFile::DatatypeDefinitionXmlData_strategy)
def test_rif12::exchangefile::datatypedefinitionxmldata_schemaLocation_setter(instance):
    original = instance.schemaLocation
    instance.schemaLocation = original
    assert instance.schemaLocation == original

@given(instance=rif12::ExchangeFile::DatatypeDefinitionBinaryFile_strategy)
@settings(max_examples=50)
def test_rif12::exchangefile::datatypedefinitionbinaryfile_instantiation(instance):
    assert isinstance(instance, rif12::ExchangeFile::DatatypeDefinitionBinaryFile)

@given(instance=rif12::ExchangeFile::DatatypeDefinitionBinaryFile_strategy)
def test_rif12::exchangefile::datatypedefinitionbinaryfile_mimeType_type(instance):
    assert isinstance(instance.mimeType, str)


@given(instance=rif12::ExchangeFile::DatatypeDefinitionBinaryFile_strategy)
def test_rif12::exchangefile::datatypedefinitionbinaryfile_mimeType_setter(instance):
    original = instance.mimeType
    instance.mimeType = original
    assert instance.mimeType == original

@given(instance=rif12::ExchangeFile::DatatypeDefinitionBinaryFile_strategy)
def test_rif12::exchangefile::datatypedefinitionbinaryfile_formatName_type(instance):
    assert isinstance(instance.formatName, str)


@given(instance=rif12::ExchangeFile::DatatypeDefinitionBinaryFile_strategy)
def test_rif12::exchangefile::datatypedefinitionbinaryfile_formatName_setter(instance):
    original = instance.formatName
    instance.formatName = original
    assert instance.formatName == original

@given(instance=rif12::ExchangeFile::DatatypeDefinitionBinaryFile_strategy)
def test_rif12::exchangefile::datatypedefinitionbinaryfile_filenameSuffix_type(instance):
    assert isinstance(instance.filenameSuffix, str)


@given(instance=rif12::ExchangeFile::DatatypeDefinitionBinaryFile_strategy)
def test_rif12::exchangefile::datatypedefinitionbinaryfile_filenameSuffix_setter(instance):
    original = instance.filenameSuffix
    instance.filenameSuffix = original
    assert instance.filenameSuffix == original

@given(instance=rif12::ExchangeFile::DatatypeDefinitionBinaryFile_strategy)
def test_rif12::exchangefile::datatypedefinitionbinaryfile_application_type(instance):
    assert isinstance(instance.application, str)


@given(instance=rif12::ExchangeFile::DatatypeDefinitionBinaryFile_strategy)
def test_rif12::exchangefile::datatypedefinitionbinaryfile_application_setter(instance):
    original = instance.application
    instance.application = original
    assert instance.application == original

@given(instance=rif12::ExchangeFile::DatatypeDefinitionDocument_strategy)
@settings(max_examples=50)
def test_rif12::exchangefile::datatypedefinitiondocument_instantiation(instance):
    assert isinstance(instance, rif12::ExchangeFile::DatatypeDefinitionDocument)

@given(instance=DatatypeDefinitionSimple_strategy)
@settings(max_examples=50)
def test_datatypedefinitionsimple_instantiation(instance):
    assert isinstance(instance, DatatypeDefinitionSimple)

@given(instance=rif12::ExchangeFile::DatatypeDefinitionInteger_strategy)
@settings(max_examples=50)
def test_rif12::exchangefile::datatypedefinitioninteger_instantiation(instance):
    assert isinstance(instance, rif12::ExchangeFile::DatatypeDefinitionInteger)

@given(instance=rif12::ExchangeFile::DatatypeDefinitionInteger_strategy)
def test_rif12::exchangefile::datatypedefinitioninteger_max_type(instance):
    assert isinstance(instance.max, str)


@given(instance=rif12::ExchangeFile::DatatypeDefinitionInteger_strategy)
def test_rif12::exchangefile::datatypedefinitioninteger_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=rif12::ExchangeFile::DatatypeDefinitionInteger_strategy)
def test_rif12::exchangefile::datatypedefinitioninteger_min_type(instance):
    assert isinstance(instance.min, str)


@given(instance=rif12::ExchangeFile::DatatypeDefinitionInteger_strategy)
def test_rif12::exchangefile::datatypedefinitioninteger_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=rif12::ExchangeFile::DatatypeDefinitionBoolean_strategy)
@settings(max_examples=50)
def test_rif12::exchangefile::datatypedefinitionboolean_instantiation(instance):
    assert isinstance(instance, rif12::ExchangeFile::DatatypeDefinitionBoolean)

@given(instance=rif12::ExchangeFile::DatatypeDefinitionDate_strategy)
@settings(max_examples=50)
def test_rif12::exchangefile::datatypedefinitiondate_instantiation(instance):
    assert isinstance(instance, rif12::ExchangeFile::DatatypeDefinitionDate)

@given(instance=rif12::ExchangeFile::DatatypeDefinitionDate_strategy)
def test_rif12::exchangefile::datatypedefinitiondate_format_type(instance):
    assert isinstance(instance.format, str)


@given(instance=rif12::ExchangeFile::DatatypeDefinitionDate_strategy)
def test_rif12::exchangefile::datatypedefinitiondate_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original

@given(instance=rif12::ExchangeFile::DatatypeDefinitionString_strategy)
@settings(max_examples=50)
def test_rif12::exchangefile::datatypedefinitionstring_instantiation(instance):
    assert isinstance(instance, rif12::ExchangeFile::DatatypeDefinitionString)

@given(instance=rif12::ExchangeFile::DatatypeDefinitionString_strategy)
def test_rif12::exchangefile::datatypedefinitionstring_maxLength_type(instance):
    assert isinstance(instance.maxLength, str)


@given(instance=rif12::ExchangeFile::DatatypeDefinitionString_strategy)
def test_rif12::exchangefile::datatypedefinitionstring_maxLength_setter(instance):
    original = instance.maxLength
    instance.maxLength = original
    assert instance.maxLength == original

@given(instance=rif12::ExchangeFile::DatatypeDefinitionReal_strategy)
@settings(max_examples=50)
def test_rif12::exchangefile::datatypedefinitionreal_instantiation(instance):
    assert isinstance(instance, rif12::ExchangeFile::DatatypeDefinitionReal)

@given(instance=rif12::ExchangeFile::DatatypeDefinitionReal_strategy)
def test_rif12::exchangefile::datatypedefinitionreal_accuracy_type(instance):
    assert isinstance(instance.accuracy, str)


@given(instance=rif12::ExchangeFile::DatatypeDefinitionReal_strategy)
def test_rif12::exchangefile::datatypedefinitionreal_accuracy_setter(instance):
    original = instance.accuracy
    instance.accuracy = original
    assert instance.accuracy == original

@given(instance=rif12::ExchangeFile::DatatypeDefinitionReal_strategy)
def test_rif12::exchangefile::datatypedefinitionreal_max_type(instance):
    assert isinstance(instance.max, str)


@given(instance=rif12::ExchangeFile::DatatypeDefinitionReal_strategy)
def test_rif12::exchangefile::datatypedefinitionreal_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=rif12::ExchangeFile::DatatypeDefinitionReal_strategy)
def test_rif12::exchangefile::datatypedefinitionreal_min_type(instance):
    assert isinstance(instance.min, str)


@given(instance=rif12::ExchangeFile::DatatypeDefinitionReal_strategy)
def test_rif12::exchangefile::datatypedefinitionreal_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=AttributeDefinitionEnumeration_strategy)
@settings(max_examples=50)
def test_attributedefinitionenumeration_instantiation(instance):
    assert isinstance(instance, AttributeDefinitionEnumeration)

@given(instance=rif12::ExchangeFile::EmbeddedValue_strategy)
@settings(max_examples=50)
def test_rif12::exchangefile::embeddedvalue_instantiation(instance):
    assert isinstance(instance, rif12::ExchangeFile::EmbeddedValue)

@given(instance=rif12::ExchangeFile::EmbeddedValue_strategy)
def test_rif12::exchangefile::embeddedvalue_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=rif12::ExchangeFile::EmbeddedValue_strategy)
def test_rif12::exchangefile::embeddedvalue_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=rif12::ExchangeFile::EmbeddedValue_strategy)
def test_rif12::exchangefile::embeddedvalue_otherContent_type(instance):
    assert isinstance(instance.otherContent, str)


@given(instance=rif12::ExchangeFile::EmbeddedValue_strategy)
def test_rif12::exchangefile::embeddedvalue_otherContent_setter(instance):
    original = instance.otherContent
    instance.otherContent = original
    assert instance.otherContent == original

@given(instance=DatatypeDefinition_strategy)
@settings(max_examples=50)
def test_datatypedefinition_instantiation(instance):
    assert isinstance(instance, DatatypeDefinition)

@given(instance=rif12::ExchangeFile::DatatypeDefinitionComplex_strategy)
@settings(max_examples=50)
def test_rif12::exchangefile::datatypedefinitioncomplex_instantiation(instance):
    assert isinstance(instance, rif12::ExchangeFile::DatatypeDefinitionComplex)

@given(instance=rif12::ExchangeFile::DatatypeDefinitionComplex_strategy)
def test_rif12::exchangefile::datatypedefinitioncomplex_embedded_type(instance):
    assert isinstance(instance.embedded, str)


@given(instance=rif12::ExchangeFile::DatatypeDefinitionComplex_strategy)
def test_rif12::exchangefile::datatypedefinitioncomplex_embedded_setter(instance):
    original = instance.embedded
    instance.embedded = original
    assert instance.embedded == original

@given(instance=rif12::ExchangeFile::DatatypeDefinitionSimple_strategy)
@settings(max_examples=50)
def test_rif12::exchangefile::datatypedefinitionsimple_instantiation(instance):
    assert isinstance(instance, rif12::ExchangeFile::DatatypeDefinitionSimple)

@given(instance=rif12::ExchangeFile::DatatypeDefinitionEnumeration_strategy)
@settings(max_examples=50)
def test_rif12::exchangefile::datatypedefinitionenumeration_instantiation(instance):
    assert isinstance(instance, rif12::ExchangeFile::DatatypeDefinitionEnumeration)

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

@given(instance=SpecGroupHierarchy_strategy)
@settings(max_examples=50)
def test_specgrouphierarchy_instantiation(instance):
    assert isinstance(instance, SpecGroupHierarchy)

@given(instance=SpecHierarchyRoot_strategy)
@settings(max_examples=50)
def test_spechierarchyroot_instantiation(instance):
    assert isinstance(instance, SpecHierarchyRoot)

@given(instance=SpecObject_strategy)
@settings(max_examples=50)
def test_specobject_instantiation(instance):
    assert isinstance(instance, SpecObject)

@given(instance=AttributeDefinition_strategy)
@settings(max_examples=50)
def test_attributedefinition_instantiation(instance):
    assert isinstance(instance, AttributeDefinition)

@given(instance=rif12::ExchangeFile::AttributeDefinitionComplex_strategy)
@settings(max_examples=50)
def test_rif12::exchangefile::attributedefinitioncomplex_instantiation(instance):
    assert isinstance(instance, rif12::ExchangeFile::AttributeDefinitionComplex)

@given(instance=rif12::ExchangeFile::AttributeDefinitionSimple_strategy)
@settings(max_examples=50)
def test_rif12::exchangefile::attributedefinitionsimple_instantiation(instance):
    assert isinstance(instance, rif12::ExchangeFile::AttributeDefinitionSimple)

@given(instance=rif12::ExchangeFile::AttributeDefinitionEnumeration_strategy)
@settings(max_examples=50)
def test_rif12::exchangefile::attributedefinitionenumeration_instantiation(instance):
    assert isinstance(instance, rif12::ExchangeFile::AttributeDefinitionEnumeration)

@given(instance=rif12::ExchangeFile::AttributeDefinitionEnumeration_strategy)
def test_rif12::exchangefile::attributedefinitionenumeration_multiValued_type(instance):
    assert isinstance(instance.multiValued, str)


@given(instance=rif12::ExchangeFile::AttributeDefinitionEnumeration_strategy)
def test_rif12::exchangefile::attributedefinitionenumeration_multiValued_setter(instance):
    original = instance.multiValued
    instance.multiValued = original
    assert instance.multiValued == original

@given(instance=rif12::ExchangeFile::Identifiable_strategy)
@settings(max_examples=50)
def test_rif12::exchangefile::identifiable_instantiation(instance):
    assert isinstance(instance, rif12::ExchangeFile::Identifiable)

@given(instance=rif12::ExchangeFile::Identifiable_strategy)
def test_rif12::exchangefile::identifiable_lastChange_type(instance):
    assert isinstance(instance.lastChange, str)


@given(instance=rif12::ExchangeFile::Identifiable_strategy)
def test_rif12::exchangefile::identifiable_lastChange_setter(instance):
    original = instance.lastChange
    instance.lastChange = original
    assert instance.lastChange == original

@given(instance=rif12::ExchangeFile::Identifiable_strategy)
def test_rif12::exchangefile::identifiable_longName_type(instance):
    assert isinstance(instance.longName, str)


@given(instance=rif12::ExchangeFile::Identifiable_strategy)
def test_rif12::exchangefile::identifiable_longName_setter(instance):
    original = instance.longName
    instance.longName = original
    assert instance.longName == original

@given(instance=rif12::ExchangeFile::Identifiable_strategy)
def test_rif12::exchangefile::identifiable_desc_type(instance):
    assert isinstance(instance.desc, str)


@given(instance=rif12::ExchangeFile::Identifiable_strategy)
def test_rif12::exchangefile::identifiable_desc_setter(instance):
    original = instance.desc
    instance.desc = original
    assert instance.desc == original

@given(instance=rif12::ExchangeFile::Identifiable_strategy)
def test_rif12::exchangefile::identifiable_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=rif12::ExchangeFile::Identifiable_strategy)
def test_rif12::exchangefile::identifiable_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=RelationGroup_strategy)
@settings(max_examples=50)
def test_relationgroup_instantiation(instance):
    assert isinstance(instance, RelationGroup)

@given(instance=SpecElementWithUserDefinedAttributes_strategy)
@settings(max_examples=50)
def test_specelementwithuserdefinedattributes_instantiation(instance):
    assert isinstance(instance, SpecElementWithUserDefinedAttributes)

@given(instance=rif12::ExchangeFile::SpecGroupHierarchyRoot_strategy)
@settings(max_examples=50)
def test_rif12::exchangefile::specgrouphierarchyroot_instantiation(instance):
    assert isinstance(instance, rif12::ExchangeFile::SpecGroupHierarchyRoot)

@given(instance=rif12::ExchangeFile::SpecGroup_strategy)
@settings(max_examples=50)
def test_rif12::exchangefile::specgroup_instantiation(instance):
    assert isinstance(instance, rif12::ExchangeFile::SpecGroup)

@given(instance=rif12::ExchangeFile::SpecRelation_strategy)
@settings(max_examples=50)
def test_rif12::exchangefile::specrelation_instantiation(instance):
    assert isinstance(instance, rif12::ExchangeFile::SpecRelation)

@given(instance=rif12::ExchangeFile::SpecObject_strategy)
@settings(max_examples=50)
def test_rif12::exchangefile::specobject_instantiation(instance):
    assert isinstance(instance, rif12::ExchangeFile::SpecObject)

@given(instance=rif12::ExchangeFile::SpecHierarchyRoot_strategy)
@settings(max_examples=50)
def test_rif12::exchangefile::spechierarchyroot_instantiation(instance):
    assert isinstance(instance, rif12::ExchangeFile::SpecHierarchyRoot)

@given(instance=AttributeValue_strategy)
@settings(max_examples=50)
def test_attributevalue_instantiation(instance):
    assert isinstance(instance, AttributeValue)

@given(instance=rif12::ExchangeFile::AttributeValueComplex_strategy)
@settings(max_examples=50)
def test_rif12::exchangefile::attributevaluecomplex_instantiation(instance):
    assert isinstance(instance, rif12::ExchangeFile::AttributeValueComplex)

@given(instance=rif12::ExchangeFile::AttributeValueSimple_strategy)
@settings(max_examples=50)
def test_rif12::exchangefile::attributevaluesimple_instantiation(instance):
    assert isinstance(instance, rif12::ExchangeFile::AttributeValueSimple)

@given(instance=rif12::ExchangeFile::AttributeValueSimple_strategy)
def test_rif12::exchangefile::attributevaluesimple_theValue_type(instance):
    assert isinstance(instance.theValue, str)


@given(instance=rif12::ExchangeFile::AttributeValueSimple_strategy)
def test_rif12::exchangefile::attributevaluesimple_theValue_setter(instance):
    original = instance.theValue
    instance.theValue = original
    assert instance.theValue == original

@given(instance=rif12::ExchangeFile::AttributeValueEnumeration_strategy)
@settings(max_examples=50)
def test_rif12::exchangefile::attributevalueenumeration_instantiation(instance):
    assert isinstance(instance, rif12::ExchangeFile::AttributeValueEnumeration)

@given(instance=SpecType_strategy)
@settings(max_examples=50)
def test_spectype_instantiation(instance):
    assert isinstance(instance, SpecType)

@given(instance=Identifiable_strategy)
@settings(max_examples=50)
def test_identifiable_instantiation(instance):
    assert isinstance(instance, Identifiable)

@given(instance=rif12::ExchangeFile::AccessPolicy_strategy)
@settings(max_examples=50)
def test_rif12::exchangefile::accesspolicy_instantiation(instance):
    assert isinstance(instance, rif12::ExchangeFile::AccessPolicy)

@given(instance=rif12::ExchangeFile::AccessPolicy_strategy)
def test_rif12::exchangefile::accesspolicy_accessMode_type(instance):
    assert isinstance(instance.accessMode, str)


@given(instance=rif12::ExchangeFile::AccessPolicy_strategy)
def test_rif12::exchangefile::accesspolicy_accessMode_setter(instance):
    original = instance.accessMode
    instance.accessMode = original
    assert instance.accessMode == original

@given(instance=rif12::ExchangeFile::EnumValue_strategy)
@settings(max_examples=50)
def test_rif12::exchangefile::enumvalue_instantiation(instance):
    assert isinstance(instance, rif12::ExchangeFile::EnumValue)

@given(instance=rif12::ExchangeFile::SpecType_strategy)
@settings(max_examples=50)
def test_rif12::exchangefile::spectype_instantiation(instance):
    assert isinstance(instance, rif12::ExchangeFile::SpecType)

@given(instance=rif12::ExchangeFile::AttributeValue_strategy)
@settings(max_examples=50)
def test_rif12::exchangefile::attributevalue_instantiation(instance):
    assert isinstance(instance, rif12::ExchangeFile::AttributeValue)

@given(instance=rif12::ExchangeFile::DatatypeDefinition_strategy)
@settings(max_examples=50)
def test_rif12::exchangefile::datatypedefinition_instantiation(instance):
    assert isinstance(instance, rif12::ExchangeFile::DatatypeDefinition)

@given(instance=rif12::ExchangeFile::SpecHierarchy_strategy)
@settings(max_examples=50)
def test_rif12::exchangefile::spechierarchy_instantiation(instance):
    assert isinstance(instance, rif12::ExchangeFile::SpecHierarchy)

@given(instance=rif12::ExchangeFile::SpecGroupHierarchy_strategy)
@settings(max_examples=50)
def test_rif12::exchangefile::specgrouphierarchy_instantiation(instance):
    assert isinstance(instance, rif12::ExchangeFile::SpecGroupHierarchy)

@given(instance=rif12::ExchangeFile::AttributeDefinition_strategy)
@settings(max_examples=50)
def test_rif12::exchangefile::attributedefinition_instantiation(instance):
    assert isinstance(instance, rif12::ExchangeFile::AttributeDefinition)

@given(instance=rif12::ExchangeFile::RelationGroup_strategy)
@settings(max_examples=50)
def test_rif12::exchangefile::relationgroup_instantiation(instance):
    assert isinstance(instance, rif12::ExchangeFile::RelationGroup)

@given(instance=rif12::ExchangeFile::SpecElementWithUserDefinedAttributes_strategy)
@settings(max_examples=50)
def test_rif12::exchangefile::specelementwithuserdefinedattributes_instantiation(instance):
    assert isinstance(instance, rif12::ExchangeFile::SpecElementWithUserDefinedAttributes)

@given(instance=SpecHierarchy_strategy)
@settings(max_examples=50)
def test_spechierarchy_instantiation(instance):
    assert isinstance(instance, SpecHierarchy)
