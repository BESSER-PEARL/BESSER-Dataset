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
ioT_SensorGetMethod = Class(name="ioT::SensorGetMethod")
ioT_Method = Class(name="ioT::Method")
ioT_System = Class(name="ioT::System")
ioT_EObject = Class(name="ioT::EObject")
ioT_SensorType = Class(name="ioT::SensorType")
ioT_SensorTypes = Class(name="ioT::SensorTypes")
ioT_Sensor = Class(name="ioT::Sensor")
ioT_SensorGroup = Class(name="ioT::SensorGroup")
ioT_Portnumber = Class(name="ioT::Portnumber")
ioT_DestinationType = Class(name="ioT::DestinationType")
ioT_DestinationTypes = Class(name="ioT::DestinationTypes")
Condition = Class(name="Condition")
ioT_DeviceType = Class(name="ioT::DeviceType")
ioT_DeviceTypes = Class(name="ioT::DeviceTypes")
ioT_Device = Class(name="ioT::Device")
ioT_ServerType = Class(name="ioT::ServerType")
ioT_ServerTypes = Class(name="ioT::ServerTypes")
ioT_Server = Class(name="ioT::Server")
ioT_Ip = Class(name="ioT::Ip")
ioT_AndCondition = Class(name="ioT::AndCondition")
ioT_Destination = Class(name="ioT::Destination")
ioT_FetchData = Class(name="ioT::FetchData")
ioT_FetchDataCondition = Class(name="ioT::FetchDataCondition")
ioT_FetchDataExpression = Class(name="ioT::FetchDataExpression")
ioT_Time = Class(name="ioT::Time")
ioT_Condition = Class(name="ioT::Condition")
ioT_OrCondition = Class(name="ioT::OrCondition")
ioT_ComparisonCondition = Class(name="ioT::ComparisonCondition")
ioT_LiteralBool = Class(name="ioT::LiteralBool")
ioT_LiteralNumber = Class(name="ioT::LiteralNumber")

# ioT_SensorGetMethod class attributes and methods

# ioT_Method class attributes and methods
ioT_Method_name: Property = Property(name="name", type=StringType)
ioT_Method_parameters: Property = Property(name="parameters", type=StringType)
ioT_Method.attributes={ioT_Method_parameters, ioT_Method_name}

# ioT_System class attributes and methods

# ioT_EObject class attributes and methods

# ioT_SensorType class attributes and methods
ioT_SensorType_name: Property = Property(name="name", type=StringType)
ioT_SensorType.attributes={ioT_SensorType_name}

# ioT_SensorTypes class attributes and methods

# ioT_Sensor class attributes and methods
ioT_Sensor_name: Property = Property(name="name", type=StringType)
ioT_Sensor.attributes={ioT_Sensor_name}

# ioT_SensorGroup class attributes and methods
ioT_SensorGroup_name: Property = Property(name="name", type=StringType)
ioT_SensorGroup.attributes={ioT_SensorGroup_name}

# ioT_Portnumber class attributes and methods
ioT_Portnumber_number: Property = Property(name="number", type=IntegerType)
ioT_Portnumber.attributes={ioT_Portnumber_number}

# ioT_DestinationType class attributes and methods
ioT_DestinationType_name: Property = Property(name="name", type=StringType)
ioT_DestinationType.attributes={ioT_DestinationType_name}

# ioT_DestinationTypes class attributes and methods

# Condition class attributes and methods

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

# ioT_AndCondition class attributes and methods

# ioT_Destination class attributes and methods
ioT_Destination_name: Property = Property(name="name", type=StringType)
ioT_Destination.attributes={ioT_Destination_name}

# ioT_FetchData class attributes and methods

# ioT_FetchDataCondition class attributes and methods

# ioT_FetchDataExpression class attributes and methods
ioT_FetchDataExpression_timeUnit: Property = Property(name="timeUnit", type=StringType)
ioT_FetchDataExpression.attributes={ioT_FetchDataExpression_timeUnit}

# ioT_Time class attributes and methods
ioT_Time_time: Property = Property(name="time", type=IntegerType)
ioT_Time.attributes={ioT_Time_time}

# ioT_Condition class attributes and methods

# ioT_OrCondition class attributes and methods

# ioT_ComparisonCondition class attributes and methods
ioT_ComparisonCondition_operator: Property = Property(name="operator", type=StringType)
ioT_ComparisonCondition.attributes={ioT_ComparisonCondition_operator}

# ioT_LiteralBool class attributes and methods
ioT_LiteralBool_value: Property = Property(name="value", type=StringType)
ioT_LiteralBool.attributes={ioT_LiteralBool_value}

# ioT_LiteralNumber class attributes and methods
ioT_LiteralNumber_value: Property = Property(name="value", type=IntegerType)
ioT_LiteralNumber.attributes={ioT_LiteralNumber_value}

# Relationships
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
system0: BinaryAssociation = BinaryAssociation(
    name="system0",
    ends={
        Property(name="ioT_EObject", type=ioT_System, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_System", type=ioT_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types1: BinaryAssociation = BinaryAssociation(
    name="types1",
    ends={
        Property(name="ioT_SensorType", type=ioT_SensorTypes, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_SensorTypes", type=ioT_SensorType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type2: BinaryAssociation = BinaryAssociation(
    name="type2",
    ends={
        Property(name="ioT_SensorType3", type=ioT_Sensor, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_Sensor", type=ioT_SensorType, multiplicity=Multiplicity(0, 1))
    }
)
port21: BinaryAssociation = BinaryAssociation(
    name="port21",
    ends={
        Property(name="ioT_Portnumber", type=ioT_Server, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_Server22", type=ioT_Portnumber, multiplicity=Multiplicity(0, 1), is_composite=True)
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
left45: BinaryAssociation = BinaryAssociation(
    name="left45",
    ends={
        Property(name="ioT_Condition46", type=ioT_OrCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_OrCondition", type=ioT_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right47: BinaryAssociation = BinaryAssociation(
    name="right47",
    ends={
        Property(name="ioT_Condition49", type=ioT_OrCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_OrCondition48", type=ioT_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
types23: BinaryAssociation = BinaryAssociation(
    name="types23",
    ends={
        Property(name="ioT_DestinationType", type=ioT_DestinationTypes, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_DestinationTypes", type=ioT_DestinationType, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
device28: BinaryAssociation = BinaryAssociation(
    name="device28",
    ends={
        Property(name="ioT_Device30", type=ioT_FetchData, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_FetchData29", type=ioT_Device, multiplicity=Multiplicity(0, 1))
    }
)
destination31: BinaryAssociation = BinaryAssociation(
    name="destination31",
    ends={
        Property(name="ioT_EObject33", type=ioT_FetchData, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_FetchData32", type=ioT_EObject, multiplicity=Multiplicity(0, 1))
    }
)
condition34: BinaryAssociation = BinaryAssociation(
    name="condition34",
    ends={
        Property(name="ioT_FetchDataCondition", type=ioT_FetchData, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_FetchData35", type=ioT_FetchDataCondition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
triggered36: BinaryAssociation = BinaryAssociation(
    name="triggered36",
    ends={
        Property(name="ioT_FetchDataExpression", type=ioT_FetchData, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_FetchData37", type=ioT_FetchDataExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
duration38: BinaryAssociation = BinaryAssociation(
    name="duration38",
    ends={
        Property(name="ioT_Time", type=ioT_FetchDataExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_FetchDataExpression39", type=ioT_Time, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition40: BinaryAssociation = BinaryAssociation(
    name="condition40",
    ends={
        Property(name="ioT_Condition", type=ioT_FetchDataCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_FetchDataCondition41", type=ioT_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
else43: BinaryAssociation = BinaryAssociation(
    name="else43",
    ends={
        Property(name="ioT_FetchDataCondition44", type=ioT_FetchDataCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_FetchDataCondition42", type=ioT_FetchDataCondition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left50: BinaryAssociation = BinaryAssociation(
    name="left50",
    ends={
        Property(name="ioT_Condition51", type=ioT_AndCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_AndCondition", type=ioT_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right52: BinaryAssociation = BinaryAssociation(
    name="right52",
    ends={
        Property(name="ioT_Condition54", type=ioT_AndCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_AndCondition53", type=ioT_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left55: BinaryAssociation = BinaryAssociation(
    name="left55",
    ends={
        Property(name="ioT_Condition56", type=ioT_ComparisonCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_ComparisonCondition", type=ioT_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right57: BinaryAssociation = BinaryAssociation(
    name="right57",
    ends={
        Property(name="ioT_Condition59", type=ioT_ComparisonCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="ioT_ComparisonCondition58", type=ioT_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_ioT_Method_Condition = Generalization(general=Condition, specific=ioT_Method)
gen_ioT_AndCondition_Condition = Generalization(general=Condition, specific=ioT_AndCondition)
gen_ioT_OrCondition_Condition = Generalization(general=Condition, specific=ioT_OrCondition)
gen_ioT_ComparisonCondition_Condition = Generalization(general=Condition, specific=ioT_ComparisonCondition)
gen_ioT_LiteralBool_Condition = Generalization(general=Condition, specific=ioT_LiteralBool)
gen_ioT_LiteralNumber_Condition = Generalization(general=Condition, specific=ioT_LiteralNumber)

# Domain Model
domain_model = DomainModel(
    name="ioT",
    types={ioT_SensorGetMethod, ioT_Method, ioT_System, ioT_EObject, ioT_SensorType, ioT_SensorTypes, ioT_Sensor, ioT_SensorGroup, ioT_Portnumber, ioT_DestinationType, ioT_DestinationTypes, Condition, ioT_DeviceType, ioT_DeviceTypes, ioT_Device, ioT_ServerType, ioT_ServerTypes, ioT_Server, ioT_Ip, ioT_AndCondition, ioT_Destination, ioT_FetchData, ioT_FetchDataCondition, ioT_FetchDataExpression, ioT_Time, ioT_Condition, ioT_OrCondition, ioT_ComparisonCondition, ioT_LiteralBool, ioT_LiteralNumber},
    associations={sensors4, method6, type7, system0, types1, type2, port21, types10, type11, devices13, types16, type17, ip19, left45, right47, types23, type24, filter26, device28, destination31, condition34, triggered36, duration38, condition40, else43, left50, right52, left55, right57},
    generalizations={gen_ioT_Method_Condition, gen_ioT_AndCondition_Condition, gen_ioT_OrCondition_Condition, gen_ioT_ComparisonCondition_Condition, gen_ioT_LiteralBool_Condition, gen_ioT_LiteralNumber_Condition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)