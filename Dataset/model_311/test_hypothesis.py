import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    library::Library,
    library::Writer,
    library::MapOfDataTypes,
    library::WriterNameMap,
    library::Book,
    BookCategory,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_library::library_is_not_abstract():
    assert not inspect.isabstract(library::Library)


def test_library::library_constructor_exists():
    assert callable(library::Library.__init__)


def test_library::library_constructor_args():
    sig = inspect.signature(library::Library.__init__)
    params = list(sig.parameters.keys())
    assert "map1" in params, "Missing parameter 'map1'"
    assert "uRIs_1" in params, "Missing parameter 'uRIs_1'"
    assert "options" in params, "Missing parameter 'options'"
    assert "bookByTitleMap" in params, "Missing parameter 'bookByTitleMap'"
    assert "name" in params, "Missing parameter 'name'"

def test_library::library_has_map1():
    assert hasattr(library::Library, "map1")
    descriptor = None
    for klass in library::Library.__mro__:
        if "map1" in klass.__dict__:
            descriptor = klass.__dict__["map1"]
            break
    assert isinstance(descriptor, property)

def test_library::library_has_uRIs_1():
    assert hasattr(library::Library, "uRIs_1")
    descriptor = None
    for klass in library::Library.__mro__:
        if "uRIs_1" in klass.__dict__:
            descriptor = klass.__dict__["uRIs_1"]
            break
    assert isinstance(descriptor, property)

def test_library::library_has_options():
    assert hasattr(library::Library, "options")
    descriptor = None
    for klass in library::Library.__mro__:
        if "options" in klass.__dict__:
            descriptor = klass.__dict__["options"]
            break
    assert isinstance(descriptor, property)

def test_library::library_has_bookByTitleMap():
    assert hasattr(library::Library, "bookByTitleMap")
    descriptor = None
    for klass in library::Library.__mro__:
        if "bookByTitleMap" in klass.__dict__:
            descriptor = klass.__dict__["bookByTitleMap"]
            break
    assert isinstance(descriptor, property)

def test_library::library_has_name():
    assert hasattr(library::Library, "name")
    descriptor = None
    for klass in library::Library.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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



def test_library::mapofdatatypes_is_not_abstract():
    assert not inspect.isabstract(library::MapOfDataTypes)


def test_library::mapofdatatypes_constructor_exists():
    assert callable(library::MapOfDataTypes.__init__)


def test_library::mapofdatatypes_constructor_args():
    sig = inspect.signature(library::MapOfDataTypes.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_library::mapofdatatypes_has_value():
    assert hasattr(library::MapOfDataTypes, "value")
    descriptor = None
    for klass in library::MapOfDataTypes.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_library::mapofdatatypes_has_key():
    assert hasattr(library::MapOfDataTypes, "key")
    descriptor = None
    for klass in library::MapOfDataTypes.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_library::writernamemap_is_not_abstract():
    assert not inspect.isabstract(library::WriterNameMap)


def test_library::writernamemap_constructor_exists():
    assert callable(library::WriterNameMap.__init__)


def test_library::writernamemap_constructor_args():
    sig = inspect.signature(library::WriterNameMap.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_library::writernamemap_has_key():
    assert hasattr(library::WriterNameMap, "key")
    descriptor = None
    for klass in library::WriterNameMap.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_library::book_is_not_abstract():
    assert not inspect.isabstract(library::Book)


def test_library::book_constructor_exists():
    assert callable(library::Book.__init__)


def test_library::book_constructor_args():
    sig = inspect.signature(library::Book.__init__)
    params = list(sig.parameters.keys())
    assert "category" in params, "Missing parameter 'category'"
    assert "pages" in params, "Missing parameter 'pages'"
    assert "title" in params, "Missing parameter 'title'"

def test_library::book_has_category():
    assert hasattr(library::Book, "category")
    descriptor = None
    for klass in library::Book.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

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

def test_bookcategory_exists():
    # Check that the Enumeration exists
    assert BookCategory is not None

def test_bookcategory_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BookCategory]
    expected_literals = [
        "MYSTERY",
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
library::Library_strategy = st.builds(
    library::Library,
    map1=
        safe_text,
    uRIs_1=
        safe_text,
    options=
        safe_text,
    bookByTitleMap=
        safe_text,
    name=
        safe_text
)
library::Writer_strategy = st.builds(
    library::Writer,
    name=
        safe_text
)
library::MapOfDataTypes_strategy = st.builds(
    library::MapOfDataTypes,
    value=
        safe_text,
    key=
        safe_text
)
library::WriterNameMap_strategy = st.builds(
    library::WriterNameMap,
    key=
        safe_text
)
library::Book_strategy = st.builds(
    library::Book,
    category=
        safe_text,
    pages=
        st.integers(),
    title=
        safe_text
)

@given(instance=library::Library_strategy)
@settings(max_examples=50)
def test_library::library_instantiation(instance):
    assert isinstance(instance, library::Library)

@given(instance=library::Library_strategy)
def test_library::library_map1_type(instance):
    assert isinstance(instance.map1, str)


@given(instance=library::Library_strategy)
def test_library::library_map1_setter(instance):
    original = instance.map1
    instance.map1 = original
    assert instance.map1 == original

@given(instance=library::Library_strategy)
def test_library::library_uRIs_1_type(instance):
    assert isinstance(instance.uRIs_1, str)


@given(instance=library::Library_strategy)
def test_library::library_uRIs_1_setter(instance):
    original = instance.uRIs_1
    instance.uRIs_1 = original
    assert instance.uRIs_1 == original

@given(instance=library::Library_strategy)
def test_library::library_options_type(instance):
    assert isinstance(instance.options, str)


@given(instance=library::Library_strategy)
def test_library::library_options_setter(instance):
    original = instance.options
    instance.options = original
    assert instance.options == original

@given(instance=library::Library_strategy)
def test_library::library_bookByTitleMap_type(instance):
    assert isinstance(instance.bookByTitleMap, str)


@given(instance=library::Library_strategy)
def test_library::library_bookByTitleMap_setter(instance):
    original = instance.bookByTitleMap
    instance.bookByTitleMap = original
    assert instance.bookByTitleMap == original

@given(instance=library::Library_strategy)
def test_library::library_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=library::Library_strategy)
def test_library::library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

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

@given(instance=library::MapOfDataTypes_strategy)
@settings(max_examples=50)
def test_library::mapofdatatypes_instantiation(instance):
    assert isinstance(instance, library::MapOfDataTypes)

@given(instance=library::MapOfDataTypes_strategy)
def test_library::mapofdatatypes_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=library::MapOfDataTypes_strategy)
def test_library::mapofdatatypes_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=library::MapOfDataTypes_strategy)
def test_library::mapofdatatypes_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=library::MapOfDataTypes_strategy)
def test_library::mapofdatatypes_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=library::WriterNameMap_strategy)
@settings(max_examples=50)
def test_library::writernamemap_instantiation(instance):
    assert isinstance(instance, library::WriterNameMap)

@given(instance=library::WriterNameMap_strategy)
def test_library::writernamemap_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=library::WriterNameMap_strategy)
def test_library::writernamemap_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=library::Book_strategy)
@settings(max_examples=50)
def test_library::book_instantiation(instance):
    assert isinstance(instance, library::Book)

@given(instance=library::Book_strategy)
def test_library::book_category_type(instance):
    assert isinstance(instance.category, str)


@given(instance=library::Book_strategy)
def test_library::book_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original

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
