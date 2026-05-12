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
    S,
    I_Interface,
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
    assert "K" in params, "Missing parameter 'K'"

def test_c3_has_K():
    assert hasattr(C3, "K")
    descriptor = None
    for klass in C3.__mro__:
        if "K" in klass.__dict__:
            descriptor = klass.__dict__["K"]
            break
    assert isinstance(descriptor, property)



def test_c2_is_not_abstract():
    assert not inspect.isabstract(C2)


def test_c2_constructor_exists():
    assert callable(C2.__init__)


def test_c2_constructor_args():
    sig = inspect.signature(C2.__init__)
    params = list(sig.parameters.keys())



def test_c1_is_not_abstract():
    assert not inspect.isabstract(C1)


def test_c1_constructor_exists():
    assert callable(C1.__init__)


def test_c1_constructor_args():
    sig = inspect.signature(C1.__init__)
    params = list(sig.parameters.keys())
    assert "b" in params, "Missing parameter 'b'"

def test_c1_has_b():
    assert hasattr(C1, "b")
    descriptor = None
    for klass in C1.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)



def test_s_is_not_abstract():
    assert not inspect.isabstract(S)


def test_s_constructor_exists():
    assert callable(S.__init__)


def test_s_constructor_args():
    sig = inspect.signature(S.__init__)
    params = list(sig.parameters.keys())
    assert "v1" in params, "Missing parameter 'v1'"

def test_s_has_v1():
    assert hasattr(S, "v1")
    descriptor = None
    for klass in S.__mro__:
        if "v1" in klass.__dict__:
            descriptor = klass.__dict__["v1"]
            break
    assert isinstance(descriptor, property)



def test_i_interface_is_not_abstract():
    assert not inspect.isabstract(I_Interface)


def test_i_interface_constructor_exists():
    assert callable(I_Interface.__init__)


def test_i_interface_constructor_args():
    sig = inspect.signature(I_Interface.__init__)
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
C3_strategy = st.builds(
    C3,
    K=
        st.integers()
)
C2_strategy = st.builds(
    C2,
)
C1_strategy = st.builds(
    C1,
    b=
        safe_text
)
S_strategy = st.builds(
    S,
    v1=
        safe_text
)
I_Interface_strategy = st.builds(
    I_Interface,
)

@given(instance=C3_strategy)
@settings(max_examples=50)
def test_c3_instantiation(instance):
    assert isinstance(instance, C3)



@given(instance=C3_strategy)
def test_c3_K_setter(instance):
    original = instance.K
    instance.K = original
    assert instance.K == original

@given(instance=C2_strategy)
@settings(max_examples=50)
def test_c2_instantiation(instance):
    assert isinstance(instance, C2)

@given(instance=C1_strategy)
@settings(max_examples=50)
def test_c1_instantiation(instance):
    assert isinstance(instance, C1)



@given(instance=C1_strategy)
def test_c1_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original

@given(instance=S_strategy)
@settings(max_examples=50)
def test_s_instantiation(instance):
    assert isinstance(instance, S)



@given(instance=S_strategy)
def test_s_v1_setter(instance):
    original = instance.v1
    instance.v1 = original
    assert instance.v1 == original

@given(instance=I_Interface_strategy)
@settings(max_examples=50)
def test_i_interface_instantiation(instance):
    assert isinstance(instance, I_Interface)
