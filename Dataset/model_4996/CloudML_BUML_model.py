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
cloudml_core_Artefact = Class(name="cloudml::core::Artefact")
ArtefactPort = Class(name="ArtefactPort")
Resource = Class(name="Resource")
cloudml_core_NodePort = Class(name="cloudml::core::NodePort")
cloudml_core_Node = Class(name="cloudml::core::Node")
NodePort = Class(name="NodePort")
cloudml_core_WithProperties = Class(name="cloudml::core::WithProperties", is_abstract=True)
Property_ = Class(name="Property")
cloudml_core_Resource = Class(name="cloudml::core::Resource")
WithProperties = Class(name="WithProperties")
cloudml_core_Provider = Class(name="cloudml::core::Provider")
cloudml_core_DeploymentModel = Class(name="cloudml::core::DeploymentModel")
Provider = Class(name="Provider")
Artefact = Class(name="Artefact")
Node = Class(name="Node")
ArtefactInstance = Class(name="ArtefactInstance")
NodeInstance = Class(name="NodeInstance")
cloudml_core_ArtefactPort = Class(name="cloudml::core::ArtefactPort")
cloudml_core_NodePortInstance = Class(name="cloudml::core::NodePortInstance")
cloudml_core_NodeInstance = Class(name="cloudml::core::NodeInstance")
cloudml_core_Composite = Class(name="cloudml::core::Composite")
cloudml_core_ArtefactPortInstance = Class(name="cloudml::core::ArtefactPortInstance")
cloudml_core_ArtefactInstance = Class(name="cloudml::core::ArtefactInstance")
NodePortInstance = Class(name="NodePortInstance")
ArtefactPortInstance = Class(name="ArtefactPortInstance")

# cloudml_core_CloudMLElement class attributes and methods

# cloudml_core_NamedElement class attributes and methods
cloudml_core_NamedElement_name: Property = Property(name="name", type=StringType)
cloudml_core_NamedElement.attributes={cloudml_core_NamedElement_name}

# CloudMLElement class attributes and methods

# cloudml_core_Property class attributes and methods
cloudml_core_Property_value: Property = Property(name="value", type=StringType)
cloudml_core_Property.attributes={cloudml_core_Property_value}

# NamedElement class attributes and methods

# cloudml_core_Artefact class attributes and methods

# ArtefactPort class attributes and methods

# Resource class attributes and methods

# cloudml_core_NodePort class attributes and methods

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
cloudml_core_Node.attributes={cloudml_core_Node_minCore, cloudml_core_Node_groupName, cloudml_core_Node_imageID, cloudml_core_Node_minDisk, cloudml_core_Node_sshKey, cloudml_core_Node_is64os, cloudml_core_Node_OS, cloudml_core_Node_securityGroup, cloudml_core_Node_minRam, cloudml_core_Node_location, cloudml_core_Node_privateKey}

# NodePort class attributes and methods

# cloudml_core_WithProperties class attributes and methods

# Property class attributes and methods

# cloudml_core_Resource class attributes and methods
cloudml_core_Resource_retrievingCommand: Property = Property(name="retrievingCommand", type=StringType)
cloudml_core_Resource_deployingCommand: Property = Property(name="deployingCommand", type=StringType)
cloudml_core_Resource_configurationCommand: Property = Property(name="configurationCommand", type=StringType)
cloudml_core_Resource_startCommand: Property = Property(name="startCommand", type=StringType)
cloudml_core_Resource.attributes={cloudml_core_Resource_deployingCommand, cloudml_core_Resource_configurationCommand, cloudml_core_Resource_retrievingCommand, cloudml_core_Resource_startCommand}

# WithProperties class attributes and methods

# cloudml_core_Provider class attributes and methods
cloudml_core_Provider_credentials: Property = Property(name="credentials", type=StringType)
cloudml_core_Provider.attributes={cloudml_core_Provider_credentials}

# cloudml_core_DeploymentModel class attributes and methods

# Provider class attributes and methods

# Artefact class attributes and methods

# Node class attributes and methods

# ArtefactInstance class attributes and methods

# NodeInstance class attributes and methods

# cloudml_core_ArtefactPort class attributes and methods
cloudml_core_ArtefactPort_portNumber: Property = Property(name="portNumber", type=IntegerType)
cloudml_core_ArtefactPort.attributes={cloudml_core_ArtefactPort_portNumber}

# cloudml_core_NodePortInstance class attributes and methods

# cloudml_core_NodeInstance class attributes and methods
cloudml_core_NodeInstance_publicAddress: Property = Property(name="publicAddress", type=StringType)
cloudml_core_NodeInstance.attributes={cloudml_core_NodeInstance_publicAddress}

# cloudml_core_Composite class attributes and methods

# cloudml_core_ArtefactPortInstance class attributes and methods

# cloudml_core_ArtefactInstance class attributes and methods

# NodePortInstance class attributes and methods

# ArtefactPortInstance class attributes and methods

# Relationships
destination10: BinaryAssociation = BinaryAssociation(
    name="destination10",
    ends={
        Property(name="ArtefactPort", type=cloudml_core_Artefact, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_Artefact", type=ArtefactPort, multiplicity=Multiplicity(0, 1))
    }
)
resource11: BinaryAssociation = BinaryAssociation(
    name="resource11",
    ends={
        Property(name="Resource", type=cloudml_core_Artefact, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_Artefact12", type=Resource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inputs13: BinaryAssociation = BinaryAssociation(
    name="inputs13",
    ends={
        Property(name="ArtefactPort15", type=cloudml_core_Artefact, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_Artefact14", type=ArtefactPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputs16: BinaryAssociation = BinaryAssociation(
    name="outputs16",
    ends={
        Property(name="ArtefactPort18", type=cloudml_core_Artefact, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_Artefact17", type=ArtefactPort, multiplicity=Multiplicity(0, 9999))
    }
)
provided19: BinaryAssociation = BinaryAssociation(
    name="provided19",
    ends={
        Property(name="ArtefactPort21", type=cloudml_core_Artefact, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_Artefact20", type=ArtefactPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
required22: BinaryAssociation = BinaryAssociation(
    name="required22",
    ends={
        Property(name="ArtefactPort24", type=cloudml_core_Artefact, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_Artefact23", type=ArtefactPort, multiplicity=Multiplicity(0, 9999))
    }
)
provided25: BinaryAssociation = BinaryAssociation(
    name="provided25",
    ends={
        Property(name="NodePort", type=cloudml_core_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_Node", type=NodePort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cloudProvider26: BinaryAssociation = BinaryAssociation(
    name="cloudProvider26",
    ends={
        Property(name="Provider28", type=cloudml_core_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_Node27", type=Provider, multiplicity=Multiplicity(1, 1))
    }
)
properties0: BinaryAssociation = BinaryAssociation(
    name="properties0",
    ends={
        Property(name="Property", type=cloudml_core_WithProperties, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_WithProperties", type=Property_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providers1: BinaryAssociation = BinaryAssociation(
    name="providers1",
    ends={
        Property(name="Provider", type=cloudml_core_DeploymentModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_DeploymentModel", type=Provider, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
artefactTypes2: BinaryAssociation = BinaryAssociation(
    name="artefactTypes2",
    ends={
        Property(name="Artefact", type=cloudml_core_DeploymentModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_DeploymentModel3", type=Artefact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodeTypes4: BinaryAssociation = BinaryAssociation(
    name="nodeTypes4",
    ends={
        Property(name="Node", type=cloudml_core_DeploymentModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_DeploymentModel5", type=Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
artefactInstances6: BinaryAssociation = BinaryAssociation(
    name="artefactInstances6",
    ends={
        Property(name="ArtefactInstance", type=cloudml_core_DeploymentModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_DeploymentModel7", type=ArtefactInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodeInstances8: BinaryAssociation = BinaryAssociation(
    name="nodeInstances8",
    ends={
        Property(name="NodeInstance", type=cloudml_core_DeploymentModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_DeploymentModel9", type=NodeInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type46: BinaryAssociation = BinaryAssociation(
    name="type46",
    ends={
        Property(name="NodePort47", type=cloudml_core_NodePortInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_NodePortInstance", type=NodePort, multiplicity=Multiplicity(1, 1))
    }
)
type48: BinaryAssociation = BinaryAssociation(
    name="type48",
    ends={
        Property(name="Node49", type=cloudml_core_NodeInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_NodeInstance", type=Node, multiplicity=Multiplicity(1, 1))
    }
)
provided50: BinaryAssociation = BinaryAssociation(
    name="provided50",
    ends={
        Property(name="NodePortInstance52", type=cloudml_core_NodeInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_NodeInstance51", type=NodePortInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containedArtefacts53: BinaryAssociation = BinaryAssociation(
    name="containedArtefacts53",
    ends={
        Property(name="ArtefactInstance54", type=cloudml_core_Composite, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_Composite", type=ArtefactInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type29: BinaryAssociation = BinaryAssociation(
    name="type29",
    ends={
        Property(name="ArtefactPort30", type=cloudml_core_ArtefactPortInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_ArtefactPortInstance", type=ArtefactPort, multiplicity=Multiplicity(1, 1))
    }
)
type31: BinaryAssociation = BinaryAssociation(
    name="type31",
    ends={
        Property(name="Artefact32", type=cloudml_core_ArtefactInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_ArtefactInstance", type=Artefact, multiplicity=Multiplicity(1, 1))
    }
)
destination33: BinaryAssociation = BinaryAssociation(
    name="destination33",
    ends={
        Property(name="NodePortInstance", type=cloudml_core_ArtefactInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_ArtefactInstance34", type=NodePortInstance, multiplicity=Multiplicity(0, 1))
    }
)
inputs35: BinaryAssociation = BinaryAssociation(
    name="inputs35",
    ends={
        Property(name="ArtefactPortInstance", type=cloudml_core_ArtefactInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_ArtefactInstance36", type=ArtefactPortInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputs37: BinaryAssociation = BinaryAssociation(
    name="outputs37",
    ends={
        Property(name="ArtefactPortInstance39", type=cloudml_core_ArtefactInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_ArtefactInstance38", type=ArtefactPortInstance, multiplicity=Multiplicity(0, 9999))
    }
)
provided40: BinaryAssociation = BinaryAssociation(
    name="provided40",
    ends={
        Property(name="ArtefactPortInstance42", type=cloudml_core_ArtefactInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_ArtefactInstance41", type=ArtefactPortInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
required43: BinaryAssociation = BinaryAssociation(
    name="required43",
    ends={
        Property(name="ArtefactPortInstance45", type=cloudml_core_ArtefactInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_ArtefactInstance44", type=ArtefactPortInstance, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_cloudml_core_NamedElement_CloudMLElement = Generalization(general=CloudMLElement, specific=cloudml_core_NamedElement)
gen_cloudml_core_Property_NamedElement = Generalization(general=NamedElement, specific=cloudml_core_Property)
gen_cloudml_core_Artefact_WithProperties = Generalization(general=WithProperties, specific=cloudml_core_Artefact)
gen_cloudml_core_NodePort_WithProperties = Generalization(general=WithProperties, specific=cloudml_core_NodePort)
gen_cloudml_core_Node_WithProperties = Generalization(general=WithProperties, specific=cloudml_core_Node)
gen_cloudml_core_WithProperties_NamedElement = Generalization(general=NamedElement, specific=cloudml_core_WithProperties)
gen_cloudml_core_Resource_WithProperties = Generalization(general=WithProperties, specific=cloudml_core_Resource)
gen_cloudml_core_Provider_WithProperties = Generalization(general=WithProperties, specific=cloudml_core_Provider)
gen_cloudml_core_DeploymentModel_WithProperties = Generalization(general=WithProperties, specific=cloudml_core_DeploymentModel)
gen_cloudml_core_ArtefactPort_WithProperties = Generalization(general=WithProperties, specific=cloudml_core_ArtefactPort)
gen_cloudml_core_NodePortInstance_WithProperties = Generalization(general=WithProperties, specific=cloudml_core_NodePortInstance)
gen_cloudml_core_NodeInstance_WithProperties = Generalization(general=WithProperties, specific=cloudml_core_NodeInstance)
gen_cloudml_core_Composite_NamedElement = Generalization(general=NamedElement, specific=cloudml_core_Composite)
gen_cloudml_core_ArtefactPortInstance_WithProperties = Generalization(general=WithProperties, specific=cloudml_core_ArtefactPortInstance)
gen_cloudml_core_ArtefactInstance_WithProperties = Generalization(general=WithProperties, specific=cloudml_core_ArtefactInstance)

# Domain Model
domain_model = DomainModel(
    name="cloudml",
    types={cloudml_core_CloudMLElement, cloudml_core_NamedElement, CloudMLElement, cloudml_core_Property, NamedElement, cloudml_core_Artefact, ArtefactPort, Resource, cloudml_core_NodePort, cloudml_core_Node, NodePort, cloudml_core_WithProperties, Property_, cloudml_core_Resource, WithProperties, cloudml_core_Provider, cloudml_core_DeploymentModel, Provider, Artefact, Node, ArtefactInstance, NodeInstance, cloudml_core_ArtefactPort, cloudml_core_NodePortInstance, cloudml_core_NodeInstance, cloudml_core_Composite, cloudml_core_ArtefactPortInstance, cloudml_core_ArtefactInstance, NodePortInstance, ArtefactPortInstance},
    associations={destination10, resource11, inputs13, outputs16, provided19, required22, provided25, cloudProvider26, properties0, providers1, artefactTypes2, nodeTypes4, artefactInstances6, nodeInstances8, type46, type48, provided50, containedArtefacts53, type29, type31, destination33, inputs35, outputs37, provided40, required43},
    generalizations={gen_cloudml_core_NamedElement_CloudMLElement, gen_cloudml_core_Property_NamedElement, gen_cloudml_core_Artefact_WithProperties, gen_cloudml_core_NodePort_WithProperties, gen_cloudml_core_Node_WithProperties, gen_cloudml_core_WithProperties_NamedElement, gen_cloudml_core_Resource_WithProperties, gen_cloudml_core_Provider_WithProperties, gen_cloudml_core_DeploymentModel_WithProperties, gen_cloudml_core_ArtefactPort_WithProperties, gen_cloudml_core_NodePortInstance_WithProperties, gen_cloudml_core_NodeInstance_WithProperties, gen_cloudml_core_Composite_NamedElement, gen_cloudml_core_ArtefactPortInstance_WithProperties, gen_cloudml_core_ArtefactInstance_WithProperties},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)