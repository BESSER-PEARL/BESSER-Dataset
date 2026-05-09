import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    FamilyMModel::Member,
    FamilyMModel::Family,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_familymmodel::member_is_not_abstract():
    assert not inspect.isabstract(FamilyMModel::Member)


def test_familymmodel::member_constructor_exists():
    assert callable(FamilyMModel::Member.__init__)


def test_familymmodel::member_constructor_args():
    sig = inspect.signature(FamilyMModel::Member.__init__)
    params = list(sig.parameters.keys())
    assert "relation" in params, "Missing parameter 'relation'"
    assert "firstName" in params, "Missing parameter 'firstName'"

def test_familymmodel::member_has_relation():
    assert hasattr(FamilyMModel::Member, "relation")
    descriptor = None
    for klass in FamilyMModel::Member.__mro__:
        if "relation" in klass.__dict__:
            descriptor = klass.__dict__["relation"]
            break
    assert isinstance(descriptor, property)

def test_familymmodel::member_has_firstName():
    assert hasattr(FamilyMModel::Member, "firstName")
    descriptor = None
    for klass in FamilyMModel::Member.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)



def test_familymmodel::family_is_not_abstract():
    assert not inspect.isabstract(FamilyMModel::Family)


def test_familymmodel::family_constructor_exists():
    assert callable(FamilyMModel::Family.__init__)


def test_familymmodel::family_constructor_args():
    sig = inspect.signature(FamilyMModel::Family.__init__)
    params = list(sig.parameters.keys())
    assert "lastName" in params, "Missing parameter 'lastName'"

def test_familymmodel::family_has_lastName():
    assert hasattr(FamilyMModel::Family, "lastName")
    descriptor = None
    for klass in FamilyMModel::Family.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
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
FamilyMModel::Member_strategy = st.builds(
    FamilyMModel::Member,
    relation=
        safe_text,
    firstName=
        safe_text
)
FamilyMModel::Family_strategy = st.builds(
    FamilyMModel::Family,
    lastName=
        safe_text
)

@given(instance=FamilyMModel::Member_strategy)
@settings(max_examples=50)
def test_familymmodel::member_instantiation(instance):
    assert isinstance(instance, FamilyMModel::Member)

@given(instance=FamilyMModel::Member_strategy)
def test_familymmodel::member_relation_type(instance):
    assert isinstance(instance.relation, str)


@given(instance=FamilyMModel::Member_strategy)
def test_familymmodel::member_relation_setter(instance):
    original = instance.relation
    instance.relation = original
    assert instance.relation == original

@given(instance=FamilyMModel::Member_strategy)
def test_familymmodel::member_firstName_type(instance):
    assert isinstance(instance.firstName, str)


@given(instance=FamilyMModel::Member_strategy)
def test_familymmodel::member_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=FamilyMModel::Family_strategy)
@settings(max_examples=50)
def test_familymmodel::family_instantiation(instance):
    assert isinstance(instance, FamilyMModel::Family)

@given(instance=FamilyMModel::Family_strategy)
def test_familymmodel::family_lastName_type(instance):
    assert isinstance(instance.lastName, str)


@given(instance=FamilyMModel::Family_strategy)
def test_familymmodel::family_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original
