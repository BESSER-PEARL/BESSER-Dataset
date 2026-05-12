import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Pet,
    Example_Dog,
    Member,
    Example_Member,
    Example_Pet,
    Example_Daughter,
    Example_Son,
    Example_Parent,
    Dog,
    Example_HuntingDog,
    Example_RaceDog,
    Example_Cat,
    Example_Family,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_pet_is_not_abstract():
    assert not inspect.isabstract(Pet)


def test_pet_constructor_exists():
    assert callable(Pet.__init__)


def test_pet_constructor_args():
    sig = inspect.signature(Pet.__init__)
    params = list(sig.parameters.keys())



def test_example_dog_is_not_abstract():
    assert not inspect.isabstract(Example_Dog)


def test_example_dog_constructor_exists():
    assert callable(Example_Dog.__init__)


def test_example_dog_constructor_args():
    sig = inspect.signature(Example_Dog.__init__)
    params = list(sig.parameters.keys())



def test_member_is_not_abstract():
    assert not inspect.isabstract(Member)


def test_member_constructor_exists():
    assert callable(Member.__init__)


def test_member_constructor_args():
    sig = inspect.signature(Member.__init__)
    params = list(sig.parameters.keys())



def test_example_member_is_not_abstract():
    assert not inspect.isabstract(Example_Member)


def test_example_member_constructor_exists():
    assert callable(Example_Member.__init__)


def test_example_member_constructor_args():
    sig = inspect.signature(Example_Member.__init__)
    params = list(sig.parameters.keys())
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "lastName" in params, "Missing parameter 'lastName'"

def test_example_member_has_firstName():
    assert hasattr(Example_Member, "firstName")
    descriptor = None
    for klass in Example_Member.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_example_member_has_lastName():
    assert hasattr(Example_Member, "lastName")
    descriptor = None
    for klass in Example_Member.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)



def test_example_pet_is_not_abstract():
    assert not inspect.isabstract(Example_Pet)


def test_example_pet_constructor_exists():
    assert callable(Example_Pet.__init__)


def test_example_pet_constructor_args():
    sig = inspect.signature(Example_Pet.__init__)
    params = list(sig.parameters.keys())
    assert "breed" in params, "Missing parameter 'breed'"
    assert "name" in params, "Missing parameter 'name'"

def test_example_pet_has_breed():
    assert hasattr(Example_Pet, "breed")
    descriptor = None
    for klass in Example_Pet.__mro__:
        if "breed" in klass.__dict__:
            descriptor = klass.__dict__["breed"]
            break
    assert isinstance(descriptor, property)

def test_example_pet_has_name():
    assert hasattr(Example_Pet, "name")
    descriptor = None
    for klass in Example_Pet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_example_daughter_is_not_abstract():
    assert not inspect.isabstract(Example_Daughter)


def test_example_daughter_constructor_exists():
    assert callable(Example_Daughter.__init__)


def test_example_daughter_constructor_args():
    sig = inspect.signature(Example_Daughter.__init__)
    params = list(sig.parameters.keys())



def test_example_son_is_not_abstract():
    assert not inspect.isabstract(Example_Son)


def test_example_son_constructor_exists():
    assert callable(Example_Son.__init__)


def test_example_son_constructor_args():
    sig = inspect.signature(Example_Son.__init__)
    params = list(sig.parameters.keys())



def test_example_parent_is_not_abstract():
    assert not inspect.isabstract(Example_Parent)


def test_example_parent_constructor_exists():
    assert callable(Example_Parent.__init__)


def test_example_parent_constructor_args():
    sig = inspect.signature(Example_Parent.__init__)
    params = list(sig.parameters.keys())



def test_dog_is_not_abstract():
    assert not inspect.isabstract(Dog)


def test_dog_constructor_exists():
    assert callable(Dog.__init__)


def test_dog_constructor_args():
    sig = inspect.signature(Dog.__init__)
    params = list(sig.parameters.keys())



def test_example_huntingdog_is_not_abstract():
    assert not inspect.isabstract(Example_HuntingDog)


def test_example_huntingdog_constructor_exists():
    assert callable(Example_HuntingDog.__init__)


def test_example_huntingdog_constructor_args():
    sig = inspect.signature(Example_HuntingDog.__init__)
    params = list(sig.parameters.keys())



def test_example_racedog_is_not_abstract():
    assert not inspect.isabstract(Example_RaceDog)


def test_example_racedog_constructor_exists():
    assert callable(Example_RaceDog.__init__)


def test_example_racedog_constructor_args():
    sig = inspect.signature(Example_RaceDog.__init__)
    params = list(sig.parameters.keys())



def test_example_cat_is_not_abstract():
    assert not inspect.isabstract(Example_Cat)


def test_example_cat_constructor_exists():
    assert callable(Example_Cat.__init__)


def test_example_cat_constructor_args():
    sig = inspect.signature(Example_Cat.__init__)
    params = list(sig.parameters.keys())



def test_example_family_is_not_abstract():
    assert not inspect.isabstract(Example_Family)


def test_example_family_constructor_exists():
    assert callable(Example_Family.__init__)


def test_example_family_constructor_args():
    sig = inspect.signature(Example_Family.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"

def test_example_family_has_address():
    assert hasattr(Example_Family, "address")
    descriptor = None
    for klass in Example_Family.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
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
Pet_strategy = st.builds(
    Pet,
)
Example_Dog_strategy = st.builds(
    Example_Dog,
)
Member_strategy = st.builds(
    Member,
)
Example_Member_strategy = st.builds(
    Example_Member,
    firstName=
        safe_text,
    lastName=
        safe_text
)
Example_Pet_strategy = st.builds(
    Example_Pet,
    breed=
        safe_text,
    name=
        safe_text
)
Example_Daughter_strategy = st.builds(
    Example_Daughter,
)
Example_Son_strategy = st.builds(
    Example_Son,
)
Example_Parent_strategy = st.builds(
    Example_Parent,
)
Dog_strategy = st.builds(
    Dog,
)
Example_HuntingDog_strategy = st.builds(
    Example_HuntingDog,
)
Example_RaceDog_strategy = st.builds(
    Example_RaceDog,
)
Example_Cat_strategy = st.builds(
    Example_Cat,
)
Example_Family_strategy = st.builds(
    Example_Family,
    address=
        safe_text
)

@given(instance=Pet_strategy)
@settings(max_examples=50)
def test_pet_instantiation(instance):
    assert isinstance(instance, Pet)

@given(instance=Example_Dog_strategy)
@settings(max_examples=50)
def test_example_dog_instantiation(instance):
    assert isinstance(instance, Example_Dog)

@given(instance=Member_strategy)
@settings(max_examples=50)
def test_member_instantiation(instance):
    assert isinstance(instance, Member)

@given(instance=Example_Member_strategy)
@settings(max_examples=50)
def test_example_member_instantiation(instance):
    assert isinstance(instance, Example_Member)



@given(instance=Example_Member_strategy)
def test_example_member_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original



@given(instance=Example_Member_strategy)
def test_example_member_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=Example_Pet_strategy)
@settings(max_examples=50)
def test_example_pet_instantiation(instance):
    assert isinstance(instance, Example_Pet)



@given(instance=Example_Pet_strategy)
def test_example_pet_breed_setter(instance):
    original = instance.breed
    instance.breed = original
    assert instance.breed == original



@given(instance=Example_Pet_strategy)
def test_example_pet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Example_Daughter_strategy)
@settings(max_examples=50)
def test_example_daughter_instantiation(instance):
    assert isinstance(instance, Example_Daughter)

@given(instance=Example_Son_strategy)
@settings(max_examples=50)
def test_example_son_instantiation(instance):
    assert isinstance(instance, Example_Son)

@given(instance=Example_Parent_strategy)
@settings(max_examples=50)
def test_example_parent_instantiation(instance):
    assert isinstance(instance, Example_Parent)

@given(instance=Dog_strategy)
@settings(max_examples=50)
def test_dog_instantiation(instance):
    assert isinstance(instance, Dog)

@given(instance=Example_HuntingDog_strategy)
@settings(max_examples=50)
def test_example_huntingdog_instantiation(instance):
    assert isinstance(instance, Example_HuntingDog)

@given(instance=Example_RaceDog_strategy)
@settings(max_examples=50)
def test_example_racedog_instantiation(instance):
    assert isinstance(instance, Example_RaceDog)

@given(instance=Example_Cat_strategy)
@settings(max_examples=50)
def test_example_cat_instantiation(instance):
    assert isinstance(instance, Example_Cat)

@given(instance=Example_Family_strategy)
@settings(max_examples=50)
def test_example_family_instantiation(instance):
    assert isinstance(instance, Example_Family)



@given(instance=Example_Family_strategy)
def test_example_family_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original
