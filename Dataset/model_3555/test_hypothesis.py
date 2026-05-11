import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    test1::ConceptA,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test1::concepta_is_not_abstract():
    assert not inspect.isabstract(test1::ConceptA)


def test_test1::concepta_constructor_exists():
    assert callable(test1::ConceptA.__init__)


def test_test1::concepta_constructor_args():
    sig = inspect.signature(test1::ConceptA.__init__)
    params = list(sig.parameters.keys())
    assert "bs" in params, "Missing parameter 'bs'"
    assert "b" in params, "Missing parameter 'b'"

def test_test1::concepta_has_bs():
    assert hasattr(test1::ConceptA, "bs")
    descriptor = None
    for klass in test1::ConceptA.__mro__:
        if "bs" in klass.__dict__:
            descriptor = klass.__dict__["bs"]
            break
    assert isinstance(descriptor, property)

def test_test1::concepta_has_b():
    assert hasattr(test1::ConceptA, "b")
    descriptor = None
    for klass in test1::ConceptA.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
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
test1::ConceptA_strategy = st.builds(
    test1::ConceptA,
    bs=
        safe_text,
    b=
        safe_text
)

@given(instance=test1::ConceptA_strategy)
@settings(max_examples=50)
def test_test1::concepta_instantiation(instance):
    assert isinstance(instance, test1::ConceptA)

@given(instance=test1::ConceptA_strategy)
def test_test1::concepta_bs_type(instance):
    assert isinstance(instance.bs, str)


@given(instance=test1::ConceptA_strategy)
def test_test1::concepta_bs_setter(instance):
    original = instance.bs
    instance.bs = original
    assert instance.bs == original

@given(instance=test1::ConceptA_strategy)
def test_test1::concepta_b_type(instance):
    assert isinstance(instance.b, str)


@given(instance=test1::ConceptA_strategy)
def test_test1::concepta_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original
