import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    NamedElement,
    persons::Committee,
    persons::District,
    Person,
    persons::Woman,
    persons::Man,
    persons::Association,
    Facility,
    persons::OrdinaryFacility,
    persons::SpecialFacility,
    persons::Facility,
    persons::NamedElement,
    persons::TownHall,
    persons::Person,
    persons::Community,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_persons::committee_is_not_abstract():
    assert not inspect.isabstract(persons::Committee)


def test_persons::committee_constructor_exists():
    assert callable(persons::Committee.__init__)


def test_persons::committee_constructor_args():
    sig = inspect.signature(persons::Committee.__init__)
    params = list(sig.parameters.keys())



def test_persons::district_is_not_abstract():
    assert not inspect.isabstract(persons::District)


def test_persons::district_constructor_exists():
    assert callable(persons::District.__init__)


def test_persons::district_constructor_args():
    sig = inspect.signature(persons::District.__init__)
    params = list(sig.parameters.keys())



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_persons::woman_is_not_abstract():
    assert not inspect.isabstract(persons::Woman)


def test_persons::woman_constructor_exists():
    assert callable(persons::Woman.__init__)


def test_persons::woman_constructor_args():
    sig = inspect.signature(persons::Woman.__init__)
    params = list(sig.parameters.keys())



def test_persons::man_is_not_abstract():
    assert not inspect.isabstract(persons::Man)


def test_persons::man_constructor_exists():
    assert callable(persons::Man.__init__)


def test_persons::man_constructor_args():
    sig = inspect.signature(persons::Man.__init__)
    params = list(sig.parameters.keys())



def test_persons::association_is_not_abstract():
    assert not inspect.isabstract(persons::Association)


def test_persons::association_constructor_exists():
    assert callable(persons::Association.__init__)


def test_persons::association_constructor_args():
    sig = inspect.signature(persons::Association.__init__)
    params = list(sig.parameters.keys())



def test_facility_is_not_abstract():
    assert not inspect.isabstract(Facility)


def test_facility_constructor_exists():
    assert callable(Facility.__init__)


def test_facility_constructor_args():
    sig = inspect.signature(Facility.__init__)
    params = list(sig.parameters.keys())



def test_persons::ordinaryfacility_is_not_abstract():
    assert not inspect.isabstract(persons::OrdinaryFacility)


def test_persons::ordinaryfacility_constructor_exists():
    assert callable(persons::OrdinaryFacility.__init__)


def test_persons::ordinaryfacility_constructor_args():
    sig = inspect.signature(persons::OrdinaryFacility.__init__)
    params = list(sig.parameters.keys())



def test_persons::specialfacility_is_not_abstract():
    assert not inspect.isabstract(persons::SpecialFacility)


def test_persons::specialfacility_constructor_exists():
    assert callable(persons::SpecialFacility.__init__)


def test_persons::specialfacility_constructor_args():
    sig = inspect.signature(persons::SpecialFacility.__init__)
    params = list(sig.parameters.keys())



def test_persons::facility_is_not_abstract():
    assert not inspect.isabstract(persons::Facility)


def test_persons::facility_constructor_exists():
    assert callable(persons::Facility.__init__)


def test_persons::facility_constructor_args():
    sig = inspect.signature(persons::Facility.__init__)
    params = list(sig.parameters.keys())



def test_persons::namedelement_is_not_abstract():
    assert not inspect.isabstract(persons::NamedElement)


def test_persons::namedelement_constructor_exists():
    assert callable(persons::NamedElement.__init__)


def test_persons::namedelement_constructor_args():
    sig = inspect.signature(persons::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_persons::namedelement_has_name():
    assert hasattr(persons::NamedElement, "name")
    descriptor = None
    for klass in persons::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_persons::townhall_is_not_abstract():
    assert not inspect.isabstract(persons::TownHall)


def test_persons::townhall_constructor_exists():
    assert callable(persons::TownHall.__init__)


def test_persons::townhall_constructor_args():
    sig = inspect.signature(persons::TownHall.__init__)
    params = list(sig.parameters.keys())



def test_persons::person_is_not_abstract():
    assert not inspect.isabstract(persons::Person)


def test_persons::person_constructor_exists():
    assert callable(persons::Person.__init__)


def test_persons::person_constructor_args():
    sig = inspect.signature(persons::Person.__init__)
    params = list(sig.parameters.keys())
    assert "fullName" in params, "Missing parameter 'fullName'"

def test_persons::person_has_fullName():
    assert hasattr(persons::Person, "fullName")
    descriptor = None
    for klass in persons::Person.__mro__:
        if "fullName" in klass.__dict__:
            descriptor = klass.__dict__["fullName"]
            break
    assert isinstance(descriptor, property)



def test_persons::community_is_not_abstract():
    assert not inspect.isabstract(persons::Community)


def test_persons::community_constructor_exists():
    assert callable(persons::Community.__init__)


def test_persons::community_constructor_args():
    sig = inspect.signature(persons::Community.__init__)
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
NamedElement_strategy = st.builds(
    NamedElement,
)
persons::Committee_strategy = st.builds(
    persons::Committee,
)
persons::District_strategy = st.builds(
    persons::District,
)
Person_strategy = st.builds(
    Person,
)
persons::Woman_strategy = st.builds(
    persons::Woman,
)
persons::Man_strategy = st.builds(
    persons::Man,
)
persons::Association_strategy = st.builds(
    persons::Association,
)
Facility_strategy = st.builds(
    Facility,
)
persons::OrdinaryFacility_strategy = st.builds(
    persons::OrdinaryFacility,
)
persons::SpecialFacility_strategy = st.builds(
    persons::SpecialFacility,
)
persons::Facility_strategy = st.builds(
    persons::Facility,
)
persons::NamedElement_strategy = st.builds(
    persons::NamedElement,
    name=
        safe_text
)
persons::TownHall_strategy = st.builds(
    persons::TownHall,
)
persons::Person_strategy = st.builds(
    persons::Person,
    fullName=
        safe_text
)
persons::Community_strategy = st.builds(
    persons::Community,
)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=persons::Committee_strategy)
@settings(max_examples=50)
def test_persons::committee_instantiation(instance):
    assert isinstance(instance, persons::Committee)

@given(instance=persons::District_strategy)
@settings(max_examples=50)
def test_persons::district_instantiation(instance):
    assert isinstance(instance, persons::District)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=persons::Woman_strategy)
@settings(max_examples=50)
def test_persons::woman_instantiation(instance):
    assert isinstance(instance, persons::Woman)

@given(instance=persons::Man_strategy)
@settings(max_examples=50)
def test_persons::man_instantiation(instance):
    assert isinstance(instance, persons::Man)

@given(instance=persons::Association_strategy)
@settings(max_examples=50)
def test_persons::association_instantiation(instance):
    assert isinstance(instance, persons::Association)

@given(instance=Facility_strategy)
@settings(max_examples=50)
def test_facility_instantiation(instance):
    assert isinstance(instance, Facility)

@given(instance=persons::OrdinaryFacility_strategy)
@settings(max_examples=50)
def test_persons::ordinaryfacility_instantiation(instance):
    assert isinstance(instance, persons::OrdinaryFacility)

@given(instance=persons::SpecialFacility_strategy)
@settings(max_examples=50)
def test_persons::specialfacility_instantiation(instance):
    assert isinstance(instance, persons::SpecialFacility)

@given(instance=persons::Facility_strategy)
@settings(max_examples=50)
def test_persons::facility_instantiation(instance):
    assert isinstance(instance, persons::Facility)

@given(instance=persons::NamedElement_strategy)
@settings(max_examples=50)
def test_persons::namedelement_instantiation(instance):
    assert isinstance(instance, persons::NamedElement)

@given(instance=persons::NamedElement_strategy)
def test_persons::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=persons::NamedElement_strategy)
def test_persons::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=persons::TownHall_strategy)
@settings(max_examples=50)
def test_persons::townhall_instantiation(instance):
    assert isinstance(instance, persons::TownHall)

@given(instance=persons::Person_strategy)
@settings(max_examples=50)
def test_persons::person_instantiation(instance):
    assert isinstance(instance, persons::Person)

@given(instance=persons::Person_strategy)
def test_persons::person_fullName_type(instance):
    assert isinstance(instance.fullName, str)


@given(instance=persons::Person_strategy)
def test_persons::person_fullName_setter(instance):
    original = instance.fullName
    instance.fullName = original
    assert instance.fullName == original

@given(instance=persons::Community_strategy)
@settings(max_examples=50)
def test_persons::community_instantiation(instance):
    assert isinstance(instance, persons::Community)
