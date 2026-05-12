import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    fsa_Transition,
    fsa_FSA,
    fsa_State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsa_transition_is_not_abstract():
    assert not inspect.isabstract(fsa_Transition)


def test_fsa_transition_constructor_exists():
    assert callable(fsa_Transition.__init__)


def test_fsa_transition_constructor_args():
    sig = inspect.signature(fsa_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_fsa_transition_has_description():
    assert hasattr(fsa_Transition, "description")
    descriptor = None
    for klass in fsa_Transition.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_fsa_fsa_is_not_abstract():
    assert not inspect.isabstract(fsa_FSA)


def test_fsa_fsa_constructor_exists():
    assert callable(fsa_FSA.__init__)


def test_fsa_fsa_constructor_args():
    sig = inspect.signature(fsa_FSA.__init__)
    params = list(sig.parameters.keys())
    assert "temporalFormula" in params, "Missing parameter 'temporalFormula'"

def test_fsa_fsa_has_temporalFormula():
    assert hasattr(fsa_FSA, "temporalFormula")
    descriptor = None
    for klass in fsa_FSA.__mro__:
        if "temporalFormula" in klass.__dict__:
            descriptor = klass.__dict__["temporalFormula"]
            break
    assert isinstance(descriptor, property)



def test_fsa_state_is_not_abstract():
    assert not inspect.isabstract(fsa_State)


def test_fsa_state_constructor_exists():
    assert callable(fsa_State.__init__)


def test_fsa_state_constructor_args():
    sig = inspect.signature(fsa_State.__init__)
    params = list(sig.parameters.keys())
    assert "temporalProperties" in params, "Missing parameter 'temporalProperties'"
    assert "final" in params, "Missing parameter 'final'"
    assert "name" in params, "Missing parameter 'name'"

def test_fsa_state_has_temporalProperties():
    assert hasattr(fsa_State, "temporalProperties")
    descriptor = None
    for klass in fsa_State.__mro__:
        if "temporalProperties" in klass.__dict__:
            descriptor = klass.__dict__["temporalProperties"]
            break
    assert isinstance(descriptor, property)

def test_fsa_state_has_final():
    assert hasattr(fsa_State, "final")
    descriptor = None
    for klass in fsa_State.__mro__:
        if "final" in klass.__dict__:
            descriptor = klass.__dict__["final"]
            break
    assert isinstance(descriptor, property)

def test_fsa_state_has_name():
    assert hasattr(fsa_State, "name")
    descriptor = None
    for klass in fsa_State.__mro__:
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
fsa_Transition_strategy = st.builds(
    fsa_Transition,
    description=
        safe_text
)
fsa_FSA_strategy = st.builds(
    fsa_FSA,
    temporalFormula=
        safe_text
)
fsa_State_strategy = st.builds(
    fsa_State,
    temporalProperties=
        safe_text,
    final=
        st.booleans(),
    name=
        safe_text
)

@given(instance=fsa_Transition_strategy)
@settings(max_examples=50)
def test_fsa_transition_instantiation(instance):
    assert isinstance(instance, fsa_Transition)



@given(instance=fsa_Transition_strategy)
def test_fsa_transition_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=fsa_FSA_strategy)
@settings(max_examples=50)
def test_fsa_fsa_instantiation(instance):
    assert isinstance(instance, fsa_FSA)



@given(instance=fsa_FSA_strategy)
def test_fsa_fsa_temporalFormula_setter(instance):
    original = instance.temporalFormula
    instance.temporalFormula = original
    assert instance.temporalFormula == original

@given(instance=fsa_State_strategy)
@settings(max_examples=50)
def test_fsa_state_instantiation(instance):
    assert isinstance(instance, fsa_State)



@given(instance=fsa_State_strategy)
def test_fsa_state_temporalProperties_setter(instance):
    original = instance.temporalProperties
    instance.temporalProperties = original
    assert instance.temporalProperties == original



@given(instance=fsa_State_strategy)
def test_fsa_state_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original



@given(instance=fsa_State_strategy)
def test_fsa_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
