import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    C3,
    C2,
    C1,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_c3_is_not_abstract():
    assert not inspect.isabstract(C3)


def test_c3_constructor_exists():
    assert callable(C3.__init__)


def test_c3_constructor_args():
    sig = inspect.signature(C3.__init__)
    params = list(sig.parameters.keys())
    assert "i3" in params, "Missing parameter 'i3'"

def test_c3_has_i3():
    assert hasattr(C3, "i3")
    descriptor = None
    for klass in C3.__mro__:
        if "i3" in klass.__dict__:
            descriptor = klass.__dict__["i3"]
            break
    assert isinstance(descriptor, property)



def test_c2_is_not_abstract():
    assert not inspect.isabstract(C2)


def test_c2_constructor_exists():
    assert callable(C2.__init__)


def test_c2_constructor_args():
    sig = inspect.signature(C2.__init__)
    params = list(sig.parameters.keys())
    assert "b1" in params, "Missing parameter 'b1'"

def test_c2_has_b1():
    assert hasattr(C2, "b1")
    descriptor = None
    for klass in C2.__mro__:
        if "b1" in klass.__dict__:
            descriptor = klass.__dict__["b1"]
            break
    assert isinstance(descriptor, property)



def test_c1_is_not_abstract():
    assert not inspect.isabstract(C1)


def test_c1_constructor_exists():
    assert callable(C1.__init__)


def test_c1_constructor_args():
    sig = inspect.signature(C1.__init__)
    params = list(sig.parameters.keys())
    assert "i3" in params, "Missing parameter 'i3'"

def test_c1_has_i3():
    assert hasattr(C1, "i3")
    descriptor = None
    for klass in C1.__mro__:
        if "i3" in klass.__dict__:
            descriptor = klass.__dict__["i3"]
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
C3_strategy = st.builds(
    C3,
    i3=
        st.integers()
)
C2_strategy = st.builds(
    C2,
    b1=
        st.booleans()
)
C1_strategy = st.builds(
    C1,
    i3=
        st.integers()
)

@given(instance=C3_strategy)
@settings(max_examples=50)
def test_c3_instantiation(instance):
    assert isinstance(instance, C3)



@given(instance=C3_strategy)
def test_c3_i3_setter(instance):
    original = instance.i3
    instance.i3 = original
    assert instance.i3 == original

@given(instance=C2_strategy)
@settings(max_examples=50)
def test_c2_instantiation(instance):
    assert isinstance(instance, C2)



@given(instance=C2_strategy)
def test_c2_b1_setter(instance):
    original = instance.b1
    instance.b1 = original
    assert instance.b1 == original

@given(instance=C1_strategy)
@settings(max_examples=50)
def test_c1_instantiation(instance):
    assert isinstance(instance, C1)



@given(instance=C1_strategy)
def test_c1_i3_setter(instance):
    original = instance.i3
    instance.i3 = original
    assert instance.i3 == original
