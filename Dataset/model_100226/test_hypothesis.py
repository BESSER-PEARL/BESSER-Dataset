import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    SpreadsheetMLBasicDef::Comment,
    SpreadsheetMLBasicDef::Data,
    Comment,
    ColOrRowElement,
    SpreadsheetMLBasicDef::Column,
    TableElement,
    SpreadsheetMLBasicDef::Cell,
    SpreadsheetMLBasicDef::Row,
    Row,
    SpreadsheetMLBasicDef::ColOrRowElement,
    Table,
    SpreadsheetMLBasicDef::Worksheet,
    Column,
    StyledElement,
    SpreadsheetMLBasicDef::TableElement,
    SpreadsheetMLBasicDef::Table,
    SpreadsheetMLBasicDef::StyledElement,
    SpreadsheetMLBasicDef::Workbook,
    SmartTagType,
    Cell,
    Worksheet,
    DocumentPropertiesCollection,
    SmartTagsCollection,
    SpreadsheetMLBasicDef::SmartTagType,
    SpreadsheetMLBasicDef::SmartTagsCollection,
    SpreadsheetMLBasicDef::CustomDocumentPropertiesCollection,
    CustomDocumentPropertiesCollection,
    SpreadsheetMLBasicDef::CustomDocumentProperty,
    CustomDocumentProperty,
    VersionType,
    Workbook,
    SpreadsheetMLBasicDef::DocumentPropertiesCollection,
    DateTimeType,
    SpreadsheetMLBasicDef::VersionType,
    ValueType,
    SpreadsheetMLBasicDef::ErrorValue,
    SpreadsheetMLBasicDef::BooleanValue,
    SpreadsheetMLBasicDef::NumberValue,
    SpreadsheetMLBasicDef::DateTimeTypeValue,
    SpreadsheetMLBasicDef::StringValue,
    Data,
    SpreadsheetMLBasicDef::ValueType,
    SpreadsheetMLBasicDef::DateTimeType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_spreadsheetmlbasicdef::comment_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLBasicDef::Comment)


def test_spreadsheetmlbasicdef::comment_constructor_exists():
    assert callable(SpreadsheetMLBasicDef::Comment.__init__)


def test_spreadsheetmlbasicdef::comment_constructor_args():
    sig = inspect.signature(SpreadsheetMLBasicDef::Comment.__init__)
    params = list(sig.parameters.keys())
    assert "showAlways" in params, "Missing parameter 'showAlways'"
    assert "author" in params, "Missing parameter 'author'"

def test_spreadsheetmlbasicdef::comment_has_showAlways():
    assert hasattr(SpreadsheetMLBasicDef::Comment, "showAlways")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::Comment.__mro__:
        if "showAlways" in klass.__dict__:
            descriptor = klass.__dict__["showAlways"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef::comment_has_author():
    assert hasattr(SpreadsheetMLBasicDef::Comment, "author")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::Comment.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlbasicdef::data_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLBasicDef::Data)


def test_spreadsheetmlbasicdef::data_constructor_exists():
    assert callable(SpreadsheetMLBasicDef::Data.__init__)


def test_spreadsheetmlbasicdef::data_constructor_args():
    sig = inspect.signature(SpreadsheetMLBasicDef::Data.__init__)
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



def test_spreadsheetmlbasicdef::column_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLBasicDef::Column)


def test_spreadsheetmlbasicdef::column_constructor_exists():
    assert callable(SpreadsheetMLBasicDef::Column.__init__)


def test_spreadsheetmlbasicdef::column_constructor_args():
    sig = inspect.signature(SpreadsheetMLBasicDef::Column.__init__)
    params = list(sig.parameters.keys())
    assert "autoFitWidth" in params, "Missing parameter 'autoFitWidth'"
    assert "width" in params, "Missing parameter 'width'"

def test_spreadsheetmlbasicdef::column_has_autoFitWidth():
    assert hasattr(SpreadsheetMLBasicDef::Column, "autoFitWidth")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::Column.__mro__:
        if "autoFitWidth" in klass.__dict__:
            descriptor = klass.__dict__["autoFitWidth"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef::column_has_width():
    assert hasattr(SpreadsheetMLBasicDef::Column, "width")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::Column.__mro__:
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



def test_spreadsheetmlbasicdef::cell_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLBasicDef::Cell)


def test_spreadsheetmlbasicdef::cell_constructor_exists():
    assert callable(SpreadsheetMLBasicDef::Cell.__init__)


def test_spreadsheetmlbasicdef::cell_constructor_args():
    sig = inspect.signature(SpreadsheetMLBasicDef::Cell.__init__)
    params = list(sig.parameters.keys())
    assert "hRef" in params, "Missing parameter 'hRef'"
    assert "mergeDown" in params, "Missing parameter 'mergeDown'"
    assert "mergeAcross" in params, "Missing parameter 'mergeAcross'"
    assert "arrayRange" in params, "Missing parameter 'arrayRange'"
    assert "formula" in params, "Missing parameter 'formula'"

def test_spreadsheetmlbasicdef::cell_has_hRef():
    assert hasattr(SpreadsheetMLBasicDef::Cell, "hRef")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::Cell.__mro__:
        if "hRef" in klass.__dict__:
            descriptor = klass.__dict__["hRef"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef::cell_has_mergeDown():
    assert hasattr(SpreadsheetMLBasicDef::Cell, "mergeDown")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::Cell.__mro__:
        if "mergeDown" in klass.__dict__:
            descriptor = klass.__dict__["mergeDown"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef::cell_has_mergeAcross():
    assert hasattr(SpreadsheetMLBasicDef::Cell, "mergeAcross")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::Cell.__mro__:
        if "mergeAcross" in klass.__dict__:
            descriptor = klass.__dict__["mergeAcross"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef::cell_has_arrayRange():
    assert hasattr(SpreadsheetMLBasicDef::Cell, "arrayRange")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::Cell.__mro__:
        if "arrayRange" in klass.__dict__:
            descriptor = klass.__dict__["arrayRange"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef::cell_has_formula():
    assert hasattr(SpreadsheetMLBasicDef::Cell, "formula")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::Cell.__mro__:
        if "formula" in klass.__dict__:
            descriptor = klass.__dict__["formula"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlbasicdef::row_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLBasicDef::Row)


def test_spreadsheetmlbasicdef::row_constructor_exists():
    assert callable(SpreadsheetMLBasicDef::Row.__init__)


def test_spreadsheetmlbasicdef::row_constructor_args():
    sig = inspect.signature(SpreadsheetMLBasicDef::Row.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "autoFitHeight" in params, "Missing parameter 'autoFitHeight'"

def test_spreadsheetmlbasicdef::row_has_height():
    assert hasattr(SpreadsheetMLBasicDef::Row, "height")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::Row.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef::row_has_autoFitHeight():
    assert hasattr(SpreadsheetMLBasicDef::Row, "autoFitHeight")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::Row.__mro__:
        if "autoFitHeight" in klass.__dict__:
            descriptor = klass.__dict__["autoFitHeight"]
            break
    assert isinstance(descriptor, property)



def test_row_is_not_abstract():
    assert not inspect.isabstract(Row)


def test_row_constructor_exists():
    assert callable(Row.__init__)


def test_row_constructor_args():
    sig = inspect.signature(Row.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlbasicdef::colorrowelement_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLBasicDef::ColOrRowElement)


def test_spreadsheetmlbasicdef::colorrowelement_constructor_exists():
    assert callable(SpreadsheetMLBasicDef::ColOrRowElement.__init__)


def test_spreadsheetmlbasicdef::colorrowelement_constructor_args():
    sig = inspect.signature(SpreadsheetMLBasicDef::ColOrRowElement.__init__)
    params = list(sig.parameters.keys())
    assert "hidden" in params, "Missing parameter 'hidden'"
    assert "span" in params, "Missing parameter 'span'"

def test_spreadsheetmlbasicdef::colorrowelement_has_hidden():
    assert hasattr(SpreadsheetMLBasicDef::ColOrRowElement, "hidden")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::ColOrRowElement.__mro__:
        if "hidden" in klass.__dict__:
            descriptor = klass.__dict__["hidden"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef::colorrowelement_has_span():
    assert hasattr(SpreadsheetMLBasicDef::ColOrRowElement, "span")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::ColOrRowElement.__mro__:
        if "span" in klass.__dict__:
            descriptor = klass.__dict__["span"]
            break
    assert isinstance(descriptor, property)



def test_table_is_not_abstract():
    assert not inspect.isabstract(Table)


def test_table_constructor_exists():
    assert callable(Table.__init__)


def test_table_constructor_args():
    sig = inspect.signature(Table.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlbasicdef::worksheet_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLBasicDef::Worksheet)


def test_spreadsheetmlbasicdef::worksheet_constructor_exists():
    assert callable(SpreadsheetMLBasicDef::Worksheet.__init__)


def test_spreadsheetmlbasicdef::worksheet_constructor_args():
    sig = inspect.signature(SpreadsheetMLBasicDef::Worksheet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_spreadsheetmlbasicdef::worksheet_has_name():
    assert hasattr(SpreadsheetMLBasicDef::Worksheet, "name")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::Worksheet.__mro__:
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



def test_spreadsheetmlbasicdef::tableelement_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLBasicDef::TableElement)


def test_spreadsheetmlbasicdef::tableelement_constructor_exists():
    assert callable(SpreadsheetMLBasicDef::TableElement.__init__)


def test_spreadsheetmlbasicdef::tableelement_constructor_args():
    sig = inspect.signature(SpreadsheetMLBasicDef::TableElement.__init__)
    params = list(sig.parameters.keys())
    assert "index" in params, "Missing parameter 'index'"

def test_spreadsheetmlbasicdef::tableelement_has_index():
    assert hasattr(SpreadsheetMLBasicDef::TableElement, "index")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::TableElement.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlbasicdef::table_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLBasicDef::Table)


def test_spreadsheetmlbasicdef::table_constructor_exists():
    assert callable(SpreadsheetMLBasicDef::Table.__init__)


def test_spreadsheetmlbasicdef::table_constructor_args():
    sig = inspect.signature(SpreadsheetMLBasicDef::Table.__init__)
    params = list(sig.parameters.keys())
    assert "leftCell" in params, "Missing parameter 'leftCell'"
    assert "expandedColumnCount" in params, "Missing parameter 'expandedColumnCount'"
    assert "defaultRowHeight" in params, "Missing parameter 'defaultRowHeight'"
    assert "topCell" in params, "Missing parameter 'topCell'"
    assert "fullColumns" in params, "Missing parameter 'fullColumns'"
    assert "expandedRowCount" in params, "Missing parameter 'expandedRowCount'"
    assert "fullRows" in params, "Missing parameter 'fullRows'"
    assert "defaultColumnWidth" in params, "Missing parameter 'defaultColumnWidth'"

def test_spreadsheetmlbasicdef::table_has_leftCell():
    assert hasattr(SpreadsheetMLBasicDef::Table, "leftCell")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::Table.__mro__:
        if "leftCell" in klass.__dict__:
            descriptor = klass.__dict__["leftCell"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef::table_has_expandedColumnCount():
    assert hasattr(SpreadsheetMLBasicDef::Table, "expandedColumnCount")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::Table.__mro__:
        if "expandedColumnCount" in klass.__dict__:
            descriptor = klass.__dict__["expandedColumnCount"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef::table_has_defaultRowHeight():
    assert hasattr(SpreadsheetMLBasicDef::Table, "defaultRowHeight")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::Table.__mro__:
        if "defaultRowHeight" in klass.__dict__:
            descriptor = klass.__dict__["defaultRowHeight"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef::table_has_topCell():
    assert hasattr(SpreadsheetMLBasicDef::Table, "topCell")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::Table.__mro__:
        if "topCell" in klass.__dict__:
            descriptor = klass.__dict__["topCell"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef::table_has_fullColumns():
    assert hasattr(SpreadsheetMLBasicDef::Table, "fullColumns")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::Table.__mro__:
        if "fullColumns" in klass.__dict__:
            descriptor = klass.__dict__["fullColumns"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef::table_has_expandedRowCount():
    assert hasattr(SpreadsheetMLBasicDef::Table, "expandedRowCount")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::Table.__mro__:
        if "expandedRowCount" in klass.__dict__:
            descriptor = klass.__dict__["expandedRowCount"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef::table_has_fullRows():
    assert hasattr(SpreadsheetMLBasicDef::Table, "fullRows")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::Table.__mro__:
        if "fullRows" in klass.__dict__:
            descriptor = klass.__dict__["fullRows"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef::table_has_defaultColumnWidth():
    assert hasattr(SpreadsheetMLBasicDef::Table, "defaultColumnWidth")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::Table.__mro__:
        if "defaultColumnWidth" in klass.__dict__:
            descriptor = klass.__dict__["defaultColumnWidth"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlbasicdef::styledelement_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLBasicDef::StyledElement)


def test_spreadsheetmlbasicdef::styledelement_constructor_exists():
    assert callable(SpreadsheetMLBasicDef::StyledElement.__init__)


def test_spreadsheetmlbasicdef::styledelement_constructor_args():
    sig = inspect.signature(SpreadsheetMLBasicDef::StyledElement.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlbasicdef::workbook_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLBasicDef::Workbook)


def test_spreadsheetmlbasicdef::workbook_constructor_exists():
    assert callable(SpreadsheetMLBasicDef::Workbook.__init__)


def test_spreadsheetmlbasicdef::workbook_constructor_args():
    sig = inspect.signature(SpreadsheetMLBasicDef::Workbook.__init__)
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



def test_spreadsheetmlbasicdef::smarttagtype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLBasicDef::SmartTagType)


def test_spreadsheetmlbasicdef::smarttagtype_constructor_exists():
    assert callable(SpreadsheetMLBasicDef::SmartTagType.__init__)


def test_spreadsheetmlbasicdef::smarttagtype_constructor_args():
    sig = inspect.signature(SpreadsheetMLBasicDef::SmartTagType.__init__)
    params = list(sig.parameters.keys())
    assert "url" in params, "Missing parameter 'url'"
    assert "name" in params, "Missing parameter 'name'"
    assert "namespaceuri" in params, "Missing parameter 'namespaceuri'"

def test_spreadsheetmlbasicdef::smarttagtype_has_url():
    assert hasattr(SpreadsheetMLBasicDef::SmartTagType, "url")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::SmartTagType.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef::smarttagtype_has_name():
    assert hasattr(SpreadsheetMLBasicDef::SmartTagType, "name")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::SmartTagType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef::smarttagtype_has_namespaceuri():
    assert hasattr(SpreadsheetMLBasicDef::SmartTagType, "namespaceuri")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::SmartTagType.__mro__:
        if "namespaceuri" in klass.__dict__:
            descriptor = klass.__dict__["namespaceuri"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlbasicdef::smarttagscollection_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLBasicDef::SmartTagsCollection)


def test_spreadsheetmlbasicdef::smarttagscollection_constructor_exists():
    assert callable(SpreadsheetMLBasicDef::SmartTagsCollection.__init__)


def test_spreadsheetmlbasicdef::smarttagscollection_constructor_args():
    sig = inspect.signature(SpreadsheetMLBasicDef::SmartTagsCollection.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlbasicdef::customdocumentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLBasicDef::CustomDocumentPropertiesCollection)


def test_spreadsheetmlbasicdef::customdocumentpropertiescollection_constructor_exists():
    assert callable(SpreadsheetMLBasicDef::CustomDocumentPropertiesCollection.__init__)


def test_spreadsheetmlbasicdef::customdocumentpropertiescollection_constructor_args():
    sig = inspect.signature(SpreadsheetMLBasicDef::CustomDocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())



def test_customdocumentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(CustomDocumentPropertiesCollection)


def test_customdocumentpropertiescollection_constructor_exists():
    assert callable(CustomDocumentPropertiesCollection.__init__)


def test_customdocumentpropertiescollection_constructor_args():
    sig = inspect.signature(CustomDocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlbasicdef::customdocumentproperty_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLBasicDef::CustomDocumentProperty)


def test_spreadsheetmlbasicdef::customdocumentproperty_constructor_exists():
    assert callable(SpreadsheetMLBasicDef::CustomDocumentProperty.__init__)


def test_spreadsheetmlbasicdef::customdocumentproperty_constructor_args():
    sig = inspect.signature(SpreadsheetMLBasicDef::CustomDocumentProperty.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_spreadsheetmlbasicdef::customdocumentproperty_has_name():
    assert hasattr(SpreadsheetMLBasicDef::CustomDocumentProperty, "name")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::CustomDocumentProperty.__mro__:
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



def test_spreadsheetmlbasicdef::documentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLBasicDef::DocumentPropertiesCollection)


def test_spreadsheetmlbasicdef::documentpropertiescollection_constructor_exists():
    assert callable(SpreadsheetMLBasicDef::DocumentPropertiesCollection.__init__)


def test_spreadsheetmlbasicdef::documentpropertiescollection_constructor_args():
    sig = inspect.signature(SpreadsheetMLBasicDef::DocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())
    assert "charactersWithSpaces" in params, "Missing parameter 'charactersWithSpaces'"
    assert "appName" in params, "Missing parameter 'appName'"
    assert "keywords" in params, "Missing parameter 'keywords'"
    assert "company" in params, "Missing parameter 'company'"
    assert "category" in params, "Missing parameter 'category'"
    assert "paragraphs" in params, "Missing parameter 'paragraphs'"
    assert "hyperlinkBase" in params, "Missing parameter 'hyperlinkBase'"
    assert "pages" in params, "Missing parameter 'pages'"
    assert "presentationFormat" in params, "Missing parameter 'presentationFormat'"
    assert "lines" in params, "Missing parameter 'lines'"
    assert "title" in params, "Missing parameter 'title'"
    assert "words" in params, "Missing parameter 'words'"
    assert "totalTime" in params, "Missing parameter 'totalTime'"
    assert "revision" in params, "Missing parameter 'revision'"
    assert "description" in params, "Missing parameter 'description'"
    assert "author" in params, "Missing parameter 'author'"
    assert "subject" in params, "Missing parameter 'subject'"
    assert "characters" in params, "Missing parameter 'characters'"
    assert "guid" in params, "Missing parameter 'guid'"
    assert "bytes" in params, "Missing parameter 'bytes'"
    assert "lastAuthor" in params, "Missing parameter 'lastAuthor'"
    assert "manager" in params, "Missing parameter 'manager'"

def test_spreadsheetmlbasicdef::documentpropertiescollection_has_charactersWithSpaces():
    assert hasattr(SpreadsheetMLBasicDef::DocumentPropertiesCollection, "charactersWithSpaces")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "charactersWithSpaces" in klass.__dict__:
            descriptor = klass.__dict__["charactersWithSpaces"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef::documentpropertiescollection_has_appName():
    assert hasattr(SpreadsheetMLBasicDef::DocumentPropertiesCollection, "appName")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "appName" in klass.__dict__:
            descriptor = klass.__dict__["appName"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef::documentpropertiescollection_has_keywords():
    assert hasattr(SpreadsheetMLBasicDef::DocumentPropertiesCollection, "keywords")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "keywords" in klass.__dict__:
            descriptor = klass.__dict__["keywords"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef::documentpropertiescollection_has_company():
    assert hasattr(SpreadsheetMLBasicDef::DocumentPropertiesCollection, "company")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "company" in klass.__dict__:
            descriptor = klass.__dict__["company"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef::documentpropertiescollection_has_category():
    assert hasattr(SpreadsheetMLBasicDef::DocumentPropertiesCollection, "category")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef::documentpropertiescollection_has_paragraphs():
    assert hasattr(SpreadsheetMLBasicDef::DocumentPropertiesCollection, "paragraphs")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "paragraphs" in klass.__dict__:
            descriptor = klass.__dict__["paragraphs"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef::documentpropertiescollection_has_hyperlinkBase():
    assert hasattr(SpreadsheetMLBasicDef::DocumentPropertiesCollection, "hyperlinkBase")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "hyperlinkBase" in klass.__dict__:
            descriptor = klass.__dict__["hyperlinkBase"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef::documentpropertiescollection_has_pages():
    assert hasattr(SpreadsheetMLBasicDef::DocumentPropertiesCollection, "pages")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef::documentpropertiescollection_has_presentationFormat():
    assert hasattr(SpreadsheetMLBasicDef::DocumentPropertiesCollection, "presentationFormat")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "presentationFormat" in klass.__dict__:
            descriptor = klass.__dict__["presentationFormat"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef::documentpropertiescollection_has_lines():
    assert hasattr(SpreadsheetMLBasicDef::DocumentPropertiesCollection, "lines")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "lines" in klass.__dict__:
            descriptor = klass.__dict__["lines"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef::documentpropertiescollection_has_title():
    assert hasattr(SpreadsheetMLBasicDef::DocumentPropertiesCollection, "title")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef::documentpropertiescollection_has_words():
    assert hasattr(SpreadsheetMLBasicDef::DocumentPropertiesCollection, "words")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "words" in klass.__dict__:
            descriptor = klass.__dict__["words"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef::documentpropertiescollection_has_totalTime():
    assert hasattr(SpreadsheetMLBasicDef::DocumentPropertiesCollection, "totalTime")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "totalTime" in klass.__dict__:
            descriptor = klass.__dict__["totalTime"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef::documentpropertiescollection_has_revision():
    assert hasattr(SpreadsheetMLBasicDef::DocumentPropertiesCollection, "revision")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "revision" in klass.__dict__:
            descriptor = klass.__dict__["revision"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef::documentpropertiescollection_has_description():
    assert hasattr(SpreadsheetMLBasicDef::DocumentPropertiesCollection, "description")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef::documentpropertiescollection_has_author():
    assert hasattr(SpreadsheetMLBasicDef::DocumentPropertiesCollection, "author")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef::documentpropertiescollection_has_subject():
    assert hasattr(SpreadsheetMLBasicDef::DocumentPropertiesCollection, "subject")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "subject" in klass.__dict__:
            descriptor = klass.__dict__["subject"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef::documentpropertiescollection_has_characters():
    assert hasattr(SpreadsheetMLBasicDef::DocumentPropertiesCollection, "characters")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "characters" in klass.__dict__:
            descriptor = klass.__dict__["characters"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef::documentpropertiescollection_has_guid():
    assert hasattr(SpreadsheetMLBasicDef::DocumentPropertiesCollection, "guid")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "guid" in klass.__dict__:
            descriptor = klass.__dict__["guid"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef::documentpropertiescollection_has_bytes():
    assert hasattr(SpreadsheetMLBasicDef::DocumentPropertiesCollection, "bytes")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "bytes" in klass.__dict__:
            descriptor = klass.__dict__["bytes"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef::documentpropertiescollection_has_lastAuthor():
    assert hasattr(SpreadsheetMLBasicDef::DocumentPropertiesCollection, "lastAuthor")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "lastAuthor" in klass.__dict__:
            descriptor = klass.__dict__["lastAuthor"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef::documentpropertiescollection_has_manager():
    assert hasattr(SpreadsheetMLBasicDef::DocumentPropertiesCollection, "manager")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "manager" in klass.__dict__:
            descriptor = klass.__dict__["manager"]
            break
    assert isinstance(descriptor, property)



def test_datetimetype_is_not_abstract():
    assert not inspect.isabstract(DateTimeType)


def test_datetimetype_constructor_exists():
    assert callable(DateTimeType.__init__)


def test_datetimetype_constructor_args():
    sig = inspect.signature(DateTimeType.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlbasicdef::versiontype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLBasicDef::VersionType)


def test_spreadsheetmlbasicdef::versiontype_constructor_exists():
    assert callable(SpreadsheetMLBasicDef::VersionType.__init__)


def test_spreadsheetmlbasicdef::versiontype_constructor_args():
    sig = inspect.signature(SpreadsheetMLBasicDef::VersionType.__init__)
    params = list(sig.parameters.keys())
    assert "n" in params, "Missing parameter 'n'"
    assert "nn" in params, "Missing parameter 'nn'"

def test_spreadsheetmlbasicdef::versiontype_has_n():
    assert hasattr(SpreadsheetMLBasicDef::VersionType, "n")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::VersionType.__mro__:
        if "n" in klass.__dict__:
            descriptor = klass.__dict__["n"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef::versiontype_has_nn():
    assert hasattr(SpreadsheetMLBasicDef::VersionType, "nn")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::VersionType.__mro__:
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



def test_spreadsheetmlbasicdef::errorvalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLBasicDef::ErrorValue)


def test_spreadsheetmlbasicdef::errorvalue_constructor_exists():
    assert callable(SpreadsheetMLBasicDef::ErrorValue.__init__)


def test_spreadsheetmlbasicdef::errorvalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLBasicDef::ErrorValue.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlbasicdef::booleanvalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLBasicDef::BooleanValue)


def test_spreadsheetmlbasicdef::booleanvalue_constructor_exists():
    assert callable(SpreadsheetMLBasicDef::BooleanValue.__init__)


def test_spreadsheetmlbasicdef::booleanvalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLBasicDef::BooleanValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_spreadsheetmlbasicdef::booleanvalue_has_value():
    assert hasattr(SpreadsheetMLBasicDef::BooleanValue, "value")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::BooleanValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlbasicdef::numbervalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLBasicDef::NumberValue)


def test_spreadsheetmlbasicdef::numbervalue_constructor_exists():
    assert callable(SpreadsheetMLBasicDef::NumberValue.__init__)


def test_spreadsheetmlbasicdef::numbervalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLBasicDef::NumberValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_spreadsheetmlbasicdef::numbervalue_has_value():
    assert hasattr(SpreadsheetMLBasicDef::NumberValue, "value")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::NumberValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlbasicdef::datetimetypevalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLBasicDef::DateTimeTypeValue)


def test_spreadsheetmlbasicdef::datetimetypevalue_constructor_exists():
    assert callable(SpreadsheetMLBasicDef::DateTimeTypeValue.__init__)


def test_spreadsheetmlbasicdef::datetimetypevalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLBasicDef::DateTimeTypeValue.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlbasicdef::stringvalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLBasicDef::StringValue)


def test_spreadsheetmlbasicdef::stringvalue_constructor_exists():
    assert callable(SpreadsheetMLBasicDef::StringValue.__init__)


def test_spreadsheetmlbasicdef::stringvalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLBasicDef::StringValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_spreadsheetmlbasicdef::stringvalue_has_value():
    assert hasattr(SpreadsheetMLBasicDef::StringValue, "value")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::StringValue.__mro__:
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



def test_spreadsheetmlbasicdef::valuetype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLBasicDef::ValueType)


def test_spreadsheetmlbasicdef::valuetype_constructor_exists():
    assert callable(SpreadsheetMLBasicDef::ValueType.__init__)


def test_spreadsheetmlbasicdef::valuetype_constructor_args():
    sig = inspect.signature(SpreadsheetMLBasicDef::ValueType.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlbasicdef::datetimetype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLBasicDef::DateTimeType)


def test_spreadsheetmlbasicdef::datetimetype_constructor_exists():
    assert callable(SpreadsheetMLBasicDef::DateTimeType.__init__)


def test_spreadsheetmlbasicdef::datetimetype_constructor_args():
    sig = inspect.signature(SpreadsheetMLBasicDef::DateTimeType.__init__)
    params = list(sig.parameters.keys())
    assert "minute" in params, "Missing parameter 'minute'"
    assert "hour" in params, "Missing parameter 'hour'"
    assert "year" in params, "Missing parameter 'year'"
    assert "day" in params, "Missing parameter 'day'"
    assert "month" in params, "Missing parameter 'month'"
    assert "second" in params, "Missing parameter 'second'"

def test_spreadsheetmlbasicdef::datetimetype_has_minute():
    assert hasattr(SpreadsheetMLBasicDef::DateTimeType, "minute")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::DateTimeType.__mro__:
        if "minute" in klass.__dict__:
            descriptor = klass.__dict__["minute"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef::datetimetype_has_hour():
    assert hasattr(SpreadsheetMLBasicDef::DateTimeType, "hour")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::DateTimeType.__mro__:
        if "hour" in klass.__dict__:
            descriptor = klass.__dict__["hour"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef::datetimetype_has_year():
    assert hasattr(SpreadsheetMLBasicDef::DateTimeType, "year")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::DateTimeType.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef::datetimetype_has_day():
    assert hasattr(SpreadsheetMLBasicDef::DateTimeType, "day")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::DateTimeType.__mro__:
        if "day" in klass.__dict__:
            descriptor = klass.__dict__["day"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef::datetimetype_has_month():
    assert hasattr(SpreadsheetMLBasicDef::DateTimeType, "month")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::DateTimeType.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlbasicdef::datetimetype_has_second():
    assert hasattr(SpreadsheetMLBasicDef::DateTimeType, "second")
    descriptor = None
    for klass in SpreadsheetMLBasicDef::DateTimeType.__mro__:
        if "second" in klass.__dict__:
            descriptor = klass.__dict__["second"]
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
SpreadsheetMLBasicDef::Comment_strategy = st.builds(
    SpreadsheetMLBasicDef::Comment,
    showAlways=
        safe_text,
    author=
        safe_text
)
SpreadsheetMLBasicDef::Data_strategy = st.builds(
    SpreadsheetMLBasicDef::Data,
)
Comment_strategy = st.builds(
    Comment,
)
ColOrRowElement_strategy = st.builds(
    ColOrRowElement,
)
SpreadsheetMLBasicDef::Column_strategy = st.builds(
    SpreadsheetMLBasicDef::Column,
    autoFitWidth=
        safe_text,
    width=
        safe_text
)
TableElement_strategy = st.builds(
    TableElement,
)
SpreadsheetMLBasicDef::Cell_strategy = st.builds(
    SpreadsheetMLBasicDef::Cell,
    hRef=
        safe_text,
    mergeDown=
        safe_text,
    mergeAcross=
        safe_text,
    arrayRange=
        safe_text,
    formula=
        safe_text
)
SpreadsheetMLBasicDef::Row_strategy = st.builds(
    SpreadsheetMLBasicDef::Row,
    height=
        safe_text,
    autoFitHeight=
        safe_text
)
Row_strategy = st.builds(
    Row,
)
SpreadsheetMLBasicDef::ColOrRowElement_strategy = st.builds(
    SpreadsheetMLBasicDef::ColOrRowElement,
    hidden=
        safe_text,
    span=
        safe_text
)
Table_strategy = st.builds(
    Table,
)
SpreadsheetMLBasicDef::Worksheet_strategy = st.builds(
    SpreadsheetMLBasicDef::Worksheet,
    name=
        safe_text
)
Column_strategy = st.builds(
    Column,
)
StyledElement_strategy = st.builds(
    StyledElement,
)
SpreadsheetMLBasicDef::TableElement_strategy = st.builds(
    SpreadsheetMLBasicDef::TableElement,
    index=
        safe_text
)
SpreadsheetMLBasicDef::Table_strategy = st.builds(
    SpreadsheetMLBasicDef::Table,
    leftCell=
        safe_text,
    expandedColumnCount=
        safe_text,
    defaultRowHeight=
        safe_text,
    topCell=
        safe_text,
    fullColumns=
        safe_text,
    expandedRowCount=
        safe_text,
    fullRows=
        safe_text,
    defaultColumnWidth=
        safe_text
)
SpreadsheetMLBasicDef::StyledElement_strategy = st.builds(
    SpreadsheetMLBasicDef::StyledElement,
)
SpreadsheetMLBasicDef::Workbook_strategy = st.builds(
    SpreadsheetMLBasicDef::Workbook,
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
SpreadsheetMLBasicDef::SmartTagType_strategy = st.builds(
    SpreadsheetMLBasicDef::SmartTagType,
    url=
        safe_text,
    name=
        safe_text,
    namespaceuri=
        safe_text
)
SpreadsheetMLBasicDef::SmartTagsCollection_strategy = st.builds(
    SpreadsheetMLBasicDef::SmartTagsCollection,
)
SpreadsheetMLBasicDef::CustomDocumentPropertiesCollection_strategy = st.builds(
    SpreadsheetMLBasicDef::CustomDocumentPropertiesCollection,
)
CustomDocumentPropertiesCollection_strategy = st.builds(
    CustomDocumentPropertiesCollection,
)
SpreadsheetMLBasicDef::CustomDocumentProperty_strategy = st.builds(
    SpreadsheetMLBasicDef::CustomDocumentProperty,
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
SpreadsheetMLBasicDef::DocumentPropertiesCollection_strategy = st.builds(
    SpreadsheetMLBasicDef::DocumentPropertiesCollection,
    charactersWithSpaces=
        safe_text,
    appName=
        safe_text,
    keywords=
        safe_text,
    company=
        safe_text,
    category=
        safe_text,
    paragraphs=
        safe_text,
    hyperlinkBase=
        safe_text,
    pages=
        safe_text,
    presentationFormat=
        safe_text,
    lines=
        safe_text,
    title=
        safe_text,
    words=
        safe_text,
    totalTime=
        safe_text,
    revision=
        safe_text,
    description=
        safe_text,
    author=
        safe_text,
    subject=
        safe_text,
    characters=
        safe_text,
    guid=
        safe_text,
    bytes=
        safe_text,
    lastAuthor=
        safe_text,
    manager=
        safe_text
)
DateTimeType_strategy = st.builds(
    DateTimeType,
)
SpreadsheetMLBasicDef::VersionType_strategy = st.builds(
    SpreadsheetMLBasicDef::VersionType,
    n=
        safe_text,
    nn=
        safe_text
)
ValueType_strategy = st.builds(
    ValueType,
)
SpreadsheetMLBasicDef::ErrorValue_strategy = st.builds(
    SpreadsheetMLBasicDef::ErrorValue,
)
SpreadsheetMLBasicDef::BooleanValue_strategy = st.builds(
    SpreadsheetMLBasicDef::BooleanValue,
    value=
        safe_text
)
SpreadsheetMLBasicDef::NumberValue_strategy = st.builds(
    SpreadsheetMLBasicDef::NumberValue,
    value=
        safe_text
)
SpreadsheetMLBasicDef::DateTimeTypeValue_strategy = st.builds(
    SpreadsheetMLBasicDef::DateTimeTypeValue,
)
SpreadsheetMLBasicDef::StringValue_strategy = st.builds(
    SpreadsheetMLBasicDef::StringValue,
    value=
        safe_text
)
Data_strategy = st.builds(
    Data,
)
SpreadsheetMLBasicDef::ValueType_strategy = st.builds(
    SpreadsheetMLBasicDef::ValueType,
)
SpreadsheetMLBasicDef::DateTimeType_strategy = st.builds(
    SpreadsheetMLBasicDef::DateTimeType,
    minute=
        safe_text,
    hour=
        safe_text,
    year=
        safe_text,
    day=
        safe_text,
    month=
        safe_text,
    second=
        safe_text
)

@given(instance=SpreadsheetMLBasicDef::Comment_strategy)
@settings(max_examples=50)
def test_spreadsheetmlbasicdef::comment_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLBasicDef::Comment)

@given(instance=SpreadsheetMLBasicDef::Comment_strategy)
def test_spreadsheetmlbasicdef::comment_showAlways_type(instance):
    assert isinstance(instance.showAlways, str)


@given(instance=SpreadsheetMLBasicDef::Comment_strategy)
def test_spreadsheetmlbasicdef::comment_showAlways_setter(instance):
    original = instance.showAlways
    instance.showAlways = original
    assert instance.showAlways == original

@given(instance=SpreadsheetMLBasicDef::Comment_strategy)
def test_spreadsheetmlbasicdef::comment_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=SpreadsheetMLBasicDef::Comment_strategy)
def test_spreadsheetmlbasicdef::comment_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=SpreadsheetMLBasicDef::Data_strategy)
@settings(max_examples=50)
def test_spreadsheetmlbasicdef::data_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLBasicDef::Data)

@given(instance=Comment_strategy)
@settings(max_examples=50)
def test_comment_instantiation(instance):
    assert isinstance(instance, Comment)

@given(instance=ColOrRowElement_strategy)
@settings(max_examples=50)
def test_colorrowelement_instantiation(instance):
    assert isinstance(instance, ColOrRowElement)

@given(instance=SpreadsheetMLBasicDef::Column_strategy)
@settings(max_examples=50)
def test_spreadsheetmlbasicdef::column_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLBasicDef::Column)

@given(instance=SpreadsheetMLBasicDef::Column_strategy)
def test_spreadsheetmlbasicdef::column_autoFitWidth_type(instance):
    assert isinstance(instance.autoFitWidth, str)


@given(instance=SpreadsheetMLBasicDef::Column_strategy)
def test_spreadsheetmlbasicdef::column_autoFitWidth_setter(instance):
    original = instance.autoFitWidth
    instance.autoFitWidth = original
    assert instance.autoFitWidth == original

@given(instance=SpreadsheetMLBasicDef::Column_strategy)
def test_spreadsheetmlbasicdef::column_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=SpreadsheetMLBasicDef::Column_strategy)
def test_spreadsheetmlbasicdef::column_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=TableElement_strategy)
@settings(max_examples=50)
def test_tableelement_instantiation(instance):
    assert isinstance(instance, TableElement)

@given(instance=SpreadsheetMLBasicDef::Cell_strategy)
@settings(max_examples=50)
def test_spreadsheetmlbasicdef::cell_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLBasicDef::Cell)

@given(instance=SpreadsheetMLBasicDef::Cell_strategy)
def test_spreadsheetmlbasicdef::cell_hRef_type(instance):
    assert isinstance(instance.hRef, str)


@given(instance=SpreadsheetMLBasicDef::Cell_strategy)
def test_spreadsheetmlbasicdef::cell_hRef_setter(instance):
    original = instance.hRef
    instance.hRef = original
    assert instance.hRef == original

@given(instance=SpreadsheetMLBasicDef::Cell_strategy)
def test_spreadsheetmlbasicdef::cell_mergeDown_type(instance):
    assert isinstance(instance.mergeDown, str)


@given(instance=SpreadsheetMLBasicDef::Cell_strategy)
def test_spreadsheetmlbasicdef::cell_mergeDown_setter(instance):
    original = instance.mergeDown
    instance.mergeDown = original
    assert instance.mergeDown == original

@given(instance=SpreadsheetMLBasicDef::Cell_strategy)
def test_spreadsheetmlbasicdef::cell_mergeAcross_type(instance):
    assert isinstance(instance.mergeAcross, str)


@given(instance=SpreadsheetMLBasicDef::Cell_strategy)
def test_spreadsheetmlbasicdef::cell_mergeAcross_setter(instance):
    original = instance.mergeAcross
    instance.mergeAcross = original
    assert instance.mergeAcross == original

@given(instance=SpreadsheetMLBasicDef::Cell_strategy)
def test_spreadsheetmlbasicdef::cell_arrayRange_type(instance):
    assert isinstance(instance.arrayRange, str)


@given(instance=SpreadsheetMLBasicDef::Cell_strategy)
def test_spreadsheetmlbasicdef::cell_arrayRange_setter(instance):
    original = instance.arrayRange
    instance.arrayRange = original
    assert instance.arrayRange == original

@given(instance=SpreadsheetMLBasicDef::Cell_strategy)
def test_spreadsheetmlbasicdef::cell_formula_type(instance):
    assert isinstance(instance.formula, str)


@given(instance=SpreadsheetMLBasicDef::Cell_strategy)
def test_spreadsheetmlbasicdef::cell_formula_setter(instance):
    original = instance.formula
    instance.formula = original
    assert instance.formula == original

@given(instance=SpreadsheetMLBasicDef::Row_strategy)
@settings(max_examples=50)
def test_spreadsheetmlbasicdef::row_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLBasicDef::Row)

@given(instance=SpreadsheetMLBasicDef::Row_strategy)
def test_spreadsheetmlbasicdef::row_height_type(instance):
    assert isinstance(instance.height, str)


@given(instance=SpreadsheetMLBasicDef::Row_strategy)
def test_spreadsheetmlbasicdef::row_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=SpreadsheetMLBasicDef::Row_strategy)
def test_spreadsheetmlbasicdef::row_autoFitHeight_type(instance):
    assert isinstance(instance.autoFitHeight, str)


@given(instance=SpreadsheetMLBasicDef::Row_strategy)
def test_spreadsheetmlbasicdef::row_autoFitHeight_setter(instance):
    original = instance.autoFitHeight
    instance.autoFitHeight = original
    assert instance.autoFitHeight == original

@given(instance=Row_strategy)
@settings(max_examples=50)
def test_row_instantiation(instance):
    assert isinstance(instance, Row)

@given(instance=SpreadsheetMLBasicDef::ColOrRowElement_strategy)
@settings(max_examples=50)
def test_spreadsheetmlbasicdef::colorrowelement_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLBasicDef::ColOrRowElement)

@given(instance=SpreadsheetMLBasicDef::ColOrRowElement_strategy)
def test_spreadsheetmlbasicdef::colorrowelement_hidden_type(instance):
    assert isinstance(instance.hidden, str)


@given(instance=SpreadsheetMLBasicDef::ColOrRowElement_strategy)
def test_spreadsheetmlbasicdef::colorrowelement_hidden_setter(instance):
    original = instance.hidden
    instance.hidden = original
    assert instance.hidden == original

@given(instance=SpreadsheetMLBasicDef::ColOrRowElement_strategy)
def test_spreadsheetmlbasicdef::colorrowelement_span_type(instance):
    assert isinstance(instance.span, str)


@given(instance=SpreadsheetMLBasicDef::ColOrRowElement_strategy)
def test_spreadsheetmlbasicdef::colorrowelement_span_setter(instance):
    original = instance.span
    instance.span = original
    assert instance.span == original

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)

@given(instance=SpreadsheetMLBasicDef::Worksheet_strategy)
@settings(max_examples=50)
def test_spreadsheetmlbasicdef::worksheet_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLBasicDef::Worksheet)

@given(instance=SpreadsheetMLBasicDef::Worksheet_strategy)
def test_spreadsheetmlbasicdef::worksheet_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SpreadsheetMLBasicDef::Worksheet_strategy)
def test_spreadsheetmlbasicdef::worksheet_name_setter(instance):
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

@given(instance=SpreadsheetMLBasicDef::TableElement_strategy)
@settings(max_examples=50)
def test_spreadsheetmlbasicdef::tableelement_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLBasicDef::TableElement)

@given(instance=SpreadsheetMLBasicDef::TableElement_strategy)
def test_spreadsheetmlbasicdef::tableelement_index_type(instance):
    assert isinstance(instance.index, str)


@given(instance=SpreadsheetMLBasicDef::TableElement_strategy)
def test_spreadsheetmlbasicdef::tableelement_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original

@given(instance=SpreadsheetMLBasicDef::Table_strategy)
@settings(max_examples=50)
def test_spreadsheetmlbasicdef::table_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLBasicDef::Table)

@given(instance=SpreadsheetMLBasicDef::Table_strategy)
def test_spreadsheetmlbasicdef::table_leftCell_type(instance):
    assert isinstance(instance.leftCell, str)


@given(instance=SpreadsheetMLBasicDef::Table_strategy)
def test_spreadsheetmlbasicdef::table_leftCell_setter(instance):
    original = instance.leftCell
    instance.leftCell = original
    assert instance.leftCell == original

@given(instance=SpreadsheetMLBasicDef::Table_strategy)
def test_spreadsheetmlbasicdef::table_expandedColumnCount_type(instance):
    assert isinstance(instance.expandedColumnCount, str)


@given(instance=SpreadsheetMLBasicDef::Table_strategy)
def test_spreadsheetmlbasicdef::table_expandedColumnCount_setter(instance):
    original = instance.expandedColumnCount
    instance.expandedColumnCount = original
    assert instance.expandedColumnCount == original

@given(instance=SpreadsheetMLBasicDef::Table_strategy)
def test_spreadsheetmlbasicdef::table_defaultRowHeight_type(instance):
    assert isinstance(instance.defaultRowHeight, str)


@given(instance=SpreadsheetMLBasicDef::Table_strategy)
def test_spreadsheetmlbasicdef::table_defaultRowHeight_setter(instance):
    original = instance.defaultRowHeight
    instance.defaultRowHeight = original
    assert instance.defaultRowHeight == original

@given(instance=SpreadsheetMLBasicDef::Table_strategy)
def test_spreadsheetmlbasicdef::table_topCell_type(instance):
    assert isinstance(instance.topCell, str)


@given(instance=SpreadsheetMLBasicDef::Table_strategy)
def test_spreadsheetmlbasicdef::table_topCell_setter(instance):
    original = instance.topCell
    instance.topCell = original
    assert instance.topCell == original

@given(instance=SpreadsheetMLBasicDef::Table_strategy)
def test_spreadsheetmlbasicdef::table_fullColumns_type(instance):
    assert isinstance(instance.fullColumns, str)


@given(instance=SpreadsheetMLBasicDef::Table_strategy)
def test_spreadsheetmlbasicdef::table_fullColumns_setter(instance):
    original = instance.fullColumns
    instance.fullColumns = original
    assert instance.fullColumns == original

@given(instance=SpreadsheetMLBasicDef::Table_strategy)
def test_spreadsheetmlbasicdef::table_expandedRowCount_type(instance):
    assert isinstance(instance.expandedRowCount, str)


@given(instance=SpreadsheetMLBasicDef::Table_strategy)
def test_spreadsheetmlbasicdef::table_expandedRowCount_setter(instance):
    original = instance.expandedRowCount
    instance.expandedRowCount = original
    assert instance.expandedRowCount == original

@given(instance=SpreadsheetMLBasicDef::Table_strategy)
def test_spreadsheetmlbasicdef::table_fullRows_type(instance):
    assert isinstance(instance.fullRows, str)


@given(instance=SpreadsheetMLBasicDef::Table_strategy)
def test_spreadsheetmlbasicdef::table_fullRows_setter(instance):
    original = instance.fullRows
    instance.fullRows = original
    assert instance.fullRows == original

@given(instance=SpreadsheetMLBasicDef::Table_strategy)
def test_spreadsheetmlbasicdef::table_defaultColumnWidth_type(instance):
    assert isinstance(instance.defaultColumnWidth, str)


@given(instance=SpreadsheetMLBasicDef::Table_strategy)
def test_spreadsheetmlbasicdef::table_defaultColumnWidth_setter(instance):
    original = instance.defaultColumnWidth
    instance.defaultColumnWidth = original
    assert instance.defaultColumnWidth == original

@given(instance=SpreadsheetMLBasicDef::StyledElement_strategy)
@settings(max_examples=50)
def test_spreadsheetmlbasicdef::styledelement_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLBasicDef::StyledElement)

@given(instance=SpreadsheetMLBasicDef::Workbook_strategy)
@settings(max_examples=50)
def test_spreadsheetmlbasicdef::workbook_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLBasicDef::Workbook)

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

@given(instance=SpreadsheetMLBasicDef::SmartTagType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlbasicdef::smarttagtype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLBasicDef::SmartTagType)

@given(instance=SpreadsheetMLBasicDef::SmartTagType_strategy)
def test_spreadsheetmlbasicdef::smarttagtype_url_type(instance):
    assert isinstance(instance.url, str)


@given(instance=SpreadsheetMLBasicDef::SmartTagType_strategy)
def test_spreadsheetmlbasicdef::smarttagtype_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=SpreadsheetMLBasicDef::SmartTagType_strategy)
def test_spreadsheetmlbasicdef::smarttagtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SpreadsheetMLBasicDef::SmartTagType_strategy)
def test_spreadsheetmlbasicdef::smarttagtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SpreadsheetMLBasicDef::SmartTagType_strategy)
def test_spreadsheetmlbasicdef::smarttagtype_namespaceuri_type(instance):
    assert isinstance(instance.namespaceuri, str)


@given(instance=SpreadsheetMLBasicDef::SmartTagType_strategy)
def test_spreadsheetmlbasicdef::smarttagtype_namespaceuri_setter(instance):
    original = instance.namespaceuri
    instance.namespaceuri = original
    assert instance.namespaceuri == original

@given(instance=SpreadsheetMLBasicDef::SmartTagsCollection_strategy)
@settings(max_examples=50)
def test_spreadsheetmlbasicdef::smarttagscollection_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLBasicDef::SmartTagsCollection)

@given(instance=SpreadsheetMLBasicDef::CustomDocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_spreadsheetmlbasicdef::customdocumentpropertiescollection_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLBasicDef::CustomDocumentPropertiesCollection)

@given(instance=CustomDocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_customdocumentpropertiescollection_instantiation(instance):
    assert isinstance(instance, CustomDocumentPropertiesCollection)

@given(instance=SpreadsheetMLBasicDef::CustomDocumentProperty_strategy)
@settings(max_examples=50)
def test_spreadsheetmlbasicdef::customdocumentproperty_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLBasicDef::CustomDocumentProperty)

@given(instance=SpreadsheetMLBasicDef::CustomDocumentProperty_strategy)
def test_spreadsheetmlbasicdef::customdocumentproperty_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SpreadsheetMLBasicDef::CustomDocumentProperty_strategy)
def test_spreadsheetmlbasicdef::customdocumentproperty_name_setter(instance):
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

@given(instance=SpreadsheetMLBasicDef::DocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_spreadsheetmlbasicdef::documentpropertiescollection_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLBasicDef::DocumentPropertiesCollection)

@given(instance=SpreadsheetMLBasicDef::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef::documentpropertiescollection_charactersWithSpaces_type(instance):
    assert isinstance(instance.charactersWithSpaces, str)


@given(instance=SpreadsheetMLBasicDef::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef::documentpropertiescollection_charactersWithSpaces_setter(instance):
    original = instance.charactersWithSpaces
    instance.charactersWithSpaces = original
    assert instance.charactersWithSpaces == original

@given(instance=SpreadsheetMLBasicDef::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef::documentpropertiescollection_appName_type(instance):
    assert isinstance(instance.appName, str)


@given(instance=SpreadsheetMLBasicDef::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef::documentpropertiescollection_appName_setter(instance):
    original = instance.appName
    instance.appName = original
    assert instance.appName == original

@given(instance=SpreadsheetMLBasicDef::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef::documentpropertiescollection_keywords_type(instance):
    assert isinstance(instance.keywords, str)


@given(instance=SpreadsheetMLBasicDef::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef::documentpropertiescollection_keywords_setter(instance):
    original = instance.keywords
    instance.keywords = original
    assert instance.keywords == original

@given(instance=SpreadsheetMLBasicDef::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef::documentpropertiescollection_company_type(instance):
    assert isinstance(instance.company, str)


@given(instance=SpreadsheetMLBasicDef::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef::documentpropertiescollection_company_setter(instance):
    original = instance.company
    instance.company = original
    assert instance.company == original

@given(instance=SpreadsheetMLBasicDef::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef::documentpropertiescollection_category_type(instance):
    assert isinstance(instance.category, str)


@given(instance=SpreadsheetMLBasicDef::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef::documentpropertiescollection_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original

@given(instance=SpreadsheetMLBasicDef::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef::documentpropertiescollection_paragraphs_type(instance):
    assert isinstance(instance.paragraphs, str)


@given(instance=SpreadsheetMLBasicDef::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef::documentpropertiescollection_paragraphs_setter(instance):
    original = instance.paragraphs
    instance.paragraphs = original
    assert instance.paragraphs == original

@given(instance=SpreadsheetMLBasicDef::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef::documentpropertiescollection_hyperlinkBase_type(instance):
    assert isinstance(instance.hyperlinkBase, str)


@given(instance=SpreadsheetMLBasicDef::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef::documentpropertiescollection_hyperlinkBase_setter(instance):
    original = instance.hyperlinkBase
    instance.hyperlinkBase = original
    assert instance.hyperlinkBase == original

@given(instance=SpreadsheetMLBasicDef::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef::documentpropertiescollection_pages_type(instance):
    assert isinstance(instance.pages, str)


@given(instance=SpreadsheetMLBasicDef::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef::documentpropertiescollection_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=SpreadsheetMLBasicDef::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef::documentpropertiescollection_presentationFormat_type(instance):
    assert isinstance(instance.presentationFormat, str)


@given(instance=SpreadsheetMLBasicDef::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef::documentpropertiescollection_presentationFormat_setter(instance):
    original = instance.presentationFormat
    instance.presentationFormat = original
    assert instance.presentationFormat == original

@given(instance=SpreadsheetMLBasicDef::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef::documentpropertiescollection_lines_type(instance):
    assert isinstance(instance.lines, str)


@given(instance=SpreadsheetMLBasicDef::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef::documentpropertiescollection_lines_setter(instance):
    original = instance.lines
    instance.lines = original
    assert instance.lines == original

@given(instance=SpreadsheetMLBasicDef::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef::documentpropertiescollection_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=SpreadsheetMLBasicDef::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef::documentpropertiescollection_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=SpreadsheetMLBasicDef::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef::documentpropertiescollection_words_type(instance):
    assert isinstance(instance.words, str)


@given(instance=SpreadsheetMLBasicDef::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef::documentpropertiescollection_words_setter(instance):
    original = instance.words
    instance.words = original
    assert instance.words == original

@given(instance=SpreadsheetMLBasicDef::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef::documentpropertiescollection_totalTime_type(instance):
    assert isinstance(instance.totalTime, str)


@given(instance=SpreadsheetMLBasicDef::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef::documentpropertiescollection_totalTime_setter(instance):
    original = instance.totalTime
    instance.totalTime = original
    assert instance.totalTime == original

@given(instance=SpreadsheetMLBasicDef::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef::documentpropertiescollection_revision_type(instance):
    assert isinstance(instance.revision, str)


@given(instance=SpreadsheetMLBasicDef::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef::documentpropertiescollection_revision_setter(instance):
    original = instance.revision
    instance.revision = original
    assert instance.revision == original

@given(instance=SpreadsheetMLBasicDef::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef::documentpropertiescollection_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=SpreadsheetMLBasicDef::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef::documentpropertiescollection_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=SpreadsheetMLBasicDef::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef::documentpropertiescollection_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=SpreadsheetMLBasicDef::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef::documentpropertiescollection_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=SpreadsheetMLBasicDef::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef::documentpropertiescollection_subject_type(instance):
    assert isinstance(instance.subject, str)


@given(instance=SpreadsheetMLBasicDef::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef::documentpropertiescollection_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original

@given(instance=SpreadsheetMLBasicDef::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef::documentpropertiescollection_characters_type(instance):
    assert isinstance(instance.characters, str)


@given(instance=SpreadsheetMLBasicDef::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef::documentpropertiescollection_characters_setter(instance):
    original = instance.characters
    instance.characters = original
    assert instance.characters == original

@given(instance=SpreadsheetMLBasicDef::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef::documentpropertiescollection_guid_type(instance):
    assert isinstance(instance.guid, str)


@given(instance=SpreadsheetMLBasicDef::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef::documentpropertiescollection_guid_setter(instance):
    original = instance.guid
    instance.guid = original
    assert instance.guid == original

@given(instance=SpreadsheetMLBasicDef::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef::documentpropertiescollection_bytes_type(instance):
    assert isinstance(instance.bytes, str)


@given(instance=SpreadsheetMLBasicDef::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef::documentpropertiescollection_bytes_setter(instance):
    original = instance.bytes
    instance.bytes = original
    assert instance.bytes == original

@given(instance=SpreadsheetMLBasicDef::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef::documentpropertiescollection_lastAuthor_type(instance):
    assert isinstance(instance.lastAuthor, str)


@given(instance=SpreadsheetMLBasicDef::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef::documentpropertiescollection_lastAuthor_setter(instance):
    original = instance.lastAuthor
    instance.lastAuthor = original
    assert instance.lastAuthor == original

@given(instance=SpreadsheetMLBasicDef::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef::documentpropertiescollection_manager_type(instance):
    assert isinstance(instance.manager, str)


@given(instance=SpreadsheetMLBasicDef::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlbasicdef::documentpropertiescollection_manager_setter(instance):
    original = instance.manager
    instance.manager = original
    assert instance.manager == original

@given(instance=DateTimeType_strategy)
@settings(max_examples=50)
def test_datetimetype_instantiation(instance):
    assert isinstance(instance, DateTimeType)

@given(instance=SpreadsheetMLBasicDef::VersionType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlbasicdef::versiontype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLBasicDef::VersionType)

@given(instance=SpreadsheetMLBasicDef::VersionType_strategy)
def test_spreadsheetmlbasicdef::versiontype_n_type(instance):
    assert isinstance(instance.n, str)


@given(instance=SpreadsheetMLBasicDef::VersionType_strategy)
def test_spreadsheetmlbasicdef::versiontype_n_setter(instance):
    original = instance.n
    instance.n = original
    assert instance.n == original

@given(instance=SpreadsheetMLBasicDef::VersionType_strategy)
def test_spreadsheetmlbasicdef::versiontype_nn_type(instance):
    assert isinstance(instance.nn, str)


@given(instance=SpreadsheetMLBasicDef::VersionType_strategy)
def test_spreadsheetmlbasicdef::versiontype_nn_setter(instance):
    original = instance.nn
    instance.nn = original
    assert instance.nn == original

@given(instance=ValueType_strategy)
@settings(max_examples=50)
def test_valuetype_instantiation(instance):
    assert isinstance(instance, ValueType)

@given(instance=SpreadsheetMLBasicDef::ErrorValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlbasicdef::errorvalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLBasicDef::ErrorValue)

@given(instance=SpreadsheetMLBasicDef::BooleanValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlbasicdef::booleanvalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLBasicDef::BooleanValue)

@given(instance=SpreadsheetMLBasicDef::BooleanValue_strategy)
def test_spreadsheetmlbasicdef::booleanvalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=SpreadsheetMLBasicDef::BooleanValue_strategy)
def test_spreadsheetmlbasicdef::booleanvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SpreadsheetMLBasicDef::NumberValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlbasicdef::numbervalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLBasicDef::NumberValue)

@given(instance=SpreadsheetMLBasicDef::NumberValue_strategy)
def test_spreadsheetmlbasicdef::numbervalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=SpreadsheetMLBasicDef::NumberValue_strategy)
def test_spreadsheetmlbasicdef::numbervalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SpreadsheetMLBasicDef::DateTimeTypeValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlbasicdef::datetimetypevalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLBasicDef::DateTimeTypeValue)

@given(instance=SpreadsheetMLBasicDef::StringValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlbasicdef::stringvalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLBasicDef::StringValue)

@given(instance=SpreadsheetMLBasicDef::StringValue_strategy)
def test_spreadsheetmlbasicdef::stringvalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=SpreadsheetMLBasicDef::StringValue_strategy)
def test_spreadsheetmlbasicdef::stringvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Data_strategy)
@settings(max_examples=50)
def test_data_instantiation(instance):
    assert isinstance(instance, Data)

@given(instance=SpreadsheetMLBasicDef::ValueType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlbasicdef::valuetype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLBasicDef::ValueType)

@given(instance=SpreadsheetMLBasicDef::DateTimeType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlbasicdef::datetimetype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLBasicDef::DateTimeType)

@given(instance=SpreadsheetMLBasicDef::DateTimeType_strategy)
def test_spreadsheetmlbasicdef::datetimetype_minute_type(instance):
    assert isinstance(instance.minute, str)


@given(instance=SpreadsheetMLBasicDef::DateTimeType_strategy)
def test_spreadsheetmlbasicdef::datetimetype_minute_setter(instance):
    original = instance.minute
    instance.minute = original
    assert instance.minute == original

@given(instance=SpreadsheetMLBasicDef::DateTimeType_strategy)
def test_spreadsheetmlbasicdef::datetimetype_hour_type(instance):
    assert isinstance(instance.hour, str)


@given(instance=SpreadsheetMLBasicDef::DateTimeType_strategy)
def test_spreadsheetmlbasicdef::datetimetype_hour_setter(instance):
    original = instance.hour
    instance.hour = original
    assert instance.hour == original

@given(instance=SpreadsheetMLBasicDef::DateTimeType_strategy)
def test_spreadsheetmlbasicdef::datetimetype_year_type(instance):
    assert isinstance(instance.year, str)


@given(instance=SpreadsheetMLBasicDef::DateTimeType_strategy)
def test_spreadsheetmlbasicdef::datetimetype_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=SpreadsheetMLBasicDef::DateTimeType_strategy)
def test_spreadsheetmlbasicdef::datetimetype_day_type(instance):
    assert isinstance(instance.day, str)


@given(instance=SpreadsheetMLBasicDef::DateTimeType_strategy)
def test_spreadsheetmlbasicdef::datetimetype_day_setter(instance):
    original = instance.day
    instance.day = original
    assert instance.day == original

@given(instance=SpreadsheetMLBasicDef::DateTimeType_strategy)
def test_spreadsheetmlbasicdef::datetimetype_month_type(instance):
    assert isinstance(instance.month, str)


@given(instance=SpreadsheetMLBasicDef::DateTimeType_strategy)
def test_spreadsheetmlbasicdef::datetimetype_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original

@given(instance=SpreadsheetMLBasicDef::DateTimeType_strategy)
def test_spreadsheetmlbasicdef::datetimetype_second_type(instance):
    assert isinstance(instance.second, str)


@given(instance=SpreadsheetMLBasicDef::DateTimeType_strategy)
def test_spreadsheetmlbasicdef::datetimetype_second_setter(instance):
    original = instance.second
    instance.second = original
    assert instance.second == original
