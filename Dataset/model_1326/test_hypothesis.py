import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Transition,
    state::TimeoutTransition,
    state::StateMachine,
    Node,
    state::ConditionalNode,
    state::FinalNode,
    state::State,
    state::InitialNode,
    state::Condition,
    state::Transition,
    state::Node,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_state::timeouttransition_is_not_abstract():
    assert not inspect.isabstract(state::TimeoutTransition)


def test_state::timeouttransition_constructor_exists():
    assert callable(state::TimeoutTransition.__init__)


def test_state::timeouttransition_constructor_args():
    sig = inspect.signature(state::TimeoutTransition.__init__)
    params = list(sig.parameters.keys())



def test_state::statemachine_is_not_abstract():
    assert not inspect.isabstract(state::StateMachine)


def test_state::statemachine_constructor_exists():
    assert callable(state::StateMachine.__init__)


def test_state::statemachine_constructor_args():
    sig = inspect.signature(state::StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_state::statemachine_has_name():
    assert hasattr(state::StateMachine, "name")
    descriptor = None
    for klass in state::StateMachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_state::conditionalnode_is_not_abstract():
    assert not inspect.isabstract(state::ConditionalNode)


def test_state::conditionalnode_constructor_exists():
    assert callable(state::ConditionalNode.__init__)


def test_state::conditionalnode_constructor_args():
    sig = inspect.signature(state::ConditionalNode.__init__)
    params = list(sig.parameters.keys())



def test_state::finalnode_is_not_abstract():
    assert not inspect.isabstract(state::FinalNode)


def test_state::finalnode_constructor_exists():
    assert callable(state::FinalNode.__init__)


def test_state::finalnode_constructor_args():
    sig = inspect.signature(state::FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_state::state_is_not_abstract():
    assert not inspect.isabstract(state::State)


def test_state::state_constructor_exists():
    assert callable(state::State.__init__)


def test_state::state_constructor_args():
    sig = inspect.signature(state::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "duration" in params, "Missing parameter 'duration'"

def test_state::state_has_name():
    assert hasattr(state::State, "name")
    descriptor = None
    for klass in state::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_state::state_has_duration():
    assert hasattr(state::State, "duration")
    descriptor = None
    for klass in state::State.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)



def test_state::initialnode_is_not_abstract():
    assert not inspect.isabstract(state::InitialNode)


def test_state::initialnode_constructor_exists():
    assert callable(state::InitialNode.__init__)


def test_state::initialnode_constructor_args():
    sig = inspect.signature(state::InitialNode.__init__)
    params = list(sig.parameters.keys())



def test_state::condition_is_not_abstract():
    assert not inspect.isabstract(state::Condition)


def test_state::condition_constructor_exists():
    assert callable(state::Condition.__init__)


def test_state::condition_constructor_args():
    sig = inspect.signature(state::Condition.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_state::condition_has_expression():
    assert hasattr(state::Condition, "expression")
    descriptor = None
    for klass in state::Condition.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_state::transition_is_not_abstract():
    assert not inspect.isabstract(state::Transition)


def test_state::transition_constructor_exists():
    assert callable(state::Transition.__init__)


def test_state::transition_constructor_args():
    sig = inspect.signature(state::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "triggerEventName" in params, "Missing parameter 'triggerEventName'"

def test_state::transition_has_triggerEventName():
    assert hasattr(state::Transition, "triggerEventName")
    descriptor = None
    for klass in state::Transition.__mro__:
        if "triggerEventName" in klass.__dict__:
            descriptor = klass.__dict__["triggerEventName"]
            break
    assert isinstance(descriptor, property)



def test_state::node_is_not_abstract():
    assert not inspect.isabstract(state::Node)


def test_state::node_constructor_exists():
    assert callable(state::Node.__init__)


def test_state::node_constructor_args():
    sig = inspect.signature(state::Node.__init__)
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
Transition_strategy = st.builds(
    Transition,
)
state::TimeoutTransition_strategy = st.builds(
    state::TimeoutTransition,
)
state::StateMachine_strategy = st.builds(
    state::StateMachine,
    name=
        safe_text
)
Node_strategy = st.builds(
    Node,
)
state::ConditionalNode_strategy = st.builds(
    state::ConditionalNode,
)
state::FinalNode_strategy = st.builds(
    state::FinalNode,
)
state::State_strategy = st.builds(
    state::State,
    name=
        safe_text,
    duration=
        safe_text
)
state::InitialNode_strategy = st.builds(
    state::InitialNode,
)
state::Condition_strategy = st.builds(
    state::Condition,
    expression=
        safe_text
)
state::Transition_strategy = st.builds(
    state::Transition,
    triggerEventName=
        safe_text
)
state::Node_strategy = st.builds(
    state::Node,
)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=state::TimeoutTransition_strategy)
@settings(max_examples=50)
def test_state::timeouttransition_instantiation(instance):
    assert isinstance(instance, state::TimeoutTransition)

@given(instance=state::StateMachine_strategy)
@settings(max_examples=50)
def test_state::statemachine_instantiation(instance):
    assert isinstance(instance, state::StateMachine)

@given(instance=state::StateMachine_strategy)
def test_state::statemachine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=state::StateMachine_strategy)
def test_state::statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=state::ConditionalNode_strategy)
@settings(max_examples=50)
def test_state::conditionalnode_instantiation(instance):
    assert isinstance(instance, state::ConditionalNode)

@given(instance=state::FinalNode_strategy)
@settings(max_examples=50)
def test_state::finalnode_instantiation(instance):
    assert isinstance(instance, state::FinalNode)

@given(instance=state::State_strategy)
@settings(max_examples=50)
def test_state::state_instantiation(instance):
    assert isinstance(instance, state::State)

@given(instance=state::State_strategy)
def test_state::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=state::State_strategy)
def test_state::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=state::State_strategy)
def test_state::state_duration_type(instance):
    assert isinstance(instance.duration, str)


@given(instance=state::State_strategy)
def test_state::state_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original

@given(instance=state::InitialNode_strategy)
@settings(max_examples=50)
def test_state::initialnode_instantiation(instance):
    assert isinstance(instance, state::InitialNode)

@given(instance=state::Condition_strategy)
@settings(max_examples=50)
def test_state::condition_instantiation(instance):
    assert isinstance(instance, state::Condition)

@given(instance=state::Condition_strategy)
def test_state::condition_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=state::Condition_strategy)
def test_state::condition_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=state::Transition_strategy)
@settings(max_examples=50)
def test_state::transition_instantiation(instance):
    assert isinstance(instance, state::Transition)

@given(instance=state::Transition_strategy)
def test_state::transition_triggerEventName_type(instance):
    assert isinstance(instance.triggerEventName, str)


@given(instance=state::Transition_strategy)
def test_state::transition_triggerEventName_setter(instance):
    original = instance.triggerEventName
    instance.triggerEventName = original
    assert instance.triggerEventName == original

@given(instance=state::Node_strategy)
@settings(max_examples=50)
def test_state::node_instantiation(instance):
    assert isinstance(instance, state::Node)
