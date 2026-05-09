import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Library,
    schoollibrary::SchoolLibrary,
    Asset,
    Book,
    schoollibrary::SchoolBook,
    schoollibrary::Asset,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_library_is_not_abstract():
    assert not inspect.isabstract(Library)


def test_library_constructor_exists():
    assert callable(Library.__init__)


def test_library_constructor_args():
    sig = inspect.signature(Library.__init__)
    params = list(sig.parameters.keys())



def test_schoollibrary::schoollibrary_is_not_abstract():
    assert not inspect.isabstract(schoollibrary::SchoolLibrary)


def test_schoollibrary::schoollibrary_constructor_exists():
    assert callable(schoollibrary::SchoolLibrary.__init__)


def test_schoollibrary::schoollibrary_constructor_args():
    sig = inspect.signature(schoollibrary::SchoolLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_schoollibrary::schoollibrary_has_location():
    assert hasattr(schoollibrary::SchoolLibrary, "location")
    descriptor = None
    for klass in schoollibrary::SchoolLibrary.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_asset_is_not_abstract():
    assert not inspect.isabstract(Asset)


def test_asset_constructor_exists():
    assert callable(Asset.__init__)


def test_asset_constructor_args():
    sig = inspect.signature(Asset.__init__)
    params = list(sig.parameters.keys())



def test_book_is_not_abstract():
    assert not inspect.isabstract(Book)


def test_book_constructor_exists():
    assert callable(Book.__init__)


def test_book_constructor_args():
    sig = inspect.signature(Book.__init__)
    params = list(sig.parameters.keys())



def test_schoollibrary::schoolbook_is_not_abstract():
    assert not inspect.isabstract(schoollibrary::SchoolBook)


def test_schoollibrary::schoolbook_constructor_exists():
    assert callable(schoollibrary::SchoolBook.__init__)


def test_schoollibrary::schoolbook_constructor_args():
    sig = inspect.signature(schoollibrary::SchoolBook.__init__)
    params = list(sig.parameters.keys())



def test_schoollibrary::asset_is_not_abstract():
    assert not inspect.isabstract(schoollibrary::Asset)


def test_schoollibrary::asset_constructor_exists():
    assert callable(schoollibrary::Asset.__init__)


def test_schoollibrary::asset_constructor_args():
    sig = inspect.signature(schoollibrary::Asset.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_schoollibrary::asset_has_value():
    assert hasattr(schoollibrary::Asset, "value")
    descriptor = None
    for klass in schoollibrary::Asset.__mro__:
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
Library_strategy = st.builds(
    Library,
)
schoollibrary::SchoolLibrary_strategy = st.builds(
    schoollibrary::SchoolLibrary,
    location=
        safe_text
)
Asset_strategy = st.builds(
    Asset,
)
Book_strategy = st.builds(
    Book,
)
schoollibrary::SchoolBook_strategy = st.builds(
    schoollibrary::SchoolBook,
)
schoollibrary::Asset_strategy = st.builds(
    schoollibrary::Asset,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

@given(instance=Library_strategy)
@settings(max_examples=50)
def test_library_instantiation(instance):
    assert isinstance(instance, Library)

@given(instance=schoollibrary::SchoolLibrary_strategy)
@settings(max_examples=50)
def test_schoollibrary::schoollibrary_instantiation(instance):
    assert isinstance(instance, schoollibrary::SchoolLibrary)

@given(instance=schoollibrary::SchoolLibrary_strategy)
def test_schoollibrary::schoollibrary_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=schoollibrary::SchoolLibrary_strategy)
def test_schoollibrary::schoollibrary_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=Asset_strategy)
@settings(max_examples=50)
def test_asset_instantiation(instance):
    assert isinstance(instance, Asset)

@given(instance=Book_strategy)
@settings(max_examples=50)
def test_book_instantiation(instance):
    assert isinstance(instance, Book)

@given(instance=schoollibrary::SchoolBook_strategy)
@settings(max_examples=50)
def test_schoollibrary::schoolbook_instantiation(instance):
    assert isinstance(instance, schoollibrary::SchoolBook)

@given(instance=schoollibrary::Asset_strategy)
@settings(max_examples=50)
def test_schoollibrary::asset_instantiation(instance):
    assert isinstance(instance, schoollibrary::Asset)

@given(instance=schoollibrary::Asset_strategy)
def test_schoollibrary::asset_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=schoollibrary::Asset_strategy)
def test_schoollibrary::asset_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original
