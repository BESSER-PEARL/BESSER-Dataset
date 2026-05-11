import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    fsm::State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsm::state_is_not_abstract():
    assert not inspect.isabstract(fsm::State)


def test_fsm::state_constructor_exists():
    assert callable(fsm::State.__init__)


def test_fsm::state_constructor_args():
    sig = inspect.signature(fsm::State.__init__)
    params = list(sig.parameters.keys())
    assert "c" in params, "Missing parameter 'c'"
    assert "i" in params, "Missing parameter 'i'"
    assert "l" in params, "Missing parameter 'l'"
    assert "b" in params, "Missing parameter 'b'"
    assert "foo" in params, "Missing parameter 'foo'"
    assert "f" in params, "Missing parameter 'f'"
    assert "d" in params, "Missing parameter 'd'"

def test_fsm::state_has_c():
    assert hasattr(fsm::State, "c")
    descriptor = None
    for klass in fsm::State.__mro__:
        if "c" in klass.__dict__:
            descriptor = klass.__dict__["c"]
            break
    assert isinstance(descriptor, property)

def test_fsm::state_has_i():
    assert hasattr(fsm::State, "i")
    descriptor = None
    for klass in fsm::State.__mro__:
        if "i" in klass.__dict__:
            descriptor = klass.__dict__["i"]
            break
    assert isinstance(descriptor, property)

def test_fsm::state_has_l():
    assert hasattr(fsm::State, "l")
    descriptor = None
    for klass in fsm::State.__mro__:
        if "l" in klass.__dict__:
            descriptor = klass.__dict__["l"]
            break
    assert isinstance(descriptor, property)

def test_fsm::state_has_b():
    assert hasattr(fsm::State, "b")
    descriptor = None
    for klass in fsm::State.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)

def test_fsm::state_has_foo():
    assert hasattr(fsm::State, "foo")
    descriptor = None
    for klass in fsm::State.__mro__:
        if "foo" in klass.__dict__:
            descriptor = klass.__dict__["foo"]
            break
    assert isinstance(descriptor, property)

def test_fsm::state_has_f():
    assert hasattr(fsm::State, "f")
    descriptor = None
    for klass in fsm::State.__mro__:
        if "f" in klass.__dict__:
            descriptor = klass.__dict__["f"]
            break
    assert isinstance(descriptor, property)

def test_fsm::state_has_d():
    assert hasattr(fsm::State, "d")
    descriptor = None
    for klass in fsm::State.__mro__:
        if "d" in klass.__dict__:
            descriptor = klass.__dict__["d"]
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
fsm::State_strategy = st.builds(
    fsm::State,
    c=
        safe_text,
    i=
        st.integers(),
    l=
        safe_text,
    b=
        st.booleans(),
    foo=
        safe_text,
    f=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    d=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

@given(instance=fsm::State_strategy)
@settings(max_examples=50)
def test_fsm::state_instantiation(instance):
    assert isinstance(instance, fsm::State)

@given(instance=fsm::State_strategy)
def test_fsm::state_c_type(instance):
    assert isinstance(instance.c, str)


@given(instance=fsm::State_strategy)
def test_fsm::state_c_setter(instance):
    original = instance.c
    instance.c = original
    assert instance.c == original

@given(instance=fsm::State_strategy)
def test_fsm::state_i_type(instance):
    assert isinstance(instance.i, int)


@given(instance=fsm::State_strategy)
def test_fsm::state_i_setter(instance):
    original = instance.i
    instance.i = original
    assert instance.i == original

@given(instance=fsm::State_strategy)
def test_fsm::state_l_type(instance):
    assert isinstance(instance.l, str)


@given(instance=fsm::State_strategy)
def test_fsm::state_l_setter(instance):
    original = instance.l
    instance.l = original
    assert instance.l == original

@given(instance=fsm::State_strategy)
def test_fsm::state_b_type(instance):
    assert isinstance(instance.b, bool)


@given(instance=fsm::State_strategy)
def test_fsm::state_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original

@given(instance=fsm::State_strategy)
def test_fsm::state_foo_type(instance):
    assert isinstance(instance.foo, str)


@given(instance=fsm::State_strategy)
def test_fsm::state_foo_setter(instance):
    original = instance.foo
    instance.foo = original
    assert instance.foo == original

@given(instance=fsm::State_strategy)
def test_fsm::state_f_type(instance):
    assert isinstance(instance.f, float)


@given(instance=fsm::State_strategy)
def test_fsm::state_f_setter(instance):
    original = instance.f
    instance.f = original
    assert instance.f == original

@given(instance=fsm::State_strategy)
def test_fsm::state_d_type(instance):
    assert isinstance(instance.d, float)


@given(instance=fsm::State_strategy)
def test_fsm::state_d_setter(instance):
    original = instance.d
    instance.d = original
    assert instance.d == original
