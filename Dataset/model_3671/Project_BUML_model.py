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
Project_Employee = Class(name="Project_Employee")
Project_Department = Class(name="Project_Department")
Project_Project = Class(name="Project_Project")

# Project_Employee class attributes and methods
Project_Employee_name: Property = Property(name="name", type=StringType)
Project_Employee_salary: Property = Property(name="salary", type=IntegerType)
Project_Employee.attributes={Project_Employee_salary, Project_Employee_name}

# Project_Department class attributes and methods
Project_Department_name: Property = Property(name="name", type=StringType)
Project_Department_location: Property = Property(name="location", type=StringType)
Project_Department_budget: Property = Property(name="budget", type=IntegerType)
Project_Department.attributes={Project_Department_budget, Project_Department_name, Project_Department_location}

# Project_Project class attributes and methods
Project_Project_name: Property = Property(name="name", type=StringType)
Project_Project_budget: Property = Property(name="budget", type=IntegerType)
Project_Project.attributes={Project_Project_budget, Project_Project_name}

# Relationships
WorksIn_Department0: BinaryAssociation = BinaryAssociation(
    name="WorksIn_Department0",
    ends={
        Property(name="Department", type=Project_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="WorksIn_Employee", type=Project_Department, multiplicity=Multiplicity(1, 9999))
    }
)
WorksOn_Project1: BinaryAssociation = BinaryAssociation(
    name="WorksOn_Project1",
    ends={
        Property(name="Project", type=Project_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="WorksOn_Employee", type=Project_Project, multiplicity=Multiplicity(0, 9999))
    }
)
WorksIn_Employee2: BinaryAssociation = BinaryAssociation(
    name="WorksIn_Employee2",
    ends={
        Property(name="Employee", type=Project_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="WorksIn_Department", type=Project_Employee, multiplicity=Multiplicity(0, 9999))
    }
)
Controls_Project3: BinaryAssociation = BinaryAssociation(
    name="Controls_Project3",
    ends={
        Property(name="Project4", type=Project_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="Controls_Department", type=Project_Project, multiplicity=Multiplicity(0, 9999))
    }
)
WorksOn_Employee5: BinaryAssociation = BinaryAssociation(
    name="WorksOn_Employee5",
    ends={
        Property(name="Employee6", type=Project_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="WorksOn_Project", type=Project_Employee, multiplicity=Multiplicity(0, 9999))
    }
)
Controls_Department7: BinaryAssociation = BinaryAssociation(
    name="Controls_Department7",
    ends={
        Property(name="Department8", type=Project_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="Controls_Project", type=Project_Department, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="Project",
    types={Project_Employee, Project_Department, Project_Project},
    associations={WorksIn_Department0, WorksOn_Project1, WorksIn_Employee2, Controls_Project3, WorksOn_Employee5, Controls_Department7},
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