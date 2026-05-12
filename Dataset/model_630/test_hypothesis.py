import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    mm2_Loan,
    mm2_Book,
    mm2_Member,
    mm2_Library,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mm2_loan_is_not_abstract():
    assert not inspect.isabstract(mm2_Loan)


def test_mm2_loan_constructor_exists():
    assert callable(mm2_Loan.__init__)


def test_mm2_loan_constructor_args():
    sig = inspect.signature(mm2_Loan.__init__)
    params = list(sig.parameters.keys())



def test_mm2_book_is_not_abstract():
    assert not inspect.isabstract(mm2_Book)


def test_mm2_book_constructor_exists():
    assert callable(mm2_Book.__init__)


def test_mm2_book_constructor_args():
    sig = inspect.signature(mm2_Book.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mm2_book_has_name():
    assert hasattr(mm2_Book, "name")
    descriptor = None
    for klass in mm2_Book.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mm2_member_is_not_abstract():
    assert not inspect.isabstract(mm2_Member)


def test_mm2_member_constructor_exists():
    assert callable(mm2_Member.__init__)


def test_mm2_member_constructor_args():
    sig = inspect.signature(mm2_Member.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mm2_member_has_name():
    assert hasattr(mm2_Member, "name")
    descriptor = None
    for klass in mm2_Member.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mm2_library_is_not_abstract():
    assert not inspect.isabstract(mm2_Library)


def test_mm2_library_constructor_exists():
    assert callable(mm2_Library.__init__)


def test_mm2_library_constructor_args():
    sig = inspect.signature(mm2_Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mm2_library_has_name():
    assert hasattr(mm2_Library, "name")
    descriptor = None
    for klass in mm2_Library.__mro__:
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
mm2_Loan_strategy = st.builds(
    mm2_Loan,
)
mm2_Book_strategy = st.builds(
    mm2_Book,
    name=
        safe_text
)
mm2_Member_strategy = st.builds(
    mm2_Member,
    name=
        safe_text
)
mm2_Library_strategy = st.builds(
    mm2_Library,
    name=
        safe_text
)

@given(instance=mm2_Loan_strategy)
@settings(max_examples=50)
def test_mm2_loan_instantiation(instance):
    assert isinstance(instance, mm2_Loan)

@given(instance=mm2_Book_strategy)
@settings(max_examples=50)
def test_mm2_book_instantiation(instance):
    assert isinstance(instance, mm2_Book)



@given(instance=mm2_Book_strategy)
def test_mm2_book_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mm2_Member_strategy)
@settings(max_examples=50)
def test_mm2_member_instantiation(instance):
    assert isinstance(instance, mm2_Member)



@given(instance=mm2_Member_strategy)
def test_mm2_member_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mm2_Library_strategy)
@settings(max_examples=50)
def test_mm2_library_instantiation(instance):
    assert isinstance(instance, mm2_Library)



@given(instance=mm2_Library_strategy)
def test_mm2_library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
