import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    emfdb::B,
    emfdb::A,
    emfdb::C,
    emfdb::E,
    emfdb::D,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_emfdb::b_is_not_abstract():
    assert not inspect.isabstract(emfdb::B)


def test_emfdb::b_constructor_exists():
    assert callable(emfdb::B.__init__)


def test_emfdb::b_constructor_args():
    sig = inspect.signature(emfdb::B.__init__)
    params = list(sig.parameters.keys())
    assert "string" in params, "Missing parameter 'string'"

def test_emfdb::b_has_string():
    assert hasattr(emfdb::B, "string")
    descriptor = None
    for klass in emfdb::B.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)



def test_emfdb::a_is_not_abstract():
    assert not inspect.isabstract(emfdb::A)


def test_emfdb::a_constructor_exists():
    assert callable(emfdb::A.__init__)


def test_emfdb::a_constructor_args():
    sig = inspect.signature(emfdb::A.__init__)
    params = list(sig.parameters.keys())
    assert "string" in params, "Missing parameter 'string'"

def test_emfdb::a_has_string():
    assert hasattr(emfdb::A, "string")
    descriptor = None
    for klass in emfdb::A.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)



def test_emfdb::c_is_not_abstract():
    assert not inspect.isabstract(emfdb::C)


def test_emfdb::c_constructor_exists():
    assert callable(emfdb::C.__init__)


def test_emfdb::c_constructor_args():
    sig = inspect.signature(emfdb::C.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_emfdb::c_has_value():
    assert hasattr(emfdb::C, "value")
    descriptor = None
    for klass in emfdb::C.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_emfdb::c_has_key():
    assert hasattr(emfdb::C, "key")
    descriptor = None
    for klass in emfdb::C.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_emfdb::e_is_not_abstract():
    assert not inspect.isabstract(emfdb::E)


def test_emfdb::e_constructor_exists():
    assert callable(emfdb::E.__init__)


def test_emfdb::e_constructor_args():
    sig = inspect.signature(emfdb::E.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_emfdb::e_has_name():
    assert hasattr(emfdb::E, "name")
    descriptor = None
    for klass in emfdb::E.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_emfdb::d_is_not_abstract():
    assert not inspect.isabstract(emfdb::D)


def test_emfdb::d_constructor_exists():
    assert callable(emfdb::D.__init__)


def test_emfdb::d_constructor_args():
    sig = inspect.signature(emfdb::D.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_emfdb::d_has_name():
    assert hasattr(emfdb::D, "name")
    descriptor = None
    for klass in emfdb::D.__mro__:
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
emfdb::B_strategy = st.builds(
    emfdb::B,
    string=
        safe_text
)
emfdb::A_strategy = st.builds(
    emfdb::A,
    string=
        safe_text
)
emfdb::C_strategy = st.builds(
    emfdb::C,
    value=
        safe_text,
    key=
        safe_text
)
emfdb::E_strategy = st.builds(
    emfdb::E,
    name=
        safe_text
)
emfdb::D_strategy = st.builds(
    emfdb::D,
    name=
        safe_text
)

@given(instance=emfdb::B_strategy)
@settings(max_examples=50)
def test_emfdb::b_instantiation(instance):
    assert isinstance(instance, emfdb::B)

@given(instance=emfdb::B_strategy)
def test_emfdb::b_string_type(instance):
    assert isinstance(instance.string, str)


@given(instance=emfdb::B_strategy)
def test_emfdb::b_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original

@given(instance=emfdb::A_strategy)
@settings(max_examples=50)
def test_emfdb::a_instantiation(instance):
    assert isinstance(instance, emfdb::A)

@given(instance=emfdb::A_strategy)
def test_emfdb::a_string_type(instance):
    assert isinstance(instance.string, str)


@given(instance=emfdb::A_strategy)
def test_emfdb::a_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original

@given(instance=emfdb::C_strategy)
@settings(max_examples=50)
def test_emfdb::c_instantiation(instance):
    assert isinstance(instance, emfdb::C)

@given(instance=emfdb::C_strategy)
def test_emfdb::c_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=emfdb::C_strategy)
def test_emfdb::c_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=emfdb::C_strategy)
def test_emfdb::c_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=emfdb::C_strategy)
def test_emfdb::c_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=emfdb::E_strategy)
@settings(max_examples=50)
def test_emfdb::e_instantiation(instance):
    assert isinstance(instance, emfdb::E)

@given(instance=emfdb::E_strategy)
def test_emfdb::e_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=emfdb::E_strategy)
def test_emfdb::e_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=emfdb::D_strategy)
@settings(max_examples=50)
def test_emfdb::d_instantiation(instance):
    assert isinstance(instance, emfdb::D)

@given(instance=emfdb::D_strategy)
def test_emfdb::d_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=emfdb::D_strategy)
def test_emfdb::d_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
