import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    mm4::Medium,
    mm4::Member,
    mm4::Library,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mm4::medium_is_not_abstract():
    assert not inspect.isabstract(mm4::Medium)


def test_mm4::medium_constructor_exists():
    assert callable(mm4::Medium.__init__)


def test_mm4::medium_constructor_args():
    sig = inspect.signature(mm4::Medium.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_mm4::medium_has_name():
    assert hasattr(mm4::Medium, "name")
    descriptor = None
    for klass in mm4::Medium.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mm4::medium_has_type():
    assert hasattr(mm4::Medium, "type")
    descriptor = None
    for klass in mm4::Medium.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_mm4::member_is_not_abstract():
    assert not inspect.isabstract(mm4::Member)


def test_mm4::member_constructor_exists():
    assert callable(mm4::Member.__init__)


def test_mm4::member_constructor_args():
    sig = inspect.signature(mm4::Member.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mm4::member_has_name():
    assert hasattr(mm4::Member, "name")
    descriptor = None
    for klass in mm4::Member.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mm4::library_is_not_abstract():
    assert not inspect.isabstract(mm4::Library)


def test_mm4::library_constructor_exists():
    assert callable(mm4::Library.__init__)


def test_mm4::library_constructor_args():
    sig = inspect.signature(mm4::Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mm4::library_has_name():
    assert hasattr(mm4::Library, "name")
    descriptor = None
    for klass in mm4::Library.__mro__:
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
mm4::Medium_strategy = st.builds(
    mm4::Medium,
    name=
        safe_text,
    type=
        safe_text
)
mm4::Member_strategy = st.builds(
    mm4::Member,
    name=
        safe_text
)
mm4::Library_strategy = st.builds(
    mm4::Library,
    name=
        safe_text
)

@given(instance=mm4::Medium_strategy)
@settings(max_examples=50)
def test_mm4::medium_instantiation(instance):
    assert isinstance(instance, mm4::Medium)

@given(instance=mm4::Medium_strategy)
def test_mm4::medium_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mm4::Medium_strategy)
def test_mm4::medium_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mm4::Medium_strategy)
def test_mm4::medium_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=mm4::Medium_strategy)
def test_mm4::medium_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=mm4::Member_strategy)
@settings(max_examples=50)
def test_mm4::member_instantiation(instance):
    assert isinstance(instance, mm4::Member)

@given(instance=mm4::Member_strategy)
def test_mm4::member_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mm4::Member_strategy)
def test_mm4::member_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mm4::Library_strategy)
@settings(max_examples=50)
def test_mm4::library_instantiation(instance):
    assert isinstance(instance, mm4::Library)

@given(instance=mm4::Library_strategy)
def test_mm4::library_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mm4::Library_strategy)
def test_mm4::library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
