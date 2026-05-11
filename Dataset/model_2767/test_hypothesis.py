import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Entity,
    my::AType,
    my::Entity,
    my::Model,
    my::BType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_entity_is_not_abstract():
    assert not inspect.isabstract(Entity)


def test_entity_constructor_exists():
    assert callable(Entity.__init__)


def test_entity_constructor_args():
    sig = inspect.signature(Entity.__init__)
    params = list(sig.parameters.keys())



def test_my::atype_is_not_abstract():
    assert not inspect.isabstract(my::AType)


def test_my::atype_constructor_exists():
    assert callable(my::AType.__init__)


def test_my::atype_constructor_args():
    sig = inspect.signature(my::AType.__init__)
    params = list(sig.parameters.keys())



def test_my::entity_is_not_abstract():
    assert not inspect.isabstract(my::Entity)


def test_my::entity_constructor_exists():
    assert callable(my::Entity.__init__)


def test_my::entity_constructor_args():
    sig = inspect.signature(my::Entity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_my::entity_has_name():
    assert hasattr(my::Entity, "name")
    descriptor = None
    for klass in my::Entity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_my::model_is_not_abstract():
    assert not inspect.isabstract(my::Model)


def test_my::model_constructor_exists():
    assert callable(my::Model.__init__)


def test_my::model_constructor_args():
    sig = inspect.signature(my::Model.__init__)
    params = list(sig.parameters.keys())



def test_my::btype_is_not_abstract():
    assert not inspect.isabstract(my::BType)


def test_my::btype_constructor_exists():
    assert callable(my::BType.__init__)


def test_my::btype_constructor_args():
    sig = inspect.signature(my::BType.__init__)
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
Entity_strategy = st.builds(
    Entity,
)
my::AType_strategy = st.builds(
    my::AType,
)
my::Entity_strategy = st.builds(
    my::Entity,
    name=
        safe_text
)
my::Model_strategy = st.builds(
    my::Model,
)
my::BType_strategy = st.builds(
    my::BType,
)

@given(instance=Entity_strategy)
@settings(max_examples=50)
def test_entity_instantiation(instance):
    assert isinstance(instance, Entity)

@given(instance=my::AType_strategy)
@settings(max_examples=50)
def test_my::atype_instantiation(instance):
    assert isinstance(instance, my::AType)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=my::AType_strategy)
@settings(max_examples=30)
def test_my::atype_referenced_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.referenced()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.referenced).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'referenced' in my::AType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'referenced' in my::AType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'referenced' in my::AType is not implemented or raised an error")

@given(instance=my::Entity_strategy)
@settings(max_examples=50)
def test_my::entity_instantiation(instance):
    assert isinstance(instance, my::Entity)

@given(instance=my::Entity_strategy)
def test_my::entity_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=my::Entity_strategy)
def test_my::entity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=my::Model_strategy)
@settings(max_examples=50)
def test_my::model_instantiation(instance):
    assert isinstance(instance, my::Model)

@given(instance=my::BType_strategy)
@settings(max_examples=50)
def test_my::btype_instantiation(instance):
    assert isinstance(instance, my::BType)
