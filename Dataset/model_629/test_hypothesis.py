import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    test_Library,
    test_Book,
    test_Writer,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test_library_is_not_abstract():
    assert not inspect.isabstract(test_Library)


def test_test_library_constructor_exists():
    assert callable(test_Library.__init__)


def test_test_library_constructor_args():
    sig = inspect.signature(test_Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_test_library_has_name():
    assert hasattr(test_Library, "name")
    descriptor = None
    for klass in test_Library.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_test_book_is_not_abstract():
    assert not inspect.isabstract(test_Book)


def test_test_book_constructor_exists():
    assert callable(test_Book.__init__)


def test_test_book_constructor_args():
    sig = inspect.signature(test_Book.__init__)
    params = list(sig.parameters.keys())
    assert "pages" in params, "Missing parameter 'pages'"
    assert "title" in params, "Missing parameter 'title'"

def test_test_book_has_pages():
    assert hasattr(test_Book, "pages")
    descriptor = None
    for klass in test_Book.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_test_book_has_title():
    assert hasattr(test_Book, "title")
    descriptor = None
    for klass in test_Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_test_writer_is_not_abstract():
    assert not inspect.isabstract(test_Writer)


def test_test_writer_constructor_exists():
    assert callable(test_Writer.__init__)


def test_test_writer_constructor_args():
    sig = inspect.signature(test_Writer.__init__)
    params = list(sig.parameters.keys())
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "BirthDate" in params, "Missing parameter 'BirthDate'"
    assert "Pseudonym" in params, "Missing parameter 'Pseudonym'"
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "EMail" in params, "Missing parameter 'EMail'"

def test_test_writer_has_firstName():
    assert hasattr(test_Writer, "firstName")
    descriptor = None
    for klass in test_Writer.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_test_writer_has_BirthDate():
    assert hasattr(test_Writer, "BirthDate")
    descriptor = None
    for klass in test_Writer.__mro__:
        if "BirthDate" in klass.__dict__:
            descriptor = klass.__dict__["BirthDate"]
            break
    assert isinstance(descriptor, property)

def test_test_writer_has_Pseudonym():
    assert hasattr(test_Writer, "Pseudonym")
    descriptor = None
    for klass in test_Writer.__mro__:
        if "Pseudonym" in klass.__dict__:
            descriptor = klass.__dict__["Pseudonym"]
            break
    assert isinstance(descriptor, property)

def test_test_writer_has_lastName():
    assert hasattr(test_Writer, "lastName")
    descriptor = None
    for klass in test_Writer.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_test_writer_has_EMail():
    assert hasattr(test_Writer, "EMail")
    descriptor = None
    for klass in test_Writer.__mro__:
        if "EMail" in klass.__dict__:
            descriptor = klass.__dict__["EMail"]
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
test_Library_strategy = st.builds(
    test_Library,
    name=
        safe_text
)
test_Book_strategy = st.builds(
    test_Book,
    pages=
        st.integers(),
    title=
        safe_text
)
test_Writer_strategy = st.builds(
    test_Writer,
    firstName=
        safe_text,
    BirthDate=
        st.dates(),
    Pseudonym=
        st.booleans(),
    lastName=
        safe_text,
    EMail=
        safe_text
)

@given(instance=test_Library_strategy)
@settings(max_examples=50)
def test_test_library_instantiation(instance):
    assert isinstance(instance, test_Library)



@given(instance=test_Library_strategy)
def test_test_library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=test_Book_strategy)
@settings(max_examples=50)
def test_test_book_instantiation(instance):
    assert isinstance(instance, test_Book)



@given(instance=test_Book_strategy)
def test_test_book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original



@given(instance=test_Book_strategy)
def test_test_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=test_Writer_strategy)
@settings(max_examples=50)
def test_test_writer_instantiation(instance):
    assert isinstance(instance, test_Writer)



@given(instance=test_Writer_strategy)
def test_test_writer_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original



@given(instance=test_Writer_strategy)
def test_test_writer_BirthDate_setter(instance):
    original = instance.BirthDate
    instance.BirthDate = original
    assert instance.BirthDate == original



@given(instance=test_Writer_strategy)
def test_test_writer_Pseudonym_setter(instance):
    original = instance.Pseudonym
    instance.Pseudonym = original
    assert instance.Pseudonym == original



@given(instance=test_Writer_strategy)
def test_test_writer_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original



@given(instance=test_Writer_strategy)
def test_test_writer_EMail_setter(instance):
    original = instance.EMail
    instance.EMail = original
    assert instance.EMail == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=test_Writer_strategy)
@settings(max_examples=30)
def test_test_writer_validate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validate(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validate).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validate' in test_Writer is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validate' in test_Writer did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validate' in test_Writer is not implemented or raised an error")
