import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    statechart::Variable,
    statechart::Transition,
    statechart::Node,
    statechart::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statechart::variable_is_not_abstract():
    assert not inspect.isabstract(statechart::Variable)


def test_statechart::variable_constructor_exists():
    assert callable(statechart::Variable.__init__)


def test_statechart::variable_constructor_args():
    sig = inspect.signature(statechart::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_statechart::variable_has_name():
    assert hasattr(statechart::Variable, "name")
    descriptor = None
    for klass in statechart::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_statechart::variable_has_type():
    assert hasattr(statechart::Variable, "type")
    descriptor = None
    for klass in statechart::Variable.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_statechart::transition_is_not_abstract():
    assert not inspect.isabstract(statechart::Transition)


def test_statechart::transition_constructor_exists():
    assert callable(statechart::Transition.__init__)


def test_statechart::transition_constructor_args():
    sig = inspect.signature(statechart::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "metadata" in params, "Missing parameter 'metadata'"
    assert "name" in params, "Missing parameter 'name'"
    assert "TE" in params, "Missing parameter 'TE'"

def test_statechart::transition_has_metadata():
    assert hasattr(statechart::Transition, "metadata")
    descriptor = None
    for klass in statechart::Transition.__mro__:
        if "metadata" in klass.__dict__:
            descriptor = klass.__dict__["metadata"]
            break
    assert isinstance(descriptor, property)

def test_statechart::transition_has_name():
    assert hasattr(statechart::Transition, "name")
    descriptor = None
    for klass in statechart::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_statechart::transition_has_TE():
    assert hasattr(statechart::Transition, "TE")
    descriptor = None
    for klass in statechart::Transition.__mro__:
        if "TE" in klass.__dict__:
            descriptor = klass.__dict__["TE"]
            break
    assert isinstance(descriptor, property)



def test_statechart::node_is_not_abstract():
    assert not inspect.isabstract(statechart::Node)


def test_statechart::node_constructor_exists():
    assert callable(statechart::Node.__init__)


def test_statechart::node_constructor_args():
    sig = inspect.signature(statechart::Node.__init__)
    params = list(sig.parameters.keys())
    assert "metadata" in params, "Missing parameter 'metadata'"
    assert "actions" in params, "Missing parameter 'actions'"
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"
    assert "label" in params, "Missing parameter 'label'"
    assert "activity" in params, "Missing parameter 'activity'"

def test_statechart::node_has_metadata():
    assert hasattr(statechart::Node, "metadata")
    descriptor = None
    for klass in statechart::Node.__mro__:
        if "metadata" in klass.__dict__:
            descriptor = klass.__dict__["metadata"]
            break
    assert isinstance(descriptor, property)

def test_statechart::node_has_actions():
    assert hasattr(statechart::Node, "actions")
    descriptor = None
    for klass in statechart::Node.__mro__:
        if "actions" in klass.__dict__:
            descriptor = klass.__dict__["actions"]
            break
    assert isinstance(descriptor, property)

def test_statechart::node_has_type():
    assert hasattr(statechart::Node, "type")
    descriptor = None
    for klass in statechart::Node.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_statechart::node_has_name():
    assert hasattr(statechart::Node, "name")
    descriptor = None
    for klass in statechart::Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_statechart::node_has_label():
    assert hasattr(statechart::Node, "label")
    descriptor = None
    for klass in statechart::Node.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_statechart::node_has_activity():
    assert hasattr(statechart::Node, "activity")
    descriptor = None
    for klass in statechart::Node.__mro__:
        if "activity" in klass.__dict__:
            descriptor = klass.__dict__["activity"]
            break
    assert isinstance(descriptor, property)



def test_statechart::model_is_not_abstract():
    assert not inspect.isabstract(statechart::Model)


def test_statechart::model_constructor_exists():
    assert callable(statechart::Model.__init__)


def test_statechart::model_constructor_args():
    sig = inspect.signature(statechart::Model.__init__)
    params = list(sig.parameters.keys())
    assert "metadata" in params, "Missing parameter 'metadata'"
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"

def test_statechart::model_has_metadata():
    assert hasattr(statechart::Model, "metadata")
    descriptor = None
    for klass in statechart::Model.__mro__:
        if "metadata" in klass.__dict__:
            descriptor = klass.__dict__["metadata"]
            break
    assert isinstance(descriptor, property)

def test_statechart::model_has_description():
    assert hasattr(statechart::Model, "description")
    descriptor = None
    for klass in statechart::Model.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_statechart::model_has_name():
    assert hasattr(statechart::Model, "name")
    descriptor = None
    for klass in statechart::Model.__mro__:
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
statechart::Variable_strategy = st.builds(
    statechart::Variable,
    name=
        safe_text,
    type=
        safe_text
)
statechart::Transition_strategy = st.builds(
    statechart::Transition,
    metadata=
        safe_text,
    name=
        safe_text,
    TE=
        safe_text
)
statechart::Node_strategy = st.builds(
    statechart::Node,
    metadata=
        safe_text,
    actions=
        safe_text,
    type=
        safe_text,
    name=
        safe_text,
    label=
        safe_text,
    activity=
        safe_text
)
statechart::Model_strategy = st.builds(
    statechart::Model,
    metadata=
        safe_text,
    description=
        safe_text,
    name=
        safe_text
)

@given(instance=statechart::Variable_strategy)
@settings(max_examples=50)
def test_statechart::variable_instantiation(instance):
    assert isinstance(instance, statechart::Variable)

@given(instance=statechart::Variable_strategy)
def test_statechart::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statechart::Variable_strategy)
def test_statechart::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statechart::Variable_strategy)
def test_statechart::variable_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=statechart::Variable_strategy)
def test_statechart::variable_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=statechart::Transition_strategy)
@settings(max_examples=50)
def test_statechart::transition_instantiation(instance):
    assert isinstance(instance, statechart::Transition)

@given(instance=statechart::Transition_strategy)
def test_statechart::transition_metadata_type(instance):
    assert isinstance(instance.metadata, str)


@given(instance=statechart::Transition_strategy)
def test_statechart::transition_metadata_setter(instance):
    original = instance.metadata
    instance.metadata = original
    assert instance.metadata == original

@given(instance=statechart::Transition_strategy)
def test_statechart::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statechart::Transition_strategy)
def test_statechart::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statechart::Transition_strategy)
def test_statechart::transition_TE_type(instance):
    assert isinstance(instance.TE, str)


@given(instance=statechart::Transition_strategy)
def test_statechart::transition_TE_setter(instance):
    original = instance.TE
    instance.TE = original
    assert instance.TE == original

@given(instance=statechart::Node_strategy)
@settings(max_examples=50)
def test_statechart::node_instantiation(instance):
    assert isinstance(instance, statechart::Node)

@given(instance=statechart::Node_strategy)
def test_statechart::node_metadata_type(instance):
    assert isinstance(instance.metadata, str)


@given(instance=statechart::Node_strategy)
def test_statechart::node_metadata_setter(instance):
    original = instance.metadata
    instance.metadata = original
    assert instance.metadata == original

@given(instance=statechart::Node_strategy)
def test_statechart::node_actions_type(instance):
    assert isinstance(instance.actions, str)


@given(instance=statechart::Node_strategy)
def test_statechart::node_actions_setter(instance):
    original = instance.actions
    instance.actions = original
    assert instance.actions == original

@given(instance=statechart::Node_strategy)
def test_statechart::node_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=statechart::Node_strategy)
def test_statechart::node_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=statechart::Node_strategy)
def test_statechart::node_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statechart::Node_strategy)
def test_statechart::node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statechart::Node_strategy)
def test_statechart::node_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=statechart::Node_strategy)
def test_statechart::node_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=statechart::Node_strategy)
def test_statechart::node_activity_type(instance):
    assert isinstance(instance.activity, str)


@given(instance=statechart::Node_strategy)
def test_statechart::node_activity_setter(instance):
    original = instance.activity
    instance.activity = original
    assert instance.activity == original

@given(instance=statechart::Model_strategy)
@settings(max_examples=50)
def test_statechart::model_instantiation(instance):
    assert isinstance(instance, statechart::Model)

@given(instance=statechart::Model_strategy)
def test_statechart::model_metadata_type(instance):
    assert isinstance(instance.metadata, str)


@given(instance=statechart::Model_strategy)
def test_statechart::model_metadata_setter(instance):
    original = instance.metadata
    instance.metadata = original
    assert instance.metadata == original

@given(instance=statechart::Model_strategy)
def test_statechart::model_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=statechart::Model_strategy)
def test_statechart::model_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=statechart::Model_strategy)
def test_statechart::model_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statechart::Model_strategy)
def test_statechart::model_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
