import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    SpreadsheetMLSimplified_Data,
    Cell,
    ColOrRowElement,
    SpreadsheetMLSimplified_Row,
    SpreadsheetMLSimplified_Column,
    TableElement,
    SpreadsheetMLSimplified_Cell,
    SpreadsheetMLSimplified_ColOrRowElement,
    SpreadsheetMLSimplified_TableElement,
    Row,
    Column,
    SpreadsheetMLSimplified_Table,
    Table,
    Workbook,
    SpreadsheetMLSimplified_Worksheet,
    Worksheet,
    SpreadsheetMLSimplified_Workbook,
    Data,
    DateTimeType,
    ValueType,
    SpreadsheetMLSimplified_DateTimeTypeValue,
    SpreadsheetMLSimplified_ErrorValue,
    SpreadsheetMLSimplified_NumberValue,
    SpreadsheetMLSimplified_BooleanValue,
    SpreadsheetMLSimplified_StringValue,
    SpreadsheetMLSimplified_ValueType,
    SpreadsheetMLSimplified_DateTimeType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_spreadsheetmlsimplified_data_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLSimplified_Data)


def test_spreadsheetmlsimplified_data_constructor_exists():
    assert callable(SpreadsheetMLSimplified_Data.__init__)


def test_spreadsheetmlsimplified_data_constructor_args():
    sig = inspect.signature(SpreadsheetMLSimplified_Data.__init__)
    params = list(sig.parameters.keys())



def test_cell_is_not_abstract():
    assert not inspect.isabstract(Cell)


def test_cell_constructor_exists():
    assert callable(Cell.__init__)


def test_cell_constructor_args():
    sig = inspect.signature(Cell.__init__)
    params = list(sig.parameters.keys())



def test_colorrowelement_is_not_abstract():
    assert not inspect.isabstract(ColOrRowElement)


def test_colorrowelement_constructor_exists():
    assert callable(ColOrRowElement.__init__)


def test_colorrowelement_constructor_args():
    sig = inspect.signature(ColOrRowElement.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlsimplified_row_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLSimplified_Row)


def test_spreadsheetmlsimplified_row_constructor_exists():
    assert callable(SpreadsheetMLSimplified_Row.__init__)


def test_spreadsheetmlsimplified_row_constructor_args():
    sig = inspect.signature(SpreadsheetMLSimplified_Row.__init__)
    params = list(sig.parameters.keys())
    assert "autoFitHeight" in params, "Missing parameter 'autoFitHeight'"
    assert "height" in params, "Missing parameter 'height'"

def test_spreadsheetmlsimplified_row_has_autoFitHeight():
    assert hasattr(SpreadsheetMLSimplified_Row, "autoFitHeight")
    descriptor = None
    for klass in SpreadsheetMLSimplified_Row.__mro__:
        if "autoFitHeight" in klass.__dict__:
            descriptor = klass.__dict__["autoFitHeight"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlsimplified_row_has_height():
    assert hasattr(SpreadsheetMLSimplified_Row, "height")
    descriptor = None
    for klass in SpreadsheetMLSimplified_Row.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlsimplified_column_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLSimplified_Column)


def test_spreadsheetmlsimplified_column_constructor_exists():
    assert callable(SpreadsheetMLSimplified_Column.__init__)


def test_spreadsheetmlsimplified_column_constructor_args():
    sig = inspect.signature(SpreadsheetMLSimplified_Column.__init__)
    params = list(sig.parameters.keys())
    assert "autoFitWidth" in params, "Missing parameter 'autoFitWidth'"
    assert "width" in params, "Missing parameter 'width'"

def test_spreadsheetmlsimplified_column_has_autoFitWidth():
    assert hasattr(SpreadsheetMLSimplified_Column, "autoFitWidth")
    descriptor = None
    for klass in SpreadsheetMLSimplified_Column.__mro__:
        if "autoFitWidth" in klass.__dict__:
            descriptor = klass.__dict__["autoFitWidth"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlsimplified_column_has_width():
    assert hasattr(SpreadsheetMLSimplified_Column, "width")
    descriptor = None
    for klass in SpreadsheetMLSimplified_Column.__mro__:
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



def test_spreadsheetmlsimplified_cell_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLSimplified_Cell)


def test_spreadsheetmlsimplified_cell_constructor_exists():
    assert callable(SpreadsheetMLSimplified_Cell.__init__)


def test_spreadsheetmlsimplified_cell_constructor_args():
    sig = inspect.signature(SpreadsheetMLSimplified_Cell.__init__)
    params = list(sig.parameters.keys())
    assert "hRef" in params, "Missing parameter 'hRef'"
    assert "formula" in params, "Missing parameter 'formula'"
    assert "arrayRange" in params, "Missing parameter 'arrayRange'"
    assert "mergeDown" in params, "Missing parameter 'mergeDown'"
    assert "mergeAcross" in params, "Missing parameter 'mergeAcross'"

def test_spreadsheetmlsimplified_cell_has_hRef():
    assert hasattr(SpreadsheetMLSimplified_Cell, "hRef")
    descriptor = None
    for klass in SpreadsheetMLSimplified_Cell.__mro__:
        if "hRef" in klass.__dict__:
            descriptor = klass.__dict__["hRef"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlsimplified_cell_has_formula():
    assert hasattr(SpreadsheetMLSimplified_Cell, "formula")
    descriptor = None
    for klass in SpreadsheetMLSimplified_Cell.__mro__:
        if "formula" in klass.__dict__:
            descriptor = klass.__dict__["formula"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlsimplified_cell_has_arrayRange():
    assert hasattr(SpreadsheetMLSimplified_Cell, "arrayRange")
    descriptor = None
    for klass in SpreadsheetMLSimplified_Cell.__mro__:
        if "arrayRange" in klass.__dict__:
            descriptor = klass.__dict__["arrayRange"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlsimplified_cell_has_mergeDown():
    assert hasattr(SpreadsheetMLSimplified_Cell, "mergeDown")
    descriptor = None
    for klass in SpreadsheetMLSimplified_Cell.__mro__:
        if "mergeDown" in klass.__dict__:
            descriptor = klass.__dict__["mergeDown"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlsimplified_cell_has_mergeAcross():
    assert hasattr(SpreadsheetMLSimplified_Cell, "mergeAcross")
    descriptor = None
    for klass in SpreadsheetMLSimplified_Cell.__mro__:
        if "mergeAcross" in klass.__dict__:
            descriptor = klass.__dict__["mergeAcross"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlsimplified_colorrowelement_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLSimplified_ColOrRowElement)


def test_spreadsheetmlsimplified_colorrowelement_constructor_exists():
    assert callable(SpreadsheetMLSimplified_ColOrRowElement.__init__)


def test_spreadsheetmlsimplified_colorrowelement_constructor_args():
    sig = inspect.signature(SpreadsheetMLSimplified_ColOrRowElement.__init__)
    params = list(sig.parameters.keys())
    assert "hidden" in params, "Missing parameter 'hidden'"
    assert "span" in params, "Missing parameter 'span'"

def test_spreadsheetmlsimplified_colorrowelement_has_hidden():
    assert hasattr(SpreadsheetMLSimplified_ColOrRowElement, "hidden")
    descriptor = None
    for klass in SpreadsheetMLSimplified_ColOrRowElement.__mro__:
        if "hidden" in klass.__dict__:
            descriptor = klass.__dict__["hidden"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlsimplified_colorrowelement_has_span():
    assert hasattr(SpreadsheetMLSimplified_ColOrRowElement, "span")
    descriptor = None
    for klass in SpreadsheetMLSimplified_ColOrRowElement.__mro__:
        if "span" in klass.__dict__:
            descriptor = klass.__dict__["span"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlsimplified_tableelement_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLSimplified_TableElement)


def test_spreadsheetmlsimplified_tableelement_constructor_exists():
    assert callable(SpreadsheetMLSimplified_TableElement.__init__)


def test_spreadsheetmlsimplified_tableelement_constructor_args():
    sig = inspect.signature(SpreadsheetMLSimplified_TableElement.__init__)
    params = list(sig.parameters.keys())
    assert "index" in params, "Missing parameter 'index'"

def test_spreadsheetmlsimplified_tableelement_has_index():
    assert hasattr(SpreadsheetMLSimplified_TableElement, "index")
    descriptor = None
    for klass in SpreadsheetMLSimplified_TableElement.__mro__:
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



def test_column_is_not_abstract():
    assert not inspect.isabstract(Column)


def test_column_constructor_exists():
    assert callable(Column.__init__)


def test_column_constructor_args():
    sig = inspect.signature(Column.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlsimplified_table_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLSimplified_Table)


def test_spreadsheetmlsimplified_table_constructor_exists():
    assert callable(SpreadsheetMLSimplified_Table.__init__)


def test_spreadsheetmlsimplified_table_constructor_args():
    sig = inspect.signature(SpreadsheetMLSimplified_Table.__init__)
    params = list(sig.parameters.keys())



def test_table_is_not_abstract():
    assert not inspect.isabstract(Table)


def test_table_constructor_exists():
    assert callable(Table.__init__)


def test_table_constructor_args():
    sig = inspect.signature(Table.__init__)
    params = list(sig.parameters.keys())



def test_workbook_is_not_abstract():
    assert not inspect.isabstract(Workbook)


def test_workbook_constructor_exists():
    assert callable(Workbook.__init__)


def test_workbook_constructor_args():
    sig = inspect.signature(Workbook.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlsimplified_worksheet_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLSimplified_Worksheet)


def test_spreadsheetmlsimplified_worksheet_constructor_exists():
    assert callable(SpreadsheetMLSimplified_Worksheet.__init__)


def test_spreadsheetmlsimplified_worksheet_constructor_args():
    sig = inspect.signature(SpreadsheetMLSimplified_Worksheet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_spreadsheetmlsimplified_worksheet_has_name():
    assert hasattr(SpreadsheetMLSimplified_Worksheet, "name")
    descriptor = None
    for klass in SpreadsheetMLSimplified_Worksheet.__mro__:
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



def test_spreadsheetmlsimplified_workbook_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLSimplified_Workbook)


def test_spreadsheetmlsimplified_workbook_constructor_exists():
    assert callable(SpreadsheetMLSimplified_Workbook.__init__)


def test_spreadsheetmlsimplified_workbook_constructor_args():
    sig = inspect.signature(SpreadsheetMLSimplified_Workbook.__init__)
    params = list(sig.parameters.keys())



def test_data_is_not_abstract():
    assert not inspect.isabstract(Data)


def test_data_constructor_exists():
    assert callable(Data.__init__)


def test_data_constructor_args():
    sig = inspect.signature(Data.__init__)
    params = list(sig.parameters.keys())



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



def test_spreadsheetmlsimplified_datetimetypevalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLSimplified_DateTimeTypeValue)


def test_spreadsheetmlsimplified_datetimetypevalue_constructor_exists():
    assert callable(SpreadsheetMLSimplified_DateTimeTypeValue.__init__)


def test_spreadsheetmlsimplified_datetimetypevalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLSimplified_DateTimeTypeValue.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlsimplified_errorvalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLSimplified_ErrorValue)


def test_spreadsheetmlsimplified_errorvalue_constructor_exists():
    assert callable(SpreadsheetMLSimplified_ErrorValue.__init__)


def test_spreadsheetmlsimplified_errorvalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLSimplified_ErrorValue.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlsimplified_numbervalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLSimplified_NumberValue)


def test_spreadsheetmlsimplified_numbervalue_constructor_exists():
    assert callable(SpreadsheetMLSimplified_NumberValue.__init__)


def test_spreadsheetmlsimplified_numbervalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLSimplified_NumberValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_spreadsheetmlsimplified_numbervalue_has_value():
    assert hasattr(SpreadsheetMLSimplified_NumberValue, "value")
    descriptor = None
    for klass in SpreadsheetMLSimplified_NumberValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlsimplified_booleanvalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLSimplified_BooleanValue)


def test_spreadsheetmlsimplified_booleanvalue_constructor_exists():
    assert callable(SpreadsheetMLSimplified_BooleanValue.__init__)


def test_spreadsheetmlsimplified_booleanvalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLSimplified_BooleanValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_spreadsheetmlsimplified_booleanvalue_has_value():
    assert hasattr(SpreadsheetMLSimplified_BooleanValue, "value")
    descriptor = None
    for klass in SpreadsheetMLSimplified_BooleanValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlsimplified_stringvalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLSimplified_StringValue)


def test_spreadsheetmlsimplified_stringvalue_constructor_exists():
    assert callable(SpreadsheetMLSimplified_StringValue.__init__)


def test_spreadsheetmlsimplified_stringvalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLSimplified_StringValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_spreadsheetmlsimplified_stringvalue_has_value():
    assert hasattr(SpreadsheetMLSimplified_StringValue, "value")
    descriptor = None
    for klass in SpreadsheetMLSimplified_StringValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlsimplified_valuetype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLSimplified_ValueType)


def test_spreadsheetmlsimplified_valuetype_constructor_exists():
    assert callable(SpreadsheetMLSimplified_ValueType.__init__)


def test_spreadsheetmlsimplified_valuetype_constructor_args():
    sig = inspect.signature(SpreadsheetMLSimplified_ValueType.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlsimplified_datetimetype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLSimplified_DateTimeType)


def test_spreadsheetmlsimplified_datetimetype_constructor_exists():
    assert callable(SpreadsheetMLSimplified_DateTimeType.__init__)


def test_spreadsheetmlsimplified_datetimetype_constructor_args():
    sig = inspect.signature(SpreadsheetMLSimplified_DateTimeType.__init__)
    params = list(sig.parameters.keys())
    assert "hour" in params, "Missing parameter 'hour'"
    assert "year" in params, "Missing parameter 'year'"
    assert "month" in params, "Missing parameter 'month'"
    assert "minute" in params, "Missing parameter 'minute'"
    assert "day" in params, "Missing parameter 'day'"
    assert "second" in params, "Missing parameter 'second'"

def test_spreadsheetmlsimplified_datetimetype_has_hour():
    assert hasattr(SpreadsheetMLSimplified_DateTimeType, "hour")
    descriptor = None
    for klass in SpreadsheetMLSimplified_DateTimeType.__mro__:
        if "hour" in klass.__dict__:
            descriptor = klass.__dict__["hour"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlsimplified_datetimetype_has_year():
    assert hasattr(SpreadsheetMLSimplified_DateTimeType, "year")
    descriptor = None
    for klass in SpreadsheetMLSimplified_DateTimeType.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlsimplified_datetimetype_has_month():
    assert hasattr(SpreadsheetMLSimplified_DateTimeType, "month")
    descriptor = None
    for klass in SpreadsheetMLSimplified_DateTimeType.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlsimplified_datetimetype_has_minute():
    assert hasattr(SpreadsheetMLSimplified_DateTimeType, "minute")
    descriptor = None
    for klass in SpreadsheetMLSimplified_DateTimeType.__mro__:
        if "minute" in klass.__dict__:
            descriptor = klass.__dict__["minute"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlsimplified_datetimetype_has_day():
    assert hasattr(SpreadsheetMLSimplified_DateTimeType, "day")
    descriptor = None
    for klass in SpreadsheetMLSimplified_DateTimeType.__mro__:
        if "day" in klass.__dict__:
            descriptor = klass.__dict__["day"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlsimplified_datetimetype_has_second():
    assert hasattr(SpreadsheetMLSimplified_DateTimeType, "second")
    descriptor = None
    for klass in SpreadsheetMLSimplified_DateTimeType.__mro__:
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
SpreadsheetMLSimplified_Data_strategy = st.builds(
    SpreadsheetMLSimplified_Data,
)
Cell_strategy = st.builds(
    Cell,
)
ColOrRowElement_strategy = st.builds(
    ColOrRowElement,
)
SpreadsheetMLSimplified_Row_strategy = st.builds(
    SpreadsheetMLSimplified_Row,
    autoFitHeight=
        safe_text,
    height=
        safe_text
)
SpreadsheetMLSimplified_Column_strategy = st.builds(
    SpreadsheetMLSimplified_Column,
    autoFitWidth=
        safe_text,
    width=
        safe_text
)
TableElement_strategy = st.builds(
    TableElement,
)
SpreadsheetMLSimplified_Cell_strategy = st.builds(
    SpreadsheetMLSimplified_Cell,
    hRef=
        safe_text,
    formula=
        safe_text,
    arrayRange=
        safe_text,
    mergeDown=
        safe_text,
    mergeAcross=
        safe_text
)
SpreadsheetMLSimplified_ColOrRowElement_strategy = st.builds(
    SpreadsheetMLSimplified_ColOrRowElement,
    hidden=
        safe_text,
    span=
        safe_text
)
SpreadsheetMLSimplified_TableElement_strategy = st.builds(
    SpreadsheetMLSimplified_TableElement,
    index=
        safe_text
)
Row_strategy = st.builds(
    Row,
)
Column_strategy = st.builds(
    Column,
)
SpreadsheetMLSimplified_Table_strategy = st.builds(
    SpreadsheetMLSimplified_Table,
)
Table_strategy = st.builds(
    Table,
)
Workbook_strategy = st.builds(
    Workbook,
)
SpreadsheetMLSimplified_Worksheet_strategy = st.builds(
    SpreadsheetMLSimplified_Worksheet,
    name=
        safe_text
)
Worksheet_strategy = st.builds(
    Worksheet,
)
SpreadsheetMLSimplified_Workbook_strategy = st.builds(
    SpreadsheetMLSimplified_Workbook,
)
Data_strategy = st.builds(
    Data,
)
DateTimeType_strategy = st.builds(
    DateTimeType,
)
ValueType_strategy = st.builds(
    ValueType,
)
SpreadsheetMLSimplified_DateTimeTypeValue_strategy = st.builds(
    SpreadsheetMLSimplified_DateTimeTypeValue,
)
SpreadsheetMLSimplified_ErrorValue_strategy = st.builds(
    SpreadsheetMLSimplified_ErrorValue,
)
SpreadsheetMLSimplified_NumberValue_strategy = st.builds(
    SpreadsheetMLSimplified_NumberValue,
    value=
        safe_text
)
SpreadsheetMLSimplified_BooleanValue_strategy = st.builds(
    SpreadsheetMLSimplified_BooleanValue,
    value=
        safe_text
)
SpreadsheetMLSimplified_StringValue_strategy = st.builds(
    SpreadsheetMLSimplified_StringValue,
    value=
        safe_text
)
SpreadsheetMLSimplified_ValueType_strategy = st.builds(
    SpreadsheetMLSimplified_ValueType,
)
SpreadsheetMLSimplified_DateTimeType_strategy = st.builds(
    SpreadsheetMLSimplified_DateTimeType,
    hour=
        safe_text,
    year=
        safe_text,
    month=
        safe_text,
    minute=
        safe_text,
    day=
        safe_text,
    second=
        safe_text
)

@given(instance=SpreadsheetMLSimplified_Data_strategy)
@settings(max_examples=50)
def test_spreadsheetmlsimplified_data_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLSimplified_Data)

@given(instance=Cell_strategy)
@settings(max_examples=50)
def test_cell_instantiation(instance):
    assert isinstance(instance, Cell)

@given(instance=ColOrRowElement_strategy)
@settings(max_examples=50)
def test_colorrowelement_instantiation(instance):
    assert isinstance(instance, ColOrRowElement)

@given(instance=SpreadsheetMLSimplified_Row_strategy)
@settings(max_examples=50)
def test_spreadsheetmlsimplified_row_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLSimplified_Row)



@given(instance=SpreadsheetMLSimplified_Row_strategy)
def test_spreadsheetmlsimplified_row_autoFitHeight_setter(instance):
    original = instance.autoFitHeight
    instance.autoFitHeight = original
    assert instance.autoFitHeight == original



@given(instance=SpreadsheetMLSimplified_Row_strategy)
def test_spreadsheetmlsimplified_row_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=SpreadsheetMLSimplified_Column_strategy)
@settings(max_examples=50)
def test_spreadsheetmlsimplified_column_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLSimplified_Column)



@given(instance=SpreadsheetMLSimplified_Column_strategy)
def test_spreadsheetmlsimplified_column_autoFitWidth_setter(instance):
    original = instance.autoFitWidth
    instance.autoFitWidth = original
    assert instance.autoFitWidth == original



@given(instance=SpreadsheetMLSimplified_Column_strategy)
def test_spreadsheetmlsimplified_column_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=TableElement_strategy)
@settings(max_examples=50)
def test_tableelement_instantiation(instance):
    assert isinstance(instance, TableElement)

@given(instance=SpreadsheetMLSimplified_Cell_strategy)
@settings(max_examples=50)
def test_spreadsheetmlsimplified_cell_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLSimplified_Cell)



@given(instance=SpreadsheetMLSimplified_Cell_strategy)
def test_spreadsheetmlsimplified_cell_hRef_setter(instance):
    original = instance.hRef
    instance.hRef = original
    assert instance.hRef == original



@given(instance=SpreadsheetMLSimplified_Cell_strategy)
def test_spreadsheetmlsimplified_cell_formula_setter(instance):
    original = instance.formula
    instance.formula = original
    assert instance.formula == original



@given(instance=SpreadsheetMLSimplified_Cell_strategy)
def test_spreadsheetmlsimplified_cell_arrayRange_setter(instance):
    original = instance.arrayRange
    instance.arrayRange = original
    assert instance.arrayRange == original



@given(instance=SpreadsheetMLSimplified_Cell_strategy)
def test_spreadsheetmlsimplified_cell_mergeDown_setter(instance):
    original = instance.mergeDown
    instance.mergeDown = original
    assert instance.mergeDown == original



@given(instance=SpreadsheetMLSimplified_Cell_strategy)
def test_spreadsheetmlsimplified_cell_mergeAcross_setter(instance):
    original = instance.mergeAcross
    instance.mergeAcross = original
    assert instance.mergeAcross == original

@given(instance=SpreadsheetMLSimplified_ColOrRowElement_strategy)
@settings(max_examples=50)
def test_spreadsheetmlsimplified_colorrowelement_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLSimplified_ColOrRowElement)



@given(instance=SpreadsheetMLSimplified_ColOrRowElement_strategy)
def test_spreadsheetmlsimplified_colorrowelement_hidden_setter(instance):
    original = instance.hidden
    instance.hidden = original
    assert instance.hidden == original



@given(instance=SpreadsheetMLSimplified_ColOrRowElement_strategy)
def test_spreadsheetmlsimplified_colorrowelement_span_setter(instance):
    original = instance.span
    instance.span = original
    assert instance.span == original

@given(instance=SpreadsheetMLSimplified_TableElement_strategy)
@settings(max_examples=50)
def test_spreadsheetmlsimplified_tableelement_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLSimplified_TableElement)



@given(instance=SpreadsheetMLSimplified_TableElement_strategy)
def test_spreadsheetmlsimplified_tableelement_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original

@given(instance=Row_strategy)
@settings(max_examples=50)
def test_row_instantiation(instance):
    assert isinstance(instance, Row)

@given(instance=Column_strategy)
@settings(max_examples=50)
def test_column_instantiation(instance):
    assert isinstance(instance, Column)

@given(instance=SpreadsheetMLSimplified_Table_strategy)
@settings(max_examples=50)
def test_spreadsheetmlsimplified_table_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLSimplified_Table)

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)

@given(instance=Workbook_strategy)
@settings(max_examples=50)
def test_workbook_instantiation(instance):
    assert isinstance(instance, Workbook)

@given(instance=SpreadsheetMLSimplified_Worksheet_strategy)
@settings(max_examples=50)
def test_spreadsheetmlsimplified_worksheet_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLSimplified_Worksheet)



@given(instance=SpreadsheetMLSimplified_Worksheet_strategy)
def test_spreadsheetmlsimplified_worksheet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Worksheet_strategy)
@settings(max_examples=50)
def test_worksheet_instantiation(instance):
    assert isinstance(instance, Worksheet)

@given(instance=SpreadsheetMLSimplified_Workbook_strategy)
@settings(max_examples=50)
def test_spreadsheetmlsimplified_workbook_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLSimplified_Workbook)

@given(instance=Data_strategy)
@settings(max_examples=50)
def test_data_instantiation(instance):
    assert isinstance(instance, Data)

@given(instance=DateTimeType_strategy)
@settings(max_examples=50)
def test_datetimetype_instantiation(instance):
    assert isinstance(instance, DateTimeType)

@given(instance=ValueType_strategy)
@settings(max_examples=50)
def test_valuetype_instantiation(instance):
    assert isinstance(instance, ValueType)

@given(instance=SpreadsheetMLSimplified_DateTimeTypeValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlsimplified_datetimetypevalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLSimplified_DateTimeTypeValue)

@given(instance=SpreadsheetMLSimplified_ErrorValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlsimplified_errorvalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLSimplified_ErrorValue)

@given(instance=SpreadsheetMLSimplified_NumberValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlsimplified_numbervalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLSimplified_NumberValue)



@given(instance=SpreadsheetMLSimplified_NumberValue_strategy)
def test_spreadsheetmlsimplified_numbervalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SpreadsheetMLSimplified_BooleanValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlsimplified_booleanvalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLSimplified_BooleanValue)



@given(instance=SpreadsheetMLSimplified_BooleanValue_strategy)
def test_spreadsheetmlsimplified_booleanvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SpreadsheetMLSimplified_StringValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlsimplified_stringvalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLSimplified_StringValue)



@given(instance=SpreadsheetMLSimplified_StringValue_strategy)
def test_spreadsheetmlsimplified_stringvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SpreadsheetMLSimplified_ValueType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlsimplified_valuetype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLSimplified_ValueType)

@given(instance=SpreadsheetMLSimplified_DateTimeType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlsimplified_datetimetype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLSimplified_DateTimeType)



@given(instance=SpreadsheetMLSimplified_DateTimeType_strategy)
def test_spreadsheetmlsimplified_datetimetype_hour_setter(instance):
    original = instance.hour
    instance.hour = original
    assert instance.hour == original



@given(instance=SpreadsheetMLSimplified_DateTimeType_strategy)
def test_spreadsheetmlsimplified_datetimetype_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original



@given(instance=SpreadsheetMLSimplified_DateTimeType_strategy)
def test_spreadsheetmlsimplified_datetimetype_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original



@given(instance=SpreadsheetMLSimplified_DateTimeType_strategy)
def test_spreadsheetmlsimplified_datetimetype_minute_setter(instance):
    original = instance.minute
    instance.minute = original
    assert instance.minute == original



@given(instance=SpreadsheetMLSimplified_DateTimeType_strategy)
def test_spreadsheetmlsimplified_datetimetype_day_setter(instance):
    original = instance.day
    instance.day = original
    assert instance.day == original



@given(instance=SpreadsheetMLSimplified_DateTimeType_strategy)
def test_spreadsheetmlsimplified_datetimetype_second_setter(instance):
    original = instance.second
    instance.second = original
    assert instance.second == original
