import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ElectronicDevice,
    component::diagram::Sensor,
    MechanicalDevice,
    component::diagram::Actuator,
    HardwareComponent,
    component::diagram::MechanicalDevice,
    component::diagram::ElectronicDevice,
    ComponentType,
    component::diagram::SoftwareComponent,
    component::diagram::HardwareComponent,
    IDBase,
    component::diagram::Connector,
    component::diagram::PortInstance,
    component::diagram::Architecture,
    component::diagram::ComponentInstance,
    component::diagram::PortType,
    component::diagram::ComponentType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_electronicdevice_is_not_abstract():
    assert not inspect.isabstract(ElectronicDevice)


def test_electronicdevice_constructor_exists():
    assert callable(ElectronicDevice.__init__)


def test_electronicdevice_constructor_args():
    sig = inspect.signature(ElectronicDevice.__init__)
    params = list(sig.parameters.keys())



def test_component::diagram::sensor_is_not_abstract():
    assert not inspect.isabstract(component::diagram::Sensor)


def test_component::diagram::sensor_constructor_exists():
    assert callable(component::diagram::Sensor.__init__)


def test_component::diagram::sensor_constructor_args():
    sig = inspect.signature(component::diagram::Sensor.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_component::diagram::sensor_has_type():
    assert hasattr(component::diagram::Sensor, "type")
    descriptor = None
    for klass in component::diagram::Sensor.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_mechanicaldevice_is_not_abstract():
    assert not inspect.isabstract(MechanicalDevice)


def test_mechanicaldevice_constructor_exists():
    assert callable(MechanicalDevice.__init__)


def test_mechanicaldevice_constructor_args():
    sig = inspect.signature(MechanicalDevice.__init__)
    params = list(sig.parameters.keys())



def test_component::diagram::actuator_is_not_abstract():
    assert not inspect.isabstract(component::diagram::Actuator)


def test_component::diagram::actuator_constructor_exists():
    assert callable(component::diagram::Actuator.__init__)


def test_component::diagram::actuator_constructor_args():
    sig = inspect.signature(component::diagram::Actuator.__init__)
    params = list(sig.parameters.keys())



def test_hardwarecomponent_is_not_abstract():
    assert not inspect.isabstract(HardwareComponent)


def test_hardwarecomponent_constructor_exists():
    assert callable(HardwareComponent.__init__)


def test_hardwarecomponent_constructor_args():
    sig = inspect.signature(HardwareComponent.__init__)
    params = list(sig.parameters.keys())



def test_component::diagram::mechanicaldevice_is_not_abstract():
    assert not inspect.isabstract(component::diagram::MechanicalDevice)


def test_component::diagram::mechanicaldevice_constructor_exists():
    assert callable(component::diagram::MechanicalDevice.__init__)


def test_component::diagram::mechanicaldevice_constructor_args():
    sig = inspect.signature(component::diagram::MechanicalDevice.__init__)
    params = list(sig.parameters.keys())



def test_component::diagram::electronicdevice_is_not_abstract():
    assert not inspect.isabstract(component::diagram::ElectronicDevice)


def test_component::diagram::electronicdevice_constructor_exists():
    assert callable(component::diagram::ElectronicDevice.__init__)


def test_component::diagram::electronicdevice_constructor_args():
    sig = inspect.signature(component::diagram::ElectronicDevice.__init__)
    params = list(sig.parameters.keys())



def test_componenttype_is_not_abstract():
    assert not inspect.isabstract(ComponentType)


def test_componenttype_constructor_exists():
    assert callable(ComponentType.__init__)


def test_componenttype_constructor_args():
    sig = inspect.signature(ComponentType.__init__)
    params = list(sig.parameters.keys())



def test_component::diagram::softwarecomponent_is_not_abstract():
    assert not inspect.isabstract(component::diagram::SoftwareComponent)


def test_component::diagram::softwarecomponent_constructor_exists():
    assert callable(component::diagram::SoftwareComponent.__init__)


def test_component::diagram::softwarecomponent_constructor_args():
    sig = inspect.signature(component::diagram::SoftwareComponent.__init__)
    params = list(sig.parameters.keys())



def test_component::diagram::hardwarecomponent_is_not_abstract():
    assert not inspect.isabstract(component::diagram::HardwareComponent)


def test_component::diagram::hardwarecomponent_constructor_exists():
    assert callable(component::diagram::HardwareComponent.__init__)


def test_component::diagram::hardwarecomponent_constructor_args():
    sig = inspect.signature(component::diagram::HardwareComponent.__init__)
    params = list(sig.parameters.keys())
    assert "powerSupply" in params, "Missing parameter 'powerSupply'"

def test_component::diagram::hardwarecomponent_has_powerSupply():
    assert hasattr(component::diagram::HardwareComponent, "powerSupply")
    descriptor = None
    for klass in component::diagram::HardwareComponent.__mro__:
        if "powerSupply" in klass.__dict__:
            descriptor = klass.__dict__["powerSupply"]
            break
    assert isinstance(descriptor, property)



def test_idbase_is_not_abstract():
    assert not inspect.isabstract(IDBase)


def test_idbase_constructor_exists():
    assert callable(IDBase.__init__)


def test_idbase_constructor_args():
    sig = inspect.signature(IDBase.__init__)
    params = list(sig.parameters.keys())



def test_component::diagram::connector_is_not_abstract():
    assert not inspect.isabstract(component::diagram::Connector)


def test_component::diagram::connector_constructor_exists():
    assert callable(component::diagram::Connector.__init__)


def test_component::diagram::connector_constructor_args():
    sig = inspect.signature(component::diagram::Connector.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_component::diagram::connector_has_name():
    assert hasattr(component::diagram::Connector, "name")
    descriptor = None
    for klass in component::diagram::Connector.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_component::diagram::portinstance_is_not_abstract():
    assert not inspect.isabstract(component::diagram::PortInstance)


def test_component::diagram::portinstance_constructor_exists():
    assert callable(component::diagram::PortInstance.__init__)


def test_component::diagram::portinstance_constructor_args():
    sig = inspect.signature(component::diagram::PortInstance.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_component::diagram::portinstance_has_name():
    assert hasattr(component::diagram::PortInstance, "name")
    descriptor = None
    for klass in component::diagram::PortInstance.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_component::diagram::architecture_is_not_abstract():
    assert not inspect.isabstract(component::diagram::Architecture)


def test_component::diagram::architecture_constructor_exists():
    assert callable(component::diagram::Architecture.__init__)


def test_component::diagram::architecture_constructor_args():
    sig = inspect.signature(component::diagram::Architecture.__init__)
    params = list(sig.parameters.keys())



def test_component::diagram::componentinstance_is_not_abstract():
    assert not inspect.isabstract(component::diagram::ComponentInstance)


def test_component::diagram::componentinstance_constructor_exists():
    assert callable(component::diagram::ComponentInstance.__init__)


def test_component::diagram::componentinstance_constructor_args():
    sig = inspect.signature(component::diagram::ComponentInstance.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "name" in params, "Missing parameter 'name'"

def test_component::diagram::componentinstance_has_version():
    assert hasattr(component::diagram::ComponentInstance, "version")
    descriptor = None
    for klass in component::diagram::ComponentInstance.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_component::diagram::componentinstance_has_name():
    assert hasattr(component::diagram::ComponentInstance, "name")
    descriptor = None
    for klass in component::diagram::ComponentInstance.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_component::diagram::porttype_is_not_abstract():
    assert not inspect.isabstract(component::diagram::PortType)


def test_component::diagram::porttype_constructor_exists():
    assert callable(component::diagram::PortType.__init__)


def test_component::diagram::porttype_constructor_args():
    sig = inspect.signature(component::diagram::PortType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_component::diagram::porttype_has_name():
    assert hasattr(component::diagram::PortType, "name")
    descriptor = None
    for klass in component::diagram::PortType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_component::diagram::componenttype_is_not_abstract():
    assert not inspect.isabstract(component::diagram::ComponentType)


def test_component::diagram::componenttype_constructor_exists():
    assert callable(component::diagram::ComponentType.__init__)


def test_component::diagram::componenttype_constructor_args():
    sig = inspect.signature(component::diagram::ComponentType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_component::diagram::componenttype_has_name():
    assert hasattr(component::diagram::ComponentType, "name")
    descriptor = None
    for klass in component::diagram::ComponentType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
ElectronicDevice_strategy = st.builds(
    ElectronicDevice,
)
component::diagram::Sensor_strategy = st.builds(
    component::diagram::Sensor,
    type=
        safe_text
)
MechanicalDevice_strategy = st.builds(
    MechanicalDevice,
)
component::diagram::Actuator_strategy = st.builds(
    component::diagram::Actuator,
)
HardwareComponent_strategy = st.builds(
    HardwareComponent,
)
component::diagram::MechanicalDevice_strategy = st.builds(
    component::diagram::MechanicalDevice,
)
component::diagram::ElectronicDevice_strategy = st.builds(
    component::diagram::ElectronicDevice,
)
ComponentType_strategy = st.builds(
    ComponentType,
)
component::diagram::SoftwareComponent_strategy = st.builds(
    component::diagram::SoftwareComponent,
)
component::diagram::HardwareComponent_strategy = st.builds(
    component::diagram::HardwareComponent,
    powerSupply=
        safe_text
)
IDBase_strategy = st.builds(
    IDBase,
)
component::diagram::Connector_strategy = st.builds(
    component::diagram::Connector,
    name=
        safe_text
)
component::diagram::PortInstance_strategy = st.builds(
    component::diagram::PortInstance,
    name=
        safe_text
)
component::diagram::Architecture_strategy = st.builds(
    component::diagram::Architecture,
)
component::diagram::ComponentInstance_strategy = st.builds(
    component::diagram::ComponentInstance,
    version=
        st.integers(),
    name=
        safe_text
)
component::diagram::PortType_strategy = st.builds(
    component::diagram::PortType,
    name=
        safe_text
)
component::diagram::ComponentType_strategy = st.builds(
    component::diagram::ComponentType,
    name=
        safe_text
)

@given(instance=ElectronicDevice_strategy)
@settings(max_examples=50)
def test_electronicdevice_instantiation(instance):
    assert isinstance(instance, ElectronicDevice)

@given(instance=component::diagram::Sensor_strategy)
@settings(max_examples=50)
def test_component::diagram::sensor_instantiation(instance):
    assert isinstance(instance, component::diagram::Sensor)

@given(instance=component::diagram::Sensor_strategy)
def test_component::diagram::sensor_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=component::diagram::Sensor_strategy)
def test_component::diagram::sensor_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=MechanicalDevice_strategy)
@settings(max_examples=50)
def test_mechanicaldevice_instantiation(instance):
    assert isinstance(instance, MechanicalDevice)

@given(instance=component::diagram::Actuator_strategy)
@settings(max_examples=50)
def test_component::diagram::actuator_instantiation(instance):
    assert isinstance(instance, component::diagram::Actuator)

@given(instance=HardwareComponent_strategy)
@settings(max_examples=50)
def test_hardwarecomponent_instantiation(instance):
    assert isinstance(instance, HardwareComponent)

@given(instance=component::diagram::MechanicalDevice_strategy)
@settings(max_examples=50)
def test_component::diagram::mechanicaldevice_instantiation(instance):
    assert isinstance(instance, component::diagram::MechanicalDevice)

@given(instance=component::diagram::ElectronicDevice_strategy)
@settings(max_examples=50)
def test_component::diagram::electronicdevice_instantiation(instance):
    assert isinstance(instance, component::diagram::ElectronicDevice)

@given(instance=ComponentType_strategy)
@settings(max_examples=50)
def test_componenttype_instantiation(instance):
    assert isinstance(instance, ComponentType)

@given(instance=component::diagram::SoftwareComponent_strategy)
@settings(max_examples=50)
def test_component::diagram::softwarecomponent_instantiation(instance):
    assert isinstance(instance, component::diagram::SoftwareComponent)

@given(instance=component::diagram::HardwareComponent_strategy)
@settings(max_examples=50)
def test_component::diagram::hardwarecomponent_instantiation(instance):
    assert isinstance(instance, component::diagram::HardwareComponent)

@given(instance=component::diagram::HardwareComponent_strategy)
def test_component::diagram::hardwarecomponent_powerSupply_type(instance):
    assert isinstance(instance.powerSupply, str)


@given(instance=component::diagram::HardwareComponent_strategy)
def test_component::diagram::hardwarecomponent_powerSupply_setter(instance):
    original = instance.powerSupply
    instance.powerSupply = original
    assert instance.powerSupply == original

@given(instance=IDBase_strategy)
@settings(max_examples=50)
def test_idbase_instantiation(instance):
    assert isinstance(instance, IDBase)

@given(instance=component::diagram::Connector_strategy)
@settings(max_examples=50)
def test_component::diagram::connector_instantiation(instance):
    assert isinstance(instance, component::diagram::Connector)

@given(instance=component::diagram::Connector_strategy)
def test_component::diagram::connector_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=component::diagram::Connector_strategy)
def test_component::diagram::connector_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=component::diagram::PortInstance_strategy)
@settings(max_examples=50)
def test_component::diagram::portinstance_instantiation(instance):
    assert isinstance(instance, component::diagram::PortInstance)

@given(instance=component::diagram::PortInstance_strategy)
def test_component::diagram::portinstance_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=component::diagram::PortInstance_strategy)
def test_component::diagram::portinstance_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=component::diagram::Architecture_strategy)
@settings(max_examples=50)
def test_component::diagram::architecture_instantiation(instance):
    assert isinstance(instance, component::diagram::Architecture)

@given(instance=component::diagram::ComponentInstance_strategy)
@settings(max_examples=50)
def test_component::diagram::componentinstance_instantiation(instance):
    assert isinstance(instance, component::diagram::ComponentInstance)

@given(instance=component::diagram::ComponentInstance_strategy)
def test_component::diagram::componentinstance_version_type(instance):
    assert isinstance(instance.version, int)


@given(instance=component::diagram::ComponentInstance_strategy)
def test_component::diagram::componentinstance_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=component::diagram::ComponentInstance_strategy)
def test_component::diagram::componentinstance_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=component::diagram::ComponentInstance_strategy)
def test_component::diagram::componentinstance_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=component::diagram::PortType_strategy)
@settings(max_examples=50)
def test_component::diagram::porttype_instantiation(instance):
    assert isinstance(instance, component::diagram::PortType)

@given(instance=component::diagram::PortType_strategy)
def test_component::diagram::porttype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=component::diagram::PortType_strategy)
def test_component::diagram::porttype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=component::diagram::ComponentType_strategy)
@settings(max_examples=50)
def test_component::diagram::componenttype_instantiation(instance):
    assert isinstance(instance, component::diagram::ComponentType)

@given(instance=component::diagram::ComponentType_strategy)
def test_component::diagram::componenttype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=component::diagram::ComponentType_strategy)
def test_component::diagram::componenttype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
