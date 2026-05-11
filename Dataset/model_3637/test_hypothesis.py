import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    DFAAutomaton::Symbol,
    DFAAutomaton::Transition,
    DFAAutomaton::State,
    DFAAutomaton::Automaton,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dfaautomaton::symbol_is_not_abstract():
    assert not inspect.isabstract(DFAAutomaton::Symbol)


def test_dfaautomaton::symbol_constructor_exists():
    assert callable(DFAAutomaton::Symbol.__init__)


def test_dfaautomaton::symbol_constructor_args():
    sig = inspect.signature(DFAAutomaton::Symbol.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_dfaautomaton::symbol_has_symbol():
    assert hasattr(DFAAutomaton::Symbol, "symbol")
    descriptor = None
    for klass in DFAAutomaton::Symbol.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_dfaautomaton::transition_is_not_abstract():
    assert not inspect.isabstract(DFAAutomaton::Transition)


def test_dfaautomaton::transition_constructor_exists():
    assert callable(DFAAutomaton::Transition.__init__)


def test_dfaautomaton::transition_constructor_args():
    sig = inspect.signature(DFAAutomaton::Transition.__init__)
    params = list(sig.parameters.keys())



def test_dfaautomaton::state_is_not_abstract():
    assert not inspect.isabstract(DFAAutomaton::State)


def test_dfaautomaton::state_constructor_exists():
    assert callable(DFAAutomaton::State.__init__)


def test_dfaautomaton::state_constructor_args():
    sig = inspect.signature(DFAAutomaton::State.__init__)
    params = list(sig.parameters.keys())
    assert "isInitial" in params, "Missing parameter 'isInitial'"
    assert "isFinal" in params, "Missing parameter 'isFinal'"
    assert "name" in params, "Missing parameter 'name'"

def test_dfaautomaton::state_has_isInitial():
    assert hasattr(DFAAutomaton::State, "isInitial")
    descriptor = None
    for klass in DFAAutomaton::State.__mro__:
        if "isInitial" in klass.__dict__:
            descriptor = klass.__dict__["isInitial"]
            break
    assert isinstance(descriptor, property)

def test_dfaautomaton::state_has_isFinal():
    assert hasattr(DFAAutomaton::State, "isFinal")
    descriptor = None
    for klass in DFAAutomaton::State.__mro__:
        if "isFinal" in klass.__dict__:
            descriptor = klass.__dict__["isFinal"]
            break
    assert isinstance(descriptor, property)

def test_dfaautomaton::state_has_name():
    assert hasattr(DFAAutomaton::State, "name")
    descriptor = None
    for klass in DFAAutomaton::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dfaautomaton::automaton_is_not_abstract():
    assert not inspect.isabstract(DFAAutomaton::Automaton)


def test_dfaautomaton::automaton_constructor_exists():
    assert callable(DFAAutomaton::Automaton.__init__)


def test_dfaautomaton::automaton_constructor_args():
    sig = inspect.signature(DFAAutomaton::Automaton.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dfaautomaton::automaton_has_name():
    assert hasattr(DFAAutomaton::Automaton, "name")
    descriptor = None
    for klass in DFAAutomaton::Automaton.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
DFAAutomaton::Symbol_strategy = st.builds(
    DFAAutomaton::Symbol,
    symbol=
        safe_text
)
DFAAutomaton::Transition_strategy = st.builds(
    DFAAutomaton::Transition,
)
DFAAutomaton::State_strategy = st.builds(
    DFAAutomaton::State,
    isInitial=
        st.booleans(),
    isFinal=
        st.booleans(),
    name=
        safe_text
)
DFAAutomaton::Automaton_strategy = st.builds(
    DFAAutomaton::Automaton,
    name=
        safe_text
)

@given(instance=DFAAutomaton::Symbol_strategy)
@settings(max_examples=50)
def test_dfaautomaton::symbol_instantiation(instance):
    assert isinstance(instance, DFAAutomaton::Symbol)

@given(instance=DFAAutomaton::Symbol_strategy)
def test_dfaautomaton::symbol_symbol_type(instance):
    assert isinstance(instance.symbol, str)


@given(instance=DFAAutomaton::Symbol_strategy)
def test_dfaautomaton::symbol_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=DFAAutomaton::Transition_strategy)
@settings(max_examples=50)
def test_dfaautomaton::transition_instantiation(instance):
    assert isinstance(instance, DFAAutomaton::Transition)

@given(instance=DFAAutomaton::State_strategy)
@settings(max_examples=50)
def test_dfaautomaton::state_instantiation(instance):
    assert isinstance(instance, DFAAutomaton::State)

@given(instance=DFAAutomaton::State_strategy)
def test_dfaautomaton::state_isInitial_type(instance):
    assert isinstance(instance.isInitial, bool)


@given(instance=DFAAutomaton::State_strategy)
def test_dfaautomaton::state_isInitial_setter(instance):
    original = instance.isInitial
    instance.isInitial = original
    assert instance.isInitial == original

@given(instance=DFAAutomaton::State_strategy)
def test_dfaautomaton::state_isFinal_type(instance):
    assert isinstance(instance.isFinal, bool)


@given(instance=DFAAutomaton::State_strategy)
def test_dfaautomaton::state_isFinal_setter(instance):
    original = instance.isFinal
    instance.isFinal = original
    assert instance.isFinal == original

@given(instance=DFAAutomaton::State_strategy)
def test_dfaautomaton::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=DFAAutomaton::State_strategy)
def test_dfaautomaton::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DFAAutomaton::Automaton_strategy)
@settings(max_examples=50)
def test_dfaautomaton::automaton_instantiation(instance):
    assert isinstance(instance, DFAAutomaton::Automaton)

@given(instance=DFAAutomaton::Automaton_strategy)
def test_dfaautomaton::automaton_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=DFAAutomaton::Automaton_strategy)
def test_dfaautomaton::automaton_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
