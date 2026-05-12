import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    FamilyMModel_Member,
    FamilyMModel_Family,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_familymmodel_member_is_not_abstract():
    assert not inspect.isabstract(FamilyMModel_Member)


def test_familymmodel_member_constructor_exists():
    assert callable(FamilyMModel_Member.__init__)


def test_familymmodel_member_constructor_args():
    sig = inspect.signature(FamilyMModel_Member.__init__)
    params = list(sig.parameters.keys())
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "relation" in params, "Missing parameter 'relation'"

def test_familymmodel_member_has_firstName():
    assert hasattr(FamilyMModel_Member, "firstName")
    descriptor = None
    for klass in FamilyMModel_Member.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_familymmodel_member_has_relation():
    assert hasattr(FamilyMModel_Member, "relation")
    descriptor = None
    for klass in FamilyMModel_Member.__mro__:
        if "relation" in klass.__dict__:
            descriptor = klass.__dict__["relation"]
            break
    assert isinstance(descriptor, property)



def test_familymmodel_family_is_not_abstract():
    assert not inspect.isabstract(FamilyMModel_Family)


def test_familymmodel_family_constructor_exists():
    assert callable(FamilyMModel_Family.__init__)


def test_familymmodel_family_constructor_args():
    sig = inspect.signature(FamilyMModel_Family.__init__)
    params = list(sig.parameters.keys())
    assert "lastName" in params, "Missing parameter 'lastName'"

def test_familymmodel_family_has_lastName():
    assert hasattr(FamilyMModel_Family, "lastName")
    descriptor = None
    for klass in FamilyMModel_Family.__mro__:
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
FamilyMModel_Member_strategy = st.builds(
    FamilyMModel_Member,
    firstName=
        safe_text,
    relation=
        safe_text
)
FamilyMModel_Family_strategy = st.builds(
    FamilyMModel_Family,
    lastName=
        safe_text
)

@given(instance=FamilyMModel_Member_strategy)
@settings(max_examples=50)
def test_familymmodel_member_instantiation(instance):
    assert isinstance(instance, FamilyMModel_Member)



@given(instance=FamilyMModel_Member_strategy)
def test_familymmodel_member_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original



@given(instance=FamilyMModel_Member_strategy)
def test_familymmodel_member_relation_setter(instance):
    original = instance.relation
    instance.relation = original
    assert instance.relation == original

@given(instance=FamilyMModel_Family_strategy)
@settings(max_examples=50)
def test_familymmodel_family_instantiation(instance):
    assert isinstance(instance, FamilyMModel_Family)



@given(instance=FamilyMModel_Family_strategy)
def test_familymmodel_family_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original
