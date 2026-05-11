import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    fsa::Transition,
    fsa::FSA,
    fsa::State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsa::transition_is_not_abstract():
    assert not inspect.isabstract(fsa::Transition)


def test_fsa::transition_constructor_exists():
    assert callable(fsa::Transition.__init__)


def test_fsa::transition_constructor_args():
    sig = inspect.signature(fsa::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_fsa::transition_has_description():
    assert hasattr(fsa::Transition, "description")
    descriptor = None
    for klass in fsa::Transition.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_fsa::fsa_is_not_abstract():
    assert not inspect.isabstract(fsa::FSA)


def test_fsa::fsa_constructor_exists():
    assert callable(fsa::FSA.__init__)


def test_fsa::fsa_constructor_args():
    sig = inspect.signature(fsa::FSA.__init__)
    params = list(sig.parameters.keys())
    assert "temporalFormula" in params, "Missing parameter 'temporalFormula'"

def test_fsa::fsa_has_temporalFormula():
    assert hasattr(fsa::FSA, "temporalFormula")
    descriptor = None
    for klass in fsa::FSA.__mro__:
        if "temporalFormula" in klass.__dict__:
            descriptor = klass.__dict__["temporalFormula"]
            break
    assert isinstance(descriptor, property)



def test_fsa::state_is_not_abstract():
    assert not inspect.isabstract(fsa::State)


def test_fsa::state_constructor_exists():
    assert callable(fsa::State.__init__)


def test_fsa::state_constructor_args():
    sig = inspect.signature(fsa::State.__init__)
    params = list(sig.parameters.keys())
    assert "temporalProperties" in params, "Missing parameter 'temporalProperties'"
    assert "final" in params, "Missing parameter 'final'"
    assert "name" in params, "Missing parameter 'name'"

def test_fsa::state_has_temporalProperties():
    assert hasattr(fsa::State, "temporalProperties")
    descriptor = None
    for klass in fsa::State.__mro__:
        if "temporalProperties" in klass.__dict__:
            descriptor = klass.__dict__["temporalProperties"]
            break
    assert isinstance(descriptor, property)

def test_fsa::state_has_final():
    assert hasattr(fsa::State, "final")
    descriptor = None
    for klass in fsa::State.__mro__:
        if "final" in klass.__dict__:
            descriptor = klass.__dict__["final"]
            break
    assert isinstance(descriptor, property)

def test_fsa::state_has_name():
    assert hasattr(fsa::State, "name")
    descriptor = None
    for klass in fsa::State.__mro__:
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
fsa::Transition_strategy = st.builds(
    fsa::Transition,
    description=
        safe_text
)
fsa::FSA_strategy = st.builds(
    fsa::FSA,
    temporalFormula=
        safe_text
)
fsa::State_strategy = st.builds(
    fsa::State,
    temporalProperties=
        safe_text,
    final=
        st.booleans(),
    name=
        safe_text
)

@given(instance=fsa::Transition_strategy)
@settings(max_examples=50)
def test_fsa::transition_instantiation(instance):
    assert isinstance(instance, fsa::Transition)

@given(instance=fsa::Transition_strategy)
def test_fsa::transition_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=fsa::Transition_strategy)
def test_fsa::transition_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=fsa::FSA_strategy)
@settings(max_examples=50)
def test_fsa::fsa_instantiation(instance):
    assert isinstance(instance, fsa::FSA)

@given(instance=fsa::FSA_strategy)
def test_fsa::fsa_temporalFormula_type(instance):
    assert isinstance(instance.temporalFormula, str)


@given(instance=fsa::FSA_strategy)
def test_fsa::fsa_temporalFormula_setter(instance):
    original = instance.temporalFormula
    instance.temporalFormula = original
    assert instance.temporalFormula == original

@given(instance=fsa::State_strategy)
@settings(max_examples=50)
def test_fsa::state_instantiation(instance):
    assert isinstance(instance, fsa::State)

@given(instance=fsa::State_strategy)
def test_fsa::state_temporalProperties_type(instance):
    assert isinstance(instance.temporalProperties, str)


@given(instance=fsa::State_strategy)
def test_fsa::state_temporalProperties_setter(instance):
    original = instance.temporalProperties
    instance.temporalProperties = original
    assert instance.temporalProperties == original

@given(instance=fsa::State_strategy)
def test_fsa::state_final_type(instance):
    assert isinstance(instance.final, bool)


@given(instance=fsa::State_strategy)
def test_fsa::state_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original

@given(instance=fsa::State_strategy)
def test_fsa::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsa::State_strategy)
def test_fsa::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
