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
cloudml_core_CloudMLElement = Class(name="cloudml::core::CloudMLElement", is_abstract=True)
cloudml_core_Property = Class(name="cloudml::core::Property")
CloudMLElement = Class(name="CloudMLElement")
cloudml_core_CloudMLElementWithProperties = Class(name="cloudml::core::CloudMLElementWithProperties", is_abstract=True)
Property_ = Class(name="Property")
Resource = Class(name="Resource")
PuppetResource = Class(name="PuppetResource")
DockerResource = Class(name="DockerResource")
cloudml_core_Resource = Class(name="cloudml::core::Resource")
CloudMLElementWithProperties = Class(name="CloudMLElementWithProperties")
cloudml_core_CloudMLModel = Class(name="cloudml::core::CloudMLModel")
Provider = Class(name="Provider")
Component = Class(name="Component")
Cloud = Class(name="Cloud")
ComponentInstance = Class(name="ComponentInstance")
InternalComponent = Class(name="InternalComponent")
ExternalComponent = Class(name="ExternalComponent")
InternalComponentInstance = Class(name="InternalComponentInstance")
ExternalComponentInstance = Class(name="ExternalComponentInstance")
VM = Class(name="VM")
VMInstance = Class(name="VMInstance")
Relationship = Class(name="Relationship")
RelationshipInstance = Class(name="RelationshipInstance")
ExecuteInstance = Class(name="ExecuteInstance")
ResourcesPool = Class(name="ResourcesPool")
VMPort = Class(name="VMPort")
cloudml_core_VMPort = Class(name="cloudml::core::VMPort")
cloudml_core_Provider = Class(name="cloudml::core::Provider")
cloudml_core_Component = Class(name="cloudml::core::Component", is_abstract=True)
ProvidedPort = Class(name="ProvidedPort")
ProvidedExecutionPlatform = Class(name="ProvidedExecutionPlatform")
cloudml_core_InternalComponent = Class(name="cloudml::core::InternalComponent")
RequiredPort = Class(name="RequiredPort")
RequiredExecutionPlatform = Class(name="RequiredExecutionPlatform")
cloudml_core_Port = Class(name="cloudml::core::Port", is_abstract=True)
cloudml_core_VM = Class(name="cloudml::core::VM")
cloudml_core_RequiredPort = Class(name="cloudml::core::RequiredPort")
Port = Class(name="Port")
cloudml_core_ProvidedPort = Class(name="cloudml::core::ProvidedPort")
cloudml_core_Relationship = Class(name="cloudml::core::Relationship")
cloudml_core_Cloud = Class(name="cloudml::core::Cloud")
cloudml_core_VMInstance = Class(name="cloudml::core::VMInstance")
VMPortInstance = Class(name="VMPortInstance")
cloudml_core_VMPortInstance = Class(name="cloudml::core::VMPortInstance")
cloudml_core_ComponentInstance = Class(name="cloudml::core::ComponentInstance", is_abstract=True)
ProvidedPortInstance = Class(name="ProvidedPortInstance")
ProvidedExecutionPlatformInstance = Class(name="ProvidedExecutionPlatformInstance")
cloudml_core_InternalComponentInstance = Class(name="cloudml::core::InternalComponentInstance")
RequiredPortInstance = Class(name="RequiredPortInstance")
RequiredExecutionPlatformInstance = Class(name="RequiredExecutionPlatformInstance")
cloudml_core_PortInstance = Class(name="cloudml::core::PortInstance")
cloudml_core_RequiredPortInstance = Class(name="cloudml::core::RequiredPortInstance")
PortInstance = Class(name="PortInstance")
cloudml_core_ProvidedPortInstance = Class(name="cloudml::core::ProvidedPortInstance")
cloudml_core_RelationshipInstance = Class(name="cloudml::core::RelationshipInstance")
cloudml_core_ExternalComponent = Class(name="cloudml::core::ExternalComponent")
cloudml_core_ExternalComponentInstance = Class(name="cloudml::core::ExternalComponentInstance")
cloudml_core_ExecutionPlatform = Class(name="cloudml::core::ExecutionPlatform", is_abstract=True)
cloudml_core_ExecutionPlatformInstance = Class(name="cloudml::core::ExecutionPlatformInstance", is_abstract=True)
ExecutionPlatform = Class(name="ExecutionPlatform")
cloudml_core_ProvidedExecutionPlatform = Class(name="cloudml::core::ProvidedExecutionPlatform")
cloudml_core_ProvidedExecutionPlatformInstance = Class(name="cloudml::core::ProvidedExecutionPlatformInstance")
ExecutionPlatformInstance = Class(name="ExecutionPlatformInstance")
cloudml_core_RequiredExecutionPlatform = Class(name="cloudml::core::RequiredExecutionPlatform")
cloudml_core_RequiredExecutionPlatformInstance = Class(name="cloudml::core::RequiredExecutionPlatformInstance")
cloudml_core_ExecuteInstance = Class(name="cloudml::core::ExecuteInstance")
cloudml_core_PuppetResource = Class(name="cloudml::core::PuppetResource")
cloudml_core_ResourcesPool = Class(name="cloudml::core::ResourcesPool")
cloudml_core_DockerResource = Class(name="cloudml::core::DockerResource")

# cloudml_core_CloudMLElement class attributes and methods
cloudml_core_CloudMLElement_name: Property = Property(name="name", type=StringType)
cloudml_core_CloudMLElement.attributes={cloudml_core_CloudMLElement_name}

# cloudml_core_Property class attributes and methods
cloudml_core_Property_value: Property = Property(name="value", type=StringType)
cloudml_core_Property.attributes={cloudml_core_Property_value}

# CloudMLElement class attributes and methods

# cloudml_core_CloudMLElementWithProperties class attributes and methods

# Property class attributes and methods

# Resource class attributes and methods

# PuppetResource class attributes and methods

# DockerResource class attributes and methods

# cloudml_core_Resource class attributes and methods
cloudml_core_Resource_downloadCommand: Property = Property(name="downloadCommand", type=StringType)
cloudml_core_Resource_configureCommand: Property = Property(name="configureCommand", type=StringType)
cloudml_core_Resource_startCommand: Property = Property(name="startCommand", type=StringType)
cloudml_core_Resource_stopCommand: Property = Property(name="stopCommand", type=StringType)
cloudml_core_Resource_requireCredentials: Property = Property(name="requireCredentials", type=BooleanType)
cloudml_core_Resource_executeLocally: Property = Property(name="executeLocally", type=BooleanType)
cloudml_core_Resource_uploadCommand: Property = Property(name="uploadCommand", type=StringType)
cloudml_core_Resource_installCommand: Property = Property(name="installCommand", type=StringType)
cloudml_core_Resource.attributes={cloudml_core_Resource_stopCommand, cloudml_core_Resource_uploadCommand, cloudml_core_Resource_downloadCommand, cloudml_core_Resource_requireCredentials, cloudml_core_Resource_configureCommand, cloudml_core_Resource_startCommand, cloudml_core_Resource_executeLocally, cloudml_core_Resource_installCommand}

# CloudMLElementWithProperties class attributes and methods

# cloudml_core_CloudMLModel class attributes and methods

# Provider class attributes and methods

# Component class attributes and methods

# Cloud class attributes and methods

# ComponentInstance class attributes and methods

# InternalComponent class attributes and methods

# ExternalComponent class attributes and methods

# InternalComponentInstance class attributes and methods

# ExternalComponentInstance class attributes and methods

# VM class attributes and methods

# VMInstance class attributes and methods

# Relationship class attributes and methods

# RelationshipInstance class attributes and methods

# ExecuteInstance class attributes and methods

# ResourcesPool class attributes and methods

# VMPort class attributes and methods

# cloudml_core_VMPort class attributes and methods

# cloudml_core_Provider class attributes and methods
cloudml_core_Provider_credentials: Property = Property(name="credentials", type=StringType)
cloudml_core_Provider_login: Property = Property(name="login", type=StringType)
cloudml_core_Provider_password: Property = Property(name="password", type=StringType)
cloudml_core_Provider.attributes={cloudml_core_Provider_password, cloudml_core_Provider_login, cloudml_core_Provider_credentials}

# cloudml_core_Component class attributes and methods

# ProvidedPort class attributes and methods

# ProvidedExecutionPlatform class attributes and methods

# cloudml_core_InternalComponent class attributes and methods

# RequiredPort class attributes and methods

# RequiredExecutionPlatform class attributes and methods

# cloudml_core_Port class attributes and methods
cloudml_core_Port_isLocal: Property = Property(name="isLocal", type=BooleanType)
cloudml_core_Port_portNumber: Property = Property(name="portNumber", type=IntegerType)
cloudml_core_Port.attributes={cloudml_core_Port_portNumber, cloudml_core_Port_isLocal}

# cloudml_core_VM class attributes and methods
cloudml_core_VM_minRam: Property = Property(name="minRam", type=IntegerType)
cloudml_core_VM_maxRam: Property = Property(name="maxRam", type=IntegerType)
cloudml_core_VM_minCores: Property = Property(name="minCores", type=IntegerType)
cloudml_core_VM_maxCores: Property = Property(name="maxCores", type=IntegerType)
cloudml_core_VM_minStorage: Property = Property(name="minStorage", type=IntegerType)
cloudml_core_VM_maxStorage: Property = Property(name="maxStorage", type=IntegerType)
cloudml_core_VM_os: Property = Property(name="os", type=StringType)
cloudml_core_VM_is64os: Property = Property(name="is64os", type=BooleanType)
cloudml_core_VM_imageId: Property = Property(name="imageId", type=StringType)
cloudml_core_VM_securityGroup: Property = Property(name="securityGroup", type=StringType)
cloudml_core_VM_sshKey: Property = Property(name="sshKey", type=StringType)
cloudml_core_VM_privateKey: Property = Property(name="privateKey", type=StringType)
cloudml_core_VM_groupName: Property = Property(name="groupName", type=StringType)
cloudml_core_VM_providerSpecificTypeName: Property = Property(name="providerSpecificTypeName", type=StringType)
cloudml_core_VM.attributes={cloudml_core_VM_privateKey, cloudml_core_VM_is64os, cloudml_core_VM_groupName, cloudml_core_VM_providerSpecificTypeName, cloudml_core_VM_maxRam, cloudml_core_VM_maxCores, cloudml_core_VM_sshKey, cloudml_core_VM_maxStorage, cloudml_core_VM_securityGroup, cloudml_core_VM_minStorage, cloudml_core_VM_imageId, cloudml_core_VM_os, cloudml_core_VM_minRam, cloudml_core_VM_minCores}

# cloudml_core_RequiredPort class attributes and methods
cloudml_core_RequiredPort_isMandatory: Property = Property(name="isMandatory", type=BooleanType)
cloudml_core_RequiredPort.attributes={cloudml_core_RequiredPort_isMandatory}

# Port class attributes and methods

# cloudml_core_ProvidedPort class attributes and methods

# cloudml_core_Relationship class attributes and methods

# cloudml_core_Cloud class attributes and methods

# cloudml_core_VMInstance class attributes and methods
cloudml_core_VMInstance_publicAddress: Property = Property(name="publicAddress", type=StringType)
cloudml_core_VMInstance_id: Property = Property(name="id", type=StringType)
cloudml_core_VMInstance.attributes={cloudml_core_VMInstance_publicAddress, cloudml_core_VMInstance_id}

# VMPortInstance class attributes and methods

# cloudml_core_VMPortInstance class attributes and methods

# cloudml_core_ComponentInstance class attributes and methods

# ProvidedPortInstance class attributes and methods

# ProvidedExecutionPlatformInstance class attributes and methods

# cloudml_core_InternalComponentInstance class attributes and methods

# RequiredPortInstance class attributes and methods

# RequiredExecutionPlatformInstance class attributes and methods

# cloudml_core_PortInstance class attributes and methods

# cloudml_core_RequiredPortInstance class attributes and methods

# PortInstance class attributes and methods

# cloudml_core_ProvidedPortInstance class attributes and methods

# cloudml_core_RelationshipInstance class attributes and methods

# cloudml_core_ExternalComponent class attributes and methods
cloudml_core_ExternalComponent_endPoint: Property = Property(name="endPoint", type=StringType)
cloudml_core_ExternalComponent_login: Property = Property(name="login", type=StringType)
cloudml_core_ExternalComponent_passwd: Property = Property(name="passwd", type=StringType)
cloudml_core_ExternalComponent_location: Property = Property(name="location", type=StringType)
cloudml_core_ExternalComponent_serviceType: Property = Property(name="serviceType", type=StringType)
cloudml_core_ExternalComponent_Region: Property = Property(name="Region", type=StringType)
cloudml_core_ExternalComponent.attributes={cloudml_core_ExternalComponent_passwd, cloudml_core_ExternalComponent_serviceType, cloudml_core_ExternalComponent_Region, cloudml_core_ExternalComponent_endPoint, cloudml_core_ExternalComponent_login, cloudml_core_ExternalComponent_location}

# cloudml_core_ExternalComponentInstance class attributes and methods
cloudml_core_ExternalComponentInstance_ips: Property = Property(name="ips", type=StringType)
cloudml_core_ExternalComponentInstance.attributes={cloudml_core_ExternalComponentInstance_ips}

# cloudml_core_ExecutionPlatform class attributes and methods

# cloudml_core_ExecutionPlatformInstance class attributes and methods

# ExecutionPlatform class attributes and methods

# cloudml_core_ProvidedExecutionPlatform class attributes and methods

# cloudml_core_ProvidedExecutionPlatformInstance class attributes and methods

# ExecutionPlatformInstance class attributes and methods

# cloudml_core_RequiredExecutionPlatform class attributes and methods

# cloudml_core_RequiredExecutionPlatformInstance class attributes and methods

# cloudml_core_ExecuteInstance class attributes and methods

# cloudml_core_PuppetResource class attributes and methods
cloudml_core_PuppetResource_masterEndpoint: Property = Property(name="masterEndpoint", type=StringType)
cloudml_core_PuppetResource_repositoryEndpoint: Property = Property(name="repositoryEndpoint", type=StringType)
cloudml_core_PuppetResource_configureHostnameCommand: Property = Property(name="configureHostnameCommand", type=StringType)
cloudml_core_PuppetResource_username: Property = Property(name="username", type=StringType)
cloudml_core_PuppetResource_repositoryKey: Property = Property(name="repositoryKey", type=StringType)
cloudml_core_PuppetResource_configurationFile: Property = Property(name="configurationFile", type=StringType)
cloudml_core_PuppetResource_manifestEntry: Property = Property(name="manifestEntry", type=StringType)
cloudml_core_PuppetResource.attributes={cloudml_core_PuppetResource_repositoryEndpoint, cloudml_core_PuppetResource_masterEndpoint, cloudml_core_PuppetResource_configurationFile, cloudml_core_PuppetResource_repositoryKey, cloudml_core_PuppetResource_configureHostnameCommand, cloudml_core_PuppetResource_manifestEntry, cloudml_core_PuppetResource_username}

# cloudml_core_ResourcesPool class attributes and methods
cloudml_core_ResourcesPool_minReplicats: Property = Property(name="minReplicats", type=IntegerType)
cloudml_core_ResourcesPool_maxReplicats: Property = Property(name="maxReplicats", type=IntegerType)
cloudml_core_ResourcesPool_nbReplicats: Property = Property(name="nbReplicats", type=IntegerType)
cloudml_core_ResourcesPool_type: Property = Property(name="type", type=StringType)
cloudml_core_ResourcesPool.attributes={cloudml_core_ResourcesPool_maxReplicats, cloudml_core_ResourcesPool_type, cloudml_core_ResourcesPool_minReplicats, cloudml_core_ResourcesPool_nbReplicats}

# cloudml_core_DockerResource class attributes and methods
cloudml_core_DockerResource_image: Property = Property(name="image", type=StringType)
cloudml_core_DockerResource_dockerFilePath: Property = Property(name="dockerFilePath", type=StringType)
cloudml_core_DockerResource.attributes={cloudml_core_DockerResource_image, cloudml_core_DockerResource_dockerFilePath}

# Relationships
properties0: BinaryAssociation = BinaryAssociation(
    name="properties0",
    ends={
        Property(name="Property", type=cloudml_core_CloudMLElementWithProperties, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_CloudMLElementWithProperties", type=Property_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resources1: BinaryAssociation = BinaryAssociation(
    name="resources1",
    ends={
        Property(name="Resource", type=cloudml_core_CloudMLElementWithProperties, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_CloudMLElementWithProperties2", type=Resource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
puppetResources3: BinaryAssociation = BinaryAssociation(
    name="puppetResources3",
    ends={
        Property(name="PuppetResource", type=cloudml_core_CloudMLElementWithProperties, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_CloudMLElementWithProperties4", type=PuppetResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dockerResources5: BinaryAssociation = BinaryAssociation(
    name="dockerResources5",
    ends={
        Property(name="DockerResource", type=cloudml_core_CloudMLElementWithProperties, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_CloudMLElementWithProperties6", type=DockerResource, multiplicity=Multiplicity(0, 9999))
    }
)
providers7: BinaryAssociation = BinaryAssociation(
    name="providers7",
    ends={
        Property(name="Provider", type=cloudml_core_CloudMLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_CloudMLModel", type=Provider, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
components8: BinaryAssociation = BinaryAssociation(
    name="components8",
    ends={
        Property(name="Component", type=cloudml_core_CloudMLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_CloudMLModel9", type=Component, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
clouds10: BinaryAssociation = BinaryAssociation(
    name="clouds10",
    ends={
        Property(name="Cloud", type=cloudml_core_CloudMLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_CloudMLModel11", type=Cloud, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
componentInstances12: BinaryAssociation = BinaryAssociation(
    name="componentInstances12",
    ends={
        Property(name="ComponentInstance", type=cloudml_core_CloudMLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_CloudMLModel13", type=ComponentInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
internalComponents14: BinaryAssociation = BinaryAssociation(
    name="internalComponents14",
    ends={
        Property(name="InternalComponent", type=cloudml_core_CloudMLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_CloudMLModel15", type=InternalComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
externalComponents16: BinaryAssociation = BinaryAssociation(
    name="externalComponents16",
    ends={
        Property(name="ExternalComponent", type=cloudml_core_CloudMLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_CloudMLModel17", type=ExternalComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
internalComponentInstances18: BinaryAssociation = BinaryAssociation(
    name="internalComponentInstances18",
    ends={
        Property(name="InternalComponentInstance", type=cloudml_core_CloudMLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_CloudMLModel19", type=InternalComponentInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
externalComponentInstances20: BinaryAssociation = BinaryAssociation(
    name="externalComponentInstances20",
    ends={
        Property(name="ExternalComponentInstance", type=cloudml_core_CloudMLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_CloudMLModel21", type=ExternalComponentInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
vms22: BinaryAssociation = BinaryAssociation(
    name="vms22",
    ends={
        Property(name="VM", type=cloudml_core_CloudMLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_CloudMLModel23", type=VM, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
vmInstances24: BinaryAssociation = BinaryAssociation(
    name="vmInstances24",
    ends={
        Property(name="VMInstance", type=cloudml_core_CloudMLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_CloudMLModel25", type=VMInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relationships26: BinaryAssociation = BinaryAssociation(
    name="relationships26",
    ends={
        Property(name="Relationship", type=cloudml_core_CloudMLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_CloudMLModel27", type=Relationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relationshipInstances28: BinaryAssociation = BinaryAssociation(
    name="relationshipInstances28",
    ends={
        Property(name="RelationshipInstance", type=cloudml_core_CloudMLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_CloudMLModel29", type=RelationshipInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
executesInstances30: BinaryAssociation = BinaryAssociation(
    name="executesInstances30",
    ends={
        Property(name="ExecuteInstance", type=cloudml_core_CloudMLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_CloudMLModel31", type=ExecuteInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourcePools32: BinaryAssociation = BinaryAssociation(
    name="resourcePools32",
    ends={
        Property(name="ResourcesPool", type=cloudml_core_CloudMLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_CloudMLModel33", type=ResourcesPool, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
provided34: BinaryAssociation = BinaryAssociation(
    name="provided34",
    ends={
        Property(name="VMPort", type=cloudml_core_VM, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_VM", type=VMPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedPorts35: BinaryAssociation = BinaryAssociation(
    name="providedPorts35",
    ends={
        Property(name="ProvidedPort", type=cloudml_core_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_Component", type=ProvidedPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedExecutionPlatforms36: BinaryAssociation = BinaryAssociation(
    name="providedExecutionPlatforms36",
    ends={
        Property(name="ProvidedExecutionPlatform", type=cloudml_core_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_Component37", type=ProvidedExecutionPlatform, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredPorts38: BinaryAssociation = BinaryAssociation(
    name="requiredPorts38",
    ends={
        Property(name="RequiredPort", type=cloudml_core_InternalComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_InternalComponent", type=RequiredPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
compositeInternalComponents39: BinaryAssociation = BinaryAssociation(
    name="compositeInternalComponents39",
    ends={
        Property(name="InternalComponent41", type=cloudml_core_InternalComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_InternalComponent40", type=InternalComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredExecutionPlatform42: BinaryAssociation = BinaryAssociation(
    name="requiredExecutionPlatform42",
    ends={
        Property(name="RequiredExecutionPlatform", type=cloudml_core_InternalComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_InternalComponent43", type=RequiredExecutionPlatform, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
component44: BinaryAssociation = BinaryAssociation(
    name="component44",
    ends={
        Property(name="Component45", type=cloudml_core_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_Port", type=Component, multiplicity=Multiplicity(1, 1))
    }
)
requiredPort46: BinaryAssociation = BinaryAssociation(
    name="requiredPort46",
    ends={
        Property(name="RequiredPort47", type=cloudml_core_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_Relationship", type=RequiredPort, multiplicity=Multiplicity(1, 1))
    }
)
providedPort48: BinaryAssociation = BinaryAssociation(
    name="providedPort48",
    ends={
        Property(name="ProvidedPort50", type=cloudml_core_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_Relationship49", type=ProvidedPort, multiplicity=Multiplicity(1, 1))
    }
)
requiredPortResource51: BinaryAssociation = BinaryAssociation(
    name="requiredPortResource51",
    ends={
        Property(name="Resource53", type=cloudml_core_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_Relationship52", type=Resource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
providedPortResource54: BinaryAssociation = BinaryAssociation(
    name="providedPortResource54",
    ends={
        Property(name="Resource56", type=cloudml_core_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_Relationship55", type=Resource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vmInstances57: BinaryAssociation = BinaryAssociation(
    name="vmInstances57",
    ends={
        Property(name="VMInstance58", type=cloudml_core_Cloud, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_Cloud", type=VMInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
provided59: BinaryAssociation = BinaryAssociation(
    name="provided59",
    ends={
        Property(name="VMPortInstance", type=cloudml_core_VMInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_VMInstance", type=VMPortInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type60: BinaryAssociation = BinaryAssociation(
    name="type60",
    ends={
        Property(name="VMPort61", type=cloudml_core_VMPortInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_VMPortInstance", type=VMPort, multiplicity=Multiplicity(1, 1))
    }
)
providedPortInstances62: BinaryAssociation = BinaryAssociation(
    name="providedPortInstances62",
    ends={
        Property(name="ProvidedPortInstance", type=cloudml_core_ComponentInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_ComponentInstance", type=ProvidedPortInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type63: BinaryAssociation = BinaryAssociation(
    name="type63",
    ends={
        Property(name="Component65", type=cloudml_core_ComponentInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_ComponentInstance64", type=Component, multiplicity=Multiplicity(1, 1))
    }
)
providedExecutionPlatformInstances66: BinaryAssociation = BinaryAssociation(
    name="providedExecutionPlatformInstances66",
    ends={
        Property(name="ProvidedExecutionPlatformInstance", type=cloudml_core_ComponentInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_ComponentInstance67", type=ProvidedExecutionPlatformInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredPortInstances68: BinaryAssociation = BinaryAssociation(
    name="requiredPortInstances68",
    ends={
        Property(name="RequiredPortInstance", type=cloudml_core_InternalComponentInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_InternalComponentInstance", type=RequiredPortInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredExecutionPlatformInstance69: BinaryAssociation = BinaryAssociation(
    name="requiredExecutionPlatformInstance69",
    ends={
        Property(name="RequiredExecutionPlatformInstance", type=cloudml_core_InternalComponentInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_InternalComponentInstance70", type=RequiredExecutionPlatformInstance, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type71: BinaryAssociation = BinaryAssociation(
    name="type71",
    ends={
        Property(name="Port", type=cloudml_core_PortInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_PortInstance", type=Port, multiplicity=Multiplicity(1, 1))
    }
)
type75: BinaryAssociation = BinaryAssociation(
    name="type75",
    ends={
        Property(name="Relationship76", type=cloudml_core_RelationshipInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_RelationshipInstance", type=Relationship, multiplicity=Multiplicity(1, 1))
    }
)
requiredPortInstance77: BinaryAssociation = BinaryAssociation(
    name="requiredPortInstance77",
    ends={
        Property(name="RequiredPortInstance79", type=cloudml_core_RelationshipInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_RelationshipInstance78", type=RequiredPortInstance, multiplicity=Multiplicity(1, 1))
    }
)
providedPortInstance80: BinaryAssociation = BinaryAssociation(
    name="providedPortInstance80",
    ends={
        Property(name="ProvidedPortInstance82", type=cloudml_core_RelationshipInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_RelationshipInstance81", type=ProvidedPortInstance, multiplicity=Multiplicity(1, 1))
    }
)
provider83: BinaryAssociation = BinaryAssociation(
    name="provider83",
    ends={
        Property(name="Provider84", type=cloudml_core_ExternalComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_ExternalComponent", type=Provider, multiplicity=Multiplicity(0, 1))
    }
)
provide85: BinaryAssociation = BinaryAssociation(
    name="provide85",
    ends={
        Property(name="VMPort87", type=cloudml_core_ExternalComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_ExternalComponent86", type=VMPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
provide88: BinaryAssociation = BinaryAssociation(
    name="provide88",
    ends={
        Property(name="VMPortInstance89", type=cloudml_core_ExternalComponentInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_ExternalComponentInstance", type=VMPortInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner90: BinaryAssociation = BinaryAssociation(
    name="owner90",
    ends={
        Property(name="Component91", type=cloudml_core_ExecutionPlatform, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_ExecutionPlatform", type=Component, multiplicity=Multiplicity(1, 1))
    }
)
owner92: BinaryAssociation = BinaryAssociation(
    name="owner92",
    ends={
        Property(name="ComponentInstance93", type=cloudml_core_ExecutionPlatformInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_ExecutionPlatformInstance", type=ComponentInstance, multiplicity=Multiplicity(1, 1))
    }
)
type94: BinaryAssociation = BinaryAssociation(
    name="type94",
    ends={
        Property(name="ExecutionPlatform", type=cloudml_core_ExecutionPlatformInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_ExecutionPlatformInstance95", type=ExecutionPlatform, multiplicity=Multiplicity(1, 1))
    }
)
offers96: BinaryAssociation = BinaryAssociation(
    name="offers96",
    ends={
        Property(name="Property97", type=cloudml_core_ProvidedExecutionPlatform, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_ProvidedExecutionPlatform", type=Property_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
componentInstance72: BinaryAssociation = BinaryAssociation(
    name="componentInstance72",
    ends={
        Property(name="ComponentInstance74", type=cloudml_core_PortInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_PortInstance73", type=ComponentInstance, multiplicity=Multiplicity(1, 1))
    }
)
demands98: BinaryAssociation = BinaryAssociation(
    name="demands98",
    ends={
        Property(name="Property99", type=cloudml_core_RequiredExecutionPlatform, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_RequiredExecutionPlatform", type=Property_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedExecutionPlatformInstance100: BinaryAssociation = BinaryAssociation(
    name="providedExecutionPlatformInstance100",
    ends={
        Property(name="ProvidedExecutionPlatformInstance101", type=cloudml_core_ExecuteInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_ExecuteInstance", type=ProvidedExecutionPlatformInstance, multiplicity=Multiplicity(1, 1))
    }
)
requiredExecutionPlatformInstance102: BinaryAssociation = BinaryAssociation(
    name="requiredExecutionPlatformInstance102",
    ends={
        Property(name="RequiredExecutionPlatformInstance104", type=cloudml_core_ExecuteInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_ExecuteInstance103", type=RequiredExecutionPlatformInstance, multiplicity=Multiplicity(1, 1))
    }
)
baseInstances105: BinaryAssociation = BinaryAssociation(
    name="baseInstances105",
    ends={
        Property(name="VMInstance106", type=cloudml_core_ResourcesPool, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_ResourcesPool", type=VMInstance, multiplicity=Multiplicity(1, 9999))
    }
)
replicats107: BinaryAssociation = BinaryAssociation(
    name="replicats107",
    ends={
        Property(name="VMInstance109", type=cloudml_core_ResourcesPool, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_ResourcesPool108", type=VMInstance, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_cloudml_core_Property_CloudMLElement = Generalization(general=CloudMLElement, specific=cloudml_core_Property)
gen_cloudml_core_CloudMLElementWithProperties_CloudMLElement = Generalization(general=CloudMLElement, specific=cloudml_core_CloudMLElementWithProperties)
gen_cloudml_core_Resource_CloudMLElementWithProperties = Generalization(general=CloudMLElementWithProperties, specific=cloudml_core_Resource)
gen_cloudml_core_CloudMLModel_CloudMLElementWithProperties = Generalization(general=CloudMLElementWithProperties, specific=cloudml_core_CloudMLModel)
gen_cloudml_core_VMPort_CloudMLElementWithProperties = Generalization(general=CloudMLElementWithProperties, specific=cloudml_core_VMPort)
gen_cloudml_core_Provider_CloudMLElementWithProperties = Generalization(general=CloudMLElementWithProperties, specific=cloudml_core_Provider)
gen_cloudml_core_Component_CloudMLElementWithProperties = Generalization(general=CloudMLElementWithProperties, specific=cloudml_core_Component)
gen_cloudml_core_InternalComponent_Component = Generalization(general=Component, specific=cloudml_core_InternalComponent)
gen_cloudml_core_Port_CloudMLElementWithProperties = Generalization(general=CloudMLElementWithProperties, specific=cloudml_core_Port)
gen_cloudml_core_VM_ExternalComponent = Generalization(general=ExternalComponent, specific=cloudml_core_VM)
gen_cloudml_core_RequiredPort_Port = Generalization(general=Port, specific=cloudml_core_RequiredPort)
gen_cloudml_core_ProvidedPort_Port = Generalization(general=Port, specific=cloudml_core_ProvidedPort)
gen_cloudml_core_Relationship_CloudMLElementWithProperties = Generalization(general=CloudMLElementWithProperties, specific=cloudml_core_Relationship)
gen_cloudml_core_Cloud_CloudMLElementWithProperties = Generalization(general=CloudMLElementWithProperties, specific=cloudml_core_Cloud)
gen_cloudml_core_VMInstance_ExternalComponentInstance = Generalization(general=ExternalComponentInstance, specific=cloudml_core_VMInstance)
gen_cloudml_core_VMPortInstance_CloudMLElementWithProperties = Generalization(general=CloudMLElementWithProperties, specific=cloudml_core_VMPortInstance)
gen_cloudml_core_ComponentInstance_CloudMLElementWithProperties = Generalization(general=CloudMLElementWithProperties, specific=cloudml_core_ComponentInstance)
gen_cloudml_core_InternalComponentInstance_ComponentInstance = Generalization(general=ComponentInstance, specific=cloudml_core_InternalComponentInstance)
gen_cloudml_core_PortInstance_CloudMLElementWithProperties = Generalization(general=CloudMLElementWithProperties, specific=cloudml_core_PortInstance)
gen_cloudml_core_RequiredExecutionPlatform_ExecutionPlatform = Generalization(general=ExecutionPlatform, specific=cloudml_core_RequiredExecutionPlatform)
gen_cloudml_core_RequiredPortInstance_PortInstance = Generalization(general=PortInstance, specific=cloudml_core_RequiredPortInstance)
gen_cloudml_core_ProvidedPortInstance_PortInstance = Generalization(general=PortInstance, specific=cloudml_core_ProvidedPortInstance)
gen_cloudml_core_RelationshipInstance_CloudMLElementWithProperties = Generalization(general=CloudMLElementWithProperties, specific=cloudml_core_RelationshipInstance)
gen_cloudml_core_ExternalComponent_Component = Generalization(general=Component, specific=cloudml_core_ExternalComponent)
gen_cloudml_core_ExternalComponentInstance_ComponentInstance = Generalization(general=ComponentInstance, specific=cloudml_core_ExternalComponentInstance)
gen_cloudml_core_ExecutionPlatform_CloudMLElementWithProperties = Generalization(general=CloudMLElementWithProperties, specific=cloudml_core_ExecutionPlatform)
gen_cloudml_core_ExecutionPlatformInstance_CloudMLElementWithProperties = Generalization(general=CloudMLElementWithProperties, specific=cloudml_core_ExecutionPlatformInstance)
gen_cloudml_core_ProvidedExecutionPlatform_ExecutionPlatform = Generalization(general=ExecutionPlatform, specific=cloudml_core_ProvidedExecutionPlatform)
gen_cloudml_core_ProvidedExecutionPlatformInstance_ExecutionPlatformInstance = Generalization(general=ExecutionPlatformInstance, specific=cloudml_core_ProvidedExecutionPlatformInstance)
gen_cloudml_core_RequiredExecutionPlatformInstance_ExecutionPlatformInstance = Generalization(general=ExecutionPlatformInstance, specific=cloudml_core_RequiredExecutionPlatformInstance)
gen_cloudml_core_ExecuteInstance_CloudMLElementWithProperties = Generalization(general=CloudMLElementWithProperties, specific=cloudml_core_ExecuteInstance)
gen_cloudml_core_PuppetResource_Resource = Generalization(general=Resource, specific=cloudml_core_PuppetResource)
gen_cloudml_core_ResourcesPool_CloudMLElementWithProperties = Generalization(general=CloudMLElementWithProperties, specific=cloudml_core_ResourcesPool)
gen_cloudml_core_DockerResource_Resource = Generalization(general=Resource, specific=cloudml_core_DockerResource)

# Domain Model
domain_model = DomainModel(
    name="cloudml",
    types={cloudml_core_CloudMLElement, cloudml_core_Property, CloudMLElement, cloudml_core_CloudMLElementWithProperties, Property_, Resource, PuppetResource, DockerResource, cloudml_core_Resource, CloudMLElementWithProperties, cloudml_core_CloudMLModel, Provider, Component, Cloud, ComponentInstance, InternalComponent, ExternalComponent, InternalComponentInstance, ExternalComponentInstance, VM, VMInstance, Relationship, RelationshipInstance, ExecuteInstance, ResourcesPool, VMPort, cloudml_core_VMPort, cloudml_core_Provider, cloudml_core_Component, ProvidedPort, ProvidedExecutionPlatform, cloudml_core_InternalComponent, RequiredPort, RequiredExecutionPlatform, cloudml_core_Port, cloudml_core_VM, cloudml_core_RequiredPort, Port, cloudml_core_ProvidedPort, cloudml_core_Relationship, cloudml_core_Cloud, cloudml_core_VMInstance, VMPortInstance, cloudml_core_VMPortInstance, cloudml_core_ComponentInstance, ProvidedPortInstance, ProvidedExecutionPlatformInstance, cloudml_core_InternalComponentInstance, RequiredPortInstance, RequiredExecutionPlatformInstance, cloudml_core_PortInstance, cloudml_core_RequiredPortInstance, PortInstance, cloudml_core_ProvidedPortInstance, cloudml_core_RelationshipInstance, cloudml_core_ExternalComponent, cloudml_core_ExternalComponentInstance, cloudml_core_ExecutionPlatform, cloudml_core_ExecutionPlatformInstance, ExecutionPlatform, cloudml_core_ProvidedExecutionPlatform, cloudml_core_ProvidedExecutionPlatformInstance, ExecutionPlatformInstance, cloudml_core_RequiredExecutionPlatform, cloudml_core_RequiredExecutionPlatformInstance, cloudml_core_ExecuteInstance, cloudml_core_PuppetResource, cloudml_core_ResourcesPool, cloudml_core_DockerResource},
    associations={properties0, resources1, puppetResources3, dockerResources5, providers7, components8, clouds10, componentInstances12, internalComponents14, externalComponents16, internalComponentInstances18, externalComponentInstances20, vms22, vmInstances24, relationships26, relationshipInstances28, executesInstances30, resourcePools32, provided34, providedPorts35, providedExecutionPlatforms36, requiredPorts38, compositeInternalComponents39, requiredExecutionPlatform42, component44, requiredPort46, providedPort48, requiredPortResource51, providedPortResource54, vmInstances57, provided59, type60, providedPortInstances62, type63, providedExecutionPlatformInstances66, requiredPortInstances68, requiredExecutionPlatformInstance69, type71, type75, requiredPortInstance77, providedPortInstance80, provider83, provide85, provide88, owner90, owner92, type94, offers96, componentInstance72, demands98, providedExecutionPlatformInstance100, requiredExecutionPlatformInstance102, baseInstances105, replicats107},
    generalizations={gen_cloudml_core_Property_CloudMLElement, gen_cloudml_core_CloudMLElementWithProperties_CloudMLElement, gen_cloudml_core_Resource_CloudMLElementWithProperties, gen_cloudml_core_CloudMLModel_CloudMLElementWithProperties, gen_cloudml_core_VMPort_CloudMLElementWithProperties, gen_cloudml_core_Provider_CloudMLElementWithProperties, gen_cloudml_core_Component_CloudMLElementWithProperties, gen_cloudml_core_InternalComponent_Component, gen_cloudml_core_Port_CloudMLElementWithProperties, gen_cloudml_core_VM_ExternalComponent, gen_cloudml_core_RequiredPort_Port, gen_cloudml_core_ProvidedPort_Port, gen_cloudml_core_Relationship_CloudMLElementWithProperties, gen_cloudml_core_Cloud_CloudMLElementWithProperties, gen_cloudml_core_VMInstance_ExternalComponentInstance, gen_cloudml_core_VMPortInstance_CloudMLElementWithProperties, gen_cloudml_core_ComponentInstance_CloudMLElementWithProperties, gen_cloudml_core_InternalComponentInstance_ComponentInstance, gen_cloudml_core_PortInstance_CloudMLElementWithProperties, gen_cloudml_core_RequiredExecutionPlatform_ExecutionPlatform, gen_cloudml_core_RequiredPortInstance_PortInstance, gen_cloudml_core_ProvidedPortInstance_PortInstance, gen_cloudml_core_RelationshipInstance_CloudMLElementWithProperties, gen_cloudml_core_ExternalComponent_Component, gen_cloudml_core_ExternalComponentInstance_ComponentInstance, gen_cloudml_core_ExecutionPlatform_CloudMLElementWithProperties, gen_cloudml_core_ExecutionPlatformInstance_CloudMLElementWithProperties, gen_cloudml_core_ProvidedExecutionPlatform_ExecutionPlatform, gen_cloudml_core_ProvidedExecutionPlatformInstance_ExecutionPlatformInstance, gen_cloudml_core_RequiredExecutionPlatformInstance_ExecutionPlatformInstance, gen_cloudml_core_ExecuteInstance_CloudMLElementWithProperties, gen_cloudml_core_PuppetResource_Resource, gen_cloudml_core_ResourcesPool_CloudMLElementWithProperties, gen_cloudml_core_DockerResource_Resource},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)