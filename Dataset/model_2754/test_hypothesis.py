import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    PK461726_B461726,
    PK461726_A461726,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_pk461726_b461726_is_not_abstract():
    assert not inspect.isabstract(PK461726_B461726)


def test_pk461726_b461726_constructor_exists():
    assert callable(PK461726_B461726.__init__)


def test_pk461726_b461726_constructor_args():
    sig = inspect.signature(PK461726_B461726.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pk461726_b461726_has_name():
    assert hasattr(PK461726_B461726, "name")
    descriptor = None
    for klass in PK461726_B461726.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pk461726_a461726_is_not_abstract():
    assert not inspect.isabstract(PK461726_A461726)


def test_pk461726_a461726_constructor_exists():
    assert callable(PK461726_A461726.__init__)


def test_pk461726_a461726_constructor_args():
    sig = inspect.signature(PK461726_A461726.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pk461726_a461726_has_name():
    assert hasattr(PK461726_A461726, "name")
    descriptor = None
    for klass in PK461726_A461726.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
PK461726_B461726_strategy = st.builds(
    PK461726_B461726,
    name=
        safe_text
)
PK461726_A461726_strategy = st.builds(
    PK461726_A461726,
    name=
        safe_text
)

@given(instance=PK461726_B461726_strategy)
@settings(max_examples=50)
def test_pk461726_b461726_instantiation(instance):
    assert isinstance(instance, PK461726_B461726)



@given(instance=PK461726_B461726_strategy)
def test_pk461726_b461726_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PK461726_A461726_strategy)
@settings(max_examples=50)
def test_pk461726_a461726_instantiation(instance):
    assert isinstance(instance, PK461726_A461726)



@given(instance=PK461726_A461726_strategy)
def test_pk461726_a461726_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
