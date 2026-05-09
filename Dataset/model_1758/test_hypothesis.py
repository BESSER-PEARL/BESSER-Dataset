import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Sample::Library,
    Sample::EString,
    Sample::Person,
    Sample::Book,
    Category,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sample::library_is_not_abstract():
    assert not inspect.isabstract(Sample::Library)


def test_sample::library_constructor_exists():
    assert callable(Sample::Library.__init__)


def test_sample::library_constructor_args():
    sig = inspect.signature(Sample::Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sample::library_has_name():
    assert hasattr(Sample::Library, "name")
    descriptor = None
    for klass in Sample::Library.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sample::estring_is_not_abstract():
    assert not inspect.isabstract(Sample::EString)


def test_sample::estring_constructor_exists():
    assert callable(Sample::EString.__init__)


def test_sample::estring_constructor_args():
    sig = inspect.signature(Sample::EString.__init__)
    params = list(sig.parameters.keys())



def test_sample::person_is_not_abstract():
    assert not inspect.isabstract(Sample::Person)


def test_sample::person_constructor_exists():
    assert callable(Sample::Person.__init__)


def test_sample::person_constructor_args():
    sig = inspect.signature(Sample::Person.__init__)
    params = list(sig.parameters.keys())
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "lastName" in params, "Missing parameter 'lastName'"

def test_sample::person_has_firstName():
    assert hasattr(Sample::Person, "firstName")
    descriptor = None
    for klass in Sample::Person.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_sample::person_has_lastName():
    assert hasattr(Sample::Person, "lastName")
    descriptor = None
    for klass in Sample::Person.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)



def test_sample::book_is_not_abstract():
    assert not inspect.isabstract(Sample::Book)


def test_sample::book_constructor_exists():
    assert callable(Sample::Book.__init__)


def test_sample::book_constructor_args():
    sig = inspect.signature(Sample::Book.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "category" in params, "Missing parameter 'category'"

def test_sample::book_has_name():
    assert hasattr(Sample::Book, "name")
    descriptor = None
    for klass in Sample::Book.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sample::book_has_category():
    assert hasattr(Sample::Book, "category")
    descriptor = None
    for klass in Sample::Book.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_category_exists():
    # Check that the Enumeration exists
    assert Category is not None

def test_category_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Category]
    expected_literals = [
        "SF",
        "Polar",
        "Enfant",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Category"


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
Sample::Library_strategy = st.builds(
    Sample::Library,
    name=
        safe_text
)
Sample::EString_strategy = st.builds(
    Sample::EString,
)
Sample::Person_strategy = st.builds(
    Sample::Person,
    firstName=
        safe_text,
    lastName=
        safe_text
)
Sample::Book_strategy = st.builds(
    Sample::Book,
    name=
        safe_text,
    category=
        safe_text
)

@given(instance=Sample::Library_strategy)
@settings(max_examples=50)
def test_sample::library_instantiation(instance):
    assert isinstance(instance, Sample::Library)

@given(instance=Sample::Library_strategy)
def test_sample::library_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Sample::Library_strategy)
def test_sample::library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Sample::EString_strategy)
@settings(max_examples=50)
def test_sample::estring_instantiation(instance):
    assert isinstance(instance, Sample::EString)

@given(instance=Sample::Person_strategy)
@settings(max_examples=50)
def test_sample::person_instantiation(instance):
    assert isinstance(instance, Sample::Person)

@given(instance=Sample::Person_strategy)
def test_sample::person_firstName_type(instance):
    assert isinstance(instance.firstName, str)


@given(instance=Sample::Person_strategy)
def test_sample::person_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=Sample::Person_strategy)
def test_sample::person_lastName_type(instance):
    assert isinstance(instance.lastName, str)


@given(instance=Sample::Person_strategy)
def test_sample::person_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=Sample::Book_strategy)
@settings(max_examples=50)
def test_sample::book_instantiation(instance):
    assert isinstance(instance, Sample::Book)

@given(instance=Sample::Book_strategy)
def test_sample::book_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Sample::Book_strategy)
def test_sample::book_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Sample::Book_strategy)
def test_sample::book_category_type(instance):
    assert isinstance(instance.category, str)


@given(instance=Sample::Book_strategy)
def test_sample::book_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original
