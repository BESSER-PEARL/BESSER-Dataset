import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Person,
    PersonList::Female,
    PersonList::Male,
    Place,
    PersonList::WorkPlace,
    PersonList::LivingPlace,
    PersonList::WorkingPosition,
    PersonList::Place,
    PersonList::Person,
    PersonList::List,
    Gender,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_personlist::female_is_not_abstract():
    assert not inspect.isabstract(PersonList::Female)


def test_personlist::female_constructor_exists():
    assert callable(PersonList::Female.__init__)


def test_personlist::female_constructor_args():
    sig = inspect.signature(PersonList::Female.__init__)
    params = list(sig.parameters.keys())



def test_personlist::male_is_not_abstract():
    assert not inspect.isabstract(PersonList::Male)


def test_personlist::male_constructor_exists():
    assert callable(PersonList::Male.__init__)


def test_personlist::male_constructor_args():
    sig = inspect.signature(PersonList::Male.__init__)
    params = list(sig.parameters.keys())



def test_place_is_not_abstract():
    assert not inspect.isabstract(Place)


def test_place_constructor_exists():
    assert callable(Place.__init__)


def test_place_constructor_args():
    sig = inspect.signature(Place.__init__)
    params = list(sig.parameters.keys())



def test_personlist::workplace_is_not_abstract():
    assert not inspect.isabstract(PersonList::WorkPlace)


def test_personlist::workplace_constructor_exists():
    assert callable(PersonList::WorkPlace.__init__)


def test_personlist::workplace_constructor_args():
    sig = inspect.signature(PersonList::WorkPlace.__init__)
    params = list(sig.parameters.keys())



def test_personlist::livingplace_is_not_abstract():
    assert not inspect.isabstract(PersonList::LivingPlace)


def test_personlist::livingplace_constructor_exists():
    assert callable(PersonList::LivingPlace.__init__)


def test_personlist::livingplace_constructor_args():
    sig = inspect.signature(PersonList::LivingPlace.__init__)
    params = list(sig.parameters.keys())



def test_personlist::workingposition_is_not_abstract():
    assert not inspect.isabstract(PersonList::WorkingPosition)


def test_personlist::workingposition_constructor_exists():
    assert callable(PersonList::WorkingPosition.__init__)


def test_personlist::workingposition_constructor_args():
    sig = inspect.signature(PersonList::WorkingPosition.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_personlist::workingposition_has_description():
    assert hasattr(PersonList::WorkingPosition, "description")
    descriptor = None
    for klass in PersonList::WorkingPosition.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_personlist::place_is_not_abstract():
    assert not inspect.isabstract(PersonList::Place)


def test_personlist::place_constructor_exists():
    assert callable(PersonList::Place.__init__)


def test_personlist::place_constructor_args():
    sig = inspect.signature(PersonList::Place.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"

def test_personlist::place_has_address():
    assert hasattr(PersonList::Place, "address")
    descriptor = None
    for klass in PersonList::Place.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)



def test_personlist::person_is_not_abstract():
    assert not inspect.isabstract(PersonList::Person)


def test_personlist::person_constructor_exists():
    assert callable(PersonList::Person.__init__)


def test_personlist::person_constructor_args():
    sig = inspect.signature(PersonList::Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_personlist::person_has_name():
    assert hasattr(PersonList::Person, "name")
    descriptor = None
    for klass in PersonList::Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_personlist::list_is_not_abstract():
    assert not inspect.isabstract(PersonList::List)


def test_personlist::list_constructor_exists():
    assert callable(PersonList::List.__init__)


def test_personlist::list_constructor_args():
    sig = inspect.signature(PersonList::List.__init__)
    params = list(sig.parameters.keys())

def test_gender_exists():
    # Check that the Enumeration exists
    assert Gender is not None

def test_gender_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Gender]
    expected_literals = [
        "Male",
        "Female",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Gender"


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
Person_strategy = st.builds(
    Person,
)
PersonList::Female_strategy = st.builds(
    PersonList::Female,
)
PersonList::Male_strategy = st.builds(
    PersonList::Male,
)
Place_strategy = st.builds(
    Place,
)
PersonList::WorkPlace_strategy = st.builds(
    PersonList::WorkPlace,
)
PersonList::LivingPlace_strategy = st.builds(
    PersonList::LivingPlace,
)
PersonList::WorkingPosition_strategy = st.builds(
    PersonList::WorkingPosition,
    description=
        safe_text
)
PersonList::Place_strategy = st.builds(
    PersonList::Place,
    address=
        safe_text
)
PersonList::Person_strategy = st.builds(
    PersonList::Person,
    name=
        safe_text
)
PersonList::List_strategy = st.builds(
    PersonList::List,
)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=PersonList::Female_strategy)
@settings(max_examples=50)
def test_personlist::female_instantiation(instance):
    assert isinstance(instance, PersonList::Female)

@given(instance=PersonList::Male_strategy)
@settings(max_examples=50)
def test_personlist::male_instantiation(instance):
    assert isinstance(instance, PersonList::Male)

@given(instance=Place_strategy)
@settings(max_examples=50)
def test_place_instantiation(instance):
    assert isinstance(instance, Place)

@given(instance=PersonList::WorkPlace_strategy)
@settings(max_examples=50)
def test_personlist::workplace_instantiation(instance):
    assert isinstance(instance, PersonList::WorkPlace)

@given(instance=PersonList::LivingPlace_strategy)
@settings(max_examples=50)
def test_personlist::livingplace_instantiation(instance):
    assert isinstance(instance, PersonList::LivingPlace)

@given(instance=PersonList::WorkingPosition_strategy)
@settings(max_examples=50)
def test_personlist::workingposition_instantiation(instance):
    assert isinstance(instance, PersonList::WorkingPosition)

@given(instance=PersonList::WorkingPosition_strategy)
def test_personlist::workingposition_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=PersonList::WorkingPosition_strategy)
def test_personlist::workingposition_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=PersonList::Place_strategy)
@settings(max_examples=50)
def test_personlist::place_instantiation(instance):
    assert isinstance(instance, PersonList::Place)

@given(instance=PersonList::Place_strategy)
def test_personlist::place_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=PersonList::Place_strategy)
def test_personlist::place_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=PersonList::Person_strategy)
@settings(max_examples=50)
def test_personlist::person_instantiation(instance):
    assert isinstance(instance, PersonList::Person)

@given(instance=PersonList::Person_strategy)
def test_personlist::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=PersonList::Person_strategy)
def test_personlist::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PersonList::List_strategy)
@settings(max_examples=50)
def test_personlist::list_instantiation(instance):
    assert isinstance(instance, PersonList::List)
