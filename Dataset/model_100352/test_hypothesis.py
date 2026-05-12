import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    dfa_Symbol,
    dfa_Transition,
    State,
    dfa_NamedElement,
    dfa_FinalState,
    dfa_RegularState,
    RegularState,
    dfa_InitialState,
    NamedElement,
    dfa_Language,
    dfa_State,
    dfa_Dfa,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dfa_symbol_is_not_abstract():
    assert not inspect.isabstract(dfa_Symbol)


def test_dfa_symbol_constructor_exists():
    assert callable(dfa_Symbol.__init__)


def test_dfa_symbol_constructor_args():
    sig = inspect.signature(dfa_Symbol.__init__)
    params = list(sig.parameters.keys())
    assert "literal" in params, "Missing parameter 'literal'"
    assert "description" in params, "Missing parameter 'description'"
    assert "direction" in params, "Missing parameter 'direction'"

def test_dfa_symbol_has_literal():
    assert hasattr(dfa_Symbol, "literal")
    descriptor = None
    for klass in dfa_Symbol.__mro__:
        if "literal" in klass.__dict__:
            descriptor = klass.__dict__["literal"]
            break
    assert isinstance(descriptor, property)

def test_dfa_symbol_has_description():
    assert hasattr(dfa_Symbol, "description")
    descriptor = None
    for klass in dfa_Symbol.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_dfa_symbol_has_direction():
    assert hasattr(dfa_Symbol, "direction")
    descriptor = None
    for klass in dfa_Symbol.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_dfa_transition_is_not_abstract():
    assert not inspect.isabstract(dfa_Transition)


def test_dfa_transition_constructor_exists():
    assert callable(dfa_Transition.__init__)


def test_dfa_transition_constructor_args():
    sig = inspect.signature(dfa_Transition.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_dfa_namedelement_is_not_abstract():
    assert not inspect.isabstract(dfa_NamedElement)


def test_dfa_namedelement_constructor_exists():
    assert callable(dfa_NamedElement.__init__)


def test_dfa_namedelement_constructor_args():
    sig = inspect.signature(dfa_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dfa_namedelement_has_name():
    assert hasattr(dfa_NamedElement, "name")
    descriptor = None
    for klass in dfa_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dfa_finalstate_is_not_abstract():
    assert not inspect.isabstract(dfa_FinalState)


def test_dfa_finalstate_constructor_exists():
    assert callable(dfa_FinalState.__init__)


def test_dfa_finalstate_constructor_args():
    sig = inspect.signature(dfa_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_dfa_regularstate_is_not_abstract():
    assert not inspect.isabstract(dfa_RegularState)


def test_dfa_regularstate_constructor_exists():
    assert callable(dfa_RegularState.__init__)


def test_dfa_regularstate_constructor_args():
    sig = inspect.signature(dfa_RegularState.__init__)
    params = list(sig.parameters.keys())



def test_regularstate_is_not_abstract():
    assert not inspect.isabstract(RegularState)


def test_regularstate_constructor_exists():
    assert callable(RegularState.__init__)


def test_regularstate_constructor_args():
    sig = inspect.signature(RegularState.__init__)
    params = list(sig.parameters.keys())



def test_dfa_initialstate_is_not_abstract():
    assert not inspect.isabstract(dfa_InitialState)


def test_dfa_initialstate_constructor_exists():
    assert callable(dfa_InitialState.__init__)


def test_dfa_initialstate_constructor_args():
    sig = inspect.signature(dfa_InitialState.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_dfa_language_is_not_abstract():
    assert not inspect.isabstract(dfa_Language)


def test_dfa_language_constructor_exists():
    assert callable(dfa_Language.__init__)


def test_dfa_language_constructor_args():
    sig = inspect.signature(dfa_Language.__init__)
    params = list(sig.parameters.keys())



def test_dfa_state_is_not_abstract():
    assert not inspect.isabstract(dfa_State)


def test_dfa_state_constructor_exists():
    assert callable(dfa_State.__init__)


def test_dfa_state_constructor_args():
    sig = inspect.signature(dfa_State.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_dfa_state_has_description():
    assert hasattr(dfa_State, "description")
    descriptor = None
    for klass in dfa_State.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_dfa_dfa_is_not_abstract():
    assert not inspect.isabstract(dfa_Dfa)


def test_dfa_dfa_constructor_exists():
    assert callable(dfa_Dfa.__init__)


def test_dfa_dfa_constructor_args():
    sig = inspect.signature(dfa_Dfa.__init__)
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
dfa_Symbol_strategy = st.builds(
    dfa_Symbol,
    literal=
        safe_text,
    description=
        safe_text,
    direction=
        safe_text
)
dfa_Transition_strategy = st.builds(
    dfa_Transition,
)
State_strategy = st.builds(
    State,
)
dfa_NamedElement_strategy = st.builds(
    dfa_NamedElement,
    name=
        safe_text
)
dfa_FinalState_strategy = st.builds(
    dfa_FinalState,
)
dfa_RegularState_strategy = st.builds(
    dfa_RegularState,
)
RegularState_strategy = st.builds(
    RegularState,
)
dfa_InitialState_strategy = st.builds(
    dfa_InitialState,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
dfa_Language_strategy = st.builds(
    dfa_Language,
)
dfa_State_strategy = st.builds(
    dfa_State,
    description=
        safe_text
)
dfa_Dfa_strategy = st.builds(
    dfa_Dfa,
)

@given(instance=dfa_Symbol_strategy)
@settings(max_examples=50)
def test_dfa_symbol_instantiation(instance):
    assert isinstance(instance, dfa_Symbol)



@given(instance=dfa_Symbol_strategy)
def test_dfa_symbol_literal_setter(instance):
    original = instance.literal
    instance.literal = original
    assert instance.literal == original



@given(instance=dfa_Symbol_strategy)
def test_dfa_symbol_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=dfa_Symbol_strategy)
def test_dfa_symbol_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=dfa_Transition_strategy)
@settings(max_examples=50)
def test_dfa_transition_instantiation(instance):
    assert isinstance(instance, dfa_Transition)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=dfa_NamedElement_strategy)
@settings(max_examples=50)
def test_dfa_namedelement_instantiation(instance):
    assert isinstance(instance, dfa_NamedElement)



@given(instance=dfa_NamedElement_strategy)
def test_dfa_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dfa_FinalState_strategy)
@settings(max_examples=50)
def test_dfa_finalstate_instantiation(instance):
    assert isinstance(instance, dfa_FinalState)

@given(instance=dfa_RegularState_strategy)
@settings(max_examples=50)
def test_dfa_regularstate_instantiation(instance):
    assert isinstance(instance, dfa_RegularState)

@given(instance=RegularState_strategy)
@settings(max_examples=50)
def test_regularstate_instantiation(instance):
    assert isinstance(instance, RegularState)

@given(instance=dfa_InitialState_strategy)
@settings(max_examples=50)
def test_dfa_initialstate_instantiation(instance):
    assert isinstance(instance, dfa_InitialState)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=dfa_Language_strategy)
@settings(max_examples=50)
def test_dfa_language_instantiation(instance):
    assert isinstance(instance, dfa_Language)

@given(instance=dfa_State_strategy)
@settings(max_examples=50)
def test_dfa_state_instantiation(instance):
    assert isinstance(instance, dfa_State)



@given(instance=dfa_State_strategy)
def test_dfa_state_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=dfa_Dfa_strategy)
@settings(max_examples=50)
def test_dfa_dfa_instantiation(instance):
    assert isinstance(instance, dfa_Dfa)
