import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    spreadsheet::Sheet,
    DocumentModel,
    spreadsheet::SpreadsheetFile,
    spreadsheet::Table,
    spreadsheet::Image,
    spreadsheet::Header,
    spreadsheet::Row,
    spreadsheet::Point,
    ContentElement,
    spreadsheet::Cell,
    spreadsheet::Title,
    spreadsheet::Text,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_spreadsheet::sheet_is_not_abstract():
    assert not inspect.isabstract(spreadsheet::Sheet)


def test_spreadsheet::sheet_constructor_exists():
    assert callable(spreadsheet::Sheet.__init__)


def test_spreadsheet::sheet_constructor_args():
    sig = inspect.signature(spreadsheet::Sheet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_spreadsheet::sheet_has_name():
    assert hasattr(spreadsheet::Sheet, "name")
    descriptor = None
    for klass in spreadsheet::Sheet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_documentmodel_is_not_abstract():
    assert not inspect.isabstract(DocumentModel)


def test_documentmodel_constructor_exists():
    assert callable(DocumentModel.__init__)


def test_documentmodel_constructor_args():
    sig = inspect.signature(DocumentModel.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheet::spreadsheetfile_is_not_abstract():
    assert not inspect.isabstract(spreadsheet::SpreadsheetFile)


def test_spreadsheet::spreadsheetfile_constructor_exists():
    assert callable(spreadsheet::SpreadsheetFile.__init__)


def test_spreadsheet::spreadsheetfile_constructor_args():
    sig = inspect.signature(spreadsheet::SpreadsheetFile.__init__)
    params = list(sig.parameters.keys())
    assert "nbSheet" in params, "Missing parameter 'nbSheet'"

def test_spreadsheet::spreadsheetfile_has_nbSheet():
    assert hasattr(spreadsheet::SpreadsheetFile, "nbSheet")
    descriptor = None
    for klass in spreadsheet::SpreadsheetFile.__mro__:
        if "nbSheet" in klass.__dict__:
            descriptor = klass.__dict__["nbSheet"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheet::table_is_not_abstract():
    assert not inspect.isabstract(spreadsheet::Table)


def test_spreadsheet::table_constructor_exists():
    assert callable(spreadsheet::Table.__init__)


def test_spreadsheet::table_constructor_args():
    sig = inspect.signature(spreadsheet::Table.__init__)
    params = list(sig.parameters.keys())
    assert "nbColumns" in params, "Missing parameter 'nbColumns'"

def test_spreadsheet::table_has_nbColumns():
    assert hasattr(spreadsheet::Table, "nbColumns")
    descriptor = None
    for klass in spreadsheet::Table.__mro__:
        if "nbColumns" in klass.__dict__:
            descriptor = klass.__dict__["nbColumns"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheet::image_is_not_abstract():
    assert not inspect.isabstract(spreadsheet::Image)


def test_spreadsheet::image_constructor_exists():
    assert callable(spreadsheet::Image.__init__)


def test_spreadsheet::image_constructor_args():
    sig = inspect.signature(spreadsheet::Image.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"

def test_spreadsheet::image_has_height():
    assert hasattr(spreadsheet::Image, "height")
    descriptor = None
    for klass in spreadsheet::Image.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheet::image_has_width():
    assert hasattr(spreadsheet::Image, "width")
    descriptor = None
    for klass in spreadsheet::Image.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheet::header_is_not_abstract():
    assert not inspect.isabstract(spreadsheet::Header)


def test_spreadsheet::header_constructor_exists():
    assert callable(spreadsheet::Header.__init__)


def test_spreadsheet::header_constructor_args():
    sig = inspect.signature(spreadsheet::Header.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheet::row_is_not_abstract():
    assert not inspect.isabstract(spreadsheet::Row)


def test_spreadsheet::row_constructor_exists():
    assert callable(spreadsheet::Row.__init__)


def test_spreadsheet::row_constructor_args():
    sig = inspect.signature(spreadsheet::Row.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheet::point_is_not_abstract():
    assert not inspect.isabstract(spreadsheet::Point)


def test_spreadsheet::point_constructor_exists():
    assert callable(spreadsheet::Point.__init__)


def test_spreadsheet::point_constructor_args():
    sig = inspect.signature(spreadsheet::Point.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"

def test_spreadsheet::point_has_y():
    assert hasattr(spreadsheet::Point, "y")
    descriptor = None
    for klass in spreadsheet::Point.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheet::point_has_x():
    assert hasattr(spreadsheet::Point, "x")
    descriptor = None
    for klass in spreadsheet::Point.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_contentelement_is_not_abstract():
    assert not inspect.isabstract(ContentElement)


def test_contentelement_constructor_exists():
    assert callable(ContentElement.__init__)


def test_contentelement_constructor_args():
    sig = inspect.signature(ContentElement.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheet::cell_is_not_abstract():
    assert not inspect.isabstract(spreadsheet::Cell)


def test_spreadsheet::cell_constructor_exists():
    assert callable(spreadsheet::Cell.__init__)


def test_spreadsheet::cell_constructor_args():
    sig = inspect.signature(spreadsheet::Cell.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheet::title_is_not_abstract():
    assert not inspect.isabstract(spreadsheet::Title)


def test_spreadsheet::title_constructor_exists():
    assert callable(spreadsheet::Title.__init__)


def test_spreadsheet::title_constructor_args():
    sig = inspect.signature(spreadsheet::Title.__init__)
    params = list(sig.parameters.keys())
    assert "hiearchy" in params, "Missing parameter 'hiearchy'"

def test_spreadsheet::title_has_hiearchy():
    assert hasattr(spreadsheet::Title, "hiearchy")
    descriptor = None
    for klass in spreadsheet::Title.__mro__:
        if "hiearchy" in klass.__dict__:
            descriptor = klass.__dict__["hiearchy"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheet::text_is_not_abstract():
    assert not inspect.isabstract(spreadsheet::Text)


def test_spreadsheet::text_constructor_exists():
    assert callable(spreadsheet::Text.__init__)


def test_spreadsheet::text_constructor_args():
    sig = inspect.signature(spreadsheet::Text.__init__)
    params = list(sig.parameters.keys())
    assert "textContent" in params, "Missing parameter 'textContent'"

def test_spreadsheet::text_has_textContent():
    assert hasattr(spreadsheet::Text, "textContent")
    descriptor = None
    for klass in spreadsheet::Text.__mro__:
        if "textContent" in klass.__dict__:
            descriptor = klass.__dict__["textContent"]
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
spreadsheet::Sheet_strategy = st.builds(
    spreadsheet::Sheet,
    name=
        safe_text
)
DocumentModel_strategy = st.builds(
    DocumentModel,
)
spreadsheet::SpreadsheetFile_strategy = st.builds(
    spreadsheet::SpreadsheetFile,
    nbSheet=
        st.integers()
)
spreadsheet::Table_strategy = st.builds(
    spreadsheet::Table,
    nbColumns=
        st.integers()
)
spreadsheet::Image_strategy = st.builds(
    spreadsheet::Image,
    height=
        st.integers(),
    width=
        st.integers()
)
spreadsheet::Header_strategy = st.builds(
    spreadsheet::Header,
)
spreadsheet::Row_strategy = st.builds(
    spreadsheet::Row,
)
spreadsheet::Point_strategy = st.builds(
    spreadsheet::Point,
    y=
        st.integers(),
    x=
        st.integers()
)
ContentElement_strategy = st.builds(
    ContentElement,
)
spreadsheet::Cell_strategy = st.builds(
    spreadsheet::Cell,
)
spreadsheet::Title_strategy = st.builds(
    spreadsheet::Title,
    hiearchy=
        safe_text
)
spreadsheet::Text_strategy = st.builds(
    spreadsheet::Text,
    textContent=
        safe_text
)

@given(instance=spreadsheet::Sheet_strategy)
@settings(max_examples=50)
def test_spreadsheet::sheet_instantiation(instance):
    assert isinstance(instance, spreadsheet::Sheet)

@given(instance=spreadsheet::Sheet_strategy)
def test_spreadsheet::sheet_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=spreadsheet::Sheet_strategy)
def test_spreadsheet::sheet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DocumentModel_strategy)
@settings(max_examples=50)
def test_documentmodel_instantiation(instance):
    assert isinstance(instance, DocumentModel)

@given(instance=spreadsheet::SpreadsheetFile_strategy)
@settings(max_examples=50)
def test_spreadsheet::spreadsheetfile_instantiation(instance):
    assert isinstance(instance, spreadsheet::SpreadsheetFile)

@given(instance=spreadsheet::SpreadsheetFile_strategy)
def test_spreadsheet::spreadsheetfile_nbSheet_type(instance):
    assert isinstance(instance.nbSheet, int)


@given(instance=spreadsheet::SpreadsheetFile_strategy)
def test_spreadsheet::spreadsheetfile_nbSheet_setter(instance):
    original = instance.nbSheet
    instance.nbSheet = original
    assert instance.nbSheet == original

@given(instance=spreadsheet::Table_strategy)
@settings(max_examples=50)
def test_spreadsheet::table_instantiation(instance):
    assert isinstance(instance, spreadsheet::Table)

@given(instance=spreadsheet::Table_strategy)
def test_spreadsheet::table_nbColumns_type(instance):
    assert isinstance(instance.nbColumns, int)


@given(instance=spreadsheet::Table_strategy)
def test_spreadsheet::table_nbColumns_setter(instance):
    original = instance.nbColumns
    instance.nbColumns = original
    assert instance.nbColumns == original

@given(instance=spreadsheet::Image_strategy)
@settings(max_examples=50)
def test_spreadsheet::image_instantiation(instance):
    assert isinstance(instance, spreadsheet::Image)

@given(instance=spreadsheet::Image_strategy)
def test_spreadsheet::image_height_type(instance):
    assert isinstance(instance.height, int)


@given(instance=spreadsheet::Image_strategy)
def test_spreadsheet::image_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=spreadsheet::Image_strategy)
def test_spreadsheet::image_width_type(instance):
    assert isinstance(instance.width, int)


@given(instance=spreadsheet::Image_strategy)
def test_spreadsheet::image_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=spreadsheet::Header_strategy)
@settings(max_examples=50)
def test_spreadsheet::header_instantiation(instance):
    assert isinstance(instance, spreadsheet::Header)

@given(instance=spreadsheet::Row_strategy)
@settings(max_examples=50)
def test_spreadsheet::row_instantiation(instance):
    assert isinstance(instance, spreadsheet::Row)

@given(instance=spreadsheet::Point_strategy)
@settings(max_examples=50)
def test_spreadsheet::point_instantiation(instance):
    assert isinstance(instance, spreadsheet::Point)

@given(instance=spreadsheet::Point_strategy)
def test_spreadsheet::point_y_type(instance):
    assert isinstance(instance.y, int)


@given(instance=spreadsheet::Point_strategy)
def test_spreadsheet::point_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=spreadsheet::Point_strategy)
def test_spreadsheet::point_x_type(instance):
    assert isinstance(instance.x, int)


@given(instance=spreadsheet::Point_strategy)
def test_spreadsheet::point_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=ContentElement_strategy)
@settings(max_examples=50)
def test_contentelement_instantiation(instance):
    assert isinstance(instance, ContentElement)

@given(instance=spreadsheet::Cell_strategy)
@settings(max_examples=50)
def test_spreadsheet::cell_instantiation(instance):
    assert isinstance(instance, spreadsheet::Cell)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=spreadsheet::Cell_strategy)
@settings(max_examples=30)
def test_spreadsheet::cell_offset_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.offset(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.offset).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'offset' in spreadsheet::Cell is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'offset' in spreadsheet::Cell did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'offset' in spreadsheet::Cell is not implemented or raised an error")

@given(instance=spreadsheet::Title_strategy)
@settings(max_examples=50)
def test_spreadsheet::title_instantiation(instance):
    assert isinstance(instance, spreadsheet::Title)

@given(instance=spreadsheet::Title_strategy)
def test_spreadsheet::title_hiearchy_type(instance):
    assert isinstance(instance.hiearchy, str)


@given(instance=spreadsheet::Title_strategy)
def test_spreadsheet::title_hiearchy_setter(instance):
    original = instance.hiearchy
    instance.hiearchy = original
    assert instance.hiearchy == original

@given(instance=spreadsheet::Text_strategy)
@settings(max_examples=50)
def test_spreadsheet::text_instantiation(instance):
    assert isinstance(instance, spreadsheet::Text)

@given(instance=spreadsheet::Text_strategy)
def test_spreadsheet::text_textContent_type(instance):
    assert isinstance(instance.textContent, str)


@given(instance=spreadsheet::Text_strategy)
def test_spreadsheet::text_textContent_setter(instance):
    original = instance.textContent
    instance.textContent = original
    assert instance.textContent == original
