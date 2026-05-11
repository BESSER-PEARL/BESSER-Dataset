import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    TypeA::B,
    TypeA::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_typea::b_is_not_abstract():
    assert not inspect.isabstract(TypeA::B)


def test_typea::b_constructor_exists():
    assert callable(TypeA::B.__init__)


def test_typea::b_constructor_args():
    sig = inspect.signature(TypeA::B.__init__)
    params = list(sig.parameters.keys())
    assert "nameB" in params, "Missing parameter 'nameB'"

def test_typea::b_has_nameB():
    assert hasattr(TypeA::B, "nameB")
    descriptor = None
    for klass in TypeA::B.__mro__:
        if "nameB" in klass.__dict__:
            descriptor = klass.__dict__["nameB"]
            break
    assert isinstance(descriptor, property)



def test_typea::a_is_not_abstract():
    assert not inspect.isabstract(TypeA::A)


def test_typea::a_constructor_exists():
    assert callable(TypeA::A.__init__)


def test_typea::a_constructor_args():
    sig = inspect.signature(TypeA::A.__init__)
    params = list(sig.parameters.keys())
    assert "nameA" in params, "Missing parameter 'nameA'"

def test_typea::a_has_nameA():
    assert hasattr(TypeA::A, "nameA")
    descriptor = None
    for klass in TypeA::A.__mro__:
        if "nameA" in klass.__dict__:
            descriptor = klass.__dict__["nameA"]
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
TypeA::B_strategy = st.builds(
    TypeA::B,
    nameB=
        safe_text
)
TypeA::A_strategy = st.builds(
    TypeA::A,
    nameA=
        safe_text
)

@given(instance=TypeA::B_strategy)
@settings(max_examples=50)
def test_typea::b_instantiation(instance):
    assert isinstance(instance, TypeA::B)

@given(instance=TypeA::B_strategy)
def test_typea::b_nameB_type(instance):
    assert isinstance(instance.nameB, str)


@given(instance=TypeA::B_strategy)
def test_typea::b_nameB_setter(instance):
    original = instance.nameB
    instance.nameB = original
    assert instance.nameB == original

@given(instance=TypeA::A_strategy)
@settings(max_examples=50)
def test_typea::a_instantiation(instance):
    assert isinstance(instance, TypeA::A)

@given(instance=TypeA::A_strategy)
def test_typea::a_nameA_type(instance):
    assert isinstance(instance.nameA, str)


@given(instance=TypeA::A_strategy)
def test_typea::a_nameA_setter(instance):
    original = instance.nameA
    instance.nameA = original
    assert instance.nameA == original
