import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Borrowable,
    library::borrowables::Book,
    library::borrowables::Magazine,
    library::borrowables::CD,
    library::Customer,
    library::Borrowable,
    library::CityLibrary,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_borrowable_is_not_abstract():
    assert not inspect.isabstract(Borrowable)


def test_borrowable_constructor_exists():
    assert callable(Borrowable.__init__)


def test_borrowable_constructor_args():
    sig = inspect.signature(Borrowable.__init__)
    params = list(sig.parameters.keys())



def test_library::borrowables::book_is_not_abstract():
    assert not inspect.isabstract(library::borrowables::Book)


def test_library::borrowables::book_constructor_exists():
    assert callable(library::borrowables::Book.__init__)


def test_library::borrowables::book_constructor_args():
    sig = inspect.signature(library::borrowables::Book.__init__)
    params = list(sig.parameters.keys())
    assert "authors" in params, "Missing parameter 'authors'"

def test_library::borrowables::book_has_authors():
    assert hasattr(library::borrowables::Book, "authors")
    descriptor = None
    for klass in library::borrowables::Book.__mro__:
        if "authors" in klass.__dict__:
            descriptor = klass.__dict__["authors"]
            break
    assert isinstance(descriptor, property)



def test_library::borrowables::magazine_is_not_abstract():
    assert not inspect.isabstract(library::borrowables::Magazine)


def test_library::borrowables::magazine_constructor_exists():
    assert callable(library::borrowables::Magazine.__init__)


def test_library::borrowables::magazine_constructor_args():
    sig = inspect.signature(library::borrowables::Magazine.__init__)
    params = list(sig.parameters.keys())



def test_library::borrowables::cd_is_not_abstract():
    assert not inspect.isabstract(library::borrowables::CD)


def test_library::borrowables::cd_constructor_exists():
    assert callable(library::borrowables::CD.__init__)


def test_library::borrowables::cd_constructor_args():
    sig = inspect.signature(library::borrowables::CD.__init__)
    params = list(sig.parameters.keys())



def test_library::customer_is_not_abstract():
    assert not inspect.isabstract(library::Customer)


def test_library::customer_constructor_exists():
    assert callable(library::Customer.__init__)


def test_library::customer_constructor_args():
    sig = inspect.signature(library::Customer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_library::customer_has_name():
    assert hasattr(library::Customer, "name")
    descriptor = None
    for klass in library::Customer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_library::borrowable_is_not_abstract():
    assert not inspect.isabstract(library::Borrowable)


def test_library::borrowable_constructor_exists():
    assert callable(library::Borrowable.__init__)


def test_library::borrowable_constructor_args():
    sig = inspect.signature(library::Borrowable.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "copiesAvailable" in params, "Missing parameter 'copiesAvailable'"

def test_library::borrowable_has_title():
    assert hasattr(library::Borrowable, "title")
    descriptor = None
    for klass in library::Borrowable.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_library::borrowable_has_copiesAvailable():
    assert hasattr(library::Borrowable, "copiesAvailable")
    descriptor = None
    for klass in library::Borrowable.__mro__:
        if "copiesAvailable" in klass.__dict__:
            descriptor = klass.__dict__["copiesAvailable"]
            break
    assert isinstance(descriptor, property)



def test_library::citylibrary_is_not_abstract():
    assert not inspect.isabstract(library::CityLibrary)


def test_library::citylibrary_constructor_exists():
    assert callable(library::CityLibrary.__init__)


def test_library::citylibrary_constructor_args():
    sig = inspect.signature(library::CityLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"

def test_library::citylibrary_has_address():
    assert hasattr(library::CityLibrary, "address")
    descriptor = None
    for klass in library::CityLibrary.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
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
Borrowable_strategy = st.builds(
    Borrowable,
)
library::borrowables::Book_strategy = st.builds(
    library::borrowables::Book,
    authors=
        safe_text
)
library::borrowables::Magazine_strategy = st.builds(
    library::borrowables::Magazine,
)
library::borrowables::CD_strategy = st.builds(
    library::borrowables::CD,
)
library::Customer_strategy = st.builds(
    library::Customer,
    name=
        safe_text
)
library::Borrowable_strategy = st.builds(
    library::Borrowable,
    title=
        safe_text,
    copiesAvailable=
        st.integers()
)
library::CityLibrary_strategy = st.builds(
    library::CityLibrary,
    address=
        safe_text
)

@given(instance=Borrowable_strategy)
@settings(max_examples=50)
def test_borrowable_instantiation(instance):
    assert isinstance(instance, Borrowable)

@given(instance=library::borrowables::Book_strategy)
@settings(max_examples=50)
def test_library::borrowables::book_instantiation(instance):
    assert isinstance(instance, library::borrowables::Book)

@given(instance=library::borrowables::Book_strategy)
def test_library::borrowables::book_authors_type(instance):
    assert isinstance(instance.authors, str)


@given(instance=library::borrowables::Book_strategy)
def test_library::borrowables::book_authors_setter(instance):
    original = instance.authors
    instance.authors = original
    assert instance.authors == original

@given(instance=library::borrowables::Magazine_strategy)
@settings(max_examples=50)
def test_library::borrowables::magazine_instantiation(instance):
    assert isinstance(instance, library::borrowables::Magazine)

@given(instance=library::borrowables::CD_strategy)
@settings(max_examples=50)
def test_library::borrowables::cd_instantiation(instance):
    assert isinstance(instance, library::borrowables::CD)

@given(instance=library::Customer_strategy)
@settings(max_examples=50)
def test_library::customer_instantiation(instance):
    assert isinstance(instance, library::Customer)

@given(instance=library::Customer_strategy)
def test_library::customer_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=library::Customer_strategy)
def test_library::customer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=library::Borrowable_strategy)
@settings(max_examples=50)
def test_library::borrowable_instantiation(instance):
    assert isinstance(instance, library::Borrowable)

@given(instance=library::Borrowable_strategy)
def test_library::borrowable_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=library::Borrowable_strategy)
def test_library::borrowable_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=library::Borrowable_strategy)
def test_library::borrowable_copiesAvailable_type(instance):
    assert isinstance(instance.copiesAvailable, int)


@given(instance=library::Borrowable_strategy)
def test_library::borrowable_copiesAvailable_setter(instance):
    original = instance.copiesAvailable
    instance.copiesAvailable = original
    assert instance.copiesAvailable == original

@given(instance=library::CityLibrary_strategy)
@settings(max_examples=50)
def test_library::citylibrary_instantiation(instance):
    assert isinstance(instance, library::CityLibrary)

@given(instance=library::CityLibrary_strategy)
def test_library::citylibrary_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=library::CityLibrary_strategy)
def test_library::citylibrary_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original
