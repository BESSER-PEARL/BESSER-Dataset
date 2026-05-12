import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    library_Book,
    library_Library,
    library_UoD,
    AbstractPerson,
    library_Author,
    library_Person,
    library_Loan,
    library_AbstractPerson,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_library_book_is_not_abstract():
    assert not inspect.isabstract(library_Book)


def test_library_book_constructor_exists():
    assert callable(library_Book.__init__)


def test_library_book_constructor_args():
    sig = inspect.signature(library_Book.__init__)
    params = list(sig.parameters.keys())
    assert "isbn" in params, "Missing parameter 'isbn'"
    assert "title" in params, "Missing parameter 'title'"

def test_library_book_has_isbn():
    assert hasattr(library_Book, "isbn")
    descriptor = None
    for klass in library_Book.__mro__:
        if "isbn" in klass.__dict__:
            descriptor = klass.__dict__["isbn"]
            break
    assert isinstance(descriptor, property)

def test_library_book_has_title():
    assert hasattr(library_Book, "title")
    descriptor = None
    for klass in library_Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_library_library_is_not_abstract():
    assert not inspect.isabstract(library_Library)


def test_library_library_constructor_exists():
    assert callable(library_Library.__init__)


def test_library_library_constructor_args():
    sig = inspect.signature(library_Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_library_library_has_name():
    assert hasattr(library_Library, "name")
    descriptor = None
    for klass in library_Library.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_library_uod_is_not_abstract():
    assert not inspect.isabstract(library_UoD)


def test_library_uod_constructor_exists():
    assert callable(library_UoD.__init__)


def test_library_uod_constructor_args():
    sig = inspect.signature(library_UoD.__init__)
    params = list(sig.parameters.keys())



def test_abstractperson_is_not_abstract():
    assert not inspect.isabstract(AbstractPerson)


def test_abstractperson_constructor_exists():
    assert callable(AbstractPerson.__init__)


def test_abstractperson_constructor_args():
    sig = inspect.signature(AbstractPerson.__init__)
    params = list(sig.parameters.keys())



def test_library_author_is_not_abstract():
    assert not inspect.isabstract(library_Author)


def test_library_author_constructor_exists():
    assert callable(library_Author.__init__)


def test_library_author_constructor_args():
    sig = inspect.signature(library_Author.__init__)
    params = list(sig.parameters.keys())



def test_library_person_is_not_abstract():
    assert not inspect.isabstract(library_Person)


def test_library_person_constructor_exists():
    assert callable(library_Person.__init__)


def test_library_person_constructor_args():
    sig = inspect.signature(library_Person.__init__)
    params = list(sig.parameters.keys())



def test_library_loan_is_not_abstract():
    assert not inspect.isabstract(library_Loan)


def test_library_loan_constructor_exists():
    assert callable(library_Loan.__init__)


def test_library_loan_constructor_args():
    sig = inspect.signature(library_Loan.__init__)
    params = list(sig.parameters.keys())



def test_library_abstractperson_is_not_abstract():
    assert not inspect.isabstract(library_AbstractPerson)


def test_library_abstractperson_constructor_exists():
    assert callable(library_AbstractPerson.__init__)


def test_library_abstractperson_constructor_args():
    sig = inspect.signature(library_AbstractPerson.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_library_abstractperson_has_name():
    assert hasattr(library_AbstractPerson, "name")
    descriptor = None
    for klass in library_AbstractPerson.__mro__:
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
library_Book_strategy = st.builds(
    library_Book,
    isbn=
        safe_text,
    title=
        safe_text
)
library_Library_strategy = st.builds(
    library_Library,
    name=
        safe_text
)
library_UoD_strategy = st.builds(
    library_UoD,
)
AbstractPerson_strategy = st.builds(
    AbstractPerson,
)
library_Author_strategy = st.builds(
    library_Author,
)
library_Person_strategy = st.builds(
    library_Person,
)
library_Loan_strategy = st.builds(
    library_Loan,
)
library_AbstractPerson_strategy = st.builds(
    library_AbstractPerson,
    name=
        safe_text
)

@given(instance=library_Book_strategy)
@settings(max_examples=50)
def test_library_book_instantiation(instance):
    assert isinstance(instance, library_Book)



@given(instance=library_Book_strategy)
def test_library_book_isbn_setter(instance):
    original = instance.isbn
    instance.isbn = original
    assert instance.isbn == original



@given(instance=library_Book_strategy)
def test_library_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=library_Library_strategy)
@settings(max_examples=50)
def test_library_library_instantiation(instance):
    assert isinstance(instance, library_Library)



@given(instance=library_Library_strategy)
def test_library_library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=library_UoD_strategy)
@settings(max_examples=50)
def test_library_uod_instantiation(instance):
    assert isinstance(instance, library_UoD)

@given(instance=AbstractPerson_strategy)
@settings(max_examples=50)
def test_abstractperson_instantiation(instance):
    assert isinstance(instance, AbstractPerson)

@given(instance=library_Author_strategy)
@settings(max_examples=50)
def test_library_author_instantiation(instance):
    assert isinstance(instance, library_Author)

@given(instance=library_Person_strategy)
@settings(max_examples=50)
def test_library_person_instantiation(instance):
    assert isinstance(instance, library_Person)

@given(instance=library_Loan_strategy)
@settings(max_examples=50)
def test_library_loan_instantiation(instance):
    assert isinstance(instance, library_Loan)

@given(instance=library_AbstractPerson_strategy)
@settings(max_examples=50)
def test_library_abstractperson_instantiation(instance):
    assert isinstance(instance, library_AbstractPerson)



@given(instance=library_AbstractPerson_strategy)
def test_library_abstractperson_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
