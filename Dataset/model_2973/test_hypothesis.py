import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    cgimodel::StateModels,
    cgimodel::Transition,
    cgimodel::BaseState,
    cgimodel::StateModel,
    cgimodel::Expr,
    BaseState,
    cgimodel::OrState,
    cgimodel::State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_cgimodel::statemodels_is_not_abstract():
    assert not inspect.isabstract(cgimodel::StateModels)


def test_cgimodel::statemodels_constructor_exists():
    assert callable(cgimodel::StateModels.__init__)


def test_cgimodel::statemodels_constructor_args():
    sig = inspect.signature(cgimodel::StateModels.__init__)
    params = list(sig.parameters.keys())



def test_cgimodel::transition_is_not_abstract():
    assert not inspect.isabstract(cgimodel::Transition)


def test_cgimodel::transition_constructor_exists():
    assert callable(cgimodel::Transition.__init__)


def test_cgimodel::transition_constructor_args():
    sig = inspect.signature(cgimodel::Transition.__init__)
    params = list(sig.parameters.keys())



def test_cgimodel::basestate_is_not_abstract():
    assert not inspect.isabstract(cgimodel::BaseState)


def test_cgimodel::basestate_constructor_exists():
    assert callable(cgimodel::BaseState.__init__)


def test_cgimodel::basestate_constructor_args():
    sig = inspect.signature(cgimodel::BaseState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cgimodel::basestate_has_name():
    assert hasattr(cgimodel::BaseState, "name")
    descriptor = None
    for klass in cgimodel::BaseState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cgimodel::statemodel_is_not_abstract():
    assert not inspect.isabstract(cgimodel::StateModel)


def test_cgimodel::statemodel_constructor_exists():
    assert callable(cgimodel::StateModel.__init__)


def test_cgimodel::statemodel_constructor_args():
    sig = inspect.signature(cgimodel::StateModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cgimodel::statemodel_has_name():
    assert hasattr(cgimodel::StateModel, "name")
    descriptor = None
    for klass in cgimodel::StateModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cgimodel::expr_is_not_abstract():
    assert not inspect.isabstract(cgimodel::Expr)


def test_cgimodel::expr_constructor_exists():
    assert callable(cgimodel::Expr.__init__)


def test_cgimodel::expr_constructor_args():
    sig = inspect.signature(cgimodel::Expr.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cgimodel::expr_has_value():
    assert hasattr(cgimodel::Expr, "value")
    descriptor = None
    for klass in cgimodel::Expr.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_basestate_is_not_abstract():
    assert not inspect.isabstract(BaseState)


def test_basestate_constructor_exists():
    assert callable(BaseState.__init__)


def test_basestate_constructor_args():
    sig = inspect.signature(BaseState.__init__)
    params = list(sig.parameters.keys())



def test_cgimodel::orstate_is_not_abstract():
    assert not inspect.isabstract(cgimodel::OrState)


def test_cgimodel::orstate_constructor_exists():
    assert callable(cgimodel::OrState.__init__)


def test_cgimodel::orstate_constructor_args():
    sig = inspect.signature(cgimodel::OrState.__init__)
    params = list(sig.parameters.keys())



def test_cgimodel::state_is_not_abstract():
    assert not inspect.isabstract(cgimodel::State)


def test_cgimodel::state_constructor_exists():
    assert callable(cgimodel::State.__init__)


def test_cgimodel::state_constructor_args():
    sig = inspect.signature(cgimodel::State.__init__)
    params = list(sig.parameters.keys())
    assert "set" in params, "Missing parameter 'set'"

def test_cgimodel::state_has_set():
    assert hasattr(cgimodel::State, "set")
    descriptor = None
    for klass in cgimodel::State.__mro__:
        if "set" in klass.__dict__:
            descriptor = klass.__dict__["set"]
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
cgimodel::StateModels_strategy = st.builds(
    cgimodel::StateModels,
)
cgimodel::Transition_strategy = st.builds(
    cgimodel::Transition,
)
cgimodel::BaseState_strategy = st.builds(
    cgimodel::BaseState,
    name=
        safe_text
)
cgimodel::StateModel_strategy = st.builds(
    cgimodel::StateModel,
    name=
        safe_text
)
cgimodel::Expr_strategy = st.builds(
    cgimodel::Expr,
    value=
        safe_text
)
BaseState_strategy = st.builds(
    BaseState,
)
cgimodel::OrState_strategy = st.builds(
    cgimodel::OrState,
)
cgimodel::State_strategy = st.builds(
    cgimodel::State,
    set=
        st.booleans()
)

@given(instance=cgimodel::StateModels_strategy)
@settings(max_examples=50)
def test_cgimodel::statemodels_instantiation(instance):
    assert isinstance(instance, cgimodel::StateModels)

@given(instance=cgimodel::Transition_strategy)
@settings(max_examples=50)
def test_cgimodel::transition_instantiation(instance):
    assert isinstance(instance, cgimodel::Transition)

@given(instance=cgimodel::BaseState_strategy)
@settings(max_examples=50)
def test_cgimodel::basestate_instantiation(instance):
    assert isinstance(instance, cgimodel::BaseState)

@given(instance=cgimodel::BaseState_strategy)
def test_cgimodel::basestate_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cgimodel::BaseState_strategy)
def test_cgimodel::basestate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=cgimodel::BaseState_strategy)
@settings(max_examples=30)
def test_cgimodel::basestate_isset_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isSet()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isSet).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isSet' in cgimodel::BaseState is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isSet' in cgimodel::BaseState did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isSet' in cgimodel::BaseState is not implemented or raised an error")

@given(instance=cgimodel::StateModel_strategy)
@settings(max_examples=50)
def test_cgimodel::statemodel_instantiation(instance):
    assert isinstance(instance, cgimodel::StateModel)

@given(instance=cgimodel::StateModel_strategy)
def test_cgimodel::statemodel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cgimodel::StateModel_strategy)
def test_cgimodel::statemodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cgimodel::Expr_strategy)
@settings(max_examples=50)
def test_cgimodel::expr_instantiation(instance):
    assert isinstance(instance, cgimodel::Expr)

@given(instance=cgimodel::Expr_strategy)
def test_cgimodel::expr_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cgimodel::Expr_strategy)
def test_cgimodel::expr_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=BaseState_strategy)
@settings(max_examples=50)
def test_basestate_instantiation(instance):
    assert isinstance(instance, BaseState)

@given(instance=cgimodel::OrState_strategy)
@settings(max_examples=50)
def test_cgimodel::orstate_instantiation(instance):
    assert isinstance(instance, cgimodel::OrState)

@given(instance=cgimodel::State_strategy)
@settings(max_examples=50)
def test_cgimodel::state_instantiation(instance):
    assert isinstance(instance, cgimodel::State)

@given(instance=cgimodel::State_strategy)
def test_cgimodel::state_set_type(instance):
    assert isinstance(instance.set, bool)


@given(instance=cgimodel::State_strategy)
def test_cgimodel::state_set_setter(instance):
    original = instance.set
    instance.set = original
    assert instance.set == original
