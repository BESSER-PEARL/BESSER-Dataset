import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    SimpleFamilies::FamilyMember,
    SimpleFamilies::Family,
    SimpleFamilies::FamilyRegister,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simplefamilies::familymember_is_not_abstract():
    assert not inspect.isabstract(SimpleFamilies::FamilyMember)


def test_simplefamilies::familymember_constructor_exists():
    assert callable(SimpleFamilies::FamilyMember.__init__)


def test_simplefamilies::familymember_constructor_args():
    sig = inspect.signature(SimpleFamilies::FamilyMember.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplefamilies::familymember_has_name():
    assert hasattr(SimpleFamilies::FamilyMember, "name")
    descriptor = None
    for klass in SimpleFamilies::FamilyMember.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplefamilies::family_is_not_abstract():
    assert not inspect.isabstract(SimpleFamilies::Family)


def test_simplefamilies::family_constructor_exists():
    assert callable(SimpleFamilies::Family.__init__)


def test_simplefamilies::family_constructor_args():
    sig = inspect.signature(SimpleFamilies::Family.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplefamilies::family_has_name():
    assert hasattr(SimpleFamilies::Family, "name")
    descriptor = None
    for klass in SimpleFamilies::Family.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplefamilies::familyregister_is_not_abstract():
    assert not inspect.isabstract(SimpleFamilies::FamilyRegister)


def test_simplefamilies::familyregister_constructor_exists():
    assert callable(SimpleFamilies::FamilyRegister.__init__)


def test_simplefamilies::familyregister_constructor_args():
    sig = inspect.signature(SimpleFamilies::FamilyRegister.__init__)
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
SimpleFamilies::FamilyMember_strategy = st.builds(
    SimpleFamilies::FamilyMember,
    name=
        safe_text
)
SimpleFamilies::Family_strategy = st.builds(
    SimpleFamilies::Family,
    name=
        safe_text
)
SimpleFamilies::FamilyRegister_strategy = st.builds(
    SimpleFamilies::FamilyRegister,
)

@given(instance=SimpleFamilies::FamilyMember_strategy)
@settings(max_examples=50)
def test_simplefamilies::familymember_instantiation(instance):
    assert isinstance(instance, SimpleFamilies::FamilyMember)

@given(instance=SimpleFamilies::FamilyMember_strategy)
def test_simplefamilies::familymember_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SimpleFamilies::FamilyMember_strategy)
def test_simplefamilies::familymember_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SimpleFamilies::Family_strategy)
@settings(max_examples=50)
def test_simplefamilies::family_instantiation(instance):
    assert isinstance(instance, SimpleFamilies::Family)

@given(instance=SimpleFamilies::Family_strategy)
def test_simplefamilies::family_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SimpleFamilies::Family_strategy)
def test_simplefamilies::family_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SimpleFamilies::FamilyRegister_strategy)
@settings(max_examples=50)
def test_simplefamilies::familyregister_instantiation(instance):
    assert isinstance(instance, SimpleFamilies::FamilyRegister)
