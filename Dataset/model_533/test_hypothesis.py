import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Dog,
    Example::HuntingDog,
    Example::Family,
    Example::RaceDog,
    Pet,
    Example::Cat,
    Example::Dog,
    Member,
    Example::Parent,
    Example::Member,
    Example::Pet,
    Example::Daughter,
    Example::Son,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dog_is_not_abstract():
    assert not inspect.isabstract(Dog)


def test_dog_constructor_exists():
    assert callable(Dog.__init__)


def test_dog_constructor_args():
    sig = inspect.signature(Dog.__init__)
    params = list(sig.parameters.keys())



def test_example::huntingdog_is_not_abstract():
    assert not inspect.isabstract(Example::HuntingDog)


def test_example::huntingdog_constructor_exists():
    assert callable(Example::HuntingDog.__init__)


def test_example::huntingdog_constructor_args():
    sig = inspect.signature(Example::HuntingDog.__init__)
    params = list(sig.parameters.keys())



def test_example::family_is_not_abstract():
    assert not inspect.isabstract(Example::Family)


def test_example::family_constructor_exists():
    assert callable(Example::Family.__init__)


def test_example::family_constructor_args():
    sig = inspect.signature(Example::Family.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"

def test_example::family_has_address():
    assert hasattr(Example::Family, "address")
    descriptor = None
    for klass in Example::Family.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)



def test_example::racedog_is_not_abstract():
    assert not inspect.isabstract(Example::RaceDog)


def test_example::racedog_constructor_exists():
    assert callable(Example::RaceDog.__init__)


def test_example::racedog_constructor_args():
    sig = inspect.signature(Example::RaceDog.__init__)
    params = list(sig.parameters.keys())



def test_pet_is_not_abstract():
    assert not inspect.isabstract(Pet)


def test_pet_constructor_exists():
    assert callable(Pet.__init__)


def test_pet_constructor_args():
    sig = inspect.signature(Pet.__init__)
    params = list(sig.parameters.keys())



def test_example::cat_is_not_abstract():
    assert not inspect.isabstract(Example::Cat)


def test_example::cat_constructor_exists():
    assert callable(Example::Cat.__init__)


def test_example::cat_constructor_args():
    sig = inspect.signature(Example::Cat.__init__)
    params = list(sig.parameters.keys())



def test_example::dog_is_not_abstract():
    assert not inspect.isabstract(Example::Dog)


def test_example::dog_constructor_exists():
    assert callable(Example::Dog.__init__)


def test_example::dog_constructor_args():
    sig = inspect.signature(Example::Dog.__init__)
    params = list(sig.parameters.keys())



def test_member_is_not_abstract():
    assert not inspect.isabstract(Member)


def test_member_constructor_exists():
    assert callable(Member.__init__)


def test_member_constructor_args():
    sig = inspect.signature(Member.__init__)
    params = list(sig.parameters.keys())



def test_example::parent_is_not_abstract():
    assert not inspect.isabstract(Example::Parent)


def test_example::parent_constructor_exists():
    assert callable(Example::Parent.__init__)


def test_example::parent_constructor_args():
    sig = inspect.signature(Example::Parent.__init__)
    params = list(sig.parameters.keys())



def test_example::member_is_not_abstract():
    assert not inspect.isabstract(Example::Member)


def test_example::member_constructor_exists():
    assert callable(Example::Member.__init__)


def test_example::member_constructor_args():
    sig = inspect.signature(Example::Member.__init__)
    params = list(sig.parameters.keys())
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "firstName" in params, "Missing parameter 'firstName'"

def test_example::member_has_lastName():
    assert hasattr(Example::Member, "lastName")
    descriptor = None
    for klass in Example::Member.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_example::member_has_firstName():
    assert hasattr(Example::Member, "firstName")
    descriptor = None
    for klass in Example::Member.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)



def test_example::pet_is_not_abstract():
    assert not inspect.isabstract(Example::Pet)


def test_example::pet_constructor_exists():
    assert callable(Example::Pet.__init__)


def test_example::pet_constructor_args():
    sig = inspect.signature(Example::Pet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "breed" in params, "Missing parameter 'breed'"

def test_example::pet_has_name():
    assert hasattr(Example::Pet, "name")
    descriptor = None
    for klass in Example::Pet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_example::pet_has_breed():
    assert hasattr(Example::Pet, "breed")
    descriptor = None
    for klass in Example::Pet.__mro__:
        if "breed" in klass.__dict__:
            descriptor = klass.__dict__["breed"]
            break
    assert isinstance(descriptor, property)



def test_example::daughter_is_not_abstract():
    assert not inspect.isabstract(Example::Daughter)


def test_example::daughter_constructor_exists():
    assert callable(Example::Daughter.__init__)


def test_example::daughter_constructor_args():
    sig = inspect.signature(Example::Daughter.__init__)
    params = list(sig.parameters.keys())



def test_example::son_is_not_abstract():
    assert not inspect.isabstract(Example::Son)


def test_example::son_constructor_exists():
    assert callable(Example::Son.__init__)


def test_example::son_constructor_args():
    sig = inspect.signature(Example::Son.__init__)
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
Dog_strategy = st.builds(
    Dog,
)
Example::HuntingDog_strategy = st.builds(
    Example::HuntingDog,
)
Example::Family_strategy = st.builds(
    Example::Family,
    address=
        safe_text
)
Example::RaceDog_strategy = st.builds(
    Example::RaceDog,
)
Pet_strategy = st.builds(
    Pet,
)
Example::Cat_strategy = st.builds(
    Example::Cat,
)
Example::Dog_strategy = st.builds(
    Example::Dog,
)
Member_strategy = st.builds(
    Member,
)
Example::Parent_strategy = st.builds(
    Example::Parent,
)
Example::Member_strategy = st.builds(
    Example::Member,
    lastName=
        safe_text,
    firstName=
        safe_text
)
Example::Pet_strategy = st.builds(
    Example::Pet,
    name=
        safe_text,
    breed=
        safe_text
)
Example::Daughter_strategy = st.builds(
    Example::Daughter,
)
Example::Son_strategy = st.builds(
    Example::Son,
)

@given(instance=Dog_strategy)
@settings(max_examples=50)
def test_dog_instantiation(instance):
    assert isinstance(instance, Dog)

@given(instance=Example::HuntingDog_strategy)
@settings(max_examples=50)
def test_example::huntingdog_instantiation(instance):
    assert isinstance(instance, Example::HuntingDog)

@given(instance=Example::Family_strategy)
@settings(max_examples=50)
def test_example::family_instantiation(instance):
    assert isinstance(instance, Example::Family)

@given(instance=Example::Family_strategy)
def test_example::family_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=Example::Family_strategy)
def test_example::family_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=Example::RaceDog_strategy)
@settings(max_examples=50)
def test_example::racedog_instantiation(instance):
    assert isinstance(instance, Example::RaceDog)

@given(instance=Pet_strategy)
@settings(max_examples=50)
def test_pet_instantiation(instance):
    assert isinstance(instance, Pet)

@given(instance=Example::Cat_strategy)
@settings(max_examples=50)
def test_example::cat_instantiation(instance):
    assert isinstance(instance, Example::Cat)

@given(instance=Example::Dog_strategy)
@settings(max_examples=50)
def test_example::dog_instantiation(instance):
    assert isinstance(instance, Example::Dog)

@given(instance=Member_strategy)
@settings(max_examples=50)
def test_member_instantiation(instance):
    assert isinstance(instance, Member)

@given(instance=Example::Parent_strategy)
@settings(max_examples=50)
def test_example::parent_instantiation(instance):
    assert isinstance(instance, Example::Parent)

@given(instance=Example::Member_strategy)
@settings(max_examples=50)
def test_example::member_instantiation(instance):
    assert isinstance(instance, Example::Member)

@given(instance=Example::Member_strategy)
def test_example::member_lastName_type(instance):
    assert isinstance(instance.lastName, str)


@given(instance=Example::Member_strategy)
def test_example::member_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=Example::Member_strategy)
def test_example::member_firstName_type(instance):
    assert isinstance(instance.firstName, str)


@given(instance=Example::Member_strategy)
def test_example::member_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=Example::Pet_strategy)
@settings(max_examples=50)
def test_example::pet_instantiation(instance):
    assert isinstance(instance, Example::Pet)

@given(instance=Example::Pet_strategy)
def test_example::pet_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Example::Pet_strategy)
def test_example::pet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Example::Pet_strategy)
def test_example::pet_breed_type(instance):
    assert isinstance(instance.breed, str)


@given(instance=Example::Pet_strategy)
def test_example::pet_breed_setter(instance):
    original = instance.breed
    instance.breed = original
    assert instance.breed == original

@given(instance=Example::Daughter_strategy)
@settings(max_examples=50)
def test_example::daughter_instantiation(instance):
    assert isinstance(instance, Example::Daughter)

@given(instance=Example::Son_strategy)
@settings(max_examples=50)
def test_example::son_instantiation(instance):
    assert isinstance(instance, Example::Son)
