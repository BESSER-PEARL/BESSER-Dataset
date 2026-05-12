import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Asset,
    schoollibrary_Asset,
    Library,
    schoollibrary_SchoolLibrary,
    Book,
    schoollibrary_SchoolBook,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_asset_is_not_abstract():
    assert not inspect.isabstract(Asset)


def test_asset_constructor_exists():
    assert callable(Asset.__init__)


def test_asset_constructor_args():
    sig = inspect.signature(Asset.__init__)
    params = list(sig.parameters.keys())



def test_schoollibrary_asset_is_not_abstract():
    assert not inspect.isabstract(schoollibrary_Asset)


def test_schoollibrary_asset_constructor_exists():
    assert callable(schoollibrary_Asset.__init__)


def test_schoollibrary_asset_constructor_args():
    sig = inspect.signature(schoollibrary_Asset.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_schoollibrary_asset_has_value():
    assert hasattr(schoollibrary_Asset, "value")
    descriptor = None
    for klass in schoollibrary_Asset.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_library_is_not_abstract():
    assert not inspect.isabstract(Library)


def test_library_constructor_exists():
    assert callable(Library.__init__)


def test_library_constructor_args():
    sig = inspect.signature(Library.__init__)
    params = list(sig.parameters.keys())



def test_schoollibrary_schoollibrary_is_not_abstract():
    assert not inspect.isabstract(schoollibrary_SchoolLibrary)


def test_schoollibrary_schoollibrary_constructor_exists():
    assert callable(schoollibrary_SchoolLibrary.__init__)


def test_schoollibrary_schoollibrary_constructor_args():
    sig = inspect.signature(schoollibrary_SchoolLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_schoollibrary_schoollibrary_has_location():
    assert hasattr(schoollibrary_SchoolLibrary, "location")
    descriptor = None
    for klass in schoollibrary_SchoolLibrary.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_book_is_not_abstract():
    assert not inspect.isabstract(Book)


def test_book_constructor_exists():
    assert callable(Book.__init__)


def test_book_constructor_args():
    sig = inspect.signature(Book.__init__)
    params = list(sig.parameters.keys())



def test_schoollibrary_schoolbook_is_not_abstract():
    assert not inspect.isabstract(schoollibrary_SchoolBook)


def test_schoollibrary_schoolbook_constructor_exists():
    assert callable(schoollibrary_SchoolBook.__init__)


def test_schoollibrary_schoolbook_constructor_args():
    sig = inspect.signature(schoollibrary_SchoolBook.__init__)
    params = list(sig.parameters.keys())


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
Asset_strategy = st.builds(
    Asset,
)
schoollibrary_Asset_strategy = st.builds(
    schoollibrary_Asset,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Library_strategy = st.builds(
    Library,
)
schoollibrary_SchoolLibrary_strategy = st.builds(
    schoollibrary_SchoolLibrary,
    location=
        safe_text
)
Book_strategy = st.builds(
    Book,
)
schoollibrary_SchoolBook_strategy = st.builds(
    schoollibrary_SchoolBook,
)

@given(instance=Asset_strategy)
@settings(max_examples=50)
def test_asset_instantiation(instance):
    assert isinstance(instance, Asset)

@given(instance=schoollibrary_Asset_strategy)
@settings(max_examples=50)
def test_schoollibrary_asset_instantiation(instance):
    assert isinstance(instance, schoollibrary_Asset)



@given(instance=schoollibrary_Asset_strategy)
def test_schoollibrary_asset_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Library_strategy)
@settings(max_examples=50)
def test_library_instantiation(instance):
    assert isinstance(instance, Library)

@given(instance=schoollibrary_SchoolLibrary_strategy)
@settings(max_examples=50)
def test_schoollibrary_schoollibrary_instantiation(instance):
    assert isinstance(instance, schoollibrary_SchoolLibrary)



@given(instance=schoollibrary_SchoolLibrary_strategy)
def test_schoollibrary_schoollibrary_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=Book_strategy)
@settings(max_examples=50)
def test_book_instantiation(instance):
    assert isinstance(instance, Book)

@given(instance=schoollibrary_SchoolBook_strategy)
@settings(max_examples=50)
def test_schoollibrary_schoolbook_instantiation(instance):
    assert isinstance(instance, schoollibrary_SchoolBook)
