import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    mm4_Medium,
    mm4_Member,
    mm4_Library,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mm4_medium_is_not_abstract():
    assert not inspect.isabstract(mm4_Medium)


def test_mm4_medium_constructor_exists():
    assert callable(mm4_Medium.__init__)


def test_mm4_medium_constructor_args():
    sig = inspect.signature(mm4_Medium.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_mm4_medium_has_type():
    assert hasattr(mm4_Medium, "type")
    descriptor = None
    for klass in mm4_Medium.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_mm4_medium_has_name():
    assert hasattr(mm4_Medium, "name")
    descriptor = None
    for klass in mm4_Medium.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mm4_member_is_not_abstract():
    assert not inspect.isabstract(mm4_Member)


def test_mm4_member_constructor_exists():
    assert callable(mm4_Member.__init__)


def test_mm4_member_constructor_args():
    sig = inspect.signature(mm4_Member.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mm4_member_has_name():
    assert hasattr(mm4_Member, "name")
    descriptor = None
    for klass in mm4_Member.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mm4_library_is_not_abstract():
    assert not inspect.isabstract(mm4_Library)


def test_mm4_library_constructor_exists():
    assert callable(mm4_Library.__init__)


def test_mm4_library_constructor_args():
    sig = inspect.signature(mm4_Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mm4_library_has_name():
    assert hasattr(mm4_Library, "name")
    descriptor = None
    for klass in mm4_Library.__mro__:
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
mm4_Medium_strategy = st.builds(
    mm4_Medium,
    type=
        safe_text,
    name=
        safe_text
)
mm4_Member_strategy = st.builds(
    mm4_Member,
    name=
        safe_text
)
mm4_Library_strategy = st.builds(
    mm4_Library,
    name=
        safe_text
)

@given(instance=mm4_Medium_strategy)
@settings(max_examples=50)
def test_mm4_medium_instantiation(instance):
    assert isinstance(instance, mm4_Medium)



@given(instance=mm4_Medium_strategy)
def test_mm4_medium_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=mm4_Medium_strategy)
def test_mm4_medium_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mm4_Member_strategy)
@settings(max_examples=50)
def test_mm4_member_instantiation(instance):
    assert isinstance(instance, mm4_Member)



@given(instance=mm4_Member_strategy)
def test_mm4_member_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mm4_Library_strategy)
@settings(max_examples=50)
def test_mm4_library_instantiation(instance):
    assert isinstance(instance, mm4_Library)



@given(instance=mm4_Library_strategy)
def test_mm4_library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
