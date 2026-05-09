import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    mm3::Film,
    mm3::Book,
    mm3::Member,
    mm3::Library,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mm3::film_is_not_abstract():
    assert not inspect.isabstract(mm3::Film)


def test_mm3::film_constructor_exists():
    assert callable(mm3::Film.__init__)


def test_mm3::film_constructor_args():
    sig = inspect.signature(mm3::Film.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mm3::film_has_name():
    assert hasattr(mm3::Film, "name")
    descriptor = None
    for klass in mm3::Film.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mm3::book_is_not_abstract():
    assert not inspect.isabstract(mm3::Book)


def test_mm3::book_constructor_exists():
    assert callable(mm3::Book.__init__)


def test_mm3::book_constructor_args():
    sig = inspect.signature(mm3::Book.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mm3::book_has_name():
    assert hasattr(mm3::Book, "name")
    descriptor = None
    for klass in mm3::Book.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mm3::member_is_not_abstract():
    assert not inspect.isabstract(mm3::Member)


def test_mm3::member_constructor_exists():
    assert callable(mm3::Member.__init__)


def test_mm3::member_constructor_args():
    sig = inspect.signature(mm3::Member.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mm3::member_has_name():
    assert hasattr(mm3::Member, "name")
    descriptor = None
    for klass in mm3::Member.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mm3::library_is_not_abstract():
    assert not inspect.isabstract(mm3::Library)


def test_mm3::library_constructor_exists():
    assert callable(mm3::Library.__init__)


def test_mm3::library_constructor_args():
    sig = inspect.signature(mm3::Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mm3::library_has_name():
    assert hasattr(mm3::Library, "name")
    descriptor = None
    for klass in mm3::Library.__mro__:
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
mm3::Film_strategy = st.builds(
    mm3::Film,
    name=
        safe_text
)
mm3::Book_strategy = st.builds(
    mm3::Book,
    name=
        safe_text
)
mm3::Member_strategy = st.builds(
    mm3::Member,
    name=
        safe_text
)
mm3::Library_strategy = st.builds(
    mm3::Library,
    name=
        safe_text
)

@given(instance=mm3::Film_strategy)
@settings(max_examples=50)
def test_mm3::film_instantiation(instance):
    assert isinstance(instance, mm3::Film)

@given(instance=mm3::Film_strategy)
def test_mm3::film_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mm3::Film_strategy)
def test_mm3::film_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mm3::Book_strategy)
@settings(max_examples=50)
def test_mm3::book_instantiation(instance):
    assert isinstance(instance, mm3::Book)

@given(instance=mm3::Book_strategy)
def test_mm3::book_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mm3::Book_strategy)
def test_mm3::book_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mm3::Member_strategy)
@settings(max_examples=50)
def test_mm3::member_instantiation(instance):
    assert isinstance(instance, mm3::Member)

@given(instance=mm3::Member_strategy)
def test_mm3::member_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mm3::Member_strategy)
def test_mm3::member_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mm3::Library_strategy)
@settings(max_examples=50)
def test_mm3::library_instantiation(instance):
    assert isinstance(instance, mm3::Library)

@given(instance=mm3::Library_strategy)
def test_mm3::library_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mm3::Library_strategy)
def test_mm3::library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
