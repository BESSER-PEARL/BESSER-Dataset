import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    FamilyRegister::Member,
    FamilyRegister::Family,
    FamilyRegister::FamilyRegister,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_familyregister::member_is_not_abstract():
    assert not inspect.isabstract(FamilyRegister::Member)


def test_familyregister::member_constructor_exists():
    assert callable(FamilyRegister::Member.__init__)


def test_familyregister::member_constructor_args():
    sig = inspect.signature(FamilyRegister::Member.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_familyregister::member_has_name():
    assert hasattr(FamilyRegister::Member, "name")
    descriptor = None
    for klass in FamilyRegister::Member.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_familyregister::family_is_not_abstract():
    assert not inspect.isabstract(FamilyRegister::Family)


def test_familyregister::family_constructor_exists():
    assert callable(FamilyRegister::Family.__init__)


def test_familyregister::family_constructor_args():
    sig = inspect.signature(FamilyRegister::Family.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_familyregister::family_has_name():
    assert hasattr(FamilyRegister::Family, "name")
    descriptor = None
    for klass in FamilyRegister::Family.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_familyregister::familyregister_is_not_abstract():
    assert not inspect.isabstract(FamilyRegister::FamilyRegister)


def test_familyregister::familyregister_constructor_exists():
    assert callable(FamilyRegister::FamilyRegister.__init__)


def test_familyregister::familyregister_constructor_args():
    sig = inspect.signature(FamilyRegister::FamilyRegister.__init__)
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
FamilyRegister::Member_strategy = st.builds(
    FamilyRegister::Member,
    name=
        safe_text
)
FamilyRegister::Family_strategy = st.builds(
    FamilyRegister::Family,
    name=
        safe_text
)
FamilyRegister::FamilyRegister_strategy = st.builds(
    FamilyRegister::FamilyRegister,
)

@given(instance=FamilyRegister::Member_strategy)
@settings(max_examples=50)
def test_familyregister::member_instantiation(instance):
    assert isinstance(instance, FamilyRegister::Member)

@given(instance=FamilyRegister::Member_strategy)
def test_familyregister::member_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=FamilyRegister::Member_strategy)
def test_familyregister::member_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=FamilyRegister::Family_strategy)
@settings(max_examples=50)
def test_familyregister::family_instantiation(instance):
    assert isinstance(instance, FamilyRegister::Family)

@given(instance=FamilyRegister::Family_strategy)
def test_familyregister::family_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=FamilyRegister::Family_strategy)
def test_familyregister::family_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=FamilyRegister::FamilyRegister_strategy)
@settings(max_examples=50)
def test_familyregister::familyregister_instantiation(instance):
    assert isinstance(instance, FamilyRegister::FamilyRegister)
