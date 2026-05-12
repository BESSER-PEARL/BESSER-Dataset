import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    TypeA_PortA,
    TypeA_BlockA,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_typea_porta_is_not_abstract():
    assert not inspect.isabstract(TypeA_PortA)


def test_typea_porta_constructor_exists():
    assert callable(TypeA_PortA.__init__)


def test_typea_porta_constructor_args():
    sig = inspect.signature(TypeA_PortA.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_typea_porta_has_name():
    assert hasattr(TypeA_PortA, "name")
    descriptor = None
    for klass in TypeA_PortA.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_typea_blocka_is_not_abstract():
    assert not inspect.isabstract(TypeA_BlockA)


def test_typea_blocka_constructor_exists():
    assert callable(TypeA_BlockA.__init__)


def test_typea_blocka_constructor_args():
    sig = inspect.signature(TypeA_BlockA.__init__)
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
TypeA_PortA_strategy = st.builds(
    TypeA_PortA,
    name=
        safe_text
)
TypeA_BlockA_strategy = st.builds(
    TypeA_BlockA,
)

@given(instance=TypeA_PortA_strategy)
@settings(max_examples=50)
def test_typea_porta_instantiation(instance):
    assert isinstance(instance, TypeA_PortA)



@given(instance=TypeA_PortA_strategy)
def test_typea_porta_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TypeA_BlockA_strategy)
@settings(max_examples=50)
def test_typea_blocka_instantiation(instance):
    assert isinstance(instance, TypeA_BlockA)
