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
cloudml_CloudMLElement = Class(name="cloudml::CloudMLElement", is_abstract=True)
cloudml_Property = Class(name="cloudml::Property")
CloudMLElement = Class(name="CloudMLElement")
cloudml_CloudMLElementWithProperties = Class(name="cloudml::CloudMLElementWithProperties", is_abstract=True)
cloudml_Resource = Class(name="cloudml::Resource")
cloudml_PuppetResource = Class(name="cloudml::PuppetResource")
CloudMLElementWithProperties = Class(name="CloudMLElementWithProperties")
cloudml_Component = Class(name="cloudml::Component", is_abstract=True)
cloudml_Cloud = Class(name="cloudml::Cloud")
cloudml_ComponentInstance = Class(name="cloudml::ComponentInstance", is_abstract=True)
cloudml_InternalComponent = Class(name="cloudml::InternalComponent")
cloudml_ExternalComponent = Class(name="cloudml::ExternalComponent")
cloudml_InternalComponentInstance = Class(name="cloudml::InternalComponentInstance")
cloudml_ExternalComponentInstance = Class(name="cloudml::ExternalComponentInstance")
cloudml_VM = Class(name="cloudml::VM")
cloudml_VMInstance = Class(name="cloudml::VMInstance")
cloudml_Relationship = Class(name="cloudml::Relationship")
cloudml_RelationshipInstance = Class(name="cloudml::RelationshipInstance")
cloudml_ExecuteInstance = Class(name="cloudml::ExecuteInstance")
ExternalComponent = Class(name="ExternalComponent")
cloudml_VMPort = Class(name="cloudml::VMPort")
cloudml_CloudMLModel = Class(name="cloudml::CloudMLModel")
cloudml_Provider = Class(name="cloudml::Provider")
cloudml_ProvidedPort = Class(name="cloudml::ProvidedPort")
cloudml_ProvidedExecutionPlatform = Class(name="cloudml::ProvidedExecutionPlatform")
Component = Class(name="Component")
cloudml_RequiredPort = Class(name="cloudml::RequiredPort")
cloudml_RequiredExecutionPlatform = Class(name="cloudml::RequiredExecutionPlatform")
cloudml_Port = Class(name="cloudml::Port", is_abstract=True)
Port = Class(name="Port")
ExternalComponentInstance = Class(name="ExternalComponentInstance")
cloudml_VMPortInstance = Class(name="cloudml::VMPortInstance")
cloudml_ProvidedPortInstance = Class(name="cloudml::ProvidedPortInstance")
cloudml_ProvidedExecutionPlatformInstance = Class(name="cloudml::ProvidedExecutionPlatformInstance")
ComponentInstance = Class(name="ComponentInstance")
cloudml_RequiredPortInstance = Class(name="cloudml::RequiredPortInstance")
cloudml_RequiredExecutionPlatformInstance = Class(name="cloudml::RequiredExecutionPlatformInstance")
cloudml_PortInstance = Class(name="cloudml::PortInstance")
cloudml_ExecutionPlatform = Class(name="cloudml::ExecutionPlatform", is_abstract=True)
cloudml_ExecutionPlatformInstance = Class(name="cloudml::ExecutionPlatformInstance", is_abstract=True)
ExecutionPlatform = Class(name="ExecutionPlatform")
PortInstance = Class(name="PortInstance")
Resource = Class(name="Resource")
ExecutionPlatformInstance = Class(name="ExecutionPlatformInstance")

# cloudml_CloudMLElement class attributes and methods
cloudml_CloudMLElement_name: Property = Property(name="name", type=StringType)
cloudml_CloudMLElement.attributes={cloudml_CloudMLElement_name}

# cloudml_Property class attributes and methods
cloudml_Property_value: Property = Property(name="value", type=StringType)
cloudml_Property.attributes={cloudml_Property_value}

# CloudMLElement class attributes and methods

# cloudml_CloudMLElementWithProperties class attributes and methods

# cloudml_Resource class attributes and methods
cloudml_Resource_downloadCommand: Property = Property(name="downloadCommand", type=StringType)
cloudml_Resource_uploadCommand: Property = Property(name="uploadCommand", type=StringType)
cloudml_Resource_installCommand: Property = Property(name="installCommand", type=StringType)
cloudml_Resource_configureCommand: Property = Property(name="configureCommand", type=StringType)
cloudml_Resource_startCommand: Property = Property(name="startCommand", type=StringType)
cloudml_Resource_stopCommand: Property = Property(name="stopCommand", type=StringType)
cloudml_Resource_requireCredentials: Property = Property(name="requireCredentials", type=BooleanType)
cloudml_Resource_executeLocally: Property = Property(name="executeLocally", type=BooleanType)
cloudml_Resource.attributes={cloudml_Resource_stopCommand, cloudml_Resource_uploadCommand, cloudml_Resource_configureCommand, cloudml_Resource_startCommand, cloudml_Resource_executeLocally, cloudml_Resource_installCommand, cloudml_Resource_downloadCommand, cloudml_Resource_requireCredentials}

# cloudml_PuppetResource class attributes and methods
cloudml_PuppetResource_masterEndpoint: Property = Property(name="masterEndpoint", type=StringType)
cloudml_PuppetResource_repositoryEndpoint: Property = Property(name="repositoryEndpoint", type=StringType)
cloudml_PuppetResource_configureHostnameCommand: Property = Property(name="configureHostnameCommand", type=StringType)
cloudml_PuppetResource_username: Property = Property(name="username", type=StringType)
cloudml_PuppetResource_repositoryKey: Property = Property(name="repositoryKey", type=StringType)
cloudml_PuppetResource_configurationFile: Property = Property(name="configurationFile", type=StringType)
cloudml_PuppetResource_manifestEntry: Property = Property(name="manifestEntry", type=StringType)
cloudml_PuppetResource.attributes={cloudml_PuppetResource_username, cloudml_PuppetResource_manifestEntry, cloudml_PuppetResource_repositoryEndpoint, cloudml_PuppetResource_configureHostnameCommand, cloudml_PuppetResource_masterEndpoint, cloudml_PuppetResource_configurationFile, cloudml_PuppetResource_repositoryKey}

# CloudMLElementWithProperties class attributes and methods

# cloudml_Component class attributes and methods

# cloudml_Cloud class attributes and methods

# cloudml_ComponentInstance class attributes and methods

# cloudml_InternalComponent class attributes and methods

# cloudml_ExternalComponent class attributes and methods
cloudml_ExternalComponent_endPoint: Property = Property(name="endPoint", type=StringType)
cloudml_ExternalComponent_login: Property = Property(name="login", type=StringType)
cloudml_ExternalComponent_passwd: Property = Property(name="passwd", type=StringType)
cloudml_ExternalComponent_location: Property = Property(name="location", type=StringType)
cloudml_ExternalComponent_serviceType: Property = Property(name="serviceType", type=StringType)
cloudml_ExternalComponent_Region: Property = Property(name="Region", type=StringType)
cloudml_ExternalComponent.attributes={cloudml_ExternalComponent_serviceType, cloudml_ExternalComponent_passwd, cloudml_ExternalComponent_Region, cloudml_ExternalComponent_location, cloudml_ExternalComponent_endPoint, cloudml_ExternalComponent_login}

# cloudml_InternalComponentInstance class attributes and methods

# cloudml_ExternalComponentInstance class attributes and methods
cloudml_ExternalComponentInstance_ips: Property = Property(name="ips", type=StringType)
cloudml_ExternalComponentInstance.attributes={cloudml_ExternalComponentInstance_ips}

# cloudml_VM class attributes and methods
cloudml_VM_minRam: Property = Property(name="minRam", type=IntegerType)
cloudml_VM_maxRam: Property = Property(name="maxRam", type=IntegerType)
cloudml_VM_minCores: Property = Property(name="minCores", type=IntegerType)
cloudml_VM_maxCores: Property = Property(name="maxCores", type=IntegerType)
cloudml_VM_minStorage: Property = Property(name="minStorage", type=IntegerType)
cloudml_VM_maxStorage: Property = Property(name="maxStorage", type=IntegerType)
cloudml_VM_os: Property = Property(name="os", type=StringType)
cloudml_VM_is64os: Property = Property(name="is64os", type=BooleanType)
cloudml_VM_imageId: Property = Property(name="imageId", type=StringType)
cloudml_VM_securityGroup: Property = Property(name="securityGroup", type=StringType)
cloudml_VM_sshKey: Property = Property(name="sshKey", type=StringType)
cloudml_VM_privateKey: Property = Property(name="privateKey", type=StringType)
cloudml_VM_groupName: Property = Property(name="groupName", type=StringType)
cloudml_VM_providerSpecificTypeName: Property = Property(name="providerSpecificTypeName", type=StringType)
cloudml_VM.attributes={cloudml_VM_maxStorage, cloudml_VM_sshKey, cloudml_VM_privateKey, cloudml_VM_groupName, cloudml_VM_is64os, cloudml_VM_securityGroup, cloudml_VM_os, cloudml_VM_imageId, cloudml_VM_minStorage, cloudml_VM_minRam, cloudml_VM_maxRam, cloudml_VM_minCores, cloudml_VM_providerSpecificTypeName, cloudml_VM_maxCores}

# cloudml_VMInstance class attributes and methods
cloudml_VMInstance_publicAddress: Property = Property(name="publicAddress", type=StringType)
cloudml_VMInstance_id: Property = Property(name="id", type=StringType)
cloudml_VMInstance.attributes={cloudml_VMInstance_id, cloudml_VMInstance_publicAddress}

# cloudml_Relationship class attributes and methods

# cloudml_RelationshipInstance class attributes and methods

# cloudml_ExecuteInstance class attributes and methods

# ExternalComponent class attributes and methods

# cloudml_VMPort class attributes and methods

# cloudml_CloudMLModel class attributes and methods

# cloudml_Provider class attributes and methods
cloudml_Provider_credentials: Property = Property(name="credentials", type=StringType)
cloudml_Provider.attributes={cloudml_Provider_credentials}

# cloudml_ProvidedPort class attributes and methods

# cloudml_ProvidedExecutionPlatform class attributes and methods

# Component class attributes and methods

# cloudml_RequiredPort class attributes and methods
cloudml_RequiredPort_isMandatory: Property = Property(name="isMandatory", type=BooleanType)
cloudml_RequiredPort.attributes={cloudml_RequiredPort_isMandatory}

# cloudml_RequiredExecutionPlatform class attributes and methods

# cloudml_Port class attributes and methods
cloudml_Port_isLocal: Property = Property(name="isLocal", type=BooleanType)
cloudml_Port_portNumber: Property = Property(name="portNumber", type=IntegerType)
cloudml_Port.attributes={cloudml_Port_isLocal, cloudml_Port_portNumber}

# Port class attributes and methods

# ExternalComponentInstance class attributes and methods

# cloudml_VMPortInstance class attributes and methods

# cloudml_ProvidedPortInstance class attributes and methods

# cloudml_ProvidedExecutionPlatformInstance class attributes and methods

# ComponentInstance class attributes and methods

# cloudml_RequiredPortInstance class attributes and methods

# cloudml_RequiredExecutionPlatformInstance class attributes and methods

# cloudml_PortInstance class attributes and methods

# cloudml_ExecutionPlatform class attributes and methods

# cloudml_ExecutionPlatformInstance class attributes and methods

# ExecutionPlatform class attributes and methods

# PortInstance class attributes and methods

# Resource class attributes and methods

# ExecutionPlatformInstance class attributes and methods

# Relationships
properties0: BinaryAssociation = BinaryAssociation(
    name="properties0",
    ends={
        Property(name="cloudml_Property", type=cloudml_CloudMLElementWithProperties, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_CloudMLElementWithProperties", type=cloudml_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resources1: BinaryAssociation = BinaryAssociation(
    name="resources1",
    ends={
        Property(name="cloudml_Resource", type=cloudml_CloudMLElementWithProperties, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_CloudMLElementWithProperties2", type=cloudml_Resource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
puppetResources3: BinaryAssociation = BinaryAssociation(
    name="puppetResources3",
    ends={
        Property(name="cloudml_PuppetResource", type=cloudml_CloudMLElementWithProperties, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_CloudMLElementWithProperties4", type=cloudml_PuppetResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
components6: BinaryAssociation = BinaryAssociation(
    name="components6",
    ends={
        Property(name="cloudml_Component", type=cloudml_CloudMLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_CloudMLModel7", type=cloudml_Component, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
clouds8: BinaryAssociation = BinaryAssociation(
    name="clouds8",
    ends={
        Property(name="cloudml_Cloud", type=cloudml_CloudMLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_CloudMLModel9", type=cloudml_Cloud, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
componentInstances10: BinaryAssociation = BinaryAssociation(
    name="componentInstances10",
    ends={
        Property(name="cloudml_ComponentInstance", type=cloudml_CloudMLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_CloudMLModel11", type=cloudml_ComponentInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
internalComponents12: BinaryAssociation = BinaryAssociation(
    name="internalComponents12",
    ends={
        Property(name="cloudml_InternalComponent", type=cloudml_CloudMLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_CloudMLModel13", type=cloudml_InternalComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
externalComponents14: BinaryAssociation = BinaryAssociation(
    name="externalComponents14",
    ends={
        Property(name="cloudml_ExternalComponent", type=cloudml_CloudMLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_CloudMLModel15", type=cloudml_ExternalComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
internalComponentInstances16: BinaryAssociation = BinaryAssociation(
    name="internalComponentInstances16",
    ends={
        Property(name="cloudml_InternalComponentInstance", type=cloudml_CloudMLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_CloudMLModel17", type=cloudml_InternalComponentInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
externalComponentInstances18: BinaryAssociation = BinaryAssociation(
    name="externalComponentInstances18",
    ends={
        Property(name="cloudml_ExternalComponentInstance", type=cloudml_CloudMLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_CloudMLModel19", type=cloudml_ExternalComponentInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
vms20: BinaryAssociation = BinaryAssociation(
    name="vms20",
    ends={
        Property(name="cloudml_VM", type=cloudml_CloudMLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_CloudMLModel21", type=cloudml_VM, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
vmInstances22: BinaryAssociation = BinaryAssociation(
    name="vmInstances22",
    ends={
        Property(name="cloudml_VMInstance", type=cloudml_CloudMLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_CloudMLModel23", type=cloudml_VMInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relationships24: BinaryAssociation = BinaryAssociation(
    name="relationships24",
    ends={
        Property(name="cloudml_Relationship", type=cloudml_CloudMLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_CloudMLModel25", type=cloudml_Relationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relationshipInstances26: BinaryAssociation = BinaryAssociation(
    name="relationshipInstances26",
    ends={
        Property(name="cloudml_RelationshipInstance", type=cloudml_CloudMLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_CloudMLModel27", type=cloudml_RelationshipInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
executesInstances28: BinaryAssociation = BinaryAssociation(
    name="executesInstances28",
    ends={
        Property(name="cloudml_ExecuteInstance", type=cloudml_CloudMLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_CloudMLModel29", type=cloudml_ExecuteInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
provided30: BinaryAssociation = BinaryAssociation(
    name="provided30",
    ends={
        Property(name="cloudml_VMPort", type=cloudml_VM, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_VM31", type=cloudml_VMPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providers5: BinaryAssociation = BinaryAssociation(
    name="providers5",
    ends={
        Property(name="cloudml_Provider", type=cloudml_CloudMLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_CloudMLModel", type=cloudml_Provider, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedPorts32: BinaryAssociation = BinaryAssociation(
    name="providedPorts32",
    ends={
        Property(name="cloudml_ProvidedPort", type=cloudml_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_Component33", type=cloudml_ProvidedPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedExecutionPlatforms34: BinaryAssociation = BinaryAssociation(
    name="providedExecutionPlatforms34",
    ends={
        Property(name="cloudml_ProvidedExecutionPlatform", type=cloudml_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_Component35", type=cloudml_ProvidedExecutionPlatform, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredPorts36: BinaryAssociation = BinaryAssociation(
    name="requiredPorts36",
    ends={
        Property(name="cloudml_RequiredPort", type=cloudml_InternalComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_InternalComponent37", type=cloudml_RequiredPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
compositeInternalComponents39: BinaryAssociation = BinaryAssociation(
    name="compositeInternalComponents39",
    ends={
        Property(name="cloudml_InternalComponent40", type=cloudml_InternalComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_InternalComponent38", type=cloudml_InternalComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredExecutionPlatform41: BinaryAssociation = BinaryAssociation(
    name="requiredExecutionPlatform41",
    ends={
        Property(name="cloudml_RequiredExecutionPlatform", type=cloudml_InternalComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_InternalComponent42", type=cloudml_RequiredExecutionPlatform, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
component43: BinaryAssociation = BinaryAssociation(
    name="component43",
    ends={
        Property(name="cloudml_Component44", type=cloudml_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_Port", type=cloudml_Component, multiplicity=Multiplicity(1, 1))
    }
)
requiredPort45: BinaryAssociation = BinaryAssociation(
    name="requiredPort45",
    ends={
        Property(name="cloudml_RequiredPort47", type=cloudml_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_Relationship46", type=cloudml_RequiredPort, multiplicity=Multiplicity(1, 1))
    }
)
providedPort48: BinaryAssociation = BinaryAssociation(
    name="providedPort48",
    ends={
        Property(name="cloudml_ProvidedPort50", type=cloudml_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_Relationship49", type=cloudml_ProvidedPort, multiplicity=Multiplicity(1, 1))
    }
)
vmInstances57: BinaryAssociation = BinaryAssociation(
    name="vmInstances57",
    ends={
        Property(name="cloudml_VMInstance59", type=cloudml_Cloud, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_Cloud58", type=cloudml_VMInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
provided60: BinaryAssociation = BinaryAssociation(
    name="provided60",
    ends={
        Property(name="cloudml_VMPortInstance", type=cloudml_VMInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_VMInstance61", type=cloudml_VMPortInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type62: BinaryAssociation = BinaryAssociation(
    name="type62",
    ends={
        Property(name="cloudml_VMPort64", type=cloudml_VMPortInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_VMPortInstance63", type=cloudml_VMPort, multiplicity=Multiplicity(1, 1))
    }
)
providedPortInstances65: BinaryAssociation = BinaryAssociation(
    name="providedPortInstances65",
    ends={
        Property(name="cloudml_ProvidedPortInstance", type=cloudml_ComponentInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_ComponentInstance66", type=cloudml_ProvidedPortInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type67: BinaryAssociation = BinaryAssociation(
    name="type67",
    ends={
        Property(name="cloudml_Component69", type=cloudml_ComponentInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_ComponentInstance68", type=cloudml_Component, multiplicity=Multiplicity(1, 1))
    }
)
providedExecutionPlatformInstances70: BinaryAssociation = BinaryAssociation(
    name="providedExecutionPlatformInstances70",
    ends={
        Property(name="cloudml_ProvidedExecutionPlatformInstance", type=cloudml_ComponentInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_ComponentInstance71", type=cloudml_ProvidedExecutionPlatformInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredPortInstances72: BinaryAssociation = BinaryAssociation(
    name="requiredPortInstances72",
    ends={
        Property(name="cloudml_RequiredPortInstance", type=cloudml_InternalComponentInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_InternalComponentInstance73", type=cloudml_RequiredPortInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredExecutionPlatformInstance74: BinaryAssociation = BinaryAssociation(
    name="requiredExecutionPlatformInstance74",
    ends={
        Property(name="cloudml_RequiredExecutionPlatformInstance", type=cloudml_InternalComponentInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_InternalComponentInstance75", type=cloudml_RequiredExecutionPlatformInstance, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type76: BinaryAssociation = BinaryAssociation(
    name="type76",
    ends={
        Property(name="cloudml_Port77", type=cloudml_PortInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_PortInstance", type=cloudml_Port, multiplicity=Multiplicity(1, 1))
    }
)
componentInstance78: BinaryAssociation = BinaryAssociation(
    name="componentInstance78",
    ends={
        Property(name="cloudml_ComponentInstance80", type=cloudml_PortInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_PortInstance79", type=cloudml_ComponentInstance, multiplicity=Multiplicity(1, 1))
    }
)
requiredPortResource51: BinaryAssociation = BinaryAssociation(
    name="requiredPortResource51",
    ends={
        Property(name="cloudml_Resource53", type=cloudml_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_Relationship52", type=cloudml_Resource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
providedPortResource54: BinaryAssociation = BinaryAssociation(
    name="providedPortResource54",
    ends={
        Property(name="cloudml_Resource56", type=cloudml_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_Relationship55", type=cloudml_Resource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type81: BinaryAssociation = BinaryAssociation(
    name="type81",
    ends={
        Property(name="cloudml_RelationshipInstance82", type=cloudml_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_Relationship83", type=cloudml_RelationshipInstance, multiplicity=Multiplicity(1, 1))
    }
)
requiredPortInstance84: BinaryAssociation = BinaryAssociation(
    name="requiredPortInstance84",
    ends={
        Property(name="cloudml_RequiredPortInstance86", type=cloudml_RelationshipInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_RelationshipInstance85", type=cloudml_RequiredPortInstance, multiplicity=Multiplicity(1, 1))
    }
)
providedPortInstance87: BinaryAssociation = BinaryAssociation(
    name="providedPortInstance87",
    ends={
        Property(name="cloudml_ProvidedPortInstance89", type=cloudml_RelationshipInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_RelationshipInstance88", type=cloudml_ProvidedPortInstance, multiplicity=Multiplicity(1, 1))
    }
)
provider90: BinaryAssociation = BinaryAssociation(
    name="provider90",
    ends={
        Property(name="cloudml_Provider92", type=cloudml_ExternalComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_ExternalComponent91", type=cloudml_Provider, multiplicity=Multiplicity(0, 1))
    }
)
provide93: BinaryAssociation = BinaryAssociation(
    name="provide93",
    ends={
        Property(name="cloudml_VMPort95", type=cloudml_ExternalComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_ExternalComponent94", type=cloudml_VMPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
provide96: BinaryAssociation = BinaryAssociation(
    name="provide96",
    ends={
        Property(name="cloudml_VMPortInstance98", type=cloudml_ExternalComponentInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_ExternalComponentInstance97", type=cloudml_VMPortInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner99: BinaryAssociation = BinaryAssociation(
    name="owner99",
    ends={
        Property(name="cloudml_Component100", type=cloudml_ExecutionPlatform, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_ExecutionPlatform", type=cloudml_Component, multiplicity=Multiplicity(1, 1))
    }
)
owner101: BinaryAssociation = BinaryAssociation(
    name="owner101",
    ends={
        Property(name="cloudml_ComponentInstance102", type=cloudml_ExecutionPlatformInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_ExecutionPlatformInstance", type=cloudml_ComponentInstance, multiplicity=Multiplicity(1, 1))
    }
)
type103: BinaryAssociation = BinaryAssociation(
    name="type103",
    ends={
        Property(name="cloudml_ExecutionPlatform105", type=cloudml_ExecutionPlatformInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_ExecutionPlatformInstance104", type=cloudml_ExecutionPlatform, multiplicity=Multiplicity(1, 1))
    }
)
demands109: BinaryAssociation = BinaryAssociation(
    name="demands109",
    ends={
        Property(name="cloudml_Property111", type=cloudml_RequiredExecutionPlatform, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_RequiredExecutionPlatform110", type=cloudml_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedExecutionPlatformInstance112: BinaryAssociation = BinaryAssociation(
    name="providedExecutionPlatformInstance112",
    ends={
        Property(name="cloudml_ProvidedExecutionPlatformInstance114", type=cloudml_ExecuteInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_ExecuteInstance113", type=cloudml_ProvidedExecutionPlatformInstance, multiplicity=Multiplicity(1, 1))
    }
)
requiredExecutionPlatformInstance115: BinaryAssociation = BinaryAssociation(
    name="requiredExecutionPlatformInstance115",
    ends={
        Property(name="cloudml_RequiredExecutionPlatformInstance117", type=cloudml_ExecuteInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_ExecuteInstance116", type=cloudml_RequiredExecutionPlatformInstance, multiplicity=Multiplicity(1, 1))
    }
)
offers106: BinaryAssociation = BinaryAssociation(
    name="offers106",
    ends={
        Property(name="cloudml_Property108", type=cloudml_ProvidedExecutionPlatform, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_ProvidedExecutionPlatform107", type=cloudml_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_cloudml_Property_CloudMLElement = Generalization(general=CloudMLElement, specific=cloudml_Property)
gen_cloudml_CloudMLElementWithProperties_CloudMLElement = Generalization(general=CloudMLElement, specific=cloudml_CloudMLElementWithProperties)
gen_cloudml_Resource_CloudMLElementWithProperties = Generalization(general=CloudMLElementWithProperties, specific=cloudml_Resource)
gen_cloudml_VM_ExternalComponent = Generalization(general=ExternalComponent, specific=cloudml_VM)
gen_cloudml_CloudMLModel_CloudMLElementWithProperties = Generalization(general=CloudMLElementWithProperties, specific=cloudml_CloudMLModel)
gen_cloudml_VMPort_CloudMLElementWithProperties = Generalization(general=CloudMLElementWithProperties, specific=cloudml_VMPort)
gen_cloudml_Provider_CloudMLElementWithProperties = Generalization(general=CloudMLElementWithProperties, specific=cloudml_Provider)
gen_cloudml_Component_CloudMLElementWithProperties = Generalization(general=CloudMLElementWithProperties, specific=cloudml_Component)
gen_cloudml_InternalComponent_Component = Generalization(general=Component, specific=cloudml_InternalComponent)
gen_cloudml_Port_CloudMLElementWithProperties = Generalization(general=CloudMLElementWithProperties, specific=cloudml_Port)
gen_cloudml_RequiredPort_Port = Generalization(general=Port, specific=cloudml_RequiredPort)
gen_cloudml_ProvidedPort_Port = Generalization(general=Port, specific=cloudml_ProvidedPort)
gen_cloudml_Relationship_CloudMLElementWithProperties = Generalization(general=CloudMLElementWithProperties, specific=cloudml_Relationship)
gen_cloudml_Cloud_CloudMLElementWithProperties = Generalization(general=CloudMLElementWithProperties, specific=cloudml_Cloud)
gen_cloudml_VMInstance_ExternalComponentInstance = Generalization(general=ExternalComponentInstance, specific=cloudml_VMInstance)
gen_cloudml_VMPortInstance_CloudMLElementWithProperties = Generalization(general=CloudMLElementWithProperties, specific=cloudml_VMPortInstance)
gen_cloudml_ComponentInstance_CloudMLElementWithProperties = Generalization(general=CloudMLElementWithProperties, specific=cloudml_ComponentInstance)
gen_cloudml_InternalComponentInstance_ComponentInstance = Generalization(general=ComponentInstance, specific=cloudml_InternalComponentInstance)
gen_cloudml_PortInstance_CloudMLElementWithProperties = Generalization(general=CloudMLElementWithProperties, specific=cloudml_PortInstance)
gen_cloudml_ExternalComponent_Component = Generalization(general=Component, specific=cloudml_ExternalComponent)
gen_cloudml_ExternalComponentInstance_ComponentInstance = Generalization(general=ComponentInstance, specific=cloudml_ExternalComponentInstance)
gen_cloudml_ExecutionPlatform_CloudMLElementWithProperties = Generalization(general=CloudMLElementWithProperties, specific=cloudml_ExecutionPlatform)
gen_cloudml_ExecutionPlatformInstance_CloudMLElementWithProperties = Generalization(general=CloudMLElementWithProperties, specific=cloudml_ExecutionPlatformInstance)
gen_cloudml_ProvidedExecutionPlatform_ExecutionPlatform = Generalization(general=ExecutionPlatform, specific=cloudml_ProvidedExecutionPlatform)
gen_cloudml_RequiredPortInstance_PortInstance = Generalization(general=PortInstance, specific=cloudml_RequiredPortInstance)
gen_cloudml_ProvidedPortInstance_PortInstance = Generalization(general=PortInstance, specific=cloudml_ProvidedPortInstance)
gen_cloudml_RelationshipInstance_CloudMLElementWithProperties = Generalization(general=CloudMLElementWithProperties, specific=cloudml_RelationshipInstance)
gen_cloudml_RequiredExecutionPlatform_ExecutionPlatform = Generalization(general=ExecutionPlatform, specific=cloudml_RequiredExecutionPlatform)
gen_cloudml_RequiredExecutionPlatformInstance_ExecutionPlatformInstance = Generalization(general=ExecutionPlatformInstance, specific=cloudml_RequiredExecutionPlatformInstance)
gen_cloudml_ExecuteInstance_CloudMLElementWithProperties = Generalization(general=CloudMLElementWithProperties, specific=cloudml_ExecuteInstance)
gen_cloudml_PuppetResource_Resource = Generalization(general=Resource, specific=cloudml_PuppetResource)
gen_cloudml_ProvidedExecutionPlatformInstance_ExecutionPlatformInstance = Generalization(general=ExecutionPlatformInstance, specific=cloudml_ProvidedExecutionPlatformInstance)

# Domain Model
domain_model = DomainModel(
    name="cloudml",
    types={cloudml_CloudMLElement, cloudml_Property, CloudMLElement, cloudml_CloudMLElementWithProperties, cloudml_Resource, cloudml_PuppetResource, CloudMLElementWithProperties, cloudml_Component, cloudml_Cloud, cloudml_ComponentInstance, cloudml_InternalComponent, cloudml_ExternalComponent, cloudml_InternalComponentInstance, cloudml_ExternalComponentInstance, cloudml_VM, cloudml_VMInstance, cloudml_Relationship, cloudml_RelationshipInstance, cloudml_ExecuteInstance, ExternalComponent, cloudml_VMPort, cloudml_CloudMLModel, cloudml_Provider, cloudml_ProvidedPort, cloudml_ProvidedExecutionPlatform, Component, cloudml_RequiredPort, cloudml_RequiredExecutionPlatform, cloudml_Port, Port, ExternalComponentInstance, cloudml_VMPortInstance, cloudml_ProvidedPortInstance, cloudml_ProvidedExecutionPlatformInstance, ComponentInstance, cloudml_RequiredPortInstance, cloudml_RequiredExecutionPlatformInstance, cloudml_PortInstance, cloudml_ExecutionPlatform, cloudml_ExecutionPlatformInstance, ExecutionPlatform, PortInstance, Resource, ExecutionPlatformInstance},
    associations={properties0, resources1, puppetResources3, components6, clouds8, componentInstances10, internalComponents12, externalComponents14, internalComponentInstances16, externalComponentInstances18, vms20, vmInstances22, relationships24, relationshipInstances26, executesInstances28, provided30, providers5, providedPorts32, providedExecutionPlatforms34, requiredPorts36, compositeInternalComponents39, requiredExecutionPlatform41, component43, requiredPort45, providedPort48, vmInstances57, provided60, type62, providedPortInstances65, type67, providedExecutionPlatformInstances70, requiredPortInstances72, requiredExecutionPlatformInstance74, type76, componentInstance78, requiredPortResource51, providedPortResource54, type81, requiredPortInstance84, providedPortInstance87, provider90, provide93, provide96, owner99, owner101, type103, demands109, providedExecutionPlatformInstance112, requiredExecutionPlatformInstance115, offers106},
    generalizations={gen_cloudml_Property_CloudMLElement, gen_cloudml_CloudMLElementWithProperties_CloudMLElement, gen_cloudml_Resource_CloudMLElementWithProperties, gen_cloudml_VM_ExternalComponent, gen_cloudml_CloudMLModel_CloudMLElementWithProperties, gen_cloudml_VMPort_CloudMLElementWithProperties, gen_cloudml_Provider_CloudMLElementWithProperties, gen_cloudml_Component_CloudMLElementWithProperties, gen_cloudml_InternalComponent_Component, gen_cloudml_Port_CloudMLElementWithProperties, gen_cloudml_RequiredPort_Port, gen_cloudml_ProvidedPort_Port, gen_cloudml_Relationship_CloudMLElementWithProperties, gen_cloudml_Cloud_CloudMLElementWithProperties, gen_cloudml_VMInstance_ExternalComponentInstance, gen_cloudml_VMPortInstance_CloudMLElementWithProperties, gen_cloudml_ComponentInstance_CloudMLElementWithProperties, gen_cloudml_InternalComponentInstance_ComponentInstance, gen_cloudml_PortInstance_CloudMLElementWithProperties, gen_cloudml_ExternalComponent_Component, gen_cloudml_ExternalComponentInstance_ComponentInstance, gen_cloudml_ExecutionPlatform_CloudMLElementWithProperties, gen_cloudml_ExecutionPlatformInstance_CloudMLElementWithProperties, gen_cloudml_ProvidedExecutionPlatform_ExecutionPlatform, gen_cloudml_RequiredPortInstance_PortInstance, gen_cloudml_ProvidedPortInstance_PortInstance, gen_cloudml_RelationshipInstance_CloudMLElementWithProperties, gen_cloudml_RequiredExecutionPlatform_ExecutionPlatform, gen_cloudml_RequiredExecutionPlatformInstance_ExecutionPlatformInstance, gen_cloudml_ExecuteInstance_CloudMLElementWithProperties, gen_cloudml_PuppetResource_Resource, gen_cloudml_ProvidedExecutionPlatformInstance_ExecutionPlatformInstance},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)