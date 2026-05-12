import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Cashier,
    Waiter,
    Cook,
    Mammal,
    Animal,
    Reptile,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_cashier_is_not_abstract():
    assert not inspect.isabstract(Cashier)


def test_cashier_constructor_exists():
    assert callable(Cashier.__init__)


def test_cashier_constructor_args():
    sig = inspect.signature(Cashier.__init__)
    params = list(sig.parameters.keys())



def test_waiter_is_not_abstract():
    assert not inspect.isabstract(Waiter)


def test_waiter_constructor_exists():
    assert callable(Waiter.__init__)


def test_waiter_constructor_args():
    sig = inspect.signature(Waiter.__init__)
    params = list(sig.parameters.keys())



def test_cook_is_not_abstract():
    assert not inspect.isabstract(Cook)


def test_cook_constructor_exists():
    assert callable(Cook.__init__)


def test_cook_constructor_args():
    sig = inspect.signature(Cook.__init__)
    params = list(sig.parameters.keys())



def test_mammal_is_not_abstract():
    assert not inspect.isabstract(Mammal)


def test_mammal_constructor_exists():
    assert callable(Mammal.__init__)


def test_mammal_constructor_args():
    sig = inspect.signature(Mammal.__init__)
    params = list(sig.parameters.keys())



def test_animal_is_not_abstract():
    assert not inspect.isabstract(Animal)


def test_animal_constructor_exists():
    assert callable(Animal.__init__)


def test_animal_constructor_args():
    sig = inspect.signature(Animal.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_animal_has_name():
    assert hasattr(Animal, "name")
    descriptor = None
    for klass in Animal.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_reptile_is_not_abstract():
    assert not inspect.isabstract(Reptile)


def test_reptile_constructor_exists():
    assert callable(Reptile.__init__)


def test_reptile_constructor_args():
    sig = inspect.signature(Reptile.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"

def test_reptile_has_attribute():
    assert hasattr(Reptile, "attribute")
    descriptor = None
    for klass in Reptile.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
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
Cashier_strategy = st.builds(
    Cashier,
)
Waiter_strategy = st.builds(
    Waiter,
)
Cook_strategy = st.builds(
    Cook,
)
Mammal_strategy = st.builds(
    Mammal,
)
Animal_strategy = st.builds(
    Animal,
    name=
        safe_text
)
Reptile_strategy = st.builds(
    Reptile,
    attribute=
        safe_text
)

@given(instance=Cashier_strategy)
@settings(max_examples=50)
def test_cashier_instantiation(instance):
    assert isinstance(instance, Cashier)

@given(instance=Waiter_strategy)
@settings(max_examples=50)
def test_waiter_instantiation(instance):
    assert isinstance(instance, Waiter)

@given(instance=Cook_strategy)
@settings(max_examples=50)
def test_cook_instantiation(instance):
    assert isinstance(instance, Cook)

@given(instance=Mammal_strategy)
@settings(max_examples=50)
def test_mammal_instantiation(instance):
    assert isinstance(instance, Mammal)

@given(instance=Animal_strategy)
@settings(max_examples=50)
def test_animal_instantiation(instance):
    assert isinstance(instance, Animal)



@given(instance=Animal_strategy)
def test_animal_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Reptile_strategy)
@settings(max_examples=50)
def test_reptile_instantiation(instance):
    assert isinstance(instance, Reptile)



@given(instance=Reptile_strategy)
def test_reptile_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original
