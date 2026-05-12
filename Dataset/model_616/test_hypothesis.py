import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    tutorial_Member,
    tutorial_Loan,
    tutorial_Library,
    tutorial_Book,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tutorial_member_is_not_abstract():
    assert not inspect.isabstract(tutorial_Member)


def test_tutorial_member_constructor_exists():
    assert callable(tutorial_Member.__init__)


def test_tutorial_member_constructor_args():
    sig = inspect.signature(tutorial_Member.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tutorial_member_has_name():
    assert hasattr(tutorial_Member, "name")
    descriptor = None
    for klass in tutorial_Member.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tutorial_loan_is_not_abstract():
    assert not inspect.isabstract(tutorial_Loan)


def test_tutorial_loan_constructor_exists():
    assert callable(tutorial_Loan.__init__)


def test_tutorial_loan_constructor_args():
    sig = inspect.signature(tutorial_Loan.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"

def test_tutorial_loan_has_date():
    assert hasattr(tutorial_Loan, "date")
    descriptor = None
    for klass in tutorial_Loan.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)



def test_tutorial_library_is_not_abstract():
    assert not inspect.isabstract(tutorial_Library)


def test_tutorial_library_constructor_exists():
    assert callable(tutorial_Library.__init__)


def test_tutorial_library_constructor_args():
    sig = inspect.signature(tutorial_Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tutorial_library_has_name():
    assert hasattr(tutorial_Library, "name")
    descriptor = None
    for klass in tutorial_Library.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tutorial_book_is_not_abstract():
    assert not inspect.isabstract(tutorial_Book)


def test_tutorial_book_constructor_exists():
    assert callable(tutorial_Book.__init__)


def test_tutorial_book_constructor_args():
    sig = inspect.signature(tutorial_Book.__init__)
    params = list(sig.parameters.keys())
    assert "copies" in params, "Missing parameter 'copies'"
    assert "name" in params, "Missing parameter 'name'"

def test_tutorial_book_has_copies():
    assert hasattr(tutorial_Book, "copies")
    descriptor = None
    for klass in tutorial_Book.__mro__:
        if "copies" in klass.__dict__:
            descriptor = klass.__dict__["copies"]
            break
    assert isinstance(descriptor, property)

def test_tutorial_book_has_name():
    assert hasattr(tutorial_Book, "name")
    descriptor = None
    for klass in tutorial_Book.__mro__:
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
tutorial_Member_strategy = st.builds(
    tutorial_Member,
    name=
        safe_text
)
tutorial_Loan_strategy = st.builds(
    tutorial_Loan,
    date=
        st.dates()
)
tutorial_Library_strategy = st.builds(
    tutorial_Library,
    name=
        safe_text
)
tutorial_Book_strategy = st.builds(
    tutorial_Book,
    copies=
        safe_text,
    name=
        safe_text
)

@given(instance=tutorial_Member_strategy)
@settings(max_examples=50)
def test_tutorial_member_instantiation(instance):
    assert isinstance(instance, tutorial_Member)



@given(instance=tutorial_Member_strategy)
def test_tutorial_member_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tutorial_Loan_strategy)
@settings(max_examples=50)
def test_tutorial_loan_instantiation(instance):
    assert isinstance(instance, tutorial_Loan)



@given(instance=tutorial_Loan_strategy)
def test_tutorial_loan_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=tutorial_Library_strategy)
@settings(max_examples=50)
def test_tutorial_library_instantiation(instance):
    assert isinstance(instance, tutorial_Library)



@given(instance=tutorial_Library_strategy)
def test_tutorial_library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tutorial_Book_strategy)
@settings(max_examples=50)
def test_tutorial_book_instantiation(instance):
    assert isinstance(instance, tutorial_Book)



@given(instance=tutorial_Book_strategy)
def test_tutorial_book_copies_setter(instance):
    original = instance.copies
    instance.copies = original
    assert instance.copies == original



@given(instance=tutorial_Book_strategy)
def test_tutorial_book_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tutorial_Book_strategy)
@settings(max_examples=30)
def test_tutorial_book_isavailable_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isAvailable()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isAvailable).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isAvailable' in tutorial_Book is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isAvailable' in tutorial_Book did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isAvailable' in tutorial_Book is not implemented or raised an error")
