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
ArchimateTechnology_NodeElement = Class(name="ArchimateTechnology::NodeElement", is_abstract=True)
ArchimateTechnology_Node = Class(name="ArchimateTechnology::Node")
NodeElement = Class(name="NodeElement")
ArchimateTechnology_Device = Class(name="ArchimateTechnology::Device")
ArchimateTechnology_Network = Class(name="ArchimateTechnology::Network")
ArchimateTechnology_CommunicationPath = Class(name="ArchimateTechnology::CommunicationPath")
ArchimateTechnology_InfrastructureInterface = Class(name="ArchimateTechnology::InfrastructureInterface")
ArchimateTechnology_SystemSoftware = Class(name="ArchimateTechnology::SystemSoftware")
ArchimateTechnology_InfrastructureFunction = Class(name="ArchimateTechnology::InfrastructureFunction")
ArchimateTechnology_InfrastructureService = Class(name="ArchimateTechnology::InfrastructureService")
ArchimateTechnology_Artifact = Class(name="ArchimateTechnology::Artifact")
ArchimateTechnology_Grouping = Class(name="ArchimateTechnology::Grouping")
ArchimateTechnology_Junction = Class(name="ArchimateTechnology::Junction")
Relationship = Class(name="Relationship")
ArchimateTechnology_Relationship = Class(name="ArchimateTechnology::Relationship", is_abstract=True)
ArchimateTechnology_Association = Class(name="ArchimateTechnology::Association")
ArchimateTechnology_UsedBy = Class(name="ArchimateTechnology::UsedBy")
ArchimateTechnology_Realization = Class(name="ArchimateTechnology::Realization")
ArchimateTechnology_Assignment = Class(name="ArchimateTechnology::Assignment")
ArchimateTechnology_Aggregation = Class(name="ArchimateTechnology::Aggregation")
ArchimateTechnology_Composition = Class(name="ArchimateTechnology::Composition")
ArchimateTechnology_Flow = Class(name="ArchimateTechnology::Flow")
ArchimateTechnology_Triggering = Class(name="ArchimateTechnology::Triggering")
ArchimateTechnology_Specialization = Class(name="ArchimateTechnology::Specialization")
ArchimateTechnology_Access = Class(name="ArchimateTechnology::Access")

# ArchimateTechnology_NodeElement class attributes and methods

# ArchimateTechnology_Node class attributes and methods

# NodeElement class attributes and methods

# ArchimateTechnology_Device class attributes and methods

# ArchimateTechnology_Network class attributes and methods

# ArchimateTechnology_CommunicationPath class attributes and methods

# ArchimateTechnology_InfrastructureInterface class attributes and methods

# ArchimateTechnology_SystemSoftware class attributes and methods

# ArchimateTechnology_InfrastructureFunction class attributes and methods

# ArchimateTechnology_InfrastructureService class attributes and methods

# ArchimateTechnology_Artifact class attributes and methods

# ArchimateTechnology_Grouping class attributes and methods

# ArchimateTechnology_Junction class attributes and methods

# Relationship class attributes and methods

# ArchimateTechnology_Relationship class attributes and methods

# ArchimateTechnology_Association class attributes and methods

# ArchimateTechnology_UsedBy class attributes and methods

# ArchimateTechnology_Realization class attributes and methods

# ArchimateTechnology_Assignment class attributes and methods

# ArchimateTechnology_Aggregation class attributes and methods

# ArchimateTechnology_Composition class attributes and methods

# ArchimateTechnology_Flow class attributes and methods

# ArchimateTechnology_Triggering class attributes and methods

# ArchimateTechnology_Specialization class attributes and methods

# ArchimateTechnology_Access class attributes and methods

# Relationships
source0: BinaryAssociation = BinaryAssociation(
    name="source0",
    ends={
        Property(name="ArchimateTechnology_NodeElement", type=ArchimateTechnology_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="ArchimateTechnology_Relationship", type=ArchimateTechnology_NodeElement, multiplicity=Multiplicity(1, 1))
    }
)
target1: BinaryAssociation = BinaryAssociation(
    name="target1",
    ends={
        Property(name="ArchimateTechnology_NodeElement3", type=ArchimateTechnology_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="ArchimateTechnology_Relationship2", type=ArchimateTechnology_NodeElement, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_ArchimateTechnology_Node_NodeElement = Generalization(general=NodeElement, specific=ArchimateTechnology_Node)
gen_ArchimateTechnology_Device_NodeElement = Generalization(general=NodeElement, specific=ArchimateTechnology_Device)
gen_ArchimateTechnology_Network_NodeElement = Generalization(general=NodeElement, specific=ArchimateTechnology_Network)
gen_ArchimateTechnology_CommunicationPath_NodeElement = Generalization(general=NodeElement, specific=ArchimateTechnology_CommunicationPath)
gen_ArchimateTechnology_InfrastructureInterface_NodeElement = Generalization(general=NodeElement, specific=ArchimateTechnology_InfrastructureInterface)
gen_ArchimateTechnology_SystemSoftware_NodeElement = Generalization(general=NodeElement, specific=ArchimateTechnology_SystemSoftware)
gen_ArchimateTechnology_InfrastructureFunction_NodeElement = Generalization(general=NodeElement, specific=ArchimateTechnology_InfrastructureFunction)
gen_ArchimateTechnology_InfrastructureService_NodeElement = Generalization(general=NodeElement, specific=ArchimateTechnology_InfrastructureService)
gen_ArchimateTechnology_Artifact_NodeElement = Generalization(general=NodeElement, specific=ArchimateTechnology_Artifact)
gen_ArchimateTechnology_Grouping_NodeElement = Generalization(general=NodeElement, specific=ArchimateTechnology_Grouping)
gen_ArchimateTechnology_Junction_Relationship = Generalization(general=Relationship, specific=ArchimateTechnology_Junction)
gen_ArchimateTechnology_Association_Relationship = Generalization(general=Relationship, specific=ArchimateTechnology_Association)
gen_ArchimateTechnology_UsedBy_Relationship = Generalization(general=Relationship, specific=ArchimateTechnology_UsedBy)
gen_ArchimateTechnology_Realization_Relationship = Generalization(general=Relationship, specific=ArchimateTechnology_Realization)
gen_ArchimateTechnology_Assignment_Relationship = Generalization(general=Relationship, specific=ArchimateTechnology_Assignment)
gen_ArchimateTechnology_Aggregation_Relationship = Generalization(general=Relationship, specific=ArchimateTechnology_Aggregation)
gen_ArchimateTechnology_Composition_Relationship = Generalization(general=Relationship, specific=ArchimateTechnology_Composition)
gen_ArchimateTechnology_Flow_Relationship = Generalization(general=Relationship, specific=ArchimateTechnology_Flow)
gen_ArchimateTechnology_Triggering_Relationship = Generalization(general=Relationship, specific=ArchimateTechnology_Triggering)
gen_ArchimateTechnology_Specialization_Relationship = Generalization(general=Relationship, specific=ArchimateTechnology_Specialization)
gen_ArchimateTechnology_Access_Relationship = Generalization(general=Relationship, specific=ArchimateTechnology_Access)

# Domain Model
domain_model = DomainModel(
    name="ArchimateTechnology",
    types={ArchimateTechnology_NodeElement, ArchimateTechnology_Node, NodeElement, ArchimateTechnology_Device, ArchimateTechnology_Network, ArchimateTechnology_CommunicationPath, ArchimateTechnology_InfrastructureInterface, ArchimateTechnology_SystemSoftware, ArchimateTechnology_InfrastructureFunction, ArchimateTechnology_InfrastructureService, ArchimateTechnology_Artifact, ArchimateTechnology_Grouping, ArchimateTechnology_Junction, Relationship, ArchimateTechnology_Relationship, ArchimateTechnology_Association, ArchimateTechnology_UsedBy, ArchimateTechnology_Realization, ArchimateTechnology_Assignment, ArchimateTechnology_Aggregation, ArchimateTechnology_Composition, ArchimateTechnology_Flow, ArchimateTechnology_Triggering, ArchimateTechnology_Specialization, ArchimateTechnology_Access},
    associations={source0, target1},
    generalizations={gen_ArchimateTechnology_Node_NodeElement, gen_ArchimateTechnology_Device_NodeElement, gen_ArchimateTechnology_Network_NodeElement, gen_ArchimateTechnology_CommunicationPath_NodeElement, gen_ArchimateTechnology_InfrastructureInterface_NodeElement, gen_ArchimateTechnology_SystemSoftware_NodeElement, gen_ArchimateTechnology_InfrastructureFunction_NodeElement, gen_ArchimateTechnology_InfrastructureService_NodeElement, gen_ArchimateTechnology_Artifact_NodeElement, gen_ArchimateTechnology_Grouping_NodeElement, gen_ArchimateTechnology_Junction_Relationship, gen_ArchimateTechnology_Association_Relationship, gen_ArchimateTechnology_UsedBy_Relationship, gen_ArchimateTechnology_Realization_Relationship, gen_ArchimateTechnology_Assignment_Relationship, gen_ArchimateTechnology_Aggregation_Relationship, gen_ArchimateTechnology_Composition_Relationship, gen_ArchimateTechnology_Flow_Relationship, gen_ArchimateTechnology_Triggering_Relationship, gen_ArchimateTechnology_Specialization_Relationship, gen_ArchimateTechnology_Access_Relationship},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)