import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ValueType,
    StringValue,
    NumberValue,
    BooleanValue,
    Data,
    ErrorValue,
    TableElement,
    Cell,
    ColOrRowElement,
    Row,
    Column,
    Table,
    Worksheet,
    Workbook,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_valuetype_is_not_abstract():
    assert not inspect.isabstract(ValueType)


def test_valuetype_constructor_exists():
    assert callable(ValueType.__init__)


def test_valuetype_constructor_args():
    sig = inspect.signature(ValueType.__init__)
    params = list(sig.parameters.keys())



def test_stringvalue_is_not_abstract():
    assert not inspect.isabstract(StringValue)


def test_stringvalue_constructor_exists():
    assert callable(StringValue.__init__)


def test_stringvalue_constructor_args():
    sig = inspect.signature(StringValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_stringvalue_has_value():
    assert hasattr(StringValue, "value")
    descriptor = None
    for klass in StringValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_numbervalue_is_not_abstract():
    assert not inspect.isabstract(NumberValue)


def test_numbervalue_constructor_exists():
    assert callable(NumberValue.__init__)


def test_numbervalue_constructor_args():
    sig = inspect.signature(NumberValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_numbervalue_has_value():
    assert hasattr(NumberValue, "value")
    descriptor = None
    for klass in NumberValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_booleanvalue_is_not_abstract():
    assert not inspect.isabstract(BooleanValue)


def test_booleanvalue_constructor_exists():
    assert callable(BooleanValue.__init__)


def test_booleanvalue_constructor_args():
    sig = inspect.signature(BooleanValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_booleanvalue_has_value():
    assert hasattr(BooleanValue, "value")
    descriptor = None
    for klass in BooleanValue.__mro__:
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



def test_errorvalue_is_not_abstract():
    assert not inspect.isabstract(ErrorValue)


def test_errorvalue_constructor_exists():
    assert callable(ErrorValue.__init__)


def test_errorvalue_constructor_args():
    sig = inspect.signature(ErrorValue.__init__)
    params = list(sig.parameters.keys())



def test_tableelement_is_not_abstract():
    assert not inspect.isabstract(TableElement)


def test_tableelement_constructor_exists():
    assert callable(TableElement.__init__)


def test_tableelement_constructor_args():
    sig = inspect.signature(TableElement.__init__)
    params = list(sig.parameters.keys())
    assert "index" in params, "Missing parameter 'index'"

def test_tableelement_has_index():
    assert hasattr(TableElement, "index")
    descriptor = None
    for klass in TableElement.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)



def test_cell_is_not_abstract():
    assert not inspect.isabstract(Cell)


def test_cell_constructor_exists():
    assert callable(Cell.__init__)


def test_cell_constructor_args():
    sig = inspect.signature(Cell.__init__)
    params = list(sig.parameters.keys())
    assert "index" in params, "Missing parameter 'index'"
    assert "formula" in params, "Missing parameter 'formula'"

def test_cell_has_index():
    assert hasattr(Cell, "index")
    descriptor = None
    for klass in Cell.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)

def test_cell_has_formula():
    assert hasattr(Cell, "formula")
    descriptor = None
    for klass in Cell.__mro__:
        if "formula" in klass.__dict__:
            descriptor = klass.__dict__["formula"]
            break
    assert isinstance(descriptor, property)



def test_colorrowelement_is_not_abstract():
    assert not inspect.isabstract(ColOrRowElement)


def test_colorrowelement_constructor_exists():
    assert callable(ColOrRowElement.__init__)


def test_colorrowelement_constructor_args():
    sig = inspect.signature(ColOrRowElement.__init__)
    params = list(sig.parameters.keys())
    assert "span" in params, "Missing parameter 'span'"
    assert "index" in params, "Missing parameter 'index'"
    assert "hidden" in params, "Missing parameter 'hidden'"

def test_colorrowelement_has_span():
    assert hasattr(ColOrRowElement, "span")
    descriptor = None
    for klass in ColOrRowElement.__mro__:
        if "span" in klass.__dict__:
            descriptor = klass.__dict__["span"]
            break
    assert isinstance(descriptor, property)

def test_colorrowelement_has_index():
    assert hasattr(ColOrRowElement, "index")
    descriptor = None
    for klass in ColOrRowElement.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)

def test_colorrowelement_has_hidden():
    assert hasattr(ColOrRowElement, "hidden")
    descriptor = None
    for klass in ColOrRowElement.__mro__:
        if "hidden" in klass.__dict__:
            descriptor = klass.__dict__["hidden"]
            break
    assert isinstance(descriptor, property)



def test_row_is_not_abstract():
    assert not inspect.isabstract(Row)


def test_row_constructor_exists():
    assert callable(Row.__init__)


def test_row_constructor_args():
    sig = inspect.signature(Row.__init__)
    params = list(sig.parameters.keys())
    assert "span" in params, "Missing parameter 'span'"
    assert "index" in params, "Missing parameter 'index'"
    assert "hidden" in params, "Missing parameter 'hidden'"

def test_row_has_span():
    assert hasattr(Row, "span")
    descriptor = None
    for klass in Row.__mro__:
        if "span" in klass.__dict__:
            descriptor = klass.__dict__["span"]
            break
    assert isinstance(descriptor, property)

def test_row_has_index():
    assert hasattr(Row, "index")
    descriptor = None
    for klass in Row.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)

def test_row_has_hidden():
    assert hasattr(Row, "hidden")
    descriptor = None
    for klass in Row.__mro__:
        if "hidden" in klass.__dict__:
            descriptor = klass.__dict__["hidden"]
            break
    assert isinstance(descriptor, property)



def test_column_is_not_abstract():
    assert not inspect.isabstract(Column)


def test_column_constructor_exists():
    assert callable(Column.__init__)


def test_column_constructor_args():
    sig = inspect.signature(Column.__init__)
    params = list(sig.parameters.keys())
    assert "span" in params, "Missing parameter 'span'"
    assert "index" in params, "Missing parameter 'index'"
    assert "hidden" in params, "Missing parameter 'hidden'"

def test_column_has_span():
    assert hasattr(Column, "span")
    descriptor = None
    for klass in Column.__mro__:
        if "span" in klass.__dict__:
            descriptor = klass.__dict__["span"]
            break
    assert isinstance(descriptor, property)

def test_column_has_index():
    assert hasattr(Column, "index")
    descriptor = None
    for klass in Column.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)

def test_column_has_hidden():
    assert hasattr(Column, "hidden")
    descriptor = None
    for klass in Column.__mro__:
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



def test_worksheet_is_not_abstract():
    assert not inspect.isabstract(Worksheet)


def test_worksheet_constructor_exists():
    assert callable(Worksheet.__init__)


def test_worksheet_constructor_args():
    sig = inspect.signature(Worksheet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_worksheet_has_name():
    assert hasattr(Worksheet, "name")
    descriptor = None
    for klass in Worksheet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_workbook_is_not_abstract():
    assert not inspect.isabstract(Workbook)


def test_workbook_constructor_exists():
    assert callable(Workbook.__init__)


def test_workbook_constructor_args():
    sig = inspect.signature(Workbook.__init__)
    params = list(sig.parameters.keys())


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
ValueType_strategy = st.builds(
    ValueType,
)
StringValue_strategy = st.builds(
    StringValue,
    value=
        safe_text
)
NumberValue_strategy = st.builds(
    NumberValue,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
BooleanValue_strategy = st.builds(
    BooleanValue,
    value=
        st.booleans()
)
Data_strategy = st.builds(
    Data,
)
ErrorValue_strategy = st.builds(
    ErrorValue,
)
TableElement_strategy = st.builds(
    TableElement,
    index=
        st.integers()
)
Cell_strategy = st.builds(
    Cell,
    index=
        st.integers(),
    formula=
        safe_text
)
ColOrRowElement_strategy = st.builds(
    ColOrRowElement,
    span=
        st.integers(),
    index=
        st.integers(),
    hidden=
        st.booleans()
)
Row_strategy = st.builds(
    Row,
    span=
        st.integers(),
    index=
        st.integers(),
    hidden=
        st.booleans()
)
Column_strategy = st.builds(
    Column,
    span=
        st.integers(),
    index=
        st.integers(),
    hidden=
        st.booleans()
)
Table_strategy = st.builds(
    Table,
)
Worksheet_strategy = st.builds(
    Worksheet,
    name=
        safe_text
)
Workbook_strategy = st.builds(
    Workbook,
)

@given(instance=ValueType_strategy)
@settings(max_examples=50)
def test_valuetype_instantiation(instance):
    assert isinstance(instance, ValueType)

@given(instance=StringValue_strategy)
@settings(max_examples=50)
def test_stringvalue_instantiation(instance):
    assert isinstance(instance, StringValue)



@given(instance=StringValue_strategy)
def test_stringvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=NumberValue_strategy)
@settings(max_examples=50)
def test_numbervalue_instantiation(instance):
    assert isinstance(instance, NumberValue)



@given(instance=NumberValue_strategy)
def test_numbervalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=BooleanValue_strategy)
@settings(max_examples=50)
def test_booleanvalue_instantiation(instance):
    assert isinstance(instance, BooleanValue)



@given(instance=BooleanValue_strategy)
def test_booleanvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Data_strategy)
@settings(max_examples=50)
def test_data_instantiation(instance):
    assert isinstance(instance, Data)

@given(instance=ErrorValue_strategy)
@settings(max_examples=50)
def test_errorvalue_instantiation(instance):
    assert isinstance(instance, ErrorValue)

@given(instance=TableElement_strategy)
@settings(max_examples=50)
def test_tableelement_instantiation(instance):
    assert isinstance(instance, TableElement)



@given(instance=TableElement_strategy)
def test_tableelement_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original

@given(instance=Cell_strategy)
@settings(max_examples=50)
def test_cell_instantiation(instance):
    assert isinstance(instance, Cell)



@given(instance=Cell_strategy)
def test_cell_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original



@given(instance=Cell_strategy)
def test_cell_formula_setter(instance):
    original = instance.formula
    instance.formula = original
    assert instance.formula == original

@given(instance=ColOrRowElement_strategy)
@settings(max_examples=50)
def test_colorrowelement_instantiation(instance):
    assert isinstance(instance, ColOrRowElement)



@given(instance=ColOrRowElement_strategy)
def test_colorrowelement_span_setter(instance):
    original = instance.span
    instance.span = original
    assert instance.span == original



@given(instance=ColOrRowElement_strategy)
def test_colorrowelement_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original



@given(instance=ColOrRowElement_strategy)
def test_colorrowelement_hidden_setter(instance):
    original = instance.hidden
    instance.hidden = original
    assert instance.hidden == original

@given(instance=Row_strategy)
@settings(max_examples=50)
def test_row_instantiation(instance):
    assert isinstance(instance, Row)



@given(instance=Row_strategy)
def test_row_span_setter(instance):
    original = instance.span
    instance.span = original
    assert instance.span == original



@given(instance=Row_strategy)
def test_row_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original



@given(instance=Row_strategy)
def test_row_hidden_setter(instance):
    original = instance.hidden
    instance.hidden = original
    assert instance.hidden == original

@given(instance=Column_strategy)
@settings(max_examples=50)
def test_column_instantiation(instance):
    assert isinstance(instance, Column)



@given(instance=Column_strategy)
def test_column_span_setter(instance):
    original = instance.span
    instance.span = original
    assert instance.span == original



@given(instance=Column_strategy)
def test_column_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original



@given(instance=Column_strategy)
def test_column_hidden_setter(instance):
    original = instance.hidden
    instance.hidden = original
    assert instance.hidden == original

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)

@given(instance=Worksheet_strategy)
@settings(max_examples=50)
def test_worksheet_instantiation(instance):
    assert isinstance(instance, Worksheet)



@given(instance=Worksheet_strategy)
def test_worksheet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Workbook_strategy)
@settings(max_examples=50)
def test_workbook_instantiation(instance):
    assert isinstance(instance, Workbook)
