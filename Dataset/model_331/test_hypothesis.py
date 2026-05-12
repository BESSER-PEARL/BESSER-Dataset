import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    library_Member,
    library_Writer,
    library_Book,
    library_Library,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_library_member_is_not_abstract():
    assert not inspect.isabstract(library_Member)


def test_library_member_constructor_exists():
    assert callable(library_Member.__init__)


def test_library_member_constructor_args():
    sig = inspect.signature(library_Member.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_library_member_has_name():
    assert hasattr(library_Member, "name")
    descriptor = None
    for klass in library_Member.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_library_member_has_id():
    assert hasattr(library_Member, "id")
    descriptor = None
    for klass in library_Member.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_library_writer_is_not_abstract():
    assert not inspect.isabstract(library_Writer)


def test_library_writer_constructor_exists():
    assert callable(library_Writer.__init__)


def test_library_writer_constructor_args():
    sig = inspect.signature(library_Writer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_library_writer_has_name():
    assert hasattr(library_Writer, "name")
    descriptor = None
    for klass in library_Writer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_library_book_is_not_abstract():
    assert not inspect.isabstract(library_Book)


def test_library_book_constructor_exists():
    assert callable(library_Book.__init__)


def test_library_book_constructor_args():
    sig = inspect.signature(library_Book.__init__)
    params = list(sig.parameters.keys())
    assert "pages" in params, "Missing parameter 'pages'"
    assert "title" in params, "Missing parameter 'title'"

def test_library_book_has_pages():
    assert hasattr(library_Book, "pages")
    descriptor = None
    for klass in library_Book.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
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
library_Member_strategy = st.builds(
    library_Member,
    name=
        safe_text,
    id=
        st.integers()
)
library_Writer_strategy = st.builds(
    library_Writer,
    name=
        safe_text
)
library_Book_strategy = st.builds(
    library_Book,
    pages=
        st.integers(),
    title=
        safe_text
)
library_Library_strategy = st.builds(
    library_Library,
    name=
        safe_text
)

@given(instance=library_Member_strategy)
@settings(max_examples=50)
def test_library_member_instantiation(instance):
    assert isinstance(instance, library_Member)



@given(instance=library_Member_strategy)
def test_library_member_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=library_Member_strategy)
def test_library_member_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=library_Writer_strategy)
@settings(max_examples=50)
def test_library_writer_instantiation(instance):
    assert isinstance(instance, library_Writer)



@given(instance=library_Writer_strategy)
def test_library_writer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=library_Book_strategy)
@settings(max_examples=50)
def test_library_book_instantiation(instance):
    assert isinstance(instance, library_Book)



@given(instance=library_Book_strategy)
def test_library_book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original



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
