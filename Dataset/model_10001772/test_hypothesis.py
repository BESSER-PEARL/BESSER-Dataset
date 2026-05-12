import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    UseCase_external,
    Package_Class2,
    Package_Class,
    Actor2_Actor,
    Component_Component,
    Actor_Actor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_usecase_external_is_not_abstract():
    assert not inspect.isabstract(UseCase_external)


def test_usecase_external_constructor_exists():
    assert callable(UseCase_external.__init__)


def test_usecase_external_constructor_args():
    sig = inspect.signature(UseCase_external.__init__)
    params = list(sig.parameters.keys())



def test_package_class2_is_not_abstract():
    assert not inspect.isabstract(Package_Class2)


def test_package_class2_constructor_exists():
    assert callable(Package_Class2.__init__)


def test_package_class2_constructor_args():
    sig = inspect.signature(Package_Class2.__init__)
    params = list(sig.parameters.keys())



def test_package_class_is_not_abstract():
    assert not inspect.isabstract(Package_Class)


def test_package_class_constructor_exists():
    assert callable(Package_Class.__init__)


def test_package_class_constructor_args():
    sig = inspect.signature(Package_Class.__init__)
    params = list(sig.parameters.keys())



def test_actor2_actor_is_not_abstract():
    assert not inspect.isabstract(Actor2_Actor)


def test_actor2_actor_constructor_exists():
    assert callable(Actor2_Actor.__init__)


def test_actor2_actor_constructor_args():
    sig = inspect.signature(Actor2_Actor.__init__)
    params = list(sig.parameters.keys())



def test_component_component_is_not_abstract():
    assert not inspect.isabstract(Component_Component)


def test_component_component_constructor_exists():
    assert callable(Component_Component.__init__)


def test_component_component_constructor_args():
    sig = inspect.signature(Component_Component.__init__)
    params = list(sig.parameters.keys())



def test_actor_actor_is_not_abstract():
    assert not inspect.isabstract(Actor_Actor)


def test_actor_actor_constructor_exists():
    assert callable(Actor_Actor.__init__)


def test_actor_actor_constructor_args():
    sig = inspect.signature(Actor_Actor.__init__)
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
UseCase_external_strategy = st.builds(
    UseCase_external,
)
Package_Class2_strategy = st.builds(
    Package_Class2,
)
Package_Class_strategy = st.builds(
    Package_Class,
)
Actor2_Actor_strategy = st.builds(
    Actor2_Actor,
)
Component_Component_strategy = st.builds(
    Component_Component,
)
Actor_Actor_strategy = st.builds(
    Actor_Actor,
)

@given(instance=UseCase_external_strategy)
@settings(max_examples=50)
def test_usecase_external_instantiation(instance):
    assert isinstance(instance, UseCase_external)

@given(instance=Package_Class2_strategy)
@settings(max_examples=50)
def test_package_class2_instantiation(instance):
    assert isinstance(instance, Package_Class2)

@given(instance=Package_Class_strategy)
@settings(max_examples=50)
def test_package_class_instantiation(instance):
    assert isinstance(instance, Package_Class)

@given(instance=Actor2_Actor_strategy)
@settings(max_examples=50)
def test_actor2_actor_instantiation(instance):
    assert isinstance(instance, Actor2_Actor)

@given(instance=Component_Component_strategy)
@settings(max_examples=50)
def test_component_component_instantiation(instance):
    assert isinstance(instance, Component_Component)

@given(instance=Actor_Actor_strategy)
@settings(max_examples=50)
def test_actor_actor_instantiation(instance):
    assert isinstance(instance, Actor_Actor)
