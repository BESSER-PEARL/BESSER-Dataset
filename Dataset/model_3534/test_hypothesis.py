import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    testaccessors_EAcc,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_testaccessors_eacc_is_not_abstract():
    assert not inspect.isabstract(testaccessors_EAcc)


def test_testaccessors_eacc_constructor_exists():
    assert callable(testaccessors_EAcc.__init__)


def test_testaccessors_eacc_constructor_args():
    sig = inspect.signature(testaccessors_EAcc.__init__)
    params = list(sig.parameters.keys())
    assert "b" in params, "Missing parameter 'b'"
    assert "i" in params, "Missing parameter 'i'"
    assert "is_" in params, "Missing parameter 'is_'"
    assert "bs" in params, "Missing parameter 'bs'"

def test_testaccessors_eacc_has_b():
    assert hasattr(testaccessors_EAcc, "b")
    descriptor = None
    for klass in testaccessors_EAcc.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)

def test_testaccessors_eacc_has_i():
    assert hasattr(testaccessors_EAcc, "i")
    descriptor = None
    for klass in testaccessors_EAcc.__mro__:
        if "i" in klass.__dict__:
            descriptor = klass.__dict__["i"]
            break
    assert isinstance(descriptor, property)

def test_testaccessors_eacc_has_is_():
    assert hasattr(testaccessors_EAcc, "is_")
    descriptor = None
    for klass in testaccessors_EAcc.__mro__:
        if "is_" in klass.__dict__:
            descriptor = klass.__dict__["is_"]
            break
    assert isinstance(descriptor, property)

def test_testaccessors_eacc_has_bs():
    assert hasattr(testaccessors_EAcc, "bs")
    descriptor = None
    for klass in testaccessors_EAcc.__mro__:
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
testaccessors_EAcc_strategy = st.builds(
    testaccessors_EAcc,
    b=
        st.booleans(),
    i=
        st.integers(),
    is_=
        st.integers(),
    bs=
        st.booleans()
)

@given(instance=testaccessors_EAcc_strategy)
@settings(max_examples=50)
def test_testaccessors_eacc_instantiation(instance):
    assert isinstance(instance, testaccessors_EAcc)



@given(instance=testaccessors_EAcc_strategy)
def test_testaccessors_eacc_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original



@given(instance=testaccessors_EAcc_strategy)
def test_testaccessors_eacc_i_setter(instance):
    original = instance.i
    instance.i = original
    assert instance.i == original



@given(instance=testaccessors_EAcc_strategy)
def test_testaccessors_eacc_is__setter(instance):
    original = instance.is_
    instance.is_ = original
    assert instance.is_ == original



@given(instance=testaccessors_EAcc_strategy)
def test_testaccessors_eacc_bs_setter(instance):
    original = instance.bs
    instance.bs = original
    assert instance.bs == original
