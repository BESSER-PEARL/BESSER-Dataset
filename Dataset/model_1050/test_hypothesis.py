import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    fsm_Transition,
    fsm_State,
    fsm_Machine,
    fsm_Language,
    fsm_Constraint,
    fsm_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsm_transition_is_not_abstract():
    assert not inspect.isabstract(fsm_Transition)


def test_fsm_transition_constructor_exists():
    assert callable(fsm_Transition.__init__)


def test_fsm_transition_constructor_args():
    sig = inspect.signature(fsm_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"

def test_fsm_transition_has_event():
    assert hasattr(fsm_Transition, "event")
    descriptor = None
    for klass in fsm_Transition.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)



def test_fsm_state_is_not_abstract():
    assert not inspect.isabstract(fsm_State)


def test_fsm_state_constructor_exists():
    assert callable(fsm_State.__init__)


def test_fsm_state_constructor_args():
    sig = inspect.signature(fsm_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "initial" in params, "Missing parameter 'initial'"
    assert "final" in params, "Missing parameter 'final'"

def test_fsm_state_has_name():
    assert hasattr(fsm_State, "name")
    descriptor = None
    for klass in fsm_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fsm_state_has_initial():
    assert hasattr(fsm_State, "initial")
    descriptor = None
    for klass in fsm_State.__mro__:
        if "initial" in klass.__dict__:
            descriptor = klass.__dict__["initial"]
            break
    assert isinstance(descriptor, property)

def test_fsm_state_has_final():
    assert hasattr(fsm_State, "final")
    descriptor = None
    for klass in fsm_State.__mro__:
        if "final" in klass.__dict__:
            descriptor = klass.__dict__["final"]
            break
    assert isinstance(descriptor, property)



def test_fsm_machine_is_not_abstract():
    assert not inspect.isabstract(fsm_Machine)


def test_fsm_machine_constructor_exists():
    assert callable(fsm_Machine.__init__)


def test_fsm_machine_constructor_args():
    sig = inspect.signature(fsm_Machine.__init__)
    params = list(sig.parameters.keys())



def test_fsm_language_is_not_abstract():
    assert not inspect.isabstract(fsm_Language)


def test_fsm_language_constructor_exists():
    assert callable(fsm_Language.__init__)


def test_fsm_language_constructor_args():
    sig = inspect.signature(fsm_Language.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "target" in params, "Missing parameter 'target'"

def test_fsm_language_has_name():
    assert hasattr(fsm_Language, "name")
    descriptor = None
    for klass in fsm_Language.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fsm_language_has_target():
    assert hasattr(fsm_Language, "target")
    descriptor = None
    for klass in fsm_Language.__mro__:
        if "target" in klass.__dict__:
            descriptor = klass.__dict__["target"]
            break
    assert isinstance(descriptor, property)



def test_fsm_constraint_is_not_abstract():
    assert not inspect.isabstract(fsm_Constraint)


def test_fsm_constraint_constructor_exists():
    assert callable(fsm_Constraint.__init__)


def test_fsm_constraint_constructor_args():
    sig = inspect.signature(fsm_Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "true" in params, "Missing parameter 'true'"

def test_fsm_constraint_has_name():
    assert hasattr(fsm_Constraint, "name")
    descriptor = None
    for klass in fsm_Constraint.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fsm_constraint_has_true():
    assert hasattr(fsm_Constraint, "true")
    descriptor = None
    for klass in fsm_Constraint.__mro__:
        if "true" in klass.__dict__:
            descriptor = klass.__dict__["true"]
            break
    assert isinstance(descriptor, property)



def test_fsm_model_is_not_abstract():
    assert not inspect.isabstract(fsm_Model)


def test_fsm_model_constructor_exists():
    assert callable(fsm_Model.__init__)


def test_fsm_model_constructor_args():
    sig = inspect.signature(fsm_Model.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm_model_has_name():
    assert hasattr(fsm_Model, "name")
    descriptor = None
    for klass in fsm_Model.__mro__:
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
fsm_Transition_strategy = st.builds(
    fsm_Transition,
    event=
        safe_text
)
fsm_State_strategy = st.builds(
    fsm_State,
    name=
        safe_text,
    initial=
        st.booleans(),
    final=
        st.booleans()
)
fsm_Machine_strategy = st.builds(
    fsm_Machine,
)
fsm_Language_strategy = st.builds(
    fsm_Language,
    name=
        safe_text,
    target=
        safe_text
)
fsm_Constraint_strategy = st.builds(
    fsm_Constraint,
    name=
        safe_text,
    true=
        st.booleans()
)
fsm_Model_strategy = st.builds(
    fsm_Model,
    name=
        safe_text
)

@given(instance=fsm_Transition_strategy)
@settings(max_examples=50)
def test_fsm_transition_instantiation(instance):
    assert isinstance(instance, fsm_Transition)



@given(instance=fsm_Transition_strategy)
def test_fsm_transition_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=fsm_State_strategy)
@settings(max_examples=50)
def test_fsm_state_instantiation(instance):
    assert isinstance(instance, fsm_State)



@given(instance=fsm_State_strategy)
def test_fsm_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fsm_State_strategy)
def test_fsm_state_initial_setter(instance):
    original = instance.initial
    instance.initial = original
    assert instance.initial == original



@given(instance=fsm_State_strategy)
def test_fsm_state_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original

@given(instance=fsm_Machine_strategy)
@settings(max_examples=50)
def test_fsm_machine_instantiation(instance):
    assert isinstance(instance, fsm_Machine)

@given(instance=fsm_Language_strategy)
@settings(max_examples=50)
def test_fsm_language_instantiation(instance):
    assert isinstance(instance, fsm_Language)



@given(instance=fsm_Language_strategy)
def test_fsm_language_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fsm_Language_strategy)
def test_fsm_language_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original

@given(instance=fsm_Constraint_strategy)
@settings(max_examples=50)
def test_fsm_constraint_instantiation(instance):
    assert isinstance(instance, fsm_Constraint)



@given(instance=fsm_Constraint_strategy)
def test_fsm_constraint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fsm_Constraint_strategy)
def test_fsm_constraint_true_setter(instance):
    original = instance.true
    instance.true = original
    assert instance.true == original

@given(instance=fsm_Model_strategy)
@settings(max_examples=50)
def test_fsm_model_instantiation(instance):
    assert isinstance(instance, fsm_Model)



@given(instance=fsm_Model_strategy)
def test_fsm_model_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
