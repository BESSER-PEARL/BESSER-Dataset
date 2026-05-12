import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    fsm_State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsm_state_is_not_abstract():
    assert not inspect.isabstract(fsm_State)


def test_fsm_state_constructor_exists():
    assert callable(fsm_State.__init__)


def test_fsm_state_constructor_args():
    sig = inspect.signature(fsm_State.__init__)
    params = list(sig.parameters.keys())
    assert "foo" in params, "Missing parameter 'foo'"
    assert "c" in params, "Missing parameter 'c'"
    assert "l" in params, "Missing parameter 'l'"
    assert "d" in params, "Missing parameter 'd'"
    assert "b" in params, "Missing parameter 'b'"
    assert "f" in params, "Missing parameter 'f'"
    assert "i" in params, "Missing parameter 'i'"

def test_fsm_state_has_foo():
    assert hasattr(fsm_State, "foo")
    descriptor = None
    for klass in fsm_State.__mro__:
        if "foo" in klass.__dict__:
            descriptor = klass.__dict__["foo"]
            break
    assert isinstance(descriptor, property)

def test_fsm_state_has_c():
    assert hasattr(fsm_State, "c")
    descriptor = None
    for klass in fsm_State.__mro__:
        if "c" in klass.__dict__:
            descriptor = klass.__dict__["c"]
            break
    assert isinstance(descriptor, property)

def test_fsm_state_has_l():
    assert hasattr(fsm_State, "l")
    descriptor = None
    for klass in fsm_State.__mro__:
        if "l" in klass.__dict__:
            descriptor = klass.__dict__["l"]
            break
    assert isinstance(descriptor, property)

def test_fsm_state_has_d():
    assert hasattr(fsm_State, "d")
    descriptor = None
    for klass in fsm_State.__mro__:
        if "d" in klass.__dict__:
            descriptor = klass.__dict__["d"]
            break
    assert isinstance(descriptor, property)

def test_fsm_state_has_b():
    assert hasattr(fsm_State, "b")
    descriptor = None
    for klass in fsm_State.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)

def test_fsm_state_has_f():
    assert hasattr(fsm_State, "f")
    descriptor = None
    for klass in fsm_State.__mro__:
        if "f" in klass.__dict__:
            descriptor = klass.__dict__["f"]
            break
    assert isinstance(descriptor, property)

def test_fsm_state_has_i():
    assert hasattr(fsm_State, "i")
    descriptor = None
    for klass in fsm_State.__mro__:
        if "i" in klass.__dict__:
            descriptor = klass.__dict__["i"]
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
fsm_State_strategy = st.builds(
    fsm_State,
    foo=
        safe_text,
    c=
        safe_text,
    l=
        safe_text,
    d=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    b=
        st.booleans(),
    f=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    i=
        st.integers()
)

@given(instance=fsm_State_strategy)
@settings(max_examples=50)
def test_fsm_state_instantiation(instance):
    assert isinstance(instance, fsm_State)



@given(instance=fsm_State_strategy)
def test_fsm_state_foo_setter(instance):
    original = instance.foo
    instance.foo = original
    assert instance.foo == original



@given(instance=fsm_State_strategy)
def test_fsm_state_c_setter(instance):
    original = instance.c
    instance.c = original
    assert instance.c == original



@given(instance=fsm_State_strategy)
def test_fsm_state_l_setter(instance):
    original = instance.l
    instance.l = original
    assert instance.l == original



@given(instance=fsm_State_strategy)
def test_fsm_state_d_setter(instance):
    original = instance.d
    instance.d = original
    assert instance.d == original



@given(instance=fsm_State_strategy)
def test_fsm_state_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original



@given(instance=fsm_State_strategy)
def test_fsm_state_f_setter(instance):
    original = instance.f
    instance.f = original
    assert instance.f == original



@given(instance=fsm_State_strategy)
def test_fsm_state_i_setter(instance):
    original = instance.i
    instance.i = original
    assert instance.i == original
