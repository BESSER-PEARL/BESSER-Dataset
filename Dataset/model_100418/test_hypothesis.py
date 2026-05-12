import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    statechart_Variable,
    statechart_Transition,
    statechart_Node,
    statechart_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statechart_variable_is_not_abstract():
    assert not inspect.isabstract(statechart_Variable)


def test_statechart_variable_constructor_exists():
    assert callable(statechart_Variable.__init__)


def test_statechart_variable_constructor_args():
    sig = inspect.signature(statechart_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_statechart_variable_has_name():
    assert hasattr(statechart_Variable, "name")
    descriptor = None
    for klass in statechart_Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_statechart_variable_has_type():
    assert hasattr(statechart_Variable, "type")
    descriptor = None
    for klass in statechart_Variable.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_statechart_transition_is_not_abstract():
    assert not inspect.isabstract(statechart_Transition)


def test_statechart_transition_constructor_exists():
    assert callable(statechart_Transition.__init__)


def test_statechart_transition_constructor_args():
    sig = inspect.signature(statechart_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "TE" in params, "Missing parameter 'TE'"
    assert "name" in params, "Missing parameter 'name'"

def test_statechart_transition_has_TE():
    assert hasattr(statechart_Transition, "TE")
    descriptor = None
    for klass in statechart_Transition.__mro__:
        if "TE" in klass.__dict__:
            descriptor = klass.__dict__["TE"]
            break
    assert isinstance(descriptor, property)

def test_statechart_transition_has_name():
    assert hasattr(statechart_Transition, "name")
    descriptor = None
    for klass in statechart_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statechart_node_is_not_abstract():
    assert not inspect.isabstract(statechart_Node)


def test_statechart_node_constructor_exists():
    assert callable(statechart_Node.__init__)


def test_statechart_node_constructor_args():
    sig = inspect.signature(statechart_Node.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "label" in params, "Missing parameter 'label'"
    assert "activity" in params, "Missing parameter 'activity'"
    assert "name" in params, "Missing parameter 'name'"

def test_statechart_node_has_type():
    assert hasattr(statechart_Node, "type")
    descriptor = None
    for klass in statechart_Node.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_statechart_node_has_label():
    assert hasattr(statechart_Node, "label")
    descriptor = None
    for klass in statechart_Node.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_statechart_node_has_activity():
    assert hasattr(statechart_Node, "activity")
    descriptor = None
    for klass in statechart_Node.__mro__:
        if "activity" in klass.__dict__:
            descriptor = klass.__dict__["activity"]
            break
    assert isinstance(descriptor, property)

def test_statechart_node_has_name():
    assert hasattr(statechart_Node, "name")
    descriptor = None
    for klass in statechart_Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statechart_model_is_not_abstract():
    assert not inspect.isabstract(statechart_Model)


def test_statechart_model_constructor_exists():
    assert callable(statechart_Model.__init__)


def test_statechart_model_constructor_args():
    sig = inspect.signature(statechart_Model.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statechart_model_has_name():
    assert hasattr(statechart_Model, "name")
    descriptor = None
    for klass in statechart_Model.__mro__:
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
statechart_Variable_strategy = st.builds(
    statechart_Variable,
    name=
        safe_text,
    type=
        safe_text
)
statechart_Transition_strategy = st.builds(
    statechart_Transition,
    TE=
        safe_text,
    name=
        safe_text
)
statechart_Node_strategy = st.builds(
    statechart_Node,
    type=
        safe_text,
    label=
        safe_text,
    activity=
        safe_text,
    name=
        safe_text
)
statechart_Model_strategy = st.builds(
    statechart_Model,
    name=
        safe_text
)

@given(instance=statechart_Variable_strategy)
@settings(max_examples=50)
def test_statechart_variable_instantiation(instance):
    assert isinstance(instance, statechart_Variable)



@given(instance=statechart_Variable_strategy)
def test_statechart_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=statechart_Variable_strategy)
def test_statechart_variable_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=statechart_Transition_strategy)
@settings(max_examples=50)
def test_statechart_transition_instantiation(instance):
    assert isinstance(instance, statechart_Transition)



@given(instance=statechart_Transition_strategy)
def test_statechart_transition_TE_setter(instance):
    original = instance.TE
    instance.TE = original
    assert instance.TE == original



@given(instance=statechart_Transition_strategy)
def test_statechart_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statechart_Node_strategy)
@settings(max_examples=50)
def test_statechart_node_instantiation(instance):
    assert isinstance(instance, statechart_Node)



@given(instance=statechart_Node_strategy)
def test_statechart_node_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=statechart_Node_strategy)
def test_statechart_node_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=statechart_Node_strategy)
def test_statechart_node_activity_setter(instance):
    original = instance.activity
    instance.activity = original
    assert instance.activity == original



@given(instance=statechart_Node_strategy)
def test_statechart_node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statechart_Model_strategy)
@settings(max_examples=50)
def test_statechart_model_instantiation(instance):
    assert isinstance(instance, statechart_Model)



@given(instance=statechart_Model_strategy)
def test_statechart_model_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
