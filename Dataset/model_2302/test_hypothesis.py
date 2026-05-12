import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Person,
    PersonList_Female,
    PersonList_Male,
    Place,
    PersonList_WorkPlace,
    PersonList_LivingPlace,
    PersonList_WorkingPosition,
    PersonList_Place,
    PersonList_Person,
    PersonList_List,
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



def test_personlist_female_is_not_abstract():
    assert not inspect.isabstract(PersonList_Female)


def test_personlist_female_constructor_exists():
    assert callable(PersonList_Female.__init__)


def test_personlist_female_constructor_args():
    sig = inspect.signature(PersonList_Female.__init__)
    params = list(sig.parameters.keys())



def test_personlist_male_is_not_abstract():
    assert not inspect.isabstract(PersonList_Male)


def test_personlist_male_constructor_exists():
    assert callable(PersonList_Male.__init__)


def test_personlist_male_constructor_args():
    sig = inspect.signature(PersonList_Male.__init__)
    params = list(sig.parameters.keys())



def test_place_is_not_abstract():
    assert not inspect.isabstract(Place)


def test_place_constructor_exists():
    assert callable(Place.__init__)


def test_place_constructor_args():
    sig = inspect.signature(Place.__init__)
    params = list(sig.parameters.keys())



def test_personlist_workplace_is_not_abstract():
    assert not inspect.isabstract(PersonList_WorkPlace)


def test_personlist_workplace_constructor_exists():
    assert callable(PersonList_WorkPlace.__init__)


def test_personlist_workplace_constructor_args():
    sig = inspect.signature(PersonList_WorkPlace.__init__)
    params = list(sig.parameters.keys())



def test_personlist_livingplace_is_not_abstract():
    assert not inspect.isabstract(PersonList_LivingPlace)


def test_personlist_livingplace_constructor_exists():
    assert callable(PersonList_LivingPlace.__init__)


def test_personlist_livingplace_constructor_args():
    sig = inspect.signature(PersonList_LivingPlace.__init__)
    params = list(sig.parameters.keys())



def test_personlist_workingposition_is_not_abstract():
    assert not inspect.isabstract(PersonList_WorkingPosition)


def test_personlist_workingposition_constructor_exists():
    assert callable(PersonList_WorkingPosition.__init__)


def test_personlist_workingposition_constructor_args():
    sig = inspect.signature(PersonList_WorkingPosition.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_personlist_workingposition_has_description():
    assert hasattr(PersonList_WorkingPosition, "description")
    descriptor = None
    for klass in PersonList_WorkingPosition.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_personlist_place_is_not_abstract():
    assert not inspect.isabstract(PersonList_Place)


def test_personlist_place_constructor_exists():
    assert callable(PersonList_Place.__init__)


def test_personlist_place_constructor_args():
    sig = inspect.signature(PersonList_Place.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"

def test_personlist_place_has_address():
    assert hasattr(PersonList_Place, "address")
    descriptor = None
    for klass in PersonList_Place.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)



def test_personlist_person_is_not_abstract():
    assert not inspect.isabstract(PersonList_Person)


def test_personlist_person_constructor_exists():
    assert callable(PersonList_Person.__init__)


def test_personlist_person_constructor_args():
    sig = inspect.signature(PersonList_Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_personlist_person_has_name():
    assert hasattr(PersonList_Person, "name")
    descriptor = None
    for klass in PersonList_Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_personlist_list_is_not_abstract():
    assert not inspect.isabstract(PersonList_List)


def test_personlist_list_constructor_exists():
    assert callable(PersonList_List.__init__)


def test_personlist_list_constructor_args():
    sig = inspect.signature(PersonList_List.__init__)
    params = list(sig.parameters.keys())

def test_gender_exists():
    # Check that the Enumeration exists
    assert Gender is not None

def test_gender_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Gender]
    expected_literals = [
        "Female",
        "Male",
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
PersonList_Female_strategy = st.builds(
    PersonList_Female,
)
PersonList_Male_strategy = st.builds(
    PersonList_Male,
)
Place_strategy = st.builds(
    Place,
)
PersonList_WorkPlace_strategy = st.builds(
    PersonList_WorkPlace,
)
PersonList_LivingPlace_strategy = st.builds(
    PersonList_LivingPlace,
)
PersonList_WorkingPosition_strategy = st.builds(
    PersonList_WorkingPosition,
    description=
        safe_text
)
PersonList_Place_strategy = st.builds(
    PersonList_Place,
    address=
        safe_text
)
PersonList_Person_strategy = st.builds(
    PersonList_Person,
    name=
        safe_text
)
PersonList_List_strategy = st.builds(
    PersonList_List,
)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=PersonList_Female_strategy)
@settings(max_examples=50)
def test_personlist_female_instantiation(instance):
    assert isinstance(instance, PersonList_Female)

@given(instance=PersonList_Male_strategy)
@settings(max_examples=50)
def test_personlist_male_instantiation(instance):
    assert isinstance(instance, PersonList_Male)

@given(instance=Place_strategy)
@settings(max_examples=50)
def test_place_instantiation(instance):
    assert isinstance(instance, Place)

@given(instance=PersonList_WorkPlace_strategy)
@settings(max_examples=50)
def test_personlist_workplace_instantiation(instance):
    assert isinstance(instance, PersonList_WorkPlace)

@given(instance=PersonList_LivingPlace_strategy)
@settings(max_examples=50)
def test_personlist_livingplace_instantiation(instance):
    assert isinstance(instance, PersonList_LivingPlace)

@given(instance=PersonList_WorkingPosition_strategy)
@settings(max_examples=50)
def test_personlist_workingposition_instantiation(instance):
    assert isinstance(instance, PersonList_WorkingPosition)



@given(instance=PersonList_WorkingPosition_strategy)
def test_personlist_workingposition_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=PersonList_Place_strategy)
@settings(max_examples=50)
def test_personlist_place_instantiation(instance):
    assert isinstance(instance, PersonList_Place)



@given(instance=PersonList_Place_strategy)
def test_personlist_place_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=PersonList_Person_strategy)
@settings(max_examples=50)
def test_personlist_person_instantiation(instance):
    assert isinstance(instance, PersonList_Person)



@given(instance=PersonList_Person_strategy)
def test_personlist_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PersonList_List_strategy)
@settings(max_examples=50)
def test_personlist_list_instantiation(instance):
    assert isinstance(instance, PersonList_List)
