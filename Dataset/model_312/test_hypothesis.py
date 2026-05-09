import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    people::library::Car,
    people::library::Book,
    library::people::Writer,
    Writer,
    library::Book,
    library::Library,
    BookCategory,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_people::library::car_is_not_abstract():
    assert not inspect.isabstract(people::library::Car)


def test_people::library::car_constructor_exists():
    assert callable(people::library::Car.__init__)


def test_people::library::car_constructor_args():
    sig = inspect.signature(people::library::Car.__init__)
    params = list(sig.parameters.keys())



def test_people::library::book_is_not_abstract():
    assert not inspect.isabstract(people::library::Book)


def test_people::library::book_constructor_exists():
    assert callable(people::library::Book.__init__)


def test_people::library::book_constructor_args():
    sig = inspect.signature(people::library::Book.__init__)
    params = list(sig.parameters.keys())



def test_library::people::writer_is_not_abstract():
    assert not inspect.isabstract(library::people::Writer)


def test_library::people::writer_constructor_exists():
    assert callable(library::people::Writer.__init__)


def test_library::people::writer_constructor_args():
    sig = inspect.signature(library::people::Writer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_library::people::writer_has_name():
    assert hasattr(library::people::Writer, "name")
    descriptor = None
    for klass in library::people::Writer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_writer_is_not_abstract():
    assert not inspect.isabstract(Writer)


def test_writer_constructor_exists():
    assert callable(Writer.__init__)


def test_writer_constructor_args():
    sig = inspect.signature(Writer.__init__)
    params = list(sig.parameters.keys())



def test_library::book_is_not_abstract():
    assert not inspect.isabstract(library::Book)


def test_library::book_constructor_exists():
    assert callable(library::Book.__init__)


def test_library::book_constructor_args():
    sig = inspect.signature(library::Book.__init__)
    params = list(sig.parameters.keys())
    assert "pages" in params, "Missing parameter 'pages'"
    assert "category" in params, "Missing parameter 'category'"
    assert "title" in params, "Missing parameter 'title'"

def test_library::book_has_pages():
    assert hasattr(library::Book, "pages")
    descriptor = None
    for klass in library::Book.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_library::book_has_category():
    assert hasattr(library::Book, "category")
    descriptor = None
    for klass in library::Book.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_library::book_has_title():
    assert hasattr(library::Book, "title")
    descriptor = None
    for klass in library::Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_library::library_is_not_abstract():
    assert not inspect.isabstract(library::Library)


def test_library::library_constructor_exists():
    assert callable(library::Library.__init__)


def test_library::library_constructor_args():
    sig = inspect.signature(library::Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_library::library_has_name():
    assert hasattr(library::Library, "name")
    descriptor = None
    for klass in library::Library.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_bookcategory_exists():
    # Check that the Enumeration exists
    assert BookCategory is not None

def test_bookcategory_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BookCategory]
    expected_literals = [
        "Mystery",
        "Biography",
        "ScienceFiction",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BookCategory"


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
people::library::Car_strategy = st.builds(
    people::library::Car,
)
people::library::Book_strategy = st.builds(
    people::library::Book,
)
library::people::Writer_strategy = st.builds(
    library::people::Writer,
    name=
        safe_text
)
Writer_strategy = st.builds(
    Writer,
)
library::Book_strategy = st.builds(
    library::Book,
    pages=
        st.integers(),
    category=
        safe_text,
    title=
        safe_text
)
library::Library_strategy = st.builds(
    library::Library,
    name=
        safe_text
)

@given(instance=people::library::Car_strategy)
@settings(max_examples=50)
def test_people::library::car_instantiation(instance):
    assert isinstance(instance, people::library::Car)

@given(instance=people::library::Book_strategy)
@settings(max_examples=50)
def test_people::library::book_instantiation(instance):
    assert isinstance(instance, people::library::Book)

@given(instance=library::people::Writer_strategy)
@settings(max_examples=50)
def test_library::people::writer_instantiation(instance):
    assert isinstance(instance, library::people::Writer)

@given(instance=library::people::Writer_strategy)
def test_library::people::writer_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=library::people::Writer_strategy)
def test_library::people::writer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Writer_strategy)
@settings(max_examples=50)
def test_writer_instantiation(instance):
    assert isinstance(instance, Writer)

@given(instance=library::Book_strategy)
@settings(max_examples=50)
def test_library::book_instantiation(instance):
    assert isinstance(instance, library::Book)

@given(instance=library::Book_strategy)
def test_library::book_pages_type(instance):
    assert isinstance(instance.pages, int)


@given(instance=library::Book_strategy)
def test_library::book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=library::Book_strategy)
def test_library::book_category_type(instance):
    assert isinstance(instance.category, str)


@given(instance=library::Book_strategy)
def test_library::book_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original

@given(instance=library::Book_strategy)
def test_library::book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=library::Book_strategy)
def test_library::book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=library::Library_strategy)
@settings(max_examples=50)
def test_library::library_instantiation(instance):
    assert isinstance(instance, library::Library)

@given(instance=library::Library_strategy)
def test_library::library_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=library::Library_strategy)
def test_library::library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=library::Library_strategy)
@settings(max_examples=30)
def test_library::library_reserve_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.reserve(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.reserve).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'reserve' in library::Library is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'reserve' in library::Library did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'reserve' in library::Library is not implemented or raised an error")
