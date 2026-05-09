import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    eavlibrary::Pen,
    eavlibrary::Writer,
    eavlibrary::Book,
    eavlibrary::Library,
    eavlibrary::City,
    BookCategory,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_eavlibrary::pen_is_not_abstract():
    assert not inspect.isabstract(eavlibrary::Pen)


def test_eavlibrary::pen_constructor_exists():
    assert callable(eavlibrary::Pen.__init__)


def test_eavlibrary::pen_constructor_args():
    sig = inspect.signature(eavlibrary::Pen.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_eavlibrary::pen_has_name():
    assert hasattr(eavlibrary::Pen, "name")
    descriptor = None
    for klass in eavlibrary::Pen.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_eavlibrary::writer_is_not_abstract():
    assert not inspect.isabstract(eavlibrary::Writer)


def test_eavlibrary::writer_constructor_exists():
    assert callable(eavlibrary::Writer.__init__)


def test_eavlibrary::writer_constructor_args():
    sig = inspect.signature(eavlibrary::Writer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "image" in params, "Missing parameter 'image'"
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_eavlibrary::writer_has_name():
    assert hasattr(eavlibrary::Writer, "name")
    descriptor = None
    for klass in eavlibrary::Writer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_eavlibrary::writer_has_image():
    assert hasattr(eavlibrary::Writer, "image")
    descriptor = None
    for klass in eavlibrary::Writer.__mro__:
        if "image" in klass.__dict__:
            descriptor = klass.__dict__["image"]
            break
    assert isinstance(descriptor, property)

def test_eavlibrary::writer_has_abstract():
    assert hasattr(eavlibrary::Writer, "abstract")
    descriptor = None
    for klass in eavlibrary::Writer.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_eavlibrary::book_is_not_abstract():
    assert not inspect.isabstract(eavlibrary::Book)


def test_eavlibrary::book_constructor_exists():
    assert callable(eavlibrary::Book.__init__)


def test_eavlibrary::book_constructor_args():
    sig = inspect.signature(eavlibrary::Book.__init__)
    params = list(sig.parameters.keys())
    assert "test" in params, "Missing parameter 'test'"
    assert "category" in params, "Missing parameter 'category'"
    assert "title" in params, "Missing parameter 'title'"
    assert "pages" in params, "Missing parameter 'pages'"

def test_eavlibrary::book_has_test():
    assert hasattr(eavlibrary::Book, "test")
    descriptor = None
    for klass in eavlibrary::Book.__mro__:
        if "test" in klass.__dict__:
            descriptor = klass.__dict__["test"]
            break
    assert isinstance(descriptor, property)

def test_eavlibrary::book_has_category():
    assert hasattr(eavlibrary::Book, "category")
    descriptor = None
    for klass in eavlibrary::Book.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_eavlibrary::book_has_title():
    assert hasattr(eavlibrary::Book, "title")
    descriptor = None
    for klass in eavlibrary::Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_eavlibrary::book_has_pages():
    assert hasattr(eavlibrary::Book, "pages")
    descriptor = None
    for klass in eavlibrary::Book.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)



def test_eavlibrary::library_is_not_abstract():
    assert not inspect.isabstract(eavlibrary::Library)


def test_eavlibrary::library_constructor_exists():
    assert callable(eavlibrary::Library.__init__)


def test_eavlibrary::library_constructor_args():
    sig = inspect.signature(eavlibrary::Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_eavlibrary::library_has_name():
    assert hasattr(eavlibrary::Library, "name")
    descriptor = None
    for klass in eavlibrary::Library.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_eavlibrary::city_is_not_abstract():
    assert not inspect.isabstract(eavlibrary::City)


def test_eavlibrary::city_constructor_exists():
    assert callable(eavlibrary::City.__init__)


def test_eavlibrary::city_constructor_args():
    sig = inspect.signature(eavlibrary::City.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_eavlibrary::city_has_name():
    assert hasattr(eavlibrary::City, "name")
    descriptor = None
    for klass in eavlibrary::City.__mro__:
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
        "ScienceFiction",
        "Mystery",
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
eavlibrary::Pen_strategy = st.builds(
    eavlibrary::Pen,
    name=
        safe_text
)
eavlibrary::Writer_strategy = st.builds(
    eavlibrary::Writer,
    name=
        safe_text,
    image=
        safe_text,
    abstract=
        safe_text
)
eavlibrary::Book_strategy = st.builds(
    eavlibrary::Book,
    test=
        safe_text,
    category=
        safe_text,
    title=
        safe_text,
    pages=
        safe_text
)
eavlibrary::Library_strategy = st.builds(
    eavlibrary::Library,
    name=
        safe_text
)
eavlibrary::City_strategy = st.builds(
    eavlibrary::City,
    name=
        safe_text
)

@given(instance=eavlibrary::Pen_strategy)
@settings(max_examples=50)
def test_eavlibrary::pen_instantiation(instance):
    assert isinstance(instance, eavlibrary::Pen)

@given(instance=eavlibrary::Pen_strategy)
def test_eavlibrary::pen_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=eavlibrary::Pen_strategy)
def test_eavlibrary::pen_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eavlibrary::Writer_strategy)
@settings(max_examples=50)
def test_eavlibrary::writer_instantiation(instance):
    assert isinstance(instance, eavlibrary::Writer)

@given(instance=eavlibrary::Writer_strategy)
def test_eavlibrary::writer_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=eavlibrary::Writer_strategy)
def test_eavlibrary::writer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eavlibrary::Writer_strategy)
def test_eavlibrary::writer_image_type(instance):
    assert isinstance(instance.image, str)


@given(instance=eavlibrary::Writer_strategy)
def test_eavlibrary::writer_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original

@given(instance=eavlibrary::Writer_strategy)
def test_eavlibrary::writer_abstract_type(instance):
    assert isinstance(instance.abstract, str)


@given(instance=eavlibrary::Writer_strategy)
def test_eavlibrary::writer_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=eavlibrary::Book_strategy)
@settings(max_examples=50)
def test_eavlibrary::book_instantiation(instance):
    assert isinstance(instance, eavlibrary::Book)

@given(instance=eavlibrary::Book_strategy)
def test_eavlibrary::book_test_type(instance):
    assert isinstance(instance.test, str)


@given(instance=eavlibrary::Book_strategy)
def test_eavlibrary::book_test_setter(instance):
    original = instance.test
    instance.test = original
    assert instance.test == original

@given(instance=eavlibrary::Book_strategy)
def test_eavlibrary::book_category_type(instance):
    assert isinstance(instance.category, str)


@given(instance=eavlibrary::Book_strategy)
def test_eavlibrary::book_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original

@given(instance=eavlibrary::Book_strategy)
def test_eavlibrary::book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=eavlibrary::Book_strategy)
def test_eavlibrary::book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=eavlibrary::Book_strategy)
def test_eavlibrary::book_pages_type(instance):
    assert isinstance(instance.pages, str)


@given(instance=eavlibrary::Book_strategy)
def test_eavlibrary::book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=eavlibrary::Library_strategy)
@settings(max_examples=50)
def test_eavlibrary::library_instantiation(instance):
    assert isinstance(instance, eavlibrary::Library)

@given(instance=eavlibrary::Library_strategy)
def test_eavlibrary::library_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=eavlibrary::Library_strategy)
def test_eavlibrary::library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eavlibrary::City_strategy)
@settings(max_examples=50)
def test_eavlibrary::city_instantiation(instance):
    assert isinstance(instance, eavlibrary::City)

@given(instance=eavlibrary::City_strategy)
def test_eavlibrary::city_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=eavlibrary::City_strategy)
def test_eavlibrary::city_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
