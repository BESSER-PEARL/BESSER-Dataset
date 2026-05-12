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
Employee_Management_System_Component = Class(name="Employee_Management_System_Component")
Authentication_UseCase = Class(name="Authentication_UseCase")
Salary_Management_UseCase = Class(name="Salary_Management_UseCase")
Administrator_Actor = Class(name="Administrator_Actor")
Employee_Actor = Class(name="Employee_Actor")
Person = Class(name="Person")
account = Class(name="account")
employee = Class(name="employee")
Patient = Class(name="Patient")
Physician = Class(name="Physician")
Coordinator = Class(name="Coordinator")
role = Class(name="role")
Role = Class(name="Role")
Department = Class(name="Department")
hourlyPay = Class(name="hourlyPay")
office = Class(name="office")
Login_external = Class(name="Login_external")
Logout_external = Class(name="Logout_external")

# Employee_Management_System_Component class attributes and methods

# Authentication_UseCase class attributes and methods

# Salary_Management_UseCase class attributes and methods

# Administrator_Actor class attributes and methods

# Employee_Actor class attributes and methods

# Person class attributes and methods
Person_firstName: Property = Property(name="firstName", type=StringType)
Person_lastName: Property = Property(name="lastName", type=StringType)
Person_middleName: Property = Property(name="middleName", type=StringType)
Person_homePhone: Property = Property(name="homePhone", type=StringType)
Person_cellPhone: Property = Property(name="cellPhone", type=StringType)
Person_email: Property = Property(name="email", type=StringType)
Person_address: Property = Property(name="address", type=StringType)
Person_city: Property = Property(name="city", type=StringType)
Person_State: Property = Property(name="State", type=StringType)
Person_DoB: Property = Property(name="DoB", type=DateType)
Person_note: Property = Property(name="note", type=StringType)
Person.attributes={Person_State, Person_middleName, Person_city, Person_firstName, Person_lastName, Person_DoB, Person_cellPhone, Person_address, Person_note, Person_homePhone, Person_email}

# account class attributes and methods
account_username: Property = Property(name="username", type=StringType)
account_password: Property = Property(name="password", type=StringType)
account_office: Property = Property(name="office", type=StringType)
account_id: Property = Property(name="id", type=IntegerType)
account.attributes={account_username, account_office, account_password, account_id}

# employee class attributes and methods
employee_empid: Property = Property(name="empid", type=StringType)
employee_ssn: Property = Property(name="ssn", type=StringType)
employee_Date_Hired: Property = Property(name="Date_Hired", type=DateType)
employee_Date_Started: Property = Property(name="Date_Started", type=DateType)
employee_Date_Ended: Property = Property(name="Date_Ended", type=DateType)
employee_workingHours: Property = Property(name="workingHours", type=FloatType)
employee_Role: Property = Property(name="Role", type=role)
employee_Department: Property = Property(name="Department", type=Department)
employee.attributes={employee_Date_Ended, employee_workingHours, employee_Date_Hired, employee_Date_Started, employee_ssn, employee_Role, employee_empid, employee_Department}

# Patient class attributes and methods
Patient_patientid: Property = Property(name="patientid", type=StringType)
Patient_ICD: Property = Property(name="ICD", type=StringType)
Patient_approvedHours: Property = Property(name="approvedHours", type=FloatType)
Patient_employee: Property = Property(name="employee", type=Employee_Actor)
Patient.attributes={Patient_patientid, Patient_approvedHours, Patient_ICD, Patient_employee}

# Physician class attributes and methods
Physician_office: Property = Property(name="office", type=office)
Physician.attributes={Physician_office}

# Coordinator class attributes and methods
Coordinator_office: Property = Property(name="office", type=office)
Coordinator.attributes={Coordinator_office}

# role class attributes and methods

# Role class attributes and methods
Role_name: Property = Property(name="name", type=StringType)
Role_description: Property = Property(name="description", type=StringType)
Role.attributes={Role_description, Role_name}

# Department class attributes and methods
Department_name: Property = Property(name="name", type=StringType)
Department_description: Property = Property(name="description", type=StringType)
Department.attributes={Department_description, Department_name}

# hourlyPay class attributes and methods
hourlyPay_employee: Property = Property(name="employee", type=employee)
hourlyPay.attributes={hourlyPay_employee}

# office class attributes and methods

# Login_external class attributes and methods

# Logout_external class attributes and methods

# Relationships
Employee_Login: BinaryAssociation = BinaryAssociation(
    name="Employee_Login",
    ends={
        Property(name="login0", type=Login_external, multiplicity=Multiplicity(0, 1)),
        Property(name="employee1", type=Employee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Employee_Logout: BinaryAssociation = BinaryAssociation(
    name="Employee_Logout",
    ends={
        Property(name="logout2", type=Logout_external, multiplicity=Multiplicity(0, 1)),
        Property(name="employee3", type=Employee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Person_account: BinaryAssociation = BinaryAssociation(
    name="Person_account",
    ends={
        Property(name="account4", type=account, multiplicity=Multiplicity(0, 1)),
        Property(name="person5", type=Person, multiplicity=Multiplicity(0, 1))
    }
)
employee_account: BinaryAssociation = BinaryAssociation(
    name="employee_account",
    ends={
        Property(name="account6", type=account, multiplicity=Multiplicity(0, 1)),
        Property(name="employee7", type=employee, multiplicity=Multiplicity(0, 1))
    }
)
account_Patient: BinaryAssociation = BinaryAssociation(
    name="account_Patient",
    ends={
        Property(name="patient8", type=Patient, multiplicity=Multiplicity(0, 1)),
        Property(name="account9", type=account, multiplicity=Multiplicity(0, 1))
    }
)
Person_Physician: BinaryAssociation = BinaryAssociation(
    name="Person_Physician",
    ends={
        Property(name="physician10", type=Physician, multiplicity=Multiplicity(0, 1)),
        Property(name="person11", type=Person, multiplicity=Multiplicity(0, 1))
    }
)
Person_Coordinator: BinaryAssociation = BinaryAssociation(
    name="Person_Coordinator",
    ends={
        Property(name="coordinator12", type=Coordinator, multiplicity=Multiplicity(0, 1)),
        Property(name="person13", type=Person, multiplicity=Multiplicity(0, 1))
    }
)
employee_Role: BinaryAssociation = BinaryAssociation(
    name="employee_Role",
    ends={
        Property(name="role14", type=Role, multiplicity=Multiplicity(0, 1)),
        Property(name="employee15", type=employee, multiplicity=Multiplicity(0, 1))
    }
)
employee_Department: BinaryAssociation = BinaryAssociation(
    name="employee_Department",
    ends={
        Property(name="department16", type=Department, multiplicity=Multiplicity(0, 1)),
        Property(name="employee17", type=employee, multiplicity=Multiplicity(0, 1))
    }
)
hourlyPay_employee: BinaryAssociation = BinaryAssociation(
    name="hourlyPay_employee",
    ends={
        Property(name="employee18", type=employee, multiplicity=Multiplicity(0, 1)),
        Property(name="hourlyPay19", type=hourlyPay, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_89d0241f_0e9b_4c19_b728_afbd82bc71d6",
    types={Employee_Management_System_Component, Authentication_UseCase, Salary_Management_UseCase, Administrator_Actor, Employee_Actor, Person, account, employee, Patient, Physician, Coordinator, role, Role, Department, hourlyPay, office, Login_external, Logout_external},
    associations={Employee_Login, Employee_Logout, Person_account, employee_account, account_Patient, Person_Physician, Person_Coordinator, employee_Role, employee_Department, hourlyPay_employee},
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