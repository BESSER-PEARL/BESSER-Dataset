import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    tutorial::Member,
    tutorial::Loan,
    tutorial::Book,
    tutorial::Library,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tutorial::member_is_not_abstract():
    assert not inspect.isabstract(tutorial::Member)


def test_tutorial::member_constructor_exists():
    assert callable(tutorial::Member.__init__)


def test_tutorial::member_constructor_args():
    sig = inspect.signature(tutorial::Member.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tutorial::member_has_name():
    assert hasattr(tutorial::Member, "name")
    descriptor = None
    for klass in tutorial::Member.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tutorial::loan_is_not_abstract():
    assert not inspect.isabstract(tutorial::Loan)


def test_tutorial::loan_constructor_exists():
    assert callable(tutorial::Loan.__init__)


def test_tutorial::loan_constructor_args():
    sig = inspect.signature(tutorial::Loan.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"

def test_tutorial::loan_has_date():
    assert hasattr(tutorial::Loan, "date")
    descriptor = None
    for klass in tutorial::Loan.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)



def test_tutorial::book_is_not_abstract():
    assert not inspect.isabstract(tutorial::Book)


def test_tutorial::book_constructor_exists():
    assert callable(tutorial::Book.__init__)


def test_tutorial::book_constructor_args():
    sig = inspect.signature(tutorial::Book.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "copies" in params, "Missing parameter 'copies'"

def test_tutorial::book_has_name():
    assert hasattr(tutorial::Book, "name")
    descriptor = None
    for klass in tutorial::Book.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_tutorial::book_has_copies():
    assert hasattr(tutorial::Book, "copies")
    descriptor = None
    for klass in tutorial::Book.__mro__:
        if "copies" in klass.__dict__:
            descriptor = klass.__dict__["copies"]
            break
    assert isinstance(descriptor, property)



def test_tutorial::library_is_not_abstract():
    assert not inspect.isabstract(tutorial::Library)


def test_tutorial::library_constructor_exists():
    assert callable(tutorial::Library.__init__)


def test_tutorial::library_constructor_args():
    sig = inspect.signature(tutorial::Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tutorial::library_has_name():
    assert hasattr(tutorial::Library, "name")
    descriptor = None
    for klass in tutorial::Library.__mro__:
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
tutorial::Member_strategy = st.builds(
    tutorial::Member,
    name=
        safe_text
)
tutorial::Loan_strategy = st.builds(
    tutorial::Loan,
    date=
        st.dates()
)
tutorial::Book_strategy = st.builds(
    tutorial::Book,
    name=
        safe_text,
    copies=
        safe_text
)
tutorial::Library_strategy = st.builds(
    tutorial::Library,
    name=
        st.booleans()
)

@given(instance=tutorial::Member_strategy)
@settings(max_examples=50)
def test_tutorial::member_instantiation(instance):
    assert isinstance(instance, tutorial::Member)

@given(instance=tutorial::Member_strategy)
def test_tutorial::member_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tutorial::Member_strategy)
def test_tutorial::member_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tutorial::Loan_strategy)
@settings(max_examples=50)
def test_tutorial::loan_instantiation(instance):
    assert isinstance(instance, tutorial::Loan)

@given(instance=tutorial::Loan_strategy)
def test_tutorial::loan_date_type(instance):
    assert isinstance(instance.date, date)


@given(instance=tutorial::Loan_strategy)
def test_tutorial::loan_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=tutorial::Book_strategy)
@settings(max_examples=50)
def test_tutorial::book_instantiation(instance):
    assert isinstance(instance, tutorial::Book)

@given(instance=tutorial::Book_strategy)
def test_tutorial::book_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tutorial::Book_strategy)
def test_tutorial::book_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tutorial::Book_strategy)
def test_tutorial::book_copies_type(instance):
    assert isinstance(instance.copies, str)


@given(instance=tutorial::Book_strategy)
def test_tutorial::book_copies_setter(instance):
    original = instance.copies
    instance.copies = original
    assert instance.copies == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tutorial::Book_strategy)
@settings(max_examples=30)
def test_tutorial::book_isavailable_changes_state(instance):
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
        assert has_statements, f"Function 'isAvailable' in tutorial::Book is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isAvailable' in tutorial::Book did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isAvailable' in tutorial::Book is not implemented or raised an error")

@given(instance=tutorial::Library_strategy)
@settings(max_examples=50)
def test_tutorial::library_instantiation(instance):
    assert isinstance(instance, tutorial::Library)

@given(instance=tutorial::Library_strategy)
def test_tutorial::library_name_type(instance):
    assert isinstance(instance.name, bool)


@given(instance=tutorial::Library_strategy)
def test_tutorial::library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
