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
Property_ = Class(name="Property")
cloudml_core_Resource = Class(name="cloudml::core::Resource")
WithProperties = Class(name="WithProperties")
cloudml_core_Provider = Class(name="cloudml::core::Provider")
cloudml_core_DeploymentModel = Class(name="cloudml::core::DeploymentModel")
Artefact = Class(name="Artefact")
Node = Class(name="Node")
ArtefactInstance = Class(name="ArtefactInstance")
NodeInstance = Class(name="NodeInstance")
cloudml_core_ArtefactPort = Class(name="cloudml::core::ArtefactPort")
cloudml_core_Artefact = Class(name="cloudml::core::Artefact")
ArtefactPort = Class(name="ArtefactPort")
Resource = Class(name="Resource")
cloudml_core_CloudMLElement = Class(name="cloudml::core::CloudMLElement", is_abstract=True)
cloudml_core_NamedElement = Class(name="cloudml::core::NamedElement", is_abstract=True)
CloudMLElement = Class(name="CloudMLElement")
cloudml_core_Property = Class(name="cloudml::core::Property")
NamedElement = Class(name="NamedElement")
cloudml_core_WithProperties = Class(name="cloudml::core::WithProperties", is_abstract=True)
cloudml_core_ArtefactPortInstance = Class(name="cloudml::core::ArtefactPortInstance")
cloudml_core_ArtefactInstance = Class(name="cloudml::core::ArtefactInstance")
NodePortInstance = Class(name="NodePortInstance")
ArtefactPortInstance = Class(name="ArtefactPortInstance")
cloudml_core_NodePortInstance = Class(name="cloudml::core::NodePortInstance")
cloudml_core_NodeInstance = Class(name="cloudml::core::NodeInstance")
cloudml_core_NodePort = Class(name="cloudml::core::NodePort")
cloudml_core_Node = Class(name="cloudml::core::Node")
NodePort = Class(name="NodePort")
Provider = Class(name="Provider")
cloudml_core_Composite = Class(name="cloudml::core::Composite")

# Property class attributes and methods

# cloudml_core_Resource class attributes and methods
cloudml_core_Resource_retrievingResourceCommand: Property = Property(name="retrievingResourceCommand", type=StringType)
cloudml_core_Resource_deployingResourceCommand: Property = Property(name="deployingResourceCommand", type=StringType)
cloudml_core_Resource.attributes={cloudml_core_Resource_deployingResourceCommand, cloudml_core_Resource_retrievingResourceCommand}

# WithProperties class attributes and methods

# cloudml_core_Provider class attributes and methods
cloudml_core_Provider_login: Property = Property(name="login", type=StringType)
cloudml_core_Provider_password: Property = Property(name="password", type=StringType)
cloudml_core_Provider.attributes={cloudml_core_Provider_login, cloudml_core_Provider_password}

# cloudml_core_DeploymentModel class attributes and methods

# Artefact class attributes and methods

# Node class attributes and methods

# ArtefactInstance class attributes and methods

# NodeInstance class attributes and methods

# cloudml_core_ArtefactPort class attributes and methods

# cloudml_core_Artefact class attributes and methods

# ArtefactPort class attributes and methods

# Resource class attributes and methods

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

# cloudml_core_ArtefactPortInstance class attributes and methods

# cloudml_core_ArtefactInstance class attributes and methods

# NodePortInstance class attributes and methods

# ArtefactPortInstance class attributes and methods

# cloudml_core_NodePortInstance class attributes and methods

# cloudml_core_NodeInstance class attributes and methods
cloudml_core_NodeInstance_publicAddress: Property = Property(name="publicAddress", type=StringType)
cloudml_core_NodeInstance.attributes={cloudml_core_NodeInstance_publicAddress}

# cloudml_core_NodePort class attributes and methods

# cloudml_core_Node class attributes and methods
cloudml_core_Node_privateKey: Property = Property(name="privateKey", type=StringType)
cloudml_core_Node_imageID: Property = Property(name="imageID", type=StringType)
cloudml_core_Node_is64os: Property = Property(name="is64os", type=BooleanType)
cloudml_core_Node_minRam: Property = Property(name="minRam", type=IntegerType)
cloudml_core_Node_minCore: Property = Property(name="minCore", type=IntegerType)
cloudml_core_Node_minDisk: Property = Property(name="minDisk", type=IntegerType)
cloudml_core_Node_location: Property = Property(name="location", type=StringType)
cloudml_core_Node_OS: Property = Property(name="OS", type=StringType)
cloudml_core_Node_sshKey: Property = Property(name="sshKey", type=StringType)
cloudml_core_Node_securityGroup: Property = Property(name="securityGroup", type=StringType)
cloudml_core_Node_groupName: Property = Property(name="groupName", type=StringType)
cloudml_core_Node.attributes={cloudml_core_Node_is64os, cloudml_core_Node_privateKey, cloudml_core_Node_minCore, cloudml_core_Node_OS, cloudml_core_Node_minDisk, cloudml_core_Node_securityGroup, cloudml_core_Node_groupName, cloudml_core_Node_minRam, cloudml_core_Node_location, cloudml_core_Node_imageID, cloudml_core_Node_sshKey}

# NodePort class attributes and methods

# Provider class attributes and methods

# cloudml_core_Composite class attributes and methods

# Relationships
properties0: BinaryAssociation = BinaryAssociation(
    name="properties0",
    ends={
        Property(name="Property", type=cloudml_core_WithProperties, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_WithProperties", type=Property_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
artefactTypes1: BinaryAssociation = BinaryAssociation(
    name="artefactTypes1",
    ends={
        Property(name="Artefact", type=cloudml_core_DeploymentModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_DeploymentModel", type=Artefact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodeTypes2: BinaryAssociation = BinaryAssociation(
    name="nodeTypes2",
    ends={
        Property(name="Node", type=cloudml_core_DeploymentModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_DeploymentModel3", type=Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
artefactInstances4: BinaryAssociation = BinaryAssociation(
    name="artefactInstances4",
    ends={
        Property(name="ArtefactInstance", type=cloudml_core_DeploymentModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_DeploymentModel5", type=ArtefactInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodeInstances6: BinaryAssociation = BinaryAssociation(
    name="nodeInstances6",
    ends={
        Property(name="NodeInstance", type=cloudml_core_DeploymentModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_DeploymentModel7", type=NodeInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
destination8: BinaryAssociation = BinaryAssociation(
    name="destination8",
    ends={
        Property(name="ArtefactPort", type=cloudml_core_Artefact, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_Artefact", type=ArtefactPort, multiplicity=Multiplicity(0, 1))
    }
)
resource9: BinaryAssociation = BinaryAssociation(
    name="resource9",
    ends={
        Property(name="Resource", type=cloudml_core_Artefact, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_Artefact10", type=Resource, multiplicity=Multiplicity(0, 1))
    }
)
type26: BinaryAssociation = BinaryAssociation(
    name="type26",
    ends={
        Property(name="ArtefactPort27", type=cloudml_core_ArtefactPortInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_ArtefactPortInstance", type=ArtefactPort, multiplicity=Multiplicity(1, 1))
    }
)
type28: BinaryAssociation = BinaryAssociation(
    name="type28",
    ends={
        Property(name="Artefact29", type=cloudml_core_ArtefactInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_ArtefactInstance", type=Artefact, multiplicity=Multiplicity(1, 1))
    }
)
destination30: BinaryAssociation = BinaryAssociation(
    name="destination30",
    ends={
        Property(name="NodePortInstance", type=cloudml_core_ArtefactInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_ArtefactInstance31", type=NodePortInstance, multiplicity=Multiplicity(0, 1))
    }
)
inputs32: BinaryAssociation = BinaryAssociation(
    name="inputs32",
    ends={
        Property(name="ArtefactPortInstance", type=cloudml_core_ArtefactInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_ArtefactInstance33", type=ArtefactPortInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputs34: BinaryAssociation = BinaryAssociation(
    name="outputs34",
    ends={
        Property(name="ArtefactPortInstance36", type=cloudml_core_ArtefactInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_ArtefactInstance35", type=ArtefactPortInstance, multiplicity=Multiplicity(0, 9999))
    }
)
required37: BinaryAssociation = BinaryAssociation(
    name="required37",
    ends={
        Property(name="ArtefactPortInstance39", type=cloudml_core_ArtefactInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_ArtefactInstance38", type=ArtefactPortInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
provided40: BinaryAssociation = BinaryAssociation(
    name="provided40",
    ends={
        Property(name="ArtefactPortInstance42", type=cloudml_core_ArtefactInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_ArtefactInstance41", type=ArtefactPortInstance, multiplicity=Multiplicity(0, 9999))
    }
)
type43: BinaryAssociation = BinaryAssociation(
    name="type43",
    ends={
        Property(name="NodePort44", type=cloudml_core_NodePortInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_NodePortInstance", type=NodePort, multiplicity=Multiplicity(1, 1))
    }
)
type45: BinaryAssociation = BinaryAssociation(
    name="type45",
    ends={
        Property(name="NodeInstance46", type=cloudml_core_NodeInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_NodeInstance", type=NodeInstance, multiplicity=Multiplicity(1, 1))
    }
)
inputs11: BinaryAssociation = BinaryAssociation(
    name="inputs11",
    ends={
        Property(name="ArtefactPort13", type=cloudml_core_Artefact, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_Artefact12", type=ArtefactPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputs14: BinaryAssociation = BinaryAssociation(
    name="outputs14",
    ends={
        Property(name="ArtefactPort16", type=cloudml_core_Artefact, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_Artefact15", type=ArtefactPort, multiplicity=Multiplicity(0, 9999))
    }
)
required17: BinaryAssociation = BinaryAssociation(
    name="required17",
    ends={
        Property(name="ArtefactPort19", type=cloudml_core_Artefact, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_Artefact18", type=ArtefactPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
provided20: BinaryAssociation = BinaryAssociation(
    name="provided20",
    ends={
        Property(name="ArtefactPort22", type=cloudml_core_Artefact, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_Artefact21", type=ArtefactPort, multiplicity=Multiplicity(0, 9999))
    }
)
provided23: BinaryAssociation = BinaryAssociation(
    name="provided23",
    ends={
        Property(name="NodePort", type=cloudml_core_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_Node", type=NodePort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cloudProvider24: BinaryAssociation = BinaryAssociation(
    name="cloudProvider24",
    ends={
        Property(name="Provider", type=cloudml_core_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_Node25", type=Provider, multiplicity=Multiplicity(1, 1))
    }
)
provided47: BinaryAssociation = BinaryAssociation(
    name="provided47",
    ends={
        Property(name="NodePortInstance49", type=cloudml_core_NodeInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_NodeInstance48", type=NodePortInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containedArtefacts50: BinaryAssociation = BinaryAssociation(
    name="containedArtefacts50",
    ends={
        Property(name="ArtefactInstance51", type=cloudml_core_Composite, multiplicity=Multiplicity(1, 1)),
        Property(name="cloudml_core_Composite", type=ArtefactInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_cloudml_core_Resource_WithProperties = Generalization(general=WithProperties, specific=cloudml_core_Resource)
gen_cloudml_core_Provider_WithProperties = Generalization(general=WithProperties, specific=cloudml_core_Provider)
gen_cloudml_core_DeploymentModel_WithProperties = Generalization(general=WithProperties, specific=cloudml_core_DeploymentModel)
gen_cloudml_core_ArtefactPort_WithProperties = Generalization(general=WithProperties, specific=cloudml_core_ArtefactPort)
gen_cloudml_core_Artefact_WithProperties = Generalization(general=WithProperties, specific=cloudml_core_Artefact)
gen_cloudml_core_NamedElement_CloudMLElement = Generalization(general=CloudMLElement, specific=cloudml_core_NamedElement)
gen_cloudml_core_Property_NamedElement = Generalization(general=NamedElement, specific=cloudml_core_Property)
gen_cloudml_core_WithProperties_NamedElement = Generalization(general=NamedElement, specific=cloudml_core_WithProperties)
gen_cloudml_core_ArtefactPortInstance_WithProperties = Generalization(general=WithProperties, specific=cloudml_core_ArtefactPortInstance)
gen_cloudml_core_ArtefactInstance_WithProperties = Generalization(general=WithProperties, specific=cloudml_core_ArtefactInstance)
gen_cloudml_core_NodePortInstance_WithProperties = Generalization(general=WithProperties, specific=cloudml_core_NodePortInstance)
gen_cloudml_core_NodeInstance_WithProperties = Generalization(general=WithProperties, specific=cloudml_core_NodeInstance)
gen_cloudml_core_NodePort_WithProperties = Generalization(general=WithProperties, specific=cloudml_core_NodePort)
gen_cloudml_core_Node_WithProperties = Generalization(general=WithProperties, specific=cloudml_core_Node)
gen_cloudml_core_Composite_NamedElement = Generalization(general=NamedElement, specific=cloudml_core_Composite)

# Domain Model
domain_model = DomainModel(
    name="cloudml",
    types={Property_, cloudml_core_Resource, WithProperties, cloudml_core_Provider, cloudml_core_DeploymentModel, Artefact, Node, ArtefactInstance, NodeInstance, cloudml_core_ArtefactPort, cloudml_core_Artefact, ArtefactPort, Resource, cloudml_core_CloudMLElement, cloudml_core_NamedElement, CloudMLElement, cloudml_core_Property, NamedElement, cloudml_core_WithProperties, cloudml_core_ArtefactPortInstance, cloudml_core_ArtefactInstance, NodePortInstance, ArtefactPortInstance, cloudml_core_NodePortInstance, cloudml_core_NodeInstance, cloudml_core_NodePort, cloudml_core_Node, NodePort, Provider, cloudml_core_Composite},
    associations={properties0, artefactTypes1, nodeTypes2, artefactInstances4, nodeInstances6, destination8, resource9, type26, type28, destination30, inputs32, outputs34, required37, provided40, type43, type45, inputs11, outputs14, required17, provided20, provided23, cloudProvider24, provided47, containedArtefacts50},
    generalizations={gen_cloudml_core_Resource_WithProperties, gen_cloudml_core_Provider_WithProperties, gen_cloudml_core_DeploymentModel_WithProperties, gen_cloudml_core_ArtefactPort_WithProperties, gen_cloudml_core_Artefact_WithProperties, gen_cloudml_core_NamedElement_CloudMLElement, gen_cloudml_core_Property_NamedElement, gen_cloudml_core_WithProperties_NamedElement, gen_cloudml_core_ArtefactPortInstance_WithProperties, gen_cloudml_core_ArtefactInstance_WithProperties, gen_cloudml_core_NodePortInstance_WithProperties, gen_cloudml_core_NodeInstance_WithProperties, gen_cloudml_core_NodePort_WithProperties, gen_cloudml_core_Node_WithProperties, gen_cloudml_core_Composite_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)