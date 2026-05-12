import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    hierarchy_Book,
    hierarchy_NonFiction,
    hierarchy_Fiction,
    hierarchy_HierLibrary,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hierarchy_book_is_not_abstract():
    assert not inspect.isabstract(hierarchy_Book)


def test_hierarchy_book_constructor_exists():
    assert callable(hierarchy_Book.__init__)


def test_hierarchy_book_constructor_args():
    sig = inspect.signature(hierarchy_Book.__init__)
    params = list(sig.parameters.keys())
    assert "genre" in params, "Missing parameter 'genre'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_hierarchy_book_has_genre():
    assert hasattr(hierarchy_Book, "genre")
    descriptor = None
    for klass in hierarchy_Book.__mro__:
        if "genre" in klass.__dict__:
            descriptor = klass.__dict__["genre"]
            break
    assert isinstance(descriptor, property)

def test_hierarchy_book_has_Name():
    assert hasattr(hierarchy_Book, "Name")
    descriptor = None
    for klass in hierarchy_Book.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_hierarchy_nonfiction_is_not_abstract():
    assert not inspect.isabstract(hierarchy_NonFiction)


def test_hierarchy_nonfiction_constructor_exists():
    assert callable(hierarchy_NonFiction.__init__)


def test_hierarchy_nonfiction_constructor_args():
    sig = inspect.signature(hierarchy_NonFiction.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_hierarchy_nonfiction_has_Name():
    assert hasattr(hierarchy_NonFiction, "Name")
    descriptor = None
    for klass in hierarchy_NonFiction.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_hierarchy_fiction_is_not_abstract():
    assert not inspect.isabstract(hierarchy_Fiction)


def test_hierarchy_fiction_constructor_exists():
    assert callable(hierarchy_Fiction.__init__)


def test_hierarchy_fiction_constructor_args():
    sig = inspect.signature(hierarchy_Fiction.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_hierarchy_fiction_has_Name():
    assert hasattr(hierarchy_Fiction, "Name")
    descriptor = None
    for klass in hierarchy_Fiction.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_hierarchy_hierlibrary_is_not_abstract():
    assert not inspect.isabstract(hierarchy_HierLibrary)


def test_hierarchy_hierlibrary_constructor_exists():
    assert callable(hierarchy_HierLibrary.__init__)


def test_hierarchy_hierlibrary_constructor_args():
    sig = inspect.signature(hierarchy_HierLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_hierarchy_hierlibrary_has_Name():
    assert hasattr(hierarchy_HierLibrary, "Name")
    descriptor = None
    for klass in hierarchy_HierLibrary.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
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
hierarchy_Book_strategy = st.builds(
    hierarchy_Book,
    genre=
        safe_text,
    Name=
        safe_text
)
hierarchy_NonFiction_strategy = st.builds(
    hierarchy_NonFiction,
    Name=
        safe_text
)
hierarchy_Fiction_strategy = st.builds(
    hierarchy_Fiction,
    Name=
        safe_text
)
hierarchy_HierLibrary_strategy = st.builds(
    hierarchy_HierLibrary,
    Name=
        safe_text
)

@given(instance=hierarchy_Book_strategy)
@settings(max_examples=50)
def test_hierarchy_book_instantiation(instance):
    assert isinstance(instance, hierarchy_Book)



@given(instance=hierarchy_Book_strategy)
def test_hierarchy_book_genre_setter(instance):
    original = instance.genre
    instance.genre = original
    assert instance.genre == original



@given(instance=hierarchy_Book_strategy)
def test_hierarchy_book_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=hierarchy_NonFiction_strategy)
@settings(max_examples=50)
def test_hierarchy_nonfiction_instantiation(instance):
    assert isinstance(instance, hierarchy_NonFiction)



@given(instance=hierarchy_NonFiction_strategy)
def test_hierarchy_nonfiction_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=hierarchy_Fiction_strategy)
@settings(max_examples=50)
def test_hierarchy_fiction_instantiation(instance):
    assert isinstance(instance, hierarchy_Fiction)



@given(instance=hierarchy_Fiction_strategy)
def test_hierarchy_fiction_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=hierarchy_HierLibrary_strategy)
@settings(max_examples=50)
def test_hierarchy_hierlibrary_instantiation(instance):
    assert isinstance(instance, hierarchy_HierLibrary)



@given(instance=hierarchy_HierLibrary_strategy)
def test_hierarchy_hierlibrary_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original
