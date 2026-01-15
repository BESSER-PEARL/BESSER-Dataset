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
projectPlanning_ProjectPlan = Class(name="projectPlanning::ProjectPlan")
projectPlanning_Capability = Class(name="projectPlanning::Capability")
projectPlanning_Employee = Class(name="projectPlanning::Employee")
projectPlanning_Project = Class(name="projectPlanning::Project")
projectPlanning_Rating = Class(name="projectPlanning::Rating")
projectPlanning_Assignment = Class(name="projectPlanning::Assignment")

# projectPlanning_ProjectPlan class attributes and methods

# projectPlanning_Capability class attributes and methods
projectPlanning_Capability_name: Property = Property(name="name", type=StringType)
projectPlanning_Capability.attributes={projectPlanning_Capability_name}

# projectPlanning_Employee class attributes and methods
projectPlanning_Employee_name: Property = Property(name="name", type=StringType)
projectPlanning_Employee_hasResource: Property = Property(name="hasResource", type=IntegerType)
projectPlanning_Employee.attributes={projectPlanning_Employee_name, projectPlanning_Employee_hasResource}

# projectPlanning_Project class attributes and methods
projectPlanning_Project_name: Property = Property(name="name", type=StringType)
projectPlanning_Project_requiresResources: Property = Property(name="requiresResources", type=IntegerType)
projectPlanning_Project.attributes={projectPlanning_Project_requiresResources, projectPlanning_Project_name}

# projectPlanning_Rating class attributes and methods
projectPlanning_Rating_rating: Property = Property(name="rating", type=IntegerType)
projectPlanning_Rating.attributes={projectPlanning_Rating_rating}

# projectPlanning_Assignment class attributes and methods

# Relationships
capabilities0: BinaryAssociation = BinaryAssociation(
    name="capabilities0",
    ends={
        Property(name="projectPlanning_Capability", type=projectPlanning_ProjectPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="projectPlanning_ProjectPlan", type=projectPlanning_Capability, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
employees1: BinaryAssociation = BinaryAssociation(
    name="employees1",
    ends={
        Property(name="projectPlanning_Employee", type=projectPlanning_ProjectPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="projectPlanning_ProjectPlan2", type=projectPlanning_Employee, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
projects3: BinaryAssociation = BinaryAssociation(
    name="projects3",
    ends={
        Property(name="projectPlanning_Project", type=projectPlanning_ProjectPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="projectPlanning_ProjectPlan4", type=projectPlanning_Project, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ratings5: BinaryAssociation = BinaryAssociation(
    name="ratings5",
    ends={
        Property(name="projectPlanning_Rating", type=projectPlanning_ProjectPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="projectPlanning_ProjectPlan6", type=projectPlanning_Rating, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assignments7: BinaryAssociation = BinaryAssociation(
    name="assignments7",
    ends={
        Property(name="projectPlanning_Assignment", type=projectPlanning_ProjectPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="projectPlanning_ProjectPlan8", type=projectPlanning_Assignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiresCapabilities9: BinaryAssociation = BinaryAssociation(
    name="requiresCapabilities9",
    ends={
        Property(name="projectPlanning_Capability11", type=projectPlanning_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="projectPlanning_Project10", type=projectPlanning_Capability, multiplicity=Multiplicity(0, 9999))
    }
)
hasCapabilities12: BinaryAssociation = BinaryAssociation(
    name="hasCapabilities12",
    ends={
        Property(name="projectPlanning_Capability14", type=projectPlanning_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="projectPlanning_Employee13", type=projectPlanning_Capability, multiplicity=Multiplicity(0, 9999))
    }
)
ratings15: BinaryAssociation = BinaryAssociation(
    name="ratings15",
    ends={
        Property(name="projectPlanning_Rating17", type=projectPlanning_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="projectPlanning_Employee16", type=projectPlanning_Rating, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
project21: BinaryAssociation = BinaryAssociation(
    name="project21",
    ends={
        Property(name="projectPlanning_Project23", type=projectPlanning_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="projectPlanning_Assignment22", type=projectPlanning_Project, multiplicity=Multiplicity(0, 1))
    }
)
employee24: BinaryAssociation = BinaryAssociation(
    name="employee24",
    ends={
        Property(name="projectPlanning_Employee26", type=projectPlanning_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="projectPlanning_Assignment25", type=projectPlanning_Employee, multiplicity=Multiplicity(0, 1))
    }
)
capability18: BinaryAssociation = BinaryAssociation(
    name="capability18",
    ends={
        Property(name="projectPlanning_Capability20", type=projectPlanning_Rating, multiplicity=Multiplicity(1, 1)),
        Property(name="projectPlanning_Rating19", type=projectPlanning_Capability, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="projectPlanning",
    types={projectPlanning_ProjectPlan, projectPlanning_Capability, projectPlanning_Employee, projectPlanning_Project, projectPlanning_Rating, projectPlanning_Assignment},
    associations={capabilities0, employees1, projects3, ratings5, assignments7, requiresCapabilities9, hasCapabilities12, ratings15, project21, employee24, capability18},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)