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
ArchimateApplication_Junction = Class(name="ArchimateApplication::Junction")
ArchimateApplication_Relationship = Class(name="ArchimateApplication::Relationship", is_abstract=True)
ArchimateApplication_NodeElement = Class(name="ArchimateApplication::NodeElement", is_abstract=True)
ArchimateApplication_ApplicationComponent = Class(name="ArchimateApplication::ApplicationComponent")
NodeElement = Class(name="NodeElement")
ArchimateApplication_ApplicationCollaboration = Class(name="ArchimateApplication::ApplicationCollaboration")
ArchimateApplication_ApplicationInterface = Class(name="ArchimateApplication::ApplicationInterface")
ArchimateApplication_ApplicationFunction = Class(name="ArchimateApplication::ApplicationFunction")
ArchimateApplication_ApplicationInteraction = Class(name="ArchimateApplication::ApplicationInteraction")
ArchimateApplication_ApplicationService = Class(name="ArchimateApplication::ApplicationService")
ArchimateApplication_DataObject = Class(name="ArchimateApplication::DataObject")
ArchimateApplication_Grouping = Class(name="ArchimateApplication::Grouping")
ArchimateApplication_Triggering = Class(name="ArchimateApplication::Triggering")
ArchimateApplication_Specialization = Class(name="ArchimateApplication::Specialization")
ArchimateApplication_Association = Class(name="ArchimateApplication::Association")
Relationship = Class(name="Relationship")
ArchimateApplication_Aggregation = Class(name="ArchimateApplication::Aggregation")
ArchimateApplication_Realization = Class(name="ArchimateApplication::Realization")
ArchimateApplication_Access = Class(name="ArchimateApplication::Access")
ArchimateApplication_UsedBy = Class(name="ArchimateApplication::UsedBy")
ArchimateApplication_Assignment = Class(name="ArchimateApplication::Assignment")
ArchimateApplication_Composition = Class(name="ArchimateApplication::Composition")
ArchimateApplication_Flow = Class(name="ArchimateApplication::Flow")

# ArchimateApplication_Junction class attributes and methods

# ArchimateApplication_Relationship class attributes and methods

# ArchimateApplication_NodeElement class attributes and methods

# ArchimateApplication_ApplicationComponent class attributes and methods

# NodeElement class attributes and methods

# ArchimateApplication_ApplicationCollaboration class attributes and methods

# ArchimateApplication_ApplicationInterface class attributes and methods

# ArchimateApplication_ApplicationFunction class attributes and methods

# ArchimateApplication_ApplicationInteraction class attributes and methods

# ArchimateApplication_ApplicationService class attributes and methods

# ArchimateApplication_DataObject class attributes and methods

# ArchimateApplication_Grouping class attributes and methods

# ArchimateApplication_Triggering class attributes and methods

# ArchimateApplication_Specialization class attributes and methods

# ArchimateApplication_Association class attributes and methods

# Relationship class attributes and methods

# ArchimateApplication_Aggregation class attributes and methods

# ArchimateApplication_Realization class attributes and methods

# ArchimateApplication_Access class attributes and methods

# ArchimateApplication_UsedBy class attributes and methods

# ArchimateApplication_Assignment class attributes and methods

# ArchimateApplication_Composition class attributes and methods

# ArchimateApplication_Flow class attributes and methods

# Relationships
source0: BinaryAssociation = BinaryAssociation(
    name="source0",
    ends={
        Property(name="ArchimateApplication_NodeElement", type=ArchimateApplication_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="ArchimateApplication_Relationship", type=ArchimateApplication_NodeElement, multiplicity=Multiplicity(1, 1))
    }
)
target1: BinaryAssociation = BinaryAssociation(
    name="target1",
    ends={
        Property(name="ArchimateApplication_NodeElement3", type=ArchimateApplication_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="ArchimateApplication_Relationship2", type=ArchimateApplication_NodeElement, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_ArchimateApplication_Junction_NodeElement = Generalization(general=NodeElement, specific=ArchimateApplication_Junction)
gen_ArchimateApplication_ApplicationComponent_NodeElement = Generalization(general=NodeElement, specific=ArchimateApplication_ApplicationComponent)
gen_ArchimateApplication_ApplicationCollaboration_NodeElement = Generalization(general=NodeElement, specific=ArchimateApplication_ApplicationCollaboration)
gen_ArchimateApplication_ApplicationInterface_NodeElement = Generalization(general=NodeElement, specific=ArchimateApplication_ApplicationInterface)
gen_ArchimateApplication_ApplicationFunction_NodeElement = Generalization(general=NodeElement, specific=ArchimateApplication_ApplicationFunction)
gen_ArchimateApplication_ApplicationInteraction_NodeElement = Generalization(general=NodeElement, specific=ArchimateApplication_ApplicationInteraction)
gen_ArchimateApplication_ApplicationService_NodeElement = Generalization(general=NodeElement, specific=ArchimateApplication_ApplicationService)
gen_ArchimateApplication_DataObject_NodeElement = Generalization(general=NodeElement, specific=ArchimateApplication_DataObject)
gen_ArchimateApplication_Grouping_NodeElement = Generalization(general=NodeElement, specific=ArchimateApplication_Grouping)
gen_ArchimateApplication_Flow_Relationship = Generalization(general=Relationship, specific=ArchimateApplication_Flow)
gen_ArchimateApplication_Triggering_Relationship = Generalization(general=Relationship, specific=ArchimateApplication_Triggering)
gen_ArchimateApplication_Specialization_Relationship = Generalization(general=Relationship, specific=ArchimateApplication_Specialization)
gen_ArchimateApplication_Association_Relationship = Generalization(general=Relationship, specific=ArchimateApplication_Association)
gen_ArchimateApplication_Aggregation_Relationship = Generalization(general=Relationship, specific=ArchimateApplication_Aggregation)
gen_ArchimateApplication_Realization_Relationship = Generalization(general=Relationship, specific=ArchimateApplication_Realization)
gen_ArchimateApplication_Access_Relationship = Generalization(general=Relationship, specific=ArchimateApplication_Access)
gen_ArchimateApplication_UsedBy_Relationship = Generalization(general=Relationship, specific=ArchimateApplication_UsedBy)
gen_ArchimateApplication_Assignment_Relationship = Generalization(general=Relationship, specific=ArchimateApplication_Assignment)
gen_ArchimateApplication_Composition_Relationship = Generalization(general=Relationship, specific=ArchimateApplication_Composition)

# Domain Model
domain_model = DomainModel(
    name="ArchimateApplication",
    types={ArchimateApplication_Junction, ArchimateApplication_Relationship, ArchimateApplication_NodeElement, ArchimateApplication_ApplicationComponent, NodeElement, ArchimateApplication_ApplicationCollaboration, ArchimateApplication_ApplicationInterface, ArchimateApplication_ApplicationFunction, ArchimateApplication_ApplicationInteraction, ArchimateApplication_ApplicationService, ArchimateApplication_DataObject, ArchimateApplication_Grouping, ArchimateApplication_Triggering, ArchimateApplication_Specialization, ArchimateApplication_Association, Relationship, ArchimateApplication_Aggregation, ArchimateApplication_Realization, ArchimateApplication_Access, ArchimateApplication_UsedBy, ArchimateApplication_Assignment, ArchimateApplication_Composition, ArchimateApplication_Flow},
    associations={source0, target1},
    generalizations={gen_ArchimateApplication_Junction_NodeElement, gen_ArchimateApplication_ApplicationComponent_NodeElement, gen_ArchimateApplication_ApplicationCollaboration_NodeElement, gen_ArchimateApplication_ApplicationInterface_NodeElement, gen_ArchimateApplication_ApplicationFunction_NodeElement, gen_ArchimateApplication_ApplicationInteraction_NodeElement, gen_ArchimateApplication_ApplicationService_NodeElement, gen_ArchimateApplication_DataObject_NodeElement, gen_ArchimateApplication_Grouping_NodeElement, gen_ArchimateApplication_Flow_Relationship, gen_ArchimateApplication_Triggering_Relationship, gen_ArchimateApplication_Specialization_Relationship, gen_ArchimateApplication_Association_Relationship, gen_ArchimateApplication_Aggregation_Relationship, gen_ArchimateApplication_Realization_Relationship, gen_ArchimateApplication_Access_Relationship, gen_ArchimateApplication_UsedBy_Relationship, gen_ArchimateApplication_Assignment_Relationship, gen_ArchimateApplication_Composition_Relationship},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)