import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Borrowable,
    library_borrowables_Book,
    library_borrowables_Magazine,
    library_borrowables_CD,
    library_Customer,
    library_Borrowable,
    library_CityLibrary,
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



def test_library_borrowables_book_is_not_abstract():
    assert not inspect.isabstract(library_borrowables_Book)


def test_library_borrowables_book_constructor_exists():
    assert callable(library_borrowables_Book.__init__)


def test_library_borrowables_book_constructor_args():
    sig = inspect.signature(library_borrowables_Book.__init__)
    params = list(sig.parameters.keys())
    assert "authors" in params, "Missing parameter 'authors'"

def test_library_borrowables_book_has_authors():
    assert hasattr(library_borrowables_Book, "authors")
    descriptor = None
    for klass in library_borrowables_Book.__mro__:
        if "authors" in klass.__dict__:
            descriptor = klass.__dict__["authors"]
            break
    assert isinstance(descriptor, property)



def test_library_borrowables_magazine_is_not_abstract():
    assert not inspect.isabstract(library_borrowables_Magazine)


def test_library_borrowables_magazine_constructor_exists():
    assert callable(library_borrowables_Magazine.__init__)


def test_library_borrowables_magazine_constructor_args():
    sig = inspect.signature(library_borrowables_Magazine.__init__)
    params = list(sig.parameters.keys())



def test_library_borrowables_cd_is_not_abstract():
    assert not inspect.isabstract(library_borrowables_CD)


def test_library_borrowables_cd_constructor_exists():
    assert callable(library_borrowables_CD.__init__)


def test_library_borrowables_cd_constructor_args():
    sig = inspect.signature(library_borrowables_CD.__init__)
    params = list(sig.parameters.keys())



def test_library_customer_is_not_abstract():
    assert not inspect.isabstract(library_Customer)


def test_library_customer_constructor_exists():
    assert callable(library_Customer.__init__)


def test_library_customer_constructor_args():
    sig = inspect.signature(library_Customer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_library_customer_has_name():
    assert hasattr(library_Customer, "name")
    descriptor = None
    for klass in library_Customer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_library_borrowable_is_not_abstract():
    assert not inspect.isabstract(library_Borrowable)


def test_library_borrowable_constructor_exists():
    assert callable(library_Borrowable.__init__)


def test_library_borrowable_constructor_args():
    sig = inspect.signature(library_Borrowable.__init__)
    params = list(sig.parameters.keys())
    assert "copiesAvailable" in params, "Missing parameter 'copiesAvailable'"
    assert "title" in params, "Missing parameter 'title'"

def test_library_borrowable_has_copiesAvailable():
    assert hasattr(library_Borrowable, "copiesAvailable")
    descriptor = None
    for klass in library_Borrowable.__mro__:
        if "copiesAvailable" in klass.__dict__:
            descriptor = klass.__dict__["copiesAvailable"]
            break
    assert isinstance(descriptor, property)

def test_library_borrowable_has_title():
    assert hasattr(library_Borrowable, "title")
    descriptor = None
    for klass in library_Borrowable.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_library_citylibrary_is_not_abstract():
    assert not inspect.isabstract(library_CityLibrary)


def test_library_citylibrary_constructor_exists():
    assert callable(library_CityLibrary.__init__)


def test_library_citylibrary_constructor_args():
    sig = inspect.signature(library_CityLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"

def test_library_citylibrary_has_address():
    assert hasattr(library_CityLibrary, "address")
    descriptor = None
    for klass in library_CityLibrary.__mro__:
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
library_borrowables_Book_strategy = st.builds(
    library_borrowables_Book,
    authors=
        safe_text
)
library_borrowables_Magazine_strategy = st.builds(
    library_borrowables_Magazine,
)
library_borrowables_CD_strategy = st.builds(
    library_borrowables_CD,
)
library_Customer_strategy = st.builds(
    library_Customer,
    name=
        safe_text
)
library_Borrowable_strategy = st.builds(
    library_Borrowable,
    copiesAvailable=
        st.integers(),
    title=
        safe_text
)
library_CityLibrary_strategy = st.builds(
    library_CityLibrary,
    address=
        safe_text
)

@given(instance=Borrowable_strategy)
@settings(max_examples=50)
def test_borrowable_instantiation(instance):
    assert isinstance(instance, Borrowable)

@given(instance=library_borrowables_Book_strategy)
@settings(max_examples=50)
def test_library_borrowables_book_instantiation(instance):
    assert isinstance(instance, library_borrowables_Book)



@given(instance=library_borrowables_Book_strategy)
def test_library_borrowables_book_authors_setter(instance):
    original = instance.authors
    instance.authors = original
    assert instance.authors == original

@given(instance=library_borrowables_Magazine_strategy)
@settings(max_examples=50)
def test_library_borrowables_magazine_instantiation(instance):
    assert isinstance(instance, library_borrowables_Magazine)

@given(instance=library_borrowables_CD_strategy)
@settings(max_examples=50)
def test_library_borrowables_cd_instantiation(instance):
    assert isinstance(instance, library_borrowables_CD)

@given(instance=library_Customer_strategy)
@settings(max_examples=50)
def test_library_customer_instantiation(instance):
    assert isinstance(instance, library_Customer)



@given(instance=library_Customer_strategy)
def test_library_customer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=library_Borrowable_strategy)
@settings(max_examples=50)
def test_library_borrowable_instantiation(instance):
    assert isinstance(instance, library_Borrowable)



@given(instance=library_Borrowable_strategy)
def test_library_borrowable_copiesAvailable_setter(instance):
    original = instance.copiesAvailable
    instance.copiesAvailable = original
    assert instance.copiesAvailable == original



@given(instance=library_Borrowable_strategy)
def test_library_borrowable_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=library_CityLibrary_strategy)
@settings(max_examples=50)
def test_library_citylibrary_instantiation(instance):
    assert isinstance(instance, library_CityLibrary)



@given(instance=library_CityLibrary_strategy)
def test_library_citylibrary_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original
