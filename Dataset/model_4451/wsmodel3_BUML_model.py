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
ControllerType: Enumeration = Enumeration(
    name="ControllerType",
    literals={
            EnumerationLiteral(name="Undefined"),
			EnumerationLiteral(name="ESP8266")
    }
)

DBType: Enumeration = Enumeration(
    name="DBType",
    literals={
            EnumerationLiteral(name="Undefined"),
			EnumerationLiteral(name="MySQL")
    }
)

SensorType: Enumeration = Enumeration(
    name="SensorType",
    literals={
            EnumerationLiteral(name="Undefined"),
			EnumerationLiteral(name="CO2"),
			EnumerationLiteral(name="Light"),
			EnumerationLiteral(name="Button"),
			EnumerationLiteral(name="HumidityG"),
			EnumerationLiteral(name="Vibration"),
			EnumerationLiteral(name="Temperature"),
			EnumerationLiteral(name="Movement"),
			EnumerationLiteral(name="Contact"),
			EnumerationLiteral(name="TempHum")
    }
)

ActuatorType: Enumeration = Enumeration(
    name="ActuatorType",
    literals={
            EnumerationLiteral(name="Buzzer"),
			EnumerationLiteral(name="Led"),
			EnumerationLiteral(name="Relay"),
			EnumerationLiteral(name="Servo"),
			EnumerationLiteral(name="LCD"),
			EnumerationLiteral(name="Undefined")
    }
)

PortType: Enumeration = Enumeration(
    name="PortType",
    literals={
            EnumerationLiteral(name="Digital"),
			EnumerationLiteral(name="Analog")
    }
)

CommunicationType: Enumeration = Enumeration(
    name="CommunicationType",
    literals={
            EnumerationLiteral(name="Undefined"),
			EnumerationLiteral(name="WiFi"),
			EnumerationLiteral(name="Serial")
    }
)

MessageBrokerType: Enumeration = Enumeration(
    name="MessageBrokerType",
    literals={
            EnumerationLiteral(name="Undefined"),
			EnumerationLiteral(name="MQTT")
    }
)

# Classes
wsmodel3_System = Class(name="wsmodel3::System")
Server = Class(name="Server")
wsmodel3_WebService = Class(name="wsmodel3::WebService")
wsmodel3_Server = Class(name="wsmodel3::Server", is_abstract=True)
wsmodel3_IoTNode = Class(name="wsmodel3::IoTNode")
wsmodel3_AccesPoint = Class(name="wsmodel3::AccesPoint")
wsmodel3_IntegrationPattern = Class(name="wsmodel3::IntegrationPattern")
wsmodel3_MessageBroker = Class(name="wsmodel3::MessageBroker")
wsmodel3_ExternalAPI = Class(name="wsmodel3::ExternalAPI")
wsmodel3_Device = Class(name="wsmodel3::Device", is_abstract=True)
wsmodel3_REST = Class(name="wsmodel3::REST")
wsmodel3_WebServer = Class(name="wsmodel3::WebServer")
wsmodel3_DBServer = Class(name="wsmodel3::DBServer")
wsmodel3_CommunicationData = Class(name="wsmodel3::CommunicationData")
wsmodel3_DeviceData = Class(name="wsmodel3::DeviceData")
wsmodel3_Sensor = Class(name="wsmodel3::Sensor")
Device = Class(name="Device")
wsmodel3_Actuator = Class(name="wsmodel3::Actuator")
wsmodel3_Controller = Class(name="wsmodel3::Controller")
wsmodel3_Port = Class(name="wsmodel3::Port", is_abstract=True)
wsmodel3_Communication = Class(name="wsmodel3::Communication")
wsmodel3_InputBridge = Class(name="wsmodel3::InputBridge")
Bridge = Class(name="Bridge")
wsmodel3_OutputBridge = Class(name="wsmodel3::OutputBridge")
wsmodel3_InputPort = Class(name="wsmodel3::InputPort")
Port = Class(name="Port")
wsmodel3_OutputPort = Class(name="wsmodel3::OutputPort")
Data = Class(name="Data")
wsmodel3_Data = Class(name="wsmodel3::Data", is_abstract=True)
wsmodel3_Bridge = Class(name="wsmodel3::Bridge", is_abstract=True)
wsmodel3_Break = Class(name="wsmodel3::Break")
wsmodel3_InputOrchestrator = Class(name="wsmodel3::InputOrchestrator")
wsmodel3_Orchestrator = Class(name="wsmodel3::Orchestrator")
wsmodel3_Function = Class(name="wsmodel3::Function")
wsmodel3_OutputOrchestrator = Class(name="wsmodel3::OutputOrchestrator")
wsmodel3_OrchestratorData = Class(name="wsmodel3::OrchestratorData")

# wsmodel3_System class attributes and methods
wsmodel3_System_name: Property = Property(name="name", type=StringType)
wsmodel3_System.attributes={wsmodel3_System_name}

# Server class attributes and methods

# wsmodel3_WebService class attributes and methods

# wsmodel3_Server class attributes and methods
wsmodel3_Server_host: Property = Property(name="host", type=StringType)
wsmodel3_Server.attributes={wsmodel3_Server_host}

# wsmodel3_IoTNode class attributes and methods

# wsmodel3_AccesPoint class attributes and methods
wsmodel3_AccesPoint_ssid: Property = Property(name="ssid", type=StringType)
wsmodel3_AccesPoint_pass: Property = Property(name="pass", type=StringType)
wsmodel3_AccesPoint.attributes={wsmodel3_AccesPoint_ssid, wsmodel3_AccesPoint_pass}

# wsmodel3_IntegrationPattern class attributes and methods

# wsmodel3_MessageBroker class attributes and methods
wsmodel3_MessageBroker_type: Property = Property(name="type", type=StringType)
wsmodel3_MessageBroker_port: Property = Property(name="port", type=IntegerType)
wsmodel3_MessageBroker_host: Property = Property(name="host", type=StringType)
wsmodel3_MessageBroker_usser: Property = Property(name="usser", type=StringType)
wsmodel3_MessageBroker_pass: Property = Property(name="pass", type=StringType)
wsmodel3_MessageBroker.attributes={wsmodel3_MessageBroker_pass, wsmodel3_MessageBroker_port, wsmodel3_MessageBroker_type, wsmodel3_MessageBroker_host, wsmodel3_MessageBroker_usser}

# wsmodel3_ExternalAPI class attributes and methods
wsmodel3_ExternalAPI_URI: Property = Property(name="URI", type=StringType)
wsmodel3_ExternalAPI.attributes={wsmodel3_ExternalAPI_URI}

# wsmodel3_Device class attributes and methods
wsmodel3_Device_name: Property = Property(name="name", type=StringType)
wsmodel3_Device.attributes={wsmodel3_Device_name}

# wsmodel3_REST class attributes and methods
wsmodel3_REST_URI: Property = Property(name="URI", type=StringType)
wsmodel3_REST_port: Property = Property(name="port", type=IntegerType)
wsmodel3_REST.attributes={wsmodel3_REST_URI, wsmodel3_REST_port}

# wsmodel3_WebServer class attributes and methods

# wsmodel3_DBServer class attributes and methods
wsmodel3_DBServer_usser: Property = Property(name="usser", type=StringType)
wsmodel3_DBServer_pass: Property = Property(name="pass", type=StringType)
wsmodel3_DBServer_type: Property = Property(name="type", type=StringType)
wsmodel3_DBServer_port: Property = Property(name="port", type=IntegerType)
wsmodel3_DBServer_database: Property = Property(name="database", type=StringType)
wsmodel3_DBServer.attributes={wsmodel3_DBServer_port, wsmodel3_DBServer_type, wsmodel3_DBServer_pass, wsmodel3_DBServer_usser, wsmodel3_DBServer_database}

# wsmodel3_CommunicationData class attributes and methods

# wsmodel3_DeviceData class attributes and methods

# wsmodel3_Sensor class attributes and methods
wsmodel3_Sensor_type: Property = Property(name="type", type=StringType)
wsmodel3_Sensor.attributes={wsmodel3_Sensor_type}

# Device class attributes and methods

# wsmodel3_Actuator class attributes and methods
wsmodel3_Actuator_type: Property = Property(name="type", type=StringType)
wsmodel3_Actuator.attributes={wsmodel3_Actuator_type}

# wsmodel3_Controller class attributes and methods
wsmodel3_Controller_type: Property = Property(name="type", type=StringType)
wsmodel3_Controller.attributes={wsmodel3_Controller_type}

# wsmodel3_Port class attributes and methods
wsmodel3_Port_id: Property = Property(name="id", type=StringType)
wsmodel3_Port_type: Property = Property(name="type", type=StringType)
wsmodel3_Port.attributes={wsmodel3_Port_id, wsmodel3_Port_type}

# wsmodel3_Communication class attributes and methods
wsmodel3_Communication_type: Property = Property(name="type", type=StringType)
wsmodel3_Communication_name: Property = Property(name="name", type=StringType)
wsmodel3_Communication.attributes={wsmodel3_Communication_name, wsmodel3_Communication_type}

# wsmodel3_InputBridge class attributes and methods
wsmodel3_InputBridge_URI: Property = Property(name="URI", type=StringType)
wsmodel3_InputBridge.attributes={wsmodel3_InputBridge_URI}

# Bridge class attributes and methods

# wsmodel3_OutputBridge class attributes and methods

# wsmodel3_InputPort class attributes and methods

# Port class attributes and methods

# wsmodel3_OutputPort class attributes and methods

# Data class attributes and methods

# wsmodel3_Data class attributes and methods
wsmodel3_Data_id: Property = Property(name="id", type=StringType)
wsmodel3_Data_Date: Property = Property(name="Date", type=StringType)
wsmodel3_Data_Time: Property = Property(name="Time", type=StringType)
wsmodel3_Data_Location: Property = Property(name="Location", type=StringType)
wsmodel3_Data_Attribute: Property = Property(name="Attribute", type=StringType)
wsmodel3_Data_Artefact: Property = Property(name="Artefact", type=StringType)
wsmodel3_Data.attributes={wsmodel3_Data_Date, wsmodel3_Data_Location, wsmodel3_Data_Attribute, wsmodel3_Data_Artefact, wsmodel3_Data_id, wsmodel3_Data_Time}

# wsmodel3_Bridge class attributes and methods
wsmodel3_Bridge_topic: Property = Property(name="topic", type=StringType)
wsmodel3_Bridge_host: Property = Property(name="host", type=StringType)
wsmodel3_Bridge_port: Property = Property(name="port", type=IntegerType)
wsmodel3_Bridge.attributes={wsmodel3_Bridge_topic, wsmodel3_Bridge_host, wsmodel3_Bridge_port}

# wsmodel3_Break class attributes and methods
wsmodel3_Break_expression: Property = Property(name="expression", type=StringType)
wsmodel3_Break.attributes={wsmodel3_Break_expression}

# wsmodel3_InputOrchestrator class attributes and methods
wsmodel3_InputOrchestrator_URI: Property = Property(name="URI", type=StringType)
wsmodel3_InputOrchestrator.attributes={wsmodel3_InputOrchestrator_URI}

# wsmodel3_Orchestrator class attributes and methods
wsmodel3_Orchestrator_name: Property = Property(name="name", type=StringType)
wsmodel3_Orchestrator_port: Property = Property(name="port", type=StringType)
wsmodel3_Orchestrator.attributes={wsmodel3_Orchestrator_name, wsmodel3_Orchestrator_port}

# wsmodel3_Function class attributes and methods
wsmodel3_Function_expression: Property = Property(name="expression", type=StringType)
wsmodel3_Function.attributes={wsmodel3_Function_expression}

# wsmodel3_OutputOrchestrator class attributes and methods

# wsmodel3_OrchestratorData class attributes and methods

# Relationships
device21: BinaryAssociation = BinaryAssociation(
    name="device21",
    ends={
        Property(name="wsmodel3_Device23", type=wsmodel3_REST, multiplicity=Multiplicity(1, 1)),
        Property(name="wsmodel3_REST22", type=wsmodel3_Device, multiplicity=Multiplicity(0, 1))
    }
)
webservice0: BinaryAssociation = BinaryAssociation(
    name="webservice0",
    ends={
        Property(name="wsmodel3_WebService", type=wsmodel3_System, multiplicity=Multiplicity(1, 1)),
        Property(name="wsmodel3_System", type=wsmodel3_WebService, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
server1: BinaryAssociation = BinaryAssociation(
    name="server1",
    ends={
        Property(name="wsmodel3_Server", type=wsmodel3_System, multiplicity=Multiplicity(1, 1)),
        Property(name="wsmodel3_System2", type=wsmodel3_Server, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
iotnode3: BinaryAssociation = BinaryAssociation(
    name="iotnode3",
    ends={
        Property(name="wsmodel3_IoTNode", type=wsmodel3_System, multiplicity=Multiplicity(1, 1)),
        Property(name="wsmodel3_System4", type=wsmodel3_IoTNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
accespoint5: BinaryAssociation = BinaryAssociation(
    name="accespoint5",
    ends={
        Property(name="wsmodel3_AccesPoint", type=wsmodel3_System, multiplicity=Multiplicity(1, 1)),
        Property(name="wsmodel3_System6", type=wsmodel3_AccesPoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
integrationpattern7: BinaryAssociation = BinaryAssociation(
    name="integrationpattern7",
    ends={
        Property(name="wsmodel3_IntegrationPattern", type=wsmodel3_System, multiplicity=Multiplicity(1, 1)),
        Property(name="wsmodel3_System8", type=wsmodel3_IntegrationPattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
messagebroker9: BinaryAssociation = BinaryAssociation(
    name="messagebroker9",
    ends={
        Property(name="wsmodel3_MessageBroker", type=wsmodel3_System, multiplicity=Multiplicity(1, 1)),
        Property(name="wsmodel3_System10", type=wsmodel3_MessageBroker, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
externalapi11: BinaryAssociation = BinaryAssociation(
    name="externalapi11",
    ends={
        Property(name="wsmodel3_ExternalAPI", type=wsmodel3_System, multiplicity=Multiplicity(1, 1)),
        Property(name="wsmodel3_System12", type=wsmodel3_ExternalAPI, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
device13: BinaryAssociation = BinaryAssociation(
    name="device13",
    ends={
        Property(name="wsmodel3_Device", type=wsmodel3_IoTNode, multiplicity=Multiplicity(1, 1)),
        Property(name="wsmodel3_IoTNode14", type=wsmodel3_Device, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rest15: BinaryAssociation = BinaryAssociation(
    name="rest15",
    ends={
        Property(name="wsmodel3_REST", type=wsmodel3_WebService, multiplicity=Multiplicity(1, 1)),
        Property(name="wsmodel3_WebService16", type=wsmodel3_REST, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
webserver17: BinaryAssociation = BinaryAssociation(
    name="webserver17",
    ends={
        Property(name="wsmodel3_WebServer", type=wsmodel3_WebService, multiplicity=Multiplicity(1, 1)),
        Property(name="wsmodel3_WebService18", type=wsmodel3_WebServer, multiplicity=Multiplicity(1, 1))
    }
)
dbserver19: BinaryAssociation = BinaryAssociation(
    name="dbserver19",
    ends={
        Property(name="wsmodel3_DBServer", type=wsmodel3_WebService, multiplicity=Multiplicity(1, 1)),
        Property(name="wsmodel3_WebService20", type=wsmodel3_DBServer, multiplicity=Multiplicity(1, 1))
    }
)
communicationdata29: BinaryAssociation = BinaryAssociation(
    name="communicationdata29",
    ends={
        Property(name="wsmodel3_CommunicationData", type=wsmodel3_Communication, multiplicity=Multiplicity(1, 1)),
        Property(name="wsmodel3_Communication30", type=wsmodel3_CommunicationData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
accespoint31: BinaryAssociation = BinaryAssociation(
    name="accespoint31",
    ends={
        Property(name="wsmodel3_AccesPoint33", type=wsmodel3_Communication, multiplicity=Multiplicity(1, 1)),
        Property(name="wsmodel3_Communication32", type=wsmodel3_AccesPoint, multiplicity=Multiplicity(0, 1))
    }
)
devicedata24: BinaryAssociation = BinaryAssociation(
    name="devicedata24",
    ends={
        Property(name="wsmodel3_DeviceData", type=wsmodel3_Device, multiplicity=Multiplicity(1, 1)),
        Property(name="wsmodel3_Device25", type=wsmodel3_DeviceData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
port26: BinaryAssociation = BinaryAssociation(
    name="port26",
    ends={
        Property(name="wsmodel3_Port", type=wsmodel3_Controller, multiplicity=Multiplicity(1, 1)),
        Property(name="wsmodel3_Controller", type=wsmodel3_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
communication27: BinaryAssociation = BinaryAssociation(
    name="communication27",
    ends={
        Property(name="wsmodel3_Communication", type=wsmodel3_Controller, multiplicity=Multiplicity(1, 1)),
        Property(name="wsmodel3_Controller28", type=wsmodel3_Communication, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rest39: BinaryAssociation = BinaryAssociation(
    name="rest39",
    ends={
        Property(name="wsmodel3_REST40", type=wsmodel3_Bridge, multiplicity=Multiplicity(1, 1)),
        Property(name="wsmodel3_Bridge", type=wsmodel3_REST, multiplicity=Multiplicity(0, 1))
    }
)
actuator41: BinaryAssociation = BinaryAssociation(
    name="actuator41",
    ends={
        Property(name="wsmodel3_Actuator42", type=wsmodel3_InputBridge, multiplicity=Multiplicity(1, 1)),
        Property(name="wsmodel3_InputBridge", type=wsmodel3_Actuator, multiplicity=Multiplicity(0, 1))
    }
)
messagebroker34: BinaryAssociation = BinaryAssociation(
    name="messagebroker34",
    ends={
        Property(name="wsmodel3_MessageBroker36", type=wsmodel3_Communication, multiplicity=Multiplicity(1, 1)),
        Property(name="wsmodel3_Communication35", type=wsmodel3_MessageBroker, multiplicity=Multiplicity(0, 1))
    }
)
sensor37: BinaryAssociation = BinaryAssociation(
    name="sensor37",
    ends={
        Property(name="wsmodel3_Sensor", type=wsmodel3_InputPort, multiplicity=Multiplicity(1, 1)),
        Property(name="wsmodel3_InputPort", type=wsmodel3_Sensor, multiplicity=Multiplicity(1, 1))
    }
)
actuator38: BinaryAssociation = BinaryAssociation(
    name="actuator38",
    ends={
        Property(name="wsmodel3_Actuator", type=wsmodel3_OutputPort, multiplicity=Multiplicity(1, 1)),
        Property(name="wsmodel3_OutputPort", type=wsmodel3_Actuator, multiplicity=Multiplicity(1, 1))
    }
)
rest65: BinaryAssociation = BinaryAssociation(
    name="rest65",
    ends={
        Property(name="wsmodel3_REST67", type=wsmodel3_Orchestrator, multiplicity=Multiplicity(1, 1)),
        Property(name="wsmodel3_Orchestrator66", type=wsmodel3_REST, multiplicity=Multiplicity(0, 9999))
    }
)
inputorchestrator68: BinaryAssociation = BinaryAssociation(
    name="inputorchestrator68",
    ends={
        Property(name="wsmodel3_InputOrchestrator70", type=wsmodel3_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="wsmodel3_Function69", type=wsmodel3_InputOrchestrator, multiplicity=Multiplicity(1, 1))
    }
)
outputorchestrator71: BinaryAssociation = BinaryAssociation(
    name="outputorchestrator71",
    ends={
        Property(name="wsmodel3_OutputOrchestrator73", type=wsmodel3_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="wsmodel3_Function72", type=wsmodel3_OutputOrchestrator, multiplicity=Multiplicity(1, 1))
    }
)
break74: BinaryAssociation = BinaryAssociation(
    name="break74",
    ends={
        Property(name="wsmodel3_Break", type=wsmodel3_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="wsmodel3_Function75", type=wsmodel3_Break, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputorchestrator43: BinaryAssociation = BinaryAssociation(
    name="inputorchestrator43",
    ends={
        Property(name="wsmodel3_InputOrchestrator", type=wsmodel3_OutputBridge, multiplicity=Multiplicity(1, 1)),
        Property(name="wsmodel3_OutputBridge", type=wsmodel3_InputOrchestrator, multiplicity=Multiplicity(0, 9999))
    }
)
sensor44: BinaryAssociation = BinaryAssociation(
    name="sensor44",
    ends={
        Property(name="wsmodel3_Sensor46", type=wsmodel3_OutputBridge, multiplicity=Multiplicity(1, 1)),
        Property(name="wsmodel3_OutputBridge45", type=wsmodel3_Sensor, multiplicity=Multiplicity(0, 1))
    }
)
bridge47: BinaryAssociation = BinaryAssociation(
    name="bridge47",
    ends={
        Property(name="wsmodel3_Bridge49", type=wsmodel3_MessageBroker, multiplicity=Multiplicity(1, 1)),
        Property(name="wsmodel3_MessageBroker48", type=wsmodel3_Bridge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
orchestrator50: BinaryAssociation = BinaryAssociation(
    name="orchestrator50",
    ends={
        Property(name="wsmodel3_Orchestrator", type=wsmodel3_IntegrationPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="wsmodel3_IntegrationPattern51", type=wsmodel3_Orchestrator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
webserver52: BinaryAssociation = BinaryAssociation(
    name="webserver52",
    ends={
        Property(name="wsmodel3_WebServer54", type=wsmodel3_IntegrationPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="wsmodel3_IntegrationPattern53", type=wsmodel3_WebServer, multiplicity=Multiplicity(1, 1))
    }
)
inputorchestrator55: BinaryAssociation = BinaryAssociation(
    name="inputorchestrator55",
    ends={
        Property(name="wsmodel3_InputOrchestrator57", type=wsmodel3_Orchestrator, multiplicity=Multiplicity(1, 1)),
        Property(name="wsmodel3_Orchestrator56", type=wsmodel3_InputOrchestrator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
function58: BinaryAssociation = BinaryAssociation(
    name="function58",
    ends={
        Property(name="wsmodel3_Function", type=wsmodel3_Orchestrator, multiplicity=Multiplicity(1, 1)),
        Property(name="wsmodel3_Orchestrator59", type=wsmodel3_Function, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
outputorchestrator60: BinaryAssociation = BinaryAssociation(
    name="outputorchestrator60",
    ends={
        Property(name="wsmodel3_OutputOrchestrator", type=wsmodel3_Orchestrator, multiplicity=Multiplicity(1, 1)),
        Property(name="wsmodel3_Orchestrator61", type=wsmodel3_OutputOrchestrator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
externalapi62: BinaryAssociation = BinaryAssociation(
    name="externalapi62",
    ends={
        Property(name="wsmodel3_ExternalAPI64", type=wsmodel3_Orchestrator, multiplicity=Multiplicity(1, 1)),
        Property(name="wsmodel3_Orchestrator63", type=wsmodel3_ExternalAPI, multiplicity=Multiplicity(0, 9999))
    }
)
inputorchestrator76: BinaryAssociation = BinaryAssociation(
    name="inputorchestrator76",
    ends={
        Property(name="wsmodel3_InputOrchestrator78", type=wsmodel3_OutputOrchestrator, multiplicity=Multiplicity(1, 1)),
        Property(name="wsmodel3_OutputOrchestrator77", type=wsmodel3_InputOrchestrator, multiplicity=Multiplicity(0, 9999))
    }
)
inputbridge79: BinaryAssociation = BinaryAssociation(
    name="inputbridge79",
    ends={
        Property(name="wsmodel3_InputBridge81", type=wsmodel3_OutputOrchestrator, multiplicity=Multiplicity(1, 1)),
        Property(name="wsmodel3_OutputOrchestrator80", type=wsmodel3_InputBridge, multiplicity=Multiplicity(0, 1))
    }
)
renponsedata82: BinaryAssociation = BinaryAssociation(
    name="renponsedata82",
    ends={
        Property(name="wsmodel3_OrchestratorData", type=wsmodel3_OutputOrchestrator, multiplicity=Multiplicity(1, 1)),
        Property(name="wsmodel3_OutputOrchestrator83", type=wsmodel3_OrchestratorData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rest84: BinaryAssociation = BinaryAssociation(
    name="rest84",
    ends={
        Property(name="wsmodel3_REST86", type=wsmodel3_OutputOrchestrator, multiplicity=Multiplicity(1, 1)),
        Property(name="wsmodel3_OutputOrchestrator85", type=wsmodel3_REST, multiplicity=Multiplicity(0, 9999))
    }
)
externalapi87: BinaryAssociation = BinaryAssociation(
    name="externalapi87",
    ends={
        Property(name="wsmodel3_ExternalAPI89", type=wsmodel3_OutputOrchestrator, multiplicity=Multiplicity(1, 1)),
        Property(name="wsmodel3_OutputOrchestrator88", type=wsmodel3_ExternalAPI, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_wsmodel3_WebServer_Server = Generalization(general=Server, specific=wsmodel3_WebServer)
gen_wsmodel3_DBServer_Server = Generalization(general=Server, specific=wsmodel3_DBServer)
gen_wsmodel3_Sensor_Device = Generalization(general=Device, specific=wsmodel3_Sensor)
gen_wsmodel3_Actuator_Device = Generalization(general=Device, specific=wsmodel3_Actuator)
gen_wsmodel3_Controller_Device = Generalization(general=Device, specific=wsmodel3_Controller)
gen_wsmodel3_InputBridge_Bridge = Generalization(general=Bridge, specific=wsmodel3_InputBridge)
gen_wsmodel3_OutputBridge_Bridge = Generalization(general=Bridge, specific=wsmodel3_OutputBridge)
gen_wsmodel3_InputPort_Port = Generalization(general=Port, specific=wsmodel3_InputPort)
gen_wsmodel3_OutputPort_Port = Generalization(general=Port, specific=wsmodel3_OutputPort)
gen_wsmodel3_DeviceData_Data = Generalization(general=Data, specific=wsmodel3_DeviceData)
gen_wsmodel3_CommunicationData_Data = Generalization(general=Data, specific=wsmodel3_CommunicationData)
gen_wsmodel3_OrchestratorData_Data = Generalization(general=Data, specific=wsmodel3_OrchestratorData)

# Domain Model
domain_model = DomainModel(
    name="wsmodel3",
    types={wsmodel3_System, Server, wsmodel3_WebService, wsmodel3_Server, wsmodel3_IoTNode, wsmodel3_AccesPoint, wsmodel3_IntegrationPattern, wsmodel3_MessageBroker, wsmodel3_ExternalAPI, wsmodel3_Device, wsmodel3_REST, wsmodel3_WebServer, wsmodel3_DBServer, wsmodel3_CommunicationData, wsmodel3_DeviceData, wsmodel3_Sensor, Device, wsmodel3_Actuator, wsmodel3_Controller, wsmodel3_Port, wsmodel3_Communication, wsmodel3_InputBridge, Bridge, wsmodel3_OutputBridge, wsmodel3_InputPort, Port, wsmodel3_OutputPort, Data, wsmodel3_Data, wsmodel3_Bridge, wsmodel3_Break, wsmodel3_InputOrchestrator, wsmodel3_Orchestrator, wsmodel3_Function, wsmodel3_OutputOrchestrator, wsmodel3_OrchestratorData, ControllerType, DBType, SensorType, ActuatorType, PortType, CommunicationType, MessageBrokerType},
    associations={device21, webservice0, server1, iotnode3, accespoint5, integrationpattern7, messagebroker9, externalapi11, device13, rest15, webserver17, dbserver19, communicationdata29, accespoint31, devicedata24, port26, communication27, rest39, actuator41, messagebroker34, sensor37, actuator38, rest65, inputorchestrator68, outputorchestrator71, break74, inputorchestrator43, sensor44, bridge47, orchestrator50, webserver52, inputorchestrator55, function58, outputorchestrator60, externalapi62, inputorchestrator76, inputbridge79, renponsedata82, rest84, externalapi87},
    generalizations={gen_wsmodel3_WebServer_Server, gen_wsmodel3_DBServer_Server, gen_wsmodel3_Sensor_Device, gen_wsmodel3_Actuator_Device, gen_wsmodel3_Controller_Device, gen_wsmodel3_InputBridge_Bridge, gen_wsmodel3_OutputBridge_Bridge, gen_wsmodel3_InputPort_Port, gen_wsmodel3_OutputPort_Port, gen_wsmodel3_DeviceData_Data, gen_wsmodel3_CommunicationData_Data, gen_wsmodel3_OrchestratorData_Data},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)