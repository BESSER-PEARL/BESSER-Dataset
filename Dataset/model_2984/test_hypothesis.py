import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    mealymodel_State,
    mealymodel_MealyMachine,
    mealymodel_Transition,
    mealymodel_Alphabet,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mealymodel_state_is_not_abstract():
    assert not inspect.isabstract(mealymodel_State)


def test_mealymodel_state_constructor_exists():
    assert callable(mealymodel_State.__init__)


def test_mealymodel_state_constructor_args():
    sig = inspect.signature(mealymodel_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mealymodel_state_has_name():
    assert hasattr(mealymodel_State, "name")
    descriptor = None
    for klass in mealymodel_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mealymodel_mealymachine_is_not_abstract():
    assert not inspect.isabstract(mealymodel_MealyMachine)


def test_mealymodel_mealymachine_constructor_exists():
    assert callable(mealymodel_MealyMachine.__init__)


def test_mealymodel_mealymachine_constructor_args():
    sig = inspect.signature(mealymodel_MealyMachine.__init__)
    params = list(sig.parameters.keys())



def test_mealymodel_transition_is_not_abstract():
    assert not inspect.isabstract(mealymodel_Transition)


def test_mealymodel_transition_constructor_exists():
    assert callable(mealymodel_Transition.__init__)


def test_mealymodel_transition_constructor_args():
    sig = inspect.signature(mealymodel_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "input" in params, "Missing parameter 'input'"
    assert "output" in params, "Missing parameter 'output'"

def test_mealymodel_transition_has_input():
    assert hasattr(mealymodel_Transition, "input")
    descriptor = None
    for klass in mealymodel_Transition.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)

def test_mealymodel_transition_has_output():
    assert hasattr(mealymodel_Transition, "output")
    descriptor = None
    for klass in mealymodel_Transition.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
            break
    assert isinstance(descriptor, property)



def test_mealymodel_alphabet_is_not_abstract():
    assert not inspect.isabstract(mealymodel_Alphabet)


def test_mealymodel_alphabet_constructor_exists():
    assert callable(mealymodel_Alphabet.__init__)


def test_mealymodel_alphabet_constructor_args():
    sig = inspect.signature(mealymodel_Alphabet.__init__)
    params = list(sig.parameters.keys())
    assert "characters" in params, "Missing parameter 'characters'"

def test_mealymodel_alphabet_has_characters():
    assert hasattr(mealymodel_Alphabet, "characters")
    descriptor = None
    for klass in mealymodel_Alphabet.__mro__:
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
mealymodel_State_strategy = st.builds(
    mealymodel_State,
    name=
        safe_text
)
mealymodel_MealyMachine_strategy = st.builds(
    mealymodel_MealyMachine,
)
mealymodel_Transition_strategy = st.builds(
    mealymodel_Transition,
    input=
        safe_text,
    output=
        safe_text
)
mealymodel_Alphabet_strategy = st.builds(
    mealymodel_Alphabet,
    characters=
        safe_text
)

@given(instance=mealymodel_State_strategy)
@settings(max_examples=50)
def test_mealymodel_state_instantiation(instance):
    assert isinstance(instance, mealymodel_State)



@given(instance=mealymodel_State_strategy)
def test_mealymodel_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mealymodel_MealyMachine_strategy)
@settings(max_examples=50)
def test_mealymodel_mealymachine_instantiation(instance):
    assert isinstance(instance, mealymodel_MealyMachine)

@given(instance=mealymodel_Transition_strategy)
@settings(max_examples=50)
def test_mealymodel_transition_instantiation(instance):
    assert isinstance(instance, mealymodel_Transition)



@given(instance=mealymodel_Transition_strategy)
def test_mealymodel_transition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original



@given(instance=mealymodel_Transition_strategy)
def test_mealymodel_transition_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original

@given(instance=mealymodel_Alphabet_strategy)
@settings(max_examples=50)
def test_mealymodel_alphabet_instantiation(instance):
    assert isinstance(instance, mealymodel_Alphabet)



@given(instance=mealymodel_Alphabet_strategy)
def test_mealymodel_alphabet_characters_setter(instance):
    original = instance.characters
    instance.characters = original
    assert instance.characters == original
