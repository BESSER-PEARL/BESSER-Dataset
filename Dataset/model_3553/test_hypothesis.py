import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    testaccessors::EAcc,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_testaccessors::eacc_is_not_abstract():
    assert not inspect.isabstract(testaccessors::EAcc)


def test_testaccessors::eacc_constructor_exists():
    assert callable(testaccessors::EAcc.__init__)


def test_testaccessors::eacc_constructor_args():
    sig = inspect.signature(testaccessors::EAcc.__init__)
    params = list(sig.parameters.keys())
    assert "is_" in params, "Missing parameter 'is_'"
    assert "i" in params, "Missing parameter 'i'"
    assert "b" in params, "Missing parameter 'b'"
    assert "bs" in params, "Missing parameter 'bs'"

def test_testaccessors::eacc_has_is_():
    assert hasattr(testaccessors::EAcc, "is_")
    descriptor = None
    for klass in testaccessors::EAcc.__mro__:
        if "is_" in klass.__dict__:
            descriptor = klass.__dict__["is_"]
            break
    assert isinstance(descriptor, property)

def test_testaccessors::eacc_has_i():
    assert hasattr(testaccessors::EAcc, "i")
    descriptor = None
    for klass in testaccessors::EAcc.__mro__:
        if "i" in klass.__dict__:
            descriptor = klass.__dict__["i"]
            break
    assert isinstance(descriptor, property)

def test_testaccessors::eacc_has_b():
    assert hasattr(testaccessors::EAcc, "b")
    descriptor = None
    for klass in testaccessors::EAcc.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)

def test_testaccessors::eacc_has_bs():
    assert hasattr(testaccessors::EAcc, "bs")
    descriptor = None
    for klass in testaccessors::EAcc.__mro__:
        if "bs" in klass.__dict__:
            descriptor = klass.__dict__["bs"]
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
testaccessors::EAcc_strategy = st.builds(
    testaccessors::EAcc,
    is_=
        st.integers(),
    i=
        st.integers(),
    b=
        st.booleans(),
    bs=
        st.booleans()
)

@given(instance=testaccessors::EAcc_strategy)
@settings(max_examples=50)
def test_testaccessors::eacc_instantiation(instance):
    assert isinstance(instance, testaccessors::EAcc)

@given(instance=testaccessors::EAcc_strategy)
def test_testaccessors::eacc_is__type(instance):
    assert isinstance(instance.is_, int)


@given(instance=testaccessors::EAcc_strategy)
def test_testaccessors::eacc_is__setter(instance):
    original = instance.is_
    instance.is_ = original
    assert instance.is_ == original

@given(instance=testaccessors::EAcc_strategy)
def test_testaccessors::eacc_i_type(instance):
    assert isinstance(instance.i, int)


@given(instance=testaccessors::EAcc_strategy)
def test_testaccessors::eacc_i_setter(instance):
    original = instance.i
    instance.i = original
    assert instance.i == original

@given(instance=testaccessors::EAcc_strategy)
def test_testaccessors::eacc_b_type(instance):
    assert isinstance(instance.b, bool)


@given(instance=testaccessors::EAcc_strategy)
def test_testaccessors::eacc_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original

@given(instance=testaccessors::EAcc_strategy)
def test_testaccessors::eacc_bs_type(instance):
    assert isinstance(instance.bs, bool)


@given(instance=testaccessors::EAcc_strategy)
def test_testaccessors::eacc_bs_setter(instance):
    original = instance.bs
    instance.bs = original
    assert instance.bs == original
