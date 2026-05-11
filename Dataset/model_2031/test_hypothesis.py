import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ioT::metamodel::Entity,
    Evaluators,
    ioT::metamodel::ScriptEvaluator,
    ioT::metamodel::JavaEvaluator,
    ioT::metamodel::Evaluators,
    ioT::metamodel::Operations,
    ioT::metamodel::AtomicDataAttributes,
    ioT::metamodel::DataStreamAttributes,
    ioT::metamodel::DataStreams,
    ioT::metamodel::AtomicData,
    ioT::metamodel::Reference::Monitor,
    ioT::metamodel::Policy::Repository,
    User,
    Digital::Artifact,
    ioT::metamodel::Passive::Digital::Artifact,
    ioT::metamodel::Active::Digital::Artifact,
    ioT::metamodel::Digital::Artifact,
    ioT::metamodel::Service::Resource,
    ioT::metamodel::Device::Resource,
    InformationResource,
    ioT::metamodel::Network::Resource,
    Passive::Digital::Artifact,
    Active::Digital::Artifact,
    ioT::metamodel::Property,
    ioT::metamodel::PhysicalThing,
    ioT::metamodel::Fog,
    ioT::metamodel::VirtualThing,
    Entity,
    ioT::metamodel::User,
    ioT::metamodel::Thing,
    ioT::metamodel::Attribute,
    ioT::metamodel::Information,
    ioT::metamodel::Port,
    ioT::metamodel::Human::User,
    ioT::metamodel::Transition,
    DeviceState,
    ioT::metamodel::CompositeState,
    Actuator,
    ioT::metamodel::ExternalActuator,
    ioT::metamodel::DeviceActuator,
    Sensor,
    ioT::metamodel::DeviceSensor,
    ioT::metamodel::ExternalSensor,
    ioT::metamodel::Action,
    ioT::metamodel::Database,
    ioT::metamodel::Cloud,
    ioT::metamodel::FogNode,
    Device,
    ioT::metamodel::Tag,
    ioT::metamodel::Sensor,
    ioT::metamodel::Actuator,
    ioT::metamodel::On::Device::Resource,
    ioT::metamodel::Communicator,
    ioT::metamodel::DeviceState,
    ioT::metamodel::Rule,
    PhysicalThing,
    ioT::metamodel::Fog::Services,
    ioT::metamodel::Analytics::Engine,
    ioT::metamodel::Container,
    ioT::metamodel::VM,
    ioT::metamodel::Authorizor,
    ioT::metamodel::Device,
    ioT::metamodel::InformationResource,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_iot::metamodel::entity_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::Entity)


def test_iot::metamodel::entity_constructor_exists():
    assert callable(ioT::metamodel::Entity.__init__)


def test_iot::metamodel::entity_constructor_args():
    sig = inspect.signature(ioT::metamodel::Entity.__init__)
    params = list(sig.parameters.keys())



def test_evaluators_is_not_abstract():
    assert not inspect.isabstract(Evaluators)


def test_evaluators_constructor_exists():
    assert callable(Evaluators.__init__)


def test_evaluators_constructor_args():
    sig = inspect.signature(Evaluators.__init__)
    params = list(sig.parameters.keys())



def test_iot::metamodel::scriptevaluator_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::ScriptEvaluator)


def test_iot::metamodel::scriptevaluator_constructor_exists():
    assert callable(ioT::metamodel::ScriptEvaluator.__init__)


def test_iot::metamodel::scriptevaluator_constructor_args():
    sig = inspect.signature(ioT::metamodel::ScriptEvaluator.__init__)
    params = list(sig.parameters.keys())



def test_iot::metamodel::javaevaluator_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::JavaEvaluator)


def test_iot::metamodel::javaevaluator_constructor_exists():
    assert callable(ioT::metamodel::JavaEvaluator.__init__)


def test_iot::metamodel::javaevaluator_constructor_args():
    sig = inspect.signature(ioT::metamodel::JavaEvaluator.__init__)
    params = list(sig.parameters.keys())



def test_iot::metamodel::evaluators_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::Evaluators)


def test_iot::metamodel::evaluators_constructor_exists():
    assert callable(ioT::metamodel::Evaluators.__init__)


def test_iot::metamodel::evaluators_constructor_args():
    sig = inspect.signature(ioT::metamodel::Evaluators.__init__)
    params = list(sig.parameters.keys())



def test_iot::metamodel::operations_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::Operations)


def test_iot::metamodel::operations_constructor_exists():
    assert callable(ioT::metamodel::Operations.__init__)


def test_iot::metamodel::operations_constructor_args():
    sig = inspect.signature(ioT::metamodel::Operations.__init__)
    params = list(sig.parameters.keys())



def test_iot::metamodel::atomicdataattributes_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::AtomicDataAttributes)


def test_iot::metamodel::atomicdataattributes_constructor_exists():
    assert callable(ioT::metamodel::AtomicDataAttributes.__init__)


def test_iot::metamodel::atomicdataattributes_constructor_args():
    sig = inspect.signature(ioT::metamodel::AtomicDataAttributes.__init__)
    params = list(sig.parameters.keys())
    assert "DeviceID" in params, "Missing parameter 'DeviceID'"
    assert "DataEncoding" in params, "Missing parameter 'DataEncoding'"

def test_iot::metamodel::atomicdataattributes_has_DeviceID():
    assert hasattr(ioT::metamodel::AtomicDataAttributes, "DeviceID")
    descriptor = None
    for klass in ioT::metamodel::AtomicDataAttributes.__mro__:
        if "DeviceID" in klass.__dict__:
            descriptor = klass.__dict__["DeviceID"]
            break
    assert isinstance(descriptor, property)

def test_iot::metamodel::atomicdataattributes_has_DataEncoding():
    assert hasattr(ioT::metamodel::AtomicDataAttributes, "DataEncoding")
    descriptor = None
    for klass in ioT::metamodel::AtomicDataAttributes.__mro__:
        if "DataEncoding" in klass.__dict__:
            descriptor = klass.__dict__["DataEncoding"]
            break
    assert isinstance(descriptor, property)



def test_iot::metamodel::datastreamattributes_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::DataStreamAttributes)


def test_iot::metamodel::datastreamattributes_constructor_exists():
    assert callable(ioT::metamodel::DataStreamAttributes.__init__)


def test_iot::metamodel::datastreamattributes_constructor_args():
    sig = inspect.signature(ioT::metamodel::DataStreamAttributes.__init__)
    params = list(sig.parameters.keys())
    assert "MaxBitrate" in params, "Missing parameter 'MaxBitrate'"
    assert "Timestamp" in params, "Missing parameter 'Timestamp'"
    assert "DataFormat" in params, "Missing parameter 'DataFormat'"
    assert "DeviceID" in params, "Missing parameter 'DeviceID'"
    assert "DataEncoding" in params, "Missing parameter 'DataEncoding'"
    assert "Description" in params, "Missing parameter 'Description'"
    assert "MeanBitRate" in params, "Missing parameter 'MeanBitRate'"

def test_iot::metamodel::datastreamattributes_has_MaxBitrate():
    assert hasattr(ioT::metamodel::DataStreamAttributes, "MaxBitrate")
    descriptor = None
    for klass in ioT::metamodel::DataStreamAttributes.__mro__:
        if "MaxBitrate" in klass.__dict__:
            descriptor = klass.__dict__["MaxBitrate"]
            break
    assert isinstance(descriptor, property)

def test_iot::metamodel::datastreamattributes_has_Timestamp():
    assert hasattr(ioT::metamodel::DataStreamAttributes, "Timestamp")
    descriptor = None
    for klass in ioT::metamodel::DataStreamAttributes.__mro__:
        if "Timestamp" in klass.__dict__:
            descriptor = klass.__dict__["Timestamp"]
            break
    assert isinstance(descriptor, property)

def test_iot::metamodel::datastreamattributes_has_DataFormat():
    assert hasattr(ioT::metamodel::DataStreamAttributes, "DataFormat")
    descriptor = None
    for klass in ioT::metamodel::DataStreamAttributes.__mro__:
        if "DataFormat" in klass.__dict__:
            descriptor = klass.__dict__["DataFormat"]
            break
    assert isinstance(descriptor, property)

def test_iot::metamodel::datastreamattributes_has_DeviceID():
    assert hasattr(ioT::metamodel::DataStreamAttributes, "DeviceID")
    descriptor = None
    for klass in ioT::metamodel::DataStreamAttributes.__mro__:
        if "DeviceID" in klass.__dict__:
            descriptor = klass.__dict__["DeviceID"]
            break
    assert isinstance(descriptor, property)

def test_iot::metamodel::datastreamattributes_has_DataEncoding():
    assert hasattr(ioT::metamodel::DataStreamAttributes, "DataEncoding")
    descriptor = None
    for klass in ioT::metamodel::DataStreamAttributes.__mro__:
        if "DataEncoding" in klass.__dict__:
            descriptor = klass.__dict__["DataEncoding"]
            break
    assert isinstance(descriptor, property)

def test_iot::metamodel::datastreamattributes_has_Description():
    assert hasattr(ioT::metamodel::DataStreamAttributes, "Description")
    descriptor = None
    for klass in ioT::metamodel::DataStreamAttributes.__mro__:
        if "Description" in klass.__dict__:
            descriptor = klass.__dict__["Description"]
            break
    assert isinstance(descriptor, property)

def test_iot::metamodel::datastreamattributes_has_MeanBitRate():
    assert hasattr(ioT::metamodel::DataStreamAttributes, "MeanBitRate")
    descriptor = None
    for klass in ioT::metamodel::DataStreamAttributes.__mro__:
        if "MeanBitRate" in klass.__dict__:
            descriptor = klass.__dict__["MeanBitRate"]
            break
    assert isinstance(descriptor, property)



def test_iot::metamodel::datastreams_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::DataStreams)


def test_iot::metamodel::datastreams_constructor_exists():
    assert callable(ioT::metamodel::DataStreams.__init__)


def test_iot::metamodel::datastreams_constructor_args():
    sig = inspect.signature(ioT::metamodel::DataStreams.__init__)
    params = list(sig.parameters.keys())



def test_iot::metamodel::atomicdata_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::AtomicData)


def test_iot::metamodel::atomicdata_constructor_exists():
    assert callable(ioT::metamodel::AtomicData.__init__)


def test_iot::metamodel::atomicdata_constructor_args():
    sig = inspect.signature(ioT::metamodel::AtomicData.__init__)
    params = list(sig.parameters.keys())



def test_iot::metamodel::reference::monitor_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::Reference::Monitor)


def test_iot::metamodel::reference::monitor_constructor_exists():
    assert callable(ioT::metamodel::Reference::Monitor.__init__)


def test_iot::metamodel::reference::monitor_constructor_args():
    sig = inspect.signature(ioT::metamodel::Reference::Monitor.__init__)
    params = list(sig.parameters.keys())



def test_iot::metamodel::policy::repository_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::Policy::Repository)


def test_iot::metamodel::policy::repository_constructor_exists():
    assert callable(ioT::metamodel::Policy::Repository.__init__)


def test_iot::metamodel::policy::repository_constructor_args():
    sig = inspect.signature(ioT::metamodel::Policy::Repository.__init__)
    params = list(sig.parameters.keys())



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())



def test_digital::artifact_is_not_abstract():
    assert not inspect.isabstract(Digital::Artifact)


def test_digital::artifact_constructor_exists():
    assert callable(Digital::Artifact.__init__)


def test_digital::artifact_constructor_args():
    sig = inspect.signature(Digital::Artifact.__init__)
    params = list(sig.parameters.keys())



def test_iot::metamodel::passive::digital::artifact_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::Passive::Digital::Artifact)


def test_iot::metamodel::passive::digital::artifact_constructor_exists():
    assert callable(ioT::metamodel::Passive::Digital::Artifact.__init__)


def test_iot::metamodel::passive::digital::artifact_constructor_args():
    sig = inspect.signature(ioT::metamodel::Passive::Digital::Artifact.__init__)
    params = list(sig.parameters.keys())



def test_iot::metamodel::active::digital::artifact_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::Active::Digital::Artifact)


def test_iot::metamodel::active::digital::artifact_constructor_exists():
    assert callable(ioT::metamodel::Active::Digital::Artifact.__init__)


def test_iot::metamodel::active::digital::artifact_constructor_args():
    sig = inspect.signature(ioT::metamodel::Active::Digital::Artifact.__init__)
    params = list(sig.parameters.keys())



def test_iot::metamodel::digital::artifact_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::Digital::Artifact)


def test_iot::metamodel::digital::artifact_constructor_exists():
    assert callable(ioT::metamodel::Digital::Artifact.__init__)


def test_iot::metamodel::digital::artifact_constructor_args():
    sig = inspect.signature(ioT::metamodel::Digital::Artifact.__init__)
    params = list(sig.parameters.keys())



def test_iot::metamodel::service::resource_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::Service::Resource)


def test_iot::metamodel::service::resource_constructor_exists():
    assert callable(ioT::metamodel::Service::Resource.__init__)


def test_iot::metamodel::service::resource_constructor_args():
    sig = inspect.signature(ioT::metamodel::Service::Resource.__init__)
    params = list(sig.parameters.keys())



def test_iot::metamodel::device::resource_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::Device::Resource)


def test_iot::metamodel::device::resource_constructor_exists():
    assert callable(ioT::metamodel::Device::Resource.__init__)


def test_iot::metamodel::device::resource_constructor_args():
    sig = inspect.signature(ioT::metamodel::Device::Resource.__init__)
    params = list(sig.parameters.keys())



def test_informationresource_is_not_abstract():
    assert not inspect.isabstract(InformationResource)


def test_informationresource_constructor_exists():
    assert callable(InformationResource.__init__)


def test_informationresource_constructor_args():
    sig = inspect.signature(InformationResource.__init__)
    params = list(sig.parameters.keys())



def test_iot::metamodel::network::resource_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::Network::Resource)


def test_iot::metamodel::network::resource_constructor_exists():
    assert callable(ioT::metamodel::Network::Resource.__init__)


def test_iot::metamodel::network::resource_constructor_args():
    sig = inspect.signature(ioT::metamodel::Network::Resource.__init__)
    params = list(sig.parameters.keys())



def test_passive::digital::artifact_is_not_abstract():
    assert not inspect.isabstract(Passive::Digital::Artifact)


def test_passive::digital::artifact_constructor_exists():
    assert callable(Passive::Digital::Artifact.__init__)


def test_passive::digital::artifact_constructor_args():
    sig = inspect.signature(Passive::Digital::Artifact.__init__)
    params = list(sig.parameters.keys())



def test_active::digital::artifact_is_not_abstract():
    assert not inspect.isabstract(Active::Digital::Artifact)


def test_active::digital::artifact_constructor_exists():
    assert callable(Active::Digital::Artifact.__init__)


def test_active::digital::artifact_constructor_args():
    sig = inspect.signature(Active::Digital::Artifact.__init__)
    params = list(sig.parameters.keys())



def test_iot::metamodel::property_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::Property)


def test_iot::metamodel::property_constructor_exists():
    assert callable(ioT::metamodel::Property.__init__)


def test_iot::metamodel::property_constructor_args():
    sig = inspect.signature(ioT::metamodel::Property.__init__)
    params = list(sig.parameters.keys())
    assert "changeable" in params, "Missing parameter 'changeable'"

def test_iot::metamodel::property_has_changeable():
    assert hasattr(ioT::metamodel::Property, "changeable")
    descriptor = None
    for klass in ioT::metamodel::Property.__mro__:
        if "changeable" in klass.__dict__:
            descriptor = klass.__dict__["changeable"]
            break
    assert isinstance(descriptor, property)



def test_iot::metamodel::physicalthing_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::PhysicalThing)


def test_iot::metamodel::physicalthing_constructor_exists():
    assert callable(ioT::metamodel::PhysicalThing.__init__)


def test_iot::metamodel::physicalthing_constructor_args():
    sig = inspect.signature(ioT::metamodel::PhysicalThing.__init__)
    params = list(sig.parameters.keys())



def test_iot::metamodel::fog_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::Fog)


def test_iot::metamodel::fog_constructor_exists():
    assert callable(ioT::metamodel::Fog.__init__)


def test_iot::metamodel::fog_constructor_args():
    sig = inspect.signature(ioT::metamodel::Fog.__init__)
    params = list(sig.parameters.keys())



def test_iot::metamodel::virtualthing_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::VirtualThing)


def test_iot::metamodel::virtualthing_constructor_exists():
    assert callable(ioT::metamodel::VirtualThing.__init__)


def test_iot::metamodel::virtualthing_constructor_args():
    sig = inspect.signature(ioT::metamodel::VirtualThing.__init__)
    params = list(sig.parameters.keys())
    assert "URI" in params, "Missing parameter 'URI'"

def test_iot::metamodel::virtualthing_has_URI():
    assert hasattr(ioT::metamodel::VirtualThing, "URI")
    descriptor = None
    for klass in ioT::metamodel::VirtualThing.__mro__:
        if "URI" in klass.__dict__:
            descriptor = klass.__dict__["URI"]
            break
    assert isinstance(descriptor, property)



def test_entity_is_not_abstract():
    assert not inspect.isabstract(Entity)


def test_entity_constructor_exists():
    assert callable(Entity.__init__)


def test_entity_constructor_args():
    sig = inspect.signature(Entity.__init__)
    params = list(sig.parameters.keys())



def test_iot::metamodel::user_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::User)


def test_iot::metamodel::user_constructor_exists():
    assert callable(ioT::metamodel::User.__init__)


def test_iot::metamodel::user_constructor_args():
    sig = inspect.signature(ioT::metamodel::User.__init__)
    params = list(sig.parameters.keys())



def test_iot::metamodel::thing_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::Thing)


def test_iot::metamodel::thing_constructor_exists():
    assert callable(ioT::metamodel::Thing.__init__)


def test_iot::metamodel::thing_constructor_args():
    sig = inspect.signature(ioT::metamodel::Thing.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iot::metamodel::thing_has_name():
    assert hasattr(ioT::metamodel::Thing, "name")
    descriptor = None
    for klass in ioT::metamodel::Thing.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iot::metamodel::attribute_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::Attribute)


def test_iot::metamodel::attribute_constructor_exists():
    assert callable(ioT::metamodel::Attribute.__init__)


def test_iot::metamodel::attribute_constructor_args():
    sig = inspect.signature(ioT::metamodel::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "Type" in params, "Missing parameter 'Type'"

def test_iot::metamodel::attribute_has_name():
    assert hasattr(ioT::metamodel::Attribute, "name")
    descriptor = None
    for klass in ioT::metamodel::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_iot::metamodel::attribute_has_Type():
    assert hasattr(ioT::metamodel::Attribute, "Type")
    descriptor = None
    for klass in ioT::metamodel::Attribute.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)



def test_iot::metamodel::information_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::Information)


def test_iot::metamodel::information_constructor_exists():
    assert callable(ioT::metamodel::Information.__init__)


def test_iot::metamodel::information_constructor_args():
    sig = inspect.signature(ioT::metamodel::Information.__init__)
    params = list(sig.parameters.keys())



def test_iot::metamodel::port_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::Port)


def test_iot::metamodel::port_constructor_exists():
    assert callable(ioT::metamodel::Port.__init__)


def test_iot::metamodel::port_constructor_args():
    sig = inspect.signature(ioT::metamodel::Port.__init__)
    params = list(sig.parameters.keys())



def test_iot::metamodel::human::user_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::Human::User)


def test_iot::metamodel::human::user_constructor_exists():
    assert callable(ioT::metamodel::Human::User.__init__)


def test_iot::metamodel::human::user_constructor_args():
    sig = inspect.signature(ioT::metamodel::Human::User.__init__)
    params = list(sig.parameters.keys())



def test_iot::metamodel::transition_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::Transition)


def test_iot::metamodel::transition_constructor_exists():
    assert callable(ioT::metamodel::Transition.__init__)


def test_iot::metamodel::transition_constructor_args():
    sig = inspect.signature(ioT::metamodel::Transition.__init__)
    params = list(sig.parameters.keys())



def test_devicestate_is_not_abstract():
    assert not inspect.isabstract(DeviceState)


def test_devicestate_constructor_exists():
    assert callable(DeviceState.__init__)


def test_devicestate_constructor_args():
    sig = inspect.signature(DeviceState.__init__)
    params = list(sig.parameters.keys())



def test_iot::metamodel::compositestate_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::CompositeState)


def test_iot::metamodel::compositestate_constructor_exists():
    assert callable(ioT::metamodel::CompositeState.__init__)


def test_iot::metamodel::compositestate_constructor_args():
    sig = inspect.signature(ioT::metamodel::CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_actuator_is_not_abstract():
    assert not inspect.isabstract(Actuator)


def test_actuator_constructor_exists():
    assert callable(Actuator.__init__)


def test_actuator_constructor_args():
    sig = inspect.signature(Actuator.__init__)
    params = list(sig.parameters.keys())



def test_iot::metamodel::externalactuator_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::ExternalActuator)


def test_iot::metamodel::externalactuator_constructor_exists():
    assert callable(ioT::metamodel::ExternalActuator.__init__)


def test_iot::metamodel::externalactuator_constructor_args():
    sig = inspect.signature(ioT::metamodel::ExternalActuator.__init__)
    params = list(sig.parameters.keys())



def test_iot::metamodel::deviceactuator_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::DeviceActuator)


def test_iot::metamodel::deviceactuator_constructor_exists():
    assert callable(ioT::metamodel::DeviceActuator.__init__)


def test_iot::metamodel::deviceactuator_constructor_args():
    sig = inspect.signature(ioT::metamodel::DeviceActuator.__init__)
    params = list(sig.parameters.keys())



def test_sensor_is_not_abstract():
    assert not inspect.isabstract(Sensor)


def test_sensor_constructor_exists():
    assert callable(Sensor.__init__)


def test_sensor_constructor_args():
    sig = inspect.signature(Sensor.__init__)
    params = list(sig.parameters.keys())



def test_iot::metamodel::devicesensor_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::DeviceSensor)


def test_iot::metamodel::devicesensor_constructor_exists():
    assert callable(ioT::metamodel::DeviceSensor.__init__)


def test_iot::metamodel::devicesensor_constructor_args():
    sig = inspect.signature(ioT::metamodel::DeviceSensor.__init__)
    params = list(sig.parameters.keys())



def test_iot::metamodel::externalsensor_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::ExternalSensor)


def test_iot::metamodel::externalsensor_constructor_exists():
    assert callable(ioT::metamodel::ExternalSensor.__init__)


def test_iot::metamodel::externalsensor_constructor_args():
    sig = inspect.signature(ioT::metamodel::ExternalSensor.__init__)
    params = list(sig.parameters.keys())



def test_iot::metamodel::action_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::Action)


def test_iot::metamodel::action_constructor_exists():
    assert callable(ioT::metamodel::Action.__init__)


def test_iot::metamodel::action_constructor_args():
    sig = inspect.signature(ioT::metamodel::Action.__init__)
    params = list(sig.parameters.keys())
    assert "Description" in params, "Missing parameter 'Description'"

def test_iot::metamodel::action_has_Description():
    assert hasattr(ioT::metamodel::Action, "Description")
    descriptor = None
    for klass in ioT::metamodel::Action.__mro__:
        if "Description" in klass.__dict__:
            descriptor = klass.__dict__["Description"]
            break
    assert isinstance(descriptor, property)



def test_iot::metamodel::database_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::Database)


def test_iot::metamodel::database_constructor_exists():
    assert callable(ioT::metamodel::Database.__init__)


def test_iot::metamodel::database_constructor_args():
    sig = inspect.signature(ioT::metamodel::Database.__init__)
    params = list(sig.parameters.keys())



def test_iot::metamodel::cloud_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::Cloud)


def test_iot::metamodel::cloud_constructor_exists():
    assert callable(ioT::metamodel::Cloud.__init__)


def test_iot::metamodel::cloud_constructor_args():
    sig = inspect.signature(ioT::metamodel::Cloud.__init__)
    params = list(sig.parameters.keys())



def test_iot::metamodel::fognode_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::FogNode)


def test_iot::metamodel::fognode_constructor_exists():
    assert callable(ioT::metamodel::FogNode.__init__)


def test_iot::metamodel::fognode_constructor_args():
    sig = inspect.signature(ioT::metamodel::FogNode.__init__)
    params = list(sig.parameters.keys())



def test_device_is_not_abstract():
    assert not inspect.isabstract(Device)


def test_device_constructor_exists():
    assert callable(Device.__init__)


def test_device_constructor_args():
    sig = inspect.signature(Device.__init__)
    params = list(sig.parameters.keys())



def test_iot::metamodel::tag_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::Tag)


def test_iot::metamodel::tag_constructor_exists():
    assert callable(ioT::metamodel::Tag.__init__)


def test_iot::metamodel::tag_constructor_args():
    sig = inspect.signature(ioT::metamodel::Tag.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_iot::metamodel::tag_has_Name():
    assert hasattr(ioT::metamodel::Tag, "Name")
    descriptor = None
    for klass in ioT::metamodel::Tag.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_iot::metamodel::sensor_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::Sensor)


def test_iot::metamodel::sensor_constructor_exists():
    assert callable(ioT::metamodel::Sensor.__init__)


def test_iot::metamodel::sensor_constructor_args():
    sig = inspect.signature(ioT::metamodel::Sensor.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "frequency" in params, "Missing parameter 'frequency'"
    assert "State" in params, "Missing parameter 'State'"

def test_iot::metamodel::sensor_has_Name():
    assert hasattr(ioT::metamodel::Sensor, "Name")
    descriptor = None
    for klass in ioT::metamodel::Sensor.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_iot::metamodel::sensor_has_frequency():
    assert hasattr(ioT::metamodel::Sensor, "frequency")
    descriptor = None
    for klass in ioT::metamodel::Sensor.__mro__:
        if "frequency" in klass.__dict__:
            descriptor = klass.__dict__["frequency"]
            break
    assert isinstance(descriptor, property)

def test_iot::metamodel::sensor_has_State():
    assert hasattr(ioT::metamodel::Sensor, "State")
    descriptor = None
    for klass in ioT::metamodel::Sensor.__mro__:
        if "State" in klass.__dict__:
            descriptor = klass.__dict__["State"]
            break
    assert isinstance(descriptor, property)



def test_iot::metamodel::actuator_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::Actuator)


def test_iot::metamodel::actuator_constructor_exists():
    assert callable(ioT::metamodel::Actuator.__init__)


def test_iot::metamodel::actuator_constructor_args():
    sig = inspect.signature(ioT::metamodel::Actuator.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iot::metamodel::actuator_has_name():
    assert hasattr(ioT::metamodel::Actuator, "name")
    descriptor = None
    for klass in ioT::metamodel::Actuator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iot::metamodel::on::device::resource_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::On::Device::Resource)


def test_iot::metamodel::on::device::resource_constructor_exists():
    assert callable(ioT::metamodel::On::Device::Resource.__init__)


def test_iot::metamodel::on::device::resource_constructor_args():
    sig = inspect.signature(ioT::metamodel::On::Device::Resource.__init__)
    params = list(sig.parameters.keys())



def test_iot::metamodel::communicator_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::Communicator)


def test_iot::metamodel::communicator_constructor_exists():
    assert callable(ioT::metamodel::Communicator.__init__)


def test_iot::metamodel::communicator_constructor_args():
    sig = inspect.signature(ioT::metamodel::Communicator.__init__)
    params = list(sig.parameters.keys())
    assert "Type" in params, "Missing parameter 'Type'"
    assert "ports_number" in params, "Missing parameter 'ports_number'"

def test_iot::metamodel::communicator_has_Type():
    assert hasattr(ioT::metamodel::Communicator, "Type")
    descriptor = None
    for klass in ioT::metamodel::Communicator.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)

def test_iot::metamodel::communicator_has_ports_number():
    assert hasattr(ioT::metamodel::Communicator, "ports_number")
    descriptor = None
    for klass in ioT::metamodel::Communicator.__mro__:
        if "ports_number" in klass.__dict__:
            descriptor = klass.__dict__["ports_number"]
            break
    assert isinstance(descriptor, property)



def test_iot::metamodel::devicestate_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::DeviceState)


def test_iot::metamodel::devicestate_constructor_exists():
    assert callable(ioT::metamodel::DeviceState.__init__)


def test_iot::metamodel::devicestate_constructor_args():
    sig = inspect.signature(ioT::metamodel::DeviceState.__init__)
    params = list(sig.parameters.keys())
    assert "Enabled" in params, "Missing parameter 'Enabled'"

def test_iot::metamodel::devicestate_has_Enabled():
    assert hasattr(ioT::metamodel::DeviceState, "Enabled")
    descriptor = None
    for klass in ioT::metamodel::DeviceState.__mro__:
        if "Enabled" in klass.__dict__:
            descriptor = klass.__dict__["Enabled"]
            break
    assert isinstance(descriptor, property)



def test_iot::metamodel::rule_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::Rule)


def test_iot::metamodel::rule_constructor_exists():
    assert callable(ioT::metamodel::Rule.__init__)


def test_iot::metamodel::rule_constructor_args():
    sig = inspect.signature(ioT::metamodel::Rule.__init__)
    params = list(sig.parameters.keys())
    assert "conditionLiteral" in params, "Missing parameter 'conditionLiteral'"
    assert "conditionValue" in params, "Missing parameter 'conditionValue'"

def test_iot::metamodel::rule_has_conditionLiteral():
    assert hasattr(ioT::metamodel::Rule, "conditionLiteral")
    descriptor = None
    for klass in ioT::metamodel::Rule.__mro__:
        if "conditionLiteral" in klass.__dict__:
            descriptor = klass.__dict__["conditionLiteral"]
            break
    assert isinstance(descriptor, property)

def test_iot::metamodel::rule_has_conditionValue():
    assert hasattr(ioT::metamodel::Rule, "conditionValue")
    descriptor = None
    for klass in ioT::metamodel::Rule.__mro__:
        if "conditionValue" in klass.__dict__:
            descriptor = klass.__dict__["conditionValue"]
            break
    assert isinstance(descriptor, property)



def test_physicalthing_is_not_abstract():
    assert not inspect.isabstract(PhysicalThing)


def test_physicalthing_constructor_exists():
    assert callable(PhysicalThing.__init__)


def test_physicalthing_constructor_args():
    sig = inspect.signature(PhysicalThing.__init__)
    params = list(sig.parameters.keys())



def test_iot::metamodel::fog::services_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::Fog::Services)


def test_iot::metamodel::fog::services_constructor_exists():
    assert callable(ioT::metamodel::Fog::Services.__init__)


def test_iot::metamodel::fog::services_constructor_args():
    sig = inspect.signature(ioT::metamodel::Fog::Services.__init__)
    params = list(sig.parameters.keys())



def test_iot::metamodel::analytics::engine_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::Analytics::Engine)


def test_iot::metamodel::analytics::engine_constructor_exists():
    assert callable(ioT::metamodel::Analytics::Engine.__init__)


def test_iot::metamodel::analytics::engine_constructor_args():
    sig = inspect.signature(ioT::metamodel::Analytics::Engine.__init__)
    params = list(sig.parameters.keys())



def test_iot::metamodel::container_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::Container)


def test_iot::metamodel::container_constructor_exists():
    assert callable(ioT::metamodel::Container.__init__)


def test_iot::metamodel::container_constructor_args():
    sig = inspect.signature(ioT::metamodel::Container.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"
    assert "IP_address" in params, "Missing parameter 'IP_address'"

def test_iot::metamodel::container_has_ID():
    assert hasattr(ioT::metamodel::Container, "ID")
    descriptor = None
    for klass in ioT::metamodel::Container.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_iot::metamodel::container_has_IP_address():
    assert hasattr(ioT::metamodel::Container, "IP_address")
    descriptor = None
    for klass in ioT::metamodel::Container.__mro__:
        if "IP_address" in klass.__dict__:
            descriptor = klass.__dict__["IP_address"]
            break
    assert isinstance(descriptor, property)



def test_iot::metamodel::vm_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::VM)


def test_iot::metamodel::vm_constructor_exists():
    assert callable(ioT::metamodel::VM.__init__)


def test_iot::metamodel::vm_constructor_args():
    sig = inspect.signature(ioT::metamodel::VM.__init__)
    params = list(sig.parameters.keys())



def test_iot::metamodel::authorizor_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::Authorizor)


def test_iot::metamodel::authorizor_constructor_exists():
    assert callable(ioT::metamodel::Authorizor.__init__)


def test_iot::metamodel::authorizor_constructor_args():
    sig = inspect.signature(ioT::metamodel::Authorizor.__init__)
    params = list(sig.parameters.keys())



def test_iot::metamodel::device_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::Device)


def test_iot::metamodel::device_constructor_exists():
    assert callable(ioT::metamodel::Device.__init__)


def test_iot::metamodel::device_constructor_args():
    sig = inspect.signature(ioT::metamodel::Device.__init__)
    params = list(sig.parameters.keys())
    assert "Technology" in params, "Missing parameter 'Technology'"

def test_iot::metamodel::device_has_Technology():
    assert hasattr(ioT::metamodel::Device, "Technology")
    descriptor = None
    for klass in ioT::metamodel::Device.__mro__:
        if "Technology" in klass.__dict__:
            descriptor = klass.__dict__["Technology"]
            break
    assert isinstance(descriptor, property)



def test_iot::metamodel::informationresource_is_not_abstract():
    assert not inspect.isabstract(ioT::metamodel::InformationResource)


def test_iot::metamodel::informationresource_constructor_exists():
    assert callable(ioT::metamodel::InformationResource.__init__)


def test_iot::metamodel::informationresource_constructor_args():
    sig = inspect.signature(ioT::metamodel::InformationResource.__init__)
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
ioT::metamodel::Entity_strategy = st.builds(
    ioT::metamodel::Entity,
)
Evaluators_strategy = st.builds(
    Evaluators,
)
ioT::metamodel::ScriptEvaluator_strategy = st.builds(
    ioT::metamodel::ScriptEvaluator,
)
ioT::metamodel::JavaEvaluator_strategy = st.builds(
    ioT::metamodel::JavaEvaluator,
)
ioT::metamodel::Evaluators_strategy = st.builds(
    ioT::metamodel::Evaluators,
)
ioT::metamodel::Operations_strategy = st.builds(
    ioT::metamodel::Operations,
)
ioT::metamodel::AtomicDataAttributes_strategy = st.builds(
    ioT::metamodel::AtomicDataAttributes,
    DeviceID=
        safe_text,
    DataEncoding=
        safe_text
)
ioT::metamodel::DataStreamAttributes_strategy = st.builds(
    ioT::metamodel::DataStreamAttributes,
    MaxBitrate=
        safe_text,
    Timestamp=
        safe_text,
    DataFormat=
        safe_text,
    DeviceID=
        safe_text,
    DataEncoding=
        safe_text,
    Description=
        safe_text,
    MeanBitRate=
        safe_text
)
ioT::metamodel::DataStreams_strategy = st.builds(
    ioT::metamodel::DataStreams,
)
ioT::metamodel::AtomicData_strategy = st.builds(
    ioT::metamodel::AtomicData,
)
ioT::metamodel::Reference::Monitor_strategy = st.builds(
    ioT::metamodel::Reference::Monitor,
)
ioT::metamodel::Policy::Repository_strategy = st.builds(
    ioT::metamodel::Policy::Repository,
)
User_strategy = st.builds(
    User,
)
Digital::Artifact_strategy = st.builds(
    Digital::Artifact,
)
ioT::metamodel::Passive::Digital::Artifact_strategy = st.builds(
    ioT::metamodel::Passive::Digital::Artifact,
)
ioT::metamodel::Active::Digital::Artifact_strategy = st.builds(
    ioT::metamodel::Active::Digital::Artifact,
)
ioT::metamodel::Digital::Artifact_strategy = st.builds(
    ioT::metamodel::Digital::Artifact,
)
ioT::metamodel::Service::Resource_strategy = st.builds(
    ioT::metamodel::Service::Resource,
)
ioT::metamodel::Device::Resource_strategy = st.builds(
    ioT::metamodel::Device::Resource,
)
InformationResource_strategy = st.builds(
    InformationResource,
)
ioT::metamodel::Network::Resource_strategy = st.builds(
    ioT::metamodel::Network::Resource,
)
Passive::Digital::Artifact_strategy = st.builds(
    Passive::Digital::Artifact,
)
Active::Digital::Artifact_strategy = st.builds(
    Active::Digital::Artifact,
)
ioT::metamodel::Property_strategy = st.builds(
    ioT::metamodel::Property,
    changeable=
        st.booleans()
)
ioT::metamodel::PhysicalThing_strategy = st.builds(
    ioT::metamodel::PhysicalThing,
)
ioT::metamodel::Fog_strategy = st.builds(
    ioT::metamodel::Fog,
)
ioT::metamodel::VirtualThing_strategy = st.builds(
    ioT::metamodel::VirtualThing,
    URI=
        safe_text
)
Entity_strategy = st.builds(
    Entity,
)
ioT::metamodel::User_strategy = st.builds(
    ioT::metamodel::User,
)
ioT::metamodel::Thing_strategy = st.builds(
    ioT::metamodel::Thing,
    name=
        safe_text
)
ioT::metamodel::Attribute_strategy = st.builds(
    ioT::metamodel::Attribute,
    name=
        safe_text,
    Type=
        safe_text
)
ioT::metamodel::Information_strategy = st.builds(
    ioT::metamodel::Information,
)
ioT::metamodel::Port_strategy = st.builds(
    ioT::metamodel::Port,
)
ioT::metamodel::Human::User_strategy = st.builds(
    ioT::metamodel::Human::User,
)
ioT::metamodel::Transition_strategy = st.builds(
    ioT::metamodel::Transition,
)
DeviceState_strategy = st.builds(
    DeviceState,
)
ioT::metamodel::CompositeState_strategy = st.builds(
    ioT::metamodel::CompositeState,
)
Actuator_strategy = st.builds(
    Actuator,
)
ioT::metamodel::ExternalActuator_strategy = st.builds(
    ioT::metamodel::ExternalActuator,
)
ioT::metamodel::DeviceActuator_strategy = st.builds(
    ioT::metamodel::DeviceActuator,
)
Sensor_strategy = st.builds(
    Sensor,
)
ioT::metamodel::DeviceSensor_strategy = st.builds(
    ioT::metamodel::DeviceSensor,
)
ioT::metamodel::ExternalSensor_strategy = st.builds(
    ioT::metamodel::ExternalSensor,
)
ioT::metamodel::Action_strategy = st.builds(
    ioT::metamodel::Action,
    Description=
        safe_text
)
ioT::metamodel::Database_strategy = st.builds(
    ioT::metamodel::Database,
)
ioT::metamodel::Cloud_strategy = st.builds(
    ioT::metamodel::Cloud,
)
ioT::metamodel::FogNode_strategy = st.builds(
    ioT::metamodel::FogNode,
)
Device_strategy = st.builds(
    Device,
)
ioT::metamodel::Tag_strategy = st.builds(
    ioT::metamodel::Tag,
    Name=
        safe_text
)
ioT::metamodel::Sensor_strategy = st.builds(
    ioT::metamodel::Sensor,
    Name=
        safe_text,
    frequency=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    State=
        st.booleans()
)
ioT::metamodel::Actuator_strategy = st.builds(
    ioT::metamodel::Actuator,
    name=
        safe_text
)
ioT::metamodel::On::Device::Resource_strategy = st.builds(
    ioT::metamodel::On::Device::Resource,
)
ioT::metamodel::Communicator_strategy = st.builds(
    ioT::metamodel::Communicator,
    Type=
        safe_text,
    ports_number=
        st.integers()
)
ioT::metamodel::DeviceState_strategy = st.builds(
    ioT::metamodel::DeviceState,
    Enabled=
        st.booleans()
)
ioT::metamodel::Rule_strategy = st.builds(
    ioT::metamodel::Rule,
    conditionLiteral=
        safe_text,
    conditionValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
PhysicalThing_strategy = st.builds(
    PhysicalThing,
)
ioT::metamodel::Fog::Services_strategy = st.builds(
    ioT::metamodel::Fog::Services,
)
ioT::metamodel::Analytics::Engine_strategy = st.builds(
    ioT::metamodel::Analytics::Engine,
)
ioT::metamodel::Container_strategy = st.builds(
    ioT::metamodel::Container,
    ID=
        safe_text,
    IP_address=
        safe_text
)
ioT::metamodel::VM_strategy = st.builds(
    ioT::metamodel::VM,
)
ioT::metamodel::Authorizor_strategy = st.builds(
    ioT::metamodel::Authorizor,
)
ioT::metamodel::Device_strategy = st.builds(
    ioT::metamodel::Device,
    Technology=
        safe_text
)
ioT::metamodel::InformationResource_strategy = st.builds(
    ioT::metamodel::InformationResource,
)

@given(instance=ioT::metamodel::Entity_strategy)
@settings(max_examples=50)
def test_iot::metamodel::entity_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::Entity)

@given(instance=Evaluators_strategy)
@settings(max_examples=50)
def test_evaluators_instantiation(instance):
    assert isinstance(instance, Evaluators)

@given(instance=ioT::metamodel::ScriptEvaluator_strategy)
@settings(max_examples=50)
def test_iot::metamodel::scriptevaluator_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::ScriptEvaluator)

@given(instance=ioT::metamodel::JavaEvaluator_strategy)
@settings(max_examples=50)
def test_iot::metamodel::javaevaluator_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::JavaEvaluator)

@given(instance=ioT::metamodel::Evaluators_strategy)
@settings(max_examples=50)
def test_iot::metamodel::evaluators_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::Evaluators)

@given(instance=ioT::metamodel::Operations_strategy)
@settings(max_examples=50)
def test_iot::metamodel::operations_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::Operations)

@given(instance=ioT::metamodel::AtomicDataAttributes_strategy)
@settings(max_examples=50)
def test_iot::metamodel::atomicdataattributes_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::AtomicDataAttributes)

@given(instance=ioT::metamodel::AtomicDataAttributes_strategy)
def test_iot::metamodel::atomicdataattributes_DeviceID_type(instance):
    assert isinstance(instance.DeviceID, str)


@given(instance=ioT::metamodel::AtomicDataAttributes_strategy)
def test_iot::metamodel::atomicdataattributes_DeviceID_setter(instance):
    original = instance.DeviceID
    instance.DeviceID = original
    assert instance.DeviceID == original

@given(instance=ioT::metamodel::AtomicDataAttributes_strategy)
def test_iot::metamodel::atomicdataattributes_DataEncoding_type(instance):
    assert isinstance(instance.DataEncoding, str)


@given(instance=ioT::metamodel::AtomicDataAttributes_strategy)
def test_iot::metamodel::atomicdataattributes_DataEncoding_setter(instance):
    original = instance.DataEncoding
    instance.DataEncoding = original
    assert instance.DataEncoding == original

@given(instance=ioT::metamodel::DataStreamAttributes_strategy)
@settings(max_examples=50)
def test_iot::metamodel::datastreamattributes_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::DataStreamAttributes)

@given(instance=ioT::metamodel::DataStreamAttributes_strategy)
def test_iot::metamodel::datastreamattributes_MaxBitrate_type(instance):
    assert isinstance(instance.MaxBitrate, str)


@given(instance=ioT::metamodel::DataStreamAttributes_strategy)
def test_iot::metamodel::datastreamattributes_MaxBitrate_setter(instance):
    original = instance.MaxBitrate
    instance.MaxBitrate = original
    assert instance.MaxBitrate == original

@given(instance=ioT::metamodel::DataStreamAttributes_strategy)
def test_iot::metamodel::datastreamattributes_Timestamp_type(instance):
    assert isinstance(instance.Timestamp, str)


@given(instance=ioT::metamodel::DataStreamAttributes_strategy)
def test_iot::metamodel::datastreamattributes_Timestamp_setter(instance):
    original = instance.Timestamp
    instance.Timestamp = original
    assert instance.Timestamp == original

@given(instance=ioT::metamodel::DataStreamAttributes_strategy)
def test_iot::metamodel::datastreamattributes_DataFormat_type(instance):
    assert isinstance(instance.DataFormat, str)


@given(instance=ioT::metamodel::DataStreamAttributes_strategy)
def test_iot::metamodel::datastreamattributes_DataFormat_setter(instance):
    original = instance.DataFormat
    instance.DataFormat = original
    assert instance.DataFormat == original

@given(instance=ioT::metamodel::DataStreamAttributes_strategy)
def test_iot::metamodel::datastreamattributes_DeviceID_type(instance):
    assert isinstance(instance.DeviceID, str)


@given(instance=ioT::metamodel::DataStreamAttributes_strategy)
def test_iot::metamodel::datastreamattributes_DeviceID_setter(instance):
    original = instance.DeviceID
    instance.DeviceID = original
    assert instance.DeviceID == original

@given(instance=ioT::metamodel::DataStreamAttributes_strategy)
def test_iot::metamodel::datastreamattributes_DataEncoding_type(instance):
    assert isinstance(instance.DataEncoding, str)


@given(instance=ioT::metamodel::DataStreamAttributes_strategy)
def test_iot::metamodel::datastreamattributes_DataEncoding_setter(instance):
    original = instance.DataEncoding
    instance.DataEncoding = original
    assert instance.DataEncoding == original

@given(instance=ioT::metamodel::DataStreamAttributes_strategy)
def test_iot::metamodel::datastreamattributes_Description_type(instance):
    assert isinstance(instance.Description, str)


@given(instance=ioT::metamodel::DataStreamAttributes_strategy)
def test_iot::metamodel::datastreamattributes_Description_setter(instance):
    original = instance.Description
    instance.Description = original
    assert instance.Description == original

@given(instance=ioT::metamodel::DataStreamAttributes_strategy)
def test_iot::metamodel::datastreamattributes_MeanBitRate_type(instance):
    assert isinstance(instance.MeanBitRate, str)


@given(instance=ioT::metamodel::DataStreamAttributes_strategy)
def test_iot::metamodel::datastreamattributes_MeanBitRate_setter(instance):
    original = instance.MeanBitRate
    instance.MeanBitRate = original
    assert instance.MeanBitRate == original

@given(instance=ioT::metamodel::DataStreams_strategy)
@settings(max_examples=50)
def test_iot::metamodel::datastreams_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::DataStreams)

@given(instance=ioT::metamodel::AtomicData_strategy)
@settings(max_examples=50)
def test_iot::metamodel::atomicdata_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::AtomicData)

@given(instance=ioT::metamodel::Reference::Monitor_strategy)
@settings(max_examples=50)
def test_iot::metamodel::reference::monitor_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::Reference::Monitor)

@given(instance=ioT::metamodel::Policy::Repository_strategy)
@settings(max_examples=50)
def test_iot::metamodel::policy::repository_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::Policy::Repository)

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)

@given(instance=Digital::Artifact_strategy)
@settings(max_examples=50)
def test_digital::artifact_instantiation(instance):
    assert isinstance(instance, Digital::Artifact)

@given(instance=ioT::metamodel::Passive::Digital::Artifact_strategy)
@settings(max_examples=50)
def test_iot::metamodel::passive::digital::artifact_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::Passive::Digital::Artifact)

@given(instance=ioT::metamodel::Active::Digital::Artifact_strategy)
@settings(max_examples=50)
def test_iot::metamodel::active::digital::artifact_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::Active::Digital::Artifact)

@given(instance=ioT::metamodel::Digital::Artifact_strategy)
@settings(max_examples=50)
def test_iot::metamodel::digital::artifact_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::Digital::Artifact)

@given(instance=ioT::metamodel::Service::Resource_strategy)
@settings(max_examples=50)
def test_iot::metamodel::service::resource_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::Service::Resource)

@given(instance=ioT::metamodel::Device::Resource_strategy)
@settings(max_examples=50)
def test_iot::metamodel::device::resource_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::Device::Resource)

@given(instance=InformationResource_strategy)
@settings(max_examples=50)
def test_informationresource_instantiation(instance):
    assert isinstance(instance, InformationResource)

@given(instance=ioT::metamodel::Network::Resource_strategy)
@settings(max_examples=50)
def test_iot::metamodel::network::resource_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::Network::Resource)

@given(instance=Passive::Digital::Artifact_strategy)
@settings(max_examples=50)
def test_passive::digital::artifact_instantiation(instance):
    assert isinstance(instance, Passive::Digital::Artifact)

@given(instance=Active::Digital::Artifact_strategy)
@settings(max_examples=50)
def test_active::digital::artifact_instantiation(instance):
    assert isinstance(instance, Active::Digital::Artifact)

@given(instance=ioT::metamodel::Property_strategy)
@settings(max_examples=50)
def test_iot::metamodel::property_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::Property)

@given(instance=ioT::metamodel::Property_strategy)
def test_iot::metamodel::property_changeable_type(instance):
    assert isinstance(instance.changeable, bool)


@given(instance=ioT::metamodel::Property_strategy)
def test_iot::metamodel::property_changeable_setter(instance):
    original = instance.changeable
    instance.changeable = original
    assert instance.changeable == original

@given(instance=ioT::metamodel::PhysicalThing_strategy)
@settings(max_examples=50)
def test_iot::metamodel::physicalthing_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::PhysicalThing)

@given(instance=ioT::metamodel::Fog_strategy)
@settings(max_examples=50)
def test_iot::metamodel::fog_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::Fog)

@given(instance=ioT::metamodel::VirtualThing_strategy)
@settings(max_examples=50)
def test_iot::metamodel::virtualthing_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::VirtualThing)

@given(instance=ioT::metamodel::VirtualThing_strategy)
def test_iot::metamodel::virtualthing_URI_type(instance):
    assert isinstance(instance.URI, str)


@given(instance=ioT::metamodel::VirtualThing_strategy)
def test_iot::metamodel::virtualthing_URI_setter(instance):
    original = instance.URI
    instance.URI = original
    assert instance.URI == original

@given(instance=Entity_strategy)
@settings(max_examples=50)
def test_entity_instantiation(instance):
    assert isinstance(instance, Entity)

@given(instance=ioT::metamodel::User_strategy)
@settings(max_examples=50)
def test_iot::metamodel::user_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::User)

@given(instance=ioT::metamodel::Thing_strategy)
@settings(max_examples=50)
def test_iot::metamodel::thing_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::Thing)

@given(instance=ioT::metamodel::Thing_strategy)
def test_iot::metamodel::thing_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ioT::metamodel::Thing_strategy)
def test_iot::metamodel::thing_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ioT::metamodel::Attribute_strategy)
@settings(max_examples=50)
def test_iot::metamodel::attribute_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::Attribute)

@given(instance=ioT::metamodel::Attribute_strategy)
def test_iot::metamodel::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ioT::metamodel::Attribute_strategy)
def test_iot::metamodel::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ioT::metamodel::Attribute_strategy)
def test_iot::metamodel::attribute_Type_type(instance):
    assert isinstance(instance.Type, str)


@given(instance=ioT::metamodel::Attribute_strategy)
def test_iot::metamodel::attribute_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original

@given(instance=ioT::metamodel::Information_strategy)
@settings(max_examples=50)
def test_iot::metamodel::information_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::Information)

@given(instance=ioT::metamodel::Port_strategy)
@settings(max_examples=50)
def test_iot::metamodel::port_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::Port)

@given(instance=ioT::metamodel::Human::User_strategy)
@settings(max_examples=50)
def test_iot::metamodel::human::user_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::Human::User)

@given(instance=ioT::metamodel::Transition_strategy)
@settings(max_examples=50)
def test_iot::metamodel::transition_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::Transition)

@given(instance=DeviceState_strategy)
@settings(max_examples=50)
def test_devicestate_instantiation(instance):
    assert isinstance(instance, DeviceState)

@given(instance=ioT::metamodel::CompositeState_strategy)
@settings(max_examples=50)
def test_iot::metamodel::compositestate_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::CompositeState)

@given(instance=Actuator_strategy)
@settings(max_examples=50)
def test_actuator_instantiation(instance):
    assert isinstance(instance, Actuator)

@given(instance=ioT::metamodel::ExternalActuator_strategy)
@settings(max_examples=50)
def test_iot::metamodel::externalactuator_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::ExternalActuator)

@given(instance=ioT::metamodel::DeviceActuator_strategy)
@settings(max_examples=50)
def test_iot::metamodel::deviceactuator_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::DeviceActuator)

@given(instance=Sensor_strategy)
@settings(max_examples=50)
def test_sensor_instantiation(instance):
    assert isinstance(instance, Sensor)

@given(instance=ioT::metamodel::DeviceSensor_strategy)
@settings(max_examples=50)
def test_iot::metamodel::devicesensor_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::DeviceSensor)

@given(instance=ioT::metamodel::ExternalSensor_strategy)
@settings(max_examples=50)
def test_iot::metamodel::externalsensor_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::ExternalSensor)

@given(instance=ioT::metamodel::Action_strategy)
@settings(max_examples=50)
def test_iot::metamodel::action_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::Action)

@given(instance=ioT::metamodel::Action_strategy)
def test_iot::metamodel::action_Description_type(instance):
    assert isinstance(instance.Description, str)


@given(instance=ioT::metamodel::Action_strategy)
def test_iot::metamodel::action_Description_setter(instance):
    original = instance.Description
    instance.Description = original
    assert instance.Description == original

@given(instance=ioT::metamodel::Database_strategy)
@settings(max_examples=50)
def test_iot::metamodel::database_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::Database)

@given(instance=ioT::metamodel::Cloud_strategy)
@settings(max_examples=50)
def test_iot::metamodel::cloud_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::Cloud)

@given(instance=ioT::metamodel::FogNode_strategy)
@settings(max_examples=50)
def test_iot::metamodel::fognode_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::FogNode)

@given(instance=Device_strategy)
@settings(max_examples=50)
def test_device_instantiation(instance):
    assert isinstance(instance, Device)

@given(instance=ioT::metamodel::Tag_strategy)
@settings(max_examples=50)
def test_iot::metamodel::tag_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::Tag)

@given(instance=ioT::metamodel::Tag_strategy)
def test_iot::metamodel::tag_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=ioT::metamodel::Tag_strategy)
def test_iot::metamodel::tag_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=ioT::metamodel::Sensor_strategy)
@settings(max_examples=50)
def test_iot::metamodel::sensor_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::Sensor)

@given(instance=ioT::metamodel::Sensor_strategy)
def test_iot::metamodel::sensor_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=ioT::metamodel::Sensor_strategy)
def test_iot::metamodel::sensor_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=ioT::metamodel::Sensor_strategy)
def test_iot::metamodel::sensor_frequency_type(instance):
    assert isinstance(instance.frequency, float)


@given(instance=ioT::metamodel::Sensor_strategy)
def test_iot::metamodel::sensor_frequency_setter(instance):
    original = instance.frequency
    instance.frequency = original
    assert instance.frequency == original

@given(instance=ioT::metamodel::Sensor_strategy)
def test_iot::metamodel::sensor_State_type(instance):
    assert isinstance(instance.State, bool)


@given(instance=ioT::metamodel::Sensor_strategy)
def test_iot::metamodel::sensor_State_setter(instance):
    original = instance.State
    instance.State = original
    assert instance.State == original

@given(instance=ioT::metamodel::Actuator_strategy)
@settings(max_examples=50)
def test_iot::metamodel::actuator_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::Actuator)

@given(instance=ioT::metamodel::Actuator_strategy)
def test_iot::metamodel::actuator_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ioT::metamodel::Actuator_strategy)
def test_iot::metamodel::actuator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ioT::metamodel::On::Device::Resource_strategy)
@settings(max_examples=50)
def test_iot::metamodel::on::device::resource_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::On::Device::Resource)

@given(instance=ioT::metamodel::Communicator_strategy)
@settings(max_examples=50)
def test_iot::metamodel::communicator_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::Communicator)

@given(instance=ioT::metamodel::Communicator_strategy)
def test_iot::metamodel::communicator_Type_type(instance):
    assert isinstance(instance.Type, str)


@given(instance=ioT::metamodel::Communicator_strategy)
def test_iot::metamodel::communicator_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original

@given(instance=ioT::metamodel::Communicator_strategy)
def test_iot::metamodel::communicator_ports_number_type(instance):
    assert isinstance(instance.ports_number, int)


@given(instance=ioT::metamodel::Communicator_strategy)
def test_iot::metamodel::communicator_ports_number_setter(instance):
    original = instance.ports_number
    instance.ports_number = original
    assert instance.ports_number == original

@given(instance=ioT::metamodel::DeviceState_strategy)
@settings(max_examples=50)
def test_iot::metamodel::devicestate_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::DeviceState)

@given(instance=ioT::metamodel::DeviceState_strategy)
def test_iot::metamodel::devicestate_Enabled_type(instance):
    assert isinstance(instance.Enabled, bool)


@given(instance=ioT::metamodel::DeviceState_strategy)
def test_iot::metamodel::devicestate_Enabled_setter(instance):
    original = instance.Enabled
    instance.Enabled = original
    assert instance.Enabled == original

@given(instance=ioT::metamodel::Rule_strategy)
@settings(max_examples=50)
def test_iot::metamodel::rule_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::Rule)

@given(instance=ioT::metamodel::Rule_strategy)
def test_iot::metamodel::rule_conditionLiteral_type(instance):
    assert isinstance(instance.conditionLiteral, str)


@given(instance=ioT::metamodel::Rule_strategy)
def test_iot::metamodel::rule_conditionLiteral_setter(instance):
    original = instance.conditionLiteral
    instance.conditionLiteral = original
    assert instance.conditionLiteral == original

@given(instance=ioT::metamodel::Rule_strategy)
def test_iot::metamodel::rule_conditionValue_type(instance):
    assert isinstance(instance.conditionValue, float)


@given(instance=ioT::metamodel::Rule_strategy)
def test_iot::metamodel::rule_conditionValue_setter(instance):
    original = instance.conditionValue
    instance.conditionValue = original
    assert instance.conditionValue == original

@given(instance=PhysicalThing_strategy)
@settings(max_examples=50)
def test_physicalthing_instantiation(instance):
    assert isinstance(instance, PhysicalThing)

@given(instance=ioT::metamodel::Fog::Services_strategy)
@settings(max_examples=50)
def test_iot::metamodel::fog::services_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::Fog::Services)

@given(instance=ioT::metamodel::Analytics::Engine_strategy)
@settings(max_examples=50)
def test_iot::metamodel::analytics::engine_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::Analytics::Engine)

@given(instance=ioT::metamodel::Container_strategy)
@settings(max_examples=50)
def test_iot::metamodel::container_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::Container)

@given(instance=ioT::metamodel::Container_strategy)
def test_iot::metamodel::container_ID_type(instance):
    assert isinstance(instance.ID, str)


@given(instance=ioT::metamodel::Container_strategy)
def test_iot::metamodel::container_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=ioT::metamodel::Container_strategy)
def test_iot::metamodel::container_IP_address_type(instance):
    assert isinstance(instance.IP_address, str)


@given(instance=ioT::metamodel::Container_strategy)
def test_iot::metamodel::container_IP_address_setter(instance):
    original = instance.IP_address
    instance.IP_address = original
    assert instance.IP_address == original

@given(instance=ioT::metamodel::VM_strategy)
@settings(max_examples=50)
def test_iot::metamodel::vm_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::VM)

@given(instance=ioT::metamodel::Authorizor_strategy)
@settings(max_examples=50)
def test_iot::metamodel::authorizor_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::Authorizor)

@given(instance=ioT::metamodel::Device_strategy)
@settings(max_examples=50)
def test_iot::metamodel::device_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::Device)

@given(instance=ioT::metamodel::Device_strategy)
def test_iot::metamodel::device_Technology_type(instance):
    assert isinstance(instance.Technology, str)


@given(instance=ioT::metamodel::Device_strategy)
def test_iot::metamodel::device_Technology_setter(instance):
    original = instance.Technology
    instance.Technology = original
    assert instance.Technology == original

@given(instance=ioT::metamodel::InformationResource_strategy)
@settings(max_examples=50)
def test_iot::metamodel::informationresource_instantiation(instance):
    assert isinstance(instance, ioT::metamodel::InformationResource)
