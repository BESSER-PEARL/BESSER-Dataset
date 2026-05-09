import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    FamiliesWithSiblings::FamilyMember,
    FamiliesWithSiblings::Family,
    FamiliesWithSiblings::FamilyRegister,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_familieswithsiblings::familymember_is_not_abstract():
    assert not inspect.isabstract(FamiliesWithSiblings::FamilyMember)


def test_familieswithsiblings::familymember_constructor_exists():
    assert callable(FamiliesWithSiblings::FamilyMember.__init__)


def test_familieswithsiblings::familymember_constructor_args():
    sig = inspect.signature(FamiliesWithSiblings::FamilyMember.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_familieswithsiblings::familymember_has_name():
    assert hasattr(FamiliesWithSiblings::FamilyMember, "name")
    descriptor = None
    for klass in FamiliesWithSiblings::FamilyMember.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_familieswithsiblings::family_is_not_abstract():
    assert not inspect.isabstract(FamiliesWithSiblings::Family)


def test_familieswithsiblings::family_constructor_exists():
    assert callable(FamiliesWithSiblings::Family.__init__)


def test_familieswithsiblings::family_constructor_args():
    sig = inspect.signature(FamiliesWithSiblings::Family.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_familieswithsiblings::family_has_name():
    assert hasattr(FamiliesWithSiblings::Family, "name")
    descriptor = None
    for klass in FamiliesWithSiblings::Family.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_familieswithsiblings::familyregister_is_not_abstract():
    assert not inspect.isabstract(FamiliesWithSiblings::FamilyRegister)


def test_familieswithsiblings::familyregister_constructor_exists():
    assert callable(FamiliesWithSiblings::FamilyRegister.__init__)


def test_familieswithsiblings::familyregister_constructor_args():
    sig = inspect.signature(FamiliesWithSiblings::FamilyRegister.__init__)
    params = list(sig.parameters.keys())


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
FamiliesWithSiblings::FamilyMember_strategy = st.builds(
    FamiliesWithSiblings::FamilyMember,
    name=
        safe_text
)
FamiliesWithSiblings::Family_strategy = st.builds(
    FamiliesWithSiblings::Family,
    name=
        safe_text
)
FamiliesWithSiblings::FamilyRegister_strategy = st.builds(
    FamiliesWithSiblings::FamilyRegister,
)

@given(instance=FamiliesWithSiblings::FamilyMember_strategy)
@settings(max_examples=50)
def test_familieswithsiblings::familymember_instantiation(instance):
    assert isinstance(instance, FamiliesWithSiblings::FamilyMember)

@given(instance=FamiliesWithSiblings::FamilyMember_strategy)
def test_familieswithsiblings::familymember_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=FamiliesWithSiblings::FamilyMember_strategy)
def test_familieswithsiblings::familymember_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=FamiliesWithSiblings::Family_strategy)
@settings(max_examples=50)
def test_familieswithsiblings::family_instantiation(instance):
    assert isinstance(instance, FamiliesWithSiblings::Family)

@given(instance=FamiliesWithSiblings::Family_strategy)
def test_familieswithsiblings::family_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=FamiliesWithSiblings::Family_strategy)
def test_familieswithsiblings::family_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=FamiliesWithSiblings::FamilyRegister_strategy)
@settings(max_examples=50)
def test_familieswithsiblings::familyregister_instantiation(instance):
    assert isinstance(instance, FamiliesWithSiblings::FamilyRegister)
