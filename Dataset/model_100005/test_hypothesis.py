import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Publication::Publication,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_publication::publication_is_not_abstract():
    assert not inspect.isabstract(Publication::Publication)


def test_publication::publication_constructor_exists():
    assert callable(Publication::Publication.__init__)


def test_publication::publication_constructor_args():
    sig = inspect.signature(Publication::Publication.__init__)
    params = list(sig.parameters.keys())
    assert "authors" in params, "Missing parameter 'authors'"
    assert "title" in params, "Missing parameter 'title'"
    assert "nbPages" in params, "Missing parameter 'nbPages'"

def test_publication::publication_has_authors():
    assert hasattr(Publication::Publication, "authors")
    descriptor = None
    for klass in Publication::Publication.__mro__:
        if "authors" in klass.__dict__:
            descriptor = klass.__dict__["authors"]
            break
    assert isinstance(descriptor, property)

def test_publication::publication_has_title():
    assert hasattr(Publication::Publication, "title")
    descriptor = None
    for klass in Publication::Publication.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_publication::publication_has_nbPages():
    assert hasattr(Publication::Publication, "nbPages")
    descriptor = None
    for klass in Publication::Publication.__mro__:
        if "nbPages" in klass.__dict__:
            descriptor = klass.__dict__["nbPages"]
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
Publication::Publication_strategy = st.builds(
    Publication::Publication,
    authors=
        safe_text,
    title=
        safe_text,
    nbPages=
        safe_text
)

@given(instance=Publication::Publication_strategy)
@settings(max_examples=50)
def test_publication::publication_instantiation(instance):
    assert isinstance(instance, Publication::Publication)

@given(instance=Publication::Publication_strategy)
def test_publication::publication_authors_type(instance):
    assert isinstance(instance.authors, str)


@given(instance=Publication::Publication_strategy)
def test_publication::publication_authors_setter(instance):
    original = instance.authors
    instance.authors = original
    assert instance.authors == original

@given(instance=Publication::Publication_strategy)
def test_publication::publication_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=Publication::Publication_strategy)
def test_publication::publication_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=Publication::Publication_strategy)
def test_publication::publication_nbPages_type(instance):
    assert isinstance(instance.nbPages, str)


@given(instance=Publication::Publication_strategy)
def test_publication::publication_nbPages_setter(instance):
    original = instance.nbPages
    instance.nbPages = original
    assert instance.nbPages == original
