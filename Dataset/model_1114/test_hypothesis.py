import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    stateChart_Node,
    stateChart_Model,
    stateChart_Transition,
    stateChart_Variable,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statechart_node_is_not_abstract():
    assert not inspect.isabstract(stateChart_Node)


def test_statechart_node_constructor_exists():
    assert callable(stateChart_Node.__init__)


def test_statechart_node_constructor_args():
    sig = inspect.signature(stateChart_Node.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "activity" in params, "Missing parameter 'activity'"
    assert "metadata" in params, "Missing parameter 'metadata'"
    assert "type" in params, "Missing parameter 'type'"
    assert "actions" in params, "Missing parameter 'actions'"
    assert "name" in params, "Missing parameter 'name'"

def test_statechart_node_has_label():
    assert hasattr(stateChart_Node, "label")
    descriptor = None
    for klass in stateChart_Node.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_statechart_node_has_activity():
    assert hasattr(stateChart_Node, "activity")
    descriptor = None
    for klass in stateChart_Node.__mro__:
        if "activity" in klass.__dict__:
            descriptor = klass.__dict__["activity"]
            break
    assert isinstance(descriptor, property)

def test_statechart_node_has_metadata():
    assert hasattr(stateChart_Node, "metadata")
    descriptor = None
    for klass in stateChart_Node.__mro__:
        if "metadata" in klass.__dict__:
            descriptor = klass.__dict__["metadata"]
            break
    assert isinstance(descriptor, property)

def test_statechart_node_has_type():
    assert hasattr(stateChart_Node, "type")
    descriptor = None
    for klass in stateChart_Node.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_statechart_node_has_actions():
    assert hasattr(stateChart_Node, "actions")
    descriptor = None
    for klass in stateChart_Node.__mro__:
        if "actions" in klass.__dict__:
            descriptor = klass.__dict__["actions"]
            break
    assert isinstance(descriptor, property)

def test_statechart_node_has_name():
    assert hasattr(stateChart_Node, "name")
    descriptor = None
    for klass in stateChart_Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statechart_model_is_not_abstract():
    assert not inspect.isabstract(stateChart_Model)


def test_statechart_model_constructor_exists():
    assert callable(stateChart_Model.__init__)


def test_statechart_model_constructor_args():
    sig = inspect.signature(stateChart_Model.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "metadata" in params, "Missing parameter 'metadata'"
    assert "description" in params, "Missing parameter 'description'"

def test_statechart_model_has_name():
    assert hasattr(stateChart_Model, "name")
    descriptor = None
    for klass in stateChart_Model.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_statechart_model_has_metadata():
    assert hasattr(stateChart_Model, "metadata")
    descriptor = None
    for klass in stateChart_Model.__mro__:
        if "metadata" in klass.__dict__:
            descriptor = klass.__dict__["metadata"]
            break
    assert isinstance(descriptor, property)

def test_statechart_model_has_description():
    assert hasattr(stateChart_Model, "description")
    descriptor = None
    for klass in stateChart_Model.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_statechart_transition_is_not_abstract():
    assert not inspect.isabstract(stateChart_Transition)


def test_statechart_transition_constructor_exists():
    assert callable(stateChart_Transition.__init__)


def test_statechart_transition_constructor_args():
    sig = inspect.signature(stateChart_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "metadata" in params, "Missing parameter 'metadata'"
    assert "TE" in params, "Missing parameter 'TE'"
    assert "name" in params, "Missing parameter 'name'"

def test_statechart_transition_has_metadata():
    assert hasattr(stateChart_Transition, "metadata")
    descriptor = None
    for klass in stateChart_Transition.__mro__:
        if "metadata" in klass.__dict__:
            descriptor = klass.__dict__["metadata"]
            break
    assert isinstance(descriptor, property)

def test_statechart_transition_has_TE():
    assert hasattr(stateChart_Transition, "TE")
    descriptor = None
    for klass in stateChart_Transition.__mro__:
        if "TE" in klass.__dict__:
            descriptor = klass.__dict__["TE"]
            break
    assert isinstance(descriptor, property)

def test_statechart_transition_has_name():
    assert hasattr(stateChart_Transition, "name")
    descriptor = None
    for klass in stateChart_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statechart_variable_is_not_abstract():
    assert not inspect.isabstract(stateChart_Variable)


def test_statechart_variable_constructor_exists():
    assert callable(stateChart_Variable.__init__)


def test_statechart_variable_constructor_args():
    sig = inspect.signature(stateChart_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_statechart_variable_has_type():
    assert hasattr(stateChart_Variable, "type")
    descriptor = None
    for klass in stateChart_Variable.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_statechart_variable_has_name():
    assert hasattr(stateChart_Variable, "name")
    descriptor = None
    for klass in stateChart_Variable.__mro__:
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
stateChart_Node_strategy = st.builds(
    stateChart_Node,
    label=
        safe_text,
    activity=
        safe_text,
    metadata=
        safe_text,
    type=
        safe_text,
    actions=
        safe_text,
    name=
        safe_text
)
stateChart_Model_strategy = st.builds(
    stateChart_Model,
    name=
        safe_text,
    metadata=
        safe_text,
    description=
        safe_text
)
stateChart_Transition_strategy = st.builds(
    stateChart_Transition,
    metadata=
        safe_text,
    TE=
        safe_text,
    name=
        safe_text
)
stateChart_Variable_strategy = st.builds(
    stateChart_Variable,
    type=
        safe_text,
    name=
        safe_text
)

@given(instance=stateChart_Node_strategy)
@settings(max_examples=50)
def test_statechart_node_instantiation(instance):
    assert isinstance(instance, stateChart_Node)



@given(instance=stateChart_Node_strategy)
def test_statechart_node_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=stateChart_Node_strategy)
def test_statechart_node_activity_setter(instance):
    original = instance.activity
    instance.activity = original
    assert instance.activity == original



@given(instance=stateChart_Node_strategy)
def test_statechart_node_metadata_setter(instance):
    original = instance.metadata
    instance.metadata = original
    assert instance.metadata == original



@given(instance=stateChart_Node_strategy)
def test_statechart_node_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=stateChart_Node_strategy)
def test_statechart_node_actions_setter(instance):
    original = instance.actions
    instance.actions = original
    assert instance.actions == original



@given(instance=stateChart_Node_strategy)
def test_statechart_node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stateChart_Model_strategy)
@settings(max_examples=50)
def test_statechart_model_instantiation(instance):
    assert isinstance(instance, stateChart_Model)



@given(instance=stateChart_Model_strategy)
def test_statechart_model_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=stateChart_Model_strategy)
def test_statechart_model_metadata_setter(instance):
    original = instance.metadata
    instance.metadata = original
    assert instance.metadata == original



@given(instance=stateChart_Model_strategy)
def test_statechart_model_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=stateChart_Transition_strategy)
@settings(max_examples=50)
def test_statechart_transition_instantiation(instance):
    assert isinstance(instance, stateChart_Transition)



@given(instance=stateChart_Transition_strategy)
def test_statechart_transition_metadata_setter(instance):
    original = instance.metadata
    instance.metadata = original
    assert instance.metadata == original



@given(instance=stateChart_Transition_strategy)
def test_statechart_transition_TE_setter(instance):
    original = instance.TE
    instance.TE = original
    assert instance.TE == original



@given(instance=stateChart_Transition_strategy)
def test_statechart_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stateChart_Variable_strategy)
@settings(max_examples=50)
def test_statechart_variable_instantiation(instance):
    assert isinstance(instance, stateChart_Variable)



@given(instance=stateChart_Variable_strategy)
def test_statechart_variable_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=stateChart_Variable_strategy)
def test_statechart_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
