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
employee_Directory = Class(name="employee_Directory")
employee_Project = Class(name="employee_Project", is_abstract=True)
employee_Employee = Class(name="employee_Employee")
employee_JobTitle = Class(name="employee_JobTitle")
employee_Degree = Class(name="employee_Degree")
employee_SmallProject = Class(name="employee_SmallProject")
Project = Class(name="Project")
employee_LargeProject = Class(name="employee_LargeProject")
employee_PhoneNumber = Class(name="employee_PhoneNumber")
employee_EmploymentPeriod = Class(name="employee_EmploymentPeriod")
employee_Address = Class(name="employee_Address")
employee_EmailAddress = Class(name="employee_EmailAddress")

# employee_Directory class attributes and methods
employee_Directory_name: Property = Property(name="name", type=StringType)
employee_Directory.attributes={employee_Directory_name}

# employee_Project class attributes and methods
employee_Project_name: Property = Property(name="name", type=StringType)
employee_Project_description: Property = Property(name="description", type=StringType)
employee_Project.attributes={employee_Project_description, employee_Project_name}

# employee_Employee class attributes and methods
employee_Employee_firstName: Property = Property(name="firstName", type=StringType)
employee_Employee_lastName: Property = Property(name="lastName", type=StringType)
employee_Employee_gender: Property = Property(name="gender", type=StringType)
employee_Employee_salary: Property = Property(name="salary", type=FloatType)
employee_Employee_responsibilities: Property = Property(name="responsibilities", type=StringType)
employee_Employee.attributes={employee_Employee_responsibilities, employee_Employee_gender, employee_Employee_lastName, employee_Employee_firstName, employee_Employee_salary}

# employee_JobTitle class attributes and methods
employee_JobTitle_title: Property = Property(name="title", type=StringType)
employee_JobTitle.attributes={employee_JobTitle_title}

# employee_Degree class attributes and methods
employee_Degree_name: Property = Property(name="name", type=StringType)
employee_Degree.attributes={employee_Degree_name}

# employee_SmallProject class attributes and methods

# Project class attributes and methods

# employee_LargeProject class attributes and methods
employee_LargeProject_budget: Property = Property(name="budget", type=FloatType)
employee_LargeProject_milestone: Property = Property(name="milestone", type=DateType)
employee_LargeProject.attributes={employee_LargeProject_milestone, employee_LargeProject_budget}

# employee_PhoneNumber class attributes and methods
employee_PhoneNumber_areaCode: Property = Property(name="areaCode", type=StringType)
employee_PhoneNumber_number: Property = Property(name="number", type=StringType)
employee_PhoneNumber_type: Property = Property(name="type", type=StringType)
employee_PhoneNumber.attributes={employee_PhoneNumber_areaCode, employee_PhoneNumber_type, employee_PhoneNumber_number}

# employee_EmploymentPeriod class attributes and methods
employee_EmploymentPeriod_startDate: Property = Property(name="startDate", type=DateType)
employee_EmploymentPeriod_endDate: Property = Property(name="endDate", type=DateType)
employee_EmploymentPeriod.attributes={employee_EmploymentPeriod_startDate, employee_EmploymentPeriod_endDate}

# employee_Address class attributes and methods
employee_Address_city: Property = Property(name="city", type=StringType)
employee_Address_country: Property = Property(name="country", type=StringType)
employee_Address_province: Property = Property(name="province", type=StringType)
employee_Address_postalCode: Property = Property(name="postalCode", type=StringType)
employee_Address_street: Property = Property(name="street", type=StringType)
employee_Address.attributes={employee_Address_street, employee_Address_city, employee_Address_province, employee_Address_country, employee_Address_postalCode}

# employee_EmailAddress class attributes and methods
employee_EmailAddress_address: Property = Property(name="address", type=StringType)
employee_EmailAddress.attributes={employee_EmailAddress_address}

# Relationships
owner10: BinaryAssociation = BinaryAssociation(
    name="owner10",
    ends={
        Property(name="Employee", type=employee_PhoneNumber, multiplicity=Multiplicity(1, 1)),
        Property(name="phoneNumbers", type=employee_Employee, multiplicity=Multiplicity(1, 1))
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
period11: BinaryAssociation = BinaryAssociation(
    name="period11",
    ends={
        Property(name="employee_EmploymentPeriod", type=employee_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="employee_Employee12", type=employee_EmploymentPeriod, multiplicity=Multiplicity(0, 1), is_composite=True)
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

# Generalizations
gen_employee_SmallProject_Project = Generalization(general=Project, specific=employee_SmallProject)
gen_employee_LargeProject_Project = Generalization(general=Project, specific=employee_LargeProject)

# Domain Model
domain_model = DomainModel(
    name="employee",
    types={employee_Directory, employee_Project, employee_Employee, employee_JobTitle, employee_Degree, employee_SmallProject, Project, employee_LargeProject, employee_PhoneNumber, employee_EmploymentPeriod, employee_Address, employee_EmailAddress, Gender},
    associations={owner10, projects0, employees1, jobs3, degrees5, teamLeader7, period11, address13, jobTitle15, manager19, managedEmployees22, phoneNumbers24, degrees25, projects28, emailAddresses31},
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