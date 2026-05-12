import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    UseCase2_UseCase,
    Actor_Actor,
    UseCase_UseCase,
    MyInterface_Interface,
    MyClass,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_usecase2_usecase_is_not_abstract():
    assert not inspect.isabstract(UseCase2_UseCase)


def test_usecase2_usecase_constructor_exists():
    assert callable(UseCase2_UseCase.__init__)


def test_usecase2_usecase_constructor_args():
    sig = inspect.signature(UseCase2_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_actor_actor_is_not_abstract():
    assert not inspect.isabstract(Actor_Actor)


def test_actor_actor_constructor_exists():
    assert callable(Actor_Actor.__init__)


def test_actor_actor_constructor_args():
    sig = inspect.signature(Actor_Actor.__init__)
    params = list(sig.parameters.keys())



def test_usecase_usecase_is_not_abstract():
    assert not inspect.isabstract(UseCase_UseCase)


def test_usecase_usecase_constructor_exists():
    assert callable(UseCase_UseCase.__init__)


def test_usecase_usecase_constructor_args():
    sig = inspect.signature(UseCase_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_myinterface_interface_is_not_abstract():
    assert not inspect.isabstract(MyInterface_Interface)


def test_myinterface_interface_constructor_exists():
    assert callable(MyInterface_Interface.__init__)


def test_myinterface_interface_constructor_args():
    sig = inspect.signature(MyInterface_Interface.__init__)
    params = list(sig.parameters.keys())



def test_myclass_is_not_abstract():
    assert not inspect.isabstract(MyClass)


def test_myclass_constructor_exists():
    assert callable(MyClass.__init__)


def test_myclass_constructor_args():
    sig = inspect.signature(MyClass.__init__)
    params = list(sig.parameters.keys())
    assert "Abb" in params, "Missing parameter 'Abb'"
    assert "ABC" in params, "Missing parameter 'ABC'"

def test_myclass_has_Abb():
    assert hasattr(MyClass, "Abb")
    descriptor = None
    for klass in MyClass.__mro__:
        if "Abb" in klass.__dict__:
            descriptor = klass.__dict__["Abb"]
            break
    assert isinstance(descriptor, property)

def test_myclass_has_ABC():
    assert hasattr(MyClass, "ABC")
    descriptor = None
    for klass in MyClass.__mro__:
        if "ABC" in klass.__dict__:
            descriptor = klass.__dict__["ABC"]
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
UseCase2_UseCase_strategy = st.builds(
    UseCase2_UseCase,
)
Actor_Actor_strategy = st.builds(
    Actor_Actor,
)
UseCase_UseCase_strategy = st.builds(
    UseCase_UseCase,
)
MyInterface_Interface_strategy = st.builds(
    MyInterface_Interface,
)
MyClass_strategy = st.builds(
    MyClass,
    Abb=
        st.booleans(),
    ABC=
        st.none()
)

@given(instance=UseCase2_UseCase_strategy)
@settings(max_examples=50)
def test_usecase2_usecase_instantiation(instance):
    assert isinstance(instance, UseCase2_UseCase)

@given(instance=Actor_Actor_strategy)
@settings(max_examples=50)
def test_actor_actor_instantiation(instance):
    assert isinstance(instance, Actor_Actor)

@given(instance=UseCase_UseCase_strategy)
@settings(max_examples=50)
def test_usecase_usecase_instantiation(instance):
    assert isinstance(instance, UseCase_UseCase)

@given(instance=MyInterface_Interface_strategy)
@settings(max_examples=50)
def test_myinterface_interface_instantiation(instance):
    assert isinstance(instance, MyInterface_Interface)

@given(instance=MyClass_strategy)
@settings(max_examples=50)
def test_myclass_instantiation(instance):
    assert isinstance(instance, MyClass)



@given(instance=MyClass_strategy)
def test_myclass_Abb_setter(instance):
    original = instance.Abb
    instance.Abb = original
    assert instance.Abb == original



@given(instance=MyClass_strategy)
def test_myclass_ABC_setter(instance):
    original = instance.ABC
    instance.ABC = original
    assert instance.ABC == original
