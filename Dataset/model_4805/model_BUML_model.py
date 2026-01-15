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
Environment: Enumeration = Enumeration(
    name="Environment",
    literals={
            EnumerationLiteral(name="KUBERNETES"),
			EnumerationLiteral(name="DOCKER_SWARM")
    }
)

# Classes
model_StringToHost = Class(name="model::StringToHost")
model_Cluster = Class(name="model::Cluster")
model_StringToApplication = Class(name="model::StringToApplication")
model_Service = Class(name="model::Service", is_abstract=True)
model_Affinity = Class(name="model::Affinity")
model_ServiceInstance = Class(name="model::ServiceInstance")
Service = Class(name="Service")
ElementWithResources = Class(name="ElementWithResources")
model_Message = Class(name="model::Message")
model_Host = Class(name="model::Host")
model_StringToServiceInstance = Class(name="model::StringToServiceInstance")
model_StringToDoubleMap = Class(name="model::StringToDoubleMap")
model_ElementWithResources = Class(name="model::ElementWithResources", is_abstract=True)
model_StringToService = Class(name="model::StringToService")
model_Application = Class(name="model::Application")

# model_StringToHost class attributes and methods
model_StringToHost_key: Property = Property(name="key", type=StringType)
model_StringToHost.attributes={model_StringToHost_key}

# model_Cluster class attributes and methods
model_Cluster_environment: Property = Property(name="environment", type=StringType)
model_Cluster_m_move: Method = Method(name="move", parameters={Parameter(name='sourceHost'), Parameter(name='serviceId'), Parameter(name='destinationHost'), Parameter(name='application')})
model_Cluster.attributes={model_Cluster_environment}
model_Cluster.methods={model_Cluster_m_move}

# model_StringToApplication class attributes and methods
model_StringToApplication_key: Property = Property(name="key", type=StringType)
model_StringToApplication.attributes={model_StringToApplication_key}

# model_Service class attributes and methods
model_Service_name: Property = Property(name="name", type=StringType)
model_Service_application: Property = Property(name="application", type=StringType)
model_Service_stateful: Property = Property(name="stateful", type=StringType)
model_Service.attributes={model_Service_stateful, model_Service_name, model_Service_application}

# model_Affinity class attributes and methods
model_Affinity_degree: Property = Property(name="degree", type=StringType)
model_Affinity.attributes={model_Affinity_degree}

# model_ServiceInstance class attributes and methods
model_ServiceInstance_id: Property = Property(name="id", type=StringType)
model_ServiceInstance_address: Property = Property(name="address", type=StringType)
model_ServiceInstance_containers: Property = Property(name="containers", type=StringType)
model_ServiceInstance_totalMessages: Property = Property(name="totalMessages", type=StringType)
model_ServiceInstance_totalData: Property = Property(name="totalData", type=StringType)
model_ServiceInstance.attributes={model_ServiceInstance_totalData, model_ServiceInstance_containers, model_ServiceInstance_address, model_ServiceInstance_id, model_ServiceInstance_totalMessages}

# Service class attributes and methods

# ElementWithResources class attributes and methods

# model_Message class attributes and methods
model_Message_name: Property = Property(name="name", type=StringType)
model_Message_avgResponseTime: Property = Property(name="avgResponseTime", type=StringType)
model_Message_timestamp: Property = Property(name="timestamp", type=StringType)
model_Message_uid: Property = Property(name="uid", type=StringType)
model_Message_messageSize: Property = Property(name="messageSize", type=StringType)
model_Message.attributes={model_Message_name, model_Message_messageSize, model_Message_timestamp, model_Message_avgResponseTime, model_Message_uid}

# model_Host class attributes and methods
model_Host_hostAddress: Property = Property(name="hostAddress", type=StringType)
model_Host_name: Property = Property(name="name", type=StringType)
model_Host_cores: Property = Property(name="cores", type=StringType)
model_Host.attributes={model_Host_name, model_Host_hostAddress, model_Host_cores}

# model_StringToServiceInstance class attributes and methods
model_StringToServiceInstance_key: Property = Property(name="key", type=StringType)
model_StringToServiceInstance.attributes={model_StringToServiceInstance_key}

# model_StringToDoubleMap class attributes and methods
model_StringToDoubleMap_key: Property = Property(name="key", type=StringType)
model_StringToDoubleMap_value: Property = Property(name="value", type=StringType)
model_StringToDoubleMap.attributes={model_StringToDoubleMap_key, model_StringToDoubleMap_value}

# model_ElementWithResources class attributes and methods

# model_StringToService class attributes and methods
model_StringToService_key: Property = Property(name="key", type=StringType)
model_StringToService.attributes={model_StringToService_key}

# model_Application class attributes and methods
model_Application_name: Property = Property(name="name", type=StringType)
model_Application_totalMessages: Property = Property(name="totalMessages", type=StringType)
model_Application_totalData: Property = Property(name="totalData", type=StringType)
model_Application_weight: Property = Property(name="weight", type=StringType)
model_Application.attributes={model_Application_name, model_Application_weight, model_Application_totalData, model_Application_totalMessages}

# Relationships
hosts0: BinaryAssociation = BinaryAssociation(
    name="hosts0",
    ends={
        Property(name="model_StringToHost", type=model_Cluster, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Cluster", type=model_StringToHost, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
applications1: BinaryAssociation = BinaryAssociation(
    name="applications1",
    ends={
        Property(name="model_StringToApplication", type=model_Cluster, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Cluster2", type=model_StringToApplication, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hasAffinities3: BinaryAssociation = BinaryAssociation(
    name="hasAffinities3",
    ends={
        Property(name="model_Affinity", type=model_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Service", type=model_Affinity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
with4: BinaryAssociation = BinaryAssociation(
    name="with4",
    ends={
        Property(name="model_Service6", type=model_Affinity, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Affinity5", type=model_Service, multiplicity=Multiplicity(0, 1))
    }
)
messages7: BinaryAssociation = BinaryAssociation(
    name="messages7",
    ends={
        Property(name="model_Message", type=model_ServiceInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ServiceInstance", type=model_Message, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
host8: BinaryAssociation = BinaryAssociation(
    name="host8",
    ends={
        Property(name="model_Host", type=model_ServiceInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ServiceInstance9", type=model_Host, multiplicity=Multiplicity(0, 1))
    }
)
source10: BinaryAssociation = BinaryAssociation(
    name="source10",
    ends={
        Property(name="model_ServiceInstance12", type=model_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Message11", type=model_ServiceInstance, multiplicity=Multiplicity(0, 1))
    }
)
destination13: BinaryAssociation = BinaryAssociation(
    name="destination13",
    ends={
        Property(name="model_ServiceInstance15", type=model_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Message14", type=model_ServiceInstance, multiplicity=Multiplicity(0, 1))
    }
)
services16: BinaryAssociation = BinaryAssociation(
    name="services16",
    ends={
        Property(name="model_StringToServiceInstance", type=model_Host, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Host17", type=model_StringToServiceInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceReserved18: BinaryAssociation = BinaryAssociation(
    name="resourceReserved18",
    ends={
        Property(name="model_StringToDoubleMap", type=model_Host, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Host19", type=model_StringToDoubleMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceLimit20: BinaryAssociation = BinaryAssociation(
    name="resourceLimit20",
    ends={
        Property(name="model_StringToDoubleMap21", type=model_ElementWithResources, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ElementWithResources", type=model_StringToDoubleMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metrics22: BinaryAssociation = BinaryAssociation(
    name="metrics22",
    ends={
        Property(name="model_StringToDoubleMap24", type=model_ElementWithResources, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ElementWithResources23", type=model_StringToDoubleMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value25: BinaryAssociation = BinaryAssociation(
    name="value25",
    ends={
        Property(name="model_Service26", type=model_StringToService, multiplicity=Multiplicity(1, 1)),
        Property(name="model_StringToService", type=model_Service, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value27: BinaryAssociation = BinaryAssociation(
    name="value27",
    ends={
        Property(name="model_Host29", type=model_StringToHost, multiplicity=Multiplicity(1, 1)),
        Property(name="model_StringToHost28", type=model_Host, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value30: BinaryAssociation = BinaryAssociation(
    name="value30",
    ends={
        Property(name="model_ServiceInstance32", type=model_StringToServiceInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="model_StringToServiceInstance31", type=model_ServiceInstance, multiplicity=Multiplicity(0, 1))
    }
)
services33: BinaryAssociation = BinaryAssociation(
    name="services33",
    ends={
        Property(name="model_StringToService34", type=model_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Application", type=model_StringToService, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value35: BinaryAssociation = BinaryAssociation(
    name="value35",
    ends={
        Property(name="model_Application37", type=model_StringToApplication, multiplicity=Multiplicity(1, 1)),
        Property(name="model_StringToApplication36", type=model_Application, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_model_ServiceInstance_Service = Generalization(general=Service, specific=model_ServiceInstance)
gen_model_ServiceInstance_ElementWithResources = Generalization(general=ElementWithResources, specific=model_ServiceInstance)
gen_model_Host_ElementWithResources = Generalization(general=ElementWithResources, specific=model_Host)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_StringToHost, model_Cluster, model_StringToApplication, model_Service, model_Affinity, model_ServiceInstance, Service, ElementWithResources, model_Message, model_Host, model_StringToServiceInstance, model_StringToDoubleMap, model_ElementWithResources, model_StringToService, model_Application, Environment},
    associations={hosts0, applications1, hasAffinities3, with4, messages7, host8, source10, destination13, services16, resourceReserved18, resourceLimit20, metrics22, value25, value27, value30, services33, value35},
    generalizations={gen_model_ServiceInstance_Service, gen_model_ServiceInstance_ElementWithResources, gen_model_Host_ElementWithResources},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)