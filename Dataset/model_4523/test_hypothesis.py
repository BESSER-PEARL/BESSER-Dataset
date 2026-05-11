import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    vmlogo::Segment,
    vmlogo::Point,
    vmlogo::CallStack,
    vmlogo::Turtle,
    vmlogo::StackFrame,
    vmlogo::Context,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_vmlogo::segment_is_not_abstract():
    assert not inspect.isabstract(vmlogo::Segment)


def test_vmlogo::segment_constructor_exists():
    assert callable(vmlogo::Segment.__init__)


def test_vmlogo::segment_constructor_args():
    sig = inspect.signature(vmlogo::Segment.__init__)
    params = list(sig.parameters.keys())



def test_vmlogo::point_is_not_abstract():
    assert not inspect.isabstract(vmlogo::Point)


def test_vmlogo::point_constructor_exists():
    assert callable(vmlogo::Point.__init__)


def test_vmlogo::point_constructor_args():
    sig = inspect.signature(vmlogo::Point.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"

def test_vmlogo::point_has_y():
    assert hasattr(vmlogo::Point, "y")
    descriptor = None
    for klass in vmlogo::Point.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_vmlogo::point_has_x():
    assert hasattr(vmlogo::Point, "x")
    descriptor = None
    for klass in vmlogo::Point.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_vmlogo::callstack_is_not_abstract():
    assert not inspect.isabstract(vmlogo::CallStack)


def test_vmlogo::callstack_constructor_exists():
    assert callable(vmlogo::CallStack.__init__)


def test_vmlogo::callstack_constructor_args():
    sig = inspect.signature(vmlogo::CallStack.__init__)
    params = list(sig.parameters.keys())



def test_vmlogo::turtle_is_not_abstract():
    assert not inspect.isabstract(vmlogo::Turtle)


def test_vmlogo::turtle_constructor_exists():
    assert callable(vmlogo::Turtle.__init__)


def test_vmlogo::turtle_constructor_args():
    sig = inspect.signature(vmlogo::Turtle.__init__)
    params = list(sig.parameters.keys())
    assert "heading" in params, "Missing parameter 'heading'"
    assert "penUp" in params, "Missing parameter 'penUp'"

def test_vmlogo::turtle_has_heading():
    assert hasattr(vmlogo::Turtle, "heading")
    descriptor = None
    for klass in vmlogo::Turtle.__mro__:
        if "heading" in klass.__dict__:
            descriptor = klass.__dict__["heading"]
            break
    assert isinstance(descriptor, property)

def test_vmlogo::turtle_has_penUp():
    assert hasattr(vmlogo::Turtle, "penUp")
    descriptor = None
    for klass in vmlogo::Turtle.__mro__:
        if "penUp" in klass.__dict__:
            descriptor = klass.__dict__["penUp"]
            break
    assert isinstance(descriptor, property)



def test_vmlogo::stackframe_is_not_abstract():
    assert not inspect.isabstract(vmlogo::StackFrame)


def test_vmlogo::stackframe_constructor_exists():
    assert callable(vmlogo::StackFrame.__init__)


def test_vmlogo::stackframe_constructor_args():
    sig = inspect.signature(vmlogo::StackFrame.__init__)
    params = list(sig.parameters.keys())
    assert "variables" in params, "Missing parameter 'variables'"

def test_vmlogo::stackframe_has_variables():
    assert hasattr(vmlogo::StackFrame, "variables")
    descriptor = None
    for klass in vmlogo::StackFrame.__mro__:
        if "variables" in klass.__dict__:
            descriptor = klass.__dict__["variables"]
            break
    assert isinstance(descriptor, property)



def test_vmlogo::context_is_not_abstract():
    assert not inspect.isabstract(vmlogo::Context)


def test_vmlogo::context_constructor_exists():
    assert callable(vmlogo::Context.__init__)


def test_vmlogo::context_constructor_args():
    sig = inspect.signature(vmlogo::Context.__init__)
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
vmlogo::Segment_strategy = st.builds(
    vmlogo::Segment,
)
vmlogo::Point_strategy = st.builds(
    vmlogo::Point,
    y=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
vmlogo::CallStack_strategy = st.builds(
    vmlogo::CallStack,
)
vmlogo::Turtle_strategy = st.builds(
    vmlogo::Turtle,
    heading=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    penUp=
        st.booleans()
)
vmlogo::StackFrame_strategy = st.builds(
    vmlogo::StackFrame,
    variables=
        safe_text
)
vmlogo::Context_strategy = st.builds(
    vmlogo::Context,
)

@given(instance=vmlogo::Segment_strategy)
@settings(max_examples=50)
def test_vmlogo::segment_instantiation(instance):
    assert isinstance(instance, vmlogo::Segment)

@given(instance=vmlogo::Point_strategy)
@settings(max_examples=50)
def test_vmlogo::point_instantiation(instance):
    assert isinstance(instance, vmlogo::Point)

@given(instance=vmlogo::Point_strategy)
def test_vmlogo::point_y_type(instance):
    assert isinstance(instance.y, float)


@given(instance=vmlogo::Point_strategy)
def test_vmlogo::point_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=vmlogo::Point_strategy)
def test_vmlogo::point_x_type(instance):
    assert isinstance(instance.x, float)


@given(instance=vmlogo::Point_strategy)
def test_vmlogo::point_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=vmlogo::CallStack_strategy)
@settings(max_examples=50)
def test_vmlogo::callstack_instantiation(instance):
    assert isinstance(instance, vmlogo::CallStack)

@given(instance=vmlogo::Turtle_strategy)
@settings(max_examples=50)
def test_vmlogo::turtle_instantiation(instance):
    assert isinstance(instance, vmlogo::Turtle)

@given(instance=vmlogo::Turtle_strategy)
def test_vmlogo::turtle_heading_type(instance):
    assert isinstance(instance.heading, float)


@given(instance=vmlogo::Turtle_strategy)
def test_vmlogo::turtle_heading_setter(instance):
    original = instance.heading
    instance.heading = original
    assert instance.heading == original

@given(instance=vmlogo::Turtle_strategy)
def test_vmlogo::turtle_penUp_type(instance):
    assert isinstance(instance.penUp, bool)


@given(instance=vmlogo::Turtle_strategy)
def test_vmlogo::turtle_penUp_setter(instance):
    original = instance.penUp
    instance.penUp = original
    assert instance.penUp == original

@given(instance=vmlogo::StackFrame_strategy)
@settings(max_examples=50)
def test_vmlogo::stackframe_instantiation(instance):
    assert isinstance(instance, vmlogo::StackFrame)

@given(instance=vmlogo::StackFrame_strategy)
def test_vmlogo::stackframe_variables_type(instance):
    assert isinstance(instance.variables, str)


@given(instance=vmlogo::StackFrame_strategy)
def test_vmlogo::stackframe_variables_setter(instance):
    original = instance.variables
    instance.variables = original
    assert instance.variables == original

@given(instance=vmlogo::Context_strategy)
@settings(max_examples=50)
def test_vmlogo::context_instantiation(instance):
    assert isinstance(instance, vmlogo::Context)
