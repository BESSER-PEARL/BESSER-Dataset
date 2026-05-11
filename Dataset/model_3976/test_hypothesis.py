import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    l3::SystemModel,
    l3::Model,
    l3::Metamodel,
    l3::Component,
    l3::BuildComponent,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_l3::systemmodel_is_not_abstract():
    assert not inspect.isabstract(l3::SystemModel)


def test_l3::systemmodel_constructor_exists():
    assert callable(l3::SystemModel.__init__)


def test_l3::systemmodel_constructor_args():
    sig = inspect.signature(l3::SystemModel.__init__)
    params = list(sig.parameters.keys())



def test_l3::model_is_not_abstract():
    assert not inspect.isabstract(l3::Model)


def test_l3::model_constructor_exists():
    assert callable(l3::Model.__init__)


def test_l3::model_constructor_args():
    sig = inspect.signature(l3::Model.__init__)
    params = list(sig.parameters.keys())



def test_l3::metamodel_is_not_abstract():
    assert not inspect.isabstract(l3::Metamodel)


def test_l3::metamodel_constructor_exists():
    assert callable(l3::Metamodel.__init__)


def test_l3::metamodel_constructor_args():
    sig = inspect.signature(l3::Metamodel.__init__)
    params = list(sig.parameters.keys())



def test_l3::component_is_not_abstract():
    assert not inspect.isabstract(l3::Component)


def test_l3::component_constructor_exists():
    assert callable(l3::Component.__init__)


def test_l3::component_constructor_args():
    sig = inspect.signature(l3::Component.__init__)
    params = list(sig.parameters.keys())



def test_l3::buildcomponent_is_not_abstract():
    assert not inspect.isabstract(l3::BuildComponent)


def test_l3::buildcomponent_constructor_exists():
    assert callable(l3::BuildComponent.__init__)


def test_l3::buildcomponent_constructor_args():
    sig = inspect.signature(l3::BuildComponent.__init__)
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
l3::SystemModel_strategy = st.builds(
    l3::SystemModel,
)
l3::Model_strategy = st.builds(
    l3::Model,
)
l3::Metamodel_strategy = st.builds(
    l3::Metamodel,
)
l3::Component_strategy = st.builds(
    l3::Component,
)
l3::BuildComponent_strategy = st.builds(
    l3::BuildComponent,
)

@given(instance=l3::SystemModel_strategy)
@settings(max_examples=50)
def test_l3::systemmodel_instantiation(instance):
    assert isinstance(instance, l3::SystemModel)

@given(instance=l3::Model_strategy)
@settings(max_examples=50)
def test_l3::model_instantiation(instance):
    assert isinstance(instance, l3::Model)

@given(instance=l3::Metamodel_strategy)
@settings(max_examples=50)
def test_l3::metamodel_instantiation(instance):
    assert isinstance(instance, l3::Metamodel)

@given(instance=l3::Component_strategy)
@settings(max_examples=50)
def test_l3::component_instantiation(instance):
    assert isinstance(instance, l3::Component)

@given(instance=l3::BuildComponent_strategy)
@settings(max_examples=50)
def test_l3::buildcomponent_instantiation(instance):
    assert isinstance(instance, l3::BuildComponent)
