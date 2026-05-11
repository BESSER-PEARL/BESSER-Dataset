import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    vmlogo::Variable,
    vmlogo::StackFrame,
    vmlogo::CallStack,
    vmlogo::Point,
    vmlogo::Turtle,
    vmlogo::Segment,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_vmlogo::variable_is_not_abstract():
    assert not inspect.isabstract(vmlogo::Variable)


def test_vmlogo::variable_constructor_exists():
    assert callable(vmlogo::Variable.__init__)


def test_vmlogo::variable_constructor_args():
    sig = inspect.signature(vmlogo::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_vmlogo::variable_has_name():
    assert hasattr(vmlogo::Variable, "name")
    descriptor = None
    for klass in vmlogo::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_vmlogo::variable_has_value():
    assert hasattr(vmlogo::Variable, "value")
    descriptor = None
    for klass in vmlogo::Variable.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vmlogo::stackframe_is_not_abstract():
    assert not inspect.isabstract(vmlogo::StackFrame)


def test_vmlogo::stackframe_constructor_exists():
    assert callable(vmlogo::StackFrame.__init__)


def test_vmlogo::stackframe_constructor_args():
    sig = inspect.signature(vmlogo::StackFrame.__init__)
    params = list(sig.parameters.keys())



def test_vmlogo::callstack_is_not_abstract():
    assert not inspect.isabstract(vmlogo::CallStack)


def test_vmlogo::callstack_constructor_exists():
    assert callable(vmlogo::CallStack.__init__)


def test_vmlogo::callstack_constructor_args():
    sig = inspect.signature(vmlogo::CallStack.__init__)
    params = list(sig.parameters.keys())



def test_vmlogo::point_is_not_abstract():
    assert not inspect.isabstract(vmlogo::Point)


def test_vmlogo::point_constructor_exists():
    assert callable(vmlogo::Point.__init__)


def test_vmlogo::point_constructor_args():
    sig = inspect.signature(vmlogo::Point.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_vmlogo::point_has_x():
    assert hasattr(vmlogo::Point, "x")
    descriptor = None
    for klass in vmlogo::Point.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_vmlogo::point_has_y():
    assert hasattr(vmlogo::Point, "y")
    descriptor = None
    for klass in vmlogo::Point.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_vmlogo::turtle_is_not_abstract():
    assert not inspect.isabstract(vmlogo::Turtle)


def test_vmlogo::turtle_constructor_exists():
    assert callable(vmlogo::Turtle.__init__)


def test_vmlogo::turtle_constructor_args():
    sig = inspect.signature(vmlogo::Turtle.__init__)
    params = list(sig.parameters.keys())
    assert "penUp" in params, "Missing parameter 'penUp'"
    assert "heading" in params, "Missing parameter 'heading'"

def test_vmlogo::turtle_has_penUp():
    assert hasattr(vmlogo::Turtle, "penUp")
    descriptor = None
    for klass in vmlogo::Turtle.__mro__:
        if "penUp" in klass.__dict__:
            descriptor = klass.__dict__["penUp"]
            break
    assert isinstance(descriptor, property)

def test_vmlogo::turtle_has_heading():
    assert hasattr(vmlogo::Turtle, "heading")
    descriptor = None
    for klass in vmlogo::Turtle.__mro__:
        if "heading" in klass.__dict__:
            descriptor = klass.__dict__["heading"]
            break
    assert isinstance(descriptor, property)



def test_vmlogo::segment_is_not_abstract():
    assert not inspect.isabstract(vmlogo::Segment)


def test_vmlogo::segment_constructor_exists():
    assert callable(vmlogo::Segment.__init__)


def test_vmlogo::segment_constructor_args():
    sig = inspect.signature(vmlogo::Segment.__init__)
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
vmlogo::Variable_strategy = st.builds(
    vmlogo::Variable,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
vmlogo::StackFrame_strategy = st.builds(
    vmlogo::StackFrame,
)
vmlogo::CallStack_strategy = st.builds(
    vmlogo::CallStack,
)
vmlogo::Point_strategy = st.builds(
    vmlogo::Point,
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    y=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
vmlogo::Turtle_strategy = st.builds(
    vmlogo::Turtle,
    penUp=
        st.booleans(),
    heading=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
vmlogo::Segment_strategy = st.builds(
    vmlogo::Segment,
)

@given(instance=vmlogo::Variable_strategy)
@settings(max_examples=50)
def test_vmlogo::variable_instantiation(instance):
    assert isinstance(instance, vmlogo::Variable)

@given(instance=vmlogo::Variable_strategy)
def test_vmlogo::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=vmlogo::Variable_strategy)
def test_vmlogo::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=vmlogo::Variable_strategy)
def test_vmlogo::variable_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=vmlogo::Variable_strategy)
def test_vmlogo::variable_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vmlogo::StackFrame_strategy)
@settings(max_examples=50)
def test_vmlogo::stackframe_instantiation(instance):
    assert isinstance(instance, vmlogo::StackFrame)

@given(instance=vmlogo::CallStack_strategy)
@settings(max_examples=50)
def test_vmlogo::callstack_instantiation(instance):
    assert isinstance(instance, vmlogo::CallStack)

@given(instance=vmlogo::Point_strategy)
@settings(max_examples=50)
def test_vmlogo::point_instantiation(instance):
    assert isinstance(instance, vmlogo::Point)

@given(instance=vmlogo::Point_strategy)
def test_vmlogo::point_x_type(instance):
    assert isinstance(instance.x, float)


@given(instance=vmlogo::Point_strategy)
def test_vmlogo::point_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=vmlogo::Point_strategy)
def test_vmlogo::point_y_type(instance):
    assert isinstance(instance.y, float)


@given(instance=vmlogo::Point_strategy)
def test_vmlogo::point_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=vmlogo::Turtle_strategy)
@settings(max_examples=50)
def test_vmlogo::turtle_instantiation(instance):
    assert isinstance(instance, vmlogo::Turtle)

@given(instance=vmlogo::Turtle_strategy)
def test_vmlogo::turtle_penUp_type(instance):
    assert isinstance(instance.penUp, bool)


@given(instance=vmlogo::Turtle_strategy)
def test_vmlogo::turtle_penUp_setter(instance):
    original = instance.penUp
    instance.penUp = original
    assert instance.penUp == original

@given(instance=vmlogo::Turtle_strategy)
def test_vmlogo::turtle_heading_type(instance):
    assert isinstance(instance.heading, float)


@given(instance=vmlogo::Turtle_strategy)
def test_vmlogo::turtle_heading_setter(instance):
    original = instance.heading
    instance.heading = original
    assert instance.heading == original

@given(instance=vmlogo::Segment_strategy)
@settings(max_examples=50)
def test_vmlogo::segment_instantiation(instance):
    assert isinstance(instance, vmlogo::Segment)
