import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Persons::NamedElement,
    Facility,
    Persons::OrdinaryFacility,
    Persons::SpecialFacility,
    NamedElement,
    Persons::District,
    Persons::Facility,
    Persons::Committee,
    Person,
    Persons::Woman,
    Persons::Man,
    Persons::Association,
    Persons::TownHall,
    Persons::Person,
    Persons::Community,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_persons::namedelement_is_not_abstract():
    assert not inspect.isabstract(Persons::NamedElement)


def test_persons::namedelement_constructor_exists():
    assert callable(Persons::NamedElement.__init__)


def test_persons::namedelement_constructor_args():
    sig = inspect.signature(Persons::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_persons::namedelement_has_name():
    assert hasattr(Persons::NamedElement, "name")
    descriptor = None
    for klass in Persons::NamedElement.__mro__:
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



def test_persons::ordinaryfacility_is_not_abstract():
    assert not inspect.isabstract(Persons::OrdinaryFacility)


def test_persons::ordinaryfacility_constructor_exists():
    assert callable(Persons::OrdinaryFacility.__init__)


def test_persons::ordinaryfacility_constructor_args():
    sig = inspect.signature(Persons::OrdinaryFacility.__init__)
    params = list(sig.parameters.keys())



def test_persons::specialfacility_is_not_abstract():
    assert not inspect.isabstract(Persons::SpecialFacility)


def test_persons::specialfacility_constructor_exists():
    assert callable(Persons::SpecialFacility.__init__)


def test_persons::specialfacility_constructor_args():
    sig = inspect.signature(Persons::SpecialFacility.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_persons::district_is_not_abstract():
    assert not inspect.isabstract(Persons::District)


def test_persons::district_constructor_exists():
    assert callable(Persons::District.__init__)


def test_persons::district_constructor_args():
    sig = inspect.signature(Persons::District.__init__)
    params = list(sig.parameters.keys())



def test_persons::facility_is_not_abstract():
    assert not inspect.isabstract(Persons::Facility)


def test_persons::facility_constructor_exists():
    assert callable(Persons::Facility.__init__)


def test_persons::facility_constructor_args():
    sig = inspect.signature(Persons::Facility.__init__)
    params = list(sig.parameters.keys())



def test_persons::committee_is_not_abstract():
    assert not inspect.isabstract(Persons::Committee)


def test_persons::committee_constructor_exists():
    assert callable(Persons::Committee.__init__)


def test_persons::committee_constructor_args():
    sig = inspect.signature(Persons::Committee.__init__)
    params = list(sig.parameters.keys())



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_persons::woman_is_not_abstract():
    assert not inspect.isabstract(Persons::Woman)


def test_persons::woman_constructor_exists():
    assert callable(Persons::Woman.__init__)


def test_persons::woman_constructor_args():
    sig = inspect.signature(Persons::Woman.__init__)
    params = list(sig.parameters.keys())



def test_persons::man_is_not_abstract():
    assert not inspect.isabstract(Persons::Man)


def test_persons::man_constructor_exists():
    assert callable(Persons::Man.__init__)


def test_persons::man_constructor_args():
    sig = inspect.signature(Persons::Man.__init__)
    params = list(sig.parameters.keys())



def test_persons::association_is_not_abstract():
    assert not inspect.isabstract(Persons::Association)


def test_persons::association_constructor_exists():
    assert callable(Persons::Association.__init__)


def test_persons::association_constructor_args():
    sig = inspect.signature(Persons::Association.__init__)
    params = list(sig.parameters.keys())



def test_persons::townhall_is_not_abstract():
    assert not inspect.isabstract(Persons::TownHall)


def test_persons::townhall_constructor_exists():
    assert callable(Persons::TownHall.__init__)


def test_persons::townhall_constructor_args():
    sig = inspect.signature(Persons::TownHall.__init__)
    params = list(sig.parameters.keys())



def test_persons::person_is_not_abstract():
    assert not inspect.isabstract(Persons::Person)


def test_persons::person_constructor_exists():
    assert callable(Persons::Person.__init__)


def test_persons::person_constructor_args():
    sig = inspect.signature(Persons::Person.__init__)
    params = list(sig.parameters.keys())
    assert "fullName" in params, "Missing parameter 'fullName'"

def test_persons::person_has_fullName():
    assert hasattr(Persons::Person, "fullName")
    descriptor = None
    for klass in Persons::Person.__mro__:
        if "fullName" in klass.__dict__:
            descriptor = klass.__dict__["fullName"]
            break
    assert isinstance(descriptor, property)



def test_persons::community_is_not_abstract():
    assert not inspect.isabstract(Persons::Community)


def test_persons::community_constructor_exists():
    assert callable(Persons::Community.__init__)


def test_persons::community_constructor_args():
    sig = inspect.signature(Persons::Community.__init__)
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
Persons::NamedElement_strategy = st.builds(
    Persons::NamedElement,
    name=
        safe_text
)
Facility_strategy = st.builds(
    Facility,
)
Persons::OrdinaryFacility_strategy = st.builds(
    Persons::OrdinaryFacility,
)
Persons::SpecialFacility_strategy = st.builds(
    Persons::SpecialFacility,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
Persons::District_strategy = st.builds(
    Persons::District,
)
Persons::Facility_strategy = st.builds(
    Persons::Facility,
)
Persons::Committee_strategy = st.builds(
    Persons::Committee,
)
Person_strategy = st.builds(
    Person,
)
Persons::Woman_strategy = st.builds(
    Persons::Woman,
)
Persons::Man_strategy = st.builds(
    Persons::Man,
)
Persons::Association_strategy = st.builds(
    Persons::Association,
)
Persons::TownHall_strategy = st.builds(
    Persons::TownHall,
)
Persons::Person_strategy = st.builds(
    Persons::Person,
    fullName=
        safe_text
)
Persons::Community_strategy = st.builds(
    Persons::Community,
)

@given(instance=Persons::NamedElement_strategy)
@settings(max_examples=50)
def test_persons::namedelement_instantiation(instance):
    assert isinstance(instance, Persons::NamedElement)

@given(instance=Persons::NamedElement_strategy)
def test_persons::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Persons::NamedElement_strategy)
def test_persons::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Facility_strategy)
@settings(max_examples=50)
def test_facility_instantiation(instance):
    assert isinstance(instance, Facility)

@given(instance=Persons::OrdinaryFacility_strategy)
@settings(max_examples=50)
def test_persons::ordinaryfacility_instantiation(instance):
    assert isinstance(instance, Persons::OrdinaryFacility)

@given(instance=Persons::SpecialFacility_strategy)
@settings(max_examples=50)
def test_persons::specialfacility_instantiation(instance):
    assert isinstance(instance, Persons::SpecialFacility)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=Persons::District_strategy)
@settings(max_examples=50)
def test_persons::district_instantiation(instance):
    assert isinstance(instance, Persons::District)

@given(instance=Persons::Facility_strategy)
@settings(max_examples=50)
def test_persons::facility_instantiation(instance):
    assert isinstance(instance, Persons::Facility)

@given(instance=Persons::Committee_strategy)
@settings(max_examples=50)
def test_persons::committee_instantiation(instance):
    assert isinstance(instance, Persons::Committee)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=Persons::Woman_strategy)
@settings(max_examples=50)
def test_persons::woman_instantiation(instance):
    assert isinstance(instance, Persons::Woman)

@given(instance=Persons::Man_strategy)
@settings(max_examples=50)
def test_persons::man_instantiation(instance):
    assert isinstance(instance, Persons::Man)

@given(instance=Persons::Association_strategy)
@settings(max_examples=50)
def test_persons::association_instantiation(instance):
    assert isinstance(instance, Persons::Association)

@given(instance=Persons::TownHall_strategy)
@settings(max_examples=50)
def test_persons::townhall_instantiation(instance):
    assert isinstance(instance, Persons::TownHall)

@given(instance=Persons::Person_strategy)
@settings(max_examples=50)
def test_persons::person_instantiation(instance):
    assert isinstance(instance, Persons::Person)

@given(instance=Persons::Person_strategy)
def test_persons::person_fullName_type(instance):
    assert isinstance(instance.fullName, str)


@given(instance=Persons::Person_strategy)
def test_persons::person_fullName_setter(instance):
    original = instance.fullName
    instance.fullName = original
    assert instance.fullName == original

@given(instance=Persons::Community_strategy)
@settings(max_examples=50)
def test_persons::community_instantiation(instance):
    assert isinstance(instance, Persons::Community)
