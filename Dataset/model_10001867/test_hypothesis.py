import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    mahasiswa,
    Actor2_Actor,
    UseCase3_UseCase,
    UseCase2_UseCase,
    UseCase_UseCase,
    Actor_Actor,
    Class,
    Interface_Interface,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mahasiswa_is_not_abstract():
    assert not inspect.isabstract(mahasiswa)


def test_mahasiswa_constructor_exists():
    assert callable(mahasiswa.__init__)


def test_mahasiswa_constructor_args():
    sig = inspect.signature(mahasiswa.__init__)
    params = list(sig.parameters.keys())
    assert "nim" in params, "Missing parameter 'nim'"

def test_mahasiswa_has_nim():
    assert hasattr(mahasiswa, "nim")
    descriptor = None
    for klass in mahasiswa.__mro__:
        if "nim" in klass.__dict__:
            descriptor = klass.__dict__["nim"]
            break
    assert isinstance(descriptor, property)



def test_actor2_actor_is_not_abstract():
    assert not inspect.isabstract(Actor2_Actor)


def test_actor2_actor_constructor_exists():
    assert callable(Actor2_Actor.__init__)


def test_actor2_actor_constructor_args():
    sig = inspect.signature(Actor2_Actor.__init__)
    params = list(sig.parameters.keys())



def test_usecase3_usecase_is_not_abstract():
    assert not inspect.isabstract(UseCase3_UseCase)


def test_usecase3_usecase_constructor_exists():
    assert callable(UseCase3_UseCase.__init__)


def test_usecase3_usecase_constructor_args():
    sig = inspect.signature(UseCase3_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_usecase2_usecase_is_not_abstract():
    assert not inspect.isabstract(UseCase2_UseCase)


def test_usecase2_usecase_constructor_exists():
    assert callable(UseCase2_UseCase.__init__)


def test_usecase2_usecase_constructor_args():
    sig = inspect.signature(UseCase2_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_usecase_usecase_is_not_abstract():
    assert not inspect.isabstract(UseCase_UseCase)


def test_usecase_usecase_constructor_exists():
    assert callable(UseCase_UseCase.__init__)


def test_usecase_usecase_constructor_args():
    sig = inspect.signature(UseCase_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_actor_actor_is_not_abstract():
    assert not inspect.isabstract(Actor_Actor)


def test_actor_actor_constructor_exists():
    assert callable(Actor_Actor.__init__)


def test_actor_actor_constructor_args():
    sig = inspect.signature(Actor_Actor.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"

def test_class_has_attribute():
    assert hasattr(Class, "attribute")
    descriptor = None
    for klass in Class.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)



def test_interface_interface_is_not_abstract():
    assert not inspect.isabstract(Interface_Interface)


def test_interface_interface_constructor_exists():
    assert callable(Interface_Interface.__init__)


def test_interface_interface_constructor_args():
    sig = inspect.signature(Interface_Interface.__init__)
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
mahasiswa_strategy = st.builds(
    mahasiswa,
    nim=
        safe_text
)
Actor2_Actor_strategy = st.builds(
    Actor2_Actor,
)
UseCase3_UseCase_strategy = st.builds(
    UseCase3_UseCase,
)
UseCase2_UseCase_strategy = st.builds(
    UseCase2_UseCase,
)
UseCase_UseCase_strategy = st.builds(
    UseCase_UseCase,
)
Actor_Actor_strategy = st.builds(
    Actor_Actor,
)
Class_strategy = st.builds(
    Class,
    attribute=
        safe_text
)
Interface_Interface_strategy = st.builds(
    Interface_Interface,
)

@given(instance=mahasiswa_strategy)
@settings(max_examples=50)
def test_mahasiswa_instantiation(instance):
    assert isinstance(instance, mahasiswa)



@given(instance=mahasiswa_strategy)
def test_mahasiswa_nim_setter(instance):
    original = instance.nim
    instance.nim = original
    assert instance.nim == original

@given(instance=Actor2_Actor_strategy)
@settings(max_examples=50)
def test_actor2_actor_instantiation(instance):
    assert isinstance(instance, Actor2_Actor)

@given(instance=UseCase3_UseCase_strategy)
@settings(max_examples=50)
def test_usecase3_usecase_instantiation(instance):
    assert isinstance(instance, UseCase3_UseCase)

@given(instance=UseCase2_UseCase_strategy)
@settings(max_examples=50)
def test_usecase2_usecase_instantiation(instance):
    assert isinstance(instance, UseCase2_UseCase)

@given(instance=UseCase_UseCase_strategy)
@settings(max_examples=50)
def test_usecase_usecase_instantiation(instance):
    assert isinstance(instance, UseCase_UseCase)

@given(instance=Actor_Actor_strategy)
@settings(max_examples=50)
def test_actor_actor_instantiation(instance):
    assert isinstance(instance, Actor_Actor)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)



@given(instance=Class_strategy)
def test_class_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original

@given(instance=Interface_Interface_strategy)
@settings(max_examples=50)
def test_interface_interface_instantiation(instance):
    assert isinstance(instance, Interface_Interface)
