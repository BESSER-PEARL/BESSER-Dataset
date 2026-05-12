import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Facility,
    persons_OrdinaryFacility,
    persons_SpecialFacility,
    persons_NamedElement,
    NamedElement,
    persons_Facility,
    Person,
    persons_Woman,
    persons_Man,
    persons_Association,
    persons_TownHall,
    persons_Person,
    persons_Community,
    persons_District,
    persons_Committee,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_facility_is_not_abstract():
    assert not inspect.isabstract(Facility)


def test_facility_constructor_exists():
    assert callable(Facility.__init__)


def test_facility_constructor_args():
    sig = inspect.signature(Facility.__init__)
    params = list(sig.parameters.keys())



def test_persons_ordinaryfacility_is_not_abstract():
    assert not inspect.isabstract(persons_OrdinaryFacility)


def test_persons_ordinaryfacility_constructor_exists():
    assert callable(persons_OrdinaryFacility.__init__)


def test_persons_ordinaryfacility_constructor_args():
    sig = inspect.signature(persons_OrdinaryFacility.__init__)
    params = list(sig.parameters.keys())



def test_persons_specialfacility_is_not_abstract():
    assert not inspect.isabstract(persons_SpecialFacility)


def test_persons_specialfacility_constructor_exists():
    assert callable(persons_SpecialFacility.__init__)


def test_persons_specialfacility_constructor_args():
    sig = inspect.signature(persons_SpecialFacility.__init__)
    params = list(sig.parameters.keys())



def test_persons_namedelement_is_not_abstract():
    assert not inspect.isabstract(persons_NamedElement)


def test_persons_namedelement_constructor_exists():
    assert callable(persons_NamedElement.__init__)


def test_persons_namedelement_constructor_args():
    sig = inspect.signature(persons_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_persons_namedelement_has_name():
    assert hasattr(persons_NamedElement, "name")
    descriptor = None
    for klass in persons_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_persons_facility_is_not_abstract():
    assert not inspect.isabstract(persons_Facility)


def test_persons_facility_constructor_exists():
    assert callable(persons_Facility.__init__)


def test_persons_facility_constructor_args():
    sig = inspect.signature(persons_Facility.__init__)
    params = list(sig.parameters.keys())



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_persons_woman_is_not_abstract():
    assert not inspect.isabstract(persons_Woman)


def test_persons_woman_constructor_exists():
    assert callable(persons_Woman.__init__)


def test_persons_woman_constructor_args():
    sig = inspect.signature(persons_Woman.__init__)
    params = list(sig.parameters.keys())



def test_persons_man_is_not_abstract():
    assert not inspect.isabstract(persons_Man)


def test_persons_man_constructor_exists():
    assert callable(persons_Man.__init__)


def test_persons_man_constructor_args():
    sig = inspect.signature(persons_Man.__init__)
    params = list(sig.parameters.keys())



def test_persons_association_is_not_abstract():
    assert not inspect.isabstract(persons_Association)


def test_persons_association_constructor_exists():
    assert callable(persons_Association.__init__)


def test_persons_association_constructor_args():
    sig = inspect.signature(persons_Association.__init__)
    params = list(sig.parameters.keys())



def test_persons_townhall_is_not_abstract():
    assert not inspect.isabstract(persons_TownHall)


def test_persons_townhall_constructor_exists():
    assert callable(persons_TownHall.__init__)


def test_persons_townhall_constructor_args():
    sig = inspect.signature(persons_TownHall.__init__)
    params = list(sig.parameters.keys())



def test_persons_person_is_not_abstract():
    assert not inspect.isabstract(persons_Person)


def test_persons_person_constructor_exists():
    assert callable(persons_Person.__init__)


def test_persons_person_constructor_args():
    sig = inspect.signature(persons_Person.__init__)
    params = list(sig.parameters.keys())
    assert "fullName" in params, "Missing parameter 'fullName'"

def test_persons_person_has_fullName():
    assert hasattr(persons_Person, "fullName")
    descriptor = None
    for klass in persons_Person.__mro__:
        if "fullName" in klass.__dict__:
            descriptor = klass.__dict__["fullName"]
            break
    assert isinstance(descriptor, property)



def test_persons_community_is_not_abstract():
    assert not inspect.isabstract(persons_Community)


def test_persons_community_constructor_exists():
    assert callable(persons_Community.__init__)


def test_persons_community_constructor_args():
    sig = inspect.signature(persons_Community.__init__)
    params = list(sig.parameters.keys())



def test_persons_district_is_not_abstract():
    assert not inspect.isabstract(persons_District)


def test_persons_district_constructor_exists():
    assert callable(persons_District.__init__)


def test_persons_district_constructor_args():
    sig = inspect.signature(persons_District.__init__)
    params = list(sig.parameters.keys())



def test_persons_committee_is_not_abstract():
    assert not inspect.isabstract(persons_Committee)


def test_persons_committee_constructor_exists():
    assert callable(persons_Committee.__init__)


def test_persons_committee_constructor_args():
    sig = inspect.signature(persons_Committee.__init__)
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
Facility_strategy = st.builds(
    Facility,
)
persons_OrdinaryFacility_strategy = st.builds(
    persons_OrdinaryFacility,
)
persons_SpecialFacility_strategy = st.builds(
    persons_SpecialFacility,
)
persons_NamedElement_strategy = st.builds(
    persons_NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
persons_Facility_strategy = st.builds(
    persons_Facility,
)
Person_strategy = st.builds(
    Person,
)
persons_Woman_strategy = st.builds(
    persons_Woman,
)
persons_Man_strategy = st.builds(
    persons_Man,
)
persons_Association_strategy = st.builds(
    persons_Association,
)
persons_TownHall_strategy = st.builds(
    persons_TownHall,
)
persons_Person_strategy = st.builds(
    persons_Person,
    fullName=
        safe_text
)
persons_Community_strategy = st.builds(
    persons_Community,
)
persons_District_strategy = st.builds(
    persons_District,
)
persons_Committee_strategy = st.builds(
    persons_Committee,
)

@given(instance=Facility_strategy)
@settings(max_examples=50)
def test_facility_instantiation(instance):
    assert isinstance(instance, Facility)

@given(instance=persons_OrdinaryFacility_strategy)
@settings(max_examples=50)
def test_persons_ordinaryfacility_instantiation(instance):
    assert isinstance(instance, persons_OrdinaryFacility)

@given(instance=persons_SpecialFacility_strategy)
@settings(max_examples=50)
def test_persons_specialfacility_instantiation(instance):
    assert isinstance(instance, persons_SpecialFacility)

@given(instance=persons_NamedElement_strategy)
@settings(max_examples=50)
def test_persons_namedelement_instantiation(instance):
    assert isinstance(instance, persons_NamedElement)



@given(instance=persons_NamedElement_strategy)
def test_persons_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=persons_Facility_strategy)
@settings(max_examples=50)
def test_persons_facility_instantiation(instance):
    assert isinstance(instance, persons_Facility)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=persons_Woman_strategy)
@settings(max_examples=50)
def test_persons_woman_instantiation(instance):
    assert isinstance(instance, persons_Woman)

@given(instance=persons_Man_strategy)
@settings(max_examples=50)
def test_persons_man_instantiation(instance):
    assert isinstance(instance, persons_Man)

@given(instance=persons_Association_strategy)
@settings(max_examples=50)
def test_persons_association_instantiation(instance):
    assert isinstance(instance, persons_Association)

@given(instance=persons_TownHall_strategy)
@settings(max_examples=50)
def test_persons_townhall_instantiation(instance):
    assert isinstance(instance, persons_TownHall)

@given(instance=persons_Person_strategy)
@settings(max_examples=50)
def test_persons_person_instantiation(instance):
    assert isinstance(instance, persons_Person)



@given(instance=persons_Person_strategy)
def test_persons_person_fullName_setter(instance):
    original = instance.fullName
    instance.fullName = original
    assert instance.fullName == original

@given(instance=persons_Community_strategy)
@settings(max_examples=50)
def test_persons_community_instantiation(instance):
    assert isinstance(instance, persons_Community)

@given(instance=persons_District_strategy)
@settings(max_examples=50)
def test_persons_district_instantiation(instance):
    assert isinstance(instance, persons_District)

@given(instance=persons_Committee_strategy)
@settings(max_examples=50)
def test_persons_committee_instantiation(instance):
    assert isinstance(instance, persons_Committee)
