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

# Enumerations
DataType: Enumeration = Enumeration(
    name="DataType",
    literals={
            EnumerationLiteral(name="BYTE"),
			EnumerationLiteral(name="UNSIGNED_BYTE"),
			EnumerationLiteral(name="SHORT"),
			EnumerationLiteral(name="UNSIGNED_SHORT"),
			EnumerationLiteral(name="INTEGER"),
			EnumerationLiteral(name="FLOAT"),
			EnumerationLiteral(name="STRING"),
			EnumerationLiteral(name="IMAGE")
    }
)

AccessType: Enumeration = Enumeration(
    name="AccessType",
    literals={
            EnumerationLiteral(name="PUBLIC"),
			EnumerationLiteral(name="PRIVATE")
    }
)

LinearMode: Enumeration = Enumeration(
    name="LinearMode",
    literals={
            EnumerationLiteral(name="LINEAR"),
			EnumerationLiteral(name="SUSTAIN")
    }
)

AudioMode: Enumeration = Enumeration(
    name="AudioMode",
    literals={
            EnumerationLiteral(name="MONO"),
			EnumerationLiteral(name="STEREO")
    }
)

ColorMode: Enumeration = Enumeration(
    name="ColorMode",
    literals={
            EnumerationLiteral(name="RGB"),
			EnumerationLiteral(name="RED_GREEN"),
			EnumerationLiteral(name="RED"),
			EnumerationLiteral(name="GREEN"),
			EnumerationLiteral(name="BLUE"),
			EnumerationLiteral(name="GRAY")
    }
)

IoMode: Enumeration = Enumeration(
    name="IoMode",
    literals={
            EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="ANALOG_INPUT"),
			EnumerationLiteral(name="DIGITAL_INPUT"),
			EnumerationLiteral(name="SERVO_OUTPUT"),
			EnumerationLiteral(name="PWM_OUTPUT"),
			EnumerationLiteral(name="DIGITAL_OUTPUT")
    }
)

# Classes
robot_NamedElement = Class(name="robot::NamedElement", is_abstract=True)
robot_Simulacra = Class(name="robot::Simulacra", is_abstract=True)
robot_DeviceListener = Class(name="robot::DeviceListener", is_abstract=True)
robot_Robot = Class(name="robot::Robot")
NamedElement = Class(name="NamedElement")
Storable = Class(name="Storable")
Findable = Class(name="Findable")
robot_Roboid = Class(name="robot::Roboid")
robot_Control = Class(name="robot::Control")
robot_Storable = Class(name="robot::Storable", is_abstract=True)
robot_Findable = Class(name="robot::Findable", is_abstract=True)
robot_Protocol = Class(name="robot::Protocol")
robot_Device = Class(name="robot::Device", is_abstract=True)
robot_Channel = Class(name="robot::Channel", is_abstract=True)
Simulacra = Class(name="Simulacra")
robot_MotoringDevice = Class(name="robot::MotoringDevice", is_abstract=True)
ChannelDevice = Class(name="ChannelDevice")
robot_Sensor = Class(name="robot::Sensor")
SensoryDevice = Class(name="SensoryDevice")
robot_Effector = Class(name="robot::Effector")
MotoringDevice = Class(name="MotoringDevice")
robot_Command = Class(name="robot::Command")
robot_Event = Class(name="robot::Event")
robot_Port = Class(name="robot::Port")
robot_ChannelDevice = Class(name="robot::ChannelDevice", is_abstract=True)
Device = Class(name="Device")
robot_SensoryDevice = Class(name="robot::SensoryDevice", is_abstract=True)
robot_VoiceChannel = Class(name="robot::VoiceChannel")
robot_ColorChannel = Class(name="robot::ColorChannel")
robot_TextChannel = Class(name="robot::TextChannel")
robot_MatrixChannel = Class(name="robot::MatrixChannel")
LinearChannel = Class(name="LinearChannel")
robot_FileChannel = Class(name="robot::FileChannel")
robot_LinearChannel = Class(name="robot::LinearChannel")
Channel = Class(name="Channel")
robot_CommandChannel = Class(name="robot::CommandChannel")
robot_AudioChannel = Class(name="robot::AudioChannel")

# robot_NamedElement class attributes and methods
robot_NamedElement_name: Property = Property(name="name", type=StringType)
robot_NamedElement_literal: Property = Property(name="literal", type=StringType)
robot_NamedElement_comment: Property = Property(name="comment", type=StringType)
robot_NamedElement_m_getParent: Method = Method(name="getParent", parameters={}, type=StringType)
robot_NamedElement_m_getChildren: Method = Method(name="getChildren", parameters={}, type=StringType)
robot_NamedElement_m_equalsContents: Method = Method(name="equalsContents", parameters={Parameter(name='obj')}, type=BooleanType)
robot_NamedElement_m_getFullName: Method = Method(name="getFullName", parameters={}, type=StringType)
robot_NamedElement.attributes={robot_NamedElement_literal, robot_NamedElement_comment, robot_NamedElement_name}
robot_NamedElement.methods={robot_NamedElement_m_equalsContents, robot_NamedElement_m_getFullName, robot_NamedElement_m_getParent, robot_NamedElement_m_getChildren}

# robot_Simulacra class attributes and methods
robot_Simulacra_m_setDeviceMap: Method = Method(name="setDeviceMap", parameters={Parameter(name='index'), Parameter(name='deviceMap'), Parameter(name='isMaster')}, type=IntegerType)
robot_Simulacra_m_setPayload: Method = Method(name="setPayload", parameters={Parameter(name='simulacrum'), Parameter(name='isMaster')})
robot_Simulacra_m_getSimulacrum: Method = Method(name="getSimulacrum", parameters={Parameter(name='payload'), Parameter(name='deviceMap')})
robot_Simulacra_m_isReceived: Method = Method(name="isReceived", parameters={}, type=BooleanType)
robot_Simulacra_m_canSend: Method = Method(name="canSend", parameters={}, type=BooleanType)
robot_Simulacra_m_updateDeviceState: Method = Method(name="updateDeviceState", parameters={})
robot_Simulacra.methods={robot_Simulacra_m_isReceived, robot_Simulacra_m_setDeviceMap, robot_Simulacra_m_updateDeviceState, robot_Simulacra_m_setPayload, robot_Simulacra_m_canSend, robot_Simulacra_m_getSimulacrum}

# robot_DeviceListener class attributes and methods
robot_DeviceListener_m_effectPerformed: Method = Method(name="effectPerformed", parameters={Parameter(name='device')})
robot_DeviceListener_m_commandPerformed: Method = Method(name="commandPerformed", parameters={Parameter(name='device')})
robot_DeviceListener_m_stateChanged: Method = Method(name="stateChanged", parameters={Parameter(name='device')})
robot_DeviceListener_m_handleEvent: Method = Method(name="handleEvent", parameters={Parameter(name='device')})
robot_DeviceListener.methods={robot_DeviceListener_m_handleEvent, robot_DeviceListener_m_effectPerformed, robot_DeviceListener_m_commandPerformed, robot_DeviceListener_m_stateChanged}

# robot_Robot class attributes and methods
robot_Robot_provider: Property = Property(name="provider", type=StringType)
robot_Robot_version: Property = Property(name="version", type=StringType)
robot_Robot_standard: Property = Property(name="standard", type=StringType)
robot_Robot_m_getProtocol: Method = Method(name="getProtocol", parameters={}, type=StringType)
robot_Robot_m_collectAllDevices: Method = Method(name="collectAllDevices", parameters={Parameter(name='devices')}, type=StringType)
robot_Robot_m_collectAllDeviceNames: Method = Method(name="collectAllDeviceNames", parameters={Parameter(name='names')}, type=StringType)
robot_Robot_m_collectAllActiveDeviceNames: Method = Method(name="collectAllActiveDeviceNames", parameters={Parameter(name='names')}, type=StringType)
robot_Robot.attributes={robot_Robot_version, robot_Robot_provider, robot_Robot_standard}
robot_Robot.methods={robot_Robot_m_collectAllDevices, robot_Robot_m_getProtocol, robot_Robot_m_collectAllActiveDeviceNames, robot_Robot_m_collectAllDeviceNames}

# NamedElement class attributes and methods

# Storable class attributes and methods

# Findable class attributes and methods

# robot_Roboid class attributes and methods
robot_Roboid_id: Property = Property(name="id", type=StringType)
robot_Roboid_uid: Property = Property(name="uid", type=StringType)
robot_Roboid_version: Property = Property(name="version", type=StringType)
robot_Roboid_provider: Property = Property(name="provider", type=StringType)
robot_Roboid_address: Property = Property(name="address", type=StringType)
robot_Roboid_m_collectAllDevices: Method = Method(name="collectAllDevices", parameters={Parameter(name='devices')}, type=StringType)
robot_Roboid.attributes={robot_Roboid_version, robot_Roboid_provider, robot_Roboid_address, robot_Roboid_uid, robot_Roboid_id}
robot_Roboid.methods={robot_Roboid_m_collectAllDevices}

# robot_Control class attributes and methods
robot_Control_version: Property = Property(name="version", type=StringType)
robot_Control_frameLimit: Property = Property(name="frameLimit", type=IntegerType)
robot_Control.attributes={robot_Control_frameLimit, robot_Control_version}

# robot_Storable class attributes and methods
robot_Storable_m_createDeviceMemory: Method = Method(name="createDeviceMemory", parameters={})
robot_Storable_m_clearDeviceMemory: Method = Method(name="clearDeviceMemory", parameters={})
robot_Storable.methods={robot_Storable_m_createDeviceMemory, robot_Storable_m_clearDeviceMemory}

# robot_Findable class attributes and methods
robot_Findable_m_findRoboid: Method = Method(name="findRoboid", parameters={Parameter(name='name')}, type=StringType)
robot_Findable_m_findDevice: Method = Method(name="findDevice", parameters={Parameter(name='name')}, type=StringType)
robot_Findable.methods={robot_Findable_m_findDevice, robot_Findable_m_findRoboid}

# robot_Protocol class attributes and methods
robot_Protocol_version: Property = Property(name="version", type=StringType)
robot_Protocol_bufferSize: Property = Property(name="bufferSize", type=IntegerType)
robot_Protocol_remainingBuffer: Property = Property(name="remainingBuffer", type=IntegerType)
robot_Protocol_m_getSimulacrum: Method = Method(name="getSimulacrum", parameters={}, type=StringType)
robot_Protocol_m_setSimulacrum: Method = Method(name="setSimulacrum", parameters={Parameter(name='simulacrum'), Parameter(name='isMaster')})
robot_Protocol_m_clearBuffer: Method = Method(name="clearBuffer", parameters={})
robot_Protocol_m_setEvents: Method = Method(name="setEvents", parameters={})
robot_Protocol_m_getBufferId: Method = Method(name="getBufferId", parameters={}, type=IntegerType)
robot_Protocol.attributes={robot_Protocol_bufferSize, robot_Protocol_remainingBuffer, robot_Protocol_version}
robot_Protocol.methods={robot_Protocol_m_getSimulacrum, robot_Protocol_m_getBufferId, robot_Protocol_m_clearBuffer, robot_Protocol_m_setEvents, robot_Protocol_m_setSimulacrum}

# robot_Device class attributes and methods
robot_Device_dataSize: Property = Property(name="dataSize", type=IntegerType)
robot_Device_dataType: Property = Property(name="dataType", type=StringType)
robot_Device_max: Property = Property(name="max", type=StringType)
robot_Device_min: Property = Property(name="min", type=StringType)
robot_Device_default: Property = Property(name="default", type=StringType)
robot_Device_proxy: Property = Property(name="proxy", type=BooleanType)
robot_Device_access: Property = Property(name="access", type=StringType)
robot_Device_m_write: Method = Method(name="write", parameters={}, type=BooleanType)
robot_Device_m_write: Method = Method(name="write", parameters={Parameter(name='data')}, type=BooleanType)
robot_Device_m_write: Method = Method(name="write", parameters={Parameter(name='data'), Parameter(name='index')}, type=BooleanType)
robot_Device_m_write: Method = Method(name="write", parameters={Parameter(name='data')}, type=BooleanType)
robot_Device_m_write: Method = Method(name="write", parameters={Parameter(name='data')}, type=BooleanType)
robot_Device_m_write: Method = Method(name="write", parameters={Parameter(name='text')}, type=BooleanType)
robot_Device_m_write: Method = Method(name="write", parameters={Parameter(name='index'), Parameter(name='text')}, type=BooleanType)
robot_Device_m_write: Method = Method(name="write", parameters={Parameter(name='text')}, type=BooleanType)
robot_Device_m_write: Method = Method(name="write", parameters={Parameter(name='imageData')}, type=BooleanType)
robot_Device_m_write: Method = Method(name="write", parameters={Parameter(name='index'), Parameter(name='imageData')}, type=BooleanType)
robot_Device_m_write: Method = Method(name="write", parameters={Parameter(name='imageData')}, type=BooleanType)
robot_Device_m_writeInt: Method = Method(name="writeInt", parameters={Parameter(name='data')}, type=BooleanType)
robot_Device_m_writeInt: Method = Method(name="writeInt", parameters={Parameter(name='index'), Parameter(name='data')}, type=BooleanType)
robot_Device_m_writeInt: Method = Method(name="writeInt", parameters={Parameter(name='data')}, type=BooleanType)
robot_Device_m_writeFloat: Method = Method(name="writeFloat", parameters={Parameter(name='data')}, type=BooleanType)
robot_Device_m_writeFloat: Method = Method(name="writeFloat", parameters={Parameter(name='index'), Parameter(name='data')}, type=BooleanType)
robot_Device_m_writeFloat: Method = Method(name="writeFloat", parameters={Parameter(name='data')}, type=BooleanType)
robot_Device_m_writeString: Method = Method(name="writeString", parameters={Parameter(name='text')}, type=BooleanType)
robot_Device_m_writeString: Method = Method(name="writeString", parameters={Parameter(name='text'), Parameter(name='index')}, type=BooleanType)
robot_Device_m_writeString: Method = Method(name="writeString", parameters={Parameter(name='text')}, type=BooleanType)
robot_Device_m_writeImageData: Method = Method(name="writeImageData", parameters={Parameter(name='imageData')}, type=BooleanType)
robot_Device_m_writeImageData: Method = Method(name="writeImageData", parameters={Parameter(name='imageData'), Parameter(name='index')}, type=BooleanType)
robot_Device_m_writeImageData: Method = Method(name="writeImageData", parameters={Parameter(name='imageData')}, type=BooleanType)
robot_Device_m_read: Method = Method(name="read", parameters={}, type=IntegerType)
robot_Device_m_read: Method = Method(name="read", parameters={Parameter(name='index')}, type=IntegerType)
robot_Device_m_read: Method = Method(name="read", parameters={Parameter(name='data')}, type=IntegerType)
robot_Device_m_read: Method = Method(name="read", parameters={Parameter(name='data')}, type=IntegerType)
robot_Device_m_read: Method = Method(name="read", parameters={Parameter(name='data')}, type=IntegerType)
robot_Device_m_write: Method = Method(name="write", parameters={Parameter(name='data')}, type=BooleanType)
robot_Device_m_write: Method = Method(name="write", parameters={Parameter(name='data'), Parameter(name='index')}, type=BooleanType)
robot_Device_m_readInt: Method = Method(name="readInt", parameters={Parameter(name='data')}, type=IntegerType)
robot_Device_m_readFloat: Method = Method(name="readFloat", parameters={}, type=FloatType)
robot_Device_m_readFloat: Method = Method(name="readFloat", parameters={Parameter(name='index')}, type=FloatType)
robot_Device_m_readFloat: Method = Method(name="readFloat", parameters={Parameter(name='data')}, type=IntegerType)
robot_Device_m_readString: Method = Method(name="readString", parameters={}, type=StringType)
robot_Device_m_readString: Method = Method(name="readString", parameters={Parameter(name='index')}, type=StringType)
robot_Device_m_readString: Method = Method(name="readString", parameters={Parameter(name='text')}, type=IntegerType)
robot_Device_m_readImageData: Method = Method(name="readImageData", parameters={}, type=StringType)
robot_Device_m_readImageData: Method = Method(name="readImageData", parameters={Parameter(name='index')}, type=StringType)
robot_Device_m_readImageData: Method = Method(name="readImageData", parameters={Parameter(name='imageData')}, type=IntegerType)
robot_Device_m_e: Method = Method(name="e", parameters={}, type=BooleanType)
robot_Device_m_setEvent: Method = Method(name="setEvent", parameters={})
robot_Device_m_setFired: Method = Method(name="setFired", parameters={})
robot_Device_m_addDeviceListener: Method = Method(name="addDeviceListener", parameters={Parameter(name='listener')})
robot_Device_m_removeDeviceListener: Method = Method(name="removeDeviceListener", parameters={Parameter(name='listener')})
robot_Device_m_getDeviceListeners: Method = Method(name="getDeviceListeners", parameters={}, type=StringType)
robot_Device_m_getMin: Method = Method(name="getMin", parameters={}, type=IntegerType)
robot_Device_m_getMinFloat: Method = Method(name="getMinFloat", parameters={}, type=FloatType)
robot_Device_m_getMinString: Method = Method(name="getMinString", parameters={}, type=StringType)
robot_Device_m_getMax: Method = Method(name="getMax", parameters={}, type=IntegerType)
robot_Device_m_getMaxFloat: Method = Method(name="getMaxFloat", parameters={}, type=FloatType)
robot_Device_m_getMaxString: Method = Method(name="getMaxString", parameters={}, type=StringType)
robot_Device_m_getDefault: Method = Method(name="getDefault", parameters={}, type=IntegerType)
robot_Device_m_getDefaultFloat: Method = Method(name="getDefaultFloat", parameters={}, type=FloatType)
robot_Device_m_getDefaultString: Method = Method(name="getDefaultString", parameters={}, type=StringType)
robot_Device_m_getDefaultImageData: Method = Method(name="getDefaultImageData", parameters={}, type=StringType)
robot_Device_m_getRootRoboid: Method = Method(name="getRootRoboid", parameters={}, type=StringType)
robot_Device_m_isDataTypeOf: Method = Method(name="isDataTypeOf", parameters={Parameter(name='device')}, type=BooleanType)
robot_Device_m_read: Method = Method(name="read", parameters={Parameter(name='data')}, type=IntegerType)
robot_Device_m_readInt: Method = Method(name="readInt", parameters={}, type=FloatType)
robot_Device_m_readInt: Method = Method(name="readInt", parameters={Parameter(name='index')}, type=FloatType)
robot_Device.attributes={robot_Device_min, robot_Device_proxy, robot_Device_access, robot_Device_default, robot_Device_dataSize, robot_Device_dataType, robot_Device_max}
robot_Device.methods={robot_Device_m_write, robot_Device_m_e, robot_Device_m_writeImageData, robot_Device_m_write, robot_Device_m_write, robot_Device_m_readString, robot_Device_m_read, robot_Device_m_getMax, robot_Device_m_read, robot_Device_m_read, robot_Device_m_getMaxString, robot_Device_m_write, robot_Device_m_writeInt, robot_Device_m_readString, robot_Device_m_getMin, robot_Device_m_getMaxFloat, robot_Device_m_writeString, robot_Device_m_read, robot_Device_m_readInt, robot_Device_m_isDataTypeOf, robot_Device_m_write, robot_Device_m_writeInt, robot_Device_m_writeFloat, robot_Device_m_getMinString, robot_Device_m_readInt, robot_Device_m_readFloat, robot_Device_m_setFired, robot_Device_m_setEvent, robot_Device_m_write, robot_Device_m_readFloat, robot_Device_m_writeImageData, robot_Device_m_writeImageData, robot_Device_m_read, robot_Device_m_write, robot_Device_m_getDefaultFloat, robot_Device_m_removeDeviceListener, robot_Device_m_addDeviceListener, robot_Device_m_getDefaultString, robot_Device_m_writeFloat, robot_Device_m_getMinFloat, robot_Device_m_write, robot_Device_m_writeString, robot_Device_m_readString, robot_Device_m_getRootRoboid, robot_Device_m_write, robot_Device_m_write, robot_Device_m_read, robot_Device_m_readInt, robot_Device_m_write, robot_Device_m_readImageData, robot_Device_m_getDeviceListeners, robot_Device_m_readImageData, robot_Device_m_readFloat, robot_Device_m_write, robot_Device_m_readImageData, robot_Device_m_getDefault, robot_Device_m_getDefaultImageData, robot_Device_m_write, robot_Device_m_writeFloat, robot_Device_m_writeString, robot_Device_m_writeInt}

# robot_Channel class attributes and methods
robot_Channel_m_isEnabled: Method = Method(name="isEnabled", parameters={}, type=BooleanType)
robot_Channel.methods={robot_Channel_m_isEnabled}

# Simulacra class attributes and methods

# robot_MotoringDevice class attributes and methods

# ChannelDevice class attributes and methods

# robot_Sensor class attributes and methods
robot_Sensor_throttle: Property = Property(name="throttle", type=IntegerType)
robot_Sensor.attributes={robot_Sensor_throttle}

# SensoryDevice class attributes and methods

# robot_Effector class attributes and methods
robot_Effector_sustain: Property = Property(name="sustain", type=IntegerType)
robot_Effector_throttle: Property = Property(name="throttle", type=IntegerType)
robot_Effector_m_hasNext: Method = Method(name="hasNext", parameters={}, type=BooleanType)
robot_Effector.attributes={robot_Effector_throttle, robot_Effector_sustain}
robot_Effector.methods={robot_Effector_m_hasNext}

# MotoringDevice class attributes and methods

# robot_Command class attributes and methods
robot_Command_id: Property = Property(name="id", type=IntegerType)
robot_Command.attributes={robot_Command_id}

# robot_Event class attributes and methods
robot_Event_id: Property = Property(name="id", type=IntegerType)
robot_Event.attributes={robot_Event_id}

# robot_Port class attributes and methods
robot_Port_mode: Property = Property(name="mode", type=StringType)
robot_Port.attributes={robot_Port_mode}

# robot_ChannelDevice class attributes and methods

# Device class attributes and methods

# robot_SensoryDevice class attributes and methods
robot_SensoryDevice_m_addReceptor: Method = Method(name="addReceptor", parameters={Parameter(name='receptor')})
robot_SensoryDevice_m_removeReceptor: Method = Method(name="removeReceptor", parameters={Parameter(name='receptor')})
robot_SensoryDevice.methods={robot_SensoryDevice_m_removeReceptor, robot_SensoryDevice_m_addReceptor}

# robot_VoiceChannel class attributes and methods

# robot_ColorChannel class attributes and methods
robot_ColorChannel_mode: Property = Property(name="mode", type=StringType)
robot_ColorChannel.attributes={robot_ColorChannel_mode}

# robot_TextChannel class attributes and methods

# robot_MatrixChannel class attributes and methods

# LinearChannel class attributes and methods

# robot_FileChannel class attributes and methods

# robot_LinearChannel class attributes and methods
robot_LinearChannel_mode: Property = Property(name="mode", type=StringType)
robot_LinearChannel.attributes={robot_LinearChannel_mode}

# Channel class attributes and methods

# robot_CommandChannel class attributes and methods

# robot_AudioChannel class attributes and methods

# Relationships
roboids0: BinaryAssociation = BinaryAssociation(
    name="roboids0",
    ends={
        Property(name="robot_Roboid", type=robot_Robot, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_Robot", type=robot_Roboid, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
controls1: BinaryAssociation = BinaryAssociation(
    name="controls1",
    ends={
        Property(name="robot_Control", type=robot_Robot, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_Robot2", type=robot_Control, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
roboids4: BinaryAssociation = BinaryAssociation(
    name="roboids4",
    ends={
        Property(name="robot_Roboid5", type=robot_Roboid, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_Roboid3", type=robot_Roboid, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
protocol6: BinaryAssociation = BinaryAssociation(
    name="protocol6",
    ends={
        Property(name="robot_Protocol", type=robot_Roboid, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_Roboid7", type=robot_Protocol, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
devices8: BinaryAssociation = BinaryAssociation(
    name="devices8",
    ends={
        Property(name="robot_Device", type=robot_Roboid, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_Roboid9", type=robot_Device, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hostRoboid11: BinaryAssociation = BinaryAssociation(
    name="hostRoboid11",
    ends={
        Property(name="robot_Roboid12", type=robot_Roboid, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_Roboid10", type=robot_Roboid, multiplicity=Multiplicity(0, 1))
    }
)
channels13: BinaryAssociation = BinaryAssociation(
    name="channels13",
    ends={
        Property(name="robot_Channel", type=robot_Control, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_Control14", type=robot_Channel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
proxyFor16: BinaryAssociation = BinaryAssociation(
    name="proxyFor16",
    ends={
        Property(name="robot_Sensor", type=robot_Sensor, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_Sensor15", type=robot_Sensor, multiplicity=Multiplicity(0, 1))
    }
)
receptors17: BinaryAssociation = BinaryAssociation(
    name="receptors17",
    ends={
        Property(name="robot_Effector", type=robot_Sensor, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_Sensor18", type=robot_Effector, multiplicity=Multiplicity(0, 9999))
    }
)
proxyFor20: BinaryAssociation = BinaryAssociation(
    name="proxyFor20",
    ends={
        Property(name="robot_Effector21", type=robot_Effector, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_Effector19", type=robot_Effector, multiplicity=Multiplicity(0, 1))
    }
)
proxyFor23: BinaryAssociation = BinaryAssociation(
    name="proxyFor23",
    ends={
        Property(name="robot_Command", type=robot_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_Command22", type=robot_Command, multiplicity=Multiplicity(0, 1))
    }
)
proxyFor25: BinaryAssociation = BinaryAssociation(
    name="proxyFor25",
    ends={
        Property(name="robot_Event", type=robot_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_Event24", type=robot_Event, multiplicity=Multiplicity(0, 1))
    }
)
receptors26: BinaryAssociation = BinaryAssociation(
    name="receptors26",
    ends={
        Property(name="robot_Command28", type=robot_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_Event27", type=robot_Command, multiplicity=Multiplicity(0, 9999))
    }
)
proxyFor30: BinaryAssociation = BinaryAssociation(
    name="proxyFor30",
    ends={
        Property(name="robot_Port", type=robot_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_Port29", type=robot_Port, multiplicity=Multiplicity(0, 1))
    }
)
devices31: BinaryAssociation = BinaryAssociation(
    name="devices31",
    ends={
        Property(name="robot_ChannelDevice", type=robot_Channel, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_Channel32", type=robot_ChannelDevice, multiplicity=Multiplicity(1, 9999))
    }
)

# Generalizations
gen_robot_Robot_NamedElement = Generalization(general=NamedElement, specific=robot_Robot)
gen_robot_Robot_Storable = Generalization(general=Storable, specific=robot_Robot)
gen_robot_Robot_Findable = Generalization(general=Findable, specific=robot_Robot)
gen_robot_Control_NamedElement = Generalization(general=NamedElement, specific=robot_Control)
gen_robot_Protocol_NamedElement = Generalization(general=NamedElement, specific=robot_Protocol)
gen_robot_Device_NamedElement = Generalization(general=NamedElement, specific=robot_Device)
gen_robot_Device_Storable = Generalization(general=Storable, specific=robot_Device)
gen_robot_Device_Simulacra = Generalization(general=Simulacra, specific=robot_Device)
gen_robot_Roboid_NamedElement = Generalization(general=NamedElement, specific=robot_Roboid)
gen_robot_Roboid_Storable = Generalization(general=Storable, specific=robot_Roboid)
gen_robot_Roboid_Simulacra = Generalization(general=Simulacra, specific=robot_Roboid)
gen_robot_Roboid_Findable = Generalization(general=Findable, specific=robot_Roboid)
gen_robot_MotoringDevice_ChannelDevice = Generalization(general=ChannelDevice, specific=robot_MotoringDevice)
gen_robot_Sensor_SensoryDevice = Generalization(general=SensoryDevice, specific=robot_Sensor)
gen_robot_Effector_MotoringDevice = Generalization(general=MotoringDevice, specific=robot_Effector)
gen_robot_Command_MotoringDevice = Generalization(general=MotoringDevice, specific=robot_Command)
gen_robot_Event_SensoryDevice = Generalization(general=SensoryDevice, specific=robot_Event)
gen_robot_Port_ChannelDevice = Generalization(general=ChannelDevice, specific=robot_Port)
gen_robot_Channel_NamedElement = Generalization(general=NamedElement, specific=robot_Channel)
gen_robot_ChannelDevice_Device = Generalization(general=Device, specific=robot_ChannelDevice)
gen_robot_SensoryDevice_Device = Generalization(general=Device, specific=robot_SensoryDevice)
gen_robot_VoiceChannel_Channel = Generalization(general=Channel, specific=robot_VoiceChannel)
gen_robot_ColorChannel_Channel = Generalization(general=Channel, specific=robot_ColorChannel)
gen_robot_TextChannel_Channel = Generalization(general=Channel, specific=robot_TextChannel)
gen_robot_MatrixChannel_LinearChannel = Generalization(general=LinearChannel, specific=robot_MatrixChannel)
gen_robot_FileChannel_Channel = Generalization(general=Channel, specific=robot_FileChannel)
gen_robot_LinearChannel_Channel = Generalization(general=Channel, specific=robot_LinearChannel)
gen_robot_CommandChannel_Channel = Generalization(general=Channel, specific=robot_CommandChannel)
gen_robot_AudioChannel_Channel = Generalization(general=Channel, specific=robot_AudioChannel)

# Domain Model
domain_model = DomainModel(
    name="robot",
    types={robot_NamedElement, robot_Simulacra, robot_DeviceListener, robot_Robot, NamedElement, Storable, Findable, robot_Roboid, robot_Control, robot_Storable, robot_Findable, robot_Protocol, robot_Device, robot_Channel, Simulacra, robot_MotoringDevice, ChannelDevice, robot_Sensor, SensoryDevice, robot_Effector, MotoringDevice, robot_Command, robot_Event, robot_Port, robot_ChannelDevice, Device, robot_SensoryDevice, robot_VoiceChannel, robot_ColorChannel, robot_TextChannel, robot_MatrixChannel, LinearChannel, robot_FileChannel, robot_LinearChannel, Channel, robot_CommandChannel, robot_AudioChannel, DataType, AccessType, LinearMode, AudioMode, ColorMode, IoMode},
    associations={roboids0, controls1, roboids4, protocol6, devices8, hostRoboid11, channels13, proxyFor16, receptors17, proxyFor20, proxyFor23, proxyFor25, receptors26, proxyFor30, devices31},
    generalizations={gen_robot_Robot_NamedElement, gen_robot_Robot_Storable, gen_robot_Robot_Findable, gen_robot_Control_NamedElement, gen_robot_Protocol_NamedElement, gen_robot_Device_NamedElement, gen_robot_Device_Storable, gen_robot_Device_Simulacra, gen_robot_Roboid_NamedElement, gen_robot_Roboid_Storable, gen_robot_Roboid_Simulacra, gen_robot_Roboid_Findable, gen_robot_MotoringDevice_ChannelDevice, gen_robot_Sensor_SensoryDevice, gen_robot_Effector_MotoringDevice, gen_robot_Command_MotoringDevice, gen_robot_Event_SensoryDevice, gen_robot_Port_ChannelDevice, gen_robot_Channel_NamedElement, gen_robot_ChannelDevice_Device, gen_robot_SensoryDevice_Device, gen_robot_VoiceChannel_Channel, gen_robot_ColorChannel_Channel, gen_robot_TextChannel_Channel, gen_robot_MatrixChannel_LinearChannel, gen_robot_FileChannel_Channel, gen_robot_LinearChannel_Channel, gen_robot_CommandChannel_Channel, gen_robot_AudioChannel_Channel},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)