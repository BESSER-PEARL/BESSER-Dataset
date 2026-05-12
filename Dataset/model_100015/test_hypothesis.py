import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    bibtex::Document,
    bibtex::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_bibtex::document_is_not_abstract():
    assert not inspect.isabstract(bibtex::Document)


def test_bibtex::document_constructor_exists():
    assert callable(bibtex::Document.__init__)


def test_bibtex::document_constructor_args():
    sig = inspect.signature(bibtex::Document.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "unparsedAuthors" in params, "Missing parameter 'unparsedAuthors'"
    assert "title" in params, "Missing parameter 'title'"
    assert "year" in params, "Missing parameter 'year'"
    assert "doi" in params, "Missing parameter 'doi'"
    assert "month" in params, "Missing parameter 'month'"
    assert "url" in params, "Missing parameter 'url'"
    assert "abstract" in params, "Missing parameter 'abstract'"
    assert "authors" in params, "Missing parameter 'authors'"
    assert "key" in params, "Missing parameter 'key'"
    assert "file" in params, "Missing parameter 'file'"
    assert "cites" in params, "Missing parameter 'cites'"

def test_bibtex::document_has_type():
    assert hasattr(bibtex::Document, "type")
    descriptor = None
    for klass in bibtex::Document.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_bibtex::document_has_unparsedAuthors():
    assert hasattr(bibtex::Document, "unparsedAuthors")
    descriptor = None
    for klass in bibtex::Document.__mro__:
        if "unparsedAuthors" in klass.__dict__:
            descriptor = klass.__dict__["unparsedAuthors"]
            break
    assert isinstance(descriptor, property)

def test_bibtex::document_has_title():
    assert hasattr(bibtex::Document, "title")
    descriptor = None
    for klass in bibtex::Document.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_bibtex::document_has_year():
    assert hasattr(bibtex::Document, "year")
    descriptor = None
    for klass in bibtex::Document.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_bibtex::document_has_doi():
    assert hasattr(bibtex::Document, "doi")
    descriptor = None
    for klass in bibtex::Document.__mro__:
        if "doi" in klass.__dict__:
            descriptor = klass.__dict__["doi"]
            break
    assert isinstance(descriptor, property)

def test_bibtex::document_has_month():
    assert hasattr(bibtex::Document, "month")
    descriptor = None
    for klass in bibtex::Document.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)

def test_bibtex::document_has_url():
    assert hasattr(bibtex::Document, "url")
    descriptor = None
    for klass in bibtex::Document.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_bibtex::document_has_abstract():
    assert hasattr(bibtex::Document, "abstract")
    descriptor = None
    for klass in bibtex::Document.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)

def test_bibtex::document_has_authors():
    assert hasattr(bibtex::Document, "authors")
    descriptor = None
    for klass in bibtex::Document.__mro__:
        if "authors" in klass.__dict__:
            descriptor = klass.__dict__["authors"]
            break
    assert isinstance(descriptor, property)

def test_bibtex::document_has_key():
    assert hasattr(bibtex::Document, "key")
    descriptor = None
    for klass in bibtex::Document.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_bibtex::document_has_file():
    assert hasattr(bibtex::Document, "file")
    descriptor = None
    for klass in bibtex::Document.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)

def test_bibtex::document_has_cites():
    assert hasattr(bibtex::Document, "cites")
    descriptor = None
    for klass in bibtex::Document.__mro__:
        if "cites" in klass.__dict__:
            descriptor = klass.__dict__["cites"]
            break
    assert isinstance(descriptor, property)



def test_bibtex::model_is_not_abstract():
    assert not inspect.isabstract(bibtex::Model)


def test_bibtex::model_constructor_exists():
    assert callable(bibtex::Model.__init__)


def test_bibtex::model_constructor_args():
    sig = inspect.signature(bibtex::Model.__init__)
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
bibtex::Document_strategy = st.builds(
    bibtex::Document,
    type=
        safe_text,
    unparsedAuthors=
        safe_text,
    title=
        safe_text,
    year=
        safe_text,
    doi=
        safe_text,
    month=
        safe_text,
    url=
        safe_text,
    abstract=
        safe_text,
    authors=
        safe_text,
    key=
        safe_text,
    file=
        safe_text,
    cites=
        st.integers()
)
bibtex::Model_strategy = st.builds(
    bibtex::Model,
)

@given(instance=bibtex::Document_strategy)
@settings(max_examples=50)
def test_bibtex::document_instantiation(instance):
    assert isinstance(instance, bibtex::Document)

@given(instance=bibtex::Document_strategy)
def test_bibtex::document_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=bibtex::Document_strategy)
def test_bibtex::document_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=bibtex::Document_strategy)
def test_bibtex::document_unparsedAuthors_type(instance):
    assert isinstance(instance.unparsedAuthors, str)


@given(instance=bibtex::Document_strategy)
def test_bibtex::document_unparsedAuthors_setter(instance):
    original = instance.unparsedAuthors
    instance.unparsedAuthors = original
    assert instance.unparsedAuthors == original

@given(instance=bibtex::Document_strategy)
def test_bibtex::document_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=bibtex::Document_strategy)
def test_bibtex::document_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=bibtex::Document_strategy)
def test_bibtex::document_year_type(instance):
    assert isinstance(instance.year, str)


@given(instance=bibtex::Document_strategy)
def test_bibtex::document_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=bibtex::Document_strategy)
def test_bibtex::document_doi_type(instance):
    assert isinstance(instance.doi, str)


@given(instance=bibtex::Document_strategy)
def test_bibtex::document_doi_setter(instance):
    original = instance.doi
    instance.doi = original
    assert instance.doi == original

@given(instance=bibtex::Document_strategy)
def test_bibtex::document_month_type(instance):
    assert isinstance(instance.month, str)


@given(instance=bibtex::Document_strategy)
def test_bibtex::document_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original

@given(instance=bibtex::Document_strategy)
def test_bibtex::document_url_type(instance):
    assert isinstance(instance.url, str)


@given(instance=bibtex::Document_strategy)
def test_bibtex::document_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=bibtex::Document_strategy)
def test_bibtex::document_abstract_type(instance):
    assert isinstance(instance.abstract, str)


@given(instance=bibtex::Document_strategy)
def test_bibtex::document_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=bibtex::Document_strategy)
def test_bibtex::document_authors_type(instance):
    assert isinstance(instance.authors, str)


@given(instance=bibtex::Document_strategy)
def test_bibtex::document_authors_setter(instance):
    original = instance.authors
    instance.authors = original
    assert instance.authors == original

@given(instance=bibtex::Document_strategy)
def test_bibtex::document_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=bibtex::Document_strategy)
def test_bibtex::document_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=bibtex::Document_strategy)
def test_bibtex::document_file_type(instance):
    assert isinstance(instance.file, str)


@given(instance=bibtex::Document_strategy)
def test_bibtex::document_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=bibtex::Document_strategy)
def test_bibtex::document_cites_type(instance):
    assert isinstance(instance.cites, int)


@given(instance=bibtex::Document_strategy)
def test_bibtex::document_cites_setter(instance):
    original = instance.cites
    instance.cites = original
    assert instance.cites == original

@given(instance=bibtex::Model_strategy)
@settings(max_examples=50)
def test_bibtex::model_instantiation(instance):
    assert isinstance(instance, bibtex::Model)
