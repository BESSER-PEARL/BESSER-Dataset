import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ModelElement,
    statechart_AbstractState,
    statechart_Transition,
    statechart_ModelElement,
    statechart_StateMachine,
    AbstractState,
    statechart_InitialState,
    statechart_SimpleState,
    statechart_FinalState,
    statechart_CompositeState,
    statechart_Action,
    ActionKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_modelelement_is_not_abstract():
    assert not inspect.isabstract(ModelElement)


def test_modelelement_constructor_exists():
    assert callable(ModelElement.__init__)


def test_modelelement_constructor_args():
    sig = inspect.signature(ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_statechart_abstractstate_is_not_abstract():
    assert not inspect.isabstract(statechart_AbstractState)


def test_statechart_abstractstate_constructor_exists():
    assert callable(statechart_AbstractState.__init__)


def test_statechart_abstractstate_constructor_args():
    sig = inspect.signature(statechart_AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_statechart_transition_is_not_abstract():
    assert not inspect.isabstract(statechart_Transition)


def test_statechart_transition_constructor_exists():
    assert callable(statechart_Transition.__init__)


def test_statechart_transition_constructor_args():
    sig = inspect.signature(statechart_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "guard" in params, "Missing parameter 'guard'"
    assert "event" in params, "Missing parameter 'event'"

def test_statechart_transition_has_guard():
    assert hasattr(statechart_Transition, "guard")
    descriptor = None
    for klass in statechart_Transition.__mro__:
        if "guard" in klass.__dict__:
            descriptor = klass.__dict__["guard"]
            break
    assert isinstance(descriptor, property)

def test_statechart_transition_has_event():
    assert hasattr(statechart_Transition, "event")
    descriptor = None
    for klass in statechart_Transition.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)



def test_statechart_modelelement_is_not_abstract():
    assert not inspect.isabstract(statechart_ModelElement)


def test_statechart_modelelement_constructor_exists():
    assert callable(statechart_ModelElement.__init__)


def test_statechart_modelelement_constructor_args():
    sig = inspect.signature(statechart_ModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statechart_modelelement_has_name():
    assert hasattr(statechart_ModelElement, "name")
    descriptor = None
    for klass in statechart_ModelElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statechart_statemachine_is_not_abstract():
    assert not inspect.isabstract(statechart_StateMachine)


def test_statechart_statemachine_constructor_exists():
    assert callable(statechart_StateMachine.__init__)


def test_statechart_statemachine_constructor_args():
    sig = inspect.signature(statechart_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_statechart_initialstate_is_not_abstract():
    assert not inspect.isabstract(statechart_InitialState)


def test_statechart_initialstate_constructor_exists():
    assert callable(statechart_InitialState.__init__)


def test_statechart_initialstate_constructor_args():
    sig = inspect.signature(statechart_InitialState.__init__)
    params = list(sig.parameters.keys())



def test_statechart_simplestate_is_not_abstract():
    assert not inspect.isabstract(statechart_SimpleState)


def test_statechart_simplestate_constructor_exists():
    assert callable(statechart_SimpleState.__init__)


def test_statechart_simplestate_constructor_args():
    sig = inspect.signature(statechart_SimpleState.__init__)
    params = list(sig.parameters.keys())



def test_statechart_finalstate_is_not_abstract():
    assert not inspect.isabstract(statechart_FinalState)


def test_statechart_finalstate_constructor_exists():
    assert callable(statechart_FinalState.__init__)


def test_statechart_finalstate_constructor_args():
    sig = inspect.signature(statechart_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_statechart_compositestate_is_not_abstract():
    assert not inspect.isabstract(statechart_CompositeState)


def test_statechart_compositestate_constructor_exists():
    assert callable(statechart_CompositeState.__init__)


def test_statechart_compositestate_constructor_args():
    sig = inspect.signature(statechart_CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_statechart_action_is_not_abstract():
    assert not inspect.isabstract(statechart_Action)


def test_statechart_action_constructor_exists():
    assert callable(statechart_Action.__init__)


def test_statechart_action_constructor_args():
    sig = inspect.signature(statechart_Action.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_statechart_action_has_kind():
    assert hasattr(statechart_Action, "kind")
    descriptor = None
    for klass in statechart_Action.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

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
ModelElement_strategy = st.builds(
    ModelElement,
)
statechart_AbstractState_strategy = st.builds(
    statechart_AbstractState,
)
statechart_Transition_strategy = st.builds(
    statechart_Transition,
    guard=
        safe_text,
    event=
        safe_text
)
statechart_ModelElement_strategy = st.builds(
    statechart_ModelElement,
    name=
        safe_text
)
statechart_StateMachine_strategy = st.builds(
    statechart_StateMachine,
)
AbstractState_strategy = st.builds(
    AbstractState,
)
statechart_InitialState_strategy = st.builds(
    statechart_InitialState,
)
statechart_SimpleState_strategy = st.builds(
    statechart_SimpleState,
)
statechart_FinalState_strategy = st.builds(
    statechart_FinalState,
)
statechart_CompositeState_strategy = st.builds(
    statechart_CompositeState,
)
statechart_Action_strategy = st.builds(
    statechart_Action,
    kind=
        safe_text
)

@given(instance=ModelElement_strategy)
@settings(max_examples=50)
def test_modelelement_instantiation(instance):
    assert isinstance(instance, ModelElement)

@given(instance=statechart_AbstractState_strategy)
@settings(max_examples=50)
def test_statechart_abstractstate_instantiation(instance):
    assert isinstance(instance, statechart_AbstractState)

@given(instance=statechart_Transition_strategy)
@settings(max_examples=50)
def test_statechart_transition_instantiation(instance):
    assert isinstance(instance, statechart_Transition)



@given(instance=statechart_Transition_strategy)
def test_statechart_transition_guard_setter(instance):
    original = instance.guard
    instance.guard = original
    assert instance.guard == original



@given(instance=statechart_Transition_strategy)
def test_statechart_transition_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=statechart_ModelElement_strategy)
@settings(max_examples=50)
def test_statechart_modelelement_instantiation(instance):
    assert isinstance(instance, statechart_ModelElement)



@given(instance=statechart_ModelElement_strategy)
def test_statechart_modelelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statechart_StateMachine_strategy)
@settings(max_examples=50)
def test_statechart_statemachine_instantiation(instance):
    assert isinstance(instance, statechart_StateMachine)

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=statechart_InitialState_strategy)
@settings(max_examples=50)
def test_statechart_initialstate_instantiation(instance):
    assert isinstance(instance, statechart_InitialState)

@given(instance=statechart_SimpleState_strategy)
@settings(max_examples=50)
def test_statechart_simplestate_instantiation(instance):
    assert isinstance(instance, statechart_SimpleState)

@given(instance=statechart_FinalState_strategy)
@settings(max_examples=50)
def test_statechart_finalstate_instantiation(instance):
    assert isinstance(instance, statechart_FinalState)

@given(instance=statechart_CompositeState_strategy)
@settings(max_examples=50)
def test_statechart_compositestate_instantiation(instance):
    assert isinstance(instance, statechart_CompositeState)

@given(instance=statechart_Action_strategy)
@settings(max_examples=50)
def test_statechart_action_instantiation(instance):
    assert isinstance(instance, statechart_Action)



@given(instance=statechart_Action_strategy)
def test_statechart_action_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original
