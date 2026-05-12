import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    vmLogo_Segment,
    vmLogo_Point,
    vmLogo_Turtle,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_vmlogo_segment_is_not_abstract():
    assert not inspect.isabstract(vmLogo_Segment)


def test_vmlogo_segment_constructor_exists():
    assert callable(vmLogo_Segment.__init__)


def test_vmlogo_segment_constructor_args():
    sig = inspect.signature(vmLogo_Segment.__init__)
    params = list(sig.parameters.keys())



def test_vmlogo_point_is_not_abstract():
    assert not inspect.isabstract(vmLogo_Point)


def test_vmlogo_point_constructor_exists():
    assert callable(vmLogo_Point.__init__)


def test_vmlogo_point_constructor_args():
    sig = inspect.signature(vmLogo_Point.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_vmlogo_point_has_x():
    assert hasattr(vmLogo_Point, "x")
    descriptor = None
    for klass in vmLogo_Point.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_vmlogo_point_has_y():
    assert hasattr(vmLogo_Point, "y")
    descriptor = None
    for klass in vmLogo_Point.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_vmlogo_turtle_is_not_abstract():
    assert not inspect.isabstract(vmLogo_Turtle)


def test_vmlogo_turtle_constructor_exists():
    assert callable(vmLogo_Turtle.__init__)


def test_vmlogo_turtle_constructor_args():
    sig = inspect.signature(vmLogo_Turtle.__init__)
    params = list(sig.parameters.keys())
    assert "heading" in params, "Missing parameter 'heading'"
    assert "penUp" in params, "Missing parameter 'penUp'"

def test_vmlogo_turtle_has_heading():
    assert hasattr(vmLogo_Turtle, "heading")
    descriptor = None
    for klass in vmLogo_Turtle.__mro__:
        if "heading" in klass.__dict__:
            descriptor = klass.__dict__["heading"]
            break
    assert isinstance(descriptor, property)

def test_vmlogo_turtle_has_penUp():
    assert hasattr(vmLogo_Turtle, "penUp")
    descriptor = None
    for klass in vmLogo_Turtle.__mro__:
        if "penUp" in klass.__dict__:
            descriptor = klass.__dict__["penUp"]
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
vmLogo_Segment_strategy = st.builds(
    vmLogo_Segment,
)
vmLogo_Point_strategy = st.builds(
    vmLogo_Point,
    x=
        safe_text,
    y=
        safe_text
)
vmLogo_Turtle_strategy = st.builds(
    vmLogo_Turtle,
    heading=
        safe_text,
    penUp=
        safe_text
)

@given(instance=vmLogo_Segment_strategy)
@settings(max_examples=50)
def test_vmlogo_segment_instantiation(instance):
    assert isinstance(instance, vmLogo_Segment)

@given(instance=vmLogo_Point_strategy)
@settings(max_examples=50)
def test_vmlogo_point_instantiation(instance):
    assert isinstance(instance, vmLogo_Point)



@given(instance=vmLogo_Point_strategy)
def test_vmlogo_point_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=vmLogo_Point_strategy)
def test_vmlogo_point_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=vmLogo_Turtle_strategy)
@settings(max_examples=50)
def test_vmlogo_turtle_instantiation(instance):
    assert isinstance(instance, vmLogo_Turtle)



@given(instance=vmLogo_Turtle_strategy)
def test_vmlogo_turtle_heading_setter(instance):
    original = instance.heading
    instance.heading = original
    assert instance.heading == original



@given(instance=vmLogo_Turtle_strategy)
def test_vmlogo_turtle_penUp_setter(instance):
    original = instance.penUp
    instance.penUp = original
    assert instance.penUp == original
