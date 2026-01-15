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
cloudml_NamedElement = Class(name="cloudml::NamedElement", is_abstract=True)
CloudMLElement = Class(name="CloudMLElement")
cloudml_Property = Class(name="cloudml::Property")
NamedElement = Class(name="NamedElement")
cloudml_WithProperties = Class(name="cloudml::WithProperties", is_abstract=True)
cloudml_Resource = Class(name="cloudml::Resource")
WithProperties = Class(name="WithProperties")
cloudml_UploadCommand = Class(name="cloudml::UploadCommand")
cloudml_Provider = Class(name="cloudml::Provider")
cloudml_DeploymentModel = Class(name="cloudml::DeploymentModel")
cloudml_Artefact = Class(name="cloudml::Artefact")
cloudml_Node = Class(name="cloudml::Node")
cloudml_Binding = Class(name="cloudml::Binding")
cloudml_ArtefactPort = Class(name="cloudml::ArtefactPort", is_abstract=True)
cloudml_ServerPort = Class(name="cloudml::ServerPort")
ArtefactPort = Class(name="ArtefactPort")
cloudml_ClientPort = Class(name="cloudml::ClientPort")
cloudml_ArtefactInstance = Class(name="cloudml::ArtefactInstance")
cloudml_NodeInstance = Class(name="cloudml::NodeInstance")
cloudml_BindingInstance = Class(name="cloudml::BindingInstance")
cloudml_ClientPortInstance = Class(name="cloudml::ClientPortInstance")
cloudml_Composite = Class(name="cloudml::Composite")
cloudml_ArtefactPortInstance = Class(name="cloudml::ArtefactPortInstance")
cloudml_ServerPortInstance = Class(name="cloudml::ServerPortInstance")
ArtefactPortInstance = Class(name="ArtefactPortInstance")

# cloudml_CloudMLElement class attributes and methods

# cloudml_NamedElement class attributes and methods
cloudml_NamedElement_name: Property = Property(name="name", type=StringType)
cloudml_NamedElement.attributes={cloudml_NamedElement_name}

# CloudMLElement class attributes and methods

# cloudml_Property class attributes and methods
cloudml_Property_value: Property = Property(name="value", type=StringType)
cloudml_Property.attributes={cloudml_Property_value}

# NamedElement class attributes and methods

# cloudml_WithProperties class attributes and methods

# cloudml_Resource class attributes and methods
cloudml_Resource_retrievingCommand: Property = Property(name="retrievingCommand", type=StringType)
cloudml_Resource_deployingCommand: Property = Property(name="deployingCommand", type=StringType)
cloudml_Resource_configurationCommand: Property = Property(name="configurationCommand", type=StringType)
cloudml_Resource_startCommand: Property = Property(name="startCommand", type=StringType)
cloudml_Resource_stopCommand: Property = Property(name="stopCommand", type=StringType)
cloudml_Resource.attributes={cloudml_Resource_startCommand, cloudml_Resource_retrievingCommand, cloudml_Resource_stopCommand, cloudml_Resource_deployingCommand, cloudml_Resource_configurationCommand}

# WithProperties class attributes and methods

# cloudml_UploadCommand class attributes and methods
cloudml_UploadCommand_source: Property = Property(name="source", type=StringType)
cloudml_UploadCommand_target: Property = Property(name="target", type=StringType)
cloudml_UploadCommand.attributes={cloudml_UploadCommand_target, cloudml_UploadCommand_source}

# cloudml_Provider class attributes and methods
cloudml_Provider_credentials: Property = Property(name="credentials", type=StringType)
cloudml_Provider.attributes={cloudml_Provider_credentials}

# cloudml_DeploymentModel class attributes and methods

# cloudml_Artefact class attributes and methods

# cloudml_Node class attributes and methods
cloudml_Node_minRam: Property = Property(name="minRam", type=IntegerType)
cloudml_Node_minCore: Property = Property(name="minCore", type=IntegerType)
cloudml_Node_minDisk: Property = Property(name="minDisk", type=IntegerType)
cloudml_Node_location: Property = Property(name="location", type=StringType)
cloudml_Node_OS: Property = Property(name="OS", type=StringType)
cloudml_Node_sshKey: Property = Property(name="sshKey", type=StringType)
cloudml_Node_securityGroup: Property = Property(name="securityGroup", type=StringType)
cloudml_Node_groupName: Property = Property(name="groupName", type=StringType)
cloudml_Node_privateKey: Property = Property(name="privateKey", type=StringType)
cloudml_Node_imageID: Property = Property(name="imageID", type=StringType)
cloudml_Node_is64os: Property = Property(name="is64os", type=BooleanType)
cloudml_Node.attributes={cloudml_Node_imageID, cloudml_Node_minDisk, cloudml_Node_sshKey, cloudml_Node_is64os, cloudml_Node_location, cloudml_Node_groupName, cloudml_Node_securityGroup, cloudml_Node_privateKey, cloudml_Node_minRam, cloudml_Node_OS, cloudml_Node_minCore}

# cloudml_Binding class attributes and methods

# cloudml_ArtefactPort class attributes and methods
cloudml_ArtefactPort_portNumber: Property = Property(name="portNumber", type=IntegerType)
cloudml_ArtefactPort_isRemote: Property = Property(name="isRemote", type=BooleanType)
cloudml_ArtefactPort.attributes={cloudml_ArtefactPort_isRemote, cloudml_ArtefactPort_portNumber}

# cloudml_ServerPort class attributes and methods

# ArtefactPort class attributes and methods

# cloudml_ClientPort class attributes and methods
cloudml_ClientPort_isOptional: Property = Property(name="isOptional", type=BooleanType)
cloudml_ClientPort.attributes={cloudml_ClientPort_isOptional}

# cloudml_ArtefactInstance class attributes and methods

# cloudml_NodeInstance class attributes and methods
cloudml_NodeInstance_publicAddress: Property = Property(name="publicAddress", type=StringType)
cloudml_NodeInstance_id: Property = Property(name="id", type=StringType)
cloudml_NodeInstance.attributes={cloudml_NodeInstance_publicAddress, cloudml_NodeInstance_id}

# cloudml_BindingInstance class attributes and methods

# cloudml_ClientPortInstance class attributes and methods

# cloudml_Composite class attributes and methods

# cloudml_ArtefactPortInstance class attributes and methods

# cloudml_ServerPortInstance class attributes and methods

# ArtefactPortInstance class attributes and methods

# Relationships
properties0: BinaryAssociation = BinaryAssociation(
    name="properties0",
    ends={
        Property(name="cloudml_Property", type=cloudml_WithProperties, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_WithProperties", type=cloudml_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uploadCommand1: BinaryAssociation = BinaryAssociation(
    name="uploadCommand1",
    ends={
        Property(name="cloudml_UploadCommand", type=cloudml_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_Resource", type=cloudml_UploadCommand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providers2: BinaryAssociation = BinaryAssociation(
    name="providers2",
    ends={
        Property(name="cloudml_Provider", type=cloudml_DeploymentModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_DeploymentModel", type=cloudml_Provider, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
artefactTypes3: BinaryAssociation = BinaryAssociation(
    name="artefactTypes3",
    ends={
        Property(name="cloudml_Artefact", type=cloudml_DeploymentModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_DeploymentModel4", type=cloudml_Artefact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodeTypes5: BinaryAssociation = BinaryAssociation(
    name="nodeTypes5",
    ends={
        Property(name="cloudml_Node", type=cloudml_DeploymentModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_DeploymentModel6", type=cloudml_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
destination15: BinaryAssociation = BinaryAssociation(
    name="destination15",
    ends={
        Property(name="cloudml_ArtefactPort", type=cloudml_Artefact, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_Artefact16", type=cloudml_ArtefactPort, multiplicity=Multiplicity(0, 1))
    }
)
resource17: BinaryAssociation = BinaryAssociation(
    name="resource17",
    ends={
        Property(name="cloudml_Resource19", type=cloudml_Artefact, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_Artefact18", type=cloudml_Resource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
provided20: BinaryAssociation = BinaryAssociation(
    name="provided20",
    ends={
        Property(name="cloudml_ServerPort", type=cloudml_Artefact, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_Artefact21", type=cloudml_ServerPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
required22: BinaryAssociation = BinaryAssociation(
    name="required22",
    ends={
        Property(name="cloudml_ClientPort", type=cloudml_Artefact, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_Artefact23", type=cloudml_ClientPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cloudProvider24: BinaryAssociation = BinaryAssociation(
    name="cloudProvider24",
    ends={
        Property(name="cloudml_Provider26", type=cloudml_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_Node25", type=cloudml_Provider, multiplicity=Multiplicity(1, 1))
    }
)
bindingTypes7: BinaryAssociation = BinaryAssociation(
    name="bindingTypes7",
    ends={
        Property(name="cloudml_Binding", type=cloudml_DeploymentModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_DeploymentModel8", type=cloudml_Binding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
artefactInstances9: BinaryAssociation = BinaryAssociation(
    name="artefactInstances9",
    ends={
        Property(name="cloudml_ArtefactInstance", type=cloudml_DeploymentModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_DeploymentModel10", type=cloudml_ArtefactInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodeInstances11: BinaryAssociation = BinaryAssociation(
    name="nodeInstances11",
    ends={
        Property(name="cloudml_NodeInstance", type=cloudml_DeploymentModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_DeploymentModel12", type=cloudml_NodeInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bindingInstances13: BinaryAssociation = BinaryAssociation(
    name="bindingInstances13",
    ends={
        Property(name="cloudml_BindingInstance", type=cloudml_DeploymentModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_DeploymentModel14", type=cloudml_BindingInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type29: BinaryAssociation = BinaryAssociation(
    name="type29",
    ends={
        Property(name="cloudml_Artefact31", type=cloudml_ArtefactInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_ArtefactInstance30", type=cloudml_Artefact, multiplicity=Multiplicity(1, 1))
    }
)
destination32: BinaryAssociation = BinaryAssociation(
    name="destination32",
    ends={
        Property(name="cloudml_NodeInstance34", type=cloudml_ArtefactInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_ArtefactInstance33", type=cloudml_NodeInstance, multiplicity=Multiplicity(0, 1))
    }
)
provided35: BinaryAssociation = BinaryAssociation(
    name="provided35",
    ends={
        Property(name="cloudml_ServerPortInstance", type=cloudml_ArtefactInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_ArtefactInstance36", type=cloudml_ServerPortInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
required37: BinaryAssociation = BinaryAssociation(
    name="required37",
    ends={
        Property(name="cloudml_ClientPortInstance", type=cloudml_ArtefactInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_ArtefactInstance38", type=cloudml_ClientPortInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type39: BinaryAssociation = BinaryAssociation(
    name="type39",
    ends={
        Property(name="cloudml_Node41", type=cloudml_NodeInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_NodeInstance40", type=cloudml_Node, multiplicity=Multiplicity(1, 1))
    }
)
containedArtefacts42: BinaryAssociation = BinaryAssociation(
    name="containedArtefacts42",
    ends={
        Property(name="cloudml_ArtefactInstance43", type=cloudml_Composite, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_Composite", type=cloudml_ArtefactInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
client44: BinaryAssociation = BinaryAssociation(
    name="client44",
    ends={
        Property(name="cloudml_ClientPort46", type=cloudml_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_Binding45", type=cloudml_ClientPort, multiplicity=Multiplicity(0, 1))
    }
)
server47: BinaryAssociation = BinaryAssociation(
    name="server47",
    ends={
        Property(name="cloudml_ServerPort49", type=cloudml_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_Binding48", type=cloudml_ServerPort, multiplicity=Multiplicity(0, 1))
    }
)
clientResource50: BinaryAssociation = BinaryAssociation(
    name="clientResource50",
    ends={
        Property(name="cloudml_Resource52", type=cloudml_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_Binding51", type=cloudml_Resource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
serverResource53: BinaryAssociation = BinaryAssociation(
    name="serverResource53",
    ends={
        Property(name="cloudml_Resource55", type=cloudml_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_Binding54", type=cloudml_Resource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type27: BinaryAssociation = BinaryAssociation(
    name="type27",
    ends={
        Property(name="cloudml_ArtefactPort28", type=cloudml_ArtefactPortInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_ArtefactPortInstance", type=cloudml_ArtefactPort, multiplicity=Multiplicity(1, 1))
    }
)
type56: BinaryAssociation = BinaryAssociation(
    name="type56",
    ends={
        Property(name="cloudml_Binding58", type=cloudml_BindingInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_BindingInstance57", type=cloudml_Binding, multiplicity=Multiplicity(1, 1))
    }
)
client59: BinaryAssociation = BinaryAssociation(
    name="client59",
    ends={
        Property(name="cloudml_ClientPortInstance61", type=cloudml_BindingInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_BindingInstance60", type=cloudml_ClientPortInstance, multiplicity=Multiplicity(0, 1))
    }
)
server62: BinaryAssociation = BinaryAssociation(
    name="server62",
    ends={
        Property(name="cloudml_ServerPortInstance64", type=cloudml_BindingInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_BindingInstance63", type=cloudml_ServerPortInstance, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_cloudml_NamedElement_CloudMLElement = Generalization(general=CloudMLElement, specific=cloudml_NamedElement)
gen_cloudml_Property_NamedElement = Generalization(general=NamedElement, specific=cloudml_Property)
gen_cloudml_WithProperties_NamedElement = Generalization(general=NamedElement, specific=cloudml_WithProperties)
gen_cloudml_Resource_WithProperties = Generalization(general=WithProperties, specific=cloudml_Resource)
gen_cloudml_Provider_WithProperties = Generalization(general=WithProperties, specific=cloudml_Provider)
gen_cloudml_DeploymentModel_WithProperties = Generalization(general=WithProperties, specific=cloudml_DeploymentModel)
gen_cloudml_ArtefactPort_WithProperties = Generalization(general=WithProperties, specific=cloudml_ArtefactPort)
gen_cloudml_ServerPort_ArtefactPort = Generalization(general=ArtefactPort, specific=cloudml_ServerPort)
gen_cloudml_ClientPort_ArtefactPort = Generalization(general=ArtefactPort, specific=cloudml_ClientPort)
gen_cloudml_Artefact_WithProperties = Generalization(general=WithProperties, specific=cloudml_Artefact)
gen_cloudml_Node_WithProperties = Generalization(general=WithProperties, specific=cloudml_Node)
gen_cloudml_ClientPortInstance_ArtefactPortInstance = Generalization(general=ArtefactPortInstance, specific=cloudml_ClientPortInstance)
gen_cloudml_ArtefactInstance_WithProperties = Generalization(general=WithProperties, specific=cloudml_ArtefactInstance)
gen_cloudml_NodeInstance_WithProperties = Generalization(general=WithProperties, specific=cloudml_NodeInstance)
gen_cloudml_Composite_NamedElement = Generalization(general=NamedElement, specific=cloudml_Composite)
gen_cloudml_Binding_WithProperties = Generalization(general=WithProperties, specific=cloudml_Binding)
gen_cloudml_BindingInstance_WithProperties = Generalization(general=WithProperties, specific=cloudml_BindingInstance)
gen_cloudml_ArtefactPortInstance_WithProperties = Generalization(general=WithProperties, specific=cloudml_ArtefactPortInstance)
gen_cloudml_ServerPortInstance_ArtefactPortInstance = Generalization(general=ArtefactPortInstance, specific=cloudml_ServerPortInstance)

# Domain Model
domain_model = DomainModel(
    name="cloudml",
    types={cloudml_CloudMLElement, cloudml_NamedElement, CloudMLElement, cloudml_Property, NamedElement, cloudml_WithProperties, cloudml_Resource, WithProperties, cloudml_UploadCommand, cloudml_Provider, cloudml_DeploymentModel, cloudml_Artefact, cloudml_Node, cloudml_Binding, cloudml_ArtefactPort, cloudml_ServerPort, ArtefactPort, cloudml_ClientPort, cloudml_ArtefactInstance, cloudml_NodeInstance, cloudml_BindingInstance, cloudml_ClientPortInstance, cloudml_Composite, cloudml_ArtefactPortInstance, cloudml_ServerPortInstance, ArtefactPortInstance},
    associations={properties0, uploadCommand1, providers2, artefactTypes3, nodeTypes5, destination15, resource17, provided20, required22, cloudProvider24, bindingTypes7, artefactInstances9, nodeInstances11, bindingInstances13, type29, destination32, provided35, required37, type39, containedArtefacts42, client44, server47, clientResource50, serverResource53, type27, type56, client59, server62},
    generalizations={gen_cloudml_NamedElement_CloudMLElement, gen_cloudml_Property_NamedElement, gen_cloudml_WithProperties_NamedElement, gen_cloudml_Resource_WithProperties, gen_cloudml_Provider_WithProperties, gen_cloudml_DeploymentModel_WithProperties, gen_cloudml_ArtefactPort_WithProperties, gen_cloudml_ServerPort_ArtefactPort, gen_cloudml_ClientPort_ArtefactPort, gen_cloudml_Artefact_WithProperties, gen_cloudml_Node_WithProperties, gen_cloudml_ClientPortInstance_ArtefactPortInstance, gen_cloudml_ArtefactInstance_WithProperties, gen_cloudml_NodeInstance_WithProperties, gen_cloudml_Composite_NamedElement, gen_cloudml_Binding_WithProperties, gen_cloudml_BindingInstance_WithProperties, gen_cloudml_ArtefactPortInstance_WithProperties, gen_cloudml_ServerPortInstance_ArtefactPortInstance},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)