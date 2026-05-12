import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Publication_Publication,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_publication_publication_is_not_abstract():
    assert not inspect.isabstract(Publication_Publication)


def test_publication_publication_constructor_exists():
    assert callable(Publication_Publication.__init__)


def test_publication_publication_constructor_args():
    sig = inspect.signature(Publication_Publication.__init__)
    params = list(sig.parameters.keys())
    assert "nbPages" in params, "Missing parameter 'nbPages'"
    assert "authors" in params, "Missing parameter 'authors'"
    assert "title" in params, "Missing parameter 'title'"

def test_publication_publication_has_nbPages():
    assert hasattr(Publication_Publication, "nbPages")
    descriptor = None
    for klass in Publication_Publication.__mro__:
        if "nbPages" in klass.__dict__:
            descriptor = klass.__dict__["nbPages"]
            break
    assert isinstance(descriptor, property)

def test_publication_publication_has_authors():
    assert hasattr(Publication_Publication, "authors")
    descriptor = None
    for klass in Publication_Publication.__mro__:
        if "authors" in klass.__dict__:
            descriptor = klass.__dict__["authors"]
            break
    assert isinstance(descriptor, property)

def test_publication_publication_has_title():
    assert hasattr(Publication_Publication, "title")
    descriptor = None
    for klass in Publication_Publication.__mro__:
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
Publication_Publication_strategy = st.builds(
    Publication_Publication,
    nbPages=
        safe_text,
    authors=
        safe_text,
    title=
        safe_text
)

@given(instance=Publication_Publication_strategy)
@settings(max_examples=50)
def test_publication_publication_instantiation(instance):
    assert isinstance(instance, Publication_Publication)



@given(instance=Publication_Publication_strategy)
def test_publication_publication_nbPages_setter(instance):
    original = instance.nbPages
    instance.nbPages = original
    assert instance.nbPages == original



@given(instance=Publication_Publication_strategy)
def test_publication_publication_authors_setter(instance):
    original = instance.authors
    instance.authors = original
    assert instance.authors == original



@given(instance=Publication_Publication_strategy)
def test_publication_publication_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original
