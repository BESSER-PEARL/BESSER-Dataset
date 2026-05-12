import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Persons_NamedElement,
    Facility,
    Persons_OrdinaryFacility,
    Persons_SpecialFacility,
    NamedElement,
    Persons_Committee,
    Persons_Facility,
    Persons_District,
    Person,
    Persons_Woman,
    Persons_Man,
    Persons_Association,
    Persons_TownHall,
    Persons_Person,
    Persons_Community,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_persons_namedelement_is_not_abstract():
    assert not inspect.isabstract(Persons_NamedElement)


def test_persons_namedelement_constructor_exists():
    assert callable(Persons_NamedElement.__init__)


def test_persons_namedelement_constructor_args():
    sig = inspect.signature(Persons_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_persons_namedelement_has_name():
    assert hasattr(Persons_NamedElement, "name")
    descriptor = None
    for klass in Persons_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_facility_is_not_abstract():
    assert not inspect.isabstract(Facility)


def test_facility_constructor_exists():
    assert callable(Facility.__init__)


def test_facility_constructor_args():
    sig = inspect.signature(Facility.__init__)
    params = list(sig.parameters.keys())



def test_persons_ordinaryfacility_is_not_abstract():
    assert not inspect.isabstract(Persons_OrdinaryFacility)


def test_persons_ordinaryfacility_constructor_exists():
    assert callable(Persons_OrdinaryFacility.__init__)


def test_persons_ordinaryfacility_constructor_args():
    sig = inspect.signature(Persons_OrdinaryFacility.__init__)
    params = list(sig.parameters.keys())



def test_persons_specialfacility_is_not_abstract():
    assert not inspect.isabstract(Persons_SpecialFacility)


def test_persons_specialfacility_constructor_exists():
    assert callable(Persons_SpecialFacility.__init__)


def test_persons_specialfacility_constructor_args():
    sig = inspect.signature(Persons_SpecialFacility.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_persons_committee_is_not_abstract():
    assert not inspect.isabstract(Persons_Committee)


def test_persons_committee_constructor_exists():
    assert callable(Persons_Committee.__init__)


def test_persons_committee_constructor_args():
    sig = inspect.signature(Persons_Committee.__init__)
    params = list(sig.parameters.keys())



def test_persons_facility_is_not_abstract():
    assert not inspect.isabstract(Persons_Facility)


def test_persons_facility_constructor_exists():
    assert callable(Persons_Facility.__init__)


def test_persons_facility_constructor_args():
    sig = inspect.signature(Persons_Facility.__init__)
    params = list(sig.parameters.keys())



def test_persons_district_is_not_abstract():
    assert not inspect.isabstract(Persons_District)


def test_persons_district_constructor_exists():
    assert callable(Persons_District.__init__)


def test_persons_district_constructor_args():
    sig = inspect.signature(Persons_District.__init__)
    params = list(sig.parameters.keys())



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_persons_woman_is_not_abstract():
    assert not inspect.isabstract(Persons_Woman)


def test_persons_woman_constructor_exists():
    assert callable(Persons_Woman.__init__)


def test_persons_woman_constructor_args():
    sig = inspect.signature(Persons_Woman.__init__)
    params = list(sig.parameters.keys())



def test_persons_man_is_not_abstract():
    assert not inspect.isabstract(Persons_Man)


def test_persons_man_constructor_exists():
    assert callable(Persons_Man.__init__)


def test_persons_man_constructor_args():
    sig = inspect.signature(Persons_Man.__init__)
    params = list(sig.parameters.keys())



def test_persons_association_is_not_abstract():
    assert not inspect.isabstract(Persons_Association)


def test_persons_association_constructor_exists():
    assert callable(Persons_Association.__init__)


def test_persons_association_constructor_args():
    sig = inspect.signature(Persons_Association.__init__)
    params = list(sig.parameters.keys())



def test_persons_townhall_is_not_abstract():
    assert not inspect.isabstract(Persons_TownHall)


def test_persons_townhall_constructor_exists():
    assert callable(Persons_TownHall.__init__)


def test_persons_townhall_constructor_args():
    sig = inspect.signature(Persons_TownHall.__init__)
    params = list(sig.parameters.keys())



def test_persons_person_is_not_abstract():
    assert not inspect.isabstract(Persons_Person)


def test_persons_person_constructor_exists():
    assert callable(Persons_Person.__init__)


def test_persons_person_constructor_args():
    sig = inspect.signature(Persons_Person.__init__)
    params = list(sig.parameters.keys())
    assert "fullName" in params, "Missing parameter 'fullName'"

def test_persons_person_has_fullName():
    assert hasattr(Persons_Person, "fullName")
    descriptor = None
    for klass in Persons_Person.__mro__:
        if "fullName" in klass.__dict__:
            descriptor = klass.__dict__["fullName"]
            break
    assert isinstance(descriptor, property)



def test_persons_community_is_not_abstract():
    assert not inspect.isabstract(Persons_Community)


def test_persons_community_constructor_exists():
    assert callable(Persons_Community.__init__)


def test_persons_community_constructor_args():
    sig = inspect.signature(Persons_Community.__init__)
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
Persons_NamedElement_strategy = st.builds(
    Persons_NamedElement,
    name=
        safe_text
)
Facility_strategy = st.builds(
    Facility,
)
Persons_OrdinaryFacility_strategy = st.builds(
    Persons_OrdinaryFacility,
)
Persons_SpecialFacility_strategy = st.builds(
    Persons_SpecialFacility,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
Persons_Committee_strategy = st.builds(
    Persons_Committee,
)
Persons_Facility_strategy = st.builds(
    Persons_Facility,
)
Persons_District_strategy = st.builds(
    Persons_District,
)
Person_strategy = st.builds(
    Person,
)
Persons_Woman_strategy = st.builds(
    Persons_Woman,
)
Persons_Man_strategy = st.builds(
    Persons_Man,
)
Persons_Association_strategy = st.builds(
    Persons_Association,
)
Persons_TownHall_strategy = st.builds(
    Persons_TownHall,
)
Persons_Person_strategy = st.builds(
    Persons_Person,
    fullName=
        safe_text
)
Persons_Community_strategy = st.builds(
    Persons_Community,
)

@given(instance=Persons_NamedElement_strategy)
@settings(max_examples=50)
def test_persons_namedelement_instantiation(instance):
    assert isinstance(instance, Persons_NamedElement)



@given(instance=Persons_NamedElement_strategy)
def test_persons_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Facility_strategy)
@settings(max_examples=50)
def test_facility_instantiation(instance):
    assert isinstance(instance, Facility)

@given(instance=Persons_OrdinaryFacility_strategy)
@settings(max_examples=50)
def test_persons_ordinaryfacility_instantiation(instance):
    assert isinstance(instance, Persons_OrdinaryFacility)

@given(instance=Persons_SpecialFacility_strategy)
@settings(max_examples=50)
def test_persons_specialfacility_instantiation(instance):
    assert isinstance(instance, Persons_SpecialFacility)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=Persons_Committee_strategy)
@settings(max_examples=50)
def test_persons_committee_instantiation(instance):
    assert isinstance(instance, Persons_Committee)

@given(instance=Persons_Facility_strategy)
@settings(max_examples=50)
def test_persons_facility_instantiation(instance):
    assert isinstance(instance, Persons_Facility)

@given(instance=Persons_District_strategy)
@settings(max_examples=50)
def test_persons_district_instantiation(instance):
    assert isinstance(instance, Persons_District)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=Persons_Woman_strategy)
@settings(max_examples=50)
def test_persons_woman_instantiation(instance):
    assert isinstance(instance, Persons_Woman)

@given(instance=Persons_Man_strategy)
@settings(max_examples=50)
def test_persons_man_instantiation(instance):
    assert isinstance(instance, Persons_Man)

@given(instance=Persons_Association_strategy)
@settings(max_examples=50)
def test_persons_association_instantiation(instance):
    assert isinstance(instance, Persons_Association)

@given(instance=Persons_TownHall_strategy)
@settings(max_examples=50)
def test_persons_townhall_instantiation(instance):
    assert isinstance(instance, Persons_TownHall)

@given(instance=Persons_Person_strategy)
@settings(max_examples=50)
def test_persons_person_instantiation(instance):
    assert isinstance(instance, Persons_Person)



@given(instance=Persons_Person_strategy)
def test_persons_person_fullName_setter(instance):
    original = instance.fullName
    instance.fullName = original
    assert instance.fullName == original

@given(instance=Persons_Community_strategy)
@settings(max_examples=50)
def test_persons_community_instantiation(instance):
    assert isinstance(instance, Persons_Community)
