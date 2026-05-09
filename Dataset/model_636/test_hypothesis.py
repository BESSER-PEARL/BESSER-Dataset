import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    lib::Address,
    lib::Book,
    lib::Library,
    lib::Cafeteria,
    lib::Person,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_lib::address_is_not_abstract():
    assert not inspect.isabstract(lib::Address)


def test_lib::address_constructor_exists():
    assert callable(lib::Address.__init__)


def test_lib::address_constructor_args():
    sig = inspect.signature(lib::Address.__init__)
    params = list(sig.parameters.keys())
    assert "postalCode" in params, "Missing parameter 'postalCode'"

def test_lib::address_has_postalCode():
    assert hasattr(lib::Address, "postalCode")
    descriptor = None
    for klass in lib::Address.__mro__:
        if "postalCode" in klass.__dict__:
            descriptor = klass.__dict__["postalCode"]
            break
    assert isinstance(descriptor, property)



def test_lib::book_is_not_abstract():
    assert not inspect.isabstract(lib::Book)


def test_lib::book_constructor_exists():
    assert callable(lib::Book.__init__)


def test_lib::book_constructor_args():
    sig = inspect.signature(lib::Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_lib::book_has_title():
    assert hasattr(lib::Book, "title")
    descriptor = None
    for klass in lib::Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_lib::library_is_not_abstract():
    assert not inspect.isabstract(lib::Library)


def test_lib::library_constructor_exists():
    assert callable(lib::Library.__init__)


def test_lib::library_constructor_args():
    sig = inspect.signature(lib::Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_lib::library_has_name():
    assert hasattr(lib::Library, "name")
    descriptor = None
    for klass in lib::Library.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_lib::cafeteria_is_not_abstract():
    assert not inspect.isabstract(lib::Cafeteria)


def test_lib::cafeteria_constructor_exists():
    assert callable(lib::Cafeteria.__init__)


def test_lib::cafeteria_constructor_args():
    sig = inspect.signature(lib::Cafeteria.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_lib::cafeteria_has_name():
    assert hasattr(lib::Cafeteria, "name")
    descriptor = None
    for klass in lib::Cafeteria.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_lib::person_is_not_abstract():
    assert not inspect.isabstract(lib::Person)


def test_lib::person_constructor_exists():
    assert callable(lib::Person.__init__)


def test_lib::person_constructor_args():
    sig = inspect.signature(lib::Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_lib::person_has_name():
    assert hasattr(lib::Person, "name")
    descriptor = None
    for klass in lib::Person.__mro__:
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
lib::Address_strategy = st.builds(
    lib::Address,
    postalCode=
        safe_text
)
lib::Book_strategy = st.builds(
    lib::Book,
    title=
        safe_text
)
lib::Library_strategy = st.builds(
    lib::Library,
    name=
        safe_text
)
lib::Cafeteria_strategy = st.builds(
    lib::Cafeteria,
    name=
        safe_text
)
lib::Person_strategy = st.builds(
    lib::Person,
    name=
        safe_text
)

@given(instance=lib::Address_strategy)
@settings(max_examples=50)
def test_lib::address_instantiation(instance):
    assert isinstance(instance, lib::Address)

@given(instance=lib::Address_strategy)
def test_lib::address_postalCode_type(instance):
    assert isinstance(instance.postalCode, str)


@given(instance=lib::Address_strategy)
def test_lib::address_postalCode_setter(instance):
    original = instance.postalCode
    instance.postalCode = original
    assert instance.postalCode == original

@given(instance=lib::Book_strategy)
@settings(max_examples=50)
def test_lib::book_instantiation(instance):
    assert isinstance(instance, lib::Book)

@given(instance=lib::Book_strategy)
def test_lib::book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=lib::Book_strategy)
def test_lib::book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=lib::Library_strategy)
@settings(max_examples=50)
def test_lib::library_instantiation(instance):
    assert isinstance(instance, lib::Library)

@given(instance=lib::Library_strategy)
def test_lib::library_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=lib::Library_strategy)
def test_lib::library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=lib::Cafeteria_strategy)
@settings(max_examples=50)
def test_lib::cafeteria_instantiation(instance):
    assert isinstance(instance, lib::Cafeteria)

@given(instance=lib::Cafeteria_strategy)
def test_lib::cafeteria_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=lib::Cafeteria_strategy)
def test_lib::cafeteria_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=lib::Person_strategy)
@settings(max_examples=50)
def test_lib::person_instantiation(instance):
    assert isinstance(instance, lib::Person)

@given(instance=lib::Person_strategy)
def test_lib::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=lib::Person_strategy)
def test_lib::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
