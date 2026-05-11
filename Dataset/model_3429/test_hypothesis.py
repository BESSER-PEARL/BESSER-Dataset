import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    people::Person,
    people::Model,
    people::Pet,
    PetKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_people::person_is_not_abstract():
    assert not inspect.isabstract(people::Person)


def test_people::person_constructor_exists():
    assert callable(people::Person.__init__)


def test_people::person_constructor_args():
    sig = inspect.signature(people::Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "alive" in params, "Missing parameter 'alive'"
    assert "age" in params, "Missing parameter 'age'"
    assert "nicknames" in params, "Missing parameter 'nicknames'"
    assert "luckyNumbers" in params, "Missing parameter 'luckyNumbers'"
    assert "lotteryChances" in params, "Missing parameter 'lotteryChances'"

def test_people::person_has_name():
    assert hasattr(people::Person, "name")
    descriptor = None
    for klass in people::Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_people::person_has_alive():
    assert hasattr(people::Person, "alive")
    descriptor = None
    for klass in people::Person.__mro__:
        if "alive" in klass.__dict__:
            descriptor = klass.__dict__["alive"]
            break
    assert isinstance(descriptor, property)

def test_people::person_has_age():
    assert hasattr(people::Person, "age")
    descriptor = None
    for klass in people::Person.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_people::person_has_nicknames():
    assert hasattr(people::Person, "nicknames")
    descriptor = None
    for klass in people::Person.__mro__:
        if "nicknames" in klass.__dict__:
            descriptor = klass.__dict__["nicknames"]
            break
    assert isinstance(descriptor, property)

def test_people::person_has_luckyNumbers():
    assert hasattr(people::Person, "luckyNumbers")
    descriptor = None
    for klass in people::Person.__mro__:
        if "luckyNumbers" in klass.__dict__:
            descriptor = klass.__dict__["luckyNumbers"]
            break
    assert isinstance(descriptor, property)

def test_people::person_has_lotteryChances():
    assert hasattr(people::Person, "lotteryChances")
    descriptor = None
    for klass in people::Person.__mro__:
        if "lotteryChances" in klass.__dict__:
            descriptor = klass.__dict__["lotteryChances"]
            break
    assert isinstance(descriptor, property)



def test_people::model_is_not_abstract():
    assert not inspect.isabstract(people::Model)


def test_people::model_constructor_exists():
    assert callable(people::Model.__init__)


def test_people::model_constructor_args():
    sig = inspect.signature(people::Model.__init__)
    params = list(sig.parameters.keys())



def test_people::pet_is_not_abstract():
    assert not inspect.isabstract(people::Pet)


def test_people::pet_constructor_exists():
    assert callable(people::Pet.__init__)


def test_people::pet_constructor_args():
    sig = inspect.signature(people::Pet.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "name" in params, "Missing parameter 'name'"

def test_people::pet_has_kind():
    assert hasattr(people::Pet, "kind")
    descriptor = None
    for klass in people::Pet.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_people::pet_has_name():
    assert hasattr(people::Pet, "name")
    descriptor = None
    for klass in people::Pet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_petkind_exists():
    # Check that the Enumeration exists
    assert PetKind is not None

def test_petkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PetKind]
    expected_literals = [
        "DANGEROUS",
        "INDEPENDENT",
        "FRIENDLY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PetKind"


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
people::Person_strategy = st.builds(
    people::Person,
    name=
        safe_text,
    alive=
        st.booleans(),
    age=
        st.integers(),
    nicknames=
        safe_text,
    luckyNumbers=
        st.integers(),
    lotteryChances=
        safe_text
)
people::Model_strategy = st.builds(
    people::Model,
)
people::Pet_strategy = st.builds(
    people::Pet,
    kind=
        safe_text,
    name=
        safe_text
)

@given(instance=people::Person_strategy)
@settings(max_examples=50)
def test_people::person_instantiation(instance):
    assert isinstance(instance, people::Person)

@given(instance=people::Person_strategy)
def test_people::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=people::Person_strategy)
def test_people::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=people::Person_strategy)
def test_people::person_alive_type(instance):
    assert isinstance(instance.alive, bool)


@given(instance=people::Person_strategy)
def test_people::person_alive_setter(instance):
    original = instance.alive
    instance.alive = original
    assert instance.alive == original

@given(instance=people::Person_strategy)
def test_people::person_age_type(instance):
    assert isinstance(instance.age, int)


@given(instance=people::Person_strategy)
def test_people::person_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=people::Person_strategy)
def test_people::person_nicknames_type(instance):
    assert isinstance(instance.nicknames, str)


@given(instance=people::Person_strategy)
def test_people::person_nicknames_setter(instance):
    original = instance.nicknames
    instance.nicknames = original
    assert instance.nicknames == original

@given(instance=people::Person_strategy)
def test_people::person_luckyNumbers_type(instance):
    assert isinstance(instance.luckyNumbers, int)


@given(instance=people::Person_strategy)
def test_people::person_luckyNumbers_setter(instance):
    original = instance.luckyNumbers
    instance.luckyNumbers = original
    assert instance.luckyNumbers == original

@given(instance=people::Person_strategy)
def test_people::person_lotteryChances_type(instance):
    assert isinstance(instance.lotteryChances, str)


@given(instance=people::Person_strategy)
def test_people::person_lotteryChances_setter(instance):
    original = instance.lotteryChances
    instance.lotteryChances = original
    assert instance.lotteryChances == original

@given(instance=people::Model_strategy)
@settings(max_examples=50)
def test_people::model_instantiation(instance):
    assert isinstance(instance, people::Model)

@given(instance=people::Pet_strategy)
@settings(max_examples=50)
def test_people::pet_instantiation(instance):
    assert isinstance(instance, people::Pet)

@given(instance=people::Pet_strategy)
def test_people::pet_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=people::Pet_strategy)
def test_people::pet_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=people::Pet_strategy)
def test_people::pet_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=people::Pet_strategy)
def test_people::pet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
