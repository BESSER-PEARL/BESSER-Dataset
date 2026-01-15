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

# Enumerations
Gender: Enumeration = Enumeration(
    name="Gender",
    literals={
            EnumerationLiteral(name="Male"),
			EnumerationLiteral(name="Female")
    }
)

# Classes
employee_Project = Class(name="employee::Project", is_abstract=True)
employee_PhoneNumber = Class(name="employee::PhoneNumber")
employee_Employee = Class(name="employee::Employee")
employee_SmallProject = Class(name="employee::SmallProject")
Project = Class(name="Project")
employee_LargeProject = Class(name="employee::LargeProject")
employee_JobTitle = Class(name="employee::JobTitle")
employee_EmploymentPeriod = Class(name="employee::EmploymentPeriod")
employee_Address = Class(name="employee::Address")
employee_Degree = Class(name="employee::Degree")
employee_EmailAddress = Class(name="employee::EmailAddress")

# employee_Project class attributes and methods
employee_Project_name: Property = Property(name="name", type=StringType)
employee_Project_description: Property = Property(name="description", type=StringType)
employee_Project.attributes={employee_Project_name, employee_Project_description}

# employee_PhoneNumber class attributes and methods
employee_PhoneNumber_number: Property = Property(name="number", type=StringType)
employee_PhoneNumber_type: Property = Property(name="type", type=StringType)
employee_PhoneNumber_areaCode: Property = Property(name="areaCode", type=StringType)
employee_PhoneNumber.attributes={employee_PhoneNumber_type, employee_PhoneNumber_areaCode, employee_PhoneNumber_number}

# employee_Employee class attributes and methods
employee_Employee_gender: Property = Property(name="gender", type=StringType)
employee_Employee_firstName: Property = Property(name="firstName", type=StringType)
employee_Employee_lastName: Property = Property(name="lastName", type=StringType)
employee_Employee_salary: Property = Property(name="salary", type=FloatType)
employee_Employee_version: Property = Property(name="version", type=StringType)
employee_Employee_responsibilities: Property = Property(name="responsibilities", type=StringType)
employee_Employee.attributes={employee_Employee_salary, employee_Employee_gender, employee_Employee_lastName, employee_Employee_version, employee_Employee_firstName, employee_Employee_responsibilities}

# employee_SmallProject class attributes and methods

# Project class attributes and methods

# employee_LargeProject class attributes and methods
employee_LargeProject_budget: Property = Property(name="budget", type=FloatType)
employee_LargeProject_milestone: Property = Property(name="milestone", type=DateType)
employee_LargeProject.attributes={employee_LargeProject_budget, employee_LargeProject_milestone}

# employee_JobTitle class attributes and methods
employee_JobTitle_title: Property = Property(name="title", type=StringType)
employee_JobTitle.attributes={employee_JobTitle_title}

# employee_EmploymentPeriod class attributes and methods
employee_EmploymentPeriod_id: Property = Property(name="id", type=IntegerType)
employee_EmploymentPeriod_startDate: Property = Property(name="startDate", type=DateType)
employee_EmploymentPeriod_endDate: Property = Property(name="endDate", type=DateType)
employee_EmploymentPeriod.attributes={employee_EmploymentPeriod_startDate, employee_EmploymentPeriod_endDate, employee_EmploymentPeriod_id}

# employee_Address class attributes and methods
employee_Address_id: Property = Property(name="id", type=IntegerType)
employee_Address_city: Property = Property(name="city", type=StringType)
employee_Address_country: Property = Property(name="country", type=StringType)
employee_Address_province: Property = Property(name="province", type=StringType)
employee_Address_postalCode: Property = Property(name="postalCode", type=StringType)
employee_Address_street: Property = Property(name="street", type=StringType)
employee_Address.attributes={employee_Address_country, employee_Address_id, employee_Address_postalCode, employee_Address_street, employee_Address_province, employee_Address_city}

# employee_Degree class attributes and methods
employee_Degree_name: Property = Property(name="name", type=StringType)
employee_Degree.attributes={employee_Degree_name}

# employee_EmailAddress class attributes and methods
employee_EmailAddress_id: Property = Property(name="id", type=IntegerType)
employee_EmailAddress_name: Property = Property(name="name", type=StringType)
employee_EmailAddress_address: Property = Property(name="address", type=StringType)
employee_EmailAddress.attributes={employee_EmailAddress_name, employee_EmailAddress_address, employee_EmailAddress_id}

# Relationships
teamLeader0: BinaryAssociation = BinaryAssociation(
    name="teamLeader0",
    ends={
        Property(name="employee_Employee", type=employee_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="employee_Project", type=employee_Employee, multiplicity=Multiplicity(0, 1))
    }
)
owner1: BinaryAssociation = BinaryAssociation(
    name="owner1",
    ends={
        Property(name="Employee", type=employee_PhoneNumber, multiplicity=Multiplicity(1, 1)),
        Property(name="phoneNumbers", type=employee_Employee, multiplicity=Multiplicity(1, 1))
    }
)
manager9: BinaryAssociation = BinaryAssociation(
    name="manager9",
    ends={
        Property(name="Employee10", type=employee_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="managedEmployees", type=employee_Employee, multiplicity=Multiplicity(0, 1))
    }
)
managedEmployees12: BinaryAssociation = BinaryAssociation(
    name="managedEmployees12",
    ends={
        Property(name="Employee13", type=employee_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="manager", type=employee_Employee, multiplicity=Multiplicity(0, 9999))
    }
)
period2: BinaryAssociation = BinaryAssociation(
    name="period2",
    ends={
        Property(name="employee_EmploymentPeriod", type=employee_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="employee_Employee3", type=employee_EmploymentPeriod, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
phoneNumbers14: BinaryAssociation = BinaryAssociation(
    name="phoneNumbers14",
    ends={
        Property(name="PhoneNumber", type=employee_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=employee_PhoneNumber, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
address4: BinaryAssociation = BinaryAssociation(
    name="address4",
    ends={
        Property(name="employee_Address", type=employee_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="employee_Employee5", type=employee_Address, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
jobTitle6: BinaryAssociation = BinaryAssociation(
    name="jobTitle6",
    ends={
        Property(name="employee_JobTitle", type=employee_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="employee_Employee7", type=employee_JobTitle, multiplicity=Multiplicity(0, 1))
    }
)
emailAddresses20: BinaryAssociation = BinaryAssociation(
    name="emailAddresses20",
    ends={
        Property(name="employee_EmailAddress", type=employee_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="employee_Employee21", type=employee_EmailAddress, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
degrees15: BinaryAssociation = BinaryAssociation(
    name="degrees15",
    ends={
        Property(name="employee_Degree", type=employee_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="employee_Employee16", type=employee_Degree, multiplicity=Multiplicity(0, 9999))
    }
)
projects17: BinaryAssociation = BinaryAssociation(
    name="projects17",
    ends={
        Property(name="employee_Project19", type=employee_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="employee_Employee18", type=employee_Project, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_employee_SmallProject_Project = Generalization(general=Project, specific=employee_SmallProject)
gen_employee_LargeProject_Project = Generalization(general=Project, specific=employee_LargeProject)

# Domain Model
domain_model = DomainModel(
    name="employee",
    types={employee_Project, employee_PhoneNumber, employee_Employee, employee_SmallProject, Project, employee_LargeProject, employee_JobTitle, employee_EmploymentPeriod, employee_Address, employee_Degree, employee_EmailAddress, Gender},
    associations={teamLeader0, owner1, manager9, managedEmployees12, period2, phoneNumbers14, address4, jobTitle6, emailAddresses20, degrees15, projects17},
    generalizations={gen_employee_SmallProject_Project, gen_employee_LargeProject_Project},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)