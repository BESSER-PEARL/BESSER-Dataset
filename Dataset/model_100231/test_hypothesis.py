import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    SpreadsheetMLWorkbookProp_Worksheet,
    Worksheet,
    SpreadsheetMLWorkbookProp_SmartTagsCollection,
    SmartTagsCollection,
    SpreadsheetMLWorkbookProp_SmartTagType,
    CustomDocumentPropertiesCollection,
    Cell,
    SpreadsheetMLWorkbookProp_CustomDocumentPropertiesCollection,
    SpreadsheetMLWorkbookProp_CustomDocumentProperty,
    CustomDocumentProperty,
    VersionType,
    Workbook,
    SpreadsheetMLWorkbookProp_DocumentPropertiesCollection,
    DateTimeType,
    ValueType,
    SpreadsheetMLWorkbookProp_ErrorValue,
    SpreadsheetMLWorkbookProp_NumberValue,
    SpreadsheetMLWorkbookProp_DateTimeTypeValue,
    SpreadsheetMLWorkbookProp_BooleanValue,
    SpreadsheetMLWorkbookProp_StringValue,
    Data,
    SpreadsheetMLWorkbookProp_ValueType,
    SpreadsheetMLWorkbookProp_VersionType,
    SpreadsheetMLWorkbookProp_DateTimeType,
    SpreadsheetMLWorkbookProp_ExcelWorkbook,
    SpreadsheetMLWorkbookProp_Comment,
    Comment,
    SpreadsheetMLWorkbookProp_Data,
    TableElement,
    SpreadsheetMLWorkbookProp_Cell,
    SpreadsheetMLWorkbookProp_ColOrRowElement,
    ColOrRowElement,
    SpreadsheetMLWorkbookProp_Row,
    SpreadsheetMLWorkbookProp_Column,
    Column,
    StyledElement,
    SpreadsheetMLWorkbookProp_TableElement,
    SpreadsheetMLWorkbookProp_Table,
    SpreadsheetMLWorkbookProp_StyledElement,
    Table,
    Row,
    ExcelWorkbook,
    DocumentPropertiesCollection,
    SpreadsheetMLWorkbookProp_Workbook,
    SmartTagType,
    DisplayDrawingObjectsType,
    CalculationWorkbookType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_spreadsheetmlworkbookprop_worksheet_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorkbookProp_Worksheet)


def test_spreadsheetmlworkbookprop_worksheet_constructor_exists():
    assert callable(SpreadsheetMLWorkbookProp_Worksheet.__init__)


def test_spreadsheetmlworkbookprop_worksheet_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorkbookProp_Worksheet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_spreadsheetmlworkbookprop_worksheet_has_name():
    assert hasattr(SpreadsheetMLWorkbookProp_Worksheet, "name")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_Worksheet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_worksheet_is_not_abstract():
    assert not inspect.isabstract(Worksheet)


def test_worksheet_constructor_exists():
    assert callable(Worksheet.__init__)


def test_worksheet_constructor_args():
    sig = inspect.signature(Worksheet.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlworkbookprop_smarttagscollection_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorkbookProp_SmartTagsCollection)


def test_spreadsheetmlworkbookprop_smarttagscollection_constructor_exists():
    assert callable(SpreadsheetMLWorkbookProp_SmartTagsCollection.__init__)


def test_spreadsheetmlworkbookprop_smarttagscollection_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorkbookProp_SmartTagsCollection.__init__)
    params = list(sig.parameters.keys())



def test_smarttagscollection_is_not_abstract():
    assert not inspect.isabstract(SmartTagsCollection)


def test_smarttagscollection_constructor_exists():
    assert callable(SmartTagsCollection.__init__)


def test_smarttagscollection_constructor_args():
    sig = inspect.signature(SmartTagsCollection.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlworkbookprop_smarttagtype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorkbookProp_SmartTagType)


def test_spreadsheetmlworkbookprop_smarttagtype_constructor_exists():
    assert callable(SpreadsheetMLWorkbookProp_SmartTagType.__init__)


def test_spreadsheetmlworkbookprop_smarttagtype_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorkbookProp_SmartTagType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "url" in params, "Missing parameter 'url'"
    assert "namespaceuri" in params, "Missing parameter 'namespaceuri'"

def test_spreadsheetmlworkbookprop_smarttagtype_has_name():
    assert hasattr(SpreadsheetMLWorkbookProp_SmartTagType, "name")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_SmartTagType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_smarttagtype_has_url():
    assert hasattr(SpreadsheetMLWorkbookProp_SmartTagType, "url")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_SmartTagType.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_smarttagtype_has_namespaceuri():
    assert hasattr(SpreadsheetMLWorkbookProp_SmartTagType, "namespaceuri")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_SmartTagType.__mro__:
        if "namespaceuri" in klass.__dict__:
            descriptor = klass.__dict__["namespaceuri"]
            break
    assert isinstance(descriptor, property)



def test_customdocumentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(CustomDocumentPropertiesCollection)


def test_customdocumentpropertiescollection_constructor_exists():
    assert callable(CustomDocumentPropertiesCollection.__init__)


def test_customdocumentpropertiescollection_constructor_args():
    sig = inspect.signature(CustomDocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())



def test_cell_is_not_abstract():
    assert not inspect.isabstract(Cell)


def test_cell_constructor_exists():
    assert callable(Cell.__init__)


def test_cell_constructor_args():
    sig = inspect.signature(Cell.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlworkbookprop_customdocumentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorkbookProp_CustomDocumentPropertiesCollection)


def test_spreadsheetmlworkbookprop_customdocumentpropertiescollection_constructor_exists():
    assert callable(SpreadsheetMLWorkbookProp_CustomDocumentPropertiesCollection.__init__)


def test_spreadsheetmlworkbookprop_customdocumentpropertiescollection_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorkbookProp_CustomDocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlworkbookprop_customdocumentproperty_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorkbookProp_CustomDocumentProperty)


def test_spreadsheetmlworkbookprop_customdocumentproperty_constructor_exists():
    assert callable(SpreadsheetMLWorkbookProp_CustomDocumentProperty.__init__)


def test_spreadsheetmlworkbookprop_customdocumentproperty_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorkbookProp_CustomDocumentProperty.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_spreadsheetmlworkbookprop_customdocumentproperty_has_name():
    assert hasattr(SpreadsheetMLWorkbookProp_CustomDocumentProperty, "name")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_CustomDocumentProperty.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_customdocumentproperty_is_not_abstract():
    assert not inspect.isabstract(CustomDocumentProperty)


def test_customdocumentproperty_constructor_exists():
    assert callable(CustomDocumentProperty.__init__)


def test_customdocumentproperty_constructor_args():
    sig = inspect.signature(CustomDocumentProperty.__init__)
    params = list(sig.parameters.keys())



def test_versiontype_is_not_abstract():
    assert not inspect.isabstract(VersionType)


def test_versiontype_constructor_exists():
    assert callable(VersionType.__init__)


def test_versiontype_constructor_args():
    sig = inspect.signature(VersionType.__init__)
    params = list(sig.parameters.keys())



def test_workbook_is_not_abstract():
    assert not inspect.isabstract(Workbook)


def test_workbook_constructor_exists():
    assert callable(Workbook.__init__)


def test_workbook_constructor_args():
    sig = inspect.signature(Workbook.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlworkbookprop_documentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorkbookProp_DocumentPropertiesCollection)


def test_spreadsheetmlworkbookprop_documentpropertiescollection_constructor_exists():
    assert callable(SpreadsheetMLWorkbookProp_DocumentPropertiesCollection.__init__)


def test_spreadsheetmlworkbookprop_documentpropertiescollection_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorkbookProp_DocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())
    assert "lines" in params, "Missing parameter 'lines'"
    assert "bytes" in params, "Missing parameter 'bytes'"
    assert "appName" in params, "Missing parameter 'appName'"
    assert "paragraphs" in params, "Missing parameter 'paragraphs'"
    assert "lastAuthor" in params, "Missing parameter 'lastAuthor'"
    assert "guid" in params, "Missing parameter 'guid'"
    assert "title" in params, "Missing parameter 'title'"
    assert "manager" in params, "Missing parameter 'manager'"
    assert "subject" in params, "Missing parameter 'subject'"
    assert "characters" in params, "Missing parameter 'characters'"
    assert "author" in params, "Missing parameter 'author'"
    assert "presentationFormat" in params, "Missing parameter 'presentationFormat'"
    assert "pages" in params, "Missing parameter 'pages'"
    assert "charactersWithSpaces" in params, "Missing parameter 'charactersWithSpaces'"
    assert "keywords" in params, "Missing parameter 'keywords'"
    assert "totalTime" in params, "Missing parameter 'totalTime'"
    assert "company" in params, "Missing parameter 'company'"
    assert "description" in params, "Missing parameter 'description'"
    assert "words" in params, "Missing parameter 'words'"
    assert "hyperlinkBase" in params, "Missing parameter 'hyperlinkBase'"
    assert "category" in params, "Missing parameter 'category'"
    assert "revision" in params, "Missing parameter 'revision'"

def test_spreadsheetmlworkbookprop_documentpropertiescollection_has_lines():
    assert hasattr(SpreadsheetMLWorkbookProp_DocumentPropertiesCollection, "lines")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_DocumentPropertiesCollection.__mro__:
        if "lines" in klass.__dict__:
            descriptor = klass.__dict__["lines"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_documentpropertiescollection_has_bytes():
    assert hasattr(SpreadsheetMLWorkbookProp_DocumentPropertiesCollection, "bytes")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_DocumentPropertiesCollection.__mro__:
        if "bytes" in klass.__dict__:
            descriptor = klass.__dict__["bytes"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_documentpropertiescollection_has_appName():
    assert hasattr(SpreadsheetMLWorkbookProp_DocumentPropertiesCollection, "appName")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_DocumentPropertiesCollection.__mro__:
        if "appName" in klass.__dict__:
            descriptor = klass.__dict__["appName"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_documentpropertiescollection_has_paragraphs():
    assert hasattr(SpreadsheetMLWorkbookProp_DocumentPropertiesCollection, "paragraphs")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_DocumentPropertiesCollection.__mro__:
        if "paragraphs" in klass.__dict__:
            descriptor = klass.__dict__["paragraphs"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_documentpropertiescollection_has_lastAuthor():
    assert hasattr(SpreadsheetMLWorkbookProp_DocumentPropertiesCollection, "lastAuthor")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_DocumentPropertiesCollection.__mro__:
        if "lastAuthor" in klass.__dict__:
            descriptor = klass.__dict__["lastAuthor"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_documentpropertiescollection_has_guid():
    assert hasattr(SpreadsheetMLWorkbookProp_DocumentPropertiesCollection, "guid")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_DocumentPropertiesCollection.__mro__:
        if "guid" in klass.__dict__:
            descriptor = klass.__dict__["guid"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_documentpropertiescollection_has_title():
    assert hasattr(SpreadsheetMLWorkbookProp_DocumentPropertiesCollection, "title")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_DocumentPropertiesCollection.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_documentpropertiescollection_has_manager():
    assert hasattr(SpreadsheetMLWorkbookProp_DocumentPropertiesCollection, "manager")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_DocumentPropertiesCollection.__mro__:
        if "manager" in klass.__dict__:
            descriptor = klass.__dict__["manager"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_documentpropertiescollection_has_subject():
    assert hasattr(SpreadsheetMLWorkbookProp_DocumentPropertiesCollection, "subject")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_DocumentPropertiesCollection.__mro__:
        if "subject" in klass.__dict__:
            descriptor = klass.__dict__["subject"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_documentpropertiescollection_has_characters():
    assert hasattr(SpreadsheetMLWorkbookProp_DocumentPropertiesCollection, "characters")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_DocumentPropertiesCollection.__mro__:
        if "characters" in klass.__dict__:
            descriptor = klass.__dict__["characters"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_documentpropertiescollection_has_author():
    assert hasattr(SpreadsheetMLWorkbookProp_DocumentPropertiesCollection, "author")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_DocumentPropertiesCollection.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_documentpropertiescollection_has_presentationFormat():
    assert hasattr(SpreadsheetMLWorkbookProp_DocumentPropertiesCollection, "presentationFormat")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_DocumentPropertiesCollection.__mro__:
        if "presentationFormat" in klass.__dict__:
            descriptor = klass.__dict__["presentationFormat"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_documentpropertiescollection_has_pages():
    assert hasattr(SpreadsheetMLWorkbookProp_DocumentPropertiesCollection, "pages")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_DocumentPropertiesCollection.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_documentpropertiescollection_has_charactersWithSpaces():
    assert hasattr(SpreadsheetMLWorkbookProp_DocumentPropertiesCollection, "charactersWithSpaces")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_DocumentPropertiesCollection.__mro__:
        if "charactersWithSpaces" in klass.__dict__:
            descriptor = klass.__dict__["charactersWithSpaces"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_documentpropertiescollection_has_keywords():
    assert hasattr(SpreadsheetMLWorkbookProp_DocumentPropertiesCollection, "keywords")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_DocumentPropertiesCollection.__mro__:
        if "keywords" in klass.__dict__:
            descriptor = klass.__dict__["keywords"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_documentpropertiescollection_has_totalTime():
    assert hasattr(SpreadsheetMLWorkbookProp_DocumentPropertiesCollection, "totalTime")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_DocumentPropertiesCollection.__mro__:
        if "totalTime" in klass.__dict__:
            descriptor = klass.__dict__["totalTime"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_documentpropertiescollection_has_company():
    assert hasattr(SpreadsheetMLWorkbookProp_DocumentPropertiesCollection, "company")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_DocumentPropertiesCollection.__mro__:
        if "company" in klass.__dict__:
            descriptor = klass.__dict__["company"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_documentpropertiescollection_has_description():
    assert hasattr(SpreadsheetMLWorkbookProp_DocumentPropertiesCollection, "description")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_DocumentPropertiesCollection.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_documentpropertiescollection_has_words():
    assert hasattr(SpreadsheetMLWorkbookProp_DocumentPropertiesCollection, "words")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_DocumentPropertiesCollection.__mro__:
        if "words" in klass.__dict__:
            descriptor = klass.__dict__["words"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_documentpropertiescollection_has_hyperlinkBase():
    assert hasattr(SpreadsheetMLWorkbookProp_DocumentPropertiesCollection, "hyperlinkBase")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_DocumentPropertiesCollection.__mro__:
        if "hyperlinkBase" in klass.__dict__:
            descriptor = klass.__dict__["hyperlinkBase"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_documentpropertiescollection_has_category():
    assert hasattr(SpreadsheetMLWorkbookProp_DocumentPropertiesCollection, "category")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_DocumentPropertiesCollection.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_documentpropertiescollection_has_revision():
    assert hasattr(SpreadsheetMLWorkbookProp_DocumentPropertiesCollection, "revision")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_DocumentPropertiesCollection.__mro__:
        if "revision" in klass.__dict__:
            descriptor = klass.__dict__["revision"]
            break
    assert isinstance(descriptor, property)



def test_datetimetype_is_not_abstract():
    assert not inspect.isabstract(DateTimeType)


def test_datetimetype_constructor_exists():
    assert callable(DateTimeType.__init__)


def test_datetimetype_constructor_args():
    sig = inspect.signature(DateTimeType.__init__)
    params = list(sig.parameters.keys())



def test_valuetype_is_not_abstract():
    assert not inspect.isabstract(ValueType)


def test_valuetype_constructor_exists():
    assert callable(ValueType.__init__)


def test_valuetype_constructor_args():
    sig = inspect.signature(ValueType.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlworkbookprop_errorvalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorkbookProp_ErrorValue)


def test_spreadsheetmlworkbookprop_errorvalue_constructor_exists():
    assert callable(SpreadsheetMLWorkbookProp_ErrorValue.__init__)


def test_spreadsheetmlworkbookprop_errorvalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorkbookProp_ErrorValue.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlworkbookprop_numbervalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorkbookProp_NumberValue)


def test_spreadsheetmlworkbookprop_numbervalue_constructor_exists():
    assert callable(SpreadsheetMLWorkbookProp_NumberValue.__init__)


def test_spreadsheetmlworkbookprop_numbervalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorkbookProp_NumberValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_spreadsheetmlworkbookprop_numbervalue_has_value():
    assert hasattr(SpreadsheetMLWorkbookProp_NumberValue, "value")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_NumberValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlworkbookprop_datetimetypevalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorkbookProp_DateTimeTypeValue)


def test_spreadsheetmlworkbookprop_datetimetypevalue_constructor_exists():
    assert callable(SpreadsheetMLWorkbookProp_DateTimeTypeValue.__init__)


def test_spreadsheetmlworkbookprop_datetimetypevalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorkbookProp_DateTimeTypeValue.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlworkbookprop_booleanvalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorkbookProp_BooleanValue)


def test_spreadsheetmlworkbookprop_booleanvalue_constructor_exists():
    assert callable(SpreadsheetMLWorkbookProp_BooleanValue.__init__)


def test_spreadsheetmlworkbookprop_booleanvalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorkbookProp_BooleanValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_spreadsheetmlworkbookprop_booleanvalue_has_value():
    assert hasattr(SpreadsheetMLWorkbookProp_BooleanValue, "value")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_BooleanValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlworkbookprop_stringvalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorkbookProp_StringValue)


def test_spreadsheetmlworkbookprop_stringvalue_constructor_exists():
    assert callable(SpreadsheetMLWorkbookProp_StringValue.__init__)


def test_spreadsheetmlworkbookprop_stringvalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorkbookProp_StringValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_spreadsheetmlworkbookprop_stringvalue_has_value():
    assert hasattr(SpreadsheetMLWorkbookProp_StringValue, "value")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_StringValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_data_is_not_abstract():
    assert not inspect.isabstract(Data)


def test_data_constructor_exists():
    assert callable(Data.__init__)


def test_data_constructor_args():
    sig = inspect.signature(Data.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlworkbookprop_valuetype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorkbookProp_ValueType)


def test_spreadsheetmlworkbookprop_valuetype_constructor_exists():
    assert callable(SpreadsheetMLWorkbookProp_ValueType.__init__)


def test_spreadsheetmlworkbookprop_valuetype_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorkbookProp_ValueType.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlworkbookprop_versiontype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorkbookProp_VersionType)


def test_spreadsheetmlworkbookprop_versiontype_constructor_exists():
    assert callable(SpreadsheetMLWorkbookProp_VersionType.__init__)


def test_spreadsheetmlworkbookprop_versiontype_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorkbookProp_VersionType.__init__)
    params = list(sig.parameters.keys())
    assert "n" in params, "Missing parameter 'n'"
    assert "nn" in params, "Missing parameter 'nn'"

def test_spreadsheetmlworkbookprop_versiontype_has_n():
    assert hasattr(SpreadsheetMLWorkbookProp_VersionType, "n")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_VersionType.__mro__:
        if "n" in klass.__dict__:
            descriptor = klass.__dict__["n"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_versiontype_has_nn():
    assert hasattr(SpreadsheetMLWorkbookProp_VersionType, "nn")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_VersionType.__mro__:
        if "nn" in klass.__dict__:
            descriptor = klass.__dict__["nn"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlworkbookprop_datetimetype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorkbookProp_DateTimeType)


def test_spreadsheetmlworkbookprop_datetimetype_constructor_exists():
    assert callable(SpreadsheetMLWorkbookProp_DateTimeType.__init__)


def test_spreadsheetmlworkbookprop_datetimetype_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorkbookProp_DateTimeType.__init__)
    params = list(sig.parameters.keys())
    assert "year" in params, "Missing parameter 'year'"
    assert "month" in params, "Missing parameter 'month'"
    assert "day" in params, "Missing parameter 'day'"
    assert "minute" in params, "Missing parameter 'minute'"
    assert "hour" in params, "Missing parameter 'hour'"
    assert "second" in params, "Missing parameter 'second'"

def test_spreadsheetmlworkbookprop_datetimetype_has_year():
    assert hasattr(SpreadsheetMLWorkbookProp_DateTimeType, "year")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_DateTimeType.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_datetimetype_has_month():
    assert hasattr(SpreadsheetMLWorkbookProp_DateTimeType, "month")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_DateTimeType.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_datetimetype_has_day():
    assert hasattr(SpreadsheetMLWorkbookProp_DateTimeType, "day")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_DateTimeType.__mro__:
        if "day" in klass.__dict__:
            descriptor = klass.__dict__["day"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_datetimetype_has_minute():
    assert hasattr(SpreadsheetMLWorkbookProp_DateTimeType, "minute")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_DateTimeType.__mro__:
        if "minute" in klass.__dict__:
            descriptor = klass.__dict__["minute"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_datetimetype_has_hour():
    assert hasattr(SpreadsheetMLWorkbookProp_DateTimeType, "hour")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_DateTimeType.__mro__:
        if "hour" in klass.__dict__:
            descriptor = klass.__dict__["hour"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_datetimetype_has_second():
    assert hasattr(SpreadsheetMLWorkbookProp_DateTimeType, "second")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_DateTimeType.__mro__:
        if "second" in klass.__dict__:
            descriptor = klass.__dict__["second"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlworkbookprop_excelworkbook_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorkbookProp_ExcelWorkbook)


def test_spreadsheetmlworkbookprop_excelworkbook_constructor_exists():
    assert callable(SpreadsheetMLWorkbookProp_ExcelWorkbook.__init__)


def test_spreadsheetmlworkbookprop_excelworkbook_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorkbookProp_ExcelWorkbook.__init__)
    params = list(sig.parameters.keys())
    assert "protectWindows" in params, "Missing parameter 'protectWindows'"
    assert "firstVisibleSheet" in params, "Missing parameter 'firstVisibleSheet'"
    assert "doNotSaveLinkValues" in params, "Missing parameter 'doNotSaveLinkValues'"
    assert "windowWidth" in params, "Missing parameter 'windowWidth'"
    assert "maxIterations" in params, "Missing parameter 'maxIterations'"
    assert "uncalced" in params, "Missing parameter 'uncalced'"
    assert "hidePivotTableFieldList" in params, "Missing parameter 'hidePivotTableFieldList'"
    assert "hideHorizontalScrollBar" in params, "Missing parameter 'hideHorizontalScrollBar'"
    assert "windowTopX" in params, "Missing parameter 'windowTopX'"
    assert "displayDrawingObjects" in params, "Missing parameter 'displayDrawingObjects'"
    assert "selectedSheets" in params, "Missing parameter 'selectedSheets'"
    assert "noAutoRecover" in params, "Missing parameter 'noAutoRecover'"
    assert "maxChange" in params, "Missing parameter 'maxChange'"
    assert "precisionAsDisplayed" in params, "Missing parameter 'precisionAsDisplayed'"
    assert "displayInkNotes" in params, "Missing parameter 'displayInkNotes'"
    assert "hideVerticalScrollBar" in params, "Missing parameter 'hideVerticalScrollBar'"
    assert "hideWorkbookTabs" in params, "Missing parameter 'hideWorkbookTabs'"
    assert "protectStructure" in params, "Missing parameter 'protectStructure'"
    assert "createBackup" in params, "Missing parameter 'createBackup'"
    assert "windowHeight" in params, "Missing parameter 'windowHeight'"
    assert "acceptLabelsInFormulas" in params, "Missing parameter 'acceptLabelsInFormulas'"
    assert "embedSaveSmartTags" in params, "Missing parameter 'embedSaveSmartTags'"
    assert "activeSheet" in params, "Missing parameter 'activeSheet'"
    assert "date1904" in params, "Missing parameter 'date1904'"
    assert "calculation" in params, "Missing parameter 'calculation'"
    assert "windowTopY" in params, "Missing parameter 'windowTopY'"
    assert "futureVer" in params, "Missing parameter 'futureVer'"
    assert "activeChart" in params, "Missing parameter 'activeChart'"
    assert "tabRatio" in params, "Missing parameter 'tabRatio'"
    assert "windowIconic" in params, "Missing parameter 'windowIconic'"
    assert "doNotCalculateBeforeSave" in params, "Missing parameter 'doNotCalculateBeforeSave'"
    assert "iteration" in params, "Missing parameter 'iteration'"
    assert "windowHidden" in params, "Missing parameter 'windowHidden'"
    assert "refModeR1C1" in params, "Missing parameter 'refModeR1C1'"

def test_spreadsheetmlworkbookprop_excelworkbook_has_protectWindows():
    assert hasattr(SpreadsheetMLWorkbookProp_ExcelWorkbook, "protectWindows")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_ExcelWorkbook.__mro__:
        if "protectWindows" in klass.__dict__:
            descriptor = klass.__dict__["protectWindows"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_excelworkbook_has_firstVisibleSheet():
    assert hasattr(SpreadsheetMLWorkbookProp_ExcelWorkbook, "firstVisibleSheet")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_ExcelWorkbook.__mro__:
        if "firstVisibleSheet" in klass.__dict__:
            descriptor = klass.__dict__["firstVisibleSheet"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_excelworkbook_has_doNotSaveLinkValues():
    assert hasattr(SpreadsheetMLWorkbookProp_ExcelWorkbook, "doNotSaveLinkValues")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_ExcelWorkbook.__mro__:
        if "doNotSaveLinkValues" in klass.__dict__:
            descriptor = klass.__dict__["doNotSaveLinkValues"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_excelworkbook_has_windowWidth():
    assert hasattr(SpreadsheetMLWorkbookProp_ExcelWorkbook, "windowWidth")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_ExcelWorkbook.__mro__:
        if "windowWidth" in klass.__dict__:
            descriptor = klass.__dict__["windowWidth"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_excelworkbook_has_maxIterations():
    assert hasattr(SpreadsheetMLWorkbookProp_ExcelWorkbook, "maxIterations")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_ExcelWorkbook.__mro__:
        if "maxIterations" in klass.__dict__:
            descriptor = klass.__dict__["maxIterations"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_excelworkbook_has_uncalced():
    assert hasattr(SpreadsheetMLWorkbookProp_ExcelWorkbook, "uncalced")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_ExcelWorkbook.__mro__:
        if "uncalced" in klass.__dict__:
            descriptor = klass.__dict__["uncalced"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_excelworkbook_has_hidePivotTableFieldList():
    assert hasattr(SpreadsheetMLWorkbookProp_ExcelWorkbook, "hidePivotTableFieldList")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_ExcelWorkbook.__mro__:
        if "hidePivotTableFieldList" in klass.__dict__:
            descriptor = klass.__dict__["hidePivotTableFieldList"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_excelworkbook_has_hideHorizontalScrollBar():
    assert hasattr(SpreadsheetMLWorkbookProp_ExcelWorkbook, "hideHorizontalScrollBar")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_ExcelWorkbook.__mro__:
        if "hideHorizontalScrollBar" in klass.__dict__:
            descriptor = klass.__dict__["hideHorizontalScrollBar"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_excelworkbook_has_windowTopX():
    assert hasattr(SpreadsheetMLWorkbookProp_ExcelWorkbook, "windowTopX")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_ExcelWorkbook.__mro__:
        if "windowTopX" in klass.__dict__:
            descriptor = klass.__dict__["windowTopX"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_excelworkbook_has_displayDrawingObjects():
    assert hasattr(SpreadsheetMLWorkbookProp_ExcelWorkbook, "displayDrawingObjects")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_ExcelWorkbook.__mro__:
        if "displayDrawingObjects" in klass.__dict__:
            descriptor = klass.__dict__["displayDrawingObjects"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_excelworkbook_has_selectedSheets():
    assert hasattr(SpreadsheetMLWorkbookProp_ExcelWorkbook, "selectedSheets")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_ExcelWorkbook.__mro__:
        if "selectedSheets" in klass.__dict__:
            descriptor = klass.__dict__["selectedSheets"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_excelworkbook_has_noAutoRecover():
    assert hasattr(SpreadsheetMLWorkbookProp_ExcelWorkbook, "noAutoRecover")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_ExcelWorkbook.__mro__:
        if "noAutoRecover" in klass.__dict__:
            descriptor = klass.__dict__["noAutoRecover"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_excelworkbook_has_maxChange():
    assert hasattr(SpreadsheetMLWorkbookProp_ExcelWorkbook, "maxChange")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_ExcelWorkbook.__mro__:
        if "maxChange" in klass.__dict__:
            descriptor = klass.__dict__["maxChange"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_excelworkbook_has_precisionAsDisplayed():
    assert hasattr(SpreadsheetMLWorkbookProp_ExcelWorkbook, "precisionAsDisplayed")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_ExcelWorkbook.__mro__:
        if "precisionAsDisplayed" in klass.__dict__:
            descriptor = klass.__dict__["precisionAsDisplayed"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_excelworkbook_has_displayInkNotes():
    assert hasattr(SpreadsheetMLWorkbookProp_ExcelWorkbook, "displayInkNotes")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_ExcelWorkbook.__mro__:
        if "displayInkNotes" in klass.__dict__:
            descriptor = klass.__dict__["displayInkNotes"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_excelworkbook_has_hideVerticalScrollBar():
    assert hasattr(SpreadsheetMLWorkbookProp_ExcelWorkbook, "hideVerticalScrollBar")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_ExcelWorkbook.__mro__:
        if "hideVerticalScrollBar" in klass.__dict__:
            descriptor = klass.__dict__["hideVerticalScrollBar"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_excelworkbook_has_hideWorkbookTabs():
    assert hasattr(SpreadsheetMLWorkbookProp_ExcelWorkbook, "hideWorkbookTabs")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_ExcelWorkbook.__mro__:
        if "hideWorkbookTabs" in klass.__dict__:
            descriptor = klass.__dict__["hideWorkbookTabs"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_excelworkbook_has_protectStructure():
    assert hasattr(SpreadsheetMLWorkbookProp_ExcelWorkbook, "protectStructure")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_ExcelWorkbook.__mro__:
        if "protectStructure" in klass.__dict__:
            descriptor = klass.__dict__["protectStructure"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_excelworkbook_has_createBackup():
    assert hasattr(SpreadsheetMLWorkbookProp_ExcelWorkbook, "createBackup")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_ExcelWorkbook.__mro__:
        if "createBackup" in klass.__dict__:
            descriptor = klass.__dict__["createBackup"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_excelworkbook_has_windowHeight():
    assert hasattr(SpreadsheetMLWorkbookProp_ExcelWorkbook, "windowHeight")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_ExcelWorkbook.__mro__:
        if "windowHeight" in klass.__dict__:
            descriptor = klass.__dict__["windowHeight"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_excelworkbook_has_acceptLabelsInFormulas():
    assert hasattr(SpreadsheetMLWorkbookProp_ExcelWorkbook, "acceptLabelsInFormulas")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_ExcelWorkbook.__mro__:
        if "acceptLabelsInFormulas" in klass.__dict__:
            descriptor = klass.__dict__["acceptLabelsInFormulas"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_excelworkbook_has_embedSaveSmartTags():
    assert hasattr(SpreadsheetMLWorkbookProp_ExcelWorkbook, "embedSaveSmartTags")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_ExcelWorkbook.__mro__:
        if "embedSaveSmartTags" in klass.__dict__:
            descriptor = klass.__dict__["embedSaveSmartTags"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_excelworkbook_has_activeSheet():
    assert hasattr(SpreadsheetMLWorkbookProp_ExcelWorkbook, "activeSheet")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_ExcelWorkbook.__mro__:
        if "activeSheet" in klass.__dict__:
            descriptor = klass.__dict__["activeSheet"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_excelworkbook_has_date1904():
    assert hasattr(SpreadsheetMLWorkbookProp_ExcelWorkbook, "date1904")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_ExcelWorkbook.__mro__:
        if "date1904" in klass.__dict__:
            descriptor = klass.__dict__["date1904"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_excelworkbook_has_calculation():
    assert hasattr(SpreadsheetMLWorkbookProp_ExcelWorkbook, "calculation")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_ExcelWorkbook.__mro__:
        if "calculation" in klass.__dict__:
            descriptor = klass.__dict__["calculation"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_excelworkbook_has_windowTopY():
    assert hasattr(SpreadsheetMLWorkbookProp_ExcelWorkbook, "windowTopY")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_ExcelWorkbook.__mro__:
        if "windowTopY" in klass.__dict__:
            descriptor = klass.__dict__["windowTopY"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_excelworkbook_has_futureVer():
    assert hasattr(SpreadsheetMLWorkbookProp_ExcelWorkbook, "futureVer")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_ExcelWorkbook.__mro__:
        if "futureVer" in klass.__dict__:
            descriptor = klass.__dict__["futureVer"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_excelworkbook_has_activeChart():
    assert hasattr(SpreadsheetMLWorkbookProp_ExcelWorkbook, "activeChart")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_ExcelWorkbook.__mro__:
        if "activeChart" in klass.__dict__:
            descriptor = klass.__dict__["activeChart"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_excelworkbook_has_tabRatio():
    assert hasattr(SpreadsheetMLWorkbookProp_ExcelWorkbook, "tabRatio")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_ExcelWorkbook.__mro__:
        if "tabRatio" in klass.__dict__:
            descriptor = klass.__dict__["tabRatio"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_excelworkbook_has_windowIconic():
    assert hasattr(SpreadsheetMLWorkbookProp_ExcelWorkbook, "windowIconic")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_ExcelWorkbook.__mro__:
        if "windowIconic" in klass.__dict__:
            descriptor = klass.__dict__["windowIconic"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_excelworkbook_has_doNotCalculateBeforeSave():
    assert hasattr(SpreadsheetMLWorkbookProp_ExcelWorkbook, "doNotCalculateBeforeSave")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_ExcelWorkbook.__mro__:
        if "doNotCalculateBeforeSave" in klass.__dict__:
            descriptor = klass.__dict__["doNotCalculateBeforeSave"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_excelworkbook_has_iteration():
    assert hasattr(SpreadsheetMLWorkbookProp_ExcelWorkbook, "iteration")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_ExcelWorkbook.__mro__:
        if "iteration" in klass.__dict__:
            descriptor = klass.__dict__["iteration"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_excelworkbook_has_windowHidden():
    assert hasattr(SpreadsheetMLWorkbookProp_ExcelWorkbook, "windowHidden")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_ExcelWorkbook.__mro__:
        if "windowHidden" in klass.__dict__:
            descriptor = klass.__dict__["windowHidden"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_excelworkbook_has_refModeR1C1():
    assert hasattr(SpreadsheetMLWorkbookProp_ExcelWorkbook, "refModeR1C1")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_ExcelWorkbook.__mro__:
        if "refModeR1C1" in klass.__dict__:
            descriptor = klass.__dict__["refModeR1C1"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlworkbookprop_comment_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorkbookProp_Comment)


def test_spreadsheetmlworkbookprop_comment_constructor_exists():
    assert callable(SpreadsheetMLWorkbookProp_Comment.__init__)


def test_spreadsheetmlworkbookprop_comment_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorkbookProp_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "author" in params, "Missing parameter 'author'"
    assert "showAlways" in params, "Missing parameter 'showAlways'"

def test_spreadsheetmlworkbookprop_comment_has_author():
    assert hasattr(SpreadsheetMLWorkbookProp_Comment, "author")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_Comment.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_comment_has_showAlways():
    assert hasattr(SpreadsheetMLWorkbookProp_Comment, "showAlways")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_Comment.__mro__:
        if "showAlways" in klass.__dict__:
            descriptor = klass.__dict__["showAlways"]
            break
    assert isinstance(descriptor, property)



def test_comment_is_not_abstract():
    assert not inspect.isabstract(Comment)


def test_comment_constructor_exists():
    assert callable(Comment.__init__)


def test_comment_constructor_args():
    sig = inspect.signature(Comment.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlworkbookprop_data_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorkbookProp_Data)


def test_spreadsheetmlworkbookprop_data_constructor_exists():
    assert callable(SpreadsheetMLWorkbookProp_Data.__init__)


def test_spreadsheetmlworkbookprop_data_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorkbookProp_Data.__init__)
    params = list(sig.parameters.keys())



def test_tableelement_is_not_abstract():
    assert not inspect.isabstract(TableElement)


def test_tableelement_constructor_exists():
    assert callable(TableElement.__init__)


def test_tableelement_constructor_args():
    sig = inspect.signature(TableElement.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlworkbookprop_cell_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorkbookProp_Cell)


def test_spreadsheetmlworkbookprop_cell_constructor_exists():
    assert callable(SpreadsheetMLWorkbookProp_Cell.__init__)


def test_spreadsheetmlworkbookprop_cell_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorkbookProp_Cell.__init__)
    params = list(sig.parameters.keys())
    assert "arrayRange" in params, "Missing parameter 'arrayRange'"
    assert "hRef" in params, "Missing parameter 'hRef'"
    assert "mergeDown" in params, "Missing parameter 'mergeDown'"
    assert "formula" in params, "Missing parameter 'formula'"
    assert "mergeAcross" in params, "Missing parameter 'mergeAcross'"

def test_spreadsheetmlworkbookprop_cell_has_arrayRange():
    assert hasattr(SpreadsheetMLWorkbookProp_Cell, "arrayRange")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_Cell.__mro__:
        if "arrayRange" in klass.__dict__:
            descriptor = klass.__dict__["arrayRange"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_cell_has_hRef():
    assert hasattr(SpreadsheetMLWorkbookProp_Cell, "hRef")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_Cell.__mro__:
        if "hRef" in klass.__dict__:
            descriptor = klass.__dict__["hRef"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_cell_has_mergeDown():
    assert hasattr(SpreadsheetMLWorkbookProp_Cell, "mergeDown")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_Cell.__mro__:
        if "mergeDown" in klass.__dict__:
            descriptor = klass.__dict__["mergeDown"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_cell_has_formula():
    assert hasattr(SpreadsheetMLWorkbookProp_Cell, "formula")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_Cell.__mro__:
        if "formula" in klass.__dict__:
            descriptor = klass.__dict__["formula"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_cell_has_mergeAcross():
    assert hasattr(SpreadsheetMLWorkbookProp_Cell, "mergeAcross")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_Cell.__mro__:
        if "mergeAcross" in klass.__dict__:
            descriptor = klass.__dict__["mergeAcross"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlworkbookprop_colorrowelement_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorkbookProp_ColOrRowElement)


def test_spreadsheetmlworkbookprop_colorrowelement_constructor_exists():
    assert callable(SpreadsheetMLWorkbookProp_ColOrRowElement.__init__)


def test_spreadsheetmlworkbookprop_colorrowelement_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorkbookProp_ColOrRowElement.__init__)
    params = list(sig.parameters.keys())
    assert "span" in params, "Missing parameter 'span'"
    assert "hidden" in params, "Missing parameter 'hidden'"

def test_spreadsheetmlworkbookprop_colorrowelement_has_span():
    assert hasattr(SpreadsheetMLWorkbookProp_ColOrRowElement, "span")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_ColOrRowElement.__mro__:
        if "span" in klass.__dict__:
            descriptor = klass.__dict__["span"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_colorrowelement_has_hidden():
    assert hasattr(SpreadsheetMLWorkbookProp_ColOrRowElement, "hidden")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_ColOrRowElement.__mro__:
        if "hidden" in klass.__dict__:
            descriptor = klass.__dict__["hidden"]
            break
    assert isinstance(descriptor, property)



def test_colorrowelement_is_not_abstract():
    assert not inspect.isabstract(ColOrRowElement)


def test_colorrowelement_constructor_exists():
    assert callable(ColOrRowElement.__init__)


def test_colorrowelement_constructor_args():
    sig = inspect.signature(ColOrRowElement.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlworkbookprop_row_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorkbookProp_Row)


def test_spreadsheetmlworkbookprop_row_constructor_exists():
    assert callable(SpreadsheetMLWorkbookProp_Row.__init__)


def test_spreadsheetmlworkbookprop_row_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorkbookProp_Row.__init__)
    params = list(sig.parameters.keys())
    assert "autoFitHeight" in params, "Missing parameter 'autoFitHeight'"
    assert "height" in params, "Missing parameter 'height'"

def test_spreadsheetmlworkbookprop_row_has_autoFitHeight():
    assert hasattr(SpreadsheetMLWorkbookProp_Row, "autoFitHeight")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_Row.__mro__:
        if "autoFitHeight" in klass.__dict__:
            descriptor = klass.__dict__["autoFitHeight"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_row_has_height():
    assert hasattr(SpreadsheetMLWorkbookProp_Row, "height")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_Row.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlworkbookprop_column_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorkbookProp_Column)


def test_spreadsheetmlworkbookprop_column_constructor_exists():
    assert callable(SpreadsheetMLWorkbookProp_Column.__init__)


def test_spreadsheetmlworkbookprop_column_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorkbookProp_Column.__init__)
    params = list(sig.parameters.keys())
    assert "autoFitWidth" in params, "Missing parameter 'autoFitWidth'"
    assert "width" in params, "Missing parameter 'width'"

def test_spreadsheetmlworkbookprop_column_has_autoFitWidth():
    assert hasattr(SpreadsheetMLWorkbookProp_Column, "autoFitWidth")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_Column.__mro__:
        if "autoFitWidth" in klass.__dict__:
            descriptor = klass.__dict__["autoFitWidth"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_column_has_width():
    assert hasattr(SpreadsheetMLWorkbookProp_Column, "width")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_Column.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_column_is_not_abstract():
    assert not inspect.isabstract(Column)


def test_column_constructor_exists():
    assert callable(Column.__init__)


def test_column_constructor_args():
    sig = inspect.signature(Column.__init__)
    params = list(sig.parameters.keys())



def test_styledelement_is_not_abstract():
    assert not inspect.isabstract(StyledElement)


def test_styledelement_constructor_exists():
    assert callable(StyledElement.__init__)


def test_styledelement_constructor_args():
    sig = inspect.signature(StyledElement.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlworkbookprop_tableelement_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorkbookProp_TableElement)


def test_spreadsheetmlworkbookprop_tableelement_constructor_exists():
    assert callable(SpreadsheetMLWorkbookProp_TableElement.__init__)


def test_spreadsheetmlworkbookprop_tableelement_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorkbookProp_TableElement.__init__)
    params = list(sig.parameters.keys())
    assert "index" in params, "Missing parameter 'index'"

def test_spreadsheetmlworkbookprop_tableelement_has_index():
    assert hasattr(SpreadsheetMLWorkbookProp_TableElement, "index")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_TableElement.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlworkbookprop_table_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorkbookProp_Table)


def test_spreadsheetmlworkbookprop_table_constructor_exists():
    assert callable(SpreadsheetMLWorkbookProp_Table.__init__)


def test_spreadsheetmlworkbookprop_table_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorkbookProp_Table.__init__)
    params = list(sig.parameters.keys())
    assert "topCell" in params, "Missing parameter 'topCell'"
    assert "fullRows" in params, "Missing parameter 'fullRows'"
    assert "leftCell" in params, "Missing parameter 'leftCell'"
    assert "defaultColumnWidth" in params, "Missing parameter 'defaultColumnWidth'"
    assert "fullColumns" in params, "Missing parameter 'fullColumns'"
    assert "expandedColumnCount" in params, "Missing parameter 'expandedColumnCount'"
    assert "defaultRowHeight" in params, "Missing parameter 'defaultRowHeight'"
    assert "expandedRowCount" in params, "Missing parameter 'expandedRowCount'"

def test_spreadsheetmlworkbookprop_table_has_topCell():
    assert hasattr(SpreadsheetMLWorkbookProp_Table, "topCell")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_Table.__mro__:
        if "topCell" in klass.__dict__:
            descriptor = klass.__dict__["topCell"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_table_has_fullRows():
    assert hasattr(SpreadsheetMLWorkbookProp_Table, "fullRows")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_Table.__mro__:
        if "fullRows" in klass.__dict__:
            descriptor = klass.__dict__["fullRows"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_table_has_leftCell():
    assert hasattr(SpreadsheetMLWorkbookProp_Table, "leftCell")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_Table.__mro__:
        if "leftCell" in klass.__dict__:
            descriptor = klass.__dict__["leftCell"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_table_has_defaultColumnWidth():
    assert hasattr(SpreadsheetMLWorkbookProp_Table, "defaultColumnWidth")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_Table.__mro__:
        if "defaultColumnWidth" in klass.__dict__:
            descriptor = klass.__dict__["defaultColumnWidth"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_table_has_fullColumns():
    assert hasattr(SpreadsheetMLWorkbookProp_Table, "fullColumns")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_Table.__mro__:
        if "fullColumns" in klass.__dict__:
            descriptor = klass.__dict__["fullColumns"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_table_has_expandedColumnCount():
    assert hasattr(SpreadsheetMLWorkbookProp_Table, "expandedColumnCount")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_Table.__mro__:
        if "expandedColumnCount" in klass.__dict__:
            descriptor = klass.__dict__["expandedColumnCount"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_table_has_defaultRowHeight():
    assert hasattr(SpreadsheetMLWorkbookProp_Table, "defaultRowHeight")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_Table.__mro__:
        if "defaultRowHeight" in klass.__dict__:
            descriptor = klass.__dict__["defaultRowHeight"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop_table_has_expandedRowCount():
    assert hasattr(SpreadsheetMLWorkbookProp_Table, "expandedRowCount")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp_Table.__mro__:
        if "expandedRowCount" in klass.__dict__:
            descriptor = klass.__dict__["expandedRowCount"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlworkbookprop_styledelement_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorkbookProp_StyledElement)


def test_spreadsheetmlworkbookprop_styledelement_constructor_exists():
    assert callable(SpreadsheetMLWorkbookProp_StyledElement.__init__)


def test_spreadsheetmlworkbookprop_styledelement_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorkbookProp_StyledElement.__init__)
    params = list(sig.parameters.keys())



def test_table_is_not_abstract():
    assert not inspect.isabstract(Table)


def test_table_constructor_exists():
    assert callable(Table.__init__)


def test_table_constructor_args():
    sig = inspect.signature(Table.__init__)
    params = list(sig.parameters.keys())



def test_row_is_not_abstract():
    assert not inspect.isabstract(Row)


def test_row_constructor_exists():
    assert callable(Row.__init__)


def test_row_constructor_args():
    sig = inspect.signature(Row.__init__)
    params = list(sig.parameters.keys())



def test_excelworkbook_is_not_abstract():
    assert not inspect.isabstract(ExcelWorkbook)


def test_excelworkbook_constructor_exists():
    assert callable(ExcelWorkbook.__init__)


def test_excelworkbook_constructor_args():
    sig = inspect.signature(ExcelWorkbook.__init__)
    params = list(sig.parameters.keys())



def test_documentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(DocumentPropertiesCollection)


def test_documentpropertiescollection_constructor_exists():
    assert callable(DocumentPropertiesCollection.__init__)


def test_documentpropertiescollection_constructor_args():
    sig = inspect.signature(DocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlworkbookprop_workbook_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorkbookProp_Workbook)


def test_spreadsheetmlworkbookprop_workbook_constructor_exists():
    assert callable(SpreadsheetMLWorkbookProp_Workbook.__init__)


def test_spreadsheetmlworkbookprop_workbook_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorkbookProp_Workbook.__init__)
    params = list(sig.parameters.keys())



def test_smarttagtype_is_not_abstract():
    assert not inspect.isabstract(SmartTagType)


def test_smarttagtype_constructor_exists():
    assert callable(SmartTagType.__init__)


def test_smarttagtype_constructor_args():
    sig = inspect.signature(SmartTagType.__init__)
    params = list(sig.parameters.keys())

def test_displaydrawingobjectstype_exists():
    # Check that the Enumeration exists
    assert DisplayDrawingObjectsType is not None

def test_displaydrawingobjectstype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DisplayDrawingObjectsType]
    expected_literals = [
        "ddot_placeHolders",
        "ddot_hideAll",
        "ddot_displayShapes",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DisplayDrawingObjectsType"

def test_calculationworkbooktype_exists():
    # Check that the Enumeration exists
    assert CalculationWorkbookType is not None

def test_calculationworkbooktype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CalculationWorkbookType]
    expected_literals = [
        "cwt_manualCalculation",
        "cwt_automaticCalculation",
        "cwt_semiAutomaticCalculation",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CalculationWorkbookType"


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
SpreadsheetMLWorkbookProp_Worksheet_strategy = st.builds(
    SpreadsheetMLWorkbookProp_Worksheet,
    name=
        safe_text
)
Worksheet_strategy = st.builds(
    Worksheet,
)
SpreadsheetMLWorkbookProp_SmartTagsCollection_strategy = st.builds(
    SpreadsheetMLWorkbookProp_SmartTagsCollection,
)
SmartTagsCollection_strategy = st.builds(
    SmartTagsCollection,
)
SpreadsheetMLWorkbookProp_SmartTagType_strategy = st.builds(
    SpreadsheetMLWorkbookProp_SmartTagType,
    name=
        safe_text,
    url=
        safe_text,
    namespaceuri=
        safe_text
)
CustomDocumentPropertiesCollection_strategy = st.builds(
    CustomDocumentPropertiesCollection,
)
Cell_strategy = st.builds(
    Cell,
)
SpreadsheetMLWorkbookProp_CustomDocumentPropertiesCollection_strategy = st.builds(
    SpreadsheetMLWorkbookProp_CustomDocumentPropertiesCollection,
)
SpreadsheetMLWorkbookProp_CustomDocumentProperty_strategy = st.builds(
    SpreadsheetMLWorkbookProp_CustomDocumentProperty,
    name=
        safe_text
)
CustomDocumentProperty_strategy = st.builds(
    CustomDocumentProperty,
)
VersionType_strategy = st.builds(
    VersionType,
)
Workbook_strategy = st.builds(
    Workbook,
)
SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_strategy = st.builds(
    SpreadsheetMLWorkbookProp_DocumentPropertiesCollection,
    lines=
        safe_text,
    bytes=
        safe_text,
    appName=
        safe_text,
    paragraphs=
        safe_text,
    lastAuthor=
        safe_text,
    guid=
        safe_text,
    title=
        safe_text,
    manager=
        safe_text,
    subject=
        safe_text,
    characters=
        safe_text,
    author=
        safe_text,
    presentationFormat=
        safe_text,
    pages=
        safe_text,
    charactersWithSpaces=
        safe_text,
    keywords=
        safe_text,
    totalTime=
        safe_text,
    company=
        safe_text,
    description=
        safe_text,
    words=
        safe_text,
    hyperlinkBase=
        safe_text,
    category=
        safe_text,
    revision=
        safe_text
)
DateTimeType_strategy = st.builds(
    DateTimeType,
)
ValueType_strategy = st.builds(
    ValueType,
)
SpreadsheetMLWorkbookProp_ErrorValue_strategy = st.builds(
    SpreadsheetMLWorkbookProp_ErrorValue,
)
SpreadsheetMLWorkbookProp_NumberValue_strategy = st.builds(
    SpreadsheetMLWorkbookProp_NumberValue,
    value=
        safe_text
)
SpreadsheetMLWorkbookProp_DateTimeTypeValue_strategy = st.builds(
    SpreadsheetMLWorkbookProp_DateTimeTypeValue,
)
SpreadsheetMLWorkbookProp_BooleanValue_strategy = st.builds(
    SpreadsheetMLWorkbookProp_BooleanValue,
    value=
        safe_text
)
SpreadsheetMLWorkbookProp_StringValue_strategy = st.builds(
    SpreadsheetMLWorkbookProp_StringValue,
    value=
        safe_text
)
Data_strategy = st.builds(
    Data,
)
SpreadsheetMLWorkbookProp_ValueType_strategy = st.builds(
    SpreadsheetMLWorkbookProp_ValueType,
)
SpreadsheetMLWorkbookProp_VersionType_strategy = st.builds(
    SpreadsheetMLWorkbookProp_VersionType,
    n=
        safe_text,
    nn=
        safe_text
)
SpreadsheetMLWorkbookProp_DateTimeType_strategy = st.builds(
    SpreadsheetMLWorkbookProp_DateTimeType,
    year=
        safe_text,
    month=
        safe_text,
    day=
        safe_text,
    minute=
        safe_text,
    hour=
        safe_text,
    second=
        safe_text
)
SpreadsheetMLWorkbookProp_ExcelWorkbook_strategy = st.builds(
    SpreadsheetMLWorkbookProp_ExcelWorkbook,
    protectWindows=
        safe_text,
    firstVisibleSheet=
        safe_text,
    doNotSaveLinkValues=
        safe_text,
    windowWidth=
        safe_text,
    maxIterations=
        safe_text,
    uncalced=
        safe_text,
    hidePivotTableFieldList=
        safe_text,
    hideHorizontalScrollBar=
        safe_text,
    windowTopX=
        safe_text,
    displayDrawingObjects=
        safe_text,
    selectedSheets=
        safe_text,
    noAutoRecover=
        safe_text,
    maxChange=
        safe_text,
    precisionAsDisplayed=
        safe_text,
    displayInkNotes=
        safe_text,
    hideVerticalScrollBar=
        safe_text,
    hideWorkbookTabs=
        safe_text,
    protectStructure=
        safe_text,
    createBackup=
        safe_text,
    windowHeight=
        safe_text,
    acceptLabelsInFormulas=
        safe_text,
    embedSaveSmartTags=
        safe_text,
    activeSheet=
        safe_text,
    date1904=
        safe_text,
    calculation=
        safe_text,
    windowTopY=
        safe_text,
    futureVer=
        safe_text,
    activeChart=
        safe_text,
    tabRatio=
        safe_text,
    windowIconic=
        safe_text,
    doNotCalculateBeforeSave=
        safe_text,
    iteration=
        safe_text,
    windowHidden=
        safe_text,
    refModeR1C1=
        safe_text
)
SpreadsheetMLWorkbookProp_Comment_strategy = st.builds(
    SpreadsheetMLWorkbookProp_Comment,
    author=
        safe_text,
    showAlways=
        safe_text
)
Comment_strategy = st.builds(
    Comment,
)
SpreadsheetMLWorkbookProp_Data_strategy = st.builds(
    SpreadsheetMLWorkbookProp_Data,
)
TableElement_strategy = st.builds(
    TableElement,
)
SpreadsheetMLWorkbookProp_Cell_strategy = st.builds(
    SpreadsheetMLWorkbookProp_Cell,
    arrayRange=
        safe_text,
    hRef=
        safe_text,
    mergeDown=
        safe_text,
    formula=
        safe_text,
    mergeAcross=
        safe_text
)
SpreadsheetMLWorkbookProp_ColOrRowElement_strategy = st.builds(
    SpreadsheetMLWorkbookProp_ColOrRowElement,
    span=
        safe_text,
    hidden=
        safe_text
)
ColOrRowElement_strategy = st.builds(
    ColOrRowElement,
)
SpreadsheetMLWorkbookProp_Row_strategy = st.builds(
    SpreadsheetMLWorkbookProp_Row,
    autoFitHeight=
        safe_text,
    height=
        safe_text
)
SpreadsheetMLWorkbookProp_Column_strategy = st.builds(
    SpreadsheetMLWorkbookProp_Column,
    autoFitWidth=
        safe_text,
    width=
        safe_text
)
Column_strategy = st.builds(
    Column,
)
StyledElement_strategy = st.builds(
    StyledElement,
)
SpreadsheetMLWorkbookProp_TableElement_strategy = st.builds(
    SpreadsheetMLWorkbookProp_TableElement,
    index=
        safe_text
)
SpreadsheetMLWorkbookProp_Table_strategy = st.builds(
    SpreadsheetMLWorkbookProp_Table,
    topCell=
        safe_text,
    fullRows=
        safe_text,
    leftCell=
        safe_text,
    defaultColumnWidth=
        safe_text,
    fullColumns=
        safe_text,
    expandedColumnCount=
        safe_text,
    defaultRowHeight=
        safe_text,
    expandedRowCount=
        safe_text
)
SpreadsheetMLWorkbookProp_StyledElement_strategy = st.builds(
    SpreadsheetMLWorkbookProp_StyledElement,
)
Table_strategy = st.builds(
    Table,
)
Row_strategy = st.builds(
    Row,
)
ExcelWorkbook_strategy = st.builds(
    ExcelWorkbook,
)
DocumentPropertiesCollection_strategy = st.builds(
    DocumentPropertiesCollection,
)
SpreadsheetMLWorkbookProp_Workbook_strategy = st.builds(
    SpreadsheetMLWorkbookProp_Workbook,
)
SmartTagType_strategy = st.builds(
    SmartTagType,
)

@given(instance=SpreadsheetMLWorkbookProp_Worksheet_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworkbookprop_worksheet_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorkbookProp_Worksheet)



@given(instance=SpreadsheetMLWorkbookProp_Worksheet_strategy)
def test_spreadsheetmlworkbookprop_worksheet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Worksheet_strategy)
@settings(max_examples=50)
def test_worksheet_instantiation(instance):
    assert isinstance(instance, Worksheet)

@given(instance=SpreadsheetMLWorkbookProp_SmartTagsCollection_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworkbookprop_smarttagscollection_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorkbookProp_SmartTagsCollection)

@given(instance=SmartTagsCollection_strategy)
@settings(max_examples=50)
def test_smarttagscollection_instantiation(instance):
    assert isinstance(instance, SmartTagsCollection)

@given(instance=SpreadsheetMLWorkbookProp_SmartTagType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworkbookprop_smarttagtype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorkbookProp_SmartTagType)



@given(instance=SpreadsheetMLWorkbookProp_SmartTagType_strategy)
def test_spreadsheetmlworkbookprop_smarttagtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=SpreadsheetMLWorkbookProp_SmartTagType_strategy)
def test_spreadsheetmlworkbookprop_smarttagtype_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original



@given(instance=SpreadsheetMLWorkbookProp_SmartTagType_strategy)
def test_spreadsheetmlworkbookprop_smarttagtype_namespaceuri_setter(instance):
    original = instance.namespaceuri
    instance.namespaceuri = original
    assert instance.namespaceuri == original

@given(instance=CustomDocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_customdocumentpropertiescollection_instantiation(instance):
    assert isinstance(instance, CustomDocumentPropertiesCollection)

@given(instance=Cell_strategy)
@settings(max_examples=50)
def test_cell_instantiation(instance):
    assert isinstance(instance, Cell)

@given(instance=SpreadsheetMLWorkbookProp_CustomDocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworkbookprop_customdocumentpropertiescollection_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorkbookProp_CustomDocumentPropertiesCollection)

@given(instance=SpreadsheetMLWorkbookProp_CustomDocumentProperty_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworkbookprop_customdocumentproperty_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorkbookProp_CustomDocumentProperty)



@given(instance=SpreadsheetMLWorkbookProp_CustomDocumentProperty_strategy)
def test_spreadsheetmlworkbookprop_customdocumentproperty_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=CustomDocumentProperty_strategy)
@settings(max_examples=50)
def test_customdocumentproperty_instantiation(instance):
    assert isinstance(instance, CustomDocumentProperty)

@given(instance=VersionType_strategy)
@settings(max_examples=50)
def test_versiontype_instantiation(instance):
    assert isinstance(instance, VersionType)

@given(instance=Workbook_strategy)
@settings(max_examples=50)
def test_workbook_instantiation(instance):
    assert isinstance(instance, Workbook)

@given(instance=SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworkbookprop_documentpropertiescollection_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorkbookProp_DocumentPropertiesCollection)



@given(instance=SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop_documentpropertiescollection_lines_setter(instance):
    original = instance.lines
    instance.lines = original
    assert instance.lines == original



@given(instance=SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop_documentpropertiescollection_bytes_setter(instance):
    original = instance.bytes
    instance.bytes = original
    assert instance.bytes == original



@given(instance=SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop_documentpropertiescollection_appName_setter(instance):
    original = instance.appName
    instance.appName = original
    assert instance.appName == original



@given(instance=SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop_documentpropertiescollection_paragraphs_setter(instance):
    original = instance.paragraphs
    instance.paragraphs = original
    assert instance.paragraphs == original



@given(instance=SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop_documentpropertiescollection_lastAuthor_setter(instance):
    original = instance.lastAuthor
    instance.lastAuthor = original
    assert instance.lastAuthor == original



@given(instance=SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop_documentpropertiescollection_guid_setter(instance):
    original = instance.guid
    instance.guid = original
    assert instance.guid == original



@given(instance=SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop_documentpropertiescollection_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop_documentpropertiescollection_manager_setter(instance):
    original = instance.manager
    instance.manager = original
    assert instance.manager == original



@given(instance=SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop_documentpropertiescollection_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original



@given(instance=SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop_documentpropertiescollection_characters_setter(instance):
    original = instance.characters
    instance.characters = original
    assert instance.characters == original



@given(instance=SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop_documentpropertiescollection_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop_documentpropertiescollection_presentationFormat_setter(instance):
    original = instance.presentationFormat
    instance.presentationFormat = original
    assert instance.presentationFormat == original



@given(instance=SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop_documentpropertiescollection_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original



@given(instance=SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop_documentpropertiescollection_charactersWithSpaces_setter(instance):
    original = instance.charactersWithSpaces
    instance.charactersWithSpaces = original
    assert instance.charactersWithSpaces == original



@given(instance=SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop_documentpropertiescollection_keywords_setter(instance):
    original = instance.keywords
    instance.keywords = original
    assert instance.keywords == original



@given(instance=SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop_documentpropertiescollection_totalTime_setter(instance):
    original = instance.totalTime
    instance.totalTime = original
    assert instance.totalTime == original



@given(instance=SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop_documentpropertiescollection_company_setter(instance):
    original = instance.company
    instance.company = original
    assert instance.company == original



@given(instance=SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop_documentpropertiescollection_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop_documentpropertiescollection_words_setter(instance):
    original = instance.words
    instance.words = original
    assert instance.words == original



@given(instance=SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop_documentpropertiescollection_hyperlinkBase_setter(instance):
    original = instance.hyperlinkBase
    instance.hyperlinkBase = original
    assert instance.hyperlinkBase == original



@given(instance=SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop_documentpropertiescollection_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original



@given(instance=SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop_documentpropertiescollection_revision_setter(instance):
    original = instance.revision
    instance.revision = original
    assert instance.revision == original

@given(instance=DateTimeType_strategy)
@settings(max_examples=50)
def test_datetimetype_instantiation(instance):
    assert isinstance(instance, DateTimeType)

@given(instance=ValueType_strategy)
@settings(max_examples=50)
def test_valuetype_instantiation(instance):
    assert isinstance(instance, ValueType)

@given(instance=SpreadsheetMLWorkbookProp_ErrorValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworkbookprop_errorvalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorkbookProp_ErrorValue)

@given(instance=SpreadsheetMLWorkbookProp_NumberValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworkbookprop_numbervalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorkbookProp_NumberValue)



@given(instance=SpreadsheetMLWorkbookProp_NumberValue_strategy)
def test_spreadsheetmlworkbookprop_numbervalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SpreadsheetMLWorkbookProp_DateTimeTypeValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworkbookprop_datetimetypevalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorkbookProp_DateTimeTypeValue)

@given(instance=SpreadsheetMLWorkbookProp_BooleanValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworkbookprop_booleanvalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorkbookProp_BooleanValue)



@given(instance=SpreadsheetMLWorkbookProp_BooleanValue_strategy)
def test_spreadsheetmlworkbookprop_booleanvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SpreadsheetMLWorkbookProp_StringValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworkbookprop_stringvalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorkbookProp_StringValue)



@given(instance=SpreadsheetMLWorkbookProp_StringValue_strategy)
def test_spreadsheetmlworkbookprop_stringvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Data_strategy)
@settings(max_examples=50)
def test_data_instantiation(instance):
    assert isinstance(instance, Data)

@given(instance=SpreadsheetMLWorkbookProp_ValueType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworkbookprop_valuetype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorkbookProp_ValueType)

@given(instance=SpreadsheetMLWorkbookProp_VersionType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworkbookprop_versiontype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorkbookProp_VersionType)



@given(instance=SpreadsheetMLWorkbookProp_VersionType_strategy)
def test_spreadsheetmlworkbookprop_versiontype_n_setter(instance):
    original = instance.n
    instance.n = original
    assert instance.n == original



@given(instance=SpreadsheetMLWorkbookProp_VersionType_strategy)
def test_spreadsheetmlworkbookprop_versiontype_nn_setter(instance):
    original = instance.nn
    instance.nn = original
    assert instance.nn == original

@given(instance=SpreadsheetMLWorkbookProp_DateTimeType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworkbookprop_datetimetype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorkbookProp_DateTimeType)



@given(instance=SpreadsheetMLWorkbookProp_DateTimeType_strategy)
def test_spreadsheetmlworkbookprop_datetimetype_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original



@given(instance=SpreadsheetMLWorkbookProp_DateTimeType_strategy)
def test_spreadsheetmlworkbookprop_datetimetype_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original



@given(instance=SpreadsheetMLWorkbookProp_DateTimeType_strategy)
def test_spreadsheetmlworkbookprop_datetimetype_day_setter(instance):
    original = instance.day
    instance.day = original
    assert instance.day == original



@given(instance=SpreadsheetMLWorkbookProp_DateTimeType_strategy)
def test_spreadsheetmlworkbookprop_datetimetype_minute_setter(instance):
    original = instance.minute
    instance.minute = original
    assert instance.minute == original



@given(instance=SpreadsheetMLWorkbookProp_DateTimeType_strategy)
def test_spreadsheetmlworkbookprop_datetimetype_hour_setter(instance):
    original = instance.hour
    instance.hour = original
    assert instance.hour == original



@given(instance=SpreadsheetMLWorkbookProp_DateTimeType_strategy)
def test_spreadsheetmlworkbookprop_datetimetype_second_setter(instance):
    original = instance.second
    instance.second = original
    assert instance.second == original

@given(instance=SpreadsheetMLWorkbookProp_ExcelWorkbook_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworkbookprop_excelworkbook_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorkbookProp_ExcelWorkbook)



@given(instance=SpreadsheetMLWorkbookProp_ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop_excelworkbook_protectWindows_setter(instance):
    original = instance.protectWindows
    instance.protectWindows = original
    assert instance.protectWindows == original



@given(instance=SpreadsheetMLWorkbookProp_ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop_excelworkbook_firstVisibleSheet_setter(instance):
    original = instance.firstVisibleSheet
    instance.firstVisibleSheet = original
    assert instance.firstVisibleSheet == original



@given(instance=SpreadsheetMLWorkbookProp_ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop_excelworkbook_doNotSaveLinkValues_setter(instance):
    original = instance.doNotSaveLinkValues
    instance.doNotSaveLinkValues = original
    assert instance.doNotSaveLinkValues == original



@given(instance=SpreadsheetMLWorkbookProp_ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop_excelworkbook_windowWidth_setter(instance):
    original = instance.windowWidth
    instance.windowWidth = original
    assert instance.windowWidth == original



@given(instance=SpreadsheetMLWorkbookProp_ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop_excelworkbook_maxIterations_setter(instance):
    original = instance.maxIterations
    instance.maxIterations = original
    assert instance.maxIterations == original



@given(instance=SpreadsheetMLWorkbookProp_ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop_excelworkbook_uncalced_setter(instance):
    original = instance.uncalced
    instance.uncalced = original
    assert instance.uncalced == original



@given(instance=SpreadsheetMLWorkbookProp_ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop_excelworkbook_hidePivotTableFieldList_setter(instance):
    original = instance.hidePivotTableFieldList
    instance.hidePivotTableFieldList = original
    assert instance.hidePivotTableFieldList == original



@given(instance=SpreadsheetMLWorkbookProp_ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop_excelworkbook_hideHorizontalScrollBar_setter(instance):
    original = instance.hideHorizontalScrollBar
    instance.hideHorizontalScrollBar = original
    assert instance.hideHorizontalScrollBar == original



@given(instance=SpreadsheetMLWorkbookProp_ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop_excelworkbook_windowTopX_setter(instance):
    original = instance.windowTopX
    instance.windowTopX = original
    assert instance.windowTopX == original



@given(instance=SpreadsheetMLWorkbookProp_ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop_excelworkbook_displayDrawingObjects_setter(instance):
    original = instance.displayDrawingObjects
    instance.displayDrawingObjects = original
    assert instance.displayDrawingObjects == original



@given(instance=SpreadsheetMLWorkbookProp_ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop_excelworkbook_selectedSheets_setter(instance):
    original = instance.selectedSheets
    instance.selectedSheets = original
    assert instance.selectedSheets == original



@given(instance=SpreadsheetMLWorkbookProp_ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop_excelworkbook_noAutoRecover_setter(instance):
    original = instance.noAutoRecover
    instance.noAutoRecover = original
    assert instance.noAutoRecover == original



@given(instance=SpreadsheetMLWorkbookProp_ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop_excelworkbook_maxChange_setter(instance):
    original = instance.maxChange
    instance.maxChange = original
    assert instance.maxChange == original



@given(instance=SpreadsheetMLWorkbookProp_ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop_excelworkbook_precisionAsDisplayed_setter(instance):
    original = instance.precisionAsDisplayed
    instance.precisionAsDisplayed = original
    assert instance.precisionAsDisplayed == original



@given(instance=SpreadsheetMLWorkbookProp_ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop_excelworkbook_displayInkNotes_setter(instance):
    original = instance.displayInkNotes
    instance.displayInkNotes = original
    assert instance.displayInkNotes == original



@given(instance=SpreadsheetMLWorkbookProp_ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop_excelworkbook_hideVerticalScrollBar_setter(instance):
    original = instance.hideVerticalScrollBar
    instance.hideVerticalScrollBar = original
    assert instance.hideVerticalScrollBar == original



@given(instance=SpreadsheetMLWorkbookProp_ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop_excelworkbook_hideWorkbookTabs_setter(instance):
    original = instance.hideWorkbookTabs
    instance.hideWorkbookTabs = original
    assert instance.hideWorkbookTabs == original



@given(instance=SpreadsheetMLWorkbookProp_ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop_excelworkbook_protectStructure_setter(instance):
    original = instance.protectStructure
    instance.protectStructure = original
    assert instance.protectStructure == original



@given(instance=SpreadsheetMLWorkbookProp_ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop_excelworkbook_createBackup_setter(instance):
    original = instance.createBackup
    instance.createBackup = original
    assert instance.createBackup == original



@given(instance=SpreadsheetMLWorkbookProp_ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop_excelworkbook_windowHeight_setter(instance):
    original = instance.windowHeight
    instance.windowHeight = original
    assert instance.windowHeight == original



@given(instance=SpreadsheetMLWorkbookProp_ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop_excelworkbook_acceptLabelsInFormulas_setter(instance):
    original = instance.acceptLabelsInFormulas
    instance.acceptLabelsInFormulas = original
    assert instance.acceptLabelsInFormulas == original



@given(instance=SpreadsheetMLWorkbookProp_ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop_excelworkbook_embedSaveSmartTags_setter(instance):
    original = instance.embedSaveSmartTags
    instance.embedSaveSmartTags = original
    assert instance.embedSaveSmartTags == original



@given(instance=SpreadsheetMLWorkbookProp_ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop_excelworkbook_activeSheet_setter(instance):
    original = instance.activeSheet
    instance.activeSheet = original
    assert instance.activeSheet == original



@given(instance=SpreadsheetMLWorkbookProp_ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop_excelworkbook_date1904_setter(instance):
    original = instance.date1904
    instance.date1904 = original
    assert instance.date1904 == original



@given(instance=SpreadsheetMLWorkbookProp_ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop_excelworkbook_calculation_setter(instance):
    original = instance.calculation
    instance.calculation = original
    assert instance.calculation == original



@given(instance=SpreadsheetMLWorkbookProp_ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop_excelworkbook_windowTopY_setter(instance):
    original = instance.windowTopY
    instance.windowTopY = original
    assert instance.windowTopY == original



@given(instance=SpreadsheetMLWorkbookProp_ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop_excelworkbook_futureVer_setter(instance):
    original = instance.futureVer
    instance.futureVer = original
    assert instance.futureVer == original



@given(instance=SpreadsheetMLWorkbookProp_ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop_excelworkbook_activeChart_setter(instance):
    original = instance.activeChart
    instance.activeChart = original
    assert instance.activeChart == original



@given(instance=SpreadsheetMLWorkbookProp_ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop_excelworkbook_tabRatio_setter(instance):
    original = instance.tabRatio
    instance.tabRatio = original
    assert instance.tabRatio == original



@given(instance=SpreadsheetMLWorkbookProp_ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop_excelworkbook_windowIconic_setter(instance):
    original = instance.windowIconic
    instance.windowIconic = original
    assert instance.windowIconic == original



@given(instance=SpreadsheetMLWorkbookProp_ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop_excelworkbook_doNotCalculateBeforeSave_setter(instance):
    original = instance.doNotCalculateBeforeSave
    instance.doNotCalculateBeforeSave = original
    assert instance.doNotCalculateBeforeSave == original



@given(instance=SpreadsheetMLWorkbookProp_ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop_excelworkbook_iteration_setter(instance):
    original = instance.iteration
    instance.iteration = original
    assert instance.iteration == original



@given(instance=SpreadsheetMLWorkbookProp_ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop_excelworkbook_windowHidden_setter(instance):
    original = instance.windowHidden
    instance.windowHidden = original
    assert instance.windowHidden == original



@given(instance=SpreadsheetMLWorkbookProp_ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop_excelworkbook_refModeR1C1_setter(instance):
    original = instance.refModeR1C1
    instance.refModeR1C1 = original
    assert instance.refModeR1C1 == original

@given(instance=SpreadsheetMLWorkbookProp_Comment_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworkbookprop_comment_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorkbookProp_Comment)



@given(instance=SpreadsheetMLWorkbookProp_Comment_strategy)
def test_spreadsheetmlworkbookprop_comment_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=SpreadsheetMLWorkbookProp_Comment_strategy)
def test_spreadsheetmlworkbookprop_comment_showAlways_setter(instance):
    original = instance.showAlways
    instance.showAlways = original
    assert instance.showAlways == original

@given(instance=Comment_strategy)
@settings(max_examples=50)
def test_comment_instantiation(instance):
    assert isinstance(instance, Comment)

@given(instance=SpreadsheetMLWorkbookProp_Data_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworkbookprop_data_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorkbookProp_Data)

@given(instance=TableElement_strategy)
@settings(max_examples=50)
def test_tableelement_instantiation(instance):
    assert isinstance(instance, TableElement)

@given(instance=SpreadsheetMLWorkbookProp_Cell_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworkbookprop_cell_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorkbookProp_Cell)



@given(instance=SpreadsheetMLWorkbookProp_Cell_strategy)
def test_spreadsheetmlworkbookprop_cell_arrayRange_setter(instance):
    original = instance.arrayRange
    instance.arrayRange = original
    assert instance.arrayRange == original



@given(instance=SpreadsheetMLWorkbookProp_Cell_strategy)
def test_spreadsheetmlworkbookprop_cell_hRef_setter(instance):
    original = instance.hRef
    instance.hRef = original
    assert instance.hRef == original



@given(instance=SpreadsheetMLWorkbookProp_Cell_strategy)
def test_spreadsheetmlworkbookprop_cell_mergeDown_setter(instance):
    original = instance.mergeDown
    instance.mergeDown = original
    assert instance.mergeDown == original



@given(instance=SpreadsheetMLWorkbookProp_Cell_strategy)
def test_spreadsheetmlworkbookprop_cell_formula_setter(instance):
    original = instance.formula
    instance.formula = original
    assert instance.formula == original



@given(instance=SpreadsheetMLWorkbookProp_Cell_strategy)
def test_spreadsheetmlworkbookprop_cell_mergeAcross_setter(instance):
    original = instance.mergeAcross
    instance.mergeAcross = original
    assert instance.mergeAcross == original

@given(instance=SpreadsheetMLWorkbookProp_ColOrRowElement_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworkbookprop_colorrowelement_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorkbookProp_ColOrRowElement)



@given(instance=SpreadsheetMLWorkbookProp_ColOrRowElement_strategy)
def test_spreadsheetmlworkbookprop_colorrowelement_span_setter(instance):
    original = instance.span
    instance.span = original
    assert instance.span == original



@given(instance=SpreadsheetMLWorkbookProp_ColOrRowElement_strategy)
def test_spreadsheetmlworkbookprop_colorrowelement_hidden_setter(instance):
    original = instance.hidden
    instance.hidden = original
    assert instance.hidden == original

@given(instance=ColOrRowElement_strategy)
@settings(max_examples=50)
def test_colorrowelement_instantiation(instance):
    assert isinstance(instance, ColOrRowElement)

@given(instance=SpreadsheetMLWorkbookProp_Row_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworkbookprop_row_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorkbookProp_Row)



@given(instance=SpreadsheetMLWorkbookProp_Row_strategy)
def test_spreadsheetmlworkbookprop_row_autoFitHeight_setter(instance):
    original = instance.autoFitHeight
    instance.autoFitHeight = original
    assert instance.autoFitHeight == original



@given(instance=SpreadsheetMLWorkbookProp_Row_strategy)
def test_spreadsheetmlworkbookprop_row_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=SpreadsheetMLWorkbookProp_Column_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworkbookprop_column_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorkbookProp_Column)



@given(instance=SpreadsheetMLWorkbookProp_Column_strategy)
def test_spreadsheetmlworkbookprop_column_autoFitWidth_setter(instance):
    original = instance.autoFitWidth
    instance.autoFitWidth = original
    assert instance.autoFitWidth == original



@given(instance=SpreadsheetMLWorkbookProp_Column_strategy)
def test_spreadsheetmlworkbookprop_column_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=Column_strategy)
@settings(max_examples=50)
def test_column_instantiation(instance):
    assert isinstance(instance, Column)

@given(instance=StyledElement_strategy)
@settings(max_examples=50)
def test_styledelement_instantiation(instance):
    assert isinstance(instance, StyledElement)

@given(instance=SpreadsheetMLWorkbookProp_TableElement_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworkbookprop_tableelement_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorkbookProp_TableElement)



@given(instance=SpreadsheetMLWorkbookProp_TableElement_strategy)
def test_spreadsheetmlworkbookprop_tableelement_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original

@given(instance=SpreadsheetMLWorkbookProp_Table_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworkbookprop_table_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorkbookProp_Table)



@given(instance=SpreadsheetMLWorkbookProp_Table_strategy)
def test_spreadsheetmlworkbookprop_table_topCell_setter(instance):
    original = instance.topCell
    instance.topCell = original
    assert instance.topCell == original



@given(instance=SpreadsheetMLWorkbookProp_Table_strategy)
def test_spreadsheetmlworkbookprop_table_fullRows_setter(instance):
    original = instance.fullRows
    instance.fullRows = original
    assert instance.fullRows == original



@given(instance=SpreadsheetMLWorkbookProp_Table_strategy)
def test_spreadsheetmlworkbookprop_table_leftCell_setter(instance):
    original = instance.leftCell
    instance.leftCell = original
    assert instance.leftCell == original



@given(instance=SpreadsheetMLWorkbookProp_Table_strategy)
def test_spreadsheetmlworkbookprop_table_defaultColumnWidth_setter(instance):
    original = instance.defaultColumnWidth
    instance.defaultColumnWidth = original
    assert instance.defaultColumnWidth == original



@given(instance=SpreadsheetMLWorkbookProp_Table_strategy)
def test_spreadsheetmlworkbookprop_table_fullColumns_setter(instance):
    original = instance.fullColumns
    instance.fullColumns = original
    assert instance.fullColumns == original



@given(instance=SpreadsheetMLWorkbookProp_Table_strategy)
def test_spreadsheetmlworkbookprop_table_expandedColumnCount_setter(instance):
    original = instance.expandedColumnCount
    instance.expandedColumnCount = original
    assert instance.expandedColumnCount == original



@given(instance=SpreadsheetMLWorkbookProp_Table_strategy)
def test_spreadsheetmlworkbookprop_table_defaultRowHeight_setter(instance):
    original = instance.defaultRowHeight
    instance.defaultRowHeight = original
    assert instance.defaultRowHeight == original



@given(instance=SpreadsheetMLWorkbookProp_Table_strategy)
def test_spreadsheetmlworkbookprop_table_expandedRowCount_setter(instance):
    original = instance.expandedRowCount
    instance.expandedRowCount = original
    assert instance.expandedRowCount == original

@given(instance=SpreadsheetMLWorkbookProp_StyledElement_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworkbookprop_styledelement_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorkbookProp_StyledElement)

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)

@given(instance=Row_strategy)
@settings(max_examples=50)
def test_row_instantiation(instance):
    assert isinstance(instance, Row)

@given(instance=ExcelWorkbook_strategy)
@settings(max_examples=50)
def test_excelworkbook_instantiation(instance):
    assert isinstance(instance, ExcelWorkbook)

@given(instance=DocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_documentpropertiescollection_instantiation(instance):
    assert isinstance(instance, DocumentPropertiesCollection)

@given(instance=SpreadsheetMLWorkbookProp_Workbook_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworkbookprop_workbook_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorkbookProp_Workbook)

@given(instance=SmartTagType_strategy)
@settings(max_examples=50)
def test_smarttagtype_instantiation(instance):
    assert isinstance(instance, SmartTagType)
