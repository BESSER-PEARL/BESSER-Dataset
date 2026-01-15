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
cloudml_core_NamedElement = Class(name="cloudml::core::NamedElement", is_abstract=True)
CloudMLElement = Class(name="CloudMLElement")
cloudml_core_Property = Class(name="cloudml::core::Property")
NamedElement = Class(name="NamedElement")
cloudml_core_WithProperties = Class(name="cloudml::core::WithProperties", is_abstract=True)
Property_ = Class(name="Property")
cloudml_core_Resource = Class(name="cloudml::core::Resource")
WithProperties = Class(name="WithProperties")
UploadCommand = Class(name="UploadCommand")
cloudml_core_Provider = Class(name="cloudml::core::Provider")
cloudml_core_DeploymentModel = Class(name="cloudml::core::DeploymentModel")
Provider = Class(name="Provider")
Artefact = Class(name="Artefact")
Node = Class(name="Node")
Binding = Class(name="Binding")
ArtefactInstance = Class(name="ArtefactInstance")
NodeInstance = Class(name="NodeInstance")
BindingInstance = Class(name="BindingInstance")
cloudml_core_ArtefactPort = Class(name="cloudml::core::ArtefactPort", is_abstract=True)
cloudml_core_ServerPort = Class(name="cloudml::core::ServerPort")
ArtefactPort = Class(name="ArtefactPort")
cloudml_core_ClientPort = Class(name="cloudml::core::ClientPort")
cloudml_core_Artefact = Class(name="cloudml::core::Artefact")
Resource = Class(name="Resource")
ServerPort = Class(name="ServerPort")
ClientPort = Class(name="ClientPort")
cloudml_core_Node = Class(name="cloudml::core::Node")
cloudml_core_ArtefactPortInstance = Class(name="cloudml::core::ArtefactPortInstance")
cloudml_core_ServerPortInstance = Class(name="cloudml::core::ServerPortInstance")
ArtefactPortInstance = Class(name="ArtefactPortInstance")
cloudml_core_ClientPortInstance = Class(name="cloudml::core::ClientPortInstance")
cloudml_core_ArtefactInstance = Class(name="cloudml::core::ArtefactInstance")
ServerPortInstance = Class(name="ServerPortInstance")
ClientPortInstance = Class(name="ClientPortInstance")
cloudml_core_NodeInstance = Class(name="cloudml::core::NodeInstance")
cloudml_core_Composite = Class(name="cloudml::core::Composite")
cloudml_core_Binding = Class(name="cloudml::core::Binding")
cloudml_core_BindingInstance = Class(name="cloudml::core::BindingInstance")
cloudml_core_UploadCommand = Class(name="cloudml::core::UploadCommand")

# cloudml_core_CloudMLElement class attributes and methods

# cloudml_core_NamedElement class attributes and methods
cloudml_core_NamedElement_name: Property = Property(name="name", type=StringType)
cloudml_core_NamedElement.attributes={cloudml_core_NamedElement_name}

# CloudMLElement class attributes and methods

# cloudml_core_Property class attributes and methods
cloudml_core_Property_value: Property = Property(name="value", type=StringType)
cloudml_core_Property.attributes={cloudml_core_Property_value}

# NamedElement class attributes and methods

# cloudml_core_WithProperties class attributes and methods

# Property class attributes and methods

# cloudml_core_Resource class attributes and methods
cloudml_core_Resource_retrievingCommand: Property = Property(name="retrievingCommand", type=StringType)
cloudml_core_Resource_deployingCommand: Property = Property(name="deployingCommand", type=StringType)
cloudml_core_Resource_configurationCommand: Property = Property(name="configurationCommand", type=StringType)
cloudml_core_Resource_startCommand: Property = Property(name="startCommand", type=StringType)
cloudml_core_Resource_stopCommand: Property = Property(name="stopCommand", type=StringType)
cloudml_core_Resource.attributes={cloudml_core_Resource_retrievingCommand, cloudml_core_Resource_deployingCommand, cloudml_core_Resource_stopCommand, cloudml_core_Resource_configurationCommand, cloudml_core_Resource_startCommand}

# WithProperties class attributes and methods

# UploadCommand class attributes and methods

# cloudml_core_Provider class attributes and methods
cloudml_core_Provider_credentials: Property = Property(name="credentials", type=StringType)
cloudml_core_Provider.attributes={cloudml_core_Provider_credentials}

# cloudml_core_DeploymentModel class attributes and methods

# Provider class attributes and methods

# Artefact class attributes and methods

# Node class attributes and methods

# Binding class attributes and methods

# ArtefactInstance class attributes and methods

# NodeInstance class attributes and methods

# BindingInstance class attributes and methods

# cloudml_core_ArtefactPort class attributes and methods
cloudml_core_ArtefactPort_portNumber: Property = Property(name="portNumber", type=IntegerType)
cloudml_core_ArtefactPort_isRemote: Property = Property(name="isRemote", type=BooleanType)
cloudml_core_ArtefactPort.attributes={cloudml_core_ArtefactPort_isRemote, cloudml_core_ArtefactPort_portNumber}

# cloudml_core_ServerPort class attributes and methods

# ArtefactPort class attributes and methods

# cloudml_core_ClientPort class attributes and methods
cloudml_core_ClientPort_isOptional: Property = Property(name="isOptional", type=BooleanType)
cloudml_core_ClientPort.attributes={cloudml_core_ClientPort_isOptional}

# cloudml_core_Artefact class attributes and methods

# Resource class attributes and methods

# ServerPort class attributes and methods

# ClientPort class attributes and methods

# cloudml_core_Node class attributes and methods
cloudml_core_Node_minRam: Property = Property(name="minRam", type=IntegerType)
cloudml_core_Node_minCore: Property = Property(name="minCore", type=IntegerType)
cloudml_core_Node_minDisk: Property = Property(name="minDisk", type=IntegerType)
cloudml_core_Node_location: Property = Property(name="location", type=StringType)
cloudml_core_Node_OS: Property = Property(name="OS", type=StringType)
cloudml_core_Node_sshKey: Property = Property(name="sshKey", type=StringType)
cloudml_core_Node_securityGroup: Property = Property(name="securityGroup", type=StringType)
cloudml_core_Node_groupName: Property = Property(name="groupName", type=StringType)
cloudml_core_Node_privateKey: Property = Property(name="privateKey", type=StringType)
cloudml_core_Node_imageID: Property = Property(name="imageID", type=StringType)
cloudml_core_Node_is64os: Property = Property(name="is64os", type=BooleanType)
cloudml_core_Node.attributes={cloudml_core_Node_OS, cloudml_core_Node_imageID, cloudml_core_Node_is64os, cloudml_core_Node_privateKey, cloudml_core_Node_securityGroup, cloudml_core_Node_minDisk, cloudml_core_Node_minRam, cloudml_core_Node_groupName, cloudml_core_Node_sshKey, cloudml_core_Node_minCore, cloudml_core_Node_location}

# cloudml_core_ArtefactPortInstance class attributes and methods

# cloudml_core_ServerPortInstance class attributes and methods

# ArtefactPortInstance class attributes and methods

# cloudml_core_ClientPortInstance class attributes and methods

# cloudml_core_ArtefactInstance class attributes and methods

# ServerPortInstance class attributes and methods

# ClientPortInstance class attributes and methods

# cloudml_core_NodeInstance class attributes and methods
cloudml_core_NodeInstance_publicAddress: Property = Property(name="publicAddress", type=StringType)
cloudml_core_NodeInstance_id: Property = Property(name="id", type=StringType)
cloudml_core_NodeInstance.attributes={cloudml_core_NodeInstance_publicAddress, cloudml_core_NodeInstance_id}

# cloudml_core_Composite class attributes and methods

# cloudml_core_Binding class attributes and methods

# cloudml_core_BindingInstance class attributes and methods

# cloudml_core_UploadCommand class attributes and methods
cloudml_core_UploadCommand_source: Property = Property(name="source", type=StringType)
cloudml_core_UploadCommand_target: Property = Property(name="target", type=StringType)
cloudml_core_UploadCommand.attributes={cloudml_core_UploadCommand_source, cloudml_core_UploadCommand_target}

# Relationships
properties0: BinaryAssociation = BinaryAssociation(
    name="properties0",
    ends={
        Property(name="Property", type=cloudml_core_WithProperties, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_WithProperties", type=Property_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uploadCommand1: BinaryAssociation = BinaryAssociation(
    name="uploadCommand1",
    ends={
        Property(name="UploadCommand", type=cloudml_core_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_Resource", type=UploadCommand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providers2: BinaryAssociation = BinaryAssociation(
    name="providers2",
    ends={
        Property(name="Provider", type=cloudml_core_DeploymentModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_DeploymentModel", type=Provider, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
artefactTypes3: BinaryAssociation = BinaryAssociation(
    name="artefactTypes3",
    ends={
        Property(name="Artefact", type=cloudml_core_DeploymentModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_DeploymentModel4", type=Artefact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodeTypes5: BinaryAssociation = BinaryAssociation(
    name="nodeTypes5",
    ends={
        Property(name="Node", type=cloudml_core_DeploymentModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_DeploymentModel6", type=Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bindingTypes7: BinaryAssociation = BinaryAssociation(
    name="bindingTypes7",
    ends={
        Property(name="Binding", type=cloudml_core_DeploymentModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_DeploymentModel8", type=Binding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
artefactInstances9: BinaryAssociation = BinaryAssociation(
    name="artefactInstances9",
    ends={
        Property(name="ArtefactInstance", type=cloudml_core_DeploymentModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_DeploymentModel10", type=ArtefactInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodeInstances11: BinaryAssociation = BinaryAssociation(
    name="nodeInstances11",
    ends={
        Property(name="NodeInstance", type=cloudml_core_DeploymentModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_DeploymentModel12", type=NodeInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bindingInstances13: BinaryAssociation = BinaryAssociation(
    name="bindingInstances13",
    ends={
        Property(name="BindingInstance", type=cloudml_core_DeploymentModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_DeploymentModel14", type=BindingInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
destination15: BinaryAssociation = BinaryAssociation(
    name="destination15",
    ends={
        Property(name="ArtefactPort", type=cloudml_core_Artefact, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_Artefact", type=ArtefactPort, multiplicity=Multiplicity(0, 1))
    }
)
resource16: BinaryAssociation = BinaryAssociation(
    name="resource16",
    ends={
        Property(name="Resource", type=cloudml_core_Artefact, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_Artefact17", type=Resource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
provided18: BinaryAssociation = BinaryAssociation(
    name="provided18",
    ends={
        Property(name="ServerPort", type=cloudml_core_Artefact, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_Artefact19", type=ServerPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
required20: BinaryAssociation = BinaryAssociation(
    name="required20",
    ends={
        Property(name="ClientPort", type=cloudml_core_Artefact, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_Artefact21", type=ClientPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cloudProvider22: BinaryAssociation = BinaryAssociation(
    name="cloudProvider22",
    ends={
        Property(name="Provider23", type=cloudml_core_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_Node", type=Provider, multiplicity=Multiplicity(1, 1))
    }
)
type24: BinaryAssociation = BinaryAssociation(
    name="type24",
    ends={
        Property(name="ArtefactPort25", type=cloudml_core_ArtefactPortInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_ArtefactPortInstance", type=ArtefactPort, multiplicity=Multiplicity(1, 1))
    }
)
type26: BinaryAssociation = BinaryAssociation(
    name="type26",
    ends={
        Property(name="Artefact27", type=cloudml_core_ArtefactInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_ArtefactInstance", type=Artefact, multiplicity=Multiplicity(1, 1))
    }
)
destination28: BinaryAssociation = BinaryAssociation(
    name="destination28",
    ends={
        Property(name="NodeInstance30", type=cloudml_core_ArtefactInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_ArtefactInstance29", type=NodeInstance, multiplicity=Multiplicity(0, 1))
    }
)
provided31: BinaryAssociation = BinaryAssociation(
    name="provided31",
    ends={
        Property(name="ServerPortInstance", type=cloudml_core_ArtefactInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_ArtefactInstance32", type=ServerPortInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
required33: BinaryAssociation = BinaryAssociation(
    name="required33",
    ends={
        Property(name="ClientPortInstance", type=cloudml_core_ArtefactInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_ArtefactInstance34", type=ClientPortInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type35: BinaryAssociation = BinaryAssociation(
    name="type35",
    ends={
        Property(name="Node36", type=cloudml_core_NodeInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_NodeInstance", type=Node, multiplicity=Multiplicity(1, 1))
    }
)
containedArtefacts37: BinaryAssociation = BinaryAssociation(
    name="containedArtefacts37",
    ends={
        Property(name="ArtefactInstance38", type=cloudml_core_Composite, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_Composite", type=ArtefactInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
client39: BinaryAssociation = BinaryAssociation(
    name="client39",
    ends={
        Property(name="ClientPort40", type=cloudml_core_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_Binding", type=ClientPort, multiplicity=Multiplicity(0, 1))
    }
)
server41: BinaryAssociation = BinaryAssociation(
    name="server41",
    ends={
        Property(name="ServerPort43", type=cloudml_core_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_Binding42", type=ServerPort, multiplicity=Multiplicity(0, 1))
    }
)
clientResource44: BinaryAssociation = BinaryAssociation(
    name="clientResource44",
    ends={
        Property(name="Resource46", type=cloudml_core_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_Binding45", type=Resource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
serverResource47: BinaryAssociation = BinaryAssociation(
    name="serverResource47",
    ends={
        Property(name="Resource49", type=cloudml_core_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_Binding48", type=Resource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type50: BinaryAssociation = BinaryAssociation(
    name="type50",
    ends={
        Property(name="Binding51", type=cloudml_core_BindingInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_BindingInstance", type=Binding, multiplicity=Multiplicity(1, 1))
    }
)
client52: BinaryAssociation = BinaryAssociation(
    name="client52",
    ends={
        Property(name="ClientPortInstance54", type=cloudml_core_BindingInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_BindingInstance53", type=ClientPortInstance, multiplicity=Multiplicity(0, 1))
    }
)
server55: BinaryAssociation = BinaryAssociation(
    name="server55",
    ends={
        Property(name="ServerPortInstance57", type=cloudml_core_BindingInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_BindingInstance56", type=ServerPortInstance, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_cloudml_core_NamedElement_CloudMLElement = Generalization(general=CloudMLElement, specific=cloudml_core_NamedElement)
gen_cloudml_core_Property_NamedElement = Generalization(general=NamedElement, specific=cloudml_core_Property)
gen_cloudml_core_WithProperties_NamedElement = Generalization(general=NamedElement, specific=cloudml_core_WithProperties)
gen_cloudml_core_Resource_WithProperties = Generalization(general=WithProperties, specific=cloudml_core_Resource)
gen_cloudml_core_DeploymentModel_WithProperties = Generalization(general=WithProperties, specific=cloudml_core_DeploymentModel)
gen_cloudml_core_ArtefactPort_WithProperties = Generalization(general=WithProperties, specific=cloudml_core_ArtefactPort)
gen_cloudml_core_ServerPort_ArtefactPort = Generalization(general=ArtefactPort, specific=cloudml_core_ServerPort)
gen_cloudml_core_ClientPort_ArtefactPort = Generalization(general=ArtefactPort, specific=cloudml_core_ClientPort)
gen_cloudml_core_Artefact_WithProperties = Generalization(general=WithProperties, specific=cloudml_core_Artefact)
gen_cloudml_core_Node_WithProperties = Generalization(general=WithProperties, specific=cloudml_core_Node)
gen_cloudml_core_Provider_WithProperties = Generalization(general=WithProperties, specific=cloudml_core_Provider)
gen_cloudml_core_Composite_NamedElement = Generalization(general=NamedElement, specific=cloudml_core_Composite)
gen_cloudml_core_ArtefactPortInstance_WithProperties = Generalization(general=WithProperties, specific=cloudml_core_ArtefactPortInstance)
gen_cloudml_core_ServerPortInstance_ArtefactPortInstance = Generalization(general=ArtefactPortInstance, specific=cloudml_core_ServerPortInstance)
gen_cloudml_core_ClientPortInstance_ArtefactPortInstance = Generalization(general=ArtefactPortInstance, specific=cloudml_core_ClientPortInstance)
gen_cloudml_core_ArtefactInstance_WithProperties = Generalization(general=WithProperties, specific=cloudml_core_ArtefactInstance)
gen_cloudml_core_NodeInstance_WithProperties = Generalization(general=WithProperties, specific=cloudml_core_NodeInstance)
gen_cloudml_core_Binding_WithProperties = Generalization(general=WithProperties, specific=cloudml_core_Binding)
gen_cloudml_core_BindingInstance_WithProperties = Generalization(general=WithProperties, specific=cloudml_core_BindingInstance)

# Domain Model
domain_model = DomainModel(
    name="cloudml",
    types={cloudml_core_CloudMLElement, cloudml_core_NamedElement, CloudMLElement, cloudml_core_Property, NamedElement, cloudml_core_WithProperties, Property_, cloudml_core_Resource, WithProperties, UploadCommand, cloudml_core_Provider, cloudml_core_DeploymentModel, Provider, Artefact, Node, Binding, ArtefactInstance, NodeInstance, BindingInstance, cloudml_core_ArtefactPort, cloudml_core_ServerPort, ArtefactPort, cloudml_core_ClientPort, cloudml_core_Artefact, Resource, ServerPort, ClientPort, cloudml_core_Node, cloudml_core_ArtefactPortInstance, cloudml_core_ServerPortInstance, ArtefactPortInstance, cloudml_core_ClientPortInstance, cloudml_core_ArtefactInstance, ServerPortInstance, ClientPortInstance, cloudml_core_NodeInstance, cloudml_core_Composite, cloudml_core_Binding, cloudml_core_BindingInstance, cloudml_core_UploadCommand},
    associations={properties0, uploadCommand1, providers2, artefactTypes3, nodeTypes5, bindingTypes7, artefactInstances9, nodeInstances11, bindingInstances13, destination15, resource16, provided18, required20, cloudProvider22, type24, type26, destination28, provided31, required33, type35, containedArtefacts37, client39, server41, clientResource44, serverResource47, type50, client52, server55},
    generalizations={gen_cloudml_core_NamedElement_CloudMLElement, gen_cloudml_core_Property_NamedElement, gen_cloudml_core_WithProperties_NamedElement, gen_cloudml_core_Resource_WithProperties, gen_cloudml_core_DeploymentModel_WithProperties, gen_cloudml_core_ArtefactPort_WithProperties, gen_cloudml_core_ServerPort_ArtefactPort, gen_cloudml_core_ClientPort_ArtefactPort, gen_cloudml_core_Artefact_WithProperties, gen_cloudml_core_Node_WithProperties, gen_cloudml_core_Provider_WithProperties, gen_cloudml_core_Composite_NamedElement, gen_cloudml_core_ArtefactPortInstance_WithProperties, gen_cloudml_core_ServerPortInstance_ArtefactPortInstance, gen_cloudml_core_ClientPortInstance_ArtefactPortInstance, gen_cloudml_core_ArtefactInstance_WithProperties, gen_cloudml_core_NodeInstance_WithProperties, gen_cloudml_core_Binding_WithProperties, gen_cloudml_core_BindingInstance_WithProperties},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)