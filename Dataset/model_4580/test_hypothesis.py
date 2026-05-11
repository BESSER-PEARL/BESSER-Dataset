import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    dsl::EJavaObject,
    dsl::Device,
    dsl::Parametre,
    dsl::Fonctionnalite,
    dsl::IDevice,
    dsl::Robot,
    EJavaObject,
    dsl::Object,
    Fonctionnalite,
    dsl::Capture,
    dsl::Action,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dsl::ejavaobject_is_not_abstract():
    assert not inspect.isabstract(dsl::EJavaObject)


def test_dsl::ejavaobject_constructor_exists():
    assert callable(dsl::EJavaObject.__init__)


def test_dsl::ejavaobject_constructor_args():
    sig = inspect.signature(dsl::EJavaObject.__init__)
    params = list(sig.parameters.keys())



def test_dsl::device_is_not_abstract():
    assert not inspect.isabstract(dsl::Device)


def test_dsl::device_constructor_exists():
    assert callable(dsl::Device.__init__)


def test_dsl::device_constructor_args():
    sig = inspect.signature(dsl::Device.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dsl::device_has_name():
    assert hasattr(dsl::Device, "name")
    descriptor = None
    for klass in dsl::Device.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dsl::parametre_is_not_abstract():
    assert not inspect.isabstract(dsl::Parametre)


def test_dsl::parametre_constructor_exists():
    assert callable(dsl::Parametre.__init__)


def test_dsl::parametre_constructor_args():
    sig = inspect.signature(dsl::Parametre.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dsl::parametre_has_name():
    assert hasattr(dsl::Parametre, "name")
    descriptor = None
    for klass in dsl::Parametre.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dsl::fonctionnalite_is_not_abstract():
    assert not inspect.isabstract(dsl::Fonctionnalite)


def test_dsl::fonctionnalite_constructor_exists():
    assert callable(dsl::Fonctionnalite.__init__)


def test_dsl::fonctionnalite_constructor_args():
    sig = inspect.signature(dsl::Fonctionnalite.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dsl::fonctionnalite_has_name():
    assert hasattr(dsl::Fonctionnalite, "name")
    descriptor = None
    for klass in dsl::Fonctionnalite.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dsl::idevice_is_not_abstract():
    assert not inspect.isabstract(dsl::IDevice)


def test_dsl::idevice_constructor_exists():
    assert callable(dsl::IDevice.__init__)


def test_dsl::idevice_constructor_args():
    sig = inspect.signature(dsl::IDevice.__init__)
    params = list(sig.parameters.keys())
    assert "typeof" in params, "Missing parameter 'typeof'"
    assert "name" in params, "Missing parameter 'name'"

def test_dsl::idevice_has_typeof():
    assert hasattr(dsl::IDevice, "typeof")
    descriptor = None
    for klass in dsl::IDevice.__mro__:
        if "typeof" in klass.__dict__:
            descriptor = klass.__dict__["typeof"]
            break
    assert isinstance(descriptor, property)

def test_dsl::idevice_has_name():
    assert hasattr(dsl::IDevice, "name")
    descriptor = None
    for klass in dsl::IDevice.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dsl::robot_is_not_abstract():
    assert not inspect.isabstract(dsl::Robot)


def test_dsl::robot_constructor_exists():
    assert callable(dsl::Robot.__init__)


def test_dsl::robot_constructor_args():
    sig = inspect.signature(dsl::Robot.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dsl::robot_has_name():
    assert hasattr(dsl::Robot, "name")
    descriptor = None
    for klass in dsl::Robot.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ejavaobject_is_not_abstract():
    assert not inspect.isabstract(EJavaObject)


def test_ejavaobject_constructor_exists():
    assert callable(EJavaObject.__init__)


def test_ejavaobject_constructor_args():
    sig = inspect.signature(EJavaObject.__init__)
    params = list(sig.parameters.keys())



def test_dsl::object_is_not_abstract():
    assert not inspect.isabstract(dsl::Object)


def test_dsl::object_constructor_exists():
    assert callable(dsl::Object.__init__)


def test_dsl::object_constructor_args():
    sig = inspect.signature(dsl::Object.__init__)
    params = list(sig.parameters.keys())



def test_fonctionnalite_is_not_abstract():
    assert not inspect.isabstract(Fonctionnalite)


def test_fonctionnalite_constructor_exists():
    assert callable(Fonctionnalite.__init__)


def test_fonctionnalite_constructor_args():
    sig = inspect.signature(Fonctionnalite.__init__)
    params = list(sig.parameters.keys())



def test_dsl::capture_is_not_abstract():
    assert not inspect.isabstract(dsl::Capture)


def test_dsl::capture_constructor_exists():
    assert callable(dsl::Capture.__init__)


def test_dsl::capture_constructor_args():
    sig = inspect.signature(dsl::Capture.__init__)
    params = list(sig.parameters.keys())



def test_dsl::action_is_not_abstract():
    assert not inspect.isabstract(dsl::Action)


def test_dsl::action_constructor_exists():
    assert callable(dsl::Action.__init__)


def test_dsl::action_constructor_args():
    sig = inspect.signature(dsl::Action.__init__)
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
dsl::EJavaObject_strategy = st.builds(
    dsl::EJavaObject,
)
dsl::Device_strategy = st.builds(
    dsl::Device,
    name=
        safe_text
)
dsl::Parametre_strategy = st.builds(
    dsl::Parametre,
    name=
        safe_text
)
dsl::Fonctionnalite_strategy = st.builds(
    dsl::Fonctionnalite,
    name=
        safe_text
)
dsl::IDevice_strategy = st.builds(
    dsl::IDevice,
    typeof=
        safe_text,
    name=
        safe_text
)
dsl::Robot_strategy = st.builds(
    dsl::Robot,
    name=
        safe_text
)
EJavaObject_strategy = st.builds(
    EJavaObject,
)
dsl::Object_strategy = st.builds(
    dsl::Object,
)
Fonctionnalite_strategy = st.builds(
    Fonctionnalite,
)
dsl::Capture_strategy = st.builds(
    dsl::Capture,
)
dsl::Action_strategy = st.builds(
    dsl::Action,
)

@given(instance=dsl::EJavaObject_strategy)
@settings(max_examples=50)
def test_dsl::ejavaobject_instantiation(instance):
    assert isinstance(instance, dsl::EJavaObject)

@given(instance=dsl::Device_strategy)
@settings(max_examples=50)
def test_dsl::device_instantiation(instance):
    assert isinstance(instance, dsl::Device)

@given(instance=dsl::Device_strategy)
def test_dsl::device_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dsl::Device_strategy)
def test_dsl::device_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dsl::Parametre_strategy)
@settings(max_examples=50)
def test_dsl::parametre_instantiation(instance):
    assert isinstance(instance, dsl::Parametre)

@given(instance=dsl::Parametre_strategy)
def test_dsl::parametre_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dsl::Parametre_strategy)
def test_dsl::parametre_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dsl::Fonctionnalite_strategy)
@settings(max_examples=50)
def test_dsl::fonctionnalite_instantiation(instance):
    assert isinstance(instance, dsl::Fonctionnalite)

@given(instance=dsl::Fonctionnalite_strategy)
def test_dsl::fonctionnalite_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dsl::Fonctionnalite_strategy)
def test_dsl::fonctionnalite_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dsl::IDevice_strategy)
@settings(max_examples=50)
def test_dsl::idevice_instantiation(instance):
    assert isinstance(instance, dsl::IDevice)

@given(instance=dsl::IDevice_strategy)
def test_dsl::idevice_typeof_type(instance):
    assert isinstance(instance.typeof, str)


@given(instance=dsl::IDevice_strategy)
def test_dsl::idevice_typeof_setter(instance):
    original = instance.typeof
    instance.typeof = original
    assert instance.typeof == original

@given(instance=dsl::IDevice_strategy)
def test_dsl::idevice_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dsl::IDevice_strategy)
def test_dsl::idevice_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dsl::Robot_strategy)
@settings(max_examples=50)
def test_dsl::robot_instantiation(instance):
    assert isinstance(instance, dsl::Robot)

@given(instance=dsl::Robot_strategy)
def test_dsl::robot_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dsl::Robot_strategy)
def test_dsl::robot_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=EJavaObject_strategy)
@settings(max_examples=50)
def test_ejavaobject_instantiation(instance):
    assert isinstance(instance, EJavaObject)

@given(instance=dsl::Object_strategy)
@settings(max_examples=50)
def test_dsl::object_instantiation(instance):
    assert isinstance(instance, dsl::Object)

@given(instance=Fonctionnalite_strategy)
@settings(max_examples=50)
def test_fonctionnalite_instantiation(instance):
    assert isinstance(instance, Fonctionnalite)

@given(instance=dsl::Capture_strategy)
@settings(max_examples=50)
def test_dsl::capture_instantiation(instance):
    assert isinstance(instance, dsl::Capture)

@given(instance=dsl::Action_strategy)
@settings(max_examples=50)
def test_dsl::action_instantiation(instance):
    assert isinstance(instance, dsl::Action)
