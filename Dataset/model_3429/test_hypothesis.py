import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    people_Person,
    people_Model,
    people_Pet,
    PetKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_people_person_is_not_abstract():
    assert not inspect.isabstract(people_Person)


def test_people_person_constructor_exists():
    assert callable(people_Person.__init__)


def test_people_person_constructor_args():
    sig = inspect.signature(people_Person.__init__)
    params = list(sig.parameters.keys())
    assert "age" in params, "Missing parameter 'age'"
    assert "luckyNumbers" in params, "Missing parameter 'luckyNumbers'"
    assert "alive" in params, "Missing parameter 'alive'"
    assert "lotteryChances" in params, "Missing parameter 'lotteryChances'"
    assert "name" in params, "Missing parameter 'name'"
    assert "nicknames" in params, "Missing parameter 'nicknames'"

def test_people_person_has_age():
    assert hasattr(people_Person, "age")
    descriptor = None
    for klass in people_Person.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_people_person_has_luckyNumbers():
    assert hasattr(people_Person, "luckyNumbers")
    descriptor = None
    for klass in people_Person.__mro__:
        if "luckyNumbers" in klass.__dict__:
            descriptor = klass.__dict__["luckyNumbers"]
            break
    assert isinstance(descriptor, property)

def test_people_person_has_alive():
    assert hasattr(people_Person, "alive")
    descriptor = None
    for klass in people_Person.__mro__:
        if "alive" in klass.__dict__:
            descriptor = klass.__dict__["alive"]
            break
    assert isinstance(descriptor, property)

def test_people_person_has_lotteryChances():
    assert hasattr(people_Person, "lotteryChances")
    descriptor = None
    for klass in people_Person.__mro__:
        if "lotteryChances" in klass.__dict__:
            descriptor = klass.__dict__["lotteryChances"]
            break
    assert isinstance(descriptor, property)

def test_people_person_has_name():
    assert hasattr(people_Person, "name")
    descriptor = None
    for klass in people_Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_people_person_has_nicknames():
    assert hasattr(people_Person, "nicknames")
    descriptor = None
    for klass in people_Person.__mro__:
        if "nicknames" in klass.__dict__:
            descriptor = klass.__dict__["nicknames"]
            break
    assert isinstance(descriptor, property)



def test_people_model_is_not_abstract():
    assert not inspect.isabstract(people_Model)


def test_people_model_constructor_exists():
    assert callable(people_Model.__init__)


def test_people_model_constructor_args():
    sig = inspect.signature(people_Model.__init__)
    params = list(sig.parameters.keys())



def test_people_pet_is_not_abstract():
    assert not inspect.isabstract(people_Pet)


def test_people_pet_constructor_exists():
    assert callable(people_Pet.__init__)


def test_people_pet_constructor_args():
    sig = inspect.signature(people_Pet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_people_pet_has_name():
    assert hasattr(people_Pet, "name")
    descriptor = None
    for klass in people_Pet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_people_pet_has_kind():
    assert hasattr(people_Pet, "kind")
    descriptor = None
    for klass in people_Pet.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_petkind_exists():
    # Check that the Enumeration exists
    assert PetKind is not None

def test_petkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PetKind]
    expected_literals = [
        "FRIENDLY",
        "INDEPENDENT",
        "DANGEROUS",
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
people_Person_strategy = st.builds(
    people_Person,
    age=
        st.integers(),
    luckyNumbers=
        st.integers(),
    alive=
        st.booleans(),
    lotteryChances=
        safe_text,
    name=
        safe_text,
    nicknames=
        safe_text
)
people_Model_strategy = st.builds(
    people_Model,
)
people_Pet_strategy = st.builds(
    people_Pet,
    name=
        safe_text,
    kind=
        safe_text
)

@given(instance=people_Person_strategy)
@settings(max_examples=50)
def test_people_person_instantiation(instance):
    assert isinstance(instance, people_Person)



@given(instance=people_Person_strategy)
def test_people_person_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original



@given(instance=people_Person_strategy)
def test_people_person_luckyNumbers_setter(instance):
    original = instance.luckyNumbers
    instance.luckyNumbers = original
    assert instance.luckyNumbers == original



@given(instance=people_Person_strategy)
def test_people_person_alive_setter(instance):
    original = instance.alive
    instance.alive = original
    assert instance.alive == original



@given(instance=people_Person_strategy)
def test_people_person_lotteryChances_setter(instance):
    original = instance.lotteryChances
    instance.lotteryChances = original
    assert instance.lotteryChances == original



@given(instance=people_Person_strategy)
def test_people_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=people_Person_strategy)
def test_people_person_nicknames_setter(instance):
    original = instance.nicknames
    instance.nicknames = original
    assert instance.nicknames == original

@given(instance=people_Model_strategy)
@settings(max_examples=50)
def test_people_model_instantiation(instance):
    assert isinstance(instance, people_Model)

@given(instance=people_Pet_strategy)
@settings(max_examples=50)
def test_people_pet_instantiation(instance):
    assert isinstance(instance, people_Pet)



@given(instance=people_Pet_strategy)
def test_people_pet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=people_Pet_strategy)
def test_people_pet_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original
