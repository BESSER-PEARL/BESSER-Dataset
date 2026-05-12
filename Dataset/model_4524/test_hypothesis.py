import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    vmlogo_Variable,
    vmlogo_StackFrame,
    vmlogo_CallStack,
    vmlogo_Point,
    vmlogo_Turtle,
    vmlogo_Segment,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_vmlogo_variable_is_not_abstract():
    assert not inspect.isabstract(vmlogo_Variable)


def test_vmlogo_variable_constructor_exists():
    assert callable(vmlogo_Variable.__init__)


def test_vmlogo_variable_constructor_args():
    sig = inspect.signature(vmlogo_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_vmlogo_variable_has_name():
    assert hasattr(vmlogo_Variable, "name")
    descriptor = None
    for klass in vmlogo_Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_vmlogo_variable_has_value():
    assert hasattr(vmlogo_Variable, "value")
    descriptor = None
    for klass in vmlogo_Variable.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vmlogo_stackframe_is_not_abstract():
    assert not inspect.isabstract(vmlogo_StackFrame)


def test_vmlogo_stackframe_constructor_exists():
    assert callable(vmlogo_StackFrame.__init__)


def test_vmlogo_stackframe_constructor_args():
    sig = inspect.signature(vmlogo_StackFrame.__init__)
    params = list(sig.parameters.keys())



def test_vmlogo_callstack_is_not_abstract():
    assert not inspect.isabstract(vmlogo_CallStack)


def test_vmlogo_callstack_constructor_exists():
    assert callable(vmlogo_CallStack.__init__)


def test_vmlogo_callstack_constructor_args():
    sig = inspect.signature(vmlogo_CallStack.__init__)
    params = list(sig.parameters.keys())



def test_vmlogo_point_is_not_abstract():
    assert not inspect.isabstract(vmlogo_Point)


def test_vmlogo_point_constructor_exists():
    assert callable(vmlogo_Point.__init__)


def test_vmlogo_point_constructor_args():
    sig = inspect.signature(vmlogo_Point.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"

def test_vmlogo_point_has_y():
    assert hasattr(vmlogo_Point, "y")
    descriptor = None
    for klass in vmlogo_Point.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_vmlogo_point_has_x():
    assert hasattr(vmlogo_Point, "x")
    descriptor = None
    for klass in vmlogo_Point.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_vmlogo_turtle_is_not_abstract():
    assert not inspect.isabstract(vmlogo_Turtle)


def test_vmlogo_turtle_constructor_exists():
    assert callable(vmlogo_Turtle.__init__)


def test_vmlogo_turtle_constructor_args():
    sig = inspect.signature(vmlogo_Turtle.__init__)
    params = list(sig.parameters.keys())
    assert "heading" in params, "Missing parameter 'heading'"
    assert "penUp" in params, "Missing parameter 'penUp'"

def test_vmlogo_turtle_has_heading():
    assert hasattr(vmlogo_Turtle, "heading")
    descriptor = None
    for klass in vmlogo_Turtle.__mro__:
        if "heading" in klass.__dict__:
            descriptor = klass.__dict__["heading"]
            break
    assert isinstance(descriptor, property)

def test_vmlogo_turtle_has_penUp():
    assert hasattr(vmlogo_Turtle, "penUp")
    descriptor = None
    for klass in vmlogo_Turtle.__mro__:
        if "penUp" in klass.__dict__:
            descriptor = klass.__dict__["penUp"]
            break
    assert isinstance(descriptor, property)



def test_vmlogo_segment_is_not_abstract():
    assert not inspect.isabstract(vmlogo_Segment)


def test_vmlogo_segment_constructor_exists():
    assert callable(vmlogo_Segment.__init__)


def test_vmlogo_segment_constructor_args():
    sig = inspect.signature(vmlogo_Segment.__init__)
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
vmlogo_Variable_strategy = st.builds(
    vmlogo_Variable,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
vmlogo_StackFrame_strategy = st.builds(
    vmlogo_StackFrame,
)
vmlogo_CallStack_strategy = st.builds(
    vmlogo_CallStack,
)
vmlogo_Point_strategy = st.builds(
    vmlogo_Point,
    y=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
vmlogo_Turtle_strategy = st.builds(
    vmlogo_Turtle,
    heading=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    penUp=
        st.booleans()
)
vmlogo_Segment_strategy = st.builds(
    vmlogo_Segment,
)

@given(instance=vmlogo_Variable_strategy)
@settings(max_examples=50)
def test_vmlogo_variable_instantiation(instance):
    assert isinstance(instance, vmlogo_Variable)



@given(instance=vmlogo_Variable_strategy)
def test_vmlogo_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=vmlogo_Variable_strategy)
def test_vmlogo_variable_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vmlogo_StackFrame_strategy)
@settings(max_examples=50)
def test_vmlogo_stackframe_instantiation(instance):
    assert isinstance(instance, vmlogo_StackFrame)

@given(instance=vmlogo_CallStack_strategy)
@settings(max_examples=50)
def test_vmlogo_callstack_instantiation(instance):
    assert isinstance(instance, vmlogo_CallStack)

@given(instance=vmlogo_Point_strategy)
@settings(max_examples=50)
def test_vmlogo_point_instantiation(instance):
    assert isinstance(instance, vmlogo_Point)



@given(instance=vmlogo_Point_strategy)
def test_vmlogo_point_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=vmlogo_Point_strategy)
def test_vmlogo_point_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=vmlogo_Turtle_strategy)
@settings(max_examples=50)
def test_vmlogo_turtle_instantiation(instance):
    assert isinstance(instance, vmlogo_Turtle)



@given(instance=vmlogo_Turtle_strategy)
def test_vmlogo_turtle_heading_setter(instance):
    original = instance.heading
    instance.heading = original
    assert instance.heading == original



@given(instance=vmlogo_Turtle_strategy)
def test_vmlogo_turtle_penUp_setter(instance):
    original = instance.penUp
    instance.penUp = original
    assert instance.penUp == original

@given(instance=vmlogo_Segment_strategy)
@settings(max_examples=50)
def test_vmlogo_segment_instantiation(instance):
    assert isinstance(instance, vmlogo_Segment)
