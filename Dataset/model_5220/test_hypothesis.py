import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    emfdb_C,
    emfdb_B,
    emfdb_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_emfdb_c_is_not_abstract():
    assert not inspect.isabstract(emfdb_C)


def test_emfdb_c_constructor_exists():
    assert callable(emfdb_C.__init__)


def test_emfdb_c_constructor_args():
    sig = inspect.signature(emfdb_C.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_emfdb_c_has_value():
    assert hasattr(emfdb_C, "value")
    descriptor = None
    for klass in emfdb_C.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_emfdb_c_has_key():
    assert hasattr(emfdb_C, "key")
    descriptor = None
    for klass in emfdb_C.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_emfdb_b_is_not_abstract():
    assert not inspect.isabstract(emfdb_B)


def test_emfdb_b_constructor_exists():
    assert callable(emfdb_B.__init__)


def test_emfdb_b_constructor_args():
    sig = inspect.signature(emfdb_B.__init__)
    params = list(sig.parameters.keys())
    assert "string" in params, "Missing parameter 'string'"

def test_emfdb_b_has_string():
    assert hasattr(emfdb_B, "string")
    descriptor = None
    for klass in emfdb_B.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)



def test_emfdb_a_is_not_abstract():
    assert not inspect.isabstract(emfdb_A)


def test_emfdb_a_constructor_exists():
    assert callable(emfdb_A.__init__)


def test_emfdb_a_constructor_args():
    sig = inspect.signature(emfdb_A.__init__)
    params = list(sig.parameters.keys())
    assert "string" in params, "Missing parameter 'string'"

def test_emfdb_a_has_string():
    assert hasattr(emfdb_A, "string")
    descriptor = None
    for klass in emfdb_A.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
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
emfdb_C_strategy = st.builds(
    emfdb_C,
    value=
        safe_text,
    key=
        safe_text
)
emfdb_B_strategy = st.builds(
    emfdb_B,
    string=
        safe_text
)
emfdb_A_strategy = st.builds(
    emfdb_A,
    string=
        safe_text
)

@given(instance=emfdb_C_strategy)
@settings(max_examples=50)
def test_emfdb_c_instantiation(instance):
    assert isinstance(instance, emfdb_C)



@given(instance=emfdb_C_strategy)
def test_emfdb_c_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=emfdb_C_strategy)
def test_emfdb_c_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=emfdb_B_strategy)
@settings(max_examples=50)
def test_emfdb_b_instantiation(instance):
    assert isinstance(instance, emfdb_B)



@given(instance=emfdb_B_strategy)
def test_emfdb_b_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original

@given(instance=emfdb_A_strategy)
@settings(max_examples=50)
def test_emfdb_a_instantiation(instance):
    assert isinstance(instance, emfdb_A)



@given(instance=emfdb_A_strategy)
def test_emfdb_a_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original
