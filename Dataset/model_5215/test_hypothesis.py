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
    emfdb_E,
    emfdb_D,
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
    assert "notUniqueValues" in params, "Missing parameter 'notUniqueValues'"
    assert "string" in params, "Missing parameter 'string'"
    assert "primitiveValues" in params, "Missing parameter 'primitiveValues'"
    assert "strings" in params, "Missing parameter 'strings'"

def test_emfdb_a_has_notUniqueValues():
    assert hasattr(emfdb_A, "notUniqueValues")
    descriptor = None
    for klass in emfdb_A.__mro__:
        if "notUniqueValues" in klass.__dict__:
            descriptor = klass.__dict__["notUniqueValues"]
            break
    assert isinstance(descriptor, property)

def test_emfdb_a_has_string():
    assert hasattr(emfdb_A, "string")
    descriptor = None
    for klass in emfdb_A.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)

def test_emfdb_a_has_primitiveValues():
    assert hasattr(emfdb_A, "primitiveValues")
    descriptor = None
    for klass in emfdb_A.__mro__:
        if "primitiveValues" in klass.__dict__:
            descriptor = klass.__dict__["primitiveValues"]
            break
    assert isinstance(descriptor, property)

def test_emfdb_a_has_strings():
    assert hasattr(emfdb_A, "strings")
    descriptor = None
    for klass in emfdb_A.__mro__:
        if "strings" in klass.__dict__:
            descriptor = klass.__dict__["strings"]
            break
    assert isinstance(descriptor, property)



def test_emfdb_e_is_not_abstract():
    assert not inspect.isabstract(emfdb_E)


def test_emfdb_e_constructor_exists():
    assert callable(emfdb_E.__init__)


def test_emfdb_e_constructor_args():
    sig = inspect.signature(emfdb_E.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_emfdb_e_has_name():
    assert hasattr(emfdb_E, "name")
    descriptor = None
    for klass in emfdb_E.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_emfdb_d_is_not_abstract():
    assert not inspect.isabstract(emfdb_D)


def test_emfdb_d_constructor_exists():
    assert callable(emfdb_D.__init__)


def test_emfdb_d_constructor_args():
    sig = inspect.signature(emfdb_D.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_emfdb_d_has_name():
    assert hasattr(emfdb_D, "name")
    descriptor = None
    for klass in emfdb_D.__mro__:
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
    notUniqueValues=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    string=
        safe_text,
    primitiveValues=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    strings=
        safe_text
)
emfdb_E_strategy = st.builds(
    emfdb_E,
    name=
        safe_text
)
emfdb_D_strategy = st.builds(
    emfdb_D,
    name=
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
def test_emfdb_a_notUniqueValues_setter(instance):
    original = instance.notUniqueValues
    instance.notUniqueValues = original
    assert instance.notUniqueValues == original



@given(instance=emfdb_A_strategy)
def test_emfdb_a_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original



@given(instance=emfdb_A_strategy)
def test_emfdb_a_primitiveValues_setter(instance):
    original = instance.primitiveValues
    instance.primitiveValues = original
    assert instance.primitiveValues == original



@given(instance=emfdb_A_strategy)
def test_emfdb_a_strings_setter(instance):
    original = instance.strings
    instance.strings = original
    assert instance.strings == original

@given(instance=emfdb_E_strategy)
@settings(max_examples=50)
def test_emfdb_e_instantiation(instance):
    assert isinstance(instance, emfdb_E)



@given(instance=emfdb_E_strategy)
def test_emfdb_e_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=emfdb_D_strategy)
@settings(max_examples=50)
def test_emfdb_d_instantiation(instance):
    assert isinstance(instance, emfdb_D)



@given(instance=emfdb_D_strategy)
def test_emfdb_d_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
