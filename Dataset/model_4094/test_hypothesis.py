import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    automaton::NamedElement,
    NamedElement,
    automaton::Output,
    automaton::Input,
    automaton::Automaton,
    automaton::Transition,
    automaton::State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_automaton::namedelement_is_not_abstract():
    assert not inspect.isabstract(automaton::NamedElement)


def test_automaton::namedelement_constructor_exists():
    assert callable(automaton::NamedElement.__init__)


def test_automaton::namedelement_constructor_args():
    sig = inspect.signature(automaton::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_automaton::namedelement_has_name():
    assert hasattr(automaton::NamedElement, "name")
    descriptor = None
    for klass in automaton::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_automaton::output_is_not_abstract():
    assert not inspect.isabstract(automaton::Output)


def test_automaton::output_constructor_exists():
    assert callable(automaton::Output.__init__)


def test_automaton::output_constructor_args():
    sig = inspect.signature(automaton::Output.__init__)
    params = list(sig.parameters.keys())



def test_automaton::input_is_not_abstract():
    assert not inspect.isabstract(automaton::Input)


def test_automaton::input_constructor_exists():
    assert callable(automaton::Input.__init__)


def test_automaton::input_constructor_args():
    sig = inspect.signature(automaton::Input.__init__)
    params = list(sig.parameters.keys())



def test_automaton::automaton_is_not_abstract():
    assert not inspect.isabstract(automaton::Automaton)


def test_automaton::automaton_constructor_exists():
    assert callable(automaton::Automaton.__init__)


def test_automaton::automaton_constructor_args():
    sig = inspect.signature(automaton::Automaton.__init__)
    params = list(sig.parameters.keys())



def test_automaton::transition_is_not_abstract():
    assert not inspect.isabstract(automaton::Transition)


def test_automaton::transition_constructor_exists():
    assert callable(automaton::Transition.__init__)


def test_automaton::transition_constructor_args():
    sig = inspect.signature(automaton::Transition.__init__)
    params = list(sig.parameters.keys())



def test_automaton::state_is_not_abstract():
    assert not inspect.isabstract(automaton::State)


def test_automaton::state_constructor_exists():
    assert callable(automaton::State.__init__)


def test_automaton::state_constructor_args():
    sig = inspect.signature(automaton::State.__init__)
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
automaton::NamedElement_strategy = st.builds(
    automaton::NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
automaton::Output_strategy = st.builds(
    automaton::Output,
)
automaton::Input_strategy = st.builds(
    automaton::Input,
)
automaton::Automaton_strategy = st.builds(
    automaton::Automaton,
)
automaton::Transition_strategy = st.builds(
    automaton::Transition,
)
automaton::State_strategy = st.builds(
    automaton::State,
)

@given(instance=automaton::NamedElement_strategy)
@settings(max_examples=50)
def test_automaton::namedelement_instantiation(instance):
    assert isinstance(instance, automaton::NamedElement)

@given(instance=automaton::NamedElement_strategy)
def test_automaton::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=automaton::NamedElement_strategy)
def test_automaton::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=automaton::Output_strategy)
@settings(max_examples=50)
def test_automaton::output_instantiation(instance):
    assert isinstance(instance, automaton::Output)

@given(instance=automaton::Input_strategy)
@settings(max_examples=50)
def test_automaton::input_instantiation(instance):
    assert isinstance(instance, automaton::Input)

@given(instance=automaton::Automaton_strategy)
@settings(max_examples=50)
def test_automaton::automaton_instantiation(instance):
    assert isinstance(instance, automaton::Automaton)

@given(instance=automaton::Transition_strategy)
@settings(max_examples=50)
def test_automaton::transition_instantiation(instance):
    assert isinstance(instance, automaton::Transition)

@given(instance=automaton::State_strategy)
@settings(max_examples=50)
def test_automaton::state_instantiation(instance):
    assert isinstance(instance, automaton::State)
