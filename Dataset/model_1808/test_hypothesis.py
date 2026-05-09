import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    hierarchy::Book,
    hierarchy::NonFiction,
    hierarchy::Fiction,
    hierarchy::HierLibrary,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hierarchy::book_is_not_abstract():
    assert not inspect.isabstract(hierarchy::Book)


def test_hierarchy::book_constructor_exists():
    assert callable(hierarchy::Book.__init__)


def test_hierarchy::book_constructor_args():
    sig = inspect.signature(hierarchy::Book.__init__)
    params = list(sig.parameters.keys())
    assert "genre" in params, "Missing parameter 'genre'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_hierarchy::book_has_genre():
    assert hasattr(hierarchy::Book, "genre")
    descriptor = None
    for klass in hierarchy::Book.__mro__:
        if "genre" in klass.__dict__:
            descriptor = klass.__dict__["genre"]
            break
    assert isinstance(descriptor, property)

def test_hierarchy::book_has_Name():
    assert hasattr(hierarchy::Book, "Name")
    descriptor = None
    for klass in hierarchy::Book.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_hierarchy::nonfiction_is_not_abstract():
    assert not inspect.isabstract(hierarchy::NonFiction)


def test_hierarchy::nonfiction_constructor_exists():
    assert callable(hierarchy::NonFiction.__init__)


def test_hierarchy::nonfiction_constructor_args():
    sig = inspect.signature(hierarchy::NonFiction.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_hierarchy::nonfiction_has_Name():
    assert hasattr(hierarchy::NonFiction, "Name")
    descriptor = None
    for klass in hierarchy::NonFiction.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_hierarchy::fiction_is_not_abstract():
    assert not inspect.isabstract(hierarchy::Fiction)


def test_hierarchy::fiction_constructor_exists():
    assert callable(hierarchy::Fiction.__init__)


def test_hierarchy::fiction_constructor_args():
    sig = inspect.signature(hierarchy::Fiction.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_hierarchy::fiction_has_Name():
    assert hasattr(hierarchy::Fiction, "Name")
    descriptor = None
    for klass in hierarchy::Fiction.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_hierarchy::hierlibrary_is_not_abstract():
    assert not inspect.isabstract(hierarchy::HierLibrary)


def test_hierarchy::hierlibrary_constructor_exists():
    assert callable(hierarchy::HierLibrary.__init__)


def test_hierarchy::hierlibrary_constructor_args():
    sig = inspect.signature(hierarchy::HierLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_hierarchy::hierlibrary_has_Name():
    assert hasattr(hierarchy::HierLibrary, "Name")
    descriptor = None
    for klass in hierarchy::HierLibrary.__mro__:
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
hierarchy::Book_strategy = st.builds(
    hierarchy::Book,
    genre=
        safe_text,
    Name=
        safe_text
)
hierarchy::NonFiction_strategy = st.builds(
    hierarchy::NonFiction,
    Name=
        safe_text
)
hierarchy::Fiction_strategy = st.builds(
    hierarchy::Fiction,
    Name=
        safe_text
)
hierarchy::HierLibrary_strategy = st.builds(
    hierarchy::HierLibrary,
    Name=
        safe_text
)

@given(instance=hierarchy::Book_strategy)
@settings(max_examples=50)
def test_hierarchy::book_instantiation(instance):
    assert isinstance(instance, hierarchy::Book)

@given(instance=hierarchy::Book_strategy)
def test_hierarchy::book_genre_type(instance):
    assert isinstance(instance.genre, str)


@given(instance=hierarchy::Book_strategy)
def test_hierarchy::book_genre_setter(instance):
    original = instance.genre
    instance.genre = original
    assert instance.genre == original

@given(instance=hierarchy::Book_strategy)
def test_hierarchy::book_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=hierarchy::Book_strategy)
def test_hierarchy::book_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=hierarchy::NonFiction_strategy)
@settings(max_examples=50)
def test_hierarchy::nonfiction_instantiation(instance):
    assert isinstance(instance, hierarchy::NonFiction)

@given(instance=hierarchy::NonFiction_strategy)
def test_hierarchy::nonfiction_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=hierarchy::NonFiction_strategy)
def test_hierarchy::nonfiction_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=hierarchy::Fiction_strategy)
@settings(max_examples=50)
def test_hierarchy::fiction_instantiation(instance):
    assert isinstance(instance, hierarchy::Fiction)

@given(instance=hierarchy::Fiction_strategy)
def test_hierarchy::fiction_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=hierarchy::Fiction_strategy)
def test_hierarchy::fiction_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=hierarchy::HierLibrary_strategy)
@settings(max_examples=50)
def test_hierarchy::hierlibrary_instantiation(instance):
    assert isinstance(instance, hierarchy::HierLibrary)

@given(instance=hierarchy::HierLibrary_strategy)
def test_hierarchy::hierlibrary_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=hierarchy::HierLibrary_strategy)
def test_hierarchy::hierlibrary_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original
