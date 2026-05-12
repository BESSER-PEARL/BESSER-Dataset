import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    NamedElement,
    automaton_Output,
    automaton_Input,
    automaton_Transition,
    automaton_State,
    automaton_NamedElement,
    automaton_Automaton,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_automaton_output_is_not_abstract():
    assert not inspect.isabstract(automaton_Output)


def test_automaton_output_constructor_exists():
    assert callable(automaton_Output.__init__)


def test_automaton_output_constructor_args():
    sig = inspect.signature(automaton_Output.__init__)
    params = list(sig.parameters.keys())



def test_automaton_input_is_not_abstract():
    assert not inspect.isabstract(automaton_Input)


def test_automaton_input_constructor_exists():
    assert callable(automaton_Input.__init__)


def test_automaton_input_constructor_args():
    sig = inspect.signature(automaton_Input.__init__)
    params = list(sig.parameters.keys())



def test_automaton_transition_is_not_abstract():
    assert not inspect.isabstract(automaton_Transition)


def test_automaton_transition_constructor_exists():
    assert callable(automaton_Transition.__init__)


def test_automaton_transition_constructor_args():
    sig = inspect.signature(automaton_Transition.__init__)
    params = list(sig.parameters.keys())



def test_automaton_state_is_not_abstract():
    assert not inspect.isabstract(automaton_State)


def test_automaton_state_constructor_exists():
    assert callable(automaton_State.__init__)


def test_automaton_state_constructor_args():
    sig = inspect.signature(automaton_State.__init__)
    params = list(sig.parameters.keys())



def test_automaton_namedelement_is_not_abstract():
    assert not inspect.isabstract(automaton_NamedElement)


def test_automaton_namedelement_constructor_exists():
    assert callable(automaton_NamedElement.__init__)


def test_automaton_namedelement_constructor_args():
    sig = inspect.signature(automaton_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_automaton_namedelement_has_name():
    assert hasattr(automaton_NamedElement, "name")
    descriptor = None
    for klass in automaton_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_automaton_automaton_is_not_abstract():
    assert not inspect.isabstract(automaton_Automaton)


def test_automaton_automaton_constructor_exists():
    assert callable(automaton_Automaton.__init__)


def test_automaton_automaton_constructor_args():
    sig = inspect.signature(automaton_Automaton.__init__)
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
NamedElement_strategy = st.builds(
    NamedElement,
)
automaton_Output_strategy = st.builds(
    automaton_Output,
)
automaton_Input_strategy = st.builds(
    automaton_Input,
)
automaton_Transition_strategy = st.builds(
    automaton_Transition,
)
automaton_State_strategy = st.builds(
    automaton_State,
)
automaton_NamedElement_strategy = st.builds(
    automaton_NamedElement,
    name=
        safe_text
)
automaton_Automaton_strategy = st.builds(
    automaton_Automaton,
)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=automaton_Output_strategy)
@settings(max_examples=50)
def test_automaton_output_instantiation(instance):
    assert isinstance(instance, automaton_Output)

@given(instance=automaton_Input_strategy)
@settings(max_examples=50)
def test_automaton_input_instantiation(instance):
    assert isinstance(instance, automaton_Input)

@given(instance=automaton_Transition_strategy)
@settings(max_examples=50)
def test_automaton_transition_instantiation(instance):
    assert isinstance(instance, automaton_Transition)

@given(instance=automaton_State_strategy)
@settings(max_examples=50)
def test_automaton_state_instantiation(instance):
    assert isinstance(instance, automaton_State)

@given(instance=automaton_NamedElement_strategy)
@settings(max_examples=50)
def test_automaton_namedelement_instantiation(instance):
    assert isinstance(instance, automaton_NamedElement)



@given(instance=automaton_NamedElement_strategy)
def test_automaton_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=automaton_Automaton_strategy)
@settings(max_examples=50)
def test_automaton_automaton_instantiation(instance):
    assert isinstance(instance, automaton_Automaton)
