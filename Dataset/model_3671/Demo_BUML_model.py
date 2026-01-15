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
Demo_Employee = Class(name="Demo::Employee")
Demo_Department = Class(name="Demo::Department")
Demo_Project = Class(name="Demo::Project")

# Demo_Employee class attributes and methods
Demo_Employee_name: Property = Property(name="name", type=BooleanType)
Demo_Employee_salary: Property = Property(name="salary", type=IntegerType)
Demo_Employee.attributes={Demo_Employee_salary, Demo_Employee_name}

# Demo_Department class attributes and methods
Demo_Department_name: Property = Property(name="name", type=BooleanType)
Demo_Department_location: Property = Property(name="location", type=BooleanType)
Demo_Department_budget: Property = Property(name="budget", type=IntegerType)
Demo_Department.attributes={Demo_Department_budget, Demo_Department_name, Demo_Department_location}

# Demo_Project class attributes and methods
Demo_Project_budget: Property = Property(name="budget", type=IntegerType)
Demo_Project_name: Property = Property(name="name", type=BooleanType)
Demo_Project.attributes={Demo_Project_budget, Demo_Project_name}

# Relationships
WorksIn_department0: BinaryAssociation = BinaryAssociation(
    name="WorksIn_department0",
    ends={
        Property(name="Department", type=Demo_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="WorksIn_employee", type=Demo_Department, multiplicity=Multiplicity(1, 9999))
    }
)
WorksOn_employee5: BinaryAssociation = BinaryAssociation(
    name="WorksOn_employee5",
    ends={
        Property(name="Employee6", type=Demo_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="WorksOn_project", type=Demo_Employee, multiplicity=Multiplicity(0, 9999))
    }
)
Controls_department7: BinaryAssociation = BinaryAssociation(
    name="Controls_department7",
    ends={
        Property(name="Department8", type=Demo_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="Controls_project", type=Demo_Department, multiplicity=Multiplicity(1, 1))
    }
)
WorksOn_project1: BinaryAssociation = BinaryAssociation(
    name="WorksOn_project1",
    ends={
        Property(name="Project", type=Demo_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="WorksOn_employee", type=Demo_Project, multiplicity=Multiplicity(0, 9999))
    }
)
WorksIn_employee2: BinaryAssociation = BinaryAssociation(
    name="WorksIn_employee2",
    ends={
        Property(name="Employee", type=Demo_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="WorksIn_department", type=Demo_Employee, multiplicity=Multiplicity(0, 9999))
    }
)
Controls_project3: BinaryAssociation = BinaryAssociation(
    name="Controls_project3",
    ends={
        Property(name="Project4", type=Demo_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="Controls_department", type=Demo_Project, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="Demo",
    types={Demo_Employee, Demo_Department, Demo_Project},
    associations={WorksIn_department0, WorksOn_employee5, Controls_department7, WorksOn_project1, WorksIn_employee2, Controls_project3},
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