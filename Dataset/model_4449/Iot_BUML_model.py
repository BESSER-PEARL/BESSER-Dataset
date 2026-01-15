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
iot_IotSystem = Class(name="iot::IotSystem")
iot_IotSystemSpec = Class(name="iot::IotSystemSpec")
iot_BrokerSpec = Class(name="iot::BrokerSpec")
iot_Message = Class(name="iot::Message")
iot_Event = Class(name="iot::Event")
Message = Class(name="Message")
iot_Dispatch = Class(name="iot::Dispatch")
iot_Request = Class(name="iot::Request")

# iot_IotSystem class attributes and methods

# iot_IotSystemSpec class attributes and methods
iot_IotSystemSpec_name: Property = Property(name="name", type=StringType)
iot_IotSystemSpec.attributes={iot_IotSystemSpec_name}

# iot_BrokerSpec class attributes and methods
iot_BrokerSpec_brokerHost: Property = Property(name="brokerHost", type=StringType)
iot_BrokerSpec_brokerPort: Property = Property(name="brokerPort", type=IntegerType)
iot_BrokerSpec.attributes={iot_BrokerSpec_brokerPort, iot_BrokerSpec_brokerHost}

# iot_Message class attributes and methods
iot_Message_name: Property = Property(name="name", type=StringType)
iot_Message_msg: Property = Property(name="msg", type=StringType)
iot_Message.attributes={iot_Message_msg, iot_Message_name}

# iot_Event class attributes and methods

# Message class attributes and methods

# iot_Dispatch class attributes and methods

# iot_Request class attributes and methods

# Relationships
spec0: BinaryAssociation = BinaryAssociation(
    name="spec0",
    ends={
        Property(name="iot_IotSystemSpec", type=iot_IotSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_IotSystem", type=iot_IotSystemSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mqttBroker1: BinaryAssociation = BinaryAssociation(
    name="mqttBroker1",
    ends={
        Property(name="iot_BrokerSpec", type=iot_IotSystemSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_IotSystemSpec2", type=iot_BrokerSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
message3: BinaryAssociation = BinaryAssociation(
    name="message3",
    ends={
        Property(name="iot_Message", type=iot_IotSystemSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="iot_IotSystemSpec4", type=iot_Message, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_iot_Event_Message = Generalization(general=Message, specific=iot_Event)
gen_iot_Dispatch_Message = Generalization(general=Message, specific=iot_Dispatch)
gen_iot_Request_Message = Generalization(general=Message, specific=iot_Request)

# Domain Model
domain_model = DomainModel(
    name="iot",
    types={iot_IotSystem, iot_IotSystemSpec, iot_BrokerSpec, iot_Message, iot_Event, Message, iot_Dispatch, iot_Request},
    associations={spec0, mqttBroker1, message3},
    generalizations={gen_iot_Event_Message, gen_iot_Dispatch_Message, gen_iot_Request_Message},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)