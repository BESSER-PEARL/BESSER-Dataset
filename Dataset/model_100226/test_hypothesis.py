import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Workbook,
    SpreadsheetMLBasicDef_DocumentPropertiesCollection,
    DateTimeType,
    SpreadsheetMLBasicDef_VersionType,
    ValueType,
    SpreadsheetMLBasicDef_BooleanValue,
    SpreadsheetMLBasicDef_ErrorValue,
    SpreadsheetMLBasicDef_StringValue,
    Data,
    SpreadsheetMLBasicDef_ValueType,
    SpreadsheetMLBasicDef_DateTimeType,
    SpreadsheetMLBasicDef_Comment,
    SpreadsheetMLBasicDef_Data,
    Comment,
    ColOrRowElement,
    SpreadsheetMLBasicDef_Column,
    TableElement,
    SpreadsheetMLBasicDef_Cell,
    SpreadsheetMLBasicDef_Row,
    Row,
    SpreadsheetMLBasicDef_ColOrRowElement,
    Table,
    SpreadsheetMLBasicDef_Worksheet,
    Column,
    StyledElement,
    SpreadsheetMLBasicDef_TableElement,
    SpreadsheetMLBasicDef_Table,
    SpreadsheetMLBasicDef_StyledElement,
    SpreadsheetMLBasicDef_Workbook,
    SmartTagType,
    Cell,
    Worksheet,
    DocumentPropertiesCollection,
    SmartTagsCollection,
    SpreadsheetMLBasicDef_SmartTagType,
    SpreadsheetMLBasicDef_SmartTagsCollection,
    SpreadsheetMLBasicDef_CustomDocumentPropertiesCollection,
    CustomDocumentPropertiesCollection,
    SpreadsheetMLBasicDef_CustomDocumentProperty,
    CustomDocumentProperty,
    VersionType,
    SpreadsheetMLBasicDef_DateTimeTypeValue,
    SpreadsheetMLBasicDef_NumberValue,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_workbook_is_not_abstract():
    assert not inspect.isabstract(Workbook)


def test_workbook_constructor_exists():
    assert callable(Workbook.__init__)


def test_workbook_constructor_args():
    sig = inspect.signature(Workbook.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlbasicdef_documentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLBasicDef_DocumentPropertiesCollection)


def test_spreadsheetmlbasicdef_documentpropertiescollection_constructor_exists():
    assert callable(SpreadsheetMLBasicDef_DocumentPropertiesCollection.__init__)


def test_spreadsheetmlbasicdef_documentpropertiescollection_constructor_args():
    sig = inspect.signature(SpreadsheetMLBasicDef_DocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "characters" in params, "Missing parameter 'characters'"
    assert "totalTime" in params, "Missing parameter 'totalTime'"
    assert "author" in params, "Missing parameter 'author'"
    assert "bytes" in params, "Missing parameter 'bytes'"
    assert "company" in params, "Missing parameter 'company'"
    assert "presentationFormat" in params, "Missing parameter 'presentationFormat'"
    assert "lastAuthor" in params, "Missing parameter 'lastAuthor'"
    assert "appName" in params, "Missing parameter 'appName'"
    assert "charactersWithSpaces" in params, "Missing parameter 'charactersWithSpaces'"
    assert "keywords" in params, "Missing parameter 'keywords'"
    assert "manager" in params, "Missing parameter 'manager'"
    assert "subject" in params, "Missing parameter 'subject'"
    assert "hyperlinkBase" in params, "Missing parameter 'hyperlinkBase'"
    assert "guid" in params, "Missing parameter 'guid'"
    assert "description" in params, "Missing parameter 'description'"
    assert "paragraphs" in params, "Missing parameter 'paragraphs'"
    assert "revision" in params, "Missing parameter 'revision'"
    assert "lines" in params, "Missing parameter 'lines'"
    assert "words" in params, "Missing parameter 'words'"
    assert "category" in params, "Missing parameter 'category'"
    assert "pages" in params, "Missing parameter 'pages'"

def test_spreadsheetmlbasicdef_documentpropertiescollection_has_title():
    assert hasattr(SpreadsheetMLBasicDef_DocumentPropertiesCollection, "title")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef_documentpropertiescollection_has_characters():
    assert hasattr(SpreadsheetMLBasicDef_DocumentPropertiesCollection, "characters")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "characters" in klass.__dict__:
            descriptor = klass.__dict__["characters"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef_documentpropertiescollection_has_totalTime():
    assert hasattr(SpreadsheetMLBasicDef_DocumentPropertiesCollection, "totalTime")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "totalTime" in klass.__dict__:
            descriptor = klass.__dict__["totalTime"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef_documentpropertiescollection_has_author():
    assert hasattr(SpreadsheetMLBasicDef_DocumentPropertiesCollection, "author")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef_documentpropertiescollection_has_bytes():
    assert hasattr(SpreadsheetMLBasicDef_DocumentPropertiesCollection, "bytes")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "bytes" in klass.__dict__:
            descriptor = klass.__dict__["bytes"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef_documentpropertiescollection_has_company():
    assert hasattr(SpreadsheetMLBasicDef_DocumentPropertiesCollection, "company")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "company" in klass.__dict__:
            descriptor = klass.__dict__["company"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef_documentpropertiescollection_has_presentationFormat():
    assert hasattr(SpreadsheetMLBasicDef_DocumentPropertiesCollection, "presentationFormat")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "presentationFormat" in klass.__dict__:
            descriptor = klass.__dict__["presentationFormat"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef_documentpropertiescollection_has_lastAuthor():
    assert hasattr(SpreadsheetMLBasicDef_DocumentPropertiesCollection, "lastAuthor")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "lastAuthor" in klass.__dict__:
            descriptor = klass.__dict__["lastAuthor"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef_documentpropertiescollection_has_appName():
    assert hasattr(SpreadsheetMLBasicDef_DocumentPropertiesCollection, "appName")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "appName" in klass.__dict__:
            descriptor = klass.__dict__["appName"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef_documentpropertiescollection_has_charactersWithSpaces():
    assert hasattr(SpreadsheetMLBasicDef_DocumentPropertiesCollection, "charactersWithSpaces")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "charactersWithSpaces" in klass.__dict__:
            descriptor = klass.__dict__["charactersWithSpaces"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef_documentpropertiescollection_has_keywords():
    assert hasattr(SpreadsheetMLBasicDef_DocumentPropertiesCollection, "keywords")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "keywords" in klass.__dict__:
            descriptor = klass.__dict__["keywords"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef_documentpropertiescollection_has_manager():
    assert hasattr(SpreadsheetMLBasicDef_DocumentPropertiesCollection, "manager")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "manager" in klass.__dict__:
            descriptor = klass.__dict__["manager"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef_documentpropertiescollection_has_subject():
    assert hasattr(SpreadsheetMLBasicDef_DocumentPropertiesCollection, "subject")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "subject" in klass.__dict__:
            descriptor = klass.__dict__["subject"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef_documentpropertiescollection_has_hyperlinkBase():
    assert hasattr(SpreadsheetMLBasicDef_DocumentPropertiesCollection, "hyperlinkBase")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "hyperlinkBase" in klass.__dict__:
            descriptor = klass.__dict__["hyperlinkBase"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef_documentpropertiescollection_has_guid():
    assert hasattr(SpreadsheetMLBasicDef_DocumentPropertiesCollection, "guid")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "guid" in klass.__dict__:
            descriptor = klass.__dict__["guid"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef_documentpropertiescollection_has_description():
    assert hasattr(SpreadsheetMLBasicDef_DocumentPropertiesCollection, "description")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef_documentpropertiescollection_has_paragraphs():
    assert hasattr(SpreadsheetMLBasicDef_DocumentPropertiesCollection, "paragraphs")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "paragraphs" in klass.__dict__:
            descriptor = klass.__dict__["paragraphs"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef_documentpropertiescollection_has_revision():
    assert hasattr(SpreadsheetMLBasicDef_DocumentPropertiesCollection, "revision")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "revision" in klass.__dict__:
            descriptor = klass.__dict__["revision"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef_documentpropertiescollection_has_lines():
    assert hasattr(SpreadsheetMLBasicDef_DocumentPropertiesCollection, "lines")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "lines" in klass.__dict__:
            descriptor = klass.__dict__["lines"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef_documentpropertiescollection_has_words():
    assert hasattr(SpreadsheetMLBasicDef_DocumentPropertiesCollection, "words")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "words" in klass.__dict__:
            descriptor = klass.__dict__["words"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef_documentpropertiescollection_has_category():
    assert hasattr(SpreadsheetMLBasicDef_DocumentPropertiesCollection, "category")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef_documentpropertiescollection_has_pages():
    assert hasattr(SpreadsheetMLBasicDef_DocumentPropertiesCollection, "pages")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)



def test_datetimetype_is_not_abstract():
    assert not inspect.isabstract(DateTimeType)


def test_datetimetype_constructor_exists():
    assert callable(DateTimeType.__init__)


def test_datetimetype_constructor_args():
    sig = inspect.signature(DateTimeType.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlbasicdef_versiontype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLBasicDef_VersionType)


def test_spreadsheetmlbasicdef_versiontype_constructor_exists():
    assert callable(SpreadsheetMLBasicDef_VersionType.__init__)


def test_spreadsheetmlbasicdef_versiontype_constructor_args():
    sig = inspect.signature(SpreadsheetMLBasicDef_VersionType.__init__)
    params = list(sig.parameters.keys())
    assert "n" in params, "Missing parameter 'n'"
    assert "nn" in params, "Missing parameter 'nn'"

def test_spreadsheetmlbasicdef_versiontype_has_n():
    assert hasattr(SpreadsheetMLBasicDef_VersionType, "n")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_VersionType.__mro__:
        if "n" in klass.__dict__:
            descriptor = klass.__dict__["n"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef_versiontype_has_nn():
    assert hasattr(SpreadsheetMLBasicDef_VersionType, "nn")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_VersionType.__mro__:
        if "nn" in klass.__dict__:
            descriptor = klass.__dict__["nn"]
            break
    assert isinstance(descriptor, property)



def test_valuetype_is_not_abstract():
    assert not inspect.isabstract(ValueType)


def test_valuetype_constructor_exists():
    assert callable(ValueType.__init__)


def test_valuetype_constructor_args():
    sig = inspect.signature(ValueType.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlbasicdef_booleanvalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLBasicDef_BooleanValue)


def test_spreadsheetmlbasicdef_booleanvalue_constructor_exists():
    assert callable(SpreadsheetMLBasicDef_BooleanValue.__init__)


def test_spreadsheetmlbasicdef_booleanvalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLBasicDef_BooleanValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_spreadsheetmlbasicdef_booleanvalue_has_value():
    assert hasattr(SpreadsheetMLBasicDef_BooleanValue, "value")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_BooleanValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlbasicdef_errorvalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLBasicDef_ErrorValue)


def test_spreadsheetmlbasicdef_errorvalue_constructor_exists():
    assert callable(SpreadsheetMLBasicDef_ErrorValue.__init__)


def test_spreadsheetmlbasicdef_errorvalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLBasicDef_ErrorValue.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlbasicdef_stringvalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLBasicDef_StringValue)


def test_spreadsheetmlbasicdef_stringvalue_constructor_exists():
    assert callable(SpreadsheetMLBasicDef_StringValue.__init__)


def test_spreadsheetmlbasicdef_stringvalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLBasicDef_StringValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_spreadsheetmlbasicdef_stringvalue_has_value():
    assert hasattr(SpreadsheetMLBasicDef_StringValue, "value")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_StringValue.__mro__:
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



def test_spreadsheetmlbasicdef_valuetype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLBasicDef_ValueType)


def test_spreadsheetmlbasicdef_valuetype_constructor_exists():
    assert callable(SpreadsheetMLBasicDef_ValueType.__init__)


def test_spreadsheetmlbasicdef_valuetype_constructor_args():
    sig = inspect.signature(SpreadsheetMLBasicDef_ValueType.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlbasicdef_datetimetype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLBasicDef_DateTimeType)


def test_spreadsheetmlbasicdef_datetimetype_constructor_exists():
    assert callable(SpreadsheetMLBasicDef_DateTimeType.__init__)


def test_spreadsheetmlbasicdef_datetimetype_constructor_args():
    sig = inspect.signature(SpreadsheetMLBasicDef_DateTimeType.__init__)
    params = list(sig.parameters.keys())
    assert "second" in params, "Missing parameter 'second'"
    assert "day" in params, "Missing parameter 'day'"
    assert "minute" in params, "Missing parameter 'minute'"
    assert "hour" in params, "Missing parameter 'hour'"
    assert "year" in params, "Missing parameter 'year'"
    assert "month" in params, "Missing parameter 'month'"

def test_spreadsheetmlbasicdef_datetimetype_has_second():
    assert hasattr(SpreadsheetMLBasicDef_DateTimeType, "second")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_DateTimeType.__mro__:
        if "second" in klass.__dict__:
            descriptor = klass.__dict__["second"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef_datetimetype_has_day():
    assert hasattr(SpreadsheetMLBasicDef_DateTimeType, "day")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_DateTimeType.__mro__:
        if "day" in klass.__dict__:
            descriptor = klass.__dict__["day"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef_datetimetype_has_minute():
    assert hasattr(SpreadsheetMLBasicDef_DateTimeType, "minute")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_DateTimeType.__mro__:
        if "minute" in klass.__dict__:
            descriptor = klass.__dict__["minute"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef_datetimetype_has_hour():
    assert hasattr(SpreadsheetMLBasicDef_DateTimeType, "hour")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_DateTimeType.__mro__:
        if "hour" in klass.__dict__:
            descriptor = klass.__dict__["hour"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef_datetimetype_has_year():
    assert hasattr(SpreadsheetMLBasicDef_DateTimeType, "year")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_DateTimeType.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef_datetimetype_has_month():
    assert hasattr(SpreadsheetMLBasicDef_DateTimeType, "month")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_DateTimeType.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlbasicdef_comment_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLBasicDef_Comment)


def test_spreadsheetmlbasicdef_comment_constructor_exists():
    assert callable(SpreadsheetMLBasicDef_Comment.__init__)


def test_spreadsheetmlbasicdef_comment_constructor_args():
    sig = inspect.signature(SpreadsheetMLBasicDef_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "showAlways" in params, "Missing parameter 'showAlways'"
    assert "author" in params, "Missing parameter 'author'"

def test_spreadsheetmlbasicdef_comment_has_showAlways():
    assert hasattr(SpreadsheetMLBasicDef_Comment, "showAlways")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_Comment.__mro__:
        if "showAlways" in klass.__dict__:
            descriptor = klass.__dict__["showAlways"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef_comment_has_author():
    assert hasattr(SpreadsheetMLBasicDef_Comment, "author")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_Comment.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlbasicdef_data_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLBasicDef_Data)


def test_spreadsheetmlbasicdef_data_constructor_exists():
    assert callable(SpreadsheetMLBasicDef_Data.__init__)


def test_spreadsheetmlbasicdef_data_constructor_args():
    sig = inspect.signature(SpreadsheetMLBasicDef_Data.__init__)
    params = list(sig.parameters.keys())



def test_comment_is_not_abstract():
    assert not inspect.isabstract(Comment)


def test_comment_constructor_exists():
    assert callable(Comment.__init__)


def test_comment_constructor_args():
    sig = inspect.signature(Comment.__init__)
    params = list(sig.parameters.keys())



def test_colorrowelement_is_not_abstract():
    assert not inspect.isabstract(ColOrRowElement)


def test_colorrowelement_constructor_exists():
    assert callable(ColOrRowElement.__init__)


def test_colorrowelement_constructor_args():
    sig = inspect.signature(ColOrRowElement.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlbasicdef_column_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLBasicDef_Column)


def test_spreadsheetmlbasicdef_column_constructor_exists():
    assert callable(SpreadsheetMLBasicDef_Column.__init__)


def test_spreadsheetmlbasicdef_column_constructor_args():
    sig = inspect.signature(SpreadsheetMLBasicDef_Column.__init__)
    params = list(sig.parameters.keys())
    assert "autoFitWidth" in params, "Missing parameter 'autoFitWidth'"
    assert "width" in params, "Missing parameter 'width'"

def test_spreadsheetmlbasicdef_column_has_autoFitWidth():
    assert hasattr(SpreadsheetMLBasicDef_Column, "autoFitWidth")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_Column.__mro__:
        if "autoFitWidth" in klass.__dict__:
            descriptor = klass.__dict__["autoFitWidth"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef_column_has_width():
    assert hasattr(SpreadsheetMLBasicDef_Column, "width")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_Column.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_tableelement_is_not_abstract():
    assert not inspect.isabstract(TableElement)


def test_tableelement_constructor_exists():
    assert callable(TableElement.__init__)


def test_tableelement_constructor_args():
    sig = inspect.signature(TableElement.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlbasicdef_cell_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLBasicDef_Cell)


def test_spreadsheetmlbasicdef_cell_constructor_exists():
    assert callable(SpreadsheetMLBasicDef_Cell.__init__)


def test_spreadsheetmlbasicdef_cell_constructor_args():
    sig = inspect.signature(SpreadsheetMLBasicDef_Cell.__init__)
    params = list(sig.parameters.keys())
    assert "mergeDown" in params, "Missing parameter 'mergeDown'"
    assert "formula" in params, "Missing parameter 'formula'"
    assert "mergeAcross" in params, "Missing parameter 'mergeAcross'"
    assert "arrayRange" in params, "Missing parameter 'arrayRange'"
    assert "hRef" in params, "Missing parameter 'hRef'"

def test_spreadsheetmlbasicdef_cell_has_mergeDown():
    assert hasattr(SpreadsheetMLBasicDef_Cell, "mergeDown")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_Cell.__mro__:
        if "mergeDown" in klass.__dict__:
            descriptor = klass.__dict__["mergeDown"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef_cell_has_formula():
    assert hasattr(SpreadsheetMLBasicDef_Cell, "formula")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_Cell.__mro__:
        if "formula" in klass.__dict__:
            descriptor = klass.__dict__["formula"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef_cell_has_mergeAcross():
    assert hasattr(SpreadsheetMLBasicDef_Cell, "mergeAcross")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_Cell.__mro__:
        if "mergeAcross" in klass.__dict__:
            descriptor = klass.__dict__["mergeAcross"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef_cell_has_arrayRange():
    assert hasattr(SpreadsheetMLBasicDef_Cell, "arrayRange")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_Cell.__mro__:
        if "arrayRange" in klass.__dict__:
            descriptor = klass.__dict__["arrayRange"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef_cell_has_hRef():
    assert hasattr(SpreadsheetMLBasicDef_Cell, "hRef")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_Cell.__mro__:
        if "hRef" in klass.__dict__:
            descriptor = klass.__dict__["hRef"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlbasicdef_row_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLBasicDef_Row)


def test_spreadsheetmlbasicdef_row_constructor_exists():
    assert callable(SpreadsheetMLBasicDef_Row.__init__)


def test_spreadsheetmlbasicdef_row_constructor_args():
    sig = inspect.signature(SpreadsheetMLBasicDef_Row.__init__)
    params = list(sig.parameters.keys())
    assert "autoFitHeight" in params, "Missing parameter 'autoFitHeight'"
    assert "height" in params, "Missing parameter 'height'"

def test_spreadsheetmlbasicdef_row_has_autoFitHeight():
    assert hasattr(SpreadsheetMLBasicDef_Row, "autoFitHeight")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_Row.__mro__:
        if "autoFitHeight" in klass.__dict__:
            descriptor = klass.__dict__["autoFitHeight"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef_row_has_height():
    assert hasattr(SpreadsheetMLBasicDef_Row, "height")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_Row.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_row_is_not_abstract():
    assert not inspect.isabstract(Row)


def test_row_constructor_exists():
    assert callable(Row.__init__)


def test_row_constructor_args():
    sig = inspect.signature(Row.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlbasicdef_colorrowelement_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLBasicDef_ColOrRowElement)


def test_spreadsheetmlbasicdef_colorrowelement_constructor_exists():
    assert callable(SpreadsheetMLBasicDef_ColOrRowElement.__init__)


def test_spreadsheetmlbasicdef_colorrowelement_constructor_args():
    sig = inspect.signature(SpreadsheetMLBasicDef_ColOrRowElement.__init__)
    params = list(sig.parameters.keys())
    assert "span" in params, "Missing parameter 'span'"
    assert "hidden" in params, "Missing parameter 'hidden'"

def test_spreadsheetmlbasicdef_colorrowelement_has_span():
    assert hasattr(SpreadsheetMLBasicDef_ColOrRowElement, "span")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_ColOrRowElement.__mro__:
        if "span" in klass.__dict__:
            descriptor = klass.__dict__["span"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef_colorrowelement_has_hidden():
    assert hasattr(SpreadsheetMLBasicDef_ColOrRowElement, "hidden")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_ColOrRowElement.__mro__:
        if "hidden" in klass.__dict__:
            descriptor = klass.__dict__["hidden"]
            break
    assert isinstance(descriptor, property)



def test_table_is_not_abstract():
    assert not inspect.isabstract(Table)


def test_table_constructor_exists():
    assert callable(Table.__init__)


def test_table_constructor_args():
    sig = inspect.signature(Table.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlbasicdef_worksheet_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLBasicDef_Worksheet)


def test_spreadsheetmlbasicdef_worksheet_constructor_exists():
    assert callable(SpreadsheetMLBasicDef_Worksheet.__init__)


def test_spreadsheetmlbasicdef_worksheet_constructor_args():
    sig = inspect.signature(SpreadsheetMLBasicDef_Worksheet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_spreadsheetmlbasicdef_worksheet_has_name():
    assert hasattr(SpreadsheetMLBasicDef_Worksheet, "name")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_Worksheet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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



def test_spreadsheetmlbasicdef_tableelement_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLBasicDef_TableElement)


def test_spreadsheetmlbasicdef_tableelement_constructor_exists():
    assert callable(SpreadsheetMLBasicDef_TableElement.__init__)


def test_spreadsheetmlbasicdef_tableelement_constructor_args():
    sig = inspect.signature(SpreadsheetMLBasicDef_TableElement.__init__)
    params = list(sig.parameters.keys())
    assert "index" in params, "Missing parameter 'index'"

def test_spreadsheetmlbasicdef_tableelement_has_index():
    assert hasattr(SpreadsheetMLBasicDef_TableElement, "index")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_TableElement.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlbasicdef_table_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLBasicDef_Table)


def test_spreadsheetmlbasicdef_table_constructor_exists():
    assert callable(SpreadsheetMLBasicDef_Table.__init__)


def test_spreadsheetmlbasicdef_table_constructor_args():
    sig = inspect.signature(SpreadsheetMLBasicDef_Table.__init__)
    params = list(sig.parameters.keys())
    assert "topCell" in params, "Missing parameter 'topCell'"
    assert "fullRows" in params, "Missing parameter 'fullRows'"
    assert "defaultColumnWidth" in params, "Missing parameter 'defaultColumnWidth'"
    assert "expandedRowCount" in params, "Missing parameter 'expandedRowCount'"
    assert "defaultRowHeight" in params, "Missing parameter 'defaultRowHeight'"
    assert "fullColumns" in params, "Missing parameter 'fullColumns'"
    assert "expandedColumnCount" in params, "Missing parameter 'expandedColumnCount'"
    assert "leftCell" in params, "Missing parameter 'leftCell'"

def test_spreadsheetmlbasicdef_table_has_topCell():
    assert hasattr(SpreadsheetMLBasicDef_Table, "topCell")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_Table.__mro__:
        if "topCell" in klass.__dict__:
            descriptor = klass.__dict__["topCell"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef_table_has_fullRows():
    assert hasattr(SpreadsheetMLBasicDef_Table, "fullRows")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_Table.__mro__:
        if "fullRows" in klass.__dict__:
            descriptor = klass.__dict__["fullRows"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef_table_has_defaultColumnWidth():
    assert hasattr(SpreadsheetMLBasicDef_Table, "defaultColumnWidth")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_Table.__mro__:
        if "defaultColumnWidth" in klass.__dict__:
            descriptor = klass.__dict__["defaultColumnWidth"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef_table_has_expandedRowCount():
    assert hasattr(SpreadsheetMLBasicDef_Table, "expandedRowCount")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_Table.__mro__:
        if "expandedRowCount" in klass.__dict__:
            descriptor = klass.__dict__["expandedRowCount"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef_table_has_defaultRowHeight():
    assert hasattr(SpreadsheetMLBasicDef_Table, "defaultRowHeight")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_Table.__mro__:
        if "defaultRowHeight" in klass.__dict__:
            descriptor = klass.__dict__["defaultRowHeight"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef_table_has_fullColumns():
    assert hasattr(SpreadsheetMLBasicDef_Table, "fullColumns")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_Table.__mro__:
        if "fullColumns" in klass.__dict__:
            descriptor = klass.__dict__["fullColumns"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef_table_has_expandedColumnCount():
    assert hasattr(SpreadsheetMLBasicDef_Table, "expandedColumnCount")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_Table.__mro__:
        if "expandedColumnCount" in klass.__dict__:
            descriptor = klass.__dict__["expandedColumnCount"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef_table_has_leftCell():
    assert hasattr(SpreadsheetMLBasicDef_Table, "leftCell")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_Table.__mro__:
        if "leftCell" in klass.__dict__:
            descriptor = klass.__dict__["leftCell"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlbasicdef_styledelement_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLBasicDef_StyledElement)


def test_spreadsheetmlbasicdef_styledelement_constructor_exists():
    assert callable(SpreadsheetMLBasicDef_StyledElement.__init__)


def test_spreadsheetmlbasicdef_styledelement_constructor_args():
    sig = inspect.signature(SpreadsheetMLBasicDef_StyledElement.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlbasicdef_workbook_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLBasicDef_Workbook)


def test_spreadsheetmlbasicdef_workbook_constructor_exists():
    assert callable(SpreadsheetMLBasicDef_Workbook.__init__)


def test_spreadsheetmlbasicdef_workbook_constructor_args():
    sig = inspect.signature(SpreadsheetMLBasicDef_Workbook.__init__)
    params = list(sig.parameters.keys())



def test_smarttagtype_is_not_abstract():
    assert not inspect.isabstract(SmartTagType)


def test_smarttagtype_constructor_exists():
    assert callable(SmartTagType.__init__)


def test_smarttagtype_constructor_args():
    sig = inspect.signature(SmartTagType.__init__)
    params = list(sig.parameters.keys())



def test_cell_is_not_abstract():
    assert not inspect.isabstract(Cell)


def test_cell_constructor_exists():
    assert callable(Cell.__init__)


def test_cell_constructor_args():
    sig = inspect.signature(Cell.__init__)
    params = list(sig.parameters.keys())



def test_worksheet_is_not_abstract():
    assert not inspect.isabstract(Worksheet)


def test_worksheet_constructor_exists():
    assert callable(Worksheet.__init__)


def test_worksheet_constructor_args():
    sig = inspect.signature(Worksheet.__init__)
    params = list(sig.parameters.keys())



def test_documentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(DocumentPropertiesCollection)


def test_documentpropertiescollection_constructor_exists():
    assert callable(DocumentPropertiesCollection.__init__)


def test_documentpropertiescollection_constructor_args():
    sig = inspect.signature(DocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())



def test_smarttagscollection_is_not_abstract():
    assert not inspect.isabstract(SmartTagsCollection)


def test_smarttagscollection_constructor_exists():
    assert callable(SmartTagsCollection.__init__)


def test_smarttagscollection_constructor_args():
    sig = inspect.signature(SmartTagsCollection.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlbasicdef_smarttagtype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLBasicDef_SmartTagType)


def test_spreadsheetmlbasicdef_smarttagtype_constructor_exists():
    assert callable(SpreadsheetMLBasicDef_SmartTagType.__init__)


def test_spreadsheetmlbasicdef_smarttagtype_constructor_args():
    sig = inspect.signature(SpreadsheetMLBasicDef_SmartTagType.__init__)
    params = list(sig.parameters.keys())
    assert "namespaceuri" in params, "Missing parameter 'namespaceuri'"
    assert "url" in params, "Missing parameter 'url'"
    assert "name" in params, "Missing parameter 'name'"

def test_spreadsheetmlbasicdef_smarttagtype_has_namespaceuri():
    assert hasattr(SpreadsheetMLBasicDef_SmartTagType, "namespaceuri")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_SmartTagType.__mro__:
        if "namespaceuri" in klass.__dict__:
            descriptor = klass.__dict__["namespaceuri"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef_smarttagtype_has_url():
    assert hasattr(SpreadsheetMLBasicDef_SmartTagType, "url")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_SmartTagType.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef_smarttagtype_has_name():
    assert hasattr(SpreadsheetMLBasicDef_SmartTagType, "name")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_SmartTagType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlbasicdef_smarttagscollection_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLBasicDef_SmartTagsCollection)


def test_spreadsheetmlbasicdef_smarttagscollection_constructor_exists():
    assert callable(SpreadsheetMLBasicDef_SmartTagsCollection.__init__)


def test_spreadsheetmlbasicdef_smarttagscollection_constructor_args():
    sig = inspect.signature(SpreadsheetMLBasicDef_SmartTagsCollection.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlbasicdef_customdocumentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLBasicDef_CustomDocumentPropertiesCollection)


def test_spreadsheetmlbasicdef_customdocumentpropertiescollection_constructor_exists():
    assert callable(SpreadsheetMLBasicDef_CustomDocumentPropertiesCollection.__init__)


def test_spreadsheetmlbasicdef_customdocumentpropertiescollection_constructor_args():
    sig = inspect.signature(SpreadsheetMLBasicDef_CustomDocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())



def test_customdocumentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(CustomDocumentPropertiesCollection)


def test_customdocumentpropertiescollection_constructor_exists():
    assert callable(CustomDocumentPropertiesCollection.__init__)


def test_customdocumentpropertiescollection_constructor_args():
    sig = inspect.signature(CustomDocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlbasicdef_customdocumentproperty_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLBasicDef_CustomDocumentProperty)


def test_spreadsheetmlbasicdef_customdocumentproperty_constructor_exists():
    assert callable(SpreadsheetMLBasicDef_CustomDocumentProperty.__init__)


def test_spreadsheetmlbasicdef_customdocumentproperty_constructor_args():
    sig = inspect.signature(SpreadsheetMLBasicDef_CustomDocumentProperty.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_spreadsheetmlbasicdef_customdocumentproperty_has_name():
    assert hasattr(SpreadsheetMLBasicDef_CustomDocumentProperty, "name")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_CustomDocumentProperty.__mro__:
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



def test_spreadsheetmlbasicdef_datetimetypevalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLBasicDef_DateTimeTypeValue)


def test_spreadsheetmlbasicdef_datetimetypevalue_constructor_exists():
    assert callable(SpreadsheetMLBasicDef_DateTimeTypeValue.__init__)


def test_spreadsheetmlbasicdef_datetimetypevalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLBasicDef_DateTimeTypeValue.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlbasicdef_numbervalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLBasicDef_NumberValue)


def test_spreadsheetmlbasicdef_numbervalue_constructor_exists():
    assert callable(SpreadsheetMLBasicDef_NumberValue.__init__)


def test_spreadsheetmlbasicdef_numbervalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLBasicDef_NumberValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_spreadsheetmlbasicdef_numbervalue_has_value():
    assert hasattr(SpreadsheetMLBasicDef_NumberValue, "value")
    descriptor = None
    for klass in SpreadsheetMLBasicDef_NumberValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)


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
Workbook_strategy = st.builds(
    Workbook,
)
SpreadsheetMLBasicDef_DocumentPropertiesCollection_strategy = st.builds(
    SpreadsheetMLBasicDef_DocumentPropertiesCollection,
    title=
        safe_text,
    characters=
        safe_text,
    totalTime=
        safe_text,
    author=
        safe_text,
    bytes=
        safe_text,
    company=
        safe_text,
    presentationFormat=
        safe_text,
    lastAuthor=
        safe_text,
    appName=
        safe_text,
    charactersWithSpaces=
        safe_text,
    keywords=
        safe_text,
    manager=
        safe_text,
    subject=
        safe_text,
    hyperlinkBase=
        safe_text,
    guid=
        safe_text,
    description=
        safe_text,
    paragraphs=
        safe_text,
    revision=
        safe_text,
    lines=
        safe_text,
    words=
        safe_text,
    category=
        safe_text,
    pages=
        safe_text
)
DateTimeType_strategy = st.builds(
    DateTimeType,
)
SpreadsheetMLBasicDef_VersionType_strategy = st.builds(
    SpreadsheetMLBasicDef_VersionType,
    n=
        safe_text,
    nn=
        safe_text
)
ValueType_strategy = st.builds(
    ValueType,
)
SpreadsheetMLBasicDef_BooleanValue_strategy = st.builds(
    SpreadsheetMLBasicDef_BooleanValue,
    value=
        safe_text
)
SpreadsheetMLBasicDef_ErrorValue_strategy = st.builds(
    SpreadsheetMLBasicDef_ErrorValue,
)
SpreadsheetMLBasicDef_StringValue_strategy = st.builds(
    SpreadsheetMLBasicDef_StringValue,
    value=
        safe_text
)
Data_strategy = st.builds(
    Data,
)
SpreadsheetMLBasicDef_ValueType_strategy = st.builds(
    SpreadsheetMLBasicDef_ValueType,
)
SpreadsheetMLBasicDef_DateTimeType_strategy = st.builds(
    SpreadsheetMLBasicDef_DateTimeType,
    second=
        safe_text,
    day=
        safe_text,
    minute=
        safe_text,
    hour=
        safe_text,
    year=
        safe_text,
    month=
        safe_text
)
SpreadsheetMLBasicDef_Comment_strategy = st.builds(
    SpreadsheetMLBasicDef_Comment,
    showAlways=
        safe_text,
    author=
        safe_text
)
SpreadsheetMLBasicDef_Data_strategy = st.builds(
    SpreadsheetMLBasicDef_Data,
)
Comment_strategy = st.builds(
    Comment,
)
ColOrRowElement_strategy = st.builds(
    ColOrRowElement,
)
SpreadsheetMLBasicDef_Column_strategy = st.builds(
    SpreadsheetMLBasicDef_Column,
    autoFitWidth=
        safe_text,
    width=
        safe_text
)
TableElement_strategy = st.builds(
    TableElement,
)
SpreadsheetMLBasicDef_Cell_strategy = st.builds(
    SpreadsheetMLBasicDef_Cell,
    mergeDown=
        safe_text,
    formula=
        safe_text,
    mergeAcross=
        safe_text,
    arrayRange=
        safe_text,
    hRef=
        safe_text
)
SpreadsheetMLBasicDef_Row_strategy = st.builds(
    SpreadsheetMLBasicDef_Row,
    autoFitHeight=
        safe_text,
    height=
        safe_text
)
Row_strategy = st.builds(
    Row,
)
SpreadsheetMLBasicDef_ColOrRowElement_strategy = st.builds(
    SpreadsheetMLBasicDef_ColOrRowElement,
    span=
        safe_text,
    hidden=
        safe_text
)
Table_strategy = st.builds(
    Table,
)
SpreadsheetMLBasicDef_Worksheet_strategy = st.builds(
    SpreadsheetMLBasicDef_Worksheet,
    name=
        safe_text
)
Column_strategy = st.builds(
    Column,
)
StyledElement_strategy = st.builds(
    StyledElement,
)
SpreadsheetMLBasicDef_TableElement_strategy = st.builds(
    SpreadsheetMLBasicDef_TableElement,
    index=
        safe_text
)
SpreadsheetMLBasicDef_Table_strategy = st.builds(
    SpreadsheetMLBasicDef_Table,
    topCell=
        safe_text,
    fullRows=
        safe_text,
    defaultColumnWidth=
        safe_text,
    expandedRowCount=
        safe_text,
    defaultRowHeight=
        safe_text,
    fullColumns=
        safe_text,
    expandedColumnCount=
        safe_text,
    leftCell=
        safe_text
)
SpreadsheetMLBasicDef_StyledElement_strategy = st.builds(
    SpreadsheetMLBasicDef_StyledElement,
)
SpreadsheetMLBasicDef_Workbook_strategy = st.builds(
    SpreadsheetMLBasicDef_Workbook,
)
SmartTagType_strategy = st.builds(
    SmartTagType,
)
Cell_strategy = st.builds(
    Cell,
)
Worksheet_strategy = st.builds(
    Worksheet,
)
DocumentPropertiesCollection_strategy = st.builds(
    DocumentPropertiesCollection,
)
SmartTagsCollection_strategy = st.builds(
    SmartTagsCollection,
)
SpreadsheetMLBasicDef_SmartTagType_strategy = st.builds(
    SpreadsheetMLBasicDef_SmartTagType,
    namespaceuri=
        safe_text,
    url=
        safe_text,
    name=
        safe_text
)
SpreadsheetMLBasicDef_SmartTagsCollection_strategy = st.builds(
    SpreadsheetMLBasicDef_SmartTagsCollection,
)
SpreadsheetMLBasicDef_CustomDocumentPropertiesCollection_strategy = st.builds(
    SpreadsheetMLBasicDef_CustomDocumentPropertiesCollection,
)
CustomDocumentPropertiesCollection_strategy = st.builds(
    CustomDocumentPropertiesCollection,
)
SpreadsheetMLBasicDef_CustomDocumentProperty_strategy = st.builds(
    SpreadsheetMLBasicDef_CustomDocumentProperty,
    name=
        safe_text
)
CustomDocumentProperty_strategy = st.builds(
    CustomDocumentProperty,
)
VersionType_strategy = st.builds(
    VersionType,
)
SpreadsheetMLBasicDef_DateTimeTypeValue_strategy = st.builds(
    SpreadsheetMLBasicDef_DateTimeTypeValue,
)
SpreadsheetMLBasicDef_NumberValue_strategy = st.builds(
    SpreadsheetMLBasicDef_NumberValue,
    value=
        safe_text
)

@given(instance=Workbook_strategy)
@settings(max_examples=50)
def test_workbook_instantiation(instance):
    assert isinstance(instance, Workbook)

@given(instance=SpreadsheetMLBasicDef_DocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_spreadsheetmlbasicdef_documentpropertiescollection_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLBasicDef_DocumentPropertiesCollection)



@given(instance=SpreadsheetMLBasicDef_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef_documentpropertiescollection_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=SpreadsheetMLBasicDef_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef_documentpropertiescollection_characters_setter(instance):
    original = instance.characters
    instance.characters = original
    assert instance.characters == original



@given(instance=SpreadsheetMLBasicDef_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef_documentpropertiescollection_totalTime_setter(instance):
    original = instance.totalTime
    instance.totalTime = original
    assert instance.totalTime == original



@given(instance=SpreadsheetMLBasicDef_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef_documentpropertiescollection_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=SpreadsheetMLBasicDef_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef_documentpropertiescollection_bytes_setter(instance):
    original = instance.bytes
    instance.bytes = original
    assert instance.bytes == original



@given(instance=SpreadsheetMLBasicDef_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef_documentpropertiescollection_company_setter(instance):
    original = instance.company
    instance.company = original
    assert instance.company == original



@given(instance=SpreadsheetMLBasicDef_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef_documentpropertiescollection_presentationFormat_setter(instance):
    original = instance.presentationFormat
    instance.presentationFormat = original
    assert instance.presentationFormat == original



@given(instance=SpreadsheetMLBasicDef_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef_documentpropertiescollection_lastAuthor_setter(instance):
    original = instance.lastAuthor
    instance.lastAuthor = original
    assert instance.lastAuthor == original



@given(instance=SpreadsheetMLBasicDef_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef_documentpropertiescollection_appName_setter(instance):
    original = instance.appName
    instance.appName = original
    assert instance.appName == original



@given(instance=SpreadsheetMLBasicDef_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef_documentpropertiescollection_charactersWithSpaces_setter(instance):
    original = instance.charactersWithSpaces
    instance.charactersWithSpaces = original
    assert instance.charactersWithSpaces == original



@given(instance=SpreadsheetMLBasicDef_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef_documentpropertiescollection_keywords_setter(instance):
    original = instance.keywords
    instance.keywords = original
    assert instance.keywords == original



@given(instance=SpreadsheetMLBasicDef_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef_documentpropertiescollection_manager_setter(instance):
    original = instance.manager
    instance.manager = original
    assert instance.manager == original



@given(instance=SpreadsheetMLBasicDef_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef_documentpropertiescollection_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original



@given(instance=SpreadsheetMLBasicDef_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef_documentpropertiescollection_hyperlinkBase_setter(instance):
    original = instance.hyperlinkBase
    instance.hyperlinkBase = original
    assert instance.hyperlinkBase == original



@given(instance=SpreadsheetMLBasicDef_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef_documentpropertiescollection_guid_setter(instance):
    original = instance.guid
    instance.guid = original
    assert instance.guid == original



@given(instance=SpreadsheetMLBasicDef_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef_documentpropertiescollection_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=SpreadsheetMLBasicDef_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef_documentpropertiescollection_paragraphs_setter(instance):
    original = instance.paragraphs
    instance.paragraphs = original
    assert instance.paragraphs == original



@given(instance=SpreadsheetMLBasicDef_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef_documentpropertiescollection_revision_setter(instance):
    original = instance.revision
    instance.revision = original
    assert instance.revision == original



@given(instance=SpreadsheetMLBasicDef_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef_documentpropertiescollection_lines_setter(instance):
    original = instance.lines
    instance.lines = original
    assert instance.lines == original



@given(instance=SpreadsheetMLBasicDef_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef_documentpropertiescollection_words_setter(instance):
    original = instance.words
    instance.words = original
    assert instance.words == original



@given(instance=SpreadsheetMLBasicDef_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef_documentpropertiescollection_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original



@given(instance=SpreadsheetMLBasicDef_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef_documentpropertiescollection_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=DateTimeType_strategy)
@settings(max_examples=50)
def test_datetimetype_instantiation(instance):
    assert isinstance(instance, DateTimeType)

@given(instance=SpreadsheetMLBasicDef_VersionType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlbasicdef_versiontype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLBasicDef_VersionType)



@given(instance=SpreadsheetMLBasicDef_VersionType_strategy)
def test_spreadsheetmlbasicdef_versiontype_n_setter(instance):
    original = instance.n
    instance.n = original
    assert instance.n == original



@given(instance=SpreadsheetMLBasicDef_VersionType_strategy)
def test_spreadsheetmlbasicdef_versiontype_nn_setter(instance):
    original = instance.nn
    instance.nn = original
    assert instance.nn == original

@given(instance=ValueType_strategy)
@settings(max_examples=50)
def test_valuetype_instantiation(instance):
    assert isinstance(instance, ValueType)

@given(instance=SpreadsheetMLBasicDef_BooleanValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlbasicdef_booleanvalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLBasicDef_BooleanValue)



@given(instance=SpreadsheetMLBasicDef_BooleanValue_strategy)
def test_spreadsheetmlbasicdef_booleanvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SpreadsheetMLBasicDef_ErrorValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlbasicdef_errorvalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLBasicDef_ErrorValue)

@given(instance=SpreadsheetMLBasicDef_StringValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlbasicdef_stringvalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLBasicDef_StringValue)



@given(instance=SpreadsheetMLBasicDef_StringValue_strategy)
def test_spreadsheetmlbasicdef_stringvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Data_strategy)
@settings(max_examples=50)
def test_data_instantiation(instance):
    assert isinstance(instance, Data)

@given(instance=SpreadsheetMLBasicDef_ValueType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlbasicdef_valuetype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLBasicDef_ValueType)

@given(instance=SpreadsheetMLBasicDef_DateTimeType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlbasicdef_datetimetype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLBasicDef_DateTimeType)



@given(instance=SpreadsheetMLBasicDef_DateTimeType_strategy)
def test_spreadsheetmlbasicdef_datetimetype_second_setter(instance):
    original = instance.second
    instance.second = original
    assert instance.second == original



@given(instance=SpreadsheetMLBasicDef_DateTimeType_strategy)
def test_spreadsheetmlbasicdef_datetimetype_day_setter(instance):
    original = instance.day
    instance.day = original
    assert instance.day == original



@given(instance=SpreadsheetMLBasicDef_DateTimeType_strategy)
def test_spreadsheetmlbasicdef_datetimetype_minute_setter(instance):
    original = instance.minute
    instance.minute = original
    assert instance.minute == original



@given(instance=SpreadsheetMLBasicDef_DateTimeType_strategy)
def test_spreadsheetmlbasicdef_datetimetype_hour_setter(instance):
    original = instance.hour
    instance.hour = original
    assert instance.hour == original



@given(instance=SpreadsheetMLBasicDef_DateTimeType_strategy)
def test_spreadsheetmlbasicdef_datetimetype_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original



@given(instance=SpreadsheetMLBasicDef_DateTimeType_strategy)
def test_spreadsheetmlbasicdef_datetimetype_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original

@given(instance=SpreadsheetMLBasicDef_Comment_strategy)
@settings(max_examples=50)
def test_spreadsheetmlbasicdef_comment_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLBasicDef_Comment)



@given(instance=SpreadsheetMLBasicDef_Comment_strategy)
def test_spreadsheetmlbasicdef_comment_showAlways_setter(instance):
    original = instance.showAlways
    instance.showAlways = original
    assert instance.showAlways == original



@given(instance=SpreadsheetMLBasicDef_Comment_strategy)
def test_spreadsheetmlbasicdef_comment_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=SpreadsheetMLBasicDef_Data_strategy)
@settings(max_examples=50)
def test_spreadsheetmlbasicdef_data_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLBasicDef_Data)

@given(instance=Comment_strategy)
@settings(max_examples=50)
def test_comment_instantiation(instance):
    assert isinstance(instance, Comment)

@given(instance=ColOrRowElement_strategy)
@settings(max_examples=50)
def test_colorrowelement_instantiation(instance):
    assert isinstance(instance, ColOrRowElement)

@given(instance=SpreadsheetMLBasicDef_Column_strategy)
@settings(max_examples=50)
def test_spreadsheetmlbasicdef_column_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLBasicDef_Column)



@given(instance=SpreadsheetMLBasicDef_Column_strategy)
def test_spreadsheetmlbasicdef_column_autoFitWidth_setter(instance):
    original = instance.autoFitWidth
    instance.autoFitWidth = original
    assert instance.autoFitWidth == original



@given(instance=SpreadsheetMLBasicDef_Column_strategy)
def test_spreadsheetmlbasicdef_column_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=TableElement_strategy)
@settings(max_examples=50)
def test_tableelement_instantiation(instance):
    assert isinstance(instance, TableElement)

@given(instance=SpreadsheetMLBasicDef_Cell_strategy)
@settings(max_examples=50)
def test_spreadsheetmlbasicdef_cell_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLBasicDef_Cell)



@given(instance=SpreadsheetMLBasicDef_Cell_strategy)
def test_spreadsheetmlbasicdef_cell_mergeDown_setter(instance):
    original = instance.mergeDown
    instance.mergeDown = original
    assert instance.mergeDown == original



@given(instance=SpreadsheetMLBasicDef_Cell_strategy)
def test_spreadsheetmlbasicdef_cell_formula_setter(instance):
    original = instance.formula
    instance.formula = original
    assert instance.formula == original



@given(instance=SpreadsheetMLBasicDef_Cell_strategy)
def test_spreadsheetmlbasicdef_cell_mergeAcross_setter(instance):
    original = instance.mergeAcross
    instance.mergeAcross = original
    assert instance.mergeAcross == original



@given(instance=SpreadsheetMLBasicDef_Cell_strategy)
def test_spreadsheetmlbasicdef_cell_arrayRange_setter(instance):
    original = instance.arrayRange
    instance.arrayRange = original
    assert instance.arrayRange == original



@given(instance=SpreadsheetMLBasicDef_Cell_strategy)
def test_spreadsheetmlbasicdef_cell_hRef_setter(instance):
    original = instance.hRef
    instance.hRef = original
    assert instance.hRef == original

@given(instance=SpreadsheetMLBasicDef_Row_strategy)
@settings(max_examples=50)
def test_spreadsheetmlbasicdef_row_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLBasicDef_Row)



@given(instance=SpreadsheetMLBasicDef_Row_strategy)
def test_spreadsheetmlbasicdef_row_autoFitHeight_setter(instance):
    original = instance.autoFitHeight
    instance.autoFitHeight = original
    assert instance.autoFitHeight == original



@given(instance=SpreadsheetMLBasicDef_Row_strategy)
def test_spreadsheetmlbasicdef_row_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=Row_strategy)
@settings(max_examples=50)
def test_row_instantiation(instance):
    assert isinstance(instance, Row)

@given(instance=SpreadsheetMLBasicDef_ColOrRowElement_strategy)
@settings(max_examples=50)
def test_spreadsheetmlbasicdef_colorrowelement_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLBasicDef_ColOrRowElement)



@given(instance=SpreadsheetMLBasicDef_ColOrRowElement_strategy)
def test_spreadsheetmlbasicdef_colorrowelement_span_setter(instance):
    original = instance.span
    instance.span = original
    assert instance.span == original



@given(instance=SpreadsheetMLBasicDef_ColOrRowElement_strategy)
def test_spreadsheetmlbasicdef_colorrowelement_hidden_setter(instance):
    original = instance.hidden
    instance.hidden = original
    assert instance.hidden == original

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)

@given(instance=SpreadsheetMLBasicDef_Worksheet_strategy)
@settings(max_examples=50)
def test_spreadsheetmlbasicdef_worksheet_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLBasicDef_Worksheet)



@given(instance=SpreadsheetMLBasicDef_Worksheet_strategy)
def test_spreadsheetmlbasicdef_worksheet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Column_strategy)
@settings(max_examples=50)
def test_column_instantiation(instance):
    assert isinstance(instance, Column)

@given(instance=StyledElement_strategy)
@settings(max_examples=50)
def test_styledelement_instantiation(instance):
    assert isinstance(instance, StyledElement)

@given(instance=SpreadsheetMLBasicDef_TableElement_strategy)
@settings(max_examples=50)
def test_spreadsheetmlbasicdef_tableelement_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLBasicDef_TableElement)



@given(instance=SpreadsheetMLBasicDef_TableElement_strategy)
def test_spreadsheetmlbasicdef_tableelement_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original

@given(instance=SpreadsheetMLBasicDef_Table_strategy)
@settings(max_examples=50)
def test_spreadsheetmlbasicdef_table_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLBasicDef_Table)



@given(instance=SpreadsheetMLBasicDef_Table_strategy)
def test_spreadsheetmlbasicdef_table_topCell_setter(instance):
    original = instance.topCell
    instance.topCell = original
    assert instance.topCell == original



@given(instance=SpreadsheetMLBasicDef_Table_strategy)
def test_spreadsheetmlbasicdef_table_fullRows_setter(instance):
    original = instance.fullRows
    instance.fullRows = original
    assert instance.fullRows == original



@given(instance=SpreadsheetMLBasicDef_Table_strategy)
def test_spreadsheetmlbasicdef_table_defaultColumnWidth_setter(instance):
    original = instance.defaultColumnWidth
    instance.defaultColumnWidth = original
    assert instance.defaultColumnWidth == original



@given(instance=SpreadsheetMLBasicDef_Table_strategy)
def test_spreadsheetmlbasicdef_table_expandedRowCount_setter(instance):
    original = instance.expandedRowCount
    instance.expandedRowCount = original
    assert instance.expandedRowCount == original



@given(instance=SpreadsheetMLBasicDef_Table_strategy)
def test_spreadsheetmlbasicdef_table_defaultRowHeight_setter(instance):
    original = instance.defaultRowHeight
    instance.defaultRowHeight = original
    assert instance.defaultRowHeight == original



@given(instance=SpreadsheetMLBasicDef_Table_strategy)
def test_spreadsheetmlbasicdef_table_fullColumns_setter(instance):
    original = instance.fullColumns
    instance.fullColumns = original
    assert instance.fullColumns == original



@given(instance=SpreadsheetMLBasicDef_Table_strategy)
def test_spreadsheetmlbasicdef_table_expandedColumnCount_setter(instance):
    original = instance.expandedColumnCount
    instance.expandedColumnCount = original
    assert instance.expandedColumnCount == original



@given(instance=SpreadsheetMLBasicDef_Table_strategy)
def test_spreadsheetmlbasicdef_table_leftCell_setter(instance):
    original = instance.leftCell
    instance.leftCell = original
    assert instance.leftCell == original

@given(instance=SpreadsheetMLBasicDef_StyledElement_strategy)
@settings(max_examples=50)
def test_spreadsheetmlbasicdef_styledelement_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLBasicDef_StyledElement)

@given(instance=SpreadsheetMLBasicDef_Workbook_strategy)
@settings(max_examples=50)
def test_spreadsheetmlbasicdef_workbook_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLBasicDef_Workbook)

@given(instance=SmartTagType_strategy)
@settings(max_examples=50)
def test_smarttagtype_instantiation(instance):
    assert isinstance(instance, SmartTagType)

@given(instance=Cell_strategy)
@settings(max_examples=50)
def test_cell_instantiation(instance):
    assert isinstance(instance, Cell)

@given(instance=Worksheet_strategy)
@settings(max_examples=50)
def test_worksheet_instantiation(instance):
    assert isinstance(instance, Worksheet)

@given(instance=DocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_documentpropertiescollection_instantiation(instance):
    assert isinstance(instance, DocumentPropertiesCollection)

@given(instance=SmartTagsCollection_strategy)
@settings(max_examples=50)
def test_smarttagscollection_instantiation(instance):
    assert isinstance(instance, SmartTagsCollection)

@given(instance=SpreadsheetMLBasicDef_SmartTagType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlbasicdef_smarttagtype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLBasicDef_SmartTagType)



@given(instance=SpreadsheetMLBasicDef_SmartTagType_strategy)
def test_spreadsheetmlbasicdef_smarttagtype_namespaceuri_setter(instance):
    original = instance.namespaceuri
    instance.namespaceuri = original
    assert instance.namespaceuri == original



@given(instance=SpreadsheetMLBasicDef_SmartTagType_strategy)
def test_spreadsheetmlbasicdef_smarttagtype_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original



@given(instance=SpreadsheetMLBasicDef_SmartTagType_strategy)
def test_spreadsheetmlbasicdef_smarttagtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SpreadsheetMLBasicDef_SmartTagsCollection_strategy)
@settings(max_examples=50)
def test_spreadsheetmlbasicdef_smarttagscollection_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLBasicDef_SmartTagsCollection)

@given(instance=SpreadsheetMLBasicDef_CustomDocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_spreadsheetmlbasicdef_customdocumentpropertiescollection_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLBasicDef_CustomDocumentPropertiesCollection)

@given(instance=CustomDocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_customdocumentpropertiescollection_instantiation(instance):
    assert isinstance(instance, CustomDocumentPropertiesCollection)

@given(instance=SpreadsheetMLBasicDef_CustomDocumentProperty_strategy)
@settings(max_examples=50)
def test_spreadsheetmlbasicdef_customdocumentproperty_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLBasicDef_CustomDocumentProperty)



@given(instance=SpreadsheetMLBasicDef_CustomDocumentProperty_strategy)
def test_spreadsheetmlbasicdef_customdocumentproperty_name_setter(instance):
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

@given(instance=SpreadsheetMLBasicDef_DateTimeTypeValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlbasicdef_datetimetypevalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLBasicDef_DateTimeTypeValue)

@given(instance=SpreadsheetMLBasicDef_NumberValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlbasicdef_numbervalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLBasicDef_NumberValue)



@given(instance=SpreadsheetMLBasicDef_NumberValue_strategy)
def test_spreadsheetmlbasicdef_numbervalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original
