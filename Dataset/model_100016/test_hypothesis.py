import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Bibtex_Entry,
    Bibtex_Author,
    Bibtex_LiteratureDb,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_bibtex_entry_is_not_abstract():
    assert not inspect.isabstract(Bibtex_Entry)


def test_bibtex_entry_constructor_exists():
    assert callable(Bibtex_Entry.__init__)


def test_bibtex_entry_constructor_args():
    sig = inspect.signature(Bibtex_Entry.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "title" in params, "Missing parameter 'title'"

def test_bibtex_entry_has_id():
    assert hasattr(Bibtex_Entry, "id")
    descriptor = None
    for klass in Bibtex_Entry.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_bibtex_entry_has_title():
    assert hasattr(Bibtex_Entry, "title")
    descriptor = None
    for klass in Bibtex_Entry.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_bibtex_author_is_not_abstract():
    assert not inspect.isabstract(Bibtex_Author)


def test_bibtex_author_constructor_exists():
    assert callable(Bibtex_Author.__init__)


def test_bibtex_author_constructor_args():
    sig = inspect.signature(Bibtex_Author.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bibtex_author_has_name():
    assert hasattr(Bibtex_Author, "name")
    descriptor = None
    for klass in Bibtex_Author.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bibtex_literaturedb_is_not_abstract():
    assert not inspect.isabstract(Bibtex_LiteratureDb)


def test_bibtex_literaturedb_constructor_exists():
    assert callable(Bibtex_LiteratureDb.__init__)


def test_bibtex_literaturedb_constructor_args():
    sig = inspect.signature(Bibtex_LiteratureDb.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bibtex_literaturedb_has_name():
    assert hasattr(Bibtex_LiteratureDb, "name")
    descriptor = None
    for klass in Bibtex_LiteratureDb.__mro__:
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
Bibtex_Entry_strategy = st.builds(
    Bibtex_Entry,
    id=
        safe_text,
    title=
        safe_text
)
Bibtex_Author_strategy = st.builds(
    Bibtex_Author,
    name=
        safe_text
)
Bibtex_LiteratureDb_strategy = st.builds(
    Bibtex_LiteratureDb,
    name=
        safe_text
)

@given(instance=Bibtex_Entry_strategy)
@settings(max_examples=50)
def test_bibtex_entry_instantiation(instance):
    assert isinstance(instance, Bibtex_Entry)



@given(instance=Bibtex_Entry_strategy)
def test_bibtex_entry_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Bibtex_Entry_strategy)
def test_bibtex_entry_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=Bibtex_Author_strategy)
@settings(max_examples=50)
def test_bibtex_author_instantiation(instance):
    assert isinstance(instance, Bibtex_Author)



@given(instance=Bibtex_Author_strategy)
def test_bibtex_author_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Bibtex_LiteratureDb_strategy)
@settings(max_examples=50)
def test_bibtex_literaturedb_instantiation(instance):
    assert isinstance(instance, Bibtex_LiteratureDb)



@given(instance=Bibtex_LiteratureDb_strategy)
def test_bibtex_literaturedb_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
