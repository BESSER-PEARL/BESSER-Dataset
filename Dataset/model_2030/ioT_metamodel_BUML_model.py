####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Classes
ioT_metamodel_VirtualThing = Class(name="ioT::metamodel::VirtualThing")
ioT_metamodel_Fog = Class(name="ioT::metamodel::Fog")
ioT_metamodel_PhysicalThing = Class(name="ioT::metamodel::PhysicalThing")
ioT_metamodel_Thing = Class(name="ioT::metamodel::Thing")
Entity = Class(name="Entity")
ioT_metamodel_InformationResource = Class(name="ioT::metamodel::InformationResource")
ioT_metamodel_Device = Class(name="ioT::metamodel::Device")
ioT_metamodel_Property = Class(name="ioT::metamodel::Property")
Active_Digital_Artifact = Class(name="Active::Digital::Artifact")
Passive_Digital_Artifact = Class(name="Passive::Digital::Artifact")
ioT_metamodel_VM = Class(name="ioT::metamodel::VM")
ioT_metamodel_Container = Class(name="ioT::metamodel::Container")
ioT_metamodel_Analytics_Engine = Class(name="ioT::metamodel::Analytics::Engine")
ioT_metamodel_Fog_Services = Class(name="ioT::metamodel::Fog::Services")
PhysicalThing = Class(name="PhysicalThing")
ioT_metamodel_FogNode = Class(name="ioT::metamodel::FogNode")
ioT_metamodel_Cloud = Class(name="ioT::metamodel::Cloud")
ioT_metamodel_Database = Class(name="ioT::metamodel::Database")
ioT_metamodel_Authorizor = Class(name="ioT::metamodel::Authorizor")
ioT_metamodel_Tag = Class(name="ioT::metamodel::Tag")
ioT_metamodel_Sensor = Class(name="ioT::metamodel::Sensor", is_abstract=True)
ioT_metamodel_Rule = Class(name="ioT::metamodel::Rule")
ioT_metamodel_DeviceState = Class(name="ioT::metamodel::DeviceState")
ioT_metamodel_Communicator = Class(name="ioT::metamodel::Communicator")
ioT_metamodel_On_Device_Resource = Class(name="ioT::metamodel::On::Device::Resource")
ioT_metamodel_Actuator = Class(name="ioT::metamodel::Actuator")
Device = Class(name="Device")
ioT_metamodel_CompositeState = Class(name="ioT::metamodel::CompositeState")
DeviceState = Class(name="DeviceState")
ioT_metamodel_Transition = Class(name="ioT::metamodel::Transition")
ioT_metamodel_Digital_Artifact = Class(name="ioT::metamodel::Digital::Artifact")
ioT_metamodel_Active_Digital_Artifact = Class(name="ioT::metamodel::Active::Digital::Artifact")
Digital_Artifact = Class(name="Digital::Artifact")
User = Class(name="User")
ioT_metamodel_Action = Class(name="ioT::metamodel::Action")
ioT_metamodel_ExternalSensor = Class(name="ioT::metamodel::ExternalSensor")
Sensor = Class(name="Sensor")
ioT_metamodel_DeviceActuator = Class(name="ioT::metamodel::DeviceActuator")
Actuator = Class(name="Actuator")
ioT_metamodel_ExternalActuator = Class(name="ioT::metamodel::ExternalActuator")
InformationResource = Class(name="InformationResource")
ioT_metamodel_Device_Resource = Class(name="ioT::metamodel::Device::Resource")
ioT_metamodel_Service_Resource = Class(name="ioT::metamodel::Service::Resource")
ioT_metamodel_Network_Resource = Class(name="ioT::metamodel::Network::Resource")
ioT_metamodel_Passive_Digital_Artifact = Class(name="ioT::metamodel::Passive::Digital::Artifact")
ioT_metamodel_User = Class(name="ioT::metamodel::User")
ioT_metamodel_Human_User = Class(name="ioT::metamodel::Human::User")
ioT_metamodel_Port = Class(name="ioT::metamodel::Port")
ioT_metamodel_Information = Class(name="ioT::metamodel::Information")
ioT_metamodel_Attribute = Class(name="ioT::metamodel::Attribute", is_abstract=True)
ioT_metamodel_AtomicData = Class(name="ioT::metamodel::AtomicData")
ioT_metamodel_DataStreams = Class(name="ioT::metamodel::DataStreams")
ioT_metamodel_Policy_Repository = Class(name="ioT::metamodel::Policy::Repository")
ioT_metamodel_Reference_Monitor = Class(name="ioT::metamodel::Reference::Monitor")
ioT_metamodel_Operations = Class(name="ioT::metamodel::Operations")
ioT_metamodel_Evaluators = Class(name="ioT::metamodel::Evaluators", is_abstract=True)
ioT_metamodel_DataStreamAttributes = Class(name="ioT::metamodel::DataStreamAttributes", is_abstract=True)
ioT_metamodel_AtomicDataAttributes = Class(name="ioT::metamodel::AtomicDataAttributes", is_abstract=True)
ioT_metamodel_JavaEvaluator = Class(name="ioT::metamodel::JavaEvaluator")
Evaluators = Class(name="Evaluators")
ioT_metamodel_Entity = Class(name="ioT::metamodel::Entity")
ioT_metamodel_ScriptEvaluator = Class(name="ioT::metamodel::ScriptEvaluator")
ioT_metamodel_DeviceSensor = Class(name="ioT::metamodel::DeviceSensor")

# ioT_metamodel_VirtualThing class attributes and methods
ioT_metamodel_VirtualThing_URI: Property = Property(name="URI", type=StringType)
ioT_metamodel_VirtualThing.attributes={ioT_metamodel_VirtualThing_URI}

# ioT_metamodel_Fog class attributes and methods

# ioT_metamodel_PhysicalThing class attributes and methods

# ioT_metamodel_Thing class attributes and methods
ioT_metamodel_Thing_name: Property = Property(name="name", type=StringType)
ioT_metamodel_Thing.attributes={ioT_metamodel_Thing_name}

# Entity class attributes and methods

# ioT_metamodel_InformationResource class attributes and methods

# ioT_metamodel_Device class attributes and methods
ioT_metamodel_Device_Technology: Property = Property(name="Technology", type=StringType)
ioT_metamodel_Device.attributes={ioT_metamodel_Device_Technology}

# ioT_metamodel_Property class attributes and methods
ioT_metamodel_Property_changeable: Property = Property(name="changeable", type=BooleanType)
ioT_metamodel_Property.attributes={ioT_metamodel_Property_changeable}

# Active_Digital_Artifact class attributes and methods

# Passive_Digital_Artifact class attributes and methods

# ioT_metamodel_VM class attributes and methods

# ioT_metamodel_Container class attributes and methods
ioT_metamodel_Container_ID: Property = Property(name="ID", type=StringType)
ioT_metamodel_Container_IP_address: Property = Property(name="IP_address", type=StringType)
ioT_metamodel_Container.attributes={ioT_metamodel_Container_IP_address, ioT_metamodel_Container_ID}

# ioT_metamodel_Analytics_Engine class attributes and methods

# ioT_metamodel_Fog_Services class attributes and methods

# PhysicalThing class attributes and methods

# ioT_metamodel_FogNode class attributes and methods

# ioT_metamodel_Cloud class attributes and methods

# ioT_metamodel_Database class attributes and methods

# ioT_metamodel_Authorizor class attributes and methods

# ioT_metamodel_Tag class attributes and methods
ioT_metamodel_Tag_Name: Property = Property(name="Name", type=StringType)
ioT_metamodel_Tag.attributes={ioT_metamodel_Tag_Name}

# ioT_metamodel_Sensor class attributes and methods
ioT_metamodel_Sensor_Name: Property = Property(name="Name", type=StringType)
ioT_metamodel_Sensor_State: Property = Property(name="State", type=BooleanType)
ioT_metamodel_Sensor_frequency: Property = Property(name="frequency", type=FloatType)
ioT_metamodel_Sensor.attributes={ioT_metamodel_Sensor_State, ioT_metamodel_Sensor_frequency, ioT_metamodel_Sensor_Name}

# ioT_metamodel_Rule class attributes and methods
ioT_metamodel_Rule_conditionLiteral: Property = Property(name="conditionLiteral", type=StringType)
ioT_metamodel_Rule_conditionValue: Property = Property(name="conditionValue", type=FloatType)
ioT_metamodel_Rule.attributes={ioT_metamodel_Rule_conditionLiteral, ioT_metamodel_Rule_conditionValue}

# ioT_metamodel_DeviceState class attributes and methods
ioT_metamodel_DeviceState_Enabled: Property = Property(name="Enabled", type=BooleanType)
ioT_metamodel_DeviceState.attributes={ioT_metamodel_DeviceState_Enabled}

# ioT_metamodel_Communicator class attributes and methods
ioT_metamodel_Communicator_Type: Property = Property(name="Type", type=StringType)
ioT_metamodel_Communicator_ports_number: Property = Property(name="ports_number", type=IntegerType)
ioT_metamodel_Communicator.attributes={ioT_metamodel_Communicator_ports_number, ioT_metamodel_Communicator_Type}

# ioT_metamodel_On_Device_Resource class attributes and methods

# ioT_metamodel_Actuator class attributes and methods
ioT_metamodel_Actuator_name: Property = Property(name="name", type=StringType)
ioT_metamodel_Actuator.attributes={ioT_metamodel_Actuator_name}

# Device class attributes and methods

# ioT_metamodel_CompositeState class attributes and methods

# DeviceState class attributes and methods

# ioT_metamodel_Transition class attributes and methods

# ioT_metamodel_Digital_Artifact class attributes and methods

# ioT_metamodel_Active_Digital_Artifact class attributes and methods

# Digital_Artifact class attributes and methods

# User class attributes and methods

# ioT_metamodel_Action class attributes and methods
ioT_metamodel_Action_Description: Property = Property(name="Description", type=StringType)
ioT_metamodel_Action.attributes={ioT_metamodel_Action_Description}

# ioT_metamodel_ExternalSensor class attributes and methods

# Sensor class attributes and methods

# ioT_metamodel_DeviceActuator class attributes and methods

# Actuator class attributes and methods

# ioT_metamodel_ExternalActuator class attributes and methods

# InformationResource class attributes and methods

# ioT_metamodel_Device_Resource class attributes and methods

# ioT_metamodel_Service_Resource class attributes and methods

# ioT_metamodel_Network_Resource class attributes and methods

# ioT_metamodel_Passive_Digital_Artifact class attributes and methods

# ioT_metamodel_User class attributes and methods

# ioT_metamodel_Human_User class attributes and methods

# ioT_metamodel_Port class attributes and methods

# ioT_metamodel_Information class attributes and methods

# ioT_metamodel_Attribute class attributes and methods
ioT_metamodel_Attribute_name: Property = Property(name="name", type=StringType)
ioT_metamodel_Attribute_Type: Property = Property(name="Type", type=StringType)
ioT_metamodel_Attribute.attributes={ioT_metamodel_Attribute_name, ioT_metamodel_Attribute_Type}

# ioT_metamodel_AtomicData class attributes and methods

# ioT_metamodel_DataStreams class attributes and methods

# ioT_metamodel_Policy_Repository class attributes and methods

# ioT_metamodel_Reference_Monitor class attributes and methods

# ioT_metamodel_Operations class attributes and methods

# ioT_metamodel_Evaluators class attributes and methods

# ioT_metamodel_DataStreamAttributes class attributes and methods
ioT_metamodel_DataStreamAttributes_MeanBitRate: Property = Property(name="MeanBitRate", type=StringType)
ioT_metamodel_DataStreamAttributes_Timestamp: Property = Property(name="Timestamp", type=StringType)
ioT_metamodel_DataStreamAttributes_MaxBitrate: Property = Property(name="MaxBitrate", type=StringType)
ioT_metamodel_DataStreamAttributes_Description: Property = Property(name="Description", type=StringType)
ioT_metamodel_DataStreamAttributes_DataFormat: Property = Property(name="DataFormat", type=StringType)
ioT_metamodel_DataStreamAttributes_DataEncoding: Property = Property(name="DataEncoding", type=StringType)
ioT_metamodel_DataStreamAttributes_DeviceID: Property = Property(name="DeviceID", type=StringType)
ioT_metamodel_DataStreamAttributes.attributes={ioT_metamodel_DataStreamAttributes_DataEncoding, ioT_metamodel_DataStreamAttributes_MeanBitRate, ioT_metamodel_DataStreamAttributes_MaxBitrate, ioT_metamodel_DataStreamAttributes_DeviceID, ioT_metamodel_DataStreamAttributes_DataFormat, ioT_metamodel_DataStreamAttributes_Description, ioT_metamodel_DataStreamAttributes_Timestamp}

# ioT_metamodel_AtomicDataAttributes class attributes and methods
ioT_metamodel_AtomicDataAttributes_DataEncoding: Property = Property(name="DataEncoding", type=StringType)
ioT_metamodel_AtomicDataAttributes_DeviceID: Property = Property(name="DeviceID", type=StringType)
ioT_metamodel_AtomicDataAttributes.attributes={ioT_metamodel_AtomicDataAttributes_DeviceID, ioT_metamodel_AtomicDataAttributes_DataEncoding}

# ioT_metamodel_JavaEvaluator class attributes and methods

# Evaluators class attributes and methods

# ioT_metamodel_Entity class attributes and methods

# ioT_metamodel_ScriptEvaluator class attributes and methods

# ioT_metamodel_DeviceSensor class attributes and methods

# Relationships
virtual_entity0: BinaryAssociation = BinaryAssociation(
    name="virtual_entity0",
    ends={
        Property(name="ioT_metamodel_VirtualThing", type=ioT_metamodel_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_Thing", type=ioT_metamodel_VirtualThing, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fog1: BinaryAssociation = BinaryAssociation(
    name="fog1",
    ends={
        Property(name="Fog", type=ioT_metamodel_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="request_service", type=ioT_metamodel_Fog, multiplicity=Multiplicity(1, 1))
    }
)
physical_entity2: BinaryAssociation = BinaryAssociation(
    name="physical_entity2",
    ends={
        Property(name="ioT_metamodel_PhysicalThing", type=ioT_metamodel_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_Thing3", type=ioT_metamodel_PhysicalThing, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
contains5: BinaryAssociation = BinaryAssociation(
    name="contains5",
    ends={
        Property(name="ioT_metamodel_Thing6", type=ioT_metamodel_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_Thing4", type=ioT_metamodel_Thing, multiplicity=Multiplicity(0, 9999))
    }
)
is_associated_with12: BinaryAssociation = BinaryAssociation(
    name="is_associated_with12",
    ends={
        Property(name="ioT_metamodel_InformationResource", type=ioT_metamodel_VirtualThing, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_VirtualThing13", type=ioT_metamodel_InformationResource, multiplicity=Multiplicity(0, 9999))
    }
)
has14: BinaryAssociation = BinaryAssociation(
    name="has14",
    ends={
        Property(name="Device", type=ioT_metamodel_PhysicalThing, multiplicity=Multiplicity(1, 1)),
        Property(name="is_attached_to", type=ioT_metamodel_Device, multiplicity=Multiplicity(0, 9999))
    }
)
property7: BinaryAssociation = BinaryAssociation(
    name="property7",
    ends={
        Property(name="ioT_metamodel_Property", type=ioT_metamodel_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_Thing8", type=ioT_metamodel_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
represents9: BinaryAssociation = BinaryAssociation(
    name="represents9",
    ends={
        Property(name="ioT_metamodel_PhysicalThing11", type=ioT_metamodel_VirtualThing, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_VirtualThing10", type=ioT_metamodel_PhysicalThing, multiplicity=Multiplicity(1, 1))
    }
)
runs_on_vm21: BinaryAssociation = BinaryAssociation(
    name="runs_on_vm21",
    ends={
        Property(name="ioT_metamodel_VM", type=ioT_metamodel_FogNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_FogNode22", type=ioT_metamodel_VM, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
runs_in_container23: BinaryAssociation = BinaryAssociation(
    name="runs_in_container23",
    ends={
        Property(name="ioT_metamodel_Container", type=ioT_metamodel_FogNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_FogNode24", type=ioT_metamodel_Container, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
analytics_engine25: BinaryAssociation = BinaryAssociation(
    name="analytics_engine25",
    ends={
        Property(name="ioT_metamodel_Analytics_Engine", type=ioT_metamodel_FogNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_FogNode26", type=ioT_metamodel_Analytics_Engine, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
associates_with27: BinaryAssociation = BinaryAssociation(
    name="associates_with27",
    ends={
        Property(name="ioT_metamodel_Fog_Services", type=ioT_metamodel_FogNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_FogNode28", type=ioT_metamodel_Fog_Services, multiplicity=Multiplicity(1, 9999))
    }
)
is_attached_to29: BinaryAssociation = BinaryAssociation(
    name="is_attached_to29",
    ends={
        Property(name="PhysicalThing", type=ioT_metamodel_Device, multiplicity=Multiplicity(1, 1)),
        Property(name="has", type=ioT_metamodel_PhysicalThing, multiplicity=Multiplicity(0, 9999))
    }
)
request_service15: BinaryAssociation = BinaryAssociation(
    name="request_service15",
    ends={
        Property(name="Thing", type=ioT_metamodel_Fog, multiplicity=Multiplicity(1, 1)),
        Property(name="fog", type=ioT_metamodel_Thing, multiplicity=Multiplicity(1, 9999))
    }
)
fognode16: BinaryAssociation = BinaryAssociation(
    name="fognode16",
    ends={
        Property(name="ioT_metamodel_FogNode", type=ioT_metamodel_Fog, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_Fog", type=ioT_metamodel_FogNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
request_cloud_service17: BinaryAssociation = BinaryAssociation(
    name="request_cloud_service17",
    ends={
        Property(name="Cloud", type=ioT_metamodel_Fog, multiplicity=Multiplicity(1, 1)),
        Property(name="respond_to_fog", type=ioT_metamodel_Cloud, multiplicity=Multiplicity(1, 9999))
    }
)
database18: BinaryAssociation = BinaryAssociation(
    name="database18",
    ends={
        Property(name="ioT_metamodel_Database", type=ioT_metamodel_Fog, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_Fog19", type=ioT_metamodel_Database, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
define_control_policies_to20: BinaryAssociation = BinaryAssociation(
    name="define_control_policies_to20",
    ends={
        Property(name="Authorizor", type=ioT_metamodel_Fog, multiplicity=Multiplicity(1, 1)),
        Property(name="connects_with", type=ioT_metamodel_Authorizor, multiplicity=Multiplicity(1, 1))
    }
)
observes42: BinaryAssociation = BinaryAssociation(
    name="observes42",
    ends={
        Property(name="ioT_metamodel_DeviceState44", type=ioT_metamodel_Actuator, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_Actuator43", type=ioT_metamodel_DeviceState, multiplicity=Multiplicity(0, 1))
    }
)
identifies45: BinaryAssociation = BinaryAssociation(
    name="identifies45",
    ends={
        Property(name="ioT_metamodel_PhysicalThing46", type=ioT_metamodel_Tag, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_Tag", type=ioT_metamodel_PhysicalThing, multiplicity=Multiplicity(0, 9999))
    }
)
contains31: BinaryAssociation = BinaryAssociation(
    name="contains31",
    ends={
        Property(name="ioT_metamodel_Device", type=ioT_metamodel_Device, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_Device30", type=ioT_metamodel_Device, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
has_rules32: BinaryAssociation = BinaryAssociation(
    name="has_rules32",
    ends={
        Property(name="ioT_metamodel_Rule", type=ioT_metamodel_Device, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_Device33", type=ioT_metamodel_Rule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
devicestate34: BinaryAssociation = BinaryAssociation(
    name="devicestate34",
    ends={
        Property(name="ioT_metamodel_DeviceState", type=ioT_metamodel_Device, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_Device35", type=ioT_metamodel_DeviceState, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
has_communicators36: BinaryAssociation = BinaryAssociation(
    name="has_communicators36",
    ends={
        Property(name="ioT_metamodel_Communicator", type=ioT_metamodel_Device, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_Device37", type=ioT_metamodel_Communicator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hosts38: BinaryAssociation = BinaryAssociation(
    name="hosts38",
    ends={
        Property(name="ioT_metamodel_On_Device_Resource", type=ioT_metamodel_Device, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_Device39", type=ioT_metamodel_On_Device_Resource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
acts40: BinaryAssociation = BinaryAssociation(
    name="acts40",
    ends={
        Property(name="ioT_metamodel_PhysicalThing41", type=ioT_metamodel_Actuator, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_Actuator", type=ioT_metamodel_PhysicalThing, multiplicity=Multiplicity(0, 9999))
    }
)
action60: BinaryAssociation = BinaryAssociation(
    name="action60",
    ends={
        Property(name="ioT_metamodel_Action61", type=ioT_metamodel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_Transition", type=ioT_metamodel_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incoming_states62: BinaryAssociation = BinaryAssociation(
    name="incoming_states62",
    ends={
        Property(name="ioT_metamodel_DeviceState64", type=ioT_metamodel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_Transition63", type=ioT_metamodel_DeviceState, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing_states65: BinaryAssociation = BinaryAssociation(
    name="outgoing_states65",
    ends={
        Property(name="ioT_metamodel_DeviceState67", type=ioT_metamodel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_Transition66", type=ioT_metamodel_DeviceState, multiplicity=Multiplicity(0, 9999))
    }
)
monitors47: BinaryAssociation = BinaryAssociation(
    name="monitors47",
    ends={
        Property(name="ioT_metamodel_PhysicalThing48", type=ioT_metamodel_Sensor, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_Sensor", type=ioT_metamodel_PhysicalThing, multiplicity=Multiplicity(0, 9999))
    }
)
observes49: BinaryAssociation = BinaryAssociation(
    name="observes49",
    ends={
        Property(name="ioT_metamodel_DeviceState51", type=ioT_metamodel_Sensor, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_Sensor50", type=ioT_metamodel_DeviceState, multiplicity=Multiplicity(0, 1))
    }
)
involves52: BinaryAssociation = BinaryAssociation(
    name="involves52",
    ends={
        Property(name="ioT_metamodel_Action", type=ioT_metamodel_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_Rule53", type=ioT_metamodel_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sensor_actions54: BinaryAssociation = BinaryAssociation(
    name="sensor_actions54",
    ends={
        Property(name="ioT_metamodel_Action55", type=ioT_metamodel_ExternalSensor, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_ExternalSensor", type=ioT_metamodel_Action, multiplicity=Multiplicity(0, 9999))
    }
)
actuator_actions56: BinaryAssociation = BinaryAssociation(
    name="actuator_actions56",
    ends={
        Property(name="ioT_metamodel_Action57", type=ioT_metamodel_DeviceActuator, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_DeviceActuator", type=ioT_metamodel_Action, multiplicity=Multiplicity(0, 9999))
    }
)
actuator_actions58: BinaryAssociation = BinaryAssociation(
    name="actuator_actions58",
    ends={
        Property(name="ioT_metamodel_Action59", type=ioT_metamodel_ExternalActuator, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_ExternalActuator", type=ioT_metamodel_Action, multiplicity=Multiplicity(0, 9999))
    }
)
has_attributes77: BinaryAssociation = BinaryAssociation(
    name="has_attributes77",
    ends={
        Property(name="ioT_metamodel_InformationResource78", type=ioT_metamodel_Attribute, multiplicity=Multiplicity(0, 9999)),
        Property(name="ioT_metamodel_Attribute", type=ioT_metamodel_InformationResource, multiplicity=Multiplicity(1, 1))
    }
)
contains_device_resource79: BinaryAssociation = BinaryAssociation(
    name="contains_device_resource79",
    ends={
        Property(name="ioT_metamodel_Device_Resource", type=ioT_metamodel_On_Device_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_On_Device_Resource80", type=ioT_metamodel_Device_Resource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contains_service_resource81: BinaryAssociation = BinaryAssociation(
    name="contains_service_resource81",
    ends={
        Property(name="ioT_metamodel_Service_Resource", type=ioT_metamodel_On_Device_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_On_Device_Resource82", type=ioT_metamodel_Service_Resource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contains_device_resource83: BinaryAssociation = BinaryAssociation(
    name="contains_device_resource83",
    ends={
        Property(name="ioT_metamodel_Device_Resource84", type=ioT_metamodel_Network_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_Network_Resource", type=ioT_metamodel_Device_Resource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contains_service_resource85: BinaryAssociation = BinaryAssociation(
    name="contains_service_resource85",
    ends={
        Property(name="ioT_metamodel_Service_Resource87", type=ioT_metamodel_Network_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_Network_Resource86", type=ioT_metamodel_Service_Resource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subscribes_invokes68: BinaryAssociation = BinaryAssociation(
    name="subscribes_invokes68",
    ends={
        Property(name="ioT_metamodel_Fog_Services69", type=ioT_metamodel_User, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_User", type=ioT_metamodel_Fog_Services, multiplicity=Multiplicity(0, 9999))
    }
)
has_ports70: BinaryAssociation = BinaryAssociation(
    name="has_ports70",
    ends={
        Property(name="ioT_metamodel_Port", type=ioT_metamodel_Communicator, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_Communicator71", type=ioT_metamodel_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
has_information_about72: BinaryAssociation = BinaryAssociation(
    name="has_information_about72",
    ends={
        Property(name="ioT_metamodel_PhysicalThing74", type=ioT_metamodel_InformationResource, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_InformationResource73", type=ioT_metamodel_PhysicalThing, multiplicity=Multiplicity(0, 9999))
    }
)
has75: BinaryAssociation = BinaryAssociation(
    name="has75",
    ends={
        Property(name="ioT_metamodel_Information", type=ioT_metamodel_InformationResource, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_InformationResource76", type=ioT_metamodel_Information, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
orchestrate_policies95: BinaryAssociation = BinaryAssociation(
    name="orchestrate_policies95",
    ends={
        Property(name="Policy_Repository", type=ioT_metamodel_Reference_Monitor, multiplicity=Multiplicity(1, 1)),
        Property(name="interacts_with", type=ioT_metamodel_Policy_Repository, multiplicity=Multiplicity(1, 1))
    }
)
enforces96: BinaryAssociation = BinaryAssociation(
    name="enforces96",
    ends={
        Property(name="ioT_metamodel_Authorizor97", type=ioT_metamodel_Reference_Monitor, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_Reference_Monitor", type=ioT_metamodel_Authorizor, multiplicity=Multiplicity(0, 9999))
    }
)
connects_with98: BinaryAssociation = BinaryAssociation(
    name="connects_with98",
    ends={
        Property(name="Fog99", type=ioT_metamodel_Authorizor, multiplicity=Multiplicity(1, 1)),
        Property(name="define_control_policies_to", type=ioT_metamodel_Fog, multiplicity=Multiplicity(1, 1))
    }
)
atomicdata100: BinaryAssociation = BinaryAssociation(
    name="atomicdata100",
    ends={
        Property(name="ioT_metamodel_AtomicData", type=ioT_metamodel_Information, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_Information101", type=ioT_metamodel_AtomicData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
datastreams102: BinaryAssociation = BinaryAssociation(
    name="datastreams102",
    ends={
        Property(name="ioT_metamodel_DataStreams", type=ioT_metamodel_Information, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_Information103", type=ioT_metamodel_DataStreams, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
consists_of104: BinaryAssociation = BinaryAssociation(
    name="consists_of104",
    ends={
        Property(name="ioT_metamodel_AtomicData106", type=ioT_metamodel_DataStreams, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_DataStreams105", type=ioT_metamodel_AtomicData, multiplicity=Multiplicity(1, 9999))
    }
)
respond_to_fog88: BinaryAssociation = BinaryAssociation(
    name="respond_to_fog88",
    ends={
        Property(name="Fog89", type=ioT_metamodel_Cloud, multiplicity=Multiplicity(1, 1)),
        Property(name="request_cloud_service", type=ioT_metamodel_Fog, multiplicity=Multiplicity(1, 9999))
    }
)
policy_repository90: BinaryAssociation = BinaryAssociation(
    name="policy_repository90",
    ends={
        Property(name="ioT_metamodel_Policy_Repository", type=ioT_metamodel_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_Database91", type=ioT_metamodel_Policy_Repository, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
interacts_with92: BinaryAssociation = BinaryAssociation(
    name="interacts_with92",
    ends={
        Property(name="Reference_Monitor", type=ioT_metamodel_Policy_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="orchestrate_policies", type=ioT_metamodel_Reference_Monitor, multiplicity=Multiplicity(1, 1))
    }
)
contains93: BinaryAssociation = BinaryAssociation(
    name="contains93",
    ends={
        Property(name="ioT_metamodel_Authorizor", type=ioT_metamodel_Policy_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_Policy_Repository94", type=ioT_metamodel_Authorizor, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
invokes114: BinaryAssociation = BinaryAssociation(
    name="invokes114",
    ends={
        Property(name="ioT_metamodel_Operations", type=ioT_metamodel_Fog_Services, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_Fog_Services115", type=ioT_metamodel_Operations, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
invokes_fog_services117: BinaryAssociation = BinaryAssociation(
    name="invokes_fog_services117",
    ends={
        Property(name="ioT_metamodel_Fog_Services118", type=ioT_metamodel_Fog_Services, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_Fog_Services116", type=ioT_metamodel_Fog_Services, multiplicity=Multiplicity(0, 9999))
    }
)
exposes119: BinaryAssociation = BinaryAssociation(
    name="exposes119",
    ends={
        Property(name="ioT_metamodel_InformationResource121", type=ioT_metamodel_Fog_Services, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_Fog_Services120", type=ioT_metamodel_InformationResource, multiplicity=Multiplicity(1, 9999))
    }
)
is_connected_with122: BinaryAssociation = BinaryAssociation(
    name="is_connected_with122",
    ends={
        Property(name="ioT_metamodel_VirtualThing124", type=ioT_metamodel_Fog_Services, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_Fog_Services123", type=ioT_metamodel_VirtualThing, multiplicity=Multiplicity(1, 9999))
    }
)
points_to_processing_logic125: BinaryAssociation = BinaryAssociation(
    name="points_to_processing_logic125",
    ends={
        Property(name="ioT_metamodel_Evaluators", type=ioT_metamodel_Operations, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_Operations126", type=ioT_metamodel_Evaluators, multiplicity=Multiplicity(0, 1))
    }
)
runs_in127: BinaryAssociation = BinaryAssociation(
    name="runs_in127",
    ends={
        Property(name="ioT_metamodel_Container129", type=ioT_metamodel_Operations, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_Operations128", type=ioT_metamodel_Container, multiplicity=Multiplicity(0, 1))
    }
)
has_datastreamattributes107: BinaryAssociation = BinaryAssociation(
    name="has_datastreamattributes107",
    ends={
        Property(name="ioT_metamodel_DataStreamAttributes", type=ioT_metamodel_DataStreams, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_DataStreams108", type=ioT_metamodel_DataStreamAttributes, multiplicity=Multiplicity(1, 1))
    }
)
has_atomicdataattributes109: BinaryAssociation = BinaryAssociation(
    name="has_atomicdataattributes109",
    ends={
        Property(name="ioT_metamodel_AtomicDataAttributes", type=ioT_metamodel_AtomicData, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_AtomicData110", type=ioT_metamodel_AtomicDataAttributes, multiplicity=Multiplicity(1, 1))
    }
)
runs_in111: BinaryAssociation = BinaryAssociation(
    name="runs_in111",
    ends={
        Property(name="ioT_metamodel_Container113", type=ioT_metamodel_Fog_Services, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_Fog_Services112", type=ioT_metamodel_Container, multiplicity=Multiplicity(1, 1))
    }
)
subscribes_to130: BinaryAssociation = BinaryAssociation(
    name="subscribes_to130",
    ends={
        Property(name="ioT_metamodel_InformationResource132", type=ioT_metamodel_Operations, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_Operations131", type=ioT_metamodel_InformationResource, multiplicity=Multiplicity(1, 9999))
    }
)
sensor_actions133: BinaryAssociation = BinaryAssociation(
    name="sensor_actions133",
    ends={
        Property(name="ioT_metamodel_Action134", type=ioT_metamodel_DeviceSensor, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_metamodel_DeviceSensor", type=ioT_metamodel_Action, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_ioT_metamodel_Thing_Entity = Generalization(general=Entity, specific=ioT_metamodel_Thing)
gen_ioT_metamodel_VirtualThing_Active_Digital_Artifact = Generalization(general=Active_Digital_Artifact, specific=ioT_metamodel_VirtualThing)
gen_ioT_metamodel_VirtualThing_Passive_Digital_Artifact = Generalization(general=Passive_Digital_Artifact, specific=ioT_metamodel_VirtualThing)
gen_ioT_metamodel_Device_PhysicalThing = Generalization(general=PhysicalThing, specific=ioT_metamodel_Device)
gen_ioT_metamodel_Tag_Device = Generalization(general=Device, specific=ioT_metamodel_Tag)
gen_ioT_metamodel_Sensor_Device = Generalization(general=Device, specific=ioT_metamodel_Sensor)
gen_ioT_metamodel_Actuator_Device = Generalization(general=Device, specific=ioT_metamodel_Actuator)
gen_ioT_metamodel_CompositeState_DeviceState = Generalization(general=DeviceState, specific=ioT_metamodel_CompositeState)
gen_ioT_metamodel_Active_Digital_Artifact_Digital_Artifact = Generalization(general=Digital_Artifact, specific=ioT_metamodel_Active_Digital_Artifact)
gen_ioT_metamodel_Active_Digital_Artifact_User = Generalization(general=User, specific=ioT_metamodel_Active_Digital_Artifact)
gen_ioT_metamodel_ExternalSensor_Sensor = Generalization(general=Sensor, specific=ioT_metamodel_ExternalSensor)
gen_ioT_metamodel_DeviceActuator_Actuator = Generalization(general=Actuator, specific=ioT_metamodel_DeviceActuator)
gen_ioT_metamodel_ExternalActuator_Actuator = Generalization(general=Actuator, specific=ioT_metamodel_ExternalActuator)
gen_ioT_metamodel_On_Device_Resource_InformationResource = Generalization(general=InformationResource, specific=ioT_metamodel_On_Device_Resource)
gen_ioT_metamodel_Network_Resource_InformationResource = Generalization(general=InformationResource, specific=ioT_metamodel_Network_Resource)
gen_ioT_metamodel_Passive_Digital_Artifact_Digital_Artifact = Generalization(general=Digital_Artifact, specific=ioT_metamodel_Passive_Digital_Artifact)
gen_ioT_metamodel_User_Entity = Generalization(general=Entity, specific=ioT_metamodel_User)
gen_ioT_metamodel_Human_User_User = Generalization(general=User, specific=ioT_metamodel_Human_User)
gen_ioT_metamodel_JavaEvaluator_Evaluators = Generalization(general=Evaluators, specific=ioT_metamodel_JavaEvaluator)
gen_ioT_metamodel_ScriptEvaluator_Evaluators = Generalization(general=Evaluators, specific=ioT_metamodel_ScriptEvaluator)
gen_ioT_metamodel_Attribute_Entity = Generalization(general=Entity, specific=ioT_metamodel_Attribute)
gen_ioT_metamodel_DeviceSensor_Sensor = Generalization(general=Sensor, specific=ioT_metamodel_DeviceSensor)

# Domain Model
domain_model = DomainModel(
    name="ioT_metamodel",
    types={ioT_metamodel_VirtualThing, ioT_metamodel_Fog, ioT_metamodel_PhysicalThing, ioT_metamodel_Thing, Entity, ioT_metamodel_InformationResource, ioT_metamodel_Device, ioT_metamodel_Property, Active_Digital_Artifact, Passive_Digital_Artifact, ioT_metamodel_VM, ioT_metamodel_Container, ioT_metamodel_Analytics_Engine, ioT_metamodel_Fog_Services, PhysicalThing, ioT_metamodel_FogNode, ioT_metamodel_Cloud, ioT_metamodel_Database, ioT_metamodel_Authorizor, ioT_metamodel_Tag, ioT_metamodel_Sensor, ioT_metamodel_Rule, ioT_metamodel_DeviceState, ioT_metamodel_Communicator, ioT_metamodel_On_Device_Resource, ioT_metamodel_Actuator, Device, ioT_metamodel_CompositeState, DeviceState, ioT_metamodel_Transition, ioT_metamodel_Digital_Artifact, ioT_metamodel_Active_Digital_Artifact, Digital_Artifact, User, ioT_metamodel_Action, ioT_metamodel_ExternalSensor, Sensor, ioT_metamodel_DeviceActuator, Actuator, ioT_metamodel_ExternalActuator, InformationResource, ioT_metamodel_Device_Resource, ioT_metamodel_Service_Resource, ioT_metamodel_Network_Resource, ioT_metamodel_Passive_Digital_Artifact, ioT_metamodel_User, ioT_metamodel_Human_User, ioT_metamodel_Port, ioT_metamodel_Information, ioT_metamodel_Attribute, ioT_metamodel_AtomicData, ioT_metamodel_DataStreams, ioT_metamodel_Policy_Repository, ioT_metamodel_Reference_Monitor, ioT_metamodel_Operations, ioT_metamodel_Evaluators, ioT_metamodel_DataStreamAttributes, ioT_metamodel_AtomicDataAttributes, ioT_metamodel_JavaEvaluator, Evaluators, ioT_metamodel_Entity, ioT_metamodel_ScriptEvaluator, ioT_metamodel_DeviceSensor},
    associations={virtual_entity0, fog1, physical_entity2, contains5, is_associated_with12, has14, property7, represents9, runs_on_vm21, runs_in_container23, analytics_engine25, associates_with27, is_attached_to29, request_service15, fognode16, request_cloud_service17, database18, define_control_policies_to20, observes42, identifies45, contains31, has_rules32, devicestate34, has_communicators36, hosts38, acts40, action60, incoming_states62, outgoing_states65, monitors47, observes49, involves52, sensor_actions54, actuator_actions56, actuator_actions58, has_attributes77, contains_device_resource79, contains_service_resource81, contains_device_resource83, contains_service_resource85, subscribes_invokes68, has_ports70, has_information_about72, has75, orchestrate_policies95, enforces96, connects_with98, atomicdata100, datastreams102, consists_of104, respond_to_fog88, policy_repository90, interacts_with92, contains93, invokes114, invokes_fog_services117, exposes119, is_connected_with122, points_to_processing_logic125, runs_in127, has_datastreamattributes107, has_atomicdataattributes109, runs_in111, subscribes_to130, sensor_actions133},
    generalizations={gen_ioT_metamodel_Thing_Entity, gen_ioT_metamodel_VirtualThing_Active_Digital_Artifact, gen_ioT_metamodel_VirtualThing_Passive_Digital_Artifact, gen_ioT_metamodel_Device_PhysicalThing, gen_ioT_metamodel_Tag_Device, gen_ioT_metamodel_Sensor_Device, gen_ioT_metamodel_Actuator_Device, gen_ioT_metamodel_CompositeState_DeviceState, gen_ioT_metamodel_Active_Digital_Artifact_Digital_Artifact, gen_ioT_metamodel_Active_Digital_Artifact_User, gen_ioT_metamodel_ExternalSensor_Sensor, gen_ioT_metamodel_DeviceActuator_Actuator, gen_ioT_metamodel_ExternalActuator_Actuator, gen_ioT_metamodel_On_Device_Resource_InformationResource, gen_ioT_metamodel_Network_Resource_InformationResource, gen_ioT_metamodel_Passive_Digital_Artifact_Digital_Artifact, gen_ioT_metamodel_User_Entity, gen_ioT_metamodel_Human_User_User, gen_ioT_metamodel_JavaEvaluator_Evaluators, gen_ioT_metamodel_ScriptEvaluator_Evaluators, gen_ioT_metamodel_Attribute_Entity, gen_ioT_metamodel_DeviceSensor_Sensor},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)