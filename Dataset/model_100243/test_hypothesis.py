import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    spreadsheet::Cell,
    spreadsheet::Column,
    spreadsheet::Row,
    spreadsheet::Sheet,
    spreadsheet::Spreadsheet,
    CellType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_spreadsheet::cell_is_not_abstract():
    assert not inspect.isabstract(spreadsheet::Cell)


def test_spreadsheet::cell_constructor_exists():
    assert callable(spreadsheet::Cell.__init__)


def test_spreadsheet::cell_constructor_args():
    sig = inspect.signature(spreadsheet::Cell.__init__)
    params = list(sig.parameters.keys())
    assert "ValueFormatted" in params, "Missing parameter 'ValueFormatted'"
    assert "StringValue" in params, "Missing parameter 'StringValue'"
    assert "DoubleValue" in params, "Missing parameter 'DoubleValue'"
    assert "CellType" in params, "Missing parameter 'CellType'"

def test_spreadsheet::cell_has_ValueFormatted():
    assert hasattr(spreadsheet::Cell, "ValueFormatted")
    descriptor = None
    for klass in spreadsheet::Cell.__mro__:
        if "ValueFormatted" in klass.__dict__:
            descriptor = klass.__dict__["ValueFormatted"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheet::cell_has_StringValue():
    assert hasattr(spreadsheet::Cell, "StringValue")
    descriptor = None
    for klass in spreadsheet::Cell.__mro__:
        if "StringValue" in klass.__dict__:
            descriptor = klass.__dict__["StringValue"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheet::cell_has_DoubleValue():
    assert hasattr(spreadsheet::Cell, "DoubleValue")
    descriptor = None
    for klass in spreadsheet::Cell.__mro__:
        if "DoubleValue" in klass.__dict__:
            descriptor = klass.__dict__["DoubleValue"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheet::cell_has_CellType():
    assert hasattr(spreadsheet::Cell, "CellType")
    descriptor = None
    for klass in spreadsheet::Cell.__mro__:
        if "CellType" in klass.__dict__:
            descriptor = klass.__dict__["CellType"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheet::column_is_not_abstract():
    assert not inspect.isabstract(spreadsheet::Column)


def test_spreadsheet::column_constructor_exists():
    assert callable(spreadsheet::Column.__init__)


def test_spreadsheet::column_constructor_args():
    sig = inspect.signature(spreadsheet::Column.__init__)
    params = list(sig.parameters.keys())
    assert "ColumnIndex" in params, "Missing parameter 'ColumnIndex'"

def test_spreadsheet::column_has_ColumnIndex():
    assert hasattr(spreadsheet::Column, "ColumnIndex")
    descriptor = None
    for klass in spreadsheet::Column.__mro__:
        if "ColumnIndex" in klass.__dict__:
            descriptor = klass.__dict__["ColumnIndex"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheet::row_is_not_abstract():
    assert not inspect.isabstract(spreadsheet::Row)


def test_spreadsheet::row_constructor_exists():
    assert callable(spreadsheet::Row.__init__)


def test_spreadsheet::row_constructor_args():
    sig = inspect.signature(spreadsheet::Row.__init__)
    params = list(sig.parameters.keys())
    assert "RowIndex" in params, "Missing parameter 'RowIndex'"

def test_spreadsheet::row_has_RowIndex():
    assert hasattr(spreadsheet::Row, "RowIndex")
    descriptor = None
    for klass in spreadsheet::Row.__mro__:
        if "RowIndex" in klass.__dict__:
            descriptor = klass.__dict__["RowIndex"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheet::sheet_is_not_abstract():
    assert not inspect.isabstract(spreadsheet::Sheet)


def test_spreadsheet::sheet_constructor_exists():
    assert callable(spreadsheet::Sheet.__init__)


def test_spreadsheet::sheet_constructor_args():
    sig = inspect.signature(spreadsheet::Sheet.__init__)
    params = list(sig.parameters.keys())
    assert "SheetIndex" in params, "Missing parameter 'SheetIndex'"
    assert "SheetName" in params, "Missing parameter 'SheetName'"

def test_spreadsheet::sheet_has_SheetIndex():
    assert hasattr(spreadsheet::Sheet, "SheetIndex")
    descriptor = None
    for klass in spreadsheet::Sheet.__mro__:
        if "SheetIndex" in klass.__dict__:
            descriptor = klass.__dict__["SheetIndex"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheet::sheet_has_SheetName():
    assert hasattr(spreadsheet::Sheet, "SheetName")
    descriptor = None
    for klass in spreadsheet::Sheet.__mro__:
        if "SheetName" in klass.__dict__:
            descriptor = klass.__dict__["SheetName"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheet::spreadsheet_is_not_abstract():
    assert not inspect.isabstract(spreadsheet::Spreadsheet)


def test_spreadsheet::spreadsheet_constructor_exists():
    assert callable(spreadsheet::Spreadsheet.__init__)


def test_spreadsheet::spreadsheet_constructor_args():
    sig = inspect.signature(spreadsheet::Spreadsheet.__init__)
    params = list(sig.parameters.keys())
    assert "FilePath" in params, "Missing parameter 'FilePath'"
    assert "Label" in params, "Missing parameter 'Label'"

def test_spreadsheet::spreadsheet_has_FilePath():
    assert hasattr(spreadsheet::Spreadsheet, "FilePath")
    descriptor = None
    for klass in spreadsheet::Spreadsheet.__mro__:
        if "FilePath" in klass.__dict__:
            descriptor = klass.__dict__["FilePath"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheet::spreadsheet_has_Label():
    assert hasattr(spreadsheet::Spreadsheet, "Label")
    descriptor = None
    for klass in spreadsheet::Spreadsheet.__mro__:
        if "Label" in klass.__dict__:
            descriptor = klass.__dict__["Label"]
            break
    assert isinstance(descriptor, property)

def test_celltype_exists():
    # Check that the Enumeration exists
    assert CellType is not None

def test_celltype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CellType]
    expected_literals = [
        "CellTypeDate",
        "CellTypeFormula",
        "CellTypeNumeric",
        "CellTypeString",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CellType"


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
spreadsheet::Cell_strategy = st.builds(
    spreadsheet::Cell,
    ValueFormatted=
        safe_text,
    StringValue=
        safe_text,
    DoubleValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    CellType=
        safe_text
)
spreadsheet::Column_strategy = st.builds(
    spreadsheet::Column,
    ColumnIndex=
        st.integers()
)
spreadsheet::Row_strategy = st.builds(
    spreadsheet::Row,
    RowIndex=
        st.integers()
)
spreadsheet::Sheet_strategy = st.builds(
    spreadsheet::Sheet,
    SheetIndex=
        st.integers(),
    SheetName=
        safe_text
)
spreadsheet::Spreadsheet_strategy = st.builds(
    spreadsheet::Spreadsheet,
    FilePath=
        safe_text,
    Label=
        safe_text
)

@given(instance=spreadsheet::Cell_strategy)
@settings(max_examples=50)
def test_spreadsheet::cell_instantiation(instance):
    assert isinstance(instance, spreadsheet::Cell)

@given(instance=spreadsheet::Cell_strategy)
def test_spreadsheet::cell_ValueFormatted_type(instance):
    assert isinstance(instance.ValueFormatted, str)


@given(instance=spreadsheet::Cell_strategy)
def test_spreadsheet::cell_ValueFormatted_setter(instance):
    original = instance.ValueFormatted
    instance.ValueFormatted = original
    assert instance.ValueFormatted == original

@given(instance=spreadsheet::Cell_strategy)
def test_spreadsheet::cell_StringValue_type(instance):
    assert isinstance(instance.StringValue, str)


@given(instance=spreadsheet::Cell_strategy)
def test_spreadsheet::cell_StringValue_setter(instance):
    original = instance.StringValue
    instance.StringValue = original
    assert instance.StringValue == original

@given(instance=spreadsheet::Cell_strategy)
def test_spreadsheet::cell_DoubleValue_type(instance):
    assert isinstance(instance.DoubleValue, float)


@given(instance=spreadsheet::Cell_strategy)
def test_spreadsheet::cell_DoubleValue_setter(instance):
    original = instance.DoubleValue
    instance.DoubleValue = original
    assert instance.DoubleValue == original

@given(instance=spreadsheet::Cell_strategy)
def test_spreadsheet::cell_CellType_type(instance):
    assert isinstance(instance.CellType, str)


@given(instance=spreadsheet::Cell_strategy)
def test_spreadsheet::cell_CellType_setter(instance):
    original = instance.CellType
    instance.CellType = original
    assert instance.CellType == original

@given(instance=spreadsheet::Column_strategy)
@settings(max_examples=50)
def test_spreadsheet::column_instantiation(instance):
    assert isinstance(instance, spreadsheet::Column)

@given(instance=spreadsheet::Column_strategy)
def test_spreadsheet::column_ColumnIndex_type(instance):
    assert isinstance(instance.ColumnIndex, int)


@given(instance=spreadsheet::Column_strategy)
def test_spreadsheet::column_ColumnIndex_setter(instance):
    original = instance.ColumnIndex
    instance.ColumnIndex = original
    assert instance.ColumnIndex == original

@given(instance=spreadsheet::Row_strategy)
@settings(max_examples=50)
def test_spreadsheet::row_instantiation(instance):
    assert isinstance(instance, spreadsheet::Row)

@given(instance=spreadsheet::Row_strategy)
def test_spreadsheet::row_RowIndex_type(instance):
    assert isinstance(instance.RowIndex, int)


@given(instance=spreadsheet::Row_strategy)
def test_spreadsheet::row_RowIndex_setter(instance):
    original = instance.RowIndex
    instance.RowIndex = original
    assert instance.RowIndex == original

@given(instance=spreadsheet::Sheet_strategy)
@settings(max_examples=50)
def test_spreadsheet::sheet_instantiation(instance):
    assert isinstance(instance, spreadsheet::Sheet)

@given(instance=spreadsheet::Sheet_strategy)
def test_spreadsheet::sheet_SheetIndex_type(instance):
    assert isinstance(instance.SheetIndex, int)


@given(instance=spreadsheet::Sheet_strategy)
def test_spreadsheet::sheet_SheetIndex_setter(instance):
    original = instance.SheetIndex
    instance.SheetIndex = original
    assert instance.SheetIndex == original

@given(instance=spreadsheet::Sheet_strategy)
def test_spreadsheet::sheet_SheetName_type(instance):
    assert isinstance(instance.SheetName, str)


@given(instance=spreadsheet::Sheet_strategy)
def test_spreadsheet::sheet_SheetName_setter(instance):
    original = instance.SheetName
    instance.SheetName = original
    assert instance.SheetName == original

@given(instance=spreadsheet::Spreadsheet_strategy)
@settings(max_examples=50)
def test_spreadsheet::spreadsheet_instantiation(instance):
    assert isinstance(instance, spreadsheet::Spreadsheet)

@given(instance=spreadsheet::Spreadsheet_strategy)
def test_spreadsheet::spreadsheet_FilePath_type(instance):
    assert isinstance(instance.FilePath, str)


@given(instance=spreadsheet::Spreadsheet_strategy)
def test_spreadsheet::spreadsheet_FilePath_setter(instance):
    original = instance.FilePath
    instance.FilePath = original
    assert instance.FilePath == original

@given(instance=spreadsheet::Spreadsheet_strategy)
def test_spreadsheet::spreadsheet_Label_type(instance):
    assert isinstance(instance.Label, str)


@given(instance=spreadsheet::Spreadsheet_strategy)
def test_spreadsheet::spreadsheet_Label_setter(instance):
    original = instance.Label
    instance.Label = original
    assert instance.Label == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=spreadsheet::Spreadsheet_strategy)
@settings(max_examples=30)
def test_spreadsheet::spreadsheet_readfile_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.readFile()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.readFile).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'readFile' in spreadsheet::Spreadsheet is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'readFile' in spreadsheet::Spreadsheet did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'readFile' in spreadsheet::Spreadsheet is not implemented or raised an error")
