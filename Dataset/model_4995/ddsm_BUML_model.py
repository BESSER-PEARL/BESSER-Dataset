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
VMSize: Enumeration = Enumeration(
    name="VMSize",
    literals={
            EnumerationLiteral(name="Small"),
			EnumerationLiteral(name="Medium"),
			EnumerationLiteral(name="Large")
    }
)

ProviderType: Enumeration = Enumeration(
    name="ProviderType",
    literals={
            EnumerationLiteral(name="Flexiant"),
			EnumerationLiteral(name="Openstack")
    }
)

# Classes
ddsm_CloudElement = Class(name="ddsm::CloudElement", is_abstract=True)
ddsm_Resource = Class(name="ddsm::Resource")
ddsm_Component = Class(name="ddsm::Component", is_abstract=True)
CloudElement = Class(name="CloudElement")
ddsm_ProvidedPort = Class(name="ddsm::ProvidedPort")
ddsm_ProvidedExecutionPlatform = Class(name="ddsm::ProvidedExecutionPlatform")
ddsm_InternalComponent = Class(name="ddsm::InternalComponent")
Component = Class(name="Component")
ddsm_RequiredPort = Class(name="ddsm::RequiredPort")
ddsm_RequiredExecutionPlatform = Class(name="ddsm::RequiredExecutionPlatform")
ddsm_ExecutionPlatform = Class(name="ddsm::ExecutionPlatform", is_abstract=True)
ddsm_Port = Class(name="ddsm::Port", is_abstract=True)
Port = Class(name="Port")
ddsm_Property = Class(name="ddsm::Property")
ddsm_Relationship = Class(name="ddsm::Relationship")
ddsm_ExecutionBinding = Class(name="ddsm::ExecutionBinding")
ddsm_ExternalComponent = Class(name="ddsm::ExternalComponent")
ddsm_Provider = Class(name="ddsm::Provider")
ddsm_VM = Class(name="ddsm::VM")
ExternalComponent = Class(name="ExternalComponent")
ExecutionPlatform = Class(name="ExecutionPlatform")
ddsm_DDSM = Class(name="ddsm::DDSM")
ddsm_StormSupervisor = Class(name="ddsm::StormSupervisor")
InternalComponent = Class(name="InternalComponent")
ddsm_StormNimbus = Class(name="ddsm::StormNimbus")
ddsm_Zookeeper = Class(name="ddsm::Zookeeper")
ddsm_Cluster = Class(name="ddsm::Cluster")
ddsm_ClientNode = Class(name="ddsm::ClientNode")
ddsm_YarnResourceManager = Class(name="ddsm::YarnResourceManager")
ddsm_YarnNodeManager = Class(name="ddsm::YarnNodeManager")
ddsm_HDFSNameNode = Class(name="ddsm::HDFSNameNode")
ddsm_HDFSDataNode = Class(name="ddsm::HDFSDataNode")
ddsm_ChefResource = Class(name="ddsm::ChefResource")
Resource = Class(name="Resource")
ddsm_StormCluster = Class(name="ddsm::StormCluster")
Cluster = Class(name="Cluster")
ddsm_Kafka = Class(name="ddsm::Kafka")

# ddsm_CloudElement class attributes and methods
ddsm_CloudElement_elementId: Property = Property(name="elementId", type=StringType)
ddsm_CloudElement_description: Property = Property(name="description", type=StringType)
ddsm_CloudElement.attributes={ddsm_CloudElement_description, ddsm_CloudElement_elementId}

# ddsm_Resource class attributes and methods
ddsm_Resource_downloadCommand: Property = Property(name="downloadCommand", type=StringType)
ddsm_Resource_createCommand: Property = Property(name="createCommand", type=StringType)
ddsm_Resource_configureCommand: Property = Property(name="configureCommand", type=StringType)
ddsm_Resource_installCommand: Property = Property(name="installCommand", type=StringType)
ddsm_Resource_startCommand: Property = Property(name="startCommand", type=StringType)
ddsm_Resource_stopCommand: Property = Property(name="stopCommand", type=StringType)
ddsm_Resource_resourceId: Property = Property(name="resourceId", type=StringType)
ddsm_Resource.attributes={ddsm_Resource_createCommand, ddsm_Resource_startCommand, ddsm_Resource_resourceId, ddsm_Resource_stopCommand, ddsm_Resource_configureCommand, ddsm_Resource_installCommand, ddsm_Resource_downloadCommand}

# ddsm_Component class attributes and methods

# CloudElement class attributes and methods

# ddsm_ProvidedPort class attributes and methods

# ddsm_ProvidedExecutionPlatform class attributes and methods

# ddsm_InternalComponent class attributes and methods

# Component class attributes and methods

# ddsm_RequiredPort class attributes and methods
ddsm_RequiredPort_isMandatory: Property = Property(name="isMandatory", type=BooleanType)
ddsm_RequiredPort.attributes={ddsm_RequiredPort_isMandatory}

# ddsm_RequiredExecutionPlatform class attributes and methods
ddsm_RequiredExecutionPlatform_isMandatory: Property = Property(name="isMandatory", type=BooleanType)
ddsm_RequiredExecutionPlatform.attributes={ddsm_RequiredExecutionPlatform_isMandatory}

# ddsm_ExecutionPlatform class attributes and methods

# ddsm_Port class attributes and methods
ddsm_Port_isLocal: Property = Property(name="isLocal", type=BooleanType)
ddsm_Port_portNumber: Property = Property(name="portNumber", type=StringType)
ddsm_Port.attributes={ddsm_Port_isLocal, ddsm_Port_portNumber}

# Port class attributes and methods

# ddsm_Property class attributes and methods
ddsm_Property_propertyId: Property = Property(name="propertyId", type=StringType)
ddsm_Property_value: Property = Property(name="value", type=StringType)
ddsm_Property.attributes={ddsm_Property_value, ddsm_Property_propertyId}

# ddsm_Relationship class attributes and methods

# ddsm_ExecutionBinding class attributes and methods

# ddsm_ExternalComponent class attributes and methods
ddsm_ExternalComponent_location: Property = Property(name="location", type=StringType)
ddsm_ExternalComponent_login: Property = Property(name="login", type=StringType)
ddsm_ExternalComponent_password: Property = Property(name="password", type=StringType)
ddsm_ExternalComponent_region: Property = Property(name="region", type=StringType)
ddsm_ExternalComponent_serviceType: Property = Property(name="serviceType", type=StringType)
ddsm_ExternalComponent.attributes={ddsm_ExternalComponent_login, ddsm_ExternalComponent_region, ddsm_ExternalComponent_serviceType, ddsm_ExternalComponent_location, ddsm_ExternalComponent_password}

# ddsm_Provider class attributes and methods
ddsm_Provider_credentialsPath: Property = Property(name="credentialsPath", type=StringType)
ddsm_Provider_type: Property = Property(name="type", type=StringType)
ddsm_Provider.attributes={ddsm_Provider_credentialsPath, ddsm_Provider_type}

# ddsm_VM class attributes and methods
ddsm_VM_is64os: Property = Property(name="is64os", type=StringType)
ddsm_VM_imageId: Property = Property(name="imageId", type=StringType)
ddsm_VM_maxCores: Property = Property(name="maxCores", type=StringType)
ddsm_VM_publicPorts: Property = Property(name="publicPorts", type=StringType)
ddsm_VM_maxRam: Property = Property(name="maxRam", type=StringType)
ddsm_VM_maxStorage: Property = Property(name="maxStorage", type=StringType)
ddsm_VM_minCores: Property = Property(name="minCores", type=StringType)
ddsm_VM_minRam: Property = Property(name="minRam", type=StringType)
ddsm_VM_minStorage: Property = Property(name="minStorage", type=StringType)
ddsm_VM_os: Property = Property(name="os", type=StringType)
ddsm_VM_privateKey: Property = Property(name="privateKey", type=StringType)
ddsm_VM_providerSpecificTypeName: Property = Property(name="providerSpecificTypeName", type=StringType)
ddsm_VM_securityGroup: Property = Property(name="securityGroup", type=StringType)
ddsm_VM_sshKey: Property = Property(name="sshKey", type=StringType)
ddsm_VM_publicAddress: Property = Property(name="publicAddress", type=StringType)
ddsm_VM_instances: Property = Property(name="instances", type=StringType)
ddsm_VM_genericSize: Property = Property(name="genericSize", type=StringType)
ddsm_VM.attributes={ddsm_VM_providerSpecificTypeName, ddsm_VM_publicPorts, ddsm_VM_imageId, ddsm_VM_maxStorage, ddsm_VM_os, ddsm_VM_minRam, ddsm_VM_minCores, ddsm_VM_minStorage, ddsm_VM_privateKey, ddsm_VM_instances, ddsm_VM_genericSize, ddsm_VM_sshKey, ddsm_VM_securityGroup, ddsm_VM_is64os, ddsm_VM_publicAddress, ddsm_VM_maxCores, ddsm_VM_maxRam}

# ExternalComponent class attributes and methods

# ExecutionPlatform class attributes and methods

# ddsm_DDSM class attributes and methods
ddsm_DDSM_modelId: Property = Property(name="modelId", type=StringType)
ddsm_DDSM_description: Property = Property(name="description", type=StringType)
ddsm_DDSM.attributes={ddsm_DDSM_modelId, ddsm_DDSM_description}

# ddsm_StormSupervisor class attributes and methods
ddsm_StormSupervisor_workerStartTimeout: Property = Property(name="workerStartTimeout", type=StringType)
ddsm_StormSupervisor_cpuCapacity: Property = Property(name="cpuCapacity", type=StringType)
ddsm_StormSupervisor_memoryCapacity: Property = Property(name="memoryCapacity", type=StringType)
ddsm_StormSupervisor_heartbeatFrequency: Property = Property(name="heartbeatFrequency", type=StringType)
ddsm_StormSupervisor.attributes={ddsm_StormSupervisor_memoryCapacity, ddsm_StormSupervisor_workerStartTimeout, ddsm_StormSupervisor_cpuCapacity, ddsm_StormSupervisor_heartbeatFrequency}

# InternalComponent class attributes and methods

# ddsm_StormNimbus class attributes and methods
ddsm_StormNimbus_taskTimeout: Property = Property(name="taskTimeout", type=StringType)
ddsm_StormNimbus_supervisorTimeout: Property = Property(name="supervisorTimeout", type=StringType)
ddsm_StormNimbus_monitorFrequency: Property = Property(name="monitorFrequency", type=StringType)
ddsm_StormNimbus_queueSize: Property = Property(name="queueSize", type=StringType)
ddsm_StormNimbus_retryTimes: Property = Property(name="retryTimes", type=StringType)
ddsm_StormNimbus_retryInterval: Property = Property(name="retryInterval", type=StringType)
ddsm_StormNimbus.attributes={ddsm_StormNimbus_supervisorTimeout, ddsm_StormNimbus_taskTimeout, ddsm_StormNimbus_retryTimes, ddsm_StormNimbus_retryInterval, ddsm_StormNimbus_queueSize, ddsm_StormNimbus_monitorFrequency}

# ddsm_Zookeeper class attributes and methods
ddsm_Zookeeper_tickTime: Property = Property(name="tickTime", type=StringType)
ddsm_Zookeeper_initLimit: Property = Property(name="initLimit", type=StringType)
ddsm_Zookeeper_syncLimit: Property = Property(name="syncLimit", type=StringType)
ddsm_Zookeeper.attributes={ddsm_Zookeeper_tickTime, ddsm_Zookeeper_initLimit, ddsm_Zookeeper_syncLimit}

# ddsm_Cluster class attributes and methods

# ddsm_ClientNode class attributes and methods
ddsm_ClientNode_type: Property = Property(name="type", type=StringType)
ddsm_ClientNode_artifactUrl: Property = Property(name="artifactUrl", type=StringType)
ddsm_ClientNode_mainClass: Property = Property(name="mainClass", type=StringType)
ddsm_ClientNode.attributes={ddsm_ClientNode_type, ddsm_ClientNode_mainClass, ddsm_ClientNode_artifactUrl}

# ddsm_YarnResourceManager class attributes and methods

# ddsm_YarnNodeManager class attributes and methods

# ddsm_HDFSNameNode class attributes and methods

# ddsm_HDFSDataNode class attributes and methods

# ddsm_ChefResource class attributes and methods
ddsm_ChefResource_cookbookId: Property = Property(name="cookbookId", type=StringType)
ddsm_ChefResource.attributes={ddsm_ChefResource_cookbookId}

# Resource class attributes and methods

# ddsm_StormCluster class attributes and methods
ddsm_StormCluster_number_of_workers: Property = Property(name="number_of_workers", type=StringType)
ddsm_StormCluster.attributes={ddsm_StormCluster_number_of_workers}

# Cluster class attributes and methods

# ddsm_Kafka class attributes and methods

# Relationships
resource0: BinaryAssociation = BinaryAssociation(
    name="resource0",
    ends={
        Property(name="ddsm_Resource", type=ddsm_CloudElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsm_CloudElement", type=ddsm_Resource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedport3: BinaryAssociation = BinaryAssociation(
    name="providedport3",
    ends={
        Property(name="ddsm_ProvidedPort", type=ddsm_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsm_Component", type=ddsm_ProvidedPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedexecutionplatform4: BinaryAssociation = BinaryAssociation(
    name="providedexecutionplatform4",
    ends={
        Property(name="ddsm_ProvidedExecutionPlatform", type=ddsm_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsm_Component5", type=ddsm_ProvidedExecutionPlatform, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredport6: BinaryAssociation = BinaryAssociation(
    name="requiredport6",
    ends={
        Property(name="ddsm_RequiredPort", type=ddsm_InternalComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsm_InternalComponent", type=ddsm_RequiredPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
internalcomponent8: BinaryAssociation = BinaryAssociation(
    name="internalcomponent8",
    ends={
        Property(name="ddsm_InternalComponent9", type=ddsm_InternalComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsm_InternalComponent7", type=ddsm_InternalComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredexecutionplatform10: BinaryAssociation = BinaryAssociation(
    name="requiredexecutionplatform10",
    ends={
        Property(name="ddsm_RequiredExecutionPlatform", type=ddsm_InternalComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsm_InternalComponent11", type=ddsm_RequiredExecutionPlatform, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
property1: BinaryAssociation = BinaryAssociation(
    name="property1",
    ends={
        Property(name="ddsm_Property", type=ddsm_CloudElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsm_CloudElement2", type=ddsm_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner15: BinaryAssociation = BinaryAssociation(
    name="owner15",
    ends={
        Property(name="ddsm_Component17", type=ddsm_ProvidedExecutionPlatform, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsm_ProvidedExecutionPlatform16", type=ddsm_Component, multiplicity=Multiplicity(1, 1))
    }
)
providedport18: BinaryAssociation = BinaryAssociation(
    name="providedport18",
    ends={
        Property(name="ddsm_ProvidedPort19", type=ddsm_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsm_Relationship", type=ddsm_ProvidedPort, multiplicity=Multiplicity(0, 1))
    }
)
requiredport20: BinaryAssociation = BinaryAssociation(
    name="requiredport20",
    ends={
        Property(name="ddsm_RequiredPort22", type=ddsm_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsm_Relationship21", type=ddsm_RequiredPort, multiplicity=Multiplicity(0, 1))
    }
)
requiredexecutionplatform23: BinaryAssociation = BinaryAssociation(
    name="requiredexecutionplatform23",
    ends={
        Property(name="ddsm_RequiredExecutionPlatform24", type=ddsm_ExecutionBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsm_ExecutionBinding", type=ddsm_RequiredExecutionPlatform, multiplicity=Multiplicity(0, 1))
    }
)
providedexecutionplatform25: BinaryAssociation = BinaryAssociation(
    name="providedexecutionplatform25",
    ends={
        Property(name="ddsm_ProvidedExecutionPlatform27", type=ddsm_ExecutionBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsm_ExecutionBinding26", type=ddsm_ProvidedExecutionPlatform, multiplicity=Multiplicity(0, 1))
    }
)
provider28: BinaryAssociation = BinaryAssociation(
    name="provider28",
    ends={
        Property(name="ddsm_Provider", type=ddsm_ExternalComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsm_ExternalComponent", type=ddsm_Provider, multiplicity=Multiplicity(1, 1))
    }
)
owner12: BinaryAssociation = BinaryAssociation(
    name="owner12",
    ends={
        Property(name="ddsm_Component14", type=ddsm_ProvidedPort, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsm_ProvidedPort13", type=ddsm_Component, multiplicity=Multiplicity(1, 1))
    }
)
cloudelement29: BinaryAssociation = BinaryAssociation(
    name="cloudelement29",
    ends={
        Property(name="ddsm_CloudElement30", type=ddsm_DDSM, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsm_DDSM", type=ddsm_CloudElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties31: BinaryAssociation = BinaryAssociation(
    name="properties31",
    ends={
        Property(name="ddsm_Property33", type=ddsm_DDSM, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsm_DDSM32", type=ddsm_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resources34: BinaryAssociation = BinaryAssociation(
    name="resources34",
    ends={
        Property(name="ddsm_Resource36", type=ddsm_DDSM, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsm_DDSM35", type=ddsm_Resource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hasVm37: BinaryAssociation = BinaryAssociation(
    name="hasVm37",
    ends={
        Property(name="ddsm_VM", type=ddsm_Cluster, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsm_Cluster", type=ddsm_VM, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_ddsm_Component_CloudElement = Generalization(general=CloudElement, specific=ddsm_Component)
gen_ddsm_InternalComponent_Component = Generalization(general=Component, specific=ddsm_InternalComponent)
gen_ddsm_ExecutionPlatform_CloudElement = Generalization(general=CloudElement, specific=ddsm_ExecutionPlatform)
gen_ddsm_Port_CloudElement = Generalization(general=CloudElement, specific=ddsm_Port)
gen_ddsm_RequiredPort_Port = Generalization(general=Port, specific=ddsm_RequiredPort)
gen_ddsm_ProvidedPort_Port = Generalization(general=Port, specific=ddsm_ProvidedPort)
gen_ddsm_Relationship_CloudElement = Generalization(general=CloudElement, specific=ddsm_Relationship)
gen_ddsm_ExecutionBinding_CloudElement = Generalization(general=CloudElement, specific=ddsm_ExecutionBinding)
gen_ddsm_ExternalComponent_Component = Generalization(general=Component, specific=ddsm_ExternalComponent)
gen_ddsm_Provider_CloudElement = Generalization(general=CloudElement, specific=ddsm_Provider)
gen_ddsm_VM_ExternalComponent = Generalization(general=ExternalComponent, specific=ddsm_VM)
gen_ddsm_RequiredExecutionPlatform_ExecutionPlatform = Generalization(general=ExecutionPlatform, specific=ddsm_RequiredExecutionPlatform)
gen_ddsm_ProvidedExecutionPlatform_ExecutionPlatform = Generalization(general=ExecutionPlatform, specific=ddsm_ProvidedExecutionPlatform)
gen_ddsm_StormSupervisor_InternalComponent = Generalization(general=InternalComponent, specific=ddsm_StormSupervisor)
gen_ddsm_StormNimbus_InternalComponent = Generalization(general=InternalComponent, specific=ddsm_StormNimbus)
gen_ddsm_Zookeeper_InternalComponent = Generalization(general=InternalComponent, specific=ddsm_Zookeeper)
gen_ddsm_Cluster_ExternalComponent = Generalization(general=ExternalComponent, specific=ddsm_Cluster)
gen_ddsm_ClientNode_InternalComponent = Generalization(general=InternalComponent, specific=ddsm_ClientNode)
gen_ddsm_YarnResourceManager_InternalComponent = Generalization(general=InternalComponent, specific=ddsm_YarnResourceManager)
gen_ddsm_YarnNodeManager_InternalComponent = Generalization(general=InternalComponent, specific=ddsm_YarnNodeManager)
gen_ddsm_HDFSNameNode_InternalComponent = Generalization(general=InternalComponent, specific=ddsm_HDFSNameNode)
gen_ddsm_HDFSDataNode_InternalComponent = Generalization(general=InternalComponent, specific=ddsm_HDFSDataNode)
gen_ddsm_ChefResource_Resource = Generalization(general=Resource, specific=ddsm_ChefResource)
gen_ddsm_StormCluster_Cluster = Generalization(general=Cluster, specific=ddsm_StormCluster)
gen_ddsm_Kafka_InternalComponent = Generalization(general=InternalComponent, specific=ddsm_Kafka)

# Domain Model
domain_model = DomainModel(
    name="ddsm",
    types={ddsm_CloudElement, ddsm_Resource, ddsm_Component, CloudElement, ddsm_ProvidedPort, ddsm_ProvidedExecutionPlatform, ddsm_InternalComponent, Component, ddsm_RequiredPort, ddsm_RequiredExecutionPlatform, ddsm_ExecutionPlatform, ddsm_Port, Port, ddsm_Property, ddsm_Relationship, ddsm_ExecutionBinding, ddsm_ExternalComponent, ddsm_Provider, ddsm_VM, ExternalComponent, ExecutionPlatform, ddsm_DDSM, ddsm_StormSupervisor, InternalComponent, ddsm_StormNimbus, ddsm_Zookeeper, ddsm_Cluster, ddsm_ClientNode, ddsm_YarnResourceManager, ddsm_YarnNodeManager, ddsm_HDFSNameNode, ddsm_HDFSDataNode, ddsm_ChefResource, Resource, ddsm_StormCluster, Cluster, ddsm_Kafka, VMSize, ProviderType},
    associations={resource0, providedport3, providedexecutionplatform4, requiredport6, internalcomponent8, requiredexecutionplatform10, property1, owner15, providedport18, requiredport20, requiredexecutionplatform23, providedexecutionplatform25, provider28, owner12, cloudelement29, properties31, resources34, hasVm37},
    generalizations={gen_ddsm_Component_CloudElement, gen_ddsm_InternalComponent_Component, gen_ddsm_ExecutionPlatform_CloudElement, gen_ddsm_Port_CloudElement, gen_ddsm_RequiredPort_Port, gen_ddsm_ProvidedPort_Port, gen_ddsm_Relationship_CloudElement, gen_ddsm_ExecutionBinding_CloudElement, gen_ddsm_ExternalComponent_Component, gen_ddsm_Provider_CloudElement, gen_ddsm_VM_ExternalComponent, gen_ddsm_RequiredExecutionPlatform_ExecutionPlatform, gen_ddsm_ProvidedExecutionPlatform_ExecutionPlatform, gen_ddsm_StormSupervisor_InternalComponent, gen_ddsm_StormNimbus_InternalComponent, gen_ddsm_Zookeeper_InternalComponent, gen_ddsm_Cluster_ExternalComponent, gen_ddsm_ClientNode_InternalComponent, gen_ddsm_YarnResourceManager_InternalComponent, gen_ddsm_YarnNodeManager_InternalComponent, gen_ddsm_HDFSNameNode_InternalComponent, gen_ddsm_HDFSDataNode_InternalComponent, gen_ddsm_ChefResource_Resource, gen_ddsm_StormCluster_Cluster, gen_ddsm_Kafka_InternalComponent},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)