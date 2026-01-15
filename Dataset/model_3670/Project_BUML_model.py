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
Project_Employee = Class(name="Project::Employee")
Project_Department = Class(name="Project::Department")
Project_Project = Class(name="Project::Project")

# Project_Employee class attributes and methods
Project_Employee_name: Property = Property(name="name", type=StringType)
Project_Employee_salary: Property = Property(name="salary", type=IntegerType)
Project_Employee.attributes={Project_Employee_name, Project_Employee_salary}

# Project_Department class attributes and methods
Project_Department_location: Property = Property(name="location", type=StringType)
Project_Department_name: Property = Property(name="name", type=StringType)
Project_Department_budget: Property = Property(name="budget", type=IntegerType)
Project_Department.attributes={Project_Department_budget, Project_Department_name, Project_Department_location}

# Project_Project class attributes and methods
Project_Project_name: Property = Property(name="name", type=StringType)
Project_Project_budget: Property = Property(name="budget", type=IntegerType)
Project_Project.attributes={Project_Project_name, Project_Project_budget}

# Relationships
WorksIn_Department0: BinaryAssociation = BinaryAssociation(
    name="WorksIn_Department0",
    ends={
        Property(name="1", type=Project_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=Project_Department, multiplicity=Multiplicity(1, 9999))
    }
)
WorksOn_Project2: BinaryAssociation = BinaryAssociation(
    name="WorksOn_Project2",
    ends={
        Property(name="4", type=Project_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="3", type=Project_Project, multiplicity=Multiplicity(0, 9999))
    }
)
WorksIn_Employee5: BinaryAssociation = BinaryAssociation(
    name="WorksIn_Employee5",
    ends={
        Property(name="7", type=Project_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="6", type=Project_Employee, multiplicity=Multiplicity(0, 9999))
    }
)
Controls_Project8: BinaryAssociation = BinaryAssociation(
    name="Controls_Project8",
    ends={
        Property(name="10", type=Project_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="9", type=Project_Project, multiplicity=Multiplicity(0, 9999))
    }
)
WorksOn_Employee11: BinaryAssociation = BinaryAssociation(
    name="WorksOn_Employee11",
    ends={
        Property(name="13", type=Project_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="12", type=Project_Employee, multiplicity=Multiplicity(0, 9999))
    }
)
Controls_Department14: BinaryAssociation = BinaryAssociation(
    name="Controls_Department14",
    ends={
        Property(name="16", type=Project_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="15", type=Project_Department, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="Project",
    types={Project_Employee, Project_Department, Project_Project},
    associations={WorksIn_Department0, WorksOn_Project2, WorksIn_Employee5, Controls_Project8, WorksOn_Employee11, Controls_Department14},
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