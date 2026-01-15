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
ioT_System = Class(name="ioT::System")
ioT_EObject = Class(name="ioT::EObject")
ioT_SensorType = Class(name="ioT::SensorType")
ioT_SensorTypes = Class(name="ioT::SensorTypes")
ioT_SensorGroup = Class(name="ioT::SensorGroup")
ioT_SensorGetMethod = Class(name="ioT::SensorGetMethod")
ioT_Method = Class(name="ioT::Method")
ioT_DeviceType = Class(name="ioT::DeviceType")
ioT_DeviceTypes = Class(name="ioT::DeviceTypes")
ioT_Device = Class(name="ioT::Device")
ioT_ServerType = Class(name="ioT::ServerType")
ioT_ServerTypes = Class(name="ioT::ServerTypes")
ioT_Server = Class(name="ioT::Server")
ioT_Ip = Class(name="ioT::Ip")
ioT_Portnumber = Class(name="ioT::Portnumber")
ioT_DestinationType = Class(name="ioT::DestinationType")
ioT_DestinationTypes = Class(name="ioT::DestinationTypes")
ioT_Sensor = Class(name="ioT::Sensor")
ioT_FetchData = Class(name="ioT::FetchData")
ioT_FetchDataExpression = Class(name="ioT::FetchDataExpression")
ioT_Time = Class(name="ioT::Time")
ioT_FetchDataCondition = Class(name="ioT::FetchDataCondition")
ioT_Destination = Class(name="ioT::Destination")

# ioT_System class attributes and methods

# ioT_EObject class attributes and methods

# ioT_SensorType class attributes and methods
ioT_SensorType_name: Property = Property(name="name", type=StringType)
ioT_SensorType.attributes={ioT_SensorType_name}

# ioT_SensorTypes class attributes and methods

# ioT_SensorGroup class attributes and methods
ioT_SensorGroup_name: Property = Property(name="name", type=StringType)
ioT_SensorGroup.attributes={ioT_SensorGroup_name}

# ioT_SensorGetMethod class attributes and methods

# ioT_Method class attributes and methods
ioT_Method_name: Property = Property(name="name", type=StringType)
ioT_Method_parameters: Property = Property(name="parameters", type=StringType)
ioT_Method.attributes={ioT_Method_parameters, ioT_Method_name}

# ioT_DeviceType class attributes and methods
ioT_DeviceType_name: Property = Property(name="name", type=StringType)
ioT_DeviceType.attributes={ioT_DeviceType_name}

# ioT_DeviceTypes class attributes and methods

# ioT_Device class attributes and methods
ioT_Device_name: Property = Property(name="name", type=StringType)
ioT_Device.attributes={ioT_Device_name}

# ioT_ServerType class attributes and methods
ioT_ServerType_name: Property = Property(name="name", type=StringType)
ioT_ServerType.attributes={ioT_ServerType_name}

# ioT_ServerTypes class attributes and methods

# ioT_Server class attributes and methods
ioT_Server_name: Property = Property(name="name", type=StringType)
ioT_Server.attributes={ioT_Server_name}

# ioT_Ip class attributes and methods
ioT_Ip_ip: Property = Property(name="ip", type=IntegerType)
ioT_Ip.attributes={ioT_Ip_ip}

# ioT_Portnumber class attributes and methods
ioT_Portnumber_number: Property = Property(name="number", type=IntegerType)
ioT_Portnumber.attributes={ioT_Portnumber_number}

# ioT_DestinationType class attributes and methods
ioT_DestinationType_name: Property = Property(name="name", type=StringType)
ioT_DestinationType.attributes={ioT_DestinationType_name}

# ioT_DestinationTypes class attributes and methods

# ioT_Sensor class attributes and methods
ioT_Sensor_name: Property = Property(name="name", type=StringType)
ioT_Sensor.attributes={ioT_Sensor_name}

# ioT_FetchData class attributes and methods

# ioT_FetchDataExpression class attributes and methods
ioT_FetchDataExpression_timeUnit: Property = Property(name="timeUnit", type=StringType)
ioT_FetchDataExpression.attributes={ioT_FetchDataExpression_timeUnit}

# ioT_Time class attributes and methods
ioT_Time_time: Property = Property(name="time", type=IntegerType)
ioT_Time.attributes={ioT_Time_time}

# ioT_FetchDataCondition class attributes and methods
ioT_FetchDataCondition_condition: Property = Property(name="condition", type=StringType)
ioT_FetchDataCondition.attributes={ioT_FetchDataCondition_condition}

# ioT_Destination class attributes and methods
ioT_Destination_name: Property = Property(name="name", type=StringType)
ioT_Destination.attributes={ioT_Destination_name}

# Relationships
system0: BinaryAssociation = BinaryAssociation(
    name="system0",
    ends={
        Property(name="ioT_EObject", type=ioT_System, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_System", type=ioT_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type2: BinaryAssociation = BinaryAssociation(
    name="type2",
    ends={
        Property(name="ioT_Sensor", type=ioT_SensorType, multiplicity=Multiplicity(0, 1)),
        Property(name="ioT_SensorType3", type=ioT_Sensor, multiplicity=Multiplicity(1, 1))
    }
)
sensors4: BinaryAssociation = BinaryAssociation(
    name="sensors4",
    ends={
        Property(name="ioT_Sensor5", type=ioT_SensorGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_SensorGroup", type=ioT_Sensor, multiplicity=Multiplicity(0, 9999))
    }
)
method6: BinaryAssociation = BinaryAssociation(
    name="method6",
    ends={
        Property(name="ioT_Method", type=ioT_SensorGetMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_SensorGetMethod", type=ioT_Method, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type7: BinaryAssociation = BinaryAssociation(
    name="type7",
    ends={
        Property(name="ioT_SensorType9", type=ioT_SensorGetMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_SensorGetMethod8", type=ioT_SensorType, multiplicity=Multiplicity(0, 1))
    }
)
types10: BinaryAssociation = BinaryAssociation(
    name="types10",
    ends={
        Property(name="ioT_DeviceType", type=ioT_DeviceTypes, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_DeviceTypes", type=ioT_DeviceType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type11: BinaryAssociation = BinaryAssociation(
    name="type11",
    ends={
        Property(name="ioT_DeviceType12", type=ioT_Device, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_Device", type=ioT_DeviceType, multiplicity=Multiplicity(0, 1))
    }
)
devices13: BinaryAssociation = BinaryAssociation(
    name="devices13",
    ends={
        Property(name="ioT_EObject15", type=ioT_Device, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_Device14", type=ioT_EObject, multiplicity=Multiplicity(0, 1))
    }
)
types16: BinaryAssociation = BinaryAssociation(
    name="types16",
    ends={
        Property(name="ioT_ServerType", type=ioT_ServerTypes, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_ServerTypes", type=ioT_ServerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type17: BinaryAssociation = BinaryAssociation(
    name="type17",
    ends={
        Property(name="ioT_ServerType18", type=ioT_Server, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_Server", type=ioT_ServerType, multiplicity=Multiplicity(0, 1))
    }
)
ip19: BinaryAssociation = BinaryAssociation(
    name="ip19",
    ends={
        Property(name="ioT_Ip", type=ioT_Server, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_Server20", type=ioT_Ip, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
port21: BinaryAssociation = BinaryAssociation(
    name="port21",
    ends={
        Property(name="ioT_Portnumber", type=ioT_Server, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_Server22", type=ioT_Portnumber, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
types23: BinaryAssociation = BinaryAssociation(
    name="types23",
    ends={
        Property(name="ioT_DestinationType", type=ioT_DestinationTypes, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_DestinationTypes", type=ioT_DestinationType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types1: BinaryAssociation = BinaryAssociation(
    name="types1",
    ends={
        Property(name="ioT_SensorType", type=ioT_SensorTypes, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_SensorTypes", type=ioT_SensorType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type24: BinaryAssociation = BinaryAssociation(
    name="type24",
    ends={
        Property(name="ioT_DestinationType25", type=ioT_Destination, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_Destination", type=ioT_DestinationType, multiplicity=Multiplicity(0, 1))
    }
)
filter26: BinaryAssociation = BinaryAssociation(
    name="filter26",
    ends={
        Property(name="ioT_EObject27", type=ioT_FetchData, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_FetchData", type=ioT_EObject, multiplicity=Multiplicity(0, 1))
    }
)
destination28: BinaryAssociation = BinaryAssociation(
    name="destination28",
    ends={
        Property(name="ioT_EObject30", type=ioT_FetchData, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_FetchData29", type=ioT_EObject, multiplicity=Multiplicity(0, 1))
    }
)
conExp31: BinaryAssociation = BinaryAssociation(
    name="conExp31",
    ends={
        Property(name="ioT_EObject33", type=ioT_FetchData, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_FetchData32", type=ioT_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
duration34: BinaryAssociation = BinaryAssociation(
    name="duration34",
    ends={
        Property(name="ioT_Time", type=ioT_FetchDataExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_FetchDataExpression", type=ioT_Time, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="ioT",
    types={ioT_System, ioT_EObject, ioT_SensorType, ioT_SensorTypes, ioT_SensorGroup, ioT_SensorGetMethod, ioT_Method, ioT_DeviceType, ioT_DeviceTypes, ioT_Device, ioT_ServerType, ioT_ServerTypes, ioT_Server, ioT_Ip, ioT_Portnumber, ioT_DestinationType, ioT_DestinationTypes, ioT_Sensor, ioT_FetchData, ioT_FetchDataExpression, ioT_Time, ioT_FetchDataCondition, ioT_Destination},
    associations={system0, type2, sensors4, method6, type7, types10, type11, devices13, types16, type17, ip19, port21, types23, types1, type24, filter26, destination28, conExp31, duration34},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)