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
soaml_Collaboration = Class(name="soaml::Collaboration")
soaml_ServiceArchitecture = Class(name="soaml::ServiceArchitecture")
Collaboration = Class(name="Collaboration")
soaml_ServiceContract = Class(name="soaml::ServiceContract")
soaml_CollaborationUse = Class(name="soaml::CollaborationUse")
soaml_Consumer = Class(name="soaml::Consumer")
soaml_Interface = Class(name="soaml::Interface")
soaml_Class = Class(name="soaml::Class")
soaml_Provider = Class(name="soaml::Provider")
soaml_MotivationRealization = Class(name="soaml::MotivationRealization")
soaml_Realization = Class(name="soaml::Realization")
soaml_ServiceInterface = Class(name="soaml::ServiceInterface")
soaml_Participant = Class(name="soaml::Participant")
soaml_Agent = Class(name="soaml::Agent")
soaml_Property = Class(name="soaml::Property")
soaml_Attachment = Class(name="soaml::Attachment")
soaml_MessageType = Class(name="soaml::MessageType")
soaml_DataType = Class(name="soaml::DataType")
soaml_Signal = Class(name="soaml::Signal")
soaml_Milestone = Class(name="soaml::Milestone")
soaml_ValueSpecification = Class(name="soaml::ValueSpecification")
soaml_Comment = Class(name="soaml::Comment")
soaml_Capability = Class(name="soaml::Capability")
soaml_Expose = Class(name="soaml::Expose")
soaml_Dependency = Class(name="soaml::Dependency")
soaml_NodeDescriptor = Class(name="soaml::NodeDescriptor")
soaml_Artifact = Class(name="soaml::Artifact")
soaml_Catalog = Class(name="soaml::Catalog")
NodeDescriptor = Class(name="NodeDescriptor")
soaml_Package = Class(name="soaml::Package")
Participant = Class(name="Participant")
soaml_Port = Class(name="soaml::Port")
soaml_Request = Class(name="soaml::Request")
soaml_Service = Class(name="soaml::Service")
soaml_ServiceChannel = Class(name="soaml::ServiceChannel")
soaml_Connector = Class(name="soaml::Connector")
soaml_Category = Class(name="soaml::Category")
soaml_FreeFormDescriptor = Class(name="soaml::FreeFormDescriptor")
soaml_FreeFormValue = Class(name="soaml::FreeFormValue")
soaml_CategoryValue = Class(name="soaml::CategoryValue")
FreeFormValue = Class(name="FreeFormValue")
soaml_Categorization = Class(name="soaml::Categorization")

# soaml_Collaboration class attributes and methods
soaml_Collaboration_isStrict: Property = Property(name="isStrict", type=StringType)
soaml_Collaboration.attributes={soaml_Collaboration_isStrict}

# soaml_ServiceArchitecture class attributes and methods

# Collaboration class attributes and methods

# soaml_ServiceContract class attributes and methods

# soaml_CollaborationUse class attributes and methods
soaml_CollaborationUse_isStrict: Property = Property(name="isStrict", type=StringType)
soaml_CollaborationUse.attributes={soaml_CollaborationUse_isStrict}

# soaml_Consumer class attributes and methods

# soaml_Interface class attributes and methods

# soaml_Class class attributes and methods

# soaml_Provider class attributes and methods

# soaml_MotivationRealization class attributes and methods

# soaml_Realization class attributes and methods

# soaml_ServiceInterface class attributes and methods

# soaml_Participant class attributes and methods

# soaml_Agent class attributes and methods

# soaml_Property class attributes and methods
soaml_Property_isID: Property = Property(name="isID", type=StringType)
soaml_Property.attributes={soaml_Property_isID}

# soaml_Attachment class attributes and methods
soaml_Attachment_encoding: Property = Property(name="encoding", type=StringType)
soaml_Attachment_mimeType: Property = Property(name="mimeType", type=StringType)
soaml_Attachment.attributes={soaml_Attachment_encoding, soaml_Attachment_mimeType}

# soaml_MessageType class attributes and methods
soaml_MessageType_encoding: Property = Property(name="encoding", type=StringType)
soaml_MessageType.attributes={soaml_MessageType_encoding}

# soaml_DataType class attributes and methods

# soaml_Signal class attributes and methods

# soaml_Milestone class attributes and methods
soaml_Milestone_progress: Property = Property(name="progress", type=StringType)
soaml_Milestone.attributes={soaml_Milestone_progress}

# soaml_ValueSpecification class attributes and methods

# soaml_Comment class attributes and methods

# soaml_Capability class attributes and methods

# soaml_Expose class attributes and methods

# soaml_Dependency class attributes and methods

# soaml_NodeDescriptor class attributes and methods

# soaml_Artifact class attributes and methods

# soaml_Catalog class attributes and methods

# NodeDescriptor class attributes and methods

# soaml_Package class attributes and methods

# Participant class attributes and methods

# soaml_Port class attributes and methods
soaml_Port_connectorRequired: Property = Property(name="connectorRequired", type=StringType)
soaml_Port.attributes={soaml_Port_connectorRequired}

# soaml_Request class attributes and methods

# soaml_Service class attributes and methods

# soaml_ServiceChannel class attributes and methods

# soaml_Connector class attributes and methods

# soaml_Category class attributes and methods

# soaml_FreeFormDescriptor class attributes and methods

# soaml_FreeFormValue class attributes and methods

# soaml_CategoryValue class attributes and methods

# FreeFormValue class attributes and methods

# soaml_Categorization class attributes and methods

# Relationships
base_Collaboration1: BinaryAssociation = BinaryAssociation(
    name="base_Collaboration1",
    ends={
        Property(name="soaml_Collaboration", type=soaml_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="soaml_Collaboration0", type=soaml_Collaboration, multiplicity=Multiplicity(1, 1))
    }
)
base_CollaborationUse3: BinaryAssociation = BinaryAssociation(
    name="base_CollaborationUse3",
    ends={
        Property(name="soaml_CollaborationUse", type=soaml_CollaborationUse, multiplicity=Multiplicity(1, 1)),
        Property(name="soaml_CollaborationUse2", type=soaml_CollaborationUse, multiplicity=Multiplicity(1, 1))
    }
)
base_Interface4: BinaryAssociation = BinaryAssociation(
    name="base_Interface4",
    ends={
        Property(name="soaml_Interface", type=soaml_Consumer, multiplicity=Multiplicity(1, 1)),
        Property(name="soaml_Consumer", type=soaml_Interface, multiplicity=Multiplicity(1, 1))
    }
)
base_Class5: BinaryAssociation = BinaryAssociation(
    name="base_Class5",
    ends={
        Property(name="soaml_Class", type=soaml_Consumer, multiplicity=Multiplicity(1, 1)),
        Property(name="soaml_Consumer6", type=soaml_Class, multiplicity=Multiplicity(1, 1))
    }
)
base_Interface7: BinaryAssociation = BinaryAssociation(
    name="base_Interface7",
    ends={
        Property(name="soaml_Interface8", type=soaml_Provider, multiplicity=Multiplicity(1, 1)),
        Property(name="soaml_Provider", type=soaml_Interface, multiplicity=Multiplicity(1, 1))
    }
)
base_Class9: BinaryAssociation = BinaryAssociation(
    name="base_Class9",
    ends={
        Property(name="soaml_Class11", type=soaml_Provider, multiplicity=Multiplicity(1, 1)),
        Property(name="soaml_Provider10", type=soaml_Class, multiplicity=Multiplicity(1, 1))
    }
)
base_Realization12: BinaryAssociation = BinaryAssociation(
    name="base_Realization12",
    ends={
        Property(name="soaml_Realization", type=soaml_MotivationRealization, multiplicity=Multiplicity(1, 1)),
        Property(name="soaml_MotivationRealization", type=soaml_Realization, multiplicity=Multiplicity(1, 1))
    }
)
base_Interface13: BinaryAssociation = BinaryAssociation(
    name="base_Interface13",
    ends={
        Property(name="soaml_Interface14", type=soaml_ServiceInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="soaml_ServiceInterface", type=soaml_Interface, multiplicity=Multiplicity(1, 1))
    }
)
base_Class15: BinaryAssociation = BinaryAssociation(
    name="base_Class15",
    ends={
        Property(name="soaml_Class17", type=soaml_ServiceInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="soaml_ServiceInterface16", type=soaml_Class, multiplicity=Multiplicity(1, 1))
    }
)
base_Class18: BinaryAssociation = BinaryAssociation(
    name="base_Class18",
    ends={
        Property(name="soaml_Class19", type=soaml_Participant, multiplicity=Multiplicity(1, 1)),
        Property(name="soaml_Participant", type=soaml_Class, multiplicity=Multiplicity(1, 1))
    }
)
base_Property28: BinaryAssociation = BinaryAssociation(
    name="base_Property28",
    ends={
        Property(name="soaml_Property", type=soaml_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="soaml_Property27", type=soaml_Property, multiplicity=Multiplicity(1, 1))
    }
)
base_Property29: BinaryAssociation = BinaryAssociation(
    name="base_Property29",
    ends={
        Property(name="soaml_Property30", type=soaml_Attachment, multiplicity=Multiplicity(1, 1)),
        Property(name="soaml_Attachment", type=soaml_Property, multiplicity=Multiplicity(1, 1))
    }
)
base_Class31: BinaryAssociation = BinaryAssociation(
    name="base_Class31",
    ends={
        Property(name="soaml_Class32", type=soaml_MessageType, multiplicity=Multiplicity(1, 1)),
        Property(name="soaml_MessageType", type=soaml_Class, multiplicity=Multiplicity(1, 1))
    }
)
base_DataType33: BinaryAssociation = BinaryAssociation(
    name="base_DataType33",
    ends={
        Property(name="soaml_DataType", type=soaml_MessageType, multiplicity=Multiplicity(1, 1)),
        Property(name="soaml_MessageType34", type=soaml_DataType, multiplicity=Multiplicity(1, 1))
    }
)
base_Signal35: BinaryAssociation = BinaryAssociation(
    name="base_Signal35",
    ends={
        Property(name="soaml_Signal", type=soaml_MessageType, multiplicity=Multiplicity(1, 1)),
        Property(name="soaml_MessageType36", type=soaml_Signal, multiplicity=Multiplicity(1, 1))
    }
)
value37: BinaryAssociation = BinaryAssociation(
    name="value37",
    ends={
        Property(name="soaml_ValueSpecification", type=soaml_Milestone, multiplicity=Multiplicity(1, 1)),
        Property(name="soaml_Milestone", type=soaml_ValueSpecification, multiplicity=Multiplicity(0, 9999))
    }
)
signal38: BinaryAssociation = BinaryAssociation(
    name="signal38",
    ends={
        Property(name="soaml_Signal40", type=soaml_Milestone, multiplicity=Multiplicity(1, 1)),
        Property(name="soaml_Milestone39", type=soaml_Signal, multiplicity=Multiplicity(0, 1))
    }
)
base_Comment41: BinaryAssociation = BinaryAssociation(
    name="base_Comment41",
    ends={
        Property(name="soaml_Comment", type=soaml_Milestone, multiplicity=Multiplicity(1, 1)),
        Property(name="soaml_Milestone42", type=soaml_Comment, multiplicity=Multiplicity(1, 1))
    }
)
base_Class43: BinaryAssociation = BinaryAssociation(
    name="base_Class43",
    ends={
        Property(name="soaml_Class44", type=soaml_Capability, multiplicity=Multiplicity(1, 1)),
        Property(name="soaml_Capability", type=soaml_Class, multiplicity=Multiplicity(1, 1))
    }
)
base_Dependency45: BinaryAssociation = BinaryAssociation(
    name="base_Dependency45",
    ends={
        Property(name="soaml_Dependency", type=soaml_Expose, multiplicity=Multiplicity(1, 1)),
        Property(name="soaml_Expose", type=soaml_Dependency, multiplicity=Multiplicity(1, 1))
    }
)
base_Artifact46: BinaryAssociation = BinaryAssociation(
    name="base_Artifact46",
    ends={
        Property(name="soaml_Artifact", type=soaml_NodeDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="soaml_NodeDescriptor", type=soaml_Artifact, multiplicity=Multiplicity(1, 1))
    }
)
base_Package47: BinaryAssociation = BinaryAssociation(
    name="base_Package47",
    ends={
        Property(name="soaml_Package", type=soaml_Catalog, multiplicity=Multiplicity(1, 1)),
        Property(name="soaml_Catalog", type=soaml_Package, multiplicity=Multiplicity(1, 1))
    }
)
base_Port21: BinaryAssociation = BinaryAssociation(
    name="base_Port21",
    ends={
        Property(name="soaml_Port", type=soaml_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="soaml_Port20", type=soaml_Port, multiplicity=Multiplicity(1, 1))
    }
)
base_Port22: BinaryAssociation = BinaryAssociation(
    name="base_Port22",
    ends={
        Property(name="soaml_Port23", type=soaml_Request, multiplicity=Multiplicity(1, 1)),
        Property(name="soaml_Request", type=soaml_Port, multiplicity=Multiplicity(1, 1))
    }
)
base_Port24: BinaryAssociation = BinaryAssociation(
    name="base_Port24",
    ends={
        Property(name="soaml_Port25", type=soaml_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="soaml_Service", type=soaml_Port, multiplicity=Multiplicity(1, 1))
    }
)
base_Connector26: BinaryAssociation = BinaryAssociation(
    name="base_Connector26",
    ends={
        Property(name="soaml_Connector", type=soaml_ServiceChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="soaml_ServiceChannel", type=soaml_Connector, multiplicity=Multiplicity(1, 1))
    }
)
base_Property48: BinaryAssociation = BinaryAssociation(
    name="base_Property48",
    ends={
        Property(name="soaml_Property49", type=soaml_FreeFormDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="soaml_FreeFormDescriptor", type=soaml_Property, multiplicity=Multiplicity(1, 1))
    }
)
base_ValueSpecification50: BinaryAssociation = BinaryAssociation(
    name="base_ValueSpecification50",
    ends={
        Property(name="soaml_ValueSpecification51", type=soaml_FreeFormValue, multiplicity=Multiplicity(1, 1)),
        Property(name="soaml_FreeFormValue", type=soaml_ValueSpecification, multiplicity=Multiplicity(1, 1))
    }
)
base_Dependency52: BinaryAssociation = BinaryAssociation(
    name="base_Dependency52",
    ends={
        Property(name="soaml_Dependency53", type=soaml_Categorization, multiplicity=Multiplicity(1, 1)),
        Property(name="soaml_Categorization", type=soaml_Dependency, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_soaml_ServiceArchitecture_Collaboration = Generalization(general=Collaboration, specific=soaml_ServiceArchitecture)
gen_soaml_ServiceContract_Collaboration = Generalization(general=Collaboration, specific=soaml_ServiceContract)
gen_soaml_Catalog_NodeDescriptor = Generalization(general=NodeDescriptor, specific=soaml_Catalog)
gen_soaml_Agent_Participant = Generalization(general=Participant, specific=soaml_Agent)
gen_soaml_Category_NodeDescriptor = Generalization(general=NodeDescriptor, specific=soaml_Category)
gen_soaml_CategoryValue_FreeFormValue = Generalization(general=FreeFormValue, specific=soaml_CategoryValue)

# Domain Model
domain_model = DomainModel(
    name="soaml",
    types={soaml_Collaboration, soaml_ServiceArchitecture, Collaboration, soaml_ServiceContract, soaml_CollaborationUse, soaml_Consumer, soaml_Interface, soaml_Class, soaml_Provider, soaml_MotivationRealization, soaml_Realization, soaml_ServiceInterface, soaml_Participant, soaml_Agent, soaml_Property, soaml_Attachment, soaml_MessageType, soaml_DataType, soaml_Signal, soaml_Milestone, soaml_ValueSpecification, soaml_Comment, soaml_Capability, soaml_Expose, soaml_Dependency, soaml_NodeDescriptor, soaml_Artifact, soaml_Catalog, NodeDescriptor, soaml_Package, Participant, soaml_Port, soaml_Request, soaml_Service, soaml_ServiceChannel, soaml_Connector, soaml_Category, soaml_FreeFormDescriptor, soaml_FreeFormValue, soaml_CategoryValue, FreeFormValue, soaml_Categorization},
    associations={base_Collaboration1, base_CollaborationUse3, base_Interface4, base_Class5, base_Interface7, base_Class9, base_Realization12, base_Interface13, base_Class15, base_Class18, base_Property28, base_Property29, base_Class31, base_DataType33, base_Signal35, value37, signal38, base_Comment41, base_Class43, base_Dependency45, base_Artifact46, base_Package47, base_Port21, base_Port22, base_Port24, base_Connector26, base_Property48, base_ValueSpecification50, base_Dependency52},
    generalizations={gen_soaml_ServiceArchitecture_Collaboration, gen_soaml_ServiceContract_Collaboration, gen_soaml_Catalog_NodeDescriptor, gen_soaml_Agent_Participant, gen_soaml_Category_NodeDescriptor, gen_soaml_CategoryValue_FreeFormValue},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)