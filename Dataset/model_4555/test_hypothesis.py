import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    kmLogo_VM_Segment,
    kmLogo_VM_Point,
    Segment,
    Point,
    kmLogo_VM_Turtle,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_kmlogo_vm_segment_is_not_abstract():
    assert not inspect.isabstract(kmLogo_VM_Segment)


def test_kmlogo_vm_segment_constructor_exists():
    assert callable(kmLogo_VM_Segment.__init__)


def test_kmlogo_vm_segment_constructor_args():
    sig = inspect.signature(kmLogo_VM_Segment.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo_vm_point_is_not_abstract():
    assert not inspect.isabstract(kmLogo_VM_Point)


def test_kmlogo_vm_point_constructor_exists():
    assert callable(kmLogo_VM_Point.__init__)


def test_kmlogo_vm_point_constructor_args():
    sig = inspect.signature(kmLogo_VM_Point.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_kmlogo_vm_point_has_x():
    assert hasattr(kmLogo_VM_Point, "x")
    descriptor = None
    for klass in kmLogo_VM_Point.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_kmlogo_vm_point_has_y():
    assert hasattr(kmLogo_VM_Point, "y")
    descriptor = None
    for klass in kmLogo_VM_Point.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
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



def test_kmlogo_vm_turtle_is_not_abstract():
    assert not inspect.isabstract(kmLogo_VM_Turtle)


def test_kmlogo_vm_turtle_constructor_exists():
    assert callable(kmLogo_VM_Turtle.__init__)


def test_kmlogo_vm_turtle_constructor_args():
    sig = inspect.signature(kmLogo_VM_Turtle.__init__)
    params = list(sig.parameters.keys())
    assert "heading" in params, "Missing parameter 'heading'"
    assert "penUp" in params, "Missing parameter 'penUp'"

def test_kmlogo_vm_turtle_has_heading():
    assert hasattr(kmLogo_VM_Turtle, "heading")
    descriptor = None
    for klass in kmLogo_VM_Turtle.__mro__:
        if "heading" in klass.__dict__:
            descriptor = klass.__dict__["heading"]
            break
    assert isinstance(descriptor, property)

def test_kmlogo_vm_turtle_has_penUp():
    assert hasattr(kmLogo_VM_Turtle, "penUp")
    descriptor = None
    for klass in kmLogo_VM_Turtle.__mro__:
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
kmLogo_VM_Segment_strategy = st.builds(
    kmLogo_VM_Segment,
)
kmLogo_VM_Point_strategy = st.builds(
    kmLogo_VM_Point,
    x=
        safe_text,
    y=
        safe_text
)
Segment_strategy = st.builds(
    Segment,
)
Point_strategy = st.builds(
    Point,
)
kmLogo_VM_Turtle_strategy = st.builds(
    kmLogo_VM_Turtle,
    heading=
        safe_text,
    penUp=
        safe_text
)

@given(instance=kmLogo_VM_Segment_strategy)
@settings(max_examples=50)
def test_kmlogo_vm_segment_instantiation(instance):
    assert isinstance(instance, kmLogo_VM_Segment)

@given(instance=kmLogo_VM_Point_strategy)
@settings(max_examples=50)
def test_kmlogo_vm_point_instantiation(instance):
    assert isinstance(instance, kmLogo_VM_Point)



@given(instance=kmLogo_VM_Point_strategy)
def test_kmlogo_vm_point_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=kmLogo_VM_Point_strategy)
def test_kmlogo_vm_point_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=Segment_strategy)
@settings(max_examples=50)
def test_segment_instantiation(instance):
    assert isinstance(instance, Segment)

@given(instance=Point_strategy)
@settings(max_examples=50)
def test_point_instantiation(instance):
    assert isinstance(instance, Point)

@given(instance=kmLogo_VM_Turtle_strategy)
@settings(max_examples=50)
def test_kmlogo_vm_turtle_instantiation(instance):
    assert isinstance(instance, kmLogo_VM_Turtle)



@given(instance=kmLogo_VM_Turtle_strategy)
def test_kmlogo_vm_turtle_heading_setter(instance):
    original = instance.heading
    instance.heading = original
    assert instance.heading == original



@given(instance=kmLogo_VM_Turtle_strategy)
def test_kmlogo_vm_turtle_penUp_setter(instance):
    original = instance.penUp
    instance.penUp = original
    assert instance.penUp == original
