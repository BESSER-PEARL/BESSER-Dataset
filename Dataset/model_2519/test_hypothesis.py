import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ext_F,
    E,
    ext_ExtE,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ext_f_is_not_abstract():
    assert not inspect.isabstract(ext_F)


def test_ext_f_constructor_exists():
    assert callable(ext_F.__init__)


def test_ext_f_constructor_args():
    sig = inspect.signature(ext_F.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_ext_f_has_id():
    assert hasattr(ext_F, "id")
    descriptor = None
    for klass in ext_F.__mro__:
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



def test_ext_exte_is_not_abstract():
    assert not inspect.isabstract(ext_ExtE)


def test_ext_exte_constructor_exists():
    assert callable(ext_ExtE.__init__)


def test_ext_exte_constructor_args():
    sig = inspect.signature(ext_ExtE.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ext_exte_has_value():
    assert hasattr(ext_ExtE, "value")
    descriptor = None
    for klass in ext_ExtE.__mro__:
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
ext_F_strategy = st.builds(
    ext_F,
    id=
        safe_text
)
E_strategy = st.builds(
    E,
)
ext_ExtE_strategy = st.builds(
    ext_ExtE,
    value=
        st.integers()
)

@given(instance=ext_F_strategy)
@settings(max_examples=50)
def test_ext_f_instantiation(instance):
    assert isinstance(instance, ext_F)



@given(instance=ext_F_strategy)
def test_ext_f_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=E_strategy)
@settings(max_examples=50)
def test_e_instantiation(instance):
    assert isinstance(instance, E)

@given(instance=ext_ExtE_strategy)
@settings(max_examples=50)
def test_ext_exte_instantiation(instance):
    assert isinstance(instance, ext_ExtE)



@given(instance=ext_ExtE_strategy)
def test_ext_exte_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original
