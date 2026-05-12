import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    AbstractState,
    errorstm_InitialState,
    errorstm_FinalState,
    errorstm_SimpleState,
    errorstm_CompositeState,
    errorstm_Action,
    errorstm_AbstractState,
    errorstm_Transition,
    errorstm_StateMachine,
    ActionKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_errorstm_initialstate_is_not_abstract():
    assert not inspect.isabstract(errorstm_InitialState)


def test_errorstm_initialstate_constructor_exists():
    assert callable(errorstm_InitialState.__init__)


def test_errorstm_initialstate_constructor_args():
    sig = inspect.signature(errorstm_InitialState.__init__)
    params = list(sig.parameters.keys())



def test_errorstm_finalstate_is_not_abstract():
    assert not inspect.isabstract(errorstm_FinalState)


def test_errorstm_finalstate_constructor_exists():
    assert callable(errorstm_FinalState.__init__)


def test_errorstm_finalstate_constructor_args():
    sig = inspect.signature(errorstm_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_errorstm_simplestate_is_not_abstract():
    assert not inspect.isabstract(errorstm_SimpleState)


def test_errorstm_simplestate_constructor_exists():
    assert callable(errorstm_SimpleState.__init__)


def test_errorstm_simplestate_constructor_args():
    sig = inspect.signature(errorstm_SimpleState.__init__)
    params = list(sig.parameters.keys())



def test_errorstm_compositestate_is_not_abstract():
    assert not inspect.isabstract(errorstm_CompositeState)


def test_errorstm_compositestate_constructor_exists():
    assert callable(errorstm_CompositeState.__init__)


def test_errorstm_compositestate_constructor_args():
    sig = inspect.signature(errorstm_CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_errorstm_action_is_not_abstract():
    assert not inspect.isabstract(errorstm_Action)


def test_errorstm_action_constructor_exists():
    assert callable(errorstm_Action.__init__)


def test_errorstm_action_constructor_args():
    sig = inspect.signature(errorstm_Action.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_errorstm_action_has_kind():
    assert hasattr(errorstm_Action, "kind")
    descriptor = None
    for klass in errorstm_Action.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_errorstm_abstractstate_is_not_abstract():
    assert not inspect.isabstract(errorstm_AbstractState)


def test_errorstm_abstractstate_constructor_exists():
    assert callable(errorstm_AbstractState.__init__)


def test_errorstm_abstractstate_constructor_args():
    sig = inspect.signature(errorstm_AbstractState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_errorstm_abstractstate_has_name():
    assert hasattr(errorstm_AbstractState, "name")
    descriptor = None
    for klass in errorstm_AbstractState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_errorstm_transition_is_not_abstract():
    assert not inspect.isabstract(errorstm_Transition)


def test_errorstm_transition_constructor_exists():
    assert callable(errorstm_Transition.__init__)


def test_errorstm_transition_constructor_args():
    sig = inspect.signature(errorstm_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"
    assert "guard" in params, "Missing parameter 'guard'"
    assert "name" in params, "Missing parameter 'name'"

def test_errorstm_transition_has_event():
    assert hasattr(errorstm_Transition, "event")
    descriptor = None
    for klass in errorstm_Transition.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)

def test_errorstm_transition_has_guard():
    assert hasattr(errorstm_Transition, "guard")
    descriptor = None
    for klass in errorstm_Transition.__mro__:
        if "guard" in klass.__dict__:
            descriptor = klass.__dict__["guard"]
            break
    assert isinstance(descriptor, property)

def test_errorstm_transition_has_name():
    assert hasattr(errorstm_Transition, "name")
    descriptor = None
    for klass in errorstm_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_errorstm_statemachine_is_not_abstract():
    assert not inspect.isabstract(errorstm_StateMachine)


def test_errorstm_statemachine_constructor_exists():
    assert callable(errorstm_StateMachine.__init__)


def test_errorstm_statemachine_constructor_args():
    sig = inspect.signature(errorstm_StateMachine.__init__)
    params = list(sig.parameters.keys())

def test_actionkind_exists():
    # Check that the Enumeration exists
    assert ActionKind is not None

def test_actionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ActionKind]
    expected_literals = [
        "EXIT",
        "ENTRY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ActionKind"


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
AbstractState_strategy = st.builds(
    AbstractState,
)
errorstm_InitialState_strategy = st.builds(
    errorstm_InitialState,
)
errorstm_FinalState_strategy = st.builds(
    errorstm_FinalState,
)
errorstm_SimpleState_strategy = st.builds(
    errorstm_SimpleState,
)
errorstm_CompositeState_strategy = st.builds(
    errorstm_CompositeState,
)
errorstm_Action_strategy = st.builds(
    errorstm_Action,
    kind=
        safe_text
)
errorstm_AbstractState_strategy = st.builds(
    errorstm_AbstractState,
    name=
        safe_text
)
errorstm_Transition_strategy = st.builds(
    errorstm_Transition,
    event=
        safe_text,
    guard=
        safe_text,
    name=
        safe_text
)
errorstm_StateMachine_strategy = st.builds(
    errorstm_StateMachine,
)

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=errorstm_InitialState_strategy)
@settings(max_examples=50)
def test_errorstm_initialstate_instantiation(instance):
    assert isinstance(instance, errorstm_InitialState)

@given(instance=errorstm_FinalState_strategy)
@settings(max_examples=50)
def test_errorstm_finalstate_instantiation(instance):
    assert isinstance(instance, errorstm_FinalState)

@given(instance=errorstm_SimpleState_strategy)
@settings(max_examples=50)
def test_errorstm_simplestate_instantiation(instance):
    assert isinstance(instance, errorstm_SimpleState)

@given(instance=errorstm_CompositeState_strategy)
@settings(max_examples=50)
def test_errorstm_compositestate_instantiation(instance):
    assert isinstance(instance, errorstm_CompositeState)

@given(instance=errorstm_Action_strategy)
@settings(max_examples=50)
def test_errorstm_action_instantiation(instance):
    assert isinstance(instance, errorstm_Action)



@given(instance=errorstm_Action_strategy)
def test_errorstm_action_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=errorstm_AbstractState_strategy)
@settings(max_examples=50)
def test_errorstm_abstractstate_instantiation(instance):
    assert isinstance(instance, errorstm_AbstractState)



@given(instance=errorstm_AbstractState_strategy)
def test_errorstm_abstractstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=errorstm_Transition_strategy)
@settings(max_examples=50)
def test_errorstm_transition_instantiation(instance):
    assert isinstance(instance, errorstm_Transition)



@given(instance=errorstm_Transition_strategy)
def test_errorstm_transition_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original



@given(instance=errorstm_Transition_strategy)
def test_errorstm_transition_guard_setter(instance):
    original = instance.guard
    instance.guard = original
    assert instance.guard == original



@given(instance=errorstm_Transition_strategy)
def test_errorstm_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=errorstm_StateMachine_strategy)
@settings(max_examples=50)
def test_errorstm_statemachine_instantiation(instance):
    assert isinstance(instance, errorstm_StateMachine)
