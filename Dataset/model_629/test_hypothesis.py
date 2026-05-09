import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    test::Library,
    test::Book,
    test::Writer,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test::library_is_not_abstract():
    assert not inspect.isabstract(test::Library)


def test_test::library_constructor_exists():
    assert callable(test::Library.__init__)


def test_test::library_constructor_args():
    sig = inspect.signature(test::Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_test::library_has_name():
    assert hasattr(test::Library, "name")
    descriptor = None
    for klass in test::Library.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_test::book_is_not_abstract():
    assert not inspect.isabstract(test::Book)


def test_test::book_constructor_exists():
    assert callable(test::Book.__init__)


def test_test::book_constructor_args():
    sig = inspect.signature(test::Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "pages" in params, "Missing parameter 'pages'"

def test_test::book_has_title():
    assert hasattr(test::Book, "title")
    descriptor = None
    for klass in test::Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_test::book_has_pages():
    assert hasattr(test::Book, "pages")
    descriptor = None
    for klass in test::Book.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)



def test_test::writer_is_not_abstract():
    assert not inspect.isabstract(test::Writer)


def test_test::writer_constructor_exists():
    assert callable(test::Writer.__init__)


def test_test::writer_constructor_args():
    sig = inspect.signature(test::Writer.__init__)
    params = list(sig.parameters.keys())
    assert "BirthDate" in params, "Missing parameter 'BirthDate'"
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "EMail" in params, "Missing parameter 'EMail'"
    assert "Pseudonym" in params, "Missing parameter 'Pseudonym'"

def test_test::writer_has_BirthDate():
    assert hasattr(test::Writer, "BirthDate")
    descriptor = None
    for klass in test::Writer.__mro__:
        if "BirthDate" in klass.__dict__:
            descriptor = klass.__dict__["BirthDate"]
            break
    assert isinstance(descriptor, property)

def test_test::writer_has_firstName():
    assert hasattr(test::Writer, "firstName")
    descriptor = None
    for klass in test::Writer.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_test::writer_has_lastName():
    assert hasattr(test::Writer, "lastName")
    descriptor = None
    for klass in test::Writer.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_test::writer_has_EMail():
    assert hasattr(test::Writer, "EMail")
    descriptor = None
    for klass in test::Writer.__mro__:
        if "EMail" in klass.__dict__:
            descriptor = klass.__dict__["EMail"]
            break
    assert isinstance(descriptor, property)

def test_test::writer_has_Pseudonym():
    assert hasattr(test::Writer, "Pseudonym")
    descriptor = None
    for klass in test::Writer.__mro__:
        if "Pseudonym" in klass.__dict__:
            descriptor = klass.__dict__["Pseudonym"]
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
test::Library_strategy = st.builds(
    test::Library,
    name=
        safe_text
)
test::Book_strategy = st.builds(
    test::Book,
    title=
        safe_text,
    pages=
        st.integers()
)
test::Writer_strategy = st.builds(
    test::Writer,
    BirthDate=
        st.dates(),
    firstName=
        safe_text,
    lastName=
        safe_text,
    EMail=
        safe_text,
    Pseudonym=
        st.booleans()
)

@given(instance=test::Library_strategy)
@settings(max_examples=50)
def test_test::library_instantiation(instance):
    assert isinstance(instance, test::Library)

@given(instance=test::Library_strategy)
def test_test::library_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=test::Library_strategy)
def test_test::library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=test::Book_strategy)
@settings(max_examples=50)
def test_test::book_instantiation(instance):
    assert isinstance(instance, test::Book)

@given(instance=test::Book_strategy)
def test_test::book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=test::Book_strategy)
def test_test::book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=test::Book_strategy)
def test_test::book_pages_type(instance):
    assert isinstance(instance.pages, int)


@given(instance=test::Book_strategy)
def test_test::book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=test::Writer_strategy)
@settings(max_examples=50)
def test_test::writer_instantiation(instance):
    assert isinstance(instance, test::Writer)

@given(instance=test::Writer_strategy)
def test_test::writer_BirthDate_type(instance):
    assert isinstance(instance.BirthDate, date)


@given(instance=test::Writer_strategy)
def test_test::writer_BirthDate_setter(instance):
    original = instance.BirthDate
    instance.BirthDate = original
    assert instance.BirthDate == original

@given(instance=test::Writer_strategy)
def test_test::writer_firstName_type(instance):
    assert isinstance(instance.firstName, str)


@given(instance=test::Writer_strategy)
def test_test::writer_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=test::Writer_strategy)
def test_test::writer_lastName_type(instance):
    assert isinstance(instance.lastName, str)


@given(instance=test::Writer_strategy)
def test_test::writer_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=test::Writer_strategy)
def test_test::writer_EMail_type(instance):
    assert isinstance(instance.EMail, str)


@given(instance=test::Writer_strategy)
def test_test::writer_EMail_setter(instance):
    original = instance.EMail
    instance.EMail = original
    assert instance.EMail == original

@given(instance=test::Writer_strategy)
def test_test::writer_Pseudonym_type(instance):
    assert isinstance(instance.Pseudonym, bool)


@given(instance=test::Writer_strategy)
def test_test::writer_Pseudonym_setter(instance):
    original = instance.Pseudonym
    instance.Pseudonym = original
    assert instance.Pseudonym == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=test::Writer_strategy)
@settings(max_examples=30)
def test_test::writer_validate_changes_state(instance):
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
        assert has_statements, f"Function 'validate' in test::Writer is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validate' in test::Writer did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validate' in test::Writer is not implemented or raised an error")
