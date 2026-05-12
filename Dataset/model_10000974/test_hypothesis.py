import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    UserwithRole,
    UserRoles,
    Users,
    Receptionist,
    DoctorServices,
    DoctorSchedule,
    Bill,
    Doctor,
    Appointment,
    Patient,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_userwithrole_is_not_abstract():
    assert not inspect.isabstract(UserwithRole)


def test_userwithrole_constructor_exists():
    assert callable(UserwithRole.__init__)


def test_userwithrole_constructor_args():
    sig = inspect.signature(UserwithRole.__init__)
    params = list(sig.parameters.keys())
    assert "RoleId" in params, "Missing parameter 'RoleId'"
    assert "UserId" in params, "Missing parameter 'UserId'"

def test_userwithrole_has_RoleId():
    assert hasattr(UserwithRole, "RoleId")
    descriptor = None
    for klass in UserwithRole.__mro__:
        if "RoleId" in klass.__dict__:
            descriptor = klass.__dict__["RoleId"]
            break
    assert isinstance(descriptor, property)

def test_userwithrole_has_UserId():
    assert hasattr(UserwithRole, "UserId")
    descriptor = None
    for klass in UserwithRole.__mro__:
        if "UserId" in klass.__dict__:
            descriptor = klass.__dict__["UserId"]
            break
    assert isinstance(descriptor, property)



def test_userroles_is_not_abstract():
    assert not inspect.isabstract(UserRoles)


def test_userroles_constructor_exists():
    assert callable(UserRoles.__init__)


def test_userroles_constructor_args():
    sig = inspect.signature(UserRoles.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Id" in params, "Missing parameter 'Id'"

def test_userroles_has_Name():
    assert hasattr(UserRoles, "Name")
    descriptor = None
    for klass in UserRoles.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_userroles_has_Id():
    assert hasattr(UserRoles, "Id")
    descriptor = None
    for klass in UserRoles.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
            break
    assert isinstance(descriptor, property)



def test_users_is_not_abstract():
    assert not inspect.isabstract(Users)


def test_users_constructor_exists():
    assert callable(Users.__init__)


def test_users_constructor_args():
    sig = inspect.signature(Users.__init__)
    params = list(sig.parameters.keys())
    assert "AccessFailedCount" in params, "Missing parameter 'AccessFailedCount'"
    assert "UserName" in params, "Missing parameter 'UserName'"
    assert "LockoutEnabled" in params, "Missing parameter 'LockoutEnabled'"
    assert "PasswordHash" in params, "Missing parameter 'PasswordHash'"
    assert "PhoneNumberConfirmed" in params, "Missing parameter 'PhoneNumberConfirmed'"
    assert "Id" in params, "Missing parameter 'Id'"
    assert "SecurityStamp" in params, "Missing parameter 'SecurityStamp'"
    assert "TwoFactorEnabled" in params, "Missing parameter 'TwoFactorEnabled'"
    assert "PhoneNumber" in params, "Missing parameter 'PhoneNumber'"
    assert "LockoutEndDateUtc" in params, "Missing parameter 'LockoutEndDateUtc'"
    assert "Email" in params, "Missing parameter 'Email'"
    assert "EmailConfirmed" in params, "Missing parameter 'EmailConfirmed'"

def test_users_has_AccessFailedCount():
    assert hasattr(Users, "AccessFailedCount")
    descriptor = None
    for klass in Users.__mro__:
        if "AccessFailedCount" in klass.__dict__:
            descriptor = klass.__dict__["AccessFailedCount"]
            break
    assert isinstance(descriptor, property)

def test_users_has_UserName():
    assert hasattr(Users, "UserName")
    descriptor = None
    for klass in Users.__mro__:
        if "UserName" in klass.__dict__:
            descriptor = klass.__dict__["UserName"]
            break
    assert isinstance(descriptor, property)

def test_users_has_LockoutEnabled():
    assert hasattr(Users, "LockoutEnabled")
    descriptor = None
    for klass in Users.__mro__:
        if "LockoutEnabled" in klass.__dict__:
            descriptor = klass.__dict__["LockoutEnabled"]
            break
    assert isinstance(descriptor, property)

def test_users_has_PasswordHash():
    assert hasattr(Users, "PasswordHash")
    descriptor = None
    for klass in Users.__mro__:
        if "PasswordHash" in klass.__dict__:
            descriptor = klass.__dict__["PasswordHash"]
            break
    assert isinstance(descriptor, property)

def test_users_has_PhoneNumberConfirmed():
    assert hasattr(Users, "PhoneNumberConfirmed")
    descriptor = None
    for klass in Users.__mro__:
        if "PhoneNumberConfirmed" in klass.__dict__:
            descriptor = klass.__dict__["PhoneNumberConfirmed"]
            break
    assert isinstance(descriptor, property)

def test_users_has_Id():
    assert hasattr(Users, "Id")
    descriptor = None
    for klass in Users.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
            break
    assert isinstance(descriptor, property)

def test_users_has_SecurityStamp():
    assert hasattr(Users, "SecurityStamp")
    descriptor = None
    for klass in Users.__mro__:
        if "SecurityStamp" in klass.__dict__:
            descriptor = klass.__dict__["SecurityStamp"]
            break
    assert isinstance(descriptor, property)

def test_users_has_TwoFactorEnabled():
    assert hasattr(Users, "TwoFactorEnabled")
    descriptor = None
    for klass in Users.__mro__:
        if "TwoFactorEnabled" in klass.__dict__:
            descriptor = klass.__dict__["TwoFactorEnabled"]
            break
    assert isinstance(descriptor, property)

def test_users_has_PhoneNumber():
    assert hasattr(Users, "PhoneNumber")
    descriptor = None
    for klass in Users.__mro__:
        if "PhoneNumber" in klass.__dict__:
            descriptor = klass.__dict__["PhoneNumber"]
            break
    assert isinstance(descriptor, property)

def test_users_has_LockoutEndDateUtc():
    assert hasattr(Users, "LockoutEndDateUtc")
    descriptor = None
    for klass in Users.__mro__:
        if "LockoutEndDateUtc" in klass.__dict__:
            descriptor = klass.__dict__["LockoutEndDateUtc"]
            break
    assert isinstance(descriptor, property)

def test_users_has_Email():
    assert hasattr(Users, "Email")
    descriptor = None
    for klass in Users.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
            break
    assert isinstance(descriptor, property)

def test_users_has_EmailConfirmed():
    assert hasattr(Users, "EmailConfirmed")
    descriptor = None
    for klass in Users.__mro__:
        if "EmailConfirmed" in klass.__dict__:
            descriptor = klass.__dict__["EmailConfirmed"]
            break
    assert isinstance(descriptor, property)



def test_receptionist_is_not_abstract():
    assert not inspect.isabstract(Receptionist)


def test_receptionist_constructor_exists():
    assert callable(Receptionist.__init__)


def test_receptionist_constructor_args():
    sig = inspect.signature(Receptionist.__init__)
    params = list(sig.parameters.keys())
    assert "UserId" in params, "Missing parameter 'UserId'"
    assert "DateOfBirth" in params, "Missing parameter 'DateOfBirth'"
    assert "PhoneNumber" in params, "Missing parameter 'PhoneNumber'"
    assert "Email" in params, "Missing parameter 'Email'"
    assert "RId" in params, "Missing parameter 'RId'"
    assert "ReceptionistId" in params, "Missing parameter 'ReceptionistId'"
    assert "ReceptionistName" in params, "Missing parameter 'ReceptionistName'"

def test_receptionist_has_UserId():
    assert hasattr(Receptionist, "UserId")
    descriptor = None
    for klass in Receptionist.__mro__:
        if "UserId" in klass.__dict__:
            descriptor = klass.__dict__["UserId"]
            break
    assert isinstance(descriptor, property)

def test_receptionist_has_DateOfBirth():
    assert hasattr(Receptionist, "DateOfBirth")
    descriptor = None
    for klass in Receptionist.__mro__:
        if "DateOfBirth" in klass.__dict__:
            descriptor = klass.__dict__["DateOfBirth"]
            break
    assert isinstance(descriptor, property)

def test_receptionist_has_PhoneNumber():
    assert hasattr(Receptionist, "PhoneNumber")
    descriptor = None
    for klass in Receptionist.__mro__:
        if "PhoneNumber" in klass.__dict__:
            descriptor = klass.__dict__["PhoneNumber"]
            break
    assert isinstance(descriptor, property)

def test_receptionist_has_Email():
    assert hasattr(Receptionist, "Email")
    descriptor = None
    for klass in Receptionist.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
            break
    assert isinstance(descriptor, property)

def test_receptionist_has_RId():
    assert hasattr(Receptionist, "RId")
    descriptor = None
    for klass in Receptionist.__mro__:
        if "RId" in klass.__dict__:
            descriptor = klass.__dict__["RId"]
            break
    assert isinstance(descriptor, property)

def test_receptionist_has_ReceptionistId():
    assert hasattr(Receptionist, "ReceptionistId")
    descriptor = None
    for klass in Receptionist.__mro__:
        if "ReceptionistId" in klass.__dict__:
            descriptor = klass.__dict__["ReceptionistId"]
            break
    assert isinstance(descriptor, property)

def test_receptionist_has_ReceptionistName():
    assert hasattr(Receptionist, "ReceptionistName")
    descriptor = None
    for klass in Receptionist.__mro__:
        if "ReceptionistName" in klass.__dict__:
            descriptor = klass.__dict__["ReceptionistName"]
            break
    assert isinstance(descriptor, property)



def test_doctorservices_is_not_abstract():
    assert not inspect.isabstract(DoctorServices)


def test_doctorservices_constructor_exists():
    assert callable(DoctorServices.__init__)


def test_doctorservices_constructor_args():
    sig = inspect.signature(DoctorServices.__init__)
    params = list(sig.parameters.keys())
    assert "ServicePrice" in params, "Missing parameter 'ServicePrice'"
    assert "ServiceId" in params, "Missing parameter 'ServiceId'"
    assert "SId" in params, "Missing parameter 'SId'"
    assert "ServiceDetails" in params, "Missing parameter 'ServiceDetails'"
    assert "ServiceName" in params, "Missing parameter 'ServiceName'"

def test_doctorservices_has_ServicePrice():
    assert hasattr(DoctorServices, "ServicePrice")
    descriptor = None
    for klass in DoctorServices.__mro__:
        if "ServicePrice" in klass.__dict__:
            descriptor = klass.__dict__["ServicePrice"]
            break
    assert isinstance(descriptor, property)

def test_doctorservices_has_ServiceId():
    assert hasattr(DoctorServices, "ServiceId")
    descriptor = None
    for klass in DoctorServices.__mro__:
        if "ServiceId" in klass.__dict__:
            descriptor = klass.__dict__["ServiceId"]
            break
    assert isinstance(descriptor, property)

def test_doctorservices_has_SId():
    assert hasattr(DoctorServices, "SId")
    descriptor = None
    for klass in DoctorServices.__mro__:
        if "SId" in klass.__dict__:
            descriptor = klass.__dict__["SId"]
            break
    assert isinstance(descriptor, property)

def test_doctorservices_has_ServiceDetails():
    assert hasattr(DoctorServices, "ServiceDetails")
    descriptor = None
    for klass in DoctorServices.__mro__:
        if "ServiceDetails" in klass.__dict__:
            descriptor = klass.__dict__["ServiceDetails"]
            break
    assert isinstance(descriptor, property)

def test_doctorservices_has_ServiceName():
    assert hasattr(DoctorServices, "ServiceName")
    descriptor = None
    for klass in DoctorServices.__mro__:
        if "ServiceName" in klass.__dict__:
            descriptor = klass.__dict__["ServiceName"]
            break
    assert isinstance(descriptor, property)



def test_doctorschedule_is_not_abstract():
    assert not inspect.isabstract(DoctorSchedule)


def test_doctorschedule_constructor_exists():
    assert callable(DoctorSchedule.__init__)


def test_doctorschedule_constructor_args():
    sig = inspect.signature(DoctorSchedule.__init__)
    params = list(sig.parameters.keys())
    assert "DoctorId" in params, "Missing parameter 'DoctorId'"
    assert "DSid" in params, "Missing parameter 'DSid'"
    assert "AvailableTime" in params, "Missing parameter 'AvailableTime'"
    assert "AvailableDate" in params, "Missing parameter 'AvailableDate'"

def test_doctorschedule_has_DoctorId():
    assert hasattr(DoctorSchedule, "DoctorId")
    descriptor = None
    for klass in DoctorSchedule.__mro__:
        if "DoctorId" in klass.__dict__:
            descriptor = klass.__dict__["DoctorId"]
            break
    assert isinstance(descriptor, property)

def test_doctorschedule_has_DSid():
    assert hasattr(DoctorSchedule, "DSid")
    descriptor = None
    for klass in DoctorSchedule.__mro__:
        if "DSid" in klass.__dict__:
            descriptor = klass.__dict__["DSid"]
            break
    assert isinstance(descriptor, property)

def test_doctorschedule_has_AvailableTime():
    assert hasattr(DoctorSchedule, "AvailableTime")
    descriptor = None
    for klass in DoctorSchedule.__mro__:
        if "AvailableTime" in klass.__dict__:
            descriptor = klass.__dict__["AvailableTime"]
            break
    assert isinstance(descriptor, property)

def test_doctorschedule_has_AvailableDate():
    assert hasattr(DoctorSchedule, "AvailableDate")
    descriptor = None
    for klass in DoctorSchedule.__mro__:
        if "AvailableDate" in klass.__dict__:
            descriptor = klass.__dict__["AvailableDate"]
            break
    assert isinstance(descriptor, property)



def test_bill_is_not_abstract():
    assert not inspect.isabstract(Bill)


def test_bill_constructor_exists():
    assert callable(Bill.__init__)


def test_bill_constructor_args():
    sig = inspect.signature(Bill.__init__)
    params = list(sig.parameters.keys())
    assert "BillDate" in params, "Missing parameter 'BillDate'"
    assert "DoctorName" in params, "Missing parameter 'DoctorName'"
    assert "TotalAmount" in params, "Missing parameter 'TotalAmount'"
    assert "BId" in params, "Missing parameter 'BId'"
    assert "BillId" in params, "Missing parameter 'BillId'"
    assert "PId" in params, "Missing parameter 'PId'"
    assert "Did" in params, "Missing parameter 'Did'"
    assert "PatientName" in params, "Missing parameter 'PatientName'"

def test_bill_has_BillDate():
    assert hasattr(Bill, "BillDate")
    descriptor = None
    for klass in Bill.__mro__:
        if "BillDate" in klass.__dict__:
            descriptor = klass.__dict__["BillDate"]
            break
    assert isinstance(descriptor, property)

def test_bill_has_DoctorName():
    assert hasattr(Bill, "DoctorName")
    descriptor = None
    for klass in Bill.__mro__:
        if "DoctorName" in klass.__dict__:
            descriptor = klass.__dict__["DoctorName"]
            break
    assert isinstance(descriptor, property)

def test_bill_has_TotalAmount():
    assert hasattr(Bill, "TotalAmount")
    descriptor = None
    for klass in Bill.__mro__:
        if "TotalAmount" in klass.__dict__:
            descriptor = klass.__dict__["TotalAmount"]
            break
    assert isinstance(descriptor, property)

def test_bill_has_BId():
    assert hasattr(Bill, "BId")
    descriptor = None
    for klass in Bill.__mro__:
        if "BId" in klass.__dict__:
            descriptor = klass.__dict__["BId"]
            break
    assert isinstance(descriptor, property)

def test_bill_has_BillId():
    assert hasattr(Bill, "BillId")
    descriptor = None
    for klass in Bill.__mro__:
        if "BillId" in klass.__dict__:
            descriptor = klass.__dict__["BillId"]
            break
    assert isinstance(descriptor, property)

def test_bill_has_PId():
    assert hasattr(Bill, "PId")
    descriptor = None
    for klass in Bill.__mro__:
        if "PId" in klass.__dict__:
            descriptor = klass.__dict__["PId"]
            break
    assert isinstance(descriptor, property)

def test_bill_has_Did():
    assert hasattr(Bill, "Did")
    descriptor = None
    for klass in Bill.__mro__:
        if "Did" in klass.__dict__:
            descriptor = klass.__dict__["Did"]
            break
    assert isinstance(descriptor, property)

def test_bill_has_PatientName():
    assert hasattr(Bill, "PatientName")
    descriptor = None
    for klass in Bill.__mro__:
        if "PatientName" in klass.__dict__:
            descriptor = klass.__dict__["PatientName"]
            break
    assert isinstance(descriptor, property)



def test_doctor_is_not_abstract():
    assert not inspect.isabstract(Doctor)


def test_doctor_constructor_exists():
    assert callable(Doctor.__init__)


def test_doctor_constructor_args():
    sig = inspect.signature(Doctor.__init__)
    params = list(sig.parameters.keys())
    assert "Email" in params, "Missing parameter 'Email'"
    assert "Speciality" in params, "Missing parameter 'Speciality'"
    assert "PhoneNumber" in params, "Missing parameter 'PhoneNumber'"
    assert "UserId" in params, "Missing parameter 'UserId'"
    assert "DId" in params, "Missing parameter 'DId'"
    assert "DoctorName" in params, "Missing parameter 'DoctorName'"
    assert "DoctorId" in params, "Missing parameter 'DoctorId'"
    assert "DateOfBirth" in params, "Missing parameter 'DateOfBirth'"

def test_doctor_has_Email():
    assert hasattr(Doctor, "Email")
    descriptor = None
    for klass in Doctor.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_Speciality():
    assert hasattr(Doctor, "Speciality")
    descriptor = None
    for klass in Doctor.__mro__:
        if "Speciality" in klass.__dict__:
            descriptor = klass.__dict__["Speciality"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_PhoneNumber():
    assert hasattr(Doctor, "PhoneNumber")
    descriptor = None
    for klass in Doctor.__mro__:
        if "PhoneNumber" in klass.__dict__:
            descriptor = klass.__dict__["PhoneNumber"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_UserId():
    assert hasattr(Doctor, "UserId")
    descriptor = None
    for klass in Doctor.__mro__:
        if "UserId" in klass.__dict__:
            descriptor = klass.__dict__["UserId"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_DId():
    assert hasattr(Doctor, "DId")
    descriptor = None
    for klass in Doctor.__mro__:
        if "DId" in klass.__dict__:
            descriptor = klass.__dict__["DId"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_DoctorName():
    assert hasattr(Doctor, "DoctorName")
    descriptor = None
    for klass in Doctor.__mro__:
        if "DoctorName" in klass.__dict__:
            descriptor = klass.__dict__["DoctorName"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_DoctorId():
    assert hasattr(Doctor, "DoctorId")
    descriptor = None
    for klass in Doctor.__mro__:
        if "DoctorId" in klass.__dict__:
            descriptor = klass.__dict__["DoctorId"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_DateOfBirth():
    assert hasattr(Doctor, "DateOfBirth")
    descriptor = None
    for klass in Doctor.__mro__:
        if "DateOfBirth" in klass.__dict__:
            descriptor = klass.__dict__["DateOfBirth"]
            break
    assert isinstance(descriptor, property)



def test_appointment_is_not_abstract():
    assert not inspect.isabstract(Appointment)


def test_appointment_constructor_exists():
    assert callable(Appointment.__init__)


def test_appointment_constructor_args():
    sig = inspect.signature(Appointment.__init__)
    params = list(sig.parameters.keys())
    assert "DoctorName" in params, "Missing parameter 'DoctorName'"
    assert "PatientId" in params, "Missing parameter 'PatientId'"
    assert "AppointmentId" in params, "Missing parameter 'AppointmentId'"
    assert "PatientName" in params, "Missing parameter 'PatientName'"
    assert "AppointmentTime" in params, "Missing parameter 'AppointmentTime'"
    assert "ServiceId" in params, "Missing parameter 'ServiceId'"
    assert "AppointmentStatus" in params, "Missing parameter 'AppointmentStatus'"
    assert "AppointmentDate" in params, "Missing parameter 'AppointmentDate'"
    assert "Aid" in params, "Missing parameter 'Aid'"
    assert "Did" in params, "Missing parameter 'Did'"
    assert "Reason" in params, "Missing parameter 'Reason'"

def test_appointment_has_DoctorName():
    assert hasattr(Appointment, "DoctorName")
    descriptor = None
    for klass in Appointment.__mro__:
        if "DoctorName" in klass.__dict__:
            descriptor = klass.__dict__["DoctorName"]
            break
    assert isinstance(descriptor, property)

def test_appointment_has_PatientId():
    assert hasattr(Appointment, "PatientId")
    descriptor = None
    for klass in Appointment.__mro__:
        if "PatientId" in klass.__dict__:
            descriptor = klass.__dict__["PatientId"]
            break
    assert isinstance(descriptor, property)

def test_appointment_has_AppointmentId():
    assert hasattr(Appointment, "AppointmentId")
    descriptor = None
    for klass in Appointment.__mro__:
        if "AppointmentId" in klass.__dict__:
            descriptor = klass.__dict__["AppointmentId"]
            break
    assert isinstance(descriptor, property)

def test_appointment_has_PatientName():
    assert hasattr(Appointment, "PatientName")
    descriptor = None
    for klass in Appointment.__mro__:
        if "PatientName" in klass.__dict__:
            descriptor = klass.__dict__["PatientName"]
            break
    assert isinstance(descriptor, property)

def test_appointment_has_AppointmentTime():
    assert hasattr(Appointment, "AppointmentTime")
    descriptor = None
    for klass in Appointment.__mro__:
        if "AppointmentTime" in klass.__dict__:
            descriptor = klass.__dict__["AppointmentTime"]
            break
    assert isinstance(descriptor, property)

def test_appointment_has_ServiceId():
    assert hasattr(Appointment, "ServiceId")
    descriptor = None
    for klass in Appointment.__mro__:
        if "ServiceId" in klass.__dict__:
            descriptor = klass.__dict__["ServiceId"]
            break
    assert isinstance(descriptor, property)

def test_appointment_has_AppointmentStatus():
    assert hasattr(Appointment, "AppointmentStatus")
    descriptor = None
    for klass in Appointment.__mro__:
        if "AppointmentStatus" in klass.__dict__:
            descriptor = klass.__dict__["AppointmentStatus"]
            break
    assert isinstance(descriptor, property)

def test_appointment_has_AppointmentDate():
    assert hasattr(Appointment, "AppointmentDate")
    descriptor = None
    for klass in Appointment.__mro__:
        if "AppointmentDate" in klass.__dict__:
            descriptor = klass.__dict__["AppointmentDate"]
            break
    assert isinstance(descriptor, property)

def test_appointment_has_Aid():
    assert hasattr(Appointment, "Aid")
    descriptor = None
    for klass in Appointment.__mro__:
        if "Aid" in klass.__dict__:
            descriptor = klass.__dict__["Aid"]
            break
    assert isinstance(descriptor, property)

def test_appointment_has_Did():
    assert hasattr(Appointment, "Did")
    descriptor = None
    for klass in Appointment.__mro__:
        if "Did" in klass.__dict__:
            descriptor = klass.__dict__["Did"]
            break
    assert isinstance(descriptor, property)

def test_appointment_has_Reason():
    assert hasattr(Appointment, "Reason")
    descriptor = None
    for klass in Appointment.__mro__:
        if "Reason" in klass.__dict__:
            descriptor = klass.__dict__["Reason"]
            break
    assert isinstance(descriptor, property)



def test_patient_is_not_abstract():
    assert not inspect.isabstract(Patient)


def test_patient_constructor_exists():
    assert callable(Patient.__init__)


def test_patient_constructor_args():
    sig = inspect.signature(Patient.__init__)
    params = list(sig.parameters.keys())
    assert "StreetAddress" in params, "Missing parameter 'StreetAddress'"
    assert "IsEmailConfirmed" in params, "Missing parameter 'IsEmailConfirmed'"
    assert "IsPhoneNumberConfirmed" in params, "Missing parameter 'IsPhoneNumberConfirmed'"
    assert "UserId" in params, "Missing parameter 'UserId'"
    assert "State" in params, "Missing parameter 'State'"
    assert "PatientId" in params, "Missing parameter 'PatientId'"
    assert "activationcode" in params, "Missing parameter 'activationcode'"
    assert "City" in params, "Missing parameter 'City'"
    assert "DateOfBirth" in params, "Missing parameter 'DateOfBirth'"
    assert "FirstName" in params, "Missing parameter 'FirstName'"
    assert "PhoneNumber" in params, "Missing parameter 'PhoneNumber'"
    assert "Email" in params, "Missing parameter 'Email'"
    assert "LastName" in params, "Missing parameter 'LastName'"
    assert "PId" in params, "Missing parameter 'PId'"
    assert "ZipCode" in params, "Missing parameter 'ZipCode'"

def test_patient_has_StreetAddress():
    assert hasattr(Patient, "StreetAddress")
    descriptor = None
    for klass in Patient.__mro__:
        if "StreetAddress" in klass.__dict__:
            descriptor = klass.__dict__["StreetAddress"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_IsEmailConfirmed():
    assert hasattr(Patient, "IsEmailConfirmed")
    descriptor = None
    for klass in Patient.__mro__:
        if "IsEmailConfirmed" in klass.__dict__:
            descriptor = klass.__dict__["IsEmailConfirmed"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_IsPhoneNumberConfirmed():
    assert hasattr(Patient, "IsPhoneNumberConfirmed")
    descriptor = None
    for klass in Patient.__mro__:
        if "IsPhoneNumberConfirmed" in klass.__dict__:
            descriptor = klass.__dict__["IsPhoneNumberConfirmed"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_UserId():
    assert hasattr(Patient, "UserId")
    descriptor = None
    for klass in Patient.__mro__:
        if "UserId" in klass.__dict__:
            descriptor = klass.__dict__["UserId"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_State():
    assert hasattr(Patient, "State")
    descriptor = None
    for klass in Patient.__mro__:
        if "State" in klass.__dict__:
            descriptor = klass.__dict__["State"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_PatientId():
    assert hasattr(Patient, "PatientId")
    descriptor = None
    for klass in Patient.__mro__:
        if "PatientId" in klass.__dict__:
            descriptor = klass.__dict__["PatientId"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_activationcode():
    assert hasattr(Patient, "activationcode")
    descriptor = None
    for klass in Patient.__mro__:
        if "activationcode" in klass.__dict__:
            descriptor = klass.__dict__["activationcode"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_City():
    assert hasattr(Patient, "City")
    descriptor = None
    for klass in Patient.__mro__:
        if "City" in klass.__dict__:
            descriptor = klass.__dict__["City"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_DateOfBirth():
    assert hasattr(Patient, "DateOfBirth")
    descriptor = None
    for klass in Patient.__mro__:
        if "DateOfBirth" in klass.__dict__:
            descriptor = klass.__dict__["DateOfBirth"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_FirstName():
    assert hasattr(Patient, "FirstName")
    descriptor = None
    for klass in Patient.__mro__:
        if "FirstName" in klass.__dict__:
            descriptor = klass.__dict__["FirstName"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_PhoneNumber():
    assert hasattr(Patient, "PhoneNumber")
    descriptor = None
    for klass in Patient.__mro__:
        if "PhoneNumber" in klass.__dict__:
            descriptor = klass.__dict__["PhoneNumber"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_Email():
    assert hasattr(Patient, "Email")
    descriptor = None
    for klass in Patient.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_LastName():
    assert hasattr(Patient, "LastName")
    descriptor = None
    for klass in Patient.__mro__:
        if "LastName" in klass.__dict__:
            descriptor = klass.__dict__["LastName"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_PId():
    assert hasattr(Patient, "PId")
    descriptor = None
    for klass in Patient.__mro__:
        if "PId" in klass.__dict__:
            descriptor = klass.__dict__["PId"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_ZipCode():
    assert hasattr(Patient, "ZipCode")
    descriptor = None
    for klass in Patient.__mro__:
        if "ZipCode" in klass.__dict__:
            descriptor = klass.__dict__["ZipCode"]
            break
    assert isinstance(descriptor, property)


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
UserwithRole_strategy = st.builds(
    UserwithRole,
    RoleId=
        st.integers(),
    UserId=
        st.integers()
)
UserRoles_strategy = st.builds(
    UserRoles,
    Name=
        safe_text,
    Id=
        st.integers()
)
Users_strategy = st.builds(
    Users,
    AccessFailedCount=
        st.integers(),
    UserName=
        safe_text,
    LockoutEnabled=
        safe_text,
    PasswordHash=
        safe_text,
    PhoneNumberConfirmed=
        safe_text,
    Id=
        st.integers(),
    SecurityStamp=
        safe_text,
    TwoFactorEnabled=
        safe_text,
    PhoneNumber=
        safe_text,
    LockoutEndDateUtc=
        safe_text,
    Email=
        safe_text,
    EmailConfirmed=
        safe_text
)
Receptionist_strategy = st.builds(
    Receptionist,
    UserId=
        st.integers(),
    DateOfBirth=
        safe_text,
    PhoneNumber=
        safe_text,
    Email=
        safe_text,
    RId=
        safe_text,
    ReceptionistId=
        st.integers(),
    ReceptionistName=
        safe_text
)
DoctorServices_strategy = st.builds(
    DoctorServices,
    ServicePrice=
        safe_text,
    ServiceId=
        st.integers(),
    SId=
        safe_text,
    ServiceDetails=
        safe_text,
    ServiceName=
        safe_text
)
DoctorSchedule_strategy = st.builds(
    DoctorSchedule,
    DoctorId=
        safe_text,
    DSid=
        st.integers(),
    AvailableTime=
        safe_text,
    AvailableDate=
        safe_text
)
Bill_strategy = st.builds(
    Bill,
    BillDate=
        safe_text,
    DoctorName=
        safe_text,
    TotalAmount=
        st.integers(),
    BId=
        safe_text,
    BillId=
        st.integers(),
    PId=
        st.integers(),
    Did=
        st.integers(),
    PatientName=
        safe_text
)
Doctor_strategy = st.builds(
    Doctor,
    Email=
        safe_text,
    Speciality=
        safe_text,
    PhoneNumber=
        safe_text,
    UserId=
        st.integers(),
    DId=
        safe_text,
    DoctorName=
        safe_text,
    DoctorId=
        st.integers(),
    DateOfBirth=
        safe_text
)
Appointment_strategy = st.builds(
    Appointment,
    DoctorName=
        safe_text,
    PatientId=
        st.integers(),
    AppointmentId=
        st.integers(),
    PatientName=
        safe_text,
    AppointmentTime=
        safe_text,
    ServiceId=
        st.integers(),
    AppointmentStatus=
        safe_text,
    AppointmentDate=
        safe_text,
    Aid=
        safe_text,
    Did=
        st.integers(),
    Reason=
        safe_text
)
Patient_strategy = st.builds(
    Patient,
    StreetAddress=
        safe_text,
    IsEmailConfirmed=
        safe_text,
    IsPhoneNumberConfirmed=
        safe_text,
    UserId=
        st.integers(),
    State=
        safe_text,
    PatientId=
        st.integers(),
    activationcode=
        safe_text,
    City=
        safe_text,
    DateOfBirth=
        safe_text,
    FirstName=
        safe_text,
    PhoneNumber=
        safe_text,
    Email=
        safe_text,
    LastName=
        safe_text,
    PId=
        safe_text,
    ZipCode=
        safe_text
)

@given(instance=UserwithRole_strategy)
@settings(max_examples=50)
def test_userwithrole_instantiation(instance):
    assert isinstance(instance, UserwithRole)



@given(instance=UserwithRole_strategy)
def test_userwithrole_RoleId_setter(instance):
    original = instance.RoleId
    instance.RoleId = original
    assert instance.RoleId == original



@given(instance=UserwithRole_strategy)
def test_userwithrole_UserId_setter(instance):
    original = instance.UserId
    instance.UserId = original
    assert instance.UserId == original

@given(instance=UserRoles_strategy)
@settings(max_examples=50)
def test_userroles_instantiation(instance):
    assert isinstance(instance, UserRoles)



@given(instance=UserRoles_strategy)
def test_userroles_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=UserRoles_strategy)
def test_userroles_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original

@given(instance=Users_strategy)
@settings(max_examples=50)
def test_users_instantiation(instance):
    assert isinstance(instance, Users)



@given(instance=Users_strategy)
def test_users_AccessFailedCount_setter(instance):
    original = instance.AccessFailedCount
    instance.AccessFailedCount = original
    assert instance.AccessFailedCount == original



@given(instance=Users_strategy)
def test_users_UserName_setter(instance):
    original = instance.UserName
    instance.UserName = original
    assert instance.UserName == original



@given(instance=Users_strategy)
def test_users_LockoutEnabled_setter(instance):
    original = instance.LockoutEnabled
    instance.LockoutEnabled = original
    assert instance.LockoutEnabled == original



@given(instance=Users_strategy)
def test_users_PasswordHash_setter(instance):
    original = instance.PasswordHash
    instance.PasswordHash = original
    assert instance.PasswordHash == original



@given(instance=Users_strategy)
def test_users_PhoneNumberConfirmed_setter(instance):
    original = instance.PhoneNumberConfirmed
    instance.PhoneNumberConfirmed = original
    assert instance.PhoneNumberConfirmed == original



@given(instance=Users_strategy)
def test_users_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original



@given(instance=Users_strategy)
def test_users_SecurityStamp_setter(instance):
    original = instance.SecurityStamp
    instance.SecurityStamp = original
    assert instance.SecurityStamp == original



@given(instance=Users_strategy)
def test_users_TwoFactorEnabled_setter(instance):
    original = instance.TwoFactorEnabled
    instance.TwoFactorEnabled = original
    assert instance.TwoFactorEnabled == original



@given(instance=Users_strategy)
def test_users_PhoneNumber_setter(instance):
    original = instance.PhoneNumber
    instance.PhoneNumber = original
    assert instance.PhoneNumber == original



@given(instance=Users_strategy)
def test_users_LockoutEndDateUtc_setter(instance):
    original = instance.LockoutEndDateUtc
    instance.LockoutEndDateUtc = original
    assert instance.LockoutEndDateUtc == original



@given(instance=Users_strategy)
def test_users_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=Users_strategy)
def test_users_EmailConfirmed_setter(instance):
    original = instance.EmailConfirmed
    instance.EmailConfirmed = original
    assert instance.EmailConfirmed == original

@given(instance=Receptionist_strategy)
@settings(max_examples=50)
def test_receptionist_instantiation(instance):
    assert isinstance(instance, Receptionist)



@given(instance=Receptionist_strategy)
def test_receptionist_UserId_setter(instance):
    original = instance.UserId
    instance.UserId = original
    assert instance.UserId == original



@given(instance=Receptionist_strategy)
def test_receptionist_DateOfBirth_setter(instance):
    original = instance.DateOfBirth
    instance.DateOfBirth = original
    assert instance.DateOfBirth == original



@given(instance=Receptionist_strategy)
def test_receptionist_PhoneNumber_setter(instance):
    original = instance.PhoneNumber
    instance.PhoneNumber = original
    assert instance.PhoneNumber == original



@given(instance=Receptionist_strategy)
def test_receptionist_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=Receptionist_strategy)
def test_receptionist_RId_setter(instance):
    original = instance.RId
    instance.RId = original
    assert instance.RId == original



@given(instance=Receptionist_strategy)
def test_receptionist_ReceptionistId_setter(instance):
    original = instance.ReceptionistId
    instance.ReceptionistId = original
    assert instance.ReceptionistId == original



@given(instance=Receptionist_strategy)
def test_receptionist_ReceptionistName_setter(instance):
    original = instance.ReceptionistName
    instance.ReceptionistName = original
    assert instance.ReceptionistName == original

@given(instance=DoctorServices_strategy)
@settings(max_examples=50)
def test_doctorservices_instantiation(instance):
    assert isinstance(instance, DoctorServices)



@given(instance=DoctorServices_strategy)
def test_doctorservices_ServicePrice_setter(instance):
    original = instance.ServicePrice
    instance.ServicePrice = original
    assert instance.ServicePrice == original



@given(instance=DoctorServices_strategy)
def test_doctorservices_ServiceId_setter(instance):
    original = instance.ServiceId
    instance.ServiceId = original
    assert instance.ServiceId == original



@given(instance=DoctorServices_strategy)
def test_doctorservices_SId_setter(instance):
    original = instance.SId
    instance.SId = original
    assert instance.SId == original



@given(instance=DoctorServices_strategy)
def test_doctorservices_ServiceDetails_setter(instance):
    original = instance.ServiceDetails
    instance.ServiceDetails = original
    assert instance.ServiceDetails == original



@given(instance=DoctorServices_strategy)
def test_doctorservices_ServiceName_setter(instance):
    original = instance.ServiceName
    instance.ServiceName = original
    assert instance.ServiceName == original

@given(instance=DoctorSchedule_strategy)
@settings(max_examples=50)
def test_doctorschedule_instantiation(instance):
    assert isinstance(instance, DoctorSchedule)



@given(instance=DoctorSchedule_strategy)
def test_doctorschedule_DoctorId_setter(instance):
    original = instance.DoctorId
    instance.DoctorId = original
    assert instance.DoctorId == original



@given(instance=DoctorSchedule_strategy)
def test_doctorschedule_DSid_setter(instance):
    original = instance.DSid
    instance.DSid = original
    assert instance.DSid == original



@given(instance=DoctorSchedule_strategy)
def test_doctorschedule_AvailableTime_setter(instance):
    original = instance.AvailableTime
    instance.AvailableTime = original
    assert instance.AvailableTime == original



@given(instance=DoctorSchedule_strategy)
def test_doctorschedule_AvailableDate_setter(instance):
    original = instance.AvailableDate
    instance.AvailableDate = original
    assert instance.AvailableDate == original

@given(instance=Bill_strategy)
@settings(max_examples=50)
def test_bill_instantiation(instance):
    assert isinstance(instance, Bill)



@given(instance=Bill_strategy)
def test_bill_BillDate_setter(instance):
    original = instance.BillDate
    instance.BillDate = original
    assert instance.BillDate == original



@given(instance=Bill_strategy)
def test_bill_DoctorName_setter(instance):
    original = instance.DoctorName
    instance.DoctorName = original
    assert instance.DoctorName == original



@given(instance=Bill_strategy)
def test_bill_TotalAmount_setter(instance):
    original = instance.TotalAmount
    instance.TotalAmount = original
    assert instance.TotalAmount == original



@given(instance=Bill_strategy)
def test_bill_BId_setter(instance):
    original = instance.BId
    instance.BId = original
    assert instance.BId == original



@given(instance=Bill_strategy)
def test_bill_BillId_setter(instance):
    original = instance.BillId
    instance.BillId = original
    assert instance.BillId == original



@given(instance=Bill_strategy)
def test_bill_PId_setter(instance):
    original = instance.PId
    instance.PId = original
    assert instance.PId == original



@given(instance=Bill_strategy)
def test_bill_Did_setter(instance):
    original = instance.Did
    instance.Did = original
    assert instance.Did == original



@given(instance=Bill_strategy)
def test_bill_PatientName_setter(instance):
    original = instance.PatientName
    instance.PatientName = original
    assert instance.PatientName == original

@given(instance=Doctor_strategy)
@settings(max_examples=50)
def test_doctor_instantiation(instance):
    assert isinstance(instance, Doctor)



@given(instance=Doctor_strategy)
def test_doctor_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=Doctor_strategy)
def test_doctor_Speciality_setter(instance):
    original = instance.Speciality
    instance.Speciality = original
    assert instance.Speciality == original



@given(instance=Doctor_strategy)
def test_doctor_PhoneNumber_setter(instance):
    original = instance.PhoneNumber
    instance.PhoneNumber = original
    assert instance.PhoneNumber == original



@given(instance=Doctor_strategy)
def test_doctor_UserId_setter(instance):
    original = instance.UserId
    instance.UserId = original
    assert instance.UserId == original



@given(instance=Doctor_strategy)
def test_doctor_DId_setter(instance):
    original = instance.DId
    instance.DId = original
    assert instance.DId == original



@given(instance=Doctor_strategy)
def test_doctor_DoctorName_setter(instance):
    original = instance.DoctorName
    instance.DoctorName = original
    assert instance.DoctorName == original



@given(instance=Doctor_strategy)
def test_doctor_DoctorId_setter(instance):
    original = instance.DoctorId
    instance.DoctorId = original
    assert instance.DoctorId == original



@given(instance=Doctor_strategy)
def test_doctor_DateOfBirth_setter(instance):
    original = instance.DateOfBirth
    instance.DateOfBirth = original
    assert instance.DateOfBirth == original

@given(instance=Appointment_strategy)
@settings(max_examples=50)
def test_appointment_instantiation(instance):
    assert isinstance(instance, Appointment)



@given(instance=Appointment_strategy)
def test_appointment_DoctorName_setter(instance):
    original = instance.DoctorName
    instance.DoctorName = original
    assert instance.DoctorName == original



@given(instance=Appointment_strategy)
def test_appointment_PatientId_setter(instance):
    original = instance.PatientId
    instance.PatientId = original
    assert instance.PatientId == original



@given(instance=Appointment_strategy)
def test_appointment_AppointmentId_setter(instance):
    original = instance.AppointmentId
    instance.AppointmentId = original
    assert instance.AppointmentId == original



@given(instance=Appointment_strategy)
def test_appointment_PatientName_setter(instance):
    original = instance.PatientName
    instance.PatientName = original
    assert instance.PatientName == original



@given(instance=Appointment_strategy)
def test_appointment_AppointmentTime_setter(instance):
    original = instance.AppointmentTime
    instance.AppointmentTime = original
    assert instance.AppointmentTime == original



@given(instance=Appointment_strategy)
def test_appointment_ServiceId_setter(instance):
    original = instance.ServiceId
    instance.ServiceId = original
    assert instance.ServiceId == original



@given(instance=Appointment_strategy)
def test_appointment_AppointmentStatus_setter(instance):
    original = instance.AppointmentStatus
    instance.AppointmentStatus = original
    assert instance.AppointmentStatus == original



@given(instance=Appointment_strategy)
def test_appointment_AppointmentDate_setter(instance):
    original = instance.AppointmentDate
    instance.AppointmentDate = original
    assert instance.AppointmentDate == original



@given(instance=Appointment_strategy)
def test_appointment_Aid_setter(instance):
    original = instance.Aid
    instance.Aid = original
    assert instance.Aid == original



@given(instance=Appointment_strategy)
def test_appointment_Did_setter(instance):
    original = instance.Did
    instance.Did = original
    assert instance.Did == original



@given(instance=Appointment_strategy)
def test_appointment_Reason_setter(instance):
    original = instance.Reason
    instance.Reason = original
    assert instance.Reason == original

@given(instance=Patient_strategy)
@settings(max_examples=50)
def test_patient_instantiation(instance):
    assert isinstance(instance, Patient)



@given(instance=Patient_strategy)
def test_patient_StreetAddress_setter(instance):
    original = instance.StreetAddress
    instance.StreetAddress = original
    assert instance.StreetAddress == original



@given(instance=Patient_strategy)
def test_patient_IsEmailConfirmed_setter(instance):
    original = instance.IsEmailConfirmed
    instance.IsEmailConfirmed = original
    assert instance.IsEmailConfirmed == original



@given(instance=Patient_strategy)
def test_patient_IsPhoneNumberConfirmed_setter(instance):
    original = instance.IsPhoneNumberConfirmed
    instance.IsPhoneNumberConfirmed = original
    assert instance.IsPhoneNumberConfirmed == original



@given(instance=Patient_strategy)
def test_patient_UserId_setter(instance):
    original = instance.UserId
    instance.UserId = original
    assert instance.UserId == original



@given(instance=Patient_strategy)
def test_patient_State_setter(instance):
    original = instance.State
    instance.State = original
    assert instance.State == original



@given(instance=Patient_strategy)
def test_patient_PatientId_setter(instance):
    original = instance.PatientId
    instance.PatientId = original
    assert instance.PatientId == original



@given(instance=Patient_strategy)
def test_patient_activationcode_setter(instance):
    original = instance.activationcode
    instance.activationcode = original
    assert instance.activationcode == original



@given(instance=Patient_strategy)
def test_patient_City_setter(instance):
    original = instance.City
    instance.City = original
    assert instance.City == original



@given(instance=Patient_strategy)
def test_patient_DateOfBirth_setter(instance):
    original = instance.DateOfBirth
    instance.DateOfBirth = original
    assert instance.DateOfBirth == original



@given(instance=Patient_strategy)
def test_patient_FirstName_setter(instance):
    original = instance.FirstName
    instance.FirstName = original
    assert instance.FirstName == original



@given(instance=Patient_strategy)
def test_patient_PhoneNumber_setter(instance):
    original = instance.PhoneNumber
    instance.PhoneNumber = original
    assert instance.PhoneNumber == original



@given(instance=Patient_strategy)
def test_patient_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=Patient_strategy)
def test_patient_LastName_setter(instance):
    original = instance.LastName
    instance.LastName = original
    assert instance.LastName == original



@given(instance=Patient_strategy)
def test_patient_PId_setter(instance):
    original = instance.PId
    instance.PId = original
    assert instance.PId == original



@given(instance=Patient_strategy)
def test_patient_ZipCode_setter(instance):
    original = instance.ZipCode
    instance.ZipCode = original
    assert instance.ZipCode == original
