import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    l3_SystemModel,
    l3_Model,
    l3_Metamodel,
    l3_Component,
    l3_BuildComponent,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_l3_systemmodel_is_not_abstract():
    assert not inspect.isabstract(l3_SystemModel)


def test_l3_systemmodel_constructor_exists():
    assert callable(l3_SystemModel.__init__)


def test_l3_systemmodel_constructor_args():
    sig = inspect.signature(l3_SystemModel.__init__)
    params = list(sig.parameters.keys())



def test_l3_model_is_not_abstract():
    assert not inspect.isabstract(l3_Model)


def test_l3_model_constructor_exists():
    assert callable(l3_Model.__init__)


def test_l3_model_constructor_args():
    sig = inspect.signature(l3_Model.__init__)
    params = list(sig.parameters.keys())



def test_l3_metamodel_is_not_abstract():
    assert not inspect.isabstract(l3_Metamodel)


def test_l3_metamodel_constructor_exists():
    assert callable(l3_Metamodel.__init__)


def test_l3_metamodel_constructor_args():
    sig = inspect.signature(l3_Metamodel.__init__)
    params = list(sig.parameters.keys())



def test_l3_component_is_not_abstract():
    assert not inspect.isabstract(l3_Component)


def test_l3_component_constructor_exists():
    assert callable(l3_Component.__init__)


def test_l3_component_constructor_args():
    sig = inspect.signature(l3_Component.__init__)
    params = list(sig.parameters.keys())



def test_l3_buildcomponent_is_not_abstract():
    assert not inspect.isabstract(l3_BuildComponent)


def test_l3_buildcomponent_constructor_exists():
    assert callable(l3_BuildComponent.__init__)


def test_l3_buildcomponent_constructor_args():
    sig = inspect.signature(l3_BuildComponent.__init__)
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
l3_SystemModel_strategy = st.builds(
    l3_SystemModel,
)
l3_Model_strategy = st.builds(
    l3_Model,
)
l3_Metamodel_strategy = st.builds(
    l3_Metamodel,
)
l3_Component_strategy = st.builds(
    l3_Component,
)
l3_BuildComponent_strategy = st.builds(
    l3_BuildComponent,
)

@given(instance=l3_SystemModel_strategy)
@settings(max_examples=50)
def test_l3_systemmodel_instantiation(instance):
    assert isinstance(instance, l3_SystemModel)

@given(instance=l3_Model_strategy)
@settings(max_examples=50)
def test_l3_model_instantiation(instance):
    assert isinstance(instance, l3_Model)

@given(instance=l3_Metamodel_strategy)
@settings(max_examples=50)
def test_l3_metamodel_instantiation(instance):
    assert isinstance(instance, l3_Metamodel)

@given(instance=l3_Component_strategy)
@settings(max_examples=50)
def test_l3_component_instantiation(instance):
    assert isinstance(instance, l3_Component)

@given(instance=l3_BuildComponent_strategy)
@settings(max_examples=50)
def test_l3_buildcomponent_instantiation(instance):
    assert isinstance(instance, l3_BuildComponent)
