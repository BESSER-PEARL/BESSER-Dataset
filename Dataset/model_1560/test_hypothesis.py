import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Paper::Paper,
    Paper::Papers,
    Paper::Author,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_paper::author_is_not_abstract():
    assert not inspect.isabstract(Paper::Author)


def test_paper::author_constructor_exists():
    assert callable(Paper::Author.__init__)


def test_paper::author_constructor_args():
    sig = inspect.signature(Paper::Author.__init__)
    params = list(sig.parameters.keys())
    assert "firstname" in params, "Missing parameter 'firstname'"
    assert "lastname" in params, "Missing parameter 'lastname'"
    assert "email" in params, "Missing parameter 'email'"

def test_paper::author_has_firstname():
    assert hasattr(Paper::Author, "firstname")
    descriptor = None
    for klass in Paper::Author.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
            break
    assert isinstance(descriptor, property)

def test_paper::author_has_lastname():
    assert hasattr(Paper::Author, "lastname")
    descriptor = None
    for klass in Paper::Author.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
            break
    assert isinstance(descriptor, property)

def test_paper::author_has_email():
    assert hasattr(Paper::Author, "email")
    descriptor = None
    for klass in Paper::Author.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
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
Paper::Paper_strategy = st.builds(
    Paper::Paper,
    title=
        safe_text
)
Paper::Papers_strategy = st.builds(
    Paper::Papers,
)
Paper::Author_strategy = st.builds(
    Paper::Author,
    firstname=
        safe_text,
    lastname=
        safe_text,
    email=
        safe_text
)

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

@given(instance=Paper::Author_strategy)
@settings(max_examples=50)
def test_paper::author_instantiation(instance):
    assert isinstance(instance, Paper::Author)

@given(instance=Paper::Author_strategy)
def test_paper::author_firstname_type(instance):
    assert isinstance(instance.firstname, str)


@given(instance=Paper::Author_strategy)
def test_paper::author_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original

@given(instance=Paper::Author_strategy)
def test_paper::author_lastname_type(instance):
    assert isinstance(instance.lastname, str)


@given(instance=Paper::Author_strategy)
def test_paper::author_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original

@given(instance=Paper::Author_strategy)
def test_paper::author_email_type(instance):
    assert isinstance(instance.email, str)


@given(instance=Paper::Author_strategy)
def test_paper::author_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original
