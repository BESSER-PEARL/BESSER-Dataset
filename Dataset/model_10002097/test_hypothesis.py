import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Class3,
    Class2,
    Package_Class,
    Interface_Interface,
    Class,
    Actor_Actor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_class3_is_not_abstract():
    assert not inspect.isabstract(Class3)


def test_class3_constructor_exists():
    assert callable(Class3.__init__)


def test_class3_constructor_args():
    sig = inspect.signature(Class3.__init__)
    params = list(sig.parameters.keys())



def test_class2_is_not_abstract():
    assert not inspect.isabstract(Class2)


def test_class2_constructor_exists():
    assert callable(Class2.__init__)


def test_class2_constructor_args():
    sig = inspect.signature(Class2.__init__)
    params = list(sig.parameters.keys())



def test_package_class_is_not_abstract():
    assert not inspect.isabstract(Package_Class)


def test_package_class_constructor_exists():
    assert callable(Package_Class.__init__)


def test_package_class_constructor_args():
    sig = inspect.signature(Package_Class.__init__)
    params = list(sig.parameters.keys())



def test_interface_interface_is_not_abstract():
    assert not inspect.isabstract(Interface_Interface)


def test_interface_interface_constructor_exists():
    assert callable(Interface_Interface.__init__)


def test_interface_interface_constructor_args():
    sig = inspect.signature(Interface_Interface.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
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
Class3_strategy = st.builds(
    Class3,
)
Class2_strategy = st.builds(
    Class2,
)
Package_Class_strategy = st.builds(
    Package_Class,
)
Interface_Interface_strategy = st.builds(
    Interface_Interface,
)
Class_strategy = st.builds(
    Class,
)
Actor_Actor_strategy = st.builds(
    Actor_Actor,
)

@given(instance=Class3_strategy)
@settings(max_examples=50)
def test_class3_instantiation(instance):
    assert isinstance(instance, Class3)

@given(instance=Class2_strategy)
@settings(max_examples=50)
def test_class2_instantiation(instance):
    assert isinstance(instance, Class2)

@given(instance=Package_Class_strategy)
@settings(max_examples=50)
def test_package_class_instantiation(instance):
    assert isinstance(instance, Package_Class)

@given(instance=Interface_Interface_strategy)
@settings(max_examples=50)
def test_interface_interface_instantiation(instance):
    assert isinstance(instance, Interface_Interface)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=Actor_Actor_strategy)
@settings(max_examples=50)
def test_actor_actor_instantiation(instance):
    assert isinstance(instance, Actor_Actor)
