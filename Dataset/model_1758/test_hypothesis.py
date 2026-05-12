import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Sample_Library,
    Sample_EString,
    Sample_Person,
    Sample_Book,
    Category,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sample_library_is_not_abstract():
    assert not inspect.isabstract(Sample_Library)


def test_sample_library_constructor_exists():
    assert callable(Sample_Library.__init__)


def test_sample_library_constructor_args():
    sig = inspect.signature(Sample_Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sample_library_has_name():
    assert hasattr(Sample_Library, "name")
    descriptor = None
    for klass in Sample_Library.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sample_estring_is_not_abstract():
    assert not inspect.isabstract(Sample_EString)


def test_sample_estring_constructor_exists():
    assert callable(Sample_EString.__init__)


def test_sample_estring_constructor_args():
    sig = inspect.signature(Sample_EString.__init__)
    params = list(sig.parameters.keys())



def test_sample_person_is_not_abstract():
    assert not inspect.isabstract(Sample_Person)


def test_sample_person_constructor_exists():
    assert callable(Sample_Person.__init__)


def test_sample_person_constructor_args():
    sig = inspect.signature(Sample_Person.__init__)
    params = list(sig.parameters.keys())
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "firstName" in params, "Missing parameter 'firstName'"

def test_sample_person_has_lastName():
    assert hasattr(Sample_Person, "lastName")
    descriptor = None
    for klass in Sample_Person.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_sample_person_has_firstName():
    assert hasattr(Sample_Person, "firstName")
    descriptor = None
    for klass in Sample_Person.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)



def test_sample_book_is_not_abstract():
    assert not inspect.isabstract(Sample_Book)


def test_sample_book_constructor_exists():
    assert callable(Sample_Book.__init__)


def test_sample_book_constructor_args():
    sig = inspect.signature(Sample_Book.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "category" in params, "Missing parameter 'category'"

def test_sample_book_has_name():
    assert hasattr(Sample_Book, "name")
    descriptor = None
    for klass in Sample_Book.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sample_book_has_category():
    assert hasattr(Sample_Book, "category")
    descriptor = None
    for klass in Sample_Book.__mro__:
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
Sample_Library_strategy = st.builds(
    Sample_Library,
    name=
        safe_text
)
Sample_EString_strategy = st.builds(
    Sample_EString,
)
Sample_Person_strategy = st.builds(
    Sample_Person,
    lastName=
        safe_text,
    firstName=
        safe_text
)
Sample_Book_strategy = st.builds(
    Sample_Book,
    name=
        safe_text,
    category=
        safe_text
)

@given(instance=Sample_Library_strategy)
@settings(max_examples=50)
def test_sample_library_instantiation(instance):
    assert isinstance(instance, Sample_Library)



@given(instance=Sample_Library_strategy)
def test_sample_library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Sample_EString_strategy)
@settings(max_examples=50)
def test_sample_estring_instantiation(instance):
    assert isinstance(instance, Sample_EString)

@given(instance=Sample_Person_strategy)
@settings(max_examples=50)
def test_sample_person_instantiation(instance):
    assert isinstance(instance, Sample_Person)



@given(instance=Sample_Person_strategy)
def test_sample_person_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original



@given(instance=Sample_Person_strategy)
def test_sample_person_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=Sample_Book_strategy)
@settings(max_examples=50)
def test_sample_book_instantiation(instance):
    assert isinstance(instance, Sample_Book)



@given(instance=Sample_Book_strategy)
def test_sample_book_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Sample_Book_strategy)
def test_sample_book_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original
