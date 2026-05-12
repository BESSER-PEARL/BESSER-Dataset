import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    vmlogo_Segment,
    vmlogo_Point,
    vmlogo_CallStack,
    vmlogo_Turtle,
    vmlogo_StackFrame,
    vmlogo_Context,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_vmlogo_segment_is_not_abstract():
    assert not inspect.isabstract(vmlogo_Segment)


def test_vmlogo_segment_constructor_exists():
    assert callable(vmlogo_Segment.__init__)


def test_vmlogo_segment_constructor_args():
    sig = inspect.signature(vmlogo_Segment.__init__)
    params = list(sig.parameters.keys())



def test_vmlogo_point_is_not_abstract():
    assert not inspect.isabstract(vmlogo_Point)


def test_vmlogo_point_constructor_exists():
    assert callable(vmlogo_Point.__init__)


def test_vmlogo_point_constructor_args():
    sig = inspect.signature(vmlogo_Point.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_vmlogo_point_has_x():
    assert hasattr(vmlogo_Point, "x")
    descriptor = None
    for klass in vmlogo_Point.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_vmlogo_point_has_y():
    assert hasattr(vmlogo_Point, "y")
    descriptor = None
    for klass in vmlogo_Point.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_vmlogo_callstack_is_not_abstract():
    assert not inspect.isabstract(vmlogo_CallStack)


def test_vmlogo_callstack_constructor_exists():
    assert callable(vmlogo_CallStack.__init__)


def test_vmlogo_callstack_constructor_args():
    sig = inspect.signature(vmlogo_CallStack.__init__)
    params = list(sig.parameters.keys())



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



def test_vmlogo_stackframe_is_not_abstract():
    assert not inspect.isabstract(vmlogo_StackFrame)


def test_vmlogo_stackframe_constructor_exists():
    assert callable(vmlogo_StackFrame.__init__)


def test_vmlogo_stackframe_constructor_args():
    sig = inspect.signature(vmlogo_StackFrame.__init__)
    params = list(sig.parameters.keys())
    assert "variables" in params, "Missing parameter 'variables'"

def test_vmlogo_stackframe_has_variables():
    assert hasattr(vmlogo_StackFrame, "variables")
    descriptor = None
    for klass in vmlogo_StackFrame.__mro__:
        if "variables" in klass.__dict__:
            descriptor = klass.__dict__["variables"]
            break
    assert isinstance(descriptor, property)



def test_vmlogo_context_is_not_abstract():
    assert not inspect.isabstract(vmlogo_Context)


def test_vmlogo_context_constructor_exists():
    assert callable(vmlogo_Context.__init__)


def test_vmlogo_context_constructor_args():
    sig = inspect.signature(vmlogo_Context.__init__)
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
vmlogo_Segment_strategy = st.builds(
    vmlogo_Segment,
)
vmlogo_Point_strategy = st.builds(
    vmlogo_Point,
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    y=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
vmlogo_CallStack_strategy = st.builds(
    vmlogo_CallStack,
)
vmlogo_Turtle_strategy = st.builds(
    vmlogo_Turtle,
    heading=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    penUp=
        st.booleans()
)
vmlogo_StackFrame_strategy = st.builds(
    vmlogo_StackFrame,
    variables=
        safe_text
)
vmlogo_Context_strategy = st.builds(
    vmlogo_Context,
)

@given(instance=vmlogo_Segment_strategy)
@settings(max_examples=50)
def test_vmlogo_segment_instantiation(instance):
    assert isinstance(instance, vmlogo_Segment)

@given(instance=vmlogo_Point_strategy)
@settings(max_examples=50)
def test_vmlogo_point_instantiation(instance):
    assert isinstance(instance, vmlogo_Point)



@given(instance=vmlogo_Point_strategy)
def test_vmlogo_point_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=vmlogo_Point_strategy)
def test_vmlogo_point_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=vmlogo_CallStack_strategy)
@settings(max_examples=50)
def test_vmlogo_callstack_instantiation(instance):
    assert isinstance(instance, vmlogo_CallStack)

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

@given(instance=vmlogo_StackFrame_strategy)
@settings(max_examples=50)
def test_vmlogo_stackframe_instantiation(instance):
    assert isinstance(instance, vmlogo_StackFrame)



@given(instance=vmlogo_StackFrame_strategy)
def test_vmlogo_stackframe_variables_setter(instance):
    original = instance.variables
    instance.variables = original
    assert instance.variables == original

@given(instance=vmlogo_Context_strategy)
@settings(max_examples=50)
def test_vmlogo_context_instantiation(instance):
    assert isinstance(instance, vmlogo_Context)
