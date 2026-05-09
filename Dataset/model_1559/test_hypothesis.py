import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Paper::Author,
    Paper::Paper,
    Paper::Papers,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_paper::author_is_not_abstract():
    assert not inspect.isabstract(Paper::Author)


def test_paper::author_constructor_exists():
    assert callable(Paper::Author.__init__)


def test_paper::author_constructor_args():
    sig = inspect.signature(Paper::Author.__init__)
    params = list(sig.parameters.keys())
    assert "email" in params, "Missing parameter 'email'"
    assert "name" in params, "Missing parameter 'name'"

def test_paper::author_has_email():
    assert hasattr(Paper::Author, "email")
    descriptor = None
    for klass in Paper::Author.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_paper::author_has_name():
    assert hasattr(Paper::Author, "name")
    descriptor = None
    for klass in Paper::Author.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_paper::paper_is_not_abstract():
    assert not inspect.isabstract(Paper::Paper)


def test_paper::paper_constructor_exists():
    assert callable(Paper::Paper.__init__)


def test_paper::paper_constructor_args():
    sig = inspect.signature(Paper::Paper.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_paper::paper_has_title():
    assert hasattr(Paper::Paper, "title")
    descriptor = None
    for klass in Paper::Paper.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_paper::papers_is_not_abstract():
    assert not inspect.isabstract(Paper::Papers)


def test_paper::papers_constructor_exists():
    assert callable(Paper::Papers.__init__)


def test_paper::papers_constructor_args():
    sig = inspect.signature(Paper::Papers.__init__)
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
Paper::Author_strategy = st.builds(
    Paper::Author,
    email=
        safe_text,
    name=
        safe_text
)
Paper::Paper_strategy = st.builds(
    Paper::Paper,
    title=
        safe_text
)
Paper::Papers_strategy = st.builds(
    Paper::Papers,
)

@given(instance=Paper::Author_strategy)
@settings(max_examples=50)
def test_paper::author_instantiation(instance):
    assert isinstance(instance, Paper::Author)

@given(instance=Paper::Author_strategy)
def test_paper::author_email_type(instance):
    assert isinstance(instance.email, str)


@given(instance=Paper::Author_strategy)
def test_paper::author_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original

@given(instance=Paper::Author_strategy)
def test_paper::author_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Paper::Author_strategy)
def test_paper::author_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Paper::Paper_strategy)
@settings(max_examples=50)
def test_paper::paper_instantiation(instance):
    assert isinstance(instance, Paper::Paper)

@given(instance=Paper::Paper_strategy)
def test_paper::paper_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=Paper::Paper_strategy)
def test_paper::paper_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=Paper::Papers_strategy)
@settings(max_examples=50)
def test_paper::papers_instantiation(instance):
    assert isinstance(instance, Paper::Papers)
