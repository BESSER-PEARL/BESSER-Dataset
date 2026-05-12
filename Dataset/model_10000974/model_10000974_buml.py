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
Patient = Class(name="Patient")
Appointment = Class(name="Appointment")
Doctor = Class(name="Doctor")
Bill = Class(name="Bill")
DoctorSchedule = Class(name="DoctorSchedule")
DoctorServices = Class(name="DoctorServices")
Receptionist = Class(name="Receptionist")
Users = Class(name="Users")
UserRoles = Class(name="UserRoles")
UserwithRole = Class(name="UserwithRole")

# Patient class attributes and methods
Patient_PatientId: Property = Property(name="PatientId", type=IntegerType)
Patient_PId: Property = Property(name="PId", type=StringType)
Patient_UserId: Property = Property(name="UserId", type=IntegerType)
Patient_FirstName: Property = Property(name="FirstName", type=StringType)
Patient_LastName: Property = Property(name="LastName", type=StringType)
Patient_DateOfBirth: Property = Property(name="DateOfBirth", type=StringType)
Patient_Email: Property = Property(name="Email", type=StringType)
Patient_IsEmailConfirmed: Property = Property(name="IsEmailConfirmed", type=StringType)
Patient_activationcode: Property = Property(name="activationcode", type=StringType)
Patient_PhoneNumber: Property = Property(name="PhoneNumber", type=StringType)
Patient_IsPhoneNumberConfirmed: Property = Property(name="IsPhoneNumberConfirmed", type=StringType)
Patient_StreetAddress: Property = Property(name="StreetAddress", type=StringType)
Patient_City: Property = Property(name="City", type=StringType)
Patient_State: Property = Property(name="State", type=StringType)
Patient_ZipCode: Property = Property(name="ZipCode", type=StringType)
Patient.attributes={Patient_IsPhoneNumberConfirmed, Patient_LastName, Patient_State, Patient_Email, Patient_PId, Patient_StreetAddress, Patient_FirstName, Patient_PatientId, Patient_IsEmailConfirmed, Patient_PhoneNumber, Patient_ZipCode, Patient_City, Patient_UserId, Patient_activationcode, Patient_DateOfBirth}

# Appointment class attributes and methods
Appointment_AppointmentId: Property = Property(name="AppointmentId", type=IntegerType)
Appointment_Aid: Property = Property(name="Aid", type=StringType)
Appointment_PatientId: Property = Property(name="PatientId", type=IntegerType)
Appointment_PatientName: Property = Property(name="PatientName", type=StringType)
Appointment_Did: Property = Property(name="Did", type=IntegerType)
Appointment_DoctorName: Property = Property(name="DoctorName", type=StringType)
Appointment_ServiceId: Property = Property(name="ServiceId", type=IntegerType)
Appointment_AppointmentDate: Property = Property(name="AppointmentDate", type=StringType)
Appointment_AppointmentTime: Property = Property(name="AppointmentTime", type=StringType)
Appointment_Reason: Property = Property(name="Reason", type=StringType)
Appointment_AppointmentStatus: Property = Property(name="AppointmentStatus", type=StringType)
Appointment.attributes={Appointment_PatientId, Appointment_Aid, Appointment_AppointmentId, Appointment_DoctorName, Appointment_ServiceId, Appointment_AppointmentTime, Appointment_Reason, Appointment_PatientName, Appointment_Did, Appointment_AppointmentStatus, Appointment_AppointmentDate}

# Doctor class attributes and methods
Doctor_DoctorId: Property = Property(name="DoctorId", type=IntegerType)
Doctor_DId: Property = Property(name="DId", type=StringType)
Doctor_UserId: Property = Property(name="UserId", type=IntegerType)
Doctor_DoctorName: Property = Property(name="DoctorName", type=StringType)
Doctor_DateOfBirth: Property = Property(name="DateOfBirth", type=StringType)
Doctor_Email: Property = Property(name="Email", type=StringType)
Doctor_PhoneNumber: Property = Property(name="PhoneNumber", type=StringType)
Doctor_Speciality: Property = Property(name="Speciality", type=StringType)
Doctor.attributes={Doctor_PhoneNumber, Doctor_Speciality, Doctor_DoctorId, Doctor_Email, Doctor_DateOfBirth, Doctor_DoctorName, Doctor_UserId, Doctor_DId}

# Bill class attributes and methods
Bill_BillId: Property = Property(name="BillId", type=IntegerType)
Bill_BId: Property = Property(name="BId", type=StringType)
Bill_Did: Property = Property(name="Did", type=IntegerType)
Bill_DoctorName: Property = Property(name="DoctorName", type=StringType)
Bill_BillDate: Property = Property(name="BillDate", type=StringType)
Bill_PId: Property = Property(name="PId", type=IntegerType)
Bill_PatientName: Property = Property(name="PatientName", type=StringType)
Bill_TotalAmount: Property = Property(name="TotalAmount", type=IntegerType)
Bill.attributes={Bill_DoctorName, Bill_PId, Bill_BillDate, Bill_TotalAmount, Bill_BillId, Bill_PatientName, Bill_Did, Bill_BId}

# DoctorSchedule class attributes and methods
DoctorSchedule_DSid: Property = Property(name="DSid", type=IntegerType)
DoctorSchedule_DoctorId: Property = Property(name="DoctorId", type=StringType)
DoctorSchedule_AvailableDate: Property = Property(name="AvailableDate", type=StringType)
DoctorSchedule_AvailableTime: Property = Property(name="AvailableTime", type=StringType)
DoctorSchedule.attributes={DoctorSchedule_AvailableTime, DoctorSchedule_DSid, DoctorSchedule_DoctorId, DoctorSchedule_AvailableDate}

# DoctorServices class attributes and methods
DoctorServices_ServiceId: Property = Property(name="ServiceId", type=IntegerType)
DoctorServices_SId: Property = Property(name="SId", type=StringType)
DoctorServices_ServiceName: Property = Property(name="ServiceName", type=StringType)
DoctorServices_ServiceDetails: Property = Property(name="ServiceDetails", type=StringType)
DoctorServices_ServicePrice: Property = Property(name="ServicePrice", type=StringType)
DoctorServices.attributes={DoctorServices_ServiceId, DoctorServices_ServiceDetails, DoctorServices_ServiceName, DoctorServices_SId, DoctorServices_ServicePrice}

# Receptionist class attributes and methods
Receptionist_ReceptionistId: Property = Property(name="ReceptionistId", type=IntegerType)
Receptionist_RId: Property = Property(name="RId", type=StringType)
Receptionist_UserId: Property = Property(name="UserId", type=IntegerType)
Receptionist_ReceptionistName: Property = Property(name="ReceptionistName", type=StringType)
Receptionist_DateOfBirth: Property = Property(name="DateOfBirth", type=StringType)
Receptionist_Email: Property = Property(name="Email", type=StringType)
Receptionist_PhoneNumber: Property = Property(name="PhoneNumber", type=StringType)
Receptionist.attributes={Receptionist_UserId, Receptionist_DateOfBirth, Receptionist_PhoneNumber, Receptionist_Email, Receptionist_ReceptionistId, Receptionist_RId, Receptionist_ReceptionistName}

# Users class attributes and methods
Users_Id: Property = Property(name="Id", type=IntegerType)
Users_Email: Property = Property(name="Email", type=StringType)
Users_EmailConfirmed: Property = Property(name="EmailConfirmed", type=StringType)
Users_PasswordHash: Property = Property(name="PasswordHash", type=StringType)
Users_SecurityStamp: Property = Property(name="SecurityStamp", type=StringType)
Users_PhoneNumber: Property = Property(name="PhoneNumber", type=StringType)
Users_PhoneNumberConfirmed: Property = Property(name="PhoneNumberConfirmed", type=StringType)
Users_TwoFactorEnabled: Property = Property(name="TwoFactorEnabled", type=StringType)
Users_LockoutEndDateUtc: Property = Property(name="LockoutEndDateUtc", type=StringType)
Users_LockoutEnabled: Property = Property(name="LockoutEnabled", type=StringType)
Users_AccessFailedCount: Property = Property(name="AccessFailedCount", type=IntegerType)
Users_UserName: Property = Property(name="UserName", type=StringType)
Users.attributes={Users_Id, Users_PasswordHash, Users_UserName, Users_LockoutEndDateUtc, Users_PhoneNumber, Users_AccessFailedCount, Users_Email, Users_EmailConfirmed, Users_PhoneNumberConfirmed, Users_TwoFactorEnabled, Users_LockoutEnabled, Users_SecurityStamp}

# UserRoles class attributes and methods
UserRoles_Id: Property = Property(name="Id", type=IntegerType)
UserRoles_Name: Property = Property(name="Name", type=StringType)
UserRoles.attributes={UserRoles_Name, UserRoles_Id}

# UserwithRole class attributes and methods
UserwithRole_UserId: Property = Property(name="UserId", type=IntegerType)
UserwithRole_RoleId: Property = Property(name="RoleId", type=IntegerType)
UserwithRole.attributes={UserwithRole_UserId, UserwithRole_RoleId}

# Relationships
Appointment_Doctor: BinaryAssociation = BinaryAssociation(
    name="Appointment_Doctor",
    ends={
        Property(name="doctor0", type=Doctor, multiplicity=Multiplicity(0, 9999)),
        Property(name="appointment1", type=Appointment, multiplicity=Multiplicity(0, 9999))
    }
)
Doctor_DoctorSchedule: BinaryAssociation = BinaryAssociation(
    name="Doctor_DoctorSchedule",
    ends={
        Property(name="doctorSchedule2", type=DoctorSchedule, multiplicity=Multiplicity(0, 9999)),
        Property(name="doctor3", type=Doctor, multiplicity=Multiplicity(0, 9999))
    }
)
Doctor_Bill: BinaryAssociation = BinaryAssociation(
    name="Doctor_Bill",
    ends={
        Property(name="bill4", type=Bill, multiplicity=Multiplicity(0, 9999)),
        Property(name="doctor5", type=Doctor, multiplicity=Multiplicity(0, 9999))
    }
)
Patient_Bill: BinaryAssociation = BinaryAssociation(
    name="Patient_Bill",
    ends={
        Property(name="bill6", type=Bill, multiplicity=Multiplicity(0, 9999)),
        Property(name="patient7", type=Patient, multiplicity=Multiplicity(0, 9999))
    }
)
Patient_Appointment: BinaryAssociation = BinaryAssociation(
    name="Patient_Appointment",
    ends={
        Property(name="appointment8", type=Appointment, multiplicity=Multiplicity(0, 9999)),
        Property(name="patient9", type=Patient, multiplicity=Multiplicity(0, 9999))
    }
)
DoctorServices_Appointment: BinaryAssociation = BinaryAssociation(
    name="DoctorServices_Appointment",
    ends={
        Property(name="appointment10", type=Appointment, multiplicity=Multiplicity(0, 9999)),
        Property(name="doctorServices11", type=DoctorServices, multiplicity=Multiplicity(0, 9999))
    }
)
Users_UserwithRole: BinaryAssociation = BinaryAssociation(
    name="Users_UserwithRole",
    ends={
        Property(name="userwithRole12", type=UserwithRole, multiplicity=Multiplicity(0, 9999)),
        Property(name="users13", type=Users, multiplicity=Multiplicity(0, 9999))
    }
)
UserRoles_UserwithRole: BinaryAssociation = BinaryAssociation(
    name="UserRoles_UserwithRole",
    ends={
        Property(name="userwithRole14", type=UserwithRole, multiplicity=Multiplicity(0, 9999)),
        Property(name="userRoles15", type=UserRoles, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_7652ddce_1bad_4912_81cd_b9b44b933533",
    types={Patient, Appointment, Doctor, Bill, DoctorSchedule, DoctorServices, Receptionist, Users, UserRoles, UserwithRole},
    associations={Appointment_Doctor, Doctor_DoctorSchedule, Doctor_Bill, Patient_Bill, Patient_Appointment, DoctorServices_Appointment, Users_UserwithRole, UserRoles_UserwithRole},
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