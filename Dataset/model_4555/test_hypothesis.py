import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    kmLogo::VM::Segment,
    kmLogo::VM::Point,
    Segment,
    Point,
    kmLogo::VM::Turtle,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_kmlogo::vm::segment_is_not_abstract():
    assert not inspect.isabstract(kmLogo::VM::Segment)


def test_kmlogo::vm::segment_constructor_exists():
    assert callable(kmLogo::VM::Segment.__init__)


def test_kmlogo::vm::segment_constructor_args():
    sig = inspect.signature(kmLogo::VM::Segment.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::vm::point_is_not_abstract():
    assert not inspect.isabstract(kmLogo::VM::Point)


def test_kmlogo::vm::point_constructor_exists():
    assert callable(kmLogo::VM::Point.__init__)


def test_kmlogo::vm::point_constructor_args():
    sig = inspect.signature(kmLogo::VM::Point.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"

def test_kmlogo::vm::point_has_y():
    assert hasattr(kmLogo::VM::Point, "y")
    descriptor = None
    for klass in kmLogo::VM::Point.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_kmlogo::vm::point_has_x():
    assert hasattr(kmLogo::VM::Point, "x")
    descriptor = None
    for klass in kmLogo::VM::Point.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_segment_is_not_abstract():
    assert not inspect.isabstract(Segment)


def test_segment_constructor_exists():
    assert callable(Segment.__init__)


def test_segment_constructor_args():
    sig = inspect.signature(Segment.__init__)
    params = list(sig.parameters.keys())



def test_point_is_not_abstract():
    assert not inspect.isabstract(Point)


def test_point_constructor_exists():
    assert callable(Point.__init__)


def test_point_constructor_args():
    sig = inspect.signature(Point.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::vm::turtle_is_not_abstract():
    assert not inspect.isabstract(kmLogo::VM::Turtle)


def test_kmlogo::vm::turtle_constructor_exists():
    assert callable(kmLogo::VM::Turtle.__init__)


def test_kmlogo::vm::turtle_constructor_args():
    sig = inspect.signature(kmLogo::VM::Turtle.__init__)
    params = list(sig.parameters.keys())
    assert "heading" in params, "Missing parameter 'heading'"
    assert "penUp" in params, "Missing parameter 'penUp'"

def test_kmlogo::vm::turtle_has_heading():
    assert hasattr(kmLogo::VM::Turtle, "heading")
    descriptor = None
    for klass in kmLogo::VM::Turtle.__mro__:
        if "heading" in klass.__dict__:
            descriptor = klass.__dict__["heading"]
            break
    assert isinstance(descriptor, property)

def test_kmlogo::vm::turtle_has_penUp():
    assert hasattr(kmLogo::VM::Turtle, "penUp")
    descriptor = None
    for klass in kmLogo::VM::Turtle.__mro__:
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
kmLogo::VM::Segment_strategy = st.builds(
    kmLogo::VM::Segment,
)
kmLogo::VM::Point_strategy = st.builds(
    kmLogo::VM::Point,
    y=
        safe_text,
    x=
        safe_text
)
Segment_strategy = st.builds(
    Segment,
)
Point_strategy = st.builds(
    Point,
)
kmLogo::VM::Turtle_strategy = st.builds(
    kmLogo::VM::Turtle,
    heading=
        safe_text,
    penUp=
        safe_text
)

@given(instance=kmLogo::VM::Segment_strategy)
@settings(max_examples=50)
def test_kmlogo::vm::segment_instantiation(instance):
    assert isinstance(instance, kmLogo::VM::Segment)

@given(instance=kmLogo::VM::Point_strategy)
@settings(max_examples=50)
def test_kmlogo::vm::point_instantiation(instance):
    assert isinstance(instance, kmLogo::VM::Point)

@given(instance=kmLogo::VM::Point_strategy)
def test_kmlogo::vm::point_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=kmLogo::VM::Point_strategy)
def test_kmlogo::vm::point_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=kmLogo::VM::Point_strategy)
def test_kmlogo::vm::point_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=kmLogo::VM::Point_strategy)
def test_kmlogo::vm::point_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=Segment_strategy)
@settings(max_examples=50)
def test_segment_instantiation(instance):
    assert isinstance(instance, Segment)

@given(instance=Point_strategy)
@settings(max_examples=50)
def test_point_instantiation(instance):
    assert isinstance(instance, Point)

@given(instance=kmLogo::VM::Turtle_strategy)
@settings(max_examples=50)
def test_kmlogo::vm::turtle_instantiation(instance):
    assert isinstance(instance, kmLogo::VM::Turtle)

@given(instance=kmLogo::VM::Turtle_strategy)
def test_kmlogo::vm::turtle_heading_type(instance):
    assert isinstance(instance.heading, str)


@given(instance=kmLogo::VM::Turtle_strategy)
def test_kmlogo::vm::turtle_heading_setter(instance):
    original = instance.heading
    instance.heading = original
    assert instance.heading == original

@given(instance=kmLogo::VM::Turtle_strategy)
def test_kmlogo::vm::turtle_penUp_type(instance):
    assert isinstance(instance.penUp, str)


@given(instance=kmLogo::VM::Turtle_strategy)
def test_kmlogo::vm::turtle_penUp_setter(instance):
    original = instance.penUp
    instance.penUp = original
    assert instance.penUp == original
