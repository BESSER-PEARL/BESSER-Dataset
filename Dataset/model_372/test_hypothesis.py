import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Writer,
    library_SpecialistBookWriter,
    library_GuideBookWriter,
    library_Library,
    library_Writer,
    library_Book,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_writer_is_not_abstract():
    assert not inspect.isabstract(Writer)


def test_writer_constructor_exists():
    assert callable(Writer.__init__)


def test_writer_constructor_args():
    sig = inspect.signature(Writer.__init__)
    params = list(sig.parameters.keys())



def test_library_specialistbookwriter_is_not_abstract():
    assert not inspect.isabstract(library_SpecialistBookWriter)


def test_library_specialistbookwriter_constructor_exists():
    assert callable(library_SpecialistBookWriter.__init__)


def test_library_specialistbookwriter_constructor_args():
    sig = inspect.signature(library_SpecialistBookWriter.__init__)
    params = list(sig.parameters.keys())
    assert "subject" in params, "Missing parameter 'subject'"

def test_library_specialistbookwriter_has_subject():
    assert hasattr(library_SpecialistBookWriter, "subject")
    descriptor = None
    for klass in library_SpecialistBookWriter.__mro__:
        if "subject" in klass.__dict__:
            descriptor = klass.__dict__["subject"]
            break
    assert isinstance(descriptor, property)



def test_library_guidebookwriter_is_not_abstract():
    assert not inspect.isabstract(library_GuideBookWriter)


def test_library_guidebookwriter_constructor_exists():
    assert callable(library_GuideBookWriter.__init__)


def test_library_guidebookwriter_constructor_args():
    sig = inspect.signature(library_GuideBookWriter.__init__)
    params = list(sig.parameters.keys())
    assert "countries" in params, "Missing parameter 'countries'"

def test_library_guidebookwriter_has_countries():
    assert hasattr(library_GuideBookWriter, "countries")
    descriptor = None
    for klass in library_GuideBookWriter.__mro__:
        if "countries" in klass.__dict__:
            descriptor = klass.__dict__["countries"]
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
    assert "ISBN" in params, "Missing parameter 'ISBN'"
    assert "pages" in params, "Missing parameter 'pages'"
    assert "title" in params, "Missing parameter 'title'"

def test_library_book_has_ISBN():
    assert hasattr(library_Book, "ISBN")
    descriptor = None
    for klass in library_Book.__mro__:
        if "ISBN" in klass.__dict__:
            descriptor = klass.__dict__["ISBN"]
            break
    assert isinstance(descriptor, property)

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
Writer_strategy = st.builds(
    Writer,
)
library_SpecialistBookWriter_strategy = st.builds(
    library_SpecialistBookWriter,
    subject=
        safe_text
)
library_GuideBookWriter_strategy = st.builds(
    library_GuideBookWriter,
    countries=
        safe_text
)
library_Library_strategy = st.builds(
    library_Library,
    name=
        safe_text
)
library_Writer_strategy = st.builds(
    library_Writer,
    name=
        safe_text
)
library_Book_strategy = st.builds(
    library_Book,
    ISBN=
        safe_text,
    pages=
        safe_text,
    title=
        safe_text
)

@given(instance=Writer_strategy)
@settings(max_examples=50)
def test_writer_instantiation(instance):
    assert isinstance(instance, Writer)

@given(instance=library_SpecialistBookWriter_strategy)
@settings(max_examples=50)
def test_library_specialistbookwriter_instantiation(instance):
    assert isinstance(instance, library_SpecialistBookWriter)



@given(instance=library_SpecialistBookWriter_strategy)
def test_library_specialistbookwriter_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original

@given(instance=library_GuideBookWriter_strategy)
@settings(max_examples=50)
def test_library_guidebookwriter_instantiation(instance):
    assert isinstance(instance, library_GuideBookWriter)



@given(instance=library_GuideBookWriter_strategy)
def test_library_guidebookwriter_countries_setter(instance):
    original = instance.countries
    instance.countries = original
    assert instance.countries == original

@given(instance=library_Library_strategy)
@settings(max_examples=50)
def test_library_library_instantiation(instance):
    assert isinstance(instance, library_Library)



@given(instance=library_Library_strategy)
def test_library_library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

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
def test_library_book_ISBN_setter(instance):
    original = instance.ISBN
    instance.ISBN = original
    assert instance.ISBN == original



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
