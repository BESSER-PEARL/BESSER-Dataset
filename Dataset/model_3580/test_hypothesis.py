import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    TypeA::PortA,
    TypeA::BlockA,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_typea::porta_is_not_abstract():
    assert not inspect.isabstract(TypeA::PortA)


def test_typea::porta_constructor_exists():
    assert callable(TypeA::PortA.__init__)


def test_typea::porta_constructor_args():
    sig = inspect.signature(TypeA::PortA.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_typea::porta_has_name():
    assert hasattr(TypeA::PortA, "name")
    descriptor = None
    for klass in TypeA::PortA.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_typea::blocka_is_not_abstract():
    assert not inspect.isabstract(TypeA::BlockA)


def test_typea::blocka_constructor_exists():
    assert callable(TypeA::BlockA.__init__)


def test_typea::blocka_constructor_args():
    sig = inspect.signature(TypeA::BlockA.__init__)
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
TypeA::PortA_strategy = st.builds(
    TypeA::PortA,
    name=
        safe_text
)
TypeA::BlockA_strategy = st.builds(
    TypeA::BlockA,
)

@given(instance=TypeA::PortA_strategy)
@settings(max_examples=50)
def test_typea::porta_instantiation(instance):
    assert isinstance(instance, TypeA::PortA)

@given(instance=TypeA::PortA_strategy)
def test_typea::porta_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=TypeA::PortA_strategy)
def test_typea::porta_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TypeA::BlockA_strategy)
@settings(max_examples=50)
def test_typea::blocka_instantiation(instance):
    assert isinstance(instance, TypeA::BlockA)
