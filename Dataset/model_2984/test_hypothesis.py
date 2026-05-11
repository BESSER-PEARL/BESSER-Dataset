import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    mealymodel::State,
    mealymodel::MealyMachine,
    mealymodel::Transition,
    mealymodel::Alphabet,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mealymodel::state_is_not_abstract():
    assert not inspect.isabstract(mealymodel::State)


def test_mealymodel::state_constructor_exists():
    assert callable(mealymodel::State.__init__)


def test_mealymodel::state_constructor_args():
    sig = inspect.signature(mealymodel::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mealymodel::state_has_name():
    assert hasattr(mealymodel::State, "name")
    descriptor = None
    for klass in mealymodel::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mealymodel::mealymachine_is_not_abstract():
    assert not inspect.isabstract(mealymodel::MealyMachine)


def test_mealymodel::mealymachine_constructor_exists():
    assert callable(mealymodel::MealyMachine.__init__)


def test_mealymodel::mealymachine_constructor_args():
    sig = inspect.signature(mealymodel::MealyMachine.__init__)
    params = list(sig.parameters.keys())



def test_mealymodel::transition_is_not_abstract():
    assert not inspect.isabstract(mealymodel::Transition)


def test_mealymodel::transition_constructor_exists():
    assert callable(mealymodel::Transition.__init__)


def test_mealymodel::transition_constructor_args():
    sig = inspect.signature(mealymodel::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "input" in params, "Missing parameter 'input'"
    assert "output" in params, "Missing parameter 'output'"

def test_mealymodel::transition_has_input():
    assert hasattr(mealymodel::Transition, "input")
    descriptor = None
    for klass in mealymodel::Transition.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)

def test_mealymodel::transition_has_output():
    assert hasattr(mealymodel::Transition, "output")
    descriptor = None
    for klass in mealymodel::Transition.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
            break
    assert isinstance(descriptor, property)



def test_mealymodel::alphabet_is_not_abstract():
    assert not inspect.isabstract(mealymodel::Alphabet)


def test_mealymodel::alphabet_constructor_exists():
    assert callable(mealymodel::Alphabet.__init__)


def test_mealymodel::alphabet_constructor_args():
    sig = inspect.signature(mealymodel::Alphabet.__init__)
    params = list(sig.parameters.keys())
    assert "characters" in params, "Missing parameter 'characters'"

def test_mealymodel::alphabet_has_characters():
    assert hasattr(mealymodel::Alphabet, "characters")
    descriptor = None
    for klass in mealymodel::Alphabet.__mro__:
        if "characters" in klass.__dict__:
            descriptor = klass.__dict__["characters"]
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
mealymodel::State_strategy = st.builds(
    mealymodel::State,
    name=
        safe_text
)
mealymodel::MealyMachine_strategy = st.builds(
    mealymodel::MealyMachine,
)
mealymodel::Transition_strategy = st.builds(
    mealymodel::Transition,
    input=
        safe_text,
    output=
        safe_text
)
mealymodel::Alphabet_strategy = st.builds(
    mealymodel::Alphabet,
    characters=
        safe_text
)

@given(instance=mealymodel::State_strategy)
@settings(max_examples=50)
def test_mealymodel::state_instantiation(instance):
    assert isinstance(instance, mealymodel::State)

@given(instance=mealymodel::State_strategy)
def test_mealymodel::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mealymodel::State_strategy)
def test_mealymodel::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mealymodel::MealyMachine_strategy)
@settings(max_examples=50)
def test_mealymodel::mealymachine_instantiation(instance):
    assert isinstance(instance, mealymodel::MealyMachine)

@given(instance=mealymodel::Transition_strategy)
@settings(max_examples=50)
def test_mealymodel::transition_instantiation(instance):
    assert isinstance(instance, mealymodel::Transition)

@given(instance=mealymodel::Transition_strategy)
def test_mealymodel::transition_input_type(instance):
    assert isinstance(instance.input, str)


@given(instance=mealymodel::Transition_strategy)
def test_mealymodel::transition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original

@given(instance=mealymodel::Transition_strategy)
def test_mealymodel::transition_output_type(instance):
    assert isinstance(instance.output, str)


@given(instance=mealymodel::Transition_strategy)
def test_mealymodel::transition_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original

@given(instance=mealymodel::Alphabet_strategy)
@settings(max_examples=50)
def test_mealymodel::alphabet_instantiation(instance):
    assert isinstance(instance, mealymodel::Alphabet)

@given(instance=mealymodel::Alphabet_strategy)
def test_mealymodel::alphabet_characters_type(instance):
    assert isinstance(instance.characters, str)


@given(instance=mealymodel::Alphabet_strategy)
def test_mealymodel::alphabet_characters_setter(instance):
    original = instance.characters
    instance.characters = original
    assert instance.characters == original
