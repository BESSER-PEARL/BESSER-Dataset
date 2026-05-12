import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Bibtex::Entry,
    Bibtex::Author,
    Bibtex::LiteratureDb,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_bibtex::entry_is_not_abstract():
    assert not inspect.isabstract(Bibtex::Entry)


def test_bibtex::entry_constructor_exists():
    assert callable(Bibtex::Entry.__init__)


def test_bibtex::entry_constructor_args():
    sig = inspect.signature(Bibtex::Entry.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "title" in params, "Missing parameter 'title'"

def test_bibtex::entry_has_id():
    assert hasattr(Bibtex::Entry, "id")
    descriptor = None
    for klass in Bibtex::Entry.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_bibtex::entry_has_title():
    assert hasattr(Bibtex::Entry, "title")
    descriptor = None
    for klass in Bibtex::Entry.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_bibtex::author_is_not_abstract():
    assert not inspect.isabstract(Bibtex::Author)


def test_bibtex::author_constructor_exists():
    assert callable(Bibtex::Author.__init__)


def test_bibtex::author_constructor_args():
    sig = inspect.signature(Bibtex::Author.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bibtex::author_has_name():
    assert hasattr(Bibtex::Author, "name")
    descriptor = None
    for klass in Bibtex::Author.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bibtex::literaturedb_is_not_abstract():
    assert not inspect.isabstract(Bibtex::LiteratureDb)


def test_bibtex::literaturedb_constructor_exists():
    assert callable(Bibtex::LiteratureDb.__init__)


def test_bibtex::literaturedb_constructor_args():
    sig = inspect.signature(Bibtex::LiteratureDb.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bibtex::literaturedb_has_name():
    assert hasattr(Bibtex::LiteratureDb, "name")
    descriptor = None
    for klass in Bibtex::LiteratureDb.__mro__:
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
Bibtex::Entry_strategy = st.builds(
    Bibtex::Entry,
    id=
        safe_text,
    title=
        safe_text
)
Bibtex::Author_strategy = st.builds(
    Bibtex::Author,
    name=
        safe_text
)
Bibtex::LiteratureDb_strategy = st.builds(
    Bibtex::LiteratureDb,
    name=
        safe_text
)

@given(instance=Bibtex::Entry_strategy)
@settings(max_examples=50)
def test_bibtex::entry_instantiation(instance):
    assert isinstance(instance, Bibtex::Entry)

@given(instance=Bibtex::Entry_strategy)
def test_bibtex::entry_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=Bibtex::Entry_strategy)
def test_bibtex::entry_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Bibtex::Entry_strategy)
def test_bibtex::entry_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=Bibtex::Entry_strategy)
def test_bibtex::entry_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=Bibtex::Author_strategy)
@settings(max_examples=50)
def test_bibtex::author_instantiation(instance):
    assert isinstance(instance, Bibtex::Author)

@given(instance=Bibtex::Author_strategy)
def test_bibtex::author_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Bibtex::Author_strategy)
def test_bibtex::author_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Bibtex::LiteratureDb_strategy)
@settings(max_examples=50)
def test_bibtex::literaturedb_instantiation(instance):
    assert isinstance(instance, Bibtex::LiteratureDb)

@given(instance=Bibtex::LiteratureDb_strategy)
def test_bibtex::literaturedb_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Bibtex::LiteratureDb_strategy)
def test_bibtex::literaturedb_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
