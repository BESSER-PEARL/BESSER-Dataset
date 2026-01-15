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
employee_JobTitle = Class(name="employee::JobTitle")
employee_Degree = Class(name="employee::Degree")
employee_Directory = Class(name="employee::Directory")
employee_Project = Class(name="employee::Project", is_abstract=True)
employee_Employee = Class(name="employee::Employee")
employee_EmploymentPeriod = Class(name="employee::EmploymentPeriod")
employee_SmallProject = Class(name="employee::SmallProject")
Project = Class(name="Project")
employee_LargeProject = Class(name="employee::LargeProject")
employee_PhoneNumber = Class(name="employee::PhoneNumber")
employee_Address = Class(name="employee::Address")
employee_EmailAddress = Class(name="employee::EmailAddress")

# employee_JobTitle class attributes and methods
employee_JobTitle_title: Property = Property(name="title", type=StringType)
employee_JobTitle.attributes={employee_JobTitle_title}

# employee_Degree class attributes and methods
employee_Degree_name: Property = Property(name="name", type=StringType)
employee_Degree.attributes={employee_Degree_name}

# employee_Directory class attributes and methods
employee_Directory_name: Property = Property(name="name", type=StringType)
employee_Directory.attributes={employee_Directory_name}

# employee_Project class attributes and methods
employee_Project_name: Property = Property(name="name", type=StringType)
employee_Project_description: Property = Property(name="description", type=StringType)
employee_Project.attributes={employee_Project_name, employee_Project_description}

# employee_Employee class attributes and methods
employee_Employee_firstName: Property = Property(name="firstName", type=StringType)
employee_Employee_lastName: Property = Property(name="lastName", type=StringType)
employee_Employee_gender: Property = Property(name="gender", type=StringType)
employee_Employee_salary: Property = Property(name="salary", type=FloatType)
employee_Employee_responsibilities: Property = Property(name="responsibilities", type=StringType)
employee_Employee.attributes={employee_Employee_firstName, employee_Employee_gender, employee_Employee_salary, employee_Employee_lastName, employee_Employee_responsibilities}

# employee_EmploymentPeriod class attributes and methods
employee_EmploymentPeriod_startDate: Property = Property(name="startDate", type=DateType)
employee_EmploymentPeriod_endDate: Property = Property(name="endDate", type=DateType)
employee_EmploymentPeriod.attributes={employee_EmploymentPeriod_endDate, employee_EmploymentPeriod_startDate}

# employee_SmallProject class attributes and methods

# Project class attributes and methods

# employee_LargeProject class attributes and methods
employee_LargeProject_budget: Property = Property(name="budget", type=FloatType)
employee_LargeProject_milestone: Property = Property(name="milestone", type=DateType)
employee_LargeProject.attributes={employee_LargeProject_milestone, employee_LargeProject_budget}

# employee_PhoneNumber class attributes and methods
employee_PhoneNumber_type: Property = Property(name="type", type=StringType)
employee_PhoneNumber_areaCode: Property = Property(name="areaCode", type=StringType)
employee_PhoneNumber_number: Property = Property(name="number", type=StringType)
employee_PhoneNumber.attributes={employee_PhoneNumber_areaCode, employee_PhoneNumber_type, employee_PhoneNumber_number}

# employee_Address class attributes and methods
employee_Address_city: Property = Property(name="city", type=StringType)
employee_Address_country: Property = Property(name="country", type=StringType)
employee_Address_province: Property = Property(name="province", type=StringType)
employee_Address_postalCode: Property = Property(name="postalCode", type=StringType)
employee_Address_street: Property = Property(name="street", type=StringType)
employee_Address.attributes={employee_Address_country, employee_Address_postalCode, employee_Address_province, employee_Address_city, employee_Address_street}

# employee_EmailAddress class attributes and methods
employee_EmailAddress_address: Property = Property(name="address", type=StringType)
employee_EmailAddress.attributes={employee_EmailAddress_address}

# Relationships
jobs3: BinaryAssociation = BinaryAssociation(
    name="jobs3",
    ends={
        Property(name="employee_JobTitle", type=employee_Directory, multiplicity=Multiplicity(1, 1)),
        Property(name="employee_Directory4", type=employee_JobTitle, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
degrees5: BinaryAssociation = BinaryAssociation(
    name="degrees5",
    ends={
        Property(name="employee_Degree", type=employee_Directory, multiplicity=Multiplicity(1, 1)),
        Property(name="employee_Directory6", type=employee_Degree, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
teamLeader7: BinaryAssociation = BinaryAssociation(
    name="teamLeader7",
    ends={
        Property(name="employee_Employee9", type=employee_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="employee_Project8", type=employee_Employee, multiplicity=Multiplicity(0, 1))
    }
)
projects0: BinaryAssociation = BinaryAssociation(
    name="projects0",
    ends={
        Property(name="employee_Project", type=employee_Directory, multiplicity=Multiplicity(1, 1)),
        Property(name="employee_Directory", type=employee_Project, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
employees1: BinaryAssociation = BinaryAssociation(
    name="employees1",
    ends={
        Property(name="employee_Employee", type=employee_Directory, multiplicity=Multiplicity(1, 1)),
        Property(name="employee_Directory2", type=employee_Employee, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner10: BinaryAssociation = BinaryAssociation(
    name="owner10",
    ends={
        Property(name="Employee", type=employee_PhoneNumber, multiplicity=Multiplicity(1, 1)),
        Property(name="phoneNumbers", type=employee_Employee, multiplicity=Multiplicity(1, 1))
    }
)
address13: BinaryAssociation = BinaryAssociation(
    name="address13",
    ends={
        Property(name="employee_Address", type=employee_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="employee_Employee14", type=employee_Address, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
jobTitle15: BinaryAssociation = BinaryAssociation(
    name="jobTitle15",
    ends={
        Property(name="employee_JobTitle17", type=employee_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="employee_Employee16", type=employee_JobTitle, multiplicity=Multiplicity(0, 1))
    }
)
manager19: BinaryAssociation = BinaryAssociation(
    name="manager19",
    ends={
        Property(name="Employee20", type=employee_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="managedEmployees", type=employee_Employee, multiplicity=Multiplicity(0, 1))
    }
)
managedEmployees22: BinaryAssociation = BinaryAssociation(
    name="managedEmployees22",
    ends={
        Property(name="Employee23", type=employee_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="manager", type=employee_Employee, multiplicity=Multiplicity(0, 9999))
    }
)
phoneNumbers24: BinaryAssociation = BinaryAssociation(
    name="phoneNumbers24",
    ends={
        Property(name="PhoneNumber", type=employee_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=employee_PhoneNumber, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
degrees25: BinaryAssociation = BinaryAssociation(
    name="degrees25",
    ends={
        Property(name="employee_Degree27", type=employee_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="employee_Employee26", type=employee_Degree, multiplicity=Multiplicity(0, 9999))
    }
)
projects28: BinaryAssociation = BinaryAssociation(
    name="projects28",
    ends={
        Property(name="employee_Project30", type=employee_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="employee_Employee29", type=employee_Project, multiplicity=Multiplicity(0, 9999))
    }
)
emailAddresses31: BinaryAssociation = BinaryAssociation(
    name="emailAddresses31",
    ends={
        Property(name="employee_EmailAddress", type=employee_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="employee_Employee32", type=employee_EmailAddress, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
period11: BinaryAssociation = BinaryAssociation(
    name="period11",
    ends={
        Property(name="employee_EmploymentPeriod", type=employee_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="employee_Employee12", type=employee_EmploymentPeriod, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_employee_SmallProject_Project = Generalization(general=Project, specific=employee_SmallProject)
gen_employee_LargeProject_Project = Generalization(general=Project, specific=employee_LargeProject)

# Domain Model
domain_model = DomainModel(
    name="employee",
    types={employee_JobTitle, employee_Degree, employee_Directory, employee_Project, employee_Employee, employee_EmploymentPeriod, employee_SmallProject, Project, employee_LargeProject, employee_PhoneNumber, employee_Address, employee_EmailAddress, Gender},
    associations={jobs3, degrees5, teamLeader7, projects0, employees1, owner10, address13, jobTitle15, manager19, managedEmployees22, phoneNumbers24, degrees25, projects28, emailAddresses31, period11},
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