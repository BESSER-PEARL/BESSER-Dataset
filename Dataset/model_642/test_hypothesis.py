import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    mm1::Library,
    mm1::Film,
    mm1::Book,
    mm1::Member,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mm1::library_is_not_abstract():
    assert not inspect.isabstract(mm1::Library)


def test_mm1::library_constructor_exists():
    assert callable(mm1::Library.__init__)


def test_mm1::library_constructor_args():
    sig = inspect.signature(mm1::Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mm1::library_has_name():
    assert hasattr(mm1::Library, "name")
    descriptor = None
    for klass in mm1::Library.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mm1::film_is_not_abstract():
    assert not inspect.isabstract(mm1::Film)


def test_mm1::film_constructor_exists():
    assert callable(mm1::Film.__init__)


def test_mm1::film_constructor_args():
    sig = inspect.signature(mm1::Film.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mm1::film_has_name():
    assert hasattr(mm1::Film, "name")
    descriptor = None
    for klass in mm1::Film.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mm1::book_is_not_abstract():
    assert not inspect.isabstract(mm1::Book)


def test_mm1::book_constructor_exists():
    assert callable(mm1::Book.__init__)


def test_mm1::book_constructor_args():
    sig = inspect.signature(mm1::Book.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mm1::book_has_name():
    assert hasattr(mm1::Book, "name")
    descriptor = None
    for klass in mm1::Book.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mm1::member_is_not_abstract():
    assert not inspect.isabstract(mm1::Member)


def test_mm1::member_constructor_exists():
    assert callable(mm1::Member.__init__)


def test_mm1::member_constructor_args():
    sig = inspect.signature(mm1::Member.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mm1::member_has_name():
    assert hasattr(mm1::Member, "name")
    descriptor = None
    for klass in mm1::Member.__mro__:
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
mm1::Library_strategy = st.builds(
    mm1::Library,
    name=
        safe_text
)
mm1::Film_strategy = st.builds(
    mm1::Film,
    name=
        safe_text
)
mm1::Book_strategy = st.builds(
    mm1::Book,
    name=
        safe_text
)
mm1::Member_strategy = st.builds(
    mm1::Member,
    name=
        safe_text
)

@given(instance=mm1::Library_strategy)
@settings(max_examples=50)
def test_mm1::library_instantiation(instance):
    assert isinstance(instance, mm1::Library)

@given(instance=mm1::Library_strategy)
def test_mm1::library_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mm1::Library_strategy)
def test_mm1::library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mm1::Film_strategy)
@settings(max_examples=50)
def test_mm1::film_instantiation(instance):
    assert isinstance(instance, mm1::Film)

@given(instance=mm1::Film_strategy)
def test_mm1::film_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mm1::Film_strategy)
def test_mm1::film_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mm1::Book_strategy)
@settings(max_examples=50)
def test_mm1::book_instantiation(instance):
    assert isinstance(instance, mm1::Book)

@given(instance=mm1::Book_strategy)
def test_mm1::book_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mm1::Book_strategy)
def test_mm1::book_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mm1::Member_strategy)
@settings(max_examples=50)
def test_mm1::member_instantiation(instance):
    assert isinstance(instance, mm1::Member)

@given(instance=mm1::Member_strategy)
def test_mm1::member_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mm1::Member_strategy)
def test_mm1::member_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
