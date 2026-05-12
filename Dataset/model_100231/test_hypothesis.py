import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    SpreadsheetMLWorkbookProp::SmartTagType,
    CustomDocumentPropertiesCollection,
    Cell,
    SpreadsheetMLWorkbookProp::CustomDocumentPropertiesCollection,
    SpreadsheetMLWorkbookProp::CustomDocumentProperty,
    CustomDocumentProperty,
    VersionType,
    Workbook,
    SpreadsheetMLWorkbookProp::DocumentPropertiesCollection,
    DateTimeType,
    ValueType,
    SpreadsheetMLWorkbookProp::ErrorValue,
    SpreadsheetMLWorkbookProp::NumberValue,
    SpreadsheetMLWorkbookProp::BooleanValue,
    SpreadsheetMLWorkbookProp::DateTimeTypeValue,
    SpreadsheetMLWorkbookProp::StringValue,
    Data,
    SpreadsheetMLWorkbookProp::ValueType,
    SpreadsheetMLWorkbookProp::VersionType,
    SpreadsheetMLWorkbookProp::DateTimeType,
    SpreadsheetMLWorkbookProp::ExcelWorkbook,
    SpreadsheetMLWorkbookProp::Comment,
    Comment,
    SpreadsheetMLWorkbookProp::Data,
    TableElement,
    SpreadsheetMLWorkbookProp::Cell,
    SpreadsheetMLWorkbookProp::ColOrRowElement,
    ColOrRowElement,
    SpreadsheetMLWorkbookProp::Row,
    SpreadsheetMLWorkbookProp::Column,
    Column,
    StyledElement,
    SpreadsheetMLWorkbookProp::TableElement,
    SpreadsheetMLWorkbookProp::Table,
    SpreadsheetMLWorkbookProp::StyledElement,
    Table,
    Row,
    ExcelWorkbook,
    DocumentPropertiesCollection,
    SpreadsheetMLWorkbookProp::Workbook,
    SmartTagType,
    SpreadsheetMLWorkbookProp::Worksheet,
    Worksheet,
    SpreadsheetMLWorkbookProp::SmartTagsCollection,
    SmartTagsCollection,
    CalculationWorkbookType,
    DisplayDrawingObjectsType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_spreadsheetmlworkbookprop::smarttagtype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorkbookProp::SmartTagType)


def test_spreadsheetmlworkbookprop::smarttagtype_constructor_exists():
    assert callable(SpreadsheetMLWorkbookProp::SmartTagType.__init__)


def test_spreadsheetmlworkbookprop::smarttagtype_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorkbookProp::SmartTagType.__init__)
    params = list(sig.parameters.keys())
    assert "url" in params, "Missing parameter 'url'"
    assert "namespaceuri" in params, "Missing parameter 'namespaceuri'"
    assert "name" in params, "Missing parameter 'name'"

def test_spreadsheetmlworkbookprop::smarttagtype_has_url():
    assert hasattr(SpreadsheetMLWorkbookProp::SmartTagType, "url")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::SmartTagType.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::smarttagtype_has_namespaceuri():
    assert hasattr(SpreadsheetMLWorkbookProp::SmartTagType, "namespaceuri")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::SmartTagType.__mro__:
        if "namespaceuri" in klass.__dict__:
            descriptor = klass.__dict__["namespaceuri"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::smarttagtype_has_name():
    assert hasattr(SpreadsheetMLWorkbookProp::SmartTagType, "name")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::SmartTagType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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



def test_spreadsheetmlworkbookprop::customdocumentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorkbookProp::CustomDocumentPropertiesCollection)


def test_spreadsheetmlworkbookprop::customdocumentpropertiescollection_constructor_exists():
    assert callable(SpreadsheetMLWorkbookProp::CustomDocumentPropertiesCollection.__init__)


def test_spreadsheetmlworkbookprop::customdocumentpropertiescollection_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorkbookProp::CustomDocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlworkbookprop::customdocumentproperty_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorkbookProp::CustomDocumentProperty)


def test_spreadsheetmlworkbookprop::customdocumentproperty_constructor_exists():
    assert callable(SpreadsheetMLWorkbookProp::CustomDocumentProperty.__init__)


def test_spreadsheetmlworkbookprop::customdocumentproperty_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorkbookProp::CustomDocumentProperty.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_spreadsheetmlworkbookprop::customdocumentproperty_has_name():
    assert hasattr(SpreadsheetMLWorkbookProp::CustomDocumentProperty, "name")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::CustomDocumentProperty.__mro__:
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



def test_spreadsheetmlworkbookprop::documentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorkbookProp::DocumentPropertiesCollection)


def test_spreadsheetmlworkbookprop::documentpropertiescollection_constructor_exists():
    assert callable(SpreadsheetMLWorkbookProp::DocumentPropertiesCollection.__init__)


def test_spreadsheetmlworkbookprop::documentpropertiescollection_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorkbookProp::DocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "paragraphs" in params, "Missing parameter 'paragraphs'"
    assert "revision" in params, "Missing parameter 'revision'"
    assert "company" in params, "Missing parameter 'company'"
    assert "guid" in params, "Missing parameter 'guid'"
    assert "characters" in params, "Missing parameter 'characters'"
    assert "lastAuthor" in params, "Missing parameter 'lastAuthor'"
    assert "subject" in params, "Missing parameter 'subject'"
    assert "title" in params, "Missing parameter 'title'"
    assert "lines" in params, "Missing parameter 'lines'"
    assert "manager" in params, "Missing parameter 'manager'"
    assert "category" in params, "Missing parameter 'category'"
    assert "totalTime" in params, "Missing parameter 'totalTime'"
    assert "hyperlinkBase" in params, "Missing parameter 'hyperlinkBase'"
    assert "presentationFormat" in params, "Missing parameter 'presentationFormat'"
    assert "bytes" in params, "Missing parameter 'bytes'"
    assert "appName" in params, "Missing parameter 'appName'"
    assert "words" in params, "Missing parameter 'words'"
    assert "author" in params, "Missing parameter 'author'"
    assert "pages" in params, "Missing parameter 'pages'"
    assert "keywords" in params, "Missing parameter 'keywords'"
    assert "charactersWithSpaces" in params, "Missing parameter 'charactersWithSpaces'"

def test_spreadsheetmlworkbookprop::documentpropertiescollection_has_description():
    assert hasattr(SpreadsheetMLWorkbookProp::DocumentPropertiesCollection, "description")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::DocumentPropertiesCollection.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::documentpropertiescollection_has_paragraphs():
    assert hasattr(SpreadsheetMLWorkbookProp::DocumentPropertiesCollection, "paragraphs")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::DocumentPropertiesCollection.__mro__:
        if "paragraphs" in klass.__dict__:
            descriptor = klass.__dict__["paragraphs"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::documentpropertiescollection_has_revision():
    assert hasattr(SpreadsheetMLWorkbookProp::DocumentPropertiesCollection, "revision")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::DocumentPropertiesCollection.__mro__:
        if "revision" in klass.__dict__:
            descriptor = klass.__dict__["revision"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::documentpropertiescollection_has_company():
    assert hasattr(SpreadsheetMLWorkbookProp::DocumentPropertiesCollection, "company")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::DocumentPropertiesCollection.__mro__:
        if "company" in klass.__dict__:
            descriptor = klass.__dict__["company"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::documentpropertiescollection_has_guid():
    assert hasattr(SpreadsheetMLWorkbookProp::DocumentPropertiesCollection, "guid")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::DocumentPropertiesCollection.__mro__:
        if "guid" in klass.__dict__:
            descriptor = klass.__dict__["guid"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::documentpropertiescollection_has_characters():
    assert hasattr(SpreadsheetMLWorkbookProp::DocumentPropertiesCollection, "characters")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::DocumentPropertiesCollection.__mro__:
        if "characters" in klass.__dict__:
            descriptor = klass.__dict__["characters"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::documentpropertiescollection_has_lastAuthor():
    assert hasattr(SpreadsheetMLWorkbookProp::DocumentPropertiesCollection, "lastAuthor")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::DocumentPropertiesCollection.__mro__:
        if "lastAuthor" in klass.__dict__:
            descriptor = klass.__dict__["lastAuthor"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::documentpropertiescollection_has_subject():
    assert hasattr(SpreadsheetMLWorkbookProp::DocumentPropertiesCollection, "subject")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::DocumentPropertiesCollection.__mro__:
        if "subject" in klass.__dict__:
            descriptor = klass.__dict__["subject"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::documentpropertiescollection_has_title():
    assert hasattr(SpreadsheetMLWorkbookProp::DocumentPropertiesCollection, "title")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::DocumentPropertiesCollection.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::documentpropertiescollection_has_lines():
    assert hasattr(SpreadsheetMLWorkbookProp::DocumentPropertiesCollection, "lines")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::DocumentPropertiesCollection.__mro__:
        if "lines" in klass.__dict__:
            descriptor = klass.__dict__["lines"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::documentpropertiescollection_has_manager():
    assert hasattr(SpreadsheetMLWorkbookProp::DocumentPropertiesCollection, "manager")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::DocumentPropertiesCollection.__mro__:
        if "manager" in klass.__dict__:
            descriptor = klass.__dict__["manager"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::documentpropertiescollection_has_category():
    assert hasattr(SpreadsheetMLWorkbookProp::DocumentPropertiesCollection, "category")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::DocumentPropertiesCollection.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::documentpropertiescollection_has_totalTime():
    assert hasattr(SpreadsheetMLWorkbookProp::DocumentPropertiesCollection, "totalTime")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::DocumentPropertiesCollection.__mro__:
        if "totalTime" in klass.__dict__:
            descriptor = klass.__dict__["totalTime"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::documentpropertiescollection_has_hyperlinkBase():
    assert hasattr(SpreadsheetMLWorkbookProp::DocumentPropertiesCollection, "hyperlinkBase")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::DocumentPropertiesCollection.__mro__:
        if "hyperlinkBase" in klass.__dict__:
            descriptor = klass.__dict__["hyperlinkBase"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::documentpropertiescollection_has_presentationFormat():
    assert hasattr(SpreadsheetMLWorkbookProp::DocumentPropertiesCollection, "presentationFormat")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::DocumentPropertiesCollection.__mro__:
        if "presentationFormat" in klass.__dict__:
            descriptor = klass.__dict__["presentationFormat"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::documentpropertiescollection_has_bytes():
    assert hasattr(SpreadsheetMLWorkbookProp::DocumentPropertiesCollection, "bytes")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::DocumentPropertiesCollection.__mro__:
        if "bytes" in klass.__dict__:
            descriptor = klass.__dict__["bytes"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::documentpropertiescollection_has_appName():
    assert hasattr(SpreadsheetMLWorkbookProp::DocumentPropertiesCollection, "appName")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::DocumentPropertiesCollection.__mro__:
        if "appName" in klass.__dict__:
            descriptor = klass.__dict__["appName"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::documentpropertiescollection_has_words():
    assert hasattr(SpreadsheetMLWorkbookProp::DocumentPropertiesCollection, "words")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::DocumentPropertiesCollection.__mro__:
        if "words" in klass.__dict__:
            descriptor = klass.__dict__["words"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::documentpropertiescollection_has_author():
    assert hasattr(SpreadsheetMLWorkbookProp::DocumentPropertiesCollection, "author")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::DocumentPropertiesCollection.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::documentpropertiescollection_has_pages():
    assert hasattr(SpreadsheetMLWorkbookProp::DocumentPropertiesCollection, "pages")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::DocumentPropertiesCollection.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::documentpropertiescollection_has_keywords():
    assert hasattr(SpreadsheetMLWorkbookProp::DocumentPropertiesCollection, "keywords")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::DocumentPropertiesCollection.__mro__:
        if "keywords" in klass.__dict__:
            descriptor = klass.__dict__["keywords"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::documentpropertiescollection_has_charactersWithSpaces():
    assert hasattr(SpreadsheetMLWorkbookProp::DocumentPropertiesCollection, "charactersWithSpaces")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::DocumentPropertiesCollection.__mro__:
        if "charactersWithSpaces" in klass.__dict__:
            descriptor = klass.__dict__["charactersWithSpaces"]
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



def test_spreadsheetmlworkbookprop::errorvalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorkbookProp::ErrorValue)


def test_spreadsheetmlworkbookprop::errorvalue_constructor_exists():
    assert callable(SpreadsheetMLWorkbookProp::ErrorValue.__init__)


def test_spreadsheetmlworkbookprop::errorvalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorkbookProp::ErrorValue.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlworkbookprop::numbervalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorkbookProp::NumberValue)


def test_spreadsheetmlworkbookprop::numbervalue_constructor_exists():
    assert callable(SpreadsheetMLWorkbookProp::NumberValue.__init__)


def test_spreadsheetmlworkbookprop::numbervalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorkbookProp::NumberValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_spreadsheetmlworkbookprop::numbervalue_has_value():
    assert hasattr(SpreadsheetMLWorkbookProp::NumberValue, "value")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::NumberValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlworkbookprop::booleanvalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorkbookProp::BooleanValue)


def test_spreadsheetmlworkbookprop::booleanvalue_constructor_exists():
    assert callable(SpreadsheetMLWorkbookProp::BooleanValue.__init__)


def test_spreadsheetmlworkbookprop::booleanvalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorkbookProp::BooleanValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_spreadsheetmlworkbookprop::booleanvalue_has_value():
    assert hasattr(SpreadsheetMLWorkbookProp::BooleanValue, "value")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::BooleanValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlworkbookprop::datetimetypevalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorkbookProp::DateTimeTypeValue)


def test_spreadsheetmlworkbookprop::datetimetypevalue_constructor_exists():
    assert callable(SpreadsheetMLWorkbookProp::DateTimeTypeValue.__init__)


def test_spreadsheetmlworkbookprop::datetimetypevalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorkbookProp::DateTimeTypeValue.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlworkbookprop::stringvalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorkbookProp::StringValue)


def test_spreadsheetmlworkbookprop::stringvalue_constructor_exists():
    assert callable(SpreadsheetMLWorkbookProp::StringValue.__init__)


def test_spreadsheetmlworkbookprop::stringvalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorkbookProp::StringValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_spreadsheetmlworkbookprop::stringvalue_has_value():
    assert hasattr(SpreadsheetMLWorkbookProp::StringValue, "value")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::StringValue.__mro__:
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



def test_spreadsheetmlworkbookprop::valuetype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorkbookProp::ValueType)


def test_spreadsheetmlworkbookprop::valuetype_constructor_exists():
    assert callable(SpreadsheetMLWorkbookProp::ValueType.__init__)


def test_spreadsheetmlworkbookprop::valuetype_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorkbookProp::ValueType.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlworkbookprop::versiontype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorkbookProp::VersionType)


def test_spreadsheetmlworkbookprop::versiontype_constructor_exists():
    assert callable(SpreadsheetMLWorkbookProp::VersionType.__init__)


def test_spreadsheetmlworkbookprop::versiontype_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorkbookProp::VersionType.__init__)
    params = list(sig.parameters.keys())
    assert "n" in params, "Missing parameter 'n'"
    assert "nn" in params, "Missing parameter 'nn'"

def test_spreadsheetmlworkbookprop::versiontype_has_n():
    assert hasattr(SpreadsheetMLWorkbookProp::VersionType, "n")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::VersionType.__mro__:
        if "n" in klass.__dict__:
            descriptor = klass.__dict__["n"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::versiontype_has_nn():
    assert hasattr(SpreadsheetMLWorkbookProp::VersionType, "nn")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::VersionType.__mro__:
        if "nn" in klass.__dict__:
            descriptor = klass.__dict__["nn"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlworkbookprop::datetimetype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorkbookProp::DateTimeType)


def test_spreadsheetmlworkbookprop::datetimetype_constructor_exists():
    assert callable(SpreadsheetMLWorkbookProp::DateTimeType.__init__)


def test_spreadsheetmlworkbookprop::datetimetype_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorkbookProp::DateTimeType.__init__)
    params = list(sig.parameters.keys())
    assert "day" in params, "Missing parameter 'day'"
    assert "hour" in params, "Missing parameter 'hour'"
    assert "year" in params, "Missing parameter 'year'"
    assert "minute" in params, "Missing parameter 'minute'"
    assert "second" in params, "Missing parameter 'second'"
    assert "month" in params, "Missing parameter 'month'"

def test_spreadsheetmlworkbookprop::datetimetype_has_day():
    assert hasattr(SpreadsheetMLWorkbookProp::DateTimeType, "day")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::DateTimeType.__mro__:
        if "day" in klass.__dict__:
            descriptor = klass.__dict__["day"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::datetimetype_has_hour():
    assert hasattr(SpreadsheetMLWorkbookProp::DateTimeType, "hour")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::DateTimeType.__mro__:
        if "hour" in klass.__dict__:
            descriptor = klass.__dict__["hour"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::datetimetype_has_year():
    assert hasattr(SpreadsheetMLWorkbookProp::DateTimeType, "year")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::DateTimeType.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::datetimetype_has_minute():
    assert hasattr(SpreadsheetMLWorkbookProp::DateTimeType, "minute")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::DateTimeType.__mro__:
        if "minute" in klass.__dict__:
            descriptor = klass.__dict__["minute"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::datetimetype_has_second():
    assert hasattr(SpreadsheetMLWorkbookProp::DateTimeType, "second")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::DateTimeType.__mro__:
        if "second" in klass.__dict__:
            descriptor = klass.__dict__["second"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::datetimetype_has_month():
    assert hasattr(SpreadsheetMLWorkbookProp::DateTimeType, "month")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::DateTimeType.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlworkbookprop::excelworkbook_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorkbookProp::ExcelWorkbook)


def test_spreadsheetmlworkbookprop::excelworkbook_constructor_exists():
    assert callable(SpreadsheetMLWorkbookProp::ExcelWorkbook.__init__)


def test_spreadsheetmlworkbookprop::excelworkbook_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorkbookProp::ExcelWorkbook.__init__)
    params = list(sig.parameters.keys())
    assert "displayDrawingObjects" in params, "Missing parameter 'displayDrawingObjects'"
    assert "hideVerticalScrollBar" in params, "Missing parameter 'hideVerticalScrollBar'"
    assert "hideWorkbookTabs" in params, "Missing parameter 'hideWorkbookTabs'"
    assert "hideHorizontalScrollBar" in params, "Missing parameter 'hideHorizontalScrollBar'"
    assert "displayInkNotes" in params, "Missing parameter 'displayInkNotes'"
    assert "selectedSheets" in params, "Missing parameter 'selectedSheets'"
    assert "activeSheet" in params, "Missing parameter 'activeSheet'"
    assert "windowTopX" in params, "Missing parameter 'windowTopX'"
    assert "doNotCalculateBeforeSave" in params, "Missing parameter 'doNotCalculateBeforeSave'"
    assert "windowIconic" in params, "Missing parameter 'windowIconic'"
    assert "iteration" in params, "Missing parameter 'iteration'"
    assert "tabRatio" in params, "Missing parameter 'tabRatio'"
    assert "hidePivotTableFieldList" in params, "Missing parameter 'hidePivotTableFieldList'"
    assert "maxChange" in params, "Missing parameter 'maxChange'"
    assert "acceptLabelsInFormulas" in params, "Missing parameter 'acceptLabelsInFormulas'"
    assert "precisionAsDisplayed" in params, "Missing parameter 'precisionAsDisplayed'"
    assert "refModeR1C1" in params, "Missing parameter 'refModeR1C1'"
    assert "createBackup" in params, "Missing parameter 'createBackup'"
    assert "uncalced" in params, "Missing parameter 'uncalced'"
    assert "maxIterations" in params, "Missing parameter 'maxIterations'"
    assert "windowWidth" in params, "Missing parameter 'windowWidth'"
    assert "windowHeight" in params, "Missing parameter 'windowHeight'"
    assert "firstVisibleSheet" in params, "Missing parameter 'firstVisibleSheet'"
    assert "protectWindows" in params, "Missing parameter 'protectWindows'"
    assert "protectStructure" in params, "Missing parameter 'protectStructure'"
    assert "date1904" in params, "Missing parameter 'date1904'"
    assert "activeChart" in params, "Missing parameter 'activeChart'"
    assert "futureVer" in params, "Missing parameter 'futureVer'"
    assert "windowTopY" in params, "Missing parameter 'windowTopY'"
    assert "calculation" in params, "Missing parameter 'calculation'"
    assert "noAutoRecover" in params, "Missing parameter 'noAutoRecover'"
    assert "windowHidden" in params, "Missing parameter 'windowHidden'"
    assert "doNotSaveLinkValues" in params, "Missing parameter 'doNotSaveLinkValues'"
    assert "embedSaveSmartTags" in params, "Missing parameter 'embedSaveSmartTags'"

def test_spreadsheetmlworkbookprop::excelworkbook_has_displayDrawingObjects():
    assert hasattr(SpreadsheetMLWorkbookProp::ExcelWorkbook, "displayDrawingObjects")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::ExcelWorkbook.__mro__:
        if "displayDrawingObjects" in klass.__dict__:
            descriptor = klass.__dict__["displayDrawingObjects"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::excelworkbook_has_hideVerticalScrollBar():
    assert hasattr(SpreadsheetMLWorkbookProp::ExcelWorkbook, "hideVerticalScrollBar")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::ExcelWorkbook.__mro__:
        if "hideVerticalScrollBar" in klass.__dict__:
            descriptor = klass.__dict__["hideVerticalScrollBar"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::excelworkbook_has_hideWorkbookTabs():
    assert hasattr(SpreadsheetMLWorkbookProp::ExcelWorkbook, "hideWorkbookTabs")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::ExcelWorkbook.__mro__:
        if "hideWorkbookTabs" in klass.__dict__:
            descriptor = klass.__dict__["hideWorkbookTabs"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::excelworkbook_has_hideHorizontalScrollBar():
    assert hasattr(SpreadsheetMLWorkbookProp::ExcelWorkbook, "hideHorizontalScrollBar")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::ExcelWorkbook.__mro__:
        if "hideHorizontalScrollBar" in klass.__dict__:
            descriptor = klass.__dict__["hideHorizontalScrollBar"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::excelworkbook_has_displayInkNotes():
    assert hasattr(SpreadsheetMLWorkbookProp::ExcelWorkbook, "displayInkNotes")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::ExcelWorkbook.__mro__:
        if "displayInkNotes" in klass.__dict__:
            descriptor = klass.__dict__["displayInkNotes"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::excelworkbook_has_selectedSheets():
    assert hasattr(SpreadsheetMLWorkbookProp::ExcelWorkbook, "selectedSheets")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::ExcelWorkbook.__mro__:
        if "selectedSheets" in klass.__dict__:
            descriptor = klass.__dict__["selectedSheets"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::excelworkbook_has_activeSheet():
    assert hasattr(SpreadsheetMLWorkbookProp::ExcelWorkbook, "activeSheet")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::ExcelWorkbook.__mro__:
        if "activeSheet" in klass.__dict__:
            descriptor = klass.__dict__["activeSheet"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::excelworkbook_has_windowTopX():
    assert hasattr(SpreadsheetMLWorkbookProp::ExcelWorkbook, "windowTopX")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::ExcelWorkbook.__mro__:
        if "windowTopX" in klass.__dict__:
            descriptor = klass.__dict__["windowTopX"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::excelworkbook_has_doNotCalculateBeforeSave():
    assert hasattr(SpreadsheetMLWorkbookProp::ExcelWorkbook, "doNotCalculateBeforeSave")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::ExcelWorkbook.__mro__:
        if "doNotCalculateBeforeSave" in klass.__dict__:
            descriptor = klass.__dict__["doNotCalculateBeforeSave"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::excelworkbook_has_windowIconic():
    assert hasattr(SpreadsheetMLWorkbookProp::ExcelWorkbook, "windowIconic")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::ExcelWorkbook.__mro__:
        if "windowIconic" in klass.__dict__:
            descriptor = klass.__dict__["windowIconic"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::excelworkbook_has_iteration():
    assert hasattr(SpreadsheetMLWorkbookProp::ExcelWorkbook, "iteration")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::ExcelWorkbook.__mro__:
        if "iteration" in klass.__dict__:
            descriptor = klass.__dict__["iteration"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::excelworkbook_has_tabRatio():
    assert hasattr(SpreadsheetMLWorkbookProp::ExcelWorkbook, "tabRatio")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::ExcelWorkbook.__mro__:
        if "tabRatio" in klass.__dict__:
            descriptor = klass.__dict__["tabRatio"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::excelworkbook_has_hidePivotTableFieldList():
    assert hasattr(SpreadsheetMLWorkbookProp::ExcelWorkbook, "hidePivotTableFieldList")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::ExcelWorkbook.__mro__:
        if "hidePivotTableFieldList" in klass.__dict__:
            descriptor = klass.__dict__["hidePivotTableFieldList"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::excelworkbook_has_maxChange():
    assert hasattr(SpreadsheetMLWorkbookProp::ExcelWorkbook, "maxChange")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::ExcelWorkbook.__mro__:
        if "maxChange" in klass.__dict__:
            descriptor = klass.__dict__["maxChange"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::excelworkbook_has_acceptLabelsInFormulas():
    assert hasattr(SpreadsheetMLWorkbookProp::ExcelWorkbook, "acceptLabelsInFormulas")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::ExcelWorkbook.__mro__:
        if "acceptLabelsInFormulas" in klass.__dict__:
            descriptor = klass.__dict__["acceptLabelsInFormulas"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::excelworkbook_has_precisionAsDisplayed():
    assert hasattr(SpreadsheetMLWorkbookProp::ExcelWorkbook, "precisionAsDisplayed")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::ExcelWorkbook.__mro__:
        if "precisionAsDisplayed" in klass.__dict__:
            descriptor = klass.__dict__["precisionAsDisplayed"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::excelworkbook_has_refModeR1C1():
    assert hasattr(SpreadsheetMLWorkbookProp::ExcelWorkbook, "refModeR1C1")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::ExcelWorkbook.__mro__:
        if "refModeR1C1" in klass.__dict__:
            descriptor = klass.__dict__["refModeR1C1"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::excelworkbook_has_createBackup():
    assert hasattr(SpreadsheetMLWorkbookProp::ExcelWorkbook, "createBackup")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::ExcelWorkbook.__mro__:
        if "createBackup" in klass.__dict__:
            descriptor = klass.__dict__["createBackup"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::excelworkbook_has_uncalced():
    assert hasattr(SpreadsheetMLWorkbookProp::ExcelWorkbook, "uncalced")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::ExcelWorkbook.__mro__:
        if "uncalced" in klass.__dict__:
            descriptor = klass.__dict__["uncalced"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::excelworkbook_has_maxIterations():
    assert hasattr(SpreadsheetMLWorkbookProp::ExcelWorkbook, "maxIterations")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::ExcelWorkbook.__mro__:
        if "maxIterations" in klass.__dict__:
            descriptor = klass.__dict__["maxIterations"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::excelworkbook_has_windowWidth():
    assert hasattr(SpreadsheetMLWorkbookProp::ExcelWorkbook, "windowWidth")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::ExcelWorkbook.__mro__:
        if "windowWidth" in klass.__dict__:
            descriptor = klass.__dict__["windowWidth"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::excelworkbook_has_windowHeight():
    assert hasattr(SpreadsheetMLWorkbookProp::ExcelWorkbook, "windowHeight")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::ExcelWorkbook.__mro__:
        if "windowHeight" in klass.__dict__:
            descriptor = klass.__dict__["windowHeight"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::excelworkbook_has_firstVisibleSheet():
    assert hasattr(SpreadsheetMLWorkbookProp::ExcelWorkbook, "firstVisibleSheet")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::ExcelWorkbook.__mro__:
        if "firstVisibleSheet" in klass.__dict__:
            descriptor = klass.__dict__["firstVisibleSheet"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::excelworkbook_has_protectWindows():
    assert hasattr(SpreadsheetMLWorkbookProp::ExcelWorkbook, "protectWindows")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::ExcelWorkbook.__mro__:
        if "protectWindows" in klass.__dict__:
            descriptor = klass.__dict__["protectWindows"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::excelworkbook_has_protectStructure():
    assert hasattr(SpreadsheetMLWorkbookProp::ExcelWorkbook, "protectStructure")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::ExcelWorkbook.__mro__:
        if "protectStructure" in klass.__dict__:
            descriptor = klass.__dict__["protectStructure"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::excelworkbook_has_date1904():
    assert hasattr(SpreadsheetMLWorkbookProp::ExcelWorkbook, "date1904")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::ExcelWorkbook.__mro__:
        if "date1904" in klass.__dict__:
            descriptor = klass.__dict__["date1904"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::excelworkbook_has_activeChart():
    assert hasattr(SpreadsheetMLWorkbookProp::ExcelWorkbook, "activeChart")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::ExcelWorkbook.__mro__:
        if "activeChart" in klass.__dict__:
            descriptor = klass.__dict__["activeChart"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::excelworkbook_has_futureVer():
    assert hasattr(SpreadsheetMLWorkbookProp::ExcelWorkbook, "futureVer")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::ExcelWorkbook.__mro__:
        if "futureVer" in klass.__dict__:
            descriptor = klass.__dict__["futureVer"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::excelworkbook_has_windowTopY():
    assert hasattr(SpreadsheetMLWorkbookProp::ExcelWorkbook, "windowTopY")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::ExcelWorkbook.__mro__:
        if "windowTopY" in klass.__dict__:
            descriptor = klass.__dict__["windowTopY"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::excelworkbook_has_calculation():
    assert hasattr(SpreadsheetMLWorkbookProp::ExcelWorkbook, "calculation")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::ExcelWorkbook.__mro__:
        if "calculation" in klass.__dict__:
            descriptor = klass.__dict__["calculation"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::excelworkbook_has_noAutoRecover():
    assert hasattr(SpreadsheetMLWorkbookProp::ExcelWorkbook, "noAutoRecover")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::ExcelWorkbook.__mro__:
        if "noAutoRecover" in klass.__dict__:
            descriptor = klass.__dict__["noAutoRecover"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::excelworkbook_has_windowHidden():
    assert hasattr(SpreadsheetMLWorkbookProp::ExcelWorkbook, "windowHidden")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::ExcelWorkbook.__mro__:
        if "windowHidden" in klass.__dict__:
            descriptor = klass.__dict__["windowHidden"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::excelworkbook_has_doNotSaveLinkValues():
    assert hasattr(SpreadsheetMLWorkbookProp::ExcelWorkbook, "doNotSaveLinkValues")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::ExcelWorkbook.__mro__:
        if "doNotSaveLinkValues" in klass.__dict__:
            descriptor = klass.__dict__["doNotSaveLinkValues"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::excelworkbook_has_embedSaveSmartTags():
    assert hasattr(SpreadsheetMLWorkbookProp::ExcelWorkbook, "embedSaveSmartTags")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::ExcelWorkbook.__mro__:
        if "embedSaveSmartTags" in klass.__dict__:
            descriptor = klass.__dict__["embedSaveSmartTags"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlworkbookprop::comment_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorkbookProp::Comment)


def test_spreadsheetmlworkbookprop::comment_constructor_exists():
    assert callable(SpreadsheetMLWorkbookProp::Comment.__init__)


def test_spreadsheetmlworkbookprop::comment_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorkbookProp::Comment.__init__)
    params = list(sig.parameters.keys())
    assert "author" in params, "Missing parameter 'author'"
    assert "showAlways" in params, "Missing parameter 'showAlways'"

def test_spreadsheetmlworkbookprop::comment_has_author():
    assert hasattr(SpreadsheetMLWorkbookProp::Comment, "author")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::Comment.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::comment_has_showAlways():
    assert hasattr(SpreadsheetMLWorkbookProp::Comment, "showAlways")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::Comment.__mro__:
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



def test_spreadsheetmlworkbookprop::data_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorkbookProp::Data)


def test_spreadsheetmlworkbookprop::data_constructor_exists():
    assert callable(SpreadsheetMLWorkbookProp::Data.__init__)


def test_spreadsheetmlworkbookprop::data_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorkbookProp::Data.__init__)
    params = list(sig.parameters.keys())



def test_tableelement_is_not_abstract():
    assert not inspect.isabstract(TableElement)


def test_tableelement_constructor_exists():
    assert callable(TableElement.__init__)


def test_tableelement_constructor_args():
    sig = inspect.signature(TableElement.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlworkbookprop::cell_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorkbookProp::Cell)


def test_spreadsheetmlworkbookprop::cell_constructor_exists():
    assert callable(SpreadsheetMLWorkbookProp::Cell.__init__)


def test_spreadsheetmlworkbookprop::cell_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorkbookProp::Cell.__init__)
    params = list(sig.parameters.keys())
    assert "hRef" in params, "Missing parameter 'hRef'"
    assert "formula" in params, "Missing parameter 'formula'"
    assert "mergeDown" in params, "Missing parameter 'mergeDown'"
    assert "arrayRange" in params, "Missing parameter 'arrayRange'"
    assert "mergeAcross" in params, "Missing parameter 'mergeAcross'"

def test_spreadsheetmlworkbookprop::cell_has_hRef():
    assert hasattr(SpreadsheetMLWorkbookProp::Cell, "hRef")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::Cell.__mro__:
        if "hRef" in klass.__dict__:
            descriptor = klass.__dict__["hRef"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::cell_has_formula():
    assert hasattr(SpreadsheetMLWorkbookProp::Cell, "formula")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::Cell.__mro__:
        if "formula" in klass.__dict__:
            descriptor = klass.__dict__["formula"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::cell_has_mergeDown():
    assert hasattr(SpreadsheetMLWorkbookProp::Cell, "mergeDown")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::Cell.__mro__:
        if "mergeDown" in klass.__dict__:
            descriptor = klass.__dict__["mergeDown"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::cell_has_arrayRange():
    assert hasattr(SpreadsheetMLWorkbookProp::Cell, "arrayRange")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::Cell.__mro__:
        if "arrayRange" in klass.__dict__:
            descriptor = klass.__dict__["arrayRange"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::cell_has_mergeAcross():
    assert hasattr(SpreadsheetMLWorkbookProp::Cell, "mergeAcross")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::Cell.__mro__:
        if "mergeAcross" in klass.__dict__:
            descriptor = klass.__dict__["mergeAcross"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlworkbookprop::colorrowelement_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorkbookProp::ColOrRowElement)


def test_spreadsheetmlworkbookprop::colorrowelement_constructor_exists():
    assert callable(SpreadsheetMLWorkbookProp::ColOrRowElement.__init__)


def test_spreadsheetmlworkbookprop::colorrowelement_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorkbookProp::ColOrRowElement.__init__)
    params = list(sig.parameters.keys())
    assert "hidden" in params, "Missing parameter 'hidden'"
    assert "span" in params, "Missing parameter 'span'"

def test_spreadsheetmlworkbookprop::colorrowelement_has_hidden():
    assert hasattr(SpreadsheetMLWorkbookProp::ColOrRowElement, "hidden")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::ColOrRowElement.__mro__:
        if "hidden" in klass.__dict__:
            descriptor = klass.__dict__["hidden"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::colorrowelement_has_span():
    assert hasattr(SpreadsheetMLWorkbookProp::ColOrRowElement, "span")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::ColOrRowElement.__mro__:
        if "span" in klass.__dict__:
            descriptor = klass.__dict__["span"]
            break
    assert isinstance(descriptor, property)



def test_colorrowelement_is_not_abstract():
    assert not inspect.isabstract(ColOrRowElement)


def test_colorrowelement_constructor_exists():
    assert callable(ColOrRowElement.__init__)


def test_colorrowelement_constructor_args():
    sig = inspect.signature(ColOrRowElement.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlworkbookprop::row_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorkbookProp::Row)


def test_spreadsheetmlworkbookprop::row_constructor_exists():
    assert callable(SpreadsheetMLWorkbookProp::Row.__init__)


def test_spreadsheetmlworkbookprop::row_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorkbookProp::Row.__init__)
    params = list(sig.parameters.keys())
    assert "autoFitHeight" in params, "Missing parameter 'autoFitHeight'"
    assert "height" in params, "Missing parameter 'height'"

def test_spreadsheetmlworkbookprop::row_has_autoFitHeight():
    assert hasattr(SpreadsheetMLWorkbookProp::Row, "autoFitHeight")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::Row.__mro__:
        if "autoFitHeight" in klass.__dict__:
            descriptor = klass.__dict__["autoFitHeight"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::row_has_height():
    assert hasattr(SpreadsheetMLWorkbookProp::Row, "height")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::Row.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlworkbookprop::column_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorkbookProp::Column)


def test_spreadsheetmlworkbookprop::column_constructor_exists():
    assert callable(SpreadsheetMLWorkbookProp::Column.__init__)


def test_spreadsheetmlworkbookprop::column_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorkbookProp::Column.__init__)
    params = list(sig.parameters.keys())
    assert "autoFitWidth" in params, "Missing parameter 'autoFitWidth'"
    assert "width" in params, "Missing parameter 'width'"

def test_spreadsheetmlworkbookprop::column_has_autoFitWidth():
    assert hasattr(SpreadsheetMLWorkbookProp::Column, "autoFitWidth")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::Column.__mro__:
        if "autoFitWidth" in klass.__dict__:
            descriptor = klass.__dict__["autoFitWidth"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::column_has_width():
    assert hasattr(SpreadsheetMLWorkbookProp::Column, "width")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::Column.__mro__:
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



def test_spreadsheetmlworkbookprop::tableelement_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorkbookProp::TableElement)


def test_spreadsheetmlworkbookprop::tableelement_constructor_exists():
    assert callable(SpreadsheetMLWorkbookProp::TableElement.__init__)


def test_spreadsheetmlworkbookprop::tableelement_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorkbookProp::TableElement.__init__)
    params = list(sig.parameters.keys())
    assert "index" in params, "Missing parameter 'index'"

def test_spreadsheetmlworkbookprop::tableelement_has_index():
    assert hasattr(SpreadsheetMLWorkbookProp::TableElement, "index")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::TableElement.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlworkbookprop::table_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorkbookProp::Table)


def test_spreadsheetmlworkbookprop::table_constructor_exists():
    assert callable(SpreadsheetMLWorkbookProp::Table.__init__)


def test_spreadsheetmlworkbookprop::table_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorkbookProp::Table.__init__)
    params = list(sig.parameters.keys())
    assert "leftCell" in params, "Missing parameter 'leftCell'"
    assert "topCell" in params, "Missing parameter 'topCell'"
    assert "fullRows" in params, "Missing parameter 'fullRows'"
    assert "expandedColumnCount" in params, "Missing parameter 'expandedColumnCount'"
    assert "fullColumns" in params, "Missing parameter 'fullColumns'"
    assert "expandedRowCount" in params, "Missing parameter 'expandedRowCount'"
    assert "defaultRowHeight" in params, "Missing parameter 'defaultRowHeight'"
    assert "defaultColumnWidth" in params, "Missing parameter 'defaultColumnWidth'"

def test_spreadsheetmlworkbookprop::table_has_leftCell():
    assert hasattr(SpreadsheetMLWorkbookProp::Table, "leftCell")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::Table.__mro__:
        if "leftCell" in klass.__dict__:
            descriptor = klass.__dict__["leftCell"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::table_has_topCell():
    assert hasattr(SpreadsheetMLWorkbookProp::Table, "topCell")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::Table.__mro__:
        if "topCell" in klass.__dict__:
            descriptor = klass.__dict__["topCell"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::table_has_fullRows():
    assert hasattr(SpreadsheetMLWorkbookProp::Table, "fullRows")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::Table.__mro__:
        if "fullRows" in klass.__dict__:
            descriptor = klass.__dict__["fullRows"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::table_has_expandedColumnCount():
    assert hasattr(SpreadsheetMLWorkbookProp::Table, "expandedColumnCount")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::Table.__mro__:
        if "expandedColumnCount" in klass.__dict__:
            descriptor = klass.__dict__["expandedColumnCount"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::table_has_fullColumns():
    assert hasattr(SpreadsheetMLWorkbookProp::Table, "fullColumns")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::Table.__mro__:
        if "fullColumns" in klass.__dict__:
            descriptor = klass.__dict__["fullColumns"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::table_has_expandedRowCount():
    assert hasattr(SpreadsheetMLWorkbookProp::Table, "expandedRowCount")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::Table.__mro__:
        if "expandedRowCount" in klass.__dict__:
            descriptor = klass.__dict__["expandedRowCount"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::table_has_defaultRowHeight():
    assert hasattr(SpreadsheetMLWorkbookProp::Table, "defaultRowHeight")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::Table.__mro__:
        if "defaultRowHeight" in klass.__dict__:
            descriptor = klass.__dict__["defaultRowHeight"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworkbookprop::table_has_defaultColumnWidth():
    assert hasattr(SpreadsheetMLWorkbookProp::Table, "defaultColumnWidth")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::Table.__mro__:
        if "defaultColumnWidth" in klass.__dict__:
            descriptor = klass.__dict__["defaultColumnWidth"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlworkbookprop::styledelement_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorkbookProp::StyledElement)


def test_spreadsheetmlworkbookprop::styledelement_constructor_exists():
    assert callable(SpreadsheetMLWorkbookProp::StyledElement.__init__)


def test_spreadsheetmlworkbookprop::styledelement_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorkbookProp::StyledElement.__init__)
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



def test_spreadsheetmlworkbookprop::workbook_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorkbookProp::Workbook)


def test_spreadsheetmlworkbookprop::workbook_constructor_exists():
    assert callable(SpreadsheetMLWorkbookProp::Workbook.__init__)


def test_spreadsheetmlworkbookprop::workbook_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorkbookProp::Workbook.__init__)
    params = list(sig.parameters.keys())



def test_smarttagtype_is_not_abstract():
    assert not inspect.isabstract(SmartTagType)


def test_smarttagtype_constructor_exists():
    assert callable(SmartTagType.__init__)


def test_smarttagtype_constructor_args():
    sig = inspect.signature(SmartTagType.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlworkbookprop::worksheet_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorkbookProp::Worksheet)


def test_spreadsheetmlworkbookprop::worksheet_constructor_exists():
    assert callable(SpreadsheetMLWorkbookProp::Worksheet.__init__)


def test_spreadsheetmlworkbookprop::worksheet_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorkbookProp::Worksheet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_spreadsheetmlworkbookprop::worksheet_has_name():
    assert hasattr(SpreadsheetMLWorkbookProp::Worksheet, "name")
    descriptor = None
    for klass in SpreadsheetMLWorkbookProp::Worksheet.__mro__:
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



def test_spreadsheetmlworkbookprop::smarttagscollection_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorkbookProp::SmartTagsCollection)


def test_spreadsheetmlworkbookprop::smarttagscollection_constructor_exists():
    assert callable(SpreadsheetMLWorkbookProp::SmartTagsCollection.__init__)


def test_spreadsheetmlworkbookprop::smarttagscollection_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorkbookProp::SmartTagsCollection.__init__)
    params = list(sig.parameters.keys())



def test_smarttagscollection_is_not_abstract():
    assert not inspect.isabstract(SmartTagsCollection)


def test_smarttagscollection_constructor_exists():
    assert callable(SmartTagsCollection.__init__)


def test_smarttagscollection_constructor_args():
    sig = inspect.signature(SmartTagsCollection.__init__)
    params = list(sig.parameters.keys())

def test_calculationworkbooktype_exists():
    # Check that the Enumeration exists
    assert CalculationWorkbookType is not None

def test_calculationworkbooktype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CalculationWorkbookType]
    expected_literals = [
        "cwt_automaticCalculation",
        "cwt_semiAutomaticCalculation",
        "cwt_manualCalculation",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CalculationWorkbookType"

def test_displaydrawingobjectstype_exists():
    # Check that the Enumeration exists
    assert DisplayDrawingObjectsType is not None

def test_displaydrawingobjectstype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DisplayDrawingObjectsType]
    expected_literals = [
        "ddot_hideAll",
        "ddot_placeHolders",
        "ddot_displayShapes",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DisplayDrawingObjectsType"


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
SpreadsheetMLWorkbookProp::SmartTagType_strategy = st.builds(
    SpreadsheetMLWorkbookProp::SmartTagType,
    url=
        safe_text,
    namespaceuri=
        safe_text,
    name=
        safe_text
)
CustomDocumentPropertiesCollection_strategy = st.builds(
    CustomDocumentPropertiesCollection,
)
Cell_strategy = st.builds(
    Cell,
)
SpreadsheetMLWorkbookProp::CustomDocumentPropertiesCollection_strategy = st.builds(
    SpreadsheetMLWorkbookProp::CustomDocumentPropertiesCollection,
)
SpreadsheetMLWorkbookProp::CustomDocumentProperty_strategy = st.builds(
    SpreadsheetMLWorkbookProp::CustomDocumentProperty,
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
SpreadsheetMLWorkbookProp::DocumentPropertiesCollection_strategy = st.builds(
    SpreadsheetMLWorkbookProp::DocumentPropertiesCollection,
    description=
        safe_text,
    paragraphs=
        safe_text,
    revision=
        safe_text,
    company=
        safe_text,
    guid=
        safe_text,
    characters=
        safe_text,
    lastAuthor=
        safe_text,
    subject=
        safe_text,
    title=
        safe_text,
    lines=
        safe_text,
    manager=
        safe_text,
    category=
        safe_text,
    totalTime=
        safe_text,
    hyperlinkBase=
        safe_text,
    presentationFormat=
        safe_text,
    bytes=
        safe_text,
    appName=
        safe_text,
    words=
        safe_text,
    author=
        safe_text,
    pages=
        safe_text,
    keywords=
        safe_text,
    charactersWithSpaces=
        safe_text
)
DateTimeType_strategy = st.builds(
    DateTimeType,
)
ValueType_strategy = st.builds(
    ValueType,
)
SpreadsheetMLWorkbookProp::ErrorValue_strategy = st.builds(
    SpreadsheetMLWorkbookProp::ErrorValue,
)
SpreadsheetMLWorkbookProp::NumberValue_strategy = st.builds(
    SpreadsheetMLWorkbookProp::NumberValue,
    value=
        safe_text
)
SpreadsheetMLWorkbookProp::BooleanValue_strategy = st.builds(
    SpreadsheetMLWorkbookProp::BooleanValue,
    value=
        safe_text
)
SpreadsheetMLWorkbookProp::DateTimeTypeValue_strategy = st.builds(
    SpreadsheetMLWorkbookProp::DateTimeTypeValue,
)
SpreadsheetMLWorkbookProp::StringValue_strategy = st.builds(
    SpreadsheetMLWorkbookProp::StringValue,
    value=
        safe_text
)
Data_strategy = st.builds(
    Data,
)
SpreadsheetMLWorkbookProp::ValueType_strategy = st.builds(
    SpreadsheetMLWorkbookProp::ValueType,
)
SpreadsheetMLWorkbookProp::VersionType_strategy = st.builds(
    SpreadsheetMLWorkbookProp::VersionType,
    n=
        safe_text,
    nn=
        safe_text
)
SpreadsheetMLWorkbookProp::DateTimeType_strategy = st.builds(
    SpreadsheetMLWorkbookProp::DateTimeType,
    day=
        safe_text,
    hour=
        safe_text,
    year=
        safe_text,
    minute=
        safe_text,
    second=
        safe_text,
    month=
        safe_text
)
SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy = st.builds(
    SpreadsheetMLWorkbookProp::ExcelWorkbook,
    displayDrawingObjects=
        safe_text,
    hideVerticalScrollBar=
        safe_text,
    hideWorkbookTabs=
        safe_text,
    hideHorizontalScrollBar=
        safe_text,
    displayInkNotes=
        safe_text,
    selectedSheets=
        safe_text,
    activeSheet=
        safe_text,
    windowTopX=
        safe_text,
    doNotCalculateBeforeSave=
        safe_text,
    windowIconic=
        safe_text,
    iteration=
        safe_text,
    tabRatio=
        safe_text,
    hidePivotTableFieldList=
        safe_text,
    maxChange=
        safe_text,
    acceptLabelsInFormulas=
        safe_text,
    precisionAsDisplayed=
        safe_text,
    refModeR1C1=
        safe_text,
    createBackup=
        safe_text,
    uncalced=
        safe_text,
    maxIterations=
        safe_text,
    windowWidth=
        safe_text,
    windowHeight=
        safe_text,
    firstVisibleSheet=
        safe_text,
    protectWindows=
        safe_text,
    protectStructure=
        safe_text,
    date1904=
        safe_text,
    activeChart=
        safe_text,
    futureVer=
        safe_text,
    windowTopY=
        safe_text,
    calculation=
        safe_text,
    noAutoRecover=
        safe_text,
    windowHidden=
        safe_text,
    doNotSaveLinkValues=
        safe_text,
    embedSaveSmartTags=
        safe_text
)
SpreadsheetMLWorkbookProp::Comment_strategy = st.builds(
    SpreadsheetMLWorkbookProp::Comment,
    author=
        safe_text,
    showAlways=
        safe_text
)
Comment_strategy = st.builds(
    Comment,
)
SpreadsheetMLWorkbookProp::Data_strategy = st.builds(
    SpreadsheetMLWorkbookProp::Data,
)
TableElement_strategy = st.builds(
    TableElement,
)
SpreadsheetMLWorkbookProp::Cell_strategy = st.builds(
    SpreadsheetMLWorkbookProp::Cell,
    hRef=
        safe_text,
    formula=
        safe_text,
    mergeDown=
        safe_text,
    arrayRange=
        safe_text,
    mergeAcross=
        safe_text
)
SpreadsheetMLWorkbookProp::ColOrRowElement_strategy = st.builds(
    SpreadsheetMLWorkbookProp::ColOrRowElement,
    hidden=
        safe_text,
    span=
        safe_text
)
ColOrRowElement_strategy = st.builds(
    ColOrRowElement,
)
SpreadsheetMLWorkbookProp::Row_strategy = st.builds(
    SpreadsheetMLWorkbookProp::Row,
    autoFitHeight=
        safe_text,
    height=
        safe_text
)
SpreadsheetMLWorkbookProp::Column_strategy = st.builds(
    SpreadsheetMLWorkbookProp::Column,
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
SpreadsheetMLWorkbookProp::TableElement_strategy = st.builds(
    SpreadsheetMLWorkbookProp::TableElement,
    index=
        safe_text
)
SpreadsheetMLWorkbookProp::Table_strategy = st.builds(
    SpreadsheetMLWorkbookProp::Table,
    leftCell=
        safe_text,
    topCell=
        safe_text,
    fullRows=
        safe_text,
    expandedColumnCount=
        safe_text,
    fullColumns=
        safe_text,
    expandedRowCount=
        safe_text,
    defaultRowHeight=
        safe_text,
    defaultColumnWidth=
        safe_text
)
SpreadsheetMLWorkbookProp::StyledElement_strategy = st.builds(
    SpreadsheetMLWorkbookProp::StyledElement,
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
SpreadsheetMLWorkbookProp::Workbook_strategy = st.builds(
    SpreadsheetMLWorkbookProp::Workbook,
)
SmartTagType_strategy = st.builds(
    SmartTagType,
)
SpreadsheetMLWorkbookProp::Worksheet_strategy = st.builds(
    SpreadsheetMLWorkbookProp::Worksheet,
    name=
        safe_text
)
Worksheet_strategy = st.builds(
    Worksheet,
)
SpreadsheetMLWorkbookProp::SmartTagsCollection_strategy = st.builds(
    SpreadsheetMLWorkbookProp::SmartTagsCollection,
)
SmartTagsCollection_strategy = st.builds(
    SmartTagsCollection,
)

@given(instance=SpreadsheetMLWorkbookProp::SmartTagType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworkbookprop::smarttagtype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorkbookProp::SmartTagType)

@given(instance=SpreadsheetMLWorkbookProp::SmartTagType_strategy)
def test_spreadsheetmlworkbookprop::smarttagtype_url_type(instance):
    assert isinstance(instance.url, str)


@given(instance=SpreadsheetMLWorkbookProp::SmartTagType_strategy)
def test_spreadsheetmlworkbookprop::smarttagtype_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=SpreadsheetMLWorkbookProp::SmartTagType_strategy)
def test_spreadsheetmlworkbookprop::smarttagtype_namespaceuri_type(instance):
    assert isinstance(instance.namespaceuri, str)


@given(instance=SpreadsheetMLWorkbookProp::SmartTagType_strategy)
def test_spreadsheetmlworkbookprop::smarttagtype_namespaceuri_setter(instance):
    original = instance.namespaceuri
    instance.namespaceuri = original
    assert instance.namespaceuri == original

@given(instance=SpreadsheetMLWorkbookProp::SmartTagType_strategy)
def test_spreadsheetmlworkbookprop::smarttagtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SpreadsheetMLWorkbookProp::SmartTagType_strategy)
def test_spreadsheetmlworkbookprop::smarttagtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=CustomDocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_customdocumentpropertiescollection_instantiation(instance):
    assert isinstance(instance, CustomDocumentPropertiesCollection)

@given(instance=Cell_strategy)
@settings(max_examples=50)
def test_cell_instantiation(instance):
    assert isinstance(instance, Cell)

@given(instance=SpreadsheetMLWorkbookProp::CustomDocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworkbookprop::customdocumentpropertiescollection_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorkbookProp::CustomDocumentPropertiesCollection)

@given(instance=SpreadsheetMLWorkbookProp::CustomDocumentProperty_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworkbookprop::customdocumentproperty_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorkbookProp::CustomDocumentProperty)

@given(instance=SpreadsheetMLWorkbookProp::CustomDocumentProperty_strategy)
def test_spreadsheetmlworkbookprop::customdocumentproperty_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SpreadsheetMLWorkbookProp::CustomDocumentProperty_strategy)
def test_spreadsheetmlworkbookprop::customdocumentproperty_name_setter(instance):
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

@given(instance=SpreadsheetMLWorkbookProp::DocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworkbookprop::documentpropertiescollection_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorkbookProp::DocumentPropertiesCollection)

@given(instance=SpreadsheetMLWorkbookProp::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop::documentpropertiescollection_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=SpreadsheetMLWorkbookProp::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop::documentpropertiescollection_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=SpreadsheetMLWorkbookProp::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop::documentpropertiescollection_paragraphs_type(instance):
    assert isinstance(instance.paragraphs, str)


@given(instance=SpreadsheetMLWorkbookProp::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop::documentpropertiescollection_paragraphs_setter(instance):
    original = instance.paragraphs
    instance.paragraphs = original
    assert instance.paragraphs == original

@given(instance=SpreadsheetMLWorkbookProp::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop::documentpropertiescollection_revision_type(instance):
    assert isinstance(instance.revision, str)


@given(instance=SpreadsheetMLWorkbookProp::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop::documentpropertiescollection_revision_setter(instance):
    original = instance.revision
    instance.revision = original
    assert instance.revision == original

@given(instance=SpreadsheetMLWorkbookProp::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop::documentpropertiescollection_company_type(instance):
    assert isinstance(instance.company, str)


@given(instance=SpreadsheetMLWorkbookProp::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop::documentpropertiescollection_company_setter(instance):
    original = instance.company
    instance.company = original
    assert instance.company == original

@given(instance=SpreadsheetMLWorkbookProp::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop::documentpropertiescollection_guid_type(instance):
    assert isinstance(instance.guid, str)


@given(instance=SpreadsheetMLWorkbookProp::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop::documentpropertiescollection_guid_setter(instance):
    original = instance.guid
    instance.guid = original
    assert instance.guid == original

@given(instance=SpreadsheetMLWorkbookProp::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop::documentpropertiescollection_characters_type(instance):
    assert isinstance(instance.characters, str)


@given(instance=SpreadsheetMLWorkbookProp::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop::documentpropertiescollection_characters_setter(instance):
    original = instance.characters
    instance.characters = original
    assert instance.characters == original

@given(instance=SpreadsheetMLWorkbookProp::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop::documentpropertiescollection_lastAuthor_type(instance):
    assert isinstance(instance.lastAuthor, str)


@given(instance=SpreadsheetMLWorkbookProp::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop::documentpropertiescollection_lastAuthor_setter(instance):
    original = instance.lastAuthor
    instance.lastAuthor = original
    assert instance.lastAuthor == original

@given(instance=SpreadsheetMLWorkbookProp::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop::documentpropertiescollection_subject_type(instance):
    assert isinstance(instance.subject, str)


@given(instance=SpreadsheetMLWorkbookProp::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop::documentpropertiescollection_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original

@given(instance=SpreadsheetMLWorkbookProp::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop::documentpropertiescollection_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=SpreadsheetMLWorkbookProp::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop::documentpropertiescollection_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=SpreadsheetMLWorkbookProp::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop::documentpropertiescollection_lines_type(instance):
    assert isinstance(instance.lines, str)


@given(instance=SpreadsheetMLWorkbookProp::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop::documentpropertiescollection_lines_setter(instance):
    original = instance.lines
    instance.lines = original
    assert instance.lines == original

@given(instance=SpreadsheetMLWorkbookProp::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop::documentpropertiescollection_manager_type(instance):
    assert isinstance(instance.manager, str)


@given(instance=SpreadsheetMLWorkbookProp::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop::documentpropertiescollection_manager_setter(instance):
    original = instance.manager
    instance.manager = original
    assert instance.manager == original

@given(instance=SpreadsheetMLWorkbookProp::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop::documentpropertiescollection_category_type(instance):
    assert isinstance(instance.category, str)


@given(instance=SpreadsheetMLWorkbookProp::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop::documentpropertiescollection_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original

@given(instance=SpreadsheetMLWorkbookProp::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop::documentpropertiescollection_totalTime_type(instance):
    assert isinstance(instance.totalTime, str)


@given(instance=SpreadsheetMLWorkbookProp::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop::documentpropertiescollection_totalTime_setter(instance):
    original = instance.totalTime
    instance.totalTime = original
    assert instance.totalTime == original

@given(instance=SpreadsheetMLWorkbookProp::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop::documentpropertiescollection_hyperlinkBase_type(instance):
    assert isinstance(instance.hyperlinkBase, str)


@given(instance=SpreadsheetMLWorkbookProp::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop::documentpropertiescollection_hyperlinkBase_setter(instance):
    original = instance.hyperlinkBase
    instance.hyperlinkBase = original
    assert instance.hyperlinkBase == original

@given(instance=SpreadsheetMLWorkbookProp::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop::documentpropertiescollection_presentationFormat_type(instance):
    assert isinstance(instance.presentationFormat, str)


@given(instance=SpreadsheetMLWorkbookProp::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop::documentpropertiescollection_presentationFormat_setter(instance):
    original = instance.presentationFormat
    instance.presentationFormat = original
    assert instance.presentationFormat == original

@given(instance=SpreadsheetMLWorkbookProp::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop::documentpropertiescollection_bytes_type(instance):
    assert isinstance(instance.bytes, str)


@given(instance=SpreadsheetMLWorkbookProp::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop::documentpropertiescollection_bytes_setter(instance):
    original = instance.bytes
    instance.bytes = original
    assert instance.bytes == original

@given(instance=SpreadsheetMLWorkbookProp::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop::documentpropertiescollection_appName_type(instance):
    assert isinstance(instance.appName, str)


@given(instance=SpreadsheetMLWorkbookProp::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop::documentpropertiescollection_appName_setter(instance):
    original = instance.appName
    instance.appName = original
    assert instance.appName == original

@given(instance=SpreadsheetMLWorkbookProp::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop::documentpropertiescollection_words_type(instance):
    assert isinstance(instance.words, str)


@given(instance=SpreadsheetMLWorkbookProp::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop::documentpropertiescollection_words_setter(instance):
    original = instance.words
    instance.words = original
    assert instance.words == original

@given(instance=SpreadsheetMLWorkbookProp::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop::documentpropertiescollection_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=SpreadsheetMLWorkbookProp::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop::documentpropertiescollection_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=SpreadsheetMLWorkbookProp::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop::documentpropertiescollection_pages_type(instance):
    assert isinstance(instance.pages, str)


@given(instance=SpreadsheetMLWorkbookProp::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop::documentpropertiescollection_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=SpreadsheetMLWorkbookProp::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop::documentpropertiescollection_keywords_type(instance):
    assert isinstance(instance.keywords, str)


@given(instance=SpreadsheetMLWorkbookProp::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop::documentpropertiescollection_keywords_setter(instance):
    original = instance.keywords
    instance.keywords = original
    assert instance.keywords == original

@given(instance=SpreadsheetMLWorkbookProp::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop::documentpropertiescollection_charactersWithSpaces_type(instance):
    assert isinstance(instance.charactersWithSpaces, str)


@given(instance=SpreadsheetMLWorkbookProp::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworkbookprop::documentpropertiescollection_charactersWithSpaces_setter(instance):
    original = instance.charactersWithSpaces
    instance.charactersWithSpaces = original
    assert instance.charactersWithSpaces == original

@given(instance=DateTimeType_strategy)
@settings(max_examples=50)
def test_datetimetype_instantiation(instance):
    assert isinstance(instance, DateTimeType)

@given(instance=ValueType_strategy)
@settings(max_examples=50)
def test_valuetype_instantiation(instance):
    assert isinstance(instance, ValueType)

@given(instance=SpreadsheetMLWorkbookProp::ErrorValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworkbookprop::errorvalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorkbookProp::ErrorValue)

@given(instance=SpreadsheetMLWorkbookProp::NumberValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworkbookprop::numbervalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorkbookProp::NumberValue)

@given(instance=SpreadsheetMLWorkbookProp::NumberValue_strategy)
def test_spreadsheetmlworkbookprop::numbervalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=SpreadsheetMLWorkbookProp::NumberValue_strategy)
def test_spreadsheetmlworkbookprop::numbervalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SpreadsheetMLWorkbookProp::BooleanValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworkbookprop::booleanvalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorkbookProp::BooleanValue)

@given(instance=SpreadsheetMLWorkbookProp::BooleanValue_strategy)
def test_spreadsheetmlworkbookprop::booleanvalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=SpreadsheetMLWorkbookProp::BooleanValue_strategy)
def test_spreadsheetmlworkbookprop::booleanvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SpreadsheetMLWorkbookProp::DateTimeTypeValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworkbookprop::datetimetypevalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorkbookProp::DateTimeTypeValue)

@given(instance=SpreadsheetMLWorkbookProp::StringValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworkbookprop::stringvalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorkbookProp::StringValue)

@given(instance=SpreadsheetMLWorkbookProp::StringValue_strategy)
def test_spreadsheetmlworkbookprop::stringvalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=SpreadsheetMLWorkbookProp::StringValue_strategy)
def test_spreadsheetmlworkbookprop::stringvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Data_strategy)
@settings(max_examples=50)
def test_data_instantiation(instance):
    assert isinstance(instance, Data)

@given(instance=SpreadsheetMLWorkbookProp::ValueType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworkbookprop::valuetype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorkbookProp::ValueType)

@given(instance=SpreadsheetMLWorkbookProp::VersionType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworkbookprop::versiontype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorkbookProp::VersionType)

@given(instance=SpreadsheetMLWorkbookProp::VersionType_strategy)
def test_spreadsheetmlworkbookprop::versiontype_n_type(instance):
    assert isinstance(instance.n, str)


@given(instance=SpreadsheetMLWorkbookProp::VersionType_strategy)
def test_spreadsheetmlworkbookprop::versiontype_n_setter(instance):
    original = instance.n
    instance.n = original
    assert instance.n == original

@given(instance=SpreadsheetMLWorkbookProp::VersionType_strategy)
def test_spreadsheetmlworkbookprop::versiontype_nn_type(instance):
    assert isinstance(instance.nn, str)


@given(instance=SpreadsheetMLWorkbookProp::VersionType_strategy)
def test_spreadsheetmlworkbookprop::versiontype_nn_setter(instance):
    original = instance.nn
    instance.nn = original
    assert instance.nn == original

@given(instance=SpreadsheetMLWorkbookProp::DateTimeType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworkbookprop::datetimetype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorkbookProp::DateTimeType)

@given(instance=SpreadsheetMLWorkbookProp::DateTimeType_strategy)
def test_spreadsheetmlworkbookprop::datetimetype_day_type(instance):
    assert isinstance(instance.day, str)


@given(instance=SpreadsheetMLWorkbookProp::DateTimeType_strategy)
def test_spreadsheetmlworkbookprop::datetimetype_day_setter(instance):
    original = instance.day
    instance.day = original
    assert instance.day == original

@given(instance=SpreadsheetMLWorkbookProp::DateTimeType_strategy)
def test_spreadsheetmlworkbookprop::datetimetype_hour_type(instance):
    assert isinstance(instance.hour, str)


@given(instance=SpreadsheetMLWorkbookProp::DateTimeType_strategy)
def test_spreadsheetmlworkbookprop::datetimetype_hour_setter(instance):
    original = instance.hour
    instance.hour = original
    assert instance.hour == original

@given(instance=SpreadsheetMLWorkbookProp::DateTimeType_strategy)
def test_spreadsheetmlworkbookprop::datetimetype_year_type(instance):
    assert isinstance(instance.year, str)


@given(instance=SpreadsheetMLWorkbookProp::DateTimeType_strategy)
def test_spreadsheetmlworkbookprop::datetimetype_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=SpreadsheetMLWorkbookProp::DateTimeType_strategy)
def test_spreadsheetmlworkbookprop::datetimetype_minute_type(instance):
    assert isinstance(instance.minute, str)


@given(instance=SpreadsheetMLWorkbookProp::DateTimeType_strategy)
def test_spreadsheetmlworkbookprop::datetimetype_minute_setter(instance):
    original = instance.minute
    instance.minute = original
    assert instance.minute == original

@given(instance=SpreadsheetMLWorkbookProp::DateTimeType_strategy)
def test_spreadsheetmlworkbookprop::datetimetype_second_type(instance):
    assert isinstance(instance.second, str)


@given(instance=SpreadsheetMLWorkbookProp::DateTimeType_strategy)
def test_spreadsheetmlworkbookprop::datetimetype_second_setter(instance):
    original = instance.second
    instance.second = original
    assert instance.second == original

@given(instance=SpreadsheetMLWorkbookProp::DateTimeType_strategy)
def test_spreadsheetmlworkbookprop::datetimetype_month_type(instance):
    assert isinstance(instance.month, str)


@given(instance=SpreadsheetMLWorkbookProp::DateTimeType_strategy)
def test_spreadsheetmlworkbookprop::datetimetype_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original

@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworkbookprop::excelworkbook_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorkbookProp::ExcelWorkbook)

@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_displayDrawingObjects_type(instance):
    assert isinstance(instance.displayDrawingObjects, str)


@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_displayDrawingObjects_setter(instance):
    original = instance.displayDrawingObjects
    instance.displayDrawingObjects = original
    assert instance.displayDrawingObjects == original

@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_hideVerticalScrollBar_type(instance):
    assert isinstance(instance.hideVerticalScrollBar, str)


@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_hideVerticalScrollBar_setter(instance):
    original = instance.hideVerticalScrollBar
    instance.hideVerticalScrollBar = original
    assert instance.hideVerticalScrollBar == original

@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_hideWorkbookTabs_type(instance):
    assert isinstance(instance.hideWorkbookTabs, str)


@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_hideWorkbookTabs_setter(instance):
    original = instance.hideWorkbookTabs
    instance.hideWorkbookTabs = original
    assert instance.hideWorkbookTabs == original

@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_hideHorizontalScrollBar_type(instance):
    assert isinstance(instance.hideHorizontalScrollBar, str)


@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_hideHorizontalScrollBar_setter(instance):
    original = instance.hideHorizontalScrollBar
    instance.hideHorizontalScrollBar = original
    assert instance.hideHorizontalScrollBar == original

@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_displayInkNotes_type(instance):
    assert isinstance(instance.displayInkNotes, str)


@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_displayInkNotes_setter(instance):
    original = instance.displayInkNotes
    instance.displayInkNotes = original
    assert instance.displayInkNotes == original

@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_selectedSheets_type(instance):
    assert isinstance(instance.selectedSheets, str)


@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_selectedSheets_setter(instance):
    original = instance.selectedSheets
    instance.selectedSheets = original
    assert instance.selectedSheets == original

@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_activeSheet_type(instance):
    assert isinstance(instance.activeSheet, str)


@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_activeSheet_setter(instance):
    original = instance.activeSheet
    instance.activeSheet = original
    assert instance.activeSheet == original

@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_windowTopX_type(instance):
    assert isinstance(instance.windowTopX, str)


@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_windowTopX_setter(instance):
    original = instance.windowTopX
    instance.windowTopX = original
    assert instance.windowTopX == original

@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_doNotCalculateBeforeSave_type(instance):
    assert isinstance(instance.doNotCalculateBeforeSave, str)


@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_doNotCalculateBeforeSave_setter(instance):
    original = instance.doNotCalculateBeforeSave
    instance.doNotCalculateBeforeSave = original
    assert instance.doNotCalculateBeforeSave == original

@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_windowIconic_type(instance):
    assert isinstance(instance.windowIconic, str)


@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_windowIconic_setter(instance):
    original = instance.windowIconic
    instance.windowIconic = original
    assert instance.windowIconic == original

@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_iteration_type(instance):
    assert isinstance(instance.iteration, str)


@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_iteration_setter(instance):
    original = instance.iteration
    instance.iteration = original
    assert instance.iteration == original

@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_tabRatio_type(instance):
    assert isinstance(instance.tabRatio, str)


@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_tabRatio_setter(instance):
    original = instance.tabRatio
    instance.tabRatio = original
    assert instance.tabRatio == original

@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_hidePivotTableFieldList_type(instance):
    assert isinstance(instance.hidePivotTableFieldList, str)


@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_hidePivotTableFieldList_setter(instance):
    original = instance.hidePivotTableFieldList
    instance.hidePivotTableFieldList = original
    assert instance.hidePivotTableFieldList == original

@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_maxChange_type(instance):
    assert isinstance(instance.maxChange, str)


@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_maxChange_setter(instance):
    original = instance.maxChange
    instance.maxChange = original
    assert instance.maxChange == original

@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_acceptLabelsInFormulas_type(instance):
    assert isinstance(instance.acceptLabelsInFormulas, str)


@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_acceptLabelsInFormulas_setter(instance):
    original = instance.acceptLabelsInFormulas
    instance.acceptLabelsInFormulas = original
    assert instance.acceptLabelsInFormulas == original

@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_precisionAsDisplayed_type(instance):
    assert isinstance(instance.precisionAsDisplayed, str)


@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_precisionAsDisplayed_setter(instance):
    original = instance.precisionAsDisplayed
    instance.precisionAsDisplayed = original
    assert instance.precisionAsDisplayed == original

@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_refModeR1C1_type(instance):
    assert isinstance(instance.refModeR1C1, str)


@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_refModeR1C1_setter(instance):
    original = instance.refModeR1C1
    instance.refModeR1C1 = original
    assert instance.refModeR1C1 == original

@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_createBackup_type(instance):
    assert isinstance(instance.createBackup, str)


@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_createBackup_setter(instance):
    original = instance.createBackup
    instance.createBackup = original
    assert instance.createBackup == original

@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_uncalced_type(instance):
    assert isinstance(instance.uncalced, str)


@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_uncalced_setter(instance):
    original = instance.uncalced
    instance.uncalced = original
    assert instance.uncalced == original

@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_maxIterations_type(instance):
    assert isinstance(instance.maxIterations, str)


@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_maxIterations_setter(instance):
    original = instance.maxIterations
    instance.maxIterations = original
    assert instance.maxIterations == original

@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_windowWidth_type(instance):
    assert isinstance(instance.windowWidth, str)


@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_windowWidth_setter(instance):
    original = instance.windowWidth
    instance.windowWidth = original
    assert instance.windowWidth == original

@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_windowHeight_type(instance):
    assert isinstance(instance.windowHeight, str)


@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_windowHeight_setter(instance):
    original = instance.windowHeight
    instance.windowHeight = original
    assert instance.windowHeight == original

@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_firstVisibleSheet_type(instance):
    assert isinstance(instance.firstVisibleSheet, str)


@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_firstVisibleSheet_setter(instance):
    original = instance.firstVisibleSheet
    instance.firstVisibleSheet = original
    assert instance.firstVisibleSheet == original

@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_protectWindows_type(instance):
    assert isinstance(instance.protectWindows, str)


@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_protectWindows_setter(instance):
    original = instance.protectWindows
    instance.protectWindows = original
    assert instance.protectWindows == original

@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_protectStructure_type(instance):
    assert isinstance(instance.protectStructure, str)


@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_protectStructure_setter(instance):
    original = instance.protectStructure
    instance.protectStructure = original
    assert instance.protectStructure == original

@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_date1904_type(instance):
    assert isinstance(instance.date1904, str)


@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_date1904_setter(instance):
    original = instance.date1904
    instance.date1904 = original
    assert instance.date1904 == original

@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_activeChart_type(instance):
    assert isinstance(instance.activeChart, str)


@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_activeChart_setter(instance):
    original = instance.activeChart
    instance.activeChart = original
    assert instance.activeChart == original

@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_futureVer_type(instance):
    assert isinstance(instance.futureVer, str)


@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_futureVer_setter(instance):
    original = instance.futureVer
    instance.futureVer = original
    assert instance.futureVer == original

@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_windowTopY_type(instance):
    assert isinstance(instance.windowTopY, str)


@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_windowTopY_setter(instance):
    original = instance.windowTopY
    instance.windowTopY = original
    assert instance.windowTopY == original

@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_calculation_type(instance):
    assert isinstance(instance.calculation, str)


@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_calculation_setter(instance):
    original = instance.calculation
    instance.calculation = original
    assert instance.calculation == original

@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_noAutoRecover_type(instance):
    assert isinstance(instance.noAutoRecover, str)


@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_noAutoRecover_setter(instance):
    original = instance.noAutoRecover
    instance.noAutoRecover = original
    assert instance.noAutoRecover == original

@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_windowHidden_type(instance):
    assert isinstance(instance.windowHidden, str)


@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_windowHidden_setter(instance):
    original = instance.windowHidden
    instance.windowHidden = original
    assert instance.windowHidden == original

@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_doNotSaveLinkValues_type(instance):
    assert isinstance(instance.doNotSaveLinkValues, str)


@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_doNotSaveLinkValues_setter(instance):
    original = instance.doNotSaveLinkValues
    instance.doNotSaveLinkValues = original
    assert instance.doNotSaveLinkValues == original

@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_embedSaveSmartTags_type(instance):
    assert isinstance(instance.embedSaveSmartTags, str)


@given(instance=SpreadsheetMLWorkbookProp::ExcelWorkbook_strategy)
def test_spreadsheetmlworkbookprop::excelworkbook_embedSaveSmartTags_setter(instance):
    original = instance.embedSaveSmartTags
    instance.embedSaveSmartTags = original
    assert instance.embedSaveSmartTags == original

@given(instance=SpreadsheetMLWorkbookProp::Comment_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworkbookprop::comment_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorkbookProp::Comment)

@given(instance=SpreadsheetMLWorkbookProp::Comment_strategy)
def test_spreadsheetmlworkbookprop::comment_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=SpreadsheetMLWorkbookProp::Comment_strategy)
def test_spreadsheetmlworkbookprop::comment_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=SpreadsheetMLWorkbookProp::Comment_strategy)
def test_spreadsheetmlworkbookprop::comment_showAlways_type(instance):
    assert isinstance(instance.showAlways, str)


@given(instance=SpreadsheetMLWorkbookProp::Comment_strategy)
def test_spreadsheetmlworkbookprop::comment_showAlways_setter(instance):
    original = instance.showAlways
    instance.showAlways = original
    assert instance.showAlways == original

@given(instance=Comment_strategy)
@settings(max_examples=50)
def test_comment_instantiation(instance):
    assert isinstance(instance, Comment)

@given(instance=SpreadsheetMLWorkbookProp::Data_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworkbookprop::data_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorkbookProp::Data)

@given(instance=TableElement_strategy)
@settings(max_examples=50)
def test_tableelement_instantiation(instance):
    assert isinstance(instance, TableElement)

@given(instance=SpreadsheetMLWorkbookProp::Cell_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworkbookprop::cell_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorkbookProp::Cell)

@given(instance=SpreadsheetMLWorkbookProp::Cell_strategy)
def test_spreadsheetmlworkbookprop::cell_hRef_type(instance):
    assert isinstance(instance.hRef, str)


@given(instance=SpreadsheetMLWorkbookProp::Cell_strategy)
def test_spreadsheetmlworkbookprop::cell_hRef_setter(instance):
    original = instance.hRef
    instance.hRef = original
    assert instance.hRef == original

@given(instance=SpreadsheetMLWorkbookProp::Cell_strategy)
def test_spreadsheetmlworkbookprop::cell_formula_type(instance):
    assert isinstance(instance.formula, str)


@given(instance=SpreadsheetMLWorkbookProp::Cell_strategy)
def test_spreadsheetmlworkbookprop::cell_formula_setter(instance):
    original = instance.formula
    instance.formula = original
    assert instance.formula == original

@given(instance=SpreadsheetMLWorkbookProp::Cell_strategy)
def test_spreadsheetmlworkbookprop::cell_mergeDown_type(instance):
    assert isinstance(instance.mergeDown, str)


@given(instance=SpreadsheetMLWorkbookProp::Cell_strategy)
def test_spreadsheetmlworkbookprop::cell_mergeDown_setter(instance):
    original = instance.mergeDown
    instance.mergeDown = original
    assert instance.mergeDown == original

@given(instance=SpreadsheetMLWorkbookProp::Cell_strategy)
def test_spreadsheetmlworkbookprop::cell_arrayRange_type(instance):
    assert isinstance(instance.arrayRange, str)


@given(instance=SpreadsheetMLWorkbookProp::Cell_strategy)
def test_spreadsheetmlworkbookprop::cell_arrayRange_setter(instance):
    original = instance.arrayRange
    instance.arrayRange = original
    assert instance.arrayRange == original

@given(instance=SpreadsheetMLWorkbookProp::Cell_strategy)
def test_spreadsheetmlworkbookprop::cell_mergeAcross_type(instance):
    assert isinstance(instance.mergeAcross, str)


@given(instance=SpreadsheetMLWorkbookProp::Cell_strategy)
def test_spreadsheetmlworkbookprop::cell_mergeAcross_setter(instance):
    original = instance.mergeAcross
    instance.mergeAcross = original
    assert instance.mergeAcross == original

@given(instance=SpreadsheetMLWorkbookProp::ColOrRowElement_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworkbookprop::colorrowelement_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorkbookProp::ColOrRowElement)

@given(instance=SpreadsheetMLWorkbookProp::ColOrRowElement_strategy)
def test_spreadsheetmlworkbookprop::colorrowelement_hidden_type(instance):
    assert isinstance(instance.hidden, str)


@given(instance=SpreadsheetMLWorkbookProp::ColOrRowElement_strategy)
def test_spreadsheetmlworkbookprop::colorrowelement_hidden_setter(instance):
    original = instance.hidden
    instance.hidden = original
    assert instance.hidden == original

@given(instance=SpreadsheetMLWorkbookProp::ColOrRowElement_strategy)
def test_spreadsheetmlworkbookprop::colorrowelement_span_type(instance):
    assert isinstance(instance.span, str)


@given(instance=SpreadsheetMLWorkbookProp::ColOrRowElement_strategy)
def test_spreadsheetmlworkbookprop::colorrowelement_span_setter(instance):
    original = instance.span
    instance.span = original
    assert instance.span == original

@given(instance=ColOrRowElement_strategy)
@settings(max_examples=50)
def test_colorrowelement_instantiation(instance):
    assert isinstance(instance, ColOrRowElement)

@given(instance=SpreadsheetMLWorkbookProp::Row_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworkbookprop::row_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorkbookProp::Row)

@given(instance=SpreadsheetMLWorkbookProp::Row_strategy)
def test_spreadsheetmlworkbookprop::row_autoFitHeight_type(instance):
    assert isinstance(instance.autoFitHeight, str)


@given(instance=SpreadsheetMLWorkbookProp::Row_strategy)
def test_spreadsheetmlworkbookprop::row_autoFitHeight_setter(instance):
    original = instance.autoFitHeight
    instance.autoFitHeight = original
    assert instance.autoFitHeight == original

@given(instance=SpreadsheetMLWorkbookProp::Row_strategy)
def test_spreadsheetmlworkbookprop::row_height_type(instance):
    assert isinstance(instance.height, str)


@given(instance=SpreadsheetMLWorkbookProp::Row_strategy)
def test_spreadsheetmlworkbookprop::row_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=SpreadsheetMLWorkbookProp::Column_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworkbookprop::column_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorkbookProp::Column)

@given(instance=SpreadsheetMLWorkbookProp::Column_strategy)
def test_spreadsheetmlworkbookprop::column_autoFitWidth_type(instance):
    assert isinstance(instance.autoFitWidth, str)


@given(instance=SpreadsheetMLWorkbookProp::Column_strategy)
def test_spreadsheetmlworkbookprop::column_autoFitWidth_setter(instance):
    original = instance.autoFitWidth
    instance.autoFitWidth = original
    assert instance.autoFitWidth == original

@given(instance=SpreadsheetMLWorkbookProp::Column_strategy)
def test_spreadsheetmlworkbookprop::column_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=SpreadsheetMLWorkbookProp::Column_strategy)
def test_spreadsheetmlworkbookprop::column_width_setter(instance):
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

@given(instance=SpreadsheetMLWorkbookProp::TableElement_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworkbookprop::tableelement_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorkbookProp::TableElement)

@given(instance=SpreadsheetMLWorkbookProp::TableElement_strategy)
def test_spreadsheetmlworkbookprop::tableelement_index_type(instance):
    assert isinstance(instance.index, str)


@given(instance=SpreadsheetMLWorkbookProp::TableElement_strategy)
def test_spreadsheetmlworkbookprop::tableelement_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original

@given(instance=SpreadsheetMLWorkbookProp::Table_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworkbookprop::table_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorkbookProp::Table)

@given(instance=SpreadsheetMLWorkbookProp::Table_strategy)
def test_spreadsheetmlworkbookprop::table_leftCell_type(instance):
    assert isinstance(instance.leftCell, str)


@given(instance=SpreadsheetMLWorkbookProp::Table_strategy)
def test_spreadsheetmlworkbookprop::table_leftCell_setter(instance):
    original = instance.leftCell
    instance.leftCell = original
    assert instance.leftCell == original

@given(instance=SpreadsheetMLWorkbookProp::Table_strategy)
def test_spreadsheetmlworkbookprop::table_topCell_type(instance):
    assert isinstance(instance.topCell, str)


@given(instance=SpreadsheetMLWorkbookProp::Table_strategy)
def test_spreadsheetmlworkbookprop::table_topCell_setter(instance):
    original = instance.topCell
    instance.topCell = original
    assert instance.topCell == original

@given(instance=SpreadsheetMLWorkbookProp::Table_strategy)
def test_spreadsheetmlworkbookprop::table_fullRows_type(instance):
    assert isinstance(instance.fullRows, str)


@given(instance=SpreadsheetMLWorkbookProp::Table_strategy)
def test_spreadsheetmlworkbookprop::table_fullRows_setter(instance):
    original = instance.fullRows
    instance.fullRows = original
    assert instance.fullRows == original

@given(instance=SpreadsheetMLWorkbookProp::Table_strategy)
def test_spreadsheetmlworkbookprop::table_expandedColumnCount_type(instance):
    assert isinstance(instance.expandedColumnCount, str)


@given(instance=SpreadsheetMLWorkbookProp::Table_strategy)
def test_spreadsheetmlworkbookprop::table_expandedColumnCount_setter(instance):
    original = instance.expandedColumnCount
    instance.expandedColumnCount = original
    assert instance.expandedColumnCount == original

@given(instance=SpreadsheetMLWorkbookProp::Table_strategy)
def test_spreadsheetmlworkbookprop::table_fullColumns_type(instance):
    assert isinstance(instance.fullColumns, str)


@given(instance=SpreadsheetMLWorkbookProp::Table_strategy)
def test_spreadsheetmlworkbookprop::table_fullColumns_setter(instance):
    original = instance.fullColumns
    instance.fullColumns = original
    assert instance.fullColumns == original

@given(instance=SpreadsheetMLWorkbookProp::Table_strategy)
def test_spreadsheetmlworkbookprop::table_expandedRowCount_type(instance):
    assert isinstance(instance.expandedRowCount, str)


@given(instance=SpreadsheetMLWorkbookProp::Table_strategy)
def test_spreadsheetmlworkbookprop::table_expandedRowCount_setter(instance):
    original = instance.expandedRowCount
    instance.expandedRowCount = original
    assert instance.expandedRowCount == original

@given(instance=SpreadsheetMLWorkbookProp::Table_strategy)
def test_spreadsheetmlworkbookprop::table_defaultRowHeight_type(instance):
    assert isinstance(instance.defaultRowHeight, str)


@given(instance=SpreadsheetMLWorkbookProp::Table_strategy)
def test_spreadsheetmlworkbookprop::table_defaultRowHeight_setter(instance):
    original = instance.defaultRowHeight
    instance.defaultRowHeight = original
    assert instance.defaultRowHeight == original

@given(instance=SpreadsheetMLWorkbookProp::Table_strategy)
def test_spreadsheetmlworkbookprop::table_defaultColumnWidth_type(instance):
    assert isinstance(instance.defaultColumnWidth, str)


@given(instance=SpreadsheetMLWorkbookProp::Table_strategy)
def test_spreadsheetmlworkbookprop::table_defaultColumnWidth_setter(instance):
    original = instance.defaultColumnWidth
    instance.defaultColumnWidth = original
    assert instance.defaultColumnWidth == original

@given(instance=SpreadsheetMLWorkbookProp::StyledElement_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworkbookprop::styledelement_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorkbookProp::StyledElement)

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

@given(instance=SpreadsheetMLWorkbookProp::Workbook_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworkbookprop::workbook_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorkbookProp::Workbook)

@given(instance=SmartTagType_strategy)
@settings(max_examples=50)
def test_smarttagtype_instantiation(instance):
    assert isinstance(instance, SmartTagType)

@given(instance=SpreadsheetMLWorkbookProp::Worksheet_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworkbookprop::worksheet_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorkbookProp::Worksheet)

@given(instance=SpreadsheetMLWorkbookProp::Worksheet_strategy)
def test_spreadsheetmlworkbookprop::worksheet_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SpreadsheetMLWorkbookProp::Worksheet_strategy)
def test_spreadsheetmlworkbookprop::worksheet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Worksheet_strategy)
@settings(max_examples=50)
def test_worksheet_instantiation(instance):
    assert isinstance(instance, Worksheet)

@given(instance=SpreadsheetMLWorkbookProp::SmartTagsCollection_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworkbookprop::smarttagscollection_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorkbookProp::SmartTagsCollection)

@given(instance=SmartTagsCollection_strategy)
@settings(max_examples=50)
def test_smarttagscollection_instantiation(instance):
    assert isinstance(instance, SmartTagsCollection)
