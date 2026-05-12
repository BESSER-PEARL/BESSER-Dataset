import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    mm2_Member,
    mm2_Category,
    mm2_Medium,
    mm2_Library,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mm2_member_is_not_abstract():
    assert not inspect.isabstract(mm2_Member)


def test_mm2_member_constructor_exists():
    assert callable(mm2_Member.__init__)


def test_mm2_member_constructor_args():
    sig = inspect.signature(mm2_Member.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mm2_member_has_name():
    assert hasattr(mm2_Member, "name")
    descriptor = None
    for klass in mm2_Member.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mm2_category_is_not_abstract():
    assert not inspect.isabstract(mm2_Category)


def test_mm2_category_constructor_exists():
    assert callable(mm2_Category.__init__)


def test_mm2_category_constructor_args():
    sig = inspect.signature(mm2_Category.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mm2_category_has_name():
    assert hasattr(mm2_Category, "name")
    descriptor = None
    for klass in mm2_Category.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mm2_medium_is_not_abstract():
    assert not inspect.isabstract(mm2_Medium)


def test_mm2_medium_constructor_exists():
    assert callable(mm2_Medium.__init__)


def test_mm2_medium_constructor_args():
    sig = inspect.signature(mm2_Medium.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_mm2_medium_has_name():
    assert hasattr(mm2_Medium, "name")
    descriptor = None
    for klass in mm2_Medium.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mm2_medium_has_type():
    assert hasattr(mm2_Medium, "type")
    descriptor = None
    for klass in mm2_Medium.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_mm2_library_is_not_abstract():
    assert not inspect.isabstract(mm2_Library)


def test_mm2_library_constructor_exists():
    assert callable(mm2_Library.__init__)


def test_mm2_library_constructor_args():
    sig = inspect.signature(mm2_Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mm2_library_has_name():
    assert hasattr(mm2_Library, "name")
    descriptor = None
    for klass in mm2_Library.__mro__:
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
mm2_Member_strategy = st.builds(
    mm2_Member,
    name=
        safe_text
)
mm2_Category_strategy = st.builds(
    mm2_Category,
    name=
        safe_text
)
mm2_Medium_strategy = st.builds(
    mm2_Medium,
    name=
        safe_text,
    type=
        safe_text
)
mm2_Library_strategy = st.builds(
    mm2_Library,
    name=
        safe_text
)

@given(instance=mm2_Member_strategy)
@settings(max_examples=50)
def test_mm2_member_instantiation(instance):
    assert isinstance(instance, mm2_Member)



@given(instance=mm2_Member_strategy)
def test_mm2_member_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mm2_Category_strategy)
@settings(max_examples=50)
def test_mm2_category_instantiation(instance):
    assert isinstance(instance, mm2_Category)



@given(instance=mm2_Category_strategy)
def test_mm2_category_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mm2_Medium_strategy)
@settings(max_examples=50)
def test_mm2_medium_instantiation(instance):
    assert isinstance(instance, mm2_Medium)



@given(instance=mm2_Medium_strategy)
def test_mm2_medium_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=mm2_Medium_strategy)
def test_mm2_medium_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=mm2_Library_strategy)
@settings(max_examples=50)
def test_mm2_library_instantiation(instance):
    assert isinstance(instance, mm2_Library)



@given(instance=mm2_Library_strategy)
def test_mm2_library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
