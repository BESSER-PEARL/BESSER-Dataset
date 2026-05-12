import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Paper_Paper,
    Paper_Papers,
    Paper_Author,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_paper_paper_is_not_abstract():
    assert not inspect.isabstract(Paper_Paper)


def test_paper_paper_constructor_exists():
    assert callable(Paper_Paper.__init__)


def test_paper_paper_constructor_args():
    sig = inspect.signature(Paper_Paper.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_paper_paper_has_title():
    assert hasattr(Paper_Paper, "title")
    descriptor = None
    for klass in Paper_Paper.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_paper_papers_is_not_abstract():
    assert not inspect.isabstract(Paper_Papers)


def test_paper_papers_constructor_exists():
    assert callable(Paper_Papers.__init__)


def test_paper_papers_constructor_args():
    sig = inspect.signature(Paper_Papers.__init__)
    params = list(sig.parameters.keys())



def test_paper_author_is_not_abstract():
    assert not inspect.isabstract(Paper_Author)


def test_paper_author_constructor_exists():
    assert callable(Paper_Author.__init__)


def test_paper_author_constructor_args():
    sig = inspect.signature(Paper_Author.__init__)
    params = list(sig.parameters.keys())
    assert "email" in params, "Missing parameter 'email'"
    assert "firstname" in params, "Missing parameter 'firstname'"
    assert "lastname" in params, "Missing parameter 'lastname'"

def test_paper_author_has_email():
    assert hasattr(Paper_Author, "email")
    descriptor = None
    for klass in Paper_Author.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_paper_author_has_firstname():
    assert hasattr(Paper_Author, "firstname")
    descriptor = None
    for klass in Paper_Author.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
            break
    assert isinstance(descriptor, property)

def test_paper_author_has_lastname():
    assert hasattr(Paper_Author, "lastname")
    descriptor = None
    for klass in Paper_Author.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
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
Paper_Paper_strategy = st.builds(
    Paper_Paper,
    title=
        safe_text
)
Paper_Papers_strategy = st.builds(
    Paper_Papers,
)
Paper_Author_strategy = st.builds(
    Paper_Author,
    email=
        safe_text,
    firstname=
        safe_text,
    lastname=
        safe_text
)

@given(instance=Paper_Paper_strategy)
@settings(max_examples=50)
def test_paper_paper_instantiation(instance):
    assert isinstance(instance, Paper_Paper)



@given(instance=Paper_Paper_strategy)
def test_paper_paper_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=Paper_Papers_strategy)
@settings(max_examples=50)
def test_paper_papers_instantiation(instance):
    assert isinstance(instance, Paper_Papers)

@given(instance=Paper_Author_strategy)
@settings(max_examples=50)
def test_paper_author_instantiation(instance):
    assert isinstance(instance, Paper_Author)



@given(instance=Paper_Author_strategy)
def test_paper_author_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Paper_Author_strategy)
def test_paper_author_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original



@given(instance=Paper_Author_strategy)
def test_paper_author_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original
