import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    SimpleFamilies_FamilyMember,
    SimpleFamilies_Family,
    SimpleFamilies_FamilyRegister,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simplefamilies_familymember_is_not_abstract():
    assert not inspect.isabstract(SimpleFamilies_FamilyMember)


def test_simplefamilies_familymember_constructor_exists():
    assert callable(SimpleFamilies_FamilyMember.__init__)


def test_simplefamilies_familymember_constructor_args():
    sig = inspect.signature(SimpleFamilies_FamilyMember.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplefamilies_familymember_has_name():
    assert hasattr(SimpleFamilies_FamilyMember, "name")
    descriptor = None
    for klass in SimpleFamilies_FamilyMember.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplefamilies_family_is_not_abstract():
    assert not inspect.isabstract(SimpleFamilies_Family)


def test_simplefamilies_family_constructor_exists():
    assert callable(SimpleFamilies_Family.__init__)


def test_simplefamilies_family_constructor_args():
    sig = inspect.signature(SimpleFamilies_Family.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplefamilies_family_has_name():
    assert hasattr(SimpleFamilies_Family, "name")
    descriptor = None
    for klass in SimpleFamilies_Family.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplefamilies_familyregister_is_not_abstract():
    assert not inspect.isabstract(SimpleFamilies_FamilyRegister)


def test_simplefamilies_familyregister_constructor_exists():
    assert callable(SimpleFamilies_FamilyRegister.__init__)


def test_simplefamilies_familyregister_constructor_args():
    sig = inspect.signature(SimpleFamilies_FamilyRegister.__init__)
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
SimpleFamilies_FamilyMember_strategy = st.builds(
    SimpleFamilies_FamilyMember,
    name=
        safe_text
)
SimpleFamilies_Family_strategy = st.builds(
    SimpleFamilies_Family,
    name=
        safe_text
)
SimpleFamilies_FamilyRegister_strategy = st.builds(
    SimpleFamilies_FamilyRegister,
)

@given(instance=SimpleFamilies_FamilyMember_strategy)
@settings(max_examples=50)
def test_simplefamilies_familymember_instantiation(instance):
    assert isinstance(instance, SimpleFamilies_FamilyMember)



@given(instance=SimpleFamilies_FamilyMember_strategy)
def test_simplefamilies_familymember_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SimpleFamilies_Family_strategy)
@settings(max_examples=50)
def test_simplefamilies_family_instantiation(instance):
    assert isinstance(instance, SimpleFamilies_Family)



@given(instance=SimpleFamilies_Family_strategy)
def test_simplefamilies_family_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SimpleFamilies_FamilyRegister_strategy)
@settings(max_examples=50)
def test_simplefamilies_familyregister_instantiation(instance):
    assert isinstance(instance, SimpleFamilies_FamilyRegister)
