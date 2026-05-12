import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ocltutorial_Loans,
    ocltutorial_Member,
    ocltutorial_Book,
    ocltutorial_Library,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ocltutorial_loans_is_not_abstract():
    assert not inspect.isabstract(ocltutorial_Loans)


def test_ocltutorial_loans_constructor_exists():
    assert callable(ocltutorial_Loans.__init__)


def test_ocltutorial_loans_constructor_args():
    sig = inspect.signature(ocltutorial_Loans.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"

def test_ocltutorial_loans_has_date():
    assert hasattr(ocltutorial_Loans, "date")
    descriptor = None
    for klass in ocltutorial_Loans.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)



def test_ocltutorial_member_is_not_abstract():
    assert not inspect.isabstract(ocltutorial_Member)


def test_ocltutorial_member_constructor_exists():
    assert callable(ocltutorial_Member.__init__)


def test_ocltutorial_member_constructor_args():
    sig = inspect.signature(ocltutorial_Member.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocltutorial_member_has_name():
    assert hasattr(ocltutorial_Member, "name")
    descriptor = None
    for klass in ocltutorial_Member.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocltutorial_book_is_not_abstract():
    assert not inspect.isabstract(ocltutorial_Book)


def test_ocltutorial_book_constructor_exists():
    assert callable(ocltutorial_Book.__init__)


def test_ocltutorial_book_constructor_args():
    sig = inspect.signature(ocltutorial_Book.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "copies" in params, "Missing parameter 'copies'"

def test_ocltutorial_book_has_name():
    assert hasattr(ocltutorial_Book, "name")
    descriptor = None
    for klass in ocltutorial_Book.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ocltutorial_book_has_copies():
    assert hasattr(ocltutorial_Book, "copies")
    descriptor = None
    for klass in ocltutorial_Book.__mro__:
        if "copies" in klass.__dict__:
            descriptor = klass.__dict__["copies"]
            break
    assert isinstance(descriptor, property)



def test_ocltutorial_library_is_not_abstract():
    assert not inspect.isabstract(ocltutorial_Library)


def test_ocltutorial_library_constructor_exists():
    assert callable(ocltutorial_Library.__init__)


def test_ocltutorial_library_constructor_args():
    sig = inspect.signature(ocltutorial_Library.__init__)
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
ocltutorial_Loans_strategy = st.builds(
    ocltutorial_Loans,
    date=
        st.dates()
)
ocltutorial_Member_strategy = st.builds(
    ocltutorial_Member,
    name=
        safe_text
)
ocltutorial_Book_strategy = st.builds(
    ocltutorial_Book,
    name=
        safe_text,
    copies=
        safe_text
)
ocltutorial_Library_strategy = st.builds(
    ocltutorial_Library,
)

@given(instance=ocltutorial_Loans_strategy)
@settings(max_examples=50)
def test_ocltutorial_loans_instantiation(instance):
    assert isinstance(instance, ocltutorial_Loans)



@given(instance=ocltutorial_Loans_strategy)
def test_ocltutorial_loans_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=ocltutorial_Member_strategy)
@settings(max_examples=50)
def test_ocltutorial_member_instantiation(instance):
    assert isinstance(instance, ocltutorial_Member)



@given(instance=ocltutorial_Member_strategy)
def test_ocltutorial_member_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ocltutorial_Book_strategy)
@settings(max_examples=50)
def test_ocltutorial_book_instantiation(instance):
    assert isinstance(instance, ocltutorial_Book)



@given(instance=ocltutorial_Book_strategy)
def test_ocltutorial_book_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ocltutorial_Book_strategy)
def test_ocltutorial_book_copies_setter(instance):
    original = instance.copies
    instance.copies = original
    assert instance.copies == original

@given(instance=ocltutorial_Library_strategy)
@settings(max_examples=50)
def test_ocltutorial_library_instantiation(instance):
    assert isinstance(instance, ocltutorial_Library)
