import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Writer,
    library::SpecialistBookWriter,
    library::GuideBookWriter,
    library::Library,
    library::Writer,
    library::Book,
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



def test_library::specialistbookwriter_is_not_abstract():
    assert not inspect.isabstract(library::SpecialistBookWriter)


def test_library::specialistbookwriter_constructor_exists():
    assert callable(library::SpecialistBookWriter.__init__)


def test_library::specialistbookwriter_constructor_args():
    sig = inspect.signature(library::SpecialistBookWriter.__init__)
    params = list(sig.parameters.keys())
    assert "subject" in params, "Missing parameter 'subject'"

def test_library::specialistbookwriter_has_subject():
    assert hasattr(library::SpecialistBookWriter, "subject")
    descriptor = None
    for klass in library::SpecialistBookWriter.__mro__:
        if "subject" in klass.__dict__:
            descriptor = klass.__dict__["subject"]
            break
    assert isinstance(descriptor, property)



def test_library::guidebookwriter_is_not_abstract():
    assert not inspect.isabstract(library::GuideBookWriter)


def test_library::guidebookwriter_constructor_exists():
    assert callable(library::GuideBookWriter.__init__)


def test_library::guidebookwriter_constructor_args():
    sig = inspect.signature(library::GuideBookWriter.__init__)
    params = list(sig.parameters.keys())
    assert "countries" in params, "Missing parameter 'countries'"

def test_library::guidebookwriter_has_countries():
    assert hasattr(library::GuideBookWriter, "countries")
    descriptor = None
    for klass in library::GuideBookWriter.__mro__:
        if "countries" in klass.__dict__:
            descriptor = klass.__dict__["countries"]
            break
    assert isinstance(descriptor, property)



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



def test_library::writer_is_not_abstract():
    assert not inspect.isabstract(library::Writer)


def test_library::writer_constructor_exists():
    assert callable(library::Writer.__init__)


def test_library::writer_constructor_args():
    sig = inspect.signature(library::Writer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_library::writer_has_name():
    assert hasattr(library::Writer, "name")
    descriptor = None
    for klass in library::Writer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_library::book_is_not_abstract():
    assert not inspect.isabstract(library::Book)


def test_library::book_constructor_exists():
    assert callable(library::Book.__init__)


def test_library::book_constructor_args():
    sig = inspect.signature(library::Book.__init__)
    params = list(sig.parameters.keys())
    assert "ISBN" in params, "Missing parameter 'ISBN'"
    assert "pages" in params, "Missing parameter 'pages'"
    assert "title" in params, "Missing parameter 'title'"

def test_library::book_has_ISBN():
    assert hasattr(library::Book, "ISBN")
    descriptor = None
    for klass in library::Book.__mro__:
        if "ISBN" in klass.__dict__:
            descriptor = klass.__dict__["ISBN"]
            break
    assert isinstance(descriptor, property)

def test_library::book_has_pages():
    assert hasattr(library::Book, "pages")
    descriptor = None
    for klass in library::Book.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
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
Writer_strategy = st.builds(
    Writer,
)
library::SpecialistBookWriter_strategy = st.builds(
    library::SpecialistBookWriter,
    subject=
        safe_text
)
library::GuideBookWriter_strategy = st.builds(
    library::GuideBookWriter,
    countries=
        safe_text
)
library::Library_strategy = st.builds(
    library::Library,
    name=
        safe_text
)
library::Writer_strategy = st.builds(
    library::Writer,
    name=
        safe_text
)
library::Book_strategy = st.builds(
    library::Book,
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

@given(instance=library::SpecialistBookWriter_strategy)
@settings(max_examples=50)
def test_library::specialistbookwriter_instantiation(instance):
    assert isinstance(instance, library::SpecialistBookWriter)

@given(instance=library::SpecialistBookWriter_strategy)
def test_library::specialistbookwriter_subject_type(instance):
    assert isinstance(instance.subject, str)


@given(instance=library::SpecialistBookWriter_strategy)
def test_library::specialistbookwriter_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original

@given(instance=library::GuideBookWriter_strategy)
@settings(max_examples=50)
def test_library::guidebookwriter_instantiation(instance):
    assert isinstance(instance, library::GuideBookWriter)

@given(instance=library::GuideBookWriter_strategy)
def test_library::guidebookwriter_countries_type(instance):
    assert isinstance(instance.countries, str)


@given(instance=library::GuideBookWriter_strategy)
def test_library::guidebookwriter_countries_setter(instance):
    original = instance.countries
    instance.countries = original
    assert instance.countries == original

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

@given(instance=library::Writer_strategy)
@settings(max_examples=50)
def test_library::writer_instantiation(instance):
    assert isinstance(instance, library::Writer)

@given(instance=library::Writer_strategy)
def test_library::writer_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=library::Writer_strategy)
def test_library::writer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=library::Book_strategy)
@settings(max_examples=50)
def test_library::book_instantiation(instance):
    assert isinstance(instance, library::Book)

@given(instance=library::Book_strategy)
def test_library::book_ISBN_type(instance):
    assert isinstance(instance.ISBN, str)


@given(instance=library::Book_strategy)
def test_library::book_ISBN_setter(instance):
    original = instance.ISBN
    instance.ISBN = original
    assert instance.ISBN == original

@given(instance=library::Book_strategy)
def test_library::book_pages_type(instance):
    assert isinstance(instance.pages, str)


@given(instance=library::Book_strategy)
def test_library::book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=library::Book_strategy)
def test_library::book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=library::Book_strategy)
def test_library::book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original
