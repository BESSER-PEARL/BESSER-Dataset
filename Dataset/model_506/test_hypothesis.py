import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Families::FamilyMember,
    Families::Family,
    Families::FamilyRegister,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_families::familymember_is_not_abstract():
    assert not inspect.isabstract(Families::FamilyMember)


def test_families::familymember_constructor_exists():
    assert callable(Families::FamilyMember.__init__)


def test_families::familymember_constructor_args():
    sig = inspect.signature(Families::FamilyMember.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_families::familymember_has_name():
    assert hasattr(Families::FamilyMember, "name")
    descriptor = None
    for klass in Families::FamilyMember.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_families::family_is_not_abstract():
    assert not inspect.isabstract(Families::Family)


def test_families::family_constructor_exists():
    assert callable(Families::Family.__init__)


def test_families::family_constructor_args():
    sig = inspect.signature(Families::Family.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_families::family_has_name():
    assert hasattr(Families::Family, "name")
    descriptor = None
    for klass in Families::Family.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_families::familyregister_is_not_abstract():
    assert not inspect.isabstract(Families::FamilyRegister)


def test_families::familyregister_constructor_exists():
    assert callable(Families::FamilyRegister.__init__)


def test_families::familyregister_constructor_args():
    sig = inspect.signature(Families::FamilyRegister.__init__)
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
Families::FamilyMember_strategy = st.builds(
    Families::FamilyMember,
    name=
        safe_text
)
Families::Family_strategy = st.builds(
    Families::Family,
    name=
        safe_text
)
Families::FamilyRegister_strategy = st.builds(
    Families::FamilyRegister,
)

@given(instance=Families::FamilyMember_strategy)
@settings(max_examples=50)
def test_families::familymember_instantiation(instance):
    assert isinstance(instance, Families::FamilyMember)

@given(instance=Families::FamilyMember_strategy)
def test_families::familymember_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Families::FamilyMember_strategy)
def test_families::familymember_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Families::Family_strategy)
@settings(max_examples=50)
def test_families::family_instantiation(instance):
    assert isinstance(instance, Families::Family)

@given(instance=Families::Family_strategy)
def test_families::family_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Families::Family_strategy)
def test_families::family_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Families::FamilyRegister_strategy)
@settings(max_examples=50)
def test_families::familyregister_instantiation(instance):
    assert isinstance(instance, Families::FamilyRegister)
