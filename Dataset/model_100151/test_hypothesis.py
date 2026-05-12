import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    connection::ConceptTarget,
    MetadataTable,
    connection::SubscriberTable,
    connection::SchemaTarget,
    connection::XmlXPathLoopDescriptor,
    SAPFunctionParameterTable,
    connection::SAPTestInputParameterTable,
    connection::CDCConnection,
    connection::OutputSAPFunctionParameterTable,
    connection::InputSAPFunctionParameterTable,
    FileConnection,
    connection::EbcdicConnection,
    connection::FileExcelConnection,
    connection::RegexpFileConnection,
    connection::HL7Connection,
    connection::PositionalFileConnection,
    connection::DelimitedFileConnection,
    connection::Concept,
    Connection,
    connection::SalesforceSchemaConnection,
    connection::XmlFileConnection,
    connection::MDMConnection,
    connection::WSDLSchemaConnection,
    connection::GenericSchemaConnection,
    connection::LdifFileConnection,
    connection::SAPConnection,
    connection::DatabaseConnection,
    connection::LDAPSchemaConnection,
    connection::FileConnection,
    connection::AbstractMetadataObject,
    AbstractMetadataObject,
    connection::SAPFunctionUnit,
    connection::Query,
    connection::SAPFunctionParameterColumn,
    connection::CDCType,
    connection::SAPFunctionParameterTable,
    connection::Metadata,
    connection::MetadataColumn,
    connection::QueriesConnection,
    connection::MetadataTable,
    connection::Connection,
    RowSeparator,
    DatabaseProperties,
    FieldSeparator,
    Escape,
    FileFormat,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_connection::concepttarget_is_not_abstract():
    assert not inspect.isabstract(connection::ConceptTarget)


def test_connection::concepttarget_constructor_exists():
    assert callable(connection::ConceptTarget.__init__)


def test_connection::concepttarget_constructor_args():
    sig = inspect.signature(connection::ConceptTarget.__init__)
    params = list(sig.parameters.keys())
    assert "RelativeLoopExpression" in params, "Missing parameter 'RelativeLoopExpression'"
    assert "targetName" in params, "Missing parameter 'targetName'"

def test_connection::concepttarget_has_RelativeLoopExpression():
    assert hasattr(connection::ConceptTarget, "RelativeLoopExpression")
    descriptor = None
    for klass in connection::ConceptTarget.__mro__:
        if "RelativeLoopExpression" in klass.__dict__:
            descriptor = klass.__dict__["RelativeLoopExpression"]
            break
    assert isinstance(descriptor, property)

def test_connection::concepttarget_has_targetName():
    assert hasattr(connection::ConceptTarget, "targetName")
    descriptor = None
    for klass in connection::ConceptTarget.__mro__:
        if "targetName" in klass.__dict__:
            descriptor = klass.__dict__["targetName"]
            break
    assert isinstance(descriptor, property)



def test_metadatatable_is_not_abstract():
    assert not inspect.isabstract(MetadataTable)


def test_metadatatable_constructor_exists():
    assert callable(MetadataTable.__init__)


def test_metadatatable_constructor_args():
    sig = inspect.signature(MetadataTable.__init__)
    params = list(sig.parameters.keys())



def test_connection::subscribertable_is_not_abstract():
    assert not inspect.isabstract(connection::SubscriberTable)


def test_connection::subscribertable_constructor_exists():
    assert callable(connection::SubscriberTable.__init__)


def test_connection::subscribertable_constructor_args():
    sig = inspect.signature(connection::SubscriberTable.__init__)
    params = list(sig.parameters.keys())
    assert "system" in params, "Missing parameter 'system'"

def test_connection::subscribertable_has_system():
    assert hasattr(connection::SubscriberTable, "system")
    descriptor = None
    for klass in connection::SubscriberTable.__mro__:
        if "system" in klass.__dict__:
            descriptor = klass.__dict__["system"]
            break
    assert isinstance(descriptor, property)



def test_connection::schematarget_is_not_abstract():
    assert not inspect.isabstract(connection::SchemaTarget)


def test_connection::schematarget_constructor_exists():
    assert callable(connection::SchemaTarget.__init__)


def test_connection::schematarget_constructor_args():
    sig = inspect.signature(connection::SchemaTarget.__init__)
    params = list(sig.parameters.keys())
    assert "TagName" in params, "Missing parameter 'TagName'"
    assert "RelativeXPathQuery" in params, "Missing parameter 'RelativeXPathQuery'"

def test_connection::schematarget_has_TagName():
    assert hasattr(connection::SchemaTarget, "TagName")
    descriptor = None
    for klass in connection::SchemaTarget.__mro__:
        if "TagName" in klass.__dict__:
            descriptor = klass.__dict__["TagName"]
            break
    assert isinstance(descriptor, property)

def test_connection::schematarget_has_RelativeXPathQuery():
    assert hasattr(connection::SchemaTarget, "RelativeXPathQuery")
    descriptor = None
    for klass in connection::SchemaTarget.__mro__:
        if "RelativeXPathQuery" in klass.__dict__:
            descriptor = klass.__dict__["RelativeXPathQuery"]
            break
    assert isinstance(descriptor, property)



def test_connection::xmlxpathloopdescriptor_is_not_abstract():
    assert not inspect.isabstract(connection::XmlXPathLoopDescriptor)


def test_connection::xmlxpathloopdescriptor_constructor_exists():
    assert callable(connection::XmlXPathLoopDescriptor.__init__)


def test_connection::xmlxpathloopdescriptor_constructor_args():
    sig = inspect.signature(connection::XmlXPathLoopDescriptor.__init__)
    params = list(sig.parameters.keys())
    assert "LimitBoucle" in params, "Missing parameter 'LimitBoucle'"
    assert "AbsoluteXPathQuery" in params, "Missing parameter 'AbsoluteXPathQuery'"

def test_connection::xmlxpathloopdescriptor_has_LimitBoucle():
    assert hasattr(connection::XmlXPathLoopDescriptor, "LimitBoucle")
    descriptor = None
    for klass in connection::XmlXPathLoopDescriptor.__mro__:
        if "LimitBoucle" in klass.__dict__:
            descriptor = klass.__dict__["LimitBoucle"]
            break
    assert isinstance(descriptor, property)

def test_connection::xmlxpathloopdescriptor_has_AbsoluteXPathQuery():
    assert hasattr(connection::XmlXPathLoopDescriptor, "AbsoluteXPathQuery")
    descriptor = None
    for klass in connection::XmlXPathLoopDescriptor.__mro__:
        if "AbsoluteXPathQuery" in klass.__dict__:
            descriptor = klass.__dict__["AbsoluteXPathQuery"]
            break
    assert isinstance(descriptor, property)



def test_sapfunctionparametertable_is_not_abstract():
    assert not inspect.isabstract(SAPFunctionParameterTable)


def test_sapfunctionparametertable_constructor_exists():
    assert callable(SAPFunctionParameterTable.__init__)


def test_sapfunctionparametertable_constructor_args():
    sig = inspect.signature(SAPFunctionParameterTable.__init__)
    params = list(sig.parameters.keys())



def test_connection::saptestinputparametertable_is_not_abstract():
    assert not inspect.isabstract(connection::SAPTestInputParameterTable)


def test_connection::saptestinputparametertable_constructor_exists():
    assert callable(connection::SAPTestInputParameterTable.__init__)


def test_connection::saptestinputparametertable_constructor_args():
    sig = inspect.signature(connection::SAPTestInputParameterTable.__init__)
    params = list(sig.parameters.keys())



def test_connection::cdcconnection_is_not_abstract():
    assert not inspect.isabstract(connection::CDCConnection)


def test_connection::cdcconnection_constructor_exists():
    assert callable(connection::CDCConnection.__init__)


def test_connection::cdcconnection_constructor_args():
    sig = inspect.signature(connection::CDCConnection.__init__)
    params = list(sig.parameters.keys())



def test_connection::outputsapfunctionparametertable_is_not_abstract():
    assert not inspect.isabstract(connection::OutputSAPFunctionParameterTable)


def test_connection::outputsapfunctionparametertable_constructor_exists():
    assert callable(connection::OutputSAPFunctionParameterTable.__init__)


def test_connection::outputsapfunctionparametertable_constructor_args():
    sig = inspect.signature(connection::OutputSAPFunctionParameterTable.__init__)
    params = list(sig.parameters.keys())



def test_connection::inputsapfunctionparametertable_is_not_abstract():
    assert not inspect.isabstract(connection::InputSAPFunctionParameterTable)


def test_connection::inputsapfunctionparametertable_constructor_exists():
    assert callable(connection::InputSAPFunctionParameterTable.__init__)


def test_connection::inputsapfunctionparametertable_constructor_args():
    sig = inspect.signature(connection::InputSAPFunctionParameterTable.__init__)
    params = list(sig.parameters.keys())



def test_fileconnection_is_not_abstract():
    assert not inspect.isabstract(FileConnection)


def test_fileconnection_constructor_exists():
    assert callable(FileConnection.__init__)


def test_fileconnection_constructor_args():
    sig = inspect.signature(FileConnection.__init__)
    params = list(sig.parameters.keys())



def test_connection::ebcdicconnection_is_not_abstract():
    assert not inspect.isabstract(connection::EbcdicConnection)


def test_connection::ebcdicconnection_constructor_exists():
    assert callable(connection::EbcdicConnection.__init__)


def test_connection::ebcdicconnection_constructor_args():
    sig = inspect.signature(connection::EbcdicConnection.__init__)
    params = list(sig.parameters.keys())
    assert "MidFile" in params, "Missing parameter 'MidFile'"
    assert "DataFile" in params, "Missing parameter 'DataFile'"

def test_connection::ebcdicconnection_has_MidFile():
    assert hasattr(connection::EbcdicConnection, "MidFile")
    descriptor = None
    for klass in connection::EbcdicConnection.__mro__:
        if "MidFile" in klass.__dict__:
            descriptor = klass.__dict__["MidFile"]
            break
    assert isinstance(descriptor, property)

def test_connection::ebcdicconnection_has_DataFile():
    assert hasattr(connection::EbcdicConnection, "DataFile")
    descriptor = None
    for klass in connection::EbcdicConnection.__mro__:
        if "DataFile" in klass.__dict__:
            descriptor = klass.__dict__["DataFile"]
            break
    assert isinstance(descriptor, property)



def test_connection::fileexcelconnection_is_not_abstract():
    assert not inspect.isabstract(connection::FileExcelConnection)


def test_connection::fileexcelconnection_constructor_exists():
    assert callable(connection::FileExcelConnection.__init__)


def test_connection::fileexcelconnection_constructor_args():
    sig = inspect.signature(connection::FileExcelConnection.__init__)
    params = list(sig.parameters.keys())
    assert "thousandSeparator" in params, "Missing parameter 'thousandSeparator'"
    assert "sheetList" in params, "Missing parameter 'sheetList'"
    assert "decimalSeparator" in params, "Missing parameter 'decimalSeparator'"
    assert "lastColumn" in params, "Missing parameter 'lastColumn'"
    assert "selectAllSheets" in params, "Missing parameter 'selectAllSheets'"
    assert "SheetName" in params, "Missing parameter 'SheetName'"
    assert "sheetColumns" in params, "Missing parameter 'sheetColumns'"
    assert "firstColumn" in params, "Missing parameter 'firstColumn'"
    assert "advancedSpearator" in params, "Missing parameter 'advancedSpearator'"

def test_connection::fileexcelconnection_has_thousandSeparator():
    assert hasattr(connection::FileExcelConnection, "thousandSeparator")
    descriptor = None
    for klass in connection::FileExcelConnection.__mro__:
        if "thousandSeparator" in klass.__dict__:
            descriptor = klass.__dict__["thousandSeparator"]
            break
    assert isinstance(descriptor, property)

def test_connection::fileexcelconnection_has_sheetList():
    assert hasattr(connection::FileExcelConnection, "sheetList")
    descriptor = None
    for klass in connection::FileExcelConnection.__mro__:
        if "sheetList" in klass.__dict__:
            descriptor = klass.__dict__["sheetList"]
            break
    assert isinstance(descriptor, property)

def test_connection::fileexcelconnection_has_decimalSeparator():
    assert hasattr(connection::FileExcelConnection, "decimalSeparator")
    descriptor = None
    for klass in connection::FileExcelConnection.__mro__:
        if "decimalSeparator" in klass.__dict__:
            descriptor = klass.__dict__["decimalSeparator"]
            break
    assert isinstance(descriptor, property)

def test_connection::fileexcelconnection_has_lastColumn():
    assert hasattr(connection::FileExcelConnection, "lastColumn")
    descriptor = None
    for klass in connection::FileExcelConnection.__mro__:
        if "lastColumn" in klass.__dict__:
            descriptor = klass.__dict__["lastColumn"]
            break
    assert isinstance(descriptor, property)

def test_connection::fileexcelconnection_has_selectAllSheets():
    assert hasattr(connection::FileExcelConnection, "selectAllSheets")
    descriptor = None
    for klass in connection::FileExcelConnection.__mro__:
        if "selectAllSheets" in klass.__dict__:
            descriptor = klass.__dict__["selectAllSheets"]
            break
    assert isinstance(descriptor, property)

def test_connection::fileexcelconnection_has_SheetName():
    assert hasattr(connection::FileExcelConnection, "SheetName")
    descriptor = None
    for klass in connection::FileExcelConnection.__mro__:
        if "SheetName" in klass.__dict__:
            descriptor = klass.__dict__["SheetName"]
            break
    assert isinstance(descriptor, property)

def test_connection::fileexcelconnection_has_sheetColumns():
    assert hasattr(connection::FileExcelConnection, "sheetColumns")
    descriptor = None
    for klass in connection::FileExcelConnection.__mro__:
        if "sheetColumns" in klass.__dict__:
            descriptor = klass.__dict__["sheetColumns"]
            break
    assert isinstance(descriptor, property)

def test_connection::fileexcelconnection_has_firstColumn():
    assert hasattr(connection::FileExcelConnection, "firstColumn")
    descriptor = None
    for klass in connection::FileExcelConnection.__mro__:
        if "firstColumn" in klass.__dict__:
            descriptor = klass.__dict__["firstColumn"]
            break
    assert isinstance(descriptor, property)

def test_connection::fileexcelconnection_has_advancedSpearator():
    assert hasattr(connection::FileExcelConnection, "advancedSpearator")
    descriptor = None
    for klass in connection::FileExcelConnection.__mro__:
        if "advancedSpearator" in klass.__dict__:
            descriptor = klass.__dict__["advancedSpearator"]
            break
    assert isinstance(descriptor, property)



def test_connection::regexpfileconnection_is_not_abstract():
    assert not inspect.isabstract(connection::RegexpFileConnection)


def test_connection::regexpfileconnection_constructor_exists():
    assert callable(connection::RegexpFileConnection.__init__)


def test_connection::regexpfileconnection_constructor_args():
    sig = inspect.signature(connection::RegexpFileConnection.__init__)
    params = list(sig.parameters.keys())
    assert "FieldSeparatorType" in params, "Missing parameter 'FieldSeparatorType'"

def test_connection::regexpfileconnection_has_FieldSeparatorType():
    assert hasattr(connection::RegexpFileConnection, "FieldSeparatorType")
    descriptor = None
    for klass in connection::RegexpFileConnection.__mro__:
        if "FieldSeparatorType" in klass.__dict__:
            descriptor = klass.__dict__["FieldSeparatorType"]
            break
    assert isinstance(descriptor, property)



def test_connection::hl7connection_is_not_abstract():
    assert not inspect.isabstract(connection::HL7Connection)


def test_connection::hl7connection_constructor_exists():
    assert callable(connection::HL7Connection.__init__)


def test_connection::hl7connection_constructor_args():
    sig = inspect.signature(connection::HL7Connection.__init__)
    params = list(sig.parameters.keys())
    assert "EndChar" in params, "Missing parameter 'EndChar'"
    assert "StartChar" in params, "Missing parameter 'StartChar'"

def test_connection::hl7connection_has_EndChar():
    assert hasattr(connection::HL7Connection, "EndChar")
    descriptor = None
    for klass in connection::HL7Connection.__mro__:
        if "EndChar" in klass.__dict__:
            descriptor = klass.__dict__["EndChar"]
            break
    assert isinstance(descriptor, property)

def test_connection::hl7connection_has_StartChar():
    assert hasattr(connection::HL7Connection, "StartChar")
    descriptor = None
    for klass in connection::HL7Connection.__mro__:
        if "StartChar" in klass.__dict__:
            descriptor = klass.__dict__["StartChar"]
            break
    assert isinstance(descriptor, property)



def test_connection::positionalfileconnection_is_not_abstract():
    assert not inspect.isabstract(connection::PositionalFileConnection)


def test_connection::positionalfileconnection_constructor_exists():
    assert callable(connection::PositionalFileConnection.__init__)


def test_connection::positionalfileconnection_constructor_args():
    sig = inspect.signature(connection::PositionalFileConnection.__init__)
    params = list(sig.parameters.keys())



def test_connection::delimitedfileconnection_is_not_abstract():
    assert not inspect.isabstract(connection::DelimitedFileConnection)


def test_connection::delimitedfileconnection_constructor_exists():
    assert callable(connection::DelimitedFileConnection.__init__)


def test_connection::delimitedfileconnection_constructor_args():
    sig = inspect.signature(connection::DelimitedFileConnection.__init__)
    params = list(sig.parameters.keys())
    assert "FieldSeparatorType" in params, "Missing parameter 'FieldSeparatorType'"
    assert "splitRecord" in params, "Missing parameter 'splitRecord'"

def test_connection::delimitedfileconnection_has_FieldSeparatorType():
    assert hasattr(connection::DelimitedFileConnection, "FieldSeparatorType")
    descriptor = None
    for klass in connection::DelimitedFileConnection.__mro__:
        if "FieldSeparatorType" in klass.__dict__:
            descriptor = klass.__dict__["FieldSeparatorType"]
            break
    assert isinstance(descriptor, property)

def test_connection::delimitedfileconnection_has_splitRecord():
    assert hasattr(connection::DelimitedFileConnection, "splitRecord")
    descriptor = None
    for klass in connection::DelimitedFileConnection.__mro__:
        if "splitRecord" in klass.__dict__:
            descriptor = klass.__dict__["splitRecord"]
            break
    assert isinstance(descriptor, property)



def test_connection::concept_is_not_abstract():
    assert not inspect.isabstract(connection::Concept)


def test_connection::concept_constructor_exists():
    assert callable(connection::Concept.__init__)


def test_connection::concept_constructor_args():
    sig = inspect.signature(connection::Concept.__init__)
    params = list(sig.parameters.keys())
    assert "LoopExpression" in params, "Missing parameter 'LoopExpression'"
    assert "LoopLimit" in params, "Missing parameter 'LoopLimit'"

def test_connection::concept_has_LoopExpression():
    assert hasattr(connection::Concept, "LoopExpression")
    descriptor = None
    for klass in connection::Concept.__mro__:
        if "LoopExpression" in klass.__dict__:
            descriptor = klass.__dict__["LoopExpression"]
            break
    assert isinstance(descriptor, property)

def test_connection::concept_has_LoopLimit():
    assert hasattr(connection::Concept, "LoopLimit")
    descriptor = None
    for klass in connection::Concept.__mro__:
        if "LoopLimit" in klass.__dict__:
            descriptor = klass.__dict__["LoopLimit"]
            break
    assert isinstance(descriptor, property)



def test_connection_is_not_abstract():
    assert not inspect.isabstract(Connection)


def test_connection_constructor_exists():
    assert callable(Connection.__init__)


def test_connection_constructor_args():
    sig = inspect.signature(Connection.__init__)
    params = list(sig.parameters.keys())



def test_connection::salesforceschemaconnection_is_not_abstract():
    assert not inspect.isabstract(connection::SalesforceSchemaConnection)


def test_connection::salesforceschemaconnection_constructor_exists():
    assert callable(connection::SalesforceSchemaConnection.__init__)


def test_connection::salesforceschemaconnection_constructor_args():
    sig = inspect.signature(connection::SalesforceSchemaConnection.__init__)
    params = list(sig.parameters.keys())
    assert "userName" in params, "Missing parameter 'userName'"
    assert "useCustomModuleName" in params, "Missing parameter 'useCustomModuleName'"
    assert "webServiceUrl" in params, "Missing parameter 'webServiceUrl'"
    assert "proxyHost" in params, "Missing parameter 'proxyHost'"
    assert "password" in params, "Missing parameter 'password'"
    assert "timeOut" in params, "Missing parameter 'timeOut'"
    assert "proxyPort" in params, "Missing parameter 'proxyPort'"
    assert "useHttpProxy" in params, "Missing parameter 'useHttpProxy'"
    assert "batchSize" in params, "Missing parameter 'batchSize'"
    assert "queryCondition" in params, "Missing parameter 'queryCondition'"
    assert "moduleName" in params, "Missing parameter 'moduleName'"
    assert "useProxy" in params, "Missing parameter 'useProxy'"
    assert "proxyUsername" in params, "Missing parameter 'proxyUsername'"
    assert "proxyPassword" in params, "Missing parameter 'proxyPassword'"
    assert "useAlphbet" in params, "Missing parameter 'useAlphbet'"

def test_connection::salesforceschemaconnection_has_userName():
    assert hasattr(connection::SalesforceSchemaConnection, "userName")
    descriptor = None
    for klass in connection::SalesforceSchemaConnection.__mro__:
        if "userName" in klass.__dict__:
            descriptor = klass.__dict__["userName"]
            break
    assert isinstance(descriptor, property)

def test_connection::salesforceschemaconnection_has_useCustomModuleName():
    assert hasattr(connection::SalesforceSchemaConnection, "useCustomModuleName")
    descriptor = None
    for klass in connection::SalesforceSchemaConnection.__mro__:
        if "useCustomModuleName" in klass.__dict__:
            descriptor = klass.__dict__["useCustomModuleName"]
            break
    assert isinstance(descriptor, property)

def test_connection::salesforceschemaconnection_has_webServiceUrl():
    assert hasattr(connection::SalesforceSchemaConnection, "webServiceUrl")
    descriptor = None
    for klass in connection::SalesforceSchemaConnection.__mro__:
        if "webServiceUrl" in klass.__dict__:
            descriptor = klass.__dict__["webServiceUrl"]
            break
    assert isinstance(descriptor, property)

def test_connection::salesforceschemaconnection_has_proxyHost():
    assert hasattr(connection::SalesforceSchemaConnection, "proxyHost")
    descriptor = None
    for klass in connection::SalesforceSchemaConnection.__mro__:
        if "proxyHost" in klass.__dict__:
            descriptor = klass.__dict__["proxyHost"]
            break
    assert isinstance(descriptor, property)

def test_connection::salesforceschemaconnection_has_password():
    assert hasattr(connection::SalesforceSchemaConnection, "password")
    descriptor = None
    for klass in connection::SalesforceSchemaConnection.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_connection::salesforceschemaconnection_has_timeOut():
    assert hasattr(connection::SalesforceSchemaConnection, "timeOut")
    descriptor = None
    for klass in connection::SalesforceSchemaConnection.__mro__:
        if "timeOut" in klass.__dict__:
            descriptor = klass.__dict__["timeOut"]
            break
    assert isinstance(descriptor, property)

def test_connection::salesforceschemaconnection_has_proxyPort():
    assert hasattr(connection::SalesforceSchemaConnection, "proxyPort")
    descriptor = None
    for klass in connection::SalesforceSchemaConnection.__mro__:
        if "proxyPort" in klass.__dict__:
            descriptor = klass.__dict__["proxyPort"]
            break
    assert isinstance(descriptor, property)

def test_connection::salesforceschemaconnection_has_useHttpProxy():
    assert hasattr(connection::SalesforceSchemaConnection, "useHttpProxy")
    descriptor = None
    for klass in connection::SalesforceSchemaConnection.__mro__:
        if "useHttpProxy" in klass.__dict__:
            descriptor = klass.__dict__["useHttpProxy"]
            break
    assert isinstance(descriptor, property)

def test_connection::salesforceschemaconnection_has_batchSize():
    assert hasattr(connection::SalesforceSchemaConnection, "batchSize")
    descriptor = None
    for klass in connection::SalesforceSchemaConnection.__mro__:
        if "batchSize" in klass.__dict__:
            descriptor = klass.__dict__["batchSize"]
            break
    assert isinstance(descriptor, property)

def test_connection::salesforceschemaconnection_has_queryCondition():
    assert hasattr(connection::SalesforceSchemaConnection, "queryCondition")
    descriptor = None
    for klass in connection::SalesforceSchemaConnection.__mro__:
        if "queryCondition" in klass.__dict__:
            descriptor = klass.__dict__["queryCondition"]
            break
    assert isinstance(descriptor, property)

def test_connection::salesforceschemaconnection_has_moduleName():
    assert hasattr(connection::SalesforceSchemaConnection, "moduleName")
    descriptor = None
    for klass in connection::SalesforceSchemaConnection.__mro__:
        if "moduleName" in klass.__dict__:
            descriptor = klass.__dict__["moduleName"]
            break
    assert isinstance(descriptor, property)

def test_connection::salesforceschemaconnection_has_useProxy():
    assert hasattr(connection::SalesforceSchemaConnection, "useProxy")
    descriptor = None
    for klass in connection::SalesforceSchemaConnection.__mro__:
        if "useProxy" in klass.__dict__:
            descriptor = klass.__dict__["useProxy"]
            break
    assert isinstance(descriptor, property)

def test_connection::salesforceschemaconnection_has_proxyUsername():
    assert hasattr(connection::SalesforceSchemaConnection, "proxyUsername")
    descriptor = None
    for klass in connection::SalesforceSchemaConnection.__mro__:
        if "proxyUsername" in klass.__dict__:
            descriptor = klass.__dict__["proxyUsername"]
            break
    assert isinstance(descriptor, property)

def test_connection::salesforceschemaconnection_has_proxyPassword():
    assert hasattr(connection::SalesforceSchemaConnection, "proxyPassword")
    descriptor = None
    for klass in connection::SalesforceSchemaConnection.__mro__:
        if "proxyPassword" in klass.__dict__:
            descriptor = klass.__dict__["proxyPassword"]
            break
    assert isinstance(descriptor, property)

def test_connection::salesforceschemaconnection_has_useAlphbet():
    assert hasattr(connection::SalesforceSchemaConnection, "useAlphbet")
    descriptor = None
    for klass in connection::SalesforceSchemaConnection.__mro__:
        if "useAlphbet" in klass.__dict__:
            descriptor = klass.__dict__["useAlphbet"]
            break
    assert isinstance(descriptor, property)



def test_connection::xmlfileconnection_is_not_abstract():
    assert not inspect.isabstract(connection::XmlFileConnection)


def test_connection::xmlfileconnection_constructor_exists():
    assert callable(connection::XmlFileConnection.__init__)


def test_connection::xmlfileconnection_constructor_args():
    sig = inspect.signature(connection::XmlFileConnection.__init__)
    params = list(sig.parameters.keys())
    assert "XsdFilePath" in params, "Missing parameter 'XsdFilePath'"
    assert "Encoding" in params, "Missing parameter 'Encoding'"
    assert "XmlFilePath" in params, "Missing parameter 'XmlFilePath'"
    assert "MaskXPattern" in params, "Missing parameter 'MaskXPattern'"
    assert "Guess" in params, "Missing parameter 'Guess'"

def test_connection::xmlfileconnection_has_XsdFilePath():
    assert hasattr(connection::XmlFileConnection, "XsdFilePath")
    descriptor = None
    for klass in connection::XmlFileConnection.__mro__:
        if "XsdFilePath" in klass.__dict__:
            descriptor = klass.__dict__["XsdFilePath"]
            break
    assert isinstance(descriptor, property)

def test_connection::xmlfileconnection_has_Encoding():
    assert hasattr(connection::XmlFileConnection, "Encoding")
    descriptor = None
    for klass in connection::XmlFileConnection.__mro__:
        if "Encoding" in klass.__dict__:
            descriptor = klass.__dict__["Encoding"]
            break
    assert isinstance(descriptor, property)

def test_connection::xmlfileconnection_has_XmlFilePath():
    assert hasattr(connection::XmlFileConnection, "XmlFilePath")
    descriptor = None
    for klass in connection::XmlFileConnection.__mro__:
        if "XmlFilePath" in klass.__dict__:
            descriptor = klass.__dict__["XmlFilePath"]
            break
    assert isinstance(descriptor, property)

def test_connection::xmlfileconnection_has_MaskXPattern():
    assert hasattr(connection::XmlFileConnection, "MaskXPattern")
    descriptor = None
    for klass in connection::XmlFileConnection.__mro__:
        if "MaskXPattern" in klass.__dict__:
            descriptor = klass.__dict__["MaskXPattern"]
            break
    assert isinstance(descriptor, property)

def test_connection::xmlfileconnection_has_Guess():
    assert hasattr(connection::XmlFileConnection, "Guess")
    descriptor = None
    for klass in connection::XmlFileConnection.__mro__:
        if "Guess" in klass.__dict__:
            descriptor = klass.__dict__["Guess"]
            break
    assert isinstance(descriptor, property)



def test_connection::mdmconnection_is_not_abstract():
    assert not inspect.isabstract(connection::MDMConnection)


def test_connection::mdmconnection_constructor_exists():
    assert callable(connection::MDMConnection.__init__)


def test_connection::mdmconnection_constructor_args():
    sig = inspect.signature(connection::MDMConnection.__init__)
    params = list(sig.parameters.keys())
    assert "Password" in params, "Missing parameter 'Password'"
    assert "Datamodel" in params, "Missing parameter 'Datamodel'"
    assert "Datacluster" in params, "Missing parameter 'Datacluster'"
    assert "Username" in params, "Missing parameter 'Username'"
    assert "Server" in params, "Missing parameter 'Server'"
    assert "Universe" in params, "Missing parameter 'Universe'"
    assert "Port" in params, "Missing parameter 'Port'"

def test_connection::mdmconnection_has_Password():
    assert hasattr(connection::MDMConnection, "Password")
    descriptor = None
    for klass in connection::MDMConnection.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)

def test_connection::mdmconnection_has_Datamodel():
    assert hasattr(connection::MDMConnection, "Datamodel")
    descriptor = None
    for klass in connection::MDMConnection.__mro__:
        if "Datamodel" in klass.__dict__:
            descriptor = klass.__dict__["Datamodel"]
            break
    assert isinstance(descriptor, property)

def test_connection::mdmconnection_has_Datacluster():
    assert hasattr(connection::MDMConnection, "Datacluster")
    descriptor = None
    for klass in connection::MDMConnection.__mro__:
        if "Datacluster" in klass.__dict__:
            descriptor = klass.__dict__["Datacluster"]
            break
    assert isinstance(descriptor, property)

def test_connection::mdmconnection_has_Username():
    assert hasattr(connection::MDMConnection, "Username")
    descriptor = None
    for klass in connection::MDMConnection.__mro__:
        if "Username" in klass.__dict__:
            descriptor = klass.__dict__["Username"]
            break
    assert isinstance(descriptor, property)

def test_connection::mdmconnection_has_Server():
    assert hasattr(connection::MDMConnection, "Server")
    descriptor = None
    for klass in connection::MDMConnection.__mro__:
        if "Server" in klass.__dict__:
            descriptor = klass.__dict__["Server"]
            break
    assert isinstance(descriptor, property)

def test_connection::mdmconnection_has_Universe():
    assert hasattr(connection::MDMConnection, "Universe")
    descriptor = None
    for klass in connection::MDMConnection.__mro__:
        if "Universe" in klass.__dict__:
            descriptor = klass.__dict__["Universe"]
            break
    assert isinstance(descriptor, property)

def test_connection::mdmconnection_has_Port():
    assert hasattr(connection::MDMConnection, "Port")
    descriptor = None
    for klass in connection::MDMConnection.__mro__:
        if "Port" in klass.__dict__:
            descriptor = klass.__dict__["Port"]
            break
    assert isinstance(descriptor, property)



def test_connection::wsdlschemaconnection_is_not_abstract():
    assert not inspect.isabstract(connection::WSDLSchemaConnection)


def test_connection::wsdlschemaconnection_constructor_exists():
    assert callable(connection::WSDLSchemaConnection.__init__)


def test_connection::wsdlschemaconnection_constructor_args():
    sig = inspect.signature(connection::WSDLSchemaConnection.__init__)
    params = list(sig.parameters.keys())
    assert "proxyPassword" in params, "Missing parameter 'proxyPassword'"
    assert "Password" in params, "Missing parameter 'Password'"
    assert "EndpointURI" in params, "Missing parameter 'EndpointURI'"
    assert "proxyUser" in params, "Missing parameter 'proxyUser'"
    assert "proxyHost" in params, "Missing parameter 'proxyHost'"
    assert "needAuth" in params, "Missing parameter 'needAuth'"
    assert "proxyPort" in params, "Missing parameter 'proxyPort'"
    assert "parameters" in params, "Missing parameter 'parameters'"
    assert "Encoding" in params, "Missing parameter 'Encoding'"
    assert "methodName" in params, "Missing parameter 'methodName'"
    assert "useProxy" in params, "Missing parameter 'useProxy'"
    assert "UserName" in params, "Missing parameter 'UserName'"
    assert "timeOut" in params, "Missing parameter 'timeOut'"
    assert "WSDL" in params, "Missing parameter 'WSDL'"
    assert "Value" in params, "Missing parameter 'Value'"

def test_connection::wsdlschemaconnection_has_proxyPassword():
    assert hasattr(connection::WSDLSchemaConnection, "proxyPassword")
    descriptor = None
    for klass in connection::WSDLSchemaConnection.__mro__:
        if "proxyPassword" in klass.__dict__:
            descriptor = klass.__dict__["proxyPassword"]
            break
    assert isinstance(descriptor, property)

def test_connection::wsdlschemaconnection_has_Password():
    assert hasattr(connection::WSDLSchemaConnection, "Password")
    descriptor = None
    for klass in connection::WSDLSchemaConnection.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)

def test_connection::wsdlschemaconnection_has_EndpointURI():
    assert hasattr(connection::WSDLSchemaConnection, "EndpointURI")
    descriptor = None
    for klass in connection::WSDLSchemaConnection.__mro__:
        if "EndpointURI" in klass.__dict__:
            descriptor = klass.__dict__["EndpointURI"]
            break
    assert isinstance(descriptor, property)

def test_connection::wsdlschemaconnection_has_proxyUser():
    assert hasattr(connection::WSDLSchemaConnection, "proxyUser")
    descriptor = None
    for klass in connection::WSDLSchemaConnection.__mro__:
        if "proxyUser" in klass.__dict__:
            descriptor = klass.__dict__["proxyUser"]
            break
    assert isinstance(descriptor, property)

def test_connection::wsdlschemaconnection_has_proxyHost():
    assert hasattr(connection::WSDLSchemaConnection, "proxyHost")
    descriptor = None
    for klass in connection::WSDLSchemaConnection.__mro__:
        if "proxyHost" in klass.__dict__:
            descriptor = klass.__dict__["proxyHost"]
            break
    assert isinstance(descriptor, property)

def test_connection::wsdlschemaconnection_has_needAuth():
    assert hasattr(connection::WSDLSchemaConnection, "needAuth")
    descriptor = None
    for klass in connection::WSDLSchemaConnection.__mro__:
        if "needAuth" in klass.__dict__:
            descriptor = klass.__dict__["needAuth"]
            break
    assert isinstance(descriptor, property)

def test_connection::wsdlschemaconnection_has_proxyPort():
    assert hasattr(connection::WSDLSchemaConnection, "proxyPort")
    descriptor = None
    for klass in connection::WSDLSchemaConnection.__mro__:
        if "proxyPort" in klass.__dict__:
            descriptor = klass.__dict__["proxyPort"]
            break
    assert isinstance(descriptor, property)

def test_connection::wsdlschemaconnection_has_parameters():
    assert hasattr(connection::WSDLSchemaConnection, "parameters")
    descriptor = None
    for klass in connection::WSDLSchemaConnection.__mro__:
        if "parameters" in klass.__dict__:
            descriptor = klass.__dict__["parameters"]
            break
    assert isinstance(descriptor, property)

def test_connection::wsdlschemaconnection_has_Encoding():
    assert hasattr(connection::WSDLSchemaConnection, "Encoding")
    descriptor = None
    for klass in connection::WSDLSchemaConnection.__mro__:
        if "Encoding" in klass.__dict__:
            descriptor = klass.__dict__["Encoding"]
            break
    assert isinstance(descriptor, property)

def test_connection::wsdlschemaconnection_has_methodName():
    assert hasattr(connection::WSDLSchemaConnection, "methodName")
    descriptor = None
    for klass in connection::WSDLSchemaConnection.__mro__:
        if "methodName" in klass.__dict__:
            descriptor = klass.__dict__["methodName"]
            break
    assert isinstance(descriptor, property)

def test_connection::wsdlschemaconnection_has_useProxy():
    assert hasattr(connection::WSDLSchemaConnection, "useProxy")
    descriptor = None
    for klass in connection::WSDLSchemaConnection.__mro__:
        if "useProxy" in klass.__dict__:
            descriptor = klass.__dict__["useProxy"]
            break
    assert isinstance(descriptor, property)

def test_connection::wsdlschemaconnection_has_UserName():
    assert hasattr(connection::WSDLSchemaConnection, "UserName")
    descriptor = None
    for klass in connection::WSDLSchemaConnection.__mro__:
        if "UserName" in klass.__dict__:
            descriptor = klass.__dict__["UserName"]
            break
    assert isinstance(descriptor, property)

def test_connection::wsdlschemaconnection_has_timeOut():
    assert hasattr(connection::WSDLSchemaConnection, "timeOut")
    descriptor = None
    for klass in connection::WSDLSchemaConnection.__mro__:
        if "timeOut" in klass.__dict__:
            descriptor = klass.__dict__["timeOut"]
            break
    assert isinstance(descriptor, property)

def test_connection::wsdlschemaconnection_has_WSDL():
    assert hasattr(connection::WSDLSchemaConnection, "WSDL")
    descriptor = None
    for klass in connection::WSDLSchemaConnection.__mro__:
        if "WSDL" in klass.__dict__:
            descriptor = klass.__dict__["WSDL"]
            break
    assert isinstance(descriptor, property)

def test_connection::wsdlschemaconnection_has_Value():
    assert hasattr(connection::WSDLSchemaConnection, "Value")
    descriptor = None
    for klass in connection::WSDLSchemaConnection.__mro__:
        if "Value" in klass.__dict__:
            descriptor = klass.__dict__["Value"]
            break
    assert isinstance(descriptor, property)



def test_connection::genericschemaconnection_is_not_abstract():
    assert not inspect.isabstract(connection::GenericSchemaConnection)


def test_connection::genericschemaconnection_constructor_exists():
    assert callable(connection::GenericSchemaConnection.__init__)


def test_connection::genericschemaconnection_constructor_args():
    sig = inspect.signature(connection::GenericSchemaConnection.__init__)
    params = list(sig.parameters.keys())
    assert "mappingTypeId" in params, "Missing parameter 'mappingTypeId'"
    assert "mappingTypeUsed" in params, "Missing parameter 'mappingTypeUsed'"

def test_connection::genericschemaconnection_has_mappingTypeId():
    assert hasattr(connection::GenericSchemaConnection, "mappingTypeId")
    descriptor = None
    for klass in connection::GenericSchemaConnection.__mro__:
        if "mappingTypeId" in klass.__dict__:
            descriptor = klass.__dict__["mappingTypeId"]
            break
    assert isinstance(descriptor, property)

def test_connection::genericschemaconnection_has_mappingTypeUsed():
    assert hasattr(connection::GenericSchemaConnection, "mappingTypeUsed")
    descriptor = None
    for klass in connection::GenericSchemaConnection.__mro__:
        if "mappingTypeUsed" in klass.__dict__:
            descriptor = klass.__dict__["mappingTypeUsed"]
            break
    assert isinstance(descriptor, property)



def test_connection::ldiffileconnection_is_not_abstract():
    assert not inspect.isabstract(connection::LdifFileConnection)


def test_connection::ldiffileconnection_constructor_exists():
    assert callable(connection::LdifFileConnection.__init__)


def test_connection::ldiffileconnection_constructor_args():
    sig = inspect.signature(connection::LdifFileConnection.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "LimitEntry" in params, "Missing parameter 'LimitEntry'"
    assert "FilePath" in params, "Missing parameter 'FilePath'"
    assert "UseLimit" in params, "Missing parameter 'UseLimit'"
    assert "Server" in params, "Missing parameter 'Server'"

def test_connection::ldiffileconnection_has_value():
    assert hasattr(connection::LdifFileConnection, "value")
    descriptor = None
    for klass in connection::LdifFileConnection.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_connection::ldiffileconnection_has_LimitEntry():
    assert hasattr(connection::LdifFileConnection, "LimitEntry")
    descriptor = None
    for klass in connection::LdifFileConnection.__mro__:
        if "LimitEntry" in klass.__dict__:
            descriptor = klass.__dict__["LimitEntry"]
            break
    assert isinstance(descriptor, property)

def test_connection::ldiffileconnection_has_FilePath():
    assert hasattr(connection::LdifFileConnection, "FilePath")
    descriptor = None
    for klass in connection::LdifFileConnection.__mro__:
        if "FilePath" in klass.__dict__:
            descriptor = klass.__dict__["FilePath"]
            break
    assert isinstance(descriptor, property)

def test_connection::ldiffileconnection_has_UseLimit():
    assert hasattr(connection::LdifFileConnection, "UseLimit")
    descriptor = None
    for klass in connection::LdifFileConnection.__mro__:
        if "UseLimit" in klass.__dict__:
            descriptor = klass.__dict__["UseLimit"]
            break
    assert isinstance(descriptor, property)

def test_connection::ldiffileconnection_has_Server():
    assert hasattr(connection::LdifFileConnection, "Server")
    descriptor = None
    for klass in connection::LdifFileConnection.__mro__:
        if "Server" in klass.__dict__:
            descriptor = klass.__dict__["Server"]
            break
    assert isinstance(descriptor, property)



def test_connection::sapconnection_is_not_abstract():
    assert not inspect.isabstract(connection::SAPConnection)


def test_connection::sapconnection_constructor_exists():
    assert callable(connection::SAPConnection.__init__)


def test_connection::sapconnection_constructor_args():
    sig = inspect.signature(connection::SAPConnection.__init__)
    params = list(sig.parameters.keys())
    assert "Username" in params, "Missing parameter 'Username'"
    assert "Host" in params, "Missing parameter 'Host'"
    assert "currentFucntion" in params, "Missing parameter 'currentFucntion'"
    assert "SystemNumber" in params, "Missing parameter 'SystemNumber'"
    assert "Password" in params, "Missing parameter 'Password'"
    assert "Language" in params, "Missing parameter 'Language'"
    assert "Client" in params, "Missing parameter 'Client'"

def test_connection::sapconnection_has_Username():
    assert hasattr(connection::SAPConnection, "Username")
    descriptor = None
    for klass in connection::SAPConnection.__mro__:
        if "Username" in klass.__dict__:
            descriptor = klass.__dict__["Username"]
            break
    assert isinstance(descriptor, property)

def test_connection::sapconnection_has_Host():
    assert hasattr(connection::SAPConnection, "Host")
    descriptor = None
    for klass in connection::SAPConnection.__mro__:
        if "Host" in klass.__dict__:
            descriptor = klass.__dict__["Host"]
            break
    assert isinstance(descriptor, property)

def test_connection::sapconnection_has_currentFucntion():
    assert hasattr(connection::SAPConnection, "currentFucntion")
    descriptor = None
    for klass in connection::SAPConnection.__mro__:
        if "currentFucntion" in klass.__dict__:
            descriptor = klass.__dict__["currentFucntion"]
            break
    assert isinstance(descriptor, property)

def test_connection::sapconnection_has_SystemNumber():
    assert hasattr(connection::SAPConnection, "SystemNumber")
    descriptor = None
    for klass in connection::SAPConnection.__mro__:
        if "SystemNumber" in klass.__dict__:
            descriptor = klass.__dict__["SystemNumber"]
            break
    assert isinstance(descriptor, property)

def test_connection::sapconnection_has_Password():
    assert hasattr(connection::SAPConnection, "Password")
    descriptor = None
    for klass in connection::SAPConnection.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)

def test_connection::sapconnection_has_Language():
    assert hasattr(connection::SAPConnection, "Language")
    descriptor = None
    for klass in connection::SAPConnection.__mro__:
        if "Language" in klass.__dict__:
            descriptor = klass.__dict__["Language"]
            break
    assert isinstance(descriptor, property)

def test_connection::sapconnection_has_Client():
    assert hasattr(connection::SAPConnection, "Client")
    descriptor = None
    for klass in connection::SAPConnection.__mro__:
        if "Client" in klass.__dict__:
            descriptor = klass.__dict__["Client"]
            break
    assert isinstance(descriptor, property)



def test_connection::databaseconnection_is_not_abstract():
    assert not inspect.isabstract(connection::DatabaseConnection)


def test_connection::databaseconnection_constructor_exists():
    assert callable(connection::DatabaseConnection.__init__)


def test_connection::databaseconnection_constructor_args():
    sig = inspect.signature(connection::DatabaseConnection.__init__)
    params = list(sig.parameters.keys())
    assert "AdditionalParams" in params, "Missing parameter 'AdditionalParams'"
    assert "Username" in params, "Missing parameter 'Username'"
    assert "dbVersionString" in params, "Missing parameter 'dbVersionString'"
    assert "SqlSynthax" in params, "Missing parameter 'SqlSynthax'"
    assert "Port" in params, "Missing parameter 'Port'"
    assert "StandardSQL" in params, "Missing parameter 'StandardSQL'"
    assert "FileFieldName" in params, "Missing parameter 'FileFieldName'"
    assert "DbmsId" in params, "Missing parameter 'DbmsId'"
    assert "ServerName" in params, "Missing parameter 'ServerName'"
    assert "DatabaseType" in params, "Missing parameter 'DatabaseType'"
    assert "SQLMode" in params, "Missing parameter 'SQLMode'"
    assert "SystemSQL" in params, "Missing parameter 'SystemSQL'"
    assert "DriverJarPath" in params, "Missing parameter 'DriverJarPath'"
    assert "cdcTypeMode" in params, "Missing parameter 'cdcTypeMode'"
    assert "DatasourceName" in params, "Missing parameter 'DatasourceName'"
    assert "DriverClass" in params, "Missing parameter 'DriverClass'"
    assert "NullChar" in params, "Missing parameter 'NullChar'"
    assert "SID" in params, "Missing parameter 'SID'"
    assert "DBRootPath" in params, "Missing parameter 'DBRootPath'"
    assert "StringQuote" in params, "Missing parameter 'StringQuote'"
    assert "ProductId" in params, "Missing parameter 'ProductId'"
    assert "Schema" in params, "Missing parameter 'Schema'"
    assert "Password" in params, "Missing parameter 'Password'"
    assert "URL" in params, "Missing parameter 'URL'"

def test_connection::databaseconnection_has_AdditionalParams():
    assert hasattr(connection::DatabaseConnection, "AdditionalParams")
    descriptor = None
    for klass in connection::DatabaseConnection.__mro__:
        if "AdditionalParams" in klass.__dict__:
            descriptor = klass.__dict__["AdditionalParams"]
            break
    assert isinstance(descriptor, property)

def test_connection::databaseconnection_has_Username():
    assert hasattr(connection::DatabaseConnection, "Username")
    descriptor = None
    for klass in connection::DatabaseConnection.__mro__:
        if "Username" in klass.__dict__:
            descriptor = klass.__dict__["Username"]
            break
    assert isinstance(descriptor, property)

def test_connection::databaseconnection_has_dbVersionString():
    assert hasattr(connection::DatabaseConnection, "dbVersionString")
    descriptor = None
    for klass in connection::DatabaseConnection.__mro__:
        if "dbVersionString" in klass.__dict__:
            descriptor = klass.__dict__["dbVersionString"]
            break
    assert isinstance(descriptor, property)

def test_connection::databaseconnection_has_SqlSynthax():
    assert hasattr(connection::DatabaseConnection, "SqlSynthax")
    descriptor = None
    for klass in connection::DatabaseConnection.__mro__:
        if "SqlSynthax" in klass.__dict__:
            descriptor = klass.__dict__["SqlSynthax"]
            break
    assert isinstance(descriptor, property)

def test_connection::databaseconnection_has_Port():
    assert hasattr(connection::DatabaseConnection, "Port")
    descriptor = None
    for klass in connection::DatabaseConnection.__mro__:
        if "Port" in klass.__dict__:
            descriptor = klass.__dict__["Port"]
            break
    assert isinstance(descriptor, property)

def test_connection::databaseconnection_has_StandardSQL():
    assert hasattr(connection::DatabaseConnection, "StandardSQL")
    descriptor = None
    for klass in connection::DatabaseConnection.__mro__:
        if "StandardSQL" in klass.__dict__:
            descriptor = klass.__dict__["StandardSQL"]
            break
    assert isinstance(descriptor, property)

def test_connection::databaseconnection_has_FileFieldName():
    assert hasattr(connection::DatabaseConnection, "FileFieldName")
    descriptor = None
    for klass in connection::DatabaseConnection.__mro__:
        if "FileFieldName" in klass.__dict__:
            descriptor = klass.__dict__["FileFieldName"]
            break
    assert isinstance(descriptor, property)

def test_connection::databaseconnection_has_DbmsId():
    assert hasattr(connection::DatabaseConnection, "DbmsId")
    descriptor = None
    for klass in connection::DatabaseConnection.__mro__:
        if "DbmsId" in klass.__dict__:
            descriptor = klass.__dict__["DbmsId"]
            break
    assert isinstance(descriptor, property)

def test_connection::databaseconnection_has_ServerName():
    assert hasattr(connection::DatabaseConnection, "ServerName")
    descriptor = None
    for klass in connection::DatabaseConnection.__mro__:
        if "ServerName" in klass.__dict__:
            descriptor = klass.__dict__["ServerName"]
            break
    assert isinstance(descriptor, property)

def test_connection::databaseconnection_has_DatabaseType():
    assert hasattr(connection::DatabaseConnection, "DatabaseType")
    descriptor = None
    for klass in connection::DatabaseConnection.__mro__:
        if "DatabaseType" in klass.__dict__:
            descriptor = klass.__dict__["DatabaseType"]
            break
    assert isinstance(descriptor, property)

def test_connection::databaseconnection_has_SQLMode():
    assert hasattr(connection::DatabaseConnection, "SQLMode")
    descriptor = None
    for klass in connection::DatabaseConnection.__mro__:
        if "SQLMode" in klass.__dict__:
            descriptor = klass.__dict__["SQLMode"]
            break
    assert isinstance(descriptor, property)

def test_connection::databaseconnection_has_SystemSQL():
    assert hasattr(connection::DatabaseConnection, "SystemSQL")
    descriptor = None
    for klass in connection::DatabaseConnection.__mro__:
        if "SystemSQL" in klass.__dict__:
            descriptor = klass.__dict__["SystemSQL"]
            break
    assert isinstance(descriptor, property)

def test_connection::databaseconnection_has_DriverJarPath():
    assert hasattr(connection::DatabaseConnection, "DriverJarPath")
    descriptor = None
    for klass in connection::DatabaseConnection.__mro__:
        if "DriverJarPath" in klass.__dict__:
            descriptor = klass.__dict__["DriverJarPath"]
            break
    assert isinstance(descriptor, property)

def test_connection::databaseconnection_has_cdcTypeMode():
    assert hasattr(connection::DatabaseConnection, "cdcTypeMode")
    descriptor = None
    for klass in connection::DatabaseConnection.__mro__:
        if "cdcTypeMode" in klass.__dict__:
            descriptor = klass.__dict__["cdcTypeMode"]
            break
    assert isinstance(descriptor, property)

def test_connection::databaseconnection_has_DatasourceName():
    assert hasattr(connection::DatabaseConnection, "DatasourceName")
    descriptor = None
    for klass in connection::DatabaseConnection.__mro__:
        if "DatasourceName" in klass.__dict__:
            descriptor = klass.__dict__["DatasourceName"]
            break
    assert isinstance(descriptor, property)

def test_connection::databaseconnection_has_DriverClass():
    assert hasattr(connection::DatabaseConnection, "DriverClass")
    descriptor = None
    for klass in connection::DatabaseConnection.__mro__:
        if "DriverClass" in klass.__dict__:
            descriptor = klass.__dict__["DriverClass"]
            break
    assert isinstance(descriptor, property)

def test_connection::databaseconnection_has_NullChar():
    assert hasattr(connection::DatabaseConnection, "NullChar")
    descriptor = None
    for klass in connection::DatabaseConnection.__mro__:
        if "NullChar" in klass.__dict__:
            descriptor = klass.__dict__["NullChar"]
            break
    assert isinstance(descriptor, property)

def test_connection::databaseconnection_has_SID():
    assert hasattr(connection::DatabaseConnection, "SID")
    descriptor = None
    for klass in connection::DatabaseConnection.__mro__:
        if "SID" in klass.__dict__:
            descriptor = klass.__dict__["SID"]
            break
    assert isinstance(descriptor, property)

def test_connection::databaseconnection_has_DBRootPath():
    assert hasattr(connection::DatabaseConnection, "DBRootPath")
    descriptor = None
    for klass in connection::DatabaseConnection.__mro__:
        if "DBRootPath" in klass.__dict__:
            descriptor = klass.__dict__["DBRootPath"]
            break
    assert isinstance(descriptor, property)

def test_connection::databaseconnection_has_StringQuote():
    assert hasattr(connection::DatabaseConnection, "StringQuote")
    descriptor = None
    for klass in connection::DatabaseConnection.__mro__:
        if "StringQuote" in klass.__dict__:
            descriptor = klass.__dict__["StringQuote"]
            break
    assert isinstance(descriptor, property)

def test_connection::databaseconnection_has_ProductId():
    assert hasattr(connection::DatabaseConnection, "ProductId")
    descriptor = None
    for klass in connection::DatabaseConnection.__mro__:
        if "ProductId" in klass.__dict__:
            descriptor = klass.__dict__["ProductId"]
            break
    assert isinstance(descriptor, property)

def test_connection::databaseconnection_has_Schema():
    assert hasattr(connection::DatabaseConnection, "Schema")
    descriptor = None
    for klass in connection::DatabaseConnection.__mro__:
        if "Schema" in klass.__dict__:
            descriptor = klass.__dict__["Schema"]
            break
    assert isinstance(descriptor, property)

def test_connection::databaseconnection_has_Password():
    assert hasattr(connection::DatabaseConnection, "Password")
    descriptor = None
    for klass in connection::DatabaseConnection.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)

def test_connection::databaseconnection_has_URL():
    assert hasattr(connection::DatabaseConnection, "URL")
    descriptor = None
    for klass in connection::DatabaseConnection.__mro__:
        if "URL" in klass.__dict__:
            descriptor = klass.__dict__["URL"]
            break
    assert isinstance(descriptor, property)



def test_connection::ldapschemaconnection_is_not_abstract():
    assert not inspect.isabstract(connection::LDAPSchemaConnection)


def test_connection::ldapschemaconnection_constructor_exists():
    assert callable(connection::LDAPSchemaConnection.__init__)


def test_connection::ldapschemaconnection_constructor_args():
    sig = inspect.signature(connection::LDAPSchemaConnection.__init__)
    params = list(sig.parameters.keys())
    assert "GetBaseDNsFromRoot" in params, "Missing parameter 'GetBaseDNsFromRoot'"
    assert "BindPrincipal" in params, "Missing parameter 'BindPrincipal'"
    assert "CountLimit" in params, "Missing parameter 'CountLimit'"
    assert "Filter" in params, "Missing parameter 'Filter'"
    assert "LimitValue" in params, "Missing parameter 'LimitValue'"
    assert "SavePassword" in params, "Missing parameter 'SavePassword'"
    assert "UseLimit" in params, "Missing parameter 'UseLimit'"
    assert "UseAdvanced" in params, "Missing parameter 'UseAdvanced'"
    assert "Protocol" in params, "Missing parameter 'Protocol'"
    assert "EncryptionMethodName" in params, "Missing parameter 'EncryptionMethodName'"
    assert "BindPassword" in params, "Missing parameter 'BindPassword'"
    assert "Port" in params, "Missing parameter 'Port'"
    assert "Separator" in params, "Missing parameter 'Separator'"
    assert "BaseDNs" in params, "Missing parameter 'BaseDNs'"
    assert "StorePath" in params, "Missing parameter 'StorePath'"
    assert "Value" in params, "Missing parameter 'Value'"
    assert "Referrals" in params, "Missing parameter 'Referrals'"
    assert "ReturnAttributes" in params, "Missing parameter 'ReturnAttributes'"
    assert "Host" in params, "Missing parameter 'Host'"
    assert "Aliases" in params, "Missing parameter 'Aliases'"
    assert "UseAuthen" in params, "Missing parameter 'UseAuthen'"
    assert "SelectedDN" in params, "Missing parameter 'SelectedDN'"
    assert "TimeOutLimit" in params, "Missing parameter 'TimeOutLimit'"

def test_connection::ldapschemaconnection_has_GetBaseDNsFromRoot():
    assert hasattr(connection::LDAPSchemaConnection, "GetBaseDNsFromRoot")
    descriptor = None
    for klass in connection::LDAPSchemaConnection.__mro__:
        if "GetBaseDNsFromRoot" in klass.__dict__:
            descriptor = klass.__dict__["GetBaseDNsFromRoot"]
            break
    assert isinstance(descriptor, property)

def test_connection::ldapschemaconnection_has_BindPrincipal():
    assert hasattr(connection::LDAPSchemaConnection, "BindPrincipal")
    descriptor = None
    for klass in connection::LDAPSchemaConnection.__mro__:
        if "BindPrincipal" in klass.__dict__:
            descriptor = klass.__dict__["BindPrincipal"]
            break
    assert isinstance(descriptor, property)

def test_connection::ldapschemaconnection_has_CountLimit():
    assert hasattr(connection::LDAPSchemaConnection, "CountLimit")
    descriptor = None
    for klass in connection::LDAPSchemaConnection.__mro__:
        if "CountLimit" in klass.__dict__:
            descriptor = klass.__dict__["CountLimit"]
            break
    assert isinstance(descriptor, property)

def test_connection::ldapschemaconnection_has_Filter():
    assert hasattr(connection::LDAPSchemaConnection, "Filter")
    descriptor = None
    for klass in connection::LDAPSchemaConnection.__mro__:
        if "Filter" in klass.__dict__:
            descriptor = klass.__dict__["Filter"]
            break
    assert isinstance(descriptor, property)

def test_connection::ldapschemaconnection_has_LimitValue():
    assert hasattr(connection::LDAPSchemaConnection, "LimitValue")
    descriptor = None
    for klass in connection::LDAPSchemaConnection.__mro__:
        if "LimitValue" in klass.__dict__:
            descriptor = klass.__dict__["LimitValue"]
            break
    assert isinstance(descriptor, property)

def test_connection::ldapschemaconnection_has_SavePassword():
    assert hasattr(connection::LDAPSchemaConnection, "SavePassword")
    descriptor = None
    for klass in connection::LDAPSchemaConnection.__mro__:
        if "SavePassword" in klass.__dict__:
            descriptor = klass.__dict__["SavePassword"]
            break
    assert isinstance(descriptor, property)

def test_connection::ldapschemaconnection_has_UseLimit():
    assert hasattr(connection::LDAPSchemaConnection, "UseLimit")
    descriptor = None
    for klass in connection::LDAPSchemaConnection.__mro__:
        if "UseLimit" in klass.__dict__:
            descriptor = klass.__dict__["UseLimit"]
            break
    assert isinstance(descriptor, property)

def test_connection::ldapschemaconnection_has_UseAdvanced():
    assert hasattr(connection::LDAPSchemaConnection, "UseAdvanced")
    descriptor = None
    for klass in connection::LDAPSchemaConnection.__mro__:
        if "UseAdvanced" in klass.__dict__:
            descriptor = klass.__dict__["UseAdvanced"]
            break
    assert isinstance(descriptor, property)

def test_connection::ldapschemaconnection_has_Protocol():
    assert hasattr(connection::LDAPSchemaConnection, "Protocol")
    descriptor = None
    for klass in connection::LDAPSchemaConnection.__mro__:
        if "Protocol" in klass.__dict__:
            descriptor = klass.__dict__["Protocol"]
            break
    assert isinstance(descriptor, property)

def test_connection::ldapschemaconnection_has_EncryptionMethodName():
    assert hasattr(connection::LDAPSchemaConnection, "EncryptionMethodName")
    descriptor = None
    for klass in connection::LDAPSchemaConnection.__mro__:
        if "EncryptionMethodName" in klass.__dict__:
            descriptor = klass.__dict__["EncryptionMethodName"]
            break
    assert isinstance(descriptor, property)

def test_connection::ldapschemaconnection_has_BindPassword():
    assert hasattr(connection::LDAPSchemaConnection, "BindPassword")
    descriptor = None
    for klass in connection::LDAPSchemaConnection.__mro__:
        if "BindPassword" in klass.__dict__:
            descriptor = klass.__dict__["BindPassword"]
            break
    assert isinstance(descriptor, property)

def test_connection::ldapschemaconnection_has_Port():
    assert hasattr(connection::LDAPSchemaConnection, "Port")
    descriptor = None
    for klass in connection::LDAPSchemaConnection.__mro__:
        if "Port" in klass.__dict__:
            descriptor = klass.__dict__["Port"]
            break
    assert isinstance(descriptor, property)

def test_connection::ldapschemaconnection_has_Separator():
    assert hasattr(connection::LDAPSchemaConnection, "Separator")
    descriptor = None
    for klass in connection::LDAPSchemaConnection.__mro__:
        if "Separator" in klass.__dict__:
            descriptor = klass.__dict__["Separator"]
            break
    assert isinstance(descriptor, property)

def test_connection::ldapschemaconnection_has_BaseDNs():
    assert hasattr(connection::LDAPSchemaConnection, "BaseDNs")
    descriptor = None
    for klass in connection::LDAPSchemaConnection.__mro__:
        if "BaseDNs" in klass.__dict__:
            descriptor = klass.__dict__["BaseDNs"]
            break
    assert isinstance(descriptor, property)

def test_connection::ldapschemaconnection_has_StorePath():
    assert hasattr(connection::LDAPSchemaConnection, "StorePath")
    descriptor = None
    for klass in connection::LDAPSchemaConnection.__mro__:
        if "StorePath" in klass.__dict__:
            descriptor = klass.__dict__["StorePath"]
            break
    assert isinstance(descriptor, property)

def test_connection::ldapschemaconnection_has_Value():
    assert hasattr(connection::LDAPSchemaConnection, "Value")
    descriptor = None
    for klass in connection::LDAPSchemaConnection.__mro__:
        if "Value" in klass.__dict__:
            descriptor = klass.__dict__["Value"]
            break
    assert isinstance(descriptor, property)

def test_connection::ldapschemaconnection_has_Referrals():
    assert hasattr(connection::LDAPSchemaConnection, "Referrals")
    descriptor = None
    for klass in connection::LDAPSchemaConnection.__mro__:
        if "Referrals" in klass.__dict__:
            descriptor = klass.__dict__["Referrals"]
            break
    assert isinstance(descriptor, property)

def test_connection::ldapschemaconnection_has_ReturnAttributes():
    assert hasattr(connection::LDAPSchemaConnection, "ReturnAttributes")
    descriptor = None
    for klass in connection::LDAPSchemaConnection.__mro__:
        if "ReturnAttributes" in klass.__dict__:
            descriptor = klass.__dict__["ReturnAttributes"]
            break
    assert isinstance(descriptor, property)

def test_connection::ldapschemaconnection_has_Host():
    assert hasattr(connection::LDAPSchemaConnection, "Host")
    descriptor = None
    for klass in connection::LDAPSchemaConnection.__mro__:
        if "Host" in klass.__dict__:
            descriptor = klass.__dict__["Host"]
            break
    assert isinstance(descriptor, property)

def test_connection::ldapschemaconnection_has_Aliases():
    assert hasattr(connection::LDAPSchemaConnection, "Aliases")
    descriptor = None
    for klass in connection::LDAPSchemaConnection.__mro__:
        if "Aliases" in klass.__dict__:
            descriptor = klass.__dict__["Aliases"]
            break
    assert isinstance(descriptor, property)

def test_connection::ldapschemaconnection_has_UseAuthen():
    assert hasattr(connection::LDAPSchemaConnection, "UseAuthen")
    descriptor = None
    for klass in connection::LDAPSchemaConnection.__mro__:
        if "UseAuthen" in klass.__dict__:
            descriptor = klass.__dict__["UseAuthen"]
            break
    assert isinstance(descriptor, property)

def test_connection::ldapschemaconnection_has_SelectedDN():
    assert hasattr(connection::LDAPSchemaConnection, "SelectedDN")
    descriptor = None
    for klass in connection::LDAPSchemaConnection.__mro__:
        if "SelectedDN" in klass.__dict__:
            descriptor = klass.__dict__["SelectedDN"]
            break
    assert isinstance(descriptor, property)

def test_connection::ldapschemaconnection_has_TimeOutLimit():
    assert hasattr(connection::LDAPSchemaConnection, "TimeOutLimit")
    descriptor = None
    for klass in connection::LDAPSchemaConnection.__mro__:
        if "TimeOutLimit" in klass.__dict__:
            descriptor = klass.__dict__["TimeOutLimit"]
            break
    assert isinstance(descriptor, property)



def test_connection::fileconnection_is_not_abstract():
    assert not inspect.isabstract(connection::FileConnection)


def test_connection::fileconnection_constructor_exists():
    assert callable(connection::FileConnection.__init__)


def test_connection::fileconnection_constructor_args():
    sig = inspect.signature(connection::FileConnection.__init__)
    params = list(sig.parameters.keys())
    assert "EscapeChar" in params, "Missing parameter 'EscapeChar'"
    assert "RowSeparatorType" in params, "Missing parameter 'RowSeparatorType'"
    assert "RowSeparatorValue" in params, "Missing parameter 'RowSeparatorValue'"
    assert "CsvOption" in params, "Missing parameter 'CsvOption'"
    assert "FirstLineCaption" in params, "Missing parameter 'FirstLineCaption'"
    assert "RemoveEmptyRow" in params, "Missing parameter 'RemoveEmptyRow'"
    assert "Format" in params, "Missing parameter 'Format'"
    assert "LimitValue" in params, "Missing parameter 'LimitValue'"
    assert "UseFooter" in params, "Missing parameter 'UseFooter'"
    assert "TextIdentifier" in params, "Missing parameter 'TextIdentifier'"
    assert "UseLimit" in params, "Missing parameter 'UseLimit'"
    assert "HeaderValue" in params, "Missing parameter 'HeaderValue'"
    assert "FooterValue" in params, "Missing parameter 'FooterValue'"
    assert "Server" in params, "Missing parameter 'Server'"
    assert "UseHeader" in params, "Missing parameter 'UseHeader'"
    assert "TextEnclosure" in params, "Missing parameter 'TextEnclosure'"
    assert "Encoding" in params, "Missing parameter 'Encoding'"
    assert "FieldSeparatorValue" in params, "Missing parameter 'FieldSeparatorValue'"
    assert "EscapeType" in params, "Missing parameter 'EscapeType'"
    assert "FilePath" in params, "Missing parameter 'FilePath'"

def test_connection::fileconnection_has_EscapeChar():
    assert hasattr(connection::FileConnection, "EscapeChar")
    descriptor = None
    for klass in connection::FileConnection.__mro__:
        if "EscapeChar" in klass.__dict__:
            descriptor = klass.__dict__["EscapeChar"]
            break
    assert isinstance(descriptor, property)

def test_connection::fileconnection_has_RowSeparatorType():
    assert hasattr(connection::FileConnection, "RowSeparatorType")
    descriptor = None
    for klass in connection::FileConnection.__mro__:
        if "RowSeparatorType" in klass.__dict__:
            descriptor = klass.__dict__["RowSeparatorType"]
            break
    assert isinstance(descriptor, property)

def test_connection::fileconnection_has_RowSeparatorValue():
    assert hasattr(connection::FileConnection, "RowSeparatorValue")
    descriptor = None
    for klass in connection::FileConnection.__mro__:
        if "RowSeparatorValue" in klass.__dict__:
            descriptor = klass.__dict__["RowSeparatorValue"]
            break
    assert isinstance(descriptor, property)

def test_connection::fileconnection_has_CsvOption():
    assert hasattr(connection::FileConnection, "CsvOption")
    descriptor = None
    for klass in connection::FileConnection.__mro__:
        if "CsvOption" in klass.__dict__:
            descriptor = klass.__dict__["CsvOption"]
            break
    assert isinstance(descriptor, property)

def test_connection::fileconnection_has_FirstLineCaption():
    assert hasattr(connection::FileConnection, "FirstLineCaption")
    descriptor = None
    for klass in connection::FileConnection.__mro__:
        if "FirstLineCaption" in klass.__dict__:
            descriptor = klass.__dict__["FirstLineCaption"]
            break
    assert isinstance(descriptor, property)

def test_connection::fileconnection_has_RemoveEmptyRow():
    assert hasattr(connection::FileConnection, "RemoveEmptyRow")
    descriptor = None
    for klass in connection::FileConnection.__mro__:
        if "RemoveEmptyRow" in klass.__dict__:
            descriptor = klass.__dict__["RemoveEmptyRow"]
            break
    assert isinstance(descriptor, property)

def test_connection::fileconnection_has_Format():
    assert hasattr(connection::FileConnection, "Format")
    descriptor = None
    for klass in connection::FileConnection.__mro__:
        if "Format" in klass.__dict__:
            descriptor = klass.__dict__["Format"]
            break
    assert isinstance(descriptor, property)

def test_connection::fileconnection_has_LimitValue():
    assert hasattr(connection::FileConnection, "LimitValue")
    descriptor = None
    for klass in connection::FileConnection.__mro__:
        if "LimitValue" in klass.__dict__:
            descriptor = klass.__dict__["LimitValue"]
            break
    assert isinstance(descriptor, property)

def test_connection::fileconnection_has_UseFooter():
    assert hasattr(connection::FileConnection, "UseFooter")
    descriptor = None
    for klass in connection::FileConnection.__mro__:
        if "UseFooter" in klass.__dict__:
            descriptor = klass.__dict__["UseFooter"]
            break
    assert isinstance(descriptor, property)

def test_connection::fileconnection_has_TextIdentifier():
    assert hasattr(connection::FileConnection, "TextIdentifier")
    descriptor = None
    for klass in connection::FileConnection.__mro__:
        if "TextIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["TextIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_connection::fileconnection_has_UseLimit():
    assert hasattr(connection::FileConnection, "UseLimit")
    descriptor = None
    for klass in connection::FileConnection.__mro__:
        if "UseLimit" in klass.__dict__:
            descriptor = klass.__dict__["UseLimit"]
            break
    assert isinstance(descriptor, property)

def test_connection::fileconnection_has_HeaderValue():
    assert hasattr(connection::FileConnection, "HeaderValue")
    descriptor = None
    for klass in connection::FileConnection.__mro__:
        if "HeaderValue" in klass.__dict__:
            descriptor = klass.__dict__["HeaderValue"]
            break
    assert isinstance(descriptor, property)

def test_connection::fileconnection_has_FooterValue():
    assert hasattr(connection::FileConnection, "FooterValue")
    descriptor = None
    for klass in connection::FileConnection.__mro__:
        if "FooterValue" in klass.__dict__:
            descriptor = klass.__dict__["FooterValue"]
            break
    assert isinstance(descriptor, property)

def test_connection::fileconnection_has_Server():
    assert hasattr(connection::FileConnection, "Server")
    descriptor = None
    for klass in connection::FileConnection.__mro__:
        if "Server" in klass.__dict__:
            descriptor = klass.__dict__["Server"]
            break
    assert isinstance(descriptor, property)

def test_connection::fileconnection_has_UseHeader():
    assert hasattr(connection::FileConnection, "UseHeader")
    descriptor = None
    for klass in connection::FileConnection.__mro__:
        if "UseHeader" in klass.__dict__:
            descriptor = klass.__dict__["UseHeader"]
            break
    assert isinstance(descriptor, property)

def test_connection::fileconnection_has_TextEnclosure():
    assert hasattr(connection::FileConnection, "TextEnclosure")
    descriptor = None
    for klass in connection::FileConnection.__mro__:
        if "TextEnclosure" in klass.__dict__:
            descriptor = klass.__dict__["TextEnclosure"]
            break
    assert isinstance(descriptor, property)

def test_connection::fileconnection_has_Encoding():
    assert hasattr(connection::FileConnection, "Encoding")
    descriptor = None
    for klass in connection::FileConnection.__mro__:
        if "Encoding" in klass.__dict__:
            descriptor = klass.__dict__["Encoding"]
            break
    assert isinstance(descriptor, property)

def test_connection::fileconnection_has_FieldSeparatorValue():
    assert hasattr(connection::FileConnection, "FieldSeparatorValue")
    descriptor = None
    for klass in connection::FileConnection.__mro__:
        if "FieldSeparatorValue" in klass.__dict__:
            descriptor = klass.__dict__["FieldSeparatorValue"]
            break
    assert isinstance(descriptor, property)

def test_connection::fileconnection_has_EscapeType():
    assert hasattr(connection::FileConnection, "EscapeType")
    descriptor = None
    for klass in connection::FileConnection.__mro__:
        if "EscapeType" in klass.__dict__:
            descriptor = klass.__dict__["EscapeType"]
            break
    assert isinstance(descriptor, property)

def test_connection::fileconnection_has_FilePath():
    assert hasattr(connection::FileConnection, "FilePath")
    descriptor = None
    for klass in connection::FileConnection.__mro__:
        if "FilePath" in klass.__dict__:
            descriptor = klass.__dict__["FilePath"]
            break
    assert isinstance(descriptor, property)



def test_connection::abstractmetadataobject_is_not_abstract():
    assert not inspect.isabstract(connection::AbstractMetadataObject)


def test_connection::abstractmetadataobject_constructor_exists():
    assert callable(connection::AbstractMetadataObject.__init__)


def test_connection::abstractmetadataobject_constructor_args():
    sig = inspect.signature(connection::AbstractMetadataObject.__init__)
    params = list(sig.parameters.keys())
    assert "properties" in params, "Missing parameter 'properties'"
    assert "id" in params, "Missing parameter 'id'"
    assert "divergency" in params, "Missing parameter 'divergency'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "label" in params, "Missing parameter 'label'"
    assert "synchronised" in params, "Missing parameter 'synchronised'"
    assert "readOnly" in params, "Missing parameter 'readOnly'"

def test_connection::abstractmetadataobject_has_properties():
    assert hasattr(connection::AbstractMetadataObject, "properties")
    descriptor = None
    for klass in connection::AbstractMetadataObject.__mro__:
        if "properties" in klass.__dict__:
            descriptor = klass.__dict__["properties"]
            break
    assert isinstance(descriptor, property)

def test_connection::abstractmetadataobject_has_id():
    assert hasattr(connection::AbstractMetadataObject, "id")
    descriptor = None
    for klass in connection::AbstractMetadataObject.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_connection::abstractmetadataobject_has_divergency():
    assert hasattr(connection::AbstractMetadataObject, "divergency")
    descriptor = None
    for klass in connection::AbstractMetadataObject.__mro__:
        if "divergency" in klass.__dict__:
            descriptor = klass.__dict__["divergency"]
            break
    assert isinstance(descriptor, property)

def test_connection::abstractmetadataobject_has_comment():
    assert hasattr(connection::AbstractMetadataObject, "comment")
    descriptor = None
    for klass in connection::AbstractMetadataObject.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_connection::abstractmetadataobject_has_label():
    assert hasattr(connection::AbstractMetadataObject, "label")
    descriptor = None
    for klass in connection::AbstractMetadataObject.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_connection::abstractmetadataobject_has_synchronised():
    assert hasattr(connection::AbstractMetadataObject, "synchronised")
    descriptor = None
    for klass in connection::AbstractMetadataObject.__mro__:
        if "synchronised" in klass.__dict__:
            descriptor = klass.__dict__["synchronised"]
            break
    assert isinstance(descriptor, property)

def test_connection::abstractmetadataobject_has_readOnly():
    assert hasattr(connection::AbstractMetadataObject, "readOnly")
    descriptor = None
    for klass in connection::AbstractMetadataObject.__mro__:
        if "readOnly" in klass.__dict__:
            descriptor = klass.__dict__["readOnly"]
            break
    assert isinstance(descriptor, property)



def test_abstractmetadataobject_is_not_abstract():
    assert not inspect.isabstract(AbstractMetadataObject)


def test_abstractmetadataobject_constructor_exists():
    assert callable(AbstractMetadataObject.__init__)


def test_abstractmetadataobject_constructor_args():
    sig = inspect.signature(AbstractMetadataObject.__init__)
    params = list(sig.parameters.keys())



def test_connection::sapfunctionunit_is_not_abstract():
    assert not inspect.isabstract(connection::SAPFunctionUnit)


def test_connection::sapfunctionunit_constructor_exists():
    assert callable(connection::SAPFunctionUnit.__init__)


def test_connection::sapfunctionunit_constructor_args():
    sig = inspect.signature(connection::SAPFunctionUnit.__init__)
    params = list(sig.parameters.keys())
    assert "Document" in params, "Missing parameter 'Document'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "OutputTableName" in params, "Missing parameter 'OutputTableName'"
    assert "OutputType" in params, "Missing parameter 'OutputType'"

def test_connection::sapfunctionunit_has_Document():
    assert hasattr(connection::SAPFunctionUnit, "Document")
    descriptor = None
    for klass in connection::SAPFunctionUnit.__mro__:
        if "Document" in klass.__dict__:
            descriptor = klass.__dict__["Document"]
            break
    assert isinstance(descriptor, property)

def test_connection::sapfunctionunit_has_Name():
    assert hasattr(connection::SAPFunctionUnit, "Name")
    descriptor = None
    for klass in connection::SAPFunctionUnit.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_connection::sapfunctionunit_has_OutputTableName():
    assert hasattr(connection::SAPFunctionUnit, "OutputTableName")
    descriptor = None
    for klass in connection::SAPFunctionUnit.__mro__:
        if "OutputTableName" in klass.__dict__:
            descriptor = klass.__dict__["OutputTableName"]
            break
    assert isinstance(descriptor, property)

def test_connection::sapfunctionunit_has_OutputType():
    assert hasattr(connection::SAPFunctionUnit, "OutputType")
    descriptor = None
    for klass in connection::SAPFunctionUnit.__mro__:
        if "OutputType" in klass.__dict__:
            descriptor = klass.__dict__["OutputType"]
            break
    assert isinstance(descriptor, property)



def test_connection::query_is_not_abstract():
    assert not inspect.isabstract(connection::Query)


def test_connection::query_constructor_exists():
    assert callable(connection::Query.__init__)


def test_connection::query_constructor_args():
    sig = inspect.signature(connection::Query.__init__)
    params = list(sig.parameters.keys())
    assert "contextMode" in params, "Missing parameter 'contextMode'"
    assert "value" in params, "Missing parameter 'value'"

def test_connection::query_has_contextMode():
    assert hasattr(connection::Query, "contextMode")
    descriptor = None
    for klass in connection::Query.__mro__:
        if "contextMode" in klass.__dict__:
            descriptor = klass.__dict__["contextMode"]
            break
    assert isinstance(descriptor, property)

def test_connection::query_has_value():
    assert hasattr(connection::Query, "value")
    descriptor = None
    for klass in connection::Query.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_connection::sapfunctionparametercolumn_is_not_abstract():
    assert not inspect.isabstract(connection::SAPFunctionParameterColumn)


def test_connection::sapfunctionparametercolumn_constructor_exists():
    assert callable(connection::SAPFunctionParameterColumn.__init__)


def test_connection::sapfunctionparametercolumn_constructor_args():
    sig = inspect.signature(connection::SAPFunctionParameterColumn.__init__)
    params = list(sig.parameters.keys())
    assert "Length" in params, "Missing parameter 'Length'"
    assert "DataType" in params, "Missing parameter 'DataType'"
    assert "StructureOrTableName" in params, "Missing parameter 'StructureOrTableName'"
    assert "Value" in params, "Missing parameter 'Value'"
    assert "ParameterType" in params, "Missing parameter 'ParameterType'"
    assert "Description" in params, "Missing parameter 'Description'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_connection::sapfunctionparametercolumn_has_Length():
    assert hasattr(connection::SAPFunctionParameterColumn, "Length")
    descriptor = None
    for klass in connection::SAPFunctionParameterColumn.__mro__:
        if "Length" in klass.__dict__:
            descriptor = klass.__dict__["Length"]
            break
    assert isinstance(descriptor, property)

def test_connection::sapfunctionparametercolumn_has_DataType():
    assert hasattr(connection::SAPFunctionParameterColumn, "DataType")
    descriptor = None
    for klass in connection::SAPFunctionParameterColumn.__mro__:
        if "DataType" in klass.__dict__:
            descriptor = klass.__dict__["DataType"]
            break
    assert isinstance(descriptor, property)

def test_connection::sapfunctionparametercolumn_has_StructureOrTableName():
    assert hasattr(connection::SAPFunctionParameterColumn, "StructureOrTableName")
    descriptor = None
    for klass in connection::SAPFunctionParameterColumn.__mro__:
        if "StructureOrTableName" in klass.__dict__:
            descriptor = klass.__dict__["StructureOrTableName"]
            break
    assert isinstance(descriptor, property)

def test_connection::sapfunctionparametercolumn_has_Value():
    assert hasattr(connection::SAPFunctionParameterColumn, "Value")
    descriptor = None
    for klass in connection::SAPFunctionParameterColumn.__mro__:
        if "Value" in klass.__dict__:
            descriptor = klass.__dict__["Value"]
            break
    assert isinstance(descriptor, property)

def test_connection::sapfunctionparametercolumn_has_ParameterType():
    assert hasattr(connection::SAPFunctionParameterColumn, "ParameterType")
    descriptor = None
    for klass in connection::SAPFunctionParameterColumn.__mro__:
        if "ParameterType" in klass.__dict__:
            descriptor = klass.__dict__["ParameterType"]
            break
    assert isinstance(descriptor, property)

def test_connection::sapfunctionparametercolumn_has_Description():
    assert hasattr(connection::SAPFunctionParameterColumn, "Description")
    descriptor = None
    for klass in connection::SAPFunctionParameterColumn.__mro__:
        if "Description" in klass.__dict__:
            descriptor = klass.__dict__["Description"]
            break
    assert isinstance(descriptor, property)

def test_connection::sapfunctionparametercolumn_has_Name():
    assert hasattr(connection::SAPFunctionParameterColumn, "Name")
    descriptor = None
    for klass in connection::SAPFunctionParameterColumn.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_connection::cdctype_is_not_abstract():
    assert not inspect.isabstract(connection::CDCType)


def test_connection::cdctype_constructor_exists():
    assert callable(connection::CDCType.__init__)


def test_connection::cdctype_constructor_args():
    sig = inspect.signature(connection::CDCType.__init__)
    params = list(sig.parameters.keys())
    assert "journalName" in params, "Missing parameter 'journalName'"
    assert "linkDB" in params, "Missing parameter 'linkDB'"

def test_connection::cdctype_has_journalName():
    assert hasattr(connection::CDCType, "journalName")
    descriptor = None
    for klass in connection::CDCType.__mro__:
        if "journalName" in klass.__dict__:
            descriptor = klass.__dict__["journalName"]
            break
    assert isinstance(descriptor, property)

def test_connection::cdctype_has_linkDB():
    assert hasattr(connection::CDCType, "linkDB")
    descriptor = None
    for klass in connection::CDCType.__mro__:
        if "linkDB" in klass.__dict__:
            descriptor = klass.__dict__["linkDB"]
            break
    assert isinstance(descriptor, property)



def test_connection::sapfunctionparametertable_is_not_abstract():
    assert not inspect.isabstract(connection::SAPFunctionParameterTable)


def test_connection::sapfunctionparametertable_constructor_exists():
    assert callable(connection::SAPFunctionParameterTable.__init__)


def test_connection::sapfunctionparametertable_constructor_args():
    sig = inspect.signature(connection::SAPFunctionParameterTable.__init__)
    params = list(sig.parameters.keys())



def test_connection::metadata_is_not_abstract():
    assert not inspect.isabstract(connection::Metadata)


def test_connection::metadata_constructor_exists():
    assert callable(connection::Metadata.__init__)


def test_connection::metadata_constructor_args():
    sig = inspect.signature(connection::Metadata.__init__)
    params = list(sig.parameters.keys())



def test_connection::metadatacolumn_is_not_abstract():
    assert not inspect.isabstract(connection::MetadataColumn)


def test_connection::metadatacolumn_constructor_exists():
    assert callable(connection::MetadataColumn.__init__)


def test_connection::metadatacolumn_constructor_args():
    sig = inspect.signature(connection::MetadataColumn.__init__)
    params = list(sig.parameters.keys())
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "sourceType" in params, "Missing parameter 'sourceType'"
    assert "pattern" in params, "Missing parameter 'pattern'"
    assert "displayField" in params, "Missing parameter 'displayField'"
    assert "originalField" in params, "Missing parameter 'originalField'"
    assert "talendType" in params, "Missing parameter 'talendType'"
    assert "key" in params, "Missing parameter 'key'"
    assert "nullable" in params, "Missing parameter 'nullable'"
    assert "precision" in params, "Missing parameter 'precision'"
    assert "length" in params, "Missing parameter 'length'"

def test_connection::metadatacolumn_has_defaultValue():
    assert hasattr(connection::MetadataColumn, "defaultValue")
    descriptor = None
    for klass in connection::MetadataColumn.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)

def test_connection::metadatacolumn_has_sourceType():
    assert hasattr(connection::MetadataColumn, "sourceType")
    descriptor = None
    for klass in connection::MetadataColumn.__mro__:
        if "sourceType" in klass.__dict__:
            descriptor = klass.__dict__["sourceType"]
            break
    assert isinstance(descriptor, property)

def test_connection::metadatacolumn_has_pattern():
    assert hasattr(connection::MetadataColumn, "pattern")
    descriptor = None
    for klass in connection::MetadataColumn.__mro__:
        if "pattern" in klass.__dict__:
            descriptor = klass.__dict__["pattern"]
            break
    assert isinstance(descriptor, property)

def test_connection::metadatacolumn_has_displayField():
    assert hasattr(connection::MetadataColumn, "displayField")
    descriptor = None
    for klass in connection::MetadataColumn.__mro__:
        if "displayField" in klass.__dict__:
            descriptor = klass.__dict__["displayField"]
            break
    assert isinstance(descriptor, property)

def test_connection::metadatacolumn_has_originalField():
    assert hasattr(connection::MetadataColumn, "originalField")
    descriptor = None
    for klass in connection::MetadataColumn.__mro__:
        if "originalField" in klass.__dict__:
            descriptor = klass.__dict__["originalField"]
            break
    assert isinstance(descriptor, property)

def test_connection::metadatacolumn_has_talendType():
    assert hasattr(connection::MetadataColumn, "talendType")
    descriptor = None
    for klass in connection::MetadataColumn.__mro__:
        if "talendType" in klass.__dict__:
            descriptor = klass.__dict__["talendType"]
            break
    assert isinstance(descriptor, property)

def test_connection::metadatacolumn_has_key():
    assert hasattr(connection::MetadataColumn, "key")
    descriptor = None
    for klass in connection::MetadataColumn.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_connection::metadatacolumn_has_nullable():
    assert hasattr(connection::MetadataColumn, "nullable")
    descriptor = None
    for klass in connection::MetadataColumn.__mro__:
        if "nullable" in klass.__dict__:
            descriptor = klass.__dict__["nullable"]
            break
    assert isinstance(descriptor, property)

def test_connection::metadatacolumn_has_precision():
    assert hasattr(connection::MetadataColumn, "precision")
    descriptor = None
    for klass in connection::MetadataColumn.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)

def test_connection::metadatacolumn_has_length():
    assert hasattr(connection::MetadataColumn, "length")
    descriptor = None
    for klass in connection::MetadataColumn.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_connection::queriesconnection_is_not_abstract():
    assert not inspect.isabstract(connection::QueriesConnection)


def test_connection::queriesconnection_constructor_exists():
    assert callable(connection::QueriesConnection.__init__)


def test_connection::queriesconnection_constructor_args():
    sig = inspect.signature(connection::QueriesConnection.__init__)
    params = list(sig.parameters.keys())



def test_connection::metadatatable_is_not_abstract():
    assert not inspect.isabstract(connection::MetadataTable)


def test_connection::metadatatable_constructor_exists():
    assert callable(connection::MetadataTable.__init__)


def test_connection::metadatatable_constructor_args():
    sig = inspect.signature(connection::MetadataTable.__init__)
    params = list(sig.parameters.keys())
    assert "attachedCDC" in params, "Missing parameter 'attachedCDC'"
    assert "activatedCDC" in params, "Missing parameter 'activatedCDC'"
    assert "tableType" in params, "Missing parameter 'tableType'"
    assert "sourceName" in params, "Missing parameter 'sourceName'"

def test_connection::metadatatable_has_attachedCDC():
    assert hasattr(connection::MetadataTable, "attachedCDC")
    descriptor = None
    for klass in connection::MetadataTable.__mro__:
        if "attachedCDC" in klass.__dict__:
            descriptor = klass.__dict__["attachedCDC"]
            break
    assert isinstance(descriptor, property)

def test_connection::metadatatable_has_activatedCDC():
    assert hasattr(connection::MetadataTable, "activatedCDC")
    descriptor = None
    for klass in connection::MetadataTable.__mro__:
        if "activatedCDC" in klass.__dict__:
            descriptor = klass.__dict__["activatedCDC"]
            break
    assert isinstance(descriptor, property)

def test_connection::metadatatable_has_tableType():
    assert hasattr(connection::MetadataTable, "tableType")
    descriptor = None
    for klass in connection::MetadataTable.__mro__:
        if "tableType" in klass.__dict__:
            descriptor = klass.__dict__["tableType"]
            break
    assert isinstance(descriptor, property)

def test_connection::metadatatable_has_sourceName():
    assert hasattr(connection::MetadataTable, "sourceName")
    descriptor = None
    for klass in connection::MetadataTable.__mro__:
        if "sourceName" in klass.__dict__:
            descriptor = klass.__dict__["sourceName"]
            break
    assert isinstance(descriptor, property)



def test_connection::connection_is_not_abstract():
    assert not inspect.isabstract(connection::Connection)


def test_connection::connection_constructor_exists():
    assert callable(connection::Connection.__init__)


def test_connection::connection_constructor_args():
    sig = inspect.signature(connection::Connection.__init__)
    params = list(sig.parameters.keys())
    assert "ContextId" in params, "Missing parameter 'ContextId'"
    assert "ContextMode" in params, "Missing parameter 'ContextMode'"
    assert "version" in params, "Missing parameter 'version'"

def test_connection::connection_has_ContextId():
    assert hasattr(connection::Connection, "ContextId")
    descriptor = None
    for klass in connection::Connection.__mro__:
        if "ContextId" in klass.__dict__:
            descriptor = klass.__dict__["ContextId"]
            break
    assert isinstance(descriptor, property)

def test_connection::connection_has_ContextMode():
    assert hasattr(connection::Connection, "ContextMode")
    descriptor = None
    for klass in connection::Connection.__mro__:
        if "ContextMode" in klass.__dict__:
            descriptor = klass.__dict__["ContextMode"]
            break
    assert isinstance(descriptor, property)

def test_connection::connection_has_version():
    assert hasattr(connection::Connection, "version")
    descriptor = None
    for klass in connection::Connection.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_rowseparator_exists():
    # Check that the Enumeration exists
    assert RowSeparator is not None

def test_rowseparator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RowSeparator]
    expected_literals = [
        "Custom_String",
        "Standart_EOL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RowSeparator"

def test_databaseproperties_exists():
    # Check that the Enumeration exists
    assert DatabaseProperties is not None

def test_databaseproperties_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DatabaseProperties]
    expected_literals = [
        "DriverClass",
        "SID",
        "Password",
        "Port",
        "ServerName",
        "FileFieldName",
        "SqlSynthax",
        "DatasourceName",
        "Username",
        "Schema",
        "StringQuote",
        "NullChar",
        "URL",
        "DatabaseType",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DatabaseProperties"

def test_fieldseparator_exists():
    # Check that the Enumeration exists
    assert FieldSeparator is not None

def test_fieldseparator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FieldSeparator]
    expected_literals = [
        "Tabulation",
        "Semicolon",
        "Custom_UTF8",
        "Custom_RegExp",
        "Custom_ANSI",
        "Space",
        "Alt_65",
        "Comma",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FieldSeparator"

def test_escape_exists():
    # Check that the Enumeration exists
    assert Escape is not None

def test_escape_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Escape]
    expected_literals = [
        "CSV",
        "Delimited",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Escape"

def test_fileformat_exists():
    # Check that the Enumeration exists
    assert FileFormat is not None

def test_fileformat_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FileFormat]
    expected_literals = [
        "UNIX",
        "WINDOWS",
        "MAC",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FileFormat"


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
connection::ConceptTarget_strategy = st.builds(
    connection::ConceptTarget,
    RelativeLoopExpression=
        safe_text,
    targetName=
        safe_text
)
MetadataTable_strategy = st.builds(
    MetadataTable,
)
connection::SubscriberTable_strategy = st.builds(
    connection::SubscriberTable,
    system=
        st.booleans()
)
connection::SchemaTarget_strategy = st.builds(
    connection::SchemaTarget,
    TagName=
        safe_text,
    RelativeXPathQuery=
        safe_text
)
connection::XmlXPathLoopDescriptor_strategy = st.builds(
    connection::XmlXPathLoopDescriptor,
    LimitBoucle=
        safe_text,
    AbsoluteXPathQuery=
        safe_text
)
SAPFunctionParameterTable_strategy = st.builds(
    SAPFunctionParameterTable,
)
connection::SAPTestInputParameterTable_strategy = st.builds(
    connection::SAPTestInputParameterTable,
)
connection::CDCConnection_strategy = st.builds(
    connection::CDCConnection,
)
connection::OutputSAPFunctionParameterTable_strategy = st.builds(
    connection::OutputSAPFunctionParameterTable,
)
connection::InputSAPFunctionParameterTable_strategy = st.builds(
    connection::InputSAPFunctionParameterTable,
)
FileConnection_strategy = st.builds(
    FileConnection,
)
connection::EbcdicConnection_strategy = st.builds(
    connection::EbcdicConnection,
    MidFile=
        safe_text,
    DataFile=
        safe_text
)
connection::FileExcelConnection_strategy = st.builds(
    connection::FileExcelConnection,
    thousandSeparator=
        safe_text,
    sheetList=
        safe_text,
    decimalSeparator=
        safe_text,
    lastColumn=
        safe_text,
    selectAllSheets=
        st.booleans(),
    SheetName=
        safe_text,
    sheetColumns=
        safe_text,
    firstColumn=
        safe_text,
    advancedSpearator=
        st.booleans()
)
connection::RegexpFileConnection_strategy = st.builds(
    connection::RegexpFileConnection,
    FieldSeparatorType=
        safe_text
)
connection::HL7Connection_strategy = st.builds(
    connection::HL7Connection,
    EndChar=
        safe_text,
    StartChar=
        safe_text
)
connection::PositionalFileConnection_strategy = st.builds(
    connection::PositionalFileConnection,
)
connection::DelimitedFileConnection_strategy = st.builds(
    connection::DelimitedFileConnection,
    FieldSeparatorType=
        safe_text,
    splitRecord=
        st.booleans()
)
connection::Concept_strategy = st.builds(
    connection::Concept,
    LoopExpression=
        safe_text,
    LoopLimit=
        safe_text
)
Connection_strategy = st.builds(
    Connection,
)
connection::SalesforceSchemaConnection_strategy = st.builds(
    connection::SalesforceSchemaConnection,
    userName=
        safe_text,
    useCustomModuleName=
        st.booleans(),
    webServiceUrl=
        safe_text,
    proxyHost=
        safe_text,
    password=
        safe_text,
    timeOut=
        safe_text,
    proxyPort=
        safe_text,
    useHttpProxy=
        st.booleans(),
    batchSize=
        safe_text,
    queryCondition=
        safe_text,
    moduleName=
        safe_text,
    useProxy=
        st.booleans(),
    proxyUsername=
        safe_text,
    proxyPassword=
        safe_text,
    useAlphbet=
        st.booleans()
)
connection::XmlFileConnection_strategy = st.builds(
    connection::XmlFileConnection,
    XsdFilePath=
        safe_text,
    Encoding=
        safe_text,
    XmlFilePath=
        safe_text,
    MaskXPattern=
        safe_text,
    Guess=
        st.booleans()
)
connection::MDMConnection_strategy = st.builds(
    connection::MDMConnection,
    Password=
        safe_text,
    Datamodel=
        safe_text,
    Datacluster=
        safe_text,
    Username=
        safe_text,
    Server=
        safe_text,
    Universe=
        safe_text,
    Port=
        safe_text
)
connection::WSDLSchemaConnection_strategy = st.builds(
    connection::WSDLSchemaConnection,
    proxyPassword=
        safe_text,
    Password=
        safe_text,
    EndpointURI=
        safe_text,
    proxyUser=
        safe_text,
    proxyHost=
        safe_text,
    needAuth=
        st.booleans(),
    proxyPort=
        safe_text,
    parameters=
        safe_text,
    Encoding=
        safe_text,
    methodName=
        safe_text,
    useProxy=
        st.booleans(),
    UserName=
        safe_text,
    timeOut=
        st.integers(),
    WSDL=
        safe_text,
    Value=
        safe_text
)
connection::GenericSchemaConnection_strategy = st.builds(
    connection::GenericSchemaConnection,
    mappingTypeId=
        safe_text,
    mappingTypeUsed=
        st.booleans()
)
connection::LdifFileConnection_strategy = st.builds(
    connection::LdifFileConnection,
    value=
        safe_text,
    LimitEntry=
        st.integers(),
    FilePath=
        safe_text,
    UseLimit=
        st.booleans(),
    Server=
        safe_text
)
connection::SAPConnection_strategy = st.builds(
    connection::SAPConnection,
    Username=
        safe_text,
    Host=
        safe_text,
    currentFucntion=
        safe_text,
    SystemNumber=
        safe_text,
    Password=
        safe_text,
    Language=
        safe_text,
    Client=
        safe_text
)
connection::DatabaseConnection_strategy = st.builds(
    connection::DatabaseConnection,
    AdditionalParams=
        safe_text,
    Username=
        safe_text,
    dbVersionString=
        safe_text,
    SqlSynthax=
        safe_text,
    Port=
        safe_text,
    StandardSQL=
        st.booleans(),
    FileFieldName=
        safe_text,
    DbmsId=
        safe_text,
    ServerName=
        safe_text,
    DatabaseType=
        safe_text,
    SQLMode=
        st.booleans(),
    SystemSQL=
        st.booleans(),
    DriverJarPath=
        safe_text,
    cdcTypeMode=
        safe_text,
    DatasourceName=
        safe_text,
    DriverClass=
        safe_text,
    NullChar=
        safe_text,
    SID=
        safe_text,
    DBRootPath=
        safe_text,
    StringQuote=
        safe_text,
    ProductId=
        safe_text,
    Schema=
        safe_text,
    Password=
        safe_text,
    URL=
        safe_text
)
connection::LDAPSchemaConnection_strategy = st.builds(
    connection::LDAPSchemaConnection,
    GetBaseDNsFromRoot=
        st.booleans(),
    BindPrincipal=
        safe_text,
    CountLimit=
        safe_text,
    Filter=
        safe_text,
    LimitValue=
        st.integers(),
    SavePassword=
        st.booleans(),
    UseLimit=
        st.booleans(),
    UseAdvanced=
        st.booleans(),
    Protocol=
        safe_text,
    EncryptionMethodName=
        safe_text,
    BindPassword=
        safe_text,
    Port=
        safe_text,
    Separator=
        safe_text,
    BaseDNs=
        safe_text,
    StorePath=
        safe_text,
    Value=
        safe_text,
    Referrals=
        safe_text,
    ReturnAttributes=
        safe_text,
    Host=
        safe_text,
    Aliases=
        safe_text,
    UseAuthen=
        st.booleans(),
    SelectedDN=
        safe_text,
    TimeOutLimit=
        safe_text
)
connection::FileConnection_strategy = st.builds(
    connection::FileConnection,
    EscapeChar=
        safe_text,
    RowSeparatorType=
        safe_text,
    RowSeparatorValue=
        safe_text,
    CsvOption=
        st.booleans(),
    FirstLineCaption=
        st.booleans(),
    RemoveEmptyRow=
        st.booleans(),
    Format=
        safe_text,
    LimitValue=
        safe_text,
    UseFooter=
        st.booleans(),
    TextIdentifier=
        safe_text,
    UseLimit=
        st.booleans(),
    HeaderValue=
        safe_text,
    FooterValue=
        safe_text,
    Server=
        safe_text,
    UseHeader=
        st.booleans(),
    TextEnclosure=
        safe_text,
    Encoding=
        safe_text,
    FieldSeparatorValue=
        safe_text,
    EscapeType=
        safe_text,
    FilePath=
        safe_text
)
connection::AbstractMetadataObject_strategy = st.builds(
    connection::AbstractMetadataObject,
    properties=
        safe_text,
    id=
        safe_text,
    divergency=
        st.booleans(),
    comment=
        safe_text,
    label=
        safe_text,
    synchronised=
        st.booleans(),
    readOnly=
        st.booleans()
)
AbstractMetadataObject_strategy = st.builds(
    AbstractMetadataObject,
)
connection::SAPFunctionUnit_strategy = st.builds(
    connection::SAPFunctionUnit,
    Document=
        safe_text,
    Name=
        safe_text,
    OutputTableName=
        safe_text,
    OutputType=
        safe_text
)
connection::Query_strategy = st.builds(
    connection::Query,
    contextMode=
        st.booleans(),
    value=
        safe_text
)
connection::SAPFunctionParameterColumn_strategy = st.builds(
    connection::SAPFunctionParameterColumn,
    Length=
        safe_text,
    DataType=
        safe_text,
    StructureOrTableName=
        safe_text,
    Value=
        safe_text,
    ParameterType=
        safe_text,
    Description=
        safe_text,
    Name=
        safe_text
)
connection::CDCType_strategy = st.builds(
    connection::CDCType,
    journalName=
        safe_text,
    linkDB=
        safe_text
)
connection::SAPFunctionParameterTable_strategy = st.builds(
    connection::SAPFunctionParameterTable,
)
connection::Metadata_strategy = st.builds(
    connection::Metadata,
)
connection::MetadataColumn_strategy = st.builds(
    connection::MetadataColumn,
    defaultValue=
        safe_text,
    sourceType=
        safe_text,
    pattern=
        safe_text,
    displayField=
        safe_text,
    originalField=
        safe_text,
    talendType=
        safe_text,
    key=
        st.booleans(),
    nullable=
        st.booleans(),
    precision=
        safe_text,
    length=
        safe_text
)
connection::QueriesConnection_strategy = st.builds(
    connection::QueriesConnection,
)
connection::MetadataTable_strategy = st.builds(
    connection::MetadataTable,
    attachedCDC=
        st.booleans(),
    activatedCDC=
        st.booleans(),
    tableType=
        safe_text,
    sourceName=
        safe_text
)
connection::Connection_strategy = st.builds(
    connection::Connection,
    ContextId=
        safe_text,
    ContextMode=
        st.booleans(),
    version=
        safe_text
)

@given(instance=connection::ConceptTarget_strategy)
@settings(max_examples=50)
def test_connection::concepttarget_instantiation(instance):
    assert isinstance(instance, connection::ConceptTarget)

@given(instance=connection::ConceptTarget_strategy)
def test_connection::concepttarget_RelativeLoopExpression_type(instance):
    assert isinstance(instance.RelativeLoopExpression, str)


@given(instance=connection::ConceptTarget_strategy)
def test_connection::concepttarget_RelativeLoopExpression_setter(instance):
    original = instance.RelativeLoopExpression
    instance.RelativeLoopExpression = original
    assert instance.RelativeLoopExpression == original

@given(instance=connection::ConceptTarget_strategy)
def test_connection::concepttarget_targetName_type(instance):
    assert isinstance(instance.targetName, str)


@given(instance=connection::ConceptTarget_strategy)
def test_connection::concepttarget_targetName_setter(instance):
    original = instance.targetName
    instance.targetName = original
    assert instance.targetName == original

@given(instance=MetadataTable_strategy)
@settings(max_examples=50)
def test_metadatatable_instantiation(instance):
    assert isinstance(instance, MetadataTable)

@given(instance=connection::SubscriberTable_strategy)
@settings(max_examples=50)
def test_connection::subscribertable_instantiation(instance):
    assert isinstance(instance, connection::SubscriberTable)

@given(instance=connection::SubscriberTable_strategy)
def test_connection::subscribertable_system_type(instance):
    assert isinstance(instance.system, bool)


@given(instance=connection::SubscriberTable_strategy)
def test_connection::subscribertable_system_setter(instance):
    original = instance.system
    instance.system = original
    assert instance.system == original

@given(instance=connection::SchemaTarget_strategy)
@settings(max_examples=50)
def test_connection::schematarget_instantiation(instance):
    assert isinstance(instance, connection::SchemaTarget)

@given(instance=connection::SchemaTarget_strategy)
def test_connection::schematarget_TagName_type(instance):
    assert isinstance(instance.TagName, str)


@given(instance=connection::SchemaTarget_strategy)
def test_connection::schematarget_TagName_setter(instance):
    original = instance.TagName
    instance.TagName = original
    assert instance.TagName == original

@given(instance=connection::SchemaTarget_strategy)
def test_connection::schematarget_RelativeXPathQuery_type(instance):
    assert isinstance(instance.RelativeXPathQuery, str)


@given(instance=connection::SchemaTarget_strategy)
def test_connection::schematarget_RelativeXPathQuery_setter(instance):
    original = instance.RelativeXPathQuery
    instance.RelativeXPathQuery = original
    assert instance.RelativeXPathQuery == original

@given(instance=connection::XmlXPathLoopDescriptor_strategy)
@settings(max_examples=50)
def test_connection::xmlxpathloopdescriptor_instantiation(instance):
    assert isinstance(instance, connection::XmlXPathLoopDescriptor)

@given(instance=connection::XmlXPathLoopDescriptor_strategy)
def test_connection::xmlxpathloopdescriptor_LimitBoucle_type(instance):
    assert isinstance(instance.LimitBoucle, str)


@given(instance=connection::XmlXPathLoopDescriptor_strategy)
def test_connection::xmlxpathloopdescriptor_LimitBoucle_setter(instance):
    original = instance.LimitBoucle
    instance.LimitBoucle = original
    assert instance.LimitBoucle == original

@given(instance=connection::XmlXPathLoopDescriptor_strategy)
def test_connection::xmlxpathloopdescriptor_AbsoluteXPathQuery_type(instance):
    assert isinstance(instance.AbsoluteXPathQuery, str)


@given(instance=connection::XmlXPathLoopDescriptor_strategy)
def test_connection::xmlxpathloopdescriptor_AbsoluteXPathQuery_setter(instance):
    original = instance.AbsoluteXPathQuery
    instance.AbsoluteXPathQuery = original
    assert instance.AbsoluteXPathQuery == original

@given(instance=SAPFunctionParameterTable_strategy)
@settings(max_examples=50)
def test_sapfunctionparametertable_instantiation(instance):
    assert isinstance(instance, SAPFunctionParameterTable)

@given(instance=connection::SAPTestInputParameterTable_strategy)
@settings(max_examples=50)
def test_connection::saptestinputparametertable_instantiation(instance):
    assert isinstance(instance, connection::SAPTestInputParameterTable)

@given(instance=connection::CDCConnection_strategy)
@settings(max_examples=50)
def test_connection::cdcconnection_instantiation(instance):
    assert isinstance(instance, connection::CDCConnection)

@given(instance=connection::OutputSAPFunctionParameterTable_strategy)
@settings(max_examples=50)
def test_connection::outputsapfunctionparametertable_instantiation(instance):
    assert isinstance(instance, connection::OutputSAPFunctionParameterTable)

@given(instance=connection::InputSAPFunctionParameterTable_strategy)
@settings(max_examples=50)
def test_connection::inputsapfunctionparametertable_instantiation(instance):
    assert isinstance(instance, connection::InputSAPFunctionParameterTable)

@given(instance=FileConnection_strategy)
@settings(max_examples=50)
def test_fileconnection_instantiation(instance):
    assert isinstance(instance, FileConnection)

@given(instance=connection::EbcdicConnection_strategy)
@settings(max_examples=50)
def test_connection::ebcdicconnection_instantiation(instance):
    assert isinstance(instance, connection::EbcdicConnection)

@given(instance=connection::EbcdicConnection_strategy)
def test_connection::ebcdicconnection_MidFile_type(instance):
    assert isinstance(instance.MidFile, str)


@given(instance=connection::EbcdicConnection_strategy)
def test_connection::ebcdicconnection_MidFile_setter(instance):
    original = instance.MidFile
    instance.MidFile = original
    assert instance.MidFile == original

@given(instance=connection::EbcdicConnection_strategy)
def test_connection::ebcdicconnection_DataFile_type(instance):
    assert isinstance(instance.DataFile, str)


@given(instance=connection::EbcdicConnection_strategy)
def test_connection::ebcdicconnection_DataFile_setter(instance):
    original = instance.DataFile
    instance.DataFile = original
    assert instance.DataFile == original

@given(instance=connection::FileExcelConnection_strategy)
@settings(max_examples=50)
def test_connection::fileexcelconnection_instantiation(instance):
    assert isinstance(instance, connection::FileExcelConnection)

@given(instance=connection::FileExcelConnection_strategy)
def test_connection::fileexcelconnection_thousandSeparator_type(instance):
    assert isinstance(instance.thousandSeparator, str)


@given(instance=connection::FileExcelConnection_strategy)
def test_connection::fileexcelconnection_thousandSeparator_setter(instance):
    original = instance.thousandSeparator
    instance.thousandSeparator = original
    assert instance.thousandSeparator == original

@given(instance=connection::FileExcelConnection_strategy)
def test_connection::fileexcelconnection_sheetList_type(instance):
    assert isinstance(instance.sheetList, str)


@given(instance=connection::FileExcelConnection_strategy)
def test_connection::fileexcelconnection_sheetList_setter(instance):
    original = instance.sheetList
    instance.sheetList = original
    assert instance.sheetList == original

@given(instance=connection::FileExcelConnection_strategy)
def test_connection::fileexcelconnection_decimalSeparator_type(instance):
    assert isinstance(instance.decimalSeparator, str)


@given(instance=connection::FileExcelConnection_strategy)
def test_connection::fileexcelconnection_decimalSeparator_setter(instance):
    original = instance.decimalSeparator
    instance.decimalSeparator = original
    assert instance.decimalSeparator == original

@given(instance=connection::FileExcelConnection_strategy)
def test_connection::fileexcelconnection_lastColumn_type(instance):
    assert isinstance(instance.lastColumn, str)


@given(instance=connection::FileExcelConnection_strategy)
def test_connection::fileexcelconnection_lastColumn_setter(instance):
    original = instance.lastColumn
    instance.lastColumn = original
    assert instance.lastColumn == original

@given(instance=connection::FileExcelConnection_strategy)
def test_connection::fileexcelconnection_selectAllSheets_type(instance):
    assert isinstance(instance.selectAllSheets, bool)


@given(instance=connection::FileExcelConnection_strategy)
def test_connection::fileexcelconnection_selectAllSheets_setter(instance):
    original = instance.selectAllSheets
    instance.selectAllSheets = original
    assert instance.selectAllSheets == original

@given(instance=connection::FileExcelConnection_strategy)
def test_connection::fileexcelconnection_SheetName_type(instance):
    assert isinstance(instance.SheetName, str)


@given(instance=connection::FileExcelConnection_strategy)
def test_connection::fileexcelconnection_SheetName_setter(instance):
    original = instance.SheetName
    instance.SheetName = original
    assert instance.SheetName == original

@given(instance=connection::FileExcelConnection_strategy)
def test_connection::fileexcelconnection_sheetColumns_type(instance):
    assert isinstance(instance.sheetColumns, str)


@given(instance=connection::FileExcelConnection_strategy)
def test_connection::fileexcelconnection_sheetColumns_setter(instance):
    original = instance.sheetColumns
    instance.sheetColumns = original
    assert instance.sheetColumns == original

@given(instance=connection::FileExcelConnection_strategy)
def test_connection::fileexcelconnection_firstColumn_type(instance):
    assert isinstance(instance.firstColumn, str)


@given(instance=connection::FileExcelConnection_strategy)
def test_connection::fileexcelconnection_firstColumn_setter(instance):
    original = instance.firstColumn
    instance.firstColumn = original
    assert instance.firstColumn == original

@given(instance=connection::FileExcelConnection_strategy)
def test_connection::fileexcelconnection_advancedSpearator_type(instance):
    assert isinstance(instance.advancedSpearator, bool)


@given(instance=connection::FileExcelConnection_strategy)
def test_connection::fileexcelconnection_advancedSpearator_setter(instance):
    original = instance.advancedSpearator
    instance.advancedSpearator = original
    assert instance.advancedSpearator == original

@given(instance=connection::RegexpFileConnection_strategy)
@settings(max_examples=50)
def test_connection::regexpfileconnection_instantiation(instance):
    assert isinstance(instance, connection::RegexpFileConnection)

@given(instance=connection::RegexpFileConnection_strategy)
def test_connection::regexpfileconnection_FieldSeparatorType_type(instance):
    assert isinstance(instance.FieldSeparatorType, str)


@given(instance=connection::RegexpFileConnection_strategy)
def test_connection::regexpfileconnection_FieldSeparatorType_setter(instance):
    original = instance.FieldSeparatorType
    instance.FieldSeparatorType = original
    assert instance.FieldSeparatorType == original

@given(instance=connection::HL7Connection_strategy)
@settings(max_examples=50)
def test_connection::hl7connection_instantiation(instance):
    assert isinstance(instance, connection::HL7Connection)

@given(instance=connection::HL7Connection_strategy)
def test_connection::hl7connection_EndChar_type(instance):
    assert isinstance(instance.EndChar, str)


@given(instance=connection::HL7Connection_strategy)
def test_connection::hl7connection_EndChar_setter(instance):
    original = instance.EndChar
    instance.EndChar = original
    assert instance.EndChar == original

@given(instance=connection::HL7Connection_strategy)
def test_connection::hl7connection_StartChar_type(instance):
    assert isinstance(instance.StartChar, str)


@given(instance=connection::HL7Connection_strategy)
def test_connection::hl7connection_StartChar_setter(instance):
    original = instance.StartChar
    instance.StartChar = original
    assert instance.StartChar == original

@given(instance=connection::PositionalFileConnection_strategy)
@settings(max_examples=50)
def test_connection::positionalfileconnection_instantiation(instance):
    assert isinstance(instance, connection::PositionalFileConnection)

@given(instance=connection::DelimitedFileConnection_strategy)
@settings(max_examples=50)
def test_connection::delimitedfileconnection_instantiation(instance):
    assert isinstance(instance, connection::DelimitedFileConnection)

@given(instance=connection::DelimitedFileConnection_strategy)
def test_connection::delimitedfileconnection_FieldSeparatorType_type(instance):
    assert isinstance(instance.FieldSeparatorType, str)


@given(instance=connection::DelimitedFileConnection_strategy)
def test_connection::delimitedfileconnection_FieldSeparatorType_setter(instance):
    original = instance.FieldSeparatorType
    instance.FieldSeparatorType = original
    assert instance.FieldSeparatorType == original

@given(instance=connection::DelimitedFileConnection_strategy)
def test_connection::delimitedfileconnection_splitRecord_type(instance):
    assert isinstance(instance.splitRecord, bool)


@given(instance=connection::DelimitedFileConnection_strategy)
def test_connection::delimitedfileconnection_splitRecord_setter(instance):
    original = instance.splitRecord
    instance.splitRecord = original
    assert instance.splitRecord == original

@given(instance=connection::Concept_strategy)
@settings(max_examples=50)
def test_connection::concept_instantiation(instance):
    assert isinstance(instance, connection::Concept)

@given(instance=connection::Concept_strategy)
def test_connection::concept_LoopExpression_type(instance):
    assert isinstance(instance.LoopExpression, str)


@given(instance=connection::Concept_strategy)
def test_connection::concept_LoopExpression_setter(instance):
    original = instance.LoopExpression
    instance.LoopExpression = original
    assert instance.LoopExpression == original

@given(instance=connection::Concept_strategy)
def test_connection::concept_LoopLimit_type(instance):
    assert isinstance(instance.LoopLimit, str)


@given(instance=connection::Concept_strategy)
def test_connection::concept_LoopLimit_setter(instance):
    original = instance.LoopLimit
    instance.LoopLimit = original
    assert instance.LoopLimit == original

@given(instance=Connection_strategy)
@settings(max_examples=50)
def test_connection_instantiation(instance):
    assert isinstance(instance, Connection)

@given(instance=connection::SalesforceSchemaConnection_strategy)
@settings(max_examples=50)
def test_connection::salesforceschemaconnection_instantiation(instance):
    assert isinstance(instance, connection::SalesforceSchemaConnection)

@given(instance=connection::SalesforceSchemaConnection_strategy)
def test_connection::salesforceschemaconnection_userName_type(instance):
    assert isinstance(instance.userName, str)


@given(instance=connection::SalesforceSchemaConnection_strategy)
def test_connection::salesforceschemaconnection_userName_setter(instance):
    original = instance.userName
    instance.userName = original
    assert instance.userName == original

@given(instance=connection::SalesforceSchemaConnection_strategy)
def test_connection::salesforceschemaconnection_useCustomModuleName_type(instance):
    assert isinstance(instance.useCustomModuleName, bool)


@given(instance=connection::SalesforceSchemaConnection_strategy)
def test_connection::salesforceschemaconnection_useCustomModuleName_setter(instance):
    original = instance.useCustomModuleName
    instance.useCustomModuleName = original
    assert instance.useCustomModuleName == original

@given(instance=connection::SalesforceSchemaConnection_strategy)
def test_connection::salesforceschemaconnection_webServiceUrl_type(instance):
    assert isinstance(instance.webServiceUrl, str)


@given(instance=connection::SalesforceSchemaConnection_strategy)
def test_connection::salesforceschemaconnection_webServiceUrl_setter(instance):
    original = instance.webServiceUrl
    instance.webServiceUrl = original
    assert instance.webServiceUrl == original

@given(instance=connection::SalesforceSchemaConnection_strategy)
def test_connection::salesforceschemaconnection_proxyHost_type(instance):
    assert isinstance(instance.proxyHost, str)


@given(instance=connection::SalesforceSchemaConnection_strategy)
def test_connection::salesforceschemaconnection_proxyHost_setter(instance):
    original = instance.proxyHost
    instance.proxyHost = original
    assert instance.proxyHost == original

@given(instance=connection::SalesforceSchemaConnection_strategy)
def test_connection::salesforceschemaconnection_password_type(instance):
    assert isinstance(instance.password, str)


@given(instance=connection::SalesforceSchemaConnection_strategy)
def test_connection::salesforceschemaconnection_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=connection::SalesforceSchemaConnection_strategy)
def test_connection::salesforceschemaconnection_timeOut_type(instance):
    assert isinstance(instance.timeOut, str)


@given(instance=connection::SalesforceSchemaConnection_strategy)
def test_connection::salesforceschemaconnection_timeOut_setter(instance):
    original = instance.timeOut
    instance.timeOut = original
    assert instance.timeOut == original

@given(instance=connection::SalesforceSchemaConnection_strategy)
def test_connection::salesforceschemaconnection_proxyPort_type(instance):
    assert isinstance(instance.proxyPort, str)


@given(instance=connection::SalesforceSchemaConnection_strategy)
def test_connection::salesforceschemaconnection_proxyPort_setter(instance):
    original = instance.proxyPort
    instance.proxyPort = original
    assert instance.proxyPort == original

@given(instance=connection::SalesforceSchemaConnection_strategy)
def test_connection::salesforceschemaconnection_useHttpProxy_type(instance):
    assert isinstance(instance.useHttpProxy, bool)


@given(instance=connection::SalesforceSchemaConnection_strategy)
def test_connection::salesforceschemaconnection_useHttpProxy_setter(instance):
    original = instance.useHttpProxy
    instance.useHttpProxy = original
    assert instance.useHttpProxy == original

@given(instance=connection::SalesforceSchemaConnection_strategy)
def test_connection::salesforceschemaconnection_batchSize_type(instance):
    assert isinstance(instance.batchSize, str)


@given(instance=connection::SalesforceSchemaConnection_strategy)
def test_connection::salesforceschemaconnection_batchSize_setter(instance):
    original = instance.batchSize
    instance.batchSize = original
    assert instance.batchSize == original

@given(instance=connection::SalesforceSchemaConnection_strategy)
def test_connection::salesforceschemaconnection_queryCondition_type(instance):
    assert isinstance(instance.queryCondition, str)


@given(instance=connection::SalesforceSchemaConnection_strategy)
def test_connection::salesforceschemaconnection_queryCondition_setter(instance):
    original = instance.queryCondition
    instance.queryCondition = original
    assert instance.queryCondition == original

@given(instance=connection::SalesforceSchemaConnection_strategy)
def test_connection::salesforceschemaconnection_moduleName_type(instance):
    assert isinstance(instance.moduleName, str)


@given(instance=connection::SalesforceSchemaConnection_strategy)
def test_connection::salesforceschemaconnection_moduleName_setter(instance):
    original = instance.moduleName
    instance.moduleName = original
    assert instance.moduleName == original

@given(instance=connection::SalesforceSchemaConnection_strategy)
def test_connection::salesforceschemaconnection_useProxy_type(instance):
    assert isinstance(instance.useProxy, bool)


@given(instance=connection::SalesforceSchemaConnection_strategy)
def test_connection::salesforceschemaconnection_useProxy_setter(instance):
    original = instance.useProxy
    instance.useProxy = original
    assert instance.useProxy == original

@given(instance=connection::SalesforceSchemaConnection_strategy)
def test_connection::salesforceschemaconnection_proxyUsername_type(instance):
    assert isinstance(instance.proxyUsername, str)


@given(instance=connection::SalesforceSchemaConnection_strategy)
def test_connection::salesforceschemaconnection_proxyUsername_setter(instance):
    original = instance.proxyUsername
    instance.proxyUsername = original
    assert instance.proxyUsername == original

@given(instance=connection::SalesforceSchemaConnection_strategy)
def test_connection::salesforceschemaconnection_proxyPassword_type(instance):
    assert isinstance(instance.proxyPassword, str)


@given(instance=connection::SalesforceSchemaConnection_strategy)
def test_connection::salesforceschemaconnection_proxyPassword_setter(instance):
    original = instance.proxyPassword
    instance.proxyPassword = original
    assert instance.proxyPassword == original

@given(instance=connection::SalesforceSchemaConnection_strategy)
def test_connection::salesforceschemaconnection_useAlphbet_type(instance):
    assert isinstance(instance.useAlphbet, bool)


@given(instance=connection::SalesforceSchemaConnection_strategy)
def test_connection::salesforceschemaconnection_useAlphbet_setter(instance):
    original = instance.useAlphbet
    instance.useAlphbet = original
    assert instance.useAlphbet == original

@given(instance=connection::XmlFileConnection_strategy)
@settings(max_examples=50)
def test_connection::xmlfileconnection_instantiation(instance):
    assert isinstance(instance, connection::XmlFileConnection)

@given(instance=connection::XmlFileConnection_strategy)
def test_connection::xmlfileconnection_XsdFilePath_type(instance):
    assert isinstance(instance.XsdFilePath, str)


@given(instance=connection::XmlFileConnection_strategy)
def test_connection::xmlfileconnection_XsdFilePath_setter(instance):
    original = instance.XsdFilePath
    instance.XsdFilePath = original
    assert instance.XsdFilePath == original

@given(instance=connection::XmlFileConnection_strategy)
def test_connection::xmlfileconnection_Encoding_type(instance):
    assert isinstance(instance.Encoding, str)


@given(instance=connection::XmlFileConnection_strategy)
def test_connection::xmlfileconnection_Encoding_setter(instance):
    original = instance.Encoding
    instance.Encoding = original
    assert instance.Encoding == original

@given(instance=connection::XmlFileConnection_strategy)
def test_connection::xmlfileconnection_XmlFilePath_type(instance):
    assert isinstance(instance.XmlFilePath, str)


@given(instance=connection::XmlFileConnection_strategy)
def test_connection::xmlfileconnection_XmlFilePath_setter(instance):
    original = instance.XmlFilePath
    instance.XmlFilePath = original
    assert instance.XmlFilePath == original

@given(instance=connection::XmlFileConnection_strategy)
def test_connection::xmlfileconnection_MaskXPattern_type(instance):
    assert isinstance(instance.MaskXPattern, str)


@given(instance=connection::XmlFileConnection_strategy)
def test_connection::xmlfileconnection_MaskXPattern_setter(instance):
    original = instance.MaskXPattern
    instance.MaskXPattern = original
    assert instance.MaskXPattern == original

@given(instance=connection::XmlFileConnection_strategy)
def test_connection::xmlfileconnection_Guess_type(instance):
    assert isinstance(instance.Guess, bool)


@given(instance=connection::XmlFileConnection_strategy)
def test_connection::xmlfileconnection_Guess_setter(instance):
    original = instance.Guess
    instance.Guess = original
    assert instance.Guess == original

@given(instance=connection::MDMConnection_strategy)
@settings(max_examples=50)
def test_connection::mdmconnection_instantiation(instance):
    assert isinstance(instance, connection::MDMConnection)

@given(instance=connection::MDMConnection_strategy)
def test_connection::mdmconnection_Password_type(instance):
    assert isinstance(instance.Password, str)


@given(instance=connection::MDMConnection_strategy)
def test_connection::mdmconnection_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original

@given(instance=connection::MDMConnection_strategy)
def test_connection::mdmconnection_Datamodel_type(instance):
    assert isinstance(instance.Datamodel, str)


@given(instance=connection::MDMConnection_strategy)
def test_connection::mdmconnection_Datamodel_setter(instance):
    original = instance.Datamodel
    instance.Datamodel = original
    assert instance.Datamodel == original

@given(instance=connection::MDMConnection_strategy)
def test_connection::mdmconnection_Datacluster_type(instance):
    assert isinstance(instance.Datacluster, str)


@given(instance=connection::MDMConnection_strategy)
def test_connection::mdmconnection_Datacluster_setter(instance):
    original = instance.Datacluster
    instance.Datacluster = original
    assert instance.Datacluster == original

@given(instance=connection::MDMConnection_strategy)
def test_connection::mdmconnection_Username_type(instance):
    assert isinstance(instance.Username, str)


@given(instance=connection::MDMConnection_strategy)
def test_connection::mdmconnection_Username_setter(instance):
    original = instance.Username
    instance.Username = original
    assert instance.Username == original

@given(instance=connection::MDMConnection_strategy)
def test_connection::mdmconnection_Server_type(instance):
    assert isinstance(instance.Server, str)


@given(instance=connection::MDMConnection_strategy)
def test_connection::mdmconnection_Server_setter(instance):
    original = instance.Server
    instance.Server = original
    assert instance.Server == original

@given(instance=connection::MDMConnection_strategy)
def test_connection::mdmconnection_Universe_type(instance):
    assert isinstance(instance.Universe, str)


@given(instance=connection::MDMConnection_strategy)
def test_connection::mdmconnection_Universe_setter(instance):
    original = instance.Universe
    instance.Universe = original
    assert instance.Universe == original

@given(instance=connection::MDMConnection_strategy)
def test_connection::mdmconnection_Port_type(instance):
    assert isinstance(instance.Port, str)


@given(instance=connection::MDMConnection_strategy)
def test_connection::mdmconnection_Port_setter(instance):
    original = instance.Port
    instance.Port = original
    assert instance.Port == original

@given(instance=connection::WSDLSchemaConnection_strategy)
@settings(max_examples=50)
def test_connection::wsdlschemaconnection_instantiation(instance):
    assert isinstance(instance, connection::WSDLSchemaConnection)

@given(instance=connection::WSDLSchemaConnection_strategy)
def test_connection::wsdlschemaconnection_proxyPassword_type(instance):
    assert isinstance(instance.proxyPassword, str)


@given(instance=connection::WSDLSchemaConnection_strategy)
def test_connection::wsdlschemaconnection_proxyPassword_setter(instance):
    original = instance.proxyPassword
    instance.proxyPassword = original
    assert instance.proxyPassword == original

@given(instance=connection::WSDLSchemaConnection_strategy)
def test_connection::wsdlschemaconnection_Password_type(instance):
    assert isinstance(instance.Password, str)


@given(instance=connection::WSDLSchemaConnection_strategy)
def test_connection::wsdlschemaconnection_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original

@given(instance=connection::WSDLSchemaConnection_strategy)
def test_connection::wsdlschemaconnection_EndpointURI_type(instance):
    assert isinstance(instance.EndpointURI, str)


@given(instance=connection::WSDLSchemaConnection_strategy)
def test_connection::wsdlschemaconnection_EndpointURI_setter(instance):
    original = instance.EndpointURI
    instance.EndpointURI = original
    assert instance.EndpointURI == original

@given(instance=connection::WSDLSchemaConnection_strategy)
def test_connection::wsdlschemaconnection_proxyUser_type(instance):
    assert isinstance(instance.proxyUser, str)


@given(instance=connection::WSDLSchemaConnection_strategy)
def test_connection::wsdlschemaconnection_proxyUser_setter(instance):
    original = instance.proxyUser
    instance.proxyUser = original
    assert instance.proxyUser == original

@given(instance=connection::WSDLSchemaConnection_strategy)
def test_connection::wsdlschemaconnection_proxyHost_type(instance):
    assert isinstance(instance.proxyHost, str)


@given(instance=connection::WSDLSchemaConnection_strategy)
def test_connection::wsdlschemaconnection_proxyHost_setter(instance):
    original = instance.proxyHost
    instance.proxyHost = original
    assert instance.proxyHost == original

@given(instance=connection::WSDLSchemaConnection_strategy)
def test_connection::wsdlschemaconnection_needAuth_type(instance):
    assert isinstance(instance.needAuth, bool)


@given(instance=connection::WSDLSchemaConnection_strategy)
def test_connection::wsdlschemaconnection_needAuth_setter(instance):
    original = instance.needAuth
    instance.needAuth = original
    assert instance.needAuth == original

@given(instance=connection::WSDLSchemaConnection_strategy)
def test_connection::wsdlschemaconnection_proxyPort_type(instance):
    assert isinstance(instance.proxyPort, str)


@given(instance=connection::WSDLSchemaConnection_strategy)
def test_connection::wsdlschemaconnection_proxyPort_setter(instance):
    original = instance.proxyPort
    instance.proxyPort = original
    assert instance.proxyPort == original

@given(instance=connection::WSDLSchemaConnection_strategy)
def test_connection::wsdlschemaconnection_parameters_type(instance):
    assert isinstance(instance.parameters, str)


@given(instance=connection::WSDLSchemaConnection_strategy)
def test_connection::wsdlschemaconnection_parameters_setter(instance):
    original = instance.parameters
    instance.parameters = original
    assert instance.parameters == original

@given(instance=connection::WSDLSchemaConnection_strategy)
def test_connection::wsdlschemaconnection_Encoding_type(instance):
    assert isinstance(instance.Encoding, str)


@given(instance=connection::WSDLSchemaConnection_strategy)
def test_connection::wsdlschemaconnection_Encoding_setter(instance):
    original = instance.Encoding
    instance.Encoding = original
    assert instance.Encoding == original

@given(instance=connection::WSDLSchemaConnection_strategy)
def test_connection::wsdlschemaconnection_methodName_type(instance):
    assert isinstance(instance.methodName, str)


@given(instance=connection::WSDLSchemaConnection_strategy)
def test_connection::wsdlschemaconnection_methodName_setter(instance):
    original = instance.methodName
    instance.methodName = original
    assert instance.methodName == original

@given(instance=connection::WSDLSchemaConnection_strategy)
def test_connection::wsdlschemaconnection_useProxy_type(instance):
    assert isinstance(instance.useProxy, bool)


@given(instance=connection::WSDLSchemaConnection_strategy)
def test_connection::wsdlschemaconnection_useProxy_setter(instance):
    original = instance.useProxy
    instance.useProxy = original
    assert instance.useProxy == original

@given(instance=connection::WSDLSchemaConnection_strategy)
def test_connection::wsdlschemaconnection_UserName_type(instance):
    assert isinstance(instance.UserName, str)


@given(instance=connection::WSDLSchemaConnection_strategy)
def test_connection::wsdlschemaconnection_UserName_setter(instance):
    original = instance.UserName
    instance.UserName = original
    assert instance.UserName == original

@given(instance=connection::WSDLSchemaConnection_strategy)
def test_connection::wsdlschemaconnection_timeOut_type(instance):
    assert isinstance(instance.timeOut, int)


@given(instance=connection::WSDLSchemaConnection_strategy)
def test_connection::wsdlschemaconnection_timeOut_setter(instance):
    original = instance.timeOut
    instance.timeOut = original
    assert instance.timeOut == original

@given(instance=connection::WSDLSchemaConnection_strategy)
def test_connection::wsdlschemaconnection_WSDL_type(instance):
    assert isinstance(instance.WSDL, str)


@given(instance=connection::WSDLSchemaConnection_strategy)
def test_connection::wsdlschemaconnection_WSDL_setter(instance):
    original = instance.WSDL
    instance.WSDL = original
    assert instance.WSDL == original

@given(instance=connection::WSDLSchemaConnection_strategy)
def test_connection::wsdlschemaconnection_Value_type(instance):
    assert isinstance(instance.Value, str)


@given(instance=connection::WSDLSchemaConnection_strategy)
def test_connection::wsdlschemaconnection_Value_setter(instance):
    original = instance.Value
    instance.Value = original
    assert instance.Value == original

@given(instance=connection::GenericSchemaConnection_strategy)
@settings(max_examples=50)
def test_connection::genericschemaconnection_instantiation(instance):
    assert isinstance(instance, connection::GenericSchemaConnection)

@given(instance=connection::GenericSchemaConnection_strategy)
def test_connection::genericschemaconnection_mappingTypeId_type(instance):
    assert isinstance(instance.mappingTypeId, str)


@given(instance=connection::GenericSchemaConnection_strategy)
def test_connection::genericschemaconnection_mappingTypeId_setter(instance):
    original = instance.mappingTypeId
    instance.mappingTypeId = original
    assert instance.mappingTypeId == original

@given(instance=connection::GenericSchemaConnection_strategy)
def test_connection::genericschemaconnection_mappingTypeUsed_type(instance):
    assert isinstance(instance.mappingTypeUsed, bool)


@given(instance=connection::GenericSchemaConnection_strategy)
def test_connection::genericschemaconnection_mappingTypeUsed_setter(instance):
    original = instance.mappingTypeUsed
    instance.mappingTypeUsed = original
    assert instance.mappingTypeUsed == original

@given(instance=connection::LdifFileConnection_strategy)
@settings(max_examples=50)
def test_connection::ldiffileconnection_instantiation(instance):
    assert isinstance(instance, connection::LdifFileConnection)

@given(instance=connection::LdifFileConnection_strategy)
def test_connection::ldiffileconnection_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=connection::LdifFileConnection_strategy)
def test_connection::ldiffileconnection_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=connection::LdifFileConnection_strategy)
def test_connection::ldiffileconnection_LimitEntry_type(instance):
    assert isinstance(instance.LimitEntry, int)


@given(instance=connection::LdifFileConnection_strategy)
def test_connection::ldiffileconnection_LimitEntry_setter(instance):
    original = instance.LimitEntry
    instance.LimitEntry = original
    assert instance.LimitEntry == original

@given(instance=connection::LdifFileConnection_strategy)
def test_connection::ldiffileconnection_FilePath_type(instance):
    assert isinstance(instance.FilePath, str)


@given(instance=connection::LdifFileConnection_strategy)
def test_connection::ldiffileconnection_FilePath_setter(instance):
    original = instance.FilePath
    instance.FilePath = original
    assert instance.FilePath == original

@given(instance=connection::LdifFileConnection_strategy)
def test_connection::ldiffileconnection_UseLimit_type(instance):
    assert isinstance(instance.UseLimit, bool)


@given(instance=connection::LdifFileConnection_strategy)
def test_connection::ldiffileconnection_UseLimit_setter(instance):
    original = instance.UseLimit
    instance.UseLimit = original
    assert instance.UseLimit == original

@given(instance=connection::LdifFileConnection_strategy)
def test_connection::ldiffileconnection_Server_type(instance):
    assert isinstance(instance.Server, str)


@given(instance=connection::LdifFileConnection_strategy)
def test_connection::ldiffileconnection_Server_setter(instance):
    original = instance.Server
    instance.Server = original
    assert instance.Server == original

@given(instance=connection::SAPConnection_strategy)
@settings(max_examples=50)
def test_connection::sapconnection_instantiation(instance):
    assert isinstance(instance, connection::SAPConnection)

@given(instance=connection::SAPConnection_strategy)
def test_connection::sapconnection_Username_type(instance):
    assert isinstance(instance.Username, str)


@given(instance=connection::SAPConnection_strategy)
def test_connection::sapconnection_Username_setter(instance):
    original = instance.Username
    instance.Username = original
    assert instance.Username == original

@given(instance=connection::SAPConnection_strategy)
def test_connection::sapconnection_Host_type(instance):
    assert isinstance(instance.Host, str)


@given(instance=connection::SAPConnection_strategy)
def test_connection::sapconnection_Host_setter(instance):
    original = instance.Host
    instance.Host = original
    assert instance.Host == original

@given(instance=connection::SAPConnection_strategy)
def test_connection::sapconnection_currentFucntion_type(instance):
    assert isinstance(instance.currentFucntion, str)


@given(instance=connection::SAPConnection_strategy)
def test_connection::sapconnection_currentFucntion_setter(instance):
    original = instance.currentFucntion
    instance.currentFucntion = original
    assert instance.currentFucntion == original

@given(instance=connection::SAPConnection_strategy)
def test_connection::sapconnection_SystemNumber_type(instance):
    assert isinstance(instance.SystemNumber, str)


@given(instance=connection::SAPConnection_strategy)
def test_connection::sapconnection_SystemNumber_setter(instance):
    original = instance.SystemNumber
    instance.SystemNumber = original
    assert instance.SystemNumber == original

@given(instance=connection::SAPConnection_strategy)
def test_connection::sapconnection_Password_type(instance):
    assert isinstance(instance.Password, str)


@given(instance=connection::SAPConnection_strategy)
def test_connection::sapconnection_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original

@given(instance=connection::SAPConnection_strategy)
def test_connection::sapconnection_Language_type(instance):
    assert isinstance(instance.Language, str)


@given(instance=connection::SAPConnection_strategy)
def test_connection::sapconnection_Language_setter(instance):
    original = instance.Language
    instance.Language = original
    assert instance.Language == original

@given(instance=connection::SAPConnection_strategy)
def test_connection::sapconnection_Client_type(instance):
    assert isinstance(instance.Client, str)


@given(instance=connection::SAPConnection_strategy)
def test_connection::sapconnection_Client_setter(instance):
    original = instance.Client
    instance.Client = original
    assert instance.Client == original

@given(instance=connection::DatabaseConnection_strategy)
@settings(max_examples=50)
def test_connection::databaseconnection_instantiation(instance):
    assert isinstance(instance, connection::DatabaseConnection)

@given(instance=connection::DatabaseConnection_strategy)
def test_connection::databaseconnection_AdditionalParams_type(instance):
    assert isinstance(instance.AdditionalParams, str)


@given(instance=connection::DatabaseConnection_strategy)
def test_connection::databaseconnection_AdditionalParams_setter(instance):
    original = instance.AdditionalParams
    instance.AdditionalParams = original
    assert instance.AdditionalParams == original

@given(instance=connection::DatabaseConnection_strategy)
def test_connection::databaseconnection_Username_type(instance):
    assert isinstance(instance.Username, str)


@given(instance=connection::DatabaseConnection_strategy)
def test_connection::databaseconnection_Username_setter(instance):
    original = instance.Username
    instance.Username = original
    assert instance.Username == original

@given(instance=connection::DatabaseConnection_strategy)
def test_connection::databaseconnection_dbVersionString_type(instance):
    assert isinstance(instance.dbVersionString, str)


@given(instance=connection::DatabaseConnection_strategy)
def test_connection::databaseconnection_dbVersionString_setter(instance):
    original = instance.dbVersionString
    instance.dbVersionString = original
    assert instance.dbVersionString == original

@given(instance=connection::DatabaseConnection_strategy)
def test_connection::databaseconnection_SqlSynthax_type(instance):
    assert isinstance(instance.SqlSynthax, str)


@given(instance=connection::DatabaseConnection_strategy)
def test_connection::databaseconnection_SqlSynthax_setter(instance):
    original = instance.SqlSynthax
    instance.SqlSynthax = original
    assert instance.SqlSynthax == original

@given(instance=connection::DatabaseConnection_strategy)
def test_connection::databaseconnection_Port_type(instance):
    assert isinstance(instance.Port, str)


@given(instance=connection::DatabaseConnection_strategy)
def test_connection::databaseconnection_Port_setter(instance):
    original = instance.Port
    instance.Port = original
    assert instance.Port == original

@given(instance=connection::DatabaseConnection_strategy)
def test_connection::databaseconnection_StandardSQL_type(instance):
    assert isinstance(instance.StandardSQL, bool)


@given(instance=connection::DatabaseConnection_strategy)
def test_connection::databaseconnection_StandardSQL_setter(instance):
    original = instance.StandardSQL
    instance.StandardSQL = original
    assert instance.StandardSQL == original

@given(instance=connection::DatabaseConnection_strategy)
def test_connection::databaseconnection_FileFieldName_type(instance):
    assert isinstance(instance.FileFieldName, str)


@given(instance=connection::DatabaseConnection_strategy)
def test_connection::databaseconnection_FileFieldName_setter(instance):
    original = instance.FileFieldName
    instance.FileFieldName = original
    assert instance.FileFieldName == original

@given(instance=connection::DatabaseConnection_strategy)
def test_connection::databaseconnection_DbmsId_type(instance):
    assert isinstance(instance.DbmsId, str)


@given(instance=connection::DatabaseConnection_strategy)
def test_connection::databaseconnection_DbmsId_setter(instance):
    original = instance.DbmsId
    instance.DbmsId = original
    assert instance.DbmsId == original

@given(instance=connection::DatabaseConnection_strategy)
def test_connection::databaseconnection_ServerName_type(instance):
    assert isinstance(instance.ServerName, str)


@given(instance=connection::DatabaseConnection_strategy)
def test_connection::databaseconnection_ServerName_setter(instance):
    original = instance.ServerName
    instance.ServerName = original
    assert instance.ServerName == original

@given(instance=connection::DatabaseConnection_strategy)
def test_connection::databaseconnection_DatabaseType_type(instance):
    assert isinstance(instance.DatabaseType, str)


@given(instance=connection::DatabaseConnection_strategy)
def test_connection::databaseconnection_DatabaseType_setter(instance):
    original = instance.DatabaseType
    instance.DatabaseType = original
    assert instance.DatabaseType == original

@given(instance=connection::DatabaseConnection_strategy)
def test_connection::databaseconnection_SQLMode_type(instance):
    assert isinstance(instance.SQLMode, bool)


@given(instance=connection::DatabaseConnection_strategy)
def test_connection::databaseconnection_SQLMode_setter(instance):
    original = instance.SQLMode
    instance.SQLMode = original
    assert instance.SQLMode == original

@given(instance=connection::DatabaseConnection_strategy)
def test_connection::databaseconnection_SystemSQL_type(instance):
    assert isinstance(instance.SystemSQL, bool)


@given(instance=connection::DatabaseConnection_strategy)
def test_connection::databaseconnection_SystemSQL_setter(instance):
    original = instance.SystemSQL
    instance.SystemSQL = original
    assert instance.SystemSQL == original

@given(instance=connection::DatabaseConnection_strategy)
def test_connection::databaseconnection_DriverJarPath_type(instance):
    assert isinstance(instance.DriverJarPath, str)


@given(instance=connection::DatabaseConnection_strategy)
def test_connection::databaseconnection_DriverJarPath_setter(instance):
    original = instance.DriverJarPath
    instance.DriverJarPath = original
    assert instance.DriverJarPath == original

@given(instance=connection::DatabaseConnection_strategy)
def test_connection::databaseconnection_cdcTypeMode_type(instance):
    assert isinstance(instance.cdcTypeMode, str)


@given(instance=connection::DatabaseConnection_strategy)
def test_connection::databaseconnection_cdcTypeMode_setter(instance):
    original = instance.cdcTypeMode
    instance.cdcTypeMode = original
    assert instance.cdcTypeMode == original

@given(instance=connection::DatabaseConnection_strategy)
def test_connection::databaseconnection_DatasourceName_type(instance):
    assert isinstance(instance.DatasourceName, str)


@given(instance=connection::DatabaseConnection_strategy)
def test_connection::databaseconnection_DatasourceName_setter(instance):
    original = instance.DatasourceName
    instance.DatasourceName = original
    assert instance.DatasourceName == original

@given(instance=connection::DatabaseConnection_strategy)
def test_connection::databaseconnection_DriverClass_type(instance):
    assert isinstance(instance.DriverClass, str)


@given(instance=connection::DatabaseConnection_strategy)
def test_connection::databaseconnection_DriverClass_setter(instance):
    original = instance.DriverClass
    instance.DriverClass = original
    assert instance.DriverClass == original

@given(instance=connection::DatabaseConnection_strategy)
def test_connection::databaseconnection_NullChar_type(instance):
    assert isinstance(instance.NullChar, str)


@given(instance=connection::DatabaseConnection_strategy)
def test_connection::databaseconnection_NullChar_setter(instance):
    original = instance.NullChar
    instance.NullChar = original
    assert instance.NullChar == original

@given(instance=connection::DatabaseConnection_strategy)
def test_connection::databaseconnection_SID_type(instance):
    assert isinstance(instance.SID, str)


@given(instance=connection::DatabaseConnection_strategy)
def test_connection::databaseconnection_SID_setter(instance):
    original = instance.SID
    instance.SID = original
    assert instance.SID == original

@given(instance=connection::DatabaseConnection_strategy)
def test_connection::databaseconnection_DBRootPath_type(instance):
    assert isinstance(instance.DBRootPath, str)


@given(instance=connection::DatabaseConnection_strategy)
def test_connection::databaseconnection_DBRootPath_setter(instance):
    original = instance.DBRootPath
    instance.DBRootPath = original
    assert instance.DBRootPath == original

@given(instance=connection::DatabaseConnection_strategy)
def test_connection::databaseconnection_StringQuote_type(instance):
    assert isinstance(instance.StringQuote, str)


@given(instance=connection::DatabaseConnection_strategy)
def test_connection::databaseconnection_StringQuote_setter(instance):
    original = instance.StringQuote
    instance.StringQuote = original
    assert instance.StringQuote == original

@given(instance=connection::DatabaseConnection_strategy)
def test_connection::databaseconnection_ProductId_type(instance):
    assert isinstance(instance.ProductId, str)


@given(instance=connection::DatabaseConnection_strategy)
def test_connection::databaseconnection_ProductId_setter(instance):
    original = instance.ProductId
    instance.ProductId = original
    assert instance.ProductId == original

@given(instance=connection::DatabaseConnection_strategy)
def test_connection::databaseconnection_Schema_type(instance):
    assert isinstance(instance.Schema, str)


@given(instance=connection::DatabaseConnection_strategy)
def test_connection::databaseconnection_Schema_setter(instance):
    original = instance.Schema
    instance.Schema = original
    assert instance.Schema == original

@given(instance=connection::DatabaseConnection_strategy)
def test_connection::databaseconnection_Password_type(instance):
    assert isinstance(instance.Password, str)


@given(instance=connection::DatabaseConnection_strategy)
def test_connection::databaseconnection_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original

@given(instance=connection::DatabaseConnection_strategy)
def test_connection::databaseconnection_URL_type(instance):
    assert isinstance(instance.URL, str)


@given(instance=connection::DatabaseConnection_strategy)
def test_connection::databaseconnection_URL_setter(instance):
    original = instance.URL
    instance.URL = original
    assert instance.URL == original

@given(instance=connection::LDAPSchemaConnection_strategy)
@settings(max_examples=50)
def test_connection::ldapschemaconnection_instantiation(instance):
    assert isinstance(instance, connection::LDAPSchemaConnection)

@given(instance=connection::LDAPSchemaConnection_strategy)
def test_connection::ldapschemaconnection_GetBaseDNsFromRoot_type(instance):
    assert isinstance(instance.GetBaseDNsFromRoot, bool)


@given(instance=connection::LDAPSchemaConnection_strategy)
def test_connection::ldapschemaconnection_GetBaseDNsFromRoot_setter(instance):
    original = instance.GetBaseDNsFromRoot
    instance.GetBaseDNsFromRoot = original
    assert instance.GetBaseDNsFromRoot == original

@given(instance=connection::LDAPSchemaConnection_strategy)
def test_connection::ldapschemaconnection_BindPrincipal_type(instance):
    assert isinstance(instance.BindPrincipal, str)


@given(instance=connection::LDAPSchemaConnection_strategy)
def test_connection::ldapschemaconnection_BindPrincipal_setter(instance):
    original = instance.BindPrincipal
    instance.BindPrincipal = original
    assert instance.BindPrincipal == original

@given(instance=connection::LDAPSchemaConnection_strategy)
def test_connection::ldapschemaconnection_CountLimit_type(instance):
    assert isinstance(instance.CountLimit, str)


@given(instance=connection::LDAPSchemaConnection_strategy)
def test_connection::ldapschemaconnection_CountLimit_setter(instance):
    original = instance.CountLimit
    instance.CountLimit = original
    assert instance.CountLimit == original

@given(instance=connection::LDAPSchemaConnection_strategy)
def test_connection::ldapschemaconnection_Filter_type(instance):
    assert isinstance(instance.Filter, str)


@given(instance=connection::LDAPSchemaConnection_strategy)
def test_connection::ldapschemaconnection_Filter_setter(instance):
    original = instance.Filter
    instance.Filter = original
    assert instance.Filter == original

@given(instance=connection::LDAPSchemaConnection_strategy)
def test_connection::ldapschemaconnection_LimitValue_type(instance):
    assert isinstance(instance.LimitValue, int)


@given(instance=connection::LDAPSchemaConnection_strategy)
def test_connection::ldapschemaconnection_LimitValue_setter(instance):
    original = instance.LimitValue
    instance.LimitValue = original
    assert instance.LimitValue == original

@given(instance=connection::LDAPSchemaConnection_strategy)
def test_connection::ldapschemaconnection_SavePassword_type(instance):
    assert isinstance(instance.SavePassword, bool)


@given(instance=connection::LDAPSchemaConnection_strategy)
def test_connection::ldapschemaconnection_SavePassword_setter(instance):
    original = instance.SavePassword
    instance.SavePassword = original
    assert instance.SavePassword == original

@given(instance=connection::LDAPSchemaConnection_strategy)
def test_connection::ldapschemaconnection_UseLimit_type(instance):
    assert isinstance(instance.UseLimit, bool)


@given(instance=connection::LDAPSchemaConnection_strategy)
def test_connection::ldapschemaconnection_UseLimit_setter(instance):
    original = instance.UseLimit
    instance.UseLimit = original
    assert instance.UseLimit == original

@given(instance=connection::LDAPSchemaConnection_strategy)
def test_connection::ldapschemaconnection_UseAdvanced_type(instance):
    assert isinstance(instance.UseAdvanced, bool)


@given(instance=connection::LDAPSchemaConnection_strategy)
def test_connection::ldapschemaconnection_UseAdvanced_setter(instance):
    original = instance.UseAdvanced
    instance.UseAdvanced = original
    assert instance.UseAdvanced == original

@given(instance=connection::LDAPSchemaConnection_strategy)
def test_connection::ldapschemaconnection_Protocol_type(instance):
    assert isinstance(instance.Protocol, str)


@given(instance=connection::LDAPSchemaConnection_strategy)
def test_connection::ldapschemaconnection_Protocol_setter(instance):
    original = instance.Protocol
    instance.Protocol = original
    assert instance.Protocol == original

@given(instance=connection::LDAPSchemaConnection_strategy)
def test_connection::ldapschemaconnection_EncryptionMethodName_type(instance):
    assert isinstance(instance.EncryptionMethodName, str)


@given(instance=connection::LDAPSchemaConnection_strategy)
def test_connection::ldapschemaconnection_EncryptionMethodName_setter(instance):
    original = instance.EncryptionMethodName
    instance.EncryptionMethodName = original
    assert instance.EncryptionMethodName == original

@given(instance=connection::LDAPSchemaConnection_strategy)
def test_connection::ldapschemaconnection_BindPassword_type(instance):
    assert isinstance(instance.BindPassword, str)


@given(instance=connection::LDAPSchemaConnection_strategy)
def test_connection::ldapschemaconnection_BindPassword_setter(instance):
    original = instance.BindPassword
    instance.BindPassword = original
    assert instance.BindPassword == original

@given(instance=connection::LDAPSchemaConnection_strategy)
def test_connection::ldapschemaconnection_Port_type(instance):
    assert isinstance(instance.Port, str)


@given(instance=connection::LDAPSchemaConnection_strategy)
def test_connection::ldapschemaconnection_Port_setter(instance):
    original = instance.Port
    instance.Port = original
    assert instance.Port == original

@given(instance=connection::LDAPSchemaConnection_strategy)
def test_connection::ldapschemaconnection_Separator_type(instance):
    assert isinstance(instance.Separator, str)


@given(instance=connection::LDAPSchemaConnection_strategy)
def test_connection::ldapschemaconnection_Separator_setter(instance):
    original = instance.Separator
    instance.Separator = original
    assert instance.Separator == original

@given(instance=connection::LDAPSchemaConnection_strategy)
def test_connection::ldapschemaconnection_BaseDNs_type(instance):
    assert isinstance(instance.BaseDNs, str)


@given(instance=connection::LDAPSchemaConnection_strategy)
def test_connection::ldapschemaconnection_BaseDNs_setter(instance):
    original = instance.BaseDNs
    instance.BaseDNs = original
    assert instance.BaseDNs == original

@given(instance=connection::LDAPSchemaConnection_strategy)
def test_connection::ldapschemaconnection_StorePath_type(instance):
    assert isinstance(instance.StorePath, str)


@given(instance=connection::LDAPSchemaConnection_strategy)
def test_connection::ldapschemaconnection_StorePath_setter(instance):
    original = instance.StorePath
    instance.StorePath = original
    assert instance.StorePath == original

@given(instance=connection::LDAPSchemaConnection_strategy)
def test_connection::ldapschemaconnection_Value_type(instance):
    assert isinstance(instance.Value, str)


@given(instance=connection::LDAPSchemaConnection_strategy)
def test_connection::ldapschemaconnection_Value_setter(instance):
    original = instance.Value
    instance.Value = original
    assert instance.Value == original

@given(instance=connection::LDAPSchemaConnection_strategy)
def test_connection::ldapschemaconnection_Referrals_type(instance):
    assert isinstance(instance.Referrals, str)


@given(instance=connection::LDAPSchemaConnection_strategy)
def test_connection::ldapschemaconnection_Referrals_setter(instance):
    original = instance.Referrals
    instance.Referrals = original
    assert instance.Referrals == original

@given(instance=connection::LDAPSchemaConnection_strategy)
def test_connection::ldapschemaconnection_ReturnAttributes_type(instance):
    assert isinstance(instance.ReturnAttributes, str)


@given(instance=connection::LDAPSchemaConnection_strategy)
def test_connection::ldapschemaconnection_ReturnAttributes_setter(instance):
    original = instance.ReturnAttributes
    instance.ReturnAttributes = original
    assert instance.ReturnAttributes == original

@given(instance=connection::LDAPSchemaConnection_strategy)
def test_connection::ldapschemaconnection_Host_type(instance):
    assert isinstance(instance.Host, str)


@given(instance=connection::LDAPSchemaConnection_strategy)
def test_connection::ldapschemaconnection_Host_setter(instance):
    original = instance.Host
    instance.Host = original
    assert instance.Host == original

@given(instance=connection::LDAPSchemaConnection_strategy)
def test_connection::ldapschemaconnection_Aliases_type(instance):
    assert isinstance(instance.Aliases, str)


@given(instance=connection::LDAPSchemaConnection_strategy)
def test_connection::ldapschemaconnection_Aliases_setter(instance):
    original = instance.Aliases
    instance.Aliases = original
    assert instance.Aliases == original

@given(instance=connection::LDAPSchemaConnection_strategy)
def test_connection::ldapschemaconnection_UseAuthen_type(instance):
    assert isinstance(instance.UseAuthen, bool)


@given(instance=connection::LDAPSchemaConnection_strategy)
def test_connection::ldapschemaconnection_UseAuthen_setter(instance):
    original = instance.UseAuthen
    instance.UseAuthen = original
    assert instance.UseAuthen == original

@given(instance=connection::LDAPSchemaConnection_strategy)
def test_connection::ldapschemaconnection_SelectedDN_type(instance):
    assert isinstance(instance.SelectedDN, str)


@given(instance=connection::LDAPSchemaConnection_strategy)
def test_connection::ldapschemaconnection_SelectedDN_setter(instance):
    original = instance.SelectedDN
    instance.SelectedDN = original
    assert instance.SelectedDN == original

@given(instance=connection::LDAPSchemaConnection_strategy)
def test_connection::ldapschemaconnection_TimeOutLimit_type(instance):
    assert isinstance(instance.TimeOutLimit, str)


@given(instance=connection::LDAPSchemaConnection_strategy)
def test_connection::ldapschemaconnection_TimeOutLimit_setter(instance):
    original = instance.TimeOutLimit
    instance.TimeOutLimit = original
    assert instance.TimeOutLimit == original

@given(instance=connection::FileConnection_strategy)
@settings(max_examples=50)
def test_connection::fileconnection_instantiation(instance):
    assert isinstance(instance, connection::FileConnection)

@given(instance=connection::FileConnection_strategy)
def test_connection::fileconnection_EscapeChar_type(instance):
    assert isinstance(instance.EscapeChar, str)


@given(instance=connection::FileConnection_strategy)
def test_connection::fileconnection_EscapeChar_setter(instance):
    original = instance.EscapeChar
    instance.EscapeChar = original
    assert instance.EscapeChar == original

@given(instance=connection::FileConnection_strategy)
def test_connection::fileconnection_RowSeparatorType_type(instance):
    assert isinstance(instance.RowSeparatorType, str)


@given(instance=connection::FileConnection_strategy)
def test_connection::fileconnection_RowSeparatorType_setter(instance):
    original = instance.RowSeparatorType
    instance.RowSeparatorType = original
    assert instance.RowSeparatorType == original

@given(instance=connection::FileConnection_strategy)
def test_connection::fileconnection_RowSeparatorValue_type(instance):
    assert isinstance(instance.RowSeparatorValue, str)


@given(instance=connection::FileConnection_strategy)
def test_connection::fileconnection_RowSeparatorValue_setter(instance):
    original = instance.RowSeparatorValue
    instance.RowSeparatorValue = original
    assert instance.RowSeparatorValue == original

@given(instance=connection::FileConnection_strategy)
def test_connection::fileconnection_CsvOption_type(instance):
    assert isinstance(instance.CsvOption, bool)


@given(instance=connection::FileConnection_strategy)
def test_connection::fileconnection_CsvOption_setter(instance):
    original = instance.CsvOption
    instance.CsvOption = original
    assert instance.CsvOption == original

@given(instance=connection::FileConnection_strategy)
def test_connection::fileconnection_FirstLineCaption_type(instance):
    assert isinstance(instance.FirstLineCaption, bool)


@given(instance=connection::FileConnection_strategy)
def test_connection::fileconnection_FirstLineCaption_setter(instance):
    original = instance.FirstLineCaption
    instance.FirstLineCaption = original
    assert instance.FirstLineCaption == original

@given(instance=connection::FileConnection_strategy)
def test_connection::fileconnection_RemoveEmptyRow_type(instance):
    assert isinstance(instance.RemoveEmptyRow, bool)


@given(instance=connection::FileConnection_strategy)
def test_connection::fileconnection_RemoveEmptyRow_setter(instance):
    original = instance.RemoveEmptyRow
    instance.RemoveEmptyRow = original
    assert instance.RemoveEmptyRow == original

@given(instance=connection::FileConnection_strategy)
def test_connection::fileconnection_Format_type(instance):
    assert isinstance(instance.Format, str)


@given(instance=connection::FileConnection_strategy)
def test_connection::fileconnection_Format_setter(instance):
    original = instance.Format
    instance.Format = original
    assert instance.Format == original

@given(instance=connection::FileConnection_strategy)
def test_connection::fileconnection_LimitValue_type(instance):
    assert isinstance(instance.LimitValue, str)


@given(instance=connection::FileConnection_strategy)
def test_connection::fileconnection_LimitValue_setter(instance):
    original = instance.LimitValue
    instance.LimitValue = original
    assert instance.LimitValue == original

@given(instance=connection::FileConnection_strategy)
def test_connection::fileconnection_UseFooter_type(instance):
    assert isinstance(instance.UseFooter, bool)


@given(instance=connection::FileConnection_strategy)
def test_connection::fileconnection_UseFooter_setter(instance):
    original = instance.UseFooter
    instance.UseFooter = original
    assert instance.UseFooter == original

@given(instance=connection::FileConnection_strategy)
def test_connection::fileconnection_TextIdentifier_type(instance):
    assert isinstance(instance.TextIdentifier, str)


@given(instance=connection::FileConnection_strategy)
def test_connection::fileconnection_TextIdentifier_setter(instance):
    original = instance.TextIdentifier
    instance.TextIdentifier = original
    assert instance.TextIdentifier == original

@given(instance=connection::FileConnection_strategy)
def test_connection::fileconnection_UseLimit_type(instance):
    assert isinstance(instance.UseLimit, bool)


@given(instance=connection::FileConnection_strategy)
def test_connection::fileconnection_UseLimit_setter(instance):
    original = instance.UseLimit
    instance.UseLimit = original
    assert instance.UseLimit == original

@given(instance=connection::FileConnection_strategy)
def test_connection::fileconnection_HeaderValue_type(instance):
    assert isinstance(instance.HeaderValue, str)


@given(instance=connection::FileConnection_strategy)
def test_connection::fileconnection_HeaderValue_setter(instance):
    original = instance.HeaderValue
    instance.HeaderValue = original
    assert instance.HeaderValue == original

@given(instance=connection::FileConnection_strategy)
def test_connection::fileconnection_FooterValue_type(instance):
    assert isinstance(instance.FooterValue, str)


@given(instance=connection::FileConnection_strategy)
def test_connection::fileconnection_FooterValue_setter(instance):
    original = instance.FooterValue
    instance.FooterValue = original
    assert instance.FooterValue == original

@given(instance=connection::FileConnection_strategy)
def test_connection::fileconnection_Server_type(instance):
    assert isinstance(instance.Server, str)


@given(instance=connection::FileConnection_strategy)
def test_connection::fileconnection_Server_setter(instance):
    original = instance.Server
    instance.Server = original
    assert instance.Server == original

@given(instance=connection::FileConnection_strategy)
def test_connection::fileconnection_UseHeader_type(instance):
    assert isinstance(instance.UseHeader, bool)


@given(instance=connection::FileConnection_strategy)
def test_connection::fileconnection_UseHeader_setter(instance):
    original = instance.UseHeader
    instance.UseHeader = original
    assert instance.UseHeader == original

@given(instance=connection::FileConnection_strategy)
def test_connection::fileconnection_TextEnclosure_type(instance):
    assert isinstance(instance.TextEnclosure, str)


@given(instance=connection::FileConnection_strategy)
def test_connection::fileconnection_TextEnclosure_setter(instance):
    original = instance.TextEnclosure
    instance.TextEnclosure = original
    assert instance.TextEnclosure == original

@given(instance=connection::FileConnection_strategy)
def test_connection::fileconnection_Encoding_type(instance):
    assert isinstance(instance.Encoding, str)


@given(instance=connection::FileConnection_strategy)
def test_connection::fileconnection_Encoding_setter(instance):
    original = instance.Encoding
    instance.Encoding = original
    assert instance.Encoding == original

@given(instance=connection::FileConnection_strategy)
def test_connection::fileconnection_FieldSeparatorValue_type(instance):
    assert isinstance(instance.FieldSeparatorValue, str)


@given(instance=connection::FileConnection_strategy)
def test_connection::fileconnection_FieldSeparatorValue_setter(instance):
    original = instance.FieldSeparatorValue
    instance.FieldSeparatorValue = original
    assert instance.FieldSeparatorValue == original

@given(instance=connection::FileConnection_strategy)
def test_connection::fileconnection_EscapeType_type(instance):
    assert isinstance(instance.EscapeType, str)


@given(instance=connection::FileConnection_strategy)
def test_connection::fileconnection_EscapeType_setter(instance):
    original = instance.EscapeType
    instance.EscapeType = original
    assert instance.EscapeType == original

@given(instance=connection::FileConnection_strategy)
def test_connection::fileconnection_FilePath_type(instance):
    assert isinstance(instance.FilePath, str)


@given(instance=connection::FileConnection_strategy)
def test_connection::fileconnection_FilePath_setter(instance):
    original = instance.FilePath
    instance.FilePath = original
    assert instance.FilePath == original

@given(instance=connection::AbstractMetadataObject_strategy)
@settings(max_examples=50)
def test_connection::abstractmetadataobject_instantiation(instance):
    assert isinstance(instance, connection::AbstractMetadataObject)

@given(instance=connection::AbstractMetadataObject_strategy)
def test_connection::abstractmetadataobject_properties_type(instance):
    assert isinstance(instance.properties, str)


@given(instance=connection::AbstractMetadataObject_strategy)
def test_connection::abstractmetadataobject_properties_setter(instance):
    original = instance.properties
    instance.properties = original
    assert instance.properties == original

@given(instance=connection::AbstractMetadataObject_strategy)
def test_connection::abstractmetadataobject_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=connection::AbstractMetadataObject_strategy)
def test_connection::abstractmetadataobject_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=connection::AbstractMetadataObject_strategy)
def test_connection::abstractmetadataobject_divergency_type(instance):
    assert isinstance(instance.divergency, bool)


@given(instance=connection::AbstractMetadataObject_strategy)
def test_connection::abstractmetadataobject_divergency_setter(instance):
    original = instance.divergency
    instance.divergency = original
    assert instance.divergency == original

@given(instance=connection::AbstractMetadataObject_strategy)
def test_connection::abstractmetadataobject_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=connection::AbstractMetadataObject_strategy)
def test_connection::abstractmetadataobject_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=connection::AbstractMetadataObject_strategy)
def test_connection::abstractmetadataobject_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=connection::AbstractMetadataObject_strategy)
def test_connection::abstractmetadataobject_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=connection::AbstractMetadataObject_strategy)
def test_connection::abstractmetadataobject_synchronised_type(instance):
    assert isinstance(instance.synchronised, bool)


@given(instance=connection::AbstractMetadataObject_strategy)
def test_connection::abstractmetadataobject_synchronised_setter(instance):
    original = instance.synchronised
    instance.synchronised = original
    assert instance.synchronised == original

@given(instance=connection::AbstractMetadataObject_strategy)
def test_connection::abstractmetadataobject_readOnly_type(instance):
    assert isinstance(instance.readOnly, bool)


@given(instance=connection::AbstractMetadataObject_strategy)
def test_connection::abstractmetadataobject_readOnly_setter(instance):
    original = instance.readOnly
    instance.readOnly = original
    assert instance.readOnly == original

@given(instance=AbstractMetadataObject_strategy)
@settings(max_examples=50)
def test_abstractmetadataobject_instantiation(instance):
    assert isinstance(instance, AbstractMetadataObject)

@given(instance=connection::SAPFunctionUnit_strategy)
@settings(max_examples=50)
def test_connection::sapfunctionunit_instantiation(instance):
    assert isinstance(instance, connection::SAPFunctionUnit)

@given(instance=connection::SAPFunctionUnit_strategy)
def test_connection::sapfunctionunit_Document_type(instance):
    assert isinstance(instance.Document, str)


@given(instance=connection::SAPFunctionUnit_strategy)
def test_connection::sapfunctionunit_Document_setter(instance):
    original = instance.Document
    instance.Document = original
    assert instance.Document == original

@given(instance=connection::SAPFunctionUnit_strategy)
def test_connection::sapfunctionunit_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=connection::SAPFunctionUnit_strategy)
def test_connection::sapfunctionunit_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=connection::SAPFunctionUnit_strategy)
def test_connection::sapfunctionunit_OutputTableName_type(instance):
    assert isinstance(instance.OutputTableName, str)


@given(instance=connection::SAPFunctionUnit_strategy)
def test_connection::sapfunctionunit_OutputTableName_setter(instance):
    original = instance.OutputTableName
    instance.OutputTableName = original
    assert instance.OutputTableName == original

@given(instance=connection::SAPFunctionUnit_strategy)
def test_connection::sapfunctionunit_OutputType_type(instance):
    assert isinstance(instance.OutputType, str)


@given(instance=connection::SAPFunctionUnit_strategy)
def test_connection::sapfunctionunit_OutputType_setter(instance):
    original = instance.OutputType
    instance.OutputType = original
    assert instance.OutputType == original

@given(instance=connection::Query_strategy)
@settings(max_examples=50)
def test_connection::query_instantiation(instance):
    assert isinstance(instance, connection::Query)

@given(instance=connection::Query_strategy)
def test_connection::query_contextMode_type(instance):
    assert isinstance(instance.contextMode, bool)


@given(instance=connection::Query_strategy)
def test_connection::query_contextMode_setter(instance):
    original = instance.contextMode
    instance.contextMode = original
    assert instance.contextMode == original

@given(instance=connection::Query_strategy)
def test_connection::query_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=connection::Query_strategy)
def test_connection::query_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=connection::SAPFunctionParameterColumn_strategy)
@settings(max_examples=50)
def test_connection::sapfunctionparametercolumn_instantiation(instance):
    assert isinstance(instance, connection::SAPFunctionParameterColumn)

@given(instance=connection::SAPFunctionParameterColumn_strategy)
def test_connection::sapfunctionparametercolumn_Length_type(instance):
    assert isinstance(instance.Length, str)


@given(instance=connection::SAPFunctionParameterColumn_strategy)
def test_connection::sapfunctionparametercolumn_Length_setter(instance):
    original = instance.Length
    instance.Length = original
    assert instance.Length == original

@given(instance=connection::SAPFunctionParameterColumn_strategy)
def test_connection::sapfunctionparametercolumn_DataType_type(instance):
    assert isinstance(instance.DataType, str)


@given(instance=connection::SAPFunctionParameterColumn_strategy)
def test_connection::sapfunctionparametercolumn_DataType_setter(instance):
    original = instance.DataType
    instance.DataType = original
    assert instance.DataType == original

@given(instance=connection::SAPFunctionParameterColumn_strategy)
def test_connection::sapfunctionparametercolumn_StructureOrTableName_type(instance):
    assert isinstance(instance.StructureOrTableName, str)


@given(instance=connection::SAPFunctionParameterColumn_strategy)
def test_connection::sapfunctionparametercolumn_StructureOrTableName_setter(instance):
    original = instance.StructureOrTableName
    instance.StructureOrTableName = original
    assert instance.StructureOrTableName == original

@given(instance=connection::SAPFunctionParameterColumn_strategy)
def test_connection::sapfunctionparametercolumn_Value_type(instance):
    assert isinstance(instance.Value, str)


@given(instance=connection::SAPFunctionParameterColumn_strategy)
def test_connection::sapfunctionparametercolumn_Value_setter(instance):
    original = instance.Value
    instance.Value = original
    assert instance.Value == original

@given(instance=connection::SAPFunctionParameterColumn_strategy)
def test_connection::sapfunctionparametercolumn_ParameterType_type(instance):
    assert isinstance(instance.ParameterType, str)


@given(instance=connection::SAPFunctionParameterColumn_strategy)
def test_connection::sapfunctionparametercolumn_ParameterType_setter(instance):
    original = instance.ParameterType
    instance.ParameterType = original
    assert instance.ParameterType == original

@given(instance=connection::SAPFunctionParameterColumn_strategy)
def test_connection::sapfunctionparametercolumn_Description_type(instance):
    assert isinstance(instance.Description, str)


@given(instance=connection::SAPFunctionParameterColumn_strategy)
def test_connection::sapfunctionparametercolumn_Description_setter(instance):
    original = instance.Description
    instance.Description = original
    assert instance.Description == original

@given(instance=connection::SAPFunctionParameterColumn_strategy)
def test_connection::sapfunctionparametercolumn_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=connection::SAPFunctionParameterColumn_strategy)
def test_connection::sapfunctionparametercolumn_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=connection::CDCType_strategy)
@settings(max_examples=50)
def test_connection::cdctype_instantiation(instance):
    assert isinstance(instance, connection::CDCType)

@given(instance=connection::CDCType_strategy)
def test_connection::cdctype_journalName_type(instance):
    assert isinstance(instance.journalName, str)


@given(instance=connection::CDCType_strategy)
def test_connection::cdctype_journalName_setter(instance):
    original = instance.journalName
    instance.journalName = original
    assert instance.journalName == original

@given(instance=connection::CDCType_strategy)
def test_connection::cdctype_linkDB_type(instance):
    assert isinstance(instance.linkDB, str)


@given(instance=connection::CDCType_strategy)
def test_connection::cdctype_linkDB_setter(instance):
    original = instance.linkDB
    instance.linkDB = original
    assert instance.linkDB == original

@given(instance=connection::SAPFunctionParameterTable_strategy)
@settings(max_examples=50)
def test_connection::sapfunctionparametertable_instantiation(instance):
    assert isinstance(instance, connection::SAPFunctionParameterTable)

@given(instance=connection::Metadata_strategy)
@settings(max_examples=50)
def test_connection::metadata_instantiation(instance):
    assert isinstance(instance, connection::Metadata)

@given(instance=connection::MetadataColumn_strategy)
@settings(max_examples=50)
def test_connection::metadatacolumn_instantiation(instance):
    assert isinstance(instance, connection::MetadataColumn)

@given(instance=connection::MetadataColumn_strategy)
def test_connection::metadatacolumn_defaultValue_type(instance):
    assert isinstance(instance.defaultValue, str)


@given(instance=connection::MetadataColumn_strategy)
def test_connection::metadatacolumn_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original

@given(instance=connection::MetadataColumn_strategy)
def test_connection::metadatacolumn_sourceType_type(instance):
    assert isinstance(instance.sourceType, str)


@given(instance=connection::MetadataColumn_strategy)
def test_connection::metadatacolumn_sourceType_setter(instance):
    original = instance.sourceType
    instance.sourceType = original
    assert instance.sourceType == original

@given(instance=connection::MetadataColumn_strategy)
def test_connection::metadatacolumn_pattern_type(instance):
    assert isinstance(instance.pattern, str)


@given(instance=connection::MetadataColumn_strategy)
def test_connection::metadatacolumn_pattern_setter(instance):
    original = instance.pattern
    instance.pattern = original
    assert instance.pattern == original

@given(instance=connection::MetadataColumn_strategy)
def test_connection::metadatacolumn_displayField_type(instance):
    assert isinstance(instance.displayField, str)


@given(instance=connection::MetadataColumn_strategy)
def test_connection::metadatacolumn_displayField_setter(instance):
    original = instance.displayField
    instance.displayField = original
    assert instance.displayField == original

@given(instance=connection::MetadataColumn_strategy)
def test_connection::metadatacolumn_originalField_type(instance):
    assert isinstance(instance.originalField, str)


@given(instance=connection::MetadataColumn_strategy)
def test_connection::metadatacolumn_originalField_setter(instance):
    original = instance.originalField
    instance.originalField = original
    assert instance.originalField == original

@given(instance=connection::MetadataColumn_strategy)
def test_connection::metadatacolumn_talendType_type(instance):
    assert isinstance(instance.talendType, str)


@given(instance=connection::MetadataColumn_strategy)
def test_connection::metadatacolumn_talendType_setter(instance):
    original = instance.talendType
    instance.talendType = original
    assert instance.talendType == original

@given(instance=connection::MetadataColumn_strategy)
def test_connection::metadatacolumn_key_type(instance):
    assert isinstance(instance.key, bool)


@given(instance=connection::MetadataColumn_strategy)
def test_connection::metadatacolumn_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=connection::MetadataColumn_strategy)
def test_connection::metadatacolumn_nullable_type(instance):
    assert isinstance(instance.nullable, bool)


@given(instance=connection::MetadataColumn_strategy)
def test_connection::metadatacolumn_nullable_setter(instance):
    original = instance.nullable
    instance.nullable = original
    assert instance.nullable == original

@given(instance=connection::MetadataColumn_strategy)
def test_connection::metadatacolumn_precision_type(instance):
    assert isinstance(instance.precision, str)


@given(instance=connection::MetadataColumn_strategy)
def test_connection::metadatacolumn_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=connection::MetadataColumn_strategy)
def test_connection::metadatacolumn_length_type(instance):
    assert isinstance(instance.length, str)


@given(instance=connection::MetadataColumn_strategy)
def test_connection::metadatacolumn_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=connection::QueriesConnection_strategy)
@settings(max_examples=50)
def test_connection::queriesconnection_instantiation(instance):
    assert isinstance(instance, connection::QueriesConnection)

@given(instance=connection::MetadataTable_strategy)
@settings(max_examples=50)
def test_connection::metadatatable_instantiation(instance):
    assert isinstance(instance, connection::MetadataTable)

@given(instance=connection::MetadataTable_strategy)
def test_connection::metadatatable_attachedCDC_type(instance):
    assert isinstance(instance.attachedCDC, bool)


@given(instance=connection::MetadataTable_strategy)
def test_connection::metadatatable_attachedCDC_setter(instance):
    original = instance.attachedCDC
    instance.attachedCDC = original
    assert instance.attachedCDC == original

@given(instance=connection::MetadataTable_strategy)
def test_connection::metadatatable_activatedCDC_type(instance):
    assert isinstance(instance.activatedCDC, bool)


@given(instance=connection::MetadataTable_strategy)
def test_connection::metadatatable_activatedCDC_setter(instance):
    original = instance.activatedCDC
    instance.activatedCDC = original
    assert instance.activatedCDC == original

@given(instance=connection::MetadataTable_strategy)
def test_connection::metadatatable_tableType_type(instance):
    assert isinstance(instance.tableType, str)


@given(instance=connection::MetadataTable_strategy)
def test_connection::metadatatable_tableType_setter(instance):
    original = instance.tableType
    instance.tableType = original
    assert instance.tableType == original

@given(instance=connection::MetadataTable_strategy)
def test_connection::metadatatable_sourceName_type(instance):
    assert isinstance(instance.sourceName, str)


@given(instance=connection::MetadataTable_strategy)
def test_connection::metadatatable_sourceName_setter(instance):
    original = instance.sourceName
    instance.sourceName = original
    assert instance.sourceName == original

@given(instance=connection::Connection_strategy)
@settings(max_examples=50)
def test_connection::connection_instantiation(instance):
    assert isinstance(instance, connection::Connection)

@given(instance=connection::Connection_strategy)
def test_connection::connection_ContextId_type(instance):
    assert isinstance(instance.ContextId, str)


@given(instance=connection::Connection_strategy)
def test_connection::connection_ContextId_setter(instance):
    original = instance.ContextId
    instance.ContextId = original
    assert instance.ContextId == original

@given(instance=connection::Connection_strategy)
def test_connection::connection_ContextMode_type(instance):
    assert isinstance(instance.ContextMode, bool)


@given(instance=connection::Connection_strategy)
def test_connection::connection_ContextMode_setter(instance):
    original = instance.ContextMode
    instance.ContextMode = original
    assert instance.ContextMode == original

@given(instance=connection::Connection_strategy)
def test_connection::connection_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=connection::Connection_strategy)
def test_connection::connection_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original
