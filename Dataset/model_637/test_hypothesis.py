import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    lib_Cafeteria,
    lib_Person,
    lib_Address,
    lib_Book,
    lib_Library,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_lib_cafeteria_is_not_abstract():
    assert not inspect.isabstract(lib_Cafeteria)


def test_lib_cafeteria_constructor_exists():
    assert callable(lib_Cafeteria.__init__)


def test_lib_cafeteria_constructor_args():
    sig = inspect.signature(lib_Cafeteria.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_lib_cafeteria_has_name():
    assert hasattr(lib_Cafeteria, "name")
    descriptor = None
    for klass in lib_Cafeteria.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_lib_person_is_not_abstract():
    assert not inspect.isabstract(lib_Person)


def test_lib_person_constructor_exists():
    assert callable(lib_Person.__init__)


def test_lib_person_constructor_args():
    sig = inspect.signature(lib_Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_lib_person_has_name():
    assert hasattr(lib_Person, "name")
    descriptor = None
    for klass in lib_Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_lib_address_is_not_abstract():
    assert not inspect.isabstract(lib_Address)


def test_lib_address_constructor_exists():
    assert callable(lib_Address.__init__)


def test_lib_address_constructor_args():
    sig = inspect.signature(lib_Address.__init__)
    params = list(sig.parameters.keys())
    assert "postalCode" in params, "Missing parameter 'postalCode'"

def test_lib_address_has_postalCode():
    assert hasattr(lib_Address, "postalCode")
    descriptor = None
    for klass in lib_Address.__mro__:
        if "postalCode" in klass.__dict__:
            descriptor = klass.__dict__["postalCode"]
            break
    assert isinstance(descriptor, property)



def test_lib_book_is_not_abstract():
    assert not inspect.isabstract(lib_Book)


def test_lib_book_constructor_exists():
    assert callable(lib_Book.__init__)


def test_lib_book_constructor_args():
    sig = inspect.signature(lib_Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_lib_book_has_title():
    assert hasattr(lib_Book, "title")
    descriptor = None
    for klass in lib_Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_lib_library_is_not_abstract():
    assert not inspect.isabstract(lib_Library)


def test_lib_library_constructor_exists():
    assert callable(lib_Library.__init__)


def test_lib_library_constructor_args():
    sig = inspect.signature(lib_Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_lib_library_has_name():
    assert hasattr(lib_Library, "name")
    descriptor = None
    for klass in lib_Library.__mro__:
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
lib_Cafeteria_strategy = st.builds(
    lib_Cafeteria,
    name=
        safe_text
)
lib_Person_strategy = st.builds(
    lib_Person,
    name=
        safe_text
)
lib_Address_strategy = st.builds(
    lib_Address,
    postalCode=
        safe_text
)
lib_Book_strategy = st.builds(
    lib_Book,
    title=
        safe_text
)
lib_Library_strategy = st.builds(
    lib_Library,
    name=
        safe_text
)

@given(instance=lib_Cafeteria_strategy)
@settings(max_examples=50)
def test_lib_cafeteria_instantiation(instance):
    assert isinstance(instance, lib_Cafeteria)



@given(instance=lib_Cafeteria_strategy)
def test_lib_cafeteria_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=lib_Person_strategy)
@settings(max_examples=50)
def test_lib_person_instantiation(instance):
    assert isinstance(instance, lib_Person)



@given(instance=lib_Person_strategy)
def test_lib_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=lib_Address_strategy)
@settings(max_examples=50)
def test_lib_address_instantiation(instance):
    assert isinstance(instance, lib_Address)



@given(instance=lib_Address_strategy)
def test_lib_address_postalCode_setter(instance):
    original = instance.postalCode
    instance.postalCode = original
    assert instance.postalCode == original

@given(instance=lib_Book_strategy)
@settings(max_examples=50)
def test_lib_book_instantiation(instance):
    assert isinstance(instance, lib_Book)



@given(instance=lib_Book_strategy)
def test_lib_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=lib_Library_strategy)
@settings(max_examples=50)
def test_lib_library_instantiation(instance):
    assert isinstance(instance, lib_Library)



@given(instance=lib_Library_strategy)
def test_lib_library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
