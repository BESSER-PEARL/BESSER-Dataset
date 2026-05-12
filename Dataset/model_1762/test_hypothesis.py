import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Chapter,
    Book_Paragraph,
    Book_Section,
    Book_Chapter,
    Book_Author,
    Book_Book,
    Book_Library,
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



def test_book_paragraph_is_not_abstract():
    assert not inspect.isabstract(Book_Paragraph)


def test_book_paragraph_constructor_exists():
    assert callable(Book_Paragraph.__init__)


def test_book_paragraph_constructor_args():
    sig = inspect.signature(Book_Paragraph.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_book_paragraph_has_title():
    assert hasattr(Book_Paragraph, "title")
    descriptor = None
    for klass in Book_Paragraph.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_book_section_is_not_abstract():
    assert not inspect.isabstract(Book_Section)


def test_book_section_constructor_exists():
    assert callable(Book_Section.__init__)


def test_book_section_constructor_args():
    sig = inspect.signature(Book_Section.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_book_section_has_title():
    assert hasattr(Book_Section, "title")
    descriptor = None
    for klass in Book_Section.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_book_chapter_is_not_abstract():
    assert not inspect.isabstract(Book_Chapter)


def test_book_chapter_constructor_exists():
    assert callable(Book_Chapter.__init__)


def test_book_chapter_constructor_args():
    sig = inspect.signature(Book_Chapter.__init__)
    params = list(sig.parameters.keys())



def test_book_author_is_not_abstract():
    assert not inspect.isabstract(Book_Author)


def test_book_author_constructor_exists():
    assert callable(Book_Author.__init__)


def test_book_author_constructor_args():
    sig = inspect.signature(Book_Author.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_book_author_has_name():
    assert hasattr(Book_Author, "name")
    descriptor = None
    for klass in Book_Author.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_book_book_is_not_abstract():
    assert not inspect.isabstract(Book_Book)


def test_book_book_constructor_exists():
    assert callable(Book_Book.__init__)


def test_book_book_constructor_args():
    sig = inspect.signature(Book_Book.__init__)
    params = list(sig.parameters.keys())
    assert "isbn" in params, "Missing parameter 'isbn'"
    assert "name" in params, "Missing parameter 'name'"
    assert "nbpages" in params, "Missing parameter 'nbpages'"

def test_book_book_has_isbn():
    assert hasattr(Book_Book, "isbn")
    descriptor = None
    for klass in Book_Book.__mro__:
        if "isbn" in klass.__dict__:
            descriptor = klass.__dict__["isbn"]
            break
    assert isinstance(descriptor, property)

def test_book_book_has_name():
    assert hasattr(Book_Book, "name")
    descriptor = None
    for klass in Book_Book.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_book_book_has_nbpages():
    assert hasattr(Book_Book, "nbpages")
    descriptor = None
    for klass in Book_Book.__mro__:
        if "nbpages" in klass.__dict__:
            descriptor = klass.__dict__["nbpages"]
            break
    assert isinstance(descriptor, property)



def test_book_library_is_not_abstract():
    assert not inspect.isabstract(Book_Library)


def test_book_library_constructor_exists():
    assert callable(Book_Library.__init__)


def test_book_library_constructor_args():
    sig = inspect.signature(Book_Library.__init__)
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
Book_Paragraph_strategy = st.builds(
    Book_Paragraph,
    title=
        safe_text
)
Book_Section_strategy = st.builds(
    Book_Section,
    title=
        safe_text
)
Book_Chapter_strategy = st.builds(
    Book_Chapter,
)
Book_Author_strategy = st.builds(
    Book_Author,
    name=
        safe_text
)
Book_Book_strategy = st.builds(
    Book_Book,
    isbn=
        safe_text,
    name=
        safe_text,
    nbpages=
        st.integers()
)
Book_Library_strategy = st.builds(
    Book_Library,
)

@given(instance=Chapter_strategy)
@settings(max_examples=50)
def test_chapter_instantiation(instance):
    assert isinstance(instance, Chapter)

@given(instance=Book_Paragraph_strategy)
@settings(max_examples=50)
def test_book_paragraph_instantiation(instance):
    assert isinstance(instance, Book_Paragraph)



@given(instance=Book_Paragraph_strategy)
def test_book_paragraph_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=Book_Section_strategy)
@settings(max_examples=50)
def test_book_section_instantiation(instance):
    assert isinstance(instance, Book_Section)



@given(instance=Book_Section_strategy)
def test_book_section_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=Book_Chapter_strategy)
@settings(max_examples=50)
def test_book_chapter_instantiation(instance):
    assert isinstance(instance, Book_Chapter)

@given(instance=Book_Author_strategy)
@settings(max_examples=50)
def test_book_author_instantiation(instance):
    assert isinstance(instance, Book_Author)



@given(instance=Book_Author_strategy)
def test_book_author_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Book_Book_strategy)
@settings(max_examples=50)
def test_book_book_instantiation(instance):
    assert isinstance(instance, Book_Book)



@given(instance=Book_Book_strategy)
def test_book_book_isbn_setter(instance):
    original = instance.isbn
    instance.isbn = original
    assert instance.isbn == original



@given(instance=Book_Book_strategy)
def test_book_book_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Book_Book_strategy)
def test_book_book_nbpages_setter(instance):
    original = instance.nbpages
    instance.nbpages = original
    assert instance.nbpages == original

@given(instance=Book_Library_strategy)
@settings(max_examples=50)
def test_book_library_instantiation(instance):
    assert isinstance(instance, Book_Library)
