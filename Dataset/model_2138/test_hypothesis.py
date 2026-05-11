import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    flowchart::Decision,
    flowchart::Action,
    flowchart::Transition,
    flowchart::Node,
    flowchart::Flowchart,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_flowchart::decision_is_not_abstract():
    assert not inspect.isabstract(flowchart::Decision)


def test_flowchart::decision_constructor_exists():
    assert callable(flowchart::Decision.__init__)


def test_flowchart::decision_constructor_args():
    sig = inspect.signature(flowchart::Decision.__init__)
    params = list(sig.parameters.keys())
    assert "condition" in params, "Missing parameter 'condition'"
    assert "isDecision" in params, "Missing parameter 'isDecision'"

def test_flowchart::decision_has_condition():
    assert hasattr(flowchart::Decision, "condition")
    descriptor = None
    for klass in flowchart::Decision.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)

def test_flowchart::decision_has_isDecision():
    assert hasattr(flowchart::Decision, "isDecision")
    descriptor = None
    for klass in flowchart::Decision.__mro__:
        if "isDecision" in klass.__dict__:
            descriptor = klass.__dict__["isDecision"]
            break
    assert isinstance(descriptor, property)



def test_flowchart::action_is_not_abstract():
    assert not inspect.isabstract(flowchart::Action)


def test_flowchart::action_constructor_exists():
    assert callable(flowchart::Action.__init__)


def test_flowchart::action_constructor_args():
    sig = inspect.signature(flowchart::Action.__init__)
    params = list(sig.parameters.keys())
    assert "isAction" in params, "Missing parameter 'isAction'"

def test_flowchart::action_has_isAction():
    assert hasattr(flowchart::Action, "isAction")
    descriptor = None
    for klass in flowchart::Action.__mro__:
        if "isAction" in klass.__dict__:
            descriptor = klass.__dict__["isAction"]
            break
    assert isinstance(descriptor, property)



def test_flowchart::transition_is_not_abstract():
    assert not inspect.isabstract(flowchart::Transition)


def test_flowchart::transition_constructor_exists():
    assert callable(flowchart::Transition.__init__)


def test_flowchart::transition_constructor_args():
    sig = inspect.signature(flowchart::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_flowchart::transition_has_label():
    assert hasattr(flowchart::Transition, "label")
    descriptor = None
    for klass in flowchart::Transition.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_flowchart::node_is_not_abstract():
    assert not inspect.isabstract(flowchart::Node)


def test_flowchart::node_constructor_exists():
    assert callable(flowchart::Node.__init__)


def test_flowchart::node_constructor_args():
    sig = inspect.signature(flowchart::Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_flowchart::node_has_name():
    assert hasattr(flowchart::Node, "name")
    descriptor = None
    for klass in flowchart::Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_flowchart::flowchart_is_not_abstract():
    assert not inspect.isabstract(flowchart::Flowchart)


def test_flowchart::flowchart_constructor_exists():
    assert callable(flowchart::Flowchart.__init__)


def test_flowchart::flowchart_constructor_args():
    sig = inspect.signature(flowchart::Flowchart.__init__)
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
flowchart::Decision_strategy = st.builds(
    flowchart::Decision,
    condition=
        safe_text,
    isDecision=
        st.booleans()
)
flowchart::Action_strategy = st.builds(
    flowchart::Action,
    isAction=
        st.booleans()
)
flowchart::Transition_strategy = st.builds(
    flowchart::Transition,
    label=
        safe_text
)
flowchart::Node_strategy = st.builds(
    flowchart::Node,
    name=
        safe_text
)
flowchart::Flowchart_strategy = st.builds(
    flowchart::Flowchart,
)

@given(instance=flowchart::Decision_strategy)
@settings(max_examples=50)
def test_flowchart::decision_instantiation(instance):
    assert isinstance(instance, flowchart::Decision)

@given(instance=flowchart::Decision_strategy)
def test_flowchart::decision_condition_type(instance):
    assert isinstance(instance.condition, str)


@given(instance=flowchart::Decision_strategy)
def test_flowchart::decision_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original

@given(instance=flowchart::Decision_strategy)
def test_flowchart::decision_isDecision_type(instance):
    assert isinstance(instance.isDecision, bool)


@given(instance=flowchart::Decision_strategy)
def test_flowchart::decision_isDecision_setter(instance):
    original = instance.isDecision
    instance.isDecision = original
    assert instance.isDecision == original

@given(instance=flowchart::Action_strategy)
@settings(max_examples=50)
def test_flowchart::action_instantiation(instance):
    assert isinstance(instance, flowchart::Action)

@given(instance=flowchart::Action_strategy)
def test_flowchart::action_isAction_type(instance):
    assert isinstance(instance.isAction, bool)


@given(instance=flowchart::Action_strategy)
def test_flowchart::action_isAction_setter(instance):
    original = instance.isAction
    instance.isAction = original
    assert instance.isAction == original

@given(instance=flowchart::Transition_strategy)
@settings(max_examples=50)
def test_flowchart::transition_instantiation(instance):
    assert isinstance(instance, flowchart::Transition)

@given(instance=flowchart::Transition_strategy)
def test_flowchart::transition_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=flowchart::Transition_strategy)
def test_flowchart::transition_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=flowchart::Node_strategy)
@settings(max_examples=50)
def test_flowchart::node_instantiation(instance):
    assert isinstance(instance, flowchart::Node)

@given(instance=flowchart::Node_strategy)
def test_flowchart::node_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=flowchart::Node_strategy)
def test_flowchart::node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=flowchart::Flowchart_strategy)
@settings(max_examples=50)
def test_flowchart::flowchart_instantiation(instance):
    assert isinstance(instance, flowchart::Flowchart)
