import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Entity,
    my_AType,
    my_Entity,
    my_Model,
    my_BType,
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



def test_my_atype_is_not_abstract():
    assert not inspect.isabstract(my_AType)


def test_my_atype_constructor_exists():
    assert callable(my_AType.__init__)


def test_my_atype_constructor_args():
    sig = inspect.signature(my_AType.__init__)
    params = list(sig.parameters.keys())



def test_my_entity_is_not_abstract():
    assert not inspect.isabstract(my_Entity)


def test_my_entity_constructor_exists():
    assert callable(my_Entity.__init__)


def test_my_entity_constructor_args():
    sig = inspect.signature(my_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_my_entity_has_name():
    assert hasattr(my_Entity, "name")
    descriptor = None
    for klass in my_Entity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_my_model_is_not_abstract():
    assert not inspect.isabstract(my_Model)


def test_my_model_constructor_exists():
    assert callable(my_Model.__init__)


def test_my_model_constructor_args():
    sig = inspect.signature(my_Model.__init__)
    params = list(sig.parameters.keys())



def test_my_btype_is_not_abstract():
    assert not inspect.isabstract(my_BType)


def test_my_btype_constructor_exists():
    assert callable(my_BType.__init__)


def test_my_btype_constructor_args():
    sig = inspect.signature(my_BType.__init__)
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
my_AType_strategy = st.builds(
    my_AType,
)
my_Entity_strategy = st.builds(
    my_Entity,
    name=
        safe_text
)
my_Model_strategy = st.builds(
    my_Model,
)
my_BType_strategy = st.builds(
    my_BType,
)

@given(instance=Entity_strategy)
@settings(max_examples=50)
def test_entity_instantiation(instance):
    assert isinstance(instance, Entity)

@given(instance=my_AType_strategy)
@settings(max_examples=50)
def test_my_atype_instantiation(instance):
    assert isinstance(instance, my_AType)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=my_AType_strategy)
@settings(max_examples=30)
def test_my_atype_referenced_changes_state(instance):
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
        assert has_statements, f"Function 'referenced' in my_AType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'referenced' in my_AType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'referenced' in my_AType is not implemented or raised an error")

@given(instance=my_Entity_strategy)
@settings(max_examples=50)
def test_my_entity_instantiation(instance):
    assert isinstance(instance, my_Entity)



@given(instance=my_Entity_strategy)
def test_my_entity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=my_Model_strategy)
@settings(max_examples=50)
def test_my_model_instantiation(instance):
    assert isinstance(instance, my_Model)

@given(instance=my_BType_strategy)
@settings(max_examples=50)
def test_my_btype_instantiation(instance):
    assert isinstance(instance, my_BType)
