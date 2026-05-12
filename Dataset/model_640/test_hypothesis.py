import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Borrowable,
    library_CD,
    library_Book,
    library_Author,
    library_Customer,
    library_Borrowable,
    library_Magazine,
    library_Library,
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



def test_library_cd_is_not_abstract():
    assert not inspect.isabstract(library_CD)


def test_library_cd_constructor_exists():
    assert callable(library_CD.__init__)


def test_library_cd_constructor_args():
    sig = inspect.signature(library_CD.__init__)
    params = list(sig.parameters.keys())



def test_library_book_is_not_abstract():
    assert not inspect.isabstract(library_Book)


def test_library_book_constructor_exists():
    assert callable(library_Book.__init__)


def test_library_book_constructor_args():
    sig = inspect.signature(library_Book.__init__)
    params = list(sig.parameters.keys())



def test_library_author_is_not_abstract():
    assert not inspect.isabstract(library_Author)


def test_library_author_constructor_exists():
    assert callable(library_Author.__init__)


def test_library_author_constructor_args():
    sig = inspect.signature(library_Author.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_library_author_has_name():
    assert hasattr(library_Author, "name")
    descriptor = None
    for klass in library_Author.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



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
    assert "title" in params, "Missing parameter 'title'"
    assert "copiesAvailable" in params, "Missing parameter 'copiesAvailable'"

def test_library_borrowable_has_title():
    assert hasattr(library_Borrowable, "title")
    descriptor = None
    for klass in library_Borrowable.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_library_borrowable_has_copiesAvailable():
    assert hasattr(library_Borrowable, "copiesAvailable")
    descriptor = None
    for klass in library_Borrowable.__mro__:
        if "copiesAvailable" in klass.__dict__:
            descriptor = klass.__dict__["copiesAvailable"]
            break
    assert isinstance(descriptor, property)



def test_library_magazine_is_not_abstract():
    assert not inspect.isabstract(library_Magazine)


def test_library_magazine_constructor_exists():
    assert callable(library_Magazine.__init__)


def test_library_magazine_constructor_args():
    sig = inspect.signature(library_Magazine.__init__)
    params = list(sig.parameters.keys())



def test_library_library_is_not_abstract():
    assert not inspect.isabstract(library_Library)


def test_library_library_constructor_exists():
    assert callable(library_Library.__init__)


def test_library_library_constructor_args():
    sig = inspect.signature(library_Library.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"

def test_library_library_has_address():
    assert hasattr(library_Library, "address")
    descriptor = None
    for klass in library_Library.__mro__:
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
library_CD_strategy = st.builds(
    library_CD,
)
library_Book_strategy = st.builds(
    library_Book,
)
library_Author_strategy = st.builds(
    library_Author,
    name=
        safe_text
)
library_Customer_strategy = st.builds(
    library_Customer,
    name=
        safe_text
)
library_Borrowable_strategy = st.builds(
    library_Borrowable,
    title=
        safe_text,
    copiesAvailable=
        st.integers()
)
library_Magazine_strategy = st.builds(
    library_Magazine,
)
library_Library_strategy = st.builds(
    library_Library,
    address=
        safe_text
)

@given(instance=Borrowable_strategy)
@settings(max_examples=50)
def test_borrowable_instantiation(instance):
    assert isinstance(instance, Borrowable)

@given(instance=library_CD_strategy)
@settings(max_examples=50)
def test_library_cd_instantiation(instance):
    assert isinstance(instance, library_CD)

@given(instance=library_Book_strategy)
@settings(max_examples=50)
def test_library_book_instantiation(instance):
    assert isinstance(instance, library_Book)

@given(instance=library_Author_strategy)
@settings(max_examples=50)
def test_library_author_instantiation(instance):
    assert isinstance(instance, library_Author)



@given(instance=library_Author_strategy)
def test_library_author_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

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
def test_library_borrowable_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=library_Borrowable_strategy)
def test_library_borrowable_copiesAvailable_setter(instance):
    original = instance.copiesAvailable
    instance.copiesAvailable = original
    assert instance.copiesAvailable == original

@given(instance=library_Magazine_strategy)
@settings(max_examples=50)
def test_library_magazine_instantiation(instance):
    assert isinstance(instance, library_Magazine)

@given(instance=library_Library_strategy)
@settings(max_examples=50)
def test_library_library_instantiation(instance):
    assert isinstance(instance, library_Library)



@given(instance=library_Library_strategy)
def test_library_library_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original
