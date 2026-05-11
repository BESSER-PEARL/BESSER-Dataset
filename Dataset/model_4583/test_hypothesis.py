import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    EJavaObject,
    device::Object,
    Fonctionnalite,
    device::Action,
    device::Capture,
    device::EJavaObject,
    device::Parametre,
    device::Fonctionnalite,
    device::Device,
    device::Types,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ejavaobject_is_not_abstract():
    assert not inspect.isabstract(EJavaObject)


def test_ejavaobject_constructor_exists():
    assert callable(EJavaObject.__init__)


def test_ejavaobject_constructor_args():
    sig = inspect.signature(EJavaObject.__init__)
    params = list(sig.parameters.keys())



def test_device::object_is_not_abstract():
    assert not inspect.isabstract(device::Object)


def test_device::object_constructor_exists():
    assert callable(device::Object.__init__)


def test_device::object_constructor_args():
    sig = inspect.signature(device::Object.__init__)
    params = list(sig.parameters.keys())



def test_fonctionnalite_is_not_abstract():
    assert not inspect.isabstract(Fonctionnalite)


def test_fonctionnalite_constructor_exists():
    assert callable(Fonctionnalite.__init__)


def test_fonctionnalite_constructor_args():
    sig = inspect.signature(Fonctionnalite.__init__)
    params = list(sig.parameters.keys())



def test_device::action_is_not_abstract():
    assert not inspect.isabstract(device::Action)


def test_device::action_constructor_exists():
    assert callable(device::Action.__init__)


def test_device::action_constructor_args():
    sig = inspect.signature(device::Action.__init__)
    params = list(sig.parameters.keys())



def test_device::capture_is_not_abstract():
    assert not inspect.isabstract(device::Capture)


def test_device::capture_constructor_exists():
    assert callable(device::Capture.__init__)


def test_device::capture_constructor_args():
    sig = inspect.signature(device::Capture.__init__)
    params = list(sig.parameters.keys())



def test_device::ejavaobject_is_not_abstract():
    assert not inspect.isabstract(device::EJavaObject)


def test_device::ejavaobject_constructor_exists():
    assert callable(device::EJavaObject.__init__)


def test_device::ejavaobject_constructor_args():
    sig = inspect.signature(device::EJavaObject.__init__)
    params = list(sig.parameters.keys())



def test_device::parametre_is_not_abstract():
    assert not inspect.isabstract(device::Parametre)


def test_device::parametre_constructor_exists():
    assert callable(device::Parametre.__init__)


def test_device::parametre_constructor_args():
    sig = inspect.signature(device::Parametre.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_device::parametre_has_name():
    assert hasattr(device::Parametre, "name")
    descriptor = None
    for klass in device::Parametre.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_device::fonctionnalite_is_not_abstract():
    assert not inspect.isabstract(device::Fonctionnalite)


def test_device::fonctionnalite_constructor_exists():
    assert callable(device::Fonctionnalite.__init__)


def test_device::fonctionnalite_constructor_args():
    sig = inspect.signature(device::Fonctionnalite.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_device::fonctionnalite_has_name():
    assert hasattr(device::Fonctionnalite, "name")
    descriptor = None
    for klass in device::Fonctionnalite.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_device::device_is_not_abstract():
    assert not inspect.isabstract(device::Device)


def test_device::device_constructor_exists():
    assert callable(device::Device.__init__)


def test_device::device_constructor_args():
    sig = inspect.signature(device::Device.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_device::device_has_name():
    assert hasattr(device::Device, "name")
    descriptor = None
    for klass in device::Device.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_device::types_is_not_abstract():
    assert not inspect.isabstract(device::Types)


def test_device::types_constructor_exists():
    assert callable(device::Types.__init__)


def test_device::types_constructor_args():
    sig = inspect.signature(device::Types.__init__)
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
EJavaObject_strategy = st.builds(
    EJavaObject,
)
device::Object_strategy = st.builds(
    device::Object,
)
Fonctionnalite_strategy = st.builds(
    Fonctionnalite,
)
device::Action_strategy = st.builds(
    device::Action,
)
device::Capture_strategy = st.builds(
    device::Capture,
)
device::EJavaObject_strategy = st.builds(
    device::EJavaObject,
)
device::Parametre_strategy = st.builds(
    device::Parametre,
    name=
        safe_text
)
device::Fonctionnalite_strategy = st.builds(
    device::Fonctionnalite,
    name=
        safe_text
)
device::Device_strategy = st.builds(
    device::Device,
    name=
        safe_text
)
device::Types_strategy = st.builds(
    device::Types,
)

@given(instance=EJavaObject_strategy)
@settings(max_examples=50)
def test_ejavaobject_instantiation(instance):
    assert isinstance(instance, EJavaObject)

@given(instance=device::Object_strategy)
@settings(max_examples=50)
def test_device::object_instantiation(instance):
    assert isinstance(instance, device::Object)

@given(instance=Fonctionnalite_strategy)
@settings(max_examples=50)
def test_fonctionnalite_instantiation(instance):
    assert isinstance(instance, Fonctionnalite)

@given(instance=device::Action_strategy)
@settings(max_examples=50)
def test_device::action_instantiation(instance):
    assert isinstance(instance, device::Action)

@given(instance=device::Capture_strategy)
@settings(max_examples=50)
def test_device::capture_instantiation(instance):
    assert isinstance(instance, device::Capture)

@given(instance=device::EJavaObject_strategy)
@settings(max_examples=50)
def test_device::ejavaobject_instantiation(instance):
    assert isinstance(instance, device::EJavaObject)

@given(instance=device::Parametre_strategy)
@settings(max_examples=50)
def test_device::parametre_instantiation(instance):
    assert isinstance(instance, device::Parametre)

@given(instance=device::Parametre_strategy)
def test_device::parametre_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=device::Parametre_strategy)
def test_device::parametre_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=device::Fonctionnalite_strategy)
@settings(max_examples=50)
def test_device::fonctionnalite_instantiation(instance):
    assert isinstance(instance, device::Fonctionnalite)

@given(instance=device::Fonctionnalite_strategy)
def test_device::fonctionnalite_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=device::Fonctionnalite_strategy)
def test_device::fonctionnalite_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=device::Device_strategy)
@settings(max_examples=50)
def test_device::device_instantiation(instance):
    assert isinstance(instance, device::Device)

@given(instance=device::Device_strategy)
def test_device::device_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=device::Device_strategy)
def test_device::device_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=device::Types_strategy)
@settings(max_examples=50)
def test_device::types_instantiation(instance):
    assert isinstance(instance, device::Types)
