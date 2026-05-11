import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ext::F,
    E,
    ext::ExtE,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ext::f_is_not_abstract():
    assert not inspect.isabstract(ext::F)


def test_ext::f_constructor_exists():
    assert callable(ext::F.__init__)


def test_ext::f_constructor_args():
    sig = inspect.signature(ext::F.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_ext::f_has_id():
    assert hasattr(ext::F, "id")
    descriptor = None
    for klass in ext::F.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_e_is_not_abstract():
    assert not inspect.isabstract(E)


def test_e_constructor_exists():
    assert callable(E.__init__)


def test_e_constructor_args():
    sig = inspect.signature(E.__init__)
    params = list(sig.parameters.keys())



def test_ext::exte_is_not_abstract():
    assert not inspect.isabstract(ext::ExtE)


def test_ext::exte_constructor_exists():
    assert callable(ext::ExtE.__init__)


def test_ext::exte_constructor_args():
    sig = inspect.signature(ext::ExtE.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ext::exte_has_value():
    assert hasattr(ext::ExtE, "value")
    descriptor = None
    for klass in ext::ExtE.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
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
ext::F_strategy = st.builds(
    ext::F,
    id=
        safe_text
)
E_strategy = st.builds(
    E,
)
ext::ExtE_strategy = st.builds(
    ext::ExtE,
    value=
        st.integers()
)

@given(instance=ext::F_strategy)
@settings(max_examples=50)
def test_ext::f_instantiation(instance):
    assert isinstance(instance, ext::F)

@given(instance=ext::F_strategy)
def test_ext::f_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=ext::F_strategy)
def test_ext::f_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=E_strategy)
@settings(max_examples=50)
def test_e_instantiation(instance):
    assert isinstance(instance, E)

@given(instance=ext::ExtE_strategy)
@settings(max_examples=50)
def test_ext::exte_instantiation(instance):
    assert isinstance(instance, ext::ExtE)

@given(instance=ext::ExtE_strategy)
def test_ext::exte_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=ext::ExtE_strategy)
def test_ext::exte_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original
