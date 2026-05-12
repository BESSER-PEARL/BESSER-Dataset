import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    dsl_EJavaObject,
    dsl_Device,
    dsl_Parametre,
    dsl_Fonctionnalite,
    dsl_IDevice,
    dsl_Robot,
    EJavaObject,
    dsl_Object,
    Fonctionnalite,
    dsl_Action,
    dsl_Capture,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dsl_ejavaobject_is_not_abstract():
    assert not inspect.isabstract(dsl_EJavaObject)


def test_dsl_ejavaobject_constructor_exists():
    assert callable(dsl_EJavaObject.__init__)


def test_dsl_ejavaobject_constructor_args():
    sig = inspect.signature(dsl_EJavaObject.__init__)
    params = list(sig.parameters.keys())



def test_dsl_device_is_not_abstract():
    assert not inspect.isabstract(dsl_Device)


def test_dsl_device_constructor_exists():
    assert callable(dsl_Device.__init__)


def test_dsl_device_constructor_args():
    sig = inspect.signature(dsl_Device.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dsl_device_has_name():
    assert hasattr(dsl_Device, "name")
    descriptor = None
    for klass in dsl_Device.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dsl_parametre_is_not_abstract():
    assert not inspect.isabstract(dsl_Parametre)


def test_dsl_parametre_constructor_exists():
    assert callable(dsl_Parametre.__init__)


def test_dsl_parametre_constructor_args():
    sig = inspect.signature(dsl_Parametre.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dsl_parametre_has_name():
    assert hasattr(dsl_Parametre, "name")
    descriptor = None
    for klass in dsl_Parametre.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dsl_fonctionnalite_is_not_abstract():
    assert not inspect.isabstract(dsl_Fonctionnalite)


def test_dsl_fonctionnalite_constructor_exists():
    assert callable(dsl_Fonctionnalite.__init__)


def test_dsl_fonctionnalite_constructor_args():
    sig = inspect.signature(dsl_Fonctionnalite.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dsl_fonctionnalite_has_name():
    assert hasattr(dsl_Fonctionnalite, "name")
    descriptor = None
    for klass in dsl_Fonctionnalite.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dsl_idevice_is_not_abstract():
    assert not inspect.isabstract(dsl_IDevice)


def test_dsl_idevice_constructor_exists():
    assert callable(dsl_IDevice.__init__)


def test_dsl_idevice_constructor_args():
    sig = inspect.signature(dsl_IDevice.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "typeof" in params, "Missing parameter 'typeof'"

def test_dsl_idevice_has_name():
    assert hasattr(dsl_IDevice, "name")
    descriptor = None
    for klass in dsl_IDevice.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dsl_idevice_has_typeof():
    assert hasattr(dsl_IDevice, "typeof")
    descriptor = None
    for klass in dsl_IDevice.__mro__:
        if "typeof" in klass.__dict__:
            descriptor = klass.__dict__["typeof"]
            break
    assert isinstance(descriptor, property)



def test_dsl_robot_is_not_abstract():
    assert not inspect.isabstract(dsl_Robot)


def test_dsl_robot_constructor_exists():
    assert callable(dsl_Robot.__init__)


def test_dsl_robot_constructor_args():
    sig = inspect.signature(dsl_Robot.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dsl_robot_has_name():
    assert hasattr(dsl_Robot, "name")
    descriptor = None
    for klass in dsl_Robot.__mro__:
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



def test_dsl_object_is_not_abstract():
    assert not inspect.isabstract(dsl_Object)


def test_dsl_object_constructor_exists():
    assert callable(dsl_Object.__init__)


def test_dsl_object_constructor_args():
    sig = inspect.signature(dsl_Object.__init__)
    params = list(sig.parameters.keys())



def test_fonctionnalite_is_not_abstract():
    assert not inspect.isabstract(Fonctionnalite)


def test_fonctionnalite_constructor_exists():
    assert callable(Fonctionnalite.__init__)


def test_fonctionnalite_constructor_args():
    sig = inspect.signature(Fonctionnalite.__init__)
    params = list(sig.parameters.keys())



def test_dsl_action_is_not_abstract():
    assert not inspect.isabstract(dsl_Action)


def test_dsl_action_constructor_exists():
    assert callable(dsl_Action.__init__)


def test_dsl_action_constructor_args():
    sig = inspect.signature(dsl_Action.__init__)
    params = list(sig.parameters.keys())



def test_dsl_capture_is_not_abstract():
    assert not inspect.isabstract(dsl_Capture)


def test_dsl_capture_constructor_exists():
    assert callable(dsl_Capture.__init__)


def test_dsl_capture_constructor_args():
    sig = inspect.signature(dsl_Capture.__init__)
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
dsl_EJavaObject_strategy = st.builds(
    dsl_EJavaObject,
)
dsl_Device_strategy = st.builds(
    dsl_Device,
    name=
        safe_text
)
dsl_Parametre_strategy = st.builds(
    dsl_Parametre,
    name=
        safe_text
)
dsl_Fonctionnalite_strategy = st.builds(
    dsl_Fonctionnalite,
    name=
        safe_text
)
dsl_IDevice_strategy = st.builds(
    dsl_IDevice,
    name=
        safe_text,
    typeof=
        safe_text
)
dsl_Robot_strategy = st.builds(
    dsl_Robot,
    name=
        safe_text
)
EJavaObject_strategy = st.builds(
    EJavaObject,
)
dsl_Object_strategy = st.builds(
    dsl_Object,
)
Fonctionnalite_strategy = st.builds(
    Fonctionnalite,
)
dsl_Action_strategy = st.builds(
    dsl_Action,
)
dsl_Capture_strategy = st.builds(
    dsl_Capture,
)

@given(instance=dsl_EJavaObject_strategy)
@settings(max_examples=50)
def test_dsl_ejavaobject_instantiation(instance):
    assert isinstance(instance, dsl_EJavaObject)

@given(instance=dsl_Device_strategy)
@settings(max_examples=50)
def test_dsl_device_instantiation(instance):
    assert isinstance(instance, dsl_Device)



@given(instance=dsl_Device_strategy)
def test_dsl_device_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dsl_Parametre_strategy)
@settings(max_examples=50)
def test_dsl_parametre_instantiation(instance):
    assert isinstance(instance, dsl_Parametre)



@given(instance=dsl_Parametre_strategy)
def test_dsl_parametre_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dsl_Fonctionnalite_strategy)
@settings(max_examples=50)
def test_dsl_fonctionnalite_instantiation(instance):
    assert isinstance(instance, dsl_Fonctionnalite)



@given(instance=dsl_Fonctionnalite_strategy)
def test_dsl_fonctionnalite_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dsl_IDevice_strategy)
@settings(max_examples=50)
def test_dsl_idevice_instantiation(instance):
    assert isinstance(instance, dsl_IDevice)



@given(instance=dsl_IDevice_strategy)
def test_dsl_idevice_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=dsl_IDevice_strategy)
def test_dsl_idevice_typeof_setter(instance):
    original = instance.typeof
    instance.typeof = original
    assert instance.typeof == original

@given(instance=dsl_Robot_strategy)
@settings(max_examples=50)
def test_dsl_robot_instantiation(instance):
    assert isinstance(instance, dsl_Robot)



@given(instance=dsl_Robot_strategy)
def test_dsl_robot_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=EJavaObject_strategy)
@settings(max_examples=50)
def test_ejavaobject_instantiation(instance):
    assert isinstance(instance, EJavaObject)

@given(instance=dsl_Object_strategy)
@settings(max_examples=50)
def test_dsl_object_instantiation(instance):
    assert isinstance(instance, dsl_Object)

@given(instance=Fonctionnalite_strategy)
@settings(max_examples=50)
def test_fonctionnalite_instantiation(instance):
    assert isinstance(instance, Fonctionnalite)

@given(instance=dsl_Action_strategy)
@settings(max_examples=50)
def test_dsl_action_instantiation(instance):
    assert isinstance(instance, dsl_Action)

@given(instance=dsl_Capture_strategy)
@settings(max_examples=50)
def test_dsl_capture_instantiation(instance):
    assert isinstance(instance, dsl_Capture)
