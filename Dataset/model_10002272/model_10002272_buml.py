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
Department = Class(name="Department")
Person = Class(name="Person")
Patient = Class(name="Patient")
inPatient = Class(name="inPatient")
outPatient = Class(name="outPatient")
Employee = Class(name="Employee")
Manager = Class(name="Manager")
Doctor = Class(name="Doctor")
Nurse = Class(name="Nurse")
Hospital = Class(name="Hospital")

# Department class attributes and methods
Department_departmentID: Property = Property(name="departmentID", type=StringType)
Department_departmentName: Property = Property(name="departmentName", type=StringType)
Department_doctorList: Property = Property(name="doctorList", type=StringType)
Department_nurseList: Property = Property(name="nurseList", type=StringType)
Department.attributes={Department_departmentID, Department_departmentName, Department_doctorList, Department_nurseList}

# Person class attributes and methods
Person_title: Property = Property(name="title", type=StringType)
Person_name: Property = Property(name="name", type=StringType)
Person_address: Property = Property(name="address", type=StringType)
Person_phoneNumber: Property = Property(name="phoneNumber", type=StringType)
Person_gender: Property = Property(name="gender", type=StringType)
Person.attributes={Person_phoneNumber, Person_gender, Person_name, Person_address, Person_title}

# Patient class attributes and methods
Patient_patientID: Property = Property(name="patientID", type=StringType)
Patient_treatment: Property = Property(name="treatment", type=StringType)
Patient.attributes={Patient_patientID, Patient_treatment}

# inPatient class attributes and methods
inPatient_inDate: Property = Property(name="inDate", type=StringType)
inPatient_outDate: Property = Property(name="outDate", type=StringType)
inPatient_rooomNumber: Property = Property(name="rooomNumber", type=StringType)
inPatient.attributes={inPatient_rooomNumber, inPatient_outDate, inPatient_inDate}

# outPatient class attributes and methods
outPatient_inDate: Property = Property(name="inDate", type=StringType)
outPatient_outDate: Property = Property(name="outDate", type=StringType)
outPatient_roomNumber: Property = Property(name="roomNumber", type=StringType)
outPatient.attributes={outPatient_outDate, outPatient_inDate, outPatient_roomNumber}

# Employee class attributes and methods
Employee_employeeID: Property = Property(name="employeeID", type=StringType)
Employee_salary: Property = Property(name="salary", type=StringType)
Employee.attributes={Employee_salary, Employee_employeeID}

# Manager class attributes and methods
Manager_employeeList: Property = Property(name="employeeList", type=StringType)
Manager_allowance: Property = Property(name="allowance", type=StringType)
Manager.attributes={Manager_allowance, Manager_employeeList}

# Doctor class attributes and methods
Doctor_department: Property = Property(name="department", type=Department)
Doctor.attributes={Doctor_department}

# Nurse class attributes and methods
Nurse_department: Property = Property(name="department", type=Department)
Nurse.attributes={Nurse_department}

# Hospital class attributes and methods
Hospital_name: Property = Property(name="name", type=StringType)
Hospital_address: Property = Property(name="address", type=StringType)
Hospital.attributes={Hospital_address, Hospital_name}

# Relationships
Hospital_Department: BinaryAssociation = BinaryAssociation(
    name="Hospital_Department",
    ends={
        Property(name="department0", type=Department, multiplicity=Multiplicity(0, 1)),
        Property(name="hospital1", type=Hospital, multiplicity=Multiplicity(0, 1))
    }
)
Hospital_Person: BinaryAssociation = BinaryAssociation(
    name="Hospital_Person",
    ends={
        Property(name="person2", type=Person, multiplicity=Multiplicity(0, 1)),
        Property(name="hospital3", type=Hospital, multiplicity=Multiplicity(0, 1))
    }
)
Manager_Doctor: BinaryAssociation = BinaryAssociation(
    name="Manager_Doctor",
    ends={
        Property(name="doctor4", type=Doctor, multiplicity=Multiplicity(0, 1)),
        Property(name="manager5", type=Manager, multiplicity=Multiplicity(0, 1))
    }
)
Manager_Nurse: BinaryAssociation = BinaryAssociation(
    name="Manager_Nurse",
    ends={
        Property(name="nurse6", type=Nurse, multiplicity=Multiplicity(0, 1)),
        Property(name="manager7", type=Manager, multiplicity=Multiplicity(0, 1))
    }
)
Department__Doctor: BinaryAssociation = BinaryAssociation(
    name="Department__Doctor",
    ends={
        Property(name="doctor8", type=Doctor, multiplicity=Multiplicity(0, 1)),
        Property(name="department_29", type=Department, multiplicity=Multiplicity(0, 1))
    }
)
Department__Nurse: BinaryAssociation = BinaryAssociation(
    name="Department__Nurse",
    ends={
        Property(name="nurse10", type=Nurse, multiplicity=Multiplicity(0, 1)),
        Property(name="department_211", type=Department, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="a2a0ae62_f6de_46c0_bf19_26bc78ebe7ab",
    types={Department, Person, Patient, inPatient, outPatient, Employee, Manager, Doctor, Nurse, Hospital},
    associations={Hospital_Department, Hospital_Person, Manager_Doctor, Manager_Nurse, Department__Doctor, Department__Nurse},
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