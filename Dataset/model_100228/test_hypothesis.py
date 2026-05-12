import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    SpreadsheetMLSimplified::Data,
    ColOrRowElement,
    SpreadsheetMLSimplified::Column,
    Cell,
    SpreadsheetMLSimplified::Row,
    Column,
    SpreadsheetMLSimplified::Table,
    Table,
    TableElement,
    SpreadsheetMLSimplified::Cell,
    SpreadsheetMLSimplified::ColOrRowElement,
    SpreadsheetMLSimplified::TableElement,
    Row,
    DateTimeType,
    Workbook,
    SpreadsheetMLSimplified::Worksheet,
    Worksheet,
    SpreadsheetMLSimplified::Workbook,
    SpreadsheetMLSimplified::ValueType,
    ValueType,
    SpreadsheetMLSimplified::BooleanValue,
    SpreadsheetMLSimplified::NumberValue,
    SpreadsheetMLSimplified::ErrorValue,
    SpreadsheetMLSimplified::DateTimeTypeValue,
    SpreadsheetMLSimplified::StringValue,
    Data,
    SpreadsheetMLSimplified::DateTimeType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_spreadsheetmlsimplified::data_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLSimplified::Data)


def test_spreadsheetmlsimplified::data_constructor_exists():
    assert callable(SpreadsheetMLSimplified::Data.__init__)


def test_spreadsheetmlsimplified::data_constructor_args():
    sig = inspect.signature(SpreadsheetMLSimplified::Data.__init__)
    params = list(sig.parameters.keys())



def test_colorrowelement_is_not_abstract():
    assert not inspect.isabstract(ColOrRowElement)


def test_colorrowelement_constructor_exists():
    assert callable(ColOrRowElement.__init__)


def test_colorrowelement_constructor_args():
    sig = inspect.signature(ColOrRowElement.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlsimplified::column_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLSimplified::Column)


def test_spreadsheetmlsimplified::column_constructor_exists():
    assert callable(SpreadsheetMLSimplified::Column.__init__)


def test_spreadsheetmlsimplified::column_constructor_args():
    sig = inspect.signature(SpreadsheetMLSimplified::Column.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "autoFitWidth" in params, "Missing parameter 'autoFitWidth'"

def test_spreadsheetmlsimplified::column_has_width():
    assert hasattr(SpreadsheetMLSimplified::Column, "width")
    descriptor = None
    for klass in SpreadsheetMLSimplified::Column.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlsimplified::column_has_autoFitWidth():
    assert hasattr(SpreadsheetMLSimplified::Column, "autoFitWidth")
    descriptor = None
    for klass in SpreadsheetMLSimplified::Column.__mro__:
        if "autoFitWidth" in klass.__dict__:
            descriptor = klass.__dict__["autoFitWidth"]
            break
    assert isinstance(descriptor, property)



def test_cell_is_not_abstract():
    assert not inspect.isabstract(Cell)


def test_cell_constructor_exists():
    assert callable(Cell.__init__)


def test_cell_constructor_args():
    sig = inspect.signature(Cell.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlsimplified::row_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLSimplified::Row)


def test_spreadsheetmlsimplified::row_constructor_exists():
    assert callable(SpreadsheetMLSimplified::Row.__init__)


def test_spreadsheetmlsimplified::row_constructor_args():
    sig = inspect.signature(SpreadsheetMLSimplified::Row.__init__)
    params = list(sig.parameters.keys())
    assert "autoFitHeight" in params, "Missing parameter 'autoFitHeight'"
    assert "height" in params, "Missing parameter 'height'"

def test_spreadsheetmlsimplified::row_has_autoFitHeight():
    assert hasattr(SpreadsheetMLSimplified::Row, "autoFitHeight")
    descriptor = None
    for klass in SpreadsheetMLSimplified::Row.__mro__:
        if "autoFitHeight" in klass.__dict__:
            descriptor = klass.__dict__["autoFitHeight"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlsimplified::row_has_height():
    assert hasattr(SpreadsheetMLSimplified::Row, "height")
    descriptor = None
    for klass in SpreadsheetMLSimplified::Row.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_column_is_not_abstract():
    assert not inspect.isabstract(Column)


def test_column_constructor_exists():
    assert callable(Column.__init__)


def test_column_constructor_args():
    sig = inspect.signature(Column.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlsimplified::table_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLSimplified::Table)


def test_spreadsheetmlsimplified::table_constructor_exists():
    assert callable(SpreadsheetMLSimplified::Table.__init__)


def test_spreadsheetmlsimplified::table_constructor_args():
    sig = inspect.signature(SpreadsheetMLSimplified::Table.__init__)
    params = list(sig.parameters.keys())



def test_table_is_not_abstract():
    assert not inspect.isabstract(Table)


def test_table_constructor_exists():
    assert callable(Table.__init__)


def test_table_constructor_args():
    sig = inspect.signature(Table.__init__)
    params = list(sig.parameters.keys())



def test_tableelement_is_not_abstract():
    assert not inspect.isabstract(TableElement)


def test_tableelement_constructor_exists():
    assert callable(TableElement.__init__)


def test_tableelement_constructor_args():
    sig = inspect.signature(TableElement.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlsimplified::cell_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLSimplified::Cell)


def test_spreadsheetmlsimplified::cell_constructor_exists():
    assert callable(SpreadsheetMLSimplified::Cell.__init__)


def test_spreadsheetmlsimplified::cell_constructor_args():
    sig = inspect.signature(SpreadsheetMLSimplified::Cell.__init__)
    params = list(sig.parameters.keys())
    assert "formula" in params, "Missing parameter 'formula'"
    assert "arrayRange" in params, "Missing parameter 'arrayRange'"
    assert "hRef" in params, "Missing parameter 'hRef'"
    assert "mergeDown" in params, "Missing parameter 'mergeDown'"
    assert "mergeAcross" in params, "Missing parameter 'mergeAcross'"

def test_spreadsheetmlsimplified::cell_has_formula():
    assert hasattr(SpreadsheetMLSimplified::Cell, "formula")
    descriptor = None
    for klass in SpreadsheetMLSimplified::Cell.__mro__:
        if "formula" in klass.__dict__:
            descriptor = klass.__dict__["formula"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlsimplified::cell_has_arrayRange():
    assert hasattr(SpreadsheetMLSimplified::Cell, "arrayRange")
    descriptor = None
    for klass in SpreadsheetMLSimplified::Cell.__mro__:
        if "arrayRange" in klass.__dict__:
            descriptor = klass.__dict__["arrayRange"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlsimplified::cell_has_hRef():
    assert hasattr(SpreadsheetMLSimplified::Cell, "hRef")
    descriptor = None
    for klass in SpreadsheetMLSimplified::Cell.__mro__:
        if "hRef" in klass.__dict__:
            descriptor = klass.__dict__["hRef"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlsimplified::cell_has_mergeDown():
    assert hasattr(SpreadsheetMLSimplified::Cell, "mergeDown")
    descriptor = None
    for klass in SpreadsheetMLSimplified::Cell.__mro__:
        if "mergeDown" in klass.__dict__:
            descriptor = klass.__dict__["mergeDown"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlsimplified::cell_has_mergeAcross():
    assert hasattr(SpreadsheetMLSimplified::Cell, "mergeAcross")
    descriptor = None
    for klass in SpreadsheetMLSimplified::Cell.__mro__:
        if "mergeAcross" in klass.__dict__:
            descriptor = klass.__dict__["mergeAcross"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlsimplified::colorrowelement_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLSimplified::ColOrRowElement)


def test_spreadsheetmlsimplified::colorrowelement_constructor_exists():
    assert callable(SpreadsheetMLSimplified::ColOrRowElement.__init__)


def test_spreadsheetmlsimplified::colorrowelement_constructor_args():
    sig = inspect.signature(SpreadsheetMLSimplified::ColOrRowElement.__init__)
    params = list(sig.parameters.keys())
    assert "hidden" in params, "Missing parameter 'hidden'"
    assert "span" in params, "Missing parameter 'span'"

def test_spreadsheetmlsimplified::colorrowelement_has_hidden():
    assert hasattr(SpreadsheetMLSimplified::ColOrRowElement, "hidden")
    descriptor = None
    for klass in SpreadsheetMLSimplified::ColOrRowElement.__mro__:
        if "hidden" in klass.__dict__:
            descriptor = klass.__dict__["hidden"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlsimplified::colorrowelement_has_span():
    assert hasattr(SpreadsheetMLSimplified::ColOrRowElement, "span")
    descriptor = None
    for klass in SpreadsheetMLSimplified::ColOrRowElement.__mro__:
        if "span" in klass.__dict__:
            descriptor = klass.__dict__["span"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlsimplified::tableelement_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLSimplified::TableElement)


def test_spreadsheetmlsimplified::tableelement_constructor_exists():
    assert callable(SpreadsheetMLSimplified::TableElement.__init__)


def test_spreadsheetmlsimplified::tableelement_constructor_args():
    sig = inspect.signature(SpreadsheetMLSimplified::TableElement.__init__)
    params = list(sig.parameters.keys())
    assert "index" in params, "Missing parameter 'index'"

def test_spreadsheetmlsimplified::tableelement_has_index():
    assert hasattr(SpreadsheetMLSimplified::TableElement, "index")
    descriptor = None
    for klass in SpreadsheetMLSimplified::TableElement.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)



def test_row_is_not_abstract():
    assert not inspect.isabstract(Row)


def test_row_constructor_exists():
    assert callable(Row.__init__)


def test_row_constructor_args():
    sig = inspect.signature(Row.__init__)
    params = list(sig.parameters.keys())



def test_datetimetype_is_not_abstract():
    assert not inspect.isabstract(DateTimeType)


def test_datetimetype_constructor_exists():
    assert callable(DateTimeType.__init__)


def test_datetimetype_constructor_args():
    sig = inspect.signature(DateTimeType.__init__)
    params = list(sig.parameters.keys())



def test_workbook_is_not_abstract():
    assert not inspect.isabstract(Workbook)


def test_workbook_constructor_exists():
    assert callable(Workbook.__init__)


def test_workbook_constructor_args():
    sig = inspect.signature(Workbook.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlsimplified::worksheet_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLSimplified::Worksheet)


def test_spreadsheetmlsimplified::worksheet_constructor_exists():
    assert callable(SpreadsheetMLSimplified::Worksheet.__init__)


def test_spreadsheetmlsimplified::worksheet_constructor_args():
    sig = inspect.signature(SpreadsheetMLSimplified::Worksheet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_spreadsheetmlsimplified::worksheet_has_name():
    assert hasattr(SpreadsheetMLSimplified::Worksheet, "name")
    descriptor = None
    for klass in SpreadsheetMLSimplified::Worksheet.__mro__:
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



def test_spreadsheetmlsimplified::workbook_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLSimplified::Workbook)


def test_spreadsheetmlsimplified::workbook_constructor_exists():
    assert callable(SpreadsheetMLSimplified::Workbook.__init__)


def test_spreadsheetmlsimplified::workbook_constructor_args():
    sig = inspect.signature(SpreadsheetMLSimplified::Workbook.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlsimplified::valuetype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLSimplified::ValueType)


def test_spreadsheetmlsimplified::valuetype_constructor_exists():
    assert callable(SpreadsheetMLSimplified::ValueType.__init__)


def test_spreadsheetmlsimplified::valuetype_constructor_args():
    sig = inspect.signature(SpreadsheetMLSimplified::ValueType.__init__)
    params = list(sig.parameters.keys())



def test_valuetype_is_not_abstract():
    assert not inspect.isabstract(ValueType)


def test_valuetype_constructor_exists():
    assert callable(ValueType.__init__)


def test_valuetype_constructor_args():
    sig = inspect.signature(ValueType.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlsimplified::booleanvalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLSimplified::BooleanValue)


def test_spreadsheetmlsimplified::booleanvalue_constructor_exists():
    assert callable(SpreadsheetMLSimplified::BooleanValue.__init__)


def test_spreadsheetmlsimplified::booleanvalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLSimplified::BooleanValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_spreadsheetmlsimplified::booleanvalue_has_value():
    assert hasattr(SpreadsheetMLSimplified::BooleanValue, "value")
    descriptor = None
    for klass in SpreadsheetMLSimplified::BooleanValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlsimplified::numbervalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLSimplified::NumberValue)


def test_spreadsheetmlsimplified::numbervalue_constructor_exists():
    assert callable(SpreadsheetMLSimplified::NumberValue.__init__)


def test_spreadsheetmlsimplified::numbervalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLSimplified::NumberValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_spreadsheetmlsimplified::numbervalue_has_value():
    assert hasattr(SpreadsheetMLSimplified::NumberValue, "value")
    descriptor = None
    for klass in SpreadsheetMLSimplified::NumberValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlsimplified::errorvalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLSimplified::ErrorValue)


def test_spreadsheetmlsimplified::errorvalue_constructor_exists():
    assert callable(SpreadsheetMLSimplified::ErrorValue.__init__)


def test_spreadsheetmlsimplified::errorvalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLSimplified::ErrorValue.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlsimplified::datetimetypevalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLSimplified::DateTimeTypeValue)


def test_spreadsheetmlsimplified::datetimetypevalue_constructor_exists():
    assert callable(SpreadsheetMLSimplified::DateTimeTypeValue.__init__)


def test_spreadsheetmlsimplified::datetimetypevalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLSimplified::DateTimeTypeValue.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlsimplified::stringvalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLSimplified::StringValue)


def test_spreadsheetmlsimplified::stringvalue_constructor_exists():
    assert callable(SpreadsheetMLSimplified::StringValue.__init__)


def test_spreadsheetmlsimplified::stringvalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLSimplified::StringValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_spreadsheetmlsimplified::stringvalue_has_value():
    assert hasattr(SpreadsheetMLSimplified::StringValue, "value")
    descriptor = None
    for klass in SpreadsheetMLSimplified::StringValue.__mro__:
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



def test_spreadsheetmlsimplified::datetimetype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLSimplified::DateTimeType)


def test_spreadsheetmlsimplified::datetimetype_constructor_exists():
    assert callable(SpreadsheetMLSimplified::DateTimeType.__init__)


def test_spreadsheetmlsimplified::datetimetype_constructor_args():
    sig = inspect.signature(SpreadsheetMLSimplified::DateTimeType.__init__)
    params = list(sig.parameters.keys())
    assert "second" in params, "Missing parameter 'second'"
    assert "hour" in params, "Missing parameter 'hour'"
    assert "month" in params, "Missing parameter 'month'"
    assert "minute" in params, "Missing parameter 'minute'"
    assert "year" in params, "Missing parameter 'year'"
    assert "day" in params, "Missing parameter 'day'"

def test_spreadsheetmlsimplified::datetimetype_has_second():
    assert hasattr(SpreadsheetMLSimplified::DateTimeType, "second")
    descriptor = None
    for klass in SpreadsheetMLSimplified::DateTimeType.__mro__:
        if "second" in klass.__dict__:
            descriptor = klass.__dict__["second"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlsimplified::datetimetype_has_hour():
    assert hasattr(SpreadsheetMLSimplified::DateTimeType, "hour")
    descriptor = None
    for klass in SpreadsheetMLSimplified::DateTimeType.__mro__:
        if "hour" in klass.__dict__:
            descriptor = klass.__dict__["hour"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlsimplified::datetimetype_has_month():
    assert hasattr(SpreadsheetMLSimplified::DateTimeType, "month")
    descriptor = None
    for klass in SpreadsheetMLSimplified::DateTimeType.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlsimplified::datetimetype_has_minute():
    assert hasattr(SpreadsheetMLSimplified::DateTimeType, "minute")
    descriptor = None
    for klass in SpreadsheetMLSimplified::DateTimeType.__mro__:
        if "minute" in klass.__dict__:
            descriptor = klass.__dict__["minute"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlsimplified::datetimetype_has_year():
    assert hasattr(SpreadsheetMLSimplified::DateTimeType, "year")
    descriptor = None
    for klass in SpreadsheetMLSimplified::DateTimeType.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlsimplified::datetimetype_has_day():
    assert hasattr(SpreadsheetMLSimplified::DateTimeType, "day")
    descriptor = None
    for klass in SpreadsheetMLSimplified::DateTimeType.__mro__:
        if "day" in klass.__dict__:
            descriptor = klass.__dict__["day"]
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
SpreadsheetMLSimplified::Data_strategy = st.builds(
    SpreadsheetMLSimplified::Data,
)
ColOrRowElement_strategy = st.builds(
    ColOrRowElement,
)
SpreadsheetMLSimplified::Column_strategy = st.builds(
    SpreadsheetMLSimplified::Column,
    width=
        safe_text,
    autoFitWidth=
        safe_text
)
Cell_strategy = st.builds(
    Cell,
)
SpreadsheetMLSimplified::Row_strategy = st.builds(
    SpreadsheetMLSimplified::Row,
    autoFitHeight=
        safe_text,
    height=
        safe_text
)
Column_strategy = st.builds(
    Column,
)
SpreadsheetMLSimplified::Table_strategy = st.builds(
    SpreadsheetMLSimplified::Table,
)
Table_strategy = st.builds(
    Table,
)
TableElement_strategy = st.builds(
    TableElement,
)
SpreadsheetMLSimplified::Cell_strategy = st.builds(
    SpreadsheetMLSimplified::Cell,
    formula=
        safe_text,
    arrayRange=
        safe_text,
    hRef=
        safe_text,
    mergeDown=
        safe_text,
    mergeAcross=
        safe_text
)
SpreadsheetMLSimplified::ColOrRowElement_strategy = st.builds(
    SpreadsheetMLSimplified::ColOrRowElement,
    hidden=
        safe_text,
    span=
        safe_text
)
SpreadsheetMLSimplified::TableElement_strategy = st.builds(
    SpreadsheetMLSimplified::TableElement,
    index=
        safe_text
)
Row_strategy = st.builds(
    Row,
)
DateTimeType_strategy = st.builds(
    DateTimeType,
)
Workbook_strategy = st.builds(
    Workbook,
)
SpreadsheetMLSimplified::Worksheet_strategy = st.builds(
    SpreadsheetMLSimplified::Worksheet,
    name=
        safe_text
)
Worksheet_strategy = st.builds(
    Worksheet,
)
SpreadsheetMLSimplified::Workbook_strategy = st.builds(
    SpreadsheetMLSimplified::Workbook,
)
SpreadsheetMLSimplified::ValueType_strategy = st.builds(
    SpreadsheetMLSimplified::ValueType,
)
ValueType_strategy = st.builds(
    ValueType,
)
SpreadsheetMLSimplified::BooleanValue_strategy = st.builds(
    SpreadsheetMLSimplified::BooleanValue,
    value=
        safe_text
)
SpreadsheetMLSimplified::NumberValue_strategy = st.builds(
    SpreadsheetMLSimplified::NumberValue,
    value=
        safe_text
)
SpreadsheetMLSimplified::ErrorValue_strategy = st.builds(
    SpreadsheetMLSimplified::ErrorValue,
)
SpreadsheetMLSimplified::DateTimeTypeValue_strategy = st.builds(
    SpreadsheetMLSimplified::DateTimeTypeValue,
)
SpreadsheetMLSimplified::StringValue_strategy = st.builds(
    SpreadsheetMLSimplified::StringValue,
    value=
        safe_text
)
Data_strategy = st.builds(
    Data,
)
SpreadsheetMLSimplified::DateTimeType_strategy = st.builds(
    SpreadsheetMLSimplified::DateTimeType,
    second=
        safe_text,
    hour=
        safe_text,
    month=
        safe_text,
    minute=
        safe_text,
    year=
        safe_text,
    day=
        safe_text
)

@given(instance=SpreadsheetMLSimplified::Data_strategy)
@settings(max_examples=50)
def test_spreadsheetmlsimplified::data_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLSimplified::Data)

@given(instance=ColOrRowElement_strategy)
@settings(max_examples=50)
def test_colorrowelement_instantiation(instance):
    assert isinstance(instance, ColOrRowElement)

@given(instance=SpreadsheetMLSimplified::Column_strategy)
@settings(max_examples=50)
def test_spreadsheetmlsimplified::column_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLSimplified::Column)

@given(instance=SpreadsheetMLSimplified::Column_strategy)
def test_spreadsheetmlsimplified::column_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=SpreadsheetMLSimplified::Column_strategy)
def test_spreadsheetmlsimplified::column_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=SpreadsheetMLSimplified::Column_strategy)
def test_spreadsheetmlsimplified::column_autoFitWidth_type(instance):
    assert isinstance(instance.autoFitWidth, str)


@given(instance=SpreadsheetMLSimplified::Column_strategy)
def test_spreadsheetmlsimplified::column_autoFitWidth_setter(instance):
    original = instance.autoFitWidth
    instance.autoFitWidth = original
    assert instance.autoFitWidth == original

@given(instance=Cell_strategy)
@settings(max_examples=50)
def test_cell_instantiation(instance):
    assert isinstance(instance, Cell)

@given(instance=SpreadsheetMLSimplified::Row_strategy)
@settings(max_examples=50)
def test_spreadsheetmlsimplified::row_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLSimplified::Row)

@given(instance=SpreadsheetMLSimplified::Row_strategy)
def test_spreadsheetmlsimplified::row_autoFitHeight_type(instance):
    assert isinstance(instance.autoFitHeight, str)


@given(instance=SpreadsheetMLSimplified::Row_strategy)
def test_spreadsheetmlsimplified::row_autoFitHeight_setter(instance):
    original = instance.autoFitHeight
    instance.autoFitHeight = original
    assert instance.autoFitHeight == original

@given(instance=SpreadsheetMLSimplified::Row_strategy)
def test_spreadsheetmlsimplified::row_height_type(instance):
    assert isinstance(instance.height, str)


@given(instance=SpreadsheetMLSimplified::Row_strategy)
def test_spreadsheetmlsimplified::row_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=Column_strategy)
@settings(max_examples=50)
def test_column_instantiation(instance):
    assert isinstance(instance, Column)

@given(instance=SpreadsheetMLSimplified::Table_strategy)
@settings(max_examples=50)
def test_spreadsheetmlsimplified::table_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLSimplified::Table)

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)

@given(instance=TableElement_strategy)
@settings(max_examples=50)
def test_tableelement_instantiation(instance):
    assert isinstance(instance, TableElement)

@given(instance=SpreadsheetMLSimplified::Cell_strategy)
@settings(max_examples=50)
def test_spreadsheetmlsimplified::cell_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLSimplified::Cell)

@given(instance=SpreadsheetMLSimplified::Cell_strategy)
def test_spreadsheetmlsimplified::cell_formula_type(instance):
    assert isinstance(instance.formula, str)


@given(instance=SpreadsheetMLSimplified::Cell_strategy)
def test_spreadsheetmlsimplified::cell_formula_setter(instance):
    original = instance.formula
    instance.formula = original
    assert instance.formula == original

@given(instance=SpreadsheetMLSimplified::Cell_strategy)
def test_spreadsheetmlsimplified::cell_arrayRange_type(instance):
    assert isinstance(instance.arrayRange, str)


@given(instance=SpreadsheetMLSimplified::Cell_strategy)
def test_spreadsheetmlsimplified::cell_arrayRange_setter(instance):
    original = instance.arrayRange
    instance.arrayRange = original
    assert instance.arrayRange == original

@given(instance=SpreadsheetMLSimplified::Cell_strategy)
def test_spreadsheetmlsimplified::cell_hRef_type(instance):
    assert isinstance(instance.hRef, str)


@given(instance=SpreadsheetMLSimplified::Cell_strategy)
def test_spreadsheetmlsimplified::cell_hRef_setter(instance):
    original = instance.hRef
    instance.hRef = original
    assert instance.hRef == original

@given(instance=SpreadsheetMLSimplified::Cell_strategy)
def test_spreadsheetmlsimplified::cell_mergeDown_type(instance):
    assert isinstance(instance.mergeDown, str)


@given(instance=SpreadsheetMLSimplified::Cell_strategy)
def test_spreadsheetmlsimplified::cell_mergeDown_setter(instance):
    original = instance.mergeDown
    instance.mergeDown = original
    assert instance.mergeDown == original

@given(instance=SpreadsheetMLSimplified::Cell_strategy)
def test_spreadsheetmlsimplified::cell_mergeAcross_type(instance):
    assert isinstance(instance.mergeAcross, str)


@given(instance=SpreadsheetMLSimplified::Cell_strategy)
def test_spreadsheetmlsimplified::cell_mergeAcross_setter(instance):
    original = instance.mergeAcross
    instance.mergeAcross = original
    assert instance.mergeAcross == original

@given(instance=SpreadsheetMLSimplified::ColOrRowElement_strategy)
@settings(max_examples=50)
def test_spreadsheetmlsimplified::colorrowelement_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLSimplified::ColOrRowElement)

@given(instance=SpreadsheetMLSimplified::ColOrRowElement_strategy)
def test_spreadsheetmlsimplified::colorrowelement_hidden_type(instance):
    assert isinstance(instance.hidden, str)


@given(instance=SpreadsheetMLSimplified::ColOrRowElement_strategy)
def test_spreadsheetmlsimplified::colorrowelement_hidden_setter(instance):
    original = instance.hidden
    instance.hidden = original
    assert instance.hidden == original

@given(instance=SpreadsheetMLSimplified::ColOrRowElement_strategy)
def test_spreadsheetmlsimplified::colorrowelement_span_type(instance):
    assert isinstance(instance.span, str)


@given(instance=SpreadsheetMLSimplified::ColOrRowElement_strategy)
def test_spreadsheetmlsimplified::colorrowelement_span_setter(instance):
    original = instance.span
    instance.span = original
    assert instance.span == original

@given(instance=SpreadsheetMLSimplified::TableElement_strategy)
@settings(max_examples=50)
def test_spreadsheetmlsimplified::tableelement_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLSimplified::TableElement)

@given(instance=SpreadsheetMLSimplified::TableElement_strategy)
def test_spreadsheetmlsimplified::tableelement_index_type(instance):
    assert isinstance(instance.index, str)


@given(instance=SpreadsheetMLSimplified::TableElement_strategy)
def test_spreadsheetmlsimplified::tableelement_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original

@given(instance=Row_strategy)
@settings(max_examples=50)
def test_row_instantiation(instance):
    assert isinstance(instance, Row)

@given(instance=DateTimeType_strategy)
@settings(max_examples=50)
def test_datetimetype_instantiation(instance):
    assert isinstance(instance, DateTimeType)

@given(instance=Workbook_strategy)
@settings(max_examples=50)
def test_workbook_instantiation(instance):
    assert isinstance(instance, Workbook)

@given(instance=SpreadsheetMLSimplified::Worksheet_strategy)
@settings(max_examples=50)
def test_spreadsheetmlsimplified::worksheet_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLSimplified::Worksheet)

@given(instance=SpreadsheetMLSimplified::Worksheet_strategy)
def test_spreadsheetmlsimplified::worksheet_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SpreadsheetMLSimplified::Worksheet_strategy)
def test_spreadsheetmlsimplified::worksheet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Worksheet_strategy)
@settings(max_examples=50)
def test_worksheet_instantiation(instance):
    assert isinstance(instance, Worksheet)

@given(instance=SpreadsheetMLSimplified::Workbook_strategy)
@settings(max_examples=50)
def test_spreadsheetmlsimplified::workbook_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLSimplified::Workbook)

@given(instance=SpreadsheetMLSimplified::ValueType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlsimplified::valuetype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLSimplified::ValueType)

@given(instance=ValueType_strategy)
@settings(max_examples=50)
def test_valuetype_instantiation(instance):
    assert isinstance(instance, ValueType)

@given(instance=SpreadsheetMLSimplified::BooleanValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlsimplified::booleanvalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLSimplified::BooleanValue)

@given(instance=SpreadsheetMLSimplified::BooleanValue_strategy)
def test_spreadsheetmlsimplified::booleanvalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=SpreadsheetMLSimplified::BooleanValue_strategy)
def test_spreadsheetmlsimplified::booleanvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SpreadsheetMLSimplified::NumberValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlsimplified::numbervalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLSimplified::NumberValue)

@given(instance=SpreadsheetMLSimplified::NumberValue_strategy)
def test_spreadsheetmlsimplified::numbervalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=SpreadsheetMLSimplified::NumberValue_strategy)
def test_spreadsheetmlsimplified::numbervalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SpreadsheetMLSimplified::ErrorValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlsimplified::errorvalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLSimplified::ErrorValue)

@given(instance=SpreadsheetMLSimplified::DateTimeTypeValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlsimplified::datetimetypevalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLSimplified::DateTimeTypeValue)

@given(instance=SpreadsheetMLSimplified::StringValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlsimplified::stringvalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLSimplified::StringValue)

@given(instance=SpreadsheetMLSimplified::StringValue_strategy)
def test_spreadsheetmlsimplified::stringvalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=SpreadsheetMLSimplified::StringValue_strategy)
def test_spreadsheetmlsimplified::stringvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Data_strategy)
@settings(max_examples=50)
def test_data_instantiation(instance):
    assert isinstance(instance, Data)

@given(instance=SpreadsheetMLSimplified::DateTimeType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlsimplified::datetimetype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLSimplified::DateTimeType)

@given(instance=SpreadsheetMLSimplified::DateTimeType_strategy)
def test_spreadsheetmlsimplified::datetimetype_second_type(instance):
    assert isinstance(instance.second, str)


@given(instance=SpreadsheetMLSimplified::DateTimeType_strategy)
def test_spreadsheetmlsimplified::datetimetype_second_setter(instance):
    original = instance.second
    instance.second = original
    assert instance.second == original

@given(instance=SpreadsheetMLSimplified::DateTimeType_strategy)
def test_spreadsheetmlsimplified::datetimetype_hour_type(instance):
    assert isinstance(instance.hour, str)


@given(instance=SpreadsheetMLSimplified::DateTimeType_strategy)
def test_spreadsheetmlsimplified::datetimetype_hour_setter(instance):
    original = instance.hour
    instance.hour = original
    assert instance.hour == original

@given(instance=SpreadsheetMLSimplified::DateTimeType_strategy)
def test_spreadsheetmlsimplified::datetimetype_month_type(instance):
    assert isinstance(instance.month, str)


@given(instance=SpreadsheetMLSimplified::DateTimeType_strategy)
def test_spreadsheetmlsimplified::datetimetype_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original

@given(instance=SpreadsheetMLSimplified::DateTimeType_strategy)
def test_spreadsheetmlsimplified::datetimetype_minute_type(instance):
    assert isinstance(instance.minute, str)


@given(instance=SpreadsheetMLSimplified::DateTimeType_strategy)
def test_spreadsheetmlsimplified::datetimetype_minute_setter(instance):
    original = instance.minute
    instance.minute = original
    assert instance.minute == original

@given(instance=SpreadsheetMLSimplified::DateTimeType_strategy)
def test_spreadsheetmlsimplified::datetimetype_year_type(instance):
    assert isinstance(instance.year, str)


@given(instance=SpreadsheetMLSimplified::DateTimeType_strategy)
def test_spreadsheetmlsimplified::datetimetype_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=SpreadsheetMLSimplified::DateTimeType_strategy)
def test_spreadsheetmlsimplified::datetimetype_day_type(instance):
    assert isinstance(instance.day, str)


@given(instance=SpreadsheetMLSimplified::DateTimeType_strategy)
def test_spreadsheetmlsimplified::datetimetype_day_setter(instance):
    original = instance.day
    instance.day = original
    assert instance.day == original
