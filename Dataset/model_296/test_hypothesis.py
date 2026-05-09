import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    library::Review,
    library::Opinion,
    library::Book,
    library::Writer,
    library::Library,
    BookCategory,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_library::review_is_not_abstract():
    assert not inspect.isabstract(library::Review)


def test_library::review_constructor_exists():
    assert callable(library::Review.__init__)


def test_library::review_constructor_args():
    sig = inspect.signature(library::Review.__init__)
    params = list(sig.parameters.keys())
    assert "positive" in params, "Missing parameter 'positive'"
    assert "title" in params, "Missing parameter 'title'"

def test_library::review_has_positive():
    assert hasattr(library::Review, "positive")
    descriptor = None
    for klass in library::Review.__mro__:
        if "positive" in klass.__dict__:
            descriptor = klass.__dict__["positive"]
            break
    assert isinstance(descriptor, property)

def test_library::review_has_title():
    assert hasattr(library::Review, "title")
    descriptor = None
    for klass in library::Review.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_library::opinion_is_not_abstract():
    assert not inspect.isabstract(library::Opinion)


def test_library::opinion_constructor_exists():
    assert callable(library::Opinion.__init__)


def test_library::opinion_constructor_args():
    sig = inspect.signature(library::Opinion.__init__)
    params = list(sig.parameters.keys())
    assert "context" in params, "Missing parameter 'context'"
    assert "text" in params, "Missing parameter 'text'"

def test_library::opinion_has_context():
    assert hasattr(library::Opinion, "context")
    descriptor = None
    for klass in library::Opinion.__mro__:
        if "context" in klass.__dict__:
            descriptor = klass.__dict__["context"]
            break
    assert isinstance(descriptor, property)

def test_library::opinion_has_text():
    assert hasattr(library::Opinion, "text")
    descriptor = None
    for klass in library::Opinion.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_library::book_is_not_abstract():
    assert not inspect.isabstract(library::Book)


def test_library::book_constructor_exists():
    assert callable(library::Book.__init__)


def test_library::book_constructor_args():
    sig = inspect.signature(library::Book.__init__)
    params = list(sig.parameters.keys())
    assert "pages" in params, "Missing parameter 'pages'"
    assert "title" in params, "Missing parameter 'title'"
    assert "category" in params, "Missing parameter 'category'"

def test_library::book_has_pages():
    assert hasattr(library::Book, "pages")
    descriptor = None
    for klass in library::Book.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
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

def test_library::book_has_category():
    assert hasattr(library::Book, "category")
    descriptor = None
    for klass in library::Book.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)



def test_library::writer_is_not_abstract():
    assert not inspect.isabstract(library::Writer)


def test_library::writer_constructor_exists():
    assert callable(library::Writer.__init__)


def test_library::writer_constructor_args():
    sig = inspect.signature(library::Writer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_library::writer_has_name():
    assert hasattr(library::Writer, "name")
    descriptor = None
    for klass in library::Writer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
        "ScienceFiction",
        "Biography",
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
library::Review_strategy = st.builds(
    library::Review,
    positive=
        st.booleans(),
    title=
        safe_text
)
library::Opinion_strategy = st.builds(
    library::Opinion,
    context=
        safe_text,
    text=
        safe_text
)
library::Book_strategy = st.builds(
    library::Book,
    pages=
        st.integers(),
    title=
        safe_text,
    category=
        safe_text
)
library::Writer_strategy = st.builds(
    library::Writer,
    name=
        safe_text
)
library::Library_strategy = st.builds(
    library::Library,
    name=
        safe_text
)

@given(instance=library::Review_strategy)
@settings(max_examples=50)
def test_library::review_instantiation(instance):
    assert isinstance(instance, library::Review)

@given(instance=library::Review_strategy)
def test_library::review_positive_type(instance):
    assert isinstance(instance.positive, bool)


@given(instance=library::Review_strategy)
def test_library::review_positive_setter(instance):
    original = instance.positive
    instance.positive = original
    assert instance.positive == original

@given(instance=library::Review_strategy)
def test_library::review_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=library::Review_strategy)
def test_library::review_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=library::Opinion_strategy)
@settings(max_examples=50)
def test_library::opinion_instantiation(instance):
    assert isinstance(instance, library::Opinion)

@given(instance=library::Opinion_strategy)
def test_library::opinion_context_type(instance):
    assert isinstance(instance.context, str)


@given(instance=library::Opinion_strategy)
def test_library::opinion_context_setter(instance):
    original = instance.context
    instance.context = original
    assert instance.context == original

@given(instance=library::Opinion_strategy)
def test_library::opinion_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=library::Opinion_strategy)
def test_library::opinion_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

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
def test_library::book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=library::Book_strategy)
def test_library::book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=library::Book_strategy)
def test_library::book_category_type(instance):
    assert isinstance(instance.category, str)


@given(instance=library::Book_strategy)
def test_library::book_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original

@given(instance=library::Writer_strategy)
@settings(max_examples=50)
def test_library::writer_instantiation(instance):
    assert isinstance(instance, library::Writer)

@given(instance=library::Writer_strategy)
def test_library::writer_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=library::Writer_strategy)
def test_library::writer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

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
