import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Port,
    componentmodel::OutPort,
    componentmodel::InPort,
    componentmodel::Property,
    Property,
    componentmodel::EnumProperty,
    componentmodel::NumericProperty,
    Component,
    componentmodel::CompositeComponent,
    componentmodel::PrimitiveComponent,
    componentmodel::Port,
    componentmodel::Component,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_port_is_not_abstract():
    assert not inspect.isabstract(Port)


def test_port_constructor_exists():
    assert callable(Port.__init__)


def test_port_constructor_args():
    sig = inspect.signature(Port.__init__)
    params = list(sig.parameters.keys())



def test_componentmodel::outport_is_not_abstract():
    assert not inspect.isabstract(componentmodel::OutPort)


def test_componentmodel::outport_constructor_exists():
    assert callable(componentmodel::OutPort.__init__)


def test_componentmodel::outport_constructor_args():
    sig = inspect.signature(componentmodel::OutPort.__init__)
    params = list(sig.parameters.keys())



def test_componentmodel::inport_is_not_abstract():
    assert not inspect.isabstract(componentmodel::InPort)


def test_componentmodel::inport_constructor_exists():
    assert callable(componentmodel::InPort.__init__)


def test_componentmodel::inport_constructor_args():
    sig = inspect.signature(componentmodel::InPort.__init__)
    params = list(sig.parameters.keys())



def test_componentmodel::property_is_not_abstract():
    assert not inspect.isabstract(componentmodel::Property)


def test_componentmodel::property_constructor_exists():
    assert callable(componentmodel::Property.__init__)


def test_componentmodel::property_constructor_args():
    sig = inspect.signature(componentmodel::Property.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"

def test_componentmodel::property_has_description():
    assert hasattr(componentmodel::Property, "description")
    descriptor = None
    for klass in componentmodel::Property.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_componentmodel::property_has_name():
    assert hasattr(componentmodel::Property, "name")
    descriptor = None
    for klass in componentmodel::Property.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_componentmodel::enumproperty_is_not_abstract():
    assert not inspect.isabstract(componentmodel::EnumProperty)


def test_componentmodel::enumproperty_constructor_exists():
    assert callable(componentmodel::EnumProperty.__init__)


def test_componentmodel::enumproperty_constructor_args():
    sig = inspect.signature(componentmodel::EnumProperty.__init__)
    params = list(sig.parameters.keys())
    assert "literalValue" in params, "Missing parameter 'literalValue'"

def test_componentmodel::enumproperty_has_literalValue():
    assert hasattr(componentmodel::EnumProperty, "literalValue")
    descriptor = None
    for klass in componentmodel::EnumProperty.__mro__:
        if "literalValue" in klass.__dict__:
            descriptor = klass.__dict__["literalValue"]
            break
    assert isinstance(descriptor, property)



def test_componentmodel::numericproperty_is_not_abstract():
    assert not inspect.isabstract(componentmodel::NumericProperty)


def test_componentmodel::numericproperty_constructor_exists():
    assert callable(componentmodel::NumericProperty.__init__)


def test_componentmodel::numericproperty_constructor_args():
    sig = inspect.signature(componentmodel::NumericProperty.__init__)
    params = list(sig.parameters.keys())
    assert "maxValue" in params, "Missing parameter 'maxValue'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "minValue" in params, "Missing parameter 'minValue'"

def test_componentmodel::numericproperty_has_maxValue():
    assert hasattr(componentmodel::NumericProperty, "maxValue")
    descriptor = None
    for klass in componentmodel::NumericProperty.__mro__:
        if "maxValue" in klass.__dict__:
            descriptor = klass.__dict__["maxValue"]
            break
    assert isinstance(descriptor, property)

def test_componentmodel::numericproperty_has_defaultValue():
    assert hasattr(componentmodel::NumericProperty, "defaultValue")
    descriptor = None
    for klass in componentmodel::NumericProperty.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)

def test_componentmodel::numericproperty_has_minValue():
    assert hasattr(componentmodel::NumericProperty, "minValue")
    descriptor = None
    for klass in componentmodel::NumericProperty.__mro__:
        if "minValue" in klass.__dict__:
            descriptor = klass.__dict__["minValue"]
            break
    assert isinstance(descriptor, property)



def test_component_is_not_abstract():
    assert not inspect.isabstract(Component)


def test_component_constructor_exists():
    assert callable(Component.__init__)


def test_component_constructor_args():
    sig = inspect.signature(Component.__init__)
    params = list(sig.parameters.keys())



def test_componentmodel::compositecomponent_is_not_abstract():
    assert not inspect.isabstract(componentmodel::CompositeComponent)


def test_componentmodel::compositecomponent_constructor_exists():
    assert callable(componentmodel::CompositeComponent.__init__)


def test_componentmodel::compositecomponent_constructor_args():
    sig = inspect.signature(componentmodel::CompositeComponent.__init__)
    params = list(sig.parameters.keys())



def test_componentmodel::primitivecomponent_is_not_abstract():
    assert not inspect.isabstract(componentmodel::PrimitiveComponent)


def test_componentmodel::primitivecomponent_constructor_exists():
    assert callable(componentmodel::PrimitiveComponent.__init__)


def test_componentmodel::primitivecomponent_constructor_args():
    sig = inspect.signature(componentmodel::PrimitiveComponent.__init__)
    params = list(sig.parameters.keys())



def test_componentmodel::port_is_not_abstract():
    assert not inspect.isabstract(componentmodel::Port)


def test_componentmodel::port_constructor_exists():
    assert callable(componentmodel::Port.__init__)


def test_componentmodel::port_constructor_args():
    sig = inspect.signature(componentmodel::Port.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"
    assert "typePackage" in params, "Missing parameter 'typePackage'"

def test_componentmodel::port_has_type():
    assert hasattr(componentmodel::Port, "type")
    descriptor = None
    for klass in componentmodel::Port.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_componentmodel::port_has_name():
    assert hasattr(componentmodel::Port, "name")
    descriptor = None
    for klass in componentmodel::Port.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_componentmodel::port_has_description():
    assert hasattr(componentmodel::Port, "description")
    descriptor = None
    for klass in componentmodel::Port.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_componentmodel::port_has_typePackage():
    assert hasattr(componentmodel::Port, "typePackage")
    descriptor = None
    for klass in componentmodel::Port.__mro__:
        if "typePackage" in klass.__dict__:
            descriptor = klass.__dict__["typePackage"]
            break
    assert isinstance(descriptor, property)



def test_componentmodel::component_is_not_abstract():
    assert not inspect.isabstract(componentmodel::Component)


def test_componentmodel::component_constructor_exists():
    assert callable(componentmodel::Component.__init__)


def test_componentmodel::component_constructor_args():
    sig = inspect.signature(componentmodel::Component.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"

def test_componentmodel::component_has_name():
    assert hasattr(componentmodel::Component, "name")
    descriptor = None
    for klass in componentmodel::Component.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_componentmodel::component_has_description():
    assert hasattr(componentmodel::Component, "description")
    descriptor = None
    for klass in componentmodel::Component.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
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
Port_strategy = st.builds(
    Port,
)
componentmodel::OutPort_strategy = st.builds(
    componentmodel::OutPort,
)
componentmodel::InPort_strategy = st.builds(
    componentmodel::InPort,
)
componentmodel::Property_strategy = st.builds(
    componentmodel::Property,
    description=
        safe_text,
    name=
        safe_text
)
Property_strategy = st.builds(
    Property,
)
componentmodel::EnumProperty_strategy = st.builds(
    componentmodel::EnumProperty,
    literalValue=
        safe_text
)
componentmodel::NumericProperty_strategy = st.builds(
    componentmodel::NumericProperty,
    maxValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    defaultValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    minValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Component_strategy = st.builds(
    Component,
)
componentmodel::CompositeComponent_strategy = st.builds(
    componentmodel::CompositeComponent,
)
componentmodel::PrimitiveComponent_strategy = st.builds(
    componentmodel::PrimitiveComponent,
)
componentmodel::Port_strategy = st.builds(
    componentmodel::Port,
    type=
        safe_text,
    name=
        safe_text,
    description=
        safe_text,
    typePackage=
        safe_text
)
componentmodel::Component_strategy = st.builds(
    componentmodel::Component,
    name=
        safe_text,
    description=
        safe_text
)

@given(instance=Port_strategy)
@settings(max_examples=50)
def test_port_instantiation(instance):
    assert isinstance(instance, Port)

@given(instance=componentmodel::OutPort_strategy)
@settings(max_examples=50)
def test_componentmodel::outport_instantiation(instance):
    assert isinstance(instance, componentmodel::OutPort)

@given(instance=componentmodel::InPort_strategy)
@settings(max_examples=50)
def test_componentmodel::inport_instantiation(instance):
    assert isinstance(instance, componentmodel::InPort)

@given(instance=componentmodel::Property_strategy)
@settings(max_examples=50)
def test_componentmodel::property_instantiation(instance):
    assert isinstance(instance, componentmodel::Property)

@given(instance=componentmodel::Property_strategy)
def test_componentmodel::property_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=componentmodel::Property_strategy)
def test_componentmodel::property_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=componentmodel::Property_strategy)
def test_componentmodel::property_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=componentmodel::Property_strategy)
def test_componentmodel::property_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=componentmodel::EnumProperty_strategy)
@settings(max_examples=50)
def test_componentmodel::enumproperty_instantiation(instance):
    assert isinstance(instance, componentmodel::EnumProperty)

@given(instance=componentmodel::EnumProperty_strategy)
def test_componentmodel::enumproperty_literalValue_type(instance):
    assert isinstance(instance.literalValue, str)


@given(instance=componentmodel::EnumProperty_strategy)
def test_componentmodel::enumproperty_literalValue_setter(instance):
    original = instance.literalValue
    instance.literalValue = original
    assert instance.literalValue == original

@given(instance=componentmodel::NumericProperty_strategy)
@settings(max_examples=50)
def test_componentmodel::numericproperty_instantiation(instance):
    assert isinstance(instance, componentmodel::NumericProperty)

@given(instance=componentmodel::NumericProperty_strategy)
def test_componentmodel::numericproperty_maxValue_type(instance):
    assert isinstance(instance.maxValue, float)


@given(instance=componentmodel::NumericProperty_strategy)
def test_componentmodel::numericproperty_maxValue_setter(instance):
    original = instance.maxValue
    instance.maxValue = original
    assert instance.maxValue == original

@given(instance=componentmodel::NumericProperty_strategy)
def test_componentmodel::numericproperty_defaultValue_type(instance):
    assert isinstance(instance.defaultValue, float)


@given(instance=componentmodel::NumericProperty_strategy)
def test_componentmodel::numericproperty_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original

@given(instance=componentmodel::NumericProperty_strategy)
def test_componentmodel::numericproperty_minValue_type(instance):
    assert isinstance(instance.minValue, float)


@given(instance=componentmodel::NumericProperty_strategy)
def test_componentmodel::numericproperty_minValue_setter(instance):
    original = instance.minValue
    instance.minValue = original
    assert instance.minValue == original

@given(instance=Component_strategy)
@settings(max_examples=50)
def test_component_instantiation(instance):
    assert isinstance(instance, Component)

@given(instance=componentmodel::CompositeComponent_strategy)
@settings(max_examples=50)
def test_componentmodel::compositecomponent_instantiation(instance):
    assert isinstance(instance, componentmodel::CompositeComponent)

@given(instance=componentmodel::PrimitiveComponent_strategy)
@settings(max_examples=50)
def test_componentmodel::primitivecomponent_instantiation(instance):
    assert isinstance(instance, componentmodel::PrimitiveComponent)

@given(instance=componentmodel::Port_strategy)
@settings(max_examples=50)
def test_componentmodel::port_instantiation(instance):
    assert isinstance(instance, componentmodel::Port)

@given(instance=componentmodel::Port_strategy)
def test_componentmodel::port_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=componentmodel::Port_strategy)
def test_componentmodel::port_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=componentmodel::Port_strategy)
def test_componentmodel::port_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=componentmodel::Port_strategy)
def test_componentmodel::port_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=componentmodel::Port_strategy)
def test_componentmodel::port_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=componentmodel::Port_strategy)
def test_componentmodel::port_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=componentmodel::Port_strategy)
def test_componentmodel::port_typePackage_type(instance):
    assert isinstance(instance.typePackage, str)


@given(instance=componentmodel::Port_strategy)
def test_componentmodel::port_typePackage_setter(instance):
    original = instance.typePackage
    instance.typePackage = original
    assert instance.typePackage == original

@given(instance=componentmodel::Component_strategy)
@settings(max_examples=50)
def test_componentmodel::component_instantiation(instance):
    assert isinstance(instance, componentmodel::Component)

@given(instance=componentmodel::Component_strategy)
def test_componentmodel::component_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=componentmodel::Component_strategy)
def test_componentmodel::component_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=componentmodel::Component_strategy)
def test_componentmodel::component_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=componentmodel::Component_strategy)
def test_componentmodel::component_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original
