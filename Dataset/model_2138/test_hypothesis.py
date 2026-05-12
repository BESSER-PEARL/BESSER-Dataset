import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    flowchart_Decision,
    flowchart_Action,
    flowchart_Transition,
    flowchart_Node,
    flowchart_Flowchart,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_flowchart_decision_is_not_abstract():
    assert not inspect.isabstract(flowchart_Decision)


def test_flowchart_decision_constructor_exists():
    assert callable(flowchart_Decision.__init__)


def test_flowchart_decision_constructor_args():
    sig = inspect.signature(flowchart_Decision.__init__)
    params = list(sig.parameters.keys())
    assert "isDecision" in params, "Missing parameter 'isDecision'"
    assert "condition" in params, "Missing parameter 'condition'"

def test_flowchart_decision_has_isDecision():
    assert hasattr(flowchart_Decision, "isDecision")
    descriptor = None
    for klass in flowchart_Decision.__mro__:
        if "isDecision" in klass.__dict__:
            descriptor = klass.__dict__["isDecision"]
            break
    assert isinstance(descriptor, property)

def test_flowchart_decision_has_condition():
    assert hasattr(flowchart_Decision, "condition")
    descriptor = None
    for klass in flowchart_Decision.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)



def test_flowchart_action_is_not_abstract():
    assert not inspect.isabstract(flowchart_Action)


def test_flowchart_action_constructor_exists():
    assert callable(flowchart_Action.__init__)


def test_flowchart_action_constructor_args():
    sig = inspect.signature(flowchart_Action.__init__)
    params = list(sig.parameters.keys())
    assert "isAction" in params, "Missing parameter 'isAction'"

def test_flowchart_action_has_isAction():
    assert hasattr(flowchart_Action, "isAction")
    descriptor = None
    for klass in flowchart_Action.__mro__:
        if "isAction" in klass.__dict__:
            descriptor = klass.__dict__["isAction"]
            break
    assert isinstance(descriptor, property)



def test_flowchart_transition_is_not_abstract():
    assert not inspect.isabstract(flowchart_Transition)


def test_flowchart_transition_constructor_exists():
    assert callable(flowchart_Transition.__init__)


def test_flowchart_transition_constructor_args():
    sig = inspect.signature(flowchart_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_flowchart_transition_has_label():
    assert hasattr(flowchart_Transition, "label")
    descriptor = None
    for klass in flowchart_Transition.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_flowchart_node_is_not_abstract():
    assert not inspect.isabstract(flowchart_Node)


def test_flowchart_node_constructor_exists():
    assert callable(flowchart_Node.__init__)


def test_flowchart_node_constructor_args():
    sig = inspect.signature(flowchart_Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_flowchart_node_has_name():
    assert hasattr(flowchart_Node, "name")
    descriptor = None
    for klass in flowchart_Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_flowchart_flowchart_is_not_abstract():
    assert not inspect.isabstract(flowchart_Flowchart)


def test_flowchart_flowchart_constructor_exists():
    assert callable(flowchart_Flowchart.__init__)


def test_flowchart_flowchart_constructor_args():
    sig = inspect.signature(flowchart_Flowchart.__init__)
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
flowchart_Decision_strategy = st.builds(
    flowchart_Decision,
    isDecision=
        st.booleans(),
    condition=
        safe_text
)
flowchart_Action_strategy = st.builds(
    flowchart_Action,
    isAction=
        st.booleans()
)
flowchart_Transition_strategy = st.builds(
    flowchart_Transition,
    label=
        safe_text
)
flowchart_Node_strategy = st.builds(
    flowchart_Node,
    name=
        safe_text
)
flowchart_Flowchart_strategy = st.builds(
    flowchart_Flowchart,
)

@given(instance=flowchart_Decision_strategy)
@settings(max_examples=50)
def test_flowchart_decision_instantiation(instance):
    assert isinstance(instance, flowchart_Decision)



@given(instance=flowchart_Decision_strategy)
def test_flowchart_decision_isDecision_setter(instance):
    original = instance.isDecision
    instance.isDecision = original
    assert instance.isDecision == original



@given(instance=flowchart_Decision_strategy)
def test_flowchart_decision_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original

@given(instance=flowchart_Action_strategy)
@settings(max_examples=50)
def test_flowchart_action_instantiation(instance):
    assert isinstance(instance, flowchart_Action)



@given(instance=flowchart_Action_strategy)
def test_flowchart_action_isAction_setter(instance):
    original = instance.isAction
    instance.isAction = original
    assert instance.isAction == original

@given(instance=flowchart_Transition_strategy)
@settings(max_examples=50)
def test_flowchart_transition_instantiation(instance):
    assert isinstance(instance, flowchart_Transition)



@given(instance=flowchart_Transition_strategy)
def test_flowchart_transition_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=flowchart_Node_strategy)
@settings(max_examples=50)
def test_flowchart_node_instantiation(instance):
    assert isinstance(instance, flowchart_Node)



@given(instance=flowchart_Node_strategy)
def test_flowchart_node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=flowchart_Flowchart_strategy)
@settings(max_examples=50)
def test_flowchart_flowchart_instantiation(instance):
    assert isinstance(instance, flowchart_Flowchart)
