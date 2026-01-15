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
exo1_Departement = Class(name="exo1::Departement")
exo1_Project = Class(name="exo1::Project")
exo1_Company = Class(name="exo1::Company")
exo1_Employee = Class(name="exo1::Employee")

# exo1_Departement class attributes and methods
exo1_Departement_name: Property = Property(name="name", type=StringType)
exo1_Departement_location: Property = Property(name="location", type=StringType)
exo1_Departement_budget: Property = Property(name="budget", type=IntegerType)
exo1_Departement.attributes={exo1_Departement_budget, exo1_Departement_location, exo1_Departement_name}

# exo1_Project class attributes and methods
exo1_Project_name: Property = Property(name="name", type=StringType)
exo1_Project_budget: Property = Property(name="budget", type=IntegerType)
exo1_Project.attributes={exo1_Project_name, exo1_Project_budget}

# exo1_Company class attributes and methods

# exo1_Employee class attributes and methods
exo1_Employee_salary: Property = Property(name="salary", type=StringType)
exo1_Employee_name: Property = Property(name="name", type=StringType)
exo1_Employee.attributes={exo1_Employee_salary, exo1_Employee_name}

# Relationships
projects0: BinaryAssociation = BinaryAssociation(
    name="projects0",
    ends={
        Property(name="Project", type=exo1_Departement, multiplicity=Multiplicity(1, 1)),
        Property(name="departement", type=exo1_Project, multiplicity=Multiplicity(0, 9999))
    }
)
employees3: BinaryAssociation = BinaryAssociation(
    name="employees3",
    ends={
        Property(name="Employee5", type=exo1_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="projects4", type=exo1_Employee, multiplicity=Multiplicity(0, 9999))
    }
)
projects6: BinaryAssociation = BinaryAssociation(
    name="projects6",
    ends={
        Property(name="Project7", type=exo1_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="employees", type=exo1_Project, multiplicity=Multiplicity(0, 9999))
    }
)
departements8: BinaryAssociation = BinaryAssociation(
    name="departements8",
    ends={
        Property(name="Departement10", type=exo1_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="employees9", type=exo1_Departement, multiplicity=Multiplicity(1, 9999))
    }
)
employees1: BinaryAssociation = BinaryAssociation(
    name="employees1",
    ends={
        Property(name="Employee", type=exo1_Departement, multiplicity=Multiplicity(1, 1)),
        Property(name="departements", type=exo1_Employee, multiplicity=Multiplicity(0, 9999))
    }
)
departement2: BinaryAssociation = BinaryAssociation(
    name="departement2",
    ends={
        Property(name="Departement", type=exo1_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="projects", type=exo1_Departement, multiplicity=Multiplicity(1, 1))
    }
)
employees11: BinaryAssociation = BinaryAssociation(
    name="employees11",
    ends={
        Property(name="exo1_Employee", type=exo1_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="exo1_Company", type=exo1_Employee, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
projets12: BinaryAssociation = BinaryAssociation(
    name="projets12",
    ends={
        Property(name="exo1_Project", type=exo1_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="exo1_Company13", type=exo1_Project, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
departements14: BinaryAssociation = BinaryAssociation(
    name="departements14",
    ends={
        Property(name="exo1_Departement", type=exo1_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="exo1_Company15", type=exo1_Departement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="exo1",
    types={exo1_Departement, exo1_Project, exo1_Company, exo1_Employee},
    associations={projects0, employees3, projects6, departements8, employees1, departement2, employees11, projets12, departements14},
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