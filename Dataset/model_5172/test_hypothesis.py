import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    binDsl::B,
    binDsl::L,
    binDsl::N,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_bindsl::b_is_not_abstract():
    assert not inspect.isabstract(binDsl::B)


def test_bindsl::b_constructor_exists():
    assert callable(binDsl::B.__init__)


def test_bindsl::b_constructor_args():
    sig = inspect.signature(binDsl::B.__init__)
    params = list(sig.parameters.keys())
    assert "b" in params, "Missing parameter 'b'"

def test_bindsl::b_has_b():
    assert hasattr(binDsl::B, "b")
    descriptor = None
    for klass in binDsl::B.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)



def test_bindsl::l_is_not_abstract():
    assert not inspect.isabstract(binDsl::L)


def test_bindsl::l_constructor_exists():
    assert callable(binDsl::L.__init__)


def test_bindsl::l_constructor_args():
    sig = inspect.signature(binDsl::L.__init__)
    params = list(sig.parameters.keys())



def test_bindsl::n_is_not_abstract():
    assert not inspect.isabstract(binDsl::N)


def test_bindsl::n_constructor_exists():
    assert callable(binDsl::N.__init__)


def test_bindsl::n_constructor_args():
    sig = inspect.signature(binDsl::N.__init__)
    params = list(sig.parameters.keys())
    assert "cond" in params, "Missing parameter 'cond'"

def test_bindsl::n_has_cond():
    assert hasattr(binDsl::N, "cond")
    descriptor = None
    for klass in binDsl::N.__mro__:
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
binDsl::B_strategy = st.builds(
    binDsl::B,
    b=
        safe_text
)
binDsl::L_strategy = st.builds(
    binDsl::L,
)
binDsl::N_strategy = st.builds(
    binDsl::N,
    cond=
        st.booleans()
)

@given(instance=binDsl::B_strategy)
@settings(max_examples=50)
def test_bindsl::b_instantiation(instance):
    assert isinstance(instance, binDsl::B)

@given(instance=binDsl::B_strategy)
def test_bindsl::b_b_type(instance):
    assert isinstance(instance.b, str)


@given(instance=binDsl::B_strategy)
def test_bindsl::b_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original

@given(instance=binDsl::L_strategy)
@settings(max_examples=50)
def test_bindsl::l_instantiation(instance):
    assert isinstance(instance, binDsl::L)

@given(instance=binDsl::N_strategy)
@settings(max_examples=50)
def test_bindsl::n_instantiation(instance):
    assert isinstance(instance, binDsl::N)

@given(instance=binDsl::N_strategy)
def test_bindsl::n_cond_type(instance):
    assert isinstance(instance.cond, bool)


@given(instance=binDsl::N_strategy)
def test_bindsl::n_cond_setter(instance):
    original = instance.cond
    instance.cond = original
    assert instance.cond == original
