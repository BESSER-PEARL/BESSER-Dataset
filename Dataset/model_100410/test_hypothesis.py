import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Thing,
    simplestatechart::Variable,
    NamedElement,
    simplestatechart::Transition,
    simplestatechart::State,
    simplestatechart::Thing,
    simplestatechart::NamedElement,
    simplestatechart::RelatedTo,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_thing_is_not_abstract():
    assert not inspect.isabstract(Thing)


def test_thing_constructor_exists():
    assert callable(Thing.__init__)


def test_thing_constructor_args():
    sig = inspect.signature(Thing.__init__)
    params = list(sig.parameters.keys())



def test_simplestatechart::variable_is_not_abstract():
    assert not inspect.isabstract(simplestatechart::Variable)


def test_simplestatechart::variable_constructor_exists():
    assert callable(simplestatechart::Variable.__init__)


def test_simplestatechart::variable_constructor_args():
    sig = inspect.signature(simplestatechart::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "value" in params, "Missing parameter 'value'"

def test_simplestatechart::variable_has_type():
    assert hasattr(simplestatechart::Variable, "type")
    descriptor = None
    for klass in simplestatechart::Variable.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_simplestatechart::variable_has_value():
    assert hasattr(simplestatechart::Variable, "value")
    descriptor = None
    for klass in simplestatechart::Variable.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_simplestatechart::transition_is_not_abstract():
    assert not inspect.isabstract(simplestatechart::Transition)


def test_simplestatechart::transition_constructor_exists():
    assert callable(simplestatechart::Transition.__init__)


def test_simplestatechart::transition_constructor_args():
    sig = inspect.signature(simplestatechart::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_simplestatechart::transition_has_expression():
    assert hasattr(simplestatechart::Transition, "expression")
    descriptor = None
    for klass in simplestatechart::Transition.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_simplestatechart::state_is_not_abstract():
    assert not inspect.isabstract(simplestatechart::State)


def test_simplestatechart::state_constructor_exists():
    assert callable(simplestatechart::State.__init__)


def test_simplestatechart::state_constructor_args():
    sig = inspect.signature(simplestatechart::State.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "activity" in params, "Missing parameter 'activity'"
    assert "label" in params, "Missing parameter 'label'"

def test_simplestatechart::state_has_type():
    assert hasattr(simplestatechart::State, "type")
    descriptor = None
    for klass in simplestatechart::State.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_simplestatechart::state_has_activity():
    assert hasattr(simplestatechart::State, "activity")
    descriptor = None
    for klass in simplestatechart::State.__mro__:
        if "activity" in klass.__dict__:
            descriptor = klass.__dict__["activity"]
            break
    assert isinstance(descriptor, property)

def test_simplestatechart::state_has_label():
    assert hasattr(simplestatechart::State, "label")
    descriptor = None
    for klass in simplestatechart::State.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_simplestatechart::thing_is_not_abstract():
    assert not inspect.isabstract(simplestatechart::Thing)


def test_simplestatechart::thing_constructor_exists():
    assert callable(simplestatechart::Thing.__init__)


def test_simplestatechart::thing_constructor_args():
    sig = inspect.signature(simplestatechart::Thing.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_simplestatechart::thing_has_id():
    assert hasattr(simplestatechart::Thing, "id")
    descriptor = None
    for klass in simplestatechart::Thing.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_simplestatechart::namedelement_is_not_abstract():
    assert not inspect.isabstract(simplestatechart::NamedElement)


def test_simplestatechart::namedelement_constructor_exists():
    assert callable(simplestatechart::NamedElement.__init__)


def test_simplestatechart::namedelement_constructor_args():
    sig = inspect.signature(simplestatechart::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplestatechart::namedelement_has_name():
    assert hasattr(simplestatechart::NamedElement, "name")
    descriptor = None
    for klass in simplestatechart::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplestatechart::relatedto_is_not_abstract():
    assert not inspect.isabstract(simplestatechart::RelatedTo)


def test_simplestatechart::relatedto_constructor_exists():
    assert callable(simplestatechart::RelatedTo.__init__)


def test_simplestatechart::relatedto_constructor_args():
    sig = inspect.signature(simplestatechart::RelatedTo.__init__)
    params = list(sig.parameters.keys())
    assert "since" in params, "Missing parameter 'since'"

def test_simplestatechart::relatedto_has_since():
    assert hasattr(simplestatechart::RelatedTo, "since")
    descriptor = None
    for klass in simplestatechart::RelatedTo.__mro__:
        if "since" in klass.__dict__:
            descriptor = klass.__dict__["since"]
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
Thing_strategy = st.builds(
    Thing,
)
simplestatechart::Variable_strategy = st.builds(
    simplestatechart::Variable,
    type=
        safe_text,
    value=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
simplestatechart::Transition_strategy = st.builds(
    simplestatechart::Transition,
    expression=
        safe_text
)
simplestatechart::State_strategy = st.builds(
    simplestatechart::State,
    type=
        safe_text,
    activity=
        safe_text,
    label=
        safe_text
)
simplestatechart::Thing_strategy = st.builds(
    simplestatechart::Thing,
    id=
        st.integers()
)
simplestatechart::NamedElement_strategy = st.builds(
    simplestatechart::NamedElement,
    name=
        safe_text
)
simplestatechart::RelatedTo_strategy = st.builds(
    simplestatechart::RelatedTo,
    since=
        safe_text
)

@given(instance=Thing_strategy)
@settings(max_examples=50)
def test_thing_instantiation(instance):
    assert isinstance(instance, Thing)

@given(instance=simplestatechart::Variable_strategy)
@settings(max_examples=50)
def test_simplestatechart::variable_instantiation(instance):
    assert isinstance(instance, simplestatechart::Variable)

@given(instance=simplestatechart::Variable_strategy)
def test_simplestatechart::variable_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=simplestatechart::Variable_strategy)
def test_simplestatechart::variable_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=simplestatechart::Variable_strategy)
def test_simplestatechart::variable_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=simplestatechart::Variable_strategy)
def test_simplestatechart::variable_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=simplestatechart::Transition_strategy)
@settings(max_examples=50)
def test_simplestatechart::transition_instantiation(instance):
    assert isinstance(instance, simplestatechart::Transition)

@given(instance=simplestatechart::Transition_strategy)
def test_simplestatechart::transition_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=simplestatechart::Transition_strategy)
def test_simplestatechart::transition_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=simplestatechart::State_strategy)
@settings(max_examples=50)
def test_simplestatechart::state_instantiation(instance):
    assert isinstance(instance, simplestatechart::State)

@given(instance=simplestatechart::State_strategy)
def test_simplestatechart::state_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=simplestatechart::State_strategy)
def test_simplestatechart::state_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=simplestatechart::State_strategy)
def test_simplestatechart::state_activity_type(instance):
    assert isinstance(instance.activity, str)


@given(instance=simplestatechart::State_strategy)
def test_simplestatechart::state_activity_setter(instance):
    original = instance.activity
    instance.activity = original
    assert instance.activity == original

@given(instance=simplestatechart::State_strategy)
def test_simplestatechart::state_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=simplestatechart::State_strategy)
def test_simplestatechart::state_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=simplestatechart::Thing_strategy)
@settings(max_examples=50)
def test_simplestatechart::thing_instantiation(instance):
    assert isinstance(instance, simplestatechart::Thing)

@given(instance=simplestatechart::Thing_strategy)
def test_simplestatechart::thing_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=simplestatechart::Thing_strategy)
def test_simplestatechart::thing_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=simplestatechart::NamedElement_strategy)
@settings(max_examples=50)
def test_simplestatechart::namedelement_instantiation(instance):
    assert isinstance(instance, simplestatechart::NamedElement)

@given(instance=simplestatechart::NamedElement_strategy)
def test_simplestatechart::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simplestatechart::NamedElement_strategy)
def test_simplestatechart::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simplestatechart::RelatedTo_strategy)
@settings(max_examples=50)
def test_simplestatechart::relatedto_instantiation(instance):
    assert isinstance(instance, simplestatechart::RelatedTo)

@given(instance=simplestatechart::RelatedTo_strategy)
def test_simplestatechart::relatedto_since_type(instance):
    assert isinstance(instance.since, str)


@given(instance=simplestatechart::RelatedTo_strategy)
def test_simplestatechart::relatedto_since_setter(instance):
    original = instance.since
    instance.since = original
    assert instance.since == original
