import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    agentDSL::Goal,
    agentDSL::Attribute,
    agentDSL::JAVAID,
    Type,
    agentDSL::Task,
    agentDSL::Outcome,
    agentDSL::Entity,
    agentDSL::TypeDef,
    agentDSL::Type,
    agentDSL::Model,
    agentDSL::Function,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_agentdsl::goal_is_not_abstract():
    assert not inspect.isabstract(agentDSL::Goal)


def test_agentdsl::goal_constructor_exists():
    assert callable(agentDSL::Goal.__init__)


def test_agentdsl::goal_constructor_args():
    sig = inspect.signature(agentDSL::Goal.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_agentdsl::goal_has_name():
    assert hasattr(agentDSL::Goal, "name")
    descriptor = None
    for klass in agentDSL::Goal.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_agentdsl::attribute_is_not_abstract():
    assert not inspect.isabstract(agentDSL::Attribute)


def test_agentdsl::attribute_constructor_exists():
    assert callable(agentDSL::Attribute.__init__)


def test_agentdsl::attribute_constructor_args():
    sig = inspect.signature(agentDSL::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "many" in params, "Missing parameter 'many'"

def test_agentdsl::attribute_has_name():
    assert hasattr(agentDSL::Attribute, "name")
    descriptor = None
    for klass in agentDSL::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_agentdsl::attribute_has_many():
    assert hasattr(agentDSL::Attribute, "many")
    descriptor = None
    for klass in agentDSL::Attribute.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)



def test_agentdsl::javaid_is_not_abstract():
    assert not inspect.isabstract(agentDSL::JAVAID)


def test_agentdsl::javaid_constructor_exists():
    assert callable(agentDSL::JAVAID.__init__)


def test_agentdsl::javaid_constructor_args():
    sig = inspect.signature(agentDSL::JAVAID.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_agentdsl::javaid_has_name():
    assert hasattr(agentDSL::JAVAID, "name")
    descriptor = None
    for klass in agentDSL::JAVAID.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_agentdsl::task_is_not_abstract():
    assert not inspect.isabstract(agentDSL::Task)


def test_agentdsl::task_constructor_exists():
    assert callable(agentDSL::Task.__init__)


def test_agentdsl::task_constructor_args():
    sig = inspect.signature(agentDSL::Task.__init__)
    params = list(sig.parameters.keys())



def test_agentdsl::outcome_is_not_abstract():
    assert not inspect.isabstract(agentDSL::Outcome)


def test_agentdsl::outcome_constructor_exists():
    assert callable(agentDSL::Outcome.__init__)


def test_agentdsl::outcome_constructor_args():
    sig = inspect.signature(agentDSL::Outcome.__init__)
    params = list(sig.parameters.keys())



def test_agentdsl::entity_is_not_abstract():
    assert not inspect.isabstract(agentDSL::Entity)


def test_agentdsl::entity_constructor_exists():
    assert callable(agentDSL::Entity.__init__)


def test_agentdsl::entity_constructor_args():
    sig = inspect.signature(agentDSL::Entity.__init__)
    params = list(sig.parameters.keys())



def test_agentdsl::typedef_is_not_abstract():
    assert not inspect.isabstract(agentDSL::TypeDef)


def test_agentdsl::typedef_constructor_exists():
    assert callable(agentDSL::TypeDef.__init__)


def test_agentdsl::typedef_constructor_args():
    sig = inspect.signature(agentDSL::TypeDef.__init__)
    params = list(sig.parameters.keys())



def test_agentdsl::type_is_not_abstract():
    assert not inspect.isabstract(agentDSL::Type)


def test_agentdsl::type_constructor_exists():
    assert callable(agentDSL::Type.__init__)


def test_agentdsl::type_constructor_args():
    sig = inspect.signature(agentDSL::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_agentdsl::type_has_name():
    assert hasattr(agentDSL::Type, "name")
    descriptor = None
    for klass in agentDSL::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_agentdsl::model_is_not_abstract():
    assert not inspect.isabstract(agentDSL::Model)


def test_agentdsl::model_constructor_exists():
    assert callable(agentDSL::Model.__init__)


def test_agentdsl::model_constructor_args():
    sig = inspect.signature(agentDSL::Model.__init__)
    params = list(sig.parameters.keys())



def test_agentdsl::function_is_not_abstract():
    assert not inspect.isabstract(agentDSL::Function)


def test_agentdsl::function_constructor_exists():
    assert callable(agentDSL::Function.__init__)


def test_agentdsl::function_constructor_args():
    sig = inspect.signature(agentDSL::Function.__init__)
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
agentDSL::Goal_strategy = st.builds(
    agentDSL::Goal,
    name=
        safe_text
)
agentDSL::Attribute_strategy = st.builds(
    agentDSL::Attribute,
    name=
        safe_text,
    many=
        st.booleans()
)
agentDSL::JAVAID_strategy = st.builds(
    agentDSL::JAVAID,
    name=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
agentDSL::Task_strategy = st.builds(
    agentDSL::Task,
)
agentDSL::Outcome_strategy = st.builds(
    agentDSL::Outcome,
)
agentDSL::Entity_strategy = st.builds(
    agentDSL::Entity,
)
agentDSL::TypeDef_strategy = st.builds(
    agentDSL::TypeDef,
)
agentDSL::Type_strategy = st.builds(
    agentDSL::Type,
    name=
        safe_text
)
agentDSL::Model_strategy = st.builds(
    agentDSL::Model,
)
agentDSL::Function_strategy = st.builds(
    agentDSL::Function,
)

@given(instance=agentDSL::Goal_strategy)
@settings(max_examples=50)
def test_agentdsl::goal_instantiation(instance):
    assert isinstance(instance, agentDSL::Goal)

@given(instance=agentDSL::Goal_strategy)
def test_agentdsl::goal_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=agentDSL::Goal_strategy)
def test_agentdsl::goal_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=agentDSL::Attribute_strategy)
@settings(max_examples=50)
def test_agentdsl::attribute_instantiation(instance):
    assert isinstance(instance, agentDSL::Attribute)

@given(instance=agentDSL::Attribute_strategy)
def test_agentdsl::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=agentDSL::Attribute_strategy)
def test_agentdsl::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=agentDSL::Attribute_strategy)
def test_agentdsl::attribute_many_type(instance):
    assert isinstance(instance.many, bool)


@given(instance=agentDSL::Attribute_strategy)
def test_agentdsl::attribute_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original

@given(instance=agentDSL::JAVAID_strategy)
@settings(max_examples=50)
def test_agentdsl::javaid_instantiation(instance):
    assert isinstance(instance, agentDSL::JAVAID)

@given(instance=agentDSL::JAVAID_strategy)
def test_agentdsl::javaid_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=agentDSL::JAVAID_strategy)
def test_agentdsl::javaid_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=agentDSL::Task_strategy)
@settings(max_examples=50)
def test_agentdsl::task_instantiation(instance):
    assert isinstance(instance, agentDSL::Task)

@given(instance=agentDSL::Outcome_strategy)
@settings(max_examples=50)
def test_agentdsl::outcome_instantiation(instance):
    assert isinstance(instance, agentDSL::Outcome)

@given(instance=agentDSL::Entity_strategy)
@settings(max_examples=50)
def test_agentdsl::entity_instantiation(instance):
    assert isinstance(instance, agentDSL::Entity)

@given(instance=agentDSL::TypeDef_strategy)
@settings(max_examples=50)
def test_agentdsl::typedef_instantiation(instance):
    assert isinstance(instance, agentDSL::TypeDef)

@given(instance=agentDSL::Type_strategy)
@settings(max_examples=50)
def test_agentdsl::type_instantiation(instance):
    assert isinstance(instance, agentDSL::Type)

@given(instance=agentDSL::Type_strategy)
def test_agentdsl::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=agentDSL::Type_strategy)
def test_agentdsl::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=agentDSL::Model_strategy)
@settings(max_examples=50)
def test_agentdsl::model_instantiation(instance):
    assert isinstance(instance, agentDSL::Model)

@given(instance=agentDSL::Function_strategy)
@settings(max_examples=50)
def test_agentdsl::function_instantiation(instance):
    assert isinstance(instance, agentDSL::Function)
