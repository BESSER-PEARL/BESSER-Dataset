import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    stateChart::Node,
    stateChart::Model,
    stateChart::Transition,
    stateChart::Variable,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statechart::node_is_not_abstract():
    assert not inspect.isabstract(stateChart::Node)


def test_statechart::node_constructor_exists():
    assert callable(stateChart::Node.__init__)


def test_statechart::node_constructor_args():
    sig = inspect.signature(stateChart::Node.__init__)
    params = list(sig.parameters.keys())
    assert "actions" in params, "Missing parameter 'actions'"
    assert "label" in params, "Missing parameter 'label'"
    assert "name" in params, "Missing parameter 'name'"
    assert "activity" in params, "Missing parameter 'activity'"
    assert "type" in params, "Missing parameter 'type'"
    assert "metadata" in params, "Missing parameter 'metadata'"

def test_statechart::node_has_actions():
    assert hasattr(stateChart::Node, "actions")
    descriptor = None
    for klass in stateChart::Node.__mro__:
        if "actions" in klass.__dict__:
            descriptor = klass.__dict__["actions"]
            break
    assert isinstance(descriptor, property)

def test_statechart::node_has_label():
    assert hasattr(stateChart::Node, "label")
    descriptor = None
    for klass in stateChart::Node.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_statechart::node_has_name():
    assert hasattr(stateChart::Node, "name")
    descriptor = None
    for klass in stateChart::Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_statechart::node_has_activity():
    assert hasattr(stateChart::Node, "activity")
    descriptor = None
    for klass in stateChart::Node.__mro__:
        if "activity" in klass.__dict__:
            descriptor = klass.__dict__["activity"]
            break
    assert isinstance(descriptor, property)

def test_statechart::node_has_type():
    assert hasattr(stateChart::Node, "type")
    descriptor = None
    for klass in stateChart::Node.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_statechart::node_has_metadata():
    assert hasattr(stateChart::Node, "metadata")
    descriptor = None
    for klass in stateChart::Node.__mro__:
        if "metadata" in klass.__dict__:
            descriptor = klass.__dict__["metadata"]
            break
    assert isinstance(descriptor, property)



def test_statechart::model_is_not_abstract():
    assert not inspect.isabstract(stateChart::Model)


def test_statechart::model_constructor_exists():
    assert callable(stateChart::Model.__init__)


def test_statechart::model_constructor_args():
    sig = inspect.signature(stateChart::Model.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "metadata" in params, "Missing parameter 'metadata'"
    assert "description" in params, "Missing parameter 'description'"

def test_statechart::model_has_name():
    assert hasattr(stateChart::Model, "name")
    descriptor = None
    for klass in stateChart::Model.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_statechart::model_has_metadata():
    assert hasattr(stateChart::Model, "metadata")
    descriptor = None
    for klass in stateChart::Model.__mro__:
        if "metadata" in klass.__dict__:
            descriptor = klass.__dict__["metadata"]
            break
    assert isinstance(descriptor, property)

def test_statechart::model_has_description():
    assert hasattr(stateChart::Model, "description")
    descriptor = None
    for klass in stateChart::Model.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_statechart::transition_is_not_abstract():
    assert not inspect.isabstract(stateChart::Transition)


def test_statechart::transition_constructor_exists():
    assert callable(stateChart::Transition.__init__)


def test_statechart::transition_constructor_args():
    sig = inspect.signature(stateChart::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "TE" in params, "Missing parameter 'TE'"
    assert "name" in params, "Missing parameter 'name'"
    assert "metadata" in params, "Missing parameter 'metadata'"

def test_statechart::transition_has_TE():
    assert hasattr(stateChart::Transition, "TE")
    descriptor = None
    for klass in stateChart::Transition.__mro__:
        if "TE" in klass.__dict__:
            descriptor = klass.__dict__["TE"]
            break
    assert isinstance(descriptor, property)

def test_statechart::transition_has_name():
    assert hasattr(stateChart::Transition, "name")
    descriptor = None
    for klass in stateChart::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_statechart::transition_has_metadata():
    assert hasattr(stateChart::Transition, "metadata")
    descriptor = None
    for klass in stateChart::Transition.__mro__:
        if "metadata" in klass.__dict__:
            descriptor = klass.__dict__["metadata"]
            break
    assert isinstance(descriptor, property)



def test_statechart::variable_is_not_abstract():
    assert not inspect.isabstract(stateChart::Variable)


def test_statechart::variable_constructor_exists():
    assert callable(stateChart::Variable.__init__)


def test_statechart::variable_constructor_args():
    sig = inspect.signature(stateChart::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_statechart::variable_has_name():
    assert hasattr(stateChart::Variable, "name")
    descriptor = None
    for klass in stateChart::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_statechart::variable_has_type():
    assert hasattr(stateChart::Variable, "type")
    descriptor = None
    for klass in stateChart::Variable.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
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
stateChart::Node_strategy = st.builds(
    stateChart::Node,
    actions=
        safe_text,
    label=
        safe_text,
    name=
        safe_text,
    activity=
        safe_text,
    type=
        safe_text,
    metadata=
        safe_text
)
stateChart::Model_strategy = st.builds(
    stateChart::Model,
    name=
        safe_text,
    metadata=
        safe_text,
    description=
        safe_text
)
stateChart::Transition_strategy = st.builds(
    stateChart::Transition,
    TE=
        safe_text,
    name=
        safe_text,
    metadata=
        safe_text
)
stateChart::Variable_strategy = st.builds(
    stateChart::Variable,
    name=
        safe_text,
    type=
        safe_text
)

@given(instance=stateChart::Node_strategy)
@settings(max_examples=50)
def test_statechart::node_instantiation(instance):
    assert isinstance(instance, stateChart::Node)

@given(instance=stateChart::Node_strategy)
def test_statechart::node_actions_type(instance):
    assert isinstance(instance.actions, str)


@given(instance=stateChart::Node_strategy)
def test_statechart::node_actions_setter(instance):
    original = instance.actions
    instance.actions = original
    assert instance.actions == original

@given(instance=stateChart::Node_strategy)
def test_statechart::node_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=stateChart::Node_strategy)
def test_statechart::node_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=stateChart::Node_strategy)
def test_statechart::node_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=stateChart::Node_strategy)
def test_statechart::node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stateChart::Node_strategy)
def test_statechart::node_activity_type(instance):
    assert isinstance(instance.activity, str)


@given(instance=stateChart::Node_strategy)
def test_statechart::node_activity_setter(instance):
    original = instance.activity
    instance.activity = original
    assert instance.activity == original

@given(instance=stateChart::Node_strategy)
def test_statechart::node_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=stateChart::Node_strategy)
def test_statechart::node_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=stateChart::Node_strategy)
def test_statechart::node_metadata_type(instance):
    assert isinstance(instance.metadata, str)


@given(instance=stateChart::Node_strategy)
def test_statechart::node_metadata_setter(instance):
    original = instance.metadata
    instance.metadata = original
    assert instance.metadata == original

@given(instance=stateChart::Model_strategy)
@settings(max_examples=50)
def test_statechart::model_instantiation(instance):
    assert isinstance(instance, stateChart::Model)

@given(instance=stateChart::Model_strategy)
def test_statechart::model_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=stateChart::Model_strategy)
def test_statechart::model_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stateChart::Model_strategy)
def test_statechart::model_metadata_type(instance):
    assert isinstance(instance.metadata, str)


@given(instance=stateChart::Model_strategy)
def test_statechart::model_metadata_setter(instance):
    original = instance.metadata
    instance.metadata = original
    assert instance.metadata == original

@given(instance=stateChart::Model_strategy)
def test_statechart::model_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=stateChart::Model_strategy)
def test_statechart::model_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=stateChart::Transition_strategy)
@settings(max_examples=50)
def test_statechart::transition_instantiation(instance):
    assert isinstance(instance, stateChart::Transition)

@given(instance=stateChart::Transition_strategy)
def test_statechart::transition_TE_type(instance):
    assert isinstance(instance.TE, str)


@given(instance=stateChart::Transition_strategy)
def test_statechart::transition_TE_setter(instance):
    original = instance.TE
    instance.TE = original
    assert instance.TE == original

@given(instance=stateChart::Transition_strategy)
def test_statechart::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=stateChart::Transition_strategy)
def test_statechart::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stateChart::Transition_strategy)
def test_statechart::transition_metadata_type(instance):
    assert isinstance(instance.metadata, str)


@given(instance=stateChart::Transition_strategy)
def test_statechart::transition_metadata_setter(instance):
    original = instance.metadata
    instance.metadata = original
    assert instance.metadata == original

@given(instance=stateChart::Variable_strategy)
@settings(max_examples=50)
def test_statechart::variable_instantiation(instance):
    assert isinstance(instance, stateChart::Variable)

@given(instance=stateChart::Variable_strategy)
def test_statechart::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=stateChart::Variable_strategy)
def test_statechart::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stateChart::Variable_strategy)
def test_statechart::variable_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=stateChart::Variable_strategy)
def test_statechart::variable_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original
