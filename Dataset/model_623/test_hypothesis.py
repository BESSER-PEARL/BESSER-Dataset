import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ocltutorial::Loans,
    ocltutorial::Member,
    ocltutorial::Book,
    ocltutorial::Library,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ocltutorial::loans_is_not_abstract():
    assert not inspect.isabstract(ocltutorial::Loans)


def test_ocltutorial::loans_constructor_exists():
    assert callable(ocltutorial::Loans.__init__)


def test_ocltutorial::loans_constructor_args():
    sig = inspect.signature(ocltutorial::Loans.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"

def test_ocltutorial::loans_has_date():
    assert hasattr(ocltutorial::Loans, "date")
    descriptor = None
    for klass in ocltutorial::Loans.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)



def test_ocltutorial::member_is_not_abstract():
    assert not inspect.isabstract(ocltutorial::Member)


def test_ocltutorial::member_constructor_exists():
    assert callable(ocltutorial::Member.__init__)


def test_ocltutorial::member_constructor_args():
    sig = inspect.signature(ocltutorial::Member.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocltutorial::member_has_name():
    assert hasattr(ocltutorial::Member, "name")
    descriptor = None
    for klass in ocltutorial::Member.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocltutorial::book_is_not_abstract():
    assert not inspect.isabstract(ocltutorial::Book)


def test_ocltutorial::book_constructor_exists():
    assert callable(ocltutorial::Book.__init__)


def test_ocltutorial::book_constructor_args():
    sig = inspect.signature(ocltutorial::Book.__init__)
    params = list(sig.parameters.keys())
    assert "copies" in params, "Missing parameter 'copies'"
    assert "name" in params, "Missing parameter 'name'"

def test_ocltutorial::book_has_copies():
    assert hasattr(ocltutorial::Book, "copies")
    descriptor = None
    for klass in ocltutorial::Book.__mro__:
        if "copies" in klass.__dict__:
            descriptor = klass.__dict__["copies"]
            break
    assert isinstance(descriptor, property)

def test_ocltutorial::book_has_name():
    assert hasattr(ocltutorial::Book, "name")
    descriptor = None
    for klass in ocltutorial::Book.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocltutorial::library_is_not_abstract():
    assert not inspect.isabstract(ocltutorial::Library)


def test_ocltutorial::library_constructor_exists():
    assert callable(ocltutorial::Library.__init__)


def test_ocltutorial::library_constructor_args():
    sig = inspect.signature(ocltutorial::Library.__init__)
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
ocltutorial::Loans_strategy = st.builds(
    ocltutorial::Loans,
    date=
        st.dates()
)
ocltutorial::Member_strategy = st.builds(
    ocltutorial::Member,
    name=
        safe_text
)
ocltutorial::Book_strategy = st.builds(
    ocltutorial::Book,
    copies=
        safe_text,
    name=
        safe_text
)
ocltutorial::Library_strategy = st.builds(
    ocltutorial::Library,
)

@given(instance=ocltutorial::Loans_strategy)
@settings(max_examples=50)
def test_ocltutorial::loans_instantiation(instance):
    assert isinstance(instance, ocltutorial::Loans)

@given(instance=ocltutorial::Loans_strategy)
def test_ocltutorial::loans_date_type(instance):
    assert isinstance(instance.date, date)


@given(instance=ocltutorial::Loans_strategy)
def test_ocltutorial::loans_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=ocltutorial::Member_strategy)
@settings(max_examples=50)
def test_ocltutorial::member_instantiation(instance):
    assert isinstance(instance, ocltutorial::Member)

@given(instance=ocltutorial::Member_strategy)
def test_ocltutorial::member_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ocltutorial::Member_strategy)
def test_ocltutorial::member_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ocltutorial::Book_strategy)
@settings(max_examples=50)
def test_ocltutorial::book_instantiation(instance):
    assert isinstance(instance, ocltutorial::Book)

@given(instance=ocltutorial::Book_strategy)
def test_ocltutorial::book_copies_type(instance):
    assert isinstance(instance.copies, str)


@given(instance=ocltutorial::Book_strategy)
def test_ocltutorial::book_copies_setter(instance):
    original = instance.copies
    instance.copies = original
    assert instance.copies == original

@given(instance=ocltutorial::Book_strategy)
def test_ocltutorial::book_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ocltutorial::Book_strategy)
def test_ocltutorial::book_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ocltutorial::Library_strategy)
@settings(max_examples=50)
def test_ocltutorial::library_instantiation(instance):
    assert isinstance(instance, ocltutorial::Library)
