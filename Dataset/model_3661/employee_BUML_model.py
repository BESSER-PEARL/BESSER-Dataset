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
employee_Organization = Class(name="employee::Organization")
employee_Employee = Class(name="employee::Employee")
employee_Project = Class(name="employee::Project", is_abstract=True)
employee_JobTitle = Class(name="employee::JobTitle")
employee_SmallProject = Class(name="employee::SmallProject")
Project = Class(name="Project")
employee_LargeProject = Class(name="employee::LargeProject")
employee_PhoneNumber = Class(name="employee::PhoneNumber")
employee_EmploymentPeriod = Class(name="employee::EmploymentPeriod")
employee_Address = Class(name="employee::Address")
employee_EmailAddress = Class(name="employee::EmailAddress")

# employee_Organization class attributes and methods
employee_Organization_name: Property = Property(name="name", type=StringType)
employee_Organization.attributes={employee_Organization_name}

# employee_Employee class attributes and methods
employee_Employee_id: Property = Property(name="id", type=StringType)
employee_Employee_firstName: Property = Property(name="firstName", type=StringType)
employee_Employee_lastName: Property = Property(name="lastName", type=StringType)
employee_Employee_gender: Property = Property(name="gender", type=StringType)
employee_Employee_salary: Property = Property(name="salary", type=FloatType)
employee_Employee_responsibilities: Property = Property(name="responsibilities", type=StringType)
employee_Employee.attributes={employee_Employee_responsibilities, employee_Employee_firstName, employee_Employee_id, employee_Employee_gender, employee_Employee_salary, employee_Employee_lastName}

# employee_Project class attributes and methods
employee_Project_description: Property = Property(name="description", type=StringType)
employee_Project_name: Property = Property(name="name", type=StringType)
employee_Project.attributes={employee_Project_name, employee_Project_description}

# employee_JobTitle class attributes and methods
employee_JobTitle_title: Property = Property(name="title", type=StringType)
employee_JobTitle.attributes={employee_JobTitle_title}

# employee_SmallProject class attributes and methods

# Project class attributes and methods

# employee_LargeProject class attributes and methods
employee_LargeProject_budget: Property = Property(name="budget", type=FloatType)
employee_LargeProject_milestone: Property = Property(name="milestone", type=DateType)
employee_LargeProject.attributes={employee_LargeProject_milestone, employee_LargeProject_budget}

# employee_PhoneNumber class attributes and methods
employee_PhoneNumber_number: Property = Property(name="number", type=StringType)
employee_PhoneNumber_areaCode: Property = Property(name="areaCode", type=StringType)
employee_PhoneNumber_type: Property = Property(name="type", type=StringType)
employee_PhoneNumber.attributes={employee_PhoneNumber_number, employee_PhoneNumber_type, employee_PhoneNumber_areaCode}

# employee_EmploymentPeriod class attributes and methods
employee_EmploymentPeriod_id: Property = Property(name="id", type=StringType)
employee_EmploymentPeriod_endDate: Property = Property(name="endDate", type=DateType)
employee_EmploymentPeriod_startDate: Property = Property(name="startDate", type=DateType)
employee_EmploymentPeriod.attributes={employee_EmploymentPeriod_id, employee_EmploymentPeriod_endDate, employee_EmploymentPeriod_startDate}

# employee_Address class attributes and methods
employee_Address_city: Property = Property(name="city", type=StringType)
employee_Address_country: Property = Property(name="country", type=StringType)
employee_Address_province: Property = Property(name="province", type=StringType)
employee_Address_id: Property = Property(name="id", type=StringType)
employee_Address_postalCode: Property = Property(name="postalCode", type=StringType)
employee_Address_street: Property = Property(name="street", type=StringType)
employee_Address.attributes={employee_Address_postalCode, employee_Address_street, employee_Address_province, employee_Address_city, employee_Address_id, employee_Address_country}

# employee_EmailAddress class attributes and methods
employee_EmailAddress_id: Property = Property(name="id", type=StringType)
employee_EmailAddress_name: Property = Property(name="name", type=StringType)
employee_EmailAddress_address: Property = Property(name="address", type=StringType)
employee_EmailAddress.attributes={employee_EmailAddress_name, employee_EmailAddress_address, employee_EmailAddress_id}

# Relationships
employees0: BinaryAssociation = BinaryAssociation(
    name="employees0",
    ends={
        Property(name="employee_Employee", type=employee_Organization, multiplicity=Multiplicity(1, 1)),
        Property(name="employee_Organization", type=employee_Employee, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
projects1: BinaryAssociation = BinaryAssociation(
    name="projects1",
    ends={
        Property(name="employee_Project", type=employee_Organization, multiplicity=Multiplicity(1, 1)),
        Property(name="employee_Organization2", type=employee_Project, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
jobs3: BinaryAssociation = BinaryAssociation(
    name="jobs3",
    ends={
        Property(name="employee_JobTitle", type=employee_Organization, multiplicity=Multiplicity(1, 1)),
        Property(name="employee_Organization4", type=employee_JobTitle, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
teamLeader5: BinaryAssociation = BinaryAssociation(
    name="teamLeader5",
    ends={
        Property(name="employee_Employee7", type=employee_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="employee_Project6", type=employee_Employee, multiplicity=Multiplicity(0, 1))
    }
)
owner8: BinaryAssociation = BinaryAssociation(
    name="owner8",
    ends={
        Property(name="employee_Employee9", type=employee_PhoneNumber, multiplicity=Multiplicity(1, 1)),
        Property(name="employee_PhoneNumber", type=employee_Employee, multiplicity=Multiplicity(1, 1))
    }
)
address12: BinaryAssociation = BinaryAssociation(
    name="address12",
    ends={
        Property(name="employee_Address", type=employee_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="employee_Employee13", type=employee_Address, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
jobTitle14: BinaryAssociation = BinaryAssociation(
    name="jobTitle14",
    ends={
        Property(name="employee_JobTitle16", type=employee_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="employee_Employee15", type=employee_JobTitle, multiplicity=Multiplicity(0, 1))
    }
)
manager18: BinaryAssociation = BinaryAssociation(
    name="manager18",
    ends={
        Property(name="employee_Employee19", type=employee_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="employee_Employee17", type=employee_Employee, multiplicity=Multiplicity(0, 1))
    }
)
managedEmployees21: BinaryAssociation = BinaryAssociation(
    name="managedEmployees21",
    ends={
        Property(name="employee_Employee22", type=employee_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="employee_Employee20", type=employee_Employee, multiplicity=Multiplicity(0, 9999))
    }
)
phoneNumbers23: BinaryAssociation = BinaryAssociation(
    name="phoneNumbers23",
    ends={
        Property(name="employee_PhoneNumber25", type=employee_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="employee_Employee24", type=employee_PhoneNumber, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
period10: BinaryAssociation = BinaryAssociation(
    name="period10",
    ends={
        Property(name="employee_EmploymentPeriod", type=employee_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="employee_Employee11", type=employee_EmploymentPeriod, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
projects26: BinaryAssociation = BinaryAssociation(
    name="projects26",
    ends={
        Property(name="employee_Project28", type=employee_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="employee_Employee27", type=employee_Project, multiplicity=Multiplicity(0, 9999))
    }
)
emailAddresses29: BinaryAssociation = BinaryAssociation(
    name="emailAddresses29",
    ends={
        Property(name="employee_EmailAddress", type=employee_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="employee_Employee30", type=employee_EmailAddress, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_employee_SmallProject_Project = Generalization(general=Project, specific=employee_SmallProject)
gen_employee_LargeProject_Project = Generalization(general=Project, specific=employee_LargeProject)

# Domain Model
domain_model = DomainModel(
    name="employee",
    types={employee_Organization, employee_Employee, employee_Project, employee_JobTitle, employee_SmallProject, Project, employee_LargeProject, employee_PhoneNumber, employee_EmploymentPeriod, employee_Address, employee_EmailAddress, Gender},
    associations={employees0, projects1, jobs3, teamLeader5, owner8, address12, jobTitle14, manager18, managedEmployees21, phoneNumbers23, period10, projects26, emailAddresses29},
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