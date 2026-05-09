import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    mm2::Member,
    mm2::Category,
    mm2::Medium,
    mm2::Library,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mm2::member_is_not_abstract():
    assert not inspect.isabstract(mm2::Member)


def test_mm2::member_constructor_exists():
    assert callable(mm2::Member.__init__)


def test_mm2::member_constructor_args():
    sig = inspect.signature(mm2::Member.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mm2::member_has_name():
    assert hasattr(mm2::Member, "name")
    descriptor = None
    for klass in mm2::Member.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mm2::category_is_not_abstract():
    assert not inspect.isabstract(mm2::Category)


def test_mm2::category_constructor_exists():
    assert callable(mm2::Category.__init__)


def test_mm2::category_constructor_args():
    sig = inspect.signature(mm2::Category.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mm2::category_has_name():
    assert hasattr(mm2::Category, "name")
    descriptor = None
    for klass in mm2::Category.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mm2::medium_is_not_abstract():
    assert not inspect.isabstract(mm2::Medium)


def test_mm2::medium_constructor_exists():
    assert callable(mm2::Medium.__init__)


def test_mm2::medium_constructor_args():
    sig = inspect.signature(mm2::Medium.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_mm2::medium_has_name():
    assert hasattr(mm2::Medium, "name")
    descriptor = None
    for klass in mm2::Medium.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mm2::medium_has_type():
    assert hasattr(mm2::Medium, "type")
    descriptor = None
    for klass in mm2::Medium.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_mm2::library_is_not_abstract():
    assert not inspect.isabstract(mm2::Library)


def test_mm2::library_constructor_exists():
    assert callable(mm2::Library.__init__)


def test_mm2::library_constructor_args():
    sig = inspect.signature(mm2::Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mm2::library_has_name():
    assert hasattr(mm2::Library, "name")
    descriptor = None
    for klass in mm2::Library.__mro__:
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
mm2::Member_strategy = st.builds(
    mm2::Member,
    name=
        safe_text
)
mm2::Category_strategy = st.builds(
    mm2::Category,
    name=
        safe_text
)
mm2::Medium_strategy = st.builds(
    mm2::Medium,
    name=
        safe_text,
    type=
        safe_text
)
mm2::Library_strategy = st.builds(
    mm2::Library,
    name=
        safe_text
)

@given(instance=mm2::Member_strategy)
@settings(max_examples=50)
def test_mm2::member_instantiation(instance):
    assert isinstance(instance, mm2::Member)

@given(instance=mm2::Member_strategy)
def test_mm2::member_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mm2::Member_strategy)
def test_mm2::member_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mm2::Category_strategy)
@settings(max_examples=50)
def test_mm2::category_instantiation(instance):
    assert isinstance(instance, mm2::Category)

@given(instance=mm2::Category_strategy)
def test_mm2::category_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mm2::Category_strategy)
def test_mm2::category_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mm2::Medium_strategy)
@settings(max_examples=50)
def test_mm2::medium_instantiation(instance):
    assert isinstance(instance, mm2::Medium)

@given(instance=mm2::Medium_strategy)
def test_mm2::medium_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mm2::Medium_strategy)
def test_mm2::medium_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mm2::Medium_strategy)
def test_mm2::medium_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=mm2::Medium_strategy)
def test_mm2::medium_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=mm2::Library_strategy)
@settings(max_examples=50)
def test_mm2::library_instantiation(instance):
    assert isinstance(instance, mm2::Library)

@given(instance=mm2::Library_strategy)
def test_mm2::library_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mm2::Library_strategy)
def test_mm2::library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
