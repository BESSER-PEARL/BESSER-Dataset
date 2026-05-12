import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    familytree_FamilyTree,
    familytree_Member,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_familytree_familytree_is_not_abstract():
    assert not inspect.isabstract(familytree_FamilyTree)


def test_familytree_familytree_constructor_exists():
    assert callable(familytree_FamilyTree.__init__)


def test_familytree_familytree_constructor_args():
    sig = inspect.signature(familytree_FamilyTree.__init__)
    params = list(sig.parameters.keys())



def test_familytree_member_is_not_abstract():
    assert not inspect.isabstract(familytree_Member)


def test_familytree_member_constructor_exists():
    assert callable(familytree_Member.__init__)


def test_familytree_member_constructor_args():
    sig = inspect.signature(familytree_Member.__init__)
    params = list(sig.parameters.keys())
    assert "age" in params, "Missing parameter 'age'"
    assert "name" in params, "Missing parameter 'name'"

def test_familytree_member_has_age():
    assert hasattr(familytree_Member, "age")
    descriptor = None
    for klass in familytree_Member.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_familytree_member_has_name():
    assert hasattr(familytree_Member, "name")
    descriptor = None
    for klass in familytree_Member.__mro__:
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
familytree_FamilyTree_strategy = st.builds(
    familytree_FamilyTree,
)
familytree_Member_strategy = st.builds(
    familytree_Member,
    age=
        st.integers(),
    name=
        safe_text
)

@given(instance=familytree_FamilyTree_strategy)
@settings(max_examples=50)
def test_familytree_familytree_instantiation(instance):
    assert isinstance(instance, familytree_FamilyTree)

@given(instance=familytree_Member_strategy)
@settings(max_examples=50)
def test_familytree_member_instantiation(instance):
    assert isinstance(instance, familytree_Member)



@given(instance=familytree_Member_strategy)
def test_familytree_member_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original



@given(instance=familytree_Member_strategy)
def test_familytree_member_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
