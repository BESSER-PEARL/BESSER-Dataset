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
Datatype: Enumeration = Enumeration(
    name="Datatype",
    literals={
            EnumerationLiteral(name="int8"),
			EnumerationLiteral(name="int16"),
			EnumerationLiteral(name="int32"),
			EnumerationLiteral(name="int64"),
			EnumerationLiteral(name="float32"),
			EnumerationLiteral(name="float64"),
			EnumerationLiteral(name="string"),
			EnumerationLiteral(name="msg")
    }
)

# Classes
rosmodel_Package = Class(name="rosmodel::Package")
rosmodel_Node = Class(name="rosmodel::Node")
rosmodel_Topic = Class(name="rosmodel::Topic")
rosmodel_Message = Class(name="rosmodel::Message")
rosmodel_ServiceType = Class(name="rosmodel::ServiceType")
rosmodel_ActionMessage = Class(name="rosmodel::ActionMessage")
rosmodel_Publisher = Class(name="rosmodel::Publisher")
rosmodel_Subscriber = Class(name="rosmodel::Subscriber")
rosmodel_ServiceClient = Class(name="rosmodel::ServiceClient")
rosmodel_ServiceServer = Class(name="rosmodel::ServiceServer")
rosmodel_ActionClient = Class(name="rosmodel::ActionClient")
rosmodel_ActionServer = Class(name="rosmodel::ActionServer")
rosmodel_State = Class(name="rosmodel::State")
rosmodel_Transition = Class(name="rosmodel::Transition")
rosmodel_Action = Class(name="rosmodel::Action")
rosmodel_Event = Class(name="rosmodel::Event")
rosmodel_Field = Class(name="rosmodel::Field")

# rosmodel_Package class attributes and methods
rosmodel_Package_name: Property = Property(name="name", type=StringType)
rosmodel_Package_author: Property = Property(name="author", type=StringType)
rosmodel_Package_author_email: Property = Property(name="author_email", type=StringType)
rosmodel_Package_description: Property = Property(name="description", type=StringType)
rosmodel_Package_depends: Property = Property(name="depends", type=StringType)
rosmodel_Package.attributes={rosmodel_Package_author_email, rosmodel_Package_name, rosmodel_Package_depends, rosmodel_Package_author, rosmodel_Package_description}

# rosmodel_Node class attributes and methods
rosmodel_Node_name: Property = Property(name="name", type=StringType)
rosmodel_Node_frequency: Property = Property(name="frequency", type=FloatType)
rosmodel_Node.attributes={rosmodel_Node_name, rosmodel_Node_frequency}

# rosmodel_Topic class attributes and methods
rosmodel_Topic_name: Property = Property(name="name", type=StringType)
rosmodel_Topic.attributes={rosmodel_Topic_name}

# rosmodel_Message class attributes and methods
rosmodel_Message_name: Property = Property(name="name", type=StringType)
rosmodel_Message.attributes={rosmodel_Message_name}

# rosmodel_ServiceType class attributes and methods
rosmodel_ServiceType_name: Property = Property(name="name", type=StringType)
rosmodel_ServiceType.attributes={rosmodel_ServiceType_name}

# rosmodel_ActionMessage class attributes and methods
rosmodel_ActionMessage_name: Property = Property(name="name", type=StringType)
rosmodel_ActionMessage.attributes={rosmodel_ActionMessage_name}

# rosmodel_Publisher class attributes and methods
rosmodel_Publisher_name: Property = Property(name="name", type=StringType)
rosmodel_Publisher_queue_size: Property = Property(name="queue_size", type=IntegerType)
rosmodel_Publisher_msg: Property = Property(name="msg", type=StringType)
rosmodel_Publisher.attributes={rosmodel_Publisher_name, rosmodel_Publisher_msg, rosmodel_Publisher_queue_size}

# rosmodel_Subscriber class attributes and methods
rosmodel_Subscriber_name: Property = Property(name="name", type=StringType)
rosmodel_Subscriber_queue_size: Property = Property(name="queue_size", type=IntegerType)
rosmodel_Subscriber_msg: Property = Property(name="msg", type=StringType)
rosmodel_Subscriber.attributes={rosmodel_Subscriber_queue_size, rosmodel_Subscriber_name, rosmodel_Subscriber_msg}

# rosmodel_ServiceClient class attributes and methods
rosmodel_ServiceClient_name: Property = Property(name="name", type=StringType)
rosmodel_ServiceClient.attributes={rosmodel_ServiceClient_name}

# rosmodel_ServiceServer class attributes and methods
rosmodel_ServiceServer_name: Property = Property(name="name", type=StringType)
rosmodel_ServiceServer.attributes={rosmodel_ServiceServer_name}

# rosmodel_ActionClient class attributes and methods
rosmodel_ActionClient_name: Property = Property(name="name", type=StringType)
rosmodel_ActionClient.attributes={rosmodel_ActionClient_name}

# rosmodel_ActionServer class attributes and methods
rosmodel_ActionServer_name: Property = Property(name="name", type=StringType)
rosmodel_ActionServer.attributes={rosmodel_ActionServer_name}

# rosmodel_State class attributes and methods
rosmodel_State_name: Property = Property(name="name", type=StringType)
rosmodel_State.attributes={rosmodel_State_name}

# rosmodel_Transition class attributes and methods
rosmodel_Transition_name: Property = Property(name="name", type=StringType)
rosmodel_Transition.attributes={rosmodel_Transition_name}

# rosmodel_Action class attributes and methods
rosmodel_Action_name: Property = Property(name="name", type=StringType)
rosmodel_Action.attributes={rosmodel_Action_name}

# rosmodel_Event class attributes and methods
rosmodel_Event_name: Property = Property(name="name", type=StringType)
rosmodel_Event.attributes={rosmodel_Event_name}

# rosmodel_Field class attributes and methods
rosmodel_Field_name: Property = Property(name="name", type=StringType)
rosmodel_Field_type: Property = Property(name="type", type=StringType)
rosmodel_Field.attributes={rosmodel_Field_name, rosmodel_Field_type}

# Relationships
node0: BinaryAssociation = BinaryAssociation(
    name="node0",
    ends={
        Property(name="rosmodel_Node", type=rosmodel_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="rosmodel_Package", type=rosmodel_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
topic1: BinaryAssociation = BinaryAssociation(
    name="topic1",
    ends={
        Property(name="rosmodel_Topic", type=rosmodel_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="rosmodel_Package2", type=rosmodel_Topic, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
message3: BinaryAssociation = BinaryAssociation(
    name="message3",
    ends={
        Property(name="rosmodel_Message", type=rosmodel_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="rosmodel_Package4", type=rosmodel_Message, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
servicetype5: BinaryAssociation = BinaryAssociation(
    name="servicetype5",
    ends={
        Property(name="rosmodel_ServiceType", type=rosmodel_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="rosmodel_Package6", type=rosmodel_ServiceType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actionmessage7: BinaryAssociation = BinaryAssociation(
    name="actionmessage7",
    ends={
        Property(name="rosmodel_ActionMessage", type=rosmodel_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="rosmodel_Package8", type=rosmodel_ActionMessage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
publisher9: BinaryAssociation = BinaryAssociation(
    name="publisher9",
    ends={
        Property(name="rosmodel_Publisher", type=rosmodel_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="rosmodel_Node10", type=rosmodel_Publisher, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subscriber11: BinaryAssociation = BinaryAssociation(
    name="subscriber11",
    ends={
        Property(name="rosmodel_Subscriber", type=rosmodel_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="rosmodel_Node12", type=rosmodel_Subscriber, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
serviceclient13: BinaryAssociation = BinaryAssociation(
    name="serviceclient13",
    ends={
        Property(name="rosmodel_ServiceClient", type=rosmodel_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="rosmodel_Node14", type=rosmodel_ServiceClient, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
serviceserver15: BinaryAssociation = BinaryAssociation(
    name="serviceserver15",
    ends={
        Property(name="rosmodel_ServiceServer", type=rosmodel_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="rosmodel_Node16", type=rosmodel_ServiceServer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actionclient17: BinaryAssociation = BinaryAssociation(
    name="actionclient17",
    ends={
        Property(name="rosmodel_ActionClient", type=rosmodel_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="rosmodel_Node18", type=rosmodel_ActionClient, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actionserver19: BinaryAssociation = BinaryAssociation(
    name="actionserver19",
    ends={
        Property(name="rosmodel_ActionServer", type=rosmodel_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="rosmodel_Node20", type=rosmodel_ActionServer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state21: BinaryAssociation = BinaryAssociation(
    name="state21",
    ends={
        Property(name="rosmodel_State", type=rosmodel_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="rosmodel_Node22", type=rosmodel_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition23: BinaryAssociation = BinaryAssociation(
    name="transition23",
    ends={
        Property(name="rosmodel_Transition", type=rosmodel_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="rosmodel_Node24", type=rosmodel_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action25: BinaryAssociation = BinaryAssociation(
    name="action25",
    ends={
        Property(name="rosmodel_Action", type=rosmodel_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="rosmodel_Node26", type=rosmodel_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event27: BinaryAssociation = BinaryAssociation(
    name="event27",
    ends={
        Property(name="rosmodel_Event", type=rosmodel_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="rosmodel_Node28", type=rosmodel_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target29: BinaryAssociation = BinaryAssociation(
    name="target29",
    ends={
        Property(name="rosmodel_Publisher30", type=rosmodel_Topic, multiplicity=Multiplicity(1, 1)),
        Property(name="rosmodel_Topic31", type=rosmodel_Publisher, multiplicity=Multiplicity(1, 1))
    }
)
source32: BinaryAssociation = BinaryAssociation(
    name="source32",
    ends={
        Property(name="rosmodel_Topic34", type=rosmodel_Subscriber, multiplicity=Multiplicity(1, 1)),
        Property(name="rosmodel_Subscriber33", type=rosmodel_Topic, multiplicity=Multiplicity(1, 1))
    }
)
field35: BinaryAssociation = BinaryAssociation(
    name="field35",
    ends={
        Property(name="rosmodel_Field", type=rosmodel_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="rosmodel_Message36", type=rosmodel_Field, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
request37: BinaryAssociation = BinaryAssociation(
    name="request37",
    ends={
        Property(name="rosmodel_Field39", type=rosmodel_ServiceType, multiplicity=Multiplicity(1, 1)),
        Property(name="rosmodel_ServiceType38", type=rosmodel_Field, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
response40: BinaryAssociation = BinaryAssociation(
    name="response40",
    ends={
        Property(name="rosmodel_Field42", type=rosmodel_ServiceType, multiplicity=Multiplicity(1, 1)),
        Property(name="rosmodel_ServiceType41", type=rosmodel_Field, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
servicetype43: BinaryAssociation = BinaryAssociation(
    name="servicetype43",
    ends={
        Property(name="rosmodel_ServiceType45", type=rosmodel_ServiceServer, multiplicity=Multiplicity(1, 1)),
        Property(name="rosmodel_ServiceServer44", type=rosmodel_ServiceType, multiplicity=Multiplicity(0, 1))
    }
)
servicetype46: BinaryAssociation = BinaryAssociation(
    name="servicetype46",
    ends={
        Property(name="rosmodel_ServiceType48", type=rosmodel_ServiceClient, multiplicity=Multiplicity(1, 1)),
        Property(name="rosmodel_ServiceClient47", type=rosmodel_ServiceType, multiplicity=Multiplicity(0, 1))
    }
)
goal49: BinaryAssociation = BinaryAssociation(
    name="goal49",
    ends={
        Property(name="rosmodel_Field51", type=rosmodel_ActionMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="rosmodel_ActionMessage50", type=rosmodel_Field, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
result52: BinaryAssociation = BinaryAssociation(
    name="result52",
    ends={
        Property(name="rosmodel_Field54", type=rosmodel_ActionMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="rosmodel_ActionMessage53", type=rosmodel_Field, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
feedback55: BinaryAssociation = BinaryAssociation(
    name="feedback55",
    ends={
        Property(name="rosmodel_Field57", type=rosmodel_ActionMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="rosmodel_ActionMessage56", type=rosmodel_Field, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actionmessage58: BinaryAssociation = BinaryAssociation(
    name="actionmessage58",
    ends={
        Property(name="rosmodel_ActionMessage60", type=rosmodel_ActionServer, multiplicity=Multiplicity(1, 1)),
        Property(name="rosmodel_ActionServer59", type=rosmodel_ActionMessage, multiplicity=Multiplicity(0, 1))
    }
)
actionmessage61: BinaryAssociation = BinaryAssociation(
    name="actionmessage61",
    ends={
        Property(name="rosmodel_ActionMessage63", type=rosmodel_ActionClient, multiplicity=Multiplicity(1, 1)),
        Property(name="rosmodel_ActionClient62", type=rosmodel_ActionMessage, multiplicity=Multiplicity(0, 1))
    }
)
transition64: BinaryAssociation = BinaryAssociation(
    name="transition64",
    ends={
        Property(name="rosmodel_Transition66", type=rosmodel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="rosmodel_State65", type=rosmodel_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
substate68: BinaryAssociation = BinaryAssociation(
    name="substate68",
    ends={
        Property(name="rosmodel_State69", type=rosmodel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="rosmodel_State67", type=rosmodel_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action70: BinaryAssociation = BinaryAssociation(
    name="action70",
    ends={
        Property(name="rosmodel_Action72", type=rosmodel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="rosmodel_State71", type=rosmodel_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entryaction73: BinaryAssociation = BinaryAssociation(
    name="entryaction73",
    ends={
        Property(name="rosmodel_Action75", type=rosmodel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="rosmodel_State74", type=rosmodel_Action, multiplicity=Multiplicity(0, 1))
    }
)
exitaction76: BinaryAssociation = BinaryAssociation(
    name="exitaction76",
    ends={
        Property(name="rosmodel_Action78", type=rosmodel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="rosmodel_State77", type=rosmodel_Action, multiplicity=Multiplicity(0, 1))
    }
)
event79: BinaryAssociation = BinaryAssociation(
    name="event79",
    ends={
        Property(name="rosmodel_Event81", type=rosmodel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="rosmodel_State80", type=rosmodel_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source82: BinaryAssociation = BinaryAssociation(
    name="source82",
    ends={
        Property(name="rosmodel_State84", type=rosmodel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="rosmodel_Transition83", type=rosmodel_State, multiplicity=Multiplicity(1, 1))
    }
)
target85: BinaryAssociation = BinaryAssociation(
    name="target85",
    ends={
        Property(name="rosmodel_State87", type=rosmodel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="rosmodel_Transition86", type=rosmodel_State, multiplicity=Multiplicity(1, 1))
    }
)
action88: BinaryAssociation = BinaryAssociation(
    name="action88",
    ends={
        Property(name="rosmodel_Action90", type=rosmodel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="rosmodel_Transition89", type=rosmodel_Action, multiplicity=Multiplicity(0, 1))
    }
)
guard91: BinaryAssociation = BinaryAssociation(
    name="guard91",
    ends={
        Property(name="rosmodel_Action93", type=rosmodel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="rosmodel_Transition92", type=rosmodel_Action, multiplicity=Multiplicity(0, 1))
    }
)
transition94: BinaryAssociation = BinaryAssociation(
    name="transition94",
    ends={
        Property(name="rosmodel_Transition96", type=rosmodel_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="rosmodel_Event95", type=rosmodel_Transition, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="rosmodel",
    types={rosmodel_Package, rosmodel_Node, rosmodel_Topic, rosmodel_Message, rosmodel_ServiceType, rosmodel_ActionMessage, rosmodel_Publisher, rosmodel_Subscriber, rosmodel_ServiceClient, rosmodel_ServiceServer, rosmodel_ActionClient, rosmodel_ActionServer, rosmodel_State, rosmodel_Transition, rosmodel_Action, rosmodel_Event, rosmodel_Field, Datatype},
    associations={node0, topic1, message3, servicetype5, actionmessage7, publisher9, subscriber11, serviceclient13, serviceserver15, actionclient17, actionserver19, state21, transition23, action25, event27, target29, source32, field35, request37, response40, servicetype43, servicetype46, goal49, result52, feedback55, actionmessage58, actionmessage61, transition64, substate68, action70, entryaction73, exitaction76, event79, source82, target85, action88, guard91, transition94},
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