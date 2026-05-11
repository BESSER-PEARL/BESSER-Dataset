import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    familytree::FamilyTree,
    familytree::Member,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_familytree::familytree_is_not_abstract():
    assert not inspect.isabstract(familytree::FamilyTree)


def test_familytree::familytree_constructor_exists():
    assert callable(familytree::FamilyTree.__init__)


def test_familytree::familytree_constructor_args():
    sig = inspect.signature(familytree::FamilyTree.__init__)
    params = list(sig.parameters.keys())



def test_familytree::member_is_not_abstract():
    assert not inspect.isabstract(familytree::Member)


def test_familytree::member_constructor_exists():
    assert callable(familytree::Member.__init__)


def test_familytree::member_constructor_args():
    sig = inspect.signature(familytree::Member.__init__)
    params = list(sig.parameters.keys())
    assert "age" in params, "Missing parameter 'age'"
    assert "name" in params, "Missing parameter 'name'"

def test_familytree::member_has_age():
    assert hasattr(familytree::Member, "age")
    descriptor = None
    for klass in familytree::Member.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_familytree::member_has_name():
    assert hasattr(familytree::Member, "name")
    descriptor = None
    for klass in familytree::Member.__mro__:
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
familytree::FamilyTree_strategy = st.builds(
    familytree::FamilyTree,
)
familytree::Member_strategy = st.builds(
    familytree::Member,
    age=
        st.integers(),
    name=
        safe_text
)

@given(instance=familytree::FamilyTree_strategy)
@settings(max_examples=50)
def test_familytree::familytree_instantiation(instance):
    assert isinstance(instance, familytree::FamilyTree)

@given(instance=familytree::Member_strategy)
@settings(max_examples=50)
def test_familytree::member_instantiation(instance):
    assert isinstance(instance, familytree::Member)

@given(instance=familytree::Member_strategy)
def test_familytree::member_age_type(instance):
    assert isinstance(instance.age, int)


@given(instance=familytree::Member_strategy)
def test_familytree::member_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=familytree::Member_strategy)
def test_familytree::member_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=familytree::Member_strategy)
def test_familytree::member_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
