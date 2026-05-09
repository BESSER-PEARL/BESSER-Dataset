import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    AbstractPerson,
    library::Loan,
    library::AbstractPerson,
    library::Author,
    library::Person,
    library::Library,
    library::UoD,
    library::Book,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_abstractperson_is_not_abstract():
    assert not inspect.isabstract(AbstractPerson)


def test_abstractperson_constructor_exists():
    assert callable(AbstractPerson.__init__)


def test_abstractperson_constructor_args():
    sig = inspect.signature(AbstractPerson.__init__)
    params = list(sig.parameters.keys())



def test_library::loan_is_not_abstract():
    assert not inspect.isabstract(library::Loan)


def test_library::loan_constructor_exists():
    assert callable(library::Loan.__init__)


def test_library::loan_constructor_args():
    sig = inspect.signature(library::Loan.__init__)
    params = list(sig.parameters.keys())



def test_library::abstractperson_is_not_abstract():
    assert not inspect.isabstract(library::AbstractPerson)


def test_library::abstractperson_constructor_exists():
    assert callable(library::AbstractPerson.__init__)


def test_library::abstractperson_constructor_args():
    sig = inspect.signature(library::AbstractPerson.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_library::abstractperson_has_name():
    assert hasattr(library::AbstractPerson, "name")
    descriptor = None
    for klass in library::AbstractPerson.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_library::author_is_not_abstract():
    assert not inspect.isabstract(library::Author)


def test_library::author_constructor_exists():
    assert callable(library::Author.__init__)


def test_library::author_constructor_args():
    sig = inspect.signature(library::Author.__init__)
    params = list(sig.parameters.keys())



def test_library::person_is_not_abstract():
    assert not inspect.isabstract(library::Person)


def test_library::person_constructor_exists():
    assert callable(library::Person.__init__)


def test_library::person_constructor_args():
    sig = inspect.signature(library::Person.__init__)
    params = list(sig.parameters.keys())



def test_library::library_is_not_abstract():
    assert not inspect.isabstract(library::Library)


def test_library::library_constructor_exists():
    assert callable(library::Library.__init__)


def test_library::library_constructor_args():
    sig = inspect.signature(library::Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_library::library_has_name():
    assert hasattr(library::Library, "name")
    descriptor = None
    for klass in library::Library.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_library::uod_is_not_abstract():
    assert not inspect.isabstract(library::UoD)


def test_library::uod_constructor_exists():
    assert callable(library::UoD.__init__)


def test_library::uod_constructor_args():
    sig = inspect.signature(library::UoD.__init__)
    params = list(sig.parameters.keys())



def test_library::book_is_not_abstract():
    assert not inspect.isabstract(library::Book)


def test_library::book_constructor_exists():
    assert callable(library::Book.__init__)


def test_library::book_constructor_args():
    sig = inspect.signature(library::Book.__init__)
    params = list(sig.parameters.keys())
    assert "isbn" in params, "Missing parameter 'isbn'"
    assert "title" in params, "Missing parameter 'title'"

def test_library::book_has_isbn():
    assert hasattr(library::Book, "isbn")
    descriptor = None
    for klass in library::Book.__mro__:
        if "isbn" in klass.__dict__:
            descriptor = klass.__dict__["isbn"]
            break
    assert isinstance(descriptor, property)

def test_library::book_has_title():
    assert hasattr(library::Book, "title")
    descriptor = None
    for klass in library::Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
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
AbstractPerson_strategy = st.builds(
    AbstractPerson,
)
library::Loan_strategy = st.builds(
    library::Loan,
)
library::AbstractPerson_strategy = st.builds(
    library::AbstractPerson,
    name=
        safe_text
)
library::Author_strategy = st.builds(
    library::Author,
)
library::Person_strategy = st.builds(
    library::Person,
)
library::Library_strategy = st.builds(
    library::Library,
    name=
        safe_text
)
library::UoD_strategy = st.builds(
    library::UoD,
)
library::Book_strategy = st.builds(
    library::Book,
    isbn=
        safe_text,
    title=
        safe_text
)

@given(instance=AbstractPerson_strategy)
@settings(max_examples=50)
def test_abstractperson_instantiation(instance):
    assert isinstance(instance, AbstractPerson)

@given(instance=library::Loan_strategy)
@settings(max_examples=50)
def test_library::loan_instantiation(instance):
    assert isinstance(instance, library::Loan)

@given(instance=library::AbstractPerson_strategy)
@settings(max_examples=50)
def test_library::abstractperson_instantiation(instance):
    assert isinstance(instance, library::AbstractPerson)

@given(instance=library::AbstractPerson_strategy)
def test_library::abstractperson_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=library::AbstractPerson_strategy)
def test_library::abstractperson_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=library::Author_strategy)
@settings(max_examples=50)
def test_library::author_instantiation(instance):
    assert isinstance(instance, library::Author)

@given(instance=library::Person_strategy)
@settings(max_examples=50)
def test_library::person_instantiation(instance):
    assert isinstance(instance, library::Person)

@given(instance=library::Library_strategy)
@settings(max_examples=50)
def test_library::library_instantiation(instance):
    assert isinstance(instance, library::Library)

@given(instance=library::Library_strategy)
def test_library::library_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=library::Library_strategy)
def test_library::library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=library::UoD_strategy)
@settings(max_examples=50)
def test_library::uod_instantiation(instance):
    assert isinstance(instance, library::UoD)

@given(instance=library::Book_strategy)
@settings(max_examples=50)
def test_library::book_instantiation(instance):
    assert isinstance(instance, library::Book)

@given(instance=library::Book_strategy)
def test_library::book_isbn_type(instance):
    assert isinstance(instance.isbn, str)


@given(instance=library::Book_strategy)
def test_library::book_isbn_setter(instance):
    original = instance.isbn
    instance.isbn = original
    assert instance.isbn == original

@given(instance=library::Book_strategy)
def test_library::book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=library::Book_strategy)
def test_library::book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original
