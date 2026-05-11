import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    vmLogo::Segment,
    vmLogo::Point,
    vmLogo::Turtle,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_vmlogo::segment_is_not_abstract():
    assert not inspect.isabstract(vmLogo::Segment)


def test_vmlogo::segment_constructor_exists():
    assert callable(vmLogo::Segment.__init__)


def test_vmlogo::segment_constructor_args():
    sig = inspect.signature(vmLogo::Segment.__init__)
    params = list(sig.parameters.keys())



def test_vmlogo::point_is_not_abstract():
    assert not inspect.isabstract(vmLogo::Point)


def test_vmlogo::point_constructor_exists():
    assert callable(vmLogo::Point.__init__)


def test_vmlogo::point_constructor_args():
    sig = inspect.signature(vmLogo::Point.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_vmlogo::point_has_x():
    assert hasattr(vmLogo::Point, "x")
    descriptor = None
    for klass in vmLogo::Point.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_vmlogo::point_has_y():
    assert hasattr(vmLogo::Point, "y")
    descriptor = None
    for klass in vmLogo::Point.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_vmlogo::turtle_is_not_abstract():
    assert not inspect.isabstract(vmLogo::Turtle)


def test_vmlogo::turtle_constructor_exists():
    assert callable(vmLogo::Turtle.__init__)


def test_vmlogo::turtle_constructor_args():
    sig = inspect.signature(vmLogo::Turtle.__init__)
    params = list(sig.parameters.keys())
    assert "penUp" in params, "Missing parameter 'penUp'"
    assert "heading" in params, "Missing parameter 'heading'"

def test_vmlogo::turtle_has_penUp():
    assert hasattr(vmLogo::Turtle, "penUp")
    descriptor = None
    for klass in vmLogo::Turtle.__mro__:
        if "penUp" in klass.__dict__:
            descriptor = klass.__dict__["penUp"]
            break
    assert isinstance(descriptor, property)

def test_vmlogo::turtle_has_heading():
    assert hasattr(vmLogo::Turtle, "heading")
    descriptor = None
    for klass in vmLogo::Turtle.__mro__:
        if "heading" in klass.__dict__:
            descriptor = klass.__dict__["heading"]
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
vmLogo::Segment_strategy = st.builds(
    vmLogo::Segment,
)
vmLogo::Point_strategy = st.builds(
    vmLogo::Point,
    x=
        safe_text,
    y=
        safe_text
)
vmLogo::Turtle_strategy = st.builds(
    vmLogo::Turtle,
    penUp=
        safe_text,
    heading=
        safe_text
)

@given(instance=vmLogo::Segment_strategy)
@settings(max_examples=50)
def test_vmlogo::segment_instantiation(instance):
    assert isinstance(instance, vmLogo::Segment)

@given(instance=vmLogo::Point_strategy)
@settings(max_examples=50)
def test_vmlogo::point_instantiation(instance):
    assert isinstance(instance, vmLogo::Point)

@given(instance=vmLogo::Point_strategy)
def test_vmlogo::point_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=vmLogo::Point_strategy)
def test_vmlogo::point_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=vmLogo::Point_strategy)
def test_vmlogo::point_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=vmLogo::Point_strategy)
def test_vmlogo::point_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=vmLogo::Turtle_strategy)
@settings(max_examples=50)
def test_vmlogo::turtle_instantiation(instance):
    assert isinstance(instance, vmLogo::Turtle)

@given(instance=vmLogo::Turtle_strategy)
def test_vmlogo::turtle_penUp_type(instance):
    assert isinstance(instance.penUp, str)


@given(instance=vmLogo::Turtle_strategy)
def test_vmlogo::turtle_penUp_setter(instance):
    original = instance.penUp
    instance.penUp = original
    assert instance.penUp == original

@given(instance=vmLogo::Turtle_strategy)
def test_vmlogo::turtle_heading_type(instance):
    assert isinstance(instance.heading, str)


@given(instance=vmLogo::Turtle_strategy)
def test_vmlogo::turtle_heading_setter(instance):
    original = instance.heading
    instance.heading = original
    assert instance.heading == original
