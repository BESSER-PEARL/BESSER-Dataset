import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    binDsl_B,
    binDsl_L,
    binDsl_N,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_bindsl_b_is_not_abstract():
    assert not inspect.isabstract(binDsl_B)


def test_bindsl_b_constructor_exists():
    assert callable(binDsl_B.__init__)


def test_bindsl_b_constructor_args():
    sig = inspect.signature(binDsl_B.__init__)
    params = list(sig.parameters.keys())
    assert "b" in params, "Missing parameter 'b'"

def test_bindsl_b_has_b():
    assert hasattr(binDsl_B, "b")
    descriptor = None
    for klass in binDsl_B.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)



def test_bindsl_l_is_not_abstract():
    assert not inspect.isabstract(binDsl_L)


def test_bindsl_l_constructor_exists():
    assert callable(binDsl_L.__init__)


def test_bindsl_l_constructor_args():
    sig = inspect.signature(binDsl_L.__init__)
    params = list(sig.parameters.keys())



def test_bindsl_n_is_not_abstract():
    assert not inspect.isabstract(binDsl_N)


def test_bindsl_n_constructor_exists():
    assert callable(binDsl_N.__init__)


def test_bindsl_n_constructor_args():
    sig = inspect.signature(binDsl_N.__init__)
    params = list(sig.parameters.keys())
    assert "cond" in params, "Missing parameter 'cond'"

def test_bindsl_n_has_cond():
    assert hasattr(binDsl_N, "cond")
    descriptor = None
    for klass in binDsl_N.__mro__:
        if "cond" in klass.__dict__:
            descriptor = klass.__dict__["cond"]
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
binDsl_B_strategy = st.builds(
    binDsl_B,
    b=
        safe_text
)
binDsl_L_strategy = st.builds(
    binDsl_L,
)
binDsl_N_strategy = st.builds(
    binDsl_N,
    cond=
        st.booleans()
)

@given(instance=binDsl_B_strategy)
@settings(max_examples=50)
def test_bindsl_b_instantiation(instance):
    assert isinstance(instance, binDsl_B)



@given(instance=binDsl_B_strategy)
def test_bindsl_b_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original

@given(instance=binDsl_L_strategy)
@settings(max_examples=50)
def test_bindsl_l_instantiation(instance):
    assert isinstance(instance, binDsl_L)

@given(instance=binDsl_N_strategy)
@settings(max_examples=50)
def test_bindsl_n_instantiation(instance):
    assert isinstance(instance, binDsl_N)



@given(instance=binDsl_N_strategy)
def test_bindsl_n_cond_setter(instance):
    original = instance.cond
    instance.cond = original
    assert instance.cond == original
