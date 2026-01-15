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
Company_Employee.attributes={Company_Employee_salary, Company_Employee_name}

# Company_Department class attributes and methods
Company_Department_name: Property = Property(name="name", type=StringType)
Company_Department_location: Property = Property(name="location", type=StringType)
Company_Department_budget: Property = Property(name="budget", type=IntegerType)
Company_Department.attributes={Company_Department_name, Company_Department_budget, Company_Department_location}

# Company_Project class attributes and methods
Company_Project_name: Property = Property(name="name", type=StringType)
Company_Project_budget: Property = Property(name="budget", type=IntegerType)
Company_Project.attributes={Company_Project_budget, Company_Project_name}

# Relationships
WorksIn_Department0: BinaryAssociation = BinaryAssociation(
    name="WorksIn_Department0",
    ends={
        Property(name="1", type=Company_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=Company_Department, multiplicity=Multiplicity(1, 9999))
    }
)
WorksOn_Project2: BinaryAssociation = BinaryAssociation(
    name="WorksOn_Project2",
    ends={
        Property(name="4", type=Company_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="3", type=Company_Project, multiplicity=Multiplicity(0, 9999))
    }
)
WorksIn_Employee5: BinaryAssociation = BinaryAssociation(
    name="WorksIn_Employee5",
    ends={
        Property(name="7", type=Company_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="6", type=Company_Employee, multiplicity=Multiplicity(0, 9999))
    }
)
Controls_Project8: BinaryAssociation = BinaryAssociation(
    name="Controls_Project8",
    ends={
        Property(name="10", type=Company_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="9", type=Company_Project, multiplicity=Multiplicity(0, 9999))
    }
)
WorksOn_Employee11: BinaryAssociation = BinaryAssociation(
    name="WorksOn_Employee11",
    ends={
        Property(name="13", type=Company_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="12", type=Company_Employee, multiplicity=Multiplicity(0, 9999))
    }
)
Controls_Department14: BinaryAssociation = BinaryAssociation(
    name="Controls_Department14",
    ends={
        Property(name="16", type=Company_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="15", type=Company_Department, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="Company",
    types={Company_Employee, Company_Department, Company_Project},
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