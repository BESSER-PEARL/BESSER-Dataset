import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    dfa::Symbol,
    dfa::Transition,
    State,
    dfa::NamedElement,
    dfa::FinalState,
    dfa::RegularState,
    RegularState,
    dfa::InitialState,
    NamedElement,
    dfa::Language,
    dfa::State,
    dfa::Dfa,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dfa::symbol_is_not_abstract():
    assert not inspect.isabstract(dfa::Symbol)


def test_dfa::symbol_constructor_exists():
    assert callable(dfa::Symbol.__init__)


def test_dfa::symbol_constructor_args():
    sig = inspect.signature(dfa::Symbol.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"
    assert "literal" in params, "Missing parameter 'literal'"
    assert "description" in params, "Missing parameter 'description'"

def test_dfa::symbol_has_direction():
    assert hasattr(dfa::Symbol, "direction")
    descriptor = None
    for klass in dfa::Symbol.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_dfa::symbol_has_literal():
    assert hasattr(dfa::Symbol, "literal")
    descriptor = None
    for klass in dfa::Symbol.__mro__:
        if "literal" in klass.__dict__:
            descriptor = klass.__dict__["literal"]
            break
    assert isinstance(descriptor, property)

def test_dfa::symbol_has_description():
    assert hasattr(dfa::Symbol, "description")
    descriptor = None
    for klass in dfa::Symbol.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_dfa::transition_is_not_abstract():
    assert not inspect.isabstract(dfa::Transition)


def test_dfa::transition_constructor_exists():
    assert callable(dfa::Transition.__init__)


def test_dfa::transition_constructor_args():
    sig = inspect.signature(dfa::Transition.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_dfa::namedelement_is_not_abstract():
    assert not inspect.isabstract(dfa::NamedElement)


def test_dfa::namedelement_constructor_exists():
    assert callable(dfa::NamedElement.__init__)


def test_dfa::namedelement_constructor_args():
    sig = inspect.signature(dfa::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dfa::namedelement_has_name():
    assert hasattr(dfa::NamedElement, "name")
    descriptor = None
    for klass in dfa::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dfa::finalstate_is_not_abstract():
    assert not inspect.isabstract(dfa::FinalState)


def test_dfa::finalstate_constructor_exists():
    assert callable(dfa::FinalState.__init__)


def test_dfa::finalstate_constructor_args():
    sig = inspect.signature(dfa::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_dfa::regularstate_is_not_abstract():
    assert not inspect.isabstract(dfa::RegularState)


def test_dfa::regularstate_constructor_exists():
    assert callable(dfa::RegularState.__init__)


def test_dfa::regularstate_constructor_args():
    sig = inspect.signature(dfa::RegularState.__init__)
    params = list(sig.parameters.keys())



def test_regularstate_is_not_abstract():
    assert not inspect.isabstract(RegularState)


def test_regularstate_constructor_exists():
    assert callable(RegularState.__init__)


def test_regularstate_constructor_args():
    sig = inspect.signature(RegularState.__init__)
    params = list(sig.parameters.keys())



def test_dfa::initialstate_is_not_abstract():
    assert not inspect.isabstract(dfa::InitialState)


def test_dfa::initialstate_constructor_exists():
    assert callable(dfa::InitialState.__init__)


def test_dfa::initialstate_constructor_args():
    sig = inspect.signature(dfa::InitialState.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_dfa::language_is_not_abstract():
    assert not inspect.isabstract(dfa::Language)


def test_dfa::language_constructor_exists():
    assert callable(dfa::Language.__init__)


def test_dfa::language_constructor_args():
    sig = inspect.signature(dfa::Language.__init__)
    params = list(sig.parameters.keys())



def test_dfa::state_is_not_abstract():
    assert not inspect.isabstract(dfa::State)


def test_dfa::state_constructor_exists():
    assert callable(dfa::State.__init__)


def test_dfa::state_constructor_args():
    sig = inspect.signature(dfa::State.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_dfa::state_has_description():
    assert hasattr(dfa::State, "description")
    descriptor = None
    for klass in dfa::State.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_dfa::dfa_is_not_abstract():
    assert not inspect.isabstract(dfa::Dfa)


def test_dfa::dfa_constructor_exists():
    assert callable(dfa::Dfa.__init__)


def test_dfa::dfa_constructor_args():
    sig = inspect.signature(dfa::Dfa.__init__)
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
dfa::Symbol_strategy = st.builds(
    dfa::Symbol,
    direction=
        safe_text,
    literal=
        safe_text,
    description=
        safe_text
)
dfa::Transition_strategy = st.builds(
    dfa::Transition,
)
State_strategy = st.builds(
    State,
)
dfa::NamedElement_strategy = st.builds(
    dfa::NamedElement,
    name=
        safe_text
)
dfa::FinalState_strategy = st.builds(
    dfa::FinalState,
)
dfa::RegularState_strategy = st.builds(
    dfa::RegularState,
)
RegularState_strategy = st.builds(
    RegularState,
)
dfa::InitialState_strategy = st.builds(
    dfa::InitialState,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
dfa::Language_strategy = st.builds(
    dfa::Language,
)
dfa::State_strategy = st.builds(
    dfa::State,
    description=
        safe_text
)
dfa::Dfa_strategy = st.builds(
    dfa::Dfa,
)

@given(instance=dfa::Symbol_strategy)
@settings(max_examples=50)
def test_dfa::symbol_instantiation(instance):
    assert isinstance(instance, dfa::Symbol)

@given(instance=dfa::Symbol_strategy)
def test_dfa::symbol_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=dfa::Symbol_strategy)
def test_dfa::symbol_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=dfa::Symbol_strategy)
def test_dfa::symbol_literal_type(instance):
    assert isinstance(instance.literal, str)


@given(instance=dfa::Symbol_strategy)
def test_dfa::symbol_literal_setter(instance):
    original = instance.literal
    instance.literal = original
    assert instance.literal == original

@given(instance=dfa::Symbol_strategy)
def test_dfa::symbol_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=dfa::Symbol_strategy)
def test_dfa::symbol_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=dfa::Transition_strategy)
@settings(max_examples=50)
def test_dfa::transition_instantiation(instance):
    assert isinstance(instance, dfa::Transition)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=dfa::NamedElement_strategy)
@settings(max_examples=50)
def test_dfa::namedelement_instantiation(instance):
    assert isinstance(instance, dfa::NamedElement)

@given(instance=dfa::NamedElement_strategy)
def test_dfa::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dfa::NamedElement_strategy)
def test_dfa::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dfa::FinalState_strategy)
@settings(max_examples=50)
def test_dfa::finalstate_instantiation(instance):
    assert isinstance(instance, dfa::FinalState)

@given(instance=dfa::RegularState_strategy)
@settings(max_examples=50)
def test_dfa::regularstate_instantiation(instance):
    assert isinstance(instance, dfa::RegularState)

@given(instance=RegularState_strategy)
@settings(max_examples=50)
def test_regularstate_instantiation(instance):
    assert isinstance(instance, RegularState)

@given(instance=dfa::InitialState_strategy)
@settings(max_examples=50)
def test_dfa::initialstate_instantiation(instance):
    assert isinstance(instance, dfa::InitialState)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=dfa::Language_strategy)
@settings(max_examples=50)
def test_dfa::language_instantiation(instance):
    assert isinstance(instance, dfa::Language)

@given(instance=dfa::State_strategy)
@settings(max_examples=50)
def test_dfa::state_instantiation(instance):
    assert isinstance(instance, dfa::State)

@given(instance=dfa::State_strategy)
def test_dfa::state_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=dfa::State_strategy)
def test_dfa::state_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=dfa::Dfa_strategy)
@settings(max_examples=50)
def test_dfa::dfa_instantiation(instance):
    assert isinstance(instance, dfa::Dfa)
