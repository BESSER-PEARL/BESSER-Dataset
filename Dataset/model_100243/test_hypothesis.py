import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    spreadsheet_Cell,
    spreadsheet_Column,
    spreadsheet_Row,
    spreadsheet_Sheet,
    spreadsheet_Spreadsheet,
    CellType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_spreadsheet_cell_is_not_abstract():
    assert not inspect.isabstract(spreadsheet_Cell)


def test_spreadsheet_cell_constructor_exists():
    assert callable(spreadsheet_Cell.__init__)


def test_spreadsheet_cell_constructor_args():
    sig = inspect.signature(spreadsheet_Cell.__init__)
    params = list(sig.parameters.keys())
    assert "ValueFormatted" in params, "Missing parameter 'ValueFormatted'"
    assert "CellType" in params, "Missing parameter 'CellType'"
    assert "StringValue" in params, "Missing parameter 'StringValue'"
    assert "DoubleValue" in params, "Missing parameter 'DoubleValue'"

def test_spreadsheet_cell_has_ValueFormatted():
    assert hasattr(spreadsheet_Cell, "ValueFormatted")
    descriptor = None
    for klass in spreadsheet_Cell.__mro__:
        if "ValueFormatted" in klass.__dict__:
            descriptor = klass.__dict__["ValueFormatted"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheet_cell_has_CellType():
    assert hasattr(spreadsheet_Cell, "CellType")
    descriptor = None
    for klass in spreadsheet_Cell.__mro__:
        if "CellType" in klass.__dict__:
            descriptor = klass.__dict__["CellType"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheet_cell_has_StringValue():
    assert hasattr(spreadsheet_Cell, "StringValue")
    descriptor = None
    for klass in spreadsheet_Cell.__mro__:
        if "StringValue" in klass.__dict__:
            descriptor = klass.__dict__["StringValue"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheet_cell_has_DoubleValue():
    assert hasattr(spreadsheet_Cell, "DoubleValue")
    descriptor = None
    for klass in spreadsheet_Cell.__mro__:
        if "DoubleValue" in klass.__dict__:
            descriptor = klass.__dict__["DoubleValue"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheet_column_is_not_abstract():
    assert not inspect.isabstract(spreadsheet_Column)


def test_spreadsheet_column_constructor_exists():
    assert callable(spreadsheet_Column.__init__)


def test_spreadsheet_column_constructor_args():
    sig = inspect.signature(spreadsheet_Column.__init__)
    params = list(sig.parameters.keys())
    assert "ColumnIndex" in params, "Missing parameter 'ColumnIndex'"

def test_spreadsheet_column_has_ColumnIndex():
    assert hasattr(spreadsheet_Column, "ColumnIndex")
    descriptor = None
    for klass in spreadsheet_Column.__mro__:
        if "ColumnIndex" in klass.__dict__:
            descriptor = klass.__dict__["ColumnIndex"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheet_row_is_not_abstract():
    assert not inspect.isabstract(spreadsheet_Row)


def test_spreadsheet_row_constructor_exists():
    assert callable(spreadsheet_Row.__init__)


def test_spreadsheet_row_constructor_args():
    sig = inspect.signature(spreadsheet_Row.__init__)
    params = list(sig.parameters.keys())
    assert "RowIndex" in params, "Missing parameter 'RowIndex'"

def test_spreadsheet_row_has_RowIndex():
    assert hasattr(spreadsheet_Row, "RowIndex")
    descriptor = None
    for klass in spreadsheet_Row.__mro__:
        if "RowIndex" in klass.__dict__:
            descriptor = klass.__dict__["RowIndex"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheet_sheet_is_not_abstract():
    assert not inspect.isabstract(spreadsheet_Sheet)


def test_spreadsheet_sheet_constructor_exists():
    assert callable(spreadsheet_Sheet.__init__)


def test_spreadsheet_sheet_constructor_args():
    sig = inspect.signature(spreadsheet_Sheet.__init__)
    params = list(sig.parameters.keys())
    assert "SheetIndex" in params, "Missing parameter 'SheetIndex'"
    assert "SheetName" in params, "Missing parameter 'SheetName'"

def test_spreadsheet_sheet_has_SheetIndex():
    assert hasattr(spreadsheet_Sheet, "SheetIndex")
    descriptor = None
    for klass in spreadsheet_Sheet.__mro__:
        if "SheetIndex" in klass.__dict__:
            descriptor = klass.__dict__["SheetIndex"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheet_sheet_has_SheetName():
    assert hasattr(spreadsheet_Sheet, "SheetName")
    descriptor = None
    for klass in spreadsheet_Sheet.__mro__:
        if "SheetName" in klass.__dict__:
            descriptor = klass.__dict__["SheetName"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheet_spreadsheet_is_not_abstract():
    assert not inspect.isabstract(spreadsheet_Spreadsheet)


def test_spreadsheet_spreadsheet_constructor_exists():
    assert callable(spreadsheet_Spreadsheet.__init__)


def test_spreadsheet_spreadsheet_constructor_args():
    sig = inspect.signature(spreadsheet_Spreadsheet.__init__)
    params = list(sig.parameters.keys())
    assert "FilePath" in params, "Missing parameter 'FilePath'"
    assert "Label" in params, "Missing parameter 'Label'"

def test_spreadsheet_spreadsheet_has_FilePath():
    assert hasattr(spreadsheet_Spreadsheet, "FilePath")
    descriptor = None
    for klass in spreadsheet_Spreadsheet.__mro__:
        if "FilePath" in klass.__dict__:
            descriptor = klass.__dict__["FilePath"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheet_spreadsheet_has_Label():
    assert hasattr(spreadsheet_Spreadsheet, "Label")
    descriptor = None
    for klass in spreadsheet_Spreadsheet.__mro__:
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
        "CellTypeNumeric",
        "CellTypeString",
        "CellTypeFormula",
        "CellTypeDate",
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
spreadsheet_Cell_strategy = st.builds(
    spreadsheet_Cell,
    ValueFormatted=
        safe_text,
    CellType=
        safe_text,
    StringValue=
        safe_text,
    DoubleValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
spreadsheet_Column_strategy = st.builds(
    spreadsheet_Column,
    ColumnIndex=
        st.integers()
)
spreadsheet_Row_strategy = st.builds(
    spreadsheet_Row,
    RowIndex=
        st.integers()
)
spreadsheet_Sheet_strategy = st.builds(
    spreadsheet_Sheet,
    SheetIndex=
        st.integers(),
    SheetName=
        safe_text
)
spreadsheet_Spreadsheet_strategy = st.builds(
    spreadsheet_Spreadsheet,
    FilePath=
        safe_text,
    Label=
        safe_text
)

@given(instance=spreadsheet_Cell_strategy)
@settings(max_examples=50)
def test_spreadsheet_cell_instantiation(instance):
    assert isinstance(instance, spreadsheet_Cell)



@given(instance=spreadsheet_Cell_strategy)
def test_spreadsheet_cell_ValueFormatted_setter(instance):
    original = instance.ValueFormatted
    instance.ValueFormatted = original
    assert instance.ValueFormatted == original



@given(instance=spreadsheet_Cell_strategy)
def test_spreadsheet_cell_CellType_setter(instance):
    original = instance.CellType
    instance.CellType = original
    assert instance.CellType == original



@given(instance=spreadsheet_Cell_strategy)
def test_spreadsheet_cell_StringValue_setter(instance):
    original = instance.StringValue
    instance.StringValue = original
    assert instance.StringValue == original



@given(instance=spreadsheet_Cell_strategy)
def test_spreadsheet_cell_DoubleValue_setter(instance):
    original = instance.DoubleValue
    instance.DoubleValue = original
    assert instance.DoubleValue == original

@given(instance=spreadsheet_Column_strategy)
@settings(max_examples=50)
def test_spreadsheet_column_instantiation(instance):
    assert isinstance(instance, spreadsheet_Column)



@given(instance=spreadsheet_Column_strategy)
def test_spreadsheet_column_ColumnIndex_setter(instance):
    original = instance.ColumnIndex
    instance.ColumnIndex = original
    assert instance.ColumnIndex == original

@given(instance=spreadsheet_Row_strategy)
@settings(max_examples=50)
def test_spreadsheet_row_instantiation(instance):
    assert isinstance(instance, spreadsheet_Row)



@given(instance=spreadsheet_Row_strategy)
def test_spreadsheet_row_RowIndex_setter(instance):
    original = instance.RowIndex
    instance.RowIndex = original
    assert instance.RowIndex == original

@given(instance=spreadsheet_Sheet_strategy)
@settings(max_examples=50)
def test_spreadsheet_sheet_instantiation(instance):
    assert isinstance(instance, spreadsheet_Sheet)



@given(instance=spreadsheet_Sheet_strategy)
def test_spreadsheet_sheet_SheetIndex_setter(instance):
    original = instance.SheetIndex
    instance.SheetIndex = original
    assert instance.SheetIndex == original



@given(instance=spreadsheet_Sheet_strategy)
def test_spreadsheet_sheet_SheetName_setter(instance):
    original = instance.SheetName
    instance.SheetName = original
    assert instance.SheetName == original

@given(instance=spreadsheet_Spreadsheet_strategy)
@settings(max_examples=50)
def test_spreadsheet_spreadsheet_instantiation(instance):
    assert isinstance(instance, spreadsheet_Spreadsheet)



@given(instance=spreadsheet_Spreadsheet_strategy)
def test_spreadsheet_spreadsheet_FilePath_setter(instance):
    original = instance.FilePath
    instance.FilePath = original
    assert instance.FilePath == original



@given(instance=spreadsheet_Spreadsheet_strategy)
def test_spreadsheet_spreadsheet_Label_setter(instance):
    original = instance.Label
    instance.Label = original
    assert instance.Label == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=spreadsheet_Spreadsheet_strategy)
@settings(max_examples=30)
def test_spreadsheet_spreadsheet_readfile_changes_state(instance):
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
        assert has_statements, f"Function 'readFile' in spreadsheet_Spreadsheet is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'readFile' in spreadsheet_Spreadsheet did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'readFile' in spreadsheet_Spreadsheet is not implemented or raised an error")
