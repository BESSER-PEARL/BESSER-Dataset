import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Borrowable,
    library::CD,
    library::Book,
    library::Author,
    library::Customer,
    library::Borrowable,
    library::Magazine,
    library::Library,
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



def test_library::cd_is_not_abstract():
    assert not inspect.isabstract(library::CD)


def test_library::cd_constructor_exists():
    assert callable(library::CD.__init__)


def test_library::cd_constructor_args():
    sig = inspect.signature(library::CD.__init__)
    params = list(sig.parameters.keys())



def test_library::book_is_not_abstract():
    assert not inspect.isabstract(library::Book)


def test_library::book_constructor_exists():
    assert callable(library::Book.__init__)


def test_library::book_constructor_args():
    sig = inspect.signature(library::Book.__init__)
    params = list(sig.parameters.keys())



def test_library::author_is_not_abstract():
    assert not inspect.isabstract(library::Author)


def test_library::author_constructor_exists():
    assert callable(library::Author.__init__)


def test_library::author_constructor_args():
    sig = inspect.signature(library::Author.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_library::author_has_name():
    assert hasattr(library::Author, "name")
    descriptor = None
    for klass in library::Author.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



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
    assert "copiesAvailable" in params, "Missing parameter 'copiesAvailable'"
    assert "title" in params, "Missing parameter 'title'"

def test_library::borrowable_has_copiesAvailable():
    assert hasattr(library::Borrowable, "copiesAvailable")
    descriptor = None
    for klass in library::Borrowable.__mro__:
        if "copiesAvailable" in klass.__dict__:
            descriptor = klass.__dict__["copiesAvailable"]
            break
    assert isinstance(descriptor, property)

def test_library::borrowable_has_title():
    assert hasattr(library::Borrowable, "title")
    descriptor = None
    for klass in library::Borrowable.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_library::magazine_is_not_abstract():
    assert not inspect.isabstract(library::Magazine)


def test_library::magazine_constructor_exists():
    assert callable(library::Magazine.__init__)


def test_library::magazine_constructor_args():
    sig = inspect.signature(library::Magazine.__init__)
    params = list(sig.parameters.keys())



def test_library::library_is_not_abstract():
    assert not inspect.isabstract(library::Library)


def test_library::library_constructor_exists():
    assert callable(library::Library.__init__)


def test_library::library_constructor_args():
    sig = inspect.signature(library::Library.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"

def test_library::library_has_address():
    assert hasattr(library::Library, "address")
    descriptor = None
    for klass in library::Library.__mro__:
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
library::CD_strategy = st.builds(
    library::CD,
)
library::Book_strategy = st.builds(
    library::Book,
)
library::Author_strategy = st.builds(
    library::Author,
    name=
        safe_text
)
library::Customer_strategy = st.builds(
    library::Customer,
    name=
        safe_text
)
library::Borrowable_strategy = st.builds(
    library::Borrowable,
    copiesAvailable=
        st.integers(),
    title=
        safe_text
)
library::Magazine_strategy = st.builds(
    library::Magazine,
)
library::Library_strategy = st.builds(
    library::Library,
    address=
        safe_text
)

@given(instance=Borrowable_strategy)
@settings(max_examples=50)
def test_borrowable_instantiation(instance):
    assert isinstance(instance, Borrowable)

@given(instance=library::CD_strategy)
@settings(max_examples=50)
def test_library::cd_instantiation(instance):
    assert isinstance(instance, library::CD)

@given(instance=library::Book_strategy)
@settings(max_examples=50)
def test_library::book_instantiation(instance):
    assert isinstance(instance, library::Book)

@given(instance=library::Author_strategy)
@settings(max_examples=50)
def test_library::author_instantiation(instance):
    assert isinstance(instance, library::Author)

@given(instance=library::Author_strategy)
def test_library::author_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=library::Author_strategy)
def test_library::author_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

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
def test_library::borrowable_copiesAvailable_type(instance):
    assert isinstance(instance.copiesAvailable, int)


@given(instance=library::Borrowable_strategy)
def test_library::borrowable_copiesAvailable_setter(instance):
    original = instance.copiesAvailable
    instance.copiesAvailable = original
    assert instance.copiesAvailable == original

@given(instance=library::Borrowable_strategy)
def test_library::borrowable_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=library::Borrowable_strategy)
def test_library::borrowable_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=library::Magazine_strategy)
@settings(max_examples=50)
def test_library::magazine_instantiation(instance):
    assert isinstance(instance, library::Magazine)

@given(instance=library::Library_strategy)
@settings(max_examples=50)
def test_library::library_instantiation(instance):
    assert isinstance(instance, library::Library)

@given(instance=library::Library_strategy)
def test_library::library_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=library::Library_strategy)
def test_library::library_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original
