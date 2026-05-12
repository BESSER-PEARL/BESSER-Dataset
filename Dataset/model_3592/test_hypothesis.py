import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    TypeA_A,
    TypeA_B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_typea_a_is_not_abstract():
    assert not inspect.isabstract(TypeA_A)


def test_typea_a_constructor_exists():
    assert callable(TypeA_A.__init__)


def test_typea_a_constructor_args():
    sig = inspect.signature(TypeA_A.__init__)
    params = list(sig.parameters.keys())
    assert "nameA" in params, "Missing parameter 'nameA'"

def test_typea_a_has_nameA():
    assert hasattr(TypeA_A, "nameA")
    descriptor = None
    for klass in TypeA_A.__mro__:
        if "nameA" in klass.__dict__:
            descriptor = klass.__dict__["nameA"]
            break
    assert isinstance(descriptor, property)



def test_typea_b_is_not_abstract():
    assert not inspect.isabstract(TypeA_B)


def test_typea_b_constructor_exists():
    assert callable(TypeA_B.__init__)


def test_typea_b_constructor_args():
    sig = inspect.signature(TypeA_B.__init__)
    params = list(sig.parameters.keys())
    assert "nameB" in params, "Missing parameter 'nameB'"

def test_typea_b_has_nameB():
    assert hasattr(TypeA_B, "nameB")
    descriptor = None
    for klass in TypeA_B.__mro__:
        if "nameB" in klass.__dict__:
            descriptor = klass.__dict__["nameB"]
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
TypeA_A_strategy = st.builds(
    TypeA_A,
    nameA=
        safe_text
)
TypeA_B_strategy = st.builds(
    TypeA_B,
    nameB=
        safe_text
)

@given(instance=TypeA_A_strategy)
@settings(max_examples=50)
def test_typea_a_instantiation(instance):
    assert isinstance(instance, TypeA_A)



@given(instance=TypeA_A_strategy)
def test_typea_a_nameA_setter(instance):
    original = instance.nameA
    instance.nameA = original
    assert instance.nameA == original

@given(instance=TypeA_B_strategy)
@settings(max_examples=50)
def test_typea_b_instantiation(instance):
    assert isinstance(instance, TypeA_B)



@given(instance=TypeA_B_strategy)
def test_typea_b_nameB_setter(instance):
    original = instance.nameB
    instance.nameB = original
    assert instance.nameB == original
