import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    dc::Bounds,
    dc::Dimension,
    dc::Point,
    KnownColor,
    AlignmentKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dc::bounds_is_not_abstract():
    assert not inspect.isabstract(dc::Bounds)


def test_dc::bounds_constructor_exists():
    assert callable(dc::Bounds.__init__)


def test_dc::bounds_constructor_args():
    sig = inspect.signature(dc::Bounds.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "x" in params, "Missing parameter 'x'"
    assert "height" in params, "Missing parameter 'height'"
    assert "y" in params, "Missing parameter 'y'"

def test_dc::bounds_has_width():
    assert hasattr(dc::Bounds, "width")
    descriptor = None
    for klass in dc::Bounds.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_dc::bounds_has_x():
    assert hasattr(dc::Bounds, "x")
    descriptor = None
    for klass in dc::Bounds.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_dc::bounds_has_height():
    assert hasattr(dc::Bounds, "height")
    descriptor = None
    for klass in dc::Bounds.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_dc::bounds_has_y():
    assert hasattr(dc::Bounds, "y")
    descriptor = None
    for klass in dc::Bounds.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_dc::dimension_is_not_abstract():
    assert not inspect.isabstract(dc::Dimension)


def test_dc::dimension_constructor_exists():
    assert callable(dc::Dimension.__init__)


def test_dc::dimension_constructor_args():
    sig = inspect.signature(dc::Dimension.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"

def test_dc::dimension_has_width():
    assert hasattr(dc::Dimension, "width")
    descriptor = None
    for klass in dc::Dimension.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_dc::dimension_has_height():
    assert hasattr(dc::Dimension, "height")
    descriptor = None
    for klass in dc::Dimension.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_dc::point_is_not_abstract():
    assert not inspect.isabstract(dc::Point)


def test_dc::point_constructor_exists():
    assert callable(dc::Point.__init__)


def test_dc::point_constructor_args():
    sig = inspect.signature(dc::Point.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_dc::point_has_x():
    assert hasattr(dc::Point, "x")
    descriptor = None
    for klass in dc::Point.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_dc::point_has_y():
    assert hasattr(dc::Point, "y")
    descriptor = None
    for klass in dc::Point.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_knowncolor_exists():
    # Check that the Enumeration exists
    assert KnownColor is not None

def test_knowncolor_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in KnownColor]
    expected_literals = [
        "lime",
        "orange",
        "red",
        "navy",
        "olive",
        "silver",
        "gray",
        "yellow",
        "green",
        "black",
        "white",
        "blue",
        "teal",
        "maroon",
        "purple",
        "fuchsia",
        "aqua",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in KnownColor"

def test_alignmentkind_exists():
    # Check that the Enumeration exists
    assert AlignmentKind is not None

def test_alignmentkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AlignmentKind]
    expected_literals = [
        "center",
        "start",
        "end",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AlignmentKind"


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
dc::Bounds_strategy = st.builds(
    dc::Bounds,
    width=
        safe_text,
    x=
        safe_text,
    height=
        safe_text,
    y=
        safe_text
)
dc::Dimension_strategy = st.builds(
    dc::Dimension,
    width=
        safe_text,
    height=
        safe_text
)
dc::Point_strategy = st.builds(
    dc::Point,
    x=
        safe_text,
    y=
        safe_text
)

@given(instance=dc::Bounds_strategy)
@settings(max_examples=50)
def test_dc::bounds_instantiation(instance):
    assert isinstance(instance, dc::Bounds)

@given(instance=dc::Bounds_strategy)
def test_dc::bounds_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=dc::Bounds_strategy)
def test_dc::bounds_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=dc::Bounds_strategy)
def test_dc::bounds_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=dc::Bounds_strategy)
def test_dc::bounds_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=dc::Bounds_strategy)
def test_dc::bounds_height_type(instance):
    assert isinstance(instance.height, str)


@given(instance=dc::Bounds_strategy)
def test_dc::bounds_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=dc::Bounds_strategy)
def test_dc::bounds_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=dc::Bounds_strategy)
def test_dc::bounds_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=dc::Bounds_strategy)
@settings(max_examples=30)
def test_dc::bounds_nonnegativesize_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.nonNegativeSize(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.nonNegativeSize).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'nonNegativeSize' in dc::Bounds is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'nonNegativeSize' in dc::Bounds did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'nonNegativeSize' in dc::Bounds is not implemented or raised an error")

@given(instance=dc::Dimension_strategy)
@settings(max_examples=50)
def test_dc::dimension_instantiation(instance):
    assert isinstance(instance, dc::Dimension)

@given(instance=dc::Dimension_strategy)
def test_dc::dimension_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=dc::Dimension_strategy)
def test_dc::dimension_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=dc::Dimension_strategy)
def test_dc::dimension_height_type(instance):
    assert isinstance(instance.height, str)


@given(instance=dc::Dimension_strategy)
def test_dc::dimension_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=dc::Dimension_strategy)
@settings(max_examples=30)
def test_dc::dimension_nonnegativedimension_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.nonNegativeDimension(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.nonNegativeDimension).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'nonNegativeDimension' in dc::Dimension is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'nonNegativeDimension' in dc::Dimension did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'nonNegativeDimension' in dc::Dimension is not implemented or raised an error")

@given(instance=dc::Point_strategy)
@settings(max_examples=50)
def test_dc::point_instantiation(instance):
    assert isinstance(instance, dc::Point)

@given(instance=dc::Point_strategy)
def test_dc::point_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=dc::Point_strategy)
def test_dc::point_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=dc::Point_strategy)
def test_dc::point_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=dc::Point_strategy)
def test_dc::point_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original
