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
ProviderType: Enumeration = Enumeration(
    name="ProviderType",
    literals={
            EnumerationLiteral(name="FCO"),
			EnumerationLiteral(name="Openstack")
    }
)

VMSize: Enumeration = Enumeration(
    name="VMSize",
    literals={
            EnumerationLiteral(name="Small"),
			EnumerationLiteral(name="Medium"),
			EnumerationLiteral(name="Large")
    }
)

Language: Enumeration = Enumeration(
    name="Language",
    literals={
            EnumerationLiteral(name="PYTHON"),
			EnumerationLiteral(name="BASH"),
			EnumerationLiteral(name="JAVA")
    }
)

# Classes
ddsm_Resource = Class(name="ddsm::Resource")
ddsm_CloudElement = Class(name="ddsm::CloudElement", is_abstract=True)
ddsm_Property = Class(name="ddsm::Property")
ddsm_Artifact = Class(name="ddsm::Artifact")
ddsm_Port = Class(name="ddsm::Port", is_abstract=True)
ddsm_Component = Class(name="ddsm::Component", is_abstract=True)
CloudElement = Class(name="CloudElement")
ddsm_ProvidedPort = Class(name="ddsm::ProvidedPort")
ddsm_ProvidedExecutionPlatform = Class(name="ddsm::ProvidedExecutionPlatform")
ddsm_InternalComponent = Class(name="ddsm::InternalComponent")
Component = Class(name="Component")
ddsm_RequiredPort = Class(name="ddsm::RequiredPort")
ddsm_RequiredExecutionPlatform = Class(name="ddsm::RequiredExecutionPlatform")
ddsm_ExecutionPlatform = Class(name="ddsm::ExecutionPlatform", is_abstract=True)
Port = Class(name="Port")
ExecutionPlatform = Class(name="ExecutionPlatform")
ddsm_Relationship = Class(name="ddsm::Relationship")
ddsm_VM = Class(name="ddsm::VM")
ExternalComponent = Class(name="ExternalComponent")
ddsm_ExecutionBinding = Class(name="ddsm::ExecutionBinding")
ddsm_ExternalComponent = Class(name="ddsm::ExternalComponent")
ddsm_Provider = Class(name="ddsm::Provider")
ddsm_DDSM = Class(name="ddsm::DDSM")
ddsm_StormCluster = Class(name="ddsm::StormCluster")
MasterSlavePlatform = Class(name="MasterSlavePlatform")
ddsm_ClientNode = Class(name="ddsm::ClientNode")
InternalComponent = Class(name="InternalComponent")
ddsm_JobSubmission = Class(name="ddsm::JobSubmission")
ddsm_Crontab = Class(name="ddsm::Crontab")
ddsm_ZookeeperCluster = Class(name="ddsm::ZookeeperCluster")
PeerToPeerPlatform = Class(name="PeerToPeerPlatform")
ddsm_MasterNode = Class(name="ddsm::MasterNode")
ddsm_SlaveNode = Class(name="ddsm::SlaveNode")
ddsm_CassandraCluster = Class(name="ddsm::CassandraCluster")
ddsm_PeerNode = Class(name="ddsm::PeerNode")
ddsm_PeersQuorum = Class(name="ddsm::PeersQuorum")
ddsm_PeerToPeerPlatform = Class(name="ddsm::PeerToPeerPlatform")
ddsm_MasterSlavePlatform = Class(name="ddsm::MasterSlavePlatform")
ddsm_SparkCluster = Class(name="ddsm::SparkCluster")
ddsm_HDFSCluster = Class(name="ddsm::HDFSCluster")
ddsm_KafkaCluster = Class(name="ddsm::KafkaCluster")
ddsm_YarnCluster = Class(name="ddsm::YarnCluster")

# ddsm_Resource class attributes and methods
ddsm_Resource_resourceId: Property = Property(name="resourceId", type=StringType)
ddsm_Resource.attributes={ddsm_Resource_resourceId}

# ddsm_CloudElement class attributes and methods
ddsm_CloudElement_elementId: Property = Property(name="elementId", type=StringType)
ddsm_CloudElement_description: Property = Property(name="description", type=StringType)
ddsm_CloudElement.attributes={ddsm_CloudElement_elementId, ddsm_CloudElement_description}

# ddsm_Property class attributes and methods
ddsm_Property_propertyId: Property = Property(name="propertyId", type=StringType)
ddsm_Property_value: Property = Property(name="value", type=StringType)
ddsm_Property.attributes={ddsm_Property_propertyId, ddsm_Property_value}

# ddsm_Artifact class attributes and methods
ddsm_Artifact_resources: Property = Property(name="resources", type=StringType)
ddsm_Artifact_language: Property = Property(name="language", type=StringType)
ddsm_Artifact_artifactPath: Property = Property(name="artifactPath", type=StringType)
ddsm_Artifact_arguments: Property = Property(name="arguments", type=StringType)
ddsm_Artifact.attributes={ddsm_Artifact_artifactPath, ddsm_Artifact_resources, ddsm_Artifact_language, ddsm_Artifact_arguments}

# ddsm_Port class attributes and methods
ddsm_Port_isLocal: Property = Property(name="isLocal", type=BooleanType)
ddsm_Port_portNumber: Property = Property(name="portNumber", type=StringType)
ddsm_Port.attributes={ddsm_Port_portNumber, ddsm_Port_isLocal}

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

# Port class attributes and methods

# ExecutionPlatform class attributes and methods

# ddsm_Relationship class attributes and methods

# ddsm_VM class attributes and methods
ddsm_VM_is64os: Property = Property(name="is64os", type=StringType)
ddsm_VM_imageId: Property = Property(name="imageId", type=StringType)
ddsm_VM_maxCores: Property = Property(name="maxCores", type=StringType)
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
ddsm_VM_genericSize: Property = Property(name="genericSize", type=StringType)
ddsm_VM_instances: Property = Property(name="instances", type=IntegerType)
ddsm_VM_publicPorts: Property = Property(name="publicPorts", type=IntegerType)
ddsm_VM.attributes={ddsm_VM_publicAddress, ddsm_VM_imageId, ddsm_VM_maxStorage, ddsm_VM_is64os, ddsm_VM_minRam, ddsm_VM_instances, ddsm_VM_privateKey, ddsm_VM_genericSize, ddsm_VM_sshKey, ddsm_VM_publicPorts, ddsm_VM_minCores, ddsm_VM_os, ddsm_VM_minStorage, ddsm_VM_providerSpecificTypeName, ddsm_VM_maxCores, ddsm_VM_securityGroup, ddsm_VM_maxRam}

# ExternalComponent class attributes and methods

# ddsm_ExecutionBinding class attributes and methods

# ddsm_ExternalComponent class attributes and methods
ddsm_ExternalComponent_location: Property = Property(name="location", type=StringType)
ddsm_ExternalComponent_login: Property = Property(name="login", type=StringType)
ddsm_ExternalComponent_password: Property = Property(name="password", type=StringType)
ddsm_ExternalComponent_region: Property = Property(name="region", type=StringType)
ddsm_ExternalComponent_serviceType: Property = Property(name="serviceType", type=StringType)
ddsm_ExternalComponent_endPoint: Property = Property(name="endPoint", type=StringType)
ddsm_ExternalComponent.attributes={ddsm_ExternalComponent_login, ddsm_ExternalComponent_location, ddsm_ExternalComponent_endPoint, ddsm_ExternalComponent_serviceType, ddsm_ExternalComponent_password, ddsm_ExternalComponent_region}

# ddsm_Provider class attributes and methods
ddsm_Provider_type: Property = Property(name="type", type=StringType)
ddsm_Provider_credentialsPath: Property = Property(name="credentialsPath", type=StringType)
ddsm_Provider.attributes={ddsm_Provider_credentialsPath, ddsm_Provider_type}

# ddsm_DDSM class attributes and methods
ddsm_DDSM_modelId: Property = Property(name="modelId", type=StringType)
ddsm_DDSM_description: Property = Property(name="description", type=StringType)
ddsm_DDSM.attributes={ddsm_DDSM_description, ddsm_DDSM_modelId}

# ddsm_StormCluster class attributes and methods
ddsm_StormCluster_taskTimeout: Property = Property(name="taskTimeout", type=IntegerType)
ddsm_StormCluster_supervisorFrequency: Property = Property(name="supervisorFrequency", type=IntegerType)
ddsm_StormCluster_queueSize: Property = Property(name="queueSize", type=IntegerType)
ddsm_StormCluster_monitorFrequency: Property = Property(name="monitorFrequency", type=IntegerType)
ddsm_StormCluster_retryTimes: Property = Property(name="retryTimes", type=IntegerType)
ddsm_StormCluster_retryInterval: Property = Property(name="retryInterval", type=IntegerType)
ddsm_StormCluster_workerStartTimeout: Property = Property(name="workerStartTimeout", type=IntegerType)
ddsm_StormCluster_heartbeatFrequency: Property = Property(name="heartbeatFrequency", type=IntegerType)
ddsm_StormCluster_cpuCapacity: Property = Property(name="cpuCapacity", type=IntegerType)
ddsm_StormCluster_memoryCapacity: Property = Property(name="memoryCapacity", type=IntegerType)
ddsm_StormCluster.attributes={ddsm_StormCluster_memoryCapacity, ddsm_StormCluster_retryTimes, ddsm_StormCluster_supervisorFrequency, ddsm_StormCluster_taskTimeout, ddsm_StormCluster_monitorFrequency, ddsm_StormCluster_queueSize, ddsm_StormCluster_workerStartTimeout, ddsm_StormCluster_cpuCapacity, ddsm_StormCluster_heartbeatFrequency, ddsm_StormCluster_retryInterval}

# MasterSlavePlatform class attributes and methods

# ddsm_ClientNode class attributes and methods
ddsm_ClientNode_skipRunningJob: Property = Property(name="skipRunningJob", type=BooleanType)
ddsm_ClientNode_numberOfSubmissions: Property = Property(name="numberOfSubmissions", type=IntegerType)
ddsm_ClientNode.attributes={ddsm_ClientNode_numberOfSubmissions, ddsm_ClientNode_skipRunningJob}

# InternalComponent class attributes and methods

# ddsm_JobSubmission class attributes and methods
ddsm_JobSubmission_artifactUrl: Property = Property(name="artifactUrl", type=StringType)
ddsm_JobSubmission_mainClass: Property = Property(name="mainClass", type=StringType)
ddsm_JobSubmission_applicationArguments: Property = Property(name="applicationArguments", type=StringType)
ddsm_JobSubmission.attributes={ddsm_JobSubmission_applicationArguments, ddsm_JobSubmission_artifactUrl, ddsm_JobSubmission_mainClass}

# ddsm_Crontab class attributes and methods
ddsm_Crontab_min: Property = Property(name="min", type=IntegerType)
ddsm_Crontab_hour: Property = Property(name="hour", type=IntegerType)
ddsm_Crontab_dayOfMonth: Property = Property(name="dayOfMonth", type=IntegerType)
ddsm_Crontab_month: Property = Property(name="month", type=IntegerType)
ddsm_Crontab_dayOfWeek: Property = Property(name="dayOfWeek", type=IntegerType)
ddsm_Crontab.attributes={ddsm_Crontab_dayOfMonth, ddsm_Crontab_hour, ddsm_Crontab_dayOfWeek, ddsm_Crontab_min, ddsm_Crontab_month}

# ddsm_ZookeeperCluster class attributes and methods
ddsm_ZookeeperCluster_tickTime: Property = Property(name="tickTime", type=IntegerType)
ddsm_ZookeeperCluster_syncLimit: Property = Property(name="syncLimit", type=IntegerType)
ddsm_ZookeeperCluster_initLimit: Property = Property(name="initLimit", type=IntegerType)
ddsm_ZookeeperCluster.attributes={ddsm_ZookeeperCluster_tickTime, ddsm_ZookeeperCluster_initLimit, ddsm_ZookeeperCluster_syncLimit}

# PeerToPeerPlatform class attributes and methods

# ddsm_MasterNode class attributes and methods

# ddsm_SlaveNode class attributes and methods

# ddsm_CassandraCluster class attributes and methods

# ddsm_PeerNode class attributes and methods

# ddsm_PeersQuorum class attributes and methods

# ddsm_PeerToPeerPlatform class attributes and methods

# ddsm_MasterSlavePlatform class attributes and methods

# ddsm_SparkCluster class attributes and methods
ddsm_SparkCluster_driverMemory: Property = Property(name="driverMemory", type=IntegerType)
ddsm_SparkCluster_driverCores: Property = Property(name="driverCores", type=IntegerType)
ddsm_SparkCluster_maxResultSize: Property = Property(name="maxResultSize", type=IntegerType)
ddsm_SparkCluster_UIPort: Property = Property(name="UIPort", type=IntegerType)
ddsm_SparkCluster_sparkExecutorMemory: Property = Property(name="sparkExecutorMemory", type=IntegerType)
ddsm_SparkCluster.attributes={ddsm_SparkCluster_UIPort, ddsm_SparkCluster_sparkExecutorMemory, ddsm_SparkCluster_maxResultSize, ddsm_SparkCluster_driverCores, ddsm_SparkCluster_driverMemory}

# ddsm_HDFSCluster class attributes and methods

# ddsm_KafkaCluster class attributes and methods

# ddsm_YarnCluster class attributes and methods

# Relationships
resource0: BinaryAssociation = BinaryAssociation(
    name="resource0",
    ends={
        Property(name="ddsm_Resource", type=ddsm_CloudElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsm_CloudElement", type=ddsm_Resource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
destroy14: BinaryAssociation = BinaryAssociation(
    name="destroy14",
    ends={
        Property(name="ddsm_Artifact16", type=ddsm_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsm_Resource15", type=ddsm_Artifact, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
property1: BinaryAssociation = BinaryAssociation(
    name="property1",
    ends={
        Property(name="ddsm_Property", type=ddsm_CloudElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsm_CloudElement2", type=ddsm_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
download3: BinaryAssociation = BinaryAssociation(
    name="download3",
    ends={
        Property(name="ddsm_Artifact", type=ddsm_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsm_Resource4", type=ddsm_Artifact, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
configure5: BinaryAssociation = BinaryAssociation(
    name="configure5",
    ends={
        Property(name="ddsm_Artifact7", type=ddsm_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsm_Resource6", type=ddsm_Artifact, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
start8: BinaryAssociation = BinaryAssociation(
    name="start8",
    ends={
        Property(name="ddsm_Artifact10", type=ddsm_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsm_Resource9", type=ddsm_Artifact, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stop11: BinaryAssociation = BinaryAssociation(
    name="stop11",
    ends={
        Property(name="ddsm_Artifact13", type=ddsm_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsm_Resource12", type=ddsm_Artifact, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
install17: BinaryAssociation = BinaryAssociation(
    name="install17",
    ends={
        Property(name="ddsm_Artifact19", type=ddsm_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsm_Resource18", type=ddsm_Artifact, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
providedport20: BinaryAssociation = BinaryAssociation(
    name="providedport20",
    ends={
        Property(name="ddsm_ProvidedPort", type=ddsm_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsm_Component", type=ddsm_ProvidedPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedexecutionplatform21: BinaryAssociation = BinaryAssociation(
    name="providedexecutionplatform21",
    ends={
        Property(name="ddsm_ProvidedExecutionPlatform", type=ddsm_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsm_Component22", type=ddsm_ProvidedExecutionPlatform, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredport23: BinaryAssociation = BinaryAssociation(
    name="requiredport23",
    ends={
        Property(name="ddsm_RequiredPort", type=ddsm_InternalComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsm_InternalComponent", type=ddsm_RequiredPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredexecutionplatform24: BinaryAssociation = BinaryAssociation(
    name="requiredexecutionplatform24",
    ends={
        Property(name="ddsm_RequiredExecutionPlatform", type=ddsm_InternalComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsm_InternalComponent25", type=ddsm_RequiredExecutionPlatform, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedport32: BinaryAssociation = BinaryAssociation(
    name="providedport32",
    ends={
        Property(name="ddsm_ProvidedPort33", type=ddsm_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsm_Relationship", type=ddsm_ProvidedPort, multiplicity=Multiplicity(1, 1))
    }
)
requiredport34: BinaryAssociation = BinaryAssociation(
    name="requiredport34",
    ends={
        Property(name="ddsm_RequiredPort36", type=ddsm_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsm_Relationship35", type=ddsm_RequiredPort, multiplicity=Multiplicity(1, 1))
    }
)
owner26: BinaryAssociation = BinaryAssociation(
    name="owner26",
    ends={
        Property(name="ddsm_Component28", type=ddsm_ProvidedPort, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsm_ProvidedPort27", type=ddsm_Component, multiplicity=Multiplicity(1, 1))
    }
)
owner29: BinaryAssociation = BinaryAssociation(
    name="owner29",
    ends={
        Property(name="ddsm_Component31", type=ddsm_ProvidedExecutionPlatform, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsm_ProvidedExecutionPlatform30", type=ddsm_Component, multiplicity=Multiplicity(1, 1))
    }
)
requiredexecutionplatform37: BinaryAssociation = BinaryAssociation(
    name="requiredexecutionplatform37",
    ends={
        Property(name="ddsm_RequiredExecutionPlatform38", type=ddsm_ExecutionBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsm_ExecutionBinding", type=ddsm_RequiredExecutionPlatform, multiplicity=Multiplicity(1, 1))
    }
)
providedexecutionplatform39: BinaryAssociation = BinaryAssociation(
    name="providedexecutionplatform39",
    ends={
        Property(name="ddsm_ProvidedExecutionPlatform41", type=ddsm_ExecutionBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsm_ExecutionBinding40", type=ddsm_ProvidedExecutionPlatform, multiplicity=Multiplicity(1, 1))
    }
)
provider42: BinaryAssociation = BinaryAssociation(
    name="provider42",
    ends={
        Property(name="ddsm_Provider", type=ddsm_ExternalComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsm_ExternalComponent", type=ddsm_Provider, multiplicity=Multiplicity(1, 1))
    }
)
cloudelement43: BinaryAssociation = BinaryAssociation(
    name="cloudelement43",
    ends={
        Property(name="ddsm_CloudElement44", type=ddsm_DDSM, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsm_DDSM", type=ddsm_CloudElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties45: BinaryAssociation = BinaryAssociation(
    name="properties45",
    ends={
        Property(name="ddsm_Property47", type=ddsm_DDSM, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsm_DDSM46", type=ddsm_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resources48: BinaryAssociation = BinaryAssociation(
    name="resources48",
    ends={
        Property(name="ddsm_Resource50", type=ddsm_DDSM, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsm_DDSM49", type=ddsm_Resource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
artifacts51: BinaryAssociation = BinaryAssociation(
    name="artifacts51",
    ends={
        Property(name="ddsm_Artifact53", type=ddsm_DDSM, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsm_DDSM52", type=ddsm_Artifact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
submits54: BinaryAssociation = BinaryAssociation(
    name="submits54",
    ends={
        Property(name="ddsm_JobSubmission", type=ddsm_ClientNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsm_ClientNode", type=ddsm_JobSubmission, multiplicity=Multiplicity(1, 1))
    }
)
hasSchedule55: BinaryAssociation = BinaryAssociation(
    name="hasSchedule55",
    ends={
        Property(name="ddsm_Crontab", type=ddsm_ClientNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsm_ClientNode56", type=ddsm_Crontab, multiplicity=Multiplicity(0, 1))
    }
)
hasMaster57: BinaryAssociation = BinaryAssociation(
    name="hasMaster57",
    ends={
        Property(name="ddsm_MasterNode", type=ddsm_SlaveNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsm_SlaveNode", type=ddsm_MasterNode, multiplicity=Multiplicity(1, 1))
    }
)
requiresSlaveVm63: BinaryAssociation = BinaryAssociation(
    name="requiresSlaveVm63",
    ends={
        Property(name="ddsm_RequiredExecutionPlatform65", type=ddsm_MasterSlavePlatform, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsm_MasterSlavePlatform64", type=ddsm_RequiredExecutionPlatform, multiplicity=Multiplicity(1, 9999))
    }
)
belongsToQuorum58: BinaryAssociation = BinaryAssociation(
    name="belongsToQuorum58",
    ends={
        Property(name="ddsm_PeersQuorum", type=ddsm_PeerNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsm_PeerNode", type=ddsm_PeersQuorum, multiplicity=Multiplicity(1, 1))
    }
)
requiresPeerVm59: BinaryAssociation = BinaryAssociation(
    name="requiresPeerVm59",
    ends={
        Property(name="ddsm_RequiredExecutionPlatform60", type=ddsm_PeerToPeerPlatform, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsm_PeerToPeerPlatform", type=ddsm_RequiredExecutionPlatform, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
requiresMasterVm61: BinaryAssociation = BinaryAssociation(
    name="requiresMasterVm61",
    ends={
        Property(name="ddsm_RequiredExecutionPlatform62", type=ddsm_MasterSlavePlatform, multiplicity=Multiplicity(1, 1)),
        Property(name="ddsm_MasterSlavePlatform", type=ddsm_RequiredExecutionPlatform, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_ddsm_Port_CloudElement = Generalization(general=CloudElement, specific=ddsm_Port)
gen_ddsm_Component_CloudElement = Generalization(general=CloudElement, specific=ddsm_Component)
gen_ddsm_InternalComponent_Component = Generalization(general=Component, specific=ddsm_InternalComponent)
gen_ddsm_ExecutionPlatform_CloudElement = Generalization(general=CloudElement, specific=ddsm_ExecutionPlatform)
gen_ddsm_RequiredPort_Port = Generalization(general=Port, specific=ddsm_RequiredPort)
gen_ddsm_ProvidedPort_Port = Generalization(general=Port, specific=ddsm_ProvidedPort)
gen_ddsm_RequiredExecutionPlatform_ExecutionPlatform = Generalization(general=ExecutionPlatform, specific=ddsm_RequiredExecutionPlatform)
gen_ddsm_ProvidedExecutionPlatform_ExecutionPlatform = Generalization(general=ExecutionPlatform, specific=ddsm_ProvidedExecutionPlatform)
gen_ddsm_Relationship_CloudElement = Generalization(general=CloudElement, specific=ddsm_Relationship)
gen_ddsm_VM_ExternalComponent = Generalization(general=ExternalComponent, specific=ddsm_VM)
gen_ddsm_ExecutionBinding_CloudElement = Generalization(general=CloudElement, specific=ddsm_ExecutionBinding)
gen_ddsm_ExternalComponent_Component = Generalization(general=Component, specific=ddsm_ExternalComponent)
gen_ddsm_Provider_CloudElement = Generalization(general=CloudElement, specific=ddsm_Provider)
gen_ddsm_StormCluster_MasterSlavePlatform = Generalization(general=MasterSlavePlatform, specific=ddsm_StormCluster)
gen_ddsm_ClientNode_InternalComponent = Generalization(general=InternalComponent, specific=ddsm_ClientNode)
gen_ddsm_ZookeeperCluster_PeerToPeerPlatform = Generalization(general=PeerToPeerPlatform, specific=ddsm_ZookeeperCluster)
gen_ddsm_JobSubmission_CloudElement = Generalization(general=CloudElement, specific=ddsm_JobSubmission)
gen_ddsm_MasterNode_InternalComponent = Generalization(general=InternalComponent, specific=ddsm_MasterNode)
gen_ddsm_SlaveNode_InternalComponent = Generalization(general=InternalComponent, specific=ddsm_SlaveNode)
gen_ddsm_CassandraCluster_PeerToPeerPlatform = Generalization(general=PeerToPeerPlatform, specific=ddsm_CassandraCluster)
gen_ddsm_PeerNode_InternalComponent = Generalization(general=InternalComponent, specific=ddsm_PeerNode)
gen_ddsm_PeersQuorum_InternalComponent = Generalization(general=InternalComponent, specific=ddsm_PeersQuorum)
gen_ddsm_PeerToPeerPlatform_InternalComponent = Generalization(general=InternalComponent, specific=ddsm_PeerToPeerPlatform)
gen_ddsm_MasterSlavePlatform_InternalComponent = Generalization(general=InternalComponent, specific=ddsm_MasterSlavePlatform)
gen_ddsm_SparkCluster_MasterSlavePlatform = Generalization(general=MasterSlavePlatform, specific=ddsm_SparkCluster)
gen_ddsm_HDFSCluster_MasterSlavePlatform = Generalization(general=MasterSlavePlatform, specific=ddsm_HDFSCluster)
gen_ddsm_KafkaCluster_PeerToPeerPlatform = Generalization(general=PeerToPeerPlatform, specific=ddsm_KafkaCluster)
gen_ddsm_YarnCluster_MasterSlavePlatform = Generalization(general=MasterSlavePlatform, specific=ddsm_YarnCluster)

# Domain Model
domain_model = DomainModel(
    name="ddsm",
    types={ddsm_Resource, ddsm_CloudElement, ddsm_Property, ddsm_Artifact, ddsm_Port, ddsm_Component, CloudElement, ddsm_ProvidedPort, ddsm_ProvidedExecutionPlatform, ddsm_InternalComponent, Component, ddsm_RequiredPort, ddsm_RequiredExecutionPlatform, ddsm_ExecutionPlatform, Port, ExecutionPlatform, ddsm_Relationship, ddsm_VM, ExternalComponent, ddsm_ExecutionBinding, ddsm_ExternalComponent, ddsm_Provider, ddsm_DDSM, ddsm_StormCluster, MasterSlavePlatform, ddsm_ClientNode, InternalComponent, ddsm_JobSubmission, ddsm_Crontab, ddsm_ZookeeperCluster, PeerToPeerPlatform, ddsm_MasterNode, ddsm_SlaveNode, ddsm_CassandraCluster, ddsm_PeerNode, ddsm_PeersQuorum, ddsm_PeerToPeerPlatform, ddsm_MasterSlavePlatform, ddsm_SparkCluster, ddsm_HDFSCluster, ddsm_KafkaCluster, ddsm_YarnCluster, ProviderType, VMSize, Language},
    associations={resource0, destroy14, property1, download3, configure5, start8, stop11, install17, providedport20, providedexecutionplatform21, requiredport23, requiredexecutionplatform24, providedport32, requiredport34, owner26, owner29, requiredexecutionplatform37, providedexecutionplatform39, provider42, cloudelement43, properties45, resources48, artifacts51, submits54, hasSchedule55, hasMaster57, requiresSlaveVm63, belongsToQuorum58, requiresPeerVm59, requiresMasterVm61},
    generalizations={gen_ddsm_Port_CloudElement, gen_ddsm_Component_CloudElement, gen_ddsm_InternalComponent_Component, gen_ddsm_ExecutionPlatform_CloudElement, gen_ddsm_RequiredPort_Port, gen_ddsm_ProvidedPort_Port, gen_ddsm_RequiredExecutionPlatform_ExecutionPlatform, gen_ddsm_ProvidedExecutionPlatform_ExecutionPlatform, gen_ddsm_Relationship_CloudElement, gen_ddsm_VM_ExternalComponent, gen_ddsm_ExecutionBinding_CloudElement, gen_ddsm_ExternalComponent_Component, gen_ddsm_Provider_CloudElement, gen_ddsm_StormCluster_MasterSlavePlatform, gen_ddsm_ClientNode_InternalComponent, gen_ddsm_ZookeeperCluster_PeerToPeerPlatform, gen_ddsm_JobSubmission_CloudElement, gen_ddsm_MasterNode_InternalComponent, gen_ddsm_SlaveNode_InternalComponent, gen_ddsm_CassandraCluster_PeerToPeerPlatform, gen_ddsm_PeerNode_InternalComponent, gen_ddsm_PeersQuorum_InternalComponent, gen_ddsm_PeerToPeerPlatform_InternalComponent, gen_ddsm_MasterSlavePlatform_InternalComponent, gen_ddsm_SparkCluster_MasterSlavePlatform, gen_ddsm_HDFSCluster_MasterSlavePlatform, gen_ddsm_KafkaCluster_PeerToPeerPlatform, gen_ddsm_YarnCluster_MasterSlavePlatform},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)