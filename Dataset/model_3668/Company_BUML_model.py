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
Company_Employee = Class(name="Company::Employee")
Company_Department = Class(name="Company::Department")
Company_Project = Class(name="Company::Project")

# Company_Employee class attributes and methods
Company_Employee_name: Property = Property(name="name", type=StringType)
Company_Employee_salary: Property = Property(name="salary", type=IntegerType)
Company_Employee.attributes={Company_Employee_name, Company_Employee_salary}

# Company_Department class attributes and methods
Company_Department_name: Property = Property(name="name", type=StringType)
Company_Department_location: Property = Property(name="location", type=StringType)
Company_Department_budget: Property = Property(name="budget", type=IntegerType)
Company_Department.attributes={Company_Department_budget, Company_Department_name, Company_Department_location}

# Company_Project class attributes and methods
Company_Project_name: Property = Property(name="name", type=StringType)
Company_Project_budget: Property = Property(name="budget", type=IntegerType)
Company_Project.attributes={Company_Project_name, Company_Project_budget}

# Relationships
Controls_Project3: BinaryAssociation = BinaryAssociation(
    name="Controls_Project3",
    ends={
        Property(name="Project4", type=Company_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="Controls_Department", type=Company_Project, multiplicity=Multiplicity(0, 9999))
    }
)
WorksIn_Department0: BinaryAssociation = BinaryAssociation(
    name="WorksIn_Department0",
    ends={
        Property(name="Department", type=Company_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="WorksIn_Employee", type=Company_Department, multiplicity=Multiplicity(1, 9999))
    }
)
WorksOn_Project1: BinaryAssociation = BinaryAssociation(
    name="WorksOn_Project1",
    ends={
        Property(name="Project", type=Company_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="WorksOn_Employee", type=Company_Project, multiplicity=Multiplicity(0, 9999))
    }
)
WorksIn_Employee2: BinaryAssociation = BinaryAssociation(
    name="WorksIn_Employee2",
    ends={
        Property(name="Employee", type=Company_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="WorksIn_Department", type=Company_Employee, multiplicity=Multiplicity(0, 9999))
    }
)
WorksOn_Employee5: BinaryAssociation = BinaryAssociation(
    name="WorksOn_Employee5",
    ends={
        Property(name="Employee6", type=Company_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="WorksOn_Project", type=Company_Employee, multiplicity=Multiplicity(0, 9999))
    }
)
Controls_Department7: BinaryAssociation = BinaryAssociation(
    name="Controls_Department7",
    ends={
        Property(name="Department8", type=Company_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="Controls_Project", type=Company_Department, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="Company",
    types={Company_Employee, Company_Department, Company_Project},
    associations={Controls_Project3, WorksIn_Department0, WorksOn_Project1, WorksIn_Employee2, WorksOn_Employee5, Controls_Department7},
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