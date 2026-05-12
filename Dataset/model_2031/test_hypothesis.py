import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ioT_metamodel_Entity,
    Evaluators,
    ioT_metamodel_ScriptEvaluator,
    ioT_metamodel_JavaEvaluator,
    ioT_metamodel_Evaluators,
    ioT_metamodel_Operations,
    ioT_metamodel_AtomicDataAttributes,
    ioT_metamodel_DataStreamAttributes,
    ioT_metamodel_DataStreams,
    ioT_metamodel_AtomicData,
    ioT_metamodel_Reference_Monitor,
    ioT_metamodel_Policy_Repository,
    User,
    Digital_Artifact,
    ioT_metamodel_Passive_Digital_Artifact,
    ioT_metamodel_Active_Digital_Artifact,
    ioT_metamodel_Digital_Artifact,
    ioT_metamodel_Service_Resource,
    ioT_metamodel_Device_Resource,
    InformationResource,
    ioT_metamodel_Network_Resource,
    ioT_metamodel_Information,
    ioT_metamodel_Port,
    ioT_metamodel_Human_User,
    ioT_metamodel_Transition,
    DeviceState,
    ioT_metamodel_CompositeState,
    Actuator,
    ioT_metamodel_ExternalActuator,
    ioT_metamodel_DeviceActuator,
    Sensor,
    ioT_metamodel_DeviceSensor,
    ioT_metamodel_ExternalSensor,
    ioT_metamodel_Action,
    ioT_metamodel_Database,
    ioT_metamodel_Cloud,
    ioT_metamodel_FogNode,
    Device,
    ioT_metamodel_Sensor,
    ioT_metamodel_Tag,
    ioT_metamodel_Actuator,
    ioT_metamodel_On_Device_Resource,
    ioT_metamodel_Communicator,
    ioT_metamodel_DeviceState,
    ioT_metamodel_Rule,
    PhysicalThing,
    ioT_metamodel_Fog_Services,
    ioT_metamodel_Analytics_Engine,
    ioT_metamodel_Container,
    ioT_metamodel_VM,
    ioT_metamodel_Authorizor,
    ioT_metamodel_Device,
    ioT_metamodel_InformationResource,
    Passive_Digital_Artifact,
    Active_Digital_Artifact,
    ioT_metamodel_Property,
    ioT_metamodel_PhysicalThing,
    ioT_metamodel_Fog,
    ioT_metamodel_VirtualThing,
    Entity,
    ioT_metamodel_User,
    ioT_metamodel_Attribute,
    ioT_metamodel_Thing,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_iot_metamodel_entity_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_Entity)


def test_iot_metamodel_entity_constructor_exists():
    assert callable(ioT_metamodel_Entity.__init__)


def test_iot_metamodel_entity_constructor_args():
    sig = inspect.signature(ioT_metamodel_Entity.__init__)
    params = list(sig.parameters.keys())



def test_evaluators_is_not_abstract():
    assert not inspect.isabstract(Evaluators)


def test_evaluators_constructor_exists():
    assert callable(Evaluators.__init__)


def test_evaluators_constructor_args():
    sig = inspect.signature(Evaluators.__init__)
    params = list(sig.parameters.keys())



def test_iot_metamodel_scriptevaluator_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_ScriptEvaluator)


def test_iot_metamodel_scriptevaluator_constructor_exists():
    assert callable(ioT_metamodel_ScriptEvaluator.__init__)


def test_iot_metamodel_scriptevaluator_constructor_args():
    sig = inspect.signature(ioT_metamodel_ScriptEvaluator.__init__)
    params = list(sig.parameters.keys())



def test_iot_metamodel_javaevaluator_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_JavaEvaluator)


def test_iot_metamodel_javaevaluator_constructor_exists():
    assert callable(ioT_metamodel_JavaEvaluator.__init__)


def test_iot_metamodel_javaevaluator_constructor_args():
    sig = inspect.signature(ioT_metamodel_JavaEvaluator.__init__)
    params = list(sig.parameters.keys())



def test_iot_metamodel_evaluators_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_Evaluators)


def test_iot_metamodel_evaluators_constructor_exists():
    assert callable(ioT_metamodel_Evaluators.__init__)


def test_iot_metamodel_evaluators_constructor_args():
    sig = inspect.signature(ioT_metamodel_Evaluators.__init__)
    params = list(sig.parameters.keys())



def test_iot_metamodel_operations_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_Operations)


def test_iot_metamodel_operations_constructor_exists():
    assert callable(ioT_metamodel_Operations.__init__)


def test_iot_metamodel_operations_constructor_args():
    sig = inspect.signature(ioT_metamodel_Operations.__init__)
    params = list(sig.parameters.keys())



def test_iot_metamodel_atomicdataattributes_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_AtomicDataAttributes)


def test_iot_metamodel_atomicdataattributes_constructor_exists():
    assert callable(ioT_metamodel_AtomicDataAttributes.__init__)


def test_iot_metamodel_atomicdataattributes_constructor_args():
    sig = inspect.signature(ioT_metamodel_AtomicDataAttributes.__init__)
    params = list(sig.parameters.keys())
    assert "DeviceID" in params, "Missing parameter 'DeviceID'"
    assert "DataEncoding" in params, "Missing parameter 'DataEncoding'"

def test_iot_metamodel_atomicdataattributes_has_DeviceID():
    assert hasattr(ioT_metamodel_AtomicDataAttributes, "DeviceID")
    descriptor = None
    for klass in ioT_metamodel_AtomicDataAttributes.__mro__:
        if "DeviceID" in klass.__dict__:
            descriptor = klass.__dict__["DeviceID"]
            break
    assert isinstance(descriptor, property)

def test_iot_metamodel_atomicdataattributes_has_DataEncoding():
    assert hasattr(ioT_metamodel_AtomicDataAttributes, "DataEncoding")
    descriptor = None
    for klass in ioT_metamodel_AtomicDataAttributes.__mro__:
        if "DataEncoding" in klass.__dict__:
            descriptor = klass.__dict__["DataEncoding"]
            break
    assert isinstance(descriptor, property)



def test_iot_metamodel_datastreamattributes_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_DataStreamAttributes)


def test_iot_metamodel_datastreamattributes_constructor_exists():
    assert callable(ioT_metamodel_DataStreamAttributes.__init__)


def test_iot_metamodel_datastreamattributes_constructor_args():
    sig = inspect.signature(ioT_metamodel_DataStreamAttributes.__init__)
    params = list(sig.parameters.keys())
    assert "Timestamp" in params, "Missing parameter 'Timestamp'"
    assert "DataFormat" in params, "Missing parameter 'DataFormat'"
    assert "Description" in params, "Missing parameter 'Description'"
    assert "DataEncoding" in params, "Missing parameter 'DataEncoding'"
    assert "MaxBitrate" in params, "Missing parameter 'MaxBitrate'"
    assert "DeviceID" in params, "Missing parameter 'DeviceID'"
    assert "MeanBitRate" in params, "Missing parameter 'MeanBitRate'"

def test_iot_metamodel_datastreamattributes_has_Timestamp():
    assert hasattr(ioT_metamodel_DataStreamAttributes, "Timestamp")
    descriptor = None
    for klass in ioT_metamodel_DataStreamAttributes.__mro__:
        if "Timestamp" in klass.__dict__:
            descriptor = klass.__dict__["Timestamp"]
            break
    assert isinstance(descriptor, property)

def test_iot_metamodel_datastreamattributes_has_DataFormat():
    assert hasattr(ioT_metamodel_DataStreamAttributes, "DataFormat")
    descriptor = None
    for klass in ioT_metamodel_DataStreamAttributes.__mro__:
        if "DataFormat" in klass.__dict__:
            descriptor = klass.__dict__["DataFormat"]
            break
    assert isinstance(descriptor, property)

def test_iot_metamodel_datastreamattributes_has_Description():
    assert hasattr(ioT_metamodel_DataStreamAttributes, "Description")
    descriptor = None
    for klass in ioT_metamodel_DataStreamAttributes.__mro__:
        if "Description" in klass.__dict__:
            descriptor = klass.__dict__["Description"]
            break
    assert isinstance(descriptor, property)

def test_iot_metamodel_datastreamattributes_has_DataEncoding():
    assert hasattr(ioT_metamodel_DataStreamAttributes, "DataEncoding")
    descriptor = None
    for klass in ioT_metamodel_DataStreamAttributes.__mro__:
        if "DataEncoding" in klass.__dict__:
            descriptor = klass.__dict__["DataEncoding"]
            break
    assert isinstance(descriptor, property)

def test_iot_metamodel_datastreamattributes_has_MaxBitrate():
    assert hasattr(ioT_metamodel_DataStreamAttributes, "MaxBitrate")
    descriptor = None
    for klass in ioT_metamodel_DataStreamAttributes.__mro__:
        if "MaxBitrate" in klass.__dict__:
            descriptor = klass.__dict__["MaxBitrate"]
            break
    assert isinstance(descriptor, property)

def test_iot_metamodel_datastreamattributes_has_DeviceID():
    assert hasattr(ioT_metamodel_DataStreamAttributes, "DeviceID")
    descriptor = None
    for klass in ioT_metamodel_DataStreamAttributes.__mro__:
        if "DeviceID" in klass.__dict__:
            descriptor = klass.__dict__["DeviceID"]
            break
    assert isinstance(descriptor, property)

def test_iot_metamodel_datastreamattributes_has_MeanBitRate():
    assert hasattr(ioT_metamodel_DataStreamAttributes, "MeanBitRate")
    descriptor = None
    for klass in ioT_metamodel_DataStreamAttributes.__mro__:
        if "MeanBitRate" in klass.__dict__:
            descriptor = klass.__dict__["MeanBitRate"]
            break
    assert isinstance(descriptor, property)



def test_iot_metamodel_datastreams_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_DataStreams)


def test_iot_metamodel_datastreams_constructor_exists():
    assert callable(ioT_metamodel_DataStreams.__init__)


def test_iot_metamodel_datastreams_constructor_args():
    sig = inspect.signature(ioT_metamodel_DataStreams.__init__)
    params = list(sig.parameters.keys())



def test_iot_metamodel_atomicdata_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_AtomicData)


def test_iot_metamodel_atomicdata_constructor_exists():
    assert callable(ioT_metamodel_AtomicData.__init__)


def test_iot_metamodel_atomicdata_constructor_args():
    sig = inspect.signature(ioT_metamodel_AtomicData.__init__)
    params = list(sig.parameters.keys())



def test_iot_metamodel_reference_monitor_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_Reference_Monitor)


def test_iot_metamodel_reference_monitor_constructor_exists():
    assert callable(ioT_metamodel_Reference_Monitor.__init__)


def test_iot_metamodel_reference_monitor_constructor_args():
    sig = inspect.signature(ioT_metamodel_Reference_Monitor.__init__)
    params = list(sig.parameters.keys())



def test_iot_metamodel_policy_repository_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_Policy_Repository)


def test_iot_metamodel_policy_repository_constructor_exists():
    assert callable(ioT_metamodel_Policy_Repository.__init__)


def test_iot_metamodel_policy_repository_constructor_args():
    sig = inspect.signature(ioT_metamodel_Policy_Repository.__init__)
    params = list(sig.parameters.keys())



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())



def test_digital_artifact_is_not_abstract():
    assert not inspect.isabstract(Digital_Artifact)


def test_digital_artifact_constructor_exists():
    assert callable(Digital_Artifact.__init__)


def test_digital_artifact_constructor_args():
    sig = inspect.signature(Digital_Artifact.__init__)
    params = list(sig.parameters.keys())



def test_iot_metamodel_passive_digital_artifact_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_Passive_Digital_Artifact)


def test_iot_metamodel_passive_digital_artifact_constructor_exists():
    assert callable(ioT_metamodel_Passive_Digital_Artifact.__init__)


def test_iot_metamodel_passive_digital_artifact_constructor_args():
    sig = inspect.signature(ioT_metamodel_Passive_Digital_Artifact.__init__)
    params = list(sig.parameters.keys())



def test_iot_metamodel_active_digital_artifact_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_Active_Digital_Artifact)


def test_iot_metamodel_active_digital_artifact_constructor_exists():
    assert callable(ioT_metamodel_Active_Digital_Artifact.__init__)


def test_iot_metamodel_active_digital_artifact_constructor_args():
    sig = inspect.signature(ioT_metamodel_Active_Digital_Artifact.__init__)
    params = list(sig.parameters.keys())



def test_iot_metamodel_digital_artifact_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_Digital_Artifact)


def test_iot_metamodel_digital_artifact_constructor_exists():
    assert callable(ioT_metamodel_Digital_Artifact.__init__)


def test_iot_metamodel_digital_artifact_constructor_args():
    sig = inspect.signature(ioT_metamodel_Digital_Artifact.__init__)
    params = list(sig.parameters.keys())



def test_iot_metamodel_service_resource_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_Service_Resource)


def test_iot_metamodel_service_resource_constructor_exists():
    assert callable(ioT_metamodel_Service_Resource.__init__)


def test_iot_metamodel_service_resource_constructor_args():
    sig = inspect.signature(ioT_metamodel_Service_Resource.__init__)
    params = list(sig.parameters.keys())



def test_iot_metamodel_device_resource_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_Device_Resource)


def test_iot_metamodel_device_resource_constructor_exists():
    assert callable(ioT_metamodel_Device_Resource.__init__)


def test_iot_metamodel_device_resource_constructor_args():
    sig = inspect.signature(ioT_metamodel_Device_Resource.__init__)
    params = list(sig.parameters.keys())



def test_informationresource_is_not_abstract():
    assert not inspect.isabstract(InformationResource)


def test_informationresource_constructor_exists():
    assert callable(InformationResource.__init__)


def test_informationresource_constructor_args():
    sig = inspect.signature(InformationResource.__init__)
    params = list(sig.parameters.keys())



def test_iot_metamodel_network_resource_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_Network_Resource)


def test_iot_metamodel_network_resource_constructor_exists():
    assert callable(ioT_metamodel_Network_Resource.__init__)


def test_iot_metamodel_network_resource_constructor_args():
    sig = inspect.signature(ioT_metamodel_Network_Resource.__init__)
    params = list(sig.parameters.keys())



def test_iot_metamodel_information_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_Information)


def test_iot_metamodel_information_constructor_exists():
    assert callable(ioT_metamodel_Information.__init__)


def test_iot_metamodel_information_constructor_args():
    sig = inspect.signature(ioT_metamodel_Information.__init__)
    params = list(sig.parameters.keys())



def test_iot_metamodel_port_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_Port)


def test_iot_metamodel_port_constructor_exists():
    assert callable(ioT_metamodel_Port.__init__)


def test_iot_metamodel_port_constructor_args():
    sig = inspect.signature(ioT_metamodel_Port.__init__)
    params = list(sig.parameters.keys())



def test_iot_metamodel_human_user_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_Human_User)


def test_iot_metamodel_human_user_constructor_exists():
    assert callable(ioT_metamodel_Human_User.__init__)


def test_iot_metamodel_human_user_constructor_args():
    sig = inspect.signature(ioT_metamodel_Human_User.__init__)
    params = list(sig.parameters.keys())



def test_iot_metamodel_transition_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_Transition)


def test_iot_metamodel_transition_constructor_exists():
    assert callable(ioT_metamodel_Transition.__init__)


def test_iot_metamodel_transition_constructor_args():
    sig = inspect.signature(ioT_metamodel_Transition.__init__)
    params = list(sig.parameters.keys())



def test_devicestate_is_not_abstract():
    assert not inspect.isabstract(DeviceState)


def test_devicestate_constructor_exists():
    assert callable(DeviceState.__init__)


def test_devicestate_constructor_args():
    sig = inspect.signature(DeviceState.__init__)
    params = list(sig.parameters.keys())



def test_iot_metamodel_compositestate_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_CompositeState)


def test_iot_metamodel_compositestate_constructor_exists():
    assert callable(ioT_metamodel_CompositeState.__init__)


def test_iot_metamodel_compositestate_constructor_args():
    sig = inspect.signature(ioT_metamodel_CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_actuator_is_not_abstract():
    assert not inspect.isabstract(Actuator)


def test_actuator_constructor_exists():
    assert callable(Actuator.__init__)


def test_actuator_constructor_args():
    sig = inspect.signature(Actuator.__init__)
    params = list(sig.parameters.keys())



def test_iot_metamodel_externalactuator_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_ExternalActuator)


def test_iot_metamodel_externalactuator_constructor_exists():
    assert callable(ioT_metamodel_ExternalActuator.__init__)


def test_iot_metamodel_externalactuator_constructor_args():
    sig = inspect.signature(ioT_metamodel_ExternalActuator.__init__)
    params = list(sig.parameters.keys())



def test_iot_metamodel_deviceactuator_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_DeviceActuator)


def test_iot_metamodel_deviceactuator_constructor_exists():
    assert callable(ioT_metamodel_DeviceActuator.__init__)


def test_iot_metamodel_deviceactuator_constructor_args():
    sig = inspect.signature(ioT_metamodel_DeviceActuator.__init__)
    params = list(sig.parameters.keys())



def test_sensor_is_not_abstract():
    assert not inspect.isabstract(Sensor)


def test_sensor_constructor_exists():
    assert callable(Sensor.__init__)


def test_sensor_constructor_args():
    sig = inspect.signature(Sensor.__init__)
    params = list(sig.parameters.keys())



def test_iot_metamodel_devicesensor_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_DeviceSensor)


def test_iot_metamodel_devicesensor_constructor_exists():
    assert callable(ioT_metamodel_DeviceSensor.__init__)


def test_iot_metamodel_devicesensor_constructor_args():
    sig = inspect.signature(ioT_metamodel_DeviceSensor.__init__)
    params = list(sig.parameters.keys())



def test_iot_metamodel_externalsensor_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_ExternalSensor)


def test_iot_metamodel_externalsensor_constructor_exists():
    assert callable(ioT_metamodel_ExternalSensor.__init__)


def test_iot_metamodel_externalsensor_constructor_args():
    sig = inspect.signature(ioT_metamodel_ExternalSensor.__init__)
    params = list(sig.parameters.keys())



def test_iot_metamodel_action_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_Action)


def test_iot_metamodel_action_constructor_exists():
    assert callable(ioT_metamodel_Action.__init__)


def test_iot_metamodel_action_constructor_args():
    sig = inspect.signature(ioT_metamodel_Action.__init__)
    params = list(sig.parameters.keys())
    assert "Description" in params, "Missing parameter 'Description'"

def test_iot_metamodel_action_has_Description():
    assert hasattr(ioT_metamodel_Action, "Description")
    descriptor = None
    for klass in ioT_metamodel_Action.__mro__:
        if "Description" in klass.__dict__:
            descriptor = klass.__dict__["Description"]
            break
    assert isinstance(descriptor, property)



def test_iot_metamodel_database_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_Database)


def test_iot_metamodel_database_constructor_exists():
    assert callable(ioT_metamodel_Database.__init__)


def test_iot_metamodel_database_constructor_args():
    sig = inspect.signature(ioT_metamodel_Database.__init__)
    params = list(sig.parameters.keys())



def test_iot_metamodel_cloud_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_Cloud)


def test_iot_metamodel_cloud_constructor_exists():
    assert callable(ioT_metamodel_Cloud.__init__)


def test_iot_metamodel_cloud_constructor_args():
    sig = inspect.signature(ioT_metamodel_Cloud.__init__)
    params = list(sig.parameters.keys())



def test_iot_metamodel_fognode_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_FogNode)


def test_iot_metamodel_fognode_constructor_exists():
    assert callable(ioT_metamodel_FogNode.__init__)


def test_iot_metamodel_fognode_constructor_args():
    sig = inspect.signature(ioT_metamodel_FogNode.__init__)
    params = list(sig.parameters.keys())



def test_device_is_not_abstract():
    assert not inspect.isabstract(Device)


def test_device_constructor_exists():
    assert callable(Device.__init__)


def test_device_constructor_args():
    sig = inspect.signature(Device.__init__)
    params = list(sig.parameters.keys())



def test_iot_metamodel_sensor_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_Sensor)


def test_iot_metamodel_sensor_constructor_exists():
    assert callable(ioT_metamodel_Sensor.__init__)


def test_iot_metamodel_sensor_constructor_args():
    sig = inspect.signature(ioT_metamodel_Sensor.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "State" in params, "Missing parameter 'State'"
    assert "frequency" in params, "Missing parameter 'frequency'"

def test_iot_metamodel_sensor_has_Name():
    assert hasattr(ioT_metamodel_Sensor, "Name")
    descriptor = None
    for klass in ioT_metamodel_Sensor.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_iot_metamodel_sensor_has_State():
    assert hasattr(ioT_metamodel_Sensor, "State")
    descriptor = None
    for klass in ioT_metamodel_Sensor.__mro__:
        if "State" in klass.__dict__:
            descriptor = klass.__dict__["State"]
            break
    assert isinstance(descriptor, property)

def test_iot_metamodel_sensor_has_frequency():
    assert hasattr(ioT_metamodel_Sensor, "frequency")
    descriptor = None
    for klass in ioT_metamodel_Sensor.__mro__:
        if "frequency" in klass.__dict__:
            descriptor = klass.__dict__["frequency"]
            break
    assert isinstance(descriptor, property)



def test_iot_metamodel_tag_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_Tag)


def test_iot_metamodel_tag_constructor_exists():
    assert callable(ioT_metamodel_Tag.__init__)


def test_iot_metamodel_tag_constructor_args():
    sig = inspect.signature(ioT_metamodel_Tag.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_iot_metamodel_tag_has_Name():
    assert hasattr(ioT_metamodel_Tag, "Name")
    descriptor = None
    for klass in ioT_metamodel_Tag.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_iot_metamodel_actuator_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_Actuator)


def test_iot_metamodel_actuator_constructor_exists():
    assert callable(ioT_metamodel_Actuator.__init__)


def test_iot_metamodel_actuator_constructor_args():
    sig = inspect.signature(ioT_metamodel_Actuator.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iot_metamodel_actuator_has_name():
    assert hasattr(ioT_metamodel_Actuator, "name")
    descriptor = None
    for klass in ioT_metamodel_Actuator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iot_metamodel_on_device_resource_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_On_Device_Resource)


def test_iot_metamodel_on_device_resource_constructor_exists():
    assert callable(ioT_metamodel_On_Device_Resource.__init__)


def test_iot_metamodel_on_device_resource_constructor_args():
    sig = inspect.signature(ioT_metamodel_On_Device_Resource.__init__)
    params = list(sig.parameters.keys())



def test_iot_metamodel_communicator_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_Communicator)


def test_iot_metamodel_communicator_constructor_exists():
    assert callable(ioT_metamodel_Communicator.__init__)


def test_iot_metamodel_communicator_constructor_args():
    sig = inspect.signature(ioT_metamodel_Communicator.__init__)
    params = list(sig.parameters.keys())
    assert "ports_number" in params, "Missing parameter 'ports_number'"
    assert "Type" in params, "Missing parameter 'Type'"

def test_iot_metamodel_communicator_has_ports_number():
    assert hasattr(ioT_metamodel_Communicator, "ports_number")
    descriptor = None
    for klass in ioT_metamodel_Communicator.__mro__:
        if "ports_number" in klass.__dict__:
            descriptor = klass.__dict__["ports_number"]
            break
    assert isinstance(descriptor, property)

def test_iot_metamodel_communicator_has_Type():
    assert hasattr(ioT_metamodel_Communicator, "Type")
    descriptor = None
    for klass in ioT_metamodel_Communicator.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)



def test_iot_metamodel_devicestate_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_DeviceState)


def test_iot_metamodel_devicestate_constructor_exists():
    assert callable(ioT_metamodel_DeviceState.__init__)


def test_iot_metamodel_devicestate_constructor_args():
    sig = inspect.signature(ioT_metamodel_DeviceState.__init__)
    params = list(sig.parameters.keys())
    assert "Enabled" in params, "Missing parameter 'Enabled'"

def test_iot_metamodel_devicestate_has_Enabled():
    assert hasattr(ioT_metamodel_DeviceState, "Enabled")
    descriptor = None
    for klass in ioT_metamodel_DeviceState.__mro__:
        if "Enabled" in klass.__dict__:
            descriptor = klass.__dict__["Enabled"]
            break
    assert isinstance(descriptor, property)



def test_iot_metamodel_rule_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_Rule)


def test_iot_metamodel_rule_constructor_exists():
    assert callable(ioT_metamodel_Rule.__init__)


def test_iot_metamodel_rule_constructor_args():
    sig = inspect.signature(ioT_metamodel_Rule.__init__)
    params = list(sig.parameters.keys())
    assert "conditionValue" in params, "Missing parameter 'conditionValue'"
    assert "conditionLiteral" in params, "Missing parameter 'conditionLiteral'"

def test_iot_metamodel_rule_has_conditionValue():
    assert hasattr(ioT_metamodel_Rule, "conditionValue")
    descriptor = None
    for klass in ioT_metamodel_Rule.__mro__:
        if "conditionValue" in klass.__dict__:
            descriptor = klass.__dict__["conditionValue"]
            break
    assert isinstance(descriptor, property)

def test_iot_metamodel_rule_has_conditionLiteral():
    assert hasattr(ioT_metamodel_Rule, "conditionLiteral")
    descriptor = None
    for klass in ioT_metamodel_Rule.__mro__:
        if "conditionLiteral" in klass.__dict__:
            descriptor = klass.__dict__["conditionLiteral"]
            break
    assert isinstance(descriptor, property)



def test_physicalthing_is_not_abstract():
    assert not inspect.isabstract(PhysicalThing)


def test_physicalthing_constructor_exists():
    assert callable(PhysicalThing.__init__)


def test_physicalthing_constructor_args():
    sig = inspect.signature(PhysicalThing.__init__)
    params = list(sig.parameters.keys())



def test_iot_metamodel_fog_services_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_Fog_Services)


def test_iot_metamodel_fog_services_constructor_exists():
    assert callable(ioT_metamodel_Fog_Services.__init__)


def test_iot_metamodel_fog_services_constructor_args():
    sig = inspect.signature(ioT_metamodel_Fog_Services.__init__)
    params = list(sig.parameters.keys())



def test_iot_metamodel_analytics_engine_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_Analytics_Engine)


def test_iot_metamodel_analytics_engine_constructor_exists():
    assert callable(ioT_metamodel_Analytics_Engine.__init__)


def test_iot_metamodel_analytics_engine_constructor_args():
    sig = inspect.signature(ioT_metamodel_Analytics_Engine.__init__)
    params = list(sig.parameters.keys())



def test_iot_metamodel_container_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_Container)


def test_iot_metamodel_container_constructor_exists():
    assert callable(ioT_metamodel_Container.__init__)


def test_iot_metamodel_container_constructor_args():
    sig = inspect.signature(ioT_metamodel_Container.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"
    assert "IP_address" in params, "Missing parameter 'IP_address'"

def test_iot_metamodel_container_has_ID():
    assert hasattr(ioT_metamodel_Container, "ID")
    descriptor = None
    for klass in ioT_metamodel_Container.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_iot_metamodel_container_has_IP_address():
    assert hasattr(ioT_metamodel_Container, "IP_address")
    descriptor = None
    for klass in ioT_metamodel_Container.__mro__:
        if "IP_address" in klass.__dict__:
            descriptor = klass.__dict__["IP_address"]
            break
    assert isinstance(descriptor, property)



def test_iot_metamodel_vm_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_VM)


def test_iot_metamodel_vm_constructor_exists():
    assert callable(ioT_metamodel_VM.__init__)


def test_iot_metamodel_vm_constructor_args():
    sig = inspect.signature(ioT_metamodel_VM.__init__)
    params = list(sig.parameters.keys())



def test_iot_metamodel_authorizor_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_Authorizor)


def test_iot_metamodel_authorizor_constructor_exists():
    assert callable(ioT_metamodel_Authorizor.__init__)


def test_iot_metamodel_authorizor_constructor_args():
    sig = inspect.signature(ioT_metamodel_Authorizor.__init__)
    params = list(sig.parameters.keys())



def test_iot_metamodel_device_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_Device)


def test_iot_metamodel_device_constructor_exists():
    assert callable(ioT_metamodel_Device.__init__)


def test_iot_metamodel_device_constructor_args():
    sig = inspect.signature(ioT_metamodel_Device.__init__)
    params = list(sig.parameters.keys())
    assert "Technology" in params, "Missing parameter 'Technology'"

def test_iot_metamodel_device_has_Technology():
    assert hasattr(ioT_metamodel_Device, "Technology")
    descriptor = None
    for klass in ioT_metamodel_Device.__mro__:
        if "Technology" in klass.__dict__:
            descriptor = klass.__dict__["Technology"]
            break
    assert isinstance(descriptor, property)



def test_iot_metamodel_informationresource_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_InformationResource)


def test_iot_metamodel_informationresource_constructor_exists():
    assert callable(ioT_metamodel_InformationResource.__init__)


def test_iot_metamodel_informationresource_constructor_args():
    sig = inspect.signature(ioT_metamodel_InformationResource.__init__)
    params = list(sig.parameters.keys())



def test_passive_digital_artifact_is_not_abstract():
    assert not inspect.isabstract(Passive_Digital_Artifact)


def test_passive_digital_artifact_constructor_exists():
    assert callable(Passive_Digital_Artifact.__init__)


def test_passive_digital_artifact_constructor_args():
    sig = inspect.signature(Passive_Digital_Artifact.__init__)
    params = list(sig.parameters.keys())



def test_active_digital_artifact_is_not_abstract():
    assert not inspect.isabstract(Active_Digital_Artifact)


def test_active_digital_artifact_constructor_exists():
    assert callable(Active_Digital_Artifact.__init__)


def test_active_digital_artifact_constructor_args():
    sig = inspect.signature(Active_Digital_Artifact.__init__)
    params = list(sig.parameters.keys())



def test_iot_metamodel_property_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_Property)


def test_iot_metamodel_property_constructor_exists():
    assert callable(ioT_metamodel_Property.__init__)


def test_iot_metamodel_property_constructor_args():
    sig = inspect.signature(ioT_metamodel_Property.__init__)
    params = list(sig.parameters.keys())
    assert "changeable" in params, "Missing parameter 'changeable'"

def test_iot_metamodel_property_has_changeable():
    assert hasattr(ioT_metamodel_Property, "changeable")
    descriptor = None
    for klass in ioT_metamodel_Property.__mro__:
        if "changeable" in klass.__dict__:
            descriptor = klass.__dict__["changeable"]
            break
    assert isinstance(descriptor, property)



def test_iot_metamodel_physicalthing_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_PhysicalThing)


def test_iot_metamodel_physicalthing_constructor_exists():
    assert callable(ioT_metamodel_PhysicalThing.__init__)


def test_iot_metamodel_physicalthing_constructor_args():
    sig = inspect.signature(ioT_metamodel_PhysicalThing.__init__)
    params = list(sig.parameters.keys())



def test_iot_metamodel_fog_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_Fog)


def test_iot_metamodel_fog_constructor_exists():
    assert callable(ioT_metamodel_Fog.__init__)


def test_iot_metamodel_fog_constructor_args():
    sig = inspect.signature(ioT_metamodel_Fog.__init__)
    params = list(sig.parameters.keys())



def test_iot_metamodel_virtualthing_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_VirtualThing)


def test_iot_metamodel_virtualthing_constructor_exists():
    assert callable(ioT_metamodel_VirtualThing.__init__)


def test_iot_metamodel_virtualthing_constructor_args():
    sig = inspect.signature(ioT_metamodel_VirtualThing.__init__)
    params = list(sig.parameters.keys())
    assert "URI" in params, "Missing parameter 'URI'"

def test_iot_metamodel_virtualthing_has_URI():
    assert hasattr(ioT_metamodel_VirtualThing, "URI")
    descriptor = None
    for klass in ioT_metamodel_VirtualThing.__mro__:
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



def test_iot_metamodel_user_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_User)


def test_iot_metamodel_user_constructor_exists():
    assert callable(ioT_metamodel_User.__init__)


def test_iot_metamodel_user_constructor_args():
    sig = inspect.signature(ioT_metamodel_User.__init__)
    params = list(sig.parameters.keys())



def test_iot_metamodel_attribute_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_Attribute)


def test_iot_metamodel_attribute_constructor_exists():
    assert callable(ioT_metamodel_Attribute.__init__)


def test_iot_metamodel_attribute_constructor_args():
    sig = inspect.signature(ioT_metamodel_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "Type" in params, "Missing parameter 'Type'"

def test_iot_metamodel_attribute_has_name():
    assert hasattr(ioT_metamodel_Attribute, "name")
    descriptor = None
    for klass in ioT_metamodel_Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_iot_metamodel_attribute_has_Type():
    assert hasattr(ioT_metamodel_Attribute, "Type")
    descriptor = None
    for klass in ioT_metamodel_Attribute.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)



def test_iot_metamodel_thing_is_not_abstract():
    assert not inspect.isabstract(ioT_metamodel_Thing)


def test_iot_metamodel_thing_constructor_exists():
    assert callable(ioT_metamodel_Thing.__init__)


def test_iot_metamodel_thing_constructor_args():
    sig = inspect.signature(ioT_metamodel_Thing.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iot_metamodel_thing_has_name():
    assert hasattr(ioT_metamodel_Thing, "name")
    descriptor = None
    for klass in ioT_metamodel_Thing.__mro__:
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
ioT_metamodel_Entity_strategy = st.builds(
    ioT_metamodel_Entity,
)
Evaluators_strategy = st.builds(
    Evaluators,
)
ioT_metamodel_ScriptEvaluator_strategy = st.builds(
    ioT_metamodel_ScriptEvaluator,
)
ioT_metamodel_JavaEvaluator_strategy = st.builds(
    ioT_metamodel_JavaEvaluator,
)
ioT_metamodel_Evaluators_strategy = st.builds(
    ioT_metamodel_Evaluators,
)
ioT_metamodel_Operations_strategy = st.builds(
    ioT_metamodel_Operations,
)
ioT_metamodel_AtomicDataAttributes_strategy = st.builds(
    ioT_metamodel_AtomicDataAttributes,
    DeviceID=
        safe_text,
    DataEncoding=
        safe_text
)
ioT_metamodel_DataStreamAttributes_strategy = st.builds(
    ioT_metamodel_DataStreamAttributes,
    Timestamp=
        safe_text,
    DataFormat=
        safe_text,
    Description=
        safe_text,
    DataEncoding=
        safe_text,
    MaxBitrate=
        safe_text,
    DeviceID=
        safe_text,
    MeanBitRate=
        safe_text
)
ioT_metamodel_DataStreams_strategy = st.builds(
    ioT_metamodel_DataStreams,
)
ioT_metamodel_AtomicData_strategy = st.builds(
    ioT_metamodel_AtomicData,
)
ioT_metamodel_Reference_Monitor_strategy = st.builds(
    ioT_metamodel_Reference_Monitor,
)
ioT_metamodel_Policy_Repository_strategy = st.builds(
    ioT_metamodel_Policy_Repository,
)
User_strategy = st.builds(
    User,
)
Digital_Artifact_strategy = st.builds(
    Digital_Artifact,
)
ioT_metamodel_Passive_Digital_Artifact_strategy = st.builds(
    ioT_metamodel_Passive_Digital_Artifact,
)
ioT_metamodel_Active_Digital_Artifact_strategy = st.builds(
    ioT_metamodel_Active_Digital_Artifact,
)
ioT_metamodel_Digital_Artifact_strategy = st.builds(
    ioT_metamodel_Digital_Artifact,
)
ioT_metamodel_Service_Resource_strategy = st.builds(
    ioT_metamodel_Service_Resource,
)
ioT_metamodel_Device_Resource_strategy = st.builds(
    ioT_metamodel_Device_Resource,
)
InformationResource_strategy = st.builds(
    InformationResource,
)
ioT_metamodel_Network_Resource_strategy = st.builds(
    ioT_metamodel_Network_Resource,
)
ioT_metamodel_Information_strategy = st.builds(
    ioT_metamodel_Information,
)
ioT_metamodel_Port_strategy = st.builds(
    ioT_metamodel_Port,
)
ioT_metamodel_Human_User_strategy = st.builds(
    ioT_metamodel_Human_User,
)
ioT_metamodel_Transition_strategy = st.builds(
    ioT_metamodel_Transition,
)
DeviceState_strategy = st.builds(
    DeviceState,
)
ioT_metamodel_CompositeState_strategy = st.builds(
    ioT_metamodel_CompositeState,
)
Actuator_strategy = st.builds(
    Actuator,
)
ioT_metamodel_ExternalActuator_strategy = st.builds(
    ioT_metamodel_ExternalActuator,
)
ioT_metamodel_DeviceActuator_strategy = st.builds(
    ioT_metamodel_DeviceActuator,
)
Sensor_strategy = st.builds(
    Sensor,
)
ioT_metamodel_DeviceSensor_strategy = st.builds(
    ioT_metamodel_DeviceSensor,
)
ioT_metamodel_ExternalSensor_strategy = st.builds(
    ioT_metamodel_ExternalSensor,
)
ioT_metamodel_Action_strategy = st.builds(
    ioT_metamodel_Action,
    Description=
        safe_text
)
ioT_metamodel_Database_strategy = st.builds(
    ioT_metamodel_Database,
)
ioT_metamodel_Cloud_strategy = st.builds(
    ioT_metamodel_Cloud,
)
ioT_metamodel_FogNode_strategy = st.builds(
    ioT_metamodel_FogNode,
)
Device_strategy = st.builds(
    Device,
)
ioT_metamodel_Sensor_strategy = st.builds(
    ioT_metamodel_Sensor,
    Name=
        safe_text,
    State=
        st.booleans(),
    frequency=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ioT_metamodel_Tag_strategy = st.builds(
    ioT_metamodel_Tag,
    Name=
        safe_text
)
ioT_metamodel_Actuator_strategy = st.builds(
    ioT_metamodel_Actuator,
    name=
        safe_text
)
ioT_metamodel_On_Device_Resource_strategy = st.builds(
    ioT_metamodel_On_Device_Resource,
)
ioT_metamodel_Communicator_strategy = st.builds(
    ioT_metamodel_Communicator,
    ports_number=
        st.integers(),
    Type=
        safe_text
)
ioT_metamodel_DeviceState_strategy = st.builds(
    ioT_metamodel_DeviceState,
    Enabled=
        st.booleans()
)
ioT_metamodel_Rule_strategy = st.builds(
    ioT_metamodel_Rule,
    conditionValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    conditionLiteral=
        safe_text
)
PhysicalThing_strategy = st.builds(
    PhysicalThing,
)
ioT_metamodel_Fog_Services_strategy = st.builds(
    ioT_metamodel_Fog_Services,
)
ioT_metamodel_Analytics_Engine_strategy = st.builds(
    ioT_metamodel_Analytics_Engine,
)
ioT_metamodel_Container_strategy = st.builds(
    ioT_metamodel_Container,
    ID=
        safe_text,
    IP_address=
        safe_text
)
ioT_metamodel_VM_strategy = st.builds(
    ioT_metamodel_VM,
)
ioT_metamodel_Authorizor_strategy = st.builds(
    ioT_metamodel_Authorizor,
)
ioT_metamodel_Device_strategy = st.builds(
    ioT_metamodel_Device,
    Technology=
        safe_text
)
ioT_metamodel_InformationResource_strategy = st.builds(
    ioT_metamodel_InformationResource,
)
Passive_Digital_Artifact_strategy = st.builds(
    Passive_Digital_Artifact,
)
Active_Digital_Artifact_strategy = st.builds(
    Active_Digital_Artifact,
)
ioT_metamodel_Property_strategy = st.builds(
    ioT_metamodel_Property,
    changeable=
        st.booleans()
)
ioT_metamodel_PhysicalThing_strategy = st.builds(
    ioT_metamodel_PhysicalThing,
)
ioT_metamodel_Fog_strategy = st.builds(
    ioT_metamodel_Fog,
)
ioT_metamodel_VirtualThing_strategy = st.builds(
    ioT_metamodel_VirtualThing,
    URI=
        safe_text
)
Entity_strategy = st.builds(
    Entity,
)
ioT_metamodel_User_strategy = st.builds(
    ioT_metamodel_User,
)
ioT_metamodel_Attribute_strategy = st.builds(
    ioT_metamodel_Attribute,
    name=
        safe_text,
    Type=
        safe_text
)
ioT_metamodel_Thing_strategy = st.builds(
    ioT_metamodel_Thing,
    name=
        safe_text
)

@given(instance=ioT_metamodel_Entity_strategy)
@settings(max_examples=50)
def test_iot_metamodel_entity_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_Entity)

@given(instance=Evaluators_strategy)
@settings(max_examples=50)
def test_evaluators_instantiation(instance):
    assert isinstance(instance, Evaluators)

@given(instance=ioT_metamodel_ScriptEvaluator_strategy)
@settings(max_examples=50)
def test_iot_metamodel_scriptevaluator_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_ScriptEvaluator)

@given(instance=ioT_metamodel_JavaEvaluator_strategy)
@settings(max_examples=50)
def test_iot_metamodel_javaevaluator_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_JavaEvaluator)

@given(instance=ioT_metamodel_Evaluators_strategy)
@settings(max_examples=50)
def test_iot_metamodel_evaluators_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_Evaluators)

@given(instance=ioT_metamodel_Operations_strategy)
@settings(max_examples=50)
def test_iot_metamodel_operations_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_Operations)

@given(instance=ioT_metamodel_AtomicDataAttributes_strategy)
@settings(max_examples=50)
def test_iot_metamodel_atomicdataattributes_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_AtomicDataAttributes)



@given(instance=ioT_metamodel_AtomicDataAttributes_strategy)
def test_iot_metamodel_atomicdataattributes_DeviceID_setter(instance):
    original = instance.DeviceID
    instance.DeviceID = original
    assert instance.DeviceID == original



@given(instance=ioT_metamodel_AtomicDataAttributes_strategy)
def test_iot_metamodel_atomicdataattributes_DataEncoding_setter(instance):
    original = instance.DataEncoding
    instance.DataEncoding = original
    assert instance.DataEncoding == original

@given(instance=ioT_metamodel_DataStreamAttributes_strategy)
@settings(max_examples=50)
def test_iot_metamodel_datastreamattributes_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_DataStreamAttributes)



@given(instance=ioT_metamodel_DataStreamAttributes_strategy)
def test_iot_metamodel_datastreamattributes_Timestamp_setter(instance):
    original = instance.Timestamp
    instance.Timestamp = original
    assert instance.Timestamp == original



@given(instance=ioT_metamodel_DataStreamAttributes_strategy)
def test_iot_metamodel_datastreamattributes_DataFormat_setter(instance):
    original = instance.DataFormat
    instance.DataFormat = original
    assert instance.DataFormat == original



@given(instance=ioT_metamodel_DataStreamAttributes_strategy)
def test_iot_metamodel_datastreamattributes_Description_setter(instance):
    original = instance.Description
    instance.Description = original
    assert instance.Description == original



@given(instance=ioT_metamodel_DataStreamAttributes_strategy)
def test_iot_metamodel_datastreamattributes_DataEncoding_setter(instance):
    original = instance.DataEncoding
    instance.DataEncoding = original
    assert instance.DataEncoding == original



@given(instance=ioT_metamodel_DataStreamAttributes_strategy)
def test_iot_metamodel_datastreamattributes_MaxBitrate_setter(instance):
    original = instance.MaxBitrate
    instance.MaxBitrate = original
    assert instance.MaxBitrate == original



@given(instance=ioT_metamodel_DataStreamAttributes_strategy)
def test_iot_metamodel_datastreamattributes_DeviceID_setter(instance):
    original = instance.DeviceID
    instance.DeviceID = original
    assert instance.DeviceID == original



@given(instance=ioT_metamodel_DataStreamAttributes_strategy)
def test_iot_metamodel_datastreamattributes_MeanBitRate_setter(instance):
    original = instance.MeanBitRate
    instance.MeanBitRate = original
    assert instance.MeanBitRate == original

@given(instance=ioT_metamodel_DataStreams_strategy)
@settings(max_examples=50)
def test_iot_metamodel_datastreams_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_DataStreams)

@given(instance=ioT_metamodel_AtomicData_strategy)
@settings(max_examples=50)
def test_iot_metamodel_atomicdata_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_AtomicData)

@given(instance=ioT_metamodel_Reference_Monitor_strategy)
@settings(max_examples=50)
def test_iot_metamodel_reference_monitor_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_Reference_Monitor)

@given(instance=ioT_metamodel_Policy_Repository_strategy)
@settings(max_examples=50)
def test_iot_metamodel_policy_repository_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_Policy_Repository)

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)

@given(instance=Digital_Artifact_strategy)
@settings(max_examples=50)
def test_digital_artifact_instantiation(instance):
    assert isinstance(instance, Digital_Artifact)

@given(instance=ioT_metamodel_Passive_Digital_Artifact_strategy)
@settings(max_examples=50)
def test_iot_metamodel_passive_digital_artifact_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_Passive_Digital_Artifact)

@given(instance=ioT_metamodel_Active_Digital_Artifact_strategy)
@settings(max_examples=50)
def test_iot_metamodel_active_digital_artifact_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_Active_Digital_Artifact)

@given(instance=ioT_metamodel_Digital_Artifact_strategy)
@settings(max_examples=50)
def test_iot_metamodel_digital_artifact_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_Digital_Artifact)

@given(instance=ioT_metamodel_Service_Resource_strategy)
@settings(max_examples=50)
def test_iot_metamodel_service_resource_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_Service_Resource)

@given(instance=ioT_metamodel_Device_Resource_strategy)
@settings(max_examples=50)
def test_iot_metamodel_device_resource_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_Device_Resource)

@given(instance=InformationResource_strategy)
@settings(max_examples=50)
def test_informationresource_instantiation(instance):
    assert isinstance(instance, InformationResource)

@given(instance=ioT_metamodel_Network_Resource_strategy)
@settings(max_examples=50)
def test_iot_metamodel_network_resource_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_Network_Resource)

@given(instance=ioT_metamodel_Information_strategy)
@settings(max_examples=50)
def test_iot_metamodel_information_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_Information)

@given(instance=ioT_metamodel_Port_strategy)
@settings(max_examples=50)
def test_iot_metamodel_port_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_Port)

@given(instance=ioT_metamodel_Human_User_strategy)
@settings(max_examples=50)
def test_iot_metamodel_human_user_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_Human_User)

@given(instance=ioT_metamodel_Transition_strategy)
@settings(max_examples=50)
def test_iot_metamodel_transition_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_Transition)

@given(instance=DeviceState_strategy)
@settings(max_examples=50)
def test_devicestate_instantiation(instance):
    assert isinstance(instance, DeviceState)

@given(instance=ioT_metamodel_CompositeState_strategy)
@settings(max_examples=50)
def test_iot_metamodel_compositestate_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_CompositeState)

@given(instance=Actuator_strategy)
@settings(max_examples=50)
def test_actuator_instantiation(instance):
    assert isinstance(instance, Actuator)

@given(instance=ioT_metamodel_ExternalActuator_strategy)
@settings(max_examples=50)
def test_iot_metamodel_externalactuator_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_ExternalActuator)

@given(instance=ioT_metamodel_DeviceActuator_strategy)
@settings(max_examples=50)
def test_iot_metamodel_deviceactuator_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_DeviceActuator)

@given(instance=Sensor_strategy)
@settings(max_examples=50)
def test_sensor_instantiation(instance):
    assert isinstance(instance, Sensor)

@given(instance=ioT_metamodel_DeviceSensor_strategy)
@settings(max_examples=50)
def test_iot_metamodel_devicesensor_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_DeviceSensor)

@given(instance=ioT_metamodel_ExternalSensor_strategy)
@settings(max_examples=50)
def test_iot_metamodel_externalsensor_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_ExternalSensor)

@given(instance=ioT_metamodel_Action_strategy)
@settings(max_examples=50)
def test_iot_metamodel_action_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_Action)



@given(instance=ioT_metamodel_Action_strategy)
def test_iot_metamodel_action_Description_setter(instance):
    original = instance.Description
    instance.Description = original
    assert instance.Description == original

@given(instance=ioT_metamodel_Database_strategy)
@settings(max_examples=50)
def test_iot_metamodel_database_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_Database)

@given(instance=ioT_metamodel_Cloud_strategy)
@settings(max_examples=50)
def test_iot_metamodel_cloud_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_Cloud)

@given(instance=ioT_metamodel_FogNode_strategy)
@settings(max_examples=50)
def test_iot_metamodel_fognode_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_FogNode)

@given(instance=Device_strategy)
@settings(max_examples=50)
def test_device_instantiation(instance):
    assert isinstance(instance, Device)

@given(instance=ioT_metamodel_Sensor_strategy)
@settings(max_examples=50)
def test_iot_metamodel_sensor_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_Sensor)



@given(instance=ioT_metamodel_Sensor_strategy)
def test_iot_metamodel_sensor_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=ioT_metamodel_Sensor_strategy)
def test_iot_metamodel_sensor_State_setter(instance):
    original = instance.State
    instance.State = original
    assert instance.State == original



@given(instance=ioT_metamodel_Sensor_strategy)
def test_iot_metamodel_sensor_frequency_setter(instance):
    original = instance.frequency
    instance.frequency = original
    assert instance.frequency == original

@given(instance=ioT_metamodel_Tag_strategy)
@settings(max_examples=50)
def test_iot_metamodel_tag_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_Tag)



@given(instance=ioT_metamodel_Tag_strategy)
def test_iot_metamodel_tag_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=ioT_metamodel_Actuator_strategy)
@settings(max_examples=50)
def test_iot_metamodel_actuator_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_Actuator)



@given(instance=ioT_metamodel_Actuator_strategy)
def test_iot_metamodel_actuator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ioT_metamodel_On_Device_Resource_strategy)
@settings(max_examples=50)
def test_iot_metamodel_on_device_resource_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_On_Device_Resource)

@given(instance=ioT_metamodel_Communicator_strategy)
@settings(max_examples=50)
def test_iot_metamodel_communicator_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_Communicator)



@given(instance=ioT_metamodel_Communicator_strategy)
def test_iot_metamodel_communicator_ports_number_setter(instance):
    original = instance.ports_number
    instance.ports_number = original
    assert instance.ports_number == original



@given(instance=ioT_metamodel_Communicator_strategy)
def test_iot_metamodel_communicator_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original

@given(instance=ioT_metamodel_DeviceState_strategy)
@settings(max_examples=50)
def test_iot_metamodel_devicestate_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_DeviceState)



@given(instance=ioT_metamodel_DeviceState_strategy)
def test_iot_metamodel_devicestate_Enabled_setter(instance):
    original = instance.Enabled
    instance.Enabled = original
    assert instance.Enabled == original

@given(instance=ioT_metamodel_Rule_strategy)
@settings(max_examples=50)
def test_iot_metamodel_rule_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_Rule)



@given(instance=ioT_metamodel_Rule_strategy)
def test_iot_metamodel_rule_conditionValue_setter(instance):
    original = instance.conditionValue
    instance.conditionValue = original
    assert instance.conditionValue == original



@given(instance=ioT_metamodel_Rule_strategy)
def test_iot_metamodel_rule_conditionLiteral_setter(instance):
    original = instance.conditionLiteral
    instance.conditionLiteral = original
    assert instance.conditionLiteral == original

@given(instance=PhysicalThing_strategy)
@settings(max_examples=50)
def test_physicalthing_instantiation(instance):
    assert isinstance(instance, PhysicalThing)

@given(instance=ioT_metamodel_Fog_Services_strategy)
@settings(max_examples=50)
def test_iot_metamodel_fog_services_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_Fog_Services)

@given(instance=ioT_metamodel_Analytics_Engine_strategy)
@settings(max_examples=50)
def test_iot_metamodel_analytics_engine_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_Analytics_Engine)

@given(instance=ioT_metamodel_Container_strategy)
@settings(max_examples=50)
def test_iot_metamodel_container_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_Container)



@given(instance=ioT_metamodel_Container_strategy)
def test_iot_metamodel_container_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=ioT_metamodel_Container_strategy)
def test_iot_metamodel_container_IP_address_setter(instance):
    original = instance.IP_address
    instance.IP_address = original
    assert instance.IP_address == original

@given(instance=ioT_metamodel_VM_strategy)
@settings(max_examples=50)
def test_iot_metamodel_vm_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_VM)

@given(instance=ioT_metamodel_Authorizor_strategy)
@settings(max_examples=50)
def test_iot_metamodel_authorizor_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_Authorizor)

@given(instance=ioT_metamodel_Device_strategy)
@settings(max_examples=50)
def test_iot_metamodel_device_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_Device)



@given(instance=ioT_metamodel_Device_strategy)
def test_iot_metamodel_device_Technology_setter(instance):
    original = instance.Technology
    instance.Technology = original
    assert instance.Technology == original

@given(instance=ioT_metamodel_InformationResource_strategy)
@settings(max_examples=50)
def test_iot_metamodel_informationresource_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_InformationResource)

@given(instance=Passive_Digital_Artifact_strategy)
@settings(max_examples=50)
def test_passive_digital_artifact_instantiation(instance):
    assert isinstance(instance, Passive_Digital_Artifact)

@given(instance=Active_Digital_Artifact_strategy)
@settings(max_examples=50)
def test_active_digital_artifact_instantiation(instance):
    assert isinstance(instance, Active_Digital_Artifact)

@given(instance=ioT_metamodel_Property_strategy)
@settings(max_examples=50)
def test_iot_metamodel_property_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_Property)



@given(instance=ioT_metamodel_Property_strategy)
def test_iot_metamodel_property_changeable_setter(instance):
    original = instance.changeable
    instance.changeable = original
    assert instance.changeable == original

@given(instance=ioT_metamodel_PhysicalThing_strategy)
@settings(max_examples=50)
def test_iot_metamodel_physicalthing_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_PhysicalThing)

@given(instance=ioT_metamodel_Fog_strategy)
@settings(max_examples=50)
def test_iot_metamodel_fog_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_Fog)

@given(instance=ioT_metamodel_VirtualThing_strategy)
@settings(max_examples=50)
def test_iot_metamodel_virtualthing_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_VirtualThing)



@given(instance=ioT_metamodel_VirtualThing_strategy)
def test_iot_metamodel_virtualthing_URI_setter(instance):
    original = instance.URI
    instance.URI = original
    assert instance.URI == original

@given(instance=Entity_strategy)
@settings(max_examples=50)
def test_entity_instantiation(instance):
    assert isinstance(instance, Entity)

@given(instance=ioT_metamodel_User_strategy)
@settings(max_examples=50)
def test_iot_metamodel_user_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_User)

@given(instance=ioT_metamodel_Attribute_strategy)
@settings(max_examples=50)
def test_iot_metamodel_attribute_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_Attribute)



@given(instance=ioT_metamodel_Attribute_strategy)
def test_iot_metamodel_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ioT_metamodel_Attribute_strategy)
def test_iot_metamodel_attribute_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original

@given(instance=ioT_metamodel_Thing_strategy)
@settings(max_examples=50)
def test_iot_metamodel_thing_instantiation(instance):
    assert isinstance(instance, ioT_metamodel_Thing)



@given(instance=ioT_metamodel_Thing_strategy)
def test_iot_metamodel_thing_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
