import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Chapter,
    Book::Paragraph,
    Book::Section,
    Book::Chapter,
    Book::Author,
    Book::Book,
    Book::Library,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_chapter_is_not_abstract():
    assert not inspect.isabstract(Chapter)


def test_chapter_constructor_exists():
    assert callable(Chapter.__init__)


def test_chapter_constructor_args():
    sig = inspect.signature(Chapter.__init__)
    params = list(sig.parameters.keys())



def test_book::paragraph_is_not_abstract():
    assert not inspect.isabstract(Book::Paragraph)


def test_book::paragraph_constructor_exists():
    assert callable(Book::Paragraph.__init__)


def test_book::paragraph_constructor_args():
    sig = inspect.signature(Book::Paragraph.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_book::paragraph_has_title():
    assert hasattr(Book::Paragraph, "title")
    descriptor = None
    for klass in Book::Paragraph.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_book::section_is_not_abstract():
    assert not inspect.isabstract(Book::Section)


def test_book::section_constructor_exists():
    assert callable(Book::Section.__init__)


def test_book::section_constructor_args():
    sig = inspect.signature(Book::Section.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_book::section_has_title():
    assert hasattr(Book::Section, "title")
    descriptor = None
    for klass in Book::Section.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_book::chapter_is_not_abstract():
    assert not inspect.isabstract(Book::Chapter)


def test_book::chapter_constructor_exists():
    assert callable(Book::Chapter.__init__)


def test_book::chapter_constructor_args():
    sig = inspect.signature(Book::Chapter.__init__)
    params = list(sig.parameters.keys())



def test_book::author_is_not_abstract():
    assert not inspect.isabstract(Book::Author)


def test_book::author_constructor_exists():
    assert callable(Book::Author.__init__)


def test_book::author_constructor_args():
    sig = inspect.signature(Book::Author.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_book::author_has_name():
    assert hasattr(Book::Author, "name")
    descriptor = None
    for klass in Book::Author.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_book::book_is_not_abstract():
    assert not inspect.isabstract(Book::Book)


def test_book::book_constructor_exists():
    assert callable(Book::Book.__init__)


def test_book::book_constructor_args():
    sig = inspect.signature(Book::Book.__init__)
    params = list(sig.parameters.keys())
    assert "nbpages" in params, "Missing parameter 'nbpages'"
    assert "name" in params, "Missing parameter 'name'"
    assert "isbn" in params, "Missing parameter 'isbn'"

def test_book::book_has_nbpages():
    assert hasattr(Book::Book, "nbpages")
    descriptor = None
    for klass in Book::Book.__mro__:
        if "nbpages" in klass.__dict__:
            descriptor = klass.__dict__["nbpages"]
            break
    assert isinstance(descriptor, property)

def test_book::book_has_name():
    assert hasattr(Book::Book, "name")
    descriptor = None
    for klass in Book::Book.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_book::book_has_isbn():
    assert hasattr(Book::Book, "isbn")
    descriptor = None
    for klass in Book::Book.__mro__:
        if "isbn" in klass.__dict__:
            descriptor = klass.__dict__["isbn"]
            break
    assert isinstance(descriptor, property)



def test_book::library_is_not_abstract():
    assert not inspect.isabstract(Book::Library)


def test_book::library_constructor_exists():
    assert callable(Book::Library.__init__)


def test_book::library_constructor_args():
    sig = inspect.signature(Book::Library.__init__)
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
Chapter_strategy = st.builds(
    Chapter,
)
Book::Paragraph_strategy = st.builds(
    Book::Paragraph,
    title=
        safe_text
)
Book::Section_strategy = st.builds(
    Book::Section,
    title=
        safe_text
)
Book::Chapter_strategy = st.builds(
    Book::Chapter,
)
Book::Author_strategy = st.builds(
    Book::Author,
    name=
        safe_text
)
Book::Book_strategy = st.builds(
    Book::Book,
    nbpages=
        st.integers(),
    name=
        safe_text,
    isbn=
        safe_text
)
Book::Library_strategy = st.builds(
    Book::Library,
)

@given(instance=Chapter_strategy)
@settings(max_examples=50)
def test_chapter_instantiation(instance):
    assert isinstance(instance, Chapter)

@given(instance=Book::Paragraph_strategy)
@settings(max_examples=50)
def test_book::paragraph_instantiation(instance):
    assert isinstance(instance, Book::Paragraph)

@given(instance=Book::Paragraph_strategy)
def test_book::paragraph_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=Book::Paragraph_strategy)
def test_book::paragraph_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=Book::Section_strategy)
@settings(max_examples=50)
def test_book::section_instantiation(instance):
    assert isinstance(instance, Book::Section)

@given(instance=Book::Section_strategy)
def test_book::section_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=Book::Section_strategy)
def test_book::section_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=Book::Chapter_strategy)
@settings(max_examples=50)
def test_book::chapter_instantiation(instance):
    assert isinstance(instance, Book::Chapter)

@given(instance=Book::Author_strategy)
@settings(max_examples=50)
def test_book::author_instantiation(instance):
    assert isinstance(instance, Book::Author)

@given(instance=Book::Author_strategy)
def test_book::author_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Book::Author_strategy)
def test_book::author_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Book::Book_strategy)
@settings(max_examples=50)
def test_book::book_instantiation(instance):
    assert isinstance(instance, Book::Book)

@given(instance=Book::Book_strategy)
def test_book::book_nbpages_type(instance):
    assert isinstance(instance.nbpages, int)


@given(instance=Book::Book_strategy)
def test_book::book_nbpages_setter(instance):
    original = instance.nbpages
    instance.nbpages = original
    assert instance.nbpages == original

@given(instance=Book::Book_strategy)
def test_book::book_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Book::Book_strategy)
def test_book::book_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Book::Book_strategy)
def test_book::book_isbn_type(instance):
    assert isinstance(instance.isbn, str)


@given(instance=Book::Book_strategy)
def test_book::book_isbn_setter(instance):
    original = instance.isbn
    instance.isbn = original
    assert instance.isbn == original

@given(instance=Book::Library_strategy)
@settings(max_examples=50)
def test_book::library_instantiation(instance):
    assert isinstance(instance, Book::Library)
