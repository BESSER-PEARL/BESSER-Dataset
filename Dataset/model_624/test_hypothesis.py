import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    mm2::Library,
    mm2::Loan,
    mm2::Book,
    mm2::Member,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mm2::library_is_not_abstract():
    assert not inspect.isabstract(mm2::Library)


def test_mm2::library_constructor_exists():
    assert callable(mm2::Library.__init__)


def test_mm2::library_constructor_args():
    sig = inspect.signature(mm2::Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mm2::library_has_name():
    assert hasattr(mm2::Library, "name")
    descriptor = None
    for klass in mm2::Library.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mm2::loan_is_not_abstract():
    assert not inspect.isabstract(mm2::Loan)


def test_mm2::loan_constructor_exists():
    assert callable(mm2::Loan.__init__)


def test_mm2::loan_constructor_args():
    sig = inspect.signature(mm2::Loan.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mm2::loan_has_name():
    assert hasattr(mm2::Loan, "name")
    descriptor = None
    for klass in mm2::Loan.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mm2::book_is_not_abstract():
    assert not inspect.isabstract(mm2::Book)


def test_mm2::book_constructor_exists():
    assert callable(mm2::Book.__init__)


def test_mm2::book_constructor_args():
    sig = inspect.signature(mm2::Book.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mm2::book_has_name():
    assert hasattr(mm2::Book, "name")
    descriptor = None
    for klass in mm2::Book.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mm2::member_is_not_abstract():
    assert not inspect.isabstract(mm2::Member)


def test_mm2::member_constructor_exists():
    assert callable(mm2::Member.__init__)


def test_mm2::member_constructor_args():
    sig = inspect.signature(mm2::Member.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mm2::member_has_name():
    assert hasattr(mm2::Member, "name")
    descriptor = None
    for klass in mm2::Member.__mro__:
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
mm2::Library_strategy = st.builds(
    mm2::Library,
    name=
        safe_text
)
mm2::Loan_strategy = st.builds(
    mm2::Loan,
    name=
        safe_text
)
mm2::Book_strategy = st.builds(
    mm2::Book,
    name=
        safe_text
)
mm2::Member_strategy = st.builds(
    mm2::Member,
    name=
        safe_text
)

@given(instance=mm2::Library_strategy)
@settings(max_examples=50)
def test_mm2::library_instantiation(instance):
    assert isinstance(instance, mm2::Library)

@given(instance=mm2::Library_strategy)
def test_mm2::library_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mm2::Library_strategy)
def test_mm2::library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mm2::Loan_strategy)
@settings(max_examples=50)
def test_mm2::loan_instantiation(instance):
    assert isinstance(instance, mm2::Loan)

@given(instance=mm2::Loan_strategy)
def test_mm2::loan_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mm2::Loan_strategy)
def test_mm2::loan_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mm2::Book_strategy)
@settings(max_examples=50)
def test_mm2::book_instantiation(instance):
    assert isinstance(instance, mm2::Book)

@given(instance=mm2::Book_strategy)
def test_mm2::book_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mm2::Book_strategy)
def test_mm2::book_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mm2::Member_strategy)
@settings(max_examples=50)
def test_mm2::member_instantiation(instance):
    assert isinstance(instance, mm2::Member)

@given(instance=mm2::Member_strategy)
def test_mm2::member_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mm2::Member_strategy)
def test_mm2::member_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
